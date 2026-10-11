---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-01T10:48:06.024278'
end_time: '2026-10-01T10:55:01.646058'
duration_seconds: 415.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neuronopathy, Distal Hereditary Motor, Autosomal Recessive 5
  mondo_id: MONDO:0013947
  category: Genetic
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
  num_turns: 32
  total_cost_usd: 2.6721118
  session_id: 3105c332-5637-47b0-a910-ca387f41e6a3
  stop_reason: end_turn
  permission_denials: 4
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
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 20
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 6
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neuronopathy, Distal Hereditary Motor, Autosomal Recessive 5
- **MONDO ID:** MONDO:0013947 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Neuronopathy, Distal Hereditary Motor, Autosomal Recessive 5** covering all of the
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

Checking the cached reference titles for the DNAJB2 papers already in the repo.

The CMT2T entry turned out to be MME, not DNAJB2, so I'm now searching the literature for the DNAJB2 primary papers.

Fetching the primary DNAJB2 abstracts from PubMed so the report can quote them exactly.

The fetch tool paraphrases abstracts, so I'll cache them with the repo's own reference fetcher to get verbatim text.

Progress: I've confirmed the core literature (Blumen 2012, Saveri 2022, Sarparanta 2020 review). Next I'm resolving PMIDs for the follow-up case series (Gess, Frasquet, Sanchez).

Almost done gathering; checking variant details in the 2026 German cohort and the identifiers in the local MONDO cache before writing.

# Research report: Neuronopathy, distal hereditary motor, autosomal recessive 5 (DNAJB2-related dHMN / AR-CMT2)

**MONDO:** MONDO:0013947 · **Category:** Genetic (Mendelian, autosomal recessive) · **Report date:** 2026-10-01

## Before you use this report

- **Snippets.** Every quoted snippet below was copied from a `references_cache/PMID_*.md` file in this worktree, not from memory or a summarizer. To cache them I ran `just fetch-reference` for 22 PMIDs. That added uncommitted files under `references_cache/`. Commit the ones the entry ends up citing; the rest can be pruned.
- **Two references are not quotable:**
  - **PMID:27083531** (Frasquet 2016, natural history of c.352+1G>A) cached with `content_type: unavailable`, so it has no quotable text. Don't quote it until a retry succeeds.
  - **PMID:38702287** (Tazir 2024 review) hit an NCBI rate limit (HTTP 429) and was not cached.
- **Identifiers I could not check from a source in this session:** the OMIM phenotype number (614881), the DNAJB2 gene MIM (604139), and any Orphanet, ICD or MeSH codes. Look these up before binding them (CLAUDE.md: "Every CURIE is read from a source in the same step it is written"). MONDO:0013947 and its label are confirmed in `cache/mondo/terms.csv`. The draft's `hgnc:5228` for DNAJB2 should be confirmed with `just validate-terms`.
- **Two issues in the existing draft:**
  - The synonym "DNAJB2-related CMT2" is supported by the literature (several families present as CMT2).
  - The KB entry `Charcot-Marie-Tooth_Disease_Axonal_Type_2T` is **MME**, not DNAJB2. Don't use it as a sibling or template for this gene.

---

## 1. Disease information

**Overview.** HMNR5 is a rare autosomal recessive disease of the lower motor neurons and peripheral axons. It is caused by biallelic loss-of-function variants in **DNAJB2** (also called HSJ1), which encodes a neuron-enriched HSP40/DNAJ co-chaperone of HSP70.
- The first family (Moroccan Jewish, Blumen 2012) had a **pure lower motor neuron** distal hereditary motor neuropathy (dHMN): mostly lower-limb paralysis, starting in early adulthood.
- Later families widened this into a **dHMN ↔ axonal CMT2 continuum**. Sensory involvement often appears with age. Some patients also have parkinsonism, hearing loss or a myopathy.

Key quotes:
- PMID:22522442 (Blumen 2012, Ann Neurol): *"We report here a novel rare variant of dHMN with autosomal recessive inheritance in a large Jewish family originating from Morocco. The disease is characterized by a predominance of paralysis at the lower limbs and an early adulthood onset."*
- PMID:32093037 (Sarparanta 2020, review): *"Recessive DNAJB2 mutations (Table 4) have been identified as a so far uncommon cause of peripheral neuropathies, which may present as distal hereditary motor neuropathy (dHMN) or sensory and motor neuropathy (Charcot–Marie–Tooth disease type 2, CMT2)"*

