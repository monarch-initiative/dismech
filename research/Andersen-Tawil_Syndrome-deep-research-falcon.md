---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T00:54:30.249495'
end_time: '2026-08-01T01:02:20.820881'
duration_seconds: 470.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Andersen-Tawil syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
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
- **Disease Name:** Andersen-Tawil syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Andersen-Tawil syndrome** covering all of the
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
- **Disease Name:** Andersen-Tawil syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Andersen-Tawil syndrome** covering all of the
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


# Andersen–Tawil syndrome: comprehensive disease-characteristics report

## Executive summary

Andersen–Tawil syndrome (ATS) is a rare, usually autosomal-dominant multisystem channelopathy characterized by the variably expressed triad of episodic flaccid paralysis, ventricular arrhythmias, and congenital craniofacial/skeletal abnormalities. ATS type 1 is caused by heterozygous loss-of-function variants in **KCNJ2**, which encodes the inwardly rectifying potassium channel Kir2.1. Reduced Kir2.1 current (**I_K1**) destabilizes resting membrane potential and repolarization in cardiomyocytes and skeletal myofibers; developmental expression of Kir2.1 also accounts for dysmorphism. Although historically called long-QT syndrome type 7, QTc is frequently normal, and prominent U waves, a broad T–U junction, ventricular ectopy, and bidirectional or polymorphic ventricular tachycardia are more characteristic. Recent work emphasizes mutation-specific mechanisms and potentially mutation-specific responses to flecainide rather than a uniform “KCNJ2 disease” phenotype. (cruz2024kir2.1mutationsdifferentially pages 3-6, kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, pupaza2023assessmentofsudden pages 9-11)

The table below gives a compact knowledge-base summary.

