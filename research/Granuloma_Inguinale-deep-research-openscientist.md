---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T22:39:34.777035'
end_time: '2026-09-24T22:51:45.172633'
duration_seconds: 730.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Granuloma Inguinale
  mondo_id: MONDO:0005777
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
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 22
  on_topic: 19
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 21
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 2
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0100820
    reported_labels:
    - "Genital/vulval swelling \u2192 elephantiasis"
    ontology_label: Glomerulopathy
  - term_id: GO:0006954
    reported_labels:
    - Cellular processes:** chronic inflammation
    ontology_label: inflammatory response
  - term_id: GO:0045335
    reported_labels:
    - cytoplasmic vacuoles/phagosomes
    - Subcellular:** bacteria within macrophage **cytoplasmic vacuoles/phagosomes
    ontology_label: phagocytic vesicle
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Granuloma_Inguinale-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Granuloma_Inguinale-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Granuloma Inguinale
- **MONDO ID:** MONDO:0005777 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Granuloma Inguinale** covering all of the
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

# Granuloma Inguinale (Donovanosis): Comprehensive Disease Profile

**Disease:** Granuloma Inguinale (Donovanosis) · **MONDO:** MONDO:0005777 · **Category:** Infectious Disease
**Report date:** 2026-09-25 · **Evidence base:** Human clinical studies, case reports/series, phylogenetic and ultrastructural studies, and management guidelines (primarily aggregated disease-level literature, not individual EHR).

---

## Summary (Answer to the Research Question)

Granuloma inguinale (donovanosis) is a **chronic, slowly progressive, mildly contagious sexually transmitted bacterial infection** that produces characteristic **beefy-red, friable, readily bleeding genital/inguinal ulcers**. It is caused by the intracellular Gram-negative bacillus ***Klebsiella granulomatis*** (formerly *Calymmatobacterium granulomatis*). The organism parasitizes tissue **macrophages/histiocytes**, driving a **granulomatous, plasma-cell–rich inflammatory response** with overlying pseudoepitheliomatous hyperplasia; the intracytoplasmic bacteria are visible as pathognomonic **Donovan bodies**. Diagnosis rests on cytology/histology (Donovan bodies) and, increasingly, PCR, because the organism is difficult to culture. **Azithromycin is first-line therapy**, with cure the norm. It is a **rare, geographically restricted disease** (endemic foci in Papua New Guinea, southern Africa, India, Brazil, and formerly among Aboriginal Australians) that is **declining toward eradication**, and it is an established **cofactor for HIV-1 acquisition/transmission**. As a purely infectious disease it has **no human causal gene, no Mendelian inheritance, and no established animal model**; several template sections (host genetics, model organisms, germline variants) are therefore Not Applicable.

---

## 1. Disease Information

- **Overview:** A chronic ulcerative bacterial STI of the genital and inguinal region. Genital papules appear after a ~50-day incubation and evolve into progressively enlarging, painless, friable ulcers with a beefy-red granulation base that bleed on contact. Course is indolent and progressive without treatment; healing occurs with antibiotics.
- **Key identifiers:**
  - **MONDO:** MONDO:0005777
  - **ICD-10:** A58 (Granuloma inguinale); **ICD-11:** 1A76 (Granuloma inguinale)
  - **MeSH:** D006099 "Granuloma Inguinale"
  - **SNOMED CT:** 5006005 (Granuloma inguinale)
  - **OMIM / Orphanet:** Not applicable as a Mendelian disorder (infectious disease; no OMIM phenotype entry). Orphanet does not list it as a rare genetic disease.
  - **Causative organism NCBI Taxonomy:** *Klebsiella granulomatis* (txid280) / *Calymmatobacterium granulomatis*.
- **Synonyms / alternative names:** Donovanosis; granuloma venereum; granuloma inguinale tropicum; "serpiginous ulcer" (historical); ulcerating granuloma of the pudenda. (Note: distinct from *granuloma inguinale tropicum*/LGV historically confused terminology.)
- **Information source:** Aggregated disease-level literature (guidelines, reviews, clinical case series), not individual-patient EHR.

*Evidence:* PMID 41016613 — "Donovanosis usually causes genital ulcers with a distinct clinical appearance… The causative organism is a gram-negative bacillus, Calymmatobacterium granulomatis." PMID 42486240 (historical review).

---

## 2. Etiology

