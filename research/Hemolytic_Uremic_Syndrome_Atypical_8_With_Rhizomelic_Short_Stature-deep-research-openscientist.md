---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T13:28:14.337500'
end_time: '2026-10-19T13:48:15.609990'
duration_seconds: 1201.27
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hemolytic Uremic Syndrome Atypical 8 With Rhizomelic Short Stature
  mondo_id: MONDO:0957495
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
citation_count: 10
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 44
  verified: 42
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 23
  labels_variant: 11
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  - term_id: GO:0051082
    ontology_label: obsolete unfolded protein binding
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hemolytic_Uremic_Syndrome_Atypical_8_With_Rhizomelic_Short_Stature-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hemolytic_Uremic_Syndrome_Atypical_8_With_Rhizomelic_Short_Stature-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemolytic Uremic Syndrome Atypical 8 With Rhizomelic Short Stature
- **MONDO ID:** MONDO:0957495 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hemolytic Uremic Syndrome Atypical 8 With Rhizomelic Short Stature** covering all of the
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

# Hemolytic Uremic Syndrome, Atypical, 8, With Rhizomelic Short Stature — Comprehensive Disease Report

**MONDO:** MONDO:0957495 · **OMIM:** #301110 · **Gene:** *C1GALT1C1* (Cosmc), Xq24 · **Category:** Mendelian (X-linked) · **Report date:** 2026-10-19

---

## Summary

