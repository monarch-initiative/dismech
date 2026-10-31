---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T01:56:32.485564'
end_time: '2026-10-23T02:02:39.420085'
duration_seconds: 366.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Myopathy 27
  mondo_id: MONDO:0979897
  category: Mendelian
  causal_genes: PACSIN3
  omim_id: not recorded
  synonyms: not recorded
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
  web_search_requests: 5
  num_turns: 32
  total_cost_usd: 2.8890599000000003
  session_id: 7037a760-53c0-469d-b423-65f999e5b2fe
  stop_reason: end_turn
  permission_denials: 8
  denied_tools:
  - Bash
  - mcp__ols-mcp__search_all_ontologies
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:16627472
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myopathy 27
- **MONDO ID:** MONDO:0979897 (if available)
- **Causal gene(s):** PACSIN3
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Myopathy 27** covering all of the
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

I've pulled the primary-case data from Genomics England PanelApp and GenCC. Next I'm getting the clinical detail from the 2024 Brain paper and the OMIM entry.

I'm checking the ontology IDs against OLS now, so the report doesn't cite any term from memory. Then I'll write it.

# Congenital Myopathy 27 (CMYO27; PACSIN3-related myopathy): Research Report

**Target:** Congenital myopathy 27, MONDO:0979897 · OMIM #621343 · causal gene **PACSIN3** (syndapin III; HGNC:8572, written `hgnc:8572` in this repo; OMIM *606513; 11p11)

**How this report was built (2026-10-23)**
- The PubMed and OLS tools were not permitted in this session.
- The evidence comes from four sources:
  - the full texts already in `references_cache/` (PMID:29202928, PMID:34990060, PMID:36980283);
  - the publisher full text of the index case report (PMID:38637313). Its cache file has **no body text**, because it is a letter without an abstract;
  - Genomics England PanelApp, GenCC and the Disease Ontology;
  - web-verified bibliographic records for three further functional papers.
- Ontology IDs marked ✔ were checked against this repository's committed `cache/*/terms.csv` label caches. Those caches confirm the ID and label exist; they do not confirm dynamic-enum membership. IDs marked ⚠ were **not** verified and must be looked up before binding.
- "Quote" means verbatim text from the source.

---

## 1. Disease Information

**Overview.** CMYO27 is an autosomal recessive, childhood-onset myopathy caused by biallelic loss-of-function (truncating) variants in **PACSIN3**. PACSIN3 encodes syndapin III, the muscle-enriched F-BAR membrane-shaping protein needed to form caveolae made with caveolin-3. Clinically it is mild:
- persistent hyperCKaemia (about 650–1,800 U/L);
- exercise intolerance, early fatigue and muscle pain;
- normal strength on examination;
- non-specific myopathic biopsy changes.

The defining publication describes three girls from two unrelated families (Distelmaier et al., *Brain* 2024; PMID:38637313). The authors propose that the disorder extends the **caveolinopathy** spectrum.

**Identifiers**

| Resource | ID / label |
|---|---|
| MONDO | MONDO:0979897 *congenital myopathy 27* |
| OMIM (phenotype) | #621343 |
| OMIM (gene) | *606513 PACSIN3 |
| Disease Ontology | DOID:0061258 *congenital myopathy 27* (parents DOID:0081337 congenital myopathy; DOID:0050737 autosomal recessive disease) |
| HGNC | `hgnc:8572` PACSIN3 ✔ |
| Orphanet / ICD-10 / ICD-11 / MeSH | None found specific to this entity. It falls under generic congenital myopathy codes. |

**Synonyms:** CMYO27; "childhood-onset myopathy with hyperCKaemia" (the title of the index report); PACSIN3-related myopathy. Disease Ontology lists no synonyms.

The Disease Ontology definition reads: *"a congenital myopathy characterized by exercise intolerance and early fatigue that has_material_basis_in homozygous or compound heterozygous mutation in the PACSIN3 gene on chromosome 11p11."*

**Data provenance.** All clinical knowledge comes from individual-patient case descriptions (one published letter) plus one unpublished GenCC submitter case. There are no aggregate cohort, registry or EHR data.

