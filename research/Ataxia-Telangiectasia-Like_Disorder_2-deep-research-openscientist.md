---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-10T18:19:21.881373'
end_time: '2026-09-10T18:38:46.539209'
duration_seconds: 1164.66
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Ataxia-Telangiectasia-Like Disorder 2
  mondo_id: MONDO:0014399
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 27
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014399
    reported_labels:
    - if available
    ontology_label: ataxia-telangiectasia-like disorder 2
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0006266
    ontology_label: obsolete DNA ligation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ataxia-Telangiectasia-Like_Disorder_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ataxia-Telangiectasia-Like_Disorder_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ataxia-Telangiectasia-Like Disorder 2
- **MONDO ID:** MONDO:0014399 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ataxia-Telangiectasia-Like Disorder 2** covering all of the
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

# Ataxia-Telangiectasia-Like Disorder 2 (ATLD2 / PCNA-Associated DNA Repair Disorder)

## Comprehensive Disease Characterization Report

**Disease:** Ataxia-Telangiectasia-Like Disorder 2 (ATLD2)
**Synonym:** PCNA-Associated DNA Repair Disorder (PARD)
**MONDO ID:** MONDO:0014399 · **OMIM:** #615919 · **Gene:** *PCNA* (HGNC:8729)
**Category:** Mendelian, autosomal recessive, ultra-rare

---

## Summary

