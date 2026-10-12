---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T14:29:08.120552'
end_time: '2026-10-08T14:33:54.493993'
duration_seconds: 286.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cardiomyopathy Dilated 2C
  mondo_id: MONDO:0032592
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 29
  total_cost_usd: 2.7257189
  session_id: ca79e023-665c-4830-ac73-a7d47fdbac8e
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 4
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
citation_count: 8
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 12
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:40745475
  relevance_assessed: 7
  on_topic: 4
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 48
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 5
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiomyopathy Dilated 2C
- **MONDO ID:** MONDO:0032592 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiomyopathy Dilated 2C** covering all of the
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

Let me fetch the primary papers' abstracts from PubMed.

I'm reading the cached full text of the 2018 index paper (Iuso et al.) for clinical and functional detail. Next I'll fetch the 2025 pantethine study and the 2022 iPSC paper.

I have the clinical case series from the 2025 paper. Now I'm reading its iPSC-cardiomyocyte and pantethine results, then I'll write the report.

I've finished reading the primary literature and checking ontology terms against the repo caches. Writing the report now.

# Cardiomyopathy, Dilated, 2C (CMD2C): PPCS deficiency disorder

**Scope and sourcing.** There are only three disease-specific primary papers and one cell-line report. Their abstracts and full texts were cached with `just fetch-reference`:

| PMID | Citation | Cache content |
|---|---|---|
| **29754768** | Iuso A, …, Sibon OCM, Anikster Y. *Mutations in PPCS, Encoding Phosphopantothenoylcysteine Synthetase, Cause Autosomal-Recessive Dilated Cardiomyopathy.* Am J Hum Genet 2018;102:1018–1030 (published 10 May 2018). doi:10.1016/j.ajhg.2018.03.022 | full text (PMC) |
| **35616428** | Lok A, …, Iuso A, Jungbluth H, Milan A, Singh RR. *Novel PPCS mutations with prominent neuromuscular features.* Am J Med Genet A 2022. doi:10.1002/ajmg.a.62848 | abstract only |
| **35397396** | Iuso A, Zhang F, …, Moretti A. *Generation of two human iPSC lines, HMGUi003-A and MRIi028-A, carrying pathogenic biallelic variants in the PPCS gene.* Stem Cell Res 2022;61:102773 | abstract only |
| **40745475** | Zhang F, Dorn T, Gnutti B, et al. *Pantethine ameliorates dilated cardiomyopathy features in PPCS deficiency disorder in patients and cell line models.* Commun Med (Lond) 2025;5:323. PMC12313872 | full text (PDF) |

All quotes below come from these cached files. Any ontology ID marked ✔ was found in this repo's `cache/*/terms.csv` with the label shown. Any ID marked ⚠ was not found in the cache and must be looked up before you bind it.

---

## 1. Disease information

**Overview.** CMD2C is an ultra-rare autosomal recessive cardiomyopathy. It is caused by biallelic hypomorphic variants in *PPCS*, which encodes the second enzyme of de novo coenzyme A (CoA) biosynthesis from vitamin B5. The 2025 paper names the condition **"PPCS deficiency disorder (PPCS DD)"** and defines it as follows:

> "PPCS deficiency disorder (PPCS DD) is an ultra-rare, autosomal recessive form of dilated cardiomyopathy (DCM) caused by pathogenic variants in PPCS, which encodes the enzyme catalyzing the second step in the coenzyme A (CoA) biosynthesis pathway." (PMID:40745475)

The 2018 index paper describes it as cardiac rather than neurodegenerative, which sets it apart from the related CoA-pathway disorders PKAN (*PANK2*) and COPAN (*COASY*):

> "In contrast to the neurodegenerative NBIA-related phenotypes associated with defects in PANK2 and COASY, PPCS-deficient individuals present with a clear dilated cardiomyopathy with a variable degree of severity and no neurodegeneration." (PMID:29754768)

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0032592 "cardiomyopathy, dilated, 2c" ✔ (in `cache/mondo/terms.csv`) |
| OMIM phenotype | 618189 (Dilated cardiomyopathy 2C, AR). Cited by PanelApp Australia. |
| OMIM gene | *PPCS* 609853. Cited in PMID:35616428 ("PPCS [MIM: 609853]"). |
| HGNC | hgnc:25686 PPCS, "phosphopantothenoylcysteine synthetase" (1p34.2; Entrez 79717; ENSG00000127125; UniProt Q9HAB8; MANE NM_024664.4). From `kb/genes/ingest/hgnc.tsv`. |
| Orphanet | No ORPHA leaf entry for PPCS was found in `references_cache/ORPHA_*.md`. It is probably covered only by the generic familial isolated DCM concept (unverified). |
| ICD-10 / ICD-11 | No specific code. It falls under I42.0 (dilated cardiomyopathy) / ICD-11 BC43.0 (generic codes). |
| MeSH | Cardiomyopathy, Dilated (D002311) as the generic heading. No supplementary concept was verified. |

