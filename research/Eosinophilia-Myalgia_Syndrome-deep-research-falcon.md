---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T12:46:18.144410'
end_time: '2026-09-25T12:54:34.067990'
duration_seconds: 495.92
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Eosinophilia-Myalgia Syndrome
  mondo_id: MONDO:0004941
  category: Environmental
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Eosinophilia-Myalgia_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Eosinophilia-Myalgia Syndrome
- **MONDO ID:** MONDO:0004941 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Eosinophilia-Myalgia Syndrome** covering all of the
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
- **Disease Name:** Eosinophilia-Myalgia Syndrome
- **MONDO ID:** MONDO:0004941 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Eosinophilia-Myalgia Syndrome** covering all of the
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


# Eosinophilia–Myalgia Syndrome: Disease Characteristics Research Report

## Executive summary

Eosinophilia–myalgia syndrome (EMS) is a rare, acquired, noninfectious multisystem inflammatory and fibrosing disease. Its defining presentation is subacute, disabling generalized myalgia with peripheral eosinophilia, often followed by edema, rash, fasciitis, scleroderma-like skin induration, myopathy, and peripheral neuropathy. The major epidemic began in 1989 and was strongly associated with manufactured L-tryptophan supplements—particularly contaminated lots from one producer—not with an inherited mutation. Approximately 1,500 cases were officially reported; mortality estimates vary with surveillance date and source from 27 to about 40 deaths. Current cases are exceptionally rare, but recurrence remains possible with contaminated L-tryptophan or 5-hydroxytryptophan products. (varga1993ltryptophanandthe pages 1-2, allen2011postepidemiceosinophiliamyalgiasyndrome pages 1-2, NCT00001918 chunk 1, silver1994amurinemodel pages 1-3)

The evidence base is unusual: most EMS-specific clinical and mechanistic knowledge comes from the 1989–1990 epidemic and subsequent 1990s studies. Research published in 2023–2024 has concentrated on impurity detection and product safety rather than new patients or therapies. There is no validated disease-specific biomarker, causal gene, approved EMS-specific drug, randomized therapeutic trial, or contemporary incidence estimate. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6, NCT00001918 chunk 1, lee2023simultaneousdeterminationof pages 1-2, bampidis2024safetyandefficacy pages 1-2)

