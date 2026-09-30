---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T14:07:38.989429'
end_time: '2026-09-28T14:27:55.479482'
duration_seconds: 1216.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Far-East Scarlet-Like Fever
  mondo_id: MONDO:0041536
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
citation_count: 45
reference_validation:
  total_references: 46
  verified: 46
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 46
  on_topic: 15
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 38
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 12
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0041536
    reported_labels:
    - MONDO
    ontology_label: Far-East scarlet-like fever
  - term_id: HP:0000202
    reported_labels:
    - Oral cavity abnormality
    ontology_label: Orofacial cleft
  labels_variant: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Far_East_Scarlet_Like_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Far_East_Scarlet_Like_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Far-East Scarlet-Like Fever
- **MONDO ID:** MONDO:0041536 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Far-East Scarlet-Like Fever** covering all of the
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

# Far-East Scarlet-Like Fever (FESLF): A Comprehensive Disease Characterization

**Disease:** Far-East Scarlet-Like Fever
**MONDO ID:** MONDO:0041536
**Category:** Infectious Disease
**Report type:** Multi-iteration autonomous literature synthesis for disease knowledge-base population

---

## Summary

**Far-East Scarlet-Like Fever (FESLF) is the severe, systemic, toxin-mediated clinical–epidemic form of infection by the enteric Gram-negative bacterium *Yersinia pseudotuberculosis*, occurring predominantly in the Russian Far East, Siberia, and Japan.** It is *not* a genetic or heritable disorder; it is an infectious disease whose distinctive severity is driven by strain-specific virulence factors carried by the "Asian clade" of *Y. pseudotuberculosis*. Where *Y. pseudotuberculosis* in Europe typically causes a self-limiting gastroenteritis or mesenteric adenitis, the Far-Eastern strains produce a scarlet-fever/Kawasaki-disease–like multisystem illness characterized by high fever, scarlatiniform rash, desquamation, strawberry tongue, cracked lips, conjunctivitis, gastrointestinal and hepatic involvement, and arthralgias.

The central molecular determinant of FESLF is the horizontally acquired superantigen gene **ypmA**, which encodes the **Y. pseudotuberculosis-derived mitogen A (YPMa)**. This structurally unique superantigen (jelly-roll fold, no homology to staphylococcal/streptococcal superantigens) cross-links MHC class II (HLA-DR) with T-cell receptor Vβ elements (Vβ3, 9, 13.1, 13.2), triggering a polyclonal, Vβ-restricted T-cell activation and a systemic IFN-γ/TNF-α cytokine storm. Far-Eastern FESLF strains additionally carry the **pVM82 (82-MDa) plasmid**, a molecular marker present *only* in strains causing the clinical-epidemic FESLF manifestation. The severity of disease is proportional to the intensity of TCR-Vβ engagement, as demonstrated by point-mutation studies in which weakened Vβ binding proportionally reduced T-cell overstimulation, cytotoxicity, and cytokine production.

FESLF sits at the intersection of scarlet fever, Japanese "Izumi fever," and Kawasaki disease (KD). *Y. pseudotuberculosis*-associated KD carries a significantly elevated risk of coronary artery lesions and IVIG resistance. The characteristic target lesion of the underlying infection is a granulomatous terminal ileitis and mesenteric lymphadenitis that histologically mimics Crohn's disease. Post-infectious immune sequelae — HLA-B27–associated reactive arthritis and erythema nodosum — are major contributors to long-term morbidity. Diagnosis rests on stool/blood culture, serology (agglutinating antibodies and anti-YPM antibody titers), and PCR for virulence genes; treatment is antibiotics plus supportive care, with IVIG/aspirin in KD-presenting pediatric cases. Prevention is through food and water hygiene, as the organism is transmitted through contaminated produce (notably carrots) and water.

---

## 1. Disease Information

