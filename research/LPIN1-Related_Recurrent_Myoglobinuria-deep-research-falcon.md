---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T19:02:23.357329'
end_time: '2026-09-05T19:11:04.818160'
duration_seconds: 521.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: LPIN1-Related Recurrent Myoglobinuria
  mondo_id: MONDO:0010791
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 11
  verified: 11
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0010791
    reported_labels:
    - if available
    ontology_label: myoglobinuria, recurrent
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: LPIN1-Related_Recurrent_Myoglobinuria-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** LPIN1-Related Recurrent Myoglobinuria
- **MONDO ID:** MONDO:0010791 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **LPIN1-Related Recurrent Myoglobinuria** covering all of the
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
- **Disease Name:** LPIN1-Related Recurrent Myoglobinuria
- **MONDO ID:** MONDO:0010791 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **LPIN1-Related Recurrent Myoglobinuria** covering all of the
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


# LPIN1-Related Recurrent Myoglobinuria: Disease-Characteristics Report

## Executive summary

LPIN1-related recurrent myoglobinuria is a rare, usually childhood-onset metabolic myopathy caused by **biallelic loss-of-function variants in LPIN1**. Its defining manifestation is episodic, potentially catastrophic rhabdomyolysis—typically precipitated by fever, infection, fasting, strenuous exercise, or another catabolic stress—with myalgia, weakness, dark urine/myoglobinuria, and extremely high serum creatine kinase (CK). Patients are often clinically well between attacks. Historical series reported substantial acute mortality, but contemporary prevalence, incidence, long-term survival, and validated quality-of-life data are unavailable. Current care is preventive and supportive; neither corticosteroids nor hydroxychloroquine has been established by randomized trials. Mechanistic work implicates disrupted phosphatidic-acid metabolism, abnormal membrane lipids, defective autophagy/mitophagy, mitochondrial and sarcoplasmic-reticulum stress, and amplification by inflammatory signals. (michot2012studyoflpin1 pages 1-2, tong2021acuterecurrentrhabdomyolysis pages 7-8, michot2010lpin1genemutations pages 5-7, hamel2021compromisedmitochondrialquality pages 25-26)

The following table provides a compact evidence-calibrated overview.

| Knowledge-base field | Evidence-based summary | Evidence level |
|---|---|---|
| Disease identity | Rare inherited metabolic myopathy characterized by acute, often recurrent skeletal-muscle breakdown with myoglobinuria; commonly termed **LPIN1-related recurrent rhabdomyolysis**, **lipin-1 deficiency**, or **LPIN1-related recurrent acute myoglobinuria**. (michot2012studyoflpin1 pages 1-2, michot2010lpin1genemutations pages 5-7) | Aggregated human cohorts |
| Inheritance | Classically **autosomal recessive**, caused by biallelic loss-of-function LPIN1 variants. Parents are generally asymptomatic heterozygotes, although cramps or myalgia have occasionally been reported in carriers; isolated heterozygous adult cases remain insufficient to establish a dominant disorder. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5, michot2010lpin1genemutations pages 5-7) | Human cohorts; isolated case reports |
| Typical onset and course | Usually begins before age 6; one foundational cohort reported median onset at **21 months**. Patients are often clinically normal between attacks, with normal or near-normal baseline CK, although adolescent- and adult-onset disease occurs rarely. (michot2012studyoflpin1 pages 1-2, michot2010lpin1genemutations pages 5-7) | Human cohorts |
| Principal triggers | Febrile illness and infection are most common; fasting, prolonged or strenuous exercise, anesthesia, and other catabolic stressors also precipitate attacks. These exposures trigger episodes rather than cause the underlying genetic disease. (abdallah2025lpin1genevariant pages 1-2, michot2010lpin1genemutations pages 5-7) | Human cohorts and case series |
| Hallmark phenotypes and laboratory findings | Acute myalgia, weakness, muscle tenderness, fatigue, hypotonia, dark/cola- or rose-colored urine, myoglobinuria, and extreme CK elevation. Peak CK is commonly **>10,000 U/L** and may exceed **100,000 U/L**; one three-child series reported mean episode CK **147,660.7 ± 28,144.5 U/L** versus baseline **438.0 ± 215.9 U/L**, with marked AST elevation. Between episodes, examination, EMG, MRI, and CK can be normal. (abdallah2025lpin1genevariant pages 1-2, tong2021acuterecurrentrhabdomyolysis pages 7-8, michot2012studyoflpin1 pages 6-8) | Human cohorts and case series |
| Major complications and mortality | Hyperkalemia and other electrolyte disturbances, circulatory collapse, arrhythmia/cardiac arrest, acute kidney injury from myoglobin-associated tubular injury, and multiorgan failure may occur. Published historical series reported **11/35 affected patients** dying during attacks; another report cited mortality up to **14%**, but modern population-level survival estimates are unavailable. (tong2021acuterecurrentrhabdomyolysis pages 7-8, michot2012studyoflpin1 pages 8-10) | Historical human cohorts/reviewed cases |
| Gene/protein mechanism | LPIN1 encodes lipin-1, a phosphatidate phosphatase that converts phosphatidic acid to diacylglycerol and also acts as a transcriptional coregulator. Loss of phosphatidate-phosphatase activity disrupts glycerolipid and membrane-lipid homeostasis, promotes phosphatidic-acid accumulation, abnormal lipid droplets, defective autophagy/mitophagy, mitochondrial dysfunction, and sarcoplasmic-reticulum stress; inflammatory cytokines may amplify this constitutive metabolic vulnerability during infection. (tong2021acuterecurrentrhabdomyolysis pages 9-9, hamel2021compromisedmitochondrialquality pages 25-26, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6, michot2010lpin1genemutations pages 5-7) | Human cells; yeast functional assays; mouse models |
| Diagnosis | Suspect in severe or recurrent early-childhood rhabdomyolysis, particularly when attacks are infection/fasting-associated and CK normalizes between episodes. Confirm with sequencing plus deletion/duplication analysis of LPIN1 or a rhabdomyolysis/metabolic-myopathy panel; WES/WGS may be used when panel testing is unrevealing. RNA analysis can identify large deletions missed by routine DNA sequencing. Biochemical testing helps exclude fatty-acid oxidation disorders, glycogenoses, mitochondrial disease, RYR1-related susceptibility, TANGO2-related disease, and phosphoglycerate-kinase deficiency. (tong2021acuterecurrentrhabdomyolysis pages 7-8, bareja2025adultonsetepisodicrhabdomyolysis pages 3-5, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6) | Human diagnostic cohorts and case reports |
| Acute management | Medical emergency management is supportive: stop exertion, reverse fasting/catabolism, provide prompt carbohydrate/nutritional support and intravenous fluids, closely monitor urine output, CK, renal function, glucose, electrolytes, acid–base status, and ECG, and treat hyperkalemia, arrhythmia, shock, or acute kidney injury; renal-replacement therapy is reserved for standard indications. No disease-specific regimen has been validated in randomized trials. (abdallah2025lpin1genevariant pages 1-2, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6) | Case series; general rhabdomyolysis practice |
| Prevention | Maintain hydration and regular carbohydrate intake during illness, avoid prolonged fasting and unaccustomed strenuous exercise, and use an individualized emergency letter/sick-day plan for early hospital assessment and anti-catabolic treatment. Cascade testing and genetic counseling permit identification of affected siblings and reproductive-risk assessment. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6) | Expert recommendations and case-based evidence |
| Experimental therapies and trials | Systemic corticosteroids have been evaluated retrospectively for acute episodes, but available evidence is nonrandomized and does not establish universal dosing or efficacy. Hydroxychloroquine was used compassionately in eight genetically confirmed pediatric patients with planned assessment of attacks, pain, and arrhythmias; registry **NCT04007562** was subsequently withdrawn with enrollment recorded as zero, so efficacy remains unproven. Chemical chaperones and fatty-acid-oxidation activation improved disease features only in mice. (hamel2021compromisedmitochondrialquality pages 26-26, NCT04007562 chunk 2, tarr2025emergencymanagementof pages 13-13, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6) | Retrospective human evidence; trial registry; mouse experiments |
| Models | LPIN1-deficient human myoblasts model starvation responses, autophagic flux, mitophagy, mitochondrial ROS and inflammatory signaling. Muscle-specific Lpin1-deficient mice develop lipid accumulation, chronic necrosis/regeneration, abnormal mitochondria, stress-sensitive CK release, and chaperone-responsive myopathy. Zebrafish lpin1 loss disrupts motor-neuron projections, myelination, and neuromuscular junctions; partial rescue by Notch inhibitor DAPT supports a developmental Notch contribution, although this atypical neurologic phenotype is not the canonical recurrent-myoglobinuria presentation. (hamel2021compromisedmitochondrialquality pages 25-26, lu2021lipin1deficiency pages 16-17, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6) | Human cells; mouse; zebrafish |


