---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-04T16:05:03.624600'
end_time: '2026-11-04T16:07:35.122508'
duration_seconds: 151.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ROGDI-Related Kohlschutter-Tonz Syndrome
  mondo_id: MONDO:0009185
  category: Mendelian
  causal_genes: ROGDI
  omim_id: OMIM:226750
  synonyms: Kohlschutter-Tonz syndrome; epilepsy-dementia-amelogenesis imperfecta
    syndrome
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
  num_turns: 14
  total_cost_usd: 2.2155604
  session_id: eb4af222-bf72-4411-bf51-7bbde549f353
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
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
citation_count: 5
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 9
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:27600704
  relevance_assessed: 19
  on_topic: 19
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ROGDI-Related Kohlschutter-Tonz Syndrome
- **MONDO ID:** MONDO:0009185 (if available)
- **Causal gene(s):** ROGDI
- **OMIM:** OMIM:226750
- **Synonyms:** Kohlschutter-Tonz syndrome; epilepsy-dementia-amelogenesis imperfecta syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ROGDI-Related Kohlschutter-Tonz Syndrome** covering all of the
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

I'm reading the cached abstracts for the key ROGDI papers. Then I'll write the report.

# Research Report: ROGDI-Related Kohlschütter-Tönz Syndrome (MONDO:0009185; OMIM #226750)

**Causal gene: *ROGDI*** (rogdi atypical leucine zipper; HGNC:29478, written `hgnc:29478` in dismech; chromosome 16p13.3). This report covers the ROGDI-related form only. The *SLC13A5*-related "Kohlschütter-Tönz-like" disease (neonatal epileptic encephalopathy with hypoplastic amelogenesis imperfecta) is a different genetic entity. It is mentioned here only for differential diagnosis.

**Sources.** Most quotes below were checked against the abstracts (or PMC full text) cached in `references_cache/` in this repository. Items marked **[unverified]** come from web search and have not been checked against a cached record. Every ontology CURIE suggested here is a lead. Look each one up (`runoak`, the cache, or OLS) before binding it, as the repository's term contract requires.

**Repo note.** `kb/disorders/ROGDI-Related_Kohlschutter-Tonz_Syndrome.yaml` already exists (674 lines). This report can be used to audit or extend that entry rather than to create a new one.

---

## 1. Disease Information

**Overview.** Kohlschütter-Tönz syndrome (KTS) is an autosomal recessive disease of childhood onset. Its defining triad is early-onset epilepsy, global developmental delay or regression, and amelogenesis imperfecta (yellow-brown, soft enamel) of both primary and permanent teeth.
- "Kohlschütter-Tönz syndrome (KTS) is an autosomal-recessive disease characterized by the combination of epilepsy, psychomotor regression, and amelogenesis imperfecta." — PMID:22424600 (Schossig et al., *Am J Hum Genet* 2012)
- It was first described in a Swiss family in 1974 (Kohlschütter et al.), as noted in PMID:34939736 and PMID:23086778.

**Identifiers**
| System | ID |
|---|---|
| MONDO | MONDO:0009185 (ClinGen label: "amelocerebrohypohidrotic syndrome") |
| OMIM | #226750 (gene *ROGDI* *614574 **[unverified]**) |
| Orphanet | ORPHA:1946 |
| HGNC | hgnc:29478 |
| ClinGen GDV | ROGDI–MONDO:0009185, AR, **Definitive** (CGGV:assertion_dc4132b5-…-2022-06-21) |
| ICD-10 | No specific code. Usually coded under K00.5 (hereditary disturbances of tooth structure) plus G40.x **[unverified]** |
| MeSH | No specific descriptor. Indexed under Amelogenesis Imperfecta, Epilepsy and Dementia (MeSH keywords on PMID:22424600) |

**Synonyms.** Kohlschütter syndrome; amelocerebrohypohidrotic syndrome; epilepsy–dementia–amelogenesis imperfecta syndrome; ROGDI-related KTS.

