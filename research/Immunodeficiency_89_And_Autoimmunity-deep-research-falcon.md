---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:08:59.237566'
end_time: '2026-09-02T17:18:41.092180'
duration_seconds: 581.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 89 and Autoimmunity
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
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
  path: Immunodeficiency_89_And_Autoimmunity-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 89 and Autoimmunity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 89 and Autoimmunity** covering all of the
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
- **Disease Name:** Immunodeficiency 89 and Autoimmunity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 89 and Autoimmunity** covering all of the
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


# Immunodeficiency 89 and Autoimmunity: Comprehensive Disease-Characteristics Report

## Executive summary and evidence limits

**Immunodeficiency 89 and autoimmunity** is an exceptionally rare, proposed autosomal-recessive inborn error of immunity associated with biallelic **CARD10** variants. Its disease definition rests principally on **two adult siblings from one consanguineous family**, both homozygous for **CARD10 NM-reference-dependent c.1258C>T, p.(Arg420Cys)**. Consequently, the phenotype, penetrance, prognosis, and causal mechanism remain provisional rather than independently replicated. Open Targets maps the disorder to **MONDO:0030484**, CARD10, and the disease-defining publication, PMID **32238915**. (OpenTargets Search: Immunodeficiency 89 with autoimmunity, yang2020mutantcard10in pages 1-2)

The primary article was received 15 March 2020, accepted 17 March, and published online **1 April 2020**: Yang et al., *Cellular & Molecular Immunology* 17:782–784, DOI [10.1038/s41423-020-0423-x](https://doi.org/10.1038/s41423-020-0423-x), PMID [32238915](https://pubmed.ncbi.nlm.nih.gov/32238915/). Its appropriately cautious conclusion was: **“we identified a CARD10 mutation as the possible cause of a novel form of autosomal recessive genetic disease characterized by primary immunodeficiency accompanied by autoimmune disease.”** (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)

| Domain | Established observation | Evidence type/strength | Knowledge-base annotation |
|---|---|---|---|
| Disease identity | Immunodeficiency 89 and autoimmunity is a Mendelian inborn error of immunity associated with **CARD10**. (OpenTargets Search: Immunodeficiency 89 with autoimmunity) | Curated disease–gene association; supported by one primary family report | **MONDO:0030484**; disease category: Mendelian immunodeficiency with immune dysregulation |
| Human evidence | Reported in **two affected siblings from one consanguineous family**; no independently replicated kindred was identified. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3) | Very limited human evidence; single-family case report | Case count: 2; family count: 1; inheritance proposed as autosomal recessive |
| Causal candidate variant | Both siblings were homozygous for **CARD10 c.1258C>T (p.Arg420Cys; R420C)** in exon 7 and the conserved coiled-coil domain. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3) | Segregation plus computational prediction; functional evidence incomplete | Gene: **CARD10**; variant: missense, germline, homozygous; pathogenic mechanism not conclusively classified as loss-of-function, gain-of-function, or hypomorphic |
| Core phenotype | Recurrent infections, asthma with low blood eosinophils, autoimmune anemia, Crohn disease/intestinal inflammation, gastrointestinal discomfort, and seasonal urticaria were reported across the siblings. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3) | Direct clinical observation; frequencies cannot be generalized beyond n=2 | Immunodeficiency, autoimmunity, allergy, and gastrointestinal inflammation; variable expressivity |
| Pulmonary disease | At age 42, the more severely affected brother had bronchiectasis with infection, lung abscess, and pulmonary bulla on high-resolution CT. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3) | Direct imaging evidence in one patient | Chronic respiratory infection and structural lung damage |
| Gastrointestinal disease | At age 42, the sister’s gastrointestinal biopsy showed local proliferative gastritis and colitis interpreted as early Crohn disease. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3) | Direct histopathology in one patient; disease interpretation by authors | Inflammatory bowel involvement; stomach and intestinal mucosa affected |
| Molecular consequence | Patient reconstitution studies showed **decreased CARD10 mRNA and protein expression** with R420C. (yang2020mutantcard10in pages 1-2) | Disease-specific functional observation, but assay scope and rescue evidence were limited | Reduced gene-product abundance; precise biochemical mechanism unresolved |
| Cellular and cytokine findings | The more affected sibling had reduced intermediate/nonclassical monocytes and monocyte-derived HLA-DR⁺CD11c⁺CD16⁺ cells; several immune-cell/cytokine measures were decreased, whereas autoantibodies and IL-8, GROα, MCP-1, MIP-1α, and SDF1α were increased. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3) | Direct comparative immunophenotyping within the family; no independent cohort | Monocyte/dendritic-cell abnormality, impaired immune output, and concurrent inflammatory/autoimmune signaling |
| Mechanism | CARD10 normally scaffolds the **CARD10–BCL10–MALT1 (CBM)** complex, connecting receptor signals to IKK/NF-κB and JNK/AP-1 signaling; attributing the patients’ phenotype specifically to reduced CBM/NF-κB activity remains **partly inferred**. (moud2024malt1substratecleavage pages 1-2, yang2020mutantcard10in pages 1-2, staal2024chimericandmutant pages 1-3) | Established pathway biology plus disease-specific expression findings; causal signaling defect not directly demonstrated for R420C | Upstream lesion: CARD10 variant; proposed downstream process: defective CBM signaling and immune/epithelial dysregulation |
| Course and modifiers | Disease was described as slowly progressive over approximately 20–30 years. Earlier, more severe disease in the brother was hypothesized to relate to unhealthy lifestyle and metal-dust exposure, but causality was not established. (yang2020mutantcard10in pages 2-3) | Longitudinal clinical description; gene–environment interaction is speculative | Chronic progressive course; variable expressivity; environmental modification unproven |
| Epidemiology and prognosis | No population prevalence, incidence, penetrance estimate, carrier frequency, survival rate, or life-expectancy data are available. (yang2020mutantcard10in pages 2-3) | Evidence absent | Ultra-rare designation is reasonable, but no numerical epidemiologic estimate should be assigned |
| Treatment and trials | The defining report supplied no disease-specific treatment outcomes, and no dedicated interventional trial or approved CARD10-targeted therapy was identified. (yang2020mutantcard10in pages 2-3) | Evidence absent | Management remains phenotype-directed and extrapolated from general immunodeficiency, infection, asthma, autoimmunity, and inflammatory-bowel-disease practice |


