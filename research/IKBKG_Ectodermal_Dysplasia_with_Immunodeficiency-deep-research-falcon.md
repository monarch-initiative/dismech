---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:08:57.754869'
end_time: '2026-04-24T18:28:03.471565'
duration_seconds: 1145.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IKBKG ectodermal dysplasia with immunodeficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IKBKG ectodermal dysplasia with immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IKBKG ectodermal dysplasia with immunodeficiency** covering all of the
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
- **Disease Name:** IKBKG ectodermal dysplasia with immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IKBKG ectodermal dysplasia with immunodeficiency** covering all of the
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


# IKBKG ectodermal dysplasia with immunodeficiency (IKBKG-EDA-ID) — Disease characteristics report

**Scope note.** This report synthesizes information primarily from aggregated disease resources and peer‑reviewed reviews/case series, complemented by recent case reports (2023–2024) for “latest research” signals; it is not derived from EHR-only data. Key limitations: (i) no MONDO/MeSH/ICD identifiers were directly available in the retrieved full texts, so those fields are flagged as *not confirmed from primary sources in this run*; (ii) several foundational mechanistic and cohort-frequency statements come from pre‑2023 landmark papers/reviews because the disorder is rare. 

---

## 1. Disease information

### 1.1 Concise overview
IKBKG ectodermal dysplasia with immunodeficiency (also called **X‑linked anhidrotic/hypohidrotic ectodermal dysplasia with immunodeficiency**, EDA‑ID/HED‑ID) is a **Mendelian X‑linked** inborn error of immunity caused by **hypomorphic (residual-function) variants in IKBKG (NEMO/IKKγ)**. The disorder couples **ectodermal dysplasia** (abnormal development of sweat glands, hair, teeth, skin, nails) with **combined immunodeficiency** and a characteristic susceptibility to **pyogenic bacteria, mycobacteria, and herpesviruses**. (keller2011hypohidroticectodermaldysplasia pages 1-2, dassante2016unravelingthelink pages 2-4)

A core mechanistic concept is that **complete IKBKG loss of function is usually male‑lethal**, while **partial loss** permits survival but causes EDA‑ID; in heterozygous females, loss‑of‑function variants classically manifest as **incontinentia pigmenti (IP)** because X‑inactivation creates mosaicism. (pescatore2022humangeneticdiseases pages 1-3, zonana2000anovelxlinked pages 4-6)

### 1.2 Key identifiers (with evidence in this run)
- **OMIM:** XL‑EDA‑ID / HED‑ID **OMIM #300291** (keller2011hypohidroticectodermaldysplasia pages 1-2, callea2020covid‐19and pages 1-2)
- **Related allelic disorders:** 
  - **Incontinentia pigmenti (IP): OMIM #308300** (callea2020covid‐19and pages 1-2)
  - **Osteopetrosis/lymphedema with EDA‑ID (OL‑EDA‑ID): OMIM #300301** (callea2020covid‐19and pages 1-2, dassante2016unravelingthelink pages 2-4)

**Not confirmed in retrieved texts:** MONDO ID, Orphanet disease ID, ICD‑10/ICD‑11 code(s), MeSH descriptor(s).

### 1.3 Synonyms / alternative names
Commonly used synonyms include: **EDA‑ID**, **XL‑EDA‑ID**, **HED‑ID**, **EDAXID**, and **NEMO deficiency syndrome**. (keller2011hypohidroticectodermaldysplasia pages 1-2, callea2020covid‐19and pages 1-2, zonana2000anovelxlinked pages 1-2)

| Concept/Label | Key synonyms | Primary gene | Inheritance | Key OMIM IDs (and related allelic disorders) | Notes | Key citations (context IDs) |
|---|---|---|---|---|---|---|
| IKBKG ectodermal dysplasia with immunodeficiency | EDA-ID; XL-EDA-ID; XR-EDA-ID; HED-ID; hypohidrotic ectodermal dysplasia with immunodeficiency; anhidrotic ectodermal dysplasia with immunodeficiency; EDAXID; NEMO deficiency syndrome | **IKBKG** (encodes NEMO/IKKγ) | X-linked recessive in affected males with hypomorphic variants | **OMIM 300291**; related allelic disorders: incontinentia pigmenti **OMIM 308300**; OL-EDA-ID / hypohidrotic ED with immunodeficiency, osteopetrosis and lymphedema **OMIM 300301** | Core phenotype combines ectodermal dysplasia with immunodeficiency due to impaired NF-κB signaling; typical ectodermal features include abnormal teeth, sparse hair, and hypohidrosis; severe infections are characteristic | (keller2011hypohidroticectodermaldysplasia pages 1-2, callea2020covid‐19and pages 1-2, dassante2016unravelingthelink pages 2-4, doffinger2001xlinkedanhidroticectodermal pages 1-2) |
| NEMO-related HED-ID in males | male HED-ID; male EDA-ID; X-linked HED-ID | **IKBKG / NEMO** | X-linked; hemizygous males survive when variants are hypomorphic rather than complete loss-of-function | **OMIM 300291** | Complete loss-of-function is generally male-lethal; surviving affected males usually have residual NEMO/NF-κB activity | (zonana2000anovelxlinked pages 1-2, zonana2000anovelxlinked pages 4-6, pescatore2022humangeneticdiseases pages 1-3, pescatore2022humangeneticdiseases pages 3-4) |
| Allelic relationship to incontinentia pigmenti | IP-related NEMO disease; allelic to IP | **IKBKG / NEMO** | IP is typically X-linked dominant in females; EDA-ID is the allelic hypomorphic male phenotype | **OMIM 308300** (IP); **OMIM 300291** (EDA-ID) | Multiple reviews describe EDA-ID and IP as “two faces of the same coin,” with phenotype depending on residual NF-κB activity, mosaicism, and X-inactivation | (fusco2015edaidandip pages 3-5, pescatore2022humangeneticdiseases pages 1-3, pescatore2022humangeneticdiseases pages 7-9, cifaldi2025partiallossof pages 13-14) |
| OL-EDA-ID / related severe allelic phenotype | osteopetrosis-lymphedema-EDA-ID; OL-HED-ID | **IKBKG / NEMO** | X-linked | **OMIM 300301** | Related but more severe allelic syndrome that adds osteopetrosis and lymphedema to ectodermal dysplasia with immunodeficiency | (dassante2016unravelingthelink pages 2-4, fusco2015edaidandip pages 5-7, callea2020covid‐19and pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 2-2) |
| Gene/protein label | NEMO; IKKγ; NF-κB essential modulator | **IKBKG** | Not applicable | Not disease OMIM-specific | NEMO is the regulatory subunit of the IKK complex required for canonical NF-κB activation; this explains why IKBKG variants affect both immunity and ectodermal development | (keller2011hypohidroticectodermaldysplasia pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 2-2, mcdonald2014humanimmunodeficienciesresulting pages 2-4, doffinger2001xlinkedanhidroticectodermal pages 1-2) |


