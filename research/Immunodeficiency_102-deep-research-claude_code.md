---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-19T01:49:09.555338'
end_time: '2026-09-19T01:53:23.109013'
duration_seconds: 253.55
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Immunodeficiency 102
  mondo_id: MONDO:0024781
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 4
  num_turns: 14
  total_cost_usd: 4.940025000000001
  session_id: 03905c22-b389-4ddc-b3cb-b216fca0a5ff
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 5
citation_count: 10
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 16
  on_topic: 14
  validator_version: 0.2.1
term_validation:
  total_terms: 56
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 35
  labels_matching: 26
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15329
    reported_labels:
    - Splenectomy
    ontology_label: Surgical Procedure
  labels_variant: 8
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 102
- **MONDO ID:** MONDO:0024781 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 102** covering all of the
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

I'll research Immunodeficiency 102 (SASH3-related). Since this repository already has a curated entry on this branch, I'll draw on the local KB and cached references, plus web sources. Let me load the web tools and inspect local material in parallel.

The local KB entry gives me a strong base. Now let me verify identifiers (OMIM, Orphanet) and check for recent literature via the web.

Orphanet blocked the direct fetch. Let me gather a few remaining identifier and gene facts.

# Research Report: Immunodeficiency 102 (IMD102; SASH3 Deficiency)

**MONDO:0024781 · OMIM #301082 · ORPHA:653751 · Gene: SASH3 (Xq26.1)**
Report date: 2026-09-19. Note on the evidence base: this disease was first described in 2021 and the entire published human literature comprises roughly a dozen patients across one four-patient index cohort and a handful of single case reports. Nearly every claim below therefore rests on small-n human data or on the *Sly1*-deficient mouse, and the report flags which is which throughout.

---

## 1. Disease Information

**Overview.** Immunodeficiency 102 (IMD102) is an X-linked recessive **combined immunodeficiency with immune dysregulation** caused by hemizygous loss-of-function variants in *SASH3* (SAM and SH3 domain containing 3, also called *SLY1*, "SH3 protein expressed in lymphocytes 1"), a lymphocyte-restricted signalling adaptor. Affected males present in early childhood with recurrent sinopulmonary, cutaneous and mucosal infections, and most develop refractory autoimmune cytopenias (autoimmune hemolytic anemia, immune thrombocytopenia). The defining laboratory picture is CD4+ T-cell lymphopenia with impaired T-cell proliferation, B- and NK-cell lymphopenia, loss of class-switched memory B cells, low IgM, and — unexpectedly for a lymphocyte-restricted gene — neutropenia.

The index description is Delmonte et al., *Blood* 2021 (PMID:33876203): *"Here, we identified 3 novel SASH3 deleterious variants in 4 unrelated male patients with a history of combined immunodeficiency and immune dysregulation that manifested as recurrent sinopulmonary, cutaneous, and mucosal infections and refractory autoimmune cytopenias."* The authors concluded: *"These findings define a new type of X-linked combined immunodeficiency in humans that recapitulates many of the abnormalities reported in mice with Sly1−/− and Sly1Δ/Δ mutations."*

**Identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0024781 (immunodeficiency 102) |
| OMIM (phenotype) | #301082 (IMMUNODEFICIENCY 102; IMD102) — note 301083 is a different disease (CNSHA9) |
| OMIM (gene) | *300441 (SASH3) |
| Orphanet | ORPHA:653751 — "X-linked combined immunodeficiency due to SASH3 deficiency" |
| ICD-10 | D81.8 (other combined immunodeficiencies) |
| HGNC | hgnc:15975 (SASH3) |
| UniProt | O75995 (SASH3_HUMAN, 380 aa, ~41.6 kDa) |
| IUIS 2022 | Table 1, "Immunodeficiencies affecting cellular and humoral immunity" (PMID:35748970) |

**Synonyms:** IMD102; SASH3 deficiency; SLY1 deficiency; X-linked combined immunodeficiency due to SASH3 deficiency; X-linked CID due to SASH3 deficiency.

**Data provenance:** all human information is aggregated from published individual patients (index cohort of 4, plus single case reports) — there is no registry, EHR cohort, or natural-history study.

## 2. Etiology

**Causal factor (single, genetic):** hemizygous germline loss-of-function variants in *SASH3* on Xq26.1. Four variant types reported worldwide as of 2025 (tabulated in PMID:40947476): three nonsense — c.505C>T p.(Gln169\*), c.733C>T p.(Arg245\*), c.862C>T p.(Arg288\*) — and one missense, c.1039C>T p.(Arg347Cys). Arg347 is conserved from *Xenopus* to human and sits in a putative protein-kinase-A-binding motif adjacent to the Ser349 phosphorylation site, which is the proposed reason a single missense substitution behaves like a null (structural modelling; COMPUTATIONAL evidence).

**Risk factors:** male sex (all reported patients are hemizygous males); maternal carrier status — *"This pathogenic variant was inherited from the mother, who carries the same variant in the heterozygous state"* (PMID:40947476). No environmental risk, protective factors, or gene–environment interactions are documented; the disease is fully Mendelian. **Penetrance is incomplete or expressivity highly variable:** one hemizygous brother carrying p.Arg288\* *"shares immunophenotypic features but is currently clinical asymptomatic, indicating heterogeneity of SASH3 deficiency"* (PMID:37646304).

## 3. Phenotypes

