---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-13T13:37:24.950303'
end_time: '2026-10-13T13:40:26.926623'
duration_seconds: 181.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 18
  mondo_id: MONDO:0013475
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
  web_search_requests: 3
  num_turns: 23
  total_cost_usd: 2.0354637
  session_id: f6391fec-15b3-4e54-b295-b55455157289
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:12639993
  relevance_assessed: 12
  on_topic: 4
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 28
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.034
  labels_checked: 4
  labels_matching: 2
  labels_variant: 2
  unresolved_terms:
  - HP:0001715
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 18
- **MONDO ID:** MONDO:0013475 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 18** covering all of the
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

Checking PubMed IDs for the main PLN–HCM papers, then writing the report.

# Hypertrophic Cardiomyopathy 18 (CMH18; PLN-related HCM): Research Report

*Prepared 2026-10-13 for the dismech entry `kb/disorders/Hypertrophic_Cardiomyopathy_18.yaml`.*

**How the quotes were checked.** Quotes marked **[cache]** were read word for word from files already in `references_cache/`: PMID:21167350, PMID:12610310, PMID:16432188, and the ClinGen `CGGV:` record. Quotes marked **[web]** came from PubMed abstracts through a summarising fetch tool. That tool limits quote length and is not guaranteed to be verbatim. Before using any **[web]** quote as a snippet, fetch the reference with `just fetch-reference PMID:…` and check it with `just count-verified-snippets`.

**How the ontology IDs were checked.** Only three identifiers were read from a source in this session:
- `MONDO:0013475`, from the existing draft entry
- `HGNC:9080` and `MONDO:0000591`, from the cached ClinGen row

Every other CURIE below is a **candidate written from memory**. Look each one up before binding it, as the repo's term rule requires.

---

## Executive summary

- **What it is.** CMH18 is the OMIM-numbered form of familial hypertrophic cardiomyopathy caused by variants in **PLN**. PLN encodes phospholamban, a 52-amino-acid protein that inhibits the cardiac SR Ca²⁺ pump SERCA2a.
- **How much evidence there is.** Very little. HCM-specific PLN evidence comes from a handful of probands:
  - the truncating variant **p.Leu39Ter (L39X / L39stop)**, seen as a heterozygote in about three families;
  - two or three **promoter variants**: −77A>G, −42C>G, and further rare variants in the Mayo cohort.
- **How ClinGen handles it.** ClinGen does **not** treat CMH18 as a separate disease. Its HCM Gene Curation Expert Panel merged CMH18 (MIM 613874) with dilated cardiomyopathy 1P (MIM 609909) into one entity, **PLN / intrinsic cardiomyopathy (MONDO:0000591), autosomal dominant, rated Definitive** (curated 2017, recurated 2021-02-12).
- **Mechanism.** The disease follows from abnormal SERCA2a regulation and abnormal Ca²⁺ cycling in cardiomyocytes. L39X behaves as a dose-dependent null allele:
  - **heterozygotes** develop hypertrophy with preserved systolic function;
  - **homozygotes** develop lethal dilated cardiomyopathy (DCM).
- **A naming trap to avoid.** The well-known **PLN p.Arg14del** founder variant (Netherlands, Greece) and **p.Arg9Cys** cause mainly DCM and arrhythmogenic cardiomyopathy, not CMH18. Cite them only as context for the shared mechanism. Do not use them as evidence for HCM phenotypes.

---

## 1. Disease information

**Overview.** Landstrom et al. (2011) frame HCM as "unexplained cardiac hypertrophy" affecting ~1 in 500 people [cache, PMID:21167350]. CMH18 is the subset attributed to PLN, usually found in families whose sarcomere-gene panel came back negative.

**Identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0013475 "hypertrophic cardiomyopathy 18" | from draft entry; confirm label with `just validate-terms` |
| OMIM (phenotype) | 613874 | stated in ClinGen record [cache] |
| OMIM (gene PLN) | 172405 | web search (OMIM mirror) |
| HGNC | PLN, HGNC:9080 (write as `hgnc:9080`) | ClinGen row [cache] |
| ClinGen lumped entity | MONDO:0000591 intrinsic cardiomyopathy | [cache] |
| Orphanet | No CMH18-specific ORPHA code found. Orphanet's familial isolated HCM entry is a candidate parent; check `references_cache/ORPHA_*` | not verified |
| ICD-10-CM | I42.1 / I42.2 (obstructive / other HCM) | standard; not specific to CMH18 |

**Synonyms.** CMH18; cardiomyopathy, hypertrophic, 18; PLN-related HCM; familial hypertrophic cardiomyopathy 18.

