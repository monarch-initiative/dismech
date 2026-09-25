---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T19:48:08.266967'
end_time: '2026-09-23T19:55:06.156630'
duration_seconds: 417.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: O'Donnell-Luria-Rodan Syndrome
  mondo_id: MONDO:0032793
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 35
  total_cost_usd: 2.114426
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** O'Donnell-Luria-Rodan Syndrome
- **MONDO ID:** MONDO:0032793 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **O'Donnell-Luria-Rodan Syndrome** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

# O'Donnell-Luria-Rodan Syndrome (KMT2E-Related Neurodevelopmental Disorder): Comprehensive Research Report

## 1. Disease Information

**Overview.** O'Donnell-Luria-Rodan syndrome (ODLURO; also termed KMT2E-related neurodevelopmental disorder, KMT2E-NDD) is an autosomal dominant neurodevelopmental disorder caused by heterozygous pathogenic/likely pathogenic variants in *KMT2E* (lysine methyltransferase 2E, also known historically as *MLL5*) or by contiguous microdeletions of 7q22.2-q22.3 that encompass the gene. It is characterized principally by global developmental delay, speech delay, variably impaired intellectual development (typically mild-to-moderate), hypotonia, macrocephaly, a subtle but recognizable facial gestalt, functional gastrointestinal symptoms, sleep disturbance, and — in a substantial minority — autism spectrum disorder (ASD) and/or epilepsy (O'Donnell-Luria et al., *AJHG* 2019, PMID:31079897; Velmans et al., *J Med Genet* 2021, PMID:34321323; Pais, Rodan, O'Donnell-Luria, *GeneReviews* 2024, PMID:38648332).

The disorder was first delineated in 2019 by Anne O'Donnell-Luria and Lance Rodan (Boston Children's Hospital / Harvard Medical School / Broad Institute), using data assembled largely through Matchmaker Exchange, in a report of 38 individuals from 36 families (PMID:31079897). Earlier exome-sequencing studies (2012–2016) had already flagged *KMT2E* loss-of-function variants as an ASD risk-gene signal without recognizing a distinct syndrome (see Etiology/Genetic section). As of the most recent literature (2024–2025 cohort and case-series publications), well over 100 individuals have been reported worldwide.

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #618512 — O'DONNELL-LURIA-RODAN SYNDROME; ODLURO |
| OMIM (gene) | *608444 — KMT2E |
| MONDO | MONDO:0032793 |
| MedGen | C5193138 |
| HGNC (gene) | HGNC:18541 (KMT2E) |
| Gene location | 7q22.2–q22.3 |
| Reference transcript | NM_182931.2/.3 |
| GeneReviews | NBK602945 (PMID:38648332) |
| ClinGen gene-disease validity | "Definitive," gene *KMT2E* → "Complex neurodevelopmental disorder" MONDO:0100038, autosomal dominant, Intellectual Disability and Autism GCEP, 08/02/2022 |
| ClinGen dosage sensitivity | Haploinsufficiency score 3 ("Sufficient Evidence"); Triplosensitivity score 0 ("No Evidence"), scored specifically against the ODLURO phenotype, 12/29/2021 |

I did not find a dedicated Orphanet (ORPHA) code in the sources searched; OMIM/MONDO/MedGen appear to be the primary cross-references currently indexed. This should be treated as an open item rather than a confirmed absence — worth a direct Orphanet lookup at curation time.

**Synonyms:** ODLURO syndrome; KMT2E-related neurodevelopmental disorder (KMT2E-NDD); MLL5-related disorder (older literature uses the *MLL5* gene alias).

**Evidentiary basis.** All information below is derived from aggregated case-series/cohort publications (disease-level, retrospective ascertainment through clinical genetics services, ClinGen matchmaking, and research sequencing cohorts such as Deciphering Developmental Disorders/DDD and Simons Searchlight), not from a single large prospective natural-history study or individual-level EHR data. This matters for interpreting the frequency figures below — they are cohort proportions from case series of variable ascertainment, not population-based incidence/prevalence.

---

## 2. Etiology

**Disease causal factor: monogenic, autosomal dominant.** ODLURO is caused by heterozygous loss-of-function (predominantly) or missense (less common, more severe) variants in *KMT2E*, or by 7q22.2-q22.3 microdeletions removing *KMT2E* (and in larger deletions, neighboring genes). The disorder is **not** known to have environmental, infectious, or multifactorial causal contributions — it is a single-gene, largely de novo Mendelian disorder.

**Genetic risk factors:**
- **Causal variant class:** In the founding cohort (n=38), 30/38 (79%) carried protein-truncating variants (24 indels/frameshift, 4 nonsense, 2 splice-site), 4/38 (11%) carried missense variants, and 4/38 (11%) carried 7q22.2-q22.23 microdeletions (0.052–3.2 Mb) (PMID:31079897). In the second cohort (Velmans et al., n=18), variant types were 7 frameshift, 4 nonsense, 4 splice-site (including one activating a cryptic donor site), and 2 partial microdeletions (711 kb, 61 kb); 14/15 sequence variants were novel (PMID:34321323).
- **Inheritance:** Overwhelmingly **de novo**. In the 2019 cohort, 26/38 were confirmed de novo, 1 maternally inherited, 4 of unknown inheritance (parents unavailable), and one family had three affected male siblings with unknown paternal mosaicism status (PMID:31079897). In the 2021 cohort, 13/18 were de novo, 2 were paternally inherited in familial cases (siblings; one unrelated inherited case), with one instance of negative maternal testing and unavailable paternal testing (PMID:34321323).
- **gnomAD constraint:** *KMT2E* is highly intolerant of protein-truncating variation — pLI = 1.0, observed/expected ratio for PTVs = 0.01 (i.e., ~99% fewer PTVs observed in gnomAD than expected under neutral mutation), consistent with strong purifying selection against haploinsufficiency. The gene is not significantly constrained against missense variation (Z-score +1.42, missense o/e = 0.87), consistent with the rarity of pathogenic missense alleles and suggesting most missense substitutions are tolerated (PMID:31079897). Only ~5 apparent PTVs were found among >140,000 gnomAD individuals, mostly outside neurologic-disease cohorts.
- **Modifier genes:** No established modifier loci. One case in the second cohort carried a comorbid pathogenic *CHD8* variant plus a *MYH8* variant, producing a blended phenotype — illustrating that dual-diagnosis can complicate genotype-phenotype interpretation in individual cases but is not evidence of a systematic modifier (PMID:34321323).
- **Sex:** Marked male predominance across cohorts (73% male in the 2019 cohort; 78% male in the 2021 cohort), with a statistically significant sex-specific phenotype split: females showed higher epilepsy rates (43% vs 5% in males, p=0.047 in the founding cohort) while males trended toward higher autism rates (35% vs 0% in females, p=0.14) (PMID:31079897). The basis for the sex skew (ascertainment bias vs biological effect) is not established in the literature reviewed.