All frequencies are qualitative — the denominator is ~12 reported patients. Onset of infections is early childhood; the oldest reported patient reached age 56 (index cohort ages 19–56, PMID:33876203).

| Phenotype | HPO | Type / notes | Frequency |
|---|---|---|---|
| Combined immunodeficiency | HP:0005387 | Defining; IUIS Table 1 entity | All symptomatic patients |
| Recurrent sinopulmonary infections | HP:0005425 | Presenting complaint | Very frequent |
| Recurrent skin infections | HP:0001581 | Cellulitis requiring admission reported | Frequent |
| Autoimmune hemolytic anemia | HP:0001890 | Refractory; Evans syndrome presentation | Frequent |
| Autoimmune thrombocytopenia | HP:0001973 | Refractory; splenectomy in one case | Frequent |
| Severe varicella zoster infection | HP:0032170 | Single adult case, age 4 | One patient |
| Decreased total CD4+ T cell count | HP:5210418 | Most consistent lab abnormality | Near-universal |
| Decreased total T cell count | HP:0005403 | Both CD4+ and CD8+ affected | Frequent |
| Decreased antigen-specific T cell proliferation | HP:0031402 | Functional,

# Research Report: Immunodeficiency 102 (IMD102; SASH3 Deficiency)

**MONDO:0024781 · OMIM #301082 · ORPHA:653751 · Gene: SASH3 (Xq26.1)**
Report date: 2026-09-19. Note on the evidence base: this disease was first described in 2021 and the entire published human literature comprises roughly a dozen patients across one four-patient index cohort and a handful of single case reports. Nearly every claim below therefore rests on small-n human data or on the *Sly1*-deficient mouse, and the report flags which is which throughout.

---

## 1. Disease Information

**Overview.** Immunodeficiency 102 (IMD102) is an X-linked recessive **combined immunodeficiency with immune dysregulation** caused by hemizygous loss-of-function variants in *SASH3* (SAM and SH3 domain containing 3, also called *SLY1*, "SH3 protein expressed in lymphocytes 1"), a lymphocyte-restricted signalling adaptor. Affected males present in early childhood with recurrent sinopulmonary, cutaneous and mucosal infections, and most develop refractory autoimmune cytopenias (autoimmune hemolytic anemia, immune thrombocytopenia). The defining laboratory picture is CD4+ T-cell lymphopenia with impaired T-cell proliferation, B- and NK-cell lymphopenia, loss of class-switched memory B cells, low IgM, and — unexpectedly for a lymphocyte-restricted gene — neutropenia.

The index description is Delmonte et al., *Blood* 2021 (PMID:33876203): *"Here, we identified 3 novel SASH3 deleterious variants in 4 unrelated male patients with a history of combined immunodeficiency and immune dysregulation that manifested as recurrent sinopulmonary, cutaneous, and mucosal infections and refractory autoimmune cytopenias."* The authors concluded: *"These findings define a new type of X-linked combined immunodeficiency in humans that recapitulates many of the abnormalities reported in mice with Sly1−/− and Sly1Δ/Δ mutations."*

**Identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0024781 (immunodeficiency 102) |
| OMIM (phenotype) | #301082 (IMMUNODEFICIENCY 102; IMD102) — note 301083 is a different disease (CNSHA9) |
| OMIM (gene) | *300441 (SASH3) |
| Orphanet | ORPHA:653751 — "X-linked combined immunodeficiency due to SASH3 deficiency" |
| ICD-10 | D81.8 (other combined immunodeficiencies) |
| HGNC | hgnc:15975 (SASH3) |
| UniProt | O75995 (SASH3_HUMAN, 380 aa, ~41.6 kDa) |
| IUIS 2022 | Table 1, "Immunodeficiencies affecting cellular and humoral immunity" (PMID:35748970) |

**Synonyms:** IMD102; SASH3 deficiency; SLY1 deficiency; X-linked combined immunodeficiency due to SASH3 deficiency; X-linked CID due to SASH3 deficiency.

**Data provenance:** all human information is aggregated from published individual patients (index cohort of 4, plus single case reports) — there is no registry, EHR cohort, or natural-history study.

## 2. Etiology

**Causal factor (single, genetic):** hemizygous germline loss-of-function variants in *SASH3* on Xq26.1. Four variant types reported worldwide as of 2025 (tabulated in PMID:40947476): three nonsense — c.505C>T p.(Gln169\*), c.733C>T p.(Arg245\*), c.862C>T p.(Arg288\*) — and one missense, c.1039C>T p.(Arg347Cys). Arg347 is conserved from *Xenopus* to human and sits in a putative protein-kinase-A-binding motif adjacent to the Ser349 phosphorylation site, which is the proposed reason a single missense substitution behaves like a null (structural modelling; COMPUTATIONAL evidence).

**Risk factors:** male sex (all reported patients are hemizygous males); maternal carrier status — *"This pathogenic variant was inherited from the mother, who carries the same variant in the heterozygous state"* (PMID:40947476). No environmental risk, protective factors, or gene–environment interactions are documented; the disease is fully Mendelian. **Penetrance is incomplete or expressivity highly variable:** one hemizygous brother carrying p.Arg288\* *"shares immunophenotypic features but is currently clinical asymptomatic, indicating heterogeneity of SASH3 deficiency"* (PMID:37646304).

## 3. Phenotypes

All frequencies are qualitative — the denominator is ~12 reported patients. Onset of infections is early childhood; the oldest reported patient reached age 56 (index cohort ages 19–56, PMID:33876203).

