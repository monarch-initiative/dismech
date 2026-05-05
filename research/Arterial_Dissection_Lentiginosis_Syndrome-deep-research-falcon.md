---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T11:40:56.092890'
end_time: '2026-05-05T11:53:27.764410'
duration_seconds: 751.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arterial Dissection-Lentiginosis Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arterial Dissection-Lentiginosis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arterial Dissection-Lentiginosis Syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Arterial Dissection-Lentiginosis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arterial Dissection-Lentiginosis Syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Comprehensive Research Report: Arterial Dissection–Lentiginosis Syndrome (ADL)

### Executive summary
Arterial Dissections with Lentiginosis (ADL) is a very rare, primarily case-report–defined Mendelian syndrome characterized by early-onset, sometimes recurrent, dissections of large/medium arteries together with multiple cutaneous lentigines and arterial wall pathology consistent with cystic medial degeneration/necrosis. The condition was initially described in two families (two sibling pairs) in a Mayo Clinic arterial-dissection cohort, and subsequent reviews mention six additional sporadic cases. A causal gene has not been identified in the retrieved primary literature; one family had negative testing for type III procollagen abnormalities (COL3A1) in cultured fibroblasts. A prominent mechanistic hypothesis proposes a neural-crest developmental defect (“neurocristopathy”) linking melanocyte abnormalities to arterial tunica media fragility. (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4)

### Artifact: consolidated snapshot
The following table is a knowledge-base–ready synopsis of identifiers, phenotypes, inheritance, and molecular status.

| Aspect | Summary | Evidence type | Citation |
|---|---|---|---|
| Disease / synonyms | **Arterial dissections with lentiginosis (ADL)**; **familial syndrome of arterial dissections with lentiginosis**; also referred to as **arterial dissection-lentiginosis syndrome** in secondary summaries. | Human case report; review | (schievink1995briefreporta pages 1-1, chrousos1998carneycomplexand pages 4-4) |
| Key identifiers | **OMIM: 600459**; listed among familial lentiginoses in review tables. No gene assignment was identified in the cited sources. | Review | (stratakis2001geneticsofpeutzjeghers pages 1-3, chrousos1998carneycomplexand pages 1-2) |
| Reported cases / count | Originally described in **2 sibling pairs** from a Mayo Clinic series of **240** arterial-dissection patients; **6 additional sporadic cases** were later noted in reviews. | Human case report; review | (schievink1995briefreporta pages 1-1, stratakis2001geneticsofpeutzjeghers pages 6-8, chrousos1998carneycomplexand pages 4-4) |
| Inheritance | **Autosomal recessive suggested** because of lack of vertical transmission and consanguinity in one family; **autosomal dominant inheritance with variable penetrance/expression not excluded**. | Human case report; review | (schievink1995briefreporta pages 1-3, stratakis2001geneticsofpeutzjeghers pages 6-8) |
| Key vascular features | Predisposition to dissections of **large/medium arteries**, especially the **aorta**, **renal artery**, and **extracranial internal carotid artery**; vertebral/cervical artery dissections and recurrent/multivessel involvement were reported in the original families. | Human case report; review | (schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4, stratakis2001geneticsofpeutzjeghers pages 6-8) |
| Key skin features | **Multiple lentigines**, typically **2–4 mm**, dark brown to black, on **trunk and extremities** (especially **lower legs**); may occur on **sun-exposed and non-sun-exposed** skin; lesions usually begin in **childhood**; **mucous membranes spared** in reported families. | Human case report; review | (schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4, fikar2000etiologicfactorsof pages 4-6) |
| Pathology | Arterial pathology showed **cystic medial necrosis / cystic medial degeneration** and elastin abnormalities; one resected artery showed **acute medial dissection with focal cystic degeneration of the media**. | Human case report; review | (schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4, fikar2000etiologicfactorsof pages 4-6) |
| Mechanistic hypothesis | Proposed developmental mechanism is a **neural crest defect / neurocristopathy**, because **melanocytes** and the **tunica media of the aortic arch and its branches** derive from neural crest; chick neural crest ablation produced similar elastin disarray. | Human case report; review | (schievink1995briefreporta pages 3-4, fikar2000etiologicfactorsof pages 4-6) |
| Molecular genetics status | **No causal gene or pathogenic variant identified** in the cited ADL literature; **COL3A1/type III procollagen abnormalities were not found** in tested fibroblasts from one family, and ADL-specific locus/gene remained unknown in reviews. | Human case report; review | (schievink1995briefreporta pages 1-3, stratakis2001geneticsofpeutzjeghers pages 9-10, chrousos1998carneycomplexand pages 1-2) |


