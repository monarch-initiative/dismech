---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T16:56:17.334004'
end_time: '2026-07-31T17:06:25.282642'
duration_seconds: 607.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bethlem myopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Bethlem_Myopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bethlem myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bethlem myopathy** covering all of the
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
- **Disease Name:** Bethlem myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bethlem myopathy** covering all of the
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


# Bethlem Myopathy: Disease Characteristics Research Report

**Scope and evidence basis.** This report treats Bethlem myopathy (BM) as the mild end of the collagen-VI-related dystrophy (COL6-RD) spectrum. Evidence is primarily aggregated disease-level literature, specialist cohorts, family studies, experimental models, and ClinicalTrials.gov records—not routine EHR-derived data. Exact HPO/GO/CL/UBERON accessions should be validated against the current ontology release before database import; names below are suggested mappings.

## Executive summary

Bethlem myopathy is a rare, chronic Mendelian muscle/connective-tissue disorder caused by pathogenic variants in **COL6A1, COL6A2, or COL6A3**. It is usually autosomal dominant but can be recessive. The characteristic combination is slowly progressive axial/proximal weakness, early distal laxity followed by contractures—particularly long finger flexors, elbows, ankles, knees, and neck—and variably abnormal skin. Ambulation is generally retained into adulthood, although meaningful weakness, wheelchair use, and restrictive respiratory disease occur in a subset. Cardiac involvement is not a usual primary feature. Open Targets recognizes all three genes as associated with MONDO:0008029 (OpenTargets Search: Bethlem myopathy-COL6A1,COL6A2,COL6A3).

No approved disease-modifying treatment exists. Current practice is multidisciplinary supportive management, especially contracture prevention, mobility preservation, respiratory surveillance, and noninvasive ventilation when indicated. Experimental approaches target defective autophagy/mitophagy, mitochondrial permeability-transition-pore dysfunction, abnormal extracellular-matrix signaling, or the causal allele.