**Hemolytic uremic syndrome, atypical, 8, with rhizomelic short stature (aHUS8)** is an ultra-rare, X-linked **congenital disorder of O-glycosylation (a chaperonopathy)** caused by germline hypomorphic or de novo mosaic loss-of-function variants in ***C1GALT1C1***, the gene encoding the endoplasmic reticulum (ER) molecular chaperone **Cosmc** (Core-1 β3-galactosyltransferase-specific chaperone 1). It was first delineated in 2023 (OMIM #301110). Cosmc is obligatory for the correct folding and activity of **T-synthase (C1GALT1)**, the enzyme that converts the Tn-antigen precursor (GalNAcα1-O-Ser/Thr) into the universal **Core-1 "T-antigen"** O-glycan. When Cosmc is lost, T-synthase misfolds, Core-1 O-glycans fail to form, and **Tn-antigen (CD175) is aberrantly exposed** across the glycoproteome and on erythrocytes. The downstream consequence is a **multisystem disease** whose kidney manifestation resembles atypical hemolytic uremic syndrome (aHUS): a thrombotic microangiopathy (TMA) with microangiopathic hemolytic anemia, thrombocytopenia, and acute kidney injury (AKI). Beyond the kidney, patients show **rhizomelic (disproportionate) short stature, immunodeficiency, neurodevelopmental delay, seizures, and dysmorphic features**.

The mechanistic model is a linear glyco-chaperonopathy cascade: **mutation → reduced Cosmc → T-synthase deficiency → loss of Core-1 O-glycans / Tn-antigen exposure → multisystem glycoprotein dysfunction → complement-mediated TMA and extrarenal disease**. Two complementary routes connect the glyco-defect to complement-driven kidney injury: (1) direct endothelial TMA, and (2) production of **galactose-deficient IgA1 (Gd-IgA1)** immune complexes that activate complement in the glomerulus (the IgA-nephropathy axis). Crucially, the renal TMA is **terminal-complement (C5) dependent and fully responsive to the anti-C5 monoclonal antibody eculizumab**, whereas the upstream glycosylation defect itself is not yet correctable.

The disease is **ultra-rare**, with fewer than ten reported individuals worldwide: two affected maternal half-brothers plus attenuated carrier mother and grandmother (defining report, 2023), and one de novo postzygotic mosaic female presenting as nonimmune hydrops fetalis (2025). Inheritance is **X-linked recessive**: hemizygous males are affected, obligate-carrier females are usually attenuated via skewed X-inactivation, and de novo mosaicism can produce disease in females. This report synthesizes the molecular, phenotypic, diagnostic, therapeutic, epidemiologic, and model-organism evidence across all 15 requested sections.

---

## Key Findings

### Finding 1 — aHUS8 is caused by germline *C1GALT1C1* (Cosmc) variants: a multisystem O-glycosylation chaperonopathy (COSMC-CDG)

aHUS8 is defined molecularly by hemizygous or mosaic loss-of-function variants in ***C1GALT1C1*** (also known as *AHUS8*, *COSMC*, *TNPS*, *C1GALT2*; NCBI Gene 29071; ENSG00000171155; Xq24). In the defining report, two maternal half-brothers both carried the hemizygous variant **c.59C>A (p.Ala20Asp; "A20D-Cosmc")**, located within the **transmembrane signal-anchor domain** of Cosmc, "resulting in dramatically reduced expression of the Cosmc protein," reduced T-synthase (C1GALT1) activity, and pathological Tn-antigen exposure ([PMID: 37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/)). The carrier mother and maternal grandmother showed an attenuated phenotype associated with skewed X-inactivation.

A second, independent case established **allelic heterogeneity and female disease via mosaicism**: a 5-year-old girl with a **de novo mosaic nonsense variant c.202C>T (p.Arg68\*)** present in ~27% of buccal cells, "which results in a truncated and nonfunctional form of Cosmc (Cosmc-R68)" ([PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/)). Together these two reports confirm gene causality by two distinct variant classes (a hypomorphic transmembrane missense and a frank truncating nonsense allele). Because the defect lies in the O-glycosylation machinery, the condition is best classed as a **congenital disorder of glycosylation (COSMC-CDG)** with aHUS as its sentinel renal phenotype. **Ontology:** MONDO:0957495; HGNC *C1GALT1C1*; inheritance HP:0001419 (X-linked recessive).

### Finding 2 — Mechanism: Cosmc loss → T-synthase deficiency → Tn-antigen exposure → complement-mediated TMA (eculizumab-responsive)

The causal chain is: (1) a hemizygous/mosaic *C1GALT1C1* variant reduces the ER chaperone Cosmc; (2) its client enzyme **T-synthase (C1GALT1) misfolds and loses activity** — "Cosmc is essential for the generation of normal O-glycans through regulating T-synthase activity, thereby enabling the formation of the universal Core 1 O-glycan" ([PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/)); (3) failure to convert Tn-antigen (GalNAcα1-O-Ser/Thr) to Core-1 T-antigen (Galβ1-3GalNAcα1-Ser/Thr); (4) "the loss of Cosmc leads to the expression of the unusual precursor O-glycan termed Tn-antigen (CD175)" ([PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/)) across glycoproteins and erythrocytes; (5) **multisystem disease** including AKI resembling aHUS, thrombocytopenia, microangiopathic hemolytic anemia with schistocytes, immunodeficiency, developmental delay, and short stature. The renal TMA in the two male index patients was "fully responsive to treatment with the complement inhibitor Eculizumab" (anti-C5), implicating **terminal complement activation (C5b-9/membrane-attack complex)** as the proximate effector of kidney injury ([PMID: 37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/)).

This glyco-mechanism is supported in vivo. In an intestinal-epithelial Cosmc-knockout mouse, "CD175 expression is accompanied by loss of glycocalyx, shortening of microvilli, compromised MUC2, thickening of the epithelial layer, as well as generation of high levels of reactive oxygen species" ([PMID: 41759737](https://pubmed.ncbi.nlm.nih.gov/41759737/)) — demonstrating that Cosmc loss produces tissue-level glycocalyx failure and oxidative stress, plausible contributors to endothelial injury. **Ontology:** GO:0016266 (O-glycan processing), GO:0006486 (protein glycosylation), GO:0006956 (complement activation), GO:0005788 (endoplasmic reticulum lumen); CHEBI Tn-antigen / N-acetylgalactosamine.

### Finding 3 — Phenotypic spectrum: aHUS/TMA triad + rhizomelic short stature + immunodeficiency + neurodevelopmental and dysmorphic features

The male index patients "exhibit developmental delay, immunodeficiency, short stature, thrombocytopenia, and acute kidney injury (AKI) resembling atypical hemolytic uremic syndrome" ([PMID: 37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/)). The HPO annotation set (Monarch; ~32 terms) and OMIM #301110 give a multisystem picture spanning hematologic, renal, growth/skeletal, immune, neurologic, and craniofacial domains (table below). The de novo mosaic female presented at the severe end of the spectrum as **nonimmune hydrops fetalis** and is now a 5-year-old ([PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/)). Onset is **congenital/early childhood**; carrier females are attenuated.

| Domain | Phenotype | HPO term |
|---|---|---|
| Hematologic (TMA) | Hemolytic-uremic syndrome | HP:0005575 |
| | Hemolytic anemia | HP:0001878 |
| | Schistocytosis | HP:0001981 |
| | Thrombocytopenia | HP:0001873 |
| | Decreased haptoglobin | HP:0020181 |
| | Anemia | HP:0001903 |
| Renal | Elevated creatinine | HP:0003259 |
| | Proteinuria | HP:0000093 |
| | Hyperechogenic kidneys | HP:0004719 |
| Growth / skeletal | Disproportionate short stature (rhizomelic) | HP:0003498 |
| | Short long bone | HP:0003026 |
| Immune | Recurrent infections | HP:0002719 |
| | Decreased neutrophil count | HP:0001875 |
| | Decreased lymphocyte count | HP:0001888 |
| | Recurrent GI infection | HP:0004798 |
| Neurologic | Global developmental delay | HP:0001263 |
| | Generalized-onset seizure | HP:0002197 |
| Craniofacial | High forehead | HP:0000348 |
| | Wide nasal bridge | HP:0000431 |
| | Long eyelashes | HP:0000527 |
| | Short philtrum | HP:0000322 |
| | Downturned corners of mouth | HP:0002714 |
| | Retrognathia | HP:0000278 |
| | Posteriorly rotated ears | HP:0000358 |

### Finding 4 — Cosmc protein biology and population genetics

Cosmc (UniProt **Q96EU7**) is a **318-amino-acid, single-pass type II ER membrane protein**: cytoplasmic residues 1–6, a transmembrane signal-anchor helix at residues 7–26, and a lumenal domain 27–318. The pathogenic **p.Ala20Asp** substitution lies squarely within the transmembrane signal-anchor (residue 20), consistent with impaired membrane insertion/stability. Its function is to be a "specific molecular chaperone assisting the folding/stability of core 1 beta-3-galactosyltransferase (C1GALT1)." Tissue expression is "ubiquitous... abundantly expressed in salivary gland, stomach, small intestine, kidney, and testis," matching the renal and gastrointestinal involvement seen clinically.

The gene *C1GALT1C1* is a **single-coding-exon, X-linked gene** at chrX:120,625,674–120,630,054 (Xq24). gnomAD v2 constraint shows a **missense Z = 1.63** (mildly constrained); standard LoF constraint metrics (pLI/LOEUF) are not computed for this small single-exon X-linked gene. RefSeq notes that mutations in this gene are associated with **Tn syndrome**. **Ontology:** GO:0005789 (ER membrane), GO:0051082 (unfolded protein binding / chaperone activity).

### Finding 5 — Model organisms: constitutive knockout is embryonic-lethal; mosaic/conditional models recapitulate Tn-antigen disease

In the mouse (NCBI Taxon 10090; ortholog *C1galt1c1*), global ablation of the X-linked *Cosmc* gene "causes embryonic lethality and Tn antigen expression," with loss of T-synthase but not other glycosyltransferases; genetically mosaic survivors "exhibited abnormalities correlated with Tn antigen expression that are related to several human diseases" ([PMID: 20439703](https://pubmed.ncbi.nlm.nih.gov/20439703/)). Tissue-specific conditional models confirm the glyco-phenotype: intestinal-epithelial Cosmc-KO mice "express CD175 throughout the intestinal epithelia" with glycocalyx loss, microvillar shortening, compromised MUC2, and high ROS ([PMID: 41759737](https://pubmed.ncbi.nlm.nih.gov/41759737/)); pancreas-specific Cosmc deletion cooperates with oncogenic KRAS in tumorigenesis ([PMID: 42537314](https://pubmed.ncbi.nlm.nih.gov/42537314/)). The human acquired analog is **Tn syndrome**, caused by somatic *COSMC* loss in hematopoietic clones producing persistent mixed-field polyagglutinability. **Resources:** MGI, IMPC, IMSR. **Limitation:** no model has yet been engineered to specifically reproduce the renal TMA + rhizomelic short stature combination of aHUS8; embryonic lethality of the full knockout necessitates conditional/mosaic strategies.

### Finding 6 — Diagnostics: biochemical glyco-phenotyping plus molecular confirmation; renal TMA on biopsy

Disease-specific confirmatory assays combine **biochemistry and molecular genetics**. Patient "red blood cells (RBCs), leukocytes, and serum... indicated reduced expression of Cosmc and T-synthase proteins and lower T-synthase activity" ([PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/)), and investigators "observed reduced normal O-glycans in serum glycoproteins and RBCs from the patient, along with elevated expression of the Tn-antigen in serum glycoproteins compared to controls" ([PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/)). Tn-antigen (CD175) is detectable by VVA (*Vicia villosa*) / HPA lectins, and RBCs show polyagglutination. Serum **galactose-deficient IgA1 (Gd-IgA1)** is elevated. Hematologic/renal labs reflect TMA: microangiopathic hemolytic anemia with schistocytes (HP:0001981), low haptoglobin (HP:0020181), thrombocytopenia (HP:0001873), elevated creatinine (HP:0003259), proteinuria (HP:0000093), plus cytopenias. **Molecular confirmation** is by whole-exome sequencing or targeted *C1GALT1C1* (AHUS8) sequencing; females require **mosaicism assessment** (buccal/tissue sampling, not blood alone). Renal biopsy shows **thrombotic microangiopathy**.

**Differential diagnosis** spans complement-mediated aHUS types 1–7 (*CFH*, *CD46/MCP*, *CFI*, *CFB*, *C3*, *THBD*, *DGKE*), STEC-HUS, pneumococcal (neuraminidase/T-antigen) HUS, TTP (ADAMTS13 deficiency), cobalamin C defect (*MMACHC*), and other CDGs. aHUS is classically "the triad of nonimmune haemolytic anaemia, thrombocytopenia, and acute renal failure, in which the underlying lesions are mediated by systemic thrombotic microangiopathy" ([PMID: 26456110](https://pubmed.ncbi.nlm.nih.gov/26456110/)).

### Finding 7 — Treatment and prognosis: C5 blockade controls the renal TMA; supportive multidisciplinary care for extrarenal disease

In the two male index patients, AKI resembling aHUS was fully responsive to **eculizumab** (anti-C5 mAb) ([PMID: 37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/)). This aligns with the established aHUS evidence base: "Eculizumab is a monoclonal antibody that inhibits the activation of C5 and blocks the generation of the pro-inflammatory molecule C5a and the formation of the cell membrane attack complex" ([PMID: 26456110](https://pubmed.ncbi.nlm.nih.gov/26456110/)), producing fast, sustained interruption of the TMA process with long-term renal improvement. Consensus guidelines position eculizumab (and plasma exchange where access is limited) as first-line for complement-mediated aHUS. Because C5 blockade raises the "risk of infection by encapsulated organisms, especially *Neisseria meningitis*" ([PMID: 28387984](https://pubmed.ncbi.nlm.nih.gov/28387984/)), **meningococcal vaccination and antibiotic prophylaxis are mandatory**.

**Extrarenal management is supportive and multidisciplinary:** transfusion for anemia/thrombocytopenia; infection prophylaxis and immunoglobulin replacement for immunodeficiency; growth and developmental support; and anti-seizure therapy. **NCIT terms:** Eculizumab (NCIT:C48479), Plasmapheresis/Plasma Exchange, Ravulizumab (long-acting anti-C5; plausible but unreported in aHUS8). The upstream glycosylation defect is **not yet correctable**; no gene/enzyme-replacement therapy exists.

### Finding 8 — Epidemiology and inheritance: ultra-rare X-linked recessive disorder

Prevalence and incidence are **not established** — aHUS8 is ultra-rare, with only a handful of reported individuals: two affected maternal half-brothers plus attenuated carrier mother and grandmother ([PMID: 37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/): "Here we identified two maternal half-brothers with a novel chaperonopathy, causing impaired protein O-glycosylation"), and one de novo mosaic female ([PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/): "This case represents the first description of a true mosaic loss-of-function variant in C1GALT1C1"). Inheritance is **X-linked recessive** (HP:0001419; gene at Xq24). Affected individuals are **hemizygous males**; obligate-carrier females show an attenuated phenotype associated with **skewed X-inactivation** in blood. A **de novo postzygotic mosaic** LoF variant (p.Arg68\*, ~27% of cells) can produce disease in a female. No founder effect, consanguinity requirement, or population enrichment is reported — consistent with private/novel variants. Carrier frequency is undefined in gnomAD (variants are private). Sex ratio is strongly **male-biased**.

### Finding 9 — Mechanistic link: Cosmc-driven Gd-IgA1 connects the glyco-defect to glomerular complement activation (IgA-nephropathy axis)

All four affected/carrier individuals in the index family had **high serum galactose-deficient IgA1 (Gd-IgA1)** ([PMID: 37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/)). IgA1's hinge-region O-glycans are Core-1 structures whose synthesis depends on the Cosmc/T-synthase machinery, so Cosmc deficiency directly produces Gd-IgA1. In IgA nephropathy, "Mesangial deposition of galactose-deficient IgA1 (Gd-IgA1) complexes remains the central pathogenic event" ([PMID: 42609724](https://pubmed.ncbi.nlm.nih.gov/42609724/)), driving the classical, lectin, and alternative complement pathways and linking mesangial complement activation, endothelial/leukocyte responses, podocyte injury, and tubulointerstitial exposure to proteinuria, glomerulosclerosis, and fibrosis. This provides a **second, biochemically demonstrated route** by which the Cosmc glyco-defect activates complement in the glomerulus, complementary to the direct endothelial-TMA route.

---

## Section-by-Section Report

### 1. Disease Information
- **Overview:** An X-linked congenital O-glycosylation chaperonopathy in which loss of the ER chaperone Cosmc causes Tn-antigen exposure and a multisystem disorder whose hallmark is atypical-HUS-like thrombotic microangiopathy accompanied by rhizomelic short stature, immunodeficiency, and neurodevelopmental delay.
- **Identifiers:** MONDO:0957495; OMIM #301110; gene *C1GALT1C1* (aliases AHUS8, COSMC, TNPS, C1GALT2). Orphanet/ICD-11/MeSH-specific codes for this precise entity are **not established** (too newly described); the generic ICD-11 category for aHUS is 3A21.2, and it falls under the broad concepts of atypical hemolytic-uremic syndrome and congenital disorders of glycosylation.
- **Synonyms:** aHUS8; AHUS8; hemolytic uremic syndrome, atypical, 8, with rhizomelic short stature; COSMC-CDG (proposed); Cosmc-associated chaperonopathy.
- **Information source:** Derived from **individual-patient case reports** (2 pedigree males + carriers; 1 mosaic female) plus mechanistic/model-organism studies — not from aggregated registries.

### 2. Etiology
- **Causal factor:** Monogenic — germline hemizygous or de novo mosaic loss-of-function variants in *C1GALT1C1*/Cosmc (Finding 1).
- **Genetic risk factors:** The causal variants themselves (c.59C>A/p.Ala20Asp hypomorphic transmembrane missense; c.202C>T/p.Arg68\* truncating). Male sex (hemizygosity) is the dominant risk factor; carrier females' risk is modulated by X-inactivation skewing (a modifier of expressivity).
- **Environmental risk factors:** None established as causal. As in other complement-mediated TMAs, intercurrent **infections** may act as complement-amplifying triggers for acute episodes (inferred).
- **Protective factors:** In carrier females, **favorable (non-skewed) X-inactivation** biasing toward the wild-type allele is protective (inferred from attenuated carrier phenotype). No environmental protective factors known.
- **Gene–environment interactions:** Not characterized; plausibly infection-triggered complement activation on a Tn-exposed endothelial surface (inferred).

### 3. Phenotypes
See Finding 3 and the HPO table. Phenotype **types** span laboratory abnormalities (hemolysis markers, cytopenias, proteinuria, elevated creatinine, Gd-IgA1), clinical signs (schistocytes, hyperechogenic kidneys, dysmorphism), physical manifestations (rhizomelic short stature), and neurobehavioral features (developmental delay, seizures). **Onset:** congenital/early childhood. **Severity:** severe and multisystem in hemizygous males and the mosaic female (hydrops); attenuated in carriers. **Progression:** AKI is episodic/acute on a chronic multisystem background. **QoL impact:** substantial — dialysis-level renal risk, recurrent infection burden, growth failure, and developmental impairment; formal EQ-5D/SF-36 data are **not available** for this ultra-rare entity.

### 4. Genetic / Molecular Information
- **Causal gene:** *C1GALT1C1* (NCBI 29071; ENSG00000171155; Xq24); OMIM gene/phenotype #301110.
- **Pathogenic variants:** c.59C>A p.(Ala20Asp) — missense, transmembrane signal-anchor, hypomorphic/reduced-expression; c.202C>T p.(Arg68\*) — nonsense, truncating, loss of function. Both are **novel/private** in ClinVar and **absent from gnomAD**. Functional consequence = **loss of chaperone function → secondary loss of T-synthase activity** (a loss-of-function mechanism).
- **Classification:** Pathogenic/likely pathogenic by ACMG criteria given functional validation and segregation, though formal ClinVar curation is pending (private variants).
- **Origin:** Germline (hemizygous males; carrier females) and **de novo postzygotic mosaic** (female case, ~27% buccal cells). No somatic-cancer relevance for this constitutional disease (though somatic *COSMC* loss causes acquired Tn syndrome).
- **Modifier genes/epigenetics:** **X-inactivation skewing** is the principal modifier in females. No other modifier loci or disease-specific DNA-methylation/histone changes have been reported.
- **Chromosomal abnormalities:** None — this is a single-gene SNV disorder.

### 5. Environmental Information
No environmental toxins, radiation, occupational exposures, or lifestyle factors are implicated as causes. **Infectious agents** are not the primary cause (distinguishing aHUS8 from STEC-HUS and pneumococcal HUS), but infections plausibly trigger acute complement-mediated flares and are clinically relevant given the comorbid immunodeficiency (inferred).

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**
1. Germline/mosaic **loss-of-function variant in *C1GALT1C1*** → **leads to** reduced/misfolded **Cosmc** chaperone in the ER.
2. Reduced Cosmc → **results in** misfolding and loss of activity of its client enzyme **T-synthase (C1GALT1)**.
3. T-synthase deficiency → **leads to** failure to add galactose to Tn-antigen, i.e., **no Core-1 T-antigen formation**.
4. **→ results in widespread Tn-antigen (CD175) neo-exposure** on cellular and secreted glycoproteins and on erythrocytes.
   - **Branch A (endothelial/TMA):** Tn-exposed glycoproteins + glycocalyx disruption + elevated ROS (shown in mouse) → **leads to** endothelial injury and complement activation on vascular surfaces → **results in** C5b-9–mediated microvascular thrombosis = **renal TMA (aHUS)**.
   - **Branch B (IgA/complement):** defective IgA1 hinge O-glycosylation → **produces galactose-deficient IgA1 (Gd-IgA1)** → **leads to** immune-complex formation and mesangial deposition → **activates classical/lectin/alternative complement** → **results in** glomerular injury, proteinuria.
   - **Branch C (extrarenal):** aberrant O-glycosylation of structural/immune/skeletal glycoproteins → **results in** immunodeficiency, rhizomelic short stature, neurodevelopmental delay, and dysmorphism (mechanism inferred).
5. Terminal complement (C5→C5a + C5b-9) is the **proximate effector** of renal injury → **therapeutically interruptible by eculizumab**.

**Pathways/processes:** O-glycan (mucin-type) biosynthesis (KEGG hsa00512); complement and coagulation cascades (KEGG hsa04610); ER protein folding/chaperone quality control; oxidative stress; thrombotic microangiopathy. **GO:** GO:0016266, GO:0006486, GO:0006956, GO:0030449 (regulation of complement activation), GO:0034976 (response to ER stress). **Protein dysfunction:** Cosmc loss of function → secondary T-synthase loss of function (enzyme deficiency). **Cell types involved:** glomerular endothelial cells (CL:1001005), mesangial cells (CL:0000650), podocytes (CL:0000653), erythrocytes (CL:0000232), platelets (CL:0000233), growth-plate chondrocytes (CL:0000138). **Molecular profiling specific to aHUS8** (patient transcriptomics/proteomics/metabolomics) is **not available**; supporting glycoproteomic data come from Cosmc-null cell/mouse models.

### 7. Anatomical Structures Affected
- **Primary organ:** Kidney (UBERON:0002113) — glomerulus (UBERON:0000074), renal microvasculature, renal cortex.
- **Secondary/other organs & systems:** Hematopoietic/blood (anemia, thrombocytopenia); immune system (immunodeficiency); skeletal system — long bones/growth plates (rhizomelic short stature, UBERON:0002495 long bone); central nervous system (developmental delay, seizures); craniofacial structures (dysmorphism); gastrointestinal tract (recurrent GI infection; Cosmc is abundant in intestine).
- **Tissue/cell level:** vascular endothelium, mesangium, erythrocytes, platelets, leukocytes, growth-plate chondrocytes.
- **Subcellular:** **ER membrane/lumen** (site of Cosmc/T-synthase folding; GO:0005789/GO:0005788); Golgi glycosylation machinery (downstream).
- **Localization/lateralization:** Bilateral/systemic (not lateralized).

### 8. Temporal Development
- **Onset:** Congenital/early childhood; most severe presentation is prenatal (nonimmune hydrops fetalis in the mosaic female).
- **Onset pattern:** Acute AKI episodes (TMA) superimposed on a chronic, congenital multisystem disorder.
- **Progression:** Variable; renal episodes are acute/episodic and responsive to C5 blockade; growth, immune, and neurodevelopmental features are chronic and persistent. Formal staging and natural-history data are **not established** (n too small).
- **Remission:** Treatment-induced remission of TMA with eculizumab/plasma exchange. **Critical period:** rapid recognition and complement blockade during acute AKI to preserve renal function.

### 9. Inheritance and Population
See Finding 8. **Inheritance:** X-linked recessive. **Penetrance:** high/complete in hemizygous males; variable/attenuated in carrier females (X-inactivation–dependent). **Expressivity:** variable. **Anticipation:** not applicable (not a repeat-expansion disorder). **Germline/somatic mosaicism:** demonstrated (female case). **Founder effect/consanguinity:** none reported. **Carrier frequency:** undefined (private variants). **Demographics:** no ethnic/geographic enrichment reported; strongly male-biased sex ratio; congenital/pediatric age distribution. **Prevalence/incidence:** not established (ultra-rare, <10 individuals).

### 10. Diagnostics
See Finding 6. **Recommended approach:** (1) recognize the aHUS triad + extrarenal multisystem features; (2) biochemical glyco-phenotyping — reduced Cosmc/T-synthase protein and activity, Tn-antigen/CD175 exposure (VVA/HPA lectins; RBC polyagglutination), elevated Gd-IgA1; (3) molecular confirmation by **WES** or targeted *C1GALT1C1* sequencing; (4) in females, **mosaicism assessment** across tissues (buccal, not blood alone); (5) **renal biopsy** showing TMA; (6) exclude ADAMTS13 deficiency (TTP), STEC/pneumococcal HUS, cobalamin C defect, and complement aHUS 1–7. WGS/WES are the key molecular tools; CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not indicated** (SNV disorder). **Omics diagnostics:** glycoproteomics/Gd-IgA1 assays are promising research-grade adjuncts.

### 11. Outcome / Prognosis
Survival, 5-/10-year outcome, and mortality statistics are **not established** for aHUS8 specifically. Prognostic drivers (inferred from aHUS and from the case series): **speed of complement blockade** governs renal recovery; the **comorbid immunodeficiency** adds infection-related morbidity/mortality risk; **growth and neurodevelopmental impairment** persist as chronic disability. The renal TMA is reversible with timely eculizumab; untreated/delayed aHUS risks ESRD or death. **QoL tools:** none applied in this entity. **Prognostic biomarkers:** TMA markers (schistocytes, haptoglobin, platelets, creatinine) track renal activity; Gd-IgA1 is a candidate but unvalidated for this disorder.

### 12. Treatment
See Finding 7. **Pharmacotherapy:** **eculizumab** (anti-C5 mAb; NCIT:C48479) — first-line for the renal TMA, with fast/sustained TMA interruption; **ravulizumab** (long-acting anti-C5) is a plausible alternative but unreported here; **plasma exchange** where anti-C5 access is limited. **Mandatory prophylaxis:** meningococcal vaccination + antibiotics due to encapsulated-organism risk during C5 blockade. **Supportive:** transfusion, immunoglobulin replacement/infection prophylaxis, growth support, anti-seizure therapy, developmental/rehabilitative services. **Advanced/experimental:** no gene, cell, RNA, or enzyme-replacement therapy exists for the Cosmc defect; the upstream glyco-lesion is **not yet correctable** — a key unmet need. **Pharmacogenomics:** none specific. **Personalized medicine:** complement-directed therapy is itself the genotype-concordant strategy for the TMA.

### 13. Prevention
- **Primary prevention:** None for disease occurrence (monogenic). Avoid/promptly treat infections that could trigger TMA (inferred).
- **Secondary prevention:** Early recognition and rapid complement blockade to prevent irreversible renal damage; monitoring of TMA labs.
- **Tertiary prevention:** Meningococcal vaccination/antibiotic prophylaxis during eculizumab; infection surveillance for immunodeficiency; growth/developmental monitoring.
- **Genetic screening/counseling:** X-linked recessive counseling; carrier testing of at-risk female relatives with X-inactivation assessment; **prenatal/preimplantation genetic testing** feasible where a familial variant is known; cascade testing. **Immunization:** meningococcal (and generally pneumococcal/Hib) vaccination before/with C5 inhibitors.

### 14. Other Species / Natural Disease
- **Taxonomy/orthologs:** Mouse *C1galt1c1* (NCBI Taxon 10090) is the principal ortholog; Cosmc/T-synthase O-glycan machinery is conserved across vertebrates.
- **Natural disease in animals:** No naturally occurring aHUS8 counterpart is documented in companion animals or wildlife (OMIA search not productive for this specific entity).
- **Comparative biology:** Mouse models (Finding 5) recapitulate the core glyco-defect (Tn/CD175 exposure, glycocalyx loss, ROS) but not the full aHUS8 phenotype; full knockout is embryonic lethal, indicating strong evolutionary conservation of Cosmc's essential role. **Zoonotic potential:** none (genetic disease).

### 15. Model Organisms
See Finding 5. **Mammalian mouse models:** global *Cosmc* knockout (embryonic-lethal; mosaic survivors model Tn disease; [PMID: 20439703](https://pubmed.ncbi.nlm.nih.gov/20439703/)); intestinal-epithelial conditional KO ([PMID: 41759737](https://pubmed.ncbi.nlm.nih.gov/41759737/)); pancreas-specific KO + KRAS ([PMID: 42537314](https://pubmed.ncbi.nlm.nih.gov/42537314/)). **Cellular/in vitro:** CRISPR *COSMC*-knockout cancer cell lines (MDA-MB-231, MCF7, T47D, Jurkat, LS174T, LL/2) that express Tn-antigen and have been used to dissect O-glycan–dependent biology ([PMID: 39074261](https://pubmed.ncbi.nlm.nih.gov/39074261/), [PMID: 32158257](https://pubmed.ncbi.nlm.nih.gov/32158257/)). **Model types available:** knockout, conditional/tissue-specific, mosaic. **Phenotype recapitulation:** strong for the molecular glyco-phenotype; **limitations:** no model yet reproduces the specific aHUS8 renal-TMA-plus-rhizomelic-short-stature constellation, and embryonic lethality forces conditional/mosaic approaches. **Resources:** MGI, IMPC, IMSR; iPSC/organoid and endothelial-specific conditional models are proposed but not yet reported for aHUS8.

---

## Mechanistic Model / Interpretation

```
  C1GALT1C1 LoF variant (hemizygous male / mosaic female)
            │  leads to
            ▼
  Reduced / misfolded Cosmc (ER chaperone, UniProt Q96EU7)
            │  results in
            ▼
  T-synthase (C1GALT1) misfolding → loss of activity
            │  leads to
            ▼
  No Core-1 T-antigen  →  Tn-antigen (CD175) EXPOSED on glycoproteome + RBCs
            │
   ┌────────┼───────────────────────────────┬─────────────────────────┐
   ▼ Branch A (endothelial)        Branch B (IgA)              Branch C (systemic)
 Glycocalyx loss, ↑ROS,         Galactose-deficient IgA1    Aberrant O-glycosylation of
 endothelial injury            → immune complexes →          skeletal/immune/neural
   │  activates complement      mesangial deposition →        glycoproteins
   ▼                             complement activation         │
 C5 → C5a + C5b-9 (MAC)          │                             ▼
   │ results in                  ▼                       Rhizomelic short stature,
 RENAL THROMBOTIC            Glomerular injury,          immunodeficiency, DD,
 MICROANGIOPATHY (aHUS)      proteinuria                 seizures, dysmorphism
   │
   ▼  ECULIZUMAB (anti-C5) interrupts here → renal recovery
```

The disease is a **single-lesion, multi-branch cascade**. The upstream lesion (Cosmc loss → Tn exposure) is shared by all phenotypes and by the Cosmc-null models and Tn syndrome; the downstream renal injury is complement-driven and **pharmacologically tractable at the C5 node**, explaining the dramatic eculizumab response despite an uncorrected upstream glyco-defect. Branches A and B offer two non-exclusive routes from the same glycosylation failure to complement-mediated kidney injury.

| Level | Upstream ↔ Downstream | Intervention point |
|---|---|---|
| Genetic | *C1GALT1C1* LoF (upstream) | Not yet druggable |
| Enzymatic | Cosmc → T-synthase loss | Not yet druggable |
| Glycan | Tn-antigen exposure | Not yet druggable |
| Effector | Complement C5 activation (downstream) | **Eculizumab (reversible)** |

---

## Evidence Base

| PMID | Title / type | Role in this report |
|---|---|---|
| [37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/) | *Germline Cosmc chaperonopathy* (PNAS 2023) — human, defining | Establishes gene (c.59C>A/p.Ala20Asp), phenotype, Gd-IgA1, and eculizumab response (Findings 1,2,3,7,8,9) |
| [39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/) | *C1GALT1C1-associated mosaic disorder of glycosylation in a female* (2025) — human | 2nd independent case (p.Arg68\* mosaic), biochemical diagnostics, mechanism (Findings 1,2,3,6,8) |
| [41759737](https://pubmed.ncbi.nlm.nih.gov/41759737/) | *Deletion of Cosmc in murine intestinal epithelia* — mouse | In vivo glyco-phenotype: CD175, glycocalyx loss, ROS (Findings 2,5) |
| [20439703](https://pubmed.ncbi.nlm.nih.gov/20439703/) | *Cosmc is an essential chaperone for O-glycosylation* — mouse | Embryonic lethality of global KO; mosaic survivors model Tn disease (Finding 5) |
| [26456110](https://pubmed.ncbi.nlm.nih.gov/26456110/) | *aHUS consensus document* — human/clinical | Defines aHUS triad; eculizumab mechanism (Findings 6,7) |
| [28387984](https://pubmed.ncbi.nlm.nih.gov/28387984/) | *Eculizumab in pediatric aHUS* — clinical | Meningococcal risk → prophylaxis (Finding 7) |
| [30989342](https://pubmed.ncbi.nlm.nih.gov/30989342/) | *HUS consensus guidelines (developing country)* — clinical | Plasma exchange/eculizumab positioning (Finding 7) |
| [42609724](https://pubmed.ncbi.nlm.nih.gov/42609724/) | *Complement as a driver in IgA nephropathy* (review 2026) | Gd-IgA1 → glomerular complement injury (Finding 9) |
| [42537314](https://pubmed.ncbi.nlm.nih.gov/42537314/) | *Cosmc loss + Kras in pancreas* — mouse | Conditional Cosmc model; Tn accumulation (Finding 5) |
| [39074261](https://pubmed.ncbi.nlm.nih.gov/39074261/), [32158257](https://pubmed.ncbi.nlm.nih.gov/32158257/) | COSMC-KO cancer cell lines | In vitro Tn models of O-glycan biology (Finding 5) |

**Evidence-type distribution:** 2 human disease-defining reports (constitutional aHUS8), multiple model-organism/in vitro Cosmc studies, and clinical/consensus aHUS literature. Causality for aHUS8 rests on **two independent human cases with concordant functional validation**, supported by a deep mechanistic literature on Cosmc/Tn biology.

---

## Limitations and Knowledge Gaps

- **Extreme rarity (n < 10):** No prevalence, incidence, survival, penetrance quantitation, or natural-history data; all clinical claims derive from case reports.
- **Single defining pedigree + one mosaic female:** genotype–phenotype correlations and the full phenotypic range are uncertain; carrier-female outcomes depend on X-inactivation that is incompletely characterized.
- **No aHUS8-specific omics:** patient transcriptomics/proteomics/metabolomics are absent; mechanism is inferred partly from Cosmc-null cancer/mouse models, which do not reproduce the renal-TMA + rhizomelic-short-stature phenotype.
- **Branch weighting unresolved:** the relative contribution of direct endothelial TMA (Branch A) vs Gd-IgA1/complement (Branch B) to the human kidney injury is not experimentally dissected.
- **No disease-specific model** reproduces aHUS8; constitutive KO is embryonic lethal.
- **Ontology/coding gaps:** Orphanet, ICD-10/11, and MeSH codes for this precise entity are not yet assigned; ClinVar curation of the two variants is pending.
- **Citation verification:** one citation snippet quoting the PNAS defining paper's variant text was flagged as a text-match mismatch during the investigation and should be verified against the published abstract before database ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Case ascertainment & registry:** Use GeneMatcher/MatchMaker Exchange to identify additional *C1GALT1C1* patients; build a natural-history registry to estimate penetrance, renal/developmental outcomes, and genotype–phenotype correlations.
2. **Endothelial disease model:** Generate endothelial-specific or kidney-organoid Cosmc-deficient models (and patient iPSC-derived endothelium/podocytes) to test whether Tn exposure directly triggers complement deposition and TMA under flow — dissecting Branch A vs Branch B.
3. **Biomarker validation:** Standardize Gd-IgA1, Tn-antigen (VVA/HPA lectin), and T-synthase activity assays as diagnostic/prognostic tools; correlate with TMA activity and treatment response.
4. **Therapeutic evaluation:** Assess ravulizumab (long-acting anti-C5) and complement-pathway alternatives; evaluate whether C5 blockade also mitigates Gd-IgA1–driven glomerular injury; explore chaperone-stabilizing or substrate-bypass strategies for the upstream glyco-defect.
5. **X-inactivation studies in carriers** across multiple tissues to define the protective threshold and refine counseling.
6. **Formal ontology/variant curation:** Submit both variants to ClinVar with functional evidence; request Orphanet/ICD-11/MeSH entries; verify the flagged PNAS citation snippet against the primary abstract.
7. **Prenatal/PGT pathway:** Establish validated prenatal and preimplantation testing protocols for known familial variants, including mosaicism-aware strategies.

---

*Report compiled from 9 confirmed findings and 24 reviewed papers across 5 investigation iterations. Evidence base centers on two human disease-defining reports ([PMID: 37216524](https://pubmed.ncbi.nlm.nih.gov/37216524/), [PMID: 39949072](https://pubmed.ncbi.nlm.nih.gov/39949072/)) supported by Cosmc/Tn model-organism and clinical aHUS literature.*


## Artifacts

- [OpenScientist final report](Hemolytic_Uremic_Syndrome_Atypical_8_With_Rhizomelic_Short_Stature-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hemolytic_Uremic_Syndrome_Atypical_8_With_Rhizomelic_Short_Stature-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 34 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 11 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (2 mentions) - replaced by `GO:0009101`
- `GO:0051082` (obsolete unfolded protein binding) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016266` (2 mentions) - the report calls it "O-glycan processing"; GO calls it **protein O-linked glycosylation via N-acetylgalactosamine**, and lists "O-glycan processing" among its other names
- `GO:0006486` (2 mentions) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**
- `HP:0020181` (2 mentions) - the report calls it "Decreased haptoglobin"; HP calls it **Decreased circulating haptoglobin concentration**, and lists "Decreased haptoglobin level" among its other names
- `HP:0003498` (1 mention) - the report calls it "Disproportionate short stature (rhizomelic)"; HP calls it **Disproportionate short stature**
- `HP:0001875` (1 mention) - the report calls it "Decreased neutrophil count"; HP calls it **Decreased total neutrophil count**
- `HP:0001888` (1 mention) - the report calls it "Decreased lymphocyte count"; HP calls it **Decreased total lymphocyte count**
- `HP:0004798` (1 mention) - the report calls it "Recurrent GI infection"; HP calls it **Recurrent infection of the gastrointestinal tract**, and lists "Recurrent gastrointestinal infections" among its other names
- `GO:0005789` (2 mentions) - the report calls it "ER membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names
- `GO:0051082` (1 mention) - the report calls it "unfolded protein binding / chaperone activity"; GO calls it **obsolete unfolded protein binding**
- `GO:0034976` (1 mention) - the report calls it "response to ER stress"; GO calls it **response to endoplasmic reticulum stress**, and lists "response to ER stress" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** Kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names

42 of 44 terms resolved to a current term; the rest could not be looked up either way.