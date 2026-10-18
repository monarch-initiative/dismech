---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T17:30:49.070567'
end_time: '2026-08-31T17:40:28.855259'
duration_seconds: 579.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual disability, X-linked 100 (KIF4A-related non-syndromic
    X-linked intellectual disability, MRX100)
  mondo_id: MONDO:0010488
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
reference_validation:
  total_references: 7
  verified: 6
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.143
  relevance_assessed: 6
  on_topic: 2
  unresolved_references:
  - DOI:10.1083/jcb.202208108
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 49
  verified: 48
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0010488
    reported_labels:
    - if available
    ontology_label: intellectual disability, X-linked 100
  obsolete_terms:
  - term_id: CL:0002609
    ontology_label: obsolete neuron of cerebral cortex
    replaced_by: CL:0010012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Intellectual_Disability_X-linked_100-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual disability, X-linked 100 (KIF4A-related non-syndromic X-linked intellectual disability, MRX100)
- **MONDO ID:** MONDO:0010488 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual disability, X-linked 100 (KIF4A-related non-syndromic X-linked intellectual disability, MRX100)** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual disability, X-linked 100 (KIF4A-related non-syndromic X-linked intellectual disability, MRX100)
- **MONDO ID:** MONDO:0010488 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual disability, X-linked 100 (KIF4A-related non-syndromic X-linked intellectual disability, MRX100)** covering all of the
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


# KIF4A-related X-linked intellectual disability (MRX100): disease-characteristics report

## Executive summary and evidence limits

**Intellectual disability, X-linked 100 (MRX100)** is an ultra-rare, predominantly male neurodevelopmental disorder caused by hemizygous variants in **KIF4A**, an X-chromosomal kinesin/chromokinesin gene. The core phenotype is childhood-onset developmental delay or intellectual disability, variably accompanied by epilepsy, speech and motor delay, microcephaly, behavioral abnormalities, and structural brain malformations. More severe alleles/cases expand the phenotype to hydrocephalus, polymicrogyria, heterotopia, hydranencephaly, and congenital eye, dental, renal/urinary, lymphatic, or limb anomalies. The label “non-syndromic” therefore describes the founding family better than the full contemporary phenotypic spectrum. Open Targets links MONDO:0010488 to KIF4A with five evidence records and an association score of 0.6245. (OpenTargets Search: intellectual disability, X-linked 100-KIF4A, willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 7-10)

The evidence base remains small: a disease-defining family reported in 2014, a heterogeneous 11-male series in 2021, and a subsequent R728Q case studied mechanistically in mice. Consequently, prevalence, penetrance in females, survival, robust phenotype frequencies, and genotype–phenotype correlations cannot yet be estimated reliably. The 2021 authors explicitly cautioned that their reported variants remained **VUS under strict ACMG criteria**, notwithstanding phenotype and segregation evidence. (kalantari2021expandingthekif4a pages 7-10)

