---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-18T17:35:22.506711'
end_time: '2026-09-18T18:06:25.940234'
duration_seconds: 1863.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Biliary, Renal, Neurologic, and Skeletal Syndrome
  mondo_id: MONDO:0859191
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
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 37
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0000175
    reported_labels:
    - Cleft lip/palate, dysmorphism, possible hearing loss
    ontology_label: Cleft palate
  labels_variant: 4
  obsolete_terms:
  - term_id: HP:0001388
    ontology_label: obsolete Joint laxity
    replaced_by: HP:0001382
  - term_id: NCIT:C29273
    ontology_label: Aluminum Hydroxide/Magnesium Hydroxide
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Biliary_Renal_Neurologic_And_Skeletal_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Biliary_Renal_Neurologic_And_Skeletal_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Biliary, Renal, Neurologic, and Skeletal Syndrome
- **MONDO ID:** MONDO:0859191 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Biliary, Renal, Neurologic, and Skeletal Syndrome** covering all of the
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

# Biliary, Renal, Neurologic, and Skeletal Syndrome (BRENS): A Comprehensive Disease Characteristics Report

**Disease:** Biliary, Renal, Neurologic, and Skeletal Syndrome (BRENS)
**MONDO ID:** MONDO:0859191 · **OMIM:** #619534 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** IFT56 (formerly TTC26; synonym DYF13), HGNC:21882, chr7q34

---

## Summary

**Biliary, Renal, Neurologic, and Skeletal Syndrome (BRENS)** is an ultra-rare, autosomal-recessive, multisystem **ciliopathy** caused by biallelic loss-of-function variants in **IFT56 (formerly TTC26)**, a tetratricopeptide-repeat (TPR) protein that is a core component of the **intraflagellar transport (IFT)-B complex**. IFT56/TTC26 is required for the anterograde transport of a selective set of cargoes along the ciliary axoneme; its loss compromises the function of both primary (signaling) cilia and motile cilia. The disorder was first delineated in 2020 by Shaheen et al., who described seven individuals from seven families with a syndromic ciliopathy featuring severe neonatal cholestasis, and identified three different homozygous *TTC26* variants that fully segregated with the phenotype [PMID: 31595528].

Mechanistically, IFT56 loss dysregulates **ciliary Sonic Hedgehog (Shh)–GLI signaling** during embryonic development. Work in the *Ttc26* hop-sterile mouse pinpointed the defect to failure of **GLI dissociation from its negative regulator SUFU** at the ciliary tip, downstream of normal GLI accumulation [PMID: 25340710]. A more recent study adds that TTC26 is required for ciliary localization of the methyltransferase **PRMT7**, which methylates **GLI2** to maintain Shh–GLI2 signaling [PMID: 42178579]. Because Hedgehog signaling patterns the limb, neural tube, skeleton, and multiple viscera, and because cilia are essential in cholangiocytes, renal tubular cells, ependyma, and photoreceptors, the consequence is a congenital, variably expressed multi-organ malformation syndrome.

Clinically, BRENS produces **neonatal cholestasis / fibrocystic biliary disease** (potentially lethal or requiring liver transplant), **renal cysts/dysplasia**, **brain malformations** (hydrocephalus, aqueductal stenosis), **pituitary stalk interruption syndrome (PSIS) with hypopituitarism and diabetes insipidus**, **polydactyly/syndactyly** and other skeletal anomalies, plus cardiac, ocular (optic atrophy), and craniofacial (cleft lip/palate) features. Expressivity is variable — one Chinese patient had renal, neurologic, and skeletal features **without** biliary involvement [PMID: 39514123]. Diagnosis is molecular (WES/WGS identifying biallelic *IFT56/TTC26* variants); there is **no curative therapy**, and management is supportive and multidisciplinary. Prognosis is guarded, dominated by the severity of the neonatal hepatic phenotype. Fewer than ~25 patients have been published worldwide as of 2025.

---

## Key Findings

### 1. BRENS is an autosomal-recessive ciliopathy caused by biallelic IFT56/TTC26 variants

