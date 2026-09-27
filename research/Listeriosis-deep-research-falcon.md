---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:15:43.183976'
end_time: '2026-09-05T17:25:12.779139'
duration_seconds: 569.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Listeriosis
  mondo_id: MONDO:0005828
  category: Infectious
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
  path: Listeriosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Listeriosis
- **MONDO ID:** MONDO:0005828 (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Listeriosis** covering all of the
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
- **Disease Name:** Listeriosis
- **MONDO ID:** MONDO:0005828 (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Listeriosis** covering all of the
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


# Listeriosis (MONDO:0005828): comprehensive disease-characteristics report

## Executive summary and evidence scope

Listeriosis is a foodborne zoonotic infection caused principally by *Listeria monocytogenes*, a Gram-positive, non-spore-forming, facultatively anaerobic and facultatively intracellular bacillus. Most exposure does not produce recognized invasive disease, but susceptible hosts can develop bacteremia/sepsis, meningitis or meningoencephalitis, and maternal–fetal or neonatal infection. The authoritative 2023 review’s abstract states: “*Listeria monocytogenes is a Gram-positive facultative intracellular pathogen that can cause severe invasive infections upon ingestion with contaminated food*.” (koopmans2023humanlisteriosis pages 1-3)

This report integrates aggregated disease-level resources, reviews, surveillance evidence, model studies, and retrospective human cohorts. It is **not** derived from one patient’s EHR. Patient-level observations are included only where explicitly identified as hospital cohorts. Because the retrieved literature did not consistently expose PMID metadata, DOI URLs and publication dates are supplied; PMIDs should not be inferred where unavailable.

| Listeriosis Knowledge-Base Core | Current knowledge | Ontology suggestions | Evidence type | Source year / DOI |
|---|---|---|---|---|
| Disease identity and etiology | Rare, potentially severe foodborne zoonosis caused primarily by the Gram-positive, facultatively intracellular bacterium *Listeria monocytogenes*, usually after ingestion of contaminated food. Principal invasive presentations are bacteremia or septicemia, meningitis or meningoencephalitis, and maternal–fetal or neonatal infection. | MONDO: MONDO:0005828; NCBI Taxon: 1639 | Authoritative review | 2023; [10.1128/cmr.00060-19](https://doi.org/10.1128/cmr.00060-19) (koopmans2023humanlisteriosis pages 1-3) |
| Principal phenotypes | Among invasive cases, pregnancy-associated or neonatal infection accounts for approximately 14%, bacteremia or septicemia 52%, and CNS infection 31%; uncommon focal sites generally account for less than 1% each. | HPO: Fever HP:0001945; Meningitis HP:0001287; Encephalitis HP:0002383; Sepsis HP:0100806; Miscarriage HP:0005268 | Aggregated review evidence | 2023; [10.1128/cmr.00060-19](https://doi.org/10.1128/cmr.00060-19) (koopmans2023humanlisteriosis pages 1-3) |
| Recent phenotype frequencies | In a 2024 cohort of 71 confirmed cases, non-neonatal manifestations included fever 88%, headache 32%, altered consciousness 25%, vomiting 17%, abdominal pain 12%, and convulsions 8%. Among neonates, fetal distress occurred in 75% and prematurity in 50%. | HPO: Headache HP:0002315; Altered consciousness HP:0004372; Vomiting HP:0002013; Abdominal pain HP:0002027; Seizure HP:0001250; Premature birth HP:0001622 | Human retrospective cohort, 2011–2023 | 2024; [10.1007/s40121-024-00986-3](https://doi.org/10.1007/s40121-024-00986-3) (xu2024clinicalcharacteristicsand pages 1-2) |
| Major risk groups | Highest-risk groups are pregnant people and fetuses or neonates, older adults, and people with impaired cell-mediated immunity or major chronic disease. Pregnancy is reported to increase susceptibility about 17-fold; gestational suppression of Th1 and IFN-gamma responses impairs intracellular clearance. | HPO: Immunodeficiency HP:0002721; GO: response to bacterium GO:0009617; interferon-gamma-mediated signaling GO:0060333; CL: macrophage CL:0000235; T cell CL:0000084 | Human and mechanistic review evidence | 2024; [10.3390/microorganisms12102102](https://doi.org/10.3390/microorganisms12102102) (kraus2024listeriainpregnancy—the pages 6-7) |
| Host Mendelian genetics | No Mendelian host gene or pathogenic germline variant is established as the cause of listeriosis. OMIM-style causal-gene, inheritance, penetrance, carrier-frequency, chromosomal-abnormality, and somatic-variant fields are not applicable. Routine human genetic testing is not indicated. | Mendelian causal-gene and ClinVar-variant fields: not applicable | Evidence-gap assessment; susceptibility research is ongoing | Clinical studies include NCT03357536 and NCT02924220; no validated causal variant established |
| Virulence chain: regulation and entry | Host temperature and intracellular glutathione activate PrfA, inducing bacterial virulence genes. Bile resistance supports intestinal survival. InlA–E-cadherin and InlB–MET interactions lead to epithelial adhesion and internalization. | GO: pathogenesis GO:0009405; entry into host cell GO:0030260; CL: intestinal epithelial cell CL:0002563; UBERON: intestine UBERON:0000160; CHEBI: glutathione CHEBI:16856 | Mechanistic review integrating in-vitro and animal evidence | 2023–2024; [10.1128/cmr.00060-19](https://doi.org/10.1128/cmr.00060-19) (kraus2024listeriainpregnancy—the pages 2-4, koopmans2023humanlisteriosis pages 5-7) |
| Virulence chain: intracellular spread | Internalization leads to phagosomal residence; listeriolysin O and phospholipases disrupt the vacuole, resulting in cytosolic escape. Cytosolic replication and ActA-mediated actin polymerization lead to intracellular motility and direct cell-to-cell spread. | GO: escape from host phagosome GO:0046710; actin-filament polymerization GO:0030041; GO-CC: phagocytic vesicle GO:0045335; cytosol GO:0005829; CL: macrophage CL:0000235 | Predominantly in-vitro and model-organism evidence | 2024; [10.3390/microorganisms12102102](https://doi.org/10.3390/microorganisms12102102) (kraus2024listeriainpregnancy—the pages 2-4, kraus2024listeriainpregnancy—the pages 1-2) |
| Barrier and organ disease | Dissemination produces bacteremia and seeding of liver and spleen. Placental invasion may cause fetal infection, miscarriage, stillbirth, preterm birth, or neonatal sepsis; CNS invasion may cause meningitis, meningoencephalitis, rhombencephalitis, or abscess. LIPI-4 in hypervirulent CC4 is associated with maternofetal and neuromeningeal disease, although its mechanism remains unresolved. | UBERON: liver UBERON:0002107; spleen UBERON:0002106; placenta UBERON:0001987; brain UBERON:0000955; meninges UBERON:0000363; CL: trophoblast cell CL:0000351; neuron CL:0000540 | Human association plus model-derived mechanism | 2023–2024; [10.1128/cmr.00060-19](https://doi.org/10.1128/cmr.00060-19), [10.3390/microorganisms12102102](https://doi.org/10.3390/microorganisms12102102) (kraus2024listeriainpregnancy—the pages 6-7, koopmans2023humanlisteriosis pages 5-7) |
| Diagnostics | Definitive diagnosis relies primarily on blood or CSF culture; growth may take about 36 hours. In pregnancy, placental culture was reported as more sensitive than maternal blood culture, 80% versus 55%, and placental-biopsy sensitivity was reported as 100%. WGS and wgMLST support outbreak surveillance rather than host diagnosis. | NCIT: Blood Culture C92225; Lumbar Puncture C15327; Whole Genome Sequencing C101295; UBERON: blood UBERON:0000178; cerebrospinal fluid UBERON:0001359; placenta UBERON:0001987 | Clinical review and surveillance evidence | 2023–2024; [10.1128/cmr.00060-19](https://doi.org/10.1128/cmr.00060-19), [10.3390/microorganisms12102102](https://doi.org/10.3390/microorganisms12102102) (kraus2024listeriainpregnancy—the pages 4-6, kraus2024listeriainpregnancy—the pages 6-7, koopmans2023humanlisteriosis pages 5-7) |
| First-line therapy | First-line treatment is high-dose intravenous ampicillin or amoxicillin, often with short-course gentamicin for severe invasive disease. Adult neurolisteriosis generally requires 12 g/day aminopenicillin for at least 21 days; brain abscess or rhombencephalitis requires at least six weeks with imaging follow-up. Co-trimoxazole is a major beta-lactam-allergy alternative. | CHEBI: ampicillin CHEBI:28971; amoxicillin CHEBI:2676; gentamicin CHEBI:27412; trimethoprim CHEBI:45924; sulfamethoxazole CHEBI:9332; NCIT: Antibiotic Therapy C15614 | Expert review and guideline synthesis; randomized trials lacking | 2023; [10.1128/cmr.00060-19](https://doi.org/10.1128/cmr.00060-19) (koopmans2023humanlisteriosis pages 26-27) |
| Prognosis | A 2024 cohort found fatality of 42% in neonates, 17% in non-neonates, 36% in neurolisteriosis, and 12% in bacteremic disease. CNS involvement, hyperbilirubinemia, and hyponatremia predicted fatality. A separate 63-adult cohort reported 27% in-hospital mortality, ICU admission in 44.4%, residual neurologic deficits in 23.9% of survivors, and brain abscess in 13.0%. | HPO: Neurological deficit HP:0011446; Brain abscess HP:0030049; Hyponatremia HP:0002902; Hyperbilirubinemia HP:0002904; NCIT: Intensive Care C53511 | Human retrospective cohorts | 2024; [10.1007/s40121-024-00986-3](https://doi.org/10.1007/s40121-024-00986-3), [10.1186/s12866-024-03478-z](https://doi.org/10.1186/s12866-024-03478-z) (xu2024clinicalcharacteristicsand pages 1-2) |
| Prevention | No licensed human vaccine or routine asymptomatic screening exists. Prevention includes pasteurization, adequate cooking, reheating or avoiding deli meats and hot dogs, avoiding unpasteurized dairy and high-risk soft cheeses, washing produce, preventing cross-contamination, environmental sanitation, and food-chain WGS surveillance. High-pressure processing at 100–600 MPa can reduce contamination, although surviving cells may recover. | NCIT: Food Safety C17577; Patient Education C16960; Whole Genome Sequencing C101295 | Public-health, surveillance, and food-processing evidence | 2023–2024; [10.1128/cmr.00060-19](https://doi.org/10.1128/cmr.00060-19), [10.3390/foods13010014](https://doi.org/10.3390/foods13010014) (kraus2024listeriainpregnancy—the pages 1-2, kraus2024listeriainpregnancy—the pages 6-7, koopmans2023humanlisteriosis pages 5-7) |
| Veterinary relevance | Natural disease principally affects cattle, sheep, and goats, producing encephalitis or meningoencephalitis, septicemia, abortion, and neonatal loss. Abortions typically occur during the final third of gestation and may affect up to 20% of animals. Ruminants act as reservoirs that contaminate food and farm environments. | NCBI Taxon: cattle 9913; sheep 9940; goat 9925 | Veterinary review and field evidence | 2024; [10.3390/microorganisms12102055](https://doi.org/10.3390/microorganisms12102055) (koncurat2024listeriosischaracteristicsoccurrence pages 1-2, koncurat2024listeriosischaracteristicsoccurrence pages 8-9) |
| Models and functional genomics | Mouse, humanized E-cadherin mouse, gerbil, zebrafish, cultured epithelial and macrophage systems, placental explants, brain slices, and organoids model intracellular infection and barrier crossing. Standard mice incompletely model oral InlA-mediated entry because murine E-cadherin is poorly recognized. A 2024 RECON/Akr1c13-disrupted mouse Tn-seq study identified 135 bacterial fitness genes; deletion of *folD* reduced liver growth by 2.5 log10, while deletion of *alsR* caused 4-log10 liver and 3-log10 spleen attenuation. | CL: macrophage CL:0000235; fibroblast CL:0000057; intestinal epithelial cell CL:0002563; trophoblast cell CL:0000351; UBERON: liver UBERON:0002107; spleen UBERON:0002106 | Animal, ex-vivo, in-vitro, and genome-wide Tn-seq evidence | 2020–2024; [10.1111/cmi.13186](https://doi.org/10.1111/cmi.13186), [10.1128/mbio.01332-24](https://doi.org/10.1128/mbio.01332-24) |


*Table: A concise evidence table summarizing listeriosis identity, phenotypes, risks, pathogenesis, diagnosis, treatment, prognosis, prevention, and comparative biology. It integrates current ontology suggestions with recent human, mechanistic, veterinary, and model-system evidence.*

## 1. Disease information

### Definition and classification

*L. monocytogenes* is ubiquitous in soil, groundwater, animal and human feces, farms, food-processing environments, and refrigerated foods. Its psychrotolerance, acid and salt tolerance, intracellular lifestyle, and biofilm formation explain both food-chain persistence and invasive pathogenicity. It can grow at approximately 0–4°C, survive around pH 4.4–9.6, and tolerate 10–12% salt. (kraus2024listeriainpregnancy—the pages 1-2, koncurat2024listeriosischaracteristicsoccurrence pages 1-2, koopmans2023humanlisteriosis pages 1-3)

**Suggested identifiers**

- **MONDO:** MONDO:0005828.
- **MeSH:** Listeriosis.
- **ICD-10-CM:** A32, with syndrome-specific children such as A32.0 cutaneous listeriosis, A32.1 listerial meningitis/meningoencephalitis, A32.7 listerial sepsis, A32.8 other forms, and A32.9 unspecified. Pregnancy and neonatal coding may additionally require obstetric/perinatal codes.
- **ICD-11:** listeriosis is classified among bacterial infections; exact extension coding should be validated against the current local ICD-11 release.
- **NCBI Taxonomy:** *L. monocytogenes*, Taxon 1639.
- **OMIM/Orphanet:** not primarily applicable: this is an acquired infection rather than a Mendelian disorder. No disease-specific OMIM causal-gene entry should be assigned.

**Synonyms:** listerial infection, *Listeria monocytogenes* infection, invasive listeriosis, non-invasive listerial gastroenteritis, neurolisteriosis, maternal–fetal or perinatal listeriosis, neonatal listeriosis, and historically “circling disease” in ruminants.

Among invasive cases summarized in 2023, bacteremia/septicemia comprised about 52%, CNS infection 31%, and pregnancy-associated/neonatal infection 14%; unusual focal infections were generally each below 1%. Serotypes 4b, 1/2a, and 1/2b account for approximately 92–95% of clinical isolates. (koopmans2023humanlisteriosis pages 1-3)

## 2. Etiology, risk, and protective factors

### Causal factor and transmission

The necessary infectious cause is viable pathogenic *L. monocytogenes*. Infection usually follows ingestion of contaminated ready-to-eat meats, unpasteurized dairy or soft cheeses, prepacked sandwiches, smoked fish, prepared produce, salads, or fruit. Vertical transplacental transmission causes fetal disease; intrapartum or nosocomial neonatal transmission is uncommon but documented. Direct occupational animal exposure is possible, particularly for cutaneous disease. (kraus2024listeriainpregnancy—the pages 1-2, koopmans2023humanlisteriosis pages 1-3)

Pathogen-level risk varies. Four lineages, 13 serotypes, and more than 1,500 sequence types are recognized. LIPI-4 is associated with hypervirulent CC4 and maternal–fetal/neuromeningeal disease; LIPI-3, encoding listeriolysin S, occurs in about 88% of lineage-I strains. CC1, CC2, CC4, and CC6 have been associated with adverse pregnancy outcomes, with CC4 showing notable placental tropism. These are bacterial genomic determinants—not inherited human variants. (kraus2024listeriainpregnancy—the pages 6-7, koopmans2023humanlisteriosis pages 5-7)

### Human risk factors

- Pregnancy, fetus/neonatal age, older age, impaired T-cell immunity, malignancy, transplantation, corticosteroid or other immunosuppressive therapy, cirrhosis, renal disease, diabetes, and other major chronic illness increase invasive risk.
- Pregnancy is reported to confer approximately 17-fold higher susceptibility. The mechanistic explanation is a gestational shift away from Th1/cell-mediated immunity, with reduced IFN-γ-dependent macrophage and cytotoxic-T-cell activity against an intracellular pathogen. (kraus2024listeriainpregnancy—the pages 6-7)
- In one 2024 adult hospital cohort, 88.9% of invasive cases had an immunocompromising condition, illustrating strong enrichment but not population-level relative risk.
- Environmental/behavioral risks include consumption of unheated ready-to-eat foods, unpasteurized milk products, poor refrigerator and kitchen hygiene, cross-contamination, and occupational contact with infected animals or abortion products.

### Genetic, epigenetic, and gene–environment considerations

No human germline mutation, chromosomal abnormality, or somatic variant is established as the cause of ordinary listeriosis. Therefore, ACMG classification, gnomAD allele frequency, penetrance, carrier frequency, inheritance, anticipation, mosaicism, and founder-effect fields are **not applicable**. Human susceptibility is better described as multifactorial immune competence interacting with exposure dose and bacterial genotype. Dedicated studies include NCT02924220, “Genetic Susceptibility and Biomarkers in Listeriosis,” and recruiting NCT03357536, but no validated clinical host-genetic test emerged from the retrieved evidence.

Epigenetic modulation of host susceptibility has been proposed, but no reproducible clinical methylation signature currently diagnoses or predicts listeriosis. Pregnancy-associated immune regulation is clinically important, but should not be represented as a disease-specific inherited epimutation.

### Protective factors

There is no established protective human allele or licensed human vaccine. Protective exposures/behaviors are pasteurization, adequate cooking and reheating, avoiding high-risk refrigerated ready-to-eat foods, washing produce, preventing raw-to-ready-food cross-contamination, maintaining clean processing surfaces, and prompt antimicrobial treatment after invasive disease is suspected. (kraus2024listeriainpregnancy—the pages 1-2, kraus2024listeriainpregnancy—the pages 6-7)

## 3. Phenotypes

Non-invasive illness generally begins within about 24 hours to several days of exposure and is self-limited, with fever, diarrhea, nausea, vomiting, myalgia, and influenza-like symptoms. Invasive disease may appear after roughly 3–70 days, with pregnancy-associated incubation often prolonged. (kraus2024listeriainpregnancy—the pages 4-6)

**Suggested phenotype annotations**

- Febrile gastroenteritis: fever **HP:0001945**, diarrhea **HP:0002014**, nausea **HP:0002018**, vomiting **HP:0002013**, abdominal pain **HP:0002027**. Usually acute, mild–moderate, self-limited in immunocompetent hosts.
- Bacteremia/sepsis: bacteremia and sepsis **HP:0100806**; acute and potentially severe, particularly with comorbidity.
- CNS disease: meningitis **HP:0001287**, encephalitis **HP:0002383**, headache **HP:0002315**, altered consciousness **HP:0004372**, seizure **HP:0001250**, ataxia **HP:0001251**, cranial-nerve dysfunction where present. Disease may rapidly progress to cerebral edema, hydrocephalus, herniation, rhombencephalitis, or abscess.
- Maternal–fetal disease: maternal fever and nonspecific myalgia may coexist with miscarriage **HP:0005268**, stillbirth **HP:0003826**, premature birth **HP:0001622**, fetal distress, neonatal respiratory distress, sepsis, or meningitis.
- Laboratory abnormalities/prognostic correlates: hyponatremia **HP:0002902**, hyperbilirubinemia **HP:0002904**, and hyperuricemia **HP:0002149**.

In a 2024 cohort of 71 confirmed cases, non-neonatal patients had fever in 88%, headache 32%, altered consciousness 25%, vomiting 17%, abdominal pain 12%, and convulsions 8%. Among 12 neonates, fetal distress occurred in 75% and prematurity in 50%. These are hospital-enriched frequencies and should not be generalized to all infected persons. (xu2024clinicalcharacteristicsand pages 1-2)

Quality-of-life studies using EQ-5D, SF-36, or PROMIS were not identified. Nevertheless, ICU admission, cognitive or focal neurologic deficit, seizures, hearing/cranial-nerve dysfunction, and abscess can impair independence and long-term neurodevelopment. In a recent adult cohort, 23.9% of discharged survivors had residual neurologic deficits and 13.0% had brain abscess, demonstrating substantial functional burden.

## 4. Genetic and molecular information

### Distinguishing host from pathogen genetics

There are **no human causal genes** for listeriosis in the Mendelian-disease sense. Routine WES, WGS, gene panels, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not diagnostic for the infection.

The relevant genetic determinants are predominantly bacterial:

- **prfA:** master transcriptional activator of virulence genes.
- **gshF:** synthesizes bacterial glutathione that stabilizes active PrfA.
- **inlA/inlB:** encode internalins mediating receptor-dependent host-cell entry.
- **hly:** encodes listeriolysin O, enabling phagosomal escape.
- **plcA/plcB:** phospholipases supporting vacuolar disruption and spread.
- **actA:** recruits host actin machinery for cytosolic motility and cell-to-cell dissemination.
- **inlC:** interferes with NF-κB-related responses and junctional architecture.
- **inlP:** contributes to placental tropism in experimental systems.
- **LIPI-3/lls:** listeriolysin-S locus, enriched in lineage I.
- **LIPI-4:** CC4-associated hypervirulence locus; mechanism remains unresolved.

Below 30°C an RNA thermoswitch suppresses *prfA* translation; within a warm host, glutathione activates PrfA. Naturally occurring loss-of-function changes in *prfA* or *gshF* occur in approximately 0.1% of isolates and may abolish virulence. (koopmans2023humanlisteriosis pages 5-7)

The 2024 complete genome of attenuated veterinary vaccine strain AUF identified polymorphisms/pseudogenes affecting motility, stress survival, biofilm and virulence-regulatory functions. Because its wild parental strain was unavailable, UV-induced attenuation remains a plausible but not definitive explanation. (feodorova2024completegenomeof pages 11-12)

## 5. Environmental information

*L. monocytogenes* behaves as an environmental saprophyte and intracellular pathogen. Relevant reservoirs include soil, water, silage, feces, livestock, wildlife, drains, refrigeration units, and food-processing equipment. Biofilms increase resistance to desiccation and sanitation and permit recurring contamination. In one summarized isolate set, 3.5% were strong and 38.5% moderate biofilm producers. (koncurat2024listeriosischaracteristicsoccurrence pages 1-2)

Diet is the dominant modifiable lifestyle factor. Smoking, exercise, and alcohol are not established direct causes, although alcohol-related liver disease may increase host susceptibility. Conventional “toxins,” ionizing radiation, or pollution are not recognized primary causes. The infectious agent is *L. monocytogenes*; *L. ivanovii* is mainly a ruminant pathogen and only rarely causes human infection. (koopmans2023humanlisteriosis pages 1-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Ingestion of contaminated food leads to** survival of *L. monocytogenes* through gastric, bile, cold, osmotic, and acid stresses.
2. **Intestinal contact leads to** InlA–E-cadherin and InlB–MET-dependent adhesion/internalization, together with alternative uptake by phagocytes and LAP–HSP60-associated junctional remodeling demonstrated chiefly in cell and animal models. (kraus2024listeriainpregnancy—the pages 2-4)
3. **Internalization leads to** residence in a primary vacuole/phagosome.
4. **Acidification and PrfA-regulated expression lead to** LLO- and PlcA/PlcB-mediated membrane damage, resulting in cytosolic escape before lysosomal killing.
5. **Cytosolic access leads to** bacterial replication and innate sensing, while bacterial InlC and related effectors partially suppress NF-κB signaling and neutrophil recruitment. (kraus2024listeriainpregnancy—the pages 4-6)
6. **ActA-mediated actin polymerization leads to** actin-comet motility, membrane protrusions, uptake by adjacent cells, and direct cell-to-cell dissemination that reduces extracellular exposure. (kraus2024listeriainpregnancy—the pages 2-4)
7. **Local spread leads to** mesenteric/hematogenous dissemination, with early hepatic and splenic capture by macrophages/Kupffer cells and systemic bacteremia when cellular immunity is insufficient.
8. **Bacteremia branches:**
   - **Placental/trophoblast invasion leads to** placentitis, fetal infection, miscarriage, stillbirth, preterm birth, neonatal sepsis, or meningitis. Internalins and hypervirulent CC4/LIPI-4 are associated with this branch, but parts of the barrier-crossing mechanism remain model-derived or unresolved. (kraus2024listeriainpregnancy—the pages 6-7, koopmans2023humanlisteriosis pages 5-7)
   - **Blood–brain-barrier/choroid-plexus invasion leads to** meningitis, meningoencephalitis, rhombencephalitis, edema, hydrocephalus, herniation, or brain abscess.
   - **Other tissue seeding leads to** rare endocardial, osteoarticular, ocular, cutaneous, or intra-abdominal disease.
9. **IL-12/IFN-γ-driven macrophage activation, NK responses, and antigen-specific CD8/CD4 T-cell immunity lead to** clearance in most immunocompetent hosts; age, pregnancy-associated Th1 attenuation, immunosuppression, and comorbidity lead to failed containment and severe disease.
10. **Bacterial replication plus host inflammatory injury leads to** sepsis, neuronal/tissue injury, fetal compromise, organ dysfunction, and death.

### Pathways, cells, compartments, and ontology suggestions

- **GO biological process:** pathogenesis GO:0009405; entry into host cell GO:0030260; escape from host phagosome GO:0046710; actin-filament polymerization GO:0030041; response to bacterium GO:0009617; inflammatory response GO:0006954; IFN-γ-mediated signaling GO:0060333; phagocytosis GO:0006909.
- **Cell Ontology:** intestinal epithelial cell CL:0002563; macrophage CL:0000235; Kupffer cell CL:0000091; neutrophil CL:0000775; dendritic cell CL:0000451; NK cell CL:0000623; T cell CL:0000084; trophoblast CL:0000351; neuron CL:0000540; endothelial cell CL:0000115.
- **GO cellular component:** phagocytic vesicle GO:0045335; cytosol GO:0005829; plasma membrane GO:0005886; actin cytoskeleton GO:0015629.
- **Metabolic regulation:** bacterial glutathione (**CHEBI:16856**) activates PrfA; bile resistance enables intestinal survival. A 2024 in-vivo Tn-seq study identified 135 bacterial fitness genes. *folD* deletion reduced liver growth by 2.5 log10 and impaired cell-to-cell spread; *alsR* deletion attenuated liver and spleen burdens by 4 and 3 log10, respectively, demonstrating organ-specific folate and D-allose metabolic requirements.

No validated clinical transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-transcriptomic biomarker is currently used. WGS/wgMLST is the mature omics implementation for isolate typing, virulence profiling, and outbreak detection. (koopmans2023humanlisteriosis pages 5-7, sousa2024currentmethodologiesavailable pages 18-18)

## 7. Anatomical structures affected

- **Primary portal:** gastrointestinal lumen and intestinal epithelium—**UBERON:0000160**.
- **Reticuloendothelial dissemination:** liver **UBERON:0002107**, spleen **UBERON:0002106**, blood **UBERON:0000178**.
- **Nervous system:** meninges **UBERON:0000363**, brain **UBERON:0000955**, brainstem, and CSF **UBERON:0001359**.
- **Pregnancy:** placenta **UBERON:0001987**, decidua, trophoblast, amniotic fluid, fetus.
- **Secondary/rare:** heart valves, bone/joints, skin, eye, peritoneum, and implanted devices.

At the tissue level, epithelial, endothelial, placental, mononuclear-phagocyte, and nervous tissues are involved. At the subcellular level, the plasma membrane, endocytic/phagocytic vacuole, cytosol, and actin cytoskeleton are central. Lateralization is not characteristic, although focal brainstem or abscess lesions may be asymmetric.

## 8. Temporal development

Non-invasive gastroenteritis is acute, usually beginning within hours to several days and resolving spontaneously. Invasive disease is acute or subacute after an incubation reported up to approximately 70 days. Pregnancy-associated infection may be mild in the mother yet evolve rapidly toward fetal compromise. (kraus2024listeriainpregnancy—the pages 4-6)

A practical staging concept is: exposure/intestinal colonization → febrile gastroenteritis or asymptomatic phase → bacteremia → CNS, placental, or other focal invasion → complications/recovery/death. This is a mechanistic clinical framework, not an official staging system.

Critical intervention windows include immediate blood cultures and empiric active therapy when a high-risk patient has compatible sepsis/CNS disease, and urgent obstetric evaluation for unexplained fever in pregnancy. Neurolisteriosis and neonatal disease can progress over hours to days; abscess disease requires prolonged therapy and serial imaging. Relapse is uncommon after adequate treatment but may occur with an uncontrolled focus or profound immunosuppression.

## 9. Inheritance and population epidemiology

Listeriosis is acquired and **not inherited**. Mendelian inheritance, penetrance, expressivity, anticipation, germline mosaicism, founder mutation, consanguinity, and carrier-frequency fields are not applicable.

Reported incidence varies by surveillance system and population. Recent reviews cite approximately 0.1–1.5 cases/100,000/year globally, while another synthesis gives 0.1–11.3 per million/year. For 2010, the estimated worldwide burden was 23,150 cases, 5,463 deaths, and 172,823 DALYs. Neonatal incidence was summarized as about 3–6/100,000 live births in the United States and 2–8/100,000 in Europe. (kraus2024listeriainpregnancy—the pages 4-6, koopmans2023humanlisteriosis pages 1-3, koopmans2023humanlisteriosis pages 5-7)

The disease occurs worldwide wherever refrigerated ready-to-eat food systems and surveillance exist; rates vary geographically with age structure, food practices, outbreaks, and ascertainment. Older adults and immunocompromised persons dominate non-pregnancy invasive cases. A 2024 adult cohort was 57.1% male with a mean/median reported age around 59 years, but this single-center distribution is not a universal sex ratio.

## 10. Diagnostics

### Clinical and microbiological diagnosis

Definitive diagnosis requires isolation of *L. monocytogenes* from a normally sterile site: blood, CSF, placenta, amniotic fluid, fetal tissue, joint fluid, or abscess. Culture commonly takes about 36 hours. In pregnancy, placental culture was reported as 80% sensitive versus 55% for maternal blood culture, and placental-biopsy sensitivity as 100%; these figures come from summarized studies and require local validation. Laboratories should not dismiss Gram-positive rods as “diphtheroids” when the syndrome fits. (kraus2024listeriainpregnancy—the pages 4-6, kraus2024listeriainpregnancy—the pages 6-7)

For suspected neurolisteriosis, perform blood cultures and lumbar puncture unless contraindicated. CSF generally shows bacterial meningitis—pleocytosis, elevated protein, and reduced glucose—but Gram stain can be insensitive. MRI is preferred for rhombencephalitis, abscess, cranial-nerve, or persistent focal findings; CT is useful urgently for mass effect/hydrocephalus. Placental histology may show microabscesses/inflammation, but culture establishes etiology.

Stool culture is not recommended to diagnose invasive listeriosis or screen asymptomatic exposed people because carriage can be transient and a negative result does not exclude systemic disease. Serology lacks adequate clinical utility. Isolate WGS/wgMLST supports outbreak linkage and surveillance, not rapid bedside exclusion. (koopmans2023humanlisteriosis pages 5-7)

### Differential diagnosis

- Gastroenteritis: *Salmonella*, *Campylobacter*, Shiga-toxin-producing *E. coli*, norovirus, and other foodborne illness.
- Sepsis/meningitis: *Streptococcus pneumoniae*, *Neisseria meningitidis*, group-B streptococcus, enteric Gram-negative bacilli, HSV encephalitis, tuberculosis, fungal meningitis, and brain abscess pathogens.
- Rhombencephalitis: HSV, enterovirus, tuberculosis, autoimmune/demyelinating brainstem disease, stroke, or neoplasm.
- Pregnancy fever/fetal compromise: pyelonephritis, influenza/COVID-19, chorioamnionitis from other bacteria, toxoplasmosis, syphilis, CMV, and placental abruption.

A critical therapeutic clue is that routine third-generation cephalosporin meningitis regimens do not reliably cover *Listeria*; an aminopenicillin is required when age or immune status creates risk.

### Genetic/omics testing and screening

Human WES/WGS, gene panels, CMA, karyotype, FISH, mtDNA, and repeat testing have no routine role. Bacterial WGS is valuable for public-health surveillance and resistance/virulence characterization. There is no newborn, carrier, cascade, prenatal-genetic, or general-population screening program for listeriosis.

## 11. Outcome and prognosis

Listeriosis has no meaningful 5- or 10-year “survival rate”; acute case fatality and neurologic/obstetric outcomes are the appropriate measures.

In the 2024 Xi’an cohort, fatality was 42% in neonates versus 17% in non-neonates and 36% in neurolisteriosis versus 12% in bacteremia. CNS involvement, hyperbilirubinemia, and hyponatremia predicted fatality; hyperuricemia added risk among non-neonates. Of 23 maternal cases, only two had uneventful obstetric outcomes despite no maternal deaths. (xu2024clinicalcharacteristicsand pages 1-2)

A separate 63-adult retrospective cohort reported 27.0% in-hospital mortality, 44.4% ICU admission, residual neurologic deficits in 23.9% of discharged survivors, and brain abscess in 13.0%. Thus, surviving uncomplicated gastroenteritis generally recover fully, whereas neonatal and CNS disease can cause death, developmental impairment, seizures, cognitive deficits, or other lasting disability.

Early gestational infection has especially poor fetal prognosis. Reviews report miscarriage in approximately 65% of first-trimester infections versus 26% diagnosed later; each additional gestational week at infection was associated with improved fetal survival in one summarized analysis. These estimates are vulnerable to referral and publication bias. (kraus2024listeriainpregnancy—the pages 6-7, koncurat2024listeriosischaracteristicsoccurrence pages 8-9)

## 12. Treatment

### Pharmacotherapy and strategy

Treatment evidence is based largely on microbiology, observational series, animal data, and expert consensus; randomized comparative trials are lacking.

- **Adult neurolisteriosis:** intravenous ampicillin or amoxicillin totaling about 12 g/day for at least 21 days. Consider short-course gentamicin in severe disease, balancing uncertain incremental benefit against nephrotoxicity/ototoxicity.
- **Brain abscess or rhombencephalitis:** active β-lactam for at least six weeks, individualized with serial MRI/CT.
- **Bacteremia without deep focus:** aminopenicillin-based therapy, commonly about two weeks after clinical response and culture clearance, longer when immunosuppression or focal infection persists.
- **Pregnancy:** IV ampicillin/amoxicillin 6–12 g/day; one French approach uses amoxicillin 100 mg/kg/day for two weeks or until delivery, with gentamicin 5 mg/kg/day for 3–5 days in selected severe cases.
- **Neonatal early-onset disease:** parenteral ampicillin/amoxicillin 100–300 mg/kg/day for 14 days; days 8–28 or meningitis generally require 21 days. Gentamicin, e.g. 2 mg/kg for seven days in the cited synthesis, may be added according to neonatal guidance and renal monitoring.
- **β-lactam allergy/intolerance:** trimethoprim–sulfamethoxazole is the best-established alternative. Meropenem, linezolid, rifampicin-containing combinations, moxifloxacin, fosfomycin, or chloramphenicol may be considered with specialist input, but superiority is unproven. (koopmans2023humanlisteriosis pages 26-27)

**CHEBI suggestions:** ampicillin CHEBI:28971; amoxicillin CHEBI:2676; gentamicin CHEBI:27412; trimethoprim CHEBI:45924; sulfamethoxazole CHEBI:9332. **NCIT suggestions:** Antibiotic Therapy C15614; Intravenous Route of Administration C38276; Intensive Care C53511; Physical Therapy C15360 and rehabilitation terms for neurologic sequelae.

Supportive care includes sepsis management, airway/ventilation, seizure control, intracranial-pressure management, obstetric/fetal monitoring, neonatal intensive care, nutrition, and neurologic/physical/occupational/speech rehabilitation. Drainage or surgery is reserved for selected abscesses, infected prostheses, endocarditis, or other source-control needs.

Recent isolates remain broadly susceptible to aminopenicillins. The 2024 Xi’an cohort found only two ampicillin-resistant and one penicillin-resistant isolate; a 63-case Hungarian cohort reported 100% in-vitro susceptibility to ampicillin and meropenem, 97.7% to trimethoprim–sulfamethoxazole, and 86.0% to gentamicin. Multidrug-resistant strains nevertheless occur, supporting isolate-level susceptibility testing. (xu2024clinicalcharacteristicsand pages 1-2, koopmans2023humanlisteriosis pages 26-27, koncurat2024listeriosischaracteristicsoccurrence pages 8-9)

No approved gene, cell, RNA, checkpoint, or precision-genotype therapy treats listeriosis. Attenuated *Listeria* vectors under study for cancer immunotherapy are conceptually distinct and should not be represented as listeriosis treatment.

## 13. Prevention

### Primary prevention

No licensed human vaccine exists. High-risk persons should avoid unpasteurized milk/dairy, refrigerated pâté or meat spreads, unheated deli meats/hot dogs, refrigerated smoked seafood unless cooked, and high-risk soft cheeses unless made from pasteurized milk under controlled production. Reheat ready-to-eat meats until steaming, wash produce, separate raw from cooked foods, clean refrigerators and preparation surfaces, and observe storage limits. (kraus2024listeriainpregnancy—the pages 6-7)

Food-industry measures include hazard analysis, environmental sampling, sanitation of drains/equipment, temperature and shelf-life control, pasteurization/cooking, product recall, and WGS-based surveillance linking clinical, food, and environmental isolates. High-pressure processing at approximately 100–600 MPa can reduce *L. monocytogenes* below detection in some foods, although sublethally injured cells may recover, so it complements rather than replaces validated controls.

### Secondary and tertiary prevention

There is no routine asymptomatic stool, blood, prenatal, or population screening. Risk stratification is clinical: pregnancy, advanced age, immunosuppression, and major comorbidity should lower the threshold for evaluation after compatible illness or outbreak exposure. Secondary prevention is prompt culture and active aminopenicillin therapy. Tertiary prevention comprises source control, adequate treatment duration, repeat cultures where indicated, CNS imaging, fetal/neonatal monitoring, and rehabilitation.

Routine antibiotic prophylaxis for an asymptomatic person who ate a recalled product is generally unsupported; clinical evaluation is appropriate if fever or invasive symptoms arise, particularly during pregnancy or immunosuppression.

## 14. Other species and natural disease

Natural listeriosis occurs across mammals, birds, wildlife, aquatic animals, and invertebrates; one review noted isolation across 42 mammalian and 29 avian species. Cattle (**NCBI Taxon 9913**), sheep (**9940**), and goats (**9925**) are particularly important. Ruminant disease includes encephalitis/meningoencephalitis (“circling”), septicemia, abortion, stillbirth, and neonatal loss. Abortions usually occur in the last gestational third and may affect up to 20% of a herd/flock during outbreaks. Ruminants can shed organisms and contaminate silage, milk, meat, soil, and processing environments, creating a One Health bridge to human exposure. (koncurat2024listeriosischaracteristicsoccurrence pages 1-2, koncurat2024listeriosischaracteristicsoccurrence pages 8-9)

*L. ivanovii* is primarily pathogenic in ruminants; *L. innocua* is usually nonpathogenic but virulent isolates exist. A 2024 study recovered *L. monocytogenes*, *L. innocua*, and *L. ivanovii* from stranded Mediterranean sea turtles, with little difference in virulence-gene distribution between some turtle and human strains, illustrating wildlife/environmental circulation rather than proving frequent turtle-to-human transmission. (renzo2024genomiccharacterizationof pages 14-15)

Breed-specific VBO associations and orthologous host “disease genes” are not applicable because natural disease is infectious rather than a breed-linked monogenic trait. An attenuated AUF *L. monocytogenes* live veterinary vaccine has been used in some settings since the 1960s; its 2,942,932-bp genome contains more than 2,800 coding sequences, 17 pseudogenes, five annotated resistance genes, and 56/92 surveyed virulence genes. This does not constitute a licensed human vaccine. (feodorova2024completegenomeof pages 11-12)

## 15. Model organisms and advanced experimental systems

- **Conventional mouse:** foundational for systemic infection, innate/adaptive immunity, hepatic/splenic colonization, bacterial mutants, and vaccine-vector work. Limitation: murine E-cadherin is poorly recognized by InlA, so ordinary mice incompletely model human oral invasion and placental tropism.
- **Humanized E-cadherin knock-in mouse:** improves InlA-dependent intestinal entry but does not eliminate all interspecies placental and immune differences.
- **Gerbil/guinea pig:** receptors and reproductive anatomy can better reproduce selected intestinal or maternal–fetal steps; fewer genetic tools are available.
- **Zebrafish larvae:** permit live imaging of phagocyte–pathogen interactions; temperature and anatomy limit direct clinical translation.
- **Invertebrates, including *Galleria mellonella*:** inexpensive virulence screening but lack mammalian adaptive immunity and relevant barriers.
- **Cell culture:** Caco-2 epithelial cells, macrophage lines such as RAW264.7, fibroblasts, endothelial cells, and trophoblasts dissect adhesion, invasion, escape, actin motility, and cytotoxicity.
- **Ex-vivo and organotypic systems:** placental explants, intestinal organoids, blood–brain-barrier cultures, and brain slices offer human tissue relevance but lack full circulation and systemic immunity.

A 2024 RECON/*Akr1c13*-disrupted mouse enabled high-dose in-vivo Tn-seq and identified 135 pathogen fitness genes, including organ-specific *folD* and *alsR* phenotypes. This exemplifies current functional genomics: it discovers bacterial dependencies but does not itself establish human treatment targets.

## Recent developments and expert interpretation, 2023–2024

1. The 2023 *Clinical Microbiology Reviews* synthesis consolidated modern clinical, genomic, and mechanistic understanding and emphasized that cross-border WGS data sharing improves outbreak-source identification. (koopmans2023humanlisteriosis pages 1-3, koopmans2023humanlisteriosis pages 5-7)
2. Two 2024 hospital cohorts quantified persistently high mortality and neurologic sequelae despite aminopenicillin susceptibility, indicating that delayed recognition, CNS invasion, age, and host illness—not antimicrobial resistance alone—drive outcomes. (xu2024clinicalcharacteristicsand pages 1-2)
3. Current pathogen-genomics work is moving from lineage description toward WGS/machine-learning virulence prediction, but genotype alone cannot yet replace phenotypic or epidemiologic assessment. Some nominally nonpathogenic isolates invade cultured cells despite lacking major LIPI loci. (sousa2024currentmethodologiesavailable pages 18-18)
4. In-vivo Tn-seq has exposed organ-specific metabolic requirements, while complete sequencing of long-used attenuated veterinary strains offers rational starting points for vaccine-vector safety assessment. (feodorova2024completegenomeof pages 11-12)
5. The expert consensus remains that prevention and early empiric aminopenicillin coverage in the correct risk groups have greater immediate clinical value than experimental host-genetic or omics biomarkers.

## Selected exact source quotations

- Koopmans et al., published March 2023: “*Clinically, listerial disease, or listeriosis, most often presents as bacteremia, meningitis or meningoencephalitis, and pregnancy-associated infections manifesting as miscarriage or neonatal sepsis*.” DOI: https://doi.org/10.1128/cmr.00060-19. (koopmans2023humanlisteriosis pages 1-3)
- Xu et al., published May 2024: “*Early administration of ampicillin- or penicillin-based therapy might be beneficial for recovery of listeriosis*.” DOI: https://doi.org/10.1007/s40121-024-00986-3. (xu2024clinicalcharacteristicsand pages 1-2)
- Feodorova et al., published June 2024, described AUF as an attenuated strain “*successfully used since the 1960s as a live whole-cell veterinary vaccine*.” DOI: https://doi.org/10.1038/s41597-024-03440-8. (feodorova2024completegenomeof pages 11-12)

## Knowledge-base caveats

Frequencies from tertiary-hospital cohorts overrepresent severe disease. Associations between clonal complexes and clinical syndromes are pathogen-level epidemiologic associations, not deterministic patient biomarkers. Most detailed barrier-crossing and intracellular mechanisms derive from in-vitro, organoid, or animal experiments; they are biologically compelling but should be labeled model-derived where direct human demonstration is unavailable. Human causal-variant, chromosomal, pharmacogenomic, validated omics-biomarker, licensed-vaccine, and population-screening fields should presently be recorded as **not established/not applicable**, rather than filled by analogy.

References

1. (koopmans2023humanlisteriosis pages 1-3): Merel M. Koopmans, Matthijs C. Brouwer, José A. Vázquez-Boland, and Diederik van de Beek. Human listeriosis. Clinical Microbiology Reviews, Mar 2023. URL: https://doi.org/10.1128/cmr.00060-19, doi:10.1128/cmr.00060-19. This article has 374 citations and is from a highest quality peer-reviewed journal.

2. (xu2024clinicalcharacteristicsand pages 1-2): Wen Xu, Mei-Juan Peng, Lin-Shan Lu, Zhen-Jun Guo, A-Min Li, Jing Li, Yan Cheng, Jia-Yu Li, Yi-Jun Li, Jian-Qi Lian, Yu Li, Yang Sun, Wei-Lu Zhang, and Ye Zhang. Clinical characteristics and fatality risk factors for patients with listeria monocytogenes infection: a 12-year hospital-based study in xi’an, china. Infectious Diseases and Therapy, 13:1359-1378, May 2024. URL: https://doi.org/10.1007/s40121-024-00986-3, doi:10.1007/s40121-024-00986-3. This article has 10 citations and is from a peer-reviewed journal.

3. (kraus2024listeriainpregnancy—the pages 6-7): Vladimír Kraus, Beáta Čižmárová, and Anna Birková. Listeria in pregnancy—the forgotten culprit. Microorganisms, 12(10):2102, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102102, doi:10.3390/microorganisms12102102. This article has 29 citations.

4. (kraus2024listeriainpregnancy—the pages 2-4): Vladimír Kraus, Beáta Čižmárová, and Anna Birková. Listeria in pregnancy—the forgotten culprit. Microorganisms, 12(10):2102, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102102, doi:10.3390/microorganisms12102102. This article has 29 citations.

5. (koopmans2023humanlisteriosis pages 5-7): Merel M. Koopmans, Matthijs C. Brouwer, José A. Vázquez-Boland, and Diederik van de Beek. Human listeriosis. Clinical Microbiology Reviews, Mar 2023. URL: https://doi.org/10.1128/cmr.00060-19, doi:10.1128/cmr.00060-19. This article has 374 citations and is from a highest quality peer-reviewed journal.

6. (kraus2024listeriainpregnancy—the pages 1-2): Vladimír Kraus, Beáta Čižmárová, and Anna Birková. Listeria in pregnancy—the forgotten culprit. Microorganisms, 12(10):2102, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102102, doi:10.3390/microorganisms12102102. This article has 29 citations.

7. (kraus2024listeriainpregnancy—the pages 4-6): Vladimír Kraus, Beáta Čižmárová, and Anna Birková. Listeria in pregnancy—the forgotten culprit. Microorganisms, 12(10):2102, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102102, doi:10.3390/microorganisms12102102. This article has 29 citations.

8. (koopmans2023humanlisteriosis pages 26-27): Merel M. Koopmans, Matthijs C. Brouwer, José A. Vázquez-Boland, and Diederik van de Beek. Human listeriosis. Clinical Microbiology Reviews, Mar 2023. URL: https://doi.org/10.1128/cmr.00060-19, doi:10.1128/cmr.00060-19. This article has 374 citations and is from a highest quality peer-reviewed journal.

9. (koncurat2024listeriosischaracteristicsoccurrence pages 1-2): Ana Končurat and Tomislav Sukalić. Listeriosis: characteristics, occurrence in domestic animals, public health significance, surveillance and control. Oct 2024. URL: https://doi.org/10.3390/microorganisms12102055, doi:10.3390/microorganisms12102055. This article has 30 citations.

10. (koncurat2024listeriosischaracteristicsoccurrence pages 8-9): Ana Končurat and Tomislav Sukalić. Listeriosis: characteristics, occurrence in domestic animals, public health significance, surveillance and control. Oct 2024. URL: https://doi.org/10.3390/microorganisms12102055, doi:10.3390/microorganisms12102055. This article has 30 citations.

11. (feodorova2024completegenomeof pages 11-12): Valentina A. Feodorova, Sergey S. Zaitsev, Mariya A. Khizhnyakova, Maxim S. Lavrukhin, Yury V. Saltykov, Alexey D. Zaberezhny, and Olga S. Larionova. Complete genome of the listeria monocytogenes strain auf, used as a live listeriosis veterinary vaccine. Scientific Data, Jun 2024. URL: https://doi.org/10.1038/s41597-024-03440-8, doi:10.1038/s41597-024-03440-8. This article has 6 citations and is from a peer-reviewed journal.

12. (sousa2024currentmethodologiesavailable pages 18-18): Mariana Sousa, Rui Magalhães, Vânia Ferreira, and Paula Teixeira. Current methodologies available to evaluate the virulence potential among listeria monocytogenes clonal complexes. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1425437, doi:10.3389/fmicb.2024.1425437. This article has 8 citations and is from a peer-reviewed journal.

13. (renzo2024genomiccharacterizationof pages 14-15): Ludovica Di Renzo, Maria Elisabetta De Angelis, Marina Torresi, Giulia Mariani, Federica Pizzurro, Luana Fiorella Mincarelli, Emanuele Esposito, Maria Oliviero, Doriana Iaccarino, Fabio Di Nocera, Gianluigi Paduano, Giuseppe Lucifora, Cesare Cammà, Nicola Ferri, and Francesco Pomilio. Genomic characterization of listeria monocytogenes and other listeria species isolated from sea turtles. Apr 2024. URL: https://doi.org/10.3390/microorganisms12040817, doi:10.3390/microorganisms12040817. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](Listeriosis-deep-research-falcon_artifacts/artifact-00.md)