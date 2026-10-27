---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-03T18:38:36.507584'
end_time: '2026-10-03T18:39:35.545926'
duration_seconds: 59.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Catamenial Pneumothorax
  mondo_id: MONDO:0022098
  category: Complex
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.8040117999999999
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  assistant_text_blocks: 1
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
citation_count: 10
reference_validation:
  total_references: 8
  verified: 3
  not_found: 0
  unverifiable: 5
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Catamenial Pneumothorax
- **MONDO ID:** MONDO:0022098 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Catamenial Pneumothorax** covering all of the
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

# Catamenial Pneumothorax: Research Report

**Verification status.** Only the PMIDs and URLs listed under "Sources actually retrieved" came from searches in this session, and I did not open the full texts or check abstract quotes. Everything else is from background knowledge of the literature and is marked *(unverified)*. Do not cite those items in the KB until they have been fetched with `just fetch-reference` and quoted exactly. I did not verify any ontology CURIEs. HP, GO, CL, UBERON and NCIT lookups are still needed, and the MONDO ID in the request (MONDO:0022098) is unconfirmed.

## 1. Disease information

Catamenial pneumothorax (CP) is a recurrent spontaneous pneumothorax that occurs within about 72 hours before or after the onset of menstruation. It mostly affects women of reproductive age. Most cases are attributed to thoracic endometriosis syndrome (TES). A recent review describes it as "an uncommon condition, usually associated with thoracic endometriosis syndrome (TES)" and notes that international guidelines are still lacking (PMC11728258).

- **Synonyms:** menstrual pneumothorax, endometriosis-related pneumothorax. It is the commonest manifestation of TES. The others are catamenial hemothorax, catamenial hemoptysis, and pulmonary endometriosis nodules.
- **Identifiers:** I did not confirm OMIM, Orphanet, ICD-10/11 or MeSH entries. ICD-10 N80.8 (other endometriosis) is a plausible fit *(unverified)*. The search tool only reached the NCBI MedGen page (C0340007) and did not retrieve its contents.
- **Lump/split note for dismech:** CP is a clinical presentation of TES, not a separate pathogen-defined disease. Consider whether it belongs as a `DISEASE` entry, as a subtype of thoracic endometriosis or endometriosis, or as a `GROUPING` member. Record the decision in the stub `notes`.
- **Data source:** The evidence is aggregated case series and case reports. It does not come from EHR-derived cohorts.

## 2. Etiology

- **Causal factors:** There is no single causal gene or exposure. The leading mechanisms are thoracic endometriosis (diaphragmatic, pleural or parenchymal) and passage of air through diaphragmatic defects. Lung blebs or bullae and hormonal effects are other proposed contributors.
- **Risk factors:**
  - Pelvic endometriosis. CP can be the first presentation of both thoracic and pelvic disease (Ciriaco et al., PMID 35268286).
  - Reproductive age.
  - Prior uterine or pelvic surgery *(unverified)*.
  - Genetic susceptibility is not established.
- **Protective factors:** Ovarian suppression by GnRH analogues or hormonal contraception reduces recurrence once the disease is present. These are treatments, not primary protective factors.
- **Gene-environment interactions:** None are established.

## 3. Phenotypes

Frequencies below are approximate and from memory *(unverified)*. They need to be traced to primary series, such as the Joseph & Sahn and Visouli et al. reviews.

| Phenotype | Notes | Candidate HPO term (look up) |
|---|---|---|
| Recurrent spontaneous pneumothorax | Cyclical, within 72 h of menses. Right-sided in about 85–90%. | Recurrent pneumothorax / Pneumothorax |
| Chest or shoulder pain | Common presenting symptom | Chest pain |
| Dyspnea | Common | Dyspnea |
| Cough | Occasional | Cough |
| Catamenial hemothorax | Part of TES | Hemothorax |
| Catamenial hemoptysis | Part of TES | Hemoptysis |
| Pelvic endometriosis | Often coexisting | Endometriosis |
| Pelvic pain, dysmenorrhea | Often coexisting | Dysmenorrhea |

- **Onset:** Typically the 30s to 40s *(unverified)*. Onset is acute and episodic, and episodes recur with the cycle.
- **Quality of life:** Repeated hospitalizations and drainage procedures, and diagnostic delay. The sources I found did not give formal QoL instrument data.

## 4. Genetic and molecular information