*Table: This table summarizes the main disease labels, synonyms, gene assignment, inheritance, and OMIM relationships for IKBKG/NEMO-associated ectodermal dysplasia with immunodeficiency. It is useful for harmonizing terminology across clinical, genetic, and knowledge-base records.*

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline **hypomorphic variants** in **IKBKG** (Xq28), encoding **NEMO (NF‑κB essential modulator; IKKγ)**, which is required for canonical NF‑κB activation. (keller2011hypohidroticectodermaldysplasia pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 1-2)

**Allelic series:** distinct IKBKG variant classes produce related phenotypes, including IP (typically female), OL‑EDA‑ID, isolated immunodeficiency, and atypical mycobacterial susceptibility phenotypes. (fusco2015edaidandip pages 5-7, fusco2015edaidandip pages 3-5)

### 2.2 Risk factors
- **Genetic:** being a hemizygous male with a hypomorphic IKBKG variant (X‑linked). (zonana2000anovelxlinked pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 1-2)
- **Iatrogenic/exposure:** live mycobacterial vaccination exposure (e.g., BCG) is clinically relevant because mycobacterial susceptibility is common in the NEMO deficiency spectrum and has been implicated in disseminated mycobacterial disease in this disorder family. (haverkamp2014correlatinginterleukin12stimulated pages 8-8, meric2024atypicalmycobacterialpneumonia pages 1-2)

**Environmental/lifestyle risk factors:** no specific non-genetic risk factors were identified in the retrieved disease-specific sources; infection risk is driven primarily by the immunodeficiency. 

### 2.3 Protective factors
No protective genetic or environmental factors were directly reported in the retrieved texts.

### 2.4 Gene–environment interactions
Relevant interaction: **pathogen exposure** (including environmental nontuberculous mycobacteria and vaccine-strain mycobacteria) interacts with impaired NF‑κB signaling to produce severe disease phenotypes. (haverkamp2014correlatinginterleukin12stimulated pages 8-8, picard2011infectiousdiseasesin pages 4-5)

---

## 3. Phenotypes

### 3.1 Major clinical phenotype categories
**Ectodermal dysplasia features**
- Hypohidrosis/anhidrosis, sparse hair/hypotrichosis, abnormal dentition (including conical teeth, hypodontia/oligodontia), eczema/ichthyosis, nail abnormalities. (keller2011hypohidroticectodermaldysplasia pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 1-2, puvilland2021edaidasevere pages 1-3)

**Infectious susceptibility**
- Broad susceptibility with a strong signal for **pyogenic bacteria** and **mycobacteria**, with also viral and opportunistic pathogens (e.g., Pneumocystis). (picard2011infectiousdiseasesin pages 4-5, doffinger2001xlinkedanhidroticectodermal pages 2-2)

**Inflammation/organ complications**
- Colitis/IBD-like disease, bronchiectasis, failure to thrive; osteopetrosis/lymphedema in the OL‑EDA‑ID allelic form. (doffinger2001xlinkedanhidroticectodermal pages 2-2, puvilland2021edaidasevere pages 1-3, dassante2016unravelingthelink pages 2-4)

### 3.2 Frequency / statistics (from cohort reviews)
From a major infectious-disease review of NEMO deficiency (including EDA‑ID presentations):
- **Pyogenic bacterial infections** in ~**90%** of NEMO patients (picard2011infectiousdiseasesin pages 4-5)
- **Mycobacterial infections** in ~**40%** (picard2011infectiousdiseasesin pages 4-5)
- **Serious viral infections** in **19%** (picard2011infectiousdiseasesin pages 4-5)
- ~**90%** have ectodermal dysplasia features (picard2011infectiousdiseasesin pages 4-5)

### 3.3 Typical onset and course
In early family descriptions, affected boys often presented **within the first 2 years of life with life‑threatening infections** and ectodermal findings such as hypohidrosis and hypodontia/conical teeth. (zonana2000anovelxlinked pages 4-6, zonana2000anovelxlinked pages 2-4)

