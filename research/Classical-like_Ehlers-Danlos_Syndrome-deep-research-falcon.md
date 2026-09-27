---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T17:06:09.510573'
end_time: '2026-09-16T17:19:35.291861'
duration_seconds: 805.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Classical-like Ehlers-Danlos Syndrome
  mondo_id: MONDO:0011670
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
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 53
  verified: 50
  not_found: 2
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.038
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0011670
    reported_labels:
    - if available
    ontology_label: Ehlers-Danlos syndrome due to tenascin-X deficiency
  - term_id: HP:0001634
    reported_labels:
    - 'clEDS2: 4/11 in the 2023 aggregate'
    ontology_label: Mitral valve prolapse
  unresolved_terms:
  - HP:0001811
  - UBERON:0000216
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Classical-like_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Classical-like Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0011670 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Classical-like Ehlers-Danlos Syndrome** covering all of the
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
- **Disease Name:** Classical-like Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0011670 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Classical-like Ehlers-Danlos Syndrome** covering all of the
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


# Classical-like Ehlers–Danlos syndrome: comprehensive disease-characteristics report

**Scope and evidence date.** This report covers **classical-like Ehlers–Danlos syndrome (clEDS)** as two autosomal-recessive extracellular-matrix disorders: **TNXB-related clEDS type 1 (clEDS1)** and **AEBP1-related clEDS type 2 (clEDS2)**. It distinguishes complete biallelic TNXB deficiency from heterozygous TNXB-associated hypermobility and from **CAH-X**, the CYP21A2–TNXB contiguous-gene disorder. Evidence is current through the retrieved 2024 literature. Because both diseases are ultra-rare, most frequencies derive from cohorts of 9–24 individuals and should not be interpreted as population estimates.

| Feature | clEDS1 / **TNXB** | clEDS2 / **AEBP1** | Evidence notes |
|---|---|---|---|
| Molecular definition | Biallelic pathogenic **TNXB** variants causing complete tenascin-X deficiency | Biallelic pathogenic **AEBP1** variants causing loss or dysfunction of aortic carboxypeptidase-like protein (ACLP) | Both are autosomal-recessive monogenic extracellular-matrix disorders; TNXB haploinsufficiency and CAH-X are related but distinct entities (gensemer2021hypermobileehlers‐danlossyndromes pages 24-29, kosho2024editorialehlersdanlossyndrome pages 2-2) |
| Protein function | Tenascin-X is an extracellular-matrix glycoprotein that regulates collagen deposition and matrix organization and interacts with collagen fibrils/decorin | ACLP binds several fibrillar collagens through its discoidin domain, enhances collagen polymerization, and contributes to development, repair, fibrosis, fibroblast proliferation, and collagen-producing-cell differentiation | Human and model evidence supports disrupted collagen-rich matrix organization rather than a primary collagen-gene defect (blackburn2018biallelicalterationsin pages 4-5, pliegoarreaga2024jointhypermobilitysyndrome pages 6-8) |
| Core phenotype | Generalized joint hypermobility, hyperextensible skin, easy bruising, and generalized tissue fragility | Joint hypermobility **11/11**, skin hyperextensibility **11/11**, easy bruising **10/11** in the 2023 aggregated series | clEDS2 percentages derive from only 11 reported individuals and are vulnerable to ascertainment bias (sugiura2023analysisofreferrals pages 26-30, kosho2024editorialehlersdanlossyndrome pages 2-2) |
| Scarring distinction | Classically resembles classical EDS but usually lacks the typical atrophic scars of COL5A1/COL5A2-related classical EDS | Atrophic scarring occurred in **9/11**, so absence of atrophic scars is not a reliable clEDS2 discriminator | The “classical-like without atrophic scarring” rule applies most strongly to TNXB-related clEDS1, not uniformly to clEDS2 (sugiura2023analysisofreferrals pages 26-30) |
| Additional phenotype clues | Muscle weakness, myalgia, fatigability, edema without cardiac failure, distal joint changes, and possible neuropathy; in one TNX-deficient dataset, mild–moderate weakness was **80%**, reduced vibration sense **60%**, axonal polyneuropathy **40%**, and mild myopathic biopsy findings **20%** | Hair loss or thinning was reported in **6/11** and may be a useful distinguishing clue; osteoporosis, poor wound healing, redundant skin, and marfanoid features have also been described | TNXB neuromuscular percentages came from a small EDS/TNX-deficiency cohort; the clEDS2 hair-loss observation requires confirmation in larger series (brady2017theehlers–danlossyndromes pages 6-7, kosho2024editorialehlersdanlossyndrome pages 2-2) |
| Vascular concerns | Easy bruising and hematomas are prominent; severe arterial events have been reported but are not sufficiently quantified for precise risk estimates | Among 11 reported individuals, **2/11** had arterial aneurysm and/or dissection; reported findings include vertebral-artery dissection, splenic-artery dilatation, arterial tortuosity, and an aortic-root aneurysm requiring surgery | Cardiovascular surveillance has been proposed for clEDS2, but evidence remains case-series level rather than guideline-grade (kosho2024editorialehlersdanlossyndrome pages 2-2) |
| Cardiac findings | Valve or structural cardiac abnormalities can occur, especially in the distinct CAH-X spectrum, but clEDS1-specific frequencies are uncertain | Mitral-valve prolapse was reported in **4/11** | Do not transfer CAH-X cardiac-frequency estimates directly to biallelic TNXB clEDS1 (sugiura2023analysisofreferrals pages 26-30, kosho2024editorialehlersdanlossyndrome pages 2-2) |
| Gastrointestinal and pelvic-floor concerns | A 2024 summary of a nine-patient TNXB cohort reported gastrointestinal complications in all patients, including perforation, diverticulitis, bleeding, obstruction, rectal/anal prolapse, and gallstones | Potentially serious bowel complications have been emphasized in recent reports, but robust frequencies are unavailable | The clEDS1 observation is from a highly selected small cohort and should not be interpreted as population prevalence (kosho2024editorialehlersdanlossyndrome pages 1-2, kosho2024editorialehlersdanlossyndrome pages 2-2) |
| Variant spectrum and functional consequence | Missense, nonsense, frameshift, splice, deletion, and TNXA-derived/chimeric alleles occur; disease-producing biallelic variants generally cause absent or profoundly deficient tenascin-X | Reported pathogenic alleles include nonsense, frameshift, splice-site, and damaging missense variants; demonstrated consequences include nonsense-mediated decay, absent ACLP, and impaired collagen assembly | More than 75% of patients in one recent TNXB cohort reportedly carried TNXA-derived variation; AEBP1 functional nullizygosity is supported by RNA/protein studies (kosho2024editorialehlersdanlossyndrome pages 1-2, blackburn2018biallelicalterationsin pages 4-5, brady2017theehlers–danlossyndromes pages 3-4) |
| Testing pitfalls | Technically difficult because **TNXB** lies in the complex RCCX locus and has a highly homologous pseudogene, **TNXA**; sequencing alone may miss exon conversions, TNXA/TNXB chimeras, or copy-number changes | Standard sequencing and deletion/duplication analysis are generally applicable, but missense variants may require segregation and functional evidence | TNXB testing should use validated locus-aware methods and copy-number/chimera analysis; long-read or genome/RNA approaches may resolve unsolved cases (kim2023molecularbasisand pages 10-10, malfait2020theehlers–danlossyndromes pages 15-16) |
| Important diagnostic distinction | Complete biallelic TNXB deficiency causes clEDS1; heterozygous TNXB deficiency may produce a hypermobility phenotype, while a CYP21A2–TNXB contiguous rearrangement produces **CAH-X** | AEBP1-related disease is not CAH-X and does not inherently cause congenital adrenal hyperplasia | Conflating these entities can distort inheritance, phenotype, and recurrence-risk counseling (gensemer2021hypermobileehlers‐danlossyndromes pages 24-29, sugiura2023analysisofreferrals pages 26-30, brady2017theehlers–danlossyndromes pages 3-4) |
| Mechanistic pathology | Tenascin-X deficiency reduces collagen density and alters matrix and elastic-fiber organization; TNX-null mouse skin has approximately **30% less collagen** despite relatively preserved fibril size and shape | ACLP deficiency impairs binding/polymerization of fibrillar collagen; patient skin shows reduced dermal collagen and ragged abnormal fibrils | Evidence includes human skin/fibroblasts, biochemical collagen-polymerization assays, and knockout mice (blackburn2018biallelicalterationsin pages 4-5, pliegoarreaga2024jointhypermobilitysyndrome pages 6-8) |
| Experimental models | **Tnxb−/− mouse:** reduced collagen deposition and mechanical allodynia; allodynia responded to gabapentin and a μ-opioid agonist but not indomethacin | **Aebp1−/− mouse:** abnormal/delayed wound repair associated with impaired fibroblast proliferation; patient-derived fibroblasts provide direct functional models | Models reproduce selected ECM, wound-healing, or pain mechanisms but do not establish the full human multisystem natural history (blackburn2018biallelicalterationsin pages 4-5, kosho2024editorialehlersdanlossyndrome pages 2-2, gensemer2021hypermobileehlers‐danlossyndromes pages 66-70) |
| Therapy status | No approved molecularly targeted, gene, RNA, or cell therapy; care is supportive and complication-directed | No approved molecularly targeted, gene, RNA, or cell therapy; care is supportive and complication-directed | Current management relies on multidisciplinary rehabilitation, pain treatment, tissue-protection and wound precautions, cardiovascular assessment, and genetic counseling; recommendations are largely extrapolated from broader EDS care (malfait2020theehlers–danlossyndromes pages 15-16, malfait2014theehlersdanlossyndrome. pages 10-12) |
| Evidence maturity | Larger clinical experience than clEDS2, but still ultra-rare with no population-level natural-history estimates | Only 11 individuals were aggregated in the 2023 report; phenotype and complication frequencies remain provisional | Neither subtype has reliable incidence, prevalence, survival, penetrance, treatment-response, or quality-of-life statistics (kosho2024editorialehlersdanlossyndrome pages 1-2, kosho2024editorialehlersdanlossyndrome pages 2-2) |


