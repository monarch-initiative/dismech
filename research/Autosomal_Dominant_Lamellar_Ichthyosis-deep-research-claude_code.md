---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-26T10:20:06.064243'
end_time: '2026-10-26T10:23:51.385529'
duration_seconds: 225.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Dominant Lamellar Ichthyosis
  mondo_id: MONDO:0007812
  category: Mendelian
  causal_genes: ASPRV1
  omim_id: OMIM:146750
  synonyms: ichthyosis lamellar, autosomal dominant
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
  num_turns: 19
  total_cost_usd: 1.9779806999999996
  session_id: 211b7378-6360-46f9-a7d2-5f607fb8c2f1
  stop_reason: end_turn
  permission_denials: 1
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
citation_count: 12
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 18
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 21
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 7
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Lamellar Ichthyosis
- **MONDO ID:** MONDO:0007812 (if available)
- **Causal gene(s):** ASPRV1
- **OMIM:** OMIM:146750
- **Synonyms:** ichthyosis lamellar, autosomal dominant
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Lamellar Ichthyosis** covering all of the
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

Still researching: I have the core ASPRV1 papers and am now pulling abstracts for the remaining key ones (new human case, NKPD1 heterogeneity, the mouse and dog models).

# Autosomal Dominant Lamellar Ichthyosis (ASPRV1; MONDO:0007812; OMIM 146750): research report

**Scope.** This report covers ichthyosis, lamellar, autosomal dominant (MONDO:0007812, OMIM 146750). Its causal gene is **ASPRV1**, which encodes aspartic peptidase retroviral-like 1, also called SASPase (skin aspartic protease). The gene is HGNC:26321 (written `hgnc:26321` in dismech), sits at 2p13.3, has gene OMIM 611765 and UniProt Q53RT3, and Entrez ID 151516.

Since 2024 the disorder is known to be genetically heterogeneous. A second dominant gene, **NKPD1**, produces a clinically similar picture that differs on ultrastructure (Komlosi 2024, PMID:38642798). This report is about the ASPRV1 form throughout. The NKPD1 form should be treated as a separate entity or subtype rather than folded in.

**How the sources were checked.**
- Abstracts were fetched through NCBI E-utilities.
- The Boyden 2020 full text came from PMC7332602.
- Identifiers came from HGNC REST and EBI OLS.
- Quotes marked "verbatim" were taken from fetched abstracts, each under 125 characters. They still need a pass of `just fetch-reference` plus snippet validation before they go into KB YAML.
- **All ontology CURIEs suggested below are leads only.** I have not looked them up here. Each needs an OAK or cache lookup before it is bound, per the repository rule.

---

## 1. Disease information

**Overview.** This is a rare, non-syndromic, autosomal dominant ichthyosis.
- It starts at or shortly after birth without a collodion membrane.
- Large, plate-like scale covers the whole body, including the flexures, and is most prominent on the limbs.
- Erythema is absent or mild.
- Palmoplantar keratoderma has accentuated creases.
- Some patients report reduced sweating when scaling is severe.

**History.** Traupe, Kolde and Happle first described the disorder in 1984 in one family: "Four patients, belonging to three consecutive generations of a family, were affected from birth." The paper also states: "We have found an autosomal dominant type of this disorder." (PMID:6499258, Clin Genet 1984). That same kindred (kindred 630) was later solved by exome sequencing (Boyden et al. 2020, PMID:32516568).

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0007812 "ichthyosis, lamellar, autosomal dominant" | Verified via OLS and the local `cache/mondo/terms.csv` |
| OMIM (phenotype) | 146750 | Given; KEGG, PanelApp and MedGen cite it |
| OMIM (gene) | 611765 ASPRV1 | HGNC REST |
| KEGG DISEASE | H02449 | Search result |
| MedGen | C1852191 (likely) | Search result; not confirmed |
| Orphanet | No dedicated ORPHA code found | ORPHA:313 is recessive lamellar ichthyosis, so do not use it for this entry. PhenoDis shows a blank Orphanet field for the dominant form. Needs a direct check on orpha.net. |
| ICD-10 | Q80.2 (lamellar ichthyosis) | Parent-level, not specific to this form; confirm before use |