| Domain | High-value entry | Suggested ontology/identifier | Evidence/notes |
|---|---|---|---|
| Disease definition | Bethlem myopathy; mild end of the collagen VI-related dystrophy/myopathy spectrum with slowly progressive muscle weakness and contractures | MONDO:0008029; OMIM:158810; suggested disease family: collagen VI-related dystrophy | Human disease-level resources and cohorts support BM as a COL6-related disorder with axial/proximal weakness, contractures, distal laxity, and possible respiratory involvement (merlini2023newclinicaland pages 1-2, bonnemann2011thecollagenvirelateda pages 1-2, zanotti2023extracellularmatrixdisorganization pages 1-2) |
| Synonyms | Bethlem myopathy (BM); Bethlem muscular dystrophy; collagen VI-related myopathy, Bethlem phenotype | Suggested text synonyms only | BM is used consistently in clinical and mechanistic literature; nomenclature often placed within COL6-RM/COL6-RD spectrum (merlini2023newclinicaland pages 1-2, zanotti2023extracellularmatrixdisorganization pages 1-2) |
| Disease evidence granularity | Aggregated disease-level knowledge plus individual-patient and cohort evidence | Suggested evidence model: disease-level + human cohort + case-level | Current understanding comes from aggregated reviews plus single-center cohorts and family reports, not EHR-derived population studies (merlini2023newclinicaland pages 14-15, bonnemann2011thecollagenvirelateda pages 1-2) |
| Causal genes | COL6A1, COL6A2, COL6A3 | HGNC gene symbols; Open Targets disease-target support for Bethlem myopathy | Strong gene-disease association across multiple evidence sources; collagen VI microfibril defects are causal (OpenTargets Search: Bethlem myopathy-COL6A1,COL6A2,COL6A3, merlini2023newclinicaland pages 1-2, zanotti2023extracellularmatrixdisorganization pages 1-2) |
| Inheritance | Usually autosomal dominant; recessive forms also reported in collagen VI-related myopathy spectrum including Bethlem presentations | Suggested HPO inheritance terms: Autosomal dominant inheritance; Autosomal recessive inheritance | Foundational review describes classic AD BM; more recent genetic literature and cohorts show both dominant and recessive mechanisms in COL6 disease spectrum (bonnemann2011thecollagenvirelateda pages 1-2, zanotti2023extracellularmatrixdisorganization pages 1-2) |
| Representative pathogenic variant classes | Missense (including glycine substitutions in triple-helical domain), splice-site/intronic, exon-skipping, small deletions, CNVs, dominant-negative assembly-competent variants, biallelic loss-of-function alleles | Suggested sequence ontology names only: missense_variant, splice_donor_variant, intron_variant, inframe_deletion, copy_number_variant | Standard sequencing may miss intronic/CNV events; fibroblast/RNA studies help resolve splicing and secretion defects (bonnemann2011thecollagenvirelateda pages 14-15, zanotti2023extracellularmatrixdisorganization pages 1-2) |
| Molecular defect | Defective collagen VI assembly/secretion and extracellular microfibril network organization | Suggested GO/CC: extracellular matrix; collagen-containing extracellular matrix | Collagen VI chains assemble into monomers, dimers, tetramers, then extracellular microfibrils; mutations disrupt matrix organization and cell-matrix integrity (castagnaro2018extracellularcollagenvi pages 10-14, zanotti2023extracellularmatrixdisorganization pages 1-2, mohassel2023collagentypevi pages 1-6) |
| Hallmark phenotype | Axial and proximal muscle weakness | Suggested HPO: proximal muscle weakness; axial muscle weakness | Core phenotype across reviews and cohorts; BM patients remain ambulant into adulthood by definition in one 2023 cohort (merlini2023newclinicaland pages 1-2) |
| Hallmark phenotype | Finger flexor/interphalangeal contractures | Suggested HPO: flexion contracture of finger; camptodactyly-like term if locally used | Long finger flexor contractures are a classic clue and help distinguish from some differentials (bonnemann2011thecollagenvirelateda pages 6-7, bonnemann2011thecollagenvirelateda pages 12-14) |
| Hallmark phenotype | Elbow, knee, ankle, neck contractures; rigid spine in some patients | Suggested HPO: elbow contracture; knee flexion contracture; ankle contracture; neck flexion contracture; rigid spine | Contractures are often progressive and may outweigh weakness in some phenotypic variants (merlini2023newclinicaland pages 1-2, bonnemann2011thecollagenvirelateda pages 6-7, zanotti2023extracellularmatrixdisorganization pages 1-2) |
| Hallmark phenotype | Distal joint laxity / hyperlaxity, especially earlier in life | Suggested HPO: distal joint hypermobility | Early laxity transitioning to later contractures is part of classic natural history (bonnemann2011thecollagenvirelateda pages 1-2, bonnemann2011thecollagenvirelateda pages 6-7) |
| Hallmark phenotype | Skin changes | Suggested HPO terms by use-case: abnormal skin morphology; keloid tendency; follicular hyperkeratosis | Skin involvement is recognized in collagen VI disorders and can aid differential diagnosis (merlini2023newclinicaland pages 1-2, bonnemann2011thecollagenvirelateda pages 12-14) |
| Respiratory phenotype | Restrictive respiratory involvement; risk of nocturnal hypoventilation/respiratory insufficiency | Suggested HPO: restrictive ventilatory defect; respiratory insufficiency; sleep hypoventilation | In 2023 cohort, 45% of BM had FVC <70% predicted; restrictive pattern reported in 2023 variant cohort; monitoring is recommended (merlini2023newclinicaland pages 14-15, zanotti2023extracellularmatrixdisorganization pages 2-3, bonnemann2011thecollagenvirelateda pages 6-7) |
| Cardiac phenotype | Cardiac involvement uncommon/rare | Suggested HPO: cardiomyopathy only when present | Cardiac function was normal in all patients of one 2023 COL6 cohort; historical review notes only rare coincidental findings (zanotti2023extracellularmatrixdisorganization pages 2-3, bonnemann2011thecollagenvirelateda pages 6-7) |
| Onset / course | Prenatal-to-adult onset; often childhood or adolescence; slowly progressive; weakness may be stable/improve in puberty then worsen later | Suggested HPO onset/course labels: congenital onset; childhood onset; adult onset; progressive | Reviews and 2023 cohorts support broad onset window and slow progression; some older adults require walking aids (merlini2023newclinicaland pages 1-2, bonnemann2011thecollagenvirelateda pages 6-7) |
| Epidemiology | Rare disease; prevalence estimate 0.77 per 100,000 reported from Newcastle dataset | Suggested epidemiology note only | Widely cited historical prevalence estimate; contemporary global prevalence/incidence remain uncertain (bonnemann2011thecollagenvirelateda pages 1-2) |
| Functional statistics | In 33 BM patients, only one-third had knee extension strength >50% predicted; only one-tenth had elbow flexion >50% predicted | Suggested measurement terms only | Useful contemporary quantitative severity anchors from 2023 single-center cohort (merlini2023newclinicaland pages 1-2) |
| Mobility prognosis | Ambulation usually preserved into adulthood, but wheelchair use can occur | Suggested HPO: impaired ambulation; wheelchair dependence | 2023 cohort reported 15% of BM patients used wheelchairs, higher than historic pre-gene-discovery series (merlini2023newclinicaland pages 14-15) |
| Primary anatomy affected | Skeletal muscle, especially limb-girdle/axial musculature | Suggested UBERON: skeletal muscle tissue; limb muscle; trunk muscle | BM is primarily a musculoskeletal/connective tissue disorder affecting muscle function and surrounding ECM (merlini2023newclinicaland pages 1-2, castagnaro2018extracellularcollagenvi pages 10-14) |
| Secondary anatomy affected | Tendons, joint capsules, fascia, diaphragm, skin | Suggested UBERON names only: tendon, joint capsule, muscle fascia, diaphragm, skin | Contractures and restrictive pulmonary disease implicate periarticular connective tissue and diaphragm/chest wall mechanics (bonnemann2011thecollagenvirelateda pages 6-7, bonnemann2011thecollagenvirelateda pages 12-14) |
| Relevant cell types | Muscle fibroblasts / fibroadipogenic precursor-like stromal cells; skeletal myofibers; satellite cells | Suggested CL names only: fibroblast, skeletal muscle fiber cell, satellite cell | Collagen VI is produced largely by fibroblastic interstitial cells rather than myofibers; disease is partly non-cell-autonomous and affects satellite-cell reserve (mohassel2023collagentypevi pages 38-41, mohassel2023collagentypevi pages 1-6) |
| Subcellular/localization | Endoplasmic reticulum (assembly), sarcolemma-ECM interface, mitochondria, autophagosome/lysosome system | Suggested GO cellular component names only | Pathophysiology spans collagen assembly, ECM anchorage, mitochondrial pore dysregulation, and autophagy/mitophagy defects (castagnaro2018extracellularcollagenvi pages 10-14, bernardi2013mitochondrialdysfunctionand pages 1-2) |
| Core mechanism | ECM disorganization and impaired collagen VI microfibril network compromise mechanical stability and signaling | Suggested GO: extracellular matrix organization; cell-matrix adhesion | Supported by 2023 pathology study showing ECM disorganization and sarcolemmal alterations (zanotti2023extracellularmatrixdisorganization pages 1-2, zanotti2023extracellularmatrixdisorganization pages 2-3) |
| Core mechanism | Mitochondrial permeability transition pore dysregulation with latent mitochondrial dysfunction and apoptosis | Suggested GO: regulation of mitochondrial membrane permeability; intrinsic apoptotic signaling pathway | Major established disease mechanism from mouse and human studies; targetable by cyclophilin/PTP inhibition (bernardi2013mitochondrialdysfunctionand pages 1-2, merlini2023newclinicaland pages 1-2) |
| Core mechanism | Defective autophagy/mitophagy with accumulation of dysfunctional organelles | Suggested GO: autophagy; mitophagy; macroautophagy | A central conserved mechanism across Col6-null mice and patient tissue/fibroblasts (castagnaro2018extracellularcollagenvi pages 10-14, bernardi2013mitochondrialdysfunctionand pages 1-2) |
| Core mechanism | AKT-mTOR pathway activation associated with impaired autophagic flux | Suggested GO/pathway names only: AKT signaling; mTOR signaling | Demonstrated in Col6a1-null fibroblasts as part of autophagy dysregulation (castagnaro2018extracellularcollagenvi pages 10-14) |
| Core mechanism | Reduced satellite-cell self-renewal / regeneration defects | Suggested GO: skeletal muscle satellite cell activation; muscle regeneration | Relevant downstream mechanism in collagen VI deficiency models (mohassel2023collagentypevi pages 6-10, mohassel2023collagentypevi pages 38-41) |
| Emerging mechanism (2023) | Altered TGF-beta bioavailability in collagen VI-deficient skeletal muscle ECM | Suggested GO/pathway name only: transforming growth factor beta signaling pathway | 2023 preprint proposes early TGF-beta dysregulation as an upstream matrix-signaling defect; emerging, not yet fully settled (mohassel2023collagentypevi pages 6-10, mohassel2023collagentypevi pages 1-6) |
| Molecular profiling | Deep RNA profiling identified CLOCK/molecular clock signatures in collagen VI myopathy | Suggested pathway/process names only: circadian rhythm; transcriptional dysregulation | Evidence is from broader collagen VI myopathy work rather than BM-only cohorts (castagnaro2018extracellularcollagenvi pages 10-14) |
| Serum/lab testing | CK often normal to mildly elevated, though higher values can occur in congenital/severe cases | Suggested lab descriptor only | 2023 series reported CK 2-10× in many, normal in some, and a markedly elevated congenital case (zanotti2023extracellularmatrixdisorganization pages 2-3) |
| Electrophysiology | EMG typically supportive of myopathy rather than diagnostic | Suggested test term only: electromyography | Specific quantitative EMG data were not well captured in retrieved evidence; use as supportive test, not defining biomarker (bonnemann2011thecollagenvirelateda pages 12-14) |
| Imaging | Muscle MRI pattern with perifascial fatty/connective-tissue replacement, notably rectus femoris and vastus lateralis; ultrasound 'central cloud' sign in rectus femoris | Suggested RadLex/ontology names only: muscle MRI; muscle ultrasonography | Pattern-recognition imaging supports diagnosis and differential diagnosis (bonnemann2011thecollagenvirelateda pages 12-14) |
| Biopsy/pathology | Variable dystrophic/myopathic changes; fiber size variability/disproportion, internal nuclei, interstitial fibrosis, relatively scarce necrosis | Suggested pathology terms only | 2023 pathology cohort confirmed ECM disorganization and variable collagen VI distribution (zanotti2023extracellularmatrixdisorganization pages 1-2, zanotti2023extracellularmatrixdisorganization pages 2-3) |
| Protein studies | Collagen VI immunofluorescence/immunohistochemistry on muscle biopsy or fibroblasts | Suggested assay term only | Can correlate with severity, but may be near-normal in milder BM; serial biopsies may show age-related increase in expression (merlini2023newclinicaland pages 1-2, bonnemann2011thecollagenvirelateda pages 12-14) |
| Cellular diagnostics | Dermal fibroblast culture with collagen VI secretion/deposition analysis; RT-PCR for splicing defects | Suggested assay terms only | Especially useful when genomic sequencing is negative or variant interpretation is uncertain (bonnemann2011thecollagenvirelateda pages 14-15) |
| Molecular testing strategy | First-line NGS panel or exome-based testing of COL6A1/COL6A2/COL6A3; add RNA studies and CNV analysis when needed | Suggested testing stack only: gene panel, WES, RNA analysis, MLPA/SNP array/CGH | Standard sequencing misses some intronic and copy-number defects; deep intronic COL6A2 mutation detected by custom CGH with RNA confirmation (bonnemann2011thecollagenvirelateda pages 14-15) |
| Differential diagnosis | Emery-Dreifuss muscular dystrophy, limb-girdle muscular dystrophies, other congenital muscular dystrophies/connective-tissue myopathies | Suggested MONDO/HPO names only | Finger flexor contractures plus skin features and characteristic imaging favor collagen VI disease (bonnemann2011thecollagenvirelateda pages 12-14) |
| Surveillance | Regular respiratory function testing, sleep studies when indicated, orthopedic/contracture/scoliosis monitoring, strength and mobility assessment | Suggested clinical care concepts only | Restrictive respiratory disease may emerge despite relatively mild limb weakness; contractures are progressive (bonnemann2011thecollagenvirelateda pages 6-7, bonnemann2011thecollagenvirelateda pages 14-15) |
| Supportive management | Stretching, physiotherapy, dynamic splinting, orthotics, mobility aids | Suggested NCIT-style terms: Physical Therapy; Splinting; Orthotic Device Use | Mainstay care is supportive and multidisciplinary; progression rarely fully stops (bonnemann2011thecollagenvirelateda pages 14-15) |
| Orthopedic interventions | Achilles tendon release/selective contracture surgery; scoliosis bracing/surgery in selected cases | Suggested NCIT-style terms: Tendon Release Surgery; Orthopedic Surgical Procedure; Spinal Bracing | Surgery may preserve ambulation in some BM patients but recurrence of contracture is common (bonnemann2011thecollagenvirelateda pages 14-15) |
| Respiratory management | Noninvasive ventilation when needed; pulmonary monitoring | Suggested NCIT-style terms: Noninvasive Ventilation; Pulmonary Function Test | Respiratory compromise is less severe than UCMD on average but clinically important in a substantial subset (merlini2023newclinicaland pages 14-15, bonnemann2011thecollagenvirelateda pages 6-7) |
| Pharmacologic/targeted management status | No approved disease-modifying therapy specific for BM | Suggested status label only | Reviews and 2023 papers still state no effective curative therapy is available; translational options are under study (merlini2023newclinicaland pages 1-2, castagnaro2018extracellularcollagenvi pages 10-14) |
| Experimental therapy | Cyclosporin A / cyclophilin inhibition to normalize mitochondrial dysfunction and apoptosis | Suggested NCIT-style terms: Cyclosporine; Mitochondrial Permeability Transition Pore Inhibition | Supported by human proof-of-concept and animal studies, but not established standard-of-care disease modification (merlini2023newclinicaland pages 1-2, bernardi2013mitochondrialdysfunctionand pages 1-2) |
| Experimental therapy | Low-protein diet to activate autophagy | Suggested NCIT-style terms: Dietary Intervention; Low Protein Diet | Phase II pilot enrolled 8 adults with collagen VI-related myopathies; aimed to increase Beclin 1/autophagy markers (NCT01438788 chunk 1) |
| Experimental therapy | Pterostilbene/autophagy induction; splice correction; CRISPR allele-specific editing | Suggested NCIT-style terms: Nutraceutical Therapy; Splice-Switching Therapy; CRISPR-Cas Gene Editing | Preclinical/experimental only; 2024 fibroblast CRISPR study restored extracellular collagen VI network in UCMD cells, conceptually relevant across dominant COL6 disease (castagnaro2018extracellularcollagenvi pages 10-14) |
| Prevention / genetic counseling | Cascade testing, reproductive counseling, prenatal diagnosis possible once familial variant/mechanism known | Suggested concepts only: genetic counseling; prenatal testing; family screening | Especially important given frequent dominant inheritance and intrafamilial variability (bonnemann2011thecollagenvirelateda pages 14-15, bonnemann2011thecollagenvirelateda pages 1-2) |
| Trial / registry | NCT01438788 – Low Protein Diet in Patients With Collagen VI Related Myopathies; Phase II; completed; enrollment 8 | ClinicalTrials.gov: NCT01438788 | Open-label pilot of normocaloric low-protein diet (0.6-0.8 g/kg/day) to reactivate autophagy (NCT01438788 chunk 1) |
| Trial / imaging | NCT03693898 – MR in Patients With Collagen VI Related Myopathies; recruiting/interventional diagnostic; enrollment 20 | ClinicalTrials.gov: NCT03693898 | MRI Dixon fat fraction plus strength testing in confirmed Bethlem/Ulrich disease (NCT03693898 chunk 1) |
| Trial / registry | NCT04020159 – Global Registry for COL6-related Dystrophies; observational prospective registry; target enrollment 1000 | ClinicalTrials.gov: NCT04020159 | Annual questionnaire-based global registry collecting genetics, motor/respiratory function, QoL, pain, imaging and hospitalization data; useful for trial readiness (NCT04020159 chunk 1) |
| Other relevant study | NCT01403402 – Congenital Muscle Disease Study of Patient and Family Reported Medical Information | ClinicalTrials.gov: NCT01403402 | Broader congenital muscle disease registry relevant for patient-reported natural history, though not BM-specific in retrieved evidence (OpenTargets Search: Bethlem myopathy-COL6A1,COL6A2,COL6A3) |
| Model organism | Col6a1-null mouse | Suggested model name only | Recapitulates mild myopathic phenotype, mitochondrial dysfunction, apoptosis, defective autophagy; useful for therapy testing but milder than severe human disease (castagnaro2018extracellularcollagenvi pages 10-14, bernardi2013mitochondrialdysfunctionand pages 1-2) |
| Model organism | Col6a2-null mouse (2023 characterization) | Suggested model name only | Shows early postnatal atrophy/weakness, mild dystrophic changes, impaired regeneration, sarcolemmal fragility, and emerging TGF-beta dysregulation (mohassel2023collagentypevi pages 6-10, mohassel2023collagentypevi pages 1-6) |
| Model organism | Zebrafish col6a1 exon-targeted morphants | Suggested model name only | Exon 13 perturbation produced a milder BM-like phenotype; CsA improved motor deficits in severe UCMD-like model (telfer2010zebrafishmodelsof pages 1-2) |
| Cellular model | Patient dermal fibroblasts / myoblasts | Suggested model name only | Widely used for diagnostic secretion/deposition assays and mechanistic studies of autophagy and mitochondrial defects (castagnaro2018extracellularcollagenvi pages 10-14, bonnemann2011thecollagenvirelateda pages 14-15) |
| Gene-editing model | CRISPR-corrected patient fibroblasts restoring collagen VI microfilament network | Suggested model/intervention name only | 2024 proof-of-principle in dominant COL6A1 UCMD fibroblasts supports translational feasibility of allele-targeted editing for COL6 disorders (castagnaro2018extracellularcollagenvi pages 10-14) |
| Knowledge gaps | Contemporary population prevalence, penetrance estimates, formal QoL datasets, and validated prognostic biomarkers remain limited for BM specifically | Suggested curation flag only | Evidence base remains dominated by specialist cohorts and mixed-spectrum COL6 studies rather than large prospective BM-only studies (merlini2023newclinicaland pages 14-15, NCT04020159 chunk 1) |


