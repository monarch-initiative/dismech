---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T11:21:10.693393'
end_time: '2026-09-09T11:34:38.041973'
duration_seconds: 807.35
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Progressive External Ophthalmoplegia with Mitochondrial DNA Deletions,
    Autosomal Recessive 4
  mondo_id: MONDO:0014899
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014899
    reported_labels:
    - if available
    ontology_label: progressive external ophthalmoplegia with mitochondrial DNA deletions,
      autosomal recessive 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Progressive_External_Ophthalmoplegia_With_Mitochondrial_DNA_Deletions_Autosomal_Recessive_4-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive External Ophthalmoplegia with Mitochondrial DNA Deletions, Autosomal Recessive 4
- **MONDO ID:** MONDO:0014899 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive External Ophthalmoplegia with Mitochondrial DNA Deletions, Autosomal Recessive 4** covering all of the
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
- **Disease Name:** Progressive External Ophthalmoplegia with Mitochondrial DNA Deletions, Autosomal Recessive 4
- **MONDO ID:** MONDO:0014899 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive External Ophthalmoplegia with Mitochondrial DNA Deletions, Autosomal Recessive 4** covering all of the
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


# Progressive External Ophthalmoplegia with Mitochondrial DNA Deletions, Autosomal Recessive 4

## Executive summary and evidence boundaries

**Progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 4 (PEO4)** is an exceptionally rare, nuclear-encoded mitochondrial DNA-maintenance disorder caused by **biallelic germline variants in DGUOK**, which encodes mitochondrial deoxyguanosine kinase. The best direct evidence is a small human clinical-molecular series published by Ronchi et al. in *Brain* on **4 October 2012** (print November 2012; PMID **23043144**; DOI/URL: https://doi.org/10.1093/brain/aws258). Five independent DGUOK-positive subjects constituted **5.6% of a selected referral cohort with adult mitochondrial myopathy and multiple skeletal-muscle mtDNA deletions**; this is not a population-prevalence estimate. Presentations ranged from late-onset ptosis/PEO and mitochondrial myopathy to rhabdomyolysis or lower-motor-neuron disease. Patient muscle showed reduced DGUOK protein or abnormal splicing, residual enzyme activity of approximately **19–45%**, and multiple mtDNA deletions. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8)

The phenotype must be distinguished from the much better documented **DGUOK-related hepatocerebral mtDNA-depletion syndrome**, often presenting in infancy with liver failure. Those conditions form an allelic spectrum, but infantile hepatocerebral findings, transplant outcomes, and mortality statistics should not automatically be assigned to adult PEO4. More than 100 people with all forms of DGUOK deficiency have been reported, but no population study has estimated PEO4 prevalence or incidence. (elhattab1993deoxyguanosinekinasedeficiency pages 3-6, elhattab1993deoxyguanosinekinasedeficiency pages 1-3, ronchi2012nextgenerationsequencingreveals pages 8-9, elhattab1993deoxyguanosinekinasedeficiency pages 6-8)

| Domain | High-confidence finding | Suggested ontology identifiers/terms | Evidence scope / caveat |
|---|---|---|---|
| Identity / gene | Progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 4 is a **DGUOK-related mitochondrial DNA-maintenance disorder** characterized by adult mitochondrial myopathy, variably including progressive external ophthalmoplegia and multiple skeletal-muscle mtDNA deletions. | **MONDO:0014899**; DGUOK; deoxyguanosine kinase; PEO4; autosomal-recessive progressive external ophthalmoplegia | Direct disease-level mapping and human molecular evidence. DGUOK also causes severe hepatocerebral mtDNA-depletion disease, which is broader than PEO4. (OpenTargets Search: Progressive external ophthalmoplegia with mitochondrial DNA deletions autosomal recessive 4, ronchi2012nextgenerationsequencingreveals pages 1-2) |
| Inheritance | Biallelic germline DGUOK variants cause disease through **autosomal-recessive inheritance**; carrier parents are generally asymptomatic, and recurrence risk is 25% for each pregnancy when both parents are carriers. | Autosomal recessive inheritance; germline variant; genetic carrier | Direct for DGUOK-associated disease; recurrence-risk statement follows Mendelian inheritance. Penetrance among individuals with two definitively pathogenic alleles is not quantified. (ronchi2012nextgenerationsequencingreveals pages 1-2, elhattab1993deoxyguanosinekinasedeficiency pages 12-15) |
| Core ocular phenotypes | Principal ocular findings are slowly progressive external ophthalmoplegia or ophthalmoparesis and usually bilateral ptosis; strabismus can occur. | **HPO labels:** Progressive external ophthalmoplegia; Ptosis; Strabismus | Direct patient-level evidence, but the published DGUOK cohort was very small and some affected individuals lacked ophthalmoplegia. Reliable percentages cannot be assigned. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3, ronchi2012nextgenerationsequencingreveals pages 8-9) |
| Other muscle phenotypes | The spectrum includes mitochondrial myopathy, limb-girdle or distal weakness, neck weakness, exercise-related pain or intolerance, cramps, dysphagia, dysphonia, and occasional rhabdomyolysis. | **HPO labels:** Mitochondrial myopathy; Muscle weakness; Proximal muscle weakness; Distal muscle weakness; Exercise intolerance; Muscle cramps; Dysphagia; Dysphonia; Rhabdomyolysis | Direct adult DGUOK case-series evidence; manifestations vary substantially and may represent PEO-plus or non-PEO DGUOK phenotypes. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 3-4) |
| Neurologic / systemic phenotypes | Rare reported presentations include adult lower-motor-neuron disease with mild cognitive impairment; diabetes and cataract occurred in an individual patient. Childhood liver disease may precede later myopathy in broader DGUOK deficiency. | **HPO labels:** Lower motor neuron dysfunction; Mild cognitive impairment; Diabetes mellitus; Cataract; Hepatic dysfunction | Patient-level associations do not establish typical PEO4 frequencies or direct causality for every feature. Infantile liver disease belongs to the broader DGUOK spectrum. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 9-10) |
| Laboratory / pathology | Muscle may show elevated creatine kinase, myopathic EMG, ragged-red fibers, cytochrome-c-oxidase-negative fibers, severe COX deficiency, and multiple mtDNA deletions. Lactate may be normal or moderately increased. | **HPO labels:** Elevated circulating creatine kinase; Ragged-red muscle fibers; Cytochrome-c oxidase deficiency; Abnormality of mitochondrial metabolism; mitochondrial DNA deletion | Direct patient-level clinical, histologic, and molecular evidence. Normal lactate does not exclude disease. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3) |
| Molecular mechanism | Mitochondrial DGUOK phosphorylates deoxyguanosine and deoxyadenosine to dGMP and dAMP in the purine-nucleoside salvage pathway. Reduced activity disrupts mitochondrial dNTP supply, impairs mtDNA maintenance, and produces depletion and/or multiple deletions followed by respiratory-chain dysfunction. | **GO labels:** Deoxyguanosine kinase activity; Deoxyadenosine kinase activity; Purine deoxyribonucleoside salvage; Mitochondrial DNA replication; Mitochondrial genome maintenance; Oxidative phosphorylation | The enzyme defect and mtDNA instability are supported directly; the detailed sequence from nucleotide imbalance to selective extraocular-muscle degeneration is partly inferred. (ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8, elhattab1993deoxyguanosinekinasedeficiency pages 12-15) |
| Variants / functional evidence | Reported variants include c.186C>A (p.Tyr62Ter), c.605_606delGA (p.Arg202TyrfsTer12), c.130G>A (p.Glu44Lys), c.137A>G (p.Asn46Ser), c.462T>A (p.Asn154Lys), c.509A>G (p.Gln170Arg), and c.444-11C>G. Patient muscle showed reduced protein or abnormal splicing and residual DGUOK activity of approximately **19%–45%** of control. | DGUOK sequence variant; missense variant; nonsense variant; frameshift variant; splice-region variant; loss of function | Direct functional human-muscle evidence. p.Gln170Arg alone has uncertain significance because it occurred in controls at a reported allele frequency of 1.98%; variants require phase, population, segregation, and ACMG/AMP reassessment rather than blanket pathogenic classification. (ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8, ronchi2012nextgenerationsequencingreveals pages 8-9) |
| Anatomy / cells / compartments | Extraocular and skeletal muscles are primary affected tissues; myofibers contain dysfunctional mitochondria and accumulated mtDNA abnormalities. Bulbar and lower-motor-neuron involvement may occur in broader presentations. DGUOK localizes to the mitochondrial matrix. | **UBERON labels:** Extraocular muscle; Skeletal muscle tissue. **CL labels:** Skeletal muscle fiber; Extraocular muscle cell; Lower motor neuron. **GO labels:** Mitochondrial matrix; Mitochondrion; Mitochondrial nucleoid | Extraocular and skeletal muscle involvement and mitochondrial localization are supported; cell-specific clonal expansion and selective vulnerability are incompletely demonstrated for DGUOK-PEO4. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 7-8, ronchi2012nextgenerationsequencingreveals pages 8-9) |
| Diagnosis | Diagnosis integrates ptosis or ophthalmoparesis, CK and lactate testing, EMG, muscle histology, mtDNA deletion/depletion analysis in affected tissue, and demonstration of biallelic pathogenic or likely pathogenic DGUOK variants. Sequencing detects most DGUOK pathogenic variants; deletion/duplication analysis is considered if sequencing is incomplete. | Genetic testing; mitochondrial DNA deletion analysis; mitochondrial DNA copy-number analysis; muscle biopsy; electromyography; DGUOK sequencing; multigene panel; exome sequencing; genome sequencing | Direct PEO4 evidence supports muscle mtDNA analysis plus DGUOK testing; estimated yields of approximately 95% for sequence analysis and 5% for deletion/duplication analysis derive from broader DGUOK deficiency. A VUS does not establish or exclude diagnosis. (ronchi2012nextgenerationsequencingreveals pages 1-2, elhattab1993deoxyguanosinekinasedeficiency pages 3-6, elhattab1993deoxyguanosinekinasedeficiency pages 1-3) |
| Treatment | No curative or DGUOK-PEO4-specific approved therapy is established. Management is individualized and supportive: ptosis and ocular-motility management, physical and occupational therapy, swallowing and nutritional assessment, and surveillance for respiratory, cardiac, neurologic, endocrine, and hepatic complications when indicated. | **NCIT labels:** Supportive care; Physical therapy; Occupational therapy; Ptosis repair; Nutritional support; Genetic counseling | Symptomatic management is extrapolated largely from mitochondrial CPEO practice rather than controlled DGUOK-PEO4 trials. Liver transplantation pertains to selected liver-predominant DGUOK deficiency and is not treatment for isolated adult PEO4; later muscle disease can still emerge. (ronchi2012nextgenerationsequencingreveals pages 9-10, elhattab1993deoxyguanosinekinasedeficiency pages 1-3) |
| Epidemiology | Population prevalence, incidence, carrier frequency, sex ratio, penetrance, and survival for PEO4 are unknown. Biallelic DGUOK variants accounted for **5.6%** of one selected adult cohort with multiple skeletal-muscle mtDNA deletions. More than 100 individuals with all forms of DGUOK deficiency have been reported. | Rare disease; orphan disease | The 5.6% figure is a referral-cohort proportion, not population prevalence. Broader estimates that DGUOK causes 15%–20% of mtDNA-depletion syndromes should not be applied to adult PEO4. (ronchi2012nextgenerationsequencingreveals pages 1-2, elhattab1993deoxyguanosinekinasedeficiency pages 6-8) |
| Evidence gaps | No robust PEO4-specific natural-history cohort, validated severity scale, prevalence study, genotype–phenotype model, protective allele, environmental-risk association, epigenetic signature, single-cell or spatial dataset, faithful disease-specific animal model, prognostic biomarker, randomized treatment trial, or DGUOK-specific interventional trial was identified. | Evidence gap; natural history study; biomarker study; clinical trial; single-cell transcriptomics; disease model | Negative finding from the retrieved literature and trial searches, not proof that no unpublished or newly registered evidence exists. Most knowledge rests on a small number of human cases and broader mitochondrial-disease extrapolation. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 9-10, elhattab1993deoxyguanosinekinasedeficiency pages 6-8) |


