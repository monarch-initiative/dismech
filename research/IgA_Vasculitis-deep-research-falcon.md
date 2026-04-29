---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-28T20:06:53.250521'
end_time: '2026-04-28T20:28:53.336320'
duration_seconds: 1320.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IgA Vasculitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IgA Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **IgA Vasculitis** covering all of the
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
- **Disease Name:** IgA Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **IgA Vasculitis** covering all of the
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


## Comprehensive Disease Characteristics Report: IgA Vasculitis (IgAV)

### Executive summary
IgA vasculitis (IgAV; formerly Henoch–Schönlein purpura, HSP) is an immune-complex, leukocytoclastic small-vessel vasculitis characterized by IgA-dominant immune deposition with a clinical tetrad of palpable purpura, joint involvement, gastrointestinal (GI) manifestations, and renal disease. Contemporary understanding emphasizes multifactorial triggers (often infections) acting on a genetically susceptible background and converging on aberrant IgA biology, complement activation, and neutrophil/endothelial injury. Kidney involvement drives long-term morbidity; most pediatric cases resolve, whereas adult disease is less common but often more severe and relapsing. (sestan2023diagnosticandmanagement pages 1-2, hu2024immunoglobulinavasculitis pages 1-2, castaneda2024igavasculitis(henoch–schönlein pages 1-2)

---

## 1. Disease information

### 1.1 Definition and overview
- IgAV is described as a systemic, leukocytoclastic small-vessel vasculitis (predominantly small vessels) with IgA immune-complex deposition and multisystem involvement. In a pediatric nephrology review, IgAV is “histologically characterised by infiltration of the walls of the blood vessels…by neutrophils with deposits of immune complexes containing predominantly IgA” and is “clinically manifested as purpuric rash accompanied by either gastrointestinal symptoms, arthritis, and/or nephritis.” (sestan2023diagnosticandmanagement pages 1-2)
- A 2024 review further frames IgAV as “an immune-mediated hypersensitivity disease caused by the deposition and immune complexes in small vessels and complement activation that recruits neutrophil polymorphs.” (parums2024areviewof pages 5-6)

### 1.2 Key identifiers and disease classification
- **Chapel Hill nomenclature (2012 revision):** the term *Henoch–Schönlein purpura* was replaced with *IgA vasculitis* (IgAV). (sestan2023diagnosticandmanagement pages 1-2)
- **Classification/diagnostic criteria used clinically:** pediatric sources emphasize reliance on **EULAR/PRINTO/PRES-endorsed Ankara 2008 classification criteria** in practice for pediatric IgAV/IgAV nephritis due to the lack of separate diagnostic criteria for nephritis. (sestan2023diagnosticandmanagement pages 1-2)
- **ICD / MeSH / MONDO / Orphanet:** these identifiers were not successfully retrieved in the accessible full-text evidence in this run; therefore, they are **not reported here** to avoid uncited assertions.

### 1.3 Synonyms and alternative names
- **IgA vasculitis (IgAV)**
- **Henoch–Schönlein purpura (HSP)** (sestan2023diagnosticandmanagement pages 1-2, castaneda2024igavasculitis(henoch–schönlein pages 1-2)

### 1.4 Evidence sources (patient-level vs aggregated)
- Evidence herein is derived from **aggregated disease-level resources** (reviews and nationwide cohorts) and **large EHR/registry cohorts** (PEDSnet; French BNDMR) as well as **single-center observational cohorts** and **biomarker studies**. (stone2023clinicalcourseand pages 1-2, maisons2023newinsightsinto pages 1-3, hocevar2023shorttermoutcomeof pages 1-2, wright2023urinarycomplementproteins pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors (mechanistic)
IgAV is best understood as an immune-complex small-vessel vasculitis driven by aberrant IgA biology and downstream inflammatory injury.
- Aberrant IgA biology: IgAV is triggered by immune complexes containing “hypoglycosylated IgA deposits” in a nationwide epidemiology study’s background statement. (maisons2023newinsightsinto pages 1-3)
- Reviews highlight interplay between “aberrantly glycosylated IgA, anti-endothelial cell antibodies, and neutrophils following infection triggers” as central pathogenic mechanisms. (hu2024immunoglobulinavasculitis pages 1-2)
- Complement and neutrophils: IgAV pathogenesis includes “complement activation that recruits neutrophil polymorphs.” (parums2024areviewof pages 5-6)

### 2.2 Risk factors
#### Infectious/environmental triggers
- In pediatric IgAV/IgAV nephritis review literature, “upper respiratory tract or gastrointestinal infections precede the onset of disease” in “more than 75% of patients,” and multiple bacterial/viral infections are described. (sestan2023diagnosticandmanagement pages 1-2)
- In the French nationwide cohort introduction, “Approximately 70% of IgAV patients have well-identified triggers…primarily respiratory tract or gastrointestinal infections.” (maisons2023newinsightsinto pages 1-3)

#### Demographic risk factors
- Pediatric disease predominance: “Globally, approximately 90% of the patients…are children,” and pediatric incidence is substantially higher than adult incidence. (hu2024immunoglobulinavasculitis pages 1-2)
- Male predominance is reported in pediatric epidemiology review (male:female ~1.5:1) and stronger male predominance in adults in French nationwide cohort (sex ratio 1.57 adults). (sestan2023diagnosticandmanagement pages 1-2, maisons2023newinsightsinto pages 1-3)

#### Genetic susceptibility
- Pediatric review: available GWAS to date emphasize **HLA class II** involvement and classify IgAV as “a prototype of a disease related to HLA class II loci.” (sestan2023diagnosticandmanagement pages 1-2)
- A 2024 Croatian pediatric cohort found susceptibility associations with **HLA-A*03**, **HLA-B*37**, and **HLA-DRB1*12** (with frequencies and p-values reported), and phenotype associations (GI involvement; nephritis) with specific HLA-DRB1 alleles. (held2024hlapolymorphismsand pages 1-2)

### 2.3 Protective factors
No clearly established protective environmental factors were identified in the retrieved evidence. Genetic protective HLA residues/haplotypes have been described in preprint-scale GWAS (see Genetics section), but these require peer-reviewed confirmation before being treated as definitive protective factors in a knowledge base. (liu2024genomewidestudiesdefine pages 6-8)

### 2.4 Gene–environment interactions
The retrieved evidence supports a model where infections frequently precede disease onset in a genetically susceptible host (HLA class II associations), consistent with gene–environment interaction; however, specific quantified interaction effects were not extracted from the available sources. (sestan2023diagnosticandmanagement pages 1-2, maisons2023newinsightsinto pages 1-3, held2024hlapolymorphismsand pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (clinical)
A 2024 review succinctly states: “Palpable purpura, gastrointestinal symptoms, joint involvement, and renal disease characterize immunoglobulin A vasculitis (IgAV).” (hu2024immunoglobulinavasculitis pages 1-2)

#### Major phenotypes, characteristics, and ontology suggestions
Below are commonly described phenotypes with suggested ontology mappings (HPO terms are suggestions for knowledge-base curation; they are not asserted as exact HPO IDs in the cited sources).

1) **Palpable purpura / purpuric rash**
- Type: clinical sign
- Frequency: emphasized as “the main attribute” in pediatric IgAV review. (sestan2023diagnosticandmanagement pages 1-2)
- HPO suggestion: *Palpable purpura*; *Purpura*

2) **Arthralgia/arthritis (joint involvement)**
- Type: symptom/sign
- Pediatric biomarker cohort: joint involvement in **76/86 (88.4%)**. (held2024insightintothe pages 2-4)
- HPO suggestions: *Arthralgia*; *Arthritis*

3) **Gastrointestinal involvement (abdominal pain/bleeding)**
- Type: symptom/sign
- Pediatric biomarker cohort: GI involvement in **39/86 (45.3%)**. (held2024insightintothe pages 2-4)
- HPO suggestions: *Abdominal pain*; *Gastrointestinal hemorrhage*

4) **Renal involvement / IgA vasculitis nephritis (IgAVN)**
- Type: laboratory abnormality/organ involvement
- Pediatric review: IgAVN occurs in **20–60%** of children with IgAV. (sestan2023diagnosticandmanagement pages 1-2)
- HPO suggestions: *Hematuria*; *Proteinuria*; *Glomerulonephritis*; *Reduced glomerular filtration rate*

