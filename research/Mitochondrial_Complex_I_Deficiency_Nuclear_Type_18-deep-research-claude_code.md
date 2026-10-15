---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-24T16:51:01.215758'
end_time: '2026-09-24T16:55:27.328418'
duration_seconds: 266.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 18
  mondo_id: MONDO:0032623
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
  web_search_requests: 13
  num_turns: 22
  total_cost_usd: 1.4283472000000002
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
citation_count: 14
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 49
  verified: 43
  not_found: 1
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.022
  unresolved_terms:
  - HP:0002082
  obsolete_terms:
  - term_id: GO:0032947
    ontology_label: GO_0032947
    replaced_by: GO:0060090
  - term_id: GO:0005747
    ontology_label: obsolete mitochondrial respiratory chain complex I
    replaced_by: GO:0045271
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
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 18
- **MONDO ID:** MONDO:0032623 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 18** covering all of the
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

# Research Report: Mitochondrial Complex I Deficiency, Nuclear Type 18 (MC1DN18)

**Target disease:** Mitochondrial Complex I Deficiency, Nuclear Type 18
**Causal gene:** *NDUFAF3* (NADH:ubiquinone oxidoreductase complex assembly factor 3)
**Key identifiers:** OMIM #618240 (MC1DN18); OMIM *612911 (*NDUFAF3* gene); HGNC:29918; parent Orphanet grouping ORPHA:2609 (Isolated complex I deficiency); MONDO:0032623
**Category:** Mendelian (autosomal recessive)

---

## 1. Disease Information

