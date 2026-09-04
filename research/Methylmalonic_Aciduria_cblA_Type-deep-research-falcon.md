---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T10:10:02.278904'
end_time: '2026-08-31T10:25:04.238337'
duration_seconds: 901.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Methylmalonic Aciduria, cblA Type
  mondo_id: MONDO:0009613
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Methylmalonic_Aciduria_cblA_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methylmalonic Aciduria, cblA Type
- **MONDO ID:** MONDO:0009613 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Methylmalonic Aciduria, cblA Type** covering all of the
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
- **Disease Name:** Methylmalonic Aciduria, cblA Type
- **MONDO ID:** MONDO:0009613 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Methylmalonic Aciduria, cblA Type** covering all of the
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


# Comprehensive research report: Methylmalonic aciduria, cblA type

## Executive summary and scope

Methylmalonic aciduria, cblA type is an autosomal-recessive, usually hydroxocobalamin-responsive form of **isolated methylmalonic acidemia/aciduria** caused by biallelic pathogenic variants in **MMAA**. A critical nomenclature point is that **MMAA causes cblA**, whereas **MMAB causes cblB**; the latter should not be assigned to MONDO:0009613. The best subtype-specific natural-history evidence is a multinational registry cohort of 28 cblA patients. It found 27/28 to be cobalamin responsive, relatively preserved neurologic and renal function, and survival of all 28 during observation. Nevertheless, neonatal metabolic crises, severe acidosis, and hyperammonemia can occur, so early diagnosis and sustained parenteral hydroxocobalamin remain important. (horster2021delineatingtheclinical pages 1-2, brennerova2021genetictestingis pages 1-2)

The compact knowledge-base summary below precedes the detailed report.

| Topic | Compact knowledge-base entry |
|---|---|
| Identity | **Methylmalonic aciduria, cblA type** is an **isolated methylmalonic aciduria/acidemia** due to defective intracellular cobalamin handling for mitochondrial methylmalonyl-CoA mutase function. **Important correction:** **MMAA causes cblA**, whereas **MMAB causes cblB**. Suggested ontology: **MONDO:0009613**; **Orphanet:79310**; HPO parent phenotype **Methylmalonic aciduria** HP:0012120. Evidence is from **aggregated disease resources and patient cohorts**, not EHR-only datasets. (OpenTargets Search: methylmalonic aciduria cblA type-MMAB, horster2021delineatingtheclinical pages 1-2, brennerova2021genetictestingis pages 1-2) |
| Causal gene | **MMAA** (methylmalonic aciduria type A gene); disease is caused by **biallelic germline pathogenic variants** in **MMAA**, located on **chromosome 4q31.21**. Common reported cblA alleles in the 28-patient registry study were **c.433C>T (p.Arg145\*)** and **c.592_595delACTG (p.Thr198Serfs\*6)**; four novel variants were also reported there. **MMAB is not the cblA gene**. Suggested gene/protein annotation: GO process terms related to **cobalamin cofactor metabolic process** and **methylmalonyl-CoA mutase activity regulation** may be used cautiously. (horster2021delineatingtheclinical pages 1-2, horster2021delineatingtheclinical pages 2-4, abdrabo2019nextgenerationsequencing pages 31-37) |
| Inheritance | **Autosomal recessive**. No convincing evidence retrieved here for somatic causation, chromosomal abnormalities, anticipation, or established modifier genes specific to cblA. Variable expressivity is supported clinically; penetrance was not quantified in the retrieved cblA-specific sources. (horster2021delineatingtheclinical pages 1-2, brennerova2021genetictestingis pages 1-2) |
| Mechanism | MMAA encodes a **mitochondrial G3E-family P-loop GTPase** that interacts with **MMUT** and helps **protect, load/gate, and reactivate adenosylcobalamin (AdoCbl)-dependent mutase function**. Loss of MMAA function impairs effective AdoCbl handling for MMUT, reducing conversion of **methylmalonyl-CoA to succinyl-CoA**, which leads to accumulation of **methylmalonic acid** and related toxic metabolites. Demonstrated components: MMAA/MMUT interaction, GTP-dependent protectase/reactivase roles, and variant-associated protein instability for some alleles; downstream organ injury is supported clinically but remains partly inferred mechanistically. Suggested ontology: GO **mitochondrial matrix**; UBERON **mitochondrion** not applicable—use GO CC for subcellular annotation. (takahashiiniguez2012roleofvitamin pages 11-12, froese2009geneticsandbiochemistry pages 32-37, brennerova2021genetictestingis pages 1-2) |
| Biochemical signature | Hallmark findings are **marked methylmalonic acid elevation** in urine/plasma, often with **elevated propionylcarnitine (C3)** and **methylcitrate**; **homocysteine is typically not elevated** in isolated MMA/cblA, helping distinguish cblA from proximal cobalamin/remethylation disorders. During crises, patients may develop **metabolic acidosis**, **secondary hyperammonemia**, and low free carnitine. Suggested HPO/lab terms: **Metabolic acidosis**, **Hyperammonemia**, **Increased urinary methylmalonic acid**. (forny2021guidelinesforthe pages 6-8, brennerova2021genetictestingis pages 1-2, schnabel2023combinednewbornscreening pages 10-11) |
| Onset | Often **neonatal or early infancy**, but variable. In the cblA registry subset with symptomatic data, **metabolic crisis** was the leading presentation; among 21 cblA patients, **43%** had first crisis in the **neonatal period**, **33%** after the neonatal period, and **24%** had **no metabolic crisis**; median age at first symptoms was **24.5 days**. Suggested HPO: **Infantile onset** / **Neonatal onset** where appropriate. (horster2021delineatingtheclinical pages 6-7, horster2021delineatingtheclinical pages 5-6) |
| Major cblA cohort statistics | In the European registry study, **28 cblA** patients were analyzed. **27/28** had reported cobalamin responsiveness. Among symptomatic cblA patients, **16/21 (76%)** presented with metabolic crisis. Neurologic/functional outcomes were relatively favorable: **0/27 seizures**, **1/27 (4%) movement disorder**, **14/18 (78%)** attended regular school. Renal outcomes were substantially milder than mut disease: chronic renal failure in about **2/23 (9%)**; **1/22 (5%)** had arterial hypertension. Nutritional support burden was lower: **1/27 PEG**, **3/27 NG feeding**. **All 28 cblA patients survived** during the study interval. (horster2021delineatingtheclinical pages 1-2, horster2021delineatingtheclinical pages 15-17, horster2021delineatingtheclinical pages 17-19) |
| Diagnosis | Diagnostic workflow: newborn screening or symptomatic workup showing **elevated C3/C3:C2**, then confirmation with **urine organic acids** and/or **plasma/DBS methylmalonic acid ± methylcitrate**, while checking that **homocysteine is not elevated** for isolated MMA. Definitive subtype assignment requires **molecular testing of MMAA** (single gene, panel, WES/WGS depending context). A standardized **hydroxocobalamin responsiveness test** is recommended in MMA: baseline MMA measurement, **1 mg intramuscular hydroxocobalamin on 3 consecutive days**, repeat sampling over ~10 days, with **>50% MMA reduction** indicating significant response. NBS can detect attenuated B12-responsive cases, including cblA. (forny2021guidelinesforthe pages 8-9, forny2021guidelinesforthe pages 6-8, forny2021guidelinesforthe pages 12-14, schnabel2023combinednewbornscreening pages 1-2, brennerova2021genetictestingis pages 1-2) |
| Core treatment | **Genotype-guided and response-guided long-term therapy** centers on **parenteral hydroxocobalamin**, especially in cblA, which “will mostly improve” with cobalamin therapy in guidelines. Common adjuncts in isolated MMA include **protein management**, **levocarnitine ~100 mg/kg/day**, and **metronidazole 10–20 mg/kg/day** to reduce gut propionate production. In acute decompensation, guidelines support **stop/reduce protein**, provide **high-calorie glucose ± lipids**, and treat hyperammonemia/acidosis per emergency protocols. Suggested NCIT intervention terms inline: hydroxocobalamin, levocarnitine, metronidazole, dietary management. (forny2021guidelinesforthe pages 11-12, forny2021guidelinesforthe pages 12-14, brennerova2021genetictestingis pages 1-2, brennerova2021genetictestingis pages 4-7) |
| Prognosis | Compared with mut MMA, **cblA has a significantly milder long-term course** with better preservation of renal and neurologic function and better survival, particularly under hydroxocobalamin treatment. Newborn screening plus specialized metabolic care appears beneficial **to some extent in cobalamin-responsive MMA**, but less so for cbl-nonresponsive MMA overall. Prognosis can still be serious if treatment is delayed or underestimated. (horster2021delineatingtheclinical pages 1-2, reischl‐hajiabadi2024outcomesafternewborn pages 1-2, brennerova2021genetictestingis pages 1-2) |
| Evidence gaps | No robust cblA-specific evidence was retrieved for: **formal prevalence/incidence specific to cblA**, validated **QoL instruments**, **modifier genes**, **epigenetic changes**, **single-cell/spatial transcriptomics**, **multi-omics signatures**, **dedicated Mmaa animal model**, or **cblA-specific interventional clinical trials**. Available recent screening/outcome studies usually pool cblA with other isolated MMA forms; careful subtype separation is required. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2, liu2024theutilityof pages 1-2, OpenTargets Search: methylmalonic aciduria cblA type-MMAB) |