**Synonyms.** Ichthyosis lamellar, autosomal dominant; ADLI; ASPRV1-related ichthyosis.

**Data basis.** All knowledge comes from aggregated, literature-level resources: case series of families. There are no EHR or registry data.

---

## 2. Etiology

- **Cause.** Heterozygous germline missense variants in ASPRV1, which cluster near the autocatalytic cleavage sites (PMID:32516568). Some are inherited and some arise de novo.
- **Genetic risk factors.** The pathogenic variants are the only established factor. Locus heterogeneity: NKPD1 p.Val458Phe causes an AD lamellar ichthyosis that looks similar (PMID:38642798).
- **Atopic eczema is a negative association.** Sandilands et al. 2012 report that "Mutations in the SASPase gene (ASPRV1) are not associated with atopic eczema or clinically dry skin" (PMID:22318384, title).
- **Environment.** No causal exposures. Warm, humid weather improves the scaling but does not clear it (Boyden 2020 full text). That is a modifier of severity, not a cause.
- **Protective factors and gene–environment interactions.** None reported.

---

## 3. Phenotypes

Source: Boyden et al. 2020 (PMID:32516568, full text). The series is 10 affected individuals from 4 kindreds, so the frequencies below are qualitative.

| Phenotype | Details | Suggested HPO lead (verify) |
|---|---|---|
| Lamellar (large plate-like) scaling, generalized | Starts at birth or in early infancy. Includes flexures; most prominent on arms and legs. Present in all patients. | Ichthyosis HP:0008064; lamellar ichthyosis term in HPO to be checked |
| No collodion membrane | Stated for the series. This distinguishes it from many recessive congenital ichthyoses (ARCI). | Record as an absent feature or in notes |
| Palmoplantar keratoderma | Accentuated palmar creases. Present in all patients and part of the defining description. | Palmoplantar keratoderma HP:0000982 |
| Mild or absent erythema | Characteristic | Erythroderma term only in negated form |
| Hypohidrosis | "Subjects report inability to perspire when scaling is severe." Some patients. | Hypohidrosis HP:0000966 |
| Pruritus | Moderate itch in some patients | Pruritus HP:0000989 |
| Pseudoainhum (constriction bands of digits) | Figure 2, proband 1099; one patient | Pseudoainhum term to be looked up |
| Seasonal variation | Better in warm weather | Notes only |

- **Histopathology:** acanthosis, compact orthohyperkeratosis, and a slightly expanded granular layer.
- **Patient biopsy (292-2):** strong filaggrin staining in the expanded granular layer.
- **Ultrastructure:** the 1984 kindred included ultrastructural studies. Komlosi 2024 says the NKPD1 ultrastructure differs clearly from that of ASPRV1-related ADLI. I could not obtain the detailed ASPRV1 EM findings.
- **Not described:** ectropion, eclabium, alopecia, nail changes, and other organs.
- **Course:** stable and lifelong.
- **Quality of life:** no instrument-based data (DLQI, EQ-5D) specific to this disorder exist.

---

## 4. Genetic and molecular information

**Gene and protein.**
- ASPRV1 is a retroviral-like aspartic protease expressed specifically in stratified epithelium.
- The full-length protein is 343 amino acids (37 kDa). It is processed to a 28 kDa pro-form (residues 85–343) and then, by auto-cleavage, to a 14 kDa active enzyme (residues 191–326).
- Discovery: Bernard et al. 2005 (PMID:16098038) — "We named this protein Skin ASpartic Protease (SASPase)." They also report: "SASPase was specifically expressed within the epidermis," with expression "restricted to the granular layers."

**Pathogenic variants in humans** (NM_152792; PMID:32516568)

| Variant | Kindred | Origin |
|---|---|---|
| c.932G>C p.(Arg311Pro) | 292 (5 affected) | Inherited; co-segregates in the extended family |
| c.595A>G p.(Lys199Glu) | 1055 (3 affected) | De novo in the proband's mother |
| c.940C>A p.(Pro314Thr) | 630 (the 1984 Traupe family) | Parental DNA unavailable |
| c.940C>A p.(Pro314Thr) | 1099 | De novo |
| p.(Arg208Met) | Single patient with a nonsyndromic epidermal differentiation disorder or ichthyosis | Wang 2026, JDDG (PMID:42338387). Abstract not available; cDNA, inheritance and phenotype need confirming. |

