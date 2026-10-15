---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T23:24:01.782734'
end_time: '2026-09-04T23:33:30.814273'
duration_seconds: 569.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Hypophosphatemic Rickets 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - Taxon
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Hypophosphatemic_Rickets_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Hypophosphatemic Rickets 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Hypophosphatemic Rickets 1** covering all of the
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
- **Disease Name:** Autosomal Recessive Hypophosphatemic Rickets 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Hypophosphatemic Rickets 1** covering all of the
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


# Autosomal Recessive Hypophosphatemic Rickets 1 (ARHR1): Disease-Characteristics Report

## Executive summary

Autosomal recessive hypophosphatemic rickets 1 (ARHR1) is an ultra-rare, Mendelian, fibroblast growth factor 23 (FGF23)-mediated phosphate-wasting disorder caused by biallelic loss-of-function variants in **DMP1**. DMP1 deficiency disrupts osteocyte maturation and extracellular-matrix mineralization and increases osteocytic FGF23 production. Excess FGF23 causes renal phosphate wasting and inappropriately low calcitriol, producing childhood rickets, growth failure, lower-limb deformity, dental disease, and persistent adult osteomalacia. Severe untreated or undertreated disease can progress to fractures, enthesopathy, ligamentous ossification, degenerative arthritis, ankylosis, and major mobility loss. The evidence base is limited to small families, individual cases, and animal models; reliable prevalence, phenotype-frequency, survival, and treatment-response estimates are unavailable. (makitie2010longtermclinicaloutcome pages 1-2, courbon2023fgf23directlyinhibits pages 1-2, makitie2010longtermclinicaloutcome pages 2-4)

The following table provides a compact knowledge-base representation.

| Domain | Curated finding | Suggested ontology terms | Evidence type / key source |
|---|---|---|---|
| Identity | **Autosomal recessive hypophosphatemic rickets 1 (ARHR1)** is an FGF23-mediated renal phosphate-wasting disorder caused by biallelic loss-of-function variants in **DMP1**. **OMIM: 241520**. | MONDO: ARHR1; MeSH: Rickets, Hypophosphatemia | Disease-resource synthesis and human genetics (gu2018targetedresequencingof pages 6-7, clinkenbeard2017heritableandacquired pages 4-6, nakanishi2022pathogenesisoffgf23related pages 7-8) |
| Gene and inheritance | **DMP1** encodes dentin matrix acidic phosphoprotein 1, a secreted SIBLING-family extracellular-matrix protein expressed in osteocytes, mature osteoblasts, and odontoblasts. Inheritance is autosomal recessive; variants are germline. | HP:0000007; GO:0005576; CL:0000137 osteocyte; CL:0000062 osteoblast; CL:0000060 odontoblast | Human genetics and model evidence (makitie2010longtermclinicaloutcome pages 1-2, yamazaki2022osteocytesandthe pages 3-5, clinkenbeard2017heritableandacquired pages 4-6) |
| Pathogenic variation | Reported loss-of-function classes include start-loss, nonsense, splice-site, and C-terminal variants. Examples: **c.730G>T (p.Glu244Ter)**, **c.1122T>G (p.Tyr374Ter)**, and **IVS5-1G>A**. Population frequency and ACMG classification require variant-specific database review. | SO:0001587 stop-gained; SO:0001574 splice-acceptor variant; SO:0002012 start-lost | Primary sequencing and family studies (chaturvedi2024lessonslearnedfrom pages 6-7, makitie2010longtermclinicaloutcome pages 1-2, gu2018targetedresequencingof pages 6-7) |
| Epidemiology | **Unknown.** No reliable ARHR1-specific prevalence, incidence, carrier-frequency, or survival estimates exist. Published evidence consists chiefly of individual families and small case series; both sexes are expected to be affected equally. | Orphanet rare disease; HP:0000007 | Evidence gap in clinical literature (chaturvedi2024lessonslearnedfrom pages 7-8, chaturvedi2024lessonslearnedfrom pages 1-2, gu2018targetedresequencingof pages 6-7) |
| Core phenotypes | Childhood-onset rickets and persistent osteomalacia; bone pain, short stature, impaired growth, genu varum/valgum, abnormal gait, fractures, and progressive skeletal deformity. Dental abnormalities and abscesses may occur; hearing impairment has been reported but its frequency is unknown. | HP:0002748 Rickets; HP:0004349 Osteomalacia; HP:0004322 Short stature; HP:0002970 Genu varum; HP:0002857 Genu valgum; HP:0000164 Abnormal dentition; HP:0000365 Hearing impairment | Human case series and long-term family study (makitie2010longtermclinicaloutcome pages 7-9, makitie2010longtermclinicaloutcome pages 2-4, gu2018targetedresequencingof pages 6-7) |
| Biomarkers | Low age-adjusted serum phosphate with renal phosphate wasting or reduced **TmP/GFR**; elevated ALP during active rickets; elevated or inappropriately normal intact FGF23; low or inappropriately normal 1,25-dihydroxyvitamin D. Calcium is often normal and PTH may be elevated. One adolescent had phosphate **0.76 mmol/L**, ALP **741 U/L**, and calcium **2.46 mmol/L**. | HP:0002148 Hypophosphatemia; CHEBI:26020 phosphate; CHEBI:17823 calcitriol | Human biochemical evidence (nakanishi2022pathogenesisoffgf23related pages 7-8, haffner2022ricketsguidanceparta pages 1-2, gu2018targetedresequencingof pages 6-7) |
| Mechanism | Biallelic DMP1 loss **leads to** defective osteocyte maturation and matrix mineralization; this **leads to** increased osteocytic FGF23, probably partly through enhanced FGFR signaling; excess FGF23 **leads to** renal phosphate wasting and suppressed calcitriol; chronic hypophosphatemia plus local DMP1/FGF23 effects **result in** impaired osteoblast differentiation, rickets, and osteomalacia. The FGFR step remains partly inferred. | GO:0030500 regulation of bone mineralization; GO:0045667 regulation of osteoblast differentiation; GO:0008543 FGFR signaling pathway; CL:0000137; CL:0000062 | Human genetics, mouse, primary-cell, and single-cell evidence (courbon2023fgf23directlyinhibits pages 1-2, courbon2023fgf23directlyinhibits pages 11-13, courbon2023fgf23directlyinhibits pages 4-5) |
| Anatomy and cells | Principal sites are growth plates, cortical and trabecular bone, long bones, skull, spine, joints, entheses, and dentin. Key cells are osteocytes, osteoblasts, osteoprogenitors, chondrocytes, odontoblasts, and renal proximal-tubule epithelial cells downstream of FGF23. | UBERON:0000982 skeletal system; UBERON:0001272 long bone; UBERON:0004766 growth plate; UBERON:0002113 kidney; CL:0002306 proximal-tubule epithelial cell | Human radiology/histology and model evidence (makitie2010longtermclinicaloutcome pages 5-7, courbon2023fgf23directlyinhibits pages 4-5, yamazaki2022osteocytesandthe pages 3-5) |
| Diagnostics | Confirm fasting hypophosphatemia using age-specific ranges; document renal wasting by urine studies and TmP/GFR; measure ALP, calcium, PTH, creatinine/eGFR, 25-hydroxyvitamin D, 1,25-dihydroxyvitamin D, and intact FGF23; obtain wrist or knee radiographs; perform a hereditary-rickets panel including **DMP1** with copy-number analysis. Use WES/WGS when panel testing is negative or the phenotype is atypical. | NCIT:C15709 Genetic Testing; NCIT:C17648 Laboratory Procedure; NCIT:C38101 Radiographic Imaging | Guidance and case-based genetic evidence (gu2018targetedresequencingof pages 6-7, chaturvedi2024lessonslearnedfrom pages 7-8, haffner2022ricketsguidanceparta pages 1-2) |
| Treatment | Conventional therapy is divided oral phosphate plus active vitamin D such as calcitriol or alfacalcidol, with surveillance for hyperparathyroidism, hypercalciuria, nephrolithiasis, and nephrocalcinosis. Multidisciplinary dental, rehabilitation, pain, and orthopedic care may be required. | CHEBI:26020 phosphate; CHEBI:17823 calcitriol; NCIT:C15329 Physical Therapy; NCIT:C15214 Orthopedic Surgery | General guidance, ARHR1 clinical experience, and mouse evidence (chaturvedi2024lessonslearnedfrom pages 7-8, haffner2022ricketsguidanceparta pages 1-2, chaturvedi2024lessonslearnedfrom pages 6-7, courbon2023fgf23directlyinhibits pages 1-2) |
| Burosumab status | **Burosumab is off-label/experimental and not specifically approved for ARHR1.** Very limited adult case evidence suggests benefit from FGF23 neutralization, but no ARHR1 randomized trial or reliable response-rate estimate exists. Mouse studies indicate that FGF23 suppression normalizes phosphate but may not fully correct DMP1-dependent mineralization defects. | NCIT:C119744 Burosumab; monoclonal antibody therapy | Small human experience and mechanistic mouse studies (courbon2023fgf23directlyinhibits pages 1-2, chaturvedi2024lessonslearnedfrom pages 7-8, courbon2023fgf23directlyinhibits pages 11-13, courbon2023fgf23directlyinhibits pages 13-15) |
| Prognosis | Disease is chronic and potentially progressive. Inadequately treated adults may develop fractures, enthesopathy, ligamentous ossification, degenerative arthritis, contractures, spinal stenosis, ankylosis, and severe mobility loss. Life expectancy and disease-specific mortality are unknown. | HP:0100686 Enthesopathy; HP:0002757 Recurrent fractures; HP:0001371 Flexion contracture; HP:0000920 Vertebral abnormality | Long-term human follow-up (makitie2010longtermclinicaloutcome pages 5-7, makitie2010longtermclinicaloutcome pages 2-4) |
| Models | **Dmp1-knockout mouse** recapitulates elevated FGF23/PTH, hypophosphatemia, growth failure, rickets, osteomalacia, cortical porosity, abnormal growth plates, and defective osteocyte maturation. Osteocyte-specific Fgf23 deletion normalizes phosphate but only partly rescues bone. DMP1-deficient rabbits also develop elevated FGF23 and hypophosphatemic rickets. | NCBI Taxon:10090 *Mus musculus*; NCBI Taxon:9986 *Oryctolagus cuniculus*; MGI: Dmp1 | Genetic model, cell culture, and single-cell evidence (courbon2023fgf23directlyinhibits pages 11-13, courbon2023fgf23directlyinhibits pages 4-5, yamazaki2022osteocytesandthe pages 3-5, courbon2023fgf23directlyinhibits pages 13-15) |


