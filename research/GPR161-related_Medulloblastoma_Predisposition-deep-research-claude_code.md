---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-13T23:54:44.550199'
end_time: '2026-10-13T23:55:57.885568'
duration_seconds: 73.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: GPR161-related medulloblastoma predisposition
  mondo_id: MONDO:1010204
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
  - claude-sonnet-5-5
  web_search_requests: 4
  num_turns: 7
  total_cost_usd: 0.7374516999999999
  session_id: aa4f0803-31cb-5b9b-8409-a0195ed1b485
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC7658916
  relevance_assessed: 4
  on_topic: 4
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 2
  verified: 2
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
- **Disease Name:** GPR161-related medulloblastoma predisposition
- **MONDO ID:** MONDO:1010204 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GPR161-related medulloblastoma predisposition** covering all of the
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

# GPR161-related medulloblastoma predisposition: research report

**Evidence base and its limits.** This report rests on web-search abstract snippets and secondary summaries. The PMC full text was blocked by a reCAPTCHA page, so I did not read the primary paper's full text. I did not extract variant-level details (cDNA/protein changes, de novo versus inherited, ClinVar IDs) or the functional-assay results. I found no post-2021 case reports or cohorts. Per your attribution rules, items marked **[gap]** have no source in hand. Items marked **[inference]** are my reasoning beyond the sources. Every PMID or identifier I could not confirm is marked unverified.

