---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-01T10:50:38.574460'
end_time: '2026-10-01T10:59:14.439852'
duration_seconds: 515.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia 27A
  mondo_id: MONDO:0008654
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
  - claude-opus-5-5
  web_search_requests: 1
  num_turns: 52
  total_cost_usd: 3.5276192
  session_id: ac1a88ea-2c9b-413f-b523-61fbe10d3c9d
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 7
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 4
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 35
  on_topic: 20
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 59
  verified: 57
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  unresolvable_prefixes:
  - ORPHA
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia 27A
- **MONDO ID:** MONDO:0008654 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia 27A** covering all of the
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

I'm pulling the core SCA27A literature from PubMed now (the FGF14 point-variant and deletion papers, plus the mouse models) so I can write the report from abstracts I've actually checked.

I found about 40 FGF14/SCA27 abstracts already cached in the repo. I'm reading those now to pull exact quotes before I write the report.

Still reading: the 2026 SCA27A knock-in mouse paper and the episodic-ataxia (EA9) case series are the most important cached sources, so I'm going through those next.

Direct PubMed pages are blocked, so I'm switching to Europe PMC to get the uncached abstracts.

Found several recent SCA27A-specific papers (NYS4 structural variants 2023, childhood-onset series 2026, patient iPSC lines 2026), so I'm pulling their abstracts now.

I have the core literature. Now checking ontology IDs against the repo's local term caches so the suggested bindings aren't from memory.

# Spinocerebellar Ataxia 27A (SCA27A; ATX‑FGF14): research report for the dismech entry

**Target:** MONDO:0008654 *spinocerebellar ataxia 27A* (the label matches `cache/mondo/terms.csv`) · **Gene:** *FGF14* (`hgnc:3671`) · **Category:** Mendelian
**Prepared:** 2026‑10‑01

**How this was sourced.** Quotes marked **[cached]** were read from the repository's `references_cache/` files. Quotes marked **[EPMC]** were taken from the abstract text Europe PMC returned. **[EPMC]** quotes have not been checked against a cache file, so run `just fetch-reference PMID:…` and then `just count-verified-snippets` before using any of them as an evidence snippet.

Ontology IDs marked ✔ were looked up in the repository's `cache/<prefix>/terms.csv` during this session. Unmarked IDs are suggestions and need a lookup before they are bound.

I could not reach OMIM (HTTP 403), ClinGen or ClinVar directly; those gaps are flagged where they matter.

---

## 1. Disease information

**Overview.** SCA27A is a very rare autosomal dominant cerebellar ataxia. It is caused by heterozygous loss‑of‑function changes in *FGF14*:
- missense variants
- nonsense and frameshift variants
- splice variants
- an in‑frame deletion
- partial duplication
- deletions of 13q33.1
- balanced translocations that disrupt the gene

*FGF14* encodes intracellular fibroblast growth factor 14 (iFGF14, also called FHF4). This protein is not secreted. It binds the C‑terminus of voltage‑gated sodium (Nav) channel α subunits and sets their availability.

The typical picture is:
- postural tremor in childhood
- slowly progressive cerebellar ataxia from young adulthood
- nystagmus and other oculomotor signs
- dyskinesias
- cognitive, behavioural and psychiatric features
- in some patients, fever‑ or stress‑triggered episodic ataxia

The suffix "A" separates this disease from **SCA27B (GAA‑FGF14 ataxia)**. SCA27B is a common late‑onset ataxia caused by an intronic GAA repeat expansion in the same gene, and it already has its own entry (`kb/disorders/Spinocerebellar_Ataxia_27B.yaml`). Evidence from SCA27B papers must not be cited for SCA27A; this is a Named Entity Confusion risk.

**Key identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0008654 spinocerebellar ataxia 27A | ✔ |
| OMIM | #193003 SCA27A | from an OMIM mirror |
| Orphanet | ORPHA:98764 | listed on the OMIM mirror's external links; no `ORPHA_98764.md` cache exists, so fetch it before citing |
| Gene | FGF14, OMIM *601515, `hgnc:3671` ✔, 13q33.1 | |
| ICD‑10 | G11.8 (other hereditary ataxias) | not confirmed |
| MeSH | Spinocerebellar Degenerations / Spinocerebellar Ataxias | indexing terms on the source papers |

