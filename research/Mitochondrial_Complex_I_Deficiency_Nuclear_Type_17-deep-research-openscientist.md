---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T15:39:43.329371'
end_time: '2026-09-25T16:05:45.084227'
duration_seconds: 1561.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 17
  mondo_id: MONDO:0032622
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_17-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_17-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 17
- **MONDO ID:** MONDO:0032622 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 17** covering all of the
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

# Mitochondrial Complex I Deficiency, Nuclear Type 17 (MC1DN17): Comprehensive Disease Report

**Disease:** Mitochondrial Complex I Deficiency, Nuclear Type 17
**MONDO ID:** MONDO:0032622 · **OMIM:** #618239 · **Causal gene:** *NDUFAF6* (C8orf38)
**Category:** Mendelian (autosomal recessive)

---

## Summary

**Mitochondrial Complex I Deficiency, Nuclear Type 17 (MC1DN17)** is a rare autosomal-recessive mitochondrial disorder caused by **biallelic loss-of-function or hypomorphic variants in *NDUFAF6*** (formerly *C8orf38*), a nuclear-encoded mitochondrial assembly factor required for the biogenesis and stabilization of the mtDNA-encoded **ND1 subunit** of respiratory-chain **complex I** (NADH:ubiquinone oxidoreductase). Loss of NDUFAF6 function produces an **isolated complex I deficiency**: mature ~1 MDa complex I is nearly absent, oxidative phosphorylation is impaired, and cells experience an elevated NADH/NAD⁺ ratio, lactate accumulation, and oxidative stress. These bioenergetic defects preferentially injure the metabolically vulnerable **basal ganglia**, producing the disease's characteristic clinical picture: **childhood-onset Leigh syndrome / bilateral striatal (putaminal) necrosis with prominent, progressive dystonia**.

The disease sits within a broader pleiotropic *NDUFAF6* phenotypic spectrum. The classic neurological presentation (MC1DN17/Leigh syndrome) arises from combinations of frameshift, nonsense, splice, and hypomorphic missense alleles. A distinct allelic disorder — **Acadian variant Fanconi renotubular syndrome (FRTS5)** — is caused by specific deep-intronic splice variants (notably c.298-768T>C) that impair the mitochondrial NDUFAF6 isoform, producing proximal renal-tubular dysfunction, progressive chronic kidney disease, and pulmonary interstitial fibrosis in the Nova Scotia Acadian founder population. This gene-level pleiotropy demonstrates that the same complex I assembly defect can manifest as either an encephalopathy or a renal/pulmonary disease depending on the allele's residual splicing output and the affected tissue.

There is **no curative therapy**. Management is supportive: empiric mitochondrial cofactor/antioxidant regimens (riboflavin, CoQ10, thiamine, etc.), avoidance of mitochondrial toxins (valproate, aminoglycosides), and aggressive management of intercurrent illness (viral infections commonly trigger decompensation). Prognosis is one of chronic, progressive extrapyramidal disability, but among Leigh syndrome genotypes, NDUFAF6-related disease is notable for **comparatively favorable survival**. Prevention is reproductive — genetic counseling, carrier/cascade testing, and prenatal/preimplantation diagnosis — supplemented by targeted population carrier screening in the Acadian founder community. This report synthesizes 13 confirmed findings across 24 reviewed papers into a complete disease knowledge-base entry.

---

## 1. Disease Information

**Overview.** MC1DN17 is a Mendelian mitochondrial encephalopathy belonging to the family of nuclear-gene isolated complex I deficiencies. It is one of the genetically defined subtypes of **Leigh syndrome (subacute necrotizing encephalomyelopathy)**, the most common pediatric mitochondrial disorder. The disease is defined at the molecular level by biallelic pathogenic variants in *NDUFAF6*, and at the biochemical level by isolated deficiency of respiratory-chain complex I.

**Key identifiers (cross-referenced via OLS4/NCBI):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032622 ("mitochondrial complex I deficiency, nuclear type 17") |
| OMIM | #618239 |
| DOID | DOID:0112078 |
| GARD | 0018372 |
| UMLS | C4748786 |
| MedGen | C4748786 |
| Causal gene | *NDUFAF6* (NCBI Gene 137682; locus 8q22.1) |

**Synonyms / alternative names:** MC1DN17; mitochondrial complex I deficiency nuclear type 17; NDUFAF6-related complex I deficiency; NDUFAF6-related Leigh syndrome; isolated bilateral striatal necrosis due to NDUFAF6. Gene aliases: *C8orf38*, *FRTS5*, *lncREST*. The allelic renal disorder is **Acadian variant Fanconi renotubular syndrome (FRTS5)**.

**Data provenance.** This entry is derived from **aggregated disease-level resources** (OMIM, MONDO, HPO annotations) and from **individual-patient primary literature** (case reports and case series), not from EHR-derived population data. Reported patient numbers are small (single-digit to low-double-digit cohorts), reflecting the disease's rarity.

