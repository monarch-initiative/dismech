---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T04:08:13.396554'
end_time: '2026-09-25T04:24:26.253942'
duration_seconds: 972.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: African Tick-Bite Fever
  mondo_id: MONDO:0000227
  category: Infectious Disease
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
citation_count: 32
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 20
  quotes_valid: 19
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:19379498
  relevance_assessed: 32
  on_topic: 26
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0012133
    reported_labels:
    - Myocarditis
    ontology_label: Erythroid hypoplasia
  - term_id: UBERON:0000029
    reported_labels:
    - regional lymph nodes
    - Lymphatic system:** draining **regional lymph nodes
    ontology_label: lymph node
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: African_Tick-Bite_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: African_Tick-Bite_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** African Tick-Bite Fever
- **MONDO ID:** MONDO:0000227 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **African Tick-Bite Fever** covering all of the
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

# African Tick-Bite Fever (ATBF) — Comprehensive Disease Characterization

**Disease:** African Tick-Bite Fever · **MONDO ID:** MONDO:0000227 · **Category:** Infectious Disease (zoonotic, vector-borne rickettsiosis)
**Causative agent:** *Rickettsia africae* (spotted-fever group) · **Vectors:** *Amblyomma hebraeum*, *Amblyomma variegatum*

---

## Summary

African Tick-Bite Fever (ATBF) is an acute, usually mild and self-limited zoonotic **spotted-fever-group (SFG) rickettsiosis** caused by the obligate intracellular Gram-negative bacterium ***Rickettsia africae***. It is transmitted by aggressive, host-hunting ticks of the genus ***Amblyomma*** — principally *A. hebraeum* (southern Africa) and *A. variegatum* (West, Central and East Africa, and the eastern Caribbean). Because *Amblyomma* ticks actively hunt and attack hosts in clusters, ATBF characteristically produces **multiple inoculation eschars** and **simultaneous illness among groups of co-travelers**, two features considered pathognomonic. The disease is overwhelmingly reported in returning travelers to rural sub-Saharan Africa (especially South Africa) and is the second most common cause of febrile illness after malaria in ill returned travelers from that region.

Mechanistically, ATBF is a **rickettsial vasculitis**. *R. africae* infects vascular endothelial cells, triggering an IL-1α–dependent proinflammatory cytokine cascade (IL-6, IL-8) that produces vascular inflammation, loss of vascular integrity, and increased permeability. At the site of the tick bite, endothelial infection and a lymphohistiocytic/granulomatous vasculitis produce dermal necrosis — the clinical **eschar (tache noire)**. Systemically, the same endothelial process, amplified by cytokine release, produces fever, headache, myalgia, regional lymphadenopathy, and a variable maculopapular or vesicular rash 5–10 days after the bite. Notably, *R. africae* is a comparatively **low-virulence** pathogen; comparative genomics shows it possesses one of the least gene-decayed rickettsial genomes and does not impair the fitness of its tick vector — consistent with the hypothesis that rickettsial virulence increases with genome reduction.

