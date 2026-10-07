---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-29T20:40:27.106475'
end_time: '2026-09-29T20:55:28.335169'
duration_seconds: 901.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial DNA Depletion Syndrome, Myopathic Form
  mondo_id: MONDO:0012301
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
  - claude-haiku-4-5-20251001
  - claude-opus-5
  num_turns: 34
  total_cost_usd: 7.588275749999999
  session_id: e75151ed-986e-4ce6-81b7-f329b1b18555
  stop_reason: end_turn
  permission_denials: 8
  denied_tools:
  - Bash
  - mcp__ols-mcp__search_all_ontologies
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 19
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 72
  verified: 72
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial DNA Depletion Syndrome, Myopathic Form
- **MONDO ID:** MONDO:0012301 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial DNA Depletion Syndrome, Myopathic Form** covering all of the
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

I'll research this thoroughly, starting with the primary literature on TK2 deficiency and the existing repository context.

PubMed MCP access isn't granted in this session. Let me use the repository's existing verified reference cache plus web search.

# Disease Characteristics Research Report

## Mitochondrial DNA Depletion Syndrome, Myopathic Form (TK2 Deficiency)

**MONDO:0012301** · TK2-related mitochondrial DNA maintenance defect, myopathic form · MTDPS2

**Report date:** 2026-09-29 · **Inheritance:** Autosomal recessive (Mendelian)

---

### Provenance and method note

This report was assembled from 18 references held in the dismech verified reference cache, of which **13 were read in full text or full abstract for this report**. Eleven carry full PubMed Central text; the remainder are abstract-only records. Where a claim rests on a reference I did not read directly, I cite it as a pointer and attribute the substance to the secondary source I did read (chiefly Berardo et al. 2022, PMID:35094997), rather than presenting a quotation I could not verify.

**Ontology identifiers in this report were read from the repository's authority-backed term caches (`cache/<prefix>/terms.csv`) and from the validated bindings of the curated `kb/disorders/` entry, in the same step they were written.** The Ontology Lookup Service MCP tool was unavailable in this session (permission not granted), so no identifier here was resolved by live OLS query, and none was written from recall. Concepts for which I could not produce a cache- or entry-backed identifier are named in prose and flagged as unresolved in §16.

**Evidence-source typing** follows the dismech convention and is marked per claim: `[HUMAN CLINICAL]`, `[MODEL ORGANISM]`, `[IN VITRO]`, `[COMPUTATIONAL]`, `[REVIEW/SYNTHESIS]`.

---

## 1. Disease Identity and Identifiers

TK2 deficiency (TK2d) is an autosomal recessive disorder of mitochondrial DNA (mtDNA) maintenance caused by biallelic pathogenic variants in *TK2*, encoding mitochondrial thymidine kinase 2. Its cardinal presentation is a progressive myopathy with early and disproportionate involvement of respiratory, cervical, facial and bulbar musculature, accompanied in muscle by quantitative mtDNA depletion, qualitative multiple mtDNA deletions, or both.

| Field | Value | Source |
|---|---|---|
| Primary ontology term | `MONDO:0012301` mitochondrial DNA depletion syndrome, myopathic form | curated entry binding |
| OMIM phenotype | **MIM #609560** | Ceballos et al. 2024, PMID:38544965 |
| Gene | *TK2*, `hgnc:11831` | curated entry binding |
| Gene locus | chromosome **16q21** | PMID:35094997 |
| Reference transcript | **NM_004614.5** | PMID:35094997 |
| Alternative designations | MTDPS2; mtDNA depletion syndrome 2 (myopathic type); TK2-related mtDNA maintenance defect, myopathic form | PMID:23230576 |

The gene's structure is given precisely by Berardo and colleagues: `[REVIEW/SYNTHESIS]`

> "The TK2 gene is located at chromosome 16q21 and spans 42,410 base pairs with 10 exons encoding a 265 amino acid protein. The TK2 mRNA length is 5114 nucleotides with a 3.8 kilobase long 3'-untranslanted [*sic*] region (NM_004614.5)."
> — Berardo A, Domínguez-González C, Engelstad K, Hirano M. *J Neuromuscul Dis*. 2022. PMID:35094997, DOI 10.3233/JND-210786

The causal gene was identified in 2001 in patients with myopathic mtDNA depletion (Saada et al., *Nat Genet*; PMID:11687801) `[HUMAN CLINICAL]` `[IN VITRO]`.

**Nomenclature caution that matters for curation.** GeneReviews titles the entity a *"TK2-related mitochondrial DNA (mtDNA) maintenance defect"* rather than a depletion syndrome, and this is not cosmetic: late-onset disease characteristically shows **multiple mtDNA deletions with normal or near-normal mtDNA copy number**, so "depletion syndrome" misdescribes a substantial minority of molecularly confirmed patients. See §8 and §9.

**Identifiers I could not resolve in this session:** Orphanet ORPHAcode, ICD-10-CM and ICD-11 codes, MeSH descriptor, UMLS CUI, and the *TK2* MIM gene number (as distinct from the phenotype MIM). These require lookups that were not available; they are flagged in §16 rather than supplied from memory.

---

## 2. Classification and Nosology

TK2d sits at the intersection of three classification axes, and its position differs on each.

**By mechanism — mtDNA maintenance defect.** TK2d belongs to the group of nuclear-gene disorders that impair replication or nucleotide supply for the mitochondrial genome, rather than disorders of the mitochondrial genome itself. Lopez-Gomez et al. give the canonical genotype-to-phenotype partition of the mtDNA depletion syndromes: `[REVIEW/SYNTHESIS]`

- **Myopathic** — *TK2*
- **Hepatocerebral** — *DGUOK*, *POLG*, *C10orf72* (*TWNK*), *MPV17*
- **Myopathy with renal tubulopathy** — *RRM2B*
- **Encephalomyopathic** — *SUCLA2*, *SUCLG1*
- **Severe infantile encephalomyopathy** — *OPA1*, *MFN2*

— Lopez-Gomez C, et al. *Ann Neurol*. 2017. PMID:28318037, DOI 10.1002/ana.24922

Garone et al. name the eight genes then established for infantile mtDNA depletion syndrome: *TK2*, *DGUOK*, *POLG*, *MPV17*, *RRM2B*, *SUCLA2*, *SUCLG1* and *C10orf2* (PMID:24968719) `[REVIEW/SYNTHESIS]`.

**By biochemical pathway — deoxyribonucleoside salvage.** Within the maintenance defects, TK2d is specifically a defect of the **mitochondrial pyrimidine deoxyribonucleoside salvage pathway**, grouping it with *DGUOK* (purine salvage) and functionally, though not mechanistically, with *TYMP*/MNGIE and *RRM2B* as disorders of nucleotide pool balance.

**By clinical phenotype — a mitochondrial myopathy.** Clinically the disorder presents as a myopathy and enters the differential of limb-girdle muscular dystrophy, spinal muscular atrophy, facioscapulohumeral dystrophy and congenital myopathy (§14) far more often than it enters the differential of a classical mitochondrial encephalopathy.

**Phenotypic continuum, not discrete types.** GeneReviews is explicit that the entity is graded rather than partitioned: `[REVIEW/SYNTHESIS]`

> "TK2-related mitochondrial DNA (mtDNA) maintenance defect is a phenotypic continuum that ranges from severe to mild. ... Three main subtypes of presentation have been described: Infantile-onset myopathy with neurologic involvement and rapid progression to early death. ... Juvenile/childhood onset with generalized proximal weakness and survival to at least 13 years. Late-/adult-onset myopathy with facial and limb weakness and mtDNA deletions."
> — GeneReviews, PMID:23230576

These three bands — **infantile (<12 months to ~2 years)**, **childhood/juvenile**, and **late/adult** — are used consistently throughout this report because every major series stratifies on them, but they are convenience bands on a continuum, and the Spanish cohort's onset distribution (§3) shows no natural breakpoints.

A placement within the International Classification of Inherited Metabolic Disorders (ICIMD) framework is available at PMID:33340416; I did not read that record in full and so do not quote its category assignment here.

---

## 3. Epidemiology

**No direct prevalence measurement of TK2d exists.** Every figure in the literature is an indirect estimate built by multiplying a mitochondrial-disease prevalence by the TK2 share of a referred mtDNA-depletion cohort. This is important to state plainly, because the resulting numbers are often quoted as though they were measured.

Berardo et al. give the derivation explicitly: `[REVIEW/SYNTHESIS]` a background mitochondrial disease prevalence of **11.5 per 100,000**, and a TK2 fraction of **10%, 12.5% and 18%** across three separate MDDS screening series, yielding

> "a minimum prevalence of TK2d at 600 patients and a maximum prevalence of 2700 TK2-deficient patients in the United States."
> — PMID:35094997