*Table: Compact curation of DMP1-related ARHR1 covering disease identity, molecular cause, clinical features, diagnostics, treatment status, prognosis, and experimental models. Evidence gaps—including unknown epidemiology and the off-label status of burosumab—are explicitly identified.*

## 1. Disease information

**Definition.** ARHR1 is a hereditary hypophosphatemic rickets/osteomalacia syndrome in which biallelic DMP1 dysfunction causes excessive FGF23 action, renal phosphate wasting, chronic hypophosphatemia, and defective skeletal and dental mineralization. It is distinct from DMP1-independent ARHR2, caused by ENPP1 deficiency. (clinkenbeard2017heritableandacquired pages 4-6, nakanishi2022pathogenesisoffgf23related pages 7-8)

**Identifiers and terminology.** The securely supported identifier is **OMIM/MIM 241520**. Common names include *autosomal recessive hypophosphatemic rickets type 1*, *ARHR1*, *DMP1-related hypophosphatemic rickets*, *DMP1-related autosomal recessive hypophosphatemia*, and historically *autosomal recessive hypophosphatemia/ARHP*. A precise MONDO identifier was not established from the retrieved sources and should be verified directly against the current MONDO release rather than inferred. ICD-10/ICD-11 and MeSH generally classify the broader entities hypophosphatemic rickets, rickets, or disorders of phosphorus metabolism; a dedicated ARHR1 code was not documented in the retrieved literature. (gu2018targetedresequencingof pages 6-7, makitie2010longtermclinicaloutcome pages 1-2)

This report synthesizes **aggregated disease-level literature**, including primary human families/cases and experimental models; it is not derived from an individual EHR.

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is a **germline biallelic loss-of-function DMP1 genotype**. DMP1 encodes dentin matrix acidic phosphoprotein 1, a secreted noncollagenous SIBLING-family matrix protein expressed especially by osteocytes, mature osteoblasts, and odontoblasts. Pathogenic variants impair DMP1 production, processing, secretion, or function. (clinkenbeard2017heritableandacquired pages 4-6, yamazaki2022osteocytesandthe pages 3-5)

### Risk factors