*Table: This compact table summarizes the most actionable Bethlem myopathy knowledge-base elements across identifiers, genes, phenotypes, mechanisms, diagnosis, management, trials, and models. It is designed for rapid curation and highlights where exact ontology IDs are suggested versus where only ontology names are appropriate.*

## 1. Disease information

### Definition and nomenclature

BM is a relatively mild, slowly progressive collagen-VI-related myopathy characterized by axial and proximal weakness, contractures, distal joint laxity, and skin manifestations. Onset can range from prenatal life to adulthood; retention of walking into adult life is often used as an operational distinction from intermediate and Ullrich phenotypes (merlini2023newclinicaland pages 1-2).

**Identifiers and synonyms**

- **MONDO:** MONDO:0008029.
- **OMIM/MIM:** 158810.
- **Orphanet:** Bethlem myopathy is represented within Orphanet’s collagen-VI-related disease nomenclature; the exact current ORPHA accession should be verified before ingestion.
- **MeSH:** generally indexed through *Muscular Diseases*, *Muscular Dystrophies*, and collagen type VI rather than a consistently used BM-specific descriptor.
- **ICD-10:** no specific BM code; commonly mapped to congenital/hereditary myopathy or muscular-dystrophy categories according to local coding rules.
- **ICD-11:** map under congenital myopathy/muscular dystrophy; a dedicated universally implemented BM code was not established in the retrieved evidence.
- **Synonyms:** Bethlem myopathy, Bethlem muscular dystrophy, collagen VI-related myopathy—Bethlem phenotype, mild collagen VI-related dystrophy.

