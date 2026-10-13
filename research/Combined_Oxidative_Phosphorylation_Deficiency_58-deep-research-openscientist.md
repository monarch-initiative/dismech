---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-13T20:15:47.847399'
end_time: '2026-10-13T20:31:31.700468'
duration_seconds: 943.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Deficiency 58
  mondo_id: MONDO:0957537
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
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 75
  verified: 73
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 13
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0957537
    reported_labels:
    - MONDO
    ontology_label: combined oxidative phosphorylation deficiency 58
  - term_id: HP:0004887
    reported_labels:
    - 1/7, severe end
    ontology_label: Respiratory failure requiring assisted ventilation
  - term_id: UBERON:0002488
    reported_labels:
    - neuromuscular junction
    ontology_label: helix of outer ear
  labels_variant: 5
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Deficiency_58-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Deficiency_58-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 58
- **MONDO ID:** MONDO:0957537 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 58** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency 58 (COXPD58) — Comprehensive Disease Characteristics Report

**Disease:** Combined Oxidative Phosphorylation Deficiency 58 (COXPD58)
**MONDO:** MONDO:0957537 · **OMIM (phenotype):** 620451 · **Causal gene:** *TEFM*
**Report date:** 2026-10-13 · **Evidence base:** small case series + functional/structural studies

---

## Summary (Answer to the Research Question)

Combined Oxidative Phosphorylation Deficiency 58 (COXPD58) is an **ultra-rare autosomal recessive mitochondrial disease** caused by **biallelic loss-of-function/hypomorphic variants in *TEFM*** (Transcription Elongation Factor, Mitochondrial; chr17q11.2). TEFM is the nuclear‑encoded elongation factor that increases the processivity of the mitochondrial RNA polymerase POLRMT; its deficiency **reduces promoter‑distal mitochondrial RNA transcripts**, lowering synthesis of mtDNA‑encoded OXPHOS subunits and producing a **combined (complex I + IV) respiratory‑chain deficiency**. Clinically it is a **childhood‑onset, variable mitochondrial encephalomyopathy** with near‑universal lactic acidosis, hypotonia, intellectual disability, ophthalmologic/ocular‑motility signs and seizures, and — in the myopathic subset — a **treatable neuromuscular‑junction (NMJ) transmission defect** that can mimic a congenital myasthenic syndrome (Van Haute et al., 2023, *Brain*, PMID 36823193).

**Evidence-source note:** Content derives from **aggregated disease-level resources** (OMIM/MedGen, HPO, UniProt, gnomAD, ClinVar, HomoloGene) and from **individual-patient primary literature** (a 7-patient defining cohort plus isolated case reports). No large registries, natural-history cohorts, or disease-level omics datasets exist for this very recently defined (2023) entity.

---

## 1. Disease Information

**Overview.** COXPD58 belongs to the clinically and genetically heterogeneous group of "combined oxidative phosphorylation deficiencies" — nuclear‑gene mitochondrial disorders in which **more than one respiratory‑chain complex is deficient**. COXPD58 specifically results from impaired **mitochondrial transcription elongation**. MedGen/OMIM definition: *"an autosomal recessive disorder characterized by a wide range of clinical presentations including neonatal lactic acidosis, epileptic encephalopathy, developmental delay and impaired intellectual development with nonspecific changes on brain MRI, or mitochondrial myopathy with a treatable neuromuscular transmission defect (Van Haute et al., 2023)."*

**Key identifiers.**
| Resource | ID |
|---|---|
| MONDO | MONDO:0957537 |
| OMIM (phenotype) | 620451 |
| OMIM (gene *TEFM*) | 616422 |
| UMLS | C5830641 |
| MedGen | 1841277 |
| GARD | 0026857 |
| HGNC (gene) | HGNC:26223 |
| NCBI Gene | 79736 |
| Ensembl | ENSG00000172171 |
| Orphanet | *No dedicated ORPHAcode as of 2026* |
| ICD-10 / ICD-11 | No specific code; maps to mitochondrial disease (ICD-10 E88.4x "mitochondrial metabolism disorders"; ICD-11 5C53.1 / 8C70-range) |
| MeSH | No specific descriptor; related: "Mitochondrial Diseases" (D028361), "OXPHOS diseases" |