**Evidence:** Ontology cross-references (OLS4/NCBI). Functional causation established in patient fibroblasts by [PMID: 22019594](https://pubmed.ncbi.nlm.nih.gov/22019594/): *"Analysis of mitochondria from fibroblasts of a patient harboring a C8orf38 mutation showed almost undetectable levels of steady-state complex I and defective biogenesis of the mtDNA-encoded subunit ND1."*

---

## 2. Etiology

**Disease causal factors.** MC1DN17 is a purely **genetic (Mendelian) disorder**. The primary cause is **biallelic pathogenic variation in *NDUFAF6***. *NDUFAF6* (NCBI Gene 137682) encodes a mitochondria-targeted 333-amino-acid protein of the **squalene/phytoene synthase family** that functions as a complex I assembly factor required for biogenesis of the ND1 subunit ([PMID: 28476317](https://pubmed.ncbi.nlm.nih.gov/28476317/): *"Human NDUFAF6 is a mitochondria-targeted 333-amino acid protein belonging to the family of squalene and phytoene synthases."*).

**Genetic risk factors.** The causal variants are the risk. Because the disorder is autosomal recessive, **carrier parents** and **consanguinity** are the principal risk determinants, and **founder effects** concentrate specific alleles in particular populations (e.g., the Acadian c.298-768T>C allele). No independent susceptibility loci or modifier genes with established effect on the neurological phenotype have been reported, though the residual splicing output of hypomorphic/deep-intronic alleles modulates disease severity and tissue tropism.

**Environmental risk factors / triggers.** There are no environmental *causes*. However, **intercurrent viral infections** and **catabolic stress (fasting, febrile illness)** act as **triggers of acute metabolic decompensation** in Leigh syndrome ([PMID: 33097395](https://pubmed.ncbi.nlm.nih.gov/33097395/): *"Acute decompensation is often triggered by viral infections."*). Mitochondrial-toxic drugs (valproate, aminoglycosides, high-dose acetaminophen) can worsen disease.

**Protective factors.** No genetic protective variants or protective environmental exposures are established. Indirectly, alleles that preserve partial NDUFAF6 isoform expression yield milder, later-onset disease.

**Gene–environment interactions.** The core interaction is between the underlying complex I deficiency (a fixed genetic ceiling on energy production) and **acute metabolic demand**: infection/fever/fasting raise ATP demand beyond the cell's compromised supply, precipitating stepwise neurological deterioration.

---

## 3. Phenotypes

MC1DN17 is a **neurological / movement-disorder-dominant** phenotype centered on basal ganglia degeneration, with metabolic (lactic acidosis) laboratory abnormalities. The curated HPO profile (OMIM:618239) is summarized below.

| Phenotype | HPO term | Type | Notes |
|---|---|---|---|
| Developmental regression | HP:0002376 | Sign | Insidious, early childhood |
| Global developmental delay | HP:0001263 | Sign | |
| Dystonia | HP:0001332 | Sign | **Prominent, defining feature** |
| Generalized dystonia | HP:0007325 | Sign | Progression from focal/gait dystonia |
| Basal ganglia necrosis | HP:0012128 | Imaging/path | Bilateral striatal (putaminal) necrosis |
| Ataxia | HP:0001251 | Sign | |
| Dysarthria | HP:0001260 | Sign | |
| Seizure / focal motor seizure | HP:0001250 / HP:0011153 | Sign | |
| Gait disturbance | HP:0001288 | Sign | Often the presenting complaint |
| Elevated brain lactate (MRS) | HP:0012707 | Lab/imaging | Lactate doublet over lesions |
| Elevated brain choline (MRS) | HP:0012706 | Lab/imaging | |
| Hypotonia | HP:0001252 | Sign | |
| Muscle weakness | HP:0001324 | Sign | |
| Rigidity | HP:0002063 | Sign | Extrapyramidal |
| Skeletal muscle atrophy | HP:0003202 | Sign | |
| Increased circulating lactate | HP:0002151 | Lab | |
| Lactic acidosis | HP:0003128 | Lab | |
| Decreased complex I activity | HP:0011923 | Lab | May be normal in mild cases |
| Scoliosis / pes planus | HP:0002650 / HP:0001763 | Physical | |
| High narrow palate / thick hair | HP:0002705 / HP:0100874 | Physical | |

**Phenotype characteristics.**
- **Age of onset:** Infantile to childhood onset (HP:0003593 infantile onset; HP:0011463 childhood onset). Gait dystonia typically begins in infancy; rare **adult/mild presentations** are documented.
- **Severity:** Variable — from severe childhood Leigh syndrome to mild adult disease with near-normal complex I activity.
- **Progression:** Progressive, with **episodic decompensations** triggered by viral illness superimposed on a chronic downhill course.
- **Frequency among affected:** Dystonia and basal ganglia degeneration are near-universal in the classic phenotype; the review of 14 NDUFAF6 patients described a "consistent phenotype."

**Quality-of-life impact.** Progressive generalized dystonia, dysarthria, and gait loss impose severe motor disability, loss of independent ambulation and communication, and dependence for daily activities. Disease-specific formal QoL instruments (EQ-5D/SF-36/PROMIS) have not been applied to this ultra-rare cohort.

**Evidence:** [PMID: 30642748](https://pubmed.ncbi.nlm.nih.gov/30642748/): *"Three siblings developed gait dystonia in infancy followed by rapid progression to generalised dystonia and psychomotor regression"* and *"A literature review of 14 NDUFAF6 patients showed a consistent phenotype of an early childhood insidious onset neurological regression with prominent dystonia associated with basal ganglia degeneration and long survival."*

---

## 4. Genetic / Molecular Information

**Causal gene.** *NDUFAF6* (HGNC-approved symbol *NDUFAF6*; NCBI Gene 137682; locus **8q22.1**; aliases *C8orf38*, *FRTS5*, *lncREST*). Encodes a 333-aa mitochondria-targeted assembly factor of the squalene/phytoene synthase family.

**Pathogenic variant spectrum (ClinVar, NM_152416.4).** 413 records, with **121 classified Pathogenic/Likely-pathogenic**, spanning multiple variant classes:

| Variant class | Representative alleles |
|---|---|
| Frameshift | c.239del (p.Pro80fs); c.33dup (p.Pro12fs); c.110_111del (p.Pro37fs); c.322del; c.838_839del; c.485_492dup; c.554_558delTTCTT (p.Tyr187AsnfsTer65) |
| Nonsense | c.727C>T (p.Gln243Ter); c.648C>A (p.Cys216Ter); c.187G>T (p.Glu63Ter) |
| Canonical splice | c.581-1G>A; c.198-2A>C |
| Multi-exon deletion | c.478-972_580+533del |
| Recurrent missense (hypomorphic) | c.371T>C (**p.Ile124Thr**, rs201732170); c.532G>C (**p.Ala178Pro**, rs201088736) |
| Deep-intronic splice (founder/pathogenic) | c.298-768T>C (**Acadian**, rs575462405); c.420+784C>T (Italian) |

**Allele frequencies (gnomAD v4, all rare — consistent with AR):**
- p.Ile124Thr (c.371T>C): AF = 3.9×10⁻⁵ (AC = 57)
- p.Ala178Pro (c.532G>C): AF = 1.05×10⁻⁴ (AC = 154)

**Variant classification & type.** Per ACMG/AMP, pathogenic/likely-pathogenic alleles include null (frameshift/nonsense/canonical-splice/multi-exon deletion) plus recurrent hypomorphic missense and deep-intronic splice-altering variants. Patients are typically **compound heterozygous** (e.g., c.554_558delTTCTT + c.371T>C; c.532G>C + c.420+784C>T).

**Somatic vs germline.** All variants are **germline**. No somatic/cancer relevance.

**Functional consequence.** **Loss of function** — absent or reduced NDUFAF6 protein and impaired complex I assembly — confirmed by cDNA complementation rescue ([PMID: 22019594](https://pubmed.ncbi.nlm.nih.gov/22019594/): *"Complementation with wild-type C8orf38 restored the levels of both ND1 and complex I, confirming the C8orf38 mutation as the cause of the complex I defect"*; [PMID: 29531337](https://pubmed.ncbi.nlm.nih.gov/29531337/): *"we found the same compound heterozygous missense (c.532G>C:p.A178P) and deep intronic (c.420+784C>T) variants in NDUFAF6"*).

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes, disease-specific epigenetic marks, or large chromosomal abnormalities. Disease is monogenic single-gene; large deletions within *NDUFAF6* itself (e.g., c.478-972_580+533del) are reported, but no aneuploidy/translocation mechanism applies.

---

## 5. Environmental Information

MC1DN17 has **no primary environmental etiology**. Relevant non-genetic factors are **triggers and aggravators** rather than causes:

- **Metabolic stressors:** viral infections, fever, fasting/catabolism precipitate acute decompensation ([PMID: 33097395](https://pubmed.ncbi.nlm.nih.gov/33097395/)).
- **Mitochondrial-toxic exposures:** valproate, aminoglycosides, and high-dose acetaminophen should be avoided ([PMID: 33105273](https://pubmed.ncbi.nlm.nih.gov/33105273/)).
- **Lifestyle factors:** not applicable as causes; supportive nutrition and avoidance of catabolic stress are protective management.
- **Infectious agents:** no pathogen causes the disease; infections act only as decompensation triggers.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *NDUFAF6* loss-of-function/hypomorphic variants** reduce or abolish the functional mitochondrial NDUFAF6 isoform [human genetics; PMID 22019594, 30642748, 27466185].
2. → Loss of NDUFAF6 assembly-factor activity **leads to** defective biogenesis/stabilization of the **mtDNA-encoded ND1 subunit** at a convergence point in complex I assembly (membrane-arm proximal / Q module) [in vitro; PMID 22019594].
3. → **Results in** failure to build late-stage assembly intermediates and **near-absent mature ~1 MDa complex I** [in vitro; PMID 22019594].
4. → Complex I deficiency **impairs NADH oxidation and proton pumping**, lowering OXPHOS/ATP output and raising the NADH/NAD⁺ ratio → **lactate accumulation / lactic acidosis** (MRS lactate peak) [human/biochemical; PMID 30642748; HP:0003128].
5. → *(inferred branch)* Electron-transfer blockade **promotes reactive oxygen species and oxidative stress**, sensitizing high-energy-demand neurons [inferred from CI biology; PMID 28476317].
6. → Chronic energy failure and oxidative injury in the metabolically vulnerable **striatum results in bilateral symmetric putaminal necrosis** [human imaging/neuropathology; PMID 30642748].
7. → Striatal degeneration **leads to** the clinical extrapyramidal syndrome: **dystonia, rigidity, developmental regression (Leigh syndrome)** [human clinical; PMID 30642748].

**Branch (renal/pulmonary, FRTS5):** deep-intronic splice alleles that preserve partial isoform expression instead cause **proximal-tubule and lung mitochondrial dysfunction → Fanconi renotubular syndrome / interstitial fibrosis** [human; PMID 27466185].

```
                          NDUFAF6 biallelic LoF/hypomorphic variants
                                          │
                          ┌───────────────┴────────────────┐
             (null / severe alleles)              (deep-intronic splice, partial isoform)
                          │                                 │
           failed ND1 biogenesis                 tissue-specific isoform loss
                          │                        (kidney proximal tubule, lung)
        near-absent mature Complex I (~1 MDa)                │
                          │                        defective respiration / CI biogenesis
        ↓OXPHOS/ATP, ↑NADH/NAD⁺, lactic acidosis             │
                          │                        FRTS5: Fanconi renotubular
        ↑ROS / oxidative stress (inferred)           syndrome, CKD, pulmonary fibrosis
                          │
        striatal (putaminal) necrosis
                          │
        dystonia, rigidity, regression (Leigh syndrome)
```

### Detail by category

- **Molecular pathways:** OXPHOS / mitochondrial respiratory chain; NADH:ubiquinone oxidoreductase (complex I) assembly. GO: mitochondrial respiratory chain complex I assembly (GO:0032981); mitochondrial electron transport, NADH to ubiquinone (GO:0006120); ATP synthesis coupled electron transport (GO:0042775).
- **Cellular processes:** bioenergetic failure, oxidative stress, and neuronal death in the basal ganglia; upstream = assembly failure; downstream = neurodegeneration.
- **Protein dysfunction:** loss of function of the NDUFAF6 assembly factor (absent/reduced protein) → failure to chaperone/stabilize ND1; not aggregation or gain-of-function.
- **Metabolic changes:** impaired ATP generation, elevated lactate/pyruvate, elevated NADH/NAD⁺. CHEBI: lactate (CHEBI:24996), NADH (CHEBI:57945), NAD⁺ (CHEBI:57540), ATP (CHEBI:30616), FMN/FAD (complex I cofactors).
- **Immune involvement:** none primary; infections are decompensation triggers.
- **Tissue damage mechanism:** energy-deficit/oxidative injury → cytotoxic edema → symmetric necrosis of the putamen/striatum with cavitation and lenticulostriate vasculopathy.
- **Biochemical abnormality:** isolated complex I enzyme deficiency (HP:0011923).
- **Cell types / GO cellular component:** high-energy-demand CNS neurons, especially **striatal medium spiny neurons** (CL:0002613 striatal neuron; CL:0000540 neuron). Compartment: **mitochondrion (GO:0005739)**, mitochondrial inner membrane (GO:0005743), respiratory chain complex I (GO:0045271).

**Evidence:** [PMID: 22019594](https://pubmed.ncbi.nlm.nih.gov/22019594/): *"In the absence of ND1 in patient cells, early- and mid-stage intermediate complexes were still formed; however, assembly of late-stage intermediates was impaired, indicating a convergence point in the assembly process."* [PMID: 27466185](https://pubmed.ncbi.nlm.nih.gov/27466185/): *"affected tissues had defects in mitochondrial respiration and complex I biogenesis."*

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary organ:** brain — specifically the **basal ganglia / striatum (putamen)**; also brainstem/thalamus in Leigh-spectrum disease. Body system: **central nervous system**.
- **Secondary involvement:** skeletal muscle (weakness, atrophy, hypotonia); skeletal system (scoliosis, pes planus).
- **Allelic branch (FRTS5):** **kidney** (proximal renal tubule) and **lung** (interstitial fibrosis).

**Tissue and cell level.** Nervous tissue — **striatal neurons** (CL:0002613), particularly medium spiny neurons, with astrocytic/vascular reaction (lenticulostriate vasculopathy). In FRTS5, renal **proximal tubule epithelial cells** (CL:1000838) and pulmonary interstitial cells.

**Subcellular level.** **Mitochondrion (GO:0005739)**; mitochondrial inner membrane (GO:0005743); mitochondrial respiratory chain complex I (GO:0045271). NDUFAF6 is a mitochondria-targeted peripheral membrane protein.

**Localization (UBERON).** Putamen (UBERON:0001874); corpus striatum (UBERON:0002435); basal ganglia (UBERON:0002420); brain (UBERON:0000955); kidney (UBERON:0002113); lung (UBERON:0002048). **Lateralization: bilateral and symmetric** striatal lesions.

**Evidence:** [PMID: 30642748](https://pubmed.ncbi.nlm.nih.gov/30642748/) documents symmetric bilateral putaminal necrosis; [PMID: 28476317](https://pubmed.ncbi.nlm.nih.gov/28476317/) establishes mitochondrial localization.

---

## 8. Temporal Development

**Onset.** Typically **infantile-to-childhood** (HP:0003593 infantile onset; HP:0011463 childhood onset). Gait dystonia usually begins in infancy; onset pattern is **insidious/subacute**. Rare **adult-onset/mild** presentations exist ([PMID: 33097395](https://pubmed.ncbi.nlm.nih.gov/33097395/)).

**Progression.** Course is **chronic-progressive** with superimposed **episodic decompensations** (often viral-triggered). Gait dystonia → generalized dystonia → psychomotor regression, with MRI evolution of putaminal lesions from T2/FLAIR hyperintensity to **cavitation and volume loss**. Progression rate is variable — rapid in classic infantile cases, slow in mild/adult cases.

**Disease stages:** early (focal/gait dystonia, developmental plateau) → intermediate (generalized dystonia, regression, cavitating striatal necrosis) → advanced (fixed severe extrapyramidal disability, dysarthria, loss of ambulation). Duration is **chronic and lifelong**.

**Patterns.** No spontaneous remission; **critical periods** correspond to intercurrent illnesses (windows of vulnerability) — aggressive supportive care during these windows is the main opportunity for intervention.

**Evidence:** [PMID: 30642748](https://pubmed.ncbi.nlm.nih.gov/30642748/); [PMID: 33097395](https://pubmed.ncbi.nlm.nih.gov/33097395/).

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal recessive** (HP:0000007; OMIM #618239). Patients are homozygous or compound heterozygous. **No sex predilection** (male:female ≈ 1:1). **Penetrance** appears high for biallelic null genotypes; **expressivity is variable** (severity depends on residual isoform output). No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism not specifically reported.

**Founder effect & consanguinity.** A documented **founder effect** exists in the **Acadian population of Nova Scotia, Canada** for the c.298-768T>C deep-intronic allele (FRTS5). Consanguinity increases homozygosity risk generally.

**Carrier frequency.** Individual pathogenic alleles are rare in gnomAD (p.Ala178Pro AF ≈ 1.05×10⁻⁴; p.Ile124Thr AF ≈ 3.9×10⁻⁵), consistent with a rare AR disorder.

**Epidemiology.** No specific prevalence/incidence figures exist for MC1DN17. Context: isolated complex I deficiency is the most common respiratory-chain defect in children; in a cohort of 109 pediatric isolated CI-deficiency patients, nuclear-gene defects were inferred in **38% (38/101 probands)**, with nuclear-gene onset earlier (median 3 months) than mtDNA (median 12 months). NDUFAF6 is a **rare** cause — single-digit numbers within large Leigh syndrome cohorts (Korea n=64; China n=40; Russia n=219). Overall primary mitochondrial disease affects **≥1 in 4,300**.

| Cohort (PMID) | Country | Total LS/mito patients | NDUFAF6 cases |
|---|---|---|---|
| [32020600](https://pubmed.ncbi.nlm.nih.gov/32020600/) | Korea | 64 | Rare (single-digit) |
| [28639102](https://pubmed.ncbi.nlm.nih.gov/28639102/) | China | 40 | 1 (among nDNA cases) |
| [36675121](https://pubmed.ncbi.nlm.nih.gov/36675121/) | Russia | 219 | Rare nuclear cases |

**Evidence:** [PMID: 21364701](https://pubmed.ncbi.nlm.nih.gov/21364701/): *"Isolated complex I deficiency is the most common enzyme defect in mitochondrial disorders, particularly in children in whom family history is often consistent with sporadic or autosomal recessive inheritance, implicating a nuclear genetic cause."* [PMID: 27466185](https://pubmed.ncbi.nlm.nih.gov/27466185/): *"This condition occurs only in Acadians, a founder population in Nova Scotia, Canada."*

---

## 10. Diagnostics

**Clinical/laboratory tests.**
- **Lactate:** elevated blood and CSF lactate and lactate:pyruvate ratio.
- **Enzymology:** isolated complex I deficiency on spectrophotometric assay of skeletal muscle or fibroblasts — **but complex I activity may be normal in mild cases** (a key diagnostic pitfall).
- **MR spectroscopy:** lactate doublet (HP:0012707) and elevated choline (HP:0012706) over lesions.

**Neuroimaging.** Brain MRI shows **symmetric bilateral T2/FLAIR-hyperintense putaminal/basal ganglia lesions** (isolated bilateral striatal necrosis) progressing to cavitation and volume loss, with lenticulostriate vasculopathy.

**Genetic testing (diagnostic anchor).** **Trio whole-exome or whole-genome sequencing.** Because many pathogenic *NDUFAF6* alleles are **deep-intronic/splice-altering**, **mRNA/cDNA analysis or genome sequencing is often required** to reach a diagnosis. Two probands were diagnosed only after exome + mRNA analysis revealed intronic variants. Functional confirmation via **cDNA complementation** and **BN-PAGE assembly assays** in fibroblasts. *NDUFAF6* is included on mitochondrial-disease / Leigh syndrome NGS gene panels (GTR).

**Omics-based diagnostics.** RNA sequencing / mRNA splicing analysis is central to detecting non-exonic variants. Enzyme/functional assays supplement.

**Clinical criteria & differential diagnosis.** Diagnosis rests on the Leigh syndrome framework (characteristic bilateral symmetric basal ganglia/brainstem lesions + neurodegeneration + lactate elevation) plus molecular confirmation. Differentials: other genetic Leigh syndrome causes (MT-ATP6, MT-ND5/ND3, SURF1, NDUFV1/NDUFS1, ECHS1), biotin-thiamine-responsive basal ganglia disease (treatable — SLC19A3), and other causes of bilateral striatal necrosis.

**Screening.** No newborn screening exists; **cascade/carrier testing** of relatives is available once familial variants are known.

**Evidence:** [PMID: 29531337](https://pubmed.ncbi.nlm.nih.gov/29531337/): *"A detailed analysis of whole-exome sequencing data together with the functional validation based on mRNA analysis may reveal pathogenic variants even in non-exonic regions."* [PMID: 33097395](https://pubmed.ncbi.nlm.nih.gov/33097395/): *"Mitochondrial assays revealed slightly reduced complex I activity in one proband and normal complex I activity in the other."*

---

## 11. Outcome / Prognosis

**Natural history.** Early-childhood insidious neurological regression with prominent dystonia and basal ganglia degeneration, but **"long survival"** across the 14 reviewed NDUFAF6 patients. Among Leigh syndrome genotypes, NDUFAF6 disease is comparatively favorable: in a Japanese Leigh syndrome mortality study (n=166; 24.1% deceased, ~90% of deaths by age 6; neonatal onset uniformly lethal/bedridden), *"Patients with NDUFAF6, ECHS1, and SURF1 deficiency had relatively mild symptoms and better survival."*

**Morbidity & function.** Despite comparatively favorable survival, patients accrue **fixed, severe extrapyramidal disability** — generalized dystonia, rigidity, dysarthria, loss of independent gait. Progressive disability arises from irreversible striatal degeneration.

**Disease course & complications.** Chronic-progressive with **episodic, infection-triggered decompensations** driving stepwise deterioration. The renal/pulmonary (FRTS5) branch causes slowly progressive CKD and pulmonary interstitial fibrosis.

**Prognostic factors.** Earlier (neonatal/infantile) onset and null genotypes → worse prognosis; milder hypomorphic/adult presentations with preserved complex I activity → better outcome. Infection frequency/severity modulates decompensation. Recovery potential is limited once necrosis is established.

**Evidence:** [PMID: 31967322](https://pubmed.ncbi.nlm.nih.gov/31967322/): *"Patients with NDUFAF6, ECHS1, and SURF1 deficiency had relatively mild symptoms and better survival."* [PMID: 33097395](https://pubmed.ncbi.nlm.nih.gov/33097395/): *"Acute decompensation is often triggered by viral infections."*

---

## 12. Treatment

**No curative therapy exists.** Management is **supportive and empiric**.

**Pharmacotherapy (empiric mitochondrial cofactors/antioxidants).** Per Mitochondrial Medicine Society dosing guidelines: **riboflavin** (precursor of complex I cofactors FMN/FAD; NCIT: riboflavin therapy), **CoQ10/ubiquinol**, **thiamine**, **vitamin E**, **N-acetylcysteine**, and **L-arginine** for stroke-like episodes; evidence *against* vitamin C and caution on L-carnitine. **Riboflavin may benefit a subset** of complex I deficiencies — a systematic review found 43+ riboflavin-responsive CI cases (predominantly ACAD9, NDUFV1/NDUFV2), though evidence is heterogeneous and no NDUFAF6-specific responsiveness is established.

**Avoidance of mitochondrial toxins.** Valproate, aminoglycosides, high-dose acetaminophen.

**Advanced/experimental therapeutics.** No approved gene, cell, or RNA therapy for MC1DN17. Leigh syndrome interventional trials have been limited to **EPI-743 (vatiquinone)** and **cysteamine bitartrate** — no NDUFAF6-specific trials reported. Gene replacement/editing remains theoretical.

**Supportive & rehabilitative care.** Dystonia management (physical/occupational therapy, botulinum toxin, oral agents), nutritional support, seizure control, and aggressive treatment of intercurrent illness. Rehabilitation to preserve function.

**Treatment strategy.** Genotype does not yet guide a specific pharmacotherapy; management is a standard mitochondrial-disease supportive algorithm plus trigger avoidance.

**Evidence:** [PMID: 42476091](https://pubmed.ncbi.nlm.nih.gov/42476091/): *"No curative therapies exist. Riboflavin, a precursor of CI cofactors FMN and FAD, is a potential treatment, but evidence is heterogeneous and formal guidelines are lacking."* [PMID: 34308912](https://pubmed.ncbi.nlm.nih.gov/34308912/): *"Though historically the treatment for LS is largely supportive, new treatments are on the horizon."* [PMID: 33105273](https://pubmed.ncbi.nlm.nih.gov/33105273/): *"Therapeutic management of mitochondrial disease typically involves empiric prescription of enzymatic cofactors, antioxidants, and amino acid and other nutrient supplements."*

---

## 13. Prevention

**No primary environmental prevention** exists (Mendelian AR disorder). Prevention is **reproductive and supportive**.

- **Primary/reproductive prevention:** genetic counseling; **carrier screening** of at-risk relatives; **cascade testing**; **prenatal diagnosis**; and **preimplantation genetic testing** once the family's biallelic *NDUFAF6* variants are known. In the Acadian founder population, the c.298-768T>C allele enables **targeted population carrier testing**.
- **Secondary prevention:** no newborn screening, but early molecular diagnosis via WGS/RNA analysis enables earlier supportive intervention.
- **Tertiary prevention (preventing decompensation/complications):** aggressive management of intercurrent illness (viral triggers), avoidance of fasting/catabolic stress and mitochondrial-toxic drugs, and empiric cofactor support.

**Evidence:** [PMID: 27466185](https://pubmed.ncbi.nlm.nih.gov/27466185/); [PMID: 33105273](https://pubmed.ncbi.nlm.nih.gov/33105273/); [PMID: 21364701](https://pubmed.ncbi.nlm.nih.gov/21364701/); [PMID: 29531337](https://pubmed.ncbi.nlm.nih.gov/29531337/).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** NDUFAF6 orthologs are conserved across most metazoans that possess complex I, but *"not all"* — indicating some organisms assemble complex I without it. Key orthologs: *Drosophila melanogaster* **'sicily'** (NCBI Taxon 7227); mouse *Ndufaf6* (Taxon 10090). *Saccharomyces cerevisiae* lacks complex I and has no ortholog.
- **Natural disease in other species:** No well-characterized spontaneous NDUFAF6 disease is reported in companion animals or wildlife (OMIA).
- **Comparative biology / evolutionary conservation:** NDUFAF6 belongs to the squalene/phytoene synthase protein family and is a mitochondria-targeted peripheral membrane protein. The conserved fly ortholog validates a conserved assembly-factor mechanism.
- **Transmission:** not applicable (non-infectious, non-zoonotic).

**Evidence:** [PMID: 28476317](https://pubmed.ncbi.nlm.nih.gov/28476317/): *"Most but not all metazoans have an NDUFAF6 ortholog, indicating that in some organisms, complex I biogenesis does not require this protein."*

---

## 15. Model Organisms

- **Drosophila melanogaster 'sicily'** — the validated primary model. Loss of Sicily causes loss of complex I proteins/preproteins, **complex I deficiency, and progressive neurodegeneration**, recapitulating the core disease features. Mechanistically, cytosolic Sicily preprotein interacts with cytosolic Hsp90 to chaperone a CI subunit (ND42) prior to mitochondrial import — revealing a cytosolic chaperone step in complex I biogenesis.
- **Cellular / in vitro models:** patient-derived fibroblasts (absent/low NDUFAF6 protein, reduced steady-state complex I, defective ND1 biogenesis, rescued by wild-type cDNA) — the workhorse for functional validation.
- **Mouse:** ortholog *Ndufaf6* exists, but no prominently published disease-recapitulating knockout.

**Phenotype recapitulation:** the fly model faithfully reproduces complex I deficiency and neurodegeneration; fibroblast complementation confirms causality. **Limitations:** the fly does not model the human bilateral striatal necrosis/dystonia anatomy, and no mammalian model reproduces the full CNS phenotype.

**Evidence:** [PMID: 23509070](https://pubmed.ncbi.nlm.nih.gov/23509070/): *"we identified sicily, the Drosophila melanogaster homologue of human C8ORF38, the loss of which causes Leigh syndrome"* and *"Loss of Sicily leads to loss of CI proteins and preproteins in both mitochondria and cytoplasm, respectively, and causes a CI deficiency and neurodegeneration."*

---

## Mechanistic Model / Interpretation

The unifying model of MC1DN17 is a **single-enzyme (complex I) assembly failure whose clinical expression is dictated by tissue metabolic vulnerability and by allele-specific residual function**:

1. **Genotype → biochemical defect.** *NDUFAF6* is an assembly factor that operates at a **convergence point** in complex I biogenesis — the incorporation/stabilization of the mtDNA-encoded ND1 subunit. Without it, early and mid-stage assembly intermediates form, but late-stage assembly fails, so mature complex I never accumulates. This is a clean **loss-of-function** mechanism (not aggregation or dominant-negative), proven by cDNA rescue.

2. **Biochemical defect → cellular energy crisis.** Absent complex I blocks the entry point of the electron transport chain, collapsing NADH oxidation and proton pumping. Cells shift to anaerobic glycolysis (lactic acidosis) and, by inference from complex I biology, generate excess ROS.

3. **Cellular crisis → selective tissue injury.** The **striatum**, with its very high, sustained energy demand, is the most vulnerable CNS structure, producing the hallmark **bilateral symmetric putaminal necrosis** — the anatomical substrate of Leigh syndrome.

4. **Tissue injury → clinical syndrome.** Striatal degeneration produces the extrapyramidal syndrome — progressive dystonia, rigidity, and developmental regression.

5. **Allelic pleiotropy.** The **FRTS5 branch** is the model's most instructive feature: deep-intronic splice alleles that leave partial NDUFAF6 isoform expression intact spare the brain but injure the **proximal renal tubule and lung**, yielding a Fanconi/pulmonary-fibrosis phenotype instead of encephalopathy. Thus the *same* gene and *same* biochemical pathway produce two clinically distinct diseases depending on **how much functional isoform survives and which tissue's threshold is crossed**.

This model is corroborated across evidence tiers — human genetics (compound-het variant spectra), in vitro (fibroblast complementation, BN-PAGE), and a conserved invertebrate model (*sicily*) — giving high confidence in the causal chain.

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|---|---|---|
| [22019594](https://pubmed.ncbi.nlm.nih.gov/22019594/) | NDUFAF6/C8orf38 loss → absent complex I via failed ND1 biogenesis; defines late-assembly convergence point; complementation rescue | In vitro (patient fibroblasts) |
| [30642748](https://pubmed.ncbi.nlm.nih.gov/30642748/) | Defines classic phenotype: isolated bilateral striatal necrosis + progressive childhood dystonia; 14-patient natural history; compound-het variants | Human clinical + functional |
| [27466185](https://pubmed.ncbi.nlm.nih.gov/27466185/) | Acadian FRTS5 branch: deep-intronic c.298-768T>C founder variant; complex I deficiency in kidney/lung; pleiotropy | Human genetics + functional |
| [29531337](https://pubmed.ncbi.nlm.nih.gov/29531337/) | Recurrent p.Ala178Pro + deep-intronic c.420+784C>T; need for exome + mRNA analysis | Human genetics |
| [33097395](https://pubmed.ncbi.nlm.nih.gov/33097395/) | Mild/atypical cases; normal complex I activity pitfall; viral-triggered decompensation | Human clinical |
| [28476317](https://pubmed.ncbi.nlm.nih.gov/28476317/) | NDUFAF6 protein identity, size, mitochondrial localization, protein family; evolutionary conservation | Computational/biochemical |
| [23509070](https://pubmed.ncbi.nlm.nih.gov/23509070/) | Drosophila 'sicily' model: CI deficiency + neurodegeneration; cytosolic Hsp90 chaperone step | Model organism |
| [31967322](https://pubmed.ncbi.nlm.nih.gov/31967322/) | Comparatively favorable survival for NDUFAF6 Leigh syndrome | Human clinical (cohort) |
| [21364701](https://pubmed.ncbi.nlm.nih.gov/21364701/) | AR inheritance and epidemiologic context of isolated CI deficiency; nuclear vs mtDNA onset | Human clinical (cohort) |
| [42476091](https://pubmed.ncbi.nlm.nih.gov/42476091/) | No cure; riboflavin rationale/uncertainty in CI deficiency | Systematic review |
| [34308912](https://pubmed.ncbi.nlm.nih.gov/34308912/) | Supportive care mainstay; emerging targeted Leigh therapies | Systematic review |
| [33105273](https://pubmed.ncbi.nlm.nih.gov/33105273/) | Empiric cofactor/antioxidant dosing; ≥1 in 4,300 prevalence | Guidelines |
| [32020600](https://pubmed.ncbi.nlm.nih.gov/32020600/), [28639102](https://pubmed.ncbi.nlm.nih.gov/28639102/), [36675121](https://pubmed.ncbi.nlm.nih.gov/36675121/) | NDUFAF6 as rare cause within large Leigh cohorts | Human cohorts |
| [42683144](https://pubmed.ncbi.nlm.nih.gov/42683144/) | NIH UDP case: biallelic NDUFAF6 with developmental delay, stage III CKD, tubular dysfunction | Human case |

**Consistency:** No paper contradicts the core causal model. The main nuance is phenotypic breadth — the same gene causes both a CNS encephalopathy (classic MC1DN17) and a renal/pulmonary disorder (FRTS5), reconciled by allele-specific residual splicing and tissue-specific vulnerability.

---

## Limitations and Knowledge Gaps

1. **No epidemiologic denominators.** There is no established prevalence/incidence for MC1DN17 specifically; estimates rely on the broader isolated complex I deficiency and Leigh syndrome literature. Reported cohorts are very small (single-digit to ~14 patients in dedicated reviews).
2. **Genotype–phenotype resolution is incomplete.** The precise rules governing whether a given allele combination produces the neurological versus the renal/pulmonary phenotype (and severity within each) are not fully defined; the "residual isoform" model is inferred, not quantitatively mapped.
3. **The ROS/oxidative-stress step is inferred**, extrapolated from general complex I biology rather than demonstrated directly in NDUFAF6 patient neurons.
4. **No mammalian model** faithfully reproduces the human striatal-necrosis/dystonia phenotype; mechanistic modeling relies on fibroblasts and Drosophila.
5. **No disease-specific therapy or trials.** Riboflavin responsiveness is documented for other CI genes (ACAD9, NDUFV1/V2), not specifically for NDUFAF6; treatment evidence is extrapolated.
6. **QoL and long-term functional outcomes** have not been formally quantified with standardized instruments.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype registry.** Aggregate all reported NDUFAF6 cases (neurological + FRTS5) with harmonized allele annotations, RNA/splicing data, and tissue phenotypes to model the residual-function → phenotype relationship quantitatively.
2. **Splicing/isoform quantification assays.** Systematically measure mitochondrial NDUFAF6 isoform output for each deep-intronic/hypomorphic allele (minigene or patient-tissue RNA-seq) to test whether isoform level predicts CNS vs renal/pulmonary outcome.
3. **Directly test oxidative stress in patient neurons.** Generate iPSC-derived striatal medium spiny neurons from NDUFAF6 patients to measure ROS, ATP, NAD⁺/NADH, and vulnerability to metabolic stress — validating step 5 of the causal chain.
4. **Riboflavin/cofactor n-of-1 trials.** Given the FMN/FAD rationale and precedent in other CI genes, evaluate riboflavin responsiveness specifically in NDUFAF6 patients under structured n-of-1 or basket-trial designs.
5. **Mammalian model development.** Create a conditional/knock-in mouse (e.g., neuronal or striatal-specific Ndufaf6 loss, or humanized hypomorphic alleles) to model the CNS phenotype and test interventions.
6. **Gene-replacement proof-of-concept.** Because fibroblast complementation fully rescues the defect, test AAV-delivered NDUFAF6 cDNA in patient neurons/organoids and animal models as a route toward gene therapy.
7. **Prospective natural-history and QoL study** using standardized dystonia/QoL instruments to define progression rates and treatment endpoints.

---

*Report compiled from 13 confirmed findings and 24 reviewed papers across a 5-iteration autonomous investigation. Evidence source types are indicated throughout: human clinical, model organism, in vitro, and computational.*


## Artifacts

- [OpenScientist final report](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_17-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_17-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032622` (3 mentions) - the report calls it "if available", "mitochondrial complex I deficiency, nuclear type 17"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 17**
- `DOID:0112078` (1 mention) - the report calls it "DOID"; DOID calls it **nuclear type mitochondrial complex I deficiency 17**
- `HP:0012707` (2 mentions) - the report calls it "Elevated brain lactate (MRS)", "MR spectroscopy:** lactate doublet"; HP calls it **Elevated brain lactate level by MRS**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012706` (2 mentions) - the report calls it "Elevated brain choline (MRS)"; HP calls it **Elevated brain choline level by MRS**
- `HP:0002151` (1 mention) - the report calls it "Increased circulating lactate"; HP calls it **Increased circulating lactate concentration**
- `HP:0011923` (2 mentions) - the report calls it "Decreased complex I activity", "Biochemical abnormality:** isolated complex I enzyme deficiency"; HP calls it **Decreased activity of mitochondrial complex I**, and lists "Respiratory complex I deficiency" among its other names
- `CL:0002613` (2 mentions) - the report calls it "striatal neurons"; CL calls it **striatum neuron**
- `CL:1000838` (1 mention) - the report calls it "proximal tubule epithelial cells"; CL calls it **kidney proximal convoluted tubule epithelial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0032622` - called "if available", "mitochondrial complex I deficiency, nuclear type 17"
- `HP:0012707` - called "Elevated brain lactate (MRS)", "MR spectroscopy:** lactate doublet"
- `HP:0011923` - called "Decreased complex I activity", "Biochemical abnormality:** isolated complex I enzyme deficiency"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.
