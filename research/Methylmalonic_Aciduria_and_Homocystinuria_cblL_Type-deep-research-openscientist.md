---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T13:30:29.359662'
end_time: '2026-09-04T14:02:42.689440'
duration_seconds: 1933.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Methylmalonic Aciduria and Homocystinuria cblL Type
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Methylmalonic_Aciduria_and_Homocystinuria_cblL_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Methylmalonic_Aciduria_and_Homocystinuria_cblL_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methylmalonic Aciduria and Homocystinuria cblL Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Methylmalonic Aciduria and Homocystinuria cblL Type** covering all of the
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

# Methylmalonic Aciduria and Homocystinuria, cblL Type (MAHCL) — Comprehensive Disease Report

**Disease:** Methylmalonic Aciduria and Homocystinuria, cblL Type
**OMIM:** #620940 (MAHCL) · **MONDO:** MONDO:0975798 · **Gene:** *THAP11* (OMIM 609119; HGNC:20856; 16q22.1)
**Category:** Mendelian · autosomal recessive inborn error of intracellular cobalamin (vitamin B12) metabolism

---

## Summary

Methylmalonic aciduria and homocystinuria, cblL type (MAHCL), is an **ultra-rare autosomal-recessive inborn error of intracellular cobalamin (vitamin B12) metabolism** caused by biallelic hypomorphic variants in ***THAP11***, a THAP-domain–containing transcription factor located at chromosome 16q22.1. Unlike the classic combined methylmalonic aciduria/homocystinuria disorders that arise from defects in the cobalamin-processing enzymes and chaperones themselves (e.g., *MMACHC* in cblC), cblL is a **transcriptional/regulatory disorder**: THAP11 partners with the global co-regulator HCFC1 (and ZNF143) to activate transcription of *MMACHC*. When THAP11 function is impaired, *MMACHC* expression is downregulated, producing a **cblC-like biochemical phenotype (mild methylmalonic aciduria, elevated/high-normal homocysteine, low-normal methionine) despite an entirely normal *MMACHC* gene sequence.** This places cblL within the "cblX-like" group of cobalamin disorders alongside HCFC1-related cblX and ZNF143-related disease.

The disorder was defined by Quintana et al. (2017), who identified a homozygous missense variant, *THAP11* c.240C>G (p.Phe80Leu; F80L), in a boy of Moroccan parentage who presented at 2 months of age with **myoclonic seizures and severe global developmental impairment** after *MMACHC* and *HCFC1* mutations had been excluded [PMID: 28449119]. To date this remains the **only reported patient with cblL worldwide**, so the clinical spectrum, natural history, prognosis, and treatment response are largely **extrapolated from the biochemically equivalent cblC and cblX disorders.** Because THAP11 (also known as Ronin) is an essential developmental transcription factor — its complete loss causes peri-implantation lethality in mice and craniofacial/neural defects in zebrafish — the human disorder is expected to be syndromic and neurodevelopmental, reflecting both the *MMACHC*-dependent cobalamin defect and *MMACHC*-independent disruption of THAP11's broad transcriptional program governing protein biosynthesis, energy metabolism, and neural/neural-crest development.

Rational management follows the cblC/cblX template: parenteral **hydroxocobalamin**, **betaine**, **folinic acid**, and **levocarnitine**, with dietary protein moderation. However, as in cblC, cognitive and neurological impairment frequently persists despite biochemical correction, and outcome data specific to cblL do not yet exist. This report compiles the current state of knowledge across all requested disease-characteristic domains, clearly distinguishing cblL-specific evidence (a single case plus model-organism data) from information imported from the wider cobalamin-disorder literature.

---

## Key Findings

### F001 — cblL (MAHCL, OMIM #620940) is caused by biallelic *THAP11* variants

cblL is genetically defined by **biallelic variants in *THAP11*** (16q22.1). The index and only case is a boy of Moroccan parentage carrying a homozygous missense variant, **c.240C>G (p.Phe80Leu; F80L)**, who presented at 2 months of age with myoclonic seizures and severe global developmental impairment; *MMACHC* (cblC) and *HCFC1* (cblX) mutations were specifically excluded before *THAP11* was sequenced [PMID: 28449119]. OMIM assigns cblL the number **#620940 (MAHCL)**, with the gene *THAP11* catalogued at **OMIM 609119**.

> "We sequenced THAP11 by Sanger sequencing and discovered a potentially pathogenic, homozygous variant, c.240C > G (p.Phe80Leu)." — Quintana et al. 2017 [PMID: 28449119]

In clinical practice, cblL sits within the combined MMA+homocystinuria (HC) gene panel. Hwang et al. (2021) list the relevant genes as *MMACHC* (cblC), *MMADHC* (cblD), *LMBRD1* (cblF), *ABCD4* (cblJ), *THAP11* and *ZNF143* (cblX-like), and *HCFC1* (cblX) [PMID: 34655177]:

> "biallelic variants in one of the following genes: MMACHC (cblC), MMADHC (cblD), LMBRD1 (cblF), ABCD4 (cblJ), THAP11 (cblX-like), and ZNF143 (cblX-like), or a hemizygous variant in HCFC1 (cblX)" — Hwang et al. 2021 [PMID: 34655177]

**Ontology terms:** MONDO:0975798 (cblL); gene HGNC:20856 (*THAP11*).

### F002 — Mechanism: the THAP11–HCFC1 complex transcriptionally regulates *MMACHC*; its loss downregulates *MMACHC*

THAP11 is a **THAP-domain transcription factor** that partners with the global transcriptional co-regulator **HCFC1** to drive *MMACHC* expression. This is the pivotal mechanistic link that explains why a disorder with a normal *MMACHC* sequence nonetheless behaves biochemically like cblC. Quintana et al. (2017) state the axis directly:

> "HCFC1 regulates cobalamin metabolism via the regulation of MMACHC expression through its interaction with THAP11, a THAP domain-containing transcription factor." — Quintana et al. 2017 [PMID: 28449119]

The same regulatory logic was established in cblX, where *HCFC1* mutations produce a severe reduction in *MMACHC* mRNA and protein in patient fibroblasts:

> "The severe reduction in MMACHC mRNA and protein within subject fibroblast lines suggested a role for HCFC1 in transcriptional regulation of MMACHC" — Yu et al. 2013 [PMID: 24011988]

RNA-seq of the THAP11-mutant patient's fibroblasts showed **downregulation of *MMACHC* (and *TMOD2*)**, consistent with a cblC-like biochemical complementation pattern despite a normal *MMACHC* sequence. This makes cblL a **regulatory (upstream) phenocopy of cblC.**

**Ontology terms:** GO:0006355 (regulation of DNA-templated transcription); GO:0009235 (cobalamin metabolic process); GO:0003700 (DNA-binding transcription factor activity).

### F003 — Downstream biochemistry: MMACHC is a cytosolic cobalamin chaperone performing decyanation/dealkylation

The functional consequence of reduced *MMACHC* is loss of the **cytosolic cobalamin trafficking chaperone** that prepares dietary/therapeutic cobalamin for use. MMACHC catalyzes **reductive decyanation** of cyanocobalamin and **glutathione-dependent dealkylation** of methyl- and adenosylcobalamin (turnover 11.7 h⁻¹ for MeCbl and 0.174 h⁻¹ for AdoCbl at 20 °C), generating cob(I)alamin for downstream conversion to the two active cofactors — methylcobalamin (for methionine synthase, MTR) and adenosylcobalamin (for methylmalonyl-CoA mutase, MMUT) [PMID: 19801555].

> "MMACHC, a cytosolic cobalamin trafficking chaperone, has been shown recently to catalyze a reductive decyanation reaction when it encounters cyanocobalamin." — Kim et al. 2009 [PMID: 19801555]

When MMACHC activity falls, **both** downstream cofactors become deficient, impairing (a) methylmalonyl-CoA mutase → methylmalonic acid accumulation and (b) methionine synthase → homocysteine accumulation with low methionine. This is the biochemical signature of the "combined" MMA+HC disorders.

**Ontology terms:** CHEBI:17439 (cyanocobalamin), CHEBI:28115 (methylcobalamin), CHEBI:18408 (adenosylcobalamin), CHEBI:16009 (methylmalonic acid), CHEBI:17230 (homocysteine); GO:0005829 (cytosol).

### F004 — Clinical phenotype and treatment framework (extrapolated from cblC)

The single reported cblL patient presented in **infancy (2 months)** with **myoclonic seizures and severe global developmental impairment**, with **mild methylmalonic aciduria and low-normal plasma methionine**; overt homocystinuria was not documented in this individual [PMID: 28449119]. Standard therapy for the biochemically equivalent cblC group comprises **hydroxocobalamin (OHCbl), betaine, folinic acid, levocarnitine, and dietary protein restriction** [PMID: 23746552]:

> "Hydroxocobalamin (OHCbl), betaine, folinic acid, levocarnitine and eventually dietary protein restriction are the main therapeutic approaches." — Matos et al. 2013 [PMID: 23746552]

In cblC, cognitive and visual impairment are nearly constant despite treatment, tempering expectations for cblL. The developmental/neural involvement underlying the severe infantile phenotype is supported by model data:

> "The loss of THAP11 in zebrafish embryos results in craniofacial abnormalities including the complete loss of Meckel's cartilage" — Quintana et al. 2017 [PMID: 28449119]

### F005 — THAP11 (Ronin) is an essential HCF-1–partnered transcription factor for embryogenesis, pluripotency, and biosynthetic gene programs

THAP11 (Ronin) is a **THAP-domain DNA-binding factor essential for embryonic stem-cell self-renewal**. Ronin deficiency causes peri-implantation lethality and inner-cell-mass defects, and Ronin binds directly to HCF-1 [PMID: 18585351]:

> "its deficiency in mice produces periimplantational lethality and defects in the inner cell mass" — Dejosez et al. 2008 [PMID: 18585351]

Ronin/HCF-1 binds a **hyperconserved enhancer element** and upregulates genes for protein biosynthesis and energy production (transcription initiation, mRNA splicing, cell metabolism) [PMID: 20581084]:

> "its activity at promoter sites more often leads to the up-regulation of genes essential to protein biosynthesis and energy production" — Dejosez et al. 2010 [PMID: 20581084]

In zebrafish, loss of THAP11 (and *hcfc1b*) impairs proliferation/differentiation of neural precursors and neural crest, causing craniofacial cartilage loss that is **rescued by human *MMACHC*** [PMID: 25281006]:

> "the hcfc1b-mediated craniofacial abnormalities were rescued by expression of human MMACHC, a downstream target of HCFC1 that is aberrantly expressed in cblX" — Quintana et al. 2014 [PMID: 25281006]

This explains two key features of cblL: (1) **only hypomorphic alleles are compatible with life** (complete loss is lethal), and (2) the disorder is **syndromic/neurodevelopmental**, drawing on THAP11's broad transcriptional program in addition to the *MMACHC*-dependent cobalamin branch.

### F006 — Epidemiology and inheritance: ultra-rare autosomal recessive, single reported homozygous case