*Table: This table summarizes the core disease-knowledge elements for methylmalonic aciduria, cblA type, emphasizing the correct causal gene assignment to MMAA and the clinically important distinction from MMAB-associated cblB disease.*

## 1. Disease information

### Definition

cblA disease is an inborn error of intracellular cobalamin metabolism in which deficient MMAA function compromises the delivery, protection, and reactivation of adenosylcobalamin-dependent methylmalonyl-CoA mutase (MMUT). The resulting biochemical phenotype is **isolated methylmalonic aciduria**—methylmalonate elevation without the marked hyperhomocysteinemia characteristic of combined cobalamin disorders. (forny2021guidelinesforthe pages 6-8, brennerova2021genetictestingis pages 1-2, takahashiiniguez2012roleofvitamin pages 11-12)

### Identifiers and synonyms

- **MONDO:** MONDO:0009613.
- **Orphanet:** ORPHA:79310, “Vitamin B12-responsive methylmalonic acidemia type cblA.”
- **OMIM phenotype:** **251100** in the strongest subtype-specific registry source. One secondary excerpt gave 251000; this conflict should be resolved in favor of the current OMIM record before automated ingestion. (OpenTargets Search: methylmalonic aciduria cblA type-MMAB, liu2010constructionofaa pages 21-26, horster2021delineatingtheclinical pages 1-2)
- **Gene:** *MMAA*, chromosome 4q31.21; the clinical case-report source gives MIM 607481 for the gene. (brennerova2021genetictestingis pages 1-2, horster2021delineatingtheclinical pages 1-2)
- **Common names:** methylmalonic acidemia/aciduria cblA type; cobalamin A deficiency; vitamin B12-responsive methylmalonic acidemia, cblA; isolated MMA, cblA complementation class.
- **ICD:** no cblA-specific ICD-10 code was established in the retrieved evidence. It is generally subsumed under disorders of amino-acid/organic-acid metabolism. A local ICD-10/ICD-11 terminology service should be queried before coding.
- **MeSH:** usually indexed under methylmalonic acidemia rather than a dedicated cblA descriptor.

The evidence is primarily **aggregated disease-level information and consented registry/cohort data**, supplemented by individual case reports and biochemical experiments—not routine EHR-derived population data. The principal cblA cohort comprised 28 patients from a 123-person isolated-MMA registry sample spanning 17 countries. (horster2021delineatingtheclinical pages 1-2, horster2021delineatingtheclinical pages 2-4)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

The necessary cause is **biallelic germline loss-of-function or function-impairing variants in MMAA**. The resulting defect is recessive and impairs mitochondrial AdoCbl handling rather than dietary B12 absorption. (brennerova2021genetictestingis pages 1-2, horster2021delineatingtheclinical pages 1-2)

### Genetic risk

Risk is highest for siblings of an affected person: under standard autosomal-recessive assumptions, each pregnancy of two confirmed carriers has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. The most frequent alleles in the registry were c.433C>T, p.(Arg145*), and c.592_595delACTG, p.(Thr198Serfs*6). Four additional variants reported there were c.1098G>A, c.589A>G, c.662_664delCAA, and c.593_596delCTGA. The p.(Arg145*) allele has been reported to account for approximately half of disease alleles in some European-ancestry series, suggesting a population enrichment, although a formal founder analysis was not retrieved. (abdrabo2019nextgenerationsequencing pages 31-37, horster2021delineatingtheclinical pages 2-4)