*Table: Compact evidence-calibrated summary of LPIN1-related recurrent myoglobinuria, spanning clinical presentation, mechanism, diagnosis, management, investigational therapies, and experimental models.*

## 1. Disease information

### Definition and nomenclature

The disorder is an inherited metabolic myopathy in which LPIN1 deficiency predisposes skeletal muscle to acute necrosis and release of CK, myoglobin, potassium, phosphate, purines, and other intracellular constituents. “Myoglobinuria” describes urinary myoglobin and dark urine; “rhabdomyolysis” describes the underlying skeletal-muscle destruction. The latter is therefore the more complete clinical name.

Common names include:

- **LPIN1-related recurrent myoglobinuria**
- **LPIN1-related recurrent rhabdomyolysis**
- **Lipin-1 deficiency**
- **Recurrent acute myoglobinuria, autosomal recessive**
- **Acute recurrent myoglobinuria of childhood**

Key identifiers are **MONDO:0010791** and **OMIM #268200**. The gene is **LPIN1**. No disease-specific ICD-10-CM code is established; coding generally uses rhabdomyolysis (M62.82) plus an appropriate genetic/metabolic diagnosis. Likewise, MeSH indexes the manifestations and molecular entity rather than providing a uniquely specific disease heading. Orphanet and ICD-11 identifiers should be locally verified before database ingestion because nomenclature mappings can change.

This report primarily aggregates disease-level resources, published cohorts, case series, case reports, trial-registry records, and experimental studies. It is **not derived from an individual EHR**. Some quantitative observations nevertheless originate from individual patients or small cohorts and are labeled accordingly.

The foundational publications include Zeharia et al. (2008/2009), *American Journal of Human Genetics*, “Mutations in LPIN1 Cause Recurrent Acute Myoglobinuria in Childhood,” DOI: https://doi.org/10.1016/j.ajhg.2008.12.003; Michot et al. (2010), *Human Mutation*, DOI: https://doi.org/10.1002/humu.21282; and Michot et al. (2012), *Journal of Inherited Metabolic Disease*, DOI: https://doi.org/10.1007/s10545-012-9461-6. (michot2012studyoflpin1 pages 1-2, michot2010lpin1genemutations pages 5-7)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The canonical disease is caused by **germline biallelic pathogenic LPIN1 variants** and follows autosomal-recessive inheritance. Most established alleles abolish or markedly reduce lipin-1 phosphatidate-phosphatase function. A yeast complementation experiment showed that a recurrent deletion construct did not rescue the relevant metabolic defect, directly supporting loss of function. (michot2010lpin1genemutations pages 5-7)

### Genetic risk factors

Severe disease is associated especially with two null or severe hypomorphic alleles—nonsense, frameshift, splice-altering, exon-level deletion, or damaging missense/in-frame variants. A recurrent approximately 1.76-kb deletion, reported as **c.2295-866_2410-30del; p.Glu766_Ser838del** and affecting exons 18–19/C-LIP-region sequence, occurred in 8/17 Caucasian patients in one foundational series. Shared breakpoints and haplotype supported a founder event. (michot2010lpin1genemutations pages 5-7)

Occasional cramps or myalgia have been reported among heterozygous relatives, and at least 40% of heterozygous relatives in one study had myalgia. Rare reports also describe adult rhabdomyolysis with a single detected allele. These findings may indicate mild carrier susceptibility, an undetected second variant, or coincidental disease; they do **not** yet establish routine dominant inheritance or high carrier penetrance. (michot2012studyoflpin1 pages 1-2, bareja2025adultonsetepisodicrhabdomyolysis pages 3-5)