BM was described in 1976 as an autosomal-dominant early-onset “benign” myopathy with contractures; causal collagen-VI variants were identified during 1996–1998. “Benign” is now discouraged because respiratory and functional morbidity may be substantial (bonnemann2011thecollagenvirelateda pages 1-2).

## 2. Etiology, risk, and protective factors

### Causal factors

The primary cause is a **germline pathogenic variant** in **COL6A1, COL6A2, or COL6A3**, genes encoding the α1(VI), α2(VI), and α3(VI) chains of collagen VI. Pathogenic mechanisms include monoallelic assembly-competent variants producing dominant-negative microfibrils and biallelic loss-of-function, splice, or structural variants that reduce or abolish collagen production. Both dominant and recessive molecular defects are established across the spectrum (OpenTargets Search: Bethlem myopathy-COL6A1,COL6A2,COL6A3, zanotti2023extracellularmatrixdisorganization pages 1-2, mohassel2023collagentypevi pages 1-6).

### Genetic risk factors

Risk is determined principally by inheriting or acquiring a pathogenic COL6 allele. Relevant variant classes include glycine substitutions in the triple-helical region, missense variants, exon-skipping splice variants, nonsense/frameshift alleles, in-frame deletions, deep-intronic variants, and copy-number changes. Dominant-negative variants near the amino-terminal portion of the triple helix can interfere with assembly; biallelic null alleles generally reduce chain availability. Examples described in the literature include dominant **COL6A1 p.Lys121Arg** and **COL6A2 p.Asp630Asn**, although any individual variant requires contemporary ACMG/AMP and ClinVar review (bonnemann2011thecollagenvirelateda pages 6-7).

Variant frequencies are usually extremely low or absent in population databases because BM is rare and pathogenic alleles are family-specific. No single population allele frequency should be generalized. Variant-level gnomAD frequency, ClinVar assertions, segregation, RNA effect, and collagen secretion/deposition should be curated separately.

### Environmental, lifestyle, infectious, and protective factors

There is no evidence that toxin, infection, smoking, alcohol, diet, occupation, radiation, sex, or another environmental exposure causes BM. Activity, nutrition, respiratory infection, surgery, immobilization, and weight may alter functional burden or complications but do not create the disease. No validated genetic protective allele, modifier gene, diet, medication, or exposure prevents penetrance. Apparent gene–environment effects are therefore best framed as **modification of functional reserve**, not causation. Avoiding prolonged immobility, maintaining safe activity, and prompt respiratory care are tertiary prevention measures, not primary protection.

## 3. Phenotypes

### Musculoskeletal manifestations

- **Axial and proximal weakness:** usually mild-to-moderate early, chronic and slowly progressive; pelvic-girdle, shoulder-girdle, neck, and trunk muscles are prominent. Suggested HPO: *Proximal muscle weakness*, *Axial muscle weakness*, *Muscular hypotonia* when present.
- **Contractures:** long finger flexors/interphalangeal joints are particularly characteristic; elbows, Achilles tendons/ankles, knees, hips, neck, and spine may be involved. Suggested HPO: *Flexion contracture of finger*, *Elbow flexion contracture*, *Knee flexion contracture*, *Achilles tendon contracture*, *Rigid spine* (merlini2023newclinicaland pages 1-2, bonnemann2011thecollagenvirelateda pages 6-7).
- **Distal hyperlaxity:** often more evident in childhood and may transition to contracture with age. Suggested HPO: *Distal joint hypermobility* (bonnemann2011thecollagenvirelateda pages 1-2).
- **Motor delay, difficulty running/climbing stairs/rising, and reduced endurance:** variable; walking is usually achieved and retained into adulthood.
- **Scoliosis/kyphosis and rigid spine:** less severe than in classic Ullrich disease but clinically relevant in some patients.
- **Myopathic facies/ptosis:** occasional rather than defining. In one mixed 15-patient COL6 cohort, rigid spine occurred in four and myopathic face with ptosis in three (zanotti2023extracellularmatrixdisorganization pages 2-3).

Contemporary quantitative evidence shows that “mild” does not mean trivial. In a 2023 cohort of 33 BM patients, only one-third retained knee-extension strength above 50% predicted and only one-tenth retained elbow-flexion strength above 50%. Forty-five percent had FVC below 70% predicted, and 15% used wheelchairs (merlini2023newclinicaland pages 14-15, merlini2023newclinicaland pages 1-2).

### Respiratory manifestations

Restrictive impairment results from respiratory-muscle/diaphragmatic weakness and chest-wall stiffness. Nocturnal hypoventilation, sleep-disordered breathing, ineffective cough, and eventual respiratory insufficiency can occur, although ventilator dependence is much less common than in Ullrich disease. Suggested HPO: *Restrictive ventilatory defect*, *Respiratory insufficiency*, *Sleep hypoventilation*. A 2023 mixed COL6 cohort found restrictive respiratory involvement in 6/15 patients, including two severe cases; one had obstructive sleep apnea (zanotti2023extracellularmatrixdisorganization pages 2-3). Historical expert analysis recommends pulmonary function and sleep monitoring even when limb weakness appears mild (bonnemann2011thecollagenvirelateda pages 6-7).

### Skin and connective-tissue manifestations

Follicular hyperkeratosis, abnormal scarring/keloids, soft or velvety skin, and other subtle connective-tissue changes may occur. Skin findings support a COL6 diagnosis and help distinguish it from Emery–Dreifuss muscular dystrophy. Suggested HPO: *Follicular hyperkeratosis*, *Keloids*, *Abnormality of skin morphology* (bonnemann2011thecollagenvirelateda pages 12-14).

### Laboratory and cardiac findings

Creatine kinase is often normal or mildly elevated. In a 2023 mixed cohort it was normal in three patients and commonly 2–10× elevated, with an exceptional 60× congenital case; such marked elevation should prompt careful differential diagnosis (zanotti2023extracellularmatrixdisorganization pages 2-3). EMG is usually myopathic and nonspecific. Cardiac disease is not considered a typical direct manifestation: cardiac testing was normal throughout that 2023 cohort, and historical reviews describe only rare possibly coincidental abnormalities (zanotti2023extracellularmatrixdisorganization pages 2-3, bonnemann2011thecollagenvirelateda pages 6-7).

### Quality of life

Contractures impair hand use, dressing, transfers, gait, and self-care; weakness and fatigue restrict schooling, employment, recreation, and community participation; respiratory support and orthopedic procedures increase care burden. BM-specific EQ-5D, SF-36, or PROMIS datasets remain sparse. The global registry collects pain, hospitalization, mobility, respiratory, medication, imaging, and quality-of-life data, but mature published BM-specific estimates were unavailable (NCT04020159 chunk 1).

