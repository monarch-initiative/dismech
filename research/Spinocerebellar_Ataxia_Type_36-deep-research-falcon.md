---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T13:17:36.552902'
end_time: '2026-09-02T13:27:52.330807'
duration_seconds: 615.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia Type 36
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 36
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0030529
    ontology_label: GO_0030529
    replaced_by: GO:1990904
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spinocerebellar_Ataxia_Type_36-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia Type 36
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 36** covering all of the
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
- **Disease Name:** Spinocerebellar Ataxia Type 36
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 36** covering all of the
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


# Spinocerebellar Ataxia Type 36 (SCA36): Disease-Characteristics Report

**Scope.** This synthesis prioritizes primary human evidence, supplemented by experimental models and recent 2023–2024 diagnostic literature. SCA36 remains exceptionally rare; consequently, many estimates derive from referral cohorts or pedigrees rather than population surveillance. “Not reported” below means that no disease-specific evidence was identified in the retrieved literature, not proof of absence.

## Executive summary

Spinocerebellar ataxia type 36 is a late-onset, slowly progressive, autosomal-dominant neurodegenerative disorder caused by a heterozygous **GGCCTG hexanucleotide repeat expansion in intron 1 of NOP56**. The defining syndrome is gait/truncal and limb ataxia with dysarthria, frequently accompanied by hyperreflexia, sensorineural hearing loss, and—usually later—lower-motor-neuron manifestations such as tongue or limb atrophy and fasciculations. Cognitive-affective abnormalities, tremor, sensory impairment, and ptosis occur in subsets. Hearing loss and tongue fasciculation are useful diagnostic clues but are not required. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 3-4, lam2023repeatexpansionsin pages 1-3)

The strongest mechanistic model is toxic gain of function from expanded repeat RNA, involving nuclear RNA foci and altered RNA-protein interactions, together with intron retention and translation of dipeptide-repeat proteins. A contribution from reduced NOP56 function remains possible but is not established as the principal human mechanism. There is currently **no approved disease-modifying treatment**; care is supportive and multidisciplinary. Repeat-targeting antisense oligonucleotides and transcriptional suppression have reduced molecular pathology only in preclinical systems. (lopez2022spinocerebellarataxia36 pages 3-5, quelleregaldie2022anop56zebrafish pages 1-2, mceachin2020chimericpeptidespecies pages 1-3, matsuzono2017antisenseoligonucleotidesreduce pages 1-2, furuta2019suppressionofthe pages 1-2)

The following table summarizes the principal evidence.

| Domain | Current evidence | Evidence type | Key quantitative detail | Caveat |
|---|---|---|---|---|
| Definition / identifier | Spinocerebellar ataxia type 36 (SCA36) is a late-onset autosomal dominant cerebellar ataxia caused by a NOP56 intron 1 hexanucleotide repeat expansion; MONDO: MONDO_0013594; common synonyms include Costa da Morte ataxia and Asidan ataxia. (OpenTargets Search: spinocerebellar ataxia type 36-NOP56, quelleregaldie2022anop56zebrafish pages 1-2, lam2023repeatexpansionsin pages 1-3) | Disease database + human cohort + review | Open Targets links SCA36 to **NOP56**; British paper screened 1257 hereditary ataxia patients and 7506 controls. (OpenTargets Search: spinocerebellar ataxia type 36-NOP56, lam2023repeatexpansionsin pages 1-3) | MONDO and disease-target association are database-level resources; clinical phenotype still derived from relatively small family-based cohorts. |
| Causal variant and repeat range | Causal lesion is a heterozygous **GGCCTG** repeat expansion in **intron 1 of NOP56**. Normal alleles are reported as **3–14** or **5–14** repeats; expanded alleles range from **~30 to 2500**, with many clinically typical alleles **650–2500** repeats; short pathogenic alleles of **25–31 repeat tracts** have also been reported. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 2-3, obayashi2015spinocerebellarataxiatype pages 7-9, lam2023repeatexpansionsin pages 1-3) | Primary human genetic studies + review | Han Chinese families: **650–2500 units**; Obayashi et al.: controls **5–14**, affected **25–31** repeat units; Lam 2023: expanded alleles **30–2500**, mostly **650–2500**. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 2-3, lam2023repeatexpansionsin pages 1-3) | Cross-study nomenclature differs because some studies estimate tract size by Southern blot while others infer smaller “short expansions” by RP-PCR/fragment analysis. |
| Hallmark phenotype / onset | Core phenotype is slowly progressive cerebellar ataxia, usually beginning with gait/truncal ataxia, with dysarthria, hyperreflexia, sensorineural hearing loss, and later upper/lower motor neuron involvement including tongue fasciculations/atrophy. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 3-4, lam2023repeatexpansionsin pages 1-3, lam2023repeatexpansionsin pages 3-4) | Primary human clinical cohorts | Mean age at onset: **44.8 ± 3.8 y** in Han Chinese families; **50.4 ± 7.2 y** in multinational cohort; British cohort mean **48.4 y** (range **28–62**). Frequencies in Obayashi et al.: hearing impairment **60%**, reduced vibration sense **52%**, lower motor neuron signs **28%**, postural tremor **28%**, ptosis **24%**, cognitive impairment **24%**. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 3-4, lam2023repeatexpansionsin pages 3-4) | Hearing loss and tongue fasciculation are not universal; British patients had a lower rate of hearing loss, so absence of these signs does not exclude SCA36. (lam2023repeatexpansionsin pages 1-3) |
| Epidemiology | SCA36 is rare globally but enriched in founder populations from western Japan and Galicia, Spain, and is also present in France, Taiwan/Han Chinese populations, the US, and White British families. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 4-5, lopez2022spinocerebellarataxia36 pages 2-3, lam2023repeatexpansionsin pages 1-3) | Primary human cohort studies + review | Reported proportions among ataxia cohorts: **6.3%** in Galicia, **1.9%** in France, **1.5%** in Japan, **0.6% (3/512)** in Han Chinese SCA pedigrees, **0.7% (4/577)** in a US undiagnosed ataxia cohort. British WGS study found **5 families / 7 patients** among **1257** hereditary ataxia patients. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 4-5, lopez2022spinocerebellarataxia36 pages 2-3, lam2023repeatexpansionsin pages 1-3) | Most figures are cohort proportions rather than population prevalence/incidence; true population-level prevalence remains uncertain. |
| Mechanism | Best-supported mechanism is toxic RNA gain-of-function with **sense RNA foci**, intron retention, and repeat translation into DPRs; RAN/canonical translation products include **poly(GP)**, **poly(PR)**, **poly(GL)** and **poly(WA)**, with disease-context-specific aggregation behavior. NOP56 loss of function may contribute but is less directly established in patients. (lopez2022spinocerebellarataxia36 pages 3-5, mceachin2020chimericpeptidespecies pages 1-3, matsuzono2017antisenseoligonucleotidesreduce pages 1-2, furuta2019suppressionofthe pages 1-2) | Human tissue + iPSC + cell + mouse + review | RNA foci reported in cerebrum, cerebellum, inferior olive, spinal cord, and temporal muscle; iPSC study reduced RNA-foci-positive cells to **~50%** after ASO treatment; Furuta et al. found RAN translation from GGCCTG direction was **rare** in Neuro2A cells, while McEachin et al. found **poly(GP)** and **poly(PR)** in patient tissue and showed poly(GP) is soluble in SCA36. (lopez2022spinocerebellarataxia36 pages 3-5, mceachin2020chimericpeptidespecies pages 1-3, matsuzono2017antisenseoligonucleotidesreduce pages 1-2, furuta2019suppressionofthe pages 1-2) | Relative contribution of RNA toxicity versus DPR toxicity versus haploinsufficiency remains unresolved; some mechanistic findings differ by model system. |
| Diagnostics | Standard molecular confirmation uses **repeat-primed PCR (RP-PCR)** and **Southern blot**; newer approaches include short-read WGS with repeat-expansion calling and long-read sequencing for direct sizing/haplotype resolution. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 4-5, lam2023repeatexpansionsin pages 1-3, rafehi2023detectionanddiscovery pages 1-2, stevanovski2022comprehensivegeneticdiagnosis pages 1-3) | Clinical molecular diagnostics + review + sequencing-method studies | RP-PCR identifies characteristic decremental/sawtooth peaks; Southern blot can detect long unstable alleles of roughly **8–15 kb** and short expansions of **~3.5 kb**; British study used ExpansionHunter on WGS and RP-PCR confirmation; long-read nanopore assays can genotype all known neuropathogenic STRs in one assay. (obayashi2015spinocerebellarataxiatype pages 4-5, lam2023repeatexpansionsin pages 1-3, rafehi2023detectionanddiscovery pages 1-2, stevanovski2022comprehensivegeneticdiagnosis pages 1-3) | WES is generally poor for direct repeat-expansion detection; WGS/long-read pipelines still require confirmatory review and are not yet uniformly available clinically. |
| Treatments | No approved disease-modifying therapy specific to SCA36. Current care is supportive/rehabilitative, while experimental strategies target toxic RNA or repeat transcription. (lopez2022spinocerebellarataxia36 pages 2-3, matsuzono2017antisenseoligonucleotidesreduce pages 1-2, furuta2019suppressionofthe pages 1-2) | Review + iPSC preclinical + cell preclinical | In patient iPSCs/iPSC-derived neurons, ENA ASOs targeting NOP56 pre-mRNA reduced RNA-foci-positive cells to **~50%**; one ASO reduced foci without lowering NOP56 mRNA. In cell models, **Supt4a** knockdown and **erythromycin** reduced RNA foci and cytotoxicity. (matsuzono2017antisenseoligonucleotidesreduce pages 1-2, furuta2019suppressionofthe pages 1-2) | Preclinical only; no SCA36-specific interventional efficacy trial was identified. Long-read diagnostic study **NCT06467175** is recruiting (**210** planned participants) for cerebellar ataxias broadly, not a therapeutic SCA36 trial. (NCT06467175 chunk 1) |
| Models | SCA36 has been studied in patient iPSCs/iPSC-derived neurons, Neuro2A and yeast/cell models of expanded repeats, transgenic mouse systems, and a zebrafish **nop56** loss-of-function model. (todd2020hexanucleotiderepeatexpansions pages 8-9, quelleregaldie2022anop56zebrafish pages 1-2, matsuzono2017antisenseoligonucleotidesreduce pages 1-2, furuta2019suppressionofthe pages 1-2) | Cellular + animal models | Zebrafish nop56 mutants showed **absence of cerebellum**, reduced spinal cord neurons, high CNS apoptosis, impaired movement, and death before **7 days post-fertilization**; mouse repeat models showed cerebellar degeneration with Purkinje cell loss; behavioral/pathology cohorts included up to **20** mice per genotype group in Todd et al. (todd2020hexanucleotiderepeatexpansions pages 16-17, quelleregaldie2022anop56zebrafish pages 1-2) | No single model captures the full human combination of late onset, slow progression, hearing loss, and motor neuron involvement; zebrafish model addresses loss-of-function more than repeat toxicity. |