**Identifiers:**
- MONDO:0013947, label "neuronopathy, distal hereditary motor, autosomal recessive 5" (verified in the cache).
- OMIM phenotype 614881 (HMNR5) and DNAJB2 gene MIM 604139: verify on OMIM.
- Sanchez 2016 (PMID:27449489) writes "DNAJB2 (MIM# 614881)", which uses the phenotype number for the gene. Don't copy that.

**Synonyms:** dHMN5 (AR) / DSMA5 / distal spinal muscular atrophy, autosomal recessive 5 (Saveri uses "dSMA5‑AR"); HSJ1-related hereditary neuropathy; DNAJB2-related CMT2 (AR-CMT2).

**Source type:** Aggregated case reports and small family series. Per the 2026 systematic review, there are about 46 families worldwide. No registry or EHR data exist.

## 2. Etiology

- **Cause:** biallelic germline DNAJB2 variants. Most patients are homozygous, often from consanguineous families.
  - PMID:42806108 (Ghermezcheshmeh 2026): *"In total, 25 distinct DNAJB2 variants were identified across 46 families in the literature, with most occurring in the homozygous state."*
- **Genetic risk:**
  - A recurrent founder allele, c.352+1G>A, is shared by Spanish families and the Moroccan family.
  - PMID:28018906 (Lupo 2016 review): *"Hence, the DNAJB2 c.352+1G>A mutation appears to be a founder event (Lupo et al., 2016), and it is shared with a family reported elsewhere (Blumen et al., 2012)."*
- **Environmental, protective and gene–environment factors:** none reported. No modifier gene is known.
  - Why only some patients develop parkinsonism is unexplained. Saveri (PMID:35286755) excluded PARK2/SNCA dosage changes and found no PD-panel variants in their PD case.
  - Heat or proteotoxic stress is a plausible modifier, but only from in vitro work (see §6).

## 3. Phenotypes

Frequencies are qualitative because the case series are small.

| Phenotype | Suggested HPO (verify) | Onset / course | Frequency | Key evidence |
|---|---|---|---|---|
| Distal lower-limb weakness and atrophy, the first sign | HP:0009053 Distal lower limb muscle weakness (already in the draft); HP:0007210 Lower limb amyotrophy | 2nd–3rd decade; slowly progressive | Nearly all | PMID:32093037: *"pareses, muscle weakness, and atrophy appearing first in distal lower limbs and progressing slowly to proximal lower limbs and arms"* |
| Spread to proximal legs and arms | HP:0008994 Proximal muscle weakness in lower limbs; HP:0008959 Distal upper limb muscle weakness | Later | Common | Saveri: *"progressive weakness in the lower limbs, first distally and then proximally"* |
| Gait difficulty | HP:0001288 Gait disturbance | Presenting symptom | Common | Saveri Table 1 onset ages 28, 28, 15 with "Gait difficulty" |
| Late sensory loss (CMT2 conversion) | HP:0003474 Somatic sensory dysfunction / HP:0010871 Sensory ataxia (rare) | Appears with age | "many if not all" | PMID:32093037: *"Sensory symptoms such as decreased sensation appear with age in many if not all patients"* |
| Axonal motor (± sensory) neuropathy on nerve conduction | HP:0007002 Motor axonal neuropathy; HP:0003477 Peripheral axonal neuropathy | — | All | PMID:35286755: *"Nerve conduction studies showed an axonal motor and sensory length-dependent polyneuropathy."* |
| Pes cavus | HP:0001761 | — | 6/6 in Bjelica | PMID:41549766: *"All six patients had pes cavus; five had scoliosis (P2‐6)."* |
| Scoliosis | HP:0002650 | — | 5/6 (Bjelica) | same |
| Bulbar or respiratory involvement | HP:0002015 Dysphagia; HP:0002093 Respiratory insufficiency | Advanced stage | Occasional | PMID:32093037: *"Bulbar and respiratory symptoms may develop at the advanced stage"* |
| Wheelchair dependence | HP:0002505 Loss of ambulation | 5th–6th decade (Italian family) | Variable | Saveri: *"All patients were wheelchair‐bound from their fifth to sixth decade of life."* |
| Parkinsonism / young-onset PD (levodopa-responsive or partly responsive) | HP:0001300 Parkinsonism | Juvenile (16 y) to 50 y | ~5 reported patients | PMID:41799927 (Lerint 2026): *"The association between clinical Parkinsonism and DNAjB2 variants has only been reported previously in 4 patients."* |
| Sensorineural hearing loss | HP:0000407 | 3rd–4th decade | 3/3 in one Italian family; 1/6 Bjelica | PMID:35286755: *"All patients had severe hearing loss and the proband also had Parkinson's disease (PD)."* |
| Rimmed-vacuolar myopathy on biopsy | HP:0003805 Rimmed vacuoles (verify) | — | Single case | PMID:35652544 |
| Depression | HP:0000716 | — | 6/6 in Bjelica | PMID:41549766: *"All patients with DNAJB2 variants fulfilled criteria for depression, compared with one with a HINT1 variant."* |
| Fatigue | HP:0012378 | — | Majority (Bjelica) | same abstract |
| Postural tremor | HP:0002174 | — | 2/6 (Bjelica) | PMID:41549766 |
| Frontotemporal atrophy with behavioural change; cerebellar ataxia | — | — | Single patients; causal link uncertain | PMID:32093037: *"it remains unclear whether the CNS symptoms in these patients are indeed due to the DNAJB2 mutations or additional factors"* |

