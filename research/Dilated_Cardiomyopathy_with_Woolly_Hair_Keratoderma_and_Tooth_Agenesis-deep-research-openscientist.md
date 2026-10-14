---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-12T14:48:25.529573'
end_time: '2026-10-12T15:06:46.251184'
duration_seconds: 1100.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy with Woolly Hair, Keratoderma, and Tooth Agenesis
  mondo_id: MONDO:0014355
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
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 23
  validator_version: 0.3.0
term_validation:
  total_terms: 26
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0000982
    reported_labels:
    - Skin sign
    ontology_label: Palmoplantar keratoderma
  - term_id: HP:0001635
    reported_labels:
    - Clinical sign
    ontology_label: Congestive heart failure
  - term_id: GO:0060215
    reported_labels:
    - fat cell differentiation
    ontology_label: primitive hemopoiesis
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Dilated_Cardiomyopathy_with_Woolly_Hair_Keratoderma_and_Tooth_Agenesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Dilated_Cardiomyopathy_with_Woolly_Hair_Keratoderma_and_Tooth_Agenesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy with Woolly Hair, Keratoderma, and Tooth Agenesis
- **MONDO ID:** MONDO:0014355 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy with Woolly Hair, Keratoderma, and Tooth Agenesis** covering all of the
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

# Dilated Cardiomyopathy with Woolly Hair, Keratoderma, and Tooth Agenesis: A Comprehensive Disease Report

**Disease:** Dilated Cardiomyopathy with Woolly Hair, Keratoderma, and Tooth Agenesis
**MONDO ID:** MONDO:0014355 | **OMIM:** #615821 | **Category:** Mendelian (desmosomal cardiocutaneous syndrome)
**Causal gene:** *DSP* (desmoplakin), HGNC:3052, chromosome 6p24.3

---

## Summary

Dilated Cardiomyopathy with Woolly Hair, Keratoderma, and Tooth Agenesis is a rare Mendelian **cardiocutaneous syndrome** caused by pathogenic variants in **DSP**, the gene encoding **desmoplakin**, the principal obligate plaque protein of the desmosome. It sits on the **Carvajal/Naxos desmosomal-disease spectrum** and is distinguished from "classic" arrhythmogenic right ventricular cardiomyopathy (ARVC) by its characteristic ectodermal triad — congenital **woolly hair**, **palmoplantar keratoderma (PPK)**, and, in the variant that defines this entry, **hypodontia/oligodontia (tooth agenesis)** — combined with a **left-dominant or biventricular dilated cardiomyopathy** that manifests in childhood and carries a high burden of ventricular arrhythmia and sudden cardiac death.

The unifying molecular mechanism is a **failure of intermediate-filament anchoring at the desmosome**. Desmoplakin normally links the desmosomal cadherin–plakoglobin–plakophilin plaque to keratin filaments (in epithelia) and desmin filaments (in cardiomyocytes). When DSP is truncated or its C-terminal filament-binding tail is lost, two consequences follow: (1) mechanical junctions fail in tissues subject to shear stress — skin, hair, and heart; and (2) the armadillo protein **plakoglobin** relocates to the nucleus, where it **suppresses canonical Wnt/β-catenin signaling** roughly two-fold through Tcf/Lef1. In the heart, this reprograms **second-heart-field cardiac progenitors** toward adipogenic/fibrogenic fates, producing the fibrofatty myocardial replacement, chamber dilation, electrical instability, and progressive heart failure that dominate prognosis. The dental and ectodermal branch is best explained by the same Wnt deficit: independent human genetics shows that mutations in the canonical Wnt ligand **WNT10A** reproduce the identical triad of tooth agenesis, palmoplantar keratoderma, and hair defects, supporting a shared Wnt/β-catenin basis for the appendageal phenotype (though direct demonstration in DSP-mutant dental epithelium is still lacking).

Inheritance is predominantly **autosomal recessive** (biallelic C-terminal DSP truncations, the configuration first described in three Ecuadorian families in 2000), but heterozygous (dominant) DSP variants cause an allelic, later-onset, left-dominant "DSP cardiomyopathy" with milder or absent cutaneous findings. Cardiac penetrance in the recessive syndrome approaches **100% by adolescence**. Management is entirely organ-directed and supportive — heart-failure pharmacotherapy, antiarrhythmics, implantable cardioverter-defibrillators (ICDs) for sudden-death prevention, exercise restriction, and cardiac transplantation — with no disease-specific cure; EGFR inhibition is an emerging experimental concept for the cutaneous phenotype. This report synthesizes nine confirmed findings drawn from 45 reviewed papers into a complete characterization across all requested domains.

---

## Key Findings

### Finding 1 — DSP mutations cause the full triad of DCM + woolly hair + keratoderma + tooth agenesis

The defining genetic cause of this syndrome is mutation in **DSP (desmoplakin)**. Chalabreysse et al. identified a *de novo* DSP missense mutation **c.1790C>T, p.Ser597Leu** — altering a serine conserved in all vertebrates and absent from 100 controls — in a family presenting woolly hair, palmoplantar keratoderma, biventricular dilated cardiomyopathy, **and** hypo/oligodontia (absent second premolars, second/third molars; 1–15 missing teeth), with no mutation in plakoglobin (*JUP*) [PMID: 20940358]. This is the finding that specifically ties **tooth agenesis** into the DSP cardiocutaneous phenotype, framing it as a "Carvajal/Naxos variant with hypo/oligodontia."