- **Variant classes:** all reported human variants are missense.
- **gnomAD:** the three Boyden variants are absent. Other changes at the same residues are present at low frequency: p.Arg311Cys at 0.0002 (0.002 in East Asians), p.Arg311His at 0.00004, and p.Val187Ile at 0.0004.
- **Constraint:** pLI = 0.01, so the gene tolerates loss of function. That argues against haploinsufficiency.
- **ClinVar and ClinGen:** no ClinGen gene-disease validity assertion was found. Run `just list-gene-validity` and check the `CGGV:` cache before recording any tier. PanelApp Australia rates ASPRV1 "high evidence" for monoallelic ADLI.

**Functional consequence.**
- All three Boyden mutants alter auto-cleavage. Each produces an aberrant ~20 kDa band in differentiated human keratinocytes, and each causes high-molecular-weight profilaggrin intermediates to accumulate.
- All three mutated residues cluster on one surface of the 14 kDa active enzyme.
- The authors propose a **dominant-negative mechanism, possibly with neomorphic effects**, rather than haploinsufficiency. That fits the pLI and the fact that knockout mice show no ichthyosis.
- Feng 2026 (PMID:42593882, crystal structures of ASPRV1-14) groups disease mutations into two routes. Verbatim: "analysis of disease-associated mutations indicates two main pathogenic mechanisms."
  - Disruption of the S2/S2′ substrate pocket (V243A).
  - Interference with self-cleavage maturation (I186T, K199E, R311C/P, P314T).
  - The same paper shows the enzyme moves "from a low-activity monomer at low ionic strength to a high-activity dimer at high ionic strength."

**Other categories.** No modifier genes, epigenetic findings or chromosomal abnormalities are reported.

---

## 5. Environmental information

- No toxins, lifestyle factors or infectious agents are implicated.
- Ambient temperature and humidity modulate how severe the scaling is (anecdotal, from Boyden 2020).

---

## 6. Mechanism and pathophysiology

**Ordered causal chain**

1. **Heterozygous ASPRV1 missense variant** (germline, inherited or de novo) changes a residue near the autocatalytic cleavage sites of the protease (PMID:32516568).
2. **This disrupts SASPase auto-processing.** Normally the 28 kDa pro-form self-cleaves into the active 14 kDa homodimer (PMID:16098038; PMID:32640672: "self-processing of SASP28 precursor causes autoactivation of the protease"). The mutants produce an abnormal ~20 kDa species instead.
   - *Inferred:* the mutant subunits then poison the wild-type enzyme by dimerizing with it (dominant negative), or gain an aberrant activity (neomorphic). This is proposed, not demonstrated.
3. **This impairs profilaggrin-to-filaggrin processing in the stratum granulosum.** SASPase cleaves the profilaggrin linker directly (Matsui 2011, PMID:21542132: "recombinant SASPase directly cleaved a linker peptide of recombinant profilaggrin").
   - Boyden mutants accumulate high-molecular-weight filaggrin.
   - Upstream regulation: the N-terminal domain of filaggrin-2 enhances SASPase autoactivation (PMID:32437351).
4. **This leads to abnormal terminal keratinocyte differentiation and cornification.** Seen as compact orthohyperkeratosis, an expanded granular layer, and acanthosis. The link from step 3 to this step is inferred from the histology together with the filaggrin data.
5. **This results in defective stratum corneum texture and hydration, and in retention hyperkeratosis.** SASPase knockout mice show a "thicker and less hydrated SC." Matsui 2011 states: "SASPase activity is indispensable for processing profilaggrin and maintaining the texture and hydration of the SC."
6. **The clinical result** is generalized lamellar scaling and palmoplantar keratoderma.
   - **Branch:** severe hyperkeratosis is followed by hypohidrosis, presumably through occlusion of sweat ducts (inferred), and in one patient by pseudoainhum.