*Table: This table consolidates the key published facts about Arterial Dissections with Lentiginosis (ADL) syndrome from the original 1995 case report and subsequent reviews. It is useful as a knowledge-base-ready snapshot of identifiers, phenotype, inheritance, pathology, and current molecular uncertainty.*

---

## 1. Disease information

### 1.1 What is the disease?
**ADL (Arterial Dissections with Lentiginosis)** is a syndromic arteriopathy in which affected individuals develop arterial dissections (cervical/cerebrovascular and systemic large arteries including aorta and renal arteries) at relatively young ages, along with **multiple lentigines** (small, dark brown-to-black macules) that typically appear in childhood and may fade later. In the original report, arterial histopathology showed **cystic medial necrosis/degeneration**. (schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4)

### 1.2 Key identifiers
- **OMIM:** **600459** (listed under familial lentiginoses as “arterial dissections and lentiginosis (ADL)” in a genetics review). (stratakis2001geneticsofpeutzjeghers pages 1-3)
- **Mondo / Orphanet / MeSH / ICD-10/ICD-11:** Not found in the retrieved corpus; these identifiers may exist in external curated resources but could not be verified here.

### 1.3 Synonyms / alternative names
- “**A familial syndrome of arterial dissections with lentiginosis**” (original NEJM description). (schievink1995briefreporta pages 1-1)
- “**Arterial dissections and lentiginosis (ADL) syndrome**” (review terminology). (stratakis2001geneticsofpeutzjeghers pages 6-8)

### 1.4 Evidence source type
The ADL entity in the retrieved sources is derived from:
- **Primary human case reports** (families; NEJM 1995). (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 1-3)
- **Aggregated review resources** summarizing those cases and additional sporadic reports. (stratakis2001geneticsofpeutzjeghers pages 6-8, chrousos1998carneycomplexand pages 4-4)

**Publication details / URLs (primary sources):**
- Schievink WI et al. *N Engl J Med* (1995-03-02). DOI/URL: https://doi.org/10.1056/NEJM199503023320905 (schievink1995briefreporta pages 1-1)
- Stratakis CA. *Horm Res* (2001-09). DOI/URL: https://doi.org/10.1159/000053283 (stratakis2001geneticsofpeutzjeghers pages 6-8)
- Chrousos GP, Stratakis CA. *J Intern Med* (1998-06). DOI/URL: https://doi.org/10.1046/j.1365-2796.1998.00341.x (chrousos1998carneycomplexand pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic cause:** The causal gene is **unknown** in the retrieved primary literature and reviews; ADL is suspected to be genetic due to familial clustering and early presentation. (schievink1995briefreporta pages 1-3, chrousos1998carneycomplexand pages 1-2)

**Mechanistic etiology (developmental hypothesis):** A proposed etiology is a defect in neural-crest–derived lineages (“neurocristopathy”), because melanocytes derive from trunk neural crest and the tunica media of the aortic arch/branches derives from cranial neural crest; this developmental link was used to explain the co-occurrence of lentigines and cystic medial necrosis/dissection. (schievink1995briefreporta pages 3-4, fikar2000etiologicfactorsof pages 4-6)

