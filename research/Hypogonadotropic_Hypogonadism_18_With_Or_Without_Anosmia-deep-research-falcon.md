---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T13:46:37.206173'
end_time: '2026-09-04T14:04:06.476715'
duration_seconds: 1049.27
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hypogonadotropic Hypogonadism 18 With or Without Anosmia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 48
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 44
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.022
  labels_checked: 7
  labels_matching: 5
  labels_variant: 2
  unresolved_terms:
  - HP:0000806
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hypogonadotropic_Hypogonadism_18_With_Or_Without_Anosmia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypogonadotropic Hypogonadism 18 With or Without Anosmia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypogonadotropic Hypogonadism 18 With or Without Anosmia** covering all of the
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
- **Disease Name:** Hypogonadotropic Hypogonadism 18 With or Without Anosmia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypogonadotropic Hypogonadism 18 With or Without Anosmia** covering all of the
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


# Hypogonadotropic Hypogonadism 18 With or Without Anosmia: Research Report

## Executive summary and evidence boundaries

Hypogonadotropic hypogonadism 18 with or without anosmia (HH18) is an *IL17RD*-associated form of congenital hypogonadotropic hypogonadism (CHH). CHH results from deficient gonadotropin-releasing hormone (GnRH) secretion or action and causes low sex steroids with low or inappropriately normal luteinizing hormone (LH) and follicle-stimulating hormone (FSH). Disease accompanied by anosmia or hyposmia is conventionally called Kallmann syndrome (KS); patients with preserved smell have normosmic CHH. The strongest HH18-specific evidence remains the 2013 discovery study of only eight unrelated *IL17RD*-positive probands. Accordingly, subtype-specific prevalence, penetrance, prognosis, and treatment-response estimates are unavailable; broader CHH evidence is identified explicitly below rather than presented as HH18-specific evidence. (miraoui2013mutationsinfgf17 pages 7-10, miraoui2013mutationsinfgf17 pages 6-7, oleari2021thedifferentialroles pages 2-4)

| Domain | Scope | Key Findings, Statistics & Mechanisms | Evidence Type & Ontology Terms | References |
|---|---|---|---|---|
| **Identity & Identifiers** | HH18-Specific | Hypogonadotropic hypogonadism 18 with or without anosmia (Synonym: Kallmann syndrome 18). Inheritance is complex: autosomal dominant, autosomal recessive, and digenic/oligogenic patterns reported. | MONDO:0014103 | (OpenTargets Search: hypogonadotropic hypogonadism 18 with or without anosmia, miraoui2013mutationsinfgf17 pages 6-7, miraoui2013mutationsinfgf17 pages 14-15) |
| **Gene & Variants** | HH18-Specific | Causal gene: *IL17RD* (*SEF*). Discovery cohort (2013, PMID: 23643382, DOI: 10.1016/j.ajhg.2013.04.008) screened 386 CHH probands and found 8 unrelated probands (~2%) with variants: p.Lys131Thr, p.Lys162Arg, p.Pro306Ser, p.Tyr379Cys, p.Ser468Leu, p.Pro577Gln, p.Ala735Val. Later variant reported: p.Met320Ile. | HGNC:28810; Human clinical cohorts | (miraoui2013mutationsinfgf17 pages 6-7, cannarella2023geneticanalysisof pages 5-8, miraoui2013mutationsinfgf17 pages 4-6) |
| **Phenotypes** | HH18-Specific | In the 2013 discovery cohort (n=8): 8/8 had Kallmann syndrome (anosmia), 7/8 had absent puberty, and 6/8 had congenital hearing loss (typically unilateral). Additional findings included dental agenesis and low bone mass. | HP:0000044 (CHH), HP:0000458 (Anosmia), HP:0000365 (Hearing impairment), HP:0000806 (Absent puberty) | (miraoui2013mutationsinfgf17 pages 6-7, miraoui2013mutationsinfgf17 pages 14-15) |
| **Mechanism & Models** | HH18-Specific / IL17RD | IL17RD is a transmembrane inhibitor of FGF8/FGFR1c and RAS-MAPK/ERK signaling. *In vitro* reporter assays showed p.Lys131Thr, p.Pro306Ser, and p.Ser468Leu variants caused 89%, 67%, and 32% loss of inhibition, respectively. In mouse embryos (E10.5-12.5), IL17RD localizes to the olfactory placode and GnRH neurons. *Sef*-null mice exhibit auditory brainstem defects. | GO:0008543 (FGF receptor signaling), In vitro assays, Mouse models | (miraoui2013mutationsinfgf17 pages 7-10, miraoui2013mutationsinfgf17 pages 6-7, pande2021interleukin17receptord pages 1-2, pande2021interleukin17receptord pages 2-4) |
| **Diagnosis** | Broad CHH | **Neonatal:** Minipuberty window shows low LH/FSH/T, micropenis, cryptorchidism. **Adolescence:** Delayed/absent puberty; inhibin B < 60 pmol/mL helps distinguish CHH from constitutional delay. **Anosmia:** Present in 52-55% of CHH cohorts. **Genetics:** UK NHS 14 "green" gene panel includes IL17RD. | Diagnostic clinical criteria, Biomarkers | (swee2019congenitalhypogonadotrophichypogonadism pages 2-3, young2019clinicalmanagementof pages 17-18, young2019clinicalmanagementof pages 10-11, sayed2023paneltestingfor pages 3-5) |
| **Treatment & Statistics** | Broad CHH | **Fertility (2024 Meta-analysis, 5328 pts):** hCG+FSH induced spermatogenesis in 86% (95% CI 82-91%) vs hCG alone (40%). **Reversal (2024 study):** 10-15% spontaneous reversal rate; among 87 reversals vs 108 non-reversals, cryptorchidism significantly lowered reversal odds (OR 0.30). **Puberty Induction:** Testosterone enanthate/cypionate for males; transdermal estradiol + progestin for females. | NCIT:C64016 (Hormone Replacement Therapy), NCIT:C63740 (Fertility Treatment) | (dwyer2024classesandpredictors pages 6-8, alexander2024gonadotropinsforpubertal pages 1-2, dwyer2024classesandpredictors pages 1-3, young2019clinicalmanagementof pages 23-24, young2019clinicalmanagementof pages 24-25) |
| **Evidence Gaps** | Both | Few HH18-specific functional cohorts exist beyond the 2013 discovery. Human GnRH neuronal impact of IL17RD is extrapolated from animal models. No gene-targeted therapies exist for FGF/IL17RD defects. Female CHH prevalence and natural history remain under-characterized. | Expert reviews, Literature gaps | (young2019clinicalmanagementof pages 7-8, pande2021interleukin17receptord pages 13-14) |


*Table: A structured knowledge-base table summarizing specific genetic, phenotypic, and mechanistic findings for IL17RD-mediated HH18, alongside diagnostic and therapeutic statistics for broader congenital hypogonadotropic hypogonadism.*

## 1. Disease information