**Caveat on the mechanism.** Loss of function alone does not reproduce the human disease. Knockout mice have dry skin and fine wrinkles but no lamellar ichthyosis (PMID:16837463, PMID:21542132), and the gene tolerates loss of function in humans. The dominant missense mechanism is therefore probably more than simple loss of activity. This would be a natural `HUMAN_MODEL_MISMATCH` discussion in the entry.

**Ontology leads (all to be verified)**
- **GO terms:**
  - aspartic-type endopeptidase activity (GO:0004190)
  - protein autoprocessing (GO:0016540)
  - keratinocyte differentiation (GO:0030216)
  - establishment of skin barrier (GO:0061436)
  - keratinization / cornification (GO:0031424 / GO:0070268)
  - epidermis development (GO:0008544)
- **CL terms:**
  - keratinocyte (CL:0000312)
  - granular-layer keratinocyte (look up)
  - corneocyte (look up)
- **Cellular location:** the protein localizes to the stratum granulosum (patient immunostaining) and keratohyalin/cytoplasm. GO cellular component terms still need to be looked up.

**Molecular profiling.** No transcriptomic, proteomic, metabolomic, single-cell or spatial data specific to this disease were found. No GEO datasets were found.

---

## 7. Anatomical structures

- **Organ:** skin only (integumentary system). No other organ involvement is reported.
- **Tissue and layers** (UBERON leads, to be verified):
  - epidermis (UBERON:0001003)
  - stratum granulosum (UBERON:0002069)
  - stratum corneum (UBERON:0002027)
  - palm and sole skin
  - flexural skin
- **Distribution:** generalized, symmetric and bilateral, with limb predominance.

---

## 8. Temporal development

- **Onset:** congenital or within the first months of life, without a collodion membrane.
- **Course:** chronic and lifelong, with no staging. It varies with season and is better in warm weather.
- **Remission:** no spontaneous remission is reported. Keratolytics gave near-complete clearing of non-palmoplantar scale in one mother and son pair.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006, verify). De novo variants occur (2 of 4 kindreds).
- **Penetrance:** appears complete in the families reported; formal data are lacking.
- **Expressivity:** variable, with some modulation by season.
- **Epidemiology:** prevalence is unknown. At least 5 human kindreds are published worldwide (4 in Boyden 2020 plus Wang 2026). Use `prevalence_class: NOT_YET_DOCUMENTED` or `CASES_IN_LITERATURE`.
- **Founder effects, populations and sex ratio:** none reported. Both sexes are affected.
- **Recurrent variant:** p.Pro314Thr appeared independently in two kindreds, one of them de novo, which suggests a mutational hotspot.

---

## 10. Diagnostics

- **Clinical diagnosis:** a non-syndromic congenital ichthyosis with lamellar scale, no collodion membrane, and palmoplantar keratoderma, segregating dominantly.
- **Histology:** compact orthohyperkeratosis, acanthosis, and a mildly expanded granular layer. These findings are not specific.
- **Genetic testing:** a multigene ichthyosis panel, or exome sequencing, including ASPRV1 and NKPD1. ASPRV1 is on PanelApp Australia's Ichthyosis and Porokeratosis panel and its Palmoplantar Keratoderma and Erythrokeratoderma panel.
- **Differential diagnosis:**
  - Recessive lamellar ichthyosis / ARCI (TGM1, ALOX12B, ALOXE3, NIPAL4, CYP4F22 and others): usually a collodion membrane at birth, recessive inheritance.
  - NKPD1-related ADLI (PMID:38642798): distinct ultrastructure and altered ceramide ratios.
  - Ichthyosis vulgaris (FLG): finer scale, with the flexures spared.
  - Epidermolytic ichthyosis (KRT1/KRT10): blistering and epidermolytic histology.
  - Keratinopathic and other autosomal dominant ichthyoses.
- **Screening:** none at population level. Cascade testing of relatives is the relevant form.

---

## 11. Outcome and prognosis

- Life expectancy is presumably normal. No mortality has been reported.
- Morbidity is cosmetic, plus pruritus, heat intolerance or hypohidrosis, and in one case pseudoainhum, which carries a risk of digital constriction.
- No prognostic factors or biomarkers are known.