**Overview.** FESLF is a severe systemic inflammatory disease caused by *Yersinia pseudotuberculosis*. It represents the special "clinical-epidemic" manifestation of pseudotuberculosis that occurs sporadically and in outbreaks in Russia and Japan, in contrast to the milder self-limiting gastroenteritis seen in Europe ([PMID: 26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/)). A case series of 12 culture-confirmed children established the multisystem phenotype and noted that the illness "resembled those of Izumi fever, an illness that occurs epidemically in Japan" ([PMID: 6344044](https://pubmed.ncbi.nlm.nih.gov/6344044/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0041536 |
| Causative organism (NCBI Taxonomy) | *Yersinia pseudotuberculosis*, txid633 |
| MeSH | Yersinia pseudotuberculosis Infections (D015008) |
| ICD-10 | A28.2 (Extraintestinal yersiniosis) / A04.8 |
| OMIM | Not applicable (non-genetic, infectious disease) |
| Orphanet | Not a listed rare Mendelian disease |

**Synonyms / alternative names.** Far East scarlet-like fever; Far Eastern scarlet-like fever; Izumi fever (Japan); Far-Eastern scarlatiniform fever; a clinical-epidemic form of pseudotuberculosis / extraintestinal yersiniosis. The relation to Izumi fever and Kawasaki disease is explicitly established in the literature ([PMID: 6344044](https://pubmed.ncbi.nlm.nih.gov/6344044/); [PMID: 39780644](https://pubmed.ncbi.nlm.nih.gov/39780644/)).

**Source of information.** The knowledge base is derived from **aggregated disease-level resources** — case series, outbreak investigations, genomic/phylogenetic studies, and mechanistic in vitro/animal experiments — rather than individual EHR-derived patient records.

---

## 2. Etiology

**Disease causal factors.** FESLF is caused by **infection** with *Y. pseudotuberculosis*, specifically Far-Eastern "Asian clade" strains carrying the superantigen gene ypmA and (in clinical-epidemic strains) the pVM82 plasmid ([PMID: 26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/); [PMID: 30695393](https://pubmed.ncbi.nlm.nih.gov/30695393/); [PMID: 39780644](https://pubmed.ncbi.nlm.nih.gov/39780644/)). The disease is fundamentally toxin-mediated: the YPM superantigen drives the systemic manifestations.

**Environmental risk factors.** Transmission is foodborne/waterborne; documented vehicles include contaminated grated carrots ([PMID: 23852698](https://pubmed.ncbi.nlm.nih.gov/23852698/)) and other fresh produce and water. The organism is psychrotrophic (grows at refrigeration temperatures), enabling amplification in stored vegetables. Age is a risk modifier — the underlying infection disproportionately affects children, and Yersinia-associated KD occurs at older onset age (3.05 ± 2.20 y vs 2.31 ± 2.05 y; p = 0.03) ([PMID: 17129979](https://pubmed.ncbi.nlm.nih.gov/17129979/)). Immunocompromise and iron overload predispose to invasive/septicemic disease ([PMID: 42448289](https://pubmed.ncbi.nlm.nih.gov/42448289/)).

**Genetic (host) risk factors.** Host genetics do not cause FESLF but modify post-infectious complications: **HLA-B27** strongly predisposes to reactive arthritis after *Y. pseudotuberculosis* infection ([PMID: 23852698](https://pubmed.ncbi.nlm.nih.gov/23852698/); [PMID: 12922960](https://pubmed.ncbi.nlm.nih.gov/12922960/)). The TCR Vβ repertoire of the host (Vβ3/9/13.1/13.2) determines which T cells respond to YPM. NOD2 and ATG16L1 autophagy polymorphisms have been implicated in susceptibility to Yersinia mucosal disease in the IBD context ([PMID: 42661478](https://pubmed.ncbi.nlm.nih.gov/42661478/)).

**Protective factors.** No germline protective alleles are established for FESLF itself. Antibiotic therapy and prior immunity (anti-YPM antibodies) modulate course. Food-hygiene behaviors are the principal protective/preventive measures.

**Gene–environment interactions.** The defining interaction is between the bacterial superantigen (environmental/infectious agent) and the host MHC-II/TCR-Vβ genotype: the same toxin produces variable illness depending on host HLA-DR and Vβ repertoire. Separately, HLA-B27 × Yersinia infection markedly raises reactive-arthritis risk — a classic gene–environment interaction.

---

## 3. Phenotypes

The core phenotype was quantified in a case series of 12 children with culture-confirmed *Y. pseudotuberculosis* (stool culture plus ≥4-fold agglutinating-antibody rise); clinical findings present in ≥50% of patients are listed below ([PMID: 6344044](https://pubmed.ncbi.nlm.nih.gov/6344044/)).

| Phenotype | Type | Frequency (≥50% cohort) | Suggested HPO term |
|---|---|---|---|
| Fever | Symptom | ≥50% | HP:0001945 |
| Scarlatiniform rash | Skin sign | ≥50% | HP:0000988 (Skin rash) |
| Diarrhea | Symptom | ≥50% | HP:0002014 |
| Desquamation | Skin sign | ≥50% | HP:0007556 (Palmoplantar desquamation) |
| Strawberry tongue | Sign | ≥50% | HP:0000206 (Glossitis, related) |
| Vomiting | Symptom | ≥50% | HP:0002013 |
| Red, cracked lips | Sign | ≥50% | HP:0000202 (Oral cavity abnormality) |
| Abdominal pain | Symptom | ≥50% | HP:0002027 |
| Arthralgias | Symptom | ≥50% | HP:0002829 |
| Hepatomegaly | Sign | ≥50% | HP:0002240 |
| Conjunctivitis | Sign | ≥50% | HP:0000509 |

Direct quote: *"Clinical findings in 50% or more of patients were fever, rash, diarrhea, desquamation, strawberry tongue, vomiting, red and cracked lips, abdominal pain, arthralgias, hepatomegaly and conjunctivitis"* ([PMID: 6344044](https://pubmed.ncbi.nlm.nih.gov/6344044/)).

Additional phenotypes documented in adults/severe cases: membranous fingertip/interdigital desquamation ([PMID: 42778384](https://pubmed.ncbi.nlm.nih.gov/42778384/); [PMID: 18411766](https://pubmed.ncbi.nlm.nih.gov/18411766/)), hepatic dysfunction and elevated inflammatory markers, erythema nodosum (42% of children in one carrot-borne outbreak), and reactive arthritis. Laboratory abnormalities include leukocytosis, elevated CRP/ferritin, and in severe cases thrombocytopenia with DIC ([PMID: 16366361](https://pubmed.ncbi.nlm.nih.gov/16366361/)).

**Onset/severity/progression.** Onset is acute (childhood-predominant). Severity ranges mild to severe; most cases are self-limited over days to weeks, but a subset progresses to systemic toxicity, coronary involvement (KD-like), DIC, or septicemia. Reactive arthritis can become chronic (>6 months) and rarely fatal (secondary amyloidosis).

**Quality-of-life impact.** Acute illness impairs feeding, activity, and school attendance. Chronic reactive arthritis and ankylosing spondylitis produce sustained functional disability; fatal amyloidosis with uremia has been reported in long-term follow-up ([PMID: 7554560](https://pubmed.ncbi.nlm.nih.gov/7554560/)).

---

## 4. Genetic / Molecular Information

**FESLF is not a human genetic disease — there are no causal human genes, pathogenic germline variants, or chromosomal abnormalities.** The relevant "genetics" are those of the pathogen and of host susceptibility loci.

**Pathogen virulence genes.**

| Determinant | Function | Association with FESLF |
|---|---|---|
| **ypmA** (encodes YPMa) | Superantigen mitogen | Present in 96.2% of Far-Eastern strains; hallmark of systemic disease ([PMID: 17163133](https://pubmed.ncbi.nlm.nih.gov/17163133/)) |
| **ypmB, ypmC** | Superantigen variants | ypmB Far-East-restricted cluster B; ypmC rare ([PMID: 21131531](https://pubmed.ncbi.nlm.nih.gov/21131531/)) |
| **pVM82 (82-MDa) plasmid** | Uncharacterized virulence | Present *only* in clinical-epidemic FESLF strains ([PMID: 30695393](https://pubmed.ncbi.nlm.nih.gov/30695393/)) |
| **pYV virulence plasmid (virF)** | Type III secretion system / Yops | Universal in pathogenic strains ([PMID: 18242014](https://pubmed.ncbi.nlm.nih.gov/18242014/)) |
| **inv** (invasin) | β1-integrin adhesion, M-cell invasion | Universal; mediates epithelial crossing ([PMID: 25576025](https://pubmed.ncbi.nlm.nih.gov/25576025/)) |
| **HPI / irp2** | High-pathogenicity island (iron uptake) | Absent in dominant FESLF genogroup ([PMID: 17163133](https://pubmed.ncbi.nlm.nih.gov/17163133/)) |
| **pil** (type IV pilus) | Adhesion | Co-acquired with ypm horizontally ([PMID: 15784605](https://pubmed.ncbi.nlm.nih.gov/15784605/)) |

The dominant systemic-infection genogroup is **pYV⁺ / ypmA⁺ / HPI⁻** (95.8% of Siberian/Far-Eastern strains) ([PMID: 17163133](https://pubmed.ncbi.nlm.nih.gov/17163133/)). The ypm and pil genes were laterally (horizontally) acquired and are significantly co-associated ([PMID: 15784605](https://pubmed.ncbi.nlm.nih.gov/15784605/)).

**Host susceptibility loci.** HLA-B27 (reactive arthritis modifier); HLA-DR (YPM presentation); TCR Vβ genes BV3S1, BV9, BV13 (target of YPM); C4B copy number (modifies Yersinia-microbiota interaction in pediatric IBD) ([PMID: 28832994](https://pubmed.ncbi.nlm.nih.gov/28832994/)).

**Epigenetics.** No disease-specific human epigenetic signature is established for FESLF. Superantigen-driven T-cell activation induces transcriptional/epigenetic reprogramming toward effector/memory phenotypes ([PMID: 11937534](https://pubmed.ncbi.nlm.nih.gov/11937534/)), but this is not disease-defining.

---

## 5. Environmental Information

**Infectious agent.** *Yersinia pseudotuberculosis* (family Yersiniaceae; NCBI Taxonomy txid633), a Gram-negative, psychrotrophic, facultatively anaerobic coccobacillus. Serotypes O:1 (incl. Ib) and O:3 are the principal causes of documented outbreaks and post-infectious complications; serotypes 4b and 1b predominate in fatal Japanese monkey outbreaks ([PMID: 18242014](https://pubmed.ncbi.nlm.nih.gov/18242014/)).

**Environmental factors.** The organism is widespread in the terrestrial environment and can persist in soil and water, in wildlife reservoirs (rodents, wild boars, birds), and even the marine habitat ([PMID: 42431144](https://pubmed.ncbi.nlm.nih.gov/42431144/); [PMID: 29980552](https://pubmed.ncbi.nlm.nih.gov/29980552/)). Its cold tolerance allows growth in refrigerated foods.

**Lifestyle factors.** Consumption of raw or improperly washed vegetables (carrots, lettuce) and untreated water; contact with animal reservoirs. Outbreaks are typically food/water-associated. The dominant environmental "cause" is ingestion of contaminated food, then M-cell invasion in the terminal ileum.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Ingestion** of *Y. pseudotuberculosis* (Asian-clade, ypmA⁺, pVM82⁺) in contaminated food/water → **leads to** delivery of viable bacteria to the terminal ileum.
2. Bacterial **invasin binds host β1-integrins on M cells** of Peyer's patches → **results in** translocation across the intestinal epithelium ([PMID: 25576025](https://pubmed.ncbi.nlm.nih.gov/25576025/)).
3. Bacteria reach the **mesenteric lymph nodes, liver, and spleen**; the type III secretion system (pYV/Yops) is selectively translocated into **professional phagocytes** (neutrophils, macrophages, dendritic cells), disarming innate clearance → **leads to** local persistence and **granulomatous terminal ileitis / mesenteric lymphadenitis** ([PMID: 20148898](https://pubmed.ncbi.nlm.nih.gov/20148898/); [PMID: 34628159](https://pubmed.ncbi.nlm.nih.gov/34628159/)).
4. The bacterium **secretes/expresses the superantigen YPMa** → which **binds MHC class II (HLA-DR) on antigen-presenting cells** outside the conventional peptide groove ([PMID: 10406939](https://pubmed.ncbi.nlm.nih.gov/10406939/)).
5. The MHC-II–YPM complex **cross-links T-cell receptors bearing Vβ3, 9, 13.1, 13.2** → **results in** massive polyclonal (Vβ-restricted) T-cell activation ([PMID: 9287138](https://pubmed.ncbi.nlm.nih.gov/9287138/); [PMID: 17369701](https://pubmed.ncbi.nlm.nih.gov/17369701/)).
6. Activated Vβ⁺ T cells **migrate from blood to liver within 1 h** and **release a cytokine storm** (IFN-γ by 4 h, plus TNF-α, IL-1, IL-6, IFN-α) → **leads to** systemic inflammation, hepatic injury, and toxic shock ([PMID: 15003813](https://pubmed.ncbi.nlm.nih.gov/15003813/); [PMID: 12449699](https://pubmed.ncbi.nlm.nih.gov/12449699/)).
7. Systemic cytokine excess and vascular inflammation **produce the clinical syndrome**: fever, scarlatiniform rash, desquamation, strawberry tongue, conjunctivitis, hepatomegaly → the FESLF/Kawasaki-like phenotype.
   - **Branch A (severity):** the *intensity* of TCR-Vβ binding scales the magnitude of T-cell overstimulation, cytotoxicity, and cytokine output → **determines** disease severity ([PMID: 10087177](https://pubmed.ncbi.nlm.nih.gov/10087177/)).
   - **Branch B (cardiac):** in a subset, superantigen-driven vasculitis → **coronary artery dilation/aneurysm** (Kawasaki-disease phenotype), with higher coronary-lesion rates and IVIG resistance in Yersinia-associated KD ([PMID: 17129979](https://pubmed.ncbi.nlm.nih.gov/17129979/)).
   - **Branch C (post-infectious autoimmunity):** in HLA-B27⁺ hosts, molecular/immune cross-reactivity → **reactive arthritis, ankylosing spondylitis, erythema nodosum**, rarely secondary amyloidosis ([PMID: 23852698](https://pubmed.ncbi.nlm.nih.gov/23852698/); [PMID: 7554560](https://pubmed.ncbi.nlm.nih.gov/7554560/)).

### Detail by category

- **Molecular pathways:** TCR/CD3 → ZAP-70 → PLCγ/PKC/NF-κB and Ras-MAPK signaling driving IL-2/IFN-γ transcription (superantigen-driven); β1-integrin → PI3K signaling in invasin-mediated neutrophil activation and NET formation ([PMID: 25576025](https://pubmed.ncbi.nlm.nih.gov/25576025/)); RhoG/Rac1 GTPase modulation by invasin/Yops during invasion ([PMID: 19208761](https://pubmed.ncbi.nlm.nih.gov/19208761/)).
- **Cellular processes:** massive T-cell proliferation and later anergy/deletion; macrophage/DC activation; neutrophil extracellular trap (NET) release; inflammasome activation and pyroptosis in Yersinia mucosal disease ([PMID: 42661478](https://pubmed.ncbi.nlm.nih.gov/42661478/)); granuloma formation.
- **Protein dysfunction (toxin structure):** YPMa is a ~150-aa protein adopting a **jelly-roll fold** resembling viral capsid/TNF-superfamily proteins, with no sequence homology to other superantigens; crystallized in space group C2, 1.8 Å resolution; an internal disulfide (S–S) bond is essential for activity ([PMID: 12832802](https://pubmed.ncbi.nlm.nih.gov/12832802/); [PMID: 17369701](https://pubmed.ncbi.nlm.nih.gov/17369701/); [PMID: 10406939](https://pubmed.ncbi.nlm.nih.gov/10406939/)).
- **Immune system involvement:** superantigen-mediated polyclonal T-cell activation, IFN-γ–dominated cytokine storm; T-cell-dependent toxicity (toxic shock in BALB/c but **not** T-cell-deficient SCID mice) ([PMID: 15003813](https://pubmed.ncbi.nlm.nih.gov/15003813/)).
- **Tissue damage mechanisms:** IFN-γ/TNF-α–mediated hepatocellular injury; immune-complex and vasculitic damage to coronary vessels; granulomatous necrosis in ileum/lymph nodes.
- **Suggested GO terms:** GO:0042110 (T cell activation), GO:0032609 (interferon-gamma production), GO:0050852 (T cell receptor signaling pathway), GO:0006955 (immune response), GO:0002250 (adaptive immune response), GO:0001816 (cytokine production).
- **Suggested CL terms:** CL:0000624 (CD4⁺ T cell), CL:0000625 (CD8⁺ T cell), CL:0000775 (neutrophil), CL:0000235 (macrophage), CL:0000451 (dendritic cell), CL:0000794 (CD8⁺ cytotoxic T cell).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** terminal ileum (UBERON:0002116), mesenteric lymph nodes (UBERON:0002509), liver (UBERON:0002107).
- **Secondary/systemic:** skin (UBERON:0002097), oral mucosa/tongue (UBERON:0001723), conjunctiva (UBERON:0001811), coronary arteries (UBERON:0001621) in KD-like cases, joints/synovium (UBERON:0002217) in reactive arthritis, spleen (UBERON:0002106), pancreas (UBERON:0001264; Yersinia pancreatitis, [PMID: 22416431](https://pubmed.ncbi.nlm.nih.gov/22416431/)).
- **Body systems:** digestive, lymphatic/immune, integumentary, cardiovascular, musculoskeletal, hepatobiliary.

**Tissue/cell level.** Intestinal epithelium (M cells), lymphoid tissue (Peyer's patches, UBERON:0001211), vascular endothelium (coronary artery endothelial cells), synovium. Cell populations: CD4⁺/CD8⁺ T cells (Vβ3/9/13⁺), professional phagocytes, epithelioid histiocytes forming granulomas with giant cells.

**Subcellular level.** T-cell plasma membrane (TCR–MHC-II synapse); cytokine secretory machinery (ER/Golgi). Suggested GO cellular-component terms: GO:0009897 (external side of plasma membrane), GO:0042101 (T cell receptor complex), GO:0042613 (MHC class II protein complex).

**Localization/lateralization.** Terminal ileitis is typically right-lower-quadrant, mimicking appendicitis; coronary lesions may be bilateral; reactive arthritis is often asymmetric oligoarticular (lower limbs) but can be polyarticular ([PMID: 12922960](https://pubmed.ncbi.nlm.nih.gov/12922960/)).

---

## 8. Temporal Development

**Onset.** Acute, pediatric-predominant; incubation typically a few days to ~2 weeks after ingestion. In the case series the illness was acute and multisystem ([PMID: 6344044](https://pubmed.ncbi.nlm.nih.gov/6344044/)).

**Progression and course.** Most acute illness is **self-limited** over 1–3 weeks. A minority progress to systemic toxicity (toxic-shock-like), DIC ([PMID: 16366361](https://pubmed.ncbi.nlm.nih.gov/16366361/)), coronary involvement, or septicemia (higher risk in immunocompromised/iron-overloaded hosts, [PMID: 42448289](https://pubmed.ncbi.nlm.nih.gov/42448289/)). Post-infectious reactive arthritis appears days to weeks after the acute phase and may persist >6 months in a substantial fraction; a 10-year follow-up found chronic joint symptoms in 9/16 patients including ankylosing spondylitis and fatal secondary amyloidosis ([PMID: 7554560](https://pubmed.ncbi.nlm.nih.gov/7554560/)).

**Patterns.** Acute phase resolves spontaneously or with antibiotics; complications may be relapsing (reactive arthritis reactivation) or progressive (spondyloarthropathy/amyloidosis). The critical intervention window for KD-like cases is the first ~10 days (IVIG to prevent coronary aneurysm).

---

## 9. Inheritance and Population

**Inheritance.** None — FESLF is infectious, not heritable. No Mendelian inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency applies to the disease itself. (Host modifiers such as HLA-B27 follow their own inheritance but only affect complication risk.)

**Epidemiology and geography.** FESLF is **geographically restricted** to the Russian Far East, Siberia, and Japan, occurring sporadically and in outbreaks ([PMID: 26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/); [PMID: 32498317](https://pubmed.ncbi.nlm.nih.gov/32498317/)). This restriction tracks the geographic distribution of ypmA⁺ Asian-clade strains: ypmA detected in **96.2%** of 212 Siberian/Far-Eastern strains ([PMID: 17163133](https://pubmed.ncbi.nlm.nih.gov/17163133/)) and **88.9%** of fatal Japanese monkey-outbreak strains ([PMID: 18242014](https://pubmed.ncbi.nlm.nih.gov/18242014/)). By contrast, European *Y. pseudotuberculosis* infection is sporadic self-limiting gastroenteritis ([PMID: 26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/)). General yersiniosis incidence in non-endemic regions is low (e.g., ~0.16/100,000/yr in a multistate US study; *Y. pseudotuberculosis* is a small minority of cases) ([PMID: 25931631](https://pubmed.ncbi.nlm.nih.gov/25931631/); [PMID: 26233079](https://pubmed.ncbi.nlm.nih.gov/26233079/)).

**Demographics.** Children are predominantly affected; Yersinia-associated KD onset is older than Yersinia-negative KD (3.05 vs 2.31 y; p = 0.03) ([PMID: 17129979](https://pubmed.ncbi.nlm.nih.gov/17129979/)). Sex ratio is not strongly skewed for the acute disease; HLA-B27-associated reactive arthritis affects both sexes.

**Population structure of the pathogen.** MLST reveals a worldwide **cluster A** (ypmA, pYV) and a Far-East-restricted **cluster B** (ypmB); the ypm superantigen genes are distributed across the phylogeny with ypmA in cluster A and ypmB in cluster B ([PMID: 21131531](https://pubmed.ncbi.nlm.nih.gov/21131531/)). FESLF strains belong to the **Asian clade** and are KD-related ([PMID: 39780644](https://pubmed.ncbi.nlm.nih.gov/39780644/)).

---

## 10. Diagnostics

**Microbiology.** Stool culture and/or blood culture for *Y. pseudotuberculosis* (cold enrichment improves yield); serotyping (O:1, O:3, 4b). Blood culture positivity in septicemic cases ([PMID: 18411766](https://pubmed.ncbi.nlm.nih.gov/18411766/)).

**Serology.** ≥4-fold rise in agglutinating antibody titers is diagnostic ([PMID: 6344044](https://pubmed.ncbi.nlm.nih.gov/6344044/)); tube agglutination titers (e.g., ≥1:160 against serotype 4b) support diagnosis ([PMID: 18411766](https://pubmed.ncbi.nlm.nih.gov/18411766/)). **Anti-YPM (anti-mitogen) antibody titers** rise between days 7–18 and confirm infection when cultures are negative ([PMID: 34108299](https://pubmed.ncbi.nlm.nih.gov/34108299/); [PMID: 16366361](https://pubmed.ncbi.nlm.nih.gov/16366361/)). Serology is described as the most informative laboratory approach ([PMID: 22416431](https://pubmed.ncbi.nlm.nih.gov/22416431/)).

**Molecular.** PCR for virulence genes — ypm (ypmA/B/C), virF, inv, irp2 — enables genotype-based confirmation and epidemiologic typing ([PMID: 18242014](https://pubmed.ncbi.nlm.nih.gov/18242014/); [PMID: 22416431](https://pubmed.ncbi.nlm.nih.gov/22416431/)).

**Laboratory abnormalities.** Leukocytosis, elevated CRP/ferritin, transaminase elevation (hepatic involvement), thrombocytopenia and prolonged PT/PTT with elevated FDP in DIC ([PMID: 16366361](https://pubmed.ncbi.nlm.nih.gov/16366361/)).

**Imaging/histopathology.** Ultrasound/CT show mesenteric lymphadenopathy and terminal ileitis; echocardiography detects coronary dilation/aneurysm in KD-like cases. **Biopsy** shows epithelioid granulomas with reticular microabscesses/stellate necrosis and giant cells, mimicking Crohn's disease ([PMID: 22228001](https://pubmed.ncbi.nlm.nih.gov/22228001/); [PMID: 18368812](https://pubmed.ncbi.nlm.nih.gov/18368812/); [PMID: 26385573](https://pubmed.ncbi.nlm.nih.gov/26385573/)).

**Clinical criteria / differential diagnosis.** When patients meet Kawasaki-disease criteria (fever ≥5 days plus ≥4 of: rash, conjunctivitis, oral changes, extremity changes, cervical lymphadenopathy), *Y. pseudotuberculosis* should be excluded ([PMID: 39697956](https://pubmed.ncbi.nlm.nih.gov/39697956/)). Differentials: scarlet fever (Group A *Streptococcus*), Kawasaki disease, appendicitis, Crohn's disease, mesenteric adenitis of other cause, other yersiniosis. Genetic testing is **not applicable** (no germline cause).

---

## 11. Outcome / Prognosis

**Survival/mortality.** The acute disease is usually self-limited with low mortality when treated. Severe outcomes include septicemia with multi-organ dysfunction (fatal cases reported, especially in immunocompromised/iron-overload hosts, [PMID: 42448289](https://pubmed.ncbi.nlm.nih.gov/42448289/)) and DIC ([PMID: 16366361](https://pubmed.ncbi.nlm.nih.gov/16366361/)). Long-term fatal outcomes are rare and usually via reactive-arthritis complications (secondary amyloidosis → uremia) ([PMID: 7554560](https://pubmed.ncbi.nlm.nih.gov/7554560/)).

**Morbidity/complications.** Coronary artery lesions (KD phenotype): significantly more frequent in Yersinia-positive KD (22/42, 52.4%) than Yersinia-negative KD (105/330, 31.8%; p = 0.001), with greater need for additional IVIG (36.1% vs 16.0%; p = 0.004) ([PMID: 17129979](https://pubmed.ncbi.nlm.nih.gov/17129979/)). Post-infectious reactive arthritis in 12–22% of adults, HLA-B27-associated, sometimes chronic/polyarticular ([PMID: 23852698](https://pubmed.ncbi.nlm.nih.gov/23852698/); [PMID: 12922960](https://pubmed.ncbi.nlm.nih.gov/12922960/)); erythema nodosum (42% of children in one outbreak); rarely ankylosing spondylitis and amyloidosis.

**Prognostic factors.** Presence of ypmA⁺ Far-Eastern strain and pVM82 plasmid (severity); host HLA-B27 (reactive-arthritis risk); older age and Yersinia positivity (coronary-lesion risk and IVIG resistance in KD); immunocompromise/iron overload (septicemia risk). Anti-YPM antibody serology serves as a diagnostic/prognostic biomarker.

---

## 12. Treatment

**Pharmacotherapy (antibiotics).** *Y. pseudotuberculosis* is generally susceptible to third-generation cephalosporins (cefotaxime, ceftriaxone), fluoroquinolones, aminoglycosides, tetracyclines, and trimethoprim-sulfamethoxazole; carbapenems (imipenem) used in severe/septicemic disease ([PMID: 18411766](https://pubmed.ncbi.nlm.nih.gov/18411766/)). Refractory KD-presenting cases have responded to cefotaxime after immunosuppressive therapy ([PMID: 39697956](https://pubmed.ncbi.nlm.nih.gov/39697956/)). Suggested NCIT: C264 (Cephalosporin), C540 (Ciprofloxacin), C61796 (Cefotaxime).

**Kawasaki-disease-presenting cases.** Intravenous immunoglobulin (IVIG) plus aspirin to reduce coronary complications; note higher IVIG-resistance in Yersinia-associated KD, sometimes requiring additional IVIG or immunosuppression ([PMID: 17129979](https://pubmed.ncbi.nlm.nih.gov/17129979/); [PMID: 39697956](https://pubmed.ncbi.nlm.nih.gov/39697956/)). NCIT: C488 (Immunoglobulin therapy), C287 (Aspirin).

**Reactive arthritis.** NSAIDs, and in chronic/severe spondyloarthropathy, DMARDs; supportive rheumatologic care.

**Supportive care.** Fluid/electrolyte management for diarrhea/vomiting; DIC management; hepatic monitoring.

**Advanced/experimental therapeutics.** A conceptual therapeutic avenue arises from mutagenesis work: engineered YPM point mutants with reduced TCR-Vβ binding lose overstimulatory/cytotoxic activity and could serve as immunotherapeutic/vaccine antigens ([PMID: 10087177](https://pubmed.ncbi.nlm.nih.gov/10087177/)). Anti-IFN-γ and anti-YPM antibodies prevented liver injury and death in mice — a proof-of-concept for toxin/cytokine-neutralizing therapy ([PMID: 15003813](https://pubmed.ncbi.nlm.nih.gov/15003813/)). No approved gene, cell, or RNA therapy exists or is applicable.

**Pharmacogenomics.** Not established for FESLF.

---

## 13. Prevention

**Primary prevention.** Food and water hygiene: thorough washing of raw vegetables (carrots, leafy greens), safe water, cold-chain awareness (organism grows at refrigeration temperatures). Outbreak control through tracing contaminated produce ([PMID: 23852698](https://pubmed.ncbi.nlm.nih.gov/23852698/)).

**Immunization.** No licensed human vaccine against *Y. pseudotuberculosis*/FESLF. An attenuated *Y. pseudotuberculosis* strain (lacking HPI, ypm, pil; retaining pYV) has been used experimentally as an oral live vaccine against plague, protecting 75–88% of mice — illustrating vaccine-platform potential but not a FESLF vaccine ([PMID: 18505804](https://pubmed.ncbi.nlm.nih.gov/18505804/)).

**Secondary/tertiary prevention.** Early antibiotic treatment; early echocardiography and IVIG in KD-presenting cases to prevent coronary aneurysm; monitoring/treatment of reactive arthritis to prevent chronic sequelae.

**Public health.** Surveillance of foodborne yersiniosis; produce-supply monitoring; reservoir awareness (rodents, wild boars, birds). Vector control is not relevant (foodborne, not vector-borne).

---

## 14. Other Species / Natural Disease

**Taxonomy of causative agent.** *Yersinia pseudotuberculosis* (NCBI:txid633).

**Natural disease in animals.** Pseudotuberculosis is a common cause of mortality in captive exotic birds and mammals; per OIE WAHIS-Wild it is the 8th most frequently reported disease/infection in wildlife worldwide and 5th in wild mammals ([PMID: 42431144](https://pubmed.ncbi.nlm.nih.gov/42431144/)). Fatal outbreaks in **breeding monkeys** in Japanese zoos (28 deaths, 8 species; 88.9% ypmA⁺) directly parallel human FESLF and implicate YPM in high mortality ([PMID: 18242014](https://pubmed.ncbi.nlm.nih.gov/18242014/)). Documented in wild boars ([PMID: 29980552](https://pubmed.ncbi.nlm.nih.gov/29980552/)) and, newly, free-ranging marine odontocetes ([PMID: 42431144](https://pubmed.ncbi.nlm.nih.gov/42431144/)).

**Zoonotic potential / reservoirs.** Rodents, birds, and other mammals serve as reservoirs; transmission to humans is principally by ingestion of contaminated food or water. Cross-species susceptibility is broad.

**Comparative biology.** The superantigen mechanism is conserved: ypmA⁺ strains cause severe/fatal systemic disease across primates and humans, supporting evolutionary conservation of the YPM–MHC-II/TCR-Vβ axis.

---

## 15. Model Organisms

**Mouse models.** BALB/c mice develop YPM-induced toxic shock; **T-cell-deficient SCID mice do not**, establishing T-cell dependence ([PMID: 15003813](https://pubmed.ncbi.nlm.nih.gov/15003813/)). Mini-osmotic-pump delivery of YPM produces protracted Vβ3⁺CD4⁺ T-cell expansion and immunological memory, modeling chronic superantigen exposure ([PMID: 11937534](https://pubmed.ncbi.nlm.nih.gov/11937534/)). A murine coronary-arteritis (KD) model is induced by oral microbe-associated molecular patterns, linking Yersinia biofilm MAMPs to KD-like vasculitis ([PMID: 25411968](https://pubmed.ncbi.nlm.nih.gov/25411968/)).

**Rat models.** **HLA-B27 transgenic rats** mount a CD8⁺ CTL response to *Y. pseudotuberculosis*; HLA-B27 exerts a negative effect on this response, modeling impaired defense and the HLA-B27–reactive-arthritis link ([PMID: 10417137](https://pubmed.ncbi.nlm.nih.gov/10417137/)). LEW rat BV8S2⁺ T cells respond to YPM, used to map TCR CDR/HV4 contributions to superantigen recognition ([PMID: 15096488](https://pubmed.ncbi.nlm.nih.gov/15096488/)).

**Non-human primates.** Naturally infected breeding monkeys constitute a spontaneous high-fidelity model of fatal systemic ypmA⁺ disease ([PMID: 18242014](https://pubmed.ncbi.nlm.nih.gov/18242014/)).

**In vitro / structural.** Human whole-blood cytokine assays (YPM elicits maximal IL-1/IL-6/IFN-α/TNF-α, [PMID: 12449699](https://pubmed.ncbi.nlm.nih.gov/12449699/)); recombinant YPM mutagenesis systems for structure–function ([PMID: 10406939](https://pubmed.ncbi.nlm.nih.gov/10406939/); [PMID: 10087177](https://pubmed.ncbi.nlm.nih.gov/10087177/)); X-ray crystallography/NMR of YPMa ([PMID: 12832802](https://pubmed.ncbi.nlm.nih.gov/12832802/); [PMID: 17369701](https://pubmed.ncbi.nlm.nih.gov/17369701/)).

**Recapitulation/limitations.** Mouse models capture superantigen-driven T-cell activation and toxic shock but incompletely reproduce the full mucosal→systemic human sequence; the HLA-B27 rat captures the reactive-arthritis modifier but not the acute scarlatiniform phenotype.

---

## Mechanistic Model / Interpretation

```
 CONTAMINATED FOOD/WATER (ypmA+, pVM82+, pYV+ Asian-clade Y. pseudotuberculosis)
        │  ingestion
        ▼
 TERMINAL ILEUM ── invasin·β1-integrin ──► M-cell translocation (Peyer's patches)
        │
        ▼
 MESENTERIC LYMPH NODES / LIVER / SPLEEN
        │  T3SS(Yops)→phagocytes: immune evasion + granulomatous ileitis/adenitis
        │  (Crohn's-mimicking target lesion)
        ▼
 YPMa SUPERANTIGEN ── binds HLA-DR (MHC-II) + TCR Vβ3/9/13.1/13.2 ──►
        │  polyclonal, Vβ-restricted T-cell activation
        ▼
 CYTOKINE STORM (IFN-γ @4h, TNF-α, IL-1, IL-6, IFN-α)   ── T-cell-dependent
        │                                                  (absent in SCID mice)
        ├──────────────► SYSTEMIC ILLNESS: fever, scarlatiniform rash,
        │                desquamation, strawberry tongue, conjunctivitis,
        │                hepatomegaly  =  FESLF / Izumi fever
        │
        ├── Branch A (dose/affinity): TCR-Vβ binding intensity → SEVERITY
        │
        ├── Branch B: coronary vasculitis → KD phenotype (↑coronary lesions,
        │              IVIG resistance)
        │
        └── Branch C (HLA-B27+ host): post-infectious reactive arthritis,
                       ankylosing spondylitis, erythema nodosum, amyloidosis
```

The unifying interpretation is that FESLF is fundamentally a **superantigen toxicosis superimposed on an enteric invasive infection**. What distinguishes the Far-Eastern severe disease from European mild yersiniosis is not the route or the organism per se but the horizontally acquired **ypmA** superantigen (plus the enigmatic **pVM82** plasmid). Severity is a graded function of TCR-Vβ engagement, and the host HLA background (HLA-DR for presentation, HLA-B27 for post-infectious autoimmunity) shapes both acute magnitude and chronic sequelae. This model explains the disease's geographic restriction, its overlap with scarlet fever and Kawasaki disease, and the rationale for both antibiotic (source control) and immunomodulatory (IVIG/anti-cytokine) treatment.

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [6344044](https://pubmed.ncbi.nlm.nih.gov/6344044/) | Defines the multisystem scarlet-fever/KD-like phenotype; links to Izumi fever (12-child series) |
| [39780644](https://pubmed.ncbi.nlm.nih.gov/39780644/) | FESLF strains = Asian clade, KD-related (genomics) |
| [26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/) | Review: FESLF definition, Russia/Japan geography, YPMa role |
| [30695393](https://pubmed.ncbi.nlm.nih.gov/30695393/) | pVM82 plasmid unique to FESLF clinical-epidemic strains |
| [17163133](https://pubmed.ncbi.nlm.nih.gov/17163133/) | ypmA in 96.2% of Far-Eastern strains; pYV⁺/ypmA⁺/HPI⁻ systemic genogroup |
| [18242014](https://pubmed.ncbi.nlm.nih.gov/18242014/) | 88.9% ypmA⁺ in fatal Japanese monkey outbreaks |
| [15784605](https://pubmed.ncbi.nlm.nih.gov/15784605/) | Horizontal acquisition/linkage of ypm and pil |
| [21131531](https://pubmed.ncbi.nlm.nih.gov/21131531/) | Population structure: cluster A (ypmA) worldwide, cluster B (ypmB) Far-East |
| [15003813](https://pubmed.ncbi.nlm.nih.gov/15003813/) | T-cell-dependent YPM toxicity; Vβ8⁺ migration to liver; IFN-γ surge; antibody protection |
| [12449699](https://pubmed.ncbi.nlm.nih.gov/12449699/) | YPM = maximal cytokine inducer among Yersinia stimuli |
| [12832802](https://pubmed.ncbi.nlm.nih.gov/12832802/) | YPM crystallization; no homology to other superantigens |
| [17369701](https://pubmed.ncbi.nlm.nih.gov/17369701/) | Jelly-roll fold of YPMa; YPMa/b/c family |
| [10406939](https://pubmed.ncbi.nlm.nih.gov/10406939/) | YPM competes with SEE for HLA-DR; MHC-II/TCR mapping; essential S–S bond |
| [9287138](https://pubmed.ncbi.nlm.nih.gov/9287138/) | YPMb shares Vβ3/9/13.1/13.2 specificity |
| [10087177](https://pubmed.ncbi.nlm.nih.gov/10087177/) | TCR-Vβ binding intensity determines pathogenic severity |
| [17129979](https://pubmed.ncbi.nlm.nih.gov/17129979/) | Yersinia-KD: ↑coronary lesions (52.4% vs 31.8%, p=0.001), IVIG resistance |
| [34108299](https://pubmed.ncbi.nlm.nih.gov/34108299/) | Anti-YPM antibody serology confirms infection; intussusception + incomplete KD |
| [16366361](https://pubmed.ncbi.nlm.nih.gov/16366361/) | KD-criteria case with DIC; anti-YPM serology |
| [39697956](https://pubmed.ncbi.nlm.nih.gov/39697956/) | Refractory KD with Y. pseudotuberculosis treated with cefotaxime |
| [10592892](https://pubmed.ncbi.nlm.nih.gov/10592892/) | Superantigen hypothesis for KD pathogenesis |
| [23852698](https://pubmed.ncbi.nlm.nih.gov/23852698/) | O:1 carrot outbreak: ReA 22% adults, 67% HLA-B27⁺, EN 42% children |
| [12922960](https://pubmed.ncbi.nlm.nih.gov/12922960/) | O:3 outbreak: severe polyarticular ReA, HLA-B27⁺ |
| [7554560](https://pubmed.ncbi.nlm.nih.gov/7554560/) | 10-yr follow-up: chronic arthritis, ankylosing spondylitis, fatal amyloidosis |
| [34628159](https://pubmed.ncbi.nlm.nih.gov/34628159/) | Meta-analysis: Yersinia 65% terminal ileitis, 51% mesenteric adenitis |
| [22228001](https://pubmed.ncbi.nlm.nih.gov/22228001/) | Terminal ileitis mimicking Crohn's in childhood |
| [18368812](https://pubmed.ncbi.nlm.nih.gov/18368812/) | Granulomatous Yersinia pathology resembling Crohn's |
| [26385573](https://pubmed.ncbi.nlm.nih.gov/26385573/) | Histopathologic IBD mimics incl. Yersinia |
| [25576025](https://pubmed.ncbi.nlm.nih.gov/25576025/) | Invasin·β1-integrin → NETs (innate arm) |
| [20148898](https://pubmed.ncbi.nlm.nih.gov/20148898/) | T3SS Yop translocation selectively to phagocytes |
| [18505804](https://pubmed.ncbi.nlm.nih.gov/18505804/) | Attenuated Y. pseudotuberculosis oral vaccine concept |
| [10417137](https://pubmed.ncbi.nlm.nih.gov/10417137/) | HLA-B27 transgenic rat CTL model |
| [42448289](https://pubmed.ncbi.nlm.nih.gov/42448289/) | Fatal septicemia in immunocompromised/iron-overload host |

---

## Limitations and Knowledge Gaps

1. **No dedicated primary data were analyzed** — this is a literature synthesis. Some key sources are non-English (Russian/Japanese) with abstracts unavailable, limiting extraction of quantitative detail (e.g., precise FESLF incidence/prevalence per 100,000, which remains unquantified in the accessible literature).
2. **pVM82 plasmid biology is understudied** — it is a molecular marker of FESLF strains, but its gene content and mechanistic contribution to severity are essentially uncharacterized ([PMID: 30695393](https://pubmed.ncbi.nlm.nih.gov/30695393/)).
3. **Direct in vivo demonstration that YPMa alone reproduces the full FESLF rash/desquamation phenotype is lacking** — most mechanistic data derive from toxic-shock and cytokine models rather than the complete syndrome.
4. **Causality vs. association in Kawasaki disease** — the Yersinia–KD link is strong epidemiologically and serologically, but whether *Y. pseudotuberculosis* is a cause of a KD subset or a mimicker remains debated.
5. **Epidemiologic underreporting** — yersiniosis is under-diagnosed and under-serotyped even in surveillance systems ([PMID: 26233079](https://pubmed.ncbi.nlm.nih.gov/26233079/)), so true FESLF burden in endemic regions is uncertain.
6. **No modern randomized treatment trials** — antibiotic and IVIG recommendations rest on case series and analogy to KD, not RCTs.

---

## Proposed Follow-up Experiments / Actions

1. **Sequence and functionally annotate the pVM82 plasmid** across FESLF vs non-FESLF strains (comparative genomics + isogenic cured-plasmid virulence assays) to test whether pVM82 independently contributes to severity beyond ypmA.
2. **Isogenic ΔypmA vs ypmA⁺ challenge** in a humanized-HLA-DR/Vβ mouse or primate model to formally establish YPMa's necessity/sufficiency for the FESLF phenotype.
3. **Prospective serologic cohort** of KD patients in endemic vs non-endemic regions using standardized anti-YPM assays to quantify the attributable fraction of Yersinia-associated KD and its coronary-outcome risk.
4. **Structure-guided anti-YPM therapeutics**: develop neutralizing monoclonal antibodies or engineered Vβ-decoy proteins based on the jelly-roll fold and the demonstrated protection by anti-YPM/anti-IFN-γ antibodies ([PMID: 15003813](https://pubmed.ncbi.nlm.nih.gov/15003813/)).
5. **HLA-B27 stratified natural-history study** to define reactive-arthritis and amyloidosis risk after *Y. pseudotuberculosis* infection and guide surveillance.
6. **Regional epidemiologic quantification** in the Russian Far East/Japan to populate incidence/prevalence fields (currently unfilled) and map ypmA/pVM82 genotype distribution to case severity.
7. **Update ontology mappings** for the knowledge base: confirm MONDO:0041536 cross-references to MeSH/ICD, and attach the HPO, GO, CL, UBERON, and NCIT terms proposed in Sections 3–12.

---

*Report compiled from 65 reviewed papers and 8 confirmed findings over a 5-iteration autonomous investigation. Evidence types: human clinical (case series, outbreaks, cohorts), model organism (mouse, rat, primate), in vitro (cytokine assays, mutagenesis), and structural/computational (X-ray crystallography, NMR, genomics).*


## Artifacts

- [OpenScientist final report](Far_East_Scarlet_Like_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Far_East_Scarlet_Like_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 46 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 22 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0041536` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Far-East scarlet-like fever**
- `HP:0000202` (1 mention) - the report calls it "Oral cavity abnormality"; HP calls it **Orofacial cleft**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007556` (1 mention) - the report calls it "Palmoplantar desquamation"; HP calls it **Plantar hyperkeratosis**
- `HP:0000206` (1 mention) - the report calls it "Glossitis, related"; HP calls it **Glossitis**
- `GO:0032609` (1 mention) - the report calls it "interferon-gamma production"; GO calls it **type II interferon production**, and lists "interferon-gamma production" among its other names
- `CL:0000624` (1 mention) - the report calls it "CD4⁺ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000625` (1 mention) - the report calls it "CD8⁺ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `CL:0000794` (1 mention) - the report calls it "CD8⁺ cytotoxic T cell"; CL calls it **CD8-positive, alpha-beta cytotoxic T cell**, and lists "cytotoxic T cell" among its other names
- `UBERON:0002116` (1 mention) - the report calls it "Primary:** terminal ileum"; UBERON calls it **ileum**, and lists "intestinum ileum" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Secondary/systemic:** skin"; UBERON calls it **skin of body**, and lists "entire skin" among its other names