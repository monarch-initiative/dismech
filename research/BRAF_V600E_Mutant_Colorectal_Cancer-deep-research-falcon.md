---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T12:47:00.929348'
end_time: '2026-04-05T12:58:20.303469'
duration_seconds: 679.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRAF V600E-Mutant Colorectal Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 60
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRAF V600E-Mutant Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600E-Mutant Colorectal Cancer** covering all of the
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
- **Disease Name:** BRAF V600E-Mutant Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600E-Mutant Colorectal Cancer** covering all of the
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


## Comprehensive Research Report: BRAF V600E–Mutant Colorectal Cancer

### Target Disease
- **Disease name:** BRAF V600E–Mutant Colorectal Cancer
- **MONDO ID:** not found in retrieved sources
- **Category:** Molecularly defined subtype of colorectal cancer (typically colorectal adenocarcinoma) driven by somatic activating BRAF p.Val600Glu.

### Evidence base and scope
This report is derived from aggregated evidence including phase III randomized trials, phase II trials, translational multi-omics profiling, real-world cohorts (EHR/registry-derived), ClinicalTrials.gov registrations, and recent reviews (prioritizing 2023–2024 where available). (zurloh2023impactofencorafenib pages 1-2, kopetz2024molecularprofilingof pages 1-2, NCT06578559 chunk 1)


## 1. Disease Information

### 1.1 Overview (what is the disease?)
BRAF V600E–mutant colorectal cancer denotes colorectal cancer characterized by an activating missense substitution in **BRAF** (valine→glutamic acid at codon 600), which constitutively activates MAPK signaling and defines a clinically distinct subgroup with poor prognosis in metastatic disease. (morris2020improvementsinclinical pages 1-5)

A clear trial-level description from BEACON CRC highlights the clinical context and biological rationale:
- “**Patients with metastatic colorectal cancer with the BRAF V600E mutation have a poor prognosis** …” and “**Inhibition of BRAF alone has limited activity because of pathway reactivation through epidermal growth factor receptor signaling**.” (kopetz2019encorafenibbinimetiniband pages 1-2)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
- **MONDO / MeSH / ICD-10 / ICD-11 / OMIM / Orphanet:** not found in retrieved sources (in practice, coded as CRC with biomarker annotation rather than a unique ICD code). (morris2020improvementsinclinical pages 1-5)

### 1.3 Common synonyms / alternative names
- “BRAFV600E-mutant metastatic colorectal cancer (mCRC)” (kopetz2019encorafenibbinimetiniband pages 1-2)
- “BRAFV600E-mutated colorectal cancer” (cutsem2023anchorcrcresults pages 1-2)
- “BRAF V600E mutated mCRC” (eriksen2022aphaseii pages 1-2)

### 1.4 Patient-level vs aggregated resources
Most evidence is aggregated from trials and cohorts. Real-world cohorts explicitly use EHR extraction (e.g., clinicopathologic data extracted from electronic records). (zurloh2023impactofencorafenib pages 1-2)


## 2. Etiology

### 2.1 Disease causal factors
- **Genetic/mechanistic:** Somatic activating **BRAF p.V600E** is the defining causal driver alteration; BRAF is a serine/threonine kinase in the EGFR–RAS–RAF–MEK–ERK (MAPK) cascade. (morris2020improvementsinclinical pages 1-5, potocki2023clinicalcharacterizationof pages 1-2)
- **Pathway association:** BRAF-mutant CRC is strongly linked to the serrated neoplasia pathway and to epigenetic phenotypes including **CIMP** and often **MSI/dMMR** in sporadic cases. (guerrero2023brafinhibitorsin pages 1-2, effendiys2024biomarkersasa pages 3-6)

### 2.2 Risk factors
#### 2.2.1 Genetic risk factors
- **Subtype context:** Sporadic MSI tumors show marked enrichment for BRAF mutations (review-level): “**observed in 60% of MSI tumors vs 5–10% of MSS tumors**,” and “**about 20% of patients with mutated BRAF V600E concurrently exhibit microsatellite instability**.” (guerrero2023brafinhibitorsin pages 1-2)

#### 2.2.2 Environmental / lifestyle risk factors (molecular-subtype specific)
A 2024 Mendelian randomization analysis provides subtype-specific causal evidence linking adiposity to BRAF-mutated/CIMP-high pathways:
- Per 1-SD (5.1 kg/m²) higher BMI, risk increased for:
  - **Jass type 1** (MSI-high, CIMP-high, BRAF-mutated, KRAS-wildtype): **OR 2.14** (95% CI 1.46–3.13)
  - **Jass type 2** (non–MSI-high, CIMP-high, BRAF-mutated, KRAS-wildtype): **OR 2.20** (95% CI 1.26–3.86) (papadimitriou2024bodysizeand pages 1-2)

High-fat diet is repeatedly framed as a CRC risk context in preclinical literature, including in BRAF-driven mouse-model work (see Section 13 and 15). (theofanous2024exploringtheprotective pages 69-72, theofanous2024exploringtheprotective pages 1-5)

### 2.3 Protective factors
Evidence directly specific to BRAF V600E CRC prevention in humans is limited in retrieved sources. The retrieved evidence includes preclinical and limited human biomarker signals for dietary compounds:
- In APCMIN/+ mice on high-fat diet, **resveratrol** reduced “intestinal adenoma number and tumour burden by ~40% and ~57%” at low dose in one study summarized in the thesis review table. (theofanous2024exploringtheprotective pages 69-72)
- In a small human CRC/metastasis context referenced by the same thesis, resveratrol interventions were associated with biomarker changes such as “cleaved caspase 3 … 39%” in hepatic metastases and a “5% reduction in Ki67 proliferation” (short-term, small n). (theofanous2024exploringtheprotective pages 69-72)

### 2.4 Gene–environment interactions
A BRAF V600E-driven mouse model in the resveratrol/HFD work showed genotype-dependent response to dietary fat exposure (interaction leading to rapid weight loss and early culling before polyp development), indicating that BRAF-driven physiology may modulate diet response in vivo. (theofanous2024exploringtheprotective pages 69-72)


## 3. Phenotypes

### 3.1 Clinicopathologic phenotype (common patterns)
A large 2023 nationwide advanced CRC cohort (n=7,604) found BRAF V600E is enriched in multiple clinicopathologic settings:
- Female sex (OR 2.009)
- Right/proximal colon primary (OR 8.356)
- High-grade tumors (OR 4.061)
- Mucinous histology (OR 3.430) and partially mucinous (OR 2.718)
- Signet cell features (OR 1.544)
- Mixed adeno-neuroendocrine cancers (MANEC; OR 9.211)
- Vascular and perineural invasion (potocki2023clinicalcharacterizationof pages 4-5)

In real-world clinical description, BRAF V600E mCRC is also described as more often right-sided, more common in female patients, and associated with MSI-high features. (zurloh2023impactofencorafenib pages 1-2)

### 3.2 Symptom/sign phenotype
Symptoms generally reflect colorectal cancer and metastatic spread; the retrieved corpus did not provide quantitative symptom frequencies specific to BRAF V600E subtype.

### 3.3 Suggested HPO terms (examples)
Because the retrieved evidence emphasizes pathology and metastatic patterns more than symptom inventories, HPO suggestions are necessarily generic for CRC/mCRC:
- **Abdominal pain** (HP:0002027)
- **Hematochezia** (HP:0001892)
- **Weight loss** (HP:0001824)
- **Anemia** (HP:0001903)
- **Metastatic neoplasm** (HP:0003002)

(Phenotype frequency data not available in retrieved sources.)

### 3.4 Quality-of-life impact
A review notes BRAF V600E CRC is linked to worse HRQoL compared with BRAF-wildtype CRC, but quantitative QoL instrument values were not available in retrieved excerpts. (morris2020improvementsinclinical pages 1-5)


## 4. Genetic/Molecular Information

