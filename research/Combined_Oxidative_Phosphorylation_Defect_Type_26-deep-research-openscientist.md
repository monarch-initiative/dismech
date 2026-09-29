---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T22:07:46.834545'
end_time: '2026-08-30T22:23:37.744130'
duration_seconds: 950.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 'Combined Oxidative Phosphorylation Defect Type 26 (COXPD26), the
    TRMT5-related mitochondrial disease (OMIM 616539). Note: this is NOT COXPD30 /
    TRMT10C.'
  mondo_id: MONDO:0014684
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
  relevance_assessed: 18
  on_topic: 6
  off_topic: 3
  off_topic_references:
  - PMID:20980671
  - PMID:23887145
  - PMID:33016876
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 11
  labels_variant: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Defect_Type_26-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Defect_Type_26-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 26 (COXPD26), the TRMT5-related mitochondrial disease (OMIM 616539). Note: this is NOT COXPD30 / TRMT10C.
- **MONDO ID:** MONDO:0014684 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 26 (COXPD26), the TRMT5-related mitochondrial disease (OMIM 616539). Note: this is NOT COXPD30 / TRMT10C.** covering all of the
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

# Combined Oxidative Phosphorylation Defect Type 26 (COXPD26): A Comprehensive Disease Characterization

**Disease:** Combined Oxidative Phosphorylation Defect Type 26 (COXPD26) — the TRMT5-related mitochondrial disease
**Key identifiers:** OMIM 616539 · MONDO:0014684 · Gene: *TRMT5* (HGNC:23141)
**Category:** Mendelian, autosomal recessive
**Note:** This entry concerns the **TRMT5**-related disorder and is distinct from COXPD30 / *TRMT10C* (OMIM 616974).

---

## Summary

Combined Oxidative Phosphorylation Defect Type 26 (COXPD26; OMIM 616539; MONDO:0014684) is an **ultra-rare autosomal recessive primary mitochondrial disease** caused by biallelic loss-of-function variants in *TRMT5*, the nuclear-encoded tRNA methyltransferase that installs the **N1-methylguanosine (m1G37)** modification on mitochondrial tRNAs 3′ to the anticodon. Loss of TRMT5 activity produces **hypomodification of G37 in mitochondrial tRNAs** — most prominent in skeletal muscle — which impairs mitochondrial translation and results in a **combined deficiency of multiple respiratory-chain complexes** accompanied by lactic acidosis. The disease was first defined molecularly by Powell et al. in 2015 through whole-exome sequencing of two unrelated patients ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)).

The clinical picture is **highly variable and multisystem**. The originally reported extremes ranged from a child with failure to thrive and hypertrophic cardiomyopathy to an adult with a lifelong history of exercise intolerance. A subsequently reported Chinese case broadened the spectrum to include developmental delay, gastrointestinal dysmotility, hypotonia/muscle weakness, neuropathy, spastic diplegia, seizures, and novel renal and hepatic involvement ([PMID: 35109800](https://pubmed.ncbi.nlm.nih.gov/35109800/)). The disorder preferentially injures high-energy, post-mitotic tissues (skeletal muscle, heart, central and peripheral nervous system), consistent with a defect in mitochondrial energy production.

There is **no disease-specific or curative therapy**. Management follows general primary mitochondrial disease principles — supportive, organ-directed care, and metabolic cofactor supplementation (e.g., CoQ10, riboflavin), with generally modest efficacy. Because etiology is purely genetic, prevention rests on **genetic counseling, carrier detection, and reproductive options**. Fewer than roughly ten patients have been reported worldwide; a gnomAD-based estimate places the null-allele carrier frequency near **1 in 350**, though true disease incidence is higher because hypomorphic missense alleles also cause disease.

---

## Section-by-Section Characterization

### 1. Disease Information

COXPD26 is a nuclear-gene mitochondrial translation disorder. It belongs to the "combined oxidative phosphorylation deficiency" (COXPD) family of OMIM phenotypes — disorders in which **multiple** respiratory-chain complexes are simultaneously deficient, typically due to defects in the mitochondrial protein-synthesis machinery rather than in a single structural OXPHOS subunit.

- **What it is:** An autosomal recessive multisystem mitochondrial disease caused by biallelic *TRMT5* variants, characterized biochemically by lactic acidosis and combined respiratory-chain-complex deficiency, and molecularly by mt-tRNA m1G37 hypomodification.
- **Key identifiers:** OMIM **616539**; MONDO **:0014684**; Gene *TRMT5* (HGNC:23141, NCBI Gene 57570, Ensembl ENSG00000126814, UniProt Q32P41). A specific Orphanet code is not firmly established (ultra-rare); ICD-11 maps broadly to mitochondrial disease (e.g., 5C53.0 / relevant metabolic mitochondrial category); MeSH has no dedicated descriptor (indexed under "Mitochondrial Diseases" / "OXPHOS deficiency").
- **Synonyms / alternative names:** "Combined oxidative phosphorylation deficiency 26"; "COXPD26"; "TRMT5-related mitochondrial disease"; "TRMT5 deficiency"; "mitochondrial tRNA m1G37 methyltransferase deficiency."
- **Information source type:** Disease-level knowledge is **aggregated from individual published case reports** (a handful of patients) plus enzymology/mechanistic studies — not from large EHR cohorts or registries. Findings are thus case-based.

### 2. Etiology

- **Disease causal factors:** Purely **genetic** — biallelic (compound heterozygous or homozygous) loss-of-function variants in *TRMT5* ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)). No infectious, environmental, or primary toxic cause.
- **Genetic risk factors:** The causal variants themselves; disease requires two defective alleles. No susceptibility loci or validated modifier genes reported.
- **Environmental risk factors:** None established as causal. By analogy to primary mitochondrial disease, **catabolic stressors** (infection, fever, fasting, dehydration, general anesthesia, certain mitotoxic drugs) may act as **symptom precipitants** — an inferred, not demonstrated, COXPD26-specific interaction.
- **Protective factors:** None known (no protective alleles, no disease-modifying diet/exposure).
- **Gene–environment interactions:** Inferred only — metabolic decompensation triggered by intercurrent illness, as seen generically in mitochondrial disease.