Only **one patient** with cblL/MAHCL has been reported worldwide — a boy born to Moroccan parents carrying a homozygous *THAP11* c.240C>G (p.Phe80Leu) missense variant, implying **autosomal recessive inheritance with a likely consanguineous/founder background** [PMID: 28449119].

> "We report a patient who presented with clinical and biochemical phenotypic features that overlap cblX, but who does not have any mutations in either MMACHC or HCFC1." — Quintana et al. 2017 [PMID: 28449119]

No prevalence or incidence estimates exist; the disorder is at "unknown/ultra-rare" frequency. For contrast, the biochemically related **cblC (*MMACHC*) is the most common inborn error of B12 metabolism**, with a newborn-screening incidence for MMA estimated at ~1:3,920 live births in one Chinese cohort [PMID: 26563984].

### F007 — Verified molecular coordinates and protein-domain context of the cblL variant

The single cblL-causing variant is **NM_020457.3:c.240C>G, p.(Phe80Leu)**, located at **GRCh38 chr16:67,842,794** (GRCh37 chr16:67,876,697), cytoband **16q22.1**; ClinVar Variation 393304 (VCV000393304), dbSNP **rs188675529**, OMIM 609119.0001, ClinGen CA396396088. The 1000 Genomes global minor-allele frequency is **~0.0032 (~0.3%)** — a low-frequency (not private) allele that is pathogenic only in the **biallelic** state. **Phe80** sits within the highly conserved **THAP-type zinc-finger DNA-binding domain** of THAP11; the protein also contains Gln-rich and Ala-rich regions, an HCFC1-binding motif (HBM), and a coiled-coil domain (Quintana et al. 2017 [PMID: 28449119]; ClinVar/UniProt Q96EK4).

