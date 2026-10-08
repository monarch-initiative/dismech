---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-03T02:53:35.692455'
end_time: '2026-10-03T02:54:51.320737'
duration_seconds: 75.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Nerve Agent Poisoning
  mondo_id: MONDO:0100331
  category: Environmental
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
  web_search_requests: 4
  num_turns: 5
  total_cost_usd: 0.8410789999999998
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
citation_count: 8
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 0
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
- **Disease Name:** Nerve Agent Poisoning
- **MONDO ID:** MONDO:0100331 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Nerve Agent Poisoning** covering all of the
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

# Nerve Agent Poisoning: Research Report for Dismech Curation

**Scope and evidence status.** I ran three web searches and did not open any full text. Every claim tied to a link below comes from the search-result summaries of that source. Material marked **[background, unsourced]** is standard toxicology knowledge that I did not verify in this session.

- I have not verified any PMID, snippet or ontology CURIE. I did not write any PMID from memory, so the sources are cited by URL and PMC ID.
- Look up every term with `runoak` or the `cache/` CSVs before binding it. The term suggestions below are names only.
- Run `just fetch-reference` on each source before using it as evidence, and take snippets from the cached text, not from this report.
- Before the entry is written, check whether MONDO:0100331 is the right term for "nerve agent poisoning". The ID came from the template and I have not checked it.

---

## 1. Disease Information