**Quality of life.** Bjelica 2026 (PMID:41549766) is the only study that measured it, using SCOPA-AUT, BDI, FSS and painDETECT. Non-motor symptoms (depression, fatigue, autonomic symptoms) reduced quality of life compared with controls.

## 4. Genetic and molecular information

- **Gene:** DNAJB2 (HSJ1), chromosome 2q35 (mapped in Blumen to 2q34–q36.1). HGNC:5228 (check against `cache/hgnc/terms.csv`).
- **Protein:** an N-terminal J domain, a G/F region, a Ser/Thr-rich region, and two ubiquitin-interacting motifs (UIMs). There are two isoforms:
  - HSJ1a/DNAJB2a: 277 aa, cytosolic and nuclear.
  - HSJ1b/DNAJB2b: 324 aa, anchored to the cytoplasmic face of the ER by a C-terminal geranylgeranyl group. This is the main isoform in neurons.
  - PMID:32093037: *"As a unique feature among human J proteins, the C-terminal region of DNAJB2 harbors two ubiquitin interaction motifs (UIMs) that mediate binding to polyubiquitylated proteins and to the proteasome"*

**Reported pathogenic variants (all germline, mostly homozygous):**

| Variant (NM_006736) | Type | Phenotype | Source |
|---|---|---|---|
| c.352+1G>A | splice donor; Spanish/Moroccan founder | dHMN/CMT2, YOPD | PMID:22522442; 28018906; 41799927 (compound het with c.175+2T>A) |
| c.229+1G>A | splice donor → intron 4 retention, protein lost | dHMN | PMID:25274842 |
| c.14A>G p.Tyr5Cys | missense in J domain | CMT2 | PMID:25274842 |
| c.619-1G>A; c.310delC | splice acceptor; frameshift | dHMN/CMT2 | cited in PMID:32093037 |
| ~3.8 kb deletion of exons 1–3/4 (+ upstream) | structural, null | SMA + juvenile parkinsonism | PMID:27449489 |
| c.145delG p.Val49TrpfsTer25 | frameshift, null | CMT2 + deafness + PD | PMID:35286755 |
| c.184C>T | nonsense (verify protein change) | dHMN + rimmed-vacuolar myopathy | PMID:35652544 |
| c.446-1G>A (also c.446-1G>C); c.445+1del (new) | splice | dHMN or CMT2 | PMID:41549766; 42806108 |
| c.99C>G p.Asp33Glu | missense, VUS | CMT2 | PMID:41549766 |
| c.175+2T>A | splice | CMT2 + YOPD (compound het) | PMID:41799927 |