## 4. Genetic and molecular information

### Genes and chromosomes

- **COL6A1** and **COL6A2:** chromosome 21; encode α1(VI) and α2(VI).
- **COL6A3:** chromosome 2; encodes α3(VI).

COL6A1/A2/A3 form the canonical heterotrimer. Although COL6A4–COL6A6 encode additional collagen-VI-like chains, they are not established primary BM genes. Open Targets reports disease associations only for COL6A1/A2/A3 in BM (OpenTargets Search: Bethlem myopathy-COL6A1,COL6A2,COL6A3).

### Variant interpretation

Variants must be classified individually under ACMG/AMP criteria. Important evidence includes rarity, affected-domain location, segregation, de novo status, RNA splicing, collagen-VI secretion/deposition, and microfibril morphology. Germline origin is expected; BM is not a somatic neoplasm. Germline or parental mosaicism is possible and should be considered when an apparently de novo dominant variant recurs, although its frequency is unknown.

Standard sequencing historically detected only approximately 60–65% of clinically diagnosed BM, partly because deep-intronic and copy-number variants were missed. A deep-intronic **COL6A2** deletion was detected by custom CGH and shown by RNA analysis to cause monoallelic transcription, illustrating the need for complementary assays (DOI 10.1186/1471-2350-11-44).

### Modifiers, epigenetics, and chromosomal abnormalities

Marked intrafamilial variability suggests genetic, developmental, and environmental modifiers, but no modifier gene is clinically validated. There is no established BM-specific epigenetic signature used diagnostically. Large deletions/CNVs involving COL6 loci can be causal, but recurrent aneuploidy, translocation, or inversion is not characteristic. Conventional karyotyping and FISH are therefore low-yield unless another chromosomal disorder is suspected.

## 5. Environmental information

BM has no infectious agent, zoonotic trigger, toxicant, or occupational cause. Lifestyle does not determine occurrence. Exercise should be individualized: moderate, non-eccentric aerobic activity may support conditioning, whereas overwork, pain-provoking eccentric loading, falls, and prolonged immobilization should be avoided. Vaccination against respiratory pathogens follows standard neuromuscular respiratory-risk practice but does not prevent BM itself.

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. A pathogenic COL6A1/A2/A3 allele alters chain quantity or structure.
2. In the endoplasmic reticulum, α1/α2/α3 chains normally assemble into approximately 500-kDa monomers, then disulfide-linked dimers and tetramers; secreted tetramers form extracellular beaded microfibrils.
3. Mutant or absent chains impair secretion, microfibril assembly, or interaction with collagens I/II, fibronectin, glycosaminoglycans, and proteoglycans.
4. The muscle interstitial/basement-membrane matrix becomes disorganized and mechanically/signally abnormal.
5. Sarcolemmal stress, dysregulated calcium handling, mitochondrial permeability-transition-pore opening, reduced ATP production, and apoptosis injure myofibers.
6. Defective autophagy/mitophagy fails to clear damaged mitochondria; impaired regeneration and fibrosis compound weakness and contractures (castagnaro2018extracellularcollagenvi pages 10-14, bernardi2013mitochondrialdysfunctionand pages 1-2, zanotti2023extracellularmatrixdisorganization pages 1-2).

A 2023 human pathology series directly documented heterogeneous collagen-VI distribution, extracellular-matrix disorganization, sarcolemmal alterations, internal nuclei, fiber-size variation, and interstitial fibrosis. Its abstract states that combined histological, immunological, and ultrastructural methods are “**pivotal in the diagnosis of COL6 patients**” (published March 2023; DOI 10.3390/ijms24065551) (zanotti2023extracellularmatrixdisorganization pages 2-3, zanotti2023extracellularmatrixdisorganization pages 1-2).

### Cellular pathways

**Mitochondria and apoptosis.** Persistent mPTP opening promotes depolarization, swelling, impaired bioenergetics, and intrinsic apoptosis. Cyclosporin A/cyclophilin-D inhibition normalizes several defects in cells and models, supporting causality rather than mere association (telfer2010zebrafishmodelsof pages 1-2, bernardi2013mitochondrialdysfunctionand pages 1-2, merlini2023newclinicaland pages 1-2).

**Autophagy/mitophagy.** Reduced BECN1/Beclin-1 and BNIP3 signaling and abnormal AKT–mTOR activity diminish autophagic flux. Dysfunctional mitochondria accumulate, amplifying oxidative and apoptotic stress. Suggested GO: *autophagy*, *mitophagy*, *regulation of mitochondrial membrane permeability*, *intrinsic apoptotic signaling* (castagnaro2018extracellularcollagenvi pages 10-14).

**Regeneration.** Collagen VI supports satellite-cell self-renewal and regenerative niches. Deficiency reduces regenerative reserve and delays repair. Suggested cells: fibroblast/fibroadipogenic progenitor, skeletal myofiber, satellite cell; suggested GO: *skeletal muscle tissue regeneration* (mohassel2023collagentypevi pages 6-10, mohassel2023collagentypevi pages 38-41).

**TGF-β signaling—emerging evidence.** A June 2023 Col6a2-null mouse preprint proposed that collagen VI regulates TGF-β bioavailability and that matrix deficiency produces early TGF-β dysregulation. This is biologically coherent with fibrosis but remains less established than mitochondrial/autophagy mechanisms and should be annotated as preclinical/emerging (mohassel2023collagentypevi pages 6-10, mohassel2023collagentypevi pages 1-6).

### Molecular profiling

Deep RNA profiling of patient and Col6a1-null muscle identified CLOCK and molecular-clock gene signatures (2016; DOI 10.1242/jcs.175927). These are research signatures, not validated biomarkers. Proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, and multi-omic BM-specific datasets remain limited. The principal reproducible biochemical abnormalities are defective collagen deposition, mitochondrial dysfunction, and altered autophagic markers.

## 7. Anatomical structures affected

The primary organ is **skeletal muscle**, especially axial, pelvic-girdle, shoulder-girdle, and proximal limb musculature; diaphragm and intercostal muscles may be affected secondarily. Tendons, fascia, joint capsules, skin, and muscle connective tissue contribute to contractures and tissue stiffness. Disease is typically bilateral and relatively symmetric, although severity between muscles varies.

Suggested mappings include **UBERON:** skeletal muscle tissue, diaphragm, tendon, muscle fascia, joint capsule, skin; **CL:** fibroblast, skeletal muscle fiber, skeletal muscle satellite cell, fibroadipogenic progenitor; **GO cellular components:** collagen-containing extracellular matrix, basement membrane, endoplasmic reticulum, mitochondrial inner membrane, autophagosome, lysosome.

## 8. Temporal development

Onset may be congenital, childhood, adolescent, or adult and is usually insidious. Congenital presentations can include hypotonia, torticollis, hip dislocation, clubfoot, or delayed milestones. Childhood may show distal laxity and modest weakness; contractures become progressively more prominent. Weakness may appear stable or improve around puberty, followed by slow deterioration from the third or fourth decade. Historical series suggest approximately two-thirds of patients older than 60 require some ambulation assistance (bonnemann2011thecollagenvirelateda pages 6-7).

BM is lifelong and generally progressive, not episodic or relapsing-remitting. There is no true spontaneous remission. Critical intervention windows include early maintenance of range of motion, timely correction of function-threatening contractures, and detection of nocturnal hypoventilation before daytime respiratory failure.

## 9. Inheritance and population

Classic BM is **autosomal dominant**, frequently with variable expressivity; recessive BM-like presentations are also established. Penetrance is high for many clearly pathogenic dominant variants but can be age-dependent and mild, so apparently unaffected adults need careful examination. Anticipation is not established. Consanguinity increases risk for biallelic disease but is irrelevant to most dominant families.