| Domain | Summary | Key data / implementation details | Ontology / IDs | Evidence |
|---|---|---|---|---|
| Identity / ontology | Andersen-Tawil syndrome (ATS) is a rare multisystem ion-channel disorder classically defined by the triad of periodic paralysis, ventricular arrhythmias, and characteristic dysmorphic/skeletal features. Most published knowledge is aggregated from disease-level resources, case series, cohorts, and genetics studies rather than EHR-only sources. | Also referred to as Long QT syndrome 7 / LQT7 and Andersen syndrome in parts of the literature. Prevalence estimate reported as ~1 per 1,000,000. | MONDO: requires database verification; OMIM: requires database verification; Orphanet: requires database verification; MeSH: requires database verification; Suggested HPO anchors: Periodic paralysis, Ventricular arrhythmia, Dysmorphism | (pupaza2023assessmentofsudden pages 9-11, cruz2024kir2.1mutationsdifferentially pages 3-6) |
| Cause / etiology | ATS1 is primarily caused by heterozygous loss-of-function variants in **KCNJ2**, encoding the inward rectifier potassium channel **Kir2.1**; inheritance is usually autosomal dominant, though sporadic cases occur. A minority of clinically diagnosed cases are KCNJ2-negative. | Review evidence notes most ATS1 cases are due to KCNJ2, while ~40% may represent non-KCNJ2 disease in some clinical overviews. >90 ATS1-associated mutations have been reported across Kir2.1 in a 2024 preprint review. | Gene: **KCNJ2**; Protein: **Kir2.1**; HGNC ID: requires database verification; Suggested GO: potassium ion transmembrane transport, inward rectifier potassium channel activity | (pupaza2023assessmentofsudden pages 9-11, cruz2024kir2.1mutationsdifferentially pages 3-6, cruz2024kir2.1mutationsdifferentially pages 1-3) |
| Hallmark phenotypes | Core phenotype spans neuromuscular, cardiac, and developmental features with marked variable expressivity. | In one 15-patient series: dysmorphic features in all subjects; periodic paralysis in 80% of males and 20% of females; cardiac arrhythmia in 75%; syncope/cardiac arrest history in 50% of females and 60% of males; prominent U waves in 84%; normal QTc in 76%; bidirectional VT in 6/12 monitored patients. Broader review: ventricular arrhythmias in 60–90%, polymorphic VT in 48%, bidirectional VT in 44%; onset commonly in first 2 decades, with 42.3% before age 19. | Suggested HPO: Periodic paralysis; Ventricular ectopy; Bidirectional ventricular tachycardia; Prominent U wave; Micrognathia; Hypertelorism; Syndactyly/clinodactyly | (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, pupaza2023assessmentofsudden pages 9-11) |
| Mechanism / pathophysiology | Upstream defect is Kir2.1 dysfunction causing reduced **IK1**, membrane depolarization, prolonged action potential/repolarization abnormalities, and arrhythmia susceptibility; downstream effects involve both sarcolemmal excitability and intracellular Ca2+ handling. | Mouse/preprint data support a dual mechanism: reduced inward rectifier K+ and Na+ currents, prolonged AP duration, slower conduction, and defective sarcoplasmic reticulum Kir2.1 localization contributing to abnormal spontaneous Ca2+ release. 2024 hiPSC multi-omics study identified downregulated potassium-related pathways and highlighted **ZNF528**, **KCNJ2**, **CTTN**, and **ATP1B1** as candidate pathogenic nodes. | Suggested GO: regulation of membrane potential; cardiac muscle cell action potential; potassium ion import across plasma membrane; calcium ion homeostasis. Suggested CL: cardiomyocyte, skeletal muscle cell. Suggested UBERON: heart, ventricular myocardium, skeletal muscle. | (macias2021dualdysfunctionof pages 1-6, chen2024transcriptomeandopen pages 19-20, cruz2024kir2.1mutationsdifferentially pages 20-22) |
| Diagnosis | Diagnosis is clinical plus electrophysiologic and genetic confirmation where possible. ECG/Holter findings are central; genetic testing supports confirmation and cascade screening. | Recommended workup includes 12-lead ECG, Holter monitoring, assessment for periodic paralysis and dysmorphic features, and KCNJ2 testing. In periodic paralysis practice guidance, if no mutation is identified, attack potassium values or long exercise testing can support diagnosis. Asymptomatic KCNJ2 carriers are recommended to undergo annual ECG plus 24-hour Holter surveillance. | Suggested HPO/LOINC concepts: ECG abnormality, Holter monitoring, long exercise test; Gene panel / single-gene **KCNJ2** testing; NCIT suggestion: Genetic Testing | (statland2018reviewofthe pages 24-30, NCT00521794 chunk 1, pupaza2023assessmentofsudden pages 9-11) |
| Treatment | Treatment remains individualized and incompletely evidence-based; separate management is needed for weakness attacks and arrhythmia risk. | Periodic paralysis management includes trigger avoidance, potassium modulation, carbonic anhydrase inhibitors (e.g., acetazolamide), and supportive behavioral measures. Antiarrhythmics reported as beneficial include flecainide, beta-blockers, calcium-channel blockers, and amiodarone in some reports; caution is advised because some agents may worsen neuromuscular symptoms. 2024 preprint review of 53 ATS1 patients found flecainide response was heterogeneous: 54% partial response, only 23% ventricular-arrhythmia reduction, 23% ineffective, and 13.5% non-fatal cardiac arrest. ICDs are used for selected high-risk patients; in one series, 40% received ICDs. | NCIT suggestions: Potassium Supplementation, Acetazolamide Therapy, Beta-Adrenergic Blockade, Flecainide Therapy, Implantable Cardioverter-Defibrillator | (statland2018reviewofthe pages 24-30, cruz2024kir2.1mutationsdifferentially pages 1-3, kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, NCT00839501 chunk 1) |
| Prognosis / natural history | Morbidity is substantial, especially from ventricular arrhythmia burden and recurrent weakness; sudden cardiac death risk is real but variable. | Review-level estimate: 5-year sudden cardiac death probability 7.9%. Risk factors highlighted include syncope history, sustained VT, micrognathia, and prolonged Tpeak-Tend interval. Only 25% were clinically/electrocardiographically asymptomatic in one series. | Suggested HPO: Sudden cardiac death, Syncope, Ventricular tachycardia; Prognostic markers: Tpeak-Tend prolongation | (pupaza2023assessmentofsudden pages 9-11, kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5) |
| Clinical trials / real-world studies | There are few formal ATS interventional trials; most practice is extrapolated from observational cohorts and case series. | **NCT00521794** (completed observational, n=28): prospective phenotyping over 2 years. **NCT00839501** (terminated phase 1, n=3): potassium 40 mEq BID and acetazolamide 250 mg BID vs placebo; terminated for poor recruitment. **NCT06205550** (not yet recruiting, estimated n=10): N-of-1 crossover comparing flecainide alone vs flecainide plus beta-blocker or calcium-channel blocker for ventricular ectopy burden. No approved gene therapy, RNA therapy, or cell therapy was identified in the retrieved evidence. | NCT00521794; NCT00839501; NCT06205550 | (NCT00521794 chunk 1, NCT00839501 chunk 1, NCT06205550 chunk 1) |
| Evidence gaps / cautions | The evidence base is limited by rarity, small cohorts, phenotype heterogeneity, and heavy reliance on retrospective reports. Some important recent mechanistic data are preprints. | Key gaps: uncertain non-KCNJ2 etiologies, incomplete penetrance/sex effects, limited prospective treatment comparisons, sparse QoL data, no validated biomarker-guided treatment algorithm, and no approved gene/RNA/cell therapies. Flecainide appears mutation-specific in benefit/risk, but this remains to be validated prospectively. | Mark uncertain identifiers as requiring database verification; prioritize future genotype-stratified registries and functional variant interpretation pipelines | (cruz2024kir2.1mutationsdifferentially pages 1-3, chen2024transcriptomeandopen pages 19-20, NCT06205550 chunk 1, statland2018reviewofthe pages 24-30) |


*Table: This table condenses the most actionable Andersen-Tawil syndrome facts for a disease knowledge base, including phenotype frequencies, mechanisms, diagnostics, treatment evidence, trial status, and explicit evidence gaps. It also flags ontology/identifier fields that require external database verification rather than speculation.*

## 1. Disease information

### Definition and terminology

ATS is a congenital, lifelong potassium-channel disorder affecting cardiac electrical activity, skeletal-muscle excitability, and development. Synonyms include **Andersen syndrome**, **Andersen–Tawil syndrome**, **long-QT syndrome type 7 (LQT7)**, **ATS1/KCNJ2-related ATS**, and, historically, **cardiodysrhythmic periodic paralysis**. “LQT7” can be misleading because one clinical series found a normal QTc in 76% of patients. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)