**Synonyms / alternative names:** COXPD58; Combined oxidative phosphorylation deficiency 58; Combined oxidative phosphorylation defect type 58; *TEFM*-related mitochondrial disease; *TEFM*-associated neurological disorder; mitochondrial transcription elongation factor deficiency.

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound‑heterozygous) pathogenic variants in ***TEFM***. The disorder is **monogenic and Mendelian (autosomal recessive)**; it is **not infectious or environmentally caused**.

**Genetic risk factors.**
- **Causal variants:** rare biallelic *TEFM* variants (missense, and loss-of-function alleles; large 17q11.2 deletions encompassing *TEFM* are also recorded in ClinVar).
- **Reported disease variant:** `NM_024683.4(TEFM):c.469C>G (p.Pro157Ala)` — recurrent, observed in an adolescent male and in two Indian siblings; a possible **population‑specific (South Asian) variant** (Adarsha et al., 2025, PMID 40272035).
- **Susceptibility/modifier loci:** none established.
- **Consanguinity** increases risk of homozygosity (reported in some families), as for most recessive mitochondrial disorders.

**Environmental risk factors / protective factors / gene–environment interactions:** **None identified.** As a Mendelian OXPHOS disorder, there are no established environmental triggers, lifestyle risk factors, protective alleles, or GxE interactions. *Inferred, by analogy to other mitochondrial diseases:* physiological stressors (intercurrent infection, fasting, fever, mitochondrial-toxic drugs such as valproate/aminoglycosides) could precipitate metabolic decompensation, but this has not been specifically documented for COXPD58.

---

## 3. Phenotypes

Phenotype frequencies below are from the HPO annotation of OMIM:620451 (source cohort PMID 36823193; denominators reflect the small cohort). **Onset:** childhood in the majority (HP:0011463, 5/7), with neonatal (HP:0003623, 1/7) and infantile (HP:0003593, 1/7) presentations at the severe end. **Severity:** variable (mild treatable myopathy → severe neonatal lactic acidosis/epileptic encephalopathy). **Progression:** chronic; may be progressive (e.g., optic atrophy, spasticity) or relatively stable; episodic decompensations possible.

**Laboratory abnormalities (type: laboratory):**
- **Increased circulating lactate — HP:0002151 — 7/7 (100%)** (hallmark biomarker; CHEBI:16651 L-lactate)
- Lacticaciduria — HP:0003648
- Hyperalaninemia — HP:0003348 (CHEBI:16977 L-alanine)
- Hypoglycemia — HP:0001943
- Hyperprolinemia — HP:0008358
- Elevated alkaline phosphatase — HP:0003155
- Elevated brain lactate on MR spectroscopy — HP:0012707

**Nervous system (signs/symptoms):**
- Intellectual disability — HP:0001249 — 5/6
- Global developmental delay — HP:0001263; Delayed speech — HP:0000750
- Gait disturbance — HP:0001288 — 4/7; Gait ataxia — HP:0002066 / Ataxia — HP:0001251
- Seizures: Bilateral tonic-clonic — HP:0002069 (2/6); **Epilepsia partialis continua — HP:0012847**; Myoclonus — HP:0001336
- Appendicular spasticity — HP:0034353 (2/6); upper motor neuron signs
- CNS demyelination — HP:0007305 (2/2); Cerebellar atrophy — HP:0001272; Thin corpus callosum — HP:0033725; Gliosis — HP:0002171; Microcephaly — HP:0000252
- Exaggerated startle — HP:0002267
- **Peripheral neuropathy — HP:0009830 — 0/7 (notably absent)**

**Ophthalmologic (signs):** Ptosis — HP:0000508 (3/6); Nystagmus — HP:0000639 (3/6); Strabismus — HP:0000486; **Ophthalmoparesis — HP:0000597** (incl. lateral rectus/abducens palsy); Optic atrophy — HP:0000648 (2/6); Reduced visual acuity/visual loss — HP:0007663/HP:0000572; Visual fixation instability — HP:0025405.