Against that estimated denominator, the count of reported patients remains small. GeneReviews records that `[REVIEW/SYNTHESIS]`

> "approximately 107 individuals with a molecularly confirmed diagnosis have been reported."
> — PMID:23230576

The single largest cohort published to date is Spanish: **53 molecularly confirmed patients** (Ceballos et al., *Neurol Genet* 2024, PMID:38544965) `[HUMAN CLINICAL]`, which by itself is roughly half the previously reported world literature — a strong indication that TK2d is substantially under-diagnosed, and that the "107 reported" figure reflects ascertainment rather than incidence.

**Age-at-onset distribution** (n = 53, Spanish cohort) `[HUMAN CLINICAL]`:

| Onset band | n | % |
|---|---|---|
| < 1 year | 4 | 7.5% |
| 12–36 months | 11 | 20.8% |
| 3–12 years | 6 | 11.3% |
| > 12 years | 32 | 60.3% |
| — of which > 40 years | 14 | 26.4% |

— PMID:38544965

This distribution is itself a finding: **the majority of molecularly confirmed patients in an unselected national cohort have adult-onset disease**, inverting the older literature's impression of TK2d as a fatal infantile myopathy. The inversion is almost certainly an ascertainment correction — infantile cases died before molecular diagnosis was available, and adult cases were mis-labelled as limb-girdle dystrophy.

**Founder effects and population genetics.** The Spanish cohort provides the only population-genetic characterisation of TK2 alleles `[HUMAN CLINICAL]` `[COMPUTATIONAL]`:

| Variant | Spanish allele freq. | gnomAD allele freq. | Enrichment |
|---|---|---|---|
| p.Lys202del (c.604_606del) | 0.034% | 0.0004% | **86-fold** |
| p.Thr108Met (c.323C>T) | 0.062% | 0.0046% | **13-fold** |

Regional enrichment is sharper still: p.Thr108Met reaches **0.176% in Galicia**, a 38-fold excess over gnomAD. gnomAD's Latino subpopulation carries p.Lys202del at 0.0029%, consistent with transmission of the Iberian allele to the Americas.

Haplotype dating placed the most recent common ancestor at **425 years (95% CI 125–1,550)** for p.Thr108Met and **2,375 years (1,212–3,532)** for p.Lys202del, corresponding to roughly 16.8 and 95.2 generations. Methods included runs-of-homozygosity analysis with FIS/FST/FROH inbreeding coefficients, PLINK, and the Axiom Spain Biobank Array. — PMID:38544965

The practical consequence: in Iberian and Iberian-descended populations, TK2d prior probability is materially higher than a global estimate implies, and p.Thr108Met / p.Lys202del warrant targeted testing.

**Not established:** incidence, sex ratio (no series reports a sex skew, but none powered to exclude one), prevalence outside Spain and referral-based US/European series, and carrier frequency in any non-Iberian population.

---

## 4. Clinical Presentation

### 4.1 The core syndrome

The presenting and dominant feature across all onset bands is **proximal and axial muscle weakness** (`HP:0003701` Proximal muscle weakness) with a distribution that is the disorder's clinical signature: cervical extensor, facial and bulbar muscles are involved early and disproportionately relative to limb strength.

The Spanish cohort quantifies this: **80% of patients had cervical and facial weakness regardless of age of onset** (PMID:38544965) `[HUMAN CLINICAL]`. This axial-and-facial predominance, in a patient with elevated creatine kinase, is what should prompt *TK2* testing rather than a further dystrophy panel.

**Respiratory involvement is the prognostically decisive feature.** Weakness of the diaphragm (`UBERON:0001103`) and accessory respiratory muscles produces respiratory insufficiency (`HP:0002093`) that drives both ventilatory dependence and mortality (§11). GeneReviews: *"Affected individuals experience progressive muscle weakness leading to respiratory failure."* (PMID:23230576).

### 4.2 Presentation by onset band

**Infantile onset (<2 years)** `[HUMAN CLINICAL]` `[REVIEW/SYNTHESIS]`
Rapidly progressive myopathy with hypotonia (`HP:0001252`), motor delay or developmental regression (`HP:0002376`), failure to thrive (`HP:0001508`), and progression to respiratory failure and early death. GeneReviews records that in this band *"Some individuals develop dysarthria, dysphagia, and/or hearing loss. Cognitive function is typically spared."* (PMID:23230576) — the sparing of cognition despite "neurologic involvement" is a clinically important and frequently misstated point. Seizures (`HP:0001250`), encephalopathy (`HP:0001298`) and sensorineural hearing impairment (`HP:0000407`) occur but are not universal.

**Childhood/juvenile onset** `[REVIEW/SYNTHESIS]`
Generalised proximal weakness with survival to at least the teens. Berardo et al. report in this band: **wheelchair dependence 60%**, **ventilator dependence 55%**, **CNS involvement 10%**, and **extraskeletal (non-muscle) involvement under 20%** (PMID:35094997).

**Late/adult onset (>12 years, and a large >40-year group)** `[HUMAN CLINICAL]` `[REVIEW/SYNTHESIS]`
Mean onset **31 years**. Facial and limb weakness, with **non-invasive ventilation in 12 of 18 (67%)** and **gastrostomy in approximately 30%, at a mean 19.6 years after onset** (PMID:35094997). Chronic progressive external ophthalmoplegia (`HP:0000590`), ptosis (`HP:0000508`) and ophthalmoparesis (`HP:0000597`) are characteristic of this band and largely absent from the infantile one.

### 4.3 The ptosis/CPEO age gradient

The Spanish cohort documents an age-dependent ocular gradient that is among the most useful discriminating observations in the disorder `[HUMAN CLINICAL]`:

| Onset band | Ptosis **and** CPEO | Ptosis only | Neither |
|---|---|---|---|
| < 12 years | 18.8% | 18.8% | 62.5% |
| 12–40 years | 40% | 46.7% | 13.3% |
| > 40 years | 13/13 (100%) ptosis | — | 11/13 (85%) had both |

— PMID:38544965

Read this as a rule of thumb: **in adult-onset TK2d, ptosis is effectively obligatory; in infantile-onset TK2d, its absence is the norm.** An adult with axial/facial weakness, high CK and *no* ptosis is a less likely TK2d candidate than the same patient with ptosis.

### 4.4 Additional and atypical features

- **Dysphagia** (`HP:0002015`) in 40% of the Spanish cohort; **dysarthria** (`HP:0001260`) also recorded.
- **Scapular winging** (`HP:0003691`), contributing to the FSHD and SMA mimicry described in §14.
- **Facial palsy / facial weakness** (`HP:0010628`).
- **Loss of ambulation** (`HP:0002505`) — but note this is *less* common than the older literature implies: only **16.8% (7/43)** of the Spanish cohort were non-ambulant (PMID:38544965). Ventilatory failure outpaces loss of walking.
- **Isolated exercise intolerance with exertional rhabdomyolysis** in **3 patients (6.8%)** (`HP:0003546`, `HP:0003201`) — a genuinely oligosymptomatic presentation that would not normally prompt mitochondrial testing (PMID:38544965).
- **Hypertrophic cardiomyopathy** reported in association with the p.Ala139Val and p.Phe70Ser variants (PMID:35094997) — cardiac involvement is otherwise rare.

### 4.5 Laboratory presentation

**Creatine kinase** (`HP:0003236` Elevated circulating creatine kinase activity) is elevated in the great majority, spanning **272–6,500 U/L across 57 patients** — but Berardo et al. record **6 patients with transient normal values**, and state the consequence directly: `[REVIEW/SYNTHESIS]`

> "indicating that a normal CK does not exclude TK2d."
> — PMID:35094997

Lactate (`HP:0002151` Increased circulating lactate concentration) may be raised but is neither sensitive nor specific.

---

## 5. Natural History and Progression

The trajectory differs qualitatively, not merely in tempo, across onset bands.

**Infantile onset** follows a compressed course: onset in the first two years, rapid progression of weakness, respiratory failure, and death typically within the first years of life. The untreated mortality in this band is stark — the Spanish cohort found **86% of untreated patients with onset before 12 years had died** by the September 2023 census (PMID:38544965) `[HUMAN CLINICAL]`.

**Childhood/juvenile onset** progresses over years to a decade-plus, accumulating wheelchair dependence (≈60%) and ventilatory support (≈55%) but with survival into the teens and beyond (PMID:35094997).

**Adult onset** is the slowest course and the one in which the sequence of milestones is best described: weakness beginning at a mean of 31 years, ptosis and CPEO accruing, non-invasive ventilation in about two-thirds, and gastrostomy at a mean of **19.6 years after onset** in the ~30% who require it (PMID:35094997) `[REVIEW/SYNTHESIS]`.

**Genotype predicts the timing of ventilatory failure.** This is one of the clearest genotype–course correlations in TK2d, and it is statistically supported `[HUMAN CLINICAL]`:

> All **6 p.Lys202del homozygotes** began mechanical ventilation **after age 40**. **78% of 9 p.Thr108Met homozygotes** began ventilation **between ages 12 and 40**. Association with variant, *p* < 0.01.
> — PMID:38544965

Dedicated natural-history analyses are available at PMID:29602790 (subtype frequencies and post-onset survival) and PMID:31060578 (late-onset series with respiratory, MRI and biomarker profiling); both are in the cache but I did not read them in full for this report and therefore quote no figures from them.

**The single most useful framing for prognosis is that respiratory function, not ambulation, is the clock.** Thirty percent of the Spanish cohort had died, **all of respiratory failure** (§11), while five in six patients remained ambulant.

---

## 6. Pathophysiology and Mechanism

### 6.1 Ordered causal chain

1. **Biallelic pathogenic variants in *TK2* (`hgnc:11831`)** reduce or abolish the catalytic efficiency of mitochondrial thymidine kinase 2 (`GO:0004797` thymidine kinase activity; `GO:0004137` deoxycytidine kinase activity). *Demonstrated in vitro by enzyme kinetics on recombinant mutant protein* (PMID:12493767).
2. Loss of TK2 activity **results in** failure of the first and rate-limiting phosphorylation step of the mitochondrial **pyrimidine deoxyribonucleoside salvage pathway** (`GO:0043099` pyrimidine deoxyribonucleoside salvage) — deoxythymidine → dTMP and deoxycytidine → dCMP. *Demonstrated* (PMID:20940150).
3. In **proliferating cells**, cytosolic thymidine kinase 1 (TK1) supplies deoxypyrimidine nucleotides independently, which **masks** the TK2 defect. *Demonstrated in mouse tissue* (PMID:20940150).
4. Post-mitotic differentiation **leads to** cell-cycle-dependent **down-regulation of TK1**, which **unmasks** the TK2 deficiency in that tissue — the step that sets both tissue selectivity and age of onset. *Demonstrated in the Tk2⁻/⁻ mouse* (PMID:20940150).
5. Unmasked TK2 deficiency **results in** depletion of the mitochondrial **dTTP** pool (`CHEBI:18077`), with the dCTP pool **relatively preserved** because de novo ribonucleotide reductase (R1–p53R2) can supply it. *Demonstrated by tissue nucleotide measurement* (PMID:20940150).
6. The resulting **imbalanced mitochondrial dNTP pool** (`GO:0009202` deoxyribonucleoside triphosphate biosynthetic process) **leads to** failure of faithful mtDNA replication (`GO:0006264` mitochondrial DNA replication; `GO:0032042` mitochondrial DNA metabolic process). *Demonstrated* (PMID:20940150, PMID:24968719).
7. **The mechanism branches here**, and the branch is the disorder's central clinical puzzle:
   - **7a — Quantitative branch:** replication failure **results in** reduced mtDNA copy number — **mtDNA depletion** (`HP:0009141` Depletion of mitochondrial DNA in muscle tissue). Dominant in early-onset disease. *Demonstrated in human muscle and mouse tissue.*
   - **7b — Qualitative branch:** replication error **results in** **multiple mtDNA deletions** (`HP:0003689`) with normal or near-normal copy number. Dominant in late-onset disease. *Demonstrated in human muscle; the mechanistic route from dNTP imbalance to deletion formation specifically — as opposed to depletion — is **inferred**, not demonstrated.*
8. **A compensatory branch intervenes before OXPHOS fails.** Reduced mtDNA copy number **leads to** down-regulation of the mitochondrial transcription terminator **MTERF3**, which **results in** increased mitochondrial transcript abundance *per mtDNA molecule* (`GO:0006390` mitochondrial transcription) — approximately **3-fold in heart** — thereby sparing OXPHOS despite substantial copy-number loss. *Demonstrated in the Tk2⁻/⁻ mouse* (PMID:20940150).
9. Where mtDNA loss **exceeds** the capacity of that transcriptional compensation — the **"mtDNA depletion threshold"** — it **results in** deficiency of mtDNA-encoded respiratory chain subunits and consequent **oxidative phosphorylation deficiency** (`GO:0006119` oxidative phosphorylation; `GO:0022904` respiratory electron transport chain), measurable as complex IV deficiency (`HP:0008347`) and cytochrome *c* oxidase-negative fibres (`HP:0003688`). *Demonstrated* (PMID:20940150).
10. OXPHOS deficiency in the **skeletal muscle fibre** (`CL:0008002`) of **skeletal muscle tissue** (`UBERON:0001134`) **leads to** fibre degeneration, ragged-red fibre formation (`HP:0003200`), necrosis and dystrophic remodelling. *Demonstrated histologically in human muscle.*
11. The degree of residual TK2 activity **determines which tissues cross the threshold**, and therefore the phenotype: **14–45% residual activity leads to myopathy; under 10% leads to encephalomyopathy.** *Demonstrated by correlating patient enzyme assays with phenotype* (PMID:20940150).
12. Progressive loss of muscle fibres **results in** proximal, cervical, facial and bulbar weakness (`HP:0003701`, `HP:0000467`, `HP:0010628`), which **leads to** diaphragmatic and accessory respiratory muscle failure (`UBERON:0001103`; `HP:0002093` Respiratory insufficiency).
13. Respiratory muscle failure **results in** ventilatory dependence and, in untreated disease, **death — in 100% of the fatalities in the largest cohort** (PMID:38544965). *Demonstrated* `[HUMAN CLINICAL]`.

**Therapeutic interruption point.** Steps 2–5 are bypassable: exogenous deoxycytidine and deoxythymidine (`CHEBI:15698`, `CHEBI:17748`) enter mitochondria and are phosphorylated by pathways that do not require TK2, restoring dNTP pools downstream of the lesion. This is the entire rationale for nucleoside substrate-enhancement therapy (§12), and it is why the therapy works *without* correcting the genetic defect.

### 6.2 Detail

**The rate-limiting-step argument.** Dorado et al. state TK2's position in the pathway precisely: `[MODEL ORGANISM]` `[REVIEW/SYNTHESIS]`

> "the first and rate-limiting step for the salvage pathway synthesis of deoxypyrimidine nucleoside triphosphates required for mitochondrial DNA (mtDNA) replication and maintenance in post-mitotic cells"
> — Dorado B, Area E, Akman HO, Hirano M. *Hum Mol Genet*. 2011. PMID:20940150, DOI 10.1093/hmg/ddq453

Because post-mitotic cells cannot rely on cell-cycle-coupled de novo synthesis, and because the mitochondrial pyrimidine supply has no redundant route, TK2 loss is uniquely consequential in differentiated tissue.

**The TK1 hand-off is the tissue-selectivity mechanism.** The same paper demonstrates the unmasking directly: `[MODEL ORGANISM]`

> "The down-regulation of Tk1 activity unmasks Tk2 deficiency in Tk2-/- mice and correlates with the onset of mtDNA depletion in the brain and the heart"
> — PMID:20940150

The measured time course in Tk2⁻/⁻ mouse brain shows the sequence: dTTP fell from **57 ± 17% of normal at day 8 to 11 ± 8% at day 13**, while **dCTP remained preserved** (attributed to de novo ribonucleotide reductase R1–p53R2 activity). Brain mtDNA fell from **45 ± 10% to 35 ± 8%**; heart mtDNA fell from normal to **58 ± 27%**.

Crucially, mtDNA loss begins **before symptoms**. Garone et al. measured a pre-symptomatic postnatal day 4 baseline in Tk2⁻/⁻ mice and already found cerebrum **38 ± 13%**, cerebellum **54 ± 1%**, muscle **28 ± 12%** and kidney **62 ± 11%** of normal mtDNA, with heart and liver still normal (PMID:24968719) `[MODEL ORGANISM]`. Any therapy that waits for symptoms is starting behind.

**MTERF3 and the depletion threshold.** The compensation mechanism in step 8 is specifically transcriptional and specifically MTERF3-mediated. MTERF3 fell to **43 ± 22% in brain** and **63 ± 21% in heart**. Dorado et al. explicitly **excluded** the canonical biogenesis regulators — PGC-1α, NRF-1, NRF-2, TFAM, TFB1M and TFB2M were *not* responsible. They define the concept: `[MODEL ORGANISM]`

> "we can define the mtDNA depletion threshold as the reduction in mtDNA that overwhelms transcriptional compensation"
> — PMID:20940150

This resolves an otherwise paradoxical observation — that tissues can lose 40% of their mtDNA with preserved respiratory function — and it identifies **MTERF3 inhibitors as a rational therapeutic class**, proposed in that paper and, so far as I can establish, never developed.

**Why muscle.** Two independent and complementary explanations exist. The first, from Saada et al., is a supply-and-demand argument: `[HUMAN CLINICAL]` `[IN VITRO]`