**Data provenance.** Everything here comes from aggregated, disease-level resources (OMIM, ClinGen) and from family and case reports. There is no EHR or registry dataset specific to CMH18.

## 2. Etiology

**Primary cause.** Germline heterozygous PLN variants: truncating (L39X) and promoter (regulatory).

**Key evidence**

- **Chiu et al. 2007** (PMID:17655857) screened 252 unrelated Australian familial HCM probands across 7 Ca²⁺-handling genes. They found a novel PLN Leu39Ter and concluded that "mutations in Ca(2+) handling genes are an infrequent but important cause of FHC" [web].
- **Landstrom et al. 2011** (PMID:21167350) [cache]:
  - "one L39X nonsense mutation was identified in 1 of 1,064 HCM proband cases with a family history of HCM, previously found to be negative for the current HCM genetic test panel."
  - "This mutation cosegregated with incidence of HCM in a multigenerational family."
  - "we identified an overall yield of PLN-HCM mutations of 0.65%"
- **Minamisawa et al. 2003** (PMID:12705874) found a heterozygous promoter variant −77A>G in 1 of 87 HCM patients. It was absent from 296 controls, and "the mutation, -77A-->G, increased the phospholamban promoter activity" in neonatal rat cardiomyocytes [web].
- **Medin et al. 2007** (PMID:16829191) found a −42C>G promoter variant in a Spanish HCM patient with reduced penetrance. This is summarised in Landstrom 2011 [cache]; the Medin abstract itself was not read.

**Risk factors.**
- **Genetic:** carrying a PLN variant; L39X dosage, since homozygosity shifts the phenotype to DCM.
- **Environmental:** none documented for CMH18.
- **Protective factors and gene–environment interactions:** none reported.
- **Common PLN promoter variant −36A>C:** Landstrom saw no excess in HCM probands (8.3% vs 7.5% in Caucasian controls) [cache]. It should not be recorded as an HCM risk factor.

## 3. Phenotypes

Data are sparse. Each item below rests on single probands or small pedigrees. HPO IDs are candidates to verify.

| Phenotype | Evidence | Onset | Candidate HPO |
|---|---|---|---|
| Left ventricular / septal hypertrophy (the defining feature), septal and apical | Landstrom proband: MLVWT 24 mm, "septal and apical HCM" [cache]; Haghighi 2003 heterozygotes "exhibited hypertrophy without diminished contractile performance" [web] | Adult (diagnosed at 51, 56, 61 and 67 in the reported probands); one 3-year-old carrier was affected | HP:0001639 Hypertrophic cardiomyopathy; HP:0001712 Left ventricular hypertrophy |
| Preserved ejection fraction / no LVOT obstruction (in the Landstrom proband) | "normal ejection fraction of 68%… without resting or valsalva-induced left ventricular outflow tract obstruction" [cache] | — | — (a negative finding; use as a note) |
| Atrial fibrillation / flutter | Landstrom: "the identification of this arrhythmia in all four PLN-HCM mutation cases described to date is notable" (vs 21% in the whole cohort) [cache] | Adult | HP:0005110 Atrial fibrillation; HP:0004749 Atrial flutter |
| Palpitations, presyncope, dyspnea, chest pain | Landstrom proband [cache] | Adult | HP:0001962; HP:0100660 (dyskinesia? — verify; presyncope term to look up); HP:0002094 Dyspnea; HP:0100749 Chest pain |
| Non-sustained ventricular tachycardia, conduction block; ICD implanted | Landstrom proband [cache] | Adult | HP:0004756 Ventricular tachycardia (verify the NSVT term); HP:0011675 Arrhythmia |
| Left atrial enlargement, mild mitral regurgitation | Landstrom proband [cache] | Adult | HP:0031295 Left atrial enlargement (verify); HP:0001653 Mitral regurgitation |
| Ventricular pre-excitation (WPW) | Landstrom proband; PRKAG2, GLA and LAMP2 all negative [cache] | Adult | HP:0001715? (verify; Wolff-Parkinson-White term) |
| Progression to DCM / heart failure (homozygotes; possibly some heterozygotes) | Homozygous L39X: DCM, transplant "at ages 16 and 27" [web, PMID:12639993]; ClinGen: "a progressive cardiomyopathy beginning with hypertrophic and leading to dilated has been observed in a proband" [cache] | Adolescent to young adult (homozygotes) | HP:0001644 Dilated cardiomyopathy; HP:0001635 Congestive heart failure |