* **Genetic:** two pathogenic DMP1 alleles; parental consanguinity or shared ancestry increases the probability of homozygosity. One Chinese patient with p.Glu244Ter was born to consanguineous parents. A Finnish family originated from the same remote island, suggesting—but not proving—a founder effect. (makitie2010longtermclinicaloutcome pages 2-4, gu2018targetedresequencingof pages 6-7)
* **Family history:** an affected sibling or known carrier parents substantially increases prior probability. For two carrier parents, standard autosomal-recessive recurrence risks per pregnancy are 25% affected, 50% carrier, and 25% neither familial allele.
* **Age/sex:** disease usually becomes evident during childhood growth. Both sexes should be affected equally; no sex-specific biological risk has been established.
* **Environmental/infectious:** no toxin, infection, smoking, alcohol, occupational exposure, or other environmental factor causes ARHR1. Low calcium intake or vitamin-D deficiency can worsen mineralization but is a comorbidity rather than the initiating cause.

### Protective factors and gene–environment interaction

No validated protective DMP1 allele or modifier gene is known. Adequate calcium intake and normal 25-hydroxyvitamin-D status support mineralization but do not prevent disease in a person with biallelic DMP1 loss. A clinically important interaction is phosphate exposure: in adult Dmp1-null mice, phosphate supplementation begun at six weeks increased FGF23, PTH, urinary phosphate loss, and osteomalacia rather than correcting disease. This result cautions against unmonitored phosphate monotherapy but cannot be directly translated into a human prohibition against carefully combined phosphate and active vitamin D. (courbon2023fgf23directlyinhibits pages 1-2, courbon2023fgf23directlyinhibits pages 13-15)

## 3. Phenotypes

ARHR1 normally begins insidiously in infancy or early childhood and is chronic. Frequencies cannot be estimated reliably because published cohorts are extremely small.

* **Rickets/osteomalacia:** defective growth-plate and mature-bone mineralization; generally progressive if inadequately treated. Suggested terms: **HP:0002748 Rickets**, **HP:0004349 Osteomalacia**. Bone biopsy may show increased osteoid volume/thickness, absent tetracycline double labels, reduced mineralizing surface, and prolonged mineralization lag time. (makitie2010longtermclinicaloutcome pages 7-9, makitie2010longtermclinicaloutcome pages 5-7)
* **Hypophosphatemia and renal phosphate wasting:** persistent laboratory hallmarks, with elevated or inappropriately normal intact FGF23 and low/inappropriately normal 1,25(OH)2D. Suggested terms: **HP:0002148 Hypophosphatemia** and an HPO renal-phosphate-wasting annotation. (ichikawa2017amutationin pages 1-1, nakanishi2022pathogenesisoffgf23related pages 7-8)
* **Raised alkaline phosphatase:** reflects active rickets/osteoblast activity. In one affected 18-year-old, phosphate was **0.76 mmol/L**, ALP **741 U/L**, and calcium **2.46 mmol/L**. (gu2018targetedresequencingof pages 6-7)
* **Growth and deformity:** short stature, impaired linear growth, bowed legs, genu varum or valgum, coxa vara, widened metaphyses, abnormal epiphyses, cortical abnormalities, and delayed growth-plate closure. Suggested terms include **HP:0004322 Short stature**, **HP:0002970 Genu varum**, **HP:0002857 Genu valgum**, and **HP:0002673 Coxa vara**. The same 18-year-old was 145 cm and had painful legs and varus knees beginning at 18 months. (makitie2010longtermclinicaloutcome pages 5-7, gu2018targetedresequencingof pages 6-7)
* **Pain, weakness, gait, and function:** bone/joint pain, muscle weakness, abnormal or waddling gait, impaired mobility, and fatigue are expected consequences. Suggested terms: **HP:0002653 Bone pain**, **HP:0003326 Myalgia/muscle weakness as appropriate**, and **HP:0001288 Gait disturbance**.
* **Fracture and orthopedic morbidity:** insufficiency/pathologic fractures, joint destruction, contractures, scoliosis/kyphosis, and repeated corrective operations may occur. A severely affected woman underwent osteotomies from age six, more than 30 orthopedic procedures, bilateral femoral-neck-fracture repair, hip replacements at ages 57 and 61, and treatment for cervical spinal stenosis. (makitie2010longtermclinicaloutcome pages 2-4)
* **Enthesopathy and extraskeletal ossification:** progressive enthesopathy, interosseous-membrane and paraspinal-ligament calcification, spinal ankylosis, and generalized degenerative arthritis are prominent adult complications. Suggested terms: **HP:0100686 Enthesopathy**, **HP:0002753/appropriate ankylosis term**, and **HP:0001371 Contracture**. (makitie2010longtermclinicaloutcome pages 7-9, makitie2010longtermclinicaloutcome pages 5-7)
* **Craniofacial/skull:** cranial hyperostosis has been reported; one patient had dural ectasia, but causality was uncertain. Suggested term: **HP:0004434 Hyperostosis of the skull**. (makitie2010longtermclinicaloutcome pages 9-10, makitie2010longtermclinicaloutcome pages 5-7)
* **Dental:** poor dental development, hypomineralization, periodontal disease, gingival/dental abscesses, delayed eruption, and tooth loss may occur. Suggested terms: **HP:0000164 Abnormality of dentition**, **HP:0000691 Dental abscess**, and more specific enamel/dentin terms where documented. One adult required a dental prosthesis from age 50 after recurrent gingival abscesses. (makitie2010longtermclinicaloutcome pages 2-4, gu2018targetedresequencingof pages 6-7)
* **Hearing:** impairment has been reported in severe adult disease, but one adolescent had normal hearing; frequency and mechanism are unknown. Suggested term: **HP:0000365 Hearing impairment**. (makitie2010longtermclinicaloutcome pages 2-4, gu2018targetedresequencingof pages 6-7)

No ARHR1-specific EQ-5D, SF-36, PROMIS, or validated disease-specific quality-of-life dataset was identified. Nonetheless, severe pain, short stature, repeated surgery, dental morbidity, spinal immobility, and loss of ambulation indicate potentially profound physical and psychosocial impact. (makitie2010longtermclinicaloutcome pages 5-7, makitie2010longtermclinicaloutcome pages 2-4)

## 4. Genetic and molecular information

**Causal gene:** **DMP1**; biallelic germline variants cause ARHR1. Variant classes include start-loss, nonsense, splice-acceptor/splice-disrupting, frameshift, and C-terminal alterations. Examples documented in the retrieved evidence include **c.730G>T (p.Glu244Ter)**, **c.1122T>G (p.Tyr374Ter)**, and **IVS5-1G>A** at the exon-6 splice acceptor. (chaturvedi2024lessonslearnedfrom pages 6-7, makitie2010longtermclinicaloutcome pages 1-2, gu2018targetedresequencingof pages 6-7)