Key quotes:
- PMID:25274842 (Gess 2014): *"One family with a dHMN phenotype showed the homozygous splice-site mutation c.229+1G>A, which leads to retention of intron 4 in the HSJ1 messenger RNA with a premature stop codon and loss of protein expression."*
- Same paper: *"we confirm that HSJ1 mutations are a rare but detectable cause of autosomal recessive dHMN and CMT2."*

**Functional consequence:** loss of function, with no protein detected.
- PMID:35286755: *"DNAJB2 expression studies revealed reduced mRNA levels and the absence of the protein in the homozygous subject in both LCLs and skin biopsy."*
- Saveri also found heterozygous carriers at 40% of normal protein and clinically unaffected, which supports a recessive, threshold-type mechanism.

**Genotype–phenotype:** PMID:42806108 found *"marked clinical heterogeneity but not a significant genotype-phenotype correlation."*

**Population frequency:** c.145delG and c.14A>G are absent from gnomAD (per the papers). Pull gnomAD frequencies for the founder allele directly; I did not retrieve them.

**Separate entities to keep out of this entry:**
- A **heterozygous** c.823+6C>T VUS in an adult sensory-motor polyneuropathy (PMID:40423229, classified VUS).
- A **dominant** DNAJB2a isoform-extension neuromyopathy (PMID:37070754).

Neither fits the HMNR5 recessive loss-of-function model. Record them as notes or exclusions, not as pathogenic variants for this disease.

**Epigenetic and chromosomal findings:** none reported, apart from the structural deletion above.

## 5. Environmental information

None reported: no environmental, lifestyle or infectious factors. The `environmental:` section would be empty; if a block is added, use a `Left deliberately uncited.` waiver.

## 6. Mechanism and pathophysiology

**Causal chain** (steps marked *inferred* are not directly shown in patient neurons):

1. **Biallelic DNAJB2 null or splice variants** lead to intron retention, premature stop codons or deletion of the J domain. Both HSJ1a and HSJ1b are lost (shown in patient fibroblasts, lymphoblastoid cells and skin).
   - PMID:22522442: *"identified a homozygous splice mutation in the gene HSJ1 (DNAJB2) decreasing the expression of the 2 main isoforms HSJ1a and HSJ1b."*
2. **Loss of the HSJ1 co-chaperone** removes J-domain stimulation of HSPA8/HSP70 ATPase activity. It also removes UIM-mediated handoff of ubiquitinated clients to the proteasome and STUB1/CHIP-assisted ubiquitination.
   - PMID:32093037: *"Instead of promoting the refolding of HSPA clients, DNAJB2 is considered to primarily direct them to degradation by the ubiquitin–proteasome system (UPS)"*
3. **Protein quality control fails** (ubiquitin–proteasome and ER-associated degradation via HSJ1b; *inferred*). This leads to accumulation and aggregation of misfolded clients such as TDP-43, mutant SOD1 and α-synuclein.
   - PMID:35286755: *"The mutation likely acts through a loss-of-function mechanism, leading to toxic protein aggregation such as TDP-43."*
   - Patient skin showed phospho-TDP-43. The patient with PD also had phospho-α-synuclein deposits in skin nerves.
4. **Branch A (main): motor neurons in the spinal cord anterior horn and their long axons degenerate** (*inferred*; no patient spinal cord pathology has been reported). This produces length-dependent axonal loss, first in long lower-limb motor axons, and later in sensory axons (sural biopsy: loss of large fibres).
   - PMID:22522442: *"this mutation causing a loss-of-function of HSJ1 is linked to a pure lower motor neuron disease, strongly suggesting that HSJ1 also plays an important and specific role in motor neurons."*
5. **Denervation** causes distal muscle atrophy and weakness, then pes cavus and scoliosis, then loss of ambulation. Occasionally there are secondary myopathic changes with rimmed vacuoles (PMID:35652544).
6. **Branch B: degeneration of dopaminergic nigrostriatal terminals** (DaT-scan shows presynaptic deficit) in a subset, leading to parkinsonism.
   - The Sanchez deletion study links HSJ1b loss to reduced BDNF and tau levels (HEK293 cells only).
   - Branch C: auditory-nerve involvement causing sensorineural deafness. Saveri proposes this ("We hypothesize the same mechanism"); it is not demonstrated.
