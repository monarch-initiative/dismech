---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T14:45:10.946598'
end_time: '2026-10-27T14:49:05.328609'
duration_seconds: 234.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Vacuolar Neuromyopathy
  mondo_id: MONDO:0011155
  category: Mendelian
  causal_genes: PLIN4
  omim_id: OMIM:601846
  synonyms: muscular dystrophy with rimmed vacuoles
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
  web_search_requests: 7
  num_turns: 27
  total_cost_usd: 2.3501535000000002
  session_id: a760f68b-e45e-42e8-aba4-4cebc69ebad7
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
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
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 11
  on_topic: 10
  validator_version: 0.4.0
term_validation:
  total_terms: 42
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 9
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vacuolar Neuromyopathy
- **MONDO ID:** MONDO:0011155 (if available)
- **Causal gene(s):** PLIN4
- **OMIM:** OMIM:601846
- **Synonyms:** muscular dystrophy with rimmed vacuoles
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Vacuolar Neuromyopathy** covering all of the
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

Still gathering the remaining PLIN4 papers: the Yang 2022 abstract, the Spanish 2025 families, and the amyloid preprint. The report comes after.

Fetching the 1999 abstract for the original "vacuolar neuromyopathy" family, then I'll write the report.

# PLIN4-related vacuolar neuromyopathy (MONDO:0011155, OMIM #601846): research report

**Identity check:** this is the disease caused by the **PLIN4** gene (perilipin 4, chromosome 19p13.3). OMIM now calls #601846 "Myopathy with rimmed ubiquitin-positive autophagic vacuolation" (MRUPAV); "vacuolar neuromyopathy" (VNM) is its older name. The cause is an in-frame expansion of a 99-nucleotide coding repeat (33 amino acids per repeat) in PLIN4. The stub and the draft at `kb/disorders/Vacuolar_Neuromyopathy.yaml` both bind MONDO:0011155 with the label "vacuolar Neuromyopathy". A sibling term, MONDO:0014945 "myopathy, distal, with rimmed vacuoles", is in `cache/mondo/terms.csv`, and PanelApp Australia attaches the PLIN4 33-mer to it. Check which MONDO term carries the OMIM:601846 xref before you finalise `disease_term`.

**Evidence caveats:**
- **Cached sources:** I quoted directly only from the three files in `references_cache/`. Two have full text (PMID:32451610 and PMID:36151849). PMID:35499779 is cached with **no content** (`content_type: unavailable`), so it cannot support a snippet in its current state.
- **Other papers:** everything else below comes from PubMed or PMC pages read through a fetch tool or from search summaries. Treat those papers as **leads**: fetch each with `just fetch-reference` and take quotes from the cache before using them.
- **Ontology IDs:** I only list CURIEs that I found in the local `cache/*/terms.csv` files. Anything marked "look up" was not cached and must be resolved with OAK; do not write it from memory.

---

## 1. Disease information

**Overview.** The disease is an adult-onset, slowly progressive, autosomal dominant skeletal myopathy. Weakness is distal-predominant or limb-girdle, varying between families. Muscle biopsy shows rimmed vacuoles that stain for ubiquitin and p62, and perilipin-4 accumulates under the sarcolemma and inside the vacuoles. The cause was found by long-read sequencing of a large Italian kindred:

> "Twenty-two individuals across four generations suffer a chromosome 19p13.3-linked autosomal dominant progressive myopathy with distinctive pathology including rimmed ubiquitin-positive autophagic vacuolation" — PMID:32451610 (Ruggieri et al., *Acta Neuropathol* 2020) *(cached, full text)*

**Identifiers.**

| System | Identifier |
|---|---|
| MONDO | MONDO:0011155 (as given; label in stub "vacuolar Neuromyopathy") |
| OMIM (phenotype) | #601846 (MRUPAV / VNM) |
| OMIM (gene) | PLIN4 *613247 (PanelApp) |
| KEGG DISEASE | H02783, "Myopathy with rimmed ubiquitin-positive autophagic vacuolation" (filed under distal myopathies) |
| LOVD | disease #07149 |
| PanelApp Australia | STR `PLIN4_MRUPAV_33-mer` |
| Orphanet / ICD-10 / ICD-11 / MeSH | Not found in this search. Check the MONDO xrefs for an ORPHA code. The MeSH keyword on the papers is *Muscular Diseases/genetics*. |

