---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T23:49:17.259641'
end_time: '2026-08-01T00:08:13.589346'
duration_seconds: 1136.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Myasthenic Syndrome 18
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
  path: Congenital_Myasthenic_Syndrome_18-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Myasthenic_Syndrome_18-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myasthenic Syndrome 18
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Myasthenic Syndrome 18** covering all of the
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

# Congenital Myasthenic Syndrome 18 (CMS18): A Comprehensive Disease Characteristics Report

**Disease:** Congenital Myasthenic Syndrome 18 (CMS18)
**MONDO ID:** MONDO:0014590 · **OMIM:** #616330 · **Causal gene:** *SNAP25* (HGNC:11132; NCBI Gene 6616)
**Category:** Mendelian (autosomal dominant, de novo)

---

## Summary

**Congenital Myasthenic Syndrome 18 (CMS18) is an ultra-rare, autosomal-dominant, presynaptic congenital myasthenic syndrome caused by a de novo missense variant (p.Ile67Asn) in *SNAP25*, the gene encoding the t-SNARE protein SNAP-25 (synaptosomal-associated protein of 25 kDa).** SNAP-25 is one of three core SNARE proteins that drive calcium-triggered fusion of synaptic vesicles at the nerve terminal. The pathogenic variant disrupts SNARE-complex assembly and Ca²⁺-triggered exocytosis, reducing quantal acetylcholine release and thereby lowering the safety margin of neuromuscular transmission. The clinical result is fatigable myasthenic muscle weakness combined with prominent central nervous system features — cortical hyperexcitability/epilepsy, cerebellar ataxia, and intellectual disability — because SNAP-25 is essential for both neuromuscular and central synaptic transmission ([PMID: 25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/)).

