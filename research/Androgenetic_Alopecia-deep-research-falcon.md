---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T23:23:55.587638'
end_time: '2026-09-04T23:40:51.410641'
duration_seconds: 1015.82
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Androgenetic Alopecia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 14
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Androgenetic_Alopecia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Androgenetic Alopecia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Androgenetic Alopecia** covering all of the
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
- **Disease Name:** Androgenetic Alopecia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Androgenetic Alopecia** covering all of the
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


# Androgenetic Alopecia: Disease-Characteristics Research Report

**Scope.** Androgenetic alopecia (AGA) is a common, complex, polygenic, androgen-dependent, non-scarring hair-loss disorder. “Male-pattern hair loss” (MPHL) and “female-pattern hair loss” (FPHL) denote its principal sex-patterned clinical presentations. Evidence below is disease-level and aggregated from publications and registries—not individual EHR data—unless a cohort is explicitly described.

| Domain | Curated finding | Suggested ontology/identifier | Evidence type/strength |
|---|---|---|---|
| Disease Identifiers | Androgenetic alopecia (Male/Female Pattern Hair Loss); MONDO:0007184 is a historical subtype | MONDO:0005339 | Consensus/Standard |
| Clinical Phenotypes | Progressive follicular miniaturization, anagen shortening, patterned hair loss (Hamilton-Norwood / Ludwig), vellus hair replacement | HP:0002286 (Premature baldness), HP:0001596 (Alopecia), HP:0011364 (Thinning hair) | Human clinical (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 1-2) |
| Anatomy & Cellular | Scalp hair follicle dermal papilla cells, follicular stem cells; regional sparing of occipital scalp | UBERON:0002073 (hair follicle), CL:0002551 (hair follicle dermal papilla cell) | Human clinical/Histology (duran2024thebiologyand pages 11-13, duran2024thebiologyand pages 6-7) |
| Susceptibility Genetics | Polygenic inheritance; strong signals at AR/EDA2R (Chr X), SRD5A2, FGF5, WNT10A, HDAC9. Not monogenic causal. | HGNC: AR, SRD5A2, WNT10A, FGF5 | GWAS, Human genetics (OpenTargets Search: androgenetic alopecia, souza2026useofgenetics pages 3-4) |
| Molecular Pathways | DHT-AR signaling, WNT/beta-catenin suppression, DKK1 induction, premature senescence, prostaglandin dysregulation (PGD2) | GO:0043401 (steroid hormone mediated signaling), GO:0016055 (Wnt signaling pathway) | In vitro, Transcriptomics, Human genetics (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 3-4) |
| Diagnostics | Clinical pattern recognition; Trichoscopy: hair diameter diversity (>20%), peripilar signs, short vellus hairs, increased single-hair units | Clinical finding, Dermoscopy | Human clinical/Systematic review (khare2023dermoscopyofhair pages 1-2, khare2023dermoscopyofhair pages 28-29) |
| Epidemiology | High prevalence: ~30% of men by age 30, up to 50% of men and 40% of women by age 50; strong familial clustering | Epidemiologic statistics | Human population studies (kumaresan2025adecadeof pages 1-2, souza2026useofgenetics pages 1-2) |
| Pharmacotherapy | Topical minoxidil (FDA-approved), oral finasteride (FDA-approved for men), off-label dutasteride, oral minoxidil, spironolactone | NCIT:C62024 (Minoxidil), NCIT:C1265 (Finasteride), NCIT:C47491 (Dutasteride) | High-quality RCTs, Network Meta-analyses (burshtein2026emergingpharmacotherapiesand pages 2-3, kumaresan2025adecadeof pages 1-2) |
| Procedural Therapy | Platelet-rich plasma (PRP), microneedling, low-level laser therapy (LLLT), follicular unit transplantation | NCIT:C175492 (Platelet Rich Plasma), NCIT:C154215 (Low Level Light Therapy) | Moderate RCTs, Systemic Reviews (burshtein2026emergingpharmacotherapiesand pages 2-3, britva2026regenerativestrategiesfor pages 19-19) |
| Prognosis & QoL | Chronic, progressive course without treatment; associated with anxiety, depression, and significant psychosocial burden | PROMIS, EQ-5D, SF-36 | Observational, Population studies (toussi2021psychosocialandpsychiatric pages 28-30, gupta2025relativeefficacyof pages 2-2) |
| Experimental Models | DHT-induced murine models, stump-tailed macaque, microfollicles, human dermal papilla explants and skin organoids | Model organism/In vitro | Animal/Organoid studies (souza2026useofgenetics pages 3-4, liu2026developmentandvalidation pages 13-13) |


*Table: This table provides a compact, ontology-mapped summary of key disease characteristics for androgenetic alopecia, curated from clinical and genomic literature.*

## 1. Disease information

