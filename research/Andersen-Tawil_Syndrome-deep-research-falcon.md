---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:28:18.483654'
end_time: '2026-07-31T17:35:37.852334'
duration_seconds: 439.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Andersen-Tawil Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Andersen-Tawil_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Andersen-Tawil Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Andersen-Tawil Syndrome** covering all of the
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
- **Disease Name:** Andersen-Tawil Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Andersen-Tawil Syndrome** covering all of the
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


# Andersen–Tawil syndrome: disease-characteristics research report

**Scope and evidence note.** This report synthesizes disease-level resources, human cohorts, primary functional studies, clinical-trial records, and recent 2023–2024 work. Andersen–Tawil syndrome (ATS) is exceptionally rare, so most treatment evidence is observational, from small cohorts or case reports rather than randomized trials. The December 2024 flecainide study discussed below is a **preprint**, not yet peer reviewed in the retrieved record.

## Executive summary

ATS is a multisystem, usually autosomal-dominant ion-channel disorder defined by a variably expressed triad of: (1) ventricular arrhythmias with characteristic prominent U waves, (2) potassium-sensitive episodic paralysis, and (3) developmental craniofacial, dental, and limb abnormalities. Most molecularly confirmed disease is caused by heterozygous loss-of-function variants in **KCNJ2**, encoding the Kir2.1 inward-rectifier potassium channel. Reduced **IK1** destabilizes resting membrane potential and terminal repolarization in cardiomyocytes and skeletal myofibers, explaining ventricular ectopy and impaired muscle excitability. Prevalence is commonly estimated near **1 per million**, although underdiagnosis is likely. Ventricular arrhythmias occur in approximately 60–90%, while severe cardiac events remain much less common than ectopy but are clinically consequential; a recent review reported a 5-year cumulative sudden-cardiac-death probability of 7.9%. (pupaza2023assessmentofsudden pages 9-11, OpenTargets Search: Andersen-Tawil syndrome-KCNJ2)