### 3.4 Suggested HPO terms
| Clinical feature | Suggested HPO term(s) (HP:) | Typical onset | Notes/quantitative frequency if available | Key citations (context IDs) |
|---|---|---|---|---|
| Hypohidrosis / anhidrosis | HP:0000975 Hypohidrosis; HP:0000870 Anhidrosis | Congenital / infancy | Core ectodermal feature of EDA-ID; described with absent sweat glands and heat intolerance in classic reports | (keller2011hypohidroticectodermaldysplasia pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 1-2) |
| Sparse scalp hair / hypotrichosis | HP:0008070 Sparse scalp hair; HP:0001006 Hypotrichosis | Congenital / infancy | Part of the classic ectodermal dysplasia triad; often accompanies abnormal teeth and hypohidrosis | (keller2011hypohidroticectodermaldysplasia pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 1-2, fusco2015edaidandip pages 3-5) |
| Abnormal / conical teeth | HP:0006482 Conical teeth; HP:0000670 Abnormality of dentition | Childhood, often evident with tooth eruption | Classic dental sign in EDA-ID; “rare conical teeth” repeatedly noted. IP/IKBKG-associated cohorts show dental involvement frequently; IP cohort reported teeth involvement in 58.7% and broader IP literature cites ~30–50% with tooth agenesis/oral anomalies | (doffinger2001xlinkedanhidroticectodermal pages 1-2, fusco2015edaidandip pages 3-5, cammaratascalisi2024maingeneticentities pages 4-5, herlin2024prevalenceandclinical pages 1-3) |
| Hypodontia / oligodontia / tooth agenesis | HP:0009804 Hypodontia; HP:0000674 Oligodontia; HP:0009805 Tooth agenesis | Childhood | Frequently grouped with abnormal dentition in ectodermal dysplasia; Cammarata-Scalisi 2024 links IKBKG-related disease to hypodontia, delayed eruption, abnormal shape and spacing | (keller2011hypohidroticectodermaldysplasia pages 1-2, cammaratascalisi2024maingeneticentities pages 4-5, zonana2000anovelxlinked pages 2-4) |
| Delayed tooth eruption / microdontia | HP:0000684 Delayed eruption of teeth; HP:0009827 Microdontia | Childhood | Reported in IKBKG-related oral phenotypes, especially in broader IP/IKBKG dental literature rather than EDA-ID-only cohorts | (cammaratascalisi2024maingeneticentities pages 4-5) |
| Recurrent severe bacterial infections | HP:0002718 Recurrent bacterial infections; HP:0002721 Recurrent infections | Infancy / early childhood | Major feature of EDA-ID; life-threatening infections often present in first 2 years of life. Picard review: pyogenic bacterial infections in ~90% of NEMO patients | (picard2011infectiousdiseasesin pages 4-5, zonana2000anovelxlinked pages 4-6, fusco2015edaidandip pages 3-5) |
| Recurrent sinopulmonary infections / pneumonia | HP:0006532 Recurrent pneumonia; HP:0012379 Bronchitis; HP:0002783 Recurrent upper respiratory tract infections | Infancy / childhood | Common real-world presentation; Meric 2024 siblings had recurrent sinopulmonary infections and pneumonia. Picard review lists pneumonia among frequent infections | (meric2024atypicalmycobacterialpneumonia pages 1-2, meric2024atypicalmycobacterialpneumonia pages 2-3, picard2011infectiousdiseasesin pages 4-5) |
| Bronchiectasis | HP:0002110 Bronchiectasis | Childhood, progressive after recurrent infections | Reported in severe patients with recurrent respiratory infection; documented in Döffinger 2001 and Meric 2024 | (doffinger2001xlinkedanhidroticectodermal pages 2-2, meric2024atypicalmycobacterialpneumonia pages 1-2) |
| Mycobacterial infection susceptibility | HP:0002726 Recurrent mycobacterial infections; HP:0032167 Increased susceptibility to mycobacterial infection | Childhood | Hallmark of NEMO deficiency spectrum. Picard review: mycobacterial infections in ~40% of NEMO patients; includes M. avium, M. kansasii, BCG-related disease, and M. bovis in 2024 siblings | (picard2011infectiousdiseasesin pages 4-5, haverkamp2014correlatinginterleukin12stimulated pages 8-8, meric2024atypicalmycobacterialpneumonia pages 1-2, fusco2015edaidandip pages 3-5) |
| Opportunistic fungal infection / Pneumocystis | HP:0005381 Recurrent fungal infections; HP:0012387 Pneumocystis jirovecii pneumonia | Infancy / childhood | Reported in severe phenotypes; examples include Pneumocystis infection in Döffinger 2001 and Puvilland 2021 | (doffinger2001xlinkedanhidroticectodermal pages 2-2, puvilland2021edaidasevere pages 1-3, george2023infectionsininborn pages 5-6) |
| Severe viral infection / CMV / HSV | HP:0004429 Recurrent viral infections | Infancy / childhood | Picard review: serious viral infections in 19% of NEMO patients; CMV and HSV reported in case series | (picard2011infectiousdiseasesin pages 4-5, puvilland2021edaidasevere pages 1-3, fusco2015edaidandip pages 3-5) |
| Colitis / inflammatory bowel disease-like enterocolitis | HP:0002037 Diarrhea; HP:0100279 Inflammatory bowel disease; HP:0002012 Abnormality of the intestine | Infancy / childhood | GI inflammation is part of the expanded phenotype; Döffinger reports recurrent GI infection/ulceration, Puvilland reports IBD-like colitis | (doffinger2001xlinkedanhidroticectodermal pages 2-2, puvilland2021edaidasevere pages 1-3) |
| Failure to thrive | HP:0001508 Failure to thrive | Infancy / childhood | Common consequence of severe infection/GI disease; described in Döffinger 2001 and Meric 2024 | (doffinger2001xlinkedanhidroticectodermal pages 2-2, meric2024atypicalmycobacterialpneumonia pages 1-2) |
| Eczema / dry skin / ichthyosis | HP:0000964 Eczema; HP:0001024 Ichthyosis; HP:0000958 Dry skin | Infancy / childhood | Skin abnormalities can accompany ectodermal findings; Keller notes eczema among HED features, Puvilland reports ichthyosis | (keller2011hypohidroticectodermaldysplasia pages 1-2, puvilland2021edaidasevere pages 1-3) |
| Nail dysplasia / nail abnormality | HP:0001597 Nail dysplasia; HP:0001197 Abnormality of nail morphology | Childhood | Part of the ectodermal anomaly spectrum; emphasized in broader syndrome descriptions and case reports | (puvilland2021edaidasevere pages 1-3, fusco2015edaidandip pages 5-7) |
| Lymphedema | HP:0001004 Lymphedema | Variable, often childhood | More characteristic of the severe allelic OL-EDA-ID phenotype than isolated EDA-ID | (dassante2016unravelingthelink pages 2-4, doffinger2001xlinkedanhidroticectodermal pages 2-2) |
| Osteopetrosis | HP:0011002 Osteopetrosis | Childhood | Seen in the allelic OL-EDA-ID form rather than typical EDA-ID; important for differential diagnosis within IKBKG disease spectrum | (dassante2016unravelingthelink pages 2-4, doffinger2001xlinkedanhidroticectodermal pages 2-2) |
| Hypogammaglobulinemia | HP:0004313 Decreased circulating IgG level; HP:0002845 Hypogammaglobulinemia | Infancy / childhood | Frequent laboratory phenotype; reduced IgG and impaired humoral immunity are recurrent findings across cohorts | (dassante2016unravelingthelink pages 2-4, callea2020covid‐19and pages 1-2, fusco2015edaidandip pages 3-5) |
| Elevated IgM / hyper-IgM-like phenotype | HP:0010703 Increased circulating IgM level | Infancy / childhood | Variable but repeatedly reported; some patients show reduced IgG with increased IgM or IgA. Example: IgM 4.6 g/L in severe 2021 case | (puvilland2021edaidasevere pages 1-3, giancane2013anhidroticectodermaldysplasia pages 3-3, zonana2000anovelxlinked pages 2-4) |
| Poor specific antibody response to polysaccharides | HP:0010773 Abnormality of immune system physiology; HP:0002721 Recurrent infections | Childhood (after immunization/testing) | A defining immunologic defect in many patients; Fusco review states all analyzed patients lacked polysaccharide-specific antibodies | (picard2011infectiousdiseasesin pages 4-5, fusco2015edaidandip pages 5-7) |
| Memory B-cell deficiency / low switched memory B cells | HP:0011837 Abnormal B-cell subset distribution | Childhood | Meric 2024 documented markedly reduced class-switched memory B cells in both siblings | (meric2024atypicalmycobacterialpneumonia pages 1-2, meric2024atypicalmycobacterialpneumonia pages 2-3) |
| T-cell lymphopenia / abnormal T-cell function | HP:0005403 T-cell lymphopenia; HP:0002843 Abnormality of T-cell function | Infancy / childhood | Variable across genotypes; includes reduced T-cell counts, absent memory T cells, and poor TCR-driven responses | (dassante2016unravelingthelink pages 2-4, giancane2013anhidroticectodermaldysplasia pages 3-3, meric2024atypicalmycobacterialpneumonia pages 2-3) |
| Impaired NK-cell cytotoxicity | HP:0011888 Abnormal natural killer cell function | Childhood | Reported in NEMO deficiency and contributes to broad infection susceptibility | (callea2020covid‐19and pages 1-2, fusco2015edaidandip pages 3-5) |


*Table: This table maps the major clinical and laboratory features reported for IKBKG/NEMO-associated ectodermal dysplasia with immunodeficiency to suggested HPO terms. It is useful for structuring phenotype annotations in a disease knowledge base and highlights where limited quantitative frequency data are available.*

### 3.5 Quality of life impact (evidence-based qualitative summary)
Although formal QoL instruments were not reported in the retrieved texts, the disease implies substantial QoL burden through recurrent/severe infections (hospitalizations, chronic lung disease/bronchiectasis) and ectodermal manifestations (heat intolerance from hypohidrosis; dental anomalies requiring long-term dental care). (keller2011hypohidroticectodermaldysplasia pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 2-2, cammaratascalisi2024maingeneticentities pages 4-5)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **IKBKG** (encodes **NEMO/IKKγ**, regulatory subunit of the IKK complex). (keller2011hypohidroticectodermaldysplasia pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 1-2)