*Table: This table condenses the main disease-level evidence for Spinocerebellar Ataxia Type 36 across genetics, phenotype, mechanism, diagnostics, treatment, and models. It is designed for direct embedding into a technical report and highlights both quantitative findings and major caveats.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Spinocerebellar ataxia type 36.
* **MONDO:** **MONDO:0013594**.
* **OMIM:** **614153** is commonly assigned to SCA36; **NOP56** is OMIM **614154**. Database releases should be checked before production ingestion.
* **Orphanet:** commonly represented under **ORPHA:276161**; verify against the current Orphanet release before committing the identifier.
* **MeSH:** no retrieved disease-specific MeSH descriptor; broader terms include *Spinocerebellar Ataxias* and *Cerebellar Ataxia* (ClinicalTrials.gov maps cerebellar ataxia to MeSH D002524).
* **ICD-10/ICD-11:** no uniquely retrieved SCA36-specific code. It is generally coded under hereditary/degenerative ataxia categories; local coding systems vary.
* **Causal target:** Open Targets associates MONDO:0013594 with **NOP56**, supported by literature including PMID **21683323** and **22492559**. (OpenTargets Search: spinocerebellar ataxia type 36-NOP56)

**Synonyms:** SCA36; NOP56-related spinocerebellar ataxia; **Costa da Morte ataxia**; **Asidan ataxia**. The two geographic names preceded recognition that the Spanish and Japanese syndromes shared the same molecular cause. (quelleregaldie2022anop56zebrafish pages 1-2, mceachin2020chimericpeptidespecies pages 1-3)

**Category and evidence granularity:** This is a Mendelian disease entity summarized from aggregated disease resources and family/cohort-level research. The cited clinical studies analyze individual participants, but the present report contains no EHR-derived patient-level record.

## 2. Etiology

### Causal and genetic factors

The primary cause is a **germline, heterozygous GGCCTG expansion in NOP56 intron 1**. Normal alleles have generally been reported as 3–14 or 5–14 repeats. Most classic expanded alleles contain approximately 650–2,500 repeats, although pathogenic short alleles around 25–31 repeat units have been reported. The lesion acts dominantly and exhibits somatic instability. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 2-3, lam2023repeatexpansionsin pages 1-3)

The canonical discovery study is Kobayashi et al., *American Journal of Human Genetics* (2011), PMID **21683323**. A related Spanish genetic study is represented by PMID **22492559**. Open Targets integrates these publications with ClinVar records including RCV000024102. (OpenTargets Search: spinocerebellar ataxia type 36-NOP56)

### Risk, modifiers, and protection

* **Established risk:** carrying the pathogenic expansion; an affected parent; ancestry from a founder population increases prior probability but is neither necessary nor sufficient.
* **Family history:** high-value evidence because inheritance is autosomal dominant, although apparently sporadic cases may occur through unrecognized late-onset disease or limited family information.
* **Repeat length:** short expansions may have later onset, but one comparison—57.3 years for short versus 49.4 years for long expansions—was not statistically significant (p=0.408). Repeat size is therefore not a validated individual prognostic biomarker. (obayashi2015spinocerebellarataxiatype pages 4-5)
* **Modifier genes/protective variants:** none validated for SCA36.
* **Environmental, lifestyle, occupational, toxic, or infectious risk factors:** none demonstrated as causal or penetrance-modifying.
* **Protective diet, exercise exposure, or medication:** none demonstrated to prevent molecular disease.
* **Gene–environment interaction:** no SCA36-specific interaction has been established. Exercise may preserve function in degenerative ataxia generally, but this is tertiary management rather than primary protection.

## 3. Phenotypes

The best quantified multinational series included 25 symptomatic individuals, with mean onset **50.4±7.2 years** (range 39–65). Progressive cerebellar ataxia was universal. Hearing impairment occurred in 60%, reduced vibration sense in 52%, lower-motor-neuron signs in 28%, postural tremor in 28%, ptosis in 24%, and cognitive impairment in 24%; peripheral nerve abnormalities were detected in 32% of tested patients. These percentages should not be treated as universal because ascertainment, ancestry, and disease duration differ among studies. (obayashi2015spinocerebellarataxiatype pages 3-4)

