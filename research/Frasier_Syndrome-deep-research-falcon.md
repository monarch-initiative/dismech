---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T14:28:08.057501'
end_time: '2026-09-03T14:36:41.166815'
duration_seconds: 513.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Frasier Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 3
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  - Taxon
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Frasier_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Frasier Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frasier Syndrome** covering all of the
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
- **Disease Name:** Frasier Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frasier Syndrome** covering all of the
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


# Frasier Syndrome: Comprehensive Disease-Characteristics Report

## Executive summary

Frasier syndrome (FS) is an ultra-rare, autosomal-dominant **WT1 disorder**, usually caused by heterozygous germline variants affecting the intron-9 alternative splice donor. Its defining clinical combination is progressive proteinuric glomerulopathy—usually steroid-resistant nephrotic syndrome (SRNS) with focal segmental glomerulosclerosis (FSGS)—and gonadal dysgenesis, especially in 46,XY individuals, with a clinically important risk of gonadoblastoma. Contemporary experts increasingly regard Frasier and Denys–Drash syndromes as overlapping ends of a continuous WT1-disorder spectrum rather than completely discrete entities. (shao2023frasiersyndromea pages 1-2, sambharia2022monogenicfocalsegmental pages 11-12, peer2024clinicalcharacterizationof pages 7-9)

The most important recent development is recognition of a wider and temporally variable WT1 phenotype. A 2024 Dutch national cohort found that all four individuals with intron-9 splice variants developed chronic kidney disease (CKD), with median onset at 15 years, while other WT1 variant classes could cause kidney failure as late as adulthood. This supports lifelong renal surveillance and full-gene testing rather than reliance on classical syndrome labels or hotspot-only sequencing. (peer2024clinicalcharacterizationof pages 1-2, peer2024clinicalcharacterizationof pages 2-4, peer2024clinicalcharacterizationof pages 7-9)

The following table provides a knowledge-base-oriented synopsis; broader WT1-spectrum statistics are identified as such rather than presented as Frasier-specific rates.