### 4.1 Causal genes
- **BRAF** (B-RAF proto-oncogene, serine/threonine kinase) is the defining driver gene in this subtype. (morris2020improvementsinclinical pages 1-5, potocki2023clinicalcharacterizationof pages 1-2)

### 4.2 Pathogenic variants
- **BRAF p.Val600Glu (V600E)**: activating substitution at residue 600, constitutive MAPK pathway activation. (morris2020improvementsinclinical pages 1-5)

**Somatic vs germline:** In CRC, BRAF V600E is typically treated as a somatic tumor driver; it is also used clinically to help exclude Lynch syndrome when MSI-H is present (see Diagnostics). (effendiys2024biomarkersasa pages 3-6, iliepetrov2024…ofcolorectal pages 7-9)

### 4.3 Modifier/co-alterations and resistance alterations
The 2024 BEACON CRC multi-omics biomarker analysis identified acquired resistance alterations:
- “**RAS, MAP2K1 and MET alterations were most commonly acquired**” on encorafenib+cetuximab±binimetinib. (kopetz2024molecularprofilingof pages 1-2)
- “**baseline TP53 mutation was associated with acquired MET amplification**.” (kopetz2024molecularprofilingof pages 1-2)

### 4.4 Epigenetics
BRAF-mutant CRC is linked to CIMP biology (hypermethylation phenotype), often aligned with serrated pathway development. (guerrero2023brafinhibitorsin pages 1-2, effendiys2024biomarkersasa pages 3-6)


## 5. Environmental Information

### 5.1 Environmental/lifestyle factors
- **Obesity/body size:** causal MR support for higher BMI increasing risk of BRAF-mutated/CIMP-high pathway CRC subtypes (see Etiology). (papadimitriou2024bodysizeand pages 1-2)
- **Dietary fat/high-fat diet:** discussed as CRC risk context and experimentally interrogated in BRAF-driven mouse models. (theofanous2024exploringtheprotective pages 69-72, theofanous2024exploringtheprotective pages 1-5)

### 5.2 Infectious agents
No infectious agents specific to BRAF V600E CRC were identified in retrieved sources.


## 6. Mechanism / Pathophysiology

### 6.1 Core pathway: EGFR–RAS–RAF–MEK–ERK (MAPK)
BRAF V600E acts downstream of EGFR and RAS to drive MAPK signaling, increasing proliferation and reducing apoptosis. (morris2020improvementsinclinical pages 1-5)

### 6.2 Why BRAF inhibitor monotherapy fails in CRC (EGFR feedback)
The dominant mechanistic concept guiding therapy is **EGFR-mediated MAPK pathway reactivation** after BRAF inhibition:
- BEACON CRC (NEJM): “**Inhibition of BRAF alone has limited activity because of pathway reactivation through epidermal growth factor receptor signaling.**” (kopetz2019encorafenibbinimetiniband pages 1-2)
- BEACON updated analysis (JCO): “**BRAF inhibition results in a rapid release of feedback-suppressed epidermal growth-factor receptor (EGFR)–mediated MAPK signaling, leading to a rebound in MAPK activation and continued cell proliferation.**” (tabernero2021encorafenibpluscetuximab pages 1-2)

**Causal chain (simplified):**
1) BRAF V600E → constitutive ERK signaling → malignant growth (morris2020improvementsinclinical pages 1-5)
2) BRAF inhibitor alone ↓ ERK transiently → releases feedback suppression → EGFR activation → RAS signaling → RAF dimerization/reactivation → restored ERK signaling → resistance (tabernero2021encorafenibpluscetuximab pages 1-2, morris2020improvementsinclinical pages 11-14)
3) Combine **BRAF + EGFR (±MEK)** inhibition → deeper pathway suppression and improved outcomes (kopetz2019encorafenibbinimetiniband pages 1-2, tabernero2021encorafenibpluscetuximab pages 1-2)

### 6.3 MSI/dMMR and immunobiology
BRAF mutations are enriched in sporadic MSI tumors and ~20% of BRAF V600E mCRC may be MSI, a key determinant of checkpoint inhibitor sensitivity. (guerrero2023brafinhibitorsin pages 1-2, effendiys2024biomarkersasa pages 3-6)

### 6.4 Suggested ontology terms
**GO Biological Process (suggestions):**
- MAPK cascade (GO:0000165)
- ERK1 and ERK2 cascade (GO:0070371)
- Regulation of cell proliferation (GO:0042127)
- Negative regulation of apoptotic process (GO:0043066)
- Epithelial cell proliferation (GO:0050673)

**CL Cell Ontology (suggestions):**
- Colonic epithelial cell / intestinal epithelial cell (CL:0000584 may map to enterocyte; general epithelial cell CL:0000066)
- Colonic stem cell (broadly: intestinal stem cell)
- Tumor-associated macrophage (for microenvironment studies; not directly evidenced in retrieved BRAF-specific excerpts)

**UBERON (suggestions):**
- Colon (UBERON:0001155)
- Large intestine (UBERON:0000059)


## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- Primary: colon/colorectum (UBERON:0001155 / UBERON:0000059) (general CRC context)
- Metastatic patterns may include peritoneal, bone, and brain involvement (review-level), though frequencies were not in retrieved excerpts. (morris2020improvementsinclinical pages 1-5)

### 7.2 Cell/subcellular
- Primary cell population: colonic epithelial tumor cells
- Key signaling compartment: cytoplasmic kinase signaling and nuclear transcriptional outputs downstream of ERK


## 8. Temporal Development

### 8.1 Onset
CRC is generally adult-onset. Early-onset CRC shows lower prevalence of BRAF mutations overall than late-onset CRC (not BRAF V600E-specific prevalence): OR 0.63 (0.51–0.78). (lawler2024thehistologicaland pages 1-2)

### 8.2 Progression
BRAF V600E mCRC is described as rapidly progressive with poor outcomes on historical standard therapies. (kopetz2019encorafenibbinimetiniband pages 1-2, morris2020improvementsinclinical pages 1-5)


## 9. Inheritance and Population

### 9.1 Epidemiology
- Prevalence of BRAF V600E in advanced CRC: **6.77%** in a nationwide cohort of 7,604 advanced CRC patients tested in one laboratory (Oct 2017–Dec 2019). (potocki2023clinicalcharacterizationof pages 1-2)
- Trial/review estimates: ~10–15% in metastatic CRC. (cutsem2023anchorcrcresults pages 1-2)

### 9.2 Inheritance
This is predominantly a **somatic tumor genotype** rather than a Mendelian inherited disease entity in standard oncology usage.

### 9.3 Demographics
- Enrichment in **female** patients and **right-sided** primaries is strongly supported by the 2023 nationwide cohort (ORs above). (potocki2023clinicalcharacterizationof pages 4-5)


## 10. Diagnostics

### 10.1 Core biomarker tests and workflows
A practical, widely used workflow in metastatic CRC includes: extended RAS testing (KRAS/NRAS), BRAF testing, and MSI/MMR status assessment. (effendiys2024biomarkersasa pages 3-6, NCT05217446 chunk 1)

**Assay modalities supported in retrieved sources:**
- **MMR/MSI:** Immunohistochemistry (IHC) for MMR proteins and PCR for MSI are explicitly discussed as standard approaches in a 2024 biomarker overview. (effendiys2024biomarkersasa pages 3-6)
- **BRAF testing:** typically performed on tumor tissue; can be done alongside RAS. (effendiys2024biomarkersasa pages 3-6)
- **NGS panels:** highlighted for comprehensive detection including atypical/non-V600 BRAF variants. (iliepetrov2024…ofcolorectal pages 7-9)

### 10.2 Lynch syndrome exclusion / differential
- BRAF V600E in MSI-H CRC is commonly used to help exclude Lynch syndrome in sporadic MSI-H disease in diagnostic algorithms (review-level and diagnostic discussion). (effendiys2024biomarkersasa pages 3-6, iliepetrov2024…ofcolorectal pages 7-9)