**Synonyms:**
- SCA27, spinocerebellar ataxia type 27
- ATX‑FGF14 (the newer nomenclature; Türkdoğan 2025 writes "ATX‑FGF/SCA27A")
- FGF14‑related ataxia
- *Nystagmus 4, congenital, autosomal dominant (NYS4)* — now explained by an *FGF14* deletion (Ceroni 2023)
- *Episodic ataxia type 9 (EA9)*, as proposed by Piarroux 2020 for the episodic presentation

**Nature of the data.** Everything below is aggregated from published families and case reports. There are no EHR or registry cohorts. The total published case count is in the low hundreds at most: a 2018 review counted 32 cases with clinical detail, and a 2025 review counted 32 cases in 11 families for microdeletions alone.

---

## 2. Etiology

- **Cause.** Heterozygous germline *FGF14* loss of function, which acts mainly through haploinsufficiency (§4 and §6). There are no environmental causes.
- **Genetic risk factors.** Only the causal *FGF14* variants. No modifier genes have been identified.
- **Biallelic loss.** One consanguineous Turkish family had a homozygous truncating variant, c.75del (p.Leu26Serfs\*51) (PMID:39704271):
  - The homozygous child had a severe congenital non‑progressive cerebellar disorder with intellectual disability and paroxysmal non‑kinesigenic dyskinesia.
  - The heterozygous parents had mild gait ataxia and tremor in their 40s.
  - This is consistent with a dosage effect.
- **Triggers rather than risk factors.** Fever, emotional stress and exertion precipitate or worsen episodic attacks (PMID:24252256, PMID:32162847). There is no evidence on causal environmental exposures or protective factors.
- **Gene–environment interaction.** The leading hypothesis is that temperature sensitivity of Nav gating lowers an already reduced Nav reserve below threshold during fever. Coebergh 2014 states: "Sodium channels can be fever sensitive." This is inferred and has not been demonstrated in SCA27A tissue.

---

## 3. Phenotypes

### Frequency data

**Groth & Berman 2018 (PMID:29416937), review of 33 cases [EPMC]:**
> "early-onset tremor (12.1 ± 10.5 years) was present in 95.8%, while gait ataxia tended to present later in life (23.7 ± 16.7 years) and was accompanied by limb ataxia, dysarthria, and nystagmus. Other features of SCA27 that may distinguish it from other SCAs include the potential for episodic ataxia, accompanying psychiatric symptoms, and cognitive impairment."

**Conci 2025 (PMID:41099962), microdeletion carriers, 32 cases in 11 families [EPMC]:**
> "75% (24/32) nystagmus, 46% (15/32) ataxia, 21% (7/32) episodic ataxia, 21% (7/32) tremor, 15% (5/32) dysarthria, 34% (11/32) learning disability, 28% (8/32) neuropsychiatric disease."

### Phenotype table