- **Causal factor — infectious:** *Klebsiella granulomatis* (formerly *Calymmatobacterium granulomatis*), an encapsulated, intracellular **Gram-negative bacillus** of family Enterobacteriaceae. Transmission is predominantly **sexual** (genital, and via ano-receptive/oro-genital contact); low infectivity, with autoinoculation contributing to spread. There is **no genetic/heritable cause**.
- **Risk factors (environmental/behavioral):** residence in or travel to endemic areas; multiple sexual partners; low socioeconomic status/poor access to care; male sex and young adult age (peak in sexually active adults, ~15–40 y); poor genital hygiene; possibly fecal contamination/anal exposure. **No genetic susceptibility loci** have been identified.
- **Protective factors:** condom use, partner notification/treatment, sexual abstinence during treatment, early antibiotic therapy, and general STI-control/health-education programs. No genetic protective variants (Not Applicable).
- **Gene–environment interactions:** Not applicable to host genetics. The clinically relevant interaction is **comorbidity with HIV**, where immunodeficiency prolongs/worsens disease and requires extended therapy.

*Evidence:* PMID 10555350; PMID 10482295; PMID 22239475 — reclassification and phylogeny; PMID 41016613 — Gram-negative bacillus, nomenclature debate.

---

## 3. Phenotypes

**Primary phenotype — chronic genital ulcer (HP:0000163 region; HP:0200035 "Genital ulcers"):**
- *Type:* clinical sign / physical manifestation (mucocutaneous ulceration).
- *Characteristics:* adult-onset; typically **painless or minimally painful**; **beefy-red, granulomatous, friable base that bleeds readily on contact**; slowly **progressive/enlarging**; chronic (weeks–months). In a Durban series, ulcers persisted >28 days in ~55% of men and ~46% of women.
- *Four recognized morphologic subtypes:* **ulcerogranulomatous** (most common), **hypertrophic/verrucous**, **necrotic** (deep, foul-smelling, destructive), and **sclerotic/cicatricial** (fibrotic).

**Associated signs/complications:**
- **Pseudobuboes** — subcutaneous inguinal granulomas mimicking lymphadenopathy (HP:0002716 lymphadenopathy — note: true lymphadenitis is usually *absent*).
- **Genital/vulval swelling → elephantiasis** (HP:0100820) from lymphatic obstruction (chronic cases).
- **Tissue destruction/mutilation, scarring, stricture**; genital lymphedema.
- **Secondary squamous cell carcinoma** (HP:0002860) in long-standing lesions (rare).

**Frequency:** Ulcerogranulomatous form predominates (>90% of lesions in series). **Quality-of-life impact:** substantial physical disability, disfigurement, sexual/urinary dysfunction, and psychological distress/stigma, particularly with elephantiasis or mutilating disease; formal EQ-5D/SF-36 data are not available for this rare disease. Stigma is amplified by sensationalist media: reports of a "flesh-eating infection donovanosis" are false and "only leading to hyperbole and increased stigma among those infected" (PMID 41016613).

**Pregnancy & special populations:** In a Durban series of 123 women, 42% were pregnant; in ~85% donovanosis had no effect on pregnancy outcome and there was **no evidence of congenital disease in neonates** (PMID 8735293), though extensive vulval lesions can complicate delivery. **Erythromycin** is the preferred agent in pregnancy. Disease behaves similarly in HIV-positive and HIV-negative women, though healing may be slower with advanced immunodeficiency.

*Evidence:* PMID 26882914 / 21097731 — incubation and lesion types; PMID 8509089 — lesion-type frequencies and chronicity; PMID 16510000 — elephantiasis.

---

## 4. Genetic / Molecular Information

**Not applicable (host).** Donovanosis is an infectious disease with **no causal human gene, no pathogenic germline/somatic variant, no modifier genes, no disease-defining epigenetic changes, and no chromosomal abnormalities**. There is no inheritance, penetrance, expressivity, or carrier frequency.

**Pathogen molecular biology (limited):** *K. granulomatis* shows ~95% 16S rRNA identity to *Klebsiella* and ~94% to *Enterobacter*; sequencing of 16S rRNA + *phoE* (2089 bp) supported reclassification as *Klebsiella granulomatis* comb. nov. Because the organism is **fastidious and hard to culture**, its genome and virulence factors remain **poorly characterized**; a defined virulence repertoire is not established.

*Evidence:* PMID 10555350; PMID 10482295; PMID 22239475 — "Because of the difficulty in growing this bacterium… its characteristics have not been sufficiently defined."