**Musculature (signs + cellular/biopsy):** Axial hypotonia — HP:0008936 (5/7); Appendicular hypotonia — HP:0012389; Muscle weakness — HP:0001324; Muscle fatigability (myasthenic-like); **EMG decremental response of CMAP to repetitive nerve stimulation — HP:0003403** (NMJ transmission defect); **Ragged-red fibers — HP:0003200 (2/3)**.

**Cellular / biochemical phenotype:** **Decreased mitochondrial complex I activity — HP:0011923 (3/3)**; Decreased complex IV activity — HP:0008347 (2/2) → confirms a **combined** OXPHOS defect.

**Other:** Feeding difficulties — HP:0011968; Vomiting — HP:0002013; Respiratory failure requiring ventilation — HP:0004887 (1/7, severe end); dysmorphic features (epicanthus HP:0000286, low-set ears HP:0000369, prominent nasal bridge) in some.

**Quality-of-life impact:** not formally measured (no EQ-5D/SF-36/PROMIS data). Expected substantial impact via intellectual disability, motor impairment/ataxia, epilepsy, and visual loss; the treatable NMJ fatigability may improve with therapy.

---

## 4. Genetic / Molecular Information

**Causal gene:** ***TEFM*** (HGNC:26223; NCBI Gene 79736; Ensembl ENSG00000172171; gene OMIM 616422). Locus **17q11.2**, GRCh38 chr17:30,897,336–30,906,238. Protein: **UniProt Q96QE5**, **360 aa**, with an N‑terminal **mitochondrial targeting/transit peptide (aa 1–35)**.

**Pathogenic variants.**
- **Type/class:** missense (e.g., p.Pro157Ala) and loss-of-function alleles; **large contiguous-gene 17q11.2 deletions** spanning *TEFM* are recorded (ClinVar) — e.g., multi-Mb deletions classified Pathogenic.
- **Classification:** ClinVar holds **~130 *TEFM* records**, predominantly **VUS** (≈32/50 sampled) and likely benign (5), with **2 Pathogenic + 2 Likely pathogenic** (several "Pathogenic" being large deletions). Variant interpretation remains immature; functional RNA evidence (reduced promoter-distal transcripts) supports pathogenicity.
- **Allele frequency / constraint (gnomAD):** *TEFM* is **not LoF-constrained** — pLI = 0.002, observed/expected LoF = 14/22.96 (**oe_lof = 0.61**, 90% CI 0.40–0.95), LOEUF in the tolerant range; missense Z = 0.82. This LoF tolerance explains the **recessive** mechanism (heterozygous carriers are healthy) and the disease's rarity.
- **Origin:** **germline** (not somatic in this disorder). *(Note: somatically, TEFM is over-expressed in several cancers — see §14 caveat.)*
- **Functional consequence:** **loss of function** (reduced transcription-elongation processivity); no gain-of-function or dominant-negative mechanism described for the disease.

**Modifier genes / epigenetics:** none established. **Chromosomal abnormalities:** 17q11.2 deletions removing *TEFM* (and neighboring genes, including the *NF1* region) can contribute — relevant for CMA/deletion analysis.

**Ontology:** gene product GO molecular function **GO:0003711** (transcription elongation factor activity), **GO:0003723** (RNA binding); MONDO:0957537.

---

## 5. Environmental Information