AGA is characterized by progressive conversion of pigmented terminal scalp hairs into shorter, finer, often depigmented vellus-like hairs through repeated shortening of anagen and follicular miniaturization. Men usually develop bitemporal recession and frontal–mid-scalp–vertex loss, whereas women more often develop diffuse central/vertex thinning with relative preservation of the frontal hairline. Occipital/parietal follicles are comparatively resistant, especially in men. The condition is non-scarring: follicular ostia and potentially recoverable miniaturized follicles remain until advanced disease. (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 1-2)

**Identifiers and synonyms.** MONDO identifies androgenetic alopecia as **MONDO:0005339**; Open Targets also maps a historical “androgenetic alopecia 1” entity to **MONDO:0007184**. Common terms include androgenic alopecia, pattern hair loss, common baldness, male-pattern baldness/MPHL and female-pattern hair loss/FPHL. Common coding mappings include ICD-10-CM **L64.9** (androgenic alopecia, unspecified), L64.0 (drug-induced androgenic alopecia), L64.8 (other androgenic alopecia), and MeSH **Androgenetic Alopecia**. Exact ICD-11 and SNOMED mappings should be terminology-server validated before ingestion because national extensions differ. (OpenTargets Search: androgenetic alopecia)

A concise 2024 review states: “Androgenetic alopecia is a highly prevalent condition mainly affecting men,” and emphasizes that it is related to aging and genetics while lifestyle and other factors may contribute. Publication: February 2024; DOI/URL: https://doi.org/10.3390/ijms25052542. (duran2024thebiologyand pages 11-13)

## 2. Etiology

### Causal architecture

AGA is not ordinarily caused by one pathogenic mutation. It reflects age-dependent expression of polygenic susceptibility in androgen-responsive scalp follicles. Testosterone is converted to dihydrotestosterone (DHT) by 5α-reductases; DHT–AR signaling in susceptible dermal papilla cells changes paracrine support for epithelial progenitors and progressively shortens anagen. Female disease is more heterogeneous and can occur without measurable systemic androgen excess. (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 3-4)

### Risk factors

* **Genetic/familial:** Twin and family data indicate strong heritability, often estimated near or above 80%. The AR/EDA2R X-chromosome region is the best-known signal, but numerous autosomal loci demonstrate polygenicity. Family history was associated with AGA presence (OR 2.72), progression (OR 4.24), and paternal history with presence (OR 2.22) in a meta-analysis of 31 studies, 11,224 cases and 36,825 controls searched through January 5, 2024. (duran2024thebiologyand pages 11-13, li2026riskfactorsfor pages 1-2)
* **Age and sex:** Clinically relevant AGA affects about 30% of men by age 30, nearly 50% by 50, and more than 70% in later decades. Female prevalence rises markedly after menopause; summarized estimates were 6% below age 50 and 30–40% above age 70. (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 1-2)
* **Smoking/metabolic factors:** Smoking was associated with presence (OR 1.46) and progression (OR 1.60); insulin resistance (SMD 0.40), fasting insulin (SMD 0.48), and male hypertension (OR 1.60) were associated with AGA. Alcohol, poor/insufficient sleep and overweight/obesity were linked mainly to progression. These observational associations do not establish causation and may be confounded. (li2026riskfactorsfor pages 1-2)
* **Early-onset disease:** A 2024 scoping review of 65 studies reported family history, smoking, unhealthy diet and high BMI as recurrent factors and examined associations with metabolic syndrome, insulin resistance, dyslipidemia and cardiovascular disease. Most studies were case-control and male-only, limiting causal and female inference. DOI: https://doi.org/10.1371/journal.pone.0299212.

### Protective factors and gene–environment interaction

No genetic variant or lifestyle exposure is sufficiently validated as clinically actionable protection. Avoiding smoking and correcting documented nutritional deficiency are reasonable general-health measures, but evidence that either prevents genetically susceptible AGA is inadequate. The likely interaction is that inherited follicular androgen sensitivity sets vulnerability while age, endocrine milieu, smoking, metabolic dysfunction, inflammation and oxidative stress modify onset or progression; direct, replicated G×E estimates remain sparse. There is no infectious cause, zoonotic transmission or vaccine-preventable trigger.

## 3. Phenotypes

* **Patterned non-scarring scalp alopecia:** adult-onset, insidious, chronic and variably progressive. Men show temporal recession and vertex/frontal loss; women usually show widening of the central part and diffuse crown thinning. Suggested HPO: **HP:0001596 Alopecia**, **HP:0011364 Thinning hair**, **HP:0002286 Premature baldness**. (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 1-2)
* **Follicular miniaturization:** terminal-to-vellus transformation, reduced shaft diameter/density and increased single-hair follicular units. Suggested phenotype annotation: hair-shaft thinning/miniaturization; retain as a disease-specific clinical feature if no exact HPO term is available. (duran2024thebiologyand pages 6-7)
* **Trichoscopic phenotype:** A 2024 systematic review found hair-diameter variability in **94.07%**, vellus hairs in **66.45%**, and peripilar sign in **43.27%** of patients. These are valuable indicators, particularly in women and early disease. Publication: March 2024; DOI: https://doi.org/10.3390/jcm13071962.
* **Psychological burden:** distress, body-image dissatisfaction, anxiety, depression and reduced self-esteem occur in subsets, especially younger or care-seeking patients. However, burden is heterogeneous: among 892 Finnish men aged 46, AGA prevalence was 68.5%—39.0% mild, 33.2% moderate and 27.8% severe—with no significant difference in measured anxiety, depression, self-esteem or overall QoL. Thus visible alopecia is not synonymous with psychiatric morbidity. DOI: https://doi.org/10.1136/bmjopen-2021-049855.