No reproducible modifier gene, protective allele, polygenic score, or disease-specific epigenetic modifier has been validated. Large chromosomal abnormalities are not the usual mechanism, although copy-number variants and unusual mechanisms such as uniparental isodisomy are possible.

### Environmental and lifestyle triggers

Fever and infection are the best documented triggers. Fasting, calorie deprivation, strenuous or prolonged exercise, and anesthesia are also reported. A Chinese case linked prolonged weight training plus calorie deprivation to attacks. These factors precipitate episodes in genetically susceptible muscle; they do not cause the inherited disorder. (abdallah2025lpin1genevariant pages 1-2, tong2021acuterecurrentrhabdomyolysis pages 7-8, michot2010lpin1genemutations pages 5-7)

Possible medication associations are anecdotal. One adult reported temporal relationships with theophylline, mefenamic acid, co-trimoxazole, and combined oral contraceptives, but the authors found no convincing causal evidence. Statins warrant caution in susceptible patients, but disease-specific risk estimates are unavailable. (michot2012studyoflpin1 pages 6-8)

### Protective factors

No proven genetic protective factor exists. Practical environmental protection consists of avoiding prolonged fasting and unaccustomed exhaustive exercise, maintaining hydration and carbohydrate intake during illness, treating fever/infection promptly, and implementing an individualized emergency regimen before catabolism and CK escalation become severe. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6)

## 3. Phenotypes

The canonical course is **episodic**, not steadily progressive. Typical onset is infancy or early childhood, generally before age six; one series reported a median of 21 months. Rare adolescent and adult presentations—including onset at 42 years—have occurred. (michot2012studyoflpin1 pages 1-2, michot2010lpin1genemutations pages 5-7)

Suggested phenotype annotations include:

- **Recurrent rhabdomyolysis** — acute, severe, episodic; core phenotype. Suggested HPO: *Rhabdomyolysis* (HP:0003201), *Recurrent rhabdomyolysis* where supported by the current HPO release.
- **Myoglobinuria/dark urine** — rose, red-brown, or cola-colored urine during attacks. HPO: *Myoglobinuria* (HP:0002913).
- **Marked hyperCKemia** — frequently >10,000 U/L and often >100,000 U/L. In a 2025 three-child Egyptian series, episode CK was 147,660.7 ± 28,144.5 U/L versus baseline 438.0 ± 215.9 U/L; AST was 2,034.2 ± 1,770.0 U/L versus baseline 110.66 ± 105.13 U/L. HPO: *Elevated circulating creatine kinase concentration* (HP:0003236). (abdallah2025lpin1genevariant pages 1-2, tong2021acuterecurrentrhabdomyolysis pages 7-8)
- **Myalgia and muscle tenderness** — acute and trigger-associated; exercise-induced myalgia can persist in adults. HPO: *Myalgia* (HP:0003326).
- **Acute muscle weakness, fatigue, hypotonia, and reduced reflexes** — variable and often reversible between episodes. Suggested HPO: *Muscle weakness* (HP:0001324), *Fatigue* (HP:0012378), *Muscular hypotonia* (HP:0001252), *Hyporeflexia* (HP:0001265). (abdallah2025lpin1genevariant pages 1-2)
- **Exercise intolerance** — variable, especially in later-onset or surviving adults. HPO: *Exercise intolerance* (HP:0003546).
- **Elevated transaminases** — AST can be extreme and primarily muscle-derived; this should not automatically be interpreted as primary hepatic disease.
- **Acute kidney injury** — secondary to pigment nephropathy, hypovolemia, acidemia, and tubular obstruction; not obligatory. HPO: *Acute kidney injury* (HP:0001919). (abdallah2025lpin1genevariant pages 1-2, tong2021acuterecurrentrhabdomyolysis pages 7-8)
- **Electrolyte disturbance, hyperuricemia, arrhythmia, circulatory failure, or cardiac arrest** — severe downstream complications rather than invariant primary features. (tong2021acuterecurrentrhabdomyolysis pages 7-8, NCT04007562 chunk 2)

Muscle examination, CK, electromyography, and calf MRI may be normal or nearly normal between episodes. Baseline mild hyperCKemia and exercise-related symptoms nevertheless occur in some patients. (tong2021acuterecurrentrhabdomyolysis pages 7-8, michot2010lpin1genemutations pages 5-7)

A muscle-biopsy survey found lipid-droplet accumulation in approximately three-quarters of examined biopsies. Other findings included type-I fiber predominance, type-II atrophy, occasional mitochondrial aggregates, weak cytochrome-c oxidase staining, or a nonspecific necrotizing/regenerating metabolic myopathy. A normal or nonspecific biopsy does not exclude disease. (michot2012studyoflpin1 pages 1-2, michot2012studyoflpin1 pages 6-8)

No LPIN1-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life study was identified. Expected burdens include recurrent emergency admission, exercise restriction, school/work interruption, fear of febrile illness, and potential intensive-care morbidity, but these have not been quantified with disease-specific instruments.

## 4. Genetic and molecular information

**Causal gene:** *LPIN1*, encoding lipin-1, on chromosome 2. Disease-causing variants are germline. Somatic mutation is not the recognized mechanism.

Pathogenic classes include nonsense and frameshift variants, splice variants, exon-level or intragenic deletions, and functionally damaging missense/in-frame alleles. In one early series, 12 of 13 coding-region mutations were nonsense/frameshift variants, with the remaining lesion an in-frame deletion affecting the C-LIP domain. (michot2010lpin1genemutations pages 5-7)

Reported examples include:

- Recurrent **p.Glu766_Ser838del** deletion: founder-associated loss of function.
- **c.1684G>T; p.Glu562Ter**: homozygous likely pathogenic null allele in an adult survivor.
- **p.Arg388Ter plus p.Arg810Cys**: compound heterozygosity in a Chinese child; the second was novel and computationally damaging.
- **c.1696G>C; p.Asp566His**: reported homozygously in severe childhood rhabdomyolysis, but the original report relied partly on prediction; current ClinVar/ACMG classification should be independently checked before clinical use.
- Novel or atypical missense/in-frame combinations require segregation, population-frequency, RNA, enzymatic, and functional evidence because not every rare LPIN1 variant is pathogenic. (tong2021acuterecurrentrhabdomyolysis pages 7-8, bareja2025adultonsetepisodicrhabdomyolysis pages 3-5)

Exact gnomAD frequencies and ClinVar classifications are transcript- and genome-build-dependent and should be populated by live variant-level queries. Established severe alleles are individually rare; aggregate carrier frequency and penetrance have not been robustly estimated.

No validated modifier gene or disease-specific methylation signature is known. No recurrent aneuploidy, translocation, or inversion defines the disorder.

## 5. Environmental information

No toxin, radiation, pollution, smoking exposure, alcohol exposure, occupational exposure, or infectious organism is independently causal. Viral and bacterial febrile illnesses act as nonspecific inflammatory/catabolic triggers. Exercise is beneficial in ordinary health but can precipitate attacks when unusually intense or combined with fasting. No pathogen-specific prophylaxis exists.

The gene–environment interaction is biologically plausible and experimentally supported: constitutive lipid-metabolic vulnerability in LPIN1-deficient myoblasts is exacerbated by inflammatory cytokines, while inflammatory inducers can repress LPIN1 expression. Thus infection likely combines increased energy demand, fasting/catabolism, fever, and cytokine signaling to cross the threshold for myofiber necrosis. (michot2010lpin1genemutations pages 5-7, michot2012studyoflpin1 pages 8-10)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic LPIN1 loss-of-function variants lead to** deficient lipin-1 protein or phosphatidate-phosphatase activity in skeletal myofibers.
2. **Reduced phosphatidate-phosphatase activity leads to** disturbed conversion of phosphatidic acid (PA) to diacylglycerol (DAG), abnormal glycerolipid/membrane-lipid composition, and lipid-droplet accumulation.
3. **Lipid disequilibrium leads to** altered fatty-acid synthesis, oxidation, elongation and desaturation, and perturbed PA/DAG-dependent signaling.
4. **These abnormalities lead to** defective autophagy and mitochondrial quality control, damaged-mitochondrial accumulation, impaired oxidative capacity, reactive-oxygen stress, and abnormal sarcoplasmic-reticulum–mitochondrial contacts.
5. **They also lead to** sarcoplasmic-reticulum stress and activation of SREBP1c/SREBP2 and FGF21 responses in mouse muscle; extrapolation of the complete branch to human attacks remains partly inferential.
6. **Fever, infection, fasting, or exhaustive exercise leads to** increased energy demand, catabolism, and inflammatory signaling in already vulnerable muscle.
7. **Inflammatory and metabolic stress leads to** failure of myofiber membrane/organelle homeostasis and acute myocyte necrosis.
8. **Myocyte necrosis leads to** release of CK, myoglobin, potassium, phosphate, purines, and transaminases, producing pain, weakness, hyperCKemia, and dark urine.
9. **Systemic release and volume depletion lead to** arrhythmia, circulatory collapse, pigment-associated acute kidney injury, and—during the most severe attacks—multiorgan failure or death.

Lipin-1 has two broad functions: a cytoplasmic phosphatidic-acid phosphatase role generating DAG and a nuclear transcriptional-coregulatory role affecting lipid/energy programs. The recurrent deletion’s failure to complement yeast *pah1* deficiency supports loss of biochemical function. (michot2012studyoflpin1 pages 1-2, michot2010lpin1genemutations pages 5-7)

Muscle-specific mouse models separate PAP deficiency from whole-body lipodystrophy. They show PA and DAG accumulation, chronic fiber necrosis/regeneration, abnormal mitochondria, impaired autophagy, and increased CK after exhaustive exercise while unfed. Chemical chaperone TUDCA and the PPAR agonist/FAO activator bezafibrate improved histology and strength in mice; these are mechanistic proofs of concept, not validated human treatments. (bareja2025adultonsetepisodicrhabdomyolysis pages 5-6)

Hamel et al. examined autophagic flux, mitophagy, mitochondrial membrane potential, ROS, respiration, mtDNA damage, calcium mobilization, and Toll-like-receptor signaling in patient-derived myoblasts. This supports a model in which defective mitochondrial disposal and inflammatory sensing participate in acute injury. Publication: August 2021, *Cell Reports Medicine* 2:100370; PMID **34467247**; DOI: https://doi.org/10.1016/j.xcrm.2021.100370. (NCT04007562 chunk 2, hamel2021compromisedmitochondrialquality pages 25-26)

An atypical adult neuromuscular LPIN1 phenotype and zebrafish work implicated excessive Notch signaling and AGRIN–LRP4–MuSK-related neuromuscular-junction abnormalities; DAPT partly rescued zebrafish defects. This branch is relevant to LPIN1 biology but should not be assumed to drive canonical childhood rhabdomyolysis. (lu2021lipin1deficiency pages 16-17)

Suggested GO terms include *phosphatidate phosphatase activity* (molecular function), *glycerolipid biosynthetic process*, *triglyceride biosynthetic process*, *fatty-acid oxidation*, *autophagy*, *mitophagy*, *mitochondrial organization*, *response to endoplasmic-reticulum stress*, *muscle-cell homeostasis*, and *necrotic cell death*. Suggested cell terms include skeletal-muscle fiber/myocyte and myoblast; kidney proximal-tubule epithelial cells are secondary targets of filtered myoglobin.

No disease-specific single-cell atlas, spatial-transcriptomic study, organoid model, validated circulating proteomic signature, or clinical multi-omics classifier was identified. Existing lipidomic, respiratory, and imaging assays are predominantly research tools.

## 7. Anatomical structures affected

The primary site is **skeletal muscle**, especially skeletal myofibers. Suggested anatomy terms are UBERON *skeletal muscle tissue* and *musculoskeletal system*; the phenotype is generally systemic rather than unilateral or anatomically focal. The sarcolemma, sarcoplasmic reticulum, mitochondria, autophagosome/lysosome system, lipid droplets, and nucleus/transcriptional machinery are relevant subcellular structures.