| Domain | High-confidence finding | Quantitative/current evidence | Suggested ontology terms |
|---|---|---|---|
| Disease identity and identifiers | Frasier syndrome is a rare Mendelian **WT1 disorder** characterized principally by progressive glomerulopathy, 46,XY gonadal dysgenesis/DSD, and predisposition to gonadoblastoma. Classical syndrome labels increasingly overlap within a broader WT1-disorder spectrum. Identifiers: **OMIM 136680**; **ORPHA:347**; MONDO identifier requires database validation. (shao2023frasiersyndromea pages 1-2, peer2024clinicalcharacterizationof pages 7-9) | No population-based prevalence or incidence estimate is established. | Frasier syndrome; WT1 disorder; MONDO ID **verify**; OMIM:136680; ORPHA:347 |
| Causal gene and inheritance | Heterozygous germline variants in **WT1** at 11p13 cause disease; classical Frasier syndrome is usually associated with intron 9 donor splice-region variants. Autosomal-dominant transmission is possible, although many cases are apparently de novo. (shao2023frasiersyndromea pages 2-4) | A 2023 patient had de novo **NM_024426.6:c.1447+4C>T**, absent in both parents and a sibling. (shao2023frasiersyndromea pages 2-4) | WT1; HGNC gene term **validate**; autosomal dominant inheritance; de novo variant |
| Molecular defect | Classical intron 9 variants disrupt alternative splicing of WT1 transcripts encoding isoforms with or without the Lys-Thr-Ser insertion. They reverse the normal renal **+KTS:−KTS ratio from approximately 2:1 toward 1:2**, impairing WT1-dependent podocyte maintenance and gonadal development. (paul2021suspicionoffrasiers pages 4-7, peer2024clinicalcharacterizationof pages 2-4) | Four of seven splice-site cases in the 2024 Dutch WT1 cohort involved intron 9; all four developed CKD, with median CKD onset at 15 years. (peer2024clinicalcharacterizationof pages 2-4) | RNA splicing; regulation of transcription; GO terms **validate**; WT1 +KTS and −KTS isoforms |
| Pathogenic variants | Recurrent classical substitutions occur at intron 9 donor-site positions, especially **c.1447+4C>T** and variants at +4/+5. These are germline splice-altering variants; pathogenicity requires transcript-aware ClinVar/ACMG review. (shao2023frasiersyndromea pages 1-2, shao2023frasiersyndromea pages 2-4) | Population allele frequencies were not reported in the reviewed studies and are expected to be extremely low; confirm each allele in gnomAD/ClinVar. | Sequence variant; splice donor variant; ClinVar classification **variant-specific validation required** |
| Renal phenotype and onset | Persistent proteinuria typically begins in childhood and progresses to steroid-resistant nephrotic syndrome, FSGS, CKD, and ESKD. Progression is generally slower and later than in classic Denys–Drash syndrome. (shao2023frasiersyndromea pages 1-2, sambharia2022monogenicfocalsegmental pages 11-12) | Historical reports place onset of proteinuria/edema/hypertension around ages 2–10 and mean diagnosis at 16.3 ± 2.3 years. In the broader 2024 WT1 cohort, CKD occurred in 25/43 (58%) and kidney failure in 22/43 (51%); all ten patients with confirmed FSGS developed kidney failure. (paul2021suspicionoffrasiers pages 4-7, peer2024clinicalcharacterizationof pages 2-4, peer2024clinicalcharacterizationof pages 4-6) | Proteinuria; steroid-resistant nephrotic syndrome; focal segmental glomerulosclerosis; chronic kidney disease; end-stage kidney disease; corresponding HPO IDs **validate** |
| Renal pathology and target cell | The characteristic lesion is usually FSGS, reflecting progressive dysfunction and loss of glomerular podocytes; diffuse mesangial sclerosis can occur but is more characteristic of severe early-onset WT1 disease. (sambharia2022monogenicfocalsegmental pages 11-12, peer2024clinicalcharacterizationof pages 6-7) | In the 2024 cohort, FSGS was confirmed in 11 patients at median age 4 years; DMS occurred in three, all in the first week of life. These figures describe the broader WT1 spectrum, not Frasier syndrome alone. (peer2024clinicalcharacterizationof pages 2-4) | Podocyte (CL term **validate**); glomerulus; FSGS; DMS; UBERON kidney/glomerulus terms **validate** |
| 46,XY DSD and puberty | Many affected 46,XY individuals have streak/dysgenetic gonads and female external genitalia; others have ambiguous or male genitalia with cryptorchidism or hypospadias. Gonadal failure may cause absent puberty, primary amenorrhea, and hypergonadotropic hypogonadism. (shao2023frasiersyndromea pages 2-4, paul2021suspicionoffrasiers pages 4-7) | A 2023 case first presented at age 15 with delayed puberty and carried c.1447+4C>T. In a broader 333-case WT1 review, 183 (55%) were 46,XY; 219 (66%) had a female phenotype, including 69/219 (32%) with XY sex reversal. (shao2023frasiersyndromea pages 1-2, drayer2022spectrumofclinical pages 6-8) | 46,XY DSD; complete/partial gonadal dysgenesis; female external genitalia in 46,XY; delayed puberty; primary amenorrhea; hypergonadotropic hypogonadism; HPO IDs **validate** |
| Gonadal tumors | Dysgenetic gonads containing Y-chromosome material confer substantial risk of gonadoblastoma, sometimes with dysgerminoma or other germ-cell/sex-cord tumors; risk begins in childhood and extends through adolescence/adulthood. (sambharia2022monogenicfocalsegmental pages 11-12, peer2024clinicalcharacterizationof pages 4-6) | Three gonadoblastomas occurred among nine patients with sex reversal in a 2014 WT1 cohort. The 2024 cohort reported four gonadoblastomas, including one intron 9 case at age 23, plus intratubular germ-cell neoplasia in another intron 9 case at age 15. (lipska2014genotypephenotypeassociationsin pages 8-9, peer2024clinicalcharacterizationof pages 4-6) | Gonadoblastoma; dysgerminoma; gonadal dysgenesis; streak gonad; NCIT tumor terms **validate** |
| Other tumors | Wilms tumor is part of the wider WT1-disorder spectrum but appears less characteristic of classical intron 9 Frasier syndrome than of truncating/deletion or DNA-binding-domain WT1 disorders. (peer2024clinicalcharacterizationof pages 2-4) | In the 2024 cohort, Wilms tumor occurred in 26/43 overall, but in **0/4 intron 9 splice-variant cases**; ascertainment was phenotype-biased. (peer2024clinicalcharacterizationof pages 2-4) | Wilms tumor; nephroblastoma; NCIT term **validate** |
| Diagnosis | Diagnosis integrates childhood proteinuria/SRNS or FSGS, genital or pubertal findings, sex-chromosome analysis, and molecular confirmation of a pathogenic germline WT1 variant. Phenotypic females with unexplained SRNS, CKD, delayed puberty, or primary amenorrhea should undergo karyotyping and WT1 testing. (shao2023frasiersyndromea pages 1-2, drayer2022spectrumofclinical pages 10-11) | Full-gene sequencing with deletion/duplication analysis is preferable to hotspot-only testing because WT1 phenotypes and causal variants extend beyond exons 8–9. The 2024 cohort identified 33 unique variants among 43 patients. (peer2024clinicalcharacterizationof pages 2-4, peer2024clinicalcharacterizationof pages 7-9) | Genetic test; chromosome analysis; kidney biopsy; serum creatinine/eGFR; urine protein; diagnostic NCIT/LOINC terms **validate** |
| Treatment and surveillance | No approved molecularly targeted therapy exists. Management includes RAAS blockade for proteinuria/hypertension, avoidance of prolonged ineffective immunosuppression in confirmed genetic disease, CKD care, dialysis/transplantation for ESKD, prophylactic removal of dysgenetic gonads after multidisciplinary counseling, and sex-steroid replacement when clinically indicated. (sambharia2022monogenicfocalsegmental pages 11-12, drayer2022spectrumofclinical pages 10-11) | In a nine-child WT1 series, all received transplants at median age 5 years; over median nine-year follow-up, two grafts were lost and no post-transplant malignancy occurred. A 2023 Frasier case underwent bilateral gonadectomy and later required hemodialysis while awaiting transplantation. (shao2023frasiersyndromea pages 2-4, drayer2022spectrumofclinical pages 1-2) | ACE inhibitor; angiotensin-receptor blocker; gonadectomy; hormone-replacement therapy; hemodialysis; kidney transplantation; NCIT intervention IDs **validate** |
| Prognosis | Untreated nephropathy is chronic and progressive, usually culminating in ESKD; gonadal malignancy is preventable through timely recognition and management. Genetic FSGS has negligible recurrence risk after kidney transplantation compared with non-genetic SRNS. (shao2023frasiersyndromea pages 1-2, drayer2022spectrumofclinical pages 1-2) | Frasier-specific survival rates and life expectancy are unavailable. Broader WT1 transplant data show useful long-term graft survival, while renal timing varies substantially by variant class. (drayer2022spectrumofclinical pages 1-2, peer2024clinicalcharacterizationof pages 1-2) | Progressive disease; kidney failure; transplant outcome; quality-of-life terms **validate** |
| Epidemiology and population | The syndrome is ultra-rare, reported across multiple ancestries and geographic regions; no established sex ratio is meaningful because chromosomal sex, gonadal sex, phenotype, and gender may differ. No founder effect, carrier frequency, or population-specific enrichment is established. | WT1 variants accounted for approximately 6% of SRNS in one intensively characterized cohort, but this is not Frasier-syndrome prevalence. (lipska2014genotypephenotypeassociationsin pages 8-9) | Rare genetic disease; Mendelian disease; prevalence term **not quantified** |
| Models | Reduced +KTS expression in heterozygous mice produces glomerulosclerosis; homozygous loss of +KTS causes complete XY sex reversal, supporting causal renal and gonadal branches of the human mechanism. (sambharia2022monogenicfocalsegmental pages 11-12) | Models reproduce core biology but do not capture the full variability, tumor risk, psychosocial outcomes, or long-term human disease course. | Mus musculus (NCBI Taxon:10090); podocyte; gonadal somatic cell; knockout/knock-in model terms **validate** |
| Major evidence gaps | Frasier-specific prospective natural-history, penetrance, prevalence, quality-of-life, fertility, long-term tumor-risk, and treatment-response data are lacking. No validated protective environmental factors, gene–environment interactions, modifiers, disease-specific epigenomic signature, metabolomic/proteomic biomarker, gene therapy, or interventional trial was identified. | Available evidence is dominated by case reports, retrospective WT1-spectrum cohorts, and small systematic compilations; the completed WT1 registry NCT01252901 enrolled 52 participants but was observational. | Natural-history study; patient registry; molecular biomarker; clinical trial terms **validate** |