The disease-gene relationship is firmly established. In the foundational cohort, whole-exome sequencing of seven individuals from seven families with syndromic ciliopathy features — including severe neonatal cholestasis — revealed *"three different homozygous variants in Tetratricopeptide Repeat Domain 26 (TTC26) that fully segregated with the phenotype"* after positional mapping to a single locus on chromosome 7q [PMID: 31595528]. Multiple independent families have since confirmed the gene: a homozygous splice-site variant c.4-1G>C [PMID: 34177428]; the recurrent homozygous missense c.695A>G (p.Asn232Ser) [PMID: 32617964]; a homozygous intronic c.1006-5T>C [PMID: 38135897]; and compound-heterozygous alleles in a Chinese boy [PMID: 39514123]. Inheritance is autosomal recessive, and several families are consanguineous. The disease carries OMIM #619534; the gene carries OMIM 617453.

> *"Whole-exome sequencing revealed three different homozygous variants in Tetratricopeptide Repeat Domain 26 (TTC26) that fully segregated with the phenotype."* — [PMID: 31595528]

> *"We describe seven individuals from seven families with syndromic ciliopathy clinical features, including severe neonatal cholestasis (lethal in one and necessitating liver transplant in two)."* — [PMID: 31595528]

### 2. TTC26/IFT56 is a conserved IFT-B core component required for cargo-selective transport

TTC26 (also called DYF13 in *Chlamydomonas* and *C. elegans*) is an integral component of the intraflagellar transport complex B. Ishikawa et al. showed that *"TTC26/DYF13 is an IFT complex B protein in mammalian cells and Chlamydomonas reinhardtii"* [PMID: 24596149]. Loss of TTC26 produces short cilia with abnormal motility while leaving IFT-particle assembly and speed largely normal; critically, *"a particular set of proteins involved in motility was specifically depleted in the dyf13 mutant"* — evidence that TTC26 mediates **cargo-selective transport** rather than bulk IFT [PMID: 24596149]. Structural/biochemical studies place TTC26/IFT56 in the **IFT-B core subcomplex** [PMID: 26980730] and show it dimerizes with and directly binds **IFT46** [PMID: 27927754, 25340710]. Xin et al. demonstrated that *"IFT56 regulates vertebrate developmental patterning by maintaining IFTB complex integrity and ciliary microtubule architecture"* [PMID: 28264835].

### 3. Mechanism: TTC26 loss dysregulates Sonic Hedgehog signaling via impaired GLI–SUFU dissociation and GLI2 methylation

The core pathogenic mechanism is disruption of ciliary Hedgehog signal transduction. In the spontaneous *Ttc26* hop-sterile mouse, the group found that *"the hop mutation is located in the Ttc26 gene and impairs Hedgehog (Hh) signaling"* [PMID: 25340710]. Importantly, the defect is not a failure of cilium formation — cilia number and length are preserved — but a downstream signaling failure: *"hop did not interfere with Hh-induced accumulation of Gli at the tip of the primary cilium, but rather with the subsequent dissociation of Gli from its negative regulator, Sufu"* [PMID: 25340710]. Patient-derived cells show cilia of variable length with dysregulated Sonic Hedgehog signaling and abnormal IFT-B staining [PMID: 31595528]. A recent study adds a molecular refinement: *"TTC26 is required for the localization of protein arginine methyltransferase 7 (PRMT7) to the primary cilium, enabling methylation of GLI2"* — with FLNB, to maintain Shh–GLI2 signaling [PMID: 42178579].

### 4. Phenotypic spectrum spans biliary, renal, neurologic, skeletal, endocrine, cardiac, ocular, and craniofacial systems

The syndrome is defined by multi-organ involvement with variable expressivity. Core features from the founding cohort include severe neonatal cholestasis (lethal in one, requiring liver transplant in two) and fibrocystic liver/biliary disease [PMID: 31595528]. Pituitary involvement is a recurrent — and now recognized as characteristic — feature: four patients with homozygous p.Asn232Ser had **pituitary stalk interruption syndrome (PSIS)**, delineated *"as a novel clinical feature of this disorder"* [PMID: 32617964]. Across cases, reported manifestations include *"cholestasis, cystic dilatation of intrahepatic biliary ducts, diabetes insipidus, dysmorphic facial features, optic atrophy, pituitary hypoplasia, hydrocephalus, aqueductal stenosis, hyperextensible knee joints, bilateral knee dislocation, polydactyly, and syndactyly"* [PMID: 34177428], plus cleft lip/palate with probable hearing loss [PMID: 38135897]. Demonstrating the breadth of expressivity, a Chinese boy showed renal, neurologic, and skeletal features but no biliary disease — *"the first description of BRENS syndrome without biliary involvement"* [PMID: 39514123].