---

## 5. Environmental Information

- **Environmental/occupational toxins:** none implicated.
- **Lifestyle factors:** high-risk sexual behavior; multiple partners; migration between urban/rural endemic areas (identified as a driver of transmission and HIV co-risk in South African studies). Minimal condom use in affected populations.
- **Infectious agent:** ***Klebsiella (Calymmatobacterium) granulomatis*** — Gram-negative bacillus; **NCBI Taxonomy** *Klebsiella granulomatis*; gamma-Proteobacteria; Enterobacteriaceae. Humans are the only known host/reservoir; no environmental or animal reservoir is established.

*Evidence:* PMID 1398660 — sexual-behavior/migration patterns; PMID 10482295 — taxonomy.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating infection → clinical manifestation)

1. **Sexual/auto-inoculation exposure** deposits *K. granulomatis* onto genital/inguinal epithelium (often at microabrasions) → **leads to** local colonization. *(demonstrated: sexual transmission; exact portal inferred)*
2. Bacteria are **phagocytosed by tissue macrophages/histiocytes** and **survive/replicate within cytoplasmic vacuoles (phagosomes)** → **results in** an intracellular reservoir (Donovan bodies). *(demonstrated by ultrastructure)*
3. Persisting intracellular bacteria **drive chronic granulomatous inflammation** — recruitment of **plasma cells, neutrophils, and activated macrophages** with few lymphocytes → **leads to** granulation-tissue formation. *(demonstrated histologically)*
4. Ongoing inflammation and proteolysis **erode the epithelium** and induce **pseudoepitheliomatous hyperplasia** at ulcer margins → **results in** the characteristic beefy-red, friable, bleeding ulcer that enlarges peripherally. *(demonstrated)*
5. **Branch A (chronic fibrosis):** persistent inflammation **traps and constricts lymphatics** → **leads to** lymphatic obstruction → **genital elephantiasis / lymphedema** and cicatricial/sclerotic scarring, strictures. *(demonstrated mechanism, PMID 16510000)*
6. **Branch B (neoplasia):** decades-long chronic ulceration and epithelial hyperplasia **predispose to malignant transformation** → **squamous cell carcinoma**. *(inferred from case reports)*
7. **Branch C (HIV facilitation):** the friable, readily bleeding ulcer **disrupts the mucosal barrier** → **facilitates HIV-1 entry/transmission** (portal of entry + blood contact). *(epidemiologically demonstrated)*
8. **Branch D (spread):** direct extension/autoinoculation and (rarely) hematogenous/lymphatic dissemination → **extragenital, pelvic, or disseminated lesions**. *(demonstrated in case reports)*

### Detail by category
- **Cellular processes:** chronic inflammation (GO:0006954), phagocytosis (GO:0006909), granuloma formation; macrophage activation (increased lysosomes, rough ER, filopodia on ultrastructure).
- **Immune involvement:** predominantly **innate/macrophage-centered** with prominent **plasma-cell (humoral) infiltrate**; sparse lymphocytes; the organism resists intracellular killing, enabling persistence. Immunodeficiency (HIV) worsens/prolongs disease.
- **Tissue damage mechanisms:** inflammatory tissue destruction, ulceration, fibrosis/sclerosis, lymphatic obstruction; **not** toxin- or ischemia-driven.
- **Molecular pathways / metabolic / epigenetic / omics:** **Not characterized** — no transcriptomic, proteomic, metabolomic, or defined signaling-pathway data exist for donovanosis (knowledge gap due to culture difficulty).
- **Cell types (CL):** macrophage (CL:0000235), plasma cell (CL:0000786), neutrophil (CL:0000775). **GO cellular component:** phagocytic vesicle/phagosome (GO:0045335).

*Evidence:* PMID 9856642 (intramacrophage localization); PMID 2777345 (ultrastructure of inflammatory response); PMID 18317211 (plasma-cell/histiocyte histology, Donovan bodies); PMID 16510000 (lymphatic constriction → elephantiasis); PMID 2063236 (HIV facilitation).

---

## 7. Anatomical Structures Affected