| Phenotype | HPO suggestion | Onset / course | Frequency | Key source |
|---|---|---|---|---|
| Postural / upper‑limb tremor (often the first sign) | HP:0002174 Postural tremor ✔; HP:0001337 Tremor ✔; HP:0002346 Head tremor ✔ | childhood, mean 12 y; stable or slow | 95.8% (point variants); 21% (deletions) | PMID:16211615, PMID:29416937 |
| Slowly progressive cerebellar ataxia (gait, limb) | HP:0001251 Ataxia ✔ (a *Cerebellar ataxia* term should be looked up; it is not in the cache); HP:0002066 Gait ataxia ✔; HP:0002070 Limb ataxia ✔; HP:0007240 Progressive gait ataxia ✔ | young adult, mean 23.7 y; slow progression | majority (point variants); 46% (deletions) | PMID:12489043, PMID:16211615 |
| Episodic ataxia, often fever‑triggered, lasting days | HP:0002131 Episodic ataxia ✔ | childhood to adult | 21% (deletions); several families | PMID:25566820, PMID:30607796, PMID:32162847, PMID:24252256 |
| Nystagmus (multidirectional, horizontal, gaze‑evoked; infantile in NYS4) | HP:0000639 ✔; HP:0000640 Gaze‑evoked ✔; HP:0000666 Horizontal ✔ | infancy onward | 75% (deletions) | PMID:36207621, PMID:32162847 |
| Saccadic dysmetria, saccadic pursuit | HP:0000571 Hypometric saccades ✔ (the source says "dysmetria", which is not necessarily hypometria) | adult | case level | PMID:30017992 |
| Dysarthria | HP:0001260 ✔ | adult | 15% (deletions); common in point‑variant families | PMID:30017992 |
| Orofacial dyskinesia / dyskinesia | HP:0002310 ✔; HP:0007166 Paroxysmal dyskinesia ✔ | variable | "often present" in the Dutch family | PMID:16211615, PMID:12489043 |
| Paroxysmal non‑kinesigenic dyskinesia (PNKD‑like) | HP:0007166 ✔ | childhood | translocation case; biallelic case | PMID:21600715, PMID:39704271 |
| Parkinsonism (responsive to levodopa/amantadine in one case) | HP:0001300 ✔ | late | rare | PMID:29416937 |
| Low IQ, memory and executive deficits | HP:0100543 Cognitive impairment ✔; HP:0002354 Memory impairment ✔; HP:0001249 Intellectual disability ✔ | developmental or progressive | common | PMID:16211615, PMID:19471976 |
| Learning disability, motor and speech delay | HP:0001270 Motor delay ✔; HP:0000750 ✔; HP:0001263 ✔ | childhood | 34% (deletions) | PMID:32162847, PMID:41099962 |
| Behavioural and psychiatric problems: aggression, depression, ADHD, psychosis | HP:0000708 ✔; HP:0000718 ✔; HP:0000716 ✔; HP:0007018 ✔; HP:0000709 ✔ | childhood or adult | 28% neuropsychiatric (deletions) | PMID:16211615, PMID:32112487 |
| Mild sensory axonal neuropathy, pes cavus | HP:0003390 ✔; HP:0001761 ✔ | adult | occasional (OMIM synopsis; mildly reduced vibration sense in PMID:30017992) | PMID:30017992 |
| Microcephaly, severe ID (translocation daughter) | HP:0000252 ✔ | congenital | single case | PMID:19471976 |
| Trigeminal neuralgia (novel) | HP:0100661 ✔ | adult | single case | PMID:41099962 |
| Cerebellar atrophy on MRI (moderate, late, inconsistent) | HP:0001272 ✔ | late | eldest patients only; MRI often normal | PMID:16211615, PMID:30607796 |

**Abstract quotes supporting the table:**
- **Brusse 2006 (PMID:16211615) [cached]:** "The patients showed a childhood-onset postural tremor and a slowly progressive ataxia evolving from young adulthood. Dyskinesia was often present, suggesting basal ganglia involvement…" and "Neuropsychological testing indicated low IQ and deficits in memory and executive functioning. Behavioral problems were also observed."
- **Coebergh 2014 (PMID:24252256) [cached]:** "mild ataxia and abnormal eye movements repeatedly deteriorated with fever, making him unable to sit or walk during fever episodes."
- **Piarroux 2020 (PMID:32162847) [cached]:** "Attacks were triggered by fever, lasted several days, and had variable frequencies. Nystagmus and/or postural tremor and/or learning disabilities were noticed in individuals harboring FGF14 mutation with or without episodic ataxia."

**Quality‑of‑life impact.** No EQ‑5D, SF‑36 or other formal QoL data exist.
- Most patients stay ambulatory. Piarroux 2020's background states that motor function "is maintained through life in most of the patients."
- In children, the main burden is learning and educational support and fever‑triggered loss of walking.
- In adults, the burden comes from tremor and psychiatric comorbidity.

---

## 4. Genetic and molecular information

**Gene.** *FGF14* is at 13q33.1 (older papers place it at 13q34). It has two major N‑terminal isoforms from alternative first exons, 1A and 1B. **FGF14‑1b is the predominant brain isoform** (PMID:19471976). Residue F145 in FGF14‑1a numbering corresponds to F150 in FGF14‑1b (PMID:41558966).

### Reported pathogenic and likely pathogenic alleles

