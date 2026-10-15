---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T03:39:43.802307'
end_time: '2026-10-15T04:09:17.222769'
duration_seconds: 1773.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Complement Component 3 Deficiency
  mondo_id: MONDO:0013417
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 18
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:19640589
  relevance_assessed: 18
  on_topic: 11
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 13
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Complement_Component_3_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Complement_Component_3_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Complement Component 3 Deficiency
- **MONDO ID:** MONDO:0013417 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Complement Component 3 Deficiency** covering all of the
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

# Complement Component 3 (C3) Deficiency — Comprehensive Disease Characteristics Report

**Disease:** Complement Component 3 Deficiency
**MONDO ID:** MONDO:0013417 · **OMIM:** #613779 (disease), *120700 (gene) · **Orphanet:** ORPHA:280133 · **DOID:** 8354 · **NCIT:** C9468 · **GARD:** 0016489 · **UMLS:** C3151071 · **MeSH:** C565169 · **MedGen:** 462421
**Category:** Mendelian (autosomal recessive inborn error of immunity)

---

## Summary

Complement component 3 (C3) deficiency is an **extremely rare autosomal-recessive inborn error of immunity** caused by biallelic loss-of-function variants in the *C3* gene (HGNC:1318; chromosome 19p13.3; UniProt P01024). Fewer than 50 cases have been reported worldwide, making it one of the rarest of all complement deficiencies — which themselves comprise only ~1–10% of primary immunodeficiencies. The biochemical hallmark is **undetectable serum C3 with markedly reduced CH50 and normal C4**, reflecting failure of all three complement activation pathways at their convergence node ([PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)).

Because C3 is the central protein through which the classical, alternative, and lectin pathways all pass, its complete loss abolishes **C3b-thioester–mediated opsonization**, **C3a/C5a-driven inflammation**, **terminal membrane attack complex (MAC) formation**, and **immune-complex clearance and B-cell co-stimulation**. This produces a characteristic **dual clinical phenotype**: (1) recurrent, severe, invasive pyogenic infections by encapsulated bacteria (*Streptococcus pneumoniae*, *Neisseria meningitidis*, *Haemophilus influenzae*) with a predominance of respiratory/ENT disease, sepsis and meningitis; and (2) immune-complex-mediated disease, including SLE-like autoimmunity and membranoproliferative/mesangioproliferative glomerulonephritis. The autoimmune arm reflects the broader "complement–SLE hierarchy," in which early-complement-component deficiencies are the strongest known monogenic risk factors for lupus and are linked to type I interferon dysregulation.

There is **no curative therapy**. Management is preventive and supportive, centered on conjugate-polysaccharide vaccination against encapsulated bacteria and consideration of long-term antibiotic prophylaxis; analogous early-complement deficiencies show that early diagnosis plus prophylaxis can allow a near-normal life. A crucial clinical caveat is that **low serum C3 is far more often secondary** (deficiency of regulators factor H or factor I, C3 nephritic factor / C3 glomerulopathy, or classical-pathway consumption in SLE) than due to primary genetic C3 deficiency, which is defined by *undetectable* C3 with normal C4.

---

## Key Findings

### 1. Disease definition, identifiers, and nature of evidence (F001, F010)

Complete C3 deficiency is an **ultra-rare autosomal-recessive inborn error of immunity** caused by homozygous or compound-heterozygous loss-of-function variants in *C3*. The authoritative MONDO definition (MONDO:0013417) describes "a rare genetic disorder with an autosomal recessive pattern of inheritance… caused by the ineffective or decreased biosynthesis of the third complement component, C3," with clinical signs appearing "within the first decade of life… consistent with the signs of recurrent systemic infection or immune complex disease." The definition further notes that "deficiency of serum C3 and its major cleavage product, C3b, will decrease the effective humoral immune response to encapsulated bacteria" and that C3 deficiency "also impairs clearance of circulating immune complexes and therefore predisposes to rheumatic and renal disease."

Cross-reference identifiers were verified against EBI OLS4/MONDO: OMIM 613779, Orphanet 280133, MeSH C565169, UMLS C3151071, MedGen 462421, DOID:8354, NCIT C9468, GARD 0016489, NANDO 2200782.