| Phenotype | HPO | Type / notes | Frequency |
|---|---|---|---|
| Combined immunodeficiency | HP:0005387 | Defining; IUIS Table 1 entity | All symptomatic patients |
| Recurrent sinopulmonary infections | HP:0005425 | Presenting complaint | Very frequent |
| Recurrent skin infections | HP:0001581 | Cellulitis requiring admission reported | Frequent |
| Autoimmune hemolytic anemia | HP:0001890 | Refractory; Evans syndrome presentation | Frequent |
| Autoimmune thrombocytopenia | HP:0001973 | Refractory; splenectomy in one case | Frequent |
| Severe varicella zoster infection | HP:0032170 | Single adult case, age 4 | One patient |
| Decreased total CD4+ T cell count | HP:5210418 | Most consistent lab abnormality | Near-universal |
| Decreased total T cell count | HP:0005403 | Both CD4+ and CD8+ affected | Frequent |
| Decreased antigen-specific T cell proliferation | HP:0031402 | Functional,  mitogen/TCR stimulation | Consistent |
| Decreased total B cell count | HP:0010976 | Not universal — one patient normal | Frequent |
| Decreased class-switched memory B cell proportion | HP:0030388 | More reliable than B-cell count | Consistent |
| Decreased circulating total IgM | HP:0002850 | Sometimes isolated (normal IgG/IgA) | Frequent |
| Reduced total natural killer cell count | HP:0040218 | Not universal | Frequent |
| Decreased total neutrophil count | HP:0001875 | **Mechanistically unexplained** (see §6) | Frequent |

Supporting quotes: *"Patients exhibited CD4+ T-cell lymphopenia, decreased T-cell proliferation, cell cycle progression, and increased T-cell apoptosis in response to mitogens"* and *"These patients also manifested neutropenia and B-cell and natural killer (NK)-cell lymphopenia"* (PMID:33876203). A 2025 case quantified the memory defect precisely: *"a considerable reduction in IgM memory B cells (CD19+CD27+IgD+) at 1.6% and switched memory B cells (CD19+CD27+IgD−) at 2.4%"* despite normal total B cells and IgG (PMID:40947476).

**Severity and course:** variable and unpredictable from genotype. The spectrum runs from asymptomatic hemizygous carrier → adult misdiagnosed as CVID for decades (*"Our patient displays a milder phenotype than has been reported previously… thus expanding the clinical spectrum"*, PMID:35464398) → refractory Evans syndrome requiring splenectomy (PMID:37646304). Infections are recurrent/episodic; the autoimmune component is chronic and refractory. **Quality-of-life data do not exist** for this disease — no EQ-5D, SF-36, or PROMIS study has been published.

**Explicitly not curated as phenotypes:** one patient had osteogenesis imperfecta, metaphyseal dysplasia, intellectual disability, hearing loss, cleft lip/palate and renal agenesis alongside the immune findings, with no pathogenic variant found in any OI or ID gene — but the reporting authors declined to attribute these to *SASH3*: *"further studies are needed to determine the association between the SASH3 variant and the skeletal or neurological manifestations"* (PMID:40947476). No other patient has had them.

## 4. Genetic / Molecular Information

**Gene.** *SASH3* / *SLY1*, HGNC:15975, Xq26.1, OMIM \*300441. Encodes a 380-aa adaptor with a bipartite nuclear localisation signal, an SH3 domain and a sterile alpha motif (SAM), and **no catalytic activity**. Expression is lymphocyte-restricted. Delmonte et al.: *"SASH3… is a putative adaptor protein that is postulated to play an important role in the organization of signaling complexes and propagation of signal transduction cascades in lymphocytes"* (PMID:33876203).

**Gene family caution.** *SASH3* is one of three SLy/SASH family members: *"The initial characterization of the first member SLy1/SASH3… in 2001 was rapidly followed by identification of SLy2/HACS1… and SASH1/SLy3"* (PMID:33710696). *SASH1* is ubiquitously expressed and curated as a tumour suppressor — do not conflate.

**Variants.** All germline, hemizygous, loss-of-function. Three nonsense + one missense (above). ACMG classification: pathogenic/likely pathogenic in ClinVar for the reported nonsense alleles. Population frequency: absent or vanishingly rare in gnomAD for the reported alleles (consistent with an ultra-rare X-linked disorder); no founder allele has been described and all four reported variants arose in unrelated families.

**Functional consequence.** Loss of function, confirmed by rescue: *"Lentivirus-mediated transfer of the SASH3 complementary DNA-corrected protein expression, in vitro proliferation, and signaling in SASH3-deficient Jurkat and patient-derived T cells"* (PMID:33876203) — this rescue experiment is what makes the gene–phenotype link causal rather than correlative.

**Modifier genes, epigenetics, chromosomal abnormalities:** none reported. No methylation, chromatin, or structural-variant data exist for this disease.

## 5. Environmental Information