| Domain | Established finding | Quantitative evidence | Evidence type / source / date | Knowledge-base ontology suggestions |
|---|---|---:|---|---|
| Definition / triad | Andersen-Tawil syndrome (ATS) is a rare inherited ion-channel disorder classically defined by ventricular arrhythmias, episodic weakness/periodic paralysis, and characteristic dysmorphic features. | Prevalence commonly cited as ~1 per 1,000,000; symptom onset within first 2 decades in 42.3%; ventricular arrhythmias in 60–90%; polymorphic VT 48%; bidirectional VT 44%. | Peer-reviewed review, *Diagnostics* (Nov 2023) (pupaza2023assessmentofsudden pages 9-11) | MONDO: Andersen-Tawil syndrome; HPO: Cardiac arrhythmia, Periodic paralysis, Facial dysmorphism |
| Genetics / KCNJ2 / Kir2.1 | ATS1 is caused predominantly by heterozygous loss-of-function variants in **KCNJ2**, encoding inward rectifier potassium channel **Kir2.1**; disease is usually autosomal dominant, with sporadic/de novo cases also reported. | Open Targets disease-target association score 0.8407 for KCNJ2–ATS; 5 supporting evidence items; KCNJ2 mutations account for majority of ATS1 and ~60% of ATS overall in older primary studies. | Database evidence, Open Targets / MONDO_0008222; peer-reviewed primary study, *Circ Cardiovasc Genet* (Feb 2011); review, *Diagnostics* (Nov 2023) (OpenTargets Search: Andersen-Tawil syndrome-KCNJ2, barajasmartinez2011biophysicalandmolecular pages 7-8, pupaza2023assessmentofsudden pages 9-11) | HGNC: KCNJ2; protein: Kir2.1; GO: inward rectifier potassium channel activity; GO: regulation of membrane potential |
| Variant spectrum | Numerous pathogenic KCNJ2 variants are distributed throughout Kir2.1; dominant-negative effects and trafficking defects are established mechanisms for some variants. | “More than 90 mutations” summarized in 2024 preprint; historical literature cited >40 mutations by 2015 cohort report; example de novo **R260P** showed strong dominant-negative effect. | Preprint, medRxiv (Dec 2024); peer-reviewed cohort, *Muscle & Nerve* (Feb 2015); peer-reviewed primary study, *Circ Cardiovasc Genet* (Feb 2011) (cruz2024kir2.1mutationsdifferentially pages 3-6, kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, barajasmartinez2011biophysicalandmolecular pages 7-8) | Sequence variant classes: missense, in-frame deletion; SO terms for missense variant / inframe deletion |
| Cardiac phenotype | Cardiac manifestations include PVCs, ventricular ectopy, prolonged QT/QU intervals with prominent U waves, polymorphic and bidirectional VT, and occasional cardiac arrest/SCD. | In one 15-patient cohort: ventricular arrhythmias 75%, BVT in 6/12 Holters, normal QTc in 76%, prominent U waves in 84%; 37 cardiac arrests in 259-patient meta-analysis. | Peer-reviewed cohort, *Muscle & Nerve* (Feb 2015); peer-reviewed meta-analysis (Jan 2026) (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, garcia2026genderspecificcardiacfeatures pages 1-2) | HPO: Premature ventricular contractions, Bidirectional ventricular tachycardia, Syncope, Abnormal U wave, Long QT interval |
| Periodic paralysis | Episodic muscle weakness is a core but variably penetrant feature; attacks may be potassium-sensitive and show sex-related variability. | In 15-patient cohort, PP observed in 7 patients across 6 kinships; attacks reported in 20% of females vs 80% of males in that series; females less likely to present with PP in 259-patient meta-analysis (p=0.02). | Peer-reviewed cohort, *Muscle & Nerve* (Feb 2015); peer-reviewed meta-analysis (Jan 2026) (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, garcia2026genderspecificcardiacfeatures pages 1-2) | HPO: Periodic paralysis, Episodic weakness, Hypokalemia (when present) |
| Dysmorphism | Developmental/craniofacial and limb anomalies are common and aid recognition. | In 15-patient cohort, dysmorphic features noted in 100%; study protocol lists low-set ears, hypertelorism, micrognathia, clinodactyly, syndactyly, hand/foot micromelia as diagnostic features. | Peer-reviewed cohort, *Muscle & Nerve* (Feb 2015); ClinicalTrials.gov observational study description (2007) (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, NCT00521794 chunk 1) | HPO: Hypertelorism, Micrognathia, Clinodactyly, Syndactyly, Low-set ears |
| Diagnostics | Practical diagnosis relies on recognition of at least 2 of 3 domains: episodic weakness, cardiac conduction/ventricular arrhythmia findings, and dysmorphic features; ECG/Holter and molecular confirmation are key. | Trial protocol diagnostic rule: ≥2 of 3 features; observational natural-history study enrolled 28 participants across 7 sites for standardized longitudinal phenotyping. | ClinicalTrials.gov observational study NCT00521794, completed; supporting clinical review 2023 (NCT00521794 chunk 1, pupaza2023assessmentofsudden pages 9-11) | HPO set above; LOINC/ECG concepts: QTc prolongation, ventricular ectopy; NCIT: genetic testing |
| Mechanism / pathophysiology | Reduced **IK1** from dysfunctional Kir2.1 destabilizes resting membrane potential and repolarization, promoting ventricular ectopy and arrhythmia; some variants also alter sodium current/channelosome behavior. | 2024 preprint reports mutation-specific reductions in IK1 and differential effects on INa with increased ventricular arrhythmia inducibility in multiple mouse models; 2011 R260P study showed trafficking defect with markedly reduced IK1. | Preprint, medRxiv (Dec 2024); peer-reviewed primary study, *Circ Cardiovasc Genet* (Feb 2011); peer-reviewed review, *Naunyn Schmiedebergs Arch Pharmacol* (Apr 2024) (cruz2024kir2.1mutationsdifferentially pages 3-6, barajasmartinez2011biophysicalandmolecular pages 7-8, cruz2024kir2.1mutationsdifferentially pages 22-24) | GO: cardiac muscle cell action potential, membrane repolarization, potassium ion transmembrane transport; CL: cardiomyocyte |
| Treatments / arrhythmia management | Management is individualized; beta-blockers are commonly used, flecainide may reduce arrhythmia burden in some patients, ICD is used in high-risk cases, and class-Ic safety is under active reassessment. | In 15-patient cohort, all arrhythmic patients received beta-blockers and 40% received ICDs; 2024 preprint literature review of 53 ATS1 patients found 54% partial flecainide response, VA reduction in 23%, ineffectiveness in 23%, non-fatal cardiac arrest in 13.5%. | Peer-reviewed cohort, *Muscle & Nerve* (Feb 2015); preprint, medRxiv (Dec 2024) (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, cruz2024kir2.1mutationsdifferentially pages 20-22) | NCIT: Beta-Adrenergic Receptor Blocker Therapy, Flecainide, Implantable Cardioverter-Defibrillator |
| Prognosis / risk | Most patients have chronic morbidity; life-threatening arrhythmias occur in a minority but are clinically important, with sex differences emerging in newer syntheses. | 5-year cumulative SCD probability reported as 7.9%; risk factors summarized in 2023 review include syncope, sustained VT, amiodarone use, micrognathia, periodic paralysis, prolonged Tpeak-Tend; females had higher cardiac arrest risk in 2026 meta-analysis (p=0.02). | Peer-reviewed review, *Diagnostics* (Nov 2023); peer-reviewed meta-analysis (Jan 2026) (pupaza2023assessmentofsudden pages 9-11, garcia2026genderspecificcardiacfeatures pages 1-2) | HPO: Sudden cardiac death, Syncope; prognostic annotation: sustained VT history |
| 2024 hiPSC multi-omics | A 2024 hiPSC-CM disease model combined RNA-seq and ATAC-seq to identify developmental and electrophysiologic ATS mechanisms beyond the primary channel defect. | Mutant iPSC-CMs had lower spontaneous pulsation, prolonged APD, reduced Kir2.1 current; **ZNF528** was continuously downregulated from day 4; 7 potassium-related pathways downregulated (p<0.05); **KCNJ2, CTTN, ATP1B1** were consistently downregulated targets. | Peer-reviewed primary study, *Journal of Translational Medicine* (Mar 2024) (chen2024transcriptomeandopen pages 1-3, chen2024transcriptomeandopen pages 3-4) | GO: potassium ion import/inward rectifier activity pathways; gene entities: ZNF528, CTTN, ATP1B1; CL: induced pluripotent stem cell-derived cardiomyocyte |
| 2024 flecainide precision-safety study | Mutation-specific flecainide safety/efficacy is a major 2024 development; some KCNJ2 variants may confer proarrhythmic risk under class-Ic therapy. | In reviewed 53 ATS1 patients: partial response 54%; VA reduction only 23%; persistent VA in 20–50% of responders; non-fatal cardiac arrest 13.5%; mouse/iPSC models showed increased rotor incidence or inducibility for several variants, while S136F appeared milder. | **Preprint** primary/translational study, medRxiv (Dec 2024) — not peer reviewed at time cited (cruz2024kir2.1mutationsdifferentially pages 20-22, cruz2024kir2.1mutationsdifferentially pages 3-6) | NCIT: Flecainide; variant-level drug response annotation; GO: conduction velocity / arrhythmogenesis |
| Clinical trials | ATS-specific interventional evidence remains sparse; available studies focus on natural history and exploratory therapy. | NCT00521794 observational natural-history study: completed, n=28; NCT00839501 potassium + acetazolamide trial: terminated, phase 1, n=3; NCT06205550 N-of-1 in ATS and MEPPC: not yet recruiting, phase 2, planned n=10. | ClinicalTrials.gov records (2007 onward) (NCT00521794 chunk 1) | NCIT: Potassium, Acetazolamide; study-design metadata; evidence-source tag: clinical trial registry |