| Evidence domain | Finding | Evidence type/model | Quantitative detail | Source date/PMID/DOI | Confidence/caveat |
|---|---|---|---|---|---|
| Disease-gene association | KIF4A is the principal gene associated with MONDO:0010488, intellectual disability, X-linked 100 | Aggregated disease-target resource integrating literature/clinical variant evidence | Open Targets association score 0.6245; 5 evidence items linked to KIF4A | Open Targets, accessed via context for MONDO_0010488 (OpenTargets Search: intellectual disability, X-linked 100-KIF4A) | High for disease-gene linkage; resource-level aggregation, not a primary clinical description |
| Founding human clinical report | Original MRX100/XLID family showed X-linked recessive neurodevelopmental disease with mild-moderate intellectual disability and epilepsy in multiple males | Human clinical genetics; multigenerational family | 5 affected males across 3 generations; 4/5 had epilepsy with onset in late childhood/adolescence; 3 carrier females identified; 2 unaffected males lacked the variant | 2014; J Med Genet; DOI: 10.1136/jmedgenet-2013-102182 (willemsen2014involvementofthe pages 3-4, willemsen2014involvementofthe pages 2-3) | High; founding disease-defining family |
| Founding causal variant | The founding family carried a splice-disrupting in-frame indel causing exon 15 skipping and reduced KIF4A expression | Human molecular genetics + patient RNA/protein studies | NM_012310.4:c.1489-8_1490delins10; ~50% reduced KIF4A expression in patient cell lines; truncated/lower-molecular-weight product reported | 2014; J Med Genet; DOI: 10.1136/jmedgenet-2013-102182 (willemsen2014involvementofthe pages 3-4) | High for variant effect in that family; exact ACMG terminology not provided in the 2014 paper |
| Severe sporadic case in 2014 study | A separate female case broadened severity toward cortical malformation, severe developmental delay, and early-onset seizures | Human sporadic case from ID cohort | 1 female from series of 100 ID patients; seizures from 6 months; walked independently at 9-10 years; secondary microcephaly; absent speech; frontal cortical malformation | 2014; J Med Genet; DOI: 10.1136/jmedgenet-2013-102182 (willemsen2014involvementofthe pages 3-4) | Moderate; single case and causal attribution is less canonical than the family report |
| Expanded phenotype cohort | KIF4A-associated phenotype expanded beyond non-syndromic ID to epilepsy, hydrocephalus, polymicrogyria, heterotopia, eye/dental/renal anomalies, and severe brain malformations | Human multicenter case series | 11 male patients total; 10 missense variants and 1 splice variant; included sibling sets; epilepsy reported in 4 patients; imaging included ventricular dilatation, polymicrogyria, heterotopia, hydranencephaly | 2021; Am J Med Genet A; DOI: 10.1002/ajmg.a.62443 (kalantari2021expandingthekif4a pages 7-10, kalantari2021expandingthekif4a pages 6-6, kalantari2021expandingthekif4a pages 6-7) | Moderate-high for phenotypic expansion; heterogeneous ascertainment |
| Variant interpretation caveat | Despite compelling phenotype overlap, all 2021 variants were considered VUS under strict ACMG criteria | Human clinical variant interpretation | 11 male patients; all reported variants classified as VUS by strict ACMG framework in that paper | 2021; Am J Med Genet A; DOI: 10.1002/ajmg.a.62443 (kalantari2021expandingthekif4a pages 7-10) | High for the caveat itself; important limitation when populating knowledge bases |
| Synaptic mechanism linked to ID | KIF4A loss/downregulation disrupts excitatory/inhibitory synaptic balance, a plausible proximal mechanism for cognitive/epileptic phenotypes | Experimental neurobiology in primary rat hippocampal neurons | Kif4a knockdown decreased mIPSC frequency and altered mEPSCs (decreased amplitude, increased frequency) | 2014; J Med Genet; DOI: 10.1136/jmedgenet-2013-102182 (willemsen2014involvementofthe pages 6-7, willemsen2014involvementofthe pages 4-6) | Moderate-high; strong cellular mechanism but not yet direct proof for every human variant |
| Human 2022 mechanistic extension | A patient KIF4A missense variant R728Q was linked to global developmental delay, severe intellectual disability, and intractable seizures | Human case plus mechanistic follow-up | Variant: R728Q in exon 20/coiled-coil region; patient pedigree included carrier females; patient MRI described as unremarkable in supplementary material excerpt | 2022; J Cell Biol; DOI: 10.1083/jcb.202208108 (wan2022kif4regulatesneuronal pages 1-2, wan2022kif4regulatesneuronal pages 24-28) | Moderate; single-family/case evidence but followed by detailed modeling |
| Knock-in mouse disease model | The R728Q-equivalent Kif4 mutant mouse recapitulated developmental delay, smaller brain/hippocampus, cognitive deficits, anxiety-like behavior, and marked seizure susceptibility | Knock-in/engineered mouse model | Male offspring underrepresented (~31% observed vs 50% expected); increased fetal demise (~26% vs 7% WT); lower weights P3-P14; after PTZ 11/15 mutants reached stage 5 seizures and 3 died; ~10-fold EEG power increase post-PTZ | 2022; J Cell Biol; DOI: 10.1083/jcb.202208108 (wan2022kif4regulatesneuronal pages 4-5, wan2022kif4regulatesneuronal pages 2-4) | High for model phenotype; animal model may not capture full human allelic spectrum |
| PARP1-TrkB-KCC2 pathway | The 2022 study supports a mechanistic chain in which mutant KIF4 alters PARP1 signaling, increases TrkB, lowers KCC2, perturbs chloride homeostasis, and increases seizure susceptibility | Mouse + cultured neuron mechanistic studies | Mutant KIF4 showed stronger PARP1 binding; KCC2 significantly reduced in motor cortex/hippocampus; intracellular chloride increased; CA3 pyramidal neurons showed hyper-branching/spine abnormalities | 2022; J Cell Biol; DOI: 10.1083/jcb.202208108 (wan2022kif4regulatesneuronal pages 5-7, wan2022kif4regulatesneuronal pages 13-15, wan2022kif4regulatesneuronal pages 1-2) | Moderate-high; some links are mechanistically strong, but pathway ordering remains partly model-based |
| Preclinical rescue | Enhancing PARP1-related signaling rescued key mutant phenotypes, suggesting therapeutic tractability but not a clinical therapy | Preclinical intervention in cultured neurons/mice | NAD supplementation rescued seizure susceptibility; neuronal survival rescued by NAD or high KCl under stress conditions; statistical significance often P < 0.0001 in cited experiments | 2022; J Cell Biol; DOI: 10.1083/jcb.202208108 (wan2022kif4regulatesneuronal pages 5-7, wan2022kif4regulatesneuronal pages 28-31) | Moderate; preclinical only, not disease-specific standard of care |
| 2023 neural biology update | KIF4A is expressed in adult neurons and Schwann cells and is induced after peripheral nerve injury, extending biology beyond development | Rat/human tissue study, preprint | Schwann-cell KIF4A mRNA ~6-fold higher in proliferating vs quiescent cultures; DRG neuron Kif4a up ~2-fold to ~2.7-fold after injury; distal stump up ~12-13-fold at 7 dpi | 2023; bioRxiv preprint; DOI: 10.1101/2023.05.21.541636 (correia2023unexpectedkif4afunctions pages 2-5, correia2023unexpectedkif4afunctions pages 10-13, correia2023unexpectedkif4afunctions pages 5-7, correia2023unexpectedkif4afunctions pages 1-2) | Moderate; biologically relevant but preprint and not disease-specific to MRX100 |
| 2024 neural injury relevance | Post-stroke rat brain re-expresses KIF4 in peri-infarct tissue, consistent with broader roles in adult neural plasticity/repair | Peer-reviewed rat stroke model | kif4 mRNA in juvenile brain ~2.47-3.30; selective re-expression in penumbra at day 3 post-stroke; KIF4 localized in neuronal precursor cells, glia, and NeuN+ neurons | 2024; Brain Pathology; DOI: 10.1111/bpa.13232 (ruscu2024thepost‐strokeyoung pages 7-8) | Moderate; not an MRX100 study, but relevant for KIF4A functional interpretation |
| Clinical implementation / trials | No disease-specific interventional clinical trial for KIF4A-related MRX100 was identified in the trial searches performed | Trial registry search + literature review | 0 relevant registered interventional trials retrieved for KIF4A/MRX100 | Trial search status in current evidence synthesis (OpenTargets Search: intellectual disability, X-linked 100-KIF4A) | High for current search result; always subject to registry update and search-scope limitations |


*Table: This table summarizes the highest-confidence disease, mechanism, model, and translational evidence for KIF4A-related X-linked intellectual disability (MRX100). It is useful for quickly separating well-supported findings from important caveats such as ACMG VUS classification and preclinical-only therapeutic signals.*

## 1. Disease information

### Definition and identifiers

- **Preferred name:** intellectual disability, X-linked 100.
- **Synonyms:** MRX100; XLID100; KIF4A-related intellectual disability; KIF4A-related neurodevelopmental disorder; KIF4A-associated disorder. “KIF4A-related non-syndromic XLID” is narrower and potentially misleading for patients with malformations.
- **MONDO:** **MONDO:0010488**.
- **Causal gene:** **KIF4A**, kinesin family member 4A; **OMIM gene 300521**; Ensembl **ENSG00000090889**. (OpenTargets Search: intellectual disability, X-linked 100-KIF4A, willemsen2014involvementofthe pages 1-2)
- **Disease OMIM:** commonly catalogued as **MRX100 / intellectual disability, X-linked 100**; the exact disease-number field should be verified directly against the current licensed OMIM record before database ingestion.
- **Orphanet:** no disorder-specific Orpha number was established from the retrieved evidence.
- **ICD-10/ICD-11/MeSH:** no KIF4A-specific code. Coding is phenotype-based—for example, intellectual developmental disorder and, when applicable, epilepsy, microcephaly, or congenital brain malformation. A generic code must not be treated as a molecular diagnosis.

The disease description is an **aggregated disease-level synthesis** of pedigrees, case reports/series, patient-derived molecular studies, and experimental models—not an EHR-derived population estimate. The founding study sequenced X-chromosome exons in more than 200 XLID families; the severe female was drawn from a separate series of 100 individuals with ID. (willemsen2014involvementofthe pages 3-4, willemsen2014involvementofthe pages 2-3)

### Key primary sources