The p.Glu244Ter variant was found by >100× targeted sequencing and confirmed by Sanger sequencing. Variant pathogenicity should be curated transcript-specifically with ClinVar/ClinGen and ACMG/AMP criteria; the retrieved papers do not supply current ClinVar review status or gnomAD frequencies for every allele. Absence or extreme rarity in population databases is expected for fully penetrant severe alleles but must not be assumed for a particular variant. (gu2018targetedresequencingof pages 6-7)

DMP1 is processed in bone matrix into approximately **37-kDa N-terminal** and **57-kDa C-terminal** fragments. A noncleavable D213A protein phenocopied Dmp1 null mice, whereas the 57-kDa C-terminal fragment rescued bone abnormalities, demonstrating that proteolytic processing is functionally important. (clinkenbeard2017heritableandacquired pages 4-6)

Heterozygotes are usually clinically unaffected carriers, but two carriers in one family had mild hypophosphatemia, and one showed focal osteomalacia. This suggests a possible subtle carrier phenotype rather than a consistently dominant disorder. Penetrance of biallelic pathogenic genotypes appears high in reported families, but numerical penetrance is unknown; expressivity is variable. No anticipation, recurrent somatic mutation, established germline mosaicism rate, modifier gene, disease-specific epigenetic lesion, or recurrent chromosomal abnormality is established. (makitie2010longtermclinicaloutcome pages 1-2, makitie2010longtermclinicaloutcome pages 7-9)

## 5. Environmental information

ARHR1 is not infectious, toxic, occupational, lifestyle-mediated, or zoonotic. Diet changes biochemical substrate availability but do not cause or cure the genetic disorder. Adequate calcium and vitamin-D status are supportive; excessive or poorly balanced phosphate replacement may stimulate FGF23 and hyperparathyroidism. There is no disease-specific evidence that smoking, alcohol, exercise, pollution, radiation, or infection modifies penetrance.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic DMP1 loss-of-function leads to** absent or dysfunctional extracellular DMP1 in bone and dentin matrix. (makitie2010longtermclinicaloutcome pages 1-2, clinkenbeard2017heritableandacquired pages 4-6)
2. **DMP1 deficiency leads to** defective osteocyte maturation and impaired hydroxyapatite nucleation/matrix mineralization. (yamazaki2022osteocytesandthe pages 3-5, clinkenbeard2017heritableandacquired pages 4-6)
3. **Abnormal osteocyte biology leads to** increased FGF23 transcription and altered FGF23 processing in mature osteoblasts/osteocytes. (courbon2023fgf23directlyinhibits pages 13-15, ichikawa2017amutationin pages 1-1)
4. **Enhanced FGFR signaling in osteocytes probably contributes to** FGF23 overproduction; this step is supported by model data but remains partly inferred rather than fully resolved in human ARHR1. (nakanishi2022pathogenesisoffgf23related pages 7-8, yamazaki2022osteocytesandthe pages 3-5)
5. **Excess intact FGF23 leads to** reduced renal proximal-tubular phosphate reabsorption and increased phosphaturia, and suppresses renal calcitriol production. (ichikawa2017amutationin pages 1-1, nakanishi2022pathogenesisoffgf23related pages 7-8)
6. **Renal phosphate loss leads to** chronic hypophosphatemia and insufficient phosphate for hydroxyapatite formation, causing growth-plate rickets and generalized osteomalacia. (courbon2023fgf23directlyinhibits pages 1-2, ichikawa2017amutationin pages 1-1)
7. **Branch A—excess FGF23 directly leads to** impaired osteoprogenitor/osteoblast differentiation through pathways involving FGFR1, ERK1/2, and PI3K/AKT in model systems. (courbon2023fgf23directlyinhibits pages 11-13, courbon2023fgf23directlyinhibits pages 4-5)
8. **Branch B—DMP1 loss independently leads to** defective matrix mineralization even when phosphate or FGF23 is corrected. This explains why normalized serum phosphate may not fully rescue bone. (courbon2023fgf23directlyinhibits pages 4-5, courbon2023fgf23directlyinhibits pages 1-2)
9. **Persistent growth-plate and matrix defects result in** short stature, bowed legs, fractures, pain, dental disease, and, over decades, enthesopathy, degenerative joint disease, ligamentous ossification, and immobility. (makitie2010longtermclinicaloutcome pages 2-4, makitie2010longtermclinicaloutcome pages 5-7)

### Cellular and omics evidence

Principal cells are osteocytes (**CL:0000137**), mature osteoblasts (**CL:0000062**), osteoprogenitors, chondrocytes, odontoblasts, and downstream renal proximal-tubule epithelial cells. Suggested processes include **GO:0030500 regulation of bone mineralization**, **GO:0045667 regulation of osteoblast differentiation**, **GO:0008543 FGFR signaling**, MAPK/ERK signaling, PI3K/AKT signaling, phosphate homeostasis, and biomineral tissue development.

In 12-week-old Dmp1-knockout mice, osteoblast/osteocyte-specific Fgf23 deletion rescued about **75%** of elevated total and intact FGF23 and completely corrected secreted FGF23 in differentiated primary osteoblast cultures. It normalized serum phosphate but only partially restored bone growth and mineralization. (courbon2023fgf23directlyinhibits pages 13-15)

Single-cell RNA sequencing used **n=3 mice per genotype** and implicated osteoprogenitor FGFR1, ERK1/2, and PI3K/AKT pathways. This is the most recent advanced-technology evidence retrieved, but no human ARHR1 single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or multi-omic cohort was identified. (courbon2023fgf23directlyinhibits pages 11-13)

A key 2023 conclusion was: **“FGF23-induced hypophosphatemia is only partially responsible for the bone defects observed in Dmp1KO mice.”** The authors proposed combined DMP1 restoration and FGF23 blockade as a mechanistically more complete future strategy. This remains preclinical. (courbon2023fgf23directlyinhibits pages 1-2)

Immune dysregulation, inflammation, apoptosis, autophagy, mitochondrial disease, and epigenetic reprogramming are not established primary mechanisms of ARHR1.

## 7. Anatomical structures affected

* **Primary organs/tissues:** skeleton and dentition—growth plates, cortical and trabecular bone, long bones, skull, spine, joints, entheses, dentin, and periodontium.
* **Secondary organ:** kidney proximal tubule is hormonally affected by FGF23, causing phosphate loss; it is not structurally mutated.
* **Suggested UBERON terms:** skeletal system **UBERON:0000982**, bone tissue, long bone **UBERON:0001272**, growth plate **UBERON:0004766**, skull, vertebral column, joint, tooth/dentin, and kidney **UBERON:0002113**.
* **Subcellular compartments:** extracellular region/matrix (**GO:0005576**, **GO:0031012**); DMP1 enters the secretory pathway and is deposited/processed in mineralized matrix. A nucleus-targeted DMP1 transgene did not rescue dental or periodontal defects in Dmp1-null mice, supporting the extracellular rather than nuclear function during odontogenesis. (yamazaki2022osteocytesandthe pages 3-5, clinkenbeard2017heritableandacquired pages 4-6)
* **Localization:** abnormalities are generally bilateral/systemic rather than unilateral, although deformity severity may be asymmetric.