**Environmental/lifestyle risk factors:** None reported or plausible given the near-exclusively de novo monogenic mechanism; no gene-environment interaction data identified in the literature searched.

**Protective factors:** None identified; no protective variants or modifier alleles reported.

---

## 3. Phenotypes

Frequencies below are drawn primarily from the two largest published cohorts — O'Donnell-Luria et al. 2019 (n=38, PMID:31079897) and Velmans et al. 2021 (n=18, PMID:34321323) — with the 2019 truncating-variant subgroup (n=~27–30) and the 2021 cohort reported separately because ascertainment and instruments differed. A pooled table (Velmans et al.) combined both cohorts for several features.

### Neurodevelopmental / cognitive
| Phenotype | 2019 cohort (truncating) | 2021 cohort | Combined (where reported) | Suggested HP term |
|---|---|---|---|---|
| Global developmental delay | Near-universal | Near-universal | — | HP:0001263 |
| Speech delay | 75% (21/28) | 94% (17/18) | 83% (38/46) | HP:0000750 |
| Motor delay | 67% (18/27) | 72% (13/18) | 69% (31/45) | HP:0001270 / HP:0001263 |
| Intellectual disability (any) | 85% (17/20) / 81% (13/16 with IQ data) | 50% (6/12) | 72% (23/32) | HP:0001249 (mild: HP:0001256) |
| Mean IQ (n=7, truncating subgroup) | 74 (range 62–98) | — | — | — |
| Autism spectrum disorder | 26% (8/31) | 41% (7/17) | 31% (15/48) | HP:0000717 |
| Behavioral abnormalities (stereotypies, skin-picking, self-injury, aggression, anxiety) | 11/29 individuals | present | — | HP:0000733 (self-injurious behavior), HP:0000722 (aggressive behavior), HP:0000726 (anxiety) |
| Sleep disturbance | not systematically reported | 47% (8/17), incl. 30% without ASD | — | HP:0002360 |
| Executive-function difficulty | described qualitatively | — | — | — |

Onset is uniformly congenital/infantile — developmental delay is present from infancy in essentially all reported individuals. Mean age of independent walking and first words was 20 months (range 12–48) in the founding truncating-variant subgroup; individuals with microdeletions or missense variants had later milestones (walking 15–42 months; first words mean 34.5 months, range 18–48 for microdeletions). Almost all individuals who reach childhood achieve independent ambulation; most are verbal, though articulation problems are common (7/14 verbal individuals with articulation difficulty in the 2019 cohort).

### Neurological
| Phenotype | Frequency | Suggested HP term |
|---|---|---|
| Macrocephaly (≥2 SD) | 55% (16–18/29–33, both cohorts consistent at ~55–56%) | HP:0000256 |
| Hypotonia | 41–56% (varies by cohort: 41% 2019, 44–56% 2021) | HP:0001252 |
| Epilepsy/seizures | 15–23% in truncating-variant carriers (2019: 15%, 4/26, plus 1 additional single seizure); 0% in the 2021 cohort (0/18) but 11% febrile seizures; a 2025 systematic review across the pooled literature estimates ~29% incidence | HP:0001250 |
| Epilepsy in missense-variant carriers | 4/4 (100%), often infantile epileptic encephalopathy, frequently drug-resistant | HP:0032792 / HP:0011097 (infantile spasms context) |
| Epilepsy in microdeletion carriers | 3/4 (75%) | HP:0001250 |

Where epilepsy occurs, seizure types reported include generalized tonic-clonic, tonic, atonic, myoclonic seizures, and infantile spasms, with EEG showing burst suppression, hypsarrhythmia, or background disorganization in the missense subgroup. A 2025 genotype-phenotype/systematic-review paper on ODLURO-associated epilepsy (PMID:40048818) found that of individuals on record with antiseizure medication (n=10), ~70% required ≥2 agents, and at least 5 individuals had drug-resistant epilepsy — indicating epilepsy, when present, is often clinically significant rather than a mild/self-limited feature, and treatment response is heterogeneous (contrasting with the more optimistic "responsive to treatment in almost all" characterization from the original 2019 series, which was itself based on the truncating-variant subgroup only).

### Craniofacial / dysmorphic (subtle facial gestalt)
Composite Face2Gene analysis (2019 cohort, n=11) and independent description (2021 cohort) converge on: dolichocephaly, tall/large/prominent forehead, deep-set eyes, downslanting palpebral fissures, periorbital fullness, prominent/full cheeks, and prominent nasolabial folds. 2021-cohort-specific frequencies: large forehead 59% (10/17), full cheeks 53% (9/17), epicanthal folds 41% (7/17), deep-set eyes 41% (7/17). Suggested HP terms: dolichocephaly (HP:0000268), frontal bossing/prominent forehead (HP:0011220 or HP:0002007), deep-set eye (HP:0000490), downslanting palpebral fissures (HP:0000494), periorbital fullness (HP:0000629), full cheeks (HP:0000293), prominent nasolabial folds (no precise HP term identified — flag for lookup).

### Gastrointestinal
Reflux, vomiting, and bowel-motility problems (constipation) are common though inconsistently quantified in the 2019 series; the 2021 cohort specifically reports constipation in 44% (8/18) vs 19% (5/27) in the original cohort — combined 29% (13/45). Suggested HP terms: gastroesophageal reflux (HP:0002020), constipation (HP:0002019), vomiting (HP:0002013), feeding difficulties in infancy (HP:0011968).

### Other/rare features
Cardiac septal defects, neonatal jaundice, kyphosis, tapering fingers, cryptorchidism, hyperflexible joints — each reported in only isolated individuals, not core features.