- **Alternative or additional mechanism (hypothesis):** loss of HSJ1b-dependent trafficking or secretion, such as Golgi clathrin-coated-vesicle sorting and BDNF secretion. PMID:32093037: *"the pathomechanism could be envisioned to depend on cytotoxicity due to impaired protein quality control and turnover or a specific defect in protein trafficking or secretion caused by loss of DNAJB2b."*
- **Known gap** (suits a `KNOWLEDGE_GAP` discussion): PMID:35286755: *"skin biopsy analysis showed a complete loss of DNAJB2 expression in patients that was not associated with an impairment of NF, leaving the pathomechanism of the axonal loss still unclear."*

**Suggested GO terms** (look each one up before binding):
- protein folding chaperone / Hsp70 protein binding / ATPase activator activity (molecular function)
- proteasome-mediated ubiquitin-dependent protein catabolic process
- ERAD pathway
- negative regulation of protein aggregation / protein refolding
- response to heat (HSJ1 is heat-inducible; PMID:40423229)
- neuron projection maintenance / axon degeneration

**Suggested CL terms:** lower motor neuron / spinal cord motor neuron; dopaminergic neuron (Branch B); sensory neuron; skeletal muscle fibre (secondary).

**Suggested GO cellular component terms:** cytosol, nucleus (HSJ1a); ER membrane, cytoplasmic side (HSJ1b); proteasome complex.

**Suggested `biological_scale` tags:** step 1 MOLECULAR; steps 2–3 CELLULAR; step 4 TISSUE; steps 5–6 ORGANISM.

**Omics, single-cell and CRISPR data:** none specific to HMNR5.

## 7. Anatomical structures

- **Primary:** peripheral nervous system, specifically spinal motor neurons and their axons (UBERON: ventral horn of spinal cord; peripheral nerve; sciatic/peroneal nerve).
- **Secondary:** distal leg muscles (anterior and posterior leg compartments more than thigh on CT, per Saveri), then the hands; foot (pes cavus); vertebral column (scoliosis).
- **Central nervous system in a subset:** substantia nigra and striatal dopaminergic terminals; auditory nerve.
- **Laterality:** bilateral and symmetric. The parkinsonism can be asymmetric.

## 8. Temporal development

- **Onset:** usually the 2nd decade, with a reported range from the late 1st to early 4th decade (PMID:32093037). In Bjelica, onset was 17–21 y.
- **Pattern:** insidious, starting with gait difficulty.
- **Progression:** slow and continuous. The only quantitative natural history is PMID:41549766: *"all patients with DNAJB2 variants experienced a progressive loss of motor function over a follow‐up period of up to 10 years, with an annual decline in the MRC‐SS score of 0.78 points per year."*
- **Suggested phases for `progression:`:**
  1. Pure distal motor (dHMN) phase.
  2. Proximal and upper-limb spread with later sensory involvement (CMT2 phase).
  3. Advanced phase: wheelchair use in the 5th–6th decade in severe families; possible bulbar or respiratory involvement.
- **Remission:** none.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007, verify). Penetrance appears complete in homozygotes. Expressivity varies (dHMN vs CMT2 ± parkinsonism or deafness, even within one family). Heterozygous carriers are unaffected (Saveri). There is no anticipation.
- **Consanguinity:** frequent (Iranian, Syrian and Moroccan families).
- **Founder allele:** c.352+1G>A in Spain and Morocco (Moroccan Jewish), and reported in Brazil.
- **Prevalence:** no disease-specific estimate. Use `prevalence_class: NOT_YET_DOCUMENTED` or `measure_type: CASES_IN_LITERATURE` with "~46 families" (PMID:42806108).
- **Context — pooled hereditary motor neuropathy prevalence:** PMID:36445400: *"Their cumulative estimated prevalence is 2.14/100 000"*.
- **Share of dHMN caused by DNAJB2:** in a European cohort, DNAJB2 explained 6.7% of genetically solved dHMN (PMID:33369814: *"The most frequent cause of distal hereditary motor neuropathies were mutations in HSPB1 (10.4%), GARS1 (9.8%), BICD2 (8.0%), and DNAJB2 (6.7%) genes."*).
- **Sex ratio:** no bias reported.