Secondary organs include:

- **Kidney**, especially proximal tubules, through myoglobin-associated pigment nephropathy and hemodynamic injury.
- **Heart/conduction system**, through hyperkalemia, metabolic disturbance, and possibly intrinsic stress susceptibility; arrhythmia is a critical acute complication.
- **Circulatory and respiratory systems**, during shock, respiratory muscle weakness, or multiorgan failure.

Suggested GO cellular components include mitochondrion, mitochondrial membrane, sarcoplasmic reticulum, endoplasmic-reticulum membrane, lipid droplet, autophagosome, lysosome, nuclear envelope, and sarcolemma.

## 8. Temporal development

The typical pattern is abrupt onset during a trigger, rapid CK escalation over hours to days, and recovery after supportive treatment. In early reports, onset was before age five with a median of 21 months and 1–10 attacks per patient. Other cohorts characterize onset before age six; rare cases begin in adolescence or adulthood. (michot2010lpin1genemutations pages 5-7, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6)

Between attacks there may be complete clinical remission and normal CK. The disorder remains lifelong because the genotype persists, but attack frequency is variable and may decline with age in some survivors. There is no validated staging system. Critical intervention windows are the first signs of febrile illness, reduced intake, muscle pain, weakness, or dark urine—before severe catabolism, electrolyte disturbance, and renal injury develop.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed carrier parents, each pregnancy conventionally has a 25% probability of an affected child, 50% probability of a heterozygous carrier, and 25% probability of inheriting neither familial allele. Penetrance of severe biallelic loss-of-function genotypes appears high but has not been measured population-wide; expressivity is variable in age at onset, triggers, number of attacks, and survival. Anticipation is not expected. Germline mosaicism has not emerged as a characteristic mechanism.

In one selected cohort of patients with onset before six years and CK >10,000 U/L, LPIN1 variants accounted for **46%**, demonstrating high diagnostic yield in that narrowly defined severe subgroup—not population prevalence. Another early series found biallelic mutations in 17/29 severely affected young patients. (michot2010lpin1genemutations pages 5-7, michot2012studyoflpin1 pages 6-8)

Population incidence and prevalence per 100,000, carrier frequency, and sex ratio are unknown. Reports span European, Middle Eastern, South Asian, East Asian, and African populations, arguing against geographic exclusivity. Founder enrichment of the recurrent exon 18–19 deletion was reported among Caucasian patients. Consanguinity increases the probability of homozygous rare alleles but is not required. (michot2012studyoflpin1 pages 1-2, michot2010lpin1genemutations pages 5-7)

## 10. Diagnostics

### Acute evaluation

Immediate tests should include CK, plasma/serum myoglobin if available, urinalysis with microscopy, creatinine, urea, electrolytes (especially potassium, calcium, phosphate and bicarbonate), glucose, venous/arterial acid–base assessment when severe, AST/ALT, urate, complete blood count, and ECG. A heme-positive urine dipstick with few or no erythrocytes supports myoglobinuria, but absence does not exclude rhabdomyolysis.

### Genetic confirmation

Preferred testing is an inherited-rhabdomyolysis/metabolic-myopathy panel containing **LPIN1** with sequence and deletion/duplication analysis. Single-gene testing is reasonable when the phenotype and familial alleles are clear. WES or WGS is appropriate for atypical or panel-negative disease, but laboratories must demonstrate reliable copy-number and difficult-region coverage. In a 2023 54-gene hyperCKemia panel cohort of 139 patients, definite diagnoses were obtained in 15.1%; importantly, RNA analysis identified a large LPIN1 deletion missed by DNA sequencing, illustrating the value of transcript studies when only one allele is found. DOI: https://doi.org/10.3390/genes14071393. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5)

CMA, karyotyping, FISH, mitochondrial-genome testing, and repeat-expansion analysis are not first-line LPIN1 tests unless broader clinical findings indicate them. Muscle RNA sequencing, enzymatic PAP assays, lipidomics, or patient-myoblast studies may resolve selected uncertain cases but are not routine diagnostics.

### Differential diagnosis

Important alternatives include fatty-acid oxidation disorders—especially CPT II deficiency—glycogenoses such as McArdle disease, mitochondrial myopathies, RYR1/CACNA1S-related exertional or malignant-hyperthermia susceptibility, TANGO2-related metabolic crises, FLAD1/ETFDH-related lipid-storage myopathy, dystrophinopathy, ANO5-related disease, phosphoglycerate-kinase deficiency, viral myositis, autoimmune myositis, trauma, seizures, heat injury, toxins, and drug-associated rhabdomyolysis. PGK deficiency is particularly relevant when hemolytic anemia and hyperbilirubinemia accompany myoglobinuria. (tong2021acuterecurrentrhabdomyolysis pages 7-8)

No universally adopted LPIN1-specific clinical diagnostic criteria exist. Molecular confirmation requires pathogenic/likely pathogenic variants in trans, with phenotype and segregation consistency.

### Screening

LPIN1 disease is not part of standard population newborn screening. Following diagnosis, cascade testing of siblings and relatives is important because a presymptomatic affected sibling may benefit from an emergency plan. Carrier testing, prenatal diagnosis, and preimplantation genetic testing are possible after familial variants are established.

## 11. Outcome and prognosis

Historical outcomes were severe: one combined series reported **11/35 affected patients and 10 unstudied siblings** dying during attacks; another early report documented five patient deaths plus three sibling deaths. A later review cited mortality up to 14%. These estimates come from selected historical cases and should not be interpreted as current population mortality. (tong2021acuterecurrentrhabdomyolysis pages 7-8, michot2010lpin1genemutations pages 5-7, michot2012studyoflpin1 pages 8-10)

Acute prognostic threats include very young age, delayed carbohydrate/fluid treatment, extreme CK rise, hyperkalemia, arrhythmia, shock, oliguria/AKI, and multiorgan involvement. Survivors can recover normal strength and CK between episodes, although some develop exercise intolerance, persistent myalgia, mild hyperCKemia, chronic weakness, or renal sequelae. No validated prognostic biomarker beyond attack severity and organ-injury measures exists. Five- and ten-year survival, life expectancy, disability-adjusted life-years, and treatment-stratified outcome rates are unavailable.