| Allele | Type | Phenotype | PMID |
|---|---|---|---|
| p.Phe145Ser (F145S; F150S in 1b) | missense | large three‑generation Dutch family (14 affected) | 12489043, 16211615 |
| c.487delA (p.Asp163fs\*12) | frameshift | one of 208 familial ataxia probands | 15470364 |
| t(5;13)(q31.2;q33.1) disrupting FGF14‑1b | balanced translocation | mother and daughter; daughter has microcephaly and severe ID | 19471976 |
| de novo t(13;21) disrupting FGF14 | translocation | PNKD‑like phenotype | 21600715 |
| c.211_212insA (p.Ile71Asnfs\*27) | frameshift | two‑generation episodic‑ataxia family | 25566820 |
| 202 kb 13q33.1 deletion | CNV | three generations; fever‑sensitive ataxia | 24252256 |
| FGF14 deletion | CNV | twin sisters | 28192817 (no abstract available) |
| c.529A>T (p.Lys177\*) | nonsense | Japanese adult, onset at 47 y | 30017992 |
| intron 1 splice variant | splice | sporadic, acetazolamide‑responsive EA | 30607796 |
| c.439G>T (p.Glu147\*); c.486_487del (p.Tyr162\*) | nonsense | two families with fever‑triggered EA ("EA9") | 32162847 |
| 13q33.1 deletion covering FGF14 + ITGBL1 | CNV | Swedish family, 9 with ataxia; psychosis, ADHD | 32112487 |
| 161 kb deletion (FGF14 + ITGBL1); partial FGF14 duplication | CNV | NYS4 family; second nystagmus family | 36207621 |
| p.Val119del | in‑frame deletion | five‑generation family; DBS and 4‑AP response | 40156335 |
| 58 kb and 545 kb deletions | CNV | paroxysmal movement disorder; EA with trigeminal neuralgia | 41099962 |
| c.75del (p.Leu26Serfs\*51), homozygous | biallelic LoF | congenital ataxia, ID, PNKD | 39704271 |

**Variant classification.** I did not reach ClinVar or ClinGen. No `CGGV:` file for FGF14 exists in `references_cache/`, so `gene_disease_validity` should stay absent until a record is fetched. `just clingen-list` will show whether ClinGen has classified *FGF14*–SCA27A; ClinGen's dosage map (`CGDS:HGNC_3671`) is also worth checking, given the deletion data.

**Variant origin and consequence.**
- All alleles are germline. Most are inherited; the t(13;21) was de novo.
- Truncating variants, CNVs and the F145S knock‑in all point to **loss of function / haploinsufficiency** (`functional_impact_category: LOSS_OF_FUNCTION`).
- F145S was originally proposed to act as a **dominant negative** in overexpression systems (PMID:17978045). The 2026 knock‑in mouse instead shows reduced protein and phenocopies the *Fgf14*+/− mouse (PMID:41558966). So `LOSS_OF_FUNCTION` is the better‑supported category, with `DOMINANT_NEGATIVE` recorded as a superseded in‑vitro hypothesis.

**Population frequency.** Variants are absent from controls: p.Lys177\* was absent from 502 Japanese controls and from public databases. Point variants are a rare cause of dominant ataxia. Stevanin 2004 (PMID:15365159) is titled "Mutations in the FGF14 gene are not a major cause of spinocerebellar ataxia in Caucasians", but there is no abstract in the cache to quote. Dalski 2005 found 1 frameshift among 208 familial cases.

**Modifiers and epigenetics.** None reported.

**Chromosomal abnormalities.** Two balanced translocations and several interstitial 13q33.1 deletions (58 kb to 545 kb, often including *ITGBL1*) plus one partial duplication. CNVs are an established mechanism: Ghorbani 2023 (PMID:38058854) [cached] lists FGF14 among the three SCA genes with reported CNVs.

---

## 5. Environmental information

There are no causal environmental, lifestyle or infectious factors. Fever, often from intercurrent viral illness, intense stress and fatigue act as **attack triggers** (PMID:32162847, PMID:24252256). A curator could record fever as an `environmental` entry with `environmental_effect: EXACERBATES` on the episodic node, citing PMID:24252256 or PMID:32162847.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous *FGF14* LoF allele** (truncation, CNV, translocation, or a destabilizing missense such as F145S) leads to **reduced iFGF14 protein**.
   - Demonstrated in the knock‑in mouse: "Western blot analyses confirmed reduced iFGF14 protein expression in cerebellar lysates prepared from Fgf14F145S/+ (and Fgf14+/-) animals" (PMID:41558966) [cached].
   - F145S was originally "predicted to reduce the stability of the protein" by modelling (PMID:12489043).
2. **Reduced iFGF14** leads to **loss of its regulatory binding to the Nav α‑subunit C‑terminus**, mainly Nav1.6 (*SCN8A*, `hgnc:10596` ✔) and Nav1.1, in cerebellar Purkinje and granule neurons.
   - Co‑IP evidence: FGF14 "is a component of the NaV1.6 macromolecular complex in mouse cerebellum" (PMID:25269146) [cached].
   - Branch (in vitro, overexpression only): mutant F145S "does not interact directly with Na(v) channel alpha subunits… [and] disrupts the interaction between wild-type FGF14 and Na(v) alpha subunits" — a dominant‑negative mechanism (PMID:17978045) [EPMC]. In vivo data now favour plain haploinsufficiency (step 1).
