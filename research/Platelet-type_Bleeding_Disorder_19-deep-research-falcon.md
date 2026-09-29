---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T14:40:08.433590'
end_time: '2026-09-03T14:52:48.478201'
duration_seconds: 760.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Platelet-type bleeding disorder 19 (BDPLT19; PRKACG-related severe
    autosomal recessive macrothrombocytopenia; OMIM 616176)
  mondo_id: MONDO:0014518
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
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Platelet-type_Bleeding_Disorder_19-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Platelet-type bleeding disorder 19 (BDPLT19; PRKACG-related severe autosomal recessive macrothrombocytopenia; OMIM 616176)
- **MONDO ID:** MONDO:0014518 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Platelet-type bleeding disorder 19 (BDPLT19; PRKACG-related severe autosomal recessive macrothrombocytopenia; OMIM 616176)** covering all of the
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
- **Disease Name:** Platelet-type bleeding disorder 19 (BDPLT19; PRKACG-related severe autosomal recessive macrothrombocytopenia; OMIM 616176)
- **MONDO ID:** MONDO:0014518 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Platelet-type bleeding disorder 19 (BDPLT19; PRKACG-related severe autosomal recessive macrothrombocytopenia; OMIM 616176)** covering all of the
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


# Platelet-type bleeding disorder 19 (BDPLT19)

## Executive summary and evidence boundary

Platelet-type bleeding disorder 19 is an ultra-rare, nonsyndromic inherited macrothrombocytopenia caused by biallelic **PRKACG** dysfunction. The established phenotype combines profoundly reduced platelet number, giant platelets, impaired platelet activation, and mucocutaneous or gynecologic bleeding. The disease–gene assertion rests principally on one consanguineous West Indian family reported by Manchev *et al.* in *Blood* in 2014: two homozygous siblings, two clinically unaffected heterozygous relatives, and functional rescue of patient-derived megakaryocytes with wild-type PRKACG. Open Targets likewise maps MONDO:0014518 only to PRKACG and cites PMID **25061177**. Thus, numerical phenotype frequencies below describe the reported family, not population-level estimates. (OpenTargets Search: platelet-type bleeding disorder 19-PRKACG, manchev2014anewform pages 1-2, manchev2014anewform pages 4-6, manchev2014anewform pages 8-9)

**Primary reference:** Manchev VT *et al.* “A new form of macrothrombocytopenia induced by a germ-line mutation in the PRKACG gene.” *Blood*. Published online **24 July 2014**; print **16 October 2014**;124(16):2554–2563. PMID: **25061177**. DOI/URL: https://doi.org/10.1182/blood-2014-01-551820. (manchev2014anewform pages 1-2, manchev2014anewform pages 10-11)

The central evidence is summarized here:

| Domain | Established finding | Quantitative/detail | Evidence type | Certainty/limitation |
|---|---|---|---|---|
| Identifiers | Platelet-type bleeding disorder 19 (BDPLT19) is PRKACG-related severe autosomal-recessive macrothrombocytopenia. | OMIM 616176; MONDO:0014518; associated gene **PRKACG**. (OpenTargets Search: platelet-type bleeding disorder 19-PRKACG, manchev2014anewform pages 1-2) | Aggregated disease resource plus primary human report | Disease–gene association is based principally on one family reported in 2014. |
| Human cases | Two affected West Indian siblings were described in a consanguineous family. | Proband II-1 was diagnosed at age 4; brother II-2 at age 2. Both lacked reported syndromic features. (manchev2014anewform pages 3-4, manchev2014anewform pages 4-6) | Human clinical—single pedigree | Extremely small evidence base; phenotype frequencies cannot be generalized beyond 2/2 reported affected individuals. |
| Genetic cause and inheritance | Homozygous germline **PRKACG c.222C>G**, causing **p.Ile74Met** in the PKA catalytic γ subunit, cosegregated with disease under an autosomal-recessive model. | Both affected siblings were homozygous; mother I-1 and relative III-1 were unaffected heterozygotes; II-3 was homozygous wild type. The variant was absent from databases queried in 2014, affected a conserved residue, and was predicted damaging by PolyPhen-2. (manchev2014anewform pages 4-6, manchev2014anewform pages 6-8) | Human genetic segregation plus computational prediction | Strong segregation and functional support within one pedigree, but no independent-family replication or current population-frequency estimate was identified. |
| Thrombocytopenia | Affected siblings had severe, persistent thrombocytopenia. | Platelet counts were **5 × 10⁹/L** in II-1 and **8 × 10⁹/L** in II-2. (manchev2014anewform pages 3-4, manchev2014anewform pages 4-6) | Human laboratory | Direct measurements in two patients; automated MPV was unavailable for either affected sibling. |
| Platelet size | Macrothrombocytopenia with predominantly giant or macrocytic platelets was demonstrated by smear and electron microscopy. | Approximately **90%** of platelets were giant or macrocytic; mean diameters were **4.86 μm** and **4.98 μm**, versus **2.84 μm** in an external control and **2.97 μm** in a heterozygous relative. (manchev2014anewform pages 4-6) | Human cytology and ultrastructure | Demonstrated in both affected siblings, but no independent cohort exists. |
| Bleeding phenotype | Bleeding was mucocutaneous and gynecologic, ranging from moderate to life-threatening. | II-1 had epistaxis, spontaneous hematomas, menorrhagia with anemia, and three hemorrhagic ovarian-cyst ruptures requiring platelet and red-cell transfusion; WHO bleeding score **4**. II-2 had lifelong epistaxis and cutaneous hematomas; narrative WHO score **3**. (manchev2014anewform pages 4-6, manchev2014anewform pages 8-9) | Human clinical | Disease-specific treatment experience is limited to transfusion support; the table and narrative differ for II-2’s score. |
| Platelet dysfunction | Patient platelets showed defective agonist-induced activation, secretion, calcium signaling, receptor trafficking, and VWF-associated actin polymerization. | After stimulation, GPIb internalization was **18%** of resting level versus **44.2%** in control; control αIIbβ3 surface expression rose to **193%**, whereas patient platelets showed no increase; P-selectin externalization was absent; the VWF-associated F-actin/G-actin ratio was **44% of control**. (manchev2014anewform pages 4-6, manchev2014anewform pages 9-10) | Ex vivo human platelet assays | Directly demonstrated with patient samples; reproducibility across unrelated cases is unknown. |
| Megakaryocytes and marrow | Bone marrow contained megakaryocyte clusters, while cultured megakaryocyte differentiation and ploidization were preserved; the principal production defect occurred during proplatelet formation. | Mature CD41⁺CD42⁺ cell proportions and ploidy were comparable with controls, but homozygous patient megakaryocytes had a **2.5-fold lower** proportion of proplatelet-bearing cells. (manchev2014anewform pages 4-6, manchev2014anewform pages 6-8) | Human marrow morphology and patient-derived CD34⁺ culture | Supports a late thrombopoiesis defect rather than impaired megakaryocyte differentiation; based on one family. |
| PKA–FLNA mechanism | Mutant PRKACG protein was not degraded, but PKA dysfunction was associated with markedly reduced filamin A and elevated platelet cAMP. Loss of PKA-mediated FLNA Ser2152 phosphorylation and consequent proteolysis was proposed. | FLNA was almost absent from mature patient megakaryocytes and platelets; platelet cAMP was **3- to 5-fold higher** than in controls or a heterozygous relative. GPIbβ Ser166 phosphorylation was normal. (manchev2014anewform pages 6-8, manchev2014anewform pages 8-9) | Human biochemical assays plus mechanistic inference | FLNA loss and cAMP elevation were demonstrated; defective FLNA Ser2152 phosphorylation and proteolytic causality were inferred rather than directly measured. |
| Functional rescue | Wild-type PRKACG rescued abnormal proplatelet formation in patient-derived megakaryocytes; mutant PRKACG did not. | Wild-type lentiviral expression significantly increased proplatelet formation and reduced platelet-like structure diameter from **3.67 to 1.68 μm** in II-1 and **4.17 to 2.01 μm** in II-2. (manchev2014anewform pages 8-9) | In vitro patient-cell rescue | Strong disease-gene functional evidence, but not a clinical gene-therapy result or evidence of in vivo safety or efficacy. |
| Diagnosis | Diagnosis requires recognition of congenital giant-platelet thrombocytopenia with platelet dysfunction, exclusion of phenocopies, and molecular confirmation. | The original study excluded **GP1BA/GP1BB/GP9** defects and neutrophil inclusions suggestive of MYH9-related disease, then used exome sequencing and Sanger segregation. General IPD evaluation includes bleeding and family history, CBC and smear, platelet-function testing, flow cytometry or electron microscopy, and panel, WES, or WGS testing. (manchev2014anewform pages 6-8, palmabarqueros2021inheritedplateletdisorders pages 11-13, palmabarqueros2021inheritedplateletdisorders pages 15-17) | Disease-specific workup plus expert-review guidance | No validated BDPLT19-specific diagnostic criteria, biomarker, or standalone functional assay exists. |
| Management | No PRKACG-specific standard therapy or response-rate evidence exists. Supportive inherited-platelet-disorder care is the current practical framework. | General expert guidance favors local hemostasis, trauma and antiplatelet-drug avoidance, antifibrinolytics or desmopressin for selected bleeding or procedures, and platelet transfusion for major bleeding or critical sites, while minimizing exposure and using HLA-compatible products when needed. (noris2017hereditarythrombocytopeniasa pages 12-13, palmabarqueros2021inheritedplateletdisorders pages 21-22) | Expert review extrapolated from other inherited platelet disorders | Not validated specifically in BDPLT19; no disease-specific evidence supports thrombopoietin-receptor agonists, HSCT, splenectomy, rFVIIa, pharmacogenomics, or targeted therapy. |
| Epidemiology | BDPLT19 is ultra-rare, with no population prevalence, incidence, carrier-frequency, sex-ratio, or mortality estimate. | The established literature identified **2 affected siblings in 1 pedigree**; reviews historically described only one PRKACG variant from a single pedigree. (johnson2017moleculargeneticinvestigation pages 51-55, johnson2017moleculargeneticinvestigationa pages 51-55) | Literature ascertainment | Two published cases are not a prevalence estimate; underdiagnosis is plausible but unquantified. |
| 2023–2024 update | No disease-specific 2023–2024 cohort, independently confirmed family or pathogenic variant, natural-history study, animal model, omics or single-cell study, clinical trial, or targeted treatment was identified. | Recent literature primarily provides general inherited platelet-disorder diagnostic context rather than new BDPLT19 evidence. (palmabarqueros2021inheritedplateletdisorders pages 1-3, donck2021hemostaticphenotypesand pages 6-7) | Evidence-gap assessment | Absence from retrieved literature does not prove that unpublished cases or database submissions do not exist; the 2014 report remains the principal direct evidence. |