**Synonyms:** vacuolar neuromyopathy (VNM); myopathy with rimmed ubiquitin-positive autophagic vacuolation (MRUPAV); PLIN4-related myopathy; PLIN4-associated myopathy; muscular dystrophy with rimmed vacuoles (the synonym supplied with the request); 19p13.3-linked distal myopathy.

**Source type:** all evidence is aggregate, from published families and case series. There is no EHR-derived data.

**Nosological caveat: is the VNM family the same disease?** The 1999 family that gave the name "vacuolar neuromyopathy" (Servidei et al., *Neurology* 1999, PMID:10489050) differs from the PLIN4 families. Per the abstract summary, it had ten affected members over three generations, onset from the late teens to the early 50s, distal-to-proximal weakness with voice and swallowing problems, **mixed neurogenic and myopathic EMG**, and rimmed vacuoles without the filamentous inclusions seen in inclusion body myositis.

The family whose expansion was found by Ruggieri 2020 is the second Italian kindred: Di Blasi et al., *Ann Neurol* 2004;56:133-138, 19 affected members over 4 generations (PMID not retrieved; look up). Fine mapping (Sangiuolo et al., *Eur J Hum Genet* 2000) narrowed the 1999 locus to about 250 kb.

I found **no publication that tested the 1999 neurogenic family for the PLIN4 expansion**. Recommendation:
- Do not attribute the "neuro-" (neurogenic) features to PLIN4 disease without such evidence.
- If the entry keeps the VNM name, record the uncertainty in `notes` or as a `KNOWLEDGE_GAP` discussion.

## 2. Etiology

- **Causal factor:** a germline in-frame expansion (or duplication) of the 99-nt / 33-aa repeat in the PLIN4 exon encoding the amphipathic-helix domain. Exon numbering differs by transcript: "exon 3" in Ruggieri 2020 and Wang 2022 (NM_001080400.1), "exon 5" in Genes Dis 2025.
- **Genetic risk factors:**
  - Expansion size: a larger expansion (50 total repeats; Yang 2022, PMID:35499779) has been linked to earlier onset and more severe disease, as reported in secondary summaries.
  - Motif composition: Wang 2022 suggests that the hypervariable motif composition of the repeat may act as a genetic modifier (a hypothesis, not demonstrated).
  - Not every series agrees: per a summary of its abstract, Llansó 2025 found no clear correlation between expansion size and severity.
- **Environmental risk, protective factors, gene-environment interactions:** none reported. One patient (Genes Dis 2025) had a single episode of severe generalized weakness at age 14 after intense exercise. That is an anecdote, not an established trigger.

## 3. Phenotypes

Pooled sources:
- Ruggieri 2020: 22 affected (Italy)
- Maggi 2023 (*J Neurol*, PMID:37145156): 15 patients from the same Italian kindred
- Wang 2022 (PMID:36151849): 4 patients from China (one family plus one sporadic case)
- Yang 2022: Chinese families
- Llansó 2025 (*Ann Clin Transl Neurol*, PMID:40693562): 2 Spanish families
- Genes Dis 2025 (PMID:41624901): 1 Italian patient with a novel duplication

