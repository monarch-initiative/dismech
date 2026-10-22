---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T12:22:59.798846'
end_time: '2026-10-22T12:46:36.894475'
duration_seconds: 1417.1
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: KPNA7-related Preimplantation Embryonic Arrest
  mondo_id: MONDO:0957220
  category: Mendelian
  causal_genes: KPNA7
  omim_id: OMIM:620319
  synonyms: OZEMA17
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: KPNA7-related_Preimplantation_Embryonic_Arrest-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KPNA7-related_Preimplantation_Embryonic_Arrest-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KPNA7-related Preimplantation Embryonic Arrest
- **MONDO ID:** MONDO:0957220 (if available)
- **Causal gene(s):** KPNA7
- **OMIM:** OMIM:620319
- **Synonyms:** OZEMA17
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **KPNA7-related Preimplantation Embryonic Arrest** covering all of the
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

# KPNA7-related Preimplantation Embryonic Arrest — Comprehensive Research Report

**Disease:** KPNA7-related Preimplantation Embryonic Arrest (PREMBA)
**MONDO ID:** MONDO:0957220 · **Disease OMIM:** 620319 (oocyte/zygote/embryo maturation arrest 17; **OZEMA17**)
**Causal gene:** **KPNA7** (karyopherin subunit alpha 7 / importin-α8) — HGNC:21839 · gene OMIM:614107 · locus 7q22.1
**Category:** Mendelian (autosomal recessive, maternal-effect)

---

## Summary

**KPNA7-related preimplantation embryonic arrest (PREMBA) is an ultra-rare, autosomal-recessive, maternal-effect female-infertility disorder caused by biallelic loss-of-function variants in *KPNA7*, the gene encoding the oocyte- and early-embryo-restricted nuclear-import receptor karyopherin subunit α7 (importin-α8).** The causal gene is **KPNA7** — stated explicitly here because the disease is catalogued under the serial-number synonym OZEMA17 (oocyte maturation arrest 17), which does not name the gene. The disease was defined in 2023 by whole-exome sequencing (WES) burden testing in a cohort of 606 Chinese women with PREMBA versus 2,813 controls, which pinpointed *KPNA7* and 10 affected families carrying rare biallelic variants, most commonly the recurrent missense **c.607C>T (p.Leu203Phe/L203F)** ([PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)).

The core pathophysiology is a failure of **nucleo-cytoplasmic transport during the oocyte-to-embryo transition**. KPNA7 is a maternally supplied importin-α whose expression is almost entirely restricted to oocytes and cleavage-stage embryos. Pathogenic variants reduce KPNA7 protein levels and impair its ability to bind and nuclear-import its cargo **RSL1D1** (ribosomal L1 domain-containing protein 1). Because the correct nuclear delivery of maternal transcriptional/chromatin-remodeling factors is required to switch on the embryo's own genome, the import defect blocks **zygotic genome activation (ZGA)**. Morphologically normal oocytes fertilize normally and begin cleavage, but embryos arrest before the 8-cell stage (day 3) or blastocyst stage (day 5), leaving no transferable embryos and producing recurrent IVF/ICSI failure.

The mechanism is strongly corroborated in a mouse model. Because mouse *Kpna7* is **not** the functional equivalent, the **mouse functional ortholog is *Kpna2***. *Kpna2⁻/⁻* female mice recapitulate PREMBA with 2-cell-stage arrest and ZGA failure, and — critically — the arrest is rescued by microinjection of **human *KPNA7* cRNA but not mouse *Kpna7* cRNA**, establishing cross-species functional equivalence. Oocyte-specific *Rsl1d1* knockout reproduces the same phenotype, nailing down the cargo. There is currently **no cure or pharmacotherapy**; affected women are otherwise systemically healthy, and **donor-oocyte IVF** is the established route to a live birth.

---

## Key Findings

### Finding 1 — *KPNA7* is the causal gene for PREMBA, identified by exome burden testing

A population- and gene-based burden test on whole-exome sequencing from **606 women with PREMBA vs 2,813 controls** identified *karyopherin subunit α7 (KPNA7)* as the candidate gene, with rare biallelic/heterozygous variants significantly enriched in cases. The disease is catalogued as **OMIM:620319** (oocyte/zygote/embryo maturation arrest 17, OZEMA17).

