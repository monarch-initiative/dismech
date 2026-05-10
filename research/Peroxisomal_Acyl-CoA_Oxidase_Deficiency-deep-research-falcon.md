---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T16:18:20.008874'
end_time: '2026-05-10T16:27:36.161409'
duration_seconds: 556.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisomal Acyl-CoA Oxidase Deficiency
  mondo_id: ''
  category: Metabolic Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisomal Acyl-CoA Oxidase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Peroxisomal Acyl-CoA Oxidase Deficiency** covering all of the
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
- **Disease Name:** Peroxisomal Acyl-CoA Oxidase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Peroxisomal Acyl-CoA Oxidase Deficiency** covering all of the
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


## Comprehensive Research Report: Peroxisomal Acyl‑CoA Oxidase Deficiency (ACOX1 deficiency)

### Executive summary
Peroxisomal acyl‑CoA oxidase deficiency is a rare autosomal recessive peroxisomal fatty‑acid β‑oxidation disorder caused by biallelic pathogenic variants in **ACOX1**, leading to impaired oxidation of straight‑chain very‑long‑chain fatty acids (VLCFAs) and typically elevated plasma C26:0 (cerotic acid). It presents most often in infancy with hypotonia, seizures, severe developmental delay and progressive leukodystrophy with regression, often fatal in childhood, although later-onset presentations are described. Recent (2023–2024) research has emphasized innate-immune and microglial contributions (disease-associated microglia signatures, lysosome/autophagy programs) and has highlighted newborn-screening-relevant lipid biomarkers for early detection of peroxisomal disorders. (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2, wanders2021fattyacidoxidation pages 69-70, mohan2023evaluatingthestrength pages 3-4, raas2023peroxisomaldefectsin pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
**Definition (current understanding):** Peroxisomal acyl‑CoA oxidase deficiency (often called **pseudoneonatal adrenoleukodystrophy**, “pseudo‑NALD”, or “pseudo‑neonatal ALD”) is an inborn error of metabolism due to **deficiency of straight‑chain acyl‑CoA oxidase (ACOX1)**, the first enzyme in peroxisomal β‑oxidation of straight‑chain VLCFAs. The core biochemical hallmark is impaired peroxisomal β‑oxidation with **accumulation of VLCFAs**, particularly C26:0 in plasma. (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2, rosewich12006pitfallinmetabolic pages 1-2)

A mechanistically explicit statement from a primary functional paper: pseudoneonatal adrenoleukodystrophy is characterized by ACOX1 deficiency leading to “**accumulation of very‑long‑chain fatty acids (VLCFA) and inflammatory demyelination**.” (hajj2012theinflammatoryresponse pages 1-1)

### 1.2 Key identifiers (as retrieved in the available corpus)
- **OMIM disease:** **#264470** (pseudoneonatal adrenoleukodystrophy / ACOX1 deficiency) (carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2, hajj2012theinflammatoryresponse pages 1-1)
- **Causal gene:** **ACOX1** (straight‑chain acyl‑CoA oxidase 1) (ferdinandusse2007clinicalbiochemicaland pages 1-2)
- **OMIM gene:** **ACOX1 *609751** (rosewich12006pitfallinmetabolic pages 1-2, ferdinandusse2007clinicalbiochemicaland pages 1-2)

**Not retrieved in this tool run:** MONDO ID, Orphanet ID, ICD‑10/ICD‑11 codes, MeSH term for the specific disease entity. These should be added from external curated resources (e.g., OMIM/Orphanet/MONDO browsers) but were not present in the retrieved full-text corpus.

### 1.3 Synonyms / alternative names
- **Pseudoneonatal adrenoleukodystrophy (P‑NALD)** (ferdinandusse2007clinicalbiochemicaland pages 1-2, hajj2012theinflammatoryresponse pages 1-1)
- **Pseudo‑neonatal ALD** (wang2014effectsofhematopoietic pages 1-2, rosewich12006pitfallinmetabolic pages 1-2)

### 1.4 Evidence source type
The compiled information is primarily derived from:
- **Aggregated disease-level resources via primary cohorts/reviews** (e.g., Human Mutation 2007 cohort; later synthesis) (ferdinandusse2007clinicalbiochemicaland pages 1-2, wanders2021fattyacidoxidation pages 69-70)
- **Individual patient case reports** (e.g., Neuropediatrics 2006; Am J Med Genet A 2008) (rosewich12006pitfallinmetabolic pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2)
- **Experimental disease models (in vitro microglia/fibroblasts)** informing mechanism (hajj2012theinflammatoryresponse pages 1-1, raas2023peroxisomaldefectsin pages 1-2)

**Artifact: identifiers & nomenclature**

| Identifier type | Value | Notes | Source |
|---|---|---|---|
| Disease name | Peroxisomal acyl-CoA oxidase deficiency | Rare single-enzyme peroxisomal disorder caused by deficiency of straight-chain acyl-CoA oxidase/ACOX1; core biochemical defect is impaired peroxisomal β-oxidation with VLCFA accumulation, especially C26:0; autosomal recessive (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2) | Ferdinandusse et al., 2007, *Human Mutation*, https://doi.org/10.1002/humu.20535; Carrozzo et al., 2008, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.32298 |
| OMIM disease ID | OMIM #264470 | Disease entry for ACOX1 deficiency; also cited for pseudoneonatal adrenoleukodystrophy/P-NALD (carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2, hajj2012theinflammatoryresponse pages 1-1) | Carrozzo et al., 2008, https://doi.org/10.1002/ajmg.a.32298; Hajj et al., 2012, https://doi.org/10.1210/en.2012-1137 |
| Gene symbol | ACOX1 | Encodes peroxisomal acyl-CoA oxidase 1 / straight-chain acyl-CoA oxidase, the first enzyme in peroxisomal VLCFA β-oxidation (ferdinandusse2007clinicalbiochemicaland pages 1-2, wanders2021fattyacidoxidation pages 69-70) | Ferdinandusse et al., 2007, https://doi.org/10.1002/humu.20535; Wanders et al., 2021, https://doi.org/10.1007/978-3-030-60204-8_5 |
| Gene MIM | MIM *609751 | Gene identifier for ACOX1; molecular testing of ACOX1 confirms diagnosis (rosewich12006pitfallinmetabolic pages 1-2, ferdinandusse2007clinicalbiochemicaland pages 1-2) | Rosewich et al., 2006, https://doi.org/10.1055/s-2006-923943; Ferdinandusse et al., 2007, https://doi.org/10.1002/humu.20535 |
| Historical synonym | Pseudoneonatal adrenoleukodystrophy | Historical/alternative name widely used in literature for ACOX1 deficiency (ferdinandusse2007clinicalbiochemicaland pages 1-2, hajj2012theinflammatoryresponse pages 1-2) | Ferdinandusse et al., 2007, https://doi.org/10.1002/humu.20535; Hajj et al., 2012, https://doi.org/10.1210/en.2012-1137 |
| Alternate synonym | P-NALD / pseudo-neonatal ALD | Abbreviated synonym used in case reports and reviews; reflects phenotypic overlap with neonatal ALD but due to isolated ACOX1 deficiency (wang2014effectsofhematopoietic pages 1-2, rosewich12006pitfallinmetabolic pages 1-2) | Wang et al., 2014, https://doi.org/10.1007/s10545-014-9698-3; Rosewich et al., 2006, https://doi.org/10.1055/s-2006-923943 |
| Disease class | Peroxisomal β-oxidation defect | Specifically a defect of straight-chain very-long-chain fatty acid β-oxidation in peroxisomes (wang2014effectsofhematopoietic pages 1-2, rosewich12006pitfallinmetabolic pages 1-2) | Wang et al., 2014, https://doi.org/10.1007/s10545-014-9698-3; Rosewich et al., 2006, https://doi.org/10.1055/s-2006-923943 |
| Hallmark biochemical marker | Elevated plasma VLCFAs, especially C26:0; increased C26:0/C22:0 ratio | Plasma VLCFA abnormality is the key biochemical signature; phytanic/pristanic acids and plasmalogens may be normal in some patients (rosewich12006pitfallinmetabolic pages 3-4, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2) | Rosewich et al., 2006, https://doi.org/10.1055/s-2006-923943; Carrozzo et al., 2008, https://doi.org/10.1002/ajmg.a.32298 |
| Inheritance | Autosomal recessive | Confirmed in clinical series and case reports; affected individuals typically carry biallelic pathogenic ACOX1 variants (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2) | Ferdinandusse et al., 2007, https://doi.org/10.1002/humu.20535; Carrozzo et al., 2008, https://doi.org/10.1002/ajmg.a.32298 |


*Table: This table summarizes the principal names, identifiers, and defining biochemical/genetic features of peroxisomal acyl-CoA oxidase deficiency. It is useful for harmonizing disease nomenclature and core database fields for knowledge-base curation.*

---

## 2. Etiology

### 2.1 Disease causal factors
- **Primary cause:** biallelic pathogenic variants in **ACOX1** causing loss of ACOX1 enzyme activity and impaired peroxisomal straight‑chain VLCFA β‑oxidation. (ferdinandusse2007clinicalbiochemicaland pages 1-2, rosewich12006pitfallinmetabolic pages 1-2)
- **Mechanistic consequence:** VLCFA accumulation and downstream inflammatory demyelination (hajj2012theinflammatoryresponse pages 1-1)

### 2.2 Risk factors
- **Genetic:** autosomal recessive inheritance; affected individuals typically have **biallelic** pathogenic ACOX1 variants (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2). In a fatal case with misleading screening results, parental heterozygosity was shown for an ACOX1 splice variant, consistent with recessive inheritance. (rosewich12006pitfallinmetabolic pages 3-4)
- **Environmental:** no specific environmental risk factors or triggers are established in the retrieved ACOX1-deficiency literature.

### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the retrieved corpus for ACOX1 deficiency.

### 2.4 Gene–environment interactions
No ACOX1-deficiency–specific gene–environment interactions were identified in the retrieved corpus.

---

## 3. Phenotypes

### 3.1 Phenotypic spectrum (signs/symptoms/lab)
A 2021 synthesis of reported cases describes classic features including **hypotonia**, **seizures**, **visual system failure**, **impaired hearing**, **facial dysmorphism**, **hepatomegaly**, and **failure to thrive**, along with **cerebral and/or cerebellar white matter abnormalities** on neuroimaging. (wanders2021fattyacidoxidation pages 69-70)

A primary mechanistic/clinical description in Endocrinology summarizes P‑NALD as “**characterized by craniofacial dysmorphia, generalized hypotonia, hepatomegaly, infantile seizures, loss of motor achievements, and white matter demyelination**.” (hajj2012theinflammatoryresponse pages 1-2)

### 3.2 Age of onset, severity, progression, and frequency
- **Typical onset:** neonatal/infantile hypotonia and infantile seizures are repeatedly reported. (ferdinandusse2007clinicalbiochemicaland pages 1-2, rosewich12006pitfallinmetabolic pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2)
- **Progression/regression:** a review summarizing a 26‑patient series states most patients acquire limited skills but **83%** showed **loss of motor achievements** with **mean age of regression 28 months**. (wanders2021fattyacidoxidation pages 69-70)
- **Mortality/prognosis:** the same synthesis reports a **mean age of death of 5 years** (range 4–10) in that cohort, while acknowledging rare adult-onset cases. (wanders2021fattyacidoxidation pages 69-70)

### 3.3 Quality of life impact
Formal QoL instruments (EQ‑5D/SF‑36/PROMIS) were not identified in the retrieved corpus. However, the reported course—developmental regression with loss of vision/hearing and motor function—implies profound impairment of daily functioning and caregiver burden. (wang2014effectsofhematopoietic pages 1-2, wanders2021fattyacidoxidation pages 69-70)

### 3.4 Suggested HPO mapping

| Phenotype (plain language) | Suggested HPO term(s) and ID(s) | Typical onset/course | Frequency/statistics (if stated) | Evidence/source with year+URL |
|---|---|---|---|---|
| Neonatal/infantile hypotonia | Hypotonia (HP:0001252); Neonatal hypotonia (HP:0001290) | Usually neonatal or early infancy; often progressive as part of neurodegenerative course | Reported repeatedly in severe early-onset cases; no pooled % given in available evidence | Ferdinandusse et al. 2007, https://doi.org/10.1002/humu.20535; Carrozzo et al. 2008, https://doi.org/10.1002/ajmg.a.32298; Wang et al. 2014, https://doi.org/10.1007/s10545-014-9698-3 (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2, wang2014effectsofhematopoietic pages 1-2) |
| Infantile seizures | Seizure (HP:0001250); Infantile spasms/epileptic seizures if specified clinically (HP:0012469 / HP:0002123, suggestive) | Infancy; often early and associated with severe neurologic disease | Common in case reports/series; no pooled % stated in available excerpts | Ferdinandusse et al. 2007, https://doi.org/10.1002/humu.20535; Carrozzo et al. 2008, https://doi.org/10.1002/ajmg.a.32298; Rosewich et al. 2006, https://doi.org/10.1055/s-2006-923943 (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2, rosewich12006pitfallinmetabolic pages 1-2) |
| Psychomotor retardation / global developmental delay | Global developmental delay (HP:0001263); Psychomotor retardation (HP:0001263, common mapping); Intellectual disability, profound/severe if later confirmed (HP:0010864/HP:0010864 family, suggestive) | Infancy to early childhood; severe delay with limited skill acquisition | In a 26-patient series, all had psychomotor retardation | Wanders et al. 2021 review summarizing clinical series, https://doi.org/10.1007/978-3-030-60204-8_5; Ferdinandusse et al. 2007, https://doi.org/10.1002/humu.20535 (wanders2021fattyacidoxidation pages 69-70, ferdinandusse2007clinicalbiochemicaland pages 1-2) |
| Regression / loss of motor achievements | Neurodevelopmental regression (HP:0002376); Loss of ambulation (HP:0002505, if applicable); Motor regression (suggestive mapping under regression) | Typically early childhood after limited development; progressive decline | In the 26-patient cohort, 83% lost motor achievements; mean age of regression 28 months | Wanders et al. 2021 review summarizing 2007 cohort, https://doi.org/10.1007/978-3-030-60204-8_5 (wanders2021fattyacidoxidation pages 69-70) |
| Leukodystrophy / white matter demyelination (cerebral/cerebellar) | Leukodystrophy (HP:0002415); Abnormal cerebral white matter morphology (HP:0002500); Demyelination of the cerebral white matter (HP:0007256); Cerebellar white matter abnormality (suggestive) | Usually progressive from infancy/early childhood; MRI shows cerebral and/or cerebellar white matter involvement | Cerebral and/or cerebellar white matter abnormalities described in series; no pooled % stated in available excerpts | Wanders et al. 2021, https://doi.org/10.1007/978-3-030-60204-8_5; Rosewich et al. 2006, https://doi.org/10.1055/s-2006-923943; Wang et al. 2014, https://doi.org/10.1007/s10545-014-9698-3 (wanders2021fattyacidoxidation pages 69-70, rosewich12006pitfallinmetabolic pages 1-2, wang2014effectsofhematopoietic pages 1-2) |
| Vision loss / retinopathy | Visual impairment (HP:0000505); Blindness (HP:0000618); Retinal dystrophy/retinopathy (HP:0000556 / HP:0000488, suggestive depending on exam) | Progressive; may accompany regression and advanced neurodegeneration | Vision failure/loss described in cohort and case reports; no pooled % stated in available excerpts | Wanders et al. 2021, https://doi.org/10.1007/978-3-030-60204-8_5; Rosewich et al. 2006, https://doi.org/10.1055/s-2006-923943; Wang et al. 2014, https://doi.org/10.1007/s10545-014-9698-3 (wanders2021fattyacidoxidation pages 69-70, rosewich12006pitfallinmetabolic pages 1-2, wang2014effectsofhematopoietic pages 1-2) |
| Hearing impairment / deafness | Hearing impairment (HP:0000365); Sensorineural hearing impairment (HP:0000407); Deafness (HP:000036 deafness family, suggestive) | Progressive in some patients; may occur with global neurologic decline | Hearing impairment noted in series and case reports; no pooled % stated in available excerpts | Wanders et al. 2021, https://doi.org/10.1007/978-3-030-60204-8_5; Rosewich et al. 2006, https://doi.org/10.1055/s-2006-923943; Wang et al. 2014, https://doi.org/10.1007/s10545-014-9698-3 (wanders2021fattyacidoxidation pages 69-70, rosewich12006pitfallinmetabolic pages 1-2, wang2014effectsofhematopoietic pages 1-2) |
| Hepatomegaly | Hepatomegaly (HP:0002240) | Infantile or early childhood; may coexist with liver enzyme abnormalities | Mentioned as a characteristic feature; no % stated in available excerpts | Hajj et al. 2012, https://doi.org/10.1210/en.2012-1137; Wanders et al. 2021, https://doi.org/10.1007/978-3-030-60204-8_5 (hajj2012theinflammatoryresponse pages 1-2, wanders2021fattyacidoxidation pages 69-70) |
| Failure to thrive / poor feeding | Failure to thrive (HP:0001508); Poor feeding (HP:0011968) | Neonatal/infantile; may precede or accompany hypotonia and seizures | Described in early-onset severe cases; no pooled % stated in available excerpts | Wanders et al. 2021, https://doi.org/10.1007/978-3-030-60204-8_5; Rosewich et al. 2006, https://doi.org/10.1055/s-2006-923943 (wanders2021fattyacidoxidation pages 69-70, rosewich12006pitfallinmetabolic pages 1-2) |
| Craniofacial dysmorphism | Facial dysmorphism (HP:0001999); Abnormality of the face (HP:0000271) | Congenital/early recognized; generally non-remitting | Mentioned as characteristic in pseudoneonatal adrenoleukodystrophy; no % stated | Hajj et al. 2012, https://doi.org/10.1210/en.2012-1137; Wanders et al. 2021, https://doi.org/10.1007/978-3-030-60204-8_5 (hajj2012theinflammatoryresponse pages 1-2, wanders2021fattyacidoxidation pages 69-70) |
| Adrenal dysfunction / elevated ACTH | Adrenal insufficiency (HP:0000846); Increased circulating ACTH level (HP:0030831, suggestive) | Can emerge during childhood in some cases; endocrine monitoring may be warranted | Reported in at least one case with elevated ACTH; frequency not established in available evidence | Carrozzo et al. 2008, https://doi.org/10.1002/ajmg.a.32298 (carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2) |


*Table: This table maps major reported clinical features of peroxisomal acyl-CoA oxidase deficiency to suggested HPO terms and summarizes onset, progression, and any available frequency data. It is useful for structured disease curation and phenotype annotation in a knowledge base.*

---

## 4. Genetic / molecular information

### 4.1 Causal gene(s)
- **ACOX1** encodes peroxisomal acyl‑CoA oxidase 1 (straight‑chain acyl‑CoA oxidase), a key enzyme initiating peroxisomal β‑oxidation of straight‑chain VLCFA‑CoA substrates. (wanders2021fattyacidoxidation pages 69-70, ferdinandusse2007clinicalbiochemicaland pages 1-2)

A mechanistic note from patient-based work: ACOX1 “**is encoded by a single gene, which generates two splice variants**,” producing two isoforms; the disorder reflects loss of enzyme function. (hajj2012theinflammatoryresponse pages 1-2)

### 4.2 Pathogenic variants (examples; not exhaustive)
Variant-level evidence in the retrieved corpus includes:
- A homozygous splice-site variant **IVS3‑1G>A** causing exon skipping (fatal infant case; parents heterozygous). (rosewich12006pitfallinmetabolic pages 3-4)
- Large deletions and point mutations/exon-skipping variants have been reported in patients in general, consistent with loss-of-function mechanisms. (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2)

**Variant frequencies (gnomAD/ExAC) and ACMG classifications** were not available in the retrieved corpus and should be added from ClinVar/gnomAD in a subsequent curation pass.

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities specific to ACOX1 deficiency were identified in the retrieved corpus.

---

## 5. Environmental information
No validated environmental, lifestyle, or infectious contributors specific to ACOX1 deficiency were identified in the retrieved corpus.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (upstream → downstream)
1) **ACOX1 loss-of-function** → 2) impaired peroxisomal straight‑chain VLCFA β‑oxidation → 3) **VLCFA accumulation** in plasma/tissues → 4) cellular stress and inflammatory signaling (including IL‑1 axis) → 5) **inflammatory demyelination / leukodystrophy** and neurodegeneration. (hajj2012theinflammatoryresponse pages 1-1, rosewich12006pitfallinmetabolic pages 1-2, wanders2021fattyacidoxidation pages 69-70)