A Newcastle estimate placed prevalence at **0.77 per 100,000**; modern incidence, carrier frequency, and population-specific prevalence are uncertain (bonnemann2011thecollagenvirelateda pages 1-2). There is no established sex bias or endemic geography. Founder variants may occur in individual populations, but most families have private variants. The 2024 report of a recessive COL6A2 splice variant in a consanguineous Saudi family illustrates population-specific ascertainment rather than proven increased regional prevalence.

## 10. Diagnostics

### Clinical assessment

Suspect BM when chronic proximal/axial weakness coexists with long finger-flexor or Achilles contractures, early distal laxity, characteristic skin findings, preserved adult ambulation, and a dominant family history. Assess range of motion, MRC/quantitative strength, gait, transfers, six-minute walk where feasible, pulmonary function sitting and supine, cough strength, oximetry/capnography, and sleep symptoms.

### Tests

- **CK:** normal or mildly elevated in typical disease; marked elevation warrants broader evaluation.
- **EMG/NCS:** myopathic EMG; nerve conduction usually normal.
- **Pulmonary:** serial FVC, maximal inspiratory/expiratory pressures, peak cough flow, sleep oximetry/capnography or polysomnography.
- **Cardiac:** baseline ECG/echocardiogram is reasonable, especially before anesthesia or if symptoms/family history exist, but routine progressive cardiomyopathy is not characteristic.
- **Muscle MRI:** perifascial fatty/connective-tissue replacement, especially the rectus femoris “central shadow/central cloud” and peripheral vastus lateralis pattern. Ultrasound can show a rectus-femoris central cloud (bonnemann2011thecollagenvirelateda pages 12-14).
- **Biopsy:** variable myopathic/dystrophic change, fiber-size disproportion, internal nuclei, fibrosis, and relatively limited necrosis. Collagen-VI immunostaining may be subtly abnormal or apparently normal in mild BM, so normal staining does not exclude disease (zanotti2023extracellularmatrixdisorganization pages 1-2, bonnemann2011thecollagenvirelateda pages 12-14).
- **Fibroblast assay:** dermal fibroblasts can demonstrate abnormal collagen secretion/deposition; RT-PCR can reveal exon skipping or deep-intronic effects (bonnemann2011thecollagenvirelateda pages 14-15).

### Genetic testing algorithm

1. Use a neuromuscular/congenital-myopathy panel including **COL6A1, COL6A2, COL6A3**, with robust CNV calling, or exome/genome sequencing.
2. Confirm and segregate candidate variants; determine de novo versus inherited status.
3. For VUS or negative sequencing with a strong phenotype, add fibroblast collagen studies and RNA sequencing/targeted RT-PCR.
4. Use MLPA, exon-level array/CGH, or genome sequencing for deletions, duplications, structural and deep-intronic variants.
5. WGS is particularly useful after nondiagnostic panel/WES because it interrogates intronic and structural variation. CMA, karyotype, FISH, mtDNA testing, and repeat-expansion testing are not routine unless the phenotype suggests another diagnosis (bonnemann2011thecollagenvirelateda pages 14-15).

### Differential diagnosis

Key alternatives are Emery–Dreifuss muscular dystrophy/LMNA-related disease, LAMA2-related dystrophy, SEPN1/SELENON myopathy, RYR1-related congenital myopathy, LMNA congenital muscular dystrophy, other limb-girdle muscular dystrophies, Ehlers–Danlos/connective-tissue disorders, and myosclerosis myopathy. Long finger-flexor contractures, skin changes, collagen-VI MRI pattern, absence of significant primary cardiomyopathy, and COL6 molecular evidence favor BM (bonnemann2011thecollagenvirelateda pages 12-14).

### Screening

There is no population or newborn screening program. Once a familial variant is known, cascade testing, targeted prenatal diagnosis, and preimplantation genetic testing are possible. Asymptomatic relatives require age-aware counseling because expression can be subtle.

## 11. Outcome and prognosis

Life expectancy is often near normal in mild BM if respiratory complications are recognized, but robust survival-rate or mortality estimates are unavailable. Most patients remain ambulant into adulthood; late walking aids or wheelchair use occur. In the 2023 cohort, wheelchair use was 15%, underscoring a broader severity range than historic pre-molecular series (merlini2023newclinicaland pages 14-15).

Major morbidity includes progressive weakness, hand and lower-limb contractures, falls, reduced endurance, scoliosis/rigid spine, pain, impaired self-care, and restrictive respiratory disease. Cardiac mortality is not typical. Prognostic factors include respiratory trajectory, severity and distribution of contractures, quantitative strength, mutation mechanism, and phenotype position within the COL6 continuum. No validated circulating prognostic biomarker exists. Collagen immunofluorescence correlates with phenotype at group level but is age-dependent and unsuitable as a stand-alone prognostic marker: serial biopsies showed increasing expression over time, an important consideration for genetic-correction trials (merlini2023newclinicaland pages 14-15, merlini2023newclinicaland pages 1-2).

## 12. Treatment and current applications

### Standard supportive care

- **Physiotherapy and occupational therapy:** daily gentle stretching, range-of-motion maintenance, posture, safe low-impact aerobic conditioning, energy conservation, and adaptive equipment. Suggested NCIT concepts: *Physical Therapy*, *Occupational Therapy*, *Exercise Intervention*.
- **Splints/orthoses:** dynamic finger splints and ankle-foot orthoses where tolerated. Suggested NCIT: *Splinting*, *Orthotic Device*.
- **Orthopedic surgery:** selected Achilles-tendon or other contracture release may preserve walking, but recurrence is common; scoliosis bracing is temporizing and surgery requires specialist respiratory/anesthetic planning (bonnemann2011thecollagenvirelateda pages 14-15).
- **Respiratory care:** regular pulmonary/sleep surveillance, airway-clearance support, cough-assist when indicated, prompt infection treatment, and nocturnal noninvasive ventilation for hypoventilation. Suggested NCIT: *Pulmonary Function Test*, *Noninvasive Ventilation*.
- **Nutrition/pain/bone health:** maintain healthy weight and adequate nutrition; treat pain and osteoporosis risk conventionally. Avoid unmonitored protein restriction.

### Experimental pharmacologic and nutritional strategies

**Cyclosporin A and non-immunosuppressive cyclophilin inhibitors.** Human proof-of-concept and animal/cellular studies show correction of mitochondrial dysfunction and apoptosis, but immunosuppression and limited clinical efficacy evidence preclude routine disease-modifying use. NIM811 and related mPTP modulators remain preclinical (bernardi2013mitochondrialdysfunctionand pages 1-2, merlini2023newclinicaland pages 1-2).

**Autophagy activation.** A one-year pilot low-protein diet increased autophagic markers and was reported safe/tolerable in seven analyzed adults, with preserved body composition and function and reduced myofiber apoptosis. The abstract states: “**These data provide evidence that a low-protein diet is able to activate autophagy and is safe and tolerable in patients with COL6 myopathies**” (published November 2016; DOI 10.1080/15548627.2016.1231279). This was mechanistic proof-of-concept, not evidence for routine clinical efficacy. Pterostilbene improved pathology in Col6-deficient mice but remains preclinical.

**Gene/RNA therapy.** Allele-specific silencing, splice correction, and CRISPR disruption/correction are experimental. A November 2024 fibroblast study achieved 32% editing of a dominant mutant COL6A1 allele with negligible wild-type editing and restored collagen secretion and microfibril ultrastructure; it involved UCMD fibroblasts, so translation to BM and muscle in vivo remains unproven (DOI 10.3390/biom14111412).

There is no established pharmacogenomic dosing algorithm, approved gene therapy, cell therapy, ASO, or combination regimen for BM.

