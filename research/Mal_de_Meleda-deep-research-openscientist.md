---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:39:33.127325'
end_time: '2026-10-15T02:04:01.821814'
duration_seconds: 1468.69
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mal de Meleda
  mondo_id: MONDO:0009552
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
citation_count: 24
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 15
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 6
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0007556
    reported_labels:
    - Characteristic / majority
    ontology_label: Plantar hyperkeratosis
  - term_id: HP:0100648
    reported_labels:
    - Subset
    ontology_label: Neoplasm of the tongue
  - term_id: HP:0000973
    reported_labels:
    - approx
    ontology_label: Cutis laxa
  - term_id: HP:0001156
    reported_labels:
    - Subset
    ontology_label: Brachydactyly
  - term_id: HP:0000975
    reported_labels:
    - Common
    ontology_label: Hyperhidrosis
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
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
  path: Mal_de_Meleda-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mal_de_Meleda-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mal de Meleda
- **MONDO ID:** MONDO:0009552 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mal de Meleda** covering all of the
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

# Mal de Meleda (MONDO:0009552; OMIM #248300): A Comprehensive Disease Characteristics Report

## Summary

**Mal de Meleda (MdM)** is a rare autosomal recessive, transgredient (spreading beyond palms/soles) and progredient (worsening with age) diffuse palmoplantar keratoderma (PPK). It is caused by biallelic loss-of-function mutations in **SLURP1** (secreted Ly-6/urokinase-type plasminogen activator receptor–related protein 1; gene *SLURP1*, formerly *ARS component B* / *LY6LS*, on chromosome 8q24.3; UniProt P55000; HGNC:11827). The disease was first described by the Dubrovnik physician Luka (Luko) Stulli in 1826 among residents of the island of Mljet (Meleda), Croatia, and has since been documented worldwide in Palestinian, Turkish, German, Emirati, Korean, Dutch, Javanese/Indonesian, Taiwanese, Algerian, and Tunisian families. Estimated prevalence is approximately **1:100,000**.

Mechanistically, SLURP-1 is a small secreted member of the Ly-6/uPAR (LU) superfamily that adopts a **three-finger-toxin fold** homologous to snake-venom neurotoxins and cardiotoxins. It functions as an autocrine/paracrine cholinergic signaling peptide that acts as a **selective allosteric modulator/antagonist of the α7 nicotinic acetylcholine receptor (α7-nAChR)** on keratinocytes, restraining keratinocyte proliferation and promoting orderly differentiation, apoptosis, and barrier formation. Loss of SLURP-1 removes this "cholinergic brake," producing keratinocyte hyperproliferation, disrupted epidermal lipid/water-barrier homeostasis, and the clinical phenotype. The pathophysiology is strongly supported by *Slurp1*-knockout mice, which faithfully recapitulate the human PPK with lipid-droplet accumulation in the stratum corneum and a water-barrier defect.

Clinically, MdM presents in early infancy with sharply demarcated erythema and hyperkeratosis of the palms and soles that progress with age and extend to the dorsal hands and feet in a "glove-and-socks" distribution. Associated features include skin sclerosis/atrophy, constricting digital bands (**pseudoainhum**, which can cause autoamputation), perioral erythema, brachydactyly, nail abnormalities, and hyperhidrosis with malodor. There is no cure; management is **symptomatic**, centered on oral acitretin (a systemic retinoid) plus topical keratolytics, with surgical release of pseudoainhum bands and genetic counseling. Life expectancy is normal, but morbidity and quality-of-life impact are substantial, and patients may carry a modestly increased risk of cutaneous squamous cell carcinoma and melanoma, consistent with SLURP-1's putative squamous-lineage tumor-suppressor role.

---

## Key Findings

### Finding 1 — Mal de Meleda is an autosomal recessive transgredient PPK caused by SLURP1 mutations

Mal de Meleda, also known as *keratosis palmoplantaris transgrediens of Siemens*, is an autosomal recessive skin disorder characterized by diffuse PPK with transgressive keratosis and onset in early infancy. Multiple independent families across the globe — Palestinian, Turkish, German, Emirati, Korean, Dutch, Javanese/Indonesian, and Taiwanese — carry homozygous or compound heterozygous loss-of-function mutations in *SLURP1* on chromosome **8q24.3**. Documented pathogenic variants span a broad allelic spectrum, including the recurrent missense **G86R (c.256G>A)** substituting arginine for a conserved glycine, the **W15R** missense, a **start-codon loss**, **nonsense/frameshift c.82delT**, splice-site mutations, and the in-frame deletion **c.271_273delTCT**. The disorder is cataloged as **OMIM #248300** with an estimated prevalence of ~1:100,000.