3. **Loss of FGF14 regulation** leads to a **hyperpolarizing shift in the voltage dependence of steady‑state (closed‑state) Nav inactivation**, so fewer channels are available at rest. Two further effects contribute:
   - faster inactivation and loss of resurgent and late current (PMID:25269146)
   - reduced Nav1.6 protein in Purkinje cells in the null mouse (PMID:18930825)

   Bosch 2015 (PMID:25926453) [cached]: "the loss of iFGF14 results in a marked hyperpolarizing shift in the voltage dependence of steady-state inactivation of the Nav currents in adult Purkinje neurons."

   Yan 2014 (PMID:25269146) [cached]: "FGF14 knockdown biased NaV channels towards the inactivated state by decreasing channel availability, diminishing the 'late' NaV current, and accelerating channel inactivation rate, thereby reducing resurgent current and repetitive spiking."
4. **Reduced Nav availability** leads to **failure of spontaneous, high‑frequency tonic firing in Purkinje neurons.** Null cells fall silent; heterozygous and knock‑in cells fire in bursts.
   - PMID:41558966 [cached]: "high-frequency repetitive firing… was replaced by prolonged bursts of action potentials."
   - PMID:18930825 [cached]: "more than 80% of Fgf14(-/-) Purkinje neurons were quiescent and failed to fire repetitively in response to depolarizing current injections."
   - This is a cell‑intrinsic defect: parallel‑fibre EPSCs are unchanged (PMID:18930825).
   - Parallel branch: granule cells also lose repetitive firing, shown in *Fhf1/Fhf4* double‑null mice (PMID:17678857).
5. **Disrupted Purkinje output from the cerebellar cortex** leads to **ataxia, tremor and abnormal eye movements.**
   - The adult requirement is shown by shRNA knockdown in adult Purkinje cells, which "impairs motor coordination and balance".
   - Re‑expressing iFGF14 "rescues spontaneous firing and improves motor performance" (PMID:25926453) [cached].
   - This means the deficit is physiological rather than purely developmental, which matters for treatment.
6. **State‑dependent worsening (inferred).** Because Nav availability is already reduced, perturbations such as fever, stress or fatigue lead to **episodic ataxia** attacks. This is supported clinically by fever triggering and by acetazolamide and 4‑AP responses, "supporting the hypothesis of a sodium channelopathy" (PMID:30607796) [cached]. It has not been tested mechanistically.
7. **Extracerebellar branches.**
   - Basal ganglia: dyskinesia, PNKD and parkinsonism. Fgf14‑null mice have "ataxia and a paroxysmal hyperkinetic movement disorder" and "reduced responses to dopamine agonists" (PMID:12123606) [EPMC]. Dutch‑family functional imaging also suggested basal ganglia involvement.
   - Hippocampus and prefrontal cortex lead to cognitive and psychiatric features:
     - Null mice show impaired spatial learning and theta‑burst LTP (PMID:17236779).
     - Null mice have reduced VGAT in the medial prefrontal cortex, and patients show prefrontal hypometabolism on FDG‑PET (PMID:32112487).
8. **Late, mild neurodegeneration.** Moderate cerebellar atrophy appears in older patients only. Whether it is secondary to chronic dysfunction is unknown; there is no SCA27A neuropathology. This should be framed as dysfunction‑predominant (Purkinje cell dysfunction > Purkinje cell loss).

### Ontology suggestions

**Cell types:**
- CL:0000121 Purkinje cell ✔
- CL:0001031 cerebellar granule cell ✔
- CL:0000540 neuron ✔ (hippocampal and cortical pyramidal neurons: search CL)

**GO:**
- GO:0017080 sodium channel regulator activity ✔ (FGF14 molecular function)
- GO:0035725 sodium ion transmembrane transport ✔
- GO:0019228 neuronal action potential ✔ (`modifier: DECREASED`)
- GO:0060291 long‑term synaptic potentiation ✔
- GO:0007611 learning or memory ✔

**Cellular components:**
- GO:0001518 voltage‑gated sodium channel complex ✔
- GO:0043194 axon initial segment ✔

**Pathway framing.** This is a channelopathy rather than a signalling cascade. iFGF14 does not activate FGF receptors. Its phosphorylation by GSK3 regulates the FGF14–Nav complex (PMID:23640885); that is relevant to pharmacology but has not been tied to the disease.

