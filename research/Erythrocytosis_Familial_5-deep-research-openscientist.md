---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T18:31:23.513072'
end_time: '2026-10-15T19:00:31.529471'
duration_seconds: 1748.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Erythrocytosis 5
  mondo_id: MONDO:0033483
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 11
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0002315
    reported_labels:
    - Symptom
    ontology_label: Headache
  - term_id: HP:0000989
    reported_labels:
    - Symptom
    ontology_label: Pruritus
  - term_id: HP:0200071
    reported_labels:
    - Clinical sign
    ontology_label: Peripheral vitreoretinal degeneration
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Erythrocytosis_Familial_5-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Erythrocytosis_Familial_5-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Erythrocytosis 5
- **MONDO ID:** MONDO:0033483 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Erythrocytosis 5** covering all of the
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

# Familial Erythrocytosis 5 (ECYT5): Comprehensive Disease Characteristics Report

**Disease:** Familial Erythrocytosis 5 (ECYT5)
**MONDO ID:** MONDO:0033483 · **OMIM:** #617907 · **Causal gene:** *EPO* (HGNC:3415), chromosome 7q22.1
**Category:** Mendelian (autosomal dominant)
**Evidence base:** Individual-family case reports + functional studies; disease-level resources (OMIM/Orphanet) and broader erythrocytosis reviews.

---

## Summary

