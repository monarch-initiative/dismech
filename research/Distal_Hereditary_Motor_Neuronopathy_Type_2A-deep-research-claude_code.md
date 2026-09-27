---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-06T00:35:32.339245'
end_time: '2026-09-06T00:40:43.337128'
duration_seconds: 311.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Distal Hereditary Motor Neuronopathy Type 2A
  mondo_id: MONDO:0008025
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
  web_search_requests: 24
  num_turns: 28
  total_cost_usd: 1.6676078000000005
  session_id: 61cdf25c-4c5c-5869-94d7-1ef4a7d6867f
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 11
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Distal Hereditary Motor Neuronopathy Type 2A
- **MONDO ID:** MONDO:0008025 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Distal Hereditary Motor Neuronopathy Type 2A** covering all of the
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

I have enough material now to compile a comprehensive, well-cited report. Let me do a couple more targeted searches to round out sections on epidemiology/founder families, other model organisms, and mitochondrial mechanistic detail, then write the full report.

I now have sufficient sourced material to compile the full report.

---

# Distal Hereditary Motor Neuronopathy Type 2A (dHMN2A) — Comprehensive Research Report

**MONDO ID:** MONDO:0008025 | **OMIM Phenotype:** #158590 (Neuronopathy, Distal Hereditary Motor, Autosomal Dominant 2; HMND2) | **Causal Gene:** ***HSPB8*** (OMIM *608014; HGNC:5254) | **Orphanet:** ORPHA:139525 (Distal hereditary motor neuropathy type 2, umbrella entry)