> *"Mutation screening in the desmoplakin gene (DSP) revealed a de novo missense mutation (c.1790 C>T, p.Ser597Leu) changing a serine residue conserved in all vertebrates"* [PMID: 20940358]

> *"this study reveals the role of desmosomes in the development of teeth and suggests that other genes encoding proteins of the desmosome could be involved in oligo/hypodontia"* [PMID: 20940358]

Multiple independent reports confirm DSP causation of the syndrome, including a Lebanese Carvajal patient with tooth agenesis [PMID: 26833927], a biventricular DCM case with homozygous c.4297C>T (p.Gln1433*) [PMID: 38433550], and a pediatric Carvajal case [PMID: 21193976].

### Finding 2 — Mechanism: desmoplakin loss → nuclear plakoglobin → suppressed Wnt/β-catenin → fibrofatty myocardium

The central disease mechanism was established by Garcia-Gras et al.: siRNA suppression of desmoplakin in atrial myocytes caused **nuclear localization of plakoglobin** and a **~2-fold reduction in canonical Wnt/β-catenin signaling** through Tcf/Lef1, driving adipogenic and fibrogenic gene expression and accumulation of fat droplets [PMID: 16823493]. Cardiac-restricted *Dsp* deletion was embryonic-lethal when homozygous and, in heterozygotes, caused fibrofatty replacement, apoptosis, cardiac dysfunction, and arrhythmias.

> *"suppression of DP expression leads to nuclear localization of the desmosomal protein plakoglobin and a 2-fold reduction in canonical Wnt/beta-catenin signaling through Tcf/Lef1 transcription factors. The ensuing phenotype is increased expression of adipogenic and fibrogenic genes and accumulation of fat droplets"* [PMID: 16823493]

Lineage tracing showed the excess adipocytes in DSP-deficient hearts derive from **Nkx2.5+/Mef2C+ second-heart-field progenitors**, explaining the regionality of the remodeling [PMID: 19359597].

> *"the majority of adipocytes in the hearts of Nkx2.5- and Mef2C-regulated lineage tracer mice, expressed enhanced yellow fluorescent protein"* [PMID: 19359597]

Endurance exercise accelerates this remodeling: Tg-DSP(R2834H) mice developed RV dilation, fat infiltration, and cytoplasmic aggregates of desmoplakin/plakoglobin/connexin-43 with perturbed GSK3-β/AKT Wnt signaling [PMID: 26545710] — the experimental basis for clinical exercise restriction.

### Finding 3 — Cardiac phenotype is severe and early: biventricular/left-dominant DCM, high arrhythmia burden, pediatric heart failure, sudden death

The cardiomyopathy dominates prognosis and is strikingly severe in childhood. In a cohort of **10 Saudi pediatric patients** (Binfadel et al.), **all** had woolly hair, **all** had severely dilated/depressed LV systolic function, **9/10** had depressed RV function, and **9/10** had frequent PVCs/VT; 3 received an ICD, **4 underwent heart transplantation**, and **3 died suddenly** while awaiting transplant [PMID: 40108711].

> *"four patients underwent heart transplantation, and three died suddenly while waiting for a heart donation"* [PMID: 40108711]

A representative single case: a 7-year-old girl with EF 22%, biventricular dilation, and moderate–severe mitral/tricuspid regurgitation, homozygous for DSP c.4297C>T (p.Gln1433*) [PMID: 38433550]. Protonotarios and Tsatsopoulou defined the Carvajal variant as showing **predominantly left-ventricular involvement**, early morbidity, and clinical overlap with dilated cardiomyopathy [PMID: 15210133].

> *"truncates the intermediate filament-binding site of desmoplakin results in a variant of Naxos disease with predominantly left ventricular involvement, early morbidity and clinical overlapping with dilated cardiomyopathy (Carvajal syndrome)"* [PMID: 15210133]

### Finding 4 — Natural history, penetrance, and epidemiology

The temporal sequence is consistent: **woolly hair is present from birth**, **palmoplantar keratoderma develops during the first year of life**, and **cardiomyopathy manifests by adolescence with 100% penetrance** [PMID: 16722579]. The Carvajal variant manifests during childhood and more frequently leads to heart failure than the right-dominant Naxos (plakoglobin) form.

> *"Woolly hair appears from birth, palmoplantar keratoderma develop during the first year of life and cardiomyopathy is clinically manifested by adolescence with 100% penetrance"* [PMID: 16722579]

In the large **DSP-ERADOS Network** cohort (800 P/LP DSP variant carriers), over 3.7 years the rate of sustained ventricular arrhythmia was **17.4% (3.9%/yr)** and HF hospitalization **9.0% (1.8%/yr)**; notably **32.5% did not meet existing ARVC diagnostic criteria**, confirming DSP cardiomyopathy as a distinct arrhythmogenic entity featuring acute **myocarditis-like "hot phases"** [PMID: 39288222].

> *"the relevance of acute myocarditis-like episodes for subsequent disease course is largely unknown"* [PMID: 39288222]

