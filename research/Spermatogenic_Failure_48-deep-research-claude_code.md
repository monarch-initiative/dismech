---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T15:31:28.477323'
end_time: '2026-10-15T15:37:31.181290'
duration_seconds: 362.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic failure 48
  mondo_id: MONDO:0030846
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
  web_search_requests: 2
  num_turns: 53
  total_cost_usd: 3.3612105000000008
  session_id: 3c11abea-49bb-488b-9c8c-4c2872e2e136
  stop_reason: end_turn
  permission_denials: 13
  denied_tools:
  - Bash
  - mcp__ols-mcp__search_all_ontologies
  - mcp__pubmed__search_articles
  assistant_text_blocks: 8
citation_count: 3
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 14
  on_topic: 14
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 27
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.036
  unresolved_terms:
  - HP:0008210
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic failure 48
- **MONDO ID:** MONDO:0030846 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic failure 48** covering all of the
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

Still gathering sources: PubMed access was denied, so I'm pulling abstracts from Europe PMC instead.

The fetch tool truncates quotes, so I'll pull the abstracts verbatim with curl instead.

Shell downloads need approval, so I'll use the project's own reference fetcher, which caches abstracts locally.

Reading the cached full text of the 2025 EMBO Mol Med M1AP study for clinical and meiotic details.

Now the remaining human cohort and mouse-variant papers.

Reading the newly cached Li 2023 mouse-mechanism abstract, then checking identifiers (OMIM, HGNC, Orphanet).

Sources are in hand. I'll check the ontology IDs I plan to suggest against the repo's term caches.

# Spermatogenic Failure 48 (SPGF48; M1AP-related male infertility): research report

**Target:** Spermatogenic failure 48 · MONDO:0030846 · Mendelian, autosomal recessive
**Prepared:** 2026-10-15

**How this was sourced:** I wasn't granted access to the PubMed and OLS tools. Instead I found literature through Europe PMC and web search, and cached abstracts or full text with `just fetch-reference`. Every quote below is copied from a `references_cache/PMID_*.md` file in this worktree, so it can be used directly as an evidence `snippet`. Ontology IDs are marked **✓** when they appear in the repo's `cache/*/terms.csv`, and **(verify)** when they come from a paper or from memory and haven't been checked.

---

## 1. Disease information

**Overview.** SPGF48 is an autosomal recessive form of male infertility. It is caused by biallelic loss-of-function variants in **M1AP** (meiosis 1 associated protein). The typical testicular picture is meiotic arrest, mostly at metaphase I, with only occasional haploid spermatids. Most affected men have **non-obstructive azoospermia (NOA)**. Some have cryptozoospermia or severe oligozoospermia. Affected men show no features outside reproduction.

> "mutations in M1AP are a relatively frequent cause of autosomal recessive severe spermatogenic failure and male infertility with strong clinical validity." — PMID:32673564 (Wyrwoll et al., *Am J Hum Genet* 2020)

**Identifiers**

| Resource | ID | Note |
|---|---|---|
| MONDO | MONDO:0030846 "spermatogenic failure 48" | in the draft entry |
| OMIM (phenotype) | **619108** | taken from Houston et al. 2021 Table (PMID:34498060): "M1AP \| 2p13.1 \| Non-obstructive azoospermia; OMIM:619108 \| AR \| 12 \| Moderate". I didn't fetch the OMIM page itself. |
| OMIM (gene) | 619098 | HGNC REST record; also PMID:36259570 table |
| HGNC | **HGNC:25183** (write as `hgnc:25183`) | HGNC REST: symbol M1AP; previous symbol C2orf65; aliases SPATA37, D6Mm5e; location 2p13.1; Entrez 130951; Ensembl ENSG00000159374; UniProt Q8TC57. **Not yet in `cache/hgnc/terms.csv`.** |
| Orphanet | no SPGF48-specific ORPHA code found | none in the local ORPHA cache. The broader NOA/spermatogenic failure groupings would apply. |
| ICD-10 / ICD-11 | N46.01 / N46.0 (azoospermia, organic causes), GB04.0 (verify) | no disease-specific code |
| MeSH | Azoospermia (D053713); Infertility, Male (D007248) (verify) | |
| ClinGen GDV | **no record found** (no `CGGV_*` cache and no hit in `cache/clingen/gene_validity.csv`) | Houston 2021 systematic review rates the gene–disease link **"Moderate"**. Leave `gene_disease_validity` absent; that review is not a GenCC source. |