Not applicable as a cause. No environmental, lifestyle, occupational, or toxic contributor is described. Infectious agents are **consequences**, not causes: bacterial sinopulmonary pathogens, cutaneous bacteria (cellulitis), rotavirus gastroenteritis, influenza A, and varicella zoster virus (VZV, NCBITaxon:10335) have all been reported as complications. The VZV episode is mechanistically informative: *"Two separate, severe viral infections drew our attention and pointed to an underlying T cell defect: severe varicella zoster virus (VZV) infection at the age of 4 years and bilateral pneumonia due type A influenza infection at the age of 38"* (PMID:35464398).

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Hemizygous loss-of-function variant in *SASH3*** (nonsense, or the Arg347Cys missense in a conserved PKA-binding motif) → **absence or non-function of the SASH3 adaptor protein in lymphocytes**. Because expression is lymphocyte-restricted, consequences are confined to the lymphoid compartment.
2. Loss of the scaffold → **failure of antigen-receptor signal propagation**. The adaptor's SH3 and SAM domains normally nucleate signalling complexes downstream of the TCR and BCR; without them, engaged receptors do not couple to their effectors. *Demonstrated*, not inferred: lentiviral SASH3 restoration rescues signalling in both Jurkat cells and patient T cells (PMID:33876203). In mouse, the molecular event lost is Ser27 phosphorylation and nucleus→cytoplasm shuttling on receptor engagement (PMID:16227612); the human protein has not been localised this way.
3. The chain then **branches into four arms**:

   **3a. Thymic arm** — signalling failure → **thymocyte survival failure at the CD4−CD8− double-negative → CD4+CD8+ double-positive transition** → **reduced thymic output** → CD4+ and total T-cell lymphopenia → severe viral infection (VZV) and the cellular half of the combined defect. *Human basis is indirect*: *"In vitro T-cell differentiation of CD34+ cells and molecular signatures of rearrangements at the T-cell receptor α (TRA) locus were indicative of impaired thymocyte survival"* (PMID:33876203) — an in vitro differentiation assay plus a rearrangement signature, not thymic tissue. The staging comes from mouse: *"SLY1 was identified as a novel anti-apoptotic protein required for developmental progression of T cell precursors to the CD4+CD8+ double-positive stage by protecting from premature programmed cell death initiation in developing CD4−CD8− double-negative thymocytes"* (PMID:19604361), with the proximate cause being failed mTOR activation — *"SLY1-deficient thymocytes were compromised in inducing nutrient receptor expression and ribosomal protein S6 phosphorylation, indicating a defect in mTOR complex activation."* A later knockout study added reduced DN3 proliferation as a second contributor (PMID:36401605).

   **3b. Peripheral T-cell arm** — signalling failure → **defective proliferation, impaired cell-cycle progression and increased activation-induced apoptosis** in mature peripheral T cells (measured directly in patient cells, PMID:33876203; independently confirmed in PMID:35464398 and PMID:37646304). *Mouse-only mechanism*: dysregulated Foxo1 shuttling after TCR signalling raises cell-cycle inhibitor expression — *"The increased susceptibility of SLy1 knock-out (KO) mice was caused by reduced proliferation of differentiated T cells"* (PMID:26306874). **Whether the human proliferative defect runs through Foxo1 is untested.**

   **3c. Humoral arm** — BCR signalling failure (cell-intrinsic) *plus* loss of cognate T-cell help from arm 3b → **impaired germinal centre reaction** → loss of class-switched and IgM memory B cells, low IgM, poor polysaccharide vaccine responses → recurrent sinopulmonary and cutaneous infection. The only direct human histology: *"Immunohistochemistry performed after clinically indicated splenectomy revealed severe hypoplasia/absence of germinal centres"* (PMID:37646304). Mouse counterpart is adjacent but not identical — a marginal-zone rather than germinal-centre lesion: *"Sly1(d/d) mice exhibit reduced lymphoid organ sizes, diminished marginal zone B-cell numbers, and severely impaired antibody responses against T-dependent and -independent antigens"* (PMID:16227612), driven by reduced Notch activity, with *"the production of antigen-specific IgM antibodies following immunization with pneumococcal polysaccharides was severely impaired"* (PMID:18950867).

   **3d. NK arm — a mechanistically separate branch.** NK cells are reduced in most patients, but the route is not established in humans and **may not share a mechanism with arms 3a–3c**. In mouse, SLy1 in NK cells is not a signalling scaffold at all: *"Unlike the case for T or B lymphocytes, where SLy1 shuttles between the cytoplasm and nucleus to facilitate signal transduction, in NK cells SLy1 functions as a ribosomal protein and is located solely in the cytoplasm"* (PMID:28123874), and *"In its absence, ribosomal instability results in p53-mediated NK cell senescence and decreased clearance of malignancies."* A 2026 follow-up confirms the functional consequence: *"SLy1 is indispensable for adequate numbers of viable, activatable NK cells with an intact cytolytic capacity, and that those phenotypic alterations are p53-mediated"* (PMID:42327758).

4. **Convergent branch: breakdown of peripheral tolerance** → refractory autoimmune hemolytic anemia and immune thrombocytopenia (Evans syndrome). *Association reported, causal steps unknown*: *"The autoimmune phenotype was associated with an increased CD21low T-bet+ CD11c+ subset along with decreased regulatory T cells, impaired T-cell proliferation and T-cell exhaustion"* (PMID:37646304). Both a thymic selection defect and the Treg deficit are plausible routes; neither has been tested against the other in patients.

5. **Unexplained: neutropenia.** This does **not** follow from the chain above and should not be forced into it. *SASH3* expression is lymphocyte-restricted, so a neutrophil-intrinsic effect has no obvious basis; autoimmune destruction — the usual alternative in an immune-dysregulation disorder — has not been demonstrated in any reported patient; and no *Sly1* mouse study reports neutropenia. Yet the phenotype is prominent enough that *SASH3* surfaces in congenital-neutropenia sequencing cohorts: *"Half of these cases involved genes traditionally associated with hereditary immunodeficiencies (GINS4, CARD11, ADA2, GINS1, LCP1, SASH3, and WAS)"* (PMID:40510848). **This is an open knowledge gap, and the honest position is that the mechanism is unknown.**