**Definition.** HH18 is a rare Mendelian neurodevelopmental reproductive disorder in which pathogenic or contributory *IL17RD* variants disrupt development or function of the GnRH neuronal system. The defining endocrine phenotype is absent, partial, or arrested puberty and infertility caused by central gonadotropin deficiency. Olfactory dysfunction is variable by disease definition, although all eight probands in the original *IL17RD* series had KS. (miraoui2013mutationsinfgf17 pages 6-7, vezzoli2023geneticarchitectureof pages 3-5)

**Identifiers and terminology.** The principal mappings are MONDO:0014103 and OMIM phenotype 615267; the causal gene is *IL17RD* (interleukin-17 receptor D; synonym *SEF*, “similar expression to FGF”; HGNC:17616; OMIM gene 606807). Common names include “hypogonadotropic hypogonadism 18 with or without anosmia,” “HH18,” “*IL17RD*-related congenital hypogonadotropic hypogonadism,” and “Kallmann syndrome 18.” Open Targets maps MONDO:0014103 specifically to *IL17RD* and cites PMID 23643382 as foundational evidence. (OpenTargets Search: hypogonadotropic hypogonadism 18 with or without anosmia)

No dedicated Orphanet, MeSH, ICD-10, or ICD-11 code reliably distinguishes HH18 from other CHH forms. Practical aggregate mappings include ICD-10-CM E23.0 (“hypopituitarism,” encompassing hypogonadotropic hypogonadism) and broader Kallmann/CHH concepts in Orphanet and MeSH. These coding systems should not be treated as genotype-specific identifiers.

The evidence is **aggregated disease-level literature and curated-resource evidence**, not an individual EHR extraction. The primary human evidence consists of deeply phenotyped research probands and families. (OpenTargets Search: hypogonadotropic hypogonadism 18 with or without anosmia, miraoui2013mutationsinfgf17 pages 4-6)

## 2. Etiology, risk, and protective factors

### Causal and genetic factors

The 2013 primary study screened 386 CHH probands—199 with KS and 187 with normosmic CHH—and 155 controls. Eight unrelated probands carried heterozygous or homozygous *IL17RD* missense variants. Reported alleles were c.392A>C (p.Lys131Thr), c.485A>G (p.Lys162Arg), c.916C>T (p.Pro306Ser), c.1136A>G (p.Tyr379Cys), c.1403C>T (p.Ser468Leu), c.1730C>A (p.Pro577Gln), and c.2204C>T (p.Ala735Val). Across the screened FGF-network genes, individual genes explained approximately 1–4% of cases; this is not an HH18 population-prevalence estimate. (miraoui2013mutationsinfgf17 pages 6-7, miraoui2013mutationsinfgf17 pages 4-6)

Inheritance can appear autosomal dominant, autosomal recessive, or oligogenic. A heterozygous *IL17RD* allele may be insufficient by itself: some severe cases also carried an *FGFR1* or *KISS1R* variant. For example, p.Tyr379Cys was inherited from an anosmic mother, while the proband additionally carried de novo *FGFR1* p.Gly348Arg and had complete absent puberty, dental agenesis, hearing loss, and osteoporosis. This illustrates incomplete penetrance, variable expressivity, and locus–locus interaction rather than simple deterministic Mendelian transmission. (miraoui2013mutationsinfgf17 pages 7-10, miraoui2013mutationsinfgf17 pages 14-15)

A 2023 case series identified heterozygous *IL17RD* c.960G>A (p.Met320Ile) together with *FGF17* p.Gly70Arg in a man with KS. Both were VUS-level findings; modeling did not demonstrate a major structural effect, so they should not be regarded as independently established pathogenic alleles. (cannarella2023geneticanalysisof pages 5-8, cannarella2023geneticanalysisof pages 4-5)

### Environmental, infectious, and protective factors

No toxin, infection, diet, occupation, or lifestyle exposure is established as a cause of germline HH18, and no validated genetic or environmental protective factor has been reported. Energy deficiency, excessive exercise, stress, chronic systemic illness, obesity, diabetes, opioids, glucocorticoids, hyperprolactinemia, iron overload, tumors, inflammation, surgery, and radiotherapy can cause **acquired or functional** hypogonadotropic hypogonadism, but these are differential diagnoses rather than demonstrated HH18 modifiers. (vezzoli2023geneticarchitectureof pages 2-3)

A plausible gene–environment interaction is that reduced developmental reserve from an incompletely penetrant allele could make the reproductive axis more vulnerable to illness, undernutrition, or stress; however, this remains unproven for *IL17RD*. There is likewise no evidence that avoiding a particular exposure prevents expression in a carrier.

## 3. Phenotypes

The discovery cohort provides the best HH18-specific frequencies: KS/anosmia in 8/8, absent puberty in 7/8, and congenital hearing loss in 6/8, often unilateral. Dental abnormalities and low bone mass occurred in selected patients. The ascertainment strategy and very small cohort make these frequencies vulnerable to selection bias and unsuitable as population estimates. (miraoui2013mutationsinfgf17 pages 6-7)

Suggested knowledge-base phenotypes are:

- **Central hypogonadism:** low testosterone or estradiol with low/inappropriately normal LH and FSH; congenital, usually recognized in adolescence; severity ranges from absent to partial/arrested puberty. HPO: Hypogonadotropic hypogonadism (HP:0000044), Delayed puberty (HP:0000823), Absent puberty (HP:0000805).
- **Olfactory dysfunction:** congenital anosmia or hyposmia, generally stable. HPO: Anosmia (HP:0000458), Hyposmia (HP:0004409), Abnormality of the olfactory bulb (HP:0002033). In a broader IHH referral cohort of 286 patients, 31.5% were anosmic, 33.6% hyposmic, and 34.9% normosmic, demonstrating a continuum rather than a binary phenotype. (lewkowitzshpuntoff2012olfactoryphenotypicspectrum pages 1-2)
- **Male neonatal signs:** micropenis and cryptorchidism reflect deficient fetal/neonatal gonadotropin action. Broader CHH series report cryptorchidism in approximately 30–50% of males. HPO: Micropenis (HP:0000054), Cryptorchidism (HP:0000028). (swee2019congenitalhypogonadotrophichypogonadism pages 2-3)
- **Male adolescent/adult manifestations:** small prepubertal testes, absent virilization, sparse body/facial hair, high-pitched voice, reduced libido, erectile dysfunction, azoospermia/infertility, and gynecomastia. HPO suggestions include Small testis (HP:0000050), Azoospermia (HP:0000027), Infertility (HP:0000789), and Gynecomastia (HP:0000771). (oleari2021thedifferentialroles pages 2-4, fanis2023gonadotropinreleasinghormonereceptor pages 14-15)
- **Female manifestations:** absent or limited breast development, primary amenorrhea, anovulation, and infertility. HPO: Primary amenorrhea (HP:0000786), Absent breast development (HP:0010311), Female infertility (HP:0008222). (oleari2021thedifferentialroles pages 2-4)
- **Auditory phenotype:** congenital, sometimes unilateral hearing impairment was unusually prominent in the original HH18 cohort. HPO: Hearing impairment (HP:0000365), Unilateral hearing impairment (HP:0000369). (miraoui2013mutationsinfgf17 pages 7-10)
- **Secondary consequences:** low bone mineral density/osteoporosis, adverse body composition, reduced muscle mass, anemia, fatigue, and metabolic risk arise downstream of untreated sex-steroid deficiency. HPO: Osteoporosis (HP:0000939), Decreased bone mineral density (HP:0004349). (oleari2021thedifferentialroles pages 2-4, vezzoli2023geneticarchitectureof pages 3-5)