### 10.3 Liquid biopsy / ctDNA implementation
Clinical trial registrations and protocols show ctDNA is being used both for enrollment and for resistance-guided retreatment decisions:
- NCT05217446 allows BRAF confirmation from “**tumor tissue or blood**” (implying ctDNA accepted) with mandatory local MSI-H/dMMR confirmation and known RAS status. (NCT05217446 chunk 1)
- NCT06578559 (BRICKET) requires ctDNA at entry showing **no KRAS/NRAS/MAP2K1 mutations and no MET amplification** before encorafenib+cetuximab rechallenge. (NCT06578559 chunk 1)


## 11. Outcome / Prognosis

### 11.1 Natural history / poor prognosis
BEACON CRC provides a trial-level summary of poor prognosis after initial therapy failure:
- “**median overall survival of 4 to 6 months after failure of initial therapy**” in BRAF V600E mCRC (historical context). (kopetz2019encorafenibbinimetiniband pages 1-2)

### 11.2 Survival statistics from recent cohorts
- Real-world cohort (Germany, 2023; n=51): median OS 17.6 months overall; targeted therapy in later lines associated with OS 25.1 months in those receiving a BRAF inhibitor. (zurloh2023impactofencorafenib pages 1-2)
- Multi-center real-world propensity-matched study (2024; n=125): median OS 14.9 months; triplet chemotherapy+bevacizumab OS 17.4 vs 13.4 months pre-PSM and 17.4 vs 10.4 months post-PSM. (wei2024clinicopathologicfeaturesand pages 10-10)

### 11.3 Prognostic factors
In a 2024 multi-center study, poor differentiation and liver metastases were negative independent prognostic factors for OS in BRAF V600E mCRC. (wei2024clinicopathologicfeaturesand pages 10-10)


## 12. Treatment

### 12.1 Targeted therapy standard of care: Encorafenib + cetuximab (post–first line)
**BEACON CRC** established BRAF+EGFR targeted therapy as standard after prior therapy.

**Phase III BEACON CRC (interim analysis; NEJM 2019):**
- Mechanistic abstract quote: “**Inhibition of BRAF alone has limited activity because of pathway reactivation through epidermal growth factor receptor signaling.**” (kopetz2019encorafenibbinimetiniband pages 1-2)
- Outcomes:
  - Triplet (encorafenib+binimetinib+cetuximab): median OS **9.0** vs control **5.4** months (HR 0.52)
  - Confirmed ORR **26%** vs **2%**
  - Grade ≥3 AEs: 58% (triplet), 50% (doublet), 61% (control) (kopetz2019encorafenibbinimetiniband pages 1-2)

**Updated BEACON CRC analysis (JCO 2021):**
- OS: **9.3 months** (triplet) and **9.3 months** (doublet) vs **5.9** months (control)
- ORR: **26.8%** (triplet), **19.5%** (doublet), **1.8%** (control)
- Grade ≥3 AEs: **65.8%** (triplet), **57.4%** (doublet), **64.2%** (control) (tabernero2021encorafenibpluscetuximab pages 1-2)

These outcomes are also supported visually by the BEACON updated OS Kaplan–Meier and response table (tabernero2021encorafenibpluscetuximab media 2b387ba4, tabernero2021encorafenibpluscetuximab media 9dac50ff).

**MAXO suggestions:**
- EGFR inhibitor therapy (cetuximab)
- BRAF inhibitor therapy (encorafenib)
- MEK inhibitor therapy (binimetinib)

### 12.2 First-line targeted therapy strategies (emerging/2023–2025)
**ANCHOR CRC phase II (JCO 2023; first-line triplet, single-arm):**
- cORR **47.4%** (95% CI 37.0–57.9)
- median PFS **5.8** months
- median OS **18.3** months (cutsem2023anchorcrcresults pages 1-2)

**BREAKWATER phase III (Nature Medicine 2025; first interim, first-line EC+mFOLFOX6):**
- ORR **60.9%** vs SOC **40.0%**
- OS HR **0.47** (interim)
- Serious AEs **37.7%** vs **34.6%** (kopetz2025encorafenibcetuximaband pages 1-2)

### 12.3 Safety lead-in evidence (BEACON)
**BEACON safety lead-in (JCO 2019):**
- ORR **48%**; median PFS **8.0** months; median OS **15.3** months (cutsem2019binimetinibencorafeniband pages 1-2)
- DLTs included serous retinopathy, decreased LVEF, infusion reactions; common grade 3–4 AEs included fatigue (13%), anemia (10%), ↑CPK (10%), ↑AST (10%), UTI (10%). (cutsem2019binimetinibencorafeniband pages 1-2)

### 12.4 Immunotherapy
The retrieved evidence emphasizes that MSI-H/dMMR status is a key selection biomarker for PD-1 blockade in metastatic CRC, including in BRAF-mutant disease. (eriksen2022aphaseii pages 1-2)

A key real-world implementation example is an ongoing/registered trial:
- NCT05217446 compares **encorafenib+cetuximab+pembrolizumab** vs pembrolizumab alone in untreated MSI-H/dMMR, BRAF V600E mCRC, permitting BRAF confirmation by tissue or blood. (NCT05217446 chunk 1)

### 12.5 Resistance and sequencing
The 2024 BEACON translational analysis supports surveillance of resistance mechanisms and suggests biologically plausible targets (RAS/MAP2K1/MET) for next-line strategies. (kopetz2024molecularprofilingof pages 1-2)

A direct implementation of resistance-informed strategy is the ctDNA-guided rechallenge trial NCT06578559 excluding ctDNA-detectable RAS/MAP2K1/MET alterations at retreatment entry. (NCT06578559 chunk 1)


## 13. Prevention

### 13.1 Primary prevention
BRAF V600E is a tumor genotype rather than a preventable infectious etiology. However, CRC primary prevention strategies likely apply and are supported by subtype-specific evidence that **obesity is causally linked to BRAF-mutated/CIMP-high pathways** (targeting BMI reduction as a plausible primary prevention lever). (papadimitriou2024bodysizeand pages 1-2)

### 13.2 Secondary prevention (screening/early detection)
CRC screening strategies (colonoscopy, stool-based tests) are not detailed in the retrieved excerpts, but MSI/MMR and BRAF testing are emphasized once CRC is diagnosed, particularly for Lynch syndrome triage and systemic therapy selection. (effendiys2024biomarkersasa pages 3-6, iliepetrov2024…ofcolorectal pages 7-9)

### 13.3 Tertiary prevention
In metastatic disease, tertiary prevention focuses on preventing progression/complications via effective systemic therapy and molecularly guided sequencing (e.g., BEACON regimen, ctDNA monitoring trials). (tabernero2021encorafenibpluscetuximab pages 1-2, NCT06578559 chunk 1)


## 14. Other Species / Natural Disease

No naturally occurring non-human species disease analogs specific to BRAF V600E CRC were identified in the retrieved sources.


## 15. Model Organisms and Experimental Systems

### 15.1 Mouse models (BRAF-driven CRC and diet interactions)
A 2024 BRAF V600E-driven CRC mouse-model study/thesis explored high-fat diet effects and resveratrol modulation, including multi-omics phenotyping (microbiome, metabolomics, cytokines) and intestinal lipid biology. (theofanous2024exploringtheprotective pages 1-5)

Quantitative preclinical “prevention-like” effects summarized in that thesis include resveratrol reducing adenoma number/tumor burden in APCMIN/+ mice on high-fat diet by ~40% and ~57% at a low dose in one study table. (theofanous2024exploringtheprotective pages 69-72)

### 15.2 Patient-derived organoids (PDOs) and living biobanks
Organoids are emphasized as clinically relevant models for CRC heterogeneity and treatment response:
- Ex vivo organoid review (Cancers 2024) notes organoids preserve tumor heterogeneity and explicitly mentions “**models with high microsatellite instability associated with BRAF V600E mutations**,” and positions living biobanks for personalized treatment testing. (randalldemllo2024exvivointestinal pages 4-6)
- EGFR-targeting review (IJMS 2024) describes organoids as reflecting “genetic heterogeneity” and being used to study resistance to anti-EGFR therapies in personalized medicine contexts. (tardito2024epidermalgrowthfactor pages 1-2)