### 6.2 Inflammation and signaling (human fibroblast evidence)
Endocrinology 2012 used transcriptomic profiling of patient fibroblasts and concluded: “**the absence of acyl‑coenzyme A oxidase 1 activity in P‑NALD fibroblasts triggers an inflammatory process, in which the IL‑1 pathway seems to be central**.” They also report IL‑6/IL‑8 downregulation by kinase inhibitors: “**expression of IL‑6 and IL‑8 cytokines in patient fibroblasts was down‑regulated by MAPK, p38MAPK, and Jun N‑terminal kinase inhibitors**,” motivating inflammation-modulating strategies as a mechanistic hypothesis (preclinical/in vitro). (hajj2012theinflammatoryresponse pages 1-2)

**Suggested GO biological process terms (examples):**
- Peroxisomal fatty acid beta-oxidation (GO:0006635)
- Inflammatory response (GO:0006954)
- Interleukin-1–mediated signaling pathway (GO:0070498)
- Cytokine-mediated signaling pathway (GO:0019221)

### 6.3 Microglia-centered mechanisms (2023 development)
A 2023 BV‑2 microglia RNA‑seq study modeling peroxisomal β‑oxidation defects (including **Acox1−/−**) found large-scale transcriptional changes including lipid metabolism and immune programs and described “**a DAM-like signature**,” along with “**cholesterol accumulation in plasma membranes**” and altered lysosome/autophagy programs. The authors conclude peroxisomal defects in microglia “**force microglial cells to adopt a pathological phenotype**” likely contributing to peroxisomal leukodystrophy pathogenesis. (raas2023peroxisomaldefectsin pages 1-2)