No validated susceptibility loci, modifier genes, protective alleles, anticipation, or quantified incomplete penetrance were identified. Expressivity is variable: presentation ranges from asymptomatic screening detection to severe neonatal decompensation. Large deletions should be considered if sequencing finds only one allele, but recurrent cblA-specific chromosomal rearrangements are not established.

### Environmental and protective factors

There is no environmental cause, infectious agent, toxin, smoking, alcohol, sex, or occupational exposure known to generate cblA disease. Environment instead modifies **decompensation risk**:

- fasting, fever, infection, surgery, vomiting, and excessive protein catabolism increase endogenous propionate production and can precipitate crisis;
- adequate energy during illness, avoidance of prolonged fasting, prompt treatment of infection, an emergency regimen, and sustained hydroxocobalamin reduce risk;
- dietary precursor load from valine, isoleucine, methionine, threonine, odd-chain fatty acids, and gut microbial propionate interacts with residual pathway capacity. The normal pathway degrades these substrates through methylmalonyl-CoA to succinyl-CoA. (takahashiiniguez2012roleofvitamin pages 4-6, forny2021guidelinesforthe pages 11-12)

These are **gene–environment interactions affecting severity**, not disease acquisition. Routine vaccination is indirectly protective by reducing infection-triggered catabolism.

## 3. Phenotypes

The most reliable cblA frequencies come from the 28-patient registry; denominators vary because of missing data. (horster2021delineatingtheclinical pages 1-2, horster2021delineatingtheclinical pages 5-6, horster2021delineatingtheclinical pages 15-17)

| Phenotype | Character and frequency | Suggested HPO annotation |
|---|---|---|
| Methylmalonic aciduria | Defining laboratory abnormality; persistent but usually lower than in mut-type MMA | HP:0012120 |
| Metabolic crisis | Leading diagnostic manifestation, 16/21 symptomatic patients (76%); episodic | Metabolic acidosis; Acute metabolic decompensation |
| Neonatal/infantile onset | Median first symptoms 24.5 days; 43% had neonatal first crisis, 33% later, 24% no crisis | Neonatal onset; Infantile onset |
| High-anion-gap metabolic acidosis | Potentially severe during crisis | HP:0001942 |
| Hyperammonemia | Secondary; case-level values of 1,600 µmol/L reported in severe neonatal cblA | HP:0001987 |
| Vomiting, poor feeding, lethargy/dehydration | Typical crisis manifestations; cblA-specific percentages unavailable | HP:0002013; HP:0011968; HP:0001254; HP:0001944 |
| Hypotonia/encephalopathy | Acute neurologic manifestations; frequencies unavailable | HP:0001252; HP:0001298 |
| Movement disorder | 1/27 (4%) | HP:0100022 |
| Seizures | 0/27 in the registry, although possible in severe MMA generally | HP:0001250 |
| Chronic kidney disease/renal failure | 2/23, approximately 9%; substantially less common than mut-type MMA | HP:0012622 / HP:0000083 |
| Hypertension | 1/22 (5%) | HP:0000822 |
| Feeding support | NG tube 3/27 (11%); PEG 1/27 (4%) | HP:0011968; Feeding difficulties |
| Pancreatitis | 0 reported in the cblA cohort | HP:0001733, if present individually |
| Growth impairment | Less marked than in mut disease; exact cblA prevalence unavailable | HP:0004322 / HP:0001510 when documented |

Functional outcomes were comparatively favorable: 14/18 (78%) attended regular school, and all four adult cblA participants lived independently. These are useful proxies for cognitive and daily function, but no cblA-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific quality-of-life study was retrieved. Intramuscular injections and restrictive diets plausibly burden daily life, but that impact was not quantitatively measured. (horster2021delineatingtheclinical pages 15-17, horster2021delineatingtheclinical pages 17-19)

## 4. Genetic and molecular information

### Gene and variant classes

*MMAA* encodes a 418-amino-acid mitochondrial protein in the G3E family of P-loop GTPases. Disease alleles include nonsense, frameshift/deletion, and missense variants. They are constitutionally inherited; somatic cblA disease is not recognized. (takahashiiniguez2012roleofvitamin pages 11-12, liu2010constructionofaa pages 21-26, horster2021delineatingtheclinical pages 1-2)

- **p.(Arg145*)**: truncating, recurrent, expected loss of function.
- **p.(Thr198Serfs*6)**: frameshift/truncating and recurrent.
- **p.(Leu89Pro)**: missense; experimental/structural analyses support severe protein destabilization and it can produce neonatal disease despite cobalamin responsiveness.
- Other experimentally discussed substitutions—R145Q, R359Q, Y209C, G147E, and G218E—can impair stability, secondary structure, or conformational flexibility. (brennerova2021genetictestingis pages 4-7, takahashiiniguez2012roleofvitamin pages 11-12, horster2021delineatingtheclinical pages 2-4)

Clinical classification must be assigned variant by variant using current ClinVar/ACMG evidence. Population allele frequencies and ClinVar review status were not present in the retrieved full texts and should not be inferred. Most disease alleles are expected to be extremely rare because the disorder is recessive and ultra-rare.

No established modifier gene, methylation signature, histone abnormality, recurrent copy-number syndrome, aneuploidy, or structural chromosome lesion specific to cblA was found. CMA, karyotyping, and FISH therefore are not first-line tests unless an independent syndromic indication exists.

## 5. Environmental information