Naxos disease (the related JUP syndrome) has a founder-driven prevalence of ~1:1000 on Naxos island; the DSP Carvajal variant is rarer and reported worldwide, often in consanguineous families.

### Finding 5 — Management: heart-failure therapy, antiarrhythmics, ICD, exercise restriction, transplantation; emerging EGFR concept

Management is organ-directed and supportive. A Carvajal patient was managed with diuretics, enalapril, carvedilol, and amiodarone and remained stable on follow-up [PMID: 21193976]. ICDs are implanted for uncontrolled VT and for sudden-death prevention, and transplantation is used for end-stage disease [PMID: 40108711]. The 2019 HRS expert consensus on arrhythmogenic cardiomyopathy provides class-of-recommendation guidance on risk stratification, ICD use, and exercise [PMID: 31078652]. Early ICD implantation can be lifesaving — one recipient was alive at age 59 [PMID: 25824144].

> *"Early diagnosis and ICD implantation may be lifes[aving]"* [PMID: 25824144]

For the cutaneous phenotype, **EGFR inhibition** restored DSP membrane expression and reduced keratinocyte fragility in DSP-mutant cells — a candidate mechanism-based dermatologic therapy [PMID: 38509711].

> *"EGFR inhibition in patient's keratinocytes strongly increased DSP expression at the plasma membrane, improved intermediate filament connection with the membrane edges and reduced the cell-cell fragility"* [PMID: 38509711]

### Finding 6 — Genotype–phenotype architecture: the "desmoplakinopathy" allelic series

DSP produces a graded allelic spectrum best captured by the umbrella term **"desmoplakinopathies"** [PMID: 20738328]. The phenotype depends on **gene dose** and **which protein domain is affected**:

- Homozygous c.7097G>A (p.Arg2366His) → skin fragility/woolly hair syndrome **without** cardiomyopathy [PMID: 20738328].
- Compound heterozygous nonsense/missense (C809X/N287K; Q664X/R2366C) → skin fragility/woolly hair via "desmoplakin haploinsufficiency"; heterozygous carriers unaffected; skin showed acantholysis and perinuclear keratin collapse [PMID: 11841538].
- A recessive DSP mutation "impairs the binding of desmoplakin to epidermal keratins and the muscle-specific intermediate filament desmin" — the dual-tissue protein-level lesion [PMID: 29878302].
- A knock-in *Dsp* mouse shows **gene dose-dependent** myocardial remodeling, arrhythmias, and premature death; recessive variants underlie syndromic Carvajal, dominant variants cause left-dominant DSP cardiomyopathy [PMID: 41411472].

> *"The complexity of the desmoplakin and its variable presentations warrant introducing the term 'desmoplakinopathies' to describe all the phenotypes related to defects in the desmoplakin"* [PMID: 20738328]

### Finding 7 — Diagnostic pitfall (myocarditis mimicry) and research infrastructure

DSP cardiomyopathy frequently **mimics acute myocarditis**. A young patient with chest pain and labs/imaging suspicious for acute myocarditis was ultimately found to have desmoplakin cardiomyopathy on genetic testing [PMID: 38652395].

> *"Desmoplakin cardiomyopathy may be considered in patients with recurrent acute myocarditis or a family history of cardiac disease to avoid the potential for misdiagnosis"* [PMID: 38652395]

The **NAXCARE** global registry has been established to systematically document clinical outcomes, genetic profiles, and care pathways for Naxos disease and related cardiocutaneous syndromes [PMID: 40316016]. Recent case reports continue to reinforce that **dermatologic signs serve as early warning of severe cardiac disease** [PMID: 42803515].

### Finding 8 — Foundational genetics: the Ecuadorian 7901delG mutation and DSP isoform biology

The disease was first defined genetically by Norgett et al., who described the **first recessive human DSP mutation, 7901delG**, homozygous in three Ecuadorian families, causing generalized striate keratoderma, woolly hair, and dilated left-ventricular cardiomyopathy; the frameshift creates a premature stop that removes the **C-domain of the desmoplakin tail**, and patients suffered heart failure in their teenage years [PMID: 11063735].

> *"we describe the first recessive human mutation, 7901delG, in the desmoplakin gene which causes a generalized striate keratoderma particularly affecting the palmoplantar epidermis, woolly hair and a dilated left ventricular cardiomyopathy"* [PMID: 11063735]

The DSP gene spans ~45 kb on chromosome 6 and comprises **24 exons** [PMID: 10594734]. Two major splice variants exist: **DSPI and DSPII**. Recessive loss of DSPI (with normal DSPII) causes epidermolytic PPK + woolly hair + severe arrhythmogenic DCM, whereas total DSP haploinsufficiency causes dominant striate PPK; DSPII is key for intermediate-filament stability and desmosome adhesion under stress [PMID: 22454510].

> *"complete absence of DSPI and the minor isoform DSPIa but normal levels of DSPII, and is associated with autosomal recessive epidermolytic PPK, woolly hair and severe arrhythmogenic dilated cardiomyopathy"* [PMID: 22454510]

### Finding 9 — WNT10A convergence unifies the ectodermal/dental triad under a shared Wnt deficit

