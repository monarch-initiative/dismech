---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T20:31:55.357602'
end_time: '2026-10-22T21:20:45.929054'
duration_seconds: 2930.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: DDX17-related Neurodevelopmental Disorder
  mondo_id: MONDO:0700368
  category: Mendelian
  causal_genes: DDX17
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 14
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 13
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: DDX17-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DDX17-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DDX17-related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0700368 (if available)
- **Causal gene(s):** DDX17
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **DDX17-related Neurodevelopmental Disorder** covering all of the
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

# DDX17-Related Neurodevelopmental Disorder — Comprehensive Research Report

**Disease:** DDX17-related Neurodevelopmental Disorder
**MONDO ID:** MONDO:0700368
**OMIM phenotype:** Intellectual developmental disorder, autosomal dominant 73 (MRD73)
**Causal gene:** **DDX17** (DEAD-box helicase 17; HGNC:2740; NCBI Gene 10521; Ensembl ENSG00000100201; UniProt Q92841), located on chromosome **22q13.1**
**Category:** Mendelian, autosomal dominant

---

## Summary

**DDX17-related neurodevelopmental disorder (DDX17-NDD) is an ultra-rare, autosomal-dominant Mendelian condition caused by *de novo* heterozygous loss-of-function and missense variants in the causal gene DDX17**, which encodes an ATP-dependent DEAD-box RNA helicase on chromosome 22q13.1. It must not be confused with the clinically overlapping but genetically distinct DDX3X syndrome, which is caused by the X-linked helicase DDX3X; the two share a DEAD-box helicase class and a neurodevelopmental presentation but differ in gene, chromosome, inheritance dynamics, and sex distribution. The entire published knowledge base for DDX17-NDD rests on a single multinational case series of 11 unrelated patients reported by Seaby and colleagues in 2025 ([PMID: 39405200](https://pubmed.ncbi.nlm.nih.gov/39405200/)), supported by extensive cross-species functional validation.

The core clinical phenotype is a neurodevelopmental one: **intellectual disability, delayed speech and language, and motor delay predominate**, accompanied in subsets of patients by hypotonia, ADHD, autism spectrum features, motor stereotypies, mild facial dysmorphism, and macrocephaly. Notably, no epilepsy was reported in the cohort. Half of imaged patients had non-specific brain MRI abnormalities (cortical dysplasia/asymmetry, white-matter changes). The condition is static and developmental rather than neurodegenerative; all 11 patients were alive at a median age of 15 years, indicating no evidence of reduced life expectancy.

Mechanistically, DDX17 is a **haploinsufficient gene** (gnomAD pLI = 1.0; 37.7 loss-of-function variants expected but only 1 observed). The protein is a multifunctional regulator of neuronal gene expression operating through alternative splicing, pri-miRNA/Microprocessor processing, transcriptional co-regulation, and — most relevant to neurodevelopment — the **REST–proneural-microRNA axis** that governs the timing of neuronal gene activation. Reduction of DDX17 dosage impairs cortical neuron radial migration and axon outgrowth, as demonstrated in mouse *in utero* electroporation, *Xenopus tropicalis* crispant and heterozygous-knockout models, and human SH-SY5Y neuroblastoma transcriptomics. There is no disease-specific or targeted therapy; management is supportive and multidisciplinary.

---

## Key Findings

### Finding 1 — DDX17 monoallelic *de novo* variants cause an autosomal-dominant neurodevelopmental disorder

The defining study ([PMID: 39405200](https://pubmed.ncbi.nlm.nih.gov/39405200/)) compiled a case series of **11 unrelated patients** with neurodevelopmental phenotypes, each carrying a *de novo* monoallelic (heterozygous) variant in DDX17. All 11/11 (100%) had a neurodevelopmental phenotype, with intellectual disability, delayed speech/language, and motor delay predominating. As stated in the abstract: *"Globally, we compiled a case series of 11 patients with neurodevelopmental phenotypes harbouring de novo monoallelic variants in DDX17. All 11 patients in our case series had a neurodevelopmental phenotype, whereby intellectual disability, delayed speech and language, and motor delay predominated."* This establishes the gene–disease relationship, the inheritance mode, the cohort size, and the core phenotype.

> **Note / correction:** An early iteration erroneously described DDX17 as X-linked. This was corrected: **DDX17 is autosomal, on chromosome 22q13.1.** (The X-linked helicase in this disease family is DDX3X, a different gene.)

### Finding 2 — Gene identity, genomic location, and pathogenic variant spectrum

**DDX17** (DEAD-box helicase 17; aliases **P72**, **RH70**) maps to **22q13.1** (Ensembl ENSG00000100201, chr22:38,483,438–38,507,660, minus strand; NCBI Gene 10521; HGNC:2740; canonical RefSeq NM_006386.5). The associated OMIM phenotype is **Intellectual developmental disorder, autosomal dominant 73 (MRD73)**. ClinVar (accessed 2026) lists approximately 75 DDX17 variant records. Disease-relevant examples span multiple variant classes:

| Variant (cDNA / protein) | Class | Classification |
|---|---|---|
| c.1151_1155del p.(Leu384fs) | Frameshift | Pathogenic |
| c.1133A>G p.(Asn378Ser) | Missense | Likely pathogenic |
| c.1684+1G>A | Canonical splice | AD 73-associated |
| c.1447+4T>C | Splice region | AD 73-associated |
| p.(Gln550Ter), p.(Arg508Ter), p.(Cys166Ter) | Nonsense | Reported |
| p.(Arg430fs), p.(Cys11fs) | Frameshift | Reported |

Variant classes therefore include frameshift, nonsense, canonical splice-site, and missense.

### Finding 3 — DDX17 molecular function: a multifunctional DEAD-box RNA helicase

DDX17 is an ATP-dependent DEAD-box RNA helicase (conserved Asp-Glu-Ala-Asp motif) with RNA-dependent ATPase and helicase activity, producing **p72 and p82 isoforms** via alternative translation initiation (including a non-AUG CUG start). It is highly expressed in neuronal tissue and cardiomyocytes. Documented molecular roles:

1. **miRNA biogenesis** — component of the Drosha/Microprocessor complex; DDX17/p72 recognizes sequences 3′ to the mature miRNA and enhances Drosha processing ([PMID: 31851931](https://pubmed.ncbi.nlm.nih.gov/31851931/): *"DDX17, a DEAD-box ATPase, is a multifunctional helicase important for various RNA functions, including microRNA maturation."*); conserved role shown in *C. elegans* ([PMID: 26601717](https://pubmed.ncbi.nlm.nih.gov/26601717/)) and for miR-132 ([PMID: 26947125](https://pubmed.ncbi.nlm.nih.gov/26947125/)).
2. **Alternative-splicing regulation and transcriptional co-activation** — of ERα, AR, p53, β-catenin, NFAT5, often paired with its closest paralog DDX5/p68 ([PMID: 24275493](https://pubmed.ncbi.nlm.nih.gov/24275493/): *"The Ddx5 and Ddx17 RNA helicases are also splicing regulators."*; [PMID: 22713328](https://pubmed.ncbi.nlm.nih.gov/22713328/); [PMID: 22266867](https://pubmed.ncbi.nlm.nih.gov/22266867/)).
3. **Regulation of Ago2 protein levels** via miRNA biogenesis ([PMID: 27478153](https://pubmed.ncbi.nlm.nih.gov/27478153/)).
4. **Membraneless-organelle / nucleolar localization** — the p82 isoform carries intrinsically disordered regions driving MLO formation ([PMID: 32065632](https://pubmed.ncbi.nlm.nih.gov/32065632/)).

High neuronal expression ([PMID: 41322492](https://pubmed.ncbi.nlm.nih.gov/41322492/): *"It distributes in the nucleus and cytoplasm, highly expressed in cardiomyocytes and neuronal tissues."*) is consistent with the neurodevelopmental phenotype.

**Suggested GO terms:** RNA helicase activity (GO:0003724), pri-miRNA processing (GO:0031053), regulation of alternative mRNA splicing via spliceosome (GO:0000381), transcription coactivator activity (GO:0003713).

### Finding 4 — Clinical phenotype spectrum and frequencies (n = 11)

From Seaby et al. Table 1 ([PMID: 39405200](https://pubmed.ncbi.nlm.nih.gov/39405200/); PMC11967813): n = 11 (8 male / 3 female, all alive, median age 15 years).

| Phenotype | Frequency | HPO term |
|---|---|---|
| Neurodevelopmental delay | 10/11 (91%) | HP:0012758 |
| Delayed speech & language | 10/11 (91%) | HP:0000750 |
| Global developmental delay | 9/11 (82%) | HP:0001263 |
| Fine motor delay | 9/11 (82%) | HP:0007010 |
| Intellectual disability (mild–moderate) | 7/11 (64%) | HP:0001249 |
| Gross motor delay | 7/11 (64%) | HP:0002194 |
| Dysmorphic facial features | 7/11 (64%) | HP:0001999 |
| Hypotonia | 5/11 (45%) | HP:0001252 |
| ADHD | 5/11 (45%) | HP:0007018 |
| Autism spectrum disorder | 4/11 (36%) | HP:0000729 |
| Motor stereotypies | 4/11 (36%) | HP:0000733 |
| Macrocephaly | 3/11 (27%) | HP:0000256 |
| Fifth-finger clinodactyly | 3/11 | HP:0004209 |
| 2–3 toe syndactyly | 3/11 | HP:0010621 |
| Clubfeet | 2/11 | HP:0001762 |

Facial dysmorphism included up/down-slanting palpebral fissures, depressed nasal bridge, posteriorly rotated ears, high-arched eyebrows, epicanthus, telecanthus, frontal bossing, micrognathia, and strabismus. Independent walking was delayed/variable (14 months to >2 years). **No epilepsy was reported in the cohort** — a potentially distinguishing negative feature. The abstract states: *"All 11 patients in our case series had a neurodevelopmental phenotype, whereby intellectual disability, delayed speech and language, and motor delay predominated."*

### Finding 5 — The 11 *de novo* variants (5 predicted LoF, 6 missense), absent from gnomAD

All 11 cohort variants are heterozygous, *de novo* (MANE transcript NM_006386.5 / NP_006377.2), and **absent from gnomAD v2.1.1 and v3.1.2**.

| Patient | Variant | Class |
|---|---|---|
| P1 | c.481_482del p.(Arg161Glyfs*7) | Frameshift (LoF) |
| P2 | c.997_998dup p.(Met333Ilefs*22) | Frameshift (LoF) |
| P3 | c.739-2A>G | Canonical splice acceptor (LoF) |
| P4 | c.953del p.(Arg318Hisfs*36) | Frameshift (LoF) |
| P5 | c.1380del p.(Asn462Metfs*16) | Frameshift (LoF) |
| P6 | c.1361A>G p.(Gln454Arg) | Missense |
| P7 | c.911G>A p.(Arg304His) | Missense |
| P8 | c.608C>T p.(Pro203Leu) | Missense |
| P9 | c.776A>G p.(Gln259Arg) | Missense |
| P10 | c.649A>G p.(Thr217Ala) | Missense |
| P11 | c.206C>A p.(Ala69Asp) | Missense |

Ascertainment was via GeneMatcher/collaboration (October 2019–August 2023); inclusion required a *de novo* missense or predicted-LoF variant absent from population databases: *"participants were eligible to join our case-series if they had a confirmed de novo variant in DDX17, either missense or predicted LoF (canonical splice site, frameshift, stop gained), and the variant was absent from population databases."* The disorder is autosomal dominant arising *de novo*; penetrance appears complete in reported carriers with variable expressivity.

### Finding 6 — Mechanism and affected neuroanatomy: disrupted cortical neuron migration and axon outgrowth

Cross-species functional data ([PMID: 39405200](https://pubmed.ncbi.nlm.nih.gov/39405200/)):

- **Mouse (in vivo):** *in utero* cortical electroporation with Ddx17 knockdown caused **delayed neuronal migration and decreased cortical axon complexity**: *"Knockdown of Ddx17 in electroporated mouse neurons in vivo showed delayed neuronal migration as well as decreased cortical axon complexity."*
- **Mouse (in vitro):** primary cortical neurons showed reduced axon outgrowth.
- **Xenopus tropicalis:** ddx17 crispants and heterozygous knockouts reproduced reduced axon outgrowth, decreased head/brain size, overt neurodevelopmental defects, and impaired neurobehavior.
- **Human (in vitro):** SH-SY5Y DDX17-knockdown transcriptomics showed significant enrichment of differentially expressed neurodevelopmental genes: *"Transcriptomic analysis identified a statistically significant number of differentially expressed genes involved in neurodevelopmental processes in DDX17-KD cells compared to control cells."*

**Affected structures:** developing cerebral cortex (UBERON:0000956); cortical projection/pyramidal neurons (CL:0000540 neuron; CL:0000679 glutamatergic neuron); axon/neuronal processes (GO:0030424). **Biological processes:** neuron migration (GO:0001764), axonogenesis/axon development (GO:0007409), regulation of neuron differentiation (GO:0045664), pri-miRNA processing (GO:0031053), regulation of alternative mRNA splicing (GO:0000381). **Subcellular:** nucleus/nucleoplasm (GO:0005634) and nucleolus (GO:0005730).

### Finding 7 — Haploinsufficient, LoF-intolerant gene; abnormal MRI in ~50%

DDX17 is **maximally constrained against loss of function** in gnomAD: 37.7 LoF variants expected, 1 observed, giving **pLI = 1.0** with a low LOEUF. Prior to this cohort, DDX17 had no established disease-gene relationship. The abstract notes: *"DDX17 is an RNA helicase shown to be involved in critical processes during the early phases of neuronal differentiation."* Neuroimaging: 8/11 had brain MRI; **4/8 (50%) were abnormal** — monolateral temporal cortical dysplasia, cerebral cortical asymmetry (left > right), right-sided and generalized non-specific demyelination, and periventricular white-matter hyperintensities; the other 4 were unremarkable. Patient 5's congenital macrocephaly normalized during infancy.

### Finding 8 — Mechanistic refinement: the REST–proneural-microRNA axis

Lambert et al. 2018 ([PMID: 29931089](https://pubmed.ncbi.nlm.nih.gov/29931089/)) showed DDX17 controls REST (RE1-silencing transcription factor) processes critical for early neuronal differentiation: *"the DEAD box RNA helicase DDX17 controls important REST-related processes that are critical during the early phases of neuronal differentiation."* Specifically:

1. DDX17 associates with REST and promotes its binding to a subset of REST-target neuronal gene promoters, co-regulating REST repression.
2. During differentiation, DDX17 is downregulated along with the REST complex, contributing to neuronal gene activation.
3. DDX17 and DDX5 regulate several **proneural microRNAs** that target the REST complex: *"DDX17 and its paralog DDX5 regulate the expression of several proneural microRNAs that are known to target the REST complex during neurogenesis, including miR-26a/b"* (miR-26a/b also directly regulate DDX17, forming a feedback loop).
4. DDX17 controls processing of intronic miRNAs (e.g., miR-26a2) via an intronic regulatory region affecting both miRNA processing and host-intron splicing.

### Finding 9 — Model organisms and orthologs

DDX17 is evolutionarily conserved. Ensembl orthologue protein identities and models:

| Species | Ortholog | Protein identity | Disease model |
|---|---|---|---|
| *Mus musculus* | Ddx17 (Gene 67040) | 98.8% | *In utero* electroporation knockdown → delayed migration, reduced axon complexity (strong recapitulation) |
| *Xenopus tropicalis* | ddx17 | 81.8% | CRISPR crispants + heterozygous KO → reduced axon outgrowth, small head/brain, behavioral impairment (good recapitulation) |
| *Danio rerio* | ddx17 | 72.7% | — |
| *Caenorhabditis elegans* | ddx-17 | 52.9% | Conserved pri-miRNA processing ([PMID: 26601717](https://pubmed.ncbi.nlm.nih.gov/26601717/)) |
| *Drosophila melanogaster* | Rm62 (single DDX5/DDX17 ortholog) | 43.0% | — |
| Human | SH-SY5Y (CVCL_0019) | — | DDX17-KD transcriptomic model |

The *Xenopus* heterozygous model is especially valuable: *"The axon outgrowth phenotype was replicated in crispant ddx17 tadpoles and in heterozygotes. Heterozygous tadpoles had clear neurodevelopmental defects and showed an impaired [neurobehavioral phenotype]."* This dominant model directly mirrors the human heterozygous dominant disease.

### Finding 10 — Identifiers, protein architecture, and variant–domain localization

**Identifiers:** MONDO:0700368 "DDX17-related neurodevelopmental disorder" (synonym "DDX17-related disorder"); OMIM phenotype MRD73; gene HGNC:2740, NCBI Gene 10521, Ensembl ENSG00000100201, UniProt Q92841, OMIM gene *608469. MeSH nearest terms: "Neurodevelopmental Disorders"/"Intellectual Disability"/"DEAD-box RNA Helicases." ICD-11 best fit LD90.Y / 6A00 (disorders of intellectual development); no disease-specific ICD-10/ICD-11 code exists.

**Protein (UniProt Q92841, 729-aa canonical p82; MANE NP_006377.2 p72 ~650 aa via downstream AUG):**

```
 N ── disordered ── Q motif ── Helicase ATP-binding ── Helicase C-terminal ── C-terminal transactivation/IDR ── C
        (Ala69)    (171-199)   (202-377, DEAD 325-328)  (405-552)             (547-729, YAP1 motif 718-726)
```

Mapping cohort missense variants (NP_006377.2 numbering, +79 offset to UniProt): **Pro203Leu, Thr217Ala, Gln259Arg** cluster within the Helicase ATP-binding/DEAD core (Gln259 adjacent to the DEAD-box motif); **Gln454Arg** lies in the Helicase C-terminal domain; **Arg304His** in the inter-domain linker; **Ala69Asp** in the N-terminal disordered region. Truncating variants are distributed across the helicase domains. The clustering of missense variants in the catalytic helicase core is consistent with disruption of ATPase/helicase function.

### Finding 11 — Epidemiology, inheritance, prognosis, counseling

**Epidemiology:** ultra-rare; the entire literature is one multinational case series of 11 patients ([PMID: 39405200](https://pubmed.ncbi.nlm.nih.gov/39405200/)), ascertained via GeneMatcher. Precise prevalence/incidence are unknown (not estimable; consistent with orphan designation <1/1,000,000). Cohort sex ratio 8M:3F (no established sex bias given small n; DDX17 is autosomal, so no inherent skew is expected — contrast X-linked DDX3X, which is female-biased).

**Inheritance:** autosomal dominant; all variants *de novo* and absent from gnomAD. Penetrance appears complete in reported heterozygotes, with variable expressivity (no/borderline ID to moderate ID). No inheritance, anticipation, founder effect, or consanguinity reported — *de novo* origin renders these largely irrelevant. Recurrence risk for unaffected parents is low (<1%, limited to rare germline mosaicism). The abstract supports this: *"we compiled a case series of 11 patients with neurodevelopmental phenotypes harbouring de novo monoallelic variants in DDX17."*

**Prognosis:** all 11 patients alive at median age 15 years (up to 23 years) — non-lethal, no evidence of reduced life expectancy. The course is static/non-progressive (developmental, not neurodegenerative). No malignancy or organ failure reported.

### Finding 12 — Diagnostics and management

**Diagnosis is molecular/genomic.** Because the phenotype (global developmental delay, ID, speech/motor delay ± ASD/ADHD, mild dysmorphism) is non-specific, DDX17-NDD is not clinically distinguishable and is diagnosed by identifying a *de novo* pathogenic/likely-pathogenic DDX17 variant on **exome (ES) or genome sequencing (GS)**, typically **trio-based** to establish *de novo* status — the method by which all 11 cases were found. Chromosomal microarray/karyotype are normal (no recurrent CNV). DDX17 now appears on expanded ID/NDD gene panels; single-gene testing is not first-line.

**Supportive workup:** brain MRI (abnormal in ~50%), developmental/cognitive assessment, ASD/ADHD screening, vision/hearing evaluation. No specific biochemical biomarker, enzyme assay, or metabolic abnormality is known; routine labs are normal.

**Differential diagnosis:** other DEAD/DEAH-box helicase NDDs — **DDX3X syndrome** (X-linked, female-predominant; [PMID: 40374608](https://pubmed.ncbi.nlm.nih.gov/40374608/), [PMID: 40418049](https://pubmed.ncbi.nlm.nih.gov/40418049/)), DHX30, DDX6, DDX23 — and the broad class of autosomal-dominant ID genes.

**Management:** no disease-specific or targeted therapy. Care is supportive and multidisciplinary — early intervention, special education, speech/language therapy, physical and occupational therapy for motor delay/hypotonia, behavioral/pharmacologic management of ADHD (e.g., methylphenidate) and ASD per standard guidelines, orthopedic management for clubfeet. No gene/RNA therapy or clinical trials for DDX17-NDD are registered as of 2026.

**Suggested NCIT terms:** Supportive Care (NCIT:C15277), Physical Therapy (NCIT:C15258), Speech Therapy, Occupational Therapy, Methylphenidate (NCIT:C62055).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A ***de novo* heterozygous variant** (frameshift, nonsense, canonical splice-site, or missense) arises in *DDX17* on chromosome 22q13.1. → *demonstrated*
2. This **reduces functional DDX17 dosage** — truncating/splice alleles via nonsense-mediated decay or loss of catalytic domains; missense alleles (clustered in the helicase ATP-binding/DEAD core) via impaired ATPase/helicase activity. Because DDX17 is LoF-intolerant (pLI = 1.0), one functional copy is insufficient → **haploinsufficiency**. → *inferred from constraint data + variant class*
3. Reduced DDX17 **disrupts its RNA-regulatory functions** in neurons: alternative splicing, pri-miRNA/Microprocessor processing, transcriptional co-regulation, and control of the **REST–proneural-microRNA axis**. → *demonstrated in neural cell models (PMID 29931089)*
4. **BRANCH A (REST axis):** impaired DDX17 mis-times REST-dependent repression and proneural-miRNA (miR-26a/b) expression → **dysregulated activation of neuronal differentiation genes**. → *demonstrated in vitro*
5. **BRANCH B (direct transcriptomic):** DDX17 loss produces a statistically significant set of **differentially expressed neurodevelopmental genes** (SH-SY5Y). → *demonstrated*
6. Converging downstream, the neuron fails to execute its developmental program correctly → **delayed radial neuronal migration and reduced axon outgrowth/complexity** in the developing cerebral cortex. → *demonstrated in mouse in vivo + Xenopus*
7. Aberrant cortical wiring (sometimes visible as cortical dysplasia/asymmetry and white-matter changes on MRI) → **intellectual disability, speech/language delay, motor delay, hypotonia, ADHD, ASD features, and mild dysmorphism**. → *clinical correlation*

```
 DDX17 de novo variant (22q13.1)
        │  haploinsufficiency (pLI=1.0)
        ▼
 ↓ DDX17 RNA-helicase activity in neurons
        │
   ┌────┴─────────────────────────┐
   ▼                              ▼
 REST–proneural-miRNA axis    Global splicing / miRNA /
 (miR-26a/b, REST targets)    transcriptomic dysregulation
   │                              │
   └──────────────┬───────────────┘
                  ▼
   Disrupted neuronal differentiation program
                  ▼
   Delayed cortical neuron migration + ↓ axon outgrowth
                  ▼
   Abnormal cortical circuitry (MRI: dysplasia/asymmetry/WM changes)
                  ▼
   ID, speech/language delay, motor delay, hypotonia, ADHD, ASD, dysmorphism
```

**Upstream vs downstream:** the mutation and haploinsufficiency are the most upstream events; RNA-regulatory dysfunction (splicing, miRNA, REST) is the proximate molecular mechanism; neuronal migration/axon defects are the cellular readout; clinical phenotypes are the most downstream. **Cell types:** cortical projection/glutamatergic neurons (CL:0000679), neurons broadly (CL:0000540). **Subcellular:** nucleus (GO:0005634), nucleolus (GO:0005730) — consistent with the p82 isoform's nucleolar/membraneless-organelle localization.

### Comparison with DDX3X syndrome (differential context)

| Feature | DDX17-NDD | DDX3X syndrome |
|---|---|---|
| Gene / location | DDX17 / 22q13.1 (autosomal) | DDX3X / Xp11.4 (X-linked, escapes XCI) |
| Inheritance | AD, *de novo* | X-linked, mostly *de novo*, female-predominant |
| Sex bias | None expected (autosomal) | Strongly female-predominant |
| Protein class | DEAD-box RNA helicase | DEAD-box RNA helicase |
| Mechanism | Haploinsufficiency; REST/splicing/miRNA | LoF; stress-granule/ribosome biogenesis; sex-dimorphic ([PMID: 40374608](https://pubmed.ncbi.nlm.nih.gov/40374608/), [PMID: 40418049](https://pubmed.ncbi.nlm.nih.gov/40418049/)) |
| Epilepsy | Not reported (n=11) | Common |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [39405200](https://pubmed.ncbi.nlm.nih.gov/39405200/) | *Monoallelic de novo variants in DDX17 cause a neurodevelopmental disorder* | **Defining study** — cohort, variants, phenotype, cross-species functional validation (Findings 1,2,4,5,6,7,9,11,12) |
| [29931089](https://pubmed.ncbi.nlm.nih.gov/29931089/) | *DDX17 controls REST transcriptional activity and proneural microRNAs* | Upstream neuronal-differentiation mechanism; REST–miR-26a/b axis (Finding 8) |
| [31851931](https://pubmed.ncbi.nlm.nih.gov/31851931/) | *RNA specificity and autoregulation of DDX17* | DDX17 enzymatic identity and miRNA maturation role (Finding 3) |
| [24275493](https://pubmed.ncbi.nlm.nih.gov/24275493/) | *Ddx5/Ddx17 in steroid hormone signaling* | Splicing-regulator / co-activator role (Finding 3) |
| [41322492](https://pubmed.ncbi.nlm.nih.gov/41322492/) | *DDX17 in chronic non-infectious diseases* | High neuronal/cardiomyocyte expression (Finding 3) |
| [26947125](https://pubmed.ncbi.nlm.nih.gov/26947125/) | *p72/DDX17 and miR-132 processing* | miRNA-processing specificity (Finding 3) |
| [26601717](https://pubmed.ncbi.nlm.nih.gov/26601717/) | *DDX-17 in C. elegans pri-miRNA processing* | Conserved miRNA role; model organism (Findings 3,9) |
| [27478153](https://pubmed.ncbi.nlm.nih.gov/27478153/) | *p72/DDX17 and KHSRP regulate Ago2* | miRNA-pathway regulation (Finding 3) |
| [32065632](https://pubmed.ncbi.nlm.nih.gov/32065632/) | *DDX17 isoforms and membraneless organelles* | p72/p82 isoforms, nucleolar/IDR localization (Findings 3,10) |
| [22713328](https://pubmed.ncbi.nlm.nih.gov/22713328/), [22266867](https://pubmed.ncbi.nlm.nih.gov/22266867/) | *DEAD-box helicases as transcription cofactors; NFAT5 control* | Transcriptional co-regulation (Finding 3) |
| [40374608](https://pubmed.ncbi.nlm.nih.gov/40374608/), [40418049](https://pubmed.ncbi.nlm.nih.gov/40418049/) | *DDX3X neurodevelopmental disorder* | Differential diagnosis; helicase-NDD comparison (Finding 12) |
| [42458834](https://pubmed.ncbi.nlm.nih.gov/42458834/) | *DDX3X overexpression toxicity in mice* | Dosage-sensitivity caution for future therapeutics |

The evidence base is dominated by one high-quality human-genetics study with strong multi-model functional validation (mouse in vivo/in vitro, *Xenopus*, human neuroblastoma), supplemented by a well-established basic-science literature on DDX17's RNA-regulatory biology. No study contradicts the core gene–disease relationship; the main limitation is the single small cohort.

---

## Limitations and Knowledge Gaps

- **Single small cohort (n = 11).** All clinical knowledge derives from one case series; phenotype frequencies have wide confidence intervals and may shift as more patients are identified. Ascertainment via GeneMatcher biases toward more severe/recognizable phenotypes.
- **No formal epidemiology.** Prevalence and incidence are unknown; no registry exists.
- **Genotype–phenotype correlation unestablished.** With 5 LoF and 6 missense variants across 11 patients, there is insufficient power to determine whether LoF and missense alleles produce different severities, or whether missense variants act purely by LoF versus a dominant-negative/gain-of-function mechanism (DDX17 heterodimerizes with DDX5, raising a theoretical dominant-negative possibility not yet tested).
- **Penetrance and expressivity** are assumed complete/variable from *de novo* cases only; no multigenerational or mosaic families have been characterized.
- **Mechanistic gaps.** The REST–miRNA axis (PMID 29931089) and the migration/axon phenotype (PMID 39405200) are each demonstrated, but the direct causal link between the specific patient variants and REST-axis dysregulation in human neurons has not been shown. Which specific mis-spliced transcripts or dysregulated miRNAs drive the cortical phenotype remains unknown.
- **No disease-specific biomarker, imaging signature, or natural-history data** beyond median age 15 years.
- **No therapeutics.** No targeted treatment, and dosage-restoration strategies carry theoretical risk given DEAD-box helicase dosage sensitivity ([PMID: 42458834](https://pubmed.ncbi.nlm.nih.gov/42458834/): *"DDX3X overexpression can cause rapid transgene-driven, tissue-specific toxicity, underscoring the need for tight DDX3X gene dosage control."*).
- **Absence of epilepsy** is based on n = 11 and may not hold in larger cohorts.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the cohort** via GeneMatcher/MatchmakerExchange and establish a DDX17-NDD patient registry to refine phenotype frequencies, define natural history, and detect rarer features (e.g., seizures, organ involvement).
2. **Functional dissection of missense alleles:** biochemical ATPase/helicase assays and DDX5-heterodimerization assays for each missense variant (Ala69Asp, Pro203Leu, Thr217Ala, Gln259Arg, Arg304His, Gln454Arg) to classify them as pure LoF vs dominant-negative vs hypomorphic. Structural modeling (AlphaFold/cryo-EM) of variants in the helicase core.
3. **Patient-derived iPSC cortical organoids** carrying index variants to test, in a human context, whether REST-axis dysregulation, mis-splicing, and migration/axon defects are recapitulated — bridging PMID 29931089 and PMID 39405200.
4. **Transcriptome + miRNome profiling** (RNA-seq + small-RNA-seq) of patient neurons to identify the specific mis-spliced transcripts and dysregulated proneural miRNAs (e.g., miR-26a/b) driving the phenotype; integrate with CLIP-seq for direct DDX17 RNA targets.
5. **Generate a Ddx17 heterozygous mouse model** (constitutive and conditional forebrain-neuron) for behavioral phenotyping and preclinical testing, complementing the existing acute-knockdown and *Xenopus* models.
6. **Deep phenotyping of MRI** across a larger cohort to determine whether cortical dysplasia/asymmetry is a consistent, diagnostically useful signature.
7. **ClinVar/ClinGen curation:** submit a formal ClinGen gene–disease validity assessment and establish variant-interpretation guidelines (e.g., whether the helicase-core missense region constitutes a PM1 hotspot).

---

*Report compiled from 12 confirmed findings and 23 reviewed papers over 5 investigation iterations. Primary evidence: Seaby et al. (PMID 39405200) and the DDX17 RNA-biology literature. All quoted text is verbatim from cited abstracts.*


## Artifacts

- [OpenScientist final report](DDX17-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DDX17-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

32 of 33 terms resolved to a current term; the rest could not be looked up either way.