No toxin, radiation exposure, pollutant, pathogen, or lifestyle behavior causes cblA. Relevant exposures are metabolic stressors—fasting, infection, fever, surgery, dehydration, and inadequate caloric intake—which drive proteolysis and precursor flux. Diet is therapeutic rather than preventive of genotype. Gut bacteria contribute propionate; this is the rationale for intermittent antimicrobial therapy in selected MMA patients. (takahashiiniguez2012roleofvitamin pages 4-6, forny2021guidelinesforthe pages 11-12)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic MMAA variants lead to** absent, unstable, or functionally impaired mitochondrial MMAA protein.
2. **Defective MMAA GTPase/chaperone activity leads to** impaired protection, gating/loading, and reactivation of AdoCbl-dependent MMUT; the protein interaction and protectase/reactivase functions are experimentally demonstrated, while their exact relative contribution in every human allele remains partly inferred. (takahashiiniguez2012roleofvitamin pages 11-12, froese2009geneticsandbiochemistry pages 32-37)
3. **Impaired active MMUT formation leads to** reduced conversion of L-methylmalonyl-CoA into succinyl-CoA in the mitochondrial matrix.
4. **The metabolic block leads to** accumulation of methylmalonyl-CoA and diversion into methylmalonic acid and methylcitrate, with elevated C3 and depletion of free carnitine/CoA. (forny2021guidelinesforthe pages 6-8, brennerova2021genetictestingis pages 1-2)
5. **During fasting, infection, or other catabolism, increased precursor flux leads to** abrupt organic-acid accumulation, high-anion-gap acidosis, ketosis, secondary hyperammonemia, and mitochondrial energetic stress.
6. **Acute biochemical toxicity and energetic failure lead to** vomiting, lethargy, dehydration, hypotonia, encephalopathy, and potentially coma or death.
7. **Branch A—recurrent/chronic metabolite exposure leads to** renal tubular/interstitial and neurologic injury; the tissue-level route is incompletely demonstrated in cblA specifically.
8. **Branch B—residual MMAA function plus pharmacologic hydroxocobalamin leads to** greater effective AdoCbl/MMUT activity, lower methylmalonate, fewer crises, and the characteristically milder cblA course. (horster2021delineatingtheclinical pages 1-2, brennerova2021genetictestingis pages 4-7)

### Molecular and cellular detail

MMAA has a mitochondrial targeting sequence and physically associates with MMUT. Biochemical work supports nucleotide-dependent protection of MMUT from oxidative inactivation and GTP-hydrolysis-dependent reactivation by exchanging inactive cofactor; one system recovered approximately 70% mutase activity. (takahashiiniguez2012roleofvitamin pages 11-12)

Relevant ontology suggestions include:

- **GO biological process:** cobalamin metabolic process; propionyl-CoA catabolic process; cellular response to oxidative stress; mitochondrial organization.
- **GO molecular function:** GTP binding; GTPase activity; protein-folding chaperone activity/regulation of methylmalonyl-CoA mutase.
- **GO cellular component:** mitochondrial matrix.
- **Cell Ontology:** hepatocyte (CL:0000182), renal proximal-tubule epithelial cell, neuron, astrocyte, skeletal-muscle cell, and cardiomyocyte are biologically relevant, although cblA-specific cell-resolution injury maps are unavailable.

No cblA-specific single-cell atlas, spatial transcriptomic study, lipidomic signature, validated epigenomic signature, or multi-omics integration was retrieved. Recent biomarker work in pooled isolated MMA emphasizes FGF21, GDF15, LCN2, propionate oxidation, methylmalonate, and C3, but subtype-specific cblA performance remains insufficiently established.

## 7. Anatomical structures affected

- **Primary biochemical compartment:** mitochondrial matrix, especially in liver, kidney, brain, skeletal muscle, and other high-energy tissues.
- **Primary organs clinically affected:** central nervous system and kidney; gastrointestinal/nutritional function during crisis.
- **Possible secondary involvement:** heart, pancreas, optic pathways, and bone marrow are recognized in broader MMA, but were uncommon or insufficiently characterized in the cblA cohort. ECG abnormalities occurred in 1/5 tested and echocardiographic abnormalities in 1/8, with inadequate data to define a cblA cardiac phenotype. (horster2021delineatingtheclinical pages 15-17)
- **Laterality:** systemic and generally bilateral/non-lateralized.

Suggested anatomy: UBERON liver, kidney, brain, basal ganglion, skeletal muscle, heart, and pancreas; GO: mitochondrial matrix. Exact UBERON identifiers should be resolved through an ontology service rather than assigned from memory.

## 8. Temporal development

cblA is congenital genetically but may be clinically silent at birth. Among 21 evaluable cblA patients, first crisis was neonatal in 43%, post-neonatal in 33%, and absent in 24%; median age at first symptoms was 24.5 days. Severe neonatal onset does **not** exclude cblA or B12 responsiveness. (horster2021delineatingtheclinical pages 6-7, brennerova2021genetictestingis pages 1-2)

The course is lifelong, with episodic catabolic crises superimposed on chronic biochemical disease. Effective hydroxocobalamin can yield prolonged stability, but biochemical normalization is not guaranteed. Critical windows are the newborn period, intercurrent illness, surgery, fasting, and any delay in recognizing B12 responsiveness. There is no established spontaneous remission; apparent remission is treatment-induced metabolic stability.

## 9. Inheritance and population

Inheritance is autosomal recessive with no expected sex bias; the registry included 17 males and 11 females, compatible with equal susceptibility. Its mean age was 11.9 years. (horster2021delineatingtheclinical pages 2-4, horster2021delineatingtheclinical pages 1-2)

A robust cblA-specific birth prevalence or incidence was not identified. Estimates of all MMA, such as 1:48,000–1:250,000, pool genetically distinct subtypes and must not be entered as cblA prevalence. (brennerova2021genetictestingis pages 1-2)

Recent screening context illustrates rarity but not subtype-specific incidence: in 548,707 newborns, a German multiple-tier program confirmed five methylmalonic acidurias among 166 total confirmed findings; the study highlighted two cofactor-responsive MMA cases. (schnabel2023combinednewbornscreening pages 1-2)

Consanguinity increases the probability that both parents carry the same rare allele. The c.433C>T, p.(Arg145*) enrichment in European ancestry is the best available population-specific signal, but carrier frequency and a proven founder haplotype were not established. Penetrance has not been formally quantified; expressivity is variable. Germline mosaicism is theoretically possible but not documented as a recurrent cblA feature.

## 10. Diagnostics

### Biochemical and clinical workflow