### 4.2 Pathogenic variant classes and examples
A compiled review of EDA‑ID reports **29 distinct IKBKG mutations**, **24 associated with EDA‑ID**, including **missense, nonsense, frameshift, splice-site**, in‑frame deletion, nonstop mutation, and duplication. (fusco2015edaidandip pages 5-7)

**Recent 2024 example:** two male siblings with atypical mycobacterial pneumonia carried a novel hemizygous **frameshift** variant **c.268delG (p.Ala90Glnfs*93)**; immunologic findings included reduced class‑switched memory B cells and the management included immunoglobulin replacement and antibacterial prophylaxis. (meric2024atypicalmycobacterialpneumonia pages 1-2, meric2024atypicalmycobacterialpneumonia pages 2-3)

### 4.3 Inheritance, penetrance, expressivity
- **Inheritance pattern:** X‑linked (classically affecting males with hypomorphic alleles). (zonana2000anovelxlinked pages 1-2, doffinger2001xlinkedanhidroticectodermal pages 1-2)
- **Male lethality for complete loss:** complete loss‑of‑function IKBKG variants are typically **embryonically lethal in males**, whereas hypomorphic variants allow male survival with EDA‑ID. (pescatore2022humangeneticdiseases pages 1-3, zonana2000anovelxlinked pages 4-6)
- **Variable expressivity:** clinical heterogeneity is emphasized across cohorts and variants, including some individuals with immunodeficiency features without overt ectodermal dysplasia. (haverkamp2014correlatinginterleukin12stimulated pages 8-8, fusco2015edaidandip pages 7-8)

### 4.4 Modifier factors (genetic/epigenetic)
- **X‑inactivation/mosaicism** is a major modifier in females and in rare surviving males with IP‑phenotypes. Mosaicism and tissue selection can affect both clinical presentation and diagnostic yield. (pescatore2022humangeneticdiseases pages 3-4, pescatore2022humangeneticdiseases pages 4-6)

### 4.5 Allele frequency in population databases
Not reported in the retrieved texts.

---

## 5. Environmental information

No specific toxins/lifestyle factors were identified as etiologic drivers in the retrieved disease‑specific sources. Infection exposure is the dominant environmental driver of clinical events. (picard2011infectiousdiseasesin pages 4-5)

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic model (causal chain)
1) **IKBKG hypomorphic mutation → reduced NEMO function** (regulatory subunit of the IKK complex) (doffinger2001xlinkedanhidroticectodermal pages 1-2)
2) **Impaired but not abolished canonical NF‑κB activation** (doffinger2001xlinkedanhidroticectodermal pages 1-2)
3) Downstream consequences:
   - **Ectodermal defects:** ectodysplasin receptor signaling requires NEMO to activate NF‑κB; impaired signaling disrupts development of sweat glands, hair follicles, and dentition. (doffinger2001xlinkedanhidroticectodermal pages 1-2, keller2011hypohidroticectodermaldysplasia pages 1-2)
   - **Immune defects:** NEMO acts downstream of multiple immune receptors (TLR/IL‑1R/TNFR/CD40/TCR/BCR), producing combined immune dysfunction, particularly defective responses to bacterial glycans/polysaccharide antigens and impaired inflammatory cytokine responses that contribute to pyogenic and mycobacterial susceptibility. (dassante2016unravelingthelink pages 2-4, picard2011infectiousdiseasesin pages 4-5)

A key immunologic summary statement from a 2011 infectious-disease review is that most NEMO patients have impaired antibody responses (notably to glycans) and substantial rates of pyogenic and mycobacterial infections. (picard2011infectiousdiseasesin pages 4-5)

### 6.2 Cell types and processes (ontology suggestions)
**Cell Ontology (CL) suggestions (most implicated):**
- B cell: **CL:0000236** (humoral defects; low switched memory B cells) (meric2024atypicalmycobacterialpneumonia pages 1-2, meric2024atypicalmycobacterialpneumonia pages 2-3)
- T cell: **CL:0000084** (variable T-cell dysfunction/lymphopenia) (giancane2013anhidroticectodermaldysplasia pages 3-3, dassante2016unravelingthelink pages 2-4)
- Natural killer cell: **CL:0000623** (impaired cytotoxicity reported) (callea2020covid‐19and pages 1-2)
- Monocyte/macrophage: **CL:0000576/CL:0000235** (TLR/IL‑1/TNF signaling defects linked to mycobacterial susceptibility) (haverkamp2014correlatinginterleukin12stimulated pages 8-8, dassante2016unravelingthelink pages 2-4)

**Gene Ontology (GO) biological process suggestions:**
- **NF‑κB signaling** (e.g., “I‑κB kinase/NF‑κB signaling”) (doffinger2001xlinkedanhidroticectodermal pages 1-2)
- **Innate immune response** and **response to lipopolysaccharide/IL‑1/TNF** (doffinger2001xlinkedanhidroticectodermal pages 2-2, dassante2016unravelingthelink pages 2-4)
- **Immunoglobulin class switch recombination / adaptive immune response** (hyper‑IgM-like patterns and impaired antibody responses) (dassante2016unravelingthelink pages 2-4, puvilland2021edaidasevere pages 1-3)
- **Ectodermal appendage development** (sweat gland/hair/tooth development via ectodysplasin–NF‑κB axis) (doffinger2001xlinkedanhidroticectodermal pages 1-2)

---

## 7. Anatomical structures affected

**Primary systems:**
- **Integumentary/ectodermal derivatives:** skin, sweat glands, hair, nails, teeth. (keller2011hypohidroticectodermaldysplasia pages 1-2, callea2020covid‐19and pages 1-2)
- **Immune system:** combined immunodeficiency affecting humoral and cellular arms. (keller2011hypohidroticectodermaldysplasia pages 1-2, dassante2016unravelingthelink pages 2-4)

**Common secondary involvement/complications:**
- **Respiratory tract/lungs:** recurrent pneumonia and **bronchiectasis**. (doffinger2001xlinkedanhidroticectodermal pages 2-2, meric2024atypicalmycobacterialpneumonia pages 1-2)
- **Gastrointestinal tract:** diarrhea, ulcerations, colitis/IBD-like. (doffinger2001xlinkedanhidroticectodermal pages 2-2, puvilland2021edaidasevere pages 1-3)

**UBERON suggestions (examples):**
- Skin: **UBERON:0002097**
- Tooth: **UBERON:0001091**
- Lung: **UBERON:0002048**
- Intestine: **UBERON:0000160**

---

## 8. Temporal development