1. Willemsen et al., *Journal of Medical Genetics*, May 2014; PMID **24812067**; DOI/URL: https://doi.org/10.1136/jmedgenet-2013-102182. The paper’s central conclusion was that KIF4A/KIF5C variants implicate kinesin-dependent synaptic function in ID. (willemsen2014involvementofthe pages 3-4, willemsen2014involvementofthe pages 1-2)
2. Kalantari et al., *American Journal of Medical Genetics A*, online August 2021; PMID **34346154**; DOI/URL: https://doi.org/10.1002/ajmg.a.62443. Abstract quote: **“We expand the phenotype associated with KIF4A variants from developmental delay and intellectual disability with or without epilepsy to a congenital anomaly phenotype with hydrocephalus and various brain anomalies.”** (kalantari2021expandingthekif4a pages 7-10)
3. Wan et al., *Journal of Cell Biology*, December 2022/2023 volume; DOI/URL: https://doi.org/10.1083/jcb.202208108. Abstract wording states that the study revealed a mechanism connecting KIF4-regulated chloride homeostasis and neuronal morphology to epilepsy susceptibility. (wan2022kif4regulatesneuronal pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The primary cause is a **germline KIF4A sequence variant** affecting KIF4A dosage, splicing, motor-domain function, or protein regulation. The founding **NM_012310.4:c.1489-8_1490delins10** allele disrupts the exon-15 acceptor, produces exon skipping and a shortened protein, and reduced KIF4A abundance by approximately 50% in patient cells. (willemsen2014involvementofthe pages 3-4)

### Genetic risk

Hemizygous males carrying a functionally damaging X-linked allele have the greatest established risk. Reported examples include **c.763G>A (p.Asp255Asn), c.794G>T (p.Arg265Leu), c.1616T>C (p.Leu539Pro), c.1745T>A (p.Leu582His), c.2266A>C (p.Ser756Arg), c.2558G>T (p.Arg853Leu), c.3299G>A (p.Arg1100Lys), c.1674+1G>A**, the founding complex splice indel, and **p.Arg728Gln (R728Q)**. Several were maternally inherited; p.Leu539Pro was reported de novo. Transcript/version normalization is essential before clinical reuse. (kalantari2021expandingthekif4a pages 6-6, kalantari2021expandingthekif4a pages 6-7, wan2022kif4regulatesneuronal pages 1-2)

Family history consistent with X-linked transmission increases prior probability. The founding pedigree contained five affected males over three generations, three carrier females, and two unaffected males without the variant. Linkage was interpreted as X-linked recessive with complete penetrance among the informative males, but this single pedigree cannot establish universal penetrance. (willemsen2014involvementofthe pages 3-4, willemsen2014involvementofthe pages 2-3)

### Environmental, infectious, and lifestyle risk

No toxin, infection, diet, occupation, smoking, alcohol exposure, or other environmental factor has been shown to cause MRX100. Maternal age, paternal age, consanguinity, and lifestyle are not established disease-specific risk factors. Consanguinity is not mechanistically required for an X-linked disorder.

### Protective factors and gene–environment interaction

No validated protective human allele or environmental exposure is known. NAD supplementation rescued seizure susceptibility in an R728Q-equivalent mouse, but this is **preclinical pathway rescue**, not evidence that dietary NAD or supplements protect humans. Seizure-provoking exposures may modify manifestations as in other epilepsies, but no KIF4A-specific gene–environment interaction has been demonstrated. (wan2022kif4regulatesneuronal pages 5-7, wan2022kif4regulatesneuronal pages 28-31)

## 3. Phenotypes

The frequencies below are study-specific rather than population estimates.

- **Developmental delay / intellectual disability** — core feature; **HP:0012758 / HP:0001249**. Onset is developmental/childhood; severity ranges from mild–moderate in the founding males to severe. The founding males could use simple sentences, whereas a severe female had absent speech and walked only at 9–10 years. Functional effect includes impaired learning, communication, independence, education, and adaptive behavior. (willemsen2014involvementofthe pages 3-4)
- **Speech/language delay or absent speech** — **HP:0000750 / HP:0001344**. Childhood onset; variable and generally persistent. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 6-7)
- **Delayed motor milestones** — **HP:0001270**, with delayed walking **HP:0002060**. Examples include head control at 5–6 months and walking after age 3 years; the severe female walked at 9–10 years. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 6-6)
- **Epilepsy/seizures** — **HP:0001250**. Four of five founding males had complex-partial/generalized seizures beginning in late childhood or adolescence; the severe female developed seizures at 6 months. The 2021 series included epilepsy in four patients, including a drug-refractory case with multifocal discharges. Frequency and onset are therefore allele-dependent and variable. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 7-10, kalantari2021expandingthekif4a pages 6-6)
- **Microcephaly/secondary microcephaly** — **HP:0000252**. Head size ranged from small/low-normal in the founding family to below −2.5 SD in the severe female. (willemsen2014involvementofthe pages 3-4, willemsen2014involvementofthe pages 2-3)
- **Brain malformations** — polymicrogyria **HP:0002126**, perisylvian polymicrogyria **HP:0006821**, heterotopia **HP:0002282**, ventriculomegaly **HP:0002119**, hydrocephalus **HP:0000238**, cerebral atrophy **HP:0002059**, and hydranencephaly **HP:0002324**. Imaging can also be normal, indicating marked variable expressivity. (kalantari2021expandingthekif4a pages 7-10, kalantari2021expandingthekif4a pages 6-6, kalantari2021expandingthekif4a pages 6-7, wan2022kif4regulatesneuronal pages 24-28)
- **Behavioral abnormalities** — autism spectrum features **HP:0000729**, self-injurious behavior **HP:0100716**, and possible anxiety **HP:0000739**. Severe self-injury was described in one patient; autism occurred in part of the expanded series. Anxiety is supported principally by the mouse model and should not be treated as an established common human feature. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 6-7, wan2022kif4regulatesneuronal pages 4-5)
- **Congenital anomalies, variable** — Peters anomaly/anterior-segment eye anomaly, small hands/feet, dental anomalies, renal/urinary-tract anomalies, congenital lymphedema, and other skeletal or limb findings. Suggested terms include **HP:0000659** (Peters anomaly), **HP:0001156** (brachydactyly), **HP:0000691** (abnormality of dental morphology), **HP:0012210** (abnormal renal morphology), and **HP:0001004** (lymphedema). These are not obligatory features. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 7-10, kalantari2021expandingthekif4a pages 6-7)

No disease-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was identified. Quality-of-life impact must therefore be inferred from developmental dependence, communication limitations, epilepsy, behavioral dysregulation, and congenital complications rather than quantified with MRX100-specific instruments.

## 4. Genetic and molecular information

**KIF4A** encodes an N-kinesin with an N-terminal ATP-dependent microtubule motor domain, central α-helical/coiled-coil stalk, and C-terminal cargo/regulatory tail. It functions in intracellular transport, chromosome condensation, spindle/midzone organization, cytokinesis, neuronal survival, morphology, and synaptic physiology. (willemsen2014involvementofthe pages 6-7, kalantari2021expandingthekif4a pages 1-2)

### Variant classes and interpretation