*Table: Compact evidence-grade summary of the genetic, clinical, molecular, and mechanistic findings supporting Immunodeficiency 89 and autoimmunity, with major evidence gaps explicitly identified.*

## 1. Disease information

### Definition

The disease is a slowly progressive combination of:

- susceptibility to recurrent infection;
- immune dysregulation/autoimmunity, including autoimmune anemia and intestinal inflammation;
- allergic disease, notably asthma and urticaria; and
- secondary pulmonary structural damage in the more severely affected individual.

This is best classified as a **Mendelian inborn error of immunity with immunodeficiency and immune dysregulation**, rather than as isolated antibody deficiency or classic severe combined immunodeficiency. (yang2020mutantcard10in pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0030484.
- **Causal-gene association:** CARD10, Ensembl ENSG00000100065; approved name *caspase recruitment domain family member 10*.
- **Primary-literature identifier:** PMID 32238915.
- **Synonyms:** “CARD10-related immunodeficiency and autoimmunity,” “CARD10 deficiency,” “CARMA3-associated immunodeficiency,” and “progressive immunodeficiency and autoimmunity due to CARD10 mutation.” The latter terms are descriptive and should not automatically be treated as independently curated disease entities.
- **OMIM/Orphanet/MeSH:** no disease-specific identifier was established from the retrieved evidence; the database entry should not infer one without direct verification.
- **ICD-10/ICD-11:** no dedicated code is documented. Generic coding would require separate codes for immunodeficiency, autoimmune disease, bronchiectasis, asthma, anemia, and Crohn disease.

The evidence is **aggregated disease-level literature derived from a single family study**, not an EHR-derived cohort or population registry. (OpenTargets Search: Immunodeficiency 89 with autoimmunity, yang2020mutantcard10in pages 1-2)

## 2. Etiology

### Causal factor

The proposed cause is a **germline homozygous missense CARD10 variant, c.1258C>T, p.(Arg420Cys), in exon 7**. Arg420 lies in a conserved coiled-coil region. Sanger sequencing confirmed the exome result and family segregation. Structural modeling predicted altered hydrogen bonding, alpha-helical hydrophobicity, and stability, while reconstitution experiments showed reduced CARD10 transcript and protein abundance. These findings support impaired function, but the allele has not been conclusively classified as complete loss-of-function, hypomorphic, gain-of-function, or dominant-negative. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)

### Risk and protective factors