**Omics.** There are no single‑cell, transcriptomic or proteomic disease datasets. The only proteomic data are from *Fgf14*−/− mouse brain (PMID:30678040, sex‑specific). Patient iPSC lines now exist for future work (PMID:42372627). `just discover-datasets` could check GEO.

**Module conformance.** Look for an existing channelopathy or Purkinje‑firing module with `just list-modules channel` and `just list-modules purkinje`. `cardiac_ion_channel_repolarization` is out of scope.

---

## 7. Anatomical structures

- **Primary:**
  - cerebellum UBERON:0002037 ✔
  - cerebellar cortex UBERON:0002129 ✔ (Purkinje and granule layers)
- **Secondary:**
  - collection of basal ganglia UBERON:0010011 ✔ and striatum UBERON:0002435 ✔ (dyskinesia, reduced dopamine response)
  - prefrontal cortex UBERON:0000451 ✔ (PET hypometabolism)
  - hippocampal formation UBERON:0002421 ✔ (mouse learning and LTP)
  - the oculomotor and vestibulocerebellar system (nystagmus)
  - mild peripheral sensory nerve involvement in a minority
- **Subcellular:** axon initial segment (GO:0043194 ✔) and the Nav channel complex (GO:0001518 ✔). Mouse FGF14 is axonally transported (PMID:12123606).
- **Laterality:** bilateral and symmetric. The NYS4 nystagmus is multidirectional.

---

## 8. Temporal development

