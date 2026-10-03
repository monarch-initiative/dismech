---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T19:31:21.711773'
end_time: '2026-09-30T19:58:52.702692'
duration_seconds: 1650.99
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Waardenburg Syndrome Type 2F
  mondo_id: MONDO:0030983
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
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 7
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 19
  verified: 17
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Waardenburg_Syndrome_Type_2F-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Waardenburg_Syndrome_Type_2F-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Waardenburg Syndrome Type 2F
- **MONDO ID:** MONDO:0030983 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Waardenburg Syndrome Type 2F** covering all of the
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

# Waardenburg Syndrome Type 2F (WS2F): Comprehensive Disease Characterization

**Disease:** Waardenburg Syndrome Type 2F
**MONDO ID:** MONDO:0030983 · **OMIM:** #619947 · **Gene:** *KITLG* (HGNC:6343)
**Category:** Mendelian (autosomal dominant neurocristopathy)

---

## Summary

Waardenburg Syndrome Type 2F (WS2F) is a rare autosomal dominant **auditory-pigmentary neurocristopathy** caused by heterozygous **loss-of-function variants in *KITLG*** (KIT ligand / stem cell factor), located on chromosome 12q21.32. WS2F belongs to the broader family of Waardenburg syndromes, which together affect roughly **1 in 40,000** individuals and account for approximately 2–3% of congenital deafness. Type 2 is distinguished from Type 1 by the **absence of dystopia canthorum** (lateral displacement of the inner canthi), and WS2F designates the molecular subtype in which the causal gene is *KITLG*, a rare cause first delineated by Zazo Seco and colleagues in 2015 ([PMID: 26522471](https://pubmed.ncbi.nlm.nih.gov/26522471/)).

The core mechanism is a deficiency of **neural-crest-derived melanocytes**. KITLG is the ligand for the KIT receptor tyrosine kinase; heterozygous loss-of-function reduces soluble KIT ligand, producing haploinsufficient KIT signaling in migrating melanoblasts and downstream failure of melanocyte survival, proliferation, and migration. Because melanocytes populate the **cochlear stria vascularis**, the **iris**, the **skin**, and **hair follicles**, their loss simultaneously causes **congenital, non-progressive sensorineural hearing loss** (via loss of the endocochlear potential) and **pigmentary anomalies** (heterochromia iridis, white forelock, premature graying, and hypo-/hyperpigmented cutaneous macules). A distinctive clinical feature of KITLG-related disease is its association with **asymmetric or unilateral hearing loss** and marked variable expressivity, such that the same variant can produce full WS2 or isolated hearing loss.

WS2F is purely Mendelian: no environmental, infectious, lifestyle, or gene-environment factors contribute to its causation, though **reduced (incomplete) penetrance** implies undefined genetic/stochastic modifiers. There is no disease-modifying or gene-specific therapy. Management is **supportive and multidisciplinary**, centered on **early cochlear implantation**, which yields excellent auditory and educational outcomes. Life expectancy is normal. This report synthesizes nine confirmed findings across 50 reviewed papers into a complete disease knowledge-base entry organized by the requested sections.

---

## Key Findings

### Finding 1 — WS2F is caused by heterozygous loss-of-function *KITLG* mutations (F001)

WS2F is caused by **heterozygous loss-of-function variants in *KITLG***, inherited in an autosomal dominant pattern with reduced penetrance. The landmark study by Zazo Seco et al. (2015) identified heterozygous *KITLG* mutations segregating with Waardenburg syndrome type 2 and with non-syndromic asymmetric/unilateral hearing loss (NS-UHL/AHL). The reported variants include a frameshift/nonsense change **c.286_303delinsT (p.Ser96Ter)**, an in-frame indel **c.200_202del (p.His67_Cys68delinsArg)**, and a missense variant **c.310C>G (p.Leu104Val)** that segregated with WS2 in a small family. In vitro functional testing showed that mutant soluble KITLG isoforms were **reduced or undetectable** in culture media, establishing a loss-of-function mechanism.

> *"a heterozygous missense mutation, c.310C>G (p.Leu104Val), that segregated with WS2 was identified in a small family"* — [PMID: 26522471](https://pubmed.ncbi.nlm.nih.gov/26522471/)

> *"These data suggest that mutations in KITLG associated with NS-UHL/AHL have a loss-of-function effect."* — [PMID: 26522471](https://pubmed.ncbi.nlm.nih.gov/26522471/)

WS2F corresponds to **OMIM #619947** and **MONDO:0030983**; the gene is *KITLG* (**HGNC:6343**, NCBI Gene 4254, UniProt P21583, chromosome 12q21.32). *Evidence type: human clinical + in vitro.*

### Finding 2 — Core WS2 phenotype: congenital SNHL and pigmentary anomalies without dystopia canthorum (F002)

WS2 (including WS2F) is clinically defined by **congenital sensorineural hearing loss (SNHL)** and **pigmentary abnormalities** of the eyes (heterochromia iridum/bright blue irides), hair (white forelock, premature graying), and skin — **without dystopia canthorum**, the feature that distinguishes WS1 from WS2. In a Chinese WS2 cohort (n=20), SNHL occurred in **85%** and heterochromia iridum in **100%**; 25% had brown freckles / pigmented macules. KITLG-specific WS2 (WS2F) has been reported with pigmented macules. Variable expressivity is prominent: *KITLG* mutations can produce full WS2 or isolated non-syndromic unilateral/asymmetric hearing loss.

> *"Sensorineural hearing loss (17/20, 85.0%) and heterochromia iridum (20/20, 100.0%) were the most commonly observed clinical features in Chinese WS2 patients."* — [PMID: 24194866](https://pubmed.ncbi.nlm.nih.gov/24194866/)

> *"Waardenburg syndrome (WS) is a genetic disorder characterized by sensorineural hearing loss and pigmentation anomalies."* — [PMID: 28236341](https://pubmed.ncbi.nlm.nih.gov/28236341/)

*Evidence type: human clinical.*

### Finding 3 — Pathophysiology: KITLG–KIT signaling deficiency impairs cochlear and cutaneous melanocyte development (F003)

KITLG (stem cell factor) binds the **KIT receptor tyrosine kinase**, activating downstream **RAS-MAPK** and **PI3K-AKT** cascades that drive neural-crest-derived melanoblast survival, proliferation, and migration; KITLG-KIT signaling functionally interacts with the master melanocyte transcription factor **MITF**. Melanocytes of neural-crest origin populate the skin, eye, and inner ear (stria vascularis); their loss produces both pigmentary defects and SNHL. Parallel evidence from the *Mitf(Mi-wh)/+* mouse (a WS2 model) shows profound hearing deficit with **absent endocochlear potential**, loss of outer hair cells, and stria vascularis abnormalities; cochlear melanocytes are present at birth but disappear between postnatal days P1 and P7.

> *"Although cochlear melanocytes are present at birth, they disappear from the Mitf(Mi-wh) /+ cochlea between P1 and P7."* — [PMID: 23020089](https://pubmed.ncbi.nlm.nih.gov/23020089/)

> *"KITLG-KIT signaling and MITF are suggested to mutually interact in melanocyte development."* — [PMID: 26522471](https://pubmed.ncbi.nlm.nih.gov/26522471/)

*Evidence type: human clinical + model organism + in vitro.*

### Finding 4 — Epidemiology, inheritance, and diagnosis (F004)

Waardenburg syndrome overall prevalence is approximately **1/40,000**, and WS accounts for ~2–3% of congenital deafness. WS2F is an **autosomal dominant** subtype with **reduced (incomplete) penetrance** and **variable expressivity** — the same *KITLG* variant can yield full WS2 or isolated unilateral/asymmetric hearing loss. Diagnosis of WS type 2 uses the **Waardenburg Syndrome Consortium major/minor criteria** (major: congenital SNHL, iris pigmentary abnormality, hair hypopigmentation, affected first-degree relative; minor: skin hypopigmentation, synophrys, etc.), combined with molecular confirmation via targeted NGS deafness-gene panels or whole-exome sequencing. Among known WS2 genes, approximate contributions are MITF (~15%), SOX10, EDNRB (~5–6%), SNAI2, and KIT/KITLG; **KITLG (WS2F) is a rare cause**.

> *"Waardenburg syndrome (WS), which occurs with a frequency of 1/40,000"* — [PMID: 41159045](https://pubmed.ncbi.nlm.nih.gov/41159045/)

> *"This mutation co-segregated with NS-UHL/AHL as a dominant trait with reduced penetrance."* — [PMID: 26522471](https://pubmed.ncbi.nlm.nih.gov/26522471/)

> *"Waardenburg syndrome type 2 was diagnosed in a 4-year-old boy according to the Waardenburg Syndrome Consortium Criteria."* — [PMID: 37272645](https://pubmed.ncbi.nlm.nih.gov/37272645/)

*Evidence type: human clinical.*

### Finding 5 — Treatment and prognosis: cochlear implantation and supportive care; normal lifespan (F005)

No disease-modifying or gene-specific therapy exists for WS2F; management is **supportive**. Congenital SNHL is treated with hearing aids and **cochlear implantation (CI)**. In WS children, early CI yields substantial gains: in a Japanese cohort (n=12, mean CI age 2.5 years), earlier intervention correlated with higher word/sentence scores; children without cochlear malformation achieved speech recognition **>80%**, and all advanced to regular junior-high classes. WS/neurocristopathy CI cohorts achieve excellent auditory-speech outcomes (CAP ~7.3, SIR ~4.0). Cochlear duct length/malformation — more pronounced in SOX10-related WS — can complicate electrode selection but is not a prominent feature of KITLG-WS2F. Prognosis: hearing loss is congenital and generally **stable (non-progressive)**; pigmentary features are cosmetic; **life expectancy is normal**.

> *"Children without cochlear malformations or delayed treatment achieved mean speech recognition scores exceeding 80%. All participants advanced to regular junior high school classes."* — [PMID: 41450428](https://pubmed.ncbi.nlm.nih.gov/41450428/)

*Evidence type: human clinical.*

### Finding 6 — Model organisms and comparative biology (F006)

The mouse ortholog of *KITLG* is ***Kitl*** (the classical **Steel, *Sl*, locus**; MGI), and its receptor is *Kit* (the **Dominant white spotting, *W*** locus). Steel mutant mice show white coat spotting, anemia, mast-cell deficiency, and sterility, and Kit/Kitl signaling is essential for melanoblast migration/survival — directly paralleling the pigmentary defects of human *KITLG* disease. KITLG-related pigmentation/deafness phenotypes are conserved across mammals because melanocytes and neurocytes share a neural-crest origin. The ***Mitf(Mi-wh)/+*** mouse is an established WS2 model reproducing deafness via strial melanocyte loss. Postnatal *Kitl* expression modulates epidermal melanocyte proliferation, differentiation, and stem-cell homeostasis.

> *"sensory organs and nerves are particularly affected by disorders because of the shared origin of melanocytes and neurocytes in the neural crest"* — [PMID: 23583561](https://pubmed.ncbi.nlm.nih.gov/23583561/)

> *"KITL signaling is important for melanocyte development in mammals"* — [PMID: 37482288](https://pubmed.ncbi.nlm.nih.gov/37482288/)

Applicable NCBI taxon: *Mus musculus* (10090). *Evidence type: model organism.*

### Finding 7 — *KITLG* gene/protein: dosage-sensitive KIT ligand shaping normal and pathological pigmentation (F007)

*KITLG* encodes **KIT ligand / stem cell factor (SCF / mast cell growth factor)**, produced as a transmembrane protein that is proteolytically cleaved to release a soluble isoform; both membrane-bound and soluble forms activate the KIT receptor. WS2F-causing variants reduce the soluble isoform (**loss-of-function / haploinsufficiency**). *KITLG* is **dosage-sensitive** for pigmentation: a common regulatory enhancer SNP (rs12821256) altering a LEF1 binding site drives classic blond hair in northern Europeans, and *KITLG* variants are genome-wide significant for human hair color and are among the established human pigmentation genes. Somatic KITLG amplification is **not** a feature of WS2F; WS2F variants are germline. No recurrent founder *KITLG* variant or common chromosomal rearrangement is established for WS2F.

> *"we dissect a regulatory region of the KITLG gene (encoding KIT ligand) that is significantly associated with common blond hair color in northern Europeans"* — [PMID: 24880339](https://pubmed.ncbi.nlm.nih.gov/24880339/)

> *"a variant near KITLG is associated with hair color"* — [PMID: 17952075](https://pubmed.ncbi.nlm.nih.gov/17952075/)

*Evidence type: human GWAS + functional.*

### Finding 8 — WS2F phenotype spectrum with HPO terms, onset, severity, and anatomy (F008)

Core WS2F phenotypes are **congenital in onset, variably expressed, and non-progressive**:

| Phenotype | HPO term | Frequency / notes |
|---|---|---|
| Congenital sensorineural hearing loss | HP:0000407 | Bilateral, unilateral, or asymmetric; KITLG notably associated with unilateral/asymmetric loss; severity moderate–profound |
| Heterochromia iridis / bright blue irides | HP:0001100 (heterochromia iridis), HP:0007730 (iris hypopigmentation) | ~100% in WS2 cohorts |
| White forelock / poliosis | HP:0002211 (white forelock); HP:0002216 (premature graying) | Characteristic |
| Skin hypopigmentation / hyperpigmented macules | HP:0001010 / HP:0001053 | Pigmented macules reported specifically in KITLG WS2F |
| Dystopia canthorum | — | **ABSENT** (distinguishes WS2 from WS1) |

> *"Pigmented macules in Waardenburg syndrome type 2 due to KITLG mutation."* — [PMID: 28504826](https://pubmed.ncbi.nlm.nih.gov/28504826/)

> *"heterochromia iridum (20/20, 100.0%) were the most commonly observed clinical features"* — [PMID: 24194866](https://pubmed.ncbi.nlm.nih.gov/24194866/)

**Anatomical structures (UBERON):** inner ear/cochlea (UBERON:0001844), stria vascularis (UBERON:0002928), iris (UBERON:0001769), skin (UBERON:0002097), hair follicle (UBERON:0002073). **Body systems:** auditory/nervous and integumentary. **Cell type (CL):** melanocyte (CL:0000148) — cochlear intermediate cells / cutaneous and uveal melanocytes. Onset congenital; course stable/lifelong; QoL impact driven by hearing loss (communication, education) rather than pigmentary features (cosmetic). *Evidence type: human clinical.*

### Finding 9 — Environmental, infectious, protective, and gene-environment factors are not applicable (F009)

WS2F is a **monogenic autosomal dominant disorder** fully attributable to heterozygous germline *KITLG* loss-of-function. Accordingly: (a) **no** environmental toxins, radiation, occupational exposures, lifestyle/dietary factors, or infectious agents cause or trigger WS2F; (b) **no** protective genetic or environmental factors are defined (though reduced penetrance implies unknown modifiers/stochastic thresholds); (c) **no** gene-environment interactions are documented. Congenital SNHL differential diagnosis includes infectious mimics (congenital CMV, rubella) that must be excluded clinically but are etiologically unrelated. No disease-specific epigenetic changes, somatic variants, recurrent chromosomal rearrangements, or founder alleles are established.

> *"Waardenburg syndrome (WS) represents a group of genetic conditions characterized by auditory and pigmentation defects."* — [PMID: 41516007](https://pubmed.ncbi.nlm.nih.gov/41516007/)

*Evidence type: human clinical / systematic review.*

---

## Report by Requested Section

### 1. Disease Information

WS2F is a rare Mendelian auditory-pigmentary syndrome — a **neurocristopathy** arising from defective development of neural-crest-derived melanocytes. Key identifiers: **OMIM #619947**, **MONDO:0030983**, gene *KITLG* (**HGNC:6343**). ICD-11 maps Waardenburg syndrome under **LD2H.1**; legacy ICD-10 coding uses **E70.3**/Q-codes variably. MeSH: *Waardenburg Syndrome* (D014849). Orphanet catalogs Waardenburg syndrome type 2 (ORPHA:895) with molecular subtypes. **Synonyms:** WS2F; Waardenburg syndrome type 2, KITLG-related; auditory-pigmentary syndrome (KITLG). Information is derived from **aggregated disease-level resources** (OMIM, Orphanet) and a small number of individual case/family reports rather than EHR cohorts, reflecting the rarity of the *KITLG* subtype.

### 2. Etiology

**Causal factor:** heterozygous germline **loss-of-function variants in *KITLG*** (F001). **Genetic risk factors:** the causal variant itself; no additional susceptibility loci or established modifier genes are defined, although reduced penetrance implies unknown genetic/stochastic modifiers (F009). **Environmental risk factors:** none (F009). **Protective factors:** none defined. **Gene-environment interactions:** none documented. WS2F is thus a "clean" monogenic disorder for etiology annotation.

### 3. Phenotypes

See Finding F008 table for the phenotype spectrum with HPO terms, frequencies, and characteristics. All phenotypes are **congenital in onset** and **non-progressive**. The dominant quality-of-life burden is from **hearing loss** (communication, language, education), which is remediable with cochlear implantation; pigmentary features are **cosmetic**. A hallmark of *KITLG*-WS2F is the tendency toward **asymmetric/unilateral hearing loss** and striking variable expressivity.

### 4. Genetic / Molecular Information

**Causal gene:** *KITLG* (12q21.32; NCBI Gene 4254; UniProt P21583). **Reported pathogenic variants** (F001): c.286_303delinsT (p.Ser96Ter) — nonsense/frameshift; c.200_202del (p.His67_Cys68delinsArg) — in-frame indel; c.310C>G (p.Leu104Val) — missense segregating with WS2. **Variant classification:** pathogenic/likely pathogenic per ACMG segregation + functional evidence. **Functional consequence:** loss of function / **haploinsufficiency**, with reduced soluble KIT ligand (F007). **Origin:** germline. **Allele frequency:** private/rare, absent or ultra-rare in gnomAD. **Modifier genes:** none established. **Epigenetic changes / chromosomal abnormalities:** none disease-specific for WS2F (F009).

### 5. Environmental Information

Not applicable — no environmental, lifestyle, or infectious contributors (F009). Infectious causes of congenital SNHL (CMV, rubella) are relevant only as **differential diagnoses**, not as etiologic agents.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous loss-of-function variant in *KITLG*** *results in* reduced production of functional KIT ligand, particularly the **soluble isoform** (demonstrated in vitro; F001/F007).
2. Reduced soluble/membrane KIT ligand *leads to* **haploinsufficient KIT receptor signaling** in neural-crest-derived melanoblasts (inferred from dosage biology; F007).
3. Deficient KIT signaling *results in* attenuated **RAS-MAPK and PI3K-AKT** cascades and reduced interaction with **MITF**, *leading to* impaired **melanoblast survival, proliferation, and migration** (F003).
4. **Branch A (auditory):** Deficient melanocyte migration/survival *results in* **absent or reduced intermediate cells/melanocytes in the cochlear stria vascularis** → *leads to* **loss of the endocochlear potential** → *results in* **congenital sensorineural hearing loss** (mechanism demonstrated in the Mitf(Mi-wh)/+ mouse, inferred for KITLG-WS2F; F003).
5. **Branch B (pigmentary):** The same melanocyte deficiency *leads to* **absent melanocytes in skin, hair follicles, and iris** → *results in* **hypopigmentation** (white forelock, heterochromia iridis) and, in KITLG cases, **pigmented macules** (F003/F008).

```
KITLG loss-of-function variant
      │  (reduced soluble KIT ligand)
      ▼
Haploinsufficient KIT signaling (RAS-MAPK, PI3K-AKT; MITF interaction)
      │
      ▼
Deficient melanoblast survival / migration / proliferation
      ├──────────────► Branch A: stria vascularis melanocyte loss
      │                        → loss of endocochlear potential
      │                        → congenital SNHL (HP:0000407)
      └──────────────► Branch B: skin / hair / iris melanocyte loss
                               → heterochromia iridis (HP:0001100),
                                 white forelock (HP:0002211),
                                 pigmented / hypopigmented macules
```

**Molecular pathways:** KITLG-KIT receptor tyrosine kinase signaling; RAS-MAPK; PI3K-AKT; MITF transcriptional program. **Cellular processes:** neural crest cell migration (GO:0001755), melanocyte differentiation (GO:0030318), melanocyte proliferation, cell survival. **Cell types (CL):** melanocyte (CL:0000148). **Upstream:** the *KITLG* lesion and KIT signaling deficit. **Downstream:** melanocyte depletion and the two organ-specific branches. No immune, metabolic, or oxidative-stress mechanisms are implicated.

### 7. Anatomical Structures Affected

**Organ level:** inner ear/cochlea (UBERON:0001844) — primary; eye/iris (UBERON:0001769), skin (UBERON:0002097), hair follicle (UBERON:0002073). **Body systems:** auditory/nervous and integumentary. **Tissue/cell level:** neural-crest-derived **melanocytes** (CL:0000148), including cochlear **stria vascularis** intermediate cells (UBERON:0002928) and cutaneous/uveal melanocytes. **Subcellular:** melanosome (GO:0042470) and melanin biosynthesis machinery. **Lateralization:** pigmentary features may be patchy/asymmetric; hearing loss may be **bilateral, unilateral, or asymmetric** — with KITLG notably associated with unilateral/asymmetric loss.

### 8. Temporal Development

**Onset:** congenital (present from birth). **Onset pattern:** developmental (established prenatally during neural-crest migration). **Progression:** hearing loss is generally **stable/non-progressive**; pigmentary features stable. **Disease course:** chronic, lifelong, non-remitting. **Critical period:** the therapeutic window for hearing rehabilitation is **early childhood** — earlier cochlear implantation correlates with better speech/language outcomes (F005).

### 9. Inheritance and Population

**Prevalence:** WS overall ~1/40,000; WS2F is a rare molecular subtype (few reported families). **Inheritance:** autosomal dominant. **Penetrance:** **reduced/incomplete**. **Expressivity:** **variable** (full WS2 to isolated hearing loss). **Anticipation / germline mosaicism / founder effects:** none established for WS2F. **Consanguinity:** not relevant (dominant). **Sex ratio:** no strong sex bias reported. **Geographic distribution:** no endemic clustering; reported across populations.

### 10. Diagnostics

**Clinical diagnosis** uses the **Waardenburg Syndrome Consortium major/minor criteria** (F004). **Audiology:** audiometry/ABR confirms congenital SNHL; **ophthalmology** documents iris pigmentary anomalies. **Imaging:** temporal-bone CT/MRI assesses cochlear anatomy prior to CI (cochlear duct length considerations more relevant to SOX10-WS). **Genetic testing:** targeted **NGS deafness/WS gene panels** or **whole-exome sequencing** including *KITLG*, *MITF*, *SOX10*, *EDNRB*, *EDN3*, *SNAI2*, *PAX3*; single-gene testing of *KITLG* when WS2F is suspected. **Differential diagnosis:** other WS subtypes (WS1 distinguished by dystopia canthorum; WS4 by Hirschsprung disease), piebaldism (*KIT*), and infectious congenital SNHL (CMV, rubella). **Screening:** newborn hearing screening detects the SNHL; **cascade genetic testing** of relatives given dominant inheritance.

### 11. Outcome / Prognosis

**Life expectancy is normal**; WS2F is not life-limiting. **Morbidity** is driven by hearing loss and its communication/educational consequences, which are substantially mitigated by early cochlear implantation — children without cochlear malformation achieve speech recognition >80% and mainstream schooling (F005). Pigmentary features carry only cosmetic/psychosocial impact. **Prognostic factors** for hearing outcome: age at implantation (younger better within the early window) and cochlear morphology.

### 12. Treatment

No gene-specific therapy (F005). **Supportive/rehabilitative:** hearing aids; **cochlear implantation** (NCIT: Cochlear Implantation); speech-language therapy; auditory-verbal rehabilitation. **Multidisciplinary care:** audiology, otology, ophthalmology, dermatology, and **genetic counseling**. Pigmentary features generally require no treatment; standard dermatologic/cosmetic measures optional. No pharmacotherapy, gene therapy, cell therapy, or RNA-based therapy is established or in trials specifically for WS2F.

### 13. Prevention

Primary prevention is not applicable (genetic). **Secondary prevention** = **newborn hearing screening** enabling early CI. **Genetic counseling** provides recurrence-risk assessment (50% transmission from an affected heterozygote, modified by reduced penetrance), with options for prenatal/preimplantation genetic testing where a familial variant is known. Cascade testing identifies at-risk relatives.

### 14. Other Species / Natural Disease

**Taxonomy:** *Mus musculus* (NCBI:txid10090). **Orthologous gene:** mouse *Kitl* (Steel locus); receptor *Kit* (W locus) (F006). Coat-color mutations in *KIT*, *EDNRB*, *MITF*, *PAX3*, *SNAI2* produce analogous pigmentation-plus-sensory phenotypes across mammals due to the shared neural-crest origin of melanocytes and neurocytes. Naturally occurring KITLG/KIT pigmentation variation is documented in cattle, dogs, and other mammals (comparative; not identical to human WS2F).

### 15. Model Organisms

**Mouse** is the principal model. **Steel (*Kitl*) mutants** recapitulate pigmentary defects (white spotting) plus anemia, mast-cell deficiency, and sterility, reflecting KIT ligand's broader roles beyond melanocytes. The ***Mitf(Mi-wh)/+*** mouse is an established **WS2 deafness model** demonstrating strial melanocyte loss between P1–P7 and absent endocochlear potential (F003/F006) — the key mechanistic bridge for the auditory phenotype. **Limitations:** no published *Kitl*-specific heterozygous mouse modeling the exact WS2F human variants; Steel homozygotes are lethal/severe, limiting direct haploinsufficiency modeling. Resources: MGI, IMSR.

---

## Mechanistic Model / Interpretation

WS2F is best understood as a **melanocyte-dosage disease**. A single wild-type *KITLG* allele is insufficient to supply the KIT ligand needed for full melanoblast survival and migration during a narrow developmental window. The convergence of human genetics (F001/F007), functional data on reduced soluble ligand (F001), pigmentation GWAS establishing KITLG dosage-sensitivity (F007), and mouse strial-melanocyte loss (F003/F006) produces a coherent, well-supported causal chain. The **branch point** — a single upstream lesion producing two phenotypic outputs (deafness and hypopigmentation) — explains the syndromic pairing, while **haploinsufficiency at a threshold-dependent developmental step** explains the reduced penetrance and variable expressivity (including unilateral hearing loss): stochastic variation in whether enough melanocytes reach a given cochlea or skin region tips individuals above or below the phenotypic threshold.

| Feature | Upstream cause | Downstream effect | Key evidence |
|---|---|---|---|
| Congenital SNHL | KITLG LoF → KIT signaling deficit | Strial melanocyte loss → no endocochlear potential | Mouse Mitf(Mi-wh) [PMID: 23020089] |
| Heterochromia / white forelock / macules | Same lesion | Skin/hair/iris melanocyte deficiency | WS2 cohorts [PMID: 24194866]; KITLG macules [PMID: 28504826] |
| Reduced penetrance / unilateral loss | Threshold-dependent haploinsufficiency | Stochastic phenotypic output | [PMID: 26522471] |

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [26522471](https://pubmed.ncbi.nlm.nih.gov/26522471/) | *Allelic Mutations of KITLG ... Cause ... Waardenburg Syndrome Type 2* | **Foundational** — establishes KITLG as WS2F gene, LoF mechanism, dominant/reduced penetrance |
| [24194866](https://pubmed.ncbi.nlm.nih.gov/24194866/) | *Genetic and phenotypic heterogeneity in Chinese WS2* | Phenotype frequencies (SNHL 85%, heterochromia 100%) |
| [28236341](https://pubmed.ncbi.nlm.nih.gov/28236341/) | *EDNRB mutations cause WS2* | Defines cardinal WS features |
| [23020089](https://pubmed.ncbi.nlm.nih.gov/23020089/) | *Hearing dysfunction in Mitf(Mi-wh)/+ mice* | Mechanistic bridge — strial melanocyte loss → deafness |
| [41159045](https://pubmed.ncbi.nlm.nih.gov/41159045/) | *Association of WS with a new mutation* | WS prevalence 1/40,000 |
| [37272645](https://pubmed.ncbi.nlm.nih.gov/37272645/) | *De Novo SOX10 mutation, WS2* | Confirms Consortium diagnostic criteria |
| [41450428](https://pubmed.ncbi.nlm.nih.gov/41450428/) | *Long-Term Outcomes After CI in WS Children* | Treatment/prognosis — CI outcomes |
| [23583561](https://pubmed.ncbi.nlm.nih.gov/23583561/) | *Pleiotropic effects of coat-colour mutations* | Comparative biology rationale |
| [37482288](https://pubmed.ncbi.nlm.nih.gov/37482288/) | *Postnatal Kitl affects epidermal pigmentation* | Conserved Kitl role in melanocytes |
| [24880339](https://pubmed.ncbi.nlm.nih.gov/24880339/) | *Molecular basis for classic blond hair* | KITLG dosage-sensitivity |
| [17952075](https://pubmed.ncbi.nlm.nih.gov/17952075/) | *Genetic determinants of hair/eye/skin pigmentation* | KITLG pigmentation GWAS |
| [28504826](https://pubmed.ncbi.nlm.nih.gov/28504826/) | *Pigmented macules in WS2 due to KITLG* | KITLG-specific skin phenotype |
| [41516007](https://pubmed.ncbi.nlm.nih.gov/41516007/) | *Genetics of WS in Africa: Systematic Review* | Confirms purely genetic etiology |
| [41271950](https://pubmed.ncbi.nlm.nih.gov/41271950/) | *Neurocristopathy hearing loss & CI outcomes* | CI outcomes in WS (CAP 7.3/SIR 4.0) |

**Evidence-source distribution:** human clinical/genetic (majority), model organism (mouse Mitf/Kitl), in vitro functional (soluble ligand assays), and computational/GWAS (pigmentation). The central causal claim rests on a single foundational human study ([PMID: 26522471](https://pubmed.ncbi.nlm.nih.gov/26522471/)) supported by convergent mechanistic and comparative evidence.

---

## Limitations and Knowledge Gaps

1. **Small evidence base for the KITLG subtype specifically.** WS2F is defined by a handful of families; most mechanistic inference borrows from *MITF* mouse models and general KITLG/pigmentation biology rather than KITLG-specific WS2F experiments.
2. **No KITLG-WS2F-specific mouse model** replicating the exact human haploinsufficiency; the strial-melanocyte mechanism is demonstrated in Mitf(Mi-wh)/+ and inferred for KITLG.
3. **Penetrance and expressivity modifiers are undefined** — the molecular basis of unilateral vs bilateral hearing loss and of unaffected carriers is unknown.
4. **No quantitative epidemiology for the KITLG subtype** (subtype-specific prevalence, sex ratio, geographic distribution unavailable).
5. **No natural-history or QoL-instrument data** specific to WS2F; prognosis is extrapolated from broader WS/CI cohorts.
6. **Allele-frequency and ClinVar annotations** for the specific reported variants were not independently re-queried in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Query ClinVar/gnomAD directly** for all reported *KITLG* WS2F variants to confirm classification, allele frequencies, and identify additional cases.
2. **Generate a Kitl heterozygous / conditional mouse** carrying humanized WS2F variants and assay endocochlear potential, strial melanocyte counts (P1–P7), and coat pigmentation to test haploinsufficiency directly.
3. **Single-cell/spatial transcriptomics of the developing stria vascularis** to quantify melanocyte dosage thresholds and model penetrance.
4. **Aggregate a WS2F case registry** (via GeneMatcher / deafness panels) to estimate subtype prevalence, penetrance, laterality distribution, and genotype-phenotype correlation.
5. **Systematic CI outcome analysis stratified by WS molecular subtype** to determine whether KITLG-WS2F outcomes differ from SOX10-WS (which has shorter cochlear duct length).
6. **Explore KIT-pathway pharmacologic modulation** in melanocyte/organoid models as a proof-of-concept for future disease-modifying approaches (currently none exist).

---

## Consensus Answer

Waardenburg Syndrome Type 2F (OMIM #619947; MONDO:0030983) is a rare autosomal dominant auditory-pigmentary neurocristopathy caused by heterozygous loss-of-function variants in *KITLG* (KIT ligand / stem cell factor) that reduce KIT-receptor signaling and impair neural-crest-derived melanocyte development. This produces congenital, non-progressive sensorineural hearing loss (from deficiency of cochlear stria vascularis melanocytes and loss of the endocochlear potential) together with pigmentary anomalies of the eyes, hair, and skin (heterochromia iridis, white forelock, pigmented/hypopigmented macules), without dystopia canthorum. It is not life-limiting; management is supportive and multidisciplinary, centered on early cochlear implantation, with no gene-specific therapy available.


## Artifacts

- [OpenScientist final report](Waardenburg_Syndrome_Type_2F-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Waardenburg_Syndrome_Type_2F-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000407` (2 mentions) - the report calls it "Congenital sensorineural hearing loss"; HP calls it **Sensorineural hearing impairment**, and lists "Sensorineural hearing loss" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

17 of 19 terms resolved to a current term; the rest could not be looked up either way.