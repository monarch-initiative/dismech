---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-26T19:30:41.601893'
end_time: '2026-11-26T19:35:36.173940'
duration_seconds: 294.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Syphilis
  mondo_id: MONDO:0005714
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: MTCT of syphilis; mother-to-child transmission of syphilis
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 19
  num_turns: 25
  total_cost_usd: 1.7014974999999999
  session_id: 2a4933da-7e52-4103-80d8-8cd7c2abd7ca
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 23
  retrieval_calls: 20
  assistant_text_blocks: 4
citation_count: 33
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 19
  on_topic: 15
  validator_version: 0.8.0
term_validation:
  total_terms: 50
  verified: 10
  not_found: 0
  obsolete: 0
  unverifiable: 40
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  unresolvable_prefixes:
  - ORPHA
  service_unreachable: 39
  obsolescence_unchecked: 3
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Syphilis
- **MONDO ID:** MONDO:0005714 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** MTCT of syphilis; mother-to-child transmission of syphilis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Syphilis** covering all of the
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

Still gathering sources: surveillance and treatment data are in hand, and I'm now looking up pathogenesis, clinical features, risk factors, and identifiers.

Understood — I'll continue gathering sources and then write the report.

I have strong coverage. Let me gather a few final pieces on identifiers, placental pathology, and immunology before writing.

I have enough to write a well-sourced report. Writing it now.

---

# Comprehensive Research Report: Congenital Syphilis (MONDO:0005714)