**Suggested CL (cell ontology) term:** microglial cell (CL:0000129)

**Suggested GO terms (examples):**
- Microglial cell activation (GO:0001774)
- Autophagy (GO:0006914)
- Lysosome organization (GO:0007040)
- Cholesterol homeostasis (GO:0042632)

### 6.4 Biochemical abnormalities and metabolites (CHEBI suggestions)
- Very long-chain fatty acids (group) (rosewich12006pitfallinmetabolic pages 1-2)
- Cerotic acid (C26:0) (CHEBI:28841) (C26:0 highlighted as marker in patient testing) (rosewich12006pitfallinmetabolic pages 3-4)
- C26:0‑lysophosphatidylcholine (C26:0‑LPC; used in NBS for related peroxisomal disorders) (mohan2023evaluatingthestrength pages 3-4)

### 6.5 Tissue/cell injury and anatomical correlates
The dominant clinical pathology is CNS white matter involvement (leukodystrophy/demyelination) with additional systemic involvement such as hepatomegaly in some cases. (wanders2021fattyacidoxidation pages 69-70, hajj2012theinflammatoryresponse pages 1-2)

**Suggested UBERON terms (examples):**
- Brain white matter (UBERON:0002317)
- Cerebellum (UBERON:0002037)
- Liver (UBERON:0002107)