**Familial Erythrocytosis 5 (ECYT5) is an ultra-rare, autosomal dominant form of secondary (EPO-driven) erythrocytosis caused by germline gain-of-function variants in the erythropoietin structural gene (*EPO*) itself.** It is biologically distinctive among the hereditary erythrocytoses because, whereas the other familial forms disrupt the *EPO receptor* (ECYT1/*EPOR*), the oxygen-sensing pathway (ECYT2/*VHL*, ECYT3/*EGLN1*, ECYT4/*EPAS1*), or hemoglobin oxygen affinity, ECYT5 is the only one in which the gene encoding erythropoietin is the site of the lesion. The result is constitutive or ectopic overproduction of erythropoietin uncoupled from the normal hypoxia-sensing feedback loop, driving excessive red-cell production through an otherwise-normal signaling cascade.

Two mechanistically distinct causal variants are documented. The founding kindred ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)) carried a single-nucleotide frameshift deletion (*EPO* c.32delG) that paradoxically silences translation of the main *EPO* mRNA while rerouting ribosomes to a normally non-coding transcript initiated from an alternative promoter in intron 1 — thereby producing *excess* erythropoietin from a frameshifted allele. A second kindred ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)) carried a promoter variant (*EPO* c.-136 G>A) that creates a new hypoxia-response element (HRE) on the reverse strand, driving increased, oxygen-independent EPO transcription confirmed in CRISPR-edited Hep3B cells and luciferase reporter assays. Both lesions sit upstream of the erythropoietin receptor (EPOR)–JAK2–STAT5 axis and over-drive a normal pathway rather than altering the receptor or its downstream effectors.

Clinically, ECYT5 manifests as lifelong, isolated erythrocytosis (elevated hemoglobin and hematocrit) with inappropriately normal-to-elevated serum EPO and a positive family history, but without the leukocytosis, thrombocytosis, or splenomegaly of polycythemia vera (PV). The principal risks arise from hyperviscosity and thrombosis. Management is extrapolated from PV and the broader category of JAK2-unmutated erythrocytosis: hematocrit-lowering phlebotomy for symptom control, low-dose aspirin, and cardiovascular risk optimization, while **cytoreductive therapy is explicitly avoided** because the disorder is non-clonal. Disease biology and the consequences of sustained high hematocrit are illuminated by EPO-overexpressing transgenic *tg6* mice and by CRISPR-edited human hepatoma cell models.

---

## Key Findings

### Finding 1 — ECYT5 is an autosomal dominant erythrocytosis caused by a gain-of-function *EPO* mutation

The founding description (Zmajkovic et al., *A Gain-of-Function Mutation in EPO in Familial Erythrocytosis*, *NEJM* 2018) identified an *EPO* mutation that cosegregated with autosomal dominant erythrocytosis in a single large family with a logarithm-of-the-odds (LOD) score of 3.3 — statistically significant genetic linkage. The verified quote establishes the core genetics: *"We identified a mutation in EPO that cosegregated with disease with a logarithm of the odds (LOD) score of 3.3 in a family with autosomal dominant erythrocytosis. This mutation, a single-nucleotide deletion (c.32delG), introduces a frameshift in exon 2"* ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)). This defines the gene (*EPO*, HGNC:3415, chromosome 7q22.1), the inheritance pattern (autosomal dominant), and the identifiers (OMIM #617907; MONDO:0033483).

### Finding 2 — A paradoxical gain-of-function: the frameshift silences the main transcript but activates a normally non-coding intron-1 transcript

The most counterintuitive feature of c.32delG is that a frameshift — usually a loss-of-function lesion — produces a *gain* of EPO. Per Zmajkovic et al., the deletion *"introduces a frameshift in exon 2 that interrupts translation of the main EPO messenger RNA (mRNA) transcript but initiates excess production of erythropoietin from what is normally a noncoding EPO mRNA transcribed from an alternative promoter located in intron 1"* ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)). The frameshift unmasks an alternative, intron-1–driven transcript whose translation yields functional erythropoietin in excess — explaining how a single-base coding deletion produces a secondary (high-EPO) rather than primary erythrocytosis.

### Finding 3 — A second, promoter-based mechanism: *EPO* c.-136 G>A creates a new hypoxia-response element

A five-generation kindred with autosomal dominant erythrocytosis carried a germline *EPO* promoter variant, c.-136 G>A (Lanikova et al., 2026). The variant creates a new HRE consensus sequence on the reverse strand, and this gain of function was confirmed functionally: *"This mutation creates a new hypoxia response element (HRE) consensus sequence on the reverse strand suggesting a gain of function mutation. CRISPR/Cas9-edited Hep3B cells harboring the c.-136 G>A variant had increased EPO mRNA and protein expression under both normoxic and hypoxic conditions compared to wild-type cells"* ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)). Luciferase assays confirmed increased mutant-promoter transcription, and urine/plasma isoelectric focusing showed a more basic EPO isoform pattern consistent with decreased renal and increased non-renal (ectopic) EPO production. This establishes a *second, independent* route to ECYT5 — a cis-regulatory promoter variant — broadening the mutational spectrum.

### Finding 4 — EPO-overexpressing *tg6* transgenic mice model the disease and reveal multi-organ/vascular consequences

The *tg6* mouse constitutively overexpresses human EPO in a hypoxia-independent manner — directly paralleling the oxygen-uncoupled EPO excess of ECYT5 — reaching hematocrit up to 0.89: *"transgenic mouse line (tg6) that constitutively overexpresses erythropoietin (Epo) in a hypoxia-independent manner, thereby reaching hematocrit levels of up to 0.89"* ([PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/)). Chronic excessive erythrocytosis caused hepatic, renal, neuronal, and muscular degeneration and reduced lifespan ([PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/)); endothelial activation and damage with reduced brain-vessel density ([PMID: 16254128](https://pubmed.ncbi.nlm.nih.gov/16254128/)); near-abolition of the endothelial glycocalyx (wild-type 0.52 µm vs *tg6* 0.13 µm; P < 0.001) ([PMID: 21859826](https://pubmed.ncbi.nlm.nih.gov/21859826/)); and pregnancy loss from impaired uterine arteriogenesis rescued by lowering hematocrit: *"pregnant human erythropoietin-overexpressing (plasma levels elevated 12-fold) mice (termed tg6 mice) suffering from excessive erythrocytosis generally abort at midgestation unless their hematocrit of 0.85 is drastically lowered"* ([PMID: 18256329](https://pubmed.ncbi.nlm.nih.gov/18256329/)). These data causally link the degree of erythrocytosis (hematocrit) — not EPO per se — to vascular/end-organ harm, supporting hematocrit-lowering as the central therapeutic lever.

### Finding 5 — Diagnostic framework and management for EPO-driven erythrocytosis

The diagnostic approach begins by excluding PV: *"Foremost in the evaluation of erythrocytosis is the exclusion of PV through JAK2 (inclusive of exons 12-15) mutation screening"* (Gangat/Szuber/Tefferi, 2023; [PMID: 36966432](https://pubmed.ncbi.nlm.nih.gov/36966432/)). Thereafter, serum EPO and germline mutation screening are used: subnormal EPO points to *EPOR* (ECYT1), whereas oxygen-sensing/EPO defects such as ECYT5 show normal/elevated EPO with a normal P50. High-oxygen-affinity hemoglobins (left-shifted P50) are a key differential ([PMID: 21511372](https://pubmed.ncbi.nlm.nih.gov/21511372/); [PMID: 33456185](https://pubmed.ncbi.nlm.nih.gov/33456185/)). Management targets are borrowed from PV data — maintain hematocrit <45% via phlebotomy: *"received only phlebotomy (PHL) or HU to maintain the hematocrit level < 45%"* ([PMID: 28699191](https://pubmed.ncbi.nlm.nih.gov/28699191/)).

### Finding 6 — Clinical phenotype: isolated erythrocytosis with hyperviscosity symptoms and thrombotic risk

ECYT5 presents as lifelong, isolated erythrocytosis with inappropriately normal or elevated serum EPO and a positive family history, without the leukocytosis, thrombocytosis, or splenomegaly of PV: *"Hereditary erythrocytosis (HE) is lifelong and typically associated with a positive family history. Subnormal serum erythropoietin (EPO) suggests an EPO receptor mutation"* ([PMID: 41347984](https://pubmed.ncbi.nlm.nih.gov/41347984/)) — with ECYT5 falling into the normal/high EPO category. Hyperviscosity manifestations shared by erythrocytosis states include headache, visual disturbances, pruritus, and erythromelalgia; splenomegaly is PV-specific: *"Polycythemia vera is characterized by headache, visual disturbances, pruritus, erythromelalgia and splenomegaly"* ([PMID: 42557631](https://pubmed.ncbi.nlm.nih.gov/42557631/)). In the original kindred, c.32delG cosegregated with the phenotype (LOD 3.3; [PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)).

### Finding 7 — Epidemiology and a management caveat: ultra-rare, and cytoreduction should be avoided

JAK2-unmutated erythrocytosis has a reported incidence of 0.13%–4.1% (*"Incidence has been reported to be between 0.13% and 4.1%"*; [PMID: 41347984](https://pubmed.ncbi.nlm.nih.gov/41347984/)), but ECYT5 specifically is vanishingly rare — a handful of families worldwide ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/); [PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)). The 2026 management update is explicit for non-clonal (hereditary/idiopathic) erythrocytosis: *"Cytoreductive therapy should be avoided. Phlebotomy should be considered for symptom control. Cardiovascular risk optimization and low-dose aspirin are advised"* ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)).

### Finding 8 — The EPO signaling causal chain

Physiologically, HIF-2 regulates EPO synthesis in response to hypoxia: *"HIF-2 has emerged as the transcription factor that regulates EPO synthesis in the kidney and liver"* (Haase, 2013; [PMID: 23291219](https://pubmed.ncbi.nlm.nih.gov/23291219/)). EPO then binds EPOR on erythroid progenitors, activating JAK2 and downstream STAT5, PI3K/AKT, and MAPK, which inhibit apoptosis and promote erythroid proliferation/differentiation: *"EPO activates the JAK2-STAT5 pathway, and two tyrosine residues (Y343, Y401) in the cytoplasmic domain of EPOR are important for STAT5 activation"* ([PMID: 9664155](https://pubmed.ncbi.nlm.nih.gov/9664155/)). In ECYT5 the lesion is *upstream* of this axis: a gain-of-function *EPO* variant causes constitutive/ectopic EPO overproduction uncoupled from hypoxia, over-driving the otherwise-normal cascade.

---

## Report by Research Section

### 1. Disease Information

ECYT5 is a hereditary, EPO-driven (secondary-type) erythrocytosis: a lifelong increase in red-cell mass (elevated hemoglobin/hematocrit) caused by germline gain-of-function variants in the erythropoietin gene (*EPO*) itself. It is the fifth-defined familial erythrocytosis locus and the only one in which the *EPO* structural gene is mutated, as opposed to its upstream oxygen-sensing regulators (*VHL*/ECYT2, *EGLN1*/ECYT3, *EPAS1*/ECYT4) or its receptor (*EPOR*/ECYT1) ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)).

