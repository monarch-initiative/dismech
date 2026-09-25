---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T14:10:36.567964'
end_time: '2026-09-06T14:21:50.782779'
duration_seconds: 674.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Dominant Hypercholesterolemia 3
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 13
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Hypercholesterolemia_3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Hypercholesterolemia 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Hypercholesterolemia 3** covering all of the
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
- **Disease Name:** Autosomal Dominant Hypercholesterolemia 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Hypercholesterolemia 3** covering all of the
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


# Autosomal Dominant Hypercholesterolemia 3: Disease-Characteristics Report

## Executive summary and evidence scope

Autosomal dominant hypercholesterolemia 3 (ADH3; FH3/HCHOLA3) is the rare familial-hypercholesterolemia subtype caused by **heterozygous germline gain-of-function (GOF) variants in PCSK9**. Excess PCSK9 activity decreases hepatocyte-surface LDL receptor (LDLR), causing lifelong elevation of LDL cholesterol (LDL-C), cumulative arterial cholesterol exposure, and premature atherosclerotic cardiovascular disease (ASCVD). The phenotype overlaps LDLR- and APOB-associated familial hypercholesterolemia (FH), so ADH3 is defined molecularly rather than by unique clinical findings. Direct ADH3 evidence is dominated by pedigrees and functional studies; most management and outcome estimates necessarily come from broader heterozygous FH cohorts.

| Domain | Evidence scope | Core fact |
|---|---|---|
| Disease identity | ADH3-specific | Autosomal dominant hypercholesterolemia 3 (ADH3; FH3/HCHOLA3) is the **PCSK9 gain-of-function subtype** of familial hypercholesterolemia. The locus was mapped to chromosome 1p32, and the causal relationship was established in 2003 ([DOI](https://doi.org/10.1038/ng1161)). (seidah2017thepcsk9revolution pages 3-6, abifadel2003mutationsinpcsk9 pages 2-2) |
| Causal gene and mechanism | ADH3-specific | Germline gain-of-function variants in **PCSK9** enhance loss of hepatic LDL receptors. Secreted PCSK9 binds the LDLR EGF-A domain and directs the complex to late endosomes/lysosomes rather than receptor recycling, reducing hepatic LDL clearance and raising plasma LDL-C. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, mcnutt2010characterizationofthe pages 115-119, weider2017inhibitionofthea pages 152-156) |
| Inheritance | ADH3-specific | Autosomal dominant; heterozygous variants segregate with hypercholesterolemia, although expressivity and cardiovascular severity vary within and between families. Biallelic PCSK9 gain-of-function disease can produce an exceptionally severe, HoFH-like phenotype but is not the usual ADH3 presentation. (allard2005novelmutationsof pages 3-6, allard2005novelmutationsof pages 1-3, abifadel2003mutationsinpcsk9 pages 2-2) |
| Hallmark phenotype | ADH3-specific | Lifelong elevation of LDL-C/type IIa hypercholesterolemia, sometimes accompanied by tendon xanthomas, corneal arcus, and premature coronary disease. One p.Arg218Ser proband had untreated LDL-C **293 mg/dL**, tendon xanthoma, and corneal arcus at age 45; an original p.Phe216Leu carrier died from myocardial infarction at age 49. (allard2005novelmutationsof pages 3-6, abifadel2003mutationsinpcsk9 pages 2-2) |
| Key variants | ADH3-specific | Landmark variants include **p.Ser127Arg** and **p.Phe216Leu**; reported variants also include **p.Asp374Tyr, p.Arg218Ser, p.Arg357His, p.Ala443Thr, and p.Arg469Trp**. p.Asp374Tyr increases PCSK9–LDLR affinity by about **10-fold** and is associated with severe disease. Variant pathogenicity must be assessed individually because not every rare PCSK9 variant is gain-of-function. (allard2005novelmutationsof pages 3-6, allard2005novelmutationsof pages 1-3, weider2017inhibitionofthe pages 152-156, abifadel2003mutationsinpcsk9 pages 2-2) |
| Epidemiology caveat | Mixed | ADH3-specific prevalence is not well quantified. PCSK9 gain-of-function variants account for approximately **1% of FH cases** in a 2024 review and about **2.3% of LDLR/APOB-negative ADH** in one 130-patient series. These selected-cohort figures should not be treated as population prevalence. General FH prevalence is approximately **1:311**, affecting more than 34 million people worldwide. (allard2005novelmutationsof pages 1-3, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, marquina2024costeffectivenessofscreening pages 1-2) |
| Diagnosis | General FH framework plus ADH3 confirmation | Diagnose the FH phenotype using repeated untreated LDL-C, premature ASCVD and family history, and physical signs; exclude secondary hypercholesterolemia. Confirm ADH3 through an FH panel including **LDLR, APOB, PCSK9**, and other validated genes, with segregation and functional/curated evidence for a pathogenic or likely pathogenic **PCSK9 gain-of-function** variant. A PCSK9 VUS or loss-of-function allele does not establish ADH3. (allard2005novelmutationsof pages 1-3, watts2023internationalatherosclerosissociety pages 7-8, yip2023geneticspectrumand pages 5-6) |
| Treatment | General FH evidence, mechanistically well matched to ADH3 | Begin early intensive LDL lowering: maximally tolerated high-intensity statin, add ezetimibe, then a PCSK9-directed agent if goals are unmet. Ezetimibe lowers LDL-C about **18%** alone and provides about **20% additional lowering** with statins; alirocumab/evolocumab typically lower LDL-C about **60%**. General FH targets are ≥**50% reduction** and LDL-C below **70 mg/dL** in high-risk disease or below **55 mg/dL** in very-high-risk disease. (fularski2024unveilingfamilialhypercholesterolemia—review pages 10-12, fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9) |
| Prevention and screening | General FH evidence applicable to ADH3 families | Primary prevention cannot remove an inherited allele, but diet, exercise, avoidance of smoking, and control of other cardiovascular risks reduce downstream risk. Perform cascade lipid and targeted-variant testing in first-degree relatives; combined cascade and young-age universal screening could identify more than **90%** of FH. Cascade screening was cost-effective in **78%** of studies and yielded the greatest health benefit per person tested. (marquina2024costeffectivenessofscreening pages 1-2, watts2023internationalatherosclerosissociety pages 1-2, watts2023internationalatherosclerosissociety pages 7-8) |
| Evidence limitations | ADH3-specific caveat | ADH3 is rare, so most phenotype, prognosis, quality-of-life, and treatment estimates are extrapolated from broader HeFH cohorts rather than PCSK9-genotyped trials. Published evidence is dominated by pedigrees, variant-functional studies, and engineered models; no reliable subtype-specific incidence, penetrance percentage, sex ratio, survival curve, or spontaneous nonhuman disease series was identified. (allard2005novelmutationsof pages 3-6, rochemolina2015inductionofsustained pages 1-2, rochemolina2015inductionofsustained pages 10-10) |


*Table: This table separates evidence specific to PCSK9 gain-of-function ADH3 from findings extrapolated from familial hypercholesterolemia generally. It summarizes defining genetics, phenotype, diagnosis, management, screening, quantitative findings, and major evidence gaps.*

## 1. Disease information

### Definition, names, and identifiers

**Preferred name:** autosomal dominant hypercholesterolemia 3. Common alternatives are **ADH3**, **familial hypercholesterolemia 3**, **FH3**, **HCHOLA3**, **PCSK9-related familial hypercholesterolemia**, and **PCSK9 gain-of-function hypercholesterolemia**. The original locus was mapped to chromosome 1p32, and the 2003 landmark study identified PCSK9 variants in two linked French families. Its abstract states that the investigators “mapped a third locus associated with ADH, HCHOLA3 at 1p32” and found two causal PCSK9 mutations. DOI: https://doi.org/10.1038/ng1161; publication: June 2003. (seidah2017thepcsk9revolution pages 3-6, abifadel2003mutationsinpcsk9 pages 2-2)

**Identifier caution:** the retrieved primary literature uses **MIM 607786** for the PCSK9-associated hypercholesterolemia phenotype and **MIM 607786/603776-related notation** in older records; an older article also cites MIM 143890 for the broader ADH phenotype. These historical numbers should be reconciled directly against the current OMIM record before database ingestion. A definitive subtype-specific MONDO identifier was not recovered by the available tools; use the current MONDO familial-hypercholesterolemia parent mapping only after curator verification. Broader coding generally uses familial/pure hypercholesterolemia categories (for example ICD-10-CM E78.01), because ICD and MeSH do not ordinarily distinguish ADH3 by gene. (allard2005novelmutationsof pages 1-3)

**Data provenance:** the disease definition and variant–phenotype relationships derive from aggregated disease resources, pedigrees, lipid-clinic cohorts, and experimental studies—not individual-level EHR data in this report. Recent implementation studies use aggregated clinical records, but their findings concern FH generally rather than PCSK9-genotyped ADH3.

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

ADH3 is caused by a **germline PCSK9 GOF allele**. Pathogenicity is mechanism-specific: rare PCSK9 variants can be GOF, loss-of-function (LOF), neutral, or uncertain, so merely finding a rare PCSK9 allele is insufficient. GOF mechanisms include enhanced LDLR binding, altered intracellular trafficking or secretion, resistance to inactivation, increased stability, and reduced inhibitory binding of PCSK9 to LDL particles. A 2024 review estimated that PCSK9 GOF variants cause approximately 1% of FH and listed about 36 pathogenic/probably pathogenic variants, although database totals evolve. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)