There are no defining laboratory abnormalities. Hyperandrogenism signs in women—irregular menses, acne, hirsutism or virilization—suggest an associated endocrine disorder rather than a required AGA phenotype.

## 4. Genetic and molecular information

### Susceptibility genes—not Mendelian causal genes

GWAS had catalogued 119 significant variants across eight studies through 2021. The strongest summarized signal, **rs200644307**, lies approximately 500 kb from **AR** and may act through cis-regulation; its function is not established. Recurrently implicated regions/genes include **AR/EDA2R**, chromosome 20p11, **SRD5A1, SRD5A2, CYP19A1, WNT10A, WNT6, RSPO2, LGR4, DKK2, FGF5, HDAC9, EBF1, PAX1, MAPT** and others. Open Targets prioritizes SRD5A2, FGF5, SRD5A1/3, WNT10A, RSPO2, DKK2, AR and developmental transcription factors, but these disease–target associations do not mean that rare pathogenic variants in each gene cause ordinary AGA. (OpenTargets Search: androgenetic alopecia, duran2024thebiologyand pages 11-13, souza2026useofgenetics pages 3-4)

Accordingly, routine ClinVar-style “pathogenic/likely pathogenic” variant classification, carrier frequency, somatic mutation testing and germline mosaicism are generally **not applicable** to common AGA. Risk alleles are predominantly germline, common and small-effect; penetrance is incomplete, sex- and age-dependent, and expressivity variable. No consistent chromosomal aneuploidy, translocation, repeat expansion or mitochondrial mutation defines AGA.

### Epigenetics and molecular profiling

Human balding-versus-nonbalding scalp studies report differential mRNA, miRNA and lncRNA expression involving WNT, HIF-1, Hippo, inflammatory, stress and fibrosis programs (reported transcriptomic PMIDs include **29122575** and **35862273**). A 2024 TWAS identified 52, 75 and 144 expression–phenotype associations across increasingly severe MPB categories and 10, 11 and 54 putative causal genes after conditional analysis; these are computational prioritizations requiring functional validation. (duran2024thebiologyand pages 11-13)

Single-cell atlases demonstrate marked follicular heterogeneity—23 subpopulations in human anagen follicles from five transplant donors and dozens of epithelial/mesenchymal states in mouse skin—but AGA-specific, replicated single-cell and spatial maps remain limited. Epigenetic involvement is plausible through regulatory GWAS enrichment and loci such as HDAC9, but no methylation signature is validated diagnostically. (duran2024thebiologyand pages 11-13)

## 5. Environmental information

No toxin, radiation exposure, occupational agent or pathogen is accepted as a primary cause. Smoking, alcohol, poor sleep, diet, obesity and metabolic dysfunction have epidemiologic associations of varying consistency. Nutritional deficiencies can independently cause diffuse shedding and may coexist with AGA; indiscriminate supplements are not evidence-based in replete patients. Mechanical traction, chemotherapy, thyroid disease, severe illness and medications should instead prompt evaluation for alternative or superimposed alopecia. (li2026riskfactorsfor pages 1-2)

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Polygenic susceptibility plus age and sex-hormone context leads to** region-specific androgen sensitivity in scalp follicular dermal papilla cells.
2. **5α-reductase-mediated conversion of testosterone to DHT leads to** high-affinity DHT binding and nuclear activation of AR in susceptible dermal papilla cells.
3. **DHT–AR transcriptional signaling leads to** altered paracrine output—including increased DKK1, IL-6, TGF-β-related/fibrotic and prostaglandin-D2 programs—and premature dermal-papilla senescence; the relative contribution of each branch is partly inferred from human scalp expression and in-vitro experiments.
4. **DKK1 and related antagonism leads to** suppression of WNT/β-catenin-dependent epithelial–mesenchymal signaling and impaired activation/support of follicular epithelial stem/progenitor cells.
5. **Parallel PGD2–PTGDR2 signaling leads to** reduced shaft elongation and promotion of catagen, while inflammatory, oxidative-stress and perifollicular-remodeling branches likely amplify dysfunction.
6. **Reduced growth signaling and premature catagen lead to** shortened anagen, relatively increased telogen, smaller dermal papillae and progressive terminal-follicle miniaturization.
7. **Repeated miniaturizing cycles result in** thin, short, depigmented vellus-like hairs and the clinically visible male or female pattern of non-scarring scalp alopecia. (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 3-4)