**Source type.** All knowledge comes from aggregated case reports and small case series. There are about 43–66 reported cases in total: PMID:34939736 counts 43 genetically confirmed patients, and PMID:39445602 counts 66 reported cases, 44 of them genetically confirmed. There are no EHR-derived cohorts or registries.

## 2. Etiology

- **Cause.** Biallelic (homozygous or compound heterozygous) loss-of-function variants in *ROGDI*.
  - "Here, we report that KTS is caused by mutations in ROGDI." — PMID:22424600
  - ClinGen: "The mechanism of pathogenicity is known to be homozygous or compound heterozygous loss of function."
- **Genetic risk factors.** Consanguinity and founder alleles. A Druze founder allele (p.Arg157\*) has a carrier rate of about 10% in one village (see §9).
- **Environmental risk factors, protective factors and gene–environment interactions.** None are known. No modifier genes have been identified. Variability in age of onset and severity within the same homozygous genotype suggests unidentified modifiers (PMID:22482807).

## 3. Phenotypes

| Phenotype | Suggested HPO (verify) | Onset / course | Frequency | Key evidence |
|---|---|---|---|---|
| Epilepsy / seizures (often drug-resistant; status epilepticus) | HP:0001250 Seizure; HP:0001250-descendants for focal/generalized | 6–12 months (range: neonatal to 2 years); progressive | 100% (43 ROGDI cases) | "100% exhibited epilepsy, global developmental delay, and amelogenesis imperfecta." — PMID:37974187 |
| Global developmental delay / psychomotor regression | HP:0001263; HP:0002376 Developmental regression | Infancy; regression after seizure onset | 100% | "All affected individuals show a psychomotor regression after onset of epilepsy or a developmental delay from birth on." — PMID:22522085 |
| Amelogenesis imperfecta (hypocalcified/hypomature); yellow-brown teeth | HP:0000705; HP:0006286 Yellow-brown discoloration of the teeth | Present from tooth eruption; affects both dentitions | 100% | Orphanet: "HP:0006286 \| Yellow-brown discoloration of the teeth \| Very frequent (99-80%)" |
| Absent or severely impaired speech | HP:0001344 Absent speech / HP:0002463 Language impairment | Childhood | ~100% | "Language disorders were observed in all patients." — PMID:37974187 |
| Severe intellectual disability | HP:0010864 Intellectual disability, severe | Progressive | Most | PMID:29150638 |
| Spasticity | HP:0001257 | Progressive; bedridden by the late teens or twenties | Very frequent (Orphanet) | "By late adolescence and early twenties, individuals with KTS are bedridden, fed by a gastrostomy tube, spastic…" — PMID:24630287 |
| ADHD / hyperactivity | HP:0007018 | Childhood | 17.2% | PMID:37974187 |
| Autism spectrum features | HP:0000729 | Childhood | 3.4% suspected | PMID:37974187 |
| Self-injurious behavior | HP:0100716 | Variable | 9.1% | PMID:37974187 |
| Hypohidrosis | HP:0000966 | — | Frequent (79–30%, Orphanet) | Orphanet ORPHA:1946 |
| Nephrocalcinosis | HP:0000121 | Childhood | Rare (3 reported cases) | PMID:34939736; PMID:39445602 |
| Distal renal tubular acidosis | HP:0008341 | Childhood | Rare (2 families) | PMID:39445602; Tunisian family (c.646-2A>G, *Clin Genet* 2025, PMC12050240) **[unverified]** |
| Hyperammonemia | HP:0001987 | — | Single report | Tunisian family **[unverified]** |
| Feeding difficulty / gastrostomy dependence | HP:0011968 | Adolescence | Common in late disease | PMID:24630287 |
| Rett-like phenotype | — | — | Case report (c.201-1G>T, Turkish girl) **[unverified]** | — |

**Quality of life.** The burden is severe: total dependence, drug-resistant seizures and loss of communication. No validated QoL instruments have been used. Brain MRI and EEG can be normal early on (PMID:37974187).

