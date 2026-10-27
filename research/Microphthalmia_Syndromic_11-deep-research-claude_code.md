---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T15:57:40.275700'
end_time: '2026-10-12T15:59:03.057032'
duration_seconds: 82.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: microphthalmia, syndromic 11
  mondo_id: ''
  category: ''
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
  - claude-sonnet-5-5
  web_search_requests: 7
  num_turns: 11
  total_cost_usd: 0.8173228000000001
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** microphthalmia, syndromic 11
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **microphthalmia, syndromic 11** covering all of the
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

I'll start by loading the search tool and confirming the gene and identifiers.

# Research report: microphthalmia, syndromic 11 (MCOPS11)

**Evidence base and limits.** This report rests on one human discovery paper (Slavotinek et al. 2012), the Vax1 knockout mouse papers (1999), and database summaries. The search tools returned abstracts and aggregator pages, not full texts. PMC returned a bot-verification page, so I could not read the Slavotinek full text.

- **Not verified:** anything beyond the abstract-level facts is marked *unverified* below. That includes the full patient phenotype, population frequencies, and Orphanet and ClinGen status.
- **Ontology IDs:** I give ontology term names only, without CURIEs. Look each one up before binding it; none was looked up in this session.
- **Missing search results:** the searches found no 2023–2024 VAX1 case reports. Variant-level and recent literature are therefore thin.

## 1. Disease information