**Interpretation note:** This report covers **congenital syphilis** — infection of the fetus/neonate by the spirochete bacterium *Treponema pallidum* subspecies *pallidum*, transmitted vertically (mother-to-child) during pregnancy. Because this is an **infectious disease**, there is **no human causal gene**; the "causal gene(s): not recorded" field in the template is correct and expected. The causative agent is the organism *T. pallidum* subsp. *pallidum* (NCBI Taxonomy; genome characterized in [Fraser et al., *Science* 1998, PMID 9665876](https://pubmed.ncbi.nlm.nih.gov/9665876/)). Where the template asks for human genetic content (causal variants, inheritance, karyotyping, pharmacogenomics of the host, etc.), I mark it **Not applicable** and instead address the pathogen's genetics where relevant. Any genes named below (e.g., *tp0751*/pallilysin, *tprK*) are **bacterial virulence genes**, not host disease genes.

---

## 1. Disease Information

**Overview.** Congenital syphilis (CS) is a multisystem infectious disease of the fetus and newborn resulting from transplacental (and occasionally perinatal contact) transmission of *Treponema pallidum* subsp. *pallidum* from an infected pregnant person. Outcomes span a wide spectrum: spontaneous abortion, stillbirth, hydrops fetalis, prematurity/low birth weight, symptomatic neonatal disease, or an asymptomatic infected infant. A 2023 illustrative review notes that affected newborns show "low birth weight, rash, hepatosplenomegaly, osteolytic bone lesions, pseudoparalysis, central nervous system infection, and long-term disabilities" ([Congenital Syphilis—An Illustrative Review, *Children* 2023, PMID 37628309](https://pubmed.ncbi.nlm.nih.gov/37628309/)). More than half of infected infants are asymptomatic at birth ([UW National STD Curriculum](https://www.std.uw.edu/congenital-syphilis)).

**Key identifiers** (verified against the NIH GARD record and source ontologies):
- **MONDO:** MONDO:0005714 ([NIH GARD](https://rarediseases.info.nih.gov/assets/singles/22036.json))
- **ICD-10:** A50 (parent), with A50.0 early symptomatic, A50.1 early latent, A50.3 late ocular, A50.4 juvenile neurosyphilis, A50.5 other late symptomatic, A50.6 late latent, A50.7 late unspecified, A50.9 unspecified ([gesund.bund.de ICD A50](https://gesund.bund.de/en/icd-code-suche/a50))
- **ICD-9:** 090 / 090.9
- **MeSH:** D013590 ("Syphilis, Congenital") ([NLM MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D013590))
- **Orphanet:** ORPHA:499009 ([GARD](https://rarediseases.info.nih.gov/assets/singles/22036.json)) (a second Orphanet code, 232035, appears in one cross-reference but I could not independently verify it)
- **Disease Ontology:** DOID:9856 ([MGI/DO](https://www.informatics.jax.org/disease/DOID:9856))
- **MedGen:** 52622; **GARD:** 22036
- **OMIM:** Not applicable (infectious, non-Mendelian disease)

**Synonyms / alternative names:** mother-to-child transmission (MTCT) of syphilis; vertical transmission of syphilis; prenatal/intrauterine syphilis; *syphilis congenita*; "lues congenita"; early congenital syphilis (<2 years) and late congenital syphilis (≥2 years) are the two major clinical subdivisions.

**Information source type:** Content here is derived predominantly from **aggregated disease-level resources** (CDC/WHO surveillance, clinical guidelines, review articles, pathology case series) rather than individual EHR data.

---

## 2. Etiology

**Primary cause (infectious).** The disease is caused by the bacterium *Treponema pallidum* subsp. *pallidum*, a motile, spiral spirochete that cannot be cultured conventionally and has a reduced ~1.14-Mb genome with 1,041 predicted ORFs and few biosynthetic pathways (an obligate host-dependent pathogen) ([Fraser et al. 1998, PMID 9665876](https://pubmed.ncbi.nlm.nih.gov/9665876/)). Transmission to the fetus is almost always **transplacental/hematogenous**; direct contact with an infectious genital lesion during delivery is a minor additional route. CHEBI/ontology note: the bacterium itself is the etiologic agent (NCBI Taxonomy *Treponema pallidum*).

**Risk factors (for a pregnant person's infant developing CS):**
- **Maternal disease stage/recency:** Risk of fetal infection is **50–70% in early (primary/secondary) maternal syphilis**, falling to ~**15%** when maternal infection was acquired >1 year before pregnancy ([review via PMC9045944](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045944)).
- **Maternal nontreponemal titer:** Each twofold rise in maternal RPR titer increased transmission risk ([Suzhou, China 2011–2014, PMC6421965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6421965/)).
- **Late, scant, or absent prenatal care; late maternal diagnosis** (diagnosis after 36 weeks) ([Suzhou MMWR, PMC6421965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6421965/); [Chicago study, PMID 35493123](https://pubmed.ncbi.nlm.nih.gov/35493123/)).
- **Substance use and psychiatric illness:** In a Chicago hospital cohort, psychiatric illness and noninjection substance use each conferred **>5-fold increased odds** of an infant with CS, and cases "initiated treatment nearly 3 months later in pregnancy" ([PMID 35493123](https://pubmed.ncbi.nlm.nih.gov/35493123/)); drug use in pregnancy was associated with 3.32-fold risk of no prenatal care ([PMC6421965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6421965/)).
- **Inadequate/untimely maternal treatment:** In CDC's 2022 analysis, timely testing and adequate treatment gaps accounted for the large majority of CS cases ([Vital Signs MMWR 2023, PMC10684351](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10684351/)).
- **Missed by behavioral screening:** "nearly half of patients did not report any risk factors," so behavior-based screening misses many infections ([review PMC9045944](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045944)).

Genetic host risk factors: **Not applicable.**

**Protective factors.** The dominant protective factor is **timely maternal penicillin treatment**, which reduces CS by ~**97%**, stillbirth by ~**82%**, and neonatal mortality by ~**80%** ([review PMC9045944](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045944)). Early antenatal screening and treatment before ~20–28 weeks' gestation are key. Genetic protective factors: **Not applicable.**

**Gene–environment interactions:** Not applicable in the host-genetic sense. The relevant analog is **host immune status × pathogen burden/stage** (e.g., HIV co-infection alters placental inflammation — see §6/§7).

---

## 3. Phenotypes

CS phenotypes divide into **early** (onset <2 years, usually first weeks–months) and **late** (≥2 years, often childhood/adolescence) manifestations. More than 50% of infected neonates are asymptomatic at birth ([UW NSTDC](https://www.std.uw.edu/congenital-syphilis)).

**Early congenital syphilis (laboratory abnormalities, clinical signs, physical manifestations):**

| Phenotype | Type | Frequency / notes | Suggested HPO |
|---|---|---|---|
| Hepatosplenomegaly | Clinical sign | Very common; 70% in one bullous-CS subgroup | HP:0001433 (hepatosplenomegaly), HP:0001744 (splenomegaly), HP:0002240 (hepatomegaly) |
| Skin rash (maculopapular, desquamating; palms/soles), incl. pemphigus syphiliticus (bullous) | Physical manifestation | ~60–70% of symptomatic infants ([UW](https://www.std.uw.edu/congenital-syphilis)) | HP:0000988 (abnormality of the skin), HP:0008066 (abnormal blistering of the skin) |
| Rhinitis / "snuffles" (persistent purulent nasal discharge, highly infectious) | Clinical sign | Common; frequency not quantified | HP:0000421 (epistaxis-adjacent nasal), HP:0025267 (snoring/nasal) — best represented as rhinitis |
| Osteochondritis / periostitis of long bones; pseudoparalysis of Parrot | Physical/radiologic | Radiologic bone changes in >95% in a 202-infant series ([PMID 4081939](https://pubmed.ncbi.nlm.nih.gov/4081939/)) | HP:0002658 (periostitis — abnormality of the metaphysis/long bones), HP:0003330 (abnormal bone ossification) |
| Jaundice / hepatitis | Laboratory/clinical | Common | HP:0000952 (jaundice), HP:0001410 (hepatic failure/dysfunction) |
| Anemia, thrombocytopenia, leukopenia/leukocytosis | Laboratory abnormality | Common | HP:0001903 (anemia), HP:0001873 (thrombocytopenia) |
| Low birth weight / prematurity | Physical | Common | HP:0001518 (small for gestational age), HP:0001622 (premature birth) |
| Generalized lymphadenopathy | Clinical sign | Common | HP:0002716 (lymphadenopathy) |
| Hydrops fetalis (severe) | Physical | Severe, "very poor prognosis" ([Front Pediatr 2023](https://frontiersin.org/journals/pediatrics/articles/10.3389/fped.2023.1215387/pdf)) | HP:0001789 (hydrops fetalis) |
| Neurosyphilis / CNS infection (abnormal CSF) | Lab/clinical | Variable; often asymptomatic CSF abnormalities | HP:0002383 (encephalitis), HP:0100785 (meningitis-adjacent) |

**Late congenital syphilis stigmata** (if untreated; typically irreversible):
- **Hutchinson's triad** — notched (peg-shaped) Hutchinson incisors, interstitial keratitis, and eighth-nerve (sensorineural) deafness ([Hutchinson's triad](https://en.wikipedia.org/wiki/Hutchinson%27s_triad)). Interstitial keratitis is bilateral in ~80% and typically presents age 5–20 y; eighth-nerve deafness often begins high-frequency at ~8–10 y.
- **Saddle nose** (nasal septum destruction), **saber shins** (anterior tibial bowing), **frontal bossing**, **Clutton's joints** (symmetric knee effusions), **Higoumenakis sign** (clavicular thickening), **mulberry molars**, rhagades (perioral scarring), optic atrophy, intellectual disability/seizures ([PMC2819963 table](https://pmc.ncbi.nlm.nih.gov/articles/PMC2819963/table/t2-pch05463)).
  - Suggested HPO: HP:0000678 (abnormal dental enamel/teeth), HP:0000486-adjacent (keratitis → HP:0000491), HP:0000407 (sensorineural hearing impairment), HP:0005105 (abnormal nasal morphology / saddle nose), HP:0002979 (bowing of the long bones / saber shin).

**Quality-of-life impact:** Late stigmata (deafness, blindness from keratitis, facial/skeletal deformity, neurodevelopmental impairment) produce lifelong disability affecting communication, education, and daily functioning. Disease-specific validated QoL instruments for CS are **not available** in the retrieved literature; impact is described qualitatively in reviews ([PMID 37628309](https://pubmed.ncbi.nlm.nih.gov/37628309/)).

---

## 4. Genetic / Molecular Information

**Host genetics:** **Not applicable** — no causal genes, pathogenic variants, modifier genes, host epigenetics, chromosomal abnormalities, allele frequencies, or inheritance. CS is an acquired infection, not a heritable disorder.

**Pathogen genetics (the relevant molecular content):**
- *T. pallidum* subsp. *pallidum* has a compact ~1,138,006-bp circular genome, 1,041 predicted ORFs, limited catabolic/biosynthetic capability, and a **family of 12 candidate membrane (Tpr) proteins proposed as virulence factors** ([Fraser et al. 1998, PMID 9665876](https://pubmed.ncbi.nlm.nih.gov/9665876/)).
- **Virulence/dissemination genes:** *tp0751* encodes **pallilysin**, a zinc-dependent metalloprotease and laminin/fibrinogen-degrading adhesin that binds the endothelial 67-kDa laminin receptor (LamR) and is implicated in vascular dissemination and (as a placental adhesin candidate, Tp0954) transplacental crossing ([mSphere 2020, PMC7113585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7113585/)).
- **Antigenic variation:** *tprK* (Tp0897) undergoes nonreciprocal gene conversion across seven variable regions (V1–V7) from silent donor cassettes, driving immune evasion and persistence ([Biological basis for syphilis, *Clin Microbiol Rev* 2006, PMID 16418521](https://pubmed.ncbi.nlm.nih.gov/16418521/)).

---

## 5. Environmental Information

- **Environmental factors:** No toxins/radiation/pollution etiology. The operative "environment" is the **in-utero / maternal-infection environment** and **access-to-care environment** (prenatal care availability, screening programs).
- **Lifestyle factors (maternal):** Substance use (noninjection and injection drug use), limited prenatal engagement, and untreated maternal sexually transmitted infection are the dominant modifiable factors ([PMID 35493123](https://pubmed.ncbi.nlm.nih.gov/35493123/); [PMC6421965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6421965/)).
- **Infectious agent:** *Treponema pallidum* subsp. *pallidum* (NCBI Taxonomy; spirochete). HIV co-infection is a frequent and clinically important comorbidity that modifies placental histopathology (fewer inflammatory lesions, complicating diagnosis) ([2023 placental review, informahealthcare](https://informahealthcare.com/doi/abs/10.1080/15513815.2023.2253309)).

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating infection → clinical manifestation)

1. **Maternal infection** with *T. pallidum* establishes spirochetemia → spirochetes circulate in maternal blood, **leading to** access to the uteroplacental interface (most efficient during early/high-burden maternal disease). *(demonstrated — correlates with maternal stage and titer; [PMC9045944](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045944))*
2. Spirochetes **adhere to and degrade the placental/vascular basement membrane** — pallilysin (Tp0751) binds laminin and the endothelial 67-kDa laminin receptor and proteolyzes laminin/fibrinogen, **resulting in** endothelial attachment and intravasation/extravasation across vascular barriers ([mSphere 2020, PMC7113585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7113585/)). *(mechanistically demonstrated in vitro and in rabbit dissemination models; its exact role at the human placenta is inferred)*
3. **Transplacental transmission** delivers organisms into the fetal circulation → **leads to** hematogenous fetal dissemination to liver, bone, skin, mucosa, CNS, and other organs ([pathogenesis of maternal-fetal syphilis, PMID 11438902](https://pubmed.ncbi.nlm.nih.gov/11438902/)).
4. Organisms **colonize the placenta and umbilical cord**, **causing** chronic villitis, acute chorioamnionitis, villous immaturity (placenta) and **necrotizing funisitis** with perivascular spirochete invasion of the umbilical arteries (cord) ([215-placenta review](https://informahealthcare.com/doi/abs/10.1080/15513815.2023.2253309); [umbilical cord study, PMID 7628852](https://pubmed.ncbi.nlm.nih.gov/7628852/)). *(demonstrated: spirochetes found in 89% of cords)*
5. Fetal **endarteritis and perivascular inflammatory infiltrate** (plasma cells, lymphocytes) → **results in** tissue ischemia, fibrosis, and organ injury (the histologic hallmark of treponemal disease across tissues) ([PMID 11438902](https://pubmed.ncbi.nlm.nih.gov/11438902/)).
6. **Immune evasion sustains chronic infection** — the organism's sparse outer-membrane protein content renders it "virtually invisible to the immune system," and TprK antigenic variation selects new variants under immune pressure, **leading to** persistence and ongoing multi-organ seeding rather than clearance ([PMID 16418521](https://pubmed.ncbi.nlm.nih.gov/16418521/)).
7. **Branch points by severity/timing:** heavy early-pregnancy infection → fetal loss/stillbirth or **hydrops fetalis** (severe, poor prognosis); moderate infection → symptomatic early CS (hepatosplenomegaly, rash, osteochondritis); low burden/late maternal infection → asymptomatic infected neonate who, if untreated, develops **late stigmata** (Hutchinson triad, saber shins) over years ([UW](https://www.std.uw.edu/congenital-syphilis); [Front Pediatr 2023](https://frontiersin.org/journals/pediatrics/articles/10.3389/fped.2023.1215387/pdf)).

### Checklist coverage
- **Molecular pathways / protein dysfunction:** Pallilysin (Tp0751) metalloprotease activity degrades extracellular matrix laminin and fibrinogen; LamR receptor engagement mediates endothelial adhesion ([PMC7113585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7113585/)).
- **Immune involvement:** Obligate chronic inflammation with plasma-cell–rich perivascular infiltrates and endarteritis; immune evasion via outer-membrane protein paucity and TprK variation ([PMID 16418521](https://pubmed.ncbi.nlm.nih.gov/16418521/)). HIV co-infection dampens placental inflammatory lesions ([2023 placental review](https://informahealthcare.com/doi/abs/10.1080/15513815.2023.2253309)).
- **Tissue damage mechanisms:** Obliterative endarteritis → ischemia and fibrosis; necrotizing funisitis; osteochondritis/periostitis from spirochete-driven inflammation at the metaphyseal–epiphyseal junction.
- **Metabolic/biochemical/epigenetic/omics/single-cell/spatial/CRISPR data:** **Largely not available / not applicable** for human CS; detailed host multi-omics or functional-genomic screens for CS were not retrieved.

**Suggested GO terms:** GO:0006952 (defense response), GO:0044409 (entry into host), GO:0052126 (movement in host environment), GO:0098542 (defense response to other organism). **Suggested CL terms:** CL:0000786 (plasma cell), CL:0000084 (T cell), CL:0000115 (endothelial cell), CL:0000235 (macrophage).

---

## 7. Anatomical Structures Affected

- **Primary organs/tissues:** **placenta** (UBERON:0001987) and **umbilical cord** (UBERON:0002331) — chronic villitis, chorioamnionitis, villous immaturity, necrotizing funisitis ([215-placenta review](https://informahealthcare.com/doi/abs/10.1080/15513815.2023.2253309); [PMID 7628852](https://pubmed.ncbi.nlm.nih.gov/7628852/)); **liver** (UBERON:0002107, hepatitis/hepatomegaly); **bone** (UBERON:0002481; long-bone metaphyses, osteochondritis/periostitis); **skin** (UBERON:0002097, rash); **nasal mucosa** (UBERON:0001707, snuffles).
- **Secondary / systemic involvement:** central nervous system (UBERON:0001017; neurosyphilis, meningitis), eye (UBERON:0000970; interstitial keratitis — cornea UBERON:0000964), inner ear/eighth nerve (UBERON:0001846 vestibulocochlear nerve; sensorineural deafness), teeth (UBERON:0001091), hematopoietic/spleen (UBERON:0002106), lymph nodes.
- **Body systems:** hepatobiliary, musculoskeletal, integumentary, nervous, hematologic, ophthalmic, auditory, and the reticuloendothelial system.
- **Tissue/cell level:** vascular **endothelial cells** (CL:0000115; pallilysin/LamR target), **plasma cells** and lymphocytes (perivascular infiltrate), chondrocytes/osteoblasts at growth plates.
- **Subcellular:** the spirochete is **extracellular/perivascular**; no defined host organelle target. GO cellular component of relevance: GO:0005576 (extracellular region), GO:0005604 (basement membrane).
- **Lateralization:** systemic/bilateral; interstitial keratitis typically **bilateral (~80%)**; bone lesions often symmetric.

---

## 8. Temporal Development

- **Onset:** **Congenital** (infection in utero). Clinical onset: **early CS** manifests from birth to <2 years (often first 3 months, frequently first weeks); **late CS** emerges ≥2 years, with stigmata appearing through childhood/adolescence ([UW](https://www.std.uw.edu/congenital-syphilis)).
- **Onset pattern:** May be apparent at birth (acute, even fulminant/hydrops) or **insidious/latent** in the >50% asymptomatic at birth.
- **Stages/course:** fetal (loss/stillbirth/hydrops) → early CS → latency → late CS. Untreated, the disease is **chronic and progressive** toward irreversible stigmata; treated early, it is largely **curable** with prevention of late sequelae.
- **Critical window for intervention:** Maternal detection and penicillin treatment **before ~20–28 weeks' gestation** prevents most fetal damage; treatment at any point in pregnancy reduces risk substantially ([review PMC9045944](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045944)).

---

## 9. Inheritance and Population

- **Inheritance / penetrance / consanguinity / carrier frequency:** **Not applicable** (acquired infection, not heritable).
- **Epidemiology:**
  - **Global (WHO, 2022):** ~**700,000 estimated CS cases**, case rate **523 per 100,000 live births**; ~**390,000 adverse birth outcomes** from maternal syphilis (≈150,000 early fetal deaths/stillbirths; 70,000 neonatal deaths; 55,000 preterm/low-birth-weight; 115,000 infants with clinical CS) ([WHO STI strategic information](https://www.who.int/teams/global-hiv-hepatitis-and-stis-programmes/stis/strategic-information)). Untreated maternal syphilis yields adverse outcomes in **50–80%** of cases ([WHO syphilis fact sheet](https://www.who.int/en/news-room/fact-sheets/detail/syphilis)).
  - **United States (CDC, 2023):** **3,882 CS cases**, national rate **105.8 per 100,000 live births** (+3.0% vs 2022), including **279 CS stillbirths and infant deaths** — the most cases since 1992 ([CDC STI Surveillance 2023](https://www.cdc.gov/sti/php/from-the-director/announcing-sti-surveillance-2023.html)). This is a **>10-fold rise over a decade** (334 cases in 2012 → 3,761 in 2022) ([Vital Signs MMWR, PMC10684351](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10684351/)). 2024 provisional data show a 12th consecutive annual increase (~4,000 cases) ([CDC 2024 provisional](https://cdc.gov/sti-statistics/annual/)).
  - **Transmission from untreated maternal syphilis (meta-analysis):** 21% excess fetal loss/stillbirth, 9.3% excess neonatal death, 5.8% excess prematurity/LBW; **15% of infants had clinical CS** ([Gomez et al., *Bull WHO* 2013, DOI 10.2471/BLT.12.107623](https://scielosp.org/pdf/bwho/2013.v91n3/217-226/en)).
- **Geographic distribution:** Highest burden in low- and middle-income regions (WHO African and other regions) and, within the US, concentrated where prenatal screening/treatment access is limited.
- **Sex ratio:** Approximately equal (no strong sex predilection reported).
- **Age distribution:** By definition congenital/pediatric; late stigmata manifest through adolescence.

---

## 10. Diagnostics

**The diagnostic challenge:** maternal IgG crosses the placenta, so an infant's nontreponemal reactivity may reflect passive transfer; interpretation relies on **comparing infant and maternal titers using the same test/lab** ([CDC congenital syphilis guidelines](https://www.cdc.gov/std/treatment-guidelines/congenital-syphilis.htm)).

- **Maternal serology** drives suspicion; all infants of reactive mothers get a **quantitative nontreponemal test (RPR or VDRL) on infant serum** (not cord blood, which can be contaminated). An **infant titer ≥4× (two dilutions higher) than maternal** (e.g., maternal 1:8, infant ≥1:32) indicates confirmed/highly probable CS ([CDC](https://www.cdc.gov/std/treatment-guidelines/congenital-syphilis.htm); [Merck Manual](https://www.merckmanuals.com/professional/pediatrics/infections-in-neonates/congenital-syphilis)).
- **Direct detection:** darkfield microscopy, direct fluorescent antibody, PCR, or special/silver stains of lesions, body fluids, placenta, or umbilical cord confirm the diagnosis ([CDC](https://www.cdc.gov/std/treatment-guidelines/congenital-syphilis.htm)). Placental **immunohistochemistry** (sensitivity ~74%) outperforms qPCR (~26%) when serology is negative ([2023 placental review](https://informahealthcare.com/doi/abs/10.1080/15513815.2023.2253309)).
- **CSF evaluation (VDRL, cell count, protein):** reactive CSF-VDRL, or (nontraumatic tap) CSF WBC >15 cells/mm³ or protein >120 mg/dL in the first 30 days, support neurosyphilis ([state CDC-derived guidance](https://in.gov/health/files/Congenital-Syphilis-Case-Definition.pdf)).
- **Adjunct tests:** CBC with platelets, LFTs, long-bone radiographs (metaphyseal lucencies, periostitis), ophthalmologic and auditory evaluation, neuroimaging as indicated.
- **Diagnostic/surveillance criteria:** CDC/CSTE surveillance case definition (confirmed vs probable) and the 2021 CDC STI Treatment Guidelines diagnostic framework ([Workowski et al., *MMWR Recomm Rep* 2021, PMC8344968](https://pmc.ncbi.nlm.nih.gov/articles/PMC8344968)).
- **Genetic/omics/liquid-biopsy host testing:** **Not applicable.**
- **Screening:** universal antenatal syphilis screening (at first prenatal visit; many jurisdictions repeat at ~28 weeks and at delivery in high-prevalence areas); rapid dual HIV/syphilis point-of-care tests improve coverage ([Cuba case study, PMC5486952](https://pmc.ncbi.nlm.nih.gov/articles/PMC5486952)). Differential diagnosis: other congenital (TORCH) infections — toxoplasmosis, rubella, CMV, herpes, parvovirus B19, Zika — plus neonatal sepsis, hemolytic disease, and non-accidental injury (for pseudoparalysis/bone changes).

**Suggested LOINC/ontology anchors:** RPR (LOINC 20507-0-class), VDRL CSF (LOINC 5292-8-class). SNOMED CT: congenital syphilis (disorder).

---

## 11. Outcome / Prognosis

- **Mortality:** Globally, maternal syphilis caused ~150,000 stillbirths/early fetal deaths and ~70,000 neonatal deaths in 2022 ([WHO](https://www.who.int/teams/global-hiv-hepatitis-and-stis-programmes/stis/strategic-information)). US 2023: 279 CS stillbirths/infant deaths ([CDC 2023](https://www.cdc.gov/sti/php/from-the-director/announcing-sti-surveillance-2023.html)). **Hydrops fetalis** carries a very poor prognosis ([Front Pediatr 2023](https://frontiersin.org/journals/pediatrics/articles/10.3389/fped.2023.1215387/pdf)).
- **With treatment:** Early penicillin treatment of the infant is curative for active infection and prevents progression to late stigmata; prognosis is excellent when treatment is timely.
- **Morbidity/disability (untreated or late-treated):** irreversible sensorineural deafness, corneal scarring/visual loss (interstitial keratitis), dental/facial/skeletal deformity, neurodevelopmental impairment, seizures — producing lifelong disability ([PMC2819963](https://pmc.ncbi.nlm.nih.gov/articles/PMC2819963/table/t2-pch05463)).
- **Complications:** CNS neurosyphilis, hepatic dysfunction, hematologic cytopenias, nephrotic syndrome, pneumonia alba (severe pulmonary involvement).
- **Prognostic factors:** maternal stage/titer, timing of maternal treatment, presence of hydrops, CNS involvement, and birth weight/prematurity. Validated prognostic biomarker panels specific to CS: **not available**.

---

## 12. Treatment

**First-line (definitive):** **Penicillin G** — the only recommended agent; no proven alternative for the infant, so penicillin-allergic infants are desensitized ([CDC congenital syphilis](https://www.cdc.gov/std/treatment-guidelines/congenital-syphilis.htm); [Workowski 2021, PMC8344968](https://pmc.ncbi.nlm.nih.gov/articles/PMC8344968)). Suggested NCIT: Penicillin G (NCIT C61656-class), Benzathine Penicillin G.

Neonatal regimens (CDC 2021 STI Treatment Guidelines):
- **Confirmed or highly probable CS:** **aqueous crystalline penicillin G 50,000 units/kg IV per dose** — every 12 h for the first 7 days of life, then every 8 h, totaling **100,000–150,000 units/kg/day for 10 days**; or **procaine penicillin G 50,000 units/kg IM once daily × 10 days** ([CDC](https://www.cdc.gov/std/treatment-guidelines/congenital-syphilis.htm)).
- **Possible CS:** same 10-day penicillin course; a single IM benzathine penicillin G 50,000 units/kg dose is an option only when full evaluation is normal and follow-up is assured.
- **Less likely / CS unlikely:** single **benzathine penicillin G 50,000 units/kg IM**.
- **Infants/children >1 month:** aqueous penicillin G 50,000 units/kg IV every 4–6 h (**200,000–300,000 units/kg/day**) × 10 days.

**Maternal treatment (prevents CS):** stage-appropriate benzathine penicillin G during pregnancy; reduces CS by ~97% ([review PMC9045944](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045944)). The Jarisch-Herxheimer reaction may occur after treatment.

**Supportive care:** management of hydrops, cytopenias, hepatic dysfunction; audiologic and ophthalmologic follow-up; developmental services for established late sequelae.

**Advanced therapeutics (gene/cell/RNA/immuno/targeted therapy), pharmacogenomics, surgery, experimental trials:** **Not applicable / not indicated** — this is a penicillin-curable bacterial infection; no gene or cell therapies apply.

**Treatment strategy / algorithm:** The CDC 2021 four-scenario algorithm (confirmed/highly probable, possible, less likely, unlikely) stratifies infant evaluation and treatment based on maternal treatment adequacy and infant exam/titers ([CDC](https://www.cdc.gov/std/treatment-guidelines/congenital-syphilis.htm)). Note the CDC guideline carries an erratum — verify dosing against the current official document.

---

## 13. Prevention

- **Primary prevention:** prevent/treat maternal syphilis before or early in pregnancy; universal antenatal screening; partner treatment; sexual-health education. Timely maternal penicillin reduces CS ~97% ([PMC9045944](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045944)).
- **Secondary prevention (screening/early detection):** routine antenatal serologic screening (first visit; repeat at ~28 weeks and delivery in high-prevalence settings); rapid dual HIV/syphilis point-of-care testing to expand coverage ([PMC5486952](https://pmc.ncbi.nlm.nih.gov/articles/PMC5486952)). CDC's analysis shows most US CS cases stem from **missed screening/treatment opportunities**, making screening the central lever ([Vital Signs MMWR, PMC10684351](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10684351/)).
- **Tertiary prevention:** complete infant penicillin course and serologic/CSF follow-up to prevent late stigmata; audiology/ophthalmology monitoring.
- **Immunization:** **No vaccine exists**; experimental *T. pallidum* vaccine candidates (e.g., Tp0751/pallilysin) show partial protection in rabbits but none is clinical ([PMC7113585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7113585/)).
- **Public health / program:** **WHO/PAHO dual (and triple, with hepatitis B) elimination of mother-to-child transmission (EMTCT)** validation framework; Cuba was first validated (2015) for HIV+syphilis EMTCT, followed by Thailand, Belarus, Moldova, Caribbean territories, Dominica, and the Maldives (first triple elimination, 2025) ([WHO Triple Elimination Initiative](https://www.who.int/initiatives/triple-elimination-initiative-of-mother-to-child-transmission-of-hiv-syphilis-and-hepatitis-b/validation)).
- **Counseling:** reproductive-health and partner-notification counseling (not genetic counseling — not applicable).

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogen:** *Treponema pallidum* subsp. *pallidum* (NCBI Taxonomy). Related treponematoses are caused by *T. pallidum* subsp. *pertenue* (yaws) and subsp. *endemicum* (bejel), and *T. carateum* (pinta).
- **Natural host:** Humans are the only natural host/reservoir for *T. pallidum* subsp. *pallidum*; there is no established natural congenital syphilis reservoir in companion animals or wildlife. (Note: nonhuman primates and rabbits can be experimentally infected — see §15.)
- **Veterinary / naturally occurring animal disease:** **Not applicable** for subsp. *pallidum*. OMIA has no human-equivalent congenital syphilis entry for domestic species.
- **Comparative biology / zoonosis:** No zoonotic transmission; human-restricted pathogen. (Treponeme infections exist in nonhuman primates in the wild but are distinct from human venereal/congenital syphilis.)

---

## 15. Model Organisms

- **Rabbit (*Oryctolagus cuniculus*):** the principal experimental model for *T. pallidum*; the organism is propagated by intratesticular inoculation in New Zealand White rabbits. A **rabbit model of congenital syphilis** (isolated uterine horn / in-utero exposure) reproduces many features of human CS and was used to study transplacental crossing; prior in-utero treponeme exposure markedly increased subsequent lesion severity ([pathogenesis review, PMID 11438902](https://pubmed.ncbi.nlm.nih.gov/11438902/); rabbit placental/congenital studies via [PMC search set](https://pmc.ncbi.nlm.nih.gov/articles/PMC257930)). Rabbits are also the system for Tp0751/pallilysin dissemination and vaccine studies ([PMC7113585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7113585/)).
- **Guinea pig:** an established alternative congenital-infection model; a 1992 guinea pig model offered new ways to study asymptomatic infection ([pathogenesis review, PMID 11438902](https://pubmed.ncbi.nlm.nih.gov/11438902/)).
- **Model type:** mammalian in vivo models (rabbit, guinea pig, nonhuman primate); **no genetic knockout/transgenic host models** are used because disease depends on the pathogen, not host genes. Recently, **in vitro continuous culture** of *T. pallidum* in cottontail rabbit epithelial (Sf1Ep) cell co-culture has been achieved, enabling molecular study.
- **Phenotype recapitulation:** the rabbit congenital model reproduces placental/fetal lesions resembling human CS; **limitation** — no model fully captures the human maternal–placental–fetal immunologic environment, and the historical **lack of an adequate animal model has hindered study of congenital infection** ([PMID 11438902](https://pubmed.ncbi.nlm.nih.gov/11438902/)).
- **Databases/resources:** NCBI Taxonomy (*T. pallidum*); no MGI/ZFIN/FlyBase host-gene models apply.

---

## Evidence-Source Summary

- **Human clinical / surveillance:** CDC 2023 STI Surveillance; Vital Signs MMWR 2023 (PMC10684351); Workowski 2021 STI Treatment Guidelines (PMC8344968); WHO 2022 global estimates; Gomez 2013 meta-analysis (DOI 10.2471/BLT.12.107623); Chicago risk-factor study (PMID 35493123); Suzhou risk-factor study (PMC6421965); clinico-radiologic series of 202 infants (PMID 4081939).
- **Pathology (human tissue):** 215-placenta review (informahealthcare 2023); umbilical cord study (PMID 7628852).
- **Pathogen molecular biology / in vitro + model organism:** *T. pallidum* genome (PMID 9665876); Tp0751/pallilysin–LamR (PMC7113585); TprK/immune evasion (PMID 16418521); maternal-fetal pathogenesis review (PMID 11438902).
- **Reviews:** Illustrative review (PMID 37628309); 2025 approach review (PMID 40619195).

**Key gaps / not available:** exact frequency percentages for individual early signs across a unified large cohort; validated CS-specific quality-of-life instruments; host multi-omics/single-cell/epigenomic data (not applicable — infectious disease); a human-protective genetic variant literature (not applicable). I did not independently retrieve the full text confirming the "88%" missed-opportunity figure or the precise 2024 final CS count, and flag the CDC 2021 guideline erratum for dosing verification.

---

**Sources:**
- [Congenital Syphilis—An Illustrative Review, PMID 37628309](https://pubmed.ncbi.nlm.nih.gov/37628309/)
- [Approach to Prevention, Diagnosis, and Treatment of Congenital Syphilis, PMID 40619195](https://pubmed.ncbi.nlm.nih.gov/40619195/)
- [Fraser et al., Complete genome of T. pallidum, PMID 9665876](https://pubmed.ncbi.nlm.nih.gov/9665876/)
- [Biological basis for syphilis, PMID 16418521](https://pubmed.ncbi.nlm.nih.gov/16418521/)
- [Pathogenesis of maternal-fetal syphilis revisited, PMID 11438902](https://pubmed.ncbi.nlm.nih.gov/11438902/)
- [Early congenital syphilis clinico-radiologic features in 202 patients, PMID 4081939](https://pubmed.ncbi.nlm.nih.gov/4081939/)
- [Chicago characteristics/risk factors study, PMID 35493123](https://pubmed.ncbi.nlm.nih.gov/35493123/)
- [Suzhou risk factors, PMC6421965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6421965/)
- [Gomez et al., Bull WHO 2013](https://scielosp.org/pdf/bwho/2013.v91n3/217-226/en)
- [Workowski et al., 2021 STI Treatment Guidelines, PMC8344968](https://pmc.ncbi.nlm.nih.gov/articles/PMC8344968)
- [CDC Congenital Syphilis treatment guidelines](https://www.cdc.gov/std/treatment-guidelines/congenital-syphilis.htm)
- [CDC 2023 STI Surveillance announcement](https://www.cdc.gov/sti/php/from-the-director/announcing-sti-surveillance-2023.html)
- [CDC Vital Signs MMWR 2022, PMC10684351](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10684351/)
- [CDC 2024 provisional STI statistics](https://cdc.gov/sti-statistics/annual/)
- [WHO STI strategic information (2022 estimates)](https://www.who.int/teams/global-hiv-hepatitis-and-stis-programmes/stis/strategic-information)
- [WHO syphilis fact sheet](https://www.who.int/en/news-room/fact-sheets/detail/syphilis)
- [WHO Triple Elimination Initiative / validation](https://www.who.int/initiatives/triple-elimination-initiative-of-mother-to-child-transmission-of-hiv-syphilis-and-hepatitis-b/validation)
- [Cuba EMTCT case study, PMC5486952](https://pmc.ncbi.nlm.nih.gov/articles/PMC5486952)
- [Tp0751/LamR endothelial receptor, PMC7113585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7113585/)
- [Placental syphilis review (215 placentas)](https://informahealthcare.com/doi/abs/10.1080/15513815.2023.2253309)
- [Umbilical cord/necrotizing funisitis study, PMID 7628852](https://pubmed.ncbi.nlm.nih.gov/7628852/)
- [Front Pediatr 2023 CS case/hydrops](https://frontiersin.org/journals/pediatrics/articles/10.3389/fped.2023.1215387/pdf)
- [UW National STD Curriculum: Early Congenital Syphilis](https://www.std.uw.edu/congenital-syphilis)
- [Merck Manual: Congenital Syphilis](https://www.merckmanuals.com/professional/pediatrics/infections-in-neonates/congenital-syphilis)
- [Hutchinson's triad / late stigmata, PMC2819963](https://pmc.ncbi.nlm.nih.gov/articles/PMC2819963/table/t2-pch05463)
- [NIH GARD record (identifiers)](https://rarediseases.info.nih.gov/assets/singles/22036.json)
- [NLM MeSH D013590](https://meshb.nlm.nih.gov/record/ui?ui=D013590)
- [ICD-10 A50](https://gesund.bund.de/en/icd-code-suche/a50)
- [Disease Ontology DOID:9856 (MGI)](https://www.informatics.jax.org/disease/DOID:9856)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 40 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001987` - called "placenta", "Primary organs/tissues:** **placenta"

### Terms the ontology service could not be reached for

39 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0005714` (2 mentions)
- `HP:0001433` (1 mention)
- `HP:0001744` (1 mention)
- `HP:0000988` (1 mention)
- `HP:0008066` (1 mention)
- `HP:0000421` (1 mention)
- `HP:0002658` (1 mention)
- `HP:0001873` (1 mention)
- `HP:0001789` (1 mention)
- `HP:0002383` (1 mention)
- `HP:0100785` (1 mention)
- `HP:0000678` (1 mention)
- `HP:0000486` (1 mention)
- `HP:0000491` (1 mention)
- `HP:0000407` (1 mention)
- `HP:0005105` (1 mention)
- `HP:0002979` (1 mention)
- `GO:0006952` (1 mention)
- `GO:0044409` (1 mention)
- `GO:0052126` (1 mention)
- `GO:0098542` (1 mention)
- `CL:0000786` (1 mention)
- `CL:0000084` (1 mention)
- `CL:0000115` (2 mentions)
- `CL:0000235` (1 mention)
- `UBERON:0001987` (1 mention)
- `UBERON:0002331` (1 mention)
- `UBERON:0002107` (1 mention)
- `UBERON:0002481` (1 mention)
- `UBERON:0002097` (1 mention)
- `UBERON:0001707` (1 mention)
- `UBERON:0001017` (1 mention)
- `UBERON:0000970` (1 mention)
- `UBERON:0000964` (1 mention)
- `UBERON:0001846` (1 mention)
- `UBERON:0001091` (1 mention)
- `UBERON:0002106` (1 mention)
- `GO:0005576` (1 mention)
- `GO:0005604` (1 mention)

### Terms whose obsolescence could not be checked

3 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `DOID:9856` (5 mentions)
- `HP:0002240` (1 mention)
- `HP:0001622` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

10 of 50 terms resolved to a current term; the rest could not be looked up either way.