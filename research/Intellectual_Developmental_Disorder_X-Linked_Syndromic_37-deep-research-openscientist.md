---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T08:42:52.426937'
end_time: '2026-08-19T09:09:29.348041'
duration_seconds: 1596.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Developmental Disorder, X-Linked, Syndromic 37
  mondo_id: ''
  category: Genetic
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
citation_count: 5
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_X-Linked_Syndromic_37-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_X-Linked_Syndromic_37-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, X-Linked, Syndromic 37
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, X-Linked, Syndromic 37** covering all of the
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

# Intellectual Developmental Disorder, X-Linked, Syndromic 37 (MRXS37): A Comprehensive Disease Characteristics Report

## Summary

**Intellectual Developmental Disorder, X-Linked, Syndromic 37 (MRXS37; OMIM #301118; MONDO:0958322)** is an ultra-rare, recently delineated X-linked neurodevelopmental syndrome caused by germline pathogenic variants in the **ZFX gene** on chromosome Xp22.11. ZFX encodes a C2H2 zinc-finger transcription factor that escapes X-chromosome inactivation and functions as a general (housekeeping) transcriptional regulator of stem-cell self-renewal, binding GC-rich CpG-island promoters. The disorder was first characterized as a distinct clinical entity by Shepherdson and colleagues in 2024 ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)), who described 18 individuals (14 males, 4 females) from 16 unrelated families identified through exome or genome sequencing.

The clinical phenotype centers on **global developmental delay and intellectual disability** (ranging from borderline to moderate), **behavioral abnormalities** (autism spectrum disorder, ADHD, sleep difficulties), **hypotonia**, and a **recurrent, recognizable facial gestalt** present in every affected individual—characterized by thickening and medial broadening of the eyebrows, variations in facial shape, external eye abnormalities, a smooth and/or long philtrum, and ear abnormalities. A notable subset of families carrying missense variants also displayed **hyperparathyroidism** and an enrichment of diverse tumor types, connecting the germline disorder to ZFX's established oncogenic role in somatic cancers. Males are more severely affected than heterozygous females, consistent with X-linked inheritance modulated by skewed X-inactivation.

Mechanistically, MRXS37 arises from two variant classes: **truncating variants** (7 of 11) that likely act through loss of function (nonsense-mediated decay or removal of the DNA-binding zinc fingers), and **missense variants** (4 of 11) clustering in the penultimate/ultimate C-terminal zinc fingers responsible for DNA-binding specificity, which perturb transcriptional activity of downstream target genes. The disorder is non-progressive (static encephalopathy), generally non-life-limiting, and managed supportively; no disease-modifying therapy exists. Because only a single cohort has been reported to date, this report reflects an evidence base derived almost entirely from one landmark study supplemented by ZFX functional biology literature.

---

## Section 1: Disease Information

**Overview.** MRXS37 is a syndromic form of X-linked intellectual developmental disorder. "Syndromic" indicates that cognitive impairment is accompanied by additional recognizable features—here, a characteristic facial gestalt, behavioral abnormalities, hypotonia, congenital anomalies, and in some individuals endocrine/tumor manifestations. It belongs to the large family of X-linked intellectual disability (XLID) disorders but is distinguished by its causal gene (ZFX) and its recurrent craniofacial signature.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| OMIM (disease) | #301118 |
| OMIM (gene, ZFX) | *314980 |
| MONDO | MONDO:0958322 |
| MedGen | C5935567 |
| Gene (HGNC) | HGNC:12869 (ZFX) |
| NCBI Gene | 7543 |
| UniProt | P17010 |
| Cytogenetic location | Xp22.11 |

**Synonyms / alternative names:** MRXS37; ZFX-related neurodevelopmental disorder; ZFX-associated X-linked neurodevelopmental disorder with recurrent facial gestalt. The gene ZFX carries the synonym ZNF926.

**Data source type.** The information is derived from **aggregated, individual-patient clinical and molecular characterization** compiled into a disease-level description—specifically deep phenotyping and genomic sequencing of 18 individuals across 16 families, not from EHR-scale population data or registries (which do not yet exist for this ultra-rare condition).

---

## Section 2: Etiology

**Disease causal factors.** MRXS37 is a **monogenic genetic disorder** caused by germline variants in ZFX. There is no environmental, infectious, or acquired etiology. As stated by Shepherdson et al.: *"ZFX on Xp22.11 encodes a transcription factor that has been linked to diverse processes including oncogenesis and development, but germline variants have not been characterized in association with disease"* ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)).