- **Organ/system level:** **reproductive/genitourinary system** and **integumentary system (skin)** are primary. Secondary: inguinal soft tissue, lymphatics (obstruction), and rarely pelvis/bone (dissemination).
- **Primary sites (~90%):** external genitalia and inguinal/perineal region — penis, prepuce, coronal sulcus, glans; vulva, labia, fourchette; also **uterine cervix** (UBERON:0000002) and **vagina** (UBERON:0000996). **Perianal/anal** lesions with ano-receptive intercourse.
- **Extragenital (rare):** lip/oral cavity, and skin sites such as the foot; disseminated pelvic/visceral disease historically reported.
- **Tissue/cell level:** epithelial tissue (pseudoepitheliomatous hyperplasia) and dermal connective/granulation tissue; key cells = macrophages/histiocytes (CL:0000235), plasma cells (CL:0000786), neutrophils (CL:0000775).
- **Subcellular:** bacteria within macrophage **cytoplasmic vacuoles/phagosomes** (GO:0045335).
- **Localization/lateralization:** lesions localize to sites of sexual contact; inguinal involvement may be **unilateral or bilateral**; "kissing lesions" from autoinoculation on apposed skin.
- **UBERON suggestions:** external genitalia; UBERON:0000996 (vagina); UBERON:0000002 (cervix); UBERON:0002097 (skin of body); inguinal region.

*Evidence:* PMID 8735293 (rectal/pelvic + genital); PMID 9924476 (extragenital foot); PMID 18317211 (cervix).

---

## 8. Temporal Development

- **Onset:** **adult-onset**, in sexually active individuals; **insidious/chronic** onset after an **incubation period of ~50 days** (reported range ~1–12 weeks, up to months). Not congenital; neonatal/perinatal transmission is rare.
- **Progression:** untreated disease is **slowly progressive** with peripheral enlargement and local tissue destruction over months–years; stages run from **papule → early ulcer → extensive ulcerogranulomatous/hypertrophic disease → sclerotic/cicatricial end-stage** with scarring, lymphedema/elephantiasis, and rare malignant transformation.
- **Course pattern:** chronic progressive; **not** self-limiting. **Relapse** can occur 6–18 months after apparently adequate therapy, warranting follow-up.
- **Remission:** **treatment-induced** (antibiotics) — healing from ulcer margins; spontaneous remission is uncommon.
- **Critical intervention window:** early antibiotic treatment prevents tissue destruction, scarring, elephantiasis, and reduces HIV-cofactor risk.

*Evidence:* PMID 26882914 (incubation ~50 days; treat until healed); PMID 8509089 (chronicity).

---

## 9. Inheritance and Population

- **Epidemiology:** **rare and geographically restricted**; endemic "hot spots" — **Papua New Guinea, South Africa (KwaZulu-Natal/Durban epidemic 1988–97), India, Brazil, and formerly Aboriginal communities in Australia**. Marked **global decline**; described in 2026 as "well on the way to being eradicated." Precise global incidence/prevalence figures are not maintained in standard registries (SEER/GBD do not track it separately); it is now seen mostly as sporadic imported cases in non-endemic countries.
- **Infectivity:** **low/mildly infectious** — only 1/21 regular partners were infected in one Durban series, supporting feasibility of elimination programs.
- **Inheritance/penetrance/carrier frequency/founder effects/consanguinity:** **Not Applicable** (infectious, non-genetic).
- **Demographics:** affects sexually active adults, roughly **15–40 years** (series mean age ~22 in women). **Sex ratio** varies by setting; classic literature reports a **male predominance** (e.g., 130 men vs 41 women in one Durban series), though other series (antenatal/gynecology clinics) are female-predominant, reflecting ascertainment. Higher burden in **lower-income, rural, and marginalized populations** in endemic regions.
- **Geographic variant distribution:** Not characterized (limited pathogen genomics).

*Evidence:* PMID 41016613 ("significant global decline… well on the way to being eradicated"); PMID 26882914 (endemic countries); PMID 7750949 (unique geography); PMID 8509089 (sex distribution, low partner infectivity).

---

## 10. Diagnostics