- **Overview.** Nerve agent poisoning is acute cholinergic toxicity from organophosphorus nerve agents. These are the G-series (tabun, sarin, soman, cyclosarin), VX and the V-series, and the "Novichok" (A-series) agents. They irreversibly inhibit acetylcholinesterase (AChE). Acetylcholine then accumulates at muscarinic and nicotinic synapses and in the CNS. [background, unsourced]
- **Treatment summary.** Therapy has three components: atropine, a benzodiazepine and an oxime ([Merck Manual](https://www.merckmanuals.com/en-ca/professional/injuries-poisoning/mass-casualty-weapons/nerve-chemical-warfare-agents); [Dawson, AMMA J 2023](https://jmvh.org/article/https-doi-ds-org-doilink-03-2023-52676377-jmvh-vol-8-no-3/)).
- **Identifiers and synonyms.** I did not check ICD-10, ICD-11, MeSH or OMIM codes. Likely ICD-10 candidates are T59.8 or T60.x (organophosphate toxic effect), which need checking. Synonyms: nerve gas poisoning, organophosphorus nerve agent intoxication, chemical warfare nerve agent toxicity.
- **Data source.** Information comes from aggregated case series and incident reports: Tokyo 1995, Ghouta 2013, Salisbury 2018.
- **Scope note.** This is an exposure-defined toxic disorder, not a Mendelian one. Check the dismech scope decisions (`docs/explanation/design-decisions.md`) on toxic exposures. The nearest precedents are `Arsenic_Poisoning` and `Digitalis_Poisoning`. Decide whether this is one entry or whether organophosphate pesticide poisoning should be lumped in. The mechanism is the same, but the agents' potency and aging kinetics differ.

## 2. Etiology

- **Cause.** Exposure to an organophosphorus nerve agent by inhalation, dermal contact or ingestion. Settings are military or terrorist use, assassination, and accidents or industrial release. [background, unsourced]
- **Documented incidents**
  - **Tokyo, 1995.** The sarin attack killed 13 and sickened more than 6,000 (see [PLoS ONE 2020 follow-up](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310687/)).
  - **Ghouta, Syria, 2013.** Sarin rockets; the US estimate was 1,429 deaths including 426 children (per the [Wikipedia summary](https://en.wikipedia.org/wiki/Ghouta_chemical_attack), which is not a primary source).
  - **Salisbury, UK, 2018.** Novichok; the NHS response was described as its longest-running major incident, about 72 days ([Frontiers in Toxicology review](https://www.frontiersin.org/journals/toxicology/articles/10.3389/ftox.2022.1004705/full); [PMC9905702](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9905702/)).
- **Genetic risk and modifiers.** Butyrylcholinesterase (BCHE) variants and paraoxonase 1 (PON1) polymorphisms plausibly modify susceptibility. I found no source for this in these searches; mark it as a literature gap. [background, unsourced]
- **Protective factors.** Pyridostigmine pretreatment is used by the military against soman. Protective equipment and rapid decontamination also protect. [background, unsourced]
- **Gene-environment interaction.** Not established from the sources retrieved.

## 3. Phenotypes

These are acute muscarinic, nicotinic and CNS features. Frequencies were not obtained.

| Phenotype | Type | Suggested HPO term (name only; look up the ID) |
|---|---|---|
| Miosis (eye pain, blurred vision) | sign/symptom | Miosis |
| Rhinorrhea, salivation, bronchorrhea | sign | Excessive salivation; Rhinorrhea |
| Bronchoconstriction, dyspnea | sign/symptom | Dyspnea; Wheezing |
| Nausea, vomiting, diarrhea, incontinence | symptom | Nausea and vomiting; Diarrhea |
| Bradycardia | sign | Bradycardia |
| Fasciculations, weakness, paralysis | sign | Fasciculations; Muscle weakness |
| Seizures | sign | Seizure |
| Altered consciousness, headache | symptom | Confusion; Headache |
| Respiratory failure | sign | Respiratory failure |

- **Salisbury Novichok.** Reported features include nausea and vomiting, headache, altered mental state, blurred or painful vision, and involuntary faecal incontinence ([Star summary of the NHS account](https://www.thestar.co.uk/health/what-is-novichok-how-does-it-affect-the-body-symptoms-poisoning-salisbury-inquiry-4822683); a secondary source, so prefer [PMC9905702](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9905702/)).
- **Onset and course.** Onset is acute: seconds to minutes after vapor exposure, longer after dermal VX. Phenotypes are episodic and self-limited if the patient survives. [background, unsourced]
- **Chronic and psychiatric sequelae in Tokyo survivors**
  - Somatic symptoms, especially eye symptoms, were present in 60–80% and had not decreased.
  - Posttraumatic stress response was present in 35.1% with no change over time.
  - This comes from annual questionnaires, 2000–2009, in a [PLoS ONE 2020 study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310687/) that described most acute symptoms as transient.
  - Evidence type: HUMAN_CLINICAL. The data are self-reported.

## 4. Genetic/Molecular Information

- **Causal genes.** None. The cause is environmental.
- **Molecular target.** ACHE (AChE) is the primary target. BCHE is a scavenger and biomarker. Candidate modifiers are BCHE and PON1 variants. All of this is [background, unsourced]. Use lowercase `hgnc:` CURIEs after lookup.
- **Epigenetic and chromosomal.** Not applicable, and nothing was retrieved.

## 5. Environmental Information

- **Exposure agents.** Sarin (GB), soman (GD), tabun (GA), cyclosarin (GF), VX and Novichok-class agents.
- **Routes.** Inhalation (vapor or aerosol), dermal (especially VX) and ocular. Ingestion occurs in poisonings.
- **Binding.** Look up ECTO exposure terms and CHEBI agent terms, and check that the term fits the specific agent. Per the project rules, run the ECTO search verbatim before writing any note that no term exists. Search both "anaesthetic"-style spelling variants and general terms such as "organophosphate" and "nerve agent".
- **Infectious agents and lifestyle factors.** Not applicable.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps 1–3 are mechanistic knowledge [background, unsourced]; aging is supported by [StatPearls via search](https://dev2.statpearls.com/articlelibrary/viewarticle/25716)):

1. Nerve agent enters the body by inhalation, skin or eye and is absorbed systemically. This leads to
2. phosphylation of the active-site serine of AChE, which inactivates the enzyme. This results in
3. accumulation of acetylcholine at cholinergic synapses and neuromuscular junctions. This causes
4. over-stimulation of muscarinic receptors (parasympathetic effector organs and glands), nicotinic receptors (autonomic ganglia and the neuromuscular junction), and central cholinergic circuits. This leads to
5. the muscarinic toxidrome (miosis, secretions, bronchoconstriction, bradycardia, GI hypermotility), nicotinic effects (fasciculations, then depolarization-block paralysis) and CNS effects (seizures, coma). The respiratory consequences arise from several of these together: bronchorrhea, bronchospasm, respiratory-muscle paralysis and central apnea. These are the usual cause of death.
6. **Branch (aging).** The phosphylated enzyme loses an alkyl group and is "aged", which makes the inhibition permanent and oxime reactivation ineffective. The time to aging differs by agent: soman about 1–2 minutes, VX about 30 hours ([search summary of StatPearls](https://dev2.statpearls.com/articlelibrary/viewarticle/25716)). Aging therefore sets the window for oxime therapy.
7. **Branch (seizures).** Sustained seizures can cause excitotoxic brain injury. This step is plausible but was not sourced here; mark it as inferred. [background, unsourced]

**Suggested GO terms** (look up IDs): acetylcholine catabolic process, cholinergic synaptic transmission, muscarinic acetylcholine receptor signaling pathway, regulation of muscle contraction.
**Suggested cell types:** skeletal muscle fiber, neuron, smooth muscle cell, exocrine gland cell (look up CL terms).
**Omics and advanced technologies:** nothing retrieved. Do not write placeholder content.

## 7. Anatomical Structures Affected

- **Primary systems.** Nervous system (central and autonomic), neuromuscular junction, respiratory tract and lungs, eye (pupil, ciliary muscle), exocrine glands, GI tract, heart. Look up UBERON terms for each.
- **Subcellular site.** The synaptic cleft and the AChE active site.
- **Lateralization.** Bilateral and systemic. Dermal exposure can cause localized sweating and fasciculation at the contact site. [background, unsourced]

## 8. Temporal Development

- **Onset.** Acute, from seconds to minutes after inhalation. Dermal onset is delayed (up to hours).
- **Course.** Self-limited if the patient survives the acute phase. Recovery of enzyme activity depends on new AChE synthesis. Some survivors have persistent symptoms: Tokyo survivors reported chronic eye and psychological symptoms for 10+ years ([PLoS ONE 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310687/)).
- **Critical period.** The oxime window is set by aging time (see section 6). Seizures need prompt control.

## 9. Inheritance and Population

- **Inheritance.** Not applicable.
- **Epidemiology.** Occurrence is incident-based.
  - Tokyo 1995: 13 deaths and over 6,000 sickened ([PLoS ONE 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310687/)).
  - Ghouta 2013: US estimate of 1,429 deaths ([Wikipedia, secondary](https://en.wikipedia.org/wiki/Ghouta_chemical_attack)).
  - A population rate cannot be given. Per the prevalence rules, `prevalence_class: NOT_YET_DOCUMENTED` or `CASES_IN_LITERATURE` is more appropriate than a made-up rate.
- **Demographics.** Civilians, military personnel and first responders. Children are affected, as in Ghouta. No sex-ratio data were retrieved.

## 10. Diagnostics

Not covered by the sources retrieved. Standard content, [background, unsourced]:
- Diagnosis is clinical, based on the cholinergic toxidrome, and treatment should not wait for lab confirmation.
- Red blood cell AChE and plasma BChE activity are supportive tests. Agent-specific adducts or metabolites (for example, BChE adducts, urinary alkyl methylphosphonates) are used in forensic confirmation.
- Differential diagnosis includes organophosphate or carbamate pesticide poisoning, other toxidromes and seizure disorders.
- There are no genetic or screening tests.

Find sources for these before curating them.

## 11. Outcome/Prognosis

- **Mortality.** Highly variable by agent, dose and access to treatment. Tokyo had a low fatality rate relative to casualties (13 of more than 6,000). No Ghouta mortality figure beyond the estimate above was retrieved.
- **Long-term.** Persistent somatic and psychological symptoms in Tokyo survivors (above).
- **Prognostic factors:** time to treatment and the agent's aging rate. [background, unsourced]

## 12. Treatment

All sourced to the search summaries of [Merck Manual](https://www.merckmanuals.com/en-ca/professional/injuries-poisoning/mass-casualty-weapons/nerve-chemical-warfare-agents), [Dawson 2023](https://jmvh.org/article/https-doi-ds-org-doilink-03-2023-52676377-jmvh-vol-8-no-3/) and [StatPearls](https://dev2.statpearls.com/articlelibrary/viewarticle/25716):

- **Atropine.** A competitive muscarinic antagonist that treats symptoms but does not affect the agent. The summaries give 2 mg IV every 5–10 minutes, with doses doubled if there is no improvement.
- **Oximes.** Nucleophiles that remove the phosphoryl group from AChE. Examples: pralidoxime (2-PAM), HI-6, obidoxime and MMB-4. They are ineffective once the enzyme has aged.
- **Benzodiazepines.** For seizures; they are part of autoinjectors and treatment regimens.
- **Supportive care.** Decontamination, airway management and ventilation. [background, unsourced]
- **Suggested NCIT treatment terms.** Pharmacotherapy `NCIT:C15986` and Supportive Care `NCIT:C15747` are from the project's CLAUDE.md list. Use `therapeutic_agent` for each drug (CHEBI), with `therapeutic_modality: SMALL_MOLECULE`.
- **Experimental therapy and trials.** Not searched. The Dawson 2023 review is a lead for newer oximes and adjuncts.
- **Pharmacogenomics.** Not retrieved.

## 13. Prevention

- Primary prevention rests on arms control, protective equipment and decontamination. Military pyridostigmine pretreatment is mentioned in section 2. [background, unsourced]
- Secondary and tertiary prevention include rapid antidote autoinjectors and psychological follow-up, given the PTSR figure above. No vaccines exist.
- Genetic counseling does not apply.

## 14. Other Species / Natural Disease

Nothing was retrieved, and there is no natural disease. Animals are affected as experimental subjects or by environmental release. NCBI Taxon, breed and OMIA entries do not apply.

## 15. Model Organisms

No sources were retrieved on models. Animal models exist (rodents, guinea pigs, non-human primates), as do in vitro AChE assays. I did not research them. [background, unsourced]

- Use `animal_models:` for whole-animal models, with `evidence_source: MODEL_ORGANISM`.
- Guinea pigs are commonly preferred for medical countermeasure studies because they have low plasma carboxylesterase. This is a claim to verify.
- Source animal-model and medical-countermeasure studies before adding entries.

---

## Gaps Before Curation
1. Find and cache primary sources, with PMIDs, for the following:
   - clinical series (Tokyo and Ghouta clinical papers);
   - the Salisbury case reports;
   - the aging kinetics of each agent;
   - oxime efficacy;
   - seizure and neuroprotection data.
2. Verify MONDO, ECTO, CHEBI, HP, GO, CL and UBERON terms by lookup.
3. Check the scope decision on lumping with organophosphate pesticide poisoning.
4. Add diagnostics, animal-model and epidemiology evidence. Those sections are currently unsourced.

## Sources Used
- [Merck Manual: Nerve Chemical-Warfare Agents](https://www.merckmanuals.com/en-ca/professional/injuries-poisoning/mass-casualty-weapons/nerve-chemical-warfare-agents)
- [Dawson, Recent Advances in the Treatment of Nerve Agent Poisoning (AMMA J, 2023)](https://jmvh.org/article/https-doi-ds-org-doilink-03-2023-52676377-jmvh-vol-8-no-3/)
- [StatPearls: Nerve Agents](https://dev2.statpearls.com/articlelibrary/viewarticle/25716)
- [Tokyo subway sarin attack long-term effects, PLoS ONE 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310687/)
- [Novichok evidence-based review, PMC9905702](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9905702/) and the [Frontiers in Toxicology version](https://www.frontiersin.org/journals/toxicology/articles/10.3389/ftox.2022.1004705/full)
- [Ghouta chemical attack (Wikipedia, secondary)](https://en.wikipedia.org/wiki/Ghouta_chemical_attack)
- [The Star Novichok summary (secondary)](https://www.thestar.co.uk/health/what-is-novichok-how-does-it-affect-the-body-symptoms-poisoning-salisbury-inquiry-4822683)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.

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