Reported classes include missense, essential splice-site, and complex splice-region indels. The founding allele has direct RNA/protein functional support. R728Q increases predicted coiled-coil probability from 0.45 to 0.92 and strengthens PARP1 binding in experimental assays. By contrast, the 10 missense and one splice variant in the 2021 series were all classified as **VUS under strict ACMG criteria**; individual ClinVar assertions may evolve and must be checked by variant, transcript, genome build, and review status. (kalantari2021expandingthekif4a pages 7-10, willemsen2014involvementofthe pages 3-4, wan2022kif4regulatesneuronal pages 2-4)

The variants are presumed or demonstrated **germline**, not somatic. No MRX100-specific somatic mosaic series, modifier gene, protective allele, reproducible epigenetic signature, repeat expansion, aneuploidy, or recurrent pathogenic translocation is established. Xq13.1 duplications involving KIF4A have been associated with a broader “floppy infant” phenotype, but dosage CNVs should not automatically be equated with sequence-variant MRX100. (liu2025kif4aindisease pages 9-10)

Population allele frequencies were not provided in the retrieved primary excerpts. A candidate disease allele should be absent or exceptionally rare in an ancestry-matched resource such as gnomAD, but database absence alone is not proof of pathogenicity.

## 5. Environmental information

MRX100 is a Mendelian neurodevelopmental disorder; no causal toxicant, radiation exposure, pollutant, occupational exposure, lifestyle behavior, or infectious agent has been identified. Environmental measures cannot prevent the inherited molecular lesion. General avoidance of seizure triggers and good prenatal/child health remain supportive practices, not disease-specific etiologic interventions.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A hemizygous damaging **KIF4A** variant **leads to** altered splicing/protein abundance or abnormal motor/regulatory protein behavior. The founding allele’s exon skipping and approximately 50% reduction are demonstrated; effects of many missense VUS remain inferred. (willemsen2014involvementofthe pages 3-4)
2. Altered KIF4A **leads to** disturbed microtubule-dependent cargo handling and/or nuclear chromokinesin regulation, including abnormal interaction with PARP1; this is demonstrated for R728Q and inferred for some other alleles. (willemsen2014involvementofthe pages 6-7, wan2022kif4regulatesneuronal pages 1-2)
3. **Branch A—developmental transport/cytoskeleton:** KIF4A dysfunction is inferred to disturb neuronal polarization, axon/dendrite formation, adhesion-cargo trafficking such as L1CAM, and synapse development, **resulting in** aberrant cortical organization and connectivity. (willemsen2014involvementofthe pages 6-7, kalantari2021expandingthekif4a pages 1-2)
4. **Branch B—PARP1 signaling:** R728Q strengthens KIF4–PARP1 binding and suppresses appropriate PARP1/PAR signaling, **leading to** increased TrkB, reduced KCC2, and abnormal neuronal chloride homeostasis. (wan2022kif4regulatesneuronal pages 5-7, wan2022kif4regulatesneuronal pages 1-2)
5. Reduced KCC2 and elevated intracellular chloride **lead to** impaired maturation of inhibitory GABAergic signaling, while KIF4A depletion independently alters miniature excitatory and inhibitory currents, **resulting in** excitation/inhibition imbalance. (willemsen2014involvementofthe pages 6-7, willemsen2014involvementofthe pages 4-6, wan2022kif4regulatesneuronal pages 13-15)
6. Circuit imbalance plus aberrant dendritic branching/spines **leads to** learning impairment, intellectual disability, anxiety-like behavior, and lower seizure threshold; this is demonstrated in mice and biologically consistent with human ID/epilepsy. (wan2022kif4regulatesneuronal pages 1-2, wan2022kif4regulatesneuronal pages 4-5)
7. **Branch C—cell division:** disruption of KIF4A–PRC1 spindle-midzone/cytokinesis functions may **contribute to** congenital brain and multi-organ anomalies, but normal mitosis in founding-family lymphocytes means this disease link remains incompletely demonstrated. (willemsen2014involvementofthe pages 6-7, kalantari2021expandingthekif4a pages 1-2)

### Molecular and cellular detail

In rat hippocampal neurons, Kif4a knockdown decreased mEPSC amplitude, increased mEPSC frequency, and decreased mIPSC frequency without changing mIPSC amplitude or current kinetics. This supports altered synapse number/release rather than a generalized postsynaptic receptor-composition defect. (willemsen2014involvementofthe pages 4-6)

R728Q mice had hyperbranched CA3 pyramidal neurons, abnormal dendritic spines, reduced KCC2 in hippocampus and motor cortex, and elevated intracellular chloride. NAD restored pathway activity and seizure susceptibility, supplying experimental—not clinical—causal support for the PARP1–TrkB–KCC2 branch. (wan2022kif4regulatesneuronal pages 5-7, wan2022kif4regulatesneuronal pages 1-2, wan2022kif4regulatesneuronal pages 28-31)

**Suggested GO biological processes:** microtubule-based movement **GO:0007018**; microtubule-based transport **GO:0099111**; chromosome segregation **GO:0007059**; cytokinesis **GO:0000910**; axon development **GO:0061564**; dendrite development **GO:0016358**; synapse organization **GO:0050808**; regulation of membrane potential **GO:0042391**; neuronal action-potential regulation and chloride transport. Suggested cellular components include microtubule cytoskeleton **GO:0015630**, spindle midzone **GO:0051233**, nucleus **GO:0005634**, axon **GO:0030424**, dendrite **GO:0030425**, and synapse **GO:0045202**.

**Suggested Cell Ontology terms:** neuron **CL:0000540**; pyramidal neuron **CL:0000598**; hippocampal neuron; cortical neuron **CL:0002609**; GABAergic neuron **CL:0000617**; glutamatergic neuron **CL:0000679**; neural progenitor cell **CL:0011020**; Schwann cell **CL:0002573**. Cell-type specificity in human MRX100 tissue has not been established by single-cell or spatial profiling.

No disease-specific human transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, single-cell, spatial-transcriptomic, organoid, or CRISPR-screen signature was identified. The mechanistic omics gap is substantial.

## 7. Anatomical structures affected

The **central nervous system**, especially cerebral cortex and hippocampal circuits, is primary. Suggested anatomy terms include brain **UBERON:0000955**, cerebral cortex **UBERON:0000956**, frontal cortex, hippocampal formation **UBERON:0002421**, lateral ventricle **UBERON:0002285**, and corticospinal/pyramidal tracts. Findings include cortical atrophy, shallow sulci/reduced gyri, polymicrogyria, heterotopia, ventriculomegaly/hydrocephalus, and hypoplastic pyramidal tracts. Disease lateralization is not established; bilateral polymicrogyria can occur. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 7-10, kalantari2021expandingthekif4a pages 6-6)

Secondary variable involvement includes eye/anterior segment, teeth, kidney/urinary tract, lymphatic system, hands/feet, and skeleton. Subcellular sites are nucleus/chromatin and spindle during division, plus neuronal microtubules, axons, dendrites, and synapses. (kalantari2021expandingthekif4a pages 7-10, willemsen2014involvementofthe pages 6-7, kalantari2021expandingthekif4a pages 1-2)