## 12. Treatment

### Acute strategy

An attack is a medical emergency. Management generally comprises:

1. Stop exertion and reverse fasting/catabolism with carbohydrate and nutritional support.
2. Give prompt isotonic intravenous fluid, individualized to age, cardiac status, urine output, and renal function.
3. Monitor CK trajectory, fluid balance, creatinine, potassium, calcium, phosphate, bicarbonate, glucose, urate, and ECG.
4. Treat hyperkalemia, arrhythmia, shock, acid–base disturbance, and hypoglycemia by standard emergency protocols.
5. Use dialysis/continuous renal-replacement therapy for conventional indications such as refractory hyperkalemia, acidosis, fluid overload, or severe renal failure—not merely for a high CK value.
6. Involve metabolic medicine, neurology, nephrology, intensive care, and cardiology as severity requires.

There is no approved LPIN1-specific drug, enzyme replacement, gene therapy, RNA therapy, cell therapy, or surgery. Suggested NCIT intervention concepts include intravenous fluid therapy, glucose administration, electrolyte replacement, cardiac monitoring, renal dialysis, nutritional support, and genetic counseling.

### Corticosteroids

A 2023 retrospective study evaluated systemic corticosteroids during acute LPIN1 attacks: Tuchmann-Durand et al., *Journal of Inherited Metabolic Disease* 46:649–661, DOI: https://doi.org/10.1002/jimd.12592. A separate 2023 report described dexamethasone use, DOI: https://doi.org/10.1016/j.ymgmr.2023.100961. These reports are clinically important recent developments, but the retrieved evidence did not provide a randomized comparator or universally validated dose. Steroids should therefore be considered center-specific/experimental rather than routine standard of care. (tarr2025emergencymanagementof pages 13-13)

### Hydroxychloroquine

Hydroxychloroquine was used compassionately in a small Paris cohort, motivated by mitochondrial-DNA/inflammatory signaling biology. Registry **NCT04007562** specified genetically confirmed pediatric LPIN1 deficiency, at least six months of treatment, and outcomes including attacks, pain, and arrhythmia over 36 months. The registry now records the study as withdrawn with zero enrollment, while the associated publication describes an eight-patient clinical experience; this discrepancy and the nonrandomized design preclude a firm efficacy conclusion. ECG/ophthalmologic and other standard hydroxychloroquine safety monitoring would be necessary if used experimentally. (hamel2021compromisedmitochondrialquality pages 26-26, NCT04007562 chunk 2)

### Preclinical approaches

TUDCA and bezafibrate improved muscle histology/strength in LPIN1-deficient mice. Notch inhibition rescued aspects of an atypical zebrafish neuromuscular phenotype. AAV-lipin-1 restoration has shown benefit in a Duchenne model, not LPIN1-deficient human disease. None is established therapy for recurrent myoglobinuria. (lu2021lipin1deficiency pages 16-17, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6)

No LPIN1-specific pharmacogenomic guideline, response rate, or comparative adverse-event dataset is available. Rehabilitation should be individualized after recovery, avoiding sudden exhaustive or fasting-state exercise.

## 13. Prevention

- **Primary prevention of genotype:** not possible after conception; reproductive options include carrier testing, genetic counseling, prenatal diagnosis, and preimplantation genetic testing.
- **Secondary prevention:** molecular diagnosis and cascade screening before a first catastrophic episode; no population or newborn screening program is established.
- **Tertiary prevention:** emergency letter, sick-day carbohydrate/hydration plan, prompt evaluation during fever or poor intake, avoidance of prolonged fasting and unaccustomed exhaustive exercise, perioperative planning, and education about dark urine, muscle pain, weakness, and reduced urine output. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5, bareja2025adultonsetepisodicrhabdomyolysis pages 5-6)

Routine immunization is appropriate because preventing febrile infections may indirectly prevent attacks, but no LPIN1-specific vaccine exists. Vaccination itself should be managed with ordinary fever/hydration precautions rather than withheld without a separate contraindication.

## 14. Other species and natural disease

No well-established, naturally occurring veterinary LPIN1 recurrent-myoglobinuria syndrome with a validated breed association was identified. Consequently, no VBO breed term or zoonotic concern applies. The disorder is not infectious and has no cross-species transmission.

Orthologous *Lpin1/lpin1* genes are conserved in mouse and zebrafish, enabling mechanistic comparison. Whole-body *Lpin1*-deficient fatty-liver-dystrophy mice develop lipodystrophy not characteristic of affected humans, limiting direct phenotypic translation. Muscle-specific models better isolate the myopathy.

## 15. Model organisms

### Mouse

Muscle-specific deletion models remove PAP activity while retaining some transcriptional function or eliminate lipin-1 protein. They reproduce lipid accumulation, PA/DAG dysregulation, chronic fiber necrosis/regeneration, abnormal mitochondria, impaired autophagy, and stress-sensitive CK release. They do not perfectly reproduce the abrupt, infection-dominated human course and may exhibit chronic pathology absent between human attacks. (bareja2025adultonsetepisodicrhabdomyolysis pages 5-6)

### Human cellular models

Primary patient myoblasts/myotubes permit analysis of lipid metabolism, cytokine sensitivity, starvation-induced autophagic flux, CCCP-induced mitophagy, mitochondrial respiration, membrane potential, ROS, mtDNA injury, calcium signaling, and innate immune pathways. They provide the most disease-proximal mechanistic system but lack whole-body renal, cardiac, endocrine, and immune interactions. (hamel2021compromisedmitochondrialquality pages 25-26, michot2010lpin1genemutations pages 5-7)

### Zebrafish

Morpholino knockdown or mutant-mRNA expression produces myotome defects, reduced motor-neuron projections, myelination and neuromuscular-junction abnormalities, impaired touch responses, and altered swimming. Partial rescue by DAPT supports Notch involvement. These developmental neural phenotypes model an atypical LPIN1 presentation more than classic recurrent rhabdomyolysis. (lu2021lipin1deficiency pages 16-17)

No validated LPIN1 organoid, humanized large-animal model, or CRISPR-corrected clinical platform was identified.