Quality-of-life effects documented across CHH include anxiety, depression, low self-esteem, altered body image, social withdrawal, impaired psychosexual development, sexual distress, and infertility-related burden. Delayed diagnosis—often around age 18–19 years—prolongs these effects. No validated HH18-specific EQ-5D, SF-36, or PROMIS study was identified. (swee2019congenitalhypogonadotrophichypogonadism pages 2-3, young2019clinicalmanagementof pages 7-8)

## 4. Genetic and molecular information

*IL17RD* lies at chromosome 3p14.3 and encodes a 739-amino-acid type-I single-pass transmembrane signaling regulator. The extracellular region contains a signal peptide, immunoglobulin-like domain, fibronectin type-III region, conserved cysteines, and potential N-glycosylation sites. The cytoplasmic region includes Tyr330, a SEFIR domain, TIR-like motifs, a putative TRAF6-binding site, and a proline-rich putative SH3-binding region. Full-length IL17RD is mainly at the plasma membrane but also occurs in Golgi and endosomal compartments; alternative translation produces cytosolic isoforms. (pande2021interleukin17receptord pages 1-2, pande2021interleukin17receptord pages 2-4)

The established HH18 alleles are germline, not somatic. Most reported founding alleles are missense variants. Functional evidence is allele-specific: p.Lys131Thr, p.Pro306Ser, and p.Ser468Leu impaired suppression of an FGF8/FGFR1c-responsive AP-1 reporter; p.Tyr379Cys and p.Pro577Gln had weaker borderline effects, while p.Lys162Arg and p.Ala735Val behaved similarly to wild type in that assay. Reduced cell-surface expression was observed for several mutants. Variant classification should therefore be performed allele by allele under ACMG/AMP criteria rather than assuming that every rare *IL17RD* missense substitution is pathogenic. (miraoui2013mutationsinfgf17 pages 7-10, miraoui2013mutationsinfgf17 pages 6-7)

Population allele frequencies were not supplied in the retrieved primary passages and should be obtained directly from the current gnomAD release for each transcript-normalized variant. Absence or rarity in gnomAD is supporting—not sufficient—evidence. No validated recurrent structural rearrangement, repeat expansion, mitochondrial defect, somatic event, disease-specific methylation signature, or epigenetic biomarker has been established for HH18.

Probable modifiers include other FGF/GnRH-network genes, especially *FGFR1* and *KISS1R* in reported families. Broad CHH studies also demonstrate oligogenicity, but specific modifier penetrance estimates for *IL17RD* are unavailable. (miraoui2013mutationsinfgf17 pages 7-10, dwyer2024classesandpredictors pages 1-3)

## 5. Environmental information