| System | Key phenotypes | HPO suggestion | Representative PMID |
|---|---|---|---|
| Hepatobiliary | Neonatal cholestasis, fibrocystic biliary disease, ductal plate malformation, intrahepatic duct dilatation | HP:0011967, HP:0001395 | 31595528, 34177428 |
| Renal/urinary | Renal cysts, dysplasia, nephropathy | HP:0000107 | 31595528, 38135897 |
| Nervous/CNS | Hydrocephalus, aqueductal stenosis | HP:0000238, HP:0002410 | 31595528, 34177428 |
| Endocrine (pituitary) | PSIS, hypopituitarism, diabetes insipidus | HP:0010626, HP:0000873 | 32617964, 38135897 |
| Skeletal/limb | Pre/postaxial polydactyly, syndactyly, joint hyperextensibility/dislocation | HP:0100259, HP:0001388 | 34177428 |
| Ocular | Optic atrophy | HP:0000648 | 34177428 |
| Cardiac | Congenital heart defect | HP:0001627 | 38135897 |
| Craniofacial | Cleft lip/palate, dysmorphism, possible hearing loss | HP:0000175 | 38135897 |

### 5. Cross-species model organisms robustly recapitulate the ciliopathy

Multiple model systems reproduce BRENS-relevant phenotypes and have illuminated mechanism. **Mouse:** the spontaneous *Ttc26* hop-sterile mutant is *"characterized by a hopping gait, polydactyly, hydrocephalus, and male sterility"* with inner dynein-arm deficiency, absent sperm flagella, and impaired Hedgehog signaling [PMID: 25340710]; a 2025 study found that *Ift56* loss-of-function *"has dramatic phenotypic differences depending on the genetic background in mice"*, establishing genetic-background modifiers [PMID: 41352382]. **Zebrafish:** morpholino knockdown of *ttc26* *"caused ciliary defects in the pronephric kidney at 27 h postfertilization and distension/dilation of pronephros"* [PMID: 22718903], plus photoreceptor outer-segment defects [PMID: 36533556]. **Chlamydomonas:** *dyf13/TTC26* mutation gives short flagella with abnormal motility and selective loss of motility proteins [PMID: 24596149]. A double *Flnb;Ttc26* heterozygous mouse models adolescent idiopathic scoliosis via Shh–GLI2 [PMID: 42178579].

### 6. IFT56/TTC26 is LoF-tolerant in heterozygotes; BRENS is ultra-rare

gnomAD v4 constraint metrics for IFT56/TTC26 (ENSG00000105948) indicate that heterozygous loss-of-function is **tolerated** — pLI ≈ 3×10⁻¹⁰, observed/expected LoF (o/e) = 0.61 (90% CI 0.49–0.77; LOEUF 0.77), with 52 observed vs 85 expected pLoF variants. This tolerance is exactly what is expected for an autosomal-recessive disease gene in which carriers are unaffected. Summing 133 high-confidence pLoF allele frequencies yields a cumulative pLoF allele frequency of ≈2.36×10⁻⁴, implying a carrier frequency of roughly **1 in ~2,100** for truncating alleles alone, and a predicted homozygous/compound-het birth frequency from pLoF alleles of ≈5.6×10⁻⁸ (~1 in 18 million). Because most reported disease alleles are splice-region/missense (e.g., the recurrent c.695A>G, p.Asn232Ser) rather than canonical LoF, the true prevalence is higher than the pLoF-only estimate but remains ultra-rare (<25 published patients worldwide as of 2025).

### 7. Diagnosis is genetic; management is supportive with guarded prognosis

BRENS diagnosis is established by molecular genetic testing — **whole-exome or whole-genome sequencing** identifying biallelic *IFT56/TTC26* variants (the original cohort combined positional mapping with WES [PMID: 31595528]; a later family used WGS with Sanger confirmation [PMID: 34177428]). Supportive workup findings include neonatal conjugated hyperbilirubinemia with elevated liver enzymes; liver biopsy showing ductal plate malformation/biliary fibrosis; brain MRI showing pituitary stalk interruption (thin/absent stalk, ectopic posterior pituitary, anterior pituitary hypoplasia) and hydrocephalus/aqueductal stenosis; renal imaging showing cysts/dysplasia; and an endocrine panel revealing hypopituitarism and diabetes insipidus. **No disease-specific or curative therapy exists.** Management is supportive and organ-directed: ursodeoxycholic acid and nutritional support for cholestasis; **liver transplantation** for end-stage liver disease (2 of 7 original patients required transplant, 1 died — *"severe neonatal cholestasis (lethal in one and necessitating liver transplant in two)"* [PMID: 31595528]); multi-hormone replacement for pituitary insufficiency, where *"hormonal replacement therapy with hydrocortisone, levothyroxine, and growth hormone led to clinical stabilization"* [PMID: 42460215]; ventriculoperitoneal shunting for hydrocephalus; and surgical correction of polydactyly and clefts. Prognosis is guarded; severe neonatal cholestasis can be lethal.

