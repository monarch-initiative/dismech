---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-26T23:33:53.335246'
end_time: '2026-09-26T23:37:20.241392'
duration_seconds: 206.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 53
  mondo_id: MONDO:0012380
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
  web_search_requests: 9
  num_turns: 23
  total_cost_usd: 1.3843918
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 8
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:15958501
  relevance_assessed: 3
  on_topic: 3
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 10
  verified: 9
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0012380
    reported_labels:
    - MONDO
    - OLS
    ontology_label: autosomal dominant nonsyndromic hearing loss 53
  - term_id: UBERON:0001846
    reported_labels:
    - cochlea
    ontology_label: internal ear
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 53
- **MONDO ID:** MONDO:0012380 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 53** covering all of the
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

I'll research this condition using primary literature sources before writing the report, given the rigor this is meant to support.

# Research Report: Autosomal Dominant Nonsyndromic Hearing Loss 53 (DFNA53)

## Summary Framing (read first)

DFNA53 is not a well-characterized clinical entity with an established molecular mechanism — it is a **single-family, locus-only mapping result** published once, in 2006, with no subsequent replication, no identified causal gene, and no follow-up literature in the intervening ~20 years (confirmed by repeated literature searches through September 2026, including the current hereditaryhearingloss.org locus table and a 2023 comprehensive DFNA review, neither of which lists a gene for this locus). Consequently, most of the mechanistic, molecular, model-organism, and treatment sections below are genuinely inapplicable or unknown, and are marked as such rather than filled with inferred or generic content. This is the honest, sourced state of the literature, not a gap in this search.

---

## 1. Disease Information