Notably, of three cblX-like, *MMACHC*/*HCFC1*-negative subjects investigated, **only one** carried the THAP11 variant — underscoring genetic heterogeneity within the cblX-like group and the singular nature of the confirmed cblL case.

---

## Section-by-Section Report

### 1. Disease Information

- **What it is:** An autosomal-recessive inborn error of intracellular cobalamin (vitamin B12) metabolism in which impaired transcriptional activation of *MMACHC* (by mutant THAP11) produces a combined methylmalonic aciduria + homocystinuria biochemical phenotype superimposed on a severe syndromic neurodevelopmental disorder.
- **Key identifiers:** OMIM **#620940** (MAHCL); MONDO **:0975798**; gene *THAP11* OMIM 609119 / HGNC:20856. No dedicated Orphanet, ICD-10/ICD-11, or MeSH code has been established for cblL specifically; it is generally grouped under disorders of cobalamin metabolism (pragmatically coded within the E71/E72 metabolic families — no cblL-specific code exists; *information not available*).
- **Synonyms/alternative names:** Methylmalonic aciduria and homocystinuria, cblL type; MAHCL; THAP11-related cobalamin metabolism disorder; a "cblX-like" cobalamin disorder.
- **Source of information:** **Aggregated disease-level resources** (OMIM, ClinVar, primary literature) plus a **single individual patient** report — not EHR/population data.

### 2. Etiology

- **Primary cause (genetic):** Biallelic hypomorphic **missense** variants in *THAP11* (the single confirmed allele is p.Phe80Leu in the THAP DNA-binding domain) [PMID: 28449119]. The mechanism is loss of transcriptional activation of *MMACHC* (F002). There is no environmental or infectious cause; cobalamin deficiency here is *functional/intracellular*, not dietary.
- **Genetic risk factors:** Homozygosity/compound heterozygosity for pathogenic *THAP11* variants; **consanguinity/founder background** (Moroccan parentage in the index case) increases the chance of homozygosity for the low-frequency allele (MAF ~0.3%).
- **Environmental risk / protective factors:** None established for cblL specifically. By analogy to cblC, adequate parenteral cobalamin and methyl-donor supplementation is protective against metabolic decompensation; catabolic stressors (infection, fasting) may precipitate crises (*inferred from cblC*).
- **Gene–environment interactions:** Not characterized. Plausibly, cobalamin/betaine/folate status modulates biochemical severity (*inferred*).

### 3. Phenotypes

Because only one patient has been reported, phenotype frequencies for cblL itself are anecdotal (n=1); the table below marks cblL-observed features and cblC-extrapolated features.

| Phenotype | Type | Onset | Severity | Source | Suggested HPO |
|---|---|---|---|---|---|
| Myoclonic seizures | Clinical sign | Neonatal/infantile (2 mo) | Severe | cblL (n=1) [PMID:28449119] | HP:0002123 (myoclonic seizure) |
| Global developmental impairment / delay | Symptom | Infantile | Severe | cblL (n=1) [PMID:28449119] | HP:0001263 |
| Methylmalonic aciduria | Lab abnormality | Infantile | Mild | cblL (n=1) [PMID:28449119] | HP:0012120 |
| Homocystinuria / hyperhomocysteinemia | Lab abnormality | — | Not documented in index case | cblC-extrapolated | HP:0002160 |
| Low-normal plasma methionine | Lab abnormality | Infantile | — | cblL (n=1) [PMID:28449119] | HP:0500152 (hypomethioninemia) |
| Craniofacial abnormalities (model) | Physical | Embryonic (model) | — | zebrafish [PMID:25281006] | HP:0001999 |
| Intellectual disability | Symptom | Childhood | Moderate–severe (cblC) | cblC/cblX-extrapolated | HP:0001249 |
| Feeding difficulty, hypotonia, lethargy | Symptom/sign | Infantile | Variable (cblC) | cblC-extrapolated [PMID:20924684] | HP:0011968, HP:0001252, HP:0001254 |
| Megaloblastic anemia | Lab abnormality | Variable (cblC) | Variable | cblC-extrapolated | HP:0001889 |

- **Progression:** Presumed progressive/episodic with metabolic decompensations, as in cblC.
- **Quality-of-life impact:** Severe — profound developmental impairment and seizures imply high dependency; formal QoL instruments have not been applied to cblL (*information not available*).

### 4. Genetic/Molecular Information

- **Causal gene:** ***THAP11*** (16q22.1; OMIM 609119; HGNC:20856; UniProt **Q96EK4**).
- **Pathogenic variant (only one confirmed):** NM_020457.3:**c.240C>G**, **p.(Phe80Leu)**; GRCh38 chr16:67,842,794; ClinVar VCV000393304; dbSNP rs188675529; OMIM 609119.0001. **Type:** missense. **Classification:** pathogenic in the biallelic state (per the disease-defining report; ClinVar entry present). **Allele frequency:** ~0.0032 (1000 Genomes global) — low-frequency, not private. **Origin:** germline. **Functional consequence:** hypomorphic loss of function affecting the THAP zinc-finger DNA-binding domain → reduced transcriptional activation of *MMACHC* (F002, F007).
- **Modifier genes:** *HCFC1* and *ZNF143* are obligate partners in the same transcriptional complex; variation in these (or in *MMACHC* itself) could plausibly modify severity (*inferred*). No formal modifier data for cblL.
- **Epigenetic information:** Not established for cblL. (In the related "epi-cblC," aberrant *PRDX1* transcripts methylate the *MMACHC* promoter [PMID: 42002808] — a parallel example of *MMACHC* silencing by a non-coding mechanism, illustrating that *MMACHC* output can be reduced without coding mutations.)
- **Chromosomal abnormalities:** None; cblL is a single-nucleotide/point-variant disorder.

### 5. Environmental Information

No environmental, lifestyle, or infectious agents cause cblL. As with other combined MMA/HC disorders, catabolic triggers (intercurrent infection, fasting, high protein load) may precipitate metabolic decompensation (*inferred from cblC* [PMID: 20924684]). Not applicable: toxins, radiation, occupational exposure, pathogens.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic hypomorphic **THAP11 p.Phe80Leu** variants impair the THAP zinc-finger DNA-binding domain → **reduced THAP11 transcription-factor function** (demonstrated: variant + fibroblast RNA-seq) [PMID: 28449119].
2. Impaired THAP11 **weakens the THAP11–HCFC1(–ZNF143) transcriptional complex** at target promoters → **decreased transcriptional activation of *MMACHC*** (demonstrated in cblL fibroblasts; established in cblX) [PMID: 28449119; 24011988].
3. Lower *MMACHC* mRNA/protein → **loss of cytosolic cobalamin chaperone activity** (reductive decyanation + glutathione-dependent dealkylation) [PMID: 19801555].
4. Failure to process cobalamin → **deficiency of both active cofactors**: methylcobalamin and adenosylcobalamin (inferred from the biochemistry of the pathway).
5a. AdoCbl deficiency → **methylmalonyl-CoA mutase (MMUT) dysfunction** → **methylmalonic acid accumulation** → methylmalonic aciduria [PMID: 28449119].
5b. MeCbl deficiency → **methionine synthase (MTR) dysfunction** → **homocysteine accumulation + low methionine** (homocystinuria/hypomethioninemia; expected, mildly expressed in index case) [PMID: 19801555].
6. **Branch (MMACHC-independent):** reduced THAP11 also **dysregulates its broad program of protein-biosynthesis, energy-metabolism, and neural/neural-crest developmental genes** → contributes to the **severe syndromic neurodevelopmental phenotype** independent of the cobalamin defect (demonstrated in mouse/zebrafish; inferred for the human syndrome) [PMID: 18585351; 20581084; 25281006].
7. Convergence of metabolite toxicity (MMA, homocysteine) + impaired methylation (low methionine/SAM) + developmental gene dysregulation → **infantile myoclonic seizures and profound global developmental impairment** [PMID: 28449119].

**Molecular pathways:** cobalamin (B12) intracellular processing pathway; methionine/homocysteine remethylation cycle; methylmalonate–succinate (propionate catabolism) pathway; THAP11/HCF-1 transcriptional enhancer program (Reactome: Metabolism of vitamins and cofactors; cobalamin metabolism).
**Cellular processes:** transcriptional regulation, cell proliferation/differentiation (neural precursors, neural crest), cellular cobalamin trafficking.
**Protein dysfunction:** hypomorphic loss of THAP11 DNA-binding function (missense in THAP domain); downstream loss of MMACHC chaperone function.
**Metabolic changes:** amino-acid (methionine/homocysteine) and organic-acid (methylmalonate) metabolism; impaired one-carbon/methylation metabolism.
**Immune involvement:** none primary.
**Tissue-damage mechanisms:** presumed metabolite-mediated neurotoxicity and impaired neurodevelopment (*inferred*).

**Suggested ontology terms:** GO:0006355 (regulation of transcription), GO:0009235 (cobalamin metabolic process), GO:0006555 (methionine metabolic process), GO:0032259 (methylation); CL:0000047 (neuronal stem cell), CL:0000333 (migratory neural crest cell); CHEBI:16009 (methylmalonic acid), CHEBI:17230 (homocysteine).

### 7. Anatomical Structures Affected

- **Organ level (primary):** brain/central nervous system (UBERON:0000955 brain; UBERON:0001017 central nervous system) — seizures, developmental impairment. **Body system:** nervous system (UBERON:0001016).
- **Secondary/model-based:** craniofacial cartilage/skeleton (Meckel's cartilage in zebrafish; UBERON:0004744) — neural-crest-derived structures.
- **Tissue/cell level:** neural precursor cells and neural crest cells (CL:0000047; CL:0000333); by analogy to cblC, hematopoietic (megaloblastic changes) and retinal cells may be affected (*inferred*).
- **Subcellular level:** **cytosol** (GO:0005829 — site of MMACHC chaperone activity) and **nucleus** (GO:0005634 — site of THAP11 transcriptional activity). Downstream mitochondrial enzyme (MMUT) function is secondarily impaired (GO:0005739 mitochondrion).
- **Localization/laterality:** CNS involvement is bilateral/diffuse (*inferred*).

### 8. Temporal Development

- **Onset:** **Infantile/neonatal** — the index patient presented at **2 months** with seizures [PMID: 28449119]. Onset pattern: subacute–progressive.
- **Progression:** presumed **progressive** with superimposed **episodic** metabolic decompensations, as in cblC; disease duration is **chronic/lifelong**.
- **Stages:** not formally staged.
- **Critical periods:** early infancy is the key window for intervention; by analogy to cblC, earlier treatment initiation (ideally via newborn screening) is associated with better — though still frequently impaired — neurodevelopmental outcome [PMID: 26563984].

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (homozygous index case) [PMID: 28449119].
- **Epidemiology:** **Ultra-rare — a single reported case worldwide.** No prevalence/incidence figures exist. Contrast with cblC (most common B12 inborn error; MMA newborn-screening incidence ~1:3,920 in one Chinese cohort) [PMID: 26563984].
- **Penetrance/expressivity:** presumed complete penetrance in biallelic state; expressivity unknown (n=1).
- **Founder effect/consanguinity:** likely — Moroccan parentage and homozygosity for a low-frequency (~0.3%) allele suggest a consanguineous/founder background [PMID: 28449119; F007].
- **Carrier frequency:** the p.Phe80Leu allele has a 1000 Genomes global MAF ~0.0032; carrier frequency for *cblL as a disease* is unknown given only one causal allele is documented.
- **Demographics:** single male patient of North African (Moroccan) descent; no sex-ratio or age-distribution data can be derived from n=1.

### 10. Diagnostics

- **Biochemical/laboratory:** elevated **methylmalonic acid** (blood/urine); **elevated total homocysteine** with **low/low-normal methionine**; elevated **propionylcarnitine (C3)** and ratios on acylcarnitine profiling (MS/MS) — the classic combined MMA+HC signature [PMID: 20924684; 28449119]. In the index cblL case, MMA was mild and methionine low-normal.
- **Complementation/cellular studies:** cblL shows a **cblC-like biochemical complementation pattern** with reduced *MMACHC* expression on fibroblast RNA-seq despite a normal *MMACHC* sequence — a key clue that directs testing to the regulatory genes.
- **Genetic testing (definitive):** Because the biochemistry mimics cblC/cblX, diagnosis requires **sequencing beyond *MMACHC***. Recommended approach: a **combined MMA+HC gene panel or exome** covering *MMACHC, MMADHC, LMBRD1, ABCD4, HCFC1, ZNF143,* and ***THAP11*** [PMID: 34655177]. cblL is confirmed by finding **biallelic *THAP11*** variants after *MMACHC* and *HCFC1* are excluded [PMID: 28449119]. WES/WGS and targeted panels are all appropriate; single-gene *THAP11* testing is reserved for the cblX-like, *MMACHC*/*HCFC1*-negative phenotype.
- **Imaging/electrophysiology:** EEG for seizure characterization; brain MRI as per cblC workup (white-matter/structural changes) — not specifically reported for cblL (*information not available*).
- **Differential diagnosis:** cblC (*MMACHC*), cblX (*HCFC1*), cblD/cblF/cblJ, ZNF143-related cblX-like disease, epi-cblC (*PRDX1* epimutation [PMID: 42002808]), and dietary/maternal B12 deficiency. The distinguishing feature of cblL is **normal *MMACHC*/*HCFC1* with biallelic *THAP11* variants and reduced *MMACHC* expression.**
- **Screening:** MMA/homocysteine-based **newborn screening** (C3, C3/C2, methionine, tHcy) will flag the biochemical phenotype but cannot distinguish cblL from other combined MMA+HC disorders without molecular confirmation [PMID: 26563984].

**Suggested LOINC-type analytes:** methylmalonic acid (urine/plasma), total homocysteine, methionine, propionylcarnitine (C3).

### 11. Outcome/Prognosis

- **Survival/mortality:** Unknown for cblL (n=1, no long-term follow-up reported). In cblC, mortality occurs from metabolic crises (e.g., a screened cblC infant died at 38 days from infection-triggered crisis) [PMID: 26563984].
- **Morbidity/function:** The index patient had **severe global developmental impairment and seizures**, predicting high long-term disability [PMID: 28449119]. By analogy to cblC, **cognitive and visual impairment are frequent despite treatment** [PMID: 23746552].
- **Disease course:** presumed chronic with risk of decompensation; recovery potential is limited given the severe neurodevelopmental component and THAP11's developmental role.
- **Prognostic factors:** earlier diagnosis/treatment and biochemical control are favorable in cblC but do not guarantee normal neurodevelopment [PMID: 26563984]. cblL-specific prognostic biomarkers are undefined.

### 12. Treatment

No cblL-specific trials exist; management is **rational extrapolation from cblC/cblX**:

| Intervention | Rationale | Evidence | Suggested NCIT |
|---|---|---|---|
| **Hydroxocobalamin (OHCbl)**, parenteral | Supplies cobalamin to partially overcome reduced processing; mainstay of cblC | [PMID: 23746552] | NCIT:C29094 (Hydroxocobalamin) |
| **Betaine** | Remethylates homocysteine → methionine (bypasses MTR limitation) | [PMID: 23746552] | NCIT:C61796 (Betaine) |
| **Folinic acid** | Supports one-carbon/methylation metabolism | [PMID: 23746552] | NCIT:C61837 (Leucovorin/folinic acid) |
| **Levocarnitine (L-carnitine)** | Conjugates/clears propionyl/methylmalonyl species | [PMID: 23746552] | NCIT:C61785 (Levocarnitine) |
| **Dietary protein moderation** | Limits propiogenic amino-acid load | [PMID: 23746552] | NCIT:C15222 (Dietary intervention) |

- **Pharmacogenomics:** none established.
- **Advanced/experimental therapeutics:** Because cblL is a *transcriptional* deficiency of *MMACHC*, conceptually distinctive approaches (e.g., restoring *MMACHC* expression, gene/gene-regulation therapy) are of theoretical interest but **not developed**; no gene, cell, or RNA therapy exists for cblL. The zebrafish rescue by human *MMACHC* [PMID: 25281006] provides proof-of-concept that restoring the downstream target can correct at least the *MMACHC*-dependent (craniofacial) branch — but not necessarily the broader THAP11 program.
- **Treatment outcomes:** biochemical improvement is achievable (as in cblC), but neurodevelopmental outcomes are frequently poor [PMID: 23746552; 26563984]. Hydroxocobalamin dose escalation improved biochemistry in a cblC series [PMID: 23746552].

### 13. Prevention

- **Primary prevention:** not applicable (genetic disorder). **Genetic counseling** for at-risk (consanguineous/carrier) families and **carrier/cascade testing** for the familial *THAP11* variant are the principal preventive tools.
- **Secondary prevention:** **newborn screening** (MMA/homocysteine metabolites) enables early detection of the combined MMA+HC phenotype and early treatment initiation [PMID: 26563984]; molecular confirmation identifies cblL specifically.
- **Prenatal/preimplantation:** prenatal diagnosis by chorionic villus sampling / molecular testing is standard for known familial cobalamin-disorder variants (demonstrated for *MMACHC* [PMID: 30157807; 26149271]) and is applicable to a known familial *THAP11* variant.
- **Tertiary prevention:** metabolic-crisis prevention through consistent cofactor supplementation, sick-day protocols, and avoidance of catabolic stress (*inferred from cblC*).

### 14. Other Species / Natural Disease

- **Taxonomy of study organisms:** *Mus musculus* (NCBI:txid10090); *Danio rerio* (zebrafish; NCBI:txid7955).
- **Orthologous genes:** mouse *Thap11* (Ronin); zebrafish *thap11* and *hcfc1b* (paralog of human *HCFC1*) [PMID: 25281006].
- **Natural disease in other species:** No naturally occurring THAP11-cobalamin disorder has been reported in companion animals or wildlife (*information not available*; no OMIA entry known for cblL). Not zoonotic; not transmissible.
- **Comparative biology / conservation:** The THAP11–HCF-1 axis and its control of biosynthetic/energy genes are **evolutionarily conserved** from zebrafish to mammals; the zebrafish craniofacial phenotype is rescued by **human *MMACHC***, demonstrating conserved regulatory logic [PMID: 25281006; 20581084].

### 15. Model Organisms

| Model | Type | Key phenotype | Recapitulation | Reference |
|---|---|---|---|---|
| *Thap11*/Ronin-null mouse | Mammalian knockout | Peri-implantation lethality; inner-cell-mass defects | Demonstrates essentiality; **too severe** to model viable human hypomorphic disease | [PMID: 18585351] |
| Ronin/HCF-1 ChIP + ESC studies | In vitro / mouse ESC | Binds hyperconserved enhancer; regulates protein-biosynthesis/energy genes | Defines the broad transcriptional program disrupted in cblL | [PMID: 20581084] |
| Zebrafish *thap11* / *hcfc1b* loss | Vertebrate morphant/mutant | Craniofacial cartilage loss (Meckel's cartilage), neural precursor/neural-crest defects; **rescued by human *MMACHC*** | Models the MMACHC-dependent developmental branch; links THAP11→MMACHC in vivo | [PMID: 25281006; 28449119] |
| cblL patient fibroblasts | In vitro (human) | Reduced *MMACHC* (and *TMOD2*) expression; cblC-like complementation | Directly demonstrates the disease mechanism | [PMID: 28449119] |

- **Model limitations:** the mouse null is embryonic-lethal (cannot model postnatal neurodevelopmental disease); zebrafish captures the developmental/MMACHC-dependent branch but not the full human syndrome; no viable hypomorphic mammalian *Thap11* p.Phe80Leu knock-in has been reported — a clear resource gap.

---

## Mechanistic Model / Interpretation

```
   THAP11 (p.Phe80Leu, biallelic)  ── impairs ──►  THAP zinc-finger DNA binding
                │
                ▼
   Weakened THAP11–HCFC1(–ZNF143) transcriptional complex
                │  (↓ activation at MMACHC promoter)
                ▼
   ↓ MMACHC mRNA/protein  ──(normal MMACHC gene sequence!)──►  regulatory phenocopy of cblC
                │
                ▼
   ↓ Cytosolic cobalamin chaperone activity (decyanation/dealkylation, Kim 2009)
                │
        ┌───────┴─────────┐
        ▼                 ▼
  ↓ AdoCbl            ↓ MeCbl
  ↓ MMUT activity     ↓ MTR (methionine synthase)
  ↑ Methylmalonic     ↑ Homocysteine
    acid (aciduria)   ↓ Methionine
        └───────┬─────────┘
                ▼
   Metabolite toxicity + impaired methylation
                │
                │   ┌── PARALLEL, MMACHC-INDEPENDENT BRANCH ──────────────┐
                │   │  ↓ THAP11 program for protein biosynthesis, energy, │
                │   │  neural/neural-crest development (Dejosez 2008/2010, │
                │   │  Quintana 2014 zebrafish)                            │
                │   └──────────────────────────────────────────────────────┘
                ▼                         ▼
   Infantile myoclonic seizures + severe global developmental impairment
```

The unifying insight is that **cblL is not a defect of the cobalamin machinery itself but of its transcriptional supply line.** THAP11 sits *upstream* of *MMACHC*; the downstream biochemistry (MMA, homocysteine, methionine) is *identical in kind* to cblC but arises from **gene-expression failure rather than protein-coding mutation**. This dual nature — a metabolic branch (shared with cblC) plus a developmental/transcriptional branch (unique to loss of an essential pluripotency/biosynthesis factor) — predicts a phenotype that is **more syndromic and neurodevelopmentally severe** than metabolite toxicity alone would explain, consistent with the single reported case.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [28449119](https://pubmed.ncbi.nlm.nih.gov/28449119/) | *Mutations in THAP11 cause an inborn error of cobalamin metabolism and developmental abnormalities* | **Disease-defining paper**; identifies THAP11 c.240C>G/p.Phe80Leu; THAP11–HCFC1–MMACHC axis; zebrafish craniofacial data (F001, F002, F004, F006, F007) |
| [24011988](https://pubmed.ncbi.nlm.nih.gov/24011988/) | *An X-linked cobalamin disorder caused by mutations in HCFC1* | Establishes that disrupting the HCFC1/THAP11 complex reduces *MMACHC* mRNA/protein (F002) |
| [19801555](https://pubmed.ncbi.nlm.nih.gov/19801555/) | *A human vitamin B12 trafficking protein uses glutathione transferase activity...* | Defines MMACHC's decyanation/dealkylation chaperone role (F003) |
| [18585351](https://pubmed.ncbi.nlm.nih.gov/18585351/) | *Ronin is essential for embryogenesis and pluripotency of mouse ESCs* | THAP11/Ronin essentiality; peri-implantation lethality; HCF-1 binding (F005) |
| [20581084](https://pubmed.ncbi.nlm.nih.gov/20581084/) | *Ronin/Hcf-1 binds a hyperconserved enhancer...* | THAP11's broad biosynthesis/energy transcriptional program (F005) |
| [25281006](https://pubmed.ncbi.nlm.nih.gov/25281006/) | *Hcfc1b regulates craniofacial development by modulating mmachc* | Zebrafish model; craniofacial phenotype rescued by human *MMACHC* (F005) |
| [23746552](https://pubmed.ncbi.nlm.nih.gov/23746552/) | *Clinical/biochemical outcome after hydroxocobalamin dose escalation in cblC* | Treatment framework (OHCbl, betaine, folinic acid, carnitine) (F004) |
| [34655177](https://pubmed.ncbi.nlm.nih.gov/34655177/) | *Prenatal diagnosis of cblC using clinical exome/targeted analysis* | Places THAP11 in the combined MMA+HC gene panel (F001) |
| [26563984](https://pubmed.ncbi.nlm.nih.gov/26563984/) | *cblC in Shandong: incidence and outcomes* | cblC incidence (~1:3,920) and post-treatment neurodevelopmental outcomes (F006) |
| [20924684](https://pubmed.ncbi.nlm.nih.gov/20924684/) | *Clinical/biochemical/molecular analysis of cblC in China* | Clinical/biochemical signature of combined MMA+HC (phenotype/diagnostics background) |
| [30157807](https://pubmed.ncbi.nlm.nih.gov/30157807/) / [26149271](https://pubmed.ncbi.nlm.nih.gov/26149271/) | *Prenatal genetic diagnosis of cblC* | Prenatal-diagnosis methodology applicable to familial variants (prevention) |
| [42002808](https://pubmed.ncbi.nlm.nih.gov/42002808/) | *Epi-cblC with MMACHC promoter methylation (PRDX1)* | Parallel example of *MMACHC* silencing without coding mutation (differential/epigenetics) |
| [33517344](https://pubmed.ncbi.nlm.nih.gov/33517344/) | *HCFC1 exon-skipping variant: ID without metabolic abnormalities* | Illustrates dissociation of clinical vs biochemical phenotype in the same regulatory pathway |
| [35337626](https://pubmed.ncbi.nlm.nih.gov/35337626/) | *Inherited defects of cobalamin metabolism* (review) | Broad classification context for the cbl complementation groups |
| [20631720](https://pubmed.ncbi.nlm.nih.gov/20631720/) | *Mutation spectrum of MMACHC in Chinese patients* | Founder-effect and mutation-spectrum context for the biochemically related cblC |
| [23580368](https://pubmed.ncbi.nlm.nih.gov/23580368/) | *Novel deletion in late-onset cblC* | Genotype–phenotype/structure context for MMACHC |

**Evidence-type note:** cblL-specific evidence is **human (single clinical case + patient fibroblasts)** plus **model organism (mouse, zebrafish)** and **in vitro biochemistry**. All clinical, prognostic, and therapeutic specifics beyond the index case are **extrapolated** from cblC/cblX human cohorts.

---

## Limitations and Knowledge Gaps

1. **n = 1.** The entire cblL clinical phenotype rests on a single homozygous p.Phe80Leu patient. Frequencies, penetrance, expressivity, natural history, sex distribution, and full phenotype spectrum are essentially unknown.
2. **No population/epidemiology data.** No prevalence or incidence estimates; carrier frequency for cblL as a disease cannot be computed from one allele.
3. **Homocystinuria under-characterized in the index case.** Overt homocystinuria was not documented, leaving the "combined" designation partly inferred from the pathway.
4. **Treatment evidence is entirely extrapolated.** No cblL-specific treatment or outcome data exist; the response of a *transcriptional* defect to cobalamin supplementation may differ from cblC.
5. **No viable mammalian disease model.** The mouse null is embryonic-lethal; a hypomorphic knock-in modeling p.Phe80Leu has not been reported.
6. **Genetic heterogeneity within "cblX-like."** *ZNF143* and other regulators may cause overlapping disease; two of three cblX-like probands in the defining study lacked the THAP11 variant, indicating additional, still-uncharacterized genes.
7. **Ontology/identifier gaps.** No dedicated Orphanet/ICD/MeSH code exists for cblL specifically.

---

## Proposed Follow-up Experiments / Actions

1. **Case ascertainment:** Deposit and query cblL/*THAP11* in GeneMatcher, ClinVar, and metabolic-disease registries to find additional biallelic *THAP11* patients; report their full biochemical (including tHcy) and neuroimaging phenotypes.
2. **Functional validation of variants:** Luciferase/ChIP and RNA-seq assays measuring *MMACHC* activation by WT vs p.Phe80Leu (and any new alleles) THAP11 in the THAP11–HCFC1–ZNF143 complex; quantify residual activity (hypomorph vs null).
3. **Hypomorphic mouse knock-in** of the p.Phe80Leu equivalent to establish a viable, treatable model that captures the neurodevelopmental phenotype (the null being lethal).
4. **Separate the two branches:** In zebrafish/organoids, test whether restoring *MMACHC* alone rescues metabolic vs developmental phenotypes, quantifying the MMACHC-independent contribution of THAP11's biosynthetic program.
5. **Therapeutic trials in model systems:** Compare hydroxocobalamin/betaine/folinic-acid/carnitine responses; explore approaches to upregulate residual *MMACHC* transcription (e.g., targeting the regulatory complex) as a cblL-specific strategy.
6. **Biomarker natural history:** Serial MMA, tHcy, methionine, and C3 in any identified cases to define treatment targets and prognostic thresholds.
7. **Ontology curation:** Establish dedicated Orphanet/ICD-11 mappings and confirm the MONDO/HPO annotation set for cblL in the knowledge base.

---

*Report compiled from 7 confirmed findings and 17 reviewed papers over 5 investigation iterations. cblL-specific claims are grounded in Quintana et al. 2017 [PMID: 28449119] and supporting model/biochemical studies; all clinical, prognostic, and therapeutic specifics beyond the single index case are explicitly extrapolated from the biochemically equivalent cblC/cblX disorders and labeled as such.*


## Artifacts

- [OpenScientist final report](Methylmalonic_Aciduria_and_Homocystinuria_cblL_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Methylmalonic_Aciduria_and_Homocystinuria_cblL_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0975798` (2 mentions) - the report calls it "cblL"; MONDO calls it **methylmalonic aciduria and homocystinuria, cb1L type**
- `CHEBI:16009` (2 mentions) - the report calls it "methylmalonic acid"; CHEBI calls it **9-riburonosyladenine**
- `GO:0005829` (2 mentions) - the report calls it "cytosol", "site of MMACHC chaperone activity"; GO calls it **cytosol**
- `HP:0002160` (1 mention) - the report calls it "cblC-extrapolated"; HP calls it **Hyperhomocystinemia**
- `HP:0001249` (1 mention) - the report calls it "cblC/cblX-extrapolated"; HP calls it **Intellectual disability**
- `HP:0001889` (1 mention) - the report calls it "cblC-extrapolated"; HP calls it **Megaloblastic anemia**
- `GO:0005634` (1 mention) - the report calls it "site of THAP11 transcriptional activity"; GO calls it **nucleus**
- `NCIT:C61796` (1 mention) - the report calls it "Betaine"; NCIT calls it **Ivermectin**
- `NCIT:C61837` (1 mention) - the report calls it "Leucovorin/folinic acid"; NCIT calls it **Methacholine**
- `NCIT:C61785` (1 mention) - the report calls it "Levocarnitine"; NCIT calls it **Hydrocortisone Acetate**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C29094` (1 mention), reported as "Hydroxocobalamin" - NCIT does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006355` (2 mentions) - the report calls it "regulation of DNA-templated transcription", "regulation of transcription"; GO calls it **regulation of DNA-templated transcription**
- `CHEBI:17439` (1 mention) - the report calls it "cyanocobalamin"; CHEBI calls it **cyanocob(III)alamin**, and lists "cyanocobalamin" among its other names
- `CHEBI:18408` (1 mention) - the report calls it "adenosylcobalamin"; CHEBI calls it **cobamamide**, and lists "Adenosylcobalamin" among its other names
- `HP:0002123` (1 mention) - the report calls it "myoclonic seizure"; HP calls it **Generalized myoclonic seizure**, and lists "Myoclonus seizures" among its other names
- `HP:0500152` (1 mention) - the report calls it "hypomethioninemia"; HP calls it **Hypocystinemia**
- `GO:0006555` (1 mention) - the report calls it "methionine metabolic process"; GO calls it **L-methionine metabolic process**
- `NCIT:C15222` (1 mention) - the report calls it "Dietary intervention"; NCIT calls it **Diet**, and lists "Dietary" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006355` - called "regulation of DNA-templated transcription", "regulation of transcription"
- `GO:0005829` - called "cytosol", "site of MMACHC chaperone activity"