| Knowledge-base field | Eosinophilia-Myalgia Syndrome summary | Ontology suggestions |
|---|---|---|
| Definition/category | Rare, environmentally acquired multisystem inflammatory and fibrosing disorder characterized by severe generalized myalgia, peripheral eosinophilia, and later fasciitis, skin induration, myopathy, or neuropathy; principally associated with contaminated manufactured L-tryptophan. | MONDO:0004941; MeSH:D016603; category: environmental/toxic exposure disease |
| Identifiers | MONDO and MeSH identifiers are established above. No disease-specific OMIM entry is expected because EMS is not Mendelian; Orphanet and dedicated ICD-10/ICD-11 identifiers were not confirmed and should not be inferred. | MONDO:0004941; MeSH:D016603 |
| Trigger | Oral L-tryptophan supplements, especially 1989 lots from one manufacturer containing more than 60 impurities. Epidemiologically associated candidates include EBT (“peak E”), PAA, IMT, PIC, HIT, and AAA, but no single contaminant has been proved to be solely causal. | L-tryptophan—CHEBI:16828; EBT/PAA disease-exposure CHEBI identifiers: not confirmed (varga1993ltryptophanandthe pages 4-5, lee2023simultaneousdeterminationof pages 1-2) |
| Diagnostic core | Historical CDC surveillance definition: blood eosinophils >1,000/mm³, generalized myalgia severe enough to limit usual activity, and exclusion of infection or neoplasm. The definition was intended for surveillance, not as a stand-alone clinical diagnostic standard; revised 2001 criteria reportedly achieved 97% specificity. | Eosinophilia—HP:0001880; Myalgia—HP:0003326 (silver1994amurinemodel pages 1-3, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6) |
| Major acute phenotypes | Myalgia 100%; rash 71%; edema 52%; fever 41%; arthralgia 35%; respiratory manifestations 32% in a summarized outbreak series. A Maryland series reported joint pain 53%, rash and extremity edema 47% each, dyspnea 33%, and fever 27%. Frequencies vary by cohort and ascertainment. | HP:0003326 Myalgia; HP:0000988 Skin rash; HP:0000969 Edema; HP:0001945 Fever; HP:0002829 Arthralgia; HP:0002094 Dyspnea (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5, varga1993ltryptophanandthe pages 2-3) |
| Chronic phenotypes | Weight loss 50%, muscle weakness 44%, paresthesia 42%, scleroderma-like skin induration 42%, xerostomia 36%, and alopecia 33%; persistent painful neuropathy, myopathy, fasciitis, contractures, and disability may occur despite normalization of eosinophilia. | HP:0001824 Weight loss; HP:0001324 Muscle weakness; HP:0003401 Paresthesia; HP:0000958 Dry skin/xerosis only if clinically appropriate—not equivalent to xerostomia; HP:0001596 Alopecia; peripheral neuropathy term/ID should be ontology-validated (varga1993ltryptophanandthe pages 2-3, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6) |
| Epidemiology | The 1989 epidemic produced more than 1,500 reported US cases; reported deaths vary by surveillance date/source from 27 to approximately 40. Cases were predominantly middle-aged women; one Maryland series was 93% female with median age 51 years. Incidence is now extremely low and no reliable current prevalence is available. | Epidemiologic annotations; no inheritance ontology applicable (varga1993ltryptophanandthe pages 1-2, roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5, NCT00001918 chunk 1, silver1994amurinemodel pages 1-3) |
| Genetic susceptibility/protection | No causal gene or pathogenic variant is established. Among L-tryptophan users, HLA-DRB1*03, HLA-DRB1*04, and HLA-DQA1*0601 were susceptibility markers; DRB1*04 had OR 3.93 (95% CI 1.08–16.37). DRB1*07 and DQA1*0501 were protective; among users of implicated lots, the DRB1*07–DQA1*0201 haplotype had OR 0.11 (95% CI 0.02–0.77). Results derive from a small retrospective cohort and are not diagnostic. | HLA gene/allele annotations; inheritance: not applicable; ClinVar/ACMG pathogenic-variant classification: not applicable (okada2009immunogeneticriskand pages 2-3, okada2009immunogeneticriskand pages 3-5) |
| Mechanism | Exposure induces an incompletely defined type-2 inflammatory response involving IL-5/IL-4, eosinophil expansion and tissue degranulation, followed by TGF-β-associated fibroblast activation, extracellular-matrix/collagen deposition, fascial and dermal fibrosis, myocyte injury, and peripheral nerve damage. Kynurenine/quinolinic-acid changes may contribute but remain uncertain. | GO:0043308 Eosinophil activation; GO:0030198 Extracellular matrix organization; GO:0032964 Collagen biosynthetic process; CL:0000771 Eosinophil; CL:0000057 Fibroblast; CL:0000097 Mast cell (varga1993ltryptophanandthe pages 3-4, allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, barth2001ltryptophancontaminant‘peak pages 1-2) |
| Anatomy | Primary sites are skeletal muscle, fascia/perimysium, dermis, subcutis, and peripheral nerves; lungs are commonly involved, while severe disease may affect the heart and other organs. Distribution is generally bilateral/systemic rather than unilateral. | UBERON:0001134 Skeletal muscle organ; UBERON:0002097 Skin of body; fascia/peripheral nerve/lung UBERON identifiers should be ontology-validated before ingestion (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, lee2023simultaneousdeterminationof pages 1-2) |
| Diagnosis | Exposure history plus CBC with differential and exclusion of parasitic/infectious, allergic, drug-induced, autoimmune, clonal, and malignant eosinophilia. Evaluate organ injury using CK/chemistry, pulmonary and cardiac testing, MRI of muscle/fascia, EMG/nerve-conduction studies, and full-thickness skin–fascia–muscle biopsy when needed. No validated genetic, proteomic, or metabolomic diagnostic test exists. | HPO terms above; LOINC/SNOMED codes should be mapped at test level; genetic testing: not routinely indicated (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, NCT00001918 chunk 1) |
| Treatment | Immediately discontinue the implicated supplement. Systemic glucocorticoids often reduce acute inflammation and eosinophilia but have inconsistent effects on chronic fibrosis and neuropathy. Mycophenolate, methotrexate, hydroxychloroquine, chlorambucil, or anakinra have only anecdotal/low-quality evidence; pain control and physical/occupational rehabilitation are important. No EMS-specific approved therapy or genotype-guided treatment exists. | NCIT suggestions: Corticosteroid Therapy, Immunosuppressive Therapy, Physical Therapy, Occupational Therapy; exact NCIT identifiers require validation (varga1993ltryptophanandthe pages 2-3, roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6) |
| Prevention | Avoid suspect or unregulated L-tryptophan/5-HTP products; enforce manufacturing controls, lot traceability, impurity testing, adverse-event surveillance, and rapid product withdrawal. A 2023 LC–MS/MS method measured selected impurities with detection limits below 11.2 μg/kg and quantification limits below 35.7 μg/kg in meat matrices. No vaccine, genetic screening, or chemoprophylaxis applies. | CHEBI:16828 L-tryptophan; environmental-exposure and product-quality annotations (varga1993ltryptophanandthe pages 1-2, lee2023simultaneousdeterminationof pages 1-2) |
| Clinical study | NCT00001918, “L-5-Hydroxy-Tryptophan-Related EMS: Clinical Patient Evaluation,” was a completed NIH/NIMH observational study (planned enrollment 20; July 1999–August 2000), not a therapeutic trial. It evaluated clinical, neurologic, psychiatric, imaging, laboratory, and supplement-impurity findings. | ClinicalTrials.gov:NCT00001918; NCIT: Observational Study—exact code should be validated (NCT00001918 chunk 1) |
| Models | Induced female C57BL/6 mouse model: daily intraperitoneal EBT caused dermal/subcutaneous inflammation, mast-cell accumulation, progressive fascial fibrosis, and transient myocyte necrosis. After six weeks, fascia measured 168±22 μm versus 43±5 μm with saline, but mice lacked peripheral eosinophilia and did not reproduce the complete human syndrome. Lewis-rat models also show myofascial inflammation/fibrosis. No confirmed naturally occurring veterinary EMS or transmissible/zoonotic form is known. | NCBI Taxon:10090 Mus musculus; NCBI Taxon:10116 Rattus norvegicus; CL:0000097 Mast cell; GO:0030198 Extracellular matrix organization (silver1994amurinemodel pages 1-3, silver1994amurinemodel pages 3-4, silver1994amurinemodel pages 4-6) |


*Table: Compact disease-level summary of eosinophilia-myalgia syndrome, including epidemiology, clinical features, exposure biology, genetics, management, prevention, and experimental models. Ontology mappings are limited to identifiers that can be assigned with reasonable confidence, with uncertain mappings explicitly flagged.*

## 1. Disease information

### Definition and identifiers

The historical US CDC surveillance definition required: **(1)** peripheral blood eosinophils greater than 1,000/mm³, **(2)** generalized myalgia sufficiently severe to limit usual activities, and **(3)** no infection or neoplasm explaining the findings. This definition was designed for outbreak surveillance, not as a stand-alone clinical diagnostic standard. Revised criteria published in 2001 reportedly achieved 97% specificity. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6, silver1994amurinemodel pages 1-3)

Key identifiers and names are:

- **MONDO:** MONDO:0004941.
- **MeSH:** D016603, *Eosinophilia-Myalgia Syndrome*, confirmed in the ClinicalTrials.gov record. (NCT00001918 chunk 1)
- **OMIM:** no disease-specific Mendelian entry is expected; EMS is acquired rather than a monogenic disorder.
- **Orphanet:** a dedicated identifier was not confirmed in the retrieved evidence and should not be inferred.
- **ICD-10/ICD-11:** no specific code was confirmed; coding generally requires syndrome manifestations or an adverse-effect/toxic-exposure code appropriate to the jurisdiction.
- **Synonyms:** eosinophilia-myalgia syndrome; L-tryptophan-associated eosinophilia-myalgia syndrome; L-tryptophan-associated EMS; tryptophan-associated EMS; historically, “L-tryptophan-associated neuromyopathy.”