### Risk factors and modifiers

* **Genetic:** one pathogenic PCSK9 GOF allele, a second pathogenic FH allele, high polygenic LDL-C burden, and other ASCVD-risk alleles can increase severity. A PCSK9 p.Arg469Trp carrier with a coexisting LDLR frameshift had especially severe disease, illustrating additive monogenic effects. Expressivity also varied among p.Arg218Ser relatives. (allard2005novelmutationsof pages 3-6, allard2005novelmutationsof pages 1-3)
* **Clinical/environmental:** smoking, hypertension, diabetes, obesity, inactivity, an atherogenic diet, elevated lipoprotein(a), and delayed or inadequate LDL-lowering do not cause ADH3 but increase downstream ASCVD risk. Lifelong LDL exposure begins at birth; broader FH guidance therefore treats cumulative LDL-C as the dominant causal exposure. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9, watts2023internationalatherosclerosissociety pages 1-2, watts2023internationalatherosclerosissociety pages 7-8)
* **Pregnancy:** physiological lipid increases can magnify hypercholesterolemia; markedly high cholesterol during pregnancy was reported in a p.Arg357His carrier. (allard2005novelmutationsof pages 1-3)

### Protective factors

PCSK9 LOF alleles lower LDL-C and coronary risk but are not a practical within-patient “protective modifier” once a causal GOF allele is present. Environmental protection consists chiefly of early sustained LDL-C lowering, smoking avoidance, exercise, heart-healthy dietary patterns, normal weight, and control of blood pressure and diabetes. These interventions reduce cardiovascular consequences, not inheritance of ADH3. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, mcnutt2010characterizationofthea pages 115-119)

A gene–treatment interaction is important: statins activate SREBP2 and increase both LDLR and PCSK9 expression. PCSK9 blockade preserves more of the statin-induced LDLR, explaining their mechanistic synergy. (mcnutt2010characterizationofthe pages 115-119, mcnutt2010characterizationofthea pages 115-119)

## 3. Phenotypes

ADH3-specific phenotype frequencies cannot be estimated reliably from the small published pedigrees. Suggested ontology annotations are therefore qualitative.