**Synonyms:** PPCS deficiency disorder (PPCS DD); PPCS-related dilated cardiomyopathy; CMD2C; dilated cardiomyopathy 2C; phosphopantothenoylcysteine synthetase deficiency.

**Data basis.** All knowledge comes from aggregated case reports and series of individual patients. By 2025 the total was **12 patients from 7 families** (PMID:40745475, Table 1). There is no registry or EHR-scale data.

---

## 2. Etiology

**Primary cause.** Biallelic germline *PPCS* variants. The variants are missense or in-frame changes, plus one intronic splice-region variant, that reduce PPCS protein stability and lower cellular CoA.

> "Identified variants lead to reduced PPCS protein stability and decreased cellular CoA levels." (PMID:40745475)

**No biallelic loss-of-function genotype has been seen.** This suggests that complete PPCS loss is lethal:

> "none of the new patients, similarly to previously reported cases, harbored biallelic loss of function variants, suggesting that this combination might be incompatible with life." (PMID:40745475)

**Genetic risk factors.** The only established ones are the causal *PPCS* alleles listed in §4. No GWAS, susceptibility locus, or modifier gene has been established.
- In family F5, the proband also carried *KCNH2* p.His1153Tyr (a VUS associated with LQT2). It did not segregate with QT prolongation, so it is not an established modifier.

**Environmental and precipitating factors.** These are hypotheses, not established causes.
- **Intercurrent infection or catabolic stress** repeatedly precipitated decompensation: viral URTI (F1:II, three episodes), CMV infection (F2:II.1), and rhabdomyolysis during illness or poor feeding (F1:II, F4:II).
- The authors suggest that the **gut microbiome and dietary intake of CoA precursors** (pantetheine) may modify expressivity. They note that some patients worsened after antibiotic-treated infections. This rests on fruit-fly data plus anecdote and is explicitly speculative:

> "part of the variable expressivity of PPCS DD among patients and siblings sharing the same pathogenic variants could be explained by differences in microbiome profile and dietary intake of CoA precursors" (PMID:40745475)

- Serum pantothenate (vitamin B5) was normal in two affected siblings (74.95 and 73.84 µg/L; reference 37–147). Dietary B5 deficiency is therefore not the mechanism (PMID:29754768).

**Protective factors.**
- No genetic protective factor is known.
- **Exogenous pantethine** is the only candidate protective or therapeutic exposure. It bypasses the PPCS step (see §6 and §12).

**Gene–environment interaction.** The proposed interaction is CoA demand (fasting, infection, fatty-acid-dependent metabolism) acting on a reduced CoA biosynthetic capacity. This is inferred, not formally tested.

---

## 3. Phenotypes

The frequencies below are counted from the 12 patients in PMID:40745475 Table 1 (Iuso 2018 + Lok 2022 + 6 new cases). They are small-number estimates.