### Ontology annotations for the mechanism

| Concept | Term |
|---|---|
| Signalling adaptor activity (lost) | GO:0035591 |
| T cell receptor signaling pathway (↓) | GO:0050852 |
| B cell receptor signaling pathway (↓) | GO:0050853 |
| Intracellular signal transduction (↓) | GO:0035556 |
| T cell differentiation in thymus (↓) | GO:0033077 |
| Thymocyte apoptotic process (↑) | GO:0070242 |
| T cell proliferation (↓) | GO:0042098 |
| Cell cycle (↓) | GO:0007049 |
| Positive regulation of apoptotic process (↑) | GO:0043065 |
| Germinal center formation (↓) | GO:0002467 |
| Isotype switching (↓) | GO:0045190 |
| Immunoglobulin production (↓) | GO:0002377 |
| NK cell mediated cytotoxicity (↓) | GO:0042267 |
| Regulation of immune response (dysregulated) | GO:0050776 |

Cell types: T cell CL:0000084; CD4-positive αβ T cell CL:0000624; B cell CL:0000236; class-switched memory B cell CL:0000972; NK cell CL:0000623; thymocyte CL:0000893; double-negative thymocyte CL:0002489; regulatory T cell CL:0000815.

**Molecular profiling.** No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial dataset has been published for IMD102 patients. The available functional-genomics analogue is the *Sly1* mouse ribosome work (PMID:28123874). This is a genuine gap, not an omission from this report.

## 7. Anatomical Structures Affected

- **Primary organs/systems:** immune system; thymus (UBERON:0002370) — site of the developmental block; spleen (UBERON:0002106) — germinal centre hypoplasia documented histologically; bone marrow (UBERON:0002371) — neutropenia, mechanism unknown; peripheral blood/lymphoid tissue generally.
- **Secondary involvement:** respiratory tract (recurrent sinopulmonary infection — lung UBERON:0002048, nasal/paranasal sinuses UBERON:0001825), skin (UBERON:0002097), mucosae, and hematologic system (immune-mediated destruction of erythrocytes and platelets).
- **Cell populations:** as listed in §6. Note the dissociation — the target is a *cell lineage set*, not an anatomical site; damage to spleen and thymus is developmental/architectural rather than destructive.
- **Subcellular:** cytoplasm (GO:0005737) and nucleus (GO:0005634) — the mouse protein shuttles between them on receptor engagement; in NK cells (mouse) it is cytoplasmic and ribosome-associated (GO:0022626, cytosolic ribosome).
- **Lateralization:** not applicable (systemic).

## 8. Temporal Development

**Onset:** early childhood for infections in most patients (OMIM describes onset of recurrent infections in early childhood). One case was ascertained in adulthood after decades under a CVID label; one hemizygous carrier remains asymptomatic into adulthood. Onset pattern is **insidious and recurrent** rather than acute.

**Course:** chronic and lifelong. Infections are episodic; autoimmune cytopenias are chronic and **refractory** — the index cohort's use of that word is itself informative, since a cytopenia is called refractory only after therapy has failed to hold. No staging system exists. Progression rate is not characterized: there is no natural-history study, no longitudinal cohort, and no registry. The oldest reported patient was 56 years old at description (PMID:33876203), so survival into the sixth decade is documented.

**Critical periods / remission:** no data. Spontaneous remission has not been reported; treatment-induced remission of cytopenias is inconsistent (hence "refractory"), and one patient required splenectomy.

## 9. Inheritance and Population

**Inheritance:** X-linked recessive (HP:0001419). *"The SASH3 gene is located on the X-chromosome"* (PMID:33876203); all reported patients are hemizygous males. The one family in which parental origin was established showed maternal heterozygous carriage (PMID:40947476). Heterozygous female carriers have not been reported as affected, though the number of carriers examined is very small and skewed X-inactivation has not been studied.

**Penetrance / expressivity:** **incomplete penetrance or extremely variable expressivity is documented** — the asymptomatic hemizygous brother sharing p.Arg288\* with an Evans-syndrome proband (PMID:37646304) is the key observation. No genetic anticipation (not a repeat disorder); no germline mosaicism reported; no founder effect; no consanguinity role (X-linked); no carrier-frequency estimate exists.

**Epidemiology:** Orphanet classifies prevalence as **<1 / 1,000,000** (ultra-rare). No incidence figure exists and none should be asserted. For scale on the denominator, a dedicated sequencing program for suspected inborn errors of immunity covering 1,505 individuals from 1,000 families returned *SASH3* in two: *"Specifically, these included individuals with pathogenic variants in GIMAP5 (n = 2) and SASH3 (n = 2)"* (PMID:35753512) — a yield within a heavily enriched referral population, **not** a population prevalence. The 2022 IUIS classification recognised five reported patients (PMID:35748970); counts in the literature overlap and no authoritative worldwide total has been published.

**Demographics:** sex ratio effectively 100% male among affected individuals (X-linked recessive). No ethnic or geographic clustering has been reported; the four index patients were unrelated and no variant is population-specific.

## 10. Diagnostics

