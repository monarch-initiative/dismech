---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-04-14T17:04:55.642969'
end_time: '2026-04-14T17:11:01.207944'
duration_seconds: 365.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Delpire-McNeill Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Delpire-McNeill Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Delpire-McNeill Syndrome** covering all of the
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

<think>
The user is asking me to write a comprehensive research report on Delpire-McNeill Syndrome using the provided search results. Let me review what I have:

From the search results, I can see:
1. Delpire-McNeill Syndrome (DELMNES) is described as a neurodevelopmental disorder with variable manifestations
2. It's caused by de novo mutations in SLC12A2 gene
3. SLC12A2 encodes NKCC1 (Na-K-2Cl cotransporter)
4. Patients present with developmental delay, intellectual disability, autism features
5. Some patients have sensorineural hearing loss and vestibular problems
6. Multiple related syndromes exist: DFNA78 (hearing loss with vestibular areflexia), Kilquist syndrome (autosomal recessive)
7. The gene plays crucial roles in neurogenesis, endolymph production, and GABA signaling

I need to create a 10,000+ word comprehensive report covering all 15 sections outlined in the template. Let me structure this thoughtfully:

Major sections to cover:
1. Disease Information
2. Etiology
3. Phenotypes
4. Genetic/Molecular Information
5. Environmental Information (may be minimal)
6. Mechanism/Pathophysiology
7. Anatomical Structures Affected
8. Temporal Development
9. Inheritance and Population
10. Diagnostics
11. Outcome/Prognosis
12. Treatment
13. Prevention
14. Other Species/Natural Disease
15. Model Organisms

Let me plan the narrative flow and then write the full report with proper citations.
</think>

# Delpire-McNeill Syndrome: A Comprehensive Clinical and Molecular Overview

Delpire-McNeill Syndrome (DELMNES), also known as SLC12A2-related developmental delay-intellectual disability-sensorineural deafness syndrome, represents a rare neurodevelopmental disorder caused by de novo and rare germline mutations in the SLC12A2 gene, which encodes the sodium-potassium-2-chloride cotransporter-1 (NKCC1)[2][4][4]. The syndrome is characterized by highly variable manifestations ranging from mild to severe global developmental delay and intellectual disability, with affected individuals frequently presenting with delayed motor and speech development, with some patients experiencing sensorineural hearing loss and vestibular dysfunction as prominent features[2][4][11]. The disease exemplifies pleiotropic genetic pathology, where a single gene defect produces multiple, seemingly unrelated clinical features across diverse organ systems including the nervous system, inner ear, and secretory epithelia, reflecting the broad tissue distribution and multifunctional roles of NKCC1 in human physiology[3][4][4]. This report provides a comprehensive examination of Delpire-McNeill Syndrome across clinical, molecular, genetic, and mechanistic dimensions, incorporating recent literature from 2016 onwards that has fundamentally transformed our understanding of SLC12A2-associated disease.

## Disease Information and Nomenclature

Delpire-McNeill Syndrome represents a recently characterized neurodevelopmental disorder that was formally identified and named following the landmark 2020 publication by McNeill and colleagues describing de novo mutations in SLC12A2 in six children with developmental disorders[2][4][4]. The condition has been assigned multiple standardized identifiers reflecting its recognition in international disease classification systems and medical databases: OMIM entry 619083, Orphanet disease code ORPHA:633024, ICD-11 code LD90.Y, and MeSH classification entry C5436771[10][17]. The syndrome exists within a complex landscape of SLC12A2-related disorders, each with distinct inheritance patterns and clinical presentations despite sharing mutations in the same gene. The designation "Delpire-McNeill syndrome" honors Eric Delpire, whose foundational work in the 1990s established the critical role of NKCC1 in murine auditory and neurological systems, and Andrew McNeill, whose team provided the first clear human disease-disease association[2][8].

Alternative naming conventions have evolved alongside evolving clinical understanding. The condition is sometimes referred to as "SLC12A2-related autosomal dominant infantile-developmental delay-intellectual disability-sensorineural deafness syndrome" to emphasize its autosomal dominant inheritance through de novo mutations[10][17]. Importantly, this nomenclature must be distinguished from related but mechanistically and inheritantly distinct conditions caused by different SLC12A2 variants. Specifically, DFNA78 (hearing loss, autosomal dominant 78, OMIM 619081) refers to non-syndromic bilateral sensorineural hearing loss with vestibular areflexia caused by heterozygous missense variants primarily affecting exon 21 of SLC12A2, without associated neurodevelopmental features[2][5][20]. Additionally, Kilquist syndrome (OMIM not yet assigned at time of writing) represents a severe autosomal recessive condition resulting from biallelic loss-of-function mutations or deletions in SLC12A2, causing syndromic sensorineural hearing loss with global developmental delay, gastrointestinal abnormalities, and absent salivation[19][19].

The disease is classified as a rare genetic disorder, with prevalence estimates not yet precisely established given its recent description, though recognition and diagnosis are increasing with expanded use of exome and genome sequencing in developmental delay evaluation[2][3]. The syndrome is appropriately categorized as a Mendelian disorder following autosomal dominant inheritance through de novo mutations, with no evidence of autosomal recessive or X-linked inheritance patterns for the syndrome form, though recessive variants exist for Kilquist syndrome[2][11][17].

## Etiology: Genetic Causation and Molecular Origins

### The SLC12A2 Gene and NKCC1 Protein

Delpire-McNeill Syndrome is caused by de novo heterozygous loss-of-function mutations in the SLC12A2 gene (solute carrier family 12, member 2), located on chromosome 5 (NCBI Gene ID 20496, HGNC ID 10911)[2][4][11]. The SLC12A2 gene encodes the Na-K-2Cl cotransporter (NKCC1), a member of the cation-chloride cotransporter (CCC) family that catalyzes the electroneutral cotransport of sodium (Na+), potassium (K+), and two chloride (Cl−) ions across biological membranes[2][6][11]. NKCC1 functions as a secondary active transporter utilizing existing Na+ and K+ gradients to move Cl− into or out of cells, playing fundamental roles in regulating transepithelial ion movement, cell volume, chloride homeostasis, and neuronal excitability[6][11][12].

The NKCC1 protein contains 12 transmembrane domains organized with a large extracellular N-terminal domain and a cytoplasmic C-terminal domain[6][4]. Structural analyses have revealed that NKCC1 functions as a dimer with multiple ion binding sites organized around discontinuous regions in transmembrane helices TM1 and TM6[6]. The protein exhibits tissue-specific alternative splicing, most notably affecting exon 21, which encodes 17 amino acid residues in the cytoplasmic tail and is preferentially expressed in cochlear tissues, providing mechanistic insight into why certain SLC12A2 variants cause isolated hearing loss while others produce neurodevelopmental manifestations[2][5][20]. The protein's regulatory capacity is enhanced by phosphorylation at multiple conserved serine and threonine residues in the N-terminus, which increases transport activity through enhanced structural dynamics of the large cytoplasmic C-terminal domains[6].

### Pathogenic Variants and Functional Consequences