*Table: This table summarizes the most actionable evidence domains for Andersen-Tawil syndrome, including established findings, quantitative support, evidence provenance, and ontology-oriented mapping suggestions. It distinguishes peer-reviewed evidence from the 2024 flecainide preprint and highlights current trial activity.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Andersen–Tawil syndrome.
* **MONDO:** **MONDO:0008222**.
* **OMIM:** commonly represented as **Andersen syndrome, 170390**; the KCNJ2-associated subtype is often termed ATS type 1.
* **Orphanet:** **ORPHA:37553**, “cardiodysrhythmic potassium-sensitive periodic paralysis.”
* **Gene:** **KCNJ2**, Ensembl **ENSG00000123700**, encoding potassium inwardly rectifying channel subfamily J member 2/Kir2.1. Open Targets identifies KCNJ2 as the sole high-confidence associated target in its ATS record, supported by five evidence items and an association score of 0.8407. (OpenTargets Search: Andersen-Tawil syndrome-KCNJ2)
* **ICD:** ATS generally lacks a uniquely specific ICD-10-CM code and may be coded under periodic paralysis, long-QT/other cardiac arrhythmia, or congenital-malformation categories depending on manifestation. ICD-11 should likewise be verified against the jurisdictional release rather than inferred from the historical label “LQT7.”
* **Synonyms:** Andersen syndrome; Andersen–Tawil syndrome type 1; cardiodysrhythmic potassium-sensitive periodic paralysis; potassium-sensitive periodic paralysis with ventricular dysrhythmia; long-QT syndrome type 7/LQT7. “LQT7” is historically used but can mislead because many patients have a normal QTc and instead exhibit prolonged terminal repolarization/QU and prominent U waves.

The evidence is principally **aggregated disease-level evidence**, not EHR-derived individual-patient data. Some frequency estimates derive from assembled case reports and small cohorts and therefore are susceptible to referral and publication bias.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The established cause of ATS1 is a **germline heterozygous loss-of-function KCNJ2 variant**. Inheritance is usually autosomal dominant, but de novo/sporadic cases occur. Older functional studies estimated KCNJ2 variants in about 60% of clinically diagnosed cases; KCNJ2-negative patients remain genetically heterogeneous or unresolved and are sometimes termed ATS2, although this is a clinical category rather than a single established locus. (pupaza2023assessmentofsudden pages 9-11, barajasmartinez2011biophysicalandmolecular pages 7-8)

No infectious, toxic, occupational, inflammatory, or lifestyle exposure is an established primary cause. Physiologic exposures instead act as **attack triggers** on the inherited electrical substrate: rest after exertion, prolonged rest, fasting, carbohydrate-rich meals, cold, emotional stress, and shifts in serum potassium may precipitate weakness or arrhythmia. A 2024 patient-derived model originated from a woman whose weakness was triggered by exercise and cold, illustrating this interaction but not proving population-wide trigger frequencies. (chen2024transcriptomeandopen pages 3-4)

### Risk and protective factors

* **Genetic risk:** a pathogenic/likely pathogenic KCNJ2 variant; family history; de novo variants; and potentially variant-specific effects on trafficking, PIP2 coupling, channel gating, or Kir2.1–Nav1.5 channelosome behavior.
* **Clinical cardiac risk:** prior syncope, sustained ventricular tachycardia, prolonged Tpeak–Tend, and previous cardiac arrest. A 2023 review also associated micrognathia, periodic paralysis, and amiodarone use with life-threatening events, but treatment association may reflect confounding by severity. (pupaza2023assessmentofsudden pages 9-11)
* **Sex:** evidence is evolving. A 2026 meta-analysis of 259 cardiac cases found more complex ventricular arrhythmias and cardiac arrest among females, whereas males more often had periodic paralysis. Because this synthesis selected cases with cardiac manifestations and pooled case reports, it is hypothesis-generating rather than a population estimate. (garcia2026genderspecificcardiacfeatures pages 1-2, garcia2026genderspecificcardiacfeatures pages 10-11)
* **Protective factors:** no validated protective allele or modifier gene is established. Trigger avoidance, maintenance of an individualized safe potassium range, avoidance of arrhythmogenic/QT-active drugs, and surveillance may reduce attacks or complications but do not prevent inheritance.

## 3. Phenotypes

### Core manifestations

1. **Ventricular electrical instability.** Findings include frequent premature ventricular contractions, couplets/bigeminy, polymorphic ventricular ectopy, nonsustained or sustained polymorphic VT, and particularly bidirectional VT. Prominent U waves and prolonged QU are characteristic; QTc can be normal. Estimated ventricular-arrhythmia prevalence is **60–90%**, with polymorphic VT reported in 48% and bidirectional VT in 44% in one recent synthesis. In a 15-person KCNJ2 cohort, 75% had ventricular arrhythmia, 6/12 monitored patients had bidirectional VT, 84% had prominent U waves, and 76% had normal QTc. (pupaza2023assessmentofsudden pages 9-11, kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)
   * Suggested HPO: **Premature ventricular contractions**, **Bidirectional ventricular tachycardia**, **Polymorphic ventricular tachycardia**, **Syncope**, **Abnormal U wave**, **Prolonged QT interval**, and **Sudden cardiac death**.