**Laboratory.** The diagnostic core is lymphocyte immunophenotyping plus functional testing:
- Full blood count with differential — cytopenias across lineages including neutropenia
- Lymphocyte subsets by flow cytometry — CD4+ and total T-cell lymphopenia, B-cell lymphopenia, NK lymphopenia, reduced naïve CD4+/CD8+ with elevated TEMRA, reduced pre-switch and switched memory B cells (CD19+CD27+IgD+ and CD19+CD27+IgD−)
- Serum immunoglobulins — hypogammaglobulinemia, frequently with disproportionately low IgM
- T-cell proliferation assays to mitogens/anti-CD3 — reduced, with impaired cell-cycle progression and increased apoptosis
- Specific antibody responses, including pneumococcal polysaccharide — suboptimal
- TREC/TRA rearrangement analysis — the TRA rearrangement signature is what reports thymocyte survival (PMID:33876203)

Relevant LOINC-coded measurements: CD4 count, CD19 count, CD56/CD16 NK count, absolute neutrophil count, quantitative IgG/IgA/IgM.

**Genetic testing** is required for diagnosis; the phenotype is not specific. Reported routes: NGS custom-targeted immunodeficiency gene panel (*"Genetic testing using an NGS-based custom-targeted gene panel revealed a novel hemizygous loss-of-function variant in the SASH3 gene (c.505C>T/p.Gln169\*)"*, PMID:35464398), clinical exome sequencing (PMID:35753512), and whole-exome/whole-genome sequencing in congenital-neutropenia workups (PMID:40510848). **Practical recommendation:** *SASH3* should be on any IEI panel used to evaluate combined immunodeficiency, CVID-like presentations, Evans syndrome, or unexplained congenital neutropenia in a male. Karyotype, CMA, FISH, mtDNA and repeat-expansion testing have no role. Functional confirmation by lentiviral rescue of patient T cells exists as a research assay (PMID:33876203) but is not a clinical test.

**Histopathology:** splenic immunohistochemistry showing germinal centre hypoplasia/absence has been documented once, after clinically indicated splenectomy (PMID:37646304) — informative but not a diagnostic route.

**Differential diagnosis.** This is the clinically important point: **IMD102 is systematically misdiagnosed**. The published differentials are (a) **common variable immunodeficiency** — one patient carried that label for decades until two severe viral infections redirected attention to a T-cell defect (PMID:35464398); (b) **Evans syndrome / other IEI with immune dysregulation** — *"Increasing evidence suggests multilineage cytopenias (also known as Evans syndrome) may be caused by inborn errors of immunity (IEI) with immune dysregulation"* (PMID:37646304); (c) **severe congenital neutropenia** (PMID:40510848); (d) other X-linked CIDs, ALPS, CTLA4/LRBA haploinsufficiency. Distinguishing features favouring *SASH3*: male sex with X-linked pedigree, the combination of CD4 lymphopenia **plus** NK lymphopenia **plus** neutropenia, and refractory autoimmune cytopenias.

**Screening:** no newborn screening program detects this disease. TREC-based SCID newborn screening has not been reported to identify a *SASH3* patient and should not be assumed to — the T-cell defect is partial. Cascade family testing for the familial variant is appropriate once a proband is identified, and should be offered to at-risk male relatives (who may be asymptomatic) and female relatives (carrier status).

## 11. Outcome / Prognosis

**There are no survival, mortality, or quality-of-life data for this disease.** No 5- or 10-year survival figure, no life-expectancy estimate, no disease-specific mortality rate has been published. Survival into the sixth decade is documented (index cohort included a 56-year-old).

**Burden is best characterized as variable.** The reported range runs from an asymptomatic hemizygous brother, through an adult managed for decades as CVID with two severe viral episodes, to refractory autoimmune cytopenias requiring splenectomy. Recurrent sinopulmonary, cutaneous and mucosal infection is the common thread, and the **immune dysregulation rather than the infection burden drives the most severe presentations**. Two independent author groups state the heterogeneity explicitly (PMID:37646304; PMID:35464398).

**Complications:** recurrent bacterial and viral infection with hospitalisation; refractory cytopenias; splenectomy and its own lifelong infection risk. A theoretical malignancy concern arises from the mouse NK ribosomopathy work (*"decreased clearance of malignancies"*, PMID:28123874) and from the *Sly1* knockout tumour data (PMID:36401605), but **no malignancy has been reported in a SASH3-deficient patient** and this should not be presented to patients as an established risk.

**Prognostic factors and biomarkers:** none validated. Genotype does not predict phenotype — the same nonsense allele produced Evans syndrome in one brother and no disease in another.

## 12. Treatment

No published series reports treatment outcomes in SASH3 deficiency. Everything below is standard management of a combined immunodeficiency with this phenotype, with the disease-specific evidence stated honestly.

| Treatment | NCIT | Modality | Evidence status |
|---|---|---|---|
| Immunoglobulin replacement therapy | NCIT:C62710 | PROTEIN_REPLACEMENT | Indication only. The single mention in the SASH3 literature is a negative datum — *"Immunoglobulin replacement therapy was not prescribed at that time"* (PMID:35464398) — in a patient with low IgG and IgM. **No efficacy data exist.** |
| Antimicrobial prophylaxis | NCIT:C51993 | SMALL_MOLECULE | Indication only, from the documented infection burden. No SASH3-specific regimen or outcome published. |
| Immunosuppressive therapy for autoimmune cytopenias | NCIT:C15261 | — | The index cohort's cytopenias are described as **refractory**, which establishes both that immunosuppression is given and that it is often inadequate. **No agent is named in any publication**, so none should be recommended by name. |
| Splenectomy | NCIT:C15329 | SURGERY | Performed in one patient as second-line therapy for immune cytopenia (PMID:37646304). |
| Genetic counseling | NCIT:C15240 | BEHAVIORAL | Must cover carrier detection in female relatives **and** the documented possibility that a hemizygous male relative is clinically well. |