As stated in the primary genetic report: *"Mal de Meleda (MDM) or keratosis palmoplantaris transgrediens of Siemens is an autosomal recessive skin disorder characterized by diffuse palmoplantar keratoderma (PPK) and transgressive keratosis with an onset in early infancy"* and *"patients are homozygous for a new mutation that substitutes an arginine for a conserved glycine residue at position 86"* ([PMID: 12483299](https://pubmed.ncbi.nlm.nih.gov/12483299/)). The prevalence and inheritance are confirmed by a focused review: *"Mal de Meleda is a rare autosomal recessive palmoplantar keratoderma (PPK) disease with an estimated prevalence of 1:100,000"* ([PMID: 26445964](https://pubmed.ncbi.nlm.nih.gov/26445964/)).

### Finding 2 — SLURP-1 is a secreted Ly-6/uPAR protein that allosterically modulates keratinocyte α7-nAChRs

SLURP-1 is an autocrine/paracrine cholinergic peptide that regulates keratinocyte growth and differentiation. Recombinant SLURP-1 inhibits proliferation of human keratinocytes (~40%, EC50 ~4 nM) via the α7-nAChR; it binds selectively to α7-nAChR and non-competitively (allosterically) inhibits acetylcholine responses (IC50 ~1 μM) in oocyte electrophysiology. Downstream, SLURP-1 signaling through α7-nAChR upregulates NF-κB via Ca²⁺ influx and activation of MEK1, Jak2, CaMKII, and PKC. Functionally, SLURP-1 regulates keratinocyte proliferation, apoptosis/differentiation, and wound re-epithelialization.

Key supporting quotes: *"Point mutations in the slurp-1 gene cause the autosomal inflammation skin disease Mal de Meleda. SLURP-1 is considered an autocrine/paracrine hormone that regulates growth and differentiation of keratinocytes"* and *"revealed α7 type nAChRs as an rSLURP-1 target in keratinocytes"* ([PMID: 26905431](https://pubmed.ncbi.nlm.nih.gov/26905431/)). The NF-κB signaling cascade is detailed in [PMID: 20660165](https://pubmed.ncbi.nlm.nih.gov/20660165/), and the wound-epithelialization role in [PMID: 22168155](https://pubmed.ncbi.nlm.nih.gov/22168155/).

### Finding 3 — Slurp1-deficient mice recapitulate MdM PPK with lipid-droplet accumulation and barrier defect

*Slurp1(-/-)* mice, and an independent *Slurp1X(-/-)* (nonsense) line, develop severe PPK with increased keratinocyte proliferation, lipid-droplet accumulation in the stratum corneum, and an epidermal water-barrier defect. These mice also exhibit reduced adiposity, protection from diet-induced obesity, low plasma lipids, and hind-limb clasping (a neuromuscular sign). Importantly, reducing EGFR signaling via a hypomorphic *Egfr* allele did **not** ameliorate the PPK, indicating SLURP1 acts independently of (or downstream of) EGFR signaling.

Supporting quotes: *"Slurp1(-/-) mice developed severe PPK characterized by increased keratinocyte proliferation, an accumulation of lipid droplets in the stratum corneum, and a water barrier defect"* ([PMID: 24499735](https://pubmed.ncbi.nlm.nih.gov/24499735/)), and *"Slurp1 deficiency in mice faithfully recapitulates the human disease, with increased keratinocyte proliferation and thickening of the epidermis on the volar surface of the paws"* ([PMID: 28418591](https://pubmed.ncbi.nlm.nih.gov/28418591/)).

### Finding 4 — Clinical phenotype: transgredient/progredient PPK with sclerosis, pseudoainhum, perioral erythema, and nail changes

The hallmark features are sharply demarcated erythema and hyperkeratosis of palms and soles with onset soon after birth, progressing with age (progrediens) and extending to the dorsal hands and feet in a glove-and-socks distribution (transgrediens). Associated features include skin sclerosis/atrophy, scleroatrophic erythematous lesions, constricting digital bands (**pseudoainhum**) that can cause autoamputation, perioral erythema, brachydactyly, nail abnormalities (koilonychia, subungual hyperkeratosis), hyperhidrosis with malodor, and keratotic plaques over knees and elbows. Histopathology shows hyperkeratosis and acanthosis **without epidermolysis**, accompanied by a perivascular lymphocytic dermal infiltrate.

Supporting quotes: *"The hallmark features of the condition include transient thickening of the palms and soles, skin sclerosis and atrophy, scleroatrophic erythematous lesions, pseudoainhum formation around the digits, and erythema around the mouth"* ([PMID: 41048964](https://pubmed.ncbi.nlm.nih.gov/41048964/)); *"characterized by transgressive palmoplantar keratoderma (PPK), keratotic skin lesions, perioral erythema, brachydactyly and nail abnormalities"* ([PMID: 11285253](https://pubmed.ncbi.nlm.nih.gov/11285253/)); and *"The histopathologic study showed marked hyperkeratosis, acanthosis, and normogranulosis, without epidermolysis"* ([PMID: 21909218](https://pubmed.ncbi.nlm.nih.gov/21909218/)).

### Finding 5 — Founder origin on Mljet Island, Croatia, with founder haplotypes and consanguinity

MdM was first described by Luka Stulli in 1826 on Mljet (Meleda) Island, Croatia. Haplotype analysis of island cases revealed a **shared haplotype near marker D8S1751 on 8qter** in all affected individuals but none of 17 controls, with genealogies consistent with common ancestry. Founder effects have been documented in Mediterranean/Adriatic and North African (Algerian) populations, and the same mutation is shared between Mljet and families located along medieval Dubrovnik trade routes (Middle East, North Africa), implying spread by migration. Croatian island populations are characterized by genetic isolation, consanguinity, and inbreeding.

Supporting quotes: *"These confirmed a shared haplotype in all cases, but in none of 17 unaffected control individuals, near the marker D8S1751 on chromosome 8"* ([PMID: 12145432](https://pubmed.ncbi.nlm.nih.gov/12145432/)); *"The disease was first described on the island of Mljet, Croatia, by Luko Stulli in 1826"* ([PMID: 25102791](https://pubmed.ncbi.nlm.nih.gov/25102791/)); and *"These populations are characterized by high degree of genetic isolation, consanguinity, and inbreeding"* ([PMID: 16909451](https://pubmed.ncbi.nlm.nih.gov/16909451/)).

### Finding 6 — SLURP1 as a putative squamous-lineage tumor suppressor; impaired T-cell activation

In a Palestinian MdM family homozygous for c.82delT, affected members developed squamous cell carcinomas and melanoma at PPK sites. *SLURP1* mRNA is markedly elevated in epithelial tissues and significantly suppressed in epithelial malignancies relative to normal or premalignant counterparts. Recombinant SLURP-1 reduces nitrosamine-induced tumorigenic transformation of keratinocytes in vitro and in nude mice. Peripheral blood mononuclear cells (PBMCs) from G86R homozygotes/heterozygotes show defective anti-CD3/CD28 T-cell activation that is rescued by recombinant SLURP-1, and homozygous patients are reported to be prone to melanoma and viral infection.

Supporting quotes: *"SLURP1 mRNA levels were found to be markedly elevated in tissues of epithelial lineage, relative to tissues of other lineages, and significantly suppressed in malignant tumors of epithelial lineage relative to normal or their premalignant counterparts"* ([PMID: 29231248](https://pubmed.ncbi.nlm.nih.gov/29231248/)); and *"PBMCs with the heterozygous and homozygous SLURP-1 G86R mutation had defective T-cell activation"* ([PMID: 20854438](https://pubmed.ncbi.nlm.nih.gov/20854438/)). Anti-tumorigenic activity of SLURP-1/-2 against tobacco nitrosamines is documented in [PMID: 17643396](https://pubmed.ncbi.nlm.nih.gov/17643396/) and [PMID: 17280689](https://pubmed.ncbi.nlm.nih.gov/17280689/).

### Finding 7 — Management is symptomatic: oral acitretin plus topical keratolytics

Because MdM is rare, there are no formal guidelines. The accepted approach is **oral acitretin** (a systemic retinoid; ATC D05BB02) combined with topical keratolytic therapy (salicylic acid, urea, emollients), plus genetic counseling. Systemic retinoids reduce hyperkeratosis in related PPKs at ~0.3–0.5 mg/kg/day but relapse on cessation and carry dose-related toxicity (teratogenicity, mucocutaneous dryness, hepatic and lipid effects). Surgical excision with Z-plasty is used for constricting pseudoainhum bands, though recurrence is common. No gene/cell/RNA-targeted therapy is approved.

Supporting quotes: *"there are no set guidelines for management, but the accepted approach tends to include oral acitretin plus topical keratolytic therapy. Genetic counseling should also be offered"* ([PMID: 26445964](https://pubmed.ncbi.nlm.nih.gov/26445964/)); and *"Surgical excision is the only treatment of pseudoainhum; however, it is fraught with recurrence"* ([PMID: 39509536](https://pubmed.ncbi.nlm.nih.gov/39509536/)).

### Finding 8 — SLURP-1 is a single-domain three-finger-toxin-fold protein; MdM mutations cause loss of function

SLURP-1 (UniProt P55000; HGNC:11827; gene *SLURP1* on 8q24.3) is a small secreted member of the Ly-6/uPAR (LU) superfamily whose amino-acid composition is homologous to three-finger toxins such as frog cytotoxin and snake-venom neurotoxins/cardiotoxins, stabilized by a conserved disulfide-bonded β-sheet "three-finger" fold. It is expressed in suprabasal/granular keratinocytes of squamous epithelia. MdM pathogenic variants (missense G86R, W15R; nonsense/frameshift c.82delT; splice-site; start-codon loss; in-frame c.271_273delTCT) disrupt the fold or abolish the protein, producing loss of function.

Supporting quotes: *"The amino acid composition of SLURP-1 is homologous to that of toxins such as frog cytotoxin and snake venom neurotoxins and cardiotoxins"* and *"Three different homozygous mutations (a deletion, a nonsense and a splice site mutation) were detected in 19 families of Algerian and Croatian origin"* ([PMID: 11285253](https://pubmed.ncbi.nlm.nih.gov/11285253/)).

---

## Report by Research Section

### 1. Disease Information

**Overview.** Mal de Meleda is a rare monogenic, autosomal recessive diffuse transgredient palmoplantar keratoderma with onset in early infancy. It is "aggregated disease-level" knowledge derived predominantly from case reports, family studies, and small case series, rather than large EHR cohorts.

**Key identifiers:**
- **MONDO:** MONDO:0009552
- **OMIM:** #248300
- **Gene (OMIM):** *SLURP1* / ARS component B, OMIM *606119
- **Orphanet:** ORPHA:87503 (Mal de Meleda)
- **ICD-10:** Q82.8 (other specified congenital malformations of skin); **ICD-11:** EC20.0 / LA90 range (hereditary PPK)
- **MeSH:** "Keratoderma, Palmoplantar" (and "Mal de Meleda" as entry term)
- **HGNC:** HGNC:11827 (*SLURP1*); **UniProt:** P55000

**Synonyms / alternative names:** Meleda disease; keratosis palmoplantaris transgrediens of Siemens; keratoderma palmoplantare transgrediens; mal de Meleda; acroerythrokeratoderma; Mljet disease.

**Evidence source:** Aggregated disease-level resources (OMIM, Orphanet, UniProt, HGNC) plus primary literature. **Not** derived from individual EHR data.

### 2. Etiology

**Causal factor:** Monogenic — biallelic loss-of-function mutations in *SLURP1* (Findings 1, 8). The disease is fully genetic; there is no established infectious or primary environmental cause.

**Genetic risk factors:** Causal variants are in *SLURP1* only (no genetic heterogeneity confirmed for classic MdM, though clinically overlapping PPKs involve other genes — see Differential Diagnosis). **Consanguinity** and **founder effects** substantially increase risk in isolated/endemic populations (Mljet, Adriatic, Algerian, Middle Eastern) (Finding 5). Being the offspring of two carriers (each contributing a loss-of-function allele) is the key determinant.

**Environmental risk factors:** No proven environmental cause. Mechanical stress, friction, pressure, heat, and secondary bacterial/fungal colonization (contributing to malodor and maceration) may aggravate established lesions but do not cause disease.

**Protective factors:** None established genetically beyond simply not carrying biallelic loss-of-function alleles. No dietary/lifestyle protective factors are documented.

**Gene–environment interactions:** Minimal/none definitively established. The mouse data (reduced adiposity, protection from diet-induced obesity in *Slurp1−/−*) hint at a SLURP1–lipid-metabolism interaction, but this is a model-organism observation, not a demonstrated human GxE effect (Finding 3).

### 3. Phenotypes

| Phenotype | Type | Onset | Severity / Course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Diffuse palmoplantar keratoderma | Physical manifestation | Early infancy / neonatal | Severe, progressive | Universal (~100%) | HP:0007592 (transgressive PPK); HP:0000982 (PPK) |
| Transgredient spread to dorsa (glove-and-socks) | Physical sign | Childhood | Progressive | Characteristic / majority | HP:0007556 |
| Pseudoainhum (constricting digital bands) | Clinical sign | Childhood–adult | Severe; can cause autoamputation | Subset | HP:0100648 |
| Perioral erythema | Clinical sign | Childhood | Variable | Common | HP:0000973 (approx.) |
| Brachydactyly | Physical sign | Congenital/childhood | Variable | Subset | HP:0001156 |
| Nail abnormalities (koilonychia, subungual hyperkeratosis) | Physical sign | Childhood | Variable | Common | HP:0001598 / HP:0008392 |
| Hyperhidrosis with malodor | Symptom/sign | Childhood | Chronic | Common | HP:0000975 |
| Skin sclerosis/atrophy | Physical sign | Progressive | Variable | Common | HP:0100679 / HP:0000964 |
| Keratotic plaques (knees/elbows) | Physical sign | Childhood | Stable/progressive | Subset | HP:0000962 (hyperkeratosis) |

**Quality-of-life impact:** Substantial. Painful hyperkeratosis and pseudoainhum impair ambulation and manual dexterity; malodor and visible disfigurement impose significant psychosocial burden and stigma, especially in close-knit island communities (Finding 4; qualitative data [PMID: 31178100](https://pubmed.ncbi.nlm.nih.gov/31178100/)). Formal EQ-5D/SF-36 scores are not available for MdM specifically.

### 4. Genetic / Molecular Information

- **Causal gene:** *SLURP1* (ARS component B / LY6LS), 8q24.3; OMIM *606119; HGNC:11827; UniProt P55000.
- **Variant spectrum (all germline, loss-of-function):** missense **G86R (c.256G>A)** at a conserved glycine (recurrent, pseudodominant transmission reported — [PMID: 17184264](https://pubmed.ncbi.nlm.nih.gov/17184264/)); **W15R**; **c.82delT** frameshift; nonsense; splice-site; start-codon loss; in-frame **c.271_273delTCT** (Javanese — [PMID: 29023701](https://pubmed.ncbi.nlm.nih.gov/29023701/)); c.154A>G reported in a Chinese cohort ([PMID: 42384829](https://pubmed.ncbi.nlm.nih.gov/42384829/)).
- **Variant classification (ACMG/AMP):** Pathogenic / likely pathogenic for the recurrent and null alleles.
- **Variant types:** missense, frameshift, nonsense, splice-site, in-frame deletion, start-loss.
- **Allele frequency:** Very rare in gnomAD; enriched locally by founder effects.
- **Somatic vs germline:** Germline.
- **Functional consequence:** Loss of function (protein absence or misfolded, non-functional three-finger domain) (Finding 8).
- **Modifier genes:** None definitively established in humans. Mouse work shows *Egfr* reduction does not modify PPK (Finding 3), arguing against EGFR as a dominant modifier.
- **Epigenetic / chromosomal abnormalities:** None reported; MdM is a single-gene disorder with no aneuploidy or structural chromosomal involvement.

### 5. Environmental Information

No environmental toxin, radiation, lifestyle, or infectious agent causes MdM. Secondary microbial colonization contributes to malodor and maceration. Mechanical/frictional stress may worsen hyperkeratosis locally. **Not applicable** as a primary etiologic category.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function mutation in *SLURP1*** (missense disrupting the three-finger fold, or null allele) **leads to** absence or non-functional secreted SLURP-1 protein in suprabasal/granular keratinocytes. *(Demonstrated — Findings 1, 8.)*
2. Loss of secreted SLURP-1 **results in** loss of allosteric modulation of **α7-nicotinic acetylcholine receptors (α7-nAChR)** on keratinocytes. *(Demonstrated in vitro/oocyte — Finding 2.)*
3. Absent α7-nAChR cholinergic signaling **removes the physiological brake on keratinocyte proliferation** and **dysregulates the proliferation–differentiation–apoptosis balance** (branch A) and **disrupts downstream NF-κB/Ca²⁺/MEK1/Jak2/CaMKII/PKC signaling** (branch B). *(Demonstrated — Findings 2, 3; signaling detail [PMID: 20660165].)*
4. **Branch A — Epidermal hyperproliferation** **leads to** marked hyperkeratosis and acanthosis (without epidermolysis). *(Demonstrated in human histology and mouse — Findings 3, 4.)*
5. **Branch B — Disrupted epidermal lipid/barrier homeostasis** **results in** lipid-droplet accumulation in the stratum corneum and a **water-barrier defect**. *(Demonstrated in mouse; inferred in human — Finding 3.)*
6. Hyperkeratosis + barrier defect + chronic low-grade dermal inflammation (perivascular lymphocytic infiltrate) **produce** the clinical diffuse transgredient PPK, sclerosis, and erythema. *(Demonstrated — Finding 4.)*
7. Progressive sclerosis around digits **leads to** constricting bands (**pseudoainhum**) and, in severe cases, autoamputation. *(Demonstrated — Finding 4.)*
8. **Parallel branch — Loss of SLURP-1 tumor-suppressor/immune function** **leads to** impaired T-cell activation and reduced protection against malignant transformation, **contributing to** increased cutaneous SCC/melanoma risk. *(Demonstrated/inferred — Finding 6.)*

**Molecular pathways:** Non-neuronal cholinergic signaling via α7-nAChR; downstream Raf-1/MEK1/ERK1/2, Jak2, Ca²⁺/CaMKII/PKC, and NF-κB. **GO terms:** GO:0007271 (synaptic transmission, cholinergic — approximate), GO:0008284 (positive regulation of cell proliferation; here dysregulated), GO:0030216 (keratinocyte differentiation), GO:0031424 (keratinization), GO:0008544 (epidermis development), GO:0043066 (negative regulation of apoptosis). **Cellular processes:** keratinocyte proliferation, differentiation, apoptosis, wound re-epithelialization, inflammation. **CL terms:** CL:0000312 (keratinocyte), CL:0000362 (epidermal cell). **Protein dysfunction:** loss of function of a three-finger-toxin-fold modulator. **Metabolic changes:** epidermal lipid dysregulation (stratum corneum lipid droplets). **Immune involvement:** defective T-cell activation; chronic perivascular lymphocytic dermal infiltrate. **CHEBI:** acetylcholine (CHEBI:15355); nicotine (CHEBI:17688); acitretin (CHEBI:50172).

### 7. Anatomical Structures Affected

- **Primary organ:** Skin (UBERON:0002097), specifically palmoplantar epidermis (UBERON:0006956, skin of palm; UBERON:0001513, skin of sole).
- **Secondary involvement:** Dorsal hands/feet (transgrediens), perioral skin, nails (UBERON:0001705), knees/elbows; digits (pseudoainhum → autoamputation).
- **Body system:** Integumentary. Mild neuromuscular signs reported in mouse model only.
- **Tissue/cell level:** Stratified squamous epithelium; **keratinocytes** (CL:0000312), predominantly suprabasal/granular layer where SLURP-1 is expressed.
- **Subcellular:** Secreted extracellular protein (GO:0005615, extracellular space); stratum corneum lipid droplets (GO:0005811).
- **Localization/laterality:** Bilateral, symmetric.

### 8. Temporal Development

- **Onset:** Congenital/early infancy (soon after birth).
- **Onset pattern:** Insidious, chronic.
- **Progression:** Progredient — worsens with age; transgredient spread over childhood. Disease course is **chronic and lifelong**, slowly progressive.
- **Stages:** Early (infantile palmoplantar erythema/hyperkeratosis) → intermediate (transgredient spread, sclerosis) → advanced (pseudoainhum, digital constriction, possible autoamputation).
- **Remission:** No spontaneous remission; partial, reversible improvement with retinoid therapy (relapses on cessation).
- **Critical periods:** Early intervention with keratolytics/retinoids and vigilance for pseudoainhum are the main windows to reduce morbidity.

### 9. Inheritance and Population

- **Epidemiology:** Prevalence ~1:100,000 ([PMID: 26445964](https://pubmed.ncbi.nlm.nih.gov/26445964/)); higher in founder populations. Incidence not separately quantified.
- **Inheritance:** Autosomal recessive (OMIM #248300). Pseudodominant transmission with G86R reported in highly consanguineous pedigrees ([PMID: 17184264](https://pubmed.ncbi.nlm.nih.gov/17184264/)).
- **Penetrance:** Complete for biallelic loss-of-function genotypes.
- **Expressivity:** Variable (severity of pseudoainhum, transgrediens extent).
- **Anticipation:** Not applicable (no repeat expansion).
- **Germline mosaicism:** Not reported.
- **Founder effects:** Well documented (Mljet/Adriatic, Algerian, Middle Eastern trade-route populations) (Finding 5).
- **Consanguinity:** Major contributor in endemic/isolated populations.
- **Carrier frequency:** Elevated in founder populations; low globally.
- **Geographic distribution:** Worldwide but historically clustered along medieval Dubrovnik trade routes; cases from Croatia, Algeria, Germany, Turkey, Palestine, UAE, Korea, Netherlands, Indonesia (Java), Taiwan, China.
- **Sex ratio:** ~1:1 (autosomal). **Age distribution:** All ages; lifelong.

### 10. Diagnostics

- **Clinical diagnosis:** Based on characteristic diffuse transgredient PPK with onset in infancy, sclerosis, pseudoainhum, perioral erythema, and family history/consanguinity.
- **Histopathology (biopsy):** Marked hyperkeratosis, acanthosis, normogranulosis, **without epidermolysis**; perivascular lymphocytic dermal infiltrate ([PMID: 21909218](https://pubmed.ncbi.nlm.nih.gov/21909218/)). Distinguishes MdM from epidermolytic PPKs.
- **Genetic testing (confirmatory, gold standard):** Single-gene *SLURP1* sequencing; gene panels for hereditary PPK; whole-exome sequencing (WES) when the panel is negative or phenotype overlaps. WGS rarely needed. CMA, karyotyping, FISH, mitochondrial and repeat-expansion testing are **not applicable**.
- **Biomarkers:** Reduced/absent SLURP-1; no routine circulating biomarker.
- **Imaging:** Not diagnostic; radiographs may document acro-osteolysis/autoamputation.
- **Differential diagnosis:** Other diffuse PPKs and mutilating keratodermas — Vohwinkel syndrome (GJB2/LOR), Olmsted syndrome (TRPV3), Papillon–Lefèvre syndrome (CTSC), Nagashima-type PPK (SERPINB7), Bothnia-type (AQP5), Greither/epidermolytic (KRT1/KRT10), loricrin keratoderma, progressive symmetric erythrokeratoderma. Distinguishing features: MdM lacks periodontitis (vs PLS), lacks deafness (vs KID/Vohwinkel classic), lacks epidermolysis histologically, and shows transgrediens with pseudoainhum and perioral erythema. MdM is "a great imitator" ([PMID: 31178100](https://pubmed.ncbi.nlm.nih.gov/31178100/)).
- **Screening:** Carrier/cascade screening in affected families and founder populations; prenatal/preimplantation testing possible once the familial variant is known.

### 11. Outcome / Prognosis

- **Survival/mortality:** Normal life expectancy; MdM is not directly fatal.
- **Morbidity/function:** High — chronic pain, impaired ambulation and hand function, malodor, psychosocial burden; pseudoainhum can cause digital autoamputation.
- **Disease course:** Chronic, lifelong, slowly progressive; partial response to therapy with relapse on cessation.
- **Complications:** Secondary bacterial/fungal infection, maceration, flexion contractures, autoamputation; increased risk of cutaneous squamous cell carcinoma and melanoma at PPK sites (Finding 6); reported susceptibility to viral infection.
- **Recovery potential:** No cure; symptomatic control only.
- **Prognostic factors:** Severity of pseudoainhum and transgrediens extent; adherence to keratolytic/retinoid therapy; timely surgical release of constricting bands.

### 12. Treatment

**Pharmacotherapy (symptomatic):**
- **Oral acitretin** (systemic retinoid; ATC D05BB02; NCIT: Acitretin) — first-line, ~0.3–0.5 mg/kg/day; reduces hyperkeratosis; relapses on cessation; dose-related toxicity (teratogenicity, mucocutaneous dryness, hepatic/lipid effects) ([PMID: 26445964](https://pubmed.ncbi.nlm.nih.gov/26445964/); analogous PPK evidence [PMID: 28008647](https://pubmed.ncbi.nlm.nih.gov/28008647/), [PMID: 29500825](https://pubmed.ncbi.nlm.nih.gov/29500825/)). Isotretinoin is an alternative retinoid.
- **Topical keratolytics:** salicylic acid, urea, emollients, topical retinoids; often combined with low-dose systemic retinoid to limit toxicity ([PMID: 29500825](https://pubmed.ncbi.nlm.nih.gov/29500825/)).

**Surgical/interventional:** Excision with **Z-plasty** for pseudoainhum constricting bands (recurrence common — [PMID: 39509536](https://pubmed.ncbi.nlm.nih.gov/39509536/)); amputation in advanced digital involvement.

**Supportive/rehabilitative:** Skin hydration, debridement, antimicrobial management of secondary infection, foot/hand care, physiotherapy to preserve function; genetic counseling.

**Advanced/targeted/experimental:** No approved gene, cell, RNA-based, or SLURP-1-replacement therapy. Recombinant SLURP-1 is a conceptual mechanism-based candidate (restores the α7-nAChR brake in vitro), but no human trials exist. **NCIT terms:** Acitretin, Salicylic Acid, Surgical Procedure, Genetic Counseling.

**Pharmacogenomics:** None specific to MdM.

### 13. Prevention

- **Primary prevention:** Not possible for a Mendelian disorder; genetic counseling, carrier screening in founder/consanguineous populations, and reproductive options (prenatal/preimplantation genetic testing) reduce new-case occurrence.
- **Secondary prevention:** Early diagnosis and keratolytic/retinoid therapy; surveillance for pseudoainhum to prevent autoamputation.
- **Tertiary prevention:** Prevent complications — skin-cancer surveillance (given SCC/melanoma risk), infection control, functional preservation.
- **Immunization / public health / environmental interventions:** Not applicable.
- **Counseling:** Genetic counseling is central, especially in consanguineous families.

### 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (*Homo sapiens*, NCBI:txid9606). Experimental models in *Mus musculus* (NCBI:txid10090).
- **Orthologous gene:** Mouse *Slurp1* (NCBI Gene).
- **Natural disease in other species:** No well-characterized naturally occurring animal homolog of MdM documented in OMIA; disease knowledge in animals derives from engineered *Slurp1*-knockout mice (Finding 3), not natural disease.
- **Comparative biology:** SLURP-1 and the cholinergic α7-nAChR axis are evolutionarily conserved; the mouse knockout recapitulates the human PPK, supporting mechanistic conservation.
- **Transmission:** Not applicable (non-infectious genetic disease; no zoonotic potential).

### 15. Model Organisms

- **Mammalian model:** *Slurp1(-/-)* knockout mouse and *Slurp1X(-/-)* nonsense-allele mouse (MGI). Genetic model types: knockout, nonsense knock-in.
- **Phenotype recapitulation:** Faithful — severe PPK with increased keratinocyte proliferation, epidermal thickening on volar paw surfaces, stratum-corneum lipid-droplet accumulation, and water-barrier defect (Finding 3). Additional phenotypes: reduced adiposity, protection from diet-induced obesity, low plasma lipids, hind-limb clasping.
- **Model-based insight:** EGFR reduction (hypomorphic *Egfr*) does not rescue the PPK, implicating SLURP1-independent/downstream mechanisms (Finding 3).
- **Cellular/in vitro models:** Human epidermal and oral keratinocytes; immortalized Het-1A esophageal keratinocytes; recombinant SLURP-1 functional assays; *Xenopus* oocyte electrophysiology for α7-nAChR modulation (Finding 2).
- **Limitations:** Mouse metabolic phenotypes (adiposity/lipid) are not prominent features of human MdM; models emphasize skin barrier/proliferation. Resources: MGI, IMPC.

---

## Mechanistic Model / Interpretation

```
  SLURP1 biallelic LOF mutation (8q24.3)
                 │ leads to
                 ▼
  Absent / non-functional secreted SLURP-1
  (three-finger-toxin fold, Ly-6/uPAR family)
                 │ results in
                 ▼
  Loss of allosteric modulation of keratinocyte α7-nAChR
         │                                   │
   (Branch A) removes brake           (Branch B) disrupts
   on proliferation                    NF-κB/Ca²⁺/MEK1/Jak2
         │                                   │
         ▼                                   ▼
  Keratinocyte hyperproliferation     Epidermal lipid/barrier
  → hyperkeratosis + acanthosis       dysregulation → stratum
  (no epidermolysis)                  corneum lipid droplets,
         │                             water-barrier defect
         └──────────────┬──────────────┘
                        ▼
      Diffuse transgredient/progredient PPK
      + sclerosis + perioral erythema + nail changes
                        │ leads to
                        ▼
          Pseudoainhum → digital autoamputation

  (Parallel) Loss of SLURP-1 tumor-suppressor/immune function
   → impaired T-cell activation + reduced protection from
     malignant transformation → ↑ cutaneous SCC / melanoma risk
```

The central, well-supported insight is that MdM is a **non-neuronal cholinergic signaling disorder of the epidermis**: SLURP-1 normally tunes keratinocyte behavior through α7-nAChR, and its loss simultaneously releases a proliferative brake and corrupts barrier lipid homeostasis. The convergence of human genetics (Findings 1, 8), biochemistry/pharmacology (Finding 2), and a faithful knockout mouse (Finding 3) makes this one of the better-validated causal chains among the inherited PPKs. The tumor-suppressor/immune arm (Finding 6) is biologically plausible and empirically supported but clinically secondary.

---

## Evidence Base

| PMID | Role | How it supports / challenges findings |
|---|---|---|
| [12483299](https://pubmed.ncbi.nlm.nih.gov/12483299/) | Supports F1 | Defines AR transgredient PPK; documents G86R across German/Turkish/Palestinian/UAE families |
| [11285253](https://pubmed.ncbi.nlm.nih.gov/11285253/) | Supports F4, F8 | First SLURP1 gene report; three-finger-toxin homology; LOF variant classes; clinical features |
| [26445964](https://pubmed.ncbi.nlm.nih.gov/26445964/) | Supports F1, F4, F7 | Focused review: prevalence 1:100,000, histology, acitretin + keratolytics |
| [26905431](https://pubmed.ncbi.nlm.nih.gov/26905431/) | Supports F2 | Identifies α7-nAChR as SLURP-1 target; selective allosteric antagonism |
| [20660165](https://pubmed.ncbi.nlm.nih.gov/20660165/) | Supports F2 | NF-κB upregulation via α7-nAChR, Ca²⁺/MEK1/Jak2/CaMKII/PKC |
| [22168155](https://pubmed.ncbi.nlm.nih.gov/22168155/) | Supports F2 | SLURP-1 regulates wound epithelialization via α7-nAChR |
| [24499735](https://pubmed.ncbi.nlm.nih.gov/24499735/) | Supports F3 | *Slurp1−/−* mice: PPK, lipid droplets, water-barrier defect |
| [28418591](https://pubmed.ncbi.nlm.nih.gov/28418591/) | Supports F3 | Faithful recapitulation; EGFR reduction does not rescue PPK |
| [12145432](https://pubmed.ncbi.nlm.nih.gov/12145432/) | Supports F5 | Founder haplotype near D8S1751 in Mljet cases |
| [25102791](https://pubmed.ncbi.nlm.nih.gov/25102791/) | Supports F5 | Historical origin, Stulli 1826, Mljet |
| [16909451](https://pubmed.ncbi.nlm.nih.gov/16909451/) | Supports F5 | Croatian island genetic isolation/consanguinity |
| [29231248](https://pubmed.ncbi.nlm.nih.gov/29231248/) | Supports F6 | SLURP1 tumor-suppressor; suppressed in epithelial malignancies; melanoma signal |
| [20854438](https://pubmed.ncbi.nlm.nih.gov/20854438/) | Supports F6 | Defective T-cell activation with G86R; rescued by recombinant SLURP-1 |
| [17643396](https://pubmed.ncbi.nlm.nih.gov/17643396/), [17280689](https://pubmed.ncbi.nlm.nih.gov/17280689/) | Supports F6 | SLURP-1 reduces nitrosamine-induced transformation (in vitro + nude mice) |
| [39509536](https://pubmed.ncbi.nlm.nih.gov/39509536/) | Supports F7 | Surgical excision for pseudoainhum; recurrence common |
| [21909218](https://pubmed.ncbi.nlm.nih.gov/21909218/) | Supports F4 | Histology: hyperkeratosis/acanthosis without epidermolysis |
| [41048964](https://pubmed.ncbi.nlm.nih.gov/41048964/) | Supports F4 | Enumerates hallmark features incl. pseudoainhum, perioral erythema |
| [17184264](https://pubmed.ncbi.nlm.nih.gov/17184264/) | Supports F1/§9 | Pseudodominant G86R inheritance in consanguineous pedigrees |
| [29023701](https://pubmed.ncbi.nlm.nih.gov/29023701/), [25557416](https://pubmed.ncbi.nlm.nih.gov/25557416/) | Supports F1/§9 | Novel c.271_273delTCT; "ubiquitous" SLURP1 mutations (Indonesia) |
| [42384829](https://pubmed.ncbi.nlm.nih.gov/42384829/) | Supports §10 | Large Chinese PPK cohort; SLURP1 c.154A>G among diffuse PPK genes |

**Evidence source types:** human clinical/genetic (family studies, case reports, cohorts), model organism (knockout mice), in vitro/biochemical (recombinant protein, oocyte electrophysiology, keratinocyte culture), and computational/structural (three-finger-fold homology).

---

## Limitations and Knowledge Gaps

1. **No human omics data** (transcriptomic/proteomic/metabolomic) on MdM lesional skin were identified; barrier-lipid mechanisms are inferred primarily from mouse.
2. **Quality-of-life metrics** (EQ-5D/SF-36/PROMIS) are not formally quantified for MdM; QoL impact is described qualitatively.
3. **Cancer risk** is based on small family observations plus mechanistic in vitro/model data; incidence of SCC/melanoma in MdM is not epidemiologically quantified.
4. **Genotype–phenotype correlations** are incompletely defined; expressivity (pseudoainhum severity) varies even within genotype.
5. **No disease-modifying therapy**; retinoid efficacy data are largely extrapolated from related PPKs rather than MdM-specific trials.
6. **Modifier genes and gene–environment interactions** in humans remain essentially unknown.
7. **No natural animal disease model** is catalogued; comparative/veterinary data are absent.

---

## Proposed Follow-up Experiments / Actions

1. **Single-cell/spatial transcriptomics** of MdM lesional vs. normal palmoplantar epidermis to map the keratinocyte proliferation–differentiation axis and barrier-lipid gene programs in humans (GEO/HCA).
2. **Lipidomics** of MdM stratum corneum (LIPID MAPS/Metabolomics Workbench) to confirm the barrier-lipid defect observed in mice and identify targetable species.
3. **Recombinant SLURP-1 / α7-nAChR agonist topical replacement**: preclinical testing in *Slurp1−/−* mice as a mechanism-based therapy, then early-phase human studies.
4. **Prospective registry** to quantify prevalence, pseudoainhum incidence, SCC/melanoma risk, and validated QoL outcomes across founder and non-founder populations.
5. **Structural studies** (AlphaFold/PDB) of G86R and W15R SLURP-1 to define how specific mutations destabilize the three-finger fold and inform variant interpretation.
6. **Carrier-screening programs** in high-prevalence/consanguineous populations with genetic counseling and reproductive options.
7. **Gene/RNA-based therapy feasibility** (e.g., AAV-delivered *SLURP1* or mRNA) as a long-term curative strategy, given the small, secreted nature of the protein.

---

*Report compiled from 8 confirmed findings and 64 reviewed papers over a 5-iteration autonomous investigation. Mal de Meleda is MONDO:0009552 / OMIM #248300, a SLURP1 loss-of-function autosomal recessive transgredient palmoplantar keratoderma.*


## Artifacts

- [OpenScientist final report](Mal_de_Meleda-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mal_de_Meleda-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0007556` (1 mention) - the report calls it "Characteristic / majority"; HP calls it **Plantar hyperkeratosis**
- `HP:0100648` (1 mention) - the report calls it "Subset"; HP calls it **Neoplasm of the tongue**
- `HP:0000973` (1 mention) - the report calls it "approx"; HP calls it **Cutis laxa**
- `HP:0001156` (1 mention) - the report calls it "Subset"; HP calls it **Brachydactyly**
- `HP:0000975` (1 mention) - the report calls it "Common"; HP calls it **Hyperhidrosis**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007271` (1 mention) - the report calls it "synaptic transmission, cholinergic — approximate"; GO calls it **synaptic transmission, cholinergic**
- `GO:0008284` (1 mention) - the report calls it "positive regulation of cell proliferation; here dysregulated"; GO calls it **positive regulation of cell population proliferation**, and lists "positive regulation of cell proliferation" among its other names
- `GO:0043066` (1 mention) - the report calls it "negative regulation of apoptosis"; GO calls it **negative regulation of apoptotic process**, and lists "negative regulation of apoptosis" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Primary organ:** Skin"; UBERON calls it **skin of body**, and lists "skin organ" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000312` - called "keratinocyte", "keratinocytes"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.