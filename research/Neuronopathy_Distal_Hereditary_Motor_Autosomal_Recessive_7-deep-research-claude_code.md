---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001
cached: false
start_time: '2026-09-19T02:40:21.950191'
end_time: '2026-09-19T02:43:39.144125'
duration_seconds: 197.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neuronopathy, Distal Hereditary Motor, Autosomal Recessive 7
  mondo_id: MONDO:0030977
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  web_search_requests: 2
  num_turns: 8
  total_cost_usd: 4.899703000000001
  session_id: 79d469d8-c55c-4fa5-8bb7-b2680d852ed2
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 12
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 30
  quotes_valid: 29
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:39502942
  relevance_assessed: 15
  on_topic: 10
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 35
  labels_matching: 24
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0030977
    reported_labels:
    - MONDO
    ontology_label: neuronopathy, distal hereditary motor, autosomal recessive 7
  - term_id: GO:0000184
    reported_labels:
    - NMD
    ontology_label: nuclear-transcribed mRNA catabolic process, nonsense-mediated
      decay
  labels_variant: 9
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neuronopathy, Distal Hereditary Motor, Autosomal Recessive 7
- **MONDO ID:** MONDO:0030977 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Neuronopathy, Distal Hereditary Motor, Autosomal Recessive 7** covering all of the
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

I'll research this disease using the curated knowledge base entry in this repo (which contains verified PMIDs and quotes) plus web searches for recent literature.

The local curated entry is a goldmine of verified PMIDs and exact quotes. Let me read the rest of it, then supplement with targeted web checks.

I have the full curated entry with verified quotes. One more quick check for identifiers (OMIM, Orphanet) and any additional recent literature, then I'll write the report.

I now have everything needed: the repository's curated, snippet-verified entry for this disease (built on the primary literature) plus current web sources. Here is the complete research report.

---

# Research Report: Neuronopathy, Distal Hereditary Motor, Autosomal Recessive 7 (HMNR7 / VWA1-Related Neuromyopathy)

**MONDO:0030977 · OMIM #619216 · Gene: VWA1 (HGNC:30910, lowercase repo form `hgnc:30910`)**
Report date: 2026-09-19

---

## 1. Disease Information

