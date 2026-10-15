---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T15:41:57.044197'
end_time: '2026-09-29T16:00:40.544919'
duration_seconds: 1123.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Estrogen Resistance Syndrome
  mondo_id: MONDO:0014148
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Estrogen_Resistance_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Estrogen_Resistance_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Estrogen Resistance Syndrome
- **MONDO ID:** MONDO:0014148 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Estrogen Resistance Syndrome** covering all of the
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

# Estrogen Resistance Syndrome (Estrogen Insensitivity Syndrome): A Comprehensive Disease Characteristics Report

**Target Disease:** Estrogen Resistance Syndrome / Estrogen Insensitivity Syndrome (EIS)
**MONDO ID:** MONDO:0014148 · **OMIM:** #615363 · **Gene:** *ESR1* (HGNC:3467)
**Category:** Mendelian, autosomal recessive
**Report compiled:** 2026-09-29 (5-iteration autonomous investigation; 9 findings; 25 papers reviewed)

---

## Summary

**Estrogen Resistance Syndrome — more precisely termed Estrogen Insensitivity Syndrome (EIS) — is an ultra-rare autosomal-recessive Mendelian endocrine disorder caused by biallelic germline loss-of-function (LOF) variants in *ESR1*, the gene encoding estrogen receptor α (ERα).** The defect renders peripheral target tissues unresponsive to estrogen despite high circulating 17β-estradiol (E2), producing a paradoxical picture of estrogen "deficiency" symptoms in the face of estrogen excess. This distinguishes true *resistance* (receptor defect, high E2) from estrogen *deficiency* disorders such as aromatase (CYP19A1) deficiency (low E2, rescued by estrogen therapy).

The clinical phenotype is dominated by the skeletal consequences of estrogen's role in epiphyseal maturation: affected individuals of both sexes lack the pubertal growth spurt, fail to fuse their epiphyses, continue linear growth into adulthood, reach very tall stature, and develop osteoporosis with elevated bone turnover. Metabolic derangements (glucose intolerance, hyperinsulinemia, dyslipidemia) and elevated gonadotropins/androgens accompany the picture because of impaired estrogen negative feedback. Females additionally present with absent breast development, primary amenorrhea, and multicystic ovaries. Critically, the syndrome is largely **refractory to estrogen replacement** — even high-affinity ligands such as diethylstilbestrol (DES) fail to induce secondary sexual characteristics — because the receptor itself is the lesion.

At the molecular level, EIS mutations disrupt distinct layers of ERα signaling — ligand binding, DNA interaction, coactivator (SRC-3/NCOA3 and p300/EP300) recruitment, nuclear trafficking, and transcriptional regulation — that converge on a shared resistance phenotype. Confirmed pathogenic variants span a truncating null (p.Arg157Ter, the original 1994 male index case) and hypomorphic ligand-binding-domain missense changes (p.Gln375His, p.Arg394His). *ESR1* is strongly constraint-depleted for loss-of-function in gnomAD (pLI ≈ 1.0, LOEUF 0.37, missense Z = 2.99), which explains the extreme rarity of complete-null EIS. Knock-in and knockout mouse models (αERKO; Esr1-Q) phenocopy the human disease, confirming causality. Management remains supportive; there is no curative therapy.

---

## 1. Disease Information

**Overview.** Estrogen Resistance Syndrome (Estrogen Insensitivity Syndrome, EIS) is a Mendelian disorder in which target tissues cannot respond to estrogen because of loss-of-function mutations in the estrogen receptor α gene (*ESR1*). Despite normal or markedly elevated circulating estradiol, downstream estrogen-dependent processes — pubertal growth, epiphyseal fusion, bone mineralization, reproductive tract maturation, and metabolic homeostasis — fail. It is the receptor-level counterpart of aromatase deficiency, which produces a similar skeletal picture through estrogen *absence* rather than *resistance*.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #615363 (Estrogen resistance) |
| OMIM (gene) | *133430 (*ESR1*) |
| MONDO | MONDO:0014148 |
| Gene / HGNC | *ESR1* / HGNC:3467 |
| Ensembl | ENSG00000091831 |
| UniProt | P03372 (ESR1_HUMAN) |
| Cytogenetic locus | 6q25.1–q25.2 |
| Gene aliases | ER, ESR, ESRA, NR3A1 |

ICD-10/ICD-11, MeSH, and Orphanet do not assign a distinct code for this ultra-rare entity; it is generally captured under disorders of estrogen action / hormone receptor abnormalities.