**Genetic risk factors.** The causal variants are germline ZFX variants (11 identified: 4 missense, 7 truncating). All were **absent from population databases** (gnomAD, RGC-ME, All of Us), consistent with high pathogenicity. In this cohort, 10 variants were de novo and 8 were maternally inherited from mildly affected or unaffected mothers who showed skewed X-inactivation—the mother's normal X preferentially active, protecting her while transmitting the variant.

**Environmental risk factors.** None identified. **Sex is the principal non-genetic modifier**: males (hemizygous) are more severely affected than heterozygous females, in whom X-inactivation patterns modulate expression.

**Protective factors.** The only established protective mechanism is **favorably skewed X-chromosome inactivation** in carrier females, which preferentially silences the mutant allele and attenuates or abolishes phenotypic expression. No dietary, lifestyle, or pharmacologic protective factors are known.

**Gene–environment interactions.** No gene–environment interactions have been characterized; the disorder is essentially fully genetically determined with severity modulated by sex and X-inactivation.

---

## Section 3: Phenotypes

All phenotype frequencies below derive from the 18-individual founding cohort ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)). Because the cohort is small, frequencies should be interpreted as qualitative.

| Phenotype | Type | Frequency | HPO term (suggested) |
|-----------|------|-----------|----------------------|
| Global developmental delay | Clinical sign / neurodevelopmental | Core feature | HP:0001263 |
| Intellectual disability (borderline–moderate) | Clinical sign | Core feature | HP:0001249 |
| Autism spectrum disorder | Behavioral | Subset | HP:0000717 |
| Attention deficit hyperactivity disorder | Behavioral | Subset | HP:0007018 |
| Sleep disturbance | Behavioral | Subset | HP:0002360 |
| Hypotonia | Clinical sign | Common | HP:0001252 |
| Thick / medially broadened eyebrows | Physical (facial) | All subjects | HP:0000574 / HP:0000280 |
| External eye abnormalities | Physical (facial) | All subjects | HP:0000492 |
| Smooth and/or long philtrum | Physical (facial) | All subjects | HP:0000319 / HP:0000343 |
| Ear abnormalities | Physical (facial) | All subjects | HP:0000377 |
| Abnormal facial shape | Physical (facial) | All subjects | HP:0001999 |
| Hyperparathyroidism | Laboratory / endocrine | 4 families (missense) | HP:0000843 |
| Congenital anomalies (variable) | Physical | Subset | HP:0000118 |

**Phenotype characteristics:**
- **Age of onset:** Congenital/neonatal to early childhood; developmental delay and facial features are apparent early.
- **Severity:** Variable; intellectual disability ranges from borderline to moderate. Males more severely affected than females.
- **Progression:** Static/non-progressive (developmental rather than degenerative).
- **The recurrent facial gestalt is the single most consistent feature—present in 100% of subjects**, per the authors: *"Overlapping and recurrent facial features were identified in all subjects, including thickening and medial broadening of eyebrows, variations in the shape of the face, external eye abnormalities, smooth and/or long philtrum, and ear abnormalities"* ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)).

**Quality-of-life impact.** Cognitive and behavioral impairment affects education, communication, and independent living. However, functional outcomes are comparatively favorable among syndromic NDDs: many individuals attend mainstream school with support and can work under supervision. No formal QoL instrument (EQ-5D, SF-36, PROMIS) data exist for this condition.

---

## Section 4: Genetic / Molecular Information