| Phenotype | Type/course and frequency | Suggested HPO term |
|---|---|---|
| Gait/truncal ataxia | Usually presenting sign; progressive, typically universal | **HP:0002066 Cerebellar ataxia**, **HP:0001288 Gait disturbance** |
| Limb ataxia/dysmetria | Common, progressive | **HP:0002070 Limb ataxia**, **HP:0001310 Dysmetria** |
| Dysarthria | Common cerebellar sign | **HP:0001260 Dysarthria** |
| Abnormal ocular movements | Variable; impaired pursuit/overshoot described | **HP:0000496 Abnormality of eye movement** |
| Hyperreflexia/pyramidal signs | Common; one review reports hyperreflexia in 79% | **HP:0001347 Hyperreflexia** |
| Sensorineural hearing impairment | Often high-frequency; 60% in one multinational cohort, lower in British series | **HP:0000407 Sensorineural hearing impairment** |
| Tongue/limb atrophy and fasciculations | Usually later with prolonged disease; 28% lower-motor-neuron signs in one cohort | **HP:0003473 Lower motor neuron dysfunction**, **HP:0001308 Tongue fasciculations**, **HP:0002460 Distal muscle weakness** |
| Reduced vibration sensation/neuropathy | 52% reduced vibration; abnormal sensory potentials in 32% tested | **HP:0002495 Impaired vibratory sensation**, **HP:0009830 Peripheral neuropathy** |
| Tremor | Postural tremor 28% | **HP:0002173 Postural tremor** |
| Cognitive-affective impairment | Cognitive impairment 24%; frontal-executive/cerebellar cognitive-affective changes reported | **HP:0100543 Cognitive impairment** |
| Ptosis | 24% in one cohort | **HP:0000508 Ptosis** |
| Cerebellar atrophy | MRI abnormality; 100% of 14 examined in one series | **HP:0001272 Cerebellar atrophy** |

Human cohort evidence supports mean onset **44.8±3.8 years** in Taiwanese Han Chinese families, with truncal ataxia first; the 2023 British series found mean onset **48.4 years** (range 28–62). (lee2016spinocerebellarataxiatype pages 1-2, lam2023repeatexpansionsin pages 3-4)

**Quality of life.** No SCA36-specific EQ-5D, SF-36, or PROMIS dataset was retrieved. Clinically, progressive gait impairment, falls risk, dysarthria, hearing loss, and weakness affect mobility, communication, employment, and independence. This impact is strongly plausible but has not been adequately quantified with disease-specific patient-reported outcomes.

## 4. Genetic and molecular information

**Gene:** **NOP56** (HGNC:15911; Ensembl ENSG00000101361), encoding a 594-amino-acid nucleolar ribonucleoprotein. It is a core scaffold of the box C/D small nucleolar RNP complex, which participates in pre-rRNA processing, 2′-O-ribose methylation, and 60S ribosomal-subunit assembly. (OpenTargets Search: spinocerebellar ataxia type 36-NOP56, lopez2022spinocerebellarataxia36 pages 3-5, quelleregaldie2022anop56zebrafish pages 1-2)

**Variant representation:** the expansion is often described as **(GGCCTG)n**, alternatively strand-oriented as TGGGCC/TG3C2. Precise HGVS description is technically difficult because expanded length and somatic mosaicism vary. It is a noncoding tandem-repeat expansion rather than a missense, nonsense, or conventional structural deletion.

**Classification:** a sufficiently expanded allele segregating with the characteristic phenotype is pathogenic. Classic very large expansions and reported short pathogenic expansions require laboratory interpretation using assay-specific thresholds, segregation, phenotype, and orthogonal confirmation. The expansion is germline; tissue-dependent repeat-size heterogeneity is somatic instability, not a primary somatic disease.

**Population frequency:** expansions were absent from 727 controls in one multinational study and from 323 Taiwanese controls; no reliable gnomAD allele frequency is available because conventional short-read population databases poorly genotype very large repeats. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 2-3)

**Functional consequence:** toxic RNA/protein gain of function is best supported. Human lymphoblastoid studies did not consistently show reduced NOP56 protein, arguing against simple haploinsufficiency, although patient iPSCs and neurons showed lower NOP56 mRNA and loss of function remains a possible contributor. (lopez2022spinocerebellarataxia36 pages 3-5, quelleregaldie2022anop56zebrafish pages 1-2, matsuzono2017antisenseoligonucleotidesreduce pages 1-2)

**Modifiers, epigenetics, chromosomal abnormalities:** no validated modifier gene, disease-specific methylation signature, aneuploidy, translocation, inversion, or pathogenic copy-number change is established. A 2023 British study identified a shared 72.2–87-kb haplotype and estimated a founder mutation age of 31.7 generations (95% CI 16.9–60), but the haplotype also occurred in controls, suggesting a permissive background rather than a fully penetrant modifier. (lam2023repeatexpansionsin pages 1-3, lam2023repeatexpansionsin pages 3-4)

## 5. Environmental information

SCA36 is not an infectious, toxic, radiation-induced, or occupational disease. No smoking, alcohol, diet, pollution, or pathogen association has been demonstrated. Acquired causes of ataxia—alcohol/toxins, vitamin deficiencies, immune-mediated ataxia, infection, neoplasm, and medication effects—remain clinically important differential diagnoses but do not explain genetically confirmed SCA36.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline heterozygous **NOP56 intron-1 GGCCTG expansion leads to** transcription of a very long, unstable GGCCUG-containing pre-mRNA. (lopez2022spinocerebellarataxia36 pages 3-5, lam2023repeatexpansionsin pages 1-3)
2. Expanded repeat RNA **leads to** abnormal secondary structure, intron retention, and nuclear RNA-foci formation in vulnerable neural cells; RNA foci are demonstrated in human tissue and patient-derived cells. (lopez2022spinocerebellarataxia36 pages 3-5, mceachin2020chimericpeptidespecies pages 1-3, matsuzono2017antisenseoligonucleotidesreduce pages 1-2)
3. RNA foci **lead to, or are inferred to lead to,** sequestration/dysregulation of RNA-binding proteins, including reported SRSF2 interaction, thereby disturbing RNA processing. The downstream transcript-wide consequences remain incompletely mapped. (lopez2022spinocerebellarataxia36 pages 3-5)
4. **Branch A:** repeat-containing RNA **leads to** unconventional RAN translation and, for poly(GP), canonical upstream-AUG/intron-retention-dependent translation, producing DPR species including poly(GP), poly(PR), poly(GL), and poly(WA). (mceachin2020chimericpeptidespecies pages 1-3)
5. DPR production **results in** soluble or aggregate-prone peptide species and cellular stress; poly(GP) is unusually soluble in SCA36 tissue, and the precise toxic DPR species remain unresolved. (todd2020hexanucleotiderepeatexpansions pages 8-9, mceachin2020chimericpeptidespecies pages 1-3)
6. **Branch B:** altered NOP56 expression/function **may lead to** impaired box C/D snoRNP activity, rRNA processing, ribosome biogenesis, and cell-cycle/homeostatic defects; this is biologically plausible and strong in knockout models but not demonstrated as the dominant patient mechanism. (quelleregaldie2022anop56zebrafish pages 1-2, matsuzono2017antisenseoligonucleotidesreduce pages 1-2)
7. RNA/protein toxicity, and possibly partial NOP56 dysfunction, **lead to** cellular dysfunction and death in Purkinje cells, inferior-olivary neurons, brainstem/hypoglossal motor neurons, and spinal motor systems. (lopez2022spinocerebellarataxia36 pages 3-5, obayashi2015spinocerebellarataxiatype pages 4-5, todd2020hexanucleotiderepeatexpansions pages 8-9)
8. Selective neuronal degeneration **results in** cerebellar atrophy and progressive gait/limb ataxia; motor-neuron injury **results in** fasciculation and atrophy; auditory-system involvement **results in** sensorineural hearing loss. (obayashi2015spinocerebellarataxiatype pages 3-4, obayashi2015spinocerebellarataxiatype pages 4-5)

