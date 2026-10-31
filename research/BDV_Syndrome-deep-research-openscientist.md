---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-21T03:37:10.812785'
end_time: '2026-10-21T03:50:34.432515'
duration_seconds: 803.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: BDV Syndrome
  mondo_id: MONDO:0859150
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 23
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 4
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: BDV_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: BDV_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BDV Syndrome
- **MONDO ID:** MONDO:0859150 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **BDV Syndrome** covering all of the
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

# BDV Syndrome (Blakemore–Durmaz–Vasileiou Syndrome): Comprehensive Disease Characterization

**Disease:** BDV Syndrome | **MONDO ID:** MONDO:0859150 | **Gene:** *CPE* (Carboxypeptidase E) | **Inheritance:** Autosomal recessive | **Category:** Mendelian

---

## Summary

**BDV syndrome (Blakemore–Durmaz–Vasileiou syndrome; MONDO:0859150) is an ultra-rare autosomal-recessive Mendelian disorder caused by biallelic loss-of-function (LoF) variants in *CPE*, the gene encoding carboxypeptidase E.** CPE is the exopeptidase that performs the final C-terminal trimming step in prohormone/proneuropeptide maturation, removing C-terminal basic residues (Lys/Arg) left behind by the prohormone convertases. It also doubles as a secretory-granule sorting receptor and as a neurotrophic/neuroprotective factor (Neurotrophic factor-α1, NF-α1). When CPE function is abolished, bioactive peptides across many neuroendocrine systems — insulin, POMC-derived α-MSH, and appetite/glucose/reproduction-regulating peptides — fail to mature, while inactive intermediates accumulate.

The clinical consequence is a near-fully-penetrant, **Prader-Willi-like triad**: childhood-onset severe hyperphagic obesity, intellectual disability/neurodevelopmental delay, and hypogonadotropic hypogonadism. Abnormal glucose homeostasis and type 2 diabetes are frequent, and elevated plasma proinsulin is a mechanistically grounded candidate biomarker. The disorder has been reported in fewer than ~15 affected individuals from roughly six consanguineous families worldwide (British/European, Turkish, Syrian, Egyptian, Pakistani ancestries). Diagnosis is made by exome or genome sequencing, generally after Prader-Willi syndrome (PWS) has been excluded, because the phenotype is clinically mistaken for PWS.

There is **no approved disease-specific therapy**; management is supportive and multidisciplinary (dietary/hyperphagia management, diabetes treatment, sex-hormone replacement, developmental/educational support). The MC4R agonist setmelanotide — approved for other leptin-melanocortin-pathway monogenic obesities (POMC, PCSK1, LEPR deficiency; Bardet-Biedl syndrome) — is a biologically rational but unvalidated candidate, since CPE acts upstream of α-MSH. Two mouse models, *Cpe*^fat/fat^ and *Cpe*-knockout, faithfully recapitulate the human metabolic, reproductive, and cognitive phenotypes and reveal CPE's role in hippocampal CA3 neuron survival.

---

## Key Findings

### Finding 1 — BDV syndrome is caused by biallelic loss-of-function *CPE* variants (autosomal recessive)

Three independent families/cohorts established that biallelic LoF *CPE* variants co-segregate with a consistent phenotype of morbid/childhood-onset obesity, intellectual disability/neurodevelopmental delay, and hypogonadotropic hypogonadism. The syndrome was formally named and standardized against Human Phenotype Ontology terms by Durmaz and colleagues: *"Comparison of clinical features with previously described cases and standardization according to the Human Phenotype Ontology terms indicated a recognizable clinical phenotype, which we termed Blakemore-Durmaz-Vasileiou (BDV) syndrome"* ([PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/)).