The dental and ectodermal components of the syndrome are mechanistically linked to Wnt/β-catenin by **independent genetic convergence**. Mutations in **WNT10A**, a canonical Wnt ligand, produce the *same* triad — tooth agenesis (hypodontia/oligodontia), palmoplantar keratoderma, and alopecia/hair defects — all attributed to Wnt/β-catenin disruption [PMID: 42089627].

> *"ranging from isolated tooth agenesis to complex multisystem disorders, including hypodontia, enamel and root defects, palmoplantar keratoderma, alopecia, nail dystrophy"* [PMID: 42089627]

> *"linking phenotypes of WNT10A mutations to disruptions in Wnt/β-catenin signaling"* [PMID: 42089627]

A signaling-threshold framework places Wnt/β-catenin at the center of odontogenesis alongside BMP/FGF/SHH [PMID: 42196506]. Because DSP loss suppresses canonical Wnt/β-catenin ~2-fold via nuclear plakoglobin [PMID: 16823493], the dental/ectodermal branch of the DSP syndrome plausibly shares the Wnt-deficit mechanism — though direct demonstration in DSP-mutant dental epithelium remains lacking (inferred by convergence).

> *"We focus on the coordinated roles of Wnt/β-catenin, bone morphogenetic protein (BMP), fibroblast growth factor (FGF), and Sonic hedgehog (SHH) pathways"* [PMID: 42196506]

---

## Section-by-Section Disease Characterization

### 1. Disease Information
- **Overview:** A rare autosomal-recessive (occasionally dominant) desmosomal cardiocutaneous syndrome combining childhood-onset dilated/arrhythmogenic cardiomyopathy with congenital woolly hair, palmoplantar keratoderma, and — in the variant defining this entry — hypodontia/oligodontia.
- **Identifiers:** MONDO:0014355; OMIM #615821; part of the Carvajal syndrome / Naxos disease spectrum; Orphanet "Carvajal syndrome"; MeSH maps to Arrhythmogenic Right Ventricular Dysplasia / cardiomyopathies and palmoplantar keratoderma. ICD-11 maps to cardiomyopathy codes with ectodermal/dental codes.
- **Synonyms:** Carvajal syndrome; Carvajal-Huerta syndrome; dilated cardiomyopathy with woolly hair and keratoderma (DCWHK); Naxos-variant/left-dominant cardiocutaneous syndrome; desmoplakinopathy (syndromic form).
- **Information source:** Aggregated from individual patient case reports and small cohorts (disease-level resources such as OMIM/Orphanet synthesize these), now supplemented by registries (DSP-ERADOS [PMID: 39288222], NAXCARE [PMID: 40316016]).

### 2. Etiology
- **Causal factor:** Monogenic — biallelic (recessive) or heterozygous (dominant) pathogenic variants in **DSP**. No infectious or primary environmental cause.
- **Genetic risk factors:** The *DSP* genotype is causal, not merely a susceptibility locus. C-terminal truncations removing the tail intermediate-filament-binding domain are characteristic of the syndromic recessive form [PMID: 11063735, 15210133].
- **Environmental/lifestyle modifiers:** **Strenuous endurance exercise** accelerates cardiac remodeling and arrhythmia (demonstrated in Tg-DSP(R2834H) mice with perturbed Wnt signaling) [PMID: 26545710] and is a clinically actionable risk factor. Consanguinity increases recessive-disease risk.
- **Protective factors:** None established genetically; exercise restriction is protective behaviorally.
- **Gene–environment interaction:** DSP genotype × mechanical/exercise stress is the best-characterized GxE axis, consistent with the junction's role in resisting shear.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Frequency | Progression |
|---|---|---|---|---|---|
| Woolly hair | Physical/hair | HP:0002224 (woolly hair) | Congenital (birth) | ~100% | Stable |
| Palmoplantar keratoderma | Skin sign | HP:0000982 | First year of life | ~100% | Progressive/stable |
| Dilated/arrhythmogenic cardiomyopathy | Clinical sign | HP:0001644 (DCM); HP:0004756 (ventricular arrhythmia) | Childhood–adolescence | ~100% penetrance by adolescence | Progressive |
| Hypodontia/oligodontia (tooth agenesis) | Physical | HP:0000668 (hypodontia); HP:0006349 (oligodontia) | Congenital (eruption age) | Variable (defines this subtype) | Stable |
| Heart failure | Clinical sign | HP:0001635 | Childhood | High | Progressive |
| Ventricular tachycardia / sudden death | Clinical sign | HP:0004756 / HP:0001645 | Childhood–young adult | High | Episodic/fatal |
| Skin fragility / hyperkeratosis | Skin sign | HP:0000962 (hyperkeratosis) | Infancy | Variable | Stable |

- **Severity:** Severe, life-limiting owing to the cardiac component; cutaneous/dental signs are morbid but not life-threatening.
- **Quality-of-life impact:** Dominated by heart failure, arrhythmia, device/transplant burden; PPK causes pain and impaired ambulation; oligodontia impairs mastication and requires prosthodontic rehabilitation. No disease-specific EQ-5D/SF-36 data available.