*Table: Compact synthesis of high-confidence Frasier syndrome genetics, clinical features, mechanisms, management, quantitative evidence, ontology candidates, and major knowledge gaps. Broader WT1-spectrum statistics are explicitly distinguished from Frasier-specific observations.*

## 1. Disease information

### Definition and classification

FS is a Mendelian developmental and renal disorder caused by pathogenic germline **WT1** variants. The classical phenotype comprises childhood-onset proteinuria progressing to CKD/ESKD, FSGS, 46,XY gonadal dysgenesis with female or atypical external genitalia, gonadal failure, and gonadoblastoma susceptibility. Less typical presentations occur in phenotypic males and 46,XX individuals. (shao2023frasiersyndromea pages 1-2, paul2021suspicionoffrasiers pages 4-7, kitsioutzeli2012sertolicelltumor pages 7-7)

Suggested identifiers are **OMIM 136680** and **ORPHA:347**. A current MONDO identifier should be verified directly against the production MONDO release before ingestion; the retrieved primary literature did not state one. No dedicated ICD-10-CM code exists: coding ordinarily combines congenital gonadal-development, nephrotic/CKD, and genetic-condition codes. ICD-11 and MeSH similarly tend to represent the component phenotypes or broader WT1-related disorder rather than a uniquely granular FS entity.

Synonyms include **Frasier syndrome**, **Frasier’s syndrome**, **WT1-related Frasier syndrome**, and historically “46,XY male pseudohermaphroditism with progressive glomerulopathy.” The latter terminology is obsolete and potentially stigmatizing; **46,XY difference/disorder of sex development (DSD)** or **46,XY gonadal dysgenesis** is preferred.

Evidence is predominantly aggregated disease-level literature, retrospective WT1 cohorts, systematic case compilations, and individual case reports. It is not primarily derived from routine EHR population studies.