The de novo mutations identified in Delpire-McNeill Syndrome patients predominantly affect functionally important domains of the SLC12A2 gene, with a 9.62-fold enrichment of de novo mutations in SLC12A2 within the deciphering developmental disorders (DDD) cohort, indicating significantly elevated mutation burden compared to background population mutation rates (P = 2.71 × 10−6)[2][4][4]. Of the pathogenic variants characterized, spatial clustering analysis using Denovonear has demonstrated that the majority of de novo mutations fall into transmembrane domains, with observed spatial proximity within the protein structure greater than expected by chance (P = 0.027)[2][4].

Identified pathogenic variants have included missense mutations affecting evolutionarily conserved residues including p.(Ala327Val), p.(Arg410Gln), p.(Asn376Ile), p.(Ala379Pro), and p.(Glu980Lys), as well as protein-truncating variants including p.(Val1026Phe*fs*2) resulting from an 11-bp deletion in exon 22 that causes frameshift and truncation of the carboxy-terminal tail[2][8][4]. Functional studies employing standard K+ influx measurements in Xenopus laevis oocytes under both basal (isotonic) and stimulated (hypertonic) conditions have demonstrated that all tested variants significantly reduced NKCC1 cotransporter function compared to wild-type controls[2][4][4][11]. In patient-derived fibroblasts, K+ transport experiments revealed reduced total and NKCC1-mediated K+ influx, with loss of bumetanide response suggesting deficits in NKCC1 regulation[8].

GnomAD database analysis has revealed strong constraint for protein-truncating variants in SLC12A2 (58.7 expected versus 11 observed, pLI = 0.96, observed:expected ratio 0.19 [0.12–0.31]), indicating that complete loss of NKCC1 function is generally incompatible with normal human development when homozygous, contrasting with viable NKCC1 knockout mice[2][4][4][32]. However, missense SNVs show less stringent constraint (594 observed versus 430 expected, Z = 2.4, observed:expected 0.72 [0.67–0.78]), suggesting some redundancy or tolerance for missense variation in certain protein domains. Importantly, amino acids 1–836 encompassing the transmembrane domains show depletion of missense variants (observed 173, expected 294.8, ratio 0.58), indicating selective constraint of missense variation in functionally significant domains[2][4].

### De Novo Mutation Mechanism and Inheritance

All well-characterized cases of Delpire-McNeill Syndrome result from de novo mutations arising in the germline, with no identified familial cases resulting from parental carriers[2][4][11]. The de novo origin has been established through trio exome sequencing comparing affected children with both parents, demonstrating mutations absent in parental DNA[2][4][4]. The recurrence risk for affected parents is exceptionally low (<1/200) but not zero, as germline or gonadal mosaicism in parental gametes remains a theoretical possibility, though no documented cases have been reported[13][13].

Genetic heterozygosity is maintained in affected individuals through complete dominance of pathogenic alleles, as heterozygous mutations reduce rather than eliminate NKCC1 function[2][3][4]. The concept of haploinsufficiency remains actively debated in SLC12A2-related disease pathology, as evidence increasingly supports that single-allele mutations do indeed cause disease manifestations despite retention of one functional allele[3][32]. Notably, parents and other family members carrying identical mutations show remarkable phenotypic variability or absence of clinical features, suggesting incomplete penetrance and variable expressivity of heterozygous SLC12A2 mutations[3][32].

### Constraint Analysis and Population Frequency

Population database analysis using gnomAD has provided critical insights into genetic constraint and background variant frequency. The complete absence of homozygous loss-of-function variants in gnomAD (despite 26 loss-of-function variants identified) provides strong evidence that biallelic NKCC1 deficiency is incompatible with viable human development, consistent with disease severity observed in Kilquist syndrome patients[19][19][32]. Regarding missense variants, regional constraint analysis reveals differential prevalence across protein domains, with 35% of residues in functionally important transmembrane domains harboring missense variants compared to 43% in functionally insignificant domains (chi-squared, P = 0.0037), indicating selective evolutionary constraint for transmembrane region variants[2][4].

## Phenotypes and Clinical Manifestations

### Neurodevelopmental Features

The cardinal manifestation of Delpire-McNeill Syndrome is global developmental delay, with all affected individuals identified to date presenting with intellectual disability ranging from mild to severe[2][4][11][17]. Developmental delay affects all developmental domains and affects achievement of early developmental milestones, with particular vulnerability in motor development and speech acquisition[2][4][13][17]. Motor development is characteristically delayed, with affected children demonstrating delayed sitting and walking milestones; the median age of independent walking is not precisely reported in current literature but is notably delayed compared to population norms[13][17]. Early motor abnormalities frequently include hypotonia, manifesting as floppiness in early infancy, progressing to hypertonia and spasticity in some patients, representing an unusual developmental pattern transition[4][13][17][13].

Speech and language development shows marked impairment in Delpire-McNeill Syndrome cohorts, with delayed speech onset and poor or absent functional communication in most affected individuals[2][4][13][17][13]. Three of six children with de novo SLC12A2 mutations identified in the McNeill cohort demonstrated autistic spectrum disorder features including social communication difficulties, restricted interests, and repetitive behaviors[2][4][11][4]. Intellectual disability severity varies substantially among affected individuals, ranging from mild delay requiring educational support to profound disability requiring intensive care and multiple services. One patient in the McNeill cohort demonstrated cerebral cortical dysplasia on brain MRI, representing structural brain malformation in association with developmental delay[2][4][4].

### Sensorineural Hearing Loss and Vestibular Dysfunction

Bilateral sensorineural hearing loss occurs in a subset of Delpire-McNeill Syndrome patients, with two of six children in the McNeill series presenting with this feature[2][4][4][11]. Additionally, three individuals with non-syndromic bilateral sensorineural hearing loss (BLSNHL) and vestibular areflexia have been identified with SLC12A2 variants, representing the DFNA78 phenotype[2][4][20]. Hearing loss ranges from mild to profound in severity, and age of onset correlates with variant location, with exon 21 variants particularly associated with congenital onset[2][5][20]. Vestibular areflexia, defined as bilateral loss of vestibular function with absent or severely reduced vestibular reflexes, frequently accompanies hearing impairment in SLC12A2-associated disease[2][5][20]. The vestibular dysfunction contributes to delayed motor development in affected children, particularly delayed walking, as balance maintenance requires intact vestibular system function[13][17][13].

### Multisystem Manifestations

Beyond neurological and auditory systems, SLC12A2 deficiency affects diverse organ systems through NKCC1's role in regulating fluid secretion and cell volume. One patient with a truncating SLC12A2 mutation presented with orthostatic intolerance, respiratory weakness, multiple endocrine abnormalities, pancreatic insufficiency, and multiorgan dysfunction involving gastrointestinal and bladder systems[8]. In the context of biallelic SLC12A2 loss-of-function (Kilquist syndrome), severe manifestations include absent or reduced salivation, absent or reduced tear production, absent or reduced sweat production, and respiratory complications mimicking cystic fibrosis with mucus plugging[19][19][29]. One patient with biallelic SLC12A2 loss-of-function mutations presented with neonatal Staphylococcus aureus parotitis with septicemia, central and obstructive apneas, disappearance of the Moro reflex, and profound hypotonia, with brain MRI revealing white matter and basal ganglia abnormalities[28][29][29].

## Genetic and Molecular Information

### SLC12A2 Gene Characteristics