## 2. Etiology

- **Causal factor:** germline biallelic truncating PACSIN3 variants leading to loss of PACSIN3 protein. Quote: *"Genetic and immunoblotting data indicate a loss-of-function effect as the underlying cause."* (PMID:38637313)
- **Genetic risk factors:** biallelic null alleles, which by inference come with consanguinity (Family 2 parents were first-degree consanguineous). No susceptibility loci, modifier genes or GWAS signals are known.
- **Environmental / lifestyle risk:** none established in humans.
  - Physical exertion is the mechanistically predicted aggravating factor. In the knockout mouse, muscle damage appears **only after exercise training** (PMID:29202928; MODEL_ORGANISM).
  - This is a gene × environment hypothesis supported by the animal data, not by human data.
- **Protective factors:** none known.

## 3. Phenotypes

Denominators are 3 published patients (P1, P2A, P2B). Frequencies are raw counts; with n=3 they carry no statistical meaning.

| Phenotype | Type | Frequency | Onset / course | HPO suggestion |
|---|---|---|---|---|
| Elevated serum CK: P1 1,000–1,800 U/L (ref <228); P2A 649–1,291 IU/L (ref 44–189); P2B 769–991 IU/L | Lab | 3/3 | Childhood, persistent | HP:0003236 *Elevated circulating creatine kinase activity* ✔ (or HP:0030234 *Highly elevated creatine kinase* ✔) |
| Exercise intolerance | Symptom | 3/3 (reported by parents) | Childhood | HP:0003546 *Exercise intolerance* ✔ |
| Early fatigue | Symptom | 3/3 | Childhood, variable | HP:0012378 *Fatigue* ✔ |
| Muscle pain | Symptom | 1/3 (P1) | Variable | HP:0003326 *Myalgia* ✔ |
| Infantile hypotonia | Sign | 1/3 (P1; resolved, tone normal at age 5) | Infancy | HP:0001252 *Hypotonia* ✔ |
| Moderately delayed motor milestones (walked at 2 y) | Sign | 1/3 (P1; Family 2 milestones on time) | Infancy | HP:0001270 *Motor delay* ✔ |
| Feeding difficulties, poor weight gain, constipation | Sign | 1/3 (P1, born preterm at 32 weeks; possibly confounded by prematurity) | First months | HP:0011968 ✔, HP:0001531 *Failure to thrive in infancy* ✔, HP:0002019 ✔ |
| Mildly raised transaminases (GOT/GPT); raised CK-MB 80–90 U/L (P1) | Lab | 2/3 | — | HP:0031956 ✔, HP:0031964 ✔. These are most likely muscle-derived. |
| Fibre-size variation | Biopsy | 3/3 | — | HP:0003557 ✔ |
| Internal nuclei | Biopsy | 2/3 (P2A, P2B) | — | HP:0031237 *Internally nucleated skeletal muscle fibers* ✔ |
| Increased endomysial connective tissue (focal) | Biopsy | 1/3 (P2B) | — | HP:0100297 ✔ |
| Membranous tubules / tubular-aggregate-like stacks; subsarcolemmal vacuoles with membranous cytoplasmic bodies; focal glycogen (EM) | Ultrastructure | 1/3 (P1; the only patient with EM) | — | "Tubular aggregates" ⚠ (HP term not in local cache) |

**Pertinent negatives** (useful for differential diagnosis and for NO_EVIDENCE/REFUTE items):
- Normal strength, tone and reflexes in all three patients.
- No muscle rippling, mounding or percussion-induced repetitive contractions (PIRCS), which are features of CAV3 rippling muscle disease.
- Normal EMG and nerve conduction studies (P2A, P2B).
- Normal muscle ultrasound (P1).
- Normal cardiac work-up (all), including echocardiography and ECG (Family 2).
- Normal respiratory function (Family 2).
- Normal cognition (P1).
- No new features at follow-up ages 11.5 and 9.5 years.

**Quality of life:** no formal instruments (EQ-5D, SF-36, PROMIS) have been reported. The impact is functional: fatigue, pain and malaise limit exercise.