No causal genes or pathogenic variants are established. I found no evidence for a Mendelian cause, so do not create `genetic:` causal rows without a source. Endometriosis itself has polygenic susceptibility (GWAS loci), but I did not verify any specific locus for thoracic disease. There is no chromosomal or epigenetic data in what I retrieved.

## 5. Environmental information

There are no established environmental, lifestyle or infectious factors. The relevant trigger is endogenous: the menstrual cycle.

## 6. Mechanism / pathophysiology

**Proposed causal chains** (the search results name four theories: physiological, migrational, microembolic-metastatic, and the diaphragmatic theory of air passage):

1. **Diaphragmatic air-passage branch (anatomical).**
   1. Diaphragmatic fenestrations are present, usually right-sided.
   2. During menses the cervical mucus plug is absent.
   3. Air passes from the genital tract into the peritoneal cavity.
   4. Air crosses the diaphragmatic fenestrations into the right pleural space.
   5. The result is pneumothorax at menses.
   - This is a proposed pathway, not demonstrated in all patients. It is the usual explanation when no thoracic endometriosis is found.
2. **Thoracic endometriosis branch.**
   1. Endometrial tissue reaches the diaphragm or pleura. The route is proposed to be retrograde menstruation with transperitoneal passage, or microembolic or lymphovascular spread. This is inferred, not shown.
   2. Ectopic endometrial implants respond to cyclic hormones.
   3. Menstrual shedding at the implants causes the diaphragmatic perforation or visceral pleural/parenchymal disruption.
   4. Air enters the pleural space, and pneumothorax follows.
3. **Hormonal/prostaglandin branch.**
   1. Prostaglandin F2α rises at menses.
   2. It is proposed to cause bronchiolar constriction, especially in expiration.
   3. Alveolar rupture follows and traps air in the pleural space.
   - This is a hypothesis. The search summary describes it as a theory only.
4. **Bleb rupture branch.** Cyclic hormonal changes are proposed to cause spontaneous bleb rupture. This is weakly supported.

**Suggested ontology terms** (all need lookup before use):

- GO: response to estradiol, response to progesterone, prostaglandin biosynthetic process.
- CL: endometrial stromal cell, endometrial epithelial cell.
- UBERON: diaphragm, parietal pleura, visceral pleura, pleural cavity, right lung.
- CHEBI: prostaglandin F2α.

No molecular profiling, single-cell or CRISPR data were found.

## 7. Anatomical structures affected

- **Primary:** Right hemidiaphragm, pleura and pleural space, and lung. Right-sided predominance is widely reported *(unverified figure)*.
- **Secondary:** Pelvic organs, because endometriosis often coexists.
- **Tissue and cell level:** Ectopic endometrial glands and stroma on the diaphragm or pleura.
- **Lateralization:** Predominantly right-sided and usually unilateral.

## 8. Temporal development

- The course is recurrent and cyclical, with episodes clustering around menses.
- Without definitive treatment, recurrence is frequent. Chest tube drainage alone carries a recurrence rate of up to 50% according to the search summary.
- Remission occurs during ovarian suppression, pregnancy, or after menopause *(unverified)*.

## 9. Inheritance and population

- It is not a Mendelian disease, and no inheritance pattern is established.
- It is rare. I could not source prevalence or incidence figures.
- It affects only people with a menstrual cycle, with onset mostly in the reproductive years.
- Diagnostic delay is likely, because the cyclical pattern is missed. Reviews describe it as an "unveiled disease" (PMC11728258).

## 10. Diagnostics

- **Clinical criterion:** Pneumothorax recurring within 72 hours of menses, with a cyclical history *(unverified criterion)*.
- **Imaging:** Chest X-ray, and CT, which can show diaphragmatic defects or nodules. Pelvic and thoracic MRI can help detect endometriosis. Timing the imaging to menses improves the yield *(unverified)*.
- **Thoracoscopy:** VATS allows direct inspection of the diaphragm for perforations or implants. It is also the route for biopsy, with histology showing endometrial glands and stroma. Immunohistochemistry (ER, PR, CD10) is supportive *(unverified)*.
- **Differential diagnosis:** Primary spontaneous pneumothorax, lymphangioleiomyomatosis, Birt-Hogg-Dubé syndrome, and other causes of cystic lung disease.
- **Genetic testing:** Not applicable for typical CP. FLCN testing is relevant only where cystic lung disease or Birt-Hogg-Dubé syndrome is a differential.