- **Cornerstone — cytology/histopathology:** microscopic identification of **Donovan bodies** (intracytoplasmic, bipolar "safety-pin" bacteria within macrophages/histiocytes) on **crush/tissue smears** stained with **Giemsa/Wright/RapiDiff** or on biopsy. Histology: granulation tissue with dense plasma-cell infiltrate, neutrophil microabscesses, enlarged vacuolated histiocytes containing Donovan bodies, and pseudoepitheliomatous hyperplasia.
- **Molecular:** **PCR** (including colorimetric-detection assays) developed for genital-ulcer specimens; increases sensitivity/specificity where available. **LOINC/SNOMED** codes exist for genital-ulcer pathogen testing.
- **Culture:** difficult/not routine (fastidious; grown historically in human peripheral-blood monocyte co-culture and Hep-2 cells).
- **Biomarkers/imaging/electrophysiology/omics:** no specific serum biomarker; imaging only for complications (deep/pelvic/bone extension); no omics-based diagnostics.
- **Genetic testing:** **Not Applicable** (no host genetic component; WGS/WES/panels/karyotype/CMA/FISH not indicated).
- **Clinical criteria & differential diagnosis:** diagnosis is clinical + cytologic/PCR confirmation. **Differential:** primary syphilis (chancre), chancroid (*H. ducreyi*), lymphogranuloma venereum (*C. trachomatis* L1–L3), genital herpes, secondary bacterial/fungal infection; and non-infectious mimics — **squamous cell carcinoma**, Behçet disease, aphthosis, psoriasis, fixed drug eruption, sexual trauma. Distinguishing features of donovanosis: chronic, painless, beefy-red, friable, bleeding ulcer usually **without true regional lymphadenitis**. *No pathogen is identified in up to 25% of genital-ulcer patients.*
- **Screening:** no asymptomatic/newborn/carrier screening; case-finding via STI services and **partner notification**.

*Evidence:* PMID 26882914 (Donovan bodies + PCR); PMID 22335265 (genital-ulcer differential; up to 25% undiagnosed); PMID 39566736 (non-infectious mimics); PMID 18317211 (histology).

---

## 11. Outcome / Prognosis

- **Prognosis with treatment:** **excellent** — highly curable with antibiotics; ulcers re-epithelialize over weeks. Early treatment prevents disfigurement and complications.
- **Mortality:** **very low**; donovanosis is rarely directly fatal. No standardized survival statistics (non-lethal, rare disease). Disease-specific mortality is negligible except via complications (secondary infection, or SCC).
- **Morbidity/disability:** without treatment — extensive genital ulceration, tissue destruction/mutilation, scarring, urethral/vaginal/anal strictures, **genital elephantiasis/lymphedema**, and psychosexual morbidity. Long-standing lesions carry a small risk of **squamous cell carcinoma**.
- **Recovery:** high recovery potential with therapy; established fibrosis/elephantiasis and tissue loss may be **irreversible** and require surgery.
- **Prognostic factors:** duration/extent of lesions at presentation, **HIV coinfection** (prolonged healing, treatment failure risk), and treatment adherence. No molecular prognostic biomarkers.

*Evidence:* PMID 26882914 (treat until healed); PMID 7750949 (treatment failure in advanced HIV); PMID 19061590 / 24554002 / 26396449 (SCC complication); PMID 16510000 (elephantiasis).

---

## 12. Treatment

- **First-line pharmacotherapy:** **Azithromycin** (macrolide; inhibits 50S ribosome) **1 g weekly** (or 500 mg daily) **continued until all lesions have fully healed** (minimum ~3 weeks). NCIT:C734; CHEBI:2955; ATC J01FA10.
- **Alternative regimens (≥3 weeks / until healed):**
  - **Doxycycline** 100 mg twice daily (tetracycline) — genital-ulcer guidance specifies **21 days**. NCIT:C744; CHEBI:50845.
  - **Trimethoprim–sulfamethoxazole** (co-trimoxazole) 160/800 mg twice daily. NCIT:C265.
  - **Erythromycin** 500 mg four times daily (preferred in pregnancy). NCIT:C61780.
  - **Ceftriaxone** and **ciprofloxacin** reported as further alternatives.
- **Adjuncts:** add a parenteral aminoglycoside (e.g., **gentamicin**) if lesions do not respond, especially in HIV-positive patients; **prolonged therapy** in advanced HIV.
- **Surgery/interventional:** reserved for complications — excision of fibrotic/mutilating tissue, correction of strictures/elephantiasis, or resection of secondary SCC.
- **Supportive care:** wound care, analgesia, treatment of secondary infection; partner evaluation/treatment.
- **Advanced/experimental therapeutics (gene/cell/RNA/targeted/immuno-therapy) and pharmacogenomics:** **Not Applicable** — no gene-guided therapy; standard antibiotics suffice. No active registered clinical trials specific to donovanosis.
- **Treatment outcome:** high response/cure rates; monitor for **relapse at 6–18 months**. Adverse events are drug-class–typical (GI upset with macrolides/tetracyclines; photosensitivity with doxycycline; sulfa hypersensitivity).