*Table: Database-ready comparison of TNXB-related clEDS1 and AEBP1-related clEDS2, emphasizing molecular definitions, phenotype differences, testing pitfalls, mechanisms, models, and evidence limitations.*

## 1. Disease information

### Definition

clEDS is a group of inherited connective-tissue disorders characterized by generalized joint hypermobility, hyperextensible skin, easy bruising and generalized tissue fragility. The adjective “classical-like” reflects overlap with COL5A1/COL5A2-related classical EDS. In **TNXB-related clEDS1**, the classic distinction is the usual absence of the characteristic atrophic scars of classical EDS; this distinction is less reliable in **AEBP1-related clEDS2**, in which atrophic scars occurred in 9/11 reported individuals. Biallelic TNXB variants cause complete tenascin-X deficiency, whereas biallelic AEBP1 variants impair aortic carboxypeptidase-like protein (ACLP) and collagen assembly. (gensemer2021hypermobileehlers‐danlossyndromes pages 24-29, sugiura2023analysisofreferrals pages 26-30, kosho2024editorialehlersdanlossyndrome pages 2-2)

### Identifiers and synonyms

* **MONDO:** the user-supplied **MONDO:0011670** corresponds to classical-like EDS in the target knowledge base; subtype-specific MONDO mappings should be checked against the current MONDO release before production ingestion.
* **OMIM:** TNXB-related classical-like EDS is commonly represented as **Ehlers–Danlos syndrome, classical-like, 1 / EDSCL1**; AEBP1-related disease as **classical-like EDS type 2 / EDSCL2**. Database release verification is recommended rather than hard-coding unverified numeric records.
* **Orphanet:** generally indexed under classical-like EDS/TNX-deficient EDS; subtype-specific records may vary by release.
* **ICD-10:** no reliably specific clEDS code; usually grouped under **Q79.6, Ehlers–Danlos syndrome**.
* **ICD-11:** grouped within hereditary connective-tissue disorders/Ehlers–Danlos syndromes; no subtype-specific billing code was established in the retrieved literature.
* **MeSH:** **Ehlers-Danlos Syndrome**.
* **Synonyms:** classical-like EDS; clEDS; TNX-deficient EDS; tenascin-X-deficient EDS; EDS due to TNXB deficiency; clEDS type 1; AEBP1-related EDS; ACLP-deficiency EDS; clEDS type 2.