- **Onset:**
  - congenital or infantile: nystagmus, hypotonia, motor delay (NYS4, deletion families, Paucar 2020's "congenital onset")
  - childhood: tremor, mean about 12 years; fever‑triggered EA from about 2 years
  - young adult: ataxia, mean about 24 years
  - late onset is reported: 47 years for p.Lys177\*
  - onset is insidious
- **Course:** very slowly progressive, with episodic exacerbations in some patients. In several children the EA attacks stopped after about 5–6 years of age (Piarroux family A). No staging system exists.
- **Duration:** lifelong.
- **Critical windows:** febrile illness in early childhood (attack risk). Adult re‑expression rescue in mice suggests therapy could work after development, although this is untested in humans.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant. One family shows autosomal recessive inheritance, with mildly affected heterozygous parents (PMID:39704271).
- **Penetrance:** apparently high, but with **marked variable expressivity**:
  - Family members range from isolated childhood tremor to severe ID (PMID:24252256, PMID:19471976).
  - Some carriers never sought medical care.
  - Ovine p.Q16\* carriers show the same variable expressivity (PMID:29253853).
- **Anticipation:** none. This is not a repeat disorder, unlike SCA27B.
- **De novo:** one translocation (PMID:21600715). Germline mosaicism has not been reported.
- **Founder effects:** none known. Families are Dutch, German, French‑Canadian, French, Japanese, Swedish, British, Spanish, US and Turkish.
- **Prevalence:** unknown. Fewer than 100 published families; Orphanet class is probably <1/1,000,000 (fetch ORPHA:98764 to confirm). Use `measure_type: CASES_IN_LITERATURE`.
- **Sex ratio:** no sex bias reported.

---

## 10. Diagnostics

- **Genetic testing is the only confirmatory test.**
  - Exome or genome sequencing, or ataxia and episodic‑ataxia panels: Piarroux used CACNA1A, KCNA1, CACNB4, SLC1A3, FGF14, SLC2A1, ATP1A3 and PRRT2.
  - **CNV analysis is essential:** SNP‑array or chromosomal microarray, or exome/genome CNV calling. Karyotype is needed for translocations.
  - Ceroni 2023 recommends screening *FGF14* "in apparently isolated early onset nystagmus."
  - **The intronic GAA repeat must be tested separately** (long‑read or RP‑PCR) to distinguish SCA27B; standard short‑read genome sequencing can miss it.
- **Imaging:** MRI is often normal or shows mild late cerebellar atrophy. FDG‑PET can show widespread hypometabolism, particularly prefrontal (PMID:32112487).
- **Electrophysiology:** nerve conduction may show mild sensory axonal neuropathy. Formal oculomotor recording (saccadic dysmetria, gaze‑evoked and rebound nystagmus) is useful.
- **No biomarkers or laboratory tests.**
- **Differential diagnosis:**
  - episodic ataxias EA1 (*KCNA1*) and EA2 (*CACNA1A*)
  - SCA6
  - SCA27B
  - essential tremor (when tremor dominates)
  - PNKD (*PNKD/MR‑1*)
  - congenital idiopathic or *FRMD7* nystagmus
  - an autoimmune mimic has been reported (Hoshina 2023, PMID:37460234, title only)
- **Screening:** cascade testing of relatives. There is no newborn or population screening.

---

## 11. Outcome and prognosis

- **Survival:** no data. Life expectancy is presumed normal; no deaths are attributed to the disease.
- **Function:**
  - Most patients remain ambulant. The Japanese patient walked without a cane at 63.
  - Disability comes mainly from tremor, learning and intellectual impairment, psychiatric illness, and transient loss of walking during attacks.
- **Prognostic factors:**
  - Episodic attacks may wane after early childhood.
  - Large deletions or translocations can be associated with more severe neurodevelopmental phenotypes, but this rests on a single case.
  - There are no prognostic biomarkers.

---

## 12. Treatment

All treatment is symptomatic and supported only by case reports or small series. There are no trials (NCT/ICTRP searches would be expected to return nothing; not run).

| Treatment | Evidence | Suggested binding |
|---|---|---|
| **Acetazolamide** | about two‑thirds reduction in attack frequency (PMID:30607796) [cached]: "Our patient responded well to acetazolamide (reduction in the frequency of attacks by about two thirds), supporting the hypothesis of a sodium channelopathy." | NCIT:C15986 Pharmacotherapy ✔ + CHEBI:27690 acetazolamide ✔; `SMALL_MOLECULE` |
| **4‑Aminopyridine (fampridine)** | "balance improvement with 4-AP" in two p.Val119del patients (PMID:40156335) [EPMC]. *Note:* the large 4‑AP literature is in SCA27B and must not be cited here. | CHEBI:34385 4‑aminopyridine ✔ |
| **STN deep brain stimulation** for disabling tremor | "Two patients showed significant tremor reduction following STN-DBS" (PMID:40156335) | NCIT surgical/neurostimulation term needed (look up "Deep Brain Stimulation"); `SURGERY` or `DEVICE` |
| Levodopa, amantadine for parkinsonism | improvement in one case (PMID:29416937) | CHEBI:2618 amantadine ✔; levodopa CHEBI needs lookup |
| Antiseizure drugs for paroxysmal dyskinesia | "drug-responsive" PNKD in the biallelic case; the agent is not named in the abstract (PMID:39704271) | omit the agent until the full text is read |
| Fever control during intercurrent illness; physiotherapy, speech, educational and psychiatric support | management suggestions (PMID:41099962, PMID:41895131) | NCIT:C15302 Physical Therapy ✔; NCIT:C15315 Rehabilitation ✔ |
| Genetic counselling | 50% recurrence risk (AD) | NCIT:C15240 ✔ |

**Experimental and preclinical approaches:**
- Gene re‑expression rescues adult *Fgf14*−/− mice (PMID:25926453).
- FGF14/Nav1.6 interface peptidomimetics and small molecules exist as research probes (PMID:34948337, PMID:29359916), but none have been tested in disease.

**Pharmacogenomics:** none.

---

## 13. Prevention

- **Primary prevention:** not possible beyond reproductive options. Prenatal or preimplantation testing is available for a known familial variant.
- **Secondary prevention:** cascade testing, and testing infants who present with nystagmus or fever‑triggered ataxia.
- **Tertiary prevention:** prompt treatment of fever, avoiding triggers, acetazolamide prophylaxis for frequent attacks, and early educational support.
- **Genetic counselling:** emphasize variable expressivity; mildly affected parents are common.

---

## 14. Other species and natural disease

**Sheep, *Ovis aries* (NCBITaxon:9940).** Familial episodic ataxia of lambs is associated with FGF14 c.46C>T, p.Q16\*. It is autosomal dominant with variable expressivity, and a more severely affected homozygote was observed (PMID:29253853) [EPMC]:
> "Familial episodic ataxia of lambs is a congenital transient autosomal dominant disorder of newborn lambs, with varying expressivity."

Signs resolve as the lambs mature. This parallels the waning of childhood EA in humans, and the authors note that the "mechanism behind the apparent recovery of lambs" is unknown. The causal link is described as "potentially associated", so it should be graded as such.

Other notes:
- Ask OMIA for any further records.
- *FGF14* is conserved across vertebrates; mouse *Fgf14* is MGI:109189 (look up).
- No zoonotic relevance.

---

## 15. Model organisms

| Model | Key phenotype | Fidelity / limitation | PMID |
|---|---|---|---|
| *Fgf14*−/− (N‑βGal) mouse | ataxia, paroxysmal hyperkinetic dyskinesia, reduced dopamine‑agonist response; silent Purkinje cells; reduced Nav1.6; impaired spatial learning and LTP; reduced mPFC VGAT; resilience to depression‑like behaviour (female) | homozygous null, whereas the human disease is heterozygous; anatomically normal | 12123606, 18930825, 17236779, 32112487, 40204701 |
| *Fgf14*+/− mouse | Purkinje burst firing; reduced protein; hyperpolarized Nav inactivation | genotype‑faithful; behaviour not reported in the abstract | 41558966 |
| **Fgf14^F145S/+ knock‑in** (the first patient allele) | Purkinje tonic firing replaced by bursts; reduced iFGF14; reduced Nav availability; phenocopies +/− (haploinsufficiency) | best genotype fidelity; behavioural ataxia not stated in the abstract | 41558966 |
| Adult Purkinje‑specific shRNA knockdown / AAV re‑expression | motor incoordination; rescued by re‑expression | establishes an adult requirement | 25926453 |
| Cultured Purkinje neurons with FGF14b knockdown | loss of resurgent and late Na current | in vitro, neonatal | 25269146 |
| *Fhf1*/*Fhf4* (*Fgf12*/*Fgf14*) double null | severe ataxia; granule‑cell Nav inactivation defects | digenic; overstates the human phenotype | 17678857 |
| Hippocampal neurons / HEK cells overexpressing F145S | dominant‑negative Nav disruption | overexpression artefact; not supported in vivo | 17978045 |
| Sheep FGF14 p.Q16\* (natural) | episodic neonatal ataxia | naturally occurring, but causality "potentially associated" | 29253853 |
| Patient iPSC lines (2 SCA27A donors) | resource for neuronal differentiation | no phenotype data yet | 42372627 |