The human SLC12A2 gene spans approximately 95 kilobases on chromosome 5 and contains 28 exons encoding an NKCC1 protein of 1196 amino acids[25][32]. Alternative splicing produces multiple protein isoforms, with exon 21 containing 48 base pairs encoding 16 amino acid residues found almost exclusively in inner ear/cochlear tissues, explaining tissue-specific phenotypes of certain mutations[2][5][20]. Gene expression analysis reveals that SLC12A2 demonstrates exceptionally high expression in radial glial cells during fetal brain development at 16–18 weeks post-conception compared to intermediate progenitor cells or mature neurons (Mann-Whitney U-test, Z = −3.3, P = 0.001 for radial glia versus intermediate progenitors; z = −5.2, P < 0.001 for radial glia versus neurons)[2][4][4][11][4]. Transcriptomic profiling of SLC12A2-expressing cells at 16–18 weeks gestation identified a transcriptomic program reflecting active neurogenesis, with high expression of genes associated with neural stem cell maintenance, cell division, and neuronal migration[2][4][4][4].

### Molecular Mechanisms of Pathogenicity

The primary molecular consequence of SLC12A2 mutations identified in Delpire-McNeill Syndrome is loss of NKCC1 cotransporter function, reducing the capacity for electroneutral Na+-K+-2Cl− transport[2][3][4][4][11]. This reduced function impairs multiple downstream processes critical for nervous system development. In radial glial cells, reduced SLC12A2 function inhibits neurogenesis through altered chloride homeostasis and disrupted GABA signaling, as loss of Slc12a2/NKCC1 in both murine models and cell systems has been demonstrated to inhibit neurogenesis[2][4][11][4][4]. The disrupted chloride homeostasis and dysregulated GABA signaling specifically affects the developmental excitatory-inhibitory GABA switch, wherein GABA normally stimulates chloride efflux from immature neurons due to elevated intracellular chloride concentrations maintained by NKCC1, producing depolarizing and excitatory effects that support neural development[2][4][11][4][4][28][29][29].

At the protein level, one identified truncated NKCC1 variant (p.Val1026Phe*fs*2) was found to be expressed and trafficked to the plasma membrane alongside wild-type NKCC1, yet no significant dominant-negative effect was observed in functional studies, suggesting the dominant effect arises primarily through haploinsufficiency rather than toxicity of mutant protein[8][32]. Conversely, heterozygous truncating variants in exon 22 have been associated with apical membrane mistargeting of NKCC1 in epithelial cells through loss of a di-leucine-like motif at the extreme carboxy-terminal end, potentially constituting significant dominant-negative effects in tissue-specific contexts[8][32].

### Tissue-Specific Pathogenic Mechanisms

The phenotypic pleiotropy of SLC12A2 mutations reflects tissue-specific roles of NKCC1 and differential sensitivity to reduced function across organ systems. In the developing nervous system, NKCC1 expressed in radial glial cells supports neurogenesis by maintaining elevated intracellular chloride and establishing the developmental chloride gradient necessary for appropriate GABAergic signaling during corticogenesis[2][4][4][11][4][4]. In the inner ear cochlea, NKCC1 expressed in marginal cells of the stria vascularis is essential for maintaining the ionic composition and volume of endolymph, the specialized K+-rich extracellular fluid bathing auditory sensory organs[2][14][9]. Reduced NKCC1 function in marginal cells leads to impaired endolymph production, reduced endocochlear potential, and ultimately hair cell degeneration and hearing loss[5][9][14][20].

In dorsal root ganglion (DRG) sensory neurons, NKCC1 maintains elevated intracellular chloride concentration, enabling GABA-mediated depolarization and presynaptic inhibition that modulates pain perception and sensory processing[12]. NKCC1 knockout mice demonstrate abnormal gait, impaired nociception, and altered sensory integration due to disrupted chloride homeostasis in sensory neurons[12]. In secretory epithelia including the salivary glands, pancreas, and trachea, NKCC1 expressed on basolateral membranes absorbs chloride that is subsequently secreted through apical transporters, supporting fluid secretion essential for maintaining airway clearance, salivary flow, and digestive function[8][19][19][29][32].

### Haploinsufficiency and Penetrance

Accumulating evidence increasingly supports the concept that SLC12A2 operates as a haploinsufficient gene in humans, whereby heterozygous mutations causing reduced but not absent NKCC1 function produce clinical disease[3][32]. However, haploinsufficiency demonstrates incomplete penetrance, as several family members carrying identical SLC12A2 mutations show no clinical phenotype, explaining variable expressivity within families[3][32]. Several hypotheses have been proposed to explain this incomplete penetrance, including genetic background effects from modifier genes, epigenetic regulation of SLC12A2 expression, and developmental compensatory mechanisms that may be variably effective among individuals[3][32].

## Pathophysiology and Molecular Mechanisms

### Corticogenesis and Neuronal Development

The primary pathophysiological mechanism through which SLC12A2 mutations produce neurodevelopmental phenotypes operates through disruption of corticogenesis and neuronal development during critical fetal periods. SLC12A2 is abundantly expressed in radial glial cells, the primary neural stem cells generating the cerebral cortex through repeated divisions producing first intermediate progenitor cells and subsequently differentiated neurons[2][4][4][11][4][4]. During radial glia proliferation and maintenance of stemness, NKCC1 maintains elevated intracellular chloride concentration that is critical for establishing the developmental chloride gradient and modulating GABAergic inhibitory neurotransmission[2][4][11][4]. Loss of Slc12a2/NKCC1 function in murine models has been conclusively demonstrated to inhibit neurogenesis through reduced proliferation of neural progenitors, suggesting that reduced human NKCC1 function compromises the expansion of neural progenitor pools during critical developmental windows[2][4][11][4][4].

The disrupted neurogenesis likely results from dysregulation of the developmental excitatory-inhibitory GABA switch, wherein immature neurons expressing high intracellular chloride maintained by NKCC1 experience GABA as depolarizing and excitatory, supporting migration and synaptic integration, while mature neurons with reduced NKCC1 and increased KCC2 expression experience GABA as hyperpolarizing and inhibitory[2][4][11][4][4][28][29][29]. Reduced NKCC1 function prematurely shifts this balance toward GABA inhibition in developing neurons, potentially suppressing migration, survival, and appropriate network formation. Furthermore, one patient with biallelic SLC12A2 loss-of-function mutations demonstrated hypomyelination on serial brain MRI with longitudinal evolution of white matter abnormalities, supporting a role for NKCC1 in oligodendrocyte development and myelin formation[28][29][29].

### Inner Ear Physiology and Endolymph Homeostasis

In the inner ear, NKCC1 plays an indispensable role in establishing and maintaining endolymph homeostasis, the specialized extracellular fluid environment critical for mechano-transduction of auditory and vestibular stimuli. Endolymph is characterized by exceptionally high potassium concentration and low sodium concentration, maintained through coordinated ion transport by multiple specialized epithelia[9][14][20]. NKCC1 expressed in marginal cells of the stria vascularis in the cochlea and dark cells of the vestibular system absorbs Na+, K+, and Cl− from the blood perilymph across the basolateral membrane[9][14][20]. The absorbed ions are subsequently secreted through various apical transporters back into endolymph, supporting the K+-rich ionic composition. NKCC1 knockout mice and zebrafish lte mutants demonstrate collapse of the otic vesicle with dramatic reduction in endolymph volume, reduced endocochlear potential, and rapid hair cell degeneration leading to profound sensorineural deafness and balance deficits[9][14][21].