| Phenotype | HPO (✔ = in cache) | Frequency / notes | Onset & course |
|---|---|---|---|
| Dilated cardiomyopathy | HP:0001644 Dilated cardiomyopathy ✔ | 10/12 recorded as DCM or severe DCM. The other two are LVNC (F3:III.2) and septal hypertrophy (F4:II). The 2025 discussion calls DCM "a constant finding". | Antenatal to 21 y. Often severe, fatal in infancy; variable within sibships |
| Left ventricular noncompaction | HP:0011664 Left ventricular noncompaction cardiomyopathy ✔ | 1/12 (F3:III.2: "noncompacted to compacted ratio of 2.7:1"; "meets criteria for LV non-compaction cardiomyopathy") | Adolescent/adult |
| Septal hypertrophy | HP:0001670 Asymmetric septal hypertrophy ✔ (verify that "asymmetric" fits) | 1/12 (F4:II, "cardiac muscle septal hypertrophy") | Neonatal |
| Heart failure | HP:0001635 Congestive heart failure ✔ | Most cases. Exertional dyspnea in surviving siblings; ECMO in F1:II (×2) and F3:III.3 | Episodic decompensations triggered by infection |
| Reduced LVEF | HP:0012664 Reduced left ventricular ejection fraction ✔ / HP:0012666 Severely reduced… ✔ | EF 15% (F1:II), 28% (F2:II.1), 34% (F5:IV.1), 36% (F6:IV.1) | Partly reversible in some |
| Ventricular fibrillation / ventricular arrhythmia | HP:0001663 ✔; HP:0004308 Ventricular arrhythmia ✔; HP:0004756 Ventricular tachycardia ✔ | VF arrest in F3:III.3 and F5:IV.1. "Malignant tachyarrhythmias" terminally in F2:II.1 | Adolescent |
| Prolonged QT | HP:0001657 ✔ | F1:II; F5:IV.1 (QT up to 560 and 624 ms; later normalized) | Episodic |
| Sudden cardiac arrest / death | HP:0001645 Sudden cardiac death ✔ | Cardiac arrest in F1:II (9 mo), F4:II (fatal), F3:III.3, F5:IV.1 | — |
| Cardiomegaly | HP:0001640 ✔ | F1:II on chest radiograph | — |
| Pulmonary arterial hypertension | HP:0002092 ✔ | 1 case (Family A index, Iuso 2018) | Neonatal |
| Hypotonia | HP:0001252 ✔ / HP:0001290 Generalized hypotonia ✔ | 3/12 (F1:II; F7:II.2 [Lok]; Family A index "severe hypotonia") | Neonatal/infantile |
| Rhabdomyolysis | HP:0003201 ✔ | 3/12 (F1:II, peak CK 26,000 U/L; F4:II, CK 71,000; Lok case "intermittent rhabdomyolysis") | Infection- or fasting-triggered |
| Elevated CK | HP:0003236 Elevated circulating creatine kinase activity ✔ | 4 of 6 tested elevated | — |
| Necrotizing myopathy / myopathy | HP:0003198 Myopathy ✔ | Lok 2022: "a necrotizing myopathy with intermittent rhabdomyolysis". F1:II muscle biopsy suggested a neurogenic process | Neonatal |
| Lactic acidosis | HP:0003128 ✔ | 6/9 tested elevated lactate | During decompensation |
| Hypoglycemia | HP:0001943 ✔ | F1:II (1.3 mmol/L at 9 mo) | Infection-triggered |
| Hyperammonemia | HP:0001987 ✔ | F4:II (max 1351 µmol/L) | Infantile |
| Hyperlysinemia | HP:0002161 ✔ | F4:II (lysine 964 µmol/L) | Single case |
| Abnormal acylcarnitines | ⚠ (e.g., "Abnormal circulating carnitine concentration"; look up) | 6/9 tested abnormal. In 2018: low C16/C18 with elevated C0/(C16+C18) ratio. In 2025: VLCADD-like C14:1/C14:2 elevation during illness | Often normal when well |
| Dysmorphic features, cutis laxa | HP:0000973 Cutis laxa ✔ | 1 (Family A index); Lok case "dysmorphic features" | Congenital |
| Exertional dyspnea | HP:0002875 ✔ | Surviving siblings of Family B/F6 | Chronic |
| Brain volume loss (non-specific) | ⚠ | F1:II, possibly secondary to ECMO or cardiac insults. **No brain iron accumulation** in any patient | — |

Key quotes:
- Neuromuscular phenotype (PMID:35616428): "a female infant who presented in the neonatal period with hypotonia, a necrotizing myopathy with intermittent rhabdomyolysis and other extracardiac manifestations before developing a progressive and ultimately fatal dilated cardiomyopathy."
- Severity and mortality (PMID:35616428): "Biallelic pathogenic variants in phosphopantothenoylcysteine synthetase, PPCS, are a rare cause of a severe early-onset dilated cardiomyopathy with high morbidity and mortality."
- Variable expressivity within one sibship (PMID:29754768): "Four out of eight siblings exhibited dilated cardiomyopathy of varying severity, without apparent extracardiac manifestations."

**Onset categories:** HP:0003593 Infantile onset ✔ and HP:0011463 Childhood onset ✔ cover most cases. Juvenile and adult presentations also occur (14–21 y).

**Quality of life.** No formal QoL instrument has been used. Reported disability includes wheelchair-assisted ambulation (F1:II), limited exertional capacity, and transplant morbidity including a below-knee amputation after a TAH complication (F3:III.3).

---

## 4. Genetic and molecular information

**Gene:** *PPCS* (hgnc:25686; OMIM 609853; chr 1p34.2). The canonical isoform is NM_024664 (311 aa). A shorter isoform (NM_001077447, 138 aa) shares the C-terminus. Only the canonical 34-kDa protein was detected in fibroblasts (PMID:29754768). PPCS acts as a homodimer:

> "in physiological conditions PPCS exists mainly as a dimer." (PMID:29754768)

**Reported variants (NM_024664)**

| Variant | Protein | Exon | Zygosity / family | Predicted effect | Phenotype class |
|---|---|---|---|---|---|
| c.698A>T | p.Glu233Val | 3 | Homozygous; Family B/F6 (Arab-Muslim, consanguineous), F3, F5 | Near the ATP-binding phosphate recognition site, close to the dimer interface; FoldX ΔΔG +0.9 kcal/mol | "DCM only", variable expressivity |
| c.538G>C | p.Ala180Pro | 2 | Compound heterozygous with del (Family A, German, non-consanguineous) | Nucleotide-binding cleft; **completely non-functional in yeast** | DCM + extracardiac |
| c.320_334del | p.Pro107_Ala111del | 1 | Compound heterozygous (Family A; Lok case) | Dimerization region; gnomAD 10 heterozygotes / 271,726 alleles (MAF ~0.0001 in 2017) | DCM + extracardiac |
| c.613-3C>G | p.? (splice region) | intron | In trans with c.320_334del (Lok 2022) | Initially VUS; "Functional studies confirmed the likely pathogenicity" | DCM + neuromuscular |
| c.232T>C | p.Tyr78His | 1 | Homozygous (F1) | Disrupts H-bond network near catalytic site; RNA-seq showed reduced PPCS expression | DCM + neuromuscular |
| c.317G>C | p.Arg106Pro | 1 | Homozygous (F2) | Dimerization β-sheet; FoldX ΔΔG +13.0 kcal/mol | DCM + extracardiac |
| c.59C>G | p.Ala20Gly | 1 | Homozygous (F4) | α1/α6 helix packing; ΔΔG ~+1.5 | Septal hypertrophy + multisystem metabolic |