1. **Newborn screening:** increased propionylcarnitine (C3), C3/C2, and related ratios. Single-tier C3 has a high false-positive rate, so second-tier methylmalonate/methylcitrate testing improves specificity. (forny2021guidelinesforthe pages 8-9, schnabel2023combinednewbornscreening pages 1-2)
2. **Confirmatory testing:** quantitative plasma or urine methylmalonic acid and urine organic-acid analysis; C3 and methylcitrate are commonly increased.
3. **Subtype discrimination:** total homocysteine and methionine. cblA produces isolated MMA with no substantial hyperhomocysteinemia; combined cblC and related disorders elevate homocysteine. Serum B12 should be checked to exclude acquired deficiency. (forny2021guidelinesforthe pages 6-8, brennerova2021genetictestingis pages 1-2)
4. **Acute severity tests:** blood gas, electrolytes/anion gap, glucose, lactate, ketones, ammonia, CBC, liver tests, creatinine/cystatin C, urinalysis, and carnitine profile.
5. **Definitive diagnosis:** biallelic pathogenic/likely pathogenic *MMAA* variants, using a targeted isolated-MMA/cobalamin panel or single-gene analysis. WES/WGS is useful for unresolved or atypical cases; deletion/duplication analysis is appropriate if only one allele is found. CMA, karyotype, FISH, mtDNA, and repeat-expansion testing are not routine.
6. **Functional confirmation where needed:** fibroblast propionate incorporation, AdoCbl synthesis, complementation analysis, or RNA studies for uncertain splice variants.

### Cobalamin-response test

Guidelines recommend assessing every MMA patient. Measure urine or plasma MMA on separate baseline days, administer **1 mg intramuscular hydroxocobalamin on three consecutive days**, and repeat MMA measurements over approximately ten days; a reduction exceeding 50% supports response. Testing should be performed when metabolically stable because dialysis, infusions, or crisis resolution can confound it. Genotyping is still essential because poorly standardized in-vivo testing can misclassify patients. (brennerova2021genetictestingis pages 1-2, brennerova2021genetictestingis pages 4-7, forny2021guidelinesforthe pages 12-14)

### Imaging and ancillary tests

MRI brain, EEG, ECG/echocardiography, ophthalmologic examination, neuropsychology, hearing testing, and renal imaging are complication-directed rather than diagnostic. Biopsy is generally unnecessary.

### Differential diagnosis

- **MMUT deficiency:** often more severe and less B12 responsive.
- **cblB:** biallelic *MMAB*; impaired adenosyltransferase, often less responsive.
- **cblD variant 2:** *MMADHC* with isolated MMA.
- **MCEE deficiency:** generally milder isolated MMA.
- **cblC and other combined cobalamin defects:** methylmalonate plus hyperhomocysteinemia/low methionine.
- **Propionic acidemia:** elevated C3/methylcitrate without marked methylmalonate.
- **Maternal/neonatal nutritional B12 deficiency:** biochemical mimic resolved by nutritional evaluation.

A 2024 LC–MS/MS study of 140 controls and 228 patients reported DBS reference intervals of 0.04–1.02 µmol/L for methylmalonate and 0.02–0.27 µmol/L for methylcitrate. DBS methylmalonate correlated with urine MMA at r=0.849, while DBS methylcitrate correlated with urine methylcitrate at r=0.693; this is promising for follow-up but was not cblA-specific. (liu2024theutilityof pages 1-2)

## 11. Outcome and prognosis

The treated cblA prognosis is substantially better than mut-type MMA. In the 28-person registry, all cblA participants survived, compared with six deaths among 95 mut patients. Chronic renal failure occurred in about 2/23 (9%), seizures in 0/27, and movement disorder in 1/27. Preserved schooling and independent adult living suggest relatively favorable function. (horster2021delineatingtheclinical pages 15-17, horster2021delineatingtheclinical pages 17-19)

No validated 5- or 10-year survival rate or life-expectancy estimate exists specifically for cblA. Prognostic factors include residual MMAA function, response and adherence to hydroxocobalamin, age/severity at first decompensation, crisis frequency, renal function, and access to specialist care. Canonical MMA and C3 levels are influenced by diet and renal clearance, so trends and multisystem biomarkers are preferable to isolated measurements.

The 2024 German screening follow-up—six MMA cases within a mixed 27-patient IMD cohort, median follow-up 3.6 years—concluded that screening and specialist care benefited cobalamin-responsive MMA “to some extent,” while cobalamin-nonresponsive MMA retained high early risk. These pooled results support early cblA detection but cannot supply a cblA-specific effect size. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2)

## 12. Treatment

### Maintenance therapy

- **Hydroxocobalamin:** cornerstone, preferably parenteral/intramuscular. The cblA cohort had 27/28 reported responders; among patients with route data, 86% received intramuscular treatment. Dose and frequency are individualized by biochemical response and adherence. A severe p.(Leu89Pro) case became stable on 1 mg IM weekly, with urine MMA approximately 799–1,291 µmol/mmol creatinine. (horster2021delineatingtheclinical pages 1-2, horster2021delineatingtheclinical pages 5-6, brennerova2021genetictestingis pages 4-7)
- **Protein/nutrition:** avoid excessive propiogenic amino-acid intake while supplying enough natural protein for normal growth. In the registry, 19/26 (73.1%) followed a calculated diet and 7/26 (27%) received precursor-free amino-acid supplements. Over-restriction risks malnutrition. (horster2021delineatingtheclinical pages 5-6)
- **Levocarnitine:** guideline starting framework approximately 100 mg/kg/day, titrated to free carnitine and clinical status.
- **Metronidazole:** approximately 10–20 mg/kg/day, often intermittently, to reduce intestinal propionate production; monitor neurologic toxicity and antimicrobial stewardship.
- **Rehabilitation/support:** PT, OT, speech/feeding therapy, educational support, renal and neuropsychological surveillance as indicated. (forny2021guidelinesforthe pages 11-12)

Suggested NCIt concepts are Hydroxocobalamin, Levocarnitine, Metronidazole, Medical Nutrition Therapy, Hemodialysis, Liver Transplantation, and Kidney Transplantation; exact NCIt identifiers should be terminology-service validated.

### Acute decompensation

Emergency care aims to reverse catabolism: temporarily stop or reduce protein, deliver high-calorie IV glucose with or without lipid, give carnitine, continue/initiate hydroxocobalamin, correct fluids/electrolytes/acidosis, identify infection, and monitor ammonia and neurologic status closely. Severe hyperammonemia or refractory acidosis may require extracorporeal clearance. The neonatal cblA case literature demonstrates that ammonia can exceed 1,000 µmol/L and require extracorporeal elimination. (brennerova2021genetictestingis pages 1-2, forny2021guidelinesforthe pages 11-12)