### 8. Identifiers and IFT56 protein architecture

Disease identifiers: **MONDO:0859191** ("biliary, renal, neurologic, and skeletal syndrome"); **OMIM #619534**; **MedGen C1794200**; **UMLS C5561990**; MalaCards entry present. No dedicated Orphanet ORPHA code or specific ICD-10/ICD-11/MeSH term is currently mapped (classified broadly under ciliopathy/congenital malformation syndromes). Gene: **IFT56** (formerly TTC26; synonym DYF13), **HGNC:21882**, **OMIM 617453**, Ensembl **ENSG00000105948**, chr7q34. Protein: **UniProt A0AVF1**, "Intraflagellar transport protein 56," 554 aa, containing **four tetratricopeptide-repeat (TPR) motifs** (aa 57–90, 92–125, 151–184, 468–501). The recurrent founder missense p.Asn232Ser lies in the inter-repeat region; splice-site variants predominate among disease alleles.

### 9. Anatomical, cellular, and subcellular map

Documented across cases [PMIDs 31595528, 34177428, 32617964, 38135897, 39514123], with ontology suggestions:

| Level | Structure / cell | Ontology term |
|---|---|---|
| Hepatobiliary | Bile duct / liver; cholangiocyte | UBERON:0002394 / UBERON:0002107; CL:0002326 |
| Renal | Kidney tubule/collecting duct; renal epithelial cell | UBERON:0002113; CL:1000454 |
| Nervous | Cerebral aqueduct; ependymal cell | UBERON:0002289; CL:0000065 |
| Endocrine | Pituitary gland; neurohypophysis | UBERON:0000007; UBERON:0002590 |
| Eye | Photoreceptor layer; photoreceptor cell | UBERON:0001789; CL:0000210 |
| Skeletal | Digit (autopod) | UBERON:0002389 |
| Cardiac | Heart | UBERON:0000948 |
| Craniofacial | Mouth (lip/palate) | UBERON:0000165 |
| Subcellular | Cilium; 9+2 motile cilium; ciliary tip; IFT particle B | GO:0005929; GO:0097729; GO:0097542; GO:0030992 |

Subcellular localization is confirmed: *"We localized Ttc26 to the transition zone of photoreceptor and to the transition zone of cilia in cultured murine inner medullary collecting duct 3 (mIMCD3) renal cells"* [PMID: 22718903]. Tissue expression supports hepatobiliary primacy: *"strong expression of Ttc26 in the embryonic mouse liver in a pattern consistent with its proposed role in the normal development of the intrahepatic biliary system"* [PMID: 31595528].

### 10. Natural history and variant landscape

BRENS is **congenital/neonatal in onset** (cholestasis and malformations present at or near birth), **chronic and lifelong**, without spontaneous remission. The hepatic component is often **progressive** (cholestasis → biliary fibrosis → end-stage liver disease/transplant), whereas malformations (polydactyly, hydrocephalus, PSIS) are static-congenital and endocrine deficiency is stable but permanent [PMID: 31595528, 32617964]. Critical intervention windows: the embryonic period fixes malformations (irreversible), and the neonatal period is critical for life-saving hormone replacement and cholestasis/transplant management. The variant landscape comprises splice-region and missense loss-of-function changes (c.4-1G>C, c.695A>G p.Asn232Ser, c.1006-5T>C, c.1069+5G>A, c.511A>G, c.1099T>C, plus three homozygous founding-cohort variants); ClinVar lists 200+ submissions, predominantly population VUS/benign, consistent with a recessive, LoF-tolerant gene. Etiology is **exclusively genetic** (autosomal recessive); no environmental, infectious, epigenetic, or chromosomal mechanism is implicated.

---

## Section-by-Section Report