## Recent developments and evidence gaps

Research published in 2023 emphasized two developments: NGS-based metabolic-myopathy diagnostics augmented by RNA analysis for cryptic LPIN1 deletions, and retrospective systemic-corticosteroid treatment of acute attacks. Neither changed the fundamental evidence hierarchy: diagnosis is increasingly genomic, while treatment remains largely supportive and preventive. Disease-specific 2024 primary clinical research was sparse; recent work involving lipin-1 in other muscular disorders should not be conflated with treatment evidence for LPIN1 deficiency. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5, tarr2025emergencymanagementof pages 13-13)

Major unresolved needs are a multinational natural-history registry; contemporary incidence and survival estimates; standardized attack definitions and core outcomes; prospective comparison of anti-catabolic protocols; controlled evaluation of corticosteroids and hydroxychloroquine; variant-specific functional assays; and clinically translatable strategies to restore PAP activity, mitochondrial quality control, or muscle LPIN1 expression.

## Selected exact abstract quotations

- Michot et al. (2012) concluded that LPIN1 myolysis is a major cause of severe early-onset rhabdomyolysis and documented adult disease; the study evaluated 171 symptomatic patients and found two LPIN1 mutations in 18. DOI: https://doi.org/10.1007/s10545-012-9461-6. (michot2012studyoflpin1 pages 1-2)
- Che et al. (2020): “**Lipin-1, encoded by LPIN1 gene, serves as an enzyme and a transcriptional co-regulator to regulate lipid metabolism and mitochondrial respiratory chain.**” DOI: https://doi.org/10.1186/s12887-020-02134-5.
- Rashid et al. (2019): “**Our data reveal that SR stress and alterations in SR–mitochondria contacts are contributing factors and potential intervention targets of the myopathy associated with lipin1 deficiency.**” DOI: https://doi.org/10.15252/embj.201899576. (bareja2025adultonsetepisodicrhabdomyolysis pages 5-6)
- Invernizzi et al. (2023): “**In one patient, mRNA analysis allowed identifying a large LPIN1 deletion missed by DNA sequencing, leading to a certain diagnosis.**” DOI: https://doi.org/10.3390/genes14071393. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5)

### Evidence-quality note

The strongest disease-specific evidence consists of retrospective cohorts, molecular case series, patient-derived-cell studies, and genetically engineered models. Frequencies from referral cohorts are subject to ascertainment bias; treatment reports are uncontrolled; adult heterozygous cases require caution; and several ontology and clinical-code mappings should be verified against the current release before production ingestion.

References

1. (michot2012studyoflpin1 pages 1-2): Caroline Michot, Laurence Hubert, Norma B. Romero, Amr Gouda, Asmaa Mamoune, Suja Mathew, Edwin Kirk, Louis Viollet, Shamima Rahman, Soumeya Bekri, Heidi Peters, James McGill, Emma Glamuzina, Michelle Farrar, Maya der von Hagen, Ian E. Alexander, Brian Kirmse, Magalie Barth, Pascal Laforet, Pascale Benlian, Arnold Munnich, Marc JeanPierre, Orly Elpeleg, Ophry Pines, Agnès Delahodde, Yves de Keyzer, and Pascale de Lonlay. Study of lpin1, lpin2 and lpin3 in rhabdomyolysis and exercise-induced myalgia. Journal of Inherited Metabolic Disease, 35:1119-1128, Apr 2012. URL: https://doi.org/10.1007/s10545-012-9461-6, doi:10.1007/s10545-012-9461-6. This article has 125 citations and is from a peer-reviewed journal.

2. (tong2021acuterecurrentrhabdomyolysis pages 7-8): Ke Tong and Geng-Sheng Yu. Acute recurrent rhabdomyolysis in a chinese boy associated with a novel compound heterozygous lpin1 variant: a case report. BMC Neurology, Jan 2021. URL: https://doi.org/10.1186/s12883-021-02050-w, doi:10.1186/s12883-021-02050-w. This article has 12 citations and is from a peer-reviewed journal.

3. (michot2010lpin1genemutations pages 5-7): Caroline Michot, Laurence Hubert, Michèle Brivet, Linda De Meirleir, Vassili Valayannopoulos, Wolfgang Müller-Felber, Ramesh Venkateswaran, Hélène Ogier, Isabelle Desguerre, Cécilia Altuzarra, Elizabeth Thompson, Martin Smitka, Angela Huebner, Marie Husson, Rita Horvath, Patrick Chinnery, Frederic M. Vaz, Arnold Munnich, Orly Elpeleg, Agnès Delahodde, Yves de Keyzer, and Pascale de Lonlay. Lpin1 gene mutations: a major cause of severe rhabdomyolysis in early childhood. Human Mutation, 31:E1564-E1573, Jul 2010. URL: https://doi.org/10.1002/humu.21282, doi:10.1002/humu.21282. This article has 175 citations and is from a domain leading peer-reviewed journal.

4. (hamel2021compromisedmitochondrialquality pages 25-26): Yamina Hamel, François-Xavier Mauvais, Marine Madrange, Perrine Renard, Corinne Lebreton, Ivan Nemazanyy, Olivier Pellé, Nicolas Goudin, Xiaoyun Tang, Mathieu P. Rodero, Caroline Tuchmann-Durand, Patrick Nusbaum, David N. Brindley, Peter van Endert, and Pascale de Lonlay. Compromised mitochondrial quality control triggers lipin1-related rhabdomyolysis. Cell Reports Medicine, 2:100370, Aug 2021. URL: https://doi.org/10.1016/j.xcrm.2021.100370, doi:10.1016/j.xcrm.2021.100370. This article has 23 citations and is from a peer-reviewed journal.

5. (bareja2025adultonsetepisodicrhabdomyolysis pages 3-5): Naman Bareja, Rafail A Chionatos, Camelia Valhuerdi Porto, Nikita Srinivasan, and Mehdi Ghasemi. Adult-onset episodic rhabdomyolysis in a patient with a heterozygous lipin 1 (lpin1) mutation: a case report. Cureus, Jan 2025. URL: https://doi.org/10.7759/cureus.76772, doi:10.7759/cureus.76772. This article has 4 citations.