### 15.3 PDX models for drug response (EGFR therapy)
A 2024 Nature Communications study underscores PDX value for studying cetuximab sensitivity:
- PDXs are “**tumour fragments engrafted into mice**” and retain “structural complexity, heterogeneity, and stromal interactions” better than in vitro models; 231 CRC PDXs were profiled and screened for cetuximab response to train a predictive multi-omics model. (perron2024integrativeensemblemodelling pages 1-2)

### 15.4 Model limitations (expert synthesis from authoritative reviews)
- Organoids lack full tumor microenvironment and pharmacokinetics/ADME; PDX provides in vivo context but is lower throughput and costly. (randalldemllo2024exvivointestinal pages 4-6)


## Current applications and real-world implementations (2023–2024 emphasis)
1) **Routine molecular profiling** in metastatic CRC including RAS/BRAF and MSI/MMR to guide therapy selection and exclude ineffective anti-EGFR monotherapy in inappropriate genotypes. (effendiys2024biomarkersasa pages 3-6, NCT05217446 chunk 1)
2) **Approved targeted standard** after prior therapy: encorafenib + cetuximab (BEACON-established). (tabernero2021encorafenibpluscetuximab pages 1-2)
3) **First-line intensification and targeted combinations** in clinical trials (ANCHOR CRC; BREAKWATER). (cutsem2023anchorcrcresults pages 1-2, kopetz2025encorafenibcetuximaband pages 1-2)
4) **ctDNA integration** for resistance-guided rechallenge (BRICKET, NCT06578559). (NCT06578559 chunk 1)
5) **Organoid and PDX platforms** for drug-response prediction and resistance studies, supporting precision medicine pipelines. (randalldemllo2024exvivointestinal pages 4-6, perron2024integrativeensemblemodelling pages 1-2, tardito2024epidermalgrowthfactor pages 1-2)


## Relevant statistics and data highlights
- Prevalence of BRAF V600E in advanced CRC: 6.77% in 7,604-patient cohort (2023 report). (potocki2023clinicalcharacterizationof pages 1-2)
- Clinicopathologic enrichment: OR 8.356 for right-sided primaries; OR 4.061 high grade; OR 3.430 mucinous; OR 9.211 MANEC/neuroendocrine component. (potocki2023clinicalcharacterizationof pages 4-5)
- BEACON updated OS and ORR: OS 9.3 vs 5.9 months; ORR 19.5% (doublet) and 26.8% (triplet) vs 1.8% control. (tabernero2021encorafenibpluscetuximab pages 1-2)
- BMI causal association with BRAF-mutated/CIMP-high subtypes: OR ~2.1–2.2 per 1-SD higher BMI. (papadimitriou2024bodysizeand pages 1-2)


## Synthesis tables and visual evidence
The table below consolidates identifiers, epidemiology/phenotype, and core clinical trial outcomes.

