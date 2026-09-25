---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T04:49:56.655373'
end_time: '2026-09-25T05:04:08.236229'
duration_seconds: 851.58
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rickettsialpox
  mondo_id: MONDO:0019360
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 6
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 22
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 5
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: NCBITaxon:10090
    reported_labels:
    - Mus musculus
    - Reservoir host:** house mouse *Mus musculus
    ontology_label: Mus musculus
  - term_id: UBERON:0001981
    reported_labels:
    - Vascular system:** small blood vessels / microvasculature
    ontology_label: blood vessel
  - term_id: UBERON:0002107
    reported_labels:
    - Secondary organ involvement:** liver
    ontology_label: liver
  - term_id: NCIT:C842
    reported_labels:
    - Tetracycline antibiotic
    ontology_label: Stanozolol
  - term_id: NCIT:C242
    reported_labels:
    - Broad-spectrum; 50S ribosome inhibitor (alternative)
    ontology_label: Anti-Androgen
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rickettsialpox-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rickettsialpox-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rickettsialpox
- **MONDO ID:** MONDO:0019360 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rickettsialpox** covering all of the
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

# Rickettsialpox (MONDO:0019360): A Comprehensive Disease Characteristics Report

## Summary

**Rickettsialpox is a mild, self-limited febrile spotted fever group (SFG) rickettsiosis caused by the obligate intracellular bacterium *Rickettsia akari*, transmitted to humans by the bite of the house-mouse mite *Liponyssoides sanguineus*, whose natural reservoir is the common house mouse (*Mus musculus*).** It is an infectious, non-heritable urban zoonosis first described in New York City in 1946 and remains endemic there today. After an incubation period of roughly 9–14 days, patients develop a painless inoculation eschar at the mite-bite site, followed by abrupt fever, headache, chills, myalgia, and regional lymphadenopathy, and then a generalized papulovesicular ("chickenpox-like") rash. The illness resolves over 2–3 weeks, systemic complications (e.g., self-limited hepatitis) are rare, and no deaths have been attributed to the disease.

The pathophysiology is shared across the spotted fever group: *R. akari* invades vascular endothelial cells, damaging them directly, increasing vascular permeability, and producing a small-vessel lymphohistiocytic vasculitis that underlies both the local eschar and the disseminated rash. Diagnosis relies on the clinical triad (eschar + fever + papulovesicular rash), skin-biopsy immunohistochemistry demonstrating SFG rickettsiae, indirect immunofluorescence serology (a four-fold IgG rise or a single titer ≥1:64), and increasingly on PCR of eschar or lesion material (*gltA*, *ompA*, *ompB*, 17-kDa genes). Empiric doxycycline is curative and produces rapid defervescence; the prognosis is excellent.

Because rickettsialpox is not a nationally notifiable disease in the United States, it is widely under-diagnosed and under-reported; reported incidence tracks clinician awareness rather than true disease burden. Prevention is entirely environmental — rodent population control, mite/vector control with acaricides, and improved dwelling sanitation. There is no vaccine, no genetic susceptibility component, and no Mendelian OMIM/Orphanet entry, because the disease is infectious rather than heritable. Serologic evidence of *R. akari* exposure in urban dogs and cats supports a One Health, urban-rodent ecology and a broader geographic footprint than the classic New York foci.

This report is organized against the 15-section disease-characteristics template. Sections tied to genetic disease (causal genes, pathogenic variants, inheritance, model organisms of a heritable condition) are explicitly marked **Not applicable** because rickettsialpox is an acquired infection.

---

## Key Findings

### Finding 1 — Etiology: *Rickettsia akari* transmitted by the house-mouse mite

Rickettsialpox is caused by *Rickettsia akari*, an obligate intracellular, Gram-negative bacterium of the spotted fever group, and is transmitted to humans by the bite of the mite *Liponyssoides sanguineus* (formerly *Allodermanyssus sanguineus*), which infests the common house mouse *Mus musculus*. The causal chain — agent, vector, reservoir — is well established in primary literature. As stated directly: *"Rickettsialpox is an acute, self-limited, febrile illness caused by Rickettsia akari and transmitted by Liponyssoides sanguineus, a mite that infests the common house mouse, Mus musculus"* [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).