*Table: High-confidence disease, phenotype, mechanism, diagnostic, and management annotations for MONDO:0014899. The table distinguishes direct PEO4 evidence from broader DGUOK-deficiency evidence and highlights major knowledge gaps.*

## 1. Disease information

### Definition

PEO4 is a Mendelian mitochondrial myopathy in which recessive nuclear **DGUOK** dysfunction causes secondary instability of the mitochondrial genome, especially **multiple mtDNA deletions in skeletal muscle**. The defining clinical ocular manifestations are slowly progressive, generally bilateral ptosis and external ophthalmoparesis; however, DGUOK disease can produce mitochondrial myopathy without ophthalmoplegia and broader “PEO-plus” phenotypes. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 2-3, ronchi2012nextgenerationsequencingreveals pages 8-9)

### Identifiers and names

- **MONDO:** MONDO:0014899.
- **Causal target:** DGUOK, Ensembl **ENSG00000114956**, approved name *deoxyguanosine kinase*. Open Targets maps MONDO:0014899 to DGUOK using five association-evidence records, including PMID 23043144. (OpenTargets Search: Progressive external ophthalmoplegia with mitochondrial DNA deletions autosomal recessive 4)
- **Common names:** PEO4; autosomal-recessive progressive external ophthalmoplegia 4; progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 4; DGUOK-related progressive external ophthalmoplegia; DGUOK-related mitochondrial myopathy with multiple mtDNA deletions.
- **OMIM:** commonly represented as the DGUOK-related recessive PEO entry; the retrieved evidence did not independently verify the exact phenotype MIM number, so it should be checked directly against the live OMIM record before database ingestion.
- **Orphanet:** no PEO4-specific Orphanet identifier was verified from the retrieved evidence; Orphanet may aggregate it under genetic PEO or mtDNA-maintenance disorders.
- **ICD-10/ICD-11 and MeSH:** no uniquely specific code exists in the retrieved evidence. Coding generally falls under mitochondrial metabolism/myopathy or ophthalmoplegia categories and loses the DGUOK/genotype distinction.

This report synthesizes **aggregated disease resources and published patient-level research**, not EHR-derived individual data. The Ronchi study contains identifiable clinical profiles but is a research cohort, not a real-world EHR extraction. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 3-4)

## 2. Etiology

### Causal and genetic factors

The necessary cause is usually **biallelic loss-of-function or function-reducing DGUOK variants**. Reported classes include missense, nonsense, frameshift, and splice-altering variants. DGUOK is a mitochondrial purine-salvage enzyme; impaired activity produces inadequate or imbalanced mitochondrial deoxyribonucleotide pools and defective mtDNA maintenance. (ronchi2012nextgenerationsequencingreveals pages 7-8, elhattab1993deoxyguanosinekinasedeficiency pages 12-15)

Variants reported in the adult multiple-deletion cohort included c.186C>A (p.Tyr62Ter), c.605_606delGA (p.Arg202TyrfsTer12), c.130G>A (p.Glu44Lys), c.137A>G (p.Asn46Ser), c.462T>A (p.Asn154Lys), c.509A>G (p.Gln170Arg), and c.444-11C>G. The c.444-11C>G allele disrupted splicing and its mutant transcript was absent from muscle cDNA, consistent with degradation; several genotypes reduced protein abundance or enzyme activity. (ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8)

**Variant-interpretation warning:** p.Gln170Arg occurred in healthy Italian controls at a reported allele frequency of **1.98%**, making it unsuitable for blanket classification as a fully penetrant pathogenic allele without phase, segregation, functional, and current population-database reassessment. A variant of uncertain significance neither confirms nor excludes diagnosis. (elhattab1993deoxyguanosinekinasedeficiency pages 1-3, ronchi2012nextgenerationsequencingreveals pages 8-9)

### Environmental, infectious, and lifestyle risks

No toxin, infection, radiation exposure, occupation, diet, smoking behavior, alcohol exposure, or other environmental factor is established as a cause of PEO4. Physiologic stress, illness, fasting, or medications may aggravate symptoms in mitochondrial disease generally, but no DGUOK-PEO4-specific gene–environment interaction has been demonstrated. Infectious-agent and zoonotic categories are therefore **not applicable etiologically**.

### Protective factors and modifiers

No validated protective DGUOK allele, nuclear modifier, mtDNA haplogroup modifier, diet, supplement, exercise program, or exposure has been shown to prevent PEO4. Residual DGUOK activity is biologically plausible as a severity modifier, but the original adult series found no simple relationship between residual muscle activity and age at myopathic onset. (ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 8-9)

## 3. Phenotypes

