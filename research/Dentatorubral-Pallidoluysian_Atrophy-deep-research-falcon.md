---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T13:25:58.508314'
end_time: '2026-05-08T13:46:06.824185'
duration_seconds: 1208.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dentatorubral-Pallidoluysian Atrophy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dentatorubral-Pallidoluysian Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dentatorubral-Pallidoluysian Atrophy** covering all of the
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

## Dentatorubral-Pallidoluysian Atrophy (DRPLA) — Comprehensive Disease Characteristics Report (2023–2024 prioritized)

### Target disease
- **Disease name:** Dentatorubral-pallidoluysian atrophy (DRPLA) (chaudhry2021drplaunderstandingthe pages 1-3)
- **Category:** Mendelian, repeat expansion (polyglutamine) neurodegenerative disease (chaudhry2021drplaunderstandingthe pages 1-3, nowak2023atrophin‐1functionand pages 1-2)
- **MONDO ID:** **MONDO_0007435** (OpenTargets mapping) (OpenTargets Search: Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
DRPLA is an autosomal dominant, progressive, neurodegenerative repeat-expansion disorder caused by a CAG expansion in **ATN1** (atrophin-1), and is clinically characterized by cerebellar ataxia, cognitive decline/dementia, myoclonus, epilepsy, chorea/choreoathetosis, and psychiatric manifestations (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4).

Recent (2024) patient-organization perspective emphasizes DRPLA as “an ultra-rare neurodegenerative disorder characterized by ataxia, cognitive decline, myoclonus, chorea, epilepsy, and psychiatric manifestations” and explicitly notes **MIM#125370** (prades2024establishingresourcesand pages 1-2).

### 1.2 Key identifiers (with availability in retrieved sources)
- **OMIM/MIM:** **125370** (listed as “DRPLA, MIM#125370”) (prades2024establishingresourcesand pages 1-2)
- **MONDO:** **MONDO_0007435** (OpenTargets disease mapping) (OpenTargets Search: Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1)
- **Orphanet:** **Orphanet_101** (OpenTargets disease mapping) (OpenTargets Search: Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1)
- **MeSH / ICD-10 / ICD-11:** not available in the retrieved full-text corpus for this run; therefore not reported here.

### 1.3 Synonyms / alternative names
- DRPLA; dentatorubral pallidoluysian atrophy; “hereditary DRPLA” (historical naming) (chaudhry2021drplaunderstandingthe pages 1-3)
- Often discussed alongside autosomal dominant SCAs / hereditary ataxias in diagnostic workflows (rudaks2024anupdateon pages 1-2, rudaks2024anupdateon pages 10-12)

### 1.4 Evidence source type
This entry synthesizes **aggregated disease-level resources** (systematic review-style neurology update, movement disorders review, patient-organization review, clinical trial registries) and **individual patient evidence** (case reports, infantile case report) (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 1-2, chen2024dentatorubralpallidoluysianatrophya pages 1-2, baide‐mairena2023infantile‐onsetparkinsonismdyskinesia pages 1-3, NCT07084311 chunk 1).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** unstable **CAG repeat expansion** in **exon 5** of **ATN1** (chromosome 12p13.31) encoding a polyglutamine-expanded atrophin-1 protein (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5).

Direct abstract quote (neurology update): “Dentatorubral–pallidoluysian atrophy (DRPLA) is a rare neurodegenerative disorder caused by CAG repeat expansions in the atrophin-1 gene and is inherited in an autosomal dominant fashion.” (published online 26 Oct 2020; Journal of Neurology 2021) (chaudhry2021drplaunderstandingthe pages 1-3).

### 2.2 Risk factors
- **Genetic:** ATN1 CAG repeat expansion length is the principal determinant of risk, with strong genotype–phenotype correlation (chaudhry2021drplaunderstandingthe pages 1-3, nowak2023atrophin‐1functionand pages 1-2).
- **Transmission-related:** genetic anticipation is prominent; paternal transmission is often associated with more prominent anticipation (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4).
- **Somatic instability:** somatic CAG instability creates tissue mosaicism and is hypothesized to contribute to progression (nowak2023atrophin‐1functionand pages 2-2, hasuike2022cagrepeatbindingsmall pages 1-2).

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes (with suggested HPO terms)

A structured phenotype table with HPO suggestions and age associations is provided below.

| Phenotype (plain language) | Suggested HPO term(s) | Typical age-of-onset association | Supporting evidence / notes |
|---|---|---|---|
| Cerebellar ataxia / gait incoordination | HP:0001251 Ataxia; HP:0002066 Gait ataxia | Both juvenile and adult; often a major presenting feature in adult-onset disease | DRPLA is characterized by progressive cerebellar ataxia; patients with onset after age 20 tend to present with cerebellar ataxia, choreoathetosis, and dementia. Adult-onset cases commonly show ataxia as an early/core feature (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, ber2003prevalenceofdentatorubralpallidoluysian pages 1-2). |
| Cognitive decline / dementia | HP:0001268 Mental deterioration; HP:0000726 Dementia; HP:0001249 Intellectual disability | Juvenile: developmental delay / intellectual disability more prominent; Adult: cognitive decline and dementia common | Core disease descriptions include cognitive impairment/dementia. Juvenile-onset DRPLA is associated with developmental delay and progressive intellectual disability, whereas adult-onset disease commonly includes dementia/cognitive decline (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5, ber2003prevalenceofdentatorubralpallidoluysian pages 1-2). |
| Myoclonus | HP:0001336 Myoclonus | Strongly associated with juvenile-onset | Juvenile-onset DRPLA typically presents with a “myoclonus phenotype”; juvenile cases are characterized by myoclonus and epilepsy, while adult-onset cases more often show chorea/ataxia/dementia (nowak2023atrophin‐1functionand pages 2-2, chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5). |
| Epilepsy / seizures | HP:0001250 Seizure; HP:0002123 Generalized myoclonic seizure; HP:0002069 Generalized tonic-clonic seizure | Strongly associated with juvenile-onset; uncommon/less frequent in adult-onset, especially after age 40 | Seizures are common in juvenile-onset DRPLA and become less frequent with later onset; juvenile patients may have generalized seizures early and generalized tonic-clonic seizures later. Adult-onset epilepsy is reported but less common (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5, ber2003prevalenceofdentatorubralpallidoluysian pages 1-2). |
| Chorea / choreoathetosis / involuntary movements | HP:0002072 Chorea; HP:0001266 Choreoathetosis; HP:0004305 Athetosis | More typical of adult-onset | Adult-onset DRPLA is characterized by ataxia, choreoathetosis/involuntary movements, cognitive impairment, and personality/psychiatric change. Choreoathetoid movements are one of the classic described phenotypes (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5, ber2003prevalenceofdentatorubralpallidoluysian pages 1-2). |
| Psychiatric symptoms / personality change | HP:0000708 Behavioral abnormality; HP:0000716 Depression; HP:0000738 Hallucinations | More typical of adult-onset, though can occur across forms | Psychiatric manifestations are part of the cardinal feature set. Adult-onset DRPLA commonly includes personality changes and psychiatric symptoms; disease overviews also list psychiatric symptoms among key manifestations (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5). |
| Developmental delay / progressive intellectual disability | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Juvenile / infantile | Juvenile-onset DRPLA is characterized by developmental delay and progressive intellectual disability, reflecting the severe neurodevelopmental/neurodegenerative presentation in early-onset disease (prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5). |
| White matter lesions and cerebellar/brainstem atrophy on MRI | HP:0002500 Abnormal cerebral white matter morphology; HP:0001272 Cerebellar atrophy; HP:0002367 Brainstem atrophy | Seen in both; more evident with progression | MRI commonly shows progressive brainstem and cerebellar atrophy and widespread white matter lesions involving cerebrum, thalamus, brainstem, and cerebellum. The DRPLA natural history study uses brain atrophy on MRI (brainstem, superior cerebellar peduncle, cerebellum, thalamus) as a primary outcome (chen2024dentatorubralpallidoluysianatrophya pages 3-5, NCT06273150 chunk 1, chaudhry2021drplaunderstandingthe pages 1-3). |
| Dysphagia / swallowing difficulty | HP:0002015 Dysphagia | Progressive complication; not clearly age-specific in retrieved sources | The ongoing natural history study includes a Clinical Assessment of Dysphagia in Neurodegeneration, indicating dysphagia is clinically relevant for longitudinal phenotyping, although age specificity was not detailed in the retrieved context (NCT06273150 chunk 1). |
| Speech impairment / dysarthria | HP:0001260 Dysarthria; HP:0002167 Slurred speech | Progressive complication; not clearly age-specific in retrieved sources | The natural history study includes a DRPLA-specific speech battery, supporting speech disturbance as a measurable phenotype in clinical follow-up, although retrieved texts did not stratify it by juvenile vs adult onset (NCT06273150 chunk 1). |
| Nystagmus / abnormal eye movements | HP:0000639 Nystagmus; HP:0000640 Gaze-evoked nystagmus | Reported in adult case; age association not established | A 34-year-old adult case showed bilateral upward rotational nystagmus; the authors suggested this may be a clinical sign worth considering, but this appears to be a less established/possibly uncommon phenotype in the retrieved literature (chen2024dentatorubralpallidoluysianatrophya pages 1-2, chen2024dentatorubralpallidoluysianatrophya pages 3-5). |


*Table: This table summarizes major clinical and imaging phenotypes of dentatorubral-pallidoluysian atrophy, with suggested HPO mappings and whether each feature is more typical of juvenile- or adult-onset disease. It is useful for knowledge-base phenotype annotation and age-stratified curation.*

Key phenotype stratification by age-of-onset:
- Juvenile-onset (<20 years) commonly features myoclonus and epilepsy, with developmental delay/intellectual disability and more rapid progression in many reports (prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 2-2).
- Adult-onset (>20 years) commonly features progressive ataxia, choreoathetosis/chorea, cognitive impairment/dementia, and psychiatric/personality changes (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 2-2).

Quality-of-life (QoL) impact evidence within this run is mainly inferred from the existence of QoL-focused registry and trial endpoints (CPCHILD; caregiver burden; health economics) rather than validated disease-specific QoL instruments reported in full text (NCT05489393 chunk 1, NCT07084311 chunk 1).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **ATN1 (atrophin-1)** is the only gene known to cause DRPLA, located on **chromosome 12p13.31** (prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5).

### 4.2 Pathogenic variant class
- **Repeat expansion** (CAG) in a coding region (exon 5) producing an expanded **polyglutamine** tract (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4).

### 4.3 Repeat-size ranges and penetrance (data)
Across major reviews/case literature retrieved here:
- Normal alleles: typically **~6–35** CAG repeats (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 1-2).
- **Incomplete penetrance:** often reported for **35–47** repeats (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 1-2).
- **Full penetrance:** typically at **≥48** repeats (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 1-2).
- Juvenile/infantile disease correlates with larger expansions (e.g., >70; extreme cases >90) (nowak2023atrophin‐1functionand pages 1-2, nowak2023atrophin‐1functionand pages 2-2).

Recent 2023 primary case data: an infantile-onset case was reported with “**the largest ATN1 CAG expansion reported to date (98 repeats)**” (Annals of Clinical and Translational Neurology, Jul 2023; https://doi.org/10.1002/acn3.51858) (baide‐mairena2023infantile‐onsetparkinsonismdyskinesia pages 1-3).

### 4.4 Modifier genes / pathways
A 2022 preclinical DRPLA study (and its framing) highlights the role of **somatic repeat instability** and references DNA repair modifiers (e.g., MLH1/MSH3/PMS2/FAN1 in context) as a general mechanism affecting age at onset/severity in repeat expansion disorders (Neurobiology of Disease 2022; https://doi.org/10.1016/j.nbd.2021.105604) (hasuike2022cagrepeatbindingsmall pages 1-2).

### 4.5 Functional consequences (current synthesis)
Evidence converges on predominantly **toxic gain-of-function** of mutant atrophin-1, with broad downstream cellular dysfunction including transcriptional dysregulation and proteostasis/autophagy defects (nowak2023atrophin‐1functionand pages 4-5, nowak2023atrophin‐1functionand pages 2-2).

---

## 5. Environmental Information

No validated environmental triggers, toxins, infectious agents, or lifestyle risk factors specific to DRPLA were identified in the retrieved sources for this run.

---

## 6. Mechanism / Pathophysiology (causal chain; ontology suggestions)

### 6.1 Mechanistic summary (from upstream trigger to clinical manifestations)
**Upstream trigger:** expansion of CAG repeats in ATN1 → expanded polyQ atrophin-1 (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4).

**Intermediate molecular/cellular mechanisms:**
- Mutant atrophin-1 aggregation and altered protein–protein interactions (nowak2023atrophin‐1functionand pages 1-2).
- Transcriptional dysregulation via sequestration/interaction with transcriptional regulators (TBP/CBP/TAFII130/RERE) (nowak2023atrophin‐1functionand pages 4-5).
- Proteostasis disruption including autophagy-lysosomal impairment (“canonical autophagy is blocked at the lysosomal level” in the reviewed mechanistic summary) (nowak2023atrophin‐1functionand pages 4-5).
- Somatic and germline repeat instability → mosaicism and anticipation, potentially accelerating neuronal dysfunction over time (nowak2023atrophin‐1functionand pages 2-2, chaudhry2021drplaunderstandingthe pages 1-3).

**Tissue/circuit vulnerability and clinical output:** neuronal dysfunction and neurodegeneration in cerebellar and basal ganglia-related regions (dentate nucleus, globus pallidus, subthalamic nucleus; broader brainstem/white matter involvement), producing ataxia, involuntary movements (chorea/choreoathetosis), epilepsy/myoclonus (especially juvenile onset), and cognitive/psychiatric features (nowak2023atrophin‐1functionand pages 2-2, chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5).

A structured mechanism table with suggested GO/CL/UBERON terms is provided below.

| Level | Mechanism description | Suggested GO biological process / cellular component terms | Suggested CL cell types | Suggested UBERON anatomy | Key supporting citations |
|---|---|---|---|---|---|
| Genetic | DRPLA is caused by an unstable CAG repeat expansion in exon 5 of **ATN1** on chromosome 12p13.31. Full penetrance is typically reported at **>=48 CAG** repeats, with **35-47** repeats described as incompletely penetrant; longer repeats are associated with earlier onset, more severe disease, and anticipation. Somatic and germline repeat instability are central upstream drivers of disease progression. | GO:0003677 DNA binding; GO:0006974 cellular response to DNA damage stimulus; GO:0006310 DNA recombination | CL:0000540 neuron | UBERON:0000955 brain; UBERON:0000073 cerebellum | (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, hasuike2022cagrepeatbindingsmall pages 1-2, nowak2023atrophin‐1functionand pages 2-2, nowak2023atrophin‐1functionand pages 1-2) |
| Protein | Expanded CAG repeats encode a polyglutamine-expanded **atrophin-1** protein that undergoes conformational change, aggregation, and abnormal protein-protein interactions. Mutant atrophin-1 is considered a toxic gain-of-function species; loss of ATN1 alone is not thought to explain disease. Nuclear accumulation/inclusions occur, but are not the sole pathogenic mechanism. | GO:0006508 proteolysis; GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process; GO:0097352 autophagosome maturation; GO:0016604 nuclear body | CL:0000540 neuron | UBERON:0000955 brain | (nowak2023atrophin‐1functionand pages 2-2, nowak2023atrophin‐1functionand pages 7-8, nowak2023atrophin‐1functionand pages 4-5, nowak2023atrophin‐1functionand pages 1-2) |
| Cellular | Mutant atrophin-1 disrupts transcriptional regulation by binding/sequestering transcriptional regulators including **TBP**, **CBP**, **TAFII130**, and **RERE**, contributing to transcriptional dysregulation and altered chromatin regulation. This is a major downstream mechanism linking repeat expansion to neuronal dysfunction. | GO:0006357 regulation of transcription by RNA polymerase II; GO:0016568 chromatin modification; GO:0005634 nucleus | CL:0000540 neuron | UBERON:0000955 brain | (nowak2023atrophin‐1functionand pages 2-2, nowak2023atrophin‐1functionand pages 4-5, nowak2023atrophin‐1functionand pages 1-2) |
| Cellular | Autophagy-lysosomal dysfunction is implicated in DRPLA pathogenesis; canonical autophagy is reported as blocked at the lysosomal level, with compensatory alternative protein-clearance pathways activated. Impaired clearance promotes persistence of mutant ATN1 and cellular degeneration. | GO:0006914 autophagy; GO:0007040 lysosome organization; GO:0005773 vacuole; GO:0005764 lysosome | CL:0000540 neuron | UBERON:0000955 brain | (nowak2023atrophin‐1functionand pages 4-5) |
| Pathway | Calcium signaling and neuronal excitability may be perturbed, including reported **ITPR1** downregulation; this may contribute to cerebellar dysfunction, myoclonus, and seizures, especially in juvenile-onset disease. | GO:0007204 positive regulation of cytosolic calcium ion concentration; GO:0006816 calcium ion transport | CL:0000540 neuron; CL:0000127 Purkinje cell | UBERON:0002037 cerebellar cortex | (nowak2023atrophin‐1functionand pages 7-8, nowak2023atrophin‐1functionand pages 4-5) |
| Cellular / network | Neurons are especially susceptible to polyQ-mediated toxicity, and DRPLA likely reflects selective vulnerability within cerebello-basal ganglia-thalamic circuitry rather than uniform brain involvement. Repeat-length-dependent phenotypes support circuit-level toxicity. | GO:0050890 cognition; GO:0007611 learning or memory; GO:0050804 modulation of chemical synaptic transmission | CL:0000540 neuron | UBERON:0000955 brain; UBERON:0001896 dentate nucleus; UBERON:0001874 globus pallidus; UBERON:0002038 thalamus | (prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4, nowak2023atrophin‐1functionand pages 2-2) |
| Tissue | Neuropathology prominently affects the **dentate nucleus**, **globus pallidus** (especially the lateral segment), **subthalamic nucleus**, brainstem, and cerebral/cerebellar white matter. These tissue-level changes correspond to ataxia, chorea, cognitive decline, and epilepsy. | GO:0014003 oligodendrocyte development; GO:0042552 myelination; GO:0007417 central nervous system development | CL:0000540 neuron; CL:0000127 Purkinje cell; CL:0002603 oligodendrocyte | UBERON:0001896 dentate nucleus; UBERON:0001874 globus pallidus; UBERON:0001906 subthalamic nucleus; UBERON:0002298 brainstem; UBERON:0001348 white matter | (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 2-2) |
| Imaging / biomarker | Ongoing prospective natural-history work operationalizes downstream tissue injury using **MRI atrophy** and fluid biomarkers. The DRPLA NHBS measures atrophy particularly in the **brainstem**, **superior cerebellar peduncle**, **cerebellum**, and **thalamus**, and tracks **plasma/CSF NfL** as a biomarker of neurodegeneration. | GO:0097421 liver?; GO:0042552 myelination; GO:0007409 axonogenesis; GO:0005886 plasma membrane | CL:0000540 neuron; CL:0000127 Purkinje cell | UBERON:0002298 brainstem; UBERON:0011177 superior cerebellar peduncle; UBERON:0000073 cerebellum; UBERON:0001897 thalamus | (NCT06273150 chunk 1) |
| Therapeutic mechanism | Preclinical evidence supports targeting the repeat itself: the small molecule **naphthyridine-azaquinolone (NA)** binds slipped CAG-repeat structures, induces repeat contraction, reduces mutant ATN1 aggregation, and improves motor coordination in a DRPLA mouse model. This supports somatic repeat instability as a disease-modifying target. | GO:0006281 DNA repair; GO:0036297 interstrand cross-link repair; GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process | CL:0000540 neuron | UBERON:0002435 striatum; UBERON:0000955 brain | (hasuike2022cagrepeatbindingsmall pages 1-2, hasuike2022cagrepeatbindingsmall pages 2-3) |
| Translational / systems | Real-world DRPLA research infrastructure now includes patient registry, iPSC and fibroblast resources, and humanized mouse models to connect upstream molecular mechanisms with longitudinal clinical outcomes and therapy development, especially **ATN1-lowering** strategies. | GO:0007399 nervous system development; GO:0031644 regulation of neurological system process | CL:0000540 neuron; CL:0002327 fibroblast | UBERON:0000955 brain | (prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4) |


*Table: This table summarizes DRPLA mechanisms across genetic, protein, cellular, pathway, and tissue levels, with suggested ontology terms and anatomical mappings. It is useful for converting narrative disease biology into structured knowledge-base annotations linked to supporting evidence.*

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- Primary system affected: **central nervous system** (chaudhry2021drplaunderstandingthe pages 1-3).

### 7.2 Tissue/cell/anatomical localization (from retrieved sources)
- Key structures: cerebellum (dentate nucleus), basal ganglia (globus pallidus), subthalamic nucleus, brainstem, cerebral/cerebellar white matter (nowak2023atrophin‐1functionand pages 2-2, chen2024dentatorubralpallidoluysianatrophya pages 3-5).
- Imaging correlates: progressive brainstem and cerebellar atrophy and widely distributed white-matter lesions (including thalamus and cerebellum) (chen2024dentatorubralpallidoluysianatrophya pages 3-5).

The DRPLA natural history/biomarker study operationalizes structural degeneration by focusing on atrophy in **brainstem, superior cerebellar peduncle, cerebellum, and thalamus** (NCT06273150 chunk 1).

---

## 8. Temporal Development

### 8.1 Onset
- Typical mean/median onset reported around **~31 years** across reviews (nowak2023atrophin‐1functionand pages 1-2, chen2024dentatorubralpallidoluysianatrophya pages 3-5).
- Clinical categories described in a 2024 case review: juvenile (<20), early adult (20–40), and late adult (>40) (chen2024dentatorubralpallidoluysianatrophya pages 3-5).

### 8.2 Progression
DRPLA is progressive; repeat length correlates with earlier onset, more severe phenotype, and poorer prognosis (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 1-2).

A striking example of early-onset severity is the 98-repeat infantile case, which presented at 4 months and had fatal outcome at 17 months (baide‐mairena2023infantile‐onsetparkinsonismdyskinesia pages 1-3).

---

## 9. Inheritance and Population

### 9.1 Inheritance pattern
- **Autosomal dominant** inheritance (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4).
- **Anticipation**: symptoms can appear earlier and more severely in subsequent generations, with paternal transmission often more prominent (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4).

### 9.2 Epidemiology (statistics)
- Japan: estimated incidence/prevalence reported as **2–7 per million** (chaudhry2021drplaunderstandingthe pages 1-3, nowak2023atrophin‐1functionand pages 1-2, prades2024establishingresourcesand pages 2-4).
- In Japan, DRPLA is described as accounting for approximately **7.3–20%** of autosomal dominant SCA in some cohorts/reports (chaudhry2021drplaunderstandingthe pages 1-3).
- Regional frequencies in SCA cohorts reported in the neurology update include: Singapore **3.4%**, Korea **3.4%**, China **1%**, Brazil **0.14%**, Venezuela **3.1%** (chaudhry2021drplaunderstandingthe pages 1-3).
- Europe: a 2003 study analyzing 809 European index ataxia cases estimated DRPLA frequency as **0.25%** in autosomal dominant cerebellar ataxia families and **0.25%** in sporadic progressive ataxia cases, emphasizing very low prevalence in that setting (Arch Neurol. 2003; https://doi.org/10.1001/archneur.60.8.1097) (ber2003prevalenceofdentatorubralpallidoluysian pages 1-2).

---

## 10. Diagnostics

### 10.1 Current best-practice diagnostic strategy (from 2024 sources)
Recent hereditary ataxia diagnostic guidance (2024) stresses that adult-onset hereditary cerebellar ataxia workups often require (i) targeted testing for STR expansions (including DRPLA) plus (ii) sequencing approaches for conventional variants, and highlights long-read sequencing as a likely future transformer of diagnostic yield (https://doi.org/10.1007/s12311-024-01703-z) (rudaks2024anupdateon pages 1-2, rudaks2024anupdateon pages 10-12).

### 10.2 Structured diagnostic tests table

| Diagnostic domain | Test / approach | What it detects or assesses in DRPLA | Key findings / practical use | Limitations / notes |
|---|---|---|---|---|
| Confirmatory genetics | **ATN1 CAG repeat sizing** by targeted repeat-expansion testing (PCR/capillary electrophoresis; orthogonal confirmation) | Detects pathogenic CAG expansion in **exon 5 of ATN1** | Central confirmatory test for suspected DRPLA; reviewed sources note normal alleles typically **6-35**, incomplete penetrance around **35-47**, and full penetrance generally at **>=48** repeats. Case reports show diagnosis from pathogenic repeat sizes such as **62 repeats**. Recommended early in the workup of hereditary ataxia or compatible multisystem neurodegenerative phenotypes. (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, chen2024dentatorubralpallidoluysianatrophya pages 1-2) | First-line test when phenotype/family history suggests DRPLA; molecular testing in European ataxia cohorts may be prioritized when ataxia co-occurs with **chorea, dementia, or myoclonic epilepsy**. (ber2003prevalenceofdentatorubralpallidoluysian pages 1-2) |
| Expanded genetic screening | **STR analysis from exome data** using tools such as ExpansionHunter + REViewer | Screens exome datasets for pathogenic repeat expansions, including **ATN1** | 2024 study showed that adding STR analysis to exome pipelines identified previously missed diagnoses, including **3 DRPLA cases**, supporting exome-based STR calling as a useful secondary diagnostic strategy in undiagnosed neurogenetic disease. (yoon2024diagnosticupliftthrough pages 1-2) | Not a replacement for orthogonal confirmation; coverage and mapping limitations can produce false positives/false negatives, so confirmatory repeat testing remains necessary. (yoon2024diagnosticupliftthrough pages 1-2) |
| Future/advanced genetics | **Long-read sequencing** | Improved characterization of repeat expansions and complex variant structure | 2024 hereditary ataxia review highlights long-read sequencing as a likely transformative technology for adult-onset hereditary ataxias because it can better resolve STR expansions than standard short-read methods; relevant when routine STR testing and NGS are nondiagnostic or when multiple variant classes are suspected. (rudaks2024anupdateon pages 1-2, rudaks2024anupdateon pages 10-12) | Not yet standard in many clinical settings; access and implementation remain limited. (rudaks2024anupdateon pages 1-2, rudaks2024anupdateon pages 10-12) |
| Clinical diagnostic framing | **Phenotype-led diagnostic assessment** | Integrates age at onset, movement disorder pattern, epilepsy, cognition, psychiatric features, family history, and ancestry | DRPLA should be considered in patients with juvenile-onset **epilepsy/myoclonus/ataxia** or adult-onset **ataxia, choreoathetosis, cognitive decline, psychiatric symptoms**, especially with autosomal dominant family history or anticipation. (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, prades2024establishingresourcesand pages 2-4) | No universally standardized standalone clinical criteria were identified in the retrieved DRPLA literature; diagnosis remains genotype-supported. (chen2024dentatorubralpallidoluysianatrophya pages 3-5) |
| Neuroimaging | **Brain MRI** | Assesses structural changes and supports differential diagnosis | Common findings include **brainstem and cerebellar atrophy** and widespread **cerebral/cerebellar white-matter lesions**; lesions may involve the **cerebrum, brainstem, thalamus, and cerebellum**. MRI abnormalities may be mild early and more nonspecific later, so imaging is supportive rather than definitive. (chen2024dentatorubralpallidoluysianatrophya pages 3-5, chaudhry2021drplaunderstandingthe pages 1-3) | MRI is variable across stage and age group; not pathognomonic, and early imaging may be subtle. (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5) |
| Imaging biomarkers in current research | **Volumetric MRI / longitudinal atrophy measurement** | Tracks disease progression and candidate trial endpoints | The ongoing natural-history/biomarker study uses MRI to quantify atrophy over 3 years, particularly in the **brainstem, superior cerebellar peduncle, cerebellum, and thalamus**, indicating these are current real-world imaging biomarker targets. (NCT06273150 chunk 1) | Research-use longitudinal biomarker strategy; not yet a validated standalone diagnostic biomarker. (NCT06273150 chunk 1) |
| Epilepsy workup | **EEG and seizure phenotyping** | Characterizes seizure type, burden, and electroclinical pattern, especially in juvenile-onset disease | Seizures are common in juvenile-onset DRPLA; epilepsy evaluation is therefore important in suspected pediatric/juvenile cases and in adults with myoclonus or unexplained seizures plus ataxia/cognitive decline. Current interventional ASO work in one participant uses **EEG-measured seizure length** and seizure tracking as primary outcomes, underscoring clinical relevance. (chaudhry2021drplaunderstandingthe pages 1-3, NCT07084311 chunk 1) | EEG findings are useful for symptom characterization and treatment monitoring but are not diagnostic of DRPLA without molecular confirmation. (NCT07084311 chunk 1, chaudhry2021drplaunderstandingthe pages 1-3) |
| Differential-diagnosis testing strategy | **Hereditary ataxia workflow**: common SCA repeat panel + DRPLA testing, then NGS/WES/WGS if negative | Distinguishes DRPLA from other dominant and sporadic ataxias | 2024 ataxia guidance recommends testing for common dominant STR ataxias and **DRPLA** early in adults with hereditary cerebellar ataxia, followed by broader sequencing if repeat expansion testing is negative. (rudaks2024anupdateon pages 1-2, rudaks2024anupdateon pages 10-12) | DRPLA prevalence is low in Europe, so selective testing based on phenotype may improve efficiency in low-prevalence settings. (ber2003prevalenceofdentatorubralpallidoluysian pages 1-2) |
| Epidemiology-informed testing | **Targeted DRPLA testing in selected ataxia cohorts** | Helps decide when DRPLA testing is high yield | European prevalence study found DRPLA was very rare in a large White ataxia series (**0.25%** overall in both AD cerebellar ataxia families and sporadic ataxia cases), supporting selective testing when hallmark features such as **chorea, dementia, or myoclonic epilepsy** accompany ataxia. (ber2003prevalenceofdentatorubralpallidoluysian pages 1-2) | Low yield in unselected European ataxia cohorts; geographic/ancestral context matters. (chaudhry2021drplaunderstandingthe pages 1-3, ber2003prevalenceofdentatorubralpallidoluysian pages 1-2) |
| Fluid / molecular biomarkers | **Plasma and CSF NfL**, plus **tau, GFAP, UCH-L1** | Candidate biomarkers for neurodegeneration and progression | The DRPLA Natural History and Biomarkers Study prospectively measures **plasma/CSF neurofilament light (NfL)** as a primary biomarker and **tau, GFAP, UCH-L1** as secondary biomarkers, reflecting the current translational biomarker strategy in DRPLA. (NCT06273150 chunk 1) | These biomarkers are under study and not yet established as routine diagnostic standards for DRPLA. (NCT06273150 chunk 1) |
| Multimodal trial-readiness phenotyping | **SARA, INAS, upper-limb testing, speech and dysphagia batteries, biospecimen collection** | Quantifies clinical severity and progression for research and future trials | Current real-world implementation includes prospective annual assessments of **SARA**, non-ataxia signs, hand function, speech, dysphagia, and broad biosample collection (blood, serum, plasma, CSF, saliva, urine, feces, fibroblasts), creating a structured biomarker/endpoint framework for future interventional studies. (NCT06273150 chunk 1) | Primarily a research infrastructure rather than routine clinical diagnosis, but highly relevant for standardizing future care and trial endpoints. (NCT06273150 chunk 1) |


*Table: This table summarizes the main diagnostic modalities currently used or emerging for dentatorubral-pallidoluysian atrophy, spanning confirmatory genetics, imaging, EEG/epilepsy assessment, and biomarker strategies. It is useful for distinguishing routine clinical diagnosis from research-stage trial-readiness tools and shows where recent 2024 evidence is changing practice.*

### 10.3 Differential diagnosis (non-exhaustive)
DRPLA may mimic Huntington disease and other hereditary SCAs, particularly in adult-onset chorea/ataxia/dementia phenotypes (chaudhry2021drplaunderstandingthe pages 1-3, ber2003prevalenceofdentatorubralpallidoluysian pages 1-2). The low yield in unselected European ataxia cohorts supports selective testing when ataxia co-occurs with hallmark features such as chorea, dementia, or myoclonic epilepsy (ber2003prevalenceofdentatorubralpallidoluysian pages 1-2).

---

## 11. Outcome / Prognosis

The retrieved sources in this run mainly provide **qualitative** prognostic relationships rather than survival curves or standardized mortality rates.

- Repeat length is inversely correlated with age at onset and associated with more severe symptoms, long-term disability, and poorer prognosis in reviewed sources (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5).
- Extreme expansions can drive very early onset and fatal outcomes (e.g., 98 repeats infantile case) (baide‐mairena2023infantile‐onsetparkinsonismdyskinesia pages 1-3).

**Evidence gap:** robust statistics on life expectancy, survival rates, or longitudinal disability trajectories in large modern cohorts were not available in the retrieved full text for this run.

---

## 12. Treatment

### 12.1 Current standard of care
No disease-modifying therapy is available in the retrieved clinical literature; management is symptomatic and supportive, with emphasis on seizures/myoclonus (juvenile onset), movement disorders, and multidisciplinary care (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 1-2).

### 12.2 Treatment and experimental therapeutics table (with MAXO suggestions)

| Treatment / approach | Clinical role | Mechanism / rationale | Evidence type | Key evidence / implementation notes | Suggested MAXO term(s) | Citations |
|---|---|---|---|---|---|---|
| Levetiracetam | Symptomatic seizure control | Antiseizure medication used for DRPLA-associated epilepsy/myoclonus; favored over sodium-channel blockers in recent evidence synthesis | Systematic review / meta-analysis | In DRPLA-related epilepsy, levetiracetam was reported more frequently as effective than sodium channel blockers; epilepsy is especially important in juvenile-onset disease (chaudhry2021drplaunderstandingthe pages 1-3) | MAXO:0000106 seizure management; MAXO:0000127 anticonvulsant therapy | (chaudhry2021drplaunderstandingthe pages 1-3) |
| Perampanel | Symptomatic seizure control | AMPA-receptor antagonist antiseizure therapy for refractory seizures / myoclonus | Review citing case evidence | A 2023 review notes a 2017 single-patient experience in a 13-year-old with continuous myoclonic seizures in whom perampanel led to seizure cessation and some intellectual recovery, though it was not expected to alter neurodegeneration (nowak2023atrophin‐1functionand pages 7-8) | MAXO:0000106 seizure management; MAXO:0000127 anticonvulsant therapy | (nowak2023atrophin‐1functionand pages 7-8) |
| Buspirone | Symptomatic treatment for movement/balance symptoms | Serotonergic anxiolytic used empirically for symptom relief; mechanism in DRPLA not established | Case report | A 2024 case report described buspirone 5 mg three times daily, but after 6 months there was no significant symptomatic improvement in that patient (chen2024dentatorubralpallidoluysianatrophya pages 1-2) | MAXO:0001298 symptomatic treatment | (chen2024dentatorubralpallidoluysianatrophya pages 1-2) |
| Rehabilitation and multidisciplinary supportive care | Supportive / functional management | Physical, occupational, speech/swallowing, and general supportive care to preserve function and quality of life in progressive ataxia/neurodegeneration | Review / natural-history implementation | Current DRPLA research infrastructure includes upper-limb testing, speech assessment, and dysphagia assessment, supporting real-world multidisciplinary management needs; recent ataxia reviews emphasize physical, speech, and occupational therapy as core care in hereditary ataxias (NCT06273150 chunk 1, rudaks2024anupdateon pages 1-2) | MAXO:0000011 physical therapy; NCIT:C15986 occupational therapy; MAXO:0000370 speech therapy; MAXO:0001103 dysphagia management | (NCT06273150 chunk 1, rudaks2024anupdateon pages 1-2) |
| Personalized ATN1-targeting antisense oligonucleotide (nL-ATN1-002) | Experimental disease-modifying therapy | ATN1-lowering ASO intended to reduce mutant atrophin-1 expression and downstream toxicity | Interventional trial registry | Ongoing single-participant open-label Phase 1/2 study for genetically confirmed ATN1-related DRPLA; primary outcomes track seizure length/frequency and safety over 24 months (NCT07084311) (NCT07084311 chunk 1) | MAXO:0000197 antisense oligonucleotide therapy; MAXO:0001526 personalized therapy | (NCT07084311 chunk 1) |
| ATN1-lowering ASO strategies (programmatic approach) | Experimental disease-modifying therapy | Gene-silencing/downregulation approach targeting the root cause by lowering ATN1 expression | Patient-organization perspective / translational review | CureDRPLA prioritizes ATN1-downregulation strategies and has funded preclinical work and infrastructure to accelerate these therapies toward the clinic; no approved disease-modifying therapy currently exists (prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4) | MAXO:0000197 antisense oligonucleotide therapy; MAXO:0001445 gene expression inhibition therapy | (prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4) |
| CAG repeat-binding small molecule naphthyridine-azaquinolone (NA) | Experimental disease-modifying therapy | Binds slipped CAG-repeat DNA structures, induces repeat contraction, reduces mutant ATN1 aggregation, and improves motor phenotype in model systems | Preclinical mouse study | In DRPLA transgenic mice, long-term intracerebroventricular NA treatment produced repeat contraction and improved motor coordination, supporting somatic repeat instability as a therapeutic target (hasuike2022cagrepeatbindingsmall pages 1-2, hasuike2022cagrepeatbindingsmall pages 2-3) | MAXO:0000014 drug treatment; MAXO:0001445 gene expression inhibition therapy | (hasuike2022cagrepeatbindingsmall pages 1-2, hasuike2022cagrepeatbindingsmall pages 2-3) |
| Broader ASO / nucleic acid therapeutic development for polyQ disease | Experimental platform strategy | RNA-targeting therapies aim to lower toxic polyQ proteins across monogenic repeat-expansion disorders | Review | Polyglutamine disorders, including DRPLA, are considered strong candidates for ASO-based gene-targeting therapy because toxic gain-of-function is central and no disease-modifying therapy is approved (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 1-2) | MAXO:0000197 antisense oligonucleotide therapy | (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 1-2) |


*Table: This table summarizes current symptomatic management and emerging disease-modifying strategies for DRPLA, spanning antiseizure therapy, supportive rehabilitation, and experimental ATN1-targeted or repeat-targeted approaches. It is useful for distinguishing routine care from translational and clinical-trial-stage therapeutics.*

### 12.3 Recent developments (2023–2024 prioritized)
- **Personalized ASO clinical implementation:** a single-participant Phase 1/2 trial of a personalized ASO targeting ATN1 (start 2024-10-24; NCT07084311) uses seizure endpoints and safety/tolerability monitoring (NCT07084311 chunk 1).
- **Infrastructure toward trials:** CureDRPLA and collaborators report active support for natural history/biomarkers studies, patient registry development, and model generation, prioritizing ATN1-lowering strategies (prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4).

---

## 13. Prevention

No primary prevention (in the sense of preventing the mutation) is available for DRPLA; however, prevention of transmission and morbidity is possible via genetic services:
- **Genetic counseling** and **cascade testing** are relevant given autosomal dominant inheritance and anticipation (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4).
- Registry-based engagement and natural history programs (below) support secondary/tertiary prevention through earlier recognition, standardized monitoring, and future trial readiness (NCT05489393 chunk 1, NCT06273150 chunk 1).

---

## 14. Other Species / Natural Disease

No naturally occurring DRPLA-like disease in non-human species was identified in the retrieved sources for this run.

---

## 15. Model Organisms and Experimental Systems

### 15.1 Model types and resources (recent developments)
CureDRPLA-funded resources include:
- **Human cellular models:** patient iPSCs (heterozygous for a 67 CAG expansion) and fibroblast cultures (prades2024establishingresourcesand pages 2-4).
- **Mouse models:** a fully humanized mouse model expressing human ATN1 from the mouse locus (two lines expressing 112 and 70 pure CAG repeats) (prades2024establishingresourcesand pages 2-4).

A preclinical therapeutic study used DRPLA transgenic mice with multiple CAG-length sublines (including Q113), enabling repeat-length–dependent phenotyping and treatment testing (hasuike2022cagrepeatbindingsmall pages 2-3).

---

## Current applications and real-world implementations (clinical research ecosystem)

The following clinical studies and real-world infrastructures are active implementations relevant to DRPLA care and research.

| Study / implementation | NCT ID | Study type | Sponsor / organization | Status | Start date | Enrollment | Key outcomes / biomarkers / real-world use | URL |
|---|---|---|---|---|---|---|---|---|
| DRPLA Natural History and Biomarkers Study (DRPLA NHBS) | NCT06273150 | Observational, prospective cohort | University College London; collaborators: University of North Carolina, Chapel Hill and NYU Langone Health | Recruiting | 2022-05-01 | 225 | Annual 3-year natural history study in adult, pediatric, and remote arms; primary outcomes include SARA, brain MRI atrophy, and plasma/CSF neurofilament light (NfL); secondary measures include INAS, upper-limb function, speech battery, dysphagia assessment, and plasma/CSF tau, GFAP, and UCH-L1; biospecimens include blood, serum, plasma, CSF, saliva, urine, feces, and fibroblasts. Designed to support future DRPLA clinical trials (NCT06273150 chunk 1) | https://clinicaltrials.gov/study/NCT06273150 |
| CureDRPLA Global Patient Registry | NCT05489393 | Observational patient registry, prospective cohort | CureDRPLA; collaborator: Ataxia UK | Recruiting | 2021-03-01 | 100 | Longitudinal global registry collecting patient- or caregiver-reported demographics, diagnosis, medical history, activities of daily living, functional mobility, disease burden, quality of life, and health economics; available in multiple languages and intended to identify a well-characterized cohort for retrospective/prospective research and connect patients with future studies/trials. Represents real-world patient data infrastructure for DRPLA research (NCT05489393 chunk 1) | https://clinicaltrials.gov/study/NCT05489393 |
| Personalized Antisense Oligonucleotide for a Single Participant With ATN1 Gene Mutation | NCT07084311 | Interventional, open-label Phase 1/2, single participant | n-Lorem Foundation; collaborator: Hawaii Pacific Neuroscience | Active, not recruiting | 2024-10-24 | 1 | Personalized ASO (nL-ATN1-002) for genetically confirmed ATN1-related DRPLA; primary outcomes focus on seizure length by EEG and seizure frequency/medication use; secondary outcomes include quality of life and caregiver burden (CPCHILD), health/comorbidity checklist, and safety/tolerability monitoring with neurologic exams and laboratory/CSF assessments over 24 months. Real-world implementation of individualized ASO therapy in ultra-rare disease (NCT07084311 chunk 1) | https://clinicaltrials.gov/study/NCT07084311 |


*Table: This table summarizes key DRPLA clinical research and implementation efforts spanning natural history/biomarker studies, a global patient registry, and a personalized ASO interventional trial. It is useful for understanding the current translational landscape, including recruitment status, biomarkers, and trial-readiness infrastructure.*

### Visual evidence: CureDRPLA resources and ecosystem
CureDRPLA’s overview figure and its table of funded resources (including patient iPSCs, humanized mice, and natural history/biomarker study elements) provide a concise depiction of the field’s current translational infrastructure (prades2024establishingresourcesand media bcf421d5, prades2024establishingresourcesand media b4717146).

---

## Expert opinions and analysis (authoritative sources)

- A 2024 neurology review frames a central barrier to therapy development as “the rarity of the condition and the wide global distribution of patients and families,” and positions natural history and biomarker development as necessary precursors to ASO trials (chaudhry2021drplaunderstandingthe pages 1-3).
- A 2024 patient-organization perspective emphasizes coordinated, multi-site research and prioritizes **ATN1-lowering** as a root-cause strategy, noting the need for registry and natural history work to enable trials (prades2024establishingresourcesand pages 1-2, prades2024establishingresourcesand pages 2-4).
- A 2024 adult-onset hereditary ataxia diagnostic review argues that implementing advanced sequencing approaches (including long-read sequencing) could transform diagnostic yield for STR expansion disorders, explicitly including DRPLA (rudaks2024anupdateon pages 1-2).

---

## Key data points (quick reference; statistics from recent/authoritative sources)
- Japan incidence/prevalence estimate: **2–7 per million** (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4, nowak2023atrophin‐1functionand pages 1-2).
- Europe ataxia cohort (2003) DRPLA frequency: **0.25%** in AD ataxia families and **0.25%** in sporadic progressive ataxia cases (ber2003prevalenceofdentatorubralpallidoluysian pages 1-2).
- Molecular thresholds: normal ~**6–35 CAG**, incomplete penetrance **35–47**, full penetrance **≥48** (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5, nowak2023atrophin‐1functionand pages 1-2).
- Extreme expansion example: **98 CAG repeats** infantile case (published Jul 2023; https://doi.org/10.1002/acn3.51858) (baide‐mairena2023infantile‐onsetparkinsonismdyskinesia pages 1-3).
- 2024 exome-STR pipeline diagnostic gain: STR analysis of 6099 exomes from 2510 families gave a **0.28% diagnostic gain (7/2510)**; identified **DRPLA in n=3** individuals (published online 2 Feb 2024; https://doi.org/10.1038/s41431-024-01542-w) (yoon2024diagnosticupliftthrough pages 1-2).

---

## Disease identifiers and nomenclature summary

| Disease name | Common synonyms / alternative names | OMIM / MIM | MONDO | Orphanet | Causal gene | Inheritance | Key notes |
|---|---|---|---|---|---|---|---|
| Dentatorubral-pallidoluysian atrophy | DRPLA; dentatorubral pallidoluysian atrophy; hereditary DRPLA; classified within the spinocerebellar ataxia group / autosomal dominant cerebellar ataxia type IV in disease mappings (chaudhry2021drplaunderstandingthe pages 1-3, OpenTargets Search: Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1) | MIM/OMIM #125370 (prades2024establishingresourcesand pages 1-2) | MONDO:0007435 / MONDO_0007435 (OpenTargets Search: Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1) | Orphanet 101 / Orphanet_101 (OpenTargets Search: Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1) | ATN1 (atrophin-1), chromosome 12p13.31; disease-causing CAG repeat expansion in exon 5 (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4) | Autosomal dominant (chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4) | Ultra-rare neurodegenerative polyglutamine disorder characterized by ataxia, cognitive decline, myoclonus, chorea, epilepsy, and psychiatric manifestations; full penetrance typically reported at >=48 CAG repeats, with incomplete penetrance at 35-47 repeats in reviewed sources (prades2024establishingresourcesand pages 1-2, chaudhry2021drplaunderstandingthe pages 1-3, prades2024establishingresourcesand pages 2-4) |


*Table: This table summarizes the core disease-normalization fields for dentatorubral-pallidoluysian atrophy, including accepted identifiers, synonyms, causal gene, and inheritance. It is useful for building a standardized disease knowledge base entry anchored to curated and review-supported sources.*

---

## Limitations of this report (evidence availability)
- **ICD-10/ICD-11 and MeSH IDs** were not found in the retrieved full-text evidence for this run and therefore are not asserted here.
- **Quantitative prognosis (survival, life expectancy, mortality rates)** is not well supported by the retrieved corpus; most prognostic evidence here is genotype–phenotype correlation (repeat length vs onset/severity) (chaudhry2021drplaunderstandingthe pages 1-3, chen2024dentatorubralpallidoluysianatrophya pages 3-5).



References

1. (chaudhry2021drplaunderstandingthe pages 1-3): Aiysha Chaudhry, Alkyoni Anthanasiou-Fragkouli, and Henry Houlden. Drpla: understanding the natural history and developing biomarkers to accelerate therapeutic trials in a globally rare repeat expansion disorder. Journal of Neurology, 268:3031-3041, Oct 2021. URL: https://doi.org/10.1007/s00415-020-10218-6, doi:10.1007/s00415-020-10218-6. This article has 31 citations and is from a domain leading peer-reviewed journal.

2. (nowak2023atrophin‐1functionand pages 1-2): Bartosz Nowak, Emilia Kozlowska, Weronika Pawlik, and Agnieszka Fiszer. Atrophin‐1 function and dysfunction in dentatorubral–pallidoluysian atrophy. Movement Disorders, 38:526-536, Feb 2023. URL: https://doi.org/10.1002/mds.29355, doi:10.1002/mds.29355. This article has 25 citations and is from a highest quality peer-reviewed journal.

3. (OpenTargets Search: Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1): Open Targets Query (Dentatorubral-pallidoluysian atrophy,DRPLA-ATN1, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (prades2024establishingresourcesand pages 1-2): Silvia Prades, Andrea Compton, and Jeffrey B. Carroll. Establishing resources and increasing awareness to advance research on dentatorubral-pallidoluysian atrophy toward a treatment: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241249189, doi:10.1177/26330040241249189. This article has 1 citations.

5. (prades2024establishingresourcesand pages 2-4): Silvia Prades, Andrea Compton, and Jeffrey B. Carroll. Establishing resources and increasing awareness to advance research on dentatorubral-pallidoluysian atrophy toward a treatment: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241249189, doi:10.1177/26330040241249189. This article has 1 citations.

6. (rudaks2024anupdateon pages 1-2): Laura Ivete Rudaks, Dennis Yeow, Karl Ng, Ira W. Deveson, Marina L. Kennerson, and Kishore Raj Kumar. An update on the adult-onset hereditary cerebellar ataxias: novel genetic causes and new diagnostic approaches. Cerebellum (London, England), 23:2152-2168, May 2024. URL: https://doi.org/10.1007/s12311-024-01703-z, doi:10.1007/s12311-024-01703-z. This article has 51 citations.

7. (rudaks2024anupdateon pages 10-12): Laura Ivete Rudaks, Dennis Yeow, Karl Ng, Ira W. Deveson, Marina L. Kennerson, and Kishore Raj Kumar. An update on the adult-onset hereditary cerebellar ataxias: novel genetic causes and new diagnostic approaches. Cerebellum (London, England), 23:2152-2168, May 2024. URL: https://doi.org/10.1007/s12311-024-01703-z, doi:10.1007/s12311-024-01703-z. This article has 51 citations.

8. (chen2024dentatorubralpallidoluysianatrophya pages 1-2): Xin Chen, Wenwen Xiang, Lijun Xu, Jiahao Zhao, Ye Yu, Qing Ke, Zhipeng Liu, and Li Gan. Dentatorubral-pallidoluysian atrophy: a case report and review of literature. Journal of Medical Case Reports, Sep 2024. URL: https://doi.org/10.1186/s13256-024-04745-3, doi:10.1186/s13256-024-04745-3. This article has 0 citations and is from a peer-reviewed journal.

9. (baide‐mairena2023infantile‐onsetparkinsonismdyskinesia pages 1-3): Heidy Baide‐Mairena, Arthur Coget, Nicolas Leboucq, Vincent Procaccio, Maud Blanluet, Pierre Meyer, Marie‐Claire Malinge, Marie‐Céline François‐Heude, Mathis Moreno, David Geneviève, Cecilia Marelli, and Agathe Roubertie. Infantile‐onset parkinsonism, dyskinesia, and developmental delay: do not forget polyglutamine defects! Annals of Clinical and Translational Neurology, 10:1937-1943, Jul 2023. URL: https://doi.org/10.1002/acn3.51858, doi:10.1002/acn3.51858. This article has 3 citations and is from a peer-reviewed journal.

10. (NCT07084311 chunk 1):  Personalized Antisense Oligonucleotide for A Single Participant With ATN1 Gene Mutation. n-Lorem Foundation. 2024. ClinicalTrials.gov Identifier: NCT07084311

11. (chen2024dentatorubralpallidoluysianatrophya pages 3-5): Xin Chen, Wenwen Xiang, Lijun Xu, Jiahao Zhao, Ye Yu, Qing Ke, Zhipeng Liu, and Li Gan. Dentatorubral-pallidoluysian atrophy: a case report and review of literature. Journal of Medical Case Reports, Sep 2024. URL: https://doi.org/10.1186/s13256-024-04745-3, doi:10.1186/s13256-024-04745-3. This article has 0 citations and is from a peer-reviewed journal.

12. (nowak2023atrophin‐1functionand pages 2-2): Bartosz Nowak, Emilia Kozlowska, Weronika Pawlik, and Agnieszka Fiszer. Atrophin‐1 function and dysfunction in dentatorubral–pallidoluysian atrophy. Movement Disorders, 38:526-536, Feb 2023. URL: https://doi.org/10.1002/mds.29355, doi:10.1002/mds.29355. This article has 25 citations and is from a highest quality peer-reviewed journal.

13. (hasuike2022cagrepeatbindingsmall pages 1-2): Yuhei Hasuike, Hana Tanaka, Terence Gall-Duncan, Mustafa Mehkary, Kazuhiko Nakatani, Christopher E. Pearson, Shoji Tsuji, Hideki Mochizuki, and Masayuki Nakamori. Cag repeat-binding small molecule improves motor coordination impairment in a mouse model of dentatorubral–pallidoluysian atrophy. Neurobiology of Disease, 163:105604, Feb 2022. URL: https://doi.org/10.1016/j.nbd.2021.105604, doi:10.1016/j.nbd.2021.105604. This article has 24 citations and is from a domain leading peer-reviewed journal.

14. (ber2003prevalenceofdentatorubralpallidoluysian pages 1-2): Isabelle Le Ber, Agnès Camuzat, Giovanni Castelnovo, Jean-Philippe Azulay, Pierre Genton, Jean-Louis Gastaut, Dominique Broglin, Pierre Labauge, Alexis Brice, and Alexandra Dürr. Prevalence of dentatorubral-pallidoluysian atrophy in a large series of white patients with cerebellar ataxia. Archives of Neurology, 60:1097, Aug 2003. URL: https://doi.org/10.1001/archneur.60.8.1097, doi:10.1001/archneur.60.8.1097. This article has 68 citations.

15. (NCT06273150 chunk 1):  Dentatorubral-pallidoluysian Atrophy Natural History and Biomarkers Study. University College, London. 2022. ClinicalTrials.gov Identifier: NCT06273150

16. (NCT05489393 chunk 1):  CureDRPLA Global Patient Registry. CureDRPLA. 2021. ClinicalTrials.gov Identifier: NCT05489393

17. (nowak2023atrophin‐1functionand pages 4-5): Bartosz Nowak, Emilia Kozlowska, Weronika Pawlik, and Agnieszka Fiszer. Atrophin‐1 function and dysfunction in dentatorubral–pallidoluysian atrophy. Movement Disorders, 38:526-536, Feb 2023. URL: https://doi.org/10.1002/mds.29355, doi:10.1002/mds.29355. This article has 25 citations and is from a highest quality peer-reviewed journal.

18. (nowak2023atrophin‐1functionand pages 7-8): Bartosz Nowak, Emilia Kozlowska, Weronika Pawlik, and Agnieszka Fiszer. Atrophin‐1 function and dysfunction in dentatorubral–pallidoluysian atrophy. Movement Disorders, 38:526-536, Feb 2023. URL: https://doi.org/10.1002/mds.29355, doi:10.1002/mds.29355. This article has 25 citations and is from a highest quality peer-reviewed journal.

19. (hasuike2022cagrepeatbindingsmall pages 2-3): Yuhei Hasuike, Hana Tanaka, Terence Gall-Duncan, Mustafa Mehkary, Kazuhiko Nakatani, Christopher E. Pearson, Shoji Tsuji, Hideki Mochizuki, and Masayuki Nakamori. Cag repeat-binding small molecule improves motor coordination impairment in a mouse model of dentatorubral–pallidoluysian atrophy. Neurobiology of Disease, 163:105604, Feb 2022. URL: https://doi.org/10.1016/j.nbd.2021.105604, doi:10.1016/j.nbd.2021.105604. This article has 24 citations and is from a domain leading peer-reviewed journal.

20. (yoon2024diagnosticupliftthrough pages 1-2): Jihoon G. Yoon, Seungbok Lee, Jaeso Cho, Narae Kim, Sheehyun Kim, Man Jin Kim, Soo Yeon Kim, Jangsup Moon, and Jong-Hee Chae. Diagnostic uplift through the implementation of short tandem repeat analysis using exome sequencing. European journal of human genetics : EJHG, 32:584-587, Feb 2024. URL: https://doi.org/10.1038/s41431-024-01542-w, doi:10.1038/s41431-024-01542-w. This article has 28 citations.

21. (prades2024establishingresourcesand media bcf421d5): Silvia Prades, Andrea Compton, and Jeffrey B. Carroll. Establishing resources and increasing awareness to advance research on dentatorubral-pallidoluysian atrophy toward a treatment: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241249189, doi:10.1177/26330040241249189. This article has 1 citations.

22. (prades2024establishingresourcesand media b4717146): Silvia Prades, Andrea Compton, and Jeffrey B. Carroll. Establishing resources and increasing awareness to advance research on dentatorubral-pallidoluysian atrophy toward a treatment: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241249189, doi:10.1177/26330040241249189. This article has 1 citations.