## 8. Temporal development and natural history

Onset is congenital/developmental but may first be recognized when milestones are delayed. Epilepsy ranges from infancy (6 months in a severe case) to late childhood/adolescence in the founding family. Intellectual and adaptive impairment appears chronic and lifelong. There is no validated staging system, remission pattern, or longitudinal natural-history curve. (willemsen2014involvementofthe pages 3-4)

Structural malformations arise prenatally, making corticogenesis a likely critical window. Synaptic maturation and childhood learning remain potential intervention windows, but this is biologically inferred rather than proven in patients. Available reports do not establish a progressive neurodegenerative course; “stable neurodevelopmental disability with variable epilepsy” is more defensible, while acknowledging inadequate longitudinal data.

## 9. Inheritance and population

Inheritance is principally **X-linked recessive**: hemizygous males are predominantly affected, while heterozygous females may be unaffected carriers or variably affected owing to X-inactivation or allele-specific effects. Maternal inheritance and at least one de novo event have been documented. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 6-6)

For a carrier mother, each pregnancy has a 50% probability of transmitting the allele; conventionally, each son has a 50% risk of being affected and each daughter a 50% risk of being a carrier, although female manifestations remain possible. Germline mosaicism cannot be excluded after an apparently de novo result. No anticipation, founder effect, population enrichment, carrier frequency, ethnic predisposition, or geographic concentration is established.

No prevalence or incidence estimate exists. Reported numbers are far too small and ascertainment-biased to calculate cases per 100,000. The observed male predominance follows X-linked biology, not a registry-derived sex ratio.

## 10. Diagnostics

### Clinical evaluation

Evaluate developmental history, adaptive and cognitive function, speech/language, neurologic examination, growth and head circumference, behavior/autism, dysmorphology, vision, hearing, dentition, limbs, and renal/urinary findings. EEG is indicated for seizures or suspicious episodes. Brain MRI is appropriate with epilepsy, microcephaly, abnormal examination, regression, or severe delay; imaging may be normal and therefore cannot exclude MRX100. (kalantari2021expandingthekif4a pages 6-6, kalantari2021expandingthekif4a pages 6-7, wan2022kif4regulatesneuronal pages 24-28)

There is no diagnostic blood metabolite, enzyme assay, pathology specimen, proteomic marker, or KIF4A-specific clinical criterion. Diagnosis requires compatible phenotype plus molecular evidence interpreted under ACMG/AMP rules.

### Genetic-testing strategy

1. **First-line:** trio exome or genome sequencing, or a comprehensive neurodevelopmental/XLID panel that includes **KIF4A**, with CNV calling.
2. **Confirmatory:** Sanger/orthogonal confirmation, maternal testing, segregation in informative relatives, and precise HGVS transcript/build annotation.
3. **Splice variants:** patient RNA analysis can demonstrate exon skipping; the founding allele shows the value of this approach. Protein studies or research functional assays may help reclassify VUS. (willemsen2014involvementofthe pages 2-3, willemsen2014involvementofthe pages 3-4)
4. **CMA:** useful for genome-wide CNVs and differential diagnosis, but does not reliably detect small KIF4A sequence variants.
5. **WGS:** useful for noncoding splice variants, structural variants, and exome-negative disease. Karyotype/FISH are not routine for a suspected small sequence variant unless a chromosomal rearrangement is suspected.
6. Mitochondrial DNA and repeat-expansion tests are not KIF4A-specific; use only when the broader phenotype warrants them.

### Differential diagnosis

Differentials include other XLID genes (**ARX, SLC9A6, CASK, MECP2, IQSEC2, HUWE1**), fragile X syndrome (**FMR1**), and kinesin/microtubule disorders such as **KIF1A, KIF2A, KIF5C, KIF11, KIF14, KIF21B, DYNC1H1, TUBA1A**, particularly when epilepsy or cortical malformation is prominent. The founding family had unrevealing karyotype, array, FMR1, ARX, and metabolic testing before KIF4A was identified. (willemsen2014involvementofthe pages 2-3)

Cascade testing is appropriate after a familial pathogenic/likely pathogenic variant is established. Population or newborn screening is not available.

## 11. Outcome and prognosis

There are no disease-specific survival curves, mortality rates, life-expectancy estimates, validated prognostic biomarkers, or quality-of-life scores. Adult affected males aged up to 53 years in the founding family show that survival into later adulthood is possible, but this does not define average life expectancy. (willemsen2014involvementofthe pages 2-3)

Long-term morbidity is driven by cognitive/adaptive disability, language impairment, dependence in daily living, epilepsy—including refractory epilepsy in some cases—and complications of major brain or congenital anomalies. Recovery to typical neurodevelopment is not reported. Prognosis likely correlates with developmental severity, seizure control, and burden of structural malformations, but sample sizes preclude validated prediction. (willemsen2014involvementofthe pages 3-4, kalantari2021expandingthekif4a pages 7-10, kalantari2021expandingthekif4a pages 6-6)

## 12. Treatment and current implementation

No KIF4A-directed treatment is approved, and no disease-specific interventional trial was identified. Current real-world care is multidisciplinary and phenotype-directed:

- early developmental and educational intervention;
- speech/language therapy, augmentative communication, occupational therapy, and physical therapy;
- standard antiseizure medication selected by seizure type, EEG, comorbidity, and adverse-effect profile; drug resistance warrants specialist epilepsy evaluation;
- behavioral/psychiatric and autism supports;
- treatment of hydrocephalus or other structural complications by relevant specialists;
- ophthalmologic, renal, dental, feeding/nutrition, and orthopedic care when indicated.

Suggested NCIt concepts include **Developmental Therapy**, **Speech and Language Therapy**, **Occupational Therapy**, **Physical Therapy**, **Anticonvulsant Therapy**, **Genetic Counseling**, and **Ventriculoperitoneal Shunt Procedure** where clinically indicated. Exact NCIt codes should be mapped against the current NCIt release.

The most specific experimental signal is **NAD supplementation/PARP1-pathway restoration** in R728Q mice, which rescued seizure susceptibility and aspects of neuronal morphology. It must not be extrapolated to human supplementation: optimal compound, dose, CNS exposure, developmental timing, long-term safety, and applicability across loss-of-function versus altered-binding alleles are unknown. (wan2022kif4regulatesneuronal pages 5-7, wan2022kif4regulatesneuronal pages 1-2, wan2022kif4regulatesneuronal pages 28-31)

Conversely, KIF4A inhibitors under oncology development are biologically inappropriate as presumptive MRX100 therapy and could worsen neuronal or mitotic function. A 2024 glioma study of WZ-3146 concerns tumor inhibition, not replacement of deficient KIF4A in neurodevelopmental disease. (liu2025researchprogressof pages 14-14)

## 13. Prevention

The condition cannot be prevented through vaccination, diet, lifestyle, or environmental remediation.