*Table: Concise summary of the established clinical, genetic, mechanistic, diagnostic, and management evidence for PRKACG-related BDPLT19. The table emphasizes that direct evidence remains limited to one family and identifies major recent-research gaps.*

## 1. Disease information

### Definition

BDPLT19 is a congenital platelet-production and platelet-function disorder. Its defining abnormalities are severe thrombocytopenia, predominantly giant or macrocytic platelets, defective megakaryocyte proplatelet formation, and thrombocytopathy. It was described as autosomal recessive and without syndromic manifestations in the two established patients. The authors’ abstract states directly: **“PRKACG is a new central actor in platelet biogenesis and a new gene involved in inherited thrombocytopenia with giant platelets associated with a thrombocytopathy.”** (manchev2014anewform pages 1-2)

### Identifiers and terminology

- **OMIM phenotype:** 616176.
- **MONDO:** MONDO:0014518.
- **Causal gene:** **PRKACG**, protein kinase cAMP-activated catalytic subunit gamma; Ensembl ENSG00000165059. (OpenTargets Search: platelet-type bleeding disorder 19-PRKACG)
- **Synonyms:** platelet-type bleeding disorder 19; bleeding disorder, platelet-type, 19; BDPLT19; PRKACG-related thrombocytopenia; PRKACG-related disease; PRKACG-related severe autosomal-recessive macrothrombocytopenia.
- **Orphanet:** no disorder-specific Orphanet identifier was established in the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no uniquely specific code/descriptor was identified; coding ordinarily falls under inherited/other thrombocytopenia or platelet-function-defect categories. Such broader codes should not be represented as exact synonyms.

This report combines an **aggregated disease-level resource**—MONDO/Open Targets—with **patient-level primary research** from one pedigree. It is not derived from EHR aggregation or a disease registry. (OpenTargets Search: platelet-type bleeding disorder 19-PRKACG, manchev2014anewform pages 3-4)

## 2. Etiology, risk, protection, and environment

### Causal factor

The established initiating lesion is a germline homozygous **PRKACG c.222C>G, p.Ile74Met** missense variant, reported on transcript NM_002732. PRKACG encodes the catalytic γ isoform of cAMP-dependent protein kinase A (PKA). The variant cosegregated with macrothrombocytopenia under an autosomal-recessive model. (manchev2014anewform pages 1-2, manchev2014anewform pages 4-6, manchev2014anewform pages 6-8)

The same homozygous siblings also carried **GNE c.1675G>A, p.Gly559Arg**. The investigators deprioritized GNE because neither patient had myopathy or sialuria, thrombocytopenia had not then been associated with GNE myopathy, and wild-type PRKACG specifically rescued the cellular phenotype. The strongest interpretation is therefore PRKACG causality, while acknowledging that evidence derives from one family and that the original genotype included this second rare homozygous variant. (manchev2014anewform pages 6-8, manchev2014anewform pages 8-9)

### Risk factors

- **Established genetic risk:** biallelic p.Ile74Met; consanguinity increased the probability of homozygosity in the reported pedigree.
- **Family history:** an affected sibling is highly informative. For two carrier parents, standard autosomal-recessive counseling predicts a 25% affected, 50% carrier, and 25% unaffected/noncarrier probability per pregnancy, assuming the disease model is correct.
- **Environmental, infectious, occupational, lifestyle, age, and sex risks:** none are known to cause BDPLT19. Trauma, surgery, menstruation, childbirth, and platelet-inhibiting drugs are best regarded as **bleeding modifiers/triggers**, not causes. General IPD reviews report that trauma, medications, surgery, and childbirth may aggravate bleeding. (palmabarqueros2021inheritedplateletdisorders pages 11-13)

### Protective factors and gene–environment interaction

No protective allele, modifier gene, diet, exposure, or validated gene–environment interaction has been reported. Practical protection consists of avoiding platelet-inhibiting medication and high-trauma activities and planning hemostatic support for procedures; this lowers bleeding exposure rather than preventing the genotype. (palmabarqueros2021inheritedplateletdisorders pages 21-22)

## 3. Phenotypes

| Phenotype | Type and suggested HPO annotation | Reported characteristics |
|---|---|---|
| Severe thrombocytopenia | Laboratory abnormality; **HP:0001873 Thrombocytopenia** | Diagnosed at ages 4 and 2 years; platelet counts 5 and 8 ×10⁹/L. Congenital/pediatric, chronic, severe; 2/2 established patients. (manchev2014anewform pages 3-4, manchev2014anewform pages 4-6) |
| Giant/macrocytic platelets | Smear/ultrastructural sign; **HP:0001902 Giant platelets**, macrothrombocytopenia | About 90% giant or macrocytic; mean diameters 4.86 and 4.98 μm versus 2.84 and 2.97 μm in control/heterozygous-relative samples; 2/2. (manchev2014anewform pages 4-6) |
| Epistaxis | Symptom; **HP:0000421 Epistaxis** | Infantile/recurrent in both siblings; lifelong in the brother; 2/2. (manchev2014anewform pages 4-6) |
| Easy bruising/spontaneous hematomas | Symptom/sign; **HP:0000978 Bruising susceptibility** | Spontaneous or cutaneous hematomas in both; 2/2. (manchev2014anewform pages 4-6) |
| Menorrhagia | Symptom; **HP:0000132 Menorrhagia** | Present in the female proband, causing anemia; 1/1 reported affected female. (manchev2014anewform pages 4-6) |
| Hemorrhagic ovarian-cyst rupture | Acute complication; ovarian hemorrhage term if locally available | Three consecutive ruptures in the proband were life-threatening and required platelet and red-cell transfusion. (manchev2014anewform pages 4-6) |
| Anemia | Laboratory abnormality; **HP:0001903 Anemia** | Proband hemoglobin 9 g/dL, associated with menorrhagia/bleeding. (manchev2014anewform pages 3-4, manchev2014anewform pages 4-6) |
| Platelet-function defect | Functional laboratory phenotype; platelet aggregation/secretion defect terms | Absent activation-induced P-selectin exposure and αIIbβ3 upregulation, poor GPIb internalization, reduced calcium mobilization, and deficient VWF-associated actin polymerization. (manchev2014anewform pages 4-6) |
| Megakaryocyte clustering | Marrow pathology | Present in patient marrow; cultured megakaryocyte maturation and ploidy were normal. (manchev2014anewform pages 4-6) |