## 11. Outcome and prognosis

- Recurrence depends on the treatment. Surgery followed by prompt hormonal therapy gave no recurrence in the series summarized in the search. One patient had a recurrence when hormone therapy was delayed by 6 weeks (from search summaries; I did not read the underlying papers).
- Mortality is very low, and complications relate to repeated pneumothorax and procedures. I found no sourced survival data.
- Prognostic factors: completeness of surgical treatment and adherence to hormonal suppression.

## 12. Treatment

- **Acute episode:** Chest tube drainage. Recurrence after drainage alone is high, up to 50% per the search summary.
- **Hormonal therapy:**
  - GnRH analogues for 6–12 months are described as the broad consensus for preventing recurrence. They induce hypogonadotropic hypogonadism and amenorrhea.
  - Oral contraceptives, progestins and danazol have been used *(unverified)*.
  - Candidate NCIT terms: Pharmacotherapy `NCIT:C15986`, with `therapeutic_agent` for leuprolide or other agents. Look up each agent in CHEBI/NCIT.
- **Surgery:**
  - VATS inspection of the diaphragm.
  - Mechanical pleurodesis.
  - Repair of diaphragmatic defects, with or without mesh.
  - Resection of implants or blebs.
  - Candidate NCIT: Surgical Procedure `NCIT:C15329`. A thoracoscopic-surgery term may exist and needs checking.
  - Combination of VATS plus postoperative hormonal therapy gives the best outcomes, per the search summary.
- **Multidisciplinary care:** Thoracic surgery, gynecology and pulmonology (PMC11728258).
- **Pharmacogenomics, gene/cell/RNA therapies and clinical trials:** None found. I did not search ClinicalTrials.gov.

## 13. Prevention

- There is no primary prevention.
- Tertiary prevention is hormonal suppression after surgery, started promptly.
- Early recognition of the menstrual pattern could shorten diagnostic delay.

## 14. Other species / natural disease

No naturally occurring animal disease was identified. This section is not applicable on the evidence I retrieved. I did not query OMIA.

## 15. Model organisms

I found no established animal model of catamenial pneumothorax. Endometriosis models exist in mouse and primate, but I did not verify any that reproduce thoracic disease. Treat this section as a gap, and consider a `KNOWLEDGE_GAP` discussion rather than an `animal_models:` entry.

## Curation recommendations

1. Fetch the references below with `just fetch-reference PMID:<id>` and quote only exact substrings.
2. Locate the primary large-series sources for laterality, age, frequency and recurrence figures, and for the TES component percentages. Do not rely on my recalled numbers.
3. Verify the MONDO ID, and decide the lump/split question first.
4. Run `just check-causal-targets` and wire the phenotypes. Unconnected phenotypes would be a likely weakness in this entry.

## Sources actually retrieved

- [Catamenial Pneumothorax—Still an Unveiled Disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11728258/) (PMC11728258)
- Ciriaco et al., *Catamenial Pneumothorax as the First Expression of Thoracic Endometriosis Syndrome and Pelvic Endometriosis*, J Clin Med 2022. [PMID 35268286](https://pmc.ncbi.nlm.nih.gov/articles/PMC8911039)
- Hirono et al., *Spontaneous recurrent menstrual pneumothorax: a case report*, Ann Med Surg. [PMID 38333324](https://pmc.ncbi.nlm.nih.gov/articles/PMC10849425)
- Tsakiridis et al., *Catamenial pneumothorax recurrence due to endometriosis*, Respir Med Case Rep 2020. [PMID 32190546](https://pmc.ncbi.nlm.nih.gov/articles/PMC7068682)
- [Multi-Loculated Catamenial Pneumothorax: A Rare Complication of Thoracic Endometriosis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8481132/)
- Other pages surfaced by the searches but not read: [Wikipedia](https://en.wikipedia.org/wiki/Catamenial_pneumothorax), [Respiratory Care](https://rc.rcjournal.com/content/respcare/58/12/e168.full.pdf), [NORD](https://rarediseases.org/?p=900), [IntechOpen chapter](https://intechopen.com/chapters/65079), [MedGen](https://ncbi.nlm.nih.gov/medgen/C0340007).

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 5 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

3 of 8 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.