> *"using whole-exome sequencing data from 606 women experiencing PREMBA compared with 2,813 controls, we performed a population and gene-based burden test and identified a candidate gene, karyopherin subunit α7 (KPNA7)"* — [PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)

This is the foundational human-genetics evidence (evidence type: **human clinical / case-control exome study**). The signal was statistically robust (burden P = 2.88×10⁻⁸ for rare biallelic variants, below the Bonferroni threshold P = 1.25×10⁻⁵).

### Finding 2 — Mechanism: variants impair RSL1D1 binding and nuclear import, disrupting ZGA

In vitro, PREMBA-associated KPNA7 variants **reduced KPNA7 protein levels**, **impaired binding to the cargo RSL1D1**, and **reduced nuclear-transport activity**. In vivo, *Kpna2⁻/⁻* female mice (mouse ortholog of human KPNA7) show embryo arrest driven by zygotic genome activation defects, and oocyte-specific *Rsl1d1* knockout recapitulates this.

> *"In vitro studies showed that identified sequence variants reduced KPNA7 protein levels, impaired KPNA7 capacity for binding to its substrate ribosomal L1 domain-containing protein 1 (RSL1D1), and affected KPNA7 nuclear transport activity"* — [PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)

> *"Kpna2-/- female mice showed embryo arrest due to zygotic genome activation defects, recapitulating the phenotype of human PREMBA"* — [PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)

The chain is therefore: loss-of-function variant → reduced/impaired KPNA7 → failed nuclear import of RSL1D1 (and likely other cargoes) → ZGA failure → embryo arrest (evidence types: **in vitro** + **model organism**).

### Finding 3 — KPNA7 is an oocyte/embryo-restricted karyopherin-α with distinct cargo specificity

KPNA7 expression is largely limited to early development (oocytes and cleavage-stage embryos). In pig, *KPNA7* knockdown by interfering RNA significantly lowered embryo cell numbers (P<0.05). Biochemically, KPNA7 has atypical behavior: it can bind Importin-β **in the absence of NLS cargo** and maintains an "open" conformation, unlike other KPNA family members whose IBB domain auto-inhibits the NLS-binding groove.