| Section | Item | Details | Study (year, journal) | Population/setting | Regimen | Key outcomes (OS/PFS/ORR, grade≥3 AEs) | URL |
|---|---|---|---|---|---|---|---|
| Disease identifiers / classification | Disease name | BRAF V600E–mutant colorectal cancer; molecular subtype of colorectal adenocarcinoma defined by activating BRAF p.Val600Glu alteration in the MAPK pathway (morris2020improvementsinclinical pages 1-5, potocki2023clinicalcharacterizationof pages 1-2) | Morris 2020, *Clin Cancer Res*; Potocki 2023, *Int J Mol Sci* | CRC / advanced CRC | — | BRAF V600E occurs in ~10% of CRC overall; 6.77% in one nationwide advanced CRC cohort (morris2020improvementsinclinical pages 1-5, potocki2023clinicalcharacterizationof pages 1-2) | https://doi.org/10.1158/1078-0432.CCR-19-3809 ; https://doi.org/10.3390/ijms24109073 |
| Disease identifiers / classification | Synonyms | BRAFV600E-mutant CRC; BRAFV600E-mutated metastatic colorectal cancer (mCRC); BRAF V600E colorectal cancer (morris2020improvementsinclinical pages 1-5, kopetz2019encorafenibbinimetiniband pages 1-2) | Morris 2020, *Clin Cancer Res*; Kopetz 2019, *N Engl J Med* | CRC / mCRC | — | Widely used trial terminology; specific ontology IDs not found in retrieved sources | https://doi.org/10.1158/1078-0432.CCR-19-3809 ; https://doi.org/10.1056/NEJMoa1908075 |
| Disease identifiers / classification | Key identifiers | MONDO: not found in retrieved sources; OMIM: not found in retrieved sources; Orphanet: not found in retrieved sources; MeSH: not found in retrieved sources; ICD-10/11: not found in retrieved sources (use disease-level CRC codes plus biomarker annotation in practice) | not found in retrieved sources | Disease knowledge-base metadata | — | not found in retrieved sources | not found in retrieved sources |
| Disease identifiers / classification | Resource level | Information in retrieved sources is primarily aggregated disease-level evidence from clinical trials, cohort studies, reviews, and trial registries; some real-world studies derive data from EHR/registry cohorts (zurloh2023impactofencorafenib pages 1-2, NCT06578559 chunk 1) | Zurloh 2023, *J Cancer Res Clin Oncol*; ClinicalTrials.gov 2024 | Real-world cohorts / clinical trials | — | Aggregated disease-level resources; not patient-identifiable | https://doi.org/10.1007/s00432-023-05141-y ; https://clinicaltrials.gov/study/NCT06578559 |
| Epidemiology & phenotype | Prevalence | BRAF V600E prevalence 6.77% in 7,604 advanced CRC patients; review sources cite ~10% of CRC and ~10–15% of mCRC; some reviews cite ~12% of mCRC (potocki2023clinicalcharacterizationof pages 1-2, cutsem2023anchorcrcresults pages 1-2, guerrero2023brafinhibitorsin pages 1-2) | Potocki 2023, *Int J Mol Sci*; Van Cutsem 2023, *J Clin Oncol*; Guerrero 2023, *Cancers* | Advanced CRC / mCRC | — | 6.77% in nationwide advanced CRC cohort; ~10–15% across trial/review sources | https://doi.org/10.3390/ijms24109073 ; https://doi.org/10.1200/JCO.22.01693 ; https://doi.org/10.3390/cancers15215243 |
| Epidemiology & phenotype | Clinicopathologic enrichment | Enriched in female sex, right/proximal colon, high-grade tumors, mucinous and signet-ring histology, partially neuroendocrine histology, perineural and vascular invasion (potocki2023clinicalcharacterizationof pages 4-5, potocki2023clinicalcharacterizationof pages 1-2) | Potocki 2023, *Int J Mol Sci* | Nationwide retrospective advanced CRC cohort | — | OR female sex 2.009; OR right-sided primary 8.356; OR high-grade 4.061; OR mucinous 3.430; OR partial mucinous 2.718; OR signet cells 1.544; OR MANEC/neuroendocrine component 9.211 (potocki2023clinicalcharacterizationof pages 4-5) | https://doi.org/10.3390/ijms24109073 |
| Epidemiology & phenotype | MSI/CIMP/serrated pathway | Strong association with serrated neoplasia pathway, CIMP-high biology, and MSI enrichment in sporadic CRC; review notes BRAF mutations in ~60% of MSI tumors vs 5–10% of MSS tumors, and ~20% of BRAF V600E-mutant mCRC may be MSI (guerrero2023brafinhibitorsin pages 1-2, effendiys2024biomarkersasa pages 3-6) | Guerrero 2023, *Cancers*; Effendi-YS 2024, book chapter | Review / biomarker overview | — | Distinct biology with MSI/CIMP enrichment; clinically relevant for immunotherapy selection and Lynch syndrome exclusion workup | https://doi.org/10.3390/cancers15215243 ; https://doi.org/10.5772/intechopen.1004189 |
| Epidemiology & phenotype | Prognosis | Adverse prognostic biomarker with decreased OS, rapid progression, and poor response to standard therapy; historical post-first-line OS ~4–6 months in mCRC (morris2020improvementsinclinical pages 1-5, kopetz2019encorafenibbinimetiniband pages 1-2, potocki2023clinicalcharacterizationof pages 11-12) | Morris 2020, *Clin Cancer Res*; Kopetz 2019, *N Engl J Med*; Potocki 2023, *Int J Mol Sci* | mCRC / advanced CRC | — | Inferior prognosis versus BRAF wild-type; historical median OS after initial therapy failure 4–6 months (kopetz2019encorafenibbinimetiniband pages 1-2) | https://doi.org/10.1158/1078-0432.CCR-19-3809 ; https://doi.org/10.1056/NEJMoa1908075 ; https://doi.org/10.3390/ijms24109073 |
| Epidemiology & phenotype | Metastatic pattern / QoL | Reviews note distinct metastatic spread with more bone, brain, and peritoneal involvement and worse HRQoL relative to wild-type CRC (morris2020improvementsinclinical pages 1-5) | Morris 2020, *Clin Cancer Res* | Review | — | Qualitative adverse metastatic pattern / HRQoL impact; exact frequencies not provided in retrieved evidence | https://doi.org/10.1158/1078-0432.CCR-19-3809 |
| Treatment & outcomes | BEACON CRC phase III interim | Previously treated BRAF V600E-mutant mCRC randomized 1:1:1 to triplet, doublet, or control (kopetz2019encorafenibbinimetiniband pages 1-2) | Kopetz 2019, *N Engl J Med* | 665 patients; progressed after 1–2 prior regimens | Encorafenib + binimetinib + cetuximab vs encorafenib + cetuximab vs cetuximab + irinotecan/FOLFIRI | Triplet: OS 9.0 mo, ORR 26%, grade≥3 AEs 58%; Doublet: OS 8.4 mo, grade≥3 AEs 50%; Control: OS 5.4 mo, ORR 2%, grade≥3 AEs 61%. Mechanistic rationale: BRAF monotherapy limited by EGFR-mediated pathway reactivation (kopetz2019encorafenibbinimetiniband pages 1-2) | https://doi.org/10.1056/NEJMoa1908075 |
| Treatment & outcomes | BEACON CRC updated analysis | Updated survival results confirming doublet as standard of care in previously treated disease (tabernero2021encorafenibpluscetuximab pages 1-2) | Tabernero 2021, *J Clin Oncol* | 665 randomized patients with previously treated BRAF V600E mCRC | Triplet: encorafenib + binimetinib + cetuximab; Doublet: encorafenib + cetuximab; Control: cetuximab + irinotecan/FOLFIRI | Triplet: OS 9.3 mo, ORR 26.8%, grade≥3 AEs 65.8%; Doublet: OS 9.3 mo, ORR 19.5%, grade≥3 AEs 57.4%; Control: OS 5.9 mo, ORR 1.8%, grade≥3 AEs 64.2% (tabernero2021encorafenibpluscetuximab pages 1-2) | https://doi.org/10.1200/JCO.20.02088 |
| Treatment & outcomes | BEACON safety lead-in | Early safety/efficacy signal supporting phase III randomized study (cutsem2019binimetinibencorafeniband pages 1-2, cutsem2019binimetinibencorafeniband pages 6-7) | Van Cutsem 2019, *J Clin Oncol* | 30 previously treated BRAF V600E mCRC patients; 29 efficacy-evaluable | Encorafenib 300 mg daily + binimetinib 45 mg BID + weekly cetuximab | ORR 48%; PFS 8.0 mo; OS 15.3 mo; DLTs in 5 patients; common grade 3–4 AEs: fatigue 13%, anemia 10%, ↑CPK 10%, ↑AST 10%, UTI 10%; overall grade 3 and 4 toxicity 53.3% and 16.7% (cutsem2019binimetinibencorafeniband pages 1-2, cutsem2019binimetinibencorafeniband pages 6-7) | https://doi.org/10.1200/JCO.18.02459 |
| Treatment & outcomes | ANCHOR CRC phase II | First-line targeted triplet in untreated BRAF V600E mCRC (cutsem2023anchorcrcresults pages 1-2) | Van Cutsem 2023, *J Clin Oncol* | 95 previously untreated BRAF V600E-mutant mCRC patients | Encorafenib + binimetinib + cetuximab | cORR 47.4% (all PRs); PFS 5.8 mo; OS 18.3 mo; treatment well tolerated with manageable safety, but grade≥3 AEs not numerically reported in retrieved context (cutsem2023anchorcrcresults pages 1-2) | https://doi.org/10.1200/JCO.22.01693 |
| Treatment & outcomes | BREAKWATER phase III | First-line BRAF-targeted combination plus chemotherapy versus SOC in untreated BRAF V600E mCRC (kopetz2025encorafenibcetuximaband pages 1-2) | Kopetz 2025, *Nat Med* | 637 untreated BRAF V600E mCRC patients | Encorafenib + cetuximab + mFOLFOX6 vs standard of care | ORR 60.9% vs 40.0%; median duration of response 13.9 vs 11.1 mo; interim OS HR 0.47; serious AEs 37.7% vs 34.6%; grade≥3 AEs not numerically reported in retrieved context (kopetz2025encorafenibcetuximaband pages 1-2) | https://doi.org/10.1038/s41591-024-03443-3 |
| Treatment & outcomes | BEACON molecular profiling / resistance | Translational biomarker study explaining response and acquired resistance to targeted therapy (kopetz2024molecularprofilingof pages 1-2) | Kopetz 2024, *Nat Med* | BEACON biomarker analyses using tissue WES/WTS and ctDNA | Encorafenib + cetuximab ± binimetinib | Response/resistance correlates: higher immune signatures trended toward greater OS benefit with triplet; acquired alterations commonly involved RAS, MAP2K1, MET; baseline TP53 linked to acquired MET amplification; resistance mutations were subclonal/polyclonal (kopetz2024molecularprofilingof pages 1-2) | https://doi.org/10.1038/s41591-024-03235-9 |
| Treatment & outcomes | Real-world EC population-based study | Real-world survival/effectiveness of encorafenib + cetuximab after approval (numeric outcomes limited in retrieved context) (kopetz2024molecularprofilingof pages 1-2) | Zwart 2024, *Br J Cancer* | Population-based real-world BRAF V600E mCRC treated with EC | Encorafenib + cetuximab | Study identified as efficacy-effectiveness analysis; specific OS/PFS/ORR values not provided in retrieved context | https://doi.org/10.1038/s41416-024-02711-w |
| Treatment & outcomes | Real-world treatment-strategy cohort | Real-world outcomes across chemotherapy and later-line BRAF-targeted therapy (zurloh2023impactofencorafenib pages 1-2) | Zurloh 2023, *J Cancer Res Clin Oncol* | 51 patients with BRAF V600E-mutant mCRC | First-line FOLFOXIRI or FOLFOX/FOLFIRI ± monoclonal antibody; later-line BRAF inhibitor in 17 patients | Median OS 17.6 mo overall; first-line PFS 13.0 mo with FOLFOXIRI vs 4.3 mo with FOLFOX/FOLFIRI; antibody addition associated with improved OS (HR 0.523); targeted therapy associated with OS 25.1 mo; grade≥3 AEs not reported in retrieved context (zurloh2023impactofencorafenib pages 1-2) | https://doi.org/10.1007/s00432-023-05141-y |
| Treatment & outcomes | Real-world multicenter propensity-matched study | Comparative first-line doublet vs triplet chemotherapy plus bevacizumab in BRAF V600E mCRC (wei2024clinicopathologicfeaturesand pages 10-10) | Wei 2024, *BMC Cancer* | 125 patients from 3 institutions | Triplet-drug vs doublet-drug first-line chemotherapy combined with bevacizumab | Median OS 14.9 mo overall; triplets vs doublets OS 17.4 vs 13.4 mo before PSM and 17.4 vs 10.4 mo after PSM; first-line PFS 6.1 mo overall; no significant PFS/ORR/DCR difference between regimens; grade≥3 AEs not reported in retrieved context (wei2024clinicopathologicfeaturesand pages 10-10) | https://doi.org/10.1186/s12885-024-13171-z |
| Diagnostics / implementation | Biomarker testing workflow | Tissue-based BRAF testing commonly performed with KRAS/NRAS; MSI/MMR testing by IHC and/or PCR; BRAF V600E helps distinguish sporadic MSI-H from Lynch syndrome; ctDNA accepted in some trials for BRAF confirmation and resistance profiling (effendiys2024biomarkersasa pages 3-6, eriksen2022aphaseii pages 1-2, NCT05217446 chunk 1, NCT06578559 chunk 1) | Effendi-YS 2024; Eriksen 2022, *BMC Cancer*; ClinicalTrials.gov 2022/2024 | CRC biomarker testing / trial eligibility / retreatment | Tissue or plasma BRAF confirmation; MSI/MMR and RAS co-testing; ctDNA for resistance-guided rechallenge | Trial examples: NCT05217446 allows BRAF confirmation from tumor tissue or blood; NCT06578559 requires ctDNA showing no KRAS/NRAS/MAP2K1 mutations and no MET amplification before EC retreatment (NCT05217446 chunk 1, NCT06578559 chunk 1) | https://doi.org/10.5772/intechopen.1004189 ; https://doi.org/10.1186/s12885-022-10420-x ; https://clinicaltrials.gov/study/NCT05217446 ; https://clinicaltrials.gov/study/NCT06578559 |