### Cells, processes and ontology suggestions

Primary cells are dermal papilla fibroblasts (**CL:0002551**), hair-follicle stem/progenitor keratinocytes, matrix keratinocytes, dermal sheath fibroblasts, endothelial cells and perifollicular immune cells. Suggested GO biological processes include steroid-hormone-mediated signaling (**GO:0043401**), WNT signaling (**GO:0016055**), hair-follicle development, hair cycle, cell senescence, regulation of apoptosis, inflammatory response, extracellular-matrix organization and angiogenesis. Relevant compartments include nucleus/AR transcriptional complex, cytosol, plasma membrane and extracellular matrix.

This mechanism is principally altered signaling rather than protein misfolding or enzyme deficiency. DHT itself is not necessarily systemically elevated; local enzyme activity and follicular receptor sensitivity matter. Open Targets’ highest disease association was SRD5A2, consistent with the clinical validation of 5α-reductase inhibition. (OpenTargets Search: androgenetic alopecia)

## 7. Anatomical structures affected

The primary organ is skin of the scalp and its pilosebaceous units; the directly affected mini-organ is the hair follicle (**UBERON:0002073**). In men the frontal, temporal, mid-scalp and vertex follicles are preferentially affected, with relative occipital/parietal sparing; female involvement is typically central/vertex and more diffuse. Distribution is bilateral and broadly symmetric, not lateralized. (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 1-2)

At tissue level, affected structures include follicular epithelium, connective-tissue dermal papilla/sheath, perifollicular extracellular matrix and microvasculature. There is no obligatory secondary-organ injury. Endocrine/metabolic comorbidities are associations, not anatomical spread.

## 8. Temporal development

Onset is commonly post-pubertal and insidious; men tend to present earlier than women. Early disease manifests as reduced density, hair-diameter diversity and increased vellus/single-hair units; intermediate disease produces evident patterned thinning; advanced disease shows extensive miniaturization. The course is chronic, slowly progressive and highly variable. Spontaneous durable remission is uncommon, while treatment can stabilize or partially reverse miniaturization. Benefits generally diminish after treatment withdrawal. Earlier intervention is biologically favored because miniaturized follicles are more recoverable than long-standing severely involuted units. (duran2024thebiologyand pages 6-7, souza2026useofgenetics pages 1-2)

## 9. Inheritance and population

Inheritance is **multifactorial/polygenic**, not simple autosomal dominant or X-linked, despite strong X-chromosomal AR/EDA2R effects. Penetrance is incomplete and age/sex dependent; expressivity varies in onset, distribution and severity. Anticipation, carrier status, consanguinity and classic founder mutations are not established features. (duran2024thebiologyand pages 11-13, souza2026useofgenetics pages 3-4)

Prevalence depends strongly on age, ancestry, case definition and ascertainment. Up to 50% of men and 40% of women may be affected by midlife in some reviews; Caucasian men have historically shown the highest reported prevalence, while onset/severity vary across ancestries. In 9,227 dermatologist-examined Chinese university freshmen, prevalence was **5.3/1,000**, including **7.9/1,000 males**; female sex had OR 0.29. The young age explains why these values are far below lifetime estimates. DOI: https://doi.org/10.1371/journal.pone.0263912. (kumaresan2025adecadeof pages 1-2, souza2026useofgenetics pages 1-2)

Reliable annual incidence per 100,000 is not established globally. Apparent healthcare prevalence also reflects access, cosmetic concern and coding behavior.

## 10. Diagnostics

Diagnosis is primarily clinical: compatible patterned non-scarring thinning, preserved follicular openings, gradual onset and family history. Grade men with Hamilton–Norwood and women with Ludwig/Sinclair; BASP can describe either sex. Serial standardized photography or phototrichograms support monitoring. Trichoscopy should assess shaft-diameter variability, miniaturized/vellus hairs, peripilar sign, yellow dots and increasing single-hair follicular units. (duran2024thebiologyand pages 6-7, khare2023dermoscopyofhair pages 1-2)

Laboratory tests are selective, not confirmatory. In women with diffuse shedding, menstrual/endocrine symptoms or systemic signs, consider CBC/ferritin, TSH and targeted androgen testing; evaluate nutritional deficiency based on history. Scalp biopsy is reserved for uncertainty: horizontal sections typically show reduced terminal:vellus ratio, increased miniaturized follicles, altered anagen:telogen ratio and sometimes mild perifollicular inflammation/fibrosis.

**Differential diagnosis:** telogen effluvium (diffuse shedding without patterned miniaturization), alopecia areata (patches, exclamation-mark/black-dot/tapering-hair pattern), traction alopecia (hairstyle distribution), trichotillomania (broken hairs of variable length), tinea capitis (scale/infection), frontal fibrosing alopecia or lichen planopilaris (loss of ostia and inflammatory scarring), central centrifugal cicatricial alopecia, thyroid/nutritional disease and medication-induced shedding.