Bleeding severity was substantial: the narrative reports WHO scores **4** and **3**, although Table 1 appears to list 3 and 2, an internal discrepancy that should be retained in curation rather than silently resolved. The female proband experienced life-threatening hemorrhage; her brother had moderate lifelong bleeding. (manchev2014anewform pages 3-4, manchev2014anewform pages 4-6, manchev2014anewform pages 8-9)

No validated EQ-5D, SF-36, PROMIS, disability, or disease-specific quality-of-life data exist. Likely burdens include recurrent bleeding, anemia, transfusion exposure, restrictions on trauma-prone activities, and intensive perioperative/gynecologic planning, but these impacts were not formally measured.

## 4. Genetic and molecular information

### Gene and variant

- **Gene:** PRKACG; protein kinase cAMP-activated catalytic subunit gamma; chromosome 9; Ensembl ENSG00000165059. (OpenTargets Search: platelet-type bleeding disorder 19-PRKACG)
- **Variant:** NM_002732:**c.222C>G**, **p.Ile74Met** (older article notation p.74I.M).
- **Class/type:** germline homozygous missense.
- **Segregation:** II-1 and II-2 were homozygous affected; I-1 and III-1 were unaffected heterozygotes; II-3 was homozygous wild type. (manchev2014anewform pages 4-6, manchev2014anewform pages 6-8)
- **Original database evidence:** absent from dbSNP and the databases filtered by the investigators in 2014; the residue was evolutionarily conserved and PolyPhen-2 predicted a damaging effect. This is not a substitute for a current gnomAD frequency or contemporary ACMG/AMP classification. (manchev2014anewform pages 4-6, manchev2014anewform pages 6-8)
- **Current frequency/classification:** no verified current gnomAD/TOPMed frequency or ClinVar assertion was available from the retrieved material. A knowledge base should therefore avoid inventing “pathogenic” ClinVar status; a defensible narrative is **disease-causing in the original report, with strong segregation and PS3-like functional rescue evidence, but only one pedigree**.

The mutant protein was present rather than degraded. Functional consequences were consistent with reduced PKA activity: platelet cAMP was three- to fivefold elevated, FLNA was almost absent from mature megakaryocytes and platelets, and wild-type—but not mutant—PRKACG corrected proplatelet formation. (manchev2014anewform pages 6-8, manchev2014anewform pages 8-9)

No established modifier gene, pathogenic structural/chromosomal rearrangement, somatic lesion, repeat expansion, mitochondrial variant, or disease-specific epigenetic alteration is known. No independent BDPLT19 families or firmly established additional pathogenic PRKACG alleles were identified in the retrieved literature; an older review explicitly described only one variant in one pedigree. (johnson2017moleculargeneticinvestigation pages 51-55, johnson2017moleculargeneticinvestigationa pages 51-55)

## 5. Environmental information

No toxin, radiation, pollutant, dietary factor, smoking/alcohol exposure, occupational agent, or infectious organism is implicated in disease initiation. Aspirin, NSAIDs, other antiplatelet drugs, trauma, invasive procedures, and heavy menstrual bleeding may increase hemorrhagic risk in a person who already has the inherited defect. Vaccination and ordinary infection are not established causes of this genotype-defined condition.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. Homozygous **PRKACG p.Ile74Met** **leads to** impaired catalytic γ-subunit contribution to platelet/megakaryocyte PKA activity. This is supported by biochemical and rescue assays, although direct catalytic kinetics were not reported. (manchev2014anewform pages 6-8, manchev2014anewform pages 8-9)
2. Impaired PKA feedback **results in** three- to fivefold accumulation of platelet cAMP, plausibly through reduced phosphodiesterase activation and/or reduced inhibition of adenylyl cyclase. The cAMP increase was demonstrated; the precise feedback route is inferred. (manchev2014anewform pages 6-8)
3. Impaired PKA activity is proposed to **reduce** FLNA Ser2152 phosphorylation, which **leads to** loss of protection from proteolysis and near-absence of FLNA in mature megakaryocytes and platelets. FLNA loss was demonstrated; reduced Ser2152 phosphorylation and causal proteolysis were inferred rather than directly measured. (manchev2014anewform pages 6-8, manchev2014anewform pages 8-9)
4. FLNA deficiency **leads to** defective actin-network stabilization and cytoplasmic fragmentation, which **results in** a 2.5-fold reduction in proplatelet-bearing megakaryocytes and oversized platelet-like structures. (manchev2014anewform pages 6-8, manchev2014anewform pages 8-9)
5. Defective proplatelet formation **results in** very low circulating platelet counts and giant platelets. Wild-type lentiviral PRKACG restored proplatelet production and reduced platelet-like structure diameter, providing direct functional support. (manchev2014anewform pages 8-9)
6. **Branch A:** increased cAMP, a negative regulator of platelet responses, is hypothesized to **lead to** impaired activation, secretion, and calcium signaling. **Branch B:** FLNA/actin disorganization is hypothesized to **lead to** defective receptor trafficking and calcium translocation. The relative contributions remain unresolved. (manchev2014anewform pages 9-10)
7. Low platelet number plus qualitative dysfunction **results in** epistaxis, bruising, menorrhagia, anemia, and potentially life-threatening ovarian hemorrhage. (manchev2014anewform pages 4-6)