---

## 12. Treatment

- **What has been used:** topical keratolytics (lactic acid, urea). Verbatim from the Boyden full text, the mother and son had "almost complete resolution of non-palmoplantar scale."
- **Suggested NCIT lead:** Pharmacotherapy (NCIT:C15986), with CHEBI agents lactic acid and urea (look these up).
- **General ichthyosis care** (not specific to this disease):
  - emollients
  - systemic retinoids for severe cases (not reported here)
  - managing heat intolerance
- **Experimental therapies:** none; no NCT trials.
- **Structural lead:** the crystal-structure work found that ASPRV1 is inhibited by indinavir but resists most HIV protease inhibitors (PMID:42593882). Indinavir also blocks autoactivation in vitro (PMID:16098038). This is relevant to the biology only and is not a therapy.

---

## 13. Prevention

- Genetic counseling: offspring of an affected person have a 50% risk. Recurrence risk is low after a de novo case, apart from germline mosaicism.
- Prenatal and preimplantation testing are possible once the familial variant is known.
- No primary prevention exists.

---

## 14. Other species and natural disease

- **Dog** (*Canis lupus familiaris*, NCBITaxon:9615; OMIA 002099-9615, "Ichthyosis, ASPRV1-related"):
  - **German Shepherd** (Bauer et al. 2017, PMID:28249031). A de novo heterozygous c.1052T>C p.(Leu351Pro) variant near an autoprocessing cleavage site, with altered filaggrin expression. Verbatim:
    - "the identified de novo variant is causative for the ichthyosis in the affected dog"
    - "ASPRV1 is thus a novel candidate gene for unexplained human forms of ichthyoses."
  - **Pembroke Welsh Corgi** (Kiener et al. 2024, PMID:38549226, Anim Genet 55:490–492). A heterozygous 2-bp deletion predicted to give p.(Leu199Argfs*342), an extended protein. The details come from OMIA; the paper has no abstract.
- **Comparative biology:**
  - These canine cases are dominant de novo heterozygous variants near the autoprocessing sites, which parallels the human mechanism.
  - SASPase evolved with terrestrial skin and is probably derived from a retroviral element (Matsui 2016, PMID:28484176).
  - Dolphins keep filaggrin but have lost caspase-14 (PMID:25739514), which is context only.
- **Zoonotic potential:** not applicable.

---

## 15. Model organisms

| Model | Phenotype | Fidelity to human ADLI |
|---|---|---|
| *Asprv1* (mSASP) knockout mouse (Matsui 2006, PMID:16837463) | "mSASP-deficient mice that at 5 weeks of age showed fine wrinkles that ran parallel on the lateral trunk"; no obvious differentiation defect | Low: no lamellar ichthyosis. `FAILS_TO_RECAPITULATE` or `PARTIALLY_RECAPITULATES` for the scaling. |
| SASPase-deficient hairless mouse (Matsui 2011, PMID:21542132) | Dry skin; thicker, less hydrated stratum corneum; aberrant profilaggrin accumulates; filaggrin markedly decreased | Moderate for the filaggrin-processing node. Loss of function rather than the dominant missense mechanism (a typed divergence). |
| *Filaggrin*/SASPase-deficient mice, corneocyte texture (Thyssen 2020, PMID:31479664) | Changes in corneocyte surface texture and stiffness | Mechanistic support |
| Differentiated human keratinocytes expressing HA-tagged mutants (Boyden 2020) | Aberrant ~20 kDa band; high-molecular-weight filaggrin accumulates | `IN_VITRO`; recapitulates the molecular nodes |
| Spontaneous dog models (above) | Clinical ichthyosis | Natural `MODEL_ORGANISM` model with high fidelity at the variant level |

No knock-in mouse carrying a human missense variant exists. That is a gap.

---

## Key references