The evidence summarized here is **aggregated disease-level literature**, including clinical cohorts, pedigrees, reviews and experimental models—not individual EHR data.

## 2. Etiology

### Causal factors

* **clEDS1:** germline biallelic pathogenic variants in **TNXB**, causing absent or severely reduced tenascin-X. Reported classes include nonsense, frameshift, missense, splice, deletion and TNXA-derived conversion/chimeric alleles. Among 24 reported people with complete TNX deficiency, 19 from 15 families had a molecular diagnosis; variants were distributed across TNXB. (brady2017theehlers–danlossyndromes pages 3-4)
* **clEDS2:** germline biallelic pathogenic variants in **AEBP1**, generally causing ACLP loss of function or impairment of its collagen-binding/polymerization activity. The foundational study identified four people from three families with compound-heterozygous or homozygous frameshift, nonsense and splice variants. (malfait2020theehlers–danlossyndromes pages 22-22, blackburn2018biallelicalterationsin pages 4-5)

### Genetic and environmental risk factors

The principal risk is inheritance of two pathogenic alleles. For two carrier parents, each pregnancy has a **25% affected, 50% carrier and 25% unaffected/non-carrier** probability. Consanguinity increases the probability that both parents carry the same rare allele; runs of homozygosity supported a shared ancestral AEBP1 segment in one family. No validated susceptibility loci, modifier genes, genetic anticipation or reproducible founder effect has been established.

No toxin, pathogen, diet, smoking pattern or occupational exposure causes clEDS. Mechanical load, trauma, surgery and high-impact activity can **modify manifestations** by precipitating dislocation, bruising, pain, poor wound healing or tissue rupture, but they do not create the Mendelian disorder. Age, sex and lifestyle may influence joint-hypermobility expression across EDS, but clEDS-specific gene–environment estimates are unavailable.

### Protective factors and gene–environment interaction

No protective allele or pharmacological prevention of disease onset is known. Low-impact conditioning, joint stabilization, avoidance of collision sports and skin protection plausibly reduce secondary injury; these are complication-prevention measures rather than molecular protection. Formal TNXB/AEBP1 gene–environment interaction studies were not identified.

## 3. Phenotypes

### Major manifestations and suggested HPO terms

| Manifestation | Type, onset/course and reported frequency | Suggested HPO term |
|---|---|---|
| Generalized joint hypermobility | Clinical sign; often recognizable in childhood; may diminish with age while instability and pain persist. clEDS2: 11/11. | **HP:0001382** Joint hypermobility; **HP:0002761** Generalized joint hypermobility |
| Joint instability, subluxation/dislocation | Sign/symptom; recurrent and mechanically triggered; severity variable. | **HP:0001373** Joint dislocation; **HP:0030860** Joint subluxation |
| Skin hyperextensibility | Physical sign; usually longstanding/congenital predisposition. clEDS2: 11/11. | **HP:0000974** Hyperextensible skin |
| Easy bruising/ecchymoses | Sign; lifelong and episodic after minor trauma. clEDS2: 10/11. | **HP:0000978** Bruising susceptibility |
| Atrophic/abnormal scarring | Usually absent as a defining feature in clEDS1, but present in 9/11 clEDS2 cases. | **HP:0001075** Atrophic scars; **HP:0001058** Poor wound healing |
| Soft, redundant or doughy skin | Physical manifestation; variable. | **HP:0000977** Soft skin; **HP:0001582** Redundant skin |
| Chronic musculoskeletal pain, myalgia and fatigue | Symptoms; often become more limiting with age and recurrent injury. | **HP:0003326** Myalgia; **HP:0012531** Pain; **HP:0012378** Fatigue |
| Muscle weakness | Sign/symptom; mild–moderate weakness occurred in 80% of one TNX-deficient neuromuscular cohort. | **HP:0001324** Muscle weakness |
| Peripheral sensory/nerve abnormalities | Reduced vibration sense 60%, axonal polyneuropathy 40%, and mild myopathic biopsy findings 20% in one small TNX-deficient cohort. | **HP:0000763** Sensory neuropathy; **HP:0003477** Peripheral axonal neuropathy |
| Edema without cardiac failure | Characteristic minor feature described particularly in clEDS1; frequency uncertain. | **HP:0000969** Edema |
| Foot/hand deformity | Reported features include brachydactyly, acrogeric appearance, pes planus and hallux valgus; variable. | **HP:0001156**, **HP:0001811**, **HP:0001760** |
| Hair loss/thinning | Emerging clEDS2 feature: 6/11 reported individuals. | **HP:0001596** Alopecia |
| Osteopenia/osteoporosis | Particularly reported in AEBP1 disease; quantitative frequency unresolved. | **HP:0000938** Osteopenia; **HP:0000939** Osteoporosis |
| Arterial aneurysm/dissection/tortuosity | Rare but potentially severe; clEDS2 arterial aneurysm and/or dissection in 2/11. | **HP:0002617**, **HP:0005294**, **HP:0005116** |
| Mitral-valve prolapse | clEDS2: 4/11 in the 2023 aggregate. | **HP:0001634** |
| Gastrointestinal/pelvic-floor complications | Diverticulitis, bleeding, obstruction, perforation, prolapse and gallstones were reported in a selected nine-person TNXB cohort; all nine had some GI complication. | **HP:0002037**, **HP:0002027**, **HP:0002012**, **HP:0002035**, **HP:0001085** |