2. **Periodic paralysis/episodic weakness.** Attacks are flaccid, episodic, and variable in duration and potassium association; ictal potassium may be low, normal, or high. Between attacks, strength may initially be normal, although fixed/progressive myopathy has been described. In one small cohort, 7/15 had periodic paralysis; attacks occurred in 80% of males versus 20% of females, demonstrating sex-related variability but not a generalizable prevalence estimate. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)
   * Suggested HPO: **Periodic paralysis**, **Episodic flaccid weakness**, **Hypokalemia** when documented, **Muscle weakness**, and **Myopathy**.

3. **Developmental dysmorphism.** Common features include hypertelorism, broad forehead, low-set ears, small or receding mandible/micrognathia, dental abnormalities, clinodactyly, syndactyly, short digits or small hands/feet, short stature, and scoliosis. Dysmorphism was recorded in 100% of one intensively phenotyped 15-person cohort but is less consistently recognized in routine practice. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, NCT00521794 chunk 1)
   * Suggested HPO: **Hypertelorism**, **Micrognathia**, **Low-set ears**, **Clinodactyly**, **Syndactyly**, **Short stature**, and **Scoliosis**.

### Onset, severity, course, and quality of life

Features are often congenital or recognizable in childhood, while episodic weakness and arrhythmia commonly emerge during childhood or adolescence. A 2023 review reported onset before 19 years in 42.3%, but delayed diagnosis into adulthood is common. Severity and expressivity vary markedly within families: some individuals have one component, others the complete triad. Arrhythmia and weakness are generally episodic; developmental abnormalities are stable; fixed myopathy can slowly progress in a minority. (pupaza2023assessmentofsudden pages 9-11)

No validated ATS-specific quality-of-life instrument or robust EQ-5D/SF-36 dataset was found. Nevertheless, recurrent weakness can impair mobility, schooling, work, and exercise; palpitations, syncope, ICD shocks, and fear of sudden death impose substantial psychosocial burden.

## 4. Genetic and molecular information

### Causal gene and variant biology

**KCNJ2** is the established causal gene. Pathogenic variants are germline and predominantly heterozygous missense variants, with in-frame deletions and other classes also reported. More than 90 variants were summarized in the 2024 preprint, distributed across Kir2.1; curated clinical classification must be performed variant-by-variant in ClinVar/ClinGen rather than assuming every rare KCNJ2 change is pathogenic. Population frequency should be extremely low or absent in gnomAD for a fully penetrant pathogenic allele, but no universal frequency cutoff substitutes for ACMG/AMP evaluation. (cruz2024kir2.1mutationsdifferentially pages 3-6)

Functional consequences include:

* impaired plasma-membrane trafficking;
* reduced channel conductance or altered gating;
* weakened phosphatidylinositol-4,5-bisphosphate (**PIP2**) coupling;
* dominant-negative suppression because mutant and wild-type subunits coassemble as tetramers;
* perturbation of Kir2.1–Nav1.5 macromolecular complexes, reducing both IK1 and, for some variants, sodium current and conduction.

The de novo **p.Arg260Pro (R260P)** variant caused defective trafficking and a strong dominant-negative reduction of IK1 in heterologous cells. Documented experimental variants also include **C122Y, G215D, R67W, S136F**, and **Δ314–315**; these are mechanistically heterogeneous and should not be treated as pharmacologically interchangeable. (barajasmartinez2011biophysicalandmolecular pages 7-8, cruz2024kir2.1mutationsdifferentially pages 20-22)

No reproducible modifier gene, protective variant, anticipation, epigenetic syndrome, recurrent chromosomal rearrangement, or founder effect is established. Germline mosaicism is biologically possible in apparently de novo families but is not quantified. Somatic mutation is not the disease mechanism.

## 5. Environmental and lifestyle information

Environmental factors modify **expression**, not occurrence. Patients should identify personal triggers using attack/food/activity records. Abrupt potassium shifts, dehydration, fasting, large carbohydrate loads, cold, vigorous exercise followed by rest, and emotional stress may provoke episodes. Smoking, alcohol, pollution, radiation, occupational toxins, and infectious agents are not established causes. Medication review is important because drugs affecting potassium balance, conduction, or repolarization may worsen either phenotype.

No vaccine or anti-infective strategy is disease-specific. Ordinary immunization remains appropriate unless an individual cardiac or neuromuscular circumstance dictates otherwise.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** pathogenic KCNJ2 variant → defective Kir2.1 assembly, trafficking, PIP2-dependent gating, or channelosome organization → reduced inward-rectifier potassium current (**IK1**).

**Cardiac downstream:** reduced IK1 → less stable ventricular-myocyte resting membrane potential and impaired terminal repolarization → altered sodium-channel availability/conduction and calcium cycling → delayed afterdepolarizations, ectopy, re-entry, polymorphic/bidirectional VT, syncope, and occasionally cardiac arrest. Kir2.1 is particularly important in ventricular cardiomyocytes and Purkinje cells. (pupaza2023assessmentofsudden pages 9-11, cruz2024kir2.1mutationsdifferentially pages 3-6)

**Skeletal-muscle downstream:** reduced Kir2.1-mediated potassium conductance → unstable myofiber resting potential and paradoxical depolarization/inexcitability during potassium or metabolic shifts → episodic flaccid weakness; repeated or persistent electrical dysfunction may contribute to fixed myopathy.

**Developmental downstream:** Kir2.1 has non-excitable developmental roles; disturbed membrane bioelectric signaling plausibly contributes to craniofacial and limb patterning. The precise human developmental chain remains less defined than cardiac electrophysiology.