### 3. Phenotypes

The spectrum is broad and multisystem. In the original report *"one presented in childhood with failure to thrive and hypertrophic cardiomyopathy, and the other was an adult with a life-long history of exercise intolerance"* ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)). The Chinese case added *"developmental delay, gastrointestinal dysfunction, shortness of breath, exercise intolerance, hypotonia and muscle weakness, neuropathy, and spastic diplegia"* plus renal and hepatic involvement and seizures ([PMID: 35109800](https://pubmed.ncbi.nlm.nih.gov/35109800/)).

| Phenotype | HPO term (suggested) | Type | Onset | Notes |
|---|---|---|---|---|
| Lactic acidosis | HP:0003128 | Laboratory abnormality | Variable | Biochemical hallmark |
| Combined OXPHOS/respiratory-chain deficiency | HP:0011922 | Laboratory abnormality | Variable | Multiple complexes in muscle |
| Hypertrophic cardiomyopathy | HP:0001639 | Clinical sign | Childhood | Severe end of spectrum |
| Failure to thrive | HP:0001508 | Clinical sign | Childhood | |
| Exercise intolerance | HP:0003546 | Symptom | Childhood–adult | Can be isolated adult presentation |
| Muscle weakness | HP:0001324 | Clinical sign | Variable | Myopathy |
| Hypotonia | HP:0001252 | Clinical sign | Variable | |
| Global developmental delay | HP:0001263 | Clinical sign | Childhood | |
| Seizures | HP:0001250 | Clinical sign | Childhood | |
| Peripheral neuropathy | HP:0009830 | Clinical sign | Variable | |
| Spastic diplegia | HP:0001264 | Clinical sign | Childhood | |
| Gastrointestinal dysmotility | HP:0002579 | Clinical sign | Variable | |
| Abnormal liver function | HP:0001392 | Clinical sign | Variable | Novel (Chinese case) |
| Renal involvement | HP:0000077 | Clinical sign | Variable | Novel (Chinese case) |

- **Severity/progression:** Variable; ranges from mild (isolated adult exercise intolerance) to severe childhood cardiomyopathy/failure to thrive. Progressive in severe cases.
- **Frequency among affected individuals:** Qualitative only — too few patients for reliable percentages.
- **Quality-of-life impact:** Not formally quantified (no EQ-5D/SF-36 data). Severe childhood disease with cardiomyopathy and developmental delay is highly disabling; isolated adult exercise intolerance is comparatively mild.

### 4. Genetic / Molecular Information

- **Causal gene:** *TRMT5* — HGNC:23141, NCBI Gene 57570, Ensembl ENSG00000126814, **chromosome 14q23.1** (GRCh37 chr14:60,971,441–60,981,694, minus strand), UniProt Q32P41. Encodes a **class I-like (Rossmann-fold) SAM-dependent methyltransferase**; *"TRMT5 encodes a mitochondrial protein with strong homology to members of the class I-like methyltransferase superfamily"* ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)).
- **Pathogenic variants (transcript NM_020810.3):** Pathogenic missense **c.1156A>G (p.Met386Val)**; likely-pathogenic truncating **c.259A>T (p.Arg87Ter)** and **c.267_270delinsCTG (p.Ala89_Phe90insTer)**; reported case variants **c.665T>C (p.Ile222Thr)** and the compound-heterozygous set **c.881A>C (p.Glu294Ala), c.1218G>C (p.Gln406His), c.1481C>T (p.Thr494Met)** ([PMID: 35109800](https://pubmed.ncbi.nlm.nih.gov/35109800/)); plus LoF alleles c.205_208del (p.Glu69fs). Variant classes span missense (predominant, hypomorphic), nonsense, frameshift, in-frame indel-with-stop, and splice/UTR.
- **Classification:** Per ACMG/AMP; ClinVar (~299 records) is dominated by VUS and likely-benign calls, so functional evidence is often needed.
- **Allele frequency:** Individual pathogenic alleles are ultra-rare in gnomAD; summed predicted-LoF allele frequency ≈ 0.00143.
- **Somatic vs germline:** All germline.
- **Functional consequence:** **Loss of function** in every case — convergent loss of m1G37 methyltransferase activity; no gain-of-function or dominant-negative described. LoF proven by rescue with wild-type cDNA ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)).
- **Constraint:** gnomAD pLI = 0.05, LOEUF = 0.588, missense Z = 0.10 — tolerant of heterozygous LoF, as expected for a recessive gene.
- **Modifier genes / epigenetics / chromosomal abnormalities:** None reported.