### Detailed biology and quantitative findings

PKA contains regulatory and catalytic subunits; PRKACG encodes catalytic γ. Candidate platelet PKA substrates include signaling regulators and actin-binding proteins such as FLNA. GPIbβ Ser166 phosphorylation was normal in patient megakaryocytes and platelets, arguing against this substrate as the proximate defect. In contrast, FLNA was almost absent. Patient platelets had an F-actin/G-actin ratio on VWF of 44% of control, but a comparable ratio on fibrinogen, suggesting matrix/pathway-dependent cytoskeletal dysfunction. (manchev2014anewform pages 6-8, manchev2014anewform pages 8-9)

Activation assays showed GPIb internalization to 18% of resting expression versus 44.2% in controls. Control αIIbβ3 surface expression rose to 193% after stimulation, whereas patient platelets showed no increase; P-selectin externalization was absent, and calcium release/influx was markedly diminished. (manchev2014anewform pages 4-6)

**Rescue evidence:** wild-type PRKACG increased patient-megakaryocyte proplatelet formation; mutant PRKACG did not. Platelet-like structure diameter fell from 3.67 to 1.68 μm in II-1 and from 4.17 to 2.01 μm in II-2. This is a patient-derived cellular rescue experiment, not clinical gene therapy. (manchev2014anewform pages 8-9)

Suggested annotations include **GO: cAMP-dependent protein kinase activity; protein phosphorylation; regulation of actin-cytoskeleton organization; megakaryocyte differentiation; platelet formation; proplatelet formation; platelet activation; calcium-mediated signaling; granule secretion**. Relevant cell types are **megakaryocyte (CL:0000556)**, **platelet (CL:0000233)**, and hematopoietic stem/progenitor cells. Relevant cellular components include cytoplasm/cytosol, actin cytoskeleton, plasma membrane, and proplatelet extensions.

No BDPLT19-specific transcriptomic, proteomic beyond targeted immunoblotting, metabolomic, lipidomic, epigenomic, single-cell, spatial, CRISPR-screen, or multi-omics dataset was identified. The only advanced functional platform was ex vivo CD34-positive patient-cell differentiation and lentiviral complementation.

## 7. Anatomical structures affected

The primary system is hematologic/hemostatic. Principal sites are circulating blood and bone marrow megakaryocytes; secondary injury occurs at bleeding sites, notably skin, nasal mucosa, uterine/endometrial tract, and ovary in the reported proband. There is no evidence of intrinsic brain, renal, hepatic, pulmonary, cardiac, skeletal, neurologic, or immune-organ disease. (manchev2014anewform pages 4-6)

Suggested ontology mappings are **blood—UBERON:0000178**, **bone marrow—UBERON:0002371**, platelet (CL:0000233), and megakaryocyte (CL:0000556). Subcellular annotations include actin cytoskeleton, cytosol, plasma membrane, platelet α-granule/P-selectin trafficking machinery, and GPIb–IX–V/αIIbβ3 receptor-associated membrane cytoskeleton. Lateralization is not applicable.

## 8. Temporal development

The disorder is genetically present from conception and manifested in early childhood: diagnosis at ages 4 and 2 years. The brother’s bleeding was described as lifelong. Available evidence supports a chronic, persistent rather than progressive thrombocytopenia, with episodic hemorrhage triggered by ordinary mucosal injury, menstruation, or ovarian-cyst rupture. No formal disease stages, remission pattern, spontaneous recovery, or age-dependent penetrance curve exists. (manchev2014anewform pages 3-4, manchev2014anewform pages 4-6)

Critical periods are inferred clinically: infancy/childhood recognition, menarche and reproductive years, pregnancy/childbirth, invasive procedures, dental work, trauma, and acute major bleeding. These are intervention windows for anticipatory hemostatic planning, not demonstrated windows of molecular reversibility.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. The two homozygous siblings were affected and heterozygous relatives had normal platelet counts and morphology, supporting recessive segregation and no evident heterozygous phenotype in this family. Because only two affected people are known, penetrance appears complete for homozygous p.Ile74Met within this pedigree but cannot be reliably estimated across populations. Expressivity varied: one sibling had life-threatening gynecologic bleeding and the other moderate lifelong mucocutaneous bleeding. (manchev2014anewform pages 4-6, manchev2014anewform pages 6-8)

No anticipation, germline mosaicism, founder effect, or geographic variant distribution is established. Consanguinity was important in the discovery family. Both sexes were affected, providing no evidence of sex-linked risk, although sex-specific exposures such as menstruation can amplify morbidity.

There are no valid prevalence, incidence, carrier-frequency, mortality, sex-ratio, or age-distribution estimates. The observable literature count—two affected siblings in one West Indian pedigree—is **not** a prevalence estimate. Older reviews continued to describe a single variant/pedigree, and no independent 2023–2024 family was identified. (johnson2017moleculargeneticinvestigation pages 51-55, johnson2017moleculargeneticinvestigationa pages 51-55)

## 10. Diagnostics

### Recommended workflow