- **Established genetic risk:** homozygosity for p.Arg420Cys in the reported family.
- **Consanguinity:** facilitated homozygosity and supports recessive inheritance.
- **Possible environmental modifiers:** the more severely affected brother had an “unhealthy lifestyle” and metal-dust exposure and developed disease earlier than his sister. This is an uncontrolled within-family observation, not proof of a gene–environment interaction. (yang2020mutantcard10in pages 2-3)
- **Sex, age, family history:** one male and one female were affected; this establishes neither a sex effect nor an age-specific risk estimate.
- **Protective factors:** none demonstrated. The sister’s healthier lifestyle was associated with milder disease, but cannot be interpreted as protective causally.
- **Modifier genes, susceptibility loci, protective alleles, toxins, diet, smoking, alcohol, or occupational-dose relationships:** no disease-specific data.

## 3. Phenotypes

Because only two people are reported, “2/2” and “1/2” below are **case-series observations**, not stable population frequencies.

| Phenotype | Type and observed characteristics | Suggested HPO annotation |
|---|---|---|
| Recurrent infections | Symptom/clinical diagnosis; 2/2; adult, slowly progressive; pathogen spectrum not adequately reported | Recurrent infections; increased susceptibility to infection |
| Asthma with low eosinophils | Respiratory/allergic manifestation; 2/2; severity variable | Asthma; decreased eosinophil count |
| Autoimmune anemia | Autoimmune hematologic manifestation reported across the affected siblings; sister specifically had unexplained microcytic hypochromic anemia | Autoimmune hemolytic anemia only if hemolysis is independently documented; otherwise anemia and microcytic anemia |
| Crohn disease/colitis | Gastrointestinal inflammatory manifestation; sister’s age-42 biopsy showed local proliferative gastritis and colitis interpreted as early Crohn disease | Inflammatory bowel disease; colitis; gastritis; abdominal discomfort |
| Seasonal urticaria | Allergic skin manifestation in the sister; episodic and comparatively mild | Urticaria |
| Bronchiectasis | CT-confirmed at age 42 in the brother, with active infection | Bronchiectasis |
| Lung abscess | CT-confirmed at age 42 in the brother | Lung abscess |
| Pulmonary bulla | CT-confirmed at age 42 in the brother | Pulmonary bulla/bullous lung disease |
| Reduced immune-cell subsets | Laboratory abnormality: reduced intermediate and nonclassical monocytes and monocyte-derived HLA-DR+CD11c+CD16+ cells in the brother relative to his sister | Abnormal monocyte count; abnormal dendritic-cell morphology/number, using the most specific validated HPO term available |
| Cytokine/chemokine dysregulation | IL-8, GROα, MCP-1, MIP-1α and SDF1α elevated; IL-6, TNFα, IFNα, IL-1α, TNFβ, IL-21, IL-22, IL-23 and IL-27 generally normal or reduced | Abnormal cytokine level; abnormal chemokine level |
| Autoantibodies | Increased in the more affected sibling | Autoantibody positivity |

The brother’s age-42 high-resolution CT showed “bronchiectasis with infection, lung abscess, and pulmonary bulla”; the sister’s age-42 gastrointestinal biopsy showed proliferative gastritis and colitis. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)

No validated EQ-5D, SF-36, PROMIS, behavioral, neurocognitive, or disease-specific quality-of-life measurements exist. Recurrent infection, chronic airway injury, asthma, anemia, and bowel inflammation would plausibly impair daily function, but the magnitude has not been measured.

## 4. Genetic and molecular information

- **Gene:** CARD10, also called **CARMA3**; protein: caspase recruitment domain-containing protein 10.
- **Variant:** c.1258C>T; p.(Arg420Cys), commonly abbreviated R420C.
- **Origin:** constitutional/germline, homozygous in both siblings.
- **Class:** missense variant in exon 7 and the coiled-coil domain.
- **Inheritance:** proposed autosomal recessive.
- **Functional evidence:** reduced CARD10 mRNA and protein in reconstitution studies; altered structure was computationally predicted, not structurally demonstrated. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)
- **ACMG/ClinVar status:** not established from the retrieved records. “Disease-causing” was the authors’ prediction; it should not be equated automatically with a current expert-panel pathogenic classification.
- **Population allele frequency:** not reported in the retrieved evidence.
- **Mechanistic class:** likely impaired abundance/function, but **unresolved**. A 2024 functional study stressed that CARD10’s high basal activity in overexpression systems complicates variant interpretation, and stated that human CARD10 mutations had been associated with several phenotypes without establishing whether they are activating or inactivating. (staal2024chimericandmutant pages 1-3, staal2024chimericandmutant pages 39-39)
- **Modifier genes/epigenetics:** none identified.
- **Chromosomal abnormalities:** none reported; this is a sequence-level disorder.
- **Somatic variation:** not implicated in this disease.