- **Onset:** typically congenital ectodermal findings and **early childhood** onset of recurrent/severe infections; in classic pedigrees, severe infections often occur within the first two years. (zonana2000anovelxlinked pages 4-6, zonana2000anovelxlinked pages 2-4)
- **Course:** variable; can progress to chronic lung disease (bronchiectasis) and chronic inflammatory complications (e.g., colitis). (doffinger2001xlinkedanhidroticectodermal pages 2-2, puvilland2021edaidasevere pages 1-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Disease-specific prevalence is rarely measured; one source provides an estimate of **HED‑ID ~1 in 250,000 newborns** (contrasted with XLHED ~1 in 100,000). (keller2011hypohidroticectodermaldysplasia pages 1-2)

For epidemiologic context of IKBKG allelic disorders, a nationwide Danish IP study reported **birth prevalence 2.37 per 100,000** (1 in 42,194) and point prevalence 1.21 per 100,000, with **71/75 female** in the validated cohort. (herlin2024prevalenceandclinical pages 1-3, herlin2024prevalenceandclinical pages 6-7)

### 9.2 Sex ratio and de novo rate (context from IP)
In the Danish IP cohort, 94.7% were female; genetic confirmation was present in 72% of cases, and the recurrent exon 4–10 deletion was the most common genotype among those with genetic diagnoses. (herlin2024prevalenceandclinical pages 1-3)

---

## 10. Diagnostics

### 10.1 Clinical suspicion
Consider IKBKG‑EDA‑ID when ectodermal dysplasia signs (hypohidrosis, abnormal teeth, sparse hair) co‑occur with recurrent or severe infections, particularly pyogenic bacteria and mycobacteria. (keller2011hypohidroticectodermaldysplasia pages 1-2, picard2011infectiousdiseasesin pages 4-5)

### 10.2 Immunologic testing (real-world implementation)
Typical abnormalities include hypogammaglobulinemia and impaired specific antibody responses, including to polysaccharide antigens; class‑switched memory B‑cell deficiency may be observed. (dassante2016unravelingthelink pages 2-4, meric2024atypicalmycobacterialpneumonia pages 2-3)

### 10.3 Genetic testing strategy and pitfalls
- Sequencing of **IKBKG** is diagnostic in males with suspected EDA‑ID; a 2024 report used an MSMD panel followed by IKBKG sequencing and Sanger confirmation. (meric2024atypicalmycobacterialpneumonia pages 1-2)
- Diagnostic pitfalls include the presence of a **pseudogene** and structural complexity at the IKBKG locus and potential **mosaicism**, which may require tissue‑appropriate sampling and CNV-aware methods in related IKBKG disorders. (zonana2000anovelxlinked pages 2-4, pescatore2022humangeneticdiseases pages 4-6)

### 10.4 Differential diagnosis
- **EDA pathway HED (EDA/EDAR/EDARADD)** without immunodeficiency (phenotypic overlap at ectodermal level). (keller2011hypohidroticectodermaldysplasia pages 1-2)
- **Autosomal dominant EDA‑ID due to NFKBIA (IκBα) variants**, which can also present with ectodermal dysplasia and immunodeficiency. (giancane2013anhidroticectodermaldysplasia pages 3-3, picard2011infectiousdiseasesin pages 4-5)

---

## 11. Outcome / prognosis

Historical summaries emphasize substantial childhood morbidity and mortality; one review states that **about half of known patients die in childhood** (reflecting older case series and ascertainment of severe cases). (fusco2015edaidandip pages 3-5)

---

## 12. Treatment

### 12.1 Anti-infective strategy (practice-relevant)
Because invasive bacterial infection can progress rapidly, one authoritative review recommends **immediate empiric parenteral antibiotics** at first suspicion or moderate fever, targeting **S. pneumoniae, S. aureus, and P. aeruginosa** in NEMO deficiency. (picard2011infectiousdiseasesin pages 4-5)

### 12.2 Immunoglobulin replacement and prophylaxis
A 2024 case report of two affected brothers documented initiation of **immunoglobulin replacement** and **antibacterial prophylaxis** as part of management. (meric2024atypicalmycobacterialpneumonia pages 1-2)

### 12.3 Hematopoietic stem cell transplantation (HSCT)
HSCT has been used in EDA‑ID, including reports of successful transplant in at least one child, but ectodermal defects are not corrected by HSCT and outcomes can be variable. (giancane2013anhidroticectodermaldysplasia pages 3-3, puvilland2021edaidasevere pages 4-6)

### 12.4 Supportive ectodermal/airway care
Supportive measures aimed at airway/nasal dryness and crusting (humidification, saline, gentle crust removal; topical antibiotic ointments during acute infections) have been proposed in ED patients including XL‑EDA‑ID to reduce sinonasal symptoms and infections. (callea2020covid‐19and pages 1-2)

### 12.5 MAXO (Medical Action Ontology) suggestions
- Immunoglobulin replacement therapy (MAXO term suggestion: “immunoglobulin replacement therapy”) (meric2024atypicalmycobacterialpneumonia pages 1-2)
- Antibiotic prophylaxis / antimicrobial prophylaxis (MAXO suggestion) (meric2024atypicalmycobacterialpneumonia pages 1-2, meric2024atypicalmycobacterialpneumonia pages 2-3)
- Hematopoietic stem cell transplantation (MAXO suggestion) (giancane2013anhidroticectodermaldysplasia pages 3-3, puvilland2021edaidasevere pages 4-6)
- Empiric parenteral antibiotic therapy for suspected sepsis (MAXO suggestion) (picard2011infectiousdiseasesin pages 4-5)

---

## 13. Prevention

**Primary/tertiary prevention** in practice is dominated by infection prevention and rapid treatment:
- Rapid initiation of empiric antibiotics for suspected invasive bacterial infections in NEMO deficiency. (picard2011infectiousdiseasesin pages 4-5)
- Ongoing antimicrobial prophylaxis and immunoglobulin replacement in patients with antibody deficiency phenotypes. (meric2024atypicalmycobacterialpneumonia pages 1-2, meric2024atypicalmycobacterialpneumonia pages 2-3)

**Vaccination considerations:** Disease literature emphasizes mycobacterial susceptibility (including BCG-related disease in the broader NEMO deficiency spectrum), supporting individualized vaccine planning; specific guideline statements were not present in the retrieved texts. (haverkamp2014correlatinginterleukin12stimulated pages 8-8)

---

## 14. Other species / natural disease

No naturally occurring animal EDA‑ID equivalent was characterized in the retrieved evidence set for this run.

---

## 15. Model organisms

- **Mouse:** NEMO/IKBKG loss-of-function is embryonically lethal in mice; inflammatory/skin phenotypes in heterozygous females and cell-death pathway dependence (e.g., TNF/RIPK1 axis) have been discussed as relevant to IP/NEMO biology, providing mechanistic context for allelic IKBKG disorders including EDA‑ID. (pescatore2022humangeneticdiseases pages 6-7, pescatore2022humangeneticdiseases pages 1-3)

---

## Visual evidence: mutation spectrum and domain mapping
The following extracted figure/table summarizes NEMO protein domains and the distribution of EDA‑ID–associated mutations, along with a mutation catalogue.

- NEMO domain map with mutation positions: (fusco2015edaidandip media a25bf9d6)
- Table of reported IKBKG/NEMO mutations in EDA‑ID: (fusco2015edaidandip media bf13b1f4)

---

## Recent developments (2023–2024 highlights)
- **2024 case report:** Two siblings with atypical mycobacterial pneumonia due to a novel hypomorphic IKBKG frameshift variant (c.268delG; p.Ala90Glnfs*93) illustrate ongoing discovery of novel variants and implementation of immunoglobulin replacement and prophylaxis. (meric2024atypicalmycobacterialpneumonia pages 1-2)
- **2024 epidemiology context:** A nationwide IP study (allelic IKBKG disorder) provided a modern population-based estimate (birth prevalence 2.37/100,000) and detailed organ involvement frequencies including teeth (58.7%), hair (26.7%), eyes (22.6%), and nails (16.0%). (herlin2024prevalenceandclinical pages 1-3)
- **2023 review signal:** A CID infections review includes EDA‑ID due to NEMO/IKBKG and lists common infection syndromes and pathogens (skin infections, pneumonia, sepsis; S. aureus, S. pneumoniae, P. aeruginosa, mycobacteria; HSV; Pneumocystis). (george2023infectionsininborn pages 5-6)

---

## Source URLs (as available in retrieved documents)
- Meric et al., *Turkish Archives of Pediatrics*, 2024-09. https://doi.org/10.5152/turkarchpediatr.2024.24087 (meric2024atypicalmycobacterialpneumonia pages 1-2)
- Herlin et al., *Orphanet Journal of Rare Diseases*, 2024-12. https://doi.org/10.1186/s13023-024-03480-8 (herlin2024prevalenceandclinical pages 1-3)
- George & Govindaraj, *Pathogens*, 2023-02. https://doi.org/10.3390/pathogens12020272 (george2023infectionsininborn pages 5-6)
- Keller et al., *Frontiers in Immunology*, 2011-10. https://doi.org/10.3389/fimmu.2011.00061 (keller2011hypohidroticectodermaldysplasia pages 1-2)
- Döffinger et al., *Nature Genetics*, 2001-03. https://doi.org/10.1038/85837 (doffinger2001xlinkedanhidroticectodermal pages 1-2)
- Picard et al., *Clinical Microbiology Reviews*, 2011-07. https://doi.org/10.1128/cmr.00001-11 (picard2011infectiousdiseasesin pages 4-5)
- Fusco et al., *International Reviews of Immunology*, 2015-08. https://doi.org/10.3109/08830185.2015.1055331 (fusco2015edaidandip pages 3-5)
- Callea et al., *Dermatologic Therapy*, 2020-07. https://doi.org/10.1111/dth.13702 (callea2020covid‐19and pages 1-2)


References

1. (keller2011hypohidroticectodermaldysplasia pages 1-2): Michael D. Keller, Maureen Petersen, Peck Ong, Joseph Church, Kimberly Risma, Jon Burham, Ashish Jain, E. Richard Stiehm, Eric P. Hanson, Gulbu Uzel, Matthew A. Deardorff, and Jordan S. Orange. Hypohidrotic ectodermal dysplasia and immunodeficiency with coincident nemo and eda mutations. Frontiers in Immunology, Oct 2011. URL: https://doi.org/10.3389/fimmu.2011.00061, doi:10.3389/fimmu.2011.00061. This article has 45 citations and is from a peer-reviewed journal.

2. (dassante2016unravelingthelink pages 2-4): Roberta D'Assante, Anna Fusco, Loredana Palamaro, Giuliana Giardino, Vera Gallo, Emilia Cirillo, and Claudio Pignata. Unraveling the link between ectodermal disorders and primary immunodeficiencies. International Reviews of Immunology, 35:25-38, Mar 2016. URL: https://doi.org/10.3109/08830185.2015.1010724, doi:10.3109/08830185.2015.1010724. This article has 16 citations and is from a peer-reviewed journal.

3. (pescatore2022humangeneticdiseases pages 1-3): Alessandra Pescatore, Ezia Spinosa, Carmela Casale, Maria Brigida Lioi, Matilde Valeria Ursini, and Francesca Fusco. Human genetic diseases linked to the absence of nemo: an obligatory somatic mosaic disorder in male. International Journal of Molecular Sciences, 23:1179, Jan 2022. URL: https://doi.org/10.3390/ijms23031179, doi:10.3390/ijms23031179. This article has 14 citations.

4. (zonana2000anovelxlinked pages 4-6): Jonathan Zonana, Melissa E. Elder, Lynda C. Schneider, Seth J. Orlow, Celia Moss, Mahin Golabi, Stuart K. Shapira, Peter A. Farndon, Diane W. Wara, Stephanie A. Emmal, and Betsy M. Ferguson. A novel x-linked disorder of immune deficiency and hypohidrotic ectodermal dysplasia is allelic to incontinentia pigmenti and due to mutations in ikk-gamma (nemo). American journal of human genetics, 67 6:1555-62, Dec 2000. URL: https://doi.org/10.1086/316914, doi:10.1086/316914. This article has 603 citations and is from a highest quality peer-reviewed journal.

5. (callea2020covid‐19and pages 1-2): Michele Callea, Colin Eric Willoughby, Diana Perry, Ulrike Holzer, Giulia Fedele, Antonio Cárdenas Tadich, and Francisco Cammarata‐Scalisi. <scp>covid</scp> ‐19 and ectodermal dysplasias. recommendations are necessary. Dermatologic Therapy, Jul 2020. URL: https://doi.org/10.1111/dth.13702, doi:10.1111/dth.13702. This article has 1 citations and is from a peer-reviewed journal.

6. (zonana2000anovelxlinked pages 1-2): Jonathan Zonana, Melissa E. Elder, Lynda C. Schneider, Seth J. Orlow, Celia Moss, Mahin Golabi, Stuart K. Shapira, Peter A. Farndon, Diane W. Wara, Stephanie A. Emmal, and Betsy M. Ferguson. A novel x-linked disorder of immune deficiency and hypohidrotic ectodermal dysplasia is allelic to incontinentia pigmenti and due to mutations in ikk-gamma (nemo). American journal of human genetics, 67 6:1555-62, Dec 2000. URL: https://doi.org/10.1086/316914, doi:10.1086/316914. This article has 603 citations and is from a highest quality peer-reviewed journal.

7. (doffinger2001xlinkedanhidroticectodermal pages 1-2): Rainer Döffinger, Asma Smahi, Christine Bessia, Frédéric Geissmann, Jacqueline Feinberg, Anne Durandy, Christine Bodemer, Sue Kenwrick, Sophie Dupuis-Girod, Stéphane Blanche, Philip Wood, Smail Hadj Rabia, Denis J. Headon, Paul A. Overbeek, Françoise Le Deist, Steven M. Holland, Kiran Belani, Dinakantha S. Kumararatne, Alain Fischer, Ralph Shapiro, Mary Ellen Conley, Eric Reimund, Hermann Kalhoff, Mario Abinun, Arnold Munnich, Alain Israël, Gilles Courtois, and Jean-Laurent Casanova. X-linked anhidrotic ectodermal dysplasia with immunodeficiency is caused by impaired nf-κb signaling. Nature Genetics, 27:277-285, Mar 2001. URL: https://doi.org/10.1038/85837, doi:10.1038/85837. This article has 992 citations and is from a highest quality peer-reviewed journal.

8. (pescatore2022humangeneticdiseases pages 3-4): Alessandra Pescatore, Ezia Spinosa, Carmela Casale, Maria Brigida Lioi, Matilde Valeria Ursini, and Francesca Fusco. Human genetic diseases linked to the absence of nemo: an obligatory somatic mosaic disorder in male. International Journal of Molecular Sciences, 23:1179, Jan 2022. URL: https://doi.org/10.3390/ijms23031179, doi:10.3390/ijms23031179. This article has 14 citations.

9. (fusco2015edaidandip pages 3-5): Francesca Fusco, Alessandra Pescatore, Matilde Immacolata Conte, Peppino Mirabelli, Mariateresa Paciolla, Elio Esposito, Maria Brigida Lioi, and Matilde Valeria Ursini. Eda-id and ip, two faces of the same coin: how the same ikbkg/nemo mutation affecting the nf-κb pathway can cause immunodeficiency and/or inflammation. International Reviews of Immunology, 34:445-459, Aug 2015. URL: https://doi.org/10.3109/08830185.2015.1055331, doi:10.3109/08830185.2015.1055331. This article has 118 citations and is from a peer-reviewed journal.

10. (pescatore2022humangeneticdiseases pages 7-9): Alessandra Pescatore, Ezia Spinosa, Carmela Casale, Maria Brigida Lioi, Matilde Valeria Ursini, and Francesca Fusco. Human genetic diseases linked to the absence of nemo: an obligatory somatic mosaic disorder in male. International Journal of Molecular Sciences, 23:1179, Jan 2022. URL: https://doi.org/10.3390/ijms23031179, doi:10.3390/ijms23031179. This article has 14 citations.

11. (cifaldi2025partiallossof pages 13-14): Cristina Cifaldi, Mayla Sgrulletti, Silvia Di Cesare, Beatrice Rivalta, Agolini Emanuele, Lucia Colucci, Giusella Maria Francesca Moscato, Marta Matraxia, Chiara Perrone, Gigliola Di Matteo, Caterina Cancrini, and Viviana Moschese. Partial loss of nemo function in a female carrier with no incontinentia pigmenti. Journal of Clinical Medicine, 14:363, Jan 2025. URL: https://doi.org/10.3390/jcm14020363, doi:10.3390/jcm14020363. This article has 0 citations.

12. (fusco2015edaidandip pages 5-7): Francesca Fusco, Alessandra Pescatore, Matilde Immacolata Conte, Peppino Mirabelli, Mariateresa Paciolla, Elio Esposito, Maria Brigida Lioi, and Matilde Valeria Ursini. Eda-id and ip, two faces of the same coin: how the same ikbkg/nemo mutation affecting the nf-κb pathway can cause immunodeficiency and/or inflammation. International Reviews of Immunology, 34:445-459, Aug 2015. URL: https://doi.org/10.3109/08830185.2015.1055331, doi:10.3109/08830185.2015.1055331. This article has 118 citations and is from a peer-reviewed journal.

13. (doffinger2001xlinkedanhidroticectodermal pages 2-2): Rainer Döffinger, Asma Smahi, Christine Bessia, Frédéric Geissmann, Jacqueline Feinberg, Anne Durandy, Christine Bodemer, Sue Kenwrick, Sophie Dupuis-Girod, Stéphane Blanche, Philip Wood, Smail Hadj Rabia, Denis J. Headon, Paul A. Overbeek, Françoise Le Deist, Steven M. Holland, Kiran Belani, Dinakantha S. Kumararatne, Alain Fischer, Ralph Shapiro, Mary Ellen Conley, Eric Reimund, Hermann Kalhoff, Mario Abinun, Arnold Munnich, Alain Israël, Gilles Courtois, and Jean-Laurent Casanova. X-linked anhidrotic ectodermal dysplasia with immunodeficiency is caused by impaired nf-κb signaling. Nature Genetics, 27:277-285, Mar 2001. URL: https://doi.org/10.1038/85837, doi:10.1038/85837. This article has 992 citations and is from a highest quality peer-reviewed journal.

14. (mcdonald2014humanimmunodeficienciesresulting pages 2-4): Douglas R. McDonald and Raif S. Geha. Human immunodeficiencies resulting from defective nf-κb activation. ArXiv, pages 665-686, Jan 2014. URL: https://doi.org/10.1016/b978-0-12-405546-9.00033-9, doi:10.1016/b978-0-12-405546-9.00033-9. This article has 2 citations.

15. (haverkamp2014correlatinginterleukin12stimulated pages 8-8): Margje H. Haverkamp, Beatriz E. Marciano, David M. Frucht, Ashish Jain, Esther van de Vosse, and Steven M. Holland. Correlating interleukin-12 stimulated interferon-γ production and the absence of ectodermal dysplasia and anhidrosis (eda) in patients with mutations in nf-κb essential modulator (nemo). Journal of Clinical Immunology, 34:436-443, Feb 2014. URL: https://doi.org/10.1007/s10875-014-9998-2, doi:10.1007/s10875-014-9998-2. This article has 19 citations and is from a domain leading peer-reviewed journal.

16. (meric2024atypicalmycobacterialpneumonia pages 1-2): Zeynep Meric, Sezin Aydemir, Azer Kilic Baskan, Betul Gemici Karaaslan, Yasemin Kendir Demirkol, Ayse Ayzit Kilinc Sakalli, Ayca Kiykim, and Haluk Cokugras 1. Atypical mycobacterial pneumonia in 2 siblings with a novel hypomorphic nemo/ikbkg mutation. Turkish Archives of Pediatrics, 59:605-607, Sep 2024. URL: https://doi.org/10.5152/turkarchpediatr.2024.24087, doi:10.5152/turkarchpediatr.2024.24087. This article has 2 citations.

17. (picard2011infectiousdiseasesin pages 4-5): Capucine Picard, Jean-Laurent Casanova, and Anne Puel. Infectious diseases in patients with irak-4, myd88, nemo, or iκbα deficiency. Clinical Microbiology Reviews, 24:490-497, Jul 2011. URL: https://doi.org/10.1128/cmr.00001-11, doi:10.1128/cmr.00001-11. This article has 494 citations and is from a highest quality peer-reviewed journal.

18. (puvilland2021edaidasevere pages 1-3): Coline Bret Puvilland, Bertrand Boisson, Mathieu Fusaro, Jacinta Bustamante, Yves Bertrand, Antony Ceraulo, and Marie Ouachée-Chardin. Eda-id: a severe clinical presentation associated with a new ikbkg mutation. Journal of Clinical Immunology, 41:1099-1102, Feb 2021. URL: https://doi.org/10.1007/s10875-021-00992-x, doi:10.1007/s10875-021-00992-x. This article has 9 citations and is from a domain leading peer-reviewed journal.

19. (zonana2000anovelxlinked pages 2-4): Jonathan Zonana, Melissa E. Elder, Lynda C. Schneider, Seth J. Orlow, Celia Moss, Mahin Golabi, Stuart K. Shapira, Peter A. Farndon, Diane W. Wara, Stephanie A. Emmal, and Betsy M. Ferguson. A novel x-linked disorder of immune deficiency and hypohidrotic ectodermal dysplasia is allelic to incontinentia pigmenti and due to mutations in ikk-gamma (nemo). American journal of human genetics, 67 6:1555-62, Dec 2000. URL: https://doi.org/10.1086/316914, doi:10.1086/316914. This article has 603 citations and is from a highest quality peer-reviewed journal.

20. (cammaratascalisi2024maingeneticentities pages 4-5): Francisco Cammarata-Scalisi, Colin E. Willoughby, Jinia R. El-Feghaly, Antonio Cárdenas Tadich, Maykol Araya Castillo, Shadi Alkhatib, Marwa Abd Elsalam Elsherif, Rabab K. El-Ghandour, Riccardo Coletta, Antonino Morabito, and Michele Callea. Main genetic entities associated with tooth agenesis. Clinical oral investigations, 29 1:9, Dec 2024. URL: https://doi.org/10.1007/s00784-024-05941-7, doi:10.1007/s00784-024-05941-7. This article has 7 citations and is from a domain leading peer-reviewed journal.

21. (herlin2024prevalenceandclinical pages 1-3): Laura Krogh Herlin, Sigrun Alba Johannesdottir Schmidt, Trine H. Mogensen, and Mette Sommerlund. Prevalence and clinical characteristics of incontinentia pigmenti: a nationwide population-based study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03480-8, doi:10.1186/s13023-024-03480-8. This article has 10 citations and is from a peer-reviewed journal.

22. (meric2024atypicalmycobacterialpneumonia pages 2-3): Zeynep Meric, Sezin Aydemir, Azer Kilic Baskan, Betul Gemici Karaaslan, Yasemin Kendir Demirkol, Ayse Ayzit Kilinc Sakalli, Ayca Kiykim, and Haluk Cokugras 1. Atypical mycobacterial pneumonia in 2 siblings with a novel hypomorphic nemo/ikbkg mutation. Turkish Archives of Pediatrics, 59:605-607, Sep 2024. URL: https://doi.org/10.5152/turkarchpediatr.2024.24087, doi:10.5152/turkarchpediatr.2024.24087. This article has 2 citations.

23. (george2023infectionsininborn pages 5-6): Kalpana George and Geeta Govindaraj. Infections in inborn errors of immunity with combined immune deficiency: a review. Pathogens, 12:272, Feb 2023. URL: https://doi.org/10.3390/pathogens12020272, doi:10.3390/pathogens12020272. This article has 20 citations.

24. (giancane2013anhidroticectodermaldysplasia pages 3-3): Gabriella Giancane, Simona Ferrari, Rita Carsetti, Paola Papoff, Metello Iacobini, and Marzia Duse. Anhidrotic ectodermal dysplasia: a new mutation. The Journal of allergy and clinical immunology, 132 6:1451-3, Dec 2013. URL: https://doi.org/10.1016/j.jaci.2013.05.034, doi:10.1016/j.jaci.2013.05.034. This article has 17 citations.

25. (fusco2015edaidandip pages 7-8): Francesca Fusco, Alessandra Pescatore, Matilde Immacolata Conte, Peppino Mirabelli, Mariateresa Paciolla, Elio Esposito, Maria Brigida Lioi, and Matilde Valeria Ursini. Eda-id and ip, two faces of the same coin: how the same ikbkg/nemo mutation affecting the nf-κb pathway can cause immunodeficiency and/or inflammation. International Reviews of Immunology, 34:445-459, Aug 2015. URL: https://doi.org/10.3109/08830185.2015.1055331, doi:10.3109/08830185.2015.1055331. This article has 118 citations and is from a peer-reviewed journal.

26. (pescatore2022humangeneticdiseases pages 4-6): Alessandra Pescatore, Ezia Spinosa, Carmela Casale, Maria Brigida Lioi, Matilde Valeria Ursini, and Francesca Fusco. Human genetic diseases linked to the absence of nemo: an obligatory somatic mosaic disorder in male. International Journal of Molecular Sciences, 23:1179, Jan 2022. URL: https://doi.org/10.3390/ijms23031179, doi:10.3390/ijms23031179. This article has 14 citations.

27. (herlin2024prevalenceandclinical pages 6-7): Laura Krogh Herlin, Sigrun Alba Johannesdottir Schmidt, Trine H. Mogensen, and Mette Sommerlund. Prevalence and clinical characteristics of incontinentia pigmenti: a nationwide population-based study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03480-8, doi:10.1186/s13023-024-03480-8. This article has 10 citations and is from a peer-reviewed journal.

28. (puvilland2021edaidasevere pages 4-6): Coline Bret Puvilland, Bertrand Boisson, Mathieu Fusaro, Jacinta Bustamante, Yves Bertrand, Antony Ceraulo, and Marie Ouachée-Chardin. Eda-id: a severe clinical presentation associated with a new ikbkg mutation. Journal of Clinical Immunology, 41:1099-1102, Feb 2021. URL: https://doi.org/10.1007/s10875-021-00992-x, doi:10.1007/s10875-021-00992-x. This article has 9 citations and is from a domain leading peer-reviewed journal.

29. (pescatore2022humangeneticdiseases pages 6-7): Alessandra Pescatore, Ezia Spinosa, Carmela Casale, Maria Brigida Lioi, Matilde Valeria Ursini, and Francesca Fusco. Human genetic diseases linked to the absence of nemo: an obligatory somatic mosaic disorder in male. International Journal of Molecular Sciences, 23:1179, Jan 2022. URL: https://doi.org/10.3390/ijms23031179, doi:10.3390/ijms23031179. This article has 14 citations.

30. (fusco2015edaidandip media a25bf9d6): Francesca Fusco, Alessandra Pescatore, Matilde Immacolata Conte, Peppino Mirabelli, Mariateresa Paciolla, Elio Esposito, Maria Brigida Lioi, and Matilde Valeria Ursini. Eda-id and ip, two faces of the same coin: how the same ikbkg/nemo mutation affecting the nf-κb pathway can cause immunodeficiency and/or inflammation. International Reviews of Immunology, 34:445-459, Aug 2015. URL: https://doi.org/10.3109/08830185.2015.1055331, doi:10.3109/08830185.2015.1055331. This article has 118 citations and is from a peer-reviewed journal.

31. (fusco2015edaidandip media bf13b1f4): Francesca Fusco, Alessandra Pescatore, Matilde Immacolata Conte, Peppino Mirabelli, Mariateresa Paciolla, Elio Esposito, Maria Brigida Lioi, and Matilde Valeria Ursini. Eda-id and ip, two faces of the same coin: how the same ikbkg/nemo mutation affecting the nf-κb pathway can cause immunodeficiency and/or inflammation. International Reviews of Immunology, 34:445-459, Aug 2015. URL: https://doi.org/10.3109/08830185.2015.1055331, doi:10.3109/08830185.2015.1055331. This article has 118 citations and is from a peer-reviewed journal.