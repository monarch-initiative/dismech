---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T14:26:39.868597'
end_time: '2026-09-03T14:40:46.420967'
duration_seconds: 846.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SPRY4-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism
    17 with or without anosmia; SPRY4/Sprouty4; OMIM 615266)
  mondo_id: MONDO:0014102
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 12
  verified: 10
  not_found: 0
  unverifiable: 2
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 10
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: SPRY4_Hypogonadotropic_Hypogonadism-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SPRY4-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 17 with or without anosmia; SPRY4/Sprouty4; OMIM 615266)
- **MONDO ID:** MONDO:0014102 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SPRY4-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 17 with or without anosmia; SPRY4/Sprouty4; OMIM 615266)** covering all of the
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
- **Disease Name:** SPRY4-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 17 with or without anosmia; SPRY4/Sprouty4; OMIM 615266)
- **MONDO ID:** MONDO:0014102 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SPRY4-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 17 with or without anosmia; SPRY4/Sprouty4; OMIM 615266)** covering all of the
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


# SPRY4-Related Hypogonadotropic Hypogonadism: Comprehensive Disease Report

## Executive summary and evidence limitations

**Hypogonadotropic hypogonadism 17 with or without anosmia (HH17; OMIM 615266)** is the disease label applied to congenital or isolated gonadotropin-releasing hormone (GnRH) deficiency associated with heterozygous variants in **SPRY4**, which encodes the fibroblast-growth-factor signaling inhibitor Sprouty-4. Patients may have Kallmann syndrome—hypogonadotropic hypogonadism with anosmia/hyposmia—or normosmic disease. However, the SPRY4 evidence base remains small, many reported alleles are variants of uncertain significance (VUS), and oligogenic inheritance is common. Thus, “SPRY4-associated” is generally more defensible than assuming that every rare SPRY4 allele causes a fully penetrant monogenic disorder. The foundational study screened 386 unrelated CHH probands and 155 controls and found SPRY4 variants in 14 probands; individual FGF-network genes each explained only approximately 1–4% of that referral cohort. [Miraoui et al., published May 2, 2013; DOI/URL: https://doi.org/10.1016/j.ajhg.2013.04.008; PMID 23643382] (miraoui2013mutationsinfgf17 pages 1-2, miraoui2013mutationsinfgf17 pages 4-6)

No substantial SPRY4-specific clinical or mechanistic studies from 2023–2024 were found. Recent advances instead concern CHH genetic-panel interpretation, differential diagnosis, fertility management, and prediction of disease reversal. These general CHH findings are identified explicitly below and should not be treated as SPRY4-specific observations. (dwyer2024classesandpredictors pages 9-11, dwyer2024classesandpredictors pages 3-4, sayed2023paneltestingfor pages 2-3, panel2024diagnosisandtreatment pages 34-35)

| Domain | SPRY4-specific finding | Evidence strength / source date | Knowledge-base interpretation |
|---|---|---|---|
| Disease definition | **SPRY4-related hypogonadotropic hypogonadism 17 with or without anosmia (HH17)** is a proposed rare genetic form of congenital/isolated GnRH deficiency. Presentations include Kallmann syndrome, normosmic hypogonadotropic hypogonadism, and one adult-onset case. (indirli2019ararespry4 pages 1-2, miraoui2013mutationsinfgf17 pages 1-2) | **Limited–moderate:** discovery cohort (2013); single case (2019) | Retain as an **SPRY4-associated CHH entity**, but do not assume every rare heterozygous SPRY4 variant is independently causal. |
| Human genetic evidence | In the foundational study, 386 unrelated CHH probands and 155 controls were screened; 14 probands carried SPRY4 variants. Individual FGF-network candidate genes each accounted for approximately 1–4% of cases. (miraoui2013mutationsinfgf17 pages 1-2, miraoui2013mutationsinfgf17 pages 4-6) | **Moderate association evidence:** candidate-gene case–control study (2013) | Supports association with the CHH spectrum, although variant-level pathogenicity and monogenic sufficiency remain uncertain. |
| **p.Ser241Tyr** | Heterozygous **NM_030964.3:c.722C>A, p.(Ser241Tyr), rs139512218** occurred in Kallmann and normosmic CHH cases, often with variants in **FGFR1, DUSP6,** or **TACR3**. The original study reported control and CHH minor-allele frequencies of 0.6% and 0.5%, respectively; later sources classify it as a VUS. (miraoui2013mutationsinfgf17 pages 12-14, gach2020newfindingsin pages 4-4) | **Conflicting:** human VUS/association evidence (2013–2020); functional evidence (2021) | Do **not** classify as pathogenic solely from case occurrence or in-vitro function. Population frequency, occurrence in controls, and oligogenic context weaken a highly penetrant monogenic interpretation. |
| p.Ser241Tyr function | Tyr241 increased SPRY4 inhibition of **FGF-induced MAPK/ERK signaling** without increasing inhibition of EGF signaling. It reduced WI-38 migration to **9.106 ± 0.305 μm/h**, versus **11.77 ± 0.685 μm/h** for wild type and **12.36 ± 0.781 μm/h** for control, and prolonged approximate doubling time from 10 to 15 days. (stutz2021asprouty4mutation pages 1-2, stutz2021asprouty4mutation pages 4-7, stutz2021asprouty4mutation pages 9-10) | **Moderate functional, low disease-specific:** non-neuronal in-vitro assays (2021) | Supports an **FGF-selective inhibitory hypermorph**, but the assays did not use olfactory ensheathing cells or GnRH neurons and do not establish clinical pathogenicity. |
| **p.Lys177Arg** | Heterozygous **c.530A>G, p.(Lys177Arg)** was reported in a male with Kallmann syndrome, underdeveloped genitalia, and diagnosis at age 13; it was maternally inherited and classified as a **VUS**. (gach2020newfindingsin pages 2-4, gach2020newfindingsin pages 5-5) | **Weak:** single-patient observation without functional validation (2020) | Record as a reported SPRY4 VUS, not a confirmed causal allele. Maternal transmission alone does not establish dominant inheritance or penetrance. |
| **p.Arg53Gln** | Heterozygous **c.158G>A, p.(Arg53Gln)** was the only finding on a 28-locus panel in one man with congenital severe hyposmia, absent olfactory bulbs and tracts, normal puberty, and adult-onset central hypogonadism at age 48. No segregation or functional analysis was reported. (indirli2019ararespry4 pages 1-2, indirli2019ararespry4 pages 2-4) | **Weak:** single case report (2019) | Treat as a **candidate/VUS-level association**. The olfactory phenotype is supportive, but causality and monogenic sufficiency are unproven. |
| Oligogenicity and inheritance | SPRY4 variants have co-occurred with variants in **FGFR1, DUSP6, TACR3, SEMA3A, PROKR2,** and **NSMF**. In the 2013 European subset, 24 of 124 variant-positive probands had variants in different genes: **19% oligogenicity** (95% CI 12–26%); 23 of 24 combinations included an FGF-network gene. (miraoui2013mutationsinfgf17 pages 12-14) | **Moderate for FGF-network oligogenicity; limited for specific SPRY4 interactions:** 2013–2020 | Model inheritance as potentially **autosomal dominant with incomplete penetrance or oligogenic**, while noting that no definitive SPRY4-specific rule is established. |
| Mechanism | SPRY4 negatively regulates receptor-tyrosine-kinase signaling, especially the **FGF–FGFR–RAS–MAPK/ERK axis**. Excess inhibition by selected variants is hypothesized to impair FGF-dependent olfactory-system development and GnRH-neuron specification, survival, or migration. (miraoui2013mutationsinfgf17 pages 3-4, stutz2021asprouty4mutation pages 1-2, stutz2021asprouty4mutation pages 9-10) | **Moderate pathway evidence; inferred developmental chain:** 2013–2021 | Annotate: SPRY4 hyperactivity → reduced FGF/MAPK signaling → impaired olfactory/GnRH development → anosmia and GnRH deficiency. Label the neuronal steps as **inferred**. |
| Phenotype range | Reported findings include anosmia or hyposmia, olfactory-bulb hypoplasia or aplasia, normosmic CHH, delayed or absent puberty, underdeveloped male genitalia, low libido, infertility, and adult-onset sexual dysfunction. Hearing loss and dental abnormalities occurred among some early carriers, but frequencies are unavailable. (indirli2019ararespry4 pages 2-4, indirli2019ararespry4 pages 5-6, gach2020newfindingsin pages 2-4) | **Limited:** small numbers, mixed variants, and oligogenic cases (2013–2020) | Use qualitative frequencies such as **reported** or **variable**; reliable SPRY4-specific percentages cannot be calculated. |
| Diagnostics | Diagnosis uses pubertal or adult symptoms, low sex steroids with low or inappropriately normal LH/FSH, exclusion of acquired hypothalamic–pituitary disease, smell testing, and pituitary/olfactory MRI when indicated. CHH panels identify variants of interest in approximately **21–51%** of patients; SPRY4 is less frequently implicated. (indirli2019ararespry4 pages 2-4, dwyer2024classesandpredictors pages 3-4, sayed2023paneltestingfor pages 2-3) | **Strong for general CHH work-up; limited SPRY4-specific utility:** 2019–2024 | Prefer a multigene CHH/Kallmann panel or exome/genome analysis over SPRY4-only testing. Apply ACMG/AMP criteria and assess population frequency, segregation, phenotype, function, and oligogenic context. |
| Treatment | No SPRY4-specific therapy exists. Testosterone improved sexual symptoms in the adult-onset p.Arg53Gln case. General CHH treatment uses sex steroids for pubertal induction or maintenance and **hCG followed by FSH**, combined gonadotropins, or pulsatile GnRH for fertility; testosterone suppresses spermatogenesis. (indirli2019ararespry4 pages 2-4, dwyer2024classesandpredictors pages 3-4, panel2024diagnosisandtreatment pages 34-35) | **Strong for general CHH; single-case SPRY4 outcome:** 2019–2024 | Management is directed by phenotype and fertility goals, not SPRY4 genotype. Patients pursuing fertility require gonadotropins or GnRH rather than testosterone alone. |
| Epidemiology | No incidence, prevalence, carrier frequency, founder effect, ethnic enrichment, or sex ratio is established for HH17. SPRY4 variants occurred in 14 of 386 probands in the discovery study and 2 of 47 in a Polish cohort, but these are referral-cohort detection rates. (miraoui2013mutationsinfgf17 pages 1-2, gach2020newfindingsin pages 2-4) | **Insufficient:** ascertainment-biased cohorts (2013–2020) | Mark disease-specific epidemiology as **unknown**; do not convert variant-detection proportions into population prevalence. |
| Mouse model | **Spry4-null mice** are viable and fertile, although some die neonatally with mandibular defects and others show growth retardation and polysyndactyly; embryonic fibroblasts have increased FGF-induced ERK activation. Combined Spry2/Spry4 loss is embryonic lethal. (stutz2021asprouty4mutation pages 1-2) | **Moderate developmental/pathway evidence:** knockout findings summarized in 2021 | The knockout models loss of negative regulation, whereas p.Ser241Tyr behaves as an inhibitory hypermorph. Simple Spry4 loss does not reproduce human HH17 convincingly, and olfactory/GnRH phenotypes remain insufficiently characterized. |


*Table: Evidence-grade summary of SPRY4-associated HH17, emphasizing variant uncertainty, oligogenic inheritance, the proposed FGF–MAPK mechanism, and limits of clinical and animal-model evidence.*

## 1. Disease information

HH17 is a rare neurodevelopmental–endocrine disorder in which deficient GnRH secretion or action produces low sex-steroid concentrations with low or inappropriately normal LH and FSH. Complete anosmia with CHH is conventionally termed Kallmann syndrome; preserved smell defines normosmic CHH. Severe disease can present during neonatal “mini-puberty” with micropenis or cryptorchidism, whereas later presentations include absent/arrested puberty and infertility. A reported SPRY4 carrier instead underwent normal puberty and developed central hypogonadism at age 48, demonstrating that the associated phenotype need not be clinically congenital. (indirli2019ararespry4 pages 1-2, indirli2019ararespry4 pages 2-4, dwyer2024classesandpredictors pages 3-4)

**Identifiers and terminology**

- Disease: hypogonadotropic hypogonadism 17 with or without anosmia; HH17; SPRY4-related isolated/congenital hypogonadotropic hypogonadism; SPRY4-related Kallmann syndrome.
- OMIM: **615266**.
- Gene/protein: **SPRY4**, Sprouty RTK signaling antagonist 4/Sprouty-4; OMIM **607984**; chromosome **5q31.3**. (miraoui2013mutationsinfgf17 pages 3-4, sayed2023paneltestingfor pages 2-3)
- MONDO: the requested mapping is **MONDO:0014102**, but it should be independently checked against the current MONDO release before database import. The available Open Targets lookup did not return an HH17–SPRY4 association and instead surfaced neighboring numbered HH entities, illustrating incomplete cross-resource harmonization. (OpenTargets Search: hypogonadotropic hypogonadism 17 with or without anosmia-SPRY4)
- Orphanet, MeSH, ICD-10 and ICD-11: no retrieved evidence established a dedicated SPRY4/HH17 code. Cases are ordinarily represented under broader congenital/isolated hypogonadotropic hypogonadism or Kallmann syndrome concepts; nonspecific endocrine codes should not be presented as exact HH17 identifiers.

The evidence is **aggregated disease-level literature plus a very small number of individual published patients**, not an EHR-derived population dataset. The adult-onset p.Arg53Gln report is explicitly a single patient. (indirli2019ararespry4 pages 1-2, miraoui2013mutationsinfgf17 pages 1-2)

## 2. Etiology, risk, protective, and environmental factors

The initiating factor is a **germline SPRY4 sequence variant**, usually heterozygous, that is hypothesized to alter negative regulation of FGF–FGFR signaling. For p.Ser241Tyr, experimental evidence indicates a gain of inhibitory function rather than SPRY4 loss of function. Other alleles have not been comparably validated. (stutz2021asprouty4mutation pages 1-2, stutz2021asprouty4mutation pages 9-10)

Genetic risk is likely context-dependent. SPRY4 variants have co-occurred with variants in **FGFR1, DUSP6, TACR3, SEMA3A, PROKR2, and NSMF**, supporting an oligogenic burden model. In the European-ancestry subset of the original FGF-network study, 24/124 variant-positive probands had variants in different genes—19%, 95% CI 12–26%—and 23/24 combinations included an FGF-network gene. This is strong evidence for CHH/FGF-network oligogenicity but not proof that every individual SPRY4 combination is pathogenic. (miraoui2013mutationsinfgf17 pages 12-14)

No validated SPRY4-specific environmental, infectious, toxic, occupational, dietary, lifestyle, epigenetic, or protective factor was identified. The adult-onset report proposed—without demonstrating—that modifying genes, intrauterine factors, or acquired environmental influences could affect penetrance. There are likewise no established gene–environment interactions, protective alleles, vaccines, or prophylactic drugs. (indirli2019ararespry4 pages 5-6)

## 3. Phenotypes

Reliable SPRY4-specific percentages cannot be calculated because carriers are few, variants differ, and several cases are oligogenic. Appropriate database frequency labels are therefore **reported**, **variable**, or **unknown**, not percentages extrapolated from CHH cohorts.

- **Hypogonadotropic hypogonadism**—laboratory/clinical phenotype; congenital, pubertal, or rarely adult-onset; severity variable. Suggested HPO: **HP:0000044**.
- **Delayed, arrested, or absent puberty**—clinical sign, generally apparent in adolescence and chronic without treatment. HPO: **HP:0000823**; absent secondary sexual characteristics: **HP:0008187**.
- **Anosmia/hyposmia**—congenital sensory sign in Kallmann presentations; typically stable. HPO: **HP:0000458**, **HP:0004409**. Normosmia is also documented. (indirli2019ararespry4 pages 2-4, gach2020newfindingsin pages 2-4)
- **Olfactory-bulb/tract aplasia or hypoplasia**—MRI sign. In the p.Arg53Gln patient, bulbs and tracts were absent and olfactory sulci hypoplastic, while hypothalamus, pituitary and stalk were normal. Suggested HPO: abnormality of the olfactory bulb **HP:0002033**. (indirli2019ararespry4 pages 1-2, indirli2019ararespry4 pages 2-4)
- **Micropenis/underdeveloped male genitalia and cryptorchidism**—neonatal or childhood markers of severe prenatal/mini-pubertal GnRH deficiency; not present in the adult-onset case, but underdeveloped genitalia occurred in the p.Lys177Arg case. HPO: **HP:0000054**, **HP:0000028**. (indirli2019ararespry4 pages 1-2, gach2020newfindingsin pages 2-4, dwyer2024classesandpredictors pages 3-4)
- **Infertility, low libido, reduced erections/erectile dysfunction**—adult reproductive symptoms. HPO: **HP:0000789**, decreased libido **HP:0000158**, erectile dysfunction **HP:0000802**. The p.Arg53Gln patient developed sexual symptoms at 48 years. (indirli2019ararespry4 pages 1-2, indirli2019ararespry4 pages 2-4)
- **Low testosterone or estradiol with low/inappropriately normal LH and FSH**—core biochemical abnormality. The adult-onset male had testosterone of 6.8 and 5.8 nmol/L on consecutive assessments. (indirli2019ararespry4 pages 1-2)
- Hearing loss and abnormal dentition were described among four earlier SPRY4-variant carriers, but neither frequency nor variant-specific causality is established. Suggested HPO: sensorineural hearing impairment **HP:0000407** and hypodontia **HP:0000668**. (indirli2019ararespry4 pages 5-6)

Untreated pubertal delay, infertility, sexual dysfunction, and impaired body composition/bone health can substantially reduce psychosocial and physical quality of life, but no EQ-5D, SF-36, PROMIS, or SPRY4-specific quality-of-life dataset was identified. General CHH literature supports early treatment to improve sexual development, fertility potential, and psychological well-being. (vezzoli2023geneticarchitectureof pages 2-3)

## 4. Genetic and molecular information

**SPRY4** is the only defining gene for HH17. The retrieved literature did not establish pathogenic SPRY4 deletions, duplications, translocations, repeat expansions, mitochondrial variants, or somatic disease alleles. Reported HH variants are germline heterozygous missense substitutions.

1. **NM_030964.3:c.722C>A, p.(Ser241Tyr), rs139512218.** This allele occurred in both Kallmann and normosmic CHH and alongside FGFR1, DUSP6, or TACR3 variants. In the original dataset, its MAF was 0.6% in controls and 0.5% in CHH—evidence against a highly penetrant monogenic pathogenic allele. It is reported as a ClinVar VUS and was maternally inherited in a later case. Nevertheless, cell assays indicate an FGF-selective inhibitory hypermorph. It should remain VUS/conflicting rather than being upgraded solely on functional evidence. (miraoui2013mutationsinfgf17 pages 12-14, gach2020newfindingsin pages 4-4)
2. **c.530A>G, p.(Lys177Arg).** Maternally inherited VUS in a male diagnosed with Kallmann syndrome at 13 years and underdeveloped genitalia; no direct functional validation. (gach2020newfindingsin pages 2-4, gach2020newfindingsin pages 5-5)
3. **c.158G>A, p.(Arg53Gln).** Rare heterozygous allele, reported MAF <0.01, found as the sole result on a 28-locus panel in one man with congenital severe hyposmia and adult-onset HH. No family segregation or functional test was reported; candidate/VUS-level evidence is appropriate. (indirli2019ararespry4 pages 1-2, indirli2019ararespry4 pages 2-4)

No validated SPRY4 modifier gene, disease-specific DNA methylation signature, histone alteration, or chromatin defect is known. The co-occurring genes listed above are better treated as potential **oligogenic partners** than proven modifiers.

## 5. Environmental information

No SPRY4-specific association with smoking, alcohol, diet, exercise, endocrine disruptors, pollution, radiation, medications, occupational agents, or infection has been demonstrated. Acquired functional hypogonadotropic hypogonadism caused by undernutrition, excessive exercise, severe illness, medication, or pituitary disease belongs in the differential diagnosis, not in HH17 etiology. No pathogen or zoonotic mechanism applies. (panel2024diagnosisandtreatment pages 34-35)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A function-altering germline **SPRY4** allele—demonstrated for p.Ser241Tyr as increased inhibitory activity—**leads to** excessive restraint of FGF-responsive signaling. (stutz2021asprouty4mutation pages 1-2, stutz2021asprouty4mutation pages 9-10)
2. Excess SPRY4 inhibition **leads to** reduced FGFR-driven RAS–RAF–MEK–ERK/MAPK output; p.Ser241Tyr inhibited FGF- but not EGF-induced signaling in vitro. (stutz2021asprouty4mutation pages 1-2, stutz2021asprouty4mutation pages 9-10)
3. Reduced FGF/MAPK signaling is **inferred to lead to** impaired olfactory-placode patterning, olfactory axon/ensheathing-cell development, and/or GnRH-neuron specification, survival, or migration. These neuronal consequences have not been demonstrated directly in SPRY4-mutant human GnRH cells. (miraoui2013mutationsinfgf17 pages 3-4, cho2019nasalplacodedevelopment pages 19-20)
4. Branch A: impaired olfactory development **leads to** hypoplastic/absent olfactory bulbs and anosmia/hyposmia (Kallmann phenotype). Branch B: deficient hypothalamic GnRH neuronal number/function **leads to** reduced pulsatile GnRH drive. (indirli2019ararespry4 pages 1-2, indirli2019ararespry4 pages 2-4)
5. Reduced GnRH drive **results in** low or inappropriately normal LH/FSH, which **leads to** reduced gonadal sex-steroid synthesis and impaired gametogenesis. (dwyer2024classesandpredictors pages 3-4, panel2024diagnosisandtreatment pages 34-35)
6. Sex-steroid and gametogenic failure **results in** absent/arrested puberty, undervirilization or amenorrhea, sexual dysfunction, and infertility. (dwyer2024classesandpredictors pages 3-4)

Sprouty proteins are intracellular antagonists of receptor-tyrosine-kinase signaling, with strongest evidence for modulation of FGF-induced MAPK/ERK; occasional PI3K and phospholipase-C effects are described, but no HH17-specific metabolic, immune, inflammatory, apoptotic, autophagic, fibrotic, or oxidative-stress mechanism is established. (stutz2021asprouty4mutation pages 1-2)

In WI-38 human embryonic fibroblasts, p.Ser241Tyr reduced migration to **9.106 ± 0.305 μm/h**, compared with **11.77 ± 0.685 μm/h** for wild-type SPRY4 and **12.36 ± 0.781 μm/h** for control, and prolonged approximate doubling time from 10 to 15 days. These assays support altered migration/proliferation but used lung fibroblasts and U2OS osteosarcoma cells—not olfactory or GnRH neurons. The authors’ abstract states directly: “the described Spry4 mutation creates a hyperactive version of a selective inhibitory molecule and can thereby contribute to a weakened FGF signaling.” [Stütz et al., published February 21, 2021; https://doi.org/10.3390/ijms22042145] (stutz2021asprouty4mutation pages 1-2, stutz2021asprouty4mutation pages 4-7)

Suggested ontology annotations include **FGF receptor signaling pathway** (GO:0008543), **MAPK cascade** (GO:0000165), **negative regulation of ERK1/ERK2 cascade** (GO:0070373), **neuron migration** (GO:0001764), **olfactory bulb development** (GO:0021772), and **regulation of gonadotropin secretion** (GO:0032276). Relevant cells are GnRH neurons, olfactory sensory neurons, olfactory ensheathing glia, pituitary gonadotrophs, Leydig cells, Sertoli cells, ovarian granulosa cells, and theca cells; exact CL identifiers should be checked in the target ontology release.

Available expression analysis is indirect: SPRY4 expression was higher in cultured olfactory ensheathing cells than in olfactory sensory neurons or adult mouse GnRH-neuron datasets. No HH17 patient single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, multi-omic, or CRISPR-screen dataset was found. (cho2019nasalplacodedevelopment pages 19-20)

## 7. Anatomical structures affected

The primary system is the **hypothalamic–pituitary–gonadal axis**. Direct or developmental sites include nasal/olfactory placode, olfactory epithelium and axonal scaffold, olfactory bulbs/tracts, preoptic–hypothalamic GnRH neuronal network, pituitary gonadotrophs functionally downstream, and testes or ovaries secondarily deprived of gonadotropin stimulation. (indirli2019ararespry4 pages 2-4, miraoui2013mutationsinfgf17 pages 3-4, dwyer2024classesandpredictors pages 3-4)

Suggested UBERON concepts are olfactory epithelium, olfactory bulb (**UBERON:0002264**), olfactory tract, hypothalamus (**UBERON:0001898**), pituitary gland (**UBERON:0000007**), testis (**UBERON:0000473**), and ovary (**UBERON:0000992**). Relevant subcellular locations include cytosol, plasma-membrane-associated RTK signaling complexes, and ERK-containing signaling compartments; suitable GO cellular-component terms include cytoplasm (**GO:0005737**) and plasma membrane (**GO:0005886**). Olfactory involvement is generally bilateral; no consistent lateralization is reported.

## 8. Temporal development and course

The initiating developmental susceptibility is prenatal, when olfactory and GnRH systems form, but clinical recognition varies:

- neonatal/infantile: micropenis or cryptorchidism from deficient prenatal/mini-pubertal HPG activation;
- adolescence: absent or arrested puberty, small testes, or primary amenorrhea;
- adulthood: infertility or sexual dysfunction;
- exceptional SPRY4 report: congenital hyposmia with normal puberty and HH emerging at 48 years. (indirli2019ararespry4 pages 1-2, indirli2019ararespry4 pages 2-4, dwyer2024classesandpredictors pages 3-4)

The condition is generally chronic but variable. General CHH—not SPRY4-specific—reverses in approximately **10–15%** of cases after sex-steroid, gonadotropin, or pulsatile-GnRH treatment. In a 2024 six-center study, reversal occurred at mean age 27.4 years, and oligogenicity was less common among reversals than non-reversals (29.3% versus 58.9%). Relapse can occur, so recovery requires continued surveillance. No SPRY4-specific reversal rate is available. [Dwyer et al., published April 2024; https://doi.org/10.1016/S2213-8587(24)00028-7] (dwyer2024classesandpredictors pages 9-11, dwyer2024classesandpredictors pages 3-4)

Critical intervention windows include mini-puberty/early infancy in severely affected boys, timely adolescent pubertal induction for bone and psychosocial health, and fertility-directed gonadotropin treatment before prolonged unopposed testosterone exposure where feasible.

## 9. Inheritance and population

Reported SPRY4 alleles are heterozygous and the disease label is commonly treated as autosomal dominant. Nevertheless, maternal transmission to an affected male, occurrence in controls, variable olfactory/reproductive phenotypes, and frequent second-gene variants indicate **incomplete penetrance, variable expressivity, and possible oligogenic inheritance**. No anticipation, germline mosaicism, founder effect, consanguinity association, or reliable carrier frequency has been established. (miraoui2013mutationsinfgf17 pages 12-14, gach2020newfindingsin pages 5-5, gach2020newfindingsin pages 4-4)

HH17-specific incidence, prevalence, sex ratio, age distribution, ancestry enrichment, and geographic distribution are unknown. Detection of SPRY4 variants in 14/386 discovery probands and 2/47 Polish patients are referral-cohort variant yields—not population prevalence estimates. General CHH is approximately fourfold more frequently diagnosed in males, but ascertainment and subtler female phenotypes contribute to this imbalance. (miraoui2013mutationsinfgf17 pages 1-2, dwyer2024classesandpredictors pages 3-4, gach2020newfindingsin pages 2-4)

## 10. Diagnostics

### Clinical and laboratory evaluation

Diagnosis requires compatible reproductive development plus low testosterone/estradiol with low or inappropriately normal LH and FSH, after excluding identifiable hypothalamic–pituitary or systemic causes. The 2024 reversal study operationalized male CHH as absent/incomplete puberty by 18 years, testosterone <6 nmol/L, low/inappropriately normal gonadotropins, and no acquired hypothalamic/pituitary cause; testes <4 mL defined absent puberty. (dwyer2024classesandpredictors pages 3-4)

Recommended evaluation includes detailed neonatal and pubertal history; Tanner stage and testicular volume; micropenis/cryptorchidism; menstruation and secondary sexual characteristics; formal or validated smell assessment; LH, FSH and sex steroids; prolactin, thyroid and other pituitary hormones; iron studies and systemic evaluation as indicated; semen analysis in adult men; pelvic ultrasound in females when appropriate; bone age and bone-density assessment; and MRI of pituitary/hypothalamus and olfactory structures when clinically indicated. GnRH stimulation, overnight LH pulsatility, inhibin B, AMH, INSL3, and hCG-stimulated testosterone can support assessment but are not individually definitive in distinguishing CHH from self-limited delayed puberty. (indirli2019ararespry4 pages 2-4, vezzoli2023geneticarchitectureof pages 2-3)

### Genetic testing

A contemporary multigene CHH/Kallmann panel is preferable to SPRY4-only sequencing because more than 60 genes may contribute and oligogenic findings are common. Panel-based studies identify a potentially relevant variant in approximately **21–51%** of CHH/KS patients. SPRY4 is a less frequently identified gene and should be interpreted under ACMG/AMP criteria with phenotype concordance, ancestry-matched population frequency, segregation, functional evidence, and second-gene burden. Exome or genome sequencing is appropriate after a nondiagnostic panel or when syndromic/structural disease is suspected; RNA sequencing remains investigational. CMA is reasonable for congenital anomalies or neurodevelopmental features; routine karyotype, FISH, mitochondrial, or repeat-expansion testing is not indicated specifically for HH17. [Al Sayed & Howard, published 2023; https://doi.org/10.1038/s41431-022-01261-0] (sayed2023paneltestingfor pages 2-3)

### Differential diagnosis

Exclude self-limited delayed puberty; functional hypothalamic amenorrhea from undernutrition/exercise/stress; chronic systemic disease; hyperprolactinemia; pituitary/suprasellar tumors; hemochromatosis, sarcoidosis, tuberculosis or histiocytosis; head trauma or pituitary apoplexy; exogenous androgens, opioids and other suppressive drugs; and syndromic/genetic CHH involving ANOS1, FGFR1/FGF8, CHD7, PROK2/PROKR2, GNRHR, KISS1R, TAC3/TACR3, SOX10 and others. The 2023 delayed-puberty study found classical HH-associated features in 38.5% of HH versus 15.4% of self-limited delayed puberty, but biochemical overlap remained substantial. (vezzoli2023geneticarchitectureof pages 2-3, panel2024diagnosisandtreatment pages 34-35)

Population newborn screening is unavailable. Targeted cascade testing and longitudinal follow-up are reasonable in relatives once a genuinely pathogenic familial variant is established. In isolated congenital anosmia, genetic evaluation may identify individuals requiring reproductive follow-up because the p.Arg53Gln case developed HH decades later. (indirli2019ararespry4 pages 1-2)

## 11. Outcome and prognosis

HH17 is not known to shorten life expectancy, and no disease-specific mortality or survival statistic exists. Principal morbidity is absent/incomplete sexual development, infertility, sexual dysfunction, reduced bone mass if sex-steroid deficiency is prolonged, and psychosocial burden. Smell loss is usually persistent, while endocrine manifestations are treatable. Testosterone normalized levels and improved sexual symptoms in the adult-onset SPRY4 case. (indirli2019ararespry4 pages 2-4)

General CHH fertility is often recoverable: approximately **75% of affected males** can achieve spermatogenesis/fertility with FSH plus hCG or pulsatile GnRH, although outcomes are poorer with cryptorchidism and very small pretreatment testes. Approximately 10–15% undergo endocrine reversal; larger baseline testes predict reversal, whereas cryptorchidism and oligogenicity are unfavorable markers. These figures cannot be assumed to represent HH17 specifically. (dwyer2024classesandpredictors pages 9-11, dwyer2024classesandpredictors pages 3-4)

## 12. Treatment and current implementation

No approved SPRY4-directed, gene, cell, RNA, CRISPR, immunologic, or pathway-targeted therapy exists. Treatment follows CHH phenotype and reproductive goals.

- **Puberty/maintenance:** gradually titrated testosterone in males; estradiol followed by cyclic progestogen in females with a uterus. Suggested NCIT concepts: Testosterone (NCIT:C862), Estradiol (NCIT:C483), hormone replacement therapy.
- **Male fertility:** hCG to stimulate Leydig-cell testosterone, adding FSH after testosterone normalization; the 2024 AUA/ASRM guideline gives hCG **500–2,500 IU two to three times weekly**, with response related to pretreatment testicular size. Pulsatile GnRH is an alternative where available. Exogenous testosterone should not be used when current or future fertility is desired because it suppresses intratesticular testosterone and spermatogenesis. [AUA/ASRM guideline, amended 2024] (panel2024diagnosisandtreatment pages 34-35)
- **Female fertility:** pulsatile GnRH for hypothalamic deficiency or individualized gonadotropin ovulation induction. A 2023 CHH case achieved twin delivery after personalized hMG plus recombinant LH, illustrating real-world feasibility but not SPRY4-specific efficacy.
- **Supportive care:** bone-health monitoring, adequate calcium/vitamin D and weight-bearing activity, sexual and psychological support, fertility counseling, cryptorchidism management, and hearing/dental assessment when indicated.

Retrieved ClinicalTrials.gov examples were general HH/IHH rather than SPRY4-genotype trials: **NCT00064987** (FSH/testicular development; terminated; n=19), **NCT02880280** (hMG+hCG; phase 4; n=40), **NCT01403532** (sequential therapy; completed phase 4; n=100), and **NCT03687606** (hCG versus hCG+hMG; phase 4; n=210). These investigate endocrine replacement/fertility induction, not molecular correction of SPRY4 signaling.

No SPRY4 pharmacogenomic association or genotype-guided dose recommendation is established. Suggested NCIT intervention terms include gonadotropin therapy, human chorionic gonadotropin, follicle-stimulating hormone, gonadotropin-releasing hormone, testosterone replacement therapy, estrogen replacement therapy, and ovulation induction.

## 13. Prevention

Primary prevention of a de novo or inherited developmental allele through lifestyle change is not possible. No vaccine, environmental avoidance program, or prophylactic medication applies. Secondary prevention consists of early recognition in infants with micropenis/cryptorchidism, adolescents with pubertal delay, adults with infertility, and individuals with congenital anosmia; prompt hormonal treatment helps prevent impaired bone accrual, psychosocial consequences, and delayed fertility care. Tertiary prevention includes sustained sex-steroid replacement, bone surveillance, fertility-preserving treatment, and management of cryptorchidism and associated sensory/dental abnormalities. (vezzoli2023geneticarchitectureof pages 2-3, dwyer2024classesandpredictors pages 3-4)

Genetic counseling should emphasize uncertain penetrance, variable expressivity, possible oligogenicity, and the danger of using a VUS for irreversible reproductive decisions. Cascade, prenatal, or preimplantation testing is appropriate only after expert confirmation of a pathogenic/likely pathogenic familial allele and a defensible inheritance model.

## 14. Other species and natural disease

No naturally occurring SPRY4-associated hypogonadotropic-hypogonadism syndrome was identified in companion animals, livestock, or wildlife; no breed/VBO association or veterinary prevalence is established. The disorder is noninfectious and nonzoonotic. Orthologous **Spry4** is evolutionarily conserved in vertebrates, supporting comparative FGF-signaling studies, but conservation alone does not establish animal disease.

## 15. Model organisms and experimental systems

**Mouse (Mus musculus; NCBI Taxon 10090):** Spry4-null mice are viable and fertile, although a subset dies shortly after birth with mandibular defects; growth retardation and polysyndactyly occur. Their embryonic fibroblasts show increased FGF-induced ERK activation, and combined Spry2/Spry4 deletion is embryonic lethal. This knockout models loss of FGF restraint—the opposite direction from inhibitory-hypermorph p.Ser241Tyr—and does not convincingly reproduce human HH17. Olfactory and GnRH-neuron phenotypes were not sufficiently characterized in the retrieved evidence. (stutz2021asprouty4mutation pages 1-2)

**Human cellular models:** adenoviral wild-type and p.Ser241Tyr SPRY4 were studied in WI-38 embryonic lung fibroblasts and U2OS osteosarcoma cells. These systems demonstrate FGF-selective MAPK inhibition and reduced migration/proliferation but lack disease-relevant GnRH neurons, olfactory sensory neurons, or olfactory ensheathing cells. (stutz2021asprouty4mutation pages 1-2, stutz2021asprouty4mutation pages 4-7, stutz2021asprouty4mutation pages 9-10)

**Future high-value models:** patient-derived iPSCs differentiated into GnRH neurons and olfactory lineages; isogenic CRISPR-corrected controls; knock-in p.Ser241Tyr mice or organoids; and single-cell/spatial profiling of olfactory–GnRH development. Human stem-cell-derived GnRH neurons can exhibit approximately 60-minute pulsatile GnRH release and respond to FGF8/kisspeptin, providing a feasible platform, although no SPRY4 HH17 line was identified.

## Overall interpretation

The most defensible current model is that rare SPRY4 variants can **contribute** to the CHH/Kallmann spectrum by perturbing FGF–MAPK signaling, frequently in an incompletely penetrant or oligogenic context. p.Ser241Tyr has strong biochemical evidence for an inhibitory hypermorph but problematic case–control frequency and VUS classification; p.Lys177Arg and p.Arg53Gln have only limited patient-level evidence. Accordingly, an HH17 knowledge-base entry should preserve the OMIM disease concept while marking variant pathogenicity, penetrance, disease-specific epidemiology, and most genotype–phenotype frequencies as unresolved. Recent 2023–2024 work strengthens multigene testing and individualized CHH management, but it does not yet validate a SPRY4-specific diagnostic criterion or therapy. (dwyer2024classesandpredictors pages 9-11, miraoui2013mutationsinfgf17 pages 12-14, stutz2021asprouty4mutation pages 9-10, sayed2023paneltestingfor pages 2-3)

References

1. (miraoui2013mutationsinfgf17 pages 1-2): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

2. (miraoui2013mutationsinfgf17 pages 4-6): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

3. (dwyer2024classesandpredictors pages 9-11): Andrew A Dwyer, Isabella R McDonald, Biagio Cangiano, Luca Giovanelli, Luigi Maione, Leticia F G Silveira, Taneli Raivio, Ana Claudia Latronico, Jacques Young, Richard Quinton, Marco Bonomi, Luca Persani, Stephanie B Seminara, and Christopher S Lee. Classes and predictors of reversal in male patients with congenital hypogonadotropic hypogonadism: a cross-sectional study of six international referral centres. Apr 2024. URL: https://doi.org/10.1016/s2213-8587(24)00028-7, doi:10.1016/s2213-8587(24)00028-7. This article has 19 citations and is from a highest quality peer-reviewed journal.

4. (dwyer2024classesandpredictors pages 3-4): Andrew A Dwyer, Isabella R McDonald, Biagio Cangiano, Luca Giovanelli, Luigi Maione, Leticia F G Silveira, Taneli Raivio, Ana Claudia Latronico, Jacques Young, Richard Quinton, Marco Bonomi, Luca Persani, Stephanie B Seminara, and Christopher S Lee. Classes and predictors of reversal in male patients with congenital hypogonadotropic hypogonadism: a cross-sectional study of six international referral centres. Apr 2024. URL: https://doi.org/10.1016/s2213-8587(24)00028-7, doi:10.1016/s2213-8587(24)00028-7. This article has 19 citations and is from a highest quality peer-reviewed journal.

5. (sayed2023paneltestingfor pages 2-3): Yasmin Al Sayed and Sasha R. Howard. Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism – a clinical perspective. European Journal of Human Genetics, 31(4):387-394, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01261-0, doi:10.1038/s41431-022-01261-0. This article has 39 citations and is from a domain leading peer-reviewed journal.

6. (panel2024diagnosisandtreatment pages 34-35): G Panel and A Panel. Diagnosis and treatment of infertility in men: aua/asrm guideline (2020; amended 2024). Unknown journal, 2024.

7. (indirli2019ararespry4 pages 1-2): Rita Indirli, Biagio Cangiano, Eriselda Profka, Giovanna Mantovani, Luca Persani, Maura Arosio, Marco Bonomi, and Emanuele Ferrante. A rare spry4 gene mutation is associated with anosmia and adult-onset isolated hypogonadotropic hypogonadism. Frontiers in Endocrinology, Nov 2019. URL: https://doi.org/10.3389/fendo.2019.00781, doi:10.3389/fendo.2019.00781. This article has 15 citations.

8. (miraoui2013mutationsinfgf17 pages 12-14): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

9. (gach2020newfindingsin pages 4-4): Agnieszka Gach, Iwona Pinkier, Urszula Wysocka, Kinga Sałacińska, Dominik Salachna, Maria Szarras-Czapnik, Aleksandra Pietrzyk, Agata Sakowicz, Anna Nykel, Lena Rutkowska, Magda Rybak-Krzyszkowska, Magda Socha, Aleksander Jamsheer, and Lucjusz Jakubowski. New findings in oligogenic inheritance of congenital hypogonadotropic hypogonadism. Archives of Medical Science : AMS, 18:353-364, Sep 2020. URL: https://doi.org/10.5114/aoms.2020.98909, doi:10.5114/aoms.2020.98909. This article has 24 citations.

10. (stutz2021asprouty4mutation pages 1-2): Astrid Stütz, Anna Z. M. Kamptner, and Hedwig Sutterlüty. A sprouty4 mutation identified in kallmann syndrome increases the inhibitory potency of the protein towards fgf and connected processes. Feb 2021. URL: https://doi.org/10.3390/ijms22042145, doi:10.3390/ijms22042145. This article has 9 citations.

11. (stutz2021asprouty4mutation pages 4-7): Astrid Stütz, Anna Z. M. Kamptner, and Hedwig Sutterlüty. A sprouty4 mutation identified in kallmann syndrome increases the inhibitory potency of the protein towards fgf and connected processes. Feb 2021. URL: https://doi.org/10.3390/ijms22042145, doi:10.3390/ijms22042145. This article has 9 citations.

12. (stutz2021asprouty4mutation pages 9-10): Astrid Stütz, Anna Z. M. Kamptner, and Hedwig Sutterlüty. A sprouty4 mutation identified in kallmann syndrome increases the inhibitory potency of the protein towards fgf and connected processes. Feb 2021. URL: https://doi.org/10.3390/ijms22042145, doi:10.3390/ijms22042145. This article has 9 citations.

13. (gach2020newfindingsin pages 2-4): Agnieszka Gach, Iwona Pinkier, Urszula Wysocka, Kinga Sałacińska, Dominik Salachna, Maria Szarras-Czapnik, Aleksandra Pietrzyk, Agata Sakowicz, Anna Nykel, Lena Rutkowska, Magda Rybak-Krzyszkowska, Magda Socha, Aleksander Jamsheer, and Lucjusz Jakubowski. New findings in oligogenic inheritance of congenital hypogonadotropic hypogonadism. Archives of Medical Science : AMS, 18:353-364, Sep 2020. URL: https://doi.org/10.5114/aoms.2020.98909, doi:10.5114/aoms.2020.98909. This article has 24 citations.

14. (gach2020newfindingsin pages 5-5): Agnieszka Gach, Iwona Pinkier, Urszula Wysocka, Kinga Sałacińska, Dominik Salachna, Maria Szarras-Czapnik, Aleksandra Pietrzyk, Agata Sakowicz, Anna Nykel, Lena Rutkowska, Magda Rybak-Krzyszkowska, Magda Socha, Aleksander Jamsheer, and Lucjusz Jakubowski. New findings in oligogenic inheritance of congenital hypogonadotropic hypogonadism. Archives of Medical Science : AMS, 18:353-364, Sep 2020. URL: https://doi.org/10.5114/aoms.2020.98909, doi:10.5114/aoms.2020.98909. This article has 24 citations.

15. (indirli2019ararespry4 pages 2-4): Rita Indirli, Biagio Cangiano, Eriselda Profka, Giovanna Mantovani, Luca Persani, Maura Arosio, Marco Bonomi, and Emanuele Ferrante. A rare spry4 gene mutation is associated with anosmia and adult-onset isolated hypogonadotropic hypogonadism. Frontiers in Endocrinology, Nov 2019. URL: https://doi.org/10.3389/fendo.2019.00781, doi:10.3389/fendo.2019.00781. This article has 15 citations.

16. (miraoui2013mutationsinfgf17 pages 3-4): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 352 citations and is from a highest quality peer-reviewed journal.

17. (indirli2019ararespry4 pages 5-6): Rita Indirli, Biagio Cangiano, Eriselda Profka, Giovanna Mantovani, Luca Persani, Maura Arosio, Marco Bonomi, and Emanuele Ferrante. A rare spry4 gene mutation is associated with anosmia and adult-onset isolated hypogonadotropic hypogonadism. Frontiers in Endocrinology, Nov 2019. URL: https://doi.org/10.3389/fendo.2019.00781, doi:10.3389/fendo.2019.00781. This article has 15 citations.

18. (OpenTargets Search: hypogonadotropic hypogonadism 17 with or without anosmia-SPRY4): Open Targets Query (hypogonadotropic hypogonadism 17 with or without anosmia-SPRY4, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

19. (vezzoli2023geneticarchitectureof pages 2-3): Valeria Vezzoli, Faris Hrvat, Giovanni Goggi, Silvia Federici, Biagio Cangiano, Richard Quinton, Luca Persani, and Marco Bonomi. Genetic architecture of self-limited delayed puberty and congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Jan 2023. URL: https://doi.org/10.3389/fendo.2022.1069741, doi:10.3389/fendo.2022.1069741. This article has 27 citations.

20. (cho2019nasalplacodedevelopment pages 19-20): Hyun-Ju Cho, Yufei Shan, Niteace C. Whittington, and Susan Wray. Nasal placode development, gnrh neuronal migration and kallmann syndrome. Frontiers in Cell and Developmental Biology, Jul 2019. URL: https://doi.org/10.3389/fcell.2019.00121, doi:10.3389/fcell.2019.00121. This article has 96 citations.

## Artifacts

- [Edison artifact artifact-00](SPRY4_Hypogonadotropic_Hypogonadism-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 2 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 10 |
| On topic | 3 |
| Off topic | 0 |

10 of 12 references resolved; the rest could not be looked up either way.