> *"Embryos injected with KPNA7-interfering RNAs possessed significantly lower cell numbers than their respective control groups (P<0.05)"* — [PMID: 22281085](https://pubmed.ncbi.nlm.nih.gov/22281085/)

> *"KPNA7, an isoform with expression mostly limited to early development, can bind Importin-β (Imp-β) in the absence of NLS cargo"* — [PMID: 31642884](https://pubmed.ncbi.nlm.nih.gov/31642884/)

This establishes both the **developmental-window specificity** (why the disease is confined to preimplantation development) and the **unique cargo/NLS specificity** that explains why KPNA7 cannot be fully substituted by other importin-α paralogs.

### Finding 4 — Gene identifiers and population constraint: LoF-tolerant, consistent with recessive maternal-effect inheritance

| Attribute | Value |
|---|---|
| Gene symbol | KPNA7 |
| Aliases | IPOA8, OZEMA17 (importin-α8) |
| HGNC | HGNC:21839 |
| Entrez Gene | 402569 |
| Ensembl | ENSG00000185467 |
| Gene OMIM | 614107 |
| Disease OMIM | 620319 |
| Cytoband | 7q22.1 (GRCh38 chr7:99,173,572–99,250,075, minus strand) |
| Pseudogene | present on chr5 |
| gnomAD pLI | 5.9×10⁻¹⁹ (≈0 — LoF-tolerant) |
| Observed/expected LoF | 54/53.7 (o/e 1.01; 90% CI 0.81–1.26) |
| Missense Z | 0.07 |

The near-zero pLI and o/e(LoF) ≈ 1 indicate *KPNA7* is **tolerant of heterozygous loss of function** at the population level — exactly what is expected for a **recessive, maternal-effect** gene whose phenotype manifests only in the embryos of homozygous/compound-heterozygous women and has no effect on carrier viability or reproduction. (Evidence type: **computational / population genomics**.)

### Finding 5 — KPNA7 somatic functions: mitotic fidelity and nuclear-envelope integrity

Although KPNA7 is virtually silent in adult somatic tissues, it is **re-expressed in some cancers**, where it supports proliferation and genome stability. siRNA knockdown in pancreatic and breast cancer cell lines reduced proliferation and S-phase fraction, produced aberrant centrosome numbers and distorted mitotic spindles, reorganized lamin A/C and B1, and produced lobulated/elongated nuclei.

> *"the silencing of KPNA7 results in a dramatic reduction in pancreatic and breast cancer cell growth, irrespective of the endogenous KPNA7 expression level. This growth inhibition is accompanied by a decrease in the fraction of S-phase cells as well as aberrant number of centrosomes and severe distortion of the mitotic spindles"* — [PMID: 29580221](https://pubmed.ncbi.nlm.nih.gov/29580221/)

> *"KPNA7 depletion leads to reorganization of lamin A/C and B1, the main nuclear lamina proteins, and drastic alterations in nuclear morphology"* — [PMID: 29580221](https://pubmed.ncbi.nlm.nih.gov/29580221/)

These somatic roles (cell-cycle progression, centrosome number, mitotic-spindle integrity, nuclear-lamina organization) are mechanistically relevant: beyond RSL1D1 import, KPNA7 loss in the cleavage-stage embryo could also compromise mitotic fidelity — a plausible contributor to arrest (evidence type: **in vitro, cancer cell lines**).

### Finding 6 — Specific pathogenic variants and genotypes (10 families; recurrent p.L203F)

In the discovery cohort, rare biallelic *KPNA7* variants (transcript **NM_001145715.3**) occurred in **10 patients and 0 controls** (burden P = 2.88×10⁻⁸). Across the 10 independent families:

| Family(ies) | Genotype | Variant(s) |
|---|---|---|
| 1, 2, 4, 5, 7, 10 | Homozygous | c.607C>T, **p.Leu203Phe (L203F)** |
| 3 | Compound het | p.L203F + c.635C>T (**p.Pro212Leu**) |
| 6 | Compound het | p.L203F + c.523C>A (**p.Gln175Lys**) |
| 9 | Compound het | p.L203F + c.1350_1356delGTGTCTT (**p.Cys451***, truncating) |

No homozygotes for the recurrent variant existed in gnomAD/ExAC (MAF<1%) or in-house controls. Homozygosity mapping suggested a **low probability of a founder effect** (recurrence of p.L203F likely reflects a mutational hotspot or independent origins rather than a single shared haplotype). All five tested mutant proteins showed reduced KPNA7 levels and impaired RSL1D1 binding/nuclear transport.

> *"In vitro studies showed that identified sequence variants reduced KPNA7 protein levels, impaired KPNA7 capacity for binding to its substrate ribosomal L1 domain-containing protein 1 (RSL1D1), and affected KPNA7 nuclear transport activity"* — [PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)

### Finding 7 — Clinical phenotype, epidemiologic context, and differential diagnosis

The PREMBA phenotype: morphologically normal oocytes are retrieved, fertilize normally, and undergo the first cleavage division, **but most embryos arrest before the 8-cell stage (day 3) or before the blastocyst stage (day 5)**, yielding no viable embryos and recurrent IVF/ICSI failure. About **10% of all IVF/ICSI embryos** arrest at primary cleavage stages (the broad clinical backdrop). Most previously identified PREMBA genes encode **subcortical maternal complex (SCMC)** proteins — *PADI6, NLRP2, NLRP5, KHDC3L* — whereas *KPNA7* defines a **distinct nuclear-transport mechanism**. Biallelic variants in *KPNA7* plus *PADI6* together explained ~**3.6% of the cohort (22/606)**.

> *"Preimplantation embryo arrest (PREMBA) is a common cause of female infertility and recurrent failure of assisted reproductive technology"* — [PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)

### Finding 8 — Mouse *Kpna2* (not *Kpna7*) is the functional ortholog; *Kpna2⁻/⁻* recapitulates 2-cell arrest with ZGA failure

*Kpna2⁻/⁻* female mice recapitulate PREMBA: reduced body size, small ovaries, few oocytes on superovulation, and embryos uniformly arrested at the **2-cell stage** (coinciding with major ZGA, which in mouse initiates at the 2-cell stage). Oocyte-specific *Rsl1d1* knockout reproduces the phenotype. Cross-species rescue established the orthology: microinjection of **human *KPNA7* cRNA — but not mouse *Kpna7* — rescued** the *Kpna2⁻/⁻* arrest.

> *"complementary RNA (cRNA) microinjection of human KPNA7, but not mouse Kpna7, was able to rescue the embryo arrest phenotype in Kpna2-/- mice, suggesting mouse KPNA2 might be a homologue of human KPNA7"* — [PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)

> *"As shown in embryos of Kpna2-null females, the consequences are disrupted zygotic genome activation and arrest of development"* — [PMID: 36647833](https://pubmed.ncbi.nlm.nih.gov/36647833/)

This is the single most important cross-species validation (evidence type: **model organism, genetic rescue**) and is a crucial caution for model selection: targeting mouse *Kpna7* would **not** model the human disease.

### Finding 9 — Protein architecture: IBB domain + 8 ARM repeats; missense variants map to the NLS-binding ARM groove

KPNA7 (UniProt **A9QM74**) is a **516-aa importin-α**: an N-terminal importin-β-binding (**IBB**) domain (~aa 1–57) and **8 armadillo (ARM) repeats** (~aa 103–439) forming the NLS-binding groove. The PREMBA missense variants map into the cargo-binding region: **p.Gln175Lys** (ARM2, ~146–185), **p.Leu203Phe** and **p.Pro212Leu** (ARM3, ~188–228); the truncating **p.Cys451*** removes the C-terminal/acidic region downstream of ARM8.

This structural mapping provides a direct mechanistic rationale: the recurrent and compound-heterozygous missense substitutions sit in the ARM repeats that build the NLS-binding surface, consistent with the observed **loss of RSL1D1 binding** (evidence type: **computational / structural annotation**).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *KPNA7* loss-of-function variants** (most commonly homozygous c.607C>T, p.Leu203Phe in ARM3) are inherited by the affected woman → **leads to** a mutant, destabilized KPNA7 importin-α in her oocytes.
2. **Reduced KPNA7 protein level + structurally altered NLS-binding ARM groove** → **results in** impaired binding of KPNA7 to its cargo **RSL1D1** (and probably other NLS-bearing maternal factors). *(Demonstrated in vitro.)*
3. **Loss of KPNA7-mediated nuclear import** of these cargoes → **leads to** failure to deliver transcriptional/chromatin-remodeling factors into the embryonic nucleus at the oocyte-to-embryo transition. *(Inferred from cargo identity + import assays.)*
4. **Nuclear-transport failure** → **results in** defective **zygotic genome activation (ZGA)** — the embryo cannot switch from maternal to its own transcriptional program. *(Demonstrated in Kpna2-null mouse; inferred in human.)*
5. **ZGA failure** → **leads to** developmental arrest: in human, before the 8-cell (day 3) / blastocyst (day 5) stage; in mouse, at the 2-cell stage (where major ZGA occurs).
6. **Branch (inferred, from somatic KPNA7 biology):** reduced KPNA7 may additionally compromise **centrosome number, mitotic-spindle integrity, and nuclear-lamina organization** in cleavage divisions → contributing to arrest independently of or alongside ZGA failure.
7. **Embryo arrest** → **results in** no transferable embryos → **recurrent IVF/ICSI failure and female infertility** (the clinical phenotype). The woman herself is systemically healthy.

```
 KPNA7 biallelic LoF (p.L203F ...)
          │  reduces protein / alters ARM groove
          ▼
 Impaired KPNA7–RSL1D1 binding  ──────┐ (in vitro)
          │                           │
          ▼                           ▼  (inferred somatic branch)
 Failed nuclear import of        Centrosome/spindle &
 maternal TFs / chromatin        nuclear-lamina defects
 remodelers                      (from cancer-cell data)
          │                           │
          ▼                           │
 Zygotic genome activation      ◄─────┘
 (ZGA) failure  (Kpna2-/- mouse)
          │
          ▼
 Cleavage-stage embryo arrest (pre-8-cell / pre-blastocyst)
          │
          ▼
 No transferable embryos → recurrent ART failure / infertility
```

### Human-vs-mouse orthology (critical for interpretation and modeling)

| Species | Functional gene at oocyte-to-embryo transition | Knockout phenotype | Notes |
|---|---|---|---|
| Human | **KPNA7** | PREMBA (pre-8-cell/blastocyst arrest) | disease gene |
| Mouse | **Kpna2** (NOT Kpna7) | 2-cell arrest, ZGA failure | rescued by human *KPNA7* cRNA, not mouse *Kpna7* |

**Ontology suggestions.** Biological process (GO): **GO:0006606** (protein import into nucleus), **GO:0051170** (import into nucleus), **GO:0017038** (protein import), positive regulation of embryonic transcription / ZGA. Molecular function (GO): **GO:0008139** (nuclear localization sequence binding), **GO:0061608** (nuclear import signal receptor activity). Cellular component (GO): **GO:0005635** (nuclear envelope), **GO:0005643** (nuclear pore), **GO:0005730** (nucleolus, for RSL1D1), **GO:0005813** (centrosome). Cell types (CL): **CL:0000023** (oocyte), **CL:0000670** (primordial germ cell), early blastomere/embryonic cell. Anatomy (UBERON): **UBERON:0000992** (ovary), **UBERON:0000922** (embryo), oocyte/zygote structures. Chemical entity (CHEBI): GTP (**CHEBI:15996**, Ran-GTP cycle context). Disease: **MONDO:0957220**.

---

## Section-by-Section Disease Characteristics

### 1. Disease Information
KPNA7-related PREMBA is a Mendelian female-infertility disorder in which fertilized oocytes arrest during preimplantation cleavage. **Causal gene: KPNA7.** Identifiers: **MONDO:0957220**, **disease OMIM:620319** (OZEMA17), **gene OMIM:614107**. There is no dedicated ICD-10/ICD-11, MeSH, or distinct Orphanet code specific to the KPNA7 subtype in the available evidence; clinically it falls under female infertility / recurrent ART failure. Synonyms: **OZEMA17** (oocyte/zygote/embryo maturation arrest 17); gene aliases **IPOA8 / importin-α8**. Information is a mix of **individual-patient** data (10 families, in-depth genotype–phenotype) and **aggregate** resources (OMIM, gnomAD).

### 2. Etiology
**Primary cause: genetic** — biallelic (homozygous or compound-heterozygous) loss-of-function variants in *KPNA7*. **Genetic risk factor:** inheriting two pathogenic *KPNA7* alleles; the recurrent **p.L203F** is the principal allele. **Consanguinity** plausibly increases homozygosity risk (6/10 families homozygous), though a founder effect was judged unlikely. No environmental, infectious, lifestyle, protective, or gene-environment factors are established — this is a monogenic maternal-effect disorder. Carriers (heterozygotes) are unaffected and fertile, consistent with the LoF-tolerant gnomAD constraint.

### 3. Phenotypes
The phenotype is reproductive and effectively **embryo-level**, not a systemic phenotype in the affected woman:
- **Preimplantation embryonic arrest** (cleavage-stage, before 8-cell/blastocyst). HPO candidates: **HP:0000789** (Infertility), **HP:0008215** (Female infertility), and embryonic-arrest/ART-failure terms.
- **Recurrent IVF/ICSI failure** — clinical sign; onset at **reproductive age** when ART is attempted; severity: **severe** (no viable embryos); progression: **stable** (consistent across cycles).
- **Normal oocyte retrieval, normal fertilization, normal first cleavage** — the defect is downstream of fertilization.
- **Frequency among affected:** essentially 100% embryo arrest within affected women.
- **Quality-of-life impact:** substantial reproductive and psychosocial burden of infertility; no somatic morbidity.

### 4. Genetic/Molecular Information
Causal gene **KPNA7** (HGNC:21839; 7q22.1). Pathogenic variants (NM_001145715.3): **c.607C>T p.Leu203Phe** (recurrent missense), **c.635C>T p.Pro212Leu**, **c.523C>A p.Gln175Lys**, **c.1350_1356del p.Cys451*** (truncating). Variant classes: missense + one truncating allele. **Functional consequence: loss of function** (reduced protein, impaired cargo binding and nuclear import). **Origin: germline.** Population AF: absent/ultra-rare in gnomAD/ExAC (MAF<1%; no control homozygotes). No modifier genes, epigenetic changes, or chromosomal abnormalities are established for this disorder.

### 5. Environmental Information
**Not applicable.** No environmental toxins, lifestyle factors, or infectious agents are implicated. This is a purely monogenic maternal-effect disorder.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** above for the full ordered causal chain. Core pathway: **nucleo-cytoplasmic transport** (importin-α/β–Ran system) → **RSL1D1 nuclear import** → **zygotic genome activation**. Cellular processes: cell-cycle/cleavage division, possible centrosome/spindle and nuclear-lamina involvement. Protein dysfunction: **loss of function** of an importin-α with destabilization and loss of NLS-binding. Upstream = variant/import failure; downstream = ZGA failure and arrest.

### 7. Anatomical Structures Affected
- **Organ/tissue:** ovary (oocytes) and the preimplantation embryo; female reproductive system (UBERON:0000992 ovary; UBERON:0000922 embryo).
- **Cell types (CL):** oocyte (CL:0000023), zygote, early blastomeres.
- **Subcellular (GO CC):** nuclear pore/nuclear envelope (GO:0005643/GO:0005635), nucleus, nucleolus (RSL1D1), centrosome (GO:0005813), nuclear lamina.
- **Lateralization:** not applicable (bilateral ovaries; defect is cell-intrinsic).

### 8. Temporal Development
- **Onset:** the embryonic defect manifests at the **oocyte-to-embryo transition / cleavage stage** (first days post-fertilization). Clinically recognized at **reproductive age** upon ART failure.
- **Progression:** **stable/consistent** — arrest recurs every cycle; not progressive within the woman.
- **Critical period:** the narrow window of **ZGA** during preimplantation development; no intervention window has been demonstrated.

### 9. Inheritance and Population
- **Inheritance:** **autosomal recessive, maternal-effect** (phenotype depends on the mother's genotype, expressed in her embryos).
- **Penetrance:** apparently high/complete for embryo arrest in biallelic women (within the reported families).
- **Epidemiology:** **ultra-rare**; precise prevalence/incidence unknown. Within an infertility cohort enriched for PREMBA, *KPNA7*+*PADI6* biallelic variants explained ~3.6% (22/606); *KPNA7* alone accounted for 10 families.
- **Founder effect:** judged **low probability** despite recurrent p.L203F.
- **Population:** discovery cohort was **Chinese**; broader ethnic distribution undefined.
- **Sex:** phenotype expressed through **females** (maternal-effect); carrier males are unaffected.

### 10. Diagnostics
- **Genetic testing is the diagnostic cornerstone:** **WES** (how the gene was found) or targeted **single-gene / infertility gene-panel** testing for biallelic *KPNA7* variants; WGS also applicable. Differential includes SCMC-gene disorders (*PADI6, NLRP2, NLRP5, KHDC3L, TLE6, OOEP*) and other oocyte/zygote maturation-arrest genes.
- **Clinical/functional clue:** time-lapse embryology documenting normal fertilization and first cleavage followed by **consistent pre-8-cell/pre-blastocyst arrest** across multiple cycles.
- No specific serum/urine biomarker, imaging, or histopathology test exists. Karyotype/CMA typically normal.
- **Screening:** carrier screening in consanguineous families / affected pedigrees; cascade testing of relatives.

### 11. Outcome / Prognosis
- **Reproductive prognosis with autologous oocytes: very poor** — recurrent total embryo arrest and ART failure.
- **No systemic mortality/morbidity** in the affected woman — she is otherwise healthy; life expectancy unaffected.
- **Favorable reproductive outcome is achievable** via donor-oocyte IVF (bypasses the maternal-effect defect).
- Prognostic factor: the defect is embryo-intrinsic and cycle-independent, so repeating autologous cycles is predictably unsuccessful.

### 12. Treatment
- **No pharmacotherapy, gene therapy, or targeted therapy exists**; none is established for a maternal-effect oocyte transport defect.
- **Standard of care: donor-oocyte IVF** (NCIT: oocyte donation / in vitro fertilization procedures) — the established route to a live birth, as it supplies wild-type KPNA7 maternal protein.
- **Genetic counseling** is a key component of management.
- Experimental concepts (not clinically available): cytoplasmic/spindle transfer or cRNA/protein supplementation of oocytes — supported conceptually by the mouse cRNA-rescue experiment but not translated to humans.

### 13. Prevention
- **Genetic counseling** for couples with recurrent total embryo arrest and identified biallelic *KPNA7* variants.
- **Carrier/cascade screening** in affected families and consanguineous couples.
- **Reproductive options:** donor-oocyte IVF. PGT is **not** useful here because the defect is a maternal-effect in the egg cytoplasm, not an embryo-genotype issue that can be selected against.
- No primary/secondary public-health or immunization prevention applies.

### 14. Other Species / Natural Disease
- **Mouse (NCBI Taxon 10090):** functional ortholog is ***Kpna2*** (not *Kpna7*); *Kpna2⁻/⁻* females show 2-cell arrest with ZGA failure. Mouse *Kpna7* exists but does **not** rescue the phenotype.
- **Pig (NCBI Taxon 9823):** *KPNA7* RNAi reduces cleavage-stage embryo cell number ([PMID: 22281085](https://pubmed.ncbi.nlm.nih.gov/22281085/)).
- No naturally occurring companion-animal/wildlife disease (OMIA) is documented for this gene; no zoonotic relevance.

### 15. Model Organisms
- **Mouse *Kpna2* knockout** (*Kpna2⁻/⁻* females): the best genetic model — **recapitulates PREMBA** (small ovaries, few oocytes, 2-cell arrest, ZGA failure); validated by human-*KPNA7*-cRNA rescue. Resource: MGI.
- **Oocyte-specific *Rsl1d1* knockout** mouse: models the cargo-side of the mechanism.
- **Porcine embryo RNAi** (in vitro/ex vivo): demonstrates conserved requirement in cleavage-stage development.
- **Cancer cell lines** (pancreatic, breast) with *KPNA7* siRNA: not disease models, but reveal KPNA7's mitotic/nuclear-envelope functions.
- **Limitations:** the species difference (mouse *Kpna2* vs human *KPNA7*) complicates naive mouse modeling; human preimplantation biology (timing/stage of arrest, specific cargo repertoire) is not fully captured by mouse.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/) | *Karyopherin α deficiency contributes to human preimplantation embryo arrest* | Human genetics + in vitro + mouse | **Primary/landmark**: gene discovery, variants, RSL1D1/import mechanism, Kpna2 rescue |
| [36647833](https://pubmed.ncbi.nlm.nih.gov/36647833/) | *Take your mother's ferry: preimplantation embryo development requires maternal karyopherins...* | Commentary/review | Independent confirmation of ZGA disruption and arrest in Kpna2-null model |
| [31642884](https://pubmed.ncbi.nlm.nih.gov/31642884/) | *Characterization of the Importin-β binding domain in KPNA7* | Biochemistry/structural | KPNA7's early-development expression and atypical Imp-β binding; "open" state |
| [22281085](https://pubmed.ncbi.nlm.nih.gov/22281085/) | *KPNA7... required for porcine embryo development* | Model organism (pig) | Functional requirement in cleavage-stage embryos (P<0.05) |
| [29580221](https://pubmed.ncbi.nlm.nih.gov/29580221/) | *Depletion of KPNA7 induces mitotic defects and deformation of nuclei in cancer cells* | In vitro (cancer lines) | Somatic roles: mitotic spindle, centrosomes, nuclear lamina |
| [26399853](https://pubmed.ncbi.nlm.nih.gov/26399853/) | *Changing expression/subcellular distribution of karyopherins during murine oogenesis* | Model organism (mouse) | Karyopherins dynamically regulated in oogenesis; supports KPN roles in oocyte development |
| [34362424](https://pubmed.ncbi.nlm.nih.gov/34362424/) | *RSL1D1 coordinates with HDM2 to regulate p53...* | In vitro | Background on cargo RSL1D1 (nucleolar protein, cell-proliferation role) |
| [17158916](https://pubmed.ncbi.nlm.nih.gov/17158916/) | *Multiple controls regulate nucleostemin partitioning...* | In vitro | RSL1D1 biology (ribosomal L1 domain; nucleolar partitioning) |

**How the evidence converges:** The landmark paper ([PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)) supplies the human genetics, the in-vitro mechanism, and the mouse model in one study — an unusually complete causal demonstration. Independent commentary ([PMID: 36647833](https://pubmed.ncbi.nlm.nih.gov/36647833/)) and prior functional work in pig ([PMID: 22281085](https://pubmed.ncbi.nlm.nih.gov/22281085/)) and biochemistry ([PMID: 31642884](https://pubmed.ncbi.nlm.nih.gov/31642884/)) corroborate the developmental restriction and transport function. The cancer-cell work ([PMID: 29580221](https://pubmed.ncbi.nlm.nih.gov/29580221/)) adds a plausible secondary (mitotic/nuclear-envelope) mechanism.

---

## Limitations and Knowledge Gaps

- **Single discovery cohort, one ethnicity:** The human genetics derives almost entirely from one Chinese cohort (606 cases). Prevalence, pan-ethnic allele spectrum, and whether p.L203F recurs globally are unknown.
- **Small family count:** 10 families define the full known mutational spectrum; the complete variant landscape and any genotype–phenotype gradation (e.g., day-3 vs day-5 arrest) are under-characterized.
- **Cargo repertoire incomplete:** RSL1D1 is the demonstrated cargo, but KPNA7 likely imports additional maternal factors; the full set and which are rate-limiting for ZGA are unresolved.
- **Secondary mechanism inferred:** The mitotic-fidelity/nuclear-lamina branch is extrapolated from cancer cells, not demonstrated in human embryos.
- **Human-vs-mouse orthology complexity:** Conclusions about ZGA timing/arrest stage rest on mouse *Kpna2*; human preimplantation specifics are inferred.
- **No therapeutics:** No treatment addresses the oocyte defect; only donor oocytes bypass it. No biomarker exists for pre-ART risk stratification.
- **Ontology coverage:** Disease lacks dedicated ICD/MeSH codes; HPO annotation for "embryonic arrest" is imperfect.

---

## Proposed Follow-up Experiments / Actions

1. **Replicate and expand the genetics:** Sequence *KPNA7* in independent, multi-ethnic PREMBA/recurrent-ART-failure cohorts to estimate true prevalence, confirm p.L203F recurrence, and expand the variant spectrum; deposit variants in ClinVar with ACMG classifications.
2. **Define the full KPNA7 cargo set** in human/mouse oocytes (e.g., proximity labeling / IP-MS of KPNA7 across the oocyte-to-embryo transition) to identify which imported factors are rate-limiting for ZGA.
3. **Human-relevant functional modeling:** Use human iPSC-derived or patient oocyte/embryo systems with single-embryo RNA-seq to directly test ZGA failure in human KPNA7-deficient embryos and map the transcriptional defect.
4. **Structural validation:** Solve/compute KPNA7–NLS/RSL1D1 complex structures (AlphaFold-Multimer + biophysics) to confirm how p.L203F/p.P212L/p.Q175K disrupt the ARM NLS groove and quantify binding-affinity changes.
5. **Test the secondary mitotic branch:** Assess centrosome number, spindle integrity, and nuclear-lamina organization in KPNA7-deficient cleavage-stage embryos to determine whether it contributes to arrest independently of ZGA.
6. **Therapeutic proof-of-concept:** Explore oocyte **cRNA/protein supplementation** of wild-type KPNA7 (building on the mouse cRNA rescue) as a conceptual rescue, while recognizing clinical/ethical barriers.
7. **Clinical pathway:** Establish genetic-counseling and **donor-oocyte** referral guidance for women with biallelic *KPNA7* variants and recurrent total embryo arrest; formalize cascade carrier screening in affected families.

---

*Evidence-source legend:* human clinical/genetics ([PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/)); model organism — mouse ([PMID: 36647821](https://pubmed.ncbi.nlm.nih.gov/36647821/), [PMID: 36647833](https://pubmed.ncbi.nlm.nih.gov/36647833/), [PMID: 26399853](https://pubmed.ncbi.nlm.nih.gov/26399853/)), pig ([PMID: 22281085](https://pubmed.ncbi.nlm.nih.gov/22281085/)); in vitro/biochemistry ([PMID: 31642884](https://pubmed.ncbi.nlm.nih.gov/31642884/), [PMID: 29580221](https://pubmed.ncbi.nlm.nih.gov/29580221/), [PMID: 34362424](https://pubmed.ncbi.nlm.nih.gov/34362424/), [PMID: 17158916](https://pubmed.ncbi.nlm.nih.gov/17158916/)); computational/population (gnomAD constraint).


## Artifacts

- [OpenScientist final report](KPNA7-related_Preimplantation_Embryonic_Arrest-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KPNA7-related_Preimplantation_Embryonic_Arrest-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957220` (4 mentions) - the report calls it "if available"; MONDO calls it **oocyte/zygote/embryo maturation arrest 17**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0008215` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0008139` (obsolete nuclear localization sequence binding) (1 mention) - replaced by `GO:0140142`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
