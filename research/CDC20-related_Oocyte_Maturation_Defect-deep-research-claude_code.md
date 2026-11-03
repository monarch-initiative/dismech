---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T15:31:29.063453'
end_time: '2026-10-15T15:35:17.120703'
duration_seconds: 228.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CDC20-related Oocyte Maturation Defect
  mondo_id: MONDO:0859521
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
  web_search_requests: 6
  num_turns: 22
  total_cost_usd: 1.9722973999999995
  session_id: 7a9a6761-7539-41ed-8e3a-bc5e15260f56
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - mcp__ols-mcp__search_all_ontologies
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 16
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 21
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CDC20-related Oocyte Maturation Defect
- **MONDO ID:** MONDO:0859521 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CDC20-related Oocyte Maturation Defect** covering all of the
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

I'm still gathering primary-literature details. Next I'm pulling the 2021 CDC20 variant paper and the mouse model data.

I've got the core literature. I'm checking a few more cached term IDs, then I'll write the report.

# CDC20-related Oocyte Maturation Defect (OOMD14 / OZEMA14): Research Report

This report rests on three primary studies: Zhao et al. 2020 (PMID:32666501), Zhao et al. 2021 (PMID:33898437) and Jin et al. 2010 (PMID:20941357). Their text was read through web fetches of the article pages. Li et al. 2007 (PMID:17325031) and Jiao et al. 2025 are known only from search-result summaries.

**Search limitations.** The PubMed and OLS tools were not permitted in this session, so the deeper PubMed sweep and the OLS term searches did not happen. Some PMC pages also returned a CAPTCHA instead of the article.

**Verify before use.** The quoted fragments below are short excerpts copied from fetched pages. Before any of them is used as a `snippet:`, run `just fetch-reference` and check it against `references_cache/`. Ontology IDs marked "(cached)" were read from this repository's `cache/*/terms.csv`. Every other CURIE is a lead to look up, not a checked binding.

---

## 1. Disease information

**Overview.** This is an autosomal recessive form of female infertility caused by biallelic loss-of-function variants in *CDC20*. *CDC20* encodes the co-activator of the anaphase-promoting complex/cyclosome (APC/C) that drives the metaphase-to-anaphase transition. Affected women are otherwise healthy. Their oocytes arrest at metaphase I (MI), fail to fertilize, or give rise to embryos that arrest early. The phenotype is only seen during IVF/ICSI.

MedGen's definition, from OMIM, in fragments: "Oocyte/zygote/embryo maturation arrest-14 (OZEMA14) is characterized by female infertility due to oocyte maturation arrest" … "fertilization failure, and/or early embryonic arrest." … "The rare fertilized embryos that are transferred to the uterus fail to establish pregnancy after transfer" ([MedGen C5830326](https://www.ncbi.nlm.nih.gov/medgen/C5830326)).

