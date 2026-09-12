---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T15:56:24.748105'
end_time: '2026-09-09T16:06:52.902756'
duration_seconds: 628.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Maleylacetoacetate Isomerase Deficiency
  mondo_id: MONDO:0060527
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 12
  verified: 10
  not_found: 0
  unverifiable: 2
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 15
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0060527
    reported_labels:
    - if available
    ontology_label: maleylacetoacetate isomerase deficiency
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Maleylacetoacetate_Isomerase_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Maleylacetoacetate Isomerase Deficiency
- **MONDO ID:** MONDO:0060527 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Maleylacetoacetate Isomerase Deficiency** covering all of the
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
- **Disease Name:** Maleylacetoacetate Isomerase Deficiency
- **MONDO ID:** MONDO:0060527 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Maleylacetoacetate Isomerase Deficiency** covering all of the
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


# Maleylacetoacetate Isomerase Deficiency: Comprehensive Disease Report

## Executive summary

Maleylacetoacetate isomerase deficiency (MAAID) is an ultra-rare autosomal-recessive disorder of phenylalanine/tyrosine degradation caused by biallelic loss-of-function variants in **GSTZ1**. It is usually detected incidentally by newborn screening (NBS) as mild or intermittent succinylacetone elevation. Unlike **FAH**-related hereditary tyrosinemia type I (HT1), currently documented MAAID is predominantly an asymptomatic biochemical trait: reported individuals generally have normal tyrosine, hepatic function, renal function, coagulation, growth, and neurodevelopment. Nevertheless, fewer than 20 individuals have been reported, so penetrance, lifetime prognosis, and responses to severe metabolic stress remain uncertain. The strongest recent developments are urinary maleic acid as a potential second-tier biomarker (2023) and a 2024 German NBS study documenting an untreated, clinically benign course in a homozygous adult through age 32. (gramer2024newcasesof pages 1-2, barretta2025variantsingstz1 pages 1-2, barretta2025variantsingstz1 pages 9-11)

| Domain | Best-supported finding | Evidence type | Certainty / gap |
|---|---|---|---|
| Identity | Maleylacetoacetate isomerase deficiency (MAAID; GSTZ1/MAAI deficiency), MONDO:0060527 and OMIM phenotype #617596, is caused by deficient glutathione S-transferase zeta 1/maleylacetoacetate isomerase encoded by **GSTZ1**. (OpenTargets Search: Maleylacetoacetate isomerase deficiency-GSTZ1, gramer2024newcasesof pages 2-4) | Curated disease–gene association; human molecular cases | High-confidence identity and gene association; no disease-specific ICD or MeSH identifier was established in the gathered evidence. |
| Inheritance | Biallelic **GSTZ1** variants cause autosomal-recessive MAAID. Homozygous and compound-heterozygous individuals have been reported; segregation was demonstrated in multiple families. (barretta2025variantsingstz1 pages 5-8, gramer2024newcasesof pages 2-4) | Human pedigrees and molecular testing | High confidence for autosomal-recessive inheritance; penetrance cannot be quantified and appears low for overt clinical disease. |
| Biochemical phenotype | Mild, persistent or intermittent elevation of succinylacetone is the principal finding, often with normal tyrosine, liver tests and coagulation. Quantitative urinary maleic acid is elevated in reported genetically confirmed cases and may distinguish MAAID from tyrosinemia type I. (gramer2024newcasesof pages 5-7, barretta2025variantsingstz1 pages 9-11) | Human newborn-screening and biomarker studies | Strong evidence for mild hypersuccinylacetonemia; maleic acid is promising but its assay, stability, reference intervals and dried-blood-spot implementation remain insufficiently standardized. |
| Clinical phenotype and natural history | Most molecularly confirmed individuals have been asymptomatic. Reported follow-up includes untreated children without liver or neurologic complications and an untreated homozygous adult clinically well at age 32; isolated microcephaly, short stature, obesity and mild hyperbilirubinemia have been reported without proof that they are disease-caused. (gramer2024newcasesof pages 4-5, barretta2025variantsingstz1 pages 1-2, barretta2025variantsingstz1 pages 8-9) | Small human case series and family follow-up | Evidence favors a benign or predominantly biochemical phenotype, but fewer than 20 individuals have been reported and long-term surveillance is sparse. |
| 2024 screening statistics | In Heidelberg, 516,803 newborns were screened during August 2016–December 2020. Among 42 elevated-succinylacetone screens, two had tyrosinemia type I, two were suspected of MAAID and one MAAID case was genetically confirmed; the index value was 2.61 µmol/L. (gramer2024newcasesof pages 1-2, gramer2024newcasesof pages 2-4) | Large regional newborn-screening cohort | Reliable center-level data, not a population prevalence estimate; ascertainment depends on assay and cutoff. |
| Diagnostics and differential | After elevated succinylacetone, confirm with repeat dried-blood-spot/plasma testing, urine organic acids or quantitative maleic acid, liver/coagulation studies, and molecular testing. Exclude **FAH**-related tyrosinemia type I first, then analyze **GSTZ1** by single-gene testing, a tyrosinemia panel, exome or genome sequencing. (barretta2025variantsingstz1 pages 2-4, gramer2024newcasesof pages 2-4, barretta2025variantsingstz1 pages 9-11) | Human diagnostic workflows | Molecular confirmation is decisive. Low succinylacetone cannot safely exclude mild tyrosinemia type I, so simply raising screening cutoffs risks missed cases. |
| Treatment | Most reported individuals received neither protein restriction nor medication and remained well. Nitisinone and tyrosine/phenylalanine restriction initiated while tyrosinemia type I was unresolved were discontinued after MAAID diagnosis without deterioration. (barretta2025variantsingstz1 pages 5-8, barretta2025variantsingstz1 pages 8-9) | Case reports and observational follow-up | Current evidence argues against routine disease-specific treatment, but there are no controlled trials or formal guidelines; surveillance and individualized intervention if liver dysfunction appears are prudent. |
| Mechanism | GSTZ1/MAAI normally catalyzes glutathione-dependent isomerization of maleylacetoacetate to fumarylacetoacetate in phenylalanine/tyrosine catabolism. Loss of activity permits upstream metabolites and succinylacetone to accumulate; a glutathione-dependent nonenzymatic bypass can still generate fumarylacetoacetate and probably explains the mild baseline phenotype. (fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1, board2011glutathionetransferasezeta pages 7-8) | Enzyme biochemistry, in vitro experiments and knockout mice | Core enzymatic defect and bypass are well supported experimentally; their quantitative contribution in affected humans has not been directly measured. |
| Mouse model | **Gstz1**-null mice excrete fumarylacetoacetate and succinylacetone and can appear relatively healthy on standard chow, but some backgrounds show enlarged liver/kidneys, hepatitis, renal abnormalities, splenic atrophy and antioxidant-response induction. Phenylalanine, tyrosine/homogentisate challenge or glutathione depletion causes severe hepatic/renal injury and age-dependent lethality. (lim2004micedeficientin pages 1-2, board2011glutathionetransferasezeta pages 8-9, fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 7-8) | Germline knockout mouse studies | Strong evidence for conditional metabolic toxicity; severe challenged-mouse phenotypes have not been observed in the small human cohort and must not be directly extrapolated. |
| Major evidence gaps | No robust incidence or prevalence, carrier frequency, penetrance estimate, genotype–phenotype model, validated clinical criteria, disease-specific quality-of-life data, controlled treatment study, clinical trial, gene therapy, human tissue omics, single-cell/spatial study or proven congenital-MAAID cancer risk is available. Cancer studies of acquired GSTZ1 downregulation are mechanistically informative but not direct evidence for the inherited disorder. (barretta2025variantsingstz1 pages 1-2, barretta2025variantsingstz1 pages 11-12) | Evidence-gap assessment across retrieved literature | Very substantial uncertainty due to ultra-rarity, screening ascertainment, predominantly asymptomatic cases and limited longitudinal follow-up. |