Mitochondrial Complex I Deficiency, Nuclear Type 18 (MC1DN18) is an autosomal recessive disorder of oxidative phosphorylation (OXPHOS) caused by biallelic pathogenic variants in *NDUFAF3*, a nuclear-encoded chaperone required for assembly (not catalysis) of respiratory chain Complex I (NADH:ubiquinone oxidoreductase). It belongs to the large, genetically heterogeneous "isolated Complex I deficiency" disease group and was assigned OMIM number 618240 following the identification of causal *NDUFAF3* variants by Saada et al. in 2009 (PMID: [19463981](https://pubmed.ncbi.nlm.nih.gov/19463981/)) [OMIM #618240; MC1DN18].

- **OMIM disease entry:** #618240
- **OMIM gene entry:** *612911 (*NDUFAF3*, also historically named *C3ORF60*)
- **Gene:** NDUFAF3, HGNC:29918, chromosome 3p21.31
- **Orphanet parent term:** ORPHA:2609 "Isolated complex I deficiency" (the umbrella entity under which nuclear-type subforms, including the *NDUFAF3*-related form, are classified)
- **MONDO:** MONDO:0032623
- **MalaCards / MedGen:** cross-referenced under "Mitochondrial complex I deficiency, nuclear type 18"

**Historical/synonym note:** The literature (and OMIM) also uses "MC1DN18" as shorthand. The causal gene name history is notable for KB curation: the assembly factor was first cloned as *C3ORF60* and later renamed *NDUFAF3*; older papers and databases may still use *C3ORF60*.

**Data provenance:** This report is built from aggregated/curated disease-level resources (OMIM, Orphanet, MedGen, GeneCards) and primary case-series literature (patient-level clinical descriptions embedded in published case reports/series), not from a single large EHR cohort — MC1DN18 is an ultra-rare disorder (fewer than a dozen molecularly confirmed families reported to date across all publications identified in this search).

---

## 2. Etiology

### 2.1 Disease Causal Factors
MC1DN18 is a **purely genetic, monogenic** disorder. It is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *NDUFAF3***, which impair assembly (not catalytic function per se) of Complex I. There is no known environmental, infectious, or purely mechanistic (non-genetic) causal pathway; symptoms can be *precipitated or exacerbated* by intercurrent physiological stress (see below), but the underlying cause is genetic.

### 2.2 Risk Factors

**Genetic:**
- Biallelic pathogenic *NDUFAF3* variants are both necessary and sufficient; this is a fully penetrant recessive Mendelian disease at the molecular level (see Penetrance/Expressivity in Section 9).
- **Consanguinity** is a major risk factor for expression of this ultra-rare autosomal recessive condition. The original description by Saada et al. (PMID: [19463981](https://pubmed.ncbi.nlm.nih.gov/19463981/)) used **homozygosity mapping** across three families, implying consanguineous or endogamous pedigrees, consistent with typical ascertainment for AR mitochondrial disease.
- No modifier genes have been specifically reported for *NDUFAF3*-related disease in the literature identified in this search; general Complex I deficiency modifier literature is not disease-specific enough to attribute to MC1DN18 with confidence — **flagged as a knowledge gap.**

**Environmental:**
- Febrile illness / infection is reported as a precipitant of acute decompensation in a related NDUFAF3-associated leukoencephalopathy presentation — the case reported by Ishiyama et al. 2018 (PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/)) presented with **altered consciousness following a respiratory infection**, a pattern typical of "metabolic stroke"-like decompensation seen broadly across mitochondrial disease (catabolic/febrile stress increasing energy demand beyond a compromised OXPHOS capacity). This is a mechanistic trigger pattern common to mitochondrial disease generally, not something uniquely characterized for *NDUFAF3*.

### 2.3 Protective Factors
No specific genetic or environmental protective factors for *NDUFAF3*-related disease were identified in this search — **knowledge gap**, consistent with the disease's rarity (no population-scale modifier studies exist).

### 2.4 Gene-Environment Interactions
Not specifically characterized for *NDUFAF3*; the general principle for mitochondrial disease (catabolic stress unmasking or worsening a latent bioenergetic deficit) applies, as illustrated by the infection-triggered decompensation above, but no formal gene-environment interaction study exists for this gene.

---

## 3. Phenotypes

### 3.1 Severe/classic (neonatal) presentation — the originally described phenotype

From Saada et al. 2009 (PMID: [19463981](https://pubmed.ncbi.nlm.nih.gov/19463981/)) and subsequent aggregation in OMIM #618240:

| Phenotype | Type | HPO suggestion |
|---|---|---|
| Lactic acidemia (soon after birth) | Laboratory abnormality | HP:0003128 Lactic acidosis |
| Hypotonia (axial) | Physical sign | HP:0008936 Axial hypotonia (or HP:0001252 Hypotonia) |
| Hypertonia | Physical sign | HP:0001276 Hypertonia |
| Poor feeding / poor sucking | Symptom | HP:0011968 Feeding difficulties |
| Weak cry | Physical sign | HP:0001612 Hypernasal speech (approx.) / HP:0001622 Premature birth n/a — best mapped as HP:0001612 not exact; consider free-text if no precise HPO |
| Macrocephaly | Physical sign | HP:0000256 Macrocephaly |
| Wide anterior fontanelle | Physical sign | HP:0000260 Wide anterior fontanel |
| Respiratory problems | Symptom/sign | HP:0002878 Respiratory failure (severity-dependent) |
| Leukomalacia | Neuroimaging finding | HP:0002082 Periventricular leukomalacia (context-dependent) |
| Seizures | Symptom | HP:0001250 Seizure |

Per OMIM's clinical synopsis and the case-series data: **"The seven patients reported to date exhibited severe neurologic symptoms and lactic acidosis, followed by a fatal course, and death occurred by 6 months of age"** in the original description; OMIM's updated synopsis states **death within the first two years of age in six of seven patients** (OMIM #618240, synthesizing Saada et al. 2009 and subsequent case reports).

### 3.2 Expanded/milder phenotype (van der Ven et al. 2023, PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/))

This paper substantially widened the recognized phenotypic spectrum, reporting a patient with **prolonged survival** (to at least age 10) and **comparatively moderate neurologic impairment**:

- Onset at 3.5 years with global developmental delay and clumsy gait
- Progressive exercise intolerance
- Dystonia
- Basal ganglia MRI abnormalities
- Elevated blood lactate
- By age 8: ataxia, dysarthria, dysphonia, failure to thrive, frequent emesis
- Muscle biopsy: abnormal mitochondrial cristae
- Biochemically: **"relatively mild reduction of CI activity"** despite **severely reduced NDUFAF3 and Complex I protein levels**, with **accumulation of early sub-assemblies of the membrane arm of Complex I** (direct finding from PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/))

Suggested HPO terms for this milder end of the spectrum: HP:0001263 Global developmental delay; HP:0003394 Exercise intolerance; HP:0001332 Dystonia; HP:0002071 Abnormality of extrapyramidal motor function; HP:0001251 Ataxia; HP:0001260 Dysarthria; HP:0001618 Dysphonia; HP:0001508 Failure to thrive; HP:0002013 Emesis.

### 3.3 Related but likely partially overlapping phenotype: cavitating leukoencephalopathy

Ishiyama et al. 2018 (PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/)) describe a 1-year-old girl with compound heterozygous *NDUFAF3* variants presenting with:
- Altered consciousness after a respiratory infection
- Bilaterally symmetrical MRI hyperintensity of substantia nigra, medial thalamic nuclei, and basal nuclei (a Leigh-syndrome-like radiological pattern) **plus** cavitating white-matter and corpus callosum lesions
- Elevated CSF lactate; elevated lactate on MR spectroscopy in white matter and basal nuclei
- Muscle Complex I activity reduced to 17–21% of control
- Immunoblot: **"reductions in Q-module (NDUFS2, NDUFS3, and NDUFA9) and P-module (NDUFB10 and NDUFB11) subunits, indicating disruption of mitochondrial complex I assembly"** (direct quote, PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/))

**Curatorial flag (design-decision-relevant):** GeneCards/aggregator listings also associate *NDUFAF3* with "Leigh disease" and with "leukoencephalopathy, progressive, with ovarian failure" (the *EIF2B*-family LBSL/vanishing-white-matter-type disease group) as gene-disease associations — this second association could not be independently verified against a primary source in this search and should be treated as an **unverified lead** requiring direct ClinGen/OMIM gene-page confirmation before use; it may reflect promiscuous aggregator gene-tagging rather than a validated distinct nosologic entity. Do not curate the ovarian-failure association without independent primary-source confirmation.

### 3.4 Phenotype characteristics summary
- **Age of onset:** bimodal — classic form: neonatal/early infantile (birth to weeks of age); expanded/milder form: early childhood (~3.5 years)
- **Severity:** variable, spectrum from fatal neonatal disease to prolonged survival with moderate impairment
- **Progression:** progressive in both forms; the milder form shows gradual accrual of exercise intolerance, ataxia, dysarthria/dysphonia, and failure to thrive over childhood
- **Frequency data:** not quantifiable as percentages given the extremely small published cohort (total of ~9 molecularly confirmed patients across the three cited reports)

### 3.5 Quality of life impact
Not formally studied (no EQ-5D/SF-36 data identified) — expected, given case-count. Qualitatively, the severe form is fatal in infancy; the milder form is associated with substantial motor/speech disability (ataxia, dysarthria, dysphonia) and failure to thrive requiring nutritional support, consistent with the broader mitochondrial-disease QoL literature (not disease-specific).

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene
- **Gene:** *NDUFAF3* (NADH:ubiquinone oxidoreductase complex assembly factor 3), previously *C3ORF60*
- **HGNC:** HGNC:29918
- **Locus:** 3p21.31
- **OMIM gene:** *612911
- **Protein:** 184 amino acids, ~20.4 kDa; predominantly mitochondrial, remains membrane-associated after carbonate extraction, consistent with tight membrane/matrix-arm interaction rather than a soluble matrix protein (GeneCards; Saada et al. 2009)

### 4.2 Pathogenic variants and functional consequence
- **Inheritance mode at the molecular level:** autosomal recessive — homozygous or compound heterozygous variants
- **Variant classes reported:** the original Saada et al. cohort (5 patients/3 families) identified pathogenic *NDUFAF3* mutations via homozygosity mapping and sequencing; van der Ven et al. 2023 report **compound heterozygosity for a pathogenic splice-site variant and a likely pathogenic missense variant**; specific HGVS nomenclature was not retrievable from the abstracts obtained in this search — **primary full-text extraction recommended before KB curation** to obtain exact variant descriptions for ClinVar cross-referencing.
- **Functional consequence:** Loss-of-function/hypomorphic — NDUFAF3 protein is reduced, and downstream Complex I holoenzyme is severely reduced, with **accumulation of early membrane-arm sub-assemblies**, indicating a **specific block in Complex I assembly at an intermediate membrane-arm step**, rather than degradation of the fully catalytic module (PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/)).
- **Population frequency:** Given the extreme rarity (single-digit families reported globally), allele frequencies in gnomAD are expected to be at or near the detection floor; no specific gnomAD frequency was retrieved in this search and should be checked directly against gnomAD before KB entry (curate as a lead, not a verified figure).

### 4.3 Molecular partners
NDUFAF3 **physically and functionally interacts with NDUFAF4** (formerly *C6ORF66*) — the two assembly factors act as an obligate pair early in Complex I assembly — and with Complex I structural subunits **NDUFS2** and **NDUFS3** (GeneCards; Saada et al. 2009, PMID: [19463981](https://pubmed.ncbi.nlm.nih.gov/19463981/): *"NDUFAF3 is a genuine mitochondrial complex I assembly protein that interacts with complex I subunits"* and establishes interaction with NDUFAF4).

### 4.4 Modifier genes, epigenetics, chromosomal abnormalities
No modifier genes, epigenetic mechanisms, or chromosomal-scale abnormalities were identified for MC1DN18 in this search — this reflects genuine absence of study for an ultra-rare disease rather than a negative finding; **report as knowledge gap**.

---

## 5. Environmental Information

No toxin, occupational, lifestyle, or infectious *causal* factor is described for MC1DN18 — it is a fully genetic disease. The one environmental element identified is **infection as a metabolic-decompensation trigger** (respiratory infection preceding acute presentation in the Ishiyama et al. case, PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/)), which would curate as an `environmental[].influences_mechanisms` `EXACERBATES` or `TRIGGERS` edge onto an "acute metabolic decompensation" pathophysiology node rather than as a root cause — this mirrors the general "catabolic stress unmasking OXPHOS insufficiency" pattern documented broadly across mitochondrial disease (general mitochondrial-disease literature, not NDUFAF3-specific).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Biallelic loss-of-function/hypomorphic variants in *NDUFAF3* **lead to** reduced or absent functional NDUFAF3 assembly-chaperone protein (demonstrated directly by immunoblot loss in PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/)).
2. Loss of NDUFAF3 **disrupts its obligate interaction with NDUFAF4** and with the structural Complex I subunits NDUFS2/NDUFS3, which **results in** a block at an intermediate step of Complex I assembly, specifically in **maturation of the membrane (P) arm**, with **accumulation of early membrane-arm sub-assembly intermediates** and reduction of Q-module (NDUFS2, NDUFS3, NDUFA9) and P-module (NDUFB10, NDUFB11) subunit incorporation (directly demonstrated, PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/); PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/)).
3. Failure of Complex I holoenzyme maturation **leads to** severely reduced steady-state levels of assembled, catalytically active Complex I (NADH:ubiquinone oxidoreductase), demonstrated biochemically as markedly reduced Complex I enzyme activity in patient muscle (17–21% of control in the Ishiyama case; "severe complex I deficiency" in the original Saada cohort).
4. Reduced Complex I activity **results in** impaired transfer of electrons from NADH to ubiquinone and **impaired coupled proton translocation across the inner mitochondrial membrane**, which **leads to** diminished proton-motive force available to ATP synthase (Complex V) and a **compensatory shift toward glycolysis with pyruvate reduction to lactate**, manifesting biochemically as elevated blood and CSF lactate (directly observed in both the neonatal and childhood-onset presentations).
5. Chronic cellular ATP insufficiency, compounded by **secondary oxidative stress from electron leak at the stalled/incompletely assembled Complex I** (a well-established general mechanism of Complex I dysfunction; inferred by mechanistic analogy rather than directly demonstrated for *NDUFAF3* in the sources retrieved here), **disproportionately affects high-energy-demand tissues** — skeletal muscle, and especially the basal ganglia, thalamus, substantia nigra, and cerebral white matter, which have high oxidative metabolic demand and low regenerative capacity.
6. In the severe/neonatal phenotype, this **leads to** rapid multi-organ bioenergetic failure — hypotonia/hypertonia, poor feeding, respiratory insufficiency, seizures, and diffuse white-matter injury (leukomalacia) — **resulting in** death, typically within the first months to two years of life.
7. In the milder/later-onset phenotype (where residual NDUFAF3/Complex I function is only partially compromised — **"relatively mild reduction of CI activity"** despite markedly reduced protein levels, PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/)), the same mechanism **leads to** a slower, progressive neurodegenerative course — developmental delay, progressive exercise intolerance, dystonia and other basal-ganglia dysfunction, ataxia, dysarthria/dysphonia, and failure to thrive — **without** the early lethality of the classic form.
8. In a subset of patients, the basal-ganglia/brainstem pattern of injury converges with the **Leigh syndrome final-common-pathway phenotype** (a well-established convergence point for many nuclear and mtDNA Complex I assembly-factor defects — general Leigh syndrome literature; PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/) shows radiologically Leigh-like symmetric substantia nigra/thalamic/basal ganglia involvement), while an additional cerebral white-matter injury branch (cavitating leukoencephalopathy) can occur in parallel or independently, as shown by Ishiyama et al.