**Source classes**
- Primary literature: Begemann et al., J Clin Oncol 2020, PMID:31609649 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/31609649/), [PMC6943973](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6943973/)).
- Commentary: [Cancer Discovery 9(12):1645](https://aacrjournals.org/cancerdiscovery/article/9/12/1645/10338/Germline-GPR161-Mutations-Are-Associated-With). I saw only its title.
- Reviews: [PMC7658916](https://pmc.ncbi.nlm.nih.gov/articles/PMC7658916/) and [PMC11341988](https://pmc.ncbi.nlm.nih.gov/articles/PMC11341988), as quoted in search snippets.
- Gene-panel curation: [Genomics England PanelApp panel 259](https://panelapp.genomicsengland.co.uk/panels/259/gene/GPR161/).
- Model-organism papers: Mukhopadhyay 2013, Shimada 2018, and an eLife knock-in study, seen through search summaries only.

## 1. Disease information

- **Entity.** GPR161-related medulloblastoma predisposition is a germline, heterozygous tumor-predisposition syndrome. It is defined by infant-onset SHH-subgroup medulloblastoma.
- **Identifiers.** MONDO:1010204 comes from your template and I did not verify it. OMIM, Orphanet, ICD, and MeSH were not checked [gap]. Medulloblastoma itself is OMIM #155255, and my search surfaced that entry.
- **Synonyms.** "Germline GPR161 mutations predispose to pediatric medulloblastoma" is the paper's title phrase. Other names [gap].
- **Data source.** The data come from patient cohorts in one study: families plus 1,044 medulloblastoma cases from international cohorts. They are not EHR-derived.
- **Lump/split, germline versus somatic (design decisions §3a).** Keep this germline syndrome separate from the somatic SHH-medulloblastoma entry. The reported tumor spectrum is a single tumor type.
- **Authors' own caveat.** The authors wrote that "Additional studies are needed to identify a potential broader tumor spectrum associated with germline GPR161 mutations." Whether this is a syndrome or a single-tumor susceptibility is open.

## 2. Etiology

- **Cause.** Heterozygous germline GPR161 loss-of-function variants, followed by a somatic loss of the wild-type allele.
  - Begemann 2020 (PMID:31609649, human clinical): "We identified heterozygous germline mutations in the G protein-coupled receptor 161 (GPR161) gene in six patients with infant-onset medulloblastoma (median age, 1.5 years)."
  - The same abstract: "Molecular tumor profiling revealed a loss of heterozygosity at GPR161 in all affected MB_SHH_ tumors… no additional somatic driver events."
- **Genetic risk modifiers.** None known [gap].
- **Environmental risk and protective factors.** None identified [gap]. Gene-environment interactions [gap].
- **Protective factors.** None identified [gap].

## 3. Phenotypes

All figures come from the single index study (six patients), which I read only in abstract form.

| Phenotype | HPO (verify before binding) | Frequency and notes |
|---|---|---|
| Medulloblastoma, SHH subgroup | HP:0002885 Medulloblastoma | All six patients. Median onset 1.5 years. The OMIM summary says the index case was a girl with SHH medulloblastoma at 12 months. |
| Other tumors | – | None reported [gap]. |
| Neural tube defects | – | Not reported in carriers [gap]. A bioRxiv preprint cites GPR161 variants in spina bifida patients (Kim et al. 2019, secondhand). |

- **Quality of life.** [gap]
- **Penetrance and exact frequencies.** [gap]. Do not infer them from a six-patient ascertainment series.
- **HPO term IDs.** These are from memory, so verify each by lookup before binding.

## 4. Genetic and molecular information

- **Gene.** GPR161, G protein-coupled receptor 161, on chromosome 1q24.
  - In this repo the HGNC CURIE is lowercase `hgnc:`. I did not look up the number, so no `hgnc:` ID is given here.
  - The chromosome position is from memory.
- **Variants.** Per the abstract, heterozygous, in six patients. The variant list is not read [gap]. Pull it from the paper's tables and from ClinVar.
- **ClinGen validity.** [gap]. Check for a CGGV record with `just clingen-list`.
  - PanelApp lists GPR161 as Green (high evidence) for "Childhood solid tumours cancer susceptibility" (panel 259).
  - A gene-panel rating is not a ClinGen assertion, so do not record it as `classified_by: CLINGEN`.
- **Allele frequency.** Search snippets quote the paper: "the carrier frequency is approximately 1 in 42,000 to 1 in 125,000 individuals". The gnomAD source for this was not checked.
- **Second hit.** Begemann 2020: "Analysis of 226 MB_SHH_ tumors revealed somatic copy-neutral loss of heterozygosity of chromosome 1q as the hallmark characteristic of GPR161 deficiency and the primary mechanism for biallelic inactivation."
  - This is classic two-hit biology.
  - Copy-neutral LOH on 1q fits the locus.
- **Functional consequence.** Loss of function is the working model [inference from LOH plus gene biology]. The paper's functional assays [gap].
- **Epigenetic, chromosomal, and modifier-gene information.** [gap]

## 5. Environmental information

None reported [gap]. No infectious agents are relevant.

## 6. Mechanism

**Causal chain** (the demonstrated links are the human genetic steps; most of the mechanism is from mouse work, and I only saw summaries of those papers):
1. A germline heterozygous GPR161 loss-of-function allele is present in all cells. *Demonstrated in patients (PMID:31609649).*
2. This leads to a somatic loss of the wild-type allele in a cerebellar lineage, mainly by copy-neutral LOH of 1q. *Demonstrated in the patients' tumors, which all showed LOH at GPR161.*
3. Biallelic loss of GPR161 removes a ciliary G-protein-coupled receptor that normally constitutively activates cAMP and PKA. *Mouse data (Mukhopadhyay 2013): "Gpr161 constitutively activates cAMP formation…"*
4. Loss of PKA activity reduces Gli3 repressor formation. *Mouse: "Gpr161 knockout embryos lack Gli3 repressor."*
5. This results in unrestrained, Smoothened-independent Hedgehog pathway activity. *Inferred for human tumors. It matches the SHH-subgroup restriction and the absence of other somatic drivers.*
6. Expansion and hyperproliferation of cerebellar granule neuron progenitors follows. *Mouse (Shimada 2018): conditional deletion in neural stem cells or granule cell progenitors "increased downstream activity of the Shh pathway by restricting Gli3-mediated repression, causing more extensive generation and proliferation of GC progenitors."*
7. Tumors arise, and tumor incidence and severity are higher with earlier deletion. *Mouse (Shimada 2018).* Early embryonic onset fits the infant presentation in humans [inference].

**Suggested ontology terms** (look up each before binding):
- Cell types: cerebellar granule cell precursor (CL), neural stem cell.
- GO processes: smoothened signaling pathway, adenylate cyclase-activating G protein-coupled receptor signaling, cilium-dependent signaling.
- Anatomy: cerebellum (UBERON).
- Cellular component: primary cilium.

**Not covered.** Immune, metabolic, omics, single-cell, and CRISPR-screen data [gap].

## 7. Anatomical structures affected

- **Organ and cell level.** Cerebellum, with granule neuron progenitors as the likely cell of origin [inference from mouse data, plus the usual SHH-medulloblastoma biology].
  - Cell of origin is derived from the pathograph in dismech. Mark the somatic second-hit node `variant_origin: SOMATIC` and bind the cell type there.
- **Lateralization.** [gap]

## 8. Temporal development

- **Onset.** Infancy, median 1.5 years (PMID:31609649).
- **Progression, staging, and remission.** [gap]
- **Critical period.** Infancy is the period of tumor presentation. The mechanism of the age restriction is [gap].

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant predisposition with a somatic second hit. Penetrance [gap].
  - Because penetrance is unknown, 5% of infant SHH cases carrying these variants does not give a penetrance figure.
- **Frequency among cases.** The paper reports about 5% of infant SHH medulloblastoma in its cohorts. A 2024 review reports 3.4% of pediatric SHH medulloblastoma (PMC11341988, snippet only).
  - These figures use different denominators: infant SHH versus pediatric SHH.
- **Carrier frequency.** About 1 in 42,000 to 1 in 125,000, as quoted from the paper above.
- **Incidence and prevalence of the syndrome.** [gap]
- **De novo versus inherited, parental carriers, family history, founder effects, and sex ratio.** [gap]. The paper began from families, so a familial component is implied, but I did not read the pedigree details.

## 10. Diagnostics

- **Germline testing.** A review recommends it: "patients with MB_SHH should be tested for germline ELP1 mutations, especially those presenting outside of infancy, and for germline GPR161 mutations, particularly those presenting in infancy" (PMC7658916).
  - Tumor LOH or 1q copy-neutral LOH is a flag for GPR161 deficiency (PMID:31609649).
- **Tumor diagnostics.** The standard medulloblastoma workup applies.
  - The molecular subgroup is SHH. Methylation profiling is the usual classifier [inference, not source-checked].
- **Differential.** SUFU, PTCH1, and TP53 germline predisposition, and ELP1 for older SHH patients.
- **Surveillance protocols.** [gap]. I found no GPR161-specific surveillance guideline. Do not borrow SUFU or PTCH1 protocols without saying so.

## 11. Outcome and prognosis

[gap]. No GPR161-specific survival or functional-outcome data were found. The same applies to prognostic factors and the quality-of-life measures.

## 12. Treatment

- No GPR161-specific treatment is documented [gap].
- **Dismech curation note.** Do not transfer SHH-inhibitor (SMO) logic to this entry as a treatment claim.
  - The mouse mechanism implies the defect lies downstream of Smoothened [inference]. If so, SMO inhibitors would be unlikely to work. That is a hypothesis, not a finding.
  - Standard infant medulloblastoma therapy and clinical trials [gap].

## 13. Prevention

- **Prevention and counseling.** Genetic counseling and cascade testing are standard for AD predisposition, but I have no GPR161-specific guidance [gap].
- **Radiation caution.** There is no GPR161 evidence on radiation sensitivity [gap]. Do not extrapolate from other syndromes.

## 14. Other species

- **Naturally occurring disease.** [gap]. Check OMIA.
- **Ortholog.** A mouse ortholog exists (Gpr161). NCBI Gene IDs were not looked up.

## 15. Model organisms

- **Germline knockout mouse** (Mukhopadhyay 2013, summary only).
  - Embryonic lethal by E10.5, with "ventralization throughout the rostro-caudal extent of the neural tube", craniofacial abnormalities, and open fore/mid brain regions and caudal neural tube defects.
  - Evidence class: model organism.
- **Conditional deletion** (Shimada 2018, Cell Reports, seen as scite report 29386106).
  - Deletion in neural stem cells or granule cell progenitors increased granule cell progenitor production.
  - "Earlier deletion of Gpr161 during embryogenesis increased tumor incidence and severity." Evidence class: model organism.
  - Fidelity to human disease: mouse tumors versus human infant SHH-medulloblastoma [gap]. The cilium-dependence finding is mouse-specific.
- **Ciliary-localization knock-in** (eLife, via search summary). A ciliary-localization-defective but cAMP-competent allele showed progenitor expansion in the intermediate neural tube that depends on Gli3 repressor loss. This suggests ciliary localization matters.
- **Human-model mismatch.**
  - The heterozygous carrier phenotype in mice is not described in my sources.
  - Whether the human neural tube defect signal is real is open.
  - Consider a `HUMAN_MODEL_MISMATCH` discussion on these.

## Curation leads, not yet checked

1. Read the full text of PMID:31609649 and copy the variant list.
2. Verify the PMIDs of Shimada 2018 and Mukhopadhyay 2013. Neither PMID is verified.
3. Run `just clingen-list` and check ClinVar for GPR161.
4. Fetch the cohort and survivor reviews and confirm the 3.4% figure.
5. Search for GPR161 papers after 2021, which my searches did not surface.
6. Confirm MONDO:1010204.

Sources:
- [Begemann et al., PubMed 31609649](https://pubmed.ncbi.nlm.nih.gov/31609649/)
- [PMC6943973](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6943973/)
- [Cancer Discovery 9(12):1645](https://aacrjournals.org/cancerdiscovery/article/9/12/1645/10338/Germline-GPR161-Mutations-Are-Associated-With)
- [PMC7658916](https://pmc.ncbi.nlm.nih.gov/articles/PMC7658916/)
- [PMC11341988](https://pmc.ncbi.nlm.nih.gov/articles/PMC11341988)
- [PanelApp panel 259](https://panelapp.genomicsengland.co.uk/panels/259/gene/GPR161/)
- [Shimada 2018 (scite)](https://scite.ai/reports/29386106)
- [Mukhopadhyay lab summary](https://labs.utsouthwestern.edu/mukhopadhyay-lab/research/ciliary-signaling-and-development)
- [eLife knock-in study](https://elifesciences.org/articles/67121.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC7658916`: "patients with MB_SHH should be tested for germline ELP1 mutations, especially those presenting outside of infancy, and for germline GPR161 mutations, particularly those presenting in infancy"
  - closest text in source: "Furthermore, we suggest that patients with MBSHH should be tested for germline ELP1 mutations, especially those presenting outside of infancy, and for germline GPR161 mutations, particularly those presenting in infancy"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.