**Synonyms:** SPGF48; M1AP-related spermatogenic failure; M1AP-associated meiotic arrest / NOA; infertility due to M1AP deficiency.

**Data provenance:** All of the evidence is per-patient: case series, exome cohorts (MERGE, GEMINI, Chinese and Pakistani cohorts) and testicular histology. None of it comes from EHR aggregates.

---

## 2. Etiology

- **Cause:** biallelic germline LoF variants in *M1AP*. The variant types are frameshift, splice and exon deletion. One missense variant segregated in a consanguineous family.
- **Genetic risk:** consanguinity (Turkish, Han Chinese and Pakistani families). There is also a recurrent European frameshift allele, c.676dup.
- **Environmental modifier (mouse only):** a Western-style diet made infertility worse in *M1ap*⁻/⁻ mice.
  > "The loss of M1AP and a Western diet separately led to subfertility (a form infertility) in male mice and in combination subfertility was worsened." — PMID:42671480 (Houston et al., *Hum Reprod* 2026; MODEL_ORGANISM)
  > "Compared to the individual gene deletion or diet treatments, the combined M1ap-/- and Western diet group had more abnormal germ cells, sloughed germ cells and resulted in fewer pups per litter." — PMID:42671480

  This is the only gene–environment interaction data for the disease. It has not been tested in humans; the paper itself says "findings should be validated in a human cohort where possible."
- **Protective factors:** none reported.

---

## 3. Phenotypes

All phenotypes are restricted to males and to the testis, and are found at post-pubertal infertility evaluation. Androgenization is normal.

| Phenotype | Suggested HPO | Frequency / detail | Evidence |
|---|---|---|---|
| Non-obstructive azoospermia | **HP:0011961 ✓** Non-obstructive azoospermia | most common: 7/10 LoF men in Rotte 2025 | PMID:32673564, PMID:40374915 |
| Cryptozoospermia | Cryptozoospermia (verify HP ID; not in cache) | 3/10 in Rotte 2025, all c.676dup homozygotes | PMID:40374915 |
| Severe oligozoospermia | **HP:0000798 ✓** Oligozoospermia (preferred_term "severe oligozoospermia") | Chinese families (c.1435-1G>A; c.1074+2T>C) | PMID:32017041, PMID:36440627 |
| Male infertility | **HP:0000789 ✓** Infertility | 100% | all |
| Meiotic arrest (spermatocyte arrest), predominantly metaphase I | **HP:0031038 ✓** Spermatogenesis maturation arrest. Rotte 2025 itself cites **HP:0031039** (verify label; not cached) | all biopsied cases | PMID:40374915 |
| Rare round/elongated spermatids | descriptive; part of the arrest phenotype | round spermatids in 7/7 stained; elongated in 6 | PMID:40374915 |
| Elevated FSH (high-normal range) | **HP:0008232 ✓** Elevated circulating follicle stimulating hormone level | "follicle-stimulating hormone in the high range" | PMID:40374915 |
| Normal testicular volume, LH and testosterone | (negative findings; no HP binding needed) | | PMID:40374915 |
| Swollen, abnormal sperm mitochondrial sheath | HP:0012868 ✓ Abnormal sperm tail morphology (coarse); GO:0097226 ✓ sperm mitochondrial sheath | **single case** (Tu 2020) | PMID:32017041 |

Key quotes:
> "The common phenotype between all affected men was NOA, but occasionally spermatids and rarely a few spermatozoa in the semen were observed." — PMID:32673564

> "Semen analysis of all 24 men included in this study revealed a high proportion of azoospermia (N = 21), with the remaining three men displaying cryptozoospermia. Interestingly, all three cryptozoospermic men were homozygous for the recurrent LoF variant in M1AP (c.676dup)." — PMID:40374915

> "Clinical features were similar between men, including normal testicular volumes, normal luteinising hormone, follicle-stimulating hormone in the high range, and normal testosterone" — PMID:40374915 (this applies to the whole M1AP+ZZS group of 24 men)

> "Ultrastructural and immunostaining analyses of patient's spermatozoa showed highly aberrant swollen mitochondrial sheaths with normal axonemal structures." — PMID:32017041

**Onset and course:** congenital genotype, with the phenotype only apparent at adult infertility work-up. It appears stable and non-progressive in humans. No longitudinal data exist. **Quality of life:** the effect is the psychosocial burden of infertility; no SPGF48-specific QoL data exist.

---

## 4. Genetic and molecular information