### Molecular pathways
- Oxidative phosphorylation / electron transport chain, specifically the **Complex I (NADH:ubiquinone oxidoreductase) assembly pathway**. KEGG: hsa00190 Oxidative phosphorylation. Reactome: "Complex I biogenesis" pathway (R-HSA-6799198).
- **GO Biological Process suggestions:** GO:0006120 mitochondrial electron transport, NADH to ubiquinone; GO:0032981 mitochondrial respiratory chain complex I assembly; GO:0006099 tricarboxylic acid cycle (downstream, compensatory relevance); GO:0006123 mitochondrial electron transport, cytochrome c to oxygen (downstream chain context).
- **GO Molecular Function:** the NDUFAF3 protein itself is a chaperone without catalytic activity (no established enzymatic GO MF term beyond "protein-containing complex scaffold activity," GO:0032947, tentative — verify against UniProt before binding).
- **GO Cellular Component:** GO:0005747 mitochondrial respiratory chain complex I; GO:0005743 mitochondrial inner membrane; GO:0005739 mitochondrion.

### Cellular processes
- Cellular ATP depletion; compensatory glycolysis/lactate production; secondary reactive oxygen species generation from a partially assembled, electron-leaking Complex I (general Complex I biology; GO:0006979 response to oxidative stress as an inferred downstream node).