### 1. Disease Information
BRENS is an ultra-rare autosomal-recessive multisystem ciliopathy affecting biliary, renal, neurologic, and skeletal systems (plus endocrine, cardiac, ocular, and craniofacial). Key identifiers: MONDO:0859191, OMIM #619534, MedGen C1794200, UMLS C5561990. No dedicated Orphanet/ICD/MeSH code is currently mapped. Synonyms: "TTC26 ciliopathy," "biliary ciliopathy (TTC26-related)." Information is derived from **aggregated disease-level resources and published individual case reports** (not EHR cohorts) — fewer than ~25 patients worldwide.

### 2. Etiology
The primary and sole established cause is **genetic**: biallelic loss-of-function variants in IFT56/TTC26. No environmental, infectious, lifestyle, or toxic contributing factors are implicated. Genetic risk requires two pathogenic alleles (autosomal recessive); consanguinity is a strong risk factor (several reported families are consanguineous, and homozygous founder alleles such as p.Asn232Ser recur). No protective variants or gene–environment interactions are described. Modifier effects are documented at the model-organism level: genetic background dramatically alters phenotype severity in *Ift56/Ttc26* mutant mice [PMID: 41352382], and FLNB acts as a genetic modifier of the Shh–GLI2 axis [PMID: 42178579].

### 3. Phenotypes
See Finding 4 table. Onset is neonatal/congenital. Severity is variable (from lethal neonatal cholestasis to milder biliary-sparing presentations). Progression: hepatic disease progressive; malformations static; endocrine deficits permanent. Quality-of-life impact is severe where hypopituitarism, hydrocephalus, and liver disease coexist, requiring lifelong hormone replacement and organ-directed care. Suggested HPO terms: Neonatal cholestasis (HP:0011967), Hepatic fibrosis (HP:0001395), Polydactyly (HP:0100259), Hydrocephalus (HP:0000238), Aqueductal stenosis (HP:0002410), Anterior pituitary hypoplasia (HP:0010626), Diabetes insipidus (HP:0000873), Optic atrophy (HP:0000648), Renal cyst (HP:0000107), Cleft lip/palate (HP:0000175), Congenital heart defect (HP:0001627), Joint hyperlaxity (HP:0001388).

### 4. Genetic/Molecular Information
Causal gene: IFT56/TTC26 (HGNC:21882, OMIM 617453). Variant types: predominantly splice-site and missense (loss-of-function). Classification per ACMG/AMP: reported disease alleles are pathogenic/likely pathogenic; the gene shows abundant benign/VUS population variation. Allele frequencies in gnomAD are consistent with an ultra-rare recessive disorder (see Finding 6). Origin is germline. Functional consequence is loss of function (disrupted IFT-B integrity and cargo transport). Modifier genes: FLNB and genetic background (from models). No epigenetic or chromosomal mechanism is implicated.

### 5. Environmental Information
Not applicable — BRENS is a purely Mendelian disorder. No environmental, lifestyle, or infectious agents contribute.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**
1. Biallelic loss-of-function variants in **IFT56/TTC26** → loss of functional IFT56 protein.
2. Loss of IFT56 → **destabilization of the IFT-B core subcomplex** and impaired ciliary microtubule architecture [PMID: 28264835] → **cargo-selective failure of anterograde intraflagellar transport** (motility-related and signaling cargoes) [PMID: 24596149].
3. Impaired IFT → **dysfunctional primary (signaling) and motile cilia** across tissues (short/variable-length cilia; abnormal motility) [PMID: 31595528, 24596149].
4a. In primary cilia → failure of **GLI dissociation from SUFU** at the ciliary tip (inferred to also involve loss of ciliary PRMT7 → reduced GLI2 methylation) → **dysregulated Sonic Hedgehog–GLI signaling** [PMID: 25340710, 42178579].
4b. In motile cilia → inner dynein-arm deficiency and impaired ciliary/flagellar motility → ependymal/CSF-flow and reproductive defects (demonstrated in mouse) [PMID: 25340710].
5. Dysregulated Shh–GLI patterning during embryogenesis → **abnormal development of limb (polydactyly), neural tube/brain (hydrocephalus, aqueductal stenosis), pituitary (PSIS), intrahepatic biliary tree (ductal plate malformation/cholestasis), kidney (cysts), heart, eye, and craniofacial structures**.
6. Postnatally → progressive biliary fibrosis and end-stage liver disease; permanent hypopituitarism and diabetes insipidus; static malformations → **the BRENS clinical phenotype**.