Suggested annotations include **GO: inward rectifier potassium channel activity**, **potassium ion transmembrane transport**, **regulation of membrane potential**, **cardiac muscle cell action potential**, and **cardiac muscle cell repolarization**; cellular targets include **cardiomyocyte**, **cardiac Purkinje cell**, and **skeletal muscle fiber/myocyte**.

### Molecular profiling and 2024 advance

Chen et al. generated patient hiPSCs carrying **KCNJ2 c.199C>T**, corrected the variant by CRISPR/HDR, differentiated cardiomyocytes, and performed electrophysiology, RNA-seq, ATAC-seq, WGCNA, and pathway analysis across six developmental time points. Mutant cells beat more slowly, had prolonged action potentials and reduced Kir2.1 current. **ZNF528** was persistently downregulated from cardiac mesoderm day 4; seven potassium-related pathways were suppressed (all p<0.05), and **KCNJ2, CTTN, and ATP1B1** emerged as consistently downregulated proteins. This provides peer-reviewed, patient-specific multi-omic evidence for developmental regulatory effects beyond the primary channel lesion, but it is a single cellular model and not yet a clinical biomarker. (chen2024transcriptomeandopen pages 1-3, chen2024transcriptomeandopen pages 3-4)

The authors’ abstract conclusion was that the study identified transcription factors and targets related to “electrophysiology and developmental pathogenicity” and potential therapeutic candidates not dependent on gene editing. (chen2024transcriptomeandopen pages 1-3)

No validated ATS metabolomic, lipidomic, immune, inflammatory, or spatial-transcriptomic signature is currently established.

## 7. Anatomical structures affected

* **Heart:** ventricular myocardium and specialized conduction system/Purkinje network; usually structurally normal. Suggested UBERON: heart, cardiac ventricle, ventricular myocardium, cardiac conduction system.
* **Skeletal muscle:** limb and axial skeletal muscle; clinically bilateral/generalized rather than consistently lateralized. Suggested UBERON: skeletal muscle organ, limb muscle.
* **Craniofacial skeleton and dentition:** mandible/maxilla, ears, facial spacing, teeth.
* **Limbs/digits and spine:** hands, feet, fingers/toes, and vertebral column.
* **Subcellular:** plasma membrane/sarcolemma, Kir2.1 tetrameric channel complex, and associated PIP2/channelosome domains; sarcoplasmic-reticulum effects have also been modeled. Suggested GO cellular-component terms: **plasma membrane**, **sarcolemma**, **potassium channel complex**, and **intercalated disc/channelosome** where experimentally supported.

## 8. Temporal development

ATS is congenital genetically and developmentally, but clinical onset is variable. Dysmorphism is present from birth; weakness and arrhythmia commonly become evident in childhood or adolescence. The course is lifelong and fluctuating rather than conventionally staged. Periods without attacks are remission intervals, not cure. Critical opportunities are early recognition after unexplained weakness, characteristic ventricular ectopy, syncope, or identification of an affected relative; early rhythm surveillance and cascade testing may prevent avoidable complications.

## 9. Inheritance and population

Prevalence is estimated at approximately **1 per 1,000,000**; reliable incidence, carrier-frequency, geographic, and ancestry-specific estimates are unavailable. No endemic region or consistently enriched ancestry is established. (garcia2026genderspecificcardiacfeatures pages 1-2, pupaza2023assessmentofsudden pages 9-11)

Inheritance is **autosomal dominant** with variable expressivity and incomplete penetrance. Each child of a heterozygous affected individual has a 50% probability of inheriting the variant, although phenotype cannot be predicted reliably. De novo cases occur. No anticipation or meaningful role for consanguinity is expected in the usual dominant disorder. Small cohorts suggest periodic paralysis may be more penetrant in males while complex arrhythmia may be more prominent in females, but estimates remain vulnerable to ascertainment bias. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, garcia2026genderspecificcardiacfeatures pages 1-2)

## 10. Diagnostics

### Clinical assessment

A historical practical rule is the presence of at least **two of three** domains: potassium-sensitive episodic weakness; ventricular electrical abnormalities; and typical dysmorphism. NCT00521794 operationalized this approach and followed 28 participants over two years with standardized strength, cardiac, electrodiagnostic, and optional genetic assessments. (NCT00521794 chunk 1)

Recommended work-up comprises:

1. Three-generation pedigree and examination for subtle facial/digital features.
2. Resting 12-lead ECG, emphasizing U waves and QU as well as QTc.
3. Ambulatory ECG/Holter to quantify PVCs and detect polymorphic/bidirectional VT; exercise testing may reveal or characterize ectopy but requires specialist supervision.
4. Echocardiography to exclude structural disease and assess ectopy-induced cardiomyopathy.
5. During weakness: serum potassium, magnesium, glucose, renal function, thyroid testing, creatine kinase, and ECG. Normal interictal potassium does not exclude ATS.
6. Neuromuscular examination and long-exercise EMG testing where available. Muscle biopsy is not routinely diagnostic; MRI may document chronic myopathy.

### Genetic testing

First-line molecular testing is **KCNJ2 sequencing with deletion/duplication analysis**, or a curated periodic-paralysis/inherited-arrhythmia panel including KCNJ2. A pathogenic/likely pathogenic variant confirms ATS1 in the appropriate phenotype. If negative, re-review phenotype and consider broader panel/WES/WGS for phenocopies or unresolved ATS-like disease. CMA, karyotype, FISH, mitochondrial DNA, and repeat-expansion tests are not routine unless other features indicate them. RNA-seq/ATAC-seq remain research tools, not clinical diagnostics.

Cascade testing should be offered to relatives after identification of a familial pathogenic variant. A VUS must not be used alone for predictive diagnosis or irreversible intervention.