**Causal gene.** ZFX (Zinc Finger protein, X-linked), OMIM *314980, HGNC:12869, NCBI Gene 7543, UniProt P17010, located at Xp22.11. Reference transcript: **NM_003410.4**.

**Protein architecture.** ZFX comprises an **N-terminal acidic transcriptional activation domain (~360 aa)**, a nuclear localization signal, and a **C-terminal cluster of 13 C2H2 zinc fingers**; the last three zinc fingers are necessary and sufficient for promoter recruitment.

**Pathogenic variant spectrum** (from Shepherdson et al. 2024): *"Four missense variants were identified in 11 subjects, with seven truncation variants in the remaining individuals"* ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)).

| Variant class | Count | Representative variants (NM_003410.4) | Mechanism |
|---------------|-------|----------------------------------------|-----------|
| Missense (DNA-binding domain) | 4 variants / 11 subjects | c.2312C>T p.(Thr771Met) — 3 patients (RCV003991065); c.2321A>G p.(Tyr774Cys) (RCV003991066); recurrent p.(Arg786Gln) — 2 patients | Altered transcriptional activity (gain or loss); clustering in penultimate/ultimate C-terminal zinc fingers |
| Truncating | 7 variants | c.1319dup p.(Leu440Phefs*21) (RCV003991068); p.(Met666Valfs*2) (VCV003367188, Pathogenic); c.115_116del (2-bp) | Loss of function via NMD or removal of DNA-binding zinc fingers |

**Variant classification.** Pathogenic/likely pathogenic per ACMG/AMP; all variants **absent from gnomAD, RGC-ME, and All of Us**, supporting pathogenicity.

**Somatic vs germline.** All MRXS37 variants are **germline**. (Notably, ZFX overexpression is documented as a somatic event in multiple cancers—hepatocellular carcinoma, renal, glioma—but that is distinct from the germline disorder.)

**Functional consequences.** Truncating variants → loss of function. Missense variants → altered transcriptional output: *"DNA-binding domain variants elicited differential expression of a small set of target genes relative to wild-type ZFX in cultured cells, suggesting a gain or loss of transcriptional activity"* ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)).

**Modifier genes.** None specifically identified; X-inactivation skewing is the dominant modifier of expression in females.