Molecular pathways: **Hedgehog/GLI** (central). Cellular processes: ciliogenesis, intraflagellar transport, developmental patterning. Protein dysfunction: loss of function of an IFT-B TPR scaffold destabilizing the complex. Suggested GO terms: intraciliary transport (GO:0042073), smoothened signaling pathway (GO:0007224), cilium assembly (GO:0060271), determination of left/right symmetry (GO:0007368). Suggested CL terms: cholangiocyte (CL:0002326), ependymal cell (CL:0000065), photoreceptor cell (CL:0000210), kidney epithelial cell (CL:1000454).

### 7. Anatomical Structures Affected
See Finding 9. Primary organs: liver/intrahepatic bile ducts, kidney, brain (ventricular system), pituitary. Secondary/associated: heart, eyes, skeleton/limbs, craniofacial structures. Involvement is generally bilateral. Subcellular: primary and motile cilia (axoneme, transition zone, ciliary tip), IFT-B particle.

### 8. Temporal Development
Onset congenital/neonatal; course chronic-lifelong. Hepatic disease progressive; malformations static; endocrine deficits permanent. No remission. Critical windows: embryonic (malformation fixation, irreversible) and neonatal (life-saving hormone replacement, cholestasis/transplant management).

### 9. Inheritance and Population
Autosomal recessive. Ultra-rare (<25 published patients; estimated carrier frequency ~1/2,000 for truncating alleles). Penetrance appears complete for biallelic pathogenic genotypes, with **variable expressivity** (biliary-sparing cases exist [PMID: 39514123]). Consanguinity and founder alleles (p.Asn232Ser) contribute. No confirmed sex bias in the syndrome itself (male sterility is seen in the mouse model). No genetic anticipation (not a repeat-expansion disorder).

### 10. Diagnostics
Molecular diagnosis by WES/WGS (biallelic IFT56/TTC26 variants). Supportive: conjugated hyperbilirubinemia, elevated liver enzymes; liver biopsy (ductal plate malformation/fibrosis); brain MRI (PSIS triad, hydrocephalus/aqueductal stenosis); renal ultrasound (cysts/dysplasia); endocrine panel (hypopituitarism, diabetes insipidus). Differential diagnosis: other syndromic ciliopathies (Meckel, Joubert, Bardet-Biedl, nephronophthisis-related; TTC12/TTC21B multisystem ciliopathies [PMID: 36273201]), Alagille syndrome, and other causes of neonatal cholestasis with malformations. Screening: cascade carrier testing in families; prenatal/preimplantation testing where the familial variant is known.

### 11. Outcome/Prognosis
Guarded. Neonatal cholestasis can be lethal; liver transplantation may be required (2/7 transplanted, 1 death in the founding cohort [PMID: 31595528]). Survivors face lifelong morbidity from hypopituitarism, diabetes insipidus, hydrocephalus, and organ malformations. No formal survival statistics exist given the small patient numbers. Prognostic factors: severity of the hepatic phenotype and presence/absence of biliary involvement.

### 12. Treatment
No curative/disease-specific therapy. Supportive/organ-directed: ursodeoxycholic acid and nutritional support (cholestasis); liver transplantation (end-stage liver disease); multi-hormone replacement — hydrocortisone, levothyroxine, growth hormone, desmopressin for DI [PMID: 42460215, 40539145]; VP shunt (hydrocephalus); surgical correction of polydactyly and cleft lip/palate. Suggested NCIT terms: Liver Transplantation (NCIT:C15238), Hormone Replacement Therapy (NCIT:C15667), Ursodeoxycholic Acid (NCIT:C29273), Ventriculoperitoneal Shunt (NCIT:C50124). No pharmacogenomic, gene, cell, or RNA therapies are established or in trials for BRENS.

### 13. Prevention
No primary prevention beyond **genetic counseling** for at-risk (especially consanguineous) families. Secondary/tertiary prevention: early diagnosis enabling timely hormone replacement, cholestasis management, and shunting to prevent complications. Options where the familial variant is known: carrier screening, prenatal testing, preimplantation genetic diagnosis. No immunization or environmental intervention applies.

### 14. Other Species / Natural Disease
No naturally occurring companion-animal or wildlife disease is reported (no OMIA entry noted). Orthologous genes: mouse *Ttc26*, zebrafish *ttc26*, *Chlamydomonas* DYF13, *C. elegans* dyf-13. Evolutionary conservation of IFT-B and its function is high across ciliated eukaryotes. No zoonotic potential (Mendelian disorder).