## 5. Environmental information

No environmental exposure is established as necessary or sufficient. Metal-dust exposure and unhealthy lifestyle coincided with earlier, more severe illness in the brother; the authors proposed environmental modification, but there was no exposure quantification, control group, toxicology, or mechanistic assay. (yang2020mutantcard10in pages 2-3)

Infectious organisms were not specified. Infections are therefore interpreted as **consequences/triggers acting on an inherited susceptibility**, not the primary etiology. No evidence addresses smoking, alcohol, diet, exercise, pollution, radiation, microbiome composition, or specific occupational chemicals.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Homozygous CARD10 p.Arg420Cys leads to reduced CARD10 mRNA and protein** in the reported reconstitution experiments; the exact reason for reduced abundance is unknown. (yang2020mutantcard10in pages 1-2)
2. **Reduced or altered CARD10 is inferred to impair assembly or tuning of the CARD10–BCL10–MALT1 signalosome** downstream of GPCRs, receptor tyrosine kinases, and epithelial TLR4-related signals; this was not directly demonstrated in patient cells. (moud2024malt1substratecleavage pages 1-2, yang2020mutantcard10in pages 1-2)
3. **Altered CBM signaling is inferred to dysregulate IKK/NF-κB and JNK/AP-1 signaling**, with possible effects on mTOR-linked immune activation, inflammatory transcription, cell survival, and differentiation. CARD10-specific pathway impairment by R420C remains unproven. (moud2024malt1substratecleavage pages 1-2, staal2024chimericandmutant pages 1-3)
4. **Immune/hematopoietic branch:** altered signaling and CARD10-dependent myeloid differentiation plausibly lead to reduced intermediate/nonclassical monocytes, abnormal monocyte-derived dendritic-cell populations, and reduced immune-cell/cytokine output, resulting in recurrent infection. Human-cell and mouse knockdown evidence supports a role for CARD10 in granulopoiesis, but direct causation in these patients is incomplete. (yang2020mutantcard10in pages 1-2, shyamsunder2018card10acebpe pages 1-7)
5. **Epithelial/allergic branch:** abnormal airway-epithelial CBM signaling leads, by inference from Card10-null mice, to reduced type-2 cytokines and eosinophils without necessarily eliminating airway hyperresponsiveness, producing asthma with unexpectedly low eosinophils. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)
6. **Gastrointestinal branch:** CARD10 dysfunction in gastrointestinal epithelial signaling is inferred to disturb mucosal inflammatory homeostasis, resulting in gastritis, colitis, and Crohn-like disease. (yang2020mutantcard10in pages 1-2)
7. **Immune-regulatory branch:** imbalanced immune activation leads to increased autoantibodies and selected chemokines while other cytokines remain normal or low, resulting in anemia, urticaria, and autoimmune/inflammatory manifestations despite immunodeficiency. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)
8. **Chronic recurrent pulmonary infection leads to structural tissue injury**, including bronchiectasis, abscess, and bullous change. This final clinical link is strongly plausible but was not longitudinally imaged. (yang2020mutantcard10in pages 1-2)

### Current mechanistic understanding

CARD10 is a scaffold with CARD, coiled-coil, PDZ, SH3, and guanylate-kinase-like regions. It nucleates BCL10–MALT1 filaments. MALT1 then serves as both a TRAF6-recruiting scaffold driving IKK/NF-κB and JNK/AP-1 and a paracaspase whose substrate cleavage regulates immune homeostasis. A 2024 authoritative review emphasized that complete MALT1 loss causes immunodeficiency whereas selective disruption of scaffolding or protease activity can provoke autoimmune inflammation—an important conceptual explanation for concurrent immunodeficiency and autoimmunity, although not direct proof for CARD10 R420C. (moud2024malt1substratecleavage pages 1-2)

**Suggested GO biological processes:** NF-κB signaling; IκB kinase/NF-κB signaling; JNK cascade; immune-response activating signaling; inflammatory response; cytokine production; chemokine production; granulocyte differentiation; monocyte differentiation; dendritic-cell differentiation; response to bacterium; epithelial-cell homeostasis.