*Table: Compact evidence map for GSTZ1-related maleylacetoacetate isomerase deficiency, integrating human screening and natural-history data with mechanistic and mouse-model findings. The final column highlights where evidence is strong and where ultra-rarity limits inference.*

## 1. Disease information

### Definition and identifiers

MAAID is an inborn error of metabolism in which deficient GSTZ1/MAAI activity impairs the glutathione-dependent conversion of maleylacetoacetate to fumarylacetoacetate, the penultimate reaction in tyrosine degradation. Its principal observed human phenotype is mild hypersuccinylacetonemia rather than overt hepatorenal disease. (fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1, gramer2024newcasesof pages 2-4)

- **MONDO:** MONDO:0060527.
- **OMIM phenotype:** **617596**.
- **Causal gene:** **GSTZ1**, glutathione S-transferase zeta 1; Ensembl ENSG00000100577. Open Targets associates only GSTZ1 with MONDO:0060527 and cites the original human series, PMID **27876694**. (OpenTargets Search: Maleylacetoacetate isomerase deficiency-GSTZ1)
- **Common names:** maleylacetoacetate isomerase deficiency; MAAI deficiency; MAAID; GSTZ1 deficiency; glutathione transferase zeta deficiency; hypersuccinylacetonemia due to GSTZ1 deficiency. Historical “tyrosinemia type Ib” terminology is potentially confusing and is best avoided.
- **ICD-10/ICD-11 and MeSH:** no disease-specific code or heading was established in the retrieved authoritative literature. A broad inherited amino-acid/metabolic-disorder code may be used locally but is not equivalent to a dedicated MAAID identifier.
- **Orphanet:** no reliable disease-specific Orpha number was established from the retrieved evidence.

Evidence is mainly **aggregated disease-level literature derived from a very small number of molecularly confirmed patients and families**, not EHR-scale population data. The 2024 report combines NBS-cohort data with individual-level clinical and segregation findings. (gramer2024newcasesof pages 2-4, gramer2024newcasesof pages 1-2)

## 2. Etiology

### Causal factors and genetic risk

The established cause is **biallelic germline GSTZ1 dysfunction**, inherited autosomal recessively. Reported disease alleles include canonical and noncanonical splice variants, missense variants, and an in-frame/complex indel. Examples are:

- **c.136-2A>G**, homozygous: predicted exon-4 splice-acceptor loss, aberrant splicing, and nonsense-mediated decay; absent from gnomAD and ClinVar when reported and classified pathogenic under ACMG/AMP criteria.
- **c.68-12G>A**, shown by patient RNA analysis to activate a cryptic splice site, retain 10 nucleotides, frameshift, and probably introduce premature termination.
- **c.295G>A (p.Val99Met)**, found in trans with c.68-12G>A.
- **c.464_471delinsCTGGG (p.Val155_Asp157delinsAlaGly)**, found in trans with c.68-12G>A. (barretta2025variantsingstz1 pages 5-8, gramer2024newcasesof pages 2-4, barretta2025variantsingstz1 pages 9-11)

These are constitutional/germline variants; no somatic cause of inherited MAAID is established. Acquired GSTZ1 downregulation in cancer and pharmacologic inactivation by dichloroacetate (DCA) are biologically related but are **not** inherited MAAID.

### Environmental and gene–environment factors

No environmental exposure independently causes congenital MAAID. Mouse evidence indicates that high phenylalanine/tyrosine flux, homogentisate loading, or glutathione depletion can expose conditional toxicity. Acetaminophen or other glutathione-depleting exposures have therefore been proposed as risks, but this has not been demonstrated clinically. (board2011glutathionetransferasezeta pages 8-9, fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 7-8)

DCA is both a GSTZ1 substrate and mechanism-based inhibitor. Glutathione-dependent metabolism can produce a reactive adduct that covalently modifies Cys-16 and inactivates GSTZ1. Common GSTZ1 haplotypes alter DCA kinetics, illustrating a genuine GSTZ1–exposure interaction, but repeated DCA exposure does not fully reproduce germline knockout biology. (board2011glutathionetransferasezeta pages 8-9, board2011glutathionetransferasezeta pages 7-8, board2011glutathionetransferasezeta pages 9-10)

