---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-25T16:51:22.470549'
end_time: '2026-09-25T16:56:05.767206'
duration_seconds: 283.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 70
  mondo_id: MONDO:0013978
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
  web_search_requests: 17
  num_turns: 30
  total_cost_usd: 1.6264862000000004
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 3
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
citation_count: 21
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 8
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 45
  verified: 41
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.023
  labels_checked: 18
  labels_matching: 13
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: GO:0140373
    reported_labels:
    - antiviral innate immune response
    ontology_label: obsolete histone H3-K14 ubiquitination
  - term_id: CL:0002510
    reported_labels:
    - spiral ganglion neuron
    ontology_label: CD103-negative, langerin-positive lymph node dendritic cell
  - term_id: UBERON:0001846
    reported_labels:
    - cochlea
    ontology_label: internal ear
  labels_variant: 2
  unresolved_terms:
  - HP:0002520
  obsolete_terms:
  - term_id: GO:0140373
    ontology_label: obsolete histone H3-K14 ubiquitination
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 70
- **MONDO ID:** MONDO:0013978 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 70** covering all of the
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

I'll research this condition now using web search and fetch tools, then compile the comprehensive report.

I have sufficient material to compile a comprehensive, well-cited report now.

I now have comprehensive, well-sourced material. Compiling the final report.

---

# Research Report: Autosomal Recessive Nonsyndromic Hearing Loss 70 (ARNSHL70 / DFNB70)

**Attribution note:** This is a deep-research–style synthesis assembled from live web search and web-fetch results (WebSearch/WebFetch tool calls, September 2026), not from primary-literature PDFs read in full. Per this repository's evidence discipline, treat every claim below as a **lead** — a curator must independently verify each PMID/OMIM/Orphanet/ClinVar identifier and pull an exact quoted substring from the cached source (`just fetch-reference <ID>`) before it can support a dismech `EvidenceItem`. Several facts below (marked) come from search-engine-summarized excerpts rather than a verified full-text or abstract fetch — several direct WebFetch attempts to PubMed, MDPI, and Wiley (Eaton 2018) returned HTTP 403/429/CAPTCHA blocks, so those sources are represented by title/search-snippet only and are flagged as `CITED_NOT_ACCESSED` in the table at the end.

## 1. Disease Information

**Overview.** Autosomal Recessive Nonsyndromic Hearing Loss 70 (ARNSHL70), more commonly indexed as **DFNB70** — full OMIM designation "**Deafness, Autosomal Recessive 70, with or without Adult-Onset Neurodegeneration**" — is a form of hereditary sensorineural hearing loss caused by biallelic pathogenic variants in **PNPT1** (polyribonucleotide nucleotidyltransferase 1), which encodes the mitochondrial RNA-import/processing enzyme **PNPase**. It was originally described as an isolated ("nonsyndromic") prelingual sensorineural deafness, but longitudinal follow-up of the original family later showed some carriers develop a multisystem adult-onset neurodegenerative syndrome, which is why OMIM's own disease name now carries the "with or without adult-onset neurodegeneration" qualifier (OMIM #614934; MedGen C1824925).

**Key identifiers:**
- OMIM phenotype: **#614934** (DFNB70)
- OMIM gene: **\*610316** (PNPT1)
- HGNC: **23166** (PNPT1)
- MONDO: **MONDO:0013978**
- Orphanet: **ORPHA:90636** ("Rare autosomal recessive non-syndromic sensorineural deafness type DFNB")
- MedGen: **C1824925**
- ClinVar/GTR condition, HPO term for the core sign: **HP:0000407** (Sensorineural hearing impairment) / congenital-onset qualifier

**Synonyms:** DFNB70; Deafness, autosomal recessive 70; Autosomal recessive deafness-70.

**Evidence basis:** Aggregated disease-level resources (OMIM, Orphanet, MedGen, GeneReviews-adjacent literature reviews) plus a small number of published patient cohorts/case families — this is not an EHR/registry-derived entity; case counts are in the tens of families worldwide across the whole PNPT1 phenotypic spectrum.