### Mechanistic detail and evidence grading

**Human tissue:** RNA foci occur in cerebrum, cerebellum, inferior olive, spinal cord, and temporal muscle, with particularly large foci in Purkinje and inferior-olivary neurons. Neuropathology shows mild Purkinje-cell loss, Bergmann gliosis, distorted dendrites, Purkinje “torpedoes,” and mild hypoglossal neuronal loss; ubiquitin, TDP-43, FUS, and p62 inclusions were absent in the examined case. (lopez2022spinocerebellarataxia36 pages 3-5, obayashi2015spinocerebellarataxiatype pages 4-5)

**Human iPSC evidence:** three SCA36 and three control clones were differentiated into neurons. Patient cells recapitulated RNA foci and showed lower NOP56 mRNA. The authors reported: **“Treatment … targeting NOP56 pre-mRNA reduced RNA-foci-positive cells to 50% in patient iPSCs and iPSC-derived neurons.”** One ASO reduced foci without lowering NOP56 mRNA, supporting RNA toxicity as a tractable mechanism. (matsuzono2017antisenseoligonucleotidesreduce pages 1-2, matsuzono2017antisenseoligonucleotidesreduce pages 6-7)

**DPR evidence:** McEachin et al. stated: **“the similar intronic GGCCTG HREs that causes … SCA36 is also translated into DPRs, including poly(GP) and poly(PR).”** Poly(GP) was more abundant but soluble in SCA36 tissue, while TDP-43 pathology was absent. This indicates that DPR presence does not automatically imply the aggregation pattern seen in C9ORF72 ALS/FTD. (mceachin2020chimericpeptidespecies pages 1-3)

**Mouse evidence:** transient/transgenic repeat-expression models develop selective cerebellar degeneration and Purkinje-cell loss. Poly(PR) was detected in human granule cells but not robustly in one SCA36 mouse model, showing that model-specific DPR expression limits causal inference. (todd2020hexanucleotiderepeatexpansions pages 8-9, todd2020hexanucleotiderepeatexpansions pages 16-17)

**Suggested annotations:** biological processes—**GO:0006364 rRNA processing**, **GO:0006396 RNA processing**, **GO:0006412 translation**, **GO:0006915 apoptotic process**, **GO:0008219 cell death**, and **GO:0048856 anatomical structure development**. Cell types—**CL:0000121 Purkinje cell**, **CL:0000100 motor neuron**, neuron, and astrocyte/Bergmann glial annotations. Subcellular compartments—**GO:0005730 nucleolus**, **GO:0005634 nucleus**, **GO:0030529 intracellular ribonucleoprotein complex**, and **GO:0005840 ribosome**.

No disease-specific metabolomic, lipidomic, proteomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature has been validated. RNA-seq was used to characterize iPSC clones, but not to establish a clinical molecular signature. (matsuzono2017antisenseoligonucleotidesreduce pages 1-2)

## 7. Anatomical structures affected

The primary system is the nervous system. The **cerebellum**—vermis and hemispheres—is central; MRI showed cerebellar atrophy in all 14 examined participants in one study, with brainstem atrophy in 28.6% and cerebral atrophy in 14.3%. FDG-PET abnormalities may precede symptoms and progress from vermis/right cerebellum toward hemispheres and brainstem, but PET is not a validated screening biomarker. (lopez2022spinocerebellarataxia36 pages 3-5, obayashi2015spinocerebellarataxiatype pages 3-4)

Other affected structures include the inferior olivary nucleus, hypoglossal nucleus, spinal cord/motor system, peripheral sensory nerves, auditory pathways, tongue, and limb skeletal muscle secondary to denervation. Disease is generally bilateral/systemic rather than unilateral. (lopez2022spinocerebellarataxia36 pages 3-5, obayashi2015spinocerebellarataxiatype pages 4-5)

**Suggested anatomy terms:** cerebellum **UBERON:0002037**; cerebellar cortex **UBERON:0002129**; Purkinje cell layer **UBERON:0002956**; brainstem **UBERON:0002298**; spinal cord **UBERON:0002240**; tongue **UBERON:0001723**; skeletal muscle tissue **UBERON:0001134**.

## 8. Temporal development

Onset is usually insidious in the fifth to sixth decade, although the British range extended from 28 to 62 years. Initial gait/truncal ataxia slowly expands to limb incoordination and dysarthria; auditory and pyramidal manifestations may coexist, whereas lower-motor-neuron signs become more evident with longer duration. (lee2016spinocerebellarataxiatype pages 1-2, lam2023repeatexpansionsin pages 1-3, lam2023repeatexpansionsin pages 3-4)

The course is chronic, lifelong, and progressive rather than episodic or relapsing. In the British series, duration was 9–29 years and all patients retained mobility at least nine years after onset; a patient with 29 years of disease continued walking. A fastest reported interval to wheelchair dependence was five years, demonstrating occasional faster progression. (lam2023repeatexpansionsin pages 1-3, lam2023repeatexpansionsin pages 3-4)

No spontaneous remission is expected. Preclinical PET changes in asymptomatic carriers suggest a presymptomatic biological phase and a potential future intervention window, but neither PET screening nor presymptomatic treatment has been validated. (lopez2022spinocerebellarataxia36 pages 3-5)

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Each child of a heterozygous affected individual has a theoretical 50% chance of inheriting the expansion. Penetrance appears strongly age dependent; precise lifetime penetrance has not been estimated. Expressivity is variable, particularly for hearing loss, cognition, neuropathy, and motor-neuron involvement. (obayashi2015spinocerebellarataxiatype pages 2-3, lam2023repeatexpansionsin pages 1-3)

Anticipation has been described clinically, but massive repeat size, somatic mosaicism, and assay limitations prevent a robust expansion-size/onset model. Three reported short-expansion cases were maternally transmitted, but evidence is insufficient to establish a general parent-of-origin rule. Germline mosaicism and carrier frequency have not been quantified. Consanguinity is not etiologically relevant to this dominant disorder. (obayashi2015spinocerebellarataxiatype pages 3-4, lopez2022spinocerebellarataxia36 pages 2-3, obayashi2015spinocerebellarataxiatype pages 7-9)

Founder effects are documented in Galicia, western Japan, Han Chinese/Taiwanese families, and possibly Britain. Three Taiwanese pedigrees shared a 5.3-kb haplotype. In Britain, five unrelated families shared a 72.2–87-kb region around NOP56. (lee2016spinocerebellarataxiatype pages 1-2, lam2023repeatexpansionsin pages 1-3, lam2023repeatexpansionsin pages 3-4)

Reported proportions among selected ataxia cohorts are 6.3% in Galicia, 1.9% in France, 1.5% in Japan, 0.6% (3/512 pedigrees) in Han Chinese SCA, and 0.7% (4/577 index cases) in a US undiagnosed-ataxia cohort. The 2023 British study found five families/seven patients among 1,257 hereditary-ataxia patients. These are **not incidence or general-population prevalence estimates**. Sex-specific risk has not been demonstrated. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 4-5, lopez2022spinocerebellarataxia36 pages 2-3, lam2023repeatexpansionsin pages 1-3)