**Not applicable.** COXPD58 is a monogenic disorder with **no environmental, lifestyle, toxic, or infectious etiology**. No occupational/pollution exposures, dietary factors, or pathogens are implicated. (As a general mitochondrial-disease precaution, avoidance of mitochondrial-toxic agents — e.g., valproate, aminoglycosides, certain antiretrovirals — is prudent but not COXPD58-specific.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *TEFM* variants** reduce the amount or function of the mitochondrial transcription elongation factor (loss of function). *(demonstrated: patient muscle/fibroblasts)*
2. Reduced TEFM **leads to** loss of its "sliding-clamp"/processivity support of POLRMT during mtDNA transcription elongation. *(demonstrated in vitro; Agaronyan 2015, Hillen 2017)*
3. Impaired processivity **results in** premature termination so that **promoter‑distal portions of the polycistronic transcripts are under-produced** → reduced promoter-distal mt-RNA. *(demonstrated in patients; Van Haute 2023)*
4. Reduced mt-mRNA/mt-rRNA **leads to** decreased synthesis of **mtDNA-encoded OXPHOS subunits** (complex I ND subunits, complex III cytB, complex IV COI–III, complex V ATP6/8). *(inferred from biochemistry)*
5. This **results in** a **combined respiratory-chain deficiency** (measured: ↓complex I 3/3, ↓complex IV 2/2) and impaired assembly. *(demonstrated)*
6. Deficient OXPHOS **leads to** reduced ATP production and a shift to anaerobic glycolysis → **lactic acidosis / hyperalaninemia** (universal biomarker). *(demonstrated)*
7. Bioenergetic failure in **high-energy-demand tissues** (CNS neurons, cerebellum, skeletal muscle, the neuromuscular junction, optic nerve) **results in** the clinical phenotype. *(demonstrated/inferred)*
   - **Branch A (CNS):** neuronal/oligodendrocyte energy failure → developmental delay, intellectual disability, seizures/epilepsia partialis continua, ataxia, CNS demyelination, cerebellar/callosal atrophy.
   - **Branch B (muscle/NMJ):** myopathy with ragged-red fibers **and** a presynaptic/postsynaptic **neuromuscular transmission defect** (decremental RNS) → fatigable weakness, ptosis, ophthalmoparesis — **treatable**, CMS-like.
   - **Branch C (eye):** optic-nerve/retinal energy failure → optic atrophy, reduced acuity.
8. In parallel, because TEFM governs the **transcription↔replication switch** and RNA processing, its loss may also perturb **mtDNA maintenance/copy number and RNA maturation** (Jiang 2019; Matsuda 2025). *(mechanistically inferred for patients)*

### Supporting detail
- **Molecular pathway:** mitochondrial gene expression / OXPHOS (Reactome "Mitochondrial transcription"; KEGG oxidative phosphorylation map00190). Upstream machinery: POLRMT, TFAM, TFB2M (initiation) → **TEFM (elongation)**; TEFM is recruited after release of initiation factors (Herbine 2025, PMID 40712587). Anti-termination at CSBII prevents G-quadruplex/replication-primer formation (Hillen 2017, PMID 29033127; Agaronyan 2015, PMID 25635099).
- **Protein dysfunction:** loss of function of the dimeric pseudonuclease-fold elongation factor; structures in PDB 5OL8/5OL9/5OLA, 8U8U/8U8V, 9BDC/9BDD/9MNA.
- **Cellular processes:** energy metabolism failure; secondary oxidative stress possible; no autoimmune/inflammatory mechanism.
- **Metabolic changes:** elevated lactate/pyruvate, alanine, proline; episodic hypoglycemia.
- **Immune involvement:** none.
- **Tissue damage:** bioenergetic/oxidative; gliosis and demyelination documented.
- **Molecular profiling (patients):** transcriptomic signature = **reduced promoter-distal mtRNA** (northern/RNA-seq/qPCR in muscle and fibroblasts); respirometry/enzymology shows combined CI+CIV deficiency.

**Ontology suggestions.** BP: GO:1903109 (positive regulation of mitochondrial transcription), GO:0006390/GO:0006392 (mitochondrial transcription/elongation), GO:0002082 (regulation of oxidative phosphorylation), GO:0006119 (oxidative phosphorylation), GO:0006264 (mtDNA replication). MF: GO:0003711, GO:0003723. CC: GO:0005759 (mitochondrial matrix), GO:0042645 (mitochondrial nucleoid), GO:1990904 (ribonucleoprotein complex), GO:0005739 (mitochondrion). Cell types (CL): neuron CL:0000540, cerebellar Purkinje cell CL:0000121, skeletal muscle fiber CL:0000188, oligodendrocyte CL:0000128. CHEBI: L-lactate CHEBI:16651, L-alanine CHEBI:16977, ATP CHEBI:30616.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **brain** (UBERON:0000955) — cerebrum, **cerebellum** (UBERON:0002037), **corpus callosum** (UBERON:0002336), white matter; **skeletal muscle** (UBERON:0001134); **eye/optic nerve** (UBERON:0000941). Body systems: **nervous** and **musculoskeletal** predominate; **neuromuscular junction** (UBERON:0002488) specifically involved.
- **Secondary/other:** respiratory (ventilatory failure in severe cases), gastrointestinal (feeding difficulties, vomiting); systemic metabolic (lactic acidosis). No consistent cardiac, hepatic, renal, or endocrine involvement reported (distinguishing from some other COXPDs).
- **Tissue/cell level:** nervous tissue (neurons, oligodendrocytes/myelin), muscle tissue (myofibers with ragged-red change). CL terms: CL:0000540 (neuron), CL:0000128 (oligodendrocyte), CL:0000188 (skeletal muscle fiber), CL:0000121 (Purkinje cell).
- **Subcellular:** **mitochondrion** — matrix and **nucleoid** (GO:0005759, GO:0042645). This is fundamentally a nucleoid/mitochondrial-matrix gene-expression defect.
- **Localization/lateralization:** **bilateral/symmetric** CNS and ocular involvement typical; muscle involvement generalized.

---

## 8. Temporal Development

- **Onset:** congenital-to-childhood; **neonatal** (lactic acidosis/encephalopathy) at the severe end, **infantile**, and most commonly **childhood** onset. Pattern: subacute/chronic; may present acutely with neonatal lactic acidosis.
- **Progression:** chronic lifelong; variable rate — some features progressive (optic atrophy, spasticity, white-matter change), others relatively static (developmental). Disease course can include **episodic metabolic decompensation**; epilepsia partialis continua indicates an active encephalopathic process.
- **Patterns:** no spontaneous remission of the underlying disorder; the **NMJ transmission defect may improve with treatment** (treatment-induced symptomatic improvement). **Critical period:** early recognition of the treatable myasthenic component offers a window for symptomatic benefit; early supportive management of lactic acidosis/seizures is important.

---

## 9. Inheritance and Population

- **Epidemiology:** **ultra-rare.** The literature comprises a **7-patient defining cohort** (Van Haute 2023) plus isolated reports (Adarsha 2025; two Indian siblings) — **well under ~15 reported individuals worldwide.** No prevalence/incidence estimates; **no Orphanet prevalence class.**
- **Inheritance:** **autosomal recessive** (biallelic). Consistent with gnomAD LoF-tolerance (carriers unaffected).
- **Penetrance:** presumed high/complete in biallelic LoF, but **variable expressivity** is prominent (neonatal-lethal encephalopathy ↔ treatable myopathy). Too few cases for formal penetrance estimates.
- **Anticipation:** not applicable (not a repeat-expansion disorder). **Germline mosaicism:** not reported.
- **Founder effects / population variants:** **p.Pro157Ala (c.469C>G)** recurs in individuals of **Indian/South Asian** ancestry — a candidate population-specific variant (PMID 40272035).
- **Consanguinity:** contributes (homozygous variants in consanguineous families).
- **Carrier frequency:** not established; expected very low given rarity. **Sex ratio:** no sex bias expected (autosomal); cohorts too small to assess. **Age distribution:** pediatric predominance.

---

## 10. Diagnostics

**Clinical/laboratory tests.**
- **Blood/CSF lactate** (↑, LOINC 2524-7 lactate; universal), **plasma amino acids** (↑alanine, ↑proline), urine organic acids (lactic aciduria), glucose (episodic hypoglycemia).
- **Muscle biopsy:** histochemistry showing **ragged-red fibers**, possible COX-deficient fibers; **respiratory-chain enzymology** demonstrating **combined complex I + IV deficiency** (± others).
- **Electrophysiology:** **repetitive nerve stimulation (RNS)** showing a **decremental CMAP response** (NMJ defect) — a key, treatable clue; EMG may show myopathic features; note RNS can be **normal** in some patients (Adarsha 2025), so a normal RNS does not exclude the disorder. EEG for seizures.
- **Imaging:** brain **MRI** — nonspecific changes, white-matter/demyelinating signal, cerebellar atrophy, thin corpus callosum; **MR spectroscopy** — elevated brain lactate.

**Genetic testing (confirmatory).**
- **Whole-exome (WES)** or **whole-genome sequencing (WGS)** is the mainstay — *TEFM* is included on broad **mitochondrial/OXPHOS nuclear-gene panels** and neurometabolic panels; **GeneMatcher** enabled cohort assembly.
- **Single-gene / targeted testing** of *TEFM* once suspected (e.g., recurrent p.Pro157Ala in South Asian probands).
- **Chromosomal microarray (CMA)/deletion analysis** to detect **17q11.2 deletions** encompassing *TEFM* (and to interpret apparent hemizygosity + a second variant).
- **mtDNA testing:** typically **normal** (this is a nuclear-gene disorder) — useful to exclude primary mtDNA disease.
- **Functional confirmation:** demonstration of **reduced promoter-distal mtRNA** in fibroblasts/muscle supports VUS reclassification.

**Clinical criteria / differential diagnosis.** No disease-specific criteria; diagnosis follows **mitochondrial-disease** frameworks plus molecular confirmation. **Differential diagnosis:** other combined OXPHOS deficiencies and mitochondrial translation/transcription defects (e.g., *POLRMT*, *TFAM*, *MTERF*, mt-aminoacyl-tRNA synthetases), **Leigh syndrome**, **congenital myasthenic syndromes** (because of the treatable NMJ defect; distinguished by combined OXPHOS deficiency + lactate), **SLC25A1**-related CMS, and primary mtDNA disorders (MELAS/Leigh). The combination of **lactic acidosis + combined CI/CIV deficiency + a myasthenic RNS decrement** is distinctive.

**Screening.** Not on newborn-screening panels. **Cascade carrier testing** of relatives and **prenatal/preimplantation testing** are feasible once familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** no formal survival statistics. Prognosis is **severity-dependent**: the **neonatal lactic-acidosis/epileptic-encephalopathy** presentation carries high morbidity/mortality (one patient required assisted ventilation), whereas the **myopathic/NMJ** presentation is comparatively milder and partly treatable.
- **Morbidity/disability:** substantial in encephalopathic patients — intellectual disability, epilepsy, ataxia/spasticity, visual loss; motor fatigability in the myopathic subset.
- **QoL measures:** none formally reported.
- **Complications:** status epilepticus/epilepsia partialis continua, metabolic (lactic) crises, respiratory failure, feeding difficulty/failure to thrive, progressive optic atrophy.
- **Recovery:** the **NMJ transmission defect may respond** to symptomatic treatment; the OXPHOS defect itself is not reversible.
- **Prognostic factors:** age/severity at onset (neonatal worst), degree of respiratory/encephalopathic involvement, and presence of a treatable NMJ component. **Prognostic biomarkers:** lactate levels and residual respiratory-chain enzyme activity (inferred).

---

## 12. Treatment

**No curative or disease-specific therapy exists.** Management is supportive and, where applicable, targets the treatable NMJ defect.

- **Targeting the NMJ transmission defect (the key actionable feature):** managed as in **congenital myasthenic syndromes** — **acetylcholinesterase inhibitors (pyridostigmine; NCIT C739)** and consideration of **β2-adrenergic agonists (salbutamol/albuterol; NCIT C28840)** / 3,4-diaminopyridine depending on the synaptic defect. *(Extrapolated from the "treatable neuromuscular transmission defect" description and CMS practice; formal response data in COXPD58 are limited.)*
- **Supportive mitochondrial care (NCIT "Supportive Care" C15277):** antiseizure medications for epilepsy (**avoid valproate** where possible); management of lactic acidosis; nutritional support/feeding assistance; treatment of intercurrent illness; avoidance of mitochondrial-toxic drugs.
- **Rehabilitation:** physical, occupational, and speech therapy (NCIT C15615 Physical Therapy; C15399 Occupational Therapy); low-vision support; developmental/educational support.
- **Empiric "mitochondrial cocktail":** riboflavin (CHEBI/NCIT vitamin B2), **coenzyme Q10** (NCIT C1097), L-carnitine, thiamine, antioxidants — **used empirically, unproven efficacy.**
- **Advanced therapeutics:** **no** gene therapy, cell therapy, RNA therapy, targeted therapy, or immunotherapy exists or is in trials for COXPD58 (no ClinicalTrials.gov entries identified). Gene replacement is a theoretical future avenue (nuclear-gene, LoF mechanism is conceptually tractable).
- **Pharmacogenomics:** none specific; general mitochondrial-disease drug-avoidance precautions apply.
- **Personalized approach:** recognizing the **treatable myasthenic component** is the principal genotype/phenotype-guided intervention.

---

## 13. Prevention

- **Primary prevention:** not possible (genetic). **Genetic counseling** for recessive 25% recurrence risk; **carrier testing** of at-risk relatives; **prenatal diagnosis / preimplantation genetic testing (PGT-M)** once familial variants are known.
- **Secondary prevention:** early molecular diagnosis (WES/WGS) enables early supportive care and a trial of CMS-type therapy for the NMJ defect; early seizure and metabolic management.
- **Tertiary prevention:** prevent complications — seizure control, nutritional/respiratory support, avoidance of mitochondrial toxins and fasting, low-vision and rehabilitation services.
- **Immunization / public-health / environmental / behavioral measures:** not applicable (non-communicable, non-environmental). Routine childhood vaccination and infection prevention are prudent to avoid metabolic decompensation.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (HomoloGene 11657):** *TEFM* is **highly conserved across vertebrates** — mouse *Tefm* (NCBI Gene 68550; NCBI:txid10090), rat *Tefm* (287554; txid10116), **zebrafish *tefm* (566236; txid7955)**, *Xenopus tropicalis* (100485913; txid8364), dog (480615; txid9615), cow (534204; txid9913), rhesus macaque (713684; txid9544), chimpanzee (454560; txid9598).
- **Natural disease / breeds (OMIA/VBO):** **none catalogued** — no naturally occurring *TEFM* disease in companion animals or livestock; no VBO breed associations. Veterinary relevance: nil to date.
- **Comparative biology:** mechanism (mitochondrial transcription elongation) is **evolutionarily conserved**, making cross-species models informative (see §15).
- **Transmission:** not applicable (genetic; **no zoonotic potential**).

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*, txid7955):** **`tefm` morpholino knockdown** in embryos produced **neuromuscular junction abnormalities and abnormal mitochondrial function**, directly recapitulating the human NMJ/bioenergetic phenotype and strengthening causality (Van Haute 2023, PMID 36823193). *In vivo vertebrate model; good phenotype recapitulation of the NMJ component; limitation: transient knockdown, not a stable genetic model.*
- **Mouse (*Mus musculus*, txid10090):** *Tefm* has been studied in vivo/at the cellular level to establish its role in **transcription elongation and RNA processing** (Jiang 2019, PMID 31036713, Larsson lab). *Mammalian model of TEFM function; a dedicated COXPD58 disease-model mouse recapitulating the full clinical syndrome is not yet reported; constitutive loss is expected to be severe given essential OXPHOS function.*
- **Cellular / in vitro models:** **patient-derived primary fibroblasts and skeletal-muscle** showing reduced promoter-distal mtRNA and combined OXPHOS deficiency (PMID 36823193); cultured cells and reconstituted in vitro transcription systems (POLRMT/TFAM/TFB2M/TEFM) for mechanism and structural studies (PMIDs 25635099, 29033127, 40712587).
- **Resources:** ZFIN (zebrafish), MGI/IMPC (mouse *Tefm*), Cellosaurus (patient lines), PDB (structures).