### 6.6 Molecular profiling / omics
- Patient-fibroblast transcriptomics and inflammatory pathway profiling were used to identify IL‑1 pathway activation. (hajj2012theinflammatoryresponse pages 1-2)
- Microglial RNA‑seq defined immune/lipid/autophagy modules and DAM-like programs under peroxisomal defects. (raas2023peroxisomaldefectsin pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ-level involvement
- **Central nervous system:** cerebral and cerebellar white matter abnormalities / demyelination (wanders2021fattyacidoxidation pages 69-70, rosewich12006pitfallinmetabolic pages 1-2)
- **Liver:** hepatomegaly described in clinical phenotypes (hajj2012theinflammatoryresponse pages 1-2, wanders2021fattyacidoxidation pages 69-70)
- **Auditory and visual systems:** progressive hearing and visual impairment reported (wanders2021fattyacidoxidation pages 69-70, wang2014effectsofhematopoietic pages 1-2)

### 7.2 Tissue/cell-level targets
- Oligodendrocyte–myelin units are implied targets by leukodystrophy/demyelination phenotype. (wanders2021fattyacidoxidation pages 69-70)
- Microglia are implicated mechanistically by disease-associated transcriptional changes under peroxisomal β‑oxidation impairment. (raas2023peroxisomaldefectsin pages 1-2)

### 7.3 Subcellular localization (GO cellular component)
- Peroxisome (GO:0005777) is the primary subcellular compartment for the enzymatic defect.

---

## 8. Temporal development

### 8.1 Onset
Most reported cases present in the neonatal period or infancy with hypotonia and seizures. (ferdinandusse2007clinicalbiochemicaland pages 1-2, rosewich12006pitfallinmetabolic pages 1-2)

### 8.2 Progression
The disease course is typically progressive neurodegeneration with regression in early childhood; in a summarized cohort, regression occurred at mean 28 months. (wanders2021fattyacidoxidation pages 69-70)

### 8.3 Remission/critical windows
No validated remission patterns were identified. The early childhood period before regression would be the presumed critical window for any future disease-modifying therapy, based on natural history summaries. (wanders2021fattyacidoxidation pages 69-70)

---

## 9. Inheritance and population

### 9.1 Inheritance
- **Autosomal recessive** (ferdinandusse2007clinicalbiochemicaland pages 1-2, carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2)

### 9.2 Epidemiology
Population-level prevalence and incidence values were not identified in the retrieved corpus. Available evidence indicates extreme rarity: one report notes that only a **small number of patients (~22 worldwide)** had been reported at the time of publication. (carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2)

---

## 10. Diagnostics

### 10.1 Core laboratory findings (clinical biochemistry)
- Typical diagnostic biochemical signature: **elevated VLCFAs**, including increased C26:0 and increased C26:0/C22:0 ratio. (rosewich12006pitfallinmetabolic pages 3-4)
- Some patients may have normal phytanic and pristanic acid oxidation and normal plasmalogen synthesis in fibroblasts, consistent with an isolated straight-chain VLCFA β‑oxidation defect. (rosewich12006pitfallinmetabolic pages 1-2)

**Diagnostic pitfall:** A fatal case report emphasizes that “**the finding of a normal very long-chain fatty acid profile does not exclude a peroxisomal disorder**,” supporting reflex testing beyond plasma VLCFA in clinically suggestive cases. (rosewich12006pitfallinmetabolic pages 1-2)

### 10.2 Confirmatory testing
- **Fibroblast functional testing:** markedly decreased C26:0 oxidation and reduced ACOX1 enzyme activity in cultured fibroblasts; immunoblot patterns can support ACOX1 deficiency. (rosewich12006pitfallinmetabolic pages 3-4)
- **Molecular genetic testing:** ACOX1 sequencing / transcript analysis confirms diagnosis (ferdinandusse2007clinicalbiochemicaland pages 1-2, rosewich12006pitfallinmetabolic pages 1-2). A review statement: “**definitive diagnosis of patients requires enzyme analysis in fibroblasts and/or genetic analysis of the ACOX1 gene**.” (wanders2021fattyacidoxidation pages 69-70)

### 10.3 Newborn screening and early detection (context and real-world implementation)
While ACOX1 deficiency is not a standard standalone newborn screening target in most jurisdictions, peroxisomal disorder newborn screening (initiated for X‑ALD) can detect broader classes of peroxisomal disorders. The ClinGen peroxisomal curation/nomenclature paper emphasizes: “**Newborn screening identifying elevated C26:0-lysophosphatidyl choline (C26:0-LPC) and molecular genetic testing are critical tools for the early detection of peroxisomal disorders**.” (mohan2023evaluatingthestrength pages 3-4)

### 10.4 Differential diagnosis (high-level)
Given overlapping biochemical and neuroimaging phenotypes, important differentials include other peroxisomal disorders with VLCFA elevation (e.g., X‑ALD, D-bifunctional protein deficiency, peroxisome biogenesis disorders). The diagnostic pitfall literature supports performing fibroblast enzymology/genetics when first-line plasma testing is non-diagnostic despite suggestive clinical features. (rosewich12006pitfallinmetabolic pages 1-2)

---

## 11. Outcome / prognosis

- Severe childhood phenotype is common and frequently fatal in childhood (mean death age 5 years; range 4–10 in a summarized cohort). (wanders2021fattyacidoxidation pages 69-70)
- Rare later-onset adult presentations exist. (wanders2021fattyacidoxidation pages 69-70)

Prognostic biomarkers beyond VLCFA levels were not identified in the retrieved corpus.

---

## 12. Treatment

### 12.1 Supportive care (standard of care)
The retrieved corpus did not provide formal consensus guidelines for ACOX1 deficiency. In practice, care is typically supportive and multidisciplinary (seizure management, nutritional support, management of feeding difficulties, respiratory/infection prevention), consistent with severe neurodegenerative leukodystrophy phenotypes. (inferred from described phenotypic course; see clinical cases) (carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2, wang2014effectsofhematopoietic pages 1-2)

**Suggested MAXO terms (examples):**
- Antiseizure therapy (MAXO:0000754; generic class)
- Nutritional support therapy (MAXO:0000076)
- Physical therapy/rehabilitation (MAXO:0000015)

### 12.2 Hematopoietic stem cell transplantation (HSCT) – limited evidence
A sibling comparison study evaluated HSCT in ACOX1 deficiency and reported: “**Although HSCT did not halt the course of ACOX1 deficiency, it reduced the extent of white matter inflammation in the brain**.” (wang2014effectsofhematopoietic pages 1-2)

Interpretation: HSCT may modulate neuroinflammation but is not established as disease-modifying for the neurodegenerative course; evidence is limited to small numbers and should be considered investigational/high-risk.

**Suggested MAXO term:** Hematopoietic stem cell transplantation (MAXO:0000747)

### 12.3 Mechanism-motivated anti-inflammatory strategies (preclinical/in vitro)
Patient fibroblast studies suggest kinase inhibitors can down-modulate inflammatory cytokine expression, and authors propose: “**The use of specific kinase inhibitors may permit the modulation of the enhanced inflammatory status**.” (hajj2012theinflammatoryresponse pages 1-2)

This is not clinical efficacy evidence; it provides a hypothesis linking VLCFA accumulation to cytokine networks and identifies candidate signaling nodes (MAPK/p38/JNK) for translational exploration.

### 12.4 Clinical trials / studies (real-world implementation)
- **NCT01668186** (Recruiting; observational): *Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD)*. URL: https://clinicaltrials.gov/study/NCT01668186. (ClinicalTrials.gov record retrieved in this run; peroxisomal disorders broadly)
- **NCT02171104** (Active, not recruiting; Phase 2): *MT2013-31: Allo HCT for Metabolic Disorders and Severe Osteopetrosis*. URL: https://clinicaltrials.gov/study/NCT02171104. (Trial includes metabolic disorders broadly)

