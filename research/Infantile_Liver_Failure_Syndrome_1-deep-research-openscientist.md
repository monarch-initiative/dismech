---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T10:12:42.248308'
end_time: '2026-08-28T10:39:37.097243'
duration_seconds: 1614.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infantile Liver Failure Syndrome 1
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
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 11
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Infantile_Liver_Failure_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Infantile_Liver_Failure_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile Liver Failure Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile Liver Failure Syndrome 1** covering all of the
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

# Infantile Liver Failure Syndrome 1 (ILFS1): A Comprehensive Disease Report

**Disease:** Infantile Liver Failure Syndrome 1 (ILFS1)
**Gene:** *LARS1* (cytosolic leucyl-tRNA synthetase 1)
**Category:** Mendelian, autosomal recessive
**Key identifiers:** OMIM #615438 (disease); OMIM *151350 / HGNC:6512 (*LARS1*); Orphanet ORPHA:463328; UniProt Q9P2J5; NCBI Gene 51520; reference transcript NM_020117.11; locus 5q31.3–q33.1 (5q32); suggested MONDO: MONDO:0014220
**Evidence base:** Human clinical case series/reviews, patient-derived cellular assays, zebrafish models, and biochemical mechanistic studies. Synthesized from **aggregated disease-level literature and case series** (not individual EHR data).

---

## Summary