*Evidence:* PMID 26882914 / 21097731 (azithromycin first-line); PMID 22335265 (doxycycline 21 days).

---

## 13. Prevention

- **Primary prevention:** safer-sex practices (**condoms**), reduction in number of partners, health education, and **prompt treatment of index cases and sexual partners** to interrupt transmission. **No vaccine exists** (immunization Not Applicable).
- **Secondary prevention:** early detection/treatment in STI clinics; **syndromic management** of genital ulcer disease in endemic settings (adapted locally); **partner notification/treatment**; abstinence until lesions heal.
- **Tertiary prevention:** complete antibiotic courses to prevent tissue destruction, strictures, elephantiasis, and malignant transformation; surveillance for relapse and SCC; management of HIV coinfection.
- **Public-health interventions:** **community-based elimination programs** are feasible given low infectivity and restricted geography — the **Australian Aboriginal donovanosis elimination program** is a documented success and proposed model; donovanosis eradication is framed as an opportunity to also curb HIV-1 spread.
- **Genetic counseling/carrier screening:** **Not Applicable**.

*Evidence:* PMID 12473810 (successful Australian elimination program; syndromic management); PMID 7750949 (global eradication opportunity linked to HIV control).

---

## 14. Other Species / Natural Disease

- **Host range:** **Humans are the only known natural host**; no established zoonotic reservoir or naturally occurring animal disease is documented for *K. granulomatis*.
- **Taxonomy of pathogen:** *Klebsiella granulomatis* (NCBI Taxonomy). Closely related human pathogens in the genus: *K. pneumoniae*, *K. rhinoscleromatis* (causes rhinoscleroma), *K. oxytoca*.
- **Comparative biology:** mechanistic parallels with **rhinoscleroma** (*K. rhinoscleromatis*) — another chronic granulomatous *Klebsiella* infection with intramacrophage bacteria (Mikulicz cells analogous to Donovan-body–laden histiocytes).
- **Breeds/orthologous genes/zoonosis/cross-species susceptibility:** **Not Applicable / Not documented.**

*Evidence:* PMID 10555350 (relatedness to *K. pneumoniae*, *K. rhinoscleromatis*).

---

## 15. Model Organisms

- **No established animal or genetic disease model exists.** The organism's **fastidious growth requirements** (only re-cultured after >30 years in **human peripheral-blood monocyte co-culture and Hep-2 cell** systems) have precluded standard mouse/rat/zebrafish/invertebrate models, and there are no knockout/transgenic/humanized models (host genetics is irrelevant).
- **In vitro systems used:** human monocyte co-cultures and Hep-2 cells for isolation and ultrastructural study.
- **Limitations / research gap:** absence of tractable models and a complete genome is the principal barrier to studying virulence factors, immune evasion, and pathway-level mechanisms.

*Evidence:* PMID 9856642 (monocyte co-culture / tissue ultrastructure); PMID 22239475 (culture difficulty; "more studies needed to understand bacterial genetics").

---

## Supported vs Refuted Hypotheses

**Supported (evidence-backed):**
1. Donovanosis is caused by intracellular Gram-negative *Klebsiella (Calymmatobacterium) granulomatis* (16S/phoE phylogeny).
2. Pathology is macrophage-based granulomatous inflammation with Donovan bodies (ultrastructure/histology).
3. Azithromycin is first-line, curative therapy (guidelines).
4. Disease is rare, geographically restricted, and declining toward eradication (reviews).
5. Donovanosis is a cofactor for HIV-1 acquisition/transmission (P=0.02 in men; risk rises with lesion duration).
6. Chronic disease causes elephantiasis (lymphatic obstruction) and rarely SCC (mechanism + case reports).

**Refuted / Not Applicable:**
- No host causal gene, inheritance, penetrance, or carrier frequency (infectious disease).
- No established animal model or knockout/transgenic system.
- No omics/pathway-level molecular profiling; no vaccine; no gene/cell/RNA therapy.

## Mechanistic Model (Synthesis)