- **Allele frequency:** The two original missense variants were absent from gnomAD (12/2017) (PMID:29754768).
- **Classification:** ClinGen has not curated PPCS (no `CGGV:` record in cache). PanelApp Australia lists PPCS for DCM with biallelic inheritance. Per the repo rule, do not assign a validity tier yourself.
- **Mechanism:** loss of function (hypomorphic) through protein instability. It is not dominant negative. Parents are heterozygous carriers and asymptomatic.
- **Somatic vs germline:** germline only.
- **Genotype–phenotype hypothesis (exploratory, n = 12):**

> "the p.Glu233Val variant leads to an isolated DCM presentation with variable expressivity" … "We hypothesize that the 'DCM only' phenotype arises when variants involve exon 3, while 'DCM plus' occurs when they involve exons 1 and 2" (PMID:40745475)

Exon 1 is proposed as a mutational hotspot.

**Modifier genes, epigenetics, chromosomal abnormalities.**
- No modifier genes are established.
- No epigenetic data exist.
- There are no chromosomal causes. Incidental CNVs and runs of homozygosity were found, e.g. a 1p31.1 duplication in F2, which was considered unrelated.

---

## 5. Environmental information

- No toxin, occupational, or infectious etiology has been reported.
- Infections such as viral URTI and CMV act as **decompensation triggers**, not causes.
- One adult death (F6:IV.1, age 21) was from SARS-CoV-2 complications. Cardiac function in both siblings stayed stable through that infection (PMID:40745475).
- **Lifestyle:** avoiding fasting is plausible given the metabolic crises (hypoglycemia, rhabdomyolysis), but this is not evidence-based.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic *PPCS* variants**, often missense in exon 1 or at the dimer interface or ATP site. These **lead to** reduced PPCS protein stability and abundance, with transcript levels normal in iPSC-derived cells.
   - Demonstrated in fibroblasts (PMID:29754768, 40745475) and in iPSCs, CPCs and cardiomyocytes. iPSC-CMs show "markedly reduced PPCS protein levels … suggesting impaired protein stability" with "no significant differences" in PPCS transcript (PMID:40745475).
   - Some variants also impair dimerization. In blue-native PAGE, no dimer was detectable in the Family A index (PMID:29754768).

2. **Loss of PPCS enzyme activity**, i.e. failure to condense 4'-phosphopantothenate with cysteine. This **results in** reduced de novo CoA biosynthesis.
   - The enzymatic step: "Phosphopantothenoylcysteine synthetase (PPCS) catalyzes the second step of the pathway during which phosphopantothenate reacts with ATP and cysteine to form phosphopantothenoylcysteine." (PMID:29754768)
   - Yeast complementation showed that the variants are deleterious.

3. **Reduced intracellular CoA**, which is rescued by re-expressing wild-type PPCS.
   - "Biochemical analysis revealed a decrease in CoA levels in fibroblasts of all affected individuals." (PMID:29754768)
   - The deficit **grows as cells commit to the cardiac lineage** (PMID:40745475): "The defect became significant and more pronounced during cardiac maturation to CPCs, d22 CMs, and d60 CMs in both lines".
   - Unlike PKAN and COPAN, PPCS deficiency lowers fibroblast CoA measurably.

4. **(Inferred) Limited acyl-CoA formation**, which leads to impaired long-chain fatty-acid activation and mitochondrial β-oxidation. Mature cardiomyocytes depend on fatty acids for energy, so this causes an energy shortfall.
   - Biochemical support: low long-chain acylcarnitines (2018) and a VLCADD-like acylcarnitine pattern during crises (2025).
   - Authors' reasoning (PMID:40745475): "iPSCs rely mainly on glycolysis for energy, while mature cardiac cells preferentially utilize fatty acids, requiring CoA for their activation and utilization. Therefore, a shortage of CoA during cardiac cell maturation could lead to reduced energy supply for cardiac cells and cause cardiac dysfunction"
   - 2018 mechanism (PMID:29754768): "Reduced cytosolic CoA concentration in PPCS-affected individuals may lead to a reduced synthesis of activated long-chain fatty acids … resulting in reduced long-chain acylcarnitine concentrations, similar to individuals with carnitine palmitoyltransferase I (CPT1) deficiency."
   - **This step is inferred.** CoA has not been measured in patient heart tissue, and fluxomics has not been done.