Routine WES, WGS, panels, AR testing, CMA, karyotype, FISH, mtDNA or repeat-expansion testing has no validated diagnostic role. Polygenic scores, transcriptomics, proteomics and liquid biopsy remain research tools.

## 11. Outcome and prognosis

AGA is medically benign and does not reduce survival or life expectancy. Morbidity is cosmetic and psychosocial rather than organ failure or mortality. Untreated disease commonly progresses, but at an unpredictable rate; existing follicles can be stabilized or thickened, whereas drugs do not generate an unlimited supply of new follicles. Surgical redistribution can provide durable cosmetic coverage but donor hair is finite. (britva2026regenerativestrategiesfor pages 19-19)

QoL impact should be measured rather than assumed, using DLQI, EQ-5D, SF-36/PROMIS or hair-specific instruments. Younger age, female sex in some settings, rapid progression, severe visible loss and body-image concern may predict greater distress, but population evidence is inconsistent. (kumaresan2025adecadeof pages 1-2)

## 12. Treatment

### Practical strategy

1. Confirm AGA and exclude scarring or superimposed shedding.
2. Offer topical minoxidil to either sex; discuss initial shedding, irritation and lifelong maintenance.
3. For men, add oral finasteride after sexual, fertility and psychiatric counseling; consider dutasteride off-label where appropriate.
4. For selected women, consider low-dose oral minoxidil and antiandrogen therapy after cardiovascular, pregnancy and endocrine assessment.
5. Use PRP, microneedling or cleared low-level-light devices as adjuncts when expectations and evidence uncertainty are discussed.
6. Consider transplantation for stable, advanced disease with adequate donor density; continue medical treatment to protect non-transplanted hair.

### Pharmacotherapy and outcomes

* **Topical minoxidil 2–5%**—FDA-approved; prolongs anagen and requires continuous use. Reviews report moderate regrowth in approximately 30–40%. Adverse effects include irritation, unwanted facial/body hypertrichosis and transient initial shedding. Suggested NCIt: minoxidil (**C62024**). (burshtein2026emergingpharmacotherapiesand pages 2-3, kumaresan2025adecadeof pages 6-8)
* **Low-dose oral minoxidil, approximately 0.25–5 mg/day**—off-label. Useful when topical therapy is poorly tolerated, but hypertrichosis, edema, tachycardia, hypotension and rare serious cardiovascular effects require screening and monitoring. (kumaresan2025adecadeof pages 6-8)
* **Finasteride 1 mg/day**—FDA-approved for male AGA; inhibits type-II 5α-reductase. Sexual adverse effects were approximately 2–4% in reviewed male studies; regulators also warn about mood/psychiatric and potentially persistent sexual symptoms. It is contraindicated in pregnancy; crushed/broken tablets should not be handled by someone who is or may be pregnant. Suggested NCIt: finasteride (**C1265**). (burshtein2026emergingpharmacotherapiesand pages 2-3, gupta2025relativeefficacyof pages 6-6)
* **Dutasteride 0.5 mg/day**—dual type-I/II inhibitor, off-label in the US but approved for AGA in some countries including Japan and South Korea. It generally produces greater hair-count improvement than finasteride 1 mg, with similar overall tolerability but concern for sexual and psychiatric adverse effects. Suggested NCIt: dutasteride (**C47491**). (burshtein2026emergingpharmacotherapiesand pages 2-3)
* **Women:** spironolactone and, less commonly, finasteride/dutasteride in carefully selected patients are off-label. Antiandrogens require reliable contraception and monitoring appropriate to drug and comorbidity. Evidence is less standardized than in men.

A large randomized Chinese study reported improvement at 12 months in **80.5%** with finasteride, **59%** with 5% topical minoxidil and **94.1%** with their combination. Combination series/reviews report hair-density improvements of roughly **18–32%**, versus **8–15%** with monotherapy, although protocols and endpoints vary. (burshtein2026emergingpharmacotherapiesand pages 2-3, kumaresan2025adecadeof pages 11-12)

### Procedural and surgical treatments

PRP can improve density and shaft thickness, but preparation, dosing and endpoints are heterogeneous; benefit commonly lasts 3–6 months and maintenance is needed. One double-blind split-scalp trial of 35 participants found no superiority to placebo, illustrating uncertainty. Microneedling may activate wound/WNT programs and enhance topical delivery; 12–24-week trials generally favored combination with minoxidil over minoxidil alone. LLLT/photobiomodulation devices have modest efficacy and favorable short-term tolerability. Hair transplantation by follicular-unit excision or strip harvesting redistributes androgen-resistant donor follicles and is the principal durable structural intervention; risks include scarring, shock loss, poor growth, unnatural design and depletion of donor supply. (britva2026regenerativestrategiesfor pages 19-19, kumaresan2025adecadeof pages 6-8)