SLC12A2 variants affecting exon 21, which encodes sequences critical for cochlear-specific NKCC1 function, cause non-syndromic sensorineural hearing loss with associated vestibular areflexia (DFNA78)[2][5][20]. Complete omission of exon 21 from Slc12a2 transcripts in homozygous murine models causes severe reduction in endolymph volume at postnatal day 1, reduced stria vascularis size, and absence of auditory brainstem responses at four weeks of age[9]. Heterozygous exon 21-skipping variants show more variable phenotypes, with some demonstrating normal hearing through sufficient cotransporter activity from shorter transcripts produced by cryptic splicing, while others demonstrate reduced hearing thresholds[9]. The tissue response to reduced stria vascularis cell size includes upregulation of claudin 9 (Cldn9) revealed by RNA sequencing, representing a compensatory mechanism attempting to restore osmotic balance[9].

### Ion Transport Defects and Cellular Dysfunction

Beyond the specific tissues described above, NKCC1 dysfunction affects diverse cellular processes through disrupted intracellular chloride homeostasis. NKCC1 mediates electroneutral Na+-K+-2Cl− transport using existing sodium and potassium gradients maintained by Na+/K+-ATPase, enabling accumulation of chloride ions within cells[6][11][14]. This accumulated chloride creates an electrochemical gradient permitting chloride efflux through various chloride channels, establishing the membrane potential and modulating neuronal excitability, cell volume, and GABA neurotransmission[2][4][11][12][4][28][29][29]. Reduced NKCC1 function decreases intracellular chloride accumulation and disrupts these fundamental cellular processes across diverse tissues.

In sensory neurons of the dorsal root ganglion, NKCC1 knockout mice demonstrate absence of chloride accumulation and loss of GABA-mediated depolarization critical for presynaptic inhibition and pain modulation[12]. Application of bumetanide, a selective NKCC1 inhibitor, in wild-type DRG neurons induces hyperpolarization of GABA reversal potential and decreased intracellular chloride, while in NKCC1 knockout neurons, bumetanide produces minimal additional effect[12]. These experiments firmly establish NKCC1 as the primary chloride loader in sensory neurons, with no compensatory pathways replacing this function[12].

### GABA Signaling Dysregulation

The dysregulation of GABAergic signaling represents a central pathophysiological mechanism in SLC12A2-associated disease affecting both developmental and mature neural function. During fetal and early postnatal development, GABA serves as an excitatory neurotransmitter through GABA receptors that are calcium-permeable chloride channels, with the reversal potential for chloride-mediated currents positive to resting membrane potential due to NKCC1-maintained elevated intracellular chloride[2][4][11][4][28][29][29]. This developmental excitatory GABA produces depolarization supporting neuronal migration, axon guidance, and synapse formation critical for normal brain development[2][4][11][4][28][29][29]. Reduced NKCC1 function prematurely suppresses developmental GABA excitation, impairing these critical developmental processes and producing neurodevelopmental delay.

Simultaneously, reduced NKCC1 function enhances GABA inhibition in developing brainstem respiratory networks, where NKCC1 and KCC2 expression shows developmental regulation during early postnatal life[28][29][29]. The resulting rapid increase of GABA inhibition may destabilize the respiratory network during critical developmental periods, potentially explaining the central apneas observed in neonates with biallelic SLC12A2 loss-of-function[28][29][29]. One patient with biallelic mutations presented with neonatal central and obstructive apneas, hypotonia, and loss of the Moro reflex during the first weeks of life, manifestations theoretically explained by enhanced brainstem GABA inhibition and disrupted development of critical reflexes in brainstem nuclei expressing high NKCC1[28][29][29].

## Anatomical and Cellular Locations

### Primary Affected Tissues

The clinical manifestations of Delpire-McNeill Syndrome reflect NKCC1 expression across multiple distinct tissues and organ systems. The **developing cerebral cortex** represents the primary site of SLC12A2 pathology in neurodevelopmental disease, with radial glial cells showing exceptionally high NKCC1 expression during the critical period of neurogenesis at 16–18 weeks post-conception[2][4][4][11][4][4]. These radial glial neural stem cells give rise through asymmetric division to intermediate progenitor cells and subsequently differentiated neurons that migrate along radial fibers to establish cortical layers[2][4][4][11][4][4]. NKCC1 expression decreases dramatically after neurogenesis concludes, with reduced expression in intermediate progenitors and mature neurons, explaining why most neurodevelopmental effects arise from prenatal NKCC1 disruption[2][4][4][11][4][4].

The **inner ear** represents another primary site of NKCC1 pathology, with expression in the marginal cells of the stria vascularis in the cochlea and dark cells of the vestibular system[2][5][9][14][20]. These specialized epithelial tissues generate and maintain endolymph through coordinated ion transport, with NKCC1 playing a rate-limiting role in endolymph production[2][5][9][14][20]. The vestibular system comprises the utricle, saccule, and semicircular canals lined with sensory hair cells that detect head position and motion, with vestibular dysfunction directly causing balance impairment and delayed motor development[2][5][20]. The cochlea contains the organ of Corti with auditory hair cells detecting sound vibrations, with hearing loss arising from reduced endolymph volume and hair cell degeneration secondary to NKCC1 dysfunction[2][5][9][14][20].

The **secretory epithelia** including salivary glands, pancreas, trachea, intestine, and sweat glands express NKCC1 on basolateral membranes supporting transepithelial fluid secretion[8][19][19][29][32]. In these tissues, NKCC1 absorbs electrolytes from blood that are subsequently secreted through apical transporters including CFTR in the cystic fibrosis pathway, supporting fluid secretion essential for mucosal lubrication and organ function[8][19][19][29][32].

### Cell Types and Subcellular Localization

At the cellular level, NKCC1 localizes to the plasma membrane where it functions as an ion cotransporter, with studies demonstrating basolateral membrane localization in epithelial tissues and neuronal soma and dendritic membrane localization in neurons[6][12][30][32]. One pathogenic variant associated with multisystem dysfunction demonstrated aberrant apical membrane mistargeting in epithelial cells through loss of a di-leucine-like motif, supporting intact NKCC1 trafficking machinery but disrupted targeting signals[8][32].

**Radial glial cells** represent the primary neural cell type affected in neurodevelopmental disease, as these neural stem cells demonstrate exceptionally high SLC12A2 expression compared to differentiated neurons[2][4][4][11][4][4]. Transcriptomic profiling specifically demonstrated that SLC12A2-expressing cells at 16–18 weeks gestation manifest a transcriptomic program reflecting active neurogenesis, with high expression of markers including EOMES, RBFOX1, and genes associated with neural stem cell self-renewal[2][4][4][4][4]. **Intermediate progenitor cells** show lower SLC12A2 expression than radial glia, contributing to the developmental stage-specific vulnerability to NKCC1 dysfunction[2][4][4][11][4][4].

