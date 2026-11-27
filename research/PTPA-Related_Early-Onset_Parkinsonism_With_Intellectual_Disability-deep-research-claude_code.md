---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T02:56:15.302867'
end_time: '2026-11-27T02:59:57.376309'
duration_seconds: 222.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PTPA-Related Early-Onset Parkinsonism with Intellectual Disability
  mondo_id: MONDO:0957576
  category: Mendelian
  causal_genes: PTPA
  omim_id: OMIM:620482
  synonyms: PARK25; PTPA early-onset parkinsonism with intellectual disability; PPP2R4-related
    early-onset parkinsonism
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
  web_search_requests: 12
  num_turns: 19
  total_cost_usd: 1.168214465
  session_id: 99004cfa-bcfd-4749-8931-79efa00f916c
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 25
  retrieval_calls: 23
  assistant_text_blocks: 2
citation_count: 15
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 4
  quotes_not_checkable: 1
  relevance_assessed: 17
  on_topic: 10
  validator_version: 0.8.0
term_validation:
  total_terms: 39
  verified: 24
  not_found: 1
  obsolete: 0
  unverifiable: 14
  confabulation_rate: 0.04
  labels_checked: 9
  labels_matching: 7
  labels_variant: 2
  unresolved_terms:
  - HP:0007075
  unresolvable_prefixes:
  - OMIM
  service_unreachable: 12
  obsolescence_unchecked: 15
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PTPA-Related Early-Onset Parkinsonism with Intellectual Disability
- **MONDO ID:** MONDO:0957576 (if available)
- **Causal gene(s):** PTPA
- **OMIM:** OMIM:620482
- **Synonyms:** PARK25; PTPA early-onset parkinsonism with intellectual disability; PPP2R4-related early-onset parkinsonism
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PTPA-Related Early-Onset Parkinsonism with Intellectual Disability** covering all of the
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

Status: I've read the key Fevga 2022 paper and the follow-up letters. Next I'm getting the Dulski and Li screening studies, the background biology of PTPA/PP2A, and any animal models.

# PTPA-Related Early-Onset Parkinsonism with Intellectual Disability (PARK25): Research Report

**How this report was built.** I researched the disease with the identifiers given: MONDO:0957576, OMIM:620482, causal gene **PTPA** (also called *PPP2R4*). PubMed would not load (it returned a cookie block) and shell access to NCBI E-utilities was not approved. So abstracts came through web search snippets and full text came from PMC and OUP pages. I could not read some PubMed abstracts directly (Dulski 2023, Li 2023), and they are cited only from search-result text. The patient-level clinical details for Fevga et al. 2022 come from a tool summary of the PMC full text, not from verbatim text, and are marked "(full-text summary)". Several PMIDs could not be retrieved; those sources are cited by DOI or PMC ID instead.

---

## 1. Disease Information