**Suggested Cell Ontology terms:** classical/intermediate/nonclassical monocyte; conventional dendritic cell; CD4-positive T cell; airway epithelial cell; intestinal epithelial cell; keratinocyte; granulocyte/neutrophil/eosinophil.

**Subcellular annotations:** cytoplasm; plasma-membrane-associated signaling complex; CARD10–BCL10–MALT1 complex; BCL10 filament; IKK complex. No disease-specific metabolomic, lipidomic, spatial-transcriptomic, single-cell, proteomic, CRISPR-screen, or integrated multi-omic dataset exists.

## 7. Anatomical structures affected

- **Primary clinically involved systems:** immune/hematopoietic system, respiratory tract and lungs, gastrointestinal mucosa, and skin/allergic system.
- **Lung:** bronchi and pulmonary parenchyma; bronchiectasis, infection, abscess, and bulla.
- **Gastrointestinal tract:** gastric and intestinal mucosa; proliferative gastritis and colitis.
- **Blood/immune compartment:** circulating monocytes, monocyte-derived dendritic cells, cytokines, chemokines, autoantibodies, and erythroid phenotype/anemia.
- **Skin:** urticaria; no CARD10-specific ectodermal dysplasia was reported.

Suggested UBERON mappings include lung, bronchus, airway epithelium, stomach, gastric mucosa, intestine, intestinal mucosa, blood, bone marrow, and skin. Suggested GO cellular components include cytosol, plasma membrane, CARD10–BCL10–MALT1 complex, and IKK complex. No lateralization is relevant. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)

## 8. Temporal development

The precise age at first symptom was not supplied. The brother developed immunodeficiency and autoimmunity substantially earlier than his sister. Both were evaluated at age 42 for key imaging/biopsy findings. The authors characterized CARD10-related disease as slowly progressive over approximately **20–30 years**, with variable severity and intermittent allergic/autoimmune manifestations superimposed on chronic infection susceptibility. (yang2020mutantcard10in pages 2-3)

No formal stages, remission rates, treatment-induced remission data, critical intervention window, or pediatric natural-history observations are available. The observed bronchiectasis argues for early recognition and infection control before irreversible airway damage, but this is clinical extrapolation rather than a CARD10-specific outcome study.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive, supported by consanguinity and homozygosity in two siblings.
- **Penetrance:** unknown. Both known homozygous siblings were affected, but n=2 cannot establish complete penetrance.
- **Expressivity:** clearly variable within the family.
- **Sex ratio:** one male and one female; no sex bias can be estimated.
- **Prevalence/incidence:** unknown. Only two affected individuals from one family formed the disease-defining report.
- **Carrier frequency/founder effect/geographic distribution:** unknown.
- **Consanguinity:** present in the reported family.
- **Anticipation:** not reported and biologically unsupported.
- **Germline mosaicism:** not reported.
- **Ethnicity and population-specific enrichment:** insufficiently documented for inference.

The disorder should be labeled **ultra-rare with no numerical prevalence estimate**, rather than assigning a cases-per-100,000 value. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)

## 10. Diagnostics

### Proposed diagnostic approach

There are no standardized criteria. A reasonable evidence-aligned workflow is:

1. Recognize the combination of recurrent infection plus autoimmune/inflammatory or allergic disease, particularly asthma with low eosinophils, Crohn-like inflammation, anemia, urticaria, or unexplained bronchiectasis.
2. Perform complete blood count with differential, blood film and anemia/hemolysis studies; immunoglobulins; vaccine-antibody responses; lymphocyte subsets; monocyte subsets; dendritic-cell phenotyping; autoantibodies; inflammatory markers; and microbiologic evaluation during infection.
3. Assess complications using high-resolution chest CT where bronchiectasis is suspected and endoscopy with biopsy for persistent gastrointestinal symptoms.
4. Use an inborn-error-of-immunity gene panel containing **CARD10**, or preferably trio/family WES/WGS where the phenotype is atypical. Confirm candidate variants by Sanger sequencing and segregation.
5. Interpret CARD10 variants cautiously with population frequency, conservation, domain location, RNA/protein expression, and ideally patient-cell CBM/NF-κB functional assays. Exome plus Sanger segregation was the successful discovery method in the reported family. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)

CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not first-line for this single-gene phenotype unless another diagnosis is suspected. RNA sequencing could assess transcript abundance or splicing, but is not validated diagnostically. No biomarker has established sensitivity or specificity.