### Emerging therapeutics and trials

Topical AR antagonists such as pyrilutamide/KX-826, topical finasteride/dutasteride carriers, AR-silencing RNA, prostaglandin modulators, WNT-directed approaches, exosomes, conditioned media, adipose/dermal-sheath cells and follicle organoids are investigational. Exosome products remain poorly standardized/unregulated, and long-term safety is unknown. (souza2026useofgenetics pages 3-4, britva2026regenerativestrategiesfor pages 19-19, kumaresan2025adecadeof pages 1-2)

Current registry examples include phase-3 oral-minoxidil studies in women (**NCT05888922**, planned n=520) and men (**NCT07529977**, planned n=372), multiple VDPHL01 phase 2/3 programs (**NCT06527365, NCT06724614, NCT06972264, NCT07146022**), and a mechanistic topical-minoxidil/JAK2 study (**NCT07563036**, n=25). Registry status and enrollment should be rechecked at https://clinicaltrials.gov before database release; NCT07563036 had no outcome results in the retrieved record. (NCT07563036 chunk 2)

There is no established genotype-guided prescribing algorithm. SULT1A1 activity is a candidate minoxidil-response biomarker: one small study reported regrowth in **75%** with a SULT1A1 adjuvant versus **33%** with placebo adjuvant over 60 days, but this is not routine pharmacogenomics. (gupta2025relativeefficacyof pages 6-6)

## 13. Prevention

No proven primary prevention, vaccine, prophylactic medication or population screening program exists. Modifiable-risk counseling—avoid smoking, treat metabolic disease, maintain adequate nutrition and avoid traction—supports general/follicular health but is not proven to override inherited risk. Secondary prevention consists of early clinical/trichoscopic detection and prompt therapy to preserve miniaturizing follicles. Tertiary prevention includes adherence, serial monitoring, managing adverse effects and psychosocial support. Genetic carrier, prenatal or preimplantation screening is inappropriate for ordinary polygenic AGA.

## 14. Other species and natural disease

A directly homologous, common spontaneous veterinary disorder with the same human scalp distribution is not firmly established. Mammals share AR, steroid metabolism and WNT-regulated follicle cycling, but coat-hair biology and synchronized cycles differ substantially. “Pattern alopecia” in dogs is phenotypically relevant but should not automatically be equated with human polygenic AGA. There is no infectious transmission, zoonotic potential or cross-species contagion.

## 15. Model organisms and experimental systems

* **Human in vitro:** primary dermal papilla cells from balding/nonbalding scalp are exposed to DHT or pathway modulators to study AR, DKK1, senescence and growth signaling. Two-dimensional culture is scalable but rapidly loses papilla inductivity and lacks epithelial–mesenchymal architecture.
* **Human ex vivo:** isolated scalp follicles or punch/excision explants preserve native cycling and regional identity for short-term drug testing but are scarce, variable and short-lived.
* **Mouse (Mus musculus; NCBI Taxon 10090):** DHT-treated C57BL/6 models test hair-growth inhibition and 5α-reductase/WNT interventions. Mouse follicles cycle synchronously, have different androgen responses and do not reproduce human patterned scalp loss.
* **Stump-tailed macaque (Macaca arctoides; NCBI Taxon 9540):** develops androgen-responsive frontal balding and has historically been useful for 5α-reductase inhibitors, but expense, ethics and limited access constrain use.
* **3D spheroids, microfollicles and skin/hair-bearing organoids:** improve papilla inductivity and multicellular organization and may support regenerative/transplantation research. A systematic appraisal found 70/101 AGA model studies used mainly 2D in-vitro systems, 27 used mice or monkeys, only four used human explants, and none then used 3D organoids/organotypic AGA skin—highlighting a translational gap. A 2024 review emphasizes that fully recreating diverse follicular cell organization and durable cycling remains difficult. DOI: https://doi.org/10.1002/ski2.15 and https://doi.org/10.3390/biology13050312. (liu2026developmentandvalidation pages 13-13)

## Evidence appraisal and knowledge gaps

The strongest causal evidence combines human genetics, regional human scalp biology and therapeutic validation of SRD5A inhibition. Evidence for smoking/metabolic factors remains observational; immune, oxidative, epigenetic and many omics pathways are biologically plausible but not yet validated as independent clinical targets. Treatment evidence is strongest for minoxidil and finasteride, moderate for dutasteride and several adjunctive devices/procedures, and preliminary for topical AR antagonists, RNA, cells, exosomes and organoids. Major needs are ancestry-diverse longitudinal cohorts, standardized female phenotyping, AGA-specific single-cell/spatial atlases, validated response biomarkers and long-term head-to-head safety trials. (OpenTargets Search: androgenetic alopecia, duran2024thebiologyand pages 11-13, li2026riskfactorsfor pages 1-2, burshtein2026emergingpharmacotherapiesand pages 2-3)