| Phenotype | HPO (cached) | Frequency / characteristics | Source |
|---|---|---|---|
| Distal lower-limb weakness, often the first sign | HP:0002460 Distal muscle weakness | 13/15 had predominant lower-limb distal involvement at last visit (Maggi 2023) | PMID:37145156 |
| Proximal (limb-girdle) weakness, lower > upper limbs | HP:0003701 Proximal muscle weakness | All 3 symptomatic Chinese patients (P > D, L > U); Spanish families start proximal and become distal | PMID:36151849, PMID:40693562 |
| Neck flexor weakness | HP:0003722 | 6/13 (Maggi); 1/4 (Wang) | PMID:37145156, PMID:36151849 |
| Waddling gait; Gowers sign | HP:0002515; HP:0003391 | Case-level | PMID:36151849; PMID:41624901 |
| Scapular winging | HP:0003691 | 1/4 (Wang); 1 case in Genes Dis | PMID:36151849, PMID:41624901 |
| Areflexia | HP:0001284 | 3/4 (Wang, Table 1: "Absent") | PMID:36151849 |
| Myotonic discharges on EMG; clinical (percussion) myotonia | HP:0002486 Myotonia; HP:0010548 Percussion myotonia | Myotonic discharges in 9/9 tested; clinical myotonia (thenar percussion) 5/9 (Maggi) | PMID:37145156 |
| Myopathic EMG with complex repetitive discharges | HP:0003458 EMG: myopathic abnormalities | 4/4 (Wang: "MP+ CRDs") | PMID:36151849 |
| Mild CK elevation | Look up "Elevated circulating creatine kinase concentration" (not cached) | Normal to under 3× normal in most patients (Maggi). Wang: 256–822 IU/L (normal 70–170). Genes Dis duplication case: 1000–2166 U/L | PMID:37145156, PMID:36151849, PMID:41624901 |
| Fatty replacement on muscle MRI | HP:0012548 | Medial gastrocnemius, tibialis anterior and semimembranosus most affected; rectus femoris, gracilis and short head of biceps femoris relatively spared (Maggi). Adductors, vastus intermedius/medialis, soleus and gastrocnemius most affected; rectus femoris and gracilis spared (Wang) | PMID:37145156, PMID:36151849 |
| Restrictive ventilatory defect | HP:0002091 | Rare: 1 sporadic Chinese case; 1 Italian patient with reduced FVC; 1 tracheostomy at age 71 | PMID:36151849, PMID:37145156 |
| Atrial fibrillation | HP:0005110 | 1 patient, late onset, no cardiomyopathy. Cardiac involvement is otherwise absent | PMID:37145156 |
| Rimmed vacuoles | HP:0003805 | Present in most biopsies, including one patient with no weakness | PMID:32451610, PMID:36151849, PMID:37145156 |
| Variation in fibre size, internal nuclei | HP:0003557 Increased variability in muscle fiber diameter | Common | PMID:32451610, PMID:36151849 |
| Type 1 fibre predominance | HP:0003803 | Genes Dis case; Ruggieri notes that type I fibres are the ones affected | PMID:41624901, PMID:32451610 |
| Dysphonia, dysphagia, neurogenic EMG | HP:0001618, HP:0002015, HP:0003445 | **Only in the 1999 VNM family.** Explicitly absent in Wang's Table 1 (dysphagia "‐") | PMID:10489050 (lead) |

Supporting quote for onset and weakness pattern (Wang 2022, cached):

> "Seven individuals from four successive generations of one family (Patient F) and one sporadic patient (Patient S) suffered predominantly proximal muscle weakness in their forties to sixties" — PMID:36151849

**Quality of life.** Function declines slowly. In Wang 2022, two patients' maximal mobility was "Sit", one walked with support, and one presymptomatic 22-year-old could run. The Genes Dis 2025 case scored 35/40 on the IBM functional rating scale at age 69. No EQ-5D or SF-36 data exist.

## 4. Genetic and molecular information

- **Gene:** PLIN4 (perilipin 4; also called S3-12), 19p13.3, OMIM *613247. Look up the HGNC CURIE with OAK; it is not in `cache/hgnc/terms.csv`.
- **Normal allele:** the 33-mer is repeated 29 or 31 times in the wild type (Ruggieri: "repeated 29 or 31 times"). PanelApp gives the normal range as 27–31 copies.
- **Pathogenic alleles:**

| Repeat count | Change | Family / case | Source |
|---|---|---|---|
| 40 × 99 nt | +9 repeats (+297 aa) | Italian kindred | PMID:32451610 |
| 39 × 99 nt | Control had 29 | Chinese family | PMID:36151849 |
| ~50 total | +19 repeats; more severe, earlier onset | Chinese family | PMID:35499779 (per secondary summary) |
| 45 total | 1386-nt / 462-aa duplication (+14 repeats) in a **different part** of the repeat region (aa 491–953, versus aa 326–359 for the earlier expansions) | Italian case | PMID:41624901 |

  PanelApp's pathogenic threshold is ≥39 copies. Classification of the expansion is pathogenic for MRUPAV, as listed by PanelApp; no ClinVar or ClinGen gene-disease validity assertion was found (check `CGGV:`).