### Differential diagnosis

Important differentials include other CBM/NF-κB pathway disorders—CARD11, BCL10, MALT1, CARD9 and CARD14 defects—as well as common variable immunodeficiency, activated PI3K-delta syndrome, CTLA4/LRBA deficiency, STAT3 gain-of-function, NFKB1/NFKB2 deficiency, chronic granulomatous disease, DOCK8 deficiency, autoimmune lymphoproliferative syndromes, monogenic inflammatory bowel disease, cystic fibrosis, primary ciliary dyskinesia, and secondary immunodeficiency. CARD10’s broad nonhematopoietic expression and the combined airway, bowel, myeloid, allergic, and autoimmune phenotype may be distinguishing, but no validated discriminant criteria exist. Recent work also cautions that CARD10 overexpression assays have high basal NF-κB activity and may misclassify variants. (staal2024chimericandmutant pages 1-3, staal2023chimericandmutant pages 11-13)

No newborn, population, or carrier-screening program exists. Once a familial variant is securely classified, targeted cascade, prenatal, or preimplantation testing can be considered with genetic counseling.

## 11. Outcome and prognosis

There are no survival curves, mortality rates, life-expectancy estimates, or validated prognostic biomarkers. The reported course was chronic and slowly progressive over decades. Documented morbidity included recurrent infection, chronic airway damage, lung abscess, asthma, bowel inflammation, anemia, and allergic disease. (yang2020mutantcard10in pages 2-3)

Potential adverse prognostic factors—based on the two-person report—include earlier onset, greater immune-cell/cytokine impairment, repeated respiratory infection, bronchiectasis, and possibly harmful inhalational exposure. These are hypotheses, not validated predictors. Recovery potential and reversibility are unknown; bronchiectasis is generally irreversible, while infection, asthma, anemia, and bowel inflammation may be controllable with phenotype-directed therapy.

## 12. Treatment

No CARD10-specific treatment, response rate, adverse-event series, pharmacogenomic recommendation, gene therapy, RNA therapy, or hematopoietic stem-cell transplantation outcome has been reported. No dedicated interventional trial was identified. The primary report did not provide treatment outcomes. (yang2020mutantcard10in pages 2-3)

Management should therefore be individualized in an expert immunology center and may include, by extrapolation:

- prompt culture-guided antimicrobial treatment and consideration of prophylaxis when infection burden warrants it;
- immunoglobulin replacement only if quantitative or functional antibody deficiency is demonstrated;
- airway clearance, vaccination planning, pulmonary surveillance, and standard bronchiectasis care;
- guideline-based asthma treatment, recognizing that eosinophil-low disease may not respond like eosinophilic asthma;
- hematology-directed evaluation and treatment of autoimmune anemia;
- gastroenterology-directed treatment of Crohn-like inflammation, balancing immunosuppression against infection risk;
- antihistamines or other standard therapy for urticaria;
- avoidance of unnecessary broad immunosuppression and multidisciplinary monitoring.

Suggested NCIt intervention annotations include antimicrobial therapy, antimicrobial prophylaxis, immunoglobulin replacement therapy, corticosteroid therapy, bronchodilator therapy, airway-clearance therapy, immunosuppressive therapy, biologic therapy, hematopoietic stem-cell transplantation, genetic counseling, and supportive care. These are ontology mappings, **not evidence of CARD10-specific efficacy**.

Direct inhibition of CARD10, MALT1, or NF-κB is not rationally established for a variant already associated with reduced CARD10 abundance. Although MALT1 inhibitors are being developed for malignancy and inflammatory indications, pathway inhibition could worsen immunodeficiency. The 2024 MALT1 review underscores that balanced—not simply reduced—CBM signaling is required for immune homeostasis. (moud2024malt1substratecleavage pages 1-2)

## 13. Prevention

- **Primary prevention:** no method prevents the phenotype in a person with a pathogenic biallelic genotype. Genetic counseling, carrier testing after familial-variant confirmation, prenatal diagnosis, and preimplantation genetic testing can reduce recurrence risk.
- **Secondary prevention:** cascade testing of relatives, early immunologic evaluation, infection surveillance, and early chest assessment may identify disease before advanced bronchiectasis.
- **Tertiary prevention:** vaccination after immunology review, antimicrobial prophylaxis where indicated, airway clearance, avoidance of tobacco and harmful dust exposure, and prompt treatment of infection may reduce complications. Avoid live vaccines when clinically significant cellular immunodeficiency has not been excluded.
- **Behavioral/environmental:** reducing metal-dust and respiratory irritant exposure is prudent, but CARD10-specific benefit has not been demonstrated.