The evidence summarized here is predominantly **aggregated disease-level evidence** from surveillance cohorts, case series, epidemiology, tissue studies, and experimental models. Individual-patient evidence is used only where post-epidemic cases illuminate recurrence, diagnosis, or molecular pathology; no EHR-derived population dataset was identified.

## 2. Etiology, risks, protective factors, and gene–environment interaction

### Primary causal factor

The strongest causal evidence is for ingestion of manufactured L-tryptophan containing process-related impurities. Epidemic lots came predominantly from one Japanese manufacturer after production changes that included a modified bacterial production strain and reduced purification. More than 60 impurities were subsequently detected. Six compounds were epidemiologically associated with affected lots: 3-phenylaminoalanine (PAA), 1,1′-ethylidenebis-L-tryptophan (EBT; “peak E”), 2-(3-indolylmethyl)-L-tryptophan (IMT), PIC, HIT, and AAA. Nevertheless, no single impurity has been proved to be the sole etiologic agent; EBT may be causal, contributory, or a marker of the responsible manufacturing conditions. (varga1993ltryptophanandthe pages 4-5, lee2023simultaneousdeterminationof pages 1-2, silver1994amurinemodel pages 1-3)

A useful authoritative formulation is the 1994 animal-model abstract: **“EBT may have been one of the mediators of EMS.”** This appropriately reflects the continuing uncertainty. (silver1994amurinemodel pages 1-3)

### Exposure and demographic risks

Reported supplement doses ranged from 10 mg to 15–16 g/day, with a typical median near 1.5 g/day. In the Maryland series, median exposure before onset was six months (range 1.5–11 months), although a later post-epidemic patient developed symptoms within three weeks at 1,500 mg/day. Higher dose was associated with disease: mean intake was 4,160.7 mg/day in affected users versus 2,898.7 mg/day in unaffected users, OR 1.35 (95% CI 1.05–1.79, as modeled in that study). Age ≥45 years also increased risk, OR 3.01 (95% CI 1.03–8.75). (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5, allen2011postepidemiceosinophiliamyalgiasyndrome pages 1-2, okada2009immunogeneticriskand pages 2-3)

Women predominated markedly in surveillance cohorts—14/15 Maryland patients (93%) were women—but immunogenetic analysis did not identify sex as an independent risk factor after accounting for exposure and other variables. This may partly reflect patterns of supplement use. Smoking, alcohol, occupation, exercise, family history, and ordinary dietary tryptophan have not been established as EMS risk factors. There is no infectious cause. (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5, okada2009immunogeneticriskand pages 2-3)

### Genetic susceptibility and protection

No gene mutation causes EMS. A retrospective study of 94 unrelated White L-tryptophan users found exposure-modifying HLA associations:

- **HLA-DRB1*03:** OR 3.89 (95% CI 1.15–15.20).
- **HLA-DRB1*04:** OR 3.93 (95% CI 1.08–16.37); among users of implicated lots, OR 7.52 (95% CI 1.30–86.05).
- **HLA-DQA1*0601:** strong association, but with very wide confidence intervals because it was absent from unaffected exposed subjects.
- **Protective associations:** DRB1*07, DQA1*0501, and—among users of implicated lots—DQA1*0201. The inferred DRB1*07–DQA1*0201 haplotype occurred in 13.0% of EMS cases versus 57.1% of unaffected exposed users, OR 0.11 (95% CI 0.02–0.77). (okada2009immunogeneticriskand pages 2-3, okada2009immunogeneticriskand pages 3-5)

These are **susceptibility markers, not pathogenic variants**. The cohort was small, several confidence intervals were very wide, and replication is limited. Accordingly, ClinVar/ACMG variant classification, penetrance, carrier frequency, anticipation, mosaicism, founder effects, and consanguinity are not applicable. No validated modifier gene, protective coding variant, chromosomal abnormality, or EMS-specific epigenetic change is known.

The best-supported gene–environment model is therefore: contaminated supplement exposure is necessary in most epidemic cases, while HLA-mediated antigen presentation and age/dose modify whether exposed persons develop disease. (okada2009immunogeneticriskand pages 1-2, okada2009immunogeneticriskand pages 3-5)

## 3. Phenotypes

EMS is typically adult-onset and heterogeneous. Frequencies vary because the CDC definition selected severe cases and studies sampled different disease stages.

### Acute/subacute phenotypes

- **Severe generalized myalgia:** 100%; usually subacute and disabling. Suggested HPO: **HP:0003326**.
- **Peripheral eosinophilia:** 100% by surveillance definition; often transient. HPO: **HP:0001880**.
- **Rash:** 71% in one summarized series; 47% in Maryland. HPO: **HP:0000988**.
- **Peripheral/extremity edema:** 52% and 47%, respectively. HPO: **HP:0000969**.
- **Fever:** 41% or 27%. HPO: **HP:0001945**.
- **Arthralgia/joint pain:** 35% or 53%. HPO: **HP:0002829**.
- **Respiratory symptoms/dyspnea:** 32–33%, ranging from cough or breathlessness to pneumonitis. HPO: **HP:0002094** for dyspnea.
- **Fatigue and stiffness:** common but not consistently quantified.
- **Laboratory findings:** absolute eosinophils exceed 1,000/mm³ under the original definition; one Maryland cohort also reported lymphocytosis in 93%. (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5, varga1993ltryptophanandthe pages 2-3)

### Later and chronic phenotypes

Reported later manifestations include weight loss (50%), muscle weakness (44%), paresthesia (42%), scleroderma-like induration (42%), xerostomia (36%), and alopecia (33%). Suggested HPO terms include **HP:0001824** weight loss, **HP:0001324** muscle weakness, **HP:0003401** paresthesia, and **HP:0001596** alopecia. Fasciitis, painful sensorimotor neuropathy, muscle atrophy, contractures, restricted mobility, and cognitive symptoms may persist. (varga1993ltryptophanandthe pages 2-3, roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4)