### 5. Environmental Information

No environmental, lifestyle, or infectious factor causes COXPD26. It is a monogenic disorder. Catabolic/metabolic stress may precipitate decompensation (inferred). No toxins, occupational exposures, dietary factors, or pathogens are implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1. Biallelic loss-of-function TRMT5 variants (missense hypomorph and/or truncating)
     │  leads to
2. Reduced/absent TRMT5 (m1G37) methyltransferase activity in the mitochondrial matrix
     │  results in
3. Hypomodification of guanosine-37 (loss of m1G37) on mitochondrial tRNAs
     │  (most prominent in skeletal muscle)
     │  leads to
4. Impaired mitochondrial translation of mtDNA-encoded OXPHOS subunits
     │  (loss of decoding fidelity / frameshift-prevention function of m1G37)
     │  results in
5. Combined deficiency of multiple respiratory-chain complexes
     │  branches to ↓ (downstream, partly inferred from related tRNA-37 defects)
     ├─► reduced mitochondrial membrane potential + reduced ATP production ──► energy failure
     ├─► accumulation of reducing equivalents ──► elevated lactate ──► LACTIC ACIDOSIS
     └─► increased reactive oxygen species (ROS) ──► oxidative stress ──► autophagy / cell injury
     │  leads to (preferential injury of high-energy, post-mitotic tissues)
6. Organ dysfunction:
     ├─ skeletal muscle ──► myopathy, exercise intolerance, hypotonia
     ├─ heart ──► hypertrophic cardiomyopathy
     ├─ CNS ──► developmental delay, seizures, spastic diplegia
     ├─ peripheral nerve ──► neuropathy
     └─ GI / liver / kidney ──► dysmotility, hepatic & renal involvement
     │  culminates in