**Epigenetic information.** ZFX itself **escapes X-inactivation** and binds GC-rich CpG-island promoters. Its own gene contains a 1.5-kb CpG island: *"a 1.5-kb CpG island encompasses multiple transcription initiation sites as well as the first and second exons. The 5' portion of the CpG island displays promoter activity"* ([PMID: 8188262](https://pubmed.ncbi.nlm.nih.gov/8188262/)). No disease-specific methylation episignature has been reported.

**Chromosomal abnormalities.** MRXS37 is caused by point/small variants; no large structural rearrangements are characteristic. (CMA is not the primary diagnostic modality.)

---

## Section 5: Environmental Information

**Environmental factors:** None. MRXS37 is a purely genetic monogenic disorder.
**Lifestyle factors:** Not applicable.
**Infectious agents:** Not applicable.

There are no known environmental, occupational, dietary, or infectious contributors to MRXS37.

---

## Section 6: Mechanism / Pathophysiology

**Core mechanism.** ZFX is a **general transcription factor and master regulator of stem-cell self-renewal**. In embryonic and hematopoietic stem cells, ZFX directly activates shared self-renewal target genes: *"Zfx directly activated common target genes in ESC and HSC, as well as ESC-specific target genes including ESC self-renewal regulators Tbx3 and Tcl1"* ([PMID: 17448993](https://pubmed.ncbi.nlm.nih.gov/17448993/)). Germline ZFX variants disrupt this transcriptional program during neurodevelopment.

**Molecular pathway.** ZFX has been linked to **canonical Wnt signaling** as a proposed mechanism for its self-renewal role: *"it appears that the ZFX is linked to the canonical Wnt signaling, which is one possible mechanism to explain the role of ZFX in the self-renewal of stem cells"* ([PMID: 39712568](https://pubmed.ncbi.nlm.nih.gov/39712568/)). ZFX and ZFY are *"zinc-finger proteins that encode general transcription factors abundant in hematopoietic and embryonic stem cells"* ([PMID: 39712568](https://pubmed.ncbi.nlm.nih.gov/39712568/)), with self-renewal regulation almost exclusive to ZFX.

**Causal chain:**

```
Germline ZFX variant (Xp22.11)
        │
        ├── Truncating → LoF (NMD / loss of DNA-binding zinc fingers)
        └── Missense (C-terminal ZFs) → altered DNA binding / transcription
        │
        ▼
Dysregulated transcription at GC-rich CpG-island promoters
(altered expression of self-renewal / developmental targets;
 canonical Wnt linkage)
        │
        ▼
Perturbed neural progenitor / stem-cell self-renewal & differentiation
        │
        ▼
Abnormal brain and craniofacial development
        │
        ▼
Developmental delay, intellectual disability, behavioral abnormalities,
recurrent facial gestalt, hypotonia
        │
        └── (missense subset) → parathyroid/tumor predisposition
            (hyperparathyroidism, tumor enrichment)
```

**Cellular processes.** Stem-cell/progenitor self-renewal (GO:0019827), regulation of transcription by RNA polymerase II (GO:0006357), cell proliferation and survival. ZFX's oncologic literature shows it controls proliferation, cell-cycle progression, and apoptosis resistance across tumor types.

**Protein dysfunction.** Missense variants impair sequence-specific DNA binding via the terminal C2H2 zinc fingers; truncating variants remove the DNA-binding module or trigger NMD. Both converge on transcriptional dysregulation.

**Immune involvement / metabolic changes / tissue damage:** Not primary features. There is no autoimmune, inflammatory, or classic metabolic-crisis component.

**Molecular profiling.** In vitro expression profiling of DNA-binding-domain variants demonstrated differential expression of a small set of ZFX target genes relative to wild-type—the direct functional readout of pathogenicity ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)).

**Suggested ontology terms:** GO:0019827 (stem cell population maintenance), GO:0006357 (regulation of transcription by RNA Pol II), GO:0060070 (canonical Wnt signaling pathway); CL:0000047 (neuronal stem cell), CL:0000034 (stem cell).

---

## Section 7: Anatomical Structures Affected

**Organ / system level:**
- **Primary:** Central nervous system / brain (UBERON:0000955) — nervous system (UBERON:0001016). Manifested as cognitive, behavioral, and tone abnormalities.
- **Craniofacial structures:** face (UBERON:0000033), eyebrow, philtrum, external ear — reflected in the recurrent facial gestalt.
- **Secondary/endocrine:** parathyroid gland (UBERON:0001132) in the missense subset with hyperparathyroidism.

**Tissue / cell level:** Nervous tissue; neural stem/progenitor cells (CL:0000047), broadly stem cells (CL:0000034). ZFX's normal role in hematopoietic and embryonic stem cells implies neural progenitor involvement during development.

**Subcellular level:** Nucleus (GO:0005634) — ZFX is a nuclear transcription factor acting at chromatin/promoters (GO:0005667, transcription regulator complex).

**Localization / lateralization:** The facial gestalt and neurodevelopmental features are **bilateral and symmetric**. No lateralized findings reported.

---

## Section 8: Temporal Development

**Onset.** Congenital / early childhood. Developmental delay and the facial gestalt are recognizable from infancy; onset pattern is **chronic/insidious** (a developmental, not acute, presentation).

**Progression.** **Static and non-progressive.** MRXS37 is a stable developmental encephalopathy rather than a neurodegenerative process. Individuals have been reported up to age 34 without documented deterioration or reduced survival.

**Disease course.** Chronic and lifelong; disability is stable. No relapsing–remitting or episodic pattern.

**Remission / critical periods.** No spontaneous remission. The relevant window for intervention is the **early developmental period**, when early-intervention therapies (speech, occupational, physical, behavioral) can optimize functional outcomes.

---

## Section 9: Inheritance and Population

**Epidemiology.** **Ultra-rare.** As of 2026, only 18 individuals from 16 families have been reported ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)); no formal prevalence or incidence has been established, and no follow-up cohorts have appeared.

**Inheritance pattern.** **X-linked.** In the founding cohort, transmission was consistent with X-linked inheritance—10 variants de novo, 8 maternally inherited from mildly affected or unaffected mothers.

**Penetrance / expressivity.** High penetrance in hemizygous males; **variable/reduced penetrance and expressivity in heterozygous females**, governed by X-inactivation skewing. Expressivity is variable overall (borderline to moderate ID).

**Sex ratio.** Male-predominant clinical severity; the cohort comprised 14 males and 4 females. Males are more severely affected.

**Germline mosaicism / founder effects / consanguinity / carrier frequency:** Not specifically documented; given ultra-rarity there are no established founder alleles, consanguinity associations, or carrier-frequency estimates. Carrier mothers with skewed X-inactivation may be asymptomatic.

**Population demographics / geographic distribution.** No ethnic or geographic predilection identified; cases were ascertained internationally through exome/genome sequencing and multi-center collaboration.

---

## Section 10: Diagnostics

**Genetic testing is the definitive diagnostic modality.** Because MRXS37 has no specific biochemical marker, diagnosis rests on identifying a pathogenic germline ZFX variant.

| Modality | Utility for MRXS37 |
|----------|--------------------|
| **Whole exome sequencing (WES)** | Primary diagnostic tool; how the founding cohort was identified |
| **Whole genome sequencing (WGS)** | Effective alternative; also used in the cohort |
| **NDD/XLID gene panels** | Useful if ZFX is included (many panels may not yet contain it) |
| **Single-gene ZFX testing** | Confirmatory / cascade testing once a familial variant is known |
| **Chromosomal microarray (CMA)** | Low yield — variants are point/small, not CNVs |
| **Karyotype / FISH** | Not indicated |

**Clinical tests / biomarkers.** No specific laboratory biomarker. **Serum calcium and parathyroid hormone (PTH)** should be checked given hyperparathyroidism risk in missense-variant carriers. Tumor surveillance is prudent given observed tumor enrichment. Brain MRI may be performed to evaluate developmental delay but shows no pathognomonic finding.

**Clinical criteria / differential diagnosis.** Diagnosis is molecular. Differential diagnoses include other syndromic XLID disorders with facial dysmorphism and behavioral features (e.g., ATR-X syndrome, DLG3-related XLID 90, MCT8/SLC16A2 deficiency, Simpson-Golabi-Behmel syndrome). The **recurrent facial gestalt** (broad medial eyebrows, smooth/long philtrum, ear anomalies) can prompt targeted ZFX evaluation.

**Screening.** No newborn or population screening exists. **Cascade genetic testing** of at-risk relatives and prenatal/preimplantation testing are options once a familial variant is identified.

**Recommended approach:** Trio exome or genome sequencing for a child with unexplained developmental delay/ID plus the characteristic facial gestalt; confirm segregation and X-inactivation status in the mother.

---

## Section 11: Outcome / Prognosis

**Survival and mortality.** No reduced survival documented; individuals reported up to age 34. MRXS37 is **generally non-life-limiting**.

**Morbidity and function.** Lifelong intellectual disability (borderline to moderate) and behavioral challenges constitute the principal morbidity. Functional prognosis is **comparatively favorable** among syndromic NDDs—many individuals attend mainstream school with support and can work under supervision.

**Complications.** Endocrine (hyperparathyroidism) and neoplastic (tumor enrichment) complications occur predominantly in missense-variant carriers and warrant monitoring. Behavioral comorbidities (autism, ADHD, sleep disturbance) affect daily functioning.

**Prognostic factors.** Sex (males more severely affected) and **variant class**: missense variants in the DNA-binding domain carry the added hyperparathyroidism/tumor risk, whereas truncating (LoF) variants are associated with the neurodevelopmental phenotype without the same reported endocrine/tumor enrichment. X-inactivation skewing predicts female severity.

**Quality-of-life measures:** No formal QoL data available.

---

## Section 12: Treatment

**No disease-modifying or gene-targeted therapy exists.** Management is **supportive and multidisciplinary**, tailored to the individual's manifestations.

| Domain | Intervention | Suggested NCIT concept |
|--------|-------------|------------------------|
| Developmental | Early intervention; special education | Early Intervention (NCIT:C154751) |
| Rehabilitative | Physical, occupational, and speech therapy | Rehabilitation Therapy (NCIT:C15917) |
| Behavioral | Behavioral therapy; ADHD/autism management; sleep hygiene | Behavioral Therapy (NCIT:C15819) |
| Endocrine | Monitoring/treatment of hyperparathyroidism (missense carriers) | Supportive Care (NCIT:C15300) |
| Oncologic | Tumor surveillance given tumor enrichment | Cancer Surveillance |
| Genetic | Genetic counseling; cascade testing | Genetic Counseling (NCIT:C15681) |

**Pharmacotherapy.** Symptomatic only—e.g., standard agents for ADHD, sleep, or seizures if present. No ZFX-specific pharmacogenomic guidance exists.

**Advanced therapeutics / experimental.** No gene therapy, RNA-based therapy, or targeted therapy is available or in trials. There are **no MRXS37/ZFX interventional clinical trials** registered.

**Treatment strategy.** Individualized, guided by phenotype: neurodevelopmental support universally; endocrine and tumor surveillance selectively for missense-variant carriers.

---

## Section 13: Prevention

**Primary prevention:** Not possible for a spontaneous germline disorder. **Genetic counseling** is the cornerstone for at-risk families.

**Secondary prevention:** In families with a known variant, **prenatal diagnosis** and **preimplantation genetic testing (PGT)** allow informed reproductive decisions. **Cascade carrier testing** identifies at-risk female relatives.

**Tertiary prevention:** Surveillance for complications—**serum calcium/PTH monitoring** for hyperparathyroidism and **tumor surveillance** in missense-variant carriers—plus early developmental intervention to optimize functional outcomes.

**Counseling.** Genetic counseling should address X-linked recurrence risk (carrier mothers have 50% transmission risk per pregnancy; sons inheriting the variant are affected, daughters are carriers with variable/attenuated expression depending on X-inactivation), and the role of skewed X-inactivation in maternal phenotype.

**Immunization / public health / environmental interventions:** Not applicable.

---

## Section 14: Other Species / Natural Disease

**Taxonomy.** No naturally occurring MRXS37-equivalent disease has been described in non-human species. ZFX orthologs are highly conserved across vertebrates.

**Orthologous genes.** Mouse *Zfx* (the ortholog most functionally studied); the Zfx/Zfy family is *"highly conserved in vertebrates."* Mouse Zfx gene structure, including its CpG-island promoter, was characterized by Luoh & Page ([PMID: 8188262](https://pubmed.ncbi.nlm.nih.gov/8188262/)).

**Natural disease / veterinary relevance.** None reported (OMIA has no corresponding entry). No zoonotic or cross-species transmission relevance—MRXS37 is a heritable genetic disorder, not communicable.

**Comparative biology.** The evolutionary conservation of ZFX's stem-cell self-renewal function underlies the utility of model organisms for studying its biology.

---

## Section 15: Model Organisms

**Zebrafish (*Danio rerio*).** A **zfx loss-of-function zebrafish model** was generated in the founding study and showed a neurobehavioral phenotype without gross morphologic abnormality: *"a zebrafish model of ZFX loss displayed an altered behavioral phenotype"* ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/))—specifically decreased anxiety and impaired habituation. This model recapitulates the behavioral dimension of MRXS37 and is the most directly disease-relevant model available.

**Mouse (*Mus musculus*).** Extensive *Zfx* knockdown/knockout work established ZFX's role in embryonic and hematopoietic stem-cell self-renewal ([PMID: 17448993](https://pubmed.ncbi.nlm.nih.gov/17448993/)) and in Hedgehog-driven tumorigenesis (basal cell carcinoma, medulloblastoma; [PMID: 25164012](https://pubmed.ncbi.nlm.nih.gov/25164012/)). These models illuminate mechanism but were not built specifically to model the neurodevelopmental syndrome.

**Cellular / in vitro.** Cultured cells expressing MRXS37 DNA-binding-domain variants demonstrated differential target-gene expression versus wild-type ZFX—the key functional assay establishing variant pathogenicity ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)). Human cancer cell lines (hepatocellular carcinoma, renal carcinoma, glioma) have been used to dissect ZFX's transcriptional targets (e.g., Nanog, SOX-2, Tbx3, Tcl1).