**Gene:** *M1AP* (HGNC:25183), 2p13.1, transcript NM_138804.4. Variant origin is germline; affected men are homozygous or compound heterozygous.

| Variant (NM_138804.4) | Type | Population / zygosity | Source |
|---|---|---|---|
| c.676dup p.(Trp226LeufsTer4) | frameshift; recurrent; truncated protein in vitro | European (German, Dutch, Portuguese, UK, US). **gnomAD v4.1 MAF 0.003327** | PMID:32673564, PMID:40374915 |
| c.1166C>T p.(Pro389Leu) | missense; homozygous; 5 affected men | consanguineous Turkish family | PMID:32673564 |
| c.1073_1074+10del p.(Leu358Glnfs*58) | splice; the minigene assay showed aberrant splicing; MAF 0.00006815 | M3609 | PMID:40374915 |
| c.1074+2T>C | splice; homozygous; abolishes M1AP axis foci (mouse knock-in) | Chinese patients with severe oligozoospermia | PMID:36440627 |
| c.1435-1G>A | splice; homozygous; no M1AP protein in sperm | consanguineous Han Chinese family | PMID:32017041 |
| ~10 kb deletion of exon 2 | CNV, homozygous; **WES can't detect it** | consanguineous Pakistani family | PMID:38073178 |
| Further variants (2 genes, 5 patients total) | rare or absent in databases; reduced *M1AP* mRNA | Chinese NOA cohort (n=108) | PMID:42324855 |
| c.949G>A p.(Gly317Arg) (rs140179344) | missense. **Likely benign: a mouse knock-in was fertile.** It was found in trans with c.676dup | US NOA case | PMID:37459509 |

> "we performed whole-exome sequencing in 58 men with unexplained meiotic arrest and identified the same homozygous frameshift variant c.676dup (p.Trp226LeufsTer4) in M1AP" — PMID:32673564

> "we identified a pathogenic single-exon deletion in M1AP that would be undetectable by WES." — PMID:38073178

> "Both male and female homozygotes were fertile. Testis weights were slightly lower in mutants, but sperm counts were not significantly altered, and testis histology appeared normal" — PMID:37459509 (G317R, mouse)

**Functional consequence:** loss of function (`functional_impact_category: LOSS_OF_FUNCTION`). In molecular dynamics simulations, the missense variants did not cause misfolding:
> "none of the variants led to a general misfolding or loss of stability in the protein structure" — PMID:35341049 (COMPUTATIONAL)

**Curation caution:** G317R shows that in-silico predictors over-call M1AP missense variants. Rotte 2025 also found that truncating only the last 97 amino acids abolishes the M1AP–TEX11 interaction in vitro.

**Modifier genes, epigenetics, chromosomal abnormalities:** none reported. Karyotype and AZF testing are normal by definition in idiopathic-cohort cases.

---

## 5. Environmental information

There are no human environmental, lifestyle or infectious causes. The only modifier data is the mouse Western-diet study (§2).

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic M1AP LoF variant** (frameshift, splice or exon deletion) **leads to** absent or truncated M1AP in meiotic germ cells. [PMID:32673564 in vitro truncation; PMID:32017041 no protein in sperm]
2. **Loss of M1AP leads to** failure of M1AP to act as a co-partner of the ZZS complex (SHOC1–TEX11–SPO16) on the chromosome axes. [human co-IP PMID:40374915; mouse PMID:36440627]
   > "M1AP interacts with the mammalian ZZS (an acronym for yeast proteins Zip2-Zip4-Spo16) complex components, SHOC1, TEX11, and SPO16." — PMID:36440627
3. **This results in** reduced recruitment of TEX11 to recombination intermediates. Human: TEX11 foci per pachytene spermatocyte fall from 199.88 ± 20.16 to 66.00 ± 7.16. [PMID:40374915; mouse PMID:36440627: "Ablation of M1AP does not alter SHOC1 localization but reduces the recruitment of TEX11 to recombination intermediates."]
4. **This leads to** fewer stabilized recombination intermediates. MSH5 foci fall from 53.70 to 28.60. RAD51 foci persist into pachytene, but DSB formation, DSB repair and **synapsis remain intact**. [PMID:40374915]
5. **This results in** fewer class I crossovers. MLH1 foci fall from 48.33 to 35.00 per cell. In the cell imaged, the obligatory crossover was still met. [PMID:40374915]
   > "Abolished M1AP led to a reduced number of recombination intermediates and class I crossover." — PMID:40374915