**Sensory neurons** in the dorsal root ganglion express high levels of NKCC1 critical for maintaining elevated intracellular chloride, with knockout studies establishing NKCC1 as the sole significant chloride accumulator in these cells[12]. **Hair cells** in cochlea and vestibular sensory organs express reduced NKCC1 directly but depend critically on NKCC1 expressed in supporting epithelial cells for endolymph homeostasis[2][5][9][14][20].

## Temporal Development and Disease Course

### Prenatal Onset and Developmental Vulnerability

Delpire-McNeill Syndrome manifests as a developmental disorder beginning during prenatal neurogenesis, with critical vulnerability during the second trimester fetal period when corticogenesis is most active. The exceptionally high SLC12A2 expression in radial glial cells at 16–18 weeks post-conception indicates this as a critical window for NKCC1-dependent neurogenesis[2][4][4][11][4][4]. De novo mutations occurring in paternal or maternal gametes are inherited during conception and present from the earliest stages of neural development, with reduced NKCC1 function compromising neural progenitor expansion and neuronal migration throughout gestation.

The brain structural changes observed in affected individuals suggest prenatal pathology, with one patient demonstrating cerebral cortical dysplasia on imaging, a structural malformation reflecting disrupted neuronal migration during fetal development[2][4][4]. The hypomyelination observed on serial brain MRI in one patient with biallelic mutations suggests delayed oligodendrocyte development and myelination secondary to NKCC1 dysfunction[28][29][29].

### Infancy and Early Childhood Manifestations

Clinical manifestations of Delpire-McNeill Syndrome become evident in infancy as delayed developmental milestones become apparent. Affected infants typically present with hypotonia (decreased muscle tone) in early months of life, manifesting as floppiness and difficulty maintaining head control[2][4][13][17]. Parents report delayed achievement of motor milestones including rolling, sitting, and walking, with the specific ages of milestone achievement not precisely characterized in current literature but substantially delayed compared to population norms. Delayed speech development becomes apparent in the first to second years of life, reflecting both neurological dysfunction and hearing loss in some patients.

For patients with sensorineural hearing loss, manifestations may present as congenital profound deafness with detection through newborn screening programs or as progressive hearing loss identified during early childhood hearing evaluations[2][5][20]. Vestibular dysfunction contributes to delayed walking and balance difficulties, with some infants demonstrating vertigo, ataxia, or developmental coordination disorder.

One patient with biallelic SLC12A2 loss-of-function presented with severe neonatal complications including apneas, disappearance of the Moro reflex, and bacterial parotitis at day 5 of life, indicating particularly severe prenatal disruption and early postnatal dysfunction[28][29][29].

### Progressive and Chronic Course

Delpire-McNeill Syndrome follows a non-progressive chronic course in surviving individuals, with developmental delay and intellectual disability present from early infancy without regression. One eight-year-old patient with biallelic mutations demonstrated stable severe neurodevelopmental impairment without regression over eight years of observation[28][29][29]. Seizures occur in some patients, with several documented cases of epilepsy in the syndrome, though seizure frequency and severity vary substantially among affected individuals[2][4][13][17][13].

The chronic nature of cognitive and motor disability persists throughout childhood and into adulthood, with no documented cases of spontaneous improvement or recovery. Supportive care and intensive rehabilitation provide functional benefits but do not reverse underlying neurological dysfunction.

## Inheritance Patterns and Population Genetics

### Autosomal Dominant Inheritance Through De Novo Mutations

Delpire-McNeill Syndrome exhibits autosomal dominant inheritance exclusively through de novo mutations, with all well-characterized cases representing new mutations arising in paternal or maternal gametes[2][4][11][17]. Trio exome sequencing studies have universally demonstrated mutations present in affected children but absent in both heterozygous parents, establishing de novo origin[2][4][4]. No familial clustering has been identified among the described cases, though theoretically germline or gonadal mosaicism could produce multiple affected siblings from phenotypically normal parents, though no documented cases exist.

### Genetic Penetrance and Expressivity

The genetic penetrance of de novo SLC12A2 mutations appears incomplete, as several families with identified pathogenic mutations show remarkable phenotypic variation or apparent non-penetrance. Specifically, some family members carrying identical mutations show no clinical phenotype, though they typically retain two functional SLC12A2 alleles (one mutant, one wild-type)[3][32]. Fathers of affected patients carrying pathogenic SLC12A2 truncating or missense variants show no reported clinical phenotype despite carrying identical mutations, supporting incomplete penetrance of heterozygous mutations[3][32].

The variable expressivity of SLC12A2 mutations reflects substantial heterogeneity in clinical severity among patients carrying similar mutation types. Of six patients with de novo SLC12A2 mutations in the McNeill cohort, developmental delay ranged from mild to severe, with three showing autism spectrum features while three did not[2][4][4][11]. Two patients with protein-truncating variants showed subjectively more severe phenotypes than patients with missense variants, suggesting potential genotype-phenotype correlation, though larger patient series will be required for definitive conclusions[2][4][4].

### De Novo Mutation Rate and Population Frequency

The de novo mutation rate in SLC12A2 is significantly elevated compared to background mutation rates. A 9.62-fold enrichment of de novo mutations in SLC12A2 was demonstrated in the Deciphering Developmental Disorders (DDD) cohort of children with neurodevelopmental disorders, with statistical significance of P = 2.71 × 10−6 (after correction for multiple testing, P = 0.05)[2][4][4]. This enrichment indicates that SLC12A2 represents a bona fide developmental delay gene with substantial contribution to developmental delay etiology.

The population frequency of Delpire-McNeill Syndrome remains incompletely characterized given the recent description of the condition, but the rarity of SLC12A2 de novo mutations in general population controls and the extremely limited number of identified cases suggest this is a rare condition, likely with prevalence in the range of rare Mendelian disorders (<1 per 100,000 population).

### Geographic and Ethnic Distribution

Current literature does not provide detailed information regarding geographic distribution or ethnic-specific prevalence of SLC12A2-related developmental disease. Identified cases span multiple geographic regions including the United Kingdom, United States, Japan, Ghana, and Pakistan, suggesting no marked geographic clustering[2][4][5][20]. The application of whole genome and exome sequencing varies substantially across global populations, with higher diagnostic rates in well-resourced healthcare systems, potentially biasing ascertainment toward developed countries[2][20].

Recent studies emphasizing exome sequencing in understudied African populations have identified additional SLC12A2 variants associated with nonsyndromic autosomal dominant hearing loss (DFNA78) in Ghanaian and Pakistani families, indicating that SLC12A2-associated disease occurs across diverse populations[20]. Population-specific founder variants have not been identified to date, though future studies in isolated populations may reveal founder effects.

### Carrier Frequency and Genetic Counseling

The carrier frequency for SLC12A2 mutations remains extremely low in general populations, as gnomAD contains only 26 loss-of-function variants in SLC12A2 with no homozygotes detected, despite analysis of extremely large sample sizes[19][19][32]. For de novo mutations causing Delpire-McNeill Syndrome, the recurrence risk for parents of affected children is exceptionally low (<1/200 empiric risk), though theoretical possibility of germline mosaicism warrants consideration of parental genetic testing and counseling regarding low but nonzero recurrence risk[13][13].

## Diagnostic Approaches and Clinical Recognition