**Model characteristics.** The zebrafish model captures behavioral abnormality but not the facial gestalt or intellectual disability (which are difficult to model). No mouse model engineered with a specific human MRXS37 variant has yet been reported—a clear opportunity.

**Resources.** MGI (mouse *Zfx*), ZFIN (zebrafish *zfx*).

---

## Mechanistic Model / Interpretation

MRXS37 is best understood as a **transcription-factor dosage/function disorder affecting stem-cell self-renewal programs during neurodevelopment**. ZFX normally sits at the top of a self-renewal transcriptional hierarchy, binding GC-rich CpG-island promoters and activating targets such as Tbx3 and Tcl1, with mechanistic links to canonical Wnt signaling. Germline perturbation of ZFX—whether by haploinsufficiency/LoF (truncating variants) or by altered DNA-binding activity (C-terminal missense variants)—dysregulates this program in neural progenitors and craniofacial precursors, producing the consistent developmental and dysmorphic phenotype.

The **genotype–phenotype split** is the most clinically actionable insight:

| Feature | Truncating variants (LoF) | C-terminal missense variants |
|---------|---------------------------|------------------------------|
| Count | 7 variants | 4 variants (11 subjects) |
| Mechanism | NMD / loss of DNA-binding zinc fingers | Altered transcriptional activity (gain or loss) |
| Neurodevelopmental phenotype | Yes | Yes |
| Hyperparathyroidism | Not reported | Yes (4 families) |
| Tumor enrichment | Not reported | Yes |