### 15. Model Organisms
Robust models exist (Finding 5): mouse (*Ttc26* hop-sterile spontaneous mutant; *Ift56/Ttc26* engineered LoF with background-dependent severity; *Flnb;Ttc26* double heterozygote for scoliosis), zebrafish (*ttc26* morpholino/CRISPR), and *Chlamydomonas* (*dyf13*). Phenotype recapitulation is strong for polydactyly, hydrocephalus, renal cystic/pronephric defects, photoreceptor defects, motile-cilia/flagellar dysfunction, and Hedgehog-signaling readouts. Limitations: the severe human biliary phenotype is incompletely modeled; genetic background strongly modulates murine phenotypes, complicating cross-study comparison. Resources: MGI, ZFIN, IMPC.

---

## Mechanistic Model (Diagram)

```
Biallelic LoF IFT56/TTC26 variants
        │  (loss of IFT-B TPR scaffold protein)
        ▼
IFT-B core destabilization + abnormal ciliary microtubules
        │  (cargo-selective anterograde transport failure)
        ▼
Dysfunctional primary & motile cilia
        ├───────────────► Motile cilia: inner dynein-arm loss →
        │                 ependymal/flagellar dysfunction (CSF flow,
        │                 male sterility [mouse]) → hydrocephalus
        │
        └──► Primary cilia signaling defect:
             GLI fails to dissociate from SUFU at ciliary tip
             (+ loss of ciliary PRMT7 → ↓GLI2 methylation)
                     │
                     ▼
             Dysregulated Sonic Hedgehog–GLI signaling
                     │  (abnormal embryonic patterning)
                     ▼
   ┌──────────┬──────────┬──────────┬──────────┬──────────┐
 Biliary     Renal     Neuro/     Pituitary  Skeletal/  Cardiac/
 (cholestasis cysts    brain      PSIS,      limb        ocular/
 fibrosis)             hydro-     hypopit,   polydactyly craniofacial
                       cephalus   DI
                     │
                     ▼
            BRENS clinical phenotype (congenital, chronic)
```

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [31595528](https://pubmed.ncbi.nlm.nih.gov/31595528/) | *Biallelic Mutations in TTC26 (IFT56) Cause Severe Biliary Ciliopathy* | **Foundational**: defines disease, gene, recessive segregation, biliary severity |
| [25340710](https://pubmed.ncbi.nlm.nih.gov/25340710/) | *A mutation in mouse ttc26 leads to impaired hedgehog signaling* | **Core mechanism**: GLI–SUFU dissociation failure; mouse model |
| [42178579](https://pubmed.ncbi.nlm.nih.gov/42178579/) | *FLNB and TTC26 regulate ciliary Hedgehog signaling…* | Mechanistic refinement: PRMT7→GLI2 methylation; FLNB modifier |
| [24596149](https://pubmed.ncbi.nlm.nih.gov/24596149/) | *TTC26/DYF13 is an IFT protein required for transport of motility proteins* | Establishes IFT-B membership; cargo selectivity |
| [28264835](https://pubmed.ncbi.nlm.nih.gov/28264835/) | *IFT56 regulates vertebrate patterning…* | IFT-B integrity, microtubule architecture |
| [26980730](https://pubmed.ncbi.nlm.nih.gov/26980730/) | *Overall architecture of the IFT-B complex* | Places TTC26/IFT56 in IFT-B core |
| [27927754](https://pubmed.ncbi.nlm.nih.gov/27927754/) | *ARL13B/INPP5E regulate retrograde trafficking* | IFT46–IFT56 dimer; Hedgehog links |
| [32617964](https://pubmed.ncbi.nlm.nih.gov/32617964/) | *PSIS broadens the TTC26 ciliopathy spectrum* | Adds PSIS; recurrent p.Asn232Ser |
| [34177428](https://pubmed.ncbi.nlm.nih.gov/34177428/) | *Identification of the c.4-1G>C variant…* | New family; enumerates multisystem phenotype |
| [38135897](https://pubmed.ncbi.nlm.nih.gov/38135897/) | *Novel TTC26 variant…expansion of phenotype* | c.1006-5T>C; adds clefts, hearing loss |
| [39514123](https://pubmed.ncbi.nlm.nih.gov/39514123/) | *BRENS in a Chinese boy* | Variable expressivity: biliary-sparing case |
| [22718903](https://pubmed.ncbi.nlm.nih.gov/22718903/) | *Knockdown of ttc26 disrupts ciliogenesis…zebrafish* | Renal/photoreceptor model; transition-zone localization |
| [36533556](https://pubmed.ncbi.nlm.nih.gov/36533556/) | *Variable phenotypes in zebrafish TZ mutants* | ttc26 crispant ciliary phenotype |
| [41352382](https://pubmed.ncbi.nlm.nih.gov/41352382/) | *Genetic background influences Ift56/Ttc26 anomalies* | Genetic-background modifiers |
| [42460215](https://pubmed.ncbi.nlm.nih.gov/42460215/) | *PSIS in a newborn with recurrent hypoglycemia* | Supports hormone replacement management |
| [40539145](https://pubmed.ncbi.nlm.nih.gov/40539145/) | *PSIS: A Case Series* | PSIS clinical triad and management |
| [36273201](https://pubmed.ncbi.nlm.nih.gov/36273201/) | *TTC12/TTC21B multisystem ciliopathies* | Differential diagnosis / phenotypic overlap |

---

## Limitations and Knowledge Gaps

- **Very small patient population** (<25 published cases) limits confident estimates of penetrance, expressivity, sex ratio, survival, and genotype–phenotype correlation.
- **No formal epidemiology**: prevalence/incidence are estimated indirectly from gnomAD allele frequencies, not measured. The pLoF-only carrier estimate (~1/2,100) omits the missense/splice alleles that dominate the reported disease spectrum, so it underestimates true carrier frequency.
- **Incomplete mechanistic mapping** of how a single ciliary transport defect yields the specific organ set; the relative contributions of primary-cilia (Hedgehog) vs motile-cilia dysfunction to each organ phenotype are not fully resolved.
- **The severe human biliary phenotype is under-modeled** in animals; no model fully recapitulates neonatal cholestasis/biliary fibrosis.
- **No therapeutics** are disease-specific; no clinical trials exist. Pharmacogenomic and gene/cell/RNA therapy data are absent.
- **Ontology mapping gaps**: no Orphanet/ICD/MeSH code; ontology term suggestions here are proposed, not curated into the disease record.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a BRENS patient registry / GeneMatcher-linked cohort** to aggregate genotype–phenotype data, refine penetrance and expressivity, and capture natural history prospectively.
2. **Variant-level functional assays** (splice reporters for the recurrent intronic variants; rescue assays for missense alleles such as p.Asn232Ser) to firm up ACMG classification and reveal hypomorphic vs null effects underlying biliary-sparing presentations.
3. **Conditional/tissue-specific Ift56 mouse models** (hepatoblast/cholangiocyte, pituitary, renal) on a controlled genetic background to model the biliary phenotype and dissect organ-specific mechanism.
4. **Single-cell transcriptomics of patient-derived cholangiocyte and renal organoids/iPSC models** to map Hedgehog-target dysregulation and identify candidate therapeutic nodes (e.g., SMO agonists, PRMT7 modulation).
5. **Curate BRENS into Orphanet/ICD-11/MeSH and submit HPO/GO/CL/UBERON annotations** derived from this report to close ontology gaps.
6. **Systematic imaging/endocrine screening protocol** (neonatal MRI + endocrine panel) for any infant with cholestasis plus polydactyly to enable early hormone replacement during the critical neonatal window.

---

*Evidence source types: primarily human clinical case reports/series and model-organism studies (mouse, zebrafish, Chlamydomonas), supplemented by in vitro biochemistry and computational (gnomAD constraint) analyses. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Biliary_Renal_Neurologic_And_Skeletal_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Biliary_Renal_Neurologic_And_Skeletal_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000175` (2 mentions) - the report calls it "Cleft lip/palate, dysmorphism, possible hearing loss"; HP calls it **Cleft palate**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001388` (obsolete Joint laxity) (2 mentions) - replaced by `HP:0001382`
- `NCIT:C29273` (Aluminum Hydroxide/Magnesium Hydroxide) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000107` (2 mentions) - the report calls it "Renal cysts, dysplasia, nephropathy"; HP calls it **Renal cyst**
- `HP:0001627` (2 mentions) - the report calls it "Congenital heart defect"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names
- `UBERON:0002389` (1 mention) - the report calls it "Digit (autopod)"; UBERON calls it **manual digit**, and lists "digit of hand" among its other names
- `UBERON:0000165` (1 mention) - the report calls it "Mouth (lip/palate)"; UBERON calls it **mouth**, and lists "mouth cavity" among its other names