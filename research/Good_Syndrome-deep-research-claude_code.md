---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T02:42:11.412599'
end_time: '2026-09-04T02:46:16.472081'
duration_seconds: 245.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Good Syndrome
  mondo_id: ''
  category: Complex
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 24
  total_cost_usd: 1.2962382000000003
  session_id: fab9582c-86c5-587f-8c13-07e30530b023
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 35
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC8185358
  relevance_assessed: 28
  on_topic: 24
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  unresolvable_prefixes:
  - ORPHA
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Good Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Good Syndrome** covering all of the
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

I'll research Good Syndrome (thymoma with immunodeficiency) now using web search and fetch tools.

I now have comprehensive data. Let me do a couple more targeted searches for model organisms/other species and prevention/screening aspects to round out the report.

# Good Syndrome (Thymoma with Immunodeficiency): Comprehensive Research Report

## 1. Disease Information

**Overview.** Good syndrome (GS) — also called thymoma-associated immunodeficiency or thymoma with immunodeficiency — is a rare, **adult-onset combined (B-cell and T-cell) primary immunodeficiency** occurring in patients with a thymoma. It was first described by Robert A. Good in 1954–1955 after he noted the co-occurrence of thymoma and hypogammaglobulinemia. GS is now recognized by the WHO/International Union of Immunological Societies (as of 1999) as a distinct primary immunodeficiency, separate from common variable immunodeficiency (CVID), despite frequent misdiagnosis as CVID ([PMC12647230](https://pmc.ncbi.nlm.nih.gov/articles/PMC12647230/); [PMC8019250](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8019250/)).

**Key identifiers:**
- **MONDO:** MONDO:0015696
- **Orphanet:** ORPHA169105 ([orpha.net](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=169105))
- **ICD-10:** D81.8 (Other combined immunodeficiencies)
- **ICD-11:** 4B40.2
- **OMIM:** No dedicated OMIM entry exists (it is an acquired, not classically Mendelian, disorder)
- **MeSH/synonyms:** Thymoma with immunodeficiency; thymoma-associated hypogammaglobulinemia; Good's syndrome; thymoma-associated combined immunodeficiency

**Nature of evidence base.** Because GS is exceedingly rare, the literature is dominated by **individual case reports and small retrospective/cross-sectional case series** pooled into systematic reviews, plus (as of 2023–2024) the first **prospective longitudinal cohort study**. There is essentially no large-scale EHR/claims-based epidemiology; most quantitative "prevalence" figures trace back to aggregated case counts rather than population registries.

---

## 2. Etiology

**Primary causal factor.** GS requires the essentially simultaneous presence of a **thymic epithelial tumor (thymoma)** and **acquired hypogammaglobulinemia with B-cell deficiency**. There is no known Mendelian/germline genetic cause; it is an **acquired (paraneoplastic-like) adult-onset immunodeficiency**, distinguishing it from inherited agammaglobulinemias (e.g., XLA) and most forms of CVID.

**Genetic risk factors (somatic, not germline):**
- Thymomas — especially WHO types A and AB, which predominate in GS — very frequently carry a recurrent **somatic missense mutation in GTF2I** (encoding transcription factor TFII-I), invariably p.L424H. This mutation is found in **82% of type A and 74% of type AB thymomas** in large series ([Nature Genetics, PMC7466068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/); [PMID:37671056](https://pubmed.ncbi.nlm.nih.gov/37671056/)).
- A mouse model of the human thymoma-associated GTF2I mutation shows that mutant TFII-I **impairs thymic epithelial progenitor differentiation**, producing aberrant thymic architecture and reduced thymopoietic activity, particularly of the medullary compartment ([PMID:36175547](https://pubmed.ncbi.nlm.nih.gov/36175547/); [Communications Biology, PMC9522929](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9522929/)) — a plausible mechanistic link between the thymoma's driver mutation and disrupted central tolerance/thymopoiesis.
- A dedicated somatic variant profiling study of a GS-associated thymoma has been published, though comprehensive GS-specific genomic characterization (as distinct from thymoma genomics generally) remains limited ([ScienceDirect S2772613424000039](https://www.sciencedirect.com/science/article/pii/S2772613424000039)).

**No established environmental/lifestyle causal or protective factors** have been identified — GS is not linked to toxin exposure, infection, diet, or lifestyle in the literature reviewed. No GWAS, susceptibility-loci, or gene–environment interaction data exist, consistent with its status as a rare acquired tumor-associated condition rather than a polygenic disease.

---

## 3. Phenotypes

### Immunological/laboratory phenotypes
| Feature | Frequency (pooled case series, n≈162) | Notes |
|---|---|---|
| Hypogammaglobulinemia | 100% | Median IgG ≈332 mg/dL (normal 700–1600 mg/dL); IgG can be as low as ~100 mg/dL |
| Low IgA | 86.0% | |
| Low IgM | 92.6% | (Some reports describe normal IgA/high IgM patterns in individual cases) |
| Absent/low peripheral B cells (CD19+) | 95.2% | Often near-complete absence; distinguishes GS from most CVID |
| Low CD4+ T-cell count | 71.3% | |
| Inverted CD4:CD8 ratio | 82.5% | e.g., ratio 0.45 vs. normal >1.1 in reported cases |
| Absent transitional B cells (CD38+CD24+) | Frequently reported | Suggests a B-cell precursor developmental defect |
| Loss of unswitched/CD21+ B cells, low CD19/CD20, near-absent surface IgD | Frequently reported | |
| Naïve CD8+CD45RA+ T-cell accumulation | Described as a hallmark finding | |

Source: [PMC8185358](https://pmc.ncbi.nlm.nih.gov/articles/PMC8185358/) (systematic review, 162 patients); [PMC5937423](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5937423/); case reports.

Suggested HPO terms: **HP:0002850** (Decreased circulating total IgG), **HP:0002850**-family Ig deficiency terms, **HP:0005404** (Hypogammaglobulinemia), **HP:0010976** (Abnormal B cell count / B lymphocytopenia), **HP:0005400** (CD4 lymphopenia), **HP:0002721** (Immunodeficiency), **HP:0002960** (Autoimmunity).

### Clinical phenotypes (symptoms/signs)
- **Recurrent sinopulmonary infections** (bronchitis, pneumonia, sinusitis) — the most common presentation (~67% of primary infection sites in the pooled series). Frequent pathogens: *Pseudomonas aeruginosa*, *Haemophilus influenzae*, *Streptococcus pneumoniae*.
- **Opportunistic/invasive infections despite sometimes-normal CD4 counts:** cytomegalovirus (CMV) disease/pneumonitis (~24.7% of infections), mucocutaneous and esophageal candidiasis (~16.7%), *Pneumocystis jirovecii* pneumonia, cryptococcosis and other invasive fungal disease ([PMC8636207](https://pmc.ncbi.nlm.nih.gov/articles/PMC8636207/)).
- **Gastrointestinal disease:** chronic diarrhea, malabsorption, and a distinctive **graft-versus-host disease (GVHD)-like colitis** with villous blunting and active chronic inflammation on histology, in the absence of any transplant — a signature and underrecognized GI phenotype of GS, distinguishing it pathologically from typical CVID enteropathy ([PMC12647230](https://pmc.ncbi.nlm.nih.gov/articles/PMC12647230/)).
- **Mucocutaneous disease:** oral **lichen planus** is a recurrent, relatively distinctive association (~22.9% of autoimmune manifestations) ([PMC11323965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11323965/)).
- **Hematologic autoimmunity: pure red cell aplasia (PRCA)** — the single most common autoimmune association, ~31–35% of GS patients.
- **Neuromuscular autoimmunity: myasthenia gravis** — second most common, ~15–28%, sometimes subclinical.
- Rarer: pure white cell aplasia, aplastic anemia/bone marrow failure, CD8+ T-cell large granular lymphocyte leukemia, systemic lupus erythematosus-like features, dementia (rare case reports).

### Phenotype characteristics
- **Onset:** adult, typically 40–70 years; mean/median age at diagnosis ~57–60 years (range 35–78 in cohort data).
- **Severity/progression:** immunodeficiency is typically **progressive** over years to decades — the 2024 McGill natural history study (37-year follow-up) documented gradual worsening of B- and T-cell compartments over time, independent of thymectomy ([JACI In Practice, PMID:38122866](https://pubmed.ncbi.nlm.nih.gov/38122866/)).
- **Diagnostic delay:** mean delay ~3.1 years (median 1 year, range 0–17 years) — reflecting the rarity and overlap with CVID.

### Quality of life
No disease-specific validated QoL instrument was identified in the literature; QoL impact is inferred from the burden of recurrent hospitalization for infection, chronic diarrhea, and autoimmune complications, but formal EQ-5D/SF-36 GS-specific data were not found in this search.

---

## 4. Genetic/Molecular Information

- **No causal germline gene.** GS is not a monogenic inherited immunodeficiency; there is no HGNC "disease gene" analogous to *BTK* in XLA.
- **Somatic driver in the associated thymoma:** **GTF2I** p.L424H missense mutation (HGNC:4661), present in the great majority of type A/AB thymomas that predominate in GS ([PMID:37671056](https://pubmed.ncbi.nlm.nih.gov/37671056/); [PMC7466068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/)). This is a **tumor-somatic**, not germline, variant.
- **Functional consequence:** TFII-I is a transcription factor regulating epithelial progenitor cell proliferation/differentiation in the thymus; the mutant form disrupts bipotent thymic epithelial progenitor differentiation and medullary thymic epithelial cell (mTEC) development in mouse models, plausibly impairing central tolerance mechanisms (including AIRE-dependent negative selection) ([PMID:36175547](https://pubmed.ncbi.nlm.nih.gov/36175547/)).
- **AIRE dysregulation:** Thymomas — including those in GS — have been reported to show **reduced AIRE (autoimmune regulator) gene expression**, contributing to defective central tolerance and paraneoplastic autoimmunity.
- **No confirmed modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities** specific to GS (as opposed to thymoma biology generally) were identified.
- **Allele frequency/population data:** not applicable — this is a somatic tumor mutation, not a population polymorphism; gnomAD/1000 Genomes data are not relevant.

---

## 5. Environmental Information

No dietary, occupational, toxin, or infectious *causal* exposures for GS itself were identified — the "trigger" is the thymoma, not an external agent. Infections in this section are better understood as **consequences** (complications) of the immunodeficiency rather than causes; see Phenotypes and Diagnostics sections for the pathogen spectrum (CMV, *Pseudomonas*, *Candida*, *Pneumocystis jirovecii*).

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, with inference flagged)

1. A thymic epithelial neoplasm arises, in the great majority of GS cases a **WHO type A (lymphocyte-poor spindle cell, ~23.5%) or type AB (mixed spindle/lymphocyte-rich, ~50.0%) thymoma**, frequently driven by the somatic **GTF2I p.L424H** mutation → *this leads to* disruption of normal thymic epithelial architecture.
2. Mutant TFII-I impairs **bipotent thymic epithelial progenitor differentiation**, particularly of the medullary lineage → *this leads to* (inferred, extrapolated from mouse model, [PMID:36175547](https://pubmed.ncbi.nlm.nih.gov/36175547/)) reduced thymopoietic output and defective **AIRE-mediated central tolerance/negative selection**.
3. Disrupted thymic microenvironment and possible bone-marrow-stromal-derived cytokine dysregulation → *this leads to* (mechanism still incompletely established/hypothesized) **impaired B-cell precursor development**, evidenced by absence of transitional (CD38+CD24+) B cells and loss of unswitched B-cell subsets.
4. Progressive **peripheral B-cell depletion** (near-complete absence of CD19+ cells in >95% of cases) → *this leads to* failure of plasma-cell differentiation and **panhypogammaglobulinemia** (low IgG, IgA, IgM).
5. In parallel, thymic T cells are reported to exert an **inhibitory effect on B-cell-mediated immunoglobulin production**, and thymoma-associated Treg export defects further destabilize peripheral immune homeostasis → *this contributes to* both the humoral defect and to loss of self-tolerance.
6. Concurrently, thymopoietic disruption produces **CD4+ T-cell lymphopenia**, an **inverted CD4:CD8 ratio**, and **accumulation of naïve CD8+CD45RA+ T cells** (proposed hallmark of thymoma-related T-cell dysfunction) → *this leads to* impaired cell-mediated immunity.
7. The combined B- and T-cell defect → *results in* susceptibility to (a) encapsulated/sinopulmonary bacterial pathogens (humoral defect pathway) and (b) viral/fungal/opportunistic pathogens — CMV, *Candida*, *Pneumocystis jirovecii* (cellular defect pathway) — clinically manifesting as recurrent infection (in >90% of patients).
8. Loss of central and peripheral tolerance (from steps 2 and 5) → *branches into* a distinct autoimmune phenotype: **pure red cell aplasia** (autoantibody/T-cell mediated marrow suppression of erythroid precursors), **myasthenia gravis** (anti-acetylcholine-receptor autoimmunity), **GVHD-like colitis**, and **oral lichen planus** — occurring in ~51–76% of patients depending on the cohort.
9. Because the immune defect originates from **stem/progenitor-level or established peripheral lymphocyte depletion rather than from the tumor mass itself**, thymectomy removes the neoplasm but **does not reverse the hypogammaglobulinemia or B-cell aplasia** in most patients — the defect is durable/self-perpetuating once established (an important and repeatedly confirmed clinical-mechanistic observation, [PMC8185358](https://pmc.ncbi.nlm.nih.gov/articles/PMC8185358/)).

**Overall causal status:** The Frontiers 2021 review explicitly states the pathophysiology "**remains unclear**," though it proposes the thymoma "disrupts the balance between host-defense and self-tolerance" ([PMC8185358](https://pmc.ncbi.nlm.nih.gov/articles/PMC8185358/)); another review states "many different theories were proposed on the pathogenesis of Good's syndrome but so far none has gained acceptance, making this syndrome still a mystery." **Much of the mechanistic chain above (steps 2–5) is therefore inferential/hypothesis-level**, built from a combination of a small number of tissue studies (e.g., B-cell depletion demonstrated directly *within thymoma tissue* — [Discover Oncology 2024](https://link.springer.com/article/10.1007/s12672-024-01450-x), showing complete B-cell absence in thymoma tissue of 4/5 GS patients) and mouse GTF2I models, rather than a fully demonstrated human causal pathway.

**Molecular pathways/GO terms suggested:**
- GO:0033077 T cell differentiation in thymus
- GO:0002519 natural killer cell tolerance induction / GO:0002377 immunoglobulin production
- GO:0030217 T cell differentiation
- GO:0042475 odontogenesis (n/a) — not relevant; instead: GO:0048538 thymus development
- GO:0002250 adaptive immune response

**Cell types (CL terms):**
- CL:0000236 B cell (depleted)
- CL:0000899 Th cell / CL:0000624 CD4-positive, alpha-beta T cell (lymphopenic)
- CL:0000625 CD8-positive, alpha-beta T cell (naïve accumulation)
- CL:0002293 epithelial cell of thymus / thymic medullary epithelial cell
- CL:0000980 plasmablast / CL:0000786 plasma cell (deficient)

**Advanced/omics data:** Single studies exist profiling "in-depth blood immune profiling of Good syndrome patients" ([PMC10684950](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10684950/)) and immunological signature studies of thymic epithelial tumor/GS patients (Frontiers 2022), but no large-scale transcriptomic (GEO), proteomic, or single-cell atlas specific to GS was identified — this remains a substantial evidence gap.

---

## 7. Anatomical Structures Affected

- **Primary organ:** Thymus (anterior mediastinum) — site of the neoplasm (UBERON:0002370 thymus).
- **Secondary/systemic involvement:**
  - Bone marrow (erythroid aplasia, occasional pancytopenia) — UBERON:0002371
  - Lungs/sinopulmonary tract (recurrent infection, bronchiectasis) — UBERON:0002048
  - Gastrointestinal tract, especially small intestine/colon (GVHD-like colitis, villous atrophy) — UBERON:0000160 (intestine)
  - Oral mucosa (lichen planus) — UBERON:0003729
  - Neuromuscular junction (myasthenia gravis) — UBERON:0000151
  - Skin/soft tissue (infections, ~18% of infection sites)
  - CNS (rare invasive infection, ~8% of infection sites)
- **Body systems:** immune system, hematologic system, respiratory system, gastrointestinal system, neuromuscular system.
- **Cellular level:** peripheral B lymphocytes and their bone-marrow/thymic precursors; CD4+ and CD8+ T lymphocyte compartments; thymic epithelial cells (neoplastic).
- **Subcellular:** not specifically characterized beyond transcriptional dysregulation (nucleus, via GTF2I/TFII-I).
- **Laterality:** thymoma is typically a solitary anterior mediastinal mass; no laterality preference reported.

---

## 8. Temporal Development

- **Onset:** adult-onset, typically **40–70 years** (mean/median ~57–60 years); a large McGill cohort recorded median age at thymoma diagnosis of 57.5 years (range 35–78). GS does not occur in childhood, unlike many primary immunodeficiencies and unlike a subset of CVID.
- **Onset pattern:** insidious — recurrent infections often precede or coincide with thymoma detection; diagnosis is frequently delayed (mean 3.1 years, median 1 year, up to 17 years).
- **Progression:** The 2024 prospective natural history study (McGill, 8 patients, up to 37 years follow-up) is the first to formally characterize GS as a **"progressive adult combined immunodeficiency"** — B- and T-cell compartments continue to decline over years/decades even after thymectomy ([PMID:38122866](https://pubmed.ncbi.nlm.nih.gov/38122866/)).
- **Disease course pattern:** chronic, generally progressive, punctuated by recurrent infectious episodes and, in many patients, later-onset autoimmune complications (autoimmunity often follows the immunodeficiency temporally).
- **Duration:** lifelong once established; no reported spontaneous remission of the immune defect.
- **Thymoma staging at diagnosis:** ~68.2% present at localized (Masaoka stage I–II) disease; ~51.4% are disease-free from the tumor at last follow-up versus ~48.6% with active thymoma disease, and active thymoma is itself an independent poor-prognostic factor (OR 4.157) ([PMC8185358](https://pmc.ncbi.nlm.nih.gov/articles/PMC8185358/)).

---

## 9. Inheritance and Population

- **Epidemiology:** GS is very rare; **fewer than 400 reported cases worldwide**, mostly from Europe and Asia. Estimated prevalence **1 in 500,000–700,000**. GS is found in roughly **6–11% of thymoma patients**.
- **Inheritance pattern:** **Not inherited** — acquired/sporadic disease; no Mendelian pattern, no penetrance/expressivity concept applies, no reported genetic anticipation, germline mosaicism, founder effect, or consanguinity association.
- **Sex ratio:** approximately equal male:female distribution (no significant sex predominance reported).
- **Geographic distribution:** most reported cases from Europe and Asia, though this may partly reflect reporting/publication patterns rather than true geographic clustering.
- **Comparative epidemiology (from the French DEFI cohort, 690 adults with primary hypogammaglobulinemia):** GS patients (n=21) were diagnosed at a **median age of 60 years**, versus 35 years for CVID and 34 years for B⁻ CVID — underscoring GS's distinctly late-adult onset ([CID 2015](https://academic.oup.com/cid/article/61/2/e13/329344)).

---

## 10. Diagnostics

**Minimal diagnostic criteria (used consistently across systematic reviews):** presence of **both thymoma and hypogammaglobulinemia**, typically with absent/decreased B cells in most cases ([PMC8185358](https://pmc.ncbi.nlm.nih.gov/articles/PMC8185358/)).

- **Laboratory/immunologic tests:**
  - Serum immunoglobulins: low IgG (median ~332 mg/dL, can be as low as ~100 mg/dL), low IgA (86%), low IgM (92.6%) — though some cases show a "low IgG/normal IgA/high IgM" pattern.
  - **Flow cytometry**: markedly reduced or absent CD19+/CD20+ B cells (as low as single-digit percentages), absent transitional (CD38+CD24+) B cells, reduced CD4+ T cells, inverted CD4:CD8 ratio, naïve CD8+CD45RA+ T-cell predominance.
  - Serology: poor/absent vaccine-antigen response (isohemagglutinins, tetanus/pneumococcal titers) consistent with functional antibody deficiency.
- **Imaging:** Chest **CT** demonstrating an **anterior mediastinal mass** (thymoma); may also show mediastinal/hilar lymphadenopathy, bilateral traction bronchiectasis, and pulmonary nodules from chronic/recurrent infection.
- **Histopathology:** Surgical thymoma specimen classified by **WHO histologic subtype** (predominantly type A or AB in GS); B-cell depletion can be demonstrated directly in thymoma tissue. GI biopsy in symptomatic patients may show villous blunting and GVHD-like active chronic inflammation, distinguishing the enteropathy from classic CVID-associated nodular lymphoid hyperplasia.
- **Genetic testing:** Not part of routine clinical workup (no germline gene to test); GTF2I mutation status is a research/tumor-genomic finding, not a diagnostic test for GS itself.
- **Differential diagnosis:** Primarily **CVID** — key distinguishing features are GS's later onset (40–70s vs. childhood/young-adult onset common in CVID), lack of familial clustering, **near-total peripheral B-cell absence** (vs. CVID's typically normal/mildly reduced B cells with reduced memory subsets), absence of lymphoid hyperplasia, and, critically, **presence of thymoma**. Other differentials include HIV/AIDS, secondary hypogammaglobulinemia (drug-induced, lymphoproliferative disease), and idiopathic CD4 lymphocytopenia.
- **Screening:** No population screening program exists given rarity; clinical practice recommends checking serum immunoglobulin levels and flow cytometry in any patient with myasthenia gravis or an anterior mediastinal mass, particularly before starting immunosuppressive therapy.

---

## 11. Outcome/Prognosis

- **Mortality:** Pooled systematic review of 162 patients found **overall mortality of 15.4%** (25/162), with **92.0% of deaths attributable to infection**. This represents substantial improvement over an earlier systematic review's reported **46.1% mortality**, reflecting improved recognition and immunoglobulin replacement access ([PMC8185358](https://pmc.ncbi.nlm.nih.gov/articles/PMC8185358/)).
- **Survival:** **10-year overall survival ≈53.7%** among patients with documented follow-up.
- **Independent prognostic factors (multivariate analysis):**
  - Active thymoma disease: OR 4.157 (p=0.023)
  - Cellular-immunity-related infections: OR 3.324 (p=0.033)
  - Sinopulmonary infections: OR 14.351 (p=0.003)
  - CNS infections: OR 6.403 (p=0.029)
  - Bloodstream infections: OR 6.917 (p=0.012)
- **Clinical subgroups (cluster analysis)** identified three phenotypic clusters with differing infection/autoimmune profiles and prognosis: Cluster 1 (31.5%, cellular-immunity defects, mucosal/CNS infections), Cluster 2 (47.5%, other/unknown immune defect, lower IgG), Cluster 3 (21.0%, humoral/phagocytic defects, sinopulmonary predominance).
- **Note:** Outcomes correlate more strongly with **severity of infections and hematologic/autoimmune complications than with thymoma severity per se** — i.e., the immunologic phenotype, not the tumor stage alone, drives prognosis.
- **Complications:** recurrent/invasive infection, bone marrow failure/aplasia (gradual, per some reviews), PRCA-related anemia requiring transfusion, myasthenic crisis, chronic malabsorptive enteropathy.

---

## 12. Treatment

- **Immunoglobulin replacement therapy (IVIG/SCIG):** the **cornerstone of management** — lifelong replacement is necessary because thymectomy does not reverse hypogammaglobulinemia. Reported in **78.4%** of patients in the pooled series; shown to reduce sinopulmonary infection frequency ([PMID:23200552](https://pubmed.ncbi.nlm.nih.gov/23200552/); [PMID:29888926](https://pubmed.ncbi.nlm.nih.gov/29888926/)). NCIT term: **NCIT:C15986** (Pharmacotherapy) with therapeutic agent immune globulin.
- **Thymectomy:** performed in **90.0%** of surgical candidates — primarily indicated for oncologic control of the thymoma (and adjunct management of associated myasthenia gravis) rather than for reversing immunodeficiency, since **"thymectomy has favorable effects on other parathymic syndromes but is ineffective in improving immunologic deficiencies in Good's syndrome."** NCIT: **NCIT:C15329** (Surgical Procedure) / thymectomy-specific term.
- **Antimicrobial prophylaxis:** used in only ~17.3% of patients in pooled data — an area of underuse relative to guideline recommendations; targeted prophylaxis (e.g., against *Pneumocystis jirovecii*, recurrent bacterial sinopulmonary pathogens) is advocated ([PMID:29878906](https://pubmed.ncbi.nlm.nih.gov/29878906/)).
- **Immunosuppressive therapy for autoimmune complications:** used in ~50.6% of patients with concurrent autoimmunity (e.g., corticosteroids, cyclosporine for PRCA; pyridostigmine/immunosuppression for myasthenia gravis). Case reports describe **rituximab** (anti-CD20) used successfully for refractory PRCA/myasthenia gravis in thymoma-associated multi-autoimmune syndrome, sometimes combined with **tocilizumab** ([PMID:31472400](https://pubmed.ncbi.nlm.nih.gov/31472400/); [PMID:27408396](https://pubmed.ncbi.nlm.nih.gov/27408396/)) — used cautiously given pre-existing combined immunodeficiency.
- **Vaccination:** Because of profound humoral (and often cellular) immunodeficiency, **live vaccines are generally contraindicated**, and non-live vaccines may be poorly immunogenic; passive immunoglobulin replacement is relied upon instead of active immunization for protection.
- **Supportive care:** aggressive treatment of acute infections; monitoring for GI disease (GVHD-like colitis) and hematologic complications; multidisciplinary follow-up (immunology, oncology/thoracic surgery, hematology).
- **Experimental/advanced therapeutics:** No gene therapy, targeted molecular therapy, or GS-specific clinical trials were identified (ClinicalTrials.gov search did not surface GS-specific interventional trials in this review); management remains supportive/replacement-based rather than disease-modifying.
- **Treatment algorithm summary:** (1) diagnose and stage thymoma → (2) thymectomy for oncologic management → (3) lifelong immunoglobulin replacement regardless of surgical outcome → (4) targeted antimicrobial prophylaxis based on infection risk profile → (5) manage autoimmune complications with immunosuppression/rituximab as needed, balanced against infection risk.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classical sense (no known preventable cause); however, prompt recognition of thymoma with early immunologic screening (immunoglobulins + flow cytometry) may allow earlier initiation of protective measures.
- **Secondary prevention:** Early diagnosis of thymoma (often incidental on chest imaging) combined with immunologic workup before immunosuppressive therapy is initiated (e.g., before treating presumed isolated myasthenia gravis) can identify GS early and avoid inappropriate immunosuppression.
- **Tertiary prevention:** Immunoglobulin replacement and antimicrobial prophylaxis to reduce infection-related morbidity/mortality; regular hematologic monitoring for PRCA/marrow failure; GI symptom surveillance for GVHD-like colitis.
- **Immunization strategy:** Passive protection via IVIG/SCIG substitutes for active vaccination; live vaccines avoided.
- **Genetic counseling:** Not applicable — GS is acquired/sporadic, not heritable.
- **Public health relevance:** Minimal, given extreme rarity; no population-level screening programs exist.

---

## 14. Other Species / Natural Disease

- **Dogs (*Canis lupus familiaris*, NCBITaxon:9615):** Thymoma is a recognized canine neoplasm, and canine paraneoplastic syndromes include **hypogammaglobulinemia analogous to human Good syndrome**, alongside myasthenia gravis, hypercalcemia, and other autoimmune disease (occurring in an estimated 20–40% of dogs with thymoma). This thymoma-associated hypogammaglobulinemia is explicitly described in the veterinary literature as "**Good syndrome**" in dogs, representing a **natural, spontaneously occurring comparative model** ([PMC5989270](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5989270/); [AVMA JAVMA 243:1448](https://avmajournals.avma.org/abstract/journals/javma/243/10/javma.243.10.1448.xml)).
- **Cats:** Thymoma-associated myasthenia gravis and paraneoplastic syndromes are also documented, though hypogammaglobulinemia specifically is less well characterized than in dogs.
- **Comparative biology:** The naturally occurring canine disease shares the core features (thymoma + acquired antibody deficiency + autoimmune paraneoplastic phenomena) but formal comparative pathology/mechanistic studies bridging dog and human GS are limited.
- **Zoonotic potential:** None — GS is not a transmissible/infectious disease in either species.

---

## 15. Model Organisms

- **No dedicated animal model exists that fully recapitulates human Good syndrome** (i.e., an induced thymoma + combined immunodeficiency model). This is an important gap.
- **Closest genetic model:** A **mouse model expressing the human thymoma-associated GTF2I p.L424H mutation** in thymic epithelium demonstrates **impaired thymic epithelial progenitor differentiation and reduced thymopoietic activity**, reproducing the upstream thymic-developmental defect implicated in GS pathogenesis, though this model targets thymoma biology broadly rather than GS's immunodeficiency/autoimmunity phenotype specifically ([PMID:36175547](https://pubmed.ncbi.nlm.nih.gov/36175547/); [Communications Biology, PMC9522929](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9522929/)).
- **Natural (non-induced) model:** Companion dogs with spontaneous thymoma and acquired hypogammaglobulinemia represent the best available **naturally occurring comparative model**, useful for studying spontaneous thymoma-associated humoral immunodeficiency, though systematic mechanistic study in this population is limited.
- **Cell/tissue-based models:** Direct study of resected human thymoma tissue (immunohistochemistry/flow cytometry showing B-cell absence within the tumor microenvironment) has served as a quasi-model system for understanding local immune dysregulation ([Discover Oncology 2024](https://link.springer.com/article/10.1007/s12672-024-01450-x)).
- **Applications/limitations:** Existing models can address thymic epithelial developmental biology (via GTF2I mouse models) but cannot yet model the peripheral B-cell aplasia, progressive T-cell dysfunction, or autoimmune complications (PRCA, myasthenia gravis, GVHD-like colitis) that define the clinical syndrome — representing a significant unmet need for a translational GS model.

---

## Summary of Key Evidence Gaps (for curation purposes)

1. **Mechanistic pathway from thymoma → B-cell aplasia is not established** — multiple reviews explicitly state the pathogenesis is unresolved; curated pathophysiology nodes should be flagged with appropriate hedging/hypothesis status rather than presented as confirmed causal biology.
2. No GS-specific transcriptomic/proteomic/single-cell atlas exists.
3. No dedicated GS animal model exists; the GTF2I mouse model addresses only the upstream thymic-developmental step.
4. Quantitative epidemiology rests on pooled case reports/series rather than population-based registries — prevalence estimates (1/500,000–700,000) should be treated as rough.
5. OMIM has no dedicated entry; MONDO:0015696 and ORPHA:169105 are the primary stable identifiers.

---

## Sources

- [Orphanet: Good syndrome (ORPHA169105)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=169105)
- [P-1563. Unraveling a good paradox — Tertiary center experience with Good syndrome, 32 cases through 2024 (PMC12792900)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12792900/)
- [A 69-year-old man with Good syndrome: thymoma-associated immunodeficiency — CMAJ](https://www.cmaj.ca/content/198/5/E171)
- [Frontiers | Good's Syndrome: Time to Move on From Reviewing the Past (2021)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2021.815710/full)
- [Prognosis of Good syndrome: mortality and morbidity — ScienceDirect (Semin Hematol 2016)](https://www.sciencedirect.com/science/article/pii/S1521661616302509)
- [When the Good Syndrome Goes Bad: A Systematic Literature Review (PMC8185358)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8185358/)
- [B cell deficiency in thymoma tissues of Good's syndrome patients — Discover Oncology (2024)](https://link.springer.com/article/10.1007/s12672-024-01450-x)
- [Unraveling the Natural History of Good's Syndrome — JACI In Practice (2024); PMID:38122866](https://pubmed.ncbi.nlm.nih.gov/38122866/)
- [Good Syndrome: An Adult-Onset Immunodeficiency Remarkable for Invasive Infections and Autoimmune Complications — Clinical Infectious Diseases (2015)](https://academic.oup.com/cid/article/61/2/e13/329344)
- [Good's Syndrome With Pure Red Cell Aplasia and Subclinical Myasthenia Gravis (PMC11147683)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11147683/)
- [Pure Red Cell Aplasia and Other Haematological Diseases Associated With Thymoma (PMC8710742)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8710742/)
- [Good's syndrome (immunodeficiency with thymoma): six cases and review — Clinical Case Reports (2021)](https://onlinelibrary.wiley.com/doi/full/10.1002/ccr3.4136)
- [Lymphocyte-Rich Spindle Cell Thymoma — PMID:35034040](https://pubmed.ncbi.nlm.nih.gov/35034040/)
- [Immunodeficiency and Thymoma: A Case Report on Good Syndrome (PMC7970526)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7970526/)
- [Insights from a Case of Good's Syndrome (PMC10296089)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10296089/)
- [Aberrant Peripheral Immune Function in a Good Syndrome Patient (PMC5937423)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5937423/)
- [Good's syndrome presenting with CMV pneumonitis and oesophageal candidiasis (PMC8636207)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8636207/)
- [Gastrointestinal pathology in Good's syndrome, thinking beyond CVID (PMC12647230)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12647230/)
- [Clinicopathologic features of Good's syndrome: Two cases and literature review (PMC8019250)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8019250/)
- [Somatic variant profiling of a thymoma in Good syndrome — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2772613424000039)
- [Human thymoma-associated mutation of GTF2I impairs thymic epithelial progenitor differentiation in mice — PMID:36175547](https://pubmed.ncbi.nlm.nih.gov/36175547/)
- [Somatic mutations of thymic epithelial tumors with myasthenia gravis — PMID:37671056](https://pubmed.ncbi.nlm.nih.gov/37671056/)
- [Primary Driver Mutations in GTF2I Specific to Thymomas (PMC7466068)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/)
- [Successful combined treatment with thymectomy, rituximab and tocilizumab for thymoma-associated multi-autoimmune syndrome — PMID:31472400](https://pubmed.ncbi.nlm.nih.gov/31472400/)
- [Thymoma with Concomitant PRCA, Good's Syndrome and Myasthenia Gravis Responding to Rituximab — PMID:27408396](https://pubmed.ncbi.nlm.nih.gov/27408396/)
- [Intravenous immunoglobulin replacement therapy — PMID:23200552](https://pubmed.ncbi.nlm.nih.gov/23200552/)
- [Features and outcomes of immunoglobulin therapy in Good syndrome, Thailand — PMID:29888926](https://pubmed.ncbi.nlm.nih.gov/29888926/)
- [Prevention of infectious diseases in patients with Good syndrome — PMID:29878906](https://pubmed.ncbi.nlm.nih.gov/29878906/)
- [Good's syndrome: brief overview of an enigmatic immune deficiency — PMID:37729389](https://pubmed.ncbi.nlm.nih.gov/37729389/)
- [A Case of Oral Lichen Planus Preceding the Diagnosis of Good Syndrome (PMC11323965)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11323965/)
- [Acquired hypogammaglobulinemia associated with thymoma: Good syndrome (veterinary) — PMC5989270](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5989270/)
- [Clinical features, treatment options, and outcome in dogs with thymoma: 116 cases — JAVMA](https://avmajournals.avma.org/abstract/journals/javma/243/10/javma.243.10.1448.xml)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 28 |
| On topic | 24 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC8185358` *(abstract only)*: "disrupts the balance between host-defense and self-tolerance"
  - Text part not found as substring: 'disrupts the balance between host-defense and self-tolerance' (note: only abstract available for PMID:34113351, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

30 of 32 terms resolved to a current term; the rest could not be looked up either way.