References

1. (duran2024thebiologyand pages 6-7): Raquel Cuevas-Diaz Duran, Emmanuel Martinez-Ledesma, Melissa Garcia-Garcia, Denisse Bajo Gauzin, Andrea Sarro-Ramírez, Carolina Gonzalez-Carrillo, Denise Rodríguez-Sardin, Alejandro Fuentes, and Alejandro Cardenas-Lopez. The biology and genomics of human hair follicles: a focus on androgenetic alopecia. International Journal of Molecular Sciences, 25(5):2542, Feb 2024. URL: https://doi.org/10.3390/ijms25052542, doi:10.3390/ijms25052542. This article has 77 citations.

2. (souza2026useofgenetics pages 1-2): Gustavo Torres de Souza, Greg Williams, Carolina Costa Vicente Silva, Caroline Brandão Chiovatto, Gorana Kuka Epstein, Laura Vila-Vecilla, and Valentina Russo. Use of genetics in the prediction of success in male pattern hair loss therapy and mechanistic studies. Frontiers in Pharmacology, Feb 2026. URL: https://doi.org/10.3389/fphar.2026.1765808, doi:10.3389/fphar.2026.1765808. This article has 1 citations.

3. (duran2024thebiologyand pages 11-13): Raquel Cuevas-Diaz Duran, Emmanuel Martinez-Ledesma, Melissa Garcia-Garcia, Denisse Bajo Gauzin, Andrea Sarro-Ramírez, Carolina Gonzalez-Carrillo, Denise Rodríguez-Sardin, Alejandro Fuentes, and Alejandro Cardenas-Lopez. The biology and genomics of human hair follicles: a focus on androgenetic alopecia. International Journal of Molecular Sciences, 25(5):2542, Feb 2024. URL: https://doi.org/10.3390/ijms25052542, doi:10.3390/ijms25052542. This article has 77 citations.

