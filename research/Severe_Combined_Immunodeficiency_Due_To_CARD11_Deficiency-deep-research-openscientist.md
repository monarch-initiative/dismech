---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T19:10:12.569317'
end_time: '2026-09-05T19:43:14.658909'
duration_seconds: 1982.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe Combined Immunodeficiency Due To CARD11 Deficiency
  mondo_id: MONDO:0014081
  category: Genetic
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 10
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014081
    reported_labels:
    - MONDO
    ontology_label: severe combined immunodeficiency due to CARD11 deficiency
  - term_id: CL:0002679
    reported_labels:
    - regulatory T cell
    ontology_label: natural helper lymphocyte
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0005435
    ontology_label: obsolete Impaired T cell function
    replaced_by: HP:0011840
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Combined Immunodeficiency Due To CARD11 Deficiency
- **MONDO ID:** MONDO:0014081 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Severe Combined Immunodeficiency Due To CARD11 Deficiency** covering all of the
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

# Severe Combined Immunodeficiency Due To CARD11 Deficiency — Comprehensive Disease Report

**MONDO ID:** MONDO:0014081 · **Category:** Genetic (autosomal-recessive inborn error of immunity)
**Gene:** *CARD11* (HGNC:16393; 7p22.2) · **OMIM phenotype:** #615206 (Immunodeficiency 11A, IMD11A)

---

## Summary

Severe combined immunodeficiency (SCID) due to CARD11 deficiency is an ultra-rare, autosomal-recessive inborn error of immunity caused by **biallelic loss-of-function (LOF) variants in *CARD11***, the lymphocyte-restricted scaffold protein that nucleates the **CARD11–BCL10–MALT1 (CBM) signalosome** downstream of the T- and B-cell antigen receptors. Complete absence of functional CARD11 abolishes assembly of the CBM complex and cripples antigen-receptor–driven activation of **NF-κB**, **c-Jun N-terminal kinase (JNK)**, and **MALT1 paracaspase**, together with a metabolic arm that couples the antigen receptor to **glutamine uptake and mTORC1**. The immunological hallmark is **agammaglobulinemia with profoundly deficient T-cell function despite numerically normal circulating T and B lymphocytes** — a functional SCID phenotype ([PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/); [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/)).