Serologic and immunohistochemical confirmation of *R. akari* as the etiologic agent in human cases was documented in a consecutive New York City hospital case series: *"A 4-fold or greater increase in IgG antibody titers reactive with Rickettsia akari was observed in all 9 patients for whom acute and convalescent phase samples were available"* [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/). Because transmission is mite-borne rather than tick-borne, rickettsialpox is unusual among SFG rickettsioses; the mite vector both maintains the organism transovarially and delivers it during blood feeding.

**Evidence type:** human clinical / serologic (aggregated case series). **Organism terms:** *Rickettsia akari* (NCBITaxon:786); *Mus musculus* (NCBITaxon:10090); vector *Liponyssoides sanguineus*.

### Finding 2 — Clinical presentation and endemic urban persistence

Rickettsialpox presents as a self-limited febrile illness defined by two hallmark skin lesions: an inoculation eschar and a generalized papulovesicular rash. In a consecutive NYC series of 18 patients (2001–2002), immunohistochemistry detected SFG rickettsiae in the great majority of lesions: *"Immunohistochemical testing revealed spotted fever group rickettsiae in all 16 eschars and in 5 of the 9 papulovesicles tested"* [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/). The disease is clinically important because it mimics more dangerous conditions: *"Rickettsialpox is a self-limited febrile illness with skin lesions that may be mistaken for signs of potentially more serious diseases, such as cutaneous anthrax or chickenpox"* [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/). Notably, 50% of that series presented in the five months after the October 2001 anthrax bioterrorism events, indicating that heightened clinician awareness — not a true rise in incidence — drove detection.

Systemic complications are uncommon but recognized; self-resolving hepatitis has been reported: *"we describe two patients with rickettsialpox who had acute hepatitis that resolved completely"* [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).

**Evidence type:** human clinical case series.

### Finding 3 — Pathophysiology: endothelial invasion and small-vessel vasculitis

The core pathophysiology is shared with the entire spotted fever group. In David Walker's authoritative SFG review, *"These obligate intracellular bacteria invade vascular endothelial cells, which are damaged directly, causing increased vascular permeability"* [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/), and an eschar forms at the site of the vector bite. Mechanistic studies of related SFG rickettsiae (*R. conorii*, *R. parkeri*) confirm the shared pathogenic program that is inferred to apply to *R. akari*: preferential tropism for microvascular endothelium producing barrier dysfunction and increased permeability. *"Obligate intracellular bacteria which exhibit preferential tropism for host microvascular endothelium in the mammalian hosts, resulting in disease manifestations attributed primarily to endothelial damage or dysfunction"* [PMID: 32977742](https://pubmed.ncbi.nlm.nih.gov/32977742/); and *"vascular inflammation and dysfunction represent salient features of rickettsial pathogenesis"* [PMID: 33003310](https://pubmed.ncbi.nlm.nih.gov/33003310/).