- **Variant type:** an in-frame coding repeat expansion / tandem duplication of a VNTR, not a classical STR.

  > "Oxford Nanopore long-read sequencing, which confirmed that the higher band is an expansion of the normal 31 × 99-nucleotide sequence to 40 × 99 bases, resulting in 297 (9 × 33) extra amino acids" — PMID:32451610

- **Origin:** germline, segregating in pedigrees. A sporadic case (Wang) may reflect an untested parent; de novo status was not shown.
- **Functional consequence:** a toxic gain of function or proteotoxicity. The mutant protein aggregates, and loss of function is unlikely because *Plin4*-null mice have no muscle phenotype:

  > "its absence in mouse results in no cardiac, skeletal muscle or other impairment" — PMID:32451610

  Candidate `functional_impact_category`: `NEOMORPHIC` or `GAIN_OF_FUNCTION`; mark it as inferred.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported.
- **Detection pitfall:** short-read exome and genome sequencing miss the expansion.

  > "Whole‐exome sequencing of F‐II7, F‐III3, and Patient S in 2019 revealed negative results." — PMID:36151849

  An unusually high read coverage over exon 3 was the clue in both Ruggieri 2020 and Wang 2022.

## 5. Environmental information

None known. No toxins, lifestyle factors or infectious agents have been reported. The `environmental:` section should stay empty.

## 6. Mechanism and pathophysiology

**Causal chain:**

1. A germline in-frame expansion of the 99-nt repeat in PLIN4 **leads to** perilipin-4 with an elongated amphipathic-helix domain (+297 to +627 aa). This is demonstrated by long-read sequencing and by a larger band on western blot (PMID:32451610, PMID:41624901).
2. The expanded perilipin-4 **misfolds and aggregates** in skeletal muscle fibres, mainly under the sarcolemma. Accumulation is demonstrated; misfolding is *inferred*: "suggesting that the mutation is leading to aggregation, likely through misfolding" (PMID:32451610).
   - **Branch (preprint):** the PLIN4 repeat region forms amyloid fibrils in vitro, and the expansion promotes fibrillation (bioRxiv 10.1101/2025.06.03.657256; not peer reviewed; fibrils not shown in patient muscle).
   - **Branch (association):** the aggregates co-deposit with disrupted lipid droplets, giving membrane-bound granulofilamentous inclusions and subsarcolemmal filaments (PMID:36151849). This is suggested by co-localisation and is not causal. Oil Red O lipid content stays normal in every series, so lipid storage is not the driver.
3. Ubiquitinated perilipin-4 aggregates **lead to** recruitment of the selective autophagy (aggrephagy) machinery: p62/SQSTM1, NBR1 and WDFY3 are upregulated and co-localise with the aggregates. FK2 (an antibody against ubiquitinated proteins) stains the same sites, and the number of positive fibres rises with clinical severity (PMID:32451610).
4. Aggregate load exceeds aggrephagic capacity, and repeated formation and fusion of failing autophagic vesicles **result in** rimmed autophagic vacuoles that grow larger. This step is *inferred* in PMID:32451610.
5. Vacuoles **disrupt** myofibrillar organisation and the sarcolemma. Electron microscopy shows vacuoles opening to the fibre surface and breaks in the sarcolemma. The result is impaired contractility, fibre atrophy and fatty replacement, which show clinically as progressive distal or limb-girdle weakness (step 5 is partly inferred).
   - **Secondary branch:** increased MHC-I, membrane attack complex deposition and minor inflammatory infiltrates suggest secondary inflammation (PMID:36151849). This is downstream and not a primary driver.
6. **Fibre-type selectivity:** type I (slow-twitch) fibres, which hold the most intramyocellular lipid, are preferentially affected (PMID:32451610).