These studies provide infrastructure for peroxisomal disorder natural history and transplant protocols but are not necessarily ACOX1-deficiency–specific.

---

## 13. Prevention

Given autosomal recessive inheritance, prevention focuses on **genetic counseling** and **reproductive options**:
- Carrier testing for at-risk relatives once familial ACOX1 variants are known. (rosewich12006pitfallinmetabolic pages 3-4)
- Prenatal or preimplantation genetic testing is feasible in principle when pathogenic variants are identified (general principles supported by the existence of prenatal diagnostic approaches for fatty acid oxidation/peroxisomal disorders). (wanders2021fattyacidoxidation pages 69-70)

Primary prevention via lifestyle/environmental modifications is not established.

---

## 14. Other species / natural disease
The retrieved corpus did not contain a clear naturally occurring veterinary disease homolog explicitly attributed to ACOX1 loss-of-function.

---

## 15. Model organisms

### 15.1 Mouse models (ACOX1 loss)
A classic Acox1 knockout mouse study (biochemical and hepatic phenotype) reports that ACOX-null mice “**accumulate very long chain fatty acids in blood**” and display liver pathology and altered peroxisome biology, demonstrating systemic consequences of ACOX loss. (fan1996 was retrieved but not processed into a citeable evidence snippet in this run; therefore not cited here.)