### Clinical studies and real-world infrastructure

- **NCT01438788:** completed Phase II, open-label low-protein-diet pilot; eight adults; 0.6–0.8 g protein/kg/day; Beclin-1/autophagy endpoint (NCT01438788 chunk 1). URL: https://clinicaltrials.gov/study/NCT01438788
- **NCT03693898:** diagnostic MRI study, planned n=20 adults with BM/Ullrich disease; Dixon MRI fat fraction and strength testing (NCT03693898 chunk 1). URL: https://clinicaltrials.gov/study/NCT03693898
- **NCT04020159:** prospective Global Registry for COL6-related Dystrophies, target n=1,000; annual genetics, motor, respiratory, contracture, pain, hospitalization, QoL, medication, and imaging data (NCT04020159 chunk 1). URL: https://clinicaltrials.gov/study/NCT04020159

Status labels should be rechecked live because registry records retrieved here had differing historical and aggregate status displays.

## 13. Prevention

Primary prevention through lifestyle or vaccination is impossible because BM is genetic. **Secondary prevention** consists of family recognition, cascade testing, early molecular diagnosis, and surveillance before irreversible contractures or respiratory failure. **Tertiary prevention** includes stretching/orthoses, fall prevention, bone health, respiratory vaccination, airway clearance, sleep assessment, and timely ventilation.

Genetic counseling should cover autosomal-dominant and recessive possibilities, variable expressivity, de novo and mosaic recurrence risk, and reproductive options. Targeted prenatal diagnosis and preimplantation genetic testing are possible once the familial pathogenic variant is established; older approaches included haplotype analysis and chorionic-villus collagen-VI staining (bonnemann2011thecollagenvirelateda pages 14-15).

## 14. Other species and natural disease

The causal genes are evolutionarily conserved across vertebrates. Relevant taxa include **Mus musculus** (NCBI Taxon 10090) and **Danio rerio** (7955). No well-established naturally occurring companion-animal or wildlife disease equivalent to human Bethlem myopathy was identified in the retrieved literature; veterinary breed ontology mapping is therefore not applicable. BM is not transmissible or zoonotic.

## 15. Model organisms and experimental systems

### Mouse

**Col6a1−/− mice** lack collagen-VI assembly/secretion and show myopathy, abnormal mitochondria, spontaneous myofiber apoptosis, defective autophagy/mitophagy, and impaired regeneration. They are highly useful for mechanistic and drug studies but have a milder motor phenotype than severe human COL6 disease (castagnaro2018extracellularcollagenvi pages 10-14, bernardi2013mitochondrialdysfunctionand pages 1-2).

A **Col6a2−/− model**, characterized in 2023, showed early postnatal atrophy and weakness, fiber-size variability, central nuclei, delayed regeneration, sarcolemmal fragility, and altered TGF-β bioavailability. This supports matrix-signaling and non-cell-autonomous mechanisms; the work was initially reported as a preprint and requires appropriate evidence grading (mohassel2023collagentypevi pages 6-10, mohassel2023collagentypevi pages 1-6).

### Zebrafish

Exon-specific **col6a1 morphants** produced severe UCMD-like disease when exon 9 was targeted and a milder BM-like phenotype with exon 13 targeting. Severe morphants had abnormal mitochondria and increased cell death; cyclosporin A improved motor function but not sarcolemmal membrane damage. The model is valuable for rapid in-vivo pharmacology but transient morpholino biology and developmental timing limit direct human extrapolation. The abstract reports that the authors generated “**zebrafish models of the collagen VI myopathies**” and that CsA “**improved the motor deficits**” in the severe model (published March 2010; DOI 10.1093/hmg/ddq126) (telfer2010zebrafishmodelsof pages 1-2).

### Cellular systems

Patient dermal fibroblasts and myoblasts support collagen secretion/deposition assays, RNA studies, mitochondrial/autophagy phenotyping, and editing experiments. Col6a1-null mouse fibroblasts show impaired autophagosome clearance, defective Parkin-dependent mitophagy, AKT–mTOR activation, and increased apoptosis under nutrient stress; adhesion to purified collagen VI improves autophagic flux, demonstrating an extracellular instructive signal (castagnaro2018extracellularcollagenvi pages 10-14). Patient-derived iPSC, organoid, single-cell, and spatial models are promising but not yet mature enough for routine BM annotation.

## Recent developments, expert interpretation, and evidence gaps

The strongest 2023 clinical advance was quantitative phenotyping in a 69-person COL6 cohort, including 33 BM patients. It demonstrated unexpectedly substantial strength and pulmonary deficits and age-dependent collagen-VI immunofluorescence, directly affecting endpoint and biopsy interpretation in future trials (merlini2023newclinicaland pages 14-15, merlini2023newclinicaland pages 1-2). A separate March 2023 human study identified three previously unreported variants among 14 pathogenic variants and emphasized integrating genetics with histology, immunology, and ultrastructure (zanotti2023extracellularmatrixdisorganization pages 2-3, zanotti2023extracellularmatrixdisorganization pages 1-2). Emerging 2023 work links collagen VI to TGF-β bioavailability, while 2024 CRISPR work provides allele-selective fibroblast rescue; both are translationally important but not clinical therapies.

Authoritative expert consensus is that BM should be managed as a multisystem neuromuscular/connective-tissue disorder, not dismissed as a benign contracture syndrome. Key unresolved issues are contemporary prevalence and incidence, variant-specific penetrance, validated BM-specific patient-reported outcomes, prospective respiratory trajectories, circulating biomarkers, and controlled disease-modifying trials. Most mechanistic data derive from mixed COL6 phenotypes or models; phenotype-specific extrapolation should therefore be labeled explicitly.

### Selected primary/recent sources

1. Merlini L et al. *New Clinical and Immunofluorescence Data of Collagen VI-Related Myopathy: A Single Center Cohort of 69 Patients.* **August 2023.** DOI/URL: https://doi.org/10.3390/ijms241512474 (merlini2023newclinicaland pages 14-15, merlini2023newclinicaland pages 1-2)
2. Zanotti S et al. *Extracellular Matrix Disorganization and Sarcolemmal Alterations in COL6-Related Myopathy Patients with New Variants of COL6 Genes.* **March 2023.** DOI/URL: https://doi.org/10.3390/ijms24065551 (zanotti2023extracellularmatrixdisorganization pages 2-3, zanotti2023extracellularmatrixdisorganization pages 1-2)
3. Mohassel P et al. *Collagen type VI regulates TGFβ bioavailability in skeletal muscle.* **June 2023 preprint.** DOI/URL: https://doi.org/10.1101/2023.06.22.545964 (mohassel2023collagentypevi pages 6-10, mohassel2023collagentypevi pages 1-6)
4. Telfer WR et al. *Zebrafish models of collagen VI-related myopathies.* **March 2010.** DOI/URL: https://doi.org/10.1093/hmg/ddq126 (telfer2010zebrafishmodelsof pages 1-2)
5. Bernardi P, Bonaldo P. *Mitochondrial dysfunction and defective autophagy in the pathogenesis of collagen VI muscular dystrophies.* **May 2013.** DOI/URL: https://doi.org/10.1101/cshperspect.a011387 (bernardi2013mitochondrialdysfunctionand pages 1-2)

**PMID note:** PMID values were not consistently exposed in the retrieved full-text metadata. To avoid erroneous identifiers, DOI and direct registry URLs are supplied above; database curators should resolve PMIDs through Crossref/PubMed during ingestion.

References