The quality-of-life burden can be profound: documented consequences include inability to perform usual activities, wheelchair dependence, chronic pain, weakness, sensory loss, and contractures. No EMS-specific EQ-5D, SF-36, or PROMIS reference dataset was identified. (roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4)

## 4. Genetic and molecular information

There are **no causal genes, pathogenic germline or somatic variants, structural variants, or chromosomal abnormalities**. WES, WGS, gene panels, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing have no established diagnostic role.

Human lesional skin profiling in a post-epidemic case identified 343 differentially expressed genes at FDR 0.64%, including collagen and extracellular-matrix genes and signatures involving TGF-β and IL-4/IL-13 signaling. This is a downstream disease-state signature, not evidence of genomic causation. Earlier tissue work also reported increased TGF-β1 and collagen expression. No validated EMS methylome, proteomic classifier, metabolomic diagnostic signature, single-cell atlas, spatial-transcriptomic dataset, multi-omics study, or CRISPR screen was found. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, allen2011postepidemiceosinophiliamyalgiasyndrome pages 6-7)

## 5. Environmental, lifestyle, and infectious information

The relevant environment is an **ingested manufactured chemical mixture**. L-tryptophan itself is CHEBI:16828; EBT and PAA require identifier validation before knowledge-base ingestion. Ordinary food-derived tryptophan has not been shown to cause the epidemic syndrome. A published cashew-associated case is insufficient to establish normal foods as a general risk.

No reproducible association exists with smoking, alcohol, exercise, radiation, ambient pollution, or occupation. There is no bacterial, viral, fungal, or parasitic etiologic agent; however, parasitic infection must be excluded during diagnosis. In five Maryland patients tested, Trichinella serology was negative. (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Ingestion of contaminated manufactured L-tryptophan or possibly 5-HTP leads to systemic exposure to EBT/PAA and other process impurities.** The exposure–disease association is demonstrated; attribution to one molecule remains unresolved. (varga1993ltryptophanandthe pages 4-5, NCT00001918 chunk 1, lee2023simultaneousdeterminationof pages 1-2)
2. **Impurity exposure leads to activation of susceptible immune cells and a type-2 cytokine response.** EBT induced IL-5 and/or IL-10 in PBMC from 6/7 responding functional-somatic-syndrome subjects; this is in-vitro evidence, not direct proof in EMS patients. (barth2001ltryptophancontaminant‘peak pages 1-2)
3. **IL-5-rich inflammation leads to eosinophil expansion, recruitment, and tissue degranulation.** Human lesions contain eosinophil-derived neurotoxin and major basic protein even when intact eosinophils are sparse. Suggested GO: eosinophil activation (**GO:0043308**); CL: eosinophil (**CL:0000771**). (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5)
4. **Eosinophil products and Th2 cytokines lead to inflammatory injury of fascia, perimysium, dermis, muscle, lung, and peripheral nerves.** This step is biologically supported but the relative contribution of eosinophils versus lymphocytes, monocytes, and mast cells remains inferred. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, silver1994amurinemodel pages 1-3)
5. **Inflammation activates TGF-β/IL-4-associated fibroblast programs, resulting in collagen and extracellular-matrix deposition.** Suggested GO: extracellular-matrix organization (**GO:0030198**) and collagen biosynthetic process (**GO:0032964**); CL: fibroblast (**CL:0000057**). (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5)
6. **Fibrosis and myocyte injury result in fascial thickening, skin induration, painful myopathy, weakness, and contractures.** (roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4, silver1994amurinemodel pages 4-6)
7. **Branch A: perineural inflammation and eosinophil-mediated toxicity lead to chronic peripheral neuropathy and paresthesia.** Quinolinic-acid neurotoxicity is plausible but unproved. (varga1993ltryptophanandthe pages 3-4, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6)
8. **Branch B: pulmonary inflammation leads to dyspnea, ground-glass change, pneumonitis, and occasionally life-threatening organ injury.** (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6)

### Metabolic and cellular detail

Active disease has been associated with increased kynurenine and cerebrospinal-fluid quinolinic acid, suggesting cytokine-driven indoleamine-2,3-dioxygenase activation. Because EMS preparations did not directly increase IDO in normal mononuclear cells and the expected quinolinate lesion differs from EMS neuropathy, this is more likely secondary or contributory than the initiating defect. No enzyme deficiency, receptor mutation, protein aggregation disorder, or primary mitochondrial lesion is established. (varga1993ltryptophanandthe pages 3-4)

In the EBT mouse model, mast cells increased two- to nearly four-fold in affected skin layers and appeared to degranulate, suggesting a possible amplifying role. Relevant CL terms are mast cell (**CL:0000097**), lymphocyte, monocyte, eosinophil, fibroblast, skeletal-muscle cell, and peripheral neuron. (silver1994amurinemodel pages 3-4, silver1994amurinemodel pages 4-6)

## 7. Anatomy

Primary sites are bilateral/systemic skeletal muscle, fascia and perimysium, dermis, subcutis, and peripheral nerves. Suggested mappings include skeletal muscle organ **UBERON:0001134** and skin of body **UBERON:0002097**; fascia, peripheral nerve, lung, and myocardium identifiers should be ontology-validated before ingestion.

Lung involvement includes pneumonitis, ground-glass opacity, and restrictive or obstructive physiology. Cardiac and other visceral involvement can occur in severe disease but is less common. Histology shows dermal/fascial collagen and mucopolysaccharide accumulation, mononuclear and variably eosinophilic infiltrates, eosinophil-protein deposition, perimysial inflammation, myofiber atrophy/necrosis, and fibrosis. There is no characteristic lateralization. (varga1993ltryptophanandthe pages 1-2, allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4)

At the subcellular level, the evidence concerns extracellular eosinophil granule proteins and extracellular matrix rather than a consistently abnormal organelle. Relevant GO cellular components include extracellular matrix and collagen-containing extracellular matrix.

## 8. Temporal development