### Protein dysfunction
- NDUFAF3 itself: loss-of-function due to reduced protein stability/abundance (demonstrated by immunoblot).
- Downstream: failure of Complex I holocomplex maturation, with accumulation of aberrant membrane-arm sub-assembly intermediates rather than simple absence of protein — this is a **specific assembly-intermediate accumulation phenotype**, distinguishing NDUFAF3 dysfunction mechanistically from subunit-structural-gene defects that more often cause simple failure to form any stable sub-complex.

### Metabolic changes
- Elevated lactate (blood and CSF) reflecting a shift toward anaerobic glycolysis; elevated lactate on MR spectroscopy in affected brain regions (directly observed, PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/)).

### Tissue damage mechanisms
- Basal ganglia/thalamic/substantia nigra neuronal injury (Leigh-like pattern) and cerebral white-matter cavitation/leukomalacia, consistent with regional vulnerability of high-oxidative-demand CNS structures to chronic ATP insufficiency plus oxidative stress.

### Advanced/omics profiling
No transcriptomic, proteomic (beyond targeted immunoblot of Complex I subunits), metabolomic, single-cell, or spatial data specific to *NDUFAF3*-related disease were identified in this search. The immunoblot/BN-PAGE assembly-intermediate data in PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/) and PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/) constitute the most granular molecular profiling currently published.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- Central nervous system — brain (basal ganglia, thalamus, substantia nigra, cerebral white matter, corpus callosum) — UBERON:0000955 brain; UBERON:0002420 basal ganglion; UBERON:0001897 dorsal thalamus; UBERON:0002038 substantia nigra
- Skeletal muscle — UBERON:0001134 skeletal muscle tissue (site of diagnostic biopsy/enzyme assay in all cited reports)