Because the direct cohort is very small, percentages would be misleading. Frequencies below are qualitative unless explicitly stated.

- **Progressive external ophthalmoplegia/ophthalmoparesis — clinical sign:** adult or late-adult onset in documented patients; chronic, slowly progressive, generally bilateral. Suggested HPO: *Progressive external ophthalmoplegia*. One woman had an 11-year history at age 69; another older woman developed bilateral ptosis/PEO followed by limb-girdle weakness. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)
- **Ptosis — sign:** usually bilateral and progressive; may be mild or prominent. Suggested HPO: *Ptosis*, *Bilateral ptosis*. Ptosis can impair superior visual fields and reading and can cause compensatory frontalis activation or neck extension, although DGUOK-specific quality-of-life scores are unavailable. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)
- **Strabismus — sign:** reported in an adult with mild ptosis and wider neuromuscular disease. Suggested HPO: *Strabismus*. (ronchi2012nextgenerationsequencingreveals pages 3-4)
- **Mitochondrial myopathy and weakness — sign:** variable limb-girdle, distal, neck, tongue, or generalized weakness; slowly progressive in adult cases. Suggested HPO: *Mitochondrial myopathy*, *Proximal muscle weakness*, *Distal muscle weakness*, *Neck flexor weakness*. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 3-4)
- **Exercise symptoms — symptom:** exercise-induced pain, exercise intolerance, cramps, and CK elevation were documented. Suggested HPO: *Exercise intolerance*, *Myalgia*, *Muscle cramps*, *Elevated circulating creatine kinase*. These limit walking, work, and sustained activity, but no EQ-5D, SF-36, or PROMIS dataset exists for PEO4. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)
- **Bulbar/laryngeal involvement — symptoms/signs:** dysphagia, occasional liquid dysphagia, dysphonia, and tongue hypotrophy. Suggested HPO: *Dysphagia*, *Dysphonia*, *Tongue atrophy*. Aspiration and nutritional risk should be assessed clinically. (ronchi2012nextgenerationsequencingreveals pages 3-4)
- **Rhabdomyolysis — laboratory/clinical episode:** recurrent episodes were described in a young woman with previous infantile DGUOK liver disease and transplantation; this represents the broader DGUOK spectrum rather than classic isolated PEO4. Suggested HPO: *Rhabdomyolysis*. (ronchi2012nextgenerationsequencingreveals pages 1-2)
- **Lower-motor-neuron syndrome and mild cognitive impairment:** observed in siblings with multiple mtDNA deletions. Suggested HPO: *Lower motor neuron dysfunction*, *Mild cognitive impairment*. These are uncommon PEO-plus manifestations, not established core features. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 9-10)
- **Individual systemic observations:** diabetes and cataract occurred in one elderly patient; causality and frequency cannot be determined. Suggested HPO: *Diabetes mellitus*, *Cataract*. (ronchi2012nextgenerationsequencingreveals pages 3-4)
- **Laboratory/pathology:** CK ranged from mild elevation to approximately 2,000 U/L in one patient; lactate could be normal or moderately increased; EMG was myopathic; muscle contained ragged-red and COX-negative fibers, severe COX deficiency, and multiple mtDNA deletions. Suggested HPO: *Elevated circulating creatine kinase*, *Ragged-red muscle fibers*, *Cytochrome-c oxidase deficiency*, *Lactic acidosis* only when documented. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)

## 4. Genetic and molecular information

**DGUOK** encodes a nuclear-synthesized enzyme imported into the mitochondrial matrix. It phosphorylates deoxyguanosine and deoxyadenosine to dGMP and dAMP—the first step of mitochondrial purine-deoxyribonucleoside salvage. Suggested GO annotations include *deoxyguanosine kinase activity*, *deoxyadenosine kinase activity*, *purine deoxyribonucleoside salvage*, *mitochondrial DNA replication*, and *mitochondrial genome maintenance*. (ronchi2012nextgenerationsequencingreveals pages 7-8, ronchi2012nextgenerationsequencingreveals pages 8-9, elhattab1993deoxyguanosinekinasedeficiency pages 12-15)

The adult study supplied unusually strong functional evidence: abnormal muscle splicing, reduced DGUOK protein on western blot, and residual enzyme activities of **19–45% of controls**. This supports a predominantly loss-of-function mechanism. (ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8)

The variants are **germline**, not somatic cancer drivers. No recurrent PEO4-associated chromosomal aneuploidy, translocation, inversion, methylation defect, histone signature, or disease-specific chromatin abnormality is established. A Druze founder allele, c.255delA (p.Ala86ProfsTer13), is known in broader DGUOK deficiency, but is not specifically established as a PEO4 founder variant. (elhattab1993deoxyguanosinekinasedeficiency pages 12-15)

Current ClinVar classifications and gnomAD allele frequencies should be retrieved variant by variant at the time of interpretation; the primary paper predates modern ACMG/AMP curation. Particularly, p.Gln170Arg should not be treated as pathogenic in isolation. (ronchi2012nextgenerationsequencingreveals pages 8-9)

## 5. Environmental information