### Protective factors

The principal mechanistic buffer is a **glutathione-dependent, nonenzymatic MAA-to-FAA bypass**, demonstrated in vitro and in knockout mice. An alternative, weakly expressed adrenal GSTZ1 isoform may also retain activity despite some pathogenic variants, but compensation in patients remains speculative. No validated protective allele, diet, drug, or lifestyle intervention is known. (fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1, gramer2024newcasesof pages 5-7)

## 3. Phenotypes

The available phenotype denominator is extremely small; percentages would be misleading. Qualitative frequencies are therefore preferable.

- **Mild or intermittent succinylacetone elevation — characteristic/common.** Usually found neonatally through HT1 screening; plasma values in six Canadian cases were 0.23–1.28 µmol/L, and German initial DBS values were 2.61 and 2.48 µmol/L. Suggested HPO: **Abnormal circulating succinylacetone concentration** or the nearest available abnormal-metabolite term; an exact dedicated HPO term should be verified before deposition. (gramer2024newcasesof pages 5-7)
- **Urinary succinylacetone — variable/trace.** It may be persistent, intermittent, or undetectable in an affected adult. Suggested HPO: abnormal urinary metabolite concentration.
- **Elevated urinary maleic acid — apparently consistent in the 2023 tested series.** Suggested HPO: abnormal urinary organic-acid concentration. It is a promising biomarker, not yet a standardized diagnostic criterion. (barretta2025variantsingstz1 pages 9-11)
- **Normal plasma tyrosine — typical.** This helps distinguish MAAID from classic HT1 but does not alone exclude HT1. (barretta2025variantsingstz1 pages 1-2, gramer2024newcasesof pages 4-5)
- **Normal liver function/coagulation — typical in documented molecular cases.** No consistent hepatic failure, cirrhosis, renal disease, neurologic syndrome, or developmental disorder has emerged during available follow-up. (gramer2024newcasesof pages 1-2, barretta2025variantsingstz1 pages 1-2)
- **Microcephaly — isolated report.** One child had microcephaly at 16 months with age-appropriate development. Suggested HPO: **Microcephaly (HP:0000252)**. Causality is uncertain. (gramer2024newcasesof pages 4-5)
- **Short stature — isolated report.** Suggested HPO: **Short stature (HP:0004322)**; causality uncertain.
- **Obesity — isolated report.** Suggested HPO: **Obesity (HP:0001513)**; causality uncertain. (barretta2025variantsingstz1 pages 8-9)
- **Mild hyperbilirubinemia — one adult.** Suggested HPO: **Hyperbilirubinemia (HP:0002904)**; no evidence that it resulted from MAAID. (gramer2024newcasesof pages 2-4)

Onset of the biochemical phenotype is neonatal, but overt clinical onset is generally absent. Severity is usually subclinical/mild and the biochemical course may fluctuate. No disease-specific EQ-5D, SF-36, PROMIS, disability, behavioral, or quality-of-life study exists. The principal documented burden is diagnostic uncertainty, recalls, possible unnecessary HT1 therapy, and parental anxiety. (gramer2024newcasesof pages 7-8)

## 4. Genetic and molecular information

**GSTZ1** encodes the bifunctional cytosolic enzyme glutathione S-transferase zeta 1/maleylacetoacetate isomerase. The disease mechanism is loss of function; gain-of-function, dominant-negative, repeat-expansion, mitochondrial, or somatic mechanisms are not established. Open Targets records five evidence items linking GSTZ1 to MONDO:0060527. (OpenTargets Search: Maleylacetoacetate isomerase deficiency-GSTZ1)

Pathogenicity evidence includes trans configuration in affected individuals, segregation, rarity/absence in population databases, canonical splice disruption, predicted nonsense-mediated decay, and direct RNA confirmation for c.68-12G>A. Exact contemporary ClinVar classifications and gnomAD frequencies should be re-queried per variant at ingestion because databases change; only c.136-2A>G was explicitly reported absent from both resources in the 2024 study. (barretta2025variantsingstz1 pages 5-8, gramer2024newcasesof pages 2-4)

No validated modifier gene, epigenetic signature, recurrent copy-number abnormality, translocation, or disease-associated chromosomal lesion has been reported. The apparently healthy homozygous father indicates that biallelic loss can have very low penetrance for overt morbidity or markedly variable expressivity. (gramer2024newcasesof pages 2-4)

## 5. Environmental information

Smoking, alcohol, exercise, occupation, pollution, radiation, infection, and sex have not been shown to alter congenital MAAID risk. Infections were tolerated normally by the untreated homozygous adult in the 2024 family. No infectious agent causes or triggers the disorder. (gramer2024newcasesof pages 7-8, gramer2024newcasesof pages 5-7)

High protein or phenylalanine/tyrosine load and glutathione depletion are theoretical human stressors derived from animal experiments. DCA exposure is particularly relevant because GSTZ1 metabolizes DCA and is inactivated during that metabolism. DCA occurs as a water-chlorination by-product, industrial-solvent metabolite, and investigational drug, but environmentally acquired GSTZ1 inhibition must not be conflated with Mendelian MAAID. (lim2004micedeficientin pages 14-14, board2011glutathionetransferasezeta pages 7-8)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic GSTZ1 loss-of-function variants lead to** reduced cytosolic GSTZ1/MAAI activity.
2. **Reduced MAAI activity leads to** impaired glutathione-dependent cis–trans isomerization of maleylacetoacetate (MAA) to fumarylacetoacetate (FAA).
3. **The block leads to** accumulation/diversion of reactive tyrosine-pathway intermediates and production of maleic acid, succinylacetoacetate, and succinylacetone.
4. **Metabolite production leads to** mild, persistent or intermittent blood/urinary succinylacetone and elevated urinary maleic acid—the principal demonstrated human manifestations.
5. **In parallel, glutathione enables** a nonenzymatic MAA-to-FAA bypass, which **results in** continued downstream flux and likely explains the mild baseline phenotype; its quantitative importance in humans is inferred from biochemical and mouse evidence.
6. **Under high substrate flux or glutathione depletion, experimental metabolite accumulation leads to** oxidative stress, antioxidant-response induction, cytotoxicity, and hepatic, renal, splenic, and leukocyte injury in knockout mice.
7. **These experimental injuries could lead to human organ disease under severe stress, but this branch remains inferred**: it has not been observed consistently in congenital human MAAID.