## 10. Diagnostics

### Recommended workflow

1. **Clinical assessment:** document three-generation pedigree; onset and progression; gait, limb, ocular, speech, pyramidal and lower-motor-neuron signs; cognition; hearing; sensory neuropathy; and acquired exposures.
2. **Exclude treatable acquired ataxias:** basic metabolic, nutritional, immune/paraneoplastic, toxic, infectious, and structural evaluation tailored to presentation.
3. **MRI brain:** look for predominantly cerebellar atrophy; a normal early MRI does not molecularly exclude disease.
4. **Audiology:** pure-tone testing, especially high frequencies; useful phenotyping, not diagnostic.
5. **Electrophysiology:** EMG/nerve-conduction testing when fasciculation, weakness, atrophy, or sensory loss is present.
6. **Molecular testing:** use a repeat-expansion panel or NOP56-specific **repeat-primed PCR (RP-PCR)**. A characteristic 6-bp sawtooth/decremental peak pattern supports expansion.
7. **Orthogonal characterization:** Southern blot estimates very large and mosaic alleles; long-range PCR may characterize short expansions. Segregation testing strengthens interpretation.
8. **Genome approaches:** short-read WGS with ExpansionHunter or comparable callers can screen the locus, but manual review and molecular confirmation remain advisable. Long-read WGS/targeted nanopore sequencing can directly span, size, phase, and assess methylation of complex expansions. (obayashi2015spinocerebellarataxiatype pages 4-5, lee2016spinocerebellarataxiatype pages 2-3, lam2023repeatexpansionsin pages 1-3, lam2023repeatexpansionsin pages 3-4, rafehi2023detectionanddiscovery pages 1-2, stevanovski2022comprehensivegeneticdiagnosis pages 1-3)

The 2023 review states that the current gold standard remains **“repeat-primed PCR assays or Southern blots, neither of which are scalable nor readily available for all STR loci.”** WGS repeat-calling is increasingly practical, while long-read sequencing is the likely future comprehensive assay. (rafehi2023detectionanddiscovery pages 1-2)

**WES:** generally unsuitable for directly detecting this deep intronic expansion. Apparent exome-based clues require dedicated confirmation. **CMA, karyotype, FISH, and mitochondrial testing** do not diagnose the repeat and are reserved for alternative hypotheses. No blood, CSF, enzyme, transcriptomic, proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic biomarker is validated.

### Differential diagnosis

Important genetic alternatives include SCA1/2/3/6/7/8/10/12/17/31, SCA27B/FGF14, SCA4/ZFHX3, DRPLA, RFC1-CANVAS, Friedreich ataxia, FXTAS, and other dominant ataxias. Motor-neuron disease with ataxia raises C9ORF72 ALS/FTD and ATXN2-associated disease; preserved swallowing and slowly progressive cerebellar disease may favor SCA36 over classic ALS. Multiple-system atrophy–cerebellar type is usually sporadic and accompanied by prominent autonomic failure. Acquired immune, toxic, nutritional, infectious, neoplastic, and structural causes must also be excluded.

### Screening

There is no newborn or population screening. **Cascade testing** is appropriate after a familial expansion is identified. Predictive testing of asymptomatic adults should occur with genetic counseling and informed consent. Prenatal diagnosis and preimplantation genetic testing are technically possible when the familial expansion and laboratory method are established.

## 11. Outcome and prognosis

SCA36 causes progressive neurological disability but generally advances more slowly than aggressive motor-neuron disease. Long-term morbidity includes falls, impaired ambulation, dysarthria, hearing-related communication difficulty, tremor, sensory loss, muscle wasting, and eventual dependence. (lee2016spinocerebellarataxiatype pages 1-2, obayashi2015spinocerebellarataxiatype pages 3-4, lam2023repeatexpansionsin pages 3-4)

Disease-specific five- or ten-year survival, mortality rates, and treatment-adjusted life expectancy have not been established. Deaths in the British series after shorter observed durations were reported as unrelated to SCA36. Aspiration, immobility, falls, and respiratory weakness are clinically plausible late complications, but SCA36-specific rates are unavailable. Recovery of lost neurons is not expected; rehabilitation can preserve function and safety.

Potential prognostic factors include age at onset, baseline ataxia severity, disease duration, and emergence of motor-neuron involvement. Repeat length is not sufficiently validated for individual prediction. No accepted molecular prognostic biomarker exists.

## 12. Treatment

### Current clinical management

No drug, gene therapy, RNA therapy, cell therapy, surgery, or immunotherapy is approved to alter SCA36 progression. Management should be coordinated by neurology/ataxia specialists:

* physical therapy, balance and gait training, home-safety assessment, walking aids, and fall prevention;
* occupational therapy and adaptive equipment;
* speech-language therapy and communication aids;
* swallow evaluation if dysphagia develops, with nutritional support as needed;
* audiology and hearing aids/cochlear evaluation where appropriate;
* EMG-guided assessment and respiratory monitoring when motor-neuron weakness is substantial;
* symptomatic treatment of tremor, spasticity, cramps, mood, sleep, pain, and bladder symptoms using standard individualized practice;
* genetic counseling and psychosocial support.

Suggested NCIT intervention concepts include **Physical Therapy (C15308)**, **Occupational Therapy**, **Speech Therapy**, **Genetic Counseling (C15241)**, **Hearing Aid**, and **Assistive Device**; terminology/version should be validated against the current NCIT release.

### Experimental therapies

**Antisense oligonucleotides:** ENA-modified ASOs reduced RNA-foci-positive cells to approximately 50% in SCA36 iPSCs and derived neurons; one candidate did so without further lowering NOP56 mRNA. This is proof of molecular target engagement, not clinical efficacy. (matsuzono2017antisenseoligonucleotidesreduce pages 1-2, matsuzono2017antisenseoligonucleotidesreduce pages 6-7)

**Transcription/RNA-pathway modulation:** Supt4a knockdown and erythromycin reduced repeat RNA, foci/DPR production, and cytotoxicity in Neuro2A models. Erythromycin is not an established SCA36 therapy and should not be used off-label on this evidence. (furuta2019suppressionofthe pages 1-2)

**DPR targeting:** repeat-targeting ASOs robustly reduced poly(GP) in experimental systems, but uncertainty over the pathogenic DPR species and CNS delivery remains. (mceachin2020chimericpeptidespecies pages 1-3)

No SCA36-specific therapeutic trial was identified. **NCT06467175 (ALICA)** is a recruiting diagnostic study—not treatment—planning 210 participants with unresolved cerebellar ataxia to assess Oxford Nanopore long-read genome sequencing after nondiagnostic short-read GS. It began December 11, 2024; estimated completion is June 2028. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT06467175. (NCT06467175 chunk 1)

## 13. Prevention

Primary prevention through lifestyle modification or vaccination is not applicable to a germline dominant expansion. Reproductive risk reduction may include informed family planning, donor gametes, prenatal diagnosis, or preimplantation genetic testing after nondirective counseling.

Secondary prevention consists of cascade identification of at-risk relatives, predictive testing of consenting adults, baseline neurologic/audiologic assessment, and early rehabilitation. There is no evidence supporting presymptomatic medication.

