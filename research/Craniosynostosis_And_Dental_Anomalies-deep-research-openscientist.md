---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T23:54:24.382651'
end_time: '2026-11-05T00:42:43.573590'
duration_seconds: 2899.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Craniosynostosis and Dental Anomalies
  mondo_id: MONDO:0013615
  category: Mendelian
  causal_genes: IL11RA
  omim_id: OMIM:614188
  synonyms: Kreiborg-Pakistani syndrome
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
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 9
  validator_version: 0.5.1
term_validation:
  total_terms: 29
  verified: 25
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000055
    reported_labels:
    - suture mesenchyme / cranial neural-crest-derived osteoprogenitors
    ontology_label: obsolete non-terminally differentiated cell
  labels_variant: 6
  obsolete_terms:
  - term_id: CL:0000055
    ontology_label: obsolete non-terminally differentiated cell
  unresolvable_prefixes:
  - OMIM
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Craniosynostosis_And_Dental_Anomalies-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Craniosynostosis_And_Dental_Anomalies-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniosynostosis and Dental Anomalies
- **MONDO ID:** MONDO:0013615 (if available)
- **Causal gene(s):** IL11RA
- **OMIM:** OMIM:614188
- **Synonyms:** Kreiborg-Pakistani syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Craniosynostosis and Dental Anomalies** covering all of the
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

# Craniosynostosis and Dental Anomalies (CRSDA / Kreiborg-Pakistani Syndrome): A Comprehensive Disease Characterization

**Disease:** Craniosynostosis and Dental Anomalies (CRSDA)
**MONDO ID:** MONDO:0013615 · **OMIM:** 614188 · **Causal gene:** **IL11RA** (interleukin 11 receptor subunit alpha, 9p13.3)
**Synonyms:** Kreiborg-Pakistani syndrome; IL11RA-related Crouzon-like autosomal recessive craniosynostosis
**Category:** Mendelian (autosomal recessive)

---

## Summary

Craniosynostosis and dental anomalies (CRSDA), also known as Kreiborg–Pakistani syndrome, is a rare **autosomal recessive** craniofacial disorder caused by **biallelic loss-of-function variants in IL11RA**, the gene encoding the alpha subunit of the interleukin-11 receptor, located on chromosome **9p13.3**. Despite the "Crouzon-like" clinical overlap with the dominant FGFR-driven craniosynostoses, CRSDA is mechanistically distinct: it is a disorder of **cytokine receptor signaling**, not fibroblast growth factor signaling. The causal gene named in this report — and the gene that must anchor any knowledge-base entry — is **IL11RA**, not an FGFR.

The core phenotype comprises **multisuture craniosynostosis**, **Crouzon-like midface hypoplasia** (with variable exophthalmos, relative prognathism, and a beaked nose), **delayed/failed tooth eruption with supernumerary teeth**, and **conductive hearing loss** from middle-ear anomalies. A subset of patients additionally shows a connective-tissue disorder with joint hypermobility and intervertebral disc fragility. Mechanistically, IL11RA loss of function abolishes IL-11 signaling through the shared **gp130 (IL6ST)/JAK-STAT3** pathway. Because IL-11 signaling normally *restricts* cranial suture fusion and tooth number, its loss releases that restraint, producing premature suture fusion and dental excess. This causal chain is strongly supported by human genetics, in-vitro STAT3 phosphorylation assays, structural modeling of ligand/co-receptor binding, and `Il11ra`-null mouse models that recapitulate the cranial and skeletal phenotype (with incomplete penetrance of craniosynostosis).

The disorder is **ultra-rare** (~40–50 patients reported as of recent literature), enriched in **consanguineous Turkish and Pakistani families**, with recurrent variants and low-frequency carrier alleles detectable in gnomAD. There is **no disease-specific pharmacotherapy or gene therapy**; management is **multidisciplinary and primarily surgical/supportive** (cranial vault remodeling, fronto-orbital advancement, distraction osteogenesis, plus ENT and orthodontic care). Prognosis for survival is generally favorable — patients survive to adulthood — with morbidity driven chiefly by **recurrent multifactorial intracranial hypertension**, craniofacial deformity, hearing loss, and dental complications. Prevention is limited to **genetic counseling, carrier/cascade testing, and prenatal/preimplantation diagnosis**; no primary (environmental) prevention exists because the etiology is purely monogenic.