Downstream molecular events characterized in SFG models include mTOR (mTORC1/mTORC2) activation in infected human endothelial cells [PMID: 33003310](https://pubmed.ncbi.nlm.nih.gov/33003310/), and endothelial secretome/exosome changes that drive barrier dysfunction and edema [PMID: 31955791](https://pubmed.ncbi.nlm.nih.gov/31955791/), [PMID: 33975935](https://pubmed.ncbi.nlm.nih.gov/33975935/).

**Evidence type:** authoritative review (human) + in vitro/in vivo mechanistic studies of related SFG species (inferred to *R. akari*).

### Finding 4 — Diagnosis and curative treatment

Diagnosis relies on serology and biopsy immunohistochemistry, and empiric doxycycline is curative. Per Walker: *"Rickettsiae are demonstrable by diagnostic immunohistology in biopsies of rash or eschar. Empiric treatment with doxycycline, tetracycline, or chloramphenicol should be given early in the course on the basis of clinical suspicion"* [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/). The NYC series demonstrated diagnosis by IHC of paraffin-embedded skin biopsy (SFG rickettsiae in 16/16 eschars and 5/9 papulovesicles) and by indirect immunofluorescence serology (four-fold IgG rise or single titer ≥1:64) [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/). Serology cross-reacts broadly across the SFG (e.g., *R. rickettsii* antigen can be used as a screen). Rickettsialpox is self-limited even without treatment, with no reported deaths, and doxycycline produces rapid resolution.

**Evidence type:** authoritative review + human case series.

### Finding 5 — One Health ecology: animal seroreactivity

Urban companion animals show measurable *R. akari* seroreactivity, supporting a One Health, urban-rodent ecology and a broad geographic distribution. In New York City dogs, *"Cross-absorption testing indicated that in 6 of 7 samples, infection was caused by R akari. Results suggest that dogs can be naturally infected with R akari"* [PMID: 11394829](https://pubmed.ncbi.nlm.nih.gov/11394829/); 7.7% of 311 dogs were EIA-positive for SFG rickettsiae, with tick infestation and increasing age as significant risk factors. Among 170 US cats, seroprevalence was *"14.9% for R akari"* [PMID: 16434226](https://pubmed.ncbi.nlm.nih.gov/16434226/). Human SFG seroreactivity including *R. akari* was also detected in a Papua New Guinea serosurvey [PMID: 16450784](https://pubmed.ncbi.nlm.nih.gov/16450784/), indicating exposure beyond the classic foci.

**Evidence type:** veterinary/human seroepidemiology.

### Finding 6 — Clinical course and natural history

The classic natural history is a ~9–14 day incubation, a painless inoculation eschar, then fever/headache and a generalized papulovesicular rash resolving over 2–3 weeks. A mite bite produces a painless papule that becomes a vesicle and then a black-crusted eschar (IHC-positive in 16/16 eschars in the Koss series) [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/). After incubation, patients develop abrupt fever, chills, headache, myalgia, and often regional lymphadenopathy, followed within 2–3 days by a generalized papulovesicular eruption (IHC-positive in 5/9 papulovesicles). Eschar formation at the vector inoculation site is a defining SFG feature: *"Eschar occurs in some SFG rickettsioses at the site of tick bite"* [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/). The illness is acute and self-limited; systemic complications are rare (occasional self-resolving hepatitis) [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).

### Finding 7 — Epidemiology and prevention: under-reported urban zoonosis

Rickettsialpox is not nationally notifiable in the US and is regarded as under-diagnosed and under-reported; reported incidence tracks clinician awareness. The NYC authors concluded: *"Rickettsialpox remains endemic in New York City, and the bioterrorism attacks of October 2001 may have led to increased awareness and detection of this disease"* [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/). The disease occurs where humans contact the rodent-associated mite: *"The hematophagic-biting mite, Liponyssoides sanguineus, is a mite of the rat, mouse, and other domestic rodents but can also bite humans"* [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/), with ectoparasite exposure heightened in homeless and inner-city populations. Prevention is achieved through rodent population control, mite/vector control (acaricides), and improved sanitation.

### Finding 8 — Identifiers and classification

Rickettsialpox is classified as an infectious spotted fever group rickettsiosis, not a genetic disease. Phylogenetic analysis of the citrate synthase (*gltA*) gene places the mite-borne organism within the SFG cluster: *"the mite-borne organism Rickettsia akari were associated with the SFG cluster"* [PMID: 9103608](https://pubmed.ncbi.nlm.nih.gov/9103608/). Standard identifiers: **MONDO:0019360**; **ICD-10 A79.1** (Rickettsialpox due to *Rickettsia akari*); **MeSH D012288**; pathogen **NCBITaxon:786**. There is no OMIM or Orphanet Mendelian entry because the disease is infectious. Synonyms include **vesicular rickettsiosis** and **Kew Gardens spotted fever**.

---

## Report by Template Section

### 1. Disease Information

**Overview.** Rickettsialpox is an acute, mild, self-limited febrile illness caused by *Rickettsia akari* and transmitted by the mite *Liponyssoides sanguineus* [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/). It is characterized by an inoculation eschar and a disseminated papulovesicular rash, and it resolves without sequelae.

**Key identifiers.** MONDO:0019360; ICD-10 A79.1; MeSH D012288 (Rickettsialpox); pathogen taxon NCBITaxon:786 (*Rickettsia akari*). No OMIM or Orphanet entry (non-heritable, infectious disease).

**Synonyms / alternative names.** Vesicular rickettsiosis; Kew Gardens spotted fever; *Rickettsia akari* infection.

**Information source.** Derived predominantly from aggregated disease-level resources and hospital case series (e.g., the New York City consecutive series, PMID 14676069) plus authoritative SFG reviews — not individual EHR-level datasets.

### 2. Etiology

- **Causal factor (infectious):** *Rickettsia akari*, an obligate intracellular SFG bacterium [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/), [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/).
- **Vector:** the house-mouse mite *Liponyssoides sanguineus* [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/), [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/).
- **Reservoir:** the common house mouse *Mus musculus* [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).
- **Genetic risk factors:** **None identified.** No human susceptibility loci, GWAS signals, or modifier genes are known; this is an acquired infection.
- **Environmental risk factors:** residence in or exposure to mouse-infested dwellings, crowded urban housing, and inner-city/homeless settings with heightened ectoparasite exposure [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/), [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/).
- **Protective factors:** rodent and mite control; sealing dwellings; sanitation. No genetic protective variants known.
- **Gene–environment interactions:** **Not applicable** (no genetic component).

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Frequency / notes |
|---|---|---|---|
| Inoculation eschar (tache noire) | Physical skin sign | HP:0200042 (Skin ulcer) / eschar | Nearly universal; IHC-positive 16/16 eschars [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/) |
| Papulovesicular ("chickenpox-like") rash | Physical skin manifestation | HP:0000988 (Skin rash); HP:0200037 (Vesicle) | Generalized; IHC-positive 5/9 papulovesicles [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/) |
| Fever | Symptom | HP:0001945 (Fever) | Abrupt, near-universal [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/) |
| Headache | Symptom | HP:0002315 (Headache) | Common |
| Chills / myalgia | Symptom | HP:0025143 (Chills); HP:0003326 (Myalgia) | Common |
| Regional lymphadenopathy | Clinical sign | HP:0002716 (Lymphadenopathy) | Frequent |
| Hepatitis (elevated transaminases) | Laboratory / organ | HP:0200119 (Hepatitis) | Uncommon, self-resolving [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/) |

**Onset:** adult-onset in most reported cases (exposure-dependent, any age). **Severity:** mild to moderate. **Progression:** acute, self-limited, resolving over 2–3 weeks. **Quality-of-life impact:** minimal and transient; full recovery is the norm.

### 4. Genetic / Molecular Information

**Not applicable.** Rickettsialpox is an infectious disease with no causal human genes, pathogenic variants, modifier genes, epigenetic drivers, or chromosomal abnormalities. Molecular characterization pertains to the *pathogen* genome (SFG classification by *gltA*/citrate synthase phylogeny [PMID: 9103608](https://pubmed.ncbi.nlm.nih.gov/9103608/)), not the host.

### 5. Environmental Information

- **Environmental factors:** proximity to house-mouse populations and their mites in urban dwellings [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/).
- **Lifestyle factors:** living conditions with rodent infestation; inner-city/homeless exposure [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/).
- **Infectious agent:** *Rickettsia akari* (NCBITaxon:786), an obligate intracellular SFG bacterium [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1. Infected mite (Liponyssoides sanguineus) bites human skin
     └─ inoculates R. akari into the dermis
        ↓ leads to
2. R. akari attaches to and invades local vascular endothelial cells
   (obligate intracellular replication)
        ↓ results in
3. Direct endothelial cell damage + local dermal infection/necrosis
        ↓ leads to
4. Formation of the inoculation ESCHAR at the bite site
        │
        ├─ (branch, local) eschar = tache noire
        │
        ↓ concurrently, hematogenous / lymphatic dissemination
5. Systemic seeding of microvascular endothelium in skin and organs
        ↓ leads to
6. Endothelial barrier dysfunction + increased vascular permeability
   (mTORC1/2 activation; secretome/exosome changes — shown in SFG models,
    inferred for R. akari)
        ↓ results in
7. Small-vessel LYMPHOHISTIOCYTIC VASCULITIS
        ↓ produces
8. Clinical manifestations: fever, headache, myalgia, lymphadenopathy,
   and the disseminated PAPULOVESICULAR RASH
        │
        └─ (rare branch) hepatic endothelial involvement → self-limited hepatitis
```

- **Upstream events:** mite inoculation and endothelial invasion (steps 1–2).
- **Downstream events:** vasculitis, permeability, rash and systemic symptoms (steps 6–8).
- **Cell types (CL):** vascular endothelial cell (CL:0000115); macrophage/histiocyte and lymphocyte infiltrates in the perivascular lymphohistiocytic reaction.
- **Biological processes (GO):** GO:0044409 (entry into host); regulation of vascular permeability; inflammatory response; GO:0031929 (TOR signaling).
- **Molecular pathways:** mTOR (mTORC1/mTORC2) activation in infected endothelium [PMID: 33003310](https://pubmed.ncbi.nlm.nih.gov/33003310/).
- **Immune involvement:** perivascular lymphohistiocytic infiltration; innate and T-cell responses control rickettsial propagation (illustrated in the *R. parkeri* benidipine model, where impaired Ca²⁺/innate signaling converted sublethal to lethal infection [PMID: 38408129](https://pubmed.ncbi.nlm.nih.gov/38408129/)).
- **Proteomic/secretome markers:** the rickettsial protein RC0497 (putative N-acetylmuramoyl-L-alanine amidase) is secreted into the endothelial secretome and circulates during SFG infection [PMID: 31955791](https://pubmed.ncbi.nlm.nih.gov/31955791/); endothelial exosomes contribute functionally to infection [PMID: 33975935](https://pubmed.ncbi.nlm.nih.gov/33975935/).

*Note:* Steps 6–7's molecular detail is demonstrated primarily in related SFG species (*R. conorii*, *R. parkeri*) and is **inferred** to apply to *R. akari*, which shares the endothelial-tropism program [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/), [PMID: 32977742](https://pubmed.ncbi.nlm.nih.gov/32977742/).

### 7. Anatomical Structures Affected

- **Primary organ/tissue:** skin (UBERON:0002097), at the eschar and across the papulovesicular rash.
- **Vascular system:** small blood vessels / microvasculature (UBERON:0001981) — the primary target through endothelial infection.
- **Secondary organ involvement:** liver (UBERON:0002107) in rare hepatitis [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/); regional lymph nodes (UBERON:0000029).
- **Body systems:** integumentary and cardiovascular (microvascular); reticuloendothelial (lymphadenopathy).
- **Cell level:** vascular endothelial cells (CL:0000115) are the primary infected cell; perivascular macrophages/histiocytes and lymphocytes constitute the inflammatory infiltrate.
- **Subcellular (GO cellular component):** cytoplasm of endothelial cells (obligate intracellular replication); host plasma membrane at entry.
- **Localization / lateralization:** eschar is typically solitary and unilateral at the bite site; the rash is generalized/bilateral.

### 8. Temporal Development

- **Incubation:** ~9–14 days from mite bite to systemic symptoms [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/).
- **Onset pattern:** eschar develops first (subacute local lesion), then abrupt/acute onset of fever and constitutional symptoms; rash follows within 2–3 days.
- **Progression:** self-limited; resolves over ~2–3 weeks.
- **Course:** monophasic, non-relapsing; no chronic phase.
- **Remission:** spontaneous (even untreated) and accelerated by doxycycline.
- **Critical intervention window:** early empiric doxycycline shortens symptomatic course; because the disease is benign, timing is less critical than in Rocky Mountain spotted fever, but early treatment remains standard [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/).

### 9. Inheritance and Population

- **Inheritance:** **Not applicable** — infectious, non-heritable. No penetrance, expressivity, anticipation, mosaicism, founder-effect, consanguinity, or carrier-frequency parameters apply.
- **Epidemiology:** under-reported; not nationally notifiable in the US. Endemic in urban New York City and reported in other urban centers and internationally (seroepidemiologically in additional regions) [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/), [PMID: 16450784](https://pubmed.ncbi.nlm.nih.gov/16450784/). Precise prevalence/incidence figures are unreliable due to under-diagnosis.
- **Geographic distribution:** worldwide wherever the house mouse and its mite coexist with humans; classically urban.
- **Demographics:** linked to mouse-infested housing; heightened exposure in crowded inner-city and homeless populations [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/). No strong intrinsic sex or ethnic predisposition beyond exposure differences.

### 10. Diagnostics

- **Clinical criteria:** the triad of eschar + fever + papulovesicular rash with a compatible exposure history.
- **Histopathology/IHC (confirmatory):** immunohistochemistry of eschar or papulovesicle biopsy detects SFG rickettsiae (16/16 eschars, 5/9 papulovesicles) [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/); biopsy immunohistology is the gold-standard tissue confirmation per Walker [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/).
- **Serology (IFA):** four-fold IgG rise or single titer ≥1:64 reactive with *R. akari*; useful mainly in convalescence and cross-reactive across SFG [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/), [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/).
- **Molecular (PCR):** amplification/sequencing of *gltA*, *ompA*, *ompB*, and 17-kDa antigen genes from eschar/lesion material identifies and speciates SFG rickettsiae; *gltA* phylogeny confirms *R. akari* within SFG [PMID: 9103608](https://pubmed.ncbi.nlm.nih.gov/9103608/).
- **Laboratory findings:** may include mild transaminase elevation in hepatitis cases [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).
- **Genetic/omics testing:** **Not applicable** to host diagnosis.
- **Differential diagnosis:** chickenpox (varicella), cutaneous anthrax, other SFG rickettsioses, disseminated herpes, and vesicular eruptions [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/).

### 11. Outcome / Prognosis

- **Mortality:** ≈0%; no deaths attributed to rickettsialpox [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/), [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/).
- **Morbidity:** low; illness is self-limited with full recovery.
- **Complications:** rare, notably self-resolving hepatitis [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).
- **Recovery:** complete, with or without antibiotics; doxycycline accelerates resolution.
- **Prognostic factors:** benign regardless; prompt doxycycline shortens symptom duration.

### 12. Treatment

| Intervention | Class / mechanism | Suggested NCIT | Evidence |
|---|---|---|---|
| **Doxycycline** (first-line) | Tetracycline; inhibits bacterial 30S ribosome / protein synthesis | NCIT:C312 (Doxycycline) | [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/) |
| Tetracycline | Tetracycline antibiotic | NCIT:C842 | [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/) |
| Chloramphenicol | Broad-spectrum; 50S ribosome inhibitor (alternative) | NCIT:C242 | [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/) |

Empiric doxycycline should be started early on clinical suspicion and produces rapid defervescence [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/). No gene, cell, RNA, or immunotherapy is relevant. No pharmacogenomic modifiers are established. Supportive care (antipyretics) is adjunctive. Because the disease is self-limited, treatment mainly shortens symptomatic duration.

### 13. Prevention

- **Primary prevention (environmental):** rodent population control, mite/vector control with acaricides, sealing and sanitizing dwellings to eliminate house-mouse infestation [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/), [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).
- **Secondary prevention:** clinician awareness and prompt recognition/treatment; enhanced surveillance (the disease is under-reported) [PMID: 14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/).
- **Immunization:** **None** — no vaccine exists.
- **Public health:** integrated urban rodent/ectoparasite control and health education; One Health surveillance including companion-animal sentinels [PMID: 11394829](https://pubmed.ncbi.nlm.nih.gov/11394829/).
- **Genetic screening / counseling:** **Not applicable.**

### 14. Other Species / Natural Disease

- **Reservoir host:** house mouse *Mus musculus* (NCBITaxon:10090); the vector is the mite *Liponyssoides sanguineus* [PMID: 18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/).
- **Companion-animal exposure (sentinels):** dogs — natural *R. akari* infection confirmed by cross-absorption (6/7 samples) with 7.7% SFG seropositivity in 311 NYC dogs [PMID: 11394829](https://pubmed.ncbi.nlm.nih.gov/11394829/); cats — 14.9% *R. akari* seroprevalence among 170 US cats [PMID: 16434226](https://pubmed.ncbi.nlm.nih.gov/16434226/).
- **Zoonotic potential:** rickettsialpox is inherently a zoonosis (rodent reservoir, mite vector, human incidental host).
- **Comparative biology:** endothelial-tropism pathogenesis is conserved across SFG rickettsiae in mammalian hosts [PMID: 2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/), [PMID: 32977742](https://pubmed.ncbi.nlm.nih.gov/32977742/).

### 15. Model Organisms

Because rickettsialpox is infectious, "model organisms" refer to *infection models*, not genetic disease models. Murine models of SFG rickettsiosis (e.g., *R. conorii* and *R. parkeri* in mice) recapitulate endothelial infection, vascular permeability, and disease severity, and have been used to test mechanistic interventions — for example, the calcium-channel blocker benidipine converted sublethal to lethal *R. parkeri* infection by impairing innate immunity [PMID: 38408129](https://pubmed.ncbi.nlm.nih.gov/38408129/). Primary human umbilical vein endothelial cells (HUVEC) serve as the standard *in vitro* model for endothelial infection, secretome, and mTOR signaling studies [PMID: 31955791](https://pubmed.ncbi.nlm.nih.gov/31955791/), [PMID: 33003310](https://pubmed.ncbi.nlm.nih.gov/33003310/). These models capture the shared SFG endothelial pathogenesis but are largely developed for more virulent species; *R. akari*-specific models are sparse, and its intrinsically mild phenotype limits severity-focused modeling.

---

## Mechanistic Model / Interpretation

The disease can be read as a single mechanistic story with one local branch and one systemic branch, both flowing from a single lesion — endothelial infection.

| Stage | Location | Key event | Manifestation |
|---|---|---|---|
| Inoculation | Skin (bite site) | Mite deposits *R. akari* | (none yet) |
| Local infection | Dermal microvasculature | Endothelial invasion + necrosis | **Eschar** |
| Dissemination | Blood / lymph | Hematogenous spread | Incubation → fever onset |
| Systemic infection | Microvascular endothelium (skin, organs) | Barrier dysfunction, ↑permeability, mTOR activation | Fever, headache, myalgia |
| Vasculitis | Small vessels | Lymphohistiocytic perivascular infiltrate | **Papulovesicular rash** |
| Rare extension | Hepatic endothelium | Focal inflammation | Self-limited hepatitis |
| Resolution | Systemic | Immune clearance ± doxycycline | Recovery in 2–3 weeks |

The unifying insight is that *R. akari* is a comparatively **avirulent** member of a virulent family. It uses the same endothelial-tropism program as *R. conorii* and *R. rickettsii* — invade endothelium, damage it, increase vascular permeability, trigger small-vessel vasculitis — but produces a mild, self-limited disease with near-zero mortality. The clinical hallmarks (eschar + papulovesicular rash) map directly onto the local and systemic branches of endothelial infection. This makes rickettsialpox both a diagnostic mimic (chickenpox, cutaneous anthrax) and an informative "benign end" of the SFG severity spectrum.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [14676069](https://pubmed.ncbi.nlm.nih.gov/14676069/) | Increased detection of rickettsialpox in a NYC hospital (2001 anthrax era) | Core human case series: IHC diagnosis (16/16 eschars, 5/9 papulovesicles), serology criteria, endemicity, differentials, under-reporting |
| [18171106](https://pubmed.ncbi.nlm.nih.gov/18171106/) | Hepatitis in association with rickettsialpox | Etiology/vector/reservoir statement; rare self-limited hepatitis |
| [2677080](https://pubmed.ncbi.nlm.nih.gov/2677080/) | Rickettsioses of the spotted fever group around the world (Walker review) | Endothelial-invasion mechanism; eschar; biopsy IHC diagnosis; doxycycline/tetracycline/chloramphenicol treatment |
| [32977742](https://pubmed.ncbi.nlm.nih.gov/32977742/) | Comparative transcriptomics of *R. conorii* | Microvascular endothelial tropism / endothelial damage (SFG-wide, inferred to *R. akari*) |
| [33003310](https://pubmed.ncbi.nlm.nih.gov/33003310/) | mTOR activation in infected human endothelial cells | Downstream signaling; vascular inflammation as core SFG feature |
| [31955791](https://pubmed.ncbi.nlm.nih.gov/31955791/) | Endothelial secretome proteomics (RC0497) | Secretome/barrier dysfunction; candidate diagnostic marker |
| [33975935](https://pubmed.ncbi.nlm.nih.gov/33975935/) | Endothelial exosome in rickettsial infection | Barrier dysfunction/edema mechanism |
| [38408129](https://pubmed.ncbi.nlm.nih.gov/38408129/) | Benidipine impairs innate immunity (mouse *R. parkeri*) | Immune control; infection model relevance |
| [11394829](https://pubmed.ncbi.nlm.nih.gov/11394829/) | *R. akari* serology in NYC dogs | One Health ecology; natural canine infection (6/7 cross-absorbed) |
| [16434226](https://pubmed.ncbi.nlm.nih.gov/16434226/) | Vector-borne pathogen serology in cats | 14.9% feline *R. akari* seroprevalence |
| [16450784](https://pubmed.ncbi.nlm.nih.gov/16450784/) | Rickettsial antibody survey, Papua New Guinea | SFG/*R. akari* exposure beyond classic foci |
| [17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/) | Arthropod-borne diseases in homeless | Rodent-mite exposure pathway; prevention rationale |
| [9103608](https://pubmed.ncbi.nlm.nih.gov/9103608/) | Citrate synthase (*gltA*) phylogeny | Classification of *R. akari* within SFG |

Evidence types span human clinical case series (14676069, 18171106), authoritative reviews (2677080), in vitro/in vivo mechanistic studies of related SFG species (32977742, 33003310, 31955791, 33975935, 38408129), seroepidemiology (11394829, 16434226, 16450784), and molecular phylogeny (9103608).

---

## Limitations and Knowledge Gaps

1. **Mechanistic detail is inferred, not *R. akari*-specific.** The endothelial-invasion, permeability, mTOR, secretome, and exosome findings come from *R. conorii*/*R. parkeri* models. While the shared SFG program strongly supports extrapolation, direct *R. akari* molecular studies are sparse.
2. **Epidemiology is unreliable.** The disease is not notifiable and is under-diagnosed; no dependable prevalence/incidence rates exist, and reported case counts track awareness (e.g., the post-2001 detection spike).
3. **Case-series bias.** Much of the human clinical data derives from a single NYC hospital series, limiting generalizability of phenotype frequencies.
4. **Sparse international quantitative data.** Global distribution is supported qualitatively and serologically, but few systematic surveys quantify burden outside New York.
5. **No modern therapeutic trials.** Treatment recommendations rest on decades of clinical experience and reviews rather than randomized trials (ethically unnecessary given benignity, but formally a gap).
6. **Not-applicable sections.** Genetic, inheritance, and pharmacogenomic sections are empty by nature; this is correct for an infection, not a data deficiency.

---

## Proposed Follow-up Experiments / Actions

1. **Direct *R. akari* endothelial-infection studies.** Perform transcriptomic/proteomic and mTOR-pathway characterization in HUVEC infected with *R. akari* to confirm (rather than infer) the shared SFG mechanism and to explain its low virulence.
2. **RC0497 (or ortholog) as a rapid diagnostic.** Test whether the *R. akari* homolog of the secreted amidase RC0497 [PMID: 31955791](https://pubmed.ncbi.nlm.nih.gov/31955791/) is detectable in acute rickettsialpox sera to enable early, species-agnostic point-of-care diagnosis.
3. **PCR/next-gen sequencing standardization.** Validate a multiplex *gltA/ompA/ompB*/17-kDa PCR panel on eschar swabs and lesion capillary blood for early confirmation, reducing reliance on convalescent serology.
4. **Sentinel surveillance via companion animals.** Use canine/feline seroprevalence as an early-warning sentinel for urban *R. akari* activity and to map geographic footprint [PMID: 11394829](https://pubmed.ncbi.nlm.nih.gov/11394829/), [PMID: 16434226](https://pubmed.ncbi.nlm.nih.gov/16434226/).
5. **Burden quantification.** Conduct multi-city seroprevalence surveys in humans in housing with documented mouse infestation to estimate true incidence and correct for under-reporting.
6. **Vector-control evaluation.** Prospectively measure the effect of integrated rodent + acaricide interventions on human case counts in endemic urban zones.

---

*Report compiled from an autonomous 5-iteration investigation: 8 confirmed findings, 46 papers reviewed. Rickettsialpox is treated throughout as an infectious, non-heritable zoonosis; genetic/inheritance template sections are marked Not Applicable accordingly.*


## Artifacts

- [OpenScientist final report](Rickettsialpox-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rickettsialpox-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCBITaxon:10090` (2 mentions) - the report calls it "Mus musculus", "Reservoir host:** house mouse *Mus musculus"; NCBITaxon calls it **Mus musculus**
- `UBERON:0001981` (1 mention) - the report calls it "Vascular system:** small blood vessels / microvasculature"; UBERON calls it **blood vessel**
- `UBERON:0002107` (1 mention) - the report calls it "Secondary organ involvement:** liver"; UBERON calls it **liver**
- `NCIT:C842` (1 mention) - the report calls it "Tetracycline antibiotic"; NCIT calls it **Stanozolol**
- `NCIT:C242` (1 mention) - the report calls it "Broad-spectrum; 50S ribosome inhibitor (alternative)"; NCIT calls it **Anti-Androgen**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:786` (4 mentions) - the report calls it "Rickettsia akari", "Infectious agent:** *Rickettsia akari"; NCBITaxon calls it **Rickettsia akari**
- `HP:0200119` (1 mention) - the report calls it "Hepatitis"; HP calls it **Acute hepatitis**
- `CL:0000115` (2 mentions) - the report calls it "Cell level:** vascular endothelial cells"; CL calls it **endothelial cell**
- `GO:0044409` (1 mention) - the report calls it "entry into host"; GO calls it **symbiont entry into host**, and lists "entry into host" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Primary organ/tissue:** skin"; UBERON calls it **skin of body**, and lists "entire skin" among its other names
- `NCIT:C312` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Bleomycin Sulfate**, and lists "BleMomycine" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:786` - called "Rickettsia akari", "Infectious agent:** *Rickettsia akari"
- `NCBITaxon:10090` - called "Mus musculus", "Reservoir host:** house mouse *Mus musculus"