Tertiary prevention includes fall reduction, exercise within safe limits, hearing rehabilitation, aspiration surveillance, mobility maintenance, vaccination according to general recommendations, and prompt management of respiratory or nutritional complications. No prophylactic drug is established.

## 14. Other species and natural disease

No naturally occurring SCA36-equivalent veterinary disorder or zoonotic transmission was identified. SCA36 is not infectious and has no zoonotic potential. **NOP56 is evolutionarily conserved**; zebrafish nop56 has approximately 70% homology to the human gene, supporting comparative functional studies. (quelleregaldie2022anop56zebrafish pages 1-2)

Relevant experimental taxa include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), *Danio rerio* (7955), and *Saccharomyces cerevisiae* (4932). Specific ortholog NCBI Gene IDs and VBO breed terms should be drawn directly from current organism databases during knowledge-base loading; no breed-specific natural disease applies.

## 15. Model organisms and experimental systems

### Patient-derived cells

SCA36 iPSCs and iPSC-derived neurons reproduce repeat retention and RNA foci and permit ASO testing. Their advantages are patient genotype and human neuronal context; limitations include immature cellular age, short culture duration, and incomplete modeling of decades-long cerebellar degeneration. (matsuzono2017antisenseoligonucleotidesreduce pages 1-2, matsuzono2017antisenseoligonucleotidesreduce pages 6-7)

### Neuro2A/cellular repeat-expression models

Expanded GGCCTG constructs produce predominantly nuclear **sense** GGCCUG foci and cytotoxicity. RAN translation was rare in one construct system, whereas human tissue showed multiple DPRs, illustrating dependence on genomic context, repeat length, intron retention, and upstream initiation sequences. These models are useful for high-throughput mechanistic and therapeutic screening but do not capture anatomy or natural expression. (mceachin2020chimericpeptidespecies pages 1-3, furuta2019suppressionofthe pages 1-2)

### Mouse

Transient/transgenic TG3C2 repeat-expression mice model RNA foci, DPR biology, gliosis, Purkinje-cell loss, and cerebellar degeneration. Todd et al. used behavioral cohorts of roughly 12–20 animals per genotype at selected ages and pathological groups of approximately 5–8. Limitations include artificial expression, incomplete motor-neuron/hearing phenotype, and failure to reproduce all human DPR pathology. (todd2020hexanucleotiderepeatexpansions pages 8-9, todd2020hexanucleotiderepeatexpansions pages 16-17)

### Zebrafish loss-of-function model

The 2022 nop56 mutant showed absent cerebellum, reduced spinal neurons, extensive CNS apoptosis, impaired movement, altered expression of C/D-box and CNS-development genes, and death before seven days post-fertilization. The abstract states: **“We observed a severe neurodegenerative phenotype … resulting in death before 7 days post-fertilization.”** This strongly demonstrates that Nop56 is essential for neural development, but the severe embryonic knockout is not a faithful model of heterozygous, late-onset repeat toxicity. DOI: https://doi.org/10.3390/biomedicines10081814; published July 28, 2022. (quelleregaldie2022anop56zebrafish pages 1-2)

### Yeast and Drosophila

Yeast/Spt4-related systems and repeat-transfected cells support transcriptional-modifier screening. Drosophila Nop56 perturbation causes optic-lobe/cell-cycle defects, informing conserved NOP56 biology rather than faithfully reproducing SCA36. (quelleregaldie2022anop56zebrafish pages 1-2, furuta2019suppressionofthe pages 1-2)

## Recent developments and expert assessment

The most important recent disease-specific development is the **2023 demonstration of SCA36 in White British families**. Analysis of 1,257 hereditary-ataxia patients and 7,506 controls found pathogenic expansions in five families/seven patients and showed that disease should be considered even without hearing loss or tongue fasciculation. DOI: https://doi.org/10.1093/braincomms/fcad244; advance publication September 14, 2023. (lam2023repeatexpansionsin pages 1-3, lam2023repeatexpansionsin pages 3-4)

The broader 2023–2024 diagnostic consensus is that repeat-expansion testing must be integrated with genome analysis: RP-PCR/Southern blot remain reference methods, short-read WGS can efficiently screen known loci, and long-read sequencing offers direct sizing, phasing, interruption detection, and methylation analysis. The recruiting ALICA study is evaluating whether long-read GS can serve as a real-world second-line diagnostic test. (NCT06467175 chunk 1, rudaks2024anupdateon pages 14-15, rafehi2023detectionanddiscovery pages 1-2, stevanovski2022comprehensivegeneticdiagnosis pages 1-3)

Expert interpretation should remain cautious in three areas. First, short and classic massive expansions complicate a single universal pathogenic cutoff. Second, hearing loss and motor-neuron signs are neither necessary nor uniformly early. Third, RNA foci, DPR production, and partial NOP56 deficiency may coexist; current evidence does not establish which downstream lesion is necessary and sufficient for human neurodegeneration. (obayashi2015spinocerebellarataxiatype pages 2-3, mceachin2020chimericpeptidespecies pages 1-3, matsuzono2017antisenseoligonucleotidesreduce pages 1-2, lam2023repeatexpansionsin pages 1-3)

## Key evidence gaps

Population incidence and prevalence per 100,000, lifetime penetrance, sex effects, longitudinal SARA progression, survival, respiratory and aspiration complication rates, validated fluid/imaging biomarkers, patient-reported quality of life, modifier genes, epigenetic signatures, single-cell/spatial omics, natural veterinary disease, and treatment response rates remain unknown or inadequately studied. Multicenter prospective natural-history cohorts and assay-standardized repeat characterization are prerequisites for genotype–phenotype modeling and future SCA36 therapeutic trials.

References

1. (lee2016spinocerebellarataxiatype pages 1-2): Yi-Chung Lee, Pei-Chien Tsai, Yuh-Cherng Guo, Cheng-Tsung Hsiao, Guan-Ting Liu, Yi-Chu Liao, and Bing-Wen Soong. Spinocerebellar ataxia type 36 in the han chinese. Jun 2016. URL: https://doi.org/10.1212/nxg.0000000000000068, doi:10.1212/nxg.0000000000000068. This article has 43 citations.

2. (obayashi2015spinocerebellarataxiatype pages 3-4): Masato Obayashi, Giovanni Stevanin, Matthis Synofzik, Marie-Lorraine Monin, Charles Duyckaerts, Nozomu Sato, Nathalie Streichenberger, Alain Vighetto, Virginie Desestret, Christelle Tesson, H-Erich Wichmann, Thomas Illig, Johanna Huttenlocher, Yasushi Kita, Yuishin Izumi, Hidehiro Mizusawa, Ludger Schöls, Thomas Klopstock, Alexis Brice, Kinya Ishikawa, and Alexandra Dürr. Spinocerebellar ataxia type 36 exists in diverse populations and can be caused by a short hexanucleotide ggcctg repeat expansion. Journal of Neurology, Neurosurgery & Psychiatry, 86:986-995, Dec 2015. URL: https://doi.org/10.1136/jnnp-2014-309153, doi:10.1136/jnnp-2014-309153. This article has 69 citations.