### 15.2 Cellular models (microglia)
A 2023 BV‑2 **Acox1−/−** microglial model recapitulated VLCFA accumulation and revealed DAM-like immune signatures, lysosome/autophagy programs, and cholesterol membrane changes, providing a mechanistic bridge to neuroinflammatory leukodystrophy. (raas2023peroxisomaldefectsin pages 1-2)

### 15.3 Zebrafish model (ACOX1 gain-of-function; adjacent ACOX1 biology)
A 2024 zebrafish model was developed for ACOX1 gain-of-function Mitchell syndrome (distinct from recessive ACOX1 deficiency) to study leukodystrophy mechanisms and test microglia-targeted antioxidant approaches; this supports broader ACOX1–white matter–neuroinflammation links but is not a direct loss-of-function model for OMIM #264470. (Not extracted into evidence snippets in this run; not cited.)

---

## 2023–2024 “latest research” highlights (prioritized)

1) **ClinGen/curation and nomenclature:** Mohan et al. (May 2023, *Molecular Genetics and Metabolism*) describes the ClinGen Peroxisomal Gene Curation Expert Panel and notes that **ACOX1** was curated for **two different disease entities** (loss-of-function vs upregulation/gain-of-function), and that newborn screening and molecular testing are critical tools for early detection of peroxisomal disorders. URL: https://doi.org/10.2139/ssrn.4330003 (mohan2023evaluatingthestrength pages 3-4)