**Overview.** DFNA53 designates an autosomal dominant, nonsyndromic (isolated) sensorineural hearing loss locus mapped to human chromosome **14q11.2–q12** in a single large, multigenerational Chinese family. The phenotype is postlingual (onset in adolescence/the second decade of life), begins as high-frequency hearing loss, and progresses to involve all frequencies, reaching a profound degree by the fourth–fifth decade of life (Yan et al., 2006, PMID:[15958501](https://pubmed.ncbi.nlm.nih.gov/15958501/); Aldè et al. 2023, PMC:[PMC10296186](https://pmc.ncbi.nlm.nih.gov/articles/PMC10296186/)).

> "post-lingual, high frequency hearing loss that progresses to involve all frequencies" — Yan D et al., *J Med Genet* 2006;43(2):170-174.

> "HL is initially mild and limited to high frequencies but gradually involves all frequencies and progresses to a profound degree by the 4th/5th decade of life." — Aldè et al., *Audiology Research* 2023 (DFNA locus table entry for DFNA53).

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM | [#609965](https://omim.org/entry/609965) — DEAFNESS, AUTOSOMAL DOMINANT 53; DFNA53 |
| MONDO | MONDO:0012380 |
| MedGen | C1864957 (NCBI GTR: [C1864957](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1864957/)) |
| GARD (NIH rare disease) | GARD ID 9934 |
| Locus | 14q11.2–q12 |
| Gene | **Not identified** |

**Synonyms:** Deafness, autosomal dominant 53; autosomal dominant nonsyndromic deafness 53; autosomal dominant nonsyndromic hearing loss 53.

**Data provenance.** All disease-level information available for DFNA53 derives from a single aggregated genetic-mapping study of one family (a case series/pedigree study), not from EHR-derived or population-registry data. There is no disease registry, no epidemiologic surveillance record, and no subsequent replication cohort.

---

## 2. Etiology

- **Disease causal factor:** Presumed to be a single dominant (heterozygous) germline variant in an as-yet-unidentified gene within the 14q11.2–q12 interval, based on autosomal dominant segregation with a maximum multipoint LOD score of 5.4 at marker D14S1280 (PMID:15958501).
- **Genetic risk factors:** Inheriting the disease haplotype from an affected parent; no specific variant, susceptibility locus, or modifier gene has been reported.
- **Environmental risk factors:** None reported or investigated for this locus; no environmental co-factor has been described in the single published family.
- **Protective factors:** Not studied.
- **Gene–environment interaction:** Not studied. No data exist to assess this axis for DFNA53 specifically.

Candidate genes within the mapped interval that were explicitly **excluded** by direct screening in the original family are:
- **COCH** (the DFNA9 gene, HGNC:2180) — the DFNA53 critical region contains the COCH locus, but sequencing did not identify a causative variant.
- **BOCT / SLC22A17**
- **EFS**
- **HSPC156 / STXBP6**

> "the critical region for DFNA53 contains the gene for DFNA9 [COCH] but does not overlap with the regions for DFNB5, DFNA23, or DFNB35... screening of the COCH gene, BOCT (SLC22A17), EFS, and HSPC156 (STXBP6) within the DFNA53 interval did not identify the cause for deafness in this family" (Yan et al. 2006, PMID:15958501).

---

## 3. Phenotypes

Because only one family has been reported, phenotype "frequency" data (e.g., % of patients with a feature) does not exist in the population-genetics sense — the figures below describe the single pedigree's clinical course as reported.

| Phenotype | HPO suggestion | Onset | Course | Notes |
|---|---|---|---|---|
| Postlingual sensorineural hearing loss | HP:0008619 (Bilateral sensorineural hearing impairment) / HP:0000407 (Sensorineural hearing impairment) | Adolescence, second decade of life | Progressive | Initial presentation |
| High-frequency-predominant hearing loss | HP:0000407 combined with a sloping-configuration descriptor; no dedicated HPO term for "sloping audiogram" beyond general SNHL terms | Onset | Evolves | Sloping audiometric configuration at onset |
| Progression to all-frequency, profound deafness | HP:0008625 (Bilateral profound sensorineural hearing impairment) | 4th–5th decade | End-stage | Progresses from high-frequency to pantonal loss |

- **Phenotype type:** Sensorineural hearing impairment (a clinical sign/laboratory-audiometric abnormality), not a syndromic constellation — the entry is explicitly "nonsyndromic," meaning no other organ system involvement was reported in the affected family.
- **Severity/progression:** Progressive, sloping-to-flat/profound audiometric configuration, consistent with many other DFNA loci (Aldè et al. 2023, PMC10296186).
- **Vestibular function:** The original 2006 report does not describe vestibular testing or vestibular symptoms. A downstream NCBI GTR/MedGen record lists "abnormal vestibular function" as an associated clinical feature for this condition, but this could not be traced to a specific statement in the primary Yan et al. paper during this search — **flag this as an unverified, database-level tag rather than a confirmed primary-literature finding**, and it should not be curated as evidence without independent confirmation.
- **Quality of life impact:** Not studied for this specific family; no disease-specific QOL instrument data exist.

---

## 4. Genetic/Molecular Information

- **Causal gene:** **Unknown.** No gene has been identified for DFNA53 in the ~20 years since the locus was mapped (confirmed by the current hereditaryhearingloss.org DFNA locus table, which lists DFNA53 as "gene unknown," and by the absence of any subsequent primary literature identifying a causal gene).
- **Locus:** 14q11.2–q12, a 9.6 cM interval bounded by microsatellite markers **D14S581** and **D14S1021**, with peak linkage (multipoint LOD 5.4) at **D14S1280** (PMID:15958501).
- **Variant classification/type/allele frequency/somatic-vs-germline/functional consequence:** Not applicable — no variant has been reported.
- **Modifier genes, epigenetic information, chromosomal abnormalities:** None reported.
- **Relationship to other loci on 14q:** Four other deafness loci map to the long arm of chromosome 14 — **DFNA9** (COCH, sits inside the DFNA53 critical region but was excluded as causal), **DFNA23**, **DFNB5**, and **DFNB35** — but the DFNA53 interval does not overlap the latter three (PMID:15958501). This makes DFNA53 genetically and physically distinct from its chromosome-14 neighbors even though it spatially contains the COCH gene.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been reported or investigated in connection with DFNA53. As a monogenic, single-family, autosomal dominant mapping result, there is no literature addressing gene–environment modulation of this specific locus.

---

## 6. Mechanism / Pathophysiology

**No mechanism can be constructed for DFNA53 with any specificity, because the causal gene is unknown.** A causal chain cannot be drawn beyond the top-level genetic statement, and any lower step would be an inference from the general biology of nonsyndromic hearing loss rather than a demonstrated fact about this locus. Presenting a plausible-looking pathway here would misrepresent the state of evidence, so only the following is offered:

1. A dominant germline variant at an unidentified gene in 14q11.2–q12 is inferred to disrupt inner-ear (most likely cochlear) structure or function — **inferred, not demonstrated**, from the clinical phenotype (progressive high-frequency-onset SNHL) by analogy to other DFNA loci with a similar audiometric trajectory.
2. This putative dysfunction is inferred to initially and preferentially affect basal-turn (high-frequency-coding) cochlear hair cells or their supporting structures, given the high-frequency-first audiometric pattern — again **inferred by analogy**, not shown directly for this locus.
3. Progression to pantonal, profound loss by the 4th–5th decade suggests a slowly progressive degenerative process rather than a static congenital lesion — **inferred from the clinical course alone.**

No molecular pathway, cellular process, protein dysfunction, metabolic change, immune involvement, tissue-damage mechanism, biochemical abnormality, epigenetic change, or any -omics profiling (transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial) has been reported for DFNA53, because the causal gene — and therefore any tissue or cellular substrate to study — has never been identified. No GO or CL term can be responsibly assigned to a specific mechanistic step for this entry without fabricating specificity the source does not support.

---

## 7. Anatomical Structures Affected

- **Organ level:** Inner ear (cochlea) — the only organ system reported as affected, consistent with the "nonsyndromic" designation (no other organ involvement reported). Body system: auditory/sensory (and, per the caveated GTR vestibular tag in §3, possibly vestibular — unconfirmed).
- **Anatomical term (UBERON):** UBERON:0001846 (cochlea) is the most specific defensible anatomical anchor, since no cell-type-specific or subcellular-level finding has been reported.
- **Tissue/cell/subcellular level:** No specific cell population (e.g., outer vs. inner hair cells, stria vascularis, spiral ganglion) or organelle has been implicated by any study — this would need to be inferred from a mechanism that does not yet exist for this locus (see §6).
- **Laterality:** Bilateral, based on standard DFNA convention and the "sensorineural hearing impairment" HPO/GTR coding (bilateral is the default assumption for nonsyndromic genetic SNHL loci; not separately confirmed as bilateral vs. asymmetric in the primary paper's abstract).

---

## 8. Temporal Development

- **Onset:** Postlingual, adolescence/second decade of life (PMID:15958501; Aldè et al. 2023).
- **Onset pattern:** Insidious, not acute.
- **Progression:** Progressive — initially mild, limited to high frequencies; gradually involves all frequencies; reaches profound severity by the 4th–5th decade of life (Aldè et al. 2023, PMC10296186).
- **Disease course pattern:** Progressive, not episodic or relapsing-remitting; no data on plateaus or stable phases.
- **Remission:** None reported (progressive sensorineural hearing loss of this type is not expected to remit).
- **Critical periods:** Not established — no data on a window during which intervention alters outcome, though for any progressive postlingual SNHL, earlier identification of decline would generally be presumed clinically useful (a general inference, not DFNA53-specific evidence).

---

## 9. Inheritance and Population

- **Epidemiology:** No prevalence or incidence estimate exists for DFNA53 specifically. It has been reported in exactly one family; DFNA loci collectively account for only a minority (roughly 20%) of hereditary nonsyndromic hearing loss, but no locus-specific frequency figure is available for DFNA53 (general DFNA-class context from Aldè et al. 2023, not DFNA53-specific).
- **Inheritance pattern:** Autosomal dominant, based on classic segregation of the phenotype with the 14q11.2-q12 haplotype across multiple generations, with a maximum multipoint LOD score of 5.4 (PMID:15958501).
- **Penetrance:** Not explicitly quantified in the abstract; the family structure implies high (if not complete) penetrance sufficient to generate a LOD score of 5.4, but no numeric penetrance estimate has been published.
- **Expressivity, anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency:** None reported/applicable — these require either multiple pedigrees or population data, neither of which exists for this single-family locus.
- **Population demographics:** The single reported family is Chinese (Han Chinese, presumptively, based on recruitment context, though ethnicity beyond "Chinese family" is not further specified in the abstract). No other population, geographic distribution, sex ratio, or age-distribution data exist.

---

## 10. Diagnostics

No DFNA53-specific diagnostic test, biomarker, imaging finding, or histopathology has been described (there is no known gene to target with a single-gene or panel-based clinical test). General, non-locus-specific guidance applicable to any postlingual progressive autosomal dominant SNHL family would include:

- **Audiometry:** Pure-tone audiometry to document the sloping-to-flat/pantonal progressive configuration — the primary phenotyping tool used in the original family study.
- **Genetic testing (general, not DFNA53-specific):** Because no causal gene is known, a clinical multi-gene hereditary hearing loss panel or exome/genome sequencing would not currently include a targeted DFNA53 assay; family-specific linkage analysis (as performed in the original 2006 study, using markers such as D14S581, D14S1280, D14S1021) would be the only way to test for co-segregation with this specific chromosomal region in a *new* large family, but this is a research approach, not a clinical diagnostic offering.
- **Differential diagnosis:** Other chromosome 14 DFNA loci in the region (DFNA9/COCH) should be excluded by direct gene sequencing before considering a novel-locus mapping study, exactly as was done in the original report.
- **Screening:** No population or newborn screening applies to this ultra-rare, single-family locus.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Not applicable — nonsyndromic hearing loss does not affect survival; no mortality data exist or would be expected.
- **Morbidity/function:** Progressive profound sensorineural hearing loss by the 4th–5th decade would be expected to significantly affect communication function and quality of life, by general analogy to other progressive DFNA phenotypes, but no disease-specific functional-outcome or QOL data have been published for DFNA53.
- **Complications:** None reported beyond the hearing loss itself (nonsyndromic — no other organ complications documented).
- **Prognostic factors/biomarkers:** None established.

---

## 12. Treatment

No DFNA53-specific treatment or gene-targeted therapy exists (there is no identified gene to target). Management would follow the standard, non-locus-specific approach to progressive sensorineural hearing loss:

- **Amplification:** Hearing aids as high-frequency loss becomes functionally significant — NCIT term candidate: `NCIT:C-hearing aid` device concept would be bound as a **device**, not a `TreatmentTerm` action, per standard NCIT device-vs-action handling (analogous devices are typically bound via the clinical-action + qualifiers pattern, e.g., "hearing aid fitting" bound to a general audiologic-rehabilitation action term with the device carried as a qualifier).
- **Cochlear implantation:** Would be the standard intervention once loss progresses to a profound, aid-non-responsive level, following the general clinical pathway used for other progressive genetic SNHL loci — NCIT:C15329 (Surgical Procedure) is the appropriate clinical-action anchor for the implantation itself, per standard dismech convention for device-based interventions.
- **Audiologic rehabilitation/speech-language therapy:** Standard supportive care for progressive hearing loss — NCIT:C15302 (Physical Therapy)/NCIT:C159273 (Speech Language Therapy) analogs, as used generically across other DFNA entries.
- **Genetic counseling:** NCIT:C15240 (Genetic Counseling), given the confirmed autosomal dominant inheritance and 50% offspring recurrence risk (GARD summary).
- **Gene therapy, RNA-based therapy, targeted/precision therapy:** Not applicable — no target gene exists to develop a molecular therapeutic against.
- **Clinical trials:** No DFNA53-specific trial was found on ClinicalTrials.gov in this search.

All of the above is general standard-of-care inference for progressive nonsyndromic SNHL, not evidence specific to DFNA53, and should be labeled as such in any curation use.

---

## 13. Prevention

No DFNA53-specific primary, secondary, or tertiary prevention strategy exists. Standard genetic-counseling-based family planning guidance (informing at-risk relatives of the 50% autosomal dominant recurrence risk) is the only prevention-adjacent measure supported by the available literature (GARD summary page).

---

## 14. Other Species / Natural Disease

Not applicable/not available. Because the causal gene is unknown, no ortholog, veterinary correlate, or naturally occurring animal disease can be identified or excluded for DFNA53.

---

## 15. Model Organisms

**None exist.** With no causal gene identified, there is no mouse, zebrafish, or other genetic model of DFNA53, no knockout/knock-in resource, and no functional-genomics screen targeting this locus. This is a direct consequence of the locus never having been resolved to a gene, not a gap in searching.

---

## Curation Guidance / Caveats for KB Use

1. **This is a locus-only OMIM entry with no gene.** Any dismech `genetic:` block should record the 14q11.2–q12 locus context in `notes`, but should **not** invent a `gene_term` binding — there is none to bind.
2. **Single-family evidence.** Every clinical/phenotypic claim above traces to one 2006 paper describing one pedigree. Treat prevalence, penetrance, and phenotype-frequency claims accordingly — there is no population-level denominator.
3. **The "abnormal vestibular function" GTR/MedGen tag is flagged, not confirmed.** Do not cite it as primary-literature evidence without independently verifying it against the full OMIM clinical synopsis or original paper (this search could not access the full OMIM clinical synopsis due to a site-side block).
4. **No mechanism section should be written with GO/CL specificity** for this entry beyond the caveated inferences in §6 — doing so would fabricate a mechanistic claim the source literature does not support.
5. Per dismech's evidence policy, only PMID:15958501 (and the general-DFNA-context review PMC10296186, cited separately and clearly as general context) should be used as sources; no other primary literature on DFNA53 was found to exist as of this search (September 2026).

---

## Sources

- [A novel locus for autosomal dominant non-syndromic deafness, DFNA53, maps to chromosome 14q11.2-q12 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/15958501/) — Yan D, Ke X, Blanton SH, Ouyang XM, Pandya A, Du LL, Nance WE, Liu XZ. *J Med Genet.* 2006 Feb;43(2):170-4. PMID:15958501.
- [A novel locus for autosomal dominant non‐syndromic deafness, DFNA53, maps to chromosome 14q11.2‐q12 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2564639/)
- [OMIM #609965 — DEAFNESS, AUTOSOMAL DOMINANT 53; DFNA53](https://omim.org/entry/609965)
- [Autosomal Dominant Non-Syndromic Hearing Loss (DFNA): A Comprehensive Narrative Review (PMC10296186)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10296186/) — Aldè M, Cantarella G, Zanetti D, Pignataro L, La Mantia I, et al. *Audiology Research* 2023;13(6):1616 (used only for general DFNA-class context and the DFNA53 locus-table entry).
- [Hereditary Hearing Loss Homepage — Autosomal Dominant Nonsyndromic Hearing Loss table](https://hereditaryhearingloss.org/dominant)
- [GARD — Autosomal dominant nonsyndromic hearing loss 53](https://rarediseases.info.nih.gov/diseases/9934/autosomal-dominant-nonsyndromic-hearing-loss-53)
- [NCBI GTR — Autosomal dominant nonsyndromic hearing loss 53 (MedGen C1864957)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1864957/)
- [MONDO:0012380 (OLS)](https://www.ebi.ac.uk/ols4/ontologies/mondo/entities/http://purl.obolibrary.org/obo/MONDO_0012380)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:15958501`: "the critical region for DFNA53 contains the gene for DFNA9 [COCH] but does not overlap with the regions for DFNB5, DFNA23, or DFNB35... screening of the COCH gene, BOCT (SLC22A17), EFS, and HSPC156 (STXBP6) within the DFNA53 interval did not identify the cause for deafness in this family"
  - closest text in source: "The critical region for DFNA53 contains the gene for DFNA9 but does not overlap with the regions for DFNB5, DFNA23, or DFNB35"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012380` (4 mentions) - the report calls it "MONDO", "OLS"; MONDO calls it **autosomal dominant nonsyndromic hearing loss 53**
- `UBERON:0001846` (1 mention) - the report calls it "cochlea"; UBERON calls it **internal ear**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008625` (1 mention) - the report calls it "Bilateral profound sensorineural hearing impairment"; HP calls it **Severe sensorineural hearing impairment**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0012380` - called "MONDO", "OLS"