### Identifiers

* **OMIM:** 170390 (Andersen syndrome; reported in the retrieved literature).
* **Orphanet:** Andersen–Tawil syndrome has a dedicated rare-disease entry; the exact ORPHA identifier should be verified against the current Orphanet release before ingestion.
* **MONDO, MeSH, SNOMED CT:** dedicated mappings should likewise be resolved against the current ontology release rather than inferred from secondary literature.
* **ICD-10/ICD-11:** there is no consistently used disease-specific billing code in the retrieved evidence; cases may be represented through periodic-paralysis, cardiac-arrhythmia, or congenital-malformation categories.

The evidence base is predominantly **aggregated disease-level evidence**—registries, cohorts, case series, laboratory studies, and curated resources—not individual-patient EHR data. The completed prospective observational study NCT00521794 enrolled 28 patients at seven sites and included serial cardiac monitoring, strength testing, and quality-of-life assessment. (NCT00521794 chunk 1)

## 2. Etiology, risk, and protective factors

### Primary cause

ATS1 results from germline heterozygous **KCNJ2** loss-of-function variants. Kir2.1 is a tetrameric inward-rectifier channel that supplies I_K1. More than 90 ATS-associated variants distributed through Kir2.1 were summarized in a 2024 analysis. A substantial minority of clinically diagnosed patients lack an identified KCNJ2 variant; “ATS2” is therefore a clinical/genetic-unknown category rather than a firmly established single-gene disorder. (cruz2024kir2.1mutationsdifferentially pages 3-6, pupaza2023assessmentofsudden pages 9-11)

Variants include missense substitutions, small in-frame deletions, truncating variants, and splice defects. Reported pathogenic mechanisms include reduced channel conductance, impaired phosphatidylinositol-4,5-bisphosphate (**PIP2**) regulation, defective membrane trafficking, abnormal tetramer/channelosome behavior, and dominant-negative suppression of wild-type subunits. Examples studied functionally include p.Arg67Trp, p.Cys122Tyr, p.Ser136Phe, p.Gly215Asp, and p.Δ314–315. Variant classification must be performed at the individual-variant level under ACMG/AMP criteria; not every rare KCNJ2 variant is pathogenic. (cruz2024kir2.1mutationsdifferentially pages 3-6, macias2021dualdysfunctionof pages 1-6, cruz2024kir2.1mutationsdifferentially pages 20-22)

### Risk and environmental modifiers

There is no infectious, toxic, occupational, or inflammatory cause. Disease expression is genetic, but episodes are modified by potassium balance and behavior. Paralysis is commonly precipitated by rest after exercise, carbohydrate-rich meals, prolonged fasting, illness, stress, cold, and sleep; attacks may occur with low, normal, or high serum potassium. Arrhythmia can be aggravated by electrolyte disturbance and QT-prolonging medication. Expert reviews recommend avoiding QT-prolonging drugs, inhaled salbutamol when alternatives exist, and thiazide-induced hypokalemia. (statland2018reviewofthe pages 24-30)

Protective factors are preventive rather than genetically protective: stable electrolyte balance, individualized avoidance of attack triggers, regular cardiac surveillance, and prompt treatment of sustained arrhythmia. No reproducible protective allele, modifier gene, epigenetic protective state, or formal gene–environment interaction effect size is established.

## 3. Phenotypes

Expression is incomplete and highly variable, including within families. Hallmark manifestations usually begin during childhood or adolescence and are episodic rather than steadily progressive.

* **Periodic paralysis**—episodic flaccid limb weakness, typically lasting hours but sometimes longer; HPO suggestions: **Periodic paralysis**, **Episodic muscle weakness**, **Flaccid paralysis**. In a 15-person series, attacks occurred in 80% of males and 20% of females, illustrating both variability and the instability of estimates from small samples. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)
* **Ventricular ectopy/arrhythmia**—PVCs, bigeminy, couplets, nonsustained or sustained polymorphic and bidirectional VT; suggested HPO terms: **Ventricular premature beats**, **Bidirectional ventricular tachycardia**, **Polymorphic ventricular tachycardia**, **Syncope**. Reviews estimate ventricular arrhythmias in 60–90%, polymorphic VT in 48%, and bidirectional VT in 44%. (pupaza2023assessmentofsudden pages 9-11)
* **Repolarization morphology**—prominent U waves, broad T–U junction, prolonged Q–U interval, and sometimes modest QTc prolongation. Prominent U waves occurred in 84% of one cohort, whereas QTc was normal in 76%. Suggested HPO terms: **Prominent U wave**, **Abnormality of cardiac repolarization**. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)
* **Dysmorphism/developmental signs**—hypertelorism, low-set ears, broad forehead, small mandible/micrognathia, low hairline, short stature, clinodactyly, syndactyly, and sometimes scoliosis. Suggested HPO terms include **Hypertelorism**, **Micrognathia**, **Clinodactyly**, **Syndactyly**, **Short stature**, and **Scoliosis**. All 15 individuals in one selected molecular cohort had dysmorphism, but this should not be generalized as universal prevalence. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5)
* **Less consistent findings**—fixed myopathy, developmental or neuropsychiatric manifestations, seizures, and structural congenital heart disease have been reported but are not defining and require exclusion of independent causes.