### 2.2 Risk factors
- **Family history:** Familial occurrence is central to the syndrome definition. In one series context, “8 of ~240” cervical-artery dissection patients had family history, motivating identification of the two ADL families. (schievink1995briefreporta pages 1-1)
- **Trauma:** At least one cervical dissection case in the original report occurred after a skiing accident; a separate dissection (occipital artery) was thought related to surgery/operation exposure rather than spontaneous disease biology. These observations suggest that mechanical triggers may precipitate events in a predisposed arterial wall, but this is not quantified as a risk factor specific to ADL. (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 1-3)

### 2.3 Protective factors
No ADL-specific protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interaction
Not established for ADL in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core phenotype domains

#### A) Vascular phenotypes (clinical signs/symptoms)
- **Arterial dissection** in multiple vascular beds, including:
  - **Extracranial internal carotid artery dissection** (angiographic stenosis consistent with dissection). (schievink1995briefreporta pages 1-3)
  - **Cervical vertebral artery dissection** (original cases). (schievink1995briefreporta pages 1-1)
  - **Ascending aortic dissection/rupture** causing sudden death in a relative (autopsy hemopericardium; cystic medial necrosis). (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 3-4)
  - Reviews also emphasize predisposition to dissections of **aorta, renal artery, extracranial internal carotid artery**. (stratakis2001geneticsofpeutzjeghers pages 6-8, chrousos1998carneycomplexand pages 4-4)
- **Associated neurologic presentations** in cervical dissections included headache and focal deficits (e.g., hemiparesis), consistent with typical cervicocephalic dissection presentations (reported within the family). (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 1-3)

**Suggested HPO terms (mapping to described features):**
- Arterial dissection: **HP:0004970** (arterial dissection; general)
- Aortic dissection: **HP:0002647**
- Carotid artery dissection: **HP:0030809** (if using specific term; otherwise arterial dissection)
- Vertebral artery dissection: (may be represented via arterial dissection plus vertebral artery involvement term if available)
- Recurrent arterial dissections: (use recurrence qualifier if present)

#### B) Dermatologic phenotypes
- **Multiple lentigines (lentiginosis):** described as “flat or slightly raised…brown-to-black…2 to 4 mm,” often present on **trunk and extremities**, particularly **lower legs**, and also reported on **palms and soles** in the case report narrative summary. Lentigines begin in childhood, increase in adolescence/early adulthood, and may fade. (schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4)
- **Mucosal sparing:** mucous membranes were spared in the NEJM families, helping distinguish from Carney complex in the differential. (schievink1995briefreporta pages 3-4)

**Suggested HPO terms:**
- Multiple lentigines: **HP:0001003**
- Hyperpigmented macules: **HP:0001013**

#### C) Structural cardiovascular phenotype
- **Aortic coarctation** occurred in one patient in the original report. (schievink1995briefreporta pages 3-4)

**Suggested HPO term:**
- Coarctation of the aorta: **HP:0001680**

### 3.2 Phenotype characteristics (onset, severity, progression, frequency)
- **Age of onset:** Lentigines “usually appear in childhood”; vascular dissections occurred at “young age” in affected members, including a 25-year-old brother with carotid dissection and a 22-year-old with ascending aortic dissection noted in secondary review. (schievink1995briefreporta pages 1-3, fikar2000etiologicfactorsof pages 4-6)
- **Progression/course:** Vascular course can be **multivessel** and **recurrent**; follow-up in one case noted no vascular events over eight years and fading lentigines. (schievink1995briefreporta pages 1-3)
- **Frequency:** No reliable penetrance/frequency estimates exist due to very small case counts; reviews cite two sibling pairs and six sporadic cases. (stratakis2001geneticsofpeutzjeghers pages 6-8, chrousos1998carneycomplexand pages 4-4)

### 3.3 Quality-of-life impact
Not directly measured with QoL instruments in retrieved literature; major impact is inferred from risk of stroke-like events and fatal aortic rupture. (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 3-4)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
**Unknown** in the retrieved ADL literature. (chrousos1998carneycomplexand pages 1-2)