Infantile Liver Failure Syndrome type 1 (ILFS1; OMIM #615438) is a rare autosomal-recessive multisystem disorder caused by biallelic hypomorphic (predominantly missense) variants in *LARS1*, the gene encoding cytosolic leucyl-tRNA synthetase. The enzyme has two essential and mechanistically distinct roles: (1) it charges cytoplasmic tRNA^Leu with leucine to enable protein translation, and (2) it "moonlights" as the intracellular leucine sensor that activates the mechanistic target of rapamycin complex 1 (mTORC1) by acting as a GTPase-activating protein (GAP) for the Rag GTPase. Loss of function in both arms explains the disease's defining feature — **fever-triggered, recurrent acute liver failure and encephalopathy** superimposed on a background of intrauterine growth restriction, failure to thrive, hypoalbuminemia, and microcytic anemia.

The pathophysiology is dual and unified by a temperature-sensitivity mechanism. Patient-derived fibroblasts show aminoacylation activity that is reduced at baseline and further diminished at febrile temperatures (38.5–40 °C), rendering the mutant enzyme rate-limiting for translation precisely when protein-synthetic demand rises during infection. Simultaneously, loss of the LARS1 leucine-sensing/Rag-GAP function downregulates mTORC1 and drives excessive autophagy, a mechanism directly modeled in zebrafish *larsb* mutants. This convergence of "insufficient aminoacylation to meet translational demands" during febrile catabolic stress establishes infancy and fever episodes as the critical window of vulnerability and the primary target for intervention.

Prognosis is guided by early onset (<3 months) and the presence of liver failure, both of which confer significantly poorer survival. Management remains largely supportive, but a mechanism-based disease-modifying therapy — supplementation with the cognate amino acid **L-leucine** — has shown benefit in growth, development, and liver/lung disease in the majority of treated patients, though it does not rescue the most severe phenotypes. Liver transplantation is reserved for end-stage or recurrent liver failure. Diagnosis rests on whole-exome/whole-genome sequencing, supported by a characteristic biochemical profile and a confirmatory temperature-dependent fibroblast aminoacylation assay. This report synthesizes 12 confirmed findings drawn from 21 reviewed papers spanning human clinical cohorts, in vitro functional studies, and zebrafish models.

---

## 1. Disease Information

ILFS1 is a Mendelian, autosomal-recessive inborn error caused by biallelic variants in *LARS1*. It presents in infancy with recurrent, fever-triggered acute liver failure on a background of poor growth, hypoalbuminemia, and anemia, and it can involve the brain, kidney, muscle, and blood.

- **Key identifiers:** OMIM #615438; Orphanet ORPHA:463328; suggested MONDO:0014220; MeSH — indexed under inborn errors/liver failure (no dedicated descriptor). ICD-10: no specific code (mapped under K72.– acute/subacute hepatic failure and P-codes for perinatal presentations); ICD-11: no dedicated code.
- **Synonyms / alternative names:** ILFS1; Infantile liver failure syndrome type 1; LARS1 deficiency; Leucyl-tRNA synthetase deficiency (cytosolic); LARS-related infantile hepatopathy.
- **Information source type:** Aggregated disease-level resources and published case series/reviews — **not** individual EHR data.

---

## 2. Etiology

**Disease causal factors.** The primary cause is **genetic**: biallelic (homozygous or compound heterozygous) hypomorphic variants in *LARS1*, encoding cytoplasmic leucyl-tRNA synthetase. The disorder is **not** mitochondrial — LARS knockdown in HEK293 cells does not impair mitochondrial function even under stress.

> *"The candidate mutation is located in the LARS gene which encodes a cytoplasmic leucyl-tRNA synthetase enzyme responsible for exclusively attaching leucine to its cognate tRNA during protein translation."* — [PMID: 22607940](https://pubmed.ncbi.nlm.nih.gov/22607940/)

> *"Knock-down of LARS in HEK293 cells did not impact on mitochondrial function even when the cells were put under physiological stress."* — [PMID: 22607940](https://pubmed.ncbi.nlm.nih.gov/22607940/)

**Genetic risk factors.** Consanguinity (homozygous variants in founder populations such as Irish Travellers); carrier parents (obligate heterozygotes). No modifier genes have been established, and there is no significant genotype–phenotype correlation with severity.

**Environmental risk factors / triggers.** **Febrile infections** are the principal precipitant of acute crises (see Section 5 and Finding 12). Catabolic stress (fasting, illness) likely lowers substrate availability and increases translational demand.

**Protective factors.** No genetic protective variants are described. Environmentally, **cognate L-leucine supplementation** and aggressive fever/sick-day management act as risk-modifying/protective interventions (see Section 12).

**Gene–environment interaction.** ILFS1 is a textbook GxE disorder: a temperature-sensitive hypomorphic enzyme becomes rate-limiting during fever (see Finding 12).

---

## 3. Phenotypes

Phenotypes combine **episodic, fever-triggered hepatic and neurologic crises** with a **chronic multisystem** background (growth failure, hypoalbuminemia, anemia). Onset is neonatal-to-infantile; severity is variable (mild-stabilizing to lethal neonatal); progression is episodic with a progressive baseline component.

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Intrauterine growth restriction | Physical/lab | 31/32 (~97%) | HP:0001511 |
| Failure to thrive | Clinical sign | 30/31 (~97%) | HP:0001508 |
| Hypoalbuminemia | Lab abnormality | 32/32 (100%) | HP:0003073 |
| Microcytic anemia | Lab abnormality | 32/33 (~97%) | HP:0001935 |
| Acute liver failure | Clinical sign | 24/34 (~71%) | HP:0006554 |
| Neurodevelopmental delay | Behavioral/dev | 25/30 (~83%) | HP:0012758 |
| Seizures | Clinical sign | 22/29 (~76%) | HP:0001250 |
| Muscular hypotonia | Clinical sign | 13/27 (~48%) | HP:0001252 |
| Recurrent transaminase elevation | Lab abnormality | Prominent | HP:0002910 |
| Encephalopathy / metabolic stroke | Clinical sign | Episodic | HP:0001298 |
| Hepatomegaly / splenomegaly | Physical | Reported | HP:0002240 / HP:0001744 |
| Coagulopathy | Lab abnormality | During crises | HP:0001928 |

> *"The main clinical features of ILFS1 were intrauterine growth restriction (31/32 patients in whom this finding was specifically described), failure to thrive (30/31), hypoalbuminemia (32/32), microcytic anemia (32/33), acute liver failure (24/34), neurodevelopmental delay (25/30), seizures (22/29), and muscular hypotonia (13/27)."* — [PMID: 38844943](https://pubmed.ncbi.nlm.nih.gov/38844943/)

> *"The most prominent clinical findings are recurrent elevation of liver transaminases up to liver failure and encephalopathic episodes, both triggered by febrile illness."* — [PMID: 32699352](https://pubmed.ncbi.nlm.nih.gov/32699352/)

**Quality of life impact.** Recurrent hospitalizations for liver crises, chronic growth failure, developmental delay/seizures, and the constant need for infection vigilance impose a substantial burden on affected children and families. Disease-specific QoL instruments have not been applied; QoL data are qualitative.

---

## 4. Genetic / Molecular Information

**Causal gene.** *LARS1* (HGNC:6512; OMIM *151350; NCBI Gene 51520; UniProt Q9P2J5), chromosome 5q32, reference transcript NM_020117.11.

**Pathogenic variants.** Predominantly **biallelic missense**, homozygous in consanguinity and compound heterozygous otherwise, with strong allelic (mostly private) heterogeneity and **loss-of-function/hypomorphic, temperature-sensitive** consequences. All are germline. There is **no significant genotype–phenotype correlation** with severity.

| Study | Variant(s) | Zygosity | PMID |
|---|---|---|---|
| Casey 2012 (Irish Traveller) | homozygous missense | homozygous | 22607940 |
| Chinese patient | p.L712del + p.D395N | compound het | 28774368 |
| ANE siblings | c.83_88delinsAATGGGATA p.(Arg28_Phe30delinsLysTryAspIle) + c.1283C>T p.(Pro428Leu) | compound het | 38923116 |
| Deep-phenotyping case | c.1818dup + c.463A>G | compound het | 34496286 |
| Lenz/Staufner 2020 | 8 previously unreported variants across 15 families | mixed | 32699352 |

> *"Twenty-five individuals from 15 families were ascertained including 12 novel patients with eight previously unreported variants."* — [PMID: 32699352](https://pubmed.ncbi.nlm.nih.gov/32699352/)

> *"Whole exome sequencing identified the compound heterozygous variants in LARS1 (NM_020117.11) as c.83_88delinsAATGGGATA, p.(Arg28_Phe30delinsLysTryAspIle) and c.1283C>T, p.(Pro428Leu) in both siblings."* — [PMID: 38923116](https://pubmed.ncbi.nlm.nih.gov/38923116/)

**Variant classification (ACMG/AMP):** ranges from pathogenic/likely pathogenic to VUS; functional aminoacylation assays provide supporting (PS3) evidence. **Allele frequencies:** individual variants are ultra-rare/absent in gnomAD (not systematically quantified here). **Modifier genes / epigenetics / chromosomal abnormalities:** none established for ILFS1.

---

## 5. Environmental Information

- **Environmental / lifestyle factors:** Febrile illness and catabolic stress are the operative environmental exposures; there are no toxin, occupational, or lifestyle exposures implicated in disease causation (the cause is genetic).
- **Infectious agents (triggers, not causes):** Documented crisis triggers include **influenza type A** and **human herpesvirus 6 (HHV-6)**, each preceding fatal acute necrotizing encephalopathy in affected siblings.

> *"She presented with generalized seizure and liver dysfunction due to influenza type A infection."* — [PMID: 38923116](https://pubmed.ncbi.nlm.nih.gov/38923116/)

---

## 6. Mechanism / Pathophysiology

**Molecular pathways.** Two arms converge from a single gene defect:

1. **Canonical (translation):** LARS1 charges cytoplasmic tRNA^Leu with leucine (GO:0004823 leucine-tRNA ligase activity; GO:0006429 leucyl-tRNA aminoacylation). Mutant enzyme is **temperature-sensitive** — aminoacylation drops at 38.5–40 °C.
2. **Non-canonical (mTORC1 signaling):** LARS1 is the **intracellular leucine sensor** that binds Rag GTPase in a leucine-dependent manner and acts as a **GAP for RagD**, switching mTORC1 ON (GO:0038202 TORC1 signaling; GO:0032008 positive regulation of TOR signaling).

> *"Aminoacylation activity is significantly decreased in all patient cells studied upon temperature elevation in vitro."* — [PMID: 32699352](https://pubmed.ncbi.nlm.nih.gov/32699352/)

> *"leucyl-tRNA synthetase (LRS) plays a critical role in amino acid-induced mTORC1 activation by sensing intracellular leucine concentration and initiating molecular events leading to mTORC1 activation"* — [PMID: 22424946](https://pubmed.ncbi.nlm.nih.gov/22424946/)

> *"LRS directly binds to Rag GTPase, the mediator of amino acid signaling to mTORC1, in an amino acid-dependent manner and functions as a GTPase-activating protein (GAP) for Rag GTPase to activate mTORC1"* — [PMID: 22424946](https://pubmed.ncbi.nlm.nih.gov/22424946/)

A refined switch model casts LARS as the initiating "ON" switch via GTP hydrolysis of RagD, opposed by Sestrin2 as the "OFF" switch ([PMID: 29784813](https://pubmed.ncbi.nlm.nih.gov/29784813/)).

**Cellular processes.** Loss of mTORC1 activation drives **excessive autophagy** (GO:0010506 regulation of autophagy; GO:0006914 autophagy), demonstrated systemically in zebrafish.

> *"Leucyl-tRNA synthetase deficiency systemically induces excessive autophagy in zebrafish."* — [PMID: 33863987](https://pubmed.ncbi.nlm.nih.gov/33863987/)

**Protein dysfunction:** hypomorphic, thermolabile loss of function (not aggregation). **Metabolic changes:** impaired leucine handling and reduced anabolic mTORC1 signaling; catabolic vulnerability during fever. **Tissue damage:** hepatocyte translational failure → hepatocellular injury, fibrogenesis; neuronal injury (metabolic stroke, ANE). **Biochemical abnormality:** reduced leucyl-tRNA aminoacylation (enzyme deficiency). **Immune involvement:** none primary; infections act as triggers. **Cell types:** hepatocytes (CL:0000182) primarily; neurons; erythroid lineage; skeletal myocytes. **Subcellular compartment:** cytoplasm (GO:0005737); Rag/mTORC1 signaling at the lysosomal surface.

---

## 7. Anatomical Structures Affected

- **Primary organ:** liver (UBERON:0002107) — recurrent transaminase elevation, acute liver failure, hepatomegaly; histology shows cirrhosis and fatty liver; autopsy shows fulminant hepatitis-like injury and fibrogenesis.
- **Secondary/multisystem:** blood (UBERON:0000178; microcytic anemia ~97%), brain (UBERON:0000955; developmental delay, seizures, encephalopathy/metabolic stroke, ANE), skeletal muscle (UBERON:0001134; dysgenesis with disrupted striated fibers), kidney (UBERON:0002113; renal tubulopathy), and — by analogy within the ARS1 cluster — lung (UBERON:0002048).
- **Subcellular:** cytoplasm (GO:0005737); lysosomal mTORC1 platform. **Cells:** hepatocyte (CL:0000182). **Lateralization:** bilateral/systemic.

> *"An autopsy showed fulminant hepatitis-like hepatocellular injury and fibrogenesis in the liver and a lack of uniformity in skeletal muscle, accompanied by the disruption of striated muscle fibers."* — [PMID: 33300650](https://pubmed.ncbi.nlm.nih.gov/33300650/)

> *"Additional symptoms include anaemia, renal tubulopathy, developmental delay, seizures, failure to thrive and deterioration of liver function with minor illness."* — [PMID: 22607940](https://pubmed.ncbi.nlm.nih.gov/22607940/)

Deep HPO phenotyping shows ILFS1 (LARS1) shares ~42% of phenotypic abnormalities with MARS1 disease ([PMID: 34496286](https://pubmed.ncbi.nlm.nih.gov/34496286/)).

---

## 8. Temporal Development

- **Onset:** congenital/neonatal-to-infantile; onset <3 months is common in severe cases. IUGR reflects prenatal onset of the growth phenotype.
- **Onset pattern:** chronic baseline (growth failure, hypoalbuminemia, anemia) punctuated by **acute, fever-triggered crises**.
- **Progression:** episodic/relapsing crises superimposed on a variably progressive course; some patients stabilize with age and management (e.g., a compound-heterozygous child stabilized by age 4 — [PMID: 28774368](https://pubmed.ncbi.nlm.nih.gov/28774368/)), while severe neonatal cases are rapidly lethal.
- **Critical period:** infancy and febrile episodes constitute the window of vulnerability and the key opportunity for intervention.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (OMIM #615438; ORPHA:463328). Penetrance appears complete in biallelic carriers; expressivity is variable. No anticipation, no reported germline mosaicism.
- **Epidemiology:** ultra-rare; no established prevalence/incidence. Cumulative reported patients rose from 3 initial cases to 25 individuals/15 families (2020) to 36 patients (2024), plus additional case reports (~50+ total worldwide). Both sexes affected; no sex bias.
- **Founder effect / consanguinity:** first described in a consanguineous Irish Traveller founder population; consanguinity is a key risk factor. Later reported in Caucasian and non-Caucasian (Chinese) patients.
- **Relative burden:** among indeterminate pediatric acute liver failure, cytosolic aminoacyl-tRNA synthetase deficiencies (including LARS1) accounted for **10%** of genetically solved cases.

> *"the most frequent were mitochondrial diseases (45%), disorders of vesicular trafficking (28%), and cytosolic aminoacyl-tRNA synthetase deficiencies (10%)"* — [PMID: 37976411](https://pubmed.ncbi.nlm.nih.gov/37976411/)

> *"Twenty-five individuals from 15 families were ascertained including 12 novel patients with eight previously unreported variants."* — [PMID: 32699352](https://pubmed.ncbi.nlm.nih.gov/32699352/)

---

## 10. Diagnostics

There is **no specific biomarker**; diagnosis rests on molecular genetic testing, supported by a characteristic biochemical profile.

- **Genetic testing (primary modality):** **WES/WGS** established the diagnosis and is recommended for neonates/infants with unexplained early liver failure when metabolic testing is inconclusive. Gene panels for infantile cholestasis/liver failure that include *LARS1* are appropriate; single-gene testing applies for known familial variants.

> *"Whole-exome sequencing may be useful for neonates with unexplained early liver failure if extensive genetic and metabolic testing is inconclusive."* — [PMID: 33300650](https://pubmed.ncbi.nlm.nih.gov/33300650/)

> *"WES established a genetic diagnosis in 37% of cases (97/260). Diagnostic yield was highest in children with PALF in the first year of life (41%), and in children with recurrent acute liver failure (64%)."* — [PMID: 37976411](https://pubmed.ncbi.nlm.nih.gov/37976411/)

- **Laboratory findings:** episodic elevated transaminases (up to liver failure), hypoalbuminemia, coagulopathy, microcytic anemia, hyperammonemia during crises.
- **Functional confirmatory test:** fibroblast **aminoacylation assay** showing reduced activity that worsens at 38.5–40 °C ([PMID: 34194004](https://pubmed.ncbi.nlm.nih.gov/34194004/)).
- **Imaging:** MRI may show metabolic stroke during encephalopathy; ultrasound may show hepatomegaly/splenomegaly.
- **Differential diagnosis:** NBAS (ILFS2), MPV17/DGUOK and other mtDNA-depletion syndromes, citrin deficiency (SLC25A13), and other cytosolic aaRS deficiencies (IARS, MARS1). The Chinese case explicitly excluded citrin deficiency before diagnosing ILFS1 ([PMID: 28774368](https://pubmed.ncbi.nlm.nih.gov/28774368/)).

---

## 11. Outcome / Prognosis

Prognosis is variable and driven by two factors. In the 36-patient cohort, **12 died or underwent liver transplantation**, and Kaplan-Meier analysis identified:

| Prognostic factor | p-value | Hazard ratio | 95% CI |
|---|---|---|---|
| Age of onset < 3 months | 0.0015 | 12.29 | 3.74–40.3 |
| Presence of liver failure | 0.0343 | 6.57 | 1.96–22.0 |

> *"Kaplan-Meier analysis indicated that age of onset < 3mo (p = 0.0015, hazard ratio = 12.29, 95% confidence interval [CI] = 3.74-40.3), like liver failure (p = 0.0343, hazard ratio = 6.57, 95% CI = 1.96-22.0), conferred poor prognosis."* — [PMID: 38844943](https://pubmed.ncbi.nlm.nih.gov/38844943/)

Severe neonatal disease can be lethal (hepatocellular injury, skeletal muscle dysgenesis; [PMID: 33300650](https://pubmed.ncbi.nlm.nih.gov/33300650/)), and some patients develop fatal **acute necrotizing encephalopathy** ([PMID: 38923116](https://pubmed.ncbi.nlm.nih.gov/38923116/)). Overall ARS1-deficiency mortality (a superset including LARS1) is ~22% ([PMID: 40044141](https://pubmed.ncbi.nlm.nih.gov/40044141/)). Complications include end-stage liver disease, encephalopathy, chronic anemia, and developmental disability. Recovery/stabilization is possible with management ([PMID: 28774368](https://pubmed.ncbi.nlm.nih.gov/28774368/)). Prognostic factors: early onset and liver failure (above); no prognostic biomarker is established.

---

## 12. Treatment

**Mechanism-based pharmacotherapy — cognate L-leucine supplementation** (CHEBI:15603; NCIT: Dietary Supplement Therapy). Supplying excess leucine helps the impaired enzyme meet translational demand and partly restores mTORC1 signaling.

> *"we observed a common disease mechanism of episodic insufficient aminoacylation to meet translational demands and illustrate the power of amino acid supplementation for the expanding ARS patient group"* — [PMID: 34194004](https://pubmed.ncbi.nlm.nih.gov/34194004/)

> *"Supplementation with cognate amino acids was described in 21 patients, with beneficial effects (e.g., improvements in growth, development, liver and lung disease) in the majority. Treatment did not alleviate the most severe phenotypes."* — [PMID: 40044141](https://pubmed.ncbi.nlm.nih.gov/40044141/)

**Supportive care (NCIT: Supportive Care, C15277):** aggressive fever/sick-day management, avoidance of catabolism, correction of hypoalbuminemia and coagulopathy, transfusion for anemia, nutritional support, seizure management.

**Surgical/advanced:** **liver transplantation** (NCIT: Liver Transplantation, C15360) for end-stage or recurrent liver failure (12/36 died or transplanted).

**Experimental / strategy:** All treatment data remain observational (case series, N-of-1); no controlled trials exist. Cognate amino acid supplementation is a shared, theoretically appealing strategy across the ARS deficiency family that requires controlled study. Pharmacogenomics: not applicable. Personalized approach: dosing guided by residual enzyme activity is a rational (untested) direction.

---

## 13. Prevention

- **Primary prevention:** none for disease occurrence (genetic); **genetic counseling** and **carrier/cascade screening** in at-risk families (especially consanguineous kindreds and the Irish Traveller founder population); prenatal and preimplantation genetic testing available for known familial variants.
- **Secondary prevention:** early molecular diagnosis via WES enables anticipatory management; there is no population newborn-screening test.
- **Tertiary prevention (preventing crises/complications):** aggressive antipyresis and sick-day protocols during febrile illness, avoidance of catabolic stress, and cognate L-leucine supplementation to reduce crisis severity. Given fever as the defined critical trigger, prompt medical attention for febrile infections is the central preventive measure.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** human *LARS1* (NCBI Gene 51520) is conserved across vertebrates; zebrafish (*Danio rerio*, NCBI Taxon 7955) ortholog is *larsb*.
- **Natural disease in other species:** no naturally occurring companion-animal or wildlife ILFS1 disease is documented in the reviewed literature; relevance is via engineered/mutant models. A bovine study shows LARS regulates casein synthesis via mTORC1-LAT1 ([PMID: 40045634](https://pubmed.ncbi.nlm.nih.gov/40045634/)), underscoring conservation of the leucine-sensing function.
- **Comparative biology / evolutionary conservation:** the dual aminoacylation + leucine-sensing/mTORC1 mechanism is conserved from fish to mammals, supporting translational relevance.

---

## 15. Model Organisms

- **Zebrafish (*larsb*):** two independent *larsb* mutant lines recapitulate ILFS1-like features (liver dysfunction/hepatopathy), and *larsb* deficiency systemically induces excessive autophagy linked to mTORC1 downregulation — directly modeling the human mechanism.

> *"we obtained zebrafish larsb"* — [PMID: 30262142](https://pubmed.ncbi.nlm.nih.gov/30262142/)

> *"Leucyl-tRNA synthetase deficiency systemically induces excessive autophagy in zebrafish."* — [PMID: 33863987](https://pubmed.ncbi.nlm.nih.gov/33863987/)

- **In vitro / cellular:** patient-derived fibroblasts (aminoacylation and thermostability assays; [PMIDs 32699352, 34194004]) and HEK293 LARS-knockdown cells (which excluded a primary mitochondrial defect; [PMID: 22607940]).
- **Model characteristics:** zebrafish recapitulate hepatopathy and the autophagy/mTORC1 mechanism; limitations include incomplete capture of human hepatic failure, neurodevelopmental, and febrile-trigger dynamics. **No mammalian (mouse) model** is documented in the reviewed literature. Resources: ZFIN (zebrafish); patient fibroblast lines from published cohorts.

---

## Mechanistic Model / Interpretation

```
                     Biallelic hypomorphic LARS1 variants
                                    │
              ┌─────────────────────┴─────────────────────┐
              ▼                                            ▼
   ARM 1: CANONICAL FUNCTION                   ARM 2: MOONLIGHTING FUNCTION
   Leu-tRNA aminoacylation                     Intracellular leucine sensor
              │                                            │
   Temperature-sensitive:                       Fails to bind Rag GTPase /
   activity ↓ at 38.5–40°C                      loss of GAP activity for RagD
              │                                            │
   FEVER (influenza A, HHV-6) ─────────►  Insufficient charged tRNA^Leu    mTORC1 activity ↓
              │                            to meet ↑ translational demand           │
              │                                            │              Excessive autophagy
              ▼                                            ▼                         ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │      Hepatocyte translational failure + catabolic stress + autophagy       │
        └──────────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────┬───────────┴───────────┬───────────────┐
        ▼               ▼                        ▼               ▼
  Acute liver      Encephalopathy /        Hypoalbuminemia   Growth failure
  failure          metabolic stroke / ANE  coagulopathy      (IUGR, FTT), anemia
```

**Upstream vs downstream.** The upstream trigger is febrile infection raising core temperature above the mutant enzyme's stability threshold, in an organ (liver) with high secretory translational load. Downstream, two parallel consequences unfold: (1) failed aminoacylation impairs synthesis of essential proteins (albumin, clotting factors) → hypoalbuminemia, coagulopathy, hepatocellular injury; and (2) failed leucine sensing collapses mTORC1 → excessive autophagy amplifying cell stress. The chronic non-febrile phenotype (IUGR, failure to thrive, anemia, developmental delay) reflects the constant baseline deficit. **Why leucine helps:** excess substrate partially restores both charged-tRNA production and the mTORC1 leucine signal — consistent with benefit in milder cases and failure in the most severe (residual activity too low). ILFS1 sits within the cytosolic ARS1 family sharing "episodic insufficient aminoacylation to meet translational demands," corroborated by ~42% HPO overlap with MARS1 disease.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [22607940](https://pubmed.ncbi.nlm.nih.gov/22607940/) | LARS as novel cause of infantile hepatopathy | Human + in vitro | Causal gene; excludes mitochondrial mechanism; multi-organ features |
| [32699352](https://pubmed.ncbi.nlm.nih.gov/32699352/) | Genotypic/phenotypic spectrum of ILFS1 | Human (25 pts) + functional | Fever trigger; temperature-sensitive aminoacylation; allelic heterogeneity |
| [38844943](https://pubmed.ncbi.nlm.nih.gov/38844943/) | Early onset & liver failure → poor prognosis | Human (36 pts) | Phenotype frequencies; Kaplan-Meier prognosis |
| [33863987](https://pubmed.ncbi.nlm.nih.gov/33863987/) | LARS deficiency induces excessive autophagy | Zebrafish | Links LARS loss to mTORC1/autophagy |
| [30262142](https://pubmed.ncbi.nlm.nih.gov/30262142/) | Loss of LARSb → ILFS1-like symptoms | Zebrafish | Disease-recapitulating model |
| [38923116](https://pubmed.ncbi.nlm.nih.gov/38923116/) | Two siblings with ANE and LARS1 variants | Human (case) | Infectious triggers; severe ANE; compound-het variants |
| [33300650](https://pubmed.ncbi.nlm.nih.gov/33300650/) | Severe neonatal course | Human + autopsy | Severe spectrum; WES recommendation; muscle pathology |
| [34194004](https://pubmed.ncbi.nlm.nih.gov/34194004/) | Treatment of ARS deficiencies with amino acids | In vitro + clinical | Common mechanism; leucine therapy; temperature assay |
| [40044141](https://pubmed.ncbi.nlm.nih.gov/40044141/) | ARS1-deficiencies phenotype & treatment review | Review (438 pts) | Cognate amino acid benefit/limits; 22% mortality |
| [22424946](https://pubmed.ncbi.nlm.nih.gov/22424946/) | LARS is intracellular leucine sensor for mTORC1 | Molecular | Leucine-sensing/Rag-GAP mechanism |
| [29784813](https://pubmed.ncbi.nlm.nih.gov/29784813/) | Coordination of Rag GTPase cycle by LARS | Molecular | LARS "ON" vs Sestrin2 "OFF" switch |
| [28774368](https://pubmed.ncbi.nlm.nih.gov/28774368/) | First non-Caucasian ILFS1 child | Human (case) | Compound-het variants; differential dx; stabilization |
| [37976411](https://pubmed.ncbi.nlm.nih.gov/37976411/) | Genetic landscape of pediatric ALF | Human cohort (260) | WES yield; cytosolic aaRS = 10% of solved cases |
| [34496286](https://pubmed.ncbi.nlm.nih.gov/34496286/) | Deep phenotyping MARS1 vs LARS1 | Human + review | ~42% HPO overlap; shared multisystem features |

**Consistency and challenges.** Human cohorts, in vitro assays, and zebrafish models converge on the dual aminoacylation/mTORC1 mechanism. The main tension is therapeutic — cognate amino acid supplementation benefits milder cases but fails in the most severe, and all treatment evidence is observational. The absence of genotype–phenotype correlation means variant identity alone does not predict severity.

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease, small numbers** (<~60 patients worldwide; max cohort 36) limit statistical power for genotype–phenotype and treatment analyses; no formal prevalence/incidence.
2. **No controlled treatment trials** — all L-leucine/cognate amino acid data are observational or N-of-1; optimal dosing/timing and long-term efficacy undefined; no rescue of severe phenotypes.
3. **Absent genotype–phenotype correlation** — determinants of lethal neonatal vs stabilizing courses unknown; modifiers/epigenetics unexplored.
4. **Mechanism partly inferred from models** — the mTORC1/autophagy arm is best demonstrated in zebrafish/cell lines; direct human hepatocyte evidence and quantitative apportioning of the two arms are lacking.
5. **No mammalian (mouse) model** documented in the reviewed literature.
6. **Biomarker gap** — no specific circulating biomarker for diagnosis, crisis prediction, or monitoring; the fibroblast temperature assay is not widely available.
7. **Population genetics** (carrier frequency, gnomAD variant frequencies, founder haplotype) not quantitatively established here.
8. **Citation caveat** — the autophagy paper (PMID 33863987) snippet was flagged as an approximate match; the mechanistic claim is supported but exact wording should be verified against the source.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective international registry** to capture natural history and enable powered genotype–phenotype and treatment-outcome analyses.
2. **Controlled/adaptive L-leucine trial** with predefined endpoints (growth, crisis frequency, transaminase/albumin trajectories, neurodevelopment), stratified by residual enzyme activity.
3. **Conditional hepatocyte-specific *Lars1* mouse model** to test temperature-sensitivity and mTORC1/autophagy mechanisms in mammalian liver and as a preclinical platform.
4. **Patient iPSC-derived hepatocyte organoids** to quantify aminoacylation vs mTORC1 activity (p-S6K, p-4E-BP1, LC3-II flux) under normothermic vs febrile (40 °C) conditions ± leucine.
5. **Validated functional assay** (standardized temperature-dependent aminoacylation or mTORC1 reporter) for ACMG classification of VUS.
6. **Population-genetics analysis** of gnomAD/founder haplotypes to estimate carrier frequency (notably Irish Travellers) and inform screening.
7. **Test mTORC1-restoring/autophagy-modulating agents** in zebrafish *larsb* mutants as complementary therapies.
8. **Prospective sick-day protocol** (aggressive antipyresis, anabolic support, early leucine loading during fever) evaluated for reduction of crisis severity.

---

## Consensus Answer

Infantile Liver Failure Syndrome type 1 (ILFS1; OMIM #615438) is a rare autosomal-recessive multisystem disorder caused by biallelic hypomorphic (mostly missense) variants in *LARS1*, the cytosolic leucyl-tRNA synthetase, presenting in infancy with fever-triggered recurrent acute liver failure plus intrauterine growth restriction, failure to thrive, hypoalbuminemia, microcytic anemia, neurodevelopmental delay, seizures, and hypotonia. Its pathophysiology is dual — temperature-sensitive loss of leucine-tRNA aminoacylation (impaired translation during fever) combined with loss of the LARS1 leucine-sensing/Rag-GTPase-GAP function that activates mTORC1, causing excessive autophagy — so that early onset (<3 months) and liver failure predict poor prognosis. Management is supportive with mechanism-based cognate L-leucine supplementation and liver transplantation for end-stage disease; zebrafish *larsb* mutants are the principal disease model.


## Artifacts

- [OpenScientist final report](Infantile_Liver_Failure_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Infantile_Liver_Failure_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.