**Synonyms / alternative names:** C3 deficiency; complement component 3 deficiency, autosomal recessive; C3 classic complement early component deficiency; classic complement early component deficiency caused by mutation in C3.

**Nature of the evidence:** Because the disease is ultra-rare (<50 cases), most knowledge derives from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, HPOA) and **individual case reports/small series** rather than large EHR cohorts. Mechanistic inferences are supported by model-organism (C3-knockout mouse) and in-vitro/structural studies, and by extrapolation from the better-characterized early-complement deficiencies (C1q, C2, factor H, factor I) ([PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)).

### 2. Clinical phenotype — infections plus immune-complex/autoimmune disease (F002, F011)

The clinical phenotype has two arms. In the infectious arm, patients suffer **recurrent severe pyogenic infections** with a predominance of the respiratory and otorhinolaryngological tracts, plus invasive disease (sepsis, meningitis) from encapsulated organisms. The index report notes that "both patients presented with chronic and recurrent infections, predominantly affecting the respiratory and otorhinolaryngological systems" ([PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)).

In the autoimmune/immune-complex arm, a subset develop **SLE-like disease** and **membranoproliferative/mesangioproliferative glomerulonephritis**. In a Saudi pediatric PID-lupus cohort, complement deficiency was the most frequent underlying PID, and "three patients had C3 deficiency" ([PMID: 33563058](https://pubmed.ncbi.nlm.nih.gov/33563058/)). More broadly, "the genetic deficiency of any early component of the classical pathway (C1q, C1r/s, C2, C4) is often associated with autoimmune diseases" ([PMID: 25037634](https://pubmed.ncbi.nlm.nih.gov/25037634/)).

**Curated HPO phenotype annotations (OMIM:613779 / HPOA; primary source PMID:15781264):**

| Phenotype | HPO term | Noted frequency |
|---|---|---|
| Decreased circulating complement C3 concentration | HP:0005421 | 2/2 |
| Recurrent bacterial infections | HP:0002718 | 1/1 |
| Recurrent pneumonia | HP:0006532 | 2/2 |
| Recurrent tonsillitis | HP:0011110 | 1/1 |
| Recurrent fever | HP:0001954 | 1/1 |
| Systemic lupus erythematosus | HP:0002725 | 1/1 |
| Membranoproliferative glomerulonephritis | HP:0000793 | — |
| Nephrotic syndrome | HP:0000100 | — |
| Renal insufficiency | HP:0000083 | — |
| Childhood onset | HP:0011463 | — |
| Infantile onset | HP:0003593 | — |
| Autosomal recessive inheritance | HP:0000007 | — |

**Quality of life:** No disease-specific QoL instruments (EQ-5D, SF-36) data are available for this ultra-rare disorder. Impact is driven by recurrent hospitalizations for invasive infection and, where present, by chronic kidney disease from glomerulonephritis.

### 3. Molecular/genetic information (F001, F005, F012)

- **Causal gene:** *C3* (complement C3), HGNC:1318, NCBI Gene 718, Ensembl ENSG00000125730, cytoband **19p13.3**, protein-coding. OMIM gene *120700; disease #613779.
- **Protein:** UniProt **P01024**. Sequence length = **1663 aa precursor** (signal peptide 1–22; mature "Complement C3" chain = residues 23–1663 = **1641 aa**), processed into a β-chain (23–667, 645 aa) and α-chain (672–1663, 992 aa), with embedded fragments **C3a** (672–748), **C3b** (749–1663), **C3d** (1002–1303), and **C3f** (1304–1320). The 1663 (precursor) vs 1641 (mature) residue count discrepancy was reconciled: crystallographic studies describe the mature 1,641-residue protein ([PMID: 16177781](https://pubmed.ncbi.nlm.nih.gov/16177781/)), while UniProt reports the full precursor.
- **Variant spectrum:** Nonsense, frameshift, missense, and splice-site variants have been reported. Example: a novel homozygous splice-site variant, **NM_000064.3:c.4030-1_4030delinsCT**, in Moroccan patients ([PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)). Variants are **germline** and typically **loss-of-function** (ACMG pathogenic/likely pathogenic).
- **Functional consequence:** Absent or non-functional C3, with loss of the thioester-mediated opsonic function.
- **Modifier genes / epigenetics / chromosomal abnormalities:** No established disease-specific modifier genes or epigenetic signatures for primary C3 deficiency; the disorder is a single-gene, protein-truncating/loss-of-function condition rather than a structural/chromosomal syndrome. Allele frequencies of pathogenic *C3* LoF variants are correspondingly rare in gnomAD given the <50-case worldwide total.

### 4. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1. Biallelic loss-of-function variant in C3 (19p13.3)
   → leads to absent or non-functional C3 protein (undetectable serum C3; normal C4).
2. Loss of C3 abolishes the convergence node of all three complement pathways
   → results in failure to generate C3 convertase products C3a and C3b.
3a. [INFECTION BRANCH] No C3b thioester deposition on microbial surfaces
   → leads to loss of opsonophagocytosis (no CRIg/CR1-mediated phagocyte uptake)
   → and failure to assemble downstream C5 convertase / MAC
   → results in defective killing of encapsulated bacteria
   → leads to recurrent invasive pyogenic infection (pneumonia, sepsis, meningitis).
3b. [AUTOIMMUNE BRANCH] No C3b/iC3b tagging of apoptotic debris and immune complexes
   → leads to impaired clearance of circulating immune complexes and apoptotic cells
   → results in autoantibody formation and tissue immune-complex deposition
   → leads to SLE-like disease and membranoproliferative glomerulonephritis.
3c. [HUMORAL BRANCH, inferred from mouse] Loss of C3d–CR2/CD21 B-cell co-stimulation
   → leads to impaired antibody responses (esp. to polysaccharide antigens) and
     defective immune-complex trafficking to follicular dendritic cells
   → compounds susceptibility to encapsulated bacteria.
```

**Central node mechanism (F003, F005).** C3 is the convergence point of the classical, alternative, and lectin pathways. "Key complement functions (C3b-mediated opsonisation, C3a/C5a-driven inflammation, and membrane attack complex formation) underlie target-specific patterns of infectious risk" ([PMID: 42175904](https://pubmed.ncbi.nlm.nih.gov/42175904/)). C3 is cleaved by C3 convertases into C3a (anaphylatoxin) and C3b, which deposits on surfaces via its reactive thioester and is recognized by phagocyte receptors; the complement receptor CRIg "binds to certain C3 cleavage products (C3b, iC3b, C3c)" ([PMID: 38032267](https://pubmed.ncbi.nlm.nih.gov/38032267/)).

**Protein-structural basis (F005).** Crystal structures of native C3 and fragment C3c reveal a 1,641-residue protein built from thirteen domains in the α₂-macroglobulin family. "Activation of component C3 (1,641 residues) is central to the three complement pathways and results in inflammation and elimination of self and non-self targets," and "a double mechanism prevents hydrolysis of the thioester group, essential for covalent attachment of activated C3 to target surfaces" ([PMID: 16177781](https://pubmed.ncbi.nlm.nih.gov/16177781/)). In deficiency, the opsonic thioester chemistry is entirely absent.

**Autoimmune mechanism and the complement–SLE hierarchy (F009).** Early-complement-component deficiencies are the strongest monogenic risk factors for SLE, graded by cascade position (C1q > C4 > C2), with C3 deficiency also predisposing to lupus-like disease. Mechanistically, deficiency impairs complement-mediated clearance of apoptotic cells and immune complexes, producing autoantibodies, immune-complex deposition, and complement consumption. Monogenic complement-deficient SLE is frequently early-onset and refractory and is "linked to interferon pathway dysregulation," with C1q-deficient pediatric SLE responding to the anti-type-I-interferon-receptor antibody anifrolumab ([PMID: 42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/)).

**Molecular pathways / GO & CL suggestions.** Biological processes: **complement activation (GO:0006956)**, complement activation alternative pathway (GO:0006957), classical pathway (GO:0006958), lectin pathway (GO:0001867), **opsonization (GO:0008228)**, complement-dependent cytotoxicity, positive regulation of B-cell activation. Cellular component: **extracellular space (GO:0005615)** (C3 is a secreted plasma protein, mainly hepatocyte-derived). Chemical entity: the reactive thioester underlies covalent opsonization (CHEBI thioester class). Cell types involved: **hepatocyte (CL:0000182)** (primary synthesis), **macrophage (CL:0000235)** / **neutrophil (CL:0000775)** (opsonophagocytosis via complement receptors), **follicular dendritic cell (CL:0000442)** and **B cell (CL:0000236)** (immune-complex trafficking / co-stimulation).

### 5. Anatomical structures affected

- **Primary "organ":** the **blood/plasma complement system** (C3 is a circulating plasma glycoprotein); the **liver** (UBERON:0002107) is the principal site of C3 synthesis (hepatocytes).
- **Secondary organ involvement:** **lung/airway and ENT** (UBERON:0002048 lung; UBERON:0001557 upper respiratory tract) — recurrent pneumonia/tonsillitis; **meninges / CNS** (meningitis); **kidney** (UBERON:0002113) — membranoproliferative/mesangioproliferative glomerulonephritis, nephrotic syndrome, renal insufficiency; **skin and joints** in SLE-like disease.
- **Body systems:** immune/hematologic, respiratory, renal/genitourinary, and (via autoimmunity) musculoskeletal and integumentary.
- **Tissue/cell level:** glomerular mesangial and capillary structures (immune-complex deposition); phagocytes; follicular dendritic cells; B cells. **Subcellular:** C3 is secreted; opsonization occurs at the plasma-membrane/extracellular interface (GO:0005615).
- **Lateralization:** not applicable — a systemic circulating-protein deficiency; organ involvement (e.g., glomerulonephritis) is bilateral/systemic.

### 6. Temporal development (F001, F010, F011)

- **Onset:** Clinical signs typically appear **within the first decade of life** (HPO: Childhood onset HP:0011463; Infantile onset HP:0003593), consistent with recurrent systemic infection or immune-complex disease.
- **Onset pattern:** Chronic/recurrent rather than a single acute event; infections are episodic and recurrent.
- **Progression/course:** Lifelong; infection susceptibility persists. Autoimmune/renal complications may accumulate over time; glomerulonephritis can progress to chronic kidney disease.
- **Critical period / window of opportunity:** Early diagnosis enables vaccination and prophylaxis before major invasive infection — the key modifiable determinant of outcome.

### 7. Inheritance and population (F001, F008)

- **Inheritance:** **Autosomal recessive** (HP:0000007). Biallelic (homozygous or compound-heterozygous) loss-of-function *C3* variants.
- **Penetrance/expressivity:** Biochemical penetrance of undetectable C3 is complete in biallelic LoF; clinical expressivity is variable (infection-predominant vs autoimmune-predominant vs, rarely, milder courses), consistent with other complement deficiencies.
- **Epidemiology:** Complement deficiencies comprise "between 1 and 10% of all primary immunodeficiencies" ([PMID: 25037634](https://pubmed.ncbi.nlm.nih.gov/25037634/)); in some pediatric PID series as low as ~1.1% ([PMID: 16836843](https://pubmed.ncbi.nlm.nih.gov/16836843/)). Complete C3 deficiency specifically is among the rarest — "fewer than 50 cases have been reported to date, and the genetic and phenotypic spectrum remains incompletely defined" ([PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)). It is widely **underdiagnosed** because few centers offer comprehensive complement analysis.
- **Founder effects / consanguinity:** Consanguinity and geographic clustering contribute to cases (e.g., multiple cases from the same region of Morocco). No large exact prevalence/incidence figures exist given rarity.
- **Sex ratio / age distribution:** No reliable sex predilection established for primary C3 deficiency; onset in childhood.

### 8. Diagnostics (F001, F007)

- **Laboratory hallmark:** **undetectable serum C3** with **markedly reduced CH50** and **normal C4** — "complement analysis showed undetectable C3 levels and markedly reduced CH50, with normal C4, consistent with isolated complete C3 deficiency" ([PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)). Both CH50 (classical) and AH50 (alternative) are low/absent because C3 is shared by both.
- **Functional/screening assays:** CH50 and AH50 total hemolytic complement assays as screens; individual component quantitation (C3, C4, factor B, factor H, factor I) to localize the defect. LOINC-codable assays include serum C3, C4, and total complement (CH50).
- **Genetic testing:** Confirmatory **single-gene *C3* sequencing** or NGS panel/exome; "NGS identified a novel homozygous splice-site variant in the C3 gene" ([PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)). Cascade testing of relatives is appropriate.
- **Differential diagnosis (F007) — critical:** Low serum C3 is **more often secondary** than primary:
  - **Factor H or factor I deficiency** → secondary C3 consumption via the unchecked alternative pathway. "A primary deficiency of factor H or I or both, will secondarily produce subnormal levels of C3 and factor B" ([PMID: 6545495](https://pubmed.ncbi.nlm.nih.gov/6545495/)); and in CFI deficiency, "no detectable factor I (<2%) together with a low level of factor B and a moderately low level of factor H, indicating consumption secondary to the factor I deficiency" ([PMID: 16138437](https://pubmed.ncbi.nlm.nih.gov/16138437/)).
  - **C3 nephritic factor (C3NeF)** autoantibodies (dense deposit disease / C3 glomerulopathy): "autoantibodies in MPGN are termed C3 Nephritic Factor (C3NeF)… directed against a neoepitope of the complement C3 convertase C3bBb… C3NeF stabilizes this convertase and this results in C3 amplification and complement activation" ([PMID: 19640589](https://pubmed.ncbi.nlm.nih.gov/19640589/)).
  - **Classical-pathway consumption** in SLE / post-infectious / MPGN (typically *both* C3 and C4 low).

  The distinguishing feature of **primary complete C3 deficiency** is undetectable C3 with **normal C4** and no evidence of a regulator defect or nephritic factor.

### 9. Outcome / Prognosis (F004)

- **No curative therapy exists.** Prognosis is determined largely by timeliness of diagnosis and institution of prophylaxis.
- With early diagnosis plus vaccination and antibiotic prophylaxis, outcomes in analogous early-complement deficiencies can approach normal life: in hereditary C2 deficiency, "early diagnosis, use of vaccinations and antibiotic prophylaxis may allow a normal life" ([PMID: 32164349](https://pubmed.ncbi.nlm.nih.gov/32164349/)).
- Major morbidity/mortality drivers: invasive infection (sepsis, meningitis) by encapsulated bacteria, and chronic kidney disease where immune-complex glomerulonephritis develops.
- No disease-specific 5-/10-year survival statistics exist given rarity; prognostic factors are infection burden, presence/severity of glomerulonephritis, and adherence to prophylaxis.

### 10. Treatment (F004)

There is **no causative/curative treatment** for hereditary complement component deficiencies. Standard of care is **preventive and supportive**:

- **Vaccination (primary prophylaxis):** conjugate vaccines against **meningococcus**, **pneumococcus** (conjugate polysaccharide), and **Haemophilus influenzae type b**. "Prophylaxis with conjugate polysaccharide vaccines is recommended and antibiotic prophylaxis should be considered in individual cases" ([PMID: 28078901](https://pubmed.ncbi.nlm.nih.gov/28078901/)).
- **Antibiotic prophylaxis:** long-term or case-by-case.
- **Pathogen targets:** "the most frequent pathogens are Neisseria meningitidis, Streptococcus pneumoniae and Haemophilus influenzae" ([PMID: 37356020](https://pubmed.ncbi.nlm.nih.gov/37356020/)).
- **Autoimmune/renal manifestations:** managed with standard immunosuppression for SLE/glomerulonephritis. By extrapolation from monogenic complement-deficient SLE, **type I interferon-targeted therapy (anifrolumab)** is an emerging option ([PMID: 42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/)).
- **NCIT intervention terms:** Pneumococcal Vaccine (NCIT C1764), Meningococcal Vaccine, Haemophilus b Conjugate Vaccine, Antibiotic Therapy (NCIT C15844), Immunosuppressive Therapy.

### 11. Prevention (F004)

- **Primary:** immunization against encapsulated bacteria (see above); risk awareness.
- **Secondary:** early diagnosis via complement screening in children with recurrent invasive infection or early/atypical SLE; cascade testing of relatives.
- **Tertiary:** antibiotic prophylaxis, prompt treatment of febrile illness, surveillance for renal disease.
- **Counseling:** autosomal-recessive genetic counseling; carrier testing in consanguineous families; prenatal/preimplantation options where a familial variant is known.

### 12. Model organisms (F006)

**C3-knockout (C3⁻/⁻) mice** (*Mus musculus*; NCBI Gene **C3** 12266) recapitulate opsonization and humoral defects:

- **Polysaccharide antibody defect:** "Mice deficient in C3 or Cr2 had an impaired primary immune response to III-PS. The defective response was characterized by low IgM levels and the lack of an isotype switch from IgM to IgG Ab production" ([PMID: 12496386](https://pubmed.ncbi.nlm.nih.gov/12496386/)) — directly relevant to vaccine responsiveness in deficient patients.
- **Immune-complex trafficking defect:** "Capture of antigen by MZ B cells as well as antigen deposition on FDC was severely impaired in mice lacking C1q or C3" ([PMID: 28710441](https://pubmed.ncbi.nlm.nih.gov/28710441/)).
- **Tissue inflammation phenotype:** "C3-deficient mice developed more severe pulmonary inflammations than wild type controls" in an AT1R-induced systemic sclerosis model ([PMID: 39737181](https://pubmed.ncbi.nlm.nih.gov/39737181/)), highlighting a context-dependent protective/regulatory role for C3 in tissue.

**Limitations of models:** Mouse C3 knockouts capture opsonization, humoral, and immune-complex-clearance defects but do not fully reproduce the human spectrum of recurrent encapsulated-bacterial invasive disease plus SLE-like autoimmunity; genetic background and specific infection/immunization challenges strongly influence phenotype.

### 13. Other species / comparative biology

- **Orthologous gene:** mouse *C3* (NCBI Gene 12266); C3 is highly evolutionarily conserved across vertebrates as a core innate-immune molecule of the α₂-macroglobulin/thioester-containing protein family ([PMID: 16177781](https://pubmed.ncbi.nlm.nih.gov/16177781/) — "insights into the function and evolution of immunity").
- **Natural disease:** Naturally occurring C3 deficiency has historically been described in domestic animals (e.g., dogs); no curated OMIA entry was validated in this investigation. Zoonotic transmission is **not applicable** (a genetic deficiency, not a transmissible disease).

---

## Mechanistic Model / Interpretation

The entire disease flows from the position of C3 as the **single convergence node** of the complement system. The following schematic integrates the findings:

```
          CLASSICAL          LECTIN          ALTERNATIVE
          (C1q/C1r/s/C4/C2)   (MBL/ficolins/   (C3/FB/FD, +properdin)
                 \            MASP2)   /
                  \             |     /
                   v            v    v
             ┌─────────────────────────────┐
             │   C3 CONVERTASES cleave C3   │  ◄── ABSENT in C3 deficiency
             └─────────────────────────────┘
                     /                \
                 C3a (anaphylatoxin)   C3b (thioester opsonin)
                 inflammation          /        \
                                 opsonophagocytosis   C5 convertase → C5b-9 (MAC)
                                 (CRIg/CR1 on              terminal lysis
                                  macrophages/neutrophils)
                                      |
                         + C3d–CR2/CD21 B-cell co-stimulation
                         + C3b/iC3b tagging of immune complexes → FDC trafficking / clearance

LOSS OF C3  ⇒  no opsonization + no MAC + no IC clearance + no B-cell co-stim
            ⇒  (a) recurrent encapsulated-bacterial infection
               (b) immune-complex disease: SLE-like autoimmunity + MPGN
```

Two features make C3 deficiency mechanistically distinctive among complement defects. First, because C3 is downstream of all three initiating pathways but upstream of the entire terminal cascade, its loss is **more complete** than that of any single upstream initiator — both CH50 and AH50 collapse. Second, the **dual phenotype** is not coincidental: the same C3b/iC3b chemistry that opsonizes bacteria also tags apoptotic debris and immune complexes for clearance, so its loss simultaneously creates infection susceptibility *and* a failure of self-tolerance housekeeping that drives SLE-like autoimmunity. This places C3 deficiency firmly on the **complement–SLE axis** alongside C1q, C4, and C2, with the modern mechanistic overlay that defective clearance converges on **type I interferon** activation — the rationale for emerging interferon-targeted therapy.

| Complement defect | CH50 | AH50 | C3 | C4 | Dominant phenotype |
|---|---|---|---|---|---|
| **Primary C3 deficiency** | ↓↓ | ↓↓ | **undetectable** | normal | Infection + SLE/MPGN |
| C1q / C4 / C2 deficiency | ↓↓ | normal | normal/low | low (C4) | SLE > infection |
| Factor H / I deficiency | variable | ↓ | **secondarily low** | normal | aHUS/GN + infection |
| C3 nephritic factor | — | ↓ | low (acquired) | normal | C3 glomerulopathy |
| Terminal (C5–C9) | ↓ | ↓ | normal | normal | Neisseria infection |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/) | Novel homozygous *C3* splice-site variant (case report) | Human clinical | Rarity (<50 cases), AR inheritance, lab signature, phenotype, example variant (F001, F002, F008) |
| [25037634](https://pubmed.ncbi.nlm.nih.gov/25037634/) | Are complement deficiencies really rare? | Review | Early-complement/autoimmune link; 1–10% of PIDs (F002, F008) |
| [33563058](https://pubmed.ncbi.nlm.nih.gov/33563058/) | Lupus in children with PID | Human cohort | C3 deficiency among monogenic lupus (F002, F009) |
| [42175904](https://pubmed.ncbi.nlm.nih.gov/42175904/) | Infection risk with complement inhibitors | Review | Core C3 effector functions (F003) |
| [38032267](https://pubmed.ncbi.nlm.nih.gov/38032267/) | Complement receptor of Ig superfamily (CRIg) | Structural/in vitro | C3 cleavage products recognized by phagocyte receptor (F003) |
| [16177781](https://pubmed.ncbi.nlm.nih.gov/16177781/) | Structures of C3 | Structural | 1,641-residue protein; thioester mechanism; central role (F005, F012) |
| [12496386](https://pubmed.ncbi.nlm.nih.gov/12496386/) | Impaired Ab response in C3/Cr2-deficient mice | Model organism | Humoral defect to polysaccharide (F006) |
| [28710441](https://pubmed.ncbi.nlm.nih.gov/28710441/) | IgG3-antigen complexes on FDCs need C1q/C3 | Model organism | Immune-complex trafficking (F006) |
| [39737181](https://pubmed.ncbi.nlm.nih.gov/39737181/) | C3 deficiency promotes pulmonary inflammation | Model organism | C3⁻/⁻ model; regulatory role (F006) |
| [16138437](https://pubmed.ncbi.nlm.nih.gov/16138437/) | Factor I deficiency, IC glomerulonephritis | Human clinical | Secondary C3 consumption (F007) |
| [6545495](https://pubmed.ncbi.nlm.nih.gov/6545495/) | Complement activation in renal disease | Review | FH/FI deficiency lowers C3 (F007) |
| [19640589](https://pubmed.ncbi.nlm.nih.gov/19640589/) | TMA and MPGN pathogenic principles | Review | C3NeF mechanism (F007) |
| [37356020](https://pubmed.ncbi.nlm.nih.gov/37356020/) | Reducing infection risk in complement deficiency | Guideline/review | Pathogen spectrum (F004) |
| [32164349](https://pubmed.ncbi.nlm.nih.gov/32164349/) | 21-yr follow-up of C2 deficiency family | Human clinical | Prophylaxis → normal life (F004) |
| [28078901](https://pubmed.ncbi.nlm.nih.gov/28078901/) | Recurrent meningitis & complement deficiency | Human clinical | Conjugate vaccines + antibiotic prophylaxis (F004) |
| [42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/) | Anifrolumab in C1q-deficient pediatric SLE | Human clinical | Monogenic lupus, IFN therapy (F009) |
| [16836843](https://pubmed.ncbi.nlm.nih.gov/16836843/) | Pediatric PID overview | Registry | Complement deficiency ~1.1% of pediatric PID (F008) |

**Source-type note:** Direct primary evidence for complete C3 deficiency is dominated by case reports and small series (the disease being ultra-rare). Mechanistic claims are buttressed by structural biology ([PMID: 16177781](https://pubmed.ncbi.nlm.nih.gov/16177781/)), mouse-knockout studies, and extrapolation from the better-characterized C1q/C2/factor H/factor I deficiencies. These extrapolations are flagged as *inferred* where they extend beyond direct C3-deficiency data.

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity limits epidemiology.** With <50 reported cases, there are no robust prevalence/incidence, sex-ratio, penetrance, or survival statistics; most data are anecdotal.
2. **Genotype–phenotype correlation is undefined.** Whether specific *C3* variant classes predispose to the infection-predominant vs autoimmune-predominant phenotype is unknown ("the genetic and phenotypic spectrum remains incompletely defined," [PMID: 42445183](https://pubmed.ncbi.nlm.nih.gov/42445183/)).
3. **Mechanistic extrapolation.** The autoimmune/type-I-interferon mechanism and the therapeutic rationale (anifrolumab) are strongest for C1q deficiency and are extended to C3 deficiency by inference, not by dedicated C3-deficiency trials.
4. **No disease-specific QoL or natural-history cohort data** exist.
5. **Model-organism gaps.** C3⁻/⁻ mice reproduce opsonization/humoral defects but not the full human infection + SLE spectrum; some models even reveal a *protective* C3 role in tissue inflammation, indicating context dependence.
6. **Secondary vs primary hypocomplementemia** remains a frequent diagnostic pitfall; many "low C3" reports in the literature are secondary and must not be conflated with primary deficiency.

---

## Proposed Follow-up Experiments / Actions

1. **Build an international C3-deficiency registry** aggregating all reported biallelic *C3* cases with harmonized genotype, complement phenotype (C3/C4/CH50/AH50), infection history, and autoimmune/renal outcomes to enable the first genotype–phenotype and natural-history analyses.
2. **Curate and ACMG-classify the full *C3* variant spectrum** (ClinVar/HGMD reconciliation), distinguishing LoF from hypomorphic alleles; correlate with residual C3 function.
3. **Prospectively evaluate vaccine responsiveness** (pneumococcal/meningococcal conjugate) in C3-deficient patients, informed by the mouse polysaccharide-response defect ([PMID: 12496386](https://pubmed.ncbi.nlm.nih.gov/12496386/)), to optimize immunization schedules.
4. **Test interferon-targeted therapy (anifrolumab)** or other IFN-axis interventions in C3-deficiency-associated SLE, formally extending the C1q-deficiency rationale ([PMID: 42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/)).
5. **Explore C3-replacement / gene-directed approaches** (plasma-derived C3, hepatocyte-directed gene therapy — the liver being the main synthesis site) as potential disease-modifying strategies, currently absent.
6. **Standardize the diagnostic algorithm** (undetectable C3 + normal C4 + low CH50/AH50 → regulator panel [factor H/I, factor B] → C3NeF assay → *C3* sequencing) to reliably separate primary from secondary hypocomplementemia.

---

*Report compiled from 12 verified findings and 50 reviewed papers over 5 investigation iterations. Ontology suggestions (MONDO:0013417, HGNC:1318, UniProt P01024, HPO/GO/CL/UBERON/NCIT terms) are provided throughout for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Complement_Component_3_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Complement_Component_3_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19640589` *(abstract only)*: "autoantibodies in MPGN are termed C3 Nephritic Factor (C3NeF)… directed against a neoepitope of the complement C3 convertase C3bBb… C3NeF stabilizes this convertase and this results in C3 amplification and complement activation"
  - closest text in source: "Autoantibodies in MPGN are termed C3 Nephritic Factor (C3NeF) and are directed against a neoepitope of the complement C3 convertase C3bBb"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (2 mentions) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000007` (2 mentions) - the report calls it "Autosomal recessive inheritance", "Autosomal recessive", "Inheritance:** **Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000007` - called "Autosomal recessive inheritance", "Autosomal recessive", "Inheritance:** **Autosomal recessive"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.

28 of 32 terms resolved to a current term; the rest could not be looked up either way.