### 4. Genetic / Molecular Information
- **Causal gene:** *DSP* (HGNC:3052; OMIM *125647), 24 exons, ~45 kb, chromosome 6p24.3 [PMID: 10594734].
- **Representative pathogenic variants:** c.1790C>T p.Ser597Leu (de novo missense, triad incl. oligodontia) [PMID: 20940358]; 7901delG (recessive, Ecuador) [PMID: 11063735]; c.4297C>T p.Gln1433* [PMID: 38433550]; c.3901C>T p.Gln1301X [PMID: 21193976].
- **Variant classes:** Nonsense/frameshift truncations (most common in syndromic recessive form), missense, splice-site. ACMG classification ranges pathogenic/likely-pathogenic to VUS; VUS complicate cardiac risk assessment.
- **Functional consequence:** Loss of function / haploinsufficiency (dominant skin disease) and biallelic loss of the DSPI isoform or C-terminal tail (recessive syndrome) [PMID: 22454510, 11841538].
- **Allele frequency:** Pathogenic truncations are rare/absent in gnomAD; the defining p.Ser597Leu was absent from 100 controls [PMID: 20940358].
- **Origin:** Germline. Both inherited (recessive, consanguineous) and *de novo* (dominant) events documented.
- **Modifier genes / epigenetics / chromosomal abnormalities:** No established DSP modifier genes or epigenetic/chromosomal mechanisms specific to this syndrome.

### 5. Environmental Information
- **Environmental factors:** None causal. **Endurance exercise** is a disease-accelerating mechanical stressor [PMID: 26545710].
- **Infectious agents:** None — but the **myocarditis-like "hot phase"** [PMID: 39288222, 38652395] is a sterile inflammatory mimic, not infection.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. Biallelic (or heterozygous) **DSP mutation** → truncated/dysfunctional desmoplakin, especially loss of the C-terminal tail / DSPI isoform. *(demonstrated)* [PMID: 11063735, 22454510]
2. **Leads to** impaired binding of desmoplakin to keratins (epidermis) and desmin (cardiomyocyte). *(demonstrated)* [PMID: 29878302]
3. **Results in** destabilized desmosomes and intermediate-filament detachment under mechanical/shear stress → cell–cell fragility, acantholysis, perinuclear keratin collapse (skin) and intercalated-disc disruption (heart). *(demonstrated)* [PMID: 11841538, 26545710]
4. **Releases plakoglobin** from the junctional pool → **nuclear translocation of plakoglobin**. *(demonstrated)* [PMID: 16823493]
5. **Suppresses canonical Wnt/β-catenin signaling** ~2-fold via Tcf/Lef1. *(demonstrated in cardiac cells)* [PMID: 16823493]
6. **Branch A (heart):** Wnt suppression → second-heart-field (Nkx2.5+/Mef2C+) progenitors adopt adipogenic/fibrogenic fate → **fibrofatty myocardial replacement**, apoptosis, connexin-43 remodeling → chamber dilation, electrical instability. *(demonstrated)* [PMID: 19359597, 16823493]
7. **Leads to** biventricular/left-dominant **dilated-arrhythmogenic cardiomyopathy**, ventricular arrhythmia, heart failure, sudden death; episodic myocarditis-like "hot phases." *(demonstrated clinically)* [PMID: 15210133, 39288222]
8. **Branch B (ectoderm/teeth):** same adhesion defect + shared Wnt deficit in ectodermal appendages → **woolly hair, palmoplantar keratoderma, and hypo/oligodontia** (tooth agenesis), paralleling WNT10A-related oligodontia. *(inferred by convergence)* [PMID: 42089627, 42196506]

- **Molecular pathways:** Canonical **Wnt/β-catenin** (central); GSK3-β/AKT (perturbed with exercise) [PMID: 26545710].
- **Cellular processes:** Cell-fate reprogramming (myocyte→adipocyte), apoptosis, fibrosis, inflammation.
- **Protein dysfunction:** Loss of IF-anchoring function of desmoplakin; mislocalization/aggregation of desmoplakin–plakoglobin–connexin-43 [PMID: 26545710].
- **GO/CL suggestions:** GO:0016055 (Wnt signaling), GO:0045216 (cell–cell junction organization), GO:0030216 (keratinocyte differentiation), GO:0060215 (fat cell differentiation); CL:0000746 (cardiac muscle cell), CL:0000312 (keratinocyte), CL:0000136 (adipocyte), CL:0000057 (fibroblast).

### 7. Anatomical Structures Affected
- **Primary organs:** Heart (myocardium, both ventricles; left-dominant) — UBERON:0000948; skin/epidermis (palms, soles) — UBERON:0001003; hair follicles — UBERON:0002073; teeth — UBERON:0001091.
- **Body systems:** Cardiovascular; integumentary; dental/ectodermal.
- **Tissues/cells:** Cardiac muscle (CL:0000746), keratinocytes (CL:0000312), adipocytes/fibroblasts replacing myocardium.
- **Subcellular:** Desmosome (GO:0030057), intercalated disc (GO:0014704), intermediate filament cytoskeleton (GO:0045111), nucleus (plakoglobin relocalization).
- **Lateralization:** Bilateral (symmetric cutaneous involvement; biventricular cardiac involvement).