5. **Cardiomyocyte structural and excitation–contraction defects.** In iPSC-CMs these are:
   - sarcomere disorganization;
   - reduced Ca²⁺ transient amplitude;
   - arrhythmic events in 42–54% of cells.

   In 3D engineered heart patches they are:
   - falling contractile force over time;
   - blunted force–frequency relationship;
   - shortened effective refractory period, i.e. a pro-arrhythmic substrate.

   This is demonstrated in vitro (PMID:40745475): "Cardiac cells exhibit impaired contractility and arrhythmias, which are partially rescued by pantethine treatment."

6. **Clinical consequences.** The cellular defects lead to dilated cardiomyopathy with systolic failure, plus ventricular arrhythmia, VF arrest and sudden death. Episodes are often precipitated by infection or catabolism. Mild interstitial fibrosis and myocyte nucleomegaly were seen on endomyocardial biopsy (F1:II), with no myocarditis.

### Branches

- **Branch A, skeletal muscle (exon 1–2 genotypes).** CoA deficit in skeletal muscle is associated with hypotonia, necrotizing myopathy, rhabdomyolysis during catabolic stress, and elevated CK. The mechanism is presumed to be the same energy and fatty-acid-oxidation failure, but this is not demonstrated.
- **Branch B, systemic metabolic crisis.** Hypoglycemia, lactic acidosis, hyperammonemia, and dicarboxylic aciduria during illness are consistent with secondary fatty-acid-oxidation and TCA impairment (inferred).
- **Branch C, alternative or toxic-metabolite hypothesis.** This is untested in humans:

> "We cannot exclude that cardiomyopathy in PPCS-deficient individuals is also due to the generation of toxic metabolites. For instance, L-cysteine normally funneled in the synthesis of phosphopantothenoylcysteine could accumulate" (PMID:29754768)

  Supporting evidence is limited to the report that dPPCS fly mutants are hypersensitive to cysteine.

**Unexplained tissue selectivity.**

> "considering the ubiquitous presence of the enzymatic PPCS activity, it remains unexplained why the brain and in general the other organs are not affected" (PMID:29754768)

The 2025 paper suggests that tissue- or time-specific alternative isoforms may explain this. A transplant recipient (F3:III.3) has had no DCM recurrence at one year, which is consistent with a heart-intrinsic (cell-autonomous) defect.

**Subcellular localization.** PPCS shows nuclear and cytosolic signal in iPSC-derived cells and in GFP-tagged HeLa cells (PMID:40745475).

### Suggested ontology terms

| Type | Term |
|---|---|
| GO BP | GO:0015937 coenzyme A biosynthetic process ✔ (DECREASED) |
| GO BP | GO:0006635 fatty acid beta-oxidation ✔ (DECREASED, inferred) |
| GO BP | GO:0060048 cardiac muscle contraction ✔ |
| GO BP | GO:0086003 cardiac muscle cell contraction ✔ |
| GO BP | GO:0045214 sarcomere organization ✔ |
| GO BP | GO:0010882 regulation of cardiac muscle contraction by calcium ion signaling ✔ |
| GO MF | phosphopantothenate–cysteine ligase activity ⚠. This is likely GO:0004632, but it is not in the cache, so look it up before binding. |
| GO CC | GO:0005829 cytosol ✔; GO:0005634 nucleus ✔ |
| CL | CL:0000746 cardiac muscle cell ✔ (primary); CL:0000057 fibroblast ✔ (diagnostic and model cell). Skeletal muscle fiber ⚠ |
| CHEBI | CHEBI:15346 coenzyme A ✔; CHEBI:16454 pantothenate ✔; pantethine ⚠ (look up); L-cysteine ⚠ |

**Molecular profiling.**
- Clinical RNA-seq of skeletal muscle in F1:II showed "an overall reduction in PPCS expression".
- No GEO, proteomic, metabolomic, single-cell, or CRISPR-screen datasets are specific to this disease.

---

## 7. Anatomical structures affected

- **Primary:** heart (UBERON:0000948 ✔), mainly the left ventricle (UBERON:0002084 heart left ventricle ✔). Biventricular dysfunction occurred in F5 (RVEF 37%).
- **Secondary:**
  - skeletal muscle (UBERON skeletal muscle tissue ⚠), in the exon 1–2 genotypes;
  - liver, through transaminitis and coagulopathy (F4);
  - pulmonary vasculature (PAH, 1 case);
  - possibly the pituitary (suspected dysfunction, 1 case);
  - the brain, with non-specific changes only and no iron accumulation.
- **Cells:** cardiomyocytes and skeletal myocytes. Fibroblasts are used for diagnosis.
- **Subcellular:** cytosol and nucleus (PPCS); mitochondria (downstream β-oxidation and acyl-CoA use).
- **Laterality:** not applicable (global ventricular dysfunction).

---

## 8. Temporal development

- **Onset:** ranges from antenatal and neonatal to 21 years.
  - Severe compound-heterozygous or exon-1 cases present in the neonatal or infantile period.
  - Glu233Val homozygotes span 23 months to 21 years.
