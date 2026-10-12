---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-12T14:48:27.563705'
end_time: '2026-10-12T15:24:07.156296'
duration_seconds: 2139.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lung Disease, Immunodeficiency, and Chromosome Breakage Syndrome
  mondo_id: MONDO:0014984
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
citation_count: 12
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 13
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 10
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014984
    reported_labels:
    - MONDO
    ontology_label: lung disease, immunodeficiency, and chromosome breakage syndrome;
  - term_id: HP:0005354
    reported_labels:
    - Combined immunodeficiency
    ontology_label: obsolete Absent cellular immunity
  - term_id: UBERON:0002048
    reported_labels:
    - Primary organ:** Lung
    ontology_label: lung
  labels_variant: 3
  obsolete_terms:
  - term_id: HP:0005354
    ontology_label: obsolete Absent cellular immunity
    replaced_by: HP:0011840
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lung_Disease_Immunodeficiency_and_Chromosome_Breakage_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lung_Disease_Immunodeficiency_and_Chromosome_Breakage_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lung Disease, Immunodeficiency, and Chromosome Breakage Syndrome
- **MONDO ID:** MONDO:0014984 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lung Disease, Immunodeficiency, and Chromosome Breakage Syndrome** covering all of the
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

# Lung Disease, Immunodeficiency, and Chromosome Breakage Syndrome (LICS) — Comprehensive Disease Characterization

**MONDO:** MONDO:0014984 · **OMIM:** #617241 · **Gene:** *NSMCE3* (NDNL2 / MAGEG1) · **Category:** Mendelian, autosomal recessive

---

## Summary

**Lung Disease, Immunodeficiency, and Chromosome Breakage Syndrome (LICS)** is an ultra-rare, autosomal-recessive Mendelian disorder caused by **biallelic missense mutations in *NSMCE3*** (also called *NDNL2* / *MAGEG1*), a subunit of the **SMC5/6 genome-maintenance complex**. The disease was first defined in 2016 by whole-exome sequencing of four children from two unrelated kindreds who died of severe pulmonary disease in infancy following viral pneumonia, with combined T- and B-cell immunodeficiency and constitutional chromosome breakage [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/). LICS belongs to an emerging "SMC5/6 complexopathy" spectrum alongside *NSMCE2*- and *SMC5*-related microcephalic primordial dwarfism.

The central molecular lesion is destabilization of the SMC5/6 complex: the pathogenic variants **p.Leu264Phe (c.790C>T)** and **p.Pro209Leu (c.626C>T)** abolish NSE3's binding to its partner subunits within the NSE1/NSE3/NSE4 module. Because NSE3 directly binds double-stranded DNA and this module is required to load SMC5/6 onto chromatin, the variants collapse a DNA-binding/loading function, producing defective homologous recombination, sensitivity to replication stress, chromosome rearrangements, and micronuclei. The resulting cellular phenotype is cell-intrinsic.

Clinically, the defining and most lethal feature is **viral-triggered diffuse alveolar damage / pediatric acute respiratory distress syndrome (PARDS)** that progresses to irreversible interstitial fibrosis, refractory to corticosteroids and to hematopoietic stem-cell transplantation (HSCT). The immunodeficiency is variable (T-cell predominant) and does not fully explain the lung disease. Death typically occurs in infancy to early childhood, though extended survival to 6.5 years and a fatal case at 11 years have been reported. A plausible but **inferred** amplifying mechanism links constitutional chromosome instability (micronuclei/chromatin bridges) to cGAS-STING/type-I-interferon signalling driving pulmonary fibrosis — this branch has not been directly demonstrated in LICS lung tissue. No curative therapy exists; management is supportive with genetic counselling for at-risk families.

---

## Section 1 — Disease Information