1. **Clinical assessment:** congenital/persistent thrombocytopenia; personal and three-generation bleeding history; consanguinity; medication review; examination for syndromic features. ISTH-BAT can standardize bleeding documentation, although it does not reliably distinguish every inherited thrombocytopenia from controls. (palmabarqueros2021inheritedplateletdisorders pages 11-13, palmabarqueros2021inheritedplateletdisorders pages 15-17)
2. **CBC and expert smear:** confirm severe thrombocytopenia and giant platelets. Automated counters can underestimate platelet number and MPV when platelets are very large; manual/optical methods are valuable.
3. **Exclude acquired causes:** immune thrombocytopenia, drug-induced disease, infection, marrow failure, liver disease/hypersplenism, and pseudothrombocytopenia.
4. **Platelet phenotyping:** flow cytometry for GPIb–IX–V and αIIbβ3; agonist-induced P-selectin and receptor trafficking; aggregometry/secretion studies; calcium mobilization where available; electron microscopy for size/ultrastructure. Light-transmission aggregometry remains a general reference test, while flow cytometry and electron microscopy help define receptor and structural defects. (palmabarqueros2021inheritedplateletdisorders pages 15-17)
5. **Genetics:** an inherited thrombocytopenia/platelet-disorder panel that includes **PRKACG**, followed by exome or genome sequencing if negative. Confirm candidate variants with orthogonal sequencing and parental/family segregation. HTS interpretation must be integrated with platelet phenotype and ACMG/AMP evidence. (palmabarqueros2021inheritedplateletdisorders pages 17-18, palmabarqueros2021inheritedplateletdisorders pages 11-13)

The original investigation excluded GP1BA/GP1BB/GP9-associated Bernard–Soulier syndrome and found no neutrophil inclusions suggestive of MYH9-related disease before exome sequencing. (manchev2014anewform pages 6-8)

### Differential diagnosis

Major differentials include Bernard–Soulier syndrome; MYH9-related disease; FLNA-, ACTN1-, TUBB1-, DIAPH1-, SRC-, GNE-, and SLC35A1-related macrothrombocytopenias; gray platelet syndrome; platelet-type von Willebrand disease; immune thrombocytopenia; and EDTA-dependent pseudothrombocytopenia. Distinguishing clues include inheritance, syndromic findings, neutrophil inclusions, receptor expression, granule morphology, VWF studies, platelet size, and molecular testing. Misdiagnosis as immune thrombocytopenia can cause ineffective or harmful immunosuppression/splenectomy. (palmabarqueros2021inheritedplateletdisorders pages 11-13, palmabarqueros2021inheritedplateletdisorders pages 15-17)

No validated BDPLT19-specific diagnostic criteria, biochemical assay, imaging signature, RNA/proteomic diagnostic, newborn screen, or liquid biopsy exists. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not first-line unless another phenotype suggests them. Cascade testing is appropriate after a familial pathogenic genotype is established; prenatal and preimplantation testing are technically possible for the known family variant with counseling.

## 11. Outcome and prognosis

No survival curve, life-expectancy estimate, disease-specific mortality rate, or prospective natural-history study exists. Both reported patients survived into their twenties at publication, but the proband had three life-threatening ovarian hemorrhages. Morbidity arises from bleeding, anemia, transfusion requirements, and procedure/reproductive risk. (manchev2014anewform pages 3-4, manchev2014anewform pages 4-6)

The disorder appears lifelong; spontaneous normalization was not reported. Prognosis probably depends on residual platelet count/function, prior major bleeding, menstrual/gynecologic burden, trauma and surgery exposure, and access to specialist hemostatic care, but no prognostic model or biomarker has been validated. There is no evidence of marrow-failure evolution, malignancy predisposition, immunodeficiency, renal disease, or neurodevelopmental involvement in BDPLT19.

## 12. Treatment and current applications

There is no approved PRKACG-targeted treatment, no disease-specific algorithm, no response-rate study, and no registered relevant interventional trial identified. Management should therefore be individualized by an inherited-bleeding-disorder center and explicitly labeled as extrapolated from broader IPD practice.

### Practical strategy

- **Education/prevention:** bleeding plan, medical-alert identification, dental hygiene, avoidance of aspirin/NSAIDs and unnecessary antiplatelet therapy, trauma precautions, and specialist planning for procedures. (palmabarqueros2021inheritedplateletdisorders pages 21-22)
- **Local hemostasis:** compression, topical measures, nasal/dental control; preferred where feasible. (noris2017hereditarythrombocytopeniasa pages 12-13)
- **Antifibrinolytics:** tranexamic acid or aminocaproic acid may be considered for mucosal, dental, or menstrual bleeding and selected procedures. Suggested NCIt concept: **Antifibrinolytic Agent**. Evidence is general IPD expert practice, not BDPLT19-specific. (noris2017hereditarythrombocytopeniasa pages 12-13)
- **Desmopressin:** sometimes used for selected IPDs/low-risk procedures, but efficacy in BDPLT19 is unknown and should be established cautiously. Suggested NCIt: **Desmopressin**. (noris2017hereditarythrombocytopeniasa pages 12-13)
- **Platelet transfusion:** appropriate for major/life-threatening bleeding or critical-site hemorrhage and major procedures. The proband received platelet and red-cell transfusions for ovarian hemorrhage. Minimize exposure because alloimmunization can cause refractoriness; use leukoreduced, single-donor and HLA-compatible products when feasible. Suggested NCIt: **Platelet Transfusion**. (manchev2014anewform pages 4-6, noris2017hereditarythrombocytopeniasa pages 12-13, palmabarqueros2021inheritedplateletdisorders pages 21-22)
- **Red-cell transfusion/iron replacement:** as clinically required for hemorrhagic or iron-deficiency anemia; direct BDPLT19 evidence exists for red-cell support during severe bleeding, not for comparative efficacy. (manchev2014anewform pages 4-6)
- **Menstrual/gynecologic management:** coordinated hematology–gynecology care, antifibrinolytic and hormonal approaches as appropriate, iron monitoring, and urgent evaluation of pelvic pain because ovarian-cyst rupture was the defining life-threatening complication.