### Transplantation and advanced therapy

Liver or combined liver–kidney transplantation is considered in MMA with frequent severe decompensations or advanced renal disease; it improves stability but does not cure systemic disease, and lifelong metabolic follow-up remains necessary. Because most cblA patients respond well to hydroxocobalamin and have milder outcomes, transplantation is uncommon and evidence is largely extrapolated from severe MMUT/cblB disease. (forny2021guidelinesforthe pages 12-14)

No approved cblA gene, mRNA, RNAi, ASO, CRISPR, or cell therapy was identified. The retrieved trial landscape contained broad MMA natural-history and gene-therapy studies, but none demonstrated a cblA-specific interventional program; MMUT-directed gene therapy should not be represented as MMAA replacement.

## 13. Prevention

- **Primary prevention of genotype:** unavailable after conception. Carrier testing, reproductive counseling, prenatal diagnosis, and preimplantation genetic testing are possible once familial variants are known.
- **Secondary prevention:** newborn screening, rapid confirmatory metabolite testing, molecular subtyping, and immediate response testing/treatment. The 2023 pilot found 161/166 confirmed newborns asymptomatic at first report and demonstrated feasibility of a multiple-tier algorithm. (schnabel2023combinednewbornscreening pages 1-2)
- **Tertiary prevention:** hydroxocobalamin adherence, avoidance of fasting, written sick-day protocols, adequate calories during illness, carnitine and dietary management, vaccination, prompt infection treatment, and periodic renal, neurologic, nutritional, ophthalmologic, and cardiac surveillance.
- **Cascade screening:** test siblings and at-risk relatives; offer biochemical testing promptly to newborn siblings while molecular results are pending.

No disease-specific vaccine or environmental public-health intervention applies.

## 14. Other species and natural disease

No well-validated naturally occurring veterinary counterpart caused by orthologous *MMAA* variants was identified in the retrieved literature. There is no zoonotic potential or cross-species transmission because cblA is inherited, not infectious. MMAA/MeaB conservation across species is mechanistically important: bacterial MeaB is the experimentally tractable ortholog that established GTP-dependent mutase protection and reactivation. However, bacterial biochemistry is not equivalent to naturally occurring cblA disease. (takahashiiniguez2012roleofvitamin pages 9-11, takahashiiniguez2012roleofvitamin pages 11-12)

Suggested taxa for comparative work include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), and commonly used bacterial MeaB systems, but no breed ontology annotation is applicable.

## 15. Model organisms and experimental systems

### Disease-specific systems

- **Patient dermal fibroblasts:** principal cblA cellular model. Assays include propionate incorporation, AdoCbl synthesis after exogenous cobalamin, complementation, and hydroxocobalamin rescue.
- **Recombinant MMAA/MMUT proteins:** define GTPase activity, protein interaction, stability, protectase/reactivase function, and structural effects of missense variants.
- **Bacterial MeaB–MCM systems:** useful for conserved chaperone mechanism and nucleotide-dependent cofactor exchange. (takahashiiniguez2012roleofvitamin pages 9-11, takahashiiniguez2012roleofvitamin pages 11-12)

### Limitations and gaps

No dedicated, well-characterized *Mmaa* knockout/knock-in mouse, zebrafish cblA model, cblA iPSC-derived organoid, or cblA-specific CRISPR screen was established in the retrieved evidence. Published *Mmut* models represent mut-type MMA, while *Mmachc* models represent cblC disease; neither should be annotated as a cblA model. Fibroblasts are excellent for biochemical classification but do not reproduce organ-level renal, cerebral, or systemic catabolic physiology.

## Recent developments and expert interpretation

1. **2023 multiple-tier screening:** 548,707 newborns were screened; five methylmalonic acidurias were confirmed, and cofactor-responsive cases could be detected before major symptoms. Published 28 July 2023, DOI: https://doi.org/10.3390/nu15153355. Its abstract states that the method “allows the identification of attenuated and severe disease courses.” (schnabel2023combinednewbornscreening pages 1-2)
2. **2024 screening outcomes:** median 3.6-year follow-up supported meaningful but incomplete benefit for cobalamin-responsive MMA. Published online after acceptance on 7 March 2024, DOI: https://doi.org/10.1002/jimd.12731. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2)
3. **2024 DBS monitoring:** simultaneous MMA, methylcitrate, and homocysteine measurement offers a less invasive monitoring approach, with strong correlation between DBS and urine MMA. Published 20 June 2024, DOI: https://doi.org/10.3389/fnut.2024.1414681. Subtype-specific validation remains needed. (liu2024theutilityof pages 1-2)
4. **Expert consensus:** the 2021 international guideline recommends molecular subtyping and testing B12 responsiveness in every MMA patient; cblA patients “will mostly improve” with parenteral cobalamin. DOI: https://doi.org/10.1002/jimd.12370. (forny2021guidelinesforthe pages 11-12, forny2021guidelinesforthe pages 12-14)
5. **Natural-history interpretation:** the principal registry study concluded that cblA and mut disease can initially present similarly, but treated cblA has lower MMA, fewer renal and neurologic complications, and superior survival. DOI: https://doi.org/10.1002/jimd.12297. (horster2021delineatingtheclinical pages 1-2, horster2021delineatingtheclinical pages 17-19)

## Evidence limitations

cblA is ultra-rare, and much MMA literature pools *MMAA*, *MMAB*, and *MMUT* disease. Accordingly, broad MMA statistics, transplant outcomes, biomarkers, and experimental therapies cannot automatically be assigned to cblA. PMID metadata were not consistently exposed in the retrieved full-text records; DOI URLs and publication dates are therefore supplied where verified rather than risking incorrect PMID assignment. The clearest unmet needs are a larger genotype-resolved longitudinal cohort, cblA-specific patient-reported outcomes, standardized hydroxocobalamin dosing/response criteria, contemporary allele-frequency analysis, and dedicated organismal and advanced human-cell models.

References

1. (horster2021delineatingtheclinical pages 1-2): Friederike Hörster, Ali Tunç Tuncel, Florian Gleich, Tanja Plessl, Sean D. Froese, Sven F. Garbade, Stefan Kölker, and Matthias R. Baumgartner. Delineating the clinical spectrum of isolated methylmalonic acidurias: <scp><i>cbla</i></scp> and <i>mut</i>. Sep 2021. URL: https://doi.org/10.1002/jimd.12297, doi:10.1002/jimd.12297. This article has 43 citations and is from a peer-reviewed journal.