Ataxia-telangiectasia-like disorder 2 (ATLD2), also termed PCNA-associated DNA repair disorder (PARD), is an ultra-rare autosomal-recessive multisystem DNA-repair disorder caused by biallelic hypomorphic missense variants in *PCNA*, the gene encoding the essential eukaryotic DNA sliding clamp. Two causal alleles have been reported: the Amish founder variant p.Ser228Ile (c.683C>T), described by Baple and colleagues in 2014 [PMID: 24911150](https://pubmed.ncbi.nlm.nih.gov/24911150/), and a second variant, p.Cys148Ser, described by Magrino and colleagues in 2023 [PMID: 36990216](https://pubmed.ncbi.nlm.nih.gov/36990216/). Because complete loss of PCNA is embryonic-lethal, both disease alleles are partial-loss-of-function (hypomorphic), preserving enough clamp function to permit development while impairing the DNA-maintenance functions that depend on faithful partner recruitment.

Mechanistically, PCNA is a homotrimeric ring that encircles DNA and serves as a mobile docking platform for more than 200 partner proteins, most of which bind through a short conserved motif called the PIP-box [PMID: 33984330](https://pubmed.ncbi.nlm.nih.gov/33984330/). The disease variants do not abolish DNA replication; instead, they selectively cripple PCNA's interactions with DNA-repair partners such as Flap endonuclease 1 (FEN1) and DNA Ligase 1 (LIG1), and they reduce PCNA thermostability and the amount of PCNA loaded onto chromatin. The structural basis of the S228I allele — a large conformational change that remodels the client-binding pocket — was solved by Duffy, Hilbert and Kelch in 2016 [PMID: 26688547](https://pubmed.ncbi.nlm.nih.gov/26688547/). The downstream consequence is defective nucleotide-excision repair (NER) and transcription-coupled repair, accumulation of unrepaired DNA damage, and progressive degeneration of vulnerable post-mitotic tissues — most prominently cerebellar neurons.

Clinically, ATLD2/PARD presents with a distinctive constellation of short stature, sensorineural hearing loss, premature aging, telangiectasia, progressive neurodegeneration (cerebellar ataxia), and cutaneous photosensitivity/UV sensitivity, overlapping with both the nucleotide-excision-repair disorders (Cockayne syndrome, xeroderma pigmentosum) and with ataxia-telangiectasia. It is distinguished from classical ataxia-telangiectasia (ATM) and from ATLD1 (MRE11) by normal alpha-fetoprotein, negative ATM testing, and its unique molecular cause. No disease-modifying therapy exists; management is supportive and multidisciplinary.

---

## Key Findings

### Finding 1 — ATLD2/PARD is caused by biallelic hypomorphic *PCNA* missense variants

ATLD2 is a monogenic disorder of the *PCNA* gene. The original description by Baple et al. (2014) identified a homozygous missense variant, c.683C>T (p.Ser228Ile), in an Amish kindred, establishing *PCNA* as the causal gene: *"resulting from a homozygous missense (p.Ser228Ile) sequence alteration of the proliferating cell nuclear antigen (PCNA)"* [PMID: 24911150](https://pubmed.ncbi.nlm.nih.gov/24911150/). Nearly a decade later, Magrino et al. (2023) reported a second, independent causal allele: *"we report a second PCNA substitution (C148S) that also causes PARD"* [PMID: 36990216](https://pubmed.ncbi.nlm.nih.gov/36990216/).

Both variants are hypomorphic (partial loss of function) rather than null. This is a mechanistic necessity: PCNA is essential for DNA replication in every proliferating cell, and complete loss of function is incompatible with embryonic development. The disease alleles therefore retain sufficient replicative clamp activity to permit survival while degrading the fidelity of DNA-maintenance functions. This places ATLD2 in the family of "essential-gene hypomorph" disorders, where the surviving phenotype reflects the most partner-sensitive and repair-dependent tissues rather than global replication failure.

- Variant 1: **NM_002592.2:c.683C>T, p.(Ser228Ile)** — Amish founder allele; missense; germline; classified pathogenic.
- Variant 2: **p.(Cys148Ser)** — second reported causal missense allele; missense; germline; pathogenic.

### Finding 2 — Cardinal clinical phenotype

The cardinal features of ATLD2/PARD were enumerated by Baple et al. (2014): *"the cardinal clinical features include short stature, hearing loss, premature aging, telangiectasia, neurodegeneration, and photosensitivity"* [PMID: 24911150](https://pubmed.ncbi.nlm.nih.gov/24911150/). The disorder therefore straddles two clinical categories — the DNA-repair "progeroid/photosensitivity" spectrum (Cockayne syndrome, xeroderma pigmentosum) and the ataxia-telangiectasia spectrum — and this hybrid presentation is itself a diagnostic clue.

Suggested HPO terms for the phenotypic spectrum:

| Phenotype | HPO term | Type | Onset | Course |
|---|---|---|---|---|
| Short stature | HP:0004322 | Physical manifestation | Childhood | Stable/constitutional |
| Sensorineural hearing loss | HP:0000407 | Clinical sign / lab (audiometry) | Childhood | Progressive |
| Premature aging / progeroid appearance | HP:0007495 / HP:0001025 | Physical manifestation | Childhood–adult | Progressive |
| Telangiectasia | HP:0001009 | Clinical sign | Childhood | Progressive |
| Cerebellar ataxia / neurodegeneration | HP:0001251 / HP:0002180 | Symptom / sign | Childhood | Progressive |
| Cutaneous photosensitivity / UV sensitivity | HP:0000992 | Clinical sign | Childhood | Chronic |

### Finding 3 — Molecular mechanism: impaired partner interactions and defective NER despite normal bulk replication

The defining mechanistic insight is that the disease variants uncouple PCNA's replicative function from its repair function. Baple et al. (2014) showed that p.Ser228Ile had no effect on PCNA protein levels or DNA replication, yet patient cells *"exhibited marked abnormalities in response to UV irradiation, displaying substantial reductions in both UV survival and RNA synthesis recovery"* [PMID: 24911150](https://pubmed.ncbi.nlm.nih.gov/24911150/). Reduced RNA-synthesis recovery after UV is a classic hallmark of defective transcription-coupled nucleotide-excision repair. The same study localized the biochemical lesion to partner binding: *"The p.Ser228Ile change also profoundly altered PCNA's interaction with Flap endonuclease 1 and DNA Ligase 1."*

Magrino et al. (2023) added a complementary and unifying dimension. The C148S variant, unlike S228I, has wild-type-like structure and partner affinity in vitro, yet it destabilizes the protein: *"The stability defect of both PARD variants indicates that PCNA levels are likely an important driver of PARD disease"* [PMID: 36990216](https://pubmed.ncbi.nlm.nih.gov/36990216/). Thus two mechanistically distinct alleles converge on the same functional endpoint — insufficient functional PCNA at sites of DNA repair — either by remodeling the partner-binding pocket (S228I) or by reducing the steady-state pool of chromatin-competent clamp (C148S, and to a degree S228I).

Relevant GO biological-process terms: nucleotide-excision repair (GO:0006289), transcription-coupled nucleotide-excision repair (GO:0006283), DNA replication (GO:0006260), base-excision repair (GO:0006284, via FEN1/LIG1), DNA ligation (GO:0006266).

### Finding 4 — PCNA is a sliding-clamp interaction hub coordinating >200 PIP-box partners

The vulnerability of PCNA to selective, partner-disrupting mutation follows from its biology as a promiscuous hub. Horsfall et al. (2021) established that human PCNA *"interacts with over 200 proteins through a conserved binding motif, the PIP-box, to orchestrate DNA replication and repair"* [PMID: 33984330](https://pubmed.ncbi.nlm.nih.gov/33984330/). Because all these partners compete for a small, overlapping surface, a single amino-acid change in or near that surface can re-weight the entire interactome — sparing some clients while excluding others. This "hub fragility" explains how a variant can leave replication intact while dismantling repair.

Suggested GO cellular-component terms: PCNA clamp / PCNA-containing complex (GO:0043626), nucleoplasm (GO:0005654), replication fork (GO:0005657), site of DNA damage (GO:0090734).

### Finding 5 — Structural basis: S228I produces a large conformational change that transforms the client-binding pocket

Duffy, Hilbert and Kelch (2016) solved the crystal structure of PCNA–S228I and revealed the physical mechanism behind the selective binding defect. The mutation lies near the site where most PCNA partners dock, and the structure *"reveals a large conformational change that dramatically transforms the binding pocket for PCNA client proteins"* [PMID: 26688547](https://pubmed.ncbi.nlm.nih.gov/26688547/). Critically, the effect is client-selective: the change *"markedly alters the binding energetics for some client proteins, while another, p21(CIP1), is only mildly affected."* This selectivity — a remodeled pocket that repels repair partners such as FEN1/LIG1 but still accommodates the high-affinity p21 PIP-box — provides the structural explanation for the finding that replication and cell-cycle control are largely preserved while repair collapses. The plasticity of the p21 PIP-box interaction with PCNA, mediated by Tyr151, has been characterized separately and underscores how differing partners tolerate pocket changes to differing degrees [PMID: 25972089](https://pubmed.ncbi.nlm.nih.gov/25972089/).

### Finding 6 — ATLD2 is one of several autosomal-recessive DNA-repair ataxias, distinguished from AT and ATLD1

Raslan et al. (2021) framed the nosology: ataxia-telangiectasia-like disorders are autosomal-recessive diseases that share clinical and pathophysiological features with classical ataxia-telangiectasia but are genetically distinct. Diagnostically, *"absence of telangiectasia, normal levels of alpha-fetoprotein and negative genetic test may direct to alternative diagnosis with similar phenotypes such as ataxia telangiectasia-like disorders (ATLD)"* [PMID: 33426167](https://pubmed.ncbi.nlm.nih.gov/33426167/). Within this family, ATLD1 is caused by *MRE11* mutations and ATLD2 by *PCNA*. Supporting clinical literature on the broader ATLD/DNA-repair-ataxia spectrum documents progressive cerebellar ataxia, oculomotor apraxia, cognitive impairment, and cerebellar atrophy on MRI [PMID: 24733832](https://pubmed.ncbi.nlm.nih.gov/24733832/), [PMID: 23436002](https://pubmed.ncbi.nlm.nih.gov/23436002/), [PMID: 23622410](https://pubmed.ncbi.nlm.nih.gov/23622410/).

### Finding 7 — Thermolability is a unifying disease mechanism; patient cells show temperature-dependent, UV-sensitive phenotypes

Magrino et al. (2023) demonstrated that the C148S variant has near-normal structure and affinity yet a thermostability defect, and that *"patient-derived cells homozygous for the C148S allele exhibit low levels of chromatin-bound PCNA and display temperature-dependent phenotypes"* [PMID: 36990216](https://pubmed.ncbi.nlm.nih.gov/36990216/). Combined with the UV-sensitivity of S228I patient cells (Finding 3), thermolability emerges as a unifying theme: reduced protein stability lowers the effective concentration of functional clamp available for repair. Hardebeck et al. (2023), in the course of developing a PCNA-inhibitor assay, framed the disease succinctly: *"ATLD2 is a neurodegenerative disease based on defects in DNA repair due to an impaired PCNA"* [PMID: 37511614](https://pubmed.ncbi.nlm.nih.gov/37511614/).

### Finding 8 — PCNA couples DNMT1 to replication sites: a plausible but untested epigenetic branch

Beyond canonical repair, PCNA is the S-phase docking platform for the maintenance-methylation machinery. Schneider et al. (2013) showed that DNMT1's *"proliferating cell nuclear antigen (PCNA)-binding domain (PBD) and the targeting sequence (TS) domain, target Dnmt1 to the replication sites in S phase"* [PMID: 23535145](https://pubmed.ncbi.nlm.nih.gov/23535145/). Because DNMT1 recruitment depends on PCNA, hypomorphic PCNA could in principle perturb the fidelity of maintenance DNA methylation during replication — an epigenetic branch that is mechanistically plausible but has **not** been directly demonstrated in ATLD2 patient tissues. This is flagged as an inference, not an established mechanism. The parallel UHRF1/Np95 pathway that reinforces DNMT1 loading onto hemimethylated DNA provides additional context for how maintenance methylation is coordinated at the replication fork [PMID: 17994007](https://pubmed.ncbi.nlm.nih.gov/17994007/).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic *PCNA* missense variant** (p.Ser228Ile or p.Cys148Ser) is inherited in an autosomal-recessive manner — *the initiating germline lesion*.
2. This **leads to** an altered PCNA protein: S228I undergoes a large conformational change that remodels the client-binding pocket (demonstrated, [PMID: 26688547]); C148S is near-normal in structure but thermolabile (demonstrated, [PMID: 36990216]).
3. The altered protein **results in** reduced PCNA thermostability and, for both alleles, lower levels of chromatin-bound PCNA — i.e., a smaller effective pool of functional clamp at DNA (demonstrated, [PMID: 36990216]).
4. In parallel, the S228I pocket change **results in** selectively weakened binding of repair partners FEN1 and DNA Ligase 1, while sparing p21 and bulk replication (demonstrated, [PMID: 24911150]; [PMID: 26688547]).
5. Reduced repair-partner recruitment **leads to** defective nucleotide-excision repair and transcription-coupled repair, evidenced by reduced UV survival and impaired RNA-synthesis recovery in patient cells (demonstrated, [PMID: 24911150]).
6. Defective repair **results in** accumulation of unrepaired DNA damage (endogenous and UV-induced) in cells — *inferred from the repair defect*.
7. **Branch A (neural):** Post-mitotic neurons — which have intrinsically low NER capacity and cannot dilute damage by division [PMID: 17236820] — accumulate damage and **lead to** progressive cerebellar neurodegeneration and ataxia (neuronal vulnerability demonstrated in general; cerebellar tropism in ATLD2 inferred).
8. **Branch B (cutaneous):** UV-hypersensitive skin **leads to** photosensitivity and telangiectasia.
9. **Branch C (systemic/progeroid):** Genome-maintenance failure in dividing and aging tissues **leads to** short stature, sensorineural hearing loss, and premature aging.
10. **Branch D (epigenetic, inferred only):** Impaired PCNA-dependent recruitment of DNMT1 to replication sites *could* perturb maintenance DNA methylation [PMID: 23535145] — not demonstrated in patients.

### Schematic

```
  Biallelic PCNA hypomorph (S228I / C148S)
                 │
        ┌────────┴─────────┐
   S228I: pocket        C148S: thermolabile
   conformational       (WT-like structure)
   change                    │
        └────────┬───────────┘
                 ▼
   ↓ chromatin-bound / functional PCNA
   + selective loss of FEN1 / LIG1 binding
                 │
                 ▼
   Defective NER / transcription-coupled repair
   (↓UV survival, ↓RNA-synthesis recovery)
                 │
                 ▼
        Accumulated DNA damage
                 │
   ┌─────────────┼─────────────┬───────────────┐
   ▼             ▼             ▼               ▼
Neurons      Skin (UV)     Growth/aging    (Epigenetic?
→ cerebellar → photo-      → short stature   DNMT1 mis-
  ataxia,      sensitivity,  hearing loss,   loading —
  neuro-       telangiec-    premature       INFERRED,
  degeneration tasia         aging           untested)
```

### Upstream vs downstream

- **Upstream (cause):** the *PCNA* genotype and its biophysical consequences (pocket remodeling, thermolability, reduced chromatin loading, lost partner binding).
- **Downstream (effect):** repair failure → DNA-damage accumulation → tissue-specific degeneration → the clinical phenotype.

**Cell types (CL) implicated:** cerebellar neuron / Purkinje cell (CL:0000121), neuron (CL:0000540), astrocyte (CL:0000127), fibroblast (CL:0000057, the principal experimental cell type), keratinocyte (CL:0000312, UV target).
**Anatomy (UBERON):** cerebellum (UBERON:0002037), central nervous system (UBERON:0001017), skin (UBERON:0002097), cochlea/inner ear (UBERON:0001844).
**Subcellular (GO CC):** nucleus (GO:0005634), replication fork (GO:0005657), sites of DNA damage (GO:0090734).

---

## Section-by-Section Synthesis

### 1. Disease Information
ATLD2/PARD is an ultra-rare autosomal-recessive multisystem DNA-repair disorder. Identifiers: **MONDO:0014399**, **OMIM #615919**, gene *PCNA* (**HGNC:8729**). Synonyms: PCNA-associated DNA repair disorder (PARD), ataxia-telangiectasia-like disorder 2. Knowledge is derived from aggregated disease-level resources (OMIM, Orphanet) and a small number of primary reports describing individual patients/kindreds (Amish S228I cohort; C148S cases), not from large EHR datasets.

### 2. Etiology
**Causal factor:** genetic — biallelic hypomorphic missense variants in *PCNA*. **Genetic risk factor:** carriage of two pathogenic *PCNA* alleles; in the Amish population, a founder effect concentrates the S228I allele, and consanguinity/endogamy raises homozygosity risk. **Environmental modifier:** UV/sunlight exposure exacerbates the cutaneous photosensitivity component (a gene–environment interaction: an inherited repair defect renders UV-induced lesions pathogenic). No protective genetic or environmental factors have been established. Sun avoidance is the only plausible environmental risk-reduction lever.

### 3. Phenotypes
See Finding 2 table. All features are childhood-onset, progressive for the neurodegenerative and sensory components, and constitutional for short stature. Frequencies are qualitative given the tiny patient population; cardinal features were consistent across the original Amish kindred. Quality-of-life impact is dominated by progressive ataxia (mobility, independence), hearing loss (communication), and the psychosocial burden of a progeroid, multisystem, incurable condition.

### 4. Genetic / Molecular Information
**Causal gene:** *PCNA* (chromosome 20p12.3). **Variants:** c.683C>T p.(Ser228Ile) and p.(Cys148Ser); both missense, germline, pathogenic; functional consequence is partial loss of function (hypomorph) via pocket remodeling (S228I) and reduced thermostability/chromatin loading (both). Population allele frequency is vanishingly rare in gnomAD (consistent with an ultra-rare recessive disorder); S228I is enriched only within the Amish founder population. No modifier genes, chromosomal abnormalities, or aneuploidy are implicated. A PCNA-dependent epigenetic (DNMT1/maintenance-methylation) branch is plausible but untested.

### 5. Environmental Information
No infectious or toxic etiology. The only relevant environmental factor is **UV radiation**, which converts the underlying NER defect into clinical photosensitivity. No lifestyle or occupational exposures are established causes.

### 6. Mechanism / Pathophysiology
Presented as the ordered causal chain above. Core molecular processes: nucleotide-excision repair (GO:0006289) and transcription-coupled repair (GO:0006283) failure secondary to disrupted PCNA–partner (FEN1/LIG1) interactions and reduced functional clamp levels; downstream DNA-damage accumulation and post-mitotic neuronal degeneration.

### 7. Anatomical Structures Affected
**Primary:** cerebellum (UBERON:0002037) / nervous system; skin (UBERON:0002097); inner ear/cochlea (UBERON:0001844). **Secondary/systemic:** skeletal growth (short stature); generalized progeroid changes. **Cells:** cerebellar neurons/Purkinje cells (CL:0000121), fibroblasts (CL:0000057), keratinocytes (CL:0000312). **Subcellular:** nucleus, replication fork, DNA-damage sites. Lateralization: bilateral/symmetric (cerebellar, cutaneous).

### 8. Temporal Development
**Onset:** childhood, insidious/chronic. **Course:** progressive neurodegeneration and hearing loss; constitutional short stature; chronic lifelong disease. No spontaneous remission; no formally defined "stages" given rarity — natural history is described only from small cohorts.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** presumed high/complete for biallelic carriers (based on limited cases). **Expressivity:** likely variable across alleles (S228I vs C148S have distinct biophysics). **Founder effect:** S228I in the Old Order Amish. **Consanguinity/endogamy** increases risk. **Prevalence:** not formally estimated — ultra-rare (fewer than ~20 reported individuals worldwide). **Carrier frequency:** elevated only within the Amish founder population; negligible elsewhere. No sex bias expected for an autosomal-recessive disorder.

### 10. Diagnostics
**Genetic testing is definitive:** targeted *PCNA* sequencing, gene panels for hereditary ataxia / DNA-repair disorders, or WES/WGS. **Cellular/functional assays** support the diagnosis: reduced UV survival and impaired post-UV RNA-synthesis recovery in patient fibroblasts; reduced chromatin-bound PCNA; temperature-dependent cellular phenotypes. **Distinguishing labs:** normal alpha-fetoprotein and negative *ATM* testing separate ATLD from classical ataxia-telangiectasia [PMID: 33426167]. **Imaging:** brain MRI shows cerebellar atrophy (as in related DNA-repair ataxias). **Differential diagnosis:** ataxia-telangiectasia (ATM), ATLD1 (MRE11), ataxia with oculomotor apraxia types 1/2, Cockayne syndrome, xeroderma pigmentosum, trichothiodystrophy.

### 11. Outcome / Prognosis
Chronic, progressive, lifelong. Neurodegeneration and sensory loss drive morbidity and disability; no curative therapy exists. Formal survival/mortality statistics are unavailable given the tiny population. Prognosis is guarded, with progressive functional decline; prognostic biomarkers are not established.

### 12. Treatment
**No disease-modifying therapy exists.** Management is **supportive and multidisciplinary** (NCIT: Supportive Care): physical, occupational, and speech therapy for ataxia; audiology and hearing aids/cochlear support for hearing loss; dermatologic surveillance and **rigorous photoprotection** for UV sensitivity; growth and endocrine monitoring; genetic counseling. No pharmacotherapy, gene therapy, cell therapy, or RNA-based therapy is approved or in trials for ATLD2. PCNA is being explored as a small-molecule inhibitor target in oncology (not as therapy for ATLD2), and assay development in that space has incidentally characterized ATLD2 disease biology [PMID: 37511614].

### 13. Prevention
**Primary prevention:** genetic counseling, carrier screening in at-risk (e.g., Amish founder) populations, and reproductive options including prenatal or preimplantation genetic testing for known familial variants. **Secondary:** early molecular diagnosis to enable supportive intervention. **Tertiary:** photoprotection to limit UV-driven cutaneous damage; rehabilitation to preserve function. No vaccine or population public-health measure is applicable.

### 14. Other Species / Natural Disease
*PCNA* is deeply and essentially conserved across eukaryotes; orthologs exist in mouse (*Pcna*), rat, zebrafish, *Drosophila*, *C. elegans*, and yeast. The bacterial functional analog is the β-clamp — a structurally distinct protein but a conceptual parallel as a sliding-clamp interaction hub that binds partners through a conserved clamp-binding motif [PMID: 38814467](https://pubmed.ncbi.nlm.nih.gov/38814467/). No naturally occurring ATLD2-equivalent disease is documented in companion animals or wildlife (OMIA), reflecting the specificity of the human hypomorphic alleles.

### 15. Model Organisms
No published animal model specifically recapitulates ATLD2. The principal experimental systems are **patient-derived fibroblasts and lymphoblasts** (in vitro), which display the UV-sensitivity, reduced chromatin-bound PCNA, and temperature-dependent phenotypes that define the disorder [PMID: 24911150; 36990216]. **Recombinant PCNA biochemistry and X-ray crystallography** provided the structural mechanism [PMID: 26688547]. Because complete *Pcna* knockout is embryonic-lethal, any faithful mouse model would need to be a knock-in of the specific hypomorphic allele (S228I or C148S) — a clear and feasible gap for future work.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [24911150](https://pubmed.ncbi.nlm.nih.gov/24911150/) | *Hypomorphic PCNA mutation underlies a human DNA repair disorder* | Landmark: defines the disease, identifies S228I, cardinal phenotype, NER defect, FEN1/LIG1 disruption |
| [36990216](https://pubmed.ncbi.nlm.nih.gov/36990216/) | *A thermosensitive PCNA allele underlies an ataxia-telangiectasia-like disorder* | Second causal allele C148S; thermolability as unifying mechanism; reduced chromatin-bound PCNA |
| [26688547](https://pubmed.ncbi.nlm.nih.gov/26688547/) | *A Disease-Causing Variant in PCNA Disrupts a Promiscuous Protein Binding Site* | Crystal structure of S228I; large conformational change remodels client pocket; client-selective effect |
| [33984330](https://pubmed.ncbi.nlm.nih.gov/33984330/) | *Unlocking the PIP-box…* | Establishes PCNA as a >200-partner PIP-box hub — basis for hub fragility |
| [33426167](https://pubmed.ncbi.nlm.nih.gov/33426167/) | *…How to Identify the Ataxia Telangiectasia-Like Disorders* | Nosology and diagnostic differentiation from AT (AFP, ATM testing) |
| [37511614](https://pubmed.ncbi.nlm.nih.gov/37511614/) | *A FRET-Based Assay for the Identification of PCNA Inhibitors* | Frames ATLD2 as a DNA-repair neurodegenerative disease; PCNA druggability context |
| [23535145](https://pubmed.ncbi.nlm.nih.gov/23535145/) | *Dissection of cell cycle-dependent dynamics of Dnmt1…* | PCNA recruits DNMT1 to replication sites — basis for inferred epigenetic branch |
| [17236820](https://pubmed.ncbi.nlm.nih.gov/17236820/) | *Neurons and astrocytes exhibit lower GG-NER than fibroblasts* | Explains neuronal vulnerability to repair deficiency |
| [24733832](https://pubmed.ncbi.nlm.nih.gov/24733832/) | ATLD clinical case (hypogonadism/hypersegmented neutrophils) | Clinical context for the ATLD spectrum |
| [23436002](https://pubmed.ncbi.nlm.nih.gov/23436002/) | Italian ATLD siblings, long clinical course | Natural-history context (ataxia, oculomotor apraxia) |
| [23622410](https://pubmed.ncbi.nlm.nih.gov/23622410/) | Progressive cerebellar atrophy / hereditary ataxias | Imaging/DNA-repair ataxia context (cerebellar atrophy) |
| [17994007](https://pubmed.ncbi.nlm.nih.gov/17994007/) | *Np95 mediates epigenetic inheritance by recruiting Dnmt1* | Supports maintenance-methylation machinery context |
| [38814467](https://pubmed.ncbi.nlm.nih.gov/38814467/) | β-clamp structure/interactions review | Comparative sliding-clamp biology |
| [25972089](https://pubmed.ncbi.nlm.nih.gov/25972089/) | *p21 exploits Tyr151 as a tether for high-affinity PCNA binding* | PIP-box affinity/plasticity; why p21 is spared |

**Evidence-type distribution:** Human clinical + patient-cell (in vitro): PMIDs 24911150, 36990216, 33426167, 24733832, 23436002, 23622410. Structural/biochemical (in vitro/computational): 26688547, 33984330, 25972089, 38814467, 37511614. Model-system/mechanistic (in vitro): 23535145, 17994007, 17236820.

---

## Limitations and Knowledge Gaps

1. **Extremely small evidence base.** The disease is defined by two alleles and a handful of individuals (predominantly one Amish kindred plus C148S cases). Penetrance, expressivity, prevalence, and natural-history parameters are therefore anecdotal, not statistical.
2. **No animal model.** No knock-in mouse or other organism reproduces ATLD2; tissue-specific mechanisms (especially cerebellar tropism) are inferred from patient cells and general neuron-NER biology rather than directly demonstrated in vivo.
3. **Cerebellar selectivity is unexplained at the molecular level.** Why the cerebellum is preferentially affected — beyond the general observation that post-mitotic neurons have low NER — is not established for ATLD2 specifically.
4. **The epigenetic branch is inferential.** PCNA–DNMT1 coupling is well established biochemically, but altered maintenance methylation has not been measured in ATLD2 patient tissues.
5. **No biomarkers or therapeutics.** There are no validated prognostic biomarkers and no disease-modifying treatment; management is entirely supportive.
6. **Allele-specific mechanism heterogeneity.** S228I (pocket remodeling) and C148S (thermolability) act through partly different biophysics; whether they produce identical clinical courses is unknown given sample size.

---

## Proposed Follow-up Experiments / Actions

1. **Generate allele-specific knock-in mouse models** (Pcna^S228I and Pcna^C148S), including conditional/neuron-restricted alleles, to test cerebellar vulnerability in vivo and produce a preclinical platform.
2. **iPSC-derived cerebellar organoids / Purkinje neurons** from patient fibroblasts to model neuron-specific damage accumulation and screen candidate neuroprotective interventions.
3. **Directly measure DNA methylation** (whole-genome bisulfite / EM-seq) in patient cells to confirm or refute the inferred DNMT1/epigenetic branch (Finding 8).
4. **Quantitative interactome mapping** (BioID or IP-MS of mutant vs WT PCNA on chromatin) to define the full re-weighted partner set beyond FEN1/LIG1 and identify additional impaired repair pathways.
5. **Structural and biophysical characterization of C148S–chromatin dynamics** and clamp-loading efficiency to complement the existing S228I crystal structure and test the thermolability model at the loading step.
6. **Establish an international patient registry** to capture natural history, penetrance, expressivity, imaging, and audiologic progression — essential given the ultra-rare status.
7. **Explore proteostasis/temperature-buffering strategies** for the thermolabile C148S allele and small molecules that stabilize the mutant PCNA fold, as candidate disease-modifying approaches.

---

*Report compiled from an autonomous multi-iteration literature-based investigation. All mechanistic and clinical claims are attributed to the cited primary literature (PMIDs). Inferred steps (cerebellar-tropism specifics, epigenetic branch) are explicitly flagged as not yet demonstrated in ATLD2.*


## Artifacts

- [OpenScientist final report](Ataxia-Telangiectasia-Like_Disorder_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ataxia-Telangiectasia-Like_Disorder_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

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
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014399` (3 mentions) - the report calls it "if available"; MONDO calls it **ataxia-telangiectasia-like disorder 2**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006266` (obsolete DNA ligation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000992` (1 mention) - the report calls it "Cutaneous photosensitivity / UV sensitivity"; HP calls it **Cutaneous photosensitivity**