### Clinical Diagnosis and Differential Diagnosis

The clinical diagnosis of Delpire-McNeill Syndrome is suspected in children presenting with developmental delay and intellectual disability in the context of sensorineural hearing loss and vestibular dysfunction, though the syndrome must be distinguished from numerous other genetic causes of developmental delay with overlapping phenotypes. The constellation of global developmental delay, hearing loss, and vestibular dysfunction resembles syndromic hearing loss syndromes including Usher syndrome, though Usher syndrome typically involves progressive vision loss not characteristic of SLC12A2 disease[5]. Congenital infections including cytomegalovirus and rubella cause sensorineural hearing loss and developmental delay but typically include distinguishing systemic features including growth restriction, hepatosplenomegaly, or characteristic imaging findings[2].

Cerebral cortical dysplasia observed in one SLC12A2 patient requires differentiation from other genetic causes of focal cortical dysplasia including mTOR pathway mutations (AKT1, AKT3, DEPDC5, MTOR, NPRL2/3, PIK3CA, PIK3R2, RHEB, TSC1/2), ARX gene mutations, and other cortical malformation genes[2][30]. Spasticity and hypertonia observed in some SLC12A2 patients superficially resemble cerebral palsy from perinatal hypoxic-ischemic injury, though careful prenatal and perinatal history excluding significant asphyxia and normal neuroimaging excluding periventricular leukomalacia distinguishes genetic causes[4][13][17][13].

Autism spectrum disorder is observed in some Delpire-McNeill Syndrome patients, requiring recognition that neurodevelopmental delay with autistic features can result from monogenic genetic causes including SLC12A2[2][4][11]. Intellectual disability of genetic etiology must be distinguished from acquired causes including postnatal infections, traumatic brain injury, or metabolic derangement.

### Genetic Testing Strategy

The diagnosis of Delpire-McNeill Syndrome is established through identification of de novo SLC12A2 mutations through next-generation sequencing approaches. **Whole genome sequencing (WGS)** and **whole exome sequencing (WES)** represent the most effective approaches for identifying SLC12A2 mutations as part of comprehensive genetic evaluation of developmental delay, as these unbiased approaches detect both point mutations and small indels without requiring prior clinical hypothesis[2][4][11]. Trio exome or genome sequencing comparing affected child to both parents remains the gold standard for establishing de novo origin and excluding biallelic inheritance patterns.

**Gene panel sequencing** focused on genes associated with developmental delay and/or hearing loss including SLC12A2 can efficiently identify mutations if SLC12A2 is specifically included in panel design. **Single gene testing** of SLC12A2 is appropriate for targeted confirmation once mutations are identified through broader testing or for confirming suspected cases in research settings.

For patients with isolated sensorineural hearing loss and vestibular areflexia (DFNA78 phenotype), targeted gene panels enriched for hearing loss genes including SLC12A2 are appropriate first-line diagnostic approaches, given the high mutation burden in hearing loss genes and relatively limited differential diagnosis in this more specific phenotype[5][20]. Specifically, SLC12A2 exon 21 variants should be prioritized in sequencing panels for nonsyndromic sensorineural hearing loss, given the high prevalence of exon 21 variants in DFNA78 disease[5][20].

### Pathogenic Variant Classification

Identified SLC12A2 variants are classified according to the American College of Medical Genetics and Genomics (ACMG) and Association for Molecular Pathology (AMP) standards for variant interpretation[2][4]. De novo missense variants affecting evolutionarily conserved residues in functionally important transmembrane domains are classified as **pathogenic or likely pathogenic** based on strong evidence of de novo origin (ACMG criterion PS2), significant population rarity (typically absent or extremely rare in gnomAD, criterion PM2), computational prediction suggesting deleterious effects (criterion PP3), and demonstration of impaired protein function in cellular or in vitro systems (criterion PP2)[2][4]. Protein-truncating variants including frameshift mutations, nonsense mutations, and splice-altering variants affecting canonical splice sites are strongly predicted to cause loss of function, typically classified as **pathogenic** (ACMG criterion PVS1) when de novo[2][4].

All tested SLC12A2 variants identified in neurodevelopmental disease have demonstrated reduced cotransporter function in functional assays, satisfying the critical ACMG criterion (PP5 - reputable source recently reports variant as pathogenic) and supporting confident pathogenic classification[2][4]. For variants of uncertain significance (VUS), functional studies in Xenopus laevis oocytes or patient-derived cells can contribute critical evidence toward reclassification[2][4].

### Neuroimaging and Laboratory Findings

**Brain MRI** should be obtained in all Delpire-McNeill Syndrome patients to assess for structural brain abnormalities including cortical dysplasia, white matter abnormalities, myelination delays, or basal ganglia abnormalities. In one patient with biallelic mutations, serial brain MRI revealed evolution of white matter and basal ganglia abnormalities on initial imaging at two months of age with unchanged findings on follow-up imaging at four years, supporting prenatal origin with postnatal stability[28][29][29]. MRI sequences should include standard T1-weighted, T2-weighted, and FLAIR sequences, with MP2RAGE or other advanced sequences potentially improving detection of subtle cortical abnormalities[30].

**Cerebrospinal fluid (CSF) analysis** obtained in cases of severe disease may reveal elevated damage biomarkers suggesting neuronal injury. One patient with biallelic mutations demonstrated increased CSF damage biomarkers on analysis, suggesting active or recent neuronal injury, though CSF analysis is not routinely indicated for uncomplicated cases[28][29][29].

**Audiology evaluation** including age-appropriate hearing assessment (auditory brainstem response for infants, air and bone conduction testing for older children) should be performed in all patients, as sensorineural hearing loss occurs in a subset of cases. **Videonystagmography** or other vestibular testing can quantify vestibular areflexia and document balance dysfunction[5][20].

**Standard laboratory tests** including electrolytes, glucose, liver function tests, and kidney function should be obtained to assess for secondary metabolic derangement, though primary metabolic abnormalities are not characteristic of heterozygous SLC12A2 mutations.

### Omics-Based Diagnostic Approaches

**RNA sequencing** analysis of patient-derived fibroblasts or lymphoblastoid cell lines can evaluate for abnormal SLC12A2 transcript patterns, identifying potential effects of splice-altering variants on transcript structure and abundance[5]. **Proteomics** analysis can quantify NKCC1 protein abundance and identify potential abnormal protein trafficking or post-translational modifications associated with pathogenic variants.

## Prognosis and Long-term Outcomes

### Survival and Longevity

The prognosis for Delpire-McNeill Syndrome has not been comprehensively defined given the recent characterization of the condition and limited longitudinal follow-up data. Currently, no reported mortality specifically attributable to heterozygous SLC12A2 mutations in Delpire-McNeill Syndrome has been documented beyond one patient's complex multisystem presentation. Conversely, biallelic SLC12A2 loss-of-function mutations (Kilquist syndrome and related severe phenotypes) demonstrate substantially worse prognosis, with one patient succumbing to neonatal septicemia complicated by central apneas at 22 days of life, though direct causality to SLC12A2 deficiency versus septicemia remains unclear[28][29][29]. Another infant with neonatal presentation of parotitis and apneas survived to at least eight years of age with severe neurological disability[28][29][29].