```
 Sexual / auto-inoculation of K. granulomatis (~50-day incubation)
                 │
                 ▼
 Phagocytosis by dermal MACROPHAGES (CL:0000235)
                 │
                 ▼
 Intracellular survival in cytoplasmic vacuoles (GO:0045335)
        → DONOVAN BODIES  (pathognomonic)
                 │
                 ▼
 Chronic GRANULOMATOUS inflammation
 (plasma cells CL:0000786 + neutrophils CL:0000775)
 + pseudoepitheliomatous hyperplasia
                 │
                 ▼
 Beefy-red, FRIABLE, bleeding ULCER  (HP:0200035)
        │              │                 │
        ▼              ▼                 ▼
  Lymphatic       Long-standing      Bleeding portal
  constriction    lesion →           → HIV-1 acquisition
  → ELEPHANTIASIS  SCC (rare)         & transmission (cofactor)
  (PMID 16510000)  (PMID 19061590)    (PMID 2063236)
```

The unifying theme is that donovanosis is a **macrophage-parasitizing intracellular infection** whose clinical severity flows from the *chronicity* of the granulomatous response rather than acute toxicity. This explains the slow tempo, the friable vascular ulcers, the late fibrotic/lymphatic and neoplastic complications, the HIV-cofactor role, and why a single mechanistic intervention — sustained intracellular-active antibiotic therapy (azithromycin) — is curative and why elimination programs succeed (breaking the sole human transmission chain).

---

## Evidence Base — Key Papers and How They Support the Findings