2) **Microglial disease programs under peroxisomal β‑oxidation impairment:** Raas et al. (Apr 2023, *Frontiers in Molecular Neuroscience*) demonstrates that peroxisomal defects (including Acox1−/−) induce microglial immune reprogramming with “a DAM-like signature,” implicating microglia and autophagy/lysosomal processes as mechanistic contributors and potential therapeutic targets. URL: https://doi.org/10.3389/fnmol.2023.1170313 (raas2023peroxisomaldefectsin pages 1-2)

3) **Peroxisomes and neuroinflammation (broader context):** Sarkar & Lipinski (Oct 2024, *Cells*) reviews that peroxisomal functions (VLCFA degradation, ether lipid synthesis, ROS metabolism) are essential for restricting neuroinflammation and suggests strategies to enhance peroxisome biogenesis as a possible anti-inflammatory approach in the CNS. URL: https://doi.org/10.3390/cells13191655 (sarkar2024roleandfunction pages 9-10)

---

## Key data/statistics extracted
- Regression/loss of motor achievements in **83%** of patients; **mean age of regression 28 months** (summary of a 26‑patient series). (wanders2021fattyacidoxidation pages 69-70)
- **Mean age of death 5 years** (range 4–10) in that summarized cohort. (wanders2021fattyacidoxidation pages 69-70)
- Case-report enzymology example: ACOX1 activity ~10% of normal in fibroblasts (9.8 vs 89 pmol/min·mg) (rosewich12006pitfallinmetabolic pages 3-4)

---

## Limitations / gaps for knowledge-base completion
- MONDO/Orphanet/ICD/MeSH identifiers were not recovered in the retrieved full texts.
- Robust prevalence/incidence estimates are absent in the retrieved corpus.
- Variant-level population frequencies and ClinVar classifications were not retrieved.
- Evidence for disease-modifying therapy is sparse; HSCT evidence is limited and not definitively effective.

---

## References (URLs and publication timing as available in retrieved evidence)
- Ferdinandusse et al. *Human Mutation* (Sep 2007). https://doi.org/10.1002/humu.20535 (ferdinandusse2007clinicalbiochemicaland pages 1-2)
- Carrozzo et al. *Am J Med Genet A* (Jul 2008). https://doi.org/10.1002/ajmg.a.32298 (carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2)
- Rosewich et al. *Neuropediatrics* (Apr 2006). https://doi.org/10.1055/s-2006-923943 (rosewich12006pitfallinmetabolic pages 1-2)
- Wang et al. *J Inherit Metab Dis* (Mar 2014). https://doi.org/10.1007/s10545-014-9698-3 (wang2014effectsofhematopoietic pages 1-2)
- Hajj et al. *Endocrinology* (Apr 2012). https://doi.org/10.1210/en.2012-1137 (hajj2012theinflammatoryresponse pages 1-2)
- Wanders et al. *Adv Exp Med Biol* (2021). https://doi.org/10.1007/978-3-030-60204-8_5 (wanders2021fattyacidoxidation pages 69-70)
- Mohan et al. *Mol Genet Metab* (May 2023). https://doi.org/10.2139/ssrn.4330003 (mohan2023evaluatingthestrength pages 3-4)
- Raas et al. *Front Mol Neurosci* (Apr 2023). https://doi.org/10.3389/fnmol.2023.1170313 (raas2023peroxisomaldefectsin pages 1-2)
- Sarkar & Lipinski *Cells* (Oct 2024). https://doi.org/10.3390/cells13191655 (sarkar2024roleandfunction pages 9-10)
- ClinicalTrials.gov NCT01668186. https://clinicaltrials.gov/study/NCT01668186
- ClinicalTrials.gov NCT02171104. https://clinicaltrials.gov/study/NCT02171104


References

1. (ferdinandusse2007clinicalbiochemicaland pages 1-2): Sacha Ferdinandusse, Simone Denis, Eveline M. Hogenhout, Janet Koster, Carlo W.T. van Roermund, Lodewijk IJlst, Ann B. Moser, Ronald J.A. Wanders, and Hans R. Waterham. Clinical, biochemical, and mutational spectrum of peroxisomal acyl–coenzyme a oxidase deficiency. Human Mutation, 28:904-912, Sep 2007. URL: https://doi.org/10.1002/humu.20535, doi:10.1002/humu.20535. This article has 180 citations and is from a domain leading peer-reviewed journal.

2. (carrozzo2008peroxisomalacyl‐coa‐oxidasedeficiency pages 1-2): Rosalba Carrozzo, Carlo Bellini, Simona Lucioli, Federica Deodato, Denise Cassandrini, Michela Cassanello, Ubaldo Caruso, Cristiano Rizzo, Teresa Rizza, Matteo L. Napolitano, Ronald J.A. Wanders, Cornelis Jakobs, Claudio Bruno, Filippo M. Santorelli, Carlo Dionisi‐Vici, and Eugenio Bonioli. Peroxisomal acyl‐coa‐oxidase deficiency: two new cases. American Journal of Medical Genetics Part A, 146A:1676-1681, Jul 2008. URL: https://doi.org/10.1002/ajmg.a.32298, doi:10.1002/ajmg.a.32298. This article has 43 citations.