- **Primary prevention/family planning:** genetic counseling; carrier testing; preimplantation genetic testing for a known familial variant; prenatal diagnosis by chorionic-villus sampling or amniocentesis after informed consent.
- **Secondary prevention:** cascade testing and early molecular diagnosis can avoid a diagnostic odyssey and enable early developmental and epilepsy surveillance, but do not reverse prenatal malformation.
- **Tertiary prevention:** optimize seizure control, communication, mobility, nutrition, safety, education, and management of hydrocephalus or organ-specific anomalies.

Prenatal or preimplantation interpretation should be based on a pathogenic/likely pathogenic familial variant, not an unresolved VUS without careful counseling.

## 14. Other species and natural disease

KIF4A/Kif4a is evolutionarily conserved in vertebrates. Relevant laboratory taxa are **Homo sapiens (NCBI Taxon 9606), Mus musculus (10090), and Rattus norvegicus (10116)**. No well-established, naturally occurring KIF4A-associated veterinary syndrome, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was identified. This is a genetic intracellular-motor disorder and has no zoonotic potential.

Recent comparative work extends KIF4A biology beyond development. A 2023 rat/human-tissue preprint found adult neuronal and Schwann-cell expression; after peripheral nerve injury, DRG Kif4a rose approximately 2–2.7-fold and distal-stump expression approximately 12–13-fold at day 7, while proliferating Schwann cells expressed about sixfold more Kif4a mRNA than quiescent cells. This informs regeneration biology but does not establish an MRX100 treatment. (correia2023unexpectedkif4afunctions pages 2-5, correia2023unexpectedkif4afunctions pages 10-13)

A January 2024 rat stroke study found selective KIF4 re-expression in peri-infarct cortex at day 3, including NeuN-positive neurons, precursor cells, and glia. This supports an adult plasticity role but is not evidence about human MRX100 natural history. DOI: https://doi.org/10.1111/bpa.13232. (ruscu2024thepost‐strokeyoung pages 7-8)

## 15. Model organisms and experimental systems

### R728Q knock-in mouse

The principal disease-oriented model is a male **Kif4Mut/Y** mouse engineered for the human R728Q coiled-coil variant. It showed increased fetal demise (approximately 26% versus 7% in wild type), male underrepresentation (31% rather than the expected 50%), prenatal/postnatal growth restriction, smaller brain and hippocampus, delayed developmental milestones, impaired spatial/object memory and fear conditioning, anxiety-like behavior, abnormal CA3 dendrites/spines, altered chloride homeostasis, and enhanced PTZ seizure susceptibility. After PTZ, 11/15 mutants reached stage-5 seizures and three died; EEG power increased approximately tenfold. (wan2022kif4regulatesneuronal pages 4-5, wan2022kif4regulatesneuronal pages 2-4)

**Applications:** allele mechanism, PARP1–TrkB–KCC2 biology, chloride homeostasis, synaptic development, cognition, seizure threshold, and preclinical rescue. **Limitations:** it models one altered-binding missense allele, not the founding exon-skipping allele or all motor-domain VUS; PTZ-provoked seizures are not identical to spontaneous human epilepsy; murine developmental and X-inactivation biology differ from humans.

### Primary neuronal systems

Kif4a siRNA knockdown in primary rat hippocampal neurons provides a reduction-of-function model and demonstrates altered mEPSC/mIPSC properties. It is valuable for synaptic physiology but lacks human genetic background, cortical morphogenesis, systemic congenital phenotypes, and long-term behavior. (willemsen2014involvementofthe pages 3-4, willemsen2014involvementofthe pages 4-6)

### Injury/regeneration models

Rat sciatic-nerve crush/transection, cultured Schwann cells, and rat stroke models establish injury-induced KIF4A expression and glial/neuronal roles. They are relevant to general KIF4A biology but are not validated MRX100 phenocopies. (correia2023unexpectedkif4afunctions pages 2-5, correia2023unexpectedkif4afunctions pages 10-13, ruscu2024thepost‐strokeyoung pages 7-8)

No disease-specific zebrafish, Drosophila, *C. elegans*, human iPSC-neuron, cerebral-organoid, or humanized replacement model was identified in the retrieved literature. High-priority research needs are patient-derived iPSC cortical neurons/organoids, isogenic correction, quantitative motor/cargo assays, female X-inactivation studies, and direct comparison of truncating, splice, motor-domain, and coiled-coil alleles.

## Overall expert assessment

The **KIF4A–MRX100 relationship is credible**, supported by X-linked segregation, a functionally validated splice defect, recurrent rare variants in similarly affected males, neuronal electrophysiology, and an allele-specific mouse model. However, the disorder should currently be represented as a **KIF4A-related neurodevelopmental spectrum**, not a uniformly non-syndromic ID entity. The strongest clinical facts are developmental impairment, variable epilepsy, and variably abnormal brain structure; the strongest mechanistic evidence concerns synaptic excitation/inhibition and the allele-specific PARP1–TrkB–KCC2/chloride pathway. Variant-level assertions require caution because much of the expanded allelic series remained VUS, and no epidemiologic, natural-history, or therapeutic trial infrastructure yet exists. (kalantari2021expandingthekif4a pages 7-10, willemsen2014involvementofthe pages 3-4, willemsen2014involvementofthe pages 4-6, wan2022kif4regulatesneuronal pages 1-2)

References