*Table: This table compiles disease metadata, clinicopathologic characteristics, and the most clinically relevant treatment studies for BRAF V600E–mutant colorectal cancer. It is designed to support rapid knowledge-base population with cited prevalence, phenotype, biomarker, and outcome data.*

BEACON updated Kaplan–Meier OS curves and tumor response table are available as visual evidence. (tabernero2021encorafenibpluscetuximab media 2b387ba4, tabernero2021encorafenibpluscetuximab media 9dac50ff)


## Limitations / gaps in retrieved sources
- Formal ontology identifiers (MONDO, MeSH, ICD-10/11 mapping specific to BRAF V600E subtype) were not found in the retrieved corpus.
- Quantitative symptom frequencies, QoL instrument scores, and detailed CRC screening guideline text were not present in retrieved excerpts.
- Species-wide “natural disease” analogs and veterinary disease parallels were not identified.


### Primary-source URLs (examples)
- BEACON CRC (NEJM 2019; published Oct 2019): https://doi.org/10.1056/NEJMoa1908075 (kopetz2019encorafenibbinimetiniband pages 1-2)
- BEACON updated (JCO 2021; published Feb 2021): https://doi.org/10.1200/JCO.20.02088 (tabernero2021encorafenibpluscetuximab pages 1-2)
- ANCHOR CRC (JCO 2023; published May 2023): https://doi.org/10.1200/JCO.22.01693 (cutsem2023anchorcrcresults pages 1-2)
- BEACON multi-omics profiling (Nature Medicine 2024; published Sep 2024): https://doi.org/10.1038/s41591-024-03235-9 (kopetz2024molecularprofilingof pages 1-2)
- Body size MR (eBioMedicine 2024; published Mar 2024): https://doi.org/10.1016/j.ebiom.2024.105010 (papadimitriou2024bodysizeand pages 1-2)
- ctDNA-guided rechallenge trial registry (posted 2024): https://clinicaltrials.gov/study/NCT06578559 (NCT06578559 chunk 1)


References

1. (zurloh2023impactofencorafenib pages 1-2): M. Zurloh, M. Goetz, T. Herold, J. Treckmann, P. Markus, B. Schumacher, D. Albers, A. Rink, V. Rosery, G. Zaun, K. Kostbade, M. Pogorzelski, S. Ting, H. Schmidt, R. Stiens, M. Wiesweg, M. Schuler, Stefan Kasper, and I. Virchow. Impact of encorafenib on survival of patients with brafv600e-mutant metastatic colorectal cancer in a real-world setting. Journal of Cancer Research and Clinical Oncology, 149:12903-12912, Jul 2023. URL: https://doi.org/10.1007/s00432-023-05141-y, doi:10.1007/s00432-023-05141-y. This article has 1 citations and is from a peer-reviewed journal.

2. (kopetz2024molecularprofilingof pages 1-2): Scott Kopetz, Danielle A. Murphy, Jie Pu, Fortunato Ciardiello, Jayesh Desai, Eric Van Cutsem, Harpreet Singh Wasan, Takayuki Yoshino, Hedieh Saffari, Xiaosong Zhang, Phineas Hamilton, Tao Xie, Rona Yaeger, and Josep Tabernero. Molecular profiling of braf-v600e-mutant metastatic colorectal cancer in the phase 3 beacon crc trial. Nature Medicine, 30:3261-3271, Sep 2024. URL: https://doi.org/10.1038/s41591-024-03235-9, doi:10.1038/s41591-024-03235-9. This article has 77 citations and is from a highest quality peer-reviewed journal.

3. (NCT06578559 chunk 1):  Phase II Study of ctDNA-guided Encorafenib Plus Cetuximab Retreatment in Patients BRAF V600E Mutated mCRC. Gruppo Oncologico del Nord-Ovest. 2024. ClinicalTrials.gov Identifier: NCT06578559

4. (morris2020improvementsinclinical pages 1-5): Van K. Morris and Tanios Bekaii-Saab. Improvements in clinical outcomes for <i>brafv600e</i>-mutant metastatic colorectal cancer. Clinical Cancer Research, 26:4435-4441, Sep 2020. URL: https://doi.org/10.1158/1078-0432.ccr-19-3809, doi:10.1158/1078-0432.ccr-19-3809. This article has 39 citations and is from a highest quality peer-reviewed journal.

5. (kopetz2019encorafenibbinimetiniband pages 1-2): Scott Kopetz, Axel Grothey, Rona Yaeger, Eric Van Cutsem, Jayesh Desai, Takayuki Yoshino, Harpreet Wasan, Fortunato Ciardiello, Fotios Loupakis, Yong Sang Hong, Neeltje Steeghs, Tormod K. Guren, Hendrik-Tobias Arkenau, Pilar Garcia-Alfonso, Per Pfeiffer, Sergey Orlov, Sara Lonardi, Elena Elez, Tae-Won Kim, Jan H.M. Schellens, Christina Guo, Asha Krishnan, Jeroen Dekervel, Van Morris, Aitana Calvo Ferrandiz, L.S. Tarpgaard, Michael Braun, Ashwin Gollerkeri, Christopher Keir, Kati Maharry, Michael Pickard, Janna Christy-Bittel, Lisa Anderson, Victor Sandor, and Josep Tabernero. Encorafenib, binimetinib, and cetuximab in <i>braf</i> v600e–mutated colorectal cancer. New England Journal of Medicine, 381:1632-1643, Oct 2019. URL: https://doi.org/10.1056/nejmoa1908075, doi:10.1056/nejmoa1908075. This article has 1745 citations and is from a highest quality peer-reviewed journal.

6. (cutsem2023anchorcrcresults pages 1-2): Eric Van Cutsem, Julien Taieb, Rona Yaeger, Takayuki Yoshino, Axel Grothey, Evaristo Maiello, Elena Elez, Jeroen Dekervel, Paul Ross, Ana Ruiz-Casado, Janet Graham, Takeshi Kato, Jose C. Ruffinelli, Thierry André, Edith Carrière Roussel, Isabelle Klauck, Mélanie Groc, Jean-Claude Vedovato, and Josep Tabernero. Anchor crc: results from a single-arm, phase ii study of encorafenib plus binimetinib and cetuximab in previously untreated <i>braf</i><sup>v600e</sup>-mutant metastatic colorectal cancer. Journal of Clinical Oncology, 41:2628-2637, May 2023. URL: https://doi.org/10.1200/jco.22.01693, doi:10.1200/jco.22.01693. This article has 99 citations and is from a highest quality peer-reviewed journal.