7. Variable multisystem clinical disease (childhood cardiomyopathy/FTT ←→ adult exercise intolerance)
```

**Molecular detail.** TRMT5 catalyzes **SAM-dependent methyl transfer to N1 of guanosine 37** on mt-tRNAs: *"Trm5 is a eukaryal and archaeal tRNA methyltransferase that catalyzes methyl transfer from S-adenosylmethionine (AdoMet) to the N(1) position of G37 directly 3' to the anticodon"* ([PMID: 20980671](https://pubmed.ncbi.nlm.nih.gov/20980671/)). m1G37 preserves reading frame and decoding fidelity: *"Enzymes of the Trm5 family catalyze methyl transfer from S-adenosyl methionine (AdoMet) to the N¹ of G37 to synthesize m¹G37-tRNA as a critical determinant to prevent ribosome frameshift errors"* ([PMID: 23887145](https://pubmed.ncbi.nlm.nih.gov/23887145/)); structural work confirms m1G37 stabilizes codon–anticodon pairing ([PMID: 33016876](https://pubmed.ncbi.nlm.nih.gov/33016876/)). In patients, *"Mutations in TRMT5 were associated with the hypomodification of a guanosine residue at position 37 (G37) of mitochondrial tRNA; this hypomodification was particularly prominent in skeletal muscle"* ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)).

**Downstream cascade** (inferred from a closely related position-37 mt-tRNA defect): *"The aberrant tRNA metabolism resulted in the impairment of mitochondrial translation, respiratory deficiency, decreasing membrane potentials and ATP production, increasing production of reactive oxygen species and promoting autophagy"* ([PMID: 33398350](https://pubmed.ncbi.nlm.nih.gov/33398350/)).

**Upstream vs downstream summary:**

| Layer | Event | Status |
|---|---|---|
| Upstream (cause) | Biallelic *TRMT5* LoF variants | Demonstrated |
| Molecular lesion | Loss of m1G37 on mt-tRNAs | Demonstrated (patients + RNAi) |
| Proximal effect | Impaired mitochondrial translation | Demonstrated |
| Biochemical readout | Combined RC-complex deficiency; lactic acidosis | Demonstrated |
| Downstream | ↓ATP, ↓Δψm, ↑ROS, autophagy | Inferred (analogous tRNA-37 defects) |
| Clinical | Multisystem organ dysfunction | Demonstrated (case reports) |

- **GO terms:** mitochondrial translation (GO:0032543); tRNA methylation (GO:0030488); mitochondrion (GO:0005739); mitochondrial matrix (GO:0005759).
- **CL terms:** skeletal muscle cell (CL:0000188); cardiac muscle cell / cardiomyocyte (CL:0000746); neuron (CL:0000540).
- **CHEBI terms:** S-adenosyl-L-methionine (CHEBI:15414); N1-methylguanosine (CHEBI:has m1G); lactate (CHEBI:24996).

### 7. Anatomical Structures Affected

- **Primary organs:** Skeletal muscle (UBERON:0001134), heart (UBERON:0000948 / cardiac muscle UBERON:0002349), brain/CNS (UBERON:0000955).
- **Secondary/additional:** Peripheral nerve (UBERON:0001021), gastrointestinal tract (UBERON:0001555), liver (UBERON:0002107), kidney (UBERON:0002113).
- **Body systems:** Musculoskeletal, cardiovascular, central & peripheral nervous, digestive, hepatic, renal.
- **Tissue/cell level:** Post-mitotic, high-oxidative-demand cells — myocytes, cardiomyocytes, neurons.
- **Subcellular:** Mitochondrial matrix translation apparatus (GO:0005759; GO:0005739). The molecular defect is fundamentally subcellular; organ damage is downstream of energy failure.
- **Localization/lateralization:** Systemic and bilateral/symmetric (metabolic disease), not focal.

### 8. Temporal Development

- **Onset:** Ranges from **childhood** (failure to thrive, hypertrophic cardiomyopathy) to **adulthood** (isolated exercise intolerance) ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)); the Chinese case had childhood/developmental onset ([PMID: 35109800](https://pubmed.ncbi.nlm.nih.gov/35109800/)). Onset pattern is typically **chronic/insidious**, with possible acute metabolic decompensation during intercurrent illness.
- **Progression:** Variable — progressive in severe childhood cases; relatively stable in mild adult cases. No formal staging exists.
- **Duration:** Chronic, lifelong.
- **Remission:** No spontaneous remission described. (Note: some *other* mt-tRNA-modification disorders, e.g., TRMU-related, can be reversible — [PMID: 21931168](https://pubmed.ncbi.nlm.nih.gov/21931168/) — but reversibility has **not** been reported for COXPD26.)
- **Critical periods:** Early childhood is the highest-risk window for severe presentation; metabolic stress is a period of vulnerability.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive; reported patients are compound heterozygous — *"we identified two unrelated individuals carrying compound heterozygous variants in TRMT5"* ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)); *"This disease is considered to be caused by compound heterozygous mutations in the TRMT5 gene"* ([PMID: 35109800](https://pubmed.ncbi.nlm.nih.gov/35109800/)).
- **Epidemiology:** Ultra-rare — fewer than ~10 reported patients worldwide. No established Orphanet prevalence.
- **Carrier frequency / incidence (computed):** gnomAD r2.1 contains 44 predicted-LoF *TRMT5* alleles (summed AF ≈ 0.00143), giving a **null-allele carrier frequency ~2q ≈ 0.29% (~1/350)** and a biallelic-null birth incidence ~q² ≈ 2×10⁻⁶ (**~1/490,000**). This is a **lower bound** — hypomorphic missense alleles also cause disease.
- **Penetrance / expressivity:** Presumed complete penetrance for biallelic LoF; **variable expressivity** (wide phenotype range).
- **Founder effects / consanguinity:** No founder mutation reported; cases span European and East Asian ancestry. Consanguinity would raise homozygous risk (general AR principle).
- **Sex ratio / age distribution:** No sex predilection expected (autosomal); onset childhood–adult.

### 10. Diagnostics

- **Laboratory:** Elevated blood (and often CSF) **lactate** (lactic acidosis).
- **Muscle biopsy / enzymology:** Combined (multiple-complex) respiratory-chain deficiency; G37 hypomodification most prominent in skeletal muscle — *"this hypomodification was particularly prominent in skeletal muscle"* ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)). **Caveat:** RC enzymology is an insensitive screen for mt-tRNA defects — *"RC enzyme analysis in muscle is not a sensitive test for MM in adults"* ([PMID: 19941338](https://pubmed.ncbi.nlm.nih.gov/19941338/)).
- **Genetic testing (diagnostic gold standard):** WES/WGS or nuclear mitochondrial-gene panels detecting biallelic *TRMT5* variants; single-gene *TRMT5* sequencing for targeted confirmation. Because most ClinVar entries are VUS, **functional confirmation** (m1G37 methylation assay, yeast complementation) strengthens classification.
- **Imaging/electrophysiology:** Echocardiography (cardiomyopathy), EMG/nerve conduction (neuropathy/myopathy), EEG (seizures), brain MRI as clinically indicated — nonspecific.
- **Differential diagnosis:** Other combined-OXPHOS / mt-tRNA-modification disorders — ACAD9 deficiency ([PMID: 33204590](https://pubmed.ncbi.nlm.nih.gov/33204590/)), MT-ND5 cardiomyopathy ([PMID: 30587702](https://pubmed.ncbi.nlm.nih.gov/30587702/)), TRMU-related reversible infantile RC deficiency ([PMID: 21931168](https://pubmed.ncbi.nlm.nih.gov/21931168/)), MERRF/MELAS. Distinguishing feature: **biallelic nuclear *TRMT5* variants with muscle-predominant mt-tRNA G37 hypomodification.** Explicitly **not** COXPD30/*TRMT10C*.
- **Screening:** No newborn screening exists; cascade carrier testing of relatives once familial variants known.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics (too few cases). Severe childhood cardiomyopathy with failure to thrive carries higher mortality risk, as in comparable mitochondrial cardiomyopathies; mild adult disease is compatible with long survival.
- **Morbidity/function:** Highly variable — from mild exercise limitation to severe disability with developmental delay, seizures, and cardiomyopathy.
- **Complications:** Heart failure/arrhythmia (cardiomyopathy), metabolic decompensation during illness, feeding failure, seizures.
- **Prognostic factors:** Age of onset and organ involvement (childhood cardiomyopathy = worse prognosis; isolated adult exercise intolerance = better). Residual TRMT5 activity (allele severity) is a plausible but unproven prognostic determinant.
- **QoL measures:** Not formally assessed.

### 12. Treatment

- **No disease-specific/curative therapy exists.** Management follows general primary mitochondrial disease practice — *"electron acceptors, enzyme activators, vitamins, coenzymes, free-radical scavengers, dietary measures, and supportive therapy"* ([PMID: 11282042](https://pubmed.ncbi.nlm.nih.gov/11282042/)), with generally modest efficacy.
- **Cofactor/pharmacotherapy (empiric):** Coenzyme Q10 (CHEBI:46245; NCIT:C1042), riboflavin/vitamin B2 (CHEBI:17015), other B-vitamins, free-radical scavengers, L-carnitine — individualized.
- **Organ-directed/supportive:** Cardiomyopathy management (standard heart-failure care); physical therapy for myopathy/exercise intolerance; nutritional support for GI dysmotility/failure-to-thrive; anticonvulsants for seizures; avoidance of mitotoxic drugs and prolonged fasting; aggressive management of intercurrent illness.
- **Advanced/experimental therapeutics:** No gene therapy, RNA therapy, or targeted therapy in trials for COXPD26. NCIT term for approach: Supportive Care (NCIT:C133435).
- **Pharmacogenomics/personalized medicine:** Genotype-guided cofactor trials plausible but unvalidated; note riboflavin responsiveness in the related ACAD9 deficiency ([PMID: 33204590](https://pubmed.ncbi.nlm.nih.gov/33204590/)) motivates empiric cofactor trials.

### 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (monogenic). Prevention centers on **genetic counseling and reproductive planning**.
- **Genetic screening:** Carrier testing of at-risk relatives (cascade testing); prenatal diagnosis or preimplantation genetic testing (PGT) once familial variants are identified.
- **Secondary/tertiary prevention:** Early recognition and organ surveillance (cardiac monitoring), prompt treatment of metabolic decompensation, avoidance of catabolic stress and mitotoxic exposures.
- **Counseling:** Recurrence risk 25% for a couple who are both carriers (AR). No population-based screening program exists (ultra-rare).

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** The Trm5/TRMT5 enzyme family is conserved from archaea to humans — *"These results establish conservation in both the catalytic mechanism and overall structure of Trm5 between evolutionarily distant eukaryotic and archaeal species"* ([PMID: 23887145](https://pubmed.ncbi.nlm.nih.gov/23887145/)). Orthologs: mouse *Trmt5* (NCBI Gene 76357), rat *Trmt5* (362754), zebrafish *trmt5* (564078).
- **Natural disease in other species:** No naturally occurring TRMT5-related disease is documented in companion animals or wildlife (no OMIA entry noted).
- **Comparative biology:** Deep conservation of the m1G37 modification mechanism implies disease mechanisms would be conserved, supporting cross-species modeling.
- **Transmission:** Not applicable (non-infectious, non-zoonotic).

### 15. Model Organisms

- **Cellular/in vitro:** *TRMT5* RNAi in human cells reproduces G37 hypomodification; re-expression of wild-type cDNA rescues the molecular phenotype ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)).
- **Yeast complementation:** *"The pathogenicity of the detected variants was further confirmed in a heterologous yeast model"* (*S. cerevisiae*) ([PMID: 26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/)) — a validated system for assessing variant function.
- **Potential whole-animal models:** Conserved orthologs in mouse, rat, and zebrafish exist, but **no published knockout/knock-in animal model** recapitulating the multisystem human disease has been reported.
- **Phenotype recapitulation:** Cellular/yeast models faithfully reproduce the **molecular** phenotype (G37 hypomodification, impaired function). Whole-organism, multisystem recapitulation is an open gap.
- **Applications:** Existing models support variant classification and mechanistic study; iPSC-derived tissues and conditional animal models are the logical next resources.

---

## Mechanistic Model / Interpretation

COXPD26 is a clean example of a **mitochondrial translation disorder**: a single nuclear enzyme deficiency (TRMT5) removes one specific chemical mark (m1G37) from mitochondrial tRNAs, degrading the fidelity and efficiency of mitochondrial protein synthesis, which in turn cripples **all** thirteen mtDNA-encoded OXPHOS subunits at once — hence a *combined* respiratory-chain deficiency rather than an isolated complex defect. The steps from mutation through m1G37 loss to combined RC deficiency and lactic acidosis are **directly demonstrated in patients and in cell/yeast models**. The specific injurious downstream events (membrane-potential collapse, ATP decline, ROS surge, autophagy) are **inferred** from a mechanistically parallel position-37 mt-tRNA modification disorder ([PMID: 33398350](https://pubmed.ncbi.nlm.nih.gov/33398350/)).

The tissue distribution follows an energetics logic: skeletal muscle, heart, and neurons — the most oxidative, least glycolytically flexible, post-mitotic tissues — bear the brunt, explaining myopathy, cardiomyopathy, developmental delay, seizures, and neuropathy. The wide phenotypic range (severe childhood cardiomyopathy vs. isolated adult exercise intolerance) most plausibly reflects **allele severity / residual enzyme activity** and possibly tissue-specific modification thresholds, though this genotype–phenotype relationship remains unproven given the tiny cohort.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [26189817](https://pubmed.ncbi.nlm.nih.gov/26189817/) | *TRMT5 Mutations Cause a Defect in Post-transcriptional Modification of Mitochondrial tRNA...* | **Landmark / disease-defining.** Biallelic *TRMT5* cause, AR inheritance, combined RC deficiency, m1G37 hypomodification (muscle-predominant), yeast + RNAi confirmation, LoF-by-rescue. Underpins Findings 1–5, 7–11. |
| [35109800](https://pubmed.ncbi.nlm.nih.gov/35109800/) | *Novel heterozygous compound TRMT5 mutations... in a Chinese family* | Expands multisystem phenotype (renal/hepatic novel); documents compound-het missense variants. Findings 3, 7, 10. |
| [20980671](https://pubmed.ncbi.nlm.nih.gov/20980671/) | *Mechanism of N-methylation by the tRNA m1G37 methyltransferase Trm5* | Defines the SAM-dependent m1G37 enzymatic reaction. Finding 2. |
| [23887145](https://pubmed.ncbi.nlm.nih.gov/23887145/) | *Conservation of structure and mechanism by Trm5 enzymes* | m1G37 prevents ribosome frameshift errors; cross-species conservation. Findings 2, 8. |
| [33016876](https://pubmed.ncbi.nlm.nih.gov/33016876/) | *Structural insights into mRNA reading frame regulation...* | Structural basis for m1G37 maintaining reading frame/decoding fidelity. Finding 2. |
| [33398350](https://pubmed.ncbi.nlm.nih.gov/33398350/) | *A deafness-associated tRNA mutation... m1G37 modification...* | Demonstrates downstream cascade (↓translation, ↓Δψm, ↓ATP, ↑ROS, autophagy) for position-37 defects. Finding 9. |
| [19941338](https://pubmed.ncbi.nlm.nih.gov/19941338/) | *Limited diagnostic value of enzyme analysis in patients with mitochondrial tRNA mutations* | Justifies molecular-first diagnosis; RC enzymology insensitive. Finding 5. |
| [11282042](https://pubmed.ncbi.nlm.nih.gov/11282042/) | *Mitochondrial Disease* | Supportive/non-curative treatment framework. Finding 6. |

**Supporting context papers:** Reviews of tRNA position-37 methylation and disease ([PMID: 40155300](https://pubmed.ncbi.nlm.nih.gov/40155300/), [PMID: 38943267](https://pubmed.ncbi.nlm.nih.gov/38943267/), [PMID: 37789629](https://pubmed.ncbi.nlm.nih.gov/37789629/)); TRMT5 in hepatocellular carcinoma ([PMID: 36632750](https://pubmed.ncbi.nlm.nih.gov/36632750/), a distinct oncologic role of the same enzyme); and comparator mitochondrial disorders for differential diagnosis (ACAD9 [PMID: 33204590](https://pubmed.ncbi.nlm.nih.gov/33204590/); MT-ND5 [PMID: 30587702](https://pubmed.ncbi.nlm.nih.gov/30587702/); TRMU/reversible infantile RC deficiency [PMID: 21931168](https://pubmed.ncbi.nlm.nih.gov/21931168/); MERRF [PMID: 21303704](https://pubmed.ncbi.nlm.nih.gov/21303704/); NARP [PMID: 25746071](https://pubmed.ncbi.nlm.nih.gov/25746071/); MELAS [PMID: 19198146](https://pubmed.ncbi.nlm.nih.gov/19198146/)).

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Fewer than ~10 patients reported. All phenotype frequencies are qualitative; no penetrance/expressivity statistics, natural-history data, survival curves, or quality-of-life measurements exist.
2. **Variant classification uncertainty.** Most *TRMT5* ClinVar entries are VUS. Without functional assays, classifying novel missense alleles is difficult, complicating diagnosis and counseling.
3. **Downstream mechanism partly inferred.** The injury cascade (↓Δψm, ↓ATP, ↑ROS, autophagy) is extrapolated from a related position-37 tRNA-modification defect ([PMID: 33398350](https://pubmed.ncbi.nlm.nih.gov/33398350/)), not directly demonstrated in COXPD26 patient tissue.
4. **No whole-animal disease model.** Orthologs exist, but no published conditional knockout/knock-in recapitulating the multisystem human phenotype.
5. **Epidemiology is a computed estimate.** Carrier frequency (~1/350) and incidence (~1/490,000) derive from gnomAD pLoF counting and underestimate true incidence because hypomorphic missense alleles cause disease.
6. **No genotype–phenotype map.** It is unknown why some patients have isolated adult exercise intolerance while others have severe childhood cardiomyopathy.
7. **No therapy trials.** No treatment has been tested specifically in COXPD26; all management is extrapolated from general mitochondrial disease practice.

---

## Proposed Follow-up Experiments / Actions

1. **Functional variant-classification pipeline.** Standardized yeast complementation and/or in vitro m1G37 methyltransferase activity assays to reclassify *TRMT5* VUS, prioritizing patient alleles (c.665T>C, c.881A>C, c.1218G>C, c.1481C>T) and producing an evidence-graded variant table.
2. **Conditional *Trmt5* animal model.** Tissue-specific (muscle, heart, CNS) mouse or zebrafish knockout to test recapitulation of muscle-predominant G37 hypomodification and combined RC deficiency, and to directly measure Δψm, ATP, ROS, and autophagy.
3. **Patient iPSC and organoid models.** Differentiate patient iPSCs into cardiomyocytes, myotubes, and cortical neurons to correlate residual m1G37 modification with OXPHOS capacity and to screen candidate metabolic therapies (CoQ10, riboflavin, ROS scavengers).
4. **International registry / natural-history study.** Aggregate cases via GeneMatcher to define onset distribution, progression, survival, genotype–phenotype correlations, and standardized quality-of-life/organ outcomes.
5. **Systematic mt-tRNA modification profiling.** Modification-sensitive sequencing of patient tissues to quantify per-tRNA G37 hypomodification and link to complex-specific deficiencies.
6. **Cofactor/therapeutic pilot.** Given riboflavin responsiveness in overlapping disorders (ACAD9), evaluate cofactor supplementation in cellular models as a rational, low-risk supportive strategy.

---

## Consensus Answer

COXPD26 (OMIM 616539; MONDO:0014684) is an ultra-rare autosomal recessive primary mitochondrial disease caused by biallelic loss-of-function variants in *TRMT5*, the nuclear-encoded enzyme that installs the m1G37 methylation on mitochondrial tRNAs; its loss causes mt-tRNA G37 hypomodification (most marked in skeletal muscle), impairing mitochondrial translation and producing a combined deficiency of respiratory-chain complexes with lactic acidosis. The phenotype is highly variable and multisystem — from childhood failure-to-thrive with hypertrophic cardiomyopathy to isolated adult exercise intolerance, plus myopathy, developmental delay, seizures, neuropathy, and GI/hepatic/renal involvement. Management is entirely supportive, as no disease-specific therapy exists.


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_26-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_26-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 6 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:20980671` (4 mentions) - Mechanism of N-methylation by the tRNA m1G37 methyltransferase Trm5.
  - shared terms: m1g37