**Overview.** PARK25 is an autosomal recessive form of early-onset Parkinson disease with impaired intellectual development. It is caused by bi-allelic (homozygous or compound heterozygous) variants in **PTPA**, which encodes protein phosphatase 2A (PP2A) phosphatase activator, at chromosome 9q34.11 ([MedGen CN372710](https://ncbi.nlm.nih.gov/medgen/CN372710); [FlyBase FBhh0001532](https://flybase.org/reports/FBhh0001532)). Parkinsonism starts in late childhood or adolescence, on a background of developmental delay and mild-to-moderate intellectual disability (ID) (MedGen; FlyBase).

The gene–disease association was first described by Fevga et al. They concluded that "bi-allelic missense *PTPA* variants associated with impaired activation of the PP2A phosphatase" cause autosomal recessive early-onset parkinsonism with ID ([PMID 36073231](https://pmc.ncbi.nlm.nih.gov/articles/PMC10115167); DOI 10.1093/brain/awac326; *Brain* 2023;146(4):1496–1510, online 8 Sep 2022).

**Identifiers**

| Resource | ID |
|---|---|
| OMIM | 620482 (PARK25) ([MGI](https://www.informatics.jax.org/disease/OMIM:620482)) |
| MONDO | MONDO:0957576 ([MedGen](https://ncbi.nlm.nih.gov/medgen/CN372710)) |
| Disease Ontology | DOID:0070486 "Parkinson's disease 25" ([DO](https://disease-ontology.org/term/DOID:0070486)) |
| MedGen | CN372710 |
| Orphanet | None found |
| ICD-10 / ICD-11 | No specific code. Generic codes would be G20 (Parkinson disease) or ICD-11 8A00.0 plus an ID code; these were not verified in this session. |
| MeSH | No specific heading; the parent is Parkinsonian Disorders |

**Synonyms:** PARK25; Parkinson disease 25, autosomal recessive early-onset, with impaired intellectual development; PTPA-related early-onset parkinsonism with intellectual disability; PPP2R4-related early-onset parkinsonism.

**Source of the evidence.** Everything comes from individual patient reports in family-based studies (two index families, plus one possible further patient), and from aggregated resources (OMIM, MedGen, DO) built on those reports. There are no EHR- or registry-based data.

---

## 2. Etiology

**Cause.** The disease is monogenic and autosomal recessive, caused by bi-allelic missense variants in PTPA that impair activation of PP2A ([PMID 36073231](https://pmc.ncbi.nlm.nih.gov/articles/PMC10115167)).

**Genetic risk factors**
- **Causal variants (both homozygous):**
  - c.893T>G, p.Met298Arg, in a South African family.
  - c.512C>A, p.Ala171Asp, in a Libyan family with first-cousin parents (PMID 36073231).
- **Possible third variant:** homozygous p.Met329Val in one patient with early-onset PD from a consanguineous family. Her heterozygous parents and sister were healthy. No ID was mentioned in the snippet ([Li et al., *Mov Disord* 2023, PMID 37046398](https://www.pubmed.gov/37046398/)).
- **Heterozygous variants:** there is no evidence that heterozygous PTPA variants raise risk of typical PD.
  - Ostrožovičová et al. studied AMP-PD (3,105 cases / 3,670 controls, WGS), GP2 (8,190 cases / 6,052 controls across nine ancestries) and a Saudi WES cohort of 58 cases. No PTPA variant was significantly enriched after Bonferroni correction, burden tests were non-significant (minimum P ≈ 0.50), and neither M298R nor A171D was found ([PMID 37467482](https://academic.oup.com/brain/article/146/12/e120/7226645); DOI 10.1093/brain/awad247).
  - Dulski et al. concluded that "PTPA variants are rare in early-onset and familial Parkinson's disease" ([PMID 37448355](https://www.pubmed.gov/37448355/); DOI 10.1093/brain/awad244).
- **Modifier genes:** none identified.

**Environmental risk factors, protective factors and gene–environment interactions:** none reported. No CTD or GxE data are specific to this disease.

---

## 3. Phenotypes

Data come from four genotyped patients in two families, plus one ungenotyped affected cousin. Frequencies below are out of the four genotyped patients (full-text summary of [PMID 36073231](https://pmc.ncbi.nlm.nih.gov/articles/PMC10115167), unless noted).

| Phenotype | HPO term (suggested) | Type | Onset | Frequency | Notes |
|---|---|---|---|---|---|
| Juvenile/early-onset parkinsonism | HP:0002548 Parkinsonism; HP:0003621 Juvenile onset | Sign | 11–16 years | 4/4 | Abstract: "juvenile-onset parkinsonism" |
| Bradykinesia | HP:0002067 | Sign | 11–16 years | 4/4 (at onset in 3) | |
| Resting tremor | HP:0002322 | Sign | Onset | 2/4 (right hand) | |
| Rigidity | HP:0002063 | Sign | — | Reported in ≥1 (F2-IV-5) | |
| Gait disturbance | HP:0001288 | Sign | — | ≥2/4 | The ungenotyped cousin had progressive walking difficulty from age 16 |
| Intellectual disability, mild–moderate | HP:0001256 / HP:0002342 | Developmental/behavioral | Childhood | 4/4 | MedGen/OMIM describe it as nonprogressive ([MedGen](https://ncbi.nlm.nih.gov/medgen/CN372710)). Two Libyan patients left school at ages 7–8. MMSE 20–21 |
| Global developmental delay | HP:0001263 | Developmental | Infancy | 1/4 (F1-II-1, delayed milestones) | |
| Levodopa-responsive parkinsonism | HP:0002548 plus response annotation | Treatment response | — | 4/4 | |
| Levodopa-induced dyskinesia | HP:0007075 (dyskinesia) | Treatment complication | Years after starting treatment | 3/4 | |
| Impulse control disorder (on dopamine agonists) | HP:5200045 (impulsivity, suggested) | Behavioral | — | 1/4 | |
| Anxiety / depression | HP:0000739 / HP:0000716 | Behavioral | — | 1/4 | |
| Restless legs | HP:0012452 | Symptom | — | 1/4 | |
| Constipation | HP:0002019 | Symptom (non-motor) | — | 1/4 | |
| Sialorrhea | HP:0002307 | Sign | — | 1/4 | |
| Normal brain MRI | — | Imaging | — | 4/4 | |

**Severity and progression.** Motor features are progressive, as in a neurodegenerative disorder ([FlyBase](https://flybase.org/reports/FBhh0001532)). They respond well to levodopa and STN-DBS ("The motor symptoms were responsive to treatment with levodopa and deep brain stimulation of the subthalamic nucleus", PMID 36073231). Cognitive impairment is described as nonprogressive (OMIM via MedGen).

**Quality of life.** No EQ-5D or SF-36 data exist. The ID led to early school exit or no mainstream schooling (full-text summary).

---

## 4. Genetic/Molecular Information

**Gene**
- PTPA (protein phosphatase 2 phosphatase activator; previous symbol PPP2R4), 9q34.11 ([MedGen](https://ncbi.nlm.nih.gov/medgen/CN372710)).
- HGNC:9308; NCBI Gene 5524; UniProt Q15257. These IDs are from my own knowledge and were not retrieved in this session.
- The mouse orthologue is *Ptpa* (NCBI Gene 110854, [NCBI](https://ncbi.nlm.nih.gov/gene/110854)).
- The *Drosophila* orthologue is *ptpa* (FBgn0016698).
- Constraint: pLI = 0.98 (full-text summary, PMID 36073231).

**Pathogenic variants**

| Variant (NM_178001) | Type | Zygosity | Population | gnomAD | CADD | Evidence |
|---|---|---|---|---|---|---|
| c.893T>G p.(Met298Arg) | Missense | Homozygous | South African, non-consanguineous parents | Absent | 32 | Co-segregates. Protein ~0.81 of WT and less stable over a 3 h chase |
| c.512C>A p.(Ala171Asp) | Missense | Homozygous | Libyan, first-cousin parents | Absent | 23.6 | Protein ~0.06 of WT; degraded via the proteasome (rescued by MG-132) |
| p.(Met329Val) | Missense | Homozygous | Consanguineous family; ancestry not confirmed | — | — | Lowered protein stability without changing mRNA ([PMID 37046398](https://www.pubmed.gov/37046398/)) |

Sources: PMID 36073231 (full-text summary); the transcript NM_178001 is stated verbatim in Methods. I did not retrieve ClinVar or ACMG classifications.

- **Functional consequence:** partial loss of function (hypomorphic). Both variants reduced PP2A-C levels and impaired PP2A activation. Measured phosphatase activity was WT 2626, A171D 1930, M298R 2139, against a baseline of 1602 pmol phosphate (full-text summary).
- **Origin:** germline.
- **Somatic variants elsewhere:** heterozygous PPP2R4 deletions and missense mutations are common in cancers. Sents et al. reported that "up to 70% of cancer patients" had heterozygous deletion or missense mutation of PPP2R4 ([Sents et al., *Cancer Res* 2017;77(24), DOI 10.1158/0008-5472.CAN-16-2911](https://doi.org/10.1158/0008-5472.22416183.v1)). This is not related to PARK25.
- **Modifier genes, epigenetic data and chromosomal abnormalities:** none reported.

---

## 5. Environmental Information

No environmental, lifestyle or infectious contributors have been reported. This section is not applicable on current evidence.

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. Bi-allelic PTPA missense variants (M298R, A171D) **lead to** lower PTPA mRNA (~0.74–0.77 of WT) and less stable PTPA protein; A171D undergoes marked proteasomal degradation. *[Demonstrated in vitro, HEK-293 overexpression; PMID 36073231]*
2. Lower functional PTPA **results in** less "activation" of the PP2A catalytic subunit (PP2A-C). Normally, PTPA, with Mg²⁺/ATP, converts PP2A-C from an inactive, conformationally relaxed state into the active conformation during holoenzyme biogenesis ([Hombauer et al. 2007, PMID 17550305](https://pmc.ncbi.nlm.nih.gov/articles/PMC1885835); [Chao et al. 2006, PMID 16916641](https://pubmed.ncbi.nlm.nih.gov/16916641/); [Guo et al. 2014, *Cell Res*, PMC3915903](https://pmc.ncbi.nlm.nih.gov/articles/PMC3915903)). *[Mechanism shown in yeast, structural and biochemical work; reduced PP2A activation by the patient variants shown in vitro]*
3. Impaired activation **leads to** lower PP2A-C levels (0.67–0.74 of WT) and fewer PP2A complexes, with reduced phosphatase activity. *[In vitro, PMID 36073231]*
   - **Branch, by analogy:** in hypomorphic Ptpa gene-trap mice, PP2A-C methylation is reduced and B56/B′-containing holoenzymes are selectively affected ([Sents 2017](https://doi.org/10.1158/0008-5472.22416183.v1); [Meeusen & Janssens, PMC5769971](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5769971/)). *[Inferred for neurons; not shown in patient cells]*
4. Low PP2A activity in neurons is **proposed to lead to** hyperphosphorylation of PP2A substrates relevant to PD, such as α-synuclein, LRRK2-pathway proteins and tau, and to faulty synaptic regulation. *[Inferred hypothesis; the full-text summary says the paper discussed these only as hypotheses]*
5. Neuronal PTPA deficiency **results in** age-dependent motor decline that L-DOPA reverses. In *Drosophila*, pan-neuronal *ptpa* knockdown impaired climbing at days 20 and 35 but not day 10. "This defect was age-dependent and fully reversed by L-DOPA treatment" (PMID 36073231). This implies a dopamine deficit. *[Model organism. Whether dopaminergic neurons are actually lost was not reported]*
6. Presumed nigrostriatal dopaminergic dysfunction **leads to** juvenile levodopa- and DBS-responsive parkinsonism. *[Human clinical; nigral loss is inferred, with no DaT-SPECT or pathology]*
7. **Parallel branch:** PTPA/PP2A dysfunction during neurodevelopment **is proposed to lead to** intellectual disability. *[Inferred.]* Supporting evidence for a role of PTPA in synapse development: in Angelman model mice, UBE3A ubiquitinates PTPA for degradation, so PTPA and PP2A activity rise. Reducing PTPA genetically (*Ptpa*+/−) rescued dendritic spine and synaptic transmission deficits ([Wang et al., *PNAS* 2019, PMC6589679](https://pmc.ncbi.nlm.nih.gov/articles/PMC6589679)). This suggests PP2A activity in synapses has to be kept within a narrow range; that point is my inference.

### Mechanism categories

- **Pathways:** PP2A holoenzyme biogenesis and activation. Suggested GO terms: GO:0008160 protein tyrosine phosphatase activator activity; GO:0019888 protein phosphatase regulator activity; GO:0006470 protein dephosphorylation; GO:0043666 regulation of phosphoprotein phosphatase activity. Signalling output: Wnt, Hedgehog and c-Myc signalling changes in the gene-trap tumors (Sents 2017).
- **Protein dysfunction:** loss of protein stability and partial loss of function. PTPA has a three-subdomain fold (core, lid and linker). "PTPA and PP2A A–C dimer together constitute a composite ATPase" (Chao 2006, PMID 16916641). A crystal structure of PTPA–PP2A with ATPγS is available as PDB 4LAC (Guo et al.).
- **Cellular processes:** GO:0007626 locomotory behavior (fly). Dopamine-related processes: GO:0042417 dopamine metabolic process (inferred).
- **Cell types:** CL:0000700 dopaminergic neuron (inferred); CL:0000540 neuron.
- **Immune, metabolic, epigenetic and omics data:** none reported.

---

## 7. Anatomical Structures Affected

- **Organ and system:** the brain and nervous system (UBERON:0000955 brain).
  - Presumed involvement of the nigrostriatal system: UBERON:0002038 substantia nigra; UBERON:0002435 striatum.
  - The subthalamic nucleus (UBERON:0001906) is the DBS target.
  - The cerebral cortex is presumed to underlie the ID (inferred).
- **Cells:** dopaminergic neurons (CL:0000700), inferred from levodopa response and the fly rescue.
- **Subcellular:** PTPA and PP2A act in the cytosol (GO:0005829) and nucleus (GO:0005634); the PP2A holoenzyme is GO:0000159. I did not retrieve localization data specific to patients.
- **Laterality:** tremor began asymmetrically (right hand) in two patients (full-text summary).
- **Imaging:** brain MRI was normal (4/4).

---

## 8. Temporal Development

- **Onset:** motor signs started at ages 11–16 (juvenile, insidious). Intellectual and developmental impairment was evident from childhood (PMID 36073231; MedGen).
- **Course:** motor signs are chronic and progressive, while cognition is nonprogressive (MedGen; FlyBase). Dyskinesias appeared within years of starting levodopa, for example at age 30 in one patient.
- **Stages, remission and natural history:** no staging or natural-history data exist. There is no spontaneous remission; symptoms improve with treatment.
- **Critical periods:** the neurodevelopmental window, relevant to ID, is inferred. The fly data suggest the motor phenotype appears with age.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (OMIM; PMID 36073231).
- **Penetrance:** appears complete in homozygotes, though n is small. Heterozygous carriers are unaffected (PMID 37046398).
- **Expressivity:** variable for developmental delay (1/4) and non-motor features. The p.Met329Val patient may have had PD without ID (unconfirmed).
- **Consanguinity:** present in the Libyan family and the p.Met329Val family, but absent in the South African family.
- **Founder effects:** none established. Ostrožovičová et al. suggested the association "may be population-specific, possibly limited to people of African descent" (paraphrase; PMID 37467482).
- **Prevalence:** unknown. Fewer than 10 genotyped patients have been reported worldwide.
  - Screening found no further bi-allelic carriers among 200 Sanger-screened patients or 589 WES-sequenced FMPD index families (PMID 36073231).
  - Nor were any found in the large AMP-PD, GP2 and Saudi datasets (PMID 37467482).
- **Sex ratio:** 2 male and 2 female genotyped patients.
- **Ancestry:** South African, Libyan (North African), and one further consanguineous family of unconfirmed ancestry.
- **Carrier frequency:** both index variants are absent from gnomAD.

---

## 10. Diagnostics

- **Genetic testing**
  - Exome sequencing (with homozygosity or linkage mapping in consanguineous families) identified both index families; this is the recommended first-tier approach.
  - Multigene PD panels should include PTPA, though its inclusion in commercial panels was not verified in GTR.
  - Targeted Sanger testing suits cascade testing.
  - CMA, karyotype, repeat-expansion and mtDNA testing have no specific role, apart from ruling out other diagnoses.
- **Imaging:** brain MRI is normal. DaT-SPECT and PET were not reported (full-text summary).
- **Laboratory and biomarkers:** none specific to the disease. PP2A activity assays are for research only.
- **Clinical criteria:** none specific to the disease. Suspect it in juvenile, levodopa-responsive parkinsonism with ID.
- **Differential diagnosis:** other recessive early-onset parkinsonisms, especially those with ID or developmental features:
  - PRKN, PINK1 and DJ-1 (usually without ID)
  - ATP13A2 (Kufor-Rakeb)
  - DNAJC6, SYNJ1, VPS13C, PLA2G6, FBXO7
  - X-linked RAB39B (ID plus parkinsonism)
  - Dopa-responsive dystonias (GCH1, TH)
  - Wilson disease

  This list is from clinical knowledge and was not retrieved in this session; the 2025 review by Cogan et al. covers AR-EOPD genetics (PMID 41253044, not read).
- **Screening:** no newborn or population screening. Cascade carrier testing is possible in affected families.

---

## 11. Outcome/Prognosis

- **Survival and life expectancy:** no data. Patients were alive at ages 24–33 at last examination (full-text summary).
- **Morbidity:** progressive motor disability that responds to treatment; motor complications (dyskinesias, 3/4); ID that limits schooling; neuropsychiatric comorbidities (impulse control disorder on agonists, anxiety, depression).
- **Prognostic factors and biomarkers:** none established.

---

## 12. Treatment

All evidence comes from a case series; there are no trials (PMID 36073231, full-text summary).

| Intervention | NCIT (suggested) | Outcome |
|---|---|---|
| Levodopa (CHEBI:15765) | NCIT C607 Levodopa | Good to complete response in 4/4. In the Libyan siblings, 500 mg/day and 250 mg/day. Dyskinesias in 3/4 |
| Dopamine agonists | NCIT C1513 class (dopamine agonist) | Impulse control disorder in 1 patient |
| STN deep brain stimulation | NCIT C80384 Deep Brain Stimulation | Effective in both South African siblings |
| Supportive care | — | Special education, physical and occupational therapy, psychiatric care (standard practice; no disease-specific data) |

- **Pharmacogenomics:** none.
- **Gene, cell or RNA therapy:** none.
- **Clinical trials:** none found. A ClinicalTrials.gov search was not done.
- **Experimental ideas:** restoring PP2A activity, for example with small-molecule PP2A activators, is a theoretical rationale only (inferred). The Angelman model shows the PTPA/PP2A axis can be targeted pharmacologically, but in the opposite direction, with the PP2A inhibitor LB-100 ([PMC6589679](https://pmc.ncbi.nlm.nih.gov/articles/PMC6589679)).

---

## 13. Prevention

- **Primary prevention, behavioral measures and vaccines:** not applicable.
- **Genetic counseling:** each sibling of an affected person has a 25% recurrence risk. Carrier testing, prenatal diagnosis and PGT are possible once the familial variants are known. Consanguinity raises risk.
- **Tertiary prevention:** limit dopamine-agonist exposure (impulse control disorder risk); manage levodopa dyskinesias; consider DBS.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** no OMIA entry or natural animal disease found.
- **Orthologues:** mouse *Ptpa* (Gene 110854; Mus musculus, NCBITaxon:10090), *Drosophila ptpa* (FBgn0016698; NCBITaxon:7227), and yeast RRD1/RRD2 (NCBITaxon:4932) (PMID 17550305).
- **Conservation:** PTPA function is conserved from yeast to human (PMID 17550305), and Met298 is conserved among orthologues (PMID 36073231).
- **Zoonotic potential:** none.

---

## 15. Model Organisms

| Model | Description | Recapitulation | Source |
|---|---|---|---|
| *Drosophila*, pan-neuronal *ptpa* RNAi (nSyb-Gal4; VDRC 41912) | Negative geotaxis (climbing) assay. *prkn* RNAi was the positive control and *nsmase* the negative control | Age-dependent climbing defect at days 20 and 35, not day 10, seen in females. Fully rescued by L-DOPA (1 mg/ml). Dopaminergic neuron counts not reported | PMID 36073231 |
| HEK-293 overexpression of mutant PTPA | Protein and RNA levels, stability (cycloheximide chase), PP2A-C levels, phosphatase activity | Shows the biochemical defect; not neuronal | PMID 36073231 |
| Mouse *Ptpa* gene-trap (hypomorph; *gt/gt* and *+/gt*) | Reduced PP2A activity and methylation | Tumors (hematologic, liver) and shorter lifespan in heterozygotes. No neurological phenotyping reported | [Sents 2017](https://doi.org/10.1158/0008-5472.22416183.v1) |
| Mouse *Ptpa*+/− crossed with Angelman (*Ube3a* m−/p+) mice | Links PTPA to synapses | Rescues spine and synaptic deficits; relevant to the ID branch, not to PD | [PMC6589679](https://pmc.ncbi.nlm.nih.gov/articles/PMC6589679) |
| Yeast *rrd1Δ rrd2Δ* | PP2A biogenesis | Basic mechanism | PMID 17550305 |

- **Not yet available:** iPSC-derived dopaminergic neurons from patients, knock-in mice carrying M298R or A171D, and a neuron-specific *Ptpa* knockout mouse.
- **Model limitations:** the fly is a knockdown, not a missense model; the cell work uses overexpression in a non-neuronal line; and the mouse models were not studied for neurology.

---

## Key Evidence Items

| PMID / ID | Type | Key point |
|---|---|---|
| 36073231 (Fevga et al., *Brain* 2022/2023) | Human genetics, in vitro, *Drosophila* | Founding gene–disease report. Quotes: "The motor symptoms were responsive to treatment with levodopa and deep brain stimulation of the subthalamic nucleus."; "This defect was age-dependent and fully reversed by L-DOPA treatment." |
| 37046398 (Li et al., *Mov Disord* 2023) | Human genetics | Homozygous p.Met329Val in one patient with early-onset PD from a consanguineous family; the variant lowers protein stability |
| 37467482 (Ostrožovičová et al., *Brain* 2023) | Human case-control (AMP-PD, GP2, Saudi) | No enrichment or burden of PTPA variants in PD |
| 37448355 (Dulski et al., *Brain* 2023) | Human genetics | "PTPA variants are rare in early-onset and familial Parkinson's disease" |
| 17550305 (Hombauer et al., *PLoS Biol* 2007) | Yeast | PTPA/RRD is needed to switch PP2A-C into its active conformation |
| 16916641 (Chao et al., *Mol Cell* 2006) | Structural | "composite ATPase" model of PTPA with the PP2A A–C dimer |
| DOI 10.1158/0008-5472.CAN-16-2911 (Sents et al., *Cancer Res* 2017) | Mouse | Hypomorphic *Ptpa* lowers PP2A activity and methylation |
| PMC6589679 (*PNAS* 2019) | Mouse | UBE3A ubiquitinates PTPA; PTPA/PP2A affects synapse development |
| 41253044 (Cogan et al., 2025) | Review of AR-EOPD genetics | Title retrieved only; content not read |

**Gaps in the evidence:**
- No ClinVar or ACMG classifications, no gnomAD carrier frequencies, no Orphanet entry, and no natural-history or quality-of-life data.
- No dopaminergic imaging and no neuropathology.
- The disease has been confirmed in only two families, and replication is limited to one possible further patient.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:37467482`: "may be population-specific, possibly limited to people of African descent"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 14 |
| Terms whose name was checked | 9 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0007075` (1 mention), reported as "dyskinesia" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000700` (2 mentions) - the report calls it "Cells:** dopaminergic neurons"; CL calls it **dopaminergic neuron**
- `CHEBI:15765` (1 mention) - the report calls it "Levodopa"; CHEBI calls it **L-dopa**, and lists "levodopa" among its other names

### Terms the ontology service could not be reached for

12 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0957576` (2 mentions)
- `HP:0002342` (1 mention)
- `HP:5200045` (1 mention)
- `HP:0012452` (1 mention)
- `GO:0008160` (1 mention)
- `GO:0019888` (1 mention)
- `GO:0007626` (1 mention)
- `GO:0042417` (1 mention)
- `GO:0005829` (1 mention)
- `GO:0005634` (1 mention)
- `GO:0000159` (1 mention)
- `NCBITaxon:4932` (1 mention)

### Terms whose obsolescence could not be checked

15 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0002548` (2 mentions)
- `HP:0003621` (1 mention)
- `HP:0002067` (1 mention)
- `HP:0002322` (1 mention)
- `HP:0001256` (1 mention)
- `HP:0001263` (1 mention)
- `HP:0000716` (1 mention)
- `HP:0002019` (1 mention)
- `HP:0002307` (1 mention)
- `GO:0043666` (1 mention)
- `CL:0000540` (1 mention)
- `UBERON:0002435` (1 mention)
- `UBERON:0001906` (1 mention)
- `CHEBI:15765` (1 mention)
- `NCBITaxon:7227` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.