The first human case was a morbidly obese female from a consanguineous family homozygous for a truncating mutation (c.76_98del; p.E26RfsX68), with *"no CPE expression in whole blood-derived RNA from the proband, consistent with nonsense-mediated decay"* ([PMID: 26120850](https://pubmed.ncbi.nlm.nih.gov/26120850/)). A second independent family carried a homozygous nonsense c.405C>A (p.Y135\*) mutation in three affected siblings ([PMID: 32936766](https://pubmed.ncbi.nlm.nih.gov/32936766/)). Additional pathogenic alleles include c.361C>T p.(Arg121\*) and c.994del p.(Ser333Alafs\*22) (Bosch 2021, [PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/)). All reported families were consanguineous, and proband RNA studies support nonsense-mediated decay as the molecular mechanism (true null alleles).

**Reported pathogenic *CPE* variants**

| Variant (cDNA) | Protein | Type | Zygosity | Source |
|---|---|---|---|---|
| c.76_98del | p.E26RfsX68 | Frameshift (truncating) | Homozygous | [PMID: 26120850](https://pubmed.ncbi.nlm.nih.gov/26120850/) |
| c.405C>A | p.Y135\* | Nonsense | Homozygous | [PMID: 32936766](https://pubmed.ncbi.nlm.nih.gov/32936766/) |
| c.361C>T | p.(Arg121\*) | Nonsense (recurrent/founder) | Homozygous | [PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/) |
| c.994del | p.(Ser333Alafs\*22) | Frameshift | Homozygous | [PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/) |

### Finding 2 — Mechanism: CPE loss abolishes C-terminal prohormone processing, accumulating inactive intermediates and depleting mature bioactive peptides

CPE is *"an exopeptidase that removes C-terminal basic amino acids from intermediates to produce bioactive peptides. The mutation renders the enzyme inactive and unstable. The absence of Cpe activity in these mutants leads to abnormal processing of many peptides, with elevated levels of intermediates and greatly reduced levels of the mature peptides"* ([PMID: 23442571](https://pubmed.ncbi.nlm.nih.gov/23442571/)). It is *"a prohormone-processing enzyme and peripheral membrane protein of endocrine/neuroendocrine secretory granules"* that also functions as a sorting receptor and co-aggregates with granule content proteins at acidic pH (~5.5–5.8) ([PMID: 9813022](https://pubmed.ncbi.nlm.nih.gov/9813022/)).

Because CPE *"is a peptide processing enzyme, involved in cleaving numerous peptide precursors, including neuropeptides and hormones involved in appetite control and glucose metabolism"* ([PMID: 26120850](https://pubmed.ncbi.nlm.nih.gov/26120850/)), its loss directly links the molecular defect to the appetite, glucose, reproductive, and cognitive phenotypes observed in patients. This is a **loss-of-function** mechanism affecting the terminal, convergent step of neuroendocrine peptide maturation — explaining the pleiotropic, multi-system presentation.

### Finding 3 — Mouse models (*Cpe*^fat/fat^ and *Cpe*-knockout) recapitulate the human disease and reveal a neuroprotective role

*Cpe*^fat/fat^ mice (Ser202Pro point mutation) *"develop obesity, diabetes and infertility in adulthood"* ([PMID: 23442571](https://pubmed.ncbi.nlm.nih.gov/23442571/)), plus age-dependent depressive-like (~60 days) and anxiety-like (>90 days) behaviours. *Cpe*-knockout mice show memory consolidation deficits, absent long-term potentiation (LTP), and *"marked degeneration specifically of the pyramidal neurons in the hippocampal CA3 region which normally expresses high levels of CPE"* from 4 weeks of age ([PMID: 18570185](https://pubmed.ncbi.nlm.nih.gov/18570185/)). Neuron-specific Camk2a-Cre conditional knockout reproduces learning/memory deficits and neurodegeneration ([PMID: 37100779](https://pubmed.ncbi.nlm.nih.gov/37100779/)).

Genetic background strongly modifies severity: *"On the HRS/J (HRS) inbred strain background, mice homozygous for the fat mutation exhibit early onset hyperinsulinemia followed by postpubertal moderate obesity without hyperglycemia. In contrast, on the C57BLKS/J (BKS) genetic background, fat/fat mice become severely obese, hyperinsulinemic, and hyperglycemic"* ([PMID: 15870393](https://pubmed.ncbi.nlm.nih.gov/15870393/)). This demonstrates that genetic modifiers can shape the obesity/diabetes phenotype and provides a model-based rationale for variable expressivity. Human patient phenotypes (obesity, intellectual disability, abnormal glucose homeostasis, hypogonadotropic hypogonadism) explicitly recapitulate the fat/fat and Cpe-KO models.

### Finding 4 — CPE loss disrupts proinsulin processing, elevating plasma proinsulin (candidate biomarker)

Human CPE-mutation carriers *"have elevated plasma proinsulin and develop severe obesity and hyperglycemia"* ([PMID: 37364047](https://pubmed.ncbi.nlm.nih.gov/37364047/)). A pancreatic β-cell-specific knockout (βCpeKO; Cpefl/fl × Ins1Cre/+) model showed that these mice *"lack mature insulin granules and have elevated proinsulin in plasma"* ([PMID: 37364047](https://pubmed.ncbi.nlm.nih.gov/37364047/)), though glucose-/KCl-stimulated secretion remained intact and spontaneous diabetes did not develop on high-fat diet. However, β-cells showed reduced mitochondrial membrane potential, increased reactive oxygen species, reduced MafA, elevated Aldh1a3 under high-glucose stress, and accelerated hyperglycemia after low-dose streptozotocin — indicating increased β-cell vulnerability rather than fixed failure. CPE's role in proinsulin processing is corroborated in human islets, where *"Laser capture microdissection followed by mass spectrometry revealed reductions in the proinsulin processing enzymes prohormone convertase 1/3 (PC1/3) and carboxypeptidase E (CPE) in T1D donors"* ([PMID: 31442418](https://pubmed.ncbi.nlm.nih.gov/31442418/)).

**Diagnostic implication:** an elevated **proinsulin-to-insulin ratio** is a mechanistically grounded biochemical signature of CPE deficiency and a candidate screening/diagnostic biomarker worth prospective evaluation.

### Finding 5 — CPE's oncogenic splice variant (CPE-ΔN) is a distinct biology, not the BDV mechanism

An N-terminal truncated splice variant *"(CPE-ΔN) has been cloned and found to be highly expressed in malignant tumors and cell lines derived from prostate, breast, liver and lung cancers and gliomas"* ([PMID: 35988818](https://pubmed.ncbi.nlm.nih.gov/35988818/)). CPE-ΔN acts in the nucleus with HDACs to drive metastasis — e.g., it *"has recently been recognized as an independent predictor for the recurrence and metastasis of lung adenocarcinoma"* by repressing E-cadherin via stabilizing the Snail-HDAC complex ([PMID: 32266100](https://pubmed.ncbi.nlm.nih.gov/32266100/)). This is a **gain-of-function, isoform-specific** oncogenic role distinct from the recessive LoF that causes BDV syndrome. It is important context for interpreting *CPE* literature: elevated CPE/CPE-ΔN in cancer is not relevant to the loss-of-function disease, and the two should not be conflated.

### Finding 6 — Phenotype spectrum: a near-fully-penetrant triad with abnormal glucose homeostasis

Across the ~8–11 clearly reported affected individuals (Alsters 2015 n=1; Durmaz 2021 n=3; Bosch 2021 n=4 from 3 families plus 4 previously reported from 2 families), essentially all exhibit the core triad of (1) childhood-onset morbid obesity with hyperphagia, (2) intellectual disability/neurodevelopmental delay, and (3) hypogonadotropic hypogonadism, described as *"core clinical features including morbid obesity, neurodevelopmental delay, and hypogonadotropic hypogonadism"* ([PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/)). An independent family confirmed *"three siblings with obesity, intellectual disability and hypogonadotropic hypogonadism"* ([PMID: 32936766](https://pubmed.ncbi.nlm.nih.gov/32936766/)). The clinical overlap with Prader-Willi syndrome drives the diagnostic pathway: *"After excluding Prader-Willi syndrome (PWS), exome sequencing was performed in both Syrian siblings"* ([PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/)).

**Phenotype → HPO term mapping**

| Phenotype | HPO term | Frequency | Onset |
|---|---|---|---|
| Childhood-onset morbid obesity | HP:0025499 (Childhood-onset obesity) | ~Universal | Childhood |
| Hyperphagia | HP:0002591 (Polyphagia) | Frequent | Childhood |
| Intellectual disability | HP:0001249 | ~Universal | Childhood |
| Global developmental delay | HP:0001263 | Frequent | Infancy/childhood |
| Hypogonadotropic hypogonadism | HP:0000044 | ~Universal | Peripubertal |
| Type 2 diabetes / abnormal glucose homeostasis | HP:0005978 / HP:0011014 | Variable/frequent | Childhood–adult |
| Behavioral abnormality (model-predicted) | HP:0000708 | Inferred (mouse) | — |
| Memory impairment (model-predicted) | HP:0002354 | Inferred (mouse) | — |

### Finding 7 — Identifiers, inheritance, and ultra-rare epidemiology

**Gene identifiers:** *CPE* (carboxypeptidase E; aka CPH, NF-α1): HGNC:2303; NCBI Gene 1363; Ensembl ENSG00000109472; cytoband 4q32.3; OMIM gene \*114855; UniProt P16870 (CBPE_HUMAN). **Disease:** MONDO:0859150; synonyms "Blakemore-Durmaz-Vasileiou syndrome," "CPE deficiency," "carboxypeptidase E deficiency."

**Inheritance and epidemiology:** autosomal recessive (biallelic LoF). The disorder is ultra-rare — fewer than ~15 affected individuals across ~6 families to date. Durmaz/Bosch describe *"4 affected individuals from 3 unrelated consanguineous families, 2 siblings of Syrian, 1 of Egyptian, and 1 of Pakistani descent, all harboring novel homozygous CPE LoF variants"* ([PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/)). A recurrent/possible founder allele is noted: *"Three individuals from 2 families shared the same CPE homozygous truncating variant c.361C > T, p.(Arg121\*)"* ([PMID: 34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/)). The first reported case involved *"a morbidly obese female from a consanguineous family… homozygosity for a truncating mutation of the CPE gene"* ([PMID: 26120850](https://pubmed.ncbi.nlm.nih.gov/26120850/)). Biallelic CPE LoF is essentially absent in gnomAD (no reported homozygous healthy LoF carriers), consistent with a recessive, highly penetrant disorder. No formal population prevalence/incidence estimate exists.

### Finding 8 — Treatment is supportive; setmelanotide is a mechanistically rational candidate

No disease-specific or curative therapy exists. Management is supportive and organ-directed: dietary/caloric restriction and hyperphagia management, type 2 diabetes treatment, sex-hormone replacement for hypogonadotropic hypogonadism (induction of puberty/fertility support), and developmental/educational/behavioral support for intellectual disability. The MC4R agonist setmelanotide is approved for upstream leptin-melanocortin-pathway defects — *"those with LEPR, PCSK1, or POMC deficiency can now be treated with the MC4R agonist setmelanotide"* ([PMID: 39777073](https://pubmed.ncbi.nlm.nih.gov/39777073/)) — and *"compensates for upstream gene defects in the brain leptin-melanocortin pathway and reduces hyperphagia and obesity in selected monogenic obesity forms and Bardet-Biedl syndrome (BBS)"* ([PMID: 40903014](https://pubmed.ncbi.nlm.nih.gov/40903014/)). Because CPE acts upstream (producing α-MSH), setmelanotide is biologically plausible but not yet approved/validated for CPE deficiency. Bariatric surgery has limited durable benefit in hyperphagic syndromic obesity: *"Benefits of bariatric surgery may be less durable"* in such patients ([PMID: 35416416](https://pubmed.ncbi.nlm.nih.gov/35416416/)).

### Finding 9 — CPE/NF-α1 is a neurotrophic/neuroprotective factor enriched in hippocampal CA3

CPE is also known as Neurotrophic factor-α1 (NF-α1). A dedicated review states that *"Families carrying null and homozygous non-sense mutations of the NF-α1/CPE gene share common clinical features including childhood onset obesity, type 2 diabetes, impaired intellectual abilities and hypogonadotrophic hypogonadism"* and that *"NF-α1/CPE expression is enriched in CA3 neurons of the hippocampus"* ([PMID: 35711734](https://pubmed.ncbi.nlm.nih.gov/35711734/)). CPE exerts enzyme-independent neuroprotection — *"overexpression of CPE in cultured hippocampal neurons protected them against H(2)O(2) oxidative-stress induced cell death"* ([PMID: 18570185](https://pubmed.ncbi.nlm.nih.gov/18570185/)). This CA3-enriched, neuroprotective role provides the mechanistic basis linking CPE loss to intellectual disability and the model-predicted depression/anxiety/memory phenotypes.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (from initiating lesion to clinical manifestation)

```
1. Biallelic LoF variant in CPE (nonsense/frameshift, e.g., p.Arg121*, p.Y135*)
        │  leads to →
2. Nonsense-mediated decay of CPE mRNA → complete absence of CPE protein
        │  results in →
3. Loss of the terminal C-terminal-basic-residue trimming step of prohormone
   maturation (and loss of CPE's granule-sorting + neurotrophic functions)
        │  results in →
4. Accumulation of inactive peptide intermediates + depletion of mature
   bioactive peptides across multiple neuroendocrine systems
        │
        ├── BRANCH A (hypothalamic leptin–melanocortin) → deficient α-MSH
        │        → impaired MC4R satiety signalling [inferred]
        │        → hyperphagia → childhood-onset severe obesity (HP:0025499)
        │
        ├── BRANCH B (pancreatic β-cell) → impaired proinsulin C-terminal
        │        trimming → elevated plasma proinsulin, defective mature
        │        insulin granules → β-cell stress/vulnerability
        │        → abnormal glucose homeostasis / type 2 diabetes (HP:0005978)
        │
        ├── BRANCH C (hypothalamic–pituitary–gonadal) → deficient processing
        │        of reproductive neuropeptides → hypogonadotropic
        │        hypogonadism (HP:0000044)
        │
        └── BRANCH D (hippocampus/CNS) → loss of NF-α1 neurotrophic/neuro-
                 protective support, CA3 pyramidal neuron vulnerability
                 → intellectual disability (HP:0001249); (mouse-inferred:
                 memory deficits, depression/anxiety-like behaviour)
```

Steps 1–4 are demonstrated in humans (genetics, absent expression) and mice (peptide processing). Branch A's MC4R-satiety link is inferred by analogy to the leptin-melanocortin pathway rather than directly demonstrated in CPE patients. Branch D's cognitive mechanism is strongly supported in mouse models and inferred for the human intellectual disability.

### Upstream vs downstream, cell types, and processes

- **Upstream (initiating):** the *CPE* null genotype and absent enzyme/sorting/neurotrophic activity.
- **Downstream (effector):** tissue-specific peptide deficiencies producing each clinical branch.
- **Cell types involved (CL terms):** pancreatic β-cell (CL:0000169), hypothalamic neurons/POMC neurons, hippocampal CA3 pyramidal neurons (CL:0000598, pyramidal neuron), photoreceptors (mouse retinal phenotype, [PMID: 16219026](https://pubmed.ncbi.nlm.nih.gov/16219026/)).
- **Subcellular compartment (GO CC):** secretory granule (GO:0030141), regulated secretory pathway.
- **Biological processes (GO BP):** peptide hormone processing (GO:0016486), neuropeptide signaling (GO:0007218), insulin processing (GO:0030070), regulation of feeding behavior (GO:0033059), neuron development/survival.
- **Anatomy (UBERON):** hypothalamus (UBERON:0001898), pituitary gland (UBERON:0000007), pancreatic islet (UBERON:0000006), hippocampus/CA3 (UBERON:0003881), retina (UBERON:0000966).

### Section-by-section synthesis against the research template

- **Disease information:** autosomal-recessive CPE deficiency; identifiers as in Finding 7; information is derived from aggregated disease-level case reports and model-organism studies (not large EHR cohorts).
- **Etiology:** monogenic (biallelic *CPE* LoF); principal non-genetic "risk factor" is **consanguinity**, which raises homozygosity; no environmental cause. Genetic modifiers (mouse strain background) influence severity.
- **Phenotypes:** see Finding 6 table.
- **Genetic/molecular:** truncating nonsense/frameshift variants → NMD → null; LoF consequence; CPE-ΔN oncogenic isoform is a separate biology (Finding 5).
- **Environmental/infectious:** none implicated. (Note: "BDV" also abbreviates Borna disease virus and Border disease virus/Bovine viral diarrhea in the literature — these are **unrelated** to BDV *syndrome* and were correctly excluded.)
- **Mechanism/pathophysiology:** causal chain above.
- **Anatomy:** hypothalamus, pituitary, pancreatic islet, hippocampus; multi-system (nervous, endocrine, reproductive).
- **Temporal development:** congenital genetic basis; obesity/developmental delay manifest in childhood; hypogonadism peripubertal; chronic lifelong course.
- **Inheritance/population:** AR; high penetrance; enriched in consanguineous families (Finding 7).
- **Diagnostics:** exome/genome sequencing after PWS exclusion; biochemical clue = elevated proinsulin / proinsulin:insulin ratio.
- **Prognosis:** chronic, non-fatal in short term but with obesity/diabetes morbidity and intellectual disability; natural history poorly quantified.
- **Treatment/prevention:** supportive; genetic counseling and cascade/carrier testing in consanguineous families; setmelanotide a rational candidate.
- **Other species/models:** mouse *Cpe*^fat/fat^ and *Cpe*-KO (Finding 3); CPE is highly conserved.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [34383079](https://pubmed.ncbi.nlm.nih.gov/34383079/) | *BDV Syndrome: An Emerging Syndrome…Resembling Prader-Willi* | Human clinical | Names syndrome; triad; consanguinity; recurrent p.Arg121\* (F1, F6, F7) |
| [26120850](https://pubmed.ncbi.nlm.nih.gov/26120850/) | *Truncating Homozygous CPE Mutation in Morbidly Obese Female* | Human clinical | First case; NMD; substrate/appetite link (F1, F2, F7) |
| [32936766](https://pubmed.ncbi.nlm.nih.gov/32936766/) | *New Obesity Syndrome…CPE in Three Siblings* | Human clinical | Independent family; homozygous p.Y135\* (F1, F6) |
| [23442571](https://pubmed.ncbi.nlm.nih.gov/23442571/) | *Anxiety-like behaviours in Cpe(fat/fat) mice* | Model organism | CPE enzymology; fat/fat metabolic + behavioral phenotype (F2, F3) |
| [18570185](https://pubmed.ncbi.nlm.nih.gov/18570185/) | *Absence of CPE → hippocampal degeneration & memory deficits* | Model organism | CA3 degeneration; neuroprotection (F3, F9) |
| [15870393](https://pubmed.ncbi.nlm.nih.gov/15870393/) | *Genetic modifiers interact with Cpe(fat)* | Model organism | Strain-dependent severity (F3) |
| [9813022](https://pubmed.ncbi.nlm.nih.gov/9813022/) | *CPE co-aggregates with granule proteins at acidic pH* | In vitro | Granule sorting/biology (F2) |
| [37364047](https://pubmed.ncbi.nlm.nih.gov/37364047/) | *Deletion of CPE in β-cells disrupts proinsulin processing* | Model organism + human | Elevated proinsulin biomarker; β-cell vulnerability (F4) |
| [31442418](https://pubmed.ncbi.nlm.nih.gov/31442418/) | *Proinsulin processing abnormalities in T1D islets* | Human | CPE role in human proinsulin processing (F4) |
| [35988818](https://pubmed.ncbi.nlm.nih.gov/35988818/) | *CPE and its splice variants in cancer* | Review | Oncogenic CPE-ΔN (distinct biology) (F5) |
| [32266100](https://pubmed.ncbi.nlm.nih.gov/32266100/) | *CPEΔN represses E-cadherin via Snail-HDAC* | In vitro/human | Gain-of-function metastasis role (F5) |
| [35711734](https://pubmed.ncbi.nlm.nih.gov/35711734/) | *NF-α1/CPE in Neuroprotection and Depression* | Review | Four-feature phenotype; CA3 enrichment (F9) |
| [37100779](https://pubmed.ncbi.nlm.nih.gov/37100779/) | *CPE conditional KO: learning/memory deficits* | Model organism | Neuron-specific cognitive phenotype (F9) |
| [39777073](https://pubmed.ncbi.nlm.nih.gov/39777073/) | *Precision medicine in rare genetic obesity* | Review | Setmelanotide for upstream pathway defects (F8) |
| [40903014](https://pubmed.ncbi.nlm.nih.gov/40903014/) | *Setmelanotide impact in Bardet-Biedl* | Clinical | Setmelanotide mechanism (F8) |
| [35416416](https://pubmed.ncbi.nlm.nih.gov/35416416/) | *Bariatric outcomes in PWS/hyperphagic disorders* | Review | Limited durability of surgery (F8) |
| [16219026](https://pubmed.ncbi.nlm.nih.gov/16219026/) | *CPE required for photoreceptor synaptic transmission* | Model organism | Additional neural role (context) |

**Note on "BDV" nomenclature:** Several retrieved papers (e.g., [PMID: 24170181](https://pubmed.ncbi.nlm.nih.gov/24170181/), [PMID: 22290118](https://pubmed.ncbi.nlm.nih.gov/22290118/), [PMID: 37898798](https://pubmed.ncbi.nlm.nih.gov/37898798/)) concern **Borna disease virus** or **Border/Bovine viral diarrhea virus** — unrelated to BDV *syndrome*. These were correctly identified as homonyms and excluded from the disease model.

---

## Limitations and Knowledge Gaps

1. **Very small patient base (<15 individuals).** All phenotype frequencies, penetrance, and expressivity estimates are derived from case reports of consanguineous families; ascertainment bias toward severe presentations is likely. No formal prevalence/incidence exists.
2. **No natural-history data.** Disease course, progression rate, survival, long-term complications, and quality-of-life outcomes are not systematically characterized in humans.
3. **Biomarker unvalidated prospectively.** Elevated proinsulin / proinsulin:insulin ratio is mechanistically grounded and observed, but not established as a validated diagnostic/screening test with sensitivity/specificity data.
4. **Human cognitive/behavioral mechanism inferred from mice.** Depression/anxiety-like and memory phenotypes are robustly demonstrated in *Cpe* models but not formally characterized in patients; the human intellectual disability mechanism is inferred from CA3/neurotrophic biology.
5. **Therapeutics untested.** Setmelanotide is biologically rational but has no reported use in CPE deficiency; its efficacy depends on intact downstream MC4R signalling and sufficient α-MSH-independent response.
6. **Genotype–phenotype correlations unknown.** With only truncating null alleles reported, the phenotypic consequences of hypomorphic/missense *CPE* variants, and the role of modifier loci (as seen in mice), are undefined in humans.
7. **Branch A (α-MSH/MC4R) not directly demonstrated** in CPE patients — the satiety-signalling step is inferred from pathway analogy.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for biallelic *CPE* LoF to aggregate phenotype frequencies, natural history, penetrance, expressivity, and QoL data across the dispersed consanguineous families.
2. **Prospectively validate plasma proinsulin and the proinsulin:insulin ratio** as a diagnostic/screening biomarker in suspected cases (and in PWS-like, PWS-excluded obesity), with defined cutoffs and test performance.
3. **Pilot setmelanotide (MC4R agonist) in CPE deficiency** — a biologically rational n-of-few trial measuring hyperphagia, weight, and metabolic endpoints; include biomarker response (α-MSH-independent pathway intact distal to CPE).
4. **Deep neurocognitive/psychiatric phenotyping** of patients (memory, mood, anxiety) to test whether mouse-predicted CNS features (CA3-linked memory deficits, depression/anxiety) manifest in humans, informing surveillance.
5. **Functional characterization of candidate hypomorphic/missense *CPE* variants** (enzyme activity, secretory-granule sorting, stability) to define genotype–phenotype relationships and resolve VUS.
6. **Modifier-gene mapping**, leveraging the strong strain-background effect in *Cpe*^fat/fat^ mice, to identify loci that could explain variable human severity and inform precision management.
7. **Cascade carrier testing and genetic counseling** in affected consanguineous families, with offer of prenatal/preimplantation testing, as a concrete preventive action given the recessive, high-penetrance inheritance.

---

*Report compiled from 9 confirmed findings across 5 investigation iterations and 35 reviewed papers. Evidence sources span human clinical case reports, mouse model-organism studies, and in vitro mechanistic work, as annotated above.*


## Artifacts

- [OpenScientist final report](BDV_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](BDV_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0025499` (2 mentions) - the report calls it "Childhood-onset obesity"; HP calls it **Class I obesity**
- `HP:0000708` (1 mention) - the report calls it "Behavioral abnormality (model-predicted)"; HP calls it **Atypical behavior**, and lists "Behavioral abnormality" among its other names
- `HP:0002354` (1 mention) - the report calls it "Memory impairment (model-predicted)"; HP calls it **Memory impairment**

22 of 23 terms resolved to a current term; the rest could not be looked up either way.