6. (abdallah2025lpin1genevariant pages 1-2): Tarek M. A. Abdallah, Said S. El-Feky, Nourhan A. A. Salem, Ghada M. Mashaal, and Zaghloul E. Gouda. Lpin-1 gene variant in egyptian children: acute recurrent myoglobinuria. Jul 2025. URL: https://doi.org/10.1007/s44162-025-00106-w, doi:10.1007/s44162-025-00106-w. This article has 1 citations.

7. (michot2012studyoflpin1 pages 6-8): Caroline Michot, Laurence Hubert, Norma B. Romero, Amr Gouda, Asmaa Mamoune, Suja Mathew, Edwin Kirk, Louis Viollet, Shamima Rahman, Soumeya Bekri, Heidi Peters, James McGill, Emma Glamuzina, Michelle Farrar, Maya der von Hagen, Ian E. Alexander, Brian Kirmse, Magalie Barth, Pascal Laforet, Pascale Benlian, Arnold Munnich, Marc JeanPierre, Orly Elpeleg, Ophry Pines, Agnès Delahodde, Yves de Keyzer, and Pascale de Lonlay. Study of lpin1, lpin2 and lpin3 in rhabdomyolysis and exercise-induced myalgia. Journal of Inherited Metabolic Disease, 35:1119-1128, Apr 2012. URL: https://doi.org/10.1007/s10545-012-9461-6, doi:10.1007/s10545-012-9461-6. This article has 125 citations and is from a peer-reviewed journal.

8. (michot2012studyoflpin1 pages 8-10): Caroline Michot, Laurence Hubert, Norma B. Romero, Amr Gouda, Asmaa Mamoune, Suja Mathew, Edwin Kirk, Louis Viollet, Shamima Rahman, Soumeya Bekri, Heidi Peters, James McGill, Emma Glamuzina, Michelle Farrar, Maya der von Hagen, Ian E. Alexander, Brian Kirmse, Magalie Barth, Pascal Laforet, Pascale Benlian, Arnold Munnich, Marc JeanPierre, Orly Elpeleg, Ophry Pines, Agnès Delahodde, Yves de Keyzer, and Pascale de Lonlay. Study of lpin1, lpin2 and lpin3 in rhabdomyolysis and exercise-induced myalgia. Journal of Inherited Metabolic Disease, 35:1119-1128, Apr 2012. URL: https://doi.org/10.1007/s10545-012-9461-6, doi:10.1007/s10545-012-9461-6. This article has 125 citations and is from a peer-reviewed journal.

9. (tong2021acuterecurrentrhabdomyolysis pages 9-9): Ke Tong and Geng-Sheng Yu. Acute recurrent rhabdomyolysis in a chinese boy associated with a novel compound heterozygous lpin1 variant: a case report. BMC Neurology, Jan 2021. URL: https://doi.org/10.1186/s12883-021-02050-w, doi:10.1186/s12883-021-02050-w. This article has 12 citations and is from a peer-reviewed journal.

10. (bareja2025adultonsetepisodicrhabdomyolysis pages 5-6): Naman Bareja, Rafail A Chionatos, Camelia Valhuerdi Porto, Nikita Srinivasan, and Mehdi Ghasemi. Adult-onset episodic rhabdomyolysis in a patient with a heterozygous lipin 1 (lpin1) mutation: a case report. Cureus, Jan 2025. URL: https://doi.org/10.7759/cureus.76772, doi:10.7759/cureus.76772. This article has 4 citations.

11. (hamel2021compromisedmitochondrialquality pages 26-26): Yamina Hamel, François-Xavier Mauvais, Marine Madrange, Perrine Renard, Corinne Lebreton, Ivan Nemazanyy, Olivier Pellé, Nicolas Goudin, Xiaoyun Tang, Mathieu P. Rodero, Caroline Tuchmann-Durand, Patrick Nusbaum, David N. Brindley, Peter van Endert, and Pascale de Lonlay. Compromised mitochondrial quality control triggers lipin1-related rhabdomyolysis. Cell Reports Medicine, 2:100370, Aug 2021. URL: https://doi.org/10.1016/j.xcrm.2021.100370, doi:10.1016/j.xcrm.2021.100370. This article has 23 citations and is from a peer-reviewed journal.

12. (NCT04007562 chunk 2):  Acute Rhabdomyolysis and Muscle Pain Associated With Mutations in the LPIN1 Gene - A Retrospective Study Describing the Safety and Efficacy of Hydroxychloroquine Sulfate Given on a Compassionate Basis to Patients Suffering From Lipin-1 Deficiency. Assistance Publique - Hôpitaux de Paris. 2019. ClinicalTrials.gov Identifier: NCT04007562

13. (tarr2025emergencymanagementof pages 13-13): J. Dexter Tarr and Andrew A. M. Morris. Emergency management of intoxication‐type inherited metabolic disorders. Journal of Inherited Metabolic Disease, Feb 2025. URL: https://doi.org/10.1002/jimd.70007, doi:10.1002/jimd.70007. This article has 3 citations and is from a peer-reviewed journal.

14. (lu2021lipin1deficiency pages 16-17): Shuxian Lu, Zhaojie Lyu, Zhihao Wang, Yao Kou, Cong Liu, Shengyue Li, Mengyan Hu, Hongjie Zhu, Wenxing Wang, Ce Zhang, Yung-Shu Kuan, Yi-Wen Liu, Jianming Chen, and Jing Tian. Lipin 1 deficiency causes adult-onset myasthenia with motor neuron dysfunction in humans and neuromuscular junction defects in zebrafish. Theranostics, 11:2788-2805, Jan 2021. URL: https://doi.org/10.7150/thno.53330, doi:10.7150/thno.53330. This article has 26 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](LPIN1-Related_Recurrent_Myoglobinuria-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 11 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010791` (2 mentions) - the report calls it "if available"; MONDO calls it **myoglobinuria, recurrent**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003236` (1 mention) - the report calls it "Elevated circulating creatine kinase concentration"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated creatine kinase concentration" among its other names
- `HP:0001252` (1 mention) - the report calls it "Muscular hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names