| Identifier | Value |
|---|---|
| MONDO | MONDO:0859521 (MedGen; [SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0859521/)) |
| OMIM (phenotype) | **620276**. 620103, which a search query offered, is not the right number. |
| OMIM (gene) | CDC20 *603618 |
| MedGen / GTR | C5830326 ([GTR](https://ncbi.nlm.nih.gov/gtr/conditions/C5830326)) |
| KEGG | H01897, Oocyte/zygote/embryo maturation arrest ([KEGG](https://www.genome.jp/entry/H01897)) |
| Orphanet | No disease-specific code was found. The broader Orphanet "oocyte maturation defect" concept is the likely umbrella; unverified. |
| ICD-10/11 | No specific code. Falls under female infertility: ICD-10 N97.x, ICD-11 GA31. These codes are generic and should not be mapped as exact. |

**Synonyms:** Oocyte maturation defect 14 (OOMD14); oocyte/zygote/embryo maturation arrest 14 (OZEMA14); CDC20-related female infertility. The gene's aliases are CDC20A, p55CDC and bA276H19.3. PanelApp Australia rates the gene–disease evidence for CDC20 as strong ([PanelApp AUS](https://panelapp-aus.org/panels/4455/gene/CDC20/)).

**Data provenance:** The data come from published case series of individual patients' IVF/ICSI cycle data plus functional assays. There are no registries and no EHR cohorts.

## 2. Etiology

- **Cause:** Biallelic germline *CDC20* variants, either homozygous (often from consanguineous parents) or compound heterozygous.
- **Genetic risk factors:** The causal variants are listed in §4. No susceptibility loci or modifier genes are reported.
- **Environmental risk factors:** None are reported. The phenotype is intrinsic to the oocyte.
- **Protective factors and gene–environment interactions:** None are known.
- **Dosage model:** The authors propose that "female infertility resulting from CDC20 reduction is dosage dependent" and that "mitosis is more tolerant than meiosis to CDC20 reduction" (Zhao 2020, PMID:32666501). This explains why somatic tissues are spared. Jin et al. (PMID:20941357) found the same in mice: a hypomorphic allele leaves somatic tissues healthy but makes females subfertile.

## 3. Phenotypes

All phenotypes are female-only. They are first detected in adulthood when infertility is investigated, and they are stable and lifelong. Severity varies with genotype, from complete MI arrest to fertilization failure or embryo arrest.

| Phenotype | Type | HPO suggestion | Frequency (11 published probands*) | Notes |
|---|---|---|---|---|
| Primary female infertility | Clinical sign | HP:0008222 Female infertility (cached) | 11/11 | Infertility lasting 2–11 years (Zhao 2021) |
| Oocyte maturation arrest at MI | Laboratory/IVF finding | HP:0031516 Metaphase I oocyte maturation arrest (cached) | Predominant in roughly 6/11 | Zhao 2020 family 2: all oocytes at MI. Zhao 2021 family 1: all 7 oocytes at MI |
| Mixed GV/MI arrest | IVF finding | HP:6001356 Mixed oocyte maturation arrest (cached) | Several | Zhao 2020 family 1: 10/11 oocytes at GV or MI |
| Fertilization failure | IVF finding | No cached HP term; the OMIM clinical synopsis lists "fertilization failure". Search HPO before binding. | Most probands | Seen with the hypomorphic genotypes (p.Arg322Gln compound heterozygotes) |
| Early embryonic arrest | IVF finding | HP:0020003 Embryo developmental arrest (cached) | Several | Arrest at the one-cell, three-cell and eight-cell stages |
| Failure of pregnancy after transfer | Clinical | No specific term; covered by the OMIM definition | Rare transfers all failed | |

\*Five probands from Zhao 2020, four affected women in three families from Zhao 2021 (including the affected sister in family 2), and at least one from Jiao 2025.

- **Genotype–phenotype pattern:** Homozygous missense variants that markedly lower protein levels (p.Tyr228Cys, p.Leu439Arg, p.Arg296Gln) cause MI arrest. Compound heterozygotes carrying the milder p.Arg322Gln allele often reach first polar body (PB1) extrusion and then show fertilization failure or embryonic arrest. Zhao 2020 described its family 3 as showing "a slight delay in maturation, with fertilization failure as the final phenotype."
- **Quality of life:** No disease-specific QoL data exist. The impact is that of untreatable infertility: psychological burden plus repeated costly IVF cycles.

## 4. Genetic and molecular information

- **Gene:** *CDC20*, cell division cycle 20, at 1p34.2. HGNC is believed to be hgnc:1723, but this is **not cached here, so verify it**. OMIM *603618. UniProt Q12834 (verify).
- **Inheritance:** Autosomal recessive.
- **Origin:** Germline.
- **Functional class:** Loss of function or hypomorph. Truncating variants are null. Missense variants lower protein abundance and impair cyclin B1 degradation.

### Published variants (NM_001255.3 presumed; verify the transcript)

| Variant | Protein | Type | Genotype | Source |
|---|---|---|---|---|
| c.683A>G | p.Tyr228Cys | missense | homozygous | Zhao 2020, family 1 (consanguineous) |
| c.1316T>G | p.Leu439Arg | missense | homozygous | Zhao 2020, family 2 (consanguineous) |
| c.965G>A | p.Arg322Gln | missense, **recurrent** (4 families) | compound heterozygous | Zhao 2020 families 3–5; Zhao 2021 family 2 |
| c.544C>T | p.Arg182* | nonsense | compound heterozygous with p.Arg322Gln | Zhao 2020, family 3 |
| c.813_814insAGTG | p.Gly272Serfs*24 | frameshift | compound heterozygous | Zhao 2020, family 4 |
| c.1176_1179delTCTG | p.Cys392* | frameshift | compound heterozygous | Zhao 2020, family 5 |
| c.887G>A | p.Arg296Gln | missense | homozygous (consanguineous) | Zhao 2021, family 1 |
| c.964C>T | p.Arg322* | nonsense | compound heterozygous with p.Arg322Gln | Zhao 2021, family 2 |
| c.330+1G>A | p.Glu111Ilefs*36 | canonical splice donor; minigene assay shows intron 2 retention | compound heterozygous | Zhao 2021, family 3 |
| c.1155G>C | p.Trp385Cys | missense | compound heterozygous (in trans, confirmed by TA cloning) | Zhao 2021, family 3 |
| Not retrieved | — | biallelic | — | Jiao et al. 2025, *Gynecol Endocrinol*, doi:10.1080/09513590.2025.2451672. The abstract was truncated, so the variants were not obtained. |

- **Cohort yield:** In Zhao 2020, families 3–5 came from whole-exome sequencing of 1,250 infertile women; families 1–2 were found by WES plus homozygosity mapping. Zhao 2021 screened 465 infertile women. The cohort yield is roughly 0.3–0.6%.
- **Ancestry and founder variant:** All reported families are Chinese. The recurrent c.965G>A (p.Arg322Gln) suggests a founder or recurrent allele in that population. Its gnomAD frequency was not retrieved.
- **ClinVar/ACMG:** Classifications were not retrieved. A ClinGen gene-disease validity record for CDC20–OZEMA14 was not confirmed; run `just list-gene-validity`.
- **Modifier genes, epigenetics, chromosomal abnormalities:** None reported.
- **Related genes:** Other OZEMA/OOMD genes include *TUBB8* (OOMD2, already in the KB as `TUBB8-related_Oocyte_Maturation_Defect`), *PATL2*, *TRIP13*, *WEE2* and *ZP1/2/3*. Most relevant mechanistically are **APC/C-pathway genes**: *CCNB3* defects lower CDK1 activity and APC/C-CDC20 activity, causing MI arrest ([J Ovarian Res 2023](https://Ovarianresearch.Biomedcentral.com/counter/pdf/10.1186/s13048-023-01229-8.pdf)).

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious contributors are reported. Maternal age may compound the effect, since oocyte quality declines with age, but this has not been studied for CDC20.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic *CDC20* LoF or hypomorphic variants lead to reduced functional CDC20 in the oocyte.** Demonstrated: missense variants lower protein levels in CHO cells and in patient lymphoblastoid cells; truncating variants yield truncated protein or no detectable signal; four variants lower mRNA; patient lymphoblastoid and granulosa cells show reduced *CDC20* mRNA (Zhao 2020, 2021).
   - The truncating variants also **fail to localize to kinetochores** in mouse oocytes, whereas missense proteins localize normally (demonstrated).
2. **Reduced CDC20 leads to insufficient APC/C^CDC20 E3 ubiquitin ligase activity at the end of meiosis I.** This is inferred from the gene's known function. APC/C activity itself was not measured; the proxy readout is that mutant CDC20 fails to drive endogenous cyclin B1 degradation.
3. **Insufficient APC/C^CDC20 activity leads to failed ubiquitin-mediated degradation of cyclin B1 and securin.** Cyclin B1 is shown directly; securin is inferred from mouse genetics (PMID:17325031). This keeps CDK1 (MPF) activity high and separase inhibited.
4. **Branch A, severe loss:** No anaphase I and no PB1 extrusion results in **MI oocyte maturation arrest**. Demonstrated in mouse oocytes: *Cdc20* knockdown causes MI arrest; wild-type human cRNA rescues PB1 extrusion; every patient mutant rescues significantly less.
5. **Branch B, partial loss, typically with p.Arg322Gln:** Delayed or error-prone anaphase I lets PB1 extrude. The resulting chromosome lagging, misalignment and aneuploidy lead to **fertilization failure, failed MII exit, or early embryonic arrest**. The aneuploidy link is demonstrated in hypomorphic mice (Jin 2010) and inferred in humans. One human blastocyst rescued with cRNA was euploid on screening.
6. **Zygote and cleavage stage:** CDC20 is also needed for the early embryonic mitoses. *Cdc20*-null mouse embryos arrest in metaphase at the two-cell stage with high cyclin B1 (Li 2007, PMID:17325031). Maternal CDC20 deficiency therefore plausibly contributes to the one- to eight-cell arrests seen in patients. This is inferred.
7. **Clinical outcome:** No transferable euploid embryos, which results in primary female infertility.

### Supporting detail

- **Dosage threshold:** Mitosis tolerates CDC20 reduction better than meiosis I does. This explains the absence of any somatic phenotype (Zhao 2020; Jin 2010).
- **Pathways:** Spindle assembly checkpoint → APC/C^CDC20 → separase/cohesin cleavage. In KEGG this sits in the cell cycle (hsa04110), oocyte meiosis (hsa04114) and progesterone-mediated oocyte maturation (hsa04914) maps. In Reactome it is "APC/C:Cdc20 mediated degradation of Cyclin B" (ID not checked).
- **Suggested GO terms:**
  - Cached: GO:0001556 oocyte maturation; GO:0007127 meiosis I; GO:0031145 anaphase-promoting complex-dependent catabolic process; GO:0008608 attachment of spindle microtubules to kinetochore; GO:0007094 mitotic spindle assembly checkpoint signaling.
  - Not cached, look up: "anaphase-promoting complex binding" and "ubiquitin-protein transferase activator activity" (molecular function); "homologous chromosome segregation"; "polar body extrusion after meiotic divisions"; "meiotic spindle assembly checkpoint signaling"; "positive regulation of anaphase-promoting complex-dependent catabolic process".
- **Cell types:** CL:0000023 oocyte (cached); CL:0000025 egg cell (look up); zygote and early blastomere (look up in CL). Granulosa cells (CL:0000501, cached) were used only as an mRNA readout and are not a disease site.
- **Not relevant:** Metabolic, immune and tissue-damage mechanisms play no role. No omics, single-cell or CRISPR-screen data specific to this disease exist.

## 7. Anatomical structures

- **Organ:** Ovary (UBERON:0000992, verify), specifically the oocyte within the ovarian follicle. The reproductive system is the only organ system involved.
- **Ovarian reserve:** Folliculogenesis and ovarian reserve are normal; hypomorphic mice show normal folliculogenesis.
- **Subcellular:** Kinetochore (GO:0000776), meiotic spindle, and the APC/C complex (GO:0005680, verify).
- **Lateralization:** Bilateral and systemic to the germline.

## 8. Temporal development

- **Onset:** Congenital, as a germline genotype, but clinically silent until attempts at conception in adulthood. Reported probands were 32–37 years old at presentation.
- **Course:** Stable and non-progressive. There is no remission.
- **Critical window:** The MI→MII transition, at oocyte resumption of meiosis, and the first embryonic cleavages.

## 9. Inheritance and population

- **Pattern:** Autosomal recessive; female-limited expression.
- **Males:** Male fertility in carriers or homozygotes is not reported. Hypomorphic male mice are fertile (Jin 2010).
- **Penetrance and expressivity:** Penetrance in homozygous or compound-heterozygous females appears complete in the families reported. Expressivity varies by allele combination, from MI arrest to embryo arrest. The affected sister in Zhao 2021 family 2 shared the genotype and the infertility.
- **Consanguinity:** 3 of 8 families in the two Zhao studies.
- **Epidemiology:** Ultra-rare, with about 9 families published (plus Jiao 2025). There are no prevalence or incidence data. Use `CASES_IN_LITERATURE`.
- **Population and sex:** All reported cases are Chinese. Expression is female-only.
- **Not reported:** anticipation, germline mosaicism.

## 10. Diagnostics

- **Clinical criteria:** Repeated IVF/ICSI failure with oocytes that arrest at GV/MI, that fail to fertilize despite ICSI, or that give rise to embryos which arrest early.
- **Laboratory finding:** Stereomicroscopic oocyte staging at retrieval and after 24 h in vitro culture (absence of PB1). No serum biomarker exists; hormone levels and ovarian reserve are normal.
- **Genetic testing:**
  - Whole-exome sequencing, or an oocyte/embryo-arrest gene panel (*TUBB8, PATL2, TRIP13, WEE2, CDC20, ZP1–3, PADI6, NLRP5, TLE6, BTG4*…).
  - Segregation testing in parents, or phasing (TA cloning was used when parents were unavailable).
  - RNA or minigene studies for splice variants.
  - Karyotyping and CMA are unhelpful.
- **Differential diagnosis:**
  - *TUBB8* (MI arrest with spindle defects; often dominant de novo)
  - *PATL2* (GV arrest)
  - *TRIP13* (MI arrest)
  - *WEE2* (fertilization failure)
  - *ZP* genes (empty follicle / zona-free oocytes)
  - Maternal-effect genes (*PADI6*, *NLRP5*, SCMC): embryo arrest
  - Iatrogenic causes: suboptimal trigger
- **Screening:** None at population level. Carrier testing of relatives can follow.

## 11. Outcome and prognosis

- **Survival:** Normal; there is no systemic morbidity.
- **Fertility:** No naturally conceived or IVF live births are reported in affected women. The main outcome is permanent infertility with own oocytes.
- **Prognostic factor:** Genotype. Hypomorphic p.Arg322Gln compound heterozygotes produce PB1 oocytes and are candidates for experimental rescue.

## 12. Treatment

No established therapy exists.

- **Assisted reproduction, for diagnosis only (fails therapeutically):**
  - IVF: NCIT:C16580 In Vitro Fertilization (cached)
  - ICSI: NCIT:C185482 Intracytoplasmic Sperm Injection (cached)
  - ART generally: NCIT:C93282 Assisted Reproductive Technology (cached)
- **Experimental: wild-type *CDC20* cRNA microinjection into patient PB1 oocytes** (Zhao 2020).
  - Family 3: four oocytes were injected; all four fertilized (2PN), two reached blastocyst by day 6, and the one screened was euploid with no large CNVs.
  - Family 4: three oocytes were injected; all fertilized and one reached the eight-cell stage.
  - This is in vitro proof of concept only, with no transfer or live birth. It is an mRNA-therapy approach (`therapeutic_modality: MRNA_THERAPY`). It should be recorded as experimental, with evidence_source IN_VITRO on human oocytes.
- **Practical options:** Oocyte donation is the only realistic route to pregnancy; adoption is the alternative. The NCIT term for oocyte donation was not verified.
- **Clinical trials:** None registered for CDC20.
- **Supportive care:** Genetic counseling (NCIT:C15240, cached) and psychological support.

## 13. Prevention

- No primary prevention.
- Genetic counseling for consanguineous families. Cascade testing of sisters can spare them futile IVF cycles.
- Preimplantation testing is not applicable to the affected woman herself.

## 14. Other species

- No naturally occurring animal disease is recorded; an OMIA search was not performed.
- **Orthologs:** mouse *Cdc20* (MGI:1859866, verify); yeast *CDC20* / *S. pombe slp1*. The gene and its APC/C co-activator function are highly conserved across eukaryotes.

## 15. Model organisms

| Model | Phenotype | Fidelity | Source |
|---|---|---|---|
| Mouse *Cdc20* gene-trap null | Embryos arrest in metaphase at the two-cell stage with high cyclin B1; Cdc20/securin double mutants cannot sustain the arrest | Models embryonic lethality, not the adult infertility | Li et al. 2007, *Mol Cell Biol*, PMID:17325031 |
| Mouse *Cdc20* hypomorph (low expression) | Healthy mice, normal folliculogenesis and fertilization; females have few or no offspring; embryos are aneuploid, mainly from lagging and misaligned chromosomes at oocyte MI; "physiologically effective threshold level of Cdc20 is high for female meiosis I" | **Partial recapitulation**, close to the human hypomorphic phenotype (fertilization and embryo arrest). Does not reproduce complete MI arrest. | Jin et al. 2010, *PLoS Genet*, PMID:20941357 ([PMC2947999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2947999)) |
| Mouse oocyte *Cdc20* knockdown (morpholino/siRNA) plus human cRNA rescue | MI arrest; wild-type rescues PB1 extrusion; patient variants rescue poorly | Ex vivo functional assay used to classify variants | Zhao 2020; Zhao 2021 |
| CHO cell overexpression | Protein and mRNA levels; cyclin B1 degradation | In vitro | Zhao 2020; 2021 |

**Divergences to record:** mouse versus human meiosis timing, a species mismatch. The knockdown model is a proxy for germline loss, a boundary omission (no maternal-effect embryonic stage).

---

## Key references

1. Zhao L, Xue S, Yao Z, et al. Biallelic mutations in CDC20 cause female infertility characterized by abnormalities in oocyte maturation and early embryonic development. *Protein Cell* 2020;11(12):921–927. **PMID:32666501**; doi:10.1007/s13238-020-00756-0. [PMC7719138](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7719138/). Human clinical, in vitro and mouse-oocyte data.
2. Zhao L, Guan Y, Meng Q, et al. Identification of novel mutations in CDC20: expanding the mutational spectrum for female infertility. *Front Cell Dev Biol* 2021;9:647130. **PMID:33898437**; doi:10.3389/fcell.2021.647130. [Frontiers](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.647130/full)
3. Jin F, Hamada M, Malureanu L, et al. Cdc20 is critical for meiosis I and fertility of female mice. *PLoS Genet* 2010;6(9):e1001147. **PMID:20941357**. Model organism.
4. Li M, York JP, Zhang P. Loss of Cdc20 causes a securin-dependent metaphase arrest in two-cell mouse embryos. *Mol Cell Biol* 2007. **PMID:17325031**. Model organism; the title is recalled from memory, so take it from the cache file.
5. Jiao G, Xing J, Du Z, Bao H, Liu X. Biallelic mutations in CDC20 cause female infertility due to oocyte maturation abnormality. *Gynecol Endocrinol* 2025. doi:10.1080/09513590.2025.2451672. PMID and variants not retrieved; [record](https://library.kab.ac.ug/Record/doaj-art-0202a1d13e7b4bbaa1b5ff7897f50687).
6. Malureanu L, et al. *J Cell Biol* 2010, PMID:20956380. Hypomorphic Cdc20 in somatic cells.
7. CCNB3 and OMA (APC/C-CDC20 pathway context), *J Ovarian Res* 2023, doi:10.1186/s13048-023-01229-8.

## Gaps to close before curation

- Get the PMID and variants for Jiao 2025.
- Check ClinVar and gnomAD for the variants.
- Check for a ClinGen validity record.
- Find an HPO term for "fertilization failure".
- Confirm hgnc:1723 and the UBERON, GO and CL IDs not in the local cache.
- Run an OMIA check.

Sources:
- [MedGen C5830326](https://www.ncbi.nlm.nih.gov/medgen/C5830326)
- [GTR C5830326](https://ncbi.nlm.nih.gov/gtr/conditions/C5830326)
- [KEGG H01897](https://www.genome.jp/entry/H01897)
- [MalaCards OZEMA14](https://www.malacards.org/card/oocyte_zygote_embryo_maturation_arrest_14)
- [PanelApp Australia CDC20](https://panelapp-aus.org/panels/4455/gene/CDC20/)
- [SAIL MONDO:0859521](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0859521/)
- [Zhao 2020, PMC7719138](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7719138/)
- [Zhao 2020, Oxford Academic](https://academic.oup.com/proteincell/article/11/12/921/6746813)
- [Zhao 2021, Frontiers](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.647130/full)
- [Zhao 2021, PMC8063106](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8063106/)
- [Jin 2010, PMC2947999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2947999)
- [JCB commentary "A little Cdc20 goes a long way"](https://rupress.org/jcb/article-split/191/2/227/36134/A-little-Cdc20-goes-a-long-way)
- [UniProt citation 17325031](https://purl.uniprot.org/citations/17325031)
- [Jiao 2025 record](https://library.kab.ac.ug/Record/doaj-art-0202a1d13e7b4bbaa1b5ff7897f50687)
- [CCNB3 OMA 2023](https://Ovarianresearch.Biomedcentral.com/counter/pdf/10.1186/s13048-023-01229-8.pdf)
- [Fudan reproductive genetics lab](https://reprod-genet.fudan.edu.cn/laben/ba/31/c22985a244273/page.htm)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0000776` (1 mention) - the report calls it "Subcellular:** Kinetochore"; GO calls it **kinetochore**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

20 of 21 terms resolved to a current term; the rest could not be looked up either way.