## 4. Genetic / Molecular Information

**Gene:** PACSIN3 (NM_016223.5). The protein has an N-terminal F-BAR domain and a C-terminal SH3 domain. Unlike PACSIN1/2 it lacks NPF motifs (PMID:34990060). Expression is enriched in skeletal muscle, heart and lung.

**Published pathogenic variants (PMID:38637313):**

| Family | Variant (NM_016223.5) | Zygosity | Type | Segregation |
|---|---|---|---|---|
| 1 (German, non-consanguineous; 1 affected) | c.270_277del p.(Leu91AlafsTer15) + c.609_610del p.(Lys203AsnfsTer4) | Compound heterozygous | Frameshift | Each parent heterozygous (Sanger) |
| 2 (Turkish, first-degree consanguineous; 2 affected) | c.592G>T p.(Glu198Ter) | Homozygous | Nonsense | Parents and sibling 2C heterozygous; sibling 2D wild-type |

- The authors predict nonsense-mediated decay. Quote: *"Both aberrant mRNA species are prone to nonsense-mediated decay."*
- Patient fibroblasts show no detectable PACSIN3 protein. Quote: *"Immunoblotting revealed absence of PACSIN3 in patient-derived fibroblasts"* (IN_VITRO; P < 0.001 across 4 experiments).
- The functional class is **LOSS_OF_FUNCTION**, through null alleles.
- Alternative diagnoses excluded in P2A: DMD MLPA, chromosomal microarray and clinical exome were normal.

**Additional case (unpublished):** a LiferaOmics GenCC submission (SGC-179464.1, 2026-04-05) describes a further homozygous null proband from a consanguineous family who also has ARSB-related MPS VI. The submitter treats PACSIN3 as a contributor to the hyperCKaemia/myopathy phenotype rather than the sole cause.

**Curation status:**
- **GenCC (LiferaOmics):** *Moderate* for PACSIN3 with myopathy (MONDO:0005336), AR, scored 7.5/18. The score breaks down as 4.0/12 genetic and 3.5/6 experimental. The page's experimental subtotals are internally inconsistent (2.5 vs 3.5).
- **Genomics England PanelApp, Congenital myopathy panel 225:** Amber as of 2026-06-09. Both reviewers (GOSH and a Genomics England curator) support Green, and the gene is tagged for promotion.
- **Gene2Phenotype:** rated "moderate" on its developmental-disorders (DD) panel, per PanelApp.
- **ClinGen:** no Gene-Disease Validity assertion found, so no `gene_disease_validity` tier should be recorded.

**Not available:**
- ClinVar classifications for these specific alleles and gnomAD allele frequencies were not retrieved.
- No modifier genes, epigenetic factors, chromosomal abnormalities or somatic contribution have been described.
- **The origin is germline.**

## 5. Environmental Information

There are no environmental, lifestyle or infectious causes. Physical exercise acts as an unmasking or aggravating stressor in the mouse model (see §6). This has not been studied in patients.

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic truncating PACSIN3 variants → no PACSIN3 protein.** Truncating alleles are predicted to undergo nonsense-mediated decay (predicted). Absence of protein is demonstrated in patient fibroblasts (PMID:38637313; human-derived, IN_VITRO).
2. **Loss of syndapin III → failed invagination of caveolin-3-coated caveolae at the muscle sarcolemma.** Demonstrated in the knockout mouse, inferred in humans.
   - Syndapin III sits at caveolar **necks**, the zones of curvature transition. Quote: *"syndapin III was not found at the lateral walls or at the bottom of caveolar invaginations but was restricted to areas of membrane curvature transition from the caveolar invagination to the continuum of the plasma membrane."*
   - Its F-BAR domain bends membranes to caveolar diameters. Quote: *"Both tagged and untagged full-length syndapin III formed tubules with an average diameter of about 80 nm."*
   - In knockout heart, only 11.7% of wild-type caveolae remain. Knockout cardiomyocytes keep about 15% of wild-type caveolae (0.29 vs ~2 per µm).
   - Caveolin-3 and cavin-1 levels at the plasma membrane are **not** reduced. Quote: *"even a combination of the two coat proteins cav3 and CAVIN-1 … is not sufficient for efficient caveolar invagination."* (PMID:29202928; MODEL_ORGANISM)
   - **Branch, a lipid-domain defect:** caveolin-3 in detergent-resistant membranes shifts to higher-density fractions. Quote: *"syndapin III plays a critical role in organizing caveolar coats and associated lipid environments."*