**Key quote for the aggrephagy and vacuole steps** (cached):

> "The present disease is characterized by dominantly inherited progressively increasing mobilization of aggrephagy at sites of progressive accumulation of a mutated protein, suggesting that the mutation is leading to aggregation, likely through misfolding, exceeding aggrephagic capacity." — PMID:32451610

**Protein biology.** Perilipins coat the phospholipid monolayer of lipid droplets. PLIN4 is the most abundant perilipin in muscle and has a very large 11-mer → 33-mer amphipathic repeat domain. It shares this architecture with α-synuclein and exchangeable apolipoproteins, which suggests an amyloidogenic transition (PMID:32451610).

**Ontology suggestions (cached):**

| Kind | Terms |
|---|---|
| GO processes | GO:0035973 aggrephagy; GO:0016236 macroautophagy; GO:0034389 lipid droplet organization |
| GO components | GO:0005811 lipid droplet; GO:0042383 sarcolemma; GO:0005776 autophagosome; GO:0044754 autolysosome; GO:0005764 lysosome |
| Cell types | CL:0008002 skeletal muscle fiber; CL:0002211 type I muscle cell (or CL:0000189 slow muscle cell) |
| Genes | hgnc:11280 SQSTM1; hgnc:6746 NBR1 (aggrephagy readouts); look up the WDFY3 and PLIN4 CURIEs |
| `biological_scale` | Step 1 MOLECULAR; steps 2–4 CELLULAR; step 5 TISSUE |
| Module | Candidate `conforms_to`: check `just list-modules autophag` and `just list-modules aggreg` for an existing protein-aggregation or autophagic vacuolar module before writing new nodes |

**Molecular profiling:** laser-microdissected vacuole proteomics found perilipin-4 about 20-fold enriched among more than 700 proteins (PMID:32451610). Whole-muscle RNA-seq was "unrevealing". No single-cell, spatial or CRISPR data exist.

## 7. Anatomical structures

- **Organ and system:** skeletal muscle only (UBERON:0001134 skeletal muscle tissue). No CNS involvement: brain MRI was normal in Wang 2022. The heart is essentially spared (one case of atrial fibrillation). Respiratory muscles are rarely affected.
- **Most affected muscles:**
  - Medial gastrocnemius (look up)
  - Tibialis anterior (UBERON:0001385)
  - Soleus (UBERON:0001389)
  - Semimembranosus and adductor magnus (look up)
  - Vastus intermedius and medialis (look up)
- **Relatively spared:** rectus femoris, gracilis, short head of biceps femoris, tibialis posterior.
- **Subcellular sites:** subsarcolemmal region, rimmed vacuoles, and intermyofibrillar membrane-bound inclusions next to mitochondria.
- **Lateralisation:** bilateral and roughly symmetric (implied by the MRI descriptions; asymmetry not systematically reported).

## 8. Temporal development

- **Onset:** adulthood (HP:0003581 Adult onset):
  - Maggi 2023: mean 46.1 ± 10.1 years, range 30–66
  - Wang 2022: 22–49 years
  - Llansó 2025: about age 30
  - Genes Dis 2025 case: 59 years, after a transient episode at age 14

  Onset is insidious.
- **Course:** slowly progressive over decades. Weakness spreads from its starting region (distal or proximal) to other groups, and the pathology can come before clinical weakness (rimmed vacuoles in an asymptomatic carrier). No remission is reported.
- **Suggested `progression:` phases:**
  1. Presymptomatic carrier: biopsy changes possible
  2. Early: focal distal or proximal lower-limb weakness
  3. Generalised limb-girdle and distal weakness with loss of ambulation in some patients
  4. Late: rare respiratory restriction

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006), with multigenerational segregation and male-to-male transmission in the Chinese pedigree.
- **Penetrance:** appears high but age-dependent. Asymptomatic carriers with abnormal biopsies are reported, and Maggi excluded one asymptomatic carrier.
- **Expressivity:** variable in topography (distal in the Italian families, proximal in the Chinese and Spanish ones) and in severity. A larger expansion was proposed as a modifier.
- **Anticipation:** not established, and repeat instability across generations was not reported (Ruggieri: the expansion was "unvaried" in all patients).
- **Prevalence:** unknown. Fewer than about 10 families and sporadic cases have been published (Italy ×3 including the duplication case, China ≥2 plus 1 sporadic, Spain ×2). Use `measure_type: CASES_IN_LITERATURE` and do not record a numeric band.
- **Sex ratio:** no bias expected for an autosomal dominant disease; all four of Wang's patients were male.