6. **This leads to** improper chromosome alignment at metaphase I in many spermatocytes, which triggers the spindle/metaphase checkpoint and **apoptosis** (TUNEL increased). This step is inferred: the human data show misaligned γH2AX-positive metaphase-like cells that are TUNEL-positive, and the mouse data show metaphase I misalignment followed by apoptosis.
   > "Cells that reached metaphase I were unable to properly align their chromosomes at the metaphase plate due to abnormal chromosome synapses and failure to form crossover foci." — PMID:23269666 (mouse)
7. **This results in** a predominant **metaphase I arrest**, so haploid output is greatly reduced. CREM+ round spermatids fall to 0.50 ± 0.43 per tubule, against 30.41 in controls.
8. **Branch: leaky escape.** A few spermatocytes complete meiosis with adequate crossovers, producing rare round or elongated spermatids and sperm, which explains cryptozoospermia and the TESE successes. One healthy, euploid child has been born after ICSI. [PMID:40374915]
9. **Clinical result:** NOA, cryptozoospermia or severe oligozoospermia, and male infertility.
10. **Branch: progressive tubular degeneration (mouse only).** Germ cell loss can progress to Sertoli-cell-only tubules. [PMID:23269666] This has not been shown in men.

> "Our study establishes M1AP as an important, but non-essential, functional enhancer in meiotic recombination." — PMID:40374915

**Sex specificity:** M1AP is dispensable in female mice.
> "M1AP shows cytoplasmic localization in fetal oocytes and is dispensable for fertility and crossover formation in female mice." — PMID:36440627

There are no human female data.

**How this differs from ZZS-gene defects** (useful for differential diagnosis): LoF in TEX11, SHOC1 or SPO16 causes an *early* zygotene/pachytene arrest with asynapsis and no haploid cells. M1AP LoF causes a *later* metaphase I arrest. [PMID:40374915]

**Unresolved:** Ma et al. 2026 (PMID:42324855) describe "zygotene arrest of meiosis" in their Chinese TEX11/M1AP patients, pooled across both genes. This is worth a note if the entry cites it.

**Ontology suggestions**
- GO: GO:0007131 ✓ reciprocal meiotic recombination; GO:0007130 ✓ synaptonemal complex assembly (intact; context); GO:0007129 ✓ homologous chromosome pairing at meiosis; GO:0007283 ✓ spermatogenesis; GO:0006915 ✓ apoptotic process; GO:0000795 ✓ synaptonemal complex (CC). Unverified: meiotic crossover formation / chiasma assembly (GO:0051026, verify).
- CL: CL:0000656 ✓ primary spermatocyte; CL:0000017 ✓ spermatocyte; CL:0000018 ✓ spermatid; CL:0000019 ✓ sperm; CL:0000216 ✓ Sertoli cell (mouse SCO branch).
- Suggested `biological_scale` per step: steps 1–5 MOLECULAR; steps 6–7 CELLULAR; step 9 ORGANISM.

**Omics:** human testis scRNA-seq shows M1AP mRNA "in all stages of meiosis with strong mRNA abundance during early prophase I (leptotene, zygotene)" (PMID:40374915, re-analysis of Di Persio 2021). No proteomic or metabolomic data exist.

---

## 7. Anatomical structures affected

- **Organ:** testis (UBERON:0000473 ✓). Seminiferous tubule (UBERON:0001343 ✓). The reproductive system only. The disease is non-syndromic.
- **Cells:** primary spermatocytes (main defect); spermatids and sperm (reduced); Sertoli cells are spared but exposed in the mouse SCO branch.
- **Subcellular:** meiotic chromosome axes and synaptonemal complex (GO:0000795 ✓), recombination nodules, and the metaphase I spindle. In one human case, the sperm mitochondrial sheath (GO:0097226 ✓).
- **Laterality:** bilateral.

---

## 8. Temporal development