GSTZ1/MAAI is a 29-kDa cytoplasmic enzyme. Glutathione participates catalytically and is not normally consumed stoichiometrically in the isomerization. Suggested GO annotations include **phenylalanine catabolic process (GO:0006559)**, tyrosine catabolic process, glutathione transferase activity, maleylacetoacetate isomerase activity, cellular response to oxidative stress, and xenobiotic metabolic process. Suggested GO cellular component: **cytosol (GO:0005829)**. (fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1, board2011glutathionetransferasezeta pages 7-8)

The best-supported primary cell is the **hepatocyte (CL:0000182)**, with renal tubular epithelial cells, splenic leukocytes, neutrophils, monocytes, and lymphocytes implicated only by challenged knockout models. Oxidative responses include reduced glutathione, induction of alpha-, mu-, and pi-class GSTs, NQO1, and glutamate-cysteine ligase. (lim2004micedeficientin pages 1-2, board2011glutathionetransferasezeta pages 8-9, board2011glutathionetransferasezeta pages 9-10)

Acquired GSTZ1 loss in hepatocellular carcinoma can produce succinylacetone-dependent KEAP1 alkylation, NRF2/IGF1R signaling, or PHD2 inhibition with HIF-1α/VEGF activation. These are valuable mechanistic hypotheses but **not demonstrated congenital-MAAID phenotypes or evidence of increased cancer risk**. No human MAAID transcriptomic, proteomic, lipidomic, single-cell, spatial, CRISPR-screen, or integrated multi-omics dataset was identified. (barretta2025variantsingstz1 pages 1-2, barretta2025variantsingstz1 pages 11-12)

## 7. Anatomical structures affected

In humans, no organ is consistently clinically damaged. The **liver** is the main site of tyrosine catabolism and biochemical concern; the **kidney** is a secondary theoretical target. Mouse studies additionally implicate spleen and circulating leukocytes. Suggested anatomy terms are **liver (UBERON:0002107)**, **kidney (UBERON:0002113)**, **renal tubule (UBERON:0001231)**, **spleen (UBERON:0002106)**, and blood. (lim2004micedeficientin pages 1-2, fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1)

At tissue/cell level, suggested annotations are hepatocyte (CL:0000182), kidney epithelial cell, renal tubular epithelial cell, lymphocyte (CL:0000542), neutrophil (CL:0000775), and monocyte (CL:0000576). Subcellular localization is cytosolic. There is no lateralization.

## 8. Temporal development

Biochemical onset is congenital/neonatal and often recognized at 48–72-hour NBS. Succinylacetone can normalize on repeat DBS, remain trace-positive in urine, or fluctuate. No validated clinical stages exist. Available untreated follow-up spans infancy through 32 years—and a summarized literature table mentions a clinically well individual at 41 years—without a demonstrated progressive course. (barretta2025variantsingstz1 pages 2-4, gramer2024newcasesof pages 2-4, gramer2024newcasesof pages 5-7)

There is no established remission concept because most individuals are never symptomatic. Potential critical periods are inferred from mice: animals under 28 days were particularly vulnerable to phenylalanine challenge. This age-dependent lethality has not been shown in human infants. (board2011glutathionetransferasezeta pages 8-9)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. A child of two heterozygous carriers has the usual Mendelian 25% conception risk of biallelic disease, 50% carrier risk, and 25% chance of inheriting neither familial allele. The 2024 index case arose in a first-cousin Afghan family, illustrating the role of consanguinity but not a population-specific founder effect. (gramer2024newcasesof pages 2-4)

No robust prevalence, incidence, carrier frequency, sex ratio, ethnic enrichment, founder variant, anticipation, or germline-mosaicism estimate exists. Fewer than 20 patients were reported by 2025, with clinical follow-up for approximately nine. (barretta2025variantsingstz1 pages 1-2)

The Heidelberg experience provides only a center-level ascertainment estimate: among **516,803** screened newborns, 42 had elevated succinylacetone, two had confirmed HT1, two were suspected MAAID, and one MAAID case was genetically confirmed. One confirmed screened infant corresponds to approximately **1 per 516,803 screened births**, but this is not a valid prevalence estimate because of variable biomarkers, thresholds, incomplete confirmation, and asymptomatic adults. (gramer2024newcasesof pages 1-2)

Penetrance for biochemical abnormalities appears incomplete or fluctuating; penetrance for clinically important disease appears low but cannot be quantified. Expressivity is variable. Anticipation is not applicable.

## 10. Diagnostics

### Recommended workflow

1. Measure succinylacetone in NBS dried blood spots by tandem mass spectrometry.
2. Urgently repeat/confirm succinylacetone in DBS or plasma and perform urine organic-acid analysis; measure plasma amino acids, tyrosine, liver enzymes, bilirubin, glucose, coagulation, renal indices, and alpha-fetoprotein.
3. Exclude HT1 with **FAH** sequencing plus deletion/duplication analysis where appropriate. Treatment for possible HT1 should not be delayed if clinical/biochemical suspicion is substantial.
4. If succinylacetone is low-level/intermittent, tyrosine is normal, and FAH testing is negative, analyze **GSTZ1** by single-gene testing or an inherited-tyrosinemia panel. One reported panel included **HPD, FAH, TAT, HGD, and GSTZ1**.
5. Use parental segregation and, for suspected splice variants, RNA analysis. WES/WGS is useful when targeted testing is unrevealing or for discovery of deep intronic/structural variants. (gramer2024newcasesof pages 2-4, barretta2025variantsingstz1 pages 2-4)