- **Disease:** MCOPS11 is a very rare autosomal recessive syndromic microphthalmia caused by loss of function of the homeobox transcription factor VAX1 (10q25.3). Reported features are microphthalmia with small optic nerves, cleft lip and palate, absent corpus callosum, hippocampal malformations and absent pineal gland. The disease description is from [Phenodis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/11859) and [Malacards](https://malacards.org/card/microphthalmia_syndromic_11_2).
- **Identifiers:**
  - OMIM 614402 (per [LOVD](https://databases.lovd.nl/shared/diseases/03632)).
  - MONDO:0013734 (taken from a URL in the search results, [concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0013734/)).
  - Disease Ontology DOID:0111804 ([DO](https://disease-ontology.org/term/DOID:0111804)).
  - Orphanet, ICD-10/11 and MeSH identifiers were not retrieved.
- **Synonyms:** MCOPS11; VAX1 syndromic microphthalmia; microphthalmia, syndromic 11. LOVD also lists the older "MCOPCB11" abbreviation.
- **Data level:** the information comes from an aggregated, literature-derived resource (OMIM) built on a single published proband. It is not EHR-derived.
- **Note on the 2012 paper's title:** it frames the condition as "microphthalmia, corpus callosum agenesis and orofacial clefting".

## 2. Etiology

- **Cause:** biallelic VAX1 variants. The Disease Ontology gives the material basis as homozygous or compound heterozygous VAX1 mutation. Only one homozygous missense case has been reported in the literature I could access.
- **Discovery paper:** Slavotinek et al. (Hum Mutat 2012;33:364–368, PMID 22095910, [record](https://www.zfin.org/ZDB-PUB-111122-28)). The authors sequenced the coding exons of VAX1 and VAX2 in 70 patients with anophthalmia/microphthalmia.
- **Environmental risk and protective factors:** none known. No gene–environment interaction data were found.
- **Related common-variant signal:** a VAX1-region locus (10q25.3) is associated with nonsyndromic cleft lip with or without cleft palate.
  - Mangold et al. (Nat Genet 2010) reported lead SNP rs7078160, combined P = 1.92 × 10⁻⁸. The PMID was not retrieved.
  - Beaty et al. 2010 flagged VAX1 as approaching genome-wide significance.
  - A 2012 resequencing study (384 cases, 384 controls) found no significant excess of functional rare variants in cases (p = 0.17).
  - Replication in Chinese cohorts is inconsistent. The secondary source is an [Open Dentistry Journal paper](https://opendentistryjournal.com/VOLUME/19/ELOCATOR/e18742106419313) and the others came from search snippets.
  - This is a susceptibility signal, not MCOPS11 causation. Do not conflate the two.

## 3. Phenotypes

Source for the main set: Phenodis/Malacards and the Slavotinek abstract. HPO term names are suggestions only.

| Phenotype | Suggested HPO term name | Frequency / notes |
|---|---|---|
| Microphthalmia (severe, bilateral in the proband, per Phenodis) | Microphthalmia | Present in the single reported proband |
| Small optic nerves | Optic nerve hypoplasia | Present in the proband |
| Cleft lip and palate | Cleft lip; Cleft palate | Present in the proband |
| Absent corpus callosum | Agenesis of corpus callosum | Present in the proband |
| Hippocampal malformation | Abnormal hippocampus morphology | From Phenodis/OMIM summary; patient-level source *unverified* |
| Absent pineal gland | Absent pineal gland (name to be confirmed) | From Phenodis/OMIM summary; *unverified* |

- **Onset:** congenital (inferred from the structural malformations).
- **Progression:** malformations are static. Course and severity data are not available.
- **Quality of life:** no data.
- **Frequencies:** with one reported proband, no population frequencies can be given.
- **Mouse-derived additional signals** (not human phenotypes):
  - Hypogonadotropic hypogonadism and subfertility appear in mouse Vax1 loss in GnRH neurons and in heterozygotes. They are not documented in MCOPS11 patients.

## 4. Genetic and molecular information

- **Gene:** VAX1 (ventral anterior homeobox 1), 10q25.3. It encodes a transcription factor that may function in dorsoventral specification of the forebrain ([Phenodis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/11859)). The HGNC ID was not retrieved. In this knowledge base the form would be lowercase `hgnc:<n>`, to be looked up.
- **Reported variant:** homozygous c.453G>A and c.454C>A (two adjacent substitutions), predicting p.Arg152Ser.
  - The proband was of Egyptian origin.
  - The variant lies at an invariant residue of the homeodomain.
  - It was absent from 96 Egyptian controls.
  - The authors favoured loss of function, because the phenotype resembles the Vax1 null mouse.
  - No VAX2 variants were found in the cohort.
  - In silico predictions, functional assays and ClinVar classification are *unverified*.
- **Other variants:** GeneBe lists several VAX1 variants of uncertain significance dated 2023–2024 and one benign call in January 2025. These are submissions without case details and are not evidence for MCOPS11.
- **Modifier genes and epigenetics:** none known.
- **Chromosomal abnormalities:** none specific to this disorder.
- **Origin:** germline.

## 5. Environmental information

- No environmental, lifestyle or infectious contributors are documented. Mark these as not applicable or not available.

## 6. Mechanism / pathophysiology

Causal chain, with inferred steps marked:

1. A homozygous missense change at an invariant homeodomain residue (p.Arg152Ser) is the initiating lesion.
2. This is presumed to impair DNA-binding function of the VAX1 homeodomain, which is the authors' loss-of-function interpretation. It is *inferred, not demonstrated*, because the abstract reports no functional assay.
3. Loss of VAX1 function disrupts ventral forebrain, optic stalk and optic nerve patterning. In mouse, Vax1 loss expands Pax6 and Rx activity proximally in the optic cup and stalk ([Hallonet et al. 1999, PMID 10601036](https://genesdev.cshlp.org/content/13/23/3106.abstract)).
4. Two downstream branches follow:
   - **Eye branch:** failed optic fissure and disc closure, optic nerve dysgenesis and coloboma, leading to small eyes and small optic nerves. Mouse data: Bertuzzi et al. 1999 (PMID 10601035) report optic disks that fail to close.
   - **Midline and brain branch:** defective axon guidance across midline commissures (corpus callosum, hippocampal and anterior commissures) leading to callosal agenesis, and abnormal basal forebrain development leading to hippocampal and pineal defects. Mouse null data support the commissural defects; the human hippocampal and pineal findings are from summaries only.
5. A craniofacial branch leads to cleft palate. The mouse null shows cleft palate (Hallonet). The human cleft lip fits with the common-variant association at this locus.

- **Candidate GO biological processes:** forebrain development; optic nerve development; axon guidance; camera-type eye development. Candidate cell types: retinal ganglion cell, optic stalk and nerve glia, neural progenitors. All are to be confirmed against ontologies.
- **Molecular detail:** a later mouse study reports that Vax1 protein is transferred into retinal ganglion cell axons, and that a non-transferring mutant causes slow axon growth, ipsilateral-only projection, reduced visual acuity and abnormal eye-movement responses. This comes from a KAIST research-highlights page and has not been verified against the paper.
- **Omics, single-cell, spatial and screen data:** none found.

## 7. Anatomical structures affected

- **Primary:** eye (globe, optic nerve), face (lip, palate), brain (corpus callosum, hippocampus, pineal). Suggested UBERON terms: eye, optic nerve, upper lip, palate, corpus callosum, hippocampal formation, pineal body (to be looked up).
- **Lateralization:** the proband's microphthalmia is described as bilateral (Phenodis).
- **Subcellular:** nucleus, as a transcription factor.

## 8. Temporal development

- **Onset:** congenital and prenatal. The structural defects arise in early forebrain and eye development.
- **Progression and remission:** nothing documented, and nothing is expected for static malformations.
- **Critical period:** embryonic optic stalk and fissure closure, inferred from the mouse work.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (OMIM, per Phenodis).
- **Prevalence and incidence:** not available. Only one reported family is known to me.
- **Consanguinity, founder effect, sex ratio, geography:** the single proband was Egyptian. Parental consanguinity is *unverified*. No other population data exist.
- **Carrier frequency:** not assessed.

## 10. Diagnostics

- **Approach:** the literature gives no dedicated protocol, so the following is general reasoning, not a sourced guideline.
  - Include VAX1 on anophthalmia/microphthalmia gene panels and in exome or genome sequencing.
  - Use brain MRI to look for callosal agenesis, hippocampal and pineal abnormalities, and optic nerve size.
  - Do detailed ophthalmic and orofacial assessment.
- **Differential:** other syndromic microphthalmias with callosal or midline defects. Examples: SOX2, OTX2, BMP4, STRA6 and VSX2-related disease (named from general knowledge, *unverified* here).
- **Screening:** none established.

## 11. Outcome and prognosis

No data. Expected issues, inferred and not documented: visual impairment, feeding and speech problems from clefting, and neurodevelopmental effects of callosal and hippocampal anomalies.

## 12. Treatment

- No disease-specific therapy. Management is supportive and surgical: cleft repair, ophthalmic and low-vision care, developmental support.
- No pharmacogenomics, gene therapy or clinical trials were identified.
- Suggested NCIT intervention terms, to be looked up: Surgical Procedure, Supportive Care, Rehabilitation, Genetic Counseling.

## 13. Prevention

- Genetic counseling with 25% recurrence risk for carrier parents follows from autosomal recessive inheritance. This is an inference, not a sourced statement.
- Prenatal and preimplantation testing are possible once the familial variants are known.
- No primary prevention measures are known.

## 14. Other species

- Natural disease: nothing found. I did not search OMIA.
- Orthologs exist in mouse; other species were not checked.

## 15. Model organisms

- **Mouse Vax1 null** ([Hallonet et al. 1999, PMID 10601036](https://genesdev.cshlp.org/content/13/23/3106.abstract)):
  - Optic nerve dysgenesis, coloboma, basal telencephalon defects and lobar holoprosencephaly.
  - Craniofacial malformations including cleft palate, and growth defects.
  - Evidence type: MODEL_ORGANISM.
- **Mouse Vax1 null, axon guidance** (Bertuzzi et al. 1999, PMID 10601035):
  - Optic disks fail to close, giving coloboma.
  - Retinal axons fail to form an optic chiasm.
  - Axons of the corpus callosum and the hippocampal and anterior commissures fail to cross the midline.
- **Fidelity to human disease:**
  - The mouse recapitulates the eye, nerve, midline and cleft features. This is why the human variant was interpreted as loss of function.
  - It also shows holoprosencephaly, which was not reported in the human proband. This is a possible human–model mismatch.
- **Vax2:** homozygous null mice have rare, milder colobomas, and Vax1/Vax2 double mutants have severe, fully penetrant colobomas (secondary, from the Slavotinek-related summary).
- **Other mouse findings:**
  - Conditional Vax1 deletion in GnRH neurons gave a 99% drop in GnRH expression, with delayed puberty, hypogonadism and infertility.
  - Heterozygotes showed reduced sperm motility and subfertility.
  - These come from PMC4804008, PMC5287408 and an unnamed dissertation; I did not read the primary text.
- Zebrafish and other models were not searched. ZFIN lists the Slavotinek paper.

## Key citations

- Slavotinek A et al. Hum Mutat 2012;33:364–368. PMID 22095910, DOI 10.1002/humu.21658. [ZFIN record](https://www.zfin.org/ZDB-PUB-111122-28).
- Hallonet M et al. Genes Dev 1999;13:3106. PMID 10601036. [Abstract](https://genesdev.cshlp.org/content/13/23/3106.abstract).
- Bertuzzi S et al. Genes Dev 1999. PMID 10601035.
- Mangold E et al. Nat Genet 2010;42:24–26 (VAX1-region cleft lip locus). PMID not retrieved.
- Database summaries: [Phenodis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/11859), [Malacards](https://malacards.org/card/microphthalmia_syndromic_11_2), [LOVD](https://databases.lovd.nl/shared/diseases/03632), [Disease Ontology](https://disease-ontology.org/term/DOID:0111804).

## Items to verify before curation

1. Full text of PMID 22095910: exact phenotype, consanguinity, and source of the hippocampal and pineal findings.
2. Exact HPO, UBERON, GO, CL and NCIT CURIEs.
3. ClinVar and ClinGen status for VAX1, and Orphanet and GeneReviews coverage.
4. Any further VAX1 families reported after 2012.
5. PMIDs for Mangold 2010 and Beaty 2010.
6. Whether the mouse holoprosencephaly is a genuine mismatch with the human phenotype.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.