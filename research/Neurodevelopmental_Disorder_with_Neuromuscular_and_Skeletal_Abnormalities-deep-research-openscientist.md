---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-18T15:06:42.314468'
end_time: '2026-08-18T15:22:38.590722'
duration_seconds: 956.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities
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
citation_count: 9
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 3
  off_topic: 1
  off_topic_references:
  - PMID:11728309
  needs_review: true
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_with_Neuromuscular_and_Skeletal_Abnormalities-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_with_Neuromuscular_and_Skeletal_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities** covering all of the
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

# Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities (NEDNMSA): A Comprehensive Disease Characteristics Report

**Disease:** Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities (NEDNMSA)
**MONDO ID:** MONDO:0859236 · **OMIM:** 619833 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *NRCAM* (HGNC:7994; NCBI Gene 4897; locus 7q31.1)

---

## Summary

Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities (NEDNMSA) is an **ultra-rare autosomal recessive Mendelian syndrome** caused by **biallelic loss-of-function or deleterious missense variants in *NRCAM***, the gene encoding the neuronal cell-adhesion molecule NrCAM (neuron-glia-related cell adhesion molecule). The disorder was first defined by Kurolap and colleagues in 2022 in a cohort of ten affected individuals from eight families ([PMID: 35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/)), and independently confirmed in 2023 by a second report describing a homozygous nonsense variant ([PMID: 36606341](https://pubmed.ncbi.nlm.nih.gov/36606341/)). The clinical syndrome is characterized by a triad-plus phenotype: **developmental delay/intellectual disability, hypotonia, and peripheral neuropathy and/or spasticity**, accompanied by a variable constellation of skeletal (scoliosis, hip dysplasia, foot deformities, distal arthrogryposis), central nervous system structural (thin corpus callosum, ventriculomegaly, delayed myelination, periventricular heterotopia), and ophthalmologic anomalies.

Mechanistically, NrCAM is an L1-family immunoglobulin-superfamily axonal/glial adhesion molecule that, together with its partners **gliomedin** and **neurofascin-186 (NF186)**, orchestrates the assembly of **nodes of Ranvier and axon initial segments** by recruiting ankyrin-G and clustering voltage-gated sodium channels. Loss of NrCAM function destabilizes this nodal complex, degrades saltatory conduction, and disrupts axon guidance and brain morphogenesis — providing a direct causal chain from gene dysfunction to the observed neuromuscular and neurodevelopmental phenotypes. Population-genetic constraint metrics from gnomAD (pLI ≈ 0; LOEUF = 0.636; observed/expected LoF = 0.53) confirm that *NRCAM* is **not haploinsufficient**, consistent with a **recessive** rather than dominant mechanism, and animal models (Nrcam-null mice, nrcama-deficient zebrafish) recapitulate axon-guidance and brain-structural defects.

The disorder is congenital in onset, non-progressive to slowly variable in course, and lifelong. Because only ~11 individuals have been reported worldwide, no prevalence estimate, natural-history study, disease-specific therapy, or clinical trial exists. Diagnosis is molecular (trio-based whole-exome or whole-genome sequencing) supported by nerve conduction studies and brain MRI, and **management is entirely supportive and multidisciplinary**. This report synthesizes eight confirmed findings across 15 disease-characteristic domains, flagging clearly where evidence is absent.

---

## Key Findings

### Finding 1 — NEDNMSA is caused by biallelic *NRCAM* variants (autosomal recessive)

Ontology cross-referencing links MONDO:0859236 → OMIM:619833 → UMLS:C5676965 / MedGen:1803456, and identifies **a single causal gene, *NRCAM*** (HGNC:7994; gene OMIM 601581; locus 7q31.1). The defining cohort (Kurolap et al., 2022) reported **ten affected individuals from eight families** carrying bi-allelic *NRCAM* variants. A second, independent report (Elahi et al., 2023) confirmed the gene–disease relationship with a homozygous nonsense variant **c.73C>T (p.Gln25\*)**, establishing the association beyond a single family.

> *"Here, we describe ten affected individuals with bi-allelic variants in the neuronal cell adhesion molecule NRCAM that lead to a neurodevelopmental syndrome of varying severity; the individuals are from eight families. This syndrome is characterized by developmental delay/intellectual disability, hypotonia, peripheral neuropathy, and/or spasticity."* — [PMID: 35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/)

> *"This study is the second report of an association between biallelic NRCAM gene variants and a Mendelian disorder."* — [PMID: 36606341](https://pubmed.ncbi.nlm.nih.gov/36606341/)

**Evidence type:** Human clinical (two independent cohorts). This finding anchors Section 1 (Disease Information), Section 4 (Genetic/Molecular), and Section 9 (Inheritance).

### Finding 2 — NrCAM mediates node-of-Ranvier assembly and Na⁺-channel clustering

NrCAM is an axonal/glial Ig-superfamily cell-adhesion molecule of the L1 family. Together with **gliomedin** and **neurofascin-186 (NF186)**, it clusters **ankyrin-G** and **voltage-gated Na⁺ channels** at nodes of Ranvier (Lustig et al., 2001, [PMID: 11728309](https://pubmed.ncbi.nlm.nih.gov/11728309/); Eshed et al., 2005, [PMID: 16039564](https://pubmed.ncbi.nlm.nih.gov/16039564/)). Combined genetic loss of gliomedin and NrCAM in mice causes progressive loss of nodal Na⁺ channels, "binary nodes," dysregulated nodal gap length, neurological abnormalities, and slowed nerve conduction (Amor et al., 2014).

> *"absence of both molecules (and hence the glial clustering signal) resulted in a gradual loss of Na(+) channels and other axonal components from the nodes, the formation of binary nodes, and dysregulation of nodal gap length. Therefore, these mice exhibit neurological abnormalities and slower nerve conduction."* — [PMID: 24719088](https://pubmed.ncbi.nlm.nih.gov/24719088/)

> *"These results provide the first evidence that neurofascin plays a major role in the formation of nodes, possibly via interactions with Nr-CAM."* — [PMID: 11728309](https://pubmed.ncbi.nlm.nih.gov/11728309/)

**Evidence type:** Model organism + in vitro. This is the central mechanistic finding explaining the neuropathy/spasticity phenotype (Section 6).

### Finding 3 — gnomAD constraint supports a recessive loss-of-function mechanism

Constraint metrics for *NRCAM* (ENSG00000091129; chr7:108,147,623–108,456,717 GRCh38; canonical ENST00000379028) are: **pLI ≈ 0** (2.58×10⁻¹¹), **LOEUF (oe_lof upper) = 0.636**, **observed/expected LoF = 0.53** (83 observed vs 156.5 expected), **LoF Z = 4.99**; missense oe = 0.89, mis_Z = 1.92. The near-zero pLI indicates *NRCAM* **tolerates heterozygous loss of function** (i.e., is not haploinsufficient), while the elevated LoF Z-score shows selection against biallelic depletion. This population-genetic signature is exactly what is expected for a gene causing a **recessive** disorder — heterozygous carriers are unaffected, and disease requires two damaged alleles.

**Evidence type:** Computational/population genetics (gnomAD v2/v4). Supports the inheritance model of Section 9.

### Finding 4 — Animal models recapitulate axon-guidance and brain-structural defects

Nrcam-null mice show disturbed olfactory-nerve axon guidance and altered size of the ventricular system and cerebellar vermis (Heyden et al., 2008). NrCAM also regulates postnatal hypothalamic tanycyte differentiation, proliferation, and neurogenesis (Moore et al., 2022, [PMID: 35464310](https://pubmed.ncbi.nlm.nih.gov/35464310/)). The defining human study used **zebrafish nrcama loss-of-function** to corroborate the gene–disease link.

> *"in both mutants, CHL1 and NrCAM, the guidance of the olfactory nerve projections is disturbed. Both mutations also alter the size of the ventricular system and the vermis"* — [PMID: 18588951](https://pubmed.ncbi.nlm.nih.gov/18588951/)

> *"These findings are corroborated by previous in vitro studies of murine Nrcam-deficient cells, revealing abnormal neurite outgrowth, synaptogenesis, and formation of nodes of Ranvier on myelinated axons."* — [PMID: 35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/)

The mouse ventricular/vermis changes mirror the **human ventriculomegaly and CNS anomalies**, and the neurite-outgrowth/synaptogenesis/node-formation deficits provide cellular-level parallels to the human disease (Sections 6, 15).

**Evidence type:** Model organism (mouse, zebrafish) + in vitro.

### Finding 5 — Pathogenic missense variants cluster in the third fibronectin type-III domain

Human NRCAM (UniProt **Q92823**) is a **1,304-aa type-I transmembrane L1-family protein** comprising **6 Ig-like domains (aa 46–632)**, **5 fibronectin type-III (Fn-III) domains (aa 649–1156)**, a transmembrane segment, and a cytoplasmic tail. The **third Fn-III domain (aa ~848–950)** is a mutational hotspot: many disease-associated missense variants cluster there and are computationally predicted to be deleterious to protein structure and protein–protein interactions.

> *"Computational analyses of NRCAM variants, many of which cluster in the third fibronectin type III (Fn-III) domain, strongly suggest a deleterious effect on NRCAM structure and function, including possible disruption of its interactions with other proteins."* — [PMID: 35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/)

**Evidence type:** Human clinical + computational. Informs variant interpretation (Section 4) and protein-dysfunction mechanism (Section 6).

### Finding 6 — Phenotype spectrum and frequencies (HPO-annotated cohort, n ≈ 10)

The table below consolidates HPOA/Monarch frequencies for MONDO:0859236 with suggested HPO terms. Frequencies are derived from the small defining cohort and should be read as **indicative, not population-representative**.

| Phenotype | HPO term | Frequency (affected/observed) |
|---|---|---|
| Global developmental delay | HP:0001263 | 40% (4/10) |
| Hypotonia | HP:0001252 | 40% (4/10) |
| Motor delay | HP:0001270 | 30% (3/10) |
| Intellectual disability | HP:0001249 | 30% (3/10) |
| Cerebral palsy / spasticity | HP:0100021 | 30% (3/10) |
| Scoliosis | HP:0002650 | 56% (5/9) |
| Hip dysplasia | HP:0001385 | 33% (3/9) |
| Pes cavus | HP:0001761 | 33% (3/9) |
| Hammertoe | HP:0001765 | 22% (2/9) |
| Distal arthrogryposis | HP:0005684 | 10% (1/10) |
| Microcephaly | HP:0000252 | 50% (3/6) |
| Micrognathia | HP:0000347 | 37.5% (3/8) |
| Demyelinating peripheral neuropathy | HP:0007108 | 10% (1/10) |
| Ataxia | HP:0001251 | 20% |
| Delayed CNS myelination | HP:0002188 | 22% |
| Thin corpus callosum | HP:0033725 | 22% |
| Ventriculomegaly | HP:0002119 | 22% |
| Periventricular heterotopia | HP:0007165 | 11% |
| Cataract | HP:0000518 | 25% |
| Optic atrophy | HP:0000648 | 12.5% |
| Retinal detachment | HP:0000541 | 12.5% |
| Failure to thrive | HP:0001508 | 25% |
| G-tube feeding | HP:0011471 | 22% |
| Self-injurious / aggressive behavior | HP:0100716 / HP:0000718 | ~20–40% |

ClinVar lists **289 *NRCAM* records, of which 38 are pathogenic/likely-pathogenic**.

> *"This syndrome is characterized by developmental delay/intellectual disability, hypotonia, peripheral neuropathy, and/or spasticity."* — [PMID: 35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/)

**Evidence type:** Human clinical (HPO annotation). Populates Section 3 (Phenotypes).

### Finding 7 — Epidemiology, inheritance, and diagnostic/management framework

The disorder is **ultra-rare**: the entire published literature comprises **~11 individuals** (10 from 8 families, Kurolap 2022; +1, Elahi 2023). **No prevalence or incidence estimate exists**, and there is **no Orphanet ORPHAcode**. Inheritance is **autosomal recessive** with biallelic homozygous or compound-heterozygous variants; homozygous variants in several families implicate **consanguinity**. Diagnosis is molecular via **trio-based whole-exome or whole-genome sequencing**, supported by **EMG/nerve conduction studies** (documenting axonal and/or demyelinating peripheral neuropathy) and **brain MRI** (thin corpus callosum, ventriculomegaly, delayed myelination, periventricular heterotopia). **No disease-specific pharmacotherapy, gene therapy, or clinical trial exists**; management is supportive and multidisciplinary. Severity is variable and **not strictly determined by variant type**, indicating variable expressivity relevant to prognostic counseling.

> *"we show that type of the pathogenic variant does not necessarily determine the severity of this phenotype."* — [PMID: 36606341](https://pubmed.ncbi.nlm.nih.gov/36606341/)

> *"the individuals are from eight families"* — [PMID: 35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/)

**Evidence type:** Human clinical. Populates Sections 8–13.

### Finding 8 — Evolutionary conservation and orthologs

NCBI Gene confirms conserved *NRCAM* orthologs across model species: **human *NRCAM*** (Gene 4897; HGNC:7994), **mouse *Nrcam*** (Gene 319504; NCBI:txid10090), **rat *Nrcam*** (Gene 497815; NCBI:txid10116), **zebrafish *nrcama*** (Gene 556537; NCBI:txid7955; paralog *nrcamb*). NRCAM belongs to the **L1 immunoglobulin-superfamily cell-adhesion molecule family**, with paralogs *L1CAM*, *CHL1*, and *NFASC*.

**Evidence type:** Computational/comparative genomics. Populates Sections 14–15.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** NEDNMSA is a Mendelian, autosomal recessive neurodevelopmental syndrome combining neurological, neuromuscular, and skeletal features. Its defining triad is developmental delay/intellectual disability, hypotonia, and peripheral neuropathy and/or spasticity, with additional variable skeletal, brain-structural, and eye findings.

**Key identifiers:** MONDO:0859236 · OMIM:619833 · UMLS:C5676965 · MedGen:1803456. **No Orphanet ORPHAcode** has been assigned (reflecting ultra-rarity). ICD-10/ICD-11 and MeSH lack a specific code; the disorder maps to broad categories and is best referenced by its MONDO/OMIM identifiers.

**Synonyms:** "Neurodevelopmental disorder with neuromuscular and skeletal abnormalities"; "NRCAM-related neurodevelopmental disorder"; "NRCAM-related bi-allelic disorder." Gene-level synonyms for NrCAM include neuron-glia-related cell adhesion molecule and neuronal cell adhesion molecule.

**Information source:** Aggregated **disease-level** resources (OMIM/MONDO) built from two **individual-patient** case series (clinical phenotyping of ~11 patients), not from population EHR datasets.

### 2. Etiology

**Causal factors.** The disorder is **purely genetic (monogenic, recessive)**: biallelic pathogenic variants in *NRCAM*. There is **no known environmental, infectious, or mechanistic (non-genetic) cause**.

**Genetic risk factors.** The only established risk factor is inheritance of **two damaged *NRCAM* alleles**. Consanguinity is a major contributor (multiple homozygous families). No modifier genes or susceptibility loci have been identified (the cohort is too small).

**Environmental / lifestyle / protective factors.** **Not applicable / not reported.** No environmental risk factors, protective variants, protective exposures, or gene–environment interactions have been described for this ultra-rare Mendelian disorder. Standard prenatal care applies but does not modify the genetic risk.

### 3. Phenotypes

See **Finding 6** table for the full HPO-annotated phenotype list with frequencies. Key characteristics:

- **Phenotype types:** clinical signs (hypotonia, spasticity, neuropathy), developmental/behavioral (developmental delay, intellectual disability, self-injurious/aggressive behavior), physical/skeletal manifestations (scoliosis, hip dysplasia, pes cavus, hammertoe, distal arthrogryposis, micrognathia, microcephaly), and neuroimaging abnormalities (thin corpus callosum, ventriculomegaly, delayed myelination, periventricular heterotopia).
- **Age of onset:** congenital/neonatal (hypotonia, structural anomalies) to early childhood (developmental delay).
- **Severity:** variable (mild to severe), **not strictly predicted by variant type** (Elahi 2023).
- **Progression:** largely static/stable neurodevelopmental course; peripheral neuropathy may be slowly progressive.
- **Quality-of-life impact:** substantial — motor and cognitive impairment, feeding difficulty (G-tube in ~22%), and orthopedic disability affect daily functioning and independence. Formal QoL instrument data (EQ-5D/SF-36/PROMIS) are **not available** for this ultra-rare disorder.

### 4. Genetic/Molecular Information

- **Causal gene:** *NRCAM* (HGNC:7994; NCBI Gene 4897; gene OMIM 601581; 7q31.1; ENSG00000091129; canonical ENST00000379028).
- **Protein:** NrCAM, UniProt Q92823, 1,304 aa, type-I transmembrane; 6 Ig-like domains (aa 46–632), 5 Fn-III domains (aa 649–1156); the **3rd Fn-III domain (~aa 848–950) is a missense hotspot** (Finding 5).
- **Variant classes:** nonsense (e.g., c.73C>T p.Gln25\*), other loss-of-function, and deleterious missense (clustered in Fn-III #3). ClinVar: **289 records, 38 pathogenic/likely-pathogenic**.
- **Functional consequence:** **loss of function** (recessive). gnomAD constraint (pLI ≈ 0; LOEUF 0.636; oe_LoF 0.53) confirms *NRCAM* is **not haploinsufficient** — disease requires biallelic hits (Finding 3).
- **Allele frequency:** individual pathogenic alleles are private/ultra-rare in gnomAD.
- **Origin:** **germline** (inherited, recessive). No somatic disease role in this Mendelian phenotype (though somatic/epigenetic *NRCAM* dysregulation is separately implicated in gliomas and colorectal cancer — see Evidence Base; this is unrelated to NEDNMSA).
- **Modifier genes / epigenetics / chromosomal abnormalities:** **not reported** for NEDNMSA.

### 5. Environmental Information

**Not applicable.** NEDNMSA is a monogenic recessive disorder with **no established environmental factors, lifestyle contributors, or infectious triggers.**

### 6. Mechanism / Pathophysiology

The core mechanism is **failure of node-of-Ranvier and axon-initial-segment assembly plus disrupted axon guidance** (Findings 2, 4, 5).

**Causal chain:**

```
Biallelic NRCAM LoF / deleterious missense (Fn-III #3 hotspot)
        │
        ▼
Loss of NrCAM adhesion function (Ig + Fn-III interactions with
gliomedin, NF186 disrupted)
        │
        ├─► Failure to recruit ankyrin-G  ──► Na⁺ channels not clustered
        │        at nodes of Ranvier / axon initial segments
        │        │
        │        ▼
        │   Degraded saltatory conduction ──► PERIPHERAL NEUROPATHY,
        │        SPASTICITY, MOTOR DELAY, HYPOTONIA
        │
        └─► Abnormal axon guidance, neurite outgrowth, synaptogenesis
                 │
                 ▼
            Brain morphogenesis defects (ventriculomegaly, thin corpus
            callosum, delayed myelination, periventricular heterotopia)
                 │
                 ▼
            DEVELOPMENTAL DELAY / INTELLECTUAL DISABILITY, MICROCEPHALY
```

- **Upstream:** loss of NrCAM adhesion; failure of the gliomedin–NF186–NrCAM glial clustering signal.
- **Downstream:** ankyrin-G / Na⁺-channel declustering → conduction failure; axon-guidance/synaptic defects → structural brain anomalies.
- **Cell types (CL terms):** neurons (CL:0000540), myelinating Schwann cells (CL:0002573), oligodendrocytes (CL:0000128), hypothalamic tanycytes (Moore 2022).
- **Biological processes (GO terms):** node of Ranvier assembly / GO:0033268; axon guidance / GO:0007411; cell adhesion / GO:0007155; myelination / GO:0042552; neuron projection development / GO:0031175; regulation of sodium ion transmembrane transport.
- **Subcellular compartments (GO CC):** node of Ranvier (GO:0033268), axon initial segment (GO:0043194), plasma membrane (GO:0005886), paranode region of axon (GO:0033270).
- **Molecular pathways:** L1-family cell-adhesion/axon-guidance signaling; ankyrin-G/βIV-spectrin cytoskeletal scaffolding. (NrCAM is also a Wnt-pathway target in cancer contexts — not relevant to NEDNMSA pathogenesis.)
- **Metabolic / immune involvement:** **not implicated.**

### 7. Anatomical Structures Affected

- **Organ level (UBERON):** brain (UBERON:0000955), peripheral nervous system / peripheral nerve (UBERON:0000010, UBERON:0001021), spinal cord (UBERON:0002240); secondary: skeletal system — vertebral column (UBERON:0001130), hip joint (UBERON:0001464), foot (UBERON:0002387); eye (UBERON:0000970).
- **Body systems:** nervous (central + peripheral), musculoskeletal, ophthalmologic.
- **Tissue/cell level:** nervous tissue, skeletal muscle (secondary, via denervation/hypotonia), connective/skeletal tissue; targeted cells — neurons, Schwann cells, oligodendrocytes (Findings 2, 4).
- **Subcellular:** node of Ranvier, axon initial segment, axolemma (Finding 2).
- **Specific sites / lateralization:** corpus callosum (UBERON:0002336), lateral ventricles (ventriculomegaly), cerebellar vermis (UBERON:0004720), periventricular zone; anomalies are typically **bilateral/symmetric** where reported.

### 8. Temporal Development

- **Onset:** congenital / neonatal (hypotonia, structural anomalies) to early-childhood (developmental delay); onset pattern is **chronic/insidious**, not acute.
- **Progression:** neurodevelopmental features are largely **static**; peripheral neuropathy and orthopedic features (e.g., scoliosis) may be **slowly progressive**. No defined disease stages.
- **Course:** chronic, lifelong. **No remission.** Severity variable and not determined by variant type (Finding 7).
- **Critical periods:** prenatal/early-postnatal neurodevelopment (axon guidance, myelination) is the window of vulnerability; no proven intervention window exists.

### 9. Inheritance and Population

- **Epidemiology:** **prevalence and incidence unknown** (ultra-rare; ~11 reported individuals; no registry).
- **Inheritance:** **autosomal recessive**; biallelic homozygous or compound-heterozygous *NRCAM* variants (Findings 1, 3).
- **Penetrance:** presumed high/complete in biallelic carriers (all reported biallelic individuals affected), though small n limits certainty.
- **Expressivity:** **variable** (severity independent of variant type; Finding 7).
- **Anticipation / mosaicism:** not reported / not applicable (no repeat expansion).
- **Founder effects:** none established; **consanguinity** is a recurring factor (multiple homozygous families).
- **Carrier frequency:** not formally estimated; heterozygous LoF alleles are tolerated per gnomAD constraint (Finding 3).
- **Demographics:** no ethnic predilection established; the small cohort spans multiple families/populations. **Sex ratio** not established (expected ~1:1 for autosomal recessive). Age distribution: pediatric at ascertainment.

### 10. Diagnostics

- **Genetic testing (primary):** trio-based **whole-exome (WES)** or **whole-genome sequencing (WGS)** is the diagnostic gold standard; targeted *NRCAM* analysis / neurodevelopmental gene panels can confirm. Chromosomal microarray/karyotype are typically normal (this is a sequence-level disorder, not a CNV syndrome).
- **Electrophysiology:** **EMG/nerve conduction studies** documenting axonal and/or demyelinating peripheral neuropathy (Finding 7).
- **Imaging:** **brain MRI** — thin corpus callosum, ventriculomegaly, delayed myelination, periventricular heterotopia (Findings 6, 7).
- **Laboratory/biomarkers:** **no specific biochemical biomarker**; diagnosis rests on genotype + phenotype.
- **Clinical criteria:** no formal consensus criteria; diagnosis is molecular + clinical gestalt.
- **Differential diagnosis:** other autosomal-recessive neurodevelopmental syndromes with neuropathy/spasticity and skeletal features (e.g., L1CAM-spectrum disorders, other L1-family conditions, hereditary motor-sensory neuropathies with CNS involvement, arthrogryposis-associated neurodevelopmental disorders). Molecular testing distinguishes them.
- **Screening:** no population newborn screening; **cascade carrier testing** of at-risk relatives is appropriate once a familial variant is known.

### 11. Outcome/Prognosis

- **Survival/mortality:** no disease-specific mortality data; the disorder is **not reported as lethal in childhood**, but survival statistics are unavailable (n too small).
- **Morbidity/function:** significant lifelong disability driven by intellectual disability, motor impairment, neuropathy/spasticity, feeding difficulty, and orthopedic complications (scoliosis, hip dysplasia).
- **Complications:** feeding failure/failure-to-thrive (G-tube ~22%), orthopedic deterioration, contractures, visual impairment (cataract/optic atrophy/retinal detachment).
- **Recovery potential:** none (structural/developmental); supportive care can improve function.
- **Prognostic factors:** severity is **variable and not predicted by variant type** (Finding 7); no validated prognostic biomarkers.

### 12. Treatment

**No disease-specific pharmacotherapy, gene therapy, cell therapy, RNA therapy, or targeted/immunotherapy exists. No clinical trials (NCT) are registered.** Management is **supportive and multidisciplinary** (Finding 7):

- **Supportive/rehabilitative (NCIT-type interventions):** physical therapy (NCIT:C15216), occupational therapy, speech therapy; nutritional support / gastrostomy feeding for failure-to-thrive.
- **Symptomatic pharmacotherapy:** antispasticity agents (e.g., baclofen) for spasticity; standard management of seizures/behavioral symptoms as needed (no disorder-specific evidence).
- **Surgical/interventional:** orthopedic correction of scoliosis, hip dysplasia, and foot deformities; ophthalmologic surgery (e.g., cataract, retinal detachment) as indicated.
- **Pharmacogenomics / personalized medicine:** not applicable / not developed.

### 13. Prevention

- **Primary prevention:** none for the genetic cause; **genetic counseling** for consanguineous or carrier families.
- **Secondary/tertiary prevention:** early developmental intervention; surveillance for and management of scoliosis, hip dysplasia, feeding, and ophthalmologic complications.
- **Genetic screening:** **carrier testing, cascade screening**, and **prenatal/preimplantation genetic diagnosis** available once a familial variant is identified.
- **Public health / immunization / behavioral / prophylaxis:** not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs (Finding 8):** mouse *Nrcam* (Gene 319504; txid10090), rat *Nrcam* (Gene 497815; txid10116), zebrafish *nrcama* (Gene 556537; txid7955; paralog *nrcamb*). NrCAM is an L1-family CAM (paralogs *L1CAM*, *CHL1*, *NFASC*).
- **Natural disease in other species:** **no naturally occurring NRCAM-equivalent disorder** is catalogued (e.g., in OMIA) — the disease is known only from engineered/experimental models, not spontaneous animal disease.
- **Comparative biology:** node-of-Ranvier assembly and NrCAM function are **highly evolutionarily conserved** across mammals and teleosts, validating cross-species modeling.
- **Zoonotic potential:** not applicable (genetic disorder).

### 15. Model Organisms

- **Mouse (*Mus musculus*, MGI):** Nrcam-null mice — disturbed olfactory-nerve axon guidance, altered ventricular-system and cerebellar-vermis size (Heyden 2008); tanycyte differentiation/neurogenesis defects (Moore 2022); combined gliomedin+NrCAM loss — node disintegration, conduction slowing (Amor 2014). **Recapitulation:** good for axon-guidance, brain-structural, and nodal/conduction phenotypes.
- **Zebrafish (*Danio rerio*, ZFIN):** nrcama loss-of-function used to corroborate the human gene–disease link (Kurolap 2022).
- **In vitro:** murine Nrcam-deficient cells — abnormal neurite outgrowth, synaptogenesis, and node-of-Ranvier formation (Finding 4).
- **Model types available:** knockout mice; morphant/mutant zebrafish; primary neuronal cultures. Humanized/conditional/iPSC-organoid models are **not yet reported** for this disorder.
- **Limitations:** models capture axonal/nodal and brain-structural biology but not the full human skeletal spectrum; small human cohort limits genotype–phenotype validation.

---

## Mechanistic Model / Interpretation

NEDNMSA is best understood as an **axonal cell-adhesion / node-of-Ranvier assembly disorder**. NrCAM sits at the intersection of two conserved neurodevelopmental processes: (1) **axon guidance and neurite/synapse formation** during brain morphogenesis, and (2) **nodal/AIS assembly** required for saltatory conduction. Biallelic loss of NrCAM function — whether through truncating variants or missense variants that disrupt the third Fn-III domain's protein interactions — degrades both processes simultaneously. This dual role explains the disorder's characteristic **combination of central (intellectual disability, brain malformations) and peripheral (neuropathy, hypotonia, spasticity) features**, with skeletal abnormalities arising secondary to the neuromuscular deficit and developmental disruption.

| Layer | Observation | Supporting evidence |
|---|---|---|
| Genetic | Biallelic *NRCAM* LoF/missense; recessive | Kurolap 2022, Elahi 2023, gnomAD |
| Protein | 3rd Fn-III domain missense hotspot; interaction disruption | Kurolap 2022 (Q92823) |
| Molecular | Failed gliomedin–NF186–NrCAM → ankyrin-G/Na⁺-channel declustering | Lustig 2001, Eshed 2005, Amor 2014 |
| Cellular | Abnormal neurite outgrowth, synaptogenesis, node formation | Kurolap 2022 (in vitro) |
| Organ | Axon-guidance defects, ventriculomegaly, vermis changes | Heyden 2008 (mouse), zebrafish |
| Clinical | DD/ID, hypotonia, neuropathy/spasticity, skeletal anomalies | Kurolap 2022, HPO |

The convergence of population-genetic constraint (recessive signature), conserved animal-model phenotypes, and human clinical/molecular data yields a **coherent, well-supported causal narrative** with no major internal contradictions.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/) | Bi-allelic *NRCAM* variants cause NDD (Kurolap 2022) | Human + zebrafish + in vitro | **Defining paper**; establishes gene–disease link, phenotype, Fn-III hotspot |
| [36606341](https://pubmed.ncbi.nlm.nih.gov/36606341/) | Bi-allelic *NRCAM* LoF, second report (Elahi 2023) | Human | Independent confirmation; variable severity |
| [24719088](https://pubmed.ncbi.nlm.nih.gov/24719088/) | Gliomedin+NrCAM maintain nodal Na⁺ channels (Amor 2014) | Mouse | Direct mechanistic link: node loss → conduction defect |
| [11728309](https://pubmed.ncbi.nlm.nih.gov/11728309/) | Nr-CAM/neurofascin cluster ankyrin-G, Na⁺ channels (Lustig 2001) | In vitro | NrCAM role in node formation |
| [16039564](https://pubmed.ncbi.nlm.nih.gov/16039564/) | Gliomedin mediates node assembly (Eshed 2005) | In vitro | Glial ligand for NrCAM/NF186 |
| [18588951](https://pubmed.ncbi.nlm.nih.gov/18588951/) | Nrcam/CHL1 mutant axon guidance + brain anatomy (Heyden 2008) | Mouse | Axon-guidance + ventricle/vermis defects |
| [35464310](https://pubmed.ncbi.nlm.nih.gov/35464310/) | NrCAM regulates hypothalamic tanycytes (Moore 2022) | Mouse | NrCAM in neurogenesis |
| [17548513](https://pubmed.ncbi.nlm.nih.gov/17548513/) | Nodes/AIS are ankyrin-G-dependent domains | In vitro | Nodal assembly framework |
| [17709431](https://pubmed.ncbi.nlm.nih.gov/17709431/) | Neurofascin assembles AIS ECM | In vitro | AIS/brevican context |

**Non-NEDNMSA context (excluded from pathogenesis):** *NRCAM* is separately dysregulated in gliomas via CNV/methylation ([PMID: 41663200](https://pubmed.ncbi.nlm.nih.gov/41663200/)) and overexpressed in colorectal cancer ([PMID: 21718388](https://pubmed.ncbi.nlm.nih.gov/21718388/)) as a Wnt target — these are **somatic/oncologic roles unrelated to the germline recessive Mendelian disorder** and are noted only to avoid conflation.

---

## Limitations and Knowledge Gaps

1. **Extremely small evidence base (~11 individuals).** All human phenotype frequencies derive from ≤10 patients; percentages are indicative, not population estimates.
2. **No epidemiology.** Prevalence, incidence, carrier frequency, sex ratio, and geographic distribution are unknown; no Orphanet code or registry exists.
3. **No natural-history or QoL data.** Progression rate, life expectancy, and validated QoL metrics are undefined.
4. **Genotype–phenotype correlation unresolved.** Severity is not predicted by variant type, but the sample is too small to establish modifiers.
5. **No disease-specific therapy or trials.** Management is empirical/supportive.
6. **Mechanistic gaps.** The precise contribution of each missense variant to specific interaction disruptions, and the relative weight of central vs. peripheral pathology, remain to be functionally dissected. No human iPSC/organoid model yet exists.
7. **Ontology mapping incomplete.** No dedicated ICD-11/MeSH/Orphanet identifiers.

---

## Proposed Follow-up Experiments / Actions

1. **International matchmaking (GeneMatcher, Matchmaker Exchange)** to expand the cohort, refine phenotype frequencies, and enable genotype–phenotype analysis.
2. **Functional validation of Fn-III #3 missense variants** — in vitro binding assays (NrCAM–gliomedin/NF186), node-of-Ranvier reconstitution, and structural modeling (AlphaFold + PDB comparison) to classify VUS per ACMG/AMP.
3. **Patient-derived iPSC neurons/organoids and myelinating co-cultures** to model node assembly and conduction deficits in a human context.
4. **Conditional / knock-in mouse models** carrying human missense alleles to test genotype-specific severity and evaluate rescue.
5. **Systematic natural-history study** (developmental, EMG/NCS, MRI, orthopedic, ophthalmologic surveillance) with standardized QoL instruments.
6. **Apply for Orphanet/ICD-11 codes** and establish a patient registry to support future epidemiology and trials.
7. **Cascade carrier screening and genetic-counseling protocols** for consanguineous families with a known variant, including prenatal/PGD options.

---

*Report compiled from 8 confirmed findings and 34 reviewed papers across 5 investigation iterations. Evidence types are labeled throughout as human clinical, model organism, in vitro, or computational.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_with_Neuromuscular_and_Skeletal_Abnormalities-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_with_Neuromuscular_and_Skeletal_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 3 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:11728309` (6 mentions) - Nr-CAM and neurofascin interactions regulate ankyrin G and sodium channel clustering at the node of Ranvier.
  - shared terms: node, conduction

Weighed against this report's own most characteristic terms: `nrcam`, `variant`, `type`, `disorder`, `gene`, `phenotype`, `recessive`, `human`, `clinical`, `neuropathy`, `peripheral`, `disease`, `model`, `developmental`, `spasticity`, `node`, `genetic`, `conduction`, `severity`, `skeletal`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.