Quantitative urinary maleic acid by LC-MS/MS is the leading emerging second-tier test. In the reported study it was elevated in all tested MAAID cases and most false-positive referrals, but absent in HT1. Limitations include instability, low concentration, potential organic-acid interference, lack of age/diet-specific reference intervals, and incomplete DBS validation. (barretta2025variantsingstz1 pages 9-11)

### Differential diagnosis

The critical differential is **FAH-related HT1**, a potentially fatal but treatable disorder. MAAID generally has much lower succinylacetone, normal tyrosine and liver function, and a benign course, but biomarker ranges overlap. Mild HT1 has been reported at succinylacetone values as low as 3.8–5.23 µmol/L or with undetectable urinary succinylacetone; therefore, raising the NBS cutoff merely to avoid MAAID can miss HT1. (gramer2024newcasesof pages 5-7)

Other differentials include transient/false-positive succinylacetone elevation, partial FAH deficiency, and other tyrosine-pathway disorders involving **TAT, HPD,** or **HGD**. CMA, karyotyping, FISH, mtDNA analysis, and repeat-expansion tests have no routine role unless another phenotype independently indicates them. Imaging, biopsy, EEG, EMG, and functional testing are not diagnostic for uncomplicated MAAID.

There are no standardized clinical diagnostic criteria or universal MAAID screening program. Detection is incidental to HT1 NBS; familial cascade testing is appropriate after molecular confirmation.

## 11. Outcome and prognosis

Available evidence supports a favorable prognosis. Six Canadian children reportedly remained untreated and clinically well through ages 1–13, while a homozygous father in the German family was clinically well at 32 years with essentially normal hepatic, renal, coagulation, AFP, amino-acid, and succinylacetone studies. (gramer2024newcasesof pages 1-2, gramer2024newcasesof pages 2-4)

No disease-specific deaths, survival curves, reduced life expectancy, organ-failure rates, disability estimates, validated prognostic model, or quality-of-life scores are available. Historical severe putative cases predated complete molecular confirmation and should not define the modern GSTZ1-confirmed phenotype. (fernandezcanon1998characterizationofa pages 7-8)

Potential adverse prognostic factors—high phenylalanine/tyrosine flux, glutathione depletion, or sustained high succinylacetone—are extrapolated from models. Neither congenital liver-cancer risk nor HCC surveillance beyond ordinary clinical judgment is established.

## 12. Treatment

No approved disease-specific treatment, formal guideline, or controlled trial exists. Most confirmed individuals have received **no pharmacotherapy and no protein restriction** and remained well. (gramer2024newcasesof pages 4-5, barretta2025variantsingstz1 pages 1-2)

One recent infant received **nitisinone/NTBC** plus tyrosine/phenylalanine restriction while HT1 remained possible. After MAAID confirmation, diet and NTBC were stopped at approximately 21–22 months; only a modest succinylacetone rise followed, and liver function and development remained normal at age four. Another untreated infant remained well at age two. These observations argue against routine NTBC or dietary restriction. (barretta2025variantsingstz1 pages 5-8)

A reasonable expert-derived strategy is:

- initially manage an unresolved positive screen as possible HT1;
- once biallelic GSTZ1 MAAID is confirmed and liver function is normal, stop unnecessary HT1-specific treatment under metabolic-specialist supervision;
- monitor growth/development, liver and renal indices, coagulation, AFP, plasma amino acids, and blood/urinary succinylacetone periodically;
- consider imaging or NTBC only for persistent substantial biochemical abnormalities or liver dysfunction, recognizing the absence of efficacy evidence. (barretta2025variantsingstz1 pages 8-9)

Suggested NCIt intervention concepts include **Genetic Counseling**, **Clinical Observation**, **Laboratory Test**, **Nitisinone**, and **Dietary Intervention**; exact NCIt codes should be validated against the current release. No gene, cell, RNA, surgical, immunologic, or rehabilitation therapy is indicated. ClinicalTrials.gov searching found no relevant MAAID interventional trial or NCT identifier.

## 13. Prevention

The germline disorder cannot be prevented by vaccination or lifestyle change. Primary reproductive prevention consists of genetic counseling, familial-variant carrier testing, prenatal diagnosis, and preimplantation genetic testing when desired. Secondary prevention is prompt molecular resolution of an elevated-succinylacetone NBS result to avoid both missed HT1 and unnecessary long-term NTBC/diet in MAAID. (gramer2024newcasesof pages 7-8)

Tertiary prevention is surveillance rather than proven prophylaxis. Avoiding extreme protein supplementation and using caution with profound glutathione-depleting exposures are biologically plausible but not evidence-based human recommendations. Standard immunization applies; no disease-specific vaccine, public-health environmental program, or prophylactic medication exists.

## 14. Other species and natural disease

No naturally occurring homologous veterinary disease, affected breed, zoonosis, or cross-species transmission was identified. The disorder is genetic and noninfectious.

Orthologous GSTZ/MAAI function is evolutionarily conserved. In *Aspergillus nidulans*, disruption of **maiA** prevents growth on phenylalanine/phenylacetate and causes accumulation of pathway products; the fungal phenotype demonstrates pathway conservation but is not a mammalian natural-disease model. (fernandezcanon1998characterizationofa pages 7-8)

RNAi silencing of MAAI in the blood-feeding insect *Rhodnius prolixus* reportedly produced no visible phenotype, consistent with possible bypass metabolism. This is mechanistically interesting but has little direct clinical fidelity.

## 15. Model organisms

The principal model is the germline **Gstz1-null mouse (Mus musculus; NCBI Taxon 10090)**. On ordinary chow, one strain was relatively healthy while excreting FAA and succinylacetone, directly supporting the nonenzymatic glutathione-dependent bypass. A BALB/c knockout showed hepatomegaly and renomegaly, multifocal hepatitis, renal ultrastructural abnormalities, splenic atrophy, altered leukocytes, elevated serum succinylacetone, and constitutive induction of GST and NQO1 antioxidant defenses. (lim2004micedeficientin pages 1-2, fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1)