7. (eriksen2022aphaseii pages 1-2): Martina Eriksen, Per Pfeiffer, Kristoffer Staal Rohrberg, Christina Westmose Yde, Lone Nørgård Petersen, Laurids Østergaard Poulsen, and Camilla Qvortrup. A phase ii study of daily encorafenib in combination with biweekly cetuximab in patients with braf v600e mutated metastatic colorectal cancer: the new beacon study. BMC Cancer, Dec 2022. URL: https://doi.org/10.1186/s12885-022-10420-x, doi:10.1186/s12885-022-10420-x. This article has 8 citations and is from a peer-reviewed journal.

8. (potocki2023clinicalcharacterizationof pages 1-2): Paweł M. Potocki, Piotr Wójcik, Łukasz Chmura, Bartłomiej Goc, Marcin Fedewicz, Zofia Bielańska, Jakub Swadźba, Kamil Konopka, Łukasz Kwinta, and Piotr J. Wysocki. Clinical characterization of targetable mutations (braf v600e and kras g12c) in advanced colorectal cancer—a nation-wide study. International Journal of Molecular Sciences, 24:9073, May 2023. URL: https://doi.org/10.3390/ijms24109073, doi:10.3390/ijms24109073. This article has 15 citations.

9. (guerrero2023brafinhibitorsin pages 1-2): Patricia Guerrero, Víctor Albarrán, María San Román, Carlos González-Merino, Coral García de Quevedo, Jaime Moreno, Juan Carlos Calvo, Guillermo González, Inmaculada Orejana, Jesús Chamorro, Íñigo Martínez-Delfrade, Blanca Morón, Belén de Frutos, and María Reyes Ferreiro. Braf inhibitors in metastatic colorectal cancer and mechanisms of resistance: a review of the literature. Cancers, 15:5243, Oct 2023. URL: https://doi.org/10.3390/cancers15215243, doi:10.3390/cancers15215243. This article has 23 citations.

10. (effendiys2024biomarkersasa pages 3-6): Rustam Effendi-YS, Amido Rey, and Imelda Rey. Biomarkers as a therapeutic approach in colorectal carcinoma. Advances in Diagnosis and Therapy of Colorectal Carcinoma, Feb 2024. URL: https://doi.org/10.5772/intechopen.1004189, doi:10.5772/intechopen.1004189. This article has 0 citations.

11. (papadimitriou2024bodysizeand pages 1-2): Nikos Papadimitriou, Conghui Qu, Tabitha A. Harrison, Alaina M. Bever, Richard M. Martin, Konstantinos K. Tsilidis, Polly A. Newcomb, Stephen N. Thibodeau, Christina C. Newton, Caroline Y. Um, Mireia Obón-Santacana, Victor Moreno, Hermann Brenner, Marko Mandic, Jenny Chang-Claude, Michael Hoffmeister, Andrew J. Pellatt, Robert E. Schoen, Sophia Harlid, Shuji Ogino, Tomotaka Ugai, Daniel D. Buchanan, Brigid M. Lynch, Stephen B. Gruber, Yin Cao, Li Hsu, Jeroen R. Huyghe, Yi Lin, Robert S. Steinfelder, Wei Sun, Bethany Van Guelpen, Syed H. Zaidi, Amanda E. Toland, Sonja I. Berndt, Wen-Yi Huang, Elom K. Aglago, David A. Drew, Amy J. French, Peter Georgeson, Marios Giannakis, Meredith Hullar, Johnathan A. Nowak, Claire E. Thomas, Loic Le Marchand, Iona Cheng, Steven Gallinger, Mark A. Jenkins, Marc J. Gunter, Peter T. Campbell, Ulrike Peters, Mingyang Song, Amanda I. Phipps, and Neil Murphy. Body size and risk of colorectal cancer molecular defined subtypes and pathways: mendelian randomization analyses. eBioMedicine, 101:105010, Mar 2024. URL: https://doi.org/10.1016/j.ebiom.2024.105010, doi:10.1016/j.ebiom.2024.105010. This article has 10 citations and is from a peer-reviewed journal.

12. (theofanous2024exploringtheprotective pages 69-72): Despoina Theofanous. Exploring the protective effects of resveratrol and interactions with dietary fat in a mouse model of brafv600e driven colorectal cancer. Text, Jan 2024. URL: https://doi.org/10.25392/leicester.data.25053359.v1, doi:10.25392/leicester.data.25053359.v1. This article has 0 citations and is from a peer-reviewed journal.

13. (theofanous2024exploringtheprotective pages 1-5): Despoina Theofanous. Exploring the protective effects of resveratrol and interactions with dietary fat in a mouse model of brafv600e driven colorectal cancer. Text, Jan 2024. URL: https://doi.org/10.25392/leicester.data.25053359.v1, doi:10.25392/leicester.data.25053359.v1. This article has 0 citations and is from a peer-reviewed journal.

14. (potocki2023clinicalcharacterizationof pages 4-5): Paweł M. Potocki, Piotr Wójcik, Łukasz Chmura, Bartłomiej Goc, Marcin Fedewicz, Zofia Bielańska, Jakub Swadźba, Kamil Konopka, Łukasz Kwinta, and Piotr J. Wysocki. Clinical characterization of targetable mutations (braf v600e and kras g12c) in advanced colorectal cancer—a nation-wide study. International Journal of Molecular Sciences, 24:9073, May 2023. URL: https://doi.org/10.3390/ijms24109073, doi:10.3390/ijms24109073. This article has 15 citations.

15. (iliepetrov2024…ofcolorectal pages 7-9): AC Ilie-Petrov, DA Cristian, and AS Diaconescu. … of colorectal cancer: exploring molecular classifications and analyzing the interplay among molecular biomarkers mmr/msi, kras, nras, braf and cdx2-a …. Unknown journal, 2024.

16. (tabernero2021encorafenibpluscetuximab pages 1-2): Josep Tabernero, Axel Grothey, Eric Van Cutsem, Rona Yaeger, Harpreet Wasan, Takayuki Yoshino, Jayesh Desai, Fortunato Ciardiello, Fotios Loupakis, Yong Sang Hong, Neeltje Steeghs, Tormod Kyrre Guren, Hendrik-Tobias Arkenau, Pilar Garcia-Alfonso, Elena Elez, Ashwin Gollerkeri, Kati Maharry, Janna Christy-Bittel, and Scott Kopetz. Encorafenib plus cetuximab as a new standard of care for previously treated <i>braf</i> v600e–mutant metastatic colorectal cancer: updated survival results and subgroup analyses from the beacon study. Journal of Clinical Oncology, 39:273-284, Feb 2021. URL: https://doi.org/10.1200/jco.20.02088, doi:10.1200/jco.20.02088. This article has 608 citations and is from a highest quality peer-reviewed journal.

17. (morris2020improvementsinclinical pages 11-14): Van K. Morris and Tanios Bekaii-Saab. Improvements in clinical outcomes for <i>brafv600e</i>-mutant metastatic colorectal cancer. Clinical Cancer Research, 26:4435-4441, Sep 2020. URL: https://doi.org/10.1158/1078-0432.ccr-19-3809, doi:10.1158/1078-0432.ccr-19-3809. This article has 39 citations and is from a highest quality peer-reviewed journal.

18. (lawler2024thehistologicaland pages 1-2): Thomas Lawler, Lisa A. Parlato, and Shaneda Warren Andersen. The histological and molecular characteristics of early-onset colorectal cancer: a systematic review and meta-analysis. Frontiers in Oncology, Apr 2024. URL: https://doi.org/10.3389/fonc.2024.1349572, doi:10.3389/fonc.2024.1349572. This article has 37 citations.