## 4. Genetic / Molecular Information

- **Gene.** *ROGDI*, 11 exons, NM_024589.3. It encodes a ~287-amino-acid protein that is conserved across metazoans. It is highly expressed in the brain and other organs (PMID:22424600).
- **Variant classes** (all predicted loss of function; no missense-only pathogenic alleles are well established):
  - Frameshift: c.229_230del p.(Leu77Alafs\*64) (PMID:22424600)
  - Nonsense: c.286C>T p.(Gln96\*) (PMID:22424600); c.469C>T p.(Arg157\*), the Druze founder allele (PMID:22482807; reported as c.571C>T in PMID:24630287 because of a different transcript numbering)
  - Splice: c.531+5G>C / c.532-2A>T (compound heterozygous, original Swiss family); c.117+1G>T; c.201-1G>T; c.646-2A>G (Tunisian); c.646-2_649del (Indian, PMID:39445602); c.46-37_46-30del (deep-intronic/branch-region deletion, Chinese patient, PMID:37974187)
  - Multi-exon deletions: deleting exons 6–11 recapitulates a patient allele (modelled in mouse, PMID:38172607). A further family was found by Tucci et al. (PMID:23086778).
- **Functional consequence.** Protein loss: "ROGDI was not detectable in cells of affected individuals." — PMID:22482807. Structural destabilization: "Disruption of the four-helix bundle by mutation results in significant destabilization of the structure." — PMID:28638151.
- **Classification.** ClinVar lists multiple Pathogenic or Likely pathogenic LoF variants. ClinGen rates the gene–disease relationship Definitive (AR).
- **Allele frequency.** All alleles are rare in gnomAD, apart from the Druze founder allele, which is enriched in one village.
- **Origin.** Germline. No somatic, epigenetic or chromosomal mechanism is known.
- **Genetic heterogeneity.** ROGDI-negative "atypical KTS" families exist (PMID:23086778). *SLC13A5* is the second gene: "SLC13A5 is the second major gene associated with the clinical diagnosis of KTZS" — PMID:27600704.

## 5. Environmental Information

There are no known environmental, lifestyle or infectious contributors. This is not applicable for a Mendelian loss-of-function disorder.

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *ROGDI* LoF variants** (nonsense, frameshift, splice, deletion) **lead to** absent or unstable ROGDI protein. This is demonstrated in patient cells (PMID:22482807) and supported structurally (PMID:28638151).
2. **Loss of ROGDI results in** loss of a Rav2-homologous subunit of the **Rabconnectin-3 (RC3) complex** (DMXL1/2 = RC3α, WDR7 = RC3β). This is demonstrated in yeast complementation and mammalian co-IP (PMID:40049412):
   - "We identified ROGDI as a Rav2 homolog and novel Rabconnectin-3 subunit."
   - "ROGDI binds to the N-terminal domains of both Rabconnectin-3 α and β, similar to Rav2 binding to Rav1."