The clEDS2 frequencies come from only 11 reported individuals—six females and five males—and are vulnerable to publication and ascertainment bias. Cardiovascular surveillance was proposed because 2/11 had aneurysm/dissection, not because a population-level risk has been established. (kosho2024editorialehlersdanlossyndrome pages 1-2, kosho2024editorialehlersdanlossyndrome pages 2-2, brady2017theehlers–danlossyndromes pages 6-7)

### Quality of life

Pain, recurrent instability, weakness, fatigue, neuropathy, bruising and fear of tissue injury can limit mobility, work, self-care and participation. EDS-wide research shows pain can be severe and associated with functional impairment, but no clEDS-specific EQ-5D, SF-36, PROMIS, disability-weight or treatment-response dataset was identified. Thus, QoL effects are clinically credible but not numerically quantifiable for these subtypes.

## 4. Genetic and molecular information

### Genes and proteins

* **TNXB**, chromosome 6p21.3, encodes tenascin-X, a large extracellular-matrix glycoprotein involved in collagen deposition, fibril/matrix organization and interactions with decorin. Suggested annotations: **GO:0031012 extracellular matrix**, **GO:0005201 extracellular matrix structural constituent**, and collagen-fibril organization processes.
* **AEBP1** encodes ACLP, an ECM-associated protein expressed in dermis, vasculature and bone. ACLP binds fibrillar collagens through a discoidin domain, enhances collagen polymerization and participates in fibroblast proliferation, repair, fibrosis and differentiation of collagen-producing mesenchymal cells. (blackburn2018biallelicalterationsin pages 4-5, pliegoarreaga2024jointhypermobilitysyndrome pages 6-8)

### Representative pathogenic variants

AEBP1 examples include c.1470delC, c.1743C>A (p.Cys581*), c.1320_1326del (p.Arg440Serfs*3), c.1630+1G>A, c.917dup (p.Tyr306*), c.821del (p.Pro274Leufs*18), c.2248T>C (p.Trp750Arg), c.1012G>T (p.Glu338*) and c.1930C>T (p.Arg644*). The c.1320_1326del allele underwent nonsense-mediated decay with no detectable ACLP, while c.1470delC disrupted the collagen-binding domain. (blackburn2018biallelicalterationsin pages 4-5)

TNXB pathogenic alleles span multiple classes. Interpretation is complicated by the homologous **TNXA pseudogene** and RCCX structural variation. TNXA-derived changes reportedly accounted for more than 75% of individuals in one recent nine-person TNXB cohort. (kosho2024editorialehlersdanlossyndrome pages 1-2, kim2023molecularbasisand pages 10-10)

These are **germline** diseases. Somatic variants are not an etiologic category. Pathogenic alleles are expected to be absent or extremely rare in population databases; exact gnomAD frequencies must be retrieved per HGVS allele and ancestry rather than generalized. A VUS does not confirm diagnosis without segregation, phenotype and preferably RNA/protein or other functional support.

### Functional consequence and other genomic mechanisms

The dominant disease mechanism for both types is **biallelic loss of function**, although damaging missense alleles may impair binding, folding or secretion. Large RCCX deletions and gene conversions are particularly relevant to TNXB. No recurrent aneuploidy, translocation, inversion, epigenetic signature or validated modifier gene is established. No disease-specific DNA-methylation episignature was identified.

### Critical distinction: clEDS1 versus CAH-X

Complete biallelic TNXB deficiency produces recessive clEDS1. Heterozygous TNXB deficiency can produce a variably penetrant hypermobility phenotype. **CAH-X** results when RCCX rearrangement disrupts CYP21A2 and TNXB, combining congenital adrenal hyperplasia with an EDS/hypermobility phenotype. It must not be assigned the phenotype frequencies or inheritance model of biallelic clEDS1. In one CAH-X study, 12/13 individuals had EDS features; separate CAH cohorts reported 8.5–15% CAH-X estimates, which are not clEDS prevalence estimates. (gensemer2021hypermobileehlers‐danlossyndromes pages 24-29, sugiura2023analysisofreferrals pages 26-30, brady2017theehlers–danlossyndromes pages 6-7)

## 5. Environmental information

No infectious agent, radiation, toxin, pollutant, nutritional deficiency or lifestyle exposure is causal. Relevant environmental modifiers are biomechanical: repeated high-impact loading can exacerbate joint injury; minor trauma can provoke bruising or skin injury; invasive procedures can expose tissue fragility. Smoking cessation and balanced nutrition are reasonable for general wound, bone and cardiovascular health, but no clEDS-specific effect size exists. Vaccination follows routine schedules; clEDS is neither infectious nor immunodeficient.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic TNXB pathogenic variants lead to** absent/profoundly deficient tenascin-X **or** biallelic AEBP1 variants lead to absent/dysfunctional ACLP.
2. **Loss of tenascin-X leads to** reduced collagen deposition and disturbed collagen–decorin/elastic-microfibril organization; **loss of ACLP leads to** impaired fibrillar-collagen binding and polymerization.
3. These abnormalities **result in** reduced matrix density, abnormal fibril architecture and defective fibroblast-mediated matrix maintenance/wound repair.
4. Defective dermal ECM **leads to** hyperextensible/soft skin, easy bruising and abnormal or delayed healing.
5. Defective ligament, tendon, fascia and periarticular ECM **leads to** joint laxity, recurrent subluxation/dislocation and altered mechanical loading.
6. Recurrent instability and altered mechanosensory input **result in** chronic pain, fatigue, weakness and functional impairment; neuropathic contributions are demonstrated in Tnxb-null mouse allodynia but remain partly inferred in humans.
7. **Branch—vascular/valvular ECM weakness leads to** mitral-valve prolapse, arterial tortuosity, aneurysm or dissection in a minority, with risk best documented but still imprecise in clEDS2.
8. **Branch—gastrointestinal and pelvic connective-tissue weakness leads to** diverticular disease, bleeding, obstruction, perforation or prolapse in selected patients; general frequency remains uncertain.

### Mechanistic detail