## 10. Diagnostics

- **Nerve conduction and EMG:** reduced compound muscle action potentials with relatively preserved conduction velocities (axonal pattern). Sensory potentials are normal early (dHMN) and reduced later (CMT2). EMG shows chronic denervation.
- **Muscle imaging:** CT/MRI shows fatty replacement of the leg more than the thigh.
- **Biopsy:**
  - Sural nerve: loss of large myelinated fibres with acute axonal degeneration.
  - Muscle: neurogenic changes, with rimmed vacuoles in one case.
  - Skin: loss of DNAJB2 immunostaining in dermal axons, and phospho-TDP-43 and phospho-α-synuclein deposits. These are research findings, but skin DNAJB2 immunostaining could serve as a functional test of variant pathogenicity.
- **DaT-scan** when parkinsonism is present. **Audiometry and brainstem auditory evoked potentials** — Saveri recommends DNAJB2 testing in CMT2 or dSMA with deafness.
- **Genetic testing:** multigene neuropathy/dHMN panels or whole-exome sequencing. Copy-number or whole-genome analysis is needed to find the structural deletion (found by whole-genome sequencing in PMID:27449489). Splice variants can be confirmed with fibroblast or lymphoblastoid RNA/protein studies.
  - Diagnostic yield for dHMN is low overall: PMID:32298515 solved 24/70 (34.3%) and placed DNAJB2 among the "dHMN-plus" genes. Fernández-Eulate 2023 (PMID:37470033) reports non-5q SMA yield and is cached but I did not extract a DNAJB2 figure.
- **Differential diagnosis:**
  - Other recessive dHMN/CMT2 genes: HINT1 (earlier, childhood onset, neuromyotonia; PMID:41549766), SIGMAR1, IGHMBP2, MME (later onset).
  - Dominant dHMN genes: HSPB1, HSPB8, GARS1, BICD2.
  - 5q SMA (exclude by SMN1 testing), ALS (no upper motor neuron signs here), and Perry syndrome / DCTN1 when parkinsonism is present.
- **Screening:** carrier or cascade testing within families. There is no newborn screening.

## 11. Outcome and prognosis

- **Survival:** no data. Life expectancy is presumed near-normal in pure dHMN; this is not documented.
- **Morbidity:** progressive motor disability, with wheelchair dependence in severe families by the 5th–6th decade. Disease severity on CMTESv2 was 17–20 (moderate to severe) in Saveri.
- **Complications:** bulbar or respiratory involvement late; deafness; parkinsonism; depression; fatigue.
- **No recovery is expected.** No prognostic biomarkers are known. Parkinsonism and deafness appear to mark a more severe course, based on very few cases.

## 12. Treatment

There is no disease-modifying therapy and no registered DNAJB2-specific trial. Management is supportive. Suggested NCIT terms below are listed in CLAUDE.md, but verify each before use.

- **Physical therapy:** NCIT:C15302, `therapeutic_modality: BEHAVIORAL`.
- **Rehabilitation:** NCIT:C15315.
- **Orthotics / ankle-foot orthoses:** a device; bind the action and use a device qualifier per CLAUDE.md.
- **Orthopaedic surgery** for foot deformity or scoliosis: NCIT:C16186, `SURGERY`.
- **Genetic counselling:** NCIT:C15240.
- **Levodopa** for parkinsonism: NCIT:C15986 pharmacotherapy plus a CHEBI levodopa `therapeutic_agent` (look the CHEBI ID up).
  - Response: good in the Italian proband (Saveri, *"responsive to L‐DOPA treatment"*), moderate in the juvenile case (Sanchez).
- **Hearing aids** for sensorineural hearing loss.
- **Experimental, preclinical only:**
  - Cystamine raised HSJ1a and HSJ1b levels in fibroblasts. This was shown in a *heterozygous VUS* line, so its relevance to recessive null HMNR5 is weak.
    - PMID:40423229: *"A 48-h pretreatment with 150 μM of Cystamine increased the levels of DNAJB2 in both the control and patient's fibroblasts."*
  - Gene replacement (AAV-DNAJB2) is a logical approach for a recessive loss-of-function disease but has not been reported.
  - Saveri suggests TDP-43 clearance as a possible target.