3. (lam2023repeatexpansionsin pages 1-3): Tanya Lam, Clarissa Rocca, Kristina Ibanez, Anupriya Dalmia, Samuel Tallman, Marios Hadjivassiliou, Anke Hensiek, Andrea Nemeth, Stefano Facchini, J C Ambrose, P Arumugam, R Bevers, M Bleda, F Boardman-Pretty, C R Boustred, H Brittain, M A Brown, M J Caulfield, G C Chan, A Giess, J N Griffin, A Hamblin, S Henderson, T J P Hubbard, R Jackson, L J Jones, D Kasperaviciute, M Kayikci, A Kousathanas, L Lahnstein, A Lakey, S E A Leigh, I U S Leong, F J Lopez, F Maleady-Crowe, M McEntagart, F Minneci, J Mitchell, L Moutsianas, M Mueller, N Murugaesu, A C Need, P O’Donovan, C A Odhams, C Patch, D Perez-Gil, M B Pereira, J Pullinger, T Rahim, A Rendon, T Rogers, K Savage, K Sawant, R H Scott, A Siddiq, A Sieghart, S C Smith, A Sosinsky, A Stuckey, M Tanguy, A L Taylor Tavares, E R A Thomas, S R Thompson, A Tucci, M J Welland, E Williams, K Witkowska, S M Wood, M Zarowiecki, Nicholas Wood, Andrea Cortese, Henry Houlden, and Arianna Tucci. Repeat expansions in nop56 are a cause of spinocerebellar ataxia type 36 in the british population. Brain Communications, Sep 2023. URL: https://doi.org/10.1093/braincomms/fcad244, doi:10.1093/braincomms/fcad244. This article has 9 citations and is from a peer-reviewed journal.

4. (lopez2022spinocerebellarataxia36 pages 3-5): Samuel Lopez and Fang He. Spinocerebellar ataxia 36: from mutations toward therapies. Frontiers in Genetics, Mar 2022. URL: https://doi.org/10.3389/fgene.2022.837690, doi:10.3389/fgene.2022.837690. This article has 13 citations and is from a peer-reviewed journal.

5. (quelleregaldie2022anop56zebrafish pages 1-2): Ana Quelle-Regaldie, Mónica Folgueira, Julián Yáñez, Daniel Sobrido-Cameán, Anabel Alba-González, Antón Barreiro-Iglesias, María-Jesús Sobrido, and Laura Sánchez. A nop56 zebrafish loss-of-function model exhibits a severe neurodegenerative phenotype. Jul 2022. URL: https://doi.org/10.3390/biomedicines10081814, doi:10.3390/biomedicines10081814. This article has 12 citations.

6. (mceachin2020chimericpeptidespecies pages 1-3): Zachary T. McEachin, Tania F. Gendron, Nisha Raj, María García-Murias, Anwesha Banerjee, Ryan H. Purcell, Patricia J. Ward, Tiffany W. Todd, Megan E. Merritt-Garza, Karen Jansen-West, Chadwick M. Hales, Tania García-Sobrino, Beatriz Quintáns, Christopher J. Holler, Georgia Taylor, Beatriz San Millán, Susana Teijeira, Toru Yamashita, Ryuichi Ohkubo, Nicholas M. Boulis, Chongchong Xu, Zhexing Wen, Nathalie Streichenberger, Brent L. Fogel, Thomas Kukar, Koji Abe, Dennis W. Dickson, Manuel Arias, Jonathan D. Glass, Jie Jiang, Malú G. Tansey, María-Jesús Sobrido, Leonard Petrucelli, Wilfried Rossoll, and Gary J. Bassell. Chimeric peptide species contribute to divergent dipeptide repeat pathology in c9als/ftd and sca36. Jul 2020. URL: https://doi.org/10.1016/j.neuron.2020.04.011, doi:10.1016/j.neuron.2020.04.011. This article has 84 citations and is from a highest quality peer-reviewed journal.

7. (matsuzono2017antisenseoligonucleotidesreduce pages 1-2): Kosuke Matsuzono, Keiko Imamura, Nagahisa Murakami, Kayoko Tsukita, Takuya Yamamoto, Yuishin Izumi, Ryuji Kaji, Yasuyuki Ohta, Toru Yamashita, Koji Abe, and Haruhisa Inoue. Antisense oligonucleotides reduce rna foci in spinocerebellar ataxia 36 patient ipscs. Sep 2017. URL: https://doi.org/10.1016/j.omtn.2017.06.017, doi:10.1016/j.omtn.2017.06.017. This article has 47 citations.

8. (furuta2019suppressionofthe pages 1-2): Natsumi Furuta, Setsuki Tsukagoshi, Kimitoshi Hirayanagi, and Yoshio Ikeda. Suppression of the yeast elongation factor spt4 ortholog reduces expanded sca36 ggccug repeat aggregation and cytotoxicity. Brain Research, 1711:29-40, May 2019. URL: https://doi.org/10.1016/j.brainres.2018.12.045, doi:10.1016/j.brainres.2018.12.045. This article has 22 citations and is from a peer-reviewed journal.