Phenylalanine challenge caused age-dependent death in mice younger than 28 days and hepatic necrosis, macrovesicular steatosis, splenic atrophy, and leukopenia in survivors. Homogentisate, tyrosine-pathway loading, or glutathione depletion produced hepatic/renal injury; all glutathione-depleted mutants challenged with homogentisate died in one experiment. (board2011glutathionetransferasezeta pages 8-9, fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 7-8)

**Applications:** pathway flux, compensatory chemistry, metabolite toxicity, oxidative stress, DCA pharmacology, diet/drug interactions, and candidate interventions. **Limitations:** genetic background strongly changes phenotype; experimental substrate loads exceed ordinary human exposure; severe mouse hepatic, renal, immune, and lethal phenotypes have not been reproduced in confirmed human MAAID. No disease-specific human iPSC, organoid, zebrafish, rat knock-in, or humanized model was identified.

## Recent developments and authoritative interpretation

- **2023:** quantitative urinary maleic acid was reported as a potentially discriminating biomarker: elevated in tested MAAID but absent in HT1. This is promising for second-tier NBS resolution, although assay harmonization and validation remain necessary. DOI: [10.1002/jimd.12669](https://doi.org/10.1002/jimd.12669), published August 2023. (barretta2025variantsingstz1 pages 11-12, barretta2025variantsingstz1 pages 9-11)
- **2024:** Gramer et al. reported 516,803 screened newborns and a family containing an untreated homozygous, clinically well 32-year-old father. Their abstract concludes: **“Our observation of natural history over 32 years adds evidence for a benign clinical course of MAAI deficiency without specific treatment.”** DOI: [10.3390/ijns10010017](https://doi.org/10.3390/ijns10010017), published February 2024. (gramer2024newcasesof pages 2-4, gramer2024newcasesof pages 1-2)
- **2025 update:** two additional molecularly confirmed infants remained well, and RNA analysis established abnormal splicing from c.68-12G>A. The abstract states: **“Although our data argue against medical treatment in MAAID, longer follow-up data are warranted.”** DOI: [10.3390/genes16091009](https://doi.org/10.3390/genes16091009), published August 2025. This post-2024 evidence reinforces—but does not settle—the benign-course interpretation. (barretta2025variantsingstz1 pages 5-8, barretta2025variantsingstz1 pages 1-2)

## Key evidence limitations

The evidence base consists of a handful of screen-detected patients and relatives, with ascertainment biased toward biochemical rather than clinical disease. Robust prevalence, penetrance, genotype–phenotype relationships, longitudinal organ imaging, quality of life, reproductive outcomes, standardized biomarker ranges, treatment trials, and lifetime cancer risk are unknown. The most defensible present classification is therefore **an ultra-rare, usually benign or subclinical GSTZ1-related biochemical disorder that is clinically important mainly because it mimics HT1 on newborn screening**. Severe organ toxicity remains a conditional model-organism concern rather than a demonstrated common human outcome. (barretta2025variantsingstz1 pages 1-2, barretta2025variantsingstz1 pages 11-12, barretta2025variantsingstz1 pages 8-9)

## Principal references

1. Yang H, et al. *Hypersuccinylacetonaemia and normal liver function in maleylacetoacetate isomerase deficiency.* Journal of Medical Genetics. Published 2017;54:241–247. PMID **27876694**. DOI: [10.1136/jmedgenet-2016-104289](https://doi.org/10.1136/jmedgenet-2016-104289). (OpenTargets Search: Maleylacetoacetate isomerase deficiency-GSTZ1, gramer2024newcasesof pages 1-2)
2. van Vliet K, et al. *Maleic acid is a biomarker for maleylacetoacetate isomerase deficiency; implications for newborn screening of tyrosinemia type 1.* Journal of Inherited Metabolic Disease. Published August 2023. DOI: [10.1002/jimd.12669](https://doi.org/10.1002/jimd.12669). (barretta2025variantsingstz1 pages 11-12, barretta2025variantsingstz1 pages 9-11)
3. Gramer G, et al. *New Cases of Maleylacetoacetate Isomerase Deficiency with Detection by Newborn Screening and Natural History over 32 Years.* International Journal of Neonatal Screening. Published February 2024;10:17. DOI: [10.3390/ijns10010017](https://doi.org/10.3390/ijns10010017). (gramer2024newcasesof pages 2-4)
4. Fernández-Cañón JM, et al. *Maleylacetoacetate Isomerase (MAAI/GSTZ)-Deficient Mice Reveal a Glutathione-Dependent Nonenzymatic Bypass in Tyrosine Catabolism.* Molecular and Cellular Biology. Published July 2002;22:4943–4951. DOI: [10.1128/MCB.22.13.4943-4951.2002](https://doi.org/10.1128/MCB.22.13.4943-4951.2002). (fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1)
5. Lim CEL, et al. *Mice Deficient in Glutathione Transferase Zeta/Maleylacetoacetate Isomerase Exhibit a Range of Pathological Changes.* American Journal of Pathology. Published August 2004;165:679–693. DOI: [10.1016/S0002-9440(10)63332-9](https://doi.org/10.1016/S0002-9440(10)63332-9). (lim2004micedeficientin pages 1-2)
6. Barretta F, et al. *Variants in GSTZ1 Gene Underlying Maleylacetoacetate Isomerase Deficiency: Characterization of Two New Individuals and Literature Review.* Genes. Published August 2025;16:1009. DOI: [10.3390/genes16091009](https://doi.org/10.3390/genes16091009). (barretta2025variantsingstz1 pages 5-8)

References

1. (gramer2024newcasesof pages 1-2): Gwendolyn Gramer, Saskia B. Wortmann, Junmin Fang-Hoffmann, Dirk Kohlmüller, Jürgen G. Okun, Holger Prokisch, Thomas Meitinger, and Georg F. Hoffmann. New cases of maleylacetoacetate isomerase deficiency with detection by newborn screening and natural history over 32 years: experience from a german newborn screening center. International Journal of Neonatal Screening, 10(1):17, Feb 2024. URL: https://doi.org/10.3390/ijns10010017, doi:10.3390/ijns10010017. This article has 4 citations.

2. (barretta2025variantsingstz1 pages 1-2): Ferdinando Barretta, Fabiana Uomo, Alessandra Verde, Mariagrazia Fisco, Giovanna Gallo, Lucia Albano, Daniela Crisci, Cristina Mazzaccara, Pietro Strisciuglio, Margherita Ruoppolo, Simona Fecarotta, Giancarlo Parenti, Giulia Frisso, and Alessandro Rossi. Variants in gstz1 gene underlying maleylacetoacetate isomerase deficiency: characterization of two new individuals and literature review. Genes, 16(9):1009, Aug 2025. URL: https://doi.org/10.3390/genes16091009, doi:10.3390/genes16091009. This article has 0 citations.

3. (barretta2025variantsingstz1 pages 9-11): Ferdinando Barretta, Fabiana Uomo, Alessandra Verde, Mariagrazia Fisco, Giovanna Gallo, Lucia Albano, Daniela Crisci, Cristina Mazzaccara, Pietro Strisciuglio, Margherita Ruoppolo, Simona Fecarotta, Giancarlo Parenti, Giulia Frisso, and Alessandro Rossi. Variants in gstz1 gene underlying maleylacetoacetate isomerase deficiency: characterization of two new individuals and literature review. Genes, 16(9):1009, Aug 2025. URL: https://doi.org/10.3390/genes16091009, doi:10.3390/genes16091009. This article has 0 citations.

4. (OpenTargets Search: Maleylacetoacetate isomerase deficiency-GSTZ1): Open Targets Query (Maleylacetoacetate isomerase deficiency-GSTZ1, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (gramer2024newcasesof pages 2-4): Gwendolyn Gramer, Saskia B. Wortmann, Junmin Fang-Hoffmann, Dirk Kohlmüller, Jürgen G. Okun, Holger Prokisch, Thomas Meitinger, and Georg F. Hoffmann. New cases of maleylacetoacetate isomerase deficiency with detection by newborn screening and natural history over 32 years: experience from a german newborn screening center. International Journal of Neonatal Screening, 10(1):17, Feb 2024. URL: https://doi.org/10.3390/ijns10010017, doi:10.3390/ijns10010017. This article has 4 citations.

6. (barretta2025variantsingstz1 pages 5-8): Ferdinando Barretta, Fabiana Uomo, Alessandra Verde, Mariagrazia Fisco, Giovanna Gallo, Lucia Albano, Daniela Crisci, Cristina Mazzaccara, Pietro Strisciuglio, Margherita Ruoppolo, Simona Fecarotta, Giancarlo Parenti, Giulia Frisso, and Alessandro Rossi. Variants in gstz1 gene underlying maleylacetoacetate isomerase deficiency: characterization of two new individuals and literature review. Genes, 16(9):1009, Aug 2025. URL: https://doi.org/10.3390/genes16091009, doi:10.3390/genes16091009. This article has 0 citations.

7. (gramer2024newcasesof pages 5-7): Gwendolyn Gramer, Saskia B. Wortmann, Junmin Fang-Hoffmann, Dirk Kohlmüller, Jürgen G. Okun, Holger Prokisch, Thomas Meitinger, and Georg F. Hoffmann. New cases of maleylacetoacetate isomerase deficiency with detection by newborn screening and natural history over 32 years: experience from a german newborn screening center. International Journal of Neonatal Screening, 10(1):17, Feb 2024. URL: https://doi.org/10.3390/ijns10010017, doi:10.3390/ijns10010017. This article has 4 citations.

8. (gramer2024newcasesof pages 4-5): Gwendolyn Gramer, Saskia B. Wortmann, Junmin Fang-Hoffmann, Dirk Kohlmüller, Jürgen G. Okun, Holger Prokisch, Thomas Meitinger, and Georg F. Hoffmann. New cases of maleylacetoacetate isomerase deficiency with detection by newborn screening and natural history over 32 years: experience from a german newborn screening center. International Journal of Neonatal Screening, 10(1):17, Feb 2024. URL: https://doi.org/10.3390/ijns10010017, doi:10.3390/ijns10010017. This article has 4 citations.

9. (barretta2025variantsingstz1 pages 8-9): Ferdinando Barretta, Fabiana Uomo, Alessandra Verde, Mariagrazia Fisco, Giovanna Gallo, Lucia Albano, Daniela Crisci, Cristina Mazzaccara, Pietro Strisciuglio, Margherita Ruoppolo, Simona Fecarotta, Giancarlo Parenti, Giulia Frisso, and Alessandro Rossi. Variants in gstz1 gene underlying maleylacetoacetate isomerase deficiency: characterization of two new individuals and literature review. Genes, 16(9):1009, Aug 2025. URL: https://doi.org/10.3390/genes16091009, doi:10.3390/genes16091009. This article has 0 citations.

10. (barretta2025variantsingstz1 pages 2-4): Ferdinando Barretta, Fabiana Uomo, Alessandra Verde, Mariagrazia Fisco, Giovanna Gallo, Lucia Albano, Daniela Crisci, Cristina Mazzaccara, Pietro Strisciuglio, Margherita Ruoppolo, Simona Fecarotta, Giancarlo Parenti, Giulia Frisso, and Alessandro Rossi. Variants in gstz1 gene underlying maleylacetoacetate isomerase deficiency: characterization of two new individuals and literature review. Genes, 16(9):1009, Aug 2025. URL: https://doi.org/10.3390/genes16091009, doi:10.3390/genes16091009. This article has 0 citations.

11. (fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 1-1): José Manuel Fernández-Cañón, Manfred W. Baetscher, Milton Finegold, Terry Burlingame, K. Michael Gibson, and Markus Grompe. Maleylacetoacetate isomerase (maai/gstz)-deficient mice reveal a glutathione-dependent nonenzymatic bypass in tyrosine catabolism. Molecular and Cellular Biology, 22:4943-4951, Jul 2002. URL: https://doi.org/10.1128/mcb.22.13.4943-4951.2002, doi:10.1128/mcb.22.13.4943-4951.2002. This article has 122 citations and is from a domain leading peer-reviewed journal.

12. (board2011glutathionetransferasezeta pages 7-8): Philip G. Board and M.W. Anders. Glutathione transferase zeta: discovery, polymorphic variants, catalysis, inactivation, and properties of gstz1−/− mice. Drug Metabolism Reviews, 43:215-225, Apr 2011. URL: https://doi.org/10.3109/03602532.2010.549132, doi:10.3109/03602532.2010.549132. This article has 33 citations and is from a peer-reviewed journal.

13. (lim2004micedeficientin pages 1-2): Cindy E.L. Lim, Klaus I. Matthaei, Anneke C. Blackburn, Richard P. Davis, Jane E. Dahlstrom, Mark E. Koina, M.W. Anders, and Philip G. Board. Mice deficient in glutathione transferase zeta/maleylacetoacetate isomerase exhibit a range of pathological changes and elevated expression of alpha, mu, and pi class glutathione transferases. The American Journal of Pathology, 165(2):679-693, Aug 2004. URL: https://doi.org/10.1016/s0002-9440(10)63332-9, doi:10.1016/s0002-9440(10)63332-9. This article has 75 citations.

14. (board2011glutathionetransferasezeta pages 8-9): Philip G. Board and M.W. Anders. Glutathione transferase zeta: discovery, polymorphic variants, catalysis, inactivation, and properties of gstz1−/− mice. Drug Metabolism Reviews, 43:215-225, Apr 2011. URL: https://doi.org/10.3109/03602532.2010.549132, doi:10.3109/03602532.2010.549132. This article has 33 citations and is from a peer-reviewed journal.

15. (fernandezcanon2002maleylacetoacetateisomerase(maaigstz)deficient pages 7-8): José Manuel Fernández-Cañón, Manfred W. Baetscher, Milton Finegold, Terry Burlingame, K. Michael Gibson, and Markus Grompe. Maleylacetoacetate isomerase (maai/gstz)-deficient mice reveal a glutathione-dependent nonenzymatic bypass in tyrosine catabolism. Molecular and Cellular Biology, 22:4943-4951, Jul 2002. URL: https://doi.org/10.1128/mcb.22.13.4943-4951.2002, doi:10.1128/mcb.22.13.4943-4951.2002. This article has 122 citations and is from a domain leading peer-reviewed journal.

16. (barretta2025variantsingstz1 pages 11-12): Ferdinando Barretta, Fabiana Uomo, Alessandra Verde, Mariagrazia Fisco, Giovanna Gallo, Lucia Albano, Daniela Crisci, Cristina Mazzaccara, Pietro Strisciuglio, Margherita Ruoppolo, Simona Fecarotta, Giancarlo Parenti, Giulia Frisso, and Alessandro Rossi. Variants in gstz1 gene underlying maleylacetoacetate isomerase deficiency: characterization of two new individuals and literature review. Genes, 16(9):1009, Aug 2025. URL: https://doi.org/10.3390/genes16091009, doi:10.3390/genes16091009. This article has 0 citations.

17. (board2011glutathionetransferasezeta pages 9-10): Philip G. Board and M.W. Anders. Glutathione transferase zeta: discovery, polymorphic variants, catalysis, inactivation, and properties of gstz1−/− mice. Drug Metabolism Reviews, 43:215-225, Apr 2011. URL: https://doi.org/10.3109/03602532.2010.549132, doi:10.3109/03602532.2010.549132. This article has 33 citations and is from a peer-reviewed journal.

18. (gramer2024newcasesof pages 7-8): Gwendolyn Gramer, Saskia B. Wortmann, Junmin Fang-Hoffmann, Dirk Kohlmüller, Jürgen G. Okun, Holger Prokisch, Thomas Meitinger, and Georg F. Hoffmann. New cases of maleylacetoacetate isomerase deficiency with detection by newborn screening and natural history over 32 years: experience from a german newborn screening center. International Journal of Neonatal Screening, 10(1):17, Feb 2024. URL: https://doi.org/10.3390/ijns10010017, doi:10.3390/ijns10010017. This article has 4 citations.

19. (lim2004micedeficientin pages 14-14): Cindy E.L. Lim, Klaus I. Matthaei, Anneke C. Blackburn, Richard P. Davis, Jane E. Dahlstrom, Mark E. Koina, M.W. Anders, and Philip G. Board. Mice deficient in glutathione transferase zeta/maleylacetoacetate isomerase exhibit a range of pathological changes and elevated expression of alpha, mu, and pi class glutathione transferases. The American Journal of Pathology, 165(2):679-693, Aug 2004. URL: https://doi.org/10.1016/s0002-9440(10)63332-9, doi:10.1016/s0002-9440(10)63332-9. This article has 75 citations.

20. (fernandezcanon1998characterizationofa pages 7-8): José Manuel Fernández-Cañón and Miguel Angel Peñalva. Characterization of a fungal maleylacetoacetate isomerase gene and identification of its human homologue*. The Journal of Biological Chemistry, 273:329-337, Jan 1998. URL: https://doi.org/10.1074/jbc.273.1.329, doi:10.1074/jbc.273.1.329. This article has 143 citations.

## Artifacts

- [Edison artifact artifact-00](Maleylacetoacetate_Isomerase_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 2 |
| References weighed for topical relevance | 10 |
| On topic | 2 |
| Off topic | 0 |

10 of 12 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0060527` (5 mentions) - the report calls it "if available"; MONDO calls it **maleylacetoacetate isomerase deficiency**