There is no disease-specific evidence supporting thrombopoietin-receptor agonists, recombinant factor VIIa, splenectomy, HSCT, immunotherapy, RNA therapy, or pharmacogenomic selection. These should not be imported from other thrombocytopenias without a case-specific rationale. Lentiviral wild-type PRKACG rescue is a mechanistic proof of principle only; it does not establish clinical gene-therapy feasibility or safety. (manchev2014anewform pages 8-9, noris2017hereditarythrombocytopeniasa pages 12-13)

## 13. Prevention

Primary prevention of the genotype is not possible through lifestyle or vaccination. Reproductive options include carrier/cascade testing, genetic counseling, prenatal diagnosis, and preimplantation genetic testing once the familial variant and phase are confirmed.

Secondary prevention consists of early recognition of congenital macrothrombocytopenia, avoiding misdiagnosis as immune thrombocytopenia, and testing relatives. Population or newborn screening is not supported.

Tertiary prevention includes avoidance of platelet inhibitors and trauma, dental hygiene, iron surveillance, menstrual management, procedure/childbirth plans, rapid treatment of bleeding, and judicious use of compatible platelets. No immunization specifically prevents BDPLT19; routine vaccines remain appropriate unless individualized clinical circumstances dictate otherwise. (palmabarqueros2021inheritedplateletdisorders pages 11-13, palmabarqueros2021inheritedplateletdisorders pages 21-22)

## 14. Other species and natural disease

No naturally occurring PRKACG-associated macrothrombocytopenia was identified in companion animals, livestock, or wildlife. There is no zoonotic or cross-species transmission because BDPLT19 is a germline human Mendelian condition. PRKACG orthologs are evolutionarily conserved, but the retrieved literature did not provide validated species-specific NCBI Gene IDs or a veterinary OMIA/VBO disease entry. These should be populated only after direct database verification.

## 15. Model organisms and experimental models

No dedicated **Prkacg p.Ile74Met** knock-in mouse, knockout model shown to recapitulate BDPLT19, zebrafish model, organoid, iPSC line, or natural animal model was identified. The principal model is a **patient-derived ex vivo cellular system**: peripheral-blood CD34-positive progenitors differentiated into megakaryocytes with thrombopoietin and stem-cell factor. It reproduced normal maturation/ploidy but reduced proplatelet formation, oversized platelet-like structures, and low FLNA. Lentiviral wild-type PRKACG rescued these abnormalities. (manchev2014anewform pages 2-3, manchev2014anewform pages 6-8, manchev2014anewform pages 8-9)

This model is valuable for late thrombopoiesis, cytoskeletal biology, variant-function studies, and candidate rescue experiments. Its limitations are the absence of marrow niche, circulation/shear, platelet clearance, immune interactions, whole-organism bleeding, long-term safety, and independent genotypes.

## Recent developments and expert interpretation, 2023–2024

The retrieved 2023–2024 literature did not reveal a new BDPLT19 family, independently replicated pathogenic variant, natural-history cohort, trial, or disease-specific therapy. The relevant advance is broader implementation of comprehensive platelet phenotyping and high-throughput genetic testing in inherited platelet disorders. A 2023 review emphasizes that these disorders can produce mucocutaneous bleeding and life-threatening trauma/surgical hemorrhage and that both platelet-function analysis and genetic testing are indispensable. General modern reviews similarly recommend integrating genotype with count, size, morphology, and functional phenotype rather than treating sequencing as a standalone diagnosis. (palmabarqueros2021inheritedplateletdisorders pages 11-13, palmabarqueros2021inheritedplateletdisorders pages 15-17, palmabarqueros2021inheritedplateletdisorders pages 1-3)

The authoritative interpretation is consequently cautious: BDPLT19 is biologically persuasive because cosegregation, patient-cell dysfunction, and allele-specific rescue align, but clinical generalizability remains weak because evidence is confined to one pedigree. Candidate PRKACG variants reported in heterogeneous platelet-secretion studies should not automatically be curated as BDPLT19 without recessive segregation and functional validation.

## Curation conclusions

- **Disease–gene validity:** supported by one pedigree plus strong patient-cell rescue; replication remains needed.
- **Core phenotype:** childhood-onset, lifelong severe macrothrombocytopenia with qualitative platelet dysfunction and variable moderate-to-life-threatening bleeding.
- **Core mechanism:** impaired PKA signaling → increased cAMP and probable failure of FLNA stabilization → defective actin organization/proplatelet formation → giant, scarce, dysfunctional platelets.
- **Best diagnostic application:** include PRKACG in inherited macrothrombocytopenia panels and interpret variants with segregation and functional platelet/megakaryocyte evidence.
- **Current implementation:** supportive bleeding prevention and hemostatic treatment; no targeted therapy or trial.
- **Highest-priority research gaps:** independent families and alleles, current population-frequency/ClinVar curation, catalytic and structural characterization, direct FLNA-Ser2152 measurements, knock-in animal/iPSC models, longitudinal outcomes, reproductive/pregnancy data, and treatment-response studies.