* **Elevated LDL-C / type IIa hyperlipoproteinemia**—laboratory abnormality, present from birth, chronic and usually progressive in cumulative impact; severity ranges from mild to very severe. Suggested HPO: **Hypercholesterolemia (HP:0003124)** and **Elevated circulating LDL cholesterol concentration**. A p.Arg218Ser proband had untreated total cholesterol 402 mg/dL and LDL-C 293 mg/dL at age 45. (allard2005novelmutationsof pages 3-6)
* **Tendon xanthoma**—physical sign caused by cholesterol deposition, usually appearing after prolonged severe exposure but potentially in childhood in severe FH. Suggested HPO: **Tendon xanthomatosis (HP:0000991)**. The p.Arg218Ser proband had tendinous xanthoma. (allard2005novelmutationsof pages 3-6)
* **Corneal arcus**—bilateral peripheral corneal lipid deposition, particularly informative when premature. Suggested HPO: **Corneal arcus (HP:0001084)**. It was present in the same p.Arg218Ser proband. (allard2005novelmutationsof pages 3-6)
* **Premature coronary atherosclerosis, angina, myocardial infarction, and cardiovascular death**—downstream complications, age-dependent and progressive. Suggested HPO: **Premature atherosclerosis (HP:0002621)**, **Coronary artery disease (HP:0001677)**, and **Myocardial infarction (HP:0001658)**. An original p.Phe216Leu carrier died from myocardial infarction at 49 years; p.Asp374Tyr is associated with particularly severe disease and premature cardiovascular death. (weider2017inhibitionofthe pages 152-156, abifadel2003mutationsinpcsk9 pages 2-2)
* **Aortic/other arterial atherosclerosis**—expected from the FH disease process, but no reliable ADH3-specific frequency was recovered.

Quality of life is usually unaffected by the biochemical phenotype itself until treatment burden, anxiety, xanthomas, angina, or vascular events intervene. No ADH3-specific EQ-5D, SF-36, or PROMIS study was identified. In general FH, childhood treatment is expected to improve quality of life and reduce later mortality. (watts2023internationalatherosclerosissociety pages 1-2)

## 4. Genetic and molecular information

**Causal gene:** **PCSK9**, chromosome 1p32.3; HGNC:20001 (curator should verify current HGNC/Ensembl cross-references). It encodes proprotein convertase subtilisin/kexin type 9, formerly NARC-1. PCSK9 is synthesized as a zymogen and autocatalytically cleaved in the endoplasmic reticulum; cleavage enables ER exit. (seidah2017thepcsk9revolution pages 3-6, abifadel2003mutationsinpcsk9 pages 2-2)

### Representative variants

* **p.Ser127Arg (S127R)** and **p.Phe216Leu (F216L):** original heterozygous variants establishing causality. S127R affects the prodomain/processing region and can inhibit normal LDL binding; F216L lies near catalytic His226. (seidah2017thepcsk9revolution pages 3-6, abifadel2003mutationsinpcsk9 pages 2-2)
* **p.Asp374Tyr (D374Y):** strong GOF missense variant with approximately tenfold greater LDLR affinity, severe hypercholesterolemia, and premature cardiovascular disease. (weider2017inhibitionofthe pages 152-156, rochemolina2015inductionofsustained pages 1-2)
* **p.Arg218Ser (R218S):** heterozygous catalytic-domain variant that cosegregated in four relatives and was absent from 415 diverse controls; functional effect was not demonstrated in the original report, so modern classification should incorporate current ClinVar/ClinGen evidence. (allard2005novelmutationsof pages 3-6)
* **p.Arg357His, p.Ala443Thr, and p.Arg469Trp:** reported in LDLR/APOB-negative ADH screening; original evidence and segregation strength varied. (allard2005novelmutationsof pages 1-3)
* **Regulatory variation:** a 2024 study of 409 suspected-FH patients found rare LDLR/PCSK9 3′UTR variants; PCSK9 c.*950C>T increased reporter expression by 41%. This is emerging FH evidence and should not automatically be labeled definitive ADH3 without segregation and clinical functional validation. DOI: https://doi.org/10.1155/2024/9964734; February 2024. (otero2024functionalanalysisof pages 4-5)

All established disease alleles are **germline**. Somatic origin is not characteristic. Most reported alleles are missense; the functional endpoint is GOF rather than simple haploinsufficiency. Population frequency should be extremely low for highly penetrant pathogenic alleles, but exact gnomAD frequencies must be entered variant by variant. No recurrent chromosomal abnormality, repeat expansion, mitochondrial defect, or disease-defining structural variant is established.

### Modifiers and epigenetics

No validated ADH3-specific modifier gene or epigenetic lesion is established. A 2024 FH study found differential LDLR, PCSK9, and LDLRAP1 methylation associated with clinical manifestations and cardiovascular events in 131 patients, but this remains a potential biomarker in mixed-genotype FH, not a proven cause or modifier of ADH3.

## 5. Environmental information

No toxin, radiation exposure, occupational agent, or infectious pathogen causes ADH3. Diet, adiposity, inactivity, smoking, diabetes, and hypertension modify LDL-C or vascular consequences. Infectious-agent and zoonotic fields are **not applicable**. Lifestyle intervention is necessary but is rarely sufficient to normalize genetically elevated LDL-C. General FH evidence shows that cumulative pathogenic LDL exposure can be reached by approximately age 12.5 years versus around 55 years without FH, emphasizing that lifestyle advice must not delay pharmacotherapy. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline **PCSK9 GOF variant leads to** increased effective PCSK9 activity through enhanced LDLR affinity, altered trafficking/secretion, increased stability, impaired inactivation, or loss of normal LDL-mediated inhibition.
2. Increased active PCSK9 **leads to** greater binding of LDLR’s EGF-A domain at the hepatocyte surface and/or within the secretory pathway.
3. The PCSK9–LDLR complex **results in** sorting to late endosomes and lysosomes rather than recycling of LDLR to the plasma membrane.
4. Accelerated LDLR degradation **leads to** reduced cell-surface LDLR on hepatocytes.
5. Reduced receptor abundance **results in** impaired hepatic uptake of apoB-containing LDL particles and lifelong elevation of plasma LDL-C.
6. Chronic LDL-C exposure **leads to** arterial-wall LDL retention and modification.
7. Retained lipoprotein **results in** endothelial dysfunction and macrophage uptake/foam-cell formation; direct LDLR-independent PCSK9 inflammatory effects are plausible but remain less firmly demonstrated in human ADH3.
8. Lipid accumulation, inflammation, smooth-muscle responses, oxidative stress, calcification, and fibrous-cap remodeling **lead to** progressive atherosclerotic plaque.
9. Plaque growth or rupture **results in** coronary disease, myocardial infarction, stroke, and premature death; extravascular cholesterol deposition branches to tendon xanthomas and corneal arcus. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, mcnutt2010characterizationofthe pages 115-119, rochemolina2015inductionofsustained pages 1-2, weider2017inhibitionofthea pages 152-156)