Heterozygous Delpire-McNeill Syndrome patients appear to have normal or near-normal life expectancy, with no specific cause of death directly attributable to NKCC1 haploinsufficiency documented in the literature, though comprehensive longitudinal mortality data in larger cohorts is unavailable.

### Functional Outcomes and Disability

The functional outcomes in Delpire-McNeill Syndrome are substantially compromised by developmental delay and intellectual disability. Affected individuals typically require intensive educational support and multidisciplinary services including speech therapy, occupational therapy, and physiotherapy. Communication abilities are markedly affected, with most individuals developing limited or absent spoken language and many requiring augmentative alternative communication (AAC) devices to facilitate social interaction[13][17][13]. Motor abilities are substantially limited, with most individuals demonstrating delayed walking when it occurs at all, and some remaining non-ambulatory into adulthood[2][4][13][17].

The cognitive abilities of individuals with Delpire-McNeill Syndrome span a broad range from mild delay compatible with mainstream or modified classroom learning to profound intellectual disability requiring 24-hour care and assistance with activities of daily living[2][4][11][17]. Quality of life measures have not been formally quantified in published literature, though the multifaceted disability affecting cognition, communication, and motor function substantially impacts both affected individuals and family members providing care[13][17][13].

### Disease Progression and Complications

Delpire-McNeill Syndrome appears to follow a stable, non-progressive course without regression, distinguishing it from progressive neurodegeneration. One patient with eight-year follow-up demonstrated stable developmental status without decline, supporting chronicity without progression[28][29][29]. The constellation of complications relevant to severe developmental disability applies, including feeding difficulties, aspiration risk, infections secondary to poor hygiene due to motor disability, and potential behavioral or mood disorders associated with autism spectrum features.

For patients with hearing loss, sensorineural hearing loss is typically non-progressive after initial onset, though one case report of progressive hearing loss has been documented in DFNA78 families, warranting serial audiometry[5][20]. For patients with vestibular areflexia, balance dysfunction remains stable and lifelong, requiring ongoing accommodation and fall prevention strategies[5][20].

## Treatment Approaches and Therapeutic Options

### Symptomatic Management and Supportive Care

Currently, no disease-modifying therapies specifically targeting NKCC1 dysfunction have been approved or undergone substantial clinical trial evaluation for Delpire-McNeill Syndrome. Management is predominantly supportive, addressing individual symptoms and functional limitations. **Speech and language therapy** targets communication deficits, utilizing strategies to maximize functional communication through speech, sign language, or augmentative alternative communication devices[13][17][13]. **Occupational therapy** addresses activities of daily living, fine motor skills, and sensory integration, promoting maximal functional independence[13][17][13].

**Physiotherapy** focusing on stretching, strengthening, and mobility training addresses gross motor delay and spasticity when present, with goals of promoting walking when possible and maintaining joint health and preventing contractures[13][17][13]. **Hearing aids and cochlear implants** provide acoustic amplification or direct stimulation of the auditory nerve for patients with sensorineural hearing loss, though the benefits in the context of associated cognitive disability require individualized assessment[5][20][13].

### Seizure Management

For patients with seizures, **anticonvulsant medications** including standard first-line agents (levetiracetam, sodium valproate, oxcarbazepine) and second-line agents are employed based on seizure type and individual tolerance. The appropriateness of specific agents in the context of underlying NKCC1 dysfunction has not been specifically evaluated, though theoretically agents affecting GABA signaling might warrant careful consideration given the dysregulated GABA signaling underlying SLC12A2 pathology. Some anticonvulsants including phenobarbital interact with ion transporters, though specific interactions with NKCC1-related disease have not been documented[13][17][13].

### Respiratory and Secretion Management

Patients with respiratory complications including chronic airway secretion management benefit from **hypertonic saline inhalations** to mobilize secretions and prevent mucus plugging, a life-threatening complication in severe NKCC1 deficiency[28][29][29][13]. **Swallowing assessment** and **feeding support** including nasogastric tube feeding or gastrostomy tube placement prevent aspiration and ensure adequate nutrition in patients with severe swallowing dysfunction[28][29][29][13].

### Future Therapeutic Possibilities

**Ion channel modulators or transporters** represent potential future therapeutic approaches targeting NKCC1 dysfunction, though no agents specifically enhancing NKCC1 function have reached clinical trials. Theoretically, pharmacological agents increasing NKCC1 expression or activity could partially compensate for reduced cotransporter function. Conversely, **NKCC1 inhibitors** including bumetanide and furosemide cause reversible hearing loss in humans through reduced endolymphatic potential and would be expected to worsen NKCC1-associated disease[14][32].

**Gene therapy** approaches represent potentially transformative therapeutic options for future development. Viral vector-mediated SLC12A2 gene replacement therapy could theoretically restore NKCC1 function in affected neural and inner ear tissues. Adeno-associated virus (AAV) vectors with neuron-specific or cell-type specific promoters could target SLC12A2 gene delivery specifically to radial glial cells during critical neurogenic periods or to inner ear epithelia supporting endolymph production. However, substantial preclinical development would be required before clinical translation, given the narrow critical developmental windows for maximal therapeutic benefit and the challenges of achieving adequate gene delivery to target tissues.

## Prevention and Genetic Counseling

### Primary and Secondary Prevention

**Primary prevention** (preventing disease occurrence) is not applicable to Delpire-McNeill Syndrome, as de novo mutations arise unpredictably in parental gametes during conception, with no identifiable modifiable environmental risk factors or preventive interventions currently established. The spontaneous de novo mutation mechanism indicates that affected parents do not carry identifiable risks that could be modified to prevent disease in subsequent pregnancies.

**Secondary prevention** through early detection and intervention applies to affected infants and children. **Newborn hearing screening** can detect sensorineural hearing loss in affected newborns, enabling timely intervention with hearing aids or cochlear implant evaluation. Early developmental assessment and intervention services including speech, occupational, and physical therapy when initiated in infancy have been demonstrated to improve functional outcomes in developmental delay, though specific efficacy data in SLC12A2-related disease is unavailable. **Genetic diagnosis** established through molecular testing enables family counseling regarding recurrence risk and genetic anticipation in future pregnancies.

**Tertiary prevention** (preventing complications in affected individuals) includes multidisciplinary supportive care and disease-specific monitoring. Seizure prevention through appropriate anticonvulsant therapy, aspiration prevention through swallowing assessment and intervention, and respiratory support addressing airway management prevent acute life-threatening complications[28][29][29][13]. Regular audiology follow-up monitors for progressive hearing loss changes, and periodic neurodevelopmental assessment tracks developmental progress or regression[2][4][11][13].

### Genetic Counseling and Recurrence Risk

For families with a child affected by Delpire-McNeill Syndrome caused by de novo mutation, **genetic counseling** should address the de novo origin of the mutation, the extremely low recurrence risk for future siblings, and the minimal risk for parental germline mosaicism. The empiric recurrence risk is typically quoted as less than 1/200 given the theoretical possibility of germline mosaicism, though documented cases of multiple siblings with identical de novo SLC12A2 mutations are not reported[13][13].