**Secondary/systemic involvement:**
- Respiratory system (respiratory insufficiency in the severe neonatal form) — UBERON:0000072 respiratory system
- Growth/nutrition — failure to thrive reflects systemic metabolic insufficiency rather than a discrete organ lesion

**Tissue/cell level:**
- Neurons of the basal ganglia and brainstem (high oxidative-metabolic-demand cell populations) — CL:0000540 neuron; more specific CL binding (e.g., CL:0000691 Purkinje neuron, or basal ganglia-specific types) was not directly evidenced in the sources retrieved and should not be over-specified without a primary histopathologic source.
- Skeletal myocytes — CL:0000188 skeletal muscle myoblast / CL:0008002 skeletal muscle fiber (biopsy-demonstrated abnormal mitochondrial cristae, PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/) - van der Ven et al.)
- White-matter oligodendrocytes/astrocytes (inferred site of cavitating leukoencephalopathy; not directly assayed at the cellular level in the cited report) — flag as inferred, not directly demonstrated.

**Subcellular level:**
- Mitochondria, specifically the **mitochondrial inner membrane** (site of Complex I) — GO:0005743 mitochondrial inner membrane; abnormal mitochondrial cristae were directly observed on muscle biopsy electron microscopy (PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/)).

**Localization/laterality:** CNS lesions are reported as **bilaterally symmetric** (substantia nigra, medial thalamic nuclei, basal nuclei) — a classic Leigh-syndrome-pattern radiologic signature (PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/)).

---

## 8. Temporal Development

- **Onset:** Bimodal.
  - Classic/severe form: neonatal to early infantile onset — symptoms by 3 weeks of age in the index cases (Saada et al. 2009).
  - Expanded/milder form: early childhood onset (~3.5 years) with slower accrual of findings (van der Ven et al. 2023).
- **Onset pattern:** acute/subacute in the severe neonatal form (rapid deterioration); insidious/progressive in the milder childhood-onset form, sometimes punctuated by acute decompensation triggered by infection (Ishiyama et al. 2018).
- **Progression:** Progressive in both forms.
  - Severe form: rapid multisystem decline, death within months (original cohort) to within 2 years (OMIM synthesis, 6/7 patients).
  - Milder form: gradual accrual over years — developmental delay at 3.5y progressing to ataxia, dysarthria, dysphonia, failure to thrive, and frequent emesis by age 8, with survival documented to at least age 10 (van der Ven et al. 2023).