### 4.2 Pathogenic variants
No ADL-specific pathogenic variant(s) were reported in the retrieved texts.

### 4.3 Relevant negative finding (candidate exclusion)
The NEJM report states that “analysis of the type III procollagen gene in cultured skin fibroblasts showed no abnormalities,” arguing against COL3A1-mediated vascular Ehlers–Danlos as an explanation in that family. (schievink1995briefreporta pages 1-3)

### 4.4 Functional consequences
Not established for ADL (no gene identified).

### 4.5 Modifier genes / epigenetics / chromosomal abnormalities
Not reported for ADL in the retrieved sources.

---

## 5. Environmental information
No ADL-specific environmental contributors were identified. Individual dissections may be precipitated by trauma or iatrogenic factors in susceptible vessels, but this is not established as syndrome-specific epidemiology. (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 1-3)

---

## 6. Mechanism / pathophysiology

### 6.1 Proposed causal chain (current best-supported hypothesis)
1. **Developmental defect in neural-crest–derived cells** (hypothesized genetic). (schievink1995briefreporta pages 3-4)
2. **Abnormal arterial tunica media / extracellular matrix organization** manifested as **cystic medial necrosis/degeneration** and elastin fiber disarray. (schievink1995briefreporta pages 3-4, fikar2000etiologicfactorsof pages 4-6)
3. **Mechanical failure of arterial wall** under physiologic or triggered stress → **arterial dissection** across multiple vascular beds (cervicocephalic, renal, aortic). (stratakis2001geneticsofpeutzjeghers pages 6-8, schievink1995briefreporta pages 1-3)
4. Parallel phenotype: altered melanocyte development/migration → **multiple cutaneous lentigines**. (schievink1995briefreporta pages 3-4)

### 6.2 Upstream vs downstream
- Upstream: suspected developmental/genetic defect; neural crest lineage biology. (schievink1995briefreporta pages 3-4)
- Downstream: cystic medial necrosis and clinical dissections; neurologic sequelae or sudden death. (schievink1995briefreporta pages 1-1, schievink1995briefreporta pages 3-4)

### 6.3 Cell types (CL suggestions)
- **Melanocyte**: CL:0000148 (lentigines biology). (schievink1995briefreporta pages 3-4)
- **Vascular smooth muscle cell** (arterial media): CL term for vascular SMC (arterial wall integrity) (mechanistically implied by tunica media pathology). (schievink1995briefreporta pages 3-4)

### 6.4 GO biological process suggestions (hypothesis-driven)
Given the neurocristopathy hypothesis and medial degeneration pathology, plausible GO process annotations include:
- Neural crest cell migration / development (e.g., “neural crest cell migration”). (schievink1995briefreporta pages 3-4)
- Extracellular matrix organization / elastic fiber formation (consistent with elastin disarray). (schievink1995briefreporta pages 3-4)

### 6.5 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic studies were identified for ADL.

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- **Cardiovascular system:** aorta; renal arteries; extracranial internal carotid arteries; vertebral/cervical arteries. (stratakis2001geneticsofpeutzjeghers pages 6-8, schievink1995briefreporta pages 1-3)
- **Integumentary system:** skin (lentigines on trunk/extremities, palms/soles; mucosa spared). (schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4)

### 7.2 Tissue/cell level
- **Arterial tunica media** (site of cystic medial necrosis). (schievink1995briefreporta pages 3-4)
- **Melanocyte-containing epidermal/dermal junction** (lentigines histology referenced in NEJM discussion). (schievink1995briefreporta pages 3-4)

### 7.3 UBERON suggestions
- Aorta: UBERON:0000947
- Renal artery: UBERON:0001496
- Internal carotid artery: UBERON:0004451
- Skin of lower limb: UBERON:0004264 (or more specific lower leg skin term)