3. **Loss of the RC3 bridge leads to** impaired V1–V0 reassembly of the **vacuolar H⁺-ATPase (V-ATPase)** and therefore defective acidification of organelles and secretory compartments. This step is *inferred* from yeast Rav2 biology and from ROGDI co-localization in acidic lysosomes. Defective V-ATPase assembly has not yet been measured directly in ROGDI-null human cells.
4. The effect then branches.
   - **4a. Dental branch.** Ameloblasts fail to generate the cyclic acidic/neutral pH modulation needed for enamel maturation. This **results in** hypomineralized, hypomature enamel, which is clinically amelogenesis imperfecta with yellow-brown teeth. In the mouse model (PMID:38172607):
     - "Rogdi-/- teeth exhibit no signs of cyclic dental acidification."
     - "Transcriptomic RNA sequencing of postnatal day 5 lower incisors showed downregulated enamel matrix proteins Enam, Amelx, and Ambn."
     - Expression of *Wdr72*, *Slc9a3r2* and *Atp6v0c* is altered.

     WDR72 is itself a known amelogenesis imperfecta gene, so this convergence is suggestive.
   - **4b. Neuronal branch.** ROGDI is a **presynaptic protein**: "Rogdi is enriched at synaptic sites" and colocalizes with Bassoon, Synaptophysin, Synapsin-1, VAMP2 and Mover (PMID:29150638). V-ATPase supplies the proton gradient that drives neurotransmitter loading into synaptic vesicles. Rabconnectin-3 is a synaptic-vesicle-associated V-ATPase regulator. Loss therefore plausibly **leads to** impaired vesicle acidification and loading, and to presynaptic dysfunction. This is *inferred*: "the neurological symptoms associated with Kohlschütter-Tönz syndrome may arise from presynaptic dysfunction" (PMID:29150638).
   - **4b′. GABAergic sub-branch** (Drosophila). Rogdi supports metabotropic (GABA-B) GABAergic transmission. Loss **results in** disinhibition of a wake-promoting dopaminergic circuit, causing sleep loss (Kim et al. 2017, *Sci Rep*, PMID:28900300 **[unverified PMID]**, PMC5595912). Reduced inhibitory tone is a candidate route to epilepsy, but this is *inferred*.
