---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-26T15:47:02.561445'
end_time: '2026-11-26T15:52:07.504886'
duration_seconds: 304.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cardiovascular Syphilis
  mondo_id: MONDO:0004911
  category: Infectious Disease
  causal_genes: not recorded
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 17
  total_cost_usd: 1.137078655
  session_id: caa02e64-9492-4cac-ae9f-74114f99540f
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  tool_calls: 40
  retrieval_calls: 34
  assistant_text_blocks: 5
citation_count: 21
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 24
  quotes_valid: 22
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:36940224
  - PMID:26678367
  relevance_assessed: 42
  on_topic: 27
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 32
  verified: 10
  not_found: 0
  obsolete: 0
  unverifiable: 22
  confabulation_rate: 0.0
  service_unreachable: 22
  obsolescence_unchecked: 3
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiovascular Syphilis
- **MONDO ID:** MONDO:0004911 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cardiovascular Syphilis** covering all of the
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

Bash is restricted, so I'm switching to web search to gather sources.

**Correction to my first report:** the full search 1 list I gave was wrong. The raw response has 20 IDs: 2679075, 17469346, 18920964, 19068539, 14777886, 32375627, 35102592, 33607833, 18862983, 14367862, 18876793, 14832504, 20250332, 15413122, 24536340, 32598616, 29608710, 30073493, 19932797, 13501141. I had dropped 18876793 and listed 32598616 twice. The first 10 used for the abstract fetch were correct.

## A. efetch of 12 PMIDs

Quotes are from a non-preapproved source, so each is under 125 characters.

1. **29608710**: 2018, Eur Heart J Cardiovasc Imaging, "Cardiovascular syphilis: down but not out!" No abstract.
2. **30073493**: 2018, Z Rheumatol, "Syphilitic aortic aneurysm." "Syphilitic aortic aneurysm occurred most commonly in the ascending aorta in either a saccular or a fusiform shape." / "Syphilitic aortic aneurysm was often complicated by aortic valve insufficiency"
3. **33744210**: 2021, JACC Cardiovasc Interv, "Syphilitic Aortitis Causing Severe Bilateral Coronary Ostial Stenosis." No abstract.
4. **38785248**: 2024, Khirurgiia (Mosk), "[Surgical treatment of a patient with syphilitic aortitis]." "Syphilitic aortitis is a rare disease caused by Treponema pallidum affecting the aorta and leading to inflammation." (Russian abstract also present.)
5. **37862785**: 2023, J Int Med Res, "Treatment of syphilitic aortitis with coronary artery bypass grafting and "open" stent placement." "Cardiovascular syphilis manifests many years after primary infection."
6. **40562738**: 2025, Emerg Infect Dis, "Syphilitic Aortitis with Concomitant Neurosyphilis in Asymptomatic Patient." "This case highlights the need to consider emerging infectious causes of aortitis"
7. **33824800**: 2021, Cureus, "Syphilitic Aortic Aneurysm: A Rare Entity in the Era of Antibiotics." "A thoracic aortic aneurysm is a rare entity of tertiary syphilis in the era of antibiotics."
8. **32598616**: 2019, Ter Arkh, "[Cardiovascular syphilis (current state of the problem and analysis of own observations)]." "A description of two cases of cardiovascular syphilis is presented." (Russian abstract also present.)
9. **6079826**: 1967, Indian Heart J, "Syphilitic aortitis." No abstract.
10. **20071445**: 2010, Int J STD AIDS, "Syphilitic aneurysm." "Syphilis was once the most common cause of aortic aneurysm."
11. **22925534**: 2012, J Neurol Sci, "Syphilitic aortic aneurysm with spastic paraparesis: a novel presentation and review of the literature." "We describe the novel presentation of a 55 year old man with a syphilitic aneurysm"
12. **39902879**: 2025, Cardiol Rev (epub ahead of print), "Cardiovascular Syphilis." "As a result, cardiovascular syphilis mostly remains a disease of the past"

## B. esearch (retmax 5) and efetch of top results

**1. Roberts syphilitic aortitis necropsy** (Count 2): 19932796, 4751946
- **19932796**: 2009, Am J Cardiol, "Natural history of syphilitic aortitis." "No large studies of cardiovascular syphilis at necropsy have been reported since 1964." / "We examined at necropsy 90 patients who had characteristic morphologic findings of syphilitic aortitis."
- **4751946**: 1973, Circulation, "Ankylosing spondylitis and aortic regurgitation..." Not about syphilis; no abstract.

**2. Workowski 2021 STI treatment guidelines** (Count 4): 34292926, 35416973, 35416968, 33003184
- **34292926**: 2021, MMWR Recomm Rep, "Sexually Transmitted Infections Treatment Guidelines, 2021." "These guidelines for the treatment of persons who have or are at risk for sexually transmitted infections"
- **35416973**: 2022, Clin Infect Dis, trichomonas evidence summary for the 2021 guidelines. "Trichomonas vaginalis is likely the most prevalent nonviral sexually transmitted infection"
- **35416968**: 2022, Clin Infect Dis, bacterial vaginosis evidence summary for the 2021 guidelines. No quote used.
- **33003184**: 2021, Sex Transm Dis, "Estimating Recommended Gonorrhea and Chlamydia Treatment Rate..." Not syphilis. "indicated low rates of recommended gonorrhea and chlamydia treatment"

**3. Peeling syphilis Nature Reviews Disease Primers** (Count 1): 29022569
- **29022569**: 2017, Nat Rev Dis Primers, "Syphilis." "syphilis is re-emerging as a global public health problem"