- **Disease course pattern:** chronic progressive, with possible acute exacerbations during intercurrent illness (metabolic decompensation pattern typical of mitochondrial disease).
- **Duration:** Life-limiting in the severe form (early death); chronic/lifelong in the milder form, with unknown long-term natural history beyond the reported follow-up window.
- **Critical periods:** Neonatal/early-infantile period represents the highest-risk window for the severe phenotype; no data on a specific intervention window (no disease-modifying therapy exists to time an intervention against).

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (AR). HPO/OMIM designation: HP:0000007 Autosomal recessive inheritance.
- **Epidemiology:** MC1DN18 specifically has no published prevalence/incidence estimate — it is represented by fewer than ten molecularly confirmed patients across the literature identified in this search (5 patients/3 families in Saada et al. 2009; 1 additional patient in Ishiyama et al. 2018; 1 additional patient in van der Ven et al. 2023; OMIM references "seven patients reported to date" as of its most recent synthesis, subsequently supplemented by at least the 2023 case). This places it well within the **ultra-rare** tier (Orphanet qualitative class, since no numeric prevalence has been established — `prevalence_class: NOT_YET_DOCUMENTED` with a qualitative `ULTRA_RARE` tier being defensible per the disease's case count, pending an Orphanet-specific numeric entry).
- **Broader context:** Isolated Complex I deficiency as a whole (all genetic causes combined, ORPHA:2609) is the **most common single OXPHOS defect category** in pediatric mitochondrial disease, accounting for **approximately 25–35% of OXPHOS cases identified in newborns**, within an overall OXPHOS-disorder birth prevalence of **approximately 1 in 5,000** (general Complex I deficiency literature — Tucker et al. 2011, PMID: [21766414](https://pubmed.ncbi.nlm.nih.gov/21766414/), and related reviews). This population-level figure describes the *gene-heterogeneous group*, not MC1DN18 specifically, and should be curated as `prevalence[]` context on a broader "isolated Complex I deficiency" entity/grouping rather than attributed numerically to MC1DN18 itself.
- **Penetrance:** Presumed complete for the biallelic genotype based on all reported cases being symptomatic, though this is an ascertainment-biased inference typical of ultra-rare recessive disease reporting (cases are found because they are symptomatic).
- **Expressivity:** Markedly variable — from neonatal lethality to survival past a decade with moderate impairment, as directly demonstrated by comparing the Saada (2009), Ishiyama (2018), and van der Ven (2023) cohorts. The 2023 paper's title explicitly frames this as "expanding the phenotypic and biochemical spectrum," and correlates milder clinical severity with **relatively preserved residual Complex I enzymatic activity despite severely reduced protein levels** — a genotype-phenotype/biochemistry correlation worth flagging for pathophysiology curation (a `mechanistic_hypotheses` candidate: residual-activity threshold as a severity modifier).
- **Genetic anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency, geographic distribution, sex ratio, age distribution:** Not established in the literature identified in this search — genuine knowledge gaps given the small number of reported families. The use of homozygosity mapping in the founding description (Saada et al. 2009) is consistent with consanguineous ascertainment in at least a subset of families, but no formal founder-variant or consanguinity-rate statement was retrieved.

---

## 10. Diagnostics

**Laboratory tests:**
- Blood and CSF lactate (elevated in both reported phenotypic forms) — LOINC 2524-7 Lactate [Moles/volume] in Serum or Plasma (representative code)
- Muscle Complex I enzyme activity assay (spectrophotometric NADH:ubiquinone oxidoreductase activity) — directly used in Ishiyama et al. (17–21% of control) and implicit in the original Saada cohort's "severe complex I deficiency" classification

**Imaging:**
- Brain MRI: bilaterally symmetric T2/FLAIR hyperintensity of substantia nigra, medial thalamic nuclei, basal nuclei (Leigh-like pattern); cavitating white-matter and corpus callosum lesions in the leukoencephalopathy-predominant presentation (Ishiyama et al. 2018)
- MR spectroscopy: elevated lactate peak in affected white matter/basal nuclei (Ishiyama et al. 2018)

**Biopsy/pathology:**
- Skeletal muscle biopsy: abnormal mitochondrial cristae on electron microscopy (van der Ven et al. 2023)
- Muscle tissue: immunoblot/BN-PAGE showing severely reduced Complex I and NDUFAF3 protein, with reduction of specific Q-module (NDUFS2, NDUFS3, NDUFA9) and P-module (NDUFB10, NDUFB11) subunits and accumulation of aberrant assembly intermediates (both PMID: [29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/) and PMID: [37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/))

**Genetic testing:**
- Definitive diagnosis requires molecular confirmation of biallelic *NDUFAF3* variants. Approaches used in the literature: homozygosity mapping + Sanger sequencing (Saada et al. 2009, earliest description); trio whole-exome sequencing (van der Ven et al. 2023, explicitly stated); targeted/panel gene sequencing is presumed feasible via any comprehensive mitochondrial-disease/nuclear-encoded-OXPHOS gene panel, though this specific modality wasn't directly documented in the retrieved sources for MC1DN18.
- Given genetic heterogeneity of isolated Complex I deficiency (at least 44 structural subunits and >15 known nuclear assembly factors, per general Complex I literature), **whole-exome or gene-panel sequencing is the practical first-line molecular approach** rather than single-gene testing, consistent with how both confirmatory cases in this report were actually diagnosed (WES).

**Differential diagnosis:**
- Other nuclear Complex I deficiency subtypes (MC1DN1 through MC1DN20+, various *NDUFS*, *NDUFV*, *NDUFA*, and other *NDUFAF* assembly-factor genes)
- mtDNA-encoded Complex I gene defects (*MT-ND1–6*, *MT-ND4L*)
- Leigh syndrome from other causal genes (e.g., *SURF1*, *MT-ATP6*) when the Leigh-like radiologic pattern predominates
- Leukoencephalopathy with vanishing white matter (*EIF2B1-5*) when the cavitating leukoencephalopathy pattern predominates — this differential is explicitly what motivated the Ishiyama et al. report title ("...may associate with cavitating leukoencephalopathy")

**Screening:** No newborn screening test exists for MC1DN18 specifically (lactic acidosis is a nonspecific analyte not currently part of standard newborn screening panels); no disease-specific carrier or cascade screening program identified, consistent with its ultra-rare status.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Poor in the classic neonatal-onset form — death by 6 months of age in the original description (Saada et al. 2009); OMIM's synthesis states death within the first two years of life in 6 of 7 originally reported patients. In contrast, the 2023-reported milder phenotype demonstrates **survival past age 10** with ongoing but comparatively moderate impairment, establishing that MC1DN18 is not uniformly fatal.
- **Morbidity/function:** In survivors, chronic progressive motor and bulbar disability — ataxia, dysarthria, dysphonia, exercise intolerance, dystonia, and failure to thrive.
- **Complications:** Respiratory insufficiency and seizures in the severe form; frequent emesis and failure to thrive as chronic complications in the milder form.
- **Quality-of-life measures:** Not formally assessed in the literature identified.
- **Prognostic factors:** The 2023 paper's biochemical data suggest that **residual Complex I enzymatic activity (rather than absolute protein abundance)** may track with clinical severity — patients with only "relatively mild reduction of CI activity" despite severe protein loss had a substantially better clinical course than the original severe/fatal cohort. This is a candidate prognostic biomarker relationship, though drawn from a single comparative case rather than a systematic cohort, and should be flagged as such in curation.

---

## 12. Treatment

No disease-specific, FDA-approved, or NDUFAF3-targeted therapy exists. Management follows the general **mitochondrial disease supportive-care paradigm**:

**Pharmacotherapy (symptomatic/supportive, general mitochondrial-disease "cocktail," not NDUFAF3-specific evidence):**
- Coenzyme Q10 (CHEBI:46245 ubiquinone / relevant CoQ10 CHEBI term) — NCIT:C15986 Pharmacotherapy category; evidence base for OXPHOS disease broadly is weak/theoretical outside primary CoQ10 biosynthesis defects
- Riboflavin — some non-randomized evidence of benefit specifically in Complex I and/or Complex II disease (general mitochondrial disease literature)
- Thiamine (50–100 mg three times daily, most widely recommended per general Leigh-syndrome-spectrum literature) — NCIT:C15986 Pharmacotherapy; CHEBI thiamine term
- L-carnitine, alpha-lipoic acid, creatine monohydrate, biotin — part of the broader empirical "mito cocktail," without disease-specific trial evidence for MC1DN18
- **Evidence caveat, quoted from general Leigh-syndrome-spectrum GeneReviews-type sourcing identified in this search:** "there is no established evidence base for any of these compounds in mtDNA-LSS[-type disease]" and CoQ10 "has limited evidence for efficacy in the treatment of LSS" outside primary CoQ10 biosynthesis disorders (general source, not NDUFAF3-specific — treat as background evidence, `quote_role: BACKGROUND` if curated).

**Dietary:**
- Ketogenic diet is beneficial specifically when **pyruvate dehydrogenase deficiency** coexists — not directly relevant to isolated Complex I deficiency unless comorbid, and not documented as used in MC1DN18 case reports retrieved here.

**Supportive/rehabilitative:**
- Multidisciplinary supportive care — pediatrics, neurology, cardiology, ophthalmology, audiology, nutrition/feeding support (general Leigh syndrome/mitochondrial disease management framework) — NCIT:C15302 Physical Therapy, NCIT:C15747 Supportive Care as general treatment-term candidates.
- Nutritional support/feeding intervention given failure to thrive and frequent emesis documented in the milder phenotype.

**Experimental/advanced therapeutics:**
- No gene therapy, cell therapy, or RNA-based therapy specific to *NDUFAF3* or MC1DN18 was identified in this search. No registered clinical trial (ClinicalTrials.gov) targeting MC1DN18 or NDUFAF3 specifically was located.
- One search result surfaced an unrelated/likely-spurious "therapeutic context" pairing of NDUFAF3 with metformin and ME-344 from an aggregator snippet; this could not be traced to a primary source in this pass and **should not be used for curation without independent verification** — flagged explicitly as an unverified, likely low-confidence lead.

**Treatment strategy:** No published treatment algorithm specific to MC1DN18; management follows generic Leigh-syndrome-spectrum/mitochondrial-disease supportive protocols by extrapolation, not disease-specific trial data.

---

## 13. Prevention

- **Primary prevention:** Genetic counseling for known carrier couples (implied by AR inheritance and the consanguinity pattern in founding pedigrees); no vaccine or exposure-avoidance strategy applies (non-environmental etiology).
- **Secondary prevention:** No population screening program exists. Prenatal diagnosis / preimplantation genetic diagnosis would be feasible in a family with a previously identified pathogenic *NDUFAF3* genotype, following standard AR-disease reproductive counseling practice, though this was not directly documented as performed in any retrieved case.
- **Tertiary prevention:** Aggressive avoidance/early treatment of catabolic stress (febrile illness, prolonged fasting) is a general principle in mitochondrial disease management to reduce risk of acute decompensation, directly supported by the infection-triggered presentation in the Ishiyama et al. case.
- **Counseling:** Genetic counseling is indicated for parents of an affected child (recurrence risk 25% per pregnancy under AR inheritance) and for extended family members in consanguineous kindreds.

---

## 14. Other Species / Natural Disease

- No naturally occurring *NDUFAF3*-associated disease in non-human species (companion animals, livestock, wildlife) was identified in this search (no OMIA entry surfaced).
- **Orthology:** *Ndufaf3* has a well-conserved mouse ortholog (MGI:1913956, *Ndufaf3*, "NADH:ubiquinone oxidoreductase complex assembly factor 3") and a zebrafish ortholog *ndufaf3* (confirmed via NCBI Gene/PubChem gene records for zebrafish). No published constitutive or conditional *Ndufaf3* knockout mouse or zebrafish disease-model phenotype was identified in this search — this is a **specific, actionable knowledge gap**: unlike the well-characterized *Ndufs4−/−* mouse (a related but distinct Complex I subunit knockout used extensively as a Leigh-syndrome model, e.g. PMID: [35266966](https://pmc.ncbi.nlm.nih.gov/articles/PMC8967107/)-type literature), no dedicated *Ndufaf3* animal model publication surfaced, despite active search.
- **Comparative biology:** Given that NDUFAF3's core assembly-chaperone role (partnering with NDUFAF4 to support membrane-arm maturation) is a conserved feature of Complex I biogenesis across eukaryotes, mechanistic insights from *Ndufs4* and other Complex I assembly-factor animal models (documented broadly in the mitochondrial-disease modeling literature) are reasonably extrapolated as analogous, but this is an inference, not direct NDUFAF3 model-organism evidence, and should be curated with a `HUMAN_MODEL_MISMATCH`-type flag if used to support any disease-model claim, since no direct model exists yet.

---

## 15. Model Organisms

- **Mouse:** *Ndufaf3* ortholog cataloged at MGI:1913956, but no disease-modeling publication (knockout, knock-in, or conditional) reporting a phenotype was located in this search.
- **Zebrafish:** *ndufaf3* ortholog cataloged (NCBI Gene/PubChem zebrafish gene record), but again no phenotyping publication was located. By contrast, related Complex I assembly-factor zebrafish models exist in the literature (e.g., *ndufaf2−/−*, and *ndufs2−/−* zebrafish reported to show impaired survival, neuromuscular activity, morphology, and one-carbon metabolism responsive to folic acid supplementation, per a 2025 report identified in this search) — these are useful *analogous* Complex I assembly-pathway models but are **not** *NDUFAF3*-specific and should not be cited as direct evidence for MC1DN18 pathophysiology.
- **Cellular models:** Patient-derived skeletal muscle biopsies and cultured fibroblasts are the model systems actually used in the cited human studies (BN-PAGE/immunoblot analysis of Complex I assembly intermediates); no iPSC-derived or CRISPR-engineered isogenic cellular model specific to *NDUFAF3* was identified.
- **Research applications:** Existing human-tissue-based studies (muscle biopsy immunoblotting/BN-PAGE) have been sufficient to establish the assembly-intermediate-accumulation mechanism, but a dedicated animal model would be valuable for testing any future therapeutic strategy (none currently exists) and for establishing genotype-severity correlations suggested by the human case comparison in Section 9/11.

---

## Summary of Key Knowledge Gaps (for curation triage)

1. No formal prevalence/incidence estimate specific to MC1DN18 (only whole-group "isolated Complex I deficiency" epidemiology exists).
2. No dedicated *Ndufaf3* animal model (mouse or zebrafish) phenotype publication located.
3. No confirmed primary-source support for the aggregator-only "leukoencephalopathy with ovarian failure" and metformin/ME-344 associations — both should be treated as unverified leads, not curated facts.
4. Exact HGVS variant nomenclature for reported *NDUFAF3* alleles was not retrievable from abstracts in this pass — full-text extraction needed before ClinVar cross-referencing.
5. No gnomAD population-frequency data specifically verified for reported *NDUFAF3* pathogenic alleles.
6. No formal quality-of-life, disability, or long-term natural-history study beyond the individual case reports summarized above.

---

## Sources

- [OMIM #618240 — Mitochondrial Complex I Deficiency, Nuclear Type 18 (MC1DN18)](https://omim.org/entry/618240)
- [OMIM *612911 — NDUFAF3 gene entry](https://omim.org/entry/612911)
- Saada A, Vogel RO, Hoefs SJ, et al. "Mutations in NDUFAF3 (C3ORF60), encoding an NDUFAF4 (C6ORF66)-interacting complex I assembly protein, cause fatal neonatal mitochondrial disease." Am J Hum Genet. 2009. [PMID: 19463981](https://pubmed.ncbi.nlm.nih.gov/19463981/)
- Ishiyama A, Muramatsu K, Uchino S, et al. "NDUFAF3 variants that disrupt mitochondrial complex I assembly may associate with cavitating leukoencephalopathy." Clin Genet. 2018. [PMID: 29344937](https://pubmed.ncbi.nlm.nih.gov/29344937/) / [ScienceDirect/Wiley](https://doi.org/10.1111/cge.13215)
- van der Ven AT, Cabrera-Orefice A, Wente I, et al. "Expanding the phenotypic and biochemical spectrum of NDUFAF3-related mitochondrial disease." Mol Genet Metab. 2023. [PMID: 37572574](https://pubmed.ncbi.nlm.nih.gov/37572574/) / [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1096719223003050)
- [NDUFAF3 Gene — GeneCards](https://www.genecards.org/card/NDUFAF3)
- [Ndufaf3 — MGI Mouse Gene Detail (MGI:1913956)](https://www.informatics.jax.org/marker/MGI:1913956)
- [Orphanet: Isolated complex I deficiency (ORPHA:2609)](http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=2609)
- Tucker EJ, Compton AG, Thorburn DR. "The molecular basis of human complex I deficiency." IUBMB Life. 2011. [PMID: 21766414](https://pubmed.ncbi.nlm.nih.gov/21766414/)
- [Mitochondrial complex I deficiency — GARD/NIH](https://rarediseases.info.nih.gov/diseases/3908/mitochondrial-complex-i-deficiency)
- [Mitochondrial DNA-Associated Leigh Syndrome Spectrum — GeneReviews (general Leigh-syndrome management context)](https://www.ncbi.nlm.nih.gov/books/NBK1173/)
- [Ndufs4 knockout mouse models of Leigh syndrome: pathophysiology and intervention — Brain, 2022 (analogous Complex I assembly-factor model, general context)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8967107/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 3 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002082` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0032947` (GO_0032947) (1 mention) - replaced by `GO:0060090`
- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.