Affected infants present early in life with life-threatening opportunistic infections (e.g., *Pneumocystis jirovecii* pneumonia, cytomegalovirus, recurrent viral and fungal respiratory infections), **interstitial lung disease**, and **severe colitis**. Because standard SCID newborn screening relies on quantifying **T-cell receptor excision circles (TRECs)**, which detect T-cell lymphopenia, CARD11 deficiency — with numerically normal T cells — can escape TREC-based screening, making functional immunology and genetic sequencing essential for diagnosis ([PMID: 42466165](https://pubmed.ncbi.nlm.nih.gov/42466165/)). The definitive therapy is **allogeneic hematopoietic stem cell transplantation (HSCT)**, which is curative because CARD11 is lineage-restricted to hematopoietic tissue and the defect is intrinsic to lymphocytes ([PMID: 40625738](https://pubmed.ncbi.nlm.nih.gov/40625738/); [PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)).

*CARD11* sits at the center of a striking **allelic series**: biallelic null variants cause SCID/combined immunodeficiency; heterozygous gain-of-function (GOF) variants cause **BENTA** (B-cell Expansion with NF-κB and T-cell Anergy); and heterozygous dominant-interfering LOF variants cause **severe atopic disease/CID**. CARD11 deficiency is furthermore one of three interchangeable **CBM-complex combined immunodeficiencies** (with BCL10 and MALT1 deficiency) that phenocopy one another, defining the core differential-diagnosis group. This report synthesizes 10 confirmed findings from 42 reviewed papers across all requested disease-characteristic dimensions.

---

## 1. Disease Information

**Overview.** CARD11-deficiency SCID is a monogenic combined immunodeficiency in which complete loss of the CARD11 scaffold prevents antigen-receptor signaling in T and B lymphocytes. It was first defined as a novel SCID entity by whole-exome sequencing in 2013 ([PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/)). Clinically it behaves as a SCID/profound combined immunodeficiency (CID) but is biochemically distinct from lymphopenic SCIDs because lymphocyte *numbers* are preserved while lymphocyte *function* is lost.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014081 |
| OMIM (phenotype) | #615206 — Immunodeficiency 11A (IMD11A) |
| Gene | *CARD11*, HGNC:16393, NCBI Gene 84433, UniProt Q9BXL7 |
| Cytoband | 7p22.2 |
| Orphanet | Combined immunodeficiency due to CARD11 deficiency (rare inborn error of immunity) |
| ICD-11 | 4A00.1 (combined immunodeficiencies) |
| MeSH | Severe Combined Immunodeficiency (D016511); CARD Signaling Adaptor Proteins |

**Synonyms / alternative names.** Immunodeficiency 11A; CARD11 deficiency; complete CARD11 deficiency; combined immunodeficiency due to CARD11 deficiency; CARMA1 deficiency (CARD11 = CARMA1 = "CARD-containing MAGUK protein 1").

**Source of information.** Predominantly **aggregated disease-level and individual-patient case reports** — the literature comprises a small number of unrelated families/probands described in detail, plus mechanistic and structural studies. There is no large registry or EHR-derived cohort given the rarity.

---

## 2. Etiology

**Disease causal factors.** The disease is **purely genetic and monogenic**: biallelic (homozygous or compound-heterozygous) LOF variants in *CARD11* are necessary and sufficient. There is **no environmental, infectious, or lifestyle cause** — infections are consequences, not causes. Consanguinity is a recurrent contributing circumstance because it raises the chance of homozygosity for a rare recessive null allele (the index case was an infant of consanguineous parents; [PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/)).

**Genetic risk factors.** The causal variants themselves are the risk factor. Reported pathogenic alleles include the nonsense variant **c.2509C>T; p.Arg837\*** (recurrent, producing undetectable protein) and **p.Cys150\*** ([PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/); [PMID: 26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/)). No common susceptibility loci or modifier genes have been established for the recessive SCID form.

**Environmental / protective factors.** None established. The only "protective" genetic event documented is a **somatic second-site reversion** in a patient that partially restored CARD11 function and converted the phenotype toward Omenn syndrome ([PMID: 26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/)). In *hypomorphic* (not null) CARD11 disease, **glutamine supplementation** partially rescued downstream mTORC1/IFN-γ defects — a metabolic modifier relevant to residual-function alleles but not to complete deficiency ([PMID: 28628108](https://pubmed.ncbi.nlm.nih.gov/28628108/)).

**Gene–environment interactions.** Not applicable in the classical GxE sense; the phenotype is fully genetically determined, though clinical severity is shaped by the pathogen exposures the immunodeficient host encounters.

---

## 3. Phenotypes

CARD11-deficiency SCID phenotypes fall into infection, immune-dysregulation/inflammatory, and laboratory categories. Onset is **neonatal to early-infancy**; severity is **severe**; course is **progressive/life-threatening without treatment**.

| Phenotype | Type | Onset / severity | Suggested HPO term |
|---|---|---|---|
| Recurrent/opportunistic infections (*Pneumocystis jirovecii* pneumonia, CMV, sepsis) | Clinical sign | Neonatal–infancy; severe | HP:0002718 (Recurrent bacterial infections); HP:0002754 (Recurrent respiratory infections); HP:0032256 (Pneumocystis pneumonia) |
| Interstitial lung disease | Clinical/imaging sign | Infancy; severe | HP:0006530 (Interstitial pulmonary abnormality) |
| Severe colitis / chronic diarrhea | Clinical sign | Infancy; severe | HP:0002583 (Colitis); HP:0002014 (Diarrhea) |
| Agammaglobulinemia / hypogammaglobulinemia | Laboratory abnormality | Congenital; severe | HP:0004432 (Decreased circulating total IgG); HP:0002090 |
| Profoundly deficient T-cell function (poor proliferation to mitogens/antigens) | Laboratory abnormality | Congenital; severe | HP:0002843 (Abnormal T cell proliferation); HP:0005435 (Impaired T cell function) |
| Numerically normal T and B lymphocyte counts (distinguishing feature) | Laboratory finding | Congenital | (normal count — diagnostic caveat) |
| Omenn features on reversion (erythroderma, lymphoproliferation, elevated IgE, oligoclonal T cells) | Physical/laboratory | Infancy; severe | HP:0001019 (Erythroderma); HP:0003212 (Increased circulating IgE); HP:0100827 (Lymphocytosis) |
| Failure to thrive | Physical manifestation | Infancy | HP:0001508 (Failure to thrive) |

*"presented with profound CID associated with viral and fungal respiratory infections, interstitial lung disease, and severe colitis"* — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/).

*"The novel entity of SCID was characterized by agammaglobulinemia and profoundly deficient T-cell function despite quantitatively normal T and B lymphocytes."* — [PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/).

**Frequency.** With only a handful of reported patients, frequencies are qualitative: opportunistic infection, agammaglobulinemia, and defective T-cell function are essentially universal; interstitial lung disease and colitis are frequently reported; Omenn-syndrome presentation is exceptional (reversion-dependent).

**Quality-of-life impact.** Untreated disease is incompatible with normal life — recurrent life-threatening infection, chronic colitis with malabsorption, and respiratory compromise impose profound morbidity. Successful HSCT can restore near-normal immune function and quality of life.

---

## 4. Genetic / Molecular Information

**Causal gene.** *CARD11* (CARMA1), 7p22.2, encoding a 1154-aa multidomain membrane-associated guanylate kinase (MAGUK) scaffold with an N-terminal **CARD**, a **LATCH**, a **coiled-coil**, an autoinhibitory **inhibitory domain (ID)**, and C-terminal **PDZ–SH3–GUK** modules.

**Pathogenic variants (recessive SCID form).**

| Variant (cDNA / protein) | Type | Consequence | Reference |
|---|---|---|---|
| c.2509C>T; p.Arg837\* | Nonsense | Undetectable protein (complete deficiency); prevents CBM assembly | [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/) |
| Homozygous nonsense (truncating) | Nonsense | Truncated CARD11 defective in antigen-receptor signaling and NF-κB activation | [PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/) |
| p.Cys150\* | Nonsense | Impaired NF-κB signaling and IL-2 production | [PMID: 26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/) |

**Variant classification.** Truncating null alleles are **pathogenic** (ACMG: PVS1 loss-of-function + segregation + functional data). Functional reconstitution assays confirmed patient-derived truncated CARD11 is signaling-defective ([PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/)).

**Variant type/class.** Predominantly **nonsense/truncating LOF**. **Allele frequency:** these specific pathogenic nulls are extremely rare/private in gnomAD, consistent with a severe recessive disease. **Origin:** **germline** (the disease-causing alleles); note the exception of a **somatic** second-site reversion that mitigated one patient's phenotype ([PMID: 26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/)). Somatic *CARD11* GOF mutations are separately associated with B-cell lymphomas (not this disease).

**Functional consequence.** **Complete loss of function** — abolition of the scaffold prevents any BCL10 nucleation. This contrasts with (a) **dominant-negative** heterozygous LOF alleles that poison wild-type CARD11 (atopy/CID) and (b) **gain-of-function** alleles that bypass autoinhibition (BENTA / lymphoma).

**The CARD11 allelic series** (a defining feature): *"Germline CARD11 mutations cause several distinct primary immune disorders in human subjects, including severe combined immune deficiency (biallelic null mutations), B-cell expansion with nuclear factor κB and T-cell anergy (heterozygous, gain-of-function mutations), and severe atopic disease (loss-of-function, heterozygous, dominant interfering mutations)"* — [PMID: 30170123](https://pubmed.ncbi.nlm.nih.gov/30170123/).

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes for the recessive SCID form. No disease-specific epigenetic signature or chromosomal abnormality — this is a single-gene coding disorder.

---

## 5. Environmental Information

**Not applicable as a cause.** CARD11-deficiency SCID has **no environmental, lifestyle, or toxicological etiology**. Infectious agents (*Pneumocystis jirovecii*, cytomegalovirus, and other viral/fungal/bacterial pathogens) are **downstream consequences** of the immunodeficiency rather than triggers. Practical environmental relevance is limited to **infection-avoidance / protective isolation** and avoidance of **live vaccines** in the immunodeficient host prior to definitive therapy.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic null *CARD11* variant** (e.g., p.Arg837\*) → **absent/non-functional CARD11 scaffold protein** in lymphocytes (demonstrated: undetectable protein) — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/).
2. Absent CARD11 → **failure of receptor-triggered closed→open conformational activation** of the scaffold (CARD11 normally relieved from autoinhibition by PKCθ/β phosphorylation) — [PMID: 20799731](https://pubmed.ncbi.nlm.nih.gov/20799731/).
3. No open CARD11 → **no nucleation of BCL10 filaments** and **failure of CARD11–BCL10–MALT1 (CBM) complex assembly** — [PMID: 31296852](https://pubmed.ncbi.nlm.nih.gov/31296852/); [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/).
4. No CBM signalosome → **severely impaired activation of NF-κB, JNK, and MALT1 paracaspase** in both B and T cells (demonstrated) — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/).
   - **Branch A (metabolic):** CBM loss → **impaired TCR-stimulated glutamine uptake and mTORC1 activation**, independent of IKK — [PMID: 24792914](https://pubmed.ncbi.nlm.nih.gov/24792914/).
   - **Branch B (cytokine):** CBM loss → **impaired IL-2 production** — [PMID: 26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/).
5. Impaired NF-κB/JNK/MALT1 signaling → **developmental block in B cells at the naive/type-1 transitional stage** and **impaired circulating T follicular helper cells / defective T-cell effector function** — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/).
6. Defective lymphocyte activation and differentiation → **agammaglobulinemia + profoundly deficient T-cell function despite normal lymphocyte counts** — [PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/).
7. Loss of protective adaptive immunity → **early-life opportunistic infections, interstitial lung disease, colitis** → life-threatening combined immunodeficiency — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/).

*(Inferred branch: an Omenn-syndrome phenotype can arise when a **somatic second-site reversion** partially restores CARD11, generating oligoclonal autoreactive T cells — [PMID: 26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/).)*

### Detail by category

- **Molecular pathways.** Antigen-receptor (TCR/BCR) → PKCθ/β → **CARD11** → BCL10/MALT1 → IKK → **canonical NF-κB**; parallel arms to **JNK/AP-1** and **MALT1 protease**; and a metabolic arm to **glutamine/ASCT2 → mTORC1** ([PMID: 24792914](https://pubmed.ncbi.nlm.nih.gov/24792914/); [PMID: 26260210](https://pubmed.ncbi.nlm.nih.gov/26260210/)). Suggested pathway refs: KEGG NF-κB signaling; Reactome "CARD11-BCL10-MALT1 assembly."
- **Cellular processes.** Lymphocyte activation, proliferation, survival, and effector-lineage differentiation (Th17 differentiation requires CARMA1; [PMID: 23091043](https://pubmed.ncbi.nlm.nih.gov/23091043/)); thymic Treg commitment (see model organisms).
- **Protein dysfunction.** Complete loss of scaffold function (null); by contrast, GOF variants disrupt the autoinhibitory ID interface causing spontaneous BCL10 filament formation — [PMID: 31296852](https://pubmed.ncbi.nlm.nih.gov/31296852/); [PMID: 26884335](https://pubmed.ncbi.nlm.nih.gov/26884335/).
- **Metabolic changes.** Loss of CARD11-dependent glutamine import → reduced mTORC1 activity → reduced IFN-γ (documented in hypomorphic disease, partially glutamine-rescuable) — [PMID: 28628108](https://pubmed.ncbi.nlm.nih.gov/28628108/).
- **Immune-system involvement.** Combined (T + B) **immunodeficiency**; the immune failure is the disease.
- **Molecular profiling.** Reconstitution and reporter assays establish the NF-κB defect; patient B-cell developmental staging documents the transitional block ([PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/)).

**Upstream vs downstream:** the mutation and absent scaffold are upstream; NF-κB/JNK/MALT1/mTORC1 failure is intermediate; lymphocyte developmental/functional defects and clinical infection are downstream.

**Suggested GO / CL terms.** GO:0007249 (I-κB kinase/NF-κB signaling); GO:0050852 (T-cell receptor signaling pathway); GO:0050853 (B-cell receptor signaling pathway); GO:0002250 (adaptive immune response). Cell types: CL:0000084 (T cell), CL:0000236 (B cell), CL:0002679 (regulatory T cell), CL:0000788 (naive B cell).

---

## 7. Anatomical Structures Affected

- **Organ / system level.** **Immune (lymphoid) system** primarily: thymus, bone marrow, spleen, lymph nodes, mucosa-associated lymphoid tissue. Secondary organ involvement from immune failure: **lungs** (interstitial lung disease; UBERON:0002048) and **gastrointestinal tract / colon** (colitis; UBERON:0001155). Systems involved: immune/hematopoietic; secondarily respiratory and digestive.
- **Tissue / cell level.** **Lymphocytes** — T cells (CL:0000084), B cells (CL:0000236), T follicular helper cells (CL:0002038), regulatory T cells (CL:0002679), naive/transitional B cells (CL:0000788). Hematopoietic tissue is the site of the intrinsic defect.
- **Subcellular level.** CARD11 acts at the **plasma membrane / cytoplasmic signalosome**; GO cellular components: GO:0032449 (CBM complex), GO:0005886 (plasma membrane), GO:0005829 (cytosol).
- **Localization / lateralization.** Systemic and **bilateral/diffuse** — a whole-body lymphoid disorder, not a focal lesion. The immune-restricted anatomy is explained by **lineage-restricted CARD11 expression**: *"CARD11 is primarily expressed in hematopoietic tissues and lymphocytes and plays a crucial role in the proper activation of B and T cells in response to antigen recognition"* — [PMID: 40625738](https://pubmed.ncbi.nlm.nih.gov/40625738/).

---

## 8. Temporal Development

- **Onset.** **Congenital defect; clinical onset in the neonatal period/early infancy** with opportunistic infection — *"in patients with severe combined immunodeficiency (SCID), infections caused by opportunistic pathogens are typically life-threatening early in life"* — [PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/). Onset pattern is **acute-on-chronic** (an underlying congenital immune defect punctuated by acute infections).
- **Progression.** **Progressive and life-threatening** without intervention; no spontaneous remission (except the rare partial, somatic-reversion event that alters rather than cures the phenotype). Disease duration is **lifelong** unless corrected by HSCT.
- **Critical period / window of opportunity.** Early diagnosis before overwhelming infection is critical; **HSCT before infectious/organ damage accrues** offers the best outcomes, as for other SCIDs.

---

## 9. Inheritance and Population

- **Inheritance.** **Autosomal recessive** (biallelic null). Consanguinity increases risk via homozygosity ([PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/)). By contrast, dominant-negative LOF and GOF *CARD11* disorders are autosomal dominant — the same gene yields different inheritance depending on allele class ([PMID: 30170123](https://pubmed.ncbi.nlm.nih.gov/30170123/); [PMID: 25645939](https://pubmed.ncbi.nlm.nih.gov/25645939/)).
- **Penetrance / expressivity.** Biallelic null penetrance is presumed **complete** for the immunodeficiency; expressivity can vary (e.g., Omenn presentation via somatic reversion).
- **Epidemiology.** **Ultra-rare** — described in a small number of unrelated families worldwide; no reliable prevalence/incidence estimate exists. It is a small fraction of overall SCID incidence (SCID overall ~1 in 50,000–100,000 births).
- **Founder effects / carrier frequency.** No established founder allele; carrier frequency is expected to be very low, elevated within consanguineous kindreds.
- **Demographics.** No sex predilection (autosomal). Reported across different populations; consanguineous families are over-represented among cases.

---

## 10. Diagnostics

**Laboratory / immunological.** Serum immunoglobulins (**agammaglobulinemia/hypogammaglobulinemia**), **lymphocyte subset enumeration** (T and B counts **normal** — a key discriminator), and **functional T-cell proliferation** to mitogens (PHA) and antigens (**profoundly reduced**) ([PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/)). Suggested LOINC-type panels: immunoglobulin quantitation, lymphocyte subset panel, lymphocyte mitogen stimulation.

**Functional confirmation.** **NF-κB activation and CBM assembly assays / reconstitution assays** demonstrating that patient-derived CARD11 is signaling-defective ([PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/); [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/)).

**Genetic testing.** **WES/WGS or targeted PID gene panels including *CARD11*** are the definitive diagnostic modality; single-gene sequencing confirms biallelic variants and segregation. Chromosomal microarray/karyotype/FISH are not indicated (point mutations, not structural).

**Newborn-screening caveat (critical).** SCID NBS quantifies **TRECs**, which reflect **T-cell lymphopenia**; CARD11-deficient patients have **numerically normal T cells** and may therefore **screen normal (false-negative)**. *"Newborn screening (NBS) based on quantifying T cell receptor excision circles (TRECs) is highly sensitive for detecting severe combined immunodeficiency (SCID)"* — [PMID: 42466165](https://pubmed.ncbi.nlm.nih.gov/42466165/) — but this sensitivity depends on lymphopenia the patient does not exhibit. **Second-tier genetic screening** can improve accuracy for such non-lymphopenic T-cell defects.

**Differential diagnosis.** Other **CBM-complex combined immunodeficiencies** — **BCL10** and **MALT1** deficiency — phenocopy CARD11 deficiency and constitute the primary differential group: *"a broad range of clinical manifestations, including those characteristic of T- and B-lymphocyte defects, are associated with CARD11, MALT1, and BCL10 deficiencies"* — [PMID: 26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/). **CARD9 deficiency** is distinguished because it causes **isolated invasive fungal infection** (innate CBM), not combined immunodeficiency ([PMID: 26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/)). Also consider other SCID/CID genes, hyper-IgE syndromes, and (for the reversion phenotype) Omenn syndrome.

---

## 11. Outcome / Prognosis

- **Natural history (untreated).** Poor — early-life opportunistic infection, interstitial lung disease, and colitis carry high mortality, consistent with SCID.
- **With treatment.** **Allogeneic HSCT is potentially curative.** By analogy within the CBM group, MALT1 deficiency has been **successfully treated and immunologically normalized by HSCT** ([PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)), and CARD11's lineage-restricted (hematopoietic) expression means donor immune reconstitution corrects the intrinsic defect ([PMID: 40625738](https://pubmed.ncbi.nlm.nih.gov/40625738/)).
- **Morbidity / complications.** Chronic lung disease, colitis with malabsorption/failure to thrive, disseminated infection; transplant-related complications (GVHD, conditioning toxicity, viral reactivation).
- **Prognostic factors.** Age at diagnosis and transplant, organ/infectious damage at HSCT, donor match, and conditioning regimen. Early, pre-damage transplant favors better outcomes.

---

## 12. Treatment

**Definitive therapy.**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — the curative standard for CBM-complex combined immunodeficiencies, ideally with reduced-intensity conditioning; supported by successful normalization in MALT1 deficiency ([PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)). NCIT: C15431 (Hematopoietic Stem Cell Transplantation).

**Supportive / bridging pharmacotherapy.**
- **Immunoglobulin replacement therapy (IVIG/SCIG)** for agammaglobulinemia. NCIT: C29294 (Intravenous Immunoglobulin Therapy).
- **Anti-infective prophylaxis** — *Pneumocystis jirovecii* prophylaxis (trimethoprim-sulfamethoxazole), antifungal and antiviral prophylaxis; treatment of intercurrent infections.
- **Avoid live vaccines**; use irradiated/CMV-safe blood products.

**Experimental / metabolic.** In **hypomorphic** (residual-function) CARD11 disease, **glutamine supplementation** partially rescued mTORC1 and IFN-γ defects — a proof-of-concept metabolic intervention that requires residual CARD11 for glutamine import and is therefore **not expected to help complete null deficiency** ([PMID: 28628108](https://pubmed.ncbi.nlm.nih.gov/28628108/)). Gene therapy/gene correction is conceptually attractive (hematopoietic-restricted, single-gene) but not clinically established for this disease.

**Personalized-medicine note.** Treatment is genotype-specific across the allelic series: null SCID → immune reconstitution (HSCT); GOF BENTA → immunosuppression (e.g., sirolimus/mTOR inhibition; [PMID: 39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/)). Correctly classifying the allele is essential to avoid opposite treatment errors.

---

## 13. Prevention

- **Primary prevention.** Not preventable at the individual level (germline recessive). Population-level: **genetic counseling and carrier testing** in consanguineous families or families with a prior affected child; **preimplantation/prenatal genetic diagnosis** and **cascade testing** of relatives once the familial variant is known.
- **Secondary prevention.** Early detection — although **TREC NBS may miss CARD11 deficiency** (normal T-cell counts), **second-tier genetic screening** and a high index of suspicion in infants with hypogammaglobulinemia + poor T-cell function improve early diagnosis ([PMID: 42466165](https://pubmed.ncbi.nlm.nih.gov/42466165/)).
- **Tertiary prevention.** Infection prophylaxis, protective isolation, irradiated blood products, avoidance of live vaccines, and timely HSCT to prevent irreversible organ damage.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** Human *CARD11* has a conserved mouse ortholog ***Card11*** (a.k.a. *Carma1*; NCBI Gene 108723; *Mus musculus*, NCBI:txid10090). Orthologs exist across mammals; the CBM signaling module is evolutionarily conserved.
- **Natural disease in other species.** No well-characterized naturally occurring companion-animal or wildlife disease is established for CARD11 in OMIA; disease knowledge derives from engineered mouse models rather than spontaneous animal disease.
- **Comparative biology.** Mouse *Card11* loss recapitulates key lymphocyte-activation and Treg defects (below), but concordance with humans is partial: *"human subjects with these mutations have some features in common with the corresponding knockout mice, but other features are different between human subjects and mice"* — [PMID: 26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/).
- **Zoonotic potential.** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

- **Model type.** **Mammalian (mouse)** genetic models predominate — **Card11/CARMA1 knockout and point-mutant** mice — plus **in vitro** cellular systems (Jurkat T cells, HEK293T reconstitution/reporter assays) used for functional validation.
- **Phenotype recapitulation.** *Card11*/CARMA1-KO mice show that the **CBM complex is required cell-intrinsically for thymic development of Foxp3+ regulatory T cells** and gate an early Treg-commitment checkpoint: *"The CARMA1/Bcl10/Malt1 (CBM) complex... is required for development of regulatory T cells (Tregs) but not conventional T cells"* — [PMID: 19454668](https://pubmed.ncbi.nlm.nih.gov/19454668/). CARMA1 is also required for **Th17 differentiation**, and KO mice are **resistant to experimental autoimmune encephalomyelitis** ([PMID: 23091043](https://pubmed.ncbi.nlm.nih.gov/23091043/)).
- **Model limitations.** Human–mouse concordance is partial ([PMID: 26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/)); mouse models capture the lymphocyte-activation/Treg biology but not every clinical feature (e.g., the human interstitial lung disease/colitis spectrum).
- **Applications.** Dissecting CBM signaling, Treg/Th17 development, NF-κB thresholds, and glutamine/mTORC1 coupling ([PMID: 24792914](https://pubmed.ncbi.nlm.nih.gov/24792914/); [PMID: 39368135](https://pubmed.ncbi.nlm.nih.gov/39368135/)).
- **Resources.** MGI (*Card11*), IMPC/KOMP for knockout alleles; Cellosaurus for Jurkat/HEK293T lines.

---

## Key Findings (with evidence)

### F001 — Biallelic loss-of-function *CARD11* variants cause autosomal-recessive SCID
Multiple unrelated patients with homozygous null *CARD11* variants (e.g., p.Arg837\* / c.2509C>T; other nonsense mutations; p.Cys150\*) present with profound combined immunodeficiency, and **reconstitution assays confirm patient-derived truncated CARD11 is defective in antigen-receptor signaling and NF-κB activation**. Consanguinity recurs (index case born to consanguineous parents). *"Genetic analysis revealed a single pathogenic homozygous nonsense mutation of the caspase recruitment domain 11 (CARD11) gene. In reconstitution assays we demonstrated that the patient-derived truncated CARD11 protein is defective in antigen receptor signaling and nuclear factor κB activation."* — [PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/). *"Both patients carried identical novel pathogenic biallelic loss-of-function variants in CARD11 (c.2509C>T; p.Arg837∗) leading to undetectable protein expression."* — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/).

### F002 — Mechanism: CARD11 loss abrogates CBM-driven NF-κB, JNK and MALT1 activation
In patient B and T cells, biallelic null variants prevent CBM-complex formation and severely impair NF-κB, JNK, and MALT1 paracaspase activity, producing a **B-cell developmental block at the naive/type-1 transitional stage** and impaired IL-2 production. *"This variant prevented CBM complex formation, severely impairing the activation of nuclear factor-κB, c-Jun N-terminal kinase, and MALT1 paracaspase activity in B and T cells. This functional defect resulted in a developmental block in B cells at the naive and type 1 transitional B-cell stage"* — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/). *"Both carried homozygous germline mutations in CARD11 (p.Cys150\*), impairing NF-κB signaling and IL-2 production."* — [PMID: 26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/).

### F003 — Clinical spectrum and curative HSCT
Patients present early in life with life-threatening infections, interstitial lung disease, and severe colitis; the laboratory hallmark is agammaglobulinemia with deficient T-cell function despite normal counts; an Omenn phenotype can arise via somatic reversion; and HSCT is definitive therapy for CBM-complex CID. *"presented with profound CID associated with viral and fungal respiratory infections, interstitial lung disease, and severe colitis"* — [PMID: 33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/). *"The clinical and immunological phenotype of MALT1 deficiency can be successfully treated with hematopoietic stem cell transplantation following reduced intensity conditioning."* — [PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/).

### F004 — CARD11 allelic series (null SCID vs dominant-negative atopy vs GOF BENTA)
Distinct germline *CARD11* variant classes cause distinct diseases. *"Germline CARD11 mutations cause several distinct primary immune disorders in human subjects, including severe combined immune deficiency (biallelic null mutations), B-cell expansion with nuclear factor κB and T-cell anergy (heterozygous, gain-of-function mutations), and severe atopic disease (loss-of-function, heterozygous, dominant interfering mutations)"* — [PMID: 30170123](https://pubmed.ncbi.nlm.nih.gov/30170123/).

### F005 — Mouse models recapitulate lymphocyte-activation and thymic Treg defects
*"The CARMA1/Bcl10/Malt1 (CBM) complex... is required for development of regulatory T cells (Tregs) but not conventional T cells"* — [PMID: 19454668](https://pubmed.ncbi.nlm.nih.gov/19454668/), with partial human concordance — [PMID: 26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/).

### F006 — CARD11 couples the antigen receptor to glutamine/mTORC1
*"TCR-stimulated glutamine uptake and mTORC1 activation also required a TCR signaling complex composed of the scaffold protein CARMA1, the adaptor molecule BCL10, and the paracaspase MALT1. This function was independent of IKK kinase"* — [PMID: 24792914](https://pubmed.ncbi.nlm.nih.gov/24792914/). *"The mTORC1 and IFN-γ production defects were partially rescued by supplementation with glutamine, which requires CARD11 for import into T cells."* — [PMID: 28628108](https://pubmed.ncbi.nlm.nih.gov/28628108/).

### F007 — TREC newborn screening can miss CARD11 deficiency
Because T-cell numbers are normal, TREC-based NBS may be falsely normal. *"The novel entity of SCID was characterized by agammaglobulinemia and profoundly deficient T-cell function despite quantitatively normal T and B lymphocytes."* — [PMID: 23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/). *"Newborn screening (NBS) based on quantifying T cell receptor excision circles (TRECs) is highly sensitive for detecting severe combined immunodeficiency (SCID)"* — [PMID: 42466165](https://pubmed.ncbi.nlm.nih.gov/42466165/).

### F008 — One of three phenocopying CBM-complex immunodeficiencies
*"a broad range of clinical manifestations, including those characteristic of T- and B-lymphocyte defects, are associated with CARD11, MALT1, and BCL10 deficiencies"* and *"Isolated invasive fungal infections of unclear cellular basis are associated with CARD9 deficiency"* — [PMID: 26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/).

### F009 — Structural basis: autoinhibited scaffold that templates BCL10 filaments
*"disruption of this interface leads to hyperactivation in cells and to the formation of Bcl10-templating filaments in vitro, illuminating the mechanism of action of numerous oncogenic mutations of CARD11"* — [PMID: 31296852](https://pubmed.ncbi.nlm.nih.gov/31296852/). *"the multidomain scaffold protein CARD11 undergoes a transition from a closed, inactive state to an open, active conformation that recruits several signaling proteins into a complex, leading to IKK kinase activation"* — [PMID: 20799731](https://pubmed.ncbi.nlm.nih.gov/20799731/).

### F010 — Lineage-restricted expression explains the immune-restricted phenotype
*"CARD11 is primarily expressed in hematopoietic tissues and lymphocytes and plays a crucial role in the proper activation of B and T cells in response to antigen recognition"* — [PMID: 40625738](https://pubmed.ncbi.nlm.nih.gov/40625738/).

---

## Mechanistic Model / Interpretation

```
 Biallelic null CARD11 (e.g., p.Arg837*)   [germline, autosomal recessive]
                 |  absent/nonfunctional scaffold
                 v
 No PKCtheta/beta-triggered closed->open CARD11 activation   [PMID:20799731]
                 |
                 v
 No BCL10 filament nucleation -> no CBM signalosome   [PMID:31296852, 33872653]
                 |
     +-----------+---------------+-------------------+
     v           v               v                   v
   NF-kB v     JNK/AP-1 v     MALT1 protease v    Glutamine->mTORC1 v (IKK-independent)
     |           |               |                   |            [PMID:24792914]
     +-----+-----+-------+-------+                   +-- IFN-gamma v, IL-2 v [PMID:26289640]
           v             v
  B-cell block at        Defective T-cell effector /
  naive/transitional     Tfh function                 [PMID:33872653]
           |             |
           +------+------+
                  v
  Agammaglobulinemia + poor T-cell function
  DESPITE NORMAL T & B CELL COUNTS         [PMID:23561803]  -> TREC NBS may miss it [PMID:42466165]
                  |
                  v
  Early-life opportunistic infection, interstitial lung disease, colitis
                  |                              (Omenn variant via somatic reversion [PMID:26289640])
                  v
  Curative: allogeneic HSCT (lineage-restricted, hematopoietic-intrinsic) [PMID:40625738, 27109639]
```

The unifying insight is that CARD11 is a **lymphocyte-restricted molecular switch**: an autoinhibited scaffold whose receptor-triggered opening nucleates the CBM signalosome. **The direction and dose of the perturbation dictate the disease** — complete loss disables adaptive immunity (SCID), dominant-interfering loss partially poisons it (atopy/CID), and constitutive gain hyperactivates it (BENTA/lymphoma). Because expression is confined to hematopoietic cells, the phenotype is immune-restricted and, crucially, **fully correctable by replacing the hematopoietic compartment via HSCT**.

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [23561803](https://pubmed.ncbi.nlm.nih.gov/23561803/) | Defines CARD11 inactivation as SCID; normal counts, defective function; reconstitution assay | Human clinical + in vitro |
| [33872653](https://pubmed.ncbi.nlm.nih.gov/33872653/) | Complete CARD11 deficiency (p.Arg837\*); CBM/NF-κB/JNK/MALT1 defect; B-cell block; ILD/colitis | Human clinical + mechanistic |
| [26289640](https://pubmed.ncbi.nlm.nih.gov/26289640/) | p.Cys150\*; impaired NF-κB/IL-2; Omenn via somatic reversion | Human clinical |
| [30170123](https://pubmed.ncbi.nlm.nih.gov/30170123/) | CARD11 allelic series (null SCID / GOF BENTA / DN atopy) | Human clinical review |
| [26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/) | CBM-complex heterogeneity; CARD11/BCL10/MALT1 phenocopy; CARD9 distinct; human–mouse concordance | Review |
| [27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/) | HSCT normalizes CBM (MALT1) deficiency — supports curative therapy | Human clinical |
| [24792914](https://pubmed.ncbi.nlm.nih.gov/24792914/) | CARD11/BCL10/MALT1 required for glutamine uptake & mTORC1, IKK-independent | In vitro / mechanistic |
| [28628108](https://pubmed.ncbi.nlm.nih.gov/28628108/) | Glutamine partially rescues mTORC1/IFN-γ in hypomorphic CARD11 disease | Human clinical + mechanistic |
| [19454668](https://pubmed.ncbi.nlm.nih.gov/19454668/) | Card11/CARMA1 KO: thymic Treg checkpoint | Mouse model |
| [23091043](https://pubmed.ncbi.nlm.nih.gov/23091043/) | CARMA1 required for Th17; EAE resistance | Mouse model |
| [31296852](https://pubmed.ncbi.nlm.nih.gov/31296852/) | Structural: autoinhibition + BCL10-templating filaments | Structural / in vitro |
| [20799731](https://pubmed.ncbi.nlm.nih.gov/20799731/) | Closed→open conformational activation of CARD11 | Mechanistic |
| [42466165](https://pubmed.ncbi.nlm.nih.gov/42466165/) | TREC NBS sensitivity relies on lymphopenia; second-tier genetics | Diagnostic methodology |
| [40625738](https://pubmed.ncbi.nlm.nih.gov/40625738/) | CARD11 lineage-restricted expression in hematopoietic/lymphoid tissue | Review |

Evidence spans **human clinical case series, in vitro reconstitution/reporter assays, structural biology, and mouse genetic models**, giving convergent, multi-modal support for the core mechanism and clinical picture.

---

## Limitations and Knowledge Gaps

- **Extreme rarity / small N.** Only a handful of unrelated biallelic-null probands are described; there are **no registry-scale prevalence, penetrance, survival, or QoL data** specific to CARD11-deficiency SCID. Many prognosis statements are extrapolated from the broader CBM/SCID literature.
- **HSCT outcome data are indirect.** Curability is inferred from MALT1 deficiency and general CBM-CID practice ([PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)); large CARD11-specific transplant series are lacking.
- **Genotype–phenotype granularity.** The full spectrum of null alleles, modifier effects, and the frequency of Omenn-via-reversion are not quantified.
- **No disease-specific omics/epigenetic signature** is established for the null SCID form; molecular profiling comes largely from single-patient studies and model systems.
- **Metabolic rescue is allele-dependent.** Glutamine/mTORC1 rescue applies to hypomorphic alleles and is **not expected to benefit complete deficiency** — this should not be over-generalized.
- **Model concordance is partial** ([PMID: 26277595](https://pubmed.ncbi.nlm.nih.gov/26277595/)); mouse phenotypes do not fully reproduce human ILD/colitis.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international CARD11-deficiency registry** to capture genotype, presentation, TREC-NBS results, transplant outcomes, and survival — directly filling the epidemiology/prognosis gaps.
2. **Systematically evaluate second-tier genetic newborn screening** (or KREC + functional add-ons) to catch non-lymphopenic T-cell defects like CARD11 deficiency that TREC screening misses ([PMID: 42466165](https://pubmed.ncbi.nlm.nih.gov/42466165/)).
3. **Report standardized HSCT outcomes** (conditioning, chimerism, immune reconstitution, GVHD, survival) for biallelic-null CARD11 patients to formalize the curative claim.
4. **Deep immunophenotyping / single-cell RNA-seq** of patient lymphocytes to map the B-cell transitional block and Tfh/Treg defects at cell-type resolution and benchmark against BCL10/MALT1 deficiency.
5. **Preclinical HSC gene-correction/gene-therapy studies** — attractive given hematopoietic-restricted, single-gene, LOF biology — as an alternative to allogeneic HSCT for patients lacking matched donors.
6. **Curate the ontology mappings** (MONDO:0014081, OMIM #615206, HGNC:16393, HPO/GO/CL/UBERON/NCIT terms listed above) into the knowledge base with the verified PMID-anchored evidence quotes.

---

*Report compiled from 10 confirmed findings and 42 reviewed papers over a 5-iteration autonomous investigation. All quoted snippets are verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 14 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014081` (3 mentions) - the report calls it "MONDO"; MONDO calls it **severe combined immunodeficiency due to CARD11 deficiency**
- `CL:0002679` (2 mentions) - the report calls it "regulatory T cell"; CL calls it **natural helper lymphocyte**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005435` (obsolete Impaired T cell function) (1 mention) - replaced by `HP:0011840`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0006530` (1 mention) - the report calls it "Interstitial pulmonary abnormality"; HP calls it **Abnormal pulmonary interstitial morphology**, and lists "Interstitial pulmonary disease" among its other names
- `GO:0007249` (1 mention) - the report calls it "I-κB kinase/NF-κB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names