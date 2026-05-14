---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T19:11:52.505645'
end_time: '2026-05-08T19:29:56.789508'
duration_seconds: 1084.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glutaryl-CoA Dehydrogenase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glutaryl-CoA Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glutaryl-CoA Dehydrogenase Deficiency** covering all of the
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
- **Disease Name:** Glutaryl-CoA Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glutaryl-CoA Dehydrogenase Deficiency** covering all of the
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


# Comprehensive Disease Characteristics Report: Glutaryl‑CoA Dehydrogenase Deficiency (Glutaric Aciduria Type 1, GA1)

## Executive summary
Glutaryl‑CoA dehydrogenase deficiency—commonly called **glutaric aciduria type 1 (GA1)**—is an **autosomal recessive** neurometabolic disorder of **lysine, hydroxylysine, and tryptophan catabolism** due to pathogenic variants in **GCDH**, leading to accumulation of **glutaric acid (GA)**, **3‑hydroxyglutaric acid (3‑OH‑GA)**, and **glutarylcarnitine (C5DC)**. The classic catastrophic outcome is **acute or insidious striatal injury** in early childhood with a severe dystonic movement disorder; critically, outcomes improve markedly with **newborn screening (NBS)** plus early dietary and emergency management, but false positives and false negatives (especially “low excretors”) remain important challenges. (kolker2011diagnosisandmanagement pages 1-2, kolker2011diagnosisandmanagement pages 2-4, zhou2023biochemicalandmolecular pages 1-2)

## Abbreviations
GA1: glutaric aciduria type 1; GCDH: glutaryl‑CoA dehydrogenase; DBS: dried blood spot; MS/MS: tandem mass spectrometry; GC/MS: gas chromatography mass spectrometry; NBS: newborn screening; HE/LE: high/low excretor biochemical phenotypes; C5DC: glutarylcarnitine.

---

## 1. Disease information
### 1.1 What is the disease?
**GA1** is a rare organic aciduria/neurometabolic disease caused by deficiency of mitochondrial **glutaryl‑CoA dehydrogenase (GCDH)**, which is required for the catabolism of lysine, hydroxylysine, and tryptophan; deficiency leads to accumulation of GA, 3‑OH‑GA, glutaconic acid, and C5DC (detectable by GC/MS and MS/MS). (kolker2011diagnosisandmanagement pages 1-2, schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2)

**Authoritative guideline definition (abstract quote):**
- “Glutaric aciduria type I (synonym, glutaric acidemia type I) is a rare organic aciduria.” (Kölker et al., 2011, *J Inherit Metab Dis*, published 2011‑03; DOI:10.1007/s10545-011-9289-5; https://doi.org/10.1007/s10545-011-9289-5) (kolker2011diagnosisandmanagement pages 1-2)
- “This defect gives rise to elevated glutaric acid, 3-hydroxyglutaric acid, glutaconic acid, and glutarylcarnitine which can be detected by gas chromatography/mass spectrometry (organic acids) or tandem mass spectrometry (acylcarnitines).” (same abstract) (kolker2011diagnosisandmanagement pages 1-2)

### 1.2 Key identifiers (retrieved from current evidence)
- **Disease OMIM:** **231670** (GA1) (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2, kolker2011diagnosisandmanagement pages 1-2)
- **Causal gene:** **GCDH** (gene OMIM **608801**) (kolker2011diagnosisandmanagement pages 2-4)

**Not retrieved in the current tool evidence set (will require external database lookup):** MONDO ID, Orphanet ID, MeSH ID, ICD‑10/ICD‑11 codes.

### 1.3 Synonyms and alternative names
- Glutaric aciduria type I / type 1 (GA‑I/GA1) (kolker2011diagnosisandmanagement pages 1-2)
- Glutaric acidemia type I / type 1 (GA‑I/GA1) (kolker2011diagnosisandmanagement pages 1-2)
- Glutaryl‑CoA dehydrogenase deficiency (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2)

### 1.4 Evidence provenance (patient vs aggregated)
The current evidence includes:
- **Aggregated resources/guidelines & literature syntheses:** major clinical guideline (2011) and variant landscape/genotype–phenotype synthesis (2023). (kolker2011diagnosisandmanagement pages 1-2, schuurmans2023exploringgenotype–phenotypecorrelations pages 1-2)
- **Population screening cohorts:** large NBS program data (Germany; 2024) and provincial NBS cohort (China; 2023). (zaunseder2024digitaltierstrategyimproves pages 2-4, zhou2023biochemicalandmolecular pages 1-2)
- **Mechanistic/therapeutics research:** protein misfolding characterization (2023) and emerging therapy preclinical studies (AAV; chaperones; 2024). (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2, mateubosch2024systemicdeliveryof pages 1-2, barroso2024useofthe pages 2-3)
- **Case reports** to illustrate diagnostic pitfalls (2025). (gragnaniello2025diagnosisofglutaric pages 1-2, larancuent2025delayeddiagnosisof pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
- **Primary cause:** biallelic pathogenic variants in **GCDH**, encoding mitochondrial glutaryl‑CoA dehydrogenase (FAD‑dependent homotetramer), impairing conversion of glutaryl‑CoA to crotonyl‑CoA. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)

### 2.2 Risk factors
- **Genetic:** autosomal recessive inheritance; population-specific founder variants reported (e.g., p.Ala421Val in Amish; IVS1+5G>T in Ojibwe; p.Arg402Trp relatively frequent in Europeans). (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3)
- **Physiologic/environmental triggers for neurologic crises:** catabolic stressors including infectious illness, surgery, immunizations, fasting, and febrile illness, especially in early childhood. (kolker2011diagnosisandmanagement pages 1-2, kolker2011diagnosisandmanagement pages 2-4)

### 2.3 Protective factors
- **Early detection + combined metabolic management** is protective against striatal injury, especially when initiated pre‑symptomatically. (kolker2011diagnosisandmanagement pages 1-2, kolker2011diagnosisandmanagement pages 4-5)

### 2.4 Gene–environment interaction (clinical concept)
GA1’s major neurologic injury is strongly **triggered by catabolic states** (environment/physiology) interacting with the underlying enzymatic block. (kolker2011diagnosisandmanagement pages 2-4, kolker2011diagnosisandmanagement pages 9-10)

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum (current understanding)
**Critical early-childhood neurologic vulnerability:** Untreated GA1 typically causes neurologic disease during a finite early developmental window. The 2011 guideline summarizes that untreated GA‑I leads to neurologic disease in ~90% during **3–36 months**, often after an encephalopathic crisis. (kolker2011diagnosisandmanagement pages 2-4)

**Key phenotypes and suggested HPO terms** (with evidence and typical timing):
- **Macrocephaly** (HP:0000256): reported in ~75% of infants in guideline synthesis; can be early sign but non‑specific. (kolker2011diagnosisandmanagement pages 2-4)
- **Acute encephalopathic crisis / metabolic decompensation** (e.g., HP:0002374 “Acute encephalopathy”): crises precipitated by infection/immunization/surgery; typical 3–36 months. (kolker2011diagnosisandmanagement pages 1-2, kolker2011diagnosisandmanagement pages 2-4)
- **Striatal/basal ganglia injury** (radiologic/clinical correlate; e.g., HP:0002134 “Basal ganglia abnormality”): acute bilateral striatal injury following crises. (kolker2011diagnosisandmanagement pages 2-4)
- **Dystonia / complex movement disorder** (HP:0001332): often severe, static, and disabling after striatal injury; dystonia on axial hypotonia is described as dominant. (kolker2011diagnosisandmanagement pages 2-4)
- **Developmental delay / motor delay** (HP:0001263 / HP:0001270): transient early delay may occur; neuroregression can follow crises. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2, kolker2011diagnosisandmanagement pages 2-4)
- **Seizures/status epilepticus** (HP:0001250): may occur during decompensation; can contribute to mortality (case-based). (patil2024glutaricaciduriapresenting pages 1-2)
- **Characteristic neuroimaging**: widened Sylvian fissures/frontotemporal atrophy are often noted; “macrocephaly and frontotemporal atrophy at birth” and widened Sylvian fissures are commonly cited. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2, patil2024glutaricaciduriapresenting pages 1-2)