For the `animal_models`/`experimental_models` blocks:
- The **knock‑in** links `PARTIALLY_RECAPITULATES` to the Purkinje‑firing node with `model_scale: CELLULAR`.
- The **null mouse** should note the `SPECIES_MISMATCH` and genotype‑dose caveat.

Resources: MGI, IMSR, MMRRC.

---

## Curation notes for the YAML draft

- The draft binds `preferred_term: Cerebellar ataxia` to HP:0001251, whose canonical label is **"Ataxia"** ✔. The label matches, but HPO has a narrower *Cerebellar ataxia* term. Look that term up rather than assuming its ID; it is not in the local cache.
- **Do not reuse SCA27B evidence.** Many cached FGF14 files are about SCA27B: PMID:36516086, 37165652, 38507876, 38271551, 39227614, 40379261, 38279833 and others.
- Fetch before use:
  - PMID:12489043, 15470364, 12123606, 17978045, 17236779, 19471976, 21600715, 29416937, 32112487, 36207621, 39704271, 40156335, 41099962, 29253853, 17678857 (abstracts read via Europe PMC)
  - ORPHA:98764
- The cached abstracts for PMID:28192817 (Amado 2017) and PMID:15365159 (Stevanin 2004) are empty, so they cannot support snippets. The abstract for PMID:41895131 (Regnier 2026, childhood SCA27A) was not returned and needs a full‑text look.
- `genetic_context.functional_impact_category: LOSS_OF_FUNCTION` is well supported. Record the F145S dominant‑negative result (PMID:17978045) as a `REFUTE`/`INDIRECT` or discussion item against the in‑vivo haploinsufficiency evidence (PMID:41558966), not as a co‑equal mechanism.

---

### Sources
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search) — abstracts for PMIDs 12489043, 15470364, 29416937, 29253853, 12123606, 17978045, 17236779, 19471976, 21600715, 17678857, 36207621, 32112487, 39704271, 40156335, 41099962, 40204701, 42372627
- [NCBI E‑utilities esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi) — literature census
- [OMIM #193003 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/193003) — synonyms, NYS4, ORPHA:98764 link
- [MalaCards SCA27A](https://www.malacards.org/card/spinocerebellar_ataxia_27a)
- Local `references_cache/` abstracts: PMID 16211615, 18930825, 24252256, 25269146, 25566820, 25926453, 30017992, 30607796, 32162847, 38058854, 41558966, 20723845

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 35 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.

57 of 59 terms resolved to a current term; the rest could not be looked up either way.