### 8. Temporal Development
- **Onset:** Woolly hair congenital; PPK in first year; cardiomyopathy childhood–adolescence [PMID: 16722579].
- **Progression:** Progressive, chronic, lifelong; punctuated by episodic arrhythmic/myocarditis-like events [PMID: 39288222].
- **Penetrance:** ~100% cardiac penetrance by adolescence in the recessive syndrome [PMID: 16722579]; later-onset, lower-penetrance cardiac phenotype in dominant carriers.
- **Critical period:** Adolescence–young adulthood is the window of highest sudden-death risk, making early ICD decisions pivotal.

### 9. Inheritance and Population
- **Inheritance:** Autosomal recessive (syndromic Carvajal with full triad, biallelic C-terminal truncations); autosomal dominant (left-dominant DSP cardiomyopathy, variable skin) [PMID: 41411472].
- **Penetrance/expressivity:** Complete cardiac penetrance by adolescence (recessive); variable expressivity across the desmoplakinopathy spectrum [PMID: 20738328].
- **Founder effects/consanguinity:** Naxos disease (JUP) ~1:1000 on Naxos island (founder); DSP Carvajal often consanguineous (Ecuador, India, Middle East) [PMID: 11063735, 21193976, 40108711].
- **Carrier frequency:** Heterozygous DSP truncation carriers may show isolated cutaneous/curly-hair signs with delayed cardiomyopathy risk.
- **Sex ratio:** No strong sex bias reported.

### 10. Diagnostics
- **Clinical recognition:** Woolly hair + PPK + childhood cardiomyopathy (± tooth agenesis) is pathognomonic; dermatologic signs are early red flags [PMID: 42803515].
- **Imaging:** Echocardiography (biventricular dilation, reduced EF), cardiac MRI (late gadolinium enhancement, subepicardial fibrosis).
- **Electrophysiology:** ECG/Holter for PVCs, VT; abnormal ECGs in models [PMID: 25659760].
- **Biopsy/histology:** Skin — acantholysis, desmosome clustering, perinuclear keratin collapse [PMID: 11841538]; myocardium — fibrofatty replacement.
- **Genetic testing:** Definitive. DSP single-gene or cardiomyopathy/ARVC gene panels, WES/WGS; must distinguish P/LP from VUS. Differential diagnosis: other desmosomal genes (JUP → Naxos/CAPK [PMID: 21668431]; PKP2, DSG2, DSC2 → ARVC), and WNT10A-related ectodermal dysplasia for the dental/skin overlap.
- **Diagnostic pitfall:** Mimics acute/recurrent myocarditis [PMID: 38652395].

### 11. Outcome / Prognosis
- **Mortality:** High in childhood recessive disease — 3/10 sudden deaths and 4/10 transplants in one pediatric cohort [PMID: 40108711].
- **Morbidity:** Progressive heart failure, recurrent arrhythmia, device dependence, transplant; PPK pain; dental impairment.
- **Prognostic factors:** Biallelic C-terminal truncation, early LV dysfunction, VT burden, and history of myocarditis-like episodes portend worse outcome [PMID: 15210133, 39288222].
- **Recovery:** No spontaneous recovery; transplantation addresses end-stage cardiac disease.

### 12. Treatment
- **Pharmacotherapy (NCIT-type: heart-failure/antiarrhythmic agents):** Diuretics, ACE inhibitors (enalapril), beta-blockers (carvedilol), antiarrhythmics (amiodarone) [PMID: 21193976]; guideline-directed HF therapy.
- **Device/surgical:** ICD for VT/sudden-death prevention [PMID: 25824144, 40108711]; cardiac transplantation for end-stage disease [PMID: 40108711].
- **Lifestyle:** Exercise restriction (mechanistically supported) [PMID: 26545710, 31078652].
- **Dermatologic/dental:** Emollients/keratolytics for PPK; prosthodontic management of oligodontia. Experimental **EGFR inhibition** restores DSP membrane localization in vitro [PMID: 38509711].
- **Guidelines:** 2019 HRS consensus on arrhythmogenic cardiomyopathy for risk stratification/ICD/exercise [PMID: 31078652].

### 13. Prevention
- **Primary:** Genetic counseling in consanguineous/affected families; carrier testing; prenatal/preimplantation diagnosis for known familial variants.
- **Secondary:** Cascade genetic screening and cardiac surveillance of at-risk relatives; recognition of cutaneous signs as pre-cardiac markers [PMID: 42803515].
- **Tertiary:** ICD, HF therapy, exercise restriction to prevent sudden death and slow remodeling.

### 14. Other Species / Natural Disease
- **Orthologue:** *Dsp* (mouse); highly conserved.
- **Natural/spontaneous models:** The **Dsp^rul (ruffled)** spontaneous mouse mutation — an autosomal-recessive frameshift truncating the C-terminal plakin repeat domain — reproduces abnormal coat/woolly hair, epidermal blistering, abnormal ECGs, and ventricular fibrosis, closely modeling Carvajal-Huerta syndrome [PMID: 25659760].
- **Comparative biology:** Desmosomal biology and the Wnt/plakoglobin mechanism are evolutionarily conserved across vertebrates [PMID: 20940358].

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | PMID |
|---|---|---|---|
| Dsp^rul (ruffled) mouse | Spontaneous recessive frameshift (C-terminal truncation) | Woolly coat, epidermal blistering, abnormal ECG, ventricular fibrosis — strong Carvajal model | [25659760] |
| Dsp knock-in mouse | Engineered knock-in | Gene dose-dependent myocardial remodeling, arrhythmias, premature death | [41411472] |
| Tg-DSP(R2834H) mouse | Transgenic (mutant overexpression) | Exercise-accelerated RV dilation, fat infiltration, desmoplakin/plakoglobin/Cx43 aggregates, perturbed Wnt | [26545710] |
| Cardiac-restricted Dsp deletion | Conditional knockout | Embryonic lethal (homozygous); fibrofatty replacement, apoptosis, arrhythmias (heterozygous) | [16823493] |
| Patient-derived keratinocytes (in vitro) | Cellular | Cell–cell fragility; corrected by EGFR inhibition | [38509711] |