### 3.2 Severity, progression, and frequency notes
- **High morbidity/mortality without treatment:** “Untreated patients characteristically develop dystonia during infancy resulting in a high morbidity and mortality.” (Kölker et al., 2011 abstract) (kolker2011diagnosisandmanagement pages 1-2)
- **Insidious onset:** guideline synthesis notes 10–20% may develop insidious/late onset without a documented crisis. (kolker2011diagnosisandmanagement pages 2-4)

### 3.3 Quality-of-life impact
Severe dystonia/complex movement disorder after striatal injury implies lifelong disability and dependence; direct standardized QoL instrument statistics were not retrieved in the current evidence set. (kolker2011diagnosisandmanagement pages 2-4)

---

## 4. Genetic / molecular information
### 4.1 Causal gene(s)
- **GCDH** (chromosome **19p13.13/p13.2** reported across sources) encodes a **438 aa** precursor with N‑terminal mitochondrial targeting sequence; mature enzyme is a **FAD‑dependent homotetramer**. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2)

### 4.2 Pathogenic variant spectrum
**Scale of known pathogenic variation (recent synthesis):**
- A 2023 comprehensive genotype–phenotype study reports **421 different GCDH pathogenic variants** identified and analyzed across **532 patients**, with four novel variants listed. (Schuurmans et al., 2023; DOI:10.1002/jimd.12608; https://doi.org/10.1002/jimd.12608; published 2023‑04) (schuurmans2023exploringgenotype–phenotypecorrelations pages 1-2)

**Variant types:** mostly missense, with also nonsense, intronic variants, and deletions described in databases. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3)

### 4.3 Biochemical subtypes (HE vs LE) and relation to residual activity
- Patients are frequently grouped by urinary GA excretion: **LE <100 mmol/mol creatinine** vs **HE >100 mmol/mol creatinine**. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3)
- Reported correlation: variants with **0–2%** or **<5%** residual activity tend to be HE; variants with **3–30%** residual activity tend to be LE/low‑GA excretion. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)
- Importantly, the 2011 guideline notes **LE patients have the same risk of striatal injury as HE** (i.e., biochemical “mildness” does not ensure clinical safety). (kolker2011diagnosisandmanagement pages 1-2)

### 4.4 Population variation and founder effects (examples)
- Founder variants: **p.Ala421Val** (Amish) and **IVS1+5G>T** (Ojibwe) are highlighted; **p.Arg402Trp** is relatively frequent in Europeans. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3)
- Example regional spectrum (Fujian, China): among 35 unrelated patients, three variants represented **~73%** of alleles; **c.1244‑2A>C** was predominant. (zhou2023biochemicalandmolecular pages 1-2)

### 4.5 Modifier genes / epigenetics / chromosomal abnormalities
No specific modifier genes, epigenetic mechanisms, or chromosomal abnormalities were retrieved in the current evidence set.

---

## 5. Environmental information
GA1 is a Mendelian disorder; “environmental” contributions primarily manifest as **catabolic triggers** for crises:
- Intercurrent infections, immunization, surgery, fasting/febrile illness precipitating encephalopathic crises during a vulnerable developmental period. (kolker2011diagnosisandmanagement pages 1-2, kolker2011diagnosisandmanagement pages 2-4)

No toxin/pollution/infectious etiologic agent was indicated.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (biochemical → cellular → clinical)
1. **Upstream trigger:** inherited GCDH deficiency (loss of mitochondrial glutaryl‑CoA dehydrogenase function) in lysine/hydroxylysine/tryptophan catabolism. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2, kolker2011diagnosisandmanagement pages 1-2)
2. **Metabolic block:** impaired conversion of **glutaryl‑CoA → crotonyl‑CoA**, leading to accumulation of **glutaryl‑CoA** and derivatives including **GA** and **3‑OH‑GA**; secondary **carnitine depletion** and increased **C5DC** reflect conjugation/detoxification. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)
3. **Neurotoxicity/energy impairment:** accumulated organic acids are described to interfere with cerebral energy metabolism and contribute to neurologic injury. (patil2024glutaricaciduriapresenting pages 1-2)
4. **Tissue vulnerability:** during early development, catabolic stress can trigger an encephalopathic crisis, leading to **bilateral striatal injury** and a severe dystonic movement disorder. (kolker2011diagnosisandmanagement pages 2-4, kolker2011diagnosisandmanagement pages 1-2)