Quality-of-life impairment derives from unpredictable weakness, falls, inability to exercise or work reliably, driving restrictions, anxiety about sudden death, medication adverse effects, and ICD shocks. Formal ATS-specific EQ-5D, SF-36, or PROMIS population norms were not identified. NCT00521794 collected prospective quality-of-life data, but the retrieved record did not provide published numerical results. (NCT00521794 chunk 1)

## 4. Genetic and molecular information

**KCNJ2** is the only firmly established major causal gene in the retrieved evidence. Variants are ordinarily **germline**, not somatic. Autosomal-dominant transmission implies a 50% transmission probability from a heterozygous parent, but clinical penetrance and organ involvement are incomplete. De novo disease occurs; parental testing is needed to distinguish inherited from de novo variants and to assess possible parental mosaicism.

Pathogenic variants are generally very rare or absent in population databases. Exact gnomAD/TOPMed frequencies should be retrieved by genomic coordinate and transcript because frequency cannot be assigned at the disease level. Copy-number analysis may be appropriate after negative sequencing, but recurrent aneuploidies, translocations, or large chromosomal abnormalities are not characteristic. No validated ATS methylation signature, repeat expansion, mitochondrial variant, or somatic driver has been established.

No modifier gene has yet reached routine clinical use. The 2024 hiPSC multi-omics study nominated **ZNF528**, **CTTN**, and **ATP1B1** as downstream regulatory/pathogenic nodes, but these are experimental candidates rather than proven Mendelian modifiers. (chen2024transcriptomeandopen pages 19-20)

## 5. Environmental information

ATS is neither infectious nor environmentally acquired and has no zoonotic component. Relevant non-genetic factors are attack or arrhythmia modifiers: exertion followed by rest, diet-related potassium shifts, dehydration, intercurrent illness, stress, and arrhythmogenic medication. Smoking and alcohol have no established disease-specific causal association, although general cardiovascular avoidance advice applies. Maintaining regular meals and hydration, avoiding known individual triggers, and correcting electrolyte abnormalities can reduce attacks; potassium should not be used blindly because ATS attacks may be hypo-, normo-, or hyperkalemic.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** heterozygous KCNJ2 loss-of-function or dominant-negative variant.
2. **Protein/channel defect:** reduced Kir2.1 surface expression, conductance, PIP2 sensitivity, or channel-complex integrity.
3. **Electrical consequence:** reduced I_K1 depolarizes resting membrane potential, impairs terminal repolarization, prolongs action potentials, reduces sodium-channel availability/conduction reserve, and facilitates triggered or re-entrant ventricular activity.
4. **Calcium-handling consequence:** experimental models place functional Kir2.1 in a sarcoplasmic-reticulum microdomain; mutant Kir2.1 disrupts intracellular Ca2+ homeostasis and promotes spontaneous Ca2+ release.
5. **Clinical outputs:** ventricular ectopy/VT in myocardium, episodic inexcitability and weakness in skeletal muscle, and congenital craniofacial/skeletal abnormalities from developmental Kir2.1 dysfunction. (macias2021dualdysfunctionof pages 1-6, cruz2024kir2.1mutationsdifferentially pages 20-22)

Suggested GO terms include **potassium ion transmembrane transport**, **regulation of membrane potential**, **cardiac muscle cell action potential**, **skeletal muscle contraction**, **calcium-ion homeostasis**, and **protein localization to plasma membrane**. Relevant cell types are **cardiomyocyte** and **skeletal muscle fiber/myocyte**; developmental effects probably involve osteogenic/chondrogenic lineages, although precise causal cell populations remain incompletely mapped.

### Molecular profiling and recent research