No quality-of-life data exist for CMH18. General HCM instruments (KCCQ, NYHA class) apply.

## 4. Genetic and molecular information

**Gene.** PLN (6q22.31) has a single coding exon and encodes a 52-amino-acid SR transmembrane protein. ClinGen [cache]:
- "PLN is encoded by one exon … many of the mutations (even LOF) result in a protein product."
- "The monomeric form is thought to inhibit SERCA2 activity. PLN-mediated SERCA2 inhibition is released upon phosphorylation of monomeric PLN by either PKA or CAMKII."

**Variants attributed to HCM**

| Variant | Type | Functional effect | Source |
|---|---|---|---|
| c.116T>G p.Leu39Ter (L39X) | Nonsense | Null: no SERCA inhibition; protein unstable or mislocalised; "no detectable PLN protein" in a homozygous explanted heart [web] | PMID:12639993, PMID:17655857, PMID:21167350 |
| −77A>G (promoter) | Regulatory | Higher promoter activity, i.e. more PLN, i.e. more SERCA inhibition (inferred) | PMID:12705874 |
| −42C>G (promoter) | Regulatory | Reduced penetrance; function not established here | PMID:16829191 |
| C>T −235, A>C −198, A>G −120, T>C −114, G>T −47 (promoter) | Regulatory, rare | Unknown; absent from 600 control alleles | PMID:21167350 [cache] |

Landstrom also reports that "We did not observe any PLN coding sequence genetic variation in 600 reference alleles" [cache]. Check gnomAD for L39X before writing any allele frequency.

**Mechanism by variant.** L39X is a loss-of-function allele with a dosage effect (ClinGen calls it "semidominance") [cache]. The promoter variants plausibly cause gain of expression, but this is shown in vitro only.

**Other points**
- Germline origin.
- No modifier genes, epigenetic data or chromosomal abnormalities have been reported for CMH18.
- **ClinGen validity:** Definitive, AD, for *intrinsic cardiomyopathy* (MONDO:0000591). That record's MONDO is not CMH18's `disease_term`. Under the repo's rules it is a "broader ClinGen lumping": cite it as evidence, but do not record it as a `gene_disease_validity` assertion for MONDO:0013475 unless an exactMatch mapping justifies it. The ARVC/Moderate record is a separate disease.

## 5. Environmental information

None documented. No infectious agent is involved.

## 6. Mechanism / pathophysiology

**Causal chain (L39X arm; steps marked *inferred* are not directly shown in CMH18 patients)**

1. **Heterozygous PLN L39X** produces truncated phospholamban that is unstable or mislocalised. Cell work shows "no PLN inhibition of SR Ca(2+)-ATPase" [web, PMID:12639993]. The result is **reduced functional PLN dosage**.
2. Less PLN means **SERCA2a is released from inhibition**: faster SR Ca²⁺ reuptake and altered Ca²⁺ transients. The mouse evidence is Luo 1994: PLN-null mice "exhibited enhanced myocardial performance" and PLN "acts as a critical repressor of basal myocardial contractility" [web, PMID:8062415].
3. Chronically altered Ca²⁺ cycling then leads to **Ca²⁺-dependent hypertrophic signalling** in cardiomyocytes, with left ventricular hypertrophy and preserved contractility in heterozygotes. *Inferred*: no study of a CMH18 patient has shown the specific signalling pathway (calcineurin–NFAT or CaMKII).
4. **Branch A (heterozygote).** HCM with atrial fibrillation and ventricular ectopy or NSVT. The association with AF is notable but unexplained: "further studies are required to elucidate any potential association between PLN function and atrial fibrillation" [cache].
5. **Branch B (homozygote, total loss).** Lethal DCM and heart failure, needing transplant in adolescence or young adulthood. Human PLN loss is therefore harmful, unlike in mice. This is a `HUMAN_MODEL_MISMATCH` candidate.
6. **ClinGen synthesis** [cache]: "the overall disease mechanism for PLN associated cardiomyopathy is dysregulation of SERCA2 function, Ca2+ handling, and disrupted relaxation and contraction of the heart."

**Promoter arm.** The −77A>G variant increases promoter activity, which should mean more PLN and **more** SERCA2a inhibition. That is the opposite direction to L39X. Why both directions would end in HCM is unresolved; record it as a knowledge gap.

**Contrast, for context only.** R9C traps PKA and blocks PLN phosphorylation [cache, PMID:12610310]. R14del "superinhibits" SERCA [cache, PMID:16432188]. Both cause DCM.

**Ontology suggestions (verify)**