EMS is usually **adult-onset and acute-to-subacute**. During the epidemic, most onset dates fell between July 1989 and February 1990. Exposure may precede disease by weeks to months; onset can also occur shortly after discontinuation. (varga1993ltryptophanandthe pages 1-2, roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5, allen2011postepidemiceosinophiliamyalgiasyndrome pages 1-2)

A practical staging model is:

1. **Early inflammatory phase:** rapidly progressive myalgia, edema, rash, fever, and marked eosinophilia.
2. **Evolving tissue phase:** weakness, fasciitis, pulmonary disease, and neuropathic symptoms.
3. **Chronic fibrotic/neuromuscular phase:** eosinophilia may resolve while skin induration, neuropathy, myopathy, contractures, and disability persist.

Spontaneous or treatment-associated improvement occurs, but chronic disease is common. The most important intervention window is early recognition and immediate withdrawal of the exposure, before fixed fibrosis and nerve damage develop. Controlled evidence defining this window is unavailable. (varga1993ltryptophanandthe pages 1-2, roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6)

## 9. Inheritance and population epidemiology

EMS has **no Mendelian inheritance pattern**. Penetrance applies only informally to exposed populations and depends on dose, product lot, age, and immunogenetic susceptibility.

Official surveillance documented at least 1,543 cases by June 1991 and 27 deaths; later sources cite more than 1,500 cases and 38–40 deaths. These differences reflect surveillance date, case definition, and probable under-ascertainment. No reliable current prevalence or annual incidence per 100,000 exists. (varga1993ltryptophanandthe pages 1-2, NCT00001918 chunk 1, silver1994amurinemodel pages 1-3)

The epidemic was concentrated in the United States but cases occurred internationally. Adults, especially middle-aged women, dominated reported cohorts. There is no established ethnicity-specific causal variant or geographic founder effect. Geographic variation tracked supplement distribution and regulatory/manufacturing conditions rather than inherited ancestry. (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5, varga1993ltryptophanandthe pages 4-5)

## 10. Diagnostics

### Clinical approach

Diagnosis rests on the clinical syndrome, supplement history, eosinophil count, organ assessment, and exclusion of alternatives. Recommended evaluation includes:

- CBC with differential and serial absolute eosinophil counts.
- CK, aldolase, metabolic panel, liver tests, inflammatory markers, urinalysis, and cardiac biomarkers as indicated.
- Parasite testing guided by travel/exposure; medication and supplement reconciliation.
- ECG/echocardiography and pulmonary function testing; chest radiography or CT for cardiopulmonary symptoms.
- MRI of symptomatic muscle and fascia; muscle/fascial edema can support active disease.
- EMG and nerve-conduction studies for myopathy or neuropathy.
- Full-thickness skin-to-fascia/muscle biopsy when diagnosis remains uncertain. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4, NCT00001918 chunk 1)

There is no validated circulating EMS biomarker beyond nonspecific eosinophilia, and eosinophil normalization does not prove resolution. Chemical analysis of retained supplement lots by LC-MS/MS can support exposure investigation but cannot exclude EMS when the consumed material is unavailable or when relevant contaminants are unknown. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, lee2023simultaneousdeterminationof pages 1-2)

### Differential diagnosis

Important alternatives include eosinophilic fasciitis, hypereosinophilic syndrome and clonal eosinophilia, eosinophilic granulomatosis with polyangiitis, parasitic infection, drug-induced eosinophilia/DRESS, eosinophilic myositis, systemic sclerosis, inflammatory myopathy, toxic-oil syndrome, malignancy, and eosinophilic pneumonia. EMS is distinguished by the exposure history, severe generalized myalgia, epidemic/toxic context, and combined fascial, neuromuscular, cutaneous, and pulmonary phenotype. Genetic testing is reserved for an alternative suspected clonal or inherited eosinophilic disorder, not EMS itself.

There is no recommended population, newborn, carrier, prenatal, or cascade screening.

## 11. Outcome and prognosis

Acute EMS can be fatal, but disease-specific 5- or 10-year survival estimates are unavailable. Historical surveillance mortality was approximately 2% using 27–40 deaths among roughly 1,500 reported cases, although both numerator and denominator are uncertain. (varga1993ltryptophanandthe pages 1-2, NCT00001918 chunk 1)

Morbidity is more prominent than mortality. Eosinophilia, fever, edema, rash, and pulmonary inflammation may improve, whereas fixed fibrosis, weakness, neuropathic pain, sensory loss, and contractures can persist for years. In the 2011 post-epidemic case, prednisone plus mycophenolate resolved eosinophilia and pulmonary ground-glass changes and modestly improved strength/myalgia, but skin induration and neuropathy progressed. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6)

Probable adverse prognostic factors include severe early organ involvement, neuropathy, established fibrosis, delayed withdrawal, and incomplete response to anti-inflammatory therapy. No validated prognostic score or molecular prognostic biomarker exists.

## 12. Treatment

1. **Immediately stop L-tryptophan, 5-HTP, and any suspect supplement.** This is the essential intervention. In one case, withdrawal was followed within four weeks by falling eosinophils and remission of respiratory symptoms and myalgia. (roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4)
2. **Systemic glucocorticoids** are commonly used for severe inflammatory, pulmonary, fascial, or neurologic disease. They often suppress eosinophilia and acute inflammation but have inconsistent effects on established fibrosis, myopathy, and neuropathy; historical comparisons did not show clearly superior overall outcomes. Suggested NCIT concept: corticosteroid therapy. (varga1993ltryptophanandthe pages 1-2, varga1993ltryptophanandthe pages 2-3)
3. **Steroid-sparing immunosuppression** may be individualized. Mycophenolate produced partial benefit in one modern case; methotrexate and anakinra did not prevent progression. Hydroxychloroquine and chlorambucil have only anecdotal historical use. There are no reliable response rates. (roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6)
4. **Supportive care** includes analgesia, neuropathic-pain treatment, physical and occupational therapy, contracture prevention, pulmonary/cardiac management, nutrition, and psychological support. Suggested NCIT concepts include physical therapy, occupational therapy, pain management, and immunosuppressive therapy; exact identifiers should be validated.

No gene, RNA, cell, surgical, or approved targeted biologic therapy exists. Anti-IL-5 drugs are mechanistically interesting but cannot be recommended specifically for EMS without clinical evidence. No pharmacogenomic guidance or personalized genotype-directed treatment exists.

**Clinical trial status:** NCT00001918, “L-5-Hydroxy-Tryptophan-Related EMS: Clinical Patient Evaluation,” was a completed NIH/NIMH observational study with planned enrollment of 20, running July 1999–August 2000. It was not a treatment trial and evaluated clinical, neurologic, psychiatric, imaging, laboratory, and supplement-chemistry findings. URL: https://clinicaltrials.gov/study/NCT00001918. (NCT00001918 chunk 1)

## 13. Prevention

**Primary prevention** is the principal public-health strategy: avoid unregulated or suspect L-tryptophan/5-HTP products; use validated fermentation and purification processes; test for known and unknown impurities; maintain lot traceability; and rapidly recall implicated products. The sharp fall in incidence after the FDA recall strongly supports exposure removal. (varga1993ltryptophanandthe pages 1-2)

Recent implementation is analytical rather than clinical. A study published online **2 January 2023** developed a five-minute LC-MS/MS assay for selected tryptophan impurities in meat matrices, with method detection limits below 11.2 μg/kg and quantification limits below 35.7 μg/kg. DOI/URL: https://doi.org/10.1007/s00726-022-03215-8. (lee2023simultaneousdeterminationof pages 1-2)

An EFSA opinion adopted **12 March 2024** concluded that ≥98% L-tryptophan made with a specified non-genetically-modified *E. coli* strain was safe for non-ruminant feed use and presented no consumer or environmental concern under assessed conditions. This is product-specific regulatory evidence—not proof that every supplement is risk-free. DOI/URL: https://doi.org/10.2903/j.efsa.2024.8707. (bampidis2024safetyandefficacy pages 1-2)

**Secondary prevention** consists of rapid recognition, supplement cessation, adverse-event reporting, retained-lot testing, and early organ assessment. **Tertiary prevention** addresses fibrosis, contractures, falls, chronic neuropathy, and cardiopulmonary complications through rehabilitation and specialist monitoring. Vaccination, genetic screening, reproductive counseling, and chemoprophylaxis are not applicable.

## 14. Other species and natural disease

No confirmed naturally occurring EMS equivalent in companion animals, livestock, or wildlife was identified. EMS is not infectious, transmissible, or zoonotic. There is no breed predisposition, orthologous causal gene, or cross-species transmission concern.

Recent swine, poultry, and EFSA studies concern the toxicologic safety of tryptophan impurities and feed additives, not spontaneous veterinary EMS. Their relevance is regulatory and comparative-toxicologic rather than evidence of natural animal disease. (lee2023simultaneousdeterminationof pages 1-2, bampidis2024safetyandefficacy pages 1-2)

## 15. Model organisms

### Mouse model

Female C57BL/6 mice given daily intraperitoneal EBT developed dermal and subcutaneous inflammation, mast-cell accumulation, progressive fascial/perimysial fibrosis, and transient myofiber necrosis. At six weeks, fascia thickness was 168±22 μm versus 43±5 μm after saline and 69±7 μm after L-tryptophan alone (P<0.01). EBT-associated fibrosis was evident by day 6 and increased by day 21. (silver1994amurinemodel pages 1-3, silver1994amurinemodel pages 3-4, silver1994amurinemodel pages 4-6)

The model reproduces inflammatory fibrosis but not the full human syndrome: mice lacked significant peripheral eosinophilia, gross weakness, and characteristic multisystem disease. Intraperitoneal pure EBT also differs from oral exposure to a complex contaminant mixture. NCBI Taxon: **10090, Mus musculus**. (silver1994amurinemodel pages 3-4)

### Rat and in-vitro models

Female Lewis rats exposed to implicated tryptophan lots or synthetic EBT developed myofascial inflammation/fibrosis, but findings varied across experiments. NCBI Taxon: **10116, Rattus norvegicus**. Human PBMC cultures provide a complementary mechanistic model: 7/12 subjects with functional somatic syndromes responded to EBT versus 3/24 controls (P<0.05), with IL-5 and/or IL-10 in six of seven responders. This suggests host-dependent type-2 reactivity but was not performed directly in an EMS cohort and cannot establish clinical susceptibility. (varga1993ltryptophanandthe pages 4-5, barth2001ltryptophancontaminant‘peak pages 1-2)

## Evidence appraisal and current research gaps

The exposure–disease relationship is compelling because of temporal clustering, lot/manufacturer association, dose effects, biological plausibility, and disappearance after recall. Expert interpretation should nevertheless separate that strong inference from the weaker claim that EBT alone caused every case. Animal findings, multiple correlated impurities, occasional cases without demonstrable EBT, and absent retained product all preserve etiologic uncertainty. (varga1993ltryptophanandthe pages 4-5, allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5, allen2011postepidemiceosinophiliamyalgiasyndrome pages 6-7)

Major unmet needs are validated modern diagnostic criteria, prospective natural-history data, contaminant-independent biomarkers, replication of HLA associations, contemporary exposure surveillance, and controlled studies of anti-fibrotic or eosinophil-directed therapy. Because EMS is now extremely rare, international case registries and standardized biobanking are more feasible than conventional randomized trials.

### Selected primary and authoritative sources

- Varga J, Jimenez SA, Uitto J. *L-tryptophan and the eosinophilia-myalgia syndrome*. **January 1993**. DOI: https://doi.org/10.1038/jid.1993.31. (varga1993ltryptophanandthe pages 1-2)
- Roubenoff R et al. *Eosinophilia-myalgia syndrome due to L-tryptophan ingestion*. **July 1990**. DOI: https://doi.org/10.1002/art.1780330703. (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5)
- Silver RM et al. *A murine model…induced by EBT*. **April 1994**. DOI: https://doi.org/10.1172/JCI117125. The abstract states that EBT caused “inflammation and fibrosis affecting the dermis and subcutis, including the fascia and perimyseal tissues.” (silver1994amurinemodel pages 1-3)
- Barth H et al. *L-tryptophan contaminant ‘peak E’ induces release of IL-5 and IL-10*. **November 2001**. DOI: https://doi.org/10.1046/j.1365-2249.2001.01559.x. (barth2001ltryptophancontaminant‘peak pages 1-2)
- Okada S et al. *Immunogenetic risk and protective factors…*. **15 October 2009**. DOI: https://doi.org/10.1002/art.24460. (okada2009immunogeneticriskand pages 1-2, okada2009immunogeneticriskand pages 3-5)
- Allen JA et al. *Post-epidemic eosinophilia-myalgia syndrome associated with L-tryptophan*. **November 2011**. DOI: https://doi.org/10.1002/art.30514. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 1-2, allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6)
- NIH/NIMH ClinicalTrials.gov record NCT00001918. Background references include PMID **1690352**, **1727200**, and **1969024**. (NCT00001918 chunk 1)
- Lee DH et al. *Simultaneous determination of L-tryptophan impurities in meat products*. **2 January 2023**. DOI: https://doi.org/10.1007/s00726-022-03215-8. (lee2023simultaneousdeterminationof pages 1-2)
- EFSA FEEDAP Panel. *Safety and efficacy of an L-tryptophan feed additive*. Adopted **12 March 2024**. DOI: https://doi.org/10.2903/j.efsa.2024.8707. (bampidis2024safetyandefficacy pages 1-2)

References

1. (varga1993ltryptophanandthe pages 1-2): John Varga, Sergio A. Jimenez, and Jouni Uitto. L-tryptophan and the eosinophilia-myalgia syndrome: current understanding of the etiology and pathogenesis. The Journal of investigative dermatology, 100 1:97S-105S, Jan 1993. URL: https://doi.org/10.1038/jid.1993.31, doi:10.1038/jid.1993.31. This article has 54 citations.

2. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 1-2): Jeffrey A. Allen, Alicia Peterson, Robert Sufit, Monique E. Hinchcliff, J. Matthew Mahoney, Tammara A. Wood, Frederick W. Miller, Michael L. Whitfield, and John Varga. Post-epidemic eosinophilia-myalgia syndrome associated with l-tryptophan. Arthritis and rheumatism, 63 11:3633-9, Nov 2011. URL: https://doi.org/10.1002/art.30514, doi:10.1002/art.30514. This article has 99 citations.

3. (NCT00001918 chunk 1):  L-5-HTP-Related EMS. National Institute of Mental Health (NIMH). 1999. ClinicalTrials.gov Identifier: NCT00001918

4. (silver1994amurinemodel pages 1-3): R. Silver, A. Ludwicka, M. Hampton, T. Ohba, S. A. Bingel, T. Smith, R. Harley, J. Maize, and Melvyn P. Heyes. A murine model of the eosinophilia-myalgia syndrome induced by 1,1'-ethylidenebis (l-tryptophan). Journal of Clinical Investigation, 93:1473-1480, Apr 1994. URL: https://doi.org/10.1172/jci117125, doi:10.1172/jci117125. This article has 41 citations and is from a highest quality peer-reviewed journal.

5. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 5-6): Jeffrey A. Allen, Alicia Peterson, Robert Sufit, Monique E. Hinchcliff, J. Matthew Mahoney, Tammara A. Wood, Frederick W. Miller, Michael L. Whitfield, and John Varga. Post-epidemic eosinophilia-myalgia syndrome associated with l-tryptophan. Arthritis and rheumatism, 63 11:3633-9, Nov 2011. URL: https://doi.org/10.1002/art.30514, doi:10.1002/art.30514. This article has 99 citations.

6. (lee2023simultaneousdeterminationof pages 1-2): Doo-Hee Lee, Yang Hee Kim, Mina Baek, In Kyung Heo, and Yonguk Shin. Simultaneous determination of l-tryptophan impurities in meat products. Amino Acids, 55:173-182, Jan 2023. URL: https://doi.org/10.1007/s00726-022-03215-8, doi:10.1007/s00726-022-03215-8. This article has 6 citations and is from a peer-reviewed journal.

7. (bampidis2024safetyandefficacy pages 1-2): Vasileios Bampidis, Giovanna Azimonti, Maria de Lourdes Bastos, Henrik Christensen, Mojca Durjava, Birgit Dusemund, Maryline Kouba, Marta López‐Alonso, Secundino López Puente, Francesca Marcon, Baltasar Mayo, Alena Pechová, Mariana Petkova, Fernando Ramos, Roberto Edoardo Villa, Ruud Woutersen, Lieve Herman, Montserrat Anguita, Matteo Lorenzo Innocenti, Jordi Tarrés‐Call, and Elisa Pettenati. Safety and efficacy of a feed additive consisting of l‐tryptophan (produced with escherichia coli cgmcc 7.460) for all animal species (kempex holland b.v.). EFSA Journal, Apr 2024. URL: https://doi.org/10.2903/j.efsa.2024.8707, doi:10.2903/j.efsa.2024.8707. This article has 0 citations and is from a peer-reviewed journal.

8. (varga1993ltryptophanandthe pages 4-5): John Varga, Sergio A. Jimenez, and Jouni Uitto. L-tryptophan and the eosinophilia-myalgia syndrome: current understanding of the etiology and pathogenesis. The Journal of investigative dermatology, 100 1:97S-105S, Jan 1993. URL: https://doi.org/10.1038/jid.1993.31, doi:10.1038/jid.1993.31. This article has 54 citations.

9. (roubenoff1990eosinophiliamyalgiasyndromedue pages 4-5): Ronenn Roubenoff, Timothy Coté, Rosemarie Watson, Michael L. Levin, and Marc C. Hochberg. Eosinophilia-myalgia syndrome due to l-tryptophan ingestion. report of four cases and review of the maryland experience. Arthritis and rheumatism, 33 7:930-8, Jul 1990. URL: https://doi.org/10.1002/art.1780330703, doi:10.1002/art.1780330703. This article has 24 citations.

10. (varga1993ltryptophanandthe pages 2-3): John Varga, Sergio A. Jimenez, and Jouni Uitto. L-tryptophan and the eosinophilia-myalgia syndrome: current understanding of the etiology and pathogenesis. The Journal of investigative dermatology, 100 1:97S-105S, Jan 1993. URL: https://doi.org/10.1038/jid.1993.31, doi:10.1038/jid.1993.31. This article has 54 citations.

11. (okada2009immunogeneticriskand pages 2-3): Satoshi Okada, Mary L. Kamb, Janardan P. Pandey, Rossanne M. Philen, Lori A. Love, and Frederick W. Miller. Immunogenetic risk and protective factors for the development of l-tryptophan-associated eosinophilia-myalgia syndrome and associated symptoms. Arthritis and rheumatism, 61 10:1305-11, Oct 2009. URL: https://doi.org/10.1002/art.24460, doi:10.1002/art.24460. This article has 19 citations.

12. (okada2009immunogeneticriskand pages 3-5): Satoshi Okada, Mary L. Kamb, Janardan P. Pandey, Rossanne M. Philen, Lori A. Love, and Frederick W. Miller. Immunogenetic risk and protective factors for the development of l-tryptophan-associated eosinophilia-myalgia syndrome and associated symptoms. Arthritis and rheumatism, 61 10:1305-11, Oct 2009. URL: https://doi.org/10.1002/art.24460, doi:10.1002/art.24460. This article has 19 citations.

13. (varga1993ltryptophanandthe pages 3-4): John Varga, Sergio A. Jimenez, and Jouni Uitto. L-tryptophan and the eosinophilia-myalgia syndrome: current understanding of the etiology and pathogenesis. The Journal of investigative dermatology, 100 1:97S-105S, Jan 1993. URL: https://doi.org/10.1038/jid.1993.31, doi:10.1038/jid.1993.31. This article has 54 citations.

14. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 2-5): Jeffrey A. Allen, Alicia Peterson, Robert Sufit, Monique E. Hinchcliff, J. Matthew Mahoney, Tammara A. Wood, Frederick W. Miller, Michael L. Whitfield, and John Varga. Post-epidemic eosinophilia-myalgia syndrome associated with l-tryptophan. Arthritis and rheumatism, 63 11:3633-9, Nov 2011. URL: https://doi.org/10.1002/art.30514, doi:10.1002/art.30514. This article has 99 citations.

15. (barth2001ltryptophancontaminant‘peak pages 1-2): H Barth, R Klein, and P A Berg. L-tryptophan contaminant ‘peak e’ induces the release of il-5 and il-10 by peripheral blood mononuclear cells from patients with functional somatic syndromes. Clinical and Experimental Immunology, 126:187-192, Nov 2001. URL: https://doi.org/10.1046/j.1365-2249.2001.01559.x, doi:10.1046/j.1365-2249.2001.01559.x. This article has 12 citations and is from a peer-reviewed journal.

16. (roubenoff1990eosinophiliamyalgiasyndromedue pages 3-4): Ronenn Roubenoff, Timothy Coté, Rosemarie Watson, Michael L. Levin, and Marc C. Hochberg. Eosinophilia-myalgia syndrome due to l-tryptophan ingestion. report of four cases and review of the maryland experience. Arthritis and rheumatism, 33 7:930-8, Jul 1990. URL: https://doi.org/10.1002/art.1780330703, doi:10.1002/art.1780330703. This article has 24 citations.

17. (silver1994amurinemodel pages 3-4): R. Silver, A. Ludwicka, M. Hampton, T. Ohba, S. A. Bingel, T. Smith, R. Harley, J. Maize, and Melvyn P. Heyes. A murine model of the eosinophilia-myalgia syndrome induced by 1,1'-ethylidenebis (l-tryptophan). Journal of Clinical Investigation, 93:1473-1480, Apr 1994. URL: https://doi.org/10.1172/jci117125, doi:10.1172/jci117125. This article has 41 citations and is from a highest quality peer-reviewed journal.

18. (silver1994amurinemodel pages 4-6): R. Silver, A. Ludwicka, M. Hampton, T. Ohba, S. A. Bingel, T. Smith, R. Harley, J. Maize, and Melvyn P. Heyes. A murine model of the eosinophilia-myalgia syndrome induced by 1,1'-ethylidenebis (l-tryptophan). Journal of Clinical Investigation, 93:1473-1480, Apr 1994. URL: https://doi.org/10.1172/jci117125, doi:10.1172/jci117125. This article has 41 citations and is from a highest quality peer-reviewed journal.

19. (okada2009immunogeneticriskand pages 1-2): Satoshi Okada, Mary L. Kamb, Janardan P. Pandey, Rossanne M. Philen, Lori A. Love, and Frederick W. Miller. Immunogenetic risk and protective factors for the development of l-tryptophan-associated eosinophilia-myalgia syndrome and associated symptoms. Arthritis and rheumatism, 61 10:1305-11, Oct 2009. URL: https://doi.org/10.1002/art.24460, doi:10.1002/art.24460. This article has 19 citations.

20. (allen2011postepidemiceosinophiliamyalgiasyndrome pages 6-7): Jeffrey A. Allen, Alicia Peterson, Robert Sufit, Monique E. Hinchcliff, J. Matthew Mahoney, Tammara A. Wood, Frederick W. Miller, Michael L. Whitfield, and John Varga. Post-epidemic eosinophilia-myalgia syndrome associated with l-tryptophan. Arthritis and rheumatism, 63 11:3633-9, Nov 2011. URL: https://doi.org/10.1002/art.30514, doi:10.1002/art.30514. This article has 99 citations.

## Artifacts

- [Edison artifact artifact-00](Eosinophilia-Myalgia_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.2903/j.efsa.2024.8707` (4 mentions) - Safety and efficacy of a feed additive consisting of l‐tryptophan (produced with Escherichia coli CGMCC 7.460) for all animal species (Kempex Holland B.V.)
  - shared terms: exposure

Weighed against this report's own most characteristic terms: `ems`, `disease`, `model`, `l-tryptophan`, `exposure`, `syndrome`, `fibrosis`, `eosinophilia`, `ebt`, `include`, `neuropathy`, `clinical`, `eosinophil`, `nct00001918`, `peripheral`, `myalgia`, `chunk`, `inflammation`, `severe`, `validated`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