**Important specificity caveat (not disease-relevant but noted):** much of the *TEFM* literature concerns its **over-expression as an oncogene** (HCC, glioma, LUAD, endometrial carcinoma; e.g., PMIDs 33771980, 39719635, 39075464, 39731053). These describe **somatic gain**, the *opposite* of the germline loss-of-function that causes COXPD58, and are not part of this Mendelian disease.

---

## Supported vs. Refuted Hypotheses

**Supported:**
1. COXPD58 is an autosomal recessive disorder caused by biallelic *TEFM* variants (OMIM 620451). ✔
2. Mechanism = impaired mitochondrial transcription elongation → reduced promoter-distal mtRNA → combined CI/CIV OXPHOS deficiency. ✔ (patient functional data)
3. Phenotype is a variable childhood-onset encephalomyopathy with universal lactic acidosis and a treatable NMJ component. ✔
4. *TEFM* is LoF-tolerant in gnomAD, consistent with recessive inheritance. ✔
5. Zebrafish *tefm* knockdown recapitulates the NMJ/mitochondrial phenotype. ✔

**Refuted / not supported:**
- Peripheral neuropathy is **not** a feature (HP:0009830, 0/7).
- No environmental, infectious, autoimmune, or somatic/oncogenic mechanism underlies this germline disease.
- No dominant-negative/gain-of-function disease mechanism.