PEO4 is a genetic mtDNA-maintenance disorder. There is no demonstrated causal role for pollution, occupational exposure, radiation, tobacco, alcohol, diet, or infection. Sensible mitochondrial-disease practice—avoiding prolonged fasting, dehydration, extreme unaccustomed exertion, and mitochondrial-toxic drugs when alternatives exist—is precautionary and individualized, not evidence-based primary prevention for DGUOK-PEO4. No PEO4-specific CTD interaction, exposure-response statistic, or infectious trigger was identified.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic DGUOK function-reducing variants lead to** impaired synthesis, stability, splicing, or catalytic activity of mitochondrial deoxyguanosine kinase. (ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8)
2. **Reduced DGUOK activity leads to** inadequate phosphorylation of deoxyguanosine/deoxyadenosine to dGMP/dAMP and disturbed mitochondrial purine-dNTP supply. (ronchi2012nextgenerationsequencingreveals pages 7-8, elhattab1993deoxyguanosinekinasedeficiency pages 12-15)
3. **Disturbed dNTP homeostasis leads to** defective mtDNA replication and maintenance; the exact biochemical transition from pool imbalance to deletion formation is partly inferred. (ronchi2012nextgenerationsequencingreveals pages 9-10, elhattab1993deoxyguanosinekinasedeficiency pages 12-15)
4. **Defective maintenance results in** multiple mtDNA deletions in postmitotic skeletal muscle; profound alleles in other tissues can instead produce mtDNA depletion. (ronchi2012nextgenerationsequencingreveals pages 1-2, elhattab1993deoxyguanosinekinasedeficiency pages 1-3, ronchi2012nextgenerationsequencingreveals pages 7-8)
5. **Deleted/depleted mtDNA results in** deficient synthesis of mtDNA-encoded respiratory-chain subunits and mosaic OXPHOS failure, demonstrated histologically by COX-negative and ragged-red fibers. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)
6. **OXPHOS failure leads to** impaired ATP production and compensatory mitochondrial proliferation in energy-demanding myofibers; oxidative-stress and cell-death contributions are plausible but not directly demonstrated in PEO4.
7. **Energetic failure in extraocular muscle fibers leads to** bilateral ptosis and progressive ophthalmoparesis; involvement of limb, neck, bulbar, or respiratory muscles branches to weakness, exercise intolerance, dysphagia, and dysphonia. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)
8. **In some genotypes/tissues, broader mtDNA instability leads to** rhabdomyolysis, lower-motor-neuron disease, cognitive findings, or childhood hepatopathy; these branches are variable and not obligatory PEO4 features. (ronchi2012nextgenerationsequencingreveals pages 1-2, ronchi2012nextgenerationsequencingreveals pages 9-10)

**Upstream:** DGUOK genotype, transcript/protein stability, kinase activity, and mitochondrial dNTP supply. **Intermediate:** mtDNA replication/maintenance, deletion burden, depletion, and respiratory-chain assembly. **Downstream:** mosaic OXPHOS deficiency, myofiber dysfunction, and clinical weakness/ophthalmoplegia.

Suggested biological-process GO terms are *purine deoxyribonucleoside salvage*, *mitochondrial DNA replication*, *mitochondrial genome maintenance*, *oxidative phosphorylation*, *ATP metabolic process*, and *muscle contraction*. Suggested cell terms are *skeletal muscle fiber*, *extraocular muscle cell*, and—only for PEO-plus cases—*lower motor neuron*. No PEO4-specific immune, inflammatory, Wnt, MAPK, PI3K–AKT, mTOR, ferroptosis, autophagy, or apoptosis mechanism has been established.

No validated disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omics signature was identified. Functional evidence currently rests mainly on human muscle mtDNA assays, histology, western blotting, RT-PCR, and kinase assays. (ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8)

## 7. Anatomical structures affected

- **Primary organ/tissue:** bilateral extraocular muscles and other skeletal muscle. Suggested UBERON labels: *extraocular muscle*, *skeletal muscle tissue*.
- **Secondary sites:** eyelid elevators; limb-girdle, distal, cervical, lingual, pharyngeal, and laryngeal musculature; lower motor neurons in rare PEO-plus disease. Liver and brain involvement belong mainly to broader DGUOK deficiency.
- **Cell level:** skeletal and extraocular myofibers, with mosaic COX deficiency and ragged-red transformation. Suggested CL labels: *skeletal muscle fiber*, *extraocular muscle cell*, *lower motor neuron* where applicable.
- **Subcellular:** mitochondrial matrix, mitochondrial nucleoid/mtDNA, respiratory-chain inner-membrane complexes. Suggested GO cellular components: *mitochondrial matrix*, *mitochondrion*, *mitochondrial nucleoid*, *mitochondrial respiratory-chain complex*.
- **Lateralization:** ptosis and ophthalmoparesis are generally bilateral, although severity can be asymmetric. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3, ronchi2012nextgenerationsequencingreveals pages 8-9)

## 8. Temporal development

The documented PEO phenotype is usually **adult-onset, insidious, chronic, and slowly progressive**. Examples include onset around age 58 in a woman assessed at 69, onset at 69 in a man assessed at 80, and an eight-year progression in a 48-year-old woman. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)

A practical, nonvalidated staging description is: early ptosis/exercise symptoms; intermediate ophthalmoparesis and focal or limb-girdle weakness; advanced PEO-plus disease with bulbar, widespread muscle, respiratory, or neurologic involvement. No validated PEO4 staging system, progression-rate estimate, remission pattern, or intervention window exists. Spontaneous remission is not expected; surgery may improve ptosis but does not correct the mitochondrial defect.

The broader allelic spectrum ranges from neonatal liver failure to late-adult myopathy, implying strong genotype-, tissue-, and residual-function dependence, but reliable genotype–age prediction is unavailable. (elhattab1993deoxyguanosinekinasedeficiency pages 3-6, ronchi2012nextgenerationsequencingreveals pages 8-9)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. If both parents carry a pathogenic allele, each pregnancy has a 25% affected, 50% carrier, and 25% noncarrier probability; heterozygous carriers are generally asymptomatic. Prenatal and preimplantation genetic testing are possible after familial variants are established. (elhattab1993deoxyguanosinekinasedeficiency pages 12-15)