3. **Loss of caveolar membrane reservoir → reduced ability to buffer acute rises in membrane tension.** Quote: *"cav3-coated caveolae serve as membrane reservoirs of muscle cells and … syndapin III plays a crucial role in forming a membrane buffer reservoir."*
   - Under hypo-osmotic swelling, knockout cardiomyocytes *"showed a significantly higher vulnerability"* and ruptured, while wild-type cells flattened their caveolae. (PMID:29202928; IN_VITRO, primary mouse cells)
4. **Mechanical stress (exercise) → sarcolemmal and fibre damage → necrosis and secondary inflammation.**
   - Quote: *"H&E stainings of musculus gastrocnemius cryosections from syndapin III KO mice subjected to physical exercise showed necrotic fibers invaded by immune cells as well as inflammation secondary to degeneration."*
   - Detached nuclei were about three times more frequent, and fibre calibre varied more widely. (PMID:29202928; MODEL_ORGANISM)
   - **Inferred step:** fibre damage leads to CK leak into serum, giving the hyperCKaemia seen in patients. This is consistent with the data but not directly demonstrated in humans.
5. **Clinical manifestation:** hyperCKaemia, exercise intolerance, fatigue and myalgia, with myopathic biopsy changes (fibre-size variation, internal nuclei) and preserved strength (PMID:38637313).