- `PMID:23887145` (6 mentions) - Conservation of structure and mechanism by Trm5 enzymes.
  - shared terms: none
- `PMID:33016876` (4 mentions) - Structural insights into mRNA reading frame regulation by tRNA modification and slippery codon-anticodon pairing.
  - shared terms: m1g37

Weighed against this report's own most characteristic terms: `trmt5`, `disease`, `mitochondrial`, `variant`, `deficiency`, `m1g37`, `combined`, `cardiomyopathy`, `patient`, `adult`, `phenotype`, `defect`, `coxpd26`, `disorder`, `muscle`, `metabolic`, `allele`, `exercise`, `hypomodification`, `intolerance`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 8 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011922` (1 mention) - the report calls it "Combined OXPHOS/respiratory-chain deficiency"; HP calls it **Abnormal activity of mitochondrial respiratory chain**
- `HP:0001392` (1 mention) - the report calls it "Abnormal liver function"; HP calls it **Abnormality of the liver**, and lists "Abnormal liver" among its other names
- `HP:0000077` (1 mention) - the report calls it "Renal involvement"; HP calls it **Abnormality of the kidney**, and lists "Renal anomaly" among its other names
- `GO:0032543` (1 mention) - the report calls it "GO terms:** mitochondrial translation"; GO calls it **mitochondrial translation**
- `CL:0000188` (1 mention) - the report calls it "CL terms:** skeletal muscle cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CHEBI:15414` (1 mention) - the report calls it "CHEBI terms:** S-adenosyl-L-methionine"; CHEBI calls it **S-adenosyl-L-methionine**
- `UBERON:0001134` (1 mention) - the report calls it "Primary organs:** Skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names
- `UBERON:0001021` (1 mention) - the report calls it "Secondary/additional:** Peripheral nerve"; UBERON calls it **nerve**, and lists "peripheral nerve" among its other names

36 of 37 terms resolved to a current term; the rest could not be looked up either way.