A peer-reviewed March 2024 study used patient hiPSC-derived cardiomyocytes, CRISPR-repaired isogenic controls, RNA sequencing, ATAC-seq, and proteomic/pathway analysis. Mutant cells had slower spontaneous beating, prolonged action potentials, and reduced Kir2.1 current. Seven potassium-related pathways were downregulated; ZNF528 remained suppressed from the cardiac mesoderm stage, and KCNJ2, CTTN, and ATP1B1 emerged as convergent targets. This is mechanistically important but not yet a validated clinical biomarker panel. [Published 2024-03; DOI: https://doi.org/10.1186/s12967-024-05125-7.] (chen2024transcriptomeandopen pages 19-20)

A December 2024 preprint combined literature-derived human outcomes, five mutation-specific mouse models, patient-specific iPSC cardiomyocyte optical mapping, and molecular docking. It found mutation-dependent effects of flecainide on I_K1, I_Na, conduction, rotor incidence, and access to a Kir2.1 Cys311 pharmacophore. These results support pharmacogenomic stratification, but their preprint status and retrospective clinical dataset require cautious interpretation. [Posted 2024-12; DOI: https://doi.org/10.1101/2024.12.10.24318629.] (cruz2024kir2.1mutationsdifferentially pages 20-22, cruz2024kir2.1mutationsdifferentially pages 1-3)

No validated ATS single-cell atlas, spatial transcriptomic map, metabolomic/lipidomic diagnostic signature, or large CRISPR-screen result was found.

## 7. Anatomical structures affected

Primary systems are:

* **Heart**, especially ventricular myocardium and the specialized conduction/repolarization system—suggested UBERON concepts: heart, ventricle, myocardium; CL: cardiomyocyte.
* **Skeletal muscle**—limb and axial muscle fibers; CL: skeletal muscle cell/myofiber.
* **Craniofacial skeleton, digits, and spine**—developmental abnormalities rather than degenerative tissue injury.

At the subcellular level, Kir2.1 acts at the **plasma membrane/sarcolemma** and, experimentally, a **sarcoplasmic-reticulum membrane microdomain**. Suggested GO cellular components are plasma membrane, sarcolemma, potassium-channel complex, and sarcoplasmic reticulum membrane. Effects are systemic/bilateral rather than characteristically lateralized. (macias2021dualdysfunctionof pages 1-6)

## 8. Temporal development

Congenital dysmorphism is present from birth, while weakness and arrhythmia commonly become evident in the first two decades; one review reported onset before age 19 in 42.3%. The disease is chronic and lifelong, but manifestations fluctuate. Paralytic attacks remit spontaneously or after electrolyte-directed treatment, whereas congenital morphology is stable. Cardiac ectopy may be persistent or episodic and does not necessarily parallel muscle symptoms. There is no recognized staging system, end-stage phase, or genetic anticipation. Childhood diagnosis is a critical opportunity for family screening, trigger education, and arrhythmia surveillance. (pupaza2023assessmentofsudden pages 9-11)

## 9. Inheritance and population

Estimated prevalence is approximately **1 per million**, although underdiagnosis is probable; reliable incidence and carrier-frequency estimates are unavailable. Disease occurs worldwide without a confirmed ethnic, geographic, founder, or consanguinity concentration. Because transmission is dominant, consanguinity is not a typical risk factor. (pupaza2023assessmentofsudden pages 9-11)

Penetrance is incomplete and expressivity markedly variable. Sex may modify the balance of cardiac and neuromuscular manifestations, but estimates remain vulnerable to ascertainment bias. In the small 2015 cohort, paralysis was more frequent in males while serious cardiac histories occurred in both sexes. A later meta-analysis suggested greater arrhythmic burden in females, but it was based on heterogeneous case reports and therefore does not establish a population sex ratio or prospective risk coefficient. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, garcia2026genderspecificcardiacfeatures pages 10-11)

## 10. Diagnostics

### Clinical and electrophysiologic evaluation

Diagnosis should integrate:

1. History of episodic weakness, triggers, family history, syncope, palpitations, seizure-like events, and sudden death.
2. Examination for characteristic craniofacial, digital, and skeletal signs.
3. Twelve-lead ECG emphasizing U waves, T–U morphology and Q–U as well as QTc.
4. Twenty-four-hour or longer ambulatory monitoring to quantify PVCs and VT; exercise testing may expose arrhythmia.
5. Serum potassium, magnesium, thyroid function, renal function, and creatine kinase during/around attacks to characterize physiology and exclude secondary paralysis.
6. Echocardiography or cardiac MRI to exclude structural disease; ATS is primarily electrical.
7. Long-exercise EMG testing when the genetic result is negative or uncertain.

A normal interictal neurological examination, normal serum potassium, or normal QTc does not exclude ATS. Annual 12-lead ECG and 24-hour Holter monitoring are recommended even for asymptomatic KCNJ2 carriers. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, statland2018reviewofthe pages 24-30)

### Genetic testing

Sequence **KCNJ2** with deletion/duplication analysis, either as single-gene testing when the phenotype is classic or as part of a curated periodic-paralysis/inherited-arrhythmia panel. Cascade testing should target the familial pathogenic variant. WES/WGS is appropriate for KCNJ2-negative, atypical, or syndromic cases, but may produce VUSs without proving ATS. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are not routine unless another diagnosis is suspected. RNA-seq and multi-omics remain research tools rather than validated diagnostics. (chen2024transcriptomeandopen pages 19-20, NCT00521794 chunk 1)

### Differential diagnosis

Important alternatives include hypokalemic and hyperkalemic periodic paralysis (**CACNA1S**, **SCN4A**), thyrotoxic paralysis, renal/gastrointestinal potassium loss, CPVT (**RYR2/CASQ2**), conventional long-QT syndromes, Brugada syndrome, short-QT syndrome, arrhythmogenic cardiomyopathy, digitalis toxicity, neurologic seizure, and functional episodic weakness. ATS is favored by the combination of dysmorphism, periodic weakness, prominent U waves, and bidirectional/polymorphic ventricular ectopy.

No population newborn screening is established. Cascade screening of first-degree relatives is the principal presymptomatic strategy.

## 11. Outcome and prognosis

ATS can cause considerable lifelong morbidity, but many affected individuals retain normal cardiac structure and near-normal function between attacks. Recurrent weakness causes falls, disability, and occupational limitations. Frequent ventricular ectopy may be asymptomatic or cause palpitations, syncope, tachycardia-induced cardiomyopathy, cardiac arrest, or sudden cardiac death.