The upstream lesion is variant-specific PCSK9 GOF; LDLR depletion and high LDL-C are central demonstrated intermediates. Arterial inflammation and tissue injury are downstream. D374Y increases PCSK9–LDLR affinity by at least tenfold. S127R/D129G can show abnormal secretion or intracellular activity, demonstrating that not all variants act identically. (rochemolina2015inductionofsustained pages 1-2, matiasperez2021pcsk9geneparticipates pages 2-4)

**Suggested GO terms:** regulation of receptor-mediated endocytosis; low-density lipoprotein particle receptor catabolic process; cholesterol homeostasis; lipoprotein metabolic process; endosomal transport; lysosomal protein catabolic process; receptor recycling; foam-cell differentiation; inflammatory response; response to oxidative stress.

**Suggested Cell Ontology terms:** hepatocyte (**CL:0000182**) as the principal causal cell; enterocyte (**CL:0000584**), macrophage (**CL:0000235**), endothelial cell (**CL:0000115**), vascular smooth-muscle cell, pancreatic beta cell, and adipocyte as secondary/contextual populations.

Molecular profiling is limited. No ADH3-specific clinical single-cell, spatial-transcriptomic, proteomic, or multi-omic atlas was identified. A genome-wide expression analysis of D374Y-expressing cells and newer methylation/3′UTR studies are exploratory rather than diagnostic. PCSK9 is regulated with LDLR by SREBP2 and is expressed mainly in hepatocytes, with lower expression reported in intestine, kidney, pancreatic islets, and cerebellum. (mcnutt2010characterizationofthe pages 115-119, weider2017inhibitionofthea pages 152-156, weider2017inhibitionofthe pages 64-68)

## 7. Anatomical structures affected

* **Primary organ/process:** liver—hepatocytes regulate circulating LDL clearance. Suggested UBERON: **liver (UBERON:0002107)**.
* **Primary injured system:** cardiovascular system, especially coronary arteries and aorta. Suggested UBERON: **aorta (UBERON:0000947)**, **coronary artery**, arterial wall/intima, and heart.
* **Secondary deposition sites:** tendons and corneal periphery; usually bilateral/systemic rather than lateralized.
* **Subcellular compartments:** endoplasmic reticulum, Golgi/trans-Golgi network, plasma membrane, endosome, late endosome, and lysosome. Corresponding GO Cellular Component annotations should include ER lumen, Golgi apparatus, cell surface, endosome, and lysosome. PCSK9’s C-terminal domain supports trafficking of the PCSK9–LDLR complex toward late endocytic compartments. (mcnutt2010characterizationofthe pages 115-119, rochemolina2015inductionofsustained pages 1-2, weider2017inhibitionofthea pages 152-156)

## 8. Temporal development

The biochemical phenotype begins **from birth** because the causal allele is constitutional. Clinical onset is chronic and insidious. Early-stage disease consists of isolated LDL-C elevation; intermediate disease may include arcus, tendon xanthomas, and subclinical plaque; advanced disease includes symptomatic coronary or other arterial disease. The course is lifelong and cumulative, not episodic or spontaneously remitting. Treatment can normalize or substantially reduce LDL-C and arrest or delay complications but does not eliminate the genotype. Childhood is the critical preventive window. In broader FH cohorts treated from youth, ASCVD occurred in 1% of treated offspring versus 26% of affected parents, and mortality was 0% versus 7%, supporting early intervention even though these figures are not ADH3-specific. (watts2023internationalatherosclerosissociety pages 9-10)

## 9. Inheritance and population

Inheritance is **autosomal dominant**; each child of a heterozygous affected individual has a 50% transmission probability. Penetrance for elevated LDL-C is considered high but is age-, variant-, treatment-, and threshold-dependent. Expressivity is variable, as demonstrated within the p.Arg218Ser family. Anticipation is not established. Germline mosaicism is theoretically possible but not a recognized recurrent feature; consanguinity is not required. Biallelic GOF variants or dual molecular diagnoses may cause an HoFH-like extreme phenotype. (allard2005novelmutationsof pages 3-6, watts2023internationalatherosclerosissociety pages 1-2)

Reliable ADH3-specific prevalence, incidence, carrier frequency, sex ratio, and geographic distribution are unavailable. PCSK9 GOF variants account for about 1% of FH in a recent review and 2.3% of LDLR/APOB-negative cases in one selected 130-patient series; these are not population-prevalence estimates. General heterozygous FH prevalence is approximately 1:311, or more than 34 million people worldwide. Males and females inherit ADH3 equally, although sex and conventional risk factors may alter event timing. (allard2005novelmutationsof pages 1-3, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, marquina2024costeffectivenessofscreening pages 1-2)

Founder effects may occur for individual alleles, but no single global ADH3 founder variant was established in the retrieved evidence.

## 10. Diagnostics

### Clinical and biochemical assessment