Environmental toxins, radiation, pollution, occupational exposures, smoking, alcohol, diet, or infectious agents have no demonstrated etiologic role in HH18. These factors may affect general reproductive health but should not be entered as HH18 causes without direct evidence. Functional hypothalamic suppression from low energy availability, illness, medications, or stress must instead be excluded diagnostically. HH18 is not infectious, transmissible, or zoonotic. (vezzoli2023geneticarchitectureof pages 2-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A functionally deleterious germline *IL17RD* allele **leads to** altered abundance, trafficking, or signaling activity of IL17RD/SEF at the cell membrane.
2. Defective IL17RD regulation **leads to** dysregulated FGF8–FGFR1 signaling through FRS2 and RAS–RAF–MEK–ERK/related MAPK pathways; the exact direction, timing, and cell-specific consequence in human embryos remain partly inferred.
3. In the embryonic olfactory placode/GnRH developmental field, mistimed FGF signaling **is inferred to lead to** abnormal GnRH-neuron specification, survival, differentiation, or migration into the forebrain/hypothalamus. Mouse colocalization supports this location, but direct human embryonic proof is absent.
4. Reduced or dysfunctional hypothalamic GnRH neurons **lead to** deficient pulsatile GnRH release.
5. Deficient GnRH stimulation of anterior-pituitary gonadotropes **leads to** low or inappropriately normal LH and FSH.
6. Low LH/FSH **lead to** insufficient Leydig/Sertoli or ovarian follicular stimulation, causing low testosterone/estradiol, deficient gametogenesis, absent or arrested puberty, and infertility.
7. **Olfactory branch:** disturbed olfactory-system development **leads to** hyposmia/anosmia and olfactory-bulb abnormalities.
8. **Auditory branch:** IL17RD-dependent developmental/signaling abnormalities **are inferred to lead to** congenital hearing impairment; knockout-mouse auditory-brainstem abnormalities support this branch, but the human mechanism is unresolved.
9. Chronic sex-steroid deficiency **leads to** reduced bone mineralization, adverse body composition, sexual dysfunction, and psychosocial morbidity. (miraoui2013mutationsinfgf17 pages 7-10, oleari2021thedifferentialroles pages 2-4, pande2021interleukin17receptord pages 1-2, miraoui2013mutationsinfgf17 pages 6-7)

IL17RD is a feedback regulator and scaffold rather than a classical metabolic enzyme. It can bind FGFR1/2 and inhibit FGFR kinase activity, FRS2α phosphorylation, ERK/AKT signaling, or MEK–ERK nuclear trafficking depending on isoform and cellular context. It also interacts with IL17RA, TLR3/4, TNFR2, and EGFR and can regulate JNK, p38, NF-κB, ACT1, and TRAF6 outputs. These inflammatory roles are biologically established in other tissues but have not been shown to cause HH18; immune-mediated tissue injury is therefore not part of the demonstrated reproductive mechanism. (pande2021interleukin17receptord pages 2-4, pande2021interleukin17receptord pages 4-6, pande2021interleukin17receptord pages 6-8)

Suggested annotations include GO:0008543 (fibroblast growth factor receptor signaling pathway), GO:0000165 (MAPK cascade), GO:0007218 (neuropeptide signaling pathway), GO:0007399 (nervous-system development), GO:0030154 (cell differentiation), GO:0050900 (leukocyte migration; only for immune studies), and GO:0005886 (plasma membrane). Relevant cell concepts include GnRH neuron, olfactory sensory neuron, anterior-pituitary gonadotroph, Leydig cell (CL:0000178), Sertoli cell (CL:0000216), ovarian granulosa cell (CL:0000501), and cochlear-nucleus astrocyte. No validated HH18-specific transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, organoid, iPSC, or CRISPR-screen signature was identified.

## 7. Anatomical structures affected

The primary axis comprises the olfactory placode/nasal embryonic compartment, olfactory nerves and bulbs, hypothalamic GnRH neuronal network, pituitary gonadotropes, and gonads. Secondary structures include testes, penis, ovaries, uterus, breast, skeleton, muscle, and adipose tissue. Hearing impairment implicates auditory pathways, although its precise lesion is uncertain. (young2019clinicalmanagementof pages 10-11, pande2021interleukin17receptord pages 1-2)

Suggested UBERON mappings include olfactory placode (UBERON:0009950), olfactory bulb (UBERON:0002264), hypothalamus (UBERON:0001898), pituitary gland (UBERON:0000007), anterior pituitary (UBERON:0002196), testis (UBERON:0000473), ovary (UBERON:0000992), uterus (UBERON:0000995), and cochlea (UBERON:0001844). Relevant subcellular GO terms are plasma membrane (GO:0005886), Golgi apparatus (GO:0005794), endosome (GO:0005768), and cytoplasm (GO:0005737). Olfactory and hearing abnormalities may be bilateral or asymmetric; unilateral hearing loss was common in the original series. (miraoui2013mutationsinfgf17 pages 7-10, pande2021interleukin17receptord pages 2-4)

## 8. Temporal development

The initiating defect is congenital and acts during embryonic GnRH/olfactory development. In males, severe disease can be detected during fetal life or neonatal “minipuberty” through micropenis, cryptorchidism, absent erections, and low LH/FSH/testosterone. Childhood may be clinically silent because the reproductive axis is normally quiescent. Adolescence reveals absent, partial, or arrested puberty; adult presentation may be infertility, sexual dysfunction, or osteoporosis. (swee2019congenitalhypogonadotrophichypogonadism pages 2-3, young2019clinicalmanagementof pages 10-11)

Untreated endocrine deficiency is chronic, but severity is variable. Across CHH—not specifically HH18—approximately 5–20% recover endogenous reproductive-axis activity, and relapse can occur. A 2024 six-center study compared 87 men with reversal against 108 non-reversal controls; cryptorchidism reduced reversal odds (OR 0.30), while larger testes and less severe phenotypes favored reversal. Long-term periodic reassessment is therefore appropriate even after apparent recovery. (dwyer2024classesandpredictors pages 6-8, dwyer2024classesandpredictors pages 1-3)

Critical intervention windows are neonatal minipuberty, timely adolescent pubertal induction, and the period before prolonged sex-steroid deficiency causes skeletal and psychosocial morbidity. (swee2019congenitalhypogonadotrophichypogonadism pages 2-3, swee2019managingcongenitalhypogonadotrophic pages 7-8)

## 9. Inheritance and population

HH18 is exceedingly rare; neither incidence nor prevalence has been measured. Broader male CHH estimates range from approximately 1:4,000 to 1:30,000, with a historical French estimate near 1:10,000 men and a Sardinian KS estimate near 1:86,000. The reported male:female ratio is roughly 4:1, probably reflecting ascertainment and the greater neonatal visibility of male disease. These figures must not be assigned directly to HH18. (oleari2021thedifferentialroles pages 2-4, young2019clinicalmanagementof pages 7-8)

Both dominant and recessive *IL17RD* genotypes have been reported, often against an oligogenic background. Penetrance is incomplete and expressivity variable. No anticipation mechanism is known. Germline mosaicism is theoretically possible but not established; no founder allele, population-specific enrichment, carrier frequency, or robust consanguinity effect has been demonstrated. Cascade testing should account for mildly affected or apparently unaffected relatives and should not use genotype alone to predict severity. (miraoui2013mutationsinfgf17 pages 7-10, miraoui2013mutationsinfgf17 pages 14-15)

## 10. Diagnostics

Diagnosis requires: (1) absent, partial, or arrested puberty or adult reproductive symptoms; (2) repeatedly low testosterone/estradiol with low or inappropriately normal LH/FSH; and (3) exclusion of functional, structural, systemic, medication-related, and combined-pituitary causes. There is no single gold-standard test distinguishing CHH from self-limited delayed puberty at age 14–16. (vezzoli2023geneticarchitectureof pages 2-3, young2019clinicalmanagementof pages 10-11)

Recommended evaluation includes:

- neonatal LH, FSH, testosterone and, when useful, inhibin B/AMH during approximately 4–12 weeks of life;
- morning testosterone on two occasions in adult males; estradiol, LH, and FSH in females; prolactin, TSH/free T4, morning cortisol, and IGF-1 when broader pituitary disease is possible;
- testicular volume, genital examination, Tanner staging, menstrual history, semen analysis, and bone age/BMD where indicated;
- formal smell testing rather than self-report; coronal T2-weighted MRI may assess olfactory bulbs and sulci;
- pituitary/brain MRI when structural disease, neurological findings, or combined pituitary deficiency is suspected;
- renal, reproductive-tract, auditory, dental, skeletal, and ophthalmic assessment guided by phenotype. A stimulated LH cutoff of 4.3 IU/L was reported with 100% sensitivity and 75% specificity for severe CHH in one study, and inhibin B below 60 pmol/mL may support severe GnRH deficiency, but neither is definitive. (young2019clinicalmanagementof pages 17-18, vezzoli2023geneticarchitectureof pages 2-3)

**Genetic testing.** A multigene CHH/KS panel is preferable to isolated *IL17RD* sequencing because oligogenicity and phenotypic overlap are common. The 2023 UK NHS PanelApp R148 “green” panel included *ANOS1, CHD7, FGF8, FGFR1, FSHB, GNRHR, IL17RD, KISS1R, LHB, PROK2, PROKR2, TAC3, TACR3,* and *WDR11*. Exome or genome sequencing is appropriate when panel testing is negative, syndromic features are atypical, or structural/noncoding variation is suspected; parental testing assists segregation and de novo assessment. CMA is reasonable for multiple congenital anomalies or developmental delay, but karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine HH18 tests unless another diagnosis is suspected. (sayed2023paneltestingfor pages 2-2, sayed2023paneltestingfor pages 3-5)

Differentials include constitutional/self-limited delayed puberty, functional hypothalamic amenorrhea, chronic illness/undernutrition, hyperprolactinemia, pituitary tumors or infiltration, combined pituitary hormone deficiency, CHARGE, Waardenburg, Bardet–Biedl, adrenal hypoplasia congenita, septo-optic dysplasia, and neurodegenerative hypogonadism syndromes. (vezzoli2023geneticarchitectureof pages 2-3, kim2015congenitalhypogonadotropichypogonadism pages 5-7)

## 11. Outcome and prognosis

Life expectancy and disease-specific mortality have not been quantified for HH18; isolated CHH is not generally considered directly life-limiting. Major untreated morbidity includes infertility, sexual dysfunction, osteoporosis/fracture risk, adverse body composition, anemia, and substantial psychological burden. Hearing loss adds communication and educational consequences in affected HH18 patients. (oleari2021thedifferentialroles pages 2-4, young2019clinicalmanagementof pages 7-8)

Puberty and sex-steroid-dependent health are usually medically restorable, and fertility can often be induced. Prognosis is less favorable for spermatogenesis in males with cryptorchidism, micropenis, complete absent puberty, or very small baseline testes. Apparent reversal requires monitoring because relapse is documented. No *IL17RD*-specific prognostic biomarker exists. (dwyer2024classesandpredictors pages 6-8, young2019clinicalmanagementof pages 26-26)

## 12. Treatment and current applications

There is no approved *IL17RD*-targeted, gene, RNA, cell, CRISPR, or immunotherapy. Treatment replaces downstream hormones and is genotype-independent.

- **Male puberty/maintenance:** gradually escalating testosterone enanthate or cypionate—often beginning near 50 mg monthly and increasing over 24–36 months—or age-appropriate transdermal/injectable adult replacement. Testosterone induces virilization and supports bone, muscle, libido, and well-being but does not enlarge testes or induce spermatogenesis. Monitor testosterone, growth/bone age, hematocrit, acne, gynecomastia, and psychosocial health. Excess dosing can cause erythrocytosis or premature epiphyseal closure. Suggested NCIt concepts: Testosterone Replacement Therapy and Hormone Replacement Therapy. (young2019clinicalmanagementof pages 23-24, lee2022treatmentofcongenital pages 3-4)
- **Female puberty/maintenance:** low-dose oral or transdermal 17β-estradiol, slowly escalated; add cyclic progestin after adequate estrogenization/bleeding to protect the endometrium. Continue physiologic replacement to the usual menopausal age unless contraindicated. Suggested NCIt concepts: Estrogen Replacement Therapy and Progestin Therapy. (young2019clinicalmanagementof pages 23-24, young2019clinicalmanagementof pages 24-25)
- **Male fertility:** pulsatile GnRH when pituitary function and specialist infrastructure permit, or hCG plus FSH/hMG. FSH priming before hCG may expand Sertoli-cell mass in severe prepubertal disease. A 2024 systematic review included 103 studies, 5,328 patients, and 21 countries; more than 98% of analyses showed increased testicular size, penile size, or testosterone. Pooled spermatogenesis was 86% with hCG+FSH (95% CI 82–91%), 76% with hCG+hMG, 76% with pulsatile GnRH, and 40% with hCG alone. The authors’ abstract states: “This systematic review provides convincing evidence of the efficacy of gonadotropins for pubertal induction,” while emphasizing major regimen heterogeneity. (alexander2024gonadotropinsforpubertal pages 3-5, alexander2024gonadotropinsforpubertal pages 1-2)
- **Female fertility:** pulsatile GnRH is physiologic where available; alternatively use FSH with LH activity followed by hCG/recombinant LH, with estradiol and ultrasound monitoring to limit ovarian hyperstimulation and multiple pregnancy. (young2019clinicalmanagementof pages 24-25, young2019clinicalmanagementof pages 26-26)
- **Neonatal management:** orchidopexy is generally undertaken by 6–12 months for persistent cryptorchidism. Short-course testosterone treats micropenis but not testicular maturation. Recombinant LH/FSH “minipuberty replacement” can increase penile length, testicular volume, testosterone, and inhibin B, but protocols remain specialized and long-term fertility benefit is not definitively established. (lee2022treatmentofcongenital pages 3-4, swee2019managingcongenitalhypogonadotrophic pages 5-7, lee2022treatmentofcongenital pages 2-3)
- **Supportive care:** bone-health assessment, adequate calcium/vitamin D and weight-bearing activity, hearing services, fertility counseling, sexual-health care, and psychological support.

In the 2024 meta-analysis, pooled gynecomastia rates were 8% with hCG+FSH, 15% with hCG+hMG, and 4% with GnRH; acne rates were 8%, 16%, and 5%, respectively. Injection-site pain/reaction was 9% with hCG+FSH and 42% with pump-delivered GnRH. These are broader HH data and not HH18-specific rates. (alexander2024gonadotropinsforpubertal pages 6-8)

Representative registered studies include NCT00064987 (FSH to improve testicular development), NCT02880280 (hCG+hMG in CHH), NCT01403532 (sequential therapy), and NCT03687606 (long-term hCG versus hCG+hMG). None is an *IL17RD*-specific interventional trial.

## 13. Prevention

The congenital germline lesion cannot currently be prevented by vaccination, medication, diet, or exposure modification. Primary prevention consists only of informed reproductive options after genetic counseling: cascade testing, partner testing where recessive risk is plausible, prenatal diagnosis, and preimplantation genetic testing for a familial pathogenic variant. Counseling must explain incomplete penetrance, oligogenicity, and uncertain phenotype prediction.

Secondary prevention is targeted early detection: examine male infants with bilateral cryptorchidism or micropenis during minipuberty, assess children from affected families, and investigate delayed puberty promptly rather than waiting until late adolescence. Tertiary prevention includes timely sex-steroid replacement, orchidopexy, fertility-preserving gonadotropin strategies, bone protection, hearing support, and mental-health care. Population newborn screening is not available or justified by present evidence. (swee2019congenitalhypogonadotrophichypogonadism pages 2-3, swee2019managingcongenitalhypogonadotrophic pages 7-8)

## 14. Other species and natural disease

No naturally occurring veterinary disease specifically established as orthologous *IL17RD*-HH18 was identified. IL17RD is evolutionarily conserved across vertebrates, and FGF-feedback functions have been studied in zebrafish, frog, chick, and mouse. These are experimental comparative systems, not evidence of transmissible or zoonotic disease. NCBI Taxonomy suggestions include *Homo sapiens* 9606, *Mus musculus* 10090, *Danio rerio* 7955, and *Gallus gallus* 9031. (pande2021interleukin17receptord pages 1-2)

## 15. Model organisms

- **Mouse embryonic localization:** at E10.5–E12.5, IL17RD was examined in the olfactory placode and in relation to GnRH neurons. Expression was FGF8-dependent and supports a role in early GnRH ontogeny, but localization is not itself proof that a patient allele causes migratory failure. (miraoui2013mutationsinfgf17 pages 7-10, miraoui2013mutationsinfgf17 pages 4-6)
- **Mouse knockout:** *Sef/Il17rd*-null mice have comparatively mild gross developmental findings but abnormal auditory-brainstem responses, supporting the human hearing phenotype. They do not fully reproduce the human reproductive syndrome, indicating redundancy and species/context dependence. (pande2021interleukin17receptord pages 2-4)
- **Zebrafish/frog/chick systems:** overexpression and loss-of-function studies establish IL17RD as an FGF-feedback regulator during morphogenesis. These models are useful for signaling, developmental patterning, and variant assays but do not recapitulate the full human HPG axis. (pande2021interleukin17receptord pages 1-2)
- **Cellular models:** HEK293/HEK293T, NIH3T3, PC12, mouse embryonic fibroblasts, macrophages, and keratinocytes have been used to study FGFR, ERK, AKT, JNK, p38, IL-17, TLR, and NF-κB regulation. The HH18 discovery study’s FGF8–FGFR1c/AP-1 assay provides the most direct patient-variant functional evidence. Major limitations are non-neuronal cellular context, overexpression, isoform differences, and incomplete correspondence to embryonic human GnRH neurons. (pande2021interleukin17receptord pages 4-6, pande2021interleukin17receptord pages 6-8, miraoui2013mutationsinfgf17 pages 6-7)

## Recent developments and expert assessment

Three developments are most relevant. First, the 2023 NHS-oriented review moved CHH testing toward curated multigene panels and explicitly included *IL17RD*, while stressing incomplete penetrance and oligogenicity. Second, the 2024 international reversal study showed that detailed phenotype plus genotype can identify patients warranting trials off treatment and continued surveillance, although no *IL17RD*-specific predictor emerged. Third, the 2024 meta-analysis supplied the strongest quantitative synthesis for gonadotropin-based male pubertal and fertility induction, favoring hCG+FSH over hCG alone while calling for standardized protocols and randomized trials. (dwyer2024classesandpredictors pages 6-8, alexander2024gonadotropinsforpubertal pages 1-2, sayed2023paneltestingfor pages 1-2)

The principal expert conclusion is therefore cautious: HH18 is a credible *IL17RD*/FGF-network disorder supported by human segregation, functional assays, and developmental-model evidence, but its gene–disease relationship is more complex than a fully penetrant single-gene syndrome. Rare missense alleles—especially VUSs—require segregation, population-frequency assessment, phenotype concordance, and preferably functional evidence. Clinical management should follow comprehensive CHH practice rather than depend on *IL17RD* genotype. (miraoui2013mutationsinfgf17 pages 7-10, cannarella2023geneticanalysisof pages 5-8, pande2021interleukin17receptord pages 12-13)

### Key primary and recent sources

1. Miraoui H, et al. “Mutations in FGF17, IL17RD, DUSP6, SPRY4, and FLRT3…” *American Journal of Human Genetics*. Published May 2013. PMID: **23643382**. https://doi.org/10.1016/j.ajhg.2013.04.008. (miraoui2013mutationsinfgf17 pages 7-10)
2. Cannarella R, et al. “Genetic Analysis of Patients with Congenital Hypogonadotropic Hypogonadism: A Case Series.” *International Journal of Molecular Sciences*. Published April 2023. https://doi.org/10.3390/ijms24087428. (cannarella2023geneticanalysisof pages 5-8)
3. Al Sayed Y, Howard SR. “Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism.” *European Journal of Human Genetics*. 2023;31:387–394. https://doi.org/10.1038/s41431-022-01261-0. (sayed2023paneltestingfor pages 3-5)
4. Dwyer AA, et al. “Classes and predictors of reversal…” *Lancet Diabetes & Endocrinology*. Published April 2024. https://doi.org/10.1016/S2213-8587(24)00028-7. (dwyer2024classesandpredictors pages 6-8)
5. Alexander EC, et al. “Gonadotropins for pubertal induction in males…” *European Journal of Endocrinology*. Published 2024. https://doi.org/10.1093/ejendo/lvad166. (alexander2024gonadotropinsforpubertal pages 1-2)
6. Young J, et al. “Clinical Management of Congenital Hypogonadotropic Hypogonadism.” *Endocrine Reviews*. Published April 2019. https://doi.org/10.1210/er.2018-00116. (young2019clinicalmanagementof pages 17-18)

**Major unresolved gaps:** no reliable HH18 prevalence or penetrance; no prospective natural-history cohort; no female-specific HH18 series; incomplete ClinVar/ACMG functional resolution for many alleles; no validated molecular biomarker; no *IL17RD*-specific treatment trial; and no human GnRH-neuron single-cell, spatial, organoid, or multi-omics model demonstrating the complete causal chain.

References

1. (miraoui2013mutationsinfgf17 pages 7-10): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

2. (miraoui2013mutationsinfgf17 pages 6-7): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

3. (oleari2021thedifferentialroles pages 2-4): Roberto Oleari, Valentina Massa, Anna Cariboni, and Antonella Lettieri. The differential roles for neurodevelopmental and neuroendocrine genes in shaping gnrh neuron physiology and deficiency. International Journal of Molecular Sciences, 22:9425, Aug 2021. URL: https://doi.org/10.3390/ijms22179425, doi:10.3390/ijms22179425. This article has 38 citations.

4. (OpenTargets Search: hypogonadotropic hypogonadism 18 with or without anosmia): Open Targets Query (hypogonadotropic hypogonadism 18 with or without anosmia, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (miraoui2013mutationsinfgf17 pages 14-15): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

6. (cannarella2023geneticanalysisof pages 5-8): Rossella Cannarella, Carmelo Gusmano, Rosita A. Condorelli, Andrea Bernini, Jurgen Kaftalli, Paolo Enrico Maltese, Stefano Paolacci, Astrit Dautaj, Giuseppe Marceddu, Matteo Bertelli, Sandro La Vignera, and Aldo E. Calogero. Genetic analysis of patients with congenital hypogonadotropic hypogonadism: a case series. Apr 2023. URL: https://doi.org/10.3390/ijms24087428, doi:10.3390/ijms24087428. This article has 11 citations.

7. (miraoui2013mutationsinfgf17 pages 4-6): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

8. (pande2021interleukin17receptord pages 1-2): Shivangi Pande, Xuehui Yang, and Robert Friesel. Interleukin-17 receptor d (sef) is a multi-functional regulator of cell signaling. Cell Communication and Signaling, Jan 2021. URL: https://doi.org/10.1186/s12964-020-00695-7, doi:10.1186/s12964-020-00695-7. This article has 34 citations and is from a peer-reviewed journal.

9. (pande2021interleukin17receptord pages 2-4): Shivangi Pande, Xuehui Yang, and Robert Friesel. Interleukin-17 receptor d (sef) is a multi-functional regulator of cell signaling. Cell Communication and Signaling, Jan 2021. URL: https://doi.org/10.1186/s12964-020-00695-7, doi:10.1186/s12964-020-00695-7. This article has 34 citations and is from a peer-reviewed journal.

10. (swee2019congenitalhypogonadotrophichypogonadism pages 2-3): Du Soon Swee and Richard Quinton. Congenital hypogonadotrophic hypogonadism: minipuberty and the case for neonatal diagnosis. Frontiers in Endocrinology, Feb 2019. URL: https://doi.org/10.3389/fendo.2019.00097, doi:10.3389/fendo.2019.00097. This article has 73 citations.

11. (young2019clinicalmanagementof pages 17-18): Jacques Young, Cheng Xu, Georgios E. Papadakis, J. Acierno, L. Maione, Johanna Hietamäki, T. Raivio, and N. Pitteloud. Clinical management of congenital hypogonadotropic hypogonadism. Endocrine reviews, 40 2:669-710, Apr 2019. URL: https://doi.org/10.1210/er.2018-00116, doi:10.1210/er.2018-00116. This article has 480 citations and is from a domain leading peer-reviewed journal.

12. (young2019clinicalmanagementof pages 10-11): Jacques Young, Cheng Xu, Georgios E. Papadakis, J. Acierno, L. Maione, Johanna Hietamäki, T. Raivio, and N. Pitteloud. Clinical management of congenital hypogonadotropic hypogonadism. Endocrine reviews, 40 2:669-710, Apr 2019. URL: https://doi.org/10.1210/er.2018-00116, doi:10.1210/er.2018-00116. This article has 480 citations and is from a domain leading peer-reviewed journal.

13. (sayed2023paneltestingfor pages 3-5): Yasmin Al Sayed and Sasha R. Howard. Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism – a clinical perspective. European Journal of Human Genetics, 31(4):387-394, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01261-0, doi:10.1038/s41431-022-01261-0. This article has 39 citations and is from a domain leading peer-reviewed journal.

14. (dwyer2024classesandpredictors pages 6-8): Andrew A Dwyer, Isabella R McDonald, Biagio Cangiano, Luca Giovanelli, Luigi Maione, Leticia F G Silveira, Taneli Raivio, Ana Claudia Latronico, Jacques Young, Richard Quinton, Marco Bonomi, Luca Persani, Stephanie B Seminara, and Christopher S Lee. Classes and predictors of reversal in male patients with congenital hypogonadotropic hypogonadism: a cross-sectional study of six international referral centres. The Lancet Diabetes &amp; Endocrinology, 12:257-266, Apr 2024. URL: https://doi.org/10.1016/s2213-8587(24)00028-7, doi:10.1016/s2213-8587(24)00028-7. This article has 19 citations and is from a highest quality peer-reviewed journal.

15. (alexander2024gonadotropinsforpubertal pages 1-2): Emma C Alexander, Duaa Faruqi, Robert Farquhar, Ayesha Unadkat, Kyla Ng Yin, Rebecca B. Hoskyns, Rachel Varughese, and Sasha R Howard. Gonadotropins for pubertal induction in males with hypogonadotropic hypogonadism: systematic review and meta-analysis. European Journal of Endocrinology, 190:S1-S11, Dec 2024. URL: https://doi.org/10.1093/ejendo/lvad166, doi:10.1093/ejendo/lvad166. This article has 53 citations and is from a highest quality peer-reviewed journal.

16. (dwyer2024classesandpredictors pages 1-3): Andrew A Dwyer, Isabella R McDonald, Biagio Cangiano, Luca Giovanelli, Luigi Maione, Leticia F G Silveira, Taneli Raivio, Ana Claudia Latronico, Jacques Young, Richard Quinton, Marco Bonomi, Luca Persani, Stephanie B Seminara, and Christopher S Lee. Classes and predictors of reversal in male patients with congenital hypogonadotropic hypogonadism: a cross-sectional study of six international referral centres. The Lancet Diabetes &amp; Endocrinology, 12:257-266, Apr 2024. URL: https://doi.org/10.1016/s2213-8587(24)00028-7, doi:10.1016/s2213-8587(24)00028-7. This article has 19 citations and is from a highest quality peer-reviewed journal.

17. (young2019clinicalmanagementof pages 23-24): Jacques Young, Cheng Xu, Georgios E. Papadakis, J. Acierno, L. Maione, Johanna Hietamäki, T. Raivio, and N. Pitteloud. Clinical management of congenital hypogonadotropic hypogonadism. Endocrine reviews, 40 2:669-710, Apr 2019. URL: https://doi.org/10.1210/er.2018-00116, doi:10.1210/er.2018-00116. This article has 480 citations and is from a domain leading peer-reviewed journal.

18. (young2019clinicalmanagementof pages 24-25): Jacques Young, Cheng Xu, Georgios E. Papadakis, J. Acierno, L. Maione, Johanna Hietamäki, T. Raivio, and N. Pitteloud. Clinical management of congenital hypogonadotropic hypogonadism. Endocrine reviews, 40 2:669-710, Apr 2019. URL: https://doi.org/10.1210/er.2018-00116, doi:10.1210/er.2018-00116. This article has 480 citations and is from a domain leading peer-reviewed journal.

19. (young2019clinicalmanagementof pages 7-8): Jacques Young, Cheng Xu, Georgios E. Papadakis, J. Acierno, L. Maione, Johanna Hietamäki, T. Raivio, and N. Pitteloud. Clinical management of congenital hypogonadotropic hypogonadism. Endocrine reviews, 40 2:669-710, Apr 2019. URL: https://doi.org/10.1210/er.2018-00116, doi:10.1210/er.2018-00116. This article has 480 citations and is from a domain leading peer-reviewed journal.

20. (pande2021interleukin17receptord pages 13-14): Shivangi Pande, Xuehui Yang, and Robert Friesel. Interleukin-17 receptor d (sef) is a multi-functional regulator of cell signaling. Cell Communication and Signaling, Jan 2021. URL: https://doi.org/10.1186/s12964-020-00695-7, doi:10.1186/s12964-020-00695-7. This article has 34 citations and is from a peer-reviewed journal.

21. (vezzoli2023geneticarchitectureof pages 3-5): Valeria Vezzoli, Faris Hrvat, Giovanni Goggi, Silvia Federici, Biagio Cangiano, Richard Quinton, Luca Persani, and Marco Bonomi. Genetic architecture of self-limited delayed puberty and congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Jan 2023. URL: https://doi.org/10.3389/fendo.2022.1069741, doi:10.3389/fendo.2022.1069741. This article has 27 citations.

22. (cannarella2023geneticanalysisof pages 4-5): Rossella Cannarella, Carmelo Gusmano, Rosita A. Condorelli, Andrea Bernini, Jurgen Kaftalli, Paolo Enrico Maltese, Stefano Paolacci, Astrit Dautaj, Giuseppe Marceddu, Matteo Bertelli, Sandro La Vignera, and Aldo E. Calogero. Genetic analysis of patients with congenital hypogonadotropic hypogonadism: a case series. Apr 2023. URL: https://doi.org/10.3390/ijms24087428, doi:10.3390/ijms24087428. This article has 11 citations.

23. (vezzoli2023geneticarchitectureof pages 2-3): Valeria Vezzoli, Faris Hrvat, Giovanni Goggi, Silvia Federici, Biagio Cangiano, Richard Quinton, Luca Persani, and Marco Bonomi. Genetic architecture of self-limited delayed puberty and congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Jan 2023. URL: https://doi.org/10.3389/fendo.2022.1069741, doi:10.3389/fendo.2022.1069741. This article has 27 citations.

24. (lewkowitzshpuntoff2012olfactoryphenotypicspectrum pages 1-2): Hilana M. Lewkowitz-Shpuntoff, Virginia A. Hughes, Lacey Plummer, Margaret G. Au, Richard L. Doty, Stephanie B. Seminara, Yee-Ming Chan, Nelly Pitteloud, William F. Crowley, and Ravikumar Balasubramanian. Olfactory phenotypic spectrum in idiopathic hypogonadotropic hypogonadism: pathophysiological and genetic implications. The Journal of clinical endocrinology and metabolism, 97 1:E136-44, Jan 2012. URL: https://doi.org/10.1210/jc.2011-2041, doi:10.1210/jc.2011-2041. This article has 142 citations.

25. (fanis2023gonadotropinreleasinghormonereceptor pages 14-15): Pavlos Fanis, Vassos Neocleous, Irene Papapetrou, Leonidas A. Phylactou, and Nicos Skordis. Gonadotropin-releasing hormone receptor (gnrhr) and hypogonadotropic hypogonadism. Nov 2023. URL: https://doi.org/10.3390/ijms242115965, doi:10.3390/ijms242115965. This article has 57 citations.

26. (pande2021interleukin17receptord pages 4-6): Shivangi Pande, Xuehui Yang, and Robert Friesel. Interleukin-17 receptor d (sef) is a multi-functional regulator of cell signaling. Cell Communication and Signaling, Jan 2021. URL: https://doi.org/10.1186/s12964-020-00695-7, doi:10.1186/s12964-020-00695-7. This article has 34 citations and is from a peer-reviewed journal.

27. (pande2021interleukin17receptord pages 6-8): Shivangi Pande, Xuehui Yang, and Robert Friesel. Interleukin-17 receptor d (sef) is a multi-functional regulator of cell signaling. Cell Communication and Signaling, Jan 2021. URL: https://doi.org/10.1186/s12964-020-00695-7, doi:10.1186/s12964-020-00695-7. This article has 34 citations and is from a peer-reviewed journal.

28. (swee2019managingcongenitalhypogonadotrophic pages 7-8): Du Soon Swee and Richard Quinton. Managing congenital hypogonadotrophic hypogonadism: a contemporary approach directed at optimizing fertility and long-term outcomes in males. Therapeutic Advances in Endocrinology and Metabolism, Feb 2019. URL: https://doi.org/10.1177/2042018819826889, doi:10.1177/2042018819826889. This article has 53 citations.

29. (sayed2023paneltestingfor pages 2-2): Yasmin Al Sayed and Sasha R. Howard. Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism – a clinical perspective. European Journal of Human Genetics, 31(4):387-394, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01261-0, doi:10.1038/s41431-022-01261-0. This article has 39 citations and is from a domain leading peer-reviewed journal.

30. (kim2015congenitalhypogonadotropichypogonadism pages 5-7): Soo-Hyun Kim. Congenital hypogonadotropic hypogonadism and kallmann syndrome: past, present, and future. Endocrinology and Metabolism, 30:456-466, Dec 2015. URL: https://doi.org/10.3803/enm.2015.30.4.456, doi:10.3803/enm.2015.30.4.456. This article has 167 citations and is from a peer-reviewed journal.

31. (young2019clinicalmanagementof pages 26-26): Jacques Young, Cheng Xu, Georgios E. Papadakis, J. Acierno, L. Maione, Johanna Hietamäki, T. Raivio, and N. Pitteloud. Clinical management of congenital hypogonadotropic hypogonadism. Endocrine reviews, 40 2:669-710, Apr 2019. URL: https://doi.org/10.1210/er.2018-00116, doi:10.1210/er.2018-00116. This article has 480 citations and is from a domain leading peer-reviewed journal.

32. (lee2022treatmentofcongenital pages 3-4): Hae Sang Lee, Young Suk Shim, and Jin Soon Hwang. Treatment of congenital hypogonadotropic hypogonadism in male patients. Sep 2022. URL: https://doi.org/10.6065/apem.2244208.104, doi:10.6065/apem.2244208.104. This article has 23 citations.

33. (alexander2024gonadotropinsforpubertal pages 3-5): Emma C Alexander, Duaa Faruqi, Robert Farquhar, Ayesha Unadkat, Kyla Ng Yin, Rebecca B. Hoskyns, Rachel Varughese, and Sasha R Howard. Gonadotropins for pubertal induction in males with hypogonadotropic hypogonadism: systematic review and meta-analysis. European Journal of Endocrinology, 190:S1-S11, Dec 2024. URL: https://doi.org/10.1093/ejendo/lvad166, doi:10.1093/ejendo/lvad166. This article has 53 citations and is from a highest quality peer-reviewed journal.

34. (swee2019managingcongenitalhypogonadotrophic pages 5-7): Du Soon Swee and Richard Quinton. Managing congenital hypogonadotrophic hypogonadism: a contemporary approach directed at optimizing fertility and long-term outcomes in males. Therapeutic Advances in Endocrinology and Metabolism, Feb 2019. URL: https://doi.org/10.1177/2042018819826889, doi:10.1177/2042018819826889. This article has 53 citations.

35. (lee2022treatmentofcongenital pages 2-3): Hae Sang Lee, Young Suk Shim, and Jin Soon Hwang. Treatment of congenital hypogonadotropic hypogonadism in male patients. Sep 2022. URL: https://doi.org/10.6065/apem.2244208.104, doi:10.6065/apem.2244208.104. This article has 23 citations.

36. (alexander2024gonadotropinsforpubertal pages 6-8): Emma C Alexander, Duaa Faruqi, Robert Farquhar, Ayesha Unadkat, Kyla Ng Yin, Rebecca B. Hoskyns, Rachel Varughese, and Sasha R Howard. Gonadotropins for pubertal induction in males with hypogonadotropic hypogonadism: systematic review and meta-analysis. European Journal of Endocrinology, 190:S1-S11, Dec 2024. URL: https://doi.org/10.1093/ejendo/lvad166, doi:10.1093/ejendo/lvad166. This article has 53 citations and is from a highest quality peer-reviewed journal.

37. (sayed2023paneltestingfor pages 1-2): Yasmin Al Sayed and Sasha R. Howard. Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism – a clinical perspective. European Journal of Human Genetics, 31(4):387-394, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01261-0, doi:10.1038/s41431-022-01261-0. This article has 39 citations and is from a domain leading peer-reviewed journal.

38. (pande2021interleukin17receptord pages 12-13): Shivangi Pande, Xuehui Yang, and Robert Friesel. Interleukin-17 receptor d (sef) is a multi-functional regulator of cell signaling. Cell Communication and Signaling, Jan 2021. URL: https://doi.org/10.1186/s12964-020-00695-7, doi:10.1186/s12964-020-00695-7. This article has 34 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hypogonadotropic_Hypogonadism_18_With_Or_Without_Anosmia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000806` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0008543` (2 mentions) - the report calls it "FGF receptor signaling", "fibroblast growth factor receptor signaling pathway"; GO calls it **fibroblast growth factor receptor signaling pathway**, and lists "FGF receptor signaling pathway" among its other names
- `GO:0050900` (1 mention) - the report calls it "leukocyte migration; only for immune studies"; GO calls it **leukocyte migration**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0008543` - called "FGF receptor signaling", "fibroblast growth factor receptor signaling pathway"