### 6.2 Protein dysfunction and “misfolding disorder” concept (recent development)
A 2023 molecular study supports that many GA1 missense variants cause **GCDH misfolding** with altered oligomerization/tetramerization, reduced stability/solubility, increased aggregation, and loss of activity—supporting GA1 as a **protein misfolding disorder** and motivating pharmacological chaperone therapies. (Barroso et al., 2023; DOI:10.3390/ijms241713158; published 2023‑08; https://doi.org/10.3390/ijms241713158) (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)

### 6.3 Pathways and ontology suggestions
- **Pathway concept:** lysine degradation / amino‑acid catabolism in mitochondria (supported by disease definitions and biomarkers). (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2, kolker2011diagnosisandmanagement pages 1-2)
- **Suggested GO Biological Process terms (examples):** lysine catabolic process; tryptophan catabolic process; mitochondrial fatty acid beta‑oxidation (context: acyl‑CoA dehydrogenase family); response to starvation; cellular response to oxidative stress (the latter not directly retrieved here).
- **Suggested GO Cellular Component:** mitochondrion; mitochondrial matrix.
- **Suggested CL cell types:** striatal medium spiny neuron (target of striatal injury); astrocyte and microglia (gliosis is reported in mouse gene therapy study outcomes). (mateubosch2024systemicdeliveryof pages 1-2)

### 6.4 Molecular profiling / omics
No transcriptomics/proteomics/metabolomics multi‑omics datasets were retrieved in the current evidence set.

---

## 7. Anatomical structures affected
### 7.1 Organ level
- **Central nervous system** is the principal affected system, with the key lesion being **striatal/basal ganglia injury**. (kolker2011diagnosisandmanagement pages 2-4)

### 7.2 Tissue/cell level
- **Striatum / basal ganglia circuits**: bilateral striatal injury is the neuropathological correlate of the movement disorder. (kolker2011diagnosisandmanagement pages 1-2)

### 7.3 Subcellular level
- **Mitochondria**: GCDH is a mitochondrial enzyme; dysfunction is mitochondrial metabolic. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2)

### 7.4 Suggested UBERON terms
- Striatum (UBERON:0002435)
- Basal ganglion (UBERON:0002420)
- Brain (UBERON:0000955)

---

## 8. Temporal development
### 8.1 Onset
- Many infants are initially asymptomatic or show macrocephaly/transient delay early in life. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2)

### 8.2 Critical period and progression
- A major “window of vulnerability” is **infancy to early childhood**; encephalopathic crises and striatal injury are concentrated in **3–36 months** in guideline synthesis, and encephalopathic crises are described as rare after ~6 years. (kolker2011diagnosisandmanagement pages 2-4, kolker2011diagnosisandmanagement pages 10-12)

---

## 9. Inheritance and population
### 9.1 Inheritance
- **Autosomal recessive**. (kolker2011diagnosisandmanagement pages 1-2)