**4. Tp0751 vascular adhesin T. pallidum** (Count 4): 32238570, 28484210, 28145405, 34354688
- **32238570**: 2020, mSphere, "Identification of the Neuroinvasive Pathogen Host Target, LamR, as an Endothelial Receptor for the Treponema pallidum Adhesin Tp0751." "One protein that has been shown to play a role in treponemal dissemination is Tp0751, a T. pallidum adhesin"
- **28484210**: 2017, Sci Rep, "Identification of Tp0751 (Pallilysin) as a Treponema pallidum Vascular Adhesin by Heterologous Expression in the Lyme disease Spirochete." "These results demonstrate that Tp0751 can function as a vascular adhesin."
- **28145405**: 2017, Nat Commun, "A defined syphilis vaccine candidate inhibits dissemination of Treponema pallidum subspecies pallidum." "These findings provide evidence that Tp0751 is a promising syphilis vaccine candidate."
- **34354688**: 2021, Front Microbiol, "Treponema pallidum Disrupts VE-Cadherin Intercellular Junctions and Traverses Endothelial Barriers Using a Cholesterol-Dependent Mechanism." "Treponema pallidum subspecies pallidum, the causative agent of syphilis, traverses the vascular endothelium"

**5. TprK antigenic variation T. pallidum** (Count 22): 16418521, 36940224, 36711914, 37769216, 20190145
- **16418521**: 2006, Clin Microbiol Rev, "Biological basis for syphilis." "Antigenic variation of TprK, a putative surface-exposed protein, is likely to contribute to immune evasion."
- **36940224**: 2023, PLoS Pathog, "Treponema pallidum subsp. pallidum with an Artificially impaired TprK antigenic variation system is attenuated in the Rabbit model of syphilis." "These data further support the critical role of TprK in T. pallidum virulence and persistence during infection."
- **36711914**: 2023, bioRxiv preprint, same work as 36940224. No separate quote.
- **37769216**: 2024 (epub 2023), J Infect Dis, "Genomic Epidemiology of Treponema pallidum and Circulation of Strains With Diminished tprK Antigen Variation Capability in Seattle, 2021-2022." "tprK sequencing may assist in linking cases beyond routine T. pallidum genome sequencing."
- **20190145**: 2010, J Immunol, "Antigenic variation in Treponema pallidum: TprK sequence diversity accumulates in response to immune pressure during experimental syphilis." "These studies demonstrate that the host immune response selects against specific TprK epitopes"

**6. Rabbit model syphilis T. pallidum review** (Count 7): 2644069, 26678367, 42383912, 8476969, 16362988
- **2644069**: 1989, Crit Rev Microbiol, "Experimental syphilis in guinea pig." Guinea pig, not rabbit. "For eight decades the rabbit has been the major animal model in studies of syphilis."
- **26678367**: 2015, Comp Med, "Rabbit Models for Studying Human Infectious Diseases." "This review focuses on the human infectious diseases for which rabbits are considered a classic"
- **42383912**: 2026, Sex Transm Dis, "A New Era in Treponema pallidum Cultivation: Current Advances and Future Directions." "it has revolutionized and accelerated research with this difficult pathogen" (about in vitro culture, not rabbits)
- **8476969**: 1993, Int J STD AIDS, "A review and update on adult syphilis, with particular reference to its treatment." "The importance of cell mediated immunity in syphilis has been demonstrated in animal models." (not rabbit-specific)
- **16362988**: 2006, J Pathol, "The pathogenesis of syphilis: the Great Mimicker, revisited." "inferences made from animal models are of limited applicability"

**7. Syphilis penicillin Jarisch-Herxheimer reaction** (Count 133): 37457541, 36743098, 6017505, 33643725, 64863
- **37457541**: 2023, Indian J Sex Transm Dis AIDS, "Jarisch‒Herxheimer reaction." "The Jarisch‒Herxheimer reaction (JHR) is a transient immunological phenomenon"
- **36743098**: 2022, Indian J Sex Transm Dis AIDS, "Jarisch-Herxheimer reaction in syphilis." "JHR is a self-limiting reaction."
- **6017505**: 1967, Br Med J, "Jarisch-Herxheimer reaction." No abstract.
- **33643725**: 2021, Cureus, "Jarisch-Herxheimer Reaction After Cephalosporin Administration in Syphilis." "Severe reactions are uncommon but may include signs of exaggerated systemic inflammatory response."
- **64863**: 1977, Lancet, "The Jarisch-Herxheimer reaction." No abstract.

**8. Syphilis aortitis FDG PET/CT** (Count 7): 41220469, 23835659, 41164740, 23377199, 23143047
- **41220469**: 2025, Cureus, "Syphilitic Aortitis Incidentally Detected by Fluorine-18 Fluorodeoxyglucose (18F-FDG) PET/CT." "Utilization of 18F-FDG PET/CT imaging can facilitate the identification of syphilitic aortitis"
- **23835659**: 2013, Clin Rheumatol, comment "Usefulness of 18F-FDG PET/CT in syphilitic aortitis." No abstract.
- **41164740**: 2025, Eur Heart J Case Rep, "Pegfilgrastim (Neulasta)-induced acute aortitis: a case report." Not syphilis; syphilis was ruled out. No quote used.
- **23377199**: 2013, Clin Rheumatol, "Early recognition of aortitis of the aorta ascendens with 18F-FDG PET/CT: syphilitic?" "(18)F-FDG PET/CT can help in an early establishment of syphilitic aortitis"
- **23143047**: 2013, Clin Nucl Med, "Usefulness of (18)F-FDG PET/CT in disease extent and treatment response assessment in a patient with syphilitic aortitis." "This case highlights the usefulness of FDG PET/CT for the assessment of disease extent and treatment response"