Obtain at least two fasting or nonfasting lipid profiles where feasible, documenting untreated or estimated pretreatment LDL-C. Assess family history of markedly elevated LDL-C and premature ASCVD, tendon xanthomas, corneal arcus, blood pressure, diabetes, smoking, renal/liver/thyroid status, and lipoprotein(a). Use a validated FH framework such as Dutch Lipid Clinic Network, Simon Broome, MEDPED, or a national pediatric criterion. General FH guidelines characterize the triad as hyper-LDL-cholesterolemia, premature coronary disease, and tendon/skin xanthomas. (watts2023internationalatherosclerosissociety pages 7-8, yip2023geneticspectrumand pages 5-6)

Exclude secondary hypercholesterolemia: hypothyroidism, nephrotic syndrome, cholestatic liver disease, chronic kidney disease, uncontrolled diabetes, medications, and severe dietary causes. Molecular differential diagnosis includes **LDLR-related FH, APOB-related familial defective apoB, APOE p.Leu167del hypercholesterolemia, LDLRAP1-related recessive hypercholesterolemia, ABCG5/ABCG8 sitosterolemia**, polygenic hypercholesterolemia, and elevated lipoprotein(a).

### Genetic testing

Use an accredited NGS FH panel including at least **LDLR, APOB, PCSK9, and LDLRAP1**, with deletion/duplication analysis and additional validated genes where appropriate. A pathogenic/likely pathogenic **PCSK9 GOF** allele plus a compatible phenotype confirms ADH3. Report VUS separately and do not use one alone for predictive diagnosis. Functional evidence is unusually important because PCSK9 has both GOF and LOF alleles. Family segregation and targeted testing of relatives strengthen interpretation. (allard2005novelmutationsof pages 1-3, watts2023internationalatherosclerosissociety pages 7-8)

Single-gene PCSK9 testing is reasonable when a familial variant is known. WES/WGS may identify deep-intronic, regulatory, or structural variants after a negative panel, but interpretation—not sequencing—is the chief limitation. RNA-seq or reporter assays remain research tools. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine.

Imaging is for complication assessment, not molecular diagnosis: coronary calcium/CT angiography may aid selected adult risk stratification; carotid ultrasound can show plaque. Routine pediatric coronary CT/calcium scoring is discouraged, whereas severe or homozygous-like presentations require specialist cardiovascular imaging. (watts2023internationalatherosclerosissociety pages 9-10)

### Screening implementation

Cascade lipid and targeted-variant testing should begin with first-degree relatives and extend through the pedigree. Combined cascade testing and young-age universal screening could identify more than 90% of FH. Yet only about 10% of affected people worldwide are diagnosed, and over 80% of treated patients fail recommended LDL-C goals. (watts2023internationalatherosclerosissociety pages 1-2, watts2023internationalatherosclerosissociety pages 7-8)

## 11. Outcome and prognosis

Untreated prognosis is governed chiefly by cumulative LDL-C and other cardiovascular risks. General FH carries approximately tenfold higher coronary-heart-disease risk than the general population. ADH3-specific survival curves, five- or ten-year survival, disability rates, and validated prognostic models are unavailable. Severe D374Y disease and the myocardial-infarction death at age 49 in an F216L family illustrate the potential natural history but cannot define average prognosis. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9, weider2017inhibitionofthe pages 152-156, abifadel2003mutationsinpcsk9 pages 2-2)

Adverse prognostic factors include higher untreated LDL-C, earlier xanthomas, established ASCVD, smoking, hypertension, diabetes, elevated lipoprotein(a), a second FH allele, and delayed/inadequate treatment. Favorable factors are early diagnosis, sustained LDL-C goal attainment, adherence, and control of all risk factors. Recovery from an established infarction or stroke is incomplete, but plaque progression and future events are preventable.

## 12. Treatment

ADH3 should be treated as high-risk heterozygous FH, intensified for severe phenotype or established ASCVD.

1. **Lifestyle and risk-factor control:** heart-healthy diet, physical activity, weight management, no smoking, and treatment of hypertension/diabetes. Lifestyle is adjunctive, not a substitute for medication.
2. **High-intensity statin:** atorvastatin or rosuvastatin unless contraindicated. Suggested NCIT concept: HMG-CoA reductase inhibitor therapy. Statin-associated muscle symptoms occur in roughly 10–15%; rhabdomyolysis is about 1–3 per 100,000 person-years and new-onset diabetes risk rises approximately 9% in broader populations. (fularski2024unveilingfamilialhypercholesterolemia—review pages 10-12)
3. **Add ezetimibe:** inhibits NPC1L1 intestinal cholesterol uptake; about 18% LDL-C lowering alone and about 20% additional lowering with a statin. Suggested NCIT: ezetimibe treatment. (fularski2024unveilingfamilialhypercholesterolemia—review pages 10-12)
4. **Add PCSK9-directed treatment:** alirocumab or evolocumab antibodies typically lower LDL-C about 60%; inclisiran suppresses hepatic PCSK9 synthesis. These are mechanistically well matched to PCSK9 GOF, although no genotype-specific randomized ADH3 trial was recovered. Injection-site reactions and flu-like symptoms are typical antibody adverse effects. (jeswani2024pcsk9inhibitorsthe pages 1-3, fularski2024unveilingfamilialhypercholesterolemia—review pages 10-12)
5. **Further options:** bempedoic acid, bile-acid sequestrants, or specialist combination therapy. Lipoprotein apheresis is reserved for exceptionally severe or refractory disease, especially biallelic/HoFH-like presentations.

ESC/EAS-derived general FH goals are at least a **50% LDL-C reduction** and LDL-C below **70 mg/dL (1.8 mmol/L)** for high-risk FH without ASCVD/major risk factors, or below **55 mg/dL (1.4 mmol/L)** for very-high-risk disease. Children generally begin statins at 8–10 years; one guideline target after age 10 is below 135–140 mg/dL, adjusted to national guidance and risk. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9)

Relevant registered studies found by the trial search include ORION-9 inclisiran in HeFH (**NCT03397121**, phase 3, 482 participants), pediatric evolocumab (**NCT02624869**, phase 3, 163), pediatric inclisiran (**NCT06597019**, recruiting phase 3, planned 60), and alirocumab plaque-burden assessment (**NCT05465278**, phase 4, 104). These enroll phenotypic FH, not specifically ADH3, and should not be presented as genotype-specific trials.