A useful exact abstract statement from Shao et al. (published 17 March 2023; DOI: https://doi.org/10.3390/children10030577) is: **“Frasier syndrome (FS) is a rare inherited disorder characterized by gonadal dysgenesis and progressive nephropathy, resulting from mutations in the intron 9 splice donor site of the Wilms tumor 1 (WT1) gene.”** (shao2023frasiersyndromea pages 1-2)

## 2. Etiology

### Causal and genetic risk factors

The causal lesion is a heterozygous germline WT1 variant, classically at nucleotides +4 or +5 of intron 9. A recurrent example is **NM_024426.6:c.1447+4C>T**, historically IVS9+4C>T. A 2023 patient carried this variant; neither parent nor a sibling carried it, supporting a de novo event. The disorder is nevertheless autosomal dominant, so an affected individual has a theoretical 50% transmission probability, subject to reproductive capacity and variant-specific expression. (shao2023frasiersyndromea pages 2-4)

Variants outside the canonical intron-9 donor can produce overlapping phenotypes. Thus, a patient with WT1-associated FSGS and DSD should not be excluded merely because the genotype or presentation is nonclassical. The 2014 cohort found that 28% of mutation-positive patients initially appeared to have isolated sporadic SRNS and another 28% had extrarenal findings recognized only after genotype-directed examination. (lipska2014genotypephenotypeassociationsin pages 8-9)

Pathogenic FS variants are expected to be absent or exceptionally rare in population databases, but allele-level gnomAD frequency and ClinVar classification should be checked against the exact transcript and genome build. No reliable carrier-frequency, founder-effect, anticipation, or population-specific enrichment estimate is available.

### Environmental, infectious, and protective factors

No toxin, infection, lifestyle, diet, occupation, or prenatal exposure has been shown to cause FS. Environmental factors may affect general CKD progression but are not established FS etiologies. No validated protective allele, modifier gene, protective lifestyle exposure, or disease-specific gene–environment interaction has been demonstrated. Likewise, no reproducible FS-specific epigenetic signature is established. These are evidence gaps, not evidence that modifiers cannot exist.

## 3. Phenotypes

### Renal manifestations

The usual earliest recognized renal abnormality is persistent proteinuria in childhood, sometimes accompanied by edema and hypertension. Historical compilations place onset commonly between ages 2 and 10, followed by steroid-resistant nephrotic syndrome, declining glomerular filtration, CKD, and ESKD during adolescence or early adulthood. Severity and timing are variable. (paul2021suspicionoffrasiers pages 4-7)

Renal biopsy usually shows **FSGS**; diffuse mesangial sclerosis is possible but is more typical of early, severe WT1 disease classically labeled Denys–Drash. In the broader 2024 WT1 cohort, FSGS was confirmed in 11 patients at a median age of four years, and all ten evaluable FSGS patients progressed to kidney failure. Those figures are not FS-specific. (peer2024clinicalcharacterizationof pages 2-4, peer2024clinicalcharacterizationof pages 4-6, peer2024clinicalcharacterizationof pages 6-7)

Suggested HPO concepts include proteinuria, nephrotic syndrome, steroid-resistant nephrotic syndrome, FSGS, hypertension, renal insufficiency, CKD, and ESKD. Exact HPO identifiers should be resolved against the current HPO release.

### Gonadal, genital, and endocrine manifestations

The classical patient has a 46,XY karyotype, female external genitalia, bilateral streak or dysgenetic gonads, absent or impaired testicular differentiation, and primary gonadal failure. Delayed or absent puberty, absent secondary sexual characteristics, primary amenorrhea, and hypergonadotropic hypogonadism may be the presenting features. Phenotypic males can have cryptorchidism, hypospadias, micropenis, or ambiguous genitalia. (shao2023frasiersyndromea pages 2-4, paul2021suspicionoffrasiers pages 4-7, kitsioutzeli2012sertolicelltumor pages 7-7)

The 2023 case is clinically important because a 15-year-old phenotypic female presented first with delayed puberty; investigation then disclosed 46,XY karyotype, c.1447+4C>T, proteinuria, renal insufficiency, and FSGS. This supports karyotyping and renal evaluation in otherwise unexplained delayed puberty. (shao2023frasiersyndromea pages 2-4, shao2023frasiersyndromea pages 1-2)

Suggested HPO concepts include 46,XY sex reversal, complete/partial gonadal dysgenesis, streak gonad, cryptorchidism, hypospadias, female external genitalia in a 46,XY individual, delayed puberty, primary amenorrhea, and hypergonadotropic hypogonadism.

### Tumors

Dysgenetic gonads containing Y-chromosome material have substantial gonadoblastoma risk, with possible progression or coexistence with dysgerminoma. Tumors can occur in childhood, adolescence, or adulthood. In a 2014 WT1 cohort, three of nine patients with sex reversal developed gonadoblastoma; the 2024 cohort reported four gonadoblastomas, including one intron-9 patient at age 23, and intratubular germ-cell neoplasia in another intron-9 patient at age 15. These small, ascertainment-biased data should not be treated as precise penetrance estimates. (lipska2014genotypephenotypeassociationsin pages 8-9, peer2024clinicalcharacterizationof pages 4-6)

Wilms tumor belongs to the broader WT1 spectrum but appears less characteristic of classical intron-9 FS than of truncating/deletion or zinc-finger missense disorders. In the 2024 cohort, none of four intron-9 cases had Wilms tumor, whereas the overall WT1 cohort rate was 26/43; ascertainment substantially influenced that overall figure. (peer2024clinicalcharacterizationof pages 2-4)

### Quality of life

No FS-specific EQ-5D, SF-36, or PROMIS study was identified. Likely burdens include chronic medication and monitoring, nephrotic edema, hypertension, dialysis, transplantation, infertility, gonadectomy, hormone replacement, tumor anxiety, disclosure of chromosomal findings, and psychosocial issues surrounding sex development. These require individualized, multidisciplinary and developmentally appropriate support.

## 4. Genetic and molecular information

**WT1**, located at 11p13, encodes a zinc-finger transcriptional regulator essential to kidney, podocyte, and gonadal development. Classical FS is produced by germline heterozygous splice-region variants rather than somatic variants. Somatic WT1 alterations may occur in tumors but do not by themselves establish inherited FS. (paul2021suspicionoffrasiers pages 4-7, shao2023frasiersyndromea pages 2-4)

The normal kidney expresses WT1 isoforms with and without a three-amino-acid lysine-threonine-serine insertion. The normal **+KTS:−KTS ratio is approximately 2:1**. Classical intron-9 variants impair the +KTS splice donor and shift the ratio toward approximately **1:2**, rather than simply eliminating all WT1 protein. (paul2021suspicionoffrasiers pages 4-7, peer2024clinicalcharacterizationof pages 2-4)

The recurrent c.1447+4C>T variant is a splice-region variant predicted to disrupt donor-site recognition. Pathogenicity assessment should include phenotype concordance, segregation/de novo evidence, population absence, computational splice prediction, and—where available—RNA evidence under ACMG/AMP criteria. The precise functional label is altered isoform dosage/splicing; describing every intron-9 FS allele as simple haploinsufficiency would be incomplete.

No validated modifier gene, disease-specific methylation pattern, recurrent large chromosomal abnormality, or causal structural variant defines classical FS. Larger 11p13 deletions instead suggest WAGR-spectrum disease. Phenotypic variability among people carrying similar WT1 variants indicates that unknown modifiers probably exist, but this remains inference. (peer2024clinicalcharacterizationof pages 7-9)

## 5. Environmental information

Environmental toxins, radiation, pollution, smoking, diet, alcohol, exercise, occupation, and infectious agents are not established causes or triggers. Standard kidney-protective measures—blood-pressure control, avoidance of nephrotoxins, and management of cardiovascular risk—are clinically rational but do not prevent the inherited developmental defect.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous germline WT1 intron-9 splice-region variant **leads to** defective alternative splice-site use.
2. Defective splicing **results in** reduced production of +KTS transcripts and reversal of the normal +KTS:−KTS balance. (paul2021suspicionoffrasiers pages 4-7, peer2024clinicalcharacterizationof pages 2-4)
3. Altered WT1 isoform dosage **leads to** dysregulated transcriptional/RNA-regulatory programs in WT1-dependent developmental and adult cell populations; many specific downstream targets in human FS remain incompletely demonstrated.
4. **Renal branch:** disturbed WT1 activity in podocytes **results in** defective podocyte differentiation/maintenance and glomerular filtration-barrier instability.
5. Podocyte injury and loss **lead to** proteinuria, foot-process dysfunction, segmental sclerosis/FSGS, nephrotic syndrome, progressive nephron loss, CKD, and ESKD. (sambharia2022monogenicfocalsegmental pages 11-12, peer2024clinicalcharacterizationof pages 6-7)
6. **Gonadal branch:** disturbed WT1-dependent gonadal and mesonephric development **leads to** impaired testicular differentiation in susceptible 46,XY embryos.
7. Gonadal dysgenesis **results in** female or atypical external genital development, streak gonads, gonadal hormone deficiency, delayed puberty, amenorrhea, and infertility.
8. Persistence of dysgenetic gonadal tissue containing Y-chromosome material **increases** survival of developmentally abnormal germ cells and **leads to** gonadoblastoma risk; detailed intermediate molecular steps are partly inferred from DSD tumor biology. (lipska2014genotypephenotypeassociationsin pages 8-9, peer2024clinicalcharacterizationof pages 4-6)

The initiating splice defect is upstream; podocyte loss, sclerosis, endocrine failure, and neoplasia are downstream. No primary metabolic enzyme deficiency, ion-channel defect, infection, or systemic autoimmune process is implicated. Inflammation and fibrosis are secondary consequences of chronic tissue injury rather than the initiating lesion.

Suggested GO processes include RNA splicing, regulation of transcription by RNA polymerase II, metanephric glomerulus development, podocyte differentiation, maintenance of glomerular filtration barrier, gonad development, and sex differentiation. Suggested cell types include podocyte, gonadal somatic/supporting cell, Sertoli-lineage cell, and primordial germ cell; exact GO/CL identifiers should be validated.

No robust FS-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or CRISPR-screen signature was identified. These are priority research gaps.

## 7. Anatomical structures affected

Primary organs are the **kidneys** and **gonads**. In the kidney, the glomerulus—particularly visceral epithelial cells/podocytes—is the principal target; secondary tubulointerstitial fibrosis and whole-kidney failure follow progressive glomerular injury. In the reproductive system, dysgenetic/streak gonads and mesonephric-derived structures are affected; external genital anatomy varies. (shao2023frasiersyndromea pages 2-4, peer2024clinicalcharacterizationof pages 6-7)

Suggested anatomy terms are kidney, renal glomerulus, glomerular visceral epithelium, gonad, testis, streak gonad, uterus, and external genitalia. Suggested Cell Ontology term: podocyte. At the subcellular level WT1 primarily acts in the nucleus through its zinc-finger regulatory domains, while +KTS isoforms also have RNA-associated functions. Bilaterality is typical for gonadal dysgenesis and diffuse genetic nephropathy, although histologic sclerosis is segmental and tumor involvement may be unilateral or bilateral.

## 8. Temporal development

The gonadal-development lesion is prenatal/congenital, although it may remain clinically unsuspected until pubertal failure. Renal disease is generally insidious and progressive: childhood proteinuria → SRNS/FSGS → CKD → ESKD, often in the second decade, but onset and progression vary. Classical FS tends to progress more slowly than Denys–Drash syndrome. (shao2023frasiersyndromea pages 1-2, sambharia2022monogenicfocalsegmental pages 11-12)

In the 2024 national cohort, all four intron-9 patients developed CKD at a median age of 15 years. This is stronger recent evidence for later onset than older descriptions, but the subgroup is very small. Lifelong surveillance remains appropriate because WT1-associated kidney failure may occur well beyond childhood. (peer2024clinicalcharacterizationof pages 2-4, peer2024clinicalcharacterizationof pages 7-9)

There is no spontaneous remission of the genetic lesion. Proteinuria may be attenuated symptomatically, but established sclerosis is usually progressive. Critical intervention windows are: early genetic diagnosis before unnecessary immunosuppression; gonadal evaluation before neoplasia; endocrine planning before or during puberty; and CKD care before irreversible complications.

## 9. Inheritance and population

Inheritance is autosomal dominant, commonly arising de novo. Penetrance is high for some WT1-associated manifestations but is not precisely quantified for FS; expressivity is clearly variable. No anticipation is recognized. Parental germline mosaicism is theoretically possible even when blood testing is negative, so recurrence risk is low but not absolutely zero after an apparently de novo finding.

No valid population prevalence or annual incidence per 100,000 is available. No consistent geographic, ancestry, founder, or consanguinity association is established. WT1 variants accounted for approximately 6% of SRNS in one intensively studied cohort, but this is neither population prevalence nor an FS-specific percentage. (lipska2014genotypephenotypeassociationsin pages 8-9)

A conventional male:female ratio is biologically misleading because chromosomal sex, gonadal development, external phenotype, and gender identity can differ. Most classical reports concern 46,XY individuals with a female phenotype, but phenotypic males and 46,XX cases occur.

## 10. Diagnostics

### Clinical evaluation

Evaluation should include urinalysis and urine protein quantification, serum creatinine/eGFR, albumin, electrolytes, blood pressure, renal ultrasonography, pubertal staging, LH/FSH and sex steroids when indicated, pelvic/gonadal ultrasonography or MRI, and chromosome analysis. Tumor-marker testing is guided by the gonadal lesion and specialist team; normal markers do not exclude gonadoblastoma.

Kidney biopsy may show FSGS and can characterize unexplained SRNS, but molecular diagnosis is decisive and biopsy is not required when the clinical-genetic diagnosis is clear. Gonadal pathology after surgery should assess gonadoblastoma, dysgerminoma, and germ-cell neoplasia.

### Genetic testing strategy

Preferred testing is a comprehensive nephrotic-syndrome/DSD panel including WT1 or full WT1 sequencing with intron-exon boundaries plus deletion/duplication analysis. Targeted testing for c.1447+4C>T and other intron-9 donor variants is efficient when the phenotype is classic, but a negative hotspot test should be followed by full-gene analysis. WES or WGS is useful for atypical or panel-negative disease; WGS can better interrogate noncoding/structural variation. CMA or karyotype is appropriate when a larger 11p13 deletion or sex-chromosome discordance is suspected. FISH is situational. Mitochondrial and repeat-expansion testing are not routinely relevant. (peer2024clinicalcharacterizationof pages 2-4, peer2024clinicalcharacterizationof pages 7-9)

RNA analysis can demonstrate abnormal splicing and help resolve a VUS, but it is not yet routine. No validated proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic test exists.

### Diagnostic clues and differential diagnosis

Genetic testing and karyotyping should be prioritized in: (1) childhood SRNS/FSGS with atypical genitalia; (2) a phenotypic female with SRNS, CKD, delayed puberty, or primary amenorrhea; and (3) unexplained CKD with cryptorchidism or hypospadias. (shao2023frasiersyndromea pages 1-2, drayer2022spectrumofclinical pages 10-11)

Differentials include Denys–Drash syndrome/other WT1 disorder, WAGR syndrome, isolated genetic FSGS (e.g., NPHS1, NPHS2, LAMB2, PLCE1), complete androgen insensitivity, Swyer syndrome from other genes, 5α-reductase or 17β-HSD deficiency, NR5A1-related DSD, and Turner syndrome in a phenotypic female with pubertal failure. Denys–Drash usually has earlier, faster nephropathy, often DMS, and greater Wilms-tumor association; however, overlap is substantial and genotype should supersede rigid clinical labels. (shao2023frasiersyndromea pages 2-4, roca2009evolutivestudyof pages 5-6)

Population newborn screening is not available. Cascade testing should be offered after a familial variant is identified.

## 11. Outcome and prognosis

Renal prognosis without transplantation is poor: proteinuria and FSGS generally progress to ESKD. Frasier-specific five- or ten-year survival and life-expectancy estimates are unavailable. Mortality depends principally on renal failure, cardiovascular/dialysis complications, tumor development, and access to transplantation.

Kidney transplantation is effective because the molecular lesion is intrinsic to the native kidney; recurrence of genetic FSGS in the allograft is expected to be negligible. In a broader nine-child WT1 series, all underwent transplantation at a median age of five years; during median nine-year follow-up, two grafts were lost after seven and ten years and no post-transplant malignancy was observed. These outcomes cannot be assumed to represent FS alone. (drayer2022spectrumofclinical pages 1-2)

A 2021 suspected case with severe untreated ESKD died after dialysis-associated cardiac arrest, illustrating the consequences of late recognition, but molecular confirmation was absent. (paul2021suspicionoffrasiers pages 1-4)

No validated FS-specific prognostic biomarker exists beyond genotype class, age/onset of proteinuria, kidney function trajectory, renal histology, and gonadal status. The 2024 cohort supports variant class as a broad predictor but also documents substantial within-class variability. (peer2024clinicalcharacterizationof pages 1-2, peer2024clinicalcharacterizationof pages 7-9)

## 12. Treatment

There is no approved disease-modifying or splice-correcting therapy.

**Renal care:** ACE inhibition or angiotensin-receptor blockade may reduce proteinuria and control hypertension; standard CKD care includes salt/fluid management, anemia and mineral-bone treatment, vaccination, cardiovascular-risk control, and avoidance of nephrotoxins. Because genetic WT1 podocytopathy is usually immunosuppression-resistant, prolonged corticosteroid, calcineurin-inhibitor, or other immunosuppressive trials should generally be avoided once a causal diagnosis is established. (drayer2022spectrumofclinical pages 1-2, drayer2022spectrumofclinical pages 10-11)

**Kidney replacement:** dialysis is used for ESKD, followed by kidney transplantation when feasible. Disease recurrence in the graft is unlikely. Native nephrectomy is individualized for severe hypertension, protein loss, tumor, or surgical considerations; prophylactic nephrectomy solely for FS is not supported by consensus. (drayer2022spectrumofclinical pages 10-11)

**Gonadal management:** dysgenetic gonads containing Y-chromosome material should be evaluated promptly by a multidisciplinary DSD/tumor team. Prophylactic bilateral gonadectomy is commonly recommended because surveillance cannot reliably exclude microscopic gonadoblastoma. Timing should balance malignancy risk, anatomy, hormonal function, age, assent/consent, fertility implications, and patient preferences. (sambharia2022monogenicfocalsegmental pages 11-12, lipska2014genotypephenotypeassociationsin pages 8-9)

**Endocrine and psychosocial care:** pubertal induction or maintenance with individualized sex-steroid replacement is used after gonadectomy or for gonadal failure. Bone health, fertility counseling, sexual health, gender identity, and psychological support are integral. A 2023 patient underwent bilateral gonadectomy but declined hormone therapy, demonstrating that real-world management requires informed shared decision-making. (shao2023frasiersyndromea pages 2-4)

Suggested NCIT intervention concepts include genetic testing, gonadectomy, hormone-replacement therapy, ACE inhibitor therapy, hemodialysis, and kidney transplantation; identifiers should be normalized against the current NCIt release. No FS-specific pharmacogenomic guidance is available.

A completed observational registry, **NCT01252901**, enrolled 52 people with WT1-associated diseases. No FS-specific interventional, gene-therapy, RNA-therapy, cell-therapy, or CRISPR trial was identified. Thus, no controlled response rates or FS-specific adverse-event statistics are available.

## 13. Prevention

The spontaneous de novo occurrence of many variants means primary prevention is generally impossible. Genetic counseling, reproductive options—including targeted prenatal diagnosis and preimplantation genetic testing for a known familial variant—can reduce recurrence according to individual preferences.

Secondary prevention comprises early detection: cascade testing, chromosome analysis in clinically suspicious phenotypic females, early WT1 testing in SRNS/FSGS, renal surveillance, and prompt gonadal assessment. Tertiary prevention includes RAAS blockade and CKD management, avoidance of ineffective immunosuppression/nephrotoxins, timely gonadectomy to prevent gonadal malignancy, hormone replacement where appropriate, and transplantation before severe ESKD complications. No vaccine, antimicrobial prophylaxis, dietary regimen, or environmental intervention prevents FS itself.

## 14. Other species and natural disease

No established naturally occurring veterinary syndrome exactly equivalent to human FS was identified. Therefore, breed associations, VBO mappings, veterinary prevalence, zoonotic potential, and cross-species transmission are not applicable. The disease is genetic and noncommunicable.

The WT1 developmental program is evolutionarily conserved, making vertebrate models informative. Relevant taxonomy includes **Homo sapiens** (NCBI Taxon 9606) and **Mus musculus** (Taxon 10090). Ortholog identifiers should be imported directly from NCBI Gene/Alliance releases rather than inferred from the literature.

## 15. Model organisms and experimental systems

The strongest disease-mechanism model is the mouse with engineered reduction or loss of the +KTS isoform. Heterozygous reduction of +KTS produces glomerulosclerosis, while homozygous absence causes complete XY sex reversal. This reproduces the two principal human mechanistic branches and strongly supports causal involvement of isoform imbalance. (sambharia2022monogenicfocalsegmental pages 11-12)

Limitations are important: engineered mice do not reproduce the full range of human renal timing, gonadoblastoma penetrance, tumor histology, endocrine management, fertility, or psychosocial outcomes. Podocyte cultures, patient-derived cells, iPSCs, and kidney/gonadal organoids could test variant-specific splicing and downstream programs, but no validated FS-specific organoid or high-throughput therapeutic platform was identified in the retrieved evidence.

## Evidence appraisal and priorities

The evidence base is constrained by ultra-rarity, inconsistent historical terminology, case-report enrichment, and mixing of FS with broader WT1 disorders. The 2024 national cohort is authoritative for the modern spectrum concept but includes only four intron-9 cases and is clinically ascertained. Its key conclusion—quoted from the article—is: **“Therefore, life-long surveillance of kidney function is recommended.”** (peer2024clinicalcharacterizationof pages 1-2, peer2024clinicalcharacterizationof pages 7-9)

Research priorities are prospective international natural-history cohorts; standardized genotype, karyotype and gonadal-pathology reporting; age-specific tumor-risk estimation; patient-reported outcomes; fertility and endocrine outcomes; single-cell studies of human podocyte and gonadal development; and variant-specific RNA/splice-correction strategies. Until those data emerge, early molecular diagnosis, multidisciplinary DSD care, gonadal tumor prevention, and planned renal replacement remain the principal real-world interventions.

References

1. (shao2023frasiersyndromea pages 1-2): Qing Shao, Xinglei Xie, Jia Geng, Xiaoling Yang, Wei Li, and Yuwei Zhang. Frasier syndrome: a 15-year-old phenotypically female adolescent presenting with delayed puberty and nephropathy. Mar 2023. URL: https://doi.org/10.3390/children10030577, doi:10.3390/children10030577. This article has 6 citations.

2. (sambharia2022monogenicfocalsegmental pages 11-12): Meenakshi Sambharia, Prerna Rastogi, and Christie P. Thomas. Monogenic focal segmental glomerulosclerosis: a conceptual framework for identification and management of a heterogeneous disease. American Journal of Medical Genetics. Part C, Seminars in Medical Genetics, 190:377-398, Jul 2022. URL: https://doi.org/10.1002/ajmg.c.31990, doi:10.1002/ajmg.c.31990. This article has 35 citations.

3. (peer2024clinicalcharacterizationof pages 7-9): Sophie E. van Peer, Roland P. Kuiper, Janna A. Hol, Sanne Egging, Bert van der Zwaag, Marc R. Lilien, M. Paola Lombardi, Marry M. van den Heuvel-Eibrink, and Marjolijn C.J. Jongmans. Clinical characterization of a national cohort of patients with germline wt1 variants including late-onset phenotypes. Dec 2024. URL: https://doi.org/10.1016/j.ekir.2024.09.007, doi:10.1016/j.ekir.2024.09.007. This article has 8 citations and is from a peer-reviewed journal.

4. (peer2024clinicalcharacterizationof pages 1-2): Sophie E. van Peer, Roland P. Kuiper, Janna A. Hol, Sanne Egging, Bert van der Zwaag, Marc R. Lilien, M. Paola Lombardi, Marry M. van den Heuvel-Eibrink, and Marjolijn C.J. Jongmans. Clinical characterization of a national cohort of patients with germline wt1 variants including late-onset phenotypes. Dec 2024. URL: https://doi.org/10.1016/j.ekir.2024.09.007, doi:10.1016/j.ekir.2024.09.007. This article has 8 citations and is from a peer-reviewed journal.

5. (peer2024clinicalcharacterizationof pages 2-4): Sophie E. van Peer, Roland P. Kuiper, Janna A. Hol, Sanne Egging, Bert van der Zwaag, Marc R. Lilien, M. Paola Lombardi, Marry M. van den Heuvel-Eibrink, and Marjolijn C.J. Jongmans. Clinical characterization of a national cohort of patients with germline wt1 variants including late-onset phenotypes. Dec 2024. URL: https://doi.org/10.1016/j.ekir.2024.09.007, doi:10.1016/j.ekir.2024.09.007. This article has 8 citations and is from a peer-reviewed journal.

6. (shao2023frasiersyndromea pages 2-4): Qing Shao, Xinglei Xie, Jia Geng, Xiaoling Yang, Wei Li, and Yuwei Zhang. Frasier syndrome: a 15-year-old phenotypically female adolescent presenting with delayed puberty and nephropathy. Mar 2023. URL: https://doi.org/10.3390/children10030577, doi:10.3390/children10030577. This article has 6 citations.

7. (paul2021suspicionoffrasiers pages 4-7): Axler JEAN PAUL, Dieuguens LOUIS, Ansly Jefferson DESRAVINES, Raema Mimrod JEAN, Alfadler JEAN BAPTISTE, Jean Henold BUTEAU, and Wislet ANDRE. Suspicion of frasier's syndrome in the nephrology unit of the internal medicine department of the hueh: case study and review of the literature. Jun 2021. URL: https://doi.org/10.21203/rs.3.rs-622151/v1, doi:10.21203/rs.3.rs-622151/v1. This article has 0 citations.

8. (peer2024clinicalcharacterizationof pages 4-6): Sophie E. van Peer, Roland P. Kuiper, Janna A. Hol, Sanne Egging, Bert van der Zwaag, Marc R. Lilien, M. Paola Lombardi, Marry M. van den Heuvel-Eibrink, and Marjolijn C.J. Jongmans. Clinical characterization of a national cohort of patients with germline wt1 variants including late-onset phenotypes. Dec 2024. URL: https://doi.org/10.1016/j.ekir.2024.09.007, doi:10.1016/j.ekir.2024.09.007. This article has 8 citations and is from a peer-reviewed journal.

9. (peer2024clinicalcharacterizationof pages 6-7): Sophie E. van Peer, Roland P. Kuiper, Janna A. Hol, Sanne Egging, Bert van der Zwaag, Marc R. Lilien, M. Paola Lombardi, Marry M. van den Heuvel-Eibrink, and Marjolijn C.J. Jongmans. Clinical characterization of a national cohort of patients with germline wt1 variants including late-onset phenotypes. Dec 2024. URL: https://doi.org/10.1016/j.ekir.2024.09.007, doi:10.1016/j.ekir.2024.09.007. This article has 8 citations and is from a peer-reviewed journal.

10. (drayer2022spectrumofclinical pages 6-8): Patricia Arroyo-Parejo Drayer, Wacharee Seeherunvong, Chryso P. Katsoufis, Marissa J. DeFreitas, Tossaporn Seeherunvong, Jayanthi Chandar, and Carolyn L. Abitbol. Spectrum of clinical manifestations in children with wt1 mutation: case series and literature review. Frontiers in Pediatrics, Apr 2022. URL: https://doi.org/10.3389/fped.2022.847295, doi:10.3389/fped.2022.847295. This article has 24 citations.

11. (lipska2014genotypephenotypeassociationsin pages 8-9): Beata S. Lipska, Bruno Ranchin, Paraskevas Iatropoulos, Jutta Gellermann, Anette Melk, Fatih Ozaltin, Gianluca Caridi, Tomas Seeman, Kalman Tory, Augustina Jankauskiene, Aleksandra Zurowska, Maria Szczepanska, Anna Wasilewska, Jerome Harambat, Agnes Trautmann, Amira Peco-Antic, Halina Borzecka, Anna Moczulska, Bassam Saeed, Radovan Bogdanovic, Mukaddes Kalyoncu, Eva Simkova, Ozlem Erdogan, Kristina Vrljicak, Ana Teixeira, Marta Azocar, and Franz Schaefer. Genotype-phenotype associations in wt1 glomerulopathy. Kidney international, 85 5:1169-78, May 2014. URL: https://doi.org/10.1038/ki.2013.519, doi:10.1038/ki.2013.519. This article has 204 citations and is from a highest quality peer-reviewed journal.

12. (drayer2022spectrumofclinical pages 10-11): Patricia Arroyo-Parejo Drayer, Wacharee Seeherunvong, Chryso P. Katsoufis, Marissa J. DeFreitas, Tossaporn Seeherunvong, Jayanthi Chandar, and Carolyn L. Abitbol. Spectrum of clinical manifestations in children with wt1 mutation: case series and literature review. Frontiers in Pediatrics, Apr 2022. URL: https://doi.org/10.3389/fped.2022.847295, doi:10.3389/fped.2022.847295. This article has 24 citations.

13. (drayer2022spectrumofclinical pages 1-2): Patricia Arroyo-Parejo Drayer, Wacharee Seeherunvong, Chryso P. Katsoufis, Marissa J. DeFreitas, Tossaporn Seeherunvong, Jayanthi Chandar, and Carolyn L. Abitbol. Spectrum of clinical manifestations in children with wt1 mutation: case series and literature review. Frontiers in Pediatrics, Apr 2022. URL: https://doi.org/10.3389/fped.2022.847295, doi:10.3389/fped.2022.847295. This article has 24 citations.

14. (kitsioutzeli2012sertolicelltumor pages 7-7): Sophia Kitsiou-Tzeli, Maria Deligiorgi, Sophia Malaktari-Skarantavou, Charalampos Vlachopoulos, Spyridon Megremis, Irene Fylaktou, Joanne Traeger-Synodinos, Christina Kanaka-Gantenbein, Christodoulos Stefanadis, and Emmanuel Kanavakis. Sertoli cell tumor and gonadoblastoma in an untreated 29-year-old 46,xy phenotypic male with frasier syndrome carrying a wt1 ivs9+4c>t mutation. Hormones, 11:361-367, Jul 2012. URL: https://doi.org/10.14310/horm.2002.1366, doi:10.14310/horm.2002.1366. This article has 13 citations and is from a peer-reviewed journal.

15. (roca2009evolutivestudyof pages 5-6): Ana Pilar Nso Roca, Antonia Peña Carrión, Marta Benito Gutiérrez, Carmen García Meseguer, Araceli García Pose, and Mercedes Navarro. Evolutive study of children with diffuse mesangial sclerosis. Pediatric Nephrology, 24:1013-1019, May 2009. URL: https://doi.org/10.1007/s00467-008-1063-z, doi:10.1007/s00467-008-1063-z. This article has 32 citations and is from a domain leading peer-reviewed journal.

16. (paul2021suspicionoffrasiers pages 1-4): Axler JEAN PAUL, Dieuguens LOUIS, Ansly Jefferson DESRAVINES, Raema Mimrod JEAN, Alfadler JEAN BAPTISTE, Jean Henold BUTEAU, and Wislet ANDRE. Suspicion of frasier's syndrome in the nephrology unit of the internal medicine department of the hueh: case study and review of the literature. Jun 2021. URL: https://doi.org/10.21203/rs.3.rs-622151/v1, doi:10.21203/rs.3.rs-622151/v1. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Frasier_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `Taxon`.

No term could be looked up either way, so nothing here was confirmed or contradicted.