**Parallel branch, with unknown causal position:** in patient P1, EM showed membranous tubules and tubular-aggregate-like stacks, plus subsarcolemmal vacuoles with membranous cytoplasmic bodies. The authors interpret the vacuoles as *altered autophagy*, but this rests only on EM morphology (no autophagy markers were measured). A plausible but undemonstrated link is excess membrane that no longer goes into caveolae (compare syndapin III's tubulating activity, PMID:29202928).

**What is absent from the mouse model.** These negatives argue that cardiac and signalling caveolinopathy features need loss of caveolin-3 protein, not just loss of caveolar invagination:
- no ERK1/2 hyperactivation;
- normal dystrophin and β-dystroglycan;
- no cardiac hypertrophy, even after training at more than 64 weeks of age.

This fits the normal cardiac findings in patients.

**Unexplained human finding (candidate `KNOWLEDGE_GAP`):** caveolin-3 immunostaining was normal in patient muscle. Caveolae were not quantified by EM in patients.

**Other PACSIN3 functions** (relevance to CMYO27 unproven):
- PACSIN3 binds TRPV4 and shifts it toward the plasma membrane (Cuajungco et al. 2006, PMID:16627472; IN_VITRO).
- PACSIN3 overexpression raises GLUT1 surface localization and glucose uptake in adipocytes (Roach & Plomann 2007, PMID:17320047; IN_VITRO).
- Review quote: *"PACSIN3 is abundant in muscle tissue and necessary for caveolar biogenesis to create membrane reservoirs, thus controlling muscle function."* (PMID:34990060)

**Suggested terms** (✔ = present in repo caches)

| Kind | Term |
|---|---|
| GO biological process | GO:0070836 *caveola assembly* ✔ (DECREASED / LOSS); GO:0097749 *membrane tubulation* ✔; GO:0001778 *plasma membrane repair* ✔; GO:0014850 *response to muscle activity* ✔ |
| GO cellular component | GO:0005901 *caveola* ✔; GO:0042383 *sarcolemma* ✔ |
| CL | CL:0008002 *skeletal muscle fiber* ✔; CL:0000746 *cardiac muscle cell* ✔ (caveolar defect present but clinically silent) |

**Suggested `biological_scale`:**
- PACSIN3 loss: MOLECULAR
- caveolar invagination failure / tension buffering: CELLULAR
- exercise-induced necrosis and inflammation: TISSUE
- hyperCKaemia: ORGANISM

**Module candidates:** consider whether a caveolinopathy or sarcolemmal-mechanoprotection module exists in `kb/modules/` (`just list-modules caveol`) before creating nodes.

**Omics, single-cell and functional screens:** none published for this disease.

## 7. Anatomical Structures Affected

- **Primary:** skeletal muscle (UBERON:0001134 *skeletal muscle tissue* ✔). No specific muscle-group predominance has been described.
- **Secondary:** clinically none. The heart has a caveolar defect in the mouse but normal structure and function, and the cardiac evaluation in patients was normal.
- **Cells:** skeletal muscle fibres.
- **Subcellular:** sarcolemma, caveolae (necks), possibly the sarcotubular/membranous system (tubular-aggregate-like stacks).
- **Lateralization:** bilateral and generalized, by inference.

## 8. Temporal Development

- **Onset:** infancy to childhood.
  - P1 had hypotonia in the first months and walked at 2 years.
  - Family 2 had normal milestones, with exercise intolerance noted in childhood.
  - Biopsies were taken at ages 5, 7 and 9.
- **Course:** apparently stable or non-progressive over short follow-up (no new features at 9.5 and 11.5 years).
  - There are no natural-history data, adult outcomes or staging.
  - Symptoms (fatigue, pain, malaise) are *variable*.

## 9. Inheritance and Population

| Item | Value |
|---|---|
| Inheritance | Autosomal recessive (HP:0000007 ✔) |
| Prevalence / incidence | Unknown. Only 3 published cases plus 1 submitted case. Use `CASES_IN_LITERATURE`. |
| Penetrance | Heterozygous carrier parents were unaffected, with normal CK in Family 1. Full penetrance in biallelic individuals cannot be assessed. |
| Consanguinity | Present in Family 2 and in the GenCC case |
| Ancestry | German (1), Turkish (2), plus an additional consanguineous family of unspecified origin |
| Sex | All 3 published cases are female. This is not interpretable given AR inheritance and n=3. |
| Founder effects, anticipation, mosaicism, carrier frequency | None reported or not available |

## 10. Diagnostics

- **Laboratory:** serum CK, raised 3–8× in published cases. CK-MB and transaminases may be secondarily raised.
- **Genetic testing:** exome sequencing found every published case. Variants were confirmed by Sanger sequencing with parental segregation. PACSIN3 is on the Genomics England congenital myopathy, fetal anomalies and DDG2P panels. Look for biallelic truncating variants.
- **Functional confirmation:** PACSIN3 immunoblot on fibroblasts (protein absent).
- **Muscle biopsy:**
  - Light microscopy: non-specific (fibre-size variation, internal nuclei, focal endomysial fibrosis).
  - Caveolin-3 immunostaining is normal and does **not** exclude the diagnosis.
  - EM may show membranous tubules or tubular-aggregate-like stacks and autophagic-appearing vacuoles.
- **EMG/NCS:** normal in both patients tested. **Muscle ultrasound:** normal. **Muscle MRI:** not reported.
- **Workup to exclude other causes:** cardiac (ECG, echocardiography) and respiratory testing; metabolic screening for fatty-acid oxidation disorders and Pompe disease; dystrophinopathy testing.
- **Differential diagnosis:**
  - **CAV3 caveolinopathies** (hyperCKaemia, LGMD-1C, rippling muscle disease). These usually show reduced caveolin-3 staining and rippling/PIRCS; CMYO27 shows neither.
  - CAVIN1 deficiency (lipodystrophy with myopathy).
  - Dystrophinopathy.
  - Pompe disease.
  - Fatty-acid oxidation and other metabolic myopathies.
  - Tubular aggregate myopathies (STIM1/ORAI1).
  - Idiopathic hyperCKaemia.
- **Screening:** no newborn or population screening exists. Cascade carrier testing is possible once familial variants are known.

## 11. Outcome / Prognosis

- No mortality has been reported. All patients were ambulant with normal strength into late childhood.
- Long-term disability, adult course and quality-of-life data are **not available**.
- Mouse data suggest a possible risk of exercise-induced muscle damage; this has not been studied in humans.
- No prognostic biomarkers are known.

## 12. Treatment

There is **no disease-specific therapy** and no clinical trials. Neither the index report nor the databases describe any treatment. Reasonable supportive approaches by analogy with mild myopathies (not evidence-based for CMYO27) are listed below. NCIT IDs are from CLAUDE.md's reference list and must be checked with `just validate-terms`.

| Approach | NCIT term ⚠ |
|---|---|
| Physical therapy, with graded rather than strenuous exercise. The mouse data suggest strenuous training could be harmful (PMID:29202928, MODEL_ORGANISM). | NCIT:C15302 Physical Therapy |
| Supportive symptom management | NCIT:C15747 Supportive Care |
| Genetic counselling | NCIT:C15240 Genetic Counseling |

No pharmacogenomic, gene, cell or RNA therapies are under study.

## 13. Prevention

- Primary prevention is not applicable.
- Genetic counselling for families: 25% recurrence risk for carrier couples; carrier testing; prenatal or preimplantation testing once familial variants are known.
- Tertiary prevention: monitor CK and symptoms. The cardiac and respiratory baseline was normal in all patients tested; whether surveillance is needed is unknown.

## 14. Other Species / Natural Disease

No naturally occurring PACSIN3 disease is recorded in animals. No OMIA search was performed. Ortholog background:
- Invertebrates have a single syndapin (Drosophila *Synd*, *C. elegans sdpn-1*).
- Vertebrates have PACSIN1–3; zebrafish has six paralogs (PMID:34990060).
- Zebrafish *pacsin3* knockdown disrupts notochord development (Edeling et al. 2009, PMID:19997509; MODEL_ORGANISM).

## 15. Model Organisms

| Model | Genotype | What it recapitulates | Limitations | Ref |
|---|---|---|---|---|
| **Syndapin III (Pacsin3) KO mouse**, *Mus musculus* | Cre/lox deletion of exons 5–6 → frameshift, *"full syndapin III loss-of-function"* | `RECAPITULATES` failed caveolar invagination with preserved caveolin-3/cavin-1. `PARTIALLY_RECAPITULATES` the myopathy: exercise-induced necrosis, inflammation, detached nuclei and widened calibre spectrum. Cardiomyocytes rupture under hypo-osmotic stress. Suggested fidelity: MODERATE. | No overt phenotype under sedentary housing. Serum CK was not reported, so the defining human biomarker is untested. Phenotype only in aged (>64 week) trained mice. | PMID:29202928 |
| Zebrafish *pacsin3* morphant | Morpholino knockdown | Notochord and body-axis defects | Not a muscle-disease model; morpholino caveats; developmental phenotype absent in humans | PMID:19997509 |
| Patient fibroblasts (P1, P2A, P2B) | Endogenous biallelic null | Absence of PACSIN3 protein | Non-muscle cells | PMID:38637313 |

No iPSC, organoid, MGI/IMPC-characterized or rescue models have been reported.

---

## Knowledge gaps (candidate `discussions`)

1. **`KNOWLEDGE_GAP` (human caveolae):** caveolar density at patient sarcolemma has not been measured by EM or freeze-fracture, so the central mechanistic step is inferred from the mouse.
2. **`HUMAN_MODEL_MISMATCH`:** knockout mice are clinically silent unless trained and serum CK was not reported in them, whereas patients have constitutive hyperCKaemia from childhood.
3. **`KNOWLEDGE_GAP` (ultrastructure):** the origin of the tubular-aggregate-like stacks and autophagic vacuoles is unknown, and they were seen in a single biopsy.
4. **`KNOWLEDGE_GAP` (natural history):** there are no adult outcome data, and it is unknown whether exercise restriction is beneficial.

## Curation notes

- PMID:38637313 has **no abstract text in its cache**: `content_type: unavailable`, and PubMed lists it as a Letter / Case Report. Every quote from it in this report comes from the publisher HTML and will **not** pass snippet validation against the current cache. Clinical claims may need a full-text-capable fetch, or must be supported by other sources.
- PMID:29202928, PMID:34990060 and PMID:36980283 are cached with full text.
- PMID:16627472, PMID:17320047 and PMID:19997509 are not cached; run `just fetch-reference` on any you use.
- PMID:36980283 (caveolae mechanotransduction review) is background only. It mentions PACSIN3 just once, in passing (*"Pacsin2 and Pacsin3 regulate caveolar density"*).
- The draft `kb/disorders/Congenital_Myopathy_27.yaml` currently contains only the name, category and MONDO term.

## Sources

- Distelmaier F et al. *Biallelic truncating variants in PACSIN3 cause childhood-onset myopathy with hyperCKaemia.* Brain 2024;147(7):e45. PMID:38637313. doi:10.1093/brain/awae099. [Full text](https://academic.oup.com/brain/article/147/7/e45/7651148?login=false)
- Seemann E et al. *Deciphering caveolar functions by syndapin III KO-mediated impairment of caveolar invagination.* eLife 2017;6:e29854. PMID:29202928. doi:10.7554/eLife.29854
- Dumont V, Lehtonen S. *PACSIN proteins in vivo: Roles in development and physiology.* Acta Physiol 2022. PMID:34990060. doi:10.1111/apha.13783
- Sotodosos-Alonso L et al. *Caveolae Mechanotransduction at the Interface between Cytoskeleton and Extracellular Matrix.* Cells 2023. PMID:36980283. doi:10.3390/cells12060942
- Cuajungco MP et al. *PACSINs bind to the TRPV4 cation channel.* J Biol Chem 2006;281:18753. PMID:16627472. [UniProt citation](https://purl.uniprot.org/citations/16627472)
- Roach W, Plomann M. *PACSIN3 overexpression increases adipocyte glucose transport through GLUT1.* BBRC 2007;355:745. PMID:17320047. [PMC1855247](https://pmc.ncbi.nlm.nih.gov/articles/PMC1855247)
- Edeling MA et al. *Structural requirements for PACSIN/Syndapin operation during zebrafish embryonic notochord development.* PLoS One 2009;4:e8150. PMID:19997509. [ZFIN record](https://zfin.org/ZDB-PUB-091215-55)
- [Genomics England PanelApp: PACSIN3, Congenital myopathy panel](https://panelapp.genomicsengland.co.uk/panels/225/gene/PACSIN3/)
- [Genomics England NHS GMS PanelApp: PACSIN3](https://nhsgms-panelapp.genomicsengland.co.uk/entities/PACSIN3)
- [GenCC submission SGC-179464.1 (LiferaOmics)](https://thegencc.org/submissions/SGC-179464.1)
- [Disease Ontology DOID:0061258](https://disease-ontology.org/term/DOID:0061258/owl)
- [OMIM *606513 PACSIN3](https://www.omim.org/entry/606513) (entry #621343 could not be fetched, HTTP 403)
- [Gene Table of Neuromuscular Disorders: PMID 38637313 entry](https://www.musclegenetable.fr/4DACTION/disease_cherche_ref/1312_38637313) (connection refused)
- [Hacettepe AVESIS record of the index paper](https://avesis.hacettepe.edu.tr/yayin/8d5cd868-149a-4bc5-9414-38d26afd7140/biallelic-truncating-variants-in-pacsin3-cause-childhood-onset-myopathy-with-hyperckaemia)
- [Wikipedia: PACSIN3](https://en.wikipedia.org/wiki/PACSIN3)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:16627472` (3 mentions) - PACSINs bind to the TRPV4 cation channel. PACSIN 3 modulates the subcellular localization of TRPV4.
  - shared terms: protein

Weighed against this report's own most characteristic terms: `pacsin3`, `normal`, `patient`, `muscle`, `exercise`, `mouse`, `disease`, `protein`, `variant`, `myopathy`, `caveolar`, `biallelic`, `syndapin`, `caveolae`, `model`, `gene`, `hyperckaemia`, `gencc`, `clinical`, `iii`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

33 of 34 terms resolved to a current term; the rest could not be looked up either way.