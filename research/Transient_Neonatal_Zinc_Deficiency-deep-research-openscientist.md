---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T14:00:09.403196'
end_time: '2026-10-31T14:33:43.145191'
duration_seconds: 2013.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Transient Neonatal Zinc Deficiency
  mondo_id: MONDO:0011973
  category: Mendelian
  causal_genes: SLC30A2
  omim_id: OMIM:608118
  synonyms: not recorded
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
citation_count: 14
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 21
  relevance_assessed: 15
  on_topic: 14
  validator_version: 0.4.0
term_validation:
  total_terms: 21
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 6
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0011973
    reported_labels:
    - MONDO
    ontology_label: zinc deficiency, transient neonatal
  - term_id: HP:0012354
    reported_labels:
    - Abnormal circulating zinc concentration
    ontology_label: Increased fucosylation of N-linked protein glycosylation
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Transient_Neonatal_Zinc_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Transient_Neonatal_Zinc_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Transient Neonatal Zinc Deficiency
- **MONDO ID:** MONDO:0011973 (if available)
- **Causal gene(s):** SLC30A2
- **OMIM:** OMIM:608118
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Transient Neonatal Zinc Deficiency** covering all of the
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

# Transient Neonatal Zinc Deficiency (TNZD) — Comprehensive Disease Report

**Disease:** Transient Neonatal Zinc Deficiency
**MONDO ID:** MONDO:0011973 · **OMIM:** 608118 · **Causal gene:** **SLC30A2 (ZnT2)**
**Category:** Mendelian (autosomal dominant, maternal-acting)

---

## Summary

**Transient Neonatal Zinc Deficiency (TNZD) is caused by loss-of-function variants in the *maternal* `SLC30A2` gene, which encodes the mammary zinc transporter ZnT2.** This is the defining and most frequently misunderstood feature of the disease: the pathogenic mutation resides in the *mother*, not the affected infant. The defective ZnT2 transporter fails to load zinc into the secretory vesicles of lactating mammary epithelial cells, producing abnormally zinc-poor breast milk. An exclusively breastfed infant consuming this milk develops severe—but fully reversible—systemic zinc deficiency. The infant's own zinc-handling genes (including the acrodermatitis enteropathica gene `SLC39A4`/ZIP4) are entirely normal.

Clinically, affected infants present between roughly 2 weeks and 6 months of age with an acrodermatitis-enteropathica-like picture: periorificial and acral dermatitis, alopecia, diarrhea, irritability, and loss of appetite. The condition is biochemically marked by low infant serum zinc and low serum alkaline phosphatase (a zinc metalloenzyme), and the pathognomonic diagnostic clue is **low zinc concentration in the mother's breast milk**. Symptoms resolve rapidly and completely with oral zinc supplementation given to the infant, and the disease is permanently self-limited: it remits on weaning and the introduction of zinc-replete complementary foods—hence "transient."

Inheritance of the causative allele in the mother is **autosomal dominant**, operating through a **dominant-negative mechanism** in which mutant ZnT2 monomers homodimerize with wild-type ZnT2 and mislocalize the whole complex. Deleterious `SLC30A2` alleles are surprisingly common in the general population (at least ~1 in 2,334 newborns estimated at risk), making TNZD likely underdiagnosed rather than genuinely rare. The crucial clinical distinction is from **acrodermatitis enteropathica (AE)**: the two disorders share a nearly identical rash and symptom complex but have opposite genetics—AE is autosomal recessive from the *infant's* `SLC39A4`/ZIP4 intestinal zinc-importer defect (lifelong, requires continuous zinc therapy), whereas TNZD stems from the *mother's* `SLC30A2`/ZnT2 milk-secretion defect (self-limited, resolves at weaning).

---

## Key Findings

### Finding 1 — Maternal SLC30A2/ZnT2 loss of function is the cause of TNZD

TNZD arises from loss-of-function mutations in `SLC30A2`, the gene encoding the zinc transporter ZnT2, in the **lactating mother**. The mutation lowers the zinc content of her breast milk; the breastfed infant, receiving inadequate dietary zinc, becomes zinc-deficient. The infant's genotype is irrelevant—any infant exclusively fed zinc-poor milk from an affected mother is at risk. The first causal variant, a missense H54R substitution (a conserved histidine → arginine at amino acid 54), was identified by Chowanadisai and colleagues in 2006.