> "Our results suggest that low basal TK2 activity combined with a high requirement for mitochondrial encoded proteins in muscle predispose this tissue to the devastating effect of TK2 deficiency."
> — Saada A, Shaag A, Elpeleg O. *Mol Genet Metab*. 2003. PMID:12765840, DOI 10.1016/s1096-7192(03)00063-5

The same paper records the striking selectivity: *"Other tissues such as liver, brain, heart, and skin remain unaffected throughout the patients' life."* The second explanation is the TK1 timing argument above — muscle exits the cell cycle early and durably. These are not competing; they compound.

**Mutant enzyme kinetics establish the genotype–activity–phenotype ladder.** Wang, Saada and Eriksson characterised recombinant mutants `[IN VITRO]`:

> "The I212N mutant showed less than 1% activity as compared with wild type TK2 with all deoxynucleosides."
> — Wang L, Saada A, Eriksson S. *J Biol Chem*. 2003. PMID:12493767, DOI 10.1074/jbc.M206143200

The p.His121Asn mutant behaves quite differently and instructively: **normal Km for deoxythymidine (6 µM) and deoxycytidine (11 µM)**, but *"2- and 3-fold lower V(max) values as compared with wild type TK2 and markedly increased K(m) values for ATP, leading to decreased enzyme efficiency."* The lesion is in phosphate donor handling, not substrate recognition — consistent with the structural observation that His126 (mouse) / His121 (human) sits at the C-terminal end of helix α4 facing the **ERS (Glu138–Arg139–Ser140) phosphate-transferring domain** (PMID:20940150).

**Substrate-specific kinetics matter for dosing.** Lopez-Gomez et al. found TK2 follows **Michaelis–Menten kinetics for deoxycytidine but shows negative cooperativity for deoxythymidine** (PMID:28318037) `[IN VITRO]`. The two substrates are not interchangeable, and a therapy must supply both.

### 6.3 Ontology terms for the mechanism

| Concept | Term | Modifier |
|---|---|---|
| Thymidine kinase activity | `GO:0004797` thymidine kinase activity | DECREASED / LOSS_OF_FUNCTION |
| Deoxycytidine kinase activity | `GO:0004137` deoxycytidine kinase activity | DECREASED |
| Pyrimidine salvage | `GO:0043099` pyrimidine deoxyribonucleoside salvage | DECREASED |
| dNTP synthesis | `GO:0009202` deoxyribonucleoside triphosphate biosynthetic process | DECREASED |
| mtDNA replication | `GO:0006264` mitochondrial DNA replication | DECREASED |
| mtDNA metabolism | `GO:0032042` mitochondrial DNA metabolic process | DECREASED |
| Mitochondrial transcription (MTERF3 compensation) | `GO:0006390` mitochondrial transcription | INCREASED (per mtDNA copy) |
| Mitochondrion organization | `GO:0007005` mitochondrion organization | — |
| OXPHOS | `GO:0006119` oxidative phosphorylation | DECREASED |
| Respiratory chain | `GO:0022904` respiratory electron transport chain | DECREASED |
| Affected cell type | `CL:0008002` skeletal muscle fiber | — |
| Affected tissue | `UBERON:0001134` skeletal muscle tissue | — |
| Respiratory failure site | `UBERON:0001103` diaphragm | — |
| Substrate (thymidine) | `CHEBI:17748` thymidine | — |
| Substrate (deoxycytidine) | `CHEBI:15698` 2'-deoxycytidine | — |
| Depleted pool | `CHEBI:18077` dTTP | DECREASED |