### Differential diagnosis

* **CACNA1S/SCN4A hypokalemic or hyperkalemic periodic paralysis:** weakness without the characteristic ATS dysmorphism/ventricular phenotype.
* **Thyrotoxic periodic paralysis:** acquired biochemical hyperthyroidism, often without childhood dysmorphism.
* **Catecholaminergic polymorphic VT:** exercise/emotion-induced bidirectional or polymorphic VT, usually RYR2-related and without periodic paralysis/dysmorphism; ATS can mimic CPVT. (barajasmartinez2011biophysicalandmolecular pages 7-8)
* **Conventional long-QT syndromes:** characteristic QT prolongation and genotype-specific triggers, but not the ATS triad.
* **Short-QT syndrome type 3:** KCNJ2 gain-of-function rather than ATS loss-of-function.
* Other causes of ventricular ectopy, U waves, hypokalemia, syncope, neuromuscular weakness, and congenital dysmorphism.

## 11. Outcome and prognosis

Most patients survive into adulthood, but no robust disease-specific life-expectancy or 5-/10-year overall-survival estimates exist. Morbidity includes recurrent paralysis, fixed weakness/myopathy, syncope, ventricular arrhythmia, treatment adverse effects, device complications, and rare ectopy-induced cardiomyopathy. A 2023 review estimated 5-year cumulative SCD risk at **7.9%**. (pupaza2023assessmentofsudden pages 9-11)

One 15-person referral cohort reported syncope/cardiac arrest in 50–60%, but this should not be generalized because of very small sample size and referral enrichment. In the same series, only 25% were clinically asymptomatic. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)

Adverse prognostic markers include previous cardiac arrest, sustained VT, syncope, high/complex ectopic burden, and possible prolonged Tpeak–Tend. Formal prognostic biomarkers, validated risk calculators, and disease-specific patient-reported outcome instruments are lacking.

## 12. Treatment

Treatment should be coordinated between inherited-arrhythmia cardiology and neuromuscular specialists. No therapy corrects all three disease domains, and no drug is universally effective.

### Weakness

* During an attack, measure potassium and obtain cardiac monitoring before replacement whenever possible. Oral potassium may help documented hypokalemic attacks but can be hazardous when potassium is normal/high or arrhythmia is active.
* Preventive options include individualized potassium management and carbonic-anhydrase inhibitors such as **acetazolamide** or dichlorphenamide, extrapolated mainly from periodic-paralysis practice. Evidence in ATS is limited, and electrolyte/renal adverse effects require monitoring.
* Physical and occupational therapy, fall prevention, mobility aids, and graded activity support function; strenuous trigger activity followed by abrupt rest may need modification.

Suggested NCIT interventions: **Potassium Supplementation**, **Acetazolamide**, **Physical Therapy**, and **Occupational Therapy**.

### Arrhythmia

* Beta-blockers are frequently used, especially for symptomatic or adrenergically influenced arrhythmia, but response is variable and excessive bradycardia may worsen ectopy. In one cohort, all arrhythmic patients received beta-blockers, most often bisoprolol. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)
* **Flecainide** has reduced PVC/VT burden in multiple reports and may be combined with a beta-blocker. The R260P case remained symptomatic on nadolol but responded to flecainide. (barajasmartinez2011biophysicalandmolecular pages 7-8)
* Treatment must now be viewed as potentially **variant-specific**. A December 2024 preprint review of 53 treated ATS1 patients reported partial response in 54%, ventricular-arrhythmia reduction in only 23%, ineffectiveness in 23%, and nonfatal cardiac arrest in 13.5%. Mouse and patient-specific iPSC-CM models showed that flecainide could reduce conduction velocity and increase inducible arrhythmia/rotors for several variants, whereas S136F behaved more favorably. The authors concluded: “Class-Ic AADs are only partially effective and might be proarrhythmic in some ATS1 patients.” These provocative findings require peer-reviewed replication and should prompt close ECG/Holter monitoring rather than abrupt unsupervised discontinuation. (cruz2024kir2.1mutationsdifferentially pages 20-22, cruz2024kir2.1mutationsdifferentially pages 3-6)
* An **ICD** is appropriate for survivors of cardiac arrest and selected patients with recurrent hemodynamically significant sustained VT despite therapy. Frequent but tolerated ectopy alone does not automatically justify implantation. In one enriched cohort, 40% received ICDs. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)
* Catheter ablation can be considered for a dominant, mappable PVC/VT focus or ectopy-induced cardiomyopathy, but multifocal disease limits efficacy.
* Amiodarone is not a preferred routine ATS therapy; observational association with adverse events may reflect both pharmacology and confounding by indication.

Suggested NCIT terms: **Beta-Adrenergic Receptor Blocker Therapy**, **Flecainide**, **Implantable Cardioverter-Defibrillator**, and **Catheter Ablation**.

### Trials and advanced therapy

* **NCT00521794:** completed observational natural-history study, 28 participants.
* **NCT00839501:** phase 1 potassium/acetazolamide study, terminated after 3 participants.
* **NCT06205550:** phase 2 N-of-1 study in ATS and MEPPC, planned enrollment 10 and listed as not yet recruiting in the retrieved record.
* No approved ATS gene, RNA, cell, or CRISPR therapy exists. Gene addition is conceptually complicated by dominant-negative alleles and the need to target both cardiac and skeletal muscle safely. The 2024 CRISPR-corrected iPSC model is a mechanistic platform, not a clinical intervention. (chen2024transcriptomeandopen pages 1-3, chen2024transcriptomeandopen pages 3-4)

## 13. Prevention

**Primary prevention of the genotype is not possible** after conception. Reproductive options include preconception counseling, prenatal diagnosis, and preimplantation genetic testing when a familial pathogenic variant is known.