**Overview.** Autosomal recessive distal hereditary motor neuronopathy type 7 (HMNR7) is a childhood-onset, slowly progressive motor neuropathy caused by biallelic loss-of-function variants in **VWA1**, which encodes the extracellular matrix protein **WARP** (von Willebrand factor A domain-related protein). The disease was defined simultaneously by two independent 2021 cohorts in *Brain*: Pagnamenta et al. described it as a non-length-dependent "hereditary motor neuropathy" (PMID:33559681), while Deschauer et al. described the same entity as a "neuromyopathy" with combined neurogenic and myopathic pathology (PMID:33459760). It presents in the first years of life with foot deformity, tip-toe gait, and foot drop, with weakness that — unusually for this disease family — involves proximal lower limbs as severely as distal ones, plus a myopathic component (raised CK, occasional myopathic EMG/biopsy findings).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0030977 |
| OMIM (phenotype) | #619216 (HMNR7) — [omim.org/entry/619216](https://omim.org/entry/619216) |
| OMIM (gene) | *611901 (VWA1) — [omim.org/entry/611901](https://omim.org/entry/611901) |
| HGNC | HGNC:30910 (VWA1) |
| Orphanet | No dedicated ORPHA code identified in this search |
| ICD-10 | G60.0 (hereditary motor and sensory neuropathy, closest applicable code; no disease-specific code) |
| Locus | Chromosome 1p36.33 |

**Synonyms:** HMNR7; HMNMYO ("neuropathy, hereditary motor, with myopathic features"); VWA1-related neuromyopathy; VWA1-related distal hereditary motor neuropathy; VWA1-related disorder.

**Data provenance.** All clinical knowledge derives from aggregated case-series/cohort literature (54 published patients as of late 2024: "Results are based on data from 54 patients (n = 20 from presented cohort and n = 34 from previous publications)" — PMID:39502942), not EHR-level data.

---

## 2. Etiology

**Causal factor (established):** Biallelic germline loss-of-function variants in *VWA1*. "Exome sequencing led us to identify bi-allelic loss of function variants in VWA1 as the molecular cause underlying a so far genetically undefined neuromuscular disorder" (PMID:33459760, 2021). Independently: "we identified 17 individuals from 15 families with an autosomal-recessive, non-length dependent, hereditary motor neuropathy and rare biallelic variants in VWA1" (PMID:33559681, 2021).

**Genetic risk factors.** The dominant risk allele is the Western European founder duplication NM_022834.5:c.62_71dup p.(Gly25ArgfsTer74) — carrier frequency ~1 in 441 in the UK/Western European population (PMID:39502942, 2024). It arose on "a shared 220 kb region suggesting that this founder mutation arose >7000 years ago" (PMID:33559681). Because one allele is this common, the usual genetic setting is two unrelated carriers meeting rather than consanguinity; only one of fifteen families in the first cohort had a positive family history, the rest being sporadic.

**Environmental risk/protective factors:** None reported. This is a fully penetrant-appearing monogenic Mendelian disease; no environmental triggers, lifestyle modifiers, protective variants, or gene–environment interactions have been described in any published cohort. (CTD, GWAS Catalog: no relevant entries for this phenotype.)

---

## 3. Phenotypes

All frequencies below come from the two founding cohorts (17 patients, PMID:33559681; 15 patients, PMID:33459760) and the 2024 20-patient cohort/54-patient literature synthesis (PMID:39502942).

| Phenotype | HPO term | Frequency | Onset/severity/course |
|---|---|---|---|
| Motor axonal neuropathy | HP:0007002 | Obligate (diagnostic) | Reduced/absent CMAPs, preserved velocities, normal sensory studies |
| Foot dorsiflexor weakness (foot drop) | HP:0009027 | Very frequent | Usually bilateral, presenting sign |
| Distal lower limb weakness | HP:0009053 | Very frequent | MRC 1–3 for foot/toe movements; onset birth–12 y |
| Proximal lower limb weakness | HP:0008994 | ~50% (frequent) | Simultaneous with distal — the non-length-dependent hallmark |
| Pes cavus | HP:0001761 | 65% (11/17) | Mostly before school age |
| Talipes equinovarus | HP:0001762 | 35% (6/17) | Congenital in two cases |
| Achilles tendon contracture | HP:0001771 | >50% | Early; contractures also at knee/hip, sometimes upper limb |
| Tip-toe gait | HP:0030051 | Frequent | Mean symptom recognition 2.0 ± 1.4 y |
| Hyporeflexia | HP:0001265 | ~50% | |
| Skeletal muscle atrophy | HP:0003202 | Frequent but **mild** | Prominent atrophy characteristically absent |
| Elevated CK | HP:0003236 | Frequent | 369–1628 IU/L (cohort 1); up to 2400 U/L (cohort 2) |
| EMG: chronic denervation signs | HP:0003444 | 10/12 studies | Without active denervation |
| EMG: myopathic abnormalities | HP:0003458 | Minority (3/12; 1/20) | Mixed neurogenic-myopathic signature |
| Fiber type grouping (biopsy) | HP:0033685 | Frequent | Denervation-reinnervation signature |
| Scoliosis / lumbar hyperlordosis | HP:0002650 / HP:0002938 | ~50% each | |
| Falls | HP:0002527 | ~33% | Ambulation nonetheless preserved |
| Tongue fasciculations | HP:0001308 | Occasional (2+2 patients) | Pushes differential toward juvenile ALS |
| Scapular winging | HP:0003691 | Occasional (n=2) | Also in the new 2026 case (PMID:41416782) |
| Hyperreflexia / spasticity (UMN signs) | HP:0001347 / HP:0001257 | Occasional, **contested** | Absent in first cohort ("uniformly negative Babinski sign"), reported in later cohorts (PMID:35975723, PMID:39502942) |
| Joint hypermobility | HP:0001382 | n=1 | |
| Dystonia | HP:0001332 | n=1 | |
| Increased endomysial connective tissue | HP:0100297 | Occasional | |
| Motheaten muscle fibers | HP:0100298 | Rare, non-specific | |

Key supporting quotes: "Of note, bilateral foot deformity was a very frequent feature revealed in almost 90% of the cases (15/17), ranging from pes cavus (65%, 11/17) to talipes equinovarus (35%, 6/17)" (PMID:33559681). "While the most common features of VWA1-related disease include foot drop, foot deformities and distal lower limb weakness, about half of the so far reported individuals develop proximal leg weakness over time, and approximately one-third experience upper limb involvement" (PMID:39502942).

A 2026 case report added **minipolymyoclonus and fasciculations** to the spectrum ([Sharma et al., Muscle & Nerve 2026, PMID:41416782](https://pubmed.ncbi.nlm.nih.gov/41416782/)).

**Quality-of-life impact:** No formal QoL instrument (EQ-5D/SF-36) study exists. Functionally the disease is comparatively benign: "the condition may go unnoticed for years to decades due to its relatively benign nature, often presenting mild neurological deficits, the absence of prominent muscle atrophy and slow disease progression" (PMID:39502942). Only 3/17 patients lost independent ambulation over a median 36.5-year disease duration.

---

## 4. Genetic/Molecular Information

**Causal gene:** *VWA1* (HGNC:30910; OMIM *611901; chromosome 1p36.33), encoding the 445-amino-acid extracellular matrix protein WARP: "In humans, VWA1 (von Willebrand factor A domain containing 1) encodes a 445 amino acid ECM protein that is also referred to as von Willebrand factor A domain related protein (WARP)" (PMID:33559681).

**Founder/pathogenic variants:**
- **NM_022834.5:c.62_71dup p.(Gly25ArgfsTer74)** — the disease-defining allele: a 10-bp duplication expanding a 2-copy 10-bp repeat in exon 1 to 3 copies ("This variant involves an expansion of a 10 bp repeat in Exon 1 of VWA1, leading to three copies instead of two compared with normal alleles" — PMID:39502942). Present in 14/15 families in the first cohort (homozygous in 10/15) and 12/15 in the 2024 cohort. Classification: Pathogenic. **Allele frequency:** "The maximum population allele frequency of the most common variant across all databases remained the highest in the European non-Finnish with 0.093% in gnomAD v4.0.0 and 0.118% in UK Biobank" (PMID:39502942); the discovery paper estimated ~1/847 European allele frequency.
- The wider spectrum is dominated by **truncating variants** (stop-gains, frameshifts) plus a few missense changes at proline residues and one in-frame deletion in the VWA domain. Deschauer: "We detected six different truncating variants in 15 affected individuals from six families of German, Arabic, and Roma descent" (PMID:33459760). The 2024 cohort reported 13 additional variants (11 novel), mostly compound heterozygous with the founder allele in trans.
- A reciprocal 10-bp deletion (c.62_71del, p.G21Afs*12) exists at the same locus and was speculated to be a second founder allele, but no biallelic case has been reported.

**Functional consequence: loss of function via NMD.** "Duplex reverse transcription polymerase chain reaction and immunoblotting using patient fibroblasts revealed that the founder allele results in partial nonsense mediated decay and an absence of detectable protein" (PMID:33559681).

**Origin:** Germline in all cases; no somatic contribution. **Modifier genes, epigenetics, chromosomal abnormalities:** none described.

**Critical technical note for variant detection:** "This novel disease gene may have previously evaded detection because of high GC content, consequential low coverage and computational difficulties associated with robustly detecting repeat-expansions" (PMID:33559681). This is the single most important practical fact about the gene.

---

## 5. Environmental Information

Not applicable. No environmental, lifestyle, occupational, or infectious factors cause, trigger, or modify this monogenic disease in any published report.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered; branch point marked):**

1. **Biallelic VWA1 loss-of-function variants** (germline; predominantly the exon 1 founder duplication) *lead to* →
2. **Nonsense-mediated decay of mutant transcript and absence of WARP protein** (demonstrated in patient fibroblasts: "there was no detectable VWA1 in either the conditioned medium or cell layer of the patient's fibroblast" — PMID:33559681) *results in* →
3. **Depletion of WARP from nerve (and muscle) basement membranes.** WARP is normally abundant in peripheral nerve — highest human tissue expression in tibial nerve — where it binds collagen VI and perlecan ("WARP interacts with perlecan, and we also demonstrate here that WARP binds type VI collagen, suggesting a function in bridging connective tissue structures" — PMID:19279005). In the knockout mouse this loss produces "reduced fibrillar collagen deposition within the peripheral nerve extracellular matrix and abnormal partial fusing of adjacent Schwann cell basement membranes" and a collagen VI matrix that "was severely reduced and mislocalized in peripheral nerves of WARP-null mice" (PMID:19279005). *This leads to* (branch):
   - **4a. Impaired motor axon outgrowth and neuromuscular junction formation** (zebrafish; **inferred for humans**): "CRISPR and morpholino vwa1 modelling in zebrafish demonstrated reductions in motor neuron axonal growth, synaptic formation in the skeletal muscles and locomotive behaviour" (PMID:33559681). The route from this developmental deficit to adult axon loss is *not demonstrated*.
   - **4b. (Contested branch) Primary muscle extracellular-matrix lesion** — see controversy below.
5. **Non-length-dependent motor axon loss** *results in* reduced/absent CMAPs with preserved velocities, simultaneous proximal + distal weakness ("Most of the cases (75%) were found to have simultaneous proximal and distal lower limb weakness" — PMID:33559681), foot drop, hyporeflexia. *Leads to* →
6. **Chronic neurogenic denervation of skeletal muscle** (EMG chronic neurogenic change 10/12; fiber type grouping; neurogenic atrophy) *which, on the canonical model, produces* →
7. **Secondary myopathic change** — raised CK, dystrophic biopsy features, myopathic EMG in a minority — culminating in the clinical picture of an early-onset, slowly progressive neuromyopathy with foot deformity and contractures.

**The central unresolved controversy** — is the muscle involvement secondary to denervation (canonical) or a primary matrix lesion (alternative)? Explicitly open in the literature: "there is no common consent if the muscular affection is a secondary pathology based on vulnerability and dysfunction of motoric axons or if a primary muscle pathology is rather part of the clinical picture" (PMID:38652110, 2024).
- *For secondary:* "We speculate that a few findings of myopathic changes might be secondary to chronic denervation rather than indicating an additional myopathic disease process" (PMID:33559681); collagen VI immunolabelling normal in patient muscle; the WARP-null mouse shows **no** muscle pathology ("articular cartilage, intervertebral discs, and skeletal muscle showed no detectable abnormalities" — PMID:19279005).
- *For primary:* "Myopathological and neurophysiological findings were indicative of combined neurogenic and myopathic pathology" (PMID:33459760); 2024 proteomics found "CRP elevated in plasma also showed an increase in the extracellular space of VWA1-mutant muscle" and "NEFM showed an increase in cells within the ECM in biopsies of all patients studied" (PMID:38652110); muscle MRI shows "a distinctive outside-in pattern of fatty replacement in the vastus lateralis, resembling that seen in type VI collagen-related myopathies" (PMID:41331965, 2025; replicated in 3 patients in PMID:42662709, 2026).

**Ontology suggestions:** GO:0000184 (NMD), GO:0005201 (ECM structural constituent), GO:0071711 (basement membrane organization), GO:0048675 (axon extension), GO:0007528 (NMJ development), GO:0030198 (ECM organization); CL:0000100 (motor neuron), CL:0002573 (Schwann cell), CL:0008002 (skeletal muscle fiber).

**Molecular profiling (2024):** Plasma proteomics identified 15 dysregulated biomarker candidates, "a profound proportion of increased ones (6/11) are mostly related to antioxidative processes" (PMID:38652110). No transcriptomic, single-cell, spatial, or metabolomic studies exist.

---

## 7. Anatomical Structures Affected

- **Primary:** Peripheral motor nerves/lower motor neurons (UBERON:0001323 tibial nerve — site of highest WARP expression; spinal motor axons); skeletal muscle (UBERON:0001134), especially anterior lower-leg compartment, vastus lateralis, gluteus maximus, peroneal muscles.
- **Secondary/musculoskeletal:** Feet (pes cavus, equinovarus), Achilles tendon, spine (scoliosis, hyperlordosis), knee/hip joints (contractures, recurrent hip and patellar dislocations).
- **Explicitly spared:** heart, respiratory muscles, cognition — "No associated neurocognitive symptoms were observed. Cardiac or respiratory involvement was not reported" (PMID:39502942); sensory nerves in most patients.
- **Cellular:** motor neurons (CL:0000100), Schwann cells (CL:0002573; basement membrane fusion in the mouse), skeletal muscle fibers (CL:0008002).
- **Subcellular/matrix compartment:** the basement membrane / extracellular matrix (GO:0005604 basement membrane) — this is an ECM disease, not an organelle disease.
- **Lateralization:** typically bilateral; asymmetric presentations occur (one patient with unilateral foot drop, pes cavus on one side and pes planus on the other).

---

## 8. Temporal Development

- **Onset:** birth to 12 years; mean symptom recognition 2.0 ± 1.4 years (tip-toe walking, foot deformity, Achilles contracture); foot deformity congenital in two cases, "suggesting antenatal onset of the disease" (PMID:33559681). The 2024 review corrects earlier impressions: "early-onset foot deformities, contractures, and gait abnormalities have been consistently reported in nearly all individuals … suggesting an early or even infantile disease onset rather than adult onset" (PMID:39502942).
- **Course:** chronic, lifelong, insidious. "Overall, the disease progression was very slow or even static in several cases. Isolated cases reported some clinical worsening after the fifth decade of life" (PMID:33559681).
- **No remissions, no episodic pattern.** Independent walking achieved at mean 1.6 ± 0.8 y, delayed with severe bilateral equinovarus.
- **Critical window:** early childhood for contracture/deformity management (inference from natural history, not a studied intervention window).

---

## 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (HP:0000007); homozygosity for the founder allele or compound heterozygosity (usually with the founder allele in trans). Pedigrees overwhelmingly *appear* sporadic ("Positive family history was reported only in Family 13, while the rest of the cases were sporadic" — PMID:33559681).
- **Carrier frequency:** ~**1 in 441** for c.62_71dup in UK/Western Europeans (PMID:39502942) — remarkably high for a "rare" disease.
- **Founder effect:** yes — 220-kb shared haplotype, >7,000 years old (PMID:33559681).
- **Consanguinity:** reported but not the usual setting (2/15 families in the 2024 cohort, Iranian and Pakistani).
- **Penetrance/expressivity:** formally unquantified; intrafamilial variability documented (one sibling with proximal weakness, the other with only dystonic features — PMID:39502942). No anticipation, no germline mosaicism reported.
- **Prevalence:** no published point prevalence; 54 patients in the literature as of 2024. The burden is believed to be substantially under-ascertained: "we estimate that biallelic variants in VWA1 may be responsible for up to 1% of unexplained hereditary motor neuropathy cases in Europeans" (PMID:33559681); Pagnamenta et al. inferred up to ~100 undiagnosed biallelic individuals in the UK alone. Reported ancestries: Western European, German, Arabic, Roma, Iranian, Pakistani, North American, Spanish, Indian. No sex bias established.

---

## 10. Diagnostics

- **Electrophysiology (cornerstone):** motor axonal neuropathy — "Motor nerve action potentials from the lower limb nerves were reduced or undetectable with uniformly preserved conduction velocities. Sensory studies were overall normal" (PMID:33559681); needle EMG with chronic neurogenic change (10/12), occasionally mixed with myopathic units.
- **Laboratory:** elevated CK (up to 2400 U/L) — the finding that misdirects workups toward muscular dystrophy.
- **Muscle MRI:** T1 fatty replacement predominantly vastus lateralis + anterior lower leg; a **gene-specific whole-body pattern**: "selective gluteus maximus and quadriceps involvement with iliopsoas, gracilis, and sartorius preservation, and predominant peroneal involvement with relative extensor digitorum longus sparing" (PMID:42662709, 2026) — proposed as a pre-test guide to sequencing, though "not exclusive." Outside-in vastus lateralis gradient mimicking collagen VI myopathy (PMID:41331965).
- **Muscle ultrasound:** moth-eaten pattern of chronic denervation; nerve ultrasound normal.
- **Biopsy:** neurogenic atrophy with fiber type grouping (majority); dystrophic/myopathic features in a minority (ring fibres, rimmed vacuoles, endomysial fibrosis); **collagen VI immunolabelling normal** — the key negative.
- **Genetic testing (definitive):** WES/WGS or gene panel — **but the founder allele is systematically missed by standard pipelines** (GC-rich repeat, low coverage). Recommendations: relaxed QC filters on exome re-analysis ("Reviewing previously unsolved exomes using lower QC filters may generate further diagnoses" — PMID:33559681) and targeted Sanger of exon 1 (a screen of 1,341 unsolved neuropathy samples yielded 3 additional diagnoses). "VWA1 should be included in multiple gene panels covering hereditary neuropathies, muscle dystrophies, hereditary spastic paraplegia and SMA" (PMID:39502942).
- **Differential diagnosis:** SMA with lower-extremity predominance (DYNC1H1/BICD2 — distinguished by upper-limb involvement in >half of VWA1 cases), dHMN type I, hereditary spastic paraplegia (when UMN signs present), collagen VI-related dystrophies (distinguished by normal collagen VI staining and neurogenic electrophysiology), juvenile ALS (tongue fasciculations; distinguished by decades-long benign course), Duchenne/FSHD (CK elevation).
- **Newborn/carrier screening:** none established.

---

## 11. Outcome / Prognosis

- **Survival:** no reported disease-related mortality; lifespan apparently normal (no cardiac or respiratory involvement).
- **Ambulation:** preserved in nearly all — 3/17 lost independent walking over median 36.5-year duration (PMID:33559681); 0/20 in the 2024 cohort.
- **Morbidity:** lifelong motor disability from early childhood — foot deformity, contractures, falls (one-third), gait limitation; cognition spared.
- **Prognostic factors:** severe bilateral equinovarus predicts delayed walking; isolated worsening after the fifth decade in some. **Prognostic biomarkers:** the 2024 plasma proteomic panel (antioxidative-process proteins) is a first biomarker candidate set, not yet validated (PMID:38652110).

---

## 12. Treatment

**No disease-modifying therapy exists, and no interventional trial has been published.** (Curator-verified searches: PubMed VWA1[Title/Abstract] and VWA1 AND therapy/treatment/trial returned no therapeutic studies in this disease; ClinicalTrials.gov shows no VWA1 trial.) Management is supportive, extrapolated from standard neuromuscular care:

| Intervention | NCIT term | Target |
|---|---|---|
| Physical therapy / contracture management | NCIT:C15302 (Physical Therapy) | Achilles contractures, gait |
| Ankle-foot orthoses | NCIT:C15315 (Rehabilitation) + device qualifier NCIT:C86054 | Foot drop |
| Orthopedic surgery | NCIT:C16186 (Orthopedic Surgical Procedure) | Equinovarus, pes cavus, contractures |
| Genetic counseling + targeted founder-allele testing | NCIT:C15240 (Genetic Counseling) | Family risk; diagnostic yield |

No pharmacotherapy, gene therapy, ASO, or cell therapy program exists for this disease. The theoretical appeal of the target (a secreted ECM protein; a single founder allele accounting for most disease chromosomes) has been noted but not advanced to preclinical therapeutics.

---

## 13. Prevention

- **Primary prevention:** none possible beyond reproductive genetic counseling. Given the ~1/441 carrier frequency of the founder allele in Western Europeans, carrier screening of partners of known carriers is rational; no population program exists.
- **Secondary prevention:** early molecular diagnosis (the main modifiable burden is the diagnostic odyssey — patients were tested for DMD, FSHD, SMA and dystonia panels before VWA1 was found; PMID:39502942). Cascade testing in families; prenatal/preimplantation diagnosis feasible once familial variants are known.
- **Tertiary prevention:** contracture and deformity management to preserve gait.

---

## 14. Other Species / Natural Disease

No naturally occurring VWA1-deficiency disease is reported in any non-human species (no OMIA entry identified). Orthologs are conserved across vertebrates — mouse *Vwa1* (NCBI Gene 246228) and zebrafish *vwa1* (64.7% protein similarity to human across a 408-aa overlap; PMID:33559681). No zoonotic dimension. Comparative point of note: the mouse knockout shows delayed nociceptive response and impaired fine motor coordination without weakness — a partial, species-divergent phenocopy.

---

## 15. Model Organisms

**Mouse — Vwa1/WARP global knockout** (Allen et al. 2009, PMID:19279005; predates the human disease and made VWA1 a candidate gene):
- Healthy, viable, fertile; but "although WARP is not essential for basement membrane formation or musculoskeletal development, it has critical roles in the structure and function of peripheral nerves" (PMID:19279005).
- Recapitulates the **nerve** lesion (collagen VI matrix "severely reduced and mislocalized in peripheral nerves"; Schwann cell basement membrane fusion) but **fails to recapitulate muscle pathology** ("skeletal muscle showed no detectable abnormalities") — a key constraint on the primary-myopathy hypothesis.
- Limitations: nociceptive phenotype has no clear human counterpart; no progressive weakness.

**Zebrafish — vwa1 CRISPR crispants and morpholino morphants** (PMID:33559681, Tg(olig2:dsRed) background):
- "Vwa1 Crispants (n = 29) and morphants (n = 26) showed significantly shortened axons compared to controls"; "significantly reduced synaptic formation in the skeletal muscles" (α-bungarotoxin); reduced locomotion. "These results established that vwa1 is required for the proper organization of skeletal muscles and in the formation of neuromuscular junctions."
- Limitations: developmental readouts (48–96 hpf) vs. a decades-long human disease; a jaw-cartilage phenotype not seen in patients; morpholino off-target risk (mitigated by CRISPR concordance).

**Human cellular models:** patient dermal fibroblasts (NMD/protein-absence demonstration). No iPSC-motor-neuron, organoid, or conditional mouse model published — a conditional muscle-restricted knockout is the experiment both camps agree would settle the primary-vs-secondary myopathy controversy.

---

## Key Primary References

1. Pagnamenta AT, et al. *An ancestral 10-bp repeat expansion in VWA1 causes recessive hereditary motor neuropathy.* Brain. 2021. **PMID:33559681** — [academic.oup.com/brain](https://academic.oup.com/brain/article/144/2/362/6158337)
2. Deschauer M, et al. *Bi-allelic truncating mutations in VWA1 cause neuromyopathy.* Brain. 2021. **PMID:33459760**
3. Record CJ, et al. *Autosomal recessive VWA1-related disorder: comprehensive analysis of phenotypic variability and genetic mutations.* Brain Commun. 2024. **PMID:39502942** — [PMC11535570](https://pmc.ncbi.nlm.nih.gov/articles/PMC11535570/)
4. Athamneh M, et al. *Proteomic studies in VWA1-related neuromyopathy…* J Cell Mol Med. 2024. **PMID:38652110** — [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/jcmm.18122)
5. *Upper motor neuron signs and early onset gait abnormalities in young children with bi-allelic VWA1 variants.* 2022. **PMID:35975723**
6. *A Distinctive MRI Pattern Resembling Type VI Collagen Myopathy…* 2025. **PMID:41331965** — [PubMed](https://pubmed.ncbi.nlm.nih.gov/41331965/)
7. *Whole-Body Muscle MRI in Non-5q Spinal Muscular Atrophy.* 2026. **PMID:42662709**
8. Allen JM, et al. *Mice lacking the extracellular matrix protein WARP…* J Biol Chem. 2009. **PMID:19279005**
9. Allen JM, et al. *WARP is a novel component of a distinct subset of basement membranes.* 2008. **PMID:18314316**
10. Fitzgerald J. *WARP: A Unique Extracellular Matrix Component…* 2019. **PMID:30768857**
11. *Hereditary motor neuropathies* (review). 2022. **PMID:35942667**
12. Sharma S, et al. *HMNR7 as a Neuromyopathy — A Novel VWA1 Variant With Minipolymyoclonus, Fasciculations, and Scapular Winging.* Muscle Nerve. 2026. **PMID:41416782** — [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/mus.70102)

Sources: [OMIM #619216](https://omim.org/entry/619216) · [OMIM *611901](https://omim.org/entry/611901) · [GeneCards VWA1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=VWA1) · [Brain Communications 2024 cohort](https://academic.oup.com/braincomms/article/6/6/fcae377/7845966) · [Genetic alterations of VWA1 (Brain commentary)](https://academic.oup.com/brain/article/144/2/362/6158337?login=false) · [J Cell Mol Med proteomics](https://onlinelibrary.wiley.com/doi/10.1111/jcmm.18122) · [PMID:41331965](https://pubmed.ncbi.nlm.nih.gov/41331965/) · [Muscle & Nerve 2026 case](https://onlinelibrary.wiley.com/doi/10.1002/mus.70102) · [MalaCards HMNR7](https://www.malacards.org/card/neuronopathy_distal_hereditary_motor_autosomal_recessive_7)

*Note on provenance: all direct quotes above were verified against cached source abstracts/records in this repository's snippet-validated knowledge base entry for MONDO:0030977; identifiers and 2026 literature were confirmed by web search on 2026-09-19.*

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 30 |
| Quoted claims found in source | 29 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 15 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:39502942`: "early-onset foot deformities, contractures, and gait abnormalities have been consistently reported in nearly all individuals … suggesting an early or even infantile disease onset rather than adult onset"
  - closest text in source: "Nonetheless, early-onset foot deformities, contractures, and gait abnormalities have been consistently reported in nearly all individuals with VWA1-related disorder, suggesting an early or even infantile disease onset rather than adult onset"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 35 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030977` (3 mentions) - the report calls it "MONDO"; MONDO calls it **neuronopathy, distal hereditary motor, autosomal recessive 7**
- `GO:0000184` (1 mention) - the report calls it "NMD"; GO calls it **nuclear-transcribed mRNA catabolic process, nonsense-mediated decay**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0009027` (1 mention) - the report calls it "Foot dorsiflexor weakness (foot drop)"; HP calls it **Foot dorsiflexor weakness**
- `HP:0009053` (1 mention) - the report calls it "Distal lower limb weakness"; HP calls it **Distal lower limb muscle weakness**
- `HP:0008994` (1 mention) - the report calls it "Proximal lower limb weakness"; HP calls it **Proximal lower limb muscle weakness**
- `HP:0003236` (1 mention) - the report calls it "Elevated CK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names
- `HP:0033685` (1 mention) - the report calls it "Fiber type grouping (biopsy)"; HP calls it **Fiber type grouping**
- `GO:0005201` (1 mention) - the report calls it "ECM structural constituent"; GO calls it **extracellular matrix structural constituent**
- `GO:0007528` (1 mention) - the report calls it "NMJ development"; GO calls it **neuromuscular junction development**
- `GO:0030198` (1 mention) - the report calls it "ECM organization"; GO calls it **extracellular matrix organization**
- `CL:0000100` (2 mentions) - the report calls it "motor neuron", "Cellular:** motor neurons"; CL calls it **motor neuron**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000100` - called "motor neuron", "Cellular:** motor neurons"