---

## Key Findings

### 1. CRSDA is an autosomal recessive syndrome caused by biallelic loss-of-function IL11RA variants (F001)

Homozygosity mapping in **three consanguineous Pakistani families** localized the syndrome to chromosome 9, and all affected children carried homozygous **IL11RA** missense mutations — `c.662C>G` (p.Pro221Arg), `c.734C>G` (p.Ser245Cys), and `c.886C>T` (p.Arg296Trp). Two North European families additionally carried a nonsense variant `c.475C>T` (p.Gln159X) and an in-frame duplication `c.916_924dup` (p.Thr306_Ser308dup) ([PMID: 21741611](https://pubmed.ncbi.nlm.nih.gov/21741611/)). The original report states that *"all affected children harbored homozygous missense mutations (c.662C>G [p.Pro221Arg], c.734C>G [p.Ser245Cys], or c.886C>T [p.Arg296Trp]) in IL11RA (encoding interleukin 11 receptor, alpha) on chromosome 9p13.3."*

A second landmark study confirmed the gene in additional families, identifying a splice mutation `c.479+6T>G` *"in the interleukin 11 receptor alpha gene (IL11RA) on chromosome 9p21"* and further missense/nonsense variants, all of which *"dramatically reduced IL11-mediated STAT3 phosphorylation"* ([PMID: 24498618](https://pubmed.ncbi.nlm.nih.gov/24498618/)).

**Ontology mapping:** Gene **HGNC:5967 (IL11RA)**; disease **MONDO:0013615 / OMIM:614188**.

### 2. Core phenotype: multisuture craniosynostosis, Crouzon-like midface hypoplasia, dental anomalies, and conductive hearing loss (F002)

The syndrome *"featuring craniosynostosis, maxillary hypoplasia, delayed tooth eruption, and supernumerary teeth"* ([PMID: 21741611](https://pubmed.ncbi.nlm.nih.gov/21741611/)) presents with a characteristic craniofacial gestalt described as *"multiple suture synostosis, midface hypoplasia, variable degree of exophthalmos, relative prognathism, a beaked nose, and conductive hearing loss"* ([PMID: 24498618](https://pubmed.ncbi.nlm.nih.gov/24498618/)). Middle-ear anomalies underlie the conductive hearing loss ([PMID: 30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/)). Importantly, *"a subset of patients had an associated connective tissue disorder with joint hypermobility and intervertebral discs fragility"* ([PMID: 29926465](https://pubmed.ncbi.nlm.nih.gov/29926465/)).

**Suggested HPO terms:**

| Phenotype | HPO term | Onset | Frequency |
|---|---|---|---|
| Craniosynostosis (multisuture) | HP:0001363 | Congenital | Core/near-universal |
| Midface/maxillary hypoplasia | HP:0011800 / HP:0000327 | Congenital–childhood | Frequent |
| Delayed tooth eruption | HP:0000684 | Childhood | Frequent |
| Supernumerary teeth | HP:0011069 | Childhood | Frequent |
| Conductive hearing impairment | HP:0000405 | Childhood | Frequent |
| Proptosis / exophthalmos | HP:0000520 | Childhood | Variable |
| Relative prognathism | HP:0000303 | Childhood | Variable |
| Joint hypermobility | HP:0001382 | Variable | Subset |

### 3. Mechanism: IL11RA LOF abrogates IL11→gp130→JAK/STAT3 signaling, releasing restraint on suture fusion and tooth number (F003)

Functional assays demonstrated that *"the p.Arg296Trp mutation rendered the receptor unable to mediate the IL11 signal, indicating that the mutation causes loss of IL11RA function"* ([PMID: 21741611](https://pubmed.ncbi.nlm.nih.gov/21741611/)). The same study concluded that *"IL11 signaling is essential for the normal development of craniofacial bones and teeth and that its function is to restrict suture fusion and tooth number."* Across all tested variants, investigators *"demonstrated dramatically reduced IL11-mediated STAT3 phosphorylation for all mutations"* ([PMID: 24498618](https://pubmed.ncbi.nlm.nih.gov/24498618/)).

Structural modeling of newer variants (p.Pro116Leu, p.Glu126Gly, p.Gly231Val, p.Leu236Pro) showed they disrupt hydrogen-bond networks, *"significantly reducing ligand-binding affinity to both interleukin-11 (IL-11) and gp130,"* alongside truncating variants p.Pro218Argfs*140 and p.Trp132Ter ([PMID: 40353334](https://pubmed.ncbi.nlm.nih.gov/40353334/)).

**Suggested GO/CL terms:** GO:0038165 (interleukin-11-mediated signaling pathway); GO:0007259 (JAK-STAT cascade / receptor signaling via STAT); GO:0060349 (bone morphogenesis); GO:0001503 (ossification); CL:0000062 (osteoblast); CL:0000092 (osteoclast); CL:0000055 (suture mesenchyme / cranial neural-crest-derived osteoprogenitors).

### 4. Pathway corroboration: gp130 (IL6ST)/SOCS3 axis and an independent GP130 craniosynostosis variant (F006)

IL-11 is an IL-6 family cytokine that signals through a receptor complex incorporating **gp130**. A review of the IL-6 cytokine family notes these cytokines have *"specific functions in craniofacial development, longitudinal bone growth, and the maintenance of trabecular and cortical bone structure, and have been implicated in musculoskeletal pathologies such as craniosynostosis,"* regulated by *"their negative feedback pathways, particularly suppressor of cytokine signaling 3 (SOCS3)"* ([PMID: 34332274](https://pubmed.ncbi.nlm.nih.gov/34332274/)). Independently, a variant in the **GP130 receptor subunit (IL6ST)** that selectively impairs IL11 signaling was also linked to craniosynostosis ([PMID: 32566365](https://pubmed.ncbi.nlm.nih.gov/32566365/)), providing orthogonal genetic validation of the IL11–gp130 axis as the critical node. IL-11 biology and emerging therapeutics are reviewed in [PMID: 31161823](https://pubmed.ncbi.nlm.nih.gov/31161823/).

### 5. Variant spectrum: biallelic missense, nonsense, frameshift, splice-site, and in-frame duplication, clustering near functional motifs (F013)

The IL11RA pathogenic allele catalog spans all major variant classes, each producing loss of function:

| Variant class | Examples | Source |
|---|---|---|
| Missense | p.Pro221Arg, p.Ser245Cys, p.Arg296Trp, p.Pro200Thr, p.Arg237Pro, p.Arg261Cys, p.Pro116Leu, p.Glu126Gly, p.Gly231Val, p.Leu236Pro | PMID 21741611, 24498618, 30811827, 40353334 |
| Nonsense | p.Gln159X, p.Tyr232*, p.Arg292*, p.Trp132Ter | PMID 21741611, 24498618, 40353334 |
| Frameshift | p.Pro218Argfs*140 | PMID 40353334 |
| Splice-site | c.479+6T>G (aberrant transcripts) | PMID 24498618 |
| In-frame duplication | c.916_924dup (p.Thr306_Ser308dup) | PMID 21741611, 30811827 |

Several variants cluster in functionally critical regions: *"these two mutation sites cluster together near a WSXWS motif that likely plays a significant role in regulating IL11RA protein function"* ([PMID: 30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/)). Compound-heterozygous and homozygous configurations both occur: *"a family with pansynostosis with compound heterozygous missense mutations, p.Pro200Thr and p.Arg237Pro; and two further Turkish families with Crouzon-like syndrome carrying the homozygous nonsense mutations p.Tyr232* and p.Arg292*"* ([PMID: 24498618](https://pubmed.ncbi.nlm.nih.gov/24498618/)). Per ACMG/AMP, LOF is an established mechanism for IL11RA, supporting pathogenic classification of truncating and functionally validated missense alleles.

### 6. Mouse and model-organism evidence recapitulates and extends the phenotype (F004, F009)

`Il11ra`-null mice show *"disturbed cranial growth and suture activity … in which reduced size and remodeling of limb bones has been previously described"* ([PMID: 21741611](https://pubmed.ncbi.nlm.nih.gov/21741611/)). Direct comparison of IL11 vs IL11RA1 knockouts established that *"loss of function (LOF) in IL11RA infers IL11 signaling as important for fertility, fibrosis, inflammation and incompletely penetrant craniosynostosis"* ([PMID: 34239012](https://pubmed.ncbi.nlm.nih.gov/34239012/)) — documenting both **incomplete penetrance** of craniosynostosis and the **pleiotropy** of the pathway. A classic reproductive phenotype shows *"female mice with a null mutation of the interleukin-11 receptor alpha chain are infertile because of defective decidualization"* ([PMID: 9500603](https://pubmed.ncbi.nlm.nih.gov/9500603/)); human data corroborate IL-11/IL-11Rα dysregulation in endometrium of infertile women with endometriosis ([PMID: 16310857](https://pubmed.ncbi.nlm.nih.gov/16310857/)).

### 7. Rarity and population genetics (F005)

*"A total of 41 similar patients have been reported with IL11RA variants"* as of 2019 ([PMID: 30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/)), rising to roughly 40–50 with subsequent reports. Carrier alleles are detectable at low frequency: in *"Non-Finnish Europeans … an allele frequency for p.Thr306_Ser308dup of 0.014% and p.Arg261Cys of 0.008%."* Ascertainment is enriched in consanguineous populations — three consanguineous Pakistani families ([PMID: 21741611](https://pubmed.ncbi.nlm.nih.gov/21741611/)) and Turkish families, including a 12-member family from Antakya and 5 mutation-positive families among a 79-patient craniosynostosis cohort ([PMID: 24498618](https://pubmed.ncbi.nlm.nih.gov/24498618/)).

---

## Section-by-Section Characterization

### 1. Disease Information
CRSDA (MONDO:0013615; OMIM:614188) is a rare autosomal recessive syndromic craniosynostosis defined by craniosynostosis plus dental anomalies and Crouzon-like facial features. Synonyms: **Kreiborg–Pakistani syndrome**, IL11RA-related Crouzon-like autosomal recessive craniosynostosis. Information is derived from **aggregated disease-level resources** (OMIM, case series) built on individual patient reports in consanguineous families, not large EHR cohorts.

### 2. Etiology
**Purely genetic/monogenic**: biallelic LOF variants in IL11RA (F001, F014). There is **no established environmental, infectious, lifestyle, or teratogenic contribution** — *"all affected children harbored homozygous … mutations"* ([PMID: 21741611](https://pubmed.ncbi.nlm.nih.gov/21741611/)). **Consanguinity** is the principal risk-amplifying factor. No protective variants or gene–environment interactions are described. Modifier contribution is suggested by incomplete penetrance of craniosynostosis in mice and intrafamilial phenotypic heterogeneity in humans, but specific human modifier genes are not established.

### 3. Phenotypes
See Finding 2 and HPO table above. Onset is **congenital** (cranial sutures) to **childhood** (dental). Severity is **variable** even within families; course is **non-episodic and lifelong/progressive** with respect to intracranial pressure and craniofacial growth. Quality-of-life impact arises from craniofacial deformity, functional visual/airway consequences of midface hypoplasia, hearing loss affecting speech/learning, and dental/orthodontic burden; no disease-specific QoL instrument data are available.

### 4. Genetic/Molecular Information
Causal gene **IL11RA (HGNC:5967)**, gene OMIM 600939, chr 9p13.3, UniProt Q14626. Variant spectrum per Finding 5. Functional consequence: **loss of function** (reduced STAT3 phosphorylation; reduced IL-11/gp130 binding). Inheritance biallelic (homozygous or compound heterozygous). No recurrent large chromosomal abnormality, aneuploidy, or established epigenetic lesion is implicated. gp130/IL6ST provides a second locus for a phenotypically overlapping craniosynostosis via impaired IL11 signaling (F006).

### 5. Environmental Information
**Not applicable** — no environmental, lifestyle, toxic, or infectious contributors are reported (F014). The disorder is defined solely by biallelic IL11RA LOF.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. Biallelic LOF variant in IL11RA (missense/nonsense/frameshift/splice/in-frame dup)
     -> results in a defective or absent IL-11 receptor alpha subunit
2. Defective IL11RA -> abolishes assembly of the functional IL-11 / IL11RA / gp130 (IL6ST) complex
     -> reduces ligand-binding affinity to IL-11 and gp130 [demonstrated: structural + binding assays]
3. Failed receptor signaling -> abrogates JAK-mediated STAT3 phosphorylation
     -> "dramatically reduced IL11-mediated STAT3 phosphorylation" [demonstrated in HEK293T/COS7]
4. Loss of STAT3 output -> removes the normal IL-11 restraint on osteogenic differentiation at sutures
     -> BRANCH A (bone): premature/excess suture ossification -> multisuture craniosynostosis
                         -> restricted calvarial/midface growth -> midface hypoplasia, exophthalmos,
                            prognathism, beaked nose; middle-ear involvement -> conductive hearing loss
     -> BRANCH B (teeth): loss of restraint on tooth number/eruption -> delayed eruption + supernumerary teeth
     -> BRANCH C (variable): connective-tissue effects -> joint hypermobility, disc fragility [inferred]
5. Fixed cranial deformity + ongoing brain growth -> recurrent, multifactorial intracranial hypertension
     -> clinical morbidity requiring staged surgical intervention
```

Steps 1–3 are **demonstrated** in vitro and by structural modeling; step 4 branches are supported by human phenotype–genotype correlation and `Il11ra`-null mouse recapitulation; the connective-tissue branch (C) and the precise cell-autonomous osteoblast/osteoclast balance are **inferred**. Negative feedback normally runs through **SOCS3** (F006). Upstream = IL11RA LOF; downstream = suture/tooth/ear phenotypes and ICP. Cell types: cranial suture mesenchyme, osteoblasts, osteoclasts, odontogenic epithelium/mesenchyme.

**Pathway/ontology terms:** KEGG JAK-STAT; Reactome "Interleukin-11 signaling"; GO:0038165, GO:0007259, GO:0001503, GO:0045669 (positive regulation of osteoblast differentiation).

### 7. Anatomical Structures Affected (F010)
- **Primary:** cranial sutures/calvaria (UBERON:0000211 suture / UBERON:0001684 skull), midface/maxilla (UBERON:0002397), teeth (UBERON:0001091), middle ear ossicles (UBERON:0001686).
- **Secondary/variable:** orbit (exophthalmos), axial skeleton/intervertebral discs (UBERON:0002412), joints/connective tissue; `Il11ra`-null mice also show reduced limb-bone size/remodeling.
- **Body systems:** skeletal, craniofacial, auditory, dental; reproductive in the mouse pleiotropy context. Lateralization: generally **bilateral/symmetric** for sutures, though suture-specific patterns vary.
- **Cell types (CL):** osteoblast (CL:0000062), osteoclast (CL:0000092), odontoblast (CL:0000060), chondrocyte (CL:0000138).

### 8. Temporal Development (F011)
Onset is **congenital** (premature suture fusion present from infancy) with dental features emerging through childhood. Course is **chronic, lifelong, progressive** (not episodic). *"Premature cranial base fusion correlates with recurrent increased ICP and repeated cranial vault remodeling procedures"* ([PMID: 42402848](https://pubmed.ncbi.nlm.nih.gov/42402848/)). Critical intervention windows coincide with skull growth in infancy/childhood; survival to adulthood is documented (two adult brothers, [PMID: 30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/)).

### 9. Inheritance and Population (F005, F012)
**Autosomal recessive** — *"it is inherited according to an autosomal recessive mode of inheritance"* ([PMID: 29926465](https://pubmed.ncbi.nlm.nih.gov/29926465/)); unaffected carrier parents carry **25% recurrence risk** per pregnancy. **Ultra-rare** (~40–50 reported). Enriched in **consanguineous Turkish/Pakistani** families; founder/recurrent alleles present. Penetrance of craniosynostosis is **incomplete** (mouse evidence); **expressivity is variable** with intrafamilial heterogeneity. Carrier alleles in gnomAD at 0.008–0.014% in Non-Finnish Europeans. No strong sex bias reported for the craniofacial phenotype.

### 10. Diagnostics (F007)
Diagnosis rests on recognizing **AR Crouzon-like syndromic craniosynostosis with dental anomalies** and confirming **biallelic IL11RA variants** by **whole-exome/targeted NGS with Sanger validation** — *"genetic analyses were carried out utilizing whole-exome sequencing, with subsequent validation through direct Sanger sequencing"* ([PMID: 40353334](https://pubmed.ncbi.nlm.nih.gov/40353334/)). Homozygosity mapping plus targeted sequencing identified cases among a *"cohort of 79 patients with an initial clinical diagnosis of Crouzon syndrome, pansynostosis, or unclassified syndromic craniosynostosis"* ([PMID: 24498618](https://pubmed.ncbi.nlm.nih.gov/24498618/)). **Differential diagnosis:** FGFR2-related Crouzon syndrome (AD) is the key mimic — *"two adult brothers diagnosed with Crouzon syndrome as children, in which the clinical diagnosis of CRSDA was made on reevaluation"* ([PMID: 30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/)); AR inheritance, dental anomalies, hearing loss, and negative FGFR testing distinguish CRSDA. Imaging (CT/3D-CT) defines suture fusion; audiometry documents conductive hearing loss. In a Turkish syndromic CS cohort, IL11RA was the gene specifically for *"craniosynostosis with dental anomaly"* ([PMID: 42084887](https://pubmed.ncbi.nlm.nih.gov/42084887/)).

### 11. Outcome / Prognosis (F008, F014)
Survival is **generally favorable** (adulthood documented). Morbidity is driven by **recurrent multifactorial intracranial hypertension** — *"intracranial hypertension in syndromic craniosynostosis is multifactorial. Abnormal cerebrospinal fluid circulation, venous hypertension, upper airway obstruction, and premature cranial base fusion appear to contribute substantially to disease progression"* ([PMID: 42402848](https://pubmed.ncbi.nlm.nih.gov/42402848/)) — plus craniofacial deformity, hearing loss, and dental complications. Crouzon-like phenotypes generally showed favorable surgical outcomes ([PMID: 42084887](https://pubmed.ncbi.nlm.nih.gov/42084887/)). Repeated procedures may be required.

### 12. Treatment (F008)
**No disease-specific pharmacotherapy or gene therapy exists.** Management is **multidisciplinary, primarily surgical and supportive**, following general syndromic craniosynostosis principles:
- **Cranial vault remodeling / fronto-orbital advancement** (NCIT clinical-intervention: Cranial Vault Remodeling; Fronto-Orbital Advancement).
- **Distraction osteogenesis**, including **posterior vault distraction osteogenesis (PVDO)** — *"intracranial volume increased by 36.3% at device removal and 27.8% at 1-year follow-up"* ([PMID: 41931363](https://pubmed.ncbi.nlm.nih.gov/41931363/)).
- **Endoscope-assisted suturectomy with orthotic therapy** and **spring-assisted cranioplasty** as minimally invasive options ([PMID: 42686138](https://pubmed.ncbi.nlm.nih.gov/42686138/); [PMID: 42853819](https://pubmed.ncbi.nlm.nih.gov/42853819/)).
- **Midface advancement**, **ENT/audiology** (hearing amplification), and **orthodontic/oral-surgical** management of dental anomalies.

Management is notably heterogeneous across centers ([PMID: 41627210](https://pubmed.ncbi.nlm.nih.gov/41627210/)). No pharmacogenomic, targeted, immunotherapy, or RNA-based therapy applies.

### 13. Prevention (F012)
Limited to **genetic counseling, carrier/cascade testing, and prenatal/preimplantation genetic diagnosis**; **no primary prevention** (etiology is monogenic). AR inheritance yields 25% recurrence risk; detectable gnomAD carrier alleles enable targeted screening in at-risk families, especially where **consanguinity** raises risk. Secondary/tertiary prevention = early surgical intervention and ICP surveillance to avert complications.

### 14. Other Species / Natural Disease (F004, F009)
Primary model species: **mouse (NCBI Taxon:10090)**, ortholog **Il11ra1**. `Il11ra`-null mice reproduce disturbed cranial growth/suture activity and reduced limb-bone size/remodeling, plus **female infertility** from defective decidualization ([PMID: 9500603](https://pubmed.ncbi.nlm.nih.gov/9500603/); [PMID: 34239012](https://pubmed.ncbi.nlm.nih.gov/34239012/)). No naturally occurring companion-animal/wildlife disease or zoonotic relevance is reported. IL11RA is a highly conserved gp130-family receptor, supporting evolutionary conservation of the mechanism.

### 15. Model Organisms (F004, F009)

| Model | Type | Key phenotype | Limitation |
|---|---|---|---|
| `Il11ra`-null mouse | Mammalian knockout | Disturbed cranial growth/suture activity; reduced limb-bone remodeling; **incompletely penetrant craniosynostosis**; female infertility | Incomplete penetrance; does not fully capture human dental/midface gestalt |
| `Il11` knockout mouse | Mammalian knockout | Fibro-inflammation (lung), fertility defects, craniosynostosis | Ligand- vs receptor-level differences |
| In-vitro HEK293T/COS7 | Cellular | Reduced IL11-mediated STAT3 phosphorylation (functional readout) | Not developmental context |

Resources: MGI, IMPC. Applications: suture biology, IL11–gp130–STAT3 signaling, bone remodeling, and the pleiotropic roles in fibrosis and reproduction.

---

## Mechanistic Model / Interpretation

CRSDA is best understood as a **loss-of-cytokine-restraint disorder**. In normal craniofacial development, IL-11 binds IL11RA, which partners with gp130 (IL6ST) to activate JAK–STAT3; this signal **restricts** osteogenic suture fusion and tooth number, held in check by SOCS3 negative feedback. Biallelic IL11RA LOF collapses this signal at its first obligatory step, so the developmental "brake" is released — sutures fuse prematurely (craniosynostosis), the midface fails to grow forward (Crouzon-like hypoplasia), and odontogenesis over-produces/mis-times teeth. The independent gp130/IL6ST craniosynostosis variant that selectively impairs IL11 signaling confirms that the **node**, not merely the gene, is what matters.

```
IL-11 --> IL11RA --> gp130(IL6ST) --> JAK --> STAT3 --> restrains suture fusion / tooth number
                               ^                              |
                               +-------- SOCS3 (-) <----------+
   [IL11RA LOF breaks this circuit -> disinhibited ossification + dental excess]
```

The same pathway's pleiotropy (fertility via decidualization, fibro-inflammation) explains why `Il11ra`/`Il11` knockouts show phenotypes beyond the skull, and raises the clinically relevant caveat that **systemic IL-11 pathway modulation is not a simple therapeutic lever** for this developmental disorder.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [21741611](https://pubmed.ncbi.nlm.nih.gov/21741611/) | Landmark (human + mouse) | Identified IL11RA as causal; defined phenotype; established LOF and developmental restraint role |
| [24498618](https://pubmed.ncbi.nlm.nih.gov/24498618/) | Confirmatory (human) | Additional families/variants; STAT3 phosphorylation defect; Crouzon differential |
| [40353334](https://pubmed.ncbi.nlm.nih.gov/40353334/) | Recent (human + structural) | Novel variants; impaired IL-11/gp130 binding via H-bond disruption; WES diagnostics |
| [30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/) | Clinical/population | Case count (~41); gnomAD carrier frequencies; WSXWS clustering; misdiagnosis as Crouzon |
| [29926465](https://pubmed.ncbi.nlm.nih.gov/29926465/) | Clinical series | AR inheritance; connective-tissue subset |
| [34239012](https://pubmed.ncbi.nlm.nih.gov/34239012/) | Model organism | Incomplete penetrance; pleiotropy (fertility, fibrosis, inflammation) |
| [9500603](https://pubmed.ncbi.nlm.nih.gov/9500603/) | Model organism | Reproductive pleiotropy (decidualization) |
| [34332274](https://pubmed.ncbi.nlm.nih.gov/34332274/) | Review | IL-6 family/gp130 in bone; SOCS3 feedback |
| [32566365](https://pubmed.ncbi.nlm.nih.gov/32566365/) | Corroborating gene | GP130/IL6ST variant -> craniosynostosis via impaired IL11 signaling |
| [31161823](https://pubmed.ncbi.nlm.nih.gov/31161823/) | Review | IL-11 biology and emerging therapeutics |
| [42402848](https://pubmed.ncbi.nlm.nih.gov/42402848/) | Surgical/clinical | Multifactorial ICP pathophysiology in syndromic CS |
| [41931363](https://pubmed.ncbi.nlm.nih.gov/41931363/) | Surgical | PVDO intracranial-volume outcomes |
| [42686138](https://pubmed.ncbi.nlm.nih.gov/42686138/), [42853819](https://pubmed.ncbi.nlm.nih.gov/42853819/), [41627210](https://pubmed.ncbi.nlm.nih.gov/41627210/) | Surgical | Distraction/spring/minimally invasive options; care heterogeneity |
| [42084887](https://pubmed.ncbi.nlm.nih.gov/42084887/) | Cohort | IL11RA as the gene for "craniosynostosis with dental anomaly" |
| [16310857](https://pubmed.ncbi.nlm.nih.gov/16310857/) | Human corroboration | IL-11/IL-11Rα dysregulation in infertile endometrium |

---

## Limitations and Knowledge Gaps

- **Small N:** ~40–50 patients limit precise penetrance, expressivity, sex-ratio, and QoL estimates; no formal prevalence/incidence figures exist.
- **Genotype–phenotype correlation is weak**, with documented intrafamilial heterogeneity; modifier genes in humans are unidentified.
- **Connective-tissue branch** mechanism is inferred, not mechanistically dissected.
- **No disease-specific natural-history study, registry, or validated QoL/outcome instrument.**
- **No targeted therapy;** whether IL-11 pathway augmentation could help is untested and complicated by pleiotropy.
- Some supporting surgical literature derives from general syndromic CS cohorts, not IL11RA-specific series.

## Proposed Follow-up Experiments / Actions

1. **Establish an international CRSDA registry** linking genotype, suture pattern, dental findings, hearing, ICP history, and surgical outcomes.
2. **Conditional/suture-specific `Il11ra` mouse models** and iPSC-derived cranial neural crest/osteoblast organoids to dissect the osteoblast–osteoclast balance and the tooth-number phenotype.
3. **Structural/biochemical deep-mutational scanning** of IL11RA mapped onto the IL-11/IL11RA/gp130 complex to functionally classify VUS and resolve the WSXWS-motif contribution.
4. **Define the connective-tissue subset** — ECM/collagen profiling in patients with joint hypermobility and disc fragility.
5. **Prospective comparison of surgical strategies** (PVDO vs cranial vault remodeling vs minimally invasive) specifically in IL11RA-confirmed patients, with ICP and neurocognitive endpoints.
6. **Carrier-screening pilots** in high-consanguinity populations using the known recurrent alleles.


## Artifacts

- [OpenScientist final report](Craniosynostosis_And_Dental_Anomalies-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Craniosynostosis_And_Dental_Anomalies-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 15 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000055` (1 mention) - the report calls it "suture mesenchyme / cranial neural-crest-derived osteoprogenitors"; CL calls it **obsolete non-terminally differentiated cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000055` (obsolete non-terminally differentiated cell) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001363` (1 mention) - the report calls it "Craniosynostosis (multisuture)"; HP calls it **Craniosynostosis**
- `HP:0011069` (1 mention) - the report calls it "Supernumerary teeth"; HP calls it **Supernumerary tooth**, and lists "Supernumerary teeth" among its other names
- `HP:0000520` (1 mention) - the report calls it "Proptosis / exophthalmos"; HP calls it **Proptosis**, and lists "Exophthalmos" among its other names
- `HP:0000303` (1 mention) - the report calls it "Relative prognathism"; HP calls it **Mandibular prognathia**, and lists "Relative mandibular prognathism" among its other names
- `GO:0038165` (2 mentions) - the report calls it "interleukin-11-mediated signaling pathway"; GO calls it **oncostatin-M-mediated signaling pathway**
- `GO:0007259` (2 mentions) - the report calls it "JAK-STAT cascade / receptor signaling via STAT"; GO calls it **cell surface receptor signaling pathway via JAK-STAT**, and lists "receptor signaling pathway via JAK-STAT" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Taxon`.