5) **Relapsing/recurrent disease**
- Adult cohort: relapse in **42/265 (15.8%)** during median 24-month follow-up. (hocevar2023shorttermoutcomeof pages 1-2)
- Pediatric biomarker cohort: at least one recurrence in **21/86 (24.4%)**. (held2024insightintothe pages 2-4)
- HPO suggestions: *Relapsing disease course*

### 3.2 Onset and course (phenotype-level)
- Pediatric onset: median onset around 6 years; 90% <10 years. (sestan2023diagnosticandmanagement pages 1-2)
- Many patients are self-limited, but a subset develops refractory nephritis/chronic kidney failure (review-level statement). (hu2024immunoglobulinavasculitis pages 1-2)

### 3.3 Quality of life (QoL) impact
Direct QoL instrument statistics (e.g., SF-36 scores) were not extracted from the retrieved observational studies; however, a pediatric atypical-course case series reported high care utilization and psychosocial burden, including ED re-presentations and psychology referrals. Specifically, among 13 atypical pediatric cases, **10/13 (77%)** re-presented to the ED and **5/13 (38%)** were referred to psychology services; **7/13 (54%)** reported frustration. (marro2023acaseseries pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and inheritance
No monogenic causal gene model is supported by the retrieved evidence. IgAV is consistently presented as **complex/multifactorial**, with GWAS and candidate associations each contributing limited effect sizes. (sestan2023diagnosticandmanagement pages 1-2)

### 4.2 Susceptibility loci and candidate genes (recent developments prioritized)

#### 4.2.1 Large-scale multi-omics GWAS preprint (2024)
A 2024 medRxiv preprint reports genome-/transcriptome-/proteome-wide association results in **2,170 IgAV cases and 5,928 controls**, identifying HLA and non-HLA loci and proposing myeloid Fcα receptor signaling as a convergent mechanism. Reported key associations include: **HLA-DRB1 OR=1.55 (P=1.1×10−25)**, **FCAR OR=1.51 (P=1.0×10−20)**, and **INPP5D OR=1.34 (P=2.2×10−9)**, with IL6R implicated by proteome-wide association. (liu2024genomewidestudiesdefine pages 2-6)
- Mechanistic interpretation (from the same work): FCAR risk alleles co-localize with cis-eQTL increasing FCAR expression and disrupt a PRDM1 motif; INPP5D encodes SHIP-1, a negative regulator of FcR signaling; IL6R risk haplotypes influence soluble IL6R levels. (liu2024genomewidestudiesdefine pages 8-11, liu2024genomewidestudiesdefine pages 11-13)
- Note: this is a **preprint** and should be treated as provisional until peer review. (liu2024genomewidestudiesdefine pages 2-6)

#### 4.2.2 HLA associations in a 2024 Croatian pediatric cohort
In a case–control cohort (130 IgAV children; 202 controls), significant susceptibility and phenotype associations included:
- Susceptibility: **HLA-A*03 21.4% vs 12.38% (p=0.0092)**; **HLA-B*37 2.9% vs 0.2% (p=0.0054)**; **HLA-DRB1*12 3.1% vs 0.7% (p=0.0216)**. (held2024hlapolymorphismsand pages 1-2)
- Nephritis phenotype: **HLA-DRB1*14:01P 17.5% vs 4.5% (p=0.0006)**. (held2024hlapolymorphismsand pages 1-2)
- Multivariate results also reported DRB1*10 association with GI symptoms and DRB1*14 association with nephritis. (held2024hlapolymorphismsand pages 6-8)

### 4.3 Molecular features and biomarkers (disease-associated)
- Complement-related urinary biomarkers: urinary C3/C4/C5/C5a are increased in pediatric IgAV nephritis and can discriminate nephritis (AUC 0.92). (wright2023urinarycomplementproteins pages 1-2)
- Multi-analyte biomarker exploration (2024): a pediatric cohort study investigated serum/urine Gd-IgA1, HMGB1, RAGE, and PCDH1 as potential biomarkers and reported clinical phenotype frequencies and treatment exposures (see Statistics table). (held2024insightintothe pages 2-4)

### 4.4 Epigenetics and chromosomal abnormalities
No epigenetic mechanisms or chromosomal abnormalities were extracted from the retrieved sources in this run.

---

## 5. Environmental information

### 5.1 Infectious agents
- Respiratory and GI infections commonly precede IgAV onset. (sestan2023diagnosticandmanagement pages 1-2, maisons2023newinsightsinto pages 1-3)

### 5.2 Lifestyle and toxins
No specific lifestyle/toxin associations were extracted from the retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding (causal chain)
A consolidated causal chain supported by the retrieved evidence:
1) **Trigger (often infection)** precedes onset in a large proportion of patients. (sestan2023diagnosticandmanagement pages 1-2, maisons2023newinsightsinto pages 1-3)
2) **Aberrantly glycosylated/hypoglycosylated IgA and immune complexes** form and deposit in tissues, with reviews referencing aberrant glycosylation and IgA1-dominant immune-complex deposition as key. (maisons2023newinsightsinto pages 1-3, castaneda2024igavasculitis(henoch–schönlein pages 1-2)
3) **Complement activation and neutrophil recruitment** occur; IgAV is described as involving “complement activation that recruits neutrophil polymorphs.” (parums2024areviewof pages 5-6)
4) **Endothelial/vascular inflammation and organ injury** manifests clinically as purpura, arthritis, GI symptoms, and nephritis. (sestan2023diagnosticandmanagement pages 1-2, hu2024immunoglobulinavasculitis pages 1-2)

### 6.2 Complement involvement and renal biomarkers
A prospective cohort study reports that urinary complement proteins are elevated in IgAV nephritis (IgAV-N) and can stratify nephritis.
- The abstract reports: “Children with immunoglobulin A vasculitis (IgAV… ) frequently encounter nephritis (IgAV-N) with 1–2% risk of kidney failure.” (wright2023urinarycomplementproteins pages 1-2)
- Quantitatively, in IgAV-N vs IgAV without nephritis, urinary complement levels were higher (e.g., C3 14.65 vs 2.26 μg/mmol) and a logistic regression model yielded **AUC 0.92 (p<0.001)** to discriminate nephritis. (wright2023urinarycomplementproteins pages 1-2)