| PMID | Paper (abbrev.) | Type | Supports |
|---|---|---|---|
| [10555350](https://pubmed.ncbi.nlm.nih.gov/10555350/) | Reclassification as *K. granulomatis* comb. nov. | Phylogenetic | Etiology/taxonomy; relatedness to *K. pneumoniae*/*K. rhinoscleromatis* |
| [10482295](https://pubmed.ncbi.nlm.nih.gov/10482295/) | 16S rRNA phylogeny of *C. granulomatis* | Phylogenetic | ~95% *Klebsiella*, ~94% *Enterobacter*; distinct gamma-proteobacterium |
| [22239475](https://pubmed.ncbi.nlm.nih.gov/22239475/) | Evolution of STI bacteria | Computational/review | Culture difficulty; sparse pathogen genetics (knowledge gap) |
| [41016613](https://pubmed.ncbi.nlm.nih.gov/41016613/) | Donovanosis review (2026) | Review | Gram-negative bacillus; near-eradication; stigma/misinformation |
| [26882914](https://pubmed.ncbi.nlm.nih.gov/26882914/) | 2016 European guideline | Guideline | ~50-day incubation; 4 lesion types; Donovan bodies/PCR; azithromycin |
| [21097731](https://pubmed.ncbi.nlm.nih.gov/21097731/) | 2010 European guideline | Guideline | Diagnosis and first-line azithromycin |
| [8509089](https://pubmed.ncbi.nlm.nih.gov/8509089/) | Durban clinico-epidemiological study | Clinical series | Lesion-type frequencies; chronicity; sex distribution |
| [2063236](https://pubmed.ncbi.nlm.nih.gov/2063236/) | HIV-1 in Durban STD clinic | Cross-sectional (human) | Donovanosis–HIV-1 association (P=0.02, men); risk ↑ with lesion duration |
| [7750949](https://pubmed.ncbi.nlm.nih.gov/7750949/) | Global eradication of donovanosis | Review | Unique geography; HIV risk factor; eradication opportunity |
| [9856642](https://pubmed.ncbi.nlm.nih.gov/9856642/) | Ultrastructure: culture vs biopsy | In vitro/ultrastructural | Intramacrophage localization; absent surface structures |
| [2777345](https://pubmed.ncbi.nlm.nih.gov/2777345/) | Ultrastructural study of donovanosis | Ultrastructural | Macrophage activation; inflammatory cell repertoire |
| [18317211](https://pubmed.ncbi.nlm.nih.gov/18317211/) | Malacoplakia & GI of cervix in AIDS | Case report | Histology (Donovan bodies); cervical involvement |
| [16510000](https://pubmed.ncbi.nlm.nih.gov/16510000/) | Genital elephantiasis & STIs | Review | Lymphatic constriction → elephantiasis mechanism |
| [19061590](https://pubmed.ncbi.nlm.nih.gov/19061590/) | Malignant transformation (HIV+) | Case report | SCC complication of chronic donovanosis |
| [8735293](https://pubmed.ncbi.nlm.nih.gov/8735293/) | GI in pregnancy & HIV | Clinical series | Benign pregnancy outcome; no congenital transmission |
| [9924476](https://pubmed.ncbi.nlm.nih.gov/9924476/) | Extragenital donovanosis of foot | Case report | Rare extragenital localization |
| [22335265](https://pubmed.ncbi.nlm.nih.gov/22335265/) | Diagnosis/management of genital ulcers | Review | Doxycycline 21 d; differential diagnosis; ≤25% undiagnosed |
| [39566736](https://pubmed.ncbi.nlm.nih.gov/39566736/) | AEDV ulcerative-STI management | Guideline | Non-infectious mimics in differential |
| [12473810](https://pubmed.ncbi.nlm.nih.gov/12473810/) | Donovanosis review | Review | Australian elimination program; declining incidence |
| [11394976](https://pubmed.ncbi.nlm.nih.gov/11394976/) | Donovanosis: an update | Review | Re-culture after >30 y; prolonged therapy in HIV; cost of azithromycin |

**Consistency of evidence:** Findings are internally consistent across independent guidelines (European 2010/2016), large clinical series (Durban), and mechanistic ultrastructural studies. Taxonomic reclassification is supported by two independent sequencing studies; the HIV-cofactor role by a large cross-sectional study with statistically significant associations. The main evidentiary weakness is reliance on case reports/series for complication rates (SCC, elephantiasis) and the near-total absence of pathogen omics data.

---

## Limitations & Future Directions

- The pathogen's culture difficulty leaves its **genome, virulence factors, and molecular immunology poorly defined**; whole-genome sequencing and in vitro/organoid infection models are key future needs.
- **Epidemiologic surveillance is sparse** (no dedicated global registry); true incidence/prevalence and sex/age distributions are uncertain and setting-dependent.
- Modern PCR-based diagnostics and controlled treatment trials are limited by the disease's rarity.
- Evidence is dominated by case reports/series and expert-guideline consensus rather than RCTs.
- Several template sections (host genetics, model organisms, omics, pharmacogenomics) are **inherently Not Applicable** to a non-genetic infectious disease.

## Proposed Follow-up Actions

1. **Whole-genome sequencing of *K. granulomatis*** from clinical isolates (via monocyte/Hep-2 co-culture) to define virulence factors, capsule/LPS loci, and confirm genome-scale *Klebsiella* placement.
2. **Develop a tractable infection model** (humanized macrophage system, skin organoid, or small-animal model) to study intracellular persistence, Donovan-body formation, and antibiotic penetration.
3. **Standardized PCR surveillance** in remaining endemic foci (PNG, India, Brazil) to quantify true incidence and monitor progress toward eradication.
4. **Prospective cohort follow-up** to estimate the risk and triggers of squamous-cell-carcinoma transformation, currently known only anecdotally.
5. **Integrate donovanosis elimination with HIV-prevention programs**, leveraging the demonstrated HIV-cofactor relationship (PMID 2063236).
6. **Cost-effectiveness analysis of azithromycin** to support universal first-line adoption (historical cost barrier; PMID 11394976).
7. **Public-health communication** to counter "flesh-eating infection" misinformation and reduce stigma (PMID 41016613).

---

### Key Citations (PMID)
41016613 · 42486240 · 10555350 · 10482295 · 22239475 · 12635932 · 26882914 · 21097731 · 12473810 · 11394976 · 8509089 · 2063236 · 7750949 · 1398660 · 8735293 · 16510000 · 18317211 · 9856642 · 2777345 · 11100808 · 19061590 · 24554002 · 26396449 · 9924476 · 22335265 · 39566736


## Artifacts

- [OpenScientist final report](Granuloma_Inguinale-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Granuloma_Inguinale-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100820` (1 mention) - the report calls it "Genital/vulval swelling → elephantiasis"; HP calls it **Glomerulopathy**
- `GO:0006954` (1 mention) - the report calls it "Cellular processes:** chronic inflammation"; GO calls it **inflammatory response**
- `GO:0045335` (3 mentions) - the report calls it "cytoplasmic vacuoles/phagosomes", "Subcellular:** bacteria within macrophage **cytoplasmic vacuoles/phagosomes"; GO calls it **phagocytic vesicle**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002860` (1 mention) - the report calls it "Secondary squamous cell carcinoma"; HP calls it **Squamous cell carcinoma**
- `UBERON:0000002` (2 mentions) - the report calls it "uterine cervix", "cervix"; UBERON calls it **uterine cervix**, and lists "cervix" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0045335` - called "cytoplasmic vacuoles/phagosomes", "Subcellular:** bacteria within macrophage **cytoplasmic vacuoles/phagosomes"
- `UBERON:0000002` - called "uterine cervix", "cervix"