**Secondary prevention** includes cascade genetic testing, ECG/Holter assessment of carriers, and evaluation of asymptomatic children because disease can begin early. ATS is not part of standard biochemical newborn screening; genomic newborn screening remains investigational.

**Tertiary prevention** includes individualized trigger avoidance, electrolyte management, medication-interaction review, rhythm surveillance, emergency plans for prolonged paralysis/syncope, and ICD therapy in appropriately selected high-risk patients. Family members should understand autosomal-dominant recurrence risk and the inability to predict severity from inheritance alone.

## 14. Other species and natural disease

Kir2.1/KCNJ2 function is evolutionarily conserved across vertebrates. However, no well-established, naturally occurring companion-animal ATS with a validated breed association was identified in the retrieved evidence. Consequently, no VBO breed term, zoonotic potential, transmission pathway, or veterinary public-health concern applies. ATS is inherited, not contagious.

## 15. Model organisms and experimental systems

* **Heterologous cells:** HEK-cell expression permits trafficking, current-density, and dominant-negative testing. R260P markedly reduced IK1 and membrane trafficking. Strength: clean variant biophysics; limitation: lacks mature cardiac architecture. (barajasmartinez2011biophysicalandmolecular pages 7-8)
* **Mouse models:** cardiac AAV/transduction models expressing C122Y, G215D, Δ314–315, R67W, or S136F reproduce variant-dependent ECG and arrhythmia phenotypes. Flecainide increased inducibility in most tested mutants but reduced arrhythmia in S136F, supporting pharmacogenetic heterogeneity. Limitation: cardiac-restricted, acute expression and murine electrophysiology do not reproduce the full human developmental/neuromuscular syndrome. (cruz2024kir2.1mutationsdifferentially pages 20-22, cruz2024kir2.1mutationsdifferentially pages 3-6)
* **Patient-specific hiPSC cardiomyocytes:** reproduce reduced IK1, prolonged action potential, slow beating, conduction abnormalities, and re-entry; CRISPR-isogenic repair strengthens causal inference. Limitations include fetal-like electrophysiology and absence of whole-organ autonomic and mechanical context. (chen2024transcriptomeandopen pages 1-3, chen2024transcriptomeandopen pages 3-4)
* **In-silico structural/docking models:** predict mutation-specific changes around the Kir2.1 Cys311 flecainide pharmacophore. These generate hypotheses and cannot independently establish clinical drug response. (cruz2024kir2.1mutationsdifferentially pages 20-22)
* **Needed next models:** skeletal-muscle iPSC/myotube systems, dual cardiac–skeletal organoids, mature engineered tissues, and knock-in animals carrying patient variants under endogenous regulation.

## Evidence-quality conclusions and knowledge gaps

The causal KCNJ2–Kir2.1–IK1 relationship is supported by convergent human genetic, heterologous-cell, animal, and isogenic iPSC evidence. Clinical frequencies and treatment effects are less certain because ATS is rare, expressivity is broad, and published cohorts are referral-enriched. The most important 2024 advances were (1) developmental RNA/ATAC profiling that implicated ZNF528, CTTN, and ATP1B1 and (2) mutation-specific experimental evidence questioning uniform flecainide safety. The latter remains preprint-level evidence and should be treated as a signal for prospective, genotype-stratified trials—not as definitive proof that flecainide is broadly harmful. (cruz2024kir2.1mutationsdifferentially pages 20-22, chen2024transcriptomeandopen pages 1-3)

Priority research needs are an international prospective registry; standardized phenotype, quality-of-life, and attack outcomes; ClinGen-level variant curation; variant-stratified antiarrhythmic studies; validated SCD-risk prediction; skeletal-muscle models; and therapeutic approaches capable of addressing dominant-negative disease in both heart and skeletal muscle.

References

1. (pupaza2023assessmentofsudden pages 9-11): Adelina Pupaza, Eliza Cinteza, Corina Maria Vasile, Alin Nicolescu, and Radu Vatasescu. Assessment of sudden cardiac death risk in pediatric primary electrical disorders: a comprehensive overview. Diagnostics, 13:3551, Nov 2023. URL: https://doi.org/10.3390/diagnostics13233551, doi:10.3390/diagnostics13233551. This article has 7 citations.

2. (OpenTargets Search: Andersen-Tawil syndrome-KCNJ2): Open Targets Query (Andersen-Tawil syndrome-KCNJ2, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (barajasmartinez2011biophysicalandmolecular pages 7-8): Hector Barajas-Martinez, Dan Hu, Gustavo Ontiveros, Gabriel Caceres, Mayurika Desai, Elena Burashnikov, Jorge Scaglione, and Charles Antzelevitch. Biophysical and molecular characterization of a novel de novo kcnj2 mutation associated with andersen-tawil syndrome and catecholaminergic polymorphic ventricular tachycardia mimicry. Circulation: Cardiovascular Genetics, 4:51–57, Feb 2011. URL: https://doi.org/10.1161/circgenetics.110.957696, doi:10.1161/circgenetics.110.957696. This article has 50 citations.

4. (cruz2024kir2.1mutationsdifferentially pages 3-6): Francisco M. Cruz, Ana I. Moreno-Manuel, Sánchez Pérez Patricia, Juan Manuel Ruiz-Robles, Paula García Socuellamos, Lilian K. Gutiérrez, María Linarejos Vera-Pedrosa, Amaia Talavera Gutierrez, Gema Mondéjar Parreño, Álvaro Macías, Isabel Martínez-Carrascoso, Francisco J Bermúdez-Jiménez, Salvador Arias Santiago, Fernando Martínez de Benito, Aitana Braza-Boils, Carmen Valenzuela, CA Morillo, Esther Zorio, Juan Jiménez-Jaimez, and José Jalife. Kir2.1 mutations differentially increase the risk of flecainide proarrhythmia in andersen tawil syndrome. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.10.24318629, doi:10.1101/2024.12.10.24318629. This article has 1 citations.

5. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5): Anna Kostera‐Pruszczyk, Anna Potulska‐Chromik, Piotr Pruszczyk, Katarzyna Bieganowska, Maria Miszczak‐Knecht, Piotr Bienias, krzysztof szczałuba, Hsien‐Yang Lee, Emily Quinn, Rafal Ploski, Anna Kaminska, and Louis J. Ptáček. Andersen–tawil syndrome: report of 3 novel mutations and high risk of symptomatic cardiac involvement. Muscle & Nerve, 51:192-196, Feb 2015. URL: https://doi.org/10.1002/mus.24293, doi:10.1002/mus.24293. This article has 28 citations and is from a peer-reviewed journal.