19. (NCT05217446 chunk 1):  A Study of Encorafenib Plus Cetuximab Taken Together With Pembrolizumab Compared to Pembrolizumab Alone in People With Previously Untreated Metastatic Colorectal Cancer. Pfizer. 2022. ClinicalTrials.gov Identifier: NCT05217446

20. (wei2024clinicopathologicfeaturesand pages 10-10): Gui-Xia Wei, Yu-Wen Zhou, Chao Dong, Tao Zhang, Peng Cao, Lin Xie, and Meng Qiu. Clinicopathologic features and treatment efficacy of patients with braf v600e-mutated metastatic colorectal cancer: a multi-center real-world propensity score matching study. BMC Cancer, Nov 2024. URL: https://doi.org/10.1186/s12885-024-13171-z, doi:10.1186/s12885-024-13171-z. This article has 2 citations and is from a peer-reviewed journal.

21. (tabernero2021encorafenibpluscetuximab media 2b387ba4): Josep Tabernero, Axel Grothey, Eric Van Cutsem, Rona Yaeger, Harpreet Wasan, Takayuki Yoshino, Jayesh Desai, Fortunato Ciardiello, Fotios Loupakis, Yong Sang Hong, Neeltje Steeghs, Tormod Kyrre Guren, Hendrik-Tobias Arkenau, Pilar Garcia-Alfonso, Elena Elez, Ashwin Gollerkeri, Kati Maharry, Janna Christy-Bittel, and Scott Kopetz. Encorafenib plus cetuximab as a new standard of care for previously treated <i>braf</i> v600e–mutant metastatic colorectal cancer: updated survival results and subgroup analyses from the beacon study. Journal of Clinical Oncology, 39:273-284, Feb 2021. URL: https://doi.org/10.1200/jco.20.02088, doi:10.1200/jco.20.02088. This article has 608 citations and is from a highest quality peer-reviewed journal.

22. (tabernero2021encorafenibpluscetuximab media 9dac50ff): Josep Tabernero, Axel Grothey, Eric Van Cutsem, Rona Yaeger, Harpreet Wasan, Takayuki Yoshino, Jayesh Desai, Fortunato Ciardiello, Fotios Loupakis, Yong Sang Hong, Neeltje Steeghs, Tormod Kyrre Guren, Hendrik-Tobias Arkenau, Pilar Garcia-Alfonso, Elena Elez, Ashwin Gollerkeri, Kati Maharry, Janna Christy-Bittel, and Scott Kopetz. Encorafenib plus cetuximab as a new standard of care for previously treated <i>braf</i> v600e–mutant metastatic colorectal cancer: updated survival results and subgroup analyses from the beacon study. Journal of Clinical Oncology, 39:273-284, Feb 2021. URL: https://doi.org/10.1200/jco.20.02088, doi:10.1200/jco.20.02088. This article has 608 citations and is from a highest quality peer-reviewed journal.

23. (kopetz2025encorafenibcetuximaband pages 1-2): Scott Kopetz, Takayuki Yoshino, Eric Van Cutsem, Cathy Eng, Tae Won Kim, Harpreet Singh Wasan, Jayesh Desai, Fortunato Ciardiello, Rona Yaeger, Timothy S. Maughan, Elena Beyzarov, Xiaoxi Zhang, Graham Ferrier, Xiaosong Zhang, and Josep Tabernero. Encorafenib, cetuximab and chemotherapy in braf-mutant colorectal cancer: a randomized phase 3 trial. Nature Medicine, 31:901-908, Jan 2025. URL: https://doi.org/10.1038/s41591-024-03443-3, doi:10.1038/s41591-024-03443-3. This article has 106 citations and is from a highest quality peer-reviewed journal.

24. (cutsem2019binimetinibencorafeniband pages 1-2): Eric Van Cutsem, Sanne Huijberts, Axel Grothey, Rona Yaeger, Pieter-Jan Cuyle, Elena Elez, Marwan Fakih, Clara Montagut, Marc Peeters, Takayuki Yoshino, Harpreet Wasan, Jayesh Desai, Fortunato Ciardiello, Ashwin Gollerkeri, Janna Christy-Bittel, Kati Maharry, Victor Sandor, Jan H.M. Schellens, Scott Kopetz, and Josep Tabernero. Binimetinib, encorafenib, and cetuximab triplet therapy for patients with <i>braf</i> v600e–mutant metastatic colorectal cancer: safety lead-in results from the phase iii beacon colorectal cancer study. Journal of Clinical Oncology, 37:1460-1469, Jun 2019. URL: https://doi.org/10.1200/jco.18.02459, doi:10.1200/jco.18.02459. This article has 273 citations and is from a highest quality peer-reviewed journal.

25. (randalldemllo2024exvivointestinal pages 4-6): Sarron Randall-Demllo, Ghanyah Al-Qadami, Anita E. Raposo, Chenkai Ma, Ilka K. Priebe, Maryam Hor, Rajvinder Singh, and Kim Y. C. Fung. Ex vivo intestinal organoid models: current state-of-the-art and challenges in disease modelling and therapeutic testing for colorectal cancer. Cancers, 16:3664, Oct 2024. URL: https://doi.org/10.3390/cancers16213664, doi:10.3390/cancers16213664. This article has 4 citations.

26. (tardito2024epidermalgrowthfactor pages 1-2): Samuele Tardito, Serena Matis, Maria Raffaella Zocchi, Roberto Benelli, and Alessandro Poggi. Epidermal growth factor receptor targeting in colorectal carcinoma: antibodies and patient-derived organoids as a smart model to study therapy resistance. International Journal of Molecular Sciences, 25:7131, Jun 2024. URL: https://doi.org/10.3390/ijms25137131, doi:10.3390/ijms25137131. This article has 24 citations.

27. (perron2024integrativeensemblemodelling pages 1-2): Umberto Perron, Elena Grassi, Aikaterini Chatzipli, Marco Viviani, Emre Karakoc, Lucia Trastulla, Lorenzo M. Brochier, Claudio Isella, Eugenia R. Zanella, Hagen Klett, Ivan Molineris, Julia Schueler, Manel Esteller, Enzo Medico, Nathalie Conte, Ultan McDermott, Livio Trusolino, Andrea Bertotti, and Francesco Iorio. Integrative ensemble modelling of cetuximab sensitivity in colorectal cancer patient-derived xenografts. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53163-y, doi:10.1038/s41467-024-53163-y. This article has 13 citations and is from a highest quality peer-reviewed journal.

28. (potocki2023clinicalcharacterizationof pages 11-12): Paweł M. Potocki, Piotr Wójcik, Łukasz Chmura, Bartłomiej Goc, Marcin Fedewicz, Zofia Bielańska, Jakub Swadźba, Kamil Konopka, Łukasz Kwinta, and Piotr J. Wysocki. Clinical characterization of targetable mutations (braf v600e and kras g12c) in advanced colorectal cancer—a nation-wide study. International Journal of Molecular Sciences, 24:9073, May 2023. URL: https://doi.org/10.3390/ijms24109073, doi:10.3390/ijms24109073. This article has 15 citations.

29. (cutsem2019binimetinibencorafeniband pages 6-7): Eric Van Cutsem, Sanne Huijberts, Axel Grothey, Rona Yaeger, Pieter-Jan Cuyle, Elena Elez, Marwan Fakih, Clara Montagut, Marc Peeters, Takayuki Yoshino, Harpreet Wasan, Jayesh Desai, Fortunato Ciardiello, Ashwin Gollerkeri, Janna Christy-Bittel, Kati Maharry, Victor Sandor, Jan H.M. Schellens, Scott Kopetz, and Josep Tabernero. Binimetinib, encorafenib, and cetuximab triplet therapy for patients with <i>braf</i> v600e–mutant metastatic colorectal cancer: safety lead-in results from the phase iii beacon colorectal cancer study. Journal of Clinical Oncology, 37:1460-1469, Jun 2019. URL: https://doi.org/10.1200/jco.18.02459, doi:10.1200/jco.18.02459. This article has 273 citations and is from a highest quality peer-reviewed journal.