**Hematopoietic stem cell transplantation** is the obvious curative candidate for a combined immunodeficiency, and it is conspicuously absent from the literature: **no reported SASH3 patient has been described as transplanted**. The full texts of the human SASH3 papers were searched for "transplant", "HSCT" and "stem cell" with no hit relevant to these patients. Asserting HSCT as established therapy here would be inventing a treatment record — though it is a reasonable consideration for a severely affected patient in a specialist multidisciplinary setting, and gene therapy is mechanistically plausible given that lentiviral *SASH3* transfer rescues patient T cells in vitro (PMID:33876203).

**No pharmacogenomic, targeted, RNA-based, or immunotherapy data exist. No clinical trial (ClinicalTrials.gov or ICTRP) is registered for this disease.**

## 13. Prevention

Primary prevention of the genetic lesion is not possible. Preventive management is therefore **secondary and tertiary**:

- **Genetic counseling and cascade testing** in affected families — the maternal carrier state is documented and X-linked recurrence risk (50% of sons affected, 50% of daughters carriers) applies. Prenatal diagnosis and preimplantation genetic testing are technically available for a known familial variant; no published case describes their use here.
- **Early diagnosis** is the single highest-yield intervention, because the disease is systematically mislabelled as CVID, Evans syndrome, or congenital neutropenia. Including *SASH3* on IEI panels is the practical measure.
- **Infection prophylaxis and immunoglobulin replacement** as tertiary prevention (see §12).
- **Immunization:** routine inactivated vaccines are appropriate; **live vaccines require caution** in a combined immunodeficiency with documented severe VZV — though no SASH3-specific vaccine guidance has been published, and the general IEI principle is what applies.
- No behavioural, dietary, environmental, or public-health intervention is relevant.

## 14. Other Species / Natural Disease

**No naturally occurring animal disease** corresponding to SASH3 deficiency has been described. There is no OMIA entry, no companion-animal or wildlife counterpart, no breed predisposition (no VBO term applies), no zoonotic or cross-species transmission dimension.