## Limitations and Future Directions

- **Very small evidence base** (<~15 patients); frequencies derive from a single cohort and are imprecise; no registries, natural-history studies, prevalence estimates, QoL data, or trials.
- **Variant interpretation immature** (mostly VUS in ClinVar); functional assays are needed for reclassification.
- **No approved or trial therapies;** the efficacy of CMS-type drugs for the NMJ defect in COXPD58 needs formal study.
- **Future needs:** stable animal/iPSC-neuron and -myocyte models, longitudinal natural-history data, genotype–phenotype correlation (e.g., p.Pro157Ala), and evaluation of mitochondrial and CMS-directed therapeutics.

---

### Key References (PMIDs)
- **36823193** — Van Haute et al., 2023, *Brain* — defining cohort; *TEFM* variants impair mitochondrial transcription causing childhood-onset neurological disease (reduced promoter-distal mtRNA; zebrafish model; treatable NMJ defect).
- **40272035** — Adarsha et al., 2025 — clinical/radiological characterization; recurrent p.Pro157Ala (South Asian).
- **37239850** — O'Connor et al., 2023 — review: mitochondrial mutations (incl. *TEFM*) and NMJ transmission; proposed "mitochondrial CMS."
- **31036713** — Jiang et al., 2019 — TEFM regulates transcription elongation and RNA processing in mitochondria (in vivo).
- **25635099** — Agaronyan et al., 2015 — TEFM as the replication–transcription switch; processivity.
- **29033127** — Hillen et al., 2017 — structural basis of TEFM anti-termination ("sliding clamp").
- **40712587 / 40236250** — Herbine et al., 2025 — cryo-EM of human mitochondrial transcription; TEFM recruitment after initiation-factor release.
- **39922921** — Matsuda et al., 2025 — TEFM facilitates RNA→DNA synthesis at OriH.
- **21278163** — original identification/characterization of TEFM function (UniProt-cited).


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_58-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_58-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 75 |
| Resolved | 73 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 21 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957537` (3 mentions) - the report calls it "MONDO"; MONDO calls it **combined oxidative phosphorylation deficiency 58**
- `HP:0004887` (1 mention) - the report calls it "1/7, severe end"; HP calls it **Respiratory failure requiring assisted ventilation**
- `UBERON:0002488` (1 mention) - the report calls it "neuromuscular junction"; UBERON calls it **helix of outer ear**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006392` (1 mention) - the report calls it "mitochondrial transcription/elongation"; GO calls it **transcription elongation by mitochondrial RNA polymerase**, and lists "transcription elongation from mitochondrial promoter" among its other names
- `GO:0006264` (1 mention) - the report calls it "mtDNA replication"; GO calls it **mitochondrial DNA replication**, and lists "mtDNA replication" among its other names
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle fiber"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names
- `UBERON:0000941` (1 mention) - the report calls it "eye/optic nerve"; UBERON calls it **cranial nerve II**, and lists "optic nerve" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.