This mirrors ZFX's dual identity in the literature: a **developmental self-renewal factor** (explaining the NDD) and a **somatic oncogene** overexpressed in hepatocellular, renal, glioma, and other cancers (explaining the tumor/endocrine enrichment in missense carriers). The missense variants may confer altered or partially gained transcriptional activity that tilts cells toward the proliferative/self-renewal state, plausibly connecting them to the neoplastic predisposition.

Sex and X-inactivation form the **second axis of variability**: males (hemizygous) fully express the phenotype, whereas heterozygous females' severity depends on which X is preferentially active—explaining mildly affected/unaffected carrier mothers and the male-predominant severity.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/) | *Variants in ZFX are associated with an X-linked neurodevelopmental disorder with recurrent facial gestalt* | **Landmark defining study.** Cohort (18 subjects/16 families), variant spectrum, facial gestalt, hyperparathyroidism/tumor link, in vitro transcriptional assay, zebrafish model. The near-sole clinical source. |
| [17448993](https://pubmed.ncbi.nlm.nih.gov/17448993/) | *Zfx controls the self-renewal of embryonic and hematopoietic stem cells* | Establishes ZFX's core function activating self-renewal targets (Tbx3, Tcl1). Mechanistic foundation. |
| [39712568](https://pubmed.ncbi.nlm.nih.gov/39712568/) | *Maintenance of stem cell self-renewal by sex chromosomal zinc-finger transcription factors* | ZFX as general transcription factor; canonical Wnt linkage; ZFX (not ZFY) drives self-renewal. |
| [8188262](https://pubmed.ncbi.nlm.nih.gov/8188262/) | *The structure of the Zfx gene on the mouse X chromosome* | Gene structure, CpG-island promoter—relevant to ZFX's GC-rich promoter binding. |
| [25164012](https://pubmed.ncbi.nlm.nih.gov/25164012/) | *Zfx facilitates tumorigenesis caused by activation of the Hedgehog pathway* | Supports ZFX's oncogenic role (BCC, medulloblastoma), contextualizing tumor enrichment. |
| [24585547](https://pubmed.ncbi.nlm.nih.gov/24585547/), [27566731](https://pubmed.ncbi.nlm.nih.gov/27566731/), [25441684](https://pubmed.ncbi.nlm.nih.gov/25441684/), [22185393](https://pubmed.ncbi.nlm.nih.gov/22185393/) | ZFX in HCC, renal carcinoma, glioma | Corroborate ZFX's proliferation/self-renewal/anti-apoptotic function in somatic cancers via Nanog/SOX-2, CDK4/cyclin D1. |

**Evidence source types:** The clinical phenotype and variant spectrum are **human clinical** (single cohort). The transcriptional-consequence data are **in vitro**. The behavioral phenotype is **model organism** (zebrafish). The self-renewal/oncogenic mechanism is **model organism + in vitro**.

---

## Limitations and Knowledge Gaps

1. **Single-cohort evidence base.** Essentially all clinical knowledge derives from one 2024 study of 18 individuals. No independent replication, natural-history study, or registry exists. Phenotype frequencies are provisional.
2. **No prevalence/incidence data.** The disorder is too newly described and rare for epidemiologic estimation.
3. **Genotype–phenotype correlation is preliminary.** The missense→hyperparathyroidism/tumor association is based on only four families; causality and penetrance of the tumor risk are not established.
4. **Mechanism incompletely defined.** The precise ZFX target genes driving the neurodevelopmental phenotype, and whether missense variants act by gain vs. loss of function, remain unresolved ("gain or loss of transcriptional activity").
5. **No purpose-built mammalian disease model.** The zebrafish captures behavior only; no mouse carries a patient-specific ZFX variant.
6. **No therapeutics.** No disease-modifying treatment, trial, or biomarker for treatment response.
7. **Female phenotype poorly characterized.** X-inactivation's quantitative effect on severity in heterozygous females needs systematic study.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the cohort** via GeneMatcher/DECIPHER and international collaboration to refine phenotype frequencies, penetrance, expressivity, and the tumor/endocrine association; establish a patient registry.
2. **Longitudinal natural-history study** to define developmental trajectory, adult outcomes, and tumor/parathyroid surveillance intervals.
3. **Functional dissection of variant classes:** systematic transcriptomic (RNA-seq) and ChIP-seq comparison of truncating vs. missense variants in isogenic neural progenitors/iPSC-derived neurons to resolve gain- vs. loss-of-function and identify the neurodevelopmentally relevant target genes.
4. **Generate patient-specific mouse (or brain-organoid) models** carrying recurrent variants (e.g., p.Thr771Met, p.Arg786Gln) to recapitulate cognitive, craniofacial, and tumor phenotypes.
5. **Define an X-inactivation–severity relationship** in carrier females through quantitative XCI assays correlated with phenotype.
6. **Investigate the ZFX–Wnt axis** in neural progenitors as a potential therapeutic node.
7. **Develop clinical surveillance guidelines**, especially calcium/PTH monitoring and tumor surveillance for missense-variant carriers.
8. **Search for a DNA-methylation episignature** to aid VUS classification, given ZFX's role at CpG-island promoters.

---

*Report compiled from an autonomous multi-iteration investigation. Primary evidence: Shepherdson et al., 2024 ([PMID: 38325380](https://pubmed.ncbi.nlm.nih.gov/38325380/)), supplemented by ZFX functional-biology literature.*


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_X-Linked_Syndromic_37-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_X-Linked_Syndromic_37-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.