Emerging nucleic-acid and gene-editing approaches aim to silence or permanently disrupt hepatic PCSK9. They are conceptually attractive but experimental for inherited PCSK9 GOF and raise irreversibility, off-target, delivery, and long-term safety issues. DOI for a 2024 review: https://doi.org/10.1161/CIRCULATIONAHA.123.067957; August 2024.

Suggested CHEBI entities include cholesterol, LDL cholesterol/esterified cholesterol, atorvastatin, rosuvastatin, ezetimibe, and bempedoic acid. Suggested NCIT intervention classes include statin therapy, cholesterol-absorption inhibitor therapy, monoclonal-antibody therapy, small-interfering-RNA therapy, and therapeutic apheresis.

## 13. Prevention

**Primary prevention of the genotype** is impossible after conception. Reproductive options following counseling include prenatal diagnosis or preimplantation genetic testing for a known familial variant; decisions must remain nondirective.

**Secondary prevention** is central: childhood lipid screening, molecular confirmation, and cascade testing permit treatment before plaque develops. In a 2024 systematic review of 21 studies and 62 strategies, cascade screening was cost-effective in 78% of studies, opportunistic screening in 85%, systematic screening in 80%, and population-wide screening in 60%; cascade testing produced the greatest health benefit per person tested. DOI: https://doi.org/10.1007/s40273-023-01347-7; January 2024. (marquina2024costeffectivenessofscreening pages 1-2)

**Tertiary prevention** consists of sustained LDL-C reduction, smoking avoidance, blood-pressure and diabetes control, antiplatelet therapy when otherwise indicated, cardiac rehabilitation after events, and surveillance of established ASCVD. Vaccination and antimicrobial prophylaxis are not disease-specific interventions.

## 14. Other species and natural disease

No convincing naturally occurring veterinary syndrome caused by orthologous PCSK9 GOF was identified. Therefore, breed, VBO, natural-disease prevalence, zoonotic transmission, and cross-species transmission are **not applicable/not established**. PCSK9 is evolutionarily conserved across mammals, and engineered mouse, hamster, and pig systems reproduce LDLR depletion and hypercholesterolemia. All such examples should be annotated as experimental, not spontaneous disease. (rochemolina2015inductionofsustained pages 1-2, rochemolina2015inductionofsustained pages 10-10, matiasperez2021pcsk9geneparticipates pages 2-4)

Useful taxa include *Mus musculus* (NCBI Taxon 10090), *Mesocricetus auratus* (10036), and *Sus scrofa* (9823); ortholog identifiers should be drawn directly from current NCBI Gene/Alliance records during database curation.

## 15. Model organisms and experimental systems

* **AAV-PCSK9-D374Y mouse:** one intravenous AAV dose (3.5×10^10 viral particles) induced sustained LDL elevation in C57BL/6J, 129/Sv, and FVB mice. With high-fat diet, animals developed aortic plaques with macrophages and fibrous caps. In Apoe-null mice, D374Y doubled aortic-lesion extent despite unchanged serum cholesterol, suggesting downstream plaque effects or model interaction. DOI: https://doi.org/10.1161/ATVBAHA.114.303617; January 2015. (rochemolina2015inductionofsustained pages 1-2)
* **Adenoviral PCSK9 models:** murine PCSK9 increased total cholesterol about twofold and non-HDL cholesterol fivefold; human PCSK9 produced approximately ninefold higher LDL-C. Similar profiles in Ldlr-null mice established LDLR dependence. (weider2017inhibitionofthe pages 61-64)
* **Humanized BAC mice:** lines expressing approximately 95–5,000 ng/mL human PCSK9 showed expression-dependent increases in total cholesterol/apoB and reduced hepatic LDLR. (weider2017inhibitionofthe pages 152-156, weider2017inhibitionofthea pages 152-156)
* **D374Y transgenic/viral models:** D374Y increases LDLR affinity around tenfold; some engineered mice expressed about 14 μg/mL active PCSK9. (weider2017inhibitionofthe pages 152-156)
* **Engineered minipigs:** transgenic human PCSK9 GOF minipigs develop FH-like hypercholesterolemia and atherosclerosis, offering more human-like lipoprotein physiology than mice. The model is engineered, not natural disease. (rochemolina2015inductionofsustained pages 10-10, weider2017inhibitionofthe pages 64-68)
* **Cell systems:** HepG2, HuH7, primary hepatocytes, fibroblasts, and fluorescent PCSK9–LDLR trafficking assays test secretion, EGF-A binding, endocytosis, and lysosomal degradation. They are valuable for ACMG functional evidence but may not reproduce lifelong whole-body disease.

Major limitations are that mice lack CETP, viral overexpression may exceed physiological concentrations, liver-restricted vectors omit extrahepatic expression, and high-fat diets introduce environmental effects. BAC and large-animal models improve physiological relevance but remain costly and do not fully reproduce human coronary events. (weider2017inhibitionofthe pages 64-68)

## Recent developments and principal evidence gaps

Notable 2023–2024 developments include stronger international emphasis on combined universal/cascade screening, implementation science addressing the evidence-to-practice gap, functional study of PCSK9 3′UTR variants, methylation as a possible FH risk biomarker, wider real-world use of inclisiran and PCSK9 antibodies, and preclinical nucleic-acid/gene-editing approaches. Up to 80–90% of FH remains undiagnosed, while most treated patients remain above goal, making implementation—not merely discovery of additional drugs—a major expert priority. (otero2024functionalanalysisof pages 4-5, marquina2024costeffectivenessofscreening pages 1-2, watts2023internationalatherosclerosissociety pages 1-2)

Critical ADH3-specific gaps are: population prevalence and penetrance; standardized functional classification of rare PCSK9 alleles; variant-specific response to antibodies versus inclisiran; prospective natural history; patient-reported quality of life; pregnancy outcomes; ancestry-diverse cohorts; and long-term safety of permanent PCSK9 editing.