Penetrance for two definitively pathogenic alleles is probably high for some DGUOK phenotype but is not quantified for PEO4; expressivity is markedly variable and age dependent. There is no evidence of genetic anticipation. Germline mosaicism is theoretically possible but not documented as a material PEO4 contributor.

No PEO4-specific prevalence, incidence, carrier frequency, sex ratio, geographic concentration, or survival distribution is known. DGUOK variants represented **5.6%** of one selected adult multiple-mtDNA-deletion cohort; all DGUOK phenotypes together account for an estimated 15–20% of mtDNA-depletion syndromes, but that figure must not be transferred to PEO4. (ronchi2012nextgenerationsequencingreveals pages 1-2, elhattab1993deoxyguanosinekinasedeficiency pages 6-8)

Consanguinity increases the probability of homozygosity for rare recessive alleles. The c.255delA founder allele occurs in Druze ancestry in broader DGUOK deficiency. No PEO4-specific founder population has been demonstrated. (elhattab1993deoxyguanosinekinasedeficiency pages 12-15)

## 10. Diagnostics

### Recommended workflow

1. **Clinical recognition:** bilateral progressive ptosis/ophthalmoparesis with myopathy, exercise intolerance, dysphagia, or family structure compatible with recessive inheritance.
2. **Baseline assessment:** CK, lactate and pyruvate, glucose, liver profile, ECG/echocardiography where indicated, respiratory function, hearing/vision examination, and neurologic assessment. Normal lactate does not exclude disease. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3)
3. **Electrophysiology:** EMG may show a myopathic pattern; nerve-conduction testing is appropriate when neuropathy or motor-neuron disease is suspected.
4. **Genomic testing:** a mitochondrial-myopathy/mtDNA-maintenance panel including **DGUOK, POLG, TWNK, TK2, RRM2B, RNASEH1, MGME1, OPA1, MPV17, SUCLA2, SUCLG1**, or exome/genome sequencing with copy-number analysis. Confirmation requires two pathogenic/likely pathogenic DGUOK alleles in trans. (elhattab1993deoxyguanosinekinasedeficiency pages 3-6, elhattab1993deoxyguanosinekinasedeficiency pages 1-3, elhattab1993deoxyguanosinekinasedeficiency pages 6-8)
5. **Affected-tissue mtDNA analysis:** long-range PCR or validated NGS/Southern-blot methods for multiple deletions and quantitative copy-number testing. Muscle can be more informative than blood for late-onset mtDNA-maintenance disease.
6. **Muscle biopsy if genetics is inconclusive:** modified Gomori trichrome for ragged-red fibers, COX/SDH histochemistry, respiratory-chain enzymology, mtDNA deletion and depletion testing, and—research/functional setting—DGUOK activity, western blot, or RNA studies. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 9-10, ronchi2012nextgenerationsequencingreveals pages 7-8)

Across broader DGUOK deficiency, sequence analysis detects approximately **95%** of identifiable pathogenic variants and deletion/duplication analysis about **5%**; these are not PEO4-specific diagnostic yields. CMA, karyotyping, FISH, and repeat-expansion testing are not first-line unless another diagnosis is suspected. (elhattab1993deoxyguanosinekinasedeficiency pages 3-6)

### Differential diagnosis

Important alternatives include mtDNA single large-scale deletion syndromes; **POLG-, TWNK-, TK2-, RRM2B-, RNASEH1-, MGME1-, OPA1-, MPV17-, SUCLA2-, and SUCLG1-related** disorders; primary mtDNA point variants; oculopharyngeal muscular dystrophy; myasthenia gravis; congenital myasthenic syndromes; thyroid eye disease; and structural orbital/brainstem disease. Distinguishing evidence for DGUOK-PEO4 is biallelic DGUOK variants plus multiple mtDNA deletions and mitochondrial pathology in muscle. (ronchi2012nextgenerationsequencingreveals pages 1-2, elhattab1993deoxyguanosinekinasedeficiency pages 6-8)

There is no population or newborn screening program for PEO4. **Cascade testing** of relatives and reproductive carrier testing are appropriate after a molecular diagnosis. (elhattab1993deoxyguanosinekinasedeficiency pages 12-15)

## 11. Outcome and prognosis

No PEO4-specific five- or ten-year survival, mortality rate, or life-expectancy estimate exists. Adult PEO can progress slowly over decades, but morbidity includes restricted gaze, ptosis-related visual-field loss, exercise limitation, weakness, falls, dysphagia, aspiration risk, and reduced independence. Rare PEO-plus presentations may add lower-motor-neuron or cognitive disability. (ronchi2012nextgenerationsequencingreveals pages 3-4, ronchi2012nextgenerationsequencingreveals pages 2-3, ronchi2012nextgenerationsequencingreveals pages 9-10)

Recovery of lost extraocular motility or established mitochondrial myopathy is generally unlikely because current care does not correct DGUOK deficiency. Functional improvement can follow rehabilitation, assistive devices, swallowing intervention, or ptosis management. Prognostic biomarkers have not been validated; residual enzyme activity, deletion burden, age at onset, bulbar/respiratory involvement, and multisystem disease are plausible but unproven predictors.

Severe early mortality before age four and variable liver-transplant outcomes apply to **neonatal hepatocerebral DGUOK deficiency**, not automatically to PEO4. (elhattab1993deoxyguanosinekinasedeficiency pages 3-6, elhattab1993deoxyguanosinekinasedeficiency pages 6-8)

## 12. Treatment and real-world implementation

There is **no approved disease-modifying treatment specifically for DGUOK-PEO4** and no DGUOK-specific randomized trial was identified. Management is multidisciplinary and phenotype directed:

- **Ptosis/ophthalmic care:** lubrication for exposure, prisms where useful, and carefully selected ptosis repair or frontalis suspension, balancing visual benefit against exposure keratopathy. Suggested NCIT terms: *Ptosis Repair*, *Supportive Care*.
- **Rehabilitation:** graded, supervised aerobic/resistance activity as tolerated, physical and occupational therapy, fall prevention, and mobility aids. Suggested NCIT: *Physical Therapy*, *Occupational Therapy*.
- **Bulbar/nutrition:** speech-language and swallowing assessment, diet modification, aspiration prevention, and enteral support if necessary. Suggested NCIT: *Nutritional Support*, *Speech Therapy*.
- **Surveillance/treatment of complications:** pulmonary function and sleep/ventilatory assessment when weak; ECG and cardiac evaluation; endocrine, hearing, neurologic, and hepatic assessment according to phenotype.
- **Supplements:** coenzyme Q10, riboflavin, creatine, antioxidants, or commercial “mitochondrial cocktails” are sometimes used empirically, but no DGUOK-PEO4 response rate or controlled efficacy evidence exists.
- **Liver transplantation:** relevant only to carefully selected liver-predominant DGUOK deficiency with minimal neurologic disease; it does not correct extrahepatic DGUOK deficiency, and later muscle disease has occurred after transplantation. It is not a treatment for isolated PEO4. (ronchi2012nextgenerationsequencingreveals pages 9-10, elhattab1993deoxyguanosinekinasedeficiency pages 1-3)

Broad mitochondrial trials involving elamipretide, nicotinamide riboside/niacin, or vitamin/cofactor approaches cannot presently be considered evidence for DGUOK-PEO4. No validated pharmacogenomic rule, gene replacement, CRISPR therapy, RNA therapy, or cell therapy is clinically available for this disorder.

## 13. Prevention

**Primary prevention after conception is not currently possible.** No vaccine, prophylactic medication, or behavioral intervention prevents biallelic DGUOK disease.

Genetic counseling is the principal preventive strategy: confirm phase and pathogenicity, test parents and at-risk relatives, offer cascade carrier testing, and discuss prenatal diagnosis or preimplantation genetic testing for monogenic disease. Each pregnancy of two confirmed carriers has a 25% recurrence risk. (elhattab1993deoxyguanosinekinasedeficiency pages 12-15)

Secondary prevention consists of earlier recognition and molecular diagnosis before avoidable procedures or prolonged misdiagnosis. Tertiary prevention includes fall prevention, aspiration and exposure-keratopathy prevention, maintenance of mobility, and surveillance for respiratory, cardiac, endocrine, neurologic, or hepatic complications.

## 14. Other species and natural disease

DGUOK and mitochondrial purine salvage are evolutionarily conserved, but no naturally occurring companion-animal, livestock, or wildlife disease was identified that faithfully corresponds to human recessive PEO4. There is no zoonotic potential or cross-species transmission because the disorder is inherited, not infectious. Exact ortholog NCBI Gene and taxonomy identifiers should be obtained directly from current NCBI/Alliance records before structured ingestion.

## 15. Model organisms and experimental systems

No validated animal model was identified that reproduces the full adult DGUOK-PEO4 combination of ptosis/ophthalmoplegia, skeletal-muscle multiple mtDNA deletions, and slow progression. Available disease biology relies most strongly on **human muscle biopsy**, patient-derived molecular assays, and broader DGUOK-deficiency cellular systems. Useful models would include DGUOK-knockout or patient-variant cell lines, myotubes, iPSC-derived skeletal/extraocular muscle, and hepatocyte-like cells for the broader depletion phenotype.

Such systems can test nucleotide-pool imbalance, mtDNA copy number/deletions, OXPHOS, ATP production, membrane potential, and rescue by wild-type DGUOK or nucleoside manipulation. Their principal limitation is that cultured proliferating cells may depend more on cytosolic de novo dNTP synthesis and may not reproduce decades-long deletion accumulation in postmitotic extraocular muscle.

## Recent developments and expert assessment

The major **2023–2024 development** is not a new DGUOK-specific therapy, but improved recognition of mitochondrial CPEO as a genetically heterogeneous syndrome and wider use of sequencing integrated with affected-tissue mtDNA analysis. For this ultra-rare subtype, the decisive evidence remains the 2012 primary series. The current expert interpretation is therefore conservative: diagnose PEO4 only when clinical and muscle-mtDNA findings align with two appropriately classified DGUOK variants; avoid extrapolating infantile liver-disease prognosis to adult PEO; and regard supplements or broad mitochondrial trials as unproven for this genotype. (ronchi2012nextgenerationsequencingreveals pages 1-2, elhattab1993deoxyguanosinekinasedeficiency pages 3-6, elhattab1993deoxyguanosinekinasedeficiency pages 1-3)

### Key primary evidence quotation

The central paper’s conclusion can be summarized by its reported finding that recessive DGUOK mutations were identified in adults with “**mitochondrial myopathy with or without progressive external ophthalmoplegia**” and that these mutations impaired “**muscle DGUOK activity and protein stability**.” This is direct human clinical and functional evidence, whereas the finer chain from nucleotide imbalance to selective extraocular-muscle vulnerability remains partly inferred. (ronchi2012nextgenerationsequencingreveals pages 1-2)

## Knowledge gaps

No robust PEO4-specific natural-history cohort, incidence/prevalence study, penetrance estimate, validated phenotype frequency, quality-of-life study, longitudinal biomarker, modifier-gene analysis, epigenetic signature, single-cell/spatial dataset, faithful animal model, genotype-guided treatment, or interventional trial was identified. Consequently, database entries should preserve evidence provenance and distinguish **direct PEO4 evidence**, **broader DGUOK allelic-spectrum evidence**, and **general mitochondrial-disease extrapolation**.