CMS18 sits at the intersection of two disease concepts. It is formally a congenital myasthenic syndrome (the 18th numbered subtype), but it also belongs to the broader **SNAP25 developmental and epileptic encephalopathy (SNAP25-DEE)** spectrum — part of a family of neurodevelopmental disorders now termed **"SNAREopathies"** that also encompass *STX1B*, *STXBP1*, and *VAMP2* ([PMID: 33299146](https://pubmed.ncbi.nlm.nih.gov/33299146/)). The myasthenic phenotype is the distinguishing feature of the original CMS18 patient, whereas most reported *SNAP25* patients present chiefly with encephalopathy. This dual identity is central to understanding the disease: the same gene, and even variants clustered in the same structural region, can produce a spectrum from predominantly myasthenic to predominantly encephalopathic phenotypes depending on the precise synaptic consequence of each variant.

Congenital myasthenic syndromes as a group are ultra-rare (UK genetically-confirmed prevalence ≈ 6.5 per million overall; 8.5 per million pediatric), and CMS18 is one of the very rarest subtypes — only a handful of cases worldwide, dwarfed by the common *CHRNE*, *DOK7*, and *RAPSN* subtypes ([PMID: 41251564](https://pubmed.ncbi.nlm.nih.gov/41251564/)). There is no cure. Management is symptomatic and genotype-guided: because CMS18 is a **presynaptic release defect**, release-enhancing agents such as 3,4-diaminopyridine (a Kv-channel blocker that prolongs nerve-terminal depolarization) and β-adrenergic agonists are the rational first-line choices, while cholinesterase inhibitors must be used cautiously because they worsen certain CMS subtypes ([PMID: 24425145](https://pubmed.ncbi.nlm.nih.gov/24425145/), [PMID: 36308527](https://pubmed.ncbi.nlm.nih.gov/36308527/)). CNS features additionally require antiseizure and supportive/rehabilitative care.

---

## 1. Disease Information

**Overview.** CMS18 is a genetic disorder of neuromuscular transmission in which the safety margin of the neuromuscular junction (NMJ) is impaired by a **presynaptic** defect in synaptic vesicle exocytosis. Unlike most CMS subtypes, which affect only the NMJ, CMS18 also affects central synapses, producing a combined neuromuscular-plus-neurodevelopmental phenotype (myasthenia, cortical hyperexcitability, cerebellar ataxia, intellectual disability) ([PMID: 25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/)).

**Key identifiers (verified via EBI OLS4 / Ontology Lookup Service — Finding F006):**

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0014590** |
| OMIM | **#616330** |
| DOID | DOID:0110683 |
| GARD | GARD:0016091 |
| MedGen | 906793 |
| UMLS | C4225364 |

**Synonyms and alternative names (registered in MONDO):**
- Myasthenic syndrome, congenital, 18, with intellectual disability and ataxia
- CMS18
- SNAP25 congenital myasthenic syndrome
- **SNAP25-DEE** (SNAP25 developmental and epileptic encephalopathy)
- Congenital myasthenic syndrome caused by mutation in *SNAP25*

**Source type.** The disease-level information here is derived from **aggregated disease-level resources** (OMIM, MONDO, Orphanet, ontology databases) and from **individual patient reports / small case series** in the primary literature (the index CMS18 patient in Shen et al. 2014; the ~23-individual SNAP25-DEE cohort in Klöckner et al. 2021). This is not EHR-derived population data — case counts are too small.

---

## 2. Etiology

**Primary cause — genetic.** CMS18 is caused by a **dominant de novo missense variant in *SNAP25*** (canonical index variant: **p.Ile67Asn**, in the neuronal SNAP25B splice isoform). It is a monogenic Mendelian disorder; the index case arose *de novo* (not inherited), which is typical of dominant SNARE-complex neurodevelopmental disorders ([PMID: 25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/)).

> *"Exome sequencing identified a dominant de novo variant, p.Ile67Asn, in SNAP25B, a SNARE protein essential for exocytosis of synaptic vesicles from nerve terminals and of dense-core vesicles from endocrine cells."* — Shen et al. 2014 ([PMID: 25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/))

**Genetic risk factors.** The single causal variant is the disease. There are no known susceptibility loci or common-variant risk factors — this is a fully penetrant monogenic dominant disorder driven by a single de novo change. No modifier genes have been established for CMS18 specifically, although the broader literature suggests the precise variant (and its differential effect on evoked vs spontaneous release) is the main determinant of phenotype severity and character ([PMID: 33147442](https://pubmed.ncbi.nlm.nih.gov/33147442/)).

**Environmental risk factors.** None established. As a de novo dominant Mendelian disorder, disease occurrence is not attributable to toxins, lifestyle, occupation, or infection. Advanced parental age is a generic contributor to de novo mutation rates but has not been specifically demonstrated for CMS18.

**Protective factors.** None identified (genetic or environmental). Not applicable for an ultra-rare monogenic disorder.

**Gene–environment interactions.** None documented. However, a clinically relevant *gene–drug* interaction exists: the presynaptic release mechanism of CMS18 dictates that release-enhancing drugs help whereas some cholinesterase inhibitors may not (see §12).

---

## 3. Phenotypes

CMS18 combines a peripheral myasthenic phenotype with central nervous system involvement. The index CMS18 patient (Shen 2014) exhibited myasthenia, cortical hyperexcitability, cerebellar ataxia, and intellectual disability; the broader SNAP25-DEE cohort (Klöckner 2021) defines the encephalopathic core.

| Phenotype | Type | HPO suggestion | Onset | Severity / course | Frequency |
|---|---|---|---|---|---|
| Fatigable muscle weakness / myasthenia | Clinical sign | HP:0003473 (Fatigable weakness) | Congenital / infancy | Variable; fluctuating/fatigable | Defining in index case |
| Intellectual disability | Clinical sign | HP:0001249 | Early childhood | Variable, static | Core in SNAP25-DEE |
| Epilepsy / early-onset seizures | Clinical sign | HP:0001250 (Seizure) | Mostly before age 2 | Often refractory | Core in SNAP25-DEE |
| Cerebellar ataxia | Clinical sign | HP:0001251 (Ataxia) | Childhood | Variable | Index case |
| Cortical hyperexcitability | Lab/electrophysiologic | HP:0002353 (EEG abnormality) | Childhood | — | Index case |
| Movement disorder | Clinical sign | HP:0100022 | Childhood | Recurrent | Recurrent in cohort |
| Cerebral visual impairment | Clinical sign | HP:0100704 / HP:0000618 | Early | — | Recurrent in cohort |
| Brain atrophy | Imaging finding | HP:0012443 | — | Progressive/static | Recurrent in cohort |

> *"Intellectual disability and early-onset epilepsy were identified as the core symptoms of SNAP25-DEE, with recurrent findings of movement disorders, cerebral visual impairment, and brain atrophy."* — Klöckner et al. 2021 ([PMID: 33299146](https://pubmed.ncbi.nlm.nih.gov/33299146/))

**Age of onset.** Congenital / early infantile. Seizures in the SNAP25-DEE spectrum typically begin before age 2.

**Severity and progression.** Variable across the spectrum. Myasthenic weakness is fatigable/fluctuating (characteristic of NMJ disorders); the neurodevelopmental component is largely static-to-slowly-evolving, with epilepsy potentially refractory.

**Quality-of-life impact.** No disease-specific QoL instrument (EQ-5D, SF-36, PROMIS) data exist for CMS18 given its rarity. By analogy to severe CMS and DEE, the combination of muscle weakness, intellectual disability, and refractory epilepsy imposes substantial impairment on mobility, communication, independent daily functioning, and caregiving burden. This is a qualitative inference, not a measured value.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***SNAP25*** (Synaptosomal-Associated Protein, 25 kDa). HGNC:11132; NCBI Gene 6616; OMIM gene *600322. Located on chromosome 20p11.2. Encodes a t-SNARE (target-membrane SNARE) protein of the plasma membrane. The neuronal splice isoform **SNAP25B** is the relevant transcript. Verified gene identifiers (Finding F006 / dossier).

**Pathogenic variant.**
- **Nomenclature:** p.Ile67Asn (I67N) in SNAP25B protein; a missense substitution replacing isoleucine 67 with asparagine.
- **Structural location (Finding F002):** Ile67 lies within the **SN1 (N-terminal) SNARE helix** of SNAP-25, the region that participates in the four-helix SNARE bundle. Substituting a hydrophobic Ile with a polar Asn in the coiled-coil interface impairs SNARE-bundle assembly/stability.
- **Variant class:** Missense.
- **Origin:** **Germline de novo** (present in the affected individual, absent in parents). Not somatic.
- **Classification:** Pathogenic (functionally validated by multiple assays; see §6).
- **Allele frequency:** Absent from population databases (gnomAD) — as expected for a de novo pathogenic variant in an ultra-rare disorder.
- **Functional consequence:** A **dominant loss/alteration of function with dominant-negative character** — the mutant protein incorporates into SNARE complexes and impairs Ca²⁺-triggered fusion, reducing evoked and spontaneous neurotransmitter release (see Finding F003).

**Allelic / phenotypic series.** Other *SNAP25* de novo variants (missense and loss-of-function) cause SNAP25-DEE without necessarily producing overt myasthenia. Variants cluster structurally but yield related-yet-distinct synaptic phenotypes; e.g., the V48F variant *increases* spontaneous release, opposite in direction to I67N ([PMID: 33147442](https://pubmed.ncbi.nlm.nih.gov/33147442/), [PMID: 40181518](https://pubmed.ncbi.nlm.nih.gov/40181518/)).

**Modifier genes.** None established for CMS18. Genetic-background modifiers plausible but undocumented.

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification data for CMS18. Not applicable / not available.

**Chromosomal abnormalities.** None — CMS18 is a single-nucleotide missense disorder, not a structural/aneuploidy syndrome.

---

## 5. Environmental Information

- **Environmental factors:** None known to cause or trigger CMS18. Not applicable (monogenic de novo disorder).
- **Lifestyle factors:** None known. (Generic caution: physical exertion transiently worsens fatigable myasthenic weakness, as in all CMS, but this is symptom modulation, not etiology.)
- **Infectious agents:** None. CMS18 is not infectious and is not known to be triggered by pathogens. Intercurrent infections/fever can nonspecifically worsen weakness and lower seizure threshold, as in many neurologic disorders, but do not cause the disease.

---

## 6. Mechanism / Pathophysiology

### Causal chain

```
De novo SNAP25(B) p.Ile67Asn (SN1 SNARE helix)
        │
        ▼
Impaired assembly / stability of the SNARE 4-helix bundle
 (SNAP-25 + syntaxin-1 + VAMP2/synaptobrevin-2)
        │
        ▼
Defective Ca2+-triggered synaptic-vesicle & dense-core-vesicle fusion
 (reduced evoked AND spontaneous release; decreased release probability)
        │
        ├───────────────► NMJ: reduced quantal ACh release
        │                  → lowered safety margin → fatigable weakness (myasthenia)
        │
        └───────────────► CNS synapses: impaired glutamatergic/GABAergic transmission
                           → cortical hyperexcitability/epilepsy, ataxia,
                             intellectual disability
```

### Molecular pathway
The core lesion is in **SNARE-mediated membrane fusion** — the final common step of regulated exocytosis. SNAP-25 is a **t-SNARE** that, with syntaxin-1 (t-SNARE) and VAMP2/synaptobrevin-2 (v-SNARE), forms the trans-SNARE four-helix bundle that draws vesicle and plasma membranes together for Ca²⁺-triggered fusion (synaptotagmin acts as the Ca²⁺ sensor). **GO terms:** GO:0006887 (exocytosis), GO:0016079 (synaptic vesicle exocytosis), GO:0017156 (calcium-ion-regulated exocytosis), GO:0031201 (SNARE complex), GO:0099504 (synaptic vesicle cycle).

### Direct functional evidence (Findings F001, F003)
Shen et al. 2014 established the causal chain with two independent in-vitro assays plus patient endplate physiology:

> *"Neuromuscular transmission at patient endplates was compromised by reduced evoked quantal release."* — [PMID: 25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/)

1. **Reconstituted fusion:** Ca²⁺-triggered liposome fusion was hindered when the t-SNARE carried mutant SNAP25B.
2. **Cellular exocytosis:** depolarization-evoked exocytosis was markedly reduced in bovine chromaffin cells transfected with mutant SNAP25B.

Østergaard et al. 2025 confirmed the mechanism in a human iPSC-derived NGN2 glutamatergic neuron model engineered to carry I67N:

> *"the variant did not affect passive or active electrical properties, but caused changes in synaptic transmission, including reduced evoked and spontaneous release, decreased synaptic vesicle release probability and consequential changes in short-term plasticity towards facilitation"* — [PMID: 40181518](https://pubmed.ncbi.nlm.nih.gov/40181518/)

The shift of short-term plasticity **toward facilitation** is the physiological signature of a reduced initial release probability — exactly what a presynaptic release defect predicts.

### Why variants differ (disease heterogeneity)
Alten et al. 2021 showed that structurally clustered *SNAP25* mutations produce related but mechanistically distinct phenotypes, with **spontaneous release** being a key axis of variation:

> *"specific alterations in spontaneous neurotransmitter release are a key factor to account for disease heterogeneity"* — [PMID: 33147442](https://pubmed.ncbi.nlm.nih.gov/33147442/)

I67N **reduces** both evoked and spontaneous release, whereas the V48F variant **increases** spontaneous release — a mechanistic contrast that helps explain why some *SNAP25* patients present with prominent myasthenia (release-deficient) while others present with predominantly epileptic encephalopathy.

### Cellular / tissue processes
- **Cell types (CL terms):** motor neuron / cholinergic neuron presynaptic terminals (CL:0000100 motor neuron; CL:0000108 cholinergic neuron), glutamatergic neurons (CL:0000679), GABAergic neurons (CL:0000617), neuroendocrine chromaffin cells (dense-core vesicle release). Skeletal muscle fibers are downstream targets (CL:0000188).
- **Subcellular compartments (GO CC):** GO:0031201 (SNARE complex), GO:0008021 (synaptic vesicle), GO:0042734 (presynaptic membrane), GO:0030141 (secretory/dense-core granule).
- **Protein dysfunction:** Not misfolding/aggregation — rather a **functional impairment of the SNARE assembly interface** with dominant-negative incorporation.
- **Immune involvement:** **None.** CMS18 is genetic, not autoimmune — this distinguishes it fundamentally from acquired myasthenia gravis and Lambert-Eaton syndrome. Anti-AChR and anti-MuSK antibodies are negative.
- **Metabolic changes:** No primary metabolic derangement; the defect is in vesicular exocytosis, not metabolism.

**Molecular profiling.** Østergaard et al. 2025 additionally reported **proteome changes** in I67N iPSC neurons alongside the electrophysiologic phenotype ([PMID: 40181518](https://pubmed.ncbi.nlm.nih.gov/40181518/)); this is the principal omics dataset available for the variant. No transcriptomic, metabolomic, or lipidomic disease signatures specific to CMS18 are established.

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Nervous system (primary):** peripheral motor nerve terminals at the NMJ; central synapses (cortex, cerebellum). Body system: nervous + neuromuscular. **UBERON:** UBERON:0001016 (nervous system), UBERON:0002037 (cerebellum), UBERON:0000956 (cerebral cortex).
- **Muscular system (target):** skeletal muscle, downstream of the failing NMJ. **UBERON:0001134** (skeletal muscle tissue); **UBERON:0001630** (muscle organ).
- **Neuromuscular junction (site of primary lesion):** **UBERON:0002439** (neuromuscular junction) / the presynaptic motor nerve terminal.
- **Endocrine (subclinical/experimental):** dense-core-vesicle secretion (e.g., chromaffin cells) is impaired in vitro; clinical endocrine disease is not a described feature.

**Tissue / cell level.** Nervous tissue (motor neurons, cortical/cerebellar neurons) and skeletal muscle. Primary cell targets are presynaptic nerve terminals; muscle fibers are secondarily under-stimulated (see CL terms in §6).

**Subcellular level.** Presynaptic active zone, synaptic vesicle membrane, presynaptic plasma membrane, SNARE complex (GO:0031201).

**Localization / lateralization.** Generalized and **bilateral/symmetric**, consistent with a systemic genetic synaptic defect (ptosis, facial, bulbar, limb weakness patterns typical of CMS; central features are diffuse).

---

## 8. Temporal Development

- **Onset:** **Congenital / early infantile.** Myasthenic features present from birth/infancy; seizures in the spectrum typically before age 2 ([PMID: 33299146](https://pubmed.ncbi.nlm.nih.gov/33299146/)).
- **Onset pattern:** Chronic, insidious with fatigable fluctuation of weakness.
- **Progression:** Chronic and **lifelong**. The neurodevelopmental component (ID) is largely static; epilepsy may be refractory; myasthenic weakness fluctuates day-to-day and worsens with exertion/fatigue. There is no established staging system.
- **Course pattern:** Fluctuating/fatigable for the myasthenic component; static-to-slowly-evolving for neurodevelopmental features.
- **Duration:** Lifelong chronic disorder.
- **Remission:** No spontaneous remission. Symptomatic pharmacologic improvement is achievable (see §12).
- **Critical periods:** Early childhood is the key window for seizure control, developmental support, and initiation of NMJ-directed therapy; the developing brain is most vulnerable to uncontrolled epilepsy.

---

## 9. Inheritance and Population

**Epidemiology.** No CMS18-specific prevalence exists (too few cases). The best genetically-confirmed anchor for the CMS umbrella comes from the UK national study (census 31 Dec 2023; 442 patients; Finding F004):

> *"The UK prevalence was 6.5 cases per million overall and 8.5 cases per million in the pediatric population."* — Rossini et al. 2026 ([PMID: 41251564](https://pubmed.ncbi.nlm.nih.gov/41251564/))

Prevalence was higher in regions served by highly specialized neuromuscular centers (8.8 vs 5.9 per million), implying underdiagnosis elsewhere. The common subtypes are *CHRNE*, *DOK7*, and *RAPSN*:

> *"CHRNE deficiency, DOK7, RAPSN were the most common subtypes."* — [PMID: 41251564](https://pubmed.ncbi.nlm.nih.gov/41251564/)

CMS18 (*SNAP25*) is **not** among the common subtypes; it is one of the rarest — only a handful of reported cases worldwide, with the entire broader SNAP25-DEE cohort numbering ~23 individuals ([PMID: 33299146](https://pubmed.ncbi.nlm.nih.gov/33299146/)). A precise CMS18 incidence/prevalence cannot be stated.

**Inheritance (genetic etiology).**
- **Pattern:** **Autosomal dominant**, essentially always **de novo** (index variant arose de novo).
- **Penetrance:** Complete for carriers of the pathogenic de novo variant (each reported carrier is affected).
- **Expressivity:** **Variable** across the *SNAP25* spectrum (myasthenia-predominant vs encephalopathy-predominant), driven largely by the specific variant's synaptic consequence.
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Theoretically possible for de novo dominant variants (recurrence-risk counseling point) but not documented for CMS18.
- **Founder effects / consanguinity:** Not applicable — de novo dominant, not recessive founder-driven (contrast with recessive CMS subtypes such as certain *CHRNE*, *RAPSN*, *DOK7* founder alleles).
- **Carrier frequency:** Not applicable (de novo dominant; unaffected "carriers" essentially do not exist).

**Population demographics.**
- **Affected populations / geography:** No ethnic or geographic clustering — consistent with sporadic de novo occurrence.
- **Sex ratio:** No established sex bias; too few cases.
- **Age distribution:** Onset in infancy/early childhood; patients are predominantly children and young adults.

---

## 10. Diagnostics

**Clinical / electrophysiologic testing.**
- **Repetitive nerve stimulation (RNS):** decrement of the compound muscle action potential on low-frequency (3 Hz) stimulation — abnormal in ~90% of CMS patients ([PMID: 33121830](https://pubmed.ncbi.nlm.nih.gov/33121830/)). For a presynaptic release defect, features may include low baseline CMAP amplitude with facilitation/increment after exercise or high-frequency stimulation (the presynaptic signature seen in other presynaptic disorders such as LEMS and SYT2-related CMS) ([PMID: 26519543](https://pubmed.ncbi.nlm.nih.gov/26519543/)).
- **Single-fiber EMG (SFEMG):** increased jitter and blocking — highly sensitive (~95% in CMS) ([PMID: 33121830](https://pubmed.ncbi.nlm.nih.gov/33121830/)). **LOINC / clinical neurophysiology.**
- **Antibody testing:** anti-AChR and anti-MuSK antibodies **negative** — essential to distinguish CMS18 from autoimmune myasthenia gravis.
- **Serum CK:** typically normal.
- **Brain MRI:** may show brain atrophy in the SNAP25-DEE spectrum ([PMID: 33299146](https://pubmed.ncbi.nlm.nih.gov/33299146/)).
- **EEG:** epileptiform abnormalities / cortical hyperexcitability.

**Genetic testing (the definitive diagnostic modality).**
- **Recommended approach:** Because the phenotype overlaps both CMS and DEE, **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** is the most effective route — this is how the index CMS18 variant was found ([PMID: 25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/)). Trio sequencing (proband + parents) confirms de novo status.
- **Gene panels:** CMS and epileptic-encephalopathy NGS panels that include *SNAP25* (alongside other SNARE genes *STX1B*, *STXBP1*, *VAMP2*).
- **Single-gene testing:** *SNAP25* Sanger confirmation of an identified variant.
- **CMA / karyotype / FISH / mtDNA / repeat testing:** Not indicated — CMS18 is a point-mutation disorder.

**Omics-based diagnostics.** Not part of routine diagnosis; the I67N iPSC-neuron functional/proteomic work ([PMID: 40181518](https://pubmed.ncbi.nlm.nih.gov/40181518/)) is a research characterization, not a clinical assay.

**Clinical criteria & differential diagnosis.** Diagnosis rests on (1) fatigable weakness with decremental RNS / abnormal SFEMG, (2) negative acetylcholine-receptor antibodies, and (3) a pathogenic *SNAP25* variant. **Differential diagnosis:** autoimmune myasthenia gravis (antibody-positive, later onset), Lambert-Eaton myasthenic syndrome (presynaptic, VGCC antibodies, incremental response), other CMS subtypes (*CHRNE*, *DOK7*, *RAPSN*, *SYT2*, *VAMP2*), congenital myopathies, and mitochondrial disorders (CPEO). SFEMG jitter parameters help separate CMS from CPEO/congenital myopathy ([PMID: 33121830](https://pubmed.ncbi.nlm.nih.gov/33121830/)).

**Screening.** No population newborn screening for CMS18. Given de novo dominant inheritance, carrier/cascade screening is generally not applicable (recurrence risk is low but non-zero due to possible germline mosaicism).

---

## 11. Outcome / Prognosis

**Survival / mortality.** No CMS18-specific survival data. CMS in general is not primarily lethal; life expectancy depends on severity of respiratory involvement (episodic apnea in some subtypes) and, for CMS18, on control of epilepsy and neurodevelopmental complications. Disease-specific mortality figures are unavailable given the rarity.

**Morbidity / function.** Substantial: combined motor weakness, intellectual disability, epilepsy, ataxia, and visual impairment produce long-term disability across mobility, cognition, and communication domains. Formal disability/QoL measures (ICF, EQ-5D, PROMIS) have not been applied to a CMS18 cohort.

**Disease course / complications.** Chronic lifelong. Complications include respiratory compromise during myasthenic exacerbations/infections, injury and developmental impact from refractory seizures, and secondary orthopedic issues (e.g., scoliosis seen broadly in chronic childhood NMJ disorders).

**Recovery potential.** No cure; the underlying synaptic defect is permanent. Symptomatic pharmacotherapy can meaningfully improve strength and function (see §12), and seizure control plus rehabilitation can improve developmental trajectory — but the neurodevelopmental deficits are generally not fully reversible.

**Prognostic factors.** Severity of the specific synaptic defect (variant-dependent), degree of epilepsy control, timeliness of correct genetic diagnosis (enabling genotype-appropriate therapy and avoidance of harmful agents), and access to specialized neuromuscular care.

---

## 12. Treatment

**There is no cure. Management is symptomatic, genotype-guided, and multidisciplinary (Finding F005).** The essential principle: CMS drug response is **subtype-specific**, and the wrong drug can worsen the patient.

> *"The majority of patients (96.4%) received specific treatment, including acetylcholinesterase inhibitors in 20, adrenergic agonists in 11 and 3,4-diaminopyridine in nine patients."* — Austrian nationwide CMS cohort ([PMID: 36308527](https://pubmed.ncbi.nlm.nih.gov/36308527/))

> *"Treatment with acetylcholinesterase inhibitors resulted in worsened conditions for most patients."* — DOK7-CMS meta-analysis ([PMID: 24425145](https://pubmed.ncbi.nlm.nih.gov/24425145/))

### Rational pharmacotherapy for a presynaptic release defect (CMS18)

| Drug | Class / mechanism | Rationale for CMS18 | Evidence context | NCIT |
|---|---|---|---|---|
| **3,4-Diaminopyridine (amifampridine)** | Kv potassium-channel blocker; prolongs nerve-terminal depolarization → ↑ Ca²⁺ entry → ↑ ACh release | Directly counteracts the presynaptic release deficit — first-line rational choice | Used in SYT2 presynaptic CMS; general CMS reviews ([PMID: 26519543](https://pubmed.ncbi.nlm.nih.gov/26519543/), [PMID: 26028221](https://pubmed.ncbi.nlm.nih.gov/26028221/), [PMID: 17635211](https://pubmed.ncbi.nlm.nih.gov/17635211/)) | NCIT:C61795 (Amifampridine) |
| **Salbutamol (albuterol) / ephedrine** | β-adrenergic agonists | Improve NMJ function/structure; benefit across several CMS | Strong benefit in severe AChR deficiency ([PMID: 26296515](https://pubmed.ncbi.nlm.nih.gov/26296515/)) and DOK7-CMS ([PMID: 24425145](https://pubmed.ncbi.nlm.nih.gov/24425145/)) | NCIT:C29010 (Albuterol) |
| **Pyridostigmine (AChE inhibitor)** | Prolongs ACh action in the cleft | **Use cautiously** — helpful in postsynaptic AChR-deficiency but can worsen DOK7 and some presynaptic subtypes | Worsened most DOK7 patients ([PMID: 24425145](https://pubmed.ncbi.nlm.nih.gov/24425145/)) | NCIT:C767 (Pyridostigmine) |
| **Antiseizure medications** | Various | Required for the epilepsy component of SNAP25-DEE | Standard DEE management ([PMID: 33299146](https://pubmed.ncbi.nlm.nih.gov/33299146/)) | — |

> *"Oral salbutamol and ephedrine appear to be effective treatments in severe cases of AChR deficiency on pyridostigmine ... improvement in strength can be dramatic."* — [PMID: 26296515](https://pubmed.ncbi.nlm.nih.gov/26296515/)

**Advanced / experimental therapeutics.** No approved gene, cell, or RNA therapy exists for CMS18. Given a dominant, likely dominant-negative de novo variant, allele-selective silencing (ASO/siRNA) is a conceptual future avenue but is not in trials. No CMS18-specific NCT trials are identified.

**Supportive and rehabilitative care.** Physical/occupational/speech therapy, respiratory support during exacerbations, nutritional support, seizure management, developmental/educational support, orthopedic monitoring (scoliosis). **Pharmacogenomics:** the key "pharmacogenomic" principle here is that the causal genotype (*SNAP25* presynaptic release defect) dictates drug selection.

**Treatment strategy (algorithm).** Confirm genetic subtype → classify as presynaptic release defect → prioritize release-enhancing agents (3,4-DAP, β-agonists) → add AChE inhibitor only with caution and monitoring → manage epilepsy and provide multidisciplinary supportive care.

---

## 13. Prevention

- **Primary prevention:** None possible — de novo dominant variants cannot be prevented.
- **Secondary prevention:** Early recognition and correct genetic diagnosis enable prompt, subtype-appropriate therapy and avoidance of harmful drugs — the practical "prevention" of iatrogenic worsening and of complications.
- **Tertiary prevention:** Optimized pharmacotherapy, seizure control, respiratory vigilance during infections, and rehabilitation to prevent disability progression and complications.
- **Immunization:** Not disease-preventive, but standard vaccination is advisable to reduce infection-triggered myasthenic exacerbations (general principle).
- **Genetic screening / counseling:** Because most cases are de novo, recurrence risk to future siblings is low (residual risk from possible germline mosaicism). Genetic counseling should convey de novo status, low but non-zero recurrence risk, and the option of prenatal/preimplantation testing if a familial variant were established. **NSGC/ACMG** counseling frameworks apply.
- **Public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *SNAP25* is highly conserved across vertebrates and invertebrates. Human *SNAP25* (NCBI Gene 6616) has orthologs including mouse *Snap25* (NCBI Gene 20614) and rat *Snap25*; SNARE machinery is conserved to *Drosophila* and *C. elegans* (invertebrate SNARE studies inform mechanism — e.g., tomosyn regulation of SNARE assembly in *C. elegans* [PMID: 17627987](https://pubmed.ncbi.nlm.nih.gov/17627987/), and interchangeable VAMP function in *Drosophila* [PMID: 12364587](https://pubmed.ncbi.nlm.nih.gov/12364587/)).
- **Natural disease in other species:** No well-characterized naturally occurring *SNAP25*-CMS is catalogued in companion animals or wildlife (OMIA does not list a prominent SNAP25 equivalent). Not applicable / not available.
- **Comparative biology:** The SNARE fusion mechanism is deeply evolutionarily conserved; disease mechanisms studied in model synapses translate directly to the human NMJ and central synapses. This conservation underpins the validity of animal and invertebrate models.
- **Transmission / zoonosis:** Not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

- **Human iPSC-derived neurons (primary CMS18 model):** Østergaard et al. 2025 knocked the **I67N** variant into human iPSC-derived NGN2 glutamatergic neurons — the most disease-faithful available model — recapitulating reduced evoked and spontaneous release, decreased release probability, altered short-term plasticity, and proteome changes ([PMID: 40181518](https://pubmed.ncbi.nlm.nih.gov/40181518/)). **Recapitulation:** high fidelity for the synaptic-release phenotype; **limitation:** does not model the intact NMJ, muscle, or whole-organism seizures/ataxia. **Cellosaurus / iPSC.**
- **In vitro reconstitution & chromaffin cells:** Shen et al. 2014 used liposome fusion assays and bovine chromaffin cell exocytosis to demonstrate causality ([PMID: 25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/)).
- **Mouse (*Snap25*):** *Snap25*-null mice reveal that SNAP-25 is essential for evoked release and network activity ([PMID: 18959796](https://pubmed.ncbi.nlm.nih.gov/18959796/), [PMID: 17728451](https://pubmed.ncbi.nlm.nih.gov/17728451/)); isoform-rescue studies (SNAP-25a vs SNAP-25b vs SNAP-23) delineate functional specialization. A knock-in I67N mouse is a logical but (per available literature) not-yet-established disease model. **MGI:** *Snap25*.
- **Invertebrate SNARE models:** *C. elegans* and *Drosophila* SNARE/VAMP/tomosyn studies illuminate the conserved fusion machinery ([PMID: 17627987](https://pubmed.ncbi.nlm.nih.gov/17627987/), [PMID: 12364587](https://pubmed.ncbi.nlm.nih.gov/12364587/)).
- **Applications:** These models enable study of release probability, evoked-vs-spontaneous release dissociation, short-term plasticity, and drug testing (e.g., release enhancers). **Limitation:** no single model captures the full combined myasthenic-plus-encephalopathic human phenotype.

---

## Mechanistic Model / Interpretation

CMS18 is best understood as a **"SNARE bottleneck" disorder**: a single amino-acid change (Ile67→Asn) at the SN1 helix of SNAP-25 degrades the efficiency of the vesicle-fusion machine that every fast chemical synapse depends on. Because the same machine operates at the NMJ and at central synapses, a **single molecular lesion produces a two-compartment disease** — peripheral myasthenia plus central encephalopathy. This is the conceptual bridge between the "CMS18" and "SNAP25-DEE" labels for the same MONDO entity.

```
                 SNAP25 p.I67N (de novo, dominant)
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
   PERIPHERAL (NMJ)                 CENTRAL (brain)
   ↓ ACh quantal release           ↓ glutamatergic/GABAergic release
   ↓ safety margin                 cortical hyperexcitability
   → fatigable weakness            → epilepsy, ataxia, ID
   (treatable: 3,4-DAP, β-agonist) (treat: antiseizure + supportive)
```

The **variant-specific direction of effect on spontaneous release** is the unifying explanatory axis for the whole *SNAP25* spectrum: I67N reduces release (myasthenia-prone), while variants like V48F increase spontaneous release (encephalopathy without myasthenia). This makes *SNAP25* a natural experiment in synaptic physiology and explains why the clinical picture ranges from CMS18-with-myasthenia to pure DEE.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report | Evidence type |
|---|---|---|---|
| [25381298](https://pubmed.ncbi.nlm.nih.gov/25381298/) | *Mutant SNAP25B causes myasthenia, cortical hyperexcitability, ataxia, and ID* | **Defining paper** — identifies I67N, proves causality (liposome + chromaffin assays), documents reduced evoked quantal release at patient endplates | Human clinical + in vitro |
| [33299146](https://pubmed.ncbi.nlm.nih.gov/33299146/) | *De novo variants in SNAP25 cause early-onset DEE* | Defines SNAP25-DEE core phenotype and the "SNAREopathy" concept; places CMS18 in a spectrum (~23 individuals) | Human clinical cohort |
| [40181518](https://pubmed.ncbi.nlm.nih.gov/40181518/) | *SNAP25 variant I67N: synaptic phenotypes, drug response, proteome* | Human iPSC-neuron model confirms I67N reduces evoked+spontaneous release, ↓release probability, plasticity shift | In vitro (human iPSC) |
| [33147442](https://pubmed.ncbi.nlm.nih.gov/33147442/) | *Aberrant spontaneous neurotransmission in SNAP25 encephalopathies* | Explains variant-specific heterogeneity via spontaneous-release alterations | In vitro / model |
| [41251564](https://pubmed.ncbi.nlm.nih.gov/41251564/) | *Prevalence/geographic distribution of CMS in the UK* | Best genetically-confirmed CMS prevalence (6.5/M; 8.5/M pediatric); shows SNAP25 not among common subtypes | Human epidemiology |
| [36308527](https://pubmed.ncbi.nlm.nih.gov/36308527/) | *Clinical/molecular landscape of CMS in Austria* | Real-world treatment distribution (AChE-I, adrenergics, 3,4-DAP) | Human cohort |
| [24425145](https://pubmed.ncbi.nlm.nih.gov/24425145/) | *Pharmacologic treatment of DOK7-CMS* | Demonstrates drug response is subtype-specific; AChE-I can worsen | Human meta-analysis |
| [26296515](https://pubmed.ncbi.nlm.nih.gov/26296515/) | *Salbutamol/ephedrine in severe AChR deficiency* | Evidence for β-agonist efficacy in CMS | Human cohort |
| [26519543](https://pubmed.ncbi.nlm.nih.gov/26519543/) | *SYT2 presynaptic CMS* | Model for presynaptic-CMS diagnostics and 3,4-DAP response | Human clinical |
| [26028221](https://pubmed.ncbi.nlm.nih.gov/26028221/) / [17635211](https://pubmed.ncbi.nlm.nih.gov/17635211/) | CMS drug-therapy reviews | Rationale/indications for 3,4-DAP and other agents by CMS level | Review |
| [33121830](https://pubmed.ncbi.nlm.nih.gov/33121830/) | *Electrophysiology of NMJ in CMS* | RNS/SFEMG sensitivity for CMS diagnosis | Human clinical |
| [18959796](https://pubmed.ncbi.nlm.nih.gov/18959796/) / [17728451](https://pubmed.ncbi.nlm.nih.gov/17728451/) | SNAP-25 isoform/knockout studies | Establish SNAP-25 necessity for evoked release and isoform specialization | Model organism |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity → thin clinical evidence.** CMS18 rests largely on a single index patient (Shen 2014) plus the broader ~23-individual SNAP25-DEE cohort. No CMS18-specific prevalence, survival, natural-history, or QoL data exist; epidemiology is borrowed from the CMS umbrella.
2. **Treatment evidence is extrapolated.** The recommended genotype-guided approach (3,4-DAP, β-agonists) is rational and grounded in presynaptic-CMS literature (SYT2, general reviews), but there is **no dedicated CMS18 treatment trial**. Direct evidence of drug response specifically in CMS18 patients is minimal (the iPSC drug-response work is a cell model).
3. **Genotype–phenotype breadth.** Whether other *SNAP25* variants can produce a myasthenia-predominant CMS18 phenotype (vs pure DEE), and what determines the myasthenic vs encephalopathic balance, is only partially explained by the spontaneous-release-direction hypothesis.
4. **No whole-animal I67N model** is established to test therapies for the combined NMJ + CNS phenotype in vivo.
5. **No CMS18-specific omics beyond the single iPSC proteome study;** transcriptomic/metabolomic signatures are absent.
6. **Recurrence-risk data (germline mosaicism)** for *SNAP25* are not quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Build a knock-in I67N mouse** (or refine iPSC-derived NMJ/organoid co-cultures) to model the combined myasthenic + encephalopathic phenotype and to test 3,4-DAP, β-agonists, and antiseizure combinations in vivo.
2. **Systematic drug-response profiling in patient iPSC neurons** — extend the Østergaard model to screen release-enhancers (3,4-DAP analogs, β-agonists) and candidate allele-selective ASOs for their ability to normalize release probability.
3. **Establish an international CMS18/SNAP25 patient registry** to aggregate phenotype, natural history, treatment response, and outcomes across the handful of cases worldwide — the only feasible route to real prevalence and prognosis estimates.
4. **Genotype–function map** of all reported *SNAP25* variants correlating evoked-vs-spontaneous release direction with myasthenic vs encephalopathic clinical weighting, to build a predictive framework for prognosis and drug choice.
5. **Prospective electrophysiology** (RNS with post-exercise facilitation testing; SFEMG) in *SNAP25* patients to confirm the presynaptic signature and define diagnostic criteria specific to CMS18.
6. **Explore allele-selective silencing** (ASO/siRNA) as a mechanism-directed therapy for this dominant, dominant-negative variant.

---

*Report compiled from 6 confirmed findings across 5 investigation iterations and 37 reviewed papers. Ontology identifiers verified via EBI OLS4 (MONDO:0014590 → OMIM:616330). Gene identifiers: SNAP25, HGNC:11132, NCBI Gene 6616.*


## Artifacts

- [OpenScientist final report](Congenital_Myasthenic_Syndrome_18-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Myasthenic_Syndrome_18-deep-research-openscientist_artifacts/final_report.pdf)