### 6.3 Cell types and ontology suggestions
- **Neutrophils** and immune-complex mediated inflammation are emphasized. (parums2024areviewof pages 5-6, sestan2023diagnosticandmanagement pages 1-2)
- CL term suggestions: *neutrophil*; *monocyte*; *macrophage*; *endothelial cell*.

### 6.4 Pathway/GO term suggestions
- GO Biological Process suggestions: *complement activation*; *neutrophil chemotaxis*; *immune complex clearance*; *leukocyte-mediated immunity*; *inflammatory response*.

---

## 7. Anatomical structures affected

### 7.1 Primary organs/systems
Commonly involved organs: skin, joints, GI tract, kidneys. (maisons2023newinsightsinto pages 1-3, sestan2023diagnosticandmanagement pages 1-2)

### 7.2 Ontology suggestions
- UBERON suggestions: *skin*; *kidney*; *glomerulus*; *small intestine*; *synovial joint*.

---

## 8. Temporal development

### 8.1 Typical onset
- Pediatric predominance with onset around early childhood; median ~6 years and 90% <10 years in one review. (sestan2023diagnosticandmanagement pages 1-2)

### 8.2 Disease course patterns
- Pediatric IgAV often follows a self-limited course, but nephritis can be refractory and lead to CKD/ESKD in a minority. (hu2024immunoglobulinavasculitis pages 1-2)
- Adult IgAV is notable for relapse and persistent urinary abnormalities: relapse **15.8%**, persistent abnormal urinalysis **27.9%**, and ≥20% eGFR decline **15.5%** over median 24 months in a histologically proven cohort. (hocevar2023shorttermoutcomeof pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
- French nationwide rare-disease network cohort (BNDMR) reported **1,988 IgAV patients** (2010–2022). Annual incidence in 2021 was **0.06 per 100,000 adults** and **0.50 per 100,000 children**. (maisons2023newinsightsinto pages 1-3)
- Seasonality and geography: more frequent in winter/autumn and more common in the South vs North of France, adults OR **4.88 [4.17–5.74]**, children OR **1.51 [1.35–1.68]**. (maisons2023newinsightsinto pages 1-3)
- COVID-19 impact: pediatric incidence decreased during the pandemic period (defined in the paper), **OR 0.62 [0.47–0.81]**. (maisons2023newinsightsinto pages 1-3)

### 9.2 Genetic architecture
Evidence supports a polygenic/complex architecture with notable HLA associations; no Mendelian inheritance pattern is supported by the retrieved evidence. (sestan2023diagnosticandmanagement pages 1-2, held2024hlapolymorphismsand pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria and routine evaluation
- Classification criteria used for IgAV diagnosis include ACR 1990 and EULAR/PRINTO/PRES criteria, with EULAR/PRINTO/PRES noted as having better sensitivity/specificity than ACR in children/adults in a 2024 review. (hu2024immunoglobulinavasculitis pages 1-2)

### 10.2 Laboratory and monitoring in nephritis
A pediatric nephrology review states: “Basic investigations that should be done in every patient with IgAVN include blood pressure measurement, estimated glomerular filtration rate and urinalysis.” (sestan2023diagnosticandmanagement pages 1-2)

### 10.3 Biopsy
- Kidney biopsy: “Kidney biopsy is still the gold standard for the diagnosis of IgAVN since noninvasive confirmation of nephritis is still pending.” (sestan2023diagnosticandmanagement pages 1-2)
- Skin biopsy: a 2024 review states that biopsy with histopathology and IgA staining is “essential for the diagnosis,” and notes that renal biopsy can be done when there is clinical evidence of renal involvement. (parums2024areviewof pages 5-6)

### 10.4 Biomarkers (clinical readiness)
- A 2024 review states: “Currently, no specific diagnostic serological laboratory tests or biomarkers for IgA vasculitis exist.” (parums2024areviewof pages 5-6)
- Complement urine markers show promise for discrimination of nephritis (AUC 0.92), but this is not yet established as standard-of-care diagnostic testing. (wright2023urinarycomplementproteins pages 1-2)

---

## 11. Outcome / prognosis

### 11.1 Pediatric renal outcomes (EHR-based cohort)
A large PEDSnet observational cohort (diagnoses 2009–2020) reported outcomes among nephrology-followed children:
- “A total of **6802** children had a diagnosis of IgAV, of whom **1139 (16.7%)** were followed by nephrology for at least 2 visits over a median follow-up period of **1.7 years** [0.4,4.2].” (stone2023clinicalcourseand pages 1-2)
- “At the end of follow-up, **2.6** and **0.5%** developed CKD and kidney failure, respectively.” (stone2023clinicalcourseand pages 1-2)

### 11.2 Adult outcomes
In a histologically proven adult cohort (2010–2022) with median follow-up 24 months:
- Baseline renal involvement was **44.5%**. (hocevar2023shorttermoutcomeof pages 1-2)
- Relapse occurred in **15.8%**, persistent abnormal urinalysis in **27.9%**, and ≥20% eGFR decline in **15.5%**. (hocevar2023shorttermoutcomeof pages 1-2)
- Mortality: standardized mortality ratio (SMR) **1.4 [1.14–1.71]** vs general population. (hocevar2023shorttermoutcomeof pages 1-2)

### 11.3 Prognostic factors
Adult review and cohort literature indicate renal function, proteinuria, and hypertension are key predictors of renal prognosis (review-level statements); detailed quantitative prognostic modeling beyond the adult cohort hazard ratios for relapse were not comprehensively extracted in this run. (audemardverger2015igavasculitis(henochshönlein pages 1-1, hocevar2023shorttermoutcomeof pages 1-2)

---

## 12. Treatment

### 12.1 Current real-world management patterns (pediatrics; PEDSnet)
In PEDSnet nephrology-followed children:
- “Conservative management was the most predominant practice pattern, consisting of **observation in 57%** and **RAAS blockade in 6%**. **Steroid monotherapy** was used in **29%** and **other immunosuppression** regimens in **8%**.” (stone2023clinicalcourseand pages 1-2)

### 12.2 Guideline-oriented treatment stratification (pediatric IgAV nephritis)
A pediatric nephrology review summarizes SHARE-oriented first-line approaches by severity:
- Mild IgAVN: “oral glucocorticoids”
- Moderate IgAVN: “parenterally administrated glucocorticoids in pulsed doses”
- Severe IgAVN: “pulsed doses of glucocorticoids in combination with intravenous cyclophosphamide pulses” (sestan2023diagnosticandmanagement pages 1-2)

### 12.3 Adult and severe disease therapeutic landscape (2024 update)
A 2024 treatment-focused review states:
- “Glucocorticoids are the first-line therapy for IgAV, especially in adults with severe manifestations.” (castaneda2024igavasculitis(henoch–schönlein pages 1-2)
- For minor manifestations: “Colchicine, dapsone, and methotrexate can be useful.” (castaneda2024igavasculitis(henoch–schönlein pages 1-2)
- Steroid-sparing/other agents: calcineurin inhibitors and mycophenolate mofetil are cited as showing favorable results as glucocorticoid-sparing agents; rituximab is described as reducing relapse frequency and steroid burden and achieving long-term remission in some settings. (castaneda2024igavasculitis(henoch–schönlein pages 1-2)

### 12.4 Evidence gaps and expert opinion
- Adult-focused expert review (2015) emphasizes uncertainty and the need for prospective RCTs; it states that corticosteroids and immunosuppressants “have not been shown to improve long-term outcomes” for severe disease in adults (review-level conclusion). (audemardverger2015igavasculitis(henochshönlein pages 1-1)
- Pediatric nephrology review similarly notes that “noninvasive confirmation of nephritis is still pending” and highlights that “new therapeutic options are currently being tested” including those targeting Gd-IgA1/autoantibodies and complement pathways. (sestan2023diagnosticandmanagement pages 1-2)

### 12.5 MAXO (Medical Action Ontology) suggestions
- Glucocorticoid therapy; RAAS inhibition; cyclophosphamide therapy; rituximab therapy; kidney biopsy; urinalysis; blood pressure monitoring; plasma exchange (for severe life-threatening situations; review-level). (sestan2023diagnosticandmanagement pages 1-2, castaneda2024igavasculitis(henoch–schönlein pages 1-2)

---

## 13. Prevention
No primary prevention strategies (e.g., vaccination, lifestyle) were identified in the retrieved evidence. Secondary/tertiary prevention is implicit in recommendations for **monitoring kidney function** and early management of nephritis. (hu2024immunoglobulinavasculitis pages 1-2, sestan2023diagnosticandmanagement pages 1-2)

---

## 14. Other species / natural disease
No veterinary/natural disease evidence in other species was identified in the retrieved evidence.

---

## 15. Model organisms
No IgAV-specific animal models were extracted in the retrieved evidence. (Mechanistic modeling is often discussed for IgA nephropathy; however, IgAN model evidence was outside the scope of the retrieved IgAV-focused texts in this run.)

---

## Recent developments (2023–2024 prioritized)
1) **Nationwide epidemiology shifts during COVID-19**: pediatric incidence decreased during the pandemic period (OR 0.62) in the French BNDMR cohort. (Published online 12 Jul 2023; https://doi.org/10.1007/s00296-023-05387-2) (maisons2023newinsightsinto pages 1-3)
2) **Large EHR-based pediatric outcome estimation**: PEDSnet analysis quantified CKD (2.6%) and kidney failure (0.5%) after median 1.7 years follow-up among nephrology-followed children. (Published online 14 Jun 2023; https://doi.org/10.1007/s00467-023-06023-8) (stone2023clinicalcourseand pages 1-2)
3) **Urinary complement markers for nephritis stratification**: AUC 0.92 for discriminating nephritis using urinary complement analytes. (Published online 13 Oct 2022; 2023 issue; https://doi.org/10.1007/s00467-022-05747-3) (wright2023urinarycomplementproteins pages 1-2)
4) **Genetic advances**: HLA associations replicated in pediatric cohorts (2024 IJMS), and a 2024 multi-omics GWAS preprint proposes FcαR pathway loci (FCAR, INPP5D) and IL6R involvement. (https://doi.org/10.3390/ijms25020882; https://doi.org/10.1101/2024.10.10.24315041) (held2024hlapolymorphismsand pages 1-2, liu2024genomewidestudiesdefine pages 2-6)

---

## Current applications and real-world implementation
- **Routine nephritis evaluation** in pediatric practice includes BP measurement, eGFR, and urinalysis; kidney biopsy remains the gold standard for IgAV nephritis diagnosis when needed. (sestan2023diagnosticandmanagement pages 1-2)
- **Treatment in practice is heterogeneous and often conservative**, as observed in PEDSnet (observation/RAAS blockade common; steroids/immunosuppression used in more severe presentations). (stone2023clinicalcourseand pages 1-2)
- **Adult care often relies on glucocorticoids** and selected immunomodulators, with increasing interest in biologics (rituximab) and pathway-directed therapies (complement/APRIL/BAFF axis), though high-quality evidence remains limited for IgAV specifically. (castaneda2024igavasculitis(henoch–schönlein pages 1-2)

---

## Ongoing and recent clinical trials (real-world translational pipeline)
- **NCT05329090 (RIGA)**: “Evaluation of Glucocorticoids Plus Rituximab in Patients with Newly-Diagnosed or Relapsing IgA Vasculitis” (Phase 3; randomized, double-blind, placebo-controlled). Primary outcome includes remission defined as alive and prednisone 0 mg/day at 180 and 360 days; status ACTIVE_NOT_RECRUITING; enrollment 75; start 2022-03-11. (https://clinicaltrials.gov/study/NCT05329090) (NCT05329090 chunk 1)
- **NCT07052981**: “Clinical Study on the Efficacy and Safety of Telitacicept in the Treatment of Pediatric IgA Nephropathy or IgA Vasculitis Nephritis” (Phase 3; multicenter; non-randomized parallel groups; telitacicept + standard therapy vs standard therapy; pediatric 5–18 years; 24-week treatment; status NOT_YET_RECRUITING; enrollment 124). (https://clinicaltrials.gov/study/NCT07052981) (NCT07052981 chunk 1)

---

## Key quantitative evidence table
The following table compiles the most decision-relevant statistics extracted from recent cohorts and biomarker studies.

| Domain | Finding (with exact number) | Population/Study | Year | PMID (if available; otherwise DOI) | URL | Evidence citation id(s) |
|---|---|---|---|---|---|---|
| Epidemiology | Incidence of IgAV worldwide in children: **3 to 27 cases per 100,000 children** | Pediatric review by Sestan & Jelusic | 2023 | DOI: 10.2147/PHMT.S379862 | https://doi.org/10.2147/phmt.s379862 | (sestan2023diagnosticandmanagement pages 1-2) |
| Epidemiology | Prevalence of IgAV: **6.1 to 20.4 per 100,000 children** | Pediatric review by Sestan & Jelusic | 2023 | DOI: 10.2147/PHMT.S379862 | https://doi.org/10.2147/phmt.s379862 | (sestan2023diagnosticandmanagement pages 1-2) |
| Epidemiology | IgAV nephritis occurs in **20–60%** of children with IgAV | Pediatric review by Sestan & Jelusic | 2023 | DOI: 10.2147/PHMT.S379862 | https://doi.org/10.2147/phmt.s379862 | (sestan2023diagnosticandmanagement pages 1-2) |
| Epidemiology | Median age of onset around **6 years**; **90%** younger than 10 years; male:female **1.5:1** | Pediatric review by Sestan & Jelusic | 2023 | DOI: 10.2147/PHMT.S379862 | https://doi.org/10.2147/phmt.s379862 | (sestan2023diagnosticandmanagement pages 1-2) |
| Epidemiology | Total cohort **1,988** IgAV patients; sex ratio **1.57** in adults and **1.05** in children | French nationwide cohort (BNDMR) | 2023 | DOI: 10.1007/s00296-023-05387-2 | https://doi.org/10.1007/s00296-023-05387-2 | (maisons2023newinsightsinto pages 1-3) |
| Epidemiology | Annual incidence in 2021: **0.06 per 100,000 adults** and **0.50 per 100,000 children** | French nationwide cohort (BNDMR) | 2023 | DOI: 10.1007/s00296-023-05387-2 | https://doi.org/10.1007/s00296-023-05387-2 | (maisons2023newinsightsinto pages 1-3) |
| Epidemiology | Higher frequency in South vs North of France: adults **OR 4.88 [4.17–5.74]**; children **OR 1.51 [1.35–1.68]** | French nationwide cohort (BNDMR) | 2023 | DOI: 10.1007/s00296-023-05387-2 | https://doi.org/10.1007/s00296-023-05387-2 | (maisons2023newinsightsinto pages 1-3) |
| Epidemiology | Pediatric incidence decreased during COVID-19 period: **OR 0.62 [0.47–0.81]** | French nationwide cohort (BNDMR) | 2023 | DOI: 10.1007/s00296-023-05387-2 | https://doi.org/10.1007/s00296-023-05387-2 | (maisons2023newinsightsinto pages 1-3) |
| Renal outcomes | **6,802** children with IgAV; **1,139 (16.7%)** followed by nephrology for at least 2 visits; median follow-up **1.7 years [0.4, 4.2]** | PEDSnet pediatric cohort (Stone et al.) | 2023 | DOI: 10.1007/s00467-023-06023-8 | https://doi.org/10.1007/s00467-023-06023-8 | (stone2023clinicalcourseand pages 1-2) |
| Renal outcomes | Management patterns: observation **57%**, RAAS blockade **6%**, steroid monotherapy **29%**, other immunosuppression **8%** | PEDSnet pediatric cohort (Stone et al.) | 2023 | DOI: 10.1007/s00467-023-06023-8 | https://doi.org/10.1007/s00467-023-06023-8 | (stone2023clinicalcourseand pages 1-2) |
| Renal outcomes | End of follow-up: **2.6%** developed CKD and **0.5%** kidney failure | PEDSnet pediatric cohort (Stone et al.) | 2023 | DOI: 10.1007/s00467-023-06023-8 | https://doi.org/10.1007/s00467-023-06023-8 | (stone2023clinicalcourseand pages 1-2) |
| Biomarkers | Study cohort: **103** children total; **47** IgAV (**37** without nephritis, **10** with IgAV-N), **30** SLE, **26** healthy controls | Urinary complement study (Wright et al.) | 2023 | DOI: 10.1007/s00467-022-05747-3 | https://doi.org/10.1007/s00467-022-05747-3 | (wright2023urinarycomplementproteins pages 1-2) |
| Biomarkers | Urinary **C3** in IgAV-N vs IgAV without nephritis: **14.65 μg/mmol [2.26–20.21] vs 2.26 μg/mmol [0.15–3.14]**, **p=0.007** | Urinary complement study (Wright et al.) | 2023 | DOI: 10.1007/s00467-022-05747-3 | https://doi.org/10.1007/s00467-022-05747-3 | (wright2023urinarycomplementproteins pages 1-2) |
| Biomarkers | Urinary **C4** in IgAV-N vs IgAV without nephritis: **6.52 μg/mmol [1.30–9.72] vs 1.37 μg/mmol [0.38–2.43]**, **p=0.04** | Urinary complement study (Wright et al.) | 2023 | DOI: 10.1007/s00467-022-05747-3 | https://doi.org/10.1007/s00467-022-05747-3 | (wright2023urinarycomplementproteins pages 1-2) |
| Biomarkers | Urinary **C5** in IgAV-N vs IgAV without nephritis: **1.36 μg/mmol [0.65–2.85] vs 0.38 μg/mmol [0.03–0.72]**, **p=0.005** | Urinary complement study (Wright et al.) | 2023 | DOI: 10.1007/s00467-022-05747-3 | https://doi.org/10.1007/s00467-022-05747-3 | (wright2023urinarycomplementproteins pages 1-2) |
| Biomarkers | Urinary **C5a** in IgAV-N vs IgAV without nephritis: **101.9 ng/mmol [15.36–230.0] vs 18.33 ng/mmol [4.27–33.30]**, **p=0.01** | Urinary complement study (Wright et al.) | 2023 | DOI: 10.1007/s00467-022-05747-3 | https://doi.org/10.1007/s00467-022-05747-3 | (wright2023urinarycomplementproteins pages 1-2) |
| Biomarkers | Combined urinary complement model discriminated nephritis with **AUC 0.92**, **p<0.001** | Urinary complement study (Wright et al.) | 2023 | DOI: 10.1007/s00467-022-05747-3 | https://doi.org/10.1007/s00467-022-05747-3 | (wright2023urinarycomplementproteins pages 1-2) |
| Biomarkers | Pediatric IgAV cohort: **86** patients; **49 girls**, **37 boys**; median age **6.4 years (IQR 4.5–7.8)** | Biomarker cohort (Held et al.) | 2024 | DOI: 10.3390/ijms25084383 | https://doi.org/10.3390/ijms25084383 | (held2024insightintothe pages 2-4) |
| Biomarkers | Clinical features: skin changes **100%**; joint involvement **76/86 (88.4%)**; GI involvement **39/86 (45.3%)**; nephritis **26/86 (30.2%)**; scrotal involvement **6 boys (16.2%)** | Biomarker cohort (Held et al.) | 2024 | DOI: 10.3390/ijms25084383 | https://doi.org/10.3390/ijms25084383 | (held2024insightintothe pages 2-4) |
| Biomarkers | At least one recurrence in **21/86 (24.4%)**; median PVAS **4 (IQR 2–6)** | Biomarker cohort (Held et al.) | 2024 | DOI: 10.3390/ijms25084383 | https://doi.org/10.3390/ijms25084383 | (held2024insightintothe pages 2-4) |
| Biomarkers | Treatments: NSAIDs **75/86 (87.2%)**; glucocorticoids **36/86 (41.8%)**; ACE inhibitors **15/86 (17.4%)**; immunosuppressants **11/86 (12.8%)** | Biomarker cohort (Held et al.) | 2024 | DOI: 10.3390/ijms25084383 | https://doi.org/10.3390/ijms25084383 | (held2024insightintothe pages 2-4) |
| Biomarkers | Nephritis outcomes among nephritis subgroup: outcome A **18 (69.3%)**, outcome B **8 (30.7%)**, outcome C **0**, outcome D **0** | Biomarker cohort (Held et al.) | 2024 | DOI: 10.3390/ijms25084383 | https://doi.org/10.3390/ijms25084383 | (held2024insightintothe pages 2-4) |
| Adult outcomes | Adult cohort size **265**; median follow-up **24 months** | Adult single-center cohort (Hočevar et al.) | 2023 | DOI: 10.3389/fmed.2023.1210307 | https://doi.org/10.3389/fmed.2023.1210307 | (hocevar2023shorttermoutcomeof pages 1-2) |
| Adult outcomes | Baseline involvement: articular **38.9%**, gastrointestinal **29.8%**, renal **44.5%** | Adult single-center cohort (Hočevar et al.) | 2023 | DOI: 10.3389/fmed.2023.1210307 | https://doi.org/10.3389/fmed.2023.1210307 | (hocevar2023shorttermoutcomeof pages 1-2) |
| Adult outcomes | Initial treatment: systemic glucocorticoids **189 (71.3%)**; additional immunomodulator **32 (12.1%)** | Adult single-center cohort (Hočevar et al.) | 2023 | DOI: 10.3389/fmed.2023.1210307 | https://doi.org/10.3389/fmed.2023.1210307 | (hocevar2023shorttermoutcomeof pages 1-2) |
| Adult outcomes | Relapse in **42 (15.8%)**; younger age associated with relapse **HR 1.03 [1.01–1.05]**; no baseline glucocorticoids **HR 3.70 [2.0–6.67]** | Adult single-center cohort (Hočevar et al.) | 2023 | DOI: 10.3389/fmed.2023.1210307 | https://doi.org/10.3389/fmed.2023.1210307 | (hocevar2023shorttermoutcomeof pages 1-2) |
| Adult outcomes | Persistent abnormal urinalysis in **74 (27.9%)**; ≥20% eGFR decline in **41 (15.5%)** | Adult single-center cohort (Hočevar et al.) | 2023 | DOI: 10.3389/fmed.2023.1210307 | https://doi.org/10.3389/fmed.2023.1210307 | (hocevar2023shorttermoutcomeof pages 1-2) |
| Adult outcomes | Overall standardized mortality ratio **1.4 [95% CI 1.14–1.71]** vs general population | Adult single-center cohort (Hočevar et al.) | 2023 | DOI: 10.3389/fmed.2023.1210307 | https://doi.org/10.3389/fmed.2023.1210307 | (hocevar2023shorttermoutcomeof pages 1-2) |


*Table: This table compiles the main quantitative epidemiology, renal outcome, biomarker, and adult outcome statistics for IgA vasculitis from the gathered evidence. It is useful as a compact evidence map for rapid reference when drafting the full report.*

---

## Visual evidence
A table summarizing kidney outcomes stratified by management patterns (observation vs RAAS blockade vs steroids vs other immunosuppression) was retrieved from the Stone et al. PEDSnet paper (Table 5). (stone2023clinicalcourseand media 45fd3a4e)

---

## Notes on evidence quality and limitations
- Several key advances are based on **observational cohorts** (PEDSnet; BNDMR; single-center adult cohorts) and therefore are subject to confounding by indication and measurement limitations. (stone2023clinicalcourseand pages 1-2, maisons2023newinsightsinto pages 1-3, hocevar2023shorttermoutcomeof pages 1-2)
- Genetic findings include a major **2024 medRxiv preprint** with large sample size and compelling mechanistic hypotheses, but it is **not yet peer-reviewed** and should be curated with that caveat. (liu2024genomewidestudiesdefine pages 2-6)
- Despite promising biomarkers (e.g., urinary complement proteins), reviews still emphasize a lack of validated diagnostic serologic biomarkers in routine clinical practice. (parums2024areviewof pages 5-6, wright2023urinarycomplementproteins pages 1-2)


References

1. (sestan2023diagnosticandmanagement pages 1-2): Mario Sestan and Marija Jelusic. Diagnostic and management strategies of iga vasculitis nephritis/henoch-schönlein purpura nephritis in pediatric patients: current perspectives. Pediatric Health, Medicine and Therapeutics, 14:89-98, Mar 2023. URL: https://doi.org/10.2147/phmt.s379862, doi:10.2147/phmt.s379862. This article has 57 citations.

2. (hu2024immunoglobulinavasculitis pages 1-2): Ya‐Chiao Hu, Yao‐Hsu Yang, and Bor‐Luen Chiang. Immunoglobulin a vasculitis: the clinical features and pathophysiology. The Kaohsiung Journal of Medical Sciences, 40:612-620, Jun 2024. URL: https://doi.org/10.1002/kjm2.12852, doi:10.1002/kjm2.12852. This article has 12 citations.

3. (castaneda2024igavasculitis(henoch–schönlein pages 1-2): Santos Castañeda, Patricia Quiroga-Colina, Paz Floranes, Miren Uriarte-Ecenarro, Cristina Valero-Martínez, Esther F. Vicente-Rabaneda, and Miguel A. González-Gay. Iga vasculitis (henoch–schönlein purpura): an update on treatment. Journal of Clinical Medicine, 13:6621, Nov 2024. URL: https://doi.org/10.3390/jcm13216621, doi:10.3390/jcm13216621. This article has 45 citations.

4. (parums2024areviewof pages 5-6): Dinah V. Parums. A review of iga vasculitis (henoch-schönlein purpura) past, present, and future. Medical Science Monitor : International Medical Journal of Experimental and Clinical Research, 30:e943912-1-e943912-7, Jan 2024. URL: https://doi.org/10.12659/msm.943912, doi:10.12659/msm.943912. This article has 62 citations.

5. (stone2023clinicalcourseand pages 1-2): Hillarey K. Stone, Mark Mitsnefes, Kimberley Dickinson, Evanette K. Burrows, Hanieh Razzaghi, Ingrid Y. Luna, Caroline A. Gluck, Bradley P. Dixon, Vikas R. Dharnidharka, William E. Smoyer, Michael J. Somers, Joseph T. Flynn, Susan L. Furth, Charles Bailey, Christopher B. Forrest, Michelle Denburg, and Edward Nehus. Clinical course and management of children with iga vasculitis with nephritis. Pediatric Nephrology (Berlin, Germany), 38:3721-3733, Jun 2023. URL: https://doi.org/10.1007/s00467-023-06023-8, doi:10.1007/s00467-023-06023-8. This article has 17 citations.

6. (maisons2023newinsightsinto pages 1-3): Valentin Maisons, Yanis Ramdani, Antoine Hankard, Claude Messiaen, Anne-Sophie Jannot, Bénédicte Sautenet, Jean-Michel Halimi, François Maillot, Évangeline Pillebout, and Alexandra Audemard-Verger. New insights into epidemiological data and impact of the covid-19 pandemic on iga vasculitis in children and adults: a french nationwide cohort. Rheumatology International, 43:1791-1798, Jul 2023. URL: https://doi.org/10.1007/s00296-023-05387-2, doi:10.1007/s00296-023-05387-2. This article has 15 citations and is from a peer-reviewed journal.

7. (hocevar2023shorttermoutcomeof pages 1-2): Alojzija Hočevar, Jaka Ostrovršnik, Vesna Jurčić, Matija Tomšič, and Žiga Rotar. Short-term outcome of patients with adult iga vasculitis: a single-center experience. Frontiers in Medicine, Jul 2023. URL: https://doi.org/10.3389/fmed.2023.1210307, doi:10.3389/fmed.2023.1210307. This article has 10 citations.

8. (wright2023urinarycomplementproteins pages 1-2): Rachael D. Wright, Julien Marro, Sarah J. Northey, Rachel Corkhill, Michael W. Beresford, and Louise Oni. Urinary complement proteins are increased in children with iga vasculitis (henoch-schönlein purpura) nephritis. Pediatric Nephrology (Berlin, Germany), 38:1491-1498, Oct 2023. URL: https://doi.org/10.1007/s00467-022-05747-3, doi:10.1007/s00467-022-05747-3. This article has 11 citations.

9. (held2024hlapolymorphismsand pages 1-2): Martina Held, Katarina Stingl Jankovic, Mario Sestan, Matej Sapina, Nastasia Kifer, Sasa Srsen, Marijan Frkovic, Alenka Gagro, Zorana Grubic, and Marija Jelusic. Hla polymorphisms and clinical manifestations in iga vasculitis. International Journal of Molecular Sciences, 25:882, Jan 2024. URL: https://doi.org/10.3390/ijms25020882, doi:10.3390/ijms25020882. This article has 11 citations.

10. (liu2024genomewidestudiesdefine pages 6-8): Lili Liu, Li Zhu, Sara Monteiro-Martins, Aaron Griffin, Lukas J Vlahos, Masashi Fujita, Cecilia Berrouet, Francesca Zanoni, Maddalena Marasa, Jun Y Zhang, Xu-Jie Zhou, Yasar Caliskan, Oleh Akchurin, Samhar Al-Akash, Augustina Jankauskiene, Monica Bodria, Aftab Chishti, Ciro Esposito, Vittoria Esposito, Donna Claes, Vladimir Tesar, Thomas K Davis, Dmitry Samsonov, Dorota Kaminska, Tomasz Hryszko, Gianluigi Zaza, Joseph T Flynn, Franca Iorember, Francesca Lugani, Dana Rizk, Bruce A Julian, Guillermo Hidalgo, Mahmoud Kallash, Luigi Biancone, Antonio Amoroso, Luisa Bono, Laila-Yasmin Mani, Fangming Lin, Bruno Vogt, Raji Sreedharan, Patricia Weng, Daniel Ranch, Nianzhou Xiao, Alejandro Quiroga, Raed Bou Matar, Michelle N Rheault, Scott Wenderfer, Dave Selewski, Sigrid Lundberg, Cynthia Silva, Sherene Mason, John D Mahan, Tetyana L Vasylyeva, Krzysztof Mucha, Bartosz Foroncewicz, Leszek Pączek, Michał Florczak, Małgorzata Olszewska, Agnieszka Gradzińska, Maria Szczepańska, Edyta Machura, Andrzej Badeński, Helena Krakowczyk, Przemysław Sikora, Norbert Kwella, Monika Miklaszewska, Dorota Drożdż, Marcin Zaniew, Krzysztof Pawlaczyk, Katarzyna SiniewiczLuzeńczyk, Andrew S Bomback, Gerald B Appel, Claudia Izzi, Francesco Scolari, Anna Materna-Kiryluk, Malgorzata Mizerska-Wasiak, Laureline Berthelot, Evangeline Pillebout, Renato C Monteiro, Jan Novak, Todd Jason Green, William E Smoyer, M Colleen Hastings, Robert J Wyatt, Raoul Nelson, Javier Martin, Miguel A González-Gay, Philip L De Jager, Anna Köttgen, Andrea Califano, Ali G Gharavi, Hong Zhang, and Krzysztof Kiryluk. Genome-wide studies define new genetic mechanisms of iga vasculitis. medRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.10.24315041, doi:10.1101/2024.10.10.24315041. This article has 2 citations.

11. (held2024insightintothe pages 2-4): Martina Held, Ana Kozmar, Mario Sestan, Daniel Turudic, Nastasia Kifer, Sasa Srsen, Alenka Gagro, Marijan Frkovic, and Marija Jelusic. Insight into the interplay of gd-iga1, hmgb1, rage and pcdh1 in iga vasculitis (igav). International Journal of Molecular Sciences, 25:4383, Apr 2024. URL: https://doi.org/10.3390/ijms25084383, doi:10.3390/ijms25084383. This article has 9 citations.

12. (marro2023acaseseries pages 1-2): Julien Marro, Chloe Williams, Clare E. Pain, and Louise Oni. A case series on recurrent and persisting iga vasculitis (henoch schonlein purpura) in children. Pediatric Rheumatology Online Journal, Aug 2023. URL: https://doi.org/10.1186/s12969-023-00872-1, doi:10.1186/s12969-023-00872-1. This article has 23 citations.

13. (liu2024genomewidestudiesdefine pages 2-6): Lili Liu, Li Zhu, Sara Monteiro-Martins, Aaron Griffin, Lukas J Vlahos, Masashi Fujita, Cecilia Berrouet, Francesca Zanoni, Maddalena Marasa, Jun Y Zhang, Xu-Jie Zhou, Yasar Caliskan, Oleh Akchurin, Samhar Al-Akash, Augustina Jankauskiene, Monica Bodria, Aftab Chishti, Ciro Esposito, Vittoria Esposito, Donna Claes, Vladimir Tesar, Thomas K Davis, Dmitry Samsonov, Dorota Kaminska, Tomasz Hryszko, Gianluigi Zaza, Joseph T Flynn, Franca Iorember, Francesca Lugani, Dana Rizk, Bruce A Julian, Guillermo Hidalgo, Mahmoud Kallash, Luigi Biancone, Antonio Amoroso, Luisa Bono, Laila-Yasmin Mani, Fangming Lin, Bruno Vogt, Raji Sreedharan, Patricia Weng, Daniel Ranch, Nianzhou Xiao, Alejandro Quiroga, Raed Bou Matar, Michelle N Rheault, Scott Wenderfer, Dave Selewski, Sigrid Lundberg, Cynthia Silva, Sherene Mason, John D Mahan, Tetyana L Vasylyeva, Krzysztof Mucha, Bartosz Foroncewicz, Leszek Pączek, Michał Florczak, Małgorzata Olszewska, Agnieszka Gradzińska, Maria Szczepańska, Edyta Machura, Andrzej Badeński, Helena Krakowczyk, Przemysław Sikora, Norbert Kwella, Monika Miklaszewska, Dorota Drożdż, Marcin Zaniew, Krzysztof Pawlaczyk, Katarzyna SiniewiczLuzeńczyk, Andrew S Bomback, Gerald B Appel, Claudia Izzi, Francesco Scolari, Anna Materna-Kiryluk, Malgorzata Mizerska-Wasiak, Laureline Berthelot, Evangeline Pillebout, Renato C Monteiro, Jan Novak, Todd Jason Green, William E Smoyer, M Colleen Hastings, Robert J Wyatt, Raoul Nelson, Javier Martin, Miguel A González-Gay, Philip L De Jager, Anna Köttgen, Andrea Califano, Ali G Gharavi, Hong Zhang, and Krzysztof Kiryluk. Genome-wide studies define new genetic mechanisms of iga vasculitis. medRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.10.24315041, doi:10.1101/2024.10.10.24315041. This article has 2 citations.

14. (liu2024genomewidestudiesdefine pages 8-11): Lili Liu, Li Zhu, Sara Monteiro-Martins, Aaron Griffin, Lukas J Vlahos, Masashi Fujita, Cecilia Berrouet, Francesca Zanoni, Maddalena Marasa, Jun Y Zhang, Xu-Jie Zhou, Yasar Caliskan, Oleh Akchurin, Samhar Al-Akash, Augustina Jankauskiene, Monica Bodria, Aftab Chishti, Ciro Esposito, Vittoria Esposito, Donna Claes, Vladimir Tesar, Thomas K Davis, Dmitry Samsonov, Dorota Kaminska, Tomasz Hryszko, Gianluigi Zaza, Joseph T Flynn, Franca Iorember, Francesca Lugani, Dana Rizk, Bruce A Julian, Guillermo Hidalgo, Mahmoud Kallash, Luigi Biancone, Antonio Amoroso, Luisa Bono, Laila-Yasmin Mani, Fangming Lin, Bruno Vogt, Raji Sreedharan, Patricia Weng, Daniel Ranch, Nianzhou Xiao, Alejandro Quiroga, Raed Bou Matar, Michelle N Rheault, Scott Wenderfer, Dave Selewski, Sigrid Lundberg, Cynthia Silva, Sherene Mason, John D Mahan, Tetyana L Vasylyeva, Krzysztof Mucha, Bartosz Foroncewicz, Leszek Pączek, Michał Florczak, Małgorzata Olszewska, Agnieszka Gradzińska, Maria Szczepańska, Edyta Machura, Andrzej Badeński, Helena Krakowczyk, Przemysław Sikora, Norbert Kwella, Monika Miklaszewska, Dorota Drożdż, Marcin Zaniew, Krzysztof Pawlaczyk, Katarzyna SiniewiczLuzeńczyk, Andrew S Bomback, Gerald B Appel, Claudia Izzi, Francesco Scolari, Anna Materna-Kiryluk, Malgorzata Mizerska-Wasiak, Laureline Berthelot, Evangeline Pillebout, Renato C Monteiro, Jan Novak, Todd Jason Green, William E Smoyer, M Colleen Hastings, Robert J Wyatt, Raoul Nelson, Javier Martin, Miguel A González-Gay, Philip L De Jager, Anna Köttgen, Andrea Califano, Ali G Gharavi, Hong Zhang, and Krzysztof Kiryluk. Genome-wide studies define new genetic mechanisms of iga vasculitis. medRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.10.24315041, doi:10.1101/2024.10.10.24315041. This article has 2 citations.

15. (liu2024genomewidestudiesdefine pages 11-13): Lili Liu, Li Zhu, Sara Monteiro-Martins, Aaron Griffin, Lukas J Vlahos, Masashi Fujita, Cecilia Berrouet, Francesca Zanoni, Maddalena Marasa, Jun Y Zhang, Xu-Jie Zhou, Yasar Caliskan, Oleh Akchurin, Samhar Al-Akash, Augustina Jankauskiene, Monica Bodria, Aftab Chishti, Ciro Esposito, Vittoria Esposito, Donna Claes, Vladimir Tesar, Thomas K Davis, Dmitry Samsonov, Dorota Kaminska, Tomasz Hryszko, Gianluigi Zaza, Joseph T Flynn, Franca Iorember, Francesca Lugani, Dana Rizk, Bruce A Julian, Guillermo Hidalgo, Mahmoud Kallash, Luigi Biancone, Antonio Amoroso, Luisa Bono, Laila-Yasmin Mani, Fangming Lin, Bruno Vogt, Raji Sreedharan, Patricia Weng, Daniel Ranch, Nianzhou Xiao, Alejandro Quiroga, Raed Bou Matar, Michelle N Rheault, Scott Wenderfer, Dave Selewski, Sigrid Lundberg, Cynthia Silva, Sherene Mason, John D Mahan, Tetyana L Vasylyeva, Krzysztof Mucha, Bartosz Foroncewicz, Leszek Pączek, Michał Florczak, Małgorzata Olszewska, Agnieszka Gradzińska, Maria Szczepańska, Edyta Machura, Andrzej Badeński, Helena Krakowczyk, Przemysław Sikora, Norbert Kwella, Monika Miklaszewska, Dorota Drożdż, Marcin Zaniew, Krzysztof Pawlaczyk, Katarzyna SiniewiczLuzeńczyk, Andrew S Bomback, Gerald B Appel, Claudia Izzi, Francesco Scolari, Anna Materna-Kiryluk, Malgorzata Mizerska-Wasiak, Laureline Berthelot, Evangeline Pillebout, Renato C Monteiro, Jan Novak, Todd Jason Green, William E Smoyer, M Colleen Hastings, Robert J Wyatt, Raoul Nelson, Javier Martin, Miguel A González-Gay, Philip L De Jager, Anna Köttgen, Andrea Califano, Ali G Gharavi, Hong Zhang, and Krzysztof Kiryluk. Genome-wide studies define new genetic mechanisms of iga vasculitis. medRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.10.24315041, doi:10.1101/2024.10.10.24315041. This article has 2 citations.

16. (held2024hlapolymorphismsand pages 6-8): Martina Held, Katarina Stingl Jankovic, Mario Sestan, Matej Sapina, Nastasia Kifer, Sasa Srsen, Marijan Frkovic, Alenka Gagro, Zorana Grubic, and Marija Jelusic. Hla polymorphisms and clinical manifestations in iga vasculitis. International Journal of Molecular Sciences, 25:882, Jan 2024. URL: https://doi.org/10.3390/ijms25020882, doi:10.3390/ijms25020882. This article has 11 citations.

17. (audemardverger2015igavasculitis(henochshönlein pages 1-1): Alexandra Audemard-Verger, Evangeline Pillebout, Loïc Guillevin, Eric Thervet, and Benjamin Terrier. Iga vasculitis (henoch-shönlein purpura) in adults: diagnostic and therapeutic aspects. Autoimmunity reviews, 14 7:579-85, Jul 2015. URL: https://doi.org/10.1016/j.autrev.2015.02.003, doi:10.1016/j.autrev.2015.02.003. This article has 358 citations and is from a peer-reviewed journal.

18. (NCT05329090 chunk 1):  Evaluation of Glucocorticoids Plus Rituximab in Patients with Newly-Diagnosed or Relapsing IgA Vasculitis. Hopital Foch. 2022. ClinicalTrials.gov Identifier: NCT05329090

19. (NCT07052981 chunk 1): Guixia Ding. Clinical Study on the Efficacy and Safety of Telitacicept in the Treatment of Pediatric IgA Nephropathy or IgA Vasculitis Nephritis. Guixia Ding. 2025. ClinicalTrials.gov Identifier: NCT07052981

20. (stone2023clinicalcourseand media 45fd3a4e): Hillarey K. Stone, Mark Mitsnefes, Kimberley Dickinson, Evanette K. Burrows, Hanieh Razzaghi, Ingrid Y. Luna, Caroline A. Gluck, Bradley P. Dixon, Vikas R. Dharnidharka, William E. Smoyer, Michael J. Somers, Joseph T. Flynn, Susan L. Furth, Charles Bailey, Christopher B. Forrest, Michelle Denburg, and Edward Nehus. Clinical course and management of children with iga vasculitis with nephritis. Pediatric Nephrology (Berlin, Germany), 38:3721-3733, Jun 2023. URL: https://doi.org/10.1007/s00467-023-06023-8, doi:10.1007/s00467-023-06023-8. This article has 17 citations.