**Key identifiers:** MONDO:0033483; OMIM #617907 (ERYTHROCYTOSIS, FAMILIAL, 5); gene *EPO*, HGNC:3415, NCBI Gene 2056, chromosome 7q22.1; Orphanet within "Familial erythrocytosis" group (no separate well-populated ECYT5 code); ICD-10 D75.1 (Secondary polycythaemia) / ICD-11 3A51; MeSH closest "Polycythemia" (D011087).

**Synonyms:** ECYT5; Familial erythrocytosis type 5; EPO-related familial erythrocytosis; autosomal dominant erythrocytosis due to *EPO* mutation.

**Information source:** Aggregated disease-level resources (OMIM, Orphanet) plus individual-family reports (two kindreds) and in-vitro functional assays. Not EHR-derived.

### 2. Etiology

**Primary cause — genetic.** ECYT5 is monogenic: a heterozygous gain-of-function germline *EPO* variant causes inappropriate EPO overproduction uncoupled from oxygen-sensing feedback. Two causal variants are documented: (1) **c.32delG** (exon-2 frameshift), cosegregating with disease at LOD 3.3 ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)); (2) **c.-136 G>A** (promoter variant creating a novel HRE) ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)).

- **Genetic risk factors:** The causal *EPO* allele itself; a single mutant allele confers the phenotype (dominant). No susceptibility loci or modifier genes established.
- **Environmental risk factors:** None causal. Exogenous drivers of red-cell mass (altitude/chronic hypoxia, smoking/CO, androgens, SGLT2 inhibitors, ESAs) could additively worsen hematocrit (inferred; [PMID: 42557631](https://pubmed.ncbi.nlm.nih.gov/42557631/), [PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)).
- **Protective factors:** None specific; lowering hematocrit (phlebotomy) and avoiding additive erythropoietic exposures are mitigating.
- **Gene–environment interactions:** Plausible additive effect of hypoxia/erythropoietic drugs on the genetically elevated baseline (inferred, not formally studied in ECYT5).

### 3. Phenotypes

ECYT5 is fundamentally a laboratory-defined phenotype; clinical symptoms, when present, arise from hyperviscosity and attendant thrombotic risk.

| Phenotype | Type | HPO term | Onset / course | Frequency |
|---|---|---|---|---|
| Erythrocytosis/polycythemia (↑RBC mass) | Lab abnormality | HP:0001901 (Polycythemia) | Lifelong, early, stable | Obligate (defining) |
| Elevated hemoglobin/hematocrit | Lab abnormality | HP:0001899 (Increased hematocrit) / HP:0001900 | Lifelong | Obligate |
| Increased serum EPO (inappropriately normal/high) | Lab abnormality | HP:0020059 (Increased circulating EPO) | Lifelong | Characteristic |
| Headache | Symptom | HP:0002315 | Episodic, with high Hct | Variable |
| Pruritus | Symptom | HP:0000989 | Variable | Occasional |
| Erythromelalgia | Clinical sign | HP:0200071 | Episodic | Occasional |
| Plethora / facial redness | Physical sign | HP:0001050 (Plethora) | Chronic | Variable |
| Visual disturbance / dizziness | Symptom | HP:0000504 / HP:0002321 | Episodic | Variable |
| Thrombosis (arterial/venous) | Clinical complication | HP:0001907 (Thromboembolism) | Event-driven, adult | Risk; undefined for ECYT5 |

Symptom source: hyperviscosity complex shared across erythrocytosis ([PMID: 42557631](https://pubmed.ncbi.nlm.nih.gov/42557631/)); unlike PV, ECYT5 shows no splenomegaly, leukocytosis, or thrombocytosis ([PMID: 41347984](https://pubmed.ncbi.nlm.nih.gov/41347984/)). **Severity/progression:** generally mild–moderate, chronic, non-progressive; variable between individuals. **Quality-of-life impact:** not formally measured (no EQ-5D/SF-36 data for ECYT5); driven mainly by thrombotic events and recurrent phlebotomy.

### 4. Genetic / Molecular Information

**Causal gene:** *EPO* (HGNC:3415; OMIM *133170; chr 7q22.1; UniProt P01588).

**Pathogenic variants (germline, heterozygous, AD):**
- **c.32delG** — exon-2 frameshift; paradoxical gain of function in EPO output via an intron-1 alternative transcript ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)).
- **c.-136 G>A** — promoter/regulatory variant; gain of function via novel HRE ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)).
- Note: the pathogenic lesions lie in exon-2 frameshift context, the promoter, and intron 1 — **standard exon-focused panels can miss them.**