## 8. Temporal development

Onset is usually chronic and insidious during infancy or early childhood, often recognized after walking begins through leg bowing, pain, short stature, or abnormal gait. One documented case began at 18 months; the Finnish siblings had pain and varus deformity from early childhood. (makitie2010longtermclinicaloutcome pages 1-2, gu2018targetedresequencingof pages 6-7)

A practical natural-history sequence is: early growth-plate rickets and deformity; childhood/adolescent growth failure and orthopedic/dental disease; persistent adult osteomalacia, fractures and pain; and later enthesopathy, ligamentous ossification, degenerative arthritis, spinal stenosis/ankylosis, contractures, and reduced mobility. Course and severity vary, and early effective treatment may reduce—but has not been proven to eliminate—long-term complications. The disease is lifelong; spontaneous remission is not established. (makitie2010longtermclinicaloutcome pages 7-9, makitie2010longtermclinicaloutcome pages 2-4)

Growth is a critical intervention window because untreated growth plates accumulate irreversible deformity. Adult intervention may improve biochemical osteomalacia and pain but cannot be assumed to reverse established skeletal geometry, ankylosis, or osteoarthritis.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Variants are constitutional/germline. Consanguinity has been observed, and geographically restricted ancestry may produce founder alleles, but no universal founder mutation is known. Genetic anticipation is not expected. (makitie2010longtermclinicaloutcome pages 2-4, gu2018targetedresequencingof pages 6-7)

No defensible ARHR1-specific prevalence, incidence, carrier-frequency, geographic-distribution, sex-ratio, or age-distribution estimate was found. The literature comprises a small number of families and cases, so percentages derived from those reports would be misleading. One targeted cohort found one DMP1 case among **86 selected patients with hypophosphatemic rickets/osteomalacia**; this is a diagnostic yield in an enriched cohort, not population prevalence. (gu2018targetedresequencingof pages 6-7)

## 10. Diagnostics

### Clinical and biochemical approach

1. Suspect disease in childhood rickets, short stature, lower-limb bowing, bone pain, abnormal gait, recurrent dental abscesses, or an affected sibling.
2. Confirm low fasting serum phosphate against **age-specific reference intervals** and measure ALP, calcium, creatinine/eGFR, PTH, 25-hydroxyvitamin D, and preferably 1,25-dihydroxyvitamin D.
3. Document inappropriate renal phosphate loss using paired fasting serum/urine phosphate and creatinine, fractional phosphate excretion, tubular phosphate reabsorption, or **TmP/GFR**.
4. Measure intact FGF23 where available. In ARHR1 it is elevated or inappropriately normal for the degree of hypophosphatemia; an inappropriately low FGF23 suggests a transporter defect or non-FGF23 cause.
5. Obtain wrist or knee radiographs for metaphyseal widening, cupping/fraying, and growth-plate abnormalities; standing lower-limb films assist deformity planning. Bone biopsy is not routinely required.
6. Confirm with molecular testing. (gu2018targetedresequencingof pages 6-7, nakanishi2022pathogenesisoffgf23related pages 7-8, haffner2022ricketsguidanceparta pages 1-2)

### Genetic testing

A hereditary hypophosphatemia/rickets panel should include at least **DMP1, PHEX, FGF23, ENPP1, FAM20C, SLC34A1, SLC34A3, SLC9A3R1, CYP27B1, CYP2R1, VDR**, and other laboratory-validated genes, with deletion/duplication analysis. Single-gene DMP1 sequencing is reasonable in a classic recessive pedigree but risks missing phenocopies. WES or WGS is appropriate after negative panels, atypical disease, or suspected novel/structural variants. A 2024 real-world report showed that restricted testing could miss DMP1 disease, whereas WES found **c.1122T>G (p.Tyr374Ter)**; the authors suggested a broad 16-gene panel as a lower-cost alternative. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line unless another phenotype indicates them. (chaturvedi2024lessonslearnedfrom pages 7-8, chaturvedi2024lessonslearnedfrom pages 6-7)

### Differential diagnosis

Differentiate ARHR1 from XLH/PHEX, ADHR/FGF23, ARHR2/ENPP1, FAM20C-related disease, renal phosphate-transporter defects, Fanconi syndromes, nutritional vitamin-D/calcium deficiency, vitamin-D-dependent rickets, renal tubular acidosis, chronic kidney disease, and tumor-induced osteomalacia. Key discriminators are inheritance, age, FGF23 appropriateness, renal phosphate handling, calcitriol, calcium/PTH pattern, extra-skeletal vascular calcification in ENPP1 disease, and molecular testing. Broad genetic testing matters because mechanism determines treatment; a non-FGF23 disorder would not be expected to benefit from FGF23 blockade. (chaturvedi2024lessonslearnedfrom pages 7-8, chaturvedi2024lessonslearnedfrom pages 1-2)

There is no population newborn biochemical screening program. Cascade testing of relatives, parental carrier testing, and testing of at-risk siblings are appropriate after identifying familial variants.

## 11. Outcome and prognosis

Life expectancy, 5- or 10-year survival, and disease-specific mortality have not been quantified. ARHR1 is principally a morbidity-producing rather than known lethal disorder. Long-term prognosis depends on age at diagnosis, severity of phosphate wasting, growth-plate damage, adherence and response to therapy, orthopedic burden, dental disease, and treatment complications.

The strongest long-term evidence involves two adults aged **66 and 78 years** with childhood onset. They developed severe joint pain, contractures, short/deformed long bones, cranial hyperostosis, enthesopathy, paraspinal-ligament calcification, and complete spinal immobilization. This demonstrates survival into older adulthood but also potentially extreme disability; it is not a population prognosis estimate. (makitie2010longtermclinicaloutcome pages 1-2)

Recovery of biochemical abnormalities and active rickets is possible with treatment, but established deformity, osteoarthritis, enthesopathy, ligamentous ossification, and ankylosis may be irreversible. No validated ARHR1-specific prognostic biomarker exists beyond conventional measures of disease activity such as phosphate, ALP, TmP/GFR, PTH, FGF23, growth, pain, and radiographic rickets.