- **Pattern:** acute decompensation on top of an insidious chronic course. Episodes are often triggered by infection.
- **Progression:** variable.
  - Rapidly fatal in infancy in several cases: deaths at 3, 4 and 10 months, and at 23 months and 3 years.
  - Others have chronic stable DCM into adulthood.
- **Remission:** some recovery of LV function occurred.
  - F1:II improved spontaneously between episodes.
  - F5:IV.1 had "fully recovered LV function" on pantethine plus standard heart-failure therapy.
- **Critical period:** the authors stress early treatment:

> "complete reversal may require early intervention." (PMID:40745475)

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007 ✔). Carriers are asymptomatic and segregation is complete in Family B/F6.
- **Penetrance:** appears complete for cardiomyopathy in homozygotes, with **variable expressivity** within sibships (mild vs fatal DCM among siblings with the same genotype).
- **Anticipation and mosaicism:** none reported.
- **Consanguinity:** 8 of 12 patients came from consanguineous families (Table 1).
- **Founder effect:** p.Glu233Val recurs in Family B/F6 (Arab-Muslim, Israel), F3 and F5. Haplotype analysis has not been reported, so a founder effect is plausible but unproven.
- **Prevalence:** unknown. There are 12 cases in the literature ("To date, only six patients worldwide have been identified" before the 2025 series). The appropriate dismech record would be `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`.
- **Carrier frequency:** not estimated. The 2018 in-house database of more than 11,000 exomes contained no other rare biallelic PPCS genotypes.
- **Sex ratio:** roughly balanced (both sexes affected).
- **Geography and ancestry:** German, Arab-Muslim (Israel), UK, North American, and other cohorts. The 2025 patients' ancestry is not fully given in the text read.

---

## 10. Diagnostics

**Genetic testing (definitive).**
- Most cases were diagnosed by exome sequencing (singleton, trio, or reanalysis). One sibling was diagnosed by single-gene testing after cascade screening. Trio genome sequencing was used in Lok 2022.
- *PPCS* is on PanelApp Australia's DCM panel. It may be missing from many commercial DCM panels, so **exome or genome reanalysis** was what found it in F1:II, years after a non-diagnostic exome.
- CMA is not diagnostic. Mitochondrial DNA testing is useful to exclude mitochondrial differentials only.

**Functional and biochemical tests (research-level).**
- Fibroblast PPCS immunoblot (reduced or absent 34-kDa band).
- Fibroblast total CoA by fluorimetric kit (reduced; rescued by wild-type PPCS transduction).
- Serum CoA and PPCS ELISA were undetectable in both patients and controls, so **they are not useful** (PMID:29754768).

**Supportive laboratory findings.**
- Acylcarnitine profile: low C16/C18, or VLCADD-like C14:1/C14:2 elevation during crises. It can be normal when the patient is well, and its role as a biomarker is inconsistent.
- CK, lactate, ammonia, glucose; urine organic acids (dicarboxylic aciduria); FGF21 was elevated in one case.

**Cardiac work-up.**
- Echocardiography (LVEDD z-score, EF, FS) and cardiac MRI (volumes, LGE usually absent, LVNC ratio).
- ECG (QT prolongation, T-wave inversion, low voltage) and Holter or implantable loop recorder.
- Endomyocardial biopsy: no myocarditis; nucleomegaly and mild fibrosis; normal mitochondria on EM.

**Differential diagnosis.**
- Other genetic DCMs (TTN, LMNA, sarcomeric).
- Fatty-acid oxidation disorders: VLCADD (the acylcarnitines mimic it), CPT1 deficiency, primary carnitine deficiency.
- Mitochondrial cardiomyopathies; Barth syndrome (males); Pompe disease (a *GAA* VUS was excluded in F2).
- Viral myocarditis (cardiac MRI in F2 initially suggested it).
- LQT syndromes (*KCNH2*).
- Other CoA-pathway disorders, PKAN and COPAN, which are distinguished by NBIA on MRI.

**Screening.** No newborn screening exists. Acylcarnitine abnormalities are not consistent enough for NBS. Cascade testing of siblings is effective: F3:III.2 was diagnosed this way.

---

## 11. Outcome and prognosis

- **Mortality:** 7 of 12 have died.
  - Deaths at 3 mo, 4 mo and 10 mo; at 23 mo and 3 y (DCM); and at 21 y (COVID-19).
  - With one more early death in the series, the counts in Table 1 are hard to align exactly. Take the totals from Table 1 when curating.
  - Causes were multi-organ failure, refractory arrhythmia, and cardiac arrest.
- **Survivors:** ages 11–21 y, with variable function. Outcomes include one heart transplant with no graft dysfunction at one year, one ICD carrier, and one person in a wheelchair.
- **Prognostic factors (hypothesized):**
  - Genotype: exon 1–2 and compound-heterozygous genotypes are more severe; Glu233Val is "DCM only".
  - Age at onset: neonatal or infantile onset is worse.
  - Timing of pantethine start.
- No survival statistics or QoL measures exist.

---

## 12. Treatment

**Targeted metabolic bypass: pantethine** (compassionate use). Rationale (PMID:29754768):