## 10. Diagnostics

- **Muscle biopsy:** rimmed vacuoles, plus subsarcolemmal and cytoplasmic ubiquitin/p62 deposits and perilipin-4 accumulation. Perilipin-4 accumulation was not seen in other vacuolar myopathies tested (DNAJB6, VMA21, GAA, GNE, LAMP2; Maggi 2023), so perilipin-4 immunostaining is the pathology test that best separates this disease from those.

  > "the combination of subsarcolemmal/cytoplasmic ubiquitin/p62 positive deposits and rimmed vacuoles could serve as a strong indicator of PLIN4-myopathy" — PMID:36151849

- **Electron microscopy:** subsarcolemmal filamentous material and membrane-bound granulofilamentous inclusions (PMID:36151849).
- **Other tests:**
  - CK: normal to mildly raised
  - EMG: myopathic pattern with myotonic discharges and complex repetitive discharges
  - Muscle MRI: the sparing pattern in section 7
  - Oil Red O: normal, which argues against a lipid storage myopathy
- **Genetic testing:**
  - Short-read panels, exome and genome sequencing **cannot size the expansion**, but a coverage spike over the PLIN4 repeat exon is a flag.
  - Confirm with long-range PCR (an extra band about 1000 bp larger) and long-read sequencing (Nanopore or PacBio; Owusu & Savarese, *Acta Myol* 2023, PMID:38406378).
  - Western blot shows a second, larger perilipin-4 band.
  - Repeat-disorder panels such as PanelApp include the STR.
- **Differential diagnosis:** other rimmed-vacuole and distal myopathies:
  - Inclusion body myositis
  - GNE myopathy
  - DNAJB6-, VCP-, MATR3- and SQSTM1/TIA1-related myopathies
  - Myofibrillar myopathies
  - Oculopharyngodistal myopathy (also a repeat expansion)
  - Myotonic dystrophy, which shares the myotonic discharges

  Savarese et al., *Acta Myol* 2020 (PMID:33458580) lists PLIN4 among the autosomal dominant distal myopathy genes.
- **Screening:** no population screening. Cascade testing of relatives is possible.

## 11. Outcome and prognosis

No survival data exist. Life expectancy appears near normal, with no cardiomyopathy and rare respiratory involvement. Morbidity comes from progressive weakness: some patients become chair-bound, and respiratory insufficiency is rare and late (tracheostomy at age 71; nocturnal non-invasive ventilation in a patient who also had COPD). A larger expansion may predict earlier and more severe disease (Yang 2022, secondary). No prognostic biomarkers have been validated.

## 12. Treatment

No disease-modifying therapy, no clinical trials (none found), and no pharmacogenomics. Management is supportive:

| Intervention | Notes | NCIT |
|---|---|---|
| Physical therapy | | NCIT:C15302 |
| Rehabilitation / orthoses | | NCIT:C15315 |
| Respiratory monitoring; non-invasive ventilation when FVC is reduced | | Supportive Care, NCIT:C15747 |
| Genetic counselling | | NCIT:C15240 |

The NCIT codes are taken from the repo's CLAUDE.md list. Run `just validate-terms` anyway.

Two speculative therapeutic directions follow from the mechanism; neither has been tested:
- Allele-selective PLIN4 knockdown (ASO or siRNA). The rationale is that loss of PLIN4 is tolerated in mice.
- Enhancing autophagy or aggrephagy.

These belong in a `KNOWLEDGE_GAP` discussion, not under `treatments`.

## 13. Prevention

Primary prevention does not apply. Options are genetic counselling with 50% recurrence risk, predictive testing of at-risk relatives, and prenatal or preimplantation testing, which is technically possible once the familial expansion is known. Tertiary prevention means monitoring respiratory function and atrial rhythm.

