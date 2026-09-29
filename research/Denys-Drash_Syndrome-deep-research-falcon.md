---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T16:52:47.621250'
end_time: '2026-09-01T17:00:11.678445'
duration_seconds: 444.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Denys-Drash Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 6
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Denys-Drash_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Denys-Drash Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Denys-Drash Syndrome** covering all of the
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
- **Disease Name:** Denys-Drash Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Denys-Drash Syndrome** covering all of the
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


# Denys–Drash Syndrome: Disease-Characteristics Research Report

## Executive summary

Denys–Drash syndrome (DDS) is a very rare, usually de novo autosomal-dominant **WT1-related disorder**. Its canonical clinical triad is (1) congenital or early-childhood steroid-resistant nephrotic syndrome, usually caused by diffuse mesangial sclerosis (DMS); (2) predisposition to Wilms tumor; and (3) a disorder/difference of sex development (DSD), particularly gonadal dysgenesis and undervirilization in individuals with a 46,XY karyotype. Modern practice increasingly treats DDS as the severe, early-onset end of a continuous spectrum of WT1-associated nephropathy rather than as a completely discrete molecular entity. Open Targets identifies WT1 as the overwhelmingly strongest disease-associated target and maps DDS to **MONDO:0008682**. (OpenTargets Search: Denys-Drash syndrome-WT1, ratelade2010amurinemodel pages 1-2, ahmad2019theroleof pages 25-29)

The strongest mechanistic evidence comes from engineered mice and podocyte systems. A heterozygous WT1 zinc-finger mutation disrupts the transcriptional programs that establish and maintain podocyte identity, filtration-barrier architecture, and glomerular signaling. This produces proteinuria, DMS, and rapidly progressive kidney failure. Separately, impaired WT1-dependent genitourinary development contributes to 46,XY DSD, while loss of tumor-suppressor function in susceptible renal precursor cells predisposes to nephroblastoma. (ratelade2010amurinemodel pages 1-2)