| PMID | Citation | Use |
|---|---|---|
| 32516568 | Boyden LM … Choate KA. *Am J Hum Genet* 2020;107:158–163 (PMC7332602) | Gene discovery; variants; phenotype; mechanism |
| 6499258 | Traupe H, Kolde G, Happle R. *Clin Genet* 1984 | First description |
| 16098038 | Bernard D et al. *J Invest Dermatol* 2005 | Identification of SASPase; expression in the granular layer |
| 16837463 | Matsui T et al. *J Biol Chem* 2006 | Mouse knockout; wrinkles |
| 21542132 | Matsui T et al. *EMBO Mol Med* 2011 | Profilaggrin processing; stratum corneum hydration |
| 22318384 | Sandilands A et al. *J Invest Dermatol* 2012 | No association with atopic eczema (negative evidence) |
| 32640672 | Golda M et al. *Biomolecules* 2020 | Enzymology; autoactivation |
| 32437351 | Donovan M et al. *PLoS One* 2020 | Filaggrin-2 regulates SASPase autoactivation |
| 39098535 | Mótyán JA et al. *J Biol Chem* 2024 | Review |
| 42593882 | Feng X et al. *Acta Biochim Biophys Sin* 2026 | Crystal structures; two pathogenic mechanisms |
| 42338387 | Wang W et al. *JDDG* 2026 | p.R208M patient (needs full text) |
| 38642798 | Komlosi K et al. *J Invest Dermatol* 2024 | NKPD1 ADLI (locus heterogeneity) |
| 39001722 | Traupe H. *J Invest Dermatol* 2024 | Editorial on ADLI (abstract not obtained) |
| 28249031 | Bauer A et al. *PLoS Genet* 2017 | German Shepherd model |
| 38549226 | Kiener S et al. *Anim Genet* 2024 | Pembroke Welsh Corgi model |

**Gaps and things to check before curating**
- An Orphanet code specific to this disorder.
- A ClinGen gene-disease validity classification for ASPRV1.
- Full text of Wang 2026 (variant details).
- Detailed electron-microscopy findings for the ASPRV1 form.
- No GeneReviews chapter is expected for this disorder; confirm with `just check-genereviews`.
- No prevalence data exist.

## Sources
- [Boyden et al. 2020, PMC7332602](https://pmc.ncbi.nlm.nih.gov/articles/PMC7332602)
- [PubMed 32516568](https://view.ncbi.nlm.nih.gov/pubmed/32516568/)
- [PanelApp Australia – ASPRV1](https://panelapp-aus.org/panels/124/gene/ASPRV1/)
- [KEGG H02449](https://www.kegg.jp/entry/H02449)
- [MedGen](https://ncbi.nlm.nih.gov/medgen/1852191)
- [PhenoDis ADLI entry](https://iegext02.helmholtz-munich.de/phenodis/disease/show/9197)
- [Bauer et al. 2017, PMC5352138](https://pmc.ncbi.nlm.nih.gov/articles/PMC5352138)
- [Kiener et al. 2024, PubMed 38549226](https://pubmed.ncbi.nlm.nih.gov/38549226/)
- [OMIA 002099-9615](https://omia.org/OMIA002099/9615/)
- [Matsui 2011 reference (JCI scholar link)](https://jci.org/references/scholar/29864/B99)
- [HGNC REST ASPRV1](https://rest.genenames.org/fetch/symbol/ASPRV1)
- [EBI OLS MONDO:0007812](https://www.ebi.ac.uk/ols4/api/search?q=MONDO:0007812&ontology=mondo&exact=true)
- NCBI E-utilities abstracts for PMIDs 42338387, 39098535, 38642798, 39001722, 38549226, 42593882, 21542132, 22318384, 16098038, 16837463, 6499258, 32437351, 28249031 and 32640672.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001003` (1 mention) - the report calls it "epidermis"; UBERON calls it **skin epidermis**, and lists "epidermis" among its other names
- `UBERON:0002027` (1 mention) - the report calls it "stratum corneum"; UBERON calls it **stratum corneum of epidermis**, and lists "stratum corneum" among its other names
- `NCIT:C15986` (1 mention) - the report calls it "Suggested NCIT lead:** Pharmacotherapy"; NCIT calls it **Pharmacotherapy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

19 of 21 terms resolved to a current term; the rest could not be looked up either way.