**Prenatal diagnosis** through chorionic villus sampling (CVS) or amniocentesis with targeted SLC12A2 sequencing could theoretically identify affected pregnancies, though clinical utility would be limited given the variable expressivity of heterozygous mutations. **Preimplantation genetic diagnosis (PGD)** selecting embryos without the parental SLC12A2 mutation could prevent disease transmission in familial cases, though this approach would only be relevant if a parent had become affected with SLC12A2 disease and was at high risk for transmitting the mutation to offspring.

### Carrier Screening

General population **carrier screening** for SLC12A2 heterozygous mutations is not currently recommended or clinically implemented, as SLC12A2 heterozygous mutations cause dominant de novo disease rather than recessive disease with carrier screening implications. The rarity of SLC12A2 variants in general populations and the incompletely penetrant nature of heterozygous mutations make population-based carrier screening impractical.

## Model Organisms and Translational Research

### Mouse Models of SLC12A2 Dysfunction

**NKCC1 knockout mice** (Slc12a2 null mice) have provided foundational insights into SLC12A2 pathophysiology and remain critical models for disease understanding. The first Slc12a2 null mouse, generated in 1999, displayed profound sensorineural deafness with cochlear malformations, hair cell loss, and absence of auditory brainstem responses, directly demonstrating NKCC1's critical role in cochlear function[21][4][32]. Additionally, these null mice demonstrated balance deficits characterized as the "shaker/waltzer" phenotype with head shaking and circling behavior, reflecting vestibular dysfunction from endolymph collapse[19][21][4][19][32].

Behavioral phenotyping of NKCC1 knockout mice revealed abnormal gait and locomotion, with disrupted sensory perception and impaired nociception, consistent with NKCC1 dysfunction in dorsal root ganglion sensory neurons[12]. Reduced neuronal proliferation has been demonstrated in the lateral ganglionic eminence of null mice, and NKCC1 knockdown by short-hairpin RNA reduced neuronal proliferation in the murine subventricular zone, supporting a neurodevelopmental role[2][4][4]. However, comprehensive cognitive and neurobehavioral testing including learning and memory has not been extensively reported in these mice, potentially underestimating the neurodevelopmental consequences of complete NKCC1 loss.

Null mice additionally demonstrated gastrointestinal dysfunction including intestinal obstruction, consistent with secretory epithelial dysfunction[19][19][32]. Male reproductive dysfunction and infertility has also been documented in NKCC1 knockout mice, reflecting NKCC1 expression in testicular tissue and potential role in spermatogenesis[32].

### Conditional and Tissue-Specific Mouse Models

**Conditional Slc12a2 knockout mice** with tissue-specific deletion in particular cell types would provide valuable models of isoform-specific and developmental stage-specific disease mechanisms. Recent studies have generated pancreatic **β-cell-specific Slc12a2 knockout mice** (Slc12a2^βKO^) that developed reduced insulin responses to glucose, fasting hyperglycemia, and non-alcoholic fatty liver disease progression in overweight mice, suggesting roles for NKCC1 in beta-cell function and metabolic homeostasis[33]. These studies demonstrate NKCC1's contribution to insulin secretion and metabolic regulation independent of auditory and neurological systems.

### Zebrafish Models

The zebrafish **little ears (lte) mutant** represents an alternative genetic model of NKCC1 dysfunction, carrying mutation in zebrafish nkcc1 that causes collapse of the otic vesicle beginning at 3 days post-fertilization with apparent loss of endolymphatic fluid and over-inflation of the swim bladder[14]. The lte mutant demonstrates developmental vulnerability of endolymph to NKCC1 disruption, with endolymph collapse occurring postnatally rather than prenatally, reflecting different developmental timing in fish. Importantly, morpholino-mediated blocking of splicing at an ectopic site introduced by the lte mutation ameliorates ear collapse, demonstrating proof-of-concept for therapeutic splicing manipulation in NKCC1 disease[14].

### Cell Culture Models

**Patient-derived fibroblasts** obtained from affected individuals have been employed for functional studies of NKCC1 variants, demonstrating reduced K+ transport and altered bumetanide responses compared to controls[8][32]. **Lymphoblastoid cell lines** from affected patients provide renewable cell sources for molecular and biochemical studies. **Induced pluripotent stem cell (iPSC) lines** generated from patient fibroblasts represent emerging models enabling differentiation toward neural and auditory lineages to model developmental aspects of disease in human-derived systems[32].

**Xenopus laevis oocyte expression systems** have provided critical functional validation of SLC12A2 variants, permitting quantitative measurement of ion transport activity under standardized conditions[2][4][4][11]. Wild-type and mutant SLC12A2 cRNA injected into oocytes permit measurement of K+ influx under basal and hypertonic stimulation, with all characterized pathogenic variants demonstrating significantly reduced transport activity[2][4][4][11].

## Recent Developments and Current Research Frontiers

Recent investigations from 2023–2026 have substantially advanced understanding of SLC12A2-related disease mechanisms and disease spectrum. A 2023 comprehensive review examining NKCC1 in human disease explicitly addressed whether SLC12A2 operates as a haploinsufficient gene, concluding that "the preponderance of evidence suggests that the SLC12A2 gene is a human disease-causing and likely haploinsufficient gene that requires further investigation," supporting heterozygous mutations as bona fide disease-causing events[3][32]. This review synthesized extensive clinical and molecular data from diverse patient cases and animal models, providing authoritative perspective on penetrance, expressivity, and mechanistic understanding.

A 2024 case report documented a patient with profound congenital hearing loss and vestibular areflexia caused by a de novo SLC12A2 splice donor site variant (NM_001046.2: c.2977+4_2977+7del) causing in-frame skipping of exon 21, adding to evidence that loss of exon 21 specifically produces cochlear-restricted phenotypes[5]. This report emphasized the genetic heterogeneity of nonsyndromic sensorineural hearing loss and vestibular areflexia and recommended broad sequencing approaches when faced with this clinical scenario.

Comprehensive research on exon 21 pathophysiology has revealed that exon 21 encodes a critical region of only 48 base pairs encompassing 17 amino acid residues that is highly conserved between species and preferentially expressed in cochlear tissues, serving as a cochlear-specific functional domain essential for inner ear homeostasis[2][5][9][20]. Analysis of ten families with DFNA78 or syndromic hearing loss revealed that eight (80%) had variants within this 17-amino-acid region, suggesting this alternate domain is critical to transporter activity in the inner ear[20].

## Conclusion: Synthesis and Future Perspectives

Delpire-McNeill Syndrome represents a recently characterized neurodevelopmental disorder caused by de novo heterozygous mutations in SLC12A2 that exemplifies how a single gene mutation affecting a ubiquitously expressed ion transporter can produce pleiotropic clinical manifestations spanning nervous system development, auditory and vestibular function, and secretory epithelial physiology. The syndrome demonstrates that NKCC1 operates as a haploinsufficient human disease gene, with heterozygous loss-of-function mutations producing clinical disease despite retention of one functional allele. The variable expressivity and incomplete penetrance of heterozygous SLC12A2 mutations suggest complex genetic and epigenetic modifying factors that remain incompletely understood.

The primary pathophysiological mechanisms through which SLC12A2 mutations produce disease involve disruption of neurogenesis during critical fetal corticogenesis through dysregulation of the developmental GABA switch an