## 12. Treatment and real-world implementation

### Conventional pharmacotherapy

Historically, FGF23-mediated rickets has been treated with divided oral phosphate salts plus active vitamin D—**calcitriol** or **alfacalcidol**—rather than nutritional vitamin D alone. Goals are healing rickets, reducing pain/deformity, improving growth, and avoiding toxicity; forcing serum phosphate continuously into the normal range with large oral doses is not an appropriate stand-alone objective. (chaturvedi2024lessonslearnedfrom pages 7-8, haffner2022ricketsguidanceparta pages 1-2)

Monitor growth, deformity, gait, pain, ALP, phosphate, calcium, PTH, creatinine/eGFR, 25-OH-D, urine calcium, and renal phosphate handling. General rickets guidance suggests visits every 1–3 months in children aged 0–5 years, every 3–6 months before puberty, approximately every three months during puberty, and renal ultrasound every 1–2 years during phosphate/active-vitamin-D or burosumab therapy. Complications include gastrointestinal intolerance, hypercalciuria, nephrolithiasis/nephrocalcinosis, and secondary or tertiary hyperparathyroidism. These schedules are general guidance, not ARHR1 trial-derived rules. (haffner2022ricketsguidanceparta pages 1-2)

Suggested intervention annotations include phosphate supplementation (**CHEBI:26020 phosphate**), calcitriol (**CHEBI:17823**), pharmacotherapy, and nutritional support. No established ARHR1 pharmacogenomic marker is known.

### Burosumab

Burosumab is a fully human monoclonal antibody that neutralizes FGF23. It is mechanistically attractive, but **it is not specifically approved for DMP1-related ARHR1** in the jurisdictions described by the retrieved evidence; use is off-label/experimental and access/reimbursement varies. No ARHR1 randomized trial or reliable response rate was identified. The retrieved literature refers to promising treatment in only two adults and a 2024 real-world DMP1 case, but does not provide sufficient standardized numerical outcomes to estimate efficacy. (courbon2023fgf23directlyinhibits pages 1-2, chaturvedi2024lessonslearnedfrom pages 7-8)

Model evidence provides an important caution: reducing osteocytic FGF23 normalized serum phosphate but only partially rescued bone because DMP1 deficiency itself impairs mineralization. Thus, burosumab may correct the endocrine branch without replacing DMP1’s local matrix function. (courbon2023fgf23directlyinhibits pages 11-13, courbon2023fgf23directlyinhibits pages 13-15)

Suggested NCIT term: **Burosumab/anti-FGF23 monoclonal-antibody therapy**. Treatment should occur through a metabolic-bone specialist with close phosphate monitoring to avoid hyperphosphatemia or ectopic mineralization.

### Surgery, dentistry, and rehabilitation

Corrective osteotomy may be required for persistent severe deformity after metabolic control; joint replacement, fracture repair, or spinal decompression may be necessary in advanced adults. Dental surveillance, prompt management of abscesses, physical therapy, low-impact strengthening, mobility aids, occupational therapy, pain management, and psychosocial support are appropriate. Surgery does not correct the biochemical disease. Suggested NCIT concepts include orthopedic surgery, osteotomy, physical therapy, occupational therapy, rehabilitation, and pain management. (makitie2010longtermclinicaloutcome pages 2-4)

### Experimental therapies

No ARHR1-specific gene, cell, RNA, or CRISPR therapy and no disease-specific interventional ClinicalTrials.gov study were identified. Preclinical evidence supports combined **DMP1 restoration plus FGF23 blockade**, but delivery, safety, dosing, and durability remain unresolved. (courbon2023fgf23directlyinhibits pages 1-2)

## 13. Prevention

Primary prevention by lifestyle or vaccination is not possible. Reproductive prevention options after identifying familial variants include genetic counseling, carrier testing, partner testing, prenatal diagnosis, and preimplantation genetic testing where legally and ethically available. Secondary prevention consists of cascade testing and early biochemical evaluation of at-risk siblings so treatment begins before major growth-plate deformity. Tertiary prevention includes sustained metabolic control, adequate calcium/25-OH-D, renal and PTH surveillance, dental care, physical therapy, fall/fracture prevention, and timely orthopedic assessment. No vaccine, antimicrobial prophylaxis, or environmental public-health intervention applies.

## 14. Other species and natural disease

DMP1 and phosphate-regulatory mechanisms are evolutionarily conserved. Relevant experimental species include **Mus musculus** (NCBI Taxon 10090) and **Oryctolagus cuniculus** (NCBI Taxon 9986). DMP1-deficient rabbits develop elevated FGF23, hypophosphatemic rickets, and severe bone-microarchitecture abnormalities. (yamazaki2022osteocytesandthe pages 3-5)

No well-established naturally occurring companion-animal breed disorder equivalent to human DMP1-ARHR1 was identified in the retrieved evidence. Accordingly, no defensible VBO breed term or veterinary prevalence can be assigned. ARHR1 is noninfectious and has no zoonotic or cross-species transmission.

## 15. Model organisms

The principal model is the **Dmp1-knockout mouse**, a germline genetic mammalian model. It reproduces elevated FGF23/PTH, hypophosphatemia, 30%–35% reductions in body weight and tail/femur length, rickets, osteomalacia, abnormal growth plates, hypomineralized trabecular bone, cortical expansion/porosity, defective osteocyte morphology/connectivity, and reduced osteoclast numbers. (courbon2023fgf23directlyinhibits pages 4-5)

Conditional osteoblast/osteocyte Fgf23 deletion in the Dmp1-null background separates systemic and local mechanisms: phosphate and fractional phosphate excretion normalize, while residual osteoid accumulation and mineralization/canalicular defects remain. Primary osteoblast/osteoprogenitor cultures demonstrate direct FGF23 inhibition of differentiation and a separate DMP1-dependent mineralization defect. These models are useful for testing FGF23 blockade, DMP1 replacement, phosphate responsiveness, matrix biology, and osteocyte signaling. (courbon2023fgf23directlyinhibits pages 11-13, courbon2023fgf23directlyinhibits pages 4-5, courbon2023fgf23directlyinhibits pages 13-15)

Limitations include species-specific skeletal growth, experimental complete knockout rather than the allelic diversity of patients, short observation relative to decades of human disease, and inability to reproduce fully the human burden of dental disease, enthesopathy, orthopedic surgery, pain, and quality of life.

## Recent developments and authoritative interpretation