- **Applications:** Mechanism of Wnt suppression, exercise interaction, and drug testing (EGFR inhibition).
- **Limitations:** Mouse cardiac anatomy and the tooth-agenesis component are incompletely modeled; dental phenotype of DSP mutants under-studied.

---

## Mechanistic Model / Interpretation

```
            DSP mutation (biallelic truncation / dominant LOF)
                              |
                              v
   Loss of desmoplakin C-terminal tail  ->  cannot bind keratin / desmin
                              |
         +--------------------+--------------------+
         |                                         |
  Mechanical junction failure              Plakoglobin released
  (shear-stressed tissues)                        |
         |                                         v
         |                          Nuclear plakoglobin -> Tcf/Lef1
         |                          ~2x suppression of canonical
         |                          Wnt/beta-catenin signaling
         |                                         |
   SKIN / HAIR / TEETH          HEART: 2nd-heart-field progenitors
   - woolly hair (congenital)   redirected to adipogenic/fibrogenic fate
   - palmoplantar keratoderma           |
   - tooth agenesis  <----- shared      v
     (WNT10A-convergent, inferred)  fibrofatty myocardial replacement
                                        |
                                        v
                        biventricular / left-dominant DCM,
                        VT / sudden death, heart failure,
                        myocarditis-like "hot phases"
```