### 9.2 Epidemiology (recent data prioritized)
- **Fujian Province, China (2014–2022):** incidence **1 in 63,948** based on **1,151,069** screened and **18** NBS diagnoses. (Zhou et al., 2023, *Orphanet J Rare Dis*, published 2023‑07; DOI:10.1186/s13023-023-02833-z; https://doi.org/10.1186/s13023-023-02833-z) (zhou2023biochemicalandmolecular pages 1-2)
- **Germany (Heidelberg NBS context):** cited birth prevalence **1:135,000**. (Zaunseder et al., 2024, *Int J Neonatal Screen*, published 2024‑12; DOI:10.3390/ijns10040083; https://doi.org/10.3390/ijns10040083) (zaunseder2024digitaltierstrategyimproves pages 1-2)
- Broad synthesis: prevalence varies widely (~1:125,000 general to ~1:250 high‑risk groups). (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2)

### 9.3 Carrier frequency / penetrance / expressivity
Not quantified in the current evidence set; GA1 shows variable expressivity and incomplete genotype–phenotype correlation (see Section 4). (schuurmans2023exploringgenotype–phenotypecorrelations pages 1-2)

---

## 10. Diagnostics
### 10.1 Core biochemical markers
- **Screening marker (DBS, MS/MS):** **C5DC (glutarylcarnitine)**. (kolker2011diagnosisandmanagement pages 4-5, zhou2023biochemicalandmolecular pages 1-2)
- **Confirmatory urine organic acids (GC/MS):** elevated **GA** and **3‑OH‑GA**. (kolker2011diagnosisandmanagement pages 4-5, zhou2023biochemicalandmolecular pages 1-2)

### 10.2 Confirmatory genetic/enzyme testing
The 2011 guideline recommends diagnosis by:
- Quantitative GA/3‑OH‑GA, plus **GCDH mutation analysis** (reported sensitivity **98–99%**), and/or **enzyme analysis**; enzyme activity testing in fibroblasts/leukocytes is described as the **“gold standard”** for confirmation. (kolker2011diagnosisandmanagement pages 7-8)

### 10.3 Newborn screening implementation and performance (real‑world)
**Heidelberg (Germany) program (2014–2021):** reported sensitivity **100%**, specificity **99.94%**, false‑positive rate **0.06%**, PPV **1.5%**. (zaunseder2024digitaltierstrategyimproves pages 2-4)

**False positives and follow‑up:** In the Heidelberg suspected‑diagnosis set, urinary 3‑OH‑GA excluded GA1 in **90%** of false positives; **7%** had elevated 3‑OH‑GA prompting additional genetic/enzymatic work‑up. (zaunseder2024digitaltierstrategyimproves pages 5-7)

**Recent development (2024): digital‑tier machine learning to reduce GA1 NBS false positives.** The Heidelberg group reports that a digital‑tier strategy using logistic regression/ridge regression/SVM can reduce false positives by **>90%** while retaining case detection; e.g., reducing test‑set false positives from **235 → 16** (LR trained on full set) or **235 → 18** (LR trained on suspected set) with **100% sensitivity**. (zaunseder2024digitaltierstrategyimproves pages 1-2, zaunseder2024digitaltierstrategyimproves pages 7-8, zaunseder2024digitaltierstrategyimproves media 0bbb340b)

### 10.4 False negatives and “low excretor” challenge
- Low excretors can have **normal C5DC in DBS and normal urine GA/3‑OH‑GA**, causing **false‑negative NBS**, and may require diagnosis via clinical suspicion + MRI + molecular testing. (gragnaniello2025diagnosisofglutaric pages 1-2)
- A delayed-diagnosis case-based review emphasizes that biochemical markers may be “within normal limits” and that exome sequencing can establish diagnosis when biomarkers/imaging are inconclusive. (larancuent2025delayeddiagnosisof pages 1-2)

### 10.5 Differential diagnosis
Not comprehensively retrieved from the current evidence set; in practice includes other organic acidurias and basal ganglia injury disorders.

---

## 11. Outcome / prognosis
### 11.1 Prognosis with vs without early treatment
Guideline-level evidence supports strong benefit of early diagnosis and combined therapy:
- “It has been shown that in the majority of neonatally diagnosed patients striatal injury can be prevented by combined metabolic treatment.” (Kölker et al., 2011 abstract) (kolker2011diagnosisandmanagement pages 1-2)
- The guideline also states: “initiation of treatment after the onset of symptoms is generally not effective in preventing permanent damage.” (same abstract) (kolker2011diagnosisandmanagement pages 1-2)

### 11.2 Residual risk despite early treatment
A 2023 review notes that, despite improved outcomes with NBS and therapy, **15–23%** of early-treated patients may still experience encephalopathic crises. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)

---

## 12. Treatment
### 12.1 Standard of care (authoritative guideline)
The 2011 revised recommendations emphasize:
- **Maintenance therapy:** low‑lysine diet (often with lysine‑free/tryptophan‑reduced amino acid supplements) plus **L‑carnitine supplementation**; recommended especially during the 0–6 year vulnerability window. (kolker2011diagnosisandmanagement pages 8-9, kolker2011diagnosisandmanagement pages 7-8)
- **Emergency therapy:** prompt, aggressive treatment during febrile illness/surgery/immunization; includes high‑energy carbohydrate intake, temporary natural protein reduction/omission for 24–48 h with staged reintroduction, and increased carnitine dosing with careful monitoring. (kolker2011diagnosisandmanagement pages 9-10, kolker2011diagnosisandmanagement pages 10-12)

**Guideline quote supporting comparative importance:**
- “It showed for the first time that both basic metabolic treatment (low lysine diet, carnitine supplementation) and emergency treatment were clearly beneficial for patients diagnosed by newborn screening.” (kolker2011diagnosisandmanagement pages 4-5)
- “The beneficial effect of emergency treatment was more pronounced than that of maintenance treatment.” (kolker2011diagnosisandmanagement pages 4-5)

### 12.2 Evidence of real-world implementations
- **NBS-linked metabolic care** is implemented in multiple countries/centers; large NBS datasets show confirmatory workflows and follow-up testing (e.g., urine 3‑OH‑GA confirmation in Heidelberg). (zaunseder2024digitaltierstrategyimproves pages 5-7)

### 12.3 Emerging therapies (2023–2024 prioritized)
#### (A) Gene replacement therapy (preclinical)
A 2024 preclinical study reports systemic **AAV9‑GCDH** delivery in **Gcdh−/−** mice:
- Neonatal systemic AAV‑GCDH restored hepatic and striatal GCDH activity and prevented high‑lysine‑diet induced lethality (**~60% death** in untreated KO vs **complete survival** with neonatal gene therapy), reduced brain metabolite accumulation, and protected against striatal injury on MRI and pathology. (Mateu‑Bosch et al., 2024‑09; DOI:10.1016/j.omtm.2024.101276; https://doi.org/10.1016/j.omtm.2024.101276) (mateubosch2024systemicdeliveryof pages 1-2)

#### (B) Pharmacological chaperones / allosteric stabilizers (structure-guided discovery)
A 2024 *Journal of Medicinal Chemistry* study applies a **site‑directed enzyme enhancement therapy (SEE‑Tx)** computational platform to identify **allosteric pharmacological chaperones** (structure‑targeted allosteric regulators) for GCDH:
- Virtual screening of ~2.7 million compounds, experimental validation hit rate >20%, and multiple validated binders (one with **Kd 3.4 μM**) that increased stability and/or activity in biochemical assays—supporting feasibility of small-molecule rescue strategies for misfolding variants. (Barroso et al., 2024‑09; DOI:10.1021/acs.jmedchem.4c00292; https://doi.org/10.1021/acs.jmedchem.4c00292) (barroso2024useofthe pages 10-10, barroso2024useofthe pages 2-3)

### 12.4 MAXO suggestions (examples)
- Dietary lysine restriction (MAXO: dietary modification)
- Emergency metabolic decompensation management (MAXO: emergency treatment)
- Levocarnitine supplementation (MAXO: supplementation)
- Gene therapy (AAV-mediated gene transfer) (MAXO: gene therapy)

---

## 13. Prevention
- **Secondary prevention:** NBS programs detect GA1 before symptoms; guideline-level evidence indicates early detection + treatment can prevent striatal injury in most neonatally diagnosed cases. (kolker2011diagnosisandmanagement pages 1-2)
- **Tertiary prevention:** strict emergency protocols during illness/surgery/immunization reduce risk of acute striatal injury in vulnerable period. (kolker2011diagnosisandmanagement pages 9-10, kolker2011diagnosisandmanagement pages 10-12)

---

## 14. Other species / natural disease
No naturally occurring GA1 in non-human species was retrieved in the current evidence set.

---

## 15. Model organisms
### 15.1 Mouse model (genetic)
- **Gcdh knockout mouse** challenged with high‑lysine diet is used to model provoked metabolic injury and test therapeutics; AAV9‑GCDH gene therapy demonstrates prevention of lethality and striatal pathology, supporting translational development. (mateubosch2024systemicdeliveryof pages 1-2, mateubosch2024systemicdeliveryof pages 6-7)

### 15.2 Suggested applications and limitations
- Application: evaluate metabolite‑driven neurotoxicity and CNS-targeting gene replacement strategies.
- Limitation (from gene therapy study): CNS transduction is much higher with neonatal dosing; adult dosing yields poor CNS expression, highlighting developmental constraints. (mateubosch2024systemicdeliveryof pages 6-7)

---

## Key quantitative evidence table
The following table compiles major statistics (epidemiology, screening performance, variant frequencies, and emerging therapies) from the retrieved sources.

| Topic | Metric/Result | Population/Study | Year | PMID or DOI | URL | Evidence type | Citation |
|---|---|---|---|---|---|---|---|
| Epidemiology | Worldwide frequency about **1 in 100,000 births** | General/global estimate summarized in GA1 molecular review | 2023 | DOI: 10.3390/ijms241713158 | https://doi.org/10.3390/ijms241713158 | Review/mechanistic human disease summary | (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2) |
| Epidemiology | Prevalence ranges from **~1:125,000** in general populations to **~1:250** in high-risk groups | Literature synthesis in genotype-phenotype study | 2023 | DOI: 10.1002/jimd.12608 | https://doi.org/10.1002/jimd.12608 | Human literature synthesis | (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2) |
| Epidemiology | Estimated birth prevalence in Germany **1:135,000** | Heidelberg NBS program background | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program | (zaunseder2024digitaltierstrategyimproves pages 1-2) |
| Epidemiology | Incidence **1 in 63,948 newborns** | Fujian Province, China; **1,151,069** screened, **18** newborns diagnosed | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human NBS cohort | (zhou2023biochemicalandmolecular pages 1-2) |
| Disease burden/outcomes | Despite early treatment, **15–23%** of patients still experience encephalopathic crises | Review of treated early-diagnosed GA1 | 2023 | DOI: 10.3390/ijms241713158 | https://doi.org/10.3390/ijms241713158 | Review/outcomes summary | (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2) |
| Genetics | **421** distinct pathogenic **GCDH** variants identified; phenotypes aggregated from **532** patients | Large genotype-phenotype analysis | 2023 | DOI: 10.1002/jimd.12608 | https://doi.org/10.1002/jimd.12608 | Human literature synthesis/genetics | (schuurmans2023exploringgenotype–phenotypecorrelations pages 1-2) |
| Genetics | Variant databases listed **240** pathogenic variants in LOVD and **232** in ClinVar | Database-informed genotype review | 2023 | DOI: 10.1002/jimd.12608 | https://doi.org/10.1002/jimd.12608 | Human genetics/database synthesis | (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3) |
| Biochemical phenotype | High excretors (HE): urinary GA **>100 mmol/mol creatinine**; Low excretors (LE): **<100 mmol/mol creatinine** | Standard GA1 biochemical classification | 2023 | DOI: 10.1002/jimd.12608 | https://doi.org/10.1002/jimd.12608 | Human biochemical genetics | (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3) |
| Residual enzyme activity | HE usually associated with residual activity **0–2%** or **<5%**; LE with **3–30%** residual activity | Genotype-biochemistry correlations across reports | 2023 | DOI: 10.1002/jimd.12608; DOI: 10.3390/ijms241713158 | https://doi.org/10.1002/jimd.12608 ; https://doi.org/10.3390/ijms241713158 | Human genetics/mechanistic review | (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2) |
| Fujian molecular spectrum | **71** variants across **70 alleles**; **19** pathogenic variants identified | 35 unrelated GA1 patients from Fujian | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human cohort/genetics | (zhou2023biochemicalandmolecular pages 1-2) |
| Common variant frequency | **c.1244-2A>C** accounted for **63.38%** of alleles | Fujian cohort | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human cohort/genetics | (zhou2023biochemicalandmolecular pages 1-2) |
| Common variant frequency | **p.Ala421Thr (c.1261G>A)** accounted for **5.63%** of alleles | Fujian cohort | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human cohort/genetics | (zhou2023biochemicalandmolecular pages 1-2) |
| Common variant frequency | **p.Gly136Cys (c.406G>T)** accounted for **4.22%** of alleles | Fujian cohort | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human cohort/genetics | (zhou2023biochemicalandmolecular pages 1-2) |
| Common genotype | Homozygous **c.[1244-2A>C];[1244-2A>C]** in **18/35 (52.43%)** patients | Fujian cohort | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human cohort/genetics | (zhou2023biochemicalandmolecular pages 1-2) |
| Excretor distribution | **28 HE** and **5 LE** patients | Fujian cohort with urine GA classification | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human cohort/biochemical | (zhou2023biochemicalandmolecular pages 1-2) |
| NBS program size | Initial extraction **1,055,885** profiles; analytic dataset **1,025,953** profiles; **494** suspected GA1 after cleaning | Heidelberg NBS study | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program | (zaunseder2024digitaltierstrategyimproves pages 2-4) |
| NBS performance | Sensitivity **100%**, specificity **99.94%**, false-positive rate **0.06%**, PPV **1.5%** | Heidelberg GA1 NBS program (2014–2021) | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program | (zaunseder2024digitaltierstrategyimproves pages 2-4) |
| Fujian NBS performance | **265** screen-positive newborns; positivity **0.023%**; PPV **6.42% (17/265)** | Fujian NBS cohort | 2023 | DOI: 10.1186/s13023-023-02833-z | https://doi.org/10.1186/s13023-023-02833-z | Human NBS cohort | (zhou2023biochemicalandmolecular pages 1-2) |
| NBS sex effect | False positives: **326/485 (67%) male** vs **159/485 (33%) female**; confirmed GA1 **4 male / 5 female** | Heidelberg suspected-diagnosis set | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program | (zaunseder2024digitaltierstrategyimproves pages 5-7, zaunseder2024digitaltierstrategyimproves pages 4-5) |
| Screening biomarker levels | Mean Glut: GA1 **2.698 ± 1.548 µmol/L**; suspected-not-confirmed **0.526 ± 0.106 µmol/L**; normal **0.157 ± 0.057 µmol/L** | Heidelberg NBS metabolite distributions | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program/biomarker study | (zaunseder2024digitaltierstrategyimproves pages 5-7) |
| Excretor biomarker levels | Mean Glut in LE **1.9 ± 1.28 µmol/L (n=6)** vs HE **4.3 ± 0.2 µmol/L (n=3)** | Heidelberg confirmed GA1 cases | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program/biomarker study | (zaunseder2024digitaltierstrategyimproves pages 5-7) |
| Confirmatory follow-up | Urinary **3-OH-GA** excluded GA1 in **90% (435/485)** false positives; **7% (34/485)** had elevated urinary 3-OH-GA prompting more testing | Heidelberg follow-up after positive NBS | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS follow-up program | (zaunseder2024digitaltierstrategyimproves pages 5-7) |
| Digital-tier NBS improvement | False positives reduced from **235** to **16** on test set (**93.19% reduction**) with LR model trained on full dataset; **100% sensitivity** maintained | Heidelberg independent test set | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program/machine learning | (zaunseder2024newapproachesin pages 76-80, zaunseder2024digitaltierstrategyimproves pages 7-8, zaunseder2024digitaltierstrategyimproves media 0bbb340b) |
| Digital-tier NBS improvement | False positives reduced from **235** to **18** on test set (**92.34% reduction**) with LR model trained on suspected-diagnosis dataset; **100% sensitivity** maintained | Heidelberg independent test set | 2024 | DOI: 10.3390/ijns10040083 | https://doi.org/10.3390/ijns10040083 | NBS program/machine learning | (zaunseder2024digitaltierstrategyimproves pages 8-10, zaunseder2024digitaltierstrategyimproves pages 7-8, zaunseder2024digitaltierstrategyimproves media 0bbb340b) |
| Traditional vs digital-tier specificity | Traditional test-set screening: **0 FN**, **235 FP**, sensitivity **100%**, specificity **99.90%** | Heidelberg test set | 2024 | DOI: 10.11588/heidok.00035789 | https://doi.org/10.11588/heidok.00035789 | NBS program/modeling thesis | (zaunseder2024newapproachesin pages 76-80) |
| False-negative risk | NBS sensitivity reported as **93.3%** and specificity **99.42%** in a delayed-diagnosis report discussing missed cases | Case-based review of diagnostic performance | 2025 | DOI: 10.7759/cureus.86380 | https://doi.org/10.7759/cureus.86380 | Case report/review | (larancuent2025delayeddiagnosisof pages 5-7) |
| Low-excretor frequency | LE phenotype estimated in **30–40%** of GA1 patients | Diagnostic review/case report | 2025 | DOI: 10.7759/cureus.86380 | https://doi.org/10.7759/cureus.86380 | Case report/review | (larancuent2025delayeddiagnosisof pages 2-3) |
| AAV gene therapy | Untreated KO mice under HLD had **~60% death**; neonatal AAV-GCDH yielded **complete survival** after HLD challenge | Gcdh knockout mouse model | 2024 | DOI: 10.1016/j.omtm.2024.101276 | https://doi.org/10.1016/j.omtm.2024.101276 | Mouse model/gene therapy | (mateubosch2024systemicdeliveryof pages 1-2) |
| AAV biodistribution/transduction | Neonatal delivery produced **~40-fold** more striatal viral genomes at 1 month than later treatment | AAV9-GCDH in Gcdh knockout mice | 2024 | DOI: 10.1016/j.omtm.2024.101276 | https://doi.org/10.1016/j.omtm.2024.101276 | Mouse model/gene therapy | (mateubosch2024systemicdeliveryof pages 6-7) |
| AAV dosing | Systemic doses evaluated included about **7.5×10^12 vg/kg** up to **~5×10^13 vg/kg** | AAV9-GCDH preclinical optimization | 2024 | DOI: 10.1016/j.omtm.2024.101276 | https://doi.org/10.1016/j.omtm.2024.101276 | Mouse model/gene therapy | (mateubosch2024systemicdeliveryof pages 6-7) |
| Pharmacological chaperone discovery | Virtual screening of **~2.7 million** compounds yielded **~2,200** candidates; **94** compounds purchased for follow-up | SEE-Tx GCDH allosteric screen | 2024 | DOI: 10.1021/acs.jmedchem.4c00292 | https://doi.org/10.1021/acs.jmedchem.4c00292 | In vitro/computational drug discovery | (barroso2024useofthe pages 10-10) |
| Pharmacological chaperone discovery | Hit rate **>20%** in experimental validation | SEE-Tx GCDH chaperone campaign | 2024 | DOI: 10.1021/acs.jmedchem.4c00292 | https://doi.org/10.1021/acs.jmedchem.4c00292 | In vitro/computational drug discovery | (barroso2024useofthe pages 10-10) |
| Pharmacological chaperone potency | One lead bound GCDH with **Kd = 3.4 µM**; additional validated binders **6.9–44.9 µM** range reported for examples | SEE-Tx validated allosteric regulators | 2024 | DOI: 10.1021/acs.jmedchem.4c00292 | https://doi.org/10.1021/acs.jmedchem.4c00292 | In vitro/computational drug discovery | (barroso2024useofthe pages 9-10, barroso2024useofthe pages 2-3) |


*Table: This table compiles key quantitative findings for glutaric acidemia type 1, including epidemiology, newborn screening performance, variant frequencies, and emerging therapy results. It is designed as a quick-reference evidence summary for a disease knowledge base entry.*

---

## Visual evidence (newborn screening performance)
Table 2 from Zaunseder et al. (2024) provides the detailed sensitivity/specificity and false-positive reductions achieved by the digital-tier ML strategy (e.g., 235 → 16/18 false positives on the independent test set with maintained sensitivity), supporting the quantitative claims in Section 10. (zaunseder2024digitaltierstrategyimproves media 0bbb340b)

---

## Notes on evidence gaps (from current tool retrieval)
- MONDO/Orphanet/MeSH/ICD identifiers were not directly retrieved in the current evidence set and should be populated via dedicated ontology/database queries.
- No high-quality, GA1-specific 2023–2024 human interventional clinical trials were retrieved here; emerging therapies are currently supported primarily by preclinical studies and structure-guided discovery.
- QoL instrument data and formal differential diagnosis lists were not retrieved in the current evidence set.


References

1. (kolker2011diagnosisandmanagement pages 1-2): Stefan Kölker, Ernst Christensen, James V. Leonard, Cheryl R. Greenberg, Avihu Boneh, Alberto B. Burlina, Alessandro P. Burlina, Marjorie Dixon, Marinus Duran, Angels García Cazorla, Stephen I. Goodman, David M. Koeller, Mårten Kyllerman, Chris Mühlhausen, Edith Müller, Jürgen G. Okun, Bridget Wilcken, Georg F. Hoffmann, and Peter Burgard. Diagnosis and management of glutaric aciduria type i – revised recommendations. Journal of Inherited Metabolic Disease, 34:677-694, Mar 2011. URL: https://doi.org/10.1007/s10545-011-9289-5, doi:10.1007/s10545-011-9289-5. This article has 422 citations and is from a peer-reviewed journal.

2. (kolker2011diagnosisandmanagement pages 2-4): Stefan Kölker, Ernst Christensen, James V. Leonard, Cheryl R. Greenberg, Avihu Boneh, Alberto B. Burlina, Alessandro P. Burlina, Marjorie Dixon, Marinus Duran, Angels García Cazorla, Stephen I. Goodman, David M. Koeller, Mårten Kyllerman, Chris Mühlhausen, Edith Müller, Jürgen G. Okun, Bridget Wilcken, Georg F. Hoffmann, and Peter Burgard. Diagnosis and management of glutaric aciduria type i – revised recommendations. Journal of Inherited Metabolic Disease, 34:677-694, Mar 2011. URL: https://doi.org/10.1007/s10545-011-9289-5, doi:10.1007/s10545-011-9289-5. This article has 422 citations and is from a peer-reviewed journal.

3. (zhou2023biochemicalandmolecular pages 1-2): Jinfu Zhou, Guilin Li, Lin Deng, Peiran Zhao, Yinglin Zeng, Xiaolong Qiu, Jinying Luo, and Liangpu Xu. Biochemical and molecular features of chinese patients with glutaric acidemia type 1 from fujian province, southeastern china. Orphanet Journal of Rare Diseases, Jul 2023. URL: https://doi.org/10.1186/s13023-023-02833-z, doi:10.1186/s13023-023-02833-z. This article has 7 citations and is from a peer-reviewed journal.

4. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-2): Imke M. E. Schuurmans, Bianca Dimitrov, Julian Schröter, Antonia Ribes, Rubén Pérez de la Fuente, Berta Zamora, Clara D. M. van Karnebeek, Stefan Kölker, and Alejandro Garanto. Exploring genotype–phenotype correlations in glutaric aciduria type 1. Journal of Inherited Metabolic Disease, 46:371-390, Apr 2023. URL: https://doi.org/10.1002/jimd.12608, doi:10.1002/jimd.12608. This article has 26 citations and is from a peer-reviewed journal.

5. (schuurmans2023exploringgenotype–phenotypecorrelations pages 1-2): Imke M. E. Schuurmans, Bianca Dimitrov, Julian Schröter, Antonia Ribes, Rubén Pérez de la Fuente, Berta Zamora, Clara D. M. van Karnebeek, Stefan Kölker, and Alejandro Garanto. Exploring genotype–phenotype correlations in glutaric aciduria type 1. Journal of Inherited Metabolic Disease, 46:371-390, Apr 2023. URL: https://doi.org/10.1002/jimd.12608, doi:10.1002/jimd.12608. This article has 26 citations and is from a peer-reviewed journal.

6. (zaunseder2024digitaltierstrategyimproves pages 2-4): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

7. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2): Madalena Barroso, Marcus Gertzen, Alexandra F. Puchwein-Schwepcke, Heike Preisler, Andreas Sturm, Dunja D. Reiss, Marta K. Danecka, Ania C. Muntau, and Søren W. Gersting. Glutaryl-coa dehydrogenase misfolding in glutaric acidemia type 1. International Journal of Molecular Sciences, 24:13158, Aug 2023. URL: https://doi.org/10.3390/ijms241713158, doi:10.3390/ijms241713158. This article has 5 citations.

8. (mateubosch2024systemicdeliveryof pages 1-2): Anna Mateu-Bosch, Eulàlia Segur-Bailach, Emma Muñoz-Moreno, María José Barallobre, Maria Lourdes Arbonés, Sabrina Gea-Sorlí, Frederic Tort, Antonia Ribes, Judit García-Villoria, and Cristina Fillat. Systemic delivery of aav-gcdh ameliorates hld-induced phenotype in a glutaric aciduria type i mouse model. Molecular Therapy - Methods &amp; Clinical Development, 32:101276, Sep 2024. URL: https://doi.org/10.1016/j.omtm.2024.101276, doi:10.1016/j.omtm.2024.101276. This article has 10 citations.

9. (barroso2024useofthe pages 2-3): Madalena Barroso, Alexandra Puchwein-Schwepcke, Lars Buettner, Ingrid Goebel, Katrin Küchler, Ania C. Muntau, Aida Delgado, Ana M. Garcia-Collazo, Marc Martinell, Xavier Barril, Elena Cubero, and Søren W. Gersting. Use of the novel site-directed enzyme enhancement therapy (see-tx) drug discovery platform to identify pharmacological chaperones for glutaric acidemia type 1. Journal of Medicinal Chemistry, 67:17087-17100, Sep 2024. URL: https://doi.org/10.1021/acs.jmedchem.4c00292, doi:10.1021/acs.jmedchem.4c00292. This article has 4 citations and is from a highest quality peer-reviewed journal.

10. (gragnaniello2025diagnosisofglutaric pages 1-2): Vincenza Gragnaniello, Andrea Puma, Daniela Gueraldi, Ignazio D’Errico, Chiara Cazzorla, Christian Loro, Elena Porcù, Leonardo Salviati, and Alberto B. Burlina. Diagnosis of glutaric aciduria type i based on neuroradiological findings: when neonatal screening fails. Italian Journal of Pediatrics, May 2025. URL: https://doi.org/10.1186/s13052-025-01975-z, doi:10.1186/s13052-025-01975-z. This article has 0 citations and is from a peer-reviewed journal.

11. (larancuent2025delayeddiagnosisof pages 1-2): Cesar E. Larancuent, Tracey Weiler, and Sajel L. Kana. Delayed diagnosis of glutaric aciduria type 1: a case report. Cureus, Jun 2025. URL: https://doi.org/10.7759/cureus.86380, doi:10.7759/cureus.86380. This article has 0 citations.

12. (schuurmans2023exploringgenotype–phenotypecorrelations pages 2-3): Imke M. E. Schuurmans, Bianca Dimitrov, Julian Schröter, Antonia Ribes, Rubén Pérez de la Fuente, Berta Zamora, Clara D. M. van Karnebeek, Stefan Kölker, and Alejandro Garanto. Exploring genotype–phenotype correlations in glutaric aciduria type 1. Journal of Inherited Metabolic Disease, 46:371-390, Apr 2023. URL: https://doi.org/10.1002/jimd.12608, doi:10.1002/jimd.12608. This article has 26 citations and is from a peer-reviewed journal.

13. (kolker2011diagnosisandmanagement pages 4-5): Stefan Kölker, Ernst Christensen, James V. Leonard, Cheryl R. Greenberg, Avihu Boneh, Alberto B. Burlina, Alessandro P. Burlina, Marjorie Dixon, Marinus Duran, Angels García Cazorla, Stephen I. Goodman, David M. Koeller, Mårten Kyllerman, Chris Mühlhausen, Edith Müller, Jürgen G. Okun, Bridget Wilcken, Georg F. Hoffmann, and Peter Burgard. Diagnosis and management of glutaric aciduria type i – revised recommendations. Journal of Inherited Metabolic Disease, 34:677-694, Mar 2011. URL: https://doi.org/10.1007/s10545-011-9289-5, doi:10.1007/s10545-011-9289-5. This article has 422 citations and is from a peer-reviewed journal.

14. (kolker2011diagnosisandmanagement pages 9-10): Stefan Kölker, Ernst Christensen, James V. Leonard, Cheryl R. Greenberg, Avihu Boneh, Alberto B. Burlina, Alessandro P. Burlina, Marjorie Dixon, Marinus Duran, Angels García Cazorla, Stephen I. Goodman, David M. Koeller, Mårten Kyllerman, Chris Mühlhausen, Edith Müller, Jürgen G. Okun, Bridget Wilcken, Georg F. Hoffmann, and Peter Burgard. Diagnosis and management of glutaric aciduria type i – revised recommendations. Journal of Inherited Metabolic Disease, 34:677-694, Mar 2011. URL: https://doi.org/10.1007/s10545-011-9289-5, doi:10.1007/s10545-011-9289-5. This article has 422 citations and is from a peer-reviewed journal.

15. (patil2024glutaricaciduriapresenting pages 1-2): Manojkumar G Patil, Neha Tyagi, Om Prasanth Reddy Avuthu, and Shradha Salunkhe. Glutaric aciduria presenting with an acute encephalitic crisis: a case report. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.65722, doi:10.7759/cureus.65722. This article has 1 citations.

16. (kolker2011diagnosisandmanagement pages 10-12): Stefan Kölker, Ernst Christensen, James V. Leonard, Cheryl R. Greenberg, Avihu Boneh, Alberto B. Burlina, Alessandro P. Burlina, Marjorie Dixon, Marinus Duran, Angels García Cazorla, Stephen I. Goodman, David M. Koeller, Mårten Kyllerman, Chris Mühlhausen, Edith Müller, Jürgen G. Okun, Bridget Wilcken, Georg F. Hoffmann, and Peter Burgard. Diagnosis and management of glutaric aciduria type i – revised recommendations. Journal of Inherited Metabolic Disease, 34:677-694, Mar 2011. URL: https://doi.org/10.1007/s10545-011-9289-5, doi:10.1007/s10545-011-9289-5. This article has 422 citations and is from a peer-reviewed journal.

17. (zaunseder2024digitaltierstrategyimproves pages 1-2): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

18. (kolker2011diagnosisandmanagement pages 7-8): Stefan Kölker, Ernst Christensen, James V. Leonard, Cheryl R. Greenberg, Avihu Boneh, Alberto B. Burlina, Alessandro P. Burlina, Marjorie Dixon, Marinus Duran, Angels García Cazorla, Stephen I. Goodman, David M. Koeller, Mårten Kyllerman, Chris Mühlhausen, Edith Müller, Jürgen G. Okun, Bridget Wilcken, Georg F. Hoffmann, and Peter Burgard. Diagnosis and management of glutaric aciduria type i – revised recommendations. Journal of Inherited Metabolic Disease, 34:677-694, Mar 2011. URL: https://doi.org/10.1007/s10545-011-9289-5, doi:10.1007/s10545-011-9289-5. This article has 422 citations and is from a peer-reviewed journal.

19. (zaunseder2024digitaltierstrategyimproves pages 5-7): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

20. (zaunseder2024digitaltierstrategyimproves pages 7-8): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

21. (zaunseder2024digitaltierstrategyimproves media 0bbb340b): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

22. (kolker2011diagnosisandmanagement pages 8-9): Stefan Kölker, Ernst Christensen, James V. Leonard, Cheryl R. Greenberg, Avihu Boneh, Alberto B. Burlina, Alessandro P. Burlina, Marjorie Dixon, Marinus Duran, Angels García Cazorla, Stephen I. Goodman, David M. Koeller, Mårten Kyllerman, Chris Mühlhausen, Edith Müller, Jürgen G. Okun, Bridget Wilcken, Georg F. Hoffmann, and Peter Burgard. Diagnosis and management of glutaric aciduria type i – revised recommendations. Journal of Inherited Metabolic Disease, 34:677-694, Mar 2011. URL: https://doi.org/10.1007/s10545-011-9289-5, doi:10.1007/s10545-011-9289-5. This article has 422 citations and is from a peer-reviewed journal.

23. (barroso2024useofthe pages 10-10): Madalena Barroso, Alexandra Puchwein-Schwepcke, Lars Buettner, Ingrid Goebel, Katrin Küchler, Ania C. Muntau, Aida Delgado, Ana M. Garcia-Collazo, Marc Martinell, Xavier Barril, Elena Cubero, and Søren W. Gersting. Use of the novel site-directed enzyme enhancement therapy (see-tx) drug discovery platform to identify pharmacological chaperones for glutaric acidemia type 1. Journal of Medicinal Chemistry, 67:17087-17100, Sep 2024. URL: https://doi.org/10.1021/acs.jmedchem.4c00292, doi:10.1021/acs.jmedchem.4c00292. This article has 4 citations and is from a highest quality peer-reviewed journal.

24. (mateubosch2024systemicdeliveryof pages 6-7): Anna Mateu-Bosch, Eulàlia Segur-Bailach, Emma Muñoz-Moreno, María José Barallobre, Maria Lourdes Arbonés, Sabrina Gea-Sorlí, Frederic Tort, Antonia Ribes, Judit García-Villoria, and Cristina Fillat. Systemic delivery of aav-gcdh ameliorates hld-induced phenotype in a glutaric aciduria type i mouse model. Molecular Therapy - Methods &amp; Clinical Development, 32:101276, Sep 2024. URL: https://doi.org/10.1016/j.omtm.2024.101276, doi:10.1016/j.omtm.2024.101276. This article has 10 citations.

25. (zaunseder2024digitaltierstrategyimproves pages 4-5): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

26. (zaunseder2024newapproachesin pages 76-80): Elaine Serena Zaunseder. New approaches in mathematical and data-based modeling for newborn screening. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00035789, doi:10.11588/heidok.00035789. This article has 0 citations and is from a peer-reviewed journal.

27. (zaunseder2024digitaltierstrategyimproves pages 8-10): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

28. (larancuent2025delayeddiagnosisof pages 5-7): Cesar E. Larancuent, Tracey Weiler, and Sajel L. Kana. Delayed diagnosis of glutaric aciduria type 1: a case report. Cureus, Jun 2025. URL: https://doi.org/10.7759/cureus.86380, doi:10.7759/cureus.86380. This article has 0 citations.

29. (larancuent2025delayeddiagnosisof pages 2-3): Cesar E. Larancuent, Tracey Weiler, and Sajel L. Kana. Delayed diagnosis of glutaric aciduria type 1: a case report. Cureus, Jun 2025. URL: https://doi.org/10.7759/cureus.86380, doi:10.7759/cureus.86380. This article has 0 citations.

30. (barroso2024useofthe pages 9-10): Madalena Barroso, Alexandra Puchwein-Schwepcke, Lars Buettner, Ingrid Goebel, Katrin Küchler, Ania C. Muntau, Aida Delgado, Ana M. Garcia-Collazo, Marc Martinell, Xavier Barril, Elena Cubero, and Søren W. Gersting. Use of the novel site-directed enzyme enhancement therapy (see-tx) drug discovery platform to identify pharmacological chaperones for glutaric acidemia type 1. Journal of Medicinal Chemistry, 67:17087-17100, Sep 2024. URL: https://doi.org/10.1021/acs.jmedchem.4c00292, doi:10.1021/acs.jmedchem.4c00292. This article has 4 citations and is from a highest quality peer-reviewed journal.