3. (wanders2021fattyacidoxidation pages 69-70): Ronald J. A. Wanders, Frédéric M. Vaz, Hans R. Waterham, and Sacha Ferdinandusse. Fatty acid oxidation in peroxisomes: enzymology, metabolic crosstalk with other organelles and peroxisomal disorders. Advances in experimental medicine and biology, 1299:55-70, Jan 2021. URL: https://doi.org/10.1007/978-3-030-60204-8\_5, doi:10.1007/978-3-030-60204-8\_5. This article has 76 citations and is from a peer-reviewed journal.

4. (mohan2023evaluatingthestrength pages 3-4): Shruthi Mohan, Megan Mayers, Meredith Weaver, Heather Baudet, Irene De Biase, Jennifer Goldstein, Rong Mao, Jennifer McGlaughon, Ann Moser, Aurora Pujol, Sharon Suchy, Tatiana Yuzyuk, and Nancy E. Braverman. Evaluating the strength of evidence for genes implicated in peroxisomal disorders using the clingen clinical validity framework and providing updates to the peroxisomal disease nomenclature. Molecular genetics and metabolism, 139 3:107604, May 2023. URL: https://doi.org/10.2139/ssrn.4330003, doi:10.2139/ssrn.4330003. This article has 3 citations and is from a peer-reviewed journal.

5. (raas2023peroxisomaldefectsin pages 1-2): Quentin Raas, Ali Tawbeh, Mounia Tahri-Joutey, Catherine Gondcaille, Céline Keime, Romain Kaiser, Doriane Trompier, Boubker Nasser, Valerio Leoni, Emma Bellanger, Maud Boussand, Yannick Hamon, Alexandre Benani, Francesca Di Cara, Caroline Truntzer, Mustapha Cherkaoui-Malki, Pierre Andreoletti, and Stéphane Savary. Peroxisomal defects in microglial cells induce a disease-associated microglial signature. Frontiers in Molecular Neuroscience, Apr 2023. URL: https://doi.org/10.3389/fnmol.2023.1170313, doi:10.3389/fnmol.2023.1170313. This article has 15 citations.

6. (rosewich12006pitfallinmetabolic pages 1-2): H. Rosewich1, H. Waterham2, R. Wanders2, S. Ferdinandusse2, M. Henneke1, D. Hunneman1, and J. Gärtner1. Pitfall in metabolic screening in a patient with fatal peroxisomal β-oxidation defect. Neuropediatrics, 37:95-98, Apr 2006. URL: https://doi.org/10.1055/s-2006-923943, doi:10.1055/s-2006-923943. This article has 46 citations and is from a peer-reviewed journal.

7. (hajj2012theinflammatoryresponse pages 1-1): H. Hajj, Aurore Vluggens, Aurore Vluggens, P. Andreoletti, K. Ragot, S. Mandard, Sander Kersten, H. Waterham, Gérard Lizard, R. J. Wanders, Janardan K. Reddy, and M. Cherkaoui‐Malki. The inflammatory response in acyl-coa oxidase 1 deficiency (pseudoneonatal adrenoleukodystrophy). Endocrinology, 153:2568-2575, Apr 2012. URL: https://doi.org/10.1210/en.2012-1137, doi:10.1210/en.2012-1137. This article has 51 citations and is from a domain leading peer-reviewed journal.

8. (wang2014effectsofhematopoietic pages 1-2): Raymond Y. Wang, Edwin S. Monuki, James Powers, Phillip H. Schwartz, Paul A. Watkins, Yang Shi, Ann Moser, David A. Shrier, Hans R. Waterham, Diane J. Nugent, and Jose E. Abdenur. Effects of hematopoietic stem cell transplantation on acyl-coa oxidase deficiency: a sibling comparison study. Journal of Inherited Metabolic Disease, 37:791-799, Mar 2014. URL: https://doi.org/10.1007/s10545-014-9698-3, doi:10.1007/s10545-014-9698-3. This article has 24 citations and is from a peer-reviewed journal.

9. (hajj2012theinflammatoryresponse pages 1-2): H. Hajj, Aurore Vluggens, Aurore Vluggens, P. Andreoletti, K. Ragot, S. Mandard, Sander Kersten, H. Waterham, Gérard Lizard, R. J. Wanders, Janardan K. Reddy, and M. Cherkaoui‐Malki. The inflammatory response in acyl-coa oxidase 1 deficiency (pseudoneonatal adrenoleukodystrophy). Endocrinology, 153:2568-2575, Apr 2012. URL: https://doi.org/10.1210/en.2012-1137, doi:10.1210/en.2012-1137. This article has 51 citations and is from a domain leading peer-reviewed journal.

10. (rosewich12006pitfallinmetabolic pages 3-4): H. Rosewich1, H. Waterham2, R. Wanders2, S. Ferdinandusse2, M. Henneke1, D. Hunneman1, and J. Gärtner1. Pitfall in metabolic screening in a patient with fatal peroxisomal β-oxidation defect. Neuropediatrics, 37:95-98, Apr 2006. URL: https://doi.org/10.1055/s-2006-923943, doi:10.1055/s-2006-923943. This article has 46 citations and is from a peer-reviewed journal.

11. (sarkar2024roleandfunction pages 9-10): Chinmoy Sarkar and Marta M. Lipinski. Role and function of peroxisomes in neuroinflammation. Cells, 13:1655, Oct 2024. URL: https://doi.org/10.3390/cells13191655, doi:10.3390/cells13191655. This article has 13 citations.