ATBF has **no human genetic component** — it is a purely infectious/environmental disease driven by occupational and recreational tick exposure in endemic rural areas. Diagnosis is largely clinical at presentation (serology is insensitive in the first 1–2 weeks and cross-reacts across the SFG), with confirmation by **eschar-swab PCR** (which remains positive even after doxycycline is started) or convalescent immunofluorescence antibody assay. Treatment with **doxycycline** yields an excellent prognosis; complications (lymphangitis, myocarditis, suspected CNS involvement, secondary cellulitis, prolonged convalescence) are uncommon and concentrated in older patients, and deaths are essentially unreported. Prevention relies entirely on **personal anti-tick protection** (repellents, permethrin-treated clothing, prompt tick removal); no vaccine exists.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** ATBF is an acute febrile zoonotic illness caused by *Rickettsia africae*, an obligate intracellular SFG rickettsia, transmitted by *Amblyomma* ticks. The clinical syndrome comprises fever, one or (characteristically) several inoculation eschars, regional lymphadenopathy, and a variable rash. "Caused by *Rickettsia africae*, African tick bite fever presents with characteristic cutaneous findings such as eschar (tache noir) and a rash" ([PMID: 30537329](https://pubmed.ncbi.nlm.nih.gov/30537329/)).

**Key identifiers.**
- **MONDO:** MONDO:0000227
- **MeSH:** Indexed under spotted fever group / tick-borne rickettsial diseases.
- **ICD-10:** A77.8 (Other spotted fevers) is the applicable rubric; ICD-11 maps to "Spotted fever due to *Rickettsia africae*."
- **OMIM / Orphanet:** Not a Mendelian disorder; no OMIM gene/phenotype entry. As an infectious disease it is not a classic Orphanet rare-disease entry.
- **Causative organism (NCBI Taxonomy):** *Rickettsia africae* (species within genus *Rickettsia*, SFG).

**Synonyms / alternative names.** African tick-bite fever; African tick bite fever; *Rickettsia africae* infection; SFG rickettsiosis due to *R. africae*. Historically conflated with "tick bite fever" / boutonneuse-like fever in southern Africa before *R. africae* was recognized as a distinct species ([PMID: 9916419](https://pubmed.ncbi.nlm.nih.gov/9916419/), [PMID: 31700846](https://pubmed.ncbi.nlm.nih.gov/31700846/)).

**Source of information.** The disease-level knowledge base is derived almost exclusively from **aggregated case reports and case series of returning travelers** plus tick-surveillance/meta-analytic studies — not from EHR/population cohorts. "Human disease case reports were exclusively among returning travellers from non-endemic areas, which limits our disease knowledge among at-risk populations: people living in endemic regions" ([PMID: 38813598](https://pubmed.ncbi.nlm.nih.gov/38813598/)).

---

### 2. Etiology

**Primary cause (infectious).** ATBF is caused by infection with *Rickettsia africae*, transmitted through the bite of an infected *Amblyomma* tick. "This pathogen is transmitted by ticks of the genus *Amblyomma*, with *Amblyomma hebraeum* and *Amblyomma variegatum* being the major vectors" ([PMID: 34516408](https://pubmed.ncbi.nlm.nih.gov/34516408/)).

**Risk factors (environmental / behavioral).**
- **Occupational and recreational exposure to *Amblyomma*-infested rural habitats**: game hunting, safaris, ecotourism, farming, military deployment in sub-Saharan Africa. Multiple-eschar case clusters are repeatedly reported after safaris and game hunting ([PMID: 28544092](https://pubmed.ncbi.nlm.nih.gov/28544092/), [PMID: 20233665](https://pubmed.ncbi.nlm.nih.gov/20233665/)).
- **Geography and season**: rural southern/eastern Africa (highest), West/Central Africa, and the eastern Caribbean/French West Indies.
- **Vector behavior**: *Amblyomma* ticks actively hunt hosts and attack in clusters, so travelers in groups are frequently co-infected.
- **Age/sex**: no strong sex predilection; most reported cases are middle-aged adult travelers, but children are affected (a cluster of 3 children aged 7–16 after a hunting safari) ([PMID: 28544092](https://pubmed.ncbi.nlm.nih.gov/28544092/)). Older age is associated with more severe manifestations and slower recovery ([PMID: 18558881](https://pubmed.ncbi.nlm.nih.gov/18558881/)).

**Genetic risk factors.** **None identified.** ATBF is not a heritable disease; there are no known human causal variants, susceptibility loci, or modifier genes. Host-genetic susceptibility to ATBF has not been demonstrated.

**Protective factors.** No genetic protective factors are known. Environmental protection is behavioral: use of tick repellents, permethrin-treated clothing, protective clothing, and prompt tick removal (Section 13). No dietary or metabolic protective factors are established.

**Gene–environment interactions.** Not applicable — the disease has no established genetic axis.

---

### 3. Phenotypes

ATBF is a monophasic acute febrile illness. Phenotype frequencies (pooled from case series and reviews):

| Phenotype | Type | Frequency | Suggested HPO term |
|---|---|---|---|
| Fever | Symptom/sign | ~75–100% | Fever (HP:0001945) |
| Inoculation eschar (tache noire) | Physical manifestation | 53–100% (≥1); multiple in 21–54% | Skin ulcer (HP:0200042); Skin necrosis |
| Regional lymphadenopathy | Sign | Common | Localized lymphadenopathy (HP:0100762); Lymphadenopathy (HP:0002716) |
| Maculopapular / vesicular rash | Manifestation | 15–46% (up to 87.5% in one elderly series) | Maculopapular exanthema (HP:0040186); Vesicular rash |
| Headache | Symptom | Frequent | Headache (HP:0002315) |
| Myalgia | Symptom | Frequent | Myalgia (HP:0003326) |
| Chills | Symptom | ~87.5% (elderly series) | — |
| Enanthema (mucosal) | Sign | ~50% of those with rash | Oral mucosal blistering / enanthem |
| Lymphangitis | Sign | Uncommon | Lymphangitis |
| Fatigue / prolonged asthenia | Symptom | Variable; may persist in convalescence | Fatigue (HP:0012378) |
| Neck stiffness | Sign | Occasional | Nuchal rigidity (HP:0031179) |
| Myocarditis / suspected CNS involvement | Complication | Rare (mostly elderly) | Myocarditis (HP:0012133) |

**Characteristics.** *Onset:* adult-onset in the reported population; acute, ~5–10 days after tick bite. *Severity:* usually mild; moderate/severe manifestations rare and skewed to older patients. *Progression:* self-limited single episode; resolves with treatment (and often spontaneously). *Frequency:* eschar is the most consistent feature.

Quantitative anchors: "the presence of at least one inoculation eschar is observed in 53-100% of cases and multiple eschars in 21-54%" and "a cutaneous rash is described in 15-46% of cases" ([PMID: 20233665](https://pubmed.ncbi.nlm.nih.gov/20233665/)). In an elderly-traveler series, "Rash was frequent (present in 87.5% of patients), vesicular (in 100% of patients with rash), and often associated with an enanthema (in 50% of patients with rash)" ([PMID: 18558881](https://pubmed.ncbi.nlm.nih.gov/18558881/)).

**Pathognomonic features.** "the presence of multiple inoculation eschars, two features pathognomonic of this rickettsial disease" — multiple eschars plus clustered co-traveler infections ([PMID: 20233665](https://pubmed.ncbi.nlm.nih.gov/20233665/)).

**Quality-of-life impact.** Generally limited and transient: an acute febrile week, occasionally with prolonged asthenia during a slow convalescence ("complete recovery was slow"; [PMID: 18558881](https://pubmed.ncbi.nlm.nih.gov/18558881/)). Long-term disability is not a feature. Disease-specific QoL instruments (EQ-5D/SF-36) have not been applied to ATBF.

---

### 4. Genetic / Molecular Information

**Human genetics: not applicable.** ATBF has no causal genes, pathogenic variants, modifier genes, epigenetic signatures, or chromosomal abnormalities in the human host. There are no ClinVar/OMIM/HGMD entries; allele-frequency, germline/somatic, penetrance and expressivity concepts do not apply.

**Pathogen genomics (the relevant "molecular information").** Whole-genome sequencing of *R. africae* reveals a circular chromosome of **1,278,540 bp** plus an unstable **12,377-bp plasmid** (GenBank NZ_AAUY01000001). Comparative genomics against *R. prowazekii*, *R. rickettsii*, and *R. conorii* shows *R. africae* has **one of the least-decayed rickettsial genomes**, with **18 species-unique genes**, one carrying a putative protease domain upregulated at 37 °C. Clonality was assessed across 70 patients and 155 ticks. The central inference: "we speculate that in *Rickettsia* species virulence is mostly associated with gene loss" ([PMID: 19379498](https://pubmed.ncbi.nlm.nih.gov/19379498/)) — i.e., *R. africae*'s relatively intact genome underlies its mild phenotype.

**Molecular typing / targets.** Species confirmation and phylogenetics use the citrate synthase gene (*gltA*), outer-membrane protein genes (*ompA*, *ompB*), and the 17-kDa antigen gene. *R. africae* clusters within the SFG subgroup containing the major human pathogens by *gltA* phylogeny ([PMID: 9103608](https://pubmed.ncbi.nlm.nih.gov/9103608/)).

---

### 5. Environmental Information

**Environmental factors.** The dominant environmental determinant is presence in *Amblyomma*-infested rural landscapes of sub-Saharan Africa (grassland, bush, game reserves, farmland) and the eastern Caribbean. No chemical toxin, pollutant, or radiation exposure contributes.

**Lifestyle factors.** Activities that increase tick contact: safari/ecotourism, big-game hunting, farming/animal husbandry, and rural fieldwork. Failure to use repellents or protective clothing increases risk.

**Infectious agent.** ***Rickettsia africae*** — obligate intracellular SFG rickettsia. It is "a bacterium of zoonotic importance, which causes African tick bite fever (ATBF) in humans" ([PMID: 34516408](https://pubmed.ncbi.nlm.nih.gov/34516408/)). Reservoir/vector = *Amblyomma* ticks; livestock and wildlife amplify the transmission cycle (Sections 9/14). Relevant chemical entities (CHEBI) appear in Sections 12–13 (doxycycline; DEET, icaridin, PMD, IR3535, permethrin).

---

### 6. Mechanism / Pathophysiology

#### Ordered causal chain

1. An infected *Amblyomma* tick **actively hunts and attacks the host**, often multiple ticks in a cluster → **inoculates *R. africae* into the dermis** at one or several bite sites (→ predisposes to *multiple* eschars).
2. *R. africae*, an obligate intracellular bacterium, **adheres to and invades vascular endothelial cells** at the bite site (the O-antigen/polysaccharide-synthesis operon modulates adhesion/invasion) → *leads to* intracellular replication within endothelium.
3. Endothelial infection **activates an IL-1α–dependent proinflammatory program** → *results in* secretion of IL-6 and IL-8 (and other chemokines) by infected endothelial cells.
4. Cytokine/chemokine release **recruits perivascular T cells (CD3+) and histiocytes (CD68+)** and **triggers lymphohistiocytic/granulomatous vasculitis** → *leads to* loss of vascular integrity and increased permeability ("rickettsial vasculitis").
5. Local vasculitis with fibrin thrombi and vacuolar change **causes necrosis of the epidermis and superficial dermis** → *results in* the clinical **eschar (tache noire)** with **draining regional lymphadenopathy**.
6. In parallel (branch), the same endothelial-tropic process and systemic cytokines **produce fever, headache, myalgia**, and — where dissemination occurs — a **maculopapular/vesicular rash**.
7. Because *R. africae* has a relatively intact genome and limits damage, the process is usually **contained and self-limiting**; severe systemic vasculitis (myocarditis, CNS) is rare (branch, mostly in elderly). *[Systemic-dissemination steps are inferred from SFG-rickettsiosis biology; the endothelial/eschar steps are directly demonstrated in SFG lesions.]*

#### Detail by category

- **Molecular pathways / cellular processes.** Endothelial innate-immune activation via an **IL-1α–dependent pathway** drives NF-κB–type cytokine responses. "human umbilical vein endothelial cells (HUVEC) infected with *R. conorii* actively secrete high levels of IL-8 and IL-6" (IL-8 P<0.002; IL-6 P<0.03 vs uninfected; 80–85% suppressed by IL-1 receptor antagonist/anti-IL-1α) ([PMID: 8675654](https://pubmed.ncbi.nlm.nih.gov/8675654/)). Suggested GO terms: inflammatory response (GO:0006954), cytokine-mediated signaling pathway (GO:0019221), response to bacterium (GO:0009617).
- **Endothelial tropism / tissue damage.** "a majority of sequelae associated with human rickettsioses are the outcome of the pathogen's affinity for endothelium lining the blood vessels, the consequences of which are vascular inflammation, insult to vascular integrity and compromised vascular permeability, collectively termed 'Rickettsial vasculitis'" ([PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)).
- **Immune evasion / protein-level mechanism.** The **polysaccharide synthesis operon (pso)** governs O-antigen biosynthesis and surface-protein assembly and shields LPS/peptidoglycan from immune recognition, modulating adhesion/invasion and innate stimulation — its loss (variant HK2) reduces invasion but provokes stronger cytokine responses and premature host-cell death ([PMID: 40570043](https://pubmed.ncbi.nlm.nih.gov/40570043/)).
- **Low-virulence genomic basis.** *R. africae*'s benign phenotype tracks with minimal genome decay; "the mild pathogen *R. africae*, the agent of African tick-bite fever, which does not affect the fitness of its tick vector" ([PMID: 19379498](https://pubmed.ncbi.nlm.nih.gov/19379498/)).
- **Histopathology (eschar correlate).** In immunostain-confirmed SFG rickettsial skin lesions, "Vacuolar alterations and vasculitis were present in all specimens (6/6; 100%)," granulomatous inflammation in 83.3%, fibrin thrombi/extravasated RBCs in 50%, epidermal/superficial-dermal necrosis in 33.3%; perivascular CD3+ T cells with fewer CD20+ B cells and abundant CD68+ histiocytes (83.3%). "The histopathology of rickettsialpox infection is septic lymphocytic and granulomatous vasculitis" ([PMID: 31955452](https://pubmed.ncbi.nlm.nih.gov/31955452/)).

**Cell types (CL) and biological processes (GO):** vascular endothelial cell (CL:0000115) — primary target; T cell (CL:0000084); macrophage/histiocyte (CL:0000235). Processes: bacterial entry into host cell, actin-based intracellular motility, inflammatory response, vasculitis.

---

### 7. Anatomical Structures Affected

- **Primary organ/tissue:** **Skin** at the bite site (UBERON:0002097, skin of body) — eschar; and the **vascular endothelium / blood vessel wall** (UBERON:0001981 blood vessel; UBERON:0001986 endothelium) as the fundamental target tissue.
- **Lymphatic system:** draining **regional lymph nodes** (UBERON:0000029) — lymphadenopathy; lymphatic vessels — occasional lymphangitis.
- **Secondary/complication organs (rare):** heart/myocardium (UBERON:0002349) — myocarditis; central nervous system — suspected involvement in rare severe cases.
- **Body systems:** integumentary, cardiovascular (vascular), and lymphatic/immune systems primarily.
- **Cell/tissue level:** vascular endothelial cells (CL:0000115); perivascular lymphohistiocytic infiltrate (T cells, histiocytes/macrophages); epidermal and superficial dermal necrosis.
- **Subcellular level:** *Rickettsia* replicates free in the **host-cell cytoplasm** (GO:0005737, cytoplasm) after phagosomal escape.
- **Localization / lateralization:** eschars localize to bite sites and can be **single or multiple and asymmetric** (wherever ticks attached); lymphadenopathy is regional to the draining basin.

---

### 8. Temporal Development

- **Onset:** Acute, typically **~5–10 days** (SFG-rickettsiosis incubation broadly 5–28 days; average ~7–14) after tick attachment. In the reported (traveler) population, onset is in adulthood; pediatric onset occurs.
- **Course/stages:** Monophasic acute illness → eschar formation, fever, lymphadenopathy → resolution. Not staged like chronic/neoplastic disease.
- **Progression rate:** Usually mild and self-limited; "The clinical course of disease was mild in all cases, and all but one of the patients recovered spontaneously before antibiotic treatment was initiated" ([PMID: 11939395](https://pubmed.ncbi.nlm.nih.gov/11939395/)).
- **Duration:** Self-limited over days to ~2 weeks; convalescence (asthenia) can be prolonged, especially in older patients.
- **Remission:** Both **spontaneous** and **treatment-induced** (doxycycline shortens illness). Relapse is not a characteristic feature of ATBF.
- **Critical period for intervention:** Early empiric doxycycline; for SFG rickettsioses generally, treatment delay is the key driver of severe outcomes ([PMID: 25697742](https://pubmed.ncbi.nlm.nih.gov/25697742/)).

---

### 9. Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency.

**Epidemiology.**
- **Endemic range:** rural sub-Saharan Africa (highest in southern and eastern Africa), West/Central Africa, and the eastern Caribbean/French West Indies (where *Amblyomma variegatum* was introduced with cattle).
- **Travelers:** ATBF is "the second most commonly documented etiology of fever, after malaria, in travelers who return ill from sub-Saharan Africa" ([PMID: 28544092](https://pubmed.ncbi.nlm.nih.gov/28544092/)). Among travelers to South Africa, "spotted fever group rickettsiosis was the most common individual diagnosis" (GeoSentinel, 13 years) ([PMID: 20519590](https://pubmed.ncbi.nlm.nih.gov/20519590/)).
- **Endemic-population burden:** poorly quantified because case reports are "exclusively among returning travellers from non-endemic areas" ([PMID: 38813598](https://pubmed.ncbi.nlm.nih.gov/38813598/)). Formal incidence/prevalence per 100,000 are not reliably established.
- **Demographics:** all ages; middle-aged adults dominate reported series; both sexes; clustered co-traveler cases characteristic.

**Vector/pathogen prevalence (transmission pressure).** Meta-analysis (32 studies, 12,301 ticks): *R. africae* prevalence "was higher in *Amblyomma* spp. (48%, 95% CI: 26-70%) compared to *Rhipicephalus* spp. (1%, 95% CI: 0-5%), *Hyalomma* spp. (1%, 95% CI: 0-3%)" ([PMID: 35537238](https://pubmed.ncbi.nlm.nih.gov/35537238/)). Field surveys: up to 69–81% of *A. variegatum* positive in Ghana ([PMID: 38295420](https://pubmed.ncbi.nlm.nih.gov/38295420/)); 46.9% of *A. hebraeum* on Eastern Cape cattle ([PMID: 36468449](https://pubmed.ncbi.nlm.nih.gov/36468449/)); 81% of *A. variegatum* on dogs in Chad ([PMID: 39427603](https://pubmed.ncbi.nlm.nih.gov/39427603/)).

---

### 10. Diagnostics

**Approach.** Diagnosis is often **clinical at presentation** because reliable early tests are lacking, with retrospective/laboratory confirmation. "The diagnosis of African tick bite fever is often based on clinical grounds due to a lack of reliable diagnostic tests at commencement of symptoms" ([PMID: 27488618](https://pubmed.ncbi.nlm.nih.gov/27488618/)).

| Test | Utility / notes |
|---|---|
| **Eschar-swab PCR** (gltA, ompA, ompB, 17-kDa) | Early, **non-invasive** confirmation; remains positive after doxycycline started. "direct molecular detection of *R. africae* was performed by PCR from a sample obtained non-invasively with a swab from the rickettsial eschar. A positive PCR result was achieved although the patient had already started antibiotic treatment with doxycycline" ([PMID: 27488618](https://pubmed.ncbi.nlm.nih.gov/27488618/)) |
| **Serology (IFA, IgM/IgG)** | Reference standard but **insensitive acutely** — antibodies appear ~7–15 days into illness and **cross-react across SFG** (e.g., against *R. conorii*); best for retrospective/convalescent confirmation ([PMID: 9916419](https://pubmed.ncbi.nlm.nih.gov/9916419/), [PMID: 7622271](https://pubmed.ncbi.nlm.nih.gov/7622271/)) |
| **Culture** | Possible from eschar biopsy; restricted to specialized/biosafety labs |
| **Eschar/skin biopsy histopathology + IHC** | Lymphohistiocytic/granulomatous vasculitis, dermal necrosis; immunostaining localizes rickettsiae ([PMID: 31955452](https://pubmed.ncbi.nlm.nih.gov/31955452/)) |
| **Routine labs** | Nonspecific; may show elevated ESR, mild transaminase elevation, occasional thrombocytopenia/leukopenia (by analogy to SFG rickettsioses; [PMID: 7622271](https://pubmed.ncbi.nlm.nih.gov/7622271/)) |
| **Imaging** | Not routinely diagnostic |

**Genetic/omics testing:** not applicable to the human host. Molecular diagnostics target the **pathogen** genome (PCR/sequencing of *gltA*, *ompA*, *ompB*, 17-kDa).

**Clinical criteria / differential.** Diagnosis rests on the epidemiologic setting (rural sub-Saharan Africa/Caribbean travel + tick exposure) plus eschar(s), fever, and lymphadenopathy. **Differential diagnosis:** malaria (must exclude), Mediterranean spotted fever (*R. conorii*), other SFG rickettsioses, scrub typhus, typhoid, arboviral fevers, Lyme borreliosis, and localized bacterial skin infection. Multiple eschars and clustered cases strongly favor ATBF over single-eschar *R. conorii* infection.

**Screening:** No population screening is applicable (no clinically relevant asymptomatic carrier state).

---

### 11. Outcome / Prognosis

- **Prognosis:** Excellent. With doxycycline, "the outcome was favorable in all cases, but complete recovery was slow" ([PMID: 18558881](https://pubmed.ncbi.nlm.nih.gov/18558881/)). Many patients recover spontaneously ([PMID: 11939395](https://pubmed.ncbi.nlm.nih.gov/11939395/)).
- **Mortality:** Deaths from ATBF are essentially **not reported** — a key contrast with the severe SFG rickettsiosis Rocky Mountain spotted fever (RMSF), where treatment delay drives fatality ([PMID: 25697742](https://pubmed.ncbi.nlm.nih.gov/25697742/)).
- **Morbidity/complications (uncommon, older patients):** lymphangitis, myocarditis, suspected CNS involvement, prolonged asthenia, and reactive/subacute events. The eschar disrupts the cutaneous barrier and can predispose to **secondary bacterial cellulitis**: "In African tick bite fever (ATBF), inoculation eschar - resulting from disruption of the cutaneous barrier - may be a risk factor for cellulitis" (2 PCR-confirmed cases, good recovery on doxycycline + beta-lactam) ([PMID: 18503259](https://pubmed.ncbi.nlm.nih.gov/18503259/)).
- **Recovery:** Full recovery is the norm; long-term disability is not characteristic. QoL instruments have not been formally applied.
- **Prognostic factors:** older age → more severe manifestations/slower convalescence; timeliness of doxycycline. No molecular prognostic biomarkers are established.

---

### 12. Treatment

**First-line pharmacotherapy — Doxycycline** (tetracycline-class; CHEBI:50845; NCIT: Doxycycline). Typical regimen **100 mg twice daily for ~7 days**; consistently curative with favorable outcomes ([PMID: 18558881](https://pubmed.ncbi.nlm.nih.gov/18558881/)). Mechanism: inhibition of bacterial 30S ribosomal protein synthesis in the obligate intracellular pathogen. Doxycycline is the treatment of choice for tick-borne rickettsial diseases in adults and children ([PMID: 16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/)).

**Important caveat — beta-lactams are ineffective:** empiric beta-lactam therapy does not treat rickettsiosis, so a high index of suspicion is essential ([PMID: 9916419](https://pubmed.ncbi.nlm.nih.gov/9916419/)).

**Alternatives:** Other tetracyclines (e.g., minocycline used in a reported case; [PMID: 9916419](https://pubmed.ncbi.nlm.nih.gov/9916419/)); macrolides may be considered in pregnancy/children where tetracyclines are contraindicated (extrapolated from SFG-rickettsiosis practice — evidence limited).

**Complication-directed therapy:** Secondary cellulitis of an eschar treated with doxycycline **plus** an anti-staphylococcal/streptococcal beta-lactam ([PMID: 18503259](https://pubmed.ncbi.nlm.nih.gov/18503259/)).

**Advanced/experimental therapeutics:** None specific to ATBF (no gene, cell, RNA, targeted, or immunotherapies; no ATBF-specific registered clinical trials). Pharmacogenomics not applicable.

**Supportive care:** antipyretics/analgesics; wound care of the eschar.

---

### 13. Prevention

**No vaccine or chemoprophylaxis exists.** Prevention depends on **personal protection measures (PPM)** against ticks. "The registered and recommended active ingredients for skin application are Deet, picaridin (icaridin), p-menthane-3,8-diol (PMD) and IR3535. Volatile pyrethrins are used as space repellents while pyrethroids, especially permethrin, are employed for impregnation" ([PMID: 21302476](https://pubmed.ncbi.nlm.nih.gov/21302476/)). PPM "are essential and often the only means available" when no vaccine/prophylaxis exists.

- **Primary prevention:** repellents (DEET, picaridin/icaridin, PMD, IR3535); permethrin-impregnated clothing; protective clothing; **prompt tick removal and body checks** after exposure; pre-travel advice for those visiting endemic rural areas.
- **Secondary prevention:** early clinical recognition and prompt doxycycline in returned travelers with fever + eschar.
- **Tertiary prevention:** timely treatment of complications (e.g., cellulitis) and appropriate management of severe manifestations in the elderly.
- **Public-health/vector control:** livestock tick control reduces *Amblyomma* burden; surveillance of tick-borne pathogens in endemic regions ([PMID: 38095712](https://pubmed.ncbi.nlm.nih.gov/38095712/), [PMID: 39285746](https://pubmed.ncbi.nlm.nih.gov/39285746/)).
- **Immunization/genetic counseling:** not applicable.

---

### 14. Other Species / Natural Disease

- **Causative organism taxonomy:** *Rickettsia africae* (NCBI Taxonomy; SFG *Rickettsia*).
- **Vectors/reservoirs (NCBI Taxonomy genus *Amblyomma*):** *A. hebraeum*, *A. variegatum* are both **vector and reservoir**; the tick maintains the organism (transstadial/transovarial), and humans are **incidental/dead-end hosts**. "*Rickettsia africae* is a bacterium of zoonotic importance" ([PMID: 34516408](https://pubmed.ncbi.nlm.nih.gov/34516408/)).
- **Amplifying hosts:** cattle, camels, dogs, and wild game across sub-Saharan Africa carry infected *Amblyomma*; e.g., "*Rickettsia africae* was detected in 46.92% (95% CI = 41%-53%, n = 260) of ticks" on Eastern Cape cattle ([PMID: 36468449](https://pubmed.ncbi.nlm.nih.gov/36468449/)); *R. africae* in *A. variegatum* on dogs in Chad (81%) ([PMID: 39427603](https://pubmed.ncbi.nlm.nih.gov/39427603/)) and on camel ticks in Kenya ([PMID: 38698904](https://pubmed.ncbi.nlm.nih.gov/38698904/)) and Egypt ([PMID: 22217182](https://pubmed.ncbi.nlm.nih.gov/22217182/)).
- **Geographic spread:** *Amblyomma variegatum* introduced to the eastern Caribbean with cattle, extending the endemic range ([PMID: 16887719](https://pubmed.ncbi.nlm.nih.gov/16887719/)).
- **Zoonotic potential:** High as an exposure risk, but human infection is a spillover; no human-to-human transmission.
- **Comparative pathology:** The closely related agent *R. rickettsii* causes severe, sometimes fatal RMSF in dogs and humans, providing a comparative model of SFG-rickettsial vasculitis and doxycycline responsiveness ([PMID: 25542001](https://pubmed.ncbi.nlm.nih.gov/25542001/)); *R. africae* is comparatively benign.

---

### 15. Model Organisms

There is **no established dedicated animal model of ATBF (*R. africae*) that recapitulates human disease**, and no genetically engineered (knockout/knock-in/humanized) host models exist — consistent with a mild, self-limited human illness of limited severe-disease modeling need.

**Available/analogous systems:**
- **In vitro (best-characterized mechanistic system):** human endothelial cell cultures (HUVEC, microvascular endothelial cells) infected with SFG *Rickettsia* recapitulate endothelial infection and the IL-1α/IL-6/IL-8 cytokine cascade ([PMID: 8675654](https://pubmed.ncbi.nlm.nih.gov/8675654/), [PMID: 40570043](https://pubmed.ncbi.nlm.nih.gov/40570043/)); bone-marrow-derived macrophages used to assess intracellular survival.
- **Mouse model of spotted fever:** used to test rickettsial mutants (e.g., pso variant HK2) and a live-attenuated-vaccine concept ([PMID: 40570043](https://pubmed.ncbi.nlm.nih.gov/40570043/)) — an SFG-*Rickettsia* model, not *R. africae*-specific.
- **Natural/experimental canine RMSF (*R. rickettsii*):** models tick-borne SFG-rickettsial clinical course, convalescence, and doxycycline response ([PMID: 25542001](https://pubmed.ncbi.nlm.nih.gov/25542001/)).
- **Tick model:** *R. africae* is maintained in *Amblyomma* without fitness cost — an intact natural "vector model" of low-virulence rickettsial persistence ([PMID: 19379498](https://pubmed.ncbi.nlm.nih.gov/19379498/)).

**Limitation:** these systems model SFG-rickettsial endothelial biology broadly; the specific mild phenotype and multiple-eschar clustering of ATBF (driven by *Amblyomma* hunting behavior) are not fully captured by rodent models.

---

## Mechanistic Model / Interpretation

```
 Amblyomma tick (cluster attack) ── inoculates R. africae into dermis
                                          │  (→ often MULTIPLE bite sites)
                                          ▼
                       Adhesion + invasion of VASCULAR ENDOTHELIUM
                       (pso/O-antigen modulates invasion + immune shielding)
                                          ▼
                       Intracellular replication in endothelial cytoplasm
                                          ▼
                       IL-1α–dependent activation → IL-6, IL-8, chemokines
                                          ▼
                       Perivascular CD3+ T cells + CD68+ histiocytes
                       → LYMPHOHISTIOCYTIC / GRANULOMATOUS VASCULITIS
                       → loss of vascular integrity, ↑ permeability
                          │                                   │
       (LOCAL branch)     ▼                    (SYSTEMIC branch)▼
   Epidermal/superficial-dermal necrosis        Fever, headache, myalgia,
   → ESCHAR (tache noire) + regional            regional lymphadenopathy,
     lymphadenopathy                            variable maculopapular/
        │                                       vesicular RASH
        ▼                                              │
   Barrier breach → occasional 2° cellulitis    Rare: myocarditis, CNS
                                                 (mostly elderly)
                                          ▼
             Relatively INTACT genome (low gene decay) →
             contained, self-limited course; doxycycline curative
```

**Upstream vs downstream.** Upstream = tick inoculation and endothelial invasion. Central = IL-1α–driven cytokine cascade and vasculitis. Downstream = eschar/necrosis, lymphadenopathy, systemic febrile illness, rash. The pathogen's **genomic completeness** is a "meta-upstream" determinant setting the ceiling on virulence.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [34516408](https://pubmed.ncbi.nlm.nih.gov/34516408/) | Etiology: *R. africae* transmitted by *A. hebraeum*/*A. variegatum*; zoonotic importance | Review |
| [35537238](https://pubmed.ncbi.nlm.nih.gov/35537238/) | Meta-analysis: *Amblyomma* dominant competent vector (48% vs 1%) | Meta-analysis (32 studies) |
| [19379498](https://pubmed.ncbi.nlm.nih.gov/19379498/) | Genome (1.28 Mb + plasmid); low virulence ↔ minimal gene loss; benign to tick | Genomics/computational |
| [19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/) | Endothelial tropism → "rickettsial vasculitis" | Review |
| [8675654](https://pubmed.ncbi.nlm.nih.gov/8675654/) | IL-1α–dependent IL-6/IL-8 from infected endothelium | In vitro |
| [40570043](https://pubmed.ncbi.nlm.nih.gov/40570043/) | pso/O-antigen modulates invasion + immune evasion; attenuated-vaccine concept | In vitro + mouse |
| [31955452](https://pubmed.ncbi.nlm.nih.gov/31955452/) | Eschar histopathology: lymphohistiocytic/granulomatous vasculitis + necrosis | Human biopsy series |
| [30537329](https://pubmed.ncbi.nlm.nih.gov/30537329/) | Hallmark cutaneous presentation (eschar + rash) | Review |
| [18558881](https://pubmed.ncbi.nlm.nih.gov/18558881/) | Phenotype frequencies; doxycycline favorable but slow recovery (elderly) | Case series (n=8) |
| [20233665](https://pubmed.ncbi.nlm.nih.gov/20233665/) | Eschar 53–100%, multiple 21–54%, rash 15–46%; multiple eschars pathognomonic | Case series/review |
| [38813598](https://pubmed.ncbi.nlm.nih.gov/38813598/) | Knowledge base skewed to travelers; endemic burden unknown | Systematic review |
| [20519590](https://pubmed.ncbi.nlm.nih.gov/20519590/) | SFG rickettsiosis = most common diagnosis in travelers to South Africa | GeoSentinel |
| [28544092](https://pubmed.ncbi.nlm.nih.gov/28544092/) | 2nd cause of fever after malaria; pediatric cluster | Case series/review |
| [11939395](https://pubmed.ncbi.nlm.nih.gov/11939395/) | Mild, often spontaneously resolving course | Outbreak (n=6) |
| [27488618](https://pubmed.ncbi.nlm.nih.gov/27488618/) | Eschar-swab PCR positive post-doxycycline; clinical diagnosis | Case report |
| [21302476](https://pubmed.ncbi.nlm.nih.gov/21302476/) | Repellents/permethrin as PPM (prevention) | Review |
| [18503259](https://pubmed.ncbi.nlm.nih.gov/18503259/) | Eschar → secondary cellulitis complication | Case series |
| [36468449](https://pubmed.ncbi.nlm.nih.gov/36468449/) | *R. africae* in 46.9% *A. hebraeum* on cattle (reservoir ecology) | Field survey |
| [16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/) | Doxycycline = drug of choice for tick-borne rickettsioses | Guideline |
| [25697742](https://pubmed.ncbi.nlm.nih.gov/25697742/) | Treatment delay drives severe SFG outcomes (contrast: RMSF) | Case-control |

**Consistency.** Findings are internally consistent — endothelial tropism, cytokine biology, and vasculitic histopathology converge on the eschar/febrile syndrome, while genomics explains the mild phenotype and epidemiology explains the traveler-centric evidence base. **Caveat:** several mechanistic details (endothelial cytokine assays, pso operon, eschar histopathology) derive from related SFG species (*R. conorii*, rickettsialpox), not *R. africae* directly, and are extrapolated on the basis of shared SFG biology.

---

## Limitations and Knowledge Gaps

1. **Traveler-biased evidence base.** Nearly all clinical data come from returning travelers; incidence/prevalence and disease spectrum among **endemic residents** are essentially unquantified ([PMID: 38813598](https://pubmed.ncbi.nlm.nih.gov/38813598/)).
2. **Mechanistic extrapolation.** Direct endothelial-infection cytokine data and eschar histopathology come from *R. conorii*/rickettsialpox, not *R. africae* specifically.
3. **No *R. africae*-specific animal model** and no human host-genetic studies.
4. **Diagnostic gap.** No sensitive early-illness test; serology is delayed and cross-reactive, and PCR/eschar sampling is not universally available.
5. **Quantitative QoL, long-term convalescence, and complication rates** are imprecise (small series, older-patient skew).
6. **Formal epidemiologic metrics** (cases/100,000) are lacking.

---

## Proposed Follow-up Experiments / Actions

1. **Endemic-population cohort studies** with active surveillance and eschar-swab PCR to establish true incidence, spectrum, and pediatric burden in sub-Saharan Africa.
2. ***R. africae*-specific endothelial and in-vivo studies** (human microvascular endothelial cells; immunocompetent mouse/guinea-pig models) to confirm the IL-1α/IL-6/IL-8 cascade and pso-mediated immune evasion for this species specifically.
3. **Point-of-care molecular diagnostics** (rapid *gltA*/*ompA* PCR or LAMP on eschar swabs) validated for field/travel-clinic use.
4. **Prospective evaluation of doxycycline regimens** (duration, timing) and outcomes in older adults, plus systematic capture of complications (myocarditis, CNS, cellulitis).
5. **Vector-control / one-health interventions** targeting *Amblyomma* on livestock to reduce transmission pressure, with pre/post pathogen-prevalence monitoring.
6. **Traveler prevention trials** quantifying the protective efficacy of specific repellents/permethrin clothing against *Amblyomma* bites and ATBF incidence.

---

*Report compiled from 12 confirmed findings and 39 reviewed papers across 5 investigation iterations. All mechanistic and clinical claims are cited to primary literature (PMID). Human host genetics, causal genes, and inherited risk are not applicable — ATBF is an infectious, vector-borne rickettsiosis.*


## Artifacts

- [OpenScientist final report](African_Tick-Bite_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](African_Tick-Bite_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 32 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19379498` *(abstract only)*: "we speculate that in *Rickettsia* species virulence is mostly associated with gene loss"
  - closest text in source: "We also speculate that in Rickettsia species virulence is mostly associated with gene loss.The genome sequence was deposited in GenBank under accession number [GenBank: NZ_AAUY01000001]."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012133` (1 mention) - the report calls it "Myocarditis"; HP calls it **Erythroid hypoplasia**
- `UBERON:0000029` (1 mention) - the report calls it "regional lymph nodes", "Lymphatic system:** draining **regional lymph nodes"; UBERON calls it **lymph node**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000115` (2 mentions) - the report calls it "Cell/tissue level:** vascular endothelial cells"; CL calls it **endothelial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000029` - called "regional lymph nodes", "Lymphatic system:** draining **regional lymph nodes"