### Evidence-quality note

The strongest ADH3 evidence comprises the 2003 discovery pedigrees, later segregation studies, and convergent LDLR-trafficking experiments. Treatment targets and most quantitative outcome estimates are extrapolated from general HeFH because ADH3-specific randomized trials are absent. PMID values were not consistently exposed in the retrieved full texts; DOI URLs and publication dates are therefore supplied where verified rather than inventing PMID mappings.

References

1. (seidah2017thepcsk9revolution pages 3-6): Nabil G Seidah. The pcsk9 revolution and the potential of pcsk9-based therapies to reduce ldl-cholesterol. May 2017. URL: https://doi.org/10.21542/gcsp.2017.2, doi:10.21542/gcsp.2017.2. This article has 79 citations.

2. (abifadel2003mutationsinpcsk9 pages 2-2): Marianne Abifadel, Mathilde Varret, Jean-Pierre Rabès, Delphine Allard, Khadija Ouguerram, Martine Devillers, Corinne Cruaud, Suzanne Benjannet, Louise Wickham, Danièle Erlich, Aurélie Derré, Ludovic Villéger, Michel Farnier, Isabel Beucler, Eric Bruckert, Jean Chambaz, Bernard Chanu, Jean-Michel Lecerf, Gerald Luc, Philippe Moulin, Jean Weissenbach, Annick Prat, Michel Krempf, Claudine Junien, Nabil G Seidah, and Catherine Boileau. Mutations in pcsk9 cause autosomal dominant hypercholesterolemia. Nature Genetics, 34:154-156, Jun 2003. URL: https://doi.org/10.1038/ng1161, doi:10.1038/ng1161. This article has 4016 citations and is from a highest quality peer-reviewed journal.

3. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

4. (mcnutt2010characterizationofthe pages 115-119): MC McNutt. Characterization of the non-proteolytic mechanism and cellular site of action of pcsk9-mediated degradation of the low-density lipoprotein receptor. Unknown journal, 2010.

5. (weider2017inhibitionofthea pages 152-156): E Weider. Inhibition of the proprotein convertase subtilisin/kexin type 9 (pcsk9) for the treatment of familial hypercholesterolemia. Unknown journal, 2017.

6. (allard2005novelmutationsof pages 3-6): Delphine Allard, Sabine Amsellem, Marianne Abifadel, Mélanie Trillard, Martine Devillers, Gérald Luc, Michel Krempf, Yves Reznik, Jean-Philippe Girardet, Alexandre Fredenrich, Claudine Junien, Mathilde Varret, Catherine Boileau, Pascale Benlian, and Jean-Pierre Rabès. Novel mutations of the pcsk9 gene cause variable phenotype of autosomal dominant hypercholesterolemia. Human Mutation, 26:497-497, Nov 2005. URL: https://doi.org/10.1002/humu.9383, doi:10.1002/humu.9383. This article has 269 citations and is from a domain leading peer-reviewed journal.

7. (allard2005novelmutationsof pages 1-3): Delphine Allard, Sabine Amsellem, Marianne Abifadel, Mélanie Trillard, Martine Devillers, Gérald Luc, Michel Krempf, Yves Reznik, Jean-Philippe Girardet, Alexandre Fredenrich, Claudine Junien, Mathilde Varret, Catherine Boileau, Pascale Benlian, and Jean-Pierre Rabès. Novel mutations of the pcsk9 gene cause variable phenotype of autosomal dominant hypercholesterolemia. Human Mutation, 26:497-497, Nov 2005. URL: https://doi.org/10.1002/humu.9383, doi:10.1002/humu.9383. This article has 269 citations and is from a domain leading peer-reviewed journal.

8. (weider2017inhibitionofthe pages 152-156): E Weider. Inhibition of the proprotein convertase subtilisin/kexin type 9 (pcsk9) for the treatment of familial hypercholesterolemia. Unknown journal, 2017.

9. (marquina2024costeffectivenessofscreening pages 1-2): Clara Marquina, Jedidiah I Morton, Melanie Lloyd, Dina Abushanab, Yeji Baek, Tamrat Abebe, Adam Livori, Padam Dahal, Gerald F. Watts, and Zanfina Ademi. Cost-effectiveness of screening strategies for familial hypercholesterolaemia: an updated systematic review. Pharmacoeconomics, 42:373-392, Jan 2024. URL: https://doi.org/10.1007/s40273-023-01347-7, doi:10.1007/s40273-023-01347-7. This article has 24 citations and is from a domain leading peer-reviewed journal.

10. (watts2023internationalatherosclerosissociety pages 7-8): Gerald F. Watts, Samuel S. Gidding, Robert A. Hegele, Frederick J. Raal, Amy C. Sturm, Laney K. Jones, Mitchell N. Sarkies, Khalid Al-Rasadi, Dirk J. Blom, Magdalena Daccord, Sarah D. de Ferranti, Emanuela Folco, Peter Libby, Pedro Mata, Hapizah M. Nawawi, Uma Ramaswami, Kausik K. Ray, Claudia Stefanutti, Shizuya Yamashita, Jing Pang, Gilbert R. Thompson, and Raul D. Santos. International atherosclerosis society guidance for implementing best practice in the care of familial hypercholesterolaemia. Nature Reviews Cardiology, 20:845-869, Jun 2023. URL: https://doi.org/10.1038/s41569-023-00892-0, doi:10.1038/s41569-023-00892-0. This article has 300 citations and is from a domain leading peer-reviewed journal.

11. (yip2023geneticspectrumand pages 5-6): Man-Kwan Yip, Elaine Kwan, Jenny Leung, Emmy Lau, and Wing-Tat Poon. Genetic spectrum and cascade screening of familial hypercholesterolemia in routine clinical setting in hong kong. Nov 2023. URL: https://doi.org/10.3390/genes14112071, doi:10.3390/genes14112071. This article has 6 citations.