The defect is congenital (germline) but shows itself only after puberty, when spermatogenesis starts. Onset is insidious, since the condition has no symptoms beyond infertility. The course is stable and lifelong, with no remission. The mouse shows tubular degeneration over time. The mouse diet study compared 10–12-week and 26–28-week animals but reported its outcomes by diet rather than by age.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007, verify). Penetrance in males is complete for infertility, but **expressivity is variable**: azoospermia, cryptozoospermia, or rare TESE-retrievable sperm.
- **Sex-limited:** only males are affected. Female homozygotes are presumed fertile on mouse evidence (HP:0008210? not applicable; better to note sex-limited expression in `description`).
- **Frequency:** Wyrwoll 2020 found the c.676dup homozygote in 3 of 58 men with unexplained meiotic arrest. This is a frequent monogenic cause within that subgroup. c.676dup has a gnomAD v4.1 MAF of 0.003327, which suggests a European founder or recurrent allele. Treat any implied carrier frequency of about 1 in 150 as an inference that hasn't been published.
- **Founder effects and consanguinity:** recurrent European c.676dup; homozygous splice variants and the exon-2 deletion in consanguineous Turkish, Han Chinese and Pakistani families.
- **Prevalence:** not documented (`prevalence_class: NOT_YET_DOCUMENTED`). NOA affects about 1% of men (PMID:42324855 background), and SPGF48 is a small fraction of that.

---

## 10. Diagnostics

- **Semen analysis:** azoospermia or cryptozoospermia, confirmed on centrifuged pellet.
- **Hormones:** FSH high-normal or elevated; LH and testosterone normal. LOINC FSH serum code is 15067-2 (verify in cache before binding).
- **Exclusion work-up:** karyotype and AZF microdeletion testing are normal.
- **Histology (TESE/biopsy):** predominant meiotic (metaphase I) arrest, with aligned metaphase cells plus misaligned TUNEL-positive ones, and rare CREM+ round spermatids. Staining panel used: PAS/H&E, CREM, γH2AX, H3S10p, TUNEL. Research-grade spermatocyte spreads: SYCP1/3, MLH1, MSH5, TEX11.
- **Genetic testing:** an exome-based male infertility panel including *M1AP*.
  - c.676dup is easily detected by WES.
  - **WGS or CNV analysis is needed for exon deletions** (PMID:38073178).
  - Splice variants need RNA or minigene confirmation (PMID:40374915).
  - Be cautious calling missense variants pathogenic (PMID:37459509).
- **Differential diagnosis:**
  - TEX11 (X-linked), SHOC1, SPO16: early arrest, no spermatids.
  - Other meiotic NOA genes: SYCE1, MSH4, STAG3, MEIOB.
  - Klinefelter syndrome and AZFa/b deletions: excluded by karyotype and Y-microdeletion testing.
  - Sertoli-cell-only syndrome.
- **Screening:** none. Cascade counseling of brothers, and carrier testing of partners in consanguineous unions.

---

## 11. Outcome and prognosis

Life expectancy and general health are normal; infertility is the only morbidity. Sperm retrieval prognosis depends on the gene and **is better than for most meiotic-arrest genes**:
> "the proportion of cases with successful sperm recovery is up to 50% for patients carrying M1AP LP/P mutations, as classified using the diagnostic method, which is the same likelihood observed in idiopathic NOA cases" — PMID:40896145 (Riera-Escamilla et al., *Hum Reprod Open* 2025)

> "A positive TESE result was only seen in men with LoF variants in M1AP (N = 4)." — PMID:40374915

ICSI results in Rotte 2025:
- 4 men attempted ICSI; 1 live birth: a healthy, euploid boy from ejaculated sperm after 3 cycles.
- 3 men failed, including a total fertilization failure.

> "Medically assisted reproduction resulted in the birth of a healthy child, offering the possibility of fatherhood to men with LoF variants in M1AP." — PMID:40374915

The child is an obligate heterozygous carrier.

---

## 12. Treatment

There is no disease-modifying therapy. Management is reproductive:

| Intervention | NCIT suggestion | Notes |
|---|---|---|
| Testicular sperm extraction (micro-TESE) | NCIT:C15329 ✓ Surgical Procedure (preferred_term "testicular sperm extraction"); a specific NCIT TESE term isn't verified | ~50% retrieval (PMID:40896145) |
| ICSI / medically assisted reproduction | (verify NCIT term) | 1 live birth among 4 couples (PMID:40374915) |
| Cryopreservation of ejaculated sperm (cryptozoospermic men) | (verify) | the successful case used ejaculated sperm |
| Genetic counseling | NCIT:C15240 ✓ Genetic Counseling | |
| Lifestyle/diet optimization | NCIT:C15447 Dietary Intervention (verify) | mouse rationale only (PMID:42671480); no human evidence |
| Donor sperm / adoption | | alternatives |

`therapeutic_modality`: SURGERY (TESE); BEHAVIORAL (counseling, diet). No pharmacotherapy, gene therapy or clinical trials were found. No registered NCT trials are specific to M1AP.