A 2023 review cited a **5-year sudden-cardiac-death probability of 7.9%** and associated risk with prior syncope, sustained VT, micrognathia, and prolonged Tpeak–Tend; these estimates should be interpreted cautiously because ATS cohorts are small. In the selected 15-patient series, only 25% were clinically and electrocardiographically asymptomatic, and 50% of females and 60% of males had syncope/cardiac-arrest histories. No reliable disease-specific life-expectancy, 10-year survival, or mortality rate is available. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, pupaza2023assessmentofsudden pages 9-11)

## 12. Treatment and current implementation

There is no curative or universally effective therapy. Management should be coordinated between inherited-arrhythmia cardiology, neuromuscular neurology, clinical genetics, and rehabilitation.

### Paralysis

Acute treatment is guided by measured potassium and ECG monitoring. Oral potassium may help hypokalemic attacks but can be hazardous in normo-/hyperkalemic episodes. Preventive measures include trigger avoidance and individualized potassium management. Acetazolamide is commonly used empirically; response is variable and occasional worsening is reported. Dichlorphenamide and potassium-sparing diuretics have limited ATS-specific evidence. NCT00839501 randomized potassium 40 mEq twice daily and acetazolamide 250 mg twice daily against placebo but terminated after enrolling only three participants, so it did not establish efficacy. [ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT00839501.] (NCT00839501 chunk 1)

### Arrhythmia

Beta-blockers, flecainide, selected calcium-channel blockers, and amiodarone have been used. Older evidence suggested flecainide could reduce ventricular ectopy without syncope or cardiac arrest over a mean 23-month follow-up, but evidence was observational. Drugs that prolong QT or worsen hypokalemia should be avoided; lidocaine, mexiletine, propafenone, and quinidine may worsen neuromuscular symptoms in some patients. (statland2018reviewofthe pages 24-30)

The 2024 preprint review of 53 treated ATS1 cases found only partial response in 54%, ventricular-arrhythmia reduction in 23%, no efficacy in 23%, and nonfatal cardiac arrest in 13.5%. Mouse and iPSC results suggested that flecainide can worsen conduction and re-entry for some variants while benefiting others. This is an authoritative mechanistic warning but not yet sufficient to prohibit flecainide categorically; use should be specialist-supervised with ECG/Holter reassessment and attention to genotype. (cruz2024kir2.1mutationsdifferentially pages 38-39, cruz2024kir2.1mutationsdifferentially pages 20-22, cruz2024kir2.1mutationsdifferentially pages 1-3)

ICD implantation is appropriate for survivors of cardiac arrest and selected patients with sustained, drug-refractory life-threatening ventricular arrhythmia; indiscriminate primary-prevention implantation is undesirable because frequent self-terminating VT can cause inappropriate shocks. In one high-risk series, 40% received an ICD. Catheter ablation is not standard for diffuse polymorphic/bidirectional ectopy but may be considered for a dominant focus in exceptional cases. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5, pupaza2023assessmentofsudden pages 9-11)

Suggested NCIT intervention concepts include potassium supplementation, acetazolamide therapy, beta-adrenergic blockade, antiarrhythmic therapy, ambulatory ECG monitoring, physical therapy, and implantable cardioverter-defibrillator placement.

### Trials and advanced therapy