4. (OpenTargets Search: androgenetic alopecia): Open Targets Query (androgenetic alopecia, 20 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (souza2026useofgenetics pages 3-4): Gustavo Torres de Souza, Greg Williams, Carolina Costa Vicente Silva, Caroline Brandão Chiovatto, Gorana Kuka Epstein, Laura Vila-Vecilla, and Valentina Russo. Use of genetics in the prediction of success in male pattern hair loss therapy and mechanistic studies. Frontiers in Pharmacology, Feb 2026. URL: https://doi.org/10.3389/fphar.2026.1765808, doi:10.3389/fphar.2026.1765808. This article has 1 citations.

6. (khare2023dermoscopyofhair pages 1-2): Soumil Khare, Biswanath Behera, Delaney D Ding, Aimilios Lallas, Payal Chauhan, Nkechi Anne Enechukwu, Martyna Sławińska, Bengu Nisa Akay, Balachandra S Ankad, Yasmeen J Bhat, Abhijeet Kumar Jha, Feroze Kaliyadan, Awatef Kelati, Shekhar Neema, Nisha V Parmar, Jennifer Stein, Richard P Usatine, Keshavamurthy Vinay, and Enzo Errichetti. Dermoscopy of hair and scalp disorders (trichoscopy) in skin of color—a systematic review by the international dermoscopy society “imaging in skin of color” task force. Dermatology Practical &amp; Conceptual, 13:e2023210S, Oct 2023. URL: https://doi.org/10.5826/dpc.1304s1a310s, doi:10.5826/dpc.1304s1a310s. This article has 16 citations.

7. (khare2023dermoscopyofhair pages 28-29): Soumil Khare, Biswanath Behera, Delaney D Ding, Aimilios Lallas, Payal Chauhan, Nkechi Anne Enechukwu, Martyna Sławińska, Bengu Nisa Akay, Balachandra S Ankad, Yasmeen J Bhat, Abhijeet Kumar Jha, Feroze Kaliyadan, Awatef Kelati, Shekhar Neema, Nisha V Parmar, Jennifer Stein, Richard P Usatine, Keshavamurthy Vinay, and Enzo Errichetti. Dermoscopy of hair and scalp disorders (trichoscopy) in skin of color—a systematic review by the international dermoscopy society “imaging in skin of color” task force. Dermatology Practical &amp; Conceptual, 13:e2023210S, Oct 2023. URL: https://doi.org/10.5826/dpc.1304s1a310s, doi:10.5826/dpc.1304s1a310s. This article has 16 citations.

8. (kumaresan2025adecadeof pages 1-2): Subalakshmi Kumaresan, Dhivya Palaniappan, Navakumar Manickam, Seethalakshmi Ganga Vellaisamy, and Kannan Gopalan. A decade of progress in androgenetic alopecia management: emerging therapies and multimodal strategies. IP Indian Journal of Clinical and Experimental Dermatology, 11(4):457-472, Dec 2025. URL: https://doi.org/10.18231/j.ijced.13629.1765276898, doi:10.18231/j.ijced.13629.1765276898. This article has 0 citations.

9. (burshtein2026emergingpharmacotherapiesand pages 2-3): Joshua Burshtein, Aaron Burshtein, and Todd Schlesinger. Emerging pharmacotherapies and regenerative solutions for promoting hair growth for androgenetic alopecia. Frontiers in Pharmacology, Mar 2026. URL: https://doi.org/10.3389/fphar.2026.1776134, doi:10.3389/fphar.2026.1776134. This article has 4 citations.

10. (britva2026regenerativestrategiesfor pages 19-19): Rimma Laufer Britva and Amos Gilhar. Regenerative strategies for androgenetic alopecia: evidence, mechanisms, and translational pathways. Cosmetics, 13(1):19, Jan 2026. URL: https://doi.org/10.3390/cosmetics13010019, doi:10.3390/cosmetics13010019. This article has 1 citations.

11. (toussi2021psychosocialandpsychiatric pages 28-30): Atrin Toussi, Virginia R. Barton, Stephanie T. Le, Oma N. Agbai, and Maija Kiuru. Psychosocial and psychiatric comorbidities and health-related quality of life in alopecia areata: a systematic review. Jul 2021. URL: https://doi.org/10.1016/j.jaad.2020.06.047, doi:10.1016/j.jaad.2020.06.047. This article has 260 citations and is from a domain leading peer-reviewed journal.

12. (gupta2025relativeefficacyof pages 2-2): Aditya K. Gupta, Mary A. Bamimore, and Mesbah Talukder. Relative efficacy of conventional monotherapies and select nonconventional, over‐the‐counter products for male androgenetic alopecia: a network meta‐analysis study. Journal of Cosmetic Dermatology, Oct 2025. URL: https://doi.org/10.1111/jocd.70483, doi:10.1111/jocd.70483. This article has 3 citations and is from a peer-reviewed journal.

13. (liu2026developmentandvalidation pages 13-13): Shizhao Liu, Wenzhen Li, Botian Jiang, Haoyang Li, Jian Chen, Zhe-Xiang Fan, Zhiqi Hu, Qian Qu, and Yong Miao. Development and validation of a comprehensive in vitro organ model for androgenetic alopecia. Jun 2026. URL: https://doi.org/10.1186/s12896-026-01176-4, doi:10.1186/s12896-026-01176-4. This article has 1 citations and is from a peer-reviewed journal.

14. (li2026riskfactorsfor pages 1-2): Haoyang Li, Wenzhen Li, Jiaxian Zhang, Qihong Liang, Yingjie Zhao, Zehong Guo, Botian Jiang, Zhan Wang, Qian Qu, Shengli An, and Yong Miao. Risk factors for androgenetic alopecia: a systematic review and meta-analysis. BMC Public Health, Jan 2026. URL: https://doi.org/10.1186/s12889-026-26258-y, doi:10.1186/s12889-026-26258-y. This article has 3 citations and is from a peer-reviewed journal.

15. (kumaresan2025adecadeof pages 6-8): Subalakshmi Kumaresan, Dhivya Palaniappan, Navakumar Manickam, Seethalakshmi Ganga Vellaisamy, and Kannan Gopalan. A decade of progress in androgenetic alopecia management: emerging therapies and multimodal strategies. IP Indian Journal of Clinical and Experimental Dermatology, 11(4):457-472, Dec 2025. URL: https://doi.org/10.18231/j.ijced.13629.1765276898, doi:10.18231/j.ijced.13629.1765276898. This article has 0 citations.

16. (gupta2025relativeefficacyof pages 6-6): Aditya K. Gupta, Mary A. Bamimore, and Mesbah Talukder. Relative efficacy of conventional monotherapies and select nonconventional, over‐the‐counter products for male androgenetic alopecia: a network meta‐analysis study. Journal of Cosmetic Dermatology, Oct 2025. URL: https://doi.org/10.1111/jocd.70483, doi:10.1111/jocd.70483. This article has 3 citations and is from a peer-reviewed journal.

17. (kumaresan2025adecadeof pages 11-12): Subalakshmi Kumaresan, Dhivya Palaniappan, Navakumar Manickam, Seethalakshmi Ganga Vellaisamy, and Kannan Gopalan. A decade of progress in androgenetic alopecia management: emerging therapies and multimodal strategies. IP Indian Journal of Clinical and Experimental Dermatology, 11(4):457-472, Dec 2025. URL: https://doi.org/10.18231/j.ijced.13629.1765276898, doi:10.18231/j.ijced.13629.1765276898. This article has 0 citations.

18. (NCT07563036 chunk 2): heba ahmed abdelgayed ibrahim. JAK2 Expression in Androgenetic Alopecia Before and After Topical Minoxidil. Kasr El Aini Hospital. 2026. ClinicalTrials.gov Identifier: NCT07563036

## Artifacts

- [Edison artifact artifact-00](Androgenetic_Alopecia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.