- **Pharmacogenomics:** none.

## 13. Prevention

- **Primary:** none.
- **Reproductive options:** genetic counselling, carrier testing of relatives and partners in consanguineous families, prenatal or preimplantation testing once familial variants are known (25% recurrence risk for sibs).
- **Tertiary:** prevent contractures and falls; monitor for scoliosis, bulbar or respiratory decline, hearing and parkinsonism.

## 14. Other species

No naturally occurring DNAJB2 disease is described in animals (OMIA not checked in this session).

## 15. Model organisms

- **No published Dnajb2-null model reproduces the disease.**
  - Sarparanta 2020 mentions "studies on Dnajb2-deficient mice" only as a personal communication about antibody specificity.
  - Search MGI/IMPC for a *Dnajb2* knockout allele before claiming there is none.
- **Overexpression models** (relevant to mechanism, but not models of the disease):
  - HSJ1a overexpression delayed late-stage disease in SOD1-G93A ALS mice (PMID:24023695, Novoselov 2013).
  - HSJ1 overexpression reduced polyQ inclusions (PMID:28182921).
  - HSJ1 overexpression reduced SOD1-A4V inclusions in neuronal cells (Blumen).
  - HSJ1a helps clear TDP-43 (PMID:26936937).
  - For pathograph links, mark these as `PERTURBS` or `RESCUES`, not `RECAPITULATES`, at LOW or UNKNOWN fidelity, with a `limitations` note that they test gain, not loss, of HSJ1.
- **Patient-derived cells:**
  - Fibroblasts (Blumen, Gess, Pradhan) and lymphoblastoid cell lines (Saveri): loss of expression.
  - HEK293 cells expressing a J-domain-deleted HSJ1b construct (Sanchez): aggregation, autophagy (LC3), lower BDNF and tau.
  - No iPSC-derived motor neurons have been reported. This gap could be recorded as a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion: the patient samples studied are not neurons, and why loss of a ubiquitously low-expressed chaperone is selectively toxic to motor neurons is unresolved.

---

### Cached references for evidence

| PMID | Paper | Content |
|---|---|---|
| 22522442 | Blumen 2012 | first family, mechanism (abstract) |
| 25274842 | Gess 2014 | c.229+1G>A, p.Tyr5Cys (abstract) |
| 27449489 | Sanchez 2016 | deletion + parkinsonism (full text) |
| 35286755 | Saveri 2022 | null variant, deafness, PD, TDP-43 (full text) |
| 35652544 | Liu 2022 | myopathy (abstract) |
| 32298515 | Liu 2020 | Chinese dHMN cohort (abstract) |
| 32093037 | Sarparanta 2020 | review (full text) |
| 28018906 | Lupo 2016 | review, founder effect (full text) |
| 41549766 | Bjelica 2026 | natural history, QoL (full text) |
| 41799927 | Lerint 2026 | compound het + YOPD (full text) |
| 42806108 | Ghermezcheshmeh 2026 | systematic review (abstract) |
| 40423229 | Pradhan 2025 | heterozygous VUS, cystamine (full text) |
| 24023695 | Novoselov 2013 | SOD1 mouse overexpression |
| 26936937 | Chen 2016 | TDP-43 clearance |
| 28182921 | Howarth 2017 | polyQ inclusions |
| 20395441 | Claeys 2010 | DNAJB2 expression in muscle |
| 37070754 | Sarparanta 2023 | dominant extension; exclusion only |
| 37470033 | Fernández-Eulate 2023 | non-5q SMA diagnostic yield |
| 26752306 | Lupo 2016 | targeted sequencing |
| 28031292 | Ottaviani 2017 | CK2 phosphorylation of UIM2 |

Also already in the cache: PMID:33369814, PMID:36445400 (epidemiology). **Not quotable:** PMID:27083531 (empty cache); PMID:38702287 (not cached). PMID:26556829 was fetched by mistake (it is an SPG11 paper); delete it rather than commit it.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 0 |

27 of 28 terms resolved to a current term; the rest could not be looked up either way.