### Neuroimaging
Brain MRI is frequently normal or shows nonspecific findings. Pooled abnormalities across cohorts/reviews: corpus callosum hypoplasia/thinning/agenesis, cerebral/ventricular cysts, ventriculomegaly, delayed myelination, reduced cerebral or cerebellar volume, white-matter signal changes, basal ganglia hyperintensity, heterotopia, Chiari I malformation, and (in the epilepsy-focused 2025 review, pooling across a larger literature set) brain atrophy (3 cases), congenital cerebral malformation (3 cases), corpus callosum hypoplasia (5 cases), cysts (4 cases), normal (2 cases), delayed myelination (1 case). This is imaging-pattern description across published case reports rather than a systematically ascertained cohort, so denominators vary by report.

### Quality of life
No disease-specific QoL instrument data (EQ-5D, SF-36, PROMIS) were identified in the literature searched; this is likely an evidence gap rather than a negative finding — flag as not yet studied.

### Sensory
Hearing and ophthalmologic examinations were reported as normal in all tested individuals in the founding cohort; no consistent sensory phenotype.

---

## 4. Genetic / Molecular Information

**Causal gene:** *KMT2E* (HGNC:18541; OMIM *608444), chromosome 7q22.2-q22.3, encoding lysine methyltransferase 2E / MLL5 (histone-lysine N-methyltransferase 2E), a member of the KMT2 (mixed-lineage leukemia, MLL) gene family. Reference transcript NM_182931.2/.3; the encoded protein is 1,858 amino acids.

**Protein domain architecture (PMID:31079897):**
- N-terminal PHD (plant homeodomain) zinc finger: residues ~120–165
- Central SET domain: residues ~282–445 — structurally homologous to the catalytic domain of active KMT2-family methyltransferases, but predicted (and experimentally suggested) to be **catalytically inactive** ("pseudo-methyltransferase") — KMT2E likely lacks intrinsic histone methyltransferase activity toward histone substrates despite SET-domain homology
- Disordered C-terminus for most of the remaining protein length, with helical/strand secondary structure predicted by HMMER/PHYRE2/InterProScan modeling

**Pathogenic variant spectrum:**
- **Protein-truncating variants (predominant class):** frameshift/indel (most common), nonsense, canonical and cryptic splice-site variants. Most are predicted substrates for nonsense-mediated decay (NMD); a subset of terminal-exon frameshifts (escaping NMD) were predicted in silico to create an aberrant C-terminal "homeodomain-like" fold with increased stability relative to the disordered wild-type C-terminus — a possible structural correlate for why terminal-exon truncations do not obviously differ clinically from NMD-triggering truncations (no clear genotype-phenotype split was found between NMD-predicted and NMD-escaping variants in the 2021 cohort).
- **Missense variants (rare, more severe phenotype):** four reported in the founding cohort — c.418G>A (p.Val140Ile, PHD domain), c.850T>C (p.Tyr284His, SET domain, predicted to abolish a phosphorylation site), c.2720A>T (p.Asp907Val, non-domain region), c.4126C>T (p.Pro1376Ser, non-domain region, predicted to create a novel phosphorylation site). All four missense carriers had epilepsy, often infantile epileptic encephalopathy, more severe developmental delay, and (2/4) microcephaly rather than the typical macrocephaly — a phenotypically distinct, more severe subgroup, possibly reflecting a dominant-negative or gain-of-function mechanism rather than simple haploinsufficiency (mechanism not experimentally confirmed; stated as a hypothesis by the original authors, PMID:31079897).
- **Microdeletions:** 7q22.2-q22.3 deletions ranging 0.052–3.2 Mb; the smallest reported deletion (52 kb) affects *KMT2E* alone and produces a phenotype similar to truncating point variants, supporting haploinsufficiency as the operative mechanism for the deletion/truncating-variant class. Larger deletions additionally encompass *SRPK2*, *RINT1*, *LHFPL3* and are associated with more severe developmental delay (mean first words 34.5 months) — attributable at least in part to contiguous-gene effects.
- **Synonymous variant with cryptic splicing effect:** A 2024 case report/functional study (Genes, doi:10.3390/genes15040430) describes a synonymous *KMT2E* variant, c.186G>A, in a patient with the ODLURO phenotype, with functional characterization supporting a splicing-disruptive mechanism (consistent with the broader observation that some apparently "silent" variants act pathogenically through cryptic splice-site creation/disruption) — I was not able to fully retrieve the primary functional assay methodology (e.g., minigene vs RNA-based confirmation) due to an access restriction on the publisher site; this should be independently verified against the primary text before citing assay-level detail.

**Variant classification (ACMG/AMP):** Individual variants are curated in ClinVar under the condition "O'Donnell-Luria-Rodan syndrome" (e.g., ClinVar entries for NM_182931.3(KMT2E):c.730-6_730-2del and c.3486C>G p.Tyr1162Ter). Systematic ACMG-classification statistics (e.g., % pathogenic vs likely pathogenic vs VUS across all reported variants) were not retrieved in this search pass.

**Population allele frequency:** Given near-complete de novo occurrence and strong purifying selection (pLI 1.0, PTV o/e 0.01), pathogenic *KMT2E* variants are essentially private/ultra-rare and not meaningfully represented in population databases (gnomAD, 1000 Genomes) — consistent with a severe, reproductively-limiting dominant disorder maintained almost entirely by recurrent de novo mutation rather than transmission.

**Somatic vs germline:** Germline (constitutional) in all reported ODLURO cases; *KMT2E* has separately been implicated in myeloid neoplasia (myelodysplastic syndrome) contexts as a hematopoietic regulator, but that is a distinct, non-overlapping somatic/hematologic disease association and should not be conflated with the germline neurodevelopmental phenotype (see design-decision guidance on keeping germline syndromes separate from associated somatic phenomena).

**Epigenetic information:** No disease-specific DNA methylation/EWAS episignature study was identified in this search (unlike, e.g., Kabuki syndrome's *KMT2D* episignature) — this appears to be an evidence gap rather than a confirmed negative; worth a targeted follow-up search (EpiSign/GeneDx episignature literature) before asserting absence.

**Chromosomal abnormalities:** 7q22.2-q22.3 microdeletions as above; no translocations, inversions, or other structural rearrangements specifically reported.

---

## 5. Environmental Information

No environmental, toxic, infectious, dietary, or lifestyle causal or risk factors are described for ODLURO in the literature reviewed — consistent with its status as an essentially fully-penetrant, de novo monogenic disorder. No CTD, TOXNET, or epidemiological gene-environment interaction data were located. This section is not populated for the underlying disease mechanism, though standard advanced-paternal-age considerations that apply generically to de novo dominant disorders may be relevant (not specifically quantified for ODLURO in the sources reviewed).

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, with confidence/inference flags)