**Orthologs:** mouse *Sash3*/*Sly1* (MGI:1921381, NCBI Gene 74131) — the deduced mouse and human proteins contain 381 and 380 amino acids respectively and share **94% sequence identity**, which is the basis for treating the mouse as an informative model. A zebrafish ortholog *sash3* exists (ZFIN ZDB-GENE-130411-1) but no disease model has been published in that species. The gene is lymphocyte-restricted across species, and the lymphoid function appears evolutionarily conserved.

## 15. Model Organisms

Two mouse models carry the entire mechanistic literature. Note the chronology: the *Sly1* mouse work begins in 2005, sixteen years before the human disease was described in 2021, and remains the larger literature.

**(a) *Sly1* knockout mouse (complete null, whole-body)** — MGI; principal reference PMID:19604361.
- *Recapitulates* thymocyte survival failure (fidelity MODERATE): thymic cellularity falls by roughly half with a block at the DN→DP transition driven by premature programmed cell death; readout is decreased ribosomal protein S6 phosphorylation and nutrient-receptor induction, read as failed mTOR activation.
- *Recapitulates* the peripheral T-cell proliferative defect (fidelity MODERATE), via Foxo1 (PMID:26306874).
- *Partially recapitulates* the NK phenotype (fidelity **LOW**): numbers, viability and cytotoxicity match the patients, but the molecular route does not transfer — in mouse the mechanism is ribosomal instability and p53-mediated senescence (PMID:28123874; PMID:42327758), and no human study has tested whether SASH3 has a ribosomal role in human NK cells.
- Additional finding: knockout protects mice from p53-induced tumour formation and decreases DN thymocyte proliferation (PMID:36401605).

**(b) *Sly1*Δ/Δ N-terminal deletion mouse** (81-aa deletion removing Ser27 and part of the NLS; the truncated protein is confined to the cytoplasm) — PMID:16227612. This is the source of the humoral data: *partially recapitulates* the germinal-centre/memory-B-cell defect (fidelity MODERATE) with reduced lymphoid organ size, loss of marginal-zone B cells, and severely impaired T-dependent **and** T-independent antibody responses, including the pneumococcal polysaccharide IgM response (PMID:18950867), mediated by reduced Notch activity. It also showed prolonged allograft survival.

**Model limitations — three that matter for interpretation:**
1. **Thymic staging is unconfirmed in humans.** The human block is inferred from in vitro CD34+ differentiation and a TRA rearrangement signature, never from thymic tissue.
2. **Compartment mismatch in the humoral arm.** The mouse lesion is at the marginal-zone B-cell transition; the single human histological observation is germinal-centre hypoplasia in spleen. Marginal-zone B cells and their Notch dependence are much better defined in mouse than in human, so the lesions are adjacent but not equivalent, and no patient has been studied for a marginal-zone defect.
3. **The NK mechanism may not transfer at all** (see above) — this is a genuine human/model mismatch, not merely a fidelity caveat.
4. The mouse models are a complete null and a designed hypomorph; one human variant is missense. And no *Sly1* mouse reports neutropenia, the one human phenotype that most needs a model.

**Other model systems:** SASH3-deficient **Jurkat T cells** and **patient-derived primary T cells** with lentiviral rescue are the established in vitro system (PMID:33876203); **in vitro T-cell differentiation of patient CD34+ progenitors** is the human developmental assay. No iPSC, organoid, organ-chip, zebrafish, or *Drosophila* model has been published. No CRISPR or RNAi screen has targeted this disease.

---

## Evidence Base Summary and Caveats

| PMID | Year | Journal | Role |
|---|---|---|---|
| 33876203 | 2021 | Blood | **Index cohort** — 4 unrelated males, 3 variants; defines the disease |
| 35464398 | 2022 | Front Immunol | Adult CVID-like presentation, p.Gln169\* |
| 35748970 | 2022 | J Clin Immunol | IUIS 2022 classification — places SASH3 in Table 1 |
| 35753512 | 2022 | J Allergy Clin Immunol | 1,000-family exome program; 2 SASH3 diagnoses |
| 37646304 | 2023 | Br J Haematol | Evans syndrome, p.Arg288\*; splenic histology; asymptomatic brother |
| 40510848 | 2025 | HemaSphere | Congenital neutropenia WES/WGS cohort including SASH3 |
| 40947476 | 2025 | Hum Genome Var | p.Arg347Cys; maternal carriage; variant table; extra-immune findings |
| 16227612 | 2005 | Mol Cell Biol | *Sly1*Δ/Δ mouse — humoral phenotype |
| 18950867 | 2009 | Mol Immunol | Notch/marginal-zone B cells in *Sly1* mutant mice |
| 19604361 | 2009 | BMC Immunol | *Sly1* KO — thymocyte anti-apoptotic role |
| 26306874 | 2015 | Eur J Immunol | Foxo1-dependent T-cell proliferation |
| 28123874 | 2016 | Oncoimmunology | NK ribosomopathy |
| 33710696 | 2021 | FASEB J | SLy/SASH family review |
| 36401605 | 2023 | Eur J Immunol | DN thymocyte proliferation; p53 tumour protection |
| 42327758 | 2026 | Front Immunol | NK exhaustion/senescence, p53-mediated |

**Three things this report deliberately does not claim.** (1) A worldwide patient count — the published counts overlap and no source states a total. (2) A mechanism for the neutropenia — both candidate explanations are untested, and the honest curation is an open knowledge gap rather than an invented causal edge. (3) That the mouse NK ribosomopathy operates in human patients — it is a well-worked-out mouse mechanism with a matching human phenotype and no human mechanistic data, which is a different epistemic state from a validated model.

**Sources:**
- [OMIM #301082 — IMMUNODEFICIENCY 102; IMD102](https://www.omim.org/entry/301082)
- [OMIM *300441 — SAM- AND SH3 DOMAIN-CONTAINING PROTEIN 3; SASH3](https://www.omim.org/entry/300441)
- [Orphanet: X-linked combined immunodeficiency due to SASH3 deficiency (ORPHA:653751)](https://www.orpha.net/en/disease/detail/653751)
- [UniProt O75995 — SAM and SH3 domain-containing protein 3](https://www.uniprot.org/uniprotkb/O75995/entry)
- [MGI:1921381 — Sash3 (mouse)](https://www.informatics.jax.org/marker/MGI:1921381)
- [Delmonte et al., Blood 2021 (PMID:33876203)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8462359/)
- [Case Report: X-Linked SASH3 Deficiency Presenting as a Common Variable Immunodeficiency (PMID:35464398)](https://pubmed.ncbi.nlm.nih.gov/35464398/)
- [Osteogenesis imperfecta, intellectual disability and recurrent infections in a male with a pathogenic SASH3 variant (PMID:40947476)](https://www.nature.com/articles/s41439-025-00323-1)
- [GeneCards: SASH3](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SASH3)
- [ZFIN: sash3](https://zfin.org/ZDB-GENE-130411-1)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 35 |
| Terms named correctly | 26 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15329` (1 mention) - the report calls it "Splenectomy"; NCIT calls it **Surgical Procedure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002850` (1 mention) - the report calls it "Decreased circulating total IgM"; HP calls it **Decreased circulating IgM concentration**
- `GO:0035591` (1 mention) - the report calls it "Signalling adaptor activity (lost)"; GO calls it **signaling adaptor activity**, and lists "signalling adaptor activity" among its other names
- `GO:0042267` (1 mention) - the report calls it "NK cell mediated cytotoxicity (↓)"; GO calls it **natural killer cell mediated cytotoxicity**, and lists "NK cell mediated cytotoxicity" among its other names
- `GO:0050776` (1 mention) - the report calls it "Regulation of immune response (dysregulated)"; GO calls it **regulation of immune response**
- `GO:0005737` (1 mention) - the report calls it "Subcellular:** cytoplasm"; GO calls it **cytoplasm**
- `NCIT:C62710` (1 mention) - the report calls it "Immunoglobulin replacement therapy"; NCIT calls it **Immunoglobulin Therapy**
- `NCIT:C51993` (1 mention) - the report calls it "Antimicrobial prophylaxis"; NCIT calls it **Antibiotic Prophylaxis**
- `NCIT:C15261` (1 mention) - the report calls it "Immunosuppressive therapy for autoimmune cytopenias"; NCIT calls it **Immunosuppressive Therapy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.