> **Important nomenclature clarification (verify before curation):** Searches for "dHMN2A" frequently surface literature on the *related but genetically distinct* entity caused by ***HSPB1*** (HSP27; CMT2F / dHMN "type 2B" in the Rossor et al. classification, OMIM #608634). Cross-checking OMIM #158590, ClinVar, and NCBI MedGen (Concept ID C1834692) confirms that **"distal hereditary motor neuronopathy type 2A" (HMND2) is specifically the HSPB8-linked disorder**, first mapped to chromosome 12q24.3 and molecularly solved by Irobi et al. (2004), PMID:[15122253](https://pubmed.ncbi.nlm.nih.gov/15122253/). HSPB1-related disease is a mechanistically parallel chaperonopathy but a separate MONDO/OMIM entity and should not be conflated with dHMN2A in curation. This report focuses on the HSPB8-caused entity while noting the HSPB1 parallel where mechanistically informative.

---

## 1. Disease Information

**Overview:** Distal hereditary motor neuronopathy type 2A (dHMN2A, also called "Charcot-Marie-Tooth disease, spinal, type IIA" or CMT2L-related dHMN) is a rare, autosomal dominant, length-dependent motor neuronopathy. It is a "pure" motor axonopathy — degeneration of the distal motor axon of the peripheral motor neuron — without primary sensory nerve involvement, distinguishing it from Charcot-Marie-Tooth disease type 2 (which shows length-dependent sensorimotor loss). Onset is typically in the second to third decade of life, presenting with weakness of the toe/foot extensors and progressing over years to distal leg and, less severely, hand/forearm weakness (NCBI GTR C1834692; OMIM #158590).

**Key Identifiers:**
- OMIM phenotype: #158590 (HMND2)
- OMIM gene: *608014 (HSPB8; also HSP22, E2IG1, CMT2L)
- Orphanet: ORPHA:139525 (umbrella "Distal hereditary motor neuropathy type 2," which groups genetically heterogeneous causes including HSPB1 #608634, HSPB8 #158590, and others — OMIM 613376, 615575 — under one clinical Orphanet code)
- MONDO: MONDO:0008025
- MedGen: C1834692
- Alternate/allelic names: HMND2; "Charcot-Marie-Tooth disease, spinal, type IIA"; distal HMN type II (dHMN-II, subtype A per Rossor et al. classification); CMT2L is the allelic *sensorimotor* phenotype from the same gene (HSPB8) — same locus, different clinical label depending on whether sensory involvement is documented.
- ICD-10: G60.0 (Hereditary motor and sensory neuropathy, generic code — dHMN lacks a distinct ICD-10-CM code); ICD-11: 8C05 (hereditary motor neuropathy category)
- MeSH: Neuronal loss/motor neuropathies are not separately MeSH-indexed at this granularity; typically indexed under "Charcot-Marie-Tooth Disease" (D002607) and "Muscular Atrophy, Spinal."

**Data source type:** All available information for dHMN2A is derived from **aggregated disease-level resources** — case series, pedigree linkage studies, and cellular/animal model publications. There is no large EHR-based cohort for this ultra-rare entity; the largest single reports are multi-family pedigree studies (originally Czech and additional smaller families; Irobi et al. 2004, PMID:15122253).

**Synonyms:** Distal HMN type IIA; dHMN2A; HMND2; hereditary motor neuronopathy, distal, autosomal dominant, 2; distal spinal muscular atrophy (older, now discouraged terminology, since it is a peripheral axonal — not solely anterior-horn-cell — disorder in molecular terms, though clinically classified with the "distal SMA" phenotype group). CMT2L is the allelic disorder designation when sensory findings are documented in *HSPB8*-mutation carriers.

---

## 2. Etiology

**Disease Causal Factor:** Monogenic — heterozygous, dominantly acting missense mutation in ***HSPB8*** (chromosome 12q24.23), encoding the small heat shock protein HSPB8/HSP22/αB-crystallin-domain chaperone family member. No environmental or infectious cause is implicated; this is a pure Mendelian etiology.

**Genetic Risk Factors:**
- **Causal variants:** The founding and most extensively studied mutations are two missense substitutions at the *same* codon, **p.Lys141Asn (K141N)** and **p.Lys141Glu (K141E)**, both located in the α-crystallin domain of HSPB8 (Irobi et al. 2004, PMID:15122253). K141N arises from c.423G>C (originally described in a large Czech family; also independently reported as c.423G>T in a Chinese CMT2L family by Tang et al. 2005). "This hot-spot residue is essential to the structural and functional integrity of the small heat-shock protein" — mutation of the analogous lysine in other small heat-shock proteins (e.g., αB-crystallin, HSPB1) likewise causes human disease, indicating a shared structural vulnerability across the sHSP family (Irobi et al. 2004, Nature Genetics 36:597–601, PMID:15122253).
- Subsequent reports have expanded the *HSPB8* mutational spectrum to include additional missense variants in the N-terminal and α-crystallin domains (causing dHMN/CMT2L) versus C-terminal frameshift variants (causing a distinct **myopathy** phenotype with rimmed vacuoles — see Section 4) (Ghaoui et al. 2016 *Neurology*, PMID: [26718575](https://pubmed.ncbi.nlm.nih.gov/26718575/); Rashed et al. 2025, PMC:11989117).
- **Modifier/susceptibility loci:** None established. No GWAS or PheGenI signal exists for this ultra-rare Mendelian disorder.
- **Genetic mechanism:** Dominant-negative / toxic gain-of-function — see Section 6.

**Environmental Risk Factors:** None identified; this is not a disease with documented toxin, occupational, or lifestyle contribution to onset or severity.

**Protective Factors:** No genetic or environmental protective factors have been reported. No modifier alleles ameliorating phenotype are documented in the literature to date.

**Gene-Environment Interactions:** None reported; disease expression appears to be driven by the genotype itself (fully penetrant dominant trait) rather than by any documented environmental interaction.

---

## 3. Phenotypes

### Primary motor phenotype (symptoms/signs)
- **Distal lower-limb weakness and atrophy**, beginning with the extensor hallucis longus/big-toe extensors and progressing to the anterior compartment (tibialis anterior, peroneal muscles), consistent with a length-dependent motor axonopathy (OMIM #158590; NCBI GTR C1834692). *Suggested HPO:* HP:0009053 (Distal muscle weakness), HP:0007340 (Lower limb muscle weakness), HP:0003693 (Distal amyotrophy)
- **Foot drop / steppage gait** from anterior compartment weakness — HP:0002380 (steppage gait) is a plausible mapping.
- **Pes cavus / foot deformity** — "Most patients demonstrated pes cavus," with hammer toes, hallux valgus, flat feet, claw toes, and short Achilles tendon variably reported (Rashed et al. 2025, PMC:11989117; MDPI 2025 review). *HPO:* HP:0001762 (Talipes equinovarus)/HP:0001761 (Pes cavus).
- **Progression to hand/forearm involvement** — less severe than lower-limb disease, rarely causing paralysis (NCBI GTR).
- **Reduced/absent deep tendon reflexes** in the lower limbs (areflexia distally) — HP:0001284/HP:0001265.
- **Scoliosis** in a minority of patients (Rashed et al. 2025).
- **Sensory findings:** By definition (as a "pure" motor neuronopathy) sensory examination and nerve conduction are largely normal, though a subset of older/longer-duration patients show mildly decreased vibratory sense distally — an important distinction from the allelic CMT2L phenotype, which carries frank sensory axonal loss (Rashed et al. 2025).

### Phenotype characteristics
- **Age of onset:** Mid-teens to early 30s in most series; OMIM cites 15–25 years for the "classic" HMND2 phenotype; some pedigrees show later, more insidious onset into the 40s.
- **Severity/progression:** Slowly progressive over years to decades; "the disease progresses to complete paralysis of all distal muscles of the lower extremities" in advanced/longstanding cases (OMIM #158590), though many patients retain ambulation with orthotic support for decades.
- **Frequency among affected individuals:** As an autosomal dominant trait, penetrance appears high (though not systematically quantified across large cohorts given rarity); intra-familial variability in severity and rate of progression is described.
- **Course pattern:** Chronic, progressive, non-relapsing; no described remissions.

### Quality of life impact
No dedicated EQ-5D/SF-36 dataset exists for dHMN2A specifically; QOL burden is inferred from the general dHMN/CMT literature (mobility impairment from foot drop, need for ankle-foot orthoses, occasional wheelchair dependence in advanced disease, and standard occupational adaptations for hand involvement). No disease-specific PROMIS instrument has been validated.

---

## 4. Genetic/Molecular Information

**Causal gene:** *HSPB8* (Heat Shock Protein Family B [Small] Member 8; also HSP22, E2IG1, H11; HGNC:5254; NCBI Gene ID 26353; chromosome 12q24.23; OMIM *608014).

**Pathogenic variants:**
- **p.Lys141Asn (K141N)** — c.423G>C (originally Czech pedigree) or c.423G>T (Chinese CMT2L pedigree, Tang et al. 2005); classified pathogenic in ClinVar (variant RCV000002735, NM_014365.3).
- **p.Lys141Glu (K141E)** — same codon, second allele identified in two smaller families by Irobi et al. (2004).
- Additional missense variants in the N-terminal domain and α-crystallin domain reported subsequently, mostly private/small-family variants, causing dHMN or the allelic CMT2L phenotype (Ghaoui et al. 2016, PMID:26718575; Rashed et al. 2025 review, PMC:11989117).
- **Variant type:** All disease-causing dHMN/CMT2L variants described to date are **missense**, clustered at the K141 "hot-spot" residue in the α-crystallin dimerization domain. This contrasts with **frameshift** variants in the C-terminal domain, which extend the HSPB8 reading frame and instead cause a **distal/proximal myopathy with rimmed-vacuole myopathology** (myofibrillar myopathy-13; OMIM #619112) — a genotype-phenotype split within the same gene (Ghaoui et al. 2016; Rashed et al. 2025).
- **Allelic disorders from HSPB8:** dHMN2A/HMND2 (#158590), CMT2L (axonal, sensorimotor; #608673), and myofibrillar myopathy 13 with rimmed vacuoles (#619112/#621078) — all autosomal dominant, same gene, distinguished by variant location/type and the extent of sensory/muscle involvement.
- **Allele frequency:** No general-population carriers of K141N/K141E are reported in gnomAD-scale surveys (consistent with a fully penetrant dominant disease allele at ultra-low population frequency, i.e., de novo/founder private mutations rather than common polymorphisms); a study-specific gnomAD query was not resolved in this search pass and should be verified directly against the gnomAD browser before citing a numeric frequency.
- **Germline vs. somatic:** Exclusively germline; no somatic/mosaic reports.
- **Functional consequence:** **Toxic gain-of-function**, not simple loss-of-function — see Section 6 for mechanism. K141 mutation "eliminate[s] the positive charge of the K141 amino acid," altering HSPB8's normal oligomerization with itself and with partner sHSPs (HSPB1, HSPB2, HSPB3), producing an "increased interaction between HSPB8 and HSPB1" that promotes aberrant intracellular aggregate formation (Irobi et al. 2004, PMID:15122253).

**Modifier genes:** None established.

**Epigenetic information:** No disease-specific DNA methylation, histone modification, or chromatin studies have been reported for HSPB8-related dHMN.

**Chromosomal abnormalities:** None; this is a single-gene point-mutation disorder, not a copy-number or structural chromosomal disease.

*Suggested ontology terms:* Gene — HGNC:5254 (HSPB8); Variant consequence — consider `functional_impact_category: DOMINANT_NEGATIVE` or a gain-of-function qualitative annotation given the aggregate-forming mechanism (see dismech Gain/Loss-of-Function guidance — this is a case for `modifier: GAIN_OF_FUNCTION` on the affected chaperone/autophagy pathway node, paired with `functional_impact_category` on the `GeneticContext` for the specific K141N/K141E variant).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factors have been documented for dHMN2A. As a fully genetically determined autosomal dominant chaperonopathy, environmental modulation of onset/severity has not been systematically studied, and no CTD (Comparative Toxicogenomics Database) gene–chemical interaction records specific to HSPB8-driven dHMN were identified in this search pass.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A dominant germline missense mutation (most commonly K141N or K141E) in the α-crystallin domain of *HSPB8* **leads to** disruption of the positively charged K141 residue required for normal HSPB8 oligomeric structure and chaperone function (Irobi et al. 2004, PMID:15122253).
2. Mutant HSPB8 **results in** abnormal, increased hetero-oligomeric interaction with the partner small heat-shock protein HSPB1 (and other sHSPs, HSPB2/HSPB3) (Irobi et al. 2004).
3. This altered oligomerization **causes** impaired binding of HSPB8 to its obligate co-chaperone **BAG3** within the chaperone-assisted selective autophagy (CASA) complex, reducing the complex's normal function of tagging misfolded/damaged client proteins for autophagic clearance (mechanism reviewed in Rashed et al. 2025, PMC:11989117; and "Chaperonopathies" review, PMC:5155517).
4. Reduced HSPB8–BAG3 CASA function **leads to** formation of autophagosomes that fail to fuse productively with lysosomes — i.e., **impaired lysosomal delivery of autophagosomes** — so that autophagosomes accumulate but do not complete degradative clearance (Kwok et al. 2011, *J Neurochem*, "HspB8 mutation causing hereditary distal motor neuropathy impairs lysosomal delivery of autophagosomes").
5. This autophagy blockade **results in** accumulation of insoluble mutant-HSPB8-containing intracellular aggregates within motor neurons — this step is *inferred largely from cellular/mouse model data* rather than directly demonstrated in human postmortem tissue, given the rarity of autopsy material.
6. Aggregate accumulation, together with direct mitochondrial toxicity of the mutant protein, **causes** mitochondrial dysfunction — reduced mitochondrial membrane potential, mitochondrial aggregation, and increased oxidative stress — demonstrated directly in patient-derived dermal fibroblasts (ScienceDirect, "Mutant HSPB8 causes protein aggregates and a reduced mitochondrial membrane potential in dermal fibroblasts from distal hereditary motor neuropathy patients") and rescued in vitro by the antioxidant/Nrf2-pathway activator L-3-n-butylphthalide (PMC:5506380).
7. In parallel, mutant HSPB8 expression **leads to** selective **neurite degeneration in motor neurons** — a marked reduction in neurite number and length, occurring **independently of cell-body apoptosis** — while sensory neurons show only mild effects and cortical neurons are unaffected, explaining the motor-selective clinical phenotype (Irobi et al. 2010, *Hum Mol Genet* 19:3254–3265, PMID:20538880).
8. The combination of a length-dependent "dying-back" distal axonopathy (steps 6–7) with impaired mitochondrial bioenergetics along the long peripheral motor axon **results in** progressive distal motor axon loss, documented directly in a knock-in mouse model as reduced density of large- and medium-caliber myelinated axons in the sciatic nerve, "similar to severe peripheral axon loss reported in postmortem neuropathological analysis of dHMN patients" (Bouhy et al./knock-in study, *Acta Neuropathol* 2017, PMC:5756276).
9. Distal motor axon loss **causes** denervation of distal lower-limb (and later upper-limb) skeletal muscle, **leading to** the clinical phenotype of length-dependent distal weakness, atrophy, areflexia, and secondary orthopedic deformity (pes cavus) that defines dHMN2A.

**Branch point — the myopathy allelic phenotype:** A distinct class of *HSPB8* C-terminal frameshift mutations bypasses steps 2–3 above and instead **directly disrupts HSPB8's normal chaperone role within skeletal muscle sarcomeres/myofibrils**, causing primary myofibrillar pathology with rimmed vacuoles rather than (or in addition to) axonal motor neuron disease (Ghaoui et al. 2016, PMID:26718575).

### Molecular Pathways
- **Chaperone-assisted selective autophagy (CASA)** — the central pathway: HSPB8–BAG3–HSPC70(HSC70)–CHIP(STUB1) complex, normally responsible for autophagic clearance of misfolded, aggregation-prone client proteins (e.g., stress-induced unfolded proteins, filamin, desmin-like intermediate filaments in the muscle context). *GO term:* GO:0061684 (chaperone-mediated autophagy) and GO:1904715 (negative regulation of chaperone-mediated autophagy) are candidates; also GO:0051085 (chaperone cofactor-dependent protein refolding).

### Cellular Processes
- Impaired macroautophagy / autophagosome-lysosome fusion (GO:1901097, negative regulation of autophagosome maturation, is a plausible candidate; verify via OAK before binding).
- Protein aggregation (GO:0051503-adjacent processes; consider GO:0034976, response to endoplasmic reticulum stress, if aggregate-induced proteostatic stress is emphasized).
- Neurite/axon degeneration independent of apoptosis — a "dying-back" axonopathy process, distinct from classical caspase-driven programmed cell death.
- Oxidative stress and mitochondrial dysfunction (elevated ROS, reduced membrane potential, altered Bax/Bcl-2 ratio) (PMC:5506380).

### Protein Dysfunction
Loss of normal HSPB8 chaperone oligomerization; the K141 substitution is described as producing a toxic, aggregation-prone conformer rather than a simple null allele — i.e., dominant gain-of-toxic-function, corroborated by the knock-in/knock-out mouse comparison in which **only the knock-in (mutant-expressing) mice, not the knock-out (null) mice, developed the neuropathy phenotype**, directly demonstrating that toxic gain-of-function — not haploinsufficiency — drives the peripheral neuropathy (Bouhy et al., *Acta Neuropathol* 2017, PMC:5756276). *Suggested UniProt/ontology:* UniProt Q9UJY1 (HSPB8_HUMAN); Pfam PF00011 (HSP20 family/alpha-crystallin domain).

### Metabolic Changes
Mitochondrial bioenergetic impairment (reduced membrane potential) and increased oxidative stress in patient-derived fibroblasts, ameliorable in vitro by Nrf2-pathway activation (PMC:5506380) — indicates a downstream metabolic/redox consequence of the primary proteostatic lesion rather than a primary intrinsic metabolic-gene defect.

### Immune System Involvement
No autoimmune or inflammatory component has been described; this is a cell-autonomous proteostatic/axonal-transport disorder.

### Tissue Damage Mechanisms
Length-dependent axonal ("dying-back") degeneration of the longest peripheral motor axons (a mechanism shared conceptually with other distal axonopathies), driven by impaired autophagic quality control and mitochondrial dysfunction rather than by primary demyelination (nerve conduction studies in dHMN generally show axonal, not demyelinating, features).

### Biochemical Abnormalities
Defective HSPB8–BAG3 binding affinity is the specific measurable biochemical lesion of the K141N/K141E mutants (Rashed et al. 2025); this is a chaperone-binding defect rather than a classical enzyme deficiency or ion-channel defect.

### Advanced/Omics Profiling
No transcriptomic (GEO/ArrayExpress), proteomic, metabolomic, or single-cell datasets specific to human dHMN2A patient tissue were identified in this search pass — reflecting the extreme rarity of the disease and the reliance on model systems (fibroblasts, iPSC-derived motor neurons, mouse, and Drosophila) for mechanistic work. This is a documented data gap rather than an assertion of absence.

*Suggested GO terms for pathophysiology nodes:* GO:0006457 (protein folding), GO:0061684 (chaperone-mediated autophagy), GO:0016239 (positive regulation of macroautophagy) — modifier DECREASED for the mutant/impaired step, GO:0007005 (mitochondrion organization), GO:0055114-adjacent oxidative stress terms.
*Suggested CL terms:* CL:0000100 (motor neuron); CL:0000393 (electrically responsive cell — lower motor neuron subtype terms may be more specific, e.g., CL:0000516 lower motor neuron, pending OAK verification); CL:0002620 (skin fibroblast, for the in vitro dermal fibroblast model).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Peripheral nervous system — the distal motor axon of lower motor neurons, particularly those innervating the longest nerves (fibular/peroneal distribution to foot/toe extensors).
- **Secondary:** Skeletal muscle (secondary denervation atrophy of anterior compartment leg muscles, later intrinsic hand muscles); skeletal system (secondary pes cavus, hammer toes, scoliosis as orthopedic consequences of chronic denervation and muscle imbalance).
- **Body systems:** Nervous system (peripheral motor) primarily; musculoskeletal system secondarily. Sensory and autonomic nervous systems are largely spared, distinguishing dHMN clinically from Charcot-Marie-Tooth disease proper.

*Suggested UBERON terms:* UBERON:0001021 (nerve) / UBERON:0035965 (peripheral nerve) generically, or more specifically UBERON:0001511 (common fibular nerve) given foot-extensor predominance; UBERON:0001015 (musculature of limb) / UBERON:0007827 (anterior compartment of leg) for the muscle groups most affected.

**Tissue and cell level:**
- Motor neuron cell bodies reside in the anterior horn of the spinal cord (UBERON:0002261 anterior horn), but the *pathology* is axonal (distal axonopathy), not primarily anterior-horn-cell loss — an important mechanistic distinction from classical spinal muscular atrophy.
- Cell type: lower (peripheral) motor neuron (CL:0000100 motor neuron; more specific CL term for alpha lower motor neuron pending verification).
- Skeletal muscle fibers show secondary denervation-pattern (grouped) atrophy — CL:0000188 (skeletal muscle fiber cell).

**Subcellular level:**
- Autophagosomes/lysosomes (GO:0005776 autophagosome; GO:0005764 lysosome) — site of the CASA-complex clearance defect.
- Mitochondria (GO:0005739) — site of documented dysfunction (reduced membrane potential, increased ROS).
- Cytoplasmic protein aggregates (a GO Cellular Component term for "inclusion body," e.g., GO:0016234 inclusion body, is a plausible binding pending OAK check).

**Localization:** Bilateral, symmetric, length-dependent — lower limbs affected before/more severely than upper limbs; no reported lateralization or asymmetry.

---

## 8. Temporal Development

- **Onset:** Adolescent-to-adult onset (mid-teens to early 30s in most reported families; OMIM cites 15–25 years for the classic phenotype). Onset pattern is insidious, not acute — patients first notice difficulty with toe/foot extension (steppage/tripping) rather than an abrupt event.
- **Progression:** Slowly progressive over 5–10+ years from initial toe/foot symptoms to lower-leg atrophy and gait disturbance (NCBI GTR C1834692 narrative); further slow progression over decades to hand/forearm involvement in a subset. No defined discrete "stages" (early/intermediate/advanced/end-stage) have been formally codified for this disorder, unlike some cancer or storage-disease staging systems.
- **Course pattern:** Chronic, progressive, non-relapsing, non-remitting. No spontaneous or treatment-induced remission has been reported (no disease-modifying treatment currently exists — see Section 12).
- **Disease duration:** Lifelong; not self-limited. Life expectancy itself is not thought to be shortened (see Section 11), but functional motor disability accumulates over a normal lifespan.
- **Critical periods:** None formally defined; earlier diagnosis/genetic confirmation is valuable chiefly for genetic counseling and clinical trial eligibility rather than for a defined intervention window, since no disease-modifying therapy yet exists.

---

## 9. Inheritance and Population

**Epidemiology:**
- Orphanet lists the umbrella "Distal hereditary motor neuropathy type 2" (ORPHA:139525, spanning HSPB1/HSPB8/other causal genes) at a prevalence of **<1/1,000,000**.
- For the broader dHMN category (all genetic causes combined), population-based series report a prevalence of **~2.14–2.3 per 100,000**, with HSPB1 and HSPB8 among the more frequently implicated genes, though still individually very rare (search synthesis from multiple dHMN cohort studies).
- No incidence figures (new cases per year) specific to HSPB8-caused dHMN2A were located; given the extreme rarity, only cumulative pedigree/case counts (originally a large Czech family plus additional smaller families reported by Irobi et al. 2004, with subsequent single-family/sporadic reports worldwide) exist rather than population-based incidence estimates.

**Inheritance pattern:** **Autosomal dominant** (OMIM #158590; Orphanet). All well-characterized causal missense variants (K141N, K141E, and subsequent reports) act dominantly. Note that HSPB8-related myofibrillar myopathy (the C-terminal frameshift allelic disorder) is likewise autosomal dominant, though rare biallelic/recessive presentations of the *related* HSPB1 gene disorder have been separately reported in the literature (not to be conflated with HSPB8/dHMN2A).

**Penetrance:** Appears high/complete within reported pedigrees, though this has not been formally quantified across a large ascertained cohort (a data gap consistent with the disease's rarity).

**Expressivity:** Variable — intra-familial variation in age of onset and rate/severity of progression is documented even among carriers of the identical K141N or K141E variant, consistent with variable expressivity rather than distinct genetic causes.

**Genetic anticipation:** Not reported; this is not a repeat-expansion disorder (no trinucleotide/other repeat mechanism implicated in HSPB8 pathogenesis).

**Germline mosaicism:** Not specifically reported for HSPB8-dHMN2A in the literature surveyed.

**Founder effects:** The original K141N mutation was described in a large Czech kindred; independent K141N mutations have subsequently been reported in genetically distinct families (e.g., a Chinese CMT2L family via an independent nucleotide substitution at the same codon, c.423G>T vs. c.423G>C), indicating the K141 codon is a true mutational hot-spot rather than solely an identity-by-descent founder allele — i.e., recurrent independent mutation at this residue across populations (Irobi et al. 2004; Tang et al. 2005).

**Consanguinity:** Not a relevant risk factor given autosomal dominant inheritance.

**Carrier frequency:** Not applicable/reported in the dominant-disease sense (there is no "carrier" state distinct from being an affected heterozygote); population allele frequency of the specific pathogenic K141N/K141E variants in reference databases (gnomAD) was not confirmed as absent-vs-ultra-rare in this search pass and should be checked directly in gnomAD before making a quantitative claim in the KB entry.

**Population demographics:** No specific ethnic or geographic enrichment beyond the originally reported Czech and Chinese pedigrees has been systematically documented; reports since 2004 span multiple populations, consistent with private/recurrent mutation rather than a single ancestral founder confined to one population. Sex ratio: no skewing reported (autosomal, non-sex-linked inheritance).

---

## 10. Diagnostics

**Clinical Tests:**
- **Nerve conduction studies (NCS)/Electromyography (EMG):** The key functional test — demonstrates a length-dependent, predominantly **motor axonal** neuropathy/neuronopathy with normal or near-normal sensory nerve action potentials, distinguishing dHMN from CMT2. EMG shows chronic denervation/reinnervation changes in distal lower-limb (and later hand) muscles.
- **Nerve conduction velocities:** Typically normal-to-mildly reduced (axonal, not demyelinating, pattern) — motor amplitudes reduced with length-dependence.
- **Muscle biopsy:** Not routinely required for dHMN diagnosis (relevant instead to the allelic HSPB8 myopathy phenotype, where rimmed vacuoles and myofibrillar pathology are the diagnostic histologic hallmark).
- **Imaging:** No disease-specific imaging biomarker; muscle MRI may show a pattern of denervation-related fatty atrophy in affected distal muscle groups in advanced disease, but this is non-specific.

**Genetic Testing:**
- Given phenotypic overlap among dHMN- and CMT2-causing genes, a **multi-gene next-generation sequencing panel** covering *HSPB8, HSPB1, BSCL2, GARS1, DNAJB2, DYNC1H1, TRPV4, FBXO38*, and other established dHMN/CMT2 genes is the recommended first-tier approach in current practice, rather than single-gene *HSPB8* sequencing alone, given that "HSPB1, GARS, BICD2, and DNAJB2 are among the most frequent dHMN genes" — with *HSPB8* itself a less common but well-established cause (search synthesis).
- **Single-gene testing** for *HSPB8* is appropriate when a specific familial K141N/K141E (or other reported) variant is already known in the family, for cascade testing of at-risk relatives.
- **Whole-exome/genome sequencing** is appropriate when panel testing is non-diagnostic, given ongoing gene discovery in this heterogeneous disease category.
- **Chromosomal microarray/karyotyping/FISH:** Not indicated — this is a single-nucleotide-variant disorder, not a copy-number or structural chromosomal disease.
- **Repeat-expansion testing:** Not indicated (no repeat-expansion mechanism).

**Clinical Diagnostic Criteria:** No formal consensus diagnostic-criteria document (akin to DSM/ICD operational criteria) exists specifically for dHMN2A; diagnosis rests on the clinical phenotype (length-dependent, predominantly-motor, distal weakness with normal sensory studies) plus confirmatory *HSPB8* molecular genetic testing.

**Differential diagnosis:** Charcot-Marie-Tooth disease type 2 (particularly CMT2F/HSPB1, CMT2L, and other axonal CMT2 subtypes) — distinguished by presence of sensory involvement in CMT2; other dHMN genetic subtypes (HSPB1/dHMN "2B," BSCL2/dHMN-V, GARS1, DYNC1H1, TRPV4, FBXO38-distal SMA, DNAJB2/CMT2T); distal spinal muscular atrophy of other genetic causes; and acquired distal motor neuropathies (multifocal motor neuropathy with conduction block — distinguished by acquired/adult onset with anti-GM1 antibodies and treatment responsiveness, an important reversible mimic to exclude).

**Screening:** No population or newborn screening program exists for this ultra-rare autosomal dominant disorder; cascade genetic testing of at-risk first-degree relatives once a familial variant is identified is the standard approach, alongside genetic counseling given full penetrance expected.

---

## 11. Outcome/Prognosis

**Survival and mortality:** Life expectancy is generally considered **normal/near-normal** — dHMN2A is a disorder of progressive motor disability rather than a life-shortening systemic or respiratory-failure disease in its typical (missense, dHMN-only) form. (Contrast with the allelic myofibrillar myopathy phenotype from C-terminal frameshift variants, where "patients may develop respiratory muscle weakness and, therefore, require periodic monitoring of their respiratory status" — Rashed et al. 2025 — indicating that respiratory compromise is a feature of the *myopathy* allelic disorder rather than of classic dHMN2A itself.)

**Morbidity and function:** Progressive distal lower-limb weakness leads to gait disturbance, foot deformity (pes cavus, hammer toes), and eventual need for ankle-foot orthoses or, in advanced/longstanding disease, wheelchair assistance for some patients ("progresses to complete paralysis of all distal muscles of the lower extremities," OMIM #158590, describing the more severe end of the spectrum). Upper-limb involvement is typically milder and less disabling.

**Complications:** Secondary orthopedic complications (pes cavus, scoliosis, joint contractures from muscle imbalance) are the principal disease-related morbidity; no systemic organ complications are typical of the pure dHMN2A phenotype.

**Recovery potential:** None — this is a progressive, non-remitting neurodegenerative process; supportive/rehabilitative care can slow functional decline (bracing, physical therapy) but does not reverse axonal loss.

**Prognostic factors:** Earlier age of onset within a family may correlate loosely with a longer disease course/more severe eventual disability (as is typical for many length-dependent axonal neuropathies), though this has not been formally validated as a quantitative prognostic model for dHMN2A specifically. No validated prognostic biomarker exists.

---

## 12. Treatment

**Current status:** **No disease-modifying or curative therapy exists.** Management is entirely supportive (Rashed et al. 2025, PMC:11989117: "Currently, no cure is available for HSPB8-associated neuromuscular disorders, but numerous therapeutic strategies are under investigation").

**Supportive and Rehabilitative Care** *(NCIT terms suggested)*:
- **Physical therapy** (NCIT:C15302) — maintain range of motion, prevent contracture, strengthen unaffected muscle groups.
- **Occupational therapy** (relevant NCIT term for hand-function preservation as upper-limb involvement progresses).
- **Orthotic/bracing management** — ankle-foot orthoses for foot drop (a device/procedure combination; per dismech convention, bind the clinical action, e.g., a rehabilitation/orthopedic-device NCIT term, and attach the device concept via the `qualifiers` predicate-value pattern rather than in `treatment_term` directly).
- **Orthopedic surgical correction** (NCIT:C15329, Surgical Procedure; more specific NCIT:C16186 Orthopedic Surgical Procedure) — for severe pes cavus or tendon-imbalance correction in advanced disease.
- **Genetic counseling** (NCIT:C15240) — essential given autosomal dominant inheritance and full penetrance.

**Experimental/Investigational approaches** (preclinical stage; no human clinical trials identified for dHMN2A specifically in this search pass):
1. **RNA interference (siRNA) knockdown of mutant HSPB8** — tested in a knock-in mouse model and patient-derived iPSC motor neurons; the 2025 study concluded that "RNA interference-mediated reduction of HSPB8/Hspb8 expression might not be the best therapeutic strategy to treat dHMN/CMT2L, unless a higher viral load and earlier treatment can be applied" (Vendredy et al. 2025, *J Gene Med*, PMID:39972648) — i.e., a **negative/inconclusive preclinical result**, important to record honestly as such rather than as a positive therapeutic lead.
2. **Small-molecule antioxidant/Nrf2-pathway activation** — L-3-n-butylphthalide rescued mitochondrial dysfunction and oxidative stress in K141N-mutant patient fibroblasts in vitro (PMC:5506380) — an in vitro proof-of-concept only, not yet advanced to animal or human testing for this indication as far as identified.
3. **PINK1/Parkin-mediated mitophagy enhancement** — overexpression of PINK1 and Parkin "ameliorate[d] the loss of motor activity and mitochondrial dysfunction induced by peripheral neuropathy-associated HSPB8 mutants" in a *Drosophila* model (PMC:10045361) — a preclinical genetic-rescue proof-of-concept, not a drug-ready therapeutic.
4. **Exogenous HSPB8/chaperone-replacement delivery** and **other small-molecule chaperone modulators** are cited as under investigation but not yet at a reportable preclinical milestone in the sources reviewed (Rashed et al. 2025 review).

**Treatment outcomes:** No approved pharmacotherapy exists to report response rates or adverse-event profiles against; the RNAi mouse study above is the most advanced (negative) efficacy readout identified.

**Treatment strategy:** No formal treatment algorithm exists; management follows general neuromuscular-disease supportive-care pathways (multidisciplinary neuromuscular clinic model: neurology, physiatry, orthopedics, physical/occupational therapy, genetic counseling).

**Personalized medicine:** Not applicable at this time — no genotype-specific (e.g., K141N-specific) approved intervention exists.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable risk factor to intervene on for a fully penetrant autosomal dominant Mendelian disorder); the closest analog is **reproductive genetic counseling and prenatal/preimplantation genetic testing (PGT-M)** for at-risk families with a known familial *HSPB8* variant.

**Secondary prevention:** Early molecular diagnosis via **cascade genetic testing** of at-risk relatives once a familial pathogenic variant is identified, enabling early referral to physical therapy/orthotic management before significant deformity develops — though this does not alter the underlying neurodegenerative trajectory absent a disease-modifying therapy.

**Tertiary prevention:** Orthopedic surveillance and early bracing/surgical intervention to prevent secondary complications (fixed contracture, severe pes cavus) that would otherwise compound functional disability.

**Immunization:** Not applicable (non-infectious, non-immune-mediated disease).

**Genetic counseling:** Central to management — autosomal dominant inheritance with (apparently) high penetrance means each child of an affected individual has a 50% recurrence risk; counseling should address variable expressivity (i.e., an affected parent cannot precisely predict a child's future severity).

**Public health/environmental interventions:** Not applicable; no environmental risk factor has been identified to target.

---

## 14. Other Species / Natural Disease

No naturally occurring HSPB8-associated motor neuropathy has been reported in companion animals or wildlife (no OMIA entry identified in this search pass for a spontaneous HSPB8 veterinary phenotype). All non-human data derive from **engineered genetic models** (Section 15) rather than natural disease.

**Orthologous gene:** Mouse *Hspb8* (MGI:2135756), used for the principal knock-in/knock-out model (see below); Drosophila ortholog **HSP67Bc** used in fly rescue studies (PMC:10045361).

---

## 15. Model Organisms

**Mouse models:**
- **Hspb8 K141N knock-in / Hspb8 knock-out comparison mouse** (Bouhy et al., *Acta Neuropathologica* 2017, PMC:5756276): "Homozygous expression of Hspb8-K141N mutation induces motor behavioural and electrophysiological impairments without sensory abnormalities similar to the dHMN type II phenotype." Sciatic nerve histology in homozygous knock-in mice showed significantly reduced densities of large and medium myelinated axons, "similar to severe peripheral axon loss reported in postmortem neuropathological analysis of dHMN patients" — a **high-fidelity** recapitulation of the human axonal-loss phenotype. Critically, the **knock-out** (null) mice did **not** develop the neuropathy but instead showed abnormal mitochondrial accumulation in distal muscle with otherwise normal nerve morphology — directly demonstrating that the disease mechanism is **toxic gain-of-function of the mutant protein**, not haploinsufficiency/loss-of-function. Molecularly, presymptomatic knock-in mice showed **low autophagy potential** in sciatic nerve, and post-symptomatic mice accumulated Hspb8 aggregates — mapping directly onto the CASA/autophagy mechanism proposed from cell-based studies. This model is the **flagship reproducible in vivo model** for dHMN2A/CMT2L and is directly usable for evaluating the modeled-mechanism links in a KB entry (`RECAPITULATES`, high fidelity, for the axonal loss and autophagy-deficit nodes; useful also for the RNAi and other therapeutic-testing studies below, which were performed in this same model).
- Earlier **transgenic overexpression** mouse models (HSP27/HSPB1-S135F referenced in the HSPB1 literature, not HSPB8 — noted here only to avoid cross-gene conflation) are **not** the HSPB8/dHMN2A model and should not be cited under this entry.

**iPSC-derived motor neuron models:** Patient-derived induced pluripotent stem cell (iPSC) lines differentiated to motor neurons have been used as the human cellular substrate for RNAi therapeutic-sequence optimization (Vendredy et al. 2025, PMID:39972648) and (in the parallel HSPB1 literature) for HDAC6-inhibitor rescue-of-axonal-transport studies — the HSPB8 iPSC motor neuron system itself is an appropriate **IN_VITRO, high relevance to human motor neuron biology** model, though with the caveat that iPSC-motor-neuron differentiation protocols do not fully recapitulate adult neuromuscular junction/long-axon biology (a translatability caveat worth recording as a `limitations`/`divergence` note if used in a modeled-mechanism link).

**Drosophila models:** Pan-neuronal overexpression of human mutant HSPB8 in flies reduced motor activity and impaired mitochondrial function in neuronal tissue; co-expression of **PINK1 and Parkin** rescued both the motor-activity deficit and mitochondrial dysfunction, implicating impaired mitophagy as a tractable downstream node (PMC:10045361). This is a **genetic modifier/rescue** model — useful for `PERTURBS`/`RESCUES` relationship links rather than as a primary disease-recapitulation model, since Drosophila motor circuitry differs substantially from vertebrate peripheral motor axon biology (a `SPECIES_MISMATCH`/`BOUNDARY_OMISSION`-type divergence would apply if used for an upward-extrapolating claim about human peripheral nerve pathology).

**Cellular (non-neuronal) models:** Patient-derived **dermal fibroblasts** carrying K141N showed reduced mitochondrial membrane potential and increased protein aggregation — a peripheral, non-neuronal readout of the same core proteostatic/mitochondrial lesion, useful as a `MEASURES`-type link for the mitochondrial-dysfunction node given its accessibility (skin biopsy) relative to motor neuron tissue, with the obvious limitation that fibroblasts are not the disease-relevant cell type (a `BOUNDARY_OMISSION`/`PROXY_QUANTITY` divergence if used to support a motor-neuron-specific claim).

**Model limitations (general):** No model to date fully recapitulates the decades-long, adult-onset human clinical course within a normal mouse/fly lifespan; the knock-in mouse is the most translationally proximate model but required homozygous genotype to manifest overt phenotype, whereas human disease is dominantly penetrant in the heterozygous state — an important **fidelity caveat** to record explicitly in any `ModelMechanismLink.limitations`/`divergences` block (a `POPULATION_MISMATCH` or zygosity-related `CALIBRATION_PROVENANCE` divergence type may apply).

---

## Summary Table of Key Citations

| Finding | Citation |
|---|---|
| Original mapping/mutation discovery (K141N, K141E) | Irobi et al. 2004, *Nat Genet* 36:597–601, PMID:[15122253](https://pubmed.ncbi.nlm.nih.gov/15122253/) |
| Independent Chinese CMT2L family, K141N (c.423G>T) | Tang et al. 2005 (cited via OMIM *608014) |
| Motor-neuron-specific neurite degeneration mechanism | Irobi et al. 2010, *Hum Mol Genet* 19:3254–3265, PMID:[20538880](https://academic.oup.com/hmg/article/19/16/3254/630038) |
| Impaired autophagosome-lysosome delivery | Kwok et al. 2011, *J Neurochem*, "HspB8 mutation causing hereditary distal motor neuropathy impairs lysosomal delivery of autophagosomes" |
| Fibroblast mitochondrial dysfunction | ScienceDirect, "Mutant HSPB8 causes protein aggregates and a reduced mitochondrial membrane potential in dermal fibroblasts…" |
| NBP/Nrf2 rescue in vitro | PMC:[5506380](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5506380/) |
| Knock-in/knock-out mouse, toxic gain-of-function proof | Bouhy et al. 2017, *Acta Neuropathol*, PMC:[5756276](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5756276/) |
| C-terminal frameshift → myopathy allelic phenotype | Ghaoui et al. 2016, *Neurology*, PMID:[26718575](https://pubmed.ncbi.nlm.nih.gov/26718575/) |
| PINK1/Parkin Drosophila rescue | PMC:[10045361](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10045361/) |
| RNAi therapeutic trial in knock-in mouse (negative) | Vendredy et al. 2025, *J Gene Med*, PMID:[39972648](https://pubmed.ncbi.nlm.nih.gov/39972648/) |
| Comprehensive 2025 clinical/molecular spectrum review | Rashed, Nath, Milone 2025, *Int J Mol Sci*, PMC:[11989117](https://pmc.ncbi.nlm.nih.gov/articles/PMC11989117/) |
| OMIM phenotype/gene entries | OMIM [#158590](https://www.omim.org/entry/158590) (HMND2); OMIM [*608014](https://omim.org/entry/608014) (HSPB8) |
| Orphanet umbrella entry | Orphanet [ORPHA:139525](https://www.orpha.net/en/disease/detail/139525) |

**Key data gaps to flag for the KB entry:** (1) no large-cohort natural-history or QOL dataset specific to HSPB8-dHMN2A; (2) no confirmed gnomAD population-frequency figure for K141N/K141E verified in this pass — check directly before citing a number; (3) no human clinical-trial (NCT) record identified for dHMN2A specifically; (4) exact penetrance/expressivity statistics not formally quantified in the literature reviewed.