| Kind | Candidates |
|---|---|
| GO | regulation of calcium ion transport into the sarcoplasmic reticulum; negative regulation of calcium ion-transporting ATPase activity (PLN's normal function); cardiac muscle hypertrophy (GO:0003300); regulation of cardiac muscle contraction by calcium ion signaling; release of sequestered calcium ion into cytosol by sarcoplasmic reticulum |
| GO cellular component | sarcoplasmic reticulum membrane (GO:0033017) |
| CL | cardiac muscle cell (CL:0000746); ventricular cardiac muscle cell; atrial cardiac muscle cell (for AF) |
| CHEBI | calcium(2+) (CHEBI:29108) |

There are no omics, single-cell or CRISPR-screen data specific to CMH18.

## 7. Anatomical structures

- **Organ and system:** heart; cardiovascular system.
- **Sites:** interventricular septum, LV apex, left atrium.
- **Tissue and cell:** myocardium; ventricular and atrial cardiomyocytes.
- **Subcellular:** sarcoplasmic reticulum membrane.
- **Laterality:** left-sided predominance.
- **Candidate UBERON terms:** heart (UBERON:0000948), interventricular septum (UBERON:0002094), left cardiac atrium (UBERON:0002079), myocardium (UBERON:0002349).

## 8. Temporal development

- **Onset:** typically adult, diagnosed at 51–67 in the reported probands. One heterozygous child was phenotype-positive at 3 years [cache]. Onset is insidious.
- **Course:** chronic and lifelong. Progression to DCM has been seen in homozygotes, and ClinGen notes a hypertrophic-to-dilated course [cache].
- **Penetrance:** incomplete. A 38-year-old carrier daughter was unaffected [cache].
- **Staging:** no CMH18-specific staging exists.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant with incomplete penetrance. Recessive or semidominant dosage applies for L39X homozygotes [cache: "autosomal recessive inheritance has been noted and appears to follow a dosage effect or semidominance"]. Candidate HPO terms: HP:0000006 Autosomal dominant inheritance; HP:0003829 Typified by incomplete penetrance.
- **Frequency:** PLN accounts for ~0.65% of panel-negative HCM probands, counting promoter variants, and 0.13% for coding L39X alone [cache].
- **Prevalence:** no population figure exists for CMH18. Background HCM prevalence is about 1/500.
- **Populations:** probands have been reported as Caucasian North American, Australian, Japanese, Spanish and Greek (the L39X families in Haghighi 2003).
- **Not reported:** founder effect, sex ratio, anticipation, mosaicism.

## 10. Diagnostics

- **Imaging:** echocardiography and CMR showing maximal LV wall thickness of at least 13–15 mm without another cause.
- **ECG:** AF, pre-excitation, conduction block.
- **Monitoring:** ambulatory ECG for NSVT.
- **Genetic testing:** a multigene cardiomyopathy panel that includes PLN. Landstrom argues PLN's small size (two amplicons) and very low background variation make it easy to add to panels [cache]. Promoter coverage matters, because several HCM-linked variants are regulatory.
- **Differential diagnosis:** sarcomeric HCM; phenocopies such as PRKAG2 (which causes WPW), Fabry (GLA), Danon (LAMP2), and amyloid; athlete's heart; hypertensive LVH.
- **Cascade screening:** first-degree relatives, following the 2024 AHA/ACC HCM guideline (PMID:38718139 / 38727647).
- **Candidate NCIT diagnostic actions:** echocardiography, electrocardiography, genetic testing.

## 11. Outcome and prognosis

There are no survival data specific to CMH18.
- **Heterozygotes:** HCM with arrhythmia burden; ICD implanted in the Mayo proband.
- **Homozygotes:** end-stage DCM requiring transplant at 16 and 27.

General HCM prognosis and sudden-death risk models apply (PMID:40088231 validates the guideline's SCD risk recommendations).

## 12. Treatment

There is no PLN-specific therapy. Treatment follows general HCM management (2024 AHA/ACC guideline, PMID:38718139).

| Treatment | Notes | Candidate NCIT |
|---|---|---|
| β-blockers, non-dihydropyridine CCB, sotalol/amiodarone | The proband was treated with atenolol, amiodarone, sotalol and candesartan [cache] | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` |
| Mavacamten (cardiac myosin inhibitor) | For obstructive HCM (EXPLORER-HCM, PMID:32871100). Its relevance to PLN-HCM without obstruction is unproven | Pharmacotherapy |
| ICD implantation | For NSVT/SCD risk; implanted in the Mayo proband | Surgical Procedure + device qualifier |
| AF anticoagulation / ablation | AF is common in PLN-HCM | — |
| Heart transplantation | Homozygous L39X DCM | NCIT:C15289 Organ Transplantation |

**Experimental.** PLN-targeted approaches have been explored mainly for R14del DCM: antisense oligonucleotides, AAV-delivered inhibitory PLN, and gene editing. No trials target CMH18.

## 13. Prevention

- No primary prevention.
- Secondary: cascade genetic and clinical screening of relatives, with periodic echo and ECG for carriers given incomplete and variable-age penetrance.
- Genetic counselling covering homozygosity risk (DCM) in consanguineous or carrier-by-carrier unions.
- Tertiary: SCD risk stratification and AF management.

## 14. Other species

No naturally occurring PLN-HCM in animals was found (OMIA not searched in depth). PLN is highly conserved across vertebrates.

## 15. Model organisms

| Model | Relevance | Fidelity / limitations |
|---|---|---|
| Pln-knockout mouse (Luo 1994, PMID:8062415) | Hypercontractile, faster relaxation, no lethal DCM | **Fails to recapitulate** the human null phenotype (human homozygous L39X causes DCM). This is the explicit "critical difference between mouse and human" (PMID:12639993 title) |
| Transgenic PLN-R9C mouse (PMID:12610310) | DCM with premature death | Different variant and phenotype (DCM) |
| Transgenic PLN-R14del mouse (PMID:16432188) | DCM with premature death | Different variant and phenotype |
| HEK-293 co-expression (L39X; R14del) | In vitro SERCA inhibition assays | No cardiomyocyte context |
| Neonatal rat cardiomyocyte promoter-reporter (−77A>G; PMID:12705874) | Promoter activity | Reporter assay only |

There is no L39X-heterozygous animal or iPSC-cardiomyocyte HCM model. That is an open knowledge gap.

---

## Curation notes for the dismech entry

1. **Lump/split.** ClinGen merged CMH18 into PLN intrinsic cardiomyopathy. Keep CMH18 as a `DISEASE` entry, since the MONDO term exists, but quote the ClinGen lumping paragraph and note the overlap with DCM1P.
2. **Evidence already cached:** PMID:21167350 (full text), PMID:12610310, PMID:16432188, and the CGGV PLN records. **To fetch:** PMID:12639993, 17655857, 12705874, 16829191, 8062415.
3. **Suggested discussion items:**
   - a `HUMAN_MODEL_MISMATCH` for the mouse vs human PLN null;
   - a `KNOWLEDGE_GAP` on why opposite directions of PLN dosage (L39X null vs promoter up-regulation) would both cause HCM;
   - a `KNOWLEDGE_GAP` on the AF association.

## Sources

- [Haghighi 2003 JCI, PMC153772](https://pmc.ncbi.nlm.nih.gov/articles/PMC153772) (PMID:12639993)
- [JCI article 17892](https://www.jci.org/articles/view/17892/cite)
- [Chiu 2007 (PubAnnotation PMID:17655857)](https://pubannotation.org/docs/sourcedb/PubMed/sourceid/17655857)
- [Minamisawa 2003 (Scinapse)](https://scinapse.io/papers/2127817270) (PMID:12705874)
- [OMIM PLN 172405 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/172405)
- [Polish HCM PLN screening (Polish Heart Journal)](https://journals.viamedica.pl/polish_heart_journal/article/download/79413/61202)
- [NCBI E-utilities PubMed records](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=12639993,17655857)
- [ClinGen PLN / intrinsic cardiomyopathy](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_f49f65fb-a2df-4e86-9a89-da2325b207c8-2021-02-12T170000.000Z)
- Local cache: `references_cache/PMID_21167350.md`, `PMID_12610310.md`, `PMID_16432188.md`, and the CGGV PLN records

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:12639993`: "critical difference between mouse and human"
  - closest text in source: "In this study, the surprising difference between human and mouse PLN-null cardiac phenotypes emphasizes the need to better understand inherent differences in cardiac physiology and Ca2+-cycling mechanisms between mice and humans (31)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001715` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0000591` (4 mentions) - the report calls it "intrinsic cardiomyopathy", "ClinGen validity:** Definitive, AD, for *intrinsic cardiomyopathy"; MONDO calls it **intrinsic cardiomyopathy**
- `UBERON:0000948` (1 mention) - the report calls it "Candidate UBERON terms:** heart"; UBERON calls it **heart**, and lists "chambered heart" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0000591` - called "intrinsic cardiomyopathy", "ClinGen validity:** Definitive, AD, for *intrinsic cardiomyopathy"