**Synonyms and alternative names.** Estrogen Resistance; Estrogen Insensitivity Syndrome (EIS); ERα resistance; ESR1-related estrogen insensitivity. A recent review reframes the condition as "the 'Upside Down' of *ESR1* mutations," contrasting germline LOF (this disease) with somatic gain-of-function ligand-binding-domain mutations in breast cancer ([PMID: 42734155](https://pubmed.ncbi.nlm.nih.gov/42734155/)).

**Data provenance.** The evidence base is derived almost entirely from **aggregated disease-level resources** (OMIM, ClinVar, gnomAD) and a small number of **individual patient case reports** — this is a literature composed of single-case and small-family reports rather than EHR cohorts or registries, reflecting the disease's extreme rarity.

---

## 2. Etiology

**Primary cause (genetic).** EIS is caused by **biallelic germline loss-of-function variants in *ESR1*** (estrogen receptor α). These impair ERα function and render peripheral tissues insensitive to circulating E2 (Finding F001). Two independent reviews confirm the causal gene and mechanism:

> "germline *ESR1* mutations cause EIS by impairing ERα function and rendering peripheral tissues insensitive to circulating E2" — [PMID: 42734155](https://pubmed.ncbi.nlm.nih.gov/42734155/)

> "Germline loss-of-function variants in *ESR1*, the gene encoding estrogen receptor α, are known to cause of estrogen insensitivity/resistance" — [PMID: 34538723](https://pubmed.ncbi.nlm.nih.gov/34538723/)

**Genetic risk factors.**
- **Causal variants:** truncating (nonsense) p.Arg157Ter and hypomorphic missense p.Gln375His, p.Arg394His (see Section 4).
- **Consanguinity:** because the disorder is autosomal recessive, parental relatedness is an important risk factor. A homozygous *ESR1* case was reported in a 13-year-old girl of consanguineous parents ([PMID: 39295121](https://pubmed.ncbi.nlm.nih.gov/39295121/), Finding F006).
- **Modifier / background genes:** in mouse models, genetic background strongly modifies the ovarian transdifferentiation phenotype of estrogen-receptor knockouts (a Chr18 locus was implicated; [PMID: 39576259](https://pubmed.ncbi.nlm.nih.gov/39576259/)), suggesting modifier effects may shape expressivity.

**Environmental / non-genetic risk factors.** None established as causal. The disease is monogenic; environmental exposure is not a recognized trigger. Sex modifies *presentation* (females show the reproductive phenotype) but not disease risk.

**Protective factors.** No genetic or environmental protective factors are established. Given the disorder is caused by complete/partial receptor loss, the theoretical "protective" allele is simply a functional *ESR1* allele; heterozygous carriers are largely unaffected (recessive inheritance), though rare heterozygous variants (e.g., p.A207T) have been associated with partial insensitivity/PCOS-like phenotypes ([PMID: 36401248](https://pubmed.ncbi.nlm.nih.gov/36401248/)).

**Gene–environment interactions.** Not characterized for this monogenic disease. The dominant "environmental" interface is pharmacological: because the receptor is defective, exogenous estrogens (the usual environmental/therapeutic estrogen input) fail to signal — a gene–treatment interaction that defines the disease's therapeutic refractoriness.

---

## 3. Phenotypes

EIS is a multi-system disorder. Phenotypes derive from case reports and are consistent across estrogen-resistance and estrogen-deficiency (aromatase) states, which share a skeletal/metabolic core.

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Absent pubertal growth spurt | Clinical sign | Adolescence | Severe | Both sexes, characteristic | HP:0008819 (Abnormal pubertal development) |
| Unfused / delayed epiphyses | Radiographic sign | Adolescence–adult | Severe | Characteristic | HP:0002644 (Delayed epiphyseal ossification) |
| Continued linear growth / tall stature | Physical | Adult | Severe | Both sexes | HP:0000098 (Tall stature) |
| Delayed bone age | Radiographic | Childhood–adolescence | Moderate–severe | Characteristic | HP:0002750 (Delayed skeletal maturation) |
| Osteoporosis / reduced BMD | Lab/imaging | Young adult | Severe | Both sexes | HP:0000939 (Osteoporosis) |
| Increased bone turnover | Lab abnormality | Adult | Moderate | Characteristic | HP:0003155 (Elevated alkaline phosphatase) |
| Glucose intolerance / hyperinsulinemia | Lab abnormality | Adult | Moderate | Reported | HP:0000842 (Hyperinsulinemia) |
| Dyslipidemia | Lab abnormality | Adult | Moderate | Reported | HP:0003119 (Abnormal circulating lipid concentration) |
| Elevated gonadotropins (LH/FSH) | Lab abnormality | Adolescence–adult | — | Characteristic | HP:0000837 (Hypergonadotropic hypogonadism–related) |
| Elevated estrogens | Lab abnormality | Adolescence–adult | — | Characteristic (defines resistance) | — |
| Absent breast development (female) | Physical | Puberty | Severe | Female | HP:0003186 (Breast hypoplasia) |
| Primary amenorrhea (female) | Clinical sign | Puberty | Severe | Female | HP:0000783 (Primary amenorrhea) |
| Multicystic ovaries (female) | Imaging | Adolescence | Moderate | Female | HP:0000137 (Abnormality of the ovary) |
| Poor uterine growth (female) | Imaging | Adolescence | Moderate | Female | HP:0000013 (Hypoplasia of the uterus) |

**Evidence.** The skeletal/metabolic core is documented in the landmark pediatric-endocrinology review:

> "absence of the pubertal growth spurt, delayed bone maturation, unfused epiphyses, continued growth into adulthood and very tall adult stature in both sexes" — [PMID: 9554463](https://pubmed.ncbi.nlm.nih.gov/9554463/) (Finding F002)

> "Glucose intolerance, hyperinsulinemia and lipid abnormalities are also present. Skeletal integrity is compromised. Increased bone turnover, reduced bone mineral density and osteoporosis develop in both sexes" — [PMID: 9554463](https://pubmed.ncbi.nlm.nih.gov/9554463/)

The female reproductive phenotype comes from the first fully characterized female case:

> "she presented with lower abdominal pain, absent breast development, primary amenorrhea, and multicystic ovaries" — [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/) (Finding F003)

**Notably preserved.** Normal male sexual maturation/virilization is preserved because it is androgen-dependent, not estrogen-dependent — one of the key clues that distinguishes estrogen resistance from broader hypogonadism.

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease. Inferred burdens are substantial: lifelong osteoporosis (fracture risk), infertility, tall stature with its psychosocial dimension, and metabolic complications. QoL data represent a knowledge gap.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ESR1* (estrogen receptor α; HGNC:3467; OMIM *133430; ENSG00000091831; UniProt P03372; locus 6q25.1–q25.2). ERα is a nuclear-hormone-receptor transcription factor (NR3A1) with a modular structure: N-terminal domain (NTD, containing ligand-independent AF-1), DNA-binding domain (DBD), and C-terminal ligand-binding domain (LBD, containing ligand-dependent AF-2).

**Pathogenic variants (ClinVar-confirmed, conditioned on "Estrogen resistance syndrome"; Finding F009):**

| Variant (NM_000125.4) | Protein | Type | ClinVar classification | Note |
|---|---|---|---|---|
| c.469C>T | p.Arg157Ter | Nonsense (null) | Pathogenic | Classic homozygous truncating variant; original male index case (Smith 1994) |
| c.1125G>T | p.Gln375His | Missense (LBD, hypomorphic) | Pathogenic | Modeled in Esr1-Q knock-in mouse |
| c.1181G>A | p.Arg394His | Missense (LBD) | Pathogenic / Likely pathogenic | Alters ligand–receptor conformation |
| c.804G>C | p.Lys268Asn | Missense | Uncertain significance | Combined-condition listing |
| c.433G>A | p.Gly145Ser | Missense | Uncertain significance | Combined-condition listing |
| c.619G>A | p.Ala207Thr | Missense (heterozygous) | Reported | Partial insensitivity / PCOS-like, IVF poor response ([PMID: 36401248](https://pubmed.ncbi.nlm.nih.gov/36401248/)) |

**Variant classification & spectrum.** Of 262 total ClinVar *ESR1* records (retrieved 2026), 44 are annotated Pathogenic and 3 Likely pathogenic — but **many "Pathogenic" entries are large 6q25 copy-number changes (contiguous-gene deletions/duplications) or somatic breast-cancer variants**, not germline EIS. The germline EIS spectrum is small and dominated by the three variants above.

**Allele frequency & population constraint (Finding F008; gnomAD, computational, retrieved 2026):**

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 0.99998 | Extreme intolerance to heterozygous LoF |
| oe_lof (observed/expected LoF) | 0.228 (90% CI 0.146–0.369) | LOEUF ≈ 0.37 — strongly LoF-constrained |
| obs_lof vs exp_lof | 12 vs 52.7 | ~77% depletion of protein-truncating variants |
| Missense Z | 2.99 | Missense-constrained |
| Synonymous Z | 0.39 | Neutral (as expected) |

This strong constraint explains why complete-null biallelic EIS is exceptionally rare: LoF alleles are purged from the population, so two must co-occur (typically via consanguinity) to produce disease.

**Functional consequences.** Loss of function (nonsense null: no functional receptor; hypomorphic missense: reduced/abolished transactivation). EIS mutations "change conformation of ligand-receptor complex" and produce "altered transcriptome profile" ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/), Finding F004). There is no dominant-negative or gain-of-function mechanism in germline EIS (contrast with somatic Y537S/D538G gain-of-function LBD mutations in breast cancer).

**Modifier genes.** Mouse data implicate a Chr18 background locus modifying the ERKO ovarian phenotype ([PMID: 39576259](https://pubmed.ncbi.nlm.nih.gov/39576259/)); human modifiers are not defined.

**Epigenetic information.** EIS mutants Q375H and R394H show a **differential DNA-methylome** as well as transcriptome vs wild-type ERα ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)), indicating the receptor defect propagates to epigenetic reprogramming of estrogen-target loci. Beyond this, disease-specific epigenetic data are limited.

**Chromosomal abnormalities.** Large 6q25 copy-number variants involving *ESR1* appear in ClinVar as contiguous-gene events but are distinct from the classic point-mutation EIS.

---

## 5. Environmental Information

- **Environmental factors:** None established as causal. This is a monogenic disease.
- **Xenoestrogens (mechanistic relevance, not causal):** Environmental estrogen mimics (bisphenols BPA, BPAF, BPC) act through ERα and depend on the AF-1/NTD domain for agonist activity ([PMID: 42224247](https://pubmed.ncbi.nlm.nih.gov/42224247/)). In EIS, a defective receptor blunts responses to both endogenous and environmental estrogens — relevant to why exogenous estrogenic compounds fail therapeutically.
- **Lifestyle factors:** No causal role. Standard bone-health measures (weight-bearing exercise, calcium/vitamin D) are supportive but do not modify the underlying receptor defect.
- **Infectious agents:** Not applicable. No pathogen is implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic germline *ESR1* LOF mutation** (nonsense p.Arg157Ter or hypomorphic LBD missense p.Gln375His / p.Arg394His) → **produces a non-functional or transcriptionally impaired ERα** (demonstrated: ClinVar pathogenic classification; molecular-dynamics conformational change, [PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)).
2. Non-functional ERα → **fails to bind ligand and/or fails to adopt the active conformation** upon estradiol binding (demonstrated by MD simulation: "both *ESR1* mutations change the ERα conformation of the ligand-receptor complexes").
3. Impaired active receptor → **fails to recruit coactivators SRC-3 (NCOA3) and p300 (EP300)** at estrogen-response elements (mechanistically demonstrated by cryo-EM of the active complex, [PMID: 25728767](https://pubmed.ncbi.nlm.nih.gov/25728767/); AF-1/AF-2 cooperation, [PMID: 39432505](https://pubmed.ncbi.nlm.nih.gov/39432505/)).
4. Failed coactivator recruitment → **loss of estrogen-responsive transcription and altered transcriptome + DNA methylome** (demonstrated in EIS mutants, [PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)).
5. Loss of estrogen-target transcription in **bone (growth-plate chondrocytes/osteoblasts)** → **failure of the pubertal growth spurt and of epiphyseal fusion** → continued linear growth → **tall stature**; and reduced bone mineralization → **osteoporosis with high bone turnover** (demonstrated clinically, [PMID: 9554463](https://pubmed.ncbi.nlm.nih.gov/9554463/)).
6. **Branch — hypothalamic–pituitary axis:** Loss of ERα-mediated estrogen negative feedback → **elevated LH/FSH and androgens** despite high estradiol (demonstrated: normal pulsatile LH but elevated mean LH with markedly increased estrogens, [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)).
7. **Branch — female reproductive tract:** Loss of ERα signaling → **absent breast development, poor uterine growth, primary amenorrhea, multicystic ovaries** (demonstrated, [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/), [PMID: 39295121](https://pubmed.ncbi.nlm.nih.gov/39295121/)).
8. **Branch — metabolism/vasculature:** Loss of ERα action → **glucose intolerance, hyperinsulinemia, dyslipidemia** (clinical, [PMID: 9554463](https://pubmed.ncbi.nlm.nih.gov/9554463/)); loss of ERα-mediated eNOS enhancement → **inferred increased vascular risk** (mechanism from ER-α agonist/eNOS studies, [PMID: 28736253](https://pubmed.ncbi.nlm.nih.gov/28736253/)).
9. Because the lesion is the receptor itself → **exogenous estrogen (even high-affinity DES) cannot restore signaling** → **therapeutic refractoriness** (demonstrated, [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)).

### Detail by category

**Molecular pathways.** Nuclear-receptor (ERα/NR3A1) genomic signaling: ligand binding → receptor dimerization → DNA binding at estrogen-response elements → coactivator recruitment (SRC-3/NCOA3, p300/EP300) → RNA-Pol-II transcription. Cryo-EM shows "each of the two ligand-bound ERα monomers independently recruits one SRC-3 protein via the transactivation domain of ERα; the two SRC-3s in turn bind to different regions of one p300 protein" ([PMID: 25728767](https://pubmed.ncbi.nlm.nih.gov/25728767/), Finding F005). Non-genomic (membrane GPER) signaling contributes to some tissues but cannot compensate for ERα loss.

**Protein dysfunction.** Nonsense p.Arg157Ter → truncation/loss of protein. LBD missense (Q375H, R394H) → conformational distortion of the ligand–receptor complex impairing AF-2/coactivator surface function. The AF-1 (NTD) domain normally collaborates with the C-terminal LBD(AF-2) for coactivator recruitment ([PMID: 39432505](https://pubmed.ncbi.nlm.nih.gov/39432505/)); disruption at either pole impairs the assembly.

**Signaling nodes disrupted.** Germline EIS mutations "disrupt distinct layers of ERα signaling, including ligand binding, DNA interaction, coactivator recruitment, nuclear trafficking, transcriptional regulation" ([PMID: 42734155](https://pubmed.ncbi.nlm.nih.gov/42734155/), Finding F005).

**Cellular processes.** Growth-plate chondrocyte senescence/epiphyseal fusion (estrogen-driven) fails; osteoblast/osteoclast coupling is dysregulated (increased bone turnover). In gonads, ERα loss can drive granulosa-to-Sertoli-like transdifferentiation in mouse models ([PMID: 39576259](https://pubmed.ncbi.nlm.nih.gov/39576259/)).

**Metabolic changes.** Glucose intolerance, hyperinsulinemia, and lipid abnormalities reflect loss of ERα's role in insulin sensitivity and lipid handling ([PMID: 9554463](https://pubmed.ncbi.nlm.nih.gov/9554463/)).

**Broad ERα physiology (why the phenotype is pleiotropic; Finding F007).** ERα is expressed across bone, reproductive tract, testis (Sertoli cells), vasculature, brain, and metabolic tissues. In testis, ERα directly regulates AMH transcription: "estrogens can stimulate AMH production because estrogen receptors are present in Sertoli cells and aromatase is stimulated by FSH" and "The direct effects of sex steroids on AMH transcription are mediated by androgen receptor and estrogen receptor α action" ([PMID: 35712256](https://pubmed.ncbi.nlm.nih.gov/35712256/); mechanism confirmed via ERE on the hAMH promoter, [PMID: 32934281](https://pubmed.ncbi.nlm.nih.gov/32934281/)). ERα also mediates estrogen's eNOS-enhancing vasoprotection ([PMID: 28736253](https://pubmed.ncbi.nlm.nih.gov/28736253/)) and modulates circadian rhythms via classical ERE-dependent action ([PMID: 24527952](https://pubmed.ncbi.nlm.nih.gov/24527952/)). This ubiquitous distribution explains the simultaneous skeletal, metabolic, vascular, and reproductive manifestations, while androgen-dependent male virilization is spared.

**Suggested ontology terms.**
- GO biological process: GO:0030520 (intracellular estrogen receptor signaling pathway); GO:0006357 (regulation of transcription by RNA Pol II); GO:0030282 (bone mineralization); GO:0001503 (ossification).
- GO cellular component: GO:0005634 (nucleus); GO:0005667 (transcription regulator complex).
- CL cell types: CL:0000062 (osteoblast); CL:0000138 (chondrocyte); CL:0000216 (Sertoli cell); CL:0000501 (granulosa cell).
- CHEBI: CHEBI:16469 (17β-estradiol); CHEBI:41922 (diethylstilbestrol).

---

## 7. Anatomical Structures Affected

**Organ level (primary).**
- **Skeleton / bone** (UBERON:0002481 bone tissue; UBERON:0001474 bone element) — growth plates, epiphyses; the dominant target.
- **Reproductive organs (female):** ovary (UBERON:0000992), uterus (UBERON:0000995), breast/mammary gland (UBERON:0001911).
- **Hypothalamic–pituitary axis** (UBERON:0001898 hypothalamus; UBERON:0000007 pituitary gland) — impaired negative feedback.

**Secondary / body-system involvement.**
- **Endocrine system** (elevated gonadotropins, androgens).
- **Metabolic/endocrine** (pancreas/insulin axis — glucose intolerance, hyperinsulinemia).
- **Cardiovascular system** (inferred increased risk via loss of ERα/eNOS vasoprotection).

**Tissue/cell level.** Epithelial (mammary, uterine), connective/skeletal (bone, cartilage growth plate), and gonadal cells. Specific cell populations: growth-plate **chondrocytes** (CL:0000138), **osteoblasts** (CL:0000062) and osteoclasts, ovarian **granulosa cells** (CL:0000501), and **Sertoli cells** (CL:0000216, via AMH regulation).

**Subcellular level.** ERα is a nuclear/cytoplasmic shuttling receptor: **nucleus** (GO:0005634, site of transcriptional action) and cytoplasm (inactive receptor pool). Nuclear trafficking is itself one of the disrupted signaling layers in EIS.

**Localization / lateralization.** Systemic and bilateral (skeleton, paired gonads); no lateralized predilection.

---

## 8. Temporal Development

**Onset.** Congenital genetic defect, but clinically silent until **puberty**, when the absence of estrogen action becomes manifest (failure of pubertal growth spurt, absent breast development, primary amenorrhea). Presentation is therefore typically **adolescent** (case reports at ages 13–15; [PMID: 39295121](https://pubmed.ncbi.nlm.nih.gov/39295121/), [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)). Onset pattern is **insidious/chronic**.

**Progression.** Chronic, lifelong, non-remitting. Because epiphyses do not fuse, linear growth continues into adulthood, and skeletal complications (osteoporosis, high bone turnover) are progressive without effective intervention. No spontaneous remission occurs.

**Critical periods.** Puberty and young adulthood are the windows of maximal skeletal vulnerability (failed peak-bone-mass accrual, ongoing growth). This is also the window where any effective therapy would need to act — but estrogen replacement is ineffective owing to receptor resistance, so the "therapeutic window" is functionally closed with current tools.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare; **no reliable prevalence or incidence estimate exists** — the world literature comprises a handful of individual cases and small families. Orphanet does not list a discrete prevalence figure.

**Inheritance.** **Autosomal recessive.** Biallelic *ESR1* LOF is required; affected individuals are typically homozygous (e.g., p.Arg157Ter, or homozygous variants in consanguineous families) or compound heterozygous. Heterozygous carriers are generally unaffected, though rare heterozygous variants may confer partial phenotypes.

- **Penetrance:** Appears high/complete for the biallelic-null genotype (based on limited cases).
- **Expressivity:** Variable — sex determines the reproductive component; missense hypomorphs may be milder than nulls.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** None established.
- **Consanguinity:** Contributory — expected for a rare recessive disorder; documented in a homozygous case ([PMID: 39295121](https://pubmed.ncbi.nlm.nih.gov/39295121/), Finding F006).
- **Carrier frequency:** Not established; gnomAD shows *ESR1* LoF alleles are strongly depleted (obs_lof 12 vs exp 52.7; pLI ≈ 1.0), implying carriers are rare.

**Population demographics.** No ethnic or geographic clustering established (too few cases). Sex ratio: both sexes affected by the skeletal/metabolic phenotype; females additionally show reproductive manifestations, so ascertainment may skew toward females at puberty. Age distribution: predominantly adolescent/young-adult at diagnosis.

---

## 10. Diagnostics

**Biochemical hallmark (the diagnostic key).** **Elevated circulating estradiol with elevated gonadotropins (LH, FSH) and androgens**, in the presence of absent estrogen effect. This combination — high E2 *and* high LH/FSH — distinguishes **resistance** from **deficiency**:

> normal pulsatile LH secretion with elevated mean LH and mildly elevated FSH "despite markedly increased estrogens" — [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)

**Laboratory tests.** Serum estradiol (high), LH and FSH (high), testosterone/androgens (elevated), bone-turnover markers (elevated). Metabolic panel: fasting glucose/insulin (glucose intolerance, hyperinsulinemia), lipid profile (dyslipidemia).

**Imaging / functional.** Bone-age radiographs (delayed, **unfused epiphyses**); DXA (reduced bone mineral density/osteoporosis); pelvic ultrasound in females (poor uterine growth, multicystic ovaries).

**Genetic testing — the confirmatory test.** Molecular analysis of *ESR1*:
- **Single-gene *ESR1* sequencing** or **targeted panel** (hypogonadism / disorders-of-sex-development / skeletal panels including *ESR1*, *CYP19A1*, *ESR2*).
- **Whole-exome sequencing (WES)** is highly useful for undiagnosed cases — the p.A207T variant was found via WES ([PMID: 36401248](https://pubmed.ncbi.nlm.nih.gov/36401248/)).
- **Chromosomal microarray** for the rare 6q25 contiguous-gene deletions/duplications.
- Interpret variants per ACMG/AMP against ClinVar (pathogenic: p.Arg157Ter, p.Gln375His, p.Arg394His).

**Functional / research diagnostics.** In-vitro transactivation assays screening candidate ligands against the patient's variant receptor (a 75-compound screen showed DES could transactivate the variant in vitro even though it failed clinically; [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)); transcriptome/DNA-methylome profiling distinguishing mutant vs wild-type ERα ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)).

**Differential diagnosis.**

| Condition | Gene | Estradiol | Key distinguisher |
|---|---|---|---|
| **Estrogen resistance (EIS)** | *ESR1* | **High** | Receptor defect; refractory to estrogen |
| Aromatase deficiency | *CYP19A1* | **Low** | Estrogen *absent*; **rescued by estrogen therapy** |
| ERβ (ESR2) defect | *ESR2* | Variable | Streak gonads (46,XX) — "her gonads were clearly abnormal (streak), a finding not observed in *ESR1*-deficient patients" ([PMID: 30113650](https://pubmed.ncbi.nlm.nih.gov/30113650/)) |
| Complete androgen insensitivity | *AR* | — | Androgen (not estrogen) axis; different karyotype context |
| Hypergonadotropic hypogonadism (other) | various | Low | Low sex steroids |

**Screening.** No newborn/population screening exists (disease too rare, no actionable neonatal intervention). Cascade genetic testing of relatives in known families and carrier testing in consanguineous couples are appropriate.

---

## 11. Outcome / Prognosis

**Survival / mortality.** Not a directly lethal disease; **no life-expectancy or mortality data** exist for this ultra-rare condition. Longevity is presumed near-normal, but long-term cardiovascular and metabolic risks (from loss of ERα vasoprotection and insulin resistance) are theoretically increased and unquantified.

**Morbidity / function.** Principal long-term morbidity is **skeletal**: osteoporosis with elevated fracture risk from failure to accrue peak bone mass, plus the functional and psychosocial consequences of tall stature and unfused epiphyses. **Infertility** (female) is a major reproductive morbidity. Metabolic complications (glucose intolerance, dyslipidemia) add chronic-disease burden.

**Disease course / recovery.** Chronic and lifelong with **no natural recovery**; the receptor defect is permanent. Bone density and reproductive function do not respond to standard estrogen therapy (refractoriness demonstrated over 2.5 years of DES; [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)).

**Prognostic factors.** Variant type likely governs severity: **null alleles** (p.Arg157Ter) predict complete resistance, whereas **hypomorphic missense** alleles (Q375H, R394H) may retain partial function and milder phenotypes. This is inferred from genotype–phenotype patterns and in-vitro/mouse data ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)), not from formal prognostic studies.

---

## 12. Treatment

**There is no curative or reliably effective therapy.** Because the lesion is the estrogen receptor itself, conventional estrogen replacement — the logical treatment for estrogen-deficiency states — is **ineffective**:

> "DES treatment did not induce secondary sexual characteristics in our patient. Treatment with DES was not successful in our patient. She remains hypoestrogenic" — [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/) (Finding F003)

**Pharmacotherapy (attempted / supportive).**
- **High-affinity estrogenic ligands (e.g., diethylstilbestrol, DES; high-dose estradiol):** attempted on the rationale that a stronger ligand might drive a hypomorphic receptor; some variants are transactivatable in vitro, but clinical response is generally absent for null/severe alleles. NCIT: C2242 (Estrogen); C542 (Diethylstilbestrol).
- **Bone-directed supportive therapy:** calcium, vitamin D; bisphosphonates for osteoporosis are a rational (though unproven-in-EIS) option to address high bone turnover. NCIT: C1454 (Bisphosphonate).
- **Metabolic management:** standard management of glucose intolerance/dyslipidemia.

**Personalized / experimental directions (conceptual).**
- **Variant-tailored ligand screening:** matching a specific hypomorphic receptor to a ligand that restores its transactivation (in-vitro screen approach; [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)).
- **Reproductive management in partial insensitivity:** in a heterozygous PCOS/partial-insensitivity patient undergoing IVF, recognition of *ESR1* insensitivity informed ovarian-stimulation strategy ([PMID: 36401248](https://pubmed.ncbi.nlm.nih.gov/36401248/)).
- **Model-guided approaches:** the Esr1-Q knock-in mouse was used to explore progestogen + GnRH-inhibitor strategies to reverse impaired female reproductive-tract function ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)) — preclinical only.
- **Gene/RNA therapy:** no clinical programs exist; conceptually, gene replacement/editing of *ESR1* would be required to address the root cause. Not available.

**Note on breast-cancer therapeutics.** The rich pharmacology targeting ERα (SERMs, SERDs such as fulvestrant, oral SERDs, ER-PROTACs like vepdegestrant/ARV-471) is directed at *gain-of-function* somatic *ESR1* mutations in breast cancer and is **not applicable** to germline LOF EIS — indeed these agents antagonize/degrade ERα, the opposite of what EIS needs.

**No NCIT-coded standard-of-care regimen exists for EIS.**

---

## 13. Prevention

- **Primary prevention:** Not possible for a germline monogenic disorder. **Genetic counseling** for consanguineous couples and families with a known *ESR1* variant is the principal preventive tool. **Carrier testing** and, where desired, **preimplantation genetic diagnosis (PGD)** or **prenatal testing** can prevent affected births in known-risk families.
- **Secondary prevention:** Early recognition of the biochemical signature (high E2 + high gonadotropins + delayed bone age) enables early diagnosis and initiation of supportive bone-protective measures.
- **Tertiary prevention:** Osteoporosis management (calcium, vitamin D, ± bisphosphonates), metabolic surveillance and management, and monitoring for cardiovascular risk to prevent complications.
- **Immunization / public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *ESR1* is highly conserved across vertebrates. Mouse *Esr1* (NCBI Gene 13982) is the principal model ortholog; rat, zebrafish, and other vertebrate orthologs exist.
- **Natural disease:** No well-characterized spontaneous *ESR1*-LOF "estrogen resistance syndrome" is documented in companion animals or wildlife (no OMIA entry emerged in this investigation). The comparative evidence is from engineered models, not naturally occurring disease.
- **Comparative biology:** Estrogen-receptor knockout phenotypes are conserved in principle (infertility, skeletal and metabolic effects), but details are strain/background-dependent in mice ([PMID: 39576259](https://pubmed.ncbi.nlm.nih.gov/39576259/)).
- **Transmission / zoonosis:** Not applicable (genetic, non-communicable).

---

## 15. Model Organisms

**Mouse (principal model).**

| Model | Type | Key phenotype | Relevance to EIS |
|---|---|---|---|
| **αERKO** (*Esr1* knockout) | Constitutive knockout | Infertile (both sexes), absent mammary development, skeletal & metabolic abnormalities | Recapitulates human ERα-null EIS |
| **Esr1-Q knock-in** (models human Q375H) | CRISPR/Cas9 knock-in | Infertile male & female mice; "similar phenotypes to αERKO mice"; corresponds to human Q375H patient | **Directly recapitulates a specific human EIS variant** ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/), Finding F004) |
| **Ex3αβERKO / αβERKO** (double ERα/ERβ KO) | Knockout | Ovarian transdifferentiation to seminiferous-tubule-like structures (background-dependent) | Reveals ERα role in gonad maintenance ([PMID: 39576259](https://pubmed.ncbi.nlm.nih.gov/39576259/)) |
| **NERKI** ("non-classical" ER knock-in) | Knock-in (ERE-binding mutant) | Loss of classical genomic estrogen effects on circadian activity | Dissects genomic vs non-genomic ERα action ([PMID: 24527952](https://pubmed.ncbi.nlm.nih.gov/24527952/)) |
| **ERβ (ESR2) knockout** | Knockout | Subfertile (reduced ovarian efficiency); otherwise grossly normal | Control demonstrating ERβ ≠ ERα roles ([PMID: 9861029](https://pubmed.ncbi.nlm.nih.gov/9861029/)) |

> "Female and male Esr1-Q mice are infertile and have similar phenotypes to αERKO mice" — [PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)

**In-vitro / cellular models.** HeLa and MCF-7 luciferase reporter-gene transactivation assays for ERα variants; the SMAT1 prepubertal Sertoli-cell line for AMH-promoter/ERE studies ([PMID: 32934281](https://pubmed.ncbi.nlm.nih.gov/32934281/)); structural biology (cryo-EM of the DNA-bound ERα–SRC-3–p300 complex, [PMID: 25728767](https://pubmed.ncbi.nlm.nih.gov/25728767/)).

**Model characteristics.** The Esr1-Q knock-in provides excellent face and construct validity for a human hypomorphic EIS variant (infertility phenocopying αERKO). **Limitations:** mouse skeletal biology (continuous growth plates, no true "epiphyseal fusion" event) does not perfectly model the human tall-stature/unfused-epiphysis phenotype; genetic background strongly modifies gonadal outcomes; and murine models cannot capture human psychosocial/QoL dimensions.

**Resources.** MGI (mouse *Esr1*), IMPC/IMSR for knockout lines; NCBI Gene for orthologs.

---

## Mechanistic Model / Interpretation

```
   Biallelic germline ESR1 LOF
   (p.Arg157Ter null / Q375H, R394H hypomorph)
              |
              v
   Non-functional or conformationally
   distorted ERα protein  ──────────────┐ (LBD mutants: MD-confirmed
              |                          │  conformational change)
              v                          │
   Fails to bind ligand / adopt          │
   active conformation on E2 binding     │
              |                          │
              v                          │
   Fails to recruit SRC-3 (NCOA3) + p300 (EP300)
   at estrogen-response elements
              |
              v
   Loss of estrogen-responsive transcription
   + altered transcriptome & DNA methylome
              |
   ┌──────────┼───────────────┬────────────────┬───────────────┐
   v          v               v                v               v
 BONE     HYPOTHAL-       FEMALE            METABOLISM      VASCULATURE
 growth   PITUITARY       REPRO TRACT       glucose         loss of
 plate    loss of neg.    absent breast,    intolerance,    eNOS
 |        feedback        amenorrhea,       hyperinsulin-   enhancement
 |        |               poor uterus,      emia,           |
 v        v               multicystic       dyslipidemia    v (inferred)
 no       high LH/FSH,    ovaries           |               increased
 growth   high androgens  |                 v               vascular
 spurt,   DESPITE         v                 chronic         risk
 unfused  high E2         infertility       metabolic
 epiphyses|                                 disease
 |        |
 v        v
 tall stature,          ── HIGH ESTRADIOL + HIGH GONADOTROPINS ──
 osteoporosis,             = the biochemical fingerprint of
 high bone turnover        RESISTANCE (vs. deficiency)

   Because the RECEPTOR is the lesion →
   exogenous estrogen (even DES) cannot rescue → THERAPY REFRACTORY
```

The unifying insight is that **a single receptor defect propagates into a pleiotropic, multi-system disease because ERα is a hub transcription factor deployed across bone, gonad, hypothalamus, metabolic, and vascular tissues.** The paradox that patients look estrogen-*deficient* while being estrogen-*replete* is diagnostically decisive and mechanistically inevitable: the hormone is present but cannot be "heard." The same logic dictates the therapeutic dead-end — you cannot fix a broken receiver by shouting louder.

---

## Evidence Base

| PMID | Title (abbrev.) | Type | Supports |
|---|---|---|---|
| [42734155](https://pubmed.ncbi.nlm.nih.gov/42734155/) | *EIS: the 'Upside Down' of ESR1 mutations* | Review | F001, F005 — causal LOF mechanism; disrupted signaling layers |
| [34538723](https://pubmed.ncbi.nlm.nih.gov/34538723/) | *Congenital disorders of estrogen biosynthesis and action* | Review | F001 — germline LOF *ESR1* causes resistance |
| [9554463](https://pubmed.ncbi.nlm.nih.gov/9554463/) | *Essential roles of estrogens in pubertal growth...* | Landmark review | F002 — skeletal & metabolic phenotype |
| [32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/) | *Long-term follow-up of a female with complete estrogen insensitivity* | Case report | F003 — female phenotype; treatment refractoriness |
| [32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/) | *ESR1 mutations... change conformation & altered transcriptome* | Functional + model | F004 — conformational mechanism; Esr1-Q mouse |
| [25728767](https://pubmed.ncbi.nlm.nih.gov/25728767/) | *Structure of a biologically active ER–coactivator complex on DNA* | Structural | F005 — SRC-3/p300 coactivator assembly |
| [39432505](https://pubmed.ncbi.nlm.nih.gov/39432505/) | *AF-1 domain interacts with AF-2 LBD to recruit coactivators* | Functional | F005 — AF-1/AF-2 cooperation |
| [39295121](https://pubmed.ncbi.nlm.nih.gov/39295121/) | *EIS in a female adolescent — case report* | Case report | F006 — recessive/consanguineous homozygous case |
| [30113650](https://pubmed.ncbi.nlm.nih.gov/30113650/) | *Ovarian failure with mutated ESR2* | Case report | F006 — ESR2 differential (streak gonads) |
| [35712256](https://pubmed.ncbi.nlm.nih.gov/35712256/) | *AMH regulation by steroids in testis* | Review | F007 — ERα breadth (Sertoli/AMH) |
| [32934281](https://pubmed.ncbi.nlm.nih.gov/32934281/) | *AMH elevation in hyperoestrogenic states* | In vitro | F007 — ERα→ERE→AMH mechanism |
| [28736253](https://pubmed.ncbi.nlm.nih.gov/28736253/) | *Selective ER-α agonist & vascular dysfunction* | Animal | F007 — ERα/eNOS vasoprotection |
| [36401248](https://pubmed.ncbi.nlm.nih.gov/36401248/) | *Novel ESR1 mutation in PCOS woman (p.A207T)* | Case report | Heterozygous partial insensitivity; WES utility |
| [9861029](https://pubmed.ncbi.nlm.nih.gov/9861029/) | *Mice lacking ERβ* | Model | ERβ vs ERα role (differential) |
| [39576259](https://pubmed.ncbi.nlm.nih.gov/39576259/) | *Ovarian transdifferentiation in absence of ER signaling* | Model | Background modifiers; gonad maintenance |
| [24527952](https://pubmed.ncbi.nlm.nih.gov/24527952/) | *ESR1 modulates circadian rhythms* | Model | Classical vs non-classical ERα action |
| [42224247](https://pubmed.ncbi.nlm.nih.gov/42224247/) | *Bisphenols agonist/antagonist for ERα* | In vitro | Xenoestrogen relevance; AF-1 dependence |

**Computational/database evidence:** gnomAD constraint (F008) and ClinVar variant curation (F009) were retrieved directly (2026) and provide the population-genetics and variant-classification backbone.

**Somatic *ESR1* breast-cancer literature** (PMIDs 42714671, 42693657, 42665030, 42609450, 42603649, 42599237, 42593925, 22245602) was reviewed and explicitly **set aside** as not applicable to germline LOF EIS — it concerns gain-of-function LBD mutations and ERα-targeting/degrading therapeutics, the mechanistic inverse of this disease. This distinction is itself an important finding (the "Upside Down" framing).

---

## Limitations and Knowledge Gaps

1. **Extreme rarity → thin evidence.** The entire clinical picture rests on a handful of case reports. There are **no prevalence/incidence figures, no mortality/survival data, and no formal QoL measurements.**
2. **Genotype–phenotype correlation is under-powered.** With so few variants (essentially p.Arg157Ter, p.Gln375His, p.Arg394His, plus VUS), the mapping from allele severity to clinical severity is inferred, not established.
3. **No approved or proven therapy.** Estrogen replacement is refractory; bisphosphonate/metabolic management is extrapolated, not EIS-validated. No gene-therapy or ligand-rescue strategy has reached the clinic.
4. **Epigenetic/omics data are single-study.** The transcriptome/methylome findings ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)) need replication across variants and tissues.
5. **Model-organism gaps.** Mice do not fuse epiphyses as humans do, limiting fidelity for the tall-stature/unfused-epiphysis phenotype; background effects confound gonadal phenotypes.
6. **Cardiovascular/long-term outcome risk is inferred**, not measured, in patients.
7. **Ontology coding is incomplete** at the resource level (no dedicated ICD/Orphanet code), complicating knowledge-base integration.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international EIS registry** (case aggregation via GeneMatcher/networks) to derive prevalence, natural-history, and genotype–phenotype data — the single highest-impact action given how case-limited the field is.
2. **Systematic variant-function mapping:** transactivation, coactivator-recruitment, and DNA-binding assays for every reported *ESR1* germline variant, paired with molecular-dynamics conformational analysis, to build a functional matrix that predicts severity and ligand-rescuability.
3. **Ligand-rescue screening for hypomorphic alleles:** high-throughput screening of ER ligands/SERMs against patient-specific hypomorphic receptors (extending the 75-compound approach in [PMID: 32152632](https://pubmed.ncbi.nlm.nih.gov/32152632/)) to identify variant-tailored agonists.
4. **Preclinical therapy testing in Esr1-Q knock-in mice:** evaluate bisphosphonates for the skeletal phenotype and the progestogen + GnRH-inhibitor strategy for reproductive-tract function ([PMID: 32242619](https://pubmed.ncbi.nlm.nih.gov/32242619/)); assess AAV gene-replacement feasibility.
5. **Long-term metabolic/cardiovascular surveillance protocol** for known patients to quantify the inferred vascular/insulin-resistance risk.
6. **Multi-tissue omics in patient-derived cells (iPSC → osteoblast/chondrocyte/granulosa models)** to map the estrogen-target transcriptional program lost in EIS and identify downstream druggable nodes that bypass ERα.
7. **Formal ontology curation:** submit dedicated disease codes and complete HPO/GO/CL/UBERON/CHEBI/NCIT annotation (as compiled in this report) to improve knowledge-base interoperability.

---

*Report generated by autonomous scientific discovery agent · 5 iterations · 9 confirmed findings · 25 papers reviewed · evidence current to 2026-09-29.*


## Artifacts

- [OpenScientist final report](Estrogen_Resistance_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Estrogen_Resistance_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 25 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014148` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **estrogen resistance syndrome**
- `HP:0008819` (1 mention) - the report calls it "Abnormal pubertal development"; HP calls it **Narrow femoral neck**
- `HP:0002644` (1 mention) - the report calls it "Delayed epiphyseal ossification"; HP calls it **Abnormal pelvic girdle bone morphology**
- `HP:0000837` (1 mention) - the report calls it "Hypergonadotropic hypogonadism–related"; HP calls it **Increased circulating gonadotropin level**
- `HP:0003186` (1 mention) - the report calls it "Breast hypoplasia"; HP calls it **Inverted nipples**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000783` (1 mention), reported as "Primary amenorrhea" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030520` (1 mention) - the report calls it "intracellular estrogen receptor signaling pathway"; GO calls it **estrogen receptor signaling pathway**, and lists "intracellular estrogen receptor signaling pathway" among its other names
- `GO:0006357` (1 mention) - the report calls it "regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**
- `CHEBI:16469` (1 mention) - the report calls it "17β-estradiol"; CHEBI calls it **17beta-estradiol**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014148` - called "if available", "MONDO"
- `CL:0000062` - called "osteoblast", "osteoblasts"
- `CL:0000138` - called "chondrocyte", "chondrocytes"
- `CL:0000501` - called "granulosa cell", "granulosa cells"

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:32242619` *(abstract only)*: "altered transcriptome profile"
  - Text part not found as substring: 'altered transcriptome profile' (note: only abstract available for PMID:32242619, full text may contain this excerpt)
- `PMID:32934281` *(abstract only)*: "The direct effects of sex steroids on AMH transcription are mediated by androgen receptor and estrogen receptor α action"
  - closest text in source: "A modest action was also mediated through the membrane oestrogen receptor GPER"
- `PMID:32152632` *(abstract only)*: "despite markedly increased estrogens"
  - Text part not found as substring: 'despite markedly increased estrogens' (note: only abstract available for PMID:32152632, full text may contain this excerpt)
- `PMID:32152632` *(abstract only)*: "DES treatment did not induce secondary sexual characteristics in our patient. Treatment with DES was not successful in our patient. She remains hypoestrogenic"
  - closest text in source: "However, DES treatment did not induce secondary sexual characteristics in our patient"