9. (OpenTargets Search: spinocerebellar ataxia type 36-NOP56): Open Targets Query (spinocerebellar ataxia type 36-NOP56, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (obayashi2015spinocerebellarataxiatype pages 2-3): Masato Obayashi, Giovanni Stevanin, Matthis Synofzik, Marie-Lorraine Monin, Charles Duyckaerts, Nozomu Sato, Nathalie Streichenberger, Alain Vighetto, Virginie Desestret, Christelle Tesson, H-Erich Wichmann, Thomas Illig, Johanna Huttenlocher, Yasushi Kita, Yuishin Izumi, Hidehiro Mizusawa, Ludger Schöls, Thomas Klopstock, Alexis Brice, Kinya Ishikawa, and Alexandra Dürr. Spinocerebellar ataxia type 36 exists in diverse populations and can be caused by a short hexanucleotide ggcctg repeat expansion. Journal of Neurology, Neurosurgery & Psychiatry, 86:986-995, Dec 2015. URL: https://doi.org/10.1136/jnnp-2014-309153, doi:10.1136/jnnp-2014-309153. This article has 69 citations.

11. (obayashi2015spinocerebellarataxiatype pages 7-9): Masato Obayashi, Giovanni Stevanin, Matthis Synofzik, Marie-Lorraine Monin, Charles Duyckaerts, Nozomu Sato, Nathalie Streichenberger, Alain Vighetto, Virginie Desestret, Christelle Tesson, H-Erich Wichmann, Thomas Illig, Johanna Huttenlocher, Yasushi Kita, Yuishin Izumi, Hidehiro Mizusawa, Ludger Schöls, Thomas Klopstock, Alexis Brice, Kinya Ishikawa, and Alexandra Dürr. Spinocerebellar ataxia type 36 exists in diverse populations and can be caused by a short hexanucleotide ggcctg repeat expansion. Journal of Neurology, Neurosurgery & Psychiatry, 86:986-995, Dec 2015. URL: https://doi.org/10.1136/jnnp-2014-309153, doi:10.1136/jnnp-2014-309153. This article has 69 citations.

12. (lam2023repeatexpansionsin pages 3-4): Tanya Lam, Clarissa Rocca, Kristina Ibanez, Anupriya Dalmia, Samuel Tallman, Marios Hadjivassiliou, Anke Hensiek, Andrea Nemeth, Stefano Facchini, J C Ambrose, P Arumugam, R Bevers, M Bleda, F Boardman-Pretty, C R Boustred, H Brittain, M A Brown, M J Caulfield, G C Chan, A Giess, J N Griffin, A Hamblin, S Henderson, T J P Hubbard, R Jackson, L J Jones, D Kasperaviciute, M Kayikci, A Kousathanas, L Lahnstein, A Lakey, S E A Leigh, I U S Leong, F J Lopez, F Maleady-Crowe, M McEntagart, F Minneci, J Mitchell, L Moutsianas, M Mueller, N Murugaesu, A C Need, P O’Donovan, C A Odhams, C Patch, D Perez-Gil, M B Pereira, J Pullinger, T Rahim, A Rendon, T Rogers, K Savage, K Sawant, R H Scott, A Siddiq, A Sieghart, S C Smith, A Sosinsky, A Stuckey, M Tanguy, A L Taylor Tavares, E R A Thomas, S R Thompson, A Tucci, M J Welland, E Williams, K Witkowska, S M Wood, M Zarowiecki, Nicholas Wood, Andrea Cortese, Henry Houlden, and Arianna Tucci. Repeat expansions in nop56 are a cause of spinocerebellar ataxia type 36 in the british population. Brain Communications, Sep 2023. URL: https://doi.org/10.1093/braincomms/fcad244, doi:10.1093/braincomms/fcad244. This article has 9 citations and is from a peer-reviewed journal.

13. (obayashi2015spinocerebellarataxiatype pages 4-5): Masato Obayashi, Giovanni Stevanin, Matthis Synofzik, Marie-Lorraine Monin, Charles Duyckaerts, Nozomu Sato, Nathalie Streichenberger, Alain Vighetto, Virginie Desestret, Christelle Tesson, H-Erich Wichmann, Thomas Illig, Johanna Huttenlocher, Yasushi Kita, Yuishin Izumi, Hidehiro Mizusawa, Ludger Schöls, Thomas Klopstock, Alexis Brice, Kinya Ishikawa, and Alexandra Dürr. Spinocerebellar ataxia type 36 exists in diverse populations and can be caused by a short hexanucleotide ggcctg repeat expansion. Journal of Neurology, Neurosurgery & Psychiatry, 86:986-995, Dec 2015. URL: https://doi.org/10.1136/jnnp-2014-309153, doi:10.1136/jnnp-2014-309153. This article has 69 citations.

14. (lopez2022spinocerebellarataxia36 pages 2-3): Samuel Lopez and Fang He. Spinocerebellar ataxia 36: from mutations toward therapies. Frontiers in Genetics, Mar 2022. URL: https://doi.org/10.3389/fgene.2022.837690, doi:10.3389/fgene.2022.837690. This article has 13 citations and is from a peer-reviewed journal.

15. (rafehi2023detectionanddiscovery pages 1-2): Haloom Rafehi, Mark F. Bennett, and Melanie Bahlo. Detection and discovery of repeat expansions in ataxia enabled by next-generation sequencing: present and future. Emerging Topics in Life Sciences, 7:349-359, Sep 2023. URL: https://doi.org/10.1042/etls20230018, doi:10.1042/etls20230018. This article has 11 citations.

16. (stevanovski2022comprehensivegeneticdiagnosis pages 1-3): Igor Stevanovski, Sanjog R. Chintalaphani, Hasindu Gamaarachchi, James M. Ferguson, Sandy S. Pineda, Carolin K. Scriba, Michel Tchan, Victor Fung, Karl Ng, Andrea Cortese, Henry Houlden, Carol Dobson-Stone, Lauren Fitzpatrick, Glenda Halliday, Gianina Ravenscroft, Mark R. Davis, Nigel G. Laing, Avi Fellner, Marina Kennerson, Kishore R. Kumar, and Ira W. Deveson. Comprehensive genetic diagnosis of tandem repeat expansion disorders with programmable targeted nanopore sequencing. Mar 2022. URL: https://doi.org/10.1126/sciadv.abm5386, doi:10.1126/sciadv.abm5386. This article has 229 citations and is from a highest quality peer-reviewed journal.

17. (NCT06467175 chunk 1):  The Benefits of Long-read High-throughput Genomic Sequencing for the Causal Diagnosis of Cerebellar Ataxias. Centre Hospitalier Universitaire Dijon. 2024. ClinicalTrials.gov Identifier: NCT06467175

18. (todd2020hexanucleotiderepeatexpansions pages 8-9): Tiffany W. Todd, Zachary T. McEachin, Jeannie Chew, Alexander R. Burch, Karen Jansen-West, Jimei Tong, Mei Yue, Yuping Song, Monica Castanedes-Casey, Aishe Kurti, Judith H. Dunmore, John D. Fryer, Yong-Jie Zhang, Beatriz San Millan, Susana Teijeira Bautista, Manuel Arias, Dennis Dickson, Tania F. Gendron, María-Jesús Sobrido, Matthew D. Disney, Gary J. Bassell, Wilfried Rossoll, and Leonard Petrucelli. Hexanucleotide repeat expansions in c9ftd/als and sca36 confer selective patterns of neurodegeneration in vivo. Cell Reports, 31(5):107616, May 2020. URL: https://doi.org/10.1016/j.celrep.2020.107616, doi:10.1016/j.celrep.2020.107616. This article has 58 citations and is from a highest quality peer-reviewed journal.

19. (todd2020hexanucleotiderepeatexpansions pages 16-17): Tiffany W. Todd, Zachary T. McEachin, Jeannie Chew, Alexander R. Burch, Karen Jansen-West, Jimei Tong, Mei Yue, Yuping Song, Monica Castanedes-Casey, Aishe Kurti, Judith H. Dunmore, John D. Fryer, Yong-Jie Zhang, Beatriz San Millan, Susana Teijeira Bautista, Manuel Arias, Dennis Dickson, Tania F. Gendron, María-Jesús Sobrido, Matthew D. Disney, Gary J. Bassell, Wilfried Rossoll, and Leonard Petrucelli. Hexanucleotide repeat expansions in c9ftd/als and sca36 confer selective patterns of neurodegeneration in vivo. Cell Reports, 31(5):107616, May 2020. URL: https://doi.org/10.1016/j.celrep.2020.107616, doi:10.1016/j.celrep.2020.107616. This article has 58 citations and is from a highest quality peer-reviewed journal.

20. (matsuzono2017antisenseoligonucleotidesreduce pages 6-7): Kosuke Matsuzono, Keiko Imamura, Nagahisa Murakami, Kayoko Tsukita, Takuya Yamamoto, Yuishin Izumi, Ryuji Kaji, Yasuyuki Ohta, Toru Yamashita, Koji Abe, and Haruhisa Inoue. Antisense oligonucleotides reduce rna foci in spinocerebellar ataxia 36 patient ipscs. Sep 2017. URL: https://doi.org/10.1016/j.omtn.2017.06.017, doi:10.1016/j.omtn.2017.06.017. This article has 47 citations.

21. (lee2016spinocerebellarataxiatype pages 2-3): Yi-Chung Lee, Pei-Chien Tsai, Yuh-Cherng Guo, Cheng-Tsung Hsiao, Guan-Ting Liu, Yi-Chu Liao, and Bing-Wen Soong. Spinocerebellar ataxia type 36 in the han chinese. Jun 2016. URL: https://doi.org/10.1212/nxg.0000000000000068, doi:10.1212/nxg.0000000000000068. This article has 43 citations.

22. (rudaks2024anupdateon pages 14-15): Laura Ivete Rudaks, Dennis Yeow, Karl Ng, Ira W. Deveson, Marina L. Kennerson, and Kishore Raj Kumar. An update on the adult-onset hereditary cerebellar ataxias: novel genetic causes and new diagnostic approaches. Cerebellum (London, England), 23:2152-2168, May 2024. URL: https://doi.org/10.1007/s12311-024-01703-z, doi:10.1007/s12311-024-01703-z. This article has 59 citations.

## Artifacts

- [Edison artifact artifact-00](Spinocerebellar_Ataxia_Type_36-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030529` (GO_0030529) (1 mention) - replaced by `GO:1990904`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

36 of 39 terms resolved to a current term; the rest could not be looked up either way.