| domain | evidence-based findings | ontology suggestions | evidence limitations |
|---|---|---|---|
| 1. Disease information | Denys-Drash syndrome (DDS) is a rare Mendelian WT1-associated syndrome defined by the classic triad of early-onset nephropathy, Wilms tumor predisposition, and 46,XY disorder/difference of sex development (DSD); Open Targets lists disease identifier MONDO:0008682 and strongest target association with WT1. Evidence base is aggregated disease-level plus individual case/cohort reports, not EHR-derived population surveillance (OpenTargets Search: Denys-Drash syndrome-WT1, ahmad2019theroleof pages 25-29) | MONDO:0008682; MeSH term suggestion: *Denys-Drash Syndrome* if used locally; NCIT disease term suggestion: *Denys-Drash Syndrome* | OMIM, Orphanet, ICD-10/11, and MeSH numeric identifiers were not verified in available tool context and should be left unfilled until source-confirmed |
| 2. Etiology | Primary cause is heterozygous germline WT1 pathogenic variation, classically in exons 8 or 9 affecting zinc-finger DNA-binding domains; inheritance is autosomal dominant, but many cases are de novo. No established environmental or infectious causes were identified in available evidence (ahmad2019theroleof pages 25-29, NCT07605884 chunk 1) | HGNC: WT1; SO variant classes: missense_variant, frameshift_variant, splice_donor_variant, splice_region_variant | Gene-environment interaction and protective factors are not established for DDS in available evidence |
| 3. Phenotypes | Core renal phenotype is diffuse mesangial sclerosis (DMS) causing congenital/infantile nephrotic syndrome, proteinuria, edema, and progression to kidney failure, often before age 5; extrarenal phenotypes include Wilms tumor and male pseudohermaphroditism/46,XY DSD with ambiguous or female external genitalia (ratelade2010amurinemodel pages 1-2, ahmad2019theroleof pages 25-29) | HPO: HP:0000093 Proteinuria; HP:0000100 Nephrotic syndrome; HP:0005567 Diffuse mesangial sclerosis; HP:0003774 Stage 5 chronic kidney disease; HP:0000830 Ambiguous genitalia; HP:0000119 Abnormality of the genitourinary system; HP:0002667 Nephroblastoma | Precise phenotype frequencies vary by case series; robust pooled percentages were not available in retrieved context |
| 4. Genetic/molecular information | WT1 is the main causal gene. Open Targets also shows weaker disease associations for GPC3 and WTIP, but these are not established primary causes of classic DDS. Functional consequence is loss of normal WT1 transcriptional regulation, with evidence supporting dominant-negative or threshold-reduction effects in some models (OpenTargets Search: Denys-Drash syndrome-WT1, ratelade2010amurinemodel pages 1-2) | HGNC:12796 WT1; GO:0003700 DNA-binding transcription factor activity; GO:0006355 regulation of DNA-templated transcription | Population allele frequencies, ClinVar classifications, and full variant catalog were not available from current tool context |
| 5. Environmental information | No specific environmental, lifestyle, toxin, or infectious trigger is established as causal for DDS; disease is chiefly genetic (ahmad2019theroleof pages 25-29, NCT07605884 chunk 1) | ExO/CHEBI not clearly applicable | Absence of evidence should not be interpreted as proof of no modifiers; targeted environmental studies are lacking |
| 6. Mechanism / pathophysiology | Causal chain: WT1 pathogenic variant leads to abnormal WT1 transcription factor function, which leads to impaired metanephric/podocyte developmental programs and altered podocyte identity, which leads to slit diaphragm/cytoskeletal and growth-factor dysregulation, which leads to DMS/proteinuria and progressive kidney failure; in parallel, abnormal genitourinary development leads to 46,XY DSD, and tumor-predisposition pathways increase Wilms tumor risk. Mouse and review evidence implicate WT1 control of FGF, BMP-pSMAD, FGF8/WNT4, and podocyte transcription factors MAFB, LMX1B, FOXC2, TCF21 (ratelade2010amurinemodel pages 1-2) | GO:0032835 glomerulus development; GO:0072006 nephron development; GO:1903671 regulation of sprouting angiogenesis; GO:0045666 positive regulation of neuron differentiation not primary; CL:0000653 podocyte; CL:0000099 mesangial cell; UBERON:0001285 glomerulus | Much detailed mechanism is inferred from mouse/review data rather than directly demonstrated in large human mechanistic cohorts |
| 7. Anatomical structures affected | Primary organs: kidney and gonads/genitourinary tract; secondary oncologic involvement: kidney Wilms tumor. At tissue/cell level, glomerulus—especially podocytes and mesangium—is central. Subcellularly, WT1 is a nuclear transcription factor (ratelade2010amurinemodel pages 1-2, ahmad2019theroleof pages 25-29) | UBERON:0002113 kidney; UBERON:0001285 glomerulus; UBERON:0000473 gonad; CL:0000653 podocyte; CL:0000099 mesangial cell; GO:0005634 nucleus | Broader systemic involvement is limited in available evidence; lateralization is mainly relevant for unilateral/bilateral Wilms tumor but DDS-specific rates were not retrieved |
| 8. Temporal development | Onset is typically congenital to early childhood for nephropathy; progression is rapid, with end-stage kidney disease (ESKD) often in early childhood. The transplant-focused study notes median transplant age 3.6 years in one French cohort description; registry/cohort evidence also supports early pediatric progression (ratelade2010amurinemodel pages 1-2, NCT07605884 chunk 1) | HPO onset modifiers: congenital onset, infantile onset, childhood onset | Natural-history staging data are sparse; remission is generally not expected without renal replacement/transplant strategies |
| 9. Inheritance and population | DDS is rare, classically autosomal dominant, frequently sporadic/de novo. Sex-development manifestations are especially relevant in 46,XY individuals. No reliable prevalence/incidence estimate was available in current evidence. Registry evidence indicates need for multicenter collection due to rarity (ahmad2019theroleof pages 25-29, NCT07605884 chunk 1) | GENO:0000135 autosomal dominant inheritance; HPO: HP:0001417 X-linked not applicable | Penetrance, founder effects, carrier frequency, and population-specific prevalence could not be quantified from available context |
| 10. Diagnostics | Diagnostic workup combines clinical suspicion (early nephrotic syndrome/DMS, Wilms tumor, ambiguous genitalia/46,XY DSD), kidney pathology, imaging for renal masses, karyotype/DSD assessment, and confirmatory WT1 molecular testing. Differential includes broader WT1-related disorders such as Frasier syndrome and isolated WT1 nephropathy (ahmad2019theroleof pages 25-29, NCT07605884 chunk 1) | HPO/NCIT suggestions: kidney biopsy, renal ultrasound, karyotyping, sequence analysis of WT1 | No DDS-specific formal diagnostic criteria document was retrieved; recommendations are based on expert practice and WT1-related disorder literature |
| 11. Outcome / prognosis | Morbidity is driven by steroid-resistant nephrotic syndrome, ESKD, tumor risk, DSD-related surgical/endocrine issues, and transplant complications. Recent registry/trial context highlights post-transplant lymphoproliferative disorder (PTLD) concern, with French data cited in protocol suggesting 20% PTLD risk versus ~4% in general transplant populations (NCT07605884 chunk 1) | HPO: HP:0003774 Stage 5 CKD; NCIT: renal replacement therapy; PTLD term suggestion | Survival and long-term life expectancy estimates were not available in current verified context |
| 12. Treatment | No disease-modifying WT1-targeted therapy is established. Management is supportive and complication-directed: nephrotic syndrome care, nephrectomy in selected cases, dialysis, kidney transplantation, Wilms tumor treatment per pediatric oncology protocols, and multidisciplinary DSD care. Recent single-center WT1-associated transplant cohort reported no disease recurrence and preserved graft function after median 32 months, though not DDS-only (summarized in retrieved literature) (NCT07605884 chunk 1) | NCIT: Nephrectomy; Dialysis; Kidney Transplantation; Chemotherapy Regimen; Gonadectomy when indicated in DSD/WT1 care | Evidence is largely observational, retrospective, or extrapolated from WT1-associated disease and Wilms tumor management rather than DDS-specific trials |
| 13. Prevention | Primary prevention of genetic occurrence is not available. Secondary prevention centers on early genetic diagnosis and tumor/renal surveillance in at-risk children; tertiary prevention involves CKD management, transplant planning, and long-term DSD/oncology follow-up. Genetic counseling is central for family planning (ahmad2019theroleof pages 25-29, NCT07605884 chunk 1) | NCIT: Genetic Counseling; Surveillance; Ultrasonography | Exact surveillance intervals were not source-verified in current context and should not be over-specified here |
| 14. Other species / natural disease | No naturally occurring veterinary analogue was established in available context. Comparative relevance comes mainly from engineered mouse models rather than spontaneous disease in other species (ratelade2010amurinemodel pages 1-2) | NCBI Taxon suggestion if needed for negative annotation: *Mus musculus* 10090 for model, not natural disease | OMIA-style natural disease evidence was not retrieved |
| 15. Model organisms and current research | Mouse DDS models carrying WT1 missense alleles (for example p.Arg394Trp) recapitulate glomerulosclerosis/DMS-like renal disease and identified altered podocyte transcriptional targets including *Scel*, *Sulf1*, and *Cyp26a1*; in vitro podocyte proteomic work supports dedifferentiation-associated changes. Current research is largely observational/registry-based, including WT1 mutation registry NCT01252901, UK rare kidney disease registry NCT06065852, rare disease natural history registry NCT01793168, and PTLD risk study NCT07605884 (ratelade2010amurinemodel pages 1-2, NCT07605884 chunk 1) | NCBI Taxon:10090; CL:0000653 podocyte; GO:0006351 transcription, DNA-templated; NCIT: Disease Registry | 2023-2024 DDS-specific interventional trials, spatial transcriptomics, or multi-omics integration studies were not identified in available tool context |


*Table: This table summarizes evidence-based, knowledge-base-ready findings for Denys-Drash syndrome across all 15 requested domains. It highlights what is supported by available human, mouse, in vitro, and registry evidence while explicitly marking unverified identifiers and data gaps.*

## 1. Disease information

**Definition.** DDS is a Mendelian developmental kidney and cancer-predisposition syndrome associated with heterozygous germline pathogenic variants in **WT1**, encoding the WT1 transcription factor. The historical triad comprises progressive nephropathy/DMS, Wilms tumor, and 46,XY DSD (“male pseudohermaphroditism” in older literature). Not every affected person has all three manifestations; therefore, genotype-first descriptions such as *WT1 disorder* or *WT1-associated nephropathy* are now often more accurate. (ratelade2010amurinemodel pages 1-2, ahmad2019theroleof pages 25-29)

**Identifiers and synonyms**

- **MONDO:** MONDO:0008682, Denys–Drash syndrome. (OpenTargets Search: Denys-Drash syndrome-WT1)
- **OMIM:** commonly indexed as **Denys–Drash syndrome, 194080**; the causal gene is **WT1, 607102**. The disease number should be independently checked against the current OMIM release before automated ingestion.
- **Orphanet:** commonly indexed as **ORPHA:220**; verify against the current Orphanet release before ingestion.
- **MeSH:** *Denys-Drash Syndrome*.
- **ICD:** there is no sufficiently specific DDS code in routine ICD-10-CM; cases are generally represented using component codes for congenital malformation/DSD, nephrotic syndrome or kidney failure, and Wilms tumor. ICD-11 terminology should likewise be verified in the implementation being used.
- **Synonyms:** Drash syndrome; Denys–Drash syndrome; DDS; WT1-related Denys–Drash syndrome; nephropathy–Wilms tumor–genital anomaly syndrome.

The evidence base is principally aggregated disease resources, small retrospective cohorts, registries, individual clinical cases, tumor series, and engineered models—not population-scale EHR epidemiology.

## 2. Etiology and risk factors

### Primary cause

DDS is caused chiefly by a **heterozygous germline WT1 pathogenic variant**. Classic DDS variants are missense substitutions in exons 8 or 9, which encode zinc fingers 2 and 3 of the DNA-binding domain. Historical molecular series found WT1 variants in 10/17 and 6/8 clinically diagnosed patients, illustrating both the central role of WT1 and the limitations of early testing methods. (ahmad2019theroleof pages 25-29)

Most cases are sporadic and presumed or demonstrated de novo. A person carrying a pathogenic variant has an autosomal-dominant transmission risk of 50% for each pregnancy, although reproductive fitness may be reduced by severe childhood disease or gonadal dysgenesis.

### Variant and phenotype considerations

- **Classic DDS:** predominantly zinc-finger missense variants, often in exons 8–9. Recurrent substitutions include variants affecting Arg394, such as p.Arg394Trp in the historical numbering used by the mouse-model literature. (ratelade2010amurinemodel pages 1-2)
- **Frasier syndrome:** classically intron 9 donor-region variants that alter the +KTS/−KTS splice-isoform ratio; usually later nephropathy, FSGS, 46,XY gonadal dysgenesis, and gonadoblastoma risk, with a lower Wilms-tumor risk than classic DDS.
- **Truncating/deletion variants:** may produce Wilms tumor predisposition, nephropathy, genital anomalies, or overlapping phenotypes. Thus, variant class predicts risk imperfectly.
- **Population frequency:** fully penetrant classic DDS variants should be absent or exceptionally rare in reference populations such as gnomAD. Variant-specific gnomAD and ClinVar records must nevertheless be checked individually.

Open Targets also reports low-scoring associations with **GPC3** and **WTIP**, but these should not be encoded as established primary DDS genes. GPC3 is relevant to an overlapping Wilms-tumor/overgrowth differential, and WTIP is biologically connected to WT1/podocyte pathways; **WT1 remains the definitive causal gene**. (OpenTargets Search: Denys-Drash syndrome-WT1)

### Environmental, protective, and gene–environment factors

No toxin, lifestyle exposure, nutritional factor, or infectious agent is established as a cause of DDS. No reproducible protective allele or environmental exposure is known to prevent expression of a pathogenic WT1 variant. Clinical severity may be affected by general modifiers of kidney injury—blood pressure, infections, nephrotoxins, and treatment—but these are downstream modifiers rather than causes. Formal DDS-specific gene–environment studies are lacking.

## 3. Phenotypes

| Phenotype | Type and usual course | Suggested HPO term |
|---|---|---|
| Proteinuria | Laboratory abnormality; congenital, infantile, or early childhood; persistent and progressive | HP:0000093 |
| Nephrotic syndrome | Clinical/laboratory syndrome with heavy proteinuria, hypoalbuminemia, and edema; generally steroid resistant | HP:0000100; HP:0003073 hypoalbuminemia; HP:0000969 edema |
| Diffuse mesangial sclerosis | Biopsy manifestation; severe and progressive, often leading to kidney failure before age five | HP:0005567 |
| Chronic kidney disease/kidney failure | Progressive renal impairment; often early childhood | HP:0012622; HP:0003774 |
| Wilms tumor/nephroblastoma | Renal malignancy, commonly early childhood; may be unilateral or bilateral/multifocal | HP:0002667 |
| Ambiguous or undervirilized genitalia | Congenital physical manifestation in some 46,XY individuals | HP:0000062/HP:0000830, subject to HPO-release verification |
| Gonadal dysgenesis/streak gonads | Congenital reproductive phenotype, most relevant in 46,XY individuals | HP:0000133; HP:0000140 |
| Hypertension | Secondary renal sign; frequency increases with progressive CKD | HP:0000822 |
| Hematuria | Possible urinary abnormality, less defining than proteinuria | HP:0000790 |

The most reproducible timing statement is that DMS-associated renal disease begins in infancy or early childhood and commonly progresses to end-stage kidney disease before age five. (ratelade2010amurinemodel pages 1-2) Exact percentages for each triad component vary markedly with ascertainment and variant class; historical statements that nearly all DDS patients develop Wilms tumor should not be applied to all molecularly diagnosed WT1-nephropathy patients. (ahmad2019theroleof pages 25-29)

**Quality of life.** No validated DDS-specific EQ-5D, SF-36, PROMIS, or utility dataset was identified. Expected burdens include edema and dietary/fluid restrictions, frequent laboratory and imaging visits, dialysis, major surgery, cancer treatment, transplantation and immunosuppression, fertility concerns, and psychosocial effects of DSD care. These impacts are clinically compelling but inadequately quantified in DDS-specific cohorts.

## 4. Genetic and molecular information

- **Gene:** WT1, chromosome 11p13; HGNC:12796; NCBI Gene:7490; OMIM gene entry 607102.
- **Protein:** WT1 transcription factor, a nuclear zinc-finger DNA/RNA-binding regulator with multiple isoforms, notably +KTS and −KTS.
- **Origin:** usually constitutional germline; a second somatic alteration or other cooperating event can occur in tumor tissue. A germline result should not be confused with tumor-only somatic WT1 alteration.
- **Mechanism:** classic zinc-finger missense variants impair sequence-specific DNA binding and may exert dominant-negative effects on wild-type WT1. Mouse evidence also supports a dosage or threshold model in which residual normal WT1 activity determines podocyte stability. (ratelade2010amurinemodel pages 1-2)
- **Classification:** recurrent zinc-finger variants with established DDS cases are generally pathogenic/likely pathogenic; novel variants require ACMG/AMP assessment using population rarity, de novo status, phenotype specificity, functional evidence, and segregation. A VUS alone does not establish DDS.
- **Chromosomal abnormalities:** larger 11p13 deletions involving WT1 cause WAGR-spectrum disease rather than classic DDS. Karyotype or chromosomal microarray is useful when syndromic features suggest a deletion, but most classic DDS cases have sequence-level variants.
- **Modifier genes/epigenetics:** no clinically validated modifier gene or DDS-specific constitutional epigenetic signature is established. Tumor evolution may involve additional genetic and epigenetic events, but these are not diagnostic of the constitutional syndrome.

## 5. Environmental information

Environmental toxins, radiation, smoking, alcohol, diet, occupation, and infectious agents are not recognized initiating factors. Avoiding nephrotoxins, controlling blood pressure, maintaining appropriate nutrition, and preventing infection are tertiary renal-care measures, not primary prevention of DDS. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous germline **WT1** pathogenic variant **leads to** reduced or qualitatively abnormal WT1 transcription-factor activity in developing renal and gonadal tissues.
2. Abnormal WT1 activity **leads to** impaired regulation of nephron-progenitor renewal, mesenchymal-to-epithelial transition, and podocyte differentiation/maintenance.
3. Impaired podocyte programs **lead to** altered slit-diaphragm, actin-cytoskeleton, focal-adhesion, polarity, and paracrine angiogenic/growth-factor signaling.
4. Podocyte dysfunction **results in** filtration-barrier failure, heavy proteinuria, and nephrotic syndrome.
5. Continued podocyte and mesangial injury **leads to** DMS/glomerulosclerosis, nephron loss, CKD, and early kidney failure.
6. **Branch A:** defective WT1-dependent sex determination and gonadal development **leads to** 46,XY gonadal dysgenesis and undervirilized/ambiguous external genitalia.
7. **Branch B:** constitutional loss of WT1 tumor-suppressor competence plus additional renal-cell events—this second-event sequence is partly inferred and varies by tumor—**leads to** nephrogenic precursor persistence and Wilms tumor.

### Molecular and cellular detail

WT1 regulates FGF and BMP–pSMAD signaling, the developmental regulators **SALL1** and **PAX2**, and mesenchymal-to-epithelial transition through **FGF8** and **WNT4**. In podocytes, WT1 helps establish identity through **MAFB, LMX1B, FOXC2**, and **TCF21**, coordinating cytoskeletal, slit-diaphragm, polarity, and basement-membrane attachment programs. These relationships derive substantially from developmental and model evidence and should therefore be annotated as mechanistic support rather than direct proof in every human DDS kidney. (ratelade2010amurinemodel pages 1-2)

The p.Arg394Trp knock-in mouse developed DMS-like disease and early renal failure and revealed altered glomerular expression of candidate WT1 targets including **Scel, Sulf1**, and **Cyp26a1**. The authors described the work as providing insight into “early mechanisms leading to glomerular” disease and concluded that the results support a threshold/dominant-negative model of WT1 function. (ratelade2010amurinemodel pages 1-2)

**Suggested annotations**

- Biological processes: GO:0072006 nephron development; GO:0032835 glomerulus development; GO:0006355 regulation of DNA-templated transcription; GO:0007275 multicellular organism development; mesenchymal-to-epithelial transition and kidney epithelium development terms should be release-checked.
- Molecular function: GO:0003700 DNA-binding transcription-factor activity; GO:0000976 transcription cis-regulatory-region binding.
- Cell types: CL:0000653 podocyte; CL:0000099 mesangial cell; nephron progenitor cell and gonadal supporting-cell terms should be checked against the current CL release.
- Cellular component: GO:0005634 nucleus; GO:0005923 bicellular tight junction is not a precise substitute for the slit diaphragm, so a current slit-diaphragm term should be used where available.

No validated DDS metabolomic or lipidomic diagnostic signature exists. Human single-cell/spatial studies specifically resolving classic DDS remain emerging; consequently, most current cell-state conclusions come from engineered models, bulk glomerular profiling, and podocyte culture rather than large human single-cell cohorts.

## 7. Anatomical structures affected

- **Primary:** kidneys (UBERON:0002113), renal glomeruli (UBERON:0001285), podocytes, mesangial compartment, and developing nephrogenic tissue.
- **Genital/reproductive:** gonads (UBERON:0000473), testes or dysgenetic/streak gonads, and internal/external genital structures in 46,XY DSD.
- **Tumor site:** one or both kidneys; bilateral or multifocal disease can occur in predisposition syndromes.
- **Subcellular:** WT1 acts primarily in the nucleus (GO:0005634); downstream dysfunction affects the podocyte actin cytoskeleton, cell–matrix adhesions, and slit diaphragm.

DMS is intrinsically diffuse and generally bilateral at the glomerular level. Wilms tumor, by contrast, can be unilateral, bilateral, or multifocal.

## 8. Temporal development

The constitutional lesion is present from conception, while phenotypic expression is developmental and age dependent. Genital differences are congenital. Proteinuria/nephrotic syndrome usually becomes evident congenitally, in infancy, or early childhood. DMS progresses chronically and often rapidly to kidney failure before age five. (ratelade2010amurinemodel pages 1-2)

A French transplant-study protocol reports a median kidney-transplant age of **3.6 years**, consistent with aggressive early renal progression. (NCT07605884 chunk 1) There is no spontaneous renal remission in established DMS; apparent pharmacologic responses in isolated reports should not be generalized. The critical intervention window is therefore before irreversible kidney failure or advanced tumor development: prompt WT1 testing, renal monitoring, tumor surveillance, and multidisciplinary planning.

## 9. Inheritance and population

DDS is autosomal dominant but commonly de novo. Penetrance is high for some WT1-associated phenotype, but penetrance of each individual component—DMS, Wilms tumor, or DSD—is incomplete and variant dependent. Expressivity is substantial, even among people grouped under WT1-related disease. Genetic anticipation is not recognized. Parental germline mosaicism is possible even when parental blood tests are negative, but its frequency is unknown.

No credible population prevalence, annual incidence, carrier frequency, founder effect, ethnic enrichment, or consanguinity effect was identified. DDS occurs worldwide and across ancestry groups. Apparent sex ratios depend on whether sex is classified by chromosomes, gonads, phenotype, or sex assignment; DSD ascertainment particularly enriches reported 46,XY cases. The disease is too rare and inconsistently defined historically for a robust cases-per-100,000 estimate.

## 10. Diagnostics

### Recommended approach

1. **Recognize the phenotype:** early steroid-resistant nephrotic syndrome, DMS, Wilms tumor at a young age, bilateral/multifocal Wilms tumor, or unexplained 46,XY DSD.
2. **Renal evaluation:** urinalysis and urine protein/creatinine ratio; serum albumin, creatinine/eGFR, electrolytes; blood pressure; edema and nutritional assessment.
3. **Imaging:** renal ultrasonography to assess tumor, nephrogenic rests, kidney size, and structural disease. MRI is preferred when more detailed tumor characterization is needed without ionizing radiation.
4. **Pathology:** biopsy typically shows DMS—mesangial-matrix expansion and sclerosis involving glomeruli—although biopsy can be avoided when genetic and clinical evidence is definitive or procedural risk is excessive.
5. **Molecular confirmation:** sequence and deletion/duplication analysis of WT1. A comprehensive steroid-resistant nephrotic syndrome/Wilms-predisposition panel is appropriate when the phenotype is atypical.
6. **DSD evaluation:** chromosome analysis or rapid sex-chromosome assessment, pelvic/abdominal imaging, gonadal and adrenal hormone testing as clinically indicated, and multidisciplinary endocrinology/urology/genetics review.
7. **Tumor genetics:** paired germline/tumor analysis can clarify constitutional predisposition and acquired tumor events but is not required to diagnose nephropathy.

**WES/WGS.** Exome or genome sequencing is useful if targeted testing is negative, if the phenotype overlaps another monogenic podocytopathy, or if structural/noncoding variation is suspected. Genome sequencing may better detect complex structural and selected intronic variants, but targeted WT1 analysis remains efficient for a classic presentation.

**CMA/karyotype/FISH.** CMA is appropriate for suspected 11p13 deletion/WAGR. Karyotype is important for DSD assessment. FISH has a limited confirmatory role. Mitochondrial and repeat-expansion testing are not routine DDS tests.

**Differential diagnosis:** Frasier syndrome and other WT1-related nephropathies; WAGR; isolated DMS; NPHS1/NPHS2/LAMB2/PLCE1 and other genetic nephrotic syndromes; Simpson–Golabi–Behmel syndrome; Beckwith–Wiedemann spectrum; sporadic Wilms tumor; and other causes of 46,XY DSD. Distinction increasingly rests on molecular diagnosis rather than requiring the complete historical triad.

## 11. Outcome and prognosis

Untreated nephropathy is progressive and typically culminates in childhood kidney failure. Long-term morbidity arises from dialysis, transplantation, tumor therapy, hypertension, CKD-mineral/bone disease, growth impairment, gonadal dysfunction, infertility, and psychosocial effects. DDS-specific five- and ten-year survival estimates were not found and should not be inferred from general Wilms-tumor survival statistics.

Kidney transplantation can provide durable renal replacement because the intrinsic podocytopathy does not usually recur in a genetically normal graft. However, tumor status and native-kidney management must be addressed first. A current French observational protocol cites **20% PTLD risk in DDS recipients versus approximately 4% in general transplant populations**, and a median transplantation age of 3.6 years; these figures are cohort/protocol observations, not universal rates. (NCT07605884 chunk 1)

Prognosis depends on variant class, age and rate of renal decline, Wilms-tumor stage/histology and bilaterality, treatment toxicity, DSD/gonadal-tumor issues, transplantation access, and post-transplant complications. No validated molecular prognostic score exists.

## 12. Treatment and current applications

There is no approved therapy that corrects WT1 dysfunction.

### Renal management

- Salt/fluid management, individualized nutrition, edema treatment, vaccination, and blood-pressure control.
- ACE-inhibitor or angiotensin-receptor-blocker therapy may reduce proteinuria when blood pressure, kidney function, and potassium permit; these are supportive rather than curative.
- Genetic DMS is generally steroid resistant. Prolonged empiric glucocorticoids or other immunosuppression should be avoided once a monogenic WT1 podocytopathy is established unless another indication exists.
- Dialysis is used for kidney failure or as a bridge to transplantation.
- Unilateral or bilateral nephrectomy is individualized according to tumor status, severe protein loss/hypertension, residual function, and transplant planning.
- Kidney transplantation is definitive renal replacement after oncologic assessment; genetic disease recurrence in the graft is not expected.

Suggested NCIT interventions: **Angiotensin-Converting Enzyme Inhibitor**, **Angiotensin Receptor Blocker**, **Dialysis**, **Nephrectomy**, and **Kidney Transplantation**; exact NCIT codes should be release-validated.

### Wilms tumor and DSD management

Wilms tumor is treated according to pediatric oncology risk, stage, histology, laterality, and cooperative-group protocol, using surgery plus chemotherapy, with radiotherapy for selected risk groups. Nephron-sparing strategies are particularly important for bilateral disease but must be balanced against oncologic control and already progressive DMS.

DSD management requires pediatric endocrinology, urology/surgery, genetics, psychology, nephrology, oncology, and ethics expertise. Gonadal management is individualized according to gonadal location/function, malignancy risk, the person’s values, and contemporary DSD standards; irreversible procedures should not be reduced to the older diagnosis label alone.

### Experimental therapy and trials

No DDS-specific gene therapy, CRISPR, RNA therapy, cell therapy, or targeted pharmacologic intervention was identified in clinical trials. Current real-world research is observational:

- **NCT01252901:** WT1-mutation-associated disease registry; completed; 52 participants.
- **NCT06065852:** UK National Registry of Rare Kidney Diseases; recruiting; target enrollment 35,000.
- **NCT01793168:** rare-disease registry/natural-history study; recruiting; target enrollment 20,000.
- **NCT07605884:** planned 108-participant observational case-control study of PTLD risk after transplantation in DDS. The protocol analyzes French data from 2000–2022. (NCT07605884 chunk 1)

These studies support natural-history and safety characterization but do not establish treatment efficacy.

## 13. Prevention

**Primary prevention:** no lifestyle or vaccine can prevent a de novo WT1 variant. Reproductive options after identification of a familial variant include genetic counseling, prenatal diagnosis, and IVF with preimplantation genetic testing for monogenic disease.

**Secondary prevention:** molecular diagnosis, cascade testing, renal monitoring, and Wilms-tumor surveillance can identify complications earlier. Common expert practice is renal ultrasonography approximately every three months through the principal childhood risk window, but the exact stopping age and protocol should follow the responsible cancer-predisposition guideline and variant-specific risk assessment rather than an unreferenced universal rule.

**Tertiary prevention:** aggressive CKD and hypertension management; avoidance of nephrotoxins; dialysis/transplant planning; vaccination before transplantation; tumor follow-up; DSD and gonadal surveillance; and monitoring for immunosuppression-related EBV/PTLD. The PTLD signal in the French protocol makes EBV-risk assessment and post-transplant viral monitoring especially important, although the magnitude requires confirmation. (NCT07605884 chunk 1)

## 14. Other species and natural disease

No well-established naturally occurring veterinary DDS counterpart was identified. DDS is not infectious, transmissible, or zoonotic. WT1 orthologs and renal-development functions are evolutionarily conserved, making engineered animals scientifically useful, but this does not constitute natural disease in those species.

## 15. Model organisms and advanced research

The most informative system is **Mus musculus** (NCBI Taxon:10090). Knock-in mice carrying the DDS-associated **Wt1 p.Arg394Trp** allele reproduce key renal features, including podocyte dysfunction, DMS/glomerulosclerosis, proteinuria, and early renal failure. Isolated-glomerulus expression profiling identified **Scel, Sulf1**, and **Cyp26a1** as altered candidate WT1 targets. This is strong causal model evidence, although timing, genetic background, and complete tumor/DSD penetrance differ from human disease. (ratelade2010amurinemodel pages 1-2)

Additional models include Wt1 hypomorphic, knockout/conditional-knockout, and truncating-allele mice; immortalized human podocytes derived from DDS patients; transfected podocyte systems for DNA-binding/localization assays; and kidney organoids or iPSC systems as emerging platforms. Patient-podocyte proteomics and model transcriptomics indicate dedifferentiation and cytoskeletal/signaling abnormalities, but no proteomic, metabolomic, or epigenomic signature is clinically validated.

## Recent developments and expert assessment

The major 2023–2024 conceptual development is the move from rigid eponymous categories toward a **WT1-related disorder spectrum**, integrating genotype, age at nephropathy, histology, DSD, and tumor risk. A 2024 review, *WT1-related disorders: more than Denys–Drash syndrome*, reflects this shift (López-González and Ariceta, *Pediatric Nephrology*, published online February 2024; DOI: https://doi.org/10.1007/s00467-024-06302-y). A 2024 review of developmental FSGS likewise emphasizes genetically defined podocytopathies and transplantation rather than treating the biopsy pattern as a stand-alone disease (Klomp et al., March 2024; DOI: https://doi.org/10.1159/000538345).

The practical expert interpretation is that DDS should be considered a **high-risk clinical presentation of germline WT1 dysfunction**, not a diagnosis requiring every element of the classic triad. Early genomic diagnosis can prevent ineffective immunosuppression, trigger tumor and DSD evaluation, guide family counseling, and permit coordinated oncologic and transplant planning. This interpretation is consistent with the strong WT1–DDS association and with model evidence connecting defective WT1 dosage/function directly to podocyte failure. (OpenTargets Search: Denys-Drash syndrome-WT1, ratelade2010amurinemodel pages 1-2)

## Key evidence quotations and references

1. **Ratelade et al., 2010, Human Molecular Genetics.** DOI: https://doi.org/10.1093/hmg/ddp462. The study describes DDS as involving “early-onset nephrotic syndrome, male pseudohermaphroditism, and Wilms tumor predisposition,” reports that DMS generally reaches renal failure before age five, and provides p.Arg394Trp mouse-model evidence for a WT1 activity-threshold/dominant-negative mechanism. (ratelade2010amurinemodel pages 1-2)
2. **Historical human genetics summarized in the retrieved literature:** Pelletier et al. identified WT1 variants in 10/17 DDS patients, while Baird et al. detected heterozygous germline variants in 6/8; the characteristic lesions clustered in exons 8–9. (ahmad2019theroleof pages 25-29)
3. **Open Targets, accessed through the research tool:** WT1 had five disease-evidence records and an association score of 0.853 for MONDO:0008682, far exceeding GPC3 or WTIP. Supporting PubMed records listed by the resource include PMID **1302008, 1658787, 1655284, 1327525, 8388765, 10571943, 9499425, 9529364, 9607189, 11182928**, and **24402088**. (OpenTargets Search: Denys-Drash syndrome-WT1)
4. **NCT07605884, ClinicalTrials.gov, 2026 protocol record.** The study reports a French-cohort signal of 20% PTLD in DDS transplant recipients versus 4% in general transplant populations and median transplant age 3.6 years; these data require prospective or independent confirmation. (NCT07605884 chunk 1)

## Evidence limitations

DDS is exceptionally rare, historical clinical definitions are inconsistent, and modern molecular cohorts often combine DDS, Frasier syndrome, isolated WT1 nephropathy, and other WT1 disorders. Consequently, many commonly repeated penetrance and tumor-risk percentages are ascertainment-sensitive. Recent 2023–2024 sources are mainly expert reviews rather than DDS-specific prospective cohorts. No randomized therapeutic trial, validated quality-of-life instrument, robust population incidence estimate, DDS-specific multi-omics diagnostic signature, or clinically established disease-modifying therapy was identified.

References

1. (OpenTargets Search: Denys-Drash syndrome-WT1): Open Targets Query (Denys-Drash syndrome-WT1, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (ratelade2010amurinemodel pages 1-2): Julien Ratelade, Christelle Arrondel, Ghislaine Hamard, Serge Garbay, Scott Harvey, Nathalie Biebuyck, Herbert Schulz, Nick Hastie, Marco Pontoglio, Marie-Claire Gubler, Corinne Antignac, and Laurence Heidet. A murine model of denys-drash syndrome reveals novel transcriptional targets of wt1 in podocytes. Human molecular genetics, 19 1:1-15, Sep 2010. URL: https://doi.org/10.1093/hmg/ddp462, doi:10.1093/hmg/ddp462. This article has 50 citations and is from a domain leading peer-reviewed journal.

3. (ahmad2019theroleof pages 25-29): AH Bin Ahmad. The role of wt1 in nephron endowment and glomeruloscerosis (gs)/chronic kidney disease (ckd). Unknown journal, 2019.

4. (NCT07605884 chunk 1):  Denys-Drash Syndrome and Risk of Post-transplant Lymphoproliferative Disorder. Assistance Publique - Hôpitaux de Paris. 2026. ClinicalTrials.gov Identifier: NCT07605884

## Artifacts

- [Edison artifact artifact-00](Denys-Drash_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 8 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000093` (2 mentions) - the report calls it "Laboratory abnormality; congenital, infantile, or early childhood; persistent and progressive"; HP calls it **Proteinuria**
- `HP:0005567` (2 mentions) - the report calls it "Biopsy manifestation; severe and progressive, often leading to kidney failure before age five"; HP calls it **Renal magnesium wasting**
- `HP:0002667` (2 mentions) - the report calls it "Renal malignancy, commonly early childhood; may be unilateral or bilateral/multifocal"; HP calls it **Nephroblastoma**
- `GO:0005634` (3 mentions) - the report calls it "Subcellular:** WT1 acts primarily in the nucleus"; GO calls it **nucleus**
- `HP:0000822` (1 mention) - the report calls it "Secondary renal sign; frequency increases with progressive CKD"; HP calls it **Hypertension**
- `HP:0000790` (1 mention) - the report calls it "Possible urinary abnormality, less defining than proteinuria"; HP calls it **Hematuria**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002113` (2 mentions) - the report calls it "Primary:** kidneys"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `UBERON:0000473` (2 mentions) - the report calls it "Genital/reproductive:** gonads"; UBERON calls it **testis**, and lists "gonad of male reproductive system" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`, `ORPHA`, `Gene`.