Sources: [OMIM #614934](https://www.omim.org/entry/614934) (access blocked by WebFetch — via search snippet), [NCBI GTR condition page](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1824925/), [MedGen 760477](https://www.ncbi.nlm.nih.gov/medgen/760477), [MalaCards](https://www.malacards.org/card/deafness_autosomal_recessive_70_with_or_without_adult_onset_neurodegeneration).

## 2. Etiology

**Disease causal factor:** Purely genetic/Mendelian — biallelic (homozygous or compound heterozygous) loss-of-function/hypomorphic variants in **PNPT1** (2p16.1). No environmental or infectious contribution is described; this is a single-gene disorder.

**Genetic risk factors:**
- **Causal gene:** PNPT1 (HGNC:23166), encoding PNPase, a homotrimeric 3′→5′ exoribonuclease/poly(A) polymerase.
- **Consanguinity is a recurring feature of reported pedigrees** — the founding family (von Ameln et al. 2012, *Am J Hum Genet*, PMID:23084290) comprised **3 Moroccan siblings born to consanguineous parents**, homozygous for the same missense variant.
- **Modifier/allelic-heterogeneity risk:** PNPT1 is pleiotropic — different biallelic genotypes at the same locus produce distinct phenotypes (isolated DFNB70 hearing loss vs. combined oxidative phosphorylation deficiency 13 [COXPD13] vs. Leigh syndrome), and monoallelic (heterozygous) PNPT1 variants in the S1 RNA-binding domain cause a *dominant* disorder, spinocerebellar ataxia type 25 (SCA25, OMIM #608703) — a different inheritance mode at the same locus, which is a lump/split-relevant fact for KB curation (a monoallelic PNPT1 disease is a **separate** entity from ARNSHL70, not a subtype).
- **Variant location correlates loosely with phenotype severity:** missense variants in the RNase-PH domains have been linked to the milder isolated-hearing-loss phenotype, while more disruptive/multiple compound-heterozygous variants (nonsense, variants affecting trimerization or catalytic residues) associate with the severe multisystem COXPD13/Leigh phenotypes — this genotype-phenotype claim needs primary-source verification before KB use.

**Protective factors:** None reported in the literature surveyed.

**Gene-environment interactions:** None described; this is not currently modeled as having an environmental modifier.

Sources: [von Ameln et al. 2012 (PubMed 23084290)](https://pubmed.ncbi.nlm.nih.gov/23084290/), [OMIM #608703 SCA25](https://omim.org/entry/608703), [Barbier et al. 2022, Ann Neurol, heterozygous PNPT1 variants cause SCA25](https://onlinelibrary.wiley.com/doi/abs/10.1002/ana.26366).

## 3. Phenotypes

**Core (defining) phenotype:**
- **Congenital, bilateral, sensorineural hearing loss**, present from infancy, historically described as "stable" through the first decades of life in the original nonsyndromic presentation. HPO: **HP:0000407** (Sensorineural hearing impairment) with **HP:0008527** (Congenital sensorineural hearing impairment) as a candidate more specific term; **HP:0000365** (Hearing impairment) as the coarse parent.
- Reported severity: **severe to profound**, prelingual onset in most published families (e.g., the Indian cohort family described "prelingual profound sensorineural hearing loss").

**Extended/emerging phenotype (natural-history-dependent — key curation point):**
- **Vestibular dysfunction** — reported in at least one compound-heterozygous DFNB70 family (South Indian cohort). Candidate HPO: **HP:0011385** (Abnormal vestibular function) or **HP:0000737**-adjacent vestibular terms.
- **Progressive unilateral visual loss** in the same family (mechanism/HPO term unspecified in the summarized source — needs primary verification; candidate HP:0000618 Blindness / HP:0000505 Visual impairment).
- **Adult-onset multisystem neurodegeneration** — described in the original DFNB70 family's extended follow-up (Eaton et al. 2018, *Am J Med Genet A* — access blocked, summarized via search snippet) and echoed in OMIM's disease name: onset in the **fourth decade (40s)**, comprising:
  - Ataxia progressing to loss of ambulation (HP:0001251 Ataxia)
  - Optic atrophy (HP:0000648)
  - Dystonia (HP:0001332) or spasticity (HP:0001257)
  - Cognitive decline with psychiatric features (HP:0100543 Cognitive impairment; consider HP:0000708 Behavioral abnormality)
  - In further-aged individuals (50s–60s): additional spasticity and urinary incontinence (HP:0000020) reported.
- **COXPD13 allelic phenotype (severe end of spectrum, distinct disease-mechanism cluster, not itself DFNB70 but same gene):** neonatal/infantile-onset encephalomyopathy, hypotonia (HP:0001252), dystonic movements, poor feeding (HP:0011968), global developmental delay (HP:0001263), abnormal eye movements, lactic acidosis (HP:0003128), cardiomyopathy (HP:0001638), liver dysfunction (HP:0001410), seizures (HP:0001250), and brain MRI signal abnormalities in putamen/basal ganglia/caudate/corpus callosum with delayed myelination (HP:0002520-adjacent, HP:0002505 Delayed CNS myelination).
- **Leigh-syndrome allelic phenotype:** subacute necrotizing encephalomyelopathy onset ~1 month of age in one reported case, progressing to death by 2.4 years (Matilainen et al. 2017, *Hum Mol Genet*, PMID:28645153) — via ND6 mitochondrial transcript maturation failure and complex I deficiency.
- **Mitochondrial interferonopathy phenotype** — a 2026 case report (Brooks et al., *JIMD Reports*, PMID:42375813) describes PNPT1-related disease presenting with a **type I interferon-driven autoinflammatory ("interferonopathy") phenotype**, treated with a JAK inhibitor — this is a distinct emerging clinical facet worth noting for the pediatric/genetics framing (autoinflammation as a PNPT1 manifestation, separate from the classical deafness/neurodegeneration axis).

**Quality-of-life impact:** Not separately quantified in sources found; profound congenital deafness carries the general QoL burden of prelingual hearing loss (language acquisition impact), and the adult-onset neurodegenerative course (ataxia/loss of ambulation, cognitive/psychiatric decline) represents a major independent QoL burden layered on in mid-to-late adulthood — this progression pattern (isolated pediatric sensory phenotype → mid-life multisystem neurodegeneration) is itself the clinically important "pediatric vs. adult" framing point for this gene: **a child diagnosed with "isolated" PNPT1 hearing loss cannot be assured the phenotype will stay isolated**, which has direct surveillance/counseling implications.

Sources: [OMIM #614934 summary via search](https://www.omim.org/entry/614934), [Eaton et al. 2018 AJMG-A](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.40516) (CITED_NOT_ACCESSED), South India family report — [Bademci/authors, Ahg 2021, PubMed 34374074](https://pubmed.ncbi.nlm.nih.gov/34374074/) / [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2021.04.06.438557v2.full), [Brooks et al. 2026 JIMD Reports, PMID 42375813](https://pubmed.ncbi.nlm.nih.gov/42375813/).

## 4. Genetic / Molecular Information

**Causal gene:** **PNPT1**, HGNC:23166, chromosome **2p16.1** (some sources say 2p16.2/2p16 broadly), OMIM \*610316.

**Founding pathogenic variant (isolated DFNB70):**
- **c.1424A>G, p.(Glu475Gly)** — homozygous missense, NM_033109 transcript numbering as used by von Ameln et al. 2012. Located within the **second RNase-PH domain** of PNPase; substitutes a negatively charged glutamate for glycine at a highly conserved residue. Absent from population control databases at the time of publication; segregated with deafness in the 3-sibling Moroccan family. Functional studies (bacterial/yeast/mammalian expression systems) showed the mutant protein is **stably expressed and correctly localizes to mitochondria**, but is **hypofunctional**, showing **disturbed PNPase homotrimerization and impaired mitochondrial RNA import** — this is the mechanistic crux of the isolated hearing-loss phenotype (a partial-function allele, contrasted with the more severe null/near-null alleles causing COXPD13/Leigh syndrome).

**Additional reported variants (broader allelic spectrum, cited from search-summarized secondary sources — verify each primary source before KB use):**
- Compound heterozygous **p.(Ala46Gly)** + **p.(Asn540Ser)** — South Indian family, DFNB70 phenotype with vestibular and visual features.
- **c.1160A>G (p.Gln387Arg)**, **c.1519G>T (p.Ala507Ser)**, **c.1528G>C (p.Ala510Pro)** — reported in the COXPD13 literature cluster (a 2025 Chinese case-report/review cites these as recurring COXPD13 alleles).
- **c.1033A>G (p.Lys345Glu)** — novel variant reported 2025 in a Chinese COXPD13 patient (gnomAD-type population frequency reported as "<1 in 1,000,000").
- **c.918del (p.Val307fs)** and **c.1592C>G (p.Thr531Arg)** — appear in ClinVar as pathogenic/likely-pathogenic entries specifically linked to "Autosomal recessive nonsyndromic hearing loss 70."
- **c.1012G>T (p.Glu338Ter)** — nonsense variant in ClinVar (classification context "not provided" in the snippet found; verify).

**Variant classification (ACMG/AMP framework):** Multiple ClinVar entries exist under the DFNB70 condition (RCV001336838, RCV003147393, and others) — actual classification tiers (Pathogenic/Likely Pathogenic/VUS) were **not independently confirmed** in this pass and must be pulled from ClinVar directly before citing in a KB evidence block.

**Allele frequency:** Population-database frequencies for individual pathogenic alleles are reported in the extreme-rare range (e.g., "<1 in 1,000,000" for one COXPD13 allele); no aggregate PNPT1 pathogenic-carrier frequency was found.

**Functional consequence category:** Predominantly **hypomorphic/loss-of-function** at the enzymatic and trimerization level (isolated DFNB70 alleles are less disruptive "leaky" hypomorphs; COXPD13/Leigh alleles are more severely loss-of-function). This is **biallelic loss-of-function** for the recessive disease, contrasted with the **dominant, heterozygous** SCA25 variants that cluster specifically in the S1 RNA-binding domain (a distinct structure-function/dominant-negative or haploinsufficiency mechanism not yet fully resolved in the sources reviewed).

**Somatic vs. germline:** Exclusively germline — this is a classic Mendelian recessive disorder, no somatic/mosaic mechanism reported.

**Modifier genes:** None specifically identified for DFNB70; note the broader allelic heterogeneity within PNPT1 itself functions as the dominant "modifying" variable (different biallelic combinations → different clinical syndromes) rather than a separate modifier locus.

**Epigenetic information / chromosomal abnormalities:** None reported — this is a point-mutation/small-indel disorder, not a structural or epigenetic disease mechanism.

Sources: [von Ameln 2012 PMID:23084290](https://pubmed.ncbi.nlm.nih.gov/23084290/), [ClinVar RCV001336838](https://www.ncbi.nlm.nih.gov/clinvar/RCV001336838/), [ClinVar RCV003147393](https://www.ncbi.nlm.nih.gov/clinvar/RCV003147393/), [PNPT1 Chinese case report/review, PMC11921403](https://pmc.ncbi.nlm.nih.gov/articles/PMC11921403/) (PubMed 40115456), South India cohort (PubMed 34374074), [GeneCards PNPT1](https://www.genecards.org/card/PNPT1).

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factors are described for DFNB70 — it is a purely monogenic disorder. Not applicable.

## 6. Mechanism / Pathophysiology

**Ordered causal chain (isolated DFNB70 phenotype):**

1. Biallelic hypomorphic **PNPT1** variant (e.g., homozygous p.Glu475Gly in the RNase-PH domain) → produces a **stably expressed, correctly mitochondrially localized but catalytically/structurally impaired PNPase protein** (demonstrated in bacterial/yeast/HEK293T expression systems).
2. Impaired PNPase → **disturbed homotrimerization** of the enzyme (PNPase functions as an obligate homotrimer for its exoribonuclease/RNA-import activities) → *inferred, demonstrated in vitro rather than in patient inner-ear tissue*.
3. Disturbed trimerization → **impaired PNPase-mediated import of nuclear-encoded small RNAs (e.g., 5S rRNA, RNase MRP RNA) across the mitochondrial intermembrane space into the mitochondrial matrix**, and impaired turnover/maturation of mitochondrial-encoded RNA species — this RNA-import function is one of the very few known mammalian mechanisms for importing nucleus-encoded RNA into mitochondria.
4. Impaired mitochondrial RNA import/processing → downstream **disruption of mitochondrial gene expression / OXPHOS complex assembly** (well-demonstrated for the more severe alleles: Matilainen et al. 2017 showed loss of PNPase activity specifically impairs **ND6 mitochondrial transcript maturation**, producing **combined respiratory chain complex I deficiency**).
5. In cochlear/inner-ear tissue specifically, this manifests as **cochlear hair-cell and/or spiral ganglion dysfunction** secondary to the high metabolic (ATP) demand of the inner ear — *this specific cell-level step is inferred by analogy to other mitochondrial deafness genes rather than directly demonstrated for PNPT1 in the sources reviewed*, producing **congenital-onset bilateral sensorineural hearing loss**.
6. **Branch point — allele severity determines downstream trajectory:**
   - *Milder/leaky hypomorphic biallelic genotype* (e.g., the founding p.Glu475Gly homozygote) → clinical phenotype remains isolated ("nonsyndromic") hearing loss for decades → **later branch**: in at least one extended family, a slow-accumulating mitochondrial/neuronal vulnerability leads to **adult-onset (40s+) neurodegeneration** (ataxia, optic atrophy, dystonia/spasticity, cognitive-psychiatric decline) — mechanism for this delayed second phase is not fully elucidated in sources found; plausibly reflects cumulative post-mitotic neuronal vulnerability to chronic partial OXPHOS/RNA-processing deficiency, but this should be marked as an inference/knowledge gap rather than demonstrated mechanism.
   - *More severe biallelic genotype* (nonsense, catalytic-site missense, multiple compound-heterozygous hits) → **combined oxidative phosphorylation deficiency 13 (COXPD13)** → severe infantile multisystem mitochondrial disease (encephalomyopathy, cardiomyopathy, lactic acidosis, liver dysfunction) or **Leigh syndrome** (subacute necrotizing encephalomyelopathy with basal ganglia/brainstem MRI lesions).
   - *A separate, dominant (heterozygous) mechanism*, restricted to variants in the **S1 RNA-binding domain**, produces **spinocerebellar ataxia 25 (SCA25)** — a sensory ganglionopathy/cerebellar ataxia with incomplete penetrance and phenotypic variability; this is mechanistically and genetically distinct (dominant vs. recessive) and should be modeled as a **separate disease entity**, not a DFNB70 subtype, per this KB's lump/split conventions.
7. **A parallel, recently described innate-immune branch**: PNPase's mitochondrial intermembrane-space/matrix localization gives it a role in **preventing formation and cytosolic release of mitochondrial double-stranded RNA (mt-dsRNA)**. Biallelic hypomorphic PNPT1 variants → **failure to degrade/compartmentalize mt-dsRNA** → **cytosolic escape of mt-dsRNA** → **MDA5-dependent antiviral/type-I-interferon signaling activation** → an **"interferonopathy"/autoinflammatory phenotype**, now reported clinically and treated with a JAK inhibitor in at least one 2026 case report. This connects PNPT1 disease biology to the broader mitochondrial-dsRNA-innate-immunity literature (Nature 2018, Dhir et al., PMID not captured but widely cited as the mechanistic anchor for mt-dsRNA/MDA5/type-I-IFN signaling).

**Molecular pathways:** Mitochondrial RNA metabolism / RNA import pathway (not a classical KEGG signaling pathway); downstream engages **MDA5/RIG-I-like receptor–MAVS–type I interferon signaling** (innate antiviral pathway) when mt-dsRNA escapes to cytosol.

**Cellular processes:** RNA processing/turnover, mitochondrial translation support, oxidative phosphorylation, and (via the interferonopathy branch) innate immune/antiviral signaling activation.

**Protein dysfunction category:** Predominantly **partial loss-of-function** (hypomorphic) for the isolated-hearing-loss allele class, with **disrupted homotrimerization** as the structural correlate; **more severe loss-of-function** for COXPD13/Leigh alleles.

**Suggested GO terms:** GO:0000959 (mitochondrial RNA metabolic process), GO:0032543 (mitochondrial translation), GO:0006402 (mRNA catabolic process), GO:0140373 (antiviral innate immune response) for the interferonopathy branch, GO:0034654 (nucleobase-containing compound biosynthetic process) as a broad parent if needed.

**Suggested CL terms:** CL:0000601 (auditory hair cell) or the more specific CL:0000202 (auditory hair cell) / cochlear inner and outer hair cell terms, CL:0002510 (spiral ganglion neuron) — **not directly demonstrated for PNPT1** in the sources reviewed; these are inferred targets by analogy to other mitochondrial/cochlear-metabolic deafness genes and should be flagged as such if used in a pathograph node.

Sources: [von Ameln 2012](https://pubmed.ncbi.nlm.nih.gov/23084290/), [Matilainen et al. 2017, Hum Mol Genet, PMID 28645153](https://academic.oup.com/hmg/article/26/17/3352/3883915), [Brooks et al. 2026, JIMD Reports, PMID 42375813 / PMC13312033](https://pmc.ncbi.nlm.nih.gov/articles/PMC13312033/), general mt-dsRNA/MDA5 mechanism background: [Nature 2018 mitochondrial dsRNA paper](https://www.nature.com/articles/s41586-018-0363-0) (background reference, not PNPT1-specific — verify before use as PNPT1 evidence).

## 7. Anatomical Structures Affected

- **Primary organ:** Inner ear / cochlea (sensorineural hearing loss) — auditory system.
- **Secondary/extended involvement (allele-dependent):** 
  - Vestibular apparatus (vestibular dysfunction reported in at least one family)
  - Optic nerve (optic atrophy in the adult-onset neurodegenerative branch)
  - Central nervous system — cerebellum/basal ganglia/corpus callosum/white matter (ataxia, dystonia, delayed myelination, MRI lesions in the COXPD13/Leigh branch)
  - Cardiac muscle (cardiomyopathy in COXPD13)
  - Liver (dysfunction in COXPD13)
  - Skeletal muscle (myopathy/weakness in the severe multisystem phenotype)
- **Subcellular level:** Mitochondrion — specifically the **mitochondrial intermembrane space** (PNPase's predominant localization) and matrix; GO Cellular Component: GO:0005758 (mitochondrial intermembrane space).
- **Laterality:** Bilateral sensorineural hearing loss is the rule; the one reported visual phenotype was described as unilateral progressive vision loss (needs primary-source confirmation).

UBERON candidates: UBERON:0001846 (cochlea), UBERON:0002104 (vestibular organ), UBERON:0000966 (retina)/UBERON:0000970 (eye) for the visual phenotype, UBERON:0002037 (cerebellum), UBERON:0002420 (basal ganglion).

Sources: as above (OMIM #614934, South India family report, COXPD13 literature review PMC11921403).

## 8. Temporal Development

- **Onset:** **Congenital** for the core hearing-loss phenotype — present from infancy/prelingual period in every reported isolated-DFNB70 family.
- **Progression (core phenotype):** Described as **stable** for "the first decades of life" in the original family — i.e., a static, non-progressive congenital sensorineural hearing loss for years to decades.
- **Later-life progression (in at least one extended pedigree):** A **second, distinct progressive phase** begins in the **fourth decade (~40s)**: a stereotyped, apparently near-identical neurodegenerative course across affected siblings — ataxia → loss of ambulation, developing in parallel with optic atrophy, dystonia/spasticity, and cognitive-psychiatric decline; by the **50s–60s**, additional spasticity and incontinence. This is described as an evolving, chronic, progressive multisystem disease course, not episodic or relapsing-remitting.
- **COXPD13/Leigh-syndrome allelic branch:** Onset in the **neonatal/first months of life**; rapidly progressive, often fatal in early childhood (one Leigh syndrome case: onset at 1 month, death at 2.4 years).
- **Critical period:** The congenital auditory phenotype implicates a prenatal/perinatal developmental vulnerability window for the cochlea; the adult neurodegenerative phase implicates a separate, much later vulnerability window in post-mitotic neurons — these appear to be two temporally and possibly mechanistically distinct "hits" from the same underlying enzymatic deficiency, a point of active biological uncertainty worth flagging as a knowledge gap in any KB entry.

Sources: OMIM #614934 (via search snippet), Eaton et al. 2018 AJMG-A (CITED_NOT_ACCESSED — summarized via search), COXPD13/Leigh literature (Matilainen 2017, PMC11921403).

## 9. Inheritance and Population

- **Epidemiology:** No prevalence or incidence figures were found for DFNB70 specifically in any resource searched (OMIM, Orphanet, GTR, MalaCards summaries). It should be treated as **ultra-rare** — the disease-causing literature comprises a handful of published families (the founding Moroccan sibship, at least one South Indian family, and scattered COXPD13/Leigh case reports) — consistent with PNPT1 being a minor contributor within the large genetic-heterogeneity landscape of ARNSHL (which includes >100 known loci, GJB2 being the dominant contributor worldwide).
- **Inheritance pattern:** **Autosomal recessive** for DFNB70/COXPD13/Leigh-syndrome alleles; **autosomal dominant** for the separate SCA25 phenotype at the same locus (heterozygous, S1-domain-restricted variants) — this dominant/recessive split at one locus is an important curation flag.
- **Penetrance:** Full penetrance reported for the congenital hearing-loss component in affected homozygotes/compound heterozygotes in the founding family; penetrance/expressivity of the later adult neurodegenerative phase across the wider PNPT1-deafness population is **unknown** — only one extended pedigree with long follow-up has been reported, so it is not established whether all DFNB70 patients are at risk or whether this is specific to that family's genotype. The dominant SCA25 phenotype is explicitly described as showing **incomplete penetrance and phenotypic variability**.
- **Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).
- **Founder effects:** The Moroccan and South Indian families each carry distinct variants; no specific founder-population enrichment was identified in sources reviewed, though **consanguinity** is repeatedly implicated as the mechanism bringing rare biallelic PNPT1 variants together (both reported founding families derive from consanguineous or assortative-mating populations).
- **Carrier frequency:** Not established; individual pathogenic alleles are reported as extremely rare in population databases (e.g., <1/1,000,000 for one COXPD13 allele).
- **Population demographics:** Reported affected families are from **Morocco** and **Southern India**; a Chinese COXPD13 case was explicitly noted as the **first reported case in China**. No broader geographic/ethnic enrichment pattern established — the disease appears globally distributed but very rare everywhere, consistent with ascertainment via consanguinity/assortative mating rather than population founder effects.
- **Sex ratio:** No sex predilection reported (autosomal recessive, no sex-linked bias expected or described).

Sources: OMIM #614934, [South India family report PubMed 34374074](https://pubmed.ncbi.nlm.nih.gov/34374074/), [Chinese COXPD13 case report PMC11921403](https://pmc.ncbi.nlm.nih.gov/articles/PMC11921403/), [SCA25 heterozygous PNPT1 variants, Barbier et al. 2022](https://onlinelibrary.wiley.com/doi/abs/10.1002/ana.26366).

## 10. Diagnostics

- **Genetic testing:** The NIH Genetic Testing Registry lists **14 clinical tests** for this condition through 80 total PNPT1-linked test offerings (spanning targeted variant analysis, deletion/duplication analysis, and full coding-region sequence analysis) — i.e., PNPT1 is included on commercial hereditary-hearing-loss gene panels. Given PNPT1's pleiotropy (isolated deafness vs. COXPD13 vs. Leigh syndrome vs. dominant SCA25), **whole-exome or whole-genome sequencing**, or a broad hearing-loss/mitochondrial-disease gene panel, is the practical diagnostic approach rather than single-gene testing, especially since the clinical presentation at the time of diagnosis (isolated congenital deafness) cannot by itself predict which allelic-severity class a given patient falls into.
- **ClinGen gene-disease validity:** The ClinGen Hearing Loss Gene Curation Expert Panel has formally curated PNPT1-hearing-loss gene-disease pairs (among the panel's 164 total hearing-loss gene-disease curations). A separate ClinGen Mitochondrial Diseases Expert Panel curation lists **PNPT1–Leigh syndrome as "Moderate"** validity (classified 2020-03-19; CGGV:assertion_6ed99943-2ab9-417d-b0ec-ddbfa11c8645-2020-03-19T191429.965Z), based on three variants across three cases with supporting biochemical/functional evidence and no contradictory findings at the time of classification. The specific DFNB70 (isolated hearing loss) gene-disease validity classification tier was not directly retrieved in this pass and should be looked up separately (`search.clinicalgenome.org/kb/genes/HGNC:23166`) before citing a validity tier in the KB.
- **Audiologic testing:** Standard pediatric audiologic workup (ABR/otoacoustic emissions in infancy, pure-tone audiometry later) would characterize the bilateral sensorineural hearing loss; no PNPT1-specific audioprofile (e.g., frequency configuration) was identified in the sources reviewed and should be sought directly from the founding case series before KB use.
- **Vestibular testing:** Indicated given the reported vestibular dysfunction in at least one family.
- **Ophthalmologic evaluation:** Indicated given reported progressive visual loss/optic atrophy in some pedigrees — relevant to surveillance planning in a pediatric patient diagnosed with "isolated" PNPT1 hearing loss, since optic involvement may only emerge in adulthood.
- **Neurological surveillance:** Given the adult-onset neurodegenerative branch (ataxia, dystonia/spasticity, cognitive-psychiatric decline emerging in the 40s), longitudinal neurological follow-up into adulthood is a reasonable surveillance consideration for genetically confirmed DFNB70 patients, though this recommendation is not yet formalized in a published clinical guideline as far as this search identified.
- **Differential diagnosis:** Other genetic causes of nonsyndromic ARHL (GJB2/DFNB1 being by far the most common), other mitochondrial-disease genes causing combined OXPHOS deficiency/Leigh syndrome (when the severe multisystem phenotype is present), and — for the dominant branch — other spinocerebellar ataxia genes (when ataxia/sensory neuropathy predominates without deafness as the presenting feature).

Sources: [GTR condition page](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1824925/), [ClinGen PNPT1 gene page](https://search.clinicalgenome.org/kb/genes/HGNC:23166), [ClinGen Leigh syndrome validity record](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_6ed99943-2ab9-417d-b0ec-ddbfa11c8645-2020-03-19T191429.965Z), [ClinGen 164 hearing-loss gene-disease pairs paper, PMC7280024](https://pmc.ncbi.nlm.nih.gov/articles/PMC7280024/).

## 11. Outcome/Prognosis

- **Core hearing-loss phenotype:** Not life-limiting by itself; the congenital sensorineural hearing loss is described as stable for decades, so prognosis for the auditory phenotype alone (in the absence of the neurodegenerative branch) is comparable to other stable congenital SNHL — manageable with standard audiologic intervention.
- **Adult-onset neurodegenerative branch:** Substantially worsens long-term prognosis — progression to loss of ambulation, cognitive/psychiatric decline, and incontinence over the 40s–60s represents major cumulative disability; no disease-modifying treatment for this branch was identified in sources reviewed.
- **COXPD13/Leigh-syndrome branch:** **Poor prognosis** — described in the Chinese case-report literature review as "generally unfavorable," with one Leigh-syndrome case dying at age 2.4 years after neonatal onset.
- **Prognostic factors:** Allele severity (hypomorphic vs. more disruptive biallelic combination) appears to be the dominant driver of which phenotypic branch (isolated deafness vs. COXPD13/Leigh) a patient falls into, though this genotype-phenotype correlation is based on a small number of published cases and should not be treated as fully established.

Sources: Eaton et al. 2018 (CITED_NOT_ACCESSED, via search snippet), Matilainen et al. 2017 PMID:28645153, Chinese COXPD13 case report PMC11921403.

## 12. Treatment

- **No disease-modifying / gene-specific pharmacotherapy** for DFNB70 hearing loss itself was identified.
- **Hearing rehabilitation:** Standard-of-care for congenital sensorineural hearing loss — hearing aids and, for severe/profound bilateral loss, **cochlear implantation** would be the expected intervention pathway (NCIT:C15329 Surgical Procedure for implantation; device concept NCIT:C157820 Cochlear Implant as a qualifier per this repo's device-vs-action binding convention) — no PNPT1/DFNB70-specific cochlear implant outcome study was identified in this search pass and should be sought directly (PubMed: "PNPT1 cochlear implant outcome") before writing a treatment block.
- **Emerging targeted therapy for the interferonopathy branch:** A 2026 case report (Brooks et al., *JIMD Reports*, PMID 42375813) describes **JAK inhibitor therapy** used in a patient with PNPT1-related mitochondrial interferonopathy — this is a novel, mechanism-targeted (not curative) intervention aimed at the mt-dsRNA/MDA5/type-I-interferon signaling branch of PNPT1 disease biology, and represents the only targeted pharmacological intervention identified in this research pass. NCIT candidate: pharmacotherapy (NCIT:C15986) with therapeutic_agent bound to the relevant JAK-inhibitor class (verify exact drug name from the primary source before binding CHEBI/NCIT).
- **Supportive/rehabilitative care for the neurodegenerative branch:** Physical therapy/rehabilitation for ataxia and mobility decline, and standard supportive management for dystonia/spasticity, would be expected but were not specifically documented for DFNB70 patients in sources reviewed.
- **Genetic counseling** (NCIT:C15240) is clearly indicated given the recessive inheritance, consanguinity association, and — critically — the possibility of an unpredictable adult-onset neurodegenerative course in offspring who present initially with isolated congenital deafness.
- **Experimental/clinical trials:** No PNPT1/DFNB70-specific registered clinical trial (ClinicalTrials.gov) was identified in this search pass.

Sources: [Brooks et al. 2026, JIMD Reports, PMID 42375813 / PMC13312033](https://pmc.ncbi.nlm.nih.gov/articles/PMC13312033/).

## 13. Prevention

- **Primary prevention:** Not applicable in the population-health sense (rare monogenic disease); the relevant "prevention" pathway is **genetic counseling and reproductive planning** in consanguineous families/carrier couples, given the autosomal recessive inheritance and the demonstrated tendency for these variants to be ascertained through consanguineous or assortative-mating pedigrees.
- **Carrier/preconception screening:** No dedicated population carrier-screening program for PNPT1 was identified; it would fall under expanded carrier screening panels that include rare recessive deafness genes.
- **Newborn screening:** Not gene-specific — DFNB70 would be detected through standard universal newborn hearing screening (which identifies the phenotype, not the genotype), with genetic diagnosis following as a secondary step.
- **Secondary prevention / early detection:** Early audiologic diagnosis (universal newborn hearing screening) allows early intervention (hearing aids/cochlear implant) to mitigate the developmental-language impact of the congenital component; there is no established secondary-prevention strategy for the adult-onset neurodegenerative branch, since its risk and mechanism are not yet well characterized.
- **Prenatal/preimplantation genetic diagnosis:** Standard options for known-carrier couples once the causal familial PNPT1 variants are identified, as with any autosomal recessive Mendelian disorder — no PNPT1-specific literature on this was identified.

## 14. Other Species / Natural Disease

- No naturally occurring PNPT1-associated hearing loss in a non-human species (e.g., a veterinary/OMIA-cataloged breed disorder) was identified in this search pass.
- **Constitutive Pnpt1 knockout in mice is embryonic lethal** — i.e., complete loss of PNPase function is incompatible with mammalian development, which is consistent with the biallelic human disease alleles being hypomorphic/partial-function rather than null, and explains why functional modeling of the human hearing-loss variant required non-null (hypomorphic) or heterologous (yeast/bacterial) systems rather than a full mouse knockout.
- **Zebrafish** (*Danio rerio*) *pnpt1* ortholog shows ~70% amino acid identity to human PNPT1 and is expressed in the developing zebrafish ear (used for in situ hybridization studies by von Ameln et al. 2012), supporting zebrafish as a tractable model for auditory-specific PNPT1 functional studies, though the specific auditory/hair-cell phenotype of a zebrafish pnpt1 loss-of-function model was not clearly established in the sources retrieved and should be verified against the primary 2012 paper.
- **Mouse:** Pnpt1 expression was reported in the (murine) ear during the same 2012 study, supporting conserved auditory relevance of the gene across mammals and fish, though (per the embryonic-lethality finding above) a conditional/hypomorphic mouse model rather than constitutive knockout would be needed to model the human disease.

Sources: von Ameln et al. 2012 (PMID:23084290, via search snippets).

## 15. Model Organisms

- **Mouse (*Mus musculus*):** Constitutive *Pnpt1* knockout is **embryonic lethal**, precluding a straightforward null mouse model of DFNB70; expression in the ear has been documented, but no viable hypomorphic or conditional (e.g., cochlea-specific) mouse model of DFNB70 was identified in the sources reviewed — this would need direct follow-up in MGI/IMPC.
- **Zebrafish (*Danio rerio*):** Used as the primary in vivo model in the founding 2012 paper; ortholog conservation ~70% amino acid identity; ear expression demonstrated by in situ hybridization. A morpholino/knockdown or CRISPR functional auditory phenotype specific to pnpt1 was not clearly retrieved and should be checked directly against the full text of von Ameln et al. 2012 before citing a specific recapitulation claim.
- **In vitro/heterologous systems:** Bacterial and yeast recombinant expression systems, and human HEK293T and patient-derived myoblast cell culture, have been used to demonstrate (a) protein stability/mitochondrial localization vs. (b) trimerization and RNA-import/processing function of wild-type vs. mutant PNPase — these are the primary functional-validation systems used across the PNPT1 literature (von Ameln 2012; Matilainen 2017's myoblast complementation experiment, which showed wild-type PNPT1 re-expression rescued the biochemical defect in a Leigh-syndrome patient's cells).
- **Limitations:** No organism model captures the delayed, decades-later adult-onset neurodegenerative component of the human phenotype; the mt-dsRNA/interferonopathy mechanism is best studied in human patient-derived cells rather than an animal model in the literature surveyed.

Sources: von Ameln et al. 2012, Matilainen et al. 2017 (PMID:28645153).

---

## Verification / Access Status Table (for `just preflight-dr`-style triage)

| Source | Identifier | Access status this session |
|---|---|---|
| von Ameln et al. 2012, *Am J Hum Genet* | PMID:23084290 | `SEARCHED_NO_RESULT` for direct fetch (PubMed CAPTCHA-blocked); content reconstructed from search-engine summaries + ScienceDirect listing — **re-fetch abstract via `just fetch-reference PMID:23084290` before quoting** |
| Eaton et al. 2018, *Am J Med Genet A* | DOI 10.1002/ajmg.a.40516 | `CITED_NOT_ACCESSED` (Wiley 403) |
| Matilainen et al. 2017, *Hum Mol Genet* | PMID:28645153 | `CITED_NOT_ACCESSED` (search-summary only; academic.oup.com not fetched) |
| Brooks et al. 2026, *JIMD Reports* | PMID:42375813 / PMC13312033 | `CITED_NOT_ACCESSED` |
| South India family report | PMID:34374074 | `CITED_NOT_ACCESSED` (Wiley epdf 403; bioRxiv HTML 429) |
| Chinese COXPD13 case report/review | PMC11921403 / PMID:40115456 | `ACCESSED` (WebFetch succeeded, summarized text obtained — note this review itself contains at least one likely error, "DFNB35" for isolated PNPT1 hearing loss, which should read DFNB70; flagged, not repeated as fact above) |
| ClinGen Leigh syndrome gene-disease validity record | CGGV:assertion_6ed99943... | `ACCESSED` |
| OMIM #614934, #610316, #608703 | — | `SEARCHED_NO_RESULT` for direct fetch (omim.org 403); reconstructed from search snippets — **must be independently re-verified** against a licensed OMIM source before KB citation |
| GTR condition page | C1824925 | `ACCESSED` |

**Bottom line for curation:** The gene (PNPT1), locus (2p16.1), OMIM number (#614934), founding variant (c.1424A>G/p.Glu475Gly in 3 consanguineous Moroccan siblings), and core mechanism (hypomorphic PNPase → impaired trimerization/mitochondrial RNA import) are corroborated across multiple independent search results and are high-confidence leads. The **adult-onset neurodegeneration natural-history claim**, the **exact HPO/vestibular/visual phenotype details** of the South Indian family, and **all specific evidence snippets** still require direct primary-source fetch (`just fetch-reference`) and exact-quote extraction before they can support `EvidenceItem` blocks in a dismech YAML entry — none of the prose above should be pasted as a `snippet:` value without that step.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0140373` (1 mention) - the report calls it "antiviral innate immune response"; GO calls it **obsolete histone H3-K14 ubiquitination**
- `CL:0002510` (1 mention) - the report calls it "spiral ganglion neuron"; CL calls it **CD103-negative, langerin-positive lymph node dendritic cell**
- `UBERON:0001846` (1 mention) - the report calls it "cochlea"; UBERON calls it **internal ear**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002520` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0140373` (obsolete histone H3-K14 ubiquitination) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000601` (1 mention) - the report calls it "auditory hair cell"; CL calls it **cochlear outer hair cell**
- `UBERON:0002104` (1 mention) - the report calls it "vestibular organ"; UBERON calls it **visual system**, and lists "visual organ system" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.