---

## 8. Temporal development
- **Onset pattern:** lentigines in childhood; dissections in adolescence/young adulthood in reported kindreds. (schievink1995briefreporta pages 3-4, schievink1995briefreporta pages 1-3)
- **Course:** variable; potential for recurrent and multivessel dissections; at least one case had stable follow-up (8 years) without further vascular events and fading lentigines. (schievink1995briefreporta pages 1-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
- The NEJM case report argues the syndrome is “genetic in origin,” and suggests **autosomal recessive inheritance** due to absent vertical transmission and consanguinity in one family, while not excluding autosomal dominant inheritance with variable penetrance/expression. (schievink1995briefreporta pages 1-3)
- Reviews maintain that inheritance is “not clear,” noting the suggestion of autosomal recessive inheritance. (stratakis2001geneticsofpeutzjeghers pages 6-8)

### 9.2 Epidemiology
No population prevalence/incidence estimates were identified. Evidence is limited to a very small number of reported families/cases.

**Case-count statistic (best available):** Reviews summarize **2 sibling pairs** in the original series plus **6 sporadic cases**. (stratakis2001geneticsofpeutzjeghers pages 6-8, chrousos1998carneycomplexand pages 4-4)

---

## 10. Diagnostics

### 10.1 Clinical recognition
A high-suspicion diagnostic pattern is:
- **Early-onset arterial dissection(s)** (especially cervicocephalic and/or aortic/renal), possibly recurrent/multivessel, plus
- **Multiple cutaneous lentigines** (2–4 mm dark macules; trunk/extremities; lower legs prominent; mucosa spared), plus
- **Histopathology** showing **cystic medial necrosis/degeneration** when arterial tissue is available. (schievink1995briefreporta pages 1-3, schievink1995briefreporta pages 3-4)

### 10.2 Imaging
Not ADL-specific, but dissections were diagnosed via **angiography** in the original report (extracranial internal carotid dissection described as smooth stenosis consistent with dissection). (schievink1995briefreporta pages 1-3)

### 10.3 Genetic testing
No single-gene test is available because the causal gene is unknown. The original report noted negative COL3A1/type III procollagen evaluation in cultured fibroblasts in one family; in current real-world practice, patients with this presentation would typically undergo broad heritable arteriopathy/aortopathy testing (panel/WES/WGS), but this is an extrapolation beyond the retrieved ADL-specific literature. (schievink1995briefreporta pages 1-3)

### 10.4 Differential diagnosis (evidence-based distinctions)
- **Carney complex:** can include multiple lentigines and cardiac myxomas; in the NEJM families, Carney complex was considered unlikely due to lack of cardiac myxoma evidence and because Carney-associated lentigines often involve mucous membranes, whereas mucosa was spared in ADL. (schievink1995briefreporta pages 3-4)
- **LEOPARD / multiple lentigines syndrome:** includes lentigines and congenital heart disease; NEJM authors note that spontaneous arterial dissections had not been noted in LEOPARD and other lentiginosis syndromes in their discussion, and their cases lacked other LEOPARD components. (schievink1995briefreporta pages 3-4)
- **Vascular Ehlers–Danlos (COL3A1):** considered; NEJM report indicates no mutation/abnormality in type III procollagen gene testing in the propositus from Family B. (schievink1995briefreporta pages 1-3)

---

## 11. Outcomes / prognosis
No formal survival or long-term outcome statistics are available. However, the syndrome can be severe:
- Documented **sudden death** in a relative due to **ascending aortic dissection/rupture**. (schievink1995briefreporta pages 1-1)
- Conversely, at least one affected individual had **8 years of follow-up without vascular events**. (schievink1995briefreporta pages 1-3)

---

## 12. Treatment
No ADL-specific interventional or pharmacologic regimen is established in the retrieved literature. Management in the primary report included surgical and diagnostic management of dissections as clinically indicated (e.g., bypass procedures and recognition of operative-related dissection). (schievink1995briefreporta pages 1-3)

**Extrapolated (clearly labeled) real-world implementations:** In contemporary care, patients with suspected syndromic arteriopathy typically receive (i) vascular imaging surveillance across arterial beds and (ii) risk mitigation counseling to avoid extreme mechanical stressors; however, these are general arteriopathy principles and not ADL-specific evidence in the retrieved sources.

**MAXO suggestions (extrapolative):**
- Vascular imaging surveillance (e.g., MAXO term for diagnostic imaging procedure)
- Genetic counseling (MAXO:0000079, if using standard genetic counseling action)

---

## 13. Prevention
No primary prevention is known. **Secondary/tertiary prevention** is plausibly centered on early recognition and surveillance for arterial pathology in affected individuals and family members, but ADL-specific evidence-based prevention protocols are not available in the retrieved literature.

---

## 14. Other species / natural disease
No animal/natural disease analogs were identified in the retrieved sources.

---

## 15. Model organisms
No ADL-specific model organisms were identified. A mechanistic analog experiment is cited in the NEJM discussion and pediatric review: cranial neural crest ablation in chick embryos caused arterial elastin fiber disarray resembling cystic medial necrosis, supporting the neurocristopathy hypothesis (mechanistic support but not a genetic disease model of ADL). (schievink1995briefreporta pages 3-4, fikar2000etiologicfactorsof pages 4-6)

---

## Visual evidence (from primary publication)
- Pedigrees of the two families and a clinical image of lower-leg lentiginosis were extracted from the NEJM report (useful for inheritance pattern appraisal and dermatologic phenotype recognition). (schievink1995briefreporta media 105b5352, schievink1995briefreporta media 87dd50de)

---

## Key quotations from the retrieved literature
- NEJM 1995 mechanism statement: “**the arterial media and melanocytes are derived from neural-crest cells, suggesting that a neural-crest defect may be the underlying abnormality in these families**.” (schievink1995briefreporta pages 1-1)
- NEJM 1995 concluding diagnosis framing: “**In conclusion, we describe a familial syndrome of arterial dissection, multiple lentigines, and cystic medial necrosis. This syndrome may represent a neurocristopathy.**” (schievink1995briefreporta pages 3-4)
- Stratakis review case-count summary: “**The arterial dissections and lentiginosis (ADL) syndrome was recently described in two sets of siblings... Six additional sporadic cases were reported** …” (stratakis2001geneticsofpeutzjeghers pages 6-8)

---

## Limitations of this report (evidence gaps)
- **No causal gene/variant** was found in the retrieved ADL-specific sources; therefore, ClinVar/ClinGen/gnomAD variant-level synthesis cannot be completed without additional external retrieval.
- **No 2023–2024 primary ADL advances** were retrieved via tool-based searches; the recent literature on this specific named syndrome may be sparse or indexed under different terms.
- **Epidemiology, penetrance, and standardized clinical criteria** remain undefined due to the extremely small number of published cases.


References

1. (schievink1995briefreporta pages 1-1): Wouter I. Schievink, Virginia V. Michels, Bahram Mokri, David G. Piepgras, and Harold O. Perry. Brief report: a familial syndrome of arterial dissections with lentiginosis. The New England journal of medicine, 332 9:576-9, Mar 1995. URL: https://doi.org/10.1056/nejm199503023320905, doi:10.1056/nejm199503023320905. This article has 73 citations and is from a highest quality peer-reviewed journal.

2. (schievink1995briefreporta pages 1-3): Wouter I. Schievink, Virginia V. Michels, Bahram Mokri, David G. Piepgras, and Harold O. Perry. Brief report: a familial syndrome of arterial dissections with lentiginosis. The New England journal of medicine, 332 9:576-9, Mar 1995. URL: https://doi.org/10.1056/nejm199503023320905, doi:10.1056/nejm199503023320905. This article has 73 citations and is from a highest quality peer-reviewed journal.

3. (schievink1995briefreporta pages 3-4): Wouter I. Schievink, Virginia V. Michels, Bahram Mokri, David G. Piepgras, and Harold O. Perry. Brief report: a familial syndrome of arterial dissections with lentiginosis. The New England journal of medicine, 332 9:576-9, Mar 1995. URL: https://doi.org/10.1056/nejm199503023320905, doi:10.1056/nejm199503023320905. This article has 73 citations and is from a highest quality peer-reviewed journal.

4. (chrousos1998carneycomplexand pages 4-4): Chrousos and Stratakis. Carney complex and the familial lentiginosis syndromes: link to inherited neoplasias and developmental disorders, and genetic loci. Journal of Internal Medicine, 243:573-579, Jun 1998. URL: https://doi.org/10.1046/j.1365-2796.1998.00341.x, doi:10.1046/j.1365-2796.1998.00341.x. This article has 27 citations and is from a domain leading peer-reviewed journal.

5. (stratakis2001geneticsofpeutzjeghers pages 1-3): Constantine A. Stratakis. Genetics of peutz-jeghers syndrome, carney complex and other familial lentiginoses. Hormone Research in Paediatrics, 54:334-343, Sep 2001. URL: https://doi.org/10.1159/000053283, doi:10.1159/000053283. This article has 45 citations and is from a peer-reviewed journal.

6. (chrousos1998carneycomplexand pages 1-2): Chrousos and Stratakis. Carney complex and the familial lentiginosis syndromes: link to inherited neoplasias and developmental disorders, and genetic loci. Journal of Internal Medicine, 243:573-579, Jun 1998. URL: https://doi.org/10.1046/j.1365-2796.1998.00341.x, doi:10.1046/j.1365-2796.1998.00341.x. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (stratakis2001geneticsofpeutzjeghers pages 6-8): Constantine A. Stratakis. Genetics of peutz-jeghers syndrome, carney complex and other familial lentiginoses. Hormone Research in Paediatrics, 54:334-343, Sep 2001. URL: https://doi.org/10.1159/000053283, doi:10.1159/000053283. This article has 45 citations and is from a peer-reviewed journal.

8. (fikar2000etiologicfactorsof pages 4-6): Charles R. Fikar and Simone Koch. Etiologic factors of acute aortic dissection in children and younrg adults. Clinical Pediatrics, 39:71-80, Feb 2000. URL: https://doi.org/10.1177/000992280003900201, doi:10.1177/000992280003900201. This article has 104 citations and is from a peer-reviewed journal.

9. (stratakis2001geneticsofpeutzjeghers pages 9-10): Constantine A. Stratakis. Genetics of peutz-jeghers syndrome, carney complex and other familial lentiginoses. Hormone Research in Paediatrics, 54:334-343, Sep 2001. URL: https://doi.org/10.1159/000053283, doi:10.1159/000053283. This article has 45 citations and is from a peer-reviewed journal.

10. (schievink1995briefreporta media 105b5352): Wouter I. Schievink, Virginia V. Michels, Bahram Mokri, David G. Piepgras, and Harold O. Perry. Brief report: a familial syndrome of arterial dissections with lentiginosis. The New England journal of medicine, 332 9:576-9, Mar 1995. URL: https://doi.org/10.1056/nejm199503023320905, doi:10.1056/nejm199503023320905. This article has 73 citations and is from a highest quality peer-reviewed journal.

11. (schievink1995briefreporta media 87dd50de): Wouter I. Schievink, Virginia V. Michels, Bahram Mokri, David G. Piepgras, and Harold O. Perry. Brief report: a familial syndrome of arterial dissections with lentiginosis. The New England journal of medicine, 332 9:576-9, Mar 1995. URL: https://doi.org/10.1056/nejm199503023320905, doi:10.1056/nejm199503023320905. This article has 73 citations and is from a highest quality peer-reviewed journal.