The model's great strength is that a **single lesion** — failure of intermediate-filament anchoring at the desmosome — produces both a **mechanical** failure (skin/hair/heart fragility) and a **signaling** failure (nuclear plakoglobin → Wnt suppression). The heart branch is experimentally demonstrated end-to-end [PMID: 16823493, 19359597]. The ectodermal/dental branch is anchored mechanically (keratin-binding loss [PMID: 29878302]) and linked to Wnt by **convergence** with WNT10A oligodontia [PMID: 42089627], which remains the key inferred (not yet directly demonstrated) step.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [20940358](https://pubmed.ncbi.nlm.nih.gov/20940358/) | Supports F1 | De novo DSP p.Ser597Leu causing triad **with tooth agenesis**; links desmosomes to odontogenesis |
| [16823493](https://pubmed.ncbi.nlm.nih.gov/16823493/) | Supports F2 | Core mechanism: nuclear plakoglobin → ~2× Wnt suppression → fibrofatty fate |
| [19359597](https://pubmed.ncbi.nlm.nih.gov/19359597/) | Supports F2 | Adipocytes derive from second-heart-field progenitors |
| [26545710](https://pubmed.ncbi.nlm.nih.gov/26545710/) | Supports F2/F5 | Exercise accelerates remodeling; basis for exercise restriction |
| [40108711](https://pubmed.ncbi.nlm.nih.gov/40108711/) | Supports F3/F5 | Pediatric cohort: transplant and sudden death outcomes |
| [15210133](https://pubmed.ncbi.nlm.nih.gov/15210133/) | Supports F3 | Defines left-dominant Carvajal DCM phenotype |
| [38433550](https://pubmed.ncbi.nlm.nih.gov/38433550/) | Supports F1/F3 | Biventricular DCM, EF 22%, homozygous p.Gln1433* |
| [16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/) | Supports F4 | Onset sequence and 100% cardiac penetrance by adolescence |
| [39288222](https://pubmed.ncbi.nlm.nih.gov/39288222/) | Supports F4 | 800-carrier cohort; distinct arrhythmogenic entity; hot phases |
| [25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/) | Supports F5 | Early ICD lifesaving |
| [31078652](https://pubmed.ncbi.nlm.nih.gov/31078652/) | Supports F5 | HRS guideline for ACM management |
| [38509711](https://pubmed.ncbi.nlm.nih.gov/38509711/) | Supports F5 | EGFR inhibition corrects keratinocyte phenotype |
| [20738328](https://pubmed.ncbi.nlm.nih.gov/20738328/) | Supports F6 | "Desmoplakinopathies" spectrum; skin-only alleles |
| [11841538](https://pubmed.ncbi.nlm.nih.gov/11841538/) | Supports F6 | Compound-het haploinsufficiency; skin histology |
| [29878302](https://pubmed.ncbi.nlm.nih.gov/29878302/) | Supports F6 | Keratin + desmin binding loss (dual-tissue lesion) |
| [41411472](https://pubmed.ncbi.nlm.nih.gov/41411472/) | Supports F6 | Gene dose-dependent knock-in mouse |
| [38652395](https://pubmed.ncbi.nlm.nih.gov/38652395/) | Supports F7 | Myocarditis mimicry / misdiagnosis risk |
| [40316016](https://pubmed.ncbi.nlm.nih.gov/40316016/) | Supports F7 | NAXCARE registry |
| [11063735](https://pubmed.ncbi.nlm.nih.gov/11063735/) | Supports F8 | Foundational recessive 7901delG, Ecuador |
| [22454510](https://pubmed.ncbi.nlm.nih.gov/22454510/) | Supports F8 | DSPI vs DSPII isoform specificity |
| [10594734](https://pubmed.ncbi.nlm.nih.gov/10594734/) | Supports F8 | DSP gene structure (24 exons, ~45 kb) |
| [42089627](https://pubmed.ncbi.nlm.nih.gov/42089627/) | Supports F9 | WNT10A reproduces same triad via Wnt disruption |
| [42196506](https://pubmed.ncbi.nlm.nih.gov/42196506/) | Supports F9 | Wnt/β-catenin central to tooth agenesis |
| [25659760](https://pubmed.ncbi.nlm.nih.gov/25659760/) | Supports §14/15 | Dsp^rul spontaneous mouse model |
| [21668431](https://pubmed.ncbi.nlm.nih.gov/21668431/) | Differential | JUP (plakoglobin) cause of related CAPK syndrome |

---

## Limitations and Knowledge Gaps

1. **Dental mechanism is inferred, not demonstrated.** The link between DSP loss and tooth agenesis rests on WNT10A phenotypic convergence [PMID: 42089627] plus the demonstrated cardiac Wnt suppression [PMID: 16823493]. No study has directly shown reduced Wnt/β-catenin signaling or desmosomal failure in DSP-mutant dental epithelium.
2. **Tooth agenesis is a variable, sub-type-defining feature**, not universal across all DSP cardiocutaneous cases; frequency data are limited to small series.
3. **Rarity and reporting bias.** Most human evidence comes from case reports and small cohorts; prevalence/incidence figures are not precisely established for the DSP (as opposed to JUP/Naxos) form.
4. **Genotype–phenotype complexity.** The same gene produces skin-only, cardiac-only, and full-syndrome phenotypes depending on dose, domain, and isoform [PMID: 20738328, 22454510]; predicting phenotype from genotype remains imperfect, and VUS complicate cardiac risk assessment.
5. **No disease-specific therapy.** Management is supportive; EGFR inhibition is in-vitro only [PMID: 38509711], and no Wnt-restoring therapy has reached the clinic.
6. **Model gaps.** Mouse models capture cardiac and cutaneous features well but under-represent the human tooth-agenesis phenotype.

---

## Proposed Follow-up Experiments / Actions

1. **Directly test the Wnt-deficit hypothesis in dental epithelium:** generate DSP-mutant dental organoids or epithelial-specific Dsp knockouts and quantify β-catenin/Tcf-Lef activity and enamel-knot Wnt targets, to convert the inferred dental mechanism (F9) into a demonstrated one.
2. **Catalog tooth-agenesis frequency and pattern** across a prospective DSP cohort (via NAXCARE [PMID: 40316016]) to define its penetrance and position (which teeth) relative to WNT10A oligodontia.
3. **Genotype–phenotype stratification** correlating truncation position/isoform impact (DSPI vs DSPII) with cardiac severity, cutaneous pattern, and dental involvement, building on the gene-dose mouse data [PMID: 41411472].
4. **Evaluate Wnt-pathway or EGFR-pathway modulation** as organ-sparing therapy — extending the in-vitro EGFR-inhibition result [PMID: 38509711] to cardiac and dental models.
5. **Prospective exercise-restriction and ICD-timing studies** in genotype-positive children to refine the adolescence critical-window risk management [PMID: 31078652, 39288222].
6. **Standardized cascade screening protocols** pairing dermatologic/dental examination with cardiac genetics in families, leveraging cutaneous signs as early markers [PMID: 42803515].

---

*Evidence source types: predominantly human clinical (case reports, cohorts, registries) and model-organism (mouse) data, with in-vitro cellular mechanistic studies; the dental/Wnt link is supported by cross-disease human genetic convergence (computational/comparative inference).*


## Artifacts

- [OpenScientist final report](Dilated_Cardiomyopathy_with_Woolly_Hair_Keratoderma_and_Tooth_Agenesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Dilated_Cardiomyopathy_with_Woolly_Hair_Keratoderma_and_Tooth_Agenesis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000982` (1 mention) - the report calls it "Skin sign"; HP calls it **Palmoplantar keratoderma**
- `HP:0001635` (1 mention) - the report calls it "Clinical sign"; HP calls it **Congestive heart failure**
- `GO:0060215` (1 mention) - the report calls it "fat cell differentiation"; GO calls it **primitive hemopoiesis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016055` (1 mention) - the report calls it "Wnt signaling"; GO calls it **Wnt signaling pathway**
- `CL:0000746` (2 mentions) - the report calls it "cardiac muscle cell", "Tissues/cells:** Cardiac muscle"; CL calls it **cardiac muscle cell**
- `GO:0030057` (1 mention) - the report calls it "Subcellular:** Desmosome"; GO calls it **desmosome**, and lists "spot desmosome" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000746` - called "cardiac muscle cell", "Tissues/cells:** Cardiac muscle"