TNX-null mouse skin has relatively preserved fibril dimensions but reduced fibril density and approximately **30% lower collagen content**, indicating a defect in matrix deposition/organization rather than a primary fibrillar-collagen sequence defect. Human TNXB disease also shows abnormal elastic fibers and microfibrils. (gensemer2021hypermobileehlers‐danlossyndromes pages 24-29, pliegoarreaga2024jointhypermobilitysyndrome pages 6-8)

ACLP directly enhanced collagen polymerization and bound several fibrillar collagens in the foundational biochemical work. Patient skin showed decreased dermal collagen and ragged abnormal fibrils; patient fibroblast RNA/protein experiments demonstrated nonsense-mediated decay and ACLP absence for a null allele. An exact abstract statement from Blackburn et al. is: **“These studies support the conclusion that bi-allelic pathogenic variants in AEBP1 are the cause of this autosomal-recessive EDS subtype.”** (Published April 2018; DOI/URL: https://doi.org/10.1016/j.ajhg.2018.02.018.) (blackburn2018biallelicalterationsin pages 4-5)

Suggested **GO biological processes** include extracellular-matrix organization (**GO:0030198**), collagen-fibril organization (**GO:0030199**), wound healing (**GO:0042060**), regulation of cell adhesion and response to mechanical stimulus. Suggested **cell types** include dermal fibroblast (**CL:0002620**), tendon fibroblast/tenocyte, ligament fibroblast, vascular smooth-muscle cell (**CL:0000359**), endothelial cell (**CL:0000115**), valvular interstitial cell and mesenchymal stromal cell (**CL:0000134**). Suggested compartments are extracellular matrix (**GO:0031012**), collagen-containing extracellular matrix (**GO:0062023**) and extracellular region (**GO:0005576**).

No clEDS-specific immune, metabolic, mitochondrial, autophagy or canonical Wnt/MAPK/mTOR/PI3K-AKT mechanism is established. No validated clEDS-specific metabolomic, lipidomic, single-cell, spatial-transcriptomic, integrated multi-omic or CRISPR-screen signature was identified. Broad EDS fibroblast transcriptomics should not be annotated as clEDS-specific evidence.

## 7. Anatomical structures affected

* **Primary:** skin/dermis, ligaments, tendons, joint capsules, fascia and skeletal-muscle connective tissue.
* **Secondary/variable:** peripheral nerves, bone, heart valves, arterial wall, gastrointestinal wall and pelvic-floor support.
* **Suggested UBERON:** skin of body (**UBERON:0002097**), dermis (**UBERON:0002067**), ligament (**UBERON:0000216**), tendon (**UBERON:0000043**), joint (**UBERON:0000982**), skeletal muscle (**UBERON:0001134**), artery (**UBERON:0001637**), heart valve (**UBERON:0002139**), gastrointestinal tract (**UBERON:0005409**).
* **Subcellular:** secretory pathway may be relevant for synthesis/secretion, but the disease-defining compartment is the extracellular/collagen-containing matrix.

Manifestations are generally bilateral/systemic rather than characteristically unilateral, although individual dislocations, aneurysms or dissections can be focal.

## 8. Temporal development

The molecular defect is congenital and lifelong. Skin hyperextensibility, bruising and joint laxity often become evident in childhood, but diagnosis may be delayed into adulthood. Joint hypermobility may decrease with aging, while pain, weakness, degenerative joint consequences and vascular/GI complications may emerge or accumulate later. The course is chronic and variable, not relapsing-remitting; injury-related exacerbations are episodic. There are no validated disease stages, remission criteria or progression-rate estimates.

Critical periods include childhood for joint-protective conditioning; before surgery or pregnancy for individualized tissue-fragility planning; and adulthood for cardiovascular and GI review where indicated. A chronic vertebral-artery dissection and other vascular abnormalities were detected at age 63 in one clEDS2 individual, demonstrating that clinically important complications may present late. (kosho2024editorialehlersdanlossyndrome pages 2-2)

## 9. Inheritance and population

Both types are **autosomal recessive**. Penetrance for true biallelic loss-of-function disease appears high, but precise estimates cannot be calculated; expressivity is variable. There is no evidence of anticipation. Germline mosaicism is theoretically possible but not quantified. Heterozygous TNXB relatives may show hypermobility with sex-dependent/incomplete expression, but this is not equivalent to recessive clEDS1. In one family study, all 20 heterozygous relatives had reduced serum TNX, 17 carried truncating variants and 9 had generalized joint hypermobility. (brady2017theehlers–danlossyndromes pages 6-7)

No reliable prevalence, incidence, carrier frequency, sex ratio, ancestry enrichment or geographic distribution exists. The 2023 clEDS2 literature contained only 11 recognized individuals—six female and five male—too few for demographic inference. clEDS is appropriately considered ultra-rare. (kosho2024editorialehlersdanlossyndrome pages 2-2)

## 10. Diagnostics

### Clinical assessment

Clinical examination should document Beighton score/generalized hypermobility, age-adjusted joint range, instability/dislocations, skin extensibility and texture, bruising, scars and healing, edema, hand/foot morphology, pain, muscle strength, neurologic findings, hernias/prolapse and cardiovascular/GI history. The 2024 expert review states that massively parallel **gene-panel testing is the current gold standard** for confirming monogenic EDS, while history, pedigree and examination remain essential. (Published November 2024; DOI: https://doi.org/10.1515/medgen-2024-2060.)

### Genetic-testing algorithm

1. Use an EDS/heritable-connective-tissue panel containing at least **TNXB, AEBP1, COL5A1, COL5A2, COL3A1, PLOD1, FKBP14, ADAMTS2, CHST14, DSE, SLC39A13, B4GALT7, B3GALT6, SLC2A10, FLNA** and other phenotype-directed genes.
2. Ensure the assay explicitly validates **TNXB** coverage against TNXA and includes deletion/duplication, conversion and TNXA/TNXB chimera analysis. Ordinary short-read pipelines can mis-map this locus.
3. If negative but suspicion remains high, consider locus-specific long-range PCR, RNA studies, WES/WGS or long-read sequencing. WES is useful for AEBP1 and unsolved heterogeneous presentations, but may be inadequate alone for complex TNXB structural alleles. (kim2023molecularbasisand pages 10-10, malfait2020theehlers–danlossyndromes pages 15-16)
4. Confirm phase for two variants and perform parental segregation. Apply ACMG/AMP criteria; do not use a VUS as definitive diagnosis.
5. Once familial variants are known, use targeted testing for relatives, prenatal diagnosis or preimplantation testing.

Serum TNX can be absent in biallelic TNXB disease, but the assay is not widely available. Skin biopsy/electron microscopy may show reduced collagen density, abnormal fibrils or elastic/microfibril abnormalities; findings are supportive, not independently diagnostic. Routine biochemical, circulating, metabolomic or liquid-biopsy biomarkers do not exist. (brady2017theehlers–danlossyndromes pages 3-4, malfait2020theehlers–danlossyndromes pages 15-16)

### Differential diagnosis

* **Classical EDS:** COL5A1/COL5A2; typical papyraceous/atrophic scars strongly favor classical EDS over clEDS1, but not necessarily clEDS2.
* **Hypermobile EDS/HSD:** no established monogenic test for typical hEDS; skin and bruising are usually less pronounced. Biallelic TNXB or AEBP1 findings establish a different diagnosis.
* **Vascular EDS:** COL3A1; translucent skin, characteristic facial/acral findings and greater spontaneous arterial/organ rupture risk.
* **Kyphoscoliotic EDS:** PLOD1/FKBP14; congenital hypotonia and progressive kyphoscoliosis.
* **Other rare EDS types:** periodontal, musculocontractural, dermatosparaxis, arthrochalasia and spondylodysplastic forms.
* **Marfan/Loeys–Dietz syndromes:** aortic and skeletal pattern with FBN1 or TGF-β-pathway genes.
* **Cutis laxa, FLNA-related disorders, neuromuscular disease and bleeding disorders.**
* **CAH-X:** investigate adrenal/androgen phenotype and CYP21A2–TNXB rearrangement; it is not ordinary clEDS1.

Population or newborn screening is not recommended. **Cascade testing** is appropriate after molecular diagnosis.

## 11. Outcome and prognosis

No five- or ten-year survival, life-expectancy or disease-specific mortality estimate is available. Many affected people survive into later adulthood, but this does not establish normal life expectancy. Major morbidity arises from chronic pain, instability, fatigue, weakness, poor healing, bruising, neuropathy and occasional serious arterial or bowel complications. Recovery from the constitutional matrix disorder is not expected; functional gains and injury reduction are possible with rehabilitation and prevention.

Potential adverse prognostic features include recurrent major dislocations, severe pain/deconditioning, osteoporosis/fractures, abnormal echocardiography, arterial tortuosity/aneurysm/dissection, GI perforation/obstruction/bleeding and major poor wound healing. No validated prognostic biomarker or calculator exists.

## 12. Treatment and current applications

There is **no cure and no approved TNXB- or AEBP1-targeted drug, gene therapy, cell therapy, RNA therapy or genome-editing therapy**. No relevant disease-specific interventional trial was identified in the ClinicalTrials.gov search; a retrieved oncology trial matching a gene acronym was unrelated and excluded.

### Practical multidisciplinary strategy

1. **Rehabilitation:** individualized physiotherapy emphasizing proprioception, core and periarticular stabilization, low-impact aerobic conditioning and graded strengthening; occupational therapy, braces/orthoses and mobility aids as required. Avoid aggressive stretching and repeated end-range loading. Suggested NCIT concepts: Physical Therapy, Occupational Therapy, Exercise Therapy, Orthopedic Device.
2. **Pain management:** education, pacing, sleep optimization, physical modalities and individualized non-opioid/neuropathic-pain therapy. NSAIDs require caution when bruising or GI bleeding is prominent. Tnxb-null mouse allodynia responded to gabapentin and a μ-opioid agonist but not indomethacin; this is mechanistic animal evidence, not a clEDS clinical efficacy trial. (kosho2024editorialehlersdanlossyndrome pages 2-2)
3. **Skin/wounds:** protective pads where injury is recurrent; low-tension multilayer closure, generous deep sutures and longer retention. Watch for dehiscence and hematoma. (malfait2014theehlersdanlossyndrome. pages 10-12)
4. **Bone:** assess vitamin D/calcium intake, fall risk and DXA when osteoporosis, fractures or AEBP1 disease warrant it; treat osteoporosis according to standard guidelines.
5. **Cardiovascular:** baseline echocardiography for valves and aortic root is reasonable. Because clEDS2 has reported aneurysm/dissection and 4/11 MVP, specialist-directed periodic echocardiography and arterial imaging should be individualized. Evidence does not support a universal fixed interval or prophylactic vascular drug. (kosho2024editorialehlersdanlossyndrome pages 2-2)
6. **GI/pelvic floor:** prompt evaluation of unexplained abdominal pain, bleeding, obstruction symptoms or prolapse; avoid dismissing symptoms as functional when structural complications are possible.
7. **Surgery/anesthesia:** clearly flag connective-tissue fragility. Use careful positioning, padding, airway instrumentation, vascular access and hemostasis; avoid excessive traction. Tissue handling and closure should be gentle. Rare-type EDS guidance notes possible tracheal/esophageal injury and the need for careful delivery planning. (brady2017theehlers–danlossyndromes pages 6-7)
8. **Pregnancy:** preconception genetic counseling and coordinated maternal-fetal, anesthesia and relevant surgical review; evidence is too sparse for a clEDS-specific obstetric risk percentage.

No clEDS pharmacogenomic recommendation exists. Published management is chiefly expert opinion and extrapolation from broader EDS practice rather than randomized trials.

## 13. Prevention

Primary prevention of inherited disease is limited to informed reproductive choice: carrier testing of relatives/partners, prenatal diagnosis and preimplantation genetic testing when both familial pathogenic alleles are known. Secondary prevention consists of early molecular diagnosis and cascade testing. Tertiary prevention includes joint stabilization, impact avoidance, skin protection, bone health, cardiovascular assessment, rapid evaluation of arterial/GI warning symptoms and procedure planning. Genetic counseling must explain autosomal-recessive recurrence and distinguish carrier hypermobility—especially for TNXB—from affected biallelic disease. (malfait2020theehlers–danlossyndromes pages 15-16, malfait2014theehlersdanlossyndrome. pages 10-12)

There is no vaccine, chemoprophylaxis, population-screening program or environmental public-health intervention specific to clEDS.

## 14. Other species and natural disease

A published 2019 report described compound-heterozygous **TNXB** variants in a mixed-breed dog with an EDS phenotype, suggesting naturally occurring comparative disease, but full variant and phenotype details were unavailable in the retrieved text and should be verified before structured annotation. The relevant species is **Canis lupus familiaris, NCBI Taxon 9615**. No zoonotic transmission is possible.

Naturally occurring cutaneous asthenia/EDS-like syndromes occur in several domestic species, but unless a causal TNXB or AEBP1 orthologue is demonstrated they should not be labeled direct models of these clEDS subtypes. No robust natural AEBP1-clEDS veterinary series was identified.

## 15. Model organisms and experimental systems

* **Tnxb-null mouse** (*Mus musculus*, NCBI Taxon 10090): reduced skin collagen deposition/density, approximately 30% lower collagen content, elastic/microfibril abnormalities and mechanical allodynia. It supports ECM-organization and pain mechanisms but does not establish the full human vascular/GI natural history. (kosho2024editorialehlersdanlossyndrome pages 2-2, pliegoarreaga2024jointhypermobilitysyndrome pages 6-8, gensemer2021hypermobileehlers‐danlossyndromes pages 66-70)
* **Aebp1-null mouse:** delayed/abnormal wound repair associated with impaired fibroblast proliferation. This recapitulates a repair defect but is not a complete phenocopy of human clEDS2. (blackburn2018biallelicalterationsin pages 4-5)
* **Patient-derived dermal fibroblasts:** demonstrate absent TNX or ACLP, nonsense-mediated decay, abnormal matrix deposition and variant-specific functional consequences. These are the most direct human in-vitro systems. (blackburn2018biallelicalterationsin pages 4-5, brady2017theehlers–danlossyndromes pages 3-4)
* **Biochemical collagen-polymerization assays:** showed ACLP binding to several fibrillar collagens and enhancement of polymerization. (blackburn2018biallelicalterationsin pages 4-5)

No validated clEDS patient iPSC, organoid, zebrafish, Drosophila or C. elegans model, disease-specific CRISPR screen, or single-cell/spatial/multi-omic atlas was identified in the retrieved literature.

## Recent developments and authoritative assessment

1. **AEBP1 phenotype expansion, April 2023:** two additional individuals increased the aggregate to 11. Hyperextensibility and hypermobility were 11/11, bruising 10/11, atrophic scarring 9/11 and hair loss 6/11; vascular findings prompted the authors to state that surveillance “seems warranted.” DOI/URL: https://doi.org/10.3389/fgene.2023.1148224.
2. **TNXB cohort refinement summarized in April 2024:** a nine-person cohort used a custom NGS approach; more than 75% carried TNXA-derived variation, and GI complications were reported in all nine. The high figure likely reflects referral/selection and is not population prevalence. DOI/URL for the editorial summary: https://doi.org/10.3389/fgene.2024.1399386. (kosho2024editorialehlersdanlossyndrome pages 1-2)
3. **2024 diagnostic consensus:** gene panels using massively parallel sequencing are the practical standard for monogenic EDS, but TNXB requires locus-aware methods because ordinary sequencing may miss pseudogene-derived and structural alleles. DOI/URLs: https://doi.org/10.1515/medgen-2024-2060 and https://doi.org/10.1515/medgen-2024-2061. (zschocke2024geneticdiagnosisof pages 11-11, malfait2020theehlers–danlossyndromes pages 15-16)
4. **Expert interpretation:** current authorities regard clEDS as an ECM-organization disorder rather than simply a collagen-gene disorder. They emphasize molecular confirmation, careful subtype distinction and multidisciplinary complication-directed care; natural-history and treatment evidence remain inadequate. (blackburn2018biallelicalterationsin pages 4-5, malfait2020theehlers–danlossyndromes pages 15-16)

## Evidence-quality limitations

The strongest causal evidence comprises segregating biallelic variants, absent protein/nonsense-mediated decay, patient skin/fibroblast abnormalities, collagen-binding/polymerization assays and knockout models. Phenotype frequencies, vascular/GI risk, penetrance, QoL and prognosis are much weaker because they derive from small, clinically selected case series. No randomized treatment trial, longitudinal registry-quality natural-history study, validated biomarker or population epidemiology was found. Consequently, absence of a reported feature should not be treated as evidence of absence, and percentages should always retain their cohort denominator.

References

1. (gensemer2021hypermobileehlers‐danlossyndromes pages 24-29): Cortney Gensemer, Randall Burks, Steven Kautz, Daniel P. Judge, Mark Lavallee, and Russell A. Norris. Hypermobile <scp>ehlers‐danlos</scp> syndromes: complex phenotypes, challenging diagnoses, and poorly understood causes. Aug 2021. URL: https://doi.org/10.1002/dvdy.220, doi:10.1002/dvdy.220. This article has 219 citations and is from a peer-reviewed journal.

2. (kosho2024editorialehlersdanlossyndrome pages 2-2): Tomoki Kosho, Shujiro Hayashi, Ken-ichi Matsumoto, Delfien Syx, and Anupriya Kaur. Editorial: ehlers-danlos syndrome: from bedside to bench. Frontiers in Genetics, Apr 2024. URL: https://doi.org/10.3389/fgene.2024.1399386, doi:10.3389/fgene.2024.1399386. This article has 0 citations and is from a peer-reviewed journal.

3. (blackburn2018biallelicalterationsin pages 4-5): Patrick R. Blackburn, Zhi Xu, Kathleen E. Tumelty, Rose W. Zhao, William J. Monis, Kimberly G. Harris, Jennifer M. Gass, Margot A. Cousin, Nicole J. Boczek, Mario V. Mitkov, Mark A. Cappel, Clair A. Francomano, Joseph E. Parisi, Eric W. Klee, Eissa Faqeih, Fowzan S. Alkuraya, Matthew D. Layne, Nazli B. McDonnell, and Paldeep S. Atwal. Bi-allelic alterations in aebp1 lead to defective collagen assembly and connective tissue structure resulting in a variant of ehlers-danlos syndrome. American journal of human genetics, 102 4:696-705, Apr 2018. URL: https://doi.org/10.1016/j.ajhg.2018.02.018, doi:10.1016/j.ajhg.2018.02.018. This article has 213 citations and is from a highest quality peer-reviewed journal.

4. (pliegoarreaga2024jointhypermobilitysyndrome pages 6-8): Raquel Pliego-Arreaga, Juan Antonio Cervantes-Montelongo, Guillermo Antonio Silva-Martínez, Fabiola Estefanía Tristán-Flores, Miguel Angel Pantoja-Hernández, and Juan Raúl Maldonado-Coronado. Joint hypermobility syndrome and membrane proteins: a comprehensive review. Apr 2024. URL: https://doi.org/10.3390/biom14040472, doi:10.3390/biom14040472. This article has 11 citations.

5. (sugiura2023analysisofreferrals pages 26-30): H Sugiura. Analysis of referrals to genetics for suspected hypermobile ehlers-danlos syndrome. Unknown journal, 2023.

6. (brady2017theehlers–danlossyndromes pages 6-7): Angela F. Brady, Serwet Demirdas, Sylvie Fournel‐Gigleux, Neeti Ghali, Cecilia Giunta, Ines Kapferer‐Seebacher, Tomoki Kosho, Roberto Mendoza‐Londono, Michael F. Pope, Marianne Rohrbach, Tim Van Damme, Anthony Vandersteen, Caroline van Mourik, Nicol Voermans, Johannes Zschocke, and Fransiska Malfait. The ehlers–danlos syndromes, rare types. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 175:115-70, Mar 2017. URL: https://doi.org/10.1002/ajmg.c.31550, doi:10.1002/ajmg.c.31550. This article has 318 citations.

7. (kosho2024editorialehlersdanlossyndrome pages 1-2): Tomoki Kosho, Shujiro Hayashi, Ken-ichi Matsumoto, Delfien Syx, and Anupriya Kaur. Editorial: ehlers-danlos syndrome: from bedside to bench. Frontiers in Genetics, Apr 2024. URL: https://doi.org/10.3389/fgene.2024.1399386, doi:10.3389/fgene.2024.1399386. This article has 0 citations and is from a peer-reviewed journal.

8. (brady2017theehlers–danlossyndromes pages 3-4): Angela F. Brady, Serwet Demirdas, Sylvie Fournel‐Gigleux, Neeti Ghali, Cecilia Giunta, Ines Kapferer‐Seebacher, Tomoki Kosho, Roberto Mendoza‐Londono, Michael F. Pope, Marianne Rohrbach, Tim Van Damme, Anthony Vandersteen, Caroline van Mourik, Nicol Voermans, Johannes Zschocke, and Fransiska Malfait. The ehlers–danlos syndromes, rare types. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 175:115-70, Mar 2017. URL: https://doi.org/10.1002/ajmg.c.31550, doi:10.1002/ajmg.c.31550. This article has 318 citations.

9. (kim2023molecularbasisand pages 10-10): Ja Hye Kim, Gu-Hwan Kim, Han-Wook Yoo, and Jin-Ho Choi. Molecular basis and genetic testing strategies for diagnosing 21-hydroxylase deficiency, including cah-x syndrome. Jun 2023. URL: https://doi.org/10.6065/apem.2346108.054, doi:10.6065/apem.2346108.054. This article has 22 citations.

10. (malfait2020theehlers–danlossyndromes pages 15-16): Fransiska Malfait, Marco Castori, Clair A. Francomano, Cecilia Giunta, Tomoki Kosho, and Peter H. Byers. The ehlers–danlos syndromes. Jul 2020. URL: https://doi.org/10.1038/s41572-020-0194-9, doi:10.1038/s41572-020-0194-9. This article has 294 citations.

11. (gensemer2021hypermobileehlers‐danlossyndromes pages 66-70): Cortney Gensemer, Randall Burks, Steven Kautz, Daniel P. Judge, Mark Lavallee, and Russell A. Norris. Hypermobile <scp>ehlers‐danlos</scp> syndromes: complex phenotypes, challenging diagnoses, and poorly understood causes. Aug 2021. URL: https://doi.org/10.1002/dvdy.220, doi:10.1002/dvdy.220. This article has 219 citations and is from a peer-reviewed journal.

12. (malfait2014theehlersdanlossyndrome. pages 10-12): Fransiska Malfait and Anne De Paepe. The ehlers-danlos syndrome. Advances in experimental medicine and biology, 802:129-43, Dec 2014. URL: https://doi.org/10.1007/978-94-007-7893-1\_9, doi:10.1007/978-94-007-7893-1\_9. This article has 158 citations and is from a peer-reviewed journal.

13. (malfait2020theehlers–danlossyndromes pages 22-22): Fransiska Malfait, Marco Castori, Clair A. Francomano, Cecilia Giunta, Tomoki Kosho, and Peter H. Byers. The ehlers–danlos syndromes. Jul 2020. URL: https://doi.org/10.1038/s41572-020-0194-9, doi:10.1038/s41572-020-0194-9. This article has 294 citations.

14. (zschocke2024geneticdiagnosisof pages 11-11): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](Classical-like_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011670` (2 mentions) - the report calls it "if available"; MONDO calls it **Ehlers-Danlos syndrome due to tenascin-X deficiency**
- `HP:0001634` (1 mention) - the report calls it "clEDS2: 4/11 in the 2023 aggregate"; HP calls it **Mitral valve prolapse**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001811` (1 mention) - HP does not contain this term
- `UBERON:0000216` (1 mention) - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`