## 14. Other species

No naturally occurring animal disease was found (no OMIA entry found). Mouse *Plin4* is the ortholog. The human-specific 33-mer repeat length differs across species, which is untested and worth checking in Alliance.

## 15. Model organisms

- **Mouse *Plin4* knockout:** no skeletal or cardiac muscle phenotype apart from reduced cardiac triacylglycerol (cited in PMID:32451610). This model **fails to recapitulate** the disease and is consistent with a gain-of-function mechanism. It is a candidate `FAILS_TO_RECAPITULATE` or `HUMAN_MODEL_MISMATCH` item; get the primary knockout PMID from the Ruggieri references [10, 11].
- **No expansion knock-in mouse, zebrafish, fly or iPSC-myotube model has been published**, which is a clear knowledge gap. Wang 2022:

  > "further studies on cellular and animal models are required to investigate the underlying mechanisms of perilipin‐4 aggregates in this disease." — PMID:36151849

- **In vitro:** recombinant PLIN4 repeat peptides form amyloid fibrils, and the expansion accelerates this (bioRxiv 2025 preprint; evidence source would be `IN_VITRO`).

---

## Reference list

**Cached in `references_cache/`:**
- PMID:32451610 — Ruggieri A et al. Multiomic elucidation of a coding 99-mer repeat-expansion skeletal muscle disease. *Acta Neuropathol* 2020. Full text.
- PMID:36151849 — Wang Q et al. Subsarcolemmal and cytoplasmic p62 positivity and rimmed vacuoles are distinctive for PLIN4-myopathy. *Ann Clin Transl Neurol* 2022. Full text.
- PMID:35499779 — Yang K et al. Expanding the phenotype and genotype spectra of PLIN4-associated myopathy… *Acta Neuropathol* 2022. **Cached with no content**; a correspondence piece with no abstract, so it cannot support snippets as cached.

**Leads to fetch and verify:**
- PMID:37145156 — Maggi L et al. PLIN4-related myopathy: clinical, histological and imaging data in a large cohort. *J Neurol* 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10421775/
- PMID:40693562 — Llansó L et al. Repeat Expansions in PLIN4 Cause Autosomal Dominant Vacuolar Myopathy With Sarcolemmal Features. *Ann Clin Transl Neurol* 2025.
- PMID:41624901 — Genetic variability in the PLIN4 gene: a new sequence duplication causing autophagic vacuolar myopathy. *Genes Dis* 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12854863/
- PMID:10489050 — Servidei S et al. A distinctive autosomal dominant vacuolar neuromyopathy linked to 19p13. *Neurology* 1999. Original VNM family; PLIN4 status unconfirmed.
- Di Blasi C et al. Abnormal lysosomal and ubiquitin-proteasome pathways in 19p13.3 distal myopathy. *Ann Neurol* 2004;56:133-138 (PMID to look up).
- PMID:38406378 — Owusu R, Savarese M. Long-read sequencing improves diagnostic rate in neuromuscular disorders. *Acta Myol* 2023.
- PMID:33458580 — Savarese M et al. Panorama of the distal myopathies. *Acta Myol* 2020.
- bioRxiv 10.1101/2025.06.03.657256 — Perilipin 4 repetitive region forms amyloid fibrils promoted by a genetic expansion found in myopathy patients (preprint).

**Databases:**
- [PanelApp Australia PLIN4_MRUPAV_33-mer](https://panelapp-aus.org/panels/3597/str/PLIN4_MRUPAV_33-mer/)
- [KEGG H02783](https://www.kegg.jp/entry/H02783)
- [LOVD #07149](https://databases.lovd.nl/shared/diseases/07149)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012548` (1 mention) - the report calls it "Fatty replacement on muscle MRI"; HP calls it **Fatty replacement of skeletal muscle**
- `HP:0003803` (1 mention) - the report calls it "Type 1 fibre predominance"; HP calls it **Type 1 muscle fiber predominance**, and lists "Type 1 muscle fibre predominance" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

41 of 42 terms resolved to a current term; the rest could not be looked up either way.