1. (OpenTargets Search: intellectual disability, X-linked 100-KIF4A): Open Targets Query (intellectual disability, X-linked 100-KIF4A, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (willemsen2014involvementofthe pages 3-4): Marjolein H Willemsen, Wei Ba, Willemijn M Wissink-Lindhout, Arjan P M de Brouwer, Stefan A Haas, Melanie Bienek, Hao Hu, Lisenka E L M Vissers, Hans van Bokhoven, Vera Kalscheuer, Nael Nadif Kasri, and Tjitske Kleefstra. Involvement of the kinesin family members kif4a and kif5c in intellectual disability and synaptic function. Journal of Medical Genetics, 51:487-494, May 2014. URL: https://doi.org/10.1136/jmedgenet-2013-102182, doi:10.1136/jmedgenet-2013-102182. This article has 118 citations and is from a domain leading peer-reviewed journal.

3. (kalantari2021expandingthekif4a pages 7-10): Silvia Kalantari, Colleen Carlston, Norah Alsaleh, Ghada M. H. Abdel‐Salam, Fowzan Alkuraya, Mitsuhiro Kato, Naomichi Matsumoto, Satoko Miyatake, Tatsuya Yamamoto, Lucas Fares‐Taie, Jean‐Michel Rozet, Nicolas Chassaing, Catherine Vincent‐Delorme, Anjeung Kang‐Bellin, Kirsty McWalter, Caleb Bupp, Emily Palen, Monisa D. Wagner, Marcello Niceta, Claudia Cesario, Roberta Milone, Julie Kaplan, Erin Wadman, William B. Dobyns, and Isabel Filges. Expanding the kif4a ‐associated phenotype. American Journal of Medical Genetics. Part a, 185:3728-3739, Aug 2021. URL: https://doi.org/10.1002/ajmg.a.62443, doi:10.1002/ajmg.a.62443. This article has 20 citations and is from a peer-reviewed journal.

4. (willemsen2014involvementofthe pages 2-3): Marjolein H Willemsen, Wei Ba, Willemijn M Wissink-Lindhout, Arjan P M de Brouwer, Stefan A Haas, Melanie Bienek, Hao Hu, Lisenka E L M Vissers, Hans van Bokhoven, Vera Kalscheuer, Nael Nadif Kasri, and Tjitske Kleefstra. Involvement of the kinesin family members kif4a and kif5c in intellectual disability and synaptic function. Journal of Medical Genetics, 51:487-494, May 2014. URL: https://doi.org/10.1136/jmedgenet-2013-102182, doi:10.1136/jmedgenet-2013-102182. This article has 118 citations and is from a domain leading peer-reviewed journal.

5. (kalantari2021expandingthekif4a pages 6-6): Silvia Kalantari, Colleen Carlston, Norah Alsaleh, Ghada M. H. Abdel‐Salam, Fowzan Alkuraya, Mitsuhiro Kato, Naomichi Matsumoto, Satoko Miyatake, Tatsuya Yamamoto, Lucas Fares‐Taie, Jean‐Michel Rozet, Nicolas Chassaing, Catherine Vincent‐Delorme, Anjeung Kang‐Bellin, Kirsty McWalter, Caleb Bupp, Emily Palen, Monisa D. Wagner, Marcello Niceta, Claudia Cesario, Roberta Milone, Julie Kaplan, Erin Wadman, William B. Dobyns, and Isabel Filges. Expanding the kif4a ‐associated phenotype. American Journal of Medical Genetics. Part a, 185:3728-3739, Aug 2021. URL: https://doi.org/10.1002/ajmg.a.62443, doi:10.1002/ajmg.a.62443. This article has 20 citations and is from a peer-reviewed journal.

6. (kalantari2021expandingthekif4a pages 6-7): Silvia Kalantari, Colleen Carlston, Norah Alsaleh, Ghada M. H. Abdel‐Salam, Fowzan Alkuraya, Mitsuhiro Kato, Naomichi Matsumoto, Satoko Miyatake, Tatsuya Yamamoto, Lucas Fares‐Taie, Jean‐Michel Rozet, Nicolas Chassaing, Catherine Vincent‐Delorme, Anjeung Kang‐Bellin, Kirsty McWalter, Caleb Bupp, Emily Palen, Monisa D. Wagner, Marcello Niceta, Claudia Cesario, Roberta Milone, Julie Kaplan, Erin Wadman, William B. Dobyns, and Isabel Filges. Expanding the kif4a ‐associated phenotype. American Journal of Medical Genetics. Part a, 185:3728-3739, Aug 2021. URL: https://doi.org/10.1002/ajmg.a.62443, doi:10.1002/ajmg.a.62443. This article has 20 citations and is from a peer-reviewed journal.

7. (willemsen2014involvementofthe pages 6-7): Marjolein H Willemsen, Wei Ba, Willemijn M Wissink-Lindhout, Arjan P M de Brouwer, Stefan A Haas, Melanie Bienek, Hao Hu, Lisenka E L M Vissers, Hans van Bokhoven, Vera Kalscheuer, Nael Nadif Kasri, and Tjitske Kleefstra. Involvement of the kinesin family members kif4a and kif5c in intellectual disability and synaptic function. Journal of Medical Genetics, 51:487-494, May 2014. URL: https://doi.org/10.1136/jmedgenet-2013-102182, doi:10.1136/jmedgenet-2013-102182. This article has 118 citations and is from a domain leading peer-reviewed journal.

8. (willemsen2014involvementofthe pages 4-6): Marjolein H Willemsen, Wei Ba, Willemijn M Wissink-Lindhout, Arjan P M de Brouwer, Stefan A Haas, Melanie Bienek, Hao Hu, Lisenka E L M Vissers, Hans van Bokhoven, Vera Kalscheuer, Nael Nadif Kasri, and Tjitske Kleefstra. Involvement of the kinesin family members kif4a and kif5c in intellectual disability and synaptic function. Journal of Medical Genetics, 51:487-494, May 2014. URL: https://doi.org/10.1136/jmedgenet-2013-102182, doi:10.1136/jmedgenet-2013-102182. This article has 118 citations and is from a domain leading peer-reviewed journal.

9. (wan2022kif4regulatesneuronal pages 1-2): Yuansong Wan, Momo Morikawa, M. Morikawa, Suguru Iwata, M. Naseer, Adeel Gulzar Ahmed Chaudhary, Yosuke Tanaka, and N. Hirokawa. Kif4 regulates neuronal morphology and seizure susceptibility via the parp1 signaling pathway. The Journal of Cell Biology, Dec 2022. URL: https://doi.org/10.1083/jcb.202208108, doi:10.1083/jcb.202208108. This article has 18 citations.

10. (wan2022kif4regulatesneuronal pages 24-28): Yuansong Wan, Momo Morikawa, M. Morikawa, Suguru Iwata, M. Naseer, Adeel Gulzar Ahmed Chaudhary, Yosuke Tanaka, and N. Hirokawa. Kif4 regulates neuronal morphology and seizure susceptibility via the parp1 signaling pathway. The Journal of Cell Biology, Dec 2022. URL: https://doi.org/10.1083/jcb.202208108, doi:10.1083/jcb.202208108. This article has 18 citations.

11. (wan2022kif4regulatesneuronal pages 4-5): Yuansong Wan, Momo Morikawa, M. Morikawa, Suguru Iwata, M. Naseer, Adeel Gulzar Ahmed Chaudhary, Yosuke Tanaka, and N. Hirokawa. Kif4 regulates neuronal morphology and seizure susceptibility via the parp1 signaling pathway. The Journal of Cell Biology, Dec 2022. URL: https://doi.org/10.1083/jcb.202208108, doi:10.1083/jcb.202208108. This article has 18 citations.

12. (wan2022kif4regulatesneuronal pages 2-4): Yuansong Wan, Momo Morikawa, M. Morikawa, Suguru Iwata, M. Naseer, Adeel Gulzar Ahmed Chaudhary, Yosuke Tanaka, and N. Hirokawa. Kif4 regulates neuronal morphology and seizure susceptibility via the parp1 signaling pathway. The Journal of Cell Biology, Dec 2022. URL: https://doi.org/10.1083/jcb.202208108, doi:10.1083/jcb.202208108. This article has 18 citations.

13. (wan2022kif4regulatesneuronal pages 5-7): Yuansong Wan, Momo Morikawa, M. Morikawa, Suguru Iwata, M. Naseer, Adeel Gulzar Ahmed Chaudhary, Yosuke Tanaka, and N. Hirokawa. Kif4 regulates neuronal morphology and seizure susceptibility via the parp1 signaling pathway. The Journal of Cell Biology, Dec 2022. URL: https://doi.org/10.1083/jcb.202208108, doi:10.1083/jcb.202208108. This article has 18 citations.

14. (wan2022kif4regulatesneuronal pages 13-15): Yuansong Wan, Momo Morikawa, M. Morikawa, Suguru Iwata, M. Naseer, Adeel Gulzar Ahmed Chaudhary, Yosuke Tanaka, and N. Hirokawa. Kif4 regulates neuronal morphology and seizure susceptibility via the parp1 signaling pathway. The Journal of Cell Biology, Dec 2022. URL: https://doi.org/10.1083/jcb.202208108, doi:10.1083/jcb.202208108. This article has 18 citations.

15. (wan2022kif4regulatesneuronal pages 28-31): Yuansong Wan, Momo Morikawa, M. Morikawa, Suguru Iwata, M. Naseer, Adeel Gulzar Ahmed Chaudhary, Yosuke Tanaka, and N. Hirokawa. Kif4 regulates neuronal morphology and seizure susceptibility via the parp1 signaling pathway. The Journal of Cell Biology, Dec 2022. URL: https://doi.org/10.1083/jcb.202208108, doi:10.1083/jcb.202208108. This article has 18 citations.

16. (correia2023unexpectedkif4afunctions pages 2-5): Patrícia D. Correia, Bárbara M. de Sousa, Jesús Chato-Astrain, Joana P. Faria, Veronica Estrada, João B. Relvas, Hans W. Müller, Víctor Carriel, Frank Bosse, and Sandra I. Vieira. Unexpected kif4a functions in adult regeneration encompass a dual role in neurons and in proliferative repair schwann cells. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.21.541636, doi:10.1101/2023.05.21.541636. This article has 0 citations.

17. (correia2023unexpectedkif4afunctions pages 10-13): Patrícia D. Correia, Bárbara M. de Sousa, Jesús Chato-Astrain, Joana P. Faria, Veronica Estrada, João B. Relvas, Hans W. Müller, Víctor Carriel, Frank Bosse, and Sandra I. Vieira. Unexpected kif4a functions in adult regeneration encompass a dual role in neurons and in proliferative repair schwann cells. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.21.541636, doi:10.1101/2023.05.21.541636. This article has 0 citations.

18. (correia2023unexpectedkif4afunctions pages 5-7): Patrícia D. Correia, Bárbara M. de Sousa, Jesús Chato-Astrain, Joana P. Faria, Veronica Estrada, João B. Relvas, Hans W. Müller, Víctor Carriel, Frank Bosse, and Sandra I. Vieira. Unexpected kif4a functions in adult regeneration encompass a dual role in neurons and in proliferative repair schwann cells. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.21.541636, doi:10.1101/2023.05.21.541636. This article has 0 citations.

19. (correia2023unexpectedkif4afunctions pages 1-2): Patrícia D. Correia, Bárbara M. de Sousa, Jesús Chato-Astrain, Joana P. Faria, Veronica Estrada, João B. Relvas, Hans W. Müller, Víctor Carriel, Frank Bosse, and Sandra I. Vieira. Unexpected kif4a functions in adult regeneration encompass a dual role in neurons and in proliferative repair schwann cells. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.21.541636, doi:10.1101/2023.05.21.541636. This article has 0 citations.

20. (ruscu2024thepost‐strokeyoung pages 7-8): Mihai Ruscu, Bogdan Capitanescu, Paul Rupek, Thomas Dandekar, Eugen Radu, Dirk M. Hermann, and Aurel Popa‐Wagner. The post‐stroke young adult brain has limited capacity to re‐express the gene expression patterns seen during early postnatal brain development. Brain Pathology, Jan 2024. URL: https://doi.org/10.1111/bpa.13232, doi:10.1111/bpa.13232. This article has 5 citations and is from a domain leading peer-reviewed journal.

21. (willemsen2014involvementofthe pages 1-2): Marjolein H Willemsen, Wei Ba, Willemijn M Wissink-Lindhout, Arjan P M de Brouwer, Stefan A Haas, Melanie Bienek, Hao Hu, Lisenka E L M Vissers, Hans van Bokhoven, Vera Kalscheuer, Nael Nadif Kasri, and Tjitske Kleefstra. Involvement of the kinesin family members kif4a and kif5c in intellectual disability and synaptic function. Journal of Medical Genetics, 51:487-494, May 2014. URL: https://doi.org/10.1136/jmedgenet-2013-102182, doi:10.1136/jmedgenet-2013-102182. This article has 118 citations and is from a domain leading peer-reviewed journal.

22. (kalantari2021expandingthekif4a pages 1-2): Silvia Kalantari, Colleen Carlston, Norah Alsaleh, Ghada M. H. Abdel‐Salam, Fowzan Alkuraya, Mitsuhiro Kato, Naomichi Matsumoto, Satoko Miyatake, Tatsuya Yamamoto, Lucas Fares‐Taie, Jean‐Michel Rozet, Nicolas Chassaing, Catherine Vincent‐Delorme, Anjeung Kang‐Bellin, Kirsty McWalter, Caleb Bupp, Emily Palen, Monisa D. Wagner, Marcello Niceta, Claudia Cesario, Roberta Milone, Julie Kaplan, Erin Wadman, William B. Dobyns, and Isabel Filges. Expanding the kif4a ‐associated phenotype. American Journal of Medical Genetics. Part a, 185:3728-3739, Aug 2021. URL: https://doi.org/10.1002/ajmg.a.62443, doi:10.1002/ajmg.a.62443. This article has 20 citations and is from a peer-reviewed journal.

23. (liu2025kif4aindisease pages 9-10): Yi Liu, Yunhua Li, Chunrong Tang, Honghua Wen, Jingxian Tang, Gangwen Chen, and Yongkang Wu. Kif4a in disease pathogenesis and therapeutics: from molecular mechanisms to clinical translation. Biology Direct, Dec 2025. URL: https://doi.org/10.1186/s13062-025-00712-0, doi:10.1186/s13062-025-00712-0. This article has 3 citations and is from a peer-reviewed journal.

24. (liu2025researchprogressof pages 14-14): Shuyi Liu, Jialing Chen, Liping Shi, Yuan Deng, and Zhengbo Wang. Research progress of kinesin family in neurological diseases. Frontiers in Cellular Neuroscience, Sep 2025. URL: https://doi.org/10.3389/fncel.2025.1527305, doi:10.3389/fncel.2025.1527305. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](Intellectual_Disability_X-linked_100-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 2 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1083/jcb.202208108` (21 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010488` (4 mentions) - the report calls it "if available"; MONDO calls it **intellectual disability, X-linked 100**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0002609` (obsolete neuron of cerebral cortex) (1 mention) - replaced by `CL:0010012`