2. (brennerova2021genetictestingis pages 1-2): Katarína Brennerová, Martina Škopková, Mária Ostrožlíková, Jana Šaligová, Juraj Staník, Vladimír Bzdúch, and Daniela Gašperíková. Genetic testing is necessary for correct diagnosis and treatment in patients with isolated methylmalonic aciduria: a case report. BMC Pediatrics, Dec 2021. URL: https://doi.org/10.1186/s12887-021-03067-3, doi:10.1186/s12887-021-03067-3. This article has 4 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: methylmalonic aciduria cblA type-MMAB): Open Targets Query (methylmalonic aciduria cblA type-MMAB, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (horster2021delineatingtheclinical pages 2-4): Friederike Hörster, Ali Tunç Tuncel, Florian Gleich, Tanja Plessl, Sean D. Froese, Sven F. Garbade, Stefan Kölker, and Matthias R. Baumgartner. Delineating the clinical spectrum of isolated methylmalonic acidurias: <scp><i>cbla</i></scp> and <i>mut</i>. Sep 2021. URL: https://doi.org/10.1002/jimd.12297, doi:10.1002/jimd.12297. This article has 43 citations and is from a peer-reviewed journal.

5. (abdrabo2019nextgenerationsequencing pages 31-37): LS Abdrabo. Next generation sequencing to identify genes underlying methylmalonic aciduria. Unknown journal, 2019.

6. (takahashiiniguez2012roleofvitamin pages 11-12): Tóshiko Takahashi-Iñiguez, Enrique García-Hernandez, Roberto Arreguín-Espinosa, and María Elena Flores. Role of vitamin b12 on methylmalonyl-coa mutase activity. Journal of Zhejiang University SCIENCE B, 13:423-437, Jun 2012. URL: https://doi.org/10.1631/jzus.b1100329, doi:10.1631/jzus.b1100329. This article has 199 citations.

7. (froese2009geneticsandbiochemistry pages 32-37): Darren Sean Froese. Genetics and biochemistry of cobalamin disorders. Jan 2009. URL: https://doi.org/10.11575/prism/16795, doi:10.11575/prism/16795. This article has 0 citations.

8. (forny2021guidelinesforthe pages 6-8): Patrick Forny, Friederike Hörster, Diana Ballhausen, Anupam Chakrapani, Kimberly A. Chapman, Carlo Dionisi‐Vici, Marjorie Dixon, Sarah C. Grünert, Stephanie Grunewald, Goknur Haliloglu, Michel Hochuli, Tomas Honzik, Daniela Karall, Diego Martinelli, Femke Molema, Jörn Oliver Sass, Sabine Scholl‐Bürgi, Galit Tal, Monique Williams, Martina Huemer, and Matthias R. Baumgartner. Guidelines for the diagnosis and management of methylmalonic acidaemia and propionic acidaemia: first revision. Mar 2021. URL: https://doi.org/10.1002/jimd.12370, doi:10.1002/jimd.12370. This article has 337 citations and is from a peer-reviewed journal.

9. (schnabel2023combinednewbornscreening pages 10-11): Elena Schnabel, Stefan Kölker, Florian Gleich, Patrik Feyh, Friederike Hörster, Dorothea Haas, Junmin Fang-Hoffmann, Marina Morath, Gwendolyn Gramer, Wulf Röschinger, Sven F. Garbade, Georg F. Hoffmann, Jürgen G. Okun, and Ulrike Mütze. Combined newborn screening allows comprehensive identification also of attenuated phenotypes for methylmalonic acidurias and homocystinuria. Nutrients, 15:3355, Jul 2023. URL: https://doi.org/10.3390/nu15153355, doi:10.3390/nu15153355. This article has 25 citations.

10. (horster2021delineatingtheclinical pages 6-7): Friederike Hörster, Ali Tunç Tuncel, Florian Gleich, Tanja Plessl, Sean D. Froese, Sven F. Garbade, Stefan Kölker, and Matthias R. Baumgartner. Delineating the clinical spectrum of isolated methylmalonic acidurias: <scp><i>cbla</i></scp> and <i>mut</i>. Sep 2021. URL: https://doi.org/10.1002/jimd.12297, doi:10.1002/jimd.12297. This article has 43 citations and is from a peer-reviewed journal.

11. (horster2021delineatingtheclinical pages 5-6): Friederike Hörster, Ali Tunç Tuncel, Florian Gleich, Tanja Plessl, Sean D. Froese, Sven F. Garbade, Stefan Kölker, and Matthias R. Baumgartner. Delineating the clinical spectrum of isolated methylmalonic acidurias: <scp><i>cbla</i></scp> and <i>mut</i>. Sep 2021. URL: https://doi.org/10.1002/jimd.12297, doi:10.1002/jimd.12297. This article has 43 citations and is from a peer-reviewed journal.

12. (horster2021delineatingtheclinical pages 15-17): Friederike Hörster, Ali Tunç Tuncel, Florian Gleich, Tanja Plessl, Sean D. Froese, Sven F. Garbade, Stefan Kölker, and Matthias R. Baumgartner. Delineating the clinical spectrum of isolated methylmalonic acidurias: <scp><i>cbla</i></scp> and <i>mut</i>. Sep 2021. URL: https://doi.org/10.1002/jimd.12297, doi:10.1002/jimd.12297. This article has 43 citations and is from a peer-reviewed journal.

13. (horster2021delineatingtheclinical pages 17-19): Friederike Hörster, Ali Tunç Tuncel, Florian Gleich, Tanja Plessl, Sean D. Froese, Sven F. Garbade, Stefan Kölker, and Matthias R. Baumgartner. Delineating the clinical spectrum of isolated methylmalonic acidurias: <scp><i>cbla</i></scp> and <i>mut</i>. Sep 2021. URL: https://doi.org/10.1002/jimd.12297, doi:10.1002/jimd.12297. This article has 43 citations and is from a peer-reviewed journal.