6. (garcia2026genderspecificcardiacfeatures pages 1-2): Alan Garcia, Abdul Mueez Alam Kayani, Ricky Lemus-Zamora, Daniel Alejandro Navarro-Martinez, Eduardo Tellez-Garcia, Richard Salama-Frisbie, Jorge Gomez Flores, Eduardo Aviles, and Brijesh Patel. Gender-specific cardiac features in andersen–tawil syndrome: a comprehensive meta-analysis of case reports and series. Journal of Interventional Cardiac Electrophysiology, Jan 2026. URL: https://doi.org/10.1007/s10840-026-02237-6, doi:10.1007/s10840-026-02237-6. This article has 1 citations and is from a peer-reviewed journal.

7. (NCT00521794 chunk 1): Robert Griggs, MD. Characteristics of Andersen-Tawil Syndrome. University of Rochester. 2007. ClinicalTrials.gov Identifier: NCT00521794

8. (cruz2024kir2.1mutationsdifferentially pages 22-24): Francisco M. Cruz, Ana I. Moreno-Manuel, Sánchez Pérez Patricia, Juan Manuel Ruiz-Robles, Paula García Socuellamos, Lilian K. Gutiérrez, María Linarejos Vera-Pedrosa, Amaia Talavera Gutierrez, Gema Mondéjar Parreño, Álvaro Macías, Isabel Martínez-Carrascoso, Francisco J Bermúdez-Jiménez, Salvador Arias Santiago, Fernando Martínez de Benito, Aitana Braza-Boils, Carmen Valenzuela, CA Morillo, Esther Zorio, Juan Jiménez-Jaimez, and José Jalife. Kir2.1 mutations differentially increase the risk of flecainide proarrhythmia in andersen tawil syndrome. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.10.24318629, doi:10.1101/2024.12.10.24318629. This article has 1 citations.

9. (cruz2024kir2.1mutationsdifferentially pages 20-22): Francisco M. Cruz, Ana I. Moreno-Manuel, Sánchez Pérez Patricia, Juan Manuel Ruiz-Robles, Paula García Socuellamos, Lilian K. Gutiérrez, María Linarejos Vera-Pedrosa, Amaia Talavera Gutierrez, Gema Mondéjar Parreño, Álvaro Macías, Isabel Martínez-Carrascoso, Francisco J Bermúdez-Jiménez, Salvador Arias Santiago, Fernando Martínez de Benito, Aitana Braza-Boils, Carmen Valenzuela, CA Morillo, Esther Zorio, Juan Jiménez-Jaimez, and José Jalife. Kir2.1 mutations differentially increase the risk of flecainide proarrhythmia in andersen tawil syndrome. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.10.24318629, doi:10.1101/2024.12.10.24318629. This article has 1 citations.

10. (chen2024transcriptomeandopen pages 1-3): Peipei Chen, Junyu Long, Tianrui Hua, Zhifa Zheng, Ying Xiao, Lianfeng Chen, Kang Yu, Wei Wu, and Shuyang Zhang. Transcriptome and open chromatin analysis reveals the process of myocardial cell development and key pathogenic target proteins in long qt syndrome type 7. Journal of Translational Medicine, Mar 2024. URL: https://doi.org/10.1186/s12967-024-05125-7, doi:10.1186/s12967-024-05125-7. This article has 1 citations and is from a peer-reviewed journal.

11. (chen2024transcriptomeandopen pages 3-4): Peipei Chen, Junyu Long, Tianrui Hua, Zhifa Zheng, Ying Xiao, Lianfeng Chen, Kang Yu, Wei Wu, and Shuyang Zhang. Transcriptome and open chromatin analysis reveals the process of myocardial cell development and key pathogenic target proteins in long qt syndrome type 7. Journal of Translational Medicine, Mar 2024. URL: https://doi.org/10.1186/s12967-024-05125-7, doi:10.1186/s12967-024-05125-7. This article has 1 citations and is from a peer-reviewed journal.

12. (garcia2026genderspecificcardiacfeatures pages 10-11): Alan Garcia, Abdul Mueez Alam Kayani, Ricky Lemus-Zamora, Daniel Alejandro Navarro-Martinez, Eduardo Tellez-Garcia, Richard Salama-Frisbie, Jorge Gomez Flores, Eduardo Aviles, and Brijesh Patel. Gender-specific cardiac features in andersen–tawil syndrome: a comprehensive meta-analysis of case reports and series. Journal of Interventional Cardiac Electrophysiology, Jan 2026. URL: https://doi.org/10.1007/s10840-026-02237-6, doi:10.1007/s10840-026-02237-6. This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Andersen-Tawil_Syndrome-deep-research-falcon_artifacts/artifact-00.md)