No public-health screening program or disease-specific prophylaxis guideline exists.

## 14. Other species and natural disease

No naturally occurring veterinary CARD10 disease equivalent was identified, and there is no evidence of zoonotic transmission. The genetic and signaling mechanism is conserved across vertebrates, but “natural disease” should be recorded as **not established**.

Relevant experimental taxa include human (*Homo sapiens*, NCBI Taxon 9606) and laboratory mouse (*Mus musculus*, NCBI Taxon 10090). Ortholog-specific NCBI Gene identifiers should be imported directly from NCBI rather than inferred from this literature set.

## 15. Model organisms and experimental systems

### Mouse models

Card10-null mice provide partial mechanistic support. In an asthma model, airway eosinophils and type-2 cytokines were reduced, but airway hyperresponsiveness was not correspondingly reduced. Card10-deficient airway epithelial cells had impaired dendritic-cell maturation/antigen-presentation effects. These observations resemble the patients’ asthma with low eosinophils, but do not reproduce the complete human syndrome. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3)

More recent CARD-CC work reports neurodevelopmental phenotypes in Card10-deficient mice, shared with Bcl10 deficiency, yet comparable neurological abnormalities were not reported in the two human cases. This highlights incomplete cross-species phenotypic concordance. (staal2024chimericandmutant pages 1-3)

### Cellular models