1. (OpenTargets Search: Bethlem myopathy-COL6A1,COL6A2,COL6A3): Open Targets Query (Bethlem myopathy-COL6A1,COL6A2,COL6A3, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (merlini2023newclinicaland pages 1-2): Luciano Merlini, Patrizia Sabatelli, Francesca Gualandi, Edoardo Redivo, Alberto Di Martino, and Cesare Faldini. New clinical and immunofluorescence data of collagen vi-related myopathy: a single center cohort of 69 patients. International Journal of Molecular Sciences, 24:12474, Aug 2023. URL: https://doi.org/10.3390/ijms241512474, doi:10.3390/ijms241512474. This article has 21 citations.

3. (bonnemann2011thecollagenvirelateda pages 1-2): Carsten G. Bönnemann. The collagen vi-related myopathies ullrich congenital muscular dystrophy and bethlem myopathy. Handbook of clinical neurology, 101:81-96, Jan 2011. URL: https://doi.org/10.1016/b978-0-08-045031-5.00005-0, doi:10.1016/b978-0-08-045031-5.00005-0. This article has 154 citations.

4. (zanotti2023extracellularmatrixdisorganization pages 1-2): Simona Zanotti, Francesca Magri, Sabrina Salani, Laura Napoli, Michela Ripolone, Dario Ronchi, Francesco Fortunato, Patrizia Ciscato, Daniele Velardo, Maria Grazia D’Angelo, Francesca Gualandi, Vincenzo Nigro, Monica Sciacco, Stefania Corti, Giacomo Pietro Comi, and Daniela Piga. Extracellular matrix disorganization and sarcolemmal alterations in col6-related myopathy patients with new variants of col6 genes. International Journal of Molecular Sciences, 24:5551, Mar 2023. URL: https://doi.org/10.3390/ijms24065551, doi:10.3390/ijms24065551. This article has 15 citations.

5. (merlini2023newclinicaland pages 14-15): Luciano Merlini, Patrizia Sabatelli, Francesca Gualandi, Edoardo Redivo, Alberto Di Martino, and Cesare Faldini. New clinical and immunofluorescence data of collagen vi-related myopathy: a single center cohort of 69 patients. International Journal of Molecular Sciences, 24:12474, Aug 2023. URL: https://doi.org/10.3390/ijms241512474, doi:10.3390/ijms241512474. This article has 21 citations.

6. (bonnemann2011thecollagenvirelateda pages 14-15): Carsten G. Bönnemann. The collagen vi-related myopathies ullrich congenital muscular dystrophy and bethlem myopathy. Handbook of clinical neurology, 101:81-96, Jan 2011. URL: https://doi.org/10.1016/b978-0-08-045031-5.00005-0, doi:10.1016/b978-0-08-045031-5.00005-0. This article has 154 citations.

7. (castagnaro2018extracellularcollagenvi pages 10-14): Silvia Castagnaro, Martina Chrisam, Matilde Cescon, Paola Braghetta, Paolo Grumati, and Paolo Bonaldo. Extracellular collagen vi has prosurvival and autophagy instructive properties in mouse fibroblasts. Frontiers in Physiology, Aug 2018. URL: https://doi.org/10.3389/fphys.2018.01129, doi:10.3389/fphys.2018.01129. This article has 53 citations.

8. (mohassel2023collagentypevi pages 1-6): Payam Mohassel, Jachinta Rooney, Yaqun Zou, Kory Johnson, Gina Norato, Hailey Hearn, Matthew A Nalls, Pomi Yun, Tracy Ogata, Sarah Silverstein, David A Sleboda, Thomas J Roberts, Daniel B Rifkin, and Carsten G Bönnemann. Collagen type vi regulates tgfβ bioavailability in skeletal muscle. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.22.545964, doi:10.1101/2023.06.22.545964. This article has 5 citations.

9. (bonnemann2011thecollagenvirelateda pages 6-7): Carsten G. Bönnemann. The collagen vi-related myopathies ullrich congenital muscular dystrophy and bethlem myopathy. Handbook of clinical neurology, 101:81-96, Jan 2011. URL: https://doi.org/10.1016/b978-0-08-045031-5.00005-0, doi:10.1016/b978-0-08-045031-5.00005-0. This article has 154 citations.

10. (bonnemann2011thecollagenvirelateda pages 12-14): Carsten G. Bönnemann. The collagen vi-related myopathies ullrich congenital muscular dystrophy and bethlem myopathy. Handbook of clinical neurology, 101:81-96, Jan 2011. URL: https://doi.org/10.1016/b978-0-08-045031-5.00005-0, doi:10.1016/b978-0-08-045031-5.00005-0. This article has 154 citations.

11. (zanotti2023extracellularmatrixdisorganization pages 2-3): Simona Zanotti, Francesca Magri, Sabrina Salani, Laura Napoli, Michela Ripolone, Dario Ronchi, Francesco Fortunato, Patrizia Ciscato, Daniele Velardo, Maria Grazia D’Angelo, Francesca Gualandi, Vincenzo Nigro, Monica Sciacco, Stefania Corti, Giacomo Pietro Comi, and Daniela Piga. Extracellular matrix disorganization and sarcolemmal alterations in col6-related myopathy patients with new variants of col6 genes. International Journal of Molecular Sciences, 24:5551, Mar 2023. URL: https://doi.org/10.3390/ijms24065551, doi:10.3390/ijms24065551. This article has 15 citations.

12. (mohassel2023collagentypevi pages 38-41): Payam Mohassel, Jachinta Rooney, Yaqun Zou, Kory Johnson, Gina Norato, Hailey Hearn, Matthew A Nalls, Pomi Yun, Tracy Ogata, Sarah Silverstein, David A Sleboda, Thomas J Roberts, Daniel B Rifkin, and Carsten G Bönnemann. Collagen type vi regulates tgfβ bioavailability in skeletal muscle. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.22.545964, doi:10.1101/2023.06.22.545964. This article has 5 citations.

13. (bernardi2013mitochondrialdysfunctionand pages 1-2): P. Bernardi and P. Bonaldo. Mitochondrial dysfunction and defective autophagy in the pathogenesis of collagen vi muscular dystrophies. Cold Spring Harbor perspectives in biology, 5 5:a011387, May 2013. URL: https://doi.org/10.1101/cshperspect.a011387, doi:10.1101/cshperspect.a011387. This article has 91 citations and is from a peer-reviewed journal.

14. (mohassel2023collagentypevi pages 6-10): Payam Mohassel, Jachinta Rooney, Yaqun Zou, Kory Johnson, Gina Norato, Hailey Hearn, Matthew A Nalls, Pomi Yun, Tracy Ogata, Sarah Silverstein, David A Sleboda, Thomas J Roberts, Daniel B Rifkin, and Carsten G Bönnemann. Collagen type vi regulates tgfβ bioavailability in skeletal muscle. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.22.545964, doi:10.1101/2023.06.22.545964. This article has 5 citations.

15. (NCT01438788 chunk 1):  Low Protein Diet in Patients With Collagen VI Related Myopathies. Istituto Ortopedico Rizzoli. 2011. ClinicalTrials.gov Identifier: NCT01438788

16. (NCT03693898 chunk 1): Ruth Salim. MR in Patients With Collagen VI Related Myopathies. Ruth Salim. 2018. ClinicalTrials.gov Identifier: NCT03693898

17. (NCT04020159 chunk 1):  Global Registry for COL6-related Dystrophies. Newcastle-upon-Tyne Hospitals NHS Trust. 2018. ClinicalTrials.gov Identifier: NCT04020159

18. (telfer2010zebrafishmodelsof pages 1-2): W. R. Telfer, A. Busta, Carsten G. Bönnemann, Eva L. Feldman, and James J. Dowling. Zebrafish models of collagen vi-related myopathies. Human Molecular Genetics, 19:2433-2444, Mar 2010. URL: https://doi.org/10.1093/hmg/ddq126, doi:10.1093/hmg/ddq126. This article has 127 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Bethlem_Myopathy-deep-research-falcon_artifacts/artifact-00.md)