5. **Presynaptic or inhibitory failure leads to** network hyperexcitability, which shows clinically as early-onset, often drug-resistant epilepsy. The mouse shows pentylenetetrazol-induced seizures: "Mutants displayed pentylenetetrazol-induced seizures, confirming epilepsy susceptibility." (PMID:38172607)
6. **Recurrent seizures and the intrinsic synaptic defect result in** epileptic encephalopathy, with psychomotor regression, absent speech, severe ID, spasticity and hyperactivity. The mouse shows hyperactivity and memory deficits (PMID:38172607). Seizure severity predicts the speed of deterioration (PMID:24630287).
   - **4c. Renal branch** (rare). The V-ATPase on α-intercalated cells of the collecting duct drives distal acid secretion. Its dysfunction plausibly **leads to** distal RTA, which in turn leads to nephrocalcinosis (PMID:39445602; PMID:34939736). This is *inferred* from the parallel with *ATP6V0A4*/*ATP6V1B1* dRTA. PMID:39445602 states that the mechanism is unknown.
   - **4d. Sweat glands** (hypohidrosis). The mechanism is unknown. A V-ATPase role in eccrine secretion is speculative.

### Checklist detail
- **Pathways.** V-ATPase assembly and regulation; lysosomal and vesicular acidification; synaptic vesicle cycle; GABA-B signalling (fly).
- **Protein.** Crystal structure (PMID:28638151): an elongated curved fold with an α domain (leucine-zipper-like four-helix bundle pairing H1 [res. 19–45] with H6 [res. 252–287]) and a β-sheet domain. Truncations disrupt the bundle. An early report placed ROGDI at the nuclear envelope (PMID:22482807); later work places it at presynaptic sites and lysosomes. A proposed DISC1 interaction has not been confirmed.
- **Metabolic and biochemical.** There are no diagnostic biochemical markers (PMID:22522085). Hyperammonemia was reported once.
- **Immune system.** Not involved.
- **Omics.** The only dataset is mouse incisor bulk RNA-seq (PMID:38172607). There are no human single-cell, spatial or proteomic data.

**Suggested GO terms** (verify): vacuolar acidification (GO:0007035); proton-transporting V-type ATPase complex assembly (GO:0070070) and its vacuolar child term; synaptic vesicle lumen acidification (GO:0097401); amelogenesis (GO:0097186); enamel mineralization (GO:0070166); presynapse (GO:0098793); lysosome (GO:0005764); Rabconnectin complex (GO:0043291).
**Suggested CL terms** (verify): ameloblast (CL:0000059); neuron (CL:0000540); GABAergic neuron (CL:0011005); renal alpha-intercalated cell (CL:0005011).

## 7. Anatomical Structures

- **Primary.** Brain (cerebral cortex) [UBERON:0000955]; tooth enamel and enamel organ [UBERON:0001752 enamel] in both dentitions.
- **Secondary.** Kidney (collecting duct; nephrocalcinosis) [UBERON:0002113]; eccrine sweat glands [UBERON:0000423]; skeletal system (skeletal abnormality, PMID:39445602).
- **Cell level.** Ameloblasts, presynaptic neurons, and α-intercalated cells (by inference).
- **Subcellular.** Presynaptic terminal and synaptic vesicles (PMID:29150638); acidic perinuclear lysosomes (PMID:40049412); nuclear envelope in an early report (PMID:22482807).
- **Lateralization.** Bilateral and symmetric (generalized enamel defect; bilateral nephrocalcinosis).

## 8. Temporal Development

- **Onset.** Seizures start at 6–12 months in the Druze cohort (PMID:24630287), and usually in the first or second year of life (PMID:22522085). Some patients have delay from birth. Enamel defects appear at tooth eruption.
- **Progression.** Progressive neurodegeneration. Regression follows seizure onset. Patients are bedridden, tube-fed and spastic by the late teens or twenties: "In all cases, however, the morbid course of the disease is ultimately equally devastating by the twenties." (PMID:24630287)
- **Variability.** Variability is marked even within families and within the same genotype (PMID:22482807). Milder courses with preserved ambulation have been reported.
- **Critical window.** Early seizure control may slow deterioration, because seizure severity predicts the pace of decline (PMID:24630287). This is an inference; it has not been tested.

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007): "This report confirms the autosomal recessive inheritance of the disorder." (PMID:8357021)
- **Penetrance.** Complete for biallelic LoF. Expressivity is variable. There is no anticipation.
- **Prevalence.** Below 1 per 1,000,000 (Orphanet: "<1 / 1 000 000 | Worldwide | Point prevalence"). About 43–66 published cases.
- **Founder effect.** The Druze p.Arg157\* allele "was homozygous in all affected individuals, heterozygous in 10 of 100 unaffected individuals from the same Druze community, and absent from Druze controls from elsewhere." (PMID:22482807)
- **Consanguinity.** Common in reported families (Druze, Indian, Tunisian, Turkish and Malian).
- **Geography.** Worldwide, in sporadic families: Switzerland, Austria, Israel, the UK, Italy, Brazil, Latvia, China, India, Tunisia, Turkey and Mali.
- **Sex ratio.** About 1:1 (8F/8M in PMID:24630287).

## 10. Diagnostics

- **Clinical criteria.** There are no formal criteria. Diagnosis rests on the triad of early epilepsy, developmental delay or regression, and generalized amelogenesis imperfecta. A dental examination is a cheap, high-yield clue in any child with epileptic encephalopathy.
- **Laboratory.** No biomarkers (PMID:22522085). Renal evaluation is worth considering: venous blood gas, urine pH, urinary calcium and renal ultrasound for dRTA and nephrocalcinosis (PMID:39445602).
- **EEG and MRI.** EEG shows multifocal or generalized epileptiform activity. MRI is often normal early (PMID:37974187); cerebral and cerebellar atrophy can appear later **[unverified]**.
- **Dental histology and imaging.** Histology shows hypocalcified amelogenesis imperfecta: "the histological evaluation of a molar … from an individual with ROGDI-associated KTZS revealed hypocalcified AI" (PMID:27600704). Hypoplastic amelogenesis imperfecta instead suggests *SLC13A5*.
- **Genetic testing.**
  - Exome or genome sequencing (trio preferred), or epilepsy and amelogenesis imperfecta panels that include *ROGDI* and *SLC13A5*.
  - Deep-intronic and branch-point variants (c.46-37_46-30del) and multi-exon deletions mean that genome sequencing or CNV analysis can add yield.
  - RNA studies or long-read cDNA sequencing resolve splice variants (Tunisian report, PMC12050240).
  - CMA, karyotype, FISH, mtDNA testing and repeat-expansion testing are not indicated except for CNV detection.
- **Differential diagnosis.**
  - *SLC13A5* KTS-like (neonatal onset, hypoplastic amelogenesis imperfecta, citrate transporter)
  - Other developmental and epileptic encephalopathies (*SCN1A*, *CDKL5*, Rett/*MECP2*)
  - Enamel-renal syndrome (*FAM20A*)
  - Amelogenesis imperfecta with nephrocalcinosis; dRTA (*ATP6V0A4*, *ATP6V1B1*)
  - Neuronal ceroid lipofuscinoses
- **Screening.** No newborn screening. Carrier screening or cascade testing in founder populations (Druze). Prenatal or preimplantation diagnosis is possible once the familial variants are known.

## 11. Outcome / Prognosis

- Progressive. Most patients become completely dependent, with absent speech, spasticity and gastrostomy feeding, by the late teens or twenties (PMID:24630287).
- Death in childhood or early adulthood is reported: "which may lead to death in childhood or early adulthood" (PMID:29150638). No survival statistics exist.
- **Complications.** Refractory and super-refractory status epilepticus (PMID:34939736); aspiration and feeding problems; dental caries and attrition from soft enamel; nephrocalcinosis.
- **Prognostic factors.** Age of seizure onset and seizure severity predict the speed of decline (PMID:24630287).

## 12. Treatment

There is no disease-modifying therapy. Management is symptomatic and multidisciplinary.

- **Antiseizure medication** (NCIT:C15986 Pharmacotherapy; verify).
  - Seizures are often resistant to multiple antiseizure medications (PMID:29150638).
  - **Perampanel** (an AMPA-receptor antagonist) has reported benefit in two cases:
    - "Perampanel proved an effective treatment for our patient with prolonged super-refractory status epilepticus." (PMID:34939736)
    - "The efficacy of perampanel (PMP) in treating seizures and intellectual disability was apparent." (PMID:37974187)
  - This is case-level evidence only. The CHEBI or NCIT ID for perampanel needs a lookup.
- **Dental care** (NCIT dental restoration or Therapeutic Procedure terms; look these up). Options include restorative treatment, crowns, preventive fluoride, and treatment under general anesthesia where feasible: "The younger sibling received successful restorative treatment under general anesthesia, while the older sibling's oral care was managed conservatively…" (PMID:40960323)
- **Renal.** Alkali therapy (citrate or bicarbonate) for dRTA, by analogy with standard dRTA care. No KTS-specific trial exists.
- **Supportive and rehabilitative.** Physical therapy (NCIT:C15302), occupational and speech therapy, antispasticity management, gastrostomy (nutritional support), ADHD and behavioral management (NCIT:C15747 Supportive Care).
- **Experimental.** There are no clinical trials (no NCT or ICTRP entries found). Gene-replacement or V-ATPase-modulating approaches are conceptual only. The structure paper mentions drug-development implications (PMID:28638151).
- **Pharmacogenomics.** None known.

## 13. Prevention

- **Primary.** Genetic counseling (NCIT:C15240), carrier testing in consanguineous or founder communities, and prenatal or preimplantation genetic diagnosis.
- **Secondary.** Early recognition through dental findings, and early genetic diagnosis.
- **Tertiary.** Aggressive seizure control, dental protection, renal surveillance, nutrition and prevention of aspiration.
- No vaccines, public-health or environmental measures apply.

## 14. Other Species / Natural Disease

- **Orthologs.** *ROGDI* is conserved in *C. elegans*, *D. melanogaster* (*rogdi*), *D. rerio*, *X. laevis* and *M. musculus* (PMID:38172607). The functional yeast homolog is *RAV2* (complementation shown, PMID:40049412).
- **Naturally occurring animal disease.** None found in OMIA.

## 15. Model Organisms

| Model | Genotype | Recapitulation | Limitations | Evidence |
|---|---|---|---|---|
| Mouse (*Mus musculus*) | *Rogdi*⁻/⁻ (exon 6–11 deletion, a patient-like allele) | PTZ-induced seizures (susceptibility); hyperactivity; object-recognition memory deficit; hypomineralized and hypomature enamel; loss of cyclic enamel acidification; reduced *Enam*/*Amelx*/*Ambn* | No spontaneous seizures reported; hyperactivity is taken as a proxy for spasticity; renal and sweat phenotypes not reported | PMID:38172607 |
| *Drosophila* | *rogdi* mutants | Memory defects (first identified in a memory screen, Dubnau et al. 2003 **[unverified]**); sleep loss through reduced GABA-B transmission onto wake-promoting dopaminergic neurons | Invertebrate; no teeth | Kim et al. 2017 *Sci Rep* (PMC5595912; PMID:28900300 **[unverified]**) |
| Yeast (*S. cerevisiae*) | *rav2Δ* complemented by human ROGDI | Shows ROGDI function in V-ATPase assembly | Heterologous; no tissue phenotype | PMID:40049412 |
| Rat hippocampal neurons (in vitro) | GFP-Rogdi | Presynaptic localization | Overexpression; localization only | PMID:29150638 |

**Gaps.** There are no zebrafish or patient-iPSC neuron or organoid models. No study has directly measured V-ATPase assembly or synaptic-vesicle pH in ROGDI-null mammalian neurons. That experiment would test step 3 of the causal chain, which is currently inferred. The mouse lacks spontaneous seizures, which is a candidate `HUMAN_MODEL_MISMATCH` discussion for the entry.

---

## Key Open Questions

1. Does ROGDI loss reduce V-ATPase assembly and acidification of synaptic vesicles, ameloblast compartments and collecting-duct cells in mammals?
2. Why do only a few patients show dRTA and nephrocalcinosis? It may be an under-ascertained feature, or it may depend on the allele.
3. Are the GABA-B and dopaminergic findings in the fly relevant to human epileptogenesis?
4. Does perampanel's benefit extend beyond the two reported cases?

## Sources
- Cached in the repo (`references_cache/`): PMID:8357021, 22424600, 22482807, 22522085, 23086778, 24630287, 27600704, 28638151, 29150638, 34939736, 37974187, 38172607, 39445602, 40049412, 40960323; ORPHA:1946; the ClinGen CGGV assertion.
- [Rogdi Defines GABAergic Control of a Wake-promoting Dopaminergic Pathway to Sustain Sleep in Drosophila (PMC5595912)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5595912/)
- [The Rogdi knockout mouse is a model for Kohlschütter–Tönz syndrome (PMC10764811)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10764811/)
- [Transcript Long-Read Sequencing Unveils the Molecular Complexity of a Novel ROGDI Splicing Variant in a Tunisian Family With KTS (PMC12050240)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12050240/)
- [InteractiveFly: rogdi GeneBrief](https://www.sdbonline.org/sites/FLY/genebrief/rogdi.htm)
- [KTS case report with novel feature (RSU)](https://science.rsu.lv/en/publications/kohlsch%C3%BCtter-t%C3%B6nz-syndrome-case-report-with-novel-feature-and-det/)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:27600704` *(abstract only)*: "the histological evaluation of a molar … from an individual with ROGDI-associated KTZS revealed hypocalcified AI"
  - closest text in source: "In comparison, the histological evaluation of a molar assessed from an individual with ROGDI-associated KTZS revealed hypocalcified AI"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0009185` (3 mentions) - the report calls it "ClinGen label: "amelocerebrohypohidrotic syndrome"; MONDO calls it **amelocerebrohypohidrotic syndrome**
- `HP:0007018` (1 mention) - the report calls it "ADHD / hyperactivity"; HP calls it **Attention deficit hyperactivity disorder**
- `HP:0000729` (1 mention) - the report calls it "Autism spectrum features"; HP calls it **Autistic behavior**, and lists "Autism spectrum disorders" among its other names
- `HP:0011968` (1 mention) - the report calls it "Feeding difficulty / gastrostomy dependence"; HP calls it **Feeding difficulties**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

39 of 41 terms resolved to a current term; the rest could not be looked up either way.