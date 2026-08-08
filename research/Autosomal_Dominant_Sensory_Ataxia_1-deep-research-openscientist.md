---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-01T11:47:31.079453'
end_time: '2026-08-01T12:13:13.073292'
duration_seconds: 1541.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Sensory Ataxia 1
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
  path: Autosomal_Dominant_Sensory_Ataxia_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Dominant_Sensory_Ataxia_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Sensory Ataxia 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Sensory Ataxia 1** covering all of the
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

# Autosomal Dominant Sensory Ataxia 1 (ADSA1): Comprehensive Disease Characterization Report

**Disease:** Autosomal Dominant Sensory Ataxia 1 (ADSA1)
**Primary identifiers:** MONDO:0012166 · OMIM #608984 · DOID:0111170 · GARD:0024850 · MedGen:332346 · UMLS:C1837015
**Causal gene:** *RNF170* (OMIM *614649; HGNC:25358; NCBI Gene 81790; Ensembl ENSG00000120925; locus 8p11.21)
**Category:** Mendelian, monogenic, autosomal dominant

---

## Summary

Autosomal Dominant Sensory Ataxia 1 (ADSA1; also SNAX1, ADSA, "RNF170 hereditary ataxia") is an ultra-rare, adult/middle-age–onset, slowly progressive hereditary **sensory (proprioceptive) ataxia**. It is caused by a single recurrent heterozygous missense mutation in *RNF170*, **c.595C>T p.(Arg199Cys)**, and results clinically from degeneration of the posterior (dorsal) columns of the spinal cord and a length-dependent sensory neuronopathy/neuropathy. It was originally described in two large founder families from Maritime Canada [PMID: 21115467](https://pubmed.ncbi.nlm.nih.gov/21115467/) and has since been independently replicated in a Belgian family [PMID: 34469621](https://pubmed.ncbi.nlm.nih.gov/34469621/) and reported as a **CANVAS mimic** (sensory ataxic neuropathy with vestibular areflexia) [PMID: 32943585](https://pubmed.ncbi.nlm.nih.gov/32943585/). The disease is exceedingly rare, reported in only a handful of families/individuals worldwide.

Mechanistically, RNF170 is an **endoplasmic reticulum (ER)–membrane RING-type E3 ubiquitin ligase** that, together with the ERLIN1/2 (SPFH-family) scaffold and TMUB1, forms an ERAD "nanodomain" that ubiquitinates activated **type-1 inositol 1,4,5-trisphosphate receptors (IP3R/ITPR1)** and targets them for proteasomal degradation [PMID: 21610068](https://pubmed.ncbi.nlm.nih.gov/21610068/); [PMID: 38782601](https://pubmed.ncbi.nlm.nih.gov/38782601/). The Arg199Cys mutation **destabilizes RNF170** by enhancing its autoubiquitination and proteasomal turnover, and functionally **impairs IP3R-mediated Ca²⁺ mobilization** in patient cells despite normal ER store content, IP3R levels, and IP3 production — pinpointing a defect at the IP3R signaling locus [PMID: 25882839](https://pubmed.ncbi.nlm.nih.gov/25882839/). *Rnf170*-knockout mice recapitulate age-dependent gait abnormalities, reduced proprioception and thermal nociception, and elevated ITPR1 protein in cerebellum and spinal cord [PMID: 26433933](https://pubmed.ncbi.nlm.nih.gov/26433933/).

Notably, *RNF170* exhibits a clear **allelic series**: the dominant p.Arg199Cys missense allele causes ADSA1, whereas **biallelic loss-of-function** *RNF170* variants cause a distinct autosomal recessive complicated hereditary spastic paraplegia, **SPG85** (MONDO:0030512; OMIM #619686) [PMID: 31636353](https://pubmed.ncbi.nlm.nih.gov/31636353/); [PMID: 36046950](https://pubmed.ncbi.nlm.nih.gov/36046950/); [PMID: 35041108](https://pubmed.ncbi.nlm.nih.gov/35041108/). There is no disease-specific therapy; management is supportive (physiotherapy, gait/balance aids, sensory rehabilitation, fall prevention).

---

## Section 1 — Disease Information

**Overview.** ADSA1 is a monogenic, autosomal dominant, adult-onset **sensory ataxia** — an inability to coordinate movement due to loss of proprioceptive (position/vibration) sensation rather than primary cerebellar disease. Patients develop insidious, slowly progressive gait instability that is characteristically **worse in the dark or with eyes closed** (loss of visual compensation for absent proprioception), a positive Romberg sign, distal sensory loss, and areflexia; cerebellar imaging is typically normal.

**Key identifiers.**
- **MONDO:** MONDO:0012166 — *"Any hereditary ataxia in which the cause of the disease is a mutation in the RNF170 gene."*
- **OMIM:** #608984 (phenotype); *614649 (gene *RNF170*, allelic variant 614649.0001)
- **DOID:** 0111170 · **GARD:** 0024850 · **MedGen:** 332346 · **UMLS:** C1837015
- **Orphanet:** no dedicated code cross-referenced to ADSA1
- **ICD-10/ICD-11 / MeSH:** no ADSA1-specific code; classified under hereditary/spinocerebellar ataxia categories

**Synonyms:** SNAX1; ADSA; "ataxia, sensory, 1, autosomal dominant"; "RNF170 hereditary ataxia"; "sensory ataxic neuropathy with vestibular areflexia (CANVAS mimic)."

**Information source type:** Aggregated disease-level resources (OMIM, MONDO, HPO) plus **individual patient reports** from a small number of published families (Maritime-Canada founder families; Belgian family; scattered single cases).

---

## Section 2 — Etiology

**Primary cause — genetic.** ADSA1 is **entirely genetic and monogenic**, caused by the heterozygous *RNF170* missense variant **c.595C>T p.(Arg199Cys)**. No environmental or infectious cause is implicated.

**Genetic risk factors.** The single causal allele is the dominant R199C variant; inheritance of one copy is sufficient to cause disease. Reported penetrance in pedigrees is high. There are no established susceptibility loci or GWAS signals (the disease is Mendelian, not complex).

**Environmental risk factors / protective factors / gene–environment interactions.** None identified. As a fully penetrant dominant Mendelian disorder, no dietary, occupational, or lifestyle risk or protective factors are known, and no gene–environment interactions have been reported.

---

## Section 3 — Phenotypes (with HPO terms)

Frequencies below derive largely from the HPO/OMIM:608984 annotation set (Cortese et al. 2020, n=2 affected) supplemented by OMIM clinical synopsis and case reports. Given the tiny sample, frequencies are indicative.

| HPO term | Phenotype | Type | Frequency |
|---|---|---|---|
| HP:0010871 | Sensory ataxia | Clinical sign | 2/2 |
| HP:0002066 | Gait ataxia | Clinical sign | 2/2 |
| HP:0003596 | Middle-age onset | Onset | 2/2 |
| HP:0001265 | Hyporeflexia | Clinical sign | 2/2 |
| HP:0003409 | Distal sensory impairment (all modalities) | Clinical sign | 2/2 |
| HP:0006858 | Impaired distal proprioception | Clinical sign | 1/2 |
| HP:0006886 | Impaired distal vibration sensation | Clinical sign | 1/2 |
| HP:0007078 | Decreased amplitude of sensory action potentials | Electrophysiology | 1/2 |
| HP:0002403 | Positive Romberg sign | Clinical sign | reported |
| HP:0006962 | Gait instability worse in the dark | Symptom | OMIM |
| HP:0001284 | Areflexia | Clinical sign | OMIM |
| HP:0012534 | Dysesthesia | Symptom | reported |
| HP:0001260 | Dysarthria | Clinical sign | reported |
| HP:0007670 | Abnormal vestibulo-ocular reflex / vestibular areflexia | Clinical sign | 1/2 |
| HP:0002359 | Frequent falls | Symptom | reported |
| HP:0001317 | Abnormal cerebellar morphology | Imaging | 0/1 (usually normal) |
| HP:0003487 | Babinski sign | Clinical sign | 0/1 (usually absent) |

**Characteristics.** Age of onset: **adult/middle age** (HP:0003596). Severity: mild-to-moderate initially, progressing to significant gait disability. Progression: **slowly progressive** over years to decades. The Belgian family additionally showed **variable pyramidal involvement** [PMID: 34469621](https://pubmed.ncbi.nlm.nih.gov/34469621/), and one atypical case presented with **hypertrophic olivary degeneration** [PMID: 42052314](https://pubmed.ncbi.nlm.nih.gov/42052314/).

**Quality-of-life impact.** Progressive gait instability, frequent falls, and dependence on assistive devices impair mobility, independence, and safety; sensory dysesthesia may add discomfort. No formal EQ-5D/SF-36 data exist for this ultra-rare disease.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** *RNF170* (RING finger protein 170), locus **8p11.21**; OMIM *614649; HGNC:25358; NCBI Gene 81790; Ensembl ENSG00000120925; UniProt Q96K19.

**Pathogenic variant (ADSA1):**
- **NM_030954.4(RNF170):c.595C>T (p.Arg199Cys)**; GRCh38 chr8:42,856,340 G>A
- **ClinVar:** Pathogenic, 2-star ("criteria provided, multiple submitters, no conflicts")
- **dbSNP:** rs397514478 · **ClinGen:** CA129827 · **UniProt variant:** VAR_068219 · **OMIM allelic variant:** 614649.0001
- **Variant type:** missense (single-nucleotide substitution), germline
- **Allele frequency:** **absent from gnomAD v4** (ACMG PM2 supporting)
- **Functional consequence:** destabilizes RNF170 (enhanced autoubiquitination/proteasomal degradation) with impaired IP3R-mediated Ca²⁺ signaling — behaving as a **dominant** allele; distinct from recessive LoF

**Allelic series / other *RNF170* variants (SPG85, recessive):** p.Arg64* [PMID: 36046950](https://pubmed.ncbi.nlm.nih.gov/36046950/); p.Cys107Trp (homozygous) [PMID: 35041108](https://pubmed.ncbi.nlm.nih.gov/35041108/); additional biallelic variants in HSP cohorts [PMID: 31636353](https://pubmed.ncbi.nlm.nih.gov/31636353/); [PMID: 38499745](https://pubmed.ncbi.nlm.nih.gov/38499745/).

**Modifier genes / epigenetics / chromosomal abnormalities:** None specifically established for ADSA1. RNF170 functions within the ERLIN1/2–TMUB1–RNF170 ERAD complex, so those partner genes are mechanistically relevant [PMID: 38782601](https://pubmed.ncbi.nlm.nih.gov/38782601/).

---

## Section 5 — Environmental Information

No environmental, lifestyle, or infectious factors are implicated in ADSA1. It is a purely genetic Mendelian disorder. **Not applicable.**

---

## Section 6 — Mechanism / Pathophysiology

**Molecular function of RNF170.** RNF170 is an ER-membrane RING E3 ubiquitin ligase that binds activated IP3 receptors — recruited via the erlin1/2 SPFH complex — and mediates their ubiquitination and ER-associated degradation (ERAD): *"RNF170 plays an essential role in IP3 receptor processing via the ubiquitin-proteasome pathway"* [PMID: 21610068](https://pubmed.ncbi.nlm.nih.gov/21610068/). It operates within an **ERLIN1/2–TMUB1–RNF170 ERAD nanodomain**: *"ERLIN scaffolds mediate the interaction between the full-length isoform of TMUB1 ... and RNF170"* [PMID: 38782601](https://pubmed.ncbi.nlm.nih.gov/38782601/).

**Protein dysfunction.** The Arg199Cys mutation **destabilizes RNF170**: *"Inhibited expression of mutant RNF170 was seen in cells expressing exogenous RNF170 constructs and in ADSA lymphoblasts, and appears to result from enhanced RNF170 autoubiquitination and proteasomal degradation"* [PMID: 25882839](https://pubmed.ncbi.nlm.nih.gov/25882839/). Arg199 sits at the C-terminal end of the large cytoplasmic loop, immediately N-terminal to TM2 (residues 202–222), consistent with disruption of stabilizing transmembrane ionic interactions.

**Metabolic / signaling change.** The proximal downstream consequence is dysregulated ER Ca²⁺ signaling: *"In ADSA lymphoblasts, platelet-activating factor-induced Ca²⁺ mobilization was significantly impaired"* — despite normal ER store content, IP3R levels, and IP3 production, localizing the defect to the IP3R response [PMID: 25882839](https://pubmed.ncbi.nlm.nih.gov/25882839/). In *Rnf170*-null mice, **ITPR1 protein accumulates selectively in cerebellum and spinal cord** (not cerebral cortex) [PMID: 26433933](https://pubmed.ncbi.nlm.nih.gov/26433933/).

**Causal chain (upstream → downstream):**

```
RNF170 c.595C>T (p.Arg199Cys)  [germline, heterozygous]
        │  Arg199 at TM2 boundary → loss of stabilizing ionic interactions
        ▼
Enhanced RNF170 autoubiquitination → proteasomal degradation (↓ functional RNF170)
        ▼
Impaired ERLIN1/2–TMUB1–RNF170 ERAD nanodomain → defective ITPR1 turnover
        ▼
Dysregulated ER Ca²⁺ signaling (↓ agonist-evoked Ca²⁺ mobilization; ITPR1 accumulation)
        ▼
Chronic sensory-neuron / dorsal-column dysfunction & degeneration
        ▼
Adult-onset, slowly progressive SENSORY (proprioceptive) ATAXIA
```

**GO / CL terms.** Biological process: GO:0070936 (protein K48-linked ubiquitination), GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process), GO:0006816 (calcium ion transport). Molecular function: GO:0061630 (ubiquitin protein ligase activity), GO:0008270 (zinc ion binding). Cellular component: GO:0005789 (ER membrane). Cell types: CL:0000101 (sensory neuron), CL:0000209 (dorsal root ganglion neuron), CL:0000121 (Purkinje cell — secondary).

**Immune involvement.** RNF170 has a described role in **negative regulation of TLR3 signaling** (GO:0034140), but immune dysfunction is not part of the ADSA1 phenotype.

---

## Section 7 — Anatomical Structures Affected

- **Organ/system level:** Nervous system — specifically the **posterior (dorsal) columns of the spinal cord** (UBERON:0002240 spinal cord) and peripheral **sensory nerves / dorsal root ganglia**. Vestibular pathways in CANVAS-mimic cases. Cerebellum (UBERON:0002037) is typically **spared** morphologically.
- **Tissue/cell level:** Nervous tissue; large **proprioceptive sensory neurons** (CL:0000101, CL:0000209).
- **Subcellular level:** **Endoplasmic reticulum membrane** (GO:0005789).
- **Localization/lateralization:** **Bilateral, symmetric, length-dependent** sensory involvement. One atypical case showed bilateral inferior olivary hypertrophy (hypertrophic olivary degeneration) with mild cerebellar atrophy [PMID: 42052314](https://pubmed.ncbi.nlm.nih.gov/42052314/).

---

## Section 8 — Temporal Development

- **Onset:** Adult/middle age (HP:0003596); insidious/chronic.
- **Progression:** Slowly progressive over years-to-decades; disease course is **progressive**, not episodic or relapsing–remitting.
- **Duration:** Chronic, lifelong.
- **Remission:** None (no spontaneous or treatment-induced remission).
- **Critical periods:** The slow tempo provides a broad window for supportive/rehabilitative intervention.

---

## Section 9 — Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant** (OMIM #608984).
- **Penetrance / expressivity:** Apparently high penetrance in reported pedigrees; **variable expressivity** (e.g., variable pyramidal involvement) [PMID: 34469621](https://pubmed.ncbi.nlm.nih.gov/34469621/).
- **Founder effect:** The two Maritime-Canada families share a disease haplotype, indicating a **founder allele** [PMID: 21115467](https://pubmed.ncbi.nlm.nih.gov/21115467/).
- **Carrier frequency:** R199C is **absent from gnomAD** — effectively zero in general populations.
- **Anticipation / mosaicism / consanguinity:** No anticipation (not a repeat expansion); consanguinity is irrelevant for a dominant disorder (it is relevant only for recessive SPG85).
- **Epidemiology:** No formal prevalence/incidence; **ultra-rare** (<1/1,000,000), reported in only ~3 families plus scattered single cases.
- **Sex ratio / demographics:** No sex bias reported; reported cases are of European (Canadian, Belgian) ancestry, reflecting ascertainment.

---

## Section 10 — Diagnostics

- **Clinical/electrophysiology:** Sensory nerve conduction studies show **reduced/absent SNAPs** (HP:0007078) with preserved motor conduction — the signature of a sensory neuronopathy/neuropathy. Bedside: positive Romberg, areflexia, distal sensory loss.
- **Imaging:** MRI typically **normal cerebellum** (helps distinguish from cerebellar ataxias); rare HOD on MRI [PMID: 42052314](https://pubmed.ncbi.nlm.nih.gov/42052314/).
- **Genetic testing (diagnostic gold standard):** Detection of *RNF170* c.595C>T p.(Arg199Cys) by **single-gene testing**, **hereditary-ataxia/HSP gene panels**, or **whole-exome/whole-genome sequencing**. WES/WGS are high-yield given phenotypic overlap with other ataxias.
- **Clinical criteria / differential diagnosis:** Differentiate from **CANVAS/RFC1** disease (exclude *RFC1* biallelic AAGGG expansion), paraneoplastic sensory neuronopathy (anti-Hu), Sjögren-associated ganglionopathy, vitamin E/B12 deficiency, chemotherapy (cisplatin) toxicity, and Friedreich ataxia. The CANVAS-mimic framing makes *RNF170* testing important in adult sensory ataxic neuropathy [PMID: 32943585](https://pubmed.ncbi.nlm.nih.gov/32943585/).
- **Screening:** Cascade genetic testing of at-risk relatives once a familial variant is known.

---

## Section 11 — Outcome / Prognosis

- **Survival/mortality:** **Not life-shortening** in reported families; no disease-specific mortality documented.
- **Morbidity/function:** Progressive gait disability, falls, and eventual dependence on assistive devices are the main morbidities. Long-term functional impairment centers on mobility and balance (ICF domains).
- **Complications:** Fall-related injury; secondary deconditioning.
- **Recovery:** No spontaneous recovery; supportive care can maintain function.
- **Prognostic factors:** Genotype (R199C) defines the disease; no validated molecular prognostic biomarkers beyond the causal variant.

---

## Section 12 — Treatment

- **Disease-modifying therapy:** **None available.**
- **Supportive/rehabilitative (mainstay):** Physical therapy and **balance/gait training** (NCIT: Physical Therapy), occupational therapy, assistive devices (cane/walker), fall-prevention strategies, and management of neuropathic dysesthesia.
- **Pharmacotherapy / advanced therapeutics:** No approved drugs, gene, cell, or RNA therapies. Mechanistically rational but unproven concepts include **proteostasis modulation** (given enhanced RNF170 degradation) and **IP3R/ER-Ca²⁺-signaling–targeted** approaches.
- **Pharmacogenomics / experimental trials:** None specific to ADSA1.
- **NCIT intervention terms:** Physical Therapy; Occupational Therapy; Supportive Care.

---

## Section 13 — Prevention

- **Primary/secondary/tertiary prevention:** No primary prevention (fully genetic). Tertiary prevention = fall-prevention and rehabilitation.
- **Genetic counseling:** Central — 50% offspring transmission risk for a heterozygous parent; cascade testing for at-risk relatives.
- **Reproductive options:** Prenatal and **preimplantation genetic testing** are feasible given the defined pathogenic variant.
- **Immunization / behavioral / public-health interventions:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthologs (NCBI Gene):** mouse *Rnf170* (77733; MGI:1924983; ENSMUSG00000013878); zebrafish *rnf170* (406612; ENSDARG00000104069); dog *RNF170* (475568).
- **Natural disease (dog):** A naturally occurring **Miniature American Shepherd** neuroaxonal dystrophy is caused by an *RNF170* 1-bp deletion: *"The underlying genetic cause was identified as a 1-bp (base pair) deletion in RNF170 ... which perfectly segregates in an autosomal recessive pattern"* [PMID: 39177409](https://pubmed.ncbi.nlm.nih.gov/39177409/). This is a **recessive LoF** model (comparative to SPG85 more than to dominant ADSA1) but demonstrates conserved neurodegenerative consequences of *RNF170* dysfunction.
- **Evolutionary conservation:** RNF170's IP3R-ERAD function is conserved, supporting cross-species mechanistic relevance.

---

## Section 15 — Model Organisms

| Model | Type | Key features | Recapitulation | Reference |
|---|---|---|---|---|
| *Rnf170⁻/⁻* mouse | Mammalian knockout (LoF) | Age-dependent gait abnormality; reduced proprioception & thermal nociception; ITPR1 accumulation in cerebellum/spinal cord | Reproduces sensory/gait phenotype and pathway; but LoF (models SPG85 mechanism more than dominant R199C) | [PMID: 26433933](https://pubmed.ncbi.nlm.nih.gov/26433933/) |
| Zebrafish (*rnf170*) | Vertebrate | Mutant orthologous mRNA dominantly disrupts development | Supports dominant action of the mutant allele | [PMID: 21115467](https://pubmed.ncbi.nlm.nih.gov/21115467/) |
| Miniature American Shepherd dog | Natural, mammalian | Recessive frameshift → neuroaxonal dystrophy | Comparative neurodegeneration model | [PMID: 39177409](https://pubmed.ncbi.nlm.nih.gov/39177409/) |
| Patient lymphoblasts / transfected cells | In vitro | Destabilized mutant RNF170; impaired PAF-induced Ca²⁺ | Direct human mechanistic model | [PMID: 25882839](https://pubmed.ncbi.nlm.nih.gov/25882839/) |

**Model limitation:** No **R199C knock-in** animal exists; the available in-vivo models are loss-of-function/recessive and therefore incompletely capture the dominant ADSA1 allele.

---

## Mechanistic Model / Interpretation (Synthesis)

ADSA1 is best understood as a **dominant, protein-destabilizing disruption of ER quality control over calcium signaling** in sensory neurons. The upstream molecular lesion is destabilization of the E3 ligase RNF170; the proximal downstream consequence is failure of IP3R (ITPR1) ubiquitin/ERAD turnover and consequent Ca²⁺-signaling dysregulation; the distal, tissue-level outcome is selective vulnerability of large proprioceptive neurons and dorsal-column pathways, producing adult-onset sensory ataxia.

A central conceptual puzzle: R199C **lowers mutant-protein levels** (a loss-of-function–like biochemical signature), yet the disease is **dominant** and *distinct* from the recessive complete-LoF disorder SPG85 (spasticity). This argues that R199C acts through a **dominant-negative or dosage-sensitive** mechanism within the multiprotein ERLIN1/2–TMUB1–RNF170 nanodomain — i.e., the destabilized mutant "poisons" the complex or perturbs stoichiometry — rather than through simple haploinsufficiency. Resolving this remains the key open mechanistic question.

**Allelic-series comparison:**

| Feature | ADSA1 | SPG85 |
|---|---|---|
| *RNF170* allele | Dominant missense p.Arg199Cys | Biallelic loss-of-function (nonsense/frameshift/missense) |
| Inheritance | Autosomal dominant | Autosomal recessive |
| Onset | Adult/middle age | Infancy/childhood |
| Core phenotype | Sensory (proprioceptive) ataxia | Spastic paraplegia (± complex features) |
| IDs | MONDO:0012166; OMIM #608984 | MONDO:0030512; OMIM #619686; Orphanet:631082 |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [21115467](https://pubmed.ncbi.nlm.nih.gov/21115467/) | *RNF170 mutation causes ADSA* | Human genetics + zebrafish | Original discovery; establishes *RNF170* R199C as causal |
| [34469621](https://pubmed.ncbi.nlm.nih.gov/34469621/) | *RNF170 ADSA with variable pyramidal involvement* | Human genetics | Independent replication (Belgian family) |
| [32943585](https://pubmed.ncbi.nlm.nih.gov/32943585/) | *RNF170 CANVAS mimic* | Human clinical | Vestibular-areflexia/CANVAS-mimic phenotype; HPO source |
| [25882839](https://pubmed.ncbi.nlm.nih.gov/25882839/) | *R199C destabilizes RNF170; impairs IP3R Ca²⁺ signaling* | In vitro/biochemistry | Core mechanistic study |
| [21610068](https://pubmed.ncbi.nlm.nih.gov/21610068/) | *RNF170 mediates IP3R ubiquitination/degradation* | In vitro | Establishes RNF170 molecular function |
| [26433933](https://pubmed.ncbi.nlm.nih.gov/26433933/) | *Rnf170⁻/⁻ mice, age-dependent gait* | Mouse model | In-vivo pathway validation; ITPR1 accumulation |
| [38782601](https://pubmed.ncbi.nlm.nih.gov/38782601/) | *ERLIN1/2–TMUB1–RNF170 ERAD nanodomain* | In vitro | Places RNF170 in ERAD complex |
| [31636353](https://pubmed.ncbi.nlm.nih.gov/31636353/) | *Bi-allelic RNF170 → HSP* | Human genetics | Recessive allelic disorder (SPG85) |
| [36046950](https://pubmed.ncbi.nlm.nih.gov/36046950/) | *Stop-gain RNF170 → HSP (p.R64*)* | Human genetics | Recessive LoF → SPG85 |
| [35041108](https://pubmed.ncbi.nlm.nih.gov/35041108/) | *Homozygous RNF170 p.Cys107Trp → HSP* | Human genetics | Recessive missense → SPG85 |
| [39177409](https://pubmed.ncbi.nlm.nih.gov/39177409/) | *Canine RNF170 model of neuroaxonal dystrophy* | Animal (natural) | Comparative model |
| [42052314](https://pubmed.ncbi.nlm.nih.gov/42052314/) | *RNF170 with hypertrophic olivary degeneration* | Human clinical | Phenotype expansion |
| [38499745](https://pubmed.ncbi.nlm.nih.gov/38499745/) | *WES in Serbian HSP* | Human genetics | *RNF170* in HSP cohort |

**Consistency:** All human genetic reports converge on *RNF170* c.595C>T p.(Arg199Cys) as the recurrent ADSA1 allele; in-vitro and mouse-model data coherently support IP3R/Ca²⁺ dysregulation via impaired ERAD. The apparent tension — a "destabilizing" (LoF-like) mutation causing a dominant disease distinct from recessive LoF SPG85 — points to a dominant-negative/dosage mechanism rather than haploinsufficiency.

---

## Limitations and Knowledge Gaps

- **Extreme rarity / small n:** Phenotype frequencies derive from very few affected individuals (HPO annotations largely n=2); percentages are indicative, not epidemiologic.
- **Unresolved dominance mechanism:** Whether R199C is dominant-negative, a toxic gain of function, or dosage-sensitive nanodomain poisoning is not definitively established. No R199C **knock-in** animal exists; existing mouse/dog models are LoF/recessive and better model SPG85.
- **No formal epidemiology:** Prevalence, incidence, penetrance, and sex/age distributions are not rigorously quantified.
- **No dedicated Orphanet code** for ADSA1; nosology overlaps with CANVAS and other sensory neuronopathies.
- **No therapeutics or biomarkers:** No disease-modifying treatment, prognostic biomarker, or ADSA1-specific clinical trial.
- **Limited human neuropathology:** Direct human confirmation of dorsal-column/DRG degeneration and ITPR1 accumulation is sparse; most molecular evidence is from patient lymphoblasts, transfected cells, and mouse tissue.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in *Rnf170^R199C/+* mouse** (and iPSC-derived sensory neurons) to test dominant-negative vs. dosage mechanisms and directly model ADSA1 rather than SPG85.
2. **Structural/biophysical study of Arg199Cys** at the TM2 boundary (cryo-EM/AlphaFold-guided mutagenesis) to define how the mutation destabilizes RNF170 and perturbs the ERLIN1/2–TMUB1–RNF170 nanodomain.
3. **Quantify ITPR1 turnover and ER Ca²⁺ dynamics** in patient-derived DRG-like neurons; test whether restoring RNF170 levels or modulating proteasomal degradation rescues Ca²⁺ signaling.
4. **International case ascertainment/registry** (GeneMatcher, ataxia consortia) to refine phenotype frequencies, penetrance, progression rate, and identify additional alleles/founder haplotypes.
5. **Systematic differential-diagnosis workflow:** pair *RNF170* testing with *RFC1* CANVAS exclusion in adult sensory ataxic neuropathy cohorts to estimate ADSA1's diagnostic yield.
6. **Proof-of-concept therapeutics:** evaluate proteostasis modulators or IP3R/Ca²⁺-signaling agents in cellular and knock-in models.

---

*Evidence-source legend:* human clinical/genetic (family and case reports); in-vitro (patient lymphoblasts, transfected cells, biochemistry); model organism (mouse, zebrafish, dog); computational/ontology (MONDO, HPO, UniProt, ClinVar, gnomAD).


## Artifacts

- [OpenScientist final report](Autosomal_Dominant_Sensory_Ataxia_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Dominant_Sensory_Ataxia_1-deep-research-openscientist_artifacts/final_report.pdf)