* **NCT00521794:** completed observational natural-history study, 28 participants, 2007–2012. [https://clinicaltrials.gov/study/NCT00521794] (NCT00521794 chunk 1)
* **NCT00839501:** terminated phase 1 potassium/acetazolamide crossover trial, three participants. [https://clinicaltrials.gov/study/NCT00839501] (NCT00839501 chunk 1)
* **NCT06205550:** planned randomized open-label N-of-1 crossover study, estimated 10 adults, comparing flecainide alone with flecainide plus a beta-blocker or calcium-channel blocker; primary outcome is ventricular-ectopy burden. The retrieved record listed it as not yet recruiting. [https://clinicaltrials.gov/study/NCT06205550] (NCT06205550 chunk 1)

No approved gene replacement, CRISPR, RNA, cell, or immunotherapy exists for ATS. The 2024 ZNF528/KCNJ2/CTTN/ATP1B1 work identifies experimental targets, not clinical treatments. (chen2024transcriptomeandopen pages 19-20)

## 13. Prevention

Primary prevention of a germline disorder is limited to reproductive options after genetic counseling: prenatal diagnosis or preimplantation genetic testing when a familial pathogenic variant is known. Predictive testing of minors is clinically actionable because surveillance and drug avoidance begin in childhood.

Secondary prevention comprises cascade testing, ECG/Holter surveillance, early recognition of weakness, and evaluation of apparent seizures or syncope for ventricular arrhythmia. Tertiary prevention includes individualized trigger avoidance, electrolyte management, medication review, rehabilitation/fall prevention, arrhythmia suppression, and ICD therapy for appropriately selected high-risk patients. There is no relevant vaccine, population screening program, infectious prophylaxis, or environmental public-health intervention. (statland2018reviewofthe pages 24-30, NCT00521794 chunk 1)

## 14. Other species and natural disease

No well-established, naturally occurring veterinary counterpart or breed-specific ATS syndrome was identified in the retrieved evidence. ATS is noninfectious and nontransmissible, with no zoonotic potential. **KCNJ2/Kir2.1 is evolutionarily conserved**, enabling cross-species functional study, but engineered phenocopies should not be labeled naturally occurring animal disease.

## 15. Model organisms and experimental systems

Engineered mice expressing human ATS variants are the principal whole-animal models. A Kir2.1Δ314–315 model recapitulated reduced I_K1 and I_Na, depolarized resting potential, prolonged action potentials, slower conduction, ventricular ectopy, abnormal Ca2+ release, and catecholamine-sensitive arrhythmia. Its strength is integrated cardiac physiology; limitations include species-specific repolarization and incomplete reproduction of human dysmorphism and periodic paralysis. (macias2021dualdysfunctionof pages 1-6)

The December 2024 study compared five cardiac-specific mutant models—Δ314–315, C122Y, G215D, R67W, and S136F. Flecainide or propafenone at 40 mg/kg produced variant-dependent ECG and arrhythmia effects; all but S136F showed increased ventricular-arrhythmia inducibility. These models are valuable for pharmacogenomic hypothesis generation but do not establish human dose–response or clinical safety. (cruz2024kir2.1mutationsdifferentially pages 1-3)

Patient-derived hiPSC cardiomyocytes and CRISPR-corrected isogenic controls reproduce reduced Kir2.1 current and prolonged action potentials and support transcriptomic, ATAC-seq, optical-mapping, and drug-response experiments. Their principal limitation is cardiomyocyte immaturity and low native I_K1 compared with adult ventricular cells. (cruz2024kir2.1mutationsdifferentially pages 20-22, chen2024transcriptomeandopen pages 19-20)

## Evidence appraisal and knowledge gaps

The central KCNJ2–Kir2.1–I_K1 causal model is supported by human genetics, electrophysiology, engineered mice, patient-derived cardiomyocytes, and isogenic correction. By contrast, prevalence, sex differences, treatment response rates, and sudden-death prediction remain imprecise because ATS is exceptionally rare and studies are small and referral-enriched. Important priorities are prospective international registries, systematic functional classification of KCNJ2 variants, genotype-stratified antiarrhythmic trials, validated patient-reported outcomes, and replication of the 2024 multi-omics and flecainide-pharmacogenomic findings. The retrieval system did not expose PMIDs for most cited records; DOI and ClinicalTrials.gov URLs are therefore provided rather than inventing PMID values.

References

1. (cruz2024kir2.1mutationsdifferentially pages 3-6): Francisco M. Cruz, Ana I. Moreno-Manuel, Sánchez Pérez Patricia, Juan Manuel Ruiz-Robles, Paula García Socuellamos, Lilian K. Gutiérrez, María Linarejos Vera-Pedrosa, Amaia Talavera Gutierrez, Gema Mondéjar Parreño, Álvaro Macías, Isabel Martínez-Carrascoso, Francisco J Bermúdez-Jiménez, Salvador Arias Santiago, Fernando Martínez de Benito, Aitana Braza-Boils, Carmen Valenzuela, CA Morillo, Esther Zorio, Juan Jiménez-Jaimez, and José Jalife. Kir2.1 mutations differentially increase the risk of flecainide proarrhythmia in andersen tawil syndrome. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.10.24318629, doi:10.1101/2024.12.10.24318629. This article has 1 citations.

2. (kostera‐pruszczyk2015andersen–tawilsyndromereport pages 4-5): Anna Kostera‐Pruszczyk, Anna Potulska‐Chromik, Piotr Pruszczyk, Katarzyna Bieganowska, Maria Miszczak‐Knecht, Piotr Bienias, krzysztof szczałuba, Hsien‐Yang Lee, Emily Quinn, Rafal Ploski, Anna Kaminska, and Louis J. Ptáček. Andersen–tawil syndrome: report of 3 novel mutations and high risk of symptomatic cardiac involvement. Muscle & Nerve, 51:192-196, Feb 2015. URL: https://doi.org/10.1002/mus.24293, doi:10.1002/mus.24293. This article has 28 citations and is from a peer-reviewed journal.

3. (pupaza2023assessmentofsudden pages 9-11): Adelina Pupaza, Eliza Cinteza, Corina Maria Vasile, Alin Nicolescu, and Radu Vatasescu. Assessment of sudden cardiac death risk in pediatric primary electrical disorders: a comprehensive overview. Diagnostics, 13:3551, Nov 2023. URL: https://doi.org/10.3390/diagnostics13233551, doi:10.3390/diagnostics13233551. This article has 7 citations.

4. (cruz2024kir2.1mutationsdifferentially pages 1-3): Francisco M. Cruz, Ana I. Moreno-Manuel, Sánchez Pérez Patricia, Juan Manuel Ruiz-Robles, Paula García Socuellamos, Lilian K. Gutiérrez, María Linarejos Vera-Pedrosa, Amaia Talavera Gutierrez, Gema Mondéjar Parreño, Álvaro Macías, Isabel Martínez-Carrascoso, Francisco J Bermúdez-Jiménez, Salvador Arias Santiago, Fernando Martínez de Benito, Aitana Braza-Boils, Carmen Valenzuela, CA Morillo, Esther Zorio, Juan Jiménez-Jaimez, and José Jalife. Kir2.1 mutations differentially increase the risk of flecainide proarrhythmia in andersen tawil syndrome. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.10.24318629, doi:10.1101/2024.12.10.24318629. This article has 1 citations.

5. (macias2021dualdysfunctionof pages 1-6): Álvaro Macías, Andrés González-Guerra, Ana I. Moreno-Manuel, Francisco M. Cruz, Nieves García-Quintáns, Lilian K. Gutiérrez, Marta Roche-Molina, Francisco Bermúdez-Jiménez, Vicente Andrés, María Linarejos Vera-Pedrosa, Isabel Martínez-Carrascoso, Juan A. Bernal, and José Jalife. Dual dysfunction of kir2.1 underlies conduction and excitation-contraction coupling defects promoting arrhythmias in a mouse model of andersen-tawil syndrome type 1. bioRxiv, Jun 2021. URL: https://doi.org/10.1101/2021.06.17.448833, doi:10.1101/2021.06.17.448833. This article has 1 citations.

6. (chen2024transcriptomeandopen pages 19-20): Peipei Chen, Junyu Long, Tianrui Hua, Zhifa Zheng, Ying Xiao, Lianfeng Chen, Kang Yu, Wei Wu, and Shuyang Zhang. Transcriptome and open chromatin analysis reveals the process of myocardial cell development and key pathogenic target proteins in long qt syndrome type 7. Journal of Translational Medicine, Mar 2024. URL: https://doi.org/10.1186/s12967-024-05125-7, doi:10.1186/s12967-024-05125-7. This article has 1 citations and is from a peer-reviewed journal.

7. (cruz2024kir2.1mutationsdifferentially pages 20-22): Francisco M. Cruz, Ana I. Moreno-Manuel, Sánchez Pérez Patricia, Juan Manuel Ruiz-Robles, Paula García Socuellamos, Lilian K. Gutiérrez, María Linarejos Vera-Pedrosa, Amaia Talavera Gutierrez, Gema Mondéjar Parreño, Álvaro Macías, Isabel Martínez-Carrascoso, Francisco J Bermúdez-Jiménez, Salvador Arias Santiago, Fernando Martínez de Benito, Aitana Braza-Boils, Carmen Valenzuela, CA Morillo, Esther Zorio, Juan Jiménez-Jaimez, and José Jalife. Kir2.1 mutations differentially increase the risk of flecainide proarrhythmia in andersen tawil syndrome. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.10.24318629, doi:10.1101/2024.12.10.24318629. This article has 1 citations.

8. (statland2018reviewofthe pages 24-30): Jeffrey M. Statland, Bertrand Fontaine, Michael G. Hanna, Nicholas E. Johnson, John T. Kissel, Valeria A. Sansone, Perry B. Shieh, Rabi N. Tawil, Jaya Trivedi, Stephen C. Cannon, and Robert C. Griggs. Review of the diagnosis and treatment of periodic paralysis. Muscle & Nerve, 57:522-530, Nov 2018. URL: https://doi.org/10.1002/mus.26009, doi:10.1002/mus.26009. This article has 329 citations and is from a peer-reviewed journal.

9. (NCT00521794 chunk 1): Robert Griggs, MD. Characteristics of Andersen-Tawil Syndrome. University of Rochester. 2007. ClinicalTrials.gov Identifier: NCT00521794

10. (NCT00839501 chunk 1): Robert Griggs, MD. Effect of Potassium and Acetazolamide on People With Andersen-Tawil Syndrome. University of Rochester. 2008. ClinicalTrials.gov Identifier: NCT00839501

11. (NCT06205550 chunk 1): Christian van der Werf. N-of-1 in ATS and MEPPC. Academisch Medisch Centrum - Universiteit van Amsterdam (AMC-UvA). 2025. ClinicalTrials.gov Identifier: NCT06205550

12. (garcia2026genderspecificcardiacfeatures pages 10-11): Alan Garcia, Abdul Mueez Alam Kayani, Ricky Lemus-Zamora, Daniel Alejandro Navarro-Martinez, Eduardo Tellez-Garcia, Richard Salama-Frisbie, Jorge Gomez Flores, Eduardo Aviles, and Brijesh Patel. Gender-specific cardiac features in andersen–tawil syndrome: a comprehensive meta-analysis of case reports and series. Journal of Interventional Cardiac Electrophysiology, Jan 2026. URL: https://doi.org/10.1007/s10840-026-02237-6, doi:10.1007/s10840-026-02237-6. This article has 1 citations and is from a peer-reviewed journal.

13. (cruz2024kir2.1mutationsdifferentially pages 38-39): Francisco M. Cruz, Ana I. Moreno-Manuel, Sánchez Pérez Patricia, Juan Manuel Ruiz-Robles, Paula García Socuellamos, Lilian K. Gutiérrez, María Linarejos Vera-Pedrosa, Amaia Talavera Gutierrez, Gema Mondéjar Parreño, Álvaro Macías, Isabel Martínez-Carrascoso, Francisco J Bermúdez-Jiménez, Salvador Arias Santiago, Fernando Martínez de Benito, Aitana Braza-Boils, Carmen Valenzuela, CA Morillo, Esther Zorio, Juan Jiménez-Jaimez, and José Jalife. Kir2.1 mutations differentially increase the risk of flecainide proarrhythmia in andersen tawil syndrome. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.10.24318629, doi:10.1101/2024.12.10.24318629. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Andersen-Tawil_Syndrome-deep-research-falcon_artifacts/artifact-00.md)