References

1. (ronchi2012nextgenerationsequencingreveals pages 1-2): D. Ronchi, C. Garone, A. Bordoni, Purificación Gutiérrez Ríos, S. Calvo, M. Ripolone, M. Ranieri, M. Rizzuti, L. Villa, F. Magri, S. Corti, N. Bresolin, V. Mootha, M. Moggio, S. Dimauro, G. Comi, and M. Sciacco. Next-generation sequencing reveals dguok mutations in adult patients with mitochondrial dna multiple deletions. Brain : a journal of neurology, 135 Pt 11:3404-15, Nov 2012. URL: https://doi.org/10.1093/brain/aws258, doi:10.1093/brain/aws258. This article has 124 citations.

2. (ronchi2012nextgenerationsequencingreveals pages 9-10): D. Ronchi, C. Garone, A. Bordoni, Purificación Gutiérrez Ríos, S. Calvo, M. Ripolone, M. Ranieri, M. Rizzuti, L. Villa, F. Magri, S. Corti, N. Bresolin, V. Mootha, M. Moggio, S. Dimauro, G. Comi, and M. Sciacco. Next-generation sequencing reveals dguok mutations in adult patients with mitochondrial dna multiple deletions. Brain : a journal of neurology, 135 Pt 11:3404-15, Nov 2012. URL: https://doi.org/10.1093/brain/aws258, doi:10.1093/brain/aws258. This article has 124 citations.

3. (ronchi2012nextgenerationsequencingreveals pages 7-8): D. Ronchi, C. Garone, A. Bordoni, Purificación Gutiérrez Ríos, S. Calvo, M. Ripolone, M. Ranieri, M. Rizzuti, L. Villa, F. Magri, S. Corti, N. Bresolin, V. Mootha, M. Moggio, S. Dimauro, G. Comi, and M. Sciacco. Next-generation sequencing reveals dguok mutations in adult patients with mitochondrial dna multiple deletions. Brain : a journal of neurology, 135 Pt 11:3404-15, Nov 2012. URL: https://doi.org/10.1093/brain/aws258, doi:10.1093/brain/aws258. This article has 124 citations.

4. (elhattab1993deoxyguanosinekinasedeficiency pages 3-6): AW El-Hattab and F Scaglia. Deoxyguanosine kinase deficiency. Unknown journal, 1993.

5. (elhattab1993deoxyguanosinekinasedeficiency pages 1-3): AW El-Hattab and F Scaglia. Deoxyguanosine kinase deficiency. Unknown journal, 1993.

6. (ronchi2012nextgenerationsequencingreveals pages 8-9): D. Ronchi, C. Garone, A. Bordoni, Purificación Gutiérrez Ríos, S. Calvo, M. Ripolone, M. Ranieri, M. Rizzuti, L. Villa, F. Magri, S. Corti, N. Bresolin, V. Mootha, M. Moggio, S. Dimauro, G. Comi, and M. Sciacco. Next-generation sequencing reveals dguok mutations in adult patients with mitochondrial dna multiple deletions. Brain : a journal of neurology, 135 Pt 11:3404-15, Nov 2012. URL: https://doi.org/10.1093/brain/aws258, doi:10.1093/brain/aws258. This article has 124 citations.

7. (elhattab1993deoxyguanosinekinasedeficiency pages 6-8): AW El-Hattab and F Scaglia. Deoxyguanosine kinase deficiency. Unknown journal, 1993.

8. (OpenTargets Search: Progressive external ophthalmoplegia with mitochondrial DNA deletions autosomal recessive 4): Open Targets Query (Progressive external ophthalmoplegia with mitochondrial DNA deletions autosomal recessive 4, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (elhattab1993deoxyguanosinekinasedeficiency pages 12-15): AW El-Hattab and F Scaglia. Deoxyguanosine kinase deficiency. Unknown journal, 1993.

10. (ronchi2012nextgenerationsequencingreveals pages 3-4): D. Ronchi, C. Garone, A. Bordoni, Purificación Gutiérrez Ríos, S. Calvo, M. Ripolone, M. Ranieri, M. Rizzuti, L. Villa, F. Magri, S. Corti, N. Bresolin, V. Mootha, M. Moggio, S. Dimauro, G. Comi, and M. Sciacco. Next-generation sequencing reveals dguok mutations in adult patients with mitochondrial dna multiple deletions. Brain : a journal of neurology, 135 Pt 11:3404-15, Nov 2012. URL: https://doi.org/10.1093/brain/aws258, doi:10.1093/brain/aws258. This article has 124 citations.

11. (ronchi2012nextgenerationsequencingreveals pages 2-3): D. Ronchi, C. Garone, A. Bordoni, Purificación Gutiérrez Ríos, S. Calvo, M. Ripolone, M. Ranieri, M. Rizzuti, L. Villa, F. Magri, S. Corti, N. Bresolin, V. Mootha, M. Moggio, S. Dimauro, G. Comi, and M. Sciacco. Next-generation sequencing reveals dguok mutations in adult patients with mitochondrial dna multiple deletions. Brain : a journal of neurology, 135 Pt 11:3404-15, Nov 2012. URL: https://doi.org/10.1093/brain/aws258, doi:10.1093/brain/aws258. This article has 124 citations.

## Artifacts

- [Edison artifact artifact-00](Progressive_External_Ophthalmoplegia_With_Mitochondrial_DNA_Deletions_Autosomal_Recessive_4-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 1 |
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
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014899` (5 mentions) - the report calls it "if available"; MONDO calls it **progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 4**