1. A de novo (rarely inherited) heterozygous protein-truncating variant, damaging missense variant, or a microdeletion arises in *KMT2E* on 7q22.2-q22.3. *(Demonstrated — genetic ascertainment across cohorts, PMID:31079897, 34321323.)*
2. For truncating variants and microdeletions, this **leads to** reduced dosage of functional MLL5/KMT2E protein from the affected allele — either via nonsense-mediated decay of the truncated transcript or via physical loss of one gene copy — **resulting in** haploinsufficiency, i.e., insufficient total MLL5 protein from the single remaining wild-type allele to sustain normal function. *(Inferred from convergent phenotype between truncating-variant and microdeletion carriers, plus the pLI=1.0/PTV o/e=0.01 constraint signature and ClinGen's independent "Sufficient Evidence for Haploinsufficiency" (score 3) dosage curation — a well-supported but formally indirect line of evidence, since no direct protein-quantification study in patient tissue was identified.)*
3. For the rare missense variants (PHD- and SET-domain-affecting, plus two variants outside annotated domains), the mechanism **may instead involve** a dominant-negative or altered-function effect rather than simple haploinsufficiency, given that these carriers show a phenotypically distinct and more severe presentation (infantile epileptic encephalopathy, microcephaly) than truncating-variant/deletion carriers. *(Explicitly flagged as hypothesis-level, not proven, by the original authors, PMID:31079897 — this is an unresolved mechanistic question, not an established fact.)*
4. MLL5/KMT2E, despite SET-domain homology to catalytically active KMT2-family histone methyltransferases, **appears to lack intrinsic histone methyltransferase activity** ("pseudo-methyltransferase"). Instead, MLL5 **binds H3K4me3-marked promoter chromatin** via mechanisms involving its PHD finger and **functions as a transcriptional/chromatin co-regulator** rather than as the enzyme that writes the H3K4me3 mark itself. *(Established biochemical characterization in the broader KMT2E/MLL5 structure-function literature — Springer 2017 review PMID:28188343 — generalized to, but not specifically re-derived in, the ODLURO cohort papers.)*
5. MLL5 **forms a complex with host cell factor C1 (HCFC1) and O-GlcNAc transferase (OGT)**, which is recruited to E2F1-responsive gene promoters, **driving transcriptional activation at the G1/S cell-cycle transition** and contributing to genomic-stability maintenance through the G2/M transition and mitotic spindle integrity. *(Established cell-biology literature on MLL5 function, largely from non-neuronal/hematopoietic systems — extrapolated to neurodevelopmental context by the disease-cohort authors rather than directly demonstrated in human neurons.)*
6. Reduced or altered MLL5 activity **is proposed to** disrupt normal transcriptional programs during **nervous system development**, particularly given evidence that *KMT2E* is highly expressed in fetal brain. *(Plausible inference bridging cell-biology data to neurodevelopmental phenotype; not directly demonstrated via patient-neuron transcriptomics — no iPSC-neuron or patient-fibroblast RNA-seq study was identified in the cohort literature reviewed.)*
7. In a *Kmt2e+/−* mouse model, this haploinsufficiency **produces** amygdala-selective neurodevelopmental abnormality: decreased relative amygdala glycometabolism on ¹⁸F-FDG-PET imaging, together with increased numbers and soma size of amygdala neurons, **leading to** social-behavior deficits and anxiety-like behavior — an ASD-relevant behavioral phenotype in the animal model paralleling the human autism association. *(Direct experimental animal-model evidence, PMID:36534336 — the clearest mechanistic link in the literature reviewed between *Kmt2e* dosage and a specific brain region/behavioral output; note this is a **mouse model**, and translational fidelity to the specific human clinical phenotype has not been independently assessed — flagged as a `HUMAN_MODEL_MISMATCH`-type consideration for KB curation rather than a demonstrated human mechanism.)*
8. Separately, in hematopoietic/non-neuronal systems, *Kmt2e*-deficient mouse models show growth restriction, increased mortality, impaired hematopoiesis, and elevated DNA damage/reactive oxygen species (ROS) — reversible with N-acetylcysteine antioxidant supplementation in that model system. *(PMID:31079897, citing earlier hematopoiesis-focused *Kmt2e* mouse literature — this pathway has not been shown to operate in neurons or to explain the neurodevelopmental phenotype; the original ODLURO authors raise it only as a speculative rationale for a possible future antioxidant-biomarker/therapeutic angle, explicitly requiring clinical validation, not as an established human disease mechanism.)*
9. The composite of impaired neurodevelopmental gene transcription (from #6) and amygdala-specific structural/metabolic changes (from #7) **culminates in** the clinical syndrome: global developmental delay, intellectual disability, macrocephaly, hypotonia, autism-spectrum features, and (in a subset, more severely with missense variants) epilepsy/epileptic encephalopathy.

### Molecular pathways
Chromatin regulation / H3K4 methylation pathway (KMT2/COMPASS-family, though KMT2E itself is enzymatically atypical); E2F1 cell-cycle transcriptional pathway (G1/S checkpoint); HCFC1–OGT transcriptional co-regulator complex. Suggested GO terms: histone H3-K4 methylation (GO:0051568), positive regulation of transcription by RNA polymerase II (GO:0045944), regulation of cell cycle G1/S phase transition (GO:2000045), DNA damage response (GO:0006974).

### Cellular processes
Cell-cycle progression (G1/S and G2/M transitions), maintenance of genomic/chromosomal stability, mitotic spindle integrity, neuronal differentiation/development (inferred), amygdala neuron proliferation/soma growth (mouse model — direction of effect was *increased* neuron number/soma size in the haploinsufficient state, notably not simple loss of neurons).

### Protein dysfunction
Loss of one functional MLL5 allele (haploinsufficiency) for truncating/deletion variants; possible altered-function/dominant-negative effect for domain-disrupting missense variants (unconfirmed mechanism).

### Tissue/cell involvement
Cerebral cortex and amygdala are the principal implicated CNS structures (mouse model + human neuroimaging correlate of corpus callosum/white matter/ventricular findings). Suggested CL term: neuron (CL:0000540); no KMT2E-specific neuronal subtype marker was identified. Suggested UBERON terms: amygdala (UBERON:0001876), corpus callosum (UBERON:0002336), cerebral cortex (UBERON:0000956), cerebellum (UBERON:0002037).

### Molecular profiling / advanced technologies
No transcriptomic (RNA-seq/GEO), proteomic, metabolomic, single-cell, or spatial-transcriptomic dataset specific to ODLURO patient tissue was identified in this search. The ¹⁸F-FDG-PET amygdala-glycometabolism data from the mouse model (PMID:36534336) is the only "molecular imaging"-type dataset located. This is a notable evidence gap relative to other KMT2-family disorders (e.g., Kabuki syndrome/*KMT2D* has an established peripheral-blood DNA-methylation episignature; no equivalent was found for *KMT2E*).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** central nervous system (brain — cerebral cortex, corpus callosum, amygdala, cerebellum, ventricular system, white matter)
- **Secondary:** gastrointestinal tract (functional — reflux, motility/constipation); skeletal system (rare — kyphosis, tapering fingers); cardiovascular (rare — septal defects); genitourinary (rare — cryptorchidism)
- **Body systems:** nervous system (primary), digestive system, musculoskeletal system, and rarely cardiovascular and genitourinary systems

**Tissue/cell level:** Cerebral cortical neurons and amygdala neurons are the specific cell population implicated by the mouse model (increased neuron number and soma size in *Kmt2e+/−* amygdala). No human neuropathology/biopsy data exist (as expected for a neurodevelopmental, non-degenerative, non-biopsied disorder).

**Subcellular level:** Nucleus/chromatin — MLL5 is a chromatin-associated transcriptional regulator acting at H3K4me3-marked promoter regions. Suggested GO Cellular Component term: nucleus (GO:0005634), nuclear chromatin (GO:0000790).

**Localization:** Bilateral, non-lateralized — the amygdala finding in the mouse model was described as a whole-structure/bilateral metabolic change; no laterality pattern reported in human neuroimaging.

---

## 8. Temporal Development

**Onset:** Congenital/infantile-onset — developmental delay is evident from infancy in essentially all affected individuals; there is no adult-onset or late-onset presentation described. Onset pattern is insidious/developmental (progressive delay relative to peers becoming apparent through infancy and early childhood) rather than acute.

**Progression:** The disorder is best characterized as a **static-to-mildly-progressive neurodevelopmental disorder** rather than a degenerative one — affected individuals continue to gain skills (most achieve independent walking and verbal speech, albeit delayed) rather than losing previously acquired abilities, with the exception of rare reported speech regression in a subset. No formal staging system exists. Disease course is chronic/lifelong; there is no described remission of the core neurodevelopmental phenotype. Epilepsy, when present, follows its own variable course (from treatment-responsive to drug-resistant, per the 2025 systematic review, PMID:40048818) and can be episodic/relapsing rather than following the same static trajectory as the developmental phenotype.

**Critical periods:** Fetal/early postnatal brain development is implicated as the critical vulnerability window, based on high fetal-brain expression of *KMT2E* and the cell-cycle/chromatin regulatory role of MLL5 during neurogenesis; there is no established therapeutic window distinct from standard early-intervention timing for developmental disorders generally.

---

## 9. Inheritance and Population

**Epidemiology:** No formal population-based prevalence or incidence estimate (cases per 100,000) was identified in the literature searched — appropriate given ODLURO's status as a recently delineated (2019), likely under-ascertained condition. Cohort growth (38 individuals in 2019 → >60 within 2 years → >120 individuals reported by 2025 per a Wikipedia-sourced tertiary summary, not independently verified against a primary source) has led multiple authors (notably Velmans et al., PMID:34321323) to argue that ODLURO is "an unexpectedly high relative frequency…among the more common single-gene aetiologies of neurodevelopmental delay and ASD," with an explicit recommendation that *KMT2E* be included in routine developmental-delay/ID/ASD gene panels — but this remains a qualitative impression from clinical-ascertainment cohorts, not a quantified population prevalence/incidence figure, and should be curated as `prevalence_class: NOT_YET_DOCUMENTED` or similar pending a real denominator-based estimate.

**Inheritance pattern:** Autosomal dominant, with the overwhelming majority of cases arising de novo (see Etiology, above). Two multiplex families are documented: three affected male siblings (paternal mosaicism status unresolved, 2019 cohort) and a sibling pair with paternal transmission (2021 cohort), plus one additional unrelated paternally-inherited case.

**Penetrance:** Reported as apparently high/complete for the core neurodevelopmental phenotype among identified carriers, though formal penetrance estimation (e.g., via large unselected population cohorts) has not been performed — as is typical for a recently described, clinically-ascertained dominant disorder.

**Expressivity:** Markedly **variable** — this is one of the syndrome's defining features. Severity ranges from mild developmental/speech delay with normal-range cognition to moderate intellectual disability with autism and drug-resistant infantile epileptic encephalopathy, correlating in part with variant class (truncating/deletion = generally milder; missense = more severe, per the 2019 cohort) though the 2025 genotype-phenotype/epilepsy review notes that even individuals sharing the identical *KMT2E* variant can show divergent phenotypes, indicating expressivity is not fully explained by variant type alone.

**Genetic anticipation:** Not applicable/not reported — ODLURO is not a repeat-expansion disorder.

**Germline mosaicism:** Not formally quantified but clinically relevant, given the multiplex sibling families described above with presumed unaffected or mosaic parents; standard recurrence-risk counseling for germline mosaicism (empiric low-single-digit-percent recurrence risk, as for other de novo dominant NDDs) would apply, though ODLURO-specific recurrence-risk data were not located.

**Founder effects:** None reported — variants are private/family-specific, consistent with the essentially de novo mutational mechanism.

**Consanguinity:** Not a relevant risk factor for this autosomal dominant, de novo-predominant disorder.

**Carrier frequency:** Not applicable in the traditional (autosomal recessive) sense; population allele frequency of pathogenic variants is essentially zero given strong purifying selection (see Etiology).

**Population demographics:**
- **Sex ratio:** Strong male excess across both major cohorts (73–78% male) — see Etiology section for statistical detail and caveats about ascertainment vs. biological explanation.
- **Ethnic/geographic distribution:** Both major cohorts were explicitly multinational (assembled via Matchmaker Exchange and international collaboration), and no specific ethnic or geographic enrichment/founder population has been reported. No population-specific variant clustering identified.
- **Age distribution:** Cohorts span early childhood through adolescence (2021 cohort ages 1–16 years); no adult-ascertained cohort or aging-population data were identified, which likely reflects the recency of syndrome delineation (2019) rather than a true absence of adult-affected individuals.

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):**
- **First-tier per GeneReviews (PMID:38648332) and Wikipedia tertiary summary corroborating it:** chromosomal microarray (SNP array or oligonucleotide-based CGH) to detect 7q22.2-q22.3 microdeletions.
- **If microarray non-diagnostic:** an intellectual-disability/multigene NDD panel that includes *KMT2E*, or comprehensive genomic testing (exome or genome sequencing). Exome sequencing is currently the most commonly employed comprehensive approach in the literature; genome sequencing is noted as additionally capable of detecting noncoding/regulatory and splicing variants and structural variants missed by exome sequencing (e.g., the cryptic-splice-site and synonymous-splicing-disruptive variants described above would specifically benefit from RNA-level or genome-level analysis).
- **Variant interpretation:** De novo status confirmation via parental (trio) testing is central to establishing pathogenicity, particularly for VUS-level findings, given the disorder's predominantly de novo mechanism.

**No disease-specific biochemical, enzymatic, or biomarker laboratory test exists** — ODLURO is not a metabolic disorder, and no circulating biomarker (protein, metabolite) has been validated. The single speculative candidate mentioned in the literature (urine F2-isoprostane and blood glutathione as oxidative-stress markers, extrapolated from the hematopoietic mouse-model ROS finding) is explicitly framed by the original authors as unvalidated and requiring clinical study — it is not a diagnostic test in current use.

**Neuroimaging:** Brain MRI is a standard part of the diagnostic/clinical workup once a genetic diagnosis is suspected or confirmed, useful for characterizing (though not specific/diagnostic for) the condition — findings as detailed in Section 3 (often normal; when abnormal, most commonly corpus callosum hypoplasia, cysts, delayed myelination, ventriculomegaly).

**Electrophysiology:** EEG is indicated when seizures are suspected clinically, given the significant minority with epilepsy (especially relevant to exclude/characterize infantile epileptic encephalopathy in missense-variant carriers).

**Clinical diagnostic criteria:** No formal consensus clinical diagnostic criteria exist (no equivalent of, e.g., Kabuki syndrome's clinical scoring system was identified). Diagnosis is made on the basis of a qualifying pathogenic/likely pathogenic *KMT2E* variant (or qualifying microdeletion) in an individual with a consistent clinical picture.

**Differential diagnosis:** GeneReviews and secondary sources note phenotypic overlap with other genetic syndromes causing developmental delay/intellectual disability with subtle dysmorphism, specifically naming **Kabuki syndrome** and **Wiedemann-Steiner syndrome** as conditions with overlapping clinical findings (per the Wikipedia tertiary summary, sourced to the GeneReviews chapter, though I was not able to directly access the GeneReviews differential-diagnosis table text due to access restrictions — this specific claim should be re-verified against the primary GeneReviews source, PMID:38648332, before being asserted as `DIRECT` evidence in a KB entry). No specific overlap with Cornelia de Lange syndrome was substantiated in the sources retrieved (a search targeting that comparison returned no supporting content).

**Screening:** No population newborn-screening or carrier-screening program applies (not a metabolic/recessive disorder amenable to such screening). Standard prenatal counseling applies once a familial variant is known (e.g., for the rare inherited/multiplex-sibling scenario), including consideration of parental testing for germline mosaicism.

---

## 11. Outcome / Prognosis

**Survival/mortality:** No mortality data or life-expectancy figures specific to ODLURO were identified — the disorder is not described in the literature as life-limiting, and no deaths have been reported in the cohorts reviewed. This should be treated as an evidence gap (no data located) rather than a confirmed "normal life expectancy" claim, since no dedicated natural-history/longitudinal-survival study was found.

**Morbidity/function:** Nearly all affected individuals who reach childhood achieve independent ambulation and (with speech delay) verbal communication, indicating a generally favorable functional trajectory relative to more severe neurodevelopmental syndromes, though intellectual disability (typically mild-to-moderate, pooled cohort rate 72%) and, in a subset, drug-resistant epilepsy represent the principal sources of long-term morbidity. Executive-function difficulties (flexible thinking, working memory) are described qualitatively as prevalent but not quantified.

**Quality of life:** No validated QoL instrument data located (see Section 3) — an evidence gap.

**Complications:** Feeding difficulties sometimes progressing to need for gastrostomy tube placement (per GeneReviews/secondary-source management guidance); drug-resistant epilepsy in the missense-variant/more-severe subgroup (up to ~70% of medicated individuals in the 2025 review requiring ≥2 antiseizure medications, ≥5 individuals drug-resistant).

**Recovery potential:** Developmental gains continue over time in the majority (no degenerative course); speech regression is described as a rare exception rather than the norm.

**Prognostic factors:** Variant class is the clearest prognostic correlate identified — missense variants (particularly SET/PHD-domain) are associated with more severe developmental delay, microcephaly (rather than the typical macrocephaly), and treatment-resistant infantile epileptic encephalopathy; truncating variants and the smallest microdeletions are associated with a milder, though still variable, phenotype. However, the 2025 genotype-phenotype epilepsy review explicitly notes that "a clear genotype-phenotype correlation remains elusive even among individuals with the same *KMT2E* variation" (PMID:40048818) — so variant class should be treated as a probabilistic/partial prognostic signal, not a deterministic one.

---

## 12. Treatment

There is **no disease-modifying or curative therapy** for ODLURO. Management is entirely supportive/symptomatic, per GeneReviews (PMID:38648332) and corroborating secondary sources:

**Developmental/supportive care:**
- Early intervention services, special education
- Physical therapy (motor skills) — NCIT:C15302
- Occupational therapy (daily functioning) — NCIT:C121351 (Occupational Therapy) or NCIT:C15746-type intervention term
- Speech-language therapy — NCIT:C159273
- Periodic monitoring of head circumference and developmental milestones
- Gastrostomy tube placement for persistent/severe feeding difficulty — NCIT:C116617-type procedure term (verify exact NCIT code at curation time)

**Seizure management (for the subset with epilepsy):**
- EEG and brain MRI evaluation when seizures are suspected
- Individualized antiseizure medication selection based on seizure type/severity — NCIT:C15986 (Pharmacotherapy), with no single first-line agent established specifically for ODLURO; the 2025 review's finding that ~70% of medicated individuals required polytherapy underscores that this is often a difficult-to-control epilepsy requiring individualized, multidisciplinary epileptology input rather than a standard algorithm.
- Ketogenic diet was tried in at least one reported missense-variant case with infantile epileptic encephalopathy but was reported as ineffective in that instance (PMID:31079897) — a single-case negative result, not generalizable evidence of futility.

**Multidisciplinary/psychosocial care:** Medical genetics, developmental pediatrics, neurology, genetic counseling (risk assessment, family planning, prenatal testing discussion for known-variant families), and — for more severely affected individuals — palliative care/social work support.

**Experimental/investigational — antisense oligonucleotide (ASO) strategies (preclinical/conceptual stage only):** A 2024–2025 treatability-landscape review specifically addressing KMT2-family disorders (PMID for the PMC11925151 article not independently confirmed in this pass — verify before citing) outlines several **conceptual, not yet preclinically validated**, ASO-based strategies premised on the haploinsufficiency mechanism (goal: increase wild-type protein output from the remaining allele or correct/skip a specific mutant transcript):
1. Variant-specific exon skipping (e.g., targeting exon 15 to restore reading frame for a specific frameshift variant, c.1646_1650del/p.Ile549fs) — patient-specific, N-of-1-style approach.
2. Targeting a "poison exon" in intron 21 whose inclusion is non-productive, to increase canonical-transcript output — proposed as a more generalizable approach applicable across multiple patients (rather than variant-specific).
3. Modulating an identified upstream open reading frame (uORF) in the *KMT2E* 5′ UTR via steric-blocking ASOs, to relieve uORF-mediated translational repression of the main protein-coding ORF and thereby increase wild-type protein levels.
4. Targeting the naturally occurring antisense transcript *KMT2E-AS1*, though this requires further functional characterization before it can be considered an actionable target.

The review explicitly states that **no preclinical data or ASO treatments are currently under development** for KMT2E-associated disorders — these are proposed strategies grounded in the general ASO-therapeutics toolkit and the confirmed haploinsufficiency mechanism, not validated interventions. This should be curated as a `PROPOSED`/conceptual therapeutic-strategy discussion, not an active clinical or even preclinical program.

**No clinical trials** (NCT-registered) specific to ODLURO/*KMT2E* were identified in this search pass.

**No gene therapy, cell therapy, targeted small-molecule, or immunotherapy approach** has been reported for this condition.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategy exists for ODLURO beyond standard reproductive/genetic counseling, since the disorder is predominantly caused by de novo mutation (not currently preventable) rather than inherited from a carrier population amenable to carrier screening. For the minority of familial (inherited or mosaic-parent) cases, **genetic counseling** covering recurrence risk (including empiric germline-mosaicism risk), prenatal diagnosis, and preimplantation genetic testing options for known-familial variants is the applicable "prevention" modality — standard practice for autosomal dominant NDDs generally, not ODLURO-specific guidance. No population-level screening program (newborn or carrier) applies, and no immunization, environmental, or public-health intervention is relevant given the monogenic, non-environmental disease mechanism.

---

## 14. Other Species / Natural Disease

No naturally occurring ODLURO-like disease has been reported in non-human species (companion animals, wildlife) in the literature searched — I found no OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case series for *KMT2E*/*Kmt2e* orthologs. This should be treated as "not identified in this search," not a confirmed absence.

**Orthologous gene:** Mouse *Kmt2e* (MGI symbol; allele *Kmt2e^tm1Apa^*, MGI:3835772, used in the hematopoiesis/ROS studies cited in Section 6/12) is the principal model-organism ortholog used experimentally. No zebrafish, *Drosophila*, or *C. elegans* ortholog-based disease model was identified in this search.

**Comparative biology:** The KMT2/MLL gene family (KMT2A–KMT2F) is broadly conserved across vertebrates and is functionally implicated in a cluster of related human neurodevelopmental disorders (Wiedemann-Steiner syndrome/*KMT2A*, Kabuki syndrome/*KMT2D*), reflecting evolutionary conservation of chromatin-regulatory mechanisms in neurodevelopment — but *KMT2E* is functionally distinct within the family (pseudo-methyltransferase, non-catalytic chromatin reader/co-regulator) rather than a directly redundant paralog, so mechanistic conclusions from *KMT2A*/*KMT2D* disorders should not be assumed to transfer directly to *KMT2E*/ODLURO.

**Zoonotic/transmission potential:** Not applicable — a non-communicable monogenic disorder.

---

## 15. Model Organisms

**Mouse — germline heterozygous knockout (*Kmt2e+/−*):**
- **Model type:** Genetic (constitutive heterozygous knockout), mammalian, whole-organism.
- **Phenotype recapitulation:** *Kmt2e+/−* mice show social-interaction deficits and anxiety-like behavior on standardized behavioral assays, together with **decreased relative amygdala glycometabolism** on whole-brain ¹⁸F-FDG-PET imaging and **increased numbers and soma size of amygdala neurons**, relative to wild-type littermates (PMID:36534336). This is presented by the authors as supporting a causative role for *KMT2E* haploinsufficiency in ASD-relevant behavior, with amygdala neurodevelopmental abnormality proposed as a major underlying mechanism.
- **Model limitations:** This model recapitulates an ASD-relevant behavioral/imaging phenotype but has not been reported to reproduce the broader human ODLURO syndrome (developmental delay/intellectual-disability-equivalent measures, epilepsy, macrocephaly, dysmorphic features, or GI symptoms) — translational fidelity for those additional core human features is unestablished. The direction of the amygdala neuron finding (*increased* number/soma size, rather than a loss-of-neurons/atrophy pattern) is a specific and somewhat counterintuitive structural correlate worth flagging precisely rather than generalizing to "neurodegeneration."
- **Research applications:** Used to probe ASD-relevant circuit-level (amygdala) and behavioral consequences of *Kmt2e* dosage reduction; a plausible platform for future preclinical testing of the ASO strategies outlined in Section 12, though no such testing has yet been reported.

**Mouse — hematopoiesis-focused *Kmt2e*-deficient models (both homozygous and heterozygous):**
- **Phenotype:** Growth restriction, increased mortality, impaired hematopoiesis, elevated DNA damage and reactive oxygen species (ROS), reversible with N-acetylcysteine (CHEBI:28939) supplementation (cited in PMID:31079897, referencing earlier hematopoiesis-focused literature).
- **Limitations:** No neurological/behavioral phenotype was reported in these earlier hematopoiesis-focused models — i.e., this line of evidence establishes a non-neuronal *Kmt2e* loss-of-function phenotype (relevant to *KMT2E*'s separately described role in myeloid biology) but does **not** itself demonstrate a brain phenotype; it is cited by the ODLURO discovery paper only as indirect/speculative support for a possible oxidative-stress axis, not as a validated model of the neurodevelopmental disorder.

**Cellular/in vitro models:** No patient-derived iPSC, fibroblast, or organoid model specific to ODLURO/*KMT2E* was identified in this search — a further evidence gap relative to better-resourced neurodevelopmental-disorder genes.

**Resources:** MGI (Mouse Genome Informatics) hosts the *Kmt2e^tm1Apa^* allele record (MGI:3835772); no ZFIN, FlyBase, WormBase, or IMSR-cataloged model was located.

---

## Summary of Notable Evidence Gaps (flagged for curator follow-up rather than asserted as fact)

1. **No confirmed Orphanet (ORPHA) identifier** was located — needs direct Orphanet lookup.
2. **No population-based prevalence/incidence figure** exists; only qualitative "more common than previously appreciated" cohort-growth framing (`prevalence_class: NOT_YET_DOCUMENTED` is the honest curation state).
3. **No validated biomarker, EWAS/episignature, or patient-derived cellular/omics dataset** was located for *KMT2E* — contrasts with sibling KMT2-family disorders.
4. **Differential-diagnosis overlap with Kabuki and Wiedemann-Steiner syndromes** was sourced only via a tertiary (Wikipedia) summary attributed to GeneReviews; the primary GeneReviews differential-diagnosis text (PMID:38648332) could not be directly accessed in this session (CAPTCHA-blocked) and should be independently re-verified before quoting.
5. **The synonymous-variant splicing functional study** (Genes 2024, doi:10.3390/genes15040430) could not be fully retrieved (publisher access blocked) — assay-level detail should be confirmed from the primary text.
6. **Missense-variant dominant-negative/gain-of-function mechanism** is explicitly hypothesis-level in the primary literature, not proven — should not be curated as a `DIRECT` mechanistic claim.
7. **Mouse amygdala model** is ASD-behavior/circuit-specific and does not model the full human syndrome — a `HUMAN_MODEL_MISMATCH`-flavored caveat, not a general-purpose disease model.
8. Two PMC/PMID numbers for secondary papers (the ASO-treatability review, and the 2024 novel-cohort ScienceDirect paper) were identified via search-result triangulation but full-text access was blocked in this session (403/CAPTCHA); their PMIDs and exact quotable content should be re-confirmed via `just fetch-reference` at curation time rather than trusted from this report's paraphrase alone.

---

## Sources

- [O'Donnell-Luria A, et al. Heterozygous Variants in KMT2E Cause a Spectrum of Neurodevelopmental Disorders and Epilepsy. Am J Hum Genet. 2019;104(6):1210-1222. PMID:31079897](https://pubmed.ncbi.nlm.nih.gov/31079897/) / [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6556837/)
- [Velmans C, O'Donnell-Luria A, et al. O'Donnell-Luria-Rodan syndrome: description of a second multinational cohort and refinement of the phenotypic spectrum. J Med Genet. 2021;59(7):697-705. PMID:34321323](https://pubmed.ncbi.nlm.nih.gov/34321323/) / [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10256139/)
- [Pais LS, Rodan LH, O'Donnell-Luria A. KMT2E-Related Neurodevelopmental Disorder. GeneReviews. 2024. PMID:38648332](https://www.ncbi.nlm.nih.gov/books/NBK602945/)
- [O'DONNELL-LURIA-RODAN SYNDROME; ODLURO — OMIM #618512](https://omim.org/entry/618512)
- [KMT2E gene — OMIM *608444](https://omim.org/entry/608444)
- [O'Donnell-Luria-Rodan syndrome — MONDO:0032793 (Monarch Initiative)](https://monarchinitiative.org/MONDO:0032793)
- [KMT2E gene-disease validity and dosage sensitivity curation — ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:18541)
- [Li et al. KMT2E Haploinsufficiency Manifests Autism-Like Behaviors and Amygdala Neuronal Development Dysfunction in Mice. Mol Neurobiol. 2023. PMID:36534336](https://pubmed.ncbi.nlm.nih.gov/36534336/)
- [Genotype-phenotype correlation of ODLURO syndrome comorbid epilepsy associated with KMT2E variations: report on a novel case and systematic literature review. Epilepsy Behav. 2025. PMID:40048818](https://pubmed.ncbi.nlm.nih.gov/40048818/)
- [Molecular and clinical Insights into KMT2E-Related O'Donnell-Luria-Rodan syndrome in a novel patient cohort. PMID:39709003](https://pubmed.ncbi.nlm.nih.gov/39709003/)
- [Treatability of the KMT2-Associated Neurodevelopmental Disorders Using Antisense Oligonucleotide-Based Treatments](https://pmc.ncbi.nlm.nih.gov/articles/PMC11925151/)
- [Phenotypic Description of A Patient with ODLURO Syndrome and Functional Characterization of a Synonymous Variant c.186G>A in KMT2E. Genes. 2024;15(4):430](https://www.mdpi.com/2073-4425/15/4/430)
- [Weirauch/Vora et al. MLL5 (KMT2E): structure, function, and clinical relevance. Cell Mol Life Sci. 2017. PMID:28188343](https://pubmed.ncbi.nlm.nih.gov/28188343/)
- [O'Donnell-Luria–Rodan syndrome — Wikipedia (tertiary summary, cross-checked against primary sources above where possible)](https://en.wikipedia.org/wiki/O%27Donnell-Luria%E2%80%93Rodan_syndrome)
- [Kmt2e^tm1Apa^ allele — Mouse Genome Informatics, MGI:3835772](https://www.informatics.jax.org/allele/MGI:3835772)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032793` (4 mentions) - the report calls it "if available", "MONDO", "Monarch Initiative"; MONDO calls it **O'Donnell-Luria-Rodan syndrome**
- `HP:0000256` (1 mention) - the report calls it "55% (16–18/29–33, both cohorts consistent at ~55–56%)"; HP calls it **Macrocephaly**
- `HP:0001252` (1 mention) - the report calls it "41–56% (varies by cohort: 41% 2019, 44–56% 2021)"; HP calls it **Hypotonia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051568` (obsolete histone H3-K4 methylation) (1 mention)
- `GO:0000790` (GO_0000790) (1 mention) - replaced by `GO:0000785`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0032793` - called "if available", "MONDO", "Monarch Initiative"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.