References

1. (OpenTargets Search: platelet-type bleeding disorder 19-PRKACG): Open Targets Query (platelet-type bleeding disorder 19-PRKACG, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (manchev2014anewform pages 1-2): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

3. (manchev2014anewform pages 4-6): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

4. (manchev2014anewform pages 8-9): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

5. (manchev2014anewform pages 10-11): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

6. (manchev2014anewform pages 3-4): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

7. (manchev2014anewform pages 6-8): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

8. (manchev2014anewform pages 9-10): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

9. (palmabarqueros2021inheritedplateletdisorders pages 11-13): Verónica Palma-Barqueros, Nuria Revilla, Ana Sánchez, Ana Zamora Cánovas, Agustín Rodriguez-Alén, Ana Marín-Quílez, José Ramón González-Porras, Vicente Vicente, María Luisa Lozano, José María Bastida, and José Rivera. Inherited platelet disorders: an updated overview. International Journal of Molecular Sciences, 22:4521, Apr 2021. URL: https://doi.org/10.3390/ijms22094521, doi:10.3390/ijms22094521. This article has 144 citations.

10. (palmabarqueros2021inheritedplateletdisorders pages 15-17): Verónica Palma-Barqueros, Nuria Revilla, Ana Sánchez, Ana Zamora Cánovas, Agustín Rodriguez-Alén, Ana Marín-Quílez, José Ramón González-Porras, Vicente Vicente, María Luisa Lozano, José María Bastida, and José Rivera. Inherited platelet disorders: an updated overview. International Journal of Molecular Sciences, 22:4521, Apr 2021. URL: https://doi.org/10.3390/ijms22094521, doi:10.3390/ijms22094521. This article has 144 citations.

11. (noris2017hereditarythrombocytopeniasa pages 12-13): Patrizia Noris and Alessandro Pecci. Hereditary thrombocytopenias: a growing list of disorders. Hematology. American Society of Hematology. Education Program, 2017 1:385-399, Dec 2017. URL: https://doi.org/10.1182/asheducation-2017.1.385, doi:10.1182/asheducation-2017.1.385. This article has 163 citations.

12. (palmabarqueros2021inheritedplateletdisorders pages 21-22): Verónica Palma-Barqueros, Nuria Revilla, Ana Sánchez, Ana Zamora Cánovas, Agustín Rodriguez-Alén, Ana Marín-Quílez, José Ramón González-Porras, Vicente Vicente, María Luisa Lozano, José María Bastida, and José Rivera. Inherited platelet disorders: an updated overview. International Journal of Molecular Sciences, 22:4521, Apr 2021. URL: https://doi.org/10.3390/ijms22094521, doi:10.3390/ijms22094521. This article has 144 citations.

13. (johnson2017moleculargeneticinvestigation pages 51-55): BD Johnson. Molecular genetic investigation into inherited thrombocytopenia. Unknown journal, 2017.

14. (johnson2017moleculargeneticinvestigationa pages 51-55): BD Johnson. Molecular genetic investigation into inherited thrombocytopenia. Unknown journal, 2017.

15. (palmabarqueros2021inheritedplateletdisorders pages 1-3): Verónica Palma-Barqueros, Nuria Revilla, Ana Sánchez, Ana Zamora Cánovas, Agustín Rodriguez-Alén, Ana Marín-Quílez, José Ramón González-Porras, Vicente Vicente, María Luisa Lozano, José María Bastida, and José Rivera. Inherited platelet disorders: an updated overview. International Journal of Molecular Sciences, 22:4521, Apr 2021. URL: https://doi.org/10.3390/ijms22094521, doi:10.3390/ijms22094521. This article has 144 citations.

16. (donck2021hemostaticphenotypesand pages 6-7): Fabienne Ver Donck, Veerle Labarque, and Kathleen Freson. Hemostatic phenotypes and genetic disorders. Research and Practice in Thrombosis and Haemostasis, 5:e12637, Dec 2021. URL: https://doi.org/10.1002/rth2.12637, doi:10.1002/rth2.12637. This article has 24 citations and is from a peer-reviewed journal.

17. (palmabarqueros2021inheritedplateletdisorders pages 17-18): Verónica Palma-Barqueros, Nuria Revilla, Ana Sánchez, Ana Zamora Cánovas, Agustín Rodriguez-Alén, Ana Marín-Quílez, José Ramón González-Porras, Vicente Vicente, María Luisa Lozano, José María Bastida, and José Rivera. Inherited platelet disorders: an updated overview. International Journal of Molecular Sciences, 22:4521, Apr 2021. URL: https://doi.org/10.3390/ijms22094521, doi:10.3390/ijms22094521. This article has 144 citations.

18. (manchev2014anewform pages 2-3): Vladimir T. Manchev, Morgane Hilpert, Eliane Berrou, Ziane Elaib, Achille Aouba, Siham Boukour, Sylvie Souquere, Gerard Pierron, Philippe Rameau, Robert Andrews, François Lanza, Regis Bobe, William Vainchenker, Jean-Philippe Rosa, Marijke Bryckaert, Najet Debili, Remi Favier, and Hana Raslova. A new form of macrothrombocytopenia induced by a germ-line mutation in the prkacg gene. Blood, 124 16:2554-63, Oct 2014. URL: https://doi.org/10.1182/blood-2014-01-551820, doi:10.1182/blood-2014-01-551820. This article has 91 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Platelet-type_Bleeding_Disorder_19-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.