Related cell types available for a fuller pathograph: `CL:0002372` myotube, `CL:0000594` skeletal muscle satellite cell, `CL:0000189` slow muscle cell, `CL:0000190` fast muscle cell, `CL:0000540` neuron (encephalomyopathic band), `CL:0000182` hepatocyte (spared — useful as a contrast with *DGUOK*/*MPV17* hepatocerebral disease).

---

## 7. Genetics

**Gene and inheritance.** *TK2* (`hgnc:11831`), chromosome 16q21, 10 exons, 265 amino acids, NM_004614.5. Inheritance is **autosomal recessive** (`HP:0000007`).

**Variant spectrum.** Berardo et al. record **more than 30 pathogenic variants**, with the frequently encountered ones being **p.Thr108Met, p.Asn58Ser, p.Arg130Trp, p.Lys202del, p.His121Asn and p.Arg183Trp** (PMID:35094997) `[REVIEW/SYNTHESIS]`. The Spanish cohort found **16 distinct variants across 53 patients** (PMID:38544965) `[HUMAN CLINICAL]`.

**Allelic frequency in the largest cohort** (PMID:38544965):

| Variant | cDNA | Patients | Alleles |
|---|---|---|---|
| p.Lys202del | c.604_606del | 21 | 35 |
| p.Thr108Met | c.323C>T | 18 | 32 |
| p.Tyr208Cys | — | — | 11 |
| p.Ala139Thr | — | — | 6 |

Two variants therefore account for the large majority of Spanish alleles — a founder architecture (§3), not a mutational hotspot.

**A novel variant** was reported in that cohort: **c.503del (p.Ile168ThrfsTer2)**, classified on PVS1 + PM2 + observed *in trans*.

**Variant distribution within the gene.** Pathogenic variants were found in **all exons except 3 and 4**, with missense variants **clustering at residues 100–141** — the region containing the Mg²⁺ and ATP binding determinants (PMID:38544965). This is mechanistically coherent with the p.His121Asn kinetics above (§6.2): the disease-dense region is the phosphate-transfer machinery, not the nucleoside-binding pocket.

**Genotype–phenotype correlations.** These are real but partial:

| Variant | Association | Source |
|---|---|---|
| p.Arg130Trp | Most severe phenotype | PMID:35094997 |
| p.Ile212Asn | <1% residual activity *in vitro* | PMID:12493767 |
| p.Arg183Trp (homozygous) | Muscle-restricted mtDNA depletion | PMID:35094997 |
| p.Lys202del | Adult-only onset; MV always after age 40 | PMID:35094997, PMID:38544965 |
| p.Thr108Met (homozygous) | MV between ages 12 and 40 in 78% | PMID:38544965 |
| p.Ala139Val, p.Phe70Ser | Hypertrophic cardiomyopathy | PMID:35094997 |
| p.His121Asn | Reduced Vmax, raised ATP Km | PMID:12493767 |

**The unifying quantitative model** is residual enzyme activity, not variant identity: **14–45% of normal TK2 activity produces myopathy; below 10% produces encephalomyopathy** (PMID:20940150). Variant-specific correlations are best read as proxies for where a genotype falls on that scale.

**Modifiers, penetrance and expressivity.** No modifier loci are established. Penetrance appears complete for biallelic pathogenic genotypes, but **expressivity is wide even within a genotype** — p.Thr108Met homozygotes span onset bands — and no explanation for that intra-genotypic variability has been identified. This is a genuine open question, not an under-researched one.

---

## 8. Diagnosis

GeneReviews gives the diagnostic criteria, and they are **age-stratified**, which is the point most often missed: `[REVIEW/SYNTHESIS]`

> "The diagnosis of TK2-related mtDNA maintenance defect is established in a proband with infantile onset of disease with severely reduced (typically <20% of age- and tissue-matched healthy controls) mtDNA content in skeletal muscle. The diagnosis of TK2-related mtDNA maintenance defect is established in a proband older than age two years with reduced mtDNA content or multiple mtDNA deletions, ragged red fibers and/or COX-deficient fibers in skeletal muscle. The diagnosis is confirmed by the identification of biallelic pathogenic variants in TK2 by molecular genetic testing."
> — PMID:23230576

Two consequences follow.

**First, mtDNA quantification alone will miss late-onset disease.** Berardo et al. report that muscle mtDNA averaged **14% of normal across 55 cases** — but **15 cases had normal mtDNA content**, and in those the **mean age of onset was 19 years** (PMID:35094997) `[REVIEW/SYNTHESIS]`. In adult-onset patients the abnormality is qualitative (multiple deletions), not quantitative. A normal muscle mtDNA copy number in an adult does not exclude TK2d.

**Second, respiratory chain enzymology is an unreliable screen.** Berardo et al. state it plainly:

> "only 20% to 74% of confirmed TK2d patients have had deficiencies in OXPHOS activities."
> — PMID:35094997

Combined with the CK observation (*"a normal CK does not exclude TK2d"*, §4.5), the diagnostic implication is that **no single conventional screening test is sensitive**, and molecular testing should be reached for early rather than after a normal biochemical workup.

**Practical diagnostic pathway:**

1. **Clinical suspicion** — proximal + cervical + facial/bulbar weakness; ptosis in an adult; elevated CK; respiratory involvement out of proportion to limb weakness.
2. **Creatine kinase measurement** (`NCIT:C64489`) — supportive, not exclusionary.
3. **Muscle biopsy** (`NCIT:C51895`) — histology, histochemistry (COX/SDH), respiratory chain enzymology, and **mtDNA copy number plus deletion analysis** (§9).
4. **Molecular confirmation** — biallelic *TK2* variants by exome (`NCIT:C101295` Whole Exome Sequencing) or targeted panel. In Iberian or Iberian-descended patients, targeted p.Thr108Met / p.Lys202del testing is high-yield.
5. **Biomarkers** — GDF-15 and FGF-21 (§9) as supportive, non-diagnostic adjuncts.

Biopsy yield in the Spanish cohort was essentially total: **50 of 53 patients (94.3%) underwent muscle biopsy and all were pathologic** (PMID:38544965) — so while biopsy is not required for diagnosis once molecular testing is available, it is highly informative when performed.

---

## 9. Histopathology and Biomarkers

### 9.1 Muscle histopathology

The biopsy shows **mitochondrial and dystrophic features together**, which is itself diagnostically suggestive.

*Mitochondrial features:*
- **Ragged-red fibres** (`HP:0003200`): **2–18% of fibres** (PMID:38544965)
- **COX-negative fibres** (`HP:0003688`): **4–40% of fibres** (PMID:38544965)
- Decreased complex IV activity (`HP:0008347`)

*Dystrophic and neurogenic-mimicking features* (Spanish cohort, PMID:38544965) `[HUMAN CLINICAL]`:
- Myopathic change in **93%**
- Fibre-size variability in **93%**
- Endomysial fibrosis in **52%**
- Nuclear internalization in **50%**
- Fibre necrosis in **48%**

Berardo et al. add a feature that directly explains a recurrent misdiagnosis: **SMA-like fibre grouping with type 1 fibre predominance** (`HP:0003803` Type 1 muscle fiber predominance) (PMID:35094997). A biopsy read as neurogenic grouping in an infant is a classic route to a wrong SMA diagnosis (§14).

### 9.2 Molecular pathology of muscle

- **mtDNA depletion** (`HP:0009141`): mean **14% of normal** across 55 cases, but with 15 normal-content cases skewing toward late onset (PMID:35094997). Individual Spanish-cohort values span **<10% to 66%** (PMID:38544965).
- **Multiple mtDNA deletions** (`HP:0003689`): characteristic of late-onset disease, and the abnormality present when copy number is normal.

The two findings are best understood as the two arms of the §6.1 step-7 branch rather than as alternative severities of one finding.

### 9.3 Circulating biomarkers

Berardo et al. give both analytes with onset-band-dependent magnitudes and reference ranges `[REVIEW/SYNTHESIS]`:

| Biomarker | Early onset | Childhood/late onset | Reference range |
|---|---|---|---|
| **GDF-15** | > 10,000 pg/mL | > 1,000 pg/mL | ≤ 750 pg/mL |
| **FGF-21** | > 1,000 pg/mL | 100–1,000 pg/mL | < 350 pg/mL |

— PMID:35094997

**GDF-15 is the more informative of the two**, with both a larger dynamic range and a clearer separation from reference. Both track disease severity and onset band rather than being simply present-or-absent, which makes them plausible — though not validated — treatment-response measures. Neither is specific to TK2d; both are general mitochondrial-disease biomarkers.

I could not resolve ontology identifiers for GDF-15, FGF-21, or a creatine-kinase *analyte* term (as distinct from the `NCIT:C64489` measurement procedure) from the available caches; see §16.

---

## 10. Management and Surveillance

Management is multidisciplinary and, apart from nucleoside therapy (§12), entirely supportive. GeneReviews provides the only structured guidance `[REVIEW/SYNTHESIS]`:

> "Treatment of manifestations: Management should involve a multidisciplinary team. Feeding difficulties should be managed aggressively, including use of a nasogastric tube or gastrostomy tube when the risk for aspiration is high. Physical therapy can help maintain muscle function; a physical medicine and rehabilitation (PM&R) specialist can help those who have difficulty walking. A pulmonologist can oversee chest physiotherapy to improve pulmonary function, reduce the risk of pulmonary infection, and manage respiratory insufficiency, if present. Hearing loss and seizures are managed in a standard manner. Prevention of secondary complications: Chest physiotherapy can help reduce the risk of pulmonary infection; physical therapy can help prevent joint contractures."
> — PMID:23230576

**Surveillance recommendations, and the important caveat.** GeneReviews is explicit that no guideline exists:

> "Surveillance: No clinical guidelines are available. Treating physicians should consider: routine evaluation of growth and weight, pulmonary function tests with consideration of blood gases, neurodevelopmental assessments at each visit, and at least annual audiology evaluations in those with infantile-onset disease."
> — PMID:23230576

These are expert suggestions, not evidence-based intervals. Given that **every death in the largest cohort was respiratory** (§11), the case for prioritising serial pulmonary function testing — including supine FVC and nocturnal hypoventilation assessment — over other surveillance is strong on mechanistic grounds, though no trial supports a specific schedule.

**Interventions and their ontology terms:**

| Intervention | Term | Notes |
|---|---|---|
| Mechanical / non-invasive ventilation | `NCIT:C70909` Mechanical Ventilation | Required by 55–67% depending on band |
| Gastrostomy | `NCIT:C157864` Gastrostomy Tube Procedure | ~30% of adult-onset, mean 19.6 y post-onset |
| Physical therapy | `NCIT:C15302` Physical Therapy | Maintain function, prevent contracture |
| Occupational therapy | `NCIT:C121351` Occupational Therapy | — |
| Nutritional support | `NCIT:C15433` Nutritional Support | Failure to thrive, dysphagia |
| Supportive care | `NCIT:C15747` Supportive Care | Umbrella |
| Genetic counselling | `NCIT:C15240` Genetic Counseling | §13 |
| Pharmacotherapy | `NCIT:C15986` Pharmacotherapy | Nucleoside therapy, §12 |
| Gene therapy | `NCIT:C15238` Gene Therapy | Investigational, §12 |

Targeted phenotypes for these interventions: `HP:0002093` Respiratory insufficiency, `HP:0002015` Dysphagia, `HP:0001508` Failure to thrive, `HP:0003701` Proximal muscle weakness.

**Not established:** anaesthetic risk protocols, exercise prescription (versus avoidance), immunisation or infection-prophylaxis policy beyond general neuromuscular practice, pregnancy management, and whether any conventional "mitochondrial cocktail" (coenzyme Q10, riboflavin, carnitine) alters course — no trial addresses this in TK2d.

---

## 11. Prognosis

**The cause of death is singular.** The Spanish cohort's mortality data are the most informative prognostic dataset available `[HUMAN CLINICAL]`:

> "Approximately 30% of patients died of respiratory insufficiency, while 56% of surviving patients needed mechanical ventilation."
> — PMID:38544965

By the September 2023 census, **16 of 53 patients (30%) had died, all of respiratory failure**. No death in the cohort was attributed to cardiac, hepatic, renal or neurological cause. **Respiratory muscle function is therefore the prognosis**, and this single fact should organise both surveillance (§10) and trial endpoint selection.

**Onset band is the dominant prognostic variable.** **86% of untreated patients with onset before age 12 had died** (PMID:38544965). Infantile onset carries a very poor untreated prognosis; adult onset is compatible with decades of survival with ventilatory support.

**Treatment changes the picture, on observational evidence.** In the same cohort, **all 23 treated patients but one were alive** at census (PMID:38544965). This is an uncontrolled comparison in a cohort where treatment allocation correlated with era and with survival to the point of being treatable, so it cannot be read as an effect size. It is nonetheless the strongest available human survival signal for nucleoside therapy, and it is concordant with the mouse survival data (§12) and the pooled clinical data underlying the 2025 regulatory approval.

**Genotype refines timing rather than outcome.** The p.Lys202del / p.Thr108Met ventilation-onset difference (§5, *p* < 0.01) is a timing predictor of real counselling value.

**Favourable prognostic indicators:** later onset; p.Lys202del genotype; residual TK2 activity in the 14–45% range; preserved ambulation (the majority — only 16.8% non-ambulant); receipt of nucleoside therapy.

**Unfavourable:** onset before 12 years; p.Arg130Trp genotype; residual activity below 10%; CNS involvement; early ventilatory requirement.

---

## 12. Treatment, Including Investigational

TK2d is now one of the few mitochondrial disorders with a **mechanism-based, approved pharmacotherapy**. The development path is unusually clean and worth following in order, because each step tested and discarded a specific hypothesis.

### 12.1 Step 1 — deoxynucleoside monophosphates (2014)

Garone et al. treated Tk2⁻/⁻ mice with dCMP + dTMP `[MODEL ORGANISM]`:

| Dose | Survival | *p* |
|---|---|---|
| Untreated | 13.2 ± 2.5 days | — |
| 200 mg/kg/day | 34.6 ± 3.2 days | 0.0028 (n = 7) |
| 400 mg/kg/day | 44.3 ± 9.1 days | 0.0071 |

> "dCMP/dTMP supplementation is the first effective pharmacologic treatment for Tk2 deficiency."
> — Garone C, et al. *EMBO Mol Med*. 2014. PMID:24968719, DOI 10.15252/emmm.201404092

Two mechanistic observations from that paper shaped everything after it. First, **the monophosphates were undetectable after gavage** while deoxythymidine and deoxyuridine rose instead — implying the **nucleosides, not the monophosphates, are the active species**, which directly motivated step 2. Second, **intestinal thymidine phosphorylase activity rises by postnatal day 29** and catabolises the drug, capping efficacy. (Curiously, treatment also *raised* Tk1 activity.)

### 12.2 Step 2 — deoxynucleosides, and the refutation of THU (2017)

Lopez-Gomez et al. tested dC + dT directly, and tested tetrahydrouridine (THU) as a catabolism inhibitor `[MODEL ORGANISM]` `[IN VITRO]`:

| Regimen | Survival |
|---|---|
| dC+dT 260 mg/kg/day | P31 ± 4 |
| dC+dT 520 mg/kg/day | P43 ± 10 |
| dC+dT + THU | 30 ± 1 (vs 44 ± 7 without THU, *p* = 0.007) |

> "double the molar amounts of nucleoside relative to deoxynucleoside monophosphates were required in order to achieve the same prolongation of lifespan."
>
> "our results reveal a novel nucleoside therapy and refute the hypothesized therapeutic effect of THU for TK2 deficiency."
> — Lopez-Gomez C, et al. *Ann Neurol*. 2017. PMID:28318037

**THU shortened survival.** This is a clear negative result and worth recording as such: a plausible pharmacological adjuvant made the outcome worse.

The same paper reattributed the persistent **failure to rescue brain** to **catabolism rather than blood–brain-barrier closure**, noting that ENT1 and ENT2 do transport dT and dC. It also found the **intestine uniquely maintained mtDNA at 82–86%** of normal — consistent with continued proliferation there keeping TK1 active, i.e. a natural experiment confirming the §6.1 step-3/4 masking mechanism.

### 12.3 Step 3 — compassionate use in humans

Berardo et al. summarise the human compassionate-use experience `[HUMAN CLINICAL]` `[REVIEW/SYNTHESIS]`: **16 patients**, doses up to **400 mg/kg/day**, with **diarrhoea and transaminase elevation the only notable adverse events**. Functional outcomes: **ventilation discontinued in 2 of 4**, **gastrostomy discontinued in 2 of 3**, and **two patients regained the ability to walk** (PMID:35094997). The primary report is PMID:31125140 (Domínguez-González et al., *Ann Neurol* 2019), which I did not read in full for this report.

Regaining ambulation in a progressive mitochondrial myopathy is a substantial claim and, if it holds, indicates the disorder has a reversible component — presumably restoration of dNTP supply to surviving fibres rather than regeneration of lost ones.

### 12.4 Step 4 — trial and approval

Compassionate use was followed by formal development as **MT1621** (Modis Therapeutics / Zogenix), trial **NCT03845712** (PMID:35094997). This culminated in the **November 2025 regulatory approval of doxecitine (deoxycytidine) and doxribtimine (deoxythymidine)** for TK2 deficiency — the first approved therapy for the disorder, and, notably, an approval for a *substrate-enhancement* strategy rather than gene or enzyme replacement (PMID:41604077) `[HUMAN CLINICAL]`.

That record contains dosing, pharmacokinetic and pooled survival data. I read it in the prior session but do not hold the specific dose, PK parameter and survival figures in a form I can reproduce verbatim here, and so I do not state them — they should be read from the source before use. **One cache caveat for anyone quoting it:** its properties table contains a typographical inconsistency, reading ">1% of unchanged drug excreted in urine" where the body text says "Less than 1%". **The body text is correct; the table string must not be quoted.**

**Treatment curation pattern** for the approved therapy:

```yaml
treatment_term:
  preferred_term: Pharmacotherapy
  term:
    id: NCIT:C15986
    label: Pharmacotherapy
  therapeutic_agent:
  - preferred_term: deoxycytidine
    term:
      id: CHEBI:15698
      label: 2'-deoxycytidine
  - preferred_term: thymidine
    term:
      id: CHEBI:17748
      label: thymidine
```

### 12.5 Gene therapy (investigational)

AAV-mediated *TK2* gene transfer has been tested in the mouse `[MODEL ORGANISM]`. Berardo et al. report that **AAV9-TK2 rescued Tk2 activity in all tissues except kidney**, and that **AAV9 + AAV2 combined with dC/dT was synergistic** (PMID:35094997); the primary report is PMID:34338329, which I did not read in full. Term: `NCIT:C15238` Gene Therapy.

The synergy observation is mechanistically sensible — gene therapy restores the enzyme where transduction reaches, and nucleoside supplementation covers tissues it does not.

### 12.6 Untested rational target

Dorado et al. proposed **MTERF3 inhibitors** as a therapeutic class, on the logic that enhancing the endogenous transcriptional compensation (§6.1 step 8) could raise the mtDNA depletion threshold without touching nucleotide supply (PMID:20940150). I find no evidence this has been pursued. It remains the most clearly articulated untested therapeutic hypothesis in the disorder.

---

## 13. Genetic Counselling

GeneReviews gives the counselling content `[REVIEW/SYNTHESIS]`:

> "TK2-related mtDNA maintenance defect is inherited in an autosomal recessive manner. Each sib of an affected individual has a 25% chance of being affected, a 50% chance of being an asymptomatic carrier, and a 25% chance of being unaffected and not a carrier. Carrier testing for at-risk family members and prenatal testing for a pregnancy at increased risk are possible if the pathogenic variants in the family have been identified."
> — PMID:23230576

Inheritance term: `HP:0000007` Autosomal recessive inheritance.

**Counselling points specific to TK2d, beyond generic autosomal recessive counselling:**

1. **Expressivity within a genotype is wide.** A sibling inheriting the same biallelic genotype may have a materially different onset age. The p.Thr108Met homozygote group in the Spanish cohort spans onset bands. Counselling should not promise a sibling's course from the index case's.
2. **Genotype does predict ventilatory timing.** For the two founder alleles, the ventilation-onset association (*p* < 0.01) supports concrete anticipatory guidance: p.Lys202del homozygotes were ventilated only after 40; p.Thr108Met homozygotes mostly between 12 and 40 (PMID:38544965).
3. **Founder-population carrier risk is elevated.** In Iberian and Iberian-descended families, carrier frequencies for p.Thr108Met (0.062% Spanish, 0.176% Galicia) and p.Lys202del (0.034%) are 13- to 86-fold above gnomAD global. Reproductive counselling and partner carrier testing have a higher yield in these populations than global figures suggest (PMID:38544965).
4. **Treatment availability changes the conversation.** With an approved therapy (§12.4) and the observational survival signal (all but one of 23 treated Spanish patients alive), the prognostic counselling given before 2019 is no longer accurate. Early molecular diagnosis is now actionable, which strengthens the case for prenatal and newborn-relevant testing where a familial genotype is known.
5. **Pre-symptomatic mtDNA loss** in the mouse (§6.2) argues that a molecularly diagnosed but asymptomatic sibling is not necessarily unaffected at the tissue level — a consideration for surveillance rather than a basis for treating.

**Not established:** whether pre-symptomatic nucleoside therapy in a molecularly diagnosed asymptomatic individual is beneficial; newborn screening feasibility or candidacy; and any formal reproductive-option guidance (PGT-M, donor gametes) specific to TK2d.

---

## 14. Differential Diagnosis

Berardo et al. provide an age-banded differential grid (PMID:35094997) `[REVIEW/SYNTHESIS]`; the curated dismech entry binds the following differentials, all with validated MONDO terms:

| Differential | MONDO term | Discriminating features |
|---|---|---|
| Spinal muscular atrophy | `MONDO:0001516` spinal muscular atrophy | The key infantile mimic. TK2d biopsy shows **SMA-like fibre grouping with type 1 predominance**, so histology can mislead; *SMN1* testing and mtDNA quantification separate them |
| Facioscapulohumeral muscular dystrophy | `MONDO:0001347` facioscapulohumeral muscular dystrophy | Facial weakness and scapular winging are shared; FSHD lacks CK elevation of TK2d magnitude, ragged-red/COX-negative fibres and mtDNA depletion |
| mtDNA depletion syndrome 3 (hepatocerebral) | `MONDO:0009636` | *DGUOK*; hepatic failure dominant, muscle spared |
| mtDNA depletion, encephalomyopathic with methylmalonic aciduria | `MONDO:0012791` | *SUCLA2*/*SUCLG1*; methylmalonic aciduria is the discriminator |
| MNGIE | `MONDO:0017575` mitochondrial neurogastrointestinal encephalomyopathy | *TYMP*; also a nucleoside-pool disorder, but with GI dysmotility, leukoencephalopathy and raised plasma thymidine |
| Mitochondrial myopathy–cerebellar ataxia–pigmentary retinopathy | `MONDO:0044714` | Ataxia and retinopathy absent in TK2d |

**Additional differentials to consider** (concepts named; MONDO identifiers not resolved in this session — see §16): limb-girdle muscular dystrophies (the commonest adult misdiagnosis, given proximal weakness and high CK); congenital myopathies; Pompe disease (proximal weakness with early diaphragmatic failure — a particularly close mimic of the TK2d respiratory pattern); other *POLG*-, *TWNK*- and *RRM2B*-related mtDNA maintenance disorders; single-large-deletion CPEO and Kearns–Sayre syndrome (for the adult ptosis/CPEO presentation); myasthenia gravis and congenital myasthenic syndromes (ptosis and bulbar weakness, but fatigable and with a decrement on repetitive stimulation).

**The discriminating triad that should trigger *TK2* testing:** axial/cervical and facial weakness out of proportion to limb weakness, respiratory involvement out of proportion to ambulatory loss, and in adults, ptosis. Add elevated CK with mitochondrial *and* dystrophic changes on biopsy.

---

## 15. Model Systems

### 15.1 Mouse models

Two mouse models were published in 2008 and both are informative and both are limited.

- **Tk2 H126N knockin** — the mouse equivalent of human p.His121Asn, a kinetically characterised partial-function allele (Akman et al. 2008, PMID:18467430). I did not read this record in full.
- **Tk2 knockout (Tk2⁻/⁻)** — the model used for the mechanistic work in PMID:20940150 and the therapeutic work in PMID:24968719 and PMID:28318037.

Berardo et al. record the critical limitation directly `[REVIEW/SYNTHESIS]`:

> Both models died at **14–16 days**, none survived past **30 days**, and *"both mouse models did not reproduce the human myopathic phenotype."*
> — PMID:35094997

This is a **species/phenotype mismatch of the kind dismech records as `FAILS_TO_RECAPITULATE` or `PARTIALLY_RECAPITULATES` with explicit limitations**, and it must be stated whenever mouse data are cited for a human claim. The mice die of an encephalopathic course in under three weeks; human myopathic TK2d is a myopathy that in the majority of patients begins after age 12. Any mouse survival endpoint is therefore an **upward extrapolation** from a model observing a different phenotype.

What the models *do* recapitulate, and what they legitimately support:
- The TK1/TK2 developmental hand-off and its tissue-timing consequences (PMID:20940150) — this is a cell-biological mechanism, well served by the model.
- The dTTP-selective nucleotide pool defect with dCTP sparing (PMID:20940150).
- MTERF3-mediated transcriptional compensation and the depletion threshold (PMID:20940150).
- **Dose-responsive rescue by deoxynucleoside supplementation** (PMID:24968719, PMID:28318037) — the model's most valuable contribution, and one whose translation to humans has since been confirmed clinically, which retrospectively validates its use for this specific purpose.
- The negative THU result (PMID:28318037).
- AAV9/AAV2 gene-therapy proof of concept, and its kidney gap (PMID:34338329, via PMID:35094997).

What they do not support: any claim about human age of onset, the myopathic distribution of weakness, ptosis/CPEO, or the qualitative (multiple-deletion) arm of the mechanism.

**Model-link curation pattern** for dismech: the Tk2⁻/⁻ mouse linked to a `Mitochondrial dNTP Pool Imbalance` or `mtDNA Depletion` node would be `RECAPITULATES` with `fidelity: MODERATE` and `model_scale: ORGANISM`; the same model linked to a clinical myopathy node would be `FAILS_TO_RECAPITULATE` with `limitations` naming the 14–16-day encephalopathic death and the absent myopathic phenotype, and a `divergences` entry of type `INCOMPLETE_PHENOTYPE` or `SPECIES_MISMATCH`.

### 15.2 In vitro systems

- **Recombinant TK2 enzymology** — the workhorse for genotype-to-activity mapping. Wang, Saada and Eriksson's mutant kinetics (PMID:12493767) is the reference dataset; the substrate-specific kinetics (Michaelis–Menten for dC, negative cooperativity for dT; PMID:28318037) came from the same approach.
- **Patient fibroblasts and myoblasts** — Saada et al.'s tissue-activity comparisons (PMID:12765840) underpin the muscle-selectivity argument. Note the mechanistic trap: **proliferating patient cells express TK1 and therefore mask the defect**, so a fibroblast assay can be misleadingly normal. Differentiated myotubes (`CL:0002372`) are the appropriate cellular model, and this is a direct corollary of §6.1 step 3.

### 15.3 Gaps in the model landscape

No published model, to my knowledge from these sources, reproduces the **late-onset, multiple-deletion** arm of the disorder — which is the majority phenotype in an unselected cohort (60.3% onset >12 years). Neither is there a model of the ptosis/CPEO presentation. A hypomorphic allelic series with survival into adulthood, or a muscle-restricted conditional knockout with delayed induction, would address a real gap. Patient-derived iPSC myotube systems are an obvious candidate and I found no record of one in these sources.

---

## 16. Explicit Statements of Unavailable Information

Per the template's requirement, the following were sought and **not obtained in this session**:

**Identifiers not resolved (and deliberately not supplied from memory).** The Ontology Lookup Service tool was unavailable (permission not granted), so the following have no identifier in this report: Orphanet ORPHAcode for MONDO:0012301; ICD-10-CM and ICD-11 codes; MeSH descriptor; UMLS CUI; *TK2* MIM **gene** number; MONDO terms for limb-girdle muscular dystrophy, Pompe disease, congenital myopathy, Kearns–Sayre syndrome, CPEO, myasthenia gravis and the *POLG*/*TWNK*/*RRM2B* disorders; HPO terms for cervical extensor weakness specifically, nocturnal hypoventilation, and exertional myalgia; CHEBI terms for dCTP, dTMP and dCMP (only `CHEBI:18077` dTTP, `CHEBI:17748` thymidine and `CHEBI:15698` 2'-deoxycytidine were cache-resolvable); analyte terms for GDF-15 and FGF-21; NCIT terms for non-invasive positive-pressure ventilation specifically, mtDNA copy-number quantification, and the approved agents doxecitine and doxribtimine; and MGI, IMPC or OMIA accessions for the mouse models. Every concept above is named in prose so it can be bound once a lookup is available.

**Epidemiology.** No measured prevalence or incidence exists anywhere in the literature — every figure is derived. No sex ratio. No prevalence estimate outside Spain and referral-based series. No carrier frequency in any non-Iberian population.

**Clinical.** No validated outcome measure or severity score for TK2d. No anaesthetic risk protocol. No exercise prescription evidence. No pregnancy management data. No data on whether conventional mitochondrial supplement cocktails alter course.

**Surveillance.** GeneReviews states directly that *"No clinical guidelines are available"*; the listed items are expert suggestion, with no evidence-based intervals.

**Treatment.** Specific dose, pharmacokinetic and pooled-survival figures from the 2025 approval record (PMID:41604077) are present in the cache but not reproduced here, as I do not hold them verbatim — read them from the source. No controlled trial data on nucleoside therapy were located (the human evidence is compassionate-use and single-arm). No data on pre-symptomatic treatment. MTERF3 inhibition remains an untested proposal. Long-term (>5 year) safety data on nucleoside therapy were not located.

**Mechanism.** The route from dNTP imbalance specifically to **multiple deletions** rather than depletion is inferred, not demonstrated. The cause of **intra-genotypic variability in onset age** is unknown. Why kidney resists AAV9-TK2 rescue is unexplained.

**Models.** No model of late-onset, multiple-deletion TK2d. No iPSC-derived myotube model located. Both mouse models are explicitly stated not to reproduce the human myopathic phenotype.

**References in the cache that I did not read in full for this report**, and from which I therefore quoted nothing: PMID:18467430 (Akman, H126N knockin mouse), PMID:34338329 (AAV9 gene therapy), PMID:23932787 (Chanprasert), PMID:22345218 (Béhin, adult cases), PMID:33340416 (ICIMD nosology).

---

## Appendix A — Consolidated Ontology Term Set

All identifiers below were read from `cache/<prefix>/terms.csv` or from the validated bindings of `kb/disorders/Mitochondrial_DNA_Depletion_Syndrome_Myopathic_Form.yaml` in the same step they were written. None was supplied from recall.

**Disease (MONDO)**
`MONDO:0012301` mitochondrial DNA depletion syndrome, myopathic form *(primary)*
`MONDO:0009636` mitochondrial DNA depletion syndrome 3 (hepatocerebral type)
`MONDO:0012791` mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria
`MONDO:0017575` mitochondrial neurogastrointestinal encephalomyopathy
`MONDO:0044714` mitochondrial myopathy-cerebellar ataxia-pigmentary retinopathy syndrome
`MONDO:0001347` facioscapulohumeral muscular dystrophy
`MONDO:0001516` spinal muscular atrophy

**Gene (HGNC)**
`hgnc:11831` TK2

**Inheritance (HPO)**
`HP:0000007` Autosomal recessive inheritance

**Phenotype — muscle (HPO)**
`HP:0003701` Proximal muscle weakness · `HP:0003324` Generalized muscle weakness · `HP:0000467` Neck muscle weakness · `HP:0010628` Facial palsy · `HP:0003691` Scapular winging · `HP:0001252` Hypotonia · `HP:0002505` Loss of ambulation · `HP:0003198` Myopathy · `HP:0003546` Exercise intolerance · `HP:0003201` Rhabdomyolysis · `HP:0001270` Motor delay

**Phenotype — ocular / bulbar / respiratory (HPO)**
`HP:0000508` Ptosis · `HP:0000597` Ophthalmoparesis · `HP:0000590` Progressive external ophthalmoplegia · `HP:0002015` Dysphagia · `HP:0001260` Dysarthria · `HP:0002093` Respiratory insufficiency

**Phenotype — CNS / systemic (HPO)**
`HP:0001250` Seizure · `HP:0001298` Encephalopathy · `HP:0002376` Developmental regression · `HP:0000407` Sensorineural hearing impairment · `HP:0001508` Failure to thrive

**Phenotype — laboratory / histopathology (HPO)**
`HP:0003236` Elevated circulating creatine kinase activity · `HP:0002151` Increased circulating lactate concentration · `HP:0009141` Depletion of mitochondrial DNA in muscle tissue · `HP:0003689` Multiple mitochondrial DNA deletions · `HP:0003200` Ragged-red muscle fibers · `HP:0003688` Cytochrome C oxidase-negative muscle fibers · `HP:0008347` Decreased activity of mitochondrial complex IV · `HP:0003803` Type 1 muscle fiber predominance

**Biological process / molecular function (GO)**
`GO:0004797` thymidine kinase activity · `GO:0004137` deoxycytidine kinase activity · `GO:0043099` pyrimidine deoxyribonucleoside salvage · `GO:0009202` deoxyribonucleoside triphosphate biosynthetic process · `GO:0006264` mitochondrial DNA replication · `GO:0032042` mitochondrial DNA metabolic process · `GO:0006390` mitochondrial transcription · `GO:0007005` mitochondrion organization · `GO:0006119` oxidative phosphorylation · `GO:0022904` respiratory electron transport chain

**Cell type (CL)**
`CL:0008002` skeletal muscle fiber · `CL:0002372` myotube · `CL:0000594` skeletal muscle satellite cell · `CL:0000189` slow muscle cell · `CL:0000190` fast muscle cell · `CL:0000540` neuron · `CL:0000182` hepatocyte *(spared — contrast term)*

**Anatomy (UBERON)**
`UBERON:0001134` skeletal muscle tissue · `UBERON:0001103` diaphragm

**Chemical entity (CHEBI)**
`CHEBI:17748` thymidine · `CHEBI:15698` 2'-deoxycytidine · `CHEBI:18077` dTTP

**Clinical intervention / procedure (NCIT)**
`NCIT:C15986` Pharmacotherapy · `NCIT:C15238` Gene Therapy · `NCIT:C70909` Mechanical Ventilation · `NCIT:C157864` Gastrostomy Tube Procedure · `NCIT:C15302` Physical Therapy · `NCIT:C121351` Occupational Therapy · `NCIT:C15433` Nutritional Support · `NCIT:C15240` Genetic Counseling · `NCIT:C15747` Supportive Care · `NCIT:C51895` Muscle Biopsy · `NCIT:C101295` Whole Exome Sequencing · `NCIT:C64489` Creatine Kinase Measurement

---

## Appendix B — Reference List with Evidence Typing

| PMID | Citation | DOI | Evidence type | Read in full |
|---|---|---|---|---|
| 11687801 | Saada A, et al. *Nat Genet*. 2001. Gene discovery | — | HUMAN CLINICAL / IN VITRO | Yes (prior session) |
| 12493767 | Wang L, Saada A, Eriksson S. *J Biol Chem*. 2003. Mutant enzyme kinetics | 10.1074/jbc.M206143200 | IN VITRO | Yes (abstract-only record) |
| 12765840 | Saada A, Shaag A, Elpeleg O. *Mol Genet Metab*. 2003. Tissue specificity | 10.1016/s1096-7192(03)00063-5 | HUMAN CLINICAL / IN VITRO | Yes (abstract-only record) |
| 18467430 | Akman HO, et al. 2008. Tk2 H126N knockin mouse | — | MODEL ORGANISM | No |
| 20940150 | Dorado B, Area E, Akman HO, Hirano M. *Hum Mol Genet*. 2011. TK1 unmasking, MTERF3, depletion threshold | 10.1093/hmg/ddq453 | MODEL ORGANISM | Yes (full PMC) |
| 22345218 | Béhin A, et al. Adult cases | — | HUMAN CLINICAL | No |
| 23230576 | GeneReviews. TK2-related mtDNA maintenance defect, myopathic form | — | REVIEW/SYNTHESIS | Yes (abstract-only record) |
| 23932787 | Chanprasert S, et al. Molecular/clinical | — | HUMAN CLINICAL | No |
| 24968719 | Garone C, et al. *EMBO Mol Med*. 2014. dCMP/dTMP therapy | 10.15252/emmm.201404092 | MODEL ORGANISM | Yes (full PMC) |
| 28318037 | Lopez-Gomez C, et al. *Ann Neurol*. 2017. dC/dT therapy; THU refuted | 10.1002/ana.24922 | MODEL ORGANISM / IN VITRO | Yes (full PMC) |
| 29602790 | Garone C, et al. 2018. Natural history | — | HUMAN CLINICAL | Yes (prior session) |
| 31060578 | Domínguez-González C, et al. 2019. Late-onset series | — | HUMAN CLINICAL | Yes (prior session) |
| 31125140 | Domínguez-González C, et al. *Ann Neurol*. 2019. Compassionate use | — | HUMAN CLINICAL | Yes (prior session) |
| 33340416 | ICIMD nosology | — | REVIEW/SYNTHESIS | No |
| 34338329 | AAV9 TK2 gene therapy + deoxynucleoside synergy | — | MODEL ORGANISM | No |
| 35094997 | Berardo A, Domínguez-González C, Engelstad K, Hirano M. *J Neuromuscul Dis*. 2022. Comprehensive review | 10.3233/JND-210786 | REVIEW/SYNTHESIS | Yes (full PMC + Table 1) |
| 38544965 | Ceballos A (Ceballos-Ceballos), et al. *Neurol Genet*. 2024. 53-patient Spanish cohort | 10.1212/NXG.0000000000200138 | HUMAN CLINICAL / COMPUTATIONAL | Yes (full PMC + Tables 1–2) |
| 41604077 | 2025. Doxecitine / doxribtimine regulatory approval | — | HUMAN CLINICAL | Yes (prior session) |

**Recency note.** The template asked for prioritisation of 2023–2024+ sources. The two most recent references are the 2024 Spanish cohort (PMID:38544965) and the 2025 approval record (PMID:41604077), and both are load-bearing here — the former for §3, §4, §5, §7, §9 and §11, the latter for §12.4. The 2022 Berardo review (PMID:35094997) is the most recent comprehensive synthesis. The mechanistic core (§6) rests on 2003–2017 work, because that is when it was established and no later source supersedes it; the MTERF3 compensation mechanism in particular has, so far as these sources show, neither been replicated nor extended since 2011, which is itself worth noting as a gap.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 72 |
| Resolved | 72 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0009636` (2 mentions) - the report calls it "mtDNA depletion syndrome 3 (hepatocerebral)"; MONDO calls it **mitochondrial DNA depletion syndrome 3 (hepatocerebral type)**
- `MONDO:0012791` (2 mentions) - the report calls it "mtDNA depletion, encephalomyopathic with methylmalonic aciduria"; MONDO calls it **mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria**, and lists "mtDNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria" among its other names
- `MONDO:0044714` (2 mentions) - the report calls it "Mitochondrial myopathy–cerebellar ataxia–pigmentary retinopathy"; MONDO calls it **mitochondrial myopathy-cerebellar ataxia-pigmentary retinopathy syndrome**

Every term resolved, and every label the report gave matched.