12. (fularski2024unveilingfamilialhypercholesterolemia—review pages 10-12): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

13. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

14. (watts2023internationalatherosclerosissociety pages 1-2): Gerald F. Watts, Samuel S. Gidding, Robert A. Hegele, Frederick J. Raal, Amy C. Sturm, Laney K. Jones, Mitchell N. Sarkies, Khalid Al-Rasadi, Dirk J. Blom, Magdalena Daccord, Sarah D. de Ferranti, Emanuela Folco, Peter Libby, Pedro Mata, Hapizah M. Nawawi, Uma Ramaswami, Kausik K. Ray, Claudia Stefanutti, Shizuya Yamashita, Jing Pang, Gilbert R. Thompson, and Raul D. Santos. International atherosclerosis society guidance for implementing best practice in the care of familial hypercholesterolaemia. Nature Reviews Cardiology, 20:845-869, Jun 2023. URL: https://doi.org/10.1038/s41569-023-00892-0, doi:10.1038/s41569-023-00892-0. This article has 300 citations and is from a domain leading peer-reviewed journal.

15. (rochemolina2015inductionofsustained pages 1-2): Marta Roche-Molina, David Sanz-Rosa, Francisco M. Cruz, Jaime García-Prieto, Sergio López, Rocío Abia, Francisco J.G. Muriana, Valentín Fuster, Borja Ibáñez, and Juan A. Bernal. Induction of sustained hypercholesterolemia by single adeno-associated virus–mediated gene transfer of mutant hpcsk9. Arteriosclerosis, Thrombosis, and Vascular Biology, 35:50–59, Jan 2015. URL: https://doi.org/10.1161/atvbaha.114.303617, doi:10.1161/atvbaha.114.303617. This article has 234 citations and is from a domain leading peer-reviewed journal.

16. (rochemolina2015inductionofsustained pages 10-10): Marta Roche-Molina, David Sanz-Rosa, Francisco M. Cruz, Jaime García-Prieto, Sergio López, Rocío Abia, Francisco J.G. Muriana, Valentín Fuster, Borja Ibáñez, and Juan A. Bernal. Induction of sustained hypercholesterolemia by single adeno-associated virus–mediated gene transfer of mutant hpcsk9. Arteriosclerosis, Thrombosis, and Vascular Biology, 35:50–59, Jan 2015. URL: https://doi.org/10.1161/atvbaha.114.303617, doi:10.1161/atvbaha.114.303617. This article has 234 citations and is from a domain leading peer-reviewed journal.

17. (mcnutt2010characterizationofthea pages 115-119): MC McNutt. Characterization of the non-proteolytic mechanism and cellular site of action of pcsk9-mediated degradation of the low-density lipoprotein receptor. Unknown journal, 2010.

18. (otero2024functionalanalysisof pages 4-5): Javier Sanguino Otero, Carmen Rodríguez-Jiménez, Jose Mostaza Prieto, Carlos Rodríguez-Antolín, Ana Carazo Alvarez, Francisco Arrieta Blanco, and Sonia Rodríguez-Nóvoa. Functional analysis of 3′utr variants at the ldlr and pcsk9 genes in patients with familial hypercholesterolemia. Human Mutation, 2024:1-15, Feb 2024. URL: https://doi.org/10.1155/2024/9964734, doi:10.1155/2024/9964734. This article has 3 citations and is from a domain leading peer-reviewed journal.

19. (matiasperez2021pcsk9geneparticipates pages 2-4): D. MATÍAS-PÉREZ, A. PÉREZ-SANTIAGO, M. S. Sánchez Medina, JJ Alpuche Osorno, and I. GARCÍA-MONTALVO. Pcsk9 gene participates in the development of primary dyslipidemias. Balkan Journal of Medical Genetics : BJMG, 24:5-14, Jun 2021. URL: https://doi.org/10.2478/bjmg-2021-0009, doi:10.2478/bjmg-2021-0009. This article has 9 citations.

20. (weider2017inhibitionofthe pages 64-68): E Weider. Inhibition of the proprotein convertase subtilisin/kexin type 9 (pcsk9) for the treatment of familial hypercholesterolemia. Unknown journal, 2017.

21. (watts2023internationalatherosclerosissociety pages 9-10): Gerald F. Watts, Samuel S. Gidding, Robert A. Hegele, Frederick J. Raal, Amy C. Sturm, Laney K. Jones, Mitchell N. Sarkies, Khalid Al-Rasadi, Dirk J. Blom, Magdalena Daccord, Sarah D. de Ferranti, Emanuela Folco, Peter Libby, Pedro Mata, Hapizah M. Nawawi, Uma Ramaswami, Kausik K. Ray, Claudia Stefanutti, Shizuya Yamashita, Jing Pang, Gilbert R. Thompson, and Raul D. Santos. International atherosclerosis society guidance for implementing best practice in the care of familial hypercholesterolaemia. Nature Reviews Cardiology, 20:845-869, Jun 2023. URL: https://doi.org/10.1038/s41569-023-00892-0, doi:10.1038/s41569-023-00892-0. This article has 300 citations and is from a domain leading peer-reviewed journal.

22. (jeswani2024pcsk9inhibitorsthe pages 1-3): Bijay Mukesh Jeswani, Shubhangi Sharma, Sawai Singh Rathore, Abubakar Nazir, Rohit Bhatheja, and Kapil Kapoor. Pcsk9 inhibitors: the evolving future. Health Science Reports, Oct 2024. URL: https://doi.org/10.1002/hsr2.70174, doi:10.1002/hsr2.70174. This article has 44 citations and is from a peer-reviewed journal.

23. (weider2017inhibitionofthe pages 61-64): E Weider. Inhibition of the proprotein convertase subtilisin/kexin type 9 (pcsk9) for the treatment of familial hypercholesterolemia. Unknown journal, 2017.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Hypercholesterolemia_3-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

12 of 13 terms resolved to a current term; the rest could not be looked up either way.