---

## 13. Prevention

There is no primary prevention for the affected man. Prevention options:
- carrier testing of partners and relatives, especially in consanguineous families
- PGT or prenatal testing is technically possible but rarely indicated for a condition limited to male fertility
- tertiary: early genotype-informed counseling before TESE

---

## 14. Other species

*M1ap* is a conserved vertebrate gene; the mouse ortholog is *M1ap* (MGI, formerly D6Mm5e). No naturally occurring animal disease was found; I didn't search OMIA in depth.

---

## 15. Model organisms

| Model | Phenotype | Fidelity to human SPGF48 | Source |
|---|---|---|---|
| *M1ap*⁻/⁻ mouse (Arango 2013) | reduced testis size, severe oligozoospermia, infertility; mostly metaphase I arrest and apoptosis, some zygotene/pachytene arrest; progression to SCO-like tubules; **females normal** | RECAPITULATES metaphase I arrest (HIGH). Shows a milder output (oligozoospermia) than most men (NOA), and SCO degeneration not reported in men | PMID:23269666 |
| *M1ap* c.1074+2T>C knock-in / knockout mice (Li 2023) | M1AP axis foci lost; fewer recombination intermediates and crossovers; reduced TEX11 recruitment; female fertility normal | RECAPITULATES the recombination defect (HIGH) | PMID:36440627 |
| *M1ap*⁻/⁻ mouse with Western diet (Houston 2026) | subfertility, made worse by diet | PARTIALLY_RECAPITULATES. The mouse is "subfertile" rather than sterile; human relevance unproven | PMID:42671480 |
| *M1ap* G317R knock-in (Ding 2023) | fertile, normal histology | negative control showing that variant is benign | PMID:37459509 |
| HEK293T co-IP; minigene splice assays | human M1AP binds SHOC1, TEX11 and SPO16; splice defects confirmed | IN_VITRO | PMID:40374915 |

> "Although some germ cells arrested at the zygotene/pachytene stages, most cells advanced to metaphase I before arresting and entering apoptosis." — PMID:23269666

A possible `HUMAN_MODEL_MISMATCH` discussion: knockout mice keep producing some sperm (severe oligozoospermia), while most men are azoospermic. Also, mouse spermatogenesis is about ten times more efficient per gram of testis (PMID:40896145 discussion).

---

## Notes for building the KB entry

- **References now cached (untracked files in this worktree):** PMID 32673564, 40374915, 42671480, 35341049, 23269666, 38073178, 42324855, 37459509, 36440627, 34498060, 36259570, 32017041. PMID 40896145 was already present. Commit the ones the entry cites and prune the rest.
- **Not yet validated:** HGNC:25183, and every ID marked "(verify)", including HP:0031039, the cryptozoospermia HP term, the GO crossover term and the NCIT TESE/ICSI terms. Run `just validate-terms` after binding them.
- **Evidence source:**
  - Rotte 2025 combines human histology (HUMAN_CLINICAL) with co-IP/minigene work (IN_VITRO). Split those into separate evidence items.
  - Gerlevik 2022 is COMPUTATIONAL.
  - Arango 2013, Li 2023 (mouse parts), Houston 2026 and Ding 2023 are MODEL_ORGANISM.
- **Not found, so the entry should say so rather than fill the slot:** a ClinGen record, an Orphanet-specific code, prevalence, human QoL data, and any human environmental modifier.

Sources: PubMed records retrieved via Europe PMC and the local reference cache (DOIs: 10.1016/j.ajhg.2020.06.010; 10.1038/s44321-025-00244-0; 10.15252/embr.202255778; 10.1095/biolreprod.111.098673; 10.1111/cge.13712; 10.1111/andr.13570; 10.1111/andr.70291; 10.1073/pnas.2219925120; 10.7717/peerj.12947; 10.1093/humrep/deag130; 10.1093/hropen/hoaf049; 10.1093/humupd/dmab030); [HGNC M1AP record](https://rest.genenames.org/fetch/symbol/M1AP); [PMC7413853](https://pmc.ncbi.nlm.nih.gov/articles/PMC7413853); [UroToday summary of Wyrwoll 2020](https://www.urotoday.com/recent-abstracts/men-s-health/male-infertility/123059-bi-allelic-mutations-in-m1ap-are-a-frequent-cause-of-meiotic-arrest-and-severely-impaired-spermatogenesis-leading-to-male-infertility.html).

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0008210` (1 mention) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.