**9. Syphilis global burden incidence WHO 2022** (Count 17): 41100079, 34508022, 35261411, 38438164, 35256043
- **41100079**: 2025, JAMA, "Syphilis: A Review." "Worldwide, an estimated 8 million adults aged 18 to 49 years acquired syphilis in 2022."
- **34508022**: 2022, Sex Transm Dis, "High Burden of Active Syphilis and Human Immunodeficiency Virus/Syphilis Coinfection Among Men Who Have Sex With Men, Transwomen, and Genderqueer Individuals in Zimbabwe." "Findings highlight a high burden of syphilis among MSM and TGW/GQ"
- **35261411**: 2022, Bull World Health Organ, "WHO method for estimating congenital syphilis to inform surveillance and service provision, Paraguay." "The incidence rate of congenital syphilis estimated using the WHO tool was around nine times the reported prevalence."
- **38438164**: 2024, J Travel Med, "A systematic review and meta-analysis of sexually transmitted infections and blood-borne viruses in travellers." "Strategies to prevent STIs and sexually transmitted BBVs should be discussed at pre-travel consultations"
- **35256043**: 2022, Chin Med Sci J, "Eliminating Mother-to-Child Transmission of Syphilis: Chinese Practice before and during COVID-19 Pandemics." "Mother-to-child transmission (MTCT) of syphilis remains a leading cause of stillbirth and death among neonates"

**10. Treponema pallidum lipoprotein innate immunity TLR2** (Count 1): 18406378
- **18406378**: 2008, Immunobiology, "Immune responses induced by spirochetal outer membrane lipoproteins and glycolipids." "these structures have been convincingly shown to activate immune cells via CD14 and Toll-like receptor (TLR)-2"

## URLs read
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=29608710,30073493,33744210,38785248,37862785,40562738,33824800,32598616,6079826,20071445,22925534,39902879&rettype=abstract&retmode=text
- esearch for each of the 10 terms, retmax 5, sort=relevance (URLs follow the pattern `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<term>&retmax=5&sort=relevance`)
- efetch batches for the top-5 PMIDs of each term: 19932796,4751946,34292926,35416973,35416968,33003184,29022569,32238570,28484210,28145405,34354688; 34354688,16418521,36940224,36711914,37769216,20190145,2644069,26678367,42383912,8476969,16362988; 37457541,36743098,6017505,33643725,64863,41220469,23835659,41164740,23377199,23143047; 41100079,34508022,35261411,38438164,35256043,18406378

Sending any of these URLs again would return the same content.

## 1. More quotes from 8 abstracts

All quotes are verbatim from the efetch output, each under 125 characters.

**19932796** (2009, Am J Cardiol, "Natural history of syphilitic aortitis.")
- "All 90 had extensive involvement of the tubular portion of the ascending aorta by the syphilitic process"
- "The aortic arch was also involved in 49 (91%) of 54 patients"
- "Syphilis was the cause of death in 23 (26%) of the 90 patients."
- "Of the 40 patients who had undergone serologic testing for syphilis, 28 (70%) had a positive (reactive) finding."
- "antibiotic therapy appears desirable."

**27982548** (2018, G Ital Dermatol Venereol, "Syphilitic aortitis and its complications in the modern era.")
- "Aortic aneurysm was the most frequent involvement, detected in 71% of patients."
- "The second most common complication was the aortic valvular insufficiency, found in 47% of patients."
- "Forty four articles were collected, reporting on 66 patients."
- "Fusiform or saccular aneurysms often interested the thoracic aorta, primarily located on the ascending segment."
- "most patients had no predisposing factors and denied a primary infection."

**30073493** (2018, Z Rheumatol, "Syphilitic aortic aneurysm.")
- "Syphilitic aortic aneurysm was often complicated by aortic valve insufficiency (in almost half of the patients)"
- "by a coronary artery/ostium lesion in 16.5% of the patients."
- "Aortic valve operation was necessary in one fourth,"
- "coronary artery surgery accounted for less than one fifth of patients warranting a surgical treatment."
- "there was no difference in the survival rates between the surgically and conservatively treated patients"

**41100079** (2025, JAMA, "Syphilis: A Review.")
- "Worldwide, an estimated 8 million adults aged 18 to 49 years acquired syphilis in 2022."
- "From 2019 to 2023, US syphilis cases increased by 61% overall,"
- "In pregnancy, up to 40% of fetuses with in-utero exposure to syphilis are stillborn or die from their infection"
- "benzathine penicillin G administered as intramuscular doses of 2.4 million units"
- "a single injection for early stage and 3 weekly injections for late latent stage"

**29022569** (2017, Nat Rev Dis Primers, "Syphilis.")
- "Syphilis also causes several hundred thousand stillbirths and neonatal deaths every year in developing nations."
- "its clinical manifestations result from local inflammatory responses to replicating spirochaetes"
- "The spirochaete has a long latent period during which individuals have no signs or symptoms but can remain infectious."
- "the effectiveness of treatment with a single dose of long-acting penicillin"
- "Although several low-income countries have achieved WHO targets for the elimination of congenital syphilis,"

**16362988** (2006, J Pathol, "The pathogenesis of syphilis: the Great Mimicker, revisited.")
- "While biological functions are suggested for only about 55% of T. pallidum's 1041 open reading frames,"
- "Antibodies to the TprK variable regions are protective in a rabbit model."
- "Human and animal studies suggest that a Th1 response is elicited in primary syphilis."
- "Progression to the secondary stage is accompanied by a shift to a Th2 response,"
- "intense inflammatory responses and prostaglandins induced by fetal infection may be responsible for fetal death"

**34354688** (2021, Front Microbiol, "Treponema pallidum Disrupts VE-Cadherin Intercellular Junctions and Traverses Endothelial Barriers...")
- "traverses endothelial barriers with no disruption in barrier permeability"
- "barrier traversal by T. pallidum is reduced by pretreatment of endothelial cells with filipin"
- "a subpopulation of T. pallidum localizes to intercellular junctions"
- "suggests that a paracellular route may also be utilized,"
- No percentages, times, or treatment data in this abstract.

**28145405** (2017, Nat Commun, "A defined syphilis vaccine candidate inhibits dissemination of Treponema pallidum subspecies pallidum.")
- "Tp0751-immunized animals exhibit a significantly reduced bacterial organ burden upon T. pallidum challenge"
- "fails to induce infection, confirming sterile protection."
- "Syphilis elimination will require development of an effective vaccine that has thus far remained elusive."
- "Syphilis is a prominent disease in low- and middle-income countries,"
- No numeric animal data in the abstract.

## 2. MeSH lookup