The principal 2023 advance was mechanistic: Courbon and colleagues showed that FGF23 has direct adverse effects on osteoprogenitor differentiation, while DMP1 loss independently compromises mineralization. Their abstract reports that osteocyte-specific Fgf23 deletion **“fully restore[d] serum Pi levels but only partially corrected the bone phenotype,”** supporting a two-component disease model rather than a purely endocrine phosphate-deficiency model. (courbon2023fgf23directlyinhibits pages 1-2)

The principal 2024 clinical message is diagnostic and implementation-focused. Real-world cases showed progressive disease despite conventional phosphate and active-vitamin-D treatment and demonstrated that narrow genetic testing may miss DMP1 variants. Comprehensive panels or WES/WGS can prevent prolonged misclassification and support mechanism-specific treatment and counseling. Burosumab remains promising but off-label for ARHR1, with evidence far weaker than in XLH. (chaturvedi2024lessonslearnedfrom pages 7-8, chaturvedi2024lessonslearnedfrom pages 6-7)

## Evidence limitations

ARHR1 is exceptionally rare. Most human evidence comes from individual families, retrospective cases, and selected sequencing cohorts; consequently, phenotype percentages, penetrance estimates, prevalence, incidence, sex ratios, survival, quality-of-life scores, treatment-response rates, and variant-specific population frequencies cannot currently be stated reliably. The strongest mechanistic evidence is from engineered mice and cultured cells and should be labeled preclinical. PMID values were not consistently present in the retrieved records; DOI URLs and publication dates are therefore supplied rather than inventing PMIDs.

### Key dated sources and URLs

* Lorenz-Depiereux et al., *Nature Genetics*, October 2006, discovery genetics: https://doi.org/10.1038/ng1868.
* Mäkitie et al., *Journal of Bone and Mineral Research*, April 2010, long-term human family: https://doi.org/10.1002/jbmr.105. (makitie2010longtermclinicaloutcome pages 1-2)
* Ichikawa et al., *Endocrinology*, March 2017, phosphate responsiveness in Dmp1-mutant mice: https://doi.org/10.1210/en.2016-1642. (ichikawa2017amutationin pages 1-1)
* Gu et al., June 2018, targeted sequencing and p.Glu244Ter case: https://doi.org/10.3892/ijmm.2018.3730. (gu2018targetedresequencingof pages 6-7)
* Courbon et al., *JCI Insight*, December 2023, direct FGF23 and DMP1-independent skeletal mechanisms: https://doi.org/10.1172/jci.insight.156850. (courbon2023fgf23directlyinhibits pages 1-2)
* Chaturvedi et al., *Bone Reports*, June 2024, real-world diagnosis and management: https://doi.org/10.1016/j.bonr.2024.101753. (chaturvedi2024lessonslearnedfrom pages 7-8)
* Baroncelli et al., *Frontiers in Endocrinology*, April 2024, rickets diagnostic/management position statement: https://doi.org/10.3389/fendo.2024.1383681.

References

1. (makitie2010longtermclinicaloutcome pages 1-2): Outi Mäkitie, Renata C Pereira, Ilkka Kaitila, Serap Turan, Murat Bastepe, Tero Laine, Heikki Kröger, William G Cole, and Harald Jüppner. Long-term clinical outcome and carrier phenotype in autosomal recessive hypophosphatemia caused by a novel <i>dmp1</i> mutation. Journal of Bone and Mineral Research, 25(10):2165-2174, Apr 2010. URL: https://doi.org/10.1002/jbmr.105, doi:10.1002/jbmr.105. This article has 72 citations and is from a highest quality peer-reviewed journal.

2. (courbon2023fgf23directlyinhibits pages 1-2): Guillaume Courbon, Dominik Kentrup, Jane Joy Thomas, Xueyan Wang, Hao-Hsuan Tsai, Jadeah Spindler, John Von Drasek, Laura Mazudie Ndjonko, Marta Martinez-Calle, Sana Lynch, Lauriane Hivert, Xiaofang Wang, Wenhan Chang, Jian Q. Feng, Valentin David, and Aline Martin. Fgf23 directly inhibits osteoprogenitor differentiation in dmp1-knockout mice. Dec 2023. URL: https://doi.org/10.1172/jci.insight.156850, doi:10.1172/jci.insight.156850. This article has 23 citations and is from a domain leading peer-reviewed journal.

3. (makitie2010longtermclinicaloutcome pages 2-4): Outi Mäkitie, Renata C Pereira, Ilkka Kaitila, Serap Turan, Murat Bastepe, Tero Laine, Heikki Kröger, William G Cole, and Harald Jüppner. Long-term clinical outcome and carrier phenotype in autosomal recessive hypophosphatemia caused by a novel <i>dmp1</i> mutation. Journal of Bone and Mineral Research, 25(10):2165-2174, Apr 2010. URL: https://doi.org/10.1002/jbmr.105, doi:10.1002/jbmr.105. This article has 72 citations and is from a highest quality peer-reviewed journal.

4. (gu2018targetedresequencingof pages 6-7): Jiemei Gu, Chun Wang, Hao Zhang, Hua Yue, Weiwei Hu, Jinwei He, Wenzhen Fu, and Zhenlin Zhang. Targeted resequencing of phosphorus metabolism‑related genes in 86 patients with hypophosphatemic rickets/osteomalacia. Jun 2018. URL: https://doi.org/10.3892/ijmm.2018.3730, doi:10.3892/ijmm.2018.3730. This article has 9 citations and is from a peer-reviewed journal.

5. (clinkenbeard2017heritableandacquired pages 4-6): Erica L. Clinkenbeard and Kenneth E. White. Heritable and acquired disorders of phosphate metabolism: etiologies involving fgf23 and current therapeutics. Bone, 102:31-39, Sep 2017. URL: https://doi.org/10.1016/j.bone.2017.01.034, doi:10.1016/j.bone.2017.01.034. This article has 37 citations and is from a domain leading peer-reviewed journal.

6. (nakanishi2022pathogenesisoffgf23related pages 7-8): Tatsuro Nakanishi and Toshimi Michigami. Pathogenesis of fgf23-related hypophosphatemic diseases including x-linked hypophosphatemia. Endocrines, 3:303-316, Jun 2022. URL: https://doi.org/10.3390/endocrines3020025, doi:10.3390/endocrines3020025. This article has 10 citations.

7. (yamazaki2022osteocytesandthe pages 3-5): Miwa Yamazaki and Toshimi Michigami. Osteocytes and the pathogenesis of hypophosphatemic rickets. Frontiers in Endocrinology, Sep 2022. URL: https://doi.org/10.3389/fendo.2022.1005189, doi:10.3389/fendo.2022.1005189. This article has 32 citations.