> "TNZD is a disorder caused by mutations of the ZnT2 gene, which results in low zinc breast milk in the mother, consequently causing zinc deficiency in the breast-fed infant" — [PMID: 26598882](https://pubmed.ncbi.nlm.nih.gov/26598882/)

> "Sequencing of genomic DNA detected a mis-sense mutation (Ade→Gua) that substitutes a conserved histidine at amino acid 54 with arginine (H54R) in SLC30A2 (ZnT-2)" — [PMID: 17065149](https://pubmed.ncbi.nlm.nih.gov/17065149/)

> "transient neonatal zinc deficiency (TNZD) is caused by loss-of-function mutations in the zinc transporter SLC30A2/ZnT2 gene, resulting in poor secretion of zinc into the breast milk" — [PMID: 28665435](https://pubmed.ncbi.nlm.nih.gov/28665435/)

Evidence type: **human clinical + in vitro functional**. Multiple independent case reports plus cell-based transport assays converge on the same conclusion.

### Finding 2 — Autosomal dominant inheritance via a dominant-negative homodimerization mechanism

TNZD-causing alleles are typically heterozygous (e.g., G87R, 663delC), establishing **autosomal dominant** inheritance. The mechanistic basis is dominant-negative interference: ZnT2 functions as a homodimer, and a mutant monomer dimerizes with a wild-type monomer, dragging the otherwise functional partner into aggresomal/perinuclear mislocalization and abolishing transport. Lasry and colleagues demonstrated ZnT2 homodimerization directly using bimolecular fluorescence complementation (BiFC). Gene dosage matters: a homozygous E88K mutation produces a more severe, earlier-onset phenotype than heterozygous variants, consistent with the dominant/dose-dependent model.

> "Zn(2+) deficiency caused by an autosomal dominant negative G87R mutation in the Slc30a2 gene" — [PMID: 24194756](https://pubmed.ncbi.nlm.nih.gov/24194756/)

> "We recently proposed that ZnT2 homodimerization is the underlying basis for the dominant negative effect of a novel heterozygous G87R mutation identified in women producing zinc-deficient milk" — [PMID: 24451381](https://pubmed.ncbi.nlm.nih.gov/24451381/)

> "Compared to the heterozygous condition, a homozygous mutation seems to result in a more significant decrease in zinc secretion and a more rapid onset of TNZD" — [PMID: 32278324](https://pubmed.ncbi.nlm.nih.gov/32278324/)

Evidence type: **human clinical + in vitro mechanistic**.

### Finding 3 — Deleterious ZnT2 alleles are common; TNZD is likely underdiagnosed

A systematic functional screen (Golan et al., 2019) of 115 missense `SLC30A2` variants drawn from the ExAC database (668 alleles across 60,706 individuals) found that 14 missense variants plus 2 loss-of-function variants—26 alleles in total—were markedly deleterious to zinc transport in MCF-7 cell assays. From this, the authors estimated that **at least 1 in 2,334 newborn infants is at risk of TNZD**. A separate study (Alam et al., 2015) found that 36% of lactating women tested carried non-synonymous ZnT2 variants, and that carriers had milk zinc levels distinctly above or below those of non-carriers. Together these data indicate TNZD is considerably more common than its sparse literature suggests.

> "26 SLC30A2/ZnT2 alleles harboured deleterious mutations, suggesting that at least 1 in 2334 newborn infants are at risk to develop TNZD" — [PMID: 30450693](https://pubmed.ncbi.nlm.nih.gov/30450693/)

> "We found that 36% of women tested carried non-synonymous ZnT2 variants, all of whom had milk Zn levels that were distinctly above or below those in women without variants" — [PMID: 26293594](https://pubmed.ncbi.nlm.nih.gov/26293594/)

Evidence type: **population genetics + in vitro functional**.

### Finding 4 — Clinical presentation and transient, self-limited course

TNZD presents in exclusively breastfed neonates and young infants, typically between ~2 weeks and 6 months of age. Cardinal features are an AE-like dermatitis (periorificial and acral), alopecia, diarrhea, irritability, and loss of appetite. The disease responds rapidly and completely to oral zinc supplementation of the infant, and it is permanently self-limited—remitting on weaning and introduction of complementary zinc-containing foods. A key diagnostic observation is that maternal dietary zinc supplementation does **not** correct the low milk zinc, which points to an inherited transporter defect rather than maternal dietary deficiency.

> "The main initial symptoms of zinc deficiency are dermatitis, diarrhea, alopecia, and loss of appetite. Importantly, zinc supplementation of these zinc-deficient infants effectively and rapidly resolves these TNZD symptoms" — [PMID: 28665435](https://pubmed.ncbi.nlm.nih.gov/28665435/)

> "TNZD becomes clinically evident during breastfeeding and is resolved by weaning and the introduction of complementary nutrition" — [PMID: 24456035](https://pubmed.ncbi.nlm.nih.gov/24456035/)

> "This condition is not corrected by maternal zinc supplementation, supporting the speculation that it results from an inherited genetic condition" — [PMID: 17065149](https://pubmed.ncbi.nlm.nih.gov/17065149/)

Evidence type: **human clinical**.

### Finding 5 — ZnT2 loads zinc into secretory organelles; its loss also broadly disrupts mammary secretory cells

ZnT2 imports zinc into vesicles and mitochondria of specialized secretory cells—breast, pancreas, and prostate. In the lactating mammary gland, this vesicular loading is the route by which zinc enters milk. Beyond simply lowering milk zinc, ZnT2 dysfunction has cell-autonomous consequences for mammary epithelial cells: the T288S variant induces endoplasmic-reticulum stress, oxidative stress, and epithelial barrier defects (Lee et al., 2018), and alters lysosome function and cellular energetics, associating with low milk *volume* (Rivera et al., 2020). ZnT2-null mice show profound defects in mammary epithelial cell polarity and vesicle secretion (Alam et al., 2015). Thus some ZnT2 variants may compromise both milk zinc *content* and overall lactation performance.

> "The zinc (Zn) transporter ZnT2 (SLC30A2) is expressed in specialized secretory cells including breast, pancreas and prostate, and imports Zn into mitochondria and vesicles" — [PMID: 26293594](https://pubmed.ncbi.nlm.nih.gov/26293594/)

> "A genetic variant in SLC30A2 causes breast dysfunction during lactation by inducing ER stress, oxidative stress and epithelial barrier defects" — [PMID: 29476070](https://pubmed.ncbi.nlm.nih.gov/29476070/)

> "A common genetic variant in zinc transporter ZnT2 (Thr288Ser) is present in women with low milk volume and alters lysosome function and cell energetics" — [PMID: 32320289](https://pubmed.ncbi.nlm.nih.gov/32320289/)

Evidence type: **in vitro + model organism**.

### Finding 6 — Hormonal regulation of ZnT2 and experimental model systems

ZnT2 expression in the mammary gland is driven by prolactin, acting transcriptionally through the JAK2/STAT5 pathway on GAS elements in the `SLC30A2` promoter (Qian et al., 2009; HC11 mammary cells). This explains why ZnT2 is upregulated during lactation. The principal experimental systems used to study TNZD are: (1) ZnT2-null (knockout) mice, which produce low-zinc milk and show impaired mammary epithelial cell polarity and secretion; (2) cell-based transport and localization assays in MCF-7 human breast cells, HC11 mouse mammary cells, and HEK-293 cells, used to functionally classify variants; and (3) the related ZnT4 "lethal milk" (lm/lm) mouse, which provides comparative insight into mammary zinc-transport failure.

> "prolactin increased ZnT2 abundance transcriptionally in cultured mammary epithelial (HC11) cells" — [PMID: 19494234](https://pubmed.ncbi.nlm.nih.gov/19494234/)

> "Gene knockdown of SLC30A2 in mammary epithelial cells reduced zinc secretion, illustrating the role of ZnT-2 in zinc secretion from this cell type" — [PMID: 17065149](https://pubmed.ncbi.nlm.nih.gov/17065149/)

> "ZnT4 (SLC30A4)-null ('lethal milk') mice have defects in mammary gland secretion and hallmarks of precocious involution during lactation" — [PMID: 26538236](https://pubmed.ncbi.nlm.nih.gov/26538236/)

Evidence type: **in vitro + model organism**.

### Finding 7 — Diagnostic framework

TNZD diagnosis combines general zinc-deficiency biochemical criteria with disease-specific findings. The Japanese Society of Clinical Nutrition criteria (2018) require: (a) symptom(s) and/or low serum alkaline phosphatase, (b) exclusion of other diseases, (c) low serum zinc, and (d) symptom alleviation upon zinc administration. Serum zinc <60 μg/dL indicates deficiency; 60–80 μg/dL is marginal. Alkaline phosphatase is itself a zinc metalloenzyme, so a low ALP supports the diagnosis. The **TNZD-specific** pathognomonic finding is **low maternal breast-milk zinc** in a symptomatic exclusively breastfed infant. The diagnosis is confirmed by identifying a causal variant on **maternal `SLC30A2` sequencing**, while normal infant `SLC39A4` sequencing excludes AE.

> "low serum alkaline phosphatase, (b) ruling out other diseases, (c) low serum zinc, and (d) alleviation of symptoms upon zinc administration. Serum zinc <60 μg/dL and 60-80 μg/dL indicate zinc deficiency and marginal deficiency, respectively" — [PMID: 32331308](https://pubmed.ncbi.nlm.nih.gov/32331308/)

> "Detection of the mother's breast milk showed a significantly lower zinc level. Thus, SLC30A2 sequencing was performed on her genomic DNA" — [PMID: 32278324](https://pubmed.ncbi.nlm.nih.gov/32278324/)

Evidence type: **human clinical / clinical guideline**.

### Finding 8 — TNZD versus acrodermatitis enteropathica: same picture, opposite genetics

The single most important diagnostic distinction is between TNZD and acrodermatitis enteropathica (AE). Both present with periorificial/acral dermatitis, alopecia, and diarrhea. But AE is autosomal **recessive**, caused by mutations in the **infant's** intestinal zinc importer `SLC39A4`/ZIP4, producing defective zinc absorption—a lifelong condition requiring continuous zinc therapy. TNZD arises from the **mother's** `SLC30A2`/ZnT2 defect lowering milk zinc, with the infant's own zinc handling entirely normal—a self-limited condition that resolves at weaning. Normal infant `SLC39A4` sequencing is used to exclude AE and support a TNZD diagnosis.

> "AE is an autosomal recessive disorder caused by mutations of the ZIP4 gene, consequently resulting in defective absorption of zinc in the small intestine. In contrast, TNZD is a disorder caused by mutations of the ZnT2 gene" — [PMID: 26598882](https://pubmed.ncbi.nlm.nih.gov/26598882/)

> "Sanger sequencing of the AE-causing gene SLC39A4 revealed no mutations in genomic DNA from the infant, excluding the possibility of AE" — [PMID: 32278324](https://pubmed.ncbi.nlm.nih.gov/32278324/)

Evidence type: **human clinical**.

---

## Detailed Section-by-Section Report

### 1. Disease Information

TNZD is a Mendelian disorder of lactation in which an exclusively breastfed infant develops acquired, systemic zinc deficiency because the mother's breast milk is abnormally low in zinc. It is unusual among genetic diseases in that the pathogenic genotype resides in the mother while the clinical phenotype manifests in the (genetically normal) infant.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0011973 |
| OMIM | 608118 |
| Causal gene | `SLC30A2` (ZnT2), HGNC:11013 |
| MeSH / concept | Zinc deficiency (neonatal, transient) |

**Synonyms / alternative names:** Transient neonatal zinc deficiency; TNZD; transient symptomatic (neonatal) zinc deficiency; (historically described under broad "zinc deficiency of breastfed infants"). AE-like phenotype but a distinct entity.

**Information source:** Derived predominantly from aggregated, disease-level sources (OMIM, review articles) and from individual patient case reports/case series (EHR-type clinical descriptions) plus in vitro and model-organism functional studies.

### 2. Etiology

**Primary cause (genetic):** Maternal heterozygous (occasionally homozygous) loss-of-function variants in `SLC30A2`/ZnT2 that impair zinc transport into milk. **This is the sole established cause.**

**Genetic risk factors:** Deleterious `SLC30A2` alleles are the causal risk factor. These alleles are relatively common (≥1 in 2,334 infants at risk; 36% of lactating women carry non-synonymous variants). Reported variants include H54R, G87R, E88K (homozygous), T288S (associated with low milk volume), a 663delC frameshift, and splice-affecting variants.

**Environmental/host risk factors:** Exclusive breastfeeding from an affected mother is the necessary exposure. Prematurity and the normally rapid depletion of fetal/neonatal zinc stores increase an infant's vulnerability to low intake. Notably, maternal dietary zinc is **not** a cause—maternal supplementation does not correct the milk zinc defect (PMID: 17065149).

**Protective factors:** Formula feeding or introduction of zinc-containing complementary foods is protective (and curative). Weaning permanently resolves the condition. No specific genetic protective alleles are documented.

**Gene–environment interaction:** The disease requires both the maternal genotype (defective ZnT2) and the environmental exposure (the infant being fed that mother's milk). An affected mother's formula-fed infant would not develop TNZD; the same infant breastfed would.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset / course / frequency |
|---|---|---|---|
| Periorificial / acral dermatitis | Clinical sign (skin) | HP:0000964 (Eczema) / AE-like dermatitis | Neonatal–infancy; common; resolves with zinc |
| Alopecia | Physical manifestation | HP:0001596 (Alopecia) | Infancy; common; reversible |
| Diarrhea | Symptom (GI) | HP:0002014 (Diarrhea) | Infancy; common; reversible |
| Loss of appetite / poor feeding | Symptom | HP:0004396 (Poor appetite) | Infancy; common |
| Irritability | Behavioral | HP:0000737 (Irritability) | Infancy; common |
| Low serum zinc | Laboratory abnormality | HP:0012354 (Abnormal circulating zinc concentration) | Diagnostic; <60 μg/dL |
| Low serum alkaline phosphatase | Laboratory abnormality | HP:0003282 (Reduced alkaline phosphatase) | Supports diagnosis |
| Failure to thrive / impaired growth | Clinical sign | HP:0001508 (Failure to thrive) | Variable |

**Severity/progression:** Severe during active deficiency but **fully reversible**; episodic in the sense that it is confined to the breastfeeding window. **Quality of life:** Significant short-term morbidity (irritability, feeding difficulty, dermatitis) during the deficiency period, but no long-term QoL impact once treated—outcome is excellent.

### 4. Genetic / Molecular Information

**Causal gene:** `SLC30A2` / ZnT2 (solute carrier family 30 member 2; HGNC:11013; chromosome 1p35.3; OMIM gene 609617). ZnT2 is a cation diffusion facilitator (CDF) family zinc efflux transporter that moves Zn²⁺ from cytosol into vesicles/organelles.

**Pathogenic variants:** Reported TNZD variants include missense (H54R, G87R, E88K, T288S), a frameshift (663delC), and a splice-efficiency-reducing variant. Variant types span missense, frameshift, and splice-site. Most behave as **loss of function** at the transport level; heterozygous alleles additionally exert a **dominant-negative** effect via homodimerization with wild-type ZnT2. Golan 2019 also described some gain-of-function variants in the broader functional screen.

**Classification/frequency:** Many variants are functionally validated as deleterious (consistent with pathogenic/likely pathogenic), though formal ACMG classifications vary. Allele frequencies derive from ExAC/gnomAD; the aggregate deleterious-allele burden yields the ~1/2,334 at-risk estimate. Origin is **germline** (maternal).

**Modifier genes / epigenetics / chromosomal abnormalities:** No established modifier genes, disease-specific epigenetic marks, or chromosomal abnormalities. Gene dosage (homozygous vs heterozygous) modifies severity.

### 5. Environmental Information

The only relevant "environmental" factor is the nutritional exposure of exclusive breastfeeding on zinc-poor milk. No toxins, radiation, occupational exposures, or infectious agents are implicated. Maternal diet does not drive the milk zinc defect. Not applicable: infectious agents, pollution.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A loss-of-function variant in the mother's `SLC30A2` gene **leads to** production of defective ZnT2 protein.
2. In heterozygotes, mutant ZnT2 **homodimerizes with** wild-type ZnT2 (demonstrated by BiFC), **resulting in** aggresomal/perinuclear mislocalization of the dimer — a dominant-negative effect.
3. Loss of functional ZnT2 at the vesicular/secretory membrane **results in** failure to load Zn²⁺ into the secretory vesicles of lactating mammary epithelial cells (ZnT2 is normally induced here by prolactin via JAK2/STAT5).
4. Impaired vesicular zinc loading **leads to** abnormally low zinc secretion into breast milk (low milk zinc). *(Branch: some variants, e.g., T288S, additionally induce ER stress, oxidative stress, and barrier/lysosomal dysfunction, which may also reduce milk volume — cell-autonomous mammary dysfunction.)*
5. An exclusively breastfed infant consuming the zinc-poor milk **develops** inadequate dietary zinc intake **leading to** systemic zinc deficiency.
6. Systemic zinc deficiency **impairs** zinc-dependent enzymes and processes (e.g., alkaline phosphatase activity, epidermal and gut epithelial turnover) **resulting in** the clinical phenotype: dermatitis, alopecia, diarrhea, poor appetite, irritability.
7. Supplying zinc to the infant (or weaning onto zinc-replete foods) **restores** zinc status **and resolves** all symptoms — the "transient" resolution.

**Molecular pathways / cellular processes:** ZnT2-mediated transmembrane zinc transport (GO:0006882 cellular zinc ion homeostasis; GO:0071577 zinc ion transmembrane transport); prolactin–JAK2–STAT5 signaling driving ZnT2 transcription. Downstream: ER stress/unfolded protein response, oxidative stress, and altered lysosome/energetics in affected mammary cells (for certain variants).

**Protein dysfunction:** Loss of transport function; dominant-negative mislocalization/aggregation of the ZnT2 homodimer; protein instability in cells.

**Metabolic/biochemical abnormalities:** Reduced activity of zinc metalloenzymes (notably alkaline phosphatase) in the deficient infant.

**Upstream vs downstream:** Upstream = maternal `SLC30A2` mutation and impaired mammary vesicular zinc loading. Downstream = low milk zinc → infant systemic deficiency → enzyme/epithelial dysfunction → clinical signs.

**Cell types (CL) and tissues (UBERON):** Lactating mammary (luminal) epithelial cell (CL:0002326 luminal epithelial cell of mammary gland); mammary gland (UBERON:0001911); in the infant: epidermis/skin (UBERON:0002097), intestinal epithelium (UBERON:0001277). **Subcellular (GO CC):** secretory vesicle (GO:0099503), mitochondrion (GO:0005739), lysosome (GO:0005764), endoplasmic reticulum (GO:0005783). **CHEBI:** zinc(2+) (CHEBI:29105).

### 7. Anatomical Structures Affected

- **Maternal (source of defect):** mammary gland (UBERON:0001911), specifically secretory/luminal mammary epithelial cells; subcellular secretory vesicles and mitochondria.
- **Infant (site of disease):** skin/epidermis (periorificial and acral), especially perioral and perineal/acral regions; scalp hair follicles (alopecia); gastrointestinal tract/intestinal epithelium (diarrhea). Body systems: integumentary, digestive; systemic metabolic. Lateralization: typically bilateral/symmetric dermatitis.

### 8. Temporal Development

- **Onset:** Neonatal to early infancy, typically ~2 weeks to 6 months; homozygous maternal variants give more rapid onset. Pattern: subacute, during exclusive breastfeeding.
- **Progression:** Progressive while exclusively breastfed on zinc-poor milk; not chronic.
- **Course / duration:** Self-limited, confined to the breastfeeding period.
- **Remission:** Treatment-induced (zinc supplementation) and spontaneous at weaning. **Critical period / window of opportunity:** the exclusive-breastfeeding interval — prompt zinc supplementation or weaning is both diagnostic and curative.

### 9. Inheritance and Population

- **Epidemiology:** True prevalence/incidence unknown and historically considered rare, but functional-genetics data imply substantial underdiagnosis: ≥1 in 2,334 newborns estimated at risk; 36% of lactating women carry non-synonymous ZnT2 variants.
- **Inheritance:** Autosomal dominant (maternal-acting), via dominant-negative mechanism; homozygous cases more severe (dosage effect).
- **Penetrance/expressivity:** Variable — depends on the specific variant's residual transport, maternal milk zinc level, and infant feeding pattern.
- **Founder effects / consanguinity:** Not specifically established; homozygous cases (e.g., E88K) may reflect consanguinity in individual families. Variants reported across Japanese, European, and other populations.
- **Sex ratio:** Affected infants — no strong sex predilection reported. The genetic defect manifests clinically only in lactating (female) mutation carriers.

### 10. Diagnostics

- **Laboratory:** Low infant serum zinc (<60 μg/dL deficient; 60–80 marginal); low serum alkaline phosphatase (zinc metalloenzyme). **Low maternal breast-milk zinc is the key disease-specific test.**
- **Genetic testing:** Maternal `SLC30A2` single-gene sequencing confirms the diagnosis; infant `SLC39A4` sequencing (normal) excludes AE. WES/WGS or zinc-transporter gene panels are alternatives.
- **Clinical criteria:** General zinc-deficiency criteria (symptoms and/or low ALP; exclusion of other disease; low serum zinc; response to zinc) plus the TNZD-specific low milk zinc and maternal genotype.
- **Differential diagnosis:** Acrodermatitis enteropathica (infant `SLC39A4`/ZIP4 — recessive, lifelong), dietary zinc deficiency, biotin deficiency, essential fatty acid deficiency, cystic fibrosis–related malnutrition, and other causes of infantile periorificial dermatitis.
- **Screening:** No routine population or newborn screening exists; cascade/maternal testing is relevant where a proband is identified.

### 11. Outcome / Prognosis

Prognosis is **excellent**. With timely zinc supplementation symptoms resolve rapidly and completely; the disease is self-limited and permanently resolves at weaning. There is no established disease-specific mortality, long-term disability, or chronic morbidity when treated. Untreated severe zinc deficiency could, in principle, impair growth and immune function, underscoring the value of prompt recognition. Prognostic factors: speed of recognition and treatment.

### 12. Treatment

- **Primary therapy:** Oral **zinc supplementation of the infant** (e.g., zinc sulfate / zinc gluconate / zinc acetate) — rapidly and effectively resolves symptoms (PMID: 28665435). NCIT: Zinc Supplement / Zinc Sulfate.
- **Definitive resolution:** Weaning and introduction of zinc-replete complementary foods; or switching to zinc-fortified formula.
- **What does NOT work:** Maternal zinc supplementation does not correct the milk zinc defect (PMID: 17065149).
- **Supportive care:** Topical skin care for dermatitis during recovery.
- **Advanced/gene/cell/RNA therapies:** Not applicable and unnecessary given the benign, self-limited course.
- **Pharmacogenomics / personalized:** Diagnosis is genotype-guided (maternal `SLC30A2`), but treatment is uniform (zinc).

### 13. Prevention

- **Secondary prevention (most relevant):** Early recognition in a symptomatic breastfed infant; prompt zinc supplementation and/or weaning prevents complications.
- **Genetic counseling:** For a mother identified with a pathogenic `SLC30A2` variant, counseling regarding risk to future breastfed infants and the option of zinc supplementation or formula feeding is appropriate (autosomal dominant, maternal-acting).
- **No immunization, public-health, or environmental interventions** apply (non-infectious, non-environmental disease). No established primary prevention beyond awareness and, in at-risk dyads, prophylactic infant zinc supplementation.

### 14. Other Species / Natural Disease

- **Model-relevant orthologs:** Mouse `Slc30a2` (ZnT2); the ZnT4 "lethal milk" (`Slc30a4`, lm/lm) mouse is a naturally occurring murine model of mammary zinc-transport failure causing lethal zinc deficiency in suckling pups — a comparative natural-disease analog (PMID: 26538236).
- **Taxonomy:** *Mus musculus* (NCBI:txid10090) carries the relevant orthologs.
- No significant companion-animal or zoonotic relevance; this is a human lactation genetic disorder with rodent experimental analogs.

### 15. Model Organisms

| Model | Type | Use / phenotype recapitulation |
|---|---|---|
| ZnT2-null (Slc30a2 KO) mouse | Mammalian knockout | Low milk zinc; impaired mammary epithelial cell polarity and vesicle secretion — recapitulates the milk-zinc-secretion defect |
| ZnT4 "lethal milk" (lm/lm) mouse | Natural mutant | Mammary secretion defects, precocious involution; comparative model of mammary zinc transport failure |
| MCF-7 (human breast) | Cell line | Variant functional transport classification (Golan 2019) |
| HC11 (mouse mammary) | Cell line | Prolactin-induced ZnT2 expression; transport assays |
| HEK-293 | Cell line | Variant localization/transport assays |

**Limitations:** Cell lines capture transport function but not full lactation physiology; mouse models capture mammary secretion but differ from human milk composition and feeding dynamics.

---

## Mechanistic Model / Interpretation

```
          MOTHER (genotype-bearing)                    INFANT (phenotype-bearing)
  +----------------------------------------+    +------------------------------------+
  | SLC30A2 / ZnT2 loss-of-function variant |    |  Exclusively breastfed             |
  |            (H54R, G87R, E88K ...)        |    |  Own SLC39A4/ZIP4 = NORMAL          |
  +-------------------+--------------------+     +------------------+-----------------+
                      | heterozygous -> dominant-negative             |
                      v  (mutant.WT homodimer mislocalizes)           |
     Prolactin -> JAK2/STAT5 -> ZnT2 up (normally)                    |
                      |                                               |
                      v                                               |
   Failure to load Zn2+ into mammary secretory vesicles              |
                      |   (+/- ER/oxidative stress, low milk volume)  |
                      v                                               |
            LOW ZINC BREAST MILK  --------------------------------->  |  ingests low-Zn milk
                                                                      v
                                                      Infant SYSTEMIC ZINC DEFICIENCY
                                                                      |
                                                                      v
                       low Zn-metalloenzymes (ALP), epidermal/gut turnover
                                                                      |
                                                                      v
                   Dermatitis . alopecia . diarrhea . poor appetite . irritability
                                                                      |
                            oral zinc OR weaning  ------------------>  FULL, RAPID RESOLUTION
```

The model's central logic is a **genotype–phenotype dissociation across two individuals**: the mutation is maternal and the disease is in the infant. This is why TNZD is both easy to miss and easy to cure—and why distinguishing it from AE (where mutation and disease coincide in the infant) is clinically decisive.

| Feature | TNZD | Acrodermatitis Enteropathica (AE) |
|---|---|---|
| Causal gene | `SLC30A2`/ZnT2 (mother) | `SLC39A4`/ZIP4 (infant) |
| Defect | Zinc **secretion** into milk | Zinc **absorption** in gut |
| Inheritance | Autosomal dominant (dominant-negative) | Autosomal recessive |
| Who carries mutation | Mother | Infant |
| Course | Self-limited; resolves at weaning | Lifelong |
| Treatment | Infant zinc until weaning | Continuous lifelong zinc |
| Rash/alopecia/diarrhea | Yes | Yes (clinically indistinguishable) |

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [17065149](https://pubmed.ncbi.nlm.nih.gov/17065149/) | Landmark: first SLC30A2 mutation (H54R); maternal supplementation fails; cell knockdown reduces secretion |
| [26598882](https://pubmed.ncbi.nlm.nih.gov/26598882/) | Review: TNZD caused by ZnT2 mutation → low milk zinc; TNZD vs AE contrast |
| [28665435](https://pubmed.ncbi.nlm.nih.gov/28665435/) | Review: LoF ZnT2 impairs milk zinc secretion; cardinal symptoms; rapid zinc response |
| [24194756](https://pubmed.ncbi.nlm.nih.gov/24194756/) | Autosomal dominant-negative G87R mutation |
| [24451381](https://pubmed.ncbi.nlm.nih.gov/24451381/) | ZnT2 homodimerization as basis of dominant-negative effect (BiFC) |
| [32278324](https://pubmed.ncbi.nlm.nih.gov/32278324/) | Homozygous E88K: more severe/earlier; diagnostic pathway; AE excluded via SLC39A4 |
| [30450693](https://pubmed.ncbi.nlm.nih.gov/30450693/) | Population risk: ≥1 in 2,334 newborns at risk (ExAC functional screen) |
| [26293594](https://pubmed.ncbi.nlm.nih.gov/26293594/) | 36% of women carry non-synonymous ZnT2 variants; ZnT2 secretory-cell biology |
| [24456035](https://pubmed.ncbi.nlm.nih.gov/24456035/) | Transient, self-limited course resolving at weaning |
| [29476070](https://pubmed.ncbi.nlm.nih.gov/29476070/) | T288S variant → ER/oxidative stress, barrier defects (mammary dysfunction) |
| [32320289](https://pubmed.ncbi.nlm.nih.gov/32320289/) | T288S → low milk volume via lysosome/energetics |
| [19494234](https://pubmed.ncbi.nlm.nih.gov/19494234/) | Prolactin → JAK2/STAT5 drives ZnT2 expression |
| [26538236](https://pubmed.ncbi.nlm.nih.gov/26538236/) | ZnT4 "lethal milk" mouse comparative model |
| [32331308](https://pubmed.ncbi.nlm.nih.gov/32331308/) | Zinc-deficiency diagnostic criteria (serum zinc/ALP cutoffs) |
| [27304099](https://pubmed.ncbi.nlm.nih.gov/27304099/) | Novel heterozygous SLC30A2 mutations in Japanese mothers; many variants pathogenic |

Evidence source mix: **human clinical** (case reports/series, reviews), **in vitro functional** (MCF-7/HC11/HEK-293 transport assays, BiFC), **model organism** (ZnT2-null and ZnT4 lethal-milk mice), and **population genetics** (ExAC/gnomAD functional screens).

---

## Limitations and Knowledge Gaps

1. **No formal prevalence/incidence.** Risk estimates (~1/2,334) are derived from functional assays of population variants, not from diagnosed-case registries; the true clinical incidence is unknown and likely underascertained.
2. **Variant-level ACMG classification is incomplete.** Many variants are functionally validated as deleterious but not uniformly classified in ClinVar; the boundary between benign polymorphism and milk-zinc-lowering allele is not fully mapped.
3. **Genotype–milk-zinc correlation is imperfect.** Factors determining whether a given carrier produces symptomatically low-zinc milk (residual transport, modifiers, lactation stage) are not fully defined.
4. **Long-term infant outcomes.** Although outcomes are considered excellent after treatment, systematic long-term neurodevelopmental/growth follow-up of affected infants is sparse.
5. **Human mechanistic data on the ER/oxidative-stress branch** come from specific variants (T288S) in cell models; the in-vivo contribution of mammary cell dysfunction (vs pure transport loss) to each case is not established.
6. **No HPO/ontology-coded natural-history dataset** specific to TNZD; phenotype frequencies here are qualitative.

---

## Proposed Follow-up Experiments / Actions

1. **Registry and prospective screening:** Establish a TNZD registry; pilot maternal milk-zinc screening in symptomatic breastfed infants with periorificial dermatitis to measure true incidence and validate the ~1/2,334 estimate.
2. **Variant functional atlas:** Systematically assay all gnomAD `SLC30A2` missense variants for transport and dominant-negative behavior (MCF-7/HC11 + BiFC), feeding results into ClinVar/ClinGen for ACMG reclassification.
3. **Genotype-to-milk-zinc modeling:** Correlate maternal genotype with measured milk zinc and infant serum zinc across a cohort to build a predictive model of clinical penetrance.
4. **Mechanistic dissection of the mammary-dysfunction branch:** Determine, across diverse variants, the relative contribution of transport loss vs ER/oxidative-stress-driven secretory dysfunction and low milk volume to the clinical phenotype.
5. **Clinical guidance:** Draft a diagnostic algorithm (infant serum zinc + ALP → maternal milk zinc → maternal `SLC30A2` + infant `SLC39A4` sequencing) and genetic-counseling guidance for carrier mothers planning future breastfeeding.
6. **Long-term follow-up study:** Prospective neurodevelopmental and growth follow-up of treated TNZD infants to confirm the excellent-prognosis assumption.

---

*Report compiled from 8 confirmed findings and 17 reviewed papers over 5 investigation iterations. The causal gene is maternal **SLC30A2 (ZnT2)**; the disease is MONDO:0011973 / OMIM 608118.*


## Artifacts

- [OpenScientist final report](Transient_Neonatal_Zinc_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Transient_Neonatal_Zinc_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 9 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011973` (3 mentions) - the report calls it "MONDO"; MONDO calls it **zinc deficiency, transient neonatal**
- `HP:0012354` (1 mention) - the report calls it "Abnormal circulating zinc concentration"; HP calls it **Increased fucosylation of N-linked protein glycosylation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003282` (1 mention) - the report calls it "Reduced alkaline phosphatase"; HP calls it **Decreased circulating alkaline phosphatase activity**, and lists "Low alkaline phosphatase" among its other names