**Overview.** LICS is a Mendelian chromosome-instability (chromosome-breakage) syndrome characterized by the triad of (1) severe, often fatal early-childhood lung disease (ARDS/PARDS), (2) combined (predominantly T-cell) immunodeficiency, and (3) spontaneous chromosome breakage/rearrangements with micronuclei. It is caused by destabilization of the SMC5/6 complex through biallelic *NSMCE3* mutations [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014984 |
| OMIM | #617241 (Lung disease, immunodeficiency, and chromosome breakage syndrome, LICS) |
| Gene (OMIM) | *NSMCE3* 608243 |
| HGNC gene | *NSMCE3* |
| Cytogenetic locus | 15q13 |
| Inheritance | Autosomal recessive |

**Synonyms / alternative names.** LICS; Lung disease–immunodeficiency–chromosome breakage syndrome; SMC5/6 complex deficiency due to NSMCE3; NDNL2-related / MAGEG1-related chromosome breakage syndrome.

**Information source.** Knowledge is derived from aggregated disease-level resources (OMIM, Orphanet) and a small number of primary case reports/series totaling roughly a dozen genetically confirmed patients worldwide. This is **not** EHR/individual-patient-registry derived — the literature base is case reports and small kindred studies.

---

## Section 2 — Etiology

**Primary cause (genetic).** LICS is a monogenic disorder caused by biallelic (homozygous or compound-heterozygous) missense mutations in *NSMCE3*, which encodes a non-SMC element of the SMC5/6 complex essential for the DNA-damage response and chromosome segregation [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).

**Genetic risk factors.** The disease-causing alleles are the risk factors themselves:
- **c.790C>T, p.Leu264Phe** (rs199905054; homozygous in the original and 2021 cohorts; OMIM variant 608243.0001)
- **c.626C>T, p.Pro209Leu** (NM_138704.3; compound-heterozygous; OMIM variant 608243.0002)

Consanguinity and founder effects increase homozygosity risk, consistent with the recessive inheritance and the recurrence of p.L264F across kindreds. No established modifier genes are documented, though variable immunophenotype suggests unidentified modifiers or stochastic/environmental contributions.

**Environmental risk / trigger factors.** Although the underlying defect is constitutional, **viral respiratory infection is the principal environmental trigger** of the lethal lung disease. In the original cohort, fatal pulmonary disease followed viral pneumonia [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/); multiple viral infections were implicated in subsequent cases.

**Protective factors.** None established. No protective variants or lifestyle/dietary factors are known for this ultra-rare disorder.

**Gene–environment interaction.** The core GxE axis is **germline SMC5/6 destabilization × viral infection → ARDS**. SMC5/6 is itself a broad-spectrum antiviral restriction factor (Section 6); loss of complex function may impair control of viral episomes while the genome-instability phenotype sensitizes the host to infection-driven immunopathology. This interaction is plausible but mechanistically incompletely resolved.

---

## Section 3 — Phenotypes

LICS phenotypes cluster into three domains. Suggested HPO terms are provided; frequencies are qualitative given the small cohorts.

| Phenotype | Type | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Severe lung disease / ARDS (diffuse alveolar damage, PARDS) | Clinical sign / imaging-histopathology | Infancy–early childhood | Severe, rapidly progressive, irreversible; often fatal | Core (defining); near-universal in symptomatic cases | HP:0002878 (Respiratory failure); HP:0002090 (Pneumonia); HP:0006536 (Obstructive lung disease) |
| Interstitial pulmonary fibrosis | Physical/histopathological | After viral insult | Progressive | Frequent | HP:0002206 (Pulmonary fibrosis) |
| Combined immunodeficiency (T-cell predominant) | Laboratory abnormality | Infancy | Variable (severe to limited) | Variable | HP:0005354 (Combined immunodeficiency) |
| Decreased T-cell count / proliferation | Laboratory abnormality | Infancy | Variable | Common in original cohort | HP:0005403 (Decreased T cell count); HP:0012177 |
| Impaired antibody responses | Laboratory abnormality | Infancy | Variable | Common | HP:0004313 (Decreased antibody level) |
| Recurrent/viral respiratory infections | Symptom | Infancy | Variable; may be absent | Variable | HP:0002788 (Recurrent respiratory infections) |
| Chromosome breakage / rearrangements, micronuclei, marker chromosomes | Laboratory (cytogenetic) | Congenital (constitutional) | Stable cellular trait | Universal | HP:0040012 (Chromosome breakage) |
| Hypoglycemia | Laboratory abnormality | Infancy | Variable | Reported (2021+) | HP:0001943 (Hypoglycemia) |
| Hepatomegaly | Clinical sign | Infancy | Variable | Reported (2021+) | HP:0002240 (Hepatomegaly) |

**Age of onset:** neonatal to early-childhood; **severity:** severe for the lung phenotype, variable for immunodeficiency; **progression:** lung disease is progressive and irreversible once triggered.

**Quality of life.** Given infant/early-childhood lethality, the dominant QoL burden is respiratory failure requiring intensive care; formal QoL instruments (EQ-5D/SF-36) are not applicable/not reported.

Supporting evidence: "Four children from two unrelated kindreds died of severe pulmonary disease during infancy following viral pneumonia with evidence of combined T and B cell immunodeficiency" [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/); "the immunological abnormalities can be limited and do not fully explain the LICS phenotype" [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/).

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *NSMCE3* (NDNL2 / MAGEG1), OMIM 608243, cytogenetic locus **15q13**, encoding a non-SMC element 3 subunit of the SMC5/6 complex. NSE3/MAGEG1 is the founding member of the MAGE (melanoma-associated antigen) protein family and partners with the NSE4 kleisin (EID-family) subunit [PMID: 22536443](https://pubmed.ncbi.nlm.nih.gov/22536443/).

**Pathogenic variants.**

| Variant (cDNA) | Protein | Zygosity | dbSNP / OMIM allele | Functional consequence |
|---|---|---|---|---|
| c.790C>T | p.Leu264Phe | Homozygous (original + 2021 cohorts) | rs199905054 / 608243.0001 | Abolishes NSE3–NSE4 binding |
| c.626C>T | p.Pro209Leu | Compound-heterozygous | NM_138704.3 / 608243.0002 | Abolishes NSE3 binding to both NSE4 and NSE1 |

**Variant classification:** Pathogenic (ACMG/AMP) — biallelic, co-segregating, functionally validated. **Variant type:** missense. **Allele frequency:** rare; p.L264F (rs199905054) present at very low frequency in population databases, consistent with a recessive hypomorph. **Origin:** germline. **Functional consequence:** **loss of function** via complex destabilization — patient cells show undetectable NSE3 protein with secondarily decreased SMC5 and SMC6, increased genotoxin sensitivity, and defective homologous recombination; non-homologous end joining and V(D)J recombination are normal [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).

**Chromosomal abnormalities (acquired, in patient cells).** Karyotyping of peripheral lymphocytes showed **multiple de novo supernumerary marker chromosomes**, chromosome rearrangements, and **micronuclei** — hallmarks of constitutional chromosome instability rather than a single recurrent rearrangement.

**Modifier genes / epigenetics.** No validated modifiers or disease-specific epigenetic marks are reported. The variable immunophenotype hints at modifiers but none are mapped.

**Complexopathy context.** Three SMC5/6 subunits now map to distinct recessive disorders: *NSMCE3* → LICS; *NSMCE2* (MMS21) → primordial dwarfism/insulin resistance/gonadal failure [PMID: 25105364](https://pubmed.ncbi.nlm.nih.gov/25105364/); *SMC5* (in-frame Arg372 deletion) → microcephalic primordial dwarfism with chromosomal instability and insulin resistance [PMID: 36627765](https://pubmed.ncbi.nlm.nih.gov/36627765/).

---

## Section 5 — Environmental Information

**Environmental factors.** No chemical/radiation/occupational exposures are implicated in disease causation (the cause is genetic). However, patient cells are hypersensitive to **genotoxic/replication-stress agents** in vitro, meaning DNA-damaging exposures would be expected to be poorly tolerated.

**Lifestyle factors.** Not applicable (disease manifests in infancy/early childhood).

**Infectious agents.** **Viral respiratory infection is the dominant disease trigger.** Fatal pulmonary disease followed viral pneumonia in the index cases [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/); multiple viruses have been implicated across cases. No single causative pathogen is required — the host SMC5/6 defect converts common viral infection into lethal immunopathology. Mechanistically relevant, SMC5/6 restricts episomal DNA viruses (e.g., HBV cccDNA) [PMID: 42793236](https://pubmed.ncbi.nlm.nih.gov/42793236/).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *NSMCE3* missense mutation** (p.L264F and/or p.P209L) → **results in** loss/abolition of NSE3 binding to NSE4 (and NSE1 for P209L) within the NSE1/NSE3/NSE4 module [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).
2. Loss of intra-module interactions → **leads to** destabilization of the whole SMC5/6 complex (undetectable NSE3; secondary loss of SMC5 and SMC6) [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).
3. Because the NSE1/NSE3/NSE4 module **binds double-stranded DNA** and is required for chromatin loading, complex destabilization → **leads to** reduced SMC5/6 association with chromatin [PMID: 26446992](https://pubmed.ncbi.nlm.nih.gov/26446992/).
4. Impaired SMC5/6 chromatin function → **results in** defective homologous recombination and reduced tolerance of replication stress / DNA damage [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).
5. Defective HR/replication-fork maintenance → **leads to** chromosome rearrangements, supernumerary marker chromosomes, and **micronuclei** (constitutional chromosome instability) [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).
6. **Branch A (immune):** chromosome instability + loss of SMC5/6 → **results in** impaired lymphocyte development/function → T-cell–predominant combined immunodeficiency (variable) [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).
7. **Branch B (shared apoptosis):** SMC5/6 dysfunction → **triggers** p53-dependent apoptosis (demonstrated for SMC5 depletion in zebrafish, rescued by p53 co-deletion) [PMID: 36627765](https://pubmed.ncbi.nlm.nih.gov/36627765/) — likely contributing to cell loss across tissues.
8. **Trigger:** viral respiratory infection in this sensitized host → **leads to** diffuse alveolar damage / PARDS.
9. Diffuse alveolar damage with hyaline membranes, alveolar septal thickening → **progresses to** early interstitial fibrosis and metaplastic squamous alveolar epithelium (autopsy findings) → **results in** irreversible respiratory failure and death [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/).
10. **Inferred amplifying branch (not demonstrated in LICS):** micronuclei/chromatin bridges → cytosolic DNA → **cGAS → 2′3′-cGAMP → STING** activation → chronic type-I-interferon/pro-inflammatory signalling → **fibrotic remodeling** of lung [PMID: 36876871](https://pubmed.ncbi.nlm.nih.gov/36876871/); [PMID: 42559700](https://pubmed.ncbi.nlm.nih.gov/42559700/). Caveat: a single-cell cGAMP-reporter study found genotoxic-stress cGAS activation is a rare event not driven primarily by micronuclei enrichment [PMID: 42629426](https://pubmed.ncbi.nlm.nih.gov/42629426/).

### Mechanistic detail by category

- **Molecular pathways:** SMC5/6-mediated DNA repair/replication-fork maintenance and homologous recombination; SUMO/ubiquitin regulation (NSMCE2 is the complex's SUMO E3 ligase); p53-dependent apoptosis downstream of complex failure; inferred cGAS-STING/type-I-IFN innate-immune signalling.
- **Cellular processes:** Cell-cycle/replication-stress response, homologous recombination (GO:0000724 double-strand break repair via homologous recombination), chromosome segregation (GO:0007059), apoptosis (GO:0006915), innate immune/inflammatory signalling (GO:0002376).
- **Protein dysfunction:** Loss-of-function via complex destabilization — a scaffolding/assembly defect rather than catalytic loss. NSE3 directly binds dsDNA within the NSE1/NSE3/NSE4 module; mutating this surface reduces DNA binding and chromatin association in fission yeast and causes genotoxin hypersensitivity/cell death [PMID: 26446992](https://pubmed.ncbi.nlm.nih.gov/26446992/).
- **Immune system involvement:** Primary combined immunodeficiency (variable, T-cell predominant); SMC5/6 is also an antiviral restriction factor that transcriptionally silences episomal viral genomes — the **NSE1/NSE3 subcomplex alone is sufficient to inhibit transcription in vitro**, and NSMCE3 knockdown promotes HBV proliferation [PMID: 41825673](https://pubmed.ncbi.nlm.nih.gov/41825673/); [PMID: 42793236](https://pubmed.ncbi.nlm.nih.gov/42793236/).
- **Tissue damage mechanisms:** Viral-triggered diffuse alveolar damage → interstitial fibrosis (hyaline membranes, septal thickening, squamous metaplasia).
- **Suggested GO/CL terms:** GO:0000724, GO:0007059, GO:0006915, GO:0140374 (antiviral innate immune response); cell types CL:0000084 (T cell), CL:0000236 (B cell), CL:0002063 (type II pneumocyte), CL:0000066 (epithelial cell), CL:0000057 (fibroblast).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ:** Lung (UBERON:0002048) — alveoli (UBERON:0002299), alveolar septa, alveolar epithelium.
- **Secondary / systemic:** Immune system / lymphoid organs (bone marrow, thymus, peripheral lymphoid tissue); liver (hepatomegaly, UBERON:0002107) reported in later cases.
- **Body systems:** Respiratory system (primary); immune/hematopoietic system; chromosomal instability is a whole-organism cellular trait.
- **Tissue/cell level:** Alveolar epithelium (type II pneumocytes, CL:0002063), interstitial fibroblasts (CL:0000057), T lymphocytes (CL:0000084), B lymphocytes (CL:0000236).
- **Subcellular level:** Nucleus/chromatin (GO:0000785), chromosome (GO:0005694), micronucleus; DNA-repair machinery. SMC5/6 is a nuclear chromatin-associated complex.
- **Localization / lateralization:** Lung involvement is bilateral and diffuse (diffuse alveolar damage).

---

## Section 8 — Temporal Development

- **Onset:** Congenital genetic defect; clinical onset in infancy to early childhood, typically precipitated **acutely/subacutely by viral infection**.
- **Progression:** Lung disease is rapidly progressive and irreversible once diffuse alveolar damage is established, evolving to interstitial fibrosis. Chromosome instability is a stable constitutional cellular trait.
- **Disease course:** Progressive respiratory decline culminating in fatal respiratory failure; immunodeficiency ranges from severe to clinically limited.
- **Duration / outcome:** Frequently fatal in infancy to early childhood (death reported at ~11 and 15 months in some cases), with extended survival to **6.5 years** in one patient [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/) and a fatal case at **11 years** (Chen 2025, [PMID: 40728043](https://pubmed.ncbi.nlm.nih.gov/40728043/)).
- **Critical period / window for intervention:** Prevention/aggressive control of viral respiratory infection in early childhood is the plausible window; no intervention reliably halts established lung disease.

---

## Section 9 — Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic *NSMCE3*) [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/).
- **Epidemiology:** Ultra-rare; only ~a dozen genetically confirmed patients described worldwide across a handful of kindreds. Formal prevalence/incidence are not established (too few cases); Orphanet-level "ultra-rare."
- **Penetrance / expressivity:** The lung/chromosome-breakage phenotype appears highly penetrant in biallelic patients; immunophenotype shows **variable expressivity** (severe to limited) [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effect / consanguinity:** Recurrence of homozygous c.790C>T p.L264F across unrelated kindreds suggests a possible founder allele; recessive inheritance implies a consanguinity contribution in some families.
- **Carrier frequency:** Not formally established; expected very low given rarity.
- **Population demographics / sex ratio / geography:** No established ethnic predilection, sex bias, or geographic clustering; cases reported from multiple regions. Sex ratio not established.

---

## Section 10 — Diagnostics

**Cytogenetics / chromosome breakage testing.** Karyotype of peripheral lymphocytes reveals chromosome rearrangements, **supernumerary marker chromosomes**, and increased micronuclei; cells show hypersensitivity to replication stress/DNA-damaging agents and defective homologous recombination (with normal NHEJ and V(D)J recombination) [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/). Micronucleus/chromosome-breakage assays and genotoxin-sensitivity testing are informative.

**Immunologic work-up.** Decreased T-cell numbers, decreased T-cell proliferative responses, and impaired antibody responses with **normal B-lymphocyte numbers** — a combined, T-cell-predominant immunodeficiency; may be limited in some patients [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/); [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/).

**Laboratory:** Hypoglycemia reported in later cases; monitor hepatic status (hepatomegaly).

**Imaging / histopathology.** Chest imaging shows diffuse interstitial/alveolar disease (ARDS/PARDS). Lung histopathology: **classic diffuse alveolar damage with hyaline membranes, extensive alveolar septal thickening, early interstitial fibrosis, and metaplastic squamous alveolar epithelium** — without evidence of ongoing infection at autopsy [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/).

**Genetic testing (definitive).** Whole-exome (or whole-genome) sequencing established the diagnosis in the index families [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/). Recommended approach: **WES/WGS** or a chromosome-instability/primary-immunodeficiency gene panel including *NSMCE3*; confirmatory single-gene *NSMCE3* sequencing for known familial variants; functional confirmation (SMC5/6 protein levels, HR assays). Chromosomal microarray/karyotype supports the breakage phenotype but does not identify the point mutation.

**Clinical criteria / differential diagnosis.** No formal consensus criteria exist. Differentials: other chromosome-breakage/instability syndromes — **Nijmegen breakage syndrome, ataxia-telangiectasia, Fanconi anemia, Bloom syndrome, ICF syndrome** — and SMC5/6 complexopathies (*NSMCE2*, *SMC5* — which instead present with microcephalic primordial dwarfism and insulin resistance, distinguishing them from LICS). The distinctive LICS combination is **lethal viral-triggered lung disease + chromosome breakage + variable combined immunodeficiency**.

**Screening.** Carrier/cascade testing for known familial *NSMCE3* variants; prenatal/preimplantation genetic testing feasible in families with an identified genotype.

---

## Section 11 — Outcome / Prognosis

- **Prognosis:** Poor. Frequently fatal in infancy to early childhood from progressive respiratory failure. Reported survival spans death before 2–3 years in the original cohort to extended survival of 6.5 years and a fatal case at 11 years [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/); [PMID: 40728043](https://pubmed.ncbi.nlm.nih.gov/40728043/).
- **Disease-specific mortality:** Lung disease is the principal cause of death.
- **Complications:** Respiratory failure, recurrent/severe viral infections, interstitial fibrosis, hypoglycemia, hepatomegaly.
- **Recovery potential:** Low — established lung disease is irreversible and refractory to corticosteroids; **HSCT failed to cure** a patient, indicating the lung phenotype is cell-intrinsic (not corrected by immune reconstitution) [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/).
- **Prognostic factors:** Severity/recurrence of viral respiratory infection and the degree of lung involvement drive outcome; immunodeficiency severity is variable and does not fully predict the lethal lung phenotype.

---

## Section 12 — Treatment

**No curative therapy exists.** Care is supportive and largely ineffective at reversing the lung disease.

- **Pharmacotherapy:** Corticosteroids (e.g., methylprednisolone) have been used but did not prevent death [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/). Antimicrobial/antiviral prophylaxis and immunoglobulin replacement are reasonable for the immunodeficiency component (supportive; NCIT: Corticosteroid Therapy; Intravenous Immunoglobulin Therapy).
- **Advanced therapeutics:** **Hematopoietic stem-cell transplantation failed to cure** a patient — consistent with a cell-intrinsic, non-hematopoietic lung mechanism [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/) (NCIT: Hematopoietic Stem Cell Transplantation). No gene/RNA/targeted therapies are available or trialed.
- **Supportive / rehabilitative:** Intensive respiratory support (oxygen, mechanical ventilation) for ARDS/PARDS; nutritional and infection management.
- **Experimental:** None registered specifically for LICS.
- **Treatment strategy / personalized medicine:** Genotype-guided diagnosis enables genetic counselling and infection-avoidance strategies; no molecularly targeted therapy exists. Theoretically, modulating downstream inflammatory amplifiers (e.g., cGAS-STING/type-I-IFN) is a conceptual target but entirely unproven for LICS.

---

## Section 13 — Prevention

- **Primary prevention:** Not possible for the genetic defect. The most actionable measure is **minimizing/aggressively managing viral respiratory infection** in affected children, given the viral trigger of lethal lung disease (routine immunizations and infection-control measures are reasonable, though unproven to prevent the phenotype).
- **Secondary prevention:** Early molecular diagnosis; vigilant monitoring and prompt treatment of respiratory infections.
- **Tertiary prevention:** Supportive respiratory care to manage complications (limited efficacy).
- **Genetic screening / counselling:** Carrier testing, cascade testing, and prenatal/preimplantation genetic testing for families with a known *NSMCE3* genotype; genetic counselling regarding 25% recurrence risk in autosomal-recessive inheritance.
- **Behavioral/public-health/environmental:** Infection-avoidance guidance for the family; avoid unnecessary genotoxic exposures given cellular hypersensitivity.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** *NSMCE3*/NSE3 is evolutionarily conserved. Orthologs/paralogs are well studied in *S. pombe* and *S. cerevisiae* (Nse3), Arabidopsis, and zebrafish; the mammalian ortholog is NSE3/MAGEG1 [PMID: 22536443](https://pubmed.ncbi.nlm.nih.gov/22536443/).
- **Natural disease in other species:** No naturally occurring LICS-equivalent disease is documented in companion animals or wildlife (OMIA); LICS is a human Mendelian disorder.
- **Comparative biology:** SMC5/6 function is deeply conserved; yeast *nse3* DNA-binding mutants show reduced chromatin association and genotoxin hypersensitivity/cell death [PMID: 26446992](https://pubmed.ncbi.nlm.nih.gov/26446992/), and *smc5*-knockout zebrafish show microcephaly/short length with p53-dependent apoptosis rescued by p53 co-deletion [PMID: 36627765](https://pubmed.ncbi.nlm.nih.gov/36627765/) — illustrating conservation of the apoptotic response to complex dysfunction.
- **Transmission / zoonotic potential:** Not applicable (non-infectious, genetic disease).

---

## Section 15 — Model Organisms

- **Yeast (*S. pombe* / *S. cerevisiae*):** The foundational system for NSE3 DNA-binding and chromatin-loading function. Hypomorphic *nse3* DNA-binding mutants show reduced SMC5/6–chromatin association and genotoxin hypersensitivity/cell death [PMID: 26446992](https://pubmed.ncbi.nlm.nih.gov/26446992/) — directly relevant to the LICS loss-of-loading mechanism. Budding yeast illuminated SMC5/6 regulation of Sgs1/STR recombination and SUMO-dependent control.
- **Zebrafish:** *smc5*-knockout reproduces microcephaly/short body length via **p53-dependent apoptosis** (rescued by p53 co-deletion) [PMID: 36627765](https://pubmed.ncbi.nlm.nih.gov/36627765/) — a model for the SMC5/6 complexopathy spectrum (more directly for the SMC5/NSMCE2 dwarfism phenotypes than for LICS lung disease).
- **Cellular / in vitro:** Patient-derived cells are the principal LICS model, demonstrating undetectable NSE3 protein, secondary SMC5/SMC6 loss, defective HR, genotoxin hypersensitivity, chromosome rearrangements, and micronuclei [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/). In vitro reconstitution shows the NSE1/NSE3/NSE4 module binds dsDNA [PMID: 26446992](https://pubmed.ncbi.nlm.nih.gov/26446992/) and the NSE1/NSE3 subcomplex suffices to inhibit transcription [PMID: 41825673](https://pubmed.ncbi.nlm.nih.gov/41825673/).
- **Model limitations:** No dedicated mammalian model recapitulates the **viral-triggered lethal lung disease** that defines LICS; existing models capture chromosome-instability and apoptosis but not the pulmonary immunopathology. A conditional/humanized *Nsmce3* mouse challenged with respiratory virus is the key missing model.
- **Resources:** MGI, ZFIN, PomBase/SGD; Alliance of Genome Resources for orthology.

---

## Mechanistic Model / Interpretation

```
 Biallelic NSMCE3 missense (p.L264F / p.P209L)
        |  abolishes NSE3-NSE4 (+/-NSE1) binding
        v
 SMC5/6 complex DESTABILIZED (down NSE3, SMC5, SMC6)
        |  NSE1/NSE3/NSE4 module normally binds dsDNA & loads complex
        v
 reduced SMC5/6 chromatin loading  ->  defective HR + replication-stress intolerance
        |
        v
 Constitutional CHROMOSOME INSTABILITY (rearrangements, marker chromosomes, micronuclei)
        |---------------+----------------------------+
        v               v                            v
 p53-dependent    Combined (T-cell-pred.)     [INFERRED] micronuclei -> cGAS-STING
 apoptosis        immunodeficiency (variable)  -> type-I IFN -> pro-fibrotic signalling
        |               |                            |
        +---------------+-------------+--------------+
                                      v
            VIRAL RESPIRATORY INFECTION (trigger; SMC5/6 is antiviral RF)
                                      v
            Diffuse alveolar damage / PARDS -> interstitial fibrosis
                                      v
            Irreversible respiratory failure -> death (infancy-early childhood)
```

The unifying interpretation is that a **scaffolding/assembly loss-of-function** in SMC5/6, driven by NSE3 destabilization, produces genome instability that is cell-intrinsic across tissues. Two phenotypic domains (immunodeficiency and chromosome breakage) are directly explained by impaired HR/genome maintenance in dividing cells. The **lethal lung phenotype is only partially explained** by the immunodeficiency (it is not corrected by HSCT, and immunodeficiency can be clinically limited), implying an additional cell-intrinsic lung-epithelial/fibrotic mechanism — for which the micronuclei → cGAS-STING → type-I-IFN → fibrosis axis is an attractive but **unproven, inferred** candidate. Viral infection is the universal clinical trigger, consistent with SMC5/6's dual role as both genome guardian and antiviral restriction factor.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/) | *Destabilized SMC5/6 complex leads to chromosome breakage syndrome with severe lung disease* | **Primary/defining paper** — identifies biallelic *NSMCE3* mutations, complex destabilization, clinical triad, cellular phenotypes |
| [33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/) | *New insights in phenotype and treatment of LICS* | Follow-up cohort (n=5): variable immunodeficiency, lung histopathology (DAD/fibrosis), HSCT failure, survival to 6.5 y |
| [40728043](https://pubmed.ncbi.nlm.nih.gov/40728043/) | *Fatal lung disease caused by NSMCE3 mutation in an 11-year-old boy* | Extends age range of fatal disease to 11 years |
| [26446992](https://pubmed.ncbi.nlm.nih.gov/26446992/) | *Chromatin association of SMC5/6 depends on NSE3 binding to DNA* | Mechanistic link — NSE3 DNA-binding module required for chromatin loading; mutants hypersensitive |
| [22536443](https://pubmed.ncbi.nlm.nih.gov/22536443/) | *Analysis of the Nse3/MAGE-binding domain of Nse4/EID proteins* | NSE3/MAGEG1 identity and NSE4-kleisin partnership |
| [36627765](https://pubmed.ncbi.nlm.nih.gov/36627765/) | *In-frame deletion of SMC5 — primordial dwarfism, instability, insulin resistance* | Complexopathy spectrum; p53-dependent apoptosis in zebrafish |
| [25105364](https://pubmed.ncbi.nlm.nih.gov/25105364/) | *Hypomorphism in human NSMCE2 — primordial dwarfism and insulin resistance* | Complexopathy spectrum (differential diagnosis) |
| [42793236](https://pubmed.ncbi.nlm.nih.gov/42793236/) | *The Multifunctional SMC5/6 Complex...Antiviral Restriction, and Human Disease* | SMC5/6 as broad-spectrum antiviral restriction factor |
| [41825673](https://pubmed.ncbi.nlm.nih.gov/41825673/) | *Mechanism insights into Smc5/6 in HBV inhibition* | NSE1/NSE3 subcomplex suffices for transcriptional silencing |
| [36592669](https://pubmed.ncbi.nlm.nih.gov/36592669/) | *Critical HBx residues for Smc5/6 interaction* | Viral evasion of SMC5/6 (host–virus axis) |
| [36876871](https://pubmed.ncbi.nlm.nih.gov/36876871/) | *cGAS-STING signalling in cancer / chromosomal instability* | Supports inferred CIN→micronuclei→cGAS-STING axis |
| [42559700](https://pubmed.ncbi.nlm.nih.gov/42559700/) | *Hyper-aging in systemic sclerosis — genome instability, inflammaging, fibrosis* | Links cGAS-STING/type-I-IFN to lung fibrosis (inferred branch) |
| [42629426](https://pubmed.ncbi.nlm.nih.gov/42629426/) | *cGAMP reporter — cGAS activation by DNA damage* | **Counter-evidence** tempering the inferred micronuclei→cGAS branch |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity.** Conclusions rest on ~a dozen patients across a few kindreds; no prevalence/incidence, penetrance, or carrier-frequency estimates are statistically robust.
2. **Lung mechanism unresolved.** The cell-intrinsic driver of lethal lung disease is not established. HSCT failure and limited immunodeficiency in some patients show the immune defect cannot fully explain the pulmonary phenotype.
3. **cGAS-STING branch is inferred, not demonstrated.** No study has shown cGAS-STING/type-I-IFN activation in LICS lung tissue, and single-cell data caution that micronuclei may not be the dominant cGAS activator [PMID: 42629426](https://pubmed.ncbi.nlm.nih.gov/42629426/).
4. **No animal model of the lung phenotype.** Existing yeast/zebrafish/cell models capture genome instability and apoptosis but not viral-triggered lung immunopathology.
5. **No modifiers mapped** despite clear variable expressivity of immunodeficiency.
6. **No therapeutics.** All attempted treatments (corticosteroids, HSCT, supportive care) have failed to alter the lethal course.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional/humanized *Nsmce3* (p.L264F) mouse** and challenge with respiratory virus to test whether lung epithelial SMC5/6 loss + viral trigger recapitulates diffuse alveolar damage/fibrosis.
2. **Directly test the cGAS-STING branch in LICS tissue:** measure cytosolic DNA, cGAMP, STING pathway activation, and type-I-IFN signatures in patient-derived lung organoids/airway epithelium and autopsy tissue; test STING/IFN inhibition for anti-fibrotic effect.
3. **Dissect cell-intrinsic lung epithelial vulnerability** using patient iPSC-derived alveolar type II cells under replication stress and viral infection.
4. **Map modifiers of immunophenotype** via deeper genomic/transcriptomic profiling across the (small) patient set and unaffected carriers.
5. **Define the antiviral-restriction contribution** of NSE3 loss to viral control in respiratory-relevant cells, linking SMC5/6's dual genome-guardian/antiviral roles to the infection trigger.
6. **Establish an international LICS registry** to improve natural-history, prognosis, penetrance, and genotype–phenotype data.

---

*Evidence source legend:* findings from [PMID: 27427983](https://pubmed.ncbi.nlm.nih.gov/27427983/) and [PMID: 33741030](https://pubmed.ncbi.nlm.nih.gov/33741030/) are **human clinical**; [PMID: 26446992](https://pubmed.ncbi.nlm.nih.gov/26446992/), [PMID: 41825673](https://pubmed.ncbi.nlm.nih.gov/41825673/), and [PMID: 22536443](https://pubmed.ncbi.nlm.nih.gov/22536443/) are **in vitro / model organism (yeast)**; [PMID: 36627765](https://pubmed.ncbi.nlm.nih.gov/36627765/) includes **zebrafish model** data; the cGAS-STING/fibrosis links ([PMID: 36876871](https://pubmed.ncbi.nlm.nih.gov/36876871/), [PMID: 42559700](https://pubmed.ncbi.nlm.nih.gov/42559700/), [PMID: 42629426](https://pubmed.ncbi.nlm.nih.gov/42629426/)) are **extrapolated from other disease contexts** and flagged as inferred.


## Artifacts

- [OpenScientist final report](Lung_Disease_Immunodeficiency_and_Chromosome_Breakage_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lung_Disease_Immunodeficiency_and_Chromosome_Breakage_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014984` (2 mentions) - the report calls it "MONDO"; MONDO calls it **lung disease, immunodeficiency, and chromosome breakage syndrome;**
- `HP:0005354` (1 mention) - the report calls it "Combined immunodeficiency"; HP calls it **obsolete Absent cellular immunity**
- `UBERON:0002048` (1 mention) - the report calls it "Primary organ:** Lung"; UBERON calls it **lung**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005354` (obsolete Absent cellular immunity) (1 mention) - replaced by `HP:0011840`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004313` (1 mention) - the report calls it "Decreased antibody level"; HP calls it **Decreased circulating immunoglobulin concentration**, and lists "Decreased antibody level in blood" among its other names
- `HP:0002788` (1 mention) - the report calls it "Recurrent respiratory infections"; HP calls it **Recurrent upper respiratory tract infections**, and lists "Recurrent upper respiratory infections" among its other names
- `GO:0000785` (1 mention) - the report calls it "Subcellular level:** Nucleus/chromatin"; GO calls it **chromatin**, and lists "nuclear chromatin" among its other names