The descriptor is **D013589**, label "Syphilis, Cardiovascular" (http://id.nlm.nih.gov/mesh/D013589). It was the only exact match returned.

## 3. OLS4 MONDO search

The search returned 3 MONDO hits (numFound 3). The search response does not include xrefs (ICD10, UMLS, MeSH, DOID) for any hit, and only the third hit includes a synonym field.

1. **MONDO:0004911**, label "cardiovascular syphilis." Description: "A tertiary syphilis that is manifested as aneurysm formation in the ascending aorta, caused by chronic inflammatory destruction of the vasa vasorum, insufficiency of the aortic valve, or narrowing of the coronary arteries." No synonyms or xrefs returned.
2. **MONDO:0006992**, label "syphilitic aortitis." Description: "Cardiovascular manifestations of syphilis... Clinical signs include syphilitic aortitis, aortic insufficiency, or aortic aneurysm." No synonyms or xrefs returned.
3. **MONDO:0004497**, label "tertiary syphilis." Exact synonyms: "late tertiary syphilis", "late syphilis", "tertiary syphilis." No xrefs returned.

To get xrefs, the per-term OLS record would need to be fetched. I did not fetch it because no URL was given for it.

## 4. CDC treatment guidelines

- https://www.cdc.gov/std/treatment-guidelines/tertiary.htm returned **HTTP 404**. Retrying that URL would fail the same way.
- The latent-syphilis page at https://www.cdc.gov/std/treatment-guidelines/latent-syphilis.htm returned 200. It links to the tertiary page as its "Next" page, so I fetched https://www.cdc.gov/std/treatment-guidelines/tertiary-syphilis.htm, which returned 200 (last reviewed July 22, 2021).

**Recommended regimen (tertiary-syphilis page):** "Persons with gummas and cardiovascular syphilis who are not allergic to penicillin and have no evidence of neurosyphilis by clinical and CSF examination should be treated with the following regimen." The regimen is "Benzathine penicillin G 7.2 million units total, administered as 3 doses of 2.4 million units IM each at 1-week intervals."

**CSF recommendations:**
- "All persons who have tertiary syphilis should receive a CSF examination before therapy is initiated and have an HIV test."
- "Persons with CSF abnormalities should be treated with a neurosyphilis regimen."
- "Certain providers treat all persons who have cardiovascular syphilis with a neurosyphilis regimen."

**Other points:**
- "Any person allergic to penicillin should be treated in consultation with an infectious disease specialist."
- "Limited information is available concerning clinical response and follow-up of persons who have tertiary syphilis."

The tertiary page does not give the neurosyphilis regimen doses. It refers to a separate neurosyphilis page (https://www.cdc.gov/std/treatment-guidelines/neurosyphilis.htm), which I did not fetch.

## URLs read
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=19932796,27982548,30073493,41100079,29022569,16362988,34354688,28145405&rettype=abstract&retmode=text
- https://id.nlm.nih.gov/mesh/lookup/descriptor?label=Syphilis,%20Cardiovascular&match=exact
- https://www.ebi.ac.uk/ols4/api/search?q=cardiovascular%20syphilis&ontology=mondo
- https://www.cdc.gov/std/treatment-guidelines/tertiary.htm (404)
- https://www.cdc.gov/std/treatment-guidelines/latent-syphilis.htm
- https://www.cdc.gov/std/treatment-guidelines/tertiary-syphilis.htm

I have the sources I need and am now writing the report.

# Cardiovascular Syphilis (MONDO:0004911): Disease Characteristics Report

**How I read the request:** Cardiovascular syphilis is an infectious disease, not a Mendelian one. **It has no causal human gene.** The causal agent is the bacterium *Treponema pallidum* subsp. *pallidum*. I filled the genetics sections with "not applicable" or with the relevant pathogen biology.

**Sources:** I retrieved every cited item in this session from PubMed E-utilities, MeSH, the EBI OLS (MONDO), CDC pages or web search. Most older PubMed records (1948–1989) have no abstract, so I cite only their titles. Abstract quotes are verbatim and short.

---

## 1. Disease Information

**Overview.** MONDO defines cardiovascular syphilis (MONDO:0004911) as *"A tertiary syphilis that is manifested as aneurysm formation in the ascending aorta, caused by chronic inflammatory destruction of the vasa vasorum, insufficiency of the aortic valve, or narrowing of the coronary arteries"* (EBI OLS4 MONDO search). A 2006 review states that "Cardiovascular tertiary syphilis may lead to aortitis, aortic aneurism, coronary stenosis" (PMID 17469346). A 2025 Cardiology Review says "cardiovascular syphilis mostly remains a disease of the past" (PMID 39902879). Other authors report that it still occurs: "Cardiovascular syphilis is still present nowadays" (PMID 27982548), and a 2020 commentary is titled "The comeback of syphilitic aortitis" (PMID 32580086).

**Identifiers**

| System | ID / code | Source |
|---|---|---|
| MONDO | MONDO:0004911 cardiovascular syphilis. Related terms: MONDO:0006992 syphilitic aortitis; parent concept MONDO:0004497 tertiary syphilis | EBI OLS4 |
| MeSH | **D013589** "Syphilis, Cardiovascular" | id.nlm.nih.gov/mesh/D013589 |
| ICD-10-CM | A52.0 Cardiovascular and cerebrovascular syphilis (category heading, not reportable alone). Subcodes: A52.00 unspecified, **A52.01 syphilitic aneurysm of aorta**, **A52.02 syphilitic aortitis**, A52.03 syphilitic endocarditis, A52.04 syphilitic cerebral arteritis, A52.05 other cerebrovascular syphilis, A52.06 other syphilitic heart involvement | [Unbound Medicine](https://www.unboundmedicine.com/icd/view/ICD-10-CM/892850/all/A52_01___Syphilitic_aneurysm_of_aorta), [icdlist](https://icdlist.com/icd-10/A5201) |
| ICD-10 (WHO) | A52.0 Cardiovascular syphilis | [gesund.bund.de](https://gesund.bund.de/en/icd-code-suche/a52-0) |
| ICD-11, Orphanet, OMIM | Not retrieved. OMIM does not apply because the disease is not Mendelian | — |

**Synonyms (from the retrieved literature):** syphilitic aortitis (strictly a sub-manifestation), luetic aortitis, syphilitic aortic aneurysm, tertiary cardiovascular syphilis, and syphilitic heart disease (not retrieved as a formal synonym). The OLS search returned no MONDO synonyms for MONDO:0004911.

**Source type:** The knowledge comes from aggregate disease-level sources: necropsy series, literature reviews of case reports, historical cohorts and guidelines. No EHR-derived cohorts were retrieved.

## 2. Etiology

- **Cause:** chronic infection with *T. pallidum* subsp. *pallidum*. Cardiovascular disease is a late (tertiary) complication of untreated or inadequately treated syphilis: "Cardiovascular syphilis manifests many years after primary infection" (PMID 37862785).
- **Risk factors:**
  - Untreated or under-treated syphilis is the main one. About 10% of untreated persons develop syphilitic aortitis after 10–30 years (CDC EID 2025 case report, PMID 40562738, [EID](https://wwwnc.cdc.gov/eid/article/31/7/25-0646)).
  - Acquiring syphilis itself carries the risks of sexual transmission. The populations with rising incidence include men who have sex with men and transgender women (PMID 34508022).
  - US cases rose by 61% from 2019 to 2023 (PMID 41100079), so the pool of people at risk of future late disease is growing. This is an inference.
  - In a modern review of 66 cases, "most patients had no predisposing factors and denied a primary infection" (PMID 27982548). Many patients therefore have no history of the initial infection.
- **Genetic risk and protective factors:** none retrieved. No GWAS or host-genetic susceptibility loci for cardiovascular syphilis were found.
- **Protective factors:** timely penicillin treatment of early or latent syphilis, which is inferred from the decline after antibiotics arrived (PMID 33824800, 20071445). Incidental antibiotic exposure is not documented in the retrieved sources.
- **Gene–environment interactions:** none documented.

## 3. Phenotypes

| Phenotype | Suggested HPO term | Frequency / characteristics | Evidence |
|---|---|---|---|
| Aortitis, ascending aorta (tubular portion) | HP:0004942 Aortitis (unverified ID) | Present in 100% of necropsy cases (by definition). "All 90 had extensive involvement of the tubular portion of the ascending aorta"; arch involved in 49/54 (91%) | PMID 19932796 |
| Thoracic aortic aneurysm (saccular or fusiform, mostly ascending) | HP:0012727 Thoracic aortic aneurysm (unverified) | 71% of modern reported cases. "Aortic aneurysm was the most frequent involvement, detected in 71% of patients" | PMID 27982548, 30073493 |
| Aortic regurgitation | HP:0001659 Aortic regurgitation | 47% of reported cases; "almost half" in the aneurysm review | PMID 27982548, 30073493 |
| Coronary ostial stenosis, often bilateral, causing angina or myocardial infarction | HP:0001677 Coronary artery atherosclerosis (closest term); HP:0001658 Myocardial infarction; HP:0001681 Angina pectoris | 16.5% in the aneurysm review; up to 26% in another review | PMID 30073493; PMC10945892 |
| Acute myocardial infarction | HP:0001658 | Reported in case reports | PMID 33607833 |
| Compressive effects of the aneurysm, e.g. spastic paraparesis | HP:0002313 Spastic paraparesis | Rare | PMID 22925534 |
| Asymptomatic aortitis (found incidentally) | — | Common, but no reliable percentage was retrieved | PMID 40562738, 41220469 |
| Reactive serology (lab) | — | 28/40 (70%) of tested necropsy patients were reactive | PMID 19932796 |
| Concomitant neurosyphilis | HP:0012332 (unverified) | Reported in case reports | PMID 40562738 |

- **Onset:** adult or late, typically 10–30 years after infection (PMID 40562738). The 30-year-old case in PMID 32375627 shows it can appear earlier.
- **Severity:** ranges from silent aortitis to fatal rupture or heart failure. Syphilis caused death in 26% of the necropsy series (PMID 19932796).
- **Progression:** chronic and progressive.
- **Quality of life:** no EQ-5D or SF-36 data were retrieved. The burden is mainly from heart failure caused by aortic regurgitation, angina, and the effects of major cardiac surgery.

## 4. Genetic/Molecular Information

**Human genetics:** not applicable. There are no causal genes, pathogenic variants (ClinVar/ACMG), modifier genes, epigenetic findings or chromosomal abnormalities.

**Pathogen molecular factors (in vitro, animal and genomic evidence):**
- T. pallidum genome: "only about 55% of T. pallidum's 1041 open reading frames" have suggested biological functions (PMID 16362988).
- **TprK** antigenic variation drives immune evasion and persistence:
  - "Antigenic variation of TprK... is likely to contribute to immune evasion" (PMID 16418521).
  - "the host immune response selects against specific TprK epitopes" (PMID 20190145).
  - A strain with impaired variation "is attenuated in the Rabbit model" (PMID 36940224).
  - Strains with diminished tprK variation capability are circulating (PMID 37769216).
  - This persistence is the plausible basis for decades-long latency (inference).
- **Tp0751 (pallilysin)** binds vascular tissue: "Tp0751 can function as a vascular adhesin" (PMID 28484210). Its endothelial receptor is laminin receptor LamR (PMID 32238570).
- **Outer membrane lipoproteins** activate innate immunity "via CD14 and Toll-like receptor (TLR)-2" (PMID 18406378).

## 5. Environmental Information

- **Infectious agent:** *Treponema pallidum* subsp. *pallidum*. NCBI Taxonomy ID not retrieved here; it is generally cited as NCBITaxon:161, unverified in this session.
- **Transmission:** sexual contact or vertical (mother to child). "The spirochaete has a long latent period during which individuals have no signs or symptoms but can remain infectious" (PMID 29022569).
- **Lifestyle factors:** the sexual behaviors that drive acquisition (above).
- **Toxins and occupational exposures:** none relevant.

## 6. Mechanism / Pathophysiology

**Causal chain**

1. *T. pallidum* infection at a mucosal or skin site **leads to** rapid spread through the blood. The spirochete crosses the endothelium "with no disruption in barrier permeability", partly through a cholesterol-dependent route and partly through intercellular junctions (in vitro; PMID 34354688). Vascular adhesion is mediated by Tp0751–LamR (PMID 28484210, 32238570).
2. Antigenic variation (TprK) plus scant surface antigens **result in** escape from immune clearance and lifelong latent persistence when untreated (animal and in vitro evidence; PMID 20190145, 36940224). *Persistence specifically in the aortic adventitia is inferred.*
3. Spirochetes lodged in the adventitia of the aortic root and arch **lead to** perivascular inflammation around the **vasa vasorum**, with lymphocytes and plasma cells; one report describes mainly CD138+ plasma cells (pathology sources via search; PMID 27982548 context).
4. Chronic inflammation **results in** obliterative endarteritis of the vasa vasorum. Endothelial swelling and intimal proliferation narrow the vessels (histopathology; [pathology references](https://histo.uaz.edu.mx/pathology/ed/ch_10/c10_s22.htm)).
5. Ischemia of the outer media **leads to** focal medial necrosis, loss of elastic fibres and smooth muscle, and scarring. Scarring wrinkles the intima into the "tree-bark" appearance (histopathology).
6. Weakening of the media **branches into three paths**:
   - 6a. Aortic wall dilation **leads to** a saccular or fusiform aneurysm, mostly in the ascending aorta (PMID 30073493). Possible endpoints are compression of nearby structures (PMID 22925534) or rupture and death.
   - 6b. Dilation of the aortic root plus spread to the commissures **leads to** aortic regurgitation, then left-ventricular volume overload and heart failure (PMID 27982548).
   - 6c. Intimal thickening at the aortic root **leads to** coronary ostial stenosis. The result is angina, myocardial infarction or sudden death (PMID 33607833, 33744210). Distal coronary arteries are typically spared.
7. The damage is driven by the immune response rather than by bacterial load. Treponemes are scarce in lesions while inflammation is intense (pathology sources). The general model is that "clinical manifestations result from local inflammatory responses to replicating spirochaetes" (PMID 29022569). The suggested Th1→Th2 shift (PMID 16362988) has been described only for primary and secondary disease; its role in tertiary disease is inferred.

**Suggested GO terms:** GO:0006954 inflammatory response; GO:0002224 toll-like receptor signaling pathway; GO:0042110 T cell activation; GO:0030183 B cell differentiation / plasma cell; GO:0001525 angiogenesis (vasa vasorum remodelling, inferred); GO:0042742 defense response to bacterium.

**Suggested CL terms:** CL:0000786 plasma cell; CL:0000542 lymphocyte; CL:0000235 macrophage; CL:0000115 endothelial cell; CL:0000192 smooth muscle cell; CL:0000057 fibroblast.

**Molecular profiling:** no transcriptomic, proteomic, metabolomic, single-cell or spatial studies of cardiovascular syphilis were retrieved.

## 7. Anatomical Structures Affected

- **Primary site:** the ascending thoracic aorta, tubular portion (UBERON:0001496 ascending aorta), involved in 100% of necropsy cases. The aortic arch (UBERON:0001508) was involved in 91% (PMID 19932796).
- **Secondary sites:**
  - aortic valve (UBERON:0002137)
  - coronary artery ostia (UBERON:0001621 coronary artery)
  - left ventricle (UBERON:0002084), through volume overload
  - descending aorta (less common)
- **Tissue:** aortic adventitia and media (UBERON:0002523 tunica media; UBERON:0005734 tunica adventitia of blood vessel) and the vasa vasorum.
- **Subcellular:** treponemal interaction at endothelial intercellular junctions (GO:0005911 cell-cell junction; PMID 34354688).
- **Lateralization:** not applicable. Ostial lesions are often bilateral (PMID 11170338).

## 8. Temporal Development

- **Onset:** insidious, in adulthood, 10–30 years after infection (PMID 40562738, 37862785).
- **Stages:** uncomplicated aortitis, then complicated disease (aneurysm, aortic regurgitation, ostial stenosis), then end-stage disease (heart failure, rupture).
- **Course:** chronic and progressive. Antibiotics do not reverse structural damage that is already present. This is inferred from the high surgical burden in PMID 30073493 and from CDC: "Limited information is available concerning clinical response and follow-up of persons who have tertiary syphilis."
- **Critical window:** treating early or latent syphilis prevents late disease. FDG-PET has been used to track treatment response of aortitis (PMID 23143047).

## 9. Inheritance and Population

- **Inheritance:** not applicable (acquired infection). Congenital syphilis exists, but no cardiovascular-syphilis-specific data were retrieved for it.
- **Epidemiology:**
  - Historical: "Syphilis was once the most common cause of aortic aneurysm" (PMID 20071445).
  - Oslo cohort: 28% of untreated patients had late complications ([Oslo study summaries](https://en.wikipedia.org/wiki/Oslo_study); Gjestland 1955, [Acta Derm Venereol](https://www.medicaljournals.se/acta/content/abstract/10.2340/00015555343368)). I did not retrieve the cardiovascular-specific percentage.
  - Historical figures vary widely. One review cites cardiovascular syphilis in up to 70% of untreated patients and aneurysm in 8–45% ([PMC5695631](https://pmc.ncbi.nlm.nih.gov/articles/PMC5695631)).
  - Modern incidence and prevalence per 100,000 for cardiovascular syphilis were not retrieved; the condition is rare.
- **Background syphilis burden:** an estimated 8 million new adult cases worldwide in 2022 (PMID 41100079). Syphilis is "re-emerging as a global public health problem" (PMID 29022569).
- **Demographics:** the necropsy series and case reports are mostly men in their 40s–60s (PMID 19932796, 11170338, 22925534). I retrieved no formal sex ratio.

## 10. Diagnostics

- **Serology:**
  - Nontreponemal tests (RPR/VDRL) plus treponemal tests (TPPA, EIA/CLIA). Nontreponemal tests can be negative in late disease. In the necropsy series, 70% of tested patients were reactive (PMID 19932796).
  - LOINC codes were not retrieved.
- **CSF and HIV testing:** CDC states "All persons who have tertiary syphilis should receive a CSF examination before therapy is initiated and have an HIV test" ([CDC tertiary syphilis](https://www.cdc.gov/std/treatment-guidelines/tertiary-syphilis.htm); PMID 34292926). Concurrent neurosyphilis occurs (PMID 40562738).
- **Imaging:**
  - echocardiography for aortic regurgitation
  - CT or MR angiography for aneurysm and aortic wall thickening
  - coronary angiography or CT for ostial stenosis
  - 18F-FDG PET/CT for active aortitis and treatment response (PMID 23377199, 23143047, 41220469)
- **Pathology:**
  - plasma-cell and lymphocyte infiltrate around the vasa vasorum
  - obliterative endarteritis and medial scarring
  - tree-bark intima
  - few spirochetes (immunohistochemistry or PCR can help; specifics not retrieved)
- **Genetic testing (WES/WGS/panels/CMA):** not applicable to the host. Pathogen genome or tprK sequencing is used for epidemiology (PMID 37769216).
- **Clinical clue:** screen for syphilis in patients with bilateral ostial lesions without distal coronary disease, or with an ascending aortic aneurysm ([MJA](https://mja.com.au/node/5267)).
- **Differential diagnosis** (not individually sourced here):
  - Takayasu arteritis
  - giant-cell arteritis
  - IgG4-related aortitis
  - ankylosing spondylitis–associated aortitis with aortic regurgitation (PMID 4751946)
  - Marfan syndrome and other heritable thoracic aortic disease
  - atherosclerotic aneurysm
  - other infectious (mycotic) aortitis
- **Screening:** there is no specific screening for cardiovascular syphilis. Syphilis screening in at-risk groups and in pregnancy is the upstream measure (PMID 34292926).

## 11. Outcome/Prognosis

- **Mortality:** syphilis caused death in 23/90 (26%) of the necropsy series (PMID 19932796).
- **Surgery versus conservative treatment:** in a 2000–2017 review of syphilitic aneurysm, "Aortic valve operation was necessary in one fourth", and "there was no difference in the survival rates between the surgically and conservatively treated patients" (PMID 30073493).
- **Complications:**
  - aneurysm rupture
  - heart failure from aortic regurgitation
  - myocardial infarction (PMID 33607833)
  - compression syndromes (PMID 22925534)
- PCI for ostial stenosis has a high re-occlusion rate ([PMC12414935](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12414935/)).
- **Life expectancy, QoL measures and prognostic biomarkers:** not retrieved.

## 12. Treatment

- **Antimicrobial therapy (CDC 2021):**
  - Persons without neurosyphilis are given "Benzathine penicillin G 7.2 million units total, administered as 3 doses of 2.4 million units IM each at 1-week intervals."
  - "Persons with CSF abnormalities should be treated with a neurosyphilis regimen". Also, "Certain providers treat all persons who have cardiovascular syphilis with a neurosyphilis regimen" (usually IV aqueous penicillin G).
  - People allergic to penicillin should be treated with infectious disease consultation ([CDC](https://www.cdc.gov/std/treatment-guidelines/tertiary-syphilis.htm); PMID 34292926, 41100079).
  - NCIT term: Benzathine Penicillin G (NCIT code not retrieved).
- **Adverse effect:** the Jarisch–Herxheimer reaction, "a transient immunological phenomenon" that is usually self-limiting (PMID 37457541, 36743098). Severe forms show "exaggerated systemic inflammatory response" (PMID 33643725). Whether it matters in coronary ostial disease is not addressed in the retrieved sources.
- **Surgical and interventional treatment:**
  - aortic aneurysm repair or ascending aortic replacement (PMID 38785248)
  - aortic valve replacement, including TAVR (PMID 35102592)
  - CABG, or ostial surgery and stenting (PMID 37862785)
  - ECMO-assisted PCI in acute MI (PMID 33607833)
  - "there are no established consensus guidelines" for combined aortic regurgitation and ostial stenosis (PMC12414935)
- **Supportive care:** standard heart failure and anti-anginal management (not specifically sourced).
- **Pharmacogenomics and gene/cell/RNA therapy:** not applicable.
- **Experimental:** no cardiovascular-syphilis-specific trials were retrieved. The Tp0751 vaccine candidate is preclinical (see section 13).

## 13. Prevention

- **Primary prevention:** safer sexual practices, condoms, and partner notification. No vaccine exists; "Syphilis elimination will require development of an effective vaccine that has thus far remained elusive" (PMID 28145405).
- **Secondary prevention:** screen at-risk populations and pregnant people, and treat early or latent syphilis with benzathine penicillin G: "a single injection for early stage and 3 weekly injections for late latent stage" (PMID 41100079). This is the key step that prevents cardiovascular disease.
- **Tertiary prevention:** check CSF and HIV status, give complete penicillin therapy, monitor the aorta and valve with imaging, and operate when indicated.
- **Public health:** WHO congenital syphilis elimination programs (PMID 35261411, 35256043).
- **Genetic counseling:** not applicable.

## 14. Other Species / Natural Disease

- *T. pallidum* subsp. *pallidum* is human-adapted. No naturally occurring cardiovascular syphilis in animals was retrieved, and OMIA does not apply.
- Other treponemes cause disease in animals (e.g., *T. paraluiscuniculi* in rabbits; *T. pallidum* infection in nonhuman primates), but I retrieved no sources for this in this session.
- **Zoonotic potential:** none established.

## 15. Model Organisms

- **Rabbit (*Oryctolagus cuniculus*):** "For eight decades the rabbit has been the major animal model in studies of syphilis" (PMID 2644069; also PMID 26678367). It is used for TprK variation and virulence studies (PMID 20190145, 36940224) and for vaccine testing. Tp0751-immunized rabbits showed "significantly reduced bacterial organ burden" (PMID 28145405).
- **Guinea pig:** an experimental model (PMID 2644069).
- **In vitro:**
  - long-term T. pallidum culture, which "has revolutionized and accelerated research" (PMID 42383912)
  - endothelial cell barrier models (PMID 34354688)
  - heterologous expression of Tp0751 in *Borrelia burgd

Section 15 was cut off at the end. To finish it concisely:

**Model organisms (continued):**
- **Rabbit** — the primary model for syphilis research for decades (PMID 2644069, 26678367), used for TprK/virulence work (PMID 20190145, 36940224) and vaccine testing (PMID 28145405).
- **Guinea pig** — an alternative experimental model (PMID 2644069).
- **In vitro** — long-term *T. pallidum* culture (PMID 42383912) and endothelial barrier models (PMID 34354688).
- **Model limitations:** these systems model the *infection and dissemination* of *T. pallidum*, not the decades-long tertiary aortitis itself. "Inferences made from animal models are of limited applicability" to human disease (PMID 16362988). No animal model reproduces human cardiovascular syphilis, so mechanistic claims about the aortic lesion rest on human necropsy and clinical pathology rather than on model organisms.

---

That completes the report. A few summary notes on evidence quality and gaps:

- **No human genetics applies** — this is an infectious disease caused by *Treponema pallidum* subsp. *pallidum*; sections on causal genes, variants, inheritance and genetic testing of the host are "not applicable."
- **Strongest evidence:** the Roberts et al. necropsy series of 90 patients (PMID 19932796) and two modern literature reviews (PMID 27982548, 30073493) anchor the frequencies (aneurysm ~71%, aortic regurgitation ~47%, ostial lesions ~16.5%, syphilis-attributable death 26%).
- **Weaker/unretrieved areas:** modern incidence/prevalence per 100,000, formal sex ratio, QoL measures, prognostic biomarkers, molecular profiling (transcriptomics/proteomics/metabolomics), and ICD-11/Orphanet identifiers were not retrieved and are flagged as such in-text.
- **Key identifiers confirmed this session:** MONDO:0004911, MeSH D013589, ICD-10-CM A52.0 (with A52.01/A52.02).

Sources:
- [PMC12414935 — CV syphilis, severe AR + bilateral ostial stenosis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12414935/)
- [EID 2025 — syphilitic aortitis with neurosyphilis](https://wwwnc.cdc.gov/eid/article/31/7/25-0646)
- [CDC — Tertiary syphilis treatment](https://www.cdc.gov/std/treatment-guidelines/tertiary-syphilis.htm)
- [MeSH D013589](https://id.nlm.nih.gov/mesh/D013589)
- [ICD-10-CM A52.01 (Unbound Medicine)](https://www.unboundmedicine.com/icd/view/ICD-10-CM/892850/all/A52_01___Syphilitic_aneurysm_of_aorta) · [icdlist A5201](https://icdlist.com/icd-10/A5201) · [gesund.bund.de A52.0](https://gesund.bund.de/en/icd-code-suche/a52-0)
- [Syphilitic aortitis pathology atlas](https://histo.uaz.edu.mx/pathology/ed/ch_10/c10_s22.htm)
- [Oslo study (overview)](https://en.wikipedia.org/wiki/Oslo_study) · [Gjestland 1955 Acta Derm Venereol](https://www.medicaljournals.se/acta/content/abstract/10.2340/00015555343368)
- [PMC5695631 — untreated syphilis review](https://pmc.ncbi.nlm.nih.gov/articles/PMC5695631)
- [MJA case report — screening clues](https://mja.com.au/node/5267)

All PMIDs cited inline were retrieved via PubMed E-utilities in this session.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 24 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 42 |
| On topic | 27 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:36940224` *(abstract only)*: "is attenuated in the Rabbit model"
  - closest text in source: "pallidum strain to impair its ability to vary TprK and assessed its virulence in the rabbit model of syphilis"
- `PMID:26678367` *(abstract only)*: "For eight decades the rabbit has been the major animal model in studies of syphilis"
  - closest text in source: "This review focuses on the human infectious diseases for which rabbits are considered a classic or highly appropriate model, including AIDS (caused by HIV1), adult T-cell leukemia-lymphoma (human T-lymphotropic virus type 1), papilloma or carcinoma (human papillomavirus) , herpetic stromal keratitis (herpes simplex virus type 1), tuberculosis (Mycobacterium tuberculosis), and syphilis (Treponema pallidum)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 22 |

### Terms the ontology service could not be reached for

22 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0004911` (6 mentions)
- `MONDO:0004497` (2 mentions)
- `HP:0004942` (1 mention)
- `HP:0012727` (1 mention)
- `HP:0001677` (1 mention)
- `HP:0001681` (1 mention)
- `HP:0012332` (1 mention)
- `GO:0006954` (1 mention)
- `GO:0042742` (1 mention)
- `CL:0000542` (1 mention)
- `CL:0000235` (1 mention)
- `CL:0000115` (1 mention)
- `CL:0000192` (1 mention)
- `CL:0000057` (1 mention)
- `UBERON:0001496` (1 mention)
- `UBERON:0001508` (1 mention)
- `UBERON:0002137` (1 mention)
- `UBERON:0001621` (1 mention)
- `UBERON:0002084` (1 mention)
- `UBERON:0002523` (1 mention)
- `UBERON:0005734` (1 mention)
- `GO:0005911` (1 mention)

### Terms whose obsolescence could not be checked

3 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `MONDO:0006992` (2 mentions)
- `HP:0001658` (2 mentions)
- `HP:0002313` (1 mention)

10 of 32 terms resolved to a current term; the rest could not be looked up either way.