> "CoA biosynthesis can occur with pantethine as a source independent from PPCS, suggesting pantethine as targeted treatment for the affected individuals still alive."

Pantethine is cleaved to pantetheine, which PANK phosphorylates to 4'-phosphopantetheine, so the PPCS and PPCDC steps are skipped.

**Dosing.**
- Family B: 6–8 mg/kg/day, titrated to 20–24 mg/kg/day.
- F1:II: 450 mg/day (17 mg/kg/day), increased to 900 mg/day.
- F5:IV.1: 600 mg/day (~10 mg/kg/day).
- Family F6 long-term: ~15 mg/kg/day.

**Clinical outcomes in the 4 treated patients.**
- Family B: "mild improvement in exertional dyspnea and an increase of ejection fraction … from 36% … to 48%" in IV.1; IV.4 stable at EF 45%. The 2018 authors were cautious: "Our results thus far had not shown significant clinical improvement."
- F1:II: no further rhabdomyolysis; CK and BNP normalized; LV size normal with low-normal function.
- F5:IV.1: fully recovered LV function, alongside ICD, beta-blocker and ACE inhibitor.
- Summary (PMID:40745475): "Clinically, patients receiving pantethine show sustained improvement over time."
- **Evidence level:** uncontrolled case reports confounded by standard heart-failure therapy.

**In vitro evidence.**
- Pantethine at 50–500 µM raised CoA in fibroblasts, iPSCs, CPCs and CMs, without increasing PPCS protein.
- It partially rescued sarcomere organization, Ca²⁺ transients and ERP.
- It reduced arrhythmic events in CMs from 42% to 26% and from 54% to 24%.
- **4'-phosphopantetheine** raised fibroblast CoA less effectively than pantethine.
- One unexplained observation: F1:II began excreting 3-methylcrotonylglycine after starting pantethine. He also carries a homozygous *MCCC1* VUS.

**Standard cardiac and supportive care.**
- Guideline-directed heart-failure therapy: beta-blockers (metoprolol), ACE inhibitors, milrinone and other inotropes, and carnitine supplementation (empirical, in F2).
- ICD for secondary prevention after VF.
- ECMO for acute decompensation.
- Total artificial heart as a bridge, then **heart transplantation**, which was successful in F3:III.3.
- For metabolic crises: dietary fatty-acid-oxidation management (initially treated as VLCADD), carglumic acid, and CVVH for hyperammonemia.
- Rehabilitation and physical therapy for neuromuscular disability.

**Experimental therapies.** No registered trials were found for PPCS deficiency. 4'-phosphopantetheine has been tested in PKAN trials, but not in PPCS DD. No gene therapy or RNA therapy exists.

**Pharmacogenomics:** none.

**Suggested NCIT terms** (all are in the CLAUDE.md common list; still confirm with `validate-terms`):

| Intervention | `treatment_term` | Other slots |
|---|---|---|
| Pantethine | Pharmacotherapy (NCIT:C15986) | `therapeutic_agent` CHEBI pantethine ⚠ (look up); `therapeutic_modality: SMALL_MOLECULE` |
| Heart transplant | Organ Transplantation (NCIT:C15289) | `SURGERY` |
| ICD | Surgical Procedure (NCIT:C15329) as the action, with device qualifier | `DEVICE`, per the cochlear-implant pattern |
| Genetic counseling | NCIT:C15240 | — |
| Supportive care | NCIT:C15747 | — |
| Beta-blocker / ACE inhibitor | Pharmacotherapy | CHEBI metoprolol ⚠ |

---

## 13. Prevention

- **Primary:** none, beyond reproductive options.
- **Secondary:**
  - Cascade genetic testing of siblings, with echocardiography, ECG and loop recorder for those found affected (F3:III.2 was found pre-symptomatically).
  - Early pantethine start is proposed for genotype-positive individuals.
- **Tertiary:**
  - Avoid prolonged fasting.
  - Aggressive management of intercurrent infections.
  - Arrhythmia surveillance and ICD where indicated.
  - Vaccination (one COVID-19 death).
- **Genetic counseling:** AR with 25% recurrence risk for carrier couples; prenatal or preimplantation diagnosis is possible once familial variants are known. Consanguinity counseling is relevant.

---

## 14. Other species and natural disease

- No naturally occurring animal disease was found. A search of OMIA was not done, so treat this as unverified.
- **Orthologs:**
  - *S. cerevisiae* CAB2/YIL083C (essential)
  - *D. melanogaster* CG5629 (dPPCS)
  - *E. coli* CoaBC (bifunctional PPCS/PPCDC)
  - Zebrafish ortholog ZDB-GENE-060512-104 (from the ZFIN search result)
- Pathway conservation:

> "The pathway of CoA de novo biosynthesis from vitamin B5 is conserved in eukaryotes and prokaryotes and consists of five consecutive enzymatic steps." (PMID:29754768)

---

## 15. Model organisms and systems