- CARD10 silencing in a human cell line and murine primary progenitors impaired granulocytic differentiation and altered genes involved in myeloid development and function. This supports a possible basis for the human myeloid abnormalities. The primary study’s abstract states: **“Silencing Card10 in a human cell line and in murine primary cells impaired granulopoiesis.”** Shyamsunder et al., published online 17 May 2018, DOI [10.3324/haematol.2018.190280](https://doi.org/10.3324/haematol.2018.190280). (shyamsunder2018card10acebpe pages 1-7)
- HEK293T NF-κB reporter systems and engineered CARD9–CARD10 chimeras have been used to test CARD10 autoinhibition and variants. Their limitation is high spontaneous activity from overexpressed native CARD10; effects at endogenous expression remain uncertain. Staal et al., 2024, DOI [10.1111/febs.17035](https://doi.org/10.1111/febs.17035). (staal2024chimericandmutant pages 1-3, staal2023chimericandmutant pages 11-13, staal2024chimericandmutant pages 39-39)
- No patient-derived iPSC, organoid, knock-in p.Arg420Cys mouse, zebrafish, Drosophila, or CRISPR-corrected rescue model was identified.

## Recent developments and expert assessment, 2023–2024

The most important recent development is not discovery of additional patients but improved understanding of CARD-CC/CBM signaling and its experimental limitations. The 2024 FEBS study established chimeric systems for testing CARD10 autoinhibition and natural variants, while emphasizing that disease-associated CARD10 variants often remain mechanistically unresolved. It did **not** independently validate p.Arg420Cys. (staal2024chimericandmutant pages 1-3, staal2024chimericandmutant pages 39-39)

The 28 May 2024 MALT1 review described CBM signalosomes as receptor-to-NF-κB/JNK signaling hubs and emphasized that both inadequate and qualitatively imbalanced MALT1 activity can produce immune pathology. Its abstract states that **“balanced MALT1-TRAF6 recruitment and MALT1 substrate cleavage are critical to maintain immune homeostasis and to promote optimal immune activation.”** DOI [10.3389/fimmu.2024.1412347](https://doi.org/10.3389/fimmu.2024.1412347). (moud2024malt1substratecleavage pages 1-2)

A 17 January 2023 review of NF-κB-associated inborn errors emphasized that NF-κB acts in both immune and epithelial compartments and regulates epithelial differentiation, survival, and inflammatory amplification. This provides authoritative context for a CARD10 disorder involving immunity, airway disease, bowel inflammation, and skin allergy, but is not independent case evidence. DOI [10.3389/fped.2022.1098426](https://doi.org/10.3389/fped.2022.1098426). (shen2023skinmanifestationsof pages 1-2)

### Overall evidence-grade conclusion

The association of homozygous CARD10 p.Arg420Cys with immunodeficiency and autoimmunity is **biologically plausible and supported by segregation, reduced CARD10 expression, patient immunophenotyping, and relevant model evidence**, but remains based on one family. The disease should be represented in a knowledge base with high confidence for the reported phenotype and genotype, but only **limited-to-moderate confidence for definitive gene–disease validity and molecular mechanism** until unrelated cases, population-frequency analysis, endogenous signaling assays, and variant-specific rescue or knock-in studies become available. (yang2020mutantcard10in pages 1-2, yang2020mutantcard10in pages 2-3, staal2024chimericandmutant pages 1-3)

References

1. (OpenTargets Search: Immunodeficiency 89 with autoimmunity): Open Targets Query (Immunodeficiency 89 with autoimmunity, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (yang2020mutantcard10in pages 1-2): Dan-hui Yang, Ting Guo, Zhuang-zhuang Yuan, Cheng Lei, Shui-zi Ding, Yi-feng Yang, Zhi-ping Tan, and Hong Luo. Mutant card10 in a family with progressive immunodeficiency and autoimmunity. Cellular & Molecular Immunology, 17:782-784, Apr 2020. URL: https://doi.org/10.1038/s41423-020-0423-x, doi:10.1038/s41423-020-0423-x. This article has 9 citations and is from a peer-reviewed journal.

3. (yang2020mutantcard10in pages 2-3): Dan-hui Yang, Ting Guo, Zhuang-zhuang Yuan, Cheng Lei, Shui-zi Ding, Yi-feng Yang, Zhi-ping Tan, and Hong Luo. Mutant card10 in a family with progressive immunodeficiency and autoimmunity. Cellular & Molecular Immunology, 17:782-784, Apr 2020. URL: https://doi.org/10.1038/s41423-020-0423-x, doi:10.1038/s41423-020-0423-x. This article has 9 citations and is from a peer-reviewed journal.

4. (moud2024malt1substratecleavage pages 1-2): Bahareh Nemati Moud, Franziska Ober, Thomas J. O’Neill, and Daniel Krappmann. Malt1 substrate cleavage: what is it good for? Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1412347, doi:10.3389/fimmu.2024.1412347. This article has 21 citations and is from a peer-reviewed journal.

5. (staal2024chimericandmutant pages 1-3): Jens Staal, Yasmine Driege, Femke Van Gaever, Jill Steels, and Rudi Beyaert. Chimeric and mutant <scp>card9</scp> constructs enable analyses of conserved and diverged autoinhibition mechanisms in the <scp>card‐cc</scp> protein family. Dec 2024. URL: https://doi.org/10.1111/febs.17035, doi:10.1111/febs.17035. This article has 4 citations.

6. (staal2024chimericandmutant pages 39-39): Jens Staal, Yasmine Driege, Femke Van Gaever, Jill Steels, and Rudi Beyaert. Chimeric and mutant <scp>card9</scp> constructs enable analyses of conserved and diverged autoinhibition mechanisms in the <scp>card‐cc</scp> protein family. Dec 2024. URL: https://doi.org/10.1111/febs.17035, doi:10.1111/febs.17035. This article has 4 citations.

7. (shyamsunder2018card10acebpe pages 1-7): Pavithra Shyamsunder, Haresh Sankar, Anand Mayakonda, Lin Han, Hazimah Binte Mohd Nordin, Teoh Weoi Woon, Mahalakshmi Shanmugasundaram, Pushkar Dakle, Vikas Madan, and H. Phillip Koeffler. Card10, a cebpe target involved in granulocytic differentiation. Haematologica, 103:1269-1277, May 2018. URL: https://doi.org/10.3324/haematol.2018.190280, doi:10.3324/haematol.2018.190280. This article has 13 citations.

8. (staal2023chimericandmutant pages 11-13): Jens Staal, Yasmine Driege, Femke Van Gaever, Jill Steels, and Rudi Beyaert. Chimeric and mutant card9 constructs enable analyses of conserved and diverged autoinhibition mechanisms in the card-cc protein family. Mar 2023. URL: https://doi.org/10.1101/2023.03.06.531260, doi:10.1101/2023.03.06.531260. This article has 0 citations.

9. (shen2023skinmanifestationsof pages 1-2): Yitong Shen, Anne P. R. Boulton, Robert L. Yellon, and Matthew C. Cook. Skin manifestations of inborn errors of nf-κb. Frontiers in Pediatrics, Jan 2023. URL: https://doi.org/10.3389/fped.2022.1098426, doi:10.3389/fped.2022.1098426. This article has 24 citations.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_89_And_Autoimmunity-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.