8. (chaturvedi2024lessonslearnedfrom pages 6-7): Deepti Chaturvedi, Taif EmadEldin Mehasi, Assia Benbrahim, Lubna ElDeeb, and Asma Deeb. Lessons learned from the real-world diagnosis and management of hereditary hypophosphatemic rickets. Jun 2024. URL: https://doi.org/10.1016/j.bonr.2024.101753, doi:10.1016/j.bonr.2024.101753. This article has 3 citations and is from a peer-reviewed journal.

9. (chaturvedi2024lessonslearnedfrom pages 7-8): Deepti Chaturvedi, Taif EmadEldin Mehasi, Assia Benbrahim, Lubna ElDeeb, and Asma Deeb. Lessons learned from the real-world diagnosis and management of hereditary hypophosphatemic rickets. Jun 2024. URL: https://doi.org/10.1016/j.bonr.2024.101753, doi:10.1016/j.bonr.2024.101753. This article has 3 citations and is from a peer-reviewed journal.

10. (chaturvedi2024lessonslearnedfrom pages 1-2): Deepti Chaturvedi, Taif EmadEldin Mehasi, Assia Benbrahim, Lubna ElDeeb, and Asma Deeb. Lessons learned from the real-world diagnosis and management of hereditary hypophosphatemic rickets. Jun 2024. URL: https://doi.org/10.1016/j.bonr.2024.101753, doi:10.1016/j.bonr.2024.101753. This article has 3 citations and is from a peer-reviewed journal.

11. (makitie2010longtermclinicaloutcome pages 7-9): Outi Mäkitie, Renata C Pereira, Ilkka Kaitila, Serap Turan, Murat Bastepe, Tero Laine, Heikki Kröger, William G Cole, and Harald Jüppner. Long-term clinical outcome and carrier phenotype in autosomal recessive hypophosphatemia caused by a novel <i>dmp1</i> mutation. Journal of Bone and Mineral Research, 25(10):2165-2174, Apr 2010. URL: https://doi.org/10.1002/jbmr.105, doi:10.1002/jbmr.105. This article has 72 citations and is from a highest quality peer-reviewed journal.

12. (haffner2022ricketsguidanceparta pages 1-2): Dieter Haffner, Maren Leifheit-Nestler, Andrea Grund, and Dirk Schnabel. Rickets guidance: part ii—management. Pediatric Nephrology (Berlin, Germany), 37:2289-2302, Mar 2022. URL: https://doi.org/10.1007/s00467-022-05505-5, doi:10.1007/s00467-022-05505-5. This article has 65 citations.

13. (courbon2023fgf23directlyinhibits pages 11-13): Guillaume Courbon, Dominik Kentrup, Jane Joy Thomas, Xueyan Wang, Hao-Hsuan Tsai, Jadeah Spindler, John Von Drasek, Laura Mazudie Ndjonko, Marta Martinez-Calle, Sana Lynch, Lauriane Hivert, Xiaofang Wang, Wenhan Chang, Jian Q. Feng, Valentin David, and Aline Martin. Fgf23 directly inhibits osteoprogenitor differentiation in dmp1-knockout mice. Dec 2023. URL: https://doi.org/10.1172/jci.insight.156850, doi:10.1172/jci.insight.156850. This article has 23 citations and is from a domain leading peer-reviewed journal.

14. (courbon2023fgf23directlyinhibits pages 4-5): Guillaume Courbon, Dominik Kentrup, Jane Joy Thomas, Xueyan Wang, Hao-Hsuan Tsai, Jadeah Spindler, John Von Drasek, Laura Mazudie Ndjonko, Marta Martinez-Calle, Sana Lynch, Lauriane Hivert, Xiaofang Wang, Wenhan Chang, Jian Q. Feng, Valentin David, and Aline Martin. Fgf23 directly inhibits osteoprogenitor differentiation in dmp1-knockout mice. Dec 2023. URL: https://doi.org/10.1172/jci.insight.156850, doi:10.1172/jci.insight.156850. This article has 23 citations and is from a domain leading peer-reviewed journal.

15. (makitie2010longtermclinicaloutcome pages 5-7): Outi Mäkitie, Renata C Pereira, Ilkka Kaitila, Serap Turan, Murat Bastepe, Tero Laine, Heikki Kröger, William G Cole, and Harald Jüppner. Long-term clinical outcome and carrier phenotype in autosomal recessive hypophosphatemia caused by a novel <i>dmp1</i> mutation. Journal of Bone and Mineral Research, 25(10):2165-2174, Apr 2010. URL: https://doi.org/10.1002/jbmr.105, doi:10.1002/jbmr.105. This article has 72 citations and is from a highest quality peer-reviewed journal.

16. (courbon2023fgf23directlyinhibits pages 13-15): Guillaume Courbon, Dominik Kentrup, Jane Joy Thomas, Xueyan Wang, Hao-Hsuan Tsai, Jadeah Spindler, John Von Drasek, Laura Mazudie Ndjonko, Marta Martinez-Calle, Sana Lynch, Lauriane Hivert, Xiaofang Wang, Wenhan Chang, Jian Q. Feng, Valentin David, and Aline Martin. Fgf23 directly inhibits osteoprogenitor differentiation in dmp1-knockout mice. Dec 2023. URL: https://doi.org/10.1172/jci.insight.156850, doi:10.1172/jci.insight.156850. This article has 23 citations and is from a domain leading peer-reviewed journal.

17. (ichikawa2017amutationin pages 1-1): Shoji Ichikawa, Rita L. Gerard-O'Riley, Dena Acton, Amie K. McQueen, Isabel E. Strobel, Phillip C. Witcher, Jian Q. Feng, and Michael J. Econs. A mutation in the dmp1 gene alters phosphate responsiveness in mice. Endocrinology, 158:470–476, Mar 2017. URL: https://doi.org/10.1210/en.2016-1642, doi:10.1210/en.2016-1642. This article has 38 citations and is from a domain leading peer-reviewed journal.

18. (makitie2010longtermclinicaloutcome pages 9-10): Outi Mäkitie, Renata C Pereira, Ilkka Kaitila, Serap Turan, Murat Bastepe, Tero Laine, Heikki Kröger, William G Cole, and Harald Jüppner. Long-term clinical outcome and carrier phenotype in autosomal recessive hypophosphatemia caused by a novel <i>dmp1</i> mutation. Journal of Bone and Mineral Research, 25(10):2165-2174, Apr 2010. URL: https://doi.org/10.1002/jbmr.105, doi:10.1002/jbmr.105. This article has 72 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Hypophosphatemic_Rickets_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.

44 of 46 terms resolved to a current term; the rest could not be looked up either way.