| Model | Description | Recapitulation | Limitations | Evidence |
|---|---|---|---|---|
| *S. cerevisiae* cab2Δ plasmid-shuffle complementation | Human PPCS wild-type vs variants | Original variants fail to complement; Ala180Pro is null | Qualitative; Tyr78His and Arg106Pro showed no or moderate defect in yeast (an overexpression artefact) | PMID:29754768, 40745475 (IN_VITRO / MODEL_ORGANISM) |
| *Drosophila* dPPCS¹ (P-element in 5′UTR, hypomorph) | Pre-pupal heart imaging | ↑ heart rate, ↑ arrhythmia index, ↓ systolic length, altered wall shortening; reduced viability (9–22% vs expected 33%) **rescued by 8 mM pantethine** but not by vitamin B5 | Open tubular heart; the hypomorph is not a patient allele | PMID:29754768 (MODEL_ORGANISM) |
| Patient fibroblasts | 95595 (Ala180Pro/del), 103596 (Glu233Val hom), 128343, 128344, 146603 | ↓ PPCS protein, ↓ CoA; rescued by wild-type PPCS and partly by pantethine | Non-cardiac cell | IN_VITRO |
| Patient iPSC lines | HMGUi003-A (female, compound heterozygous); MRIi028-A (male, Glu233Val hom; RRID CVCL_A0TH) | Platform for cardiac differentiation | — | PMID:35397396 |
| iPSC-CMs (2D, d22/d60) and 3D engineered heart patches on decellularized porcine ventricular ECM | — | Sarcomere disorganization, ↓ Ca²⁺ transients, arrhythmias, ↓ force, ↓ FFR, ↓ ERP; partial pantethine rescue | Immature cardiomyocytes; no systemic metabolism; n = 2 patient lines | PMID:40745475 |
| Mouse | — | **No Ppcs mouse model has been reported** in the literature reviewed | — | — |

For dismech `modeled_mechanisms`:
- The **Drosophila model** could link to the cardiac contractile/arrhythmia node with `PARTIALLY_RECAPITULATES` and `SPECIES_MISMATCH` + `BOUNDARY_OMISSION` divergences.
- The **iPSC-CM patch** could link to the CoA deficiency node (`RECAPITULATES`, `model_scale: CELLULAR`) and to the DCM node. The DCM link is an upward extrapolation, so it needs `limitations`.

---

## Gaps and open questions

1. CoA has never been measured in human or animal heart tissue. The fatty-acid-oxidation energy-deficit step is inferred.
2. It is unexplained why the heart is affected and the brain is not, given ubiquitous PPCS expression. The isoform hypothesis is unproven.
3. The genotype–phenotype rule (exon 3 vs exons 1–2) rests on n = 12.
4. Pantethine efficacy is uncontrolled, and the optimal dose and timing are unknown. 4'-phosphopantetheine has not been tested clinically.
5. The microbiome and dietary pantetheine contribution to expressivity has been shown only in flies.
6. There is no mammalian genetic model.
7. No ClinGen validity curation exists, and no Orphanet entry was verified.

**Curation notes for the open `Cardiomyopathy_Dilated_2C.yaml` draft:**
- The draft currently has one stub node. It should be expanded along the six-step chain above.
- Four PMIDs are now cached in `references_cache/`: 29754768, 35616428, 35397396, 40745475. 35616428 and 35397396 are abstract-only, so snippets from them must come from the abstract.
- Before binding, look up the ⚠ terms: the PPCS molecular-function GO term, pantethine CHEBI, and skeletal muscle UBERON.

### Sources
- [PMC12313872 – Zhang et al. 2025, Commun Med](https://pmc.ncbi.nlm.nih.gov/articles/PMC12313872/) (PMID:40745475)
- [Springer Nature Communities – "Pantethine for a Rare Cardiomyopathy"](https://communities.springernature.com/posts/pantethine-for-a-rare-cardiomyopathy-a-step-toward-metabolic-therapy)
- [University of Tübingen repository – Iuso et al. 2018](https://publikationen.uni-tuebingen.de/xmlui/handle/10900/92871?show=full) (PMID:29754768)
- [PanelApp Australia – PPCS, Dilated Cardiomyopathy panel](https://panelapp-aus.org/panels/95/gene/PPCS)
- [Cellosaurus MRIi028-A (CVCL_A0TH)](https://cellosaurus.org/CVCL_A0TH) and [hPSCreg publication record](https://hpscreg.eu/browse/publication/2835) (PMID:35397396)
- [ZFIN ZDB-GENE-060512-104](https://www.zfin.org/ZDB-GENE-060512-104)
- [ERIBA – Sibon 2025 Commun Med](https://eriba.umcg.nl/publications/sibon-2025-07-31-commun-med/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:40745475`: "none of the new patients, similarly to previously reported cases, harbored biallelic loss of function variants, suggesting that this combination might be incompatible with life."
  - closest text in source: "Genetically, none of the new patients, similarly to previously reported cases, harbored biallelic loss of fun ction variants, suggesting that this combination might be incompatible with life"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.