14. (forny2021guidelinesforthe pages 8-9): Patrick Forny, Friederike Hörster, Diana Ballhausen, Anupam Chakrapani, Kimberly A. Chapman, Carlo Dionisi‐Vici, Marjorie Dixon, Sarah C. Grünert, Stephanie Grunewald, Goknur Haliloglu, Michel Hochuli, Tomas Honzik, Daniela Karall, Diego Martinelli, Femke Molema, Jörn Oliver Sass, Sabine Scholl‐Bürgi, Galit Tal, Monique Williams, Martina Huemer, and Matthias R. Baumgartner. Guidelines for the diagnosis and management of methylmalonic acidaemia and propionic acidaemia: first revision. Mar 2021. URL: https://doi.org/10.1002/jimd.12370, doi:10.1002/jimd.12370. This article has 337 citations and is from a peer-reviewed journal.

15. (forny2021guidelinesforthe pages 12-14): Patrick Forny, Friederike Hörster, Diana Ballhausen, Anupam Chakrapani, Kimberly A. Chapman, Carlo Dionisi‐Vici, Marjorie Dixon, Sarah C. Grünert, Stephanie Grunewald, Goknur Haliloglu, Michel Hochuli, Tomas Honzik, Daniela Karall, Diego Martinelli, Femke Molema, Jörn Oliver Sass, Sabine Scholl‐Bürgi, Galit Tal, Monique Williams, Martina Huemer, and Matthias R. Baumgartner. Guidelines for the diagnosis and management of methylmalonic acidaemia and propionic acidaemia: first revision. Mar 2021. URL: https://doi.org/10.1002/jimd.12370, doi:10.1002/jimd.12370. This article has 337 citations and is from a peer-reviewed journal.

16. (schnabel2023combinednewbornscreening pages 1-2): Elena Schnabel, Stefan Kölker, Florian Gleich, Patrik Feyh, Friederike Hörster, Dorothea Haas, Junmin Fang-Hoffmann, Marina Morath, Gwendolyn Gramer, Wulf Röschinger, Sven F. Garbade, Georg F. Hoffmann, Jürgen G. Okun, and Ulrike Mütze. Combined newborn screening allows comprehensive identification also of attenuated phenotypes for methylmalonic acidurias and homocystinuria. Nutrients, 15:3355, Jul 2023. URL: https://doi.org/10.3390/nu15153355, doi:10.3390/nu15153355. This article has 25 citations.

17. (forny2021guidelinesforthe pages 11-12): Patrick Forny, Friederike Hörster, Diana Ballhausen, Anupam Chakrapani, Kimberly A. Chapman, Carlo Dionisi‐Vici, Marjorie Dixon, Sarah C. Grünert, Stephanie Grunewald, Goknur Haliloglu, Michel Hochuli, Tomas Honzik, Daniela Karall, Diego Martinelli, Femke Molema, Jörn Oliver Sass, Sabine Scholl‐Bürgi, Galit Tal, Monique Williams, Martina Huemer, and Matthias R. Baumgartner. Guidelines for the diagnosis and management of methylmalonic acidaemia and propionic acidaemia: first revision. Mar 2021. URL: https://doi.org/10.1002/jimd.12370, doi:10.1002/jimd.12370. This article has 337 citations and is from a peer-reviewed journal.

18. (brennerova2021genetictestingis pages 4-7): Katarína Brennerová, Martina Škopková, Mária Ostrožlíková, Jana Šaligová, Juraj Staník, Vladimír Bzdúch, and Daniela Gašperíková. Genetic testing is necessary for correct diagnosis and treatment in patients with isolated methylmalonic aciduria: a case report. BMC Pediatrics, Dec 2021. URL: https://doi.org/10.1186/s12887-021-03067-3, doi:10.1186/s12887-021-03067-3. This article has 4 citations and is from a peer-reviewed journal.

19. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2): Anna T. Reischl‐Hajiabadi, Elena Schnabel, Florian Gleich, Katharina Mengler, Martin Lindner, Peter Burgard, Roland Posset, Svenja Lommer‐Steinhoff, Sarah C. Grünert, Eva Thimm, Peter Freisinger, Julia B. Hennermann, Johannes Krämer, Gwendolyn Gramer, Dominic Lenz, Stine Christ, Friederike Hörster, Georg F. Hoffmann, Sven F. Garbade, Stefan Kölker, and Ulrike Mütze. Outcomes after newborn screening for propionic and methylmalonic acidemia and homocystinurias. Journal of Inherited Metabolic Disease, 47:674-689, Apr 2024. URL: https://doi.org/10.1002/jimd.12731, doi:10.1002/jimd.12731. This article has 20 citations and is from a peer-reviewed journal.

20. (liu2024theutilityof pages 1-2): Yi Liu, Xue Ma, Lulu Kang, Ying Jin, Mengqiu Li, Jin-qing Song, Haixia Li, Yongtong Cao, and Yanling Yang. The utility of methylmalonic acid, methylcitrate acid, and homocysteine in dried blood spots for therapeutic monitoring of three inherited metabolic diseases. Frontiers in Nutrition, Jun 2024. URL: https://doi.org/10.3389/fnut.2024.1414681, doi:10.3389/fnut.2024.1414681. This article has 5 citations.

21. (liu2010constructionofaa pages 21-26): JH Liu. Construction of a knockout mouse model for combined methylmalonic aciduria and homocystinuria,«cblc» type («mmachc»). Unknown journal, 2010.

22. (takahashiiniguez2012roleofvitamin pages 4-6): Tóshiko Takahashi-Iñiguez, Enrique García-Hernandez, Roberto Arreguín-Espinosa, and María Elena Flores. Role of vitamin b12 on methylmalonyl-coa mutase activity. Journal of Zhejiang University SCIENCE B, 13:423-437, Jun 2012. URL: https://doi.org/10.1631/jzus.b1100329, doi:10.1631/jzus.b1100329. This article has 199 citations.

23. (takahashiiniguez2012roleofvitamin pages 9-11): Tóshiko Takahashi-Iñiguez, Enrique García-Hernandez, Roberto Arreguín-Espinosa, and María Elena Flores. Role of vitamin b12 on methylmalonyl-coa mutase activity. Journal of Zhejiang University SCIENCE B, 13:423-437, Jun 2012. URL: https://doi.org/10.1631/jzus.b1100329, doi:10.1631/jzus.b1100329. This article has 199 citations.

## Artifacts

- [Edison artifact artifact-00](Methylmalonic_Aciduria_cblA_Type-deep-research-falcon_artifacts/artifact-00.md)