**Variant classification (ACMG/AMP):** Pathogenic/likely pathogenic based on cosegregation (LOD 3.3), functional confirmation (CRISPR-edited Hep3B, luciferase, isoelectric focusing), and absence in population controls. **Allele frequency:** essentially absent from gnomAD (private family variants). **Origin:** germline. **Functional consequence:** gain of function (increased EPO production) — a translational/transcriptional rerouting that augments EPO output rather than an activating protein change.

**Modifier genes:** none established. **Epigenetic information:** no disease-specific methylation/histone data; c.-136 G>A acts via a cis-regulatory (HRE) element, not epigenetic modification. **Chromosomal abnormalities:** none — ECYT5 is a point/indel disorder.

### 5. Environmental Information

- **Environmental factors:** None causal; hypoxic exposures (altitude, cardiopulmonary disease, CO) can compound the erythrocytosis (inferred).
- **Lifestyle factors:** Smoking, androgen/anabolic-steroid use, testosterone therapy, SGLT2 inhibitors, and ESAs independently raise hematocrit and would aggravate ECYT5 ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/), [PMID: 42557631](https://pubmed.ncbi.nlm.nih.gov/42557631/)).
- **Infectious agents:** Not applicable.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A germline **gain-of-function *EPO* variant** (c.32delG frameshift **or** c.-136 G>A promoter HRE) is present in EPO-producing cells. *(demonstrated: linkage + functional assays)*
2. **Frameshift branch (c.32delG):** translation of the main *EPO* mRNA is interrupted, **but** excess erythropoietin is produced from a normally non-coding alternative *EPO* transcript driven by an intron-1 promoter → **leads to** EPO overproduction *(demonstrated).* **Promoter branch (c.-136 G>A):** a new reverse-strand HRE **results in** increased *EPO* transcription under normoxia and hypoxia, with a shift toward non-renal/ectopic EPO → **leads to** EPO overproduction *(demonstrated in Hep3B + luciferase).*
3. Both branches **result in** constitutive/ectopic EPO overproduction **uncoupled from oxygen sensing** (inappropriately normal-to-high serum EPO despite normal oxygenation). *(demonstrated clinically)*
4. Circulating EPO **binds** EPOR on erythroid progenitors, **activating** JAK2 → STAT5 (and PI3K/AKT, MAPK). *(inferred from canonical EPO biology; [PMID: 9664155](https://pubmed.ncbi.nlm.nih.gov/9664155/))*
5. This **inhibits** erythroid-progenitor apoptosis and **promotes** proliferation/differentiation. *(demonstrated in EPO biology)*
6. Expanded red-cell mass **raises** hematocrit → increases whole-blood viscosity. *(demonstrated)*
7. Hyperviscosity **leads to** impaired microcirculation, endothelial activation, and increased thrombotic risk plus hyperviscosity symptoms; at extreme Hct it **causes** endothelial/glycocalyx damage and multi-organ degeneration (tg6 mice; [PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/), [PMID: 16254128](https://pubmed.ncbi.nlm.nih.gov/16254128/), [PMID: 21859826](https://pubmed.ncbi.nlm.nih.gov/21859826/)). *(model-organism evidence + clinical inference)*

**Detail by category.** *Molecular pathways:* EPO–EPOR–JAK2–STAT5 (primary), PI3K/AKT and RAS–MAPK (secondary) ([PMID: 9664155](https://pubmed.ncbi.nlm.nih.gov/9664155/)); the upstream physiologic regulator normally dysregulated is HIF-2/EPAS1, controlling renal/hepatic EPO synthesis ([PMID: 23291219](https://pubmed.ncbi.nlm.nih.gov/23291219/)). *Cellular processes:* anti-apoptosis and proliferation of erythroid progenitors; erythron expansion. *Protein dysfunction:* not altered EPO structure — the defect is excess production of functional EPO (gain of function in dosage/expression); isoelectric focusing shows a more basic, non-renal-type EPO isoform in the promoter-variant family ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)). *Metabolic/biochemical:* secondary to erythrocytosis (↑iron utilization, possible phlebotomy-induced iron deficiency; altered 2,3-BPG/oxygen delivery in models, [PMID: 17365666](https://pubmed.ncbi.nlm.nih.gov/17365666/)). *Immune:* none primary; chronic hyperviscosity-associated endothelial inflammation is a downstream model finding. *Tissue-damage:* hyperviscosity, endothelial activation, reduced glycocalyx, impaired arteriogenesis (model organism; [PMID: 18256329](https://pubmed.ncbi.nlm.nih.gov/18256329/), [PMID: 21859826](https://pubmed.ncbi.nlm.nih.gov/21859826/)). **Ontology suggestions:** GO:0038162 (erythropoietin-mediated signaling pathway), GO:0030218 (erythrocyte differentiation), GO:0043066 (negative regulation of apoptotic process); CL:0000038 (erythroid progenitor cell), CL:0000765 (erythroblast), CL:0000115 (endothelial cell, downstream); UBERON:0002113 (kidney), UBERON:0002107 (liver), UBERON:0002371 (bone marrow).

### 7. Anatomical Structures Affected

- **Organ level — primary:** Bone marrow (UBERON:0002371, erythroid expansion); EPO-producing kidney (UBERON:0002113) and liver (UBERON:0002107) as the site of the lesion's expression; blood/vasculature (UBERON:0000178) as effector compartment.
- **Secondary/complication organs:** Cerebral and coronary vasculature, splanchnic/portal veins (thrombosis sites); in models, liver, kidney, brain, peripheral nerve, and skeletal muscle degenerate under extreme Hct ([PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/)).
- **Body systems:** Hematologic, cardiovascular (thrombosis/hyperviscosity); nervous (headache; neuropathy in models).
- **Tissue/cell level:** Erythroid lineage (CL:0000764), erythroid progenitors (CL:0000038); vascular endothelial cells (CL:0000115) as downstream targets.
- **Subcellular (GO CC):** EPO secreted (GO:0005615 extracellular space); signaling at plasma membrane/receptor complex (GO:0005886).
- **Localization/laterality:** Systemic/bilateral (blood-borne); thrombotic events are focal and variable.

### 8. Temporal Development

- **Onset:** Congenital/early-life predisposition; lifelong erythrocytosis typically detected in childhood–adulthood ([PMID: 41347984](https://pubmed.ncbi.nlm.nih.gov/41347984/)); chronic/insidious pattern.
- **Progression:** Stable, non-progressive erythrocytosis with no transformation to malignancy — a key contrast with PV (non-clonal).
- **Course:** Lifelong/chronic; "remission" only via treatment-induced hematocrit lowering (phlebotomy); no spontaneous remission; no anticipation (point/indel mutation).
- **Critical periods:** Pregnancy (hyperviscosity risk; model shows hematocrit-dependent pregnancy loss, [PMID: 18256329](https://pubmed.ncbi.nlm.nih.gov/18256329/)) and perioperative/immobilization windows for thrombosis.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant (single heterozygous *EPO* gain-of-function allele; cosegregation LOD 3.3; [PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)).
- **Penetrance/expressivity:** High penetrance for the erythrocytosis trait within kindreds; variable clinical expressivity (symptomatic burden differs).
- **Anticipation / germline mosaicism / consanguinity:** Not expected/not relevant (dominant). **Founder effects:** none — private family variants.
- **Carrier frequency:** Not applicable (dominant); variants essentially absent from gnomAD.
- **Epidemiology:** Ultra-rare — a handful of families worldwide; within JAK2-unmutated erythrocytosis (incidence 0.13%–4.1%, [PMID: 41347984](https://pubmed.ncbi.nlm.nih.gov/41347984/)), but a vanishingly small subset. No ECYT5-specific prevalence/incidence figures exist.
- **Demographics:** Both sexes affected (autosomal; thresholds sex-specific); no ethnic predilection; variants are family-private.

### 10. Diagnostics

**Diagnostic algorithm** ([PMID: 41347984](https://pubmed.ncbi.nlm.nih.gov/41347984/), [PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/), [PMID: 36966432](https://pubmed.ncbi.nlm.nih.gov/36966432/)):
1. Confirm true erythrocytosis (↑Hgb/Hct vs age/sex thresholds; exclude relative/apparent polycythemia). LOINC: hemoglobin 718-7; hematocrit 4544-3; erythropoietin 14743-9.
2. **Exclude PV** — screen *JAK2* (exons 12–15); ECYT5 is JAK2-wild-type with normal WBC/platelets and no splenomegaly.
3. **Serum EPO:** inappropriately normal or elevated in ECYT5 (contrast: subnormal → EPOR mutation/PV).
4. **P50:** normal in ECYT5 (contrast: low/left-shifted → high-oxygen-affinity hemoglobin; [PMID: 21511372](https://pubmed.ncbi.nlm.nih.gov/21511372/), [PMID: 33456185](https://pubmed.ncbi.nlm.nih.gov/33456185/)).
5. **Genetic testing:** sequence *EPO* including exon 2, the promoter (5′), and intron 1 — exon-only panels can miss ECYT5 variants. Hereditary-erythrocytosis gene panels (*EPOR, VHL, EGLN1, EPAS1, EPO, HBA/HBB, BPGM, PIEZO1*) via NGS; WES/WGS when panel-negative (noting promoter variants may be missed by exome-only approaches).

**Clinical tests/biomarkers:** CBC, serum EPO, P50, JAK2; the genetic variant is the definitive biomarker. Isoelectric focusing of urine/plasma EPO can reveal a non-renal isoform pattern ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)). Bone marrow biopsy not required (no clonal myeloproliferation). **Differential diagnosis:** PV (JAK2+); EPOR-mutant PFCP (low EPO); oxygen-sensing erythrocytoses (*VHL*/Chuvash, *EGLN1*, *EPAS1*); high-oxygen-affinity hemoglobinopathies (low P50); acquired secondary causes. **Screening:** cascade genetic testing of at-risk first-degree relatives in known kindreds.

### 11. Outcome / Prognosis

- **Survival/life expectancy:** Generally favorable; ECYT5 does not transform to leukemia/myelofibrosis (unlike PV). No ECYT5-specific survival statistics.
- **Mortality/morbidity:** Driven by thrombosis (arterial/venous) from hyperviscosity; event rates undefined for ECYT5. Models under extreme Hct show reduced lifespan and multi-organ damage ([PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/)).
- **Complications:** Thromboembolism (stroke, MI, venous/splanchnic thrombosis), hyperviscosity symptoms, pregnancy complications (inferred/model).
- **Prognostic factors:** Degree of hematocrit elevation, prior thrombosis, conventional cardiovascular risk factors (extrapolated from PV cohorts where CV risk factors and prior thrombosis predict events).
- **Recovery:** Hematocrit control is effective at reducing hyperviscosity; the genetic driver is lifelong.

### 12. Treatment

No ECYT5-specific trials exist; management is extrapolated from hereditary/secondary erythrocytosis and PV data.

- **Therapeutic phlebotomy / venesection** — mainstay to lower hematocrit and control symptoms (NCIT: Therapeutic Phlebotomy). Target historically <45% (from PV; [PMID: 28699191](https://pubmed.ncbi.nlm.nih.gov/28699191/)), individualized for secondary erythrocytosis ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)).
- **Low-dose aspirin** — antiplatelet thromboprophylaxis: *"Cardiovascular risk optimization and low-dose aspirin are advised"* ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)) (NCIT: Aspirin, C287).
- **Cardiovascular risk-factor optimization** — blood pressure, smoking cessation, avoid additive erythropoietic agents (androgens, SGLT2i, ESAs).
- **Cytoreduction (hydroxyurea) — generally AVOIDED** in non-clonal hereditary erythrocytosis: *"Cytoreductive therapy should be avoided"* ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)) (NCIT: Hydroxyurea, C546).
- **Experimental/targeted:** Role of HIF-2α inhibitors remains unclear for hereditary erythrocytosis ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)); no gene/cell/RNA therapy exists. **Pharmacogenomics:** none established.
- **Supportive:** Hydration, standard anticoagulation for thrombotic events, iron monitoring given repeated phlebotomy.

### 13. Prevention

- **Primary prevention:** Not possible (germline). Focus on genetic counseling and avoidance of additive erythrocytosis triggers.
- **Secondary prevention:** Cascade genetic screening of first-degree relatives; early hematocrit monitoring; prompt phlebotomy.
- **Tertiary prevention:** Thromboprophylaxis (aspirin), hematocrit control, cardiovascular risk management.
- **Genetic counseling:** Autosomal dominant → 50% transmission risk; prenatal/preimplantation testing technically feasible for a known family variant but rarely pursued given the generally manageable course.
- **Immunization / public-health / environmental:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *EPO* is conserved across mammals. Mouse *Epo* (NCBI Gene 13856), rat *Epo* (NCBI Gene 24335). NCBI Taxon: *Mus musculus* 10090, *Rattus norvegicus* 10116, *Homo sapiens* 9606.
- **Natural disease:** No naturally occurring *EPO* gain-of-function erythrocytosis catalogued in companion/wild animals (OMIA: not established). No breed-associated *EPO* variants (no VBO entry).
- **Comparative biology:** The EPO–EPOR–JAK2–STAT5 axis and HIF-mediated EPO regulation are highly evolutionarily conserved ([PMID: 23291219](https://pubmed.ncbi.nlm.nih.gov/23291219/)), underpinning rodent-model validity.
- **Transmission/zoonosis:** Not applicable (non-infectious genetic disease).

### 15. Model Organisms

- **Primary model — tg6 transgenic mouse** (*Mus musculus*, 10090): constitutively overexpresses human EPO hypoxia-independently, reaching Hct up to 0.89 ([PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/)), mimicking the ECYT5 principle (oxygen-uncoupled EPO excess → erythrocytosis).
  - **Phenotype recapitulation:** Strong for the *consequences* of EPO-driven erythrocytosis — hyperviscosity, endothelial activation and glycocalyx loss ([PMID: 21859826](https://pubmed.ncbi.nlm.nih.gov/21859826/)), reduced brain-vessel density/BBB changes ([PMID: 16254128](https://pubmed.ncbi.nlm.nih.gov/16254128/)), multi-organ (hepatic/renal/neuronal/muscular) degeneration and reduced lifespan ([PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/)), and hematocrit-dependent pregnancy loss reversible by lowering Hct ([PMID: 18256329](https://pubmed.ncbi.nlm.nih.gov/18256329/)).
  - **Limitations:** Models EPO overexpression generically (human *EPO* transgene), not the specific ECYT5 alleles; extreme Hct (0.85–0.89) exceeds typical human ECYT5 levels, exaggerating organ pathology.
- **Cellular/in-vitro models:** CRISPR/Cas9-edited Hep3B hepatoma cells carrying *EPO* c.-136 G>A (increased EPO mRNA/protein under normoxia and hypoxia) and luciferase promoter-reporter assays confirming transcriptional gain of function ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)); the frameshift-driven alternative-transcript mechanism was demonstrated in cellular expression systems ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)).
- **Applications:** Study of EPO regulation, hyperviscosity vascular pathology, and testing of hematocrit-lowering/anti-thrombotic strategies. **Resources:** MGI (*Epo*), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
            ┌────────────────────────────────────────────────────────────┐
            │  Germline gain-of-function EPO variant (7q22.1, AD)         │
            └───────────────┬───────────────────────────┬─────────────────┘
                            │                           │
          Branch A: c.32delG (exon-2 frameshift)   Branch B: c.-136 G>A (promoter)
          silences main EPO mRNA; activates        creates new reverse-strand HRE;
          non-coding intron-1 transcript →          ↑EPO transcription (normoxia &
          EXCESS EPO protein                         hypoxia); shift to non-renal EPO
                            │                           │
                            └─────────────┬─────────────┘
                                          ▼
                 Oxygen-UNCOUPLED erythropoietin overproduction
                     (bypasses normal HIF-2 feedback loop)
                                          ▼
                 EPO binds EPOR on erythroid progenitors (bone marrow)
                                          ▼
                 JAK2 activation → STAT5 (+ PI3K/AKT, MAPK)
                                          ▼
                 ↓ apoptosis, ↑ proliferation/differentiation of erythroid cells
                                          ▼
                 ↑ Red-cell mass  →  ↑ Hematocrit / Hemoglobin
                                          ▼
                 ↑ Blood viscosity → hyperviscosity symptoms + THROMBOSIS risk
                 (+ endothelial/glycocalyx damage at extreme Hct — tg6 evidence)
```

**ECYT5 vs other familial erythrocytoses (differential-diagnostic context):**

| Type | Gene | Mechanism | Serum EPO | P50 |
|---|---|---|---|---|
| **ECYT5** | ***EPO*** | **GoF EPO overproduction (ligand excess)** | **Normal/high** | **Normal** |
| ECYT1 | *EPOR* | GoF truncated receptor (EPO hypersensitivity) | Low/subnormal | Normal |
| ECYT2 | *VHL* | LoF → HIF stabilization → ↑EPO | Normal/high | Normal |
| ECYT3 | *EGLN1/PHD2* | LoF → HIF stabilization → ↑EPO | Normal/high | Normal |
| ECYT4 | *EPAS1/HIF2A* | GoF → ↑EPO | Normal/high | Normal |
| High-affinity Hb | globin genes | ↑O₂ affinity → tissue hypoxia → ↑EPO | Normal/high | **Low (left-shift)** |

**Unifying interpretation:** ECYT5 is a "ligand-excess" secondary erythrocytosis in which the *EPO* gene itself is the driver. The signaling machinery (EPOR–JAK2–STAT5) is intact and normal; it is simply over-stimulated. This explains the clinical picture (isolated erythrocytosis with normal/high EPO, no cytopenias, no splenomegaly, no clonal transformation) and dictates management (hematocrit control, not cytoreduction).

---

## Evidence Base

| PMID | Role | How it supports/challenges findings |
|---|---|---|
| [29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/) | Founding ECYT5 description | *EPO* c.32delG, AD inheritance, LOD 3.3, paradoxical intron-1 transcript mechanism (F1, F2) |
| [41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/) | Second causal mechanism | *EPO* c.-136 G>A promoter HRE; functional confirmation in Hep3B + luciferase (F3) |
| [16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/) | Model organism | *tg6* mouse, hypoxia-independent EPO overexpression, Hct up to 0.89, multi-organ degeneration (F4) |
| [18256329](https://pubmed.ncbi.nlm.nih.gov/18256329/) | Model organism | Hematocrit-dependent pregnancy loss reversible by lowering Hct (F4; management rationale) |
| [16254128](https://pubmed.ncbi.nlm.nih.gov/16254128/) | Model organism | Endothelial activation/damage, reduced brain-vessel density (F4) |
| [21859826](https://pubmed.ncbi.nlm.nih.gov/21859826/) | Model organism | Glycocalyx near-abolished (0.52→0.13 µm, P<0.001) at high Hct (F4) |
| [36966432](https://pubmed.ncbi.nlm.nih.gov/36966432/) | Diagnostic framework | JAK2 exclusion as first step; EPO-based workup (F5) |
| [28699191](https://pubmed.ncbi.nlm.nih.gov/28699191/) | Management target | Hematocrit <45% via phlebotomy/HU (F5) |
| [41347984](https://pubmed.ncbi.nlm.nih.gov/41347984/) | Phenotype & epidemiology | Lifelong familial HE; EPO level distinguishes EPOR; incidence 0.13–4.1% (F6, F7) |
| [42557631](https://pubmed.ncbi.nlm.nih.gov/42557631/) | Phenotype | Hyperviscosity symptom complex; splenomegaly PV-specific (F6) |
| [41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/) | Management (2026) | Avoid cytoreduction; phlebotomy + aspirin + CV risk optimization (F7) |
| [23291219](https://pubmed.ncbi.nlm.nih.gov/23291219/) | Normal physiology | HIF-2 regulates kidney/liver EPO synthesis — the circuit ECYT5 bypasses (F8) |
| [9664155](https://pubmed.ncbi.nlm.nih.gov/9664155/) | Downstream signaling | EPO→JAK2-STAT5; EPOR Y343/Y401 (F8) |
| [21511372](https://pubmed.ncbi.nlm.nih.gov/21511372/), [33456185](https://pubmed.ncbi.nlm.nih.gov/33456185/) | Differential diagnosis | High-O₂-affinity Hb, left-shifted P50 (Section 10) |

Evidence source types: **human clinical/genetic** (29514032, 41574959, 36966432, 41347984, 41123216, 42557631, 28699191, 21511372, 33456185); **model organism** (16690772, 18256329, 16254128, 21859826); **molecular/in-vitro + review** (9664155, 23291219, plus the Hep3B/luciferase work within 41574959).

---

## Supported vs. Refuted Hypotheses

**Supported:**
- ECYT5 is an autosomal dominant erythrocytosis caused by gain-of-function *EPO* variants ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)).
- The c.32delG mechanism is a paradoxical gain of function via an intron-1 alternative transcript ([PMID: 29514032](https://pubmed.ncbi.nlm.nih.gov/29514032/)).
- A promoter variant (c.-136 G>A) creating a new HRE is a second causal mechanism ([PMID: 41574959](https://pubmed.ncbi.nlm.nih.gov/41574959/)).
- Pathology downstream of EPO excess is hyperviscosity/endothelial, demonstrated in tg6 mice ([PMID: 16690772](https://pubmed.ncbi.nlm.nih.gov/16690772/), [PMID: 16254128](https://pubmed.ncbi.nlm.nih.gov/16254128/), [PMID: 21859826](https://pubmed.ncbi.nlm.nih.gov/21859826/), [PMID: 18256329](https://pubmed.ncbi.nlm.nih.gov/18256329/)).

**Refuted / excluded:**
- ECYT5 is **not** a JAK2-mutated myeloproliferative neoplasm (no clonal transformation).
- It is **not** caused by altered EPO protein structure or by oxygen-sensing-pathway genes (those define ECYT2–4).
- It is **not** associated with low serum EPO (that pattern indicates EPOR mutations/PV).

---

## Limitations and Knowledge Gaps

- **Extreme rarity:** ECYT5 rests on essentially two reported kindreds (c.32delG and c.-136 G>A). No cohort-level data exist on penetrance, expressivity, long-term thrombotic rates, survival, or quality of life specific to ECYT5; prognosis and management are extrapolated from PV and the broader JAK2-unmutated category.
- **Extrapolated management:** The hematocrit <45% target and aspirin recommendation derive from PV/erythrocytosis data, not ECYT5-specific trials. No randomized evidence exists for this ultra-rare entity.
- **Model fidelity:** The *tg6* mouse reaches more extreme hematocrit (0.85–0.89) than typical human ECYT5 and overexpresses EPO via a transgene rather than the specific human regulatory lesions, potentially overstating human risk. The Hep3B model addresses transcription but not systemic physiology.
- **Variant ascertainment:** The promoter variant (c.-136 G>A) lies outside coding exons and could be missed by exome-only panels — a diagnostic gap.
- **Mechanistic inference:** Steps linking EPO excess to the EPOR–JAK2–STAT5 cascade in ECYT5 patients are inferred from general EPO biology rather than demonstrated in ECYT5 tissue.
- **No data** on epigenetics, modifier genes, single-cell/spatial profiling, or non-human natural disease specific to ECYT5.

---

## Proposed Follow-up Experiments / Actions

1. **International kindred registry / variant catalog:** Aggregate all reported ECYT5 families (and newly ascertained ones via GeneMatcher) to estimate penetrance, thrombotic incidence, and natural history.
2. **Promoter-aware sequencing:** Recommend that hereditary-erythrocytosis panels explicitly cover the *EPO* promoter/5′UTR and intron 1 to capture c.-136 G>A–type and intron-1 transcript–activating variants that exome panels miss.
3. **Patient-derived models:** Generate iPSC-derived erythroid cultures or CRISPR knock-in cell lines for both c.32delG and c.-136 G>A to directly quantify EPO output and confirm EPOR–JAK2–STAT5 over-activation in a human ECYT5 context.
4. **Transcript-level validation:** Use targeted long-read RNA-seq in c.32delG carriers to confirm and quantify the intron-1–driven EPO transcript and its translation product in vivo.
5. **Thrombosis-risk and management study:** Prospectively monitor hematocrit, thrombotic events, and outcomes under phlebotomy ± low-dose aspirin in known carriers to generate ECYT5-specific (rather than PV-extrapolated) management evidence.
6. **Pregnancy-management guidance:** Given the *tg6* reproductive data, develop hematocrit-control protocols for pregnant ECYT5 patients and document uteroplacental outcomes.
7. **Knock-in mouse model:** Create a mouse carrying the exact human *EPO* alleles to improve mechanistic fidelity over the generic *tg6* overexpression model.

---

*Report compiled from 8 confirmed findings and 38 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are anchored to the cited PMIDs with verified abstract quotes.*


## Artifacts

- [OpenScientist final report](Erythrocytosis_Familial_5-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Erythrocytosis_Familial_5-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002315` (1 mention) - the report calls it "Symptom"; HP calls it **Headache**
- `HP:0000989` (1 mention) - the report calls it "Symptom"; HP calls it **Pruritus**
- `HP:0200071` (1 mention) - the report calls it "Clinical sign"; HP calls it **Peripheral vitreoretinal degeneration**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0020059` (1 mention) - the report calls it "Increased circulating EPO"; HP calls it **Increased red blood cell count**, and lists "Increased RBC count" among its other names
- `CL:0000115` (2 mentions) - the report calls it "endothelial cell, downstream"; CL calls it **endothelial cell**
- `CL:0000764` (1 mention) - the report calls it "Tissue/cell level:** Erythroid lineage"; CL calls it **erythroid lineage cell**