---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-09-29T21:56:45.665531'
end_time: '2026-09-29T21:58:17.194106'
duration_seconds: 91.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe Congenital Neutropenia 7, Autosomal Recessive
  mondo_id: MONDO:0014865
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
  - claude-sonnet-5-5
  web_search_requests: 5
  num_turns: 11
  total_cost_usd: 0.9452969999999997
  session_id: 70c7a523-9294-5481-860a-3eabfc5c8c41
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:24753537
  - PMID:34778134
  relevance_assessed: 10
  on_topic: 9
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 9
  verified: 9
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
- **Disease Name:** Severe Congenital Neutropenia 7, Autosomal Recessive
- **MONDO ID:** MONDO:0014865 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe Congenital Neutropenia 7, Autosomal Recessive** covering all of the
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

Still researching. I have the Triot 2014 paper, the Zhou 2021 case report and review, and the mouse knockout, so I'm writing the report now.

# Severe Congenital Neutropenia 7, Autosomal Recessive (SCN7): research report

**Verification status.** Everything cited below with a PMID or URL was seen in this session's searches, except the items in the closing "Unverified" list. I did not open the ClinGen, gnomAD, OMIM, OMIA or MGI records. Values there are marked "not verified" and need a lookup before curation. CURIEs were not looked up in OAK, so treat all suggested ontology terms as leads only.

## 1. Disease information

**Overview.** SCN7 is an autosomal recessive primary immunodeficiency caused by biallelic loss-of-function variants in *CSF3R*, which encodes the G-CSF receptor. It presents in infancy or early childhood with recurrent bacterial infections and profound peripheral neutropenia. Bone marrow shows full myeloid maturation, and neutropenia is typically refractory to recombinant human G-CSF (rhG-CSF). Some patients respond to GM-CSF.
- Sources: [LOVD disease entry](https://databases.lovd.nl/shared/diseases/06009); [NORD/MONDO entry](https://rarediseases.org/mondo-disease/autosomal-recessive-severe-congenital-neutropenia-due-to-csf3r-deficiency/); [Triot 2014, PMID:24753537](https://pmc.ncbi.nlm.nih.gov/articles/PMC4055927/).

**Identifiers.**
- OMIM #617014 (per [LOVD](https://databases.lovd.nl/shared/diseases/06009)).
- The template gives MONDO:0014865. The search hit for that ID returned the NORD page titled "autosomal recessive severe congenital neutropenia due to CSF3R deficiency". The label match is plausible but I did not confirm the ID-to-label pairing in MONDO itself. Check it with OAK before binding.
- DOID:0112129, "severe congenital neutropenia 7" ([Glycosmos](https://glycosmos.org/diseases/DOID:0112129)).
- Orphanet, ICD-10/11 and MeSH: not verified.

**Synonyms.** SCN7; neutropenia, severe congenital, 7, autosomal recessive; autosomal recessive SCN due to CSF3R deficiency; G-CSFR-deficient congenital neutropenia.

**Data source.** The evidence is aggregated, published case and family reports (about 13 biallelic cases per the 2021 review). It is not EHR-derived.

## 2. Etiology

- **Cause.** Recessively inherited biallelic *CSF3R* variants (homozygous or compound heterozygous). "We describe a novel genetic SCN type in 2 unrelated families associated with recessively inherited biallelic CSF3R mutations." (PMID:24753537)
- **Heterozygous carriers.** Parents of probands had normal ANCs (Family A father 5780 and mother 7080/µL; Family B father 3000 and mother 3900/µL) (PMID:24753537).
- **Related but distinct.** Heterozygous germline *CSF3R* variants have been discussed as risk alleles for hematologic malignancy (Trottier 2020, PMID:33108454). Acquired somatic *CSF3R* truncating mutations in the cytoplasmic domain are a separate mechanism, associated with secondary AML in G-CSF-treated SCN patients (Klimiankou 2016, PMID:27270496). Both are out of scope for the SCN7 entry except as differential or context.
- **Environmental, protective and gene-environment factors.** None documented. Infection burden is the main environmental modifier of clinical course.
- **Modifier genes.** None established. Milder, hypomorphic alleles exist (see Section 4).

## 3. Phenotypes

Frequencies are qualitative because n≈13 in the literature. Suggested HP terms are leads, not verified.

| Phenotype | Notes | Suggested HP |
|---|---|---|
| Severe neutropenia | ANC <0.5×10⁹/L; onset in infancy (birth to 5 months in reported cases). Family A ANC ranged 420–2180/µL; Family B 200–1000/µL. Present in all affected. | Neutropenia; Severe congenital neutropenia |
| Recurrent bacterial infections | Pneumonia, otitis media, urinary tract infection, suppurative tonsillitis (15–30 episodes between ages 1 and 2 on rhG-CSF in one patient, PMID:34778134) | Recurrent bacterial infections; Recurrent pneumonia; Recurrent otitis media |
| Fever | Multiple hospitalizations (PMID:24753537) | Fever |
| Normal bone marrow maturation | "all patients had morphologic evidence of full myeloid cell maturation in bone marrow" | No specific term; describe in text |
| Death in infancy | One patient died at 3 months of suspected aspiration pneumonia (PMID:24753537) | Death in infancy |
| Dextrocardia | One patient. Likely incidental and not established as part of the disease. | Dextrocardia |

Phenotype range: "from severe neutropenia unresponsive to high-dose rhG-CSF treatment… to mild neutropenia that does not require active treatment" (PMID:34778134). A homozygous p.R440* patient was reported untreated with a mild phenotype (PMID:34778134). Quality-of-life data: none found.

## 4. Genetic and molecular information

**Gene.** *CSF3R* (G-CSF receptor) at 1p34.3. The HGNC ID was not verified; look it up, using the lowercase `hgnc:` form.

**Reported variants.**

| Variant | Genotype | Consequence and response | Source |
|---|---|---|---|
| c.922C>T, p.Arg308Cys | Homozygous (Family A, Turkish, consanguineous) | Altered N-glycosylation, ER retention, reduced STAT3/STAT5 phosphorylation; refractory to rhG-CSF | PMID:24753537 |
| c.948_963del (p.Gly316fsTer322) plus c.1245del (p.Gly415fsTer432) | Compound heterozygous (Family B, Spanish) | Frameshift, premature stop; refractory to rhG-CSF | PMID:24753537 |
| c.690delC (p.Met231Cysfs*32) plus c.64+5G>A | Compound heterozygous | Refractory to rhG-CSF; responded to low-dose GM-CSF | PMID:34778134 |
| c.998-2A>T plus p.W547* | Compound heterozygous | Unresponsive to G-CSF up to 110 µg/kg/d; GM-CSF response sustained for 12 years | Review in PMID:34778134 |
| c.610-611delinsAG (p.Q204R) | Homozygous | Unresponsive to G-CSF; GM-CSF responsive | Review in PMID:34778134; PMID:30499904 |
| c.1318C>T (p.R440*) | Homozygous | Mild phenotype, untreated | Review in PMID:34778134 |

A hypomorphic biallelic allele responding to G-CSF has also been reported (PMID:30028820; title only, not read).

**Functional consequence.** Loss of function, with partial function retained for p.Arg308Cys. ClinVar/ACMG classification and gnomAD frequencies: not verified. Origin is germline. Epigenetic and chromosomal abnormalities: none reported.

**Compensation.** Heterozygous parents showed elevated *CSF3R* mRNA with normal protein levels, which the authors interpret as a genetic compensation mechanism rather than nonsense-mediated decay (PMID:34778134).

## 5. Environmental information

No environmental or lifestyle factors are established. The pathogen exposure that matters is opportunistic and ordinary bacterial flora (organisms were not systematically reported in the sources I read). No specific infectious agent defines the disease, so an `infectious_agent` block is not applicable.

## 6. Mechanism and pathophysiology

**Causal chain.**
1. Biallelic *CSF3R* variants (missense affecting folding, or frameshift/splice/nonsense truncations) reduce functional G-CSFR. *Demonstrated.*
2. For p.Arg308Cys: abnormal N-glycosylation (EndoH-sensitive, unlike wild type), retention around the nucleus co-localizing with calnexin (ER), and no proper plasma-membrane localization. *Demonstrated in vitro.* Leads to reduced cell-surface receptor.
3. Reduced receptor number or function lowers G-CSF-driven STAT3/STAT5 phosphorylation. "Cells expressing the mutant receptor showed reduced phosphorylation of STAT3 and STAT5, but signal transduction was not completely abrogated." *Demonstrated in vitro.*
4. Impaired G-CSF signaling results in reduced neutrophil output or release and survival. Mouse data support this: G-CSFR-deficient mice have "decreased numbers of phenotypically normal circulating neutrophils", decreased marrow progenitors, and impaired expansion and terminal differentiation (Liu 1996, Immunity 5:491; MGI/RIKEN PMID 8934575, seen via search snippet only). *Inferred for humans.*
5. Maturation still proceeds, so bone marrow appears morphologically normal while circulating neutrophils are low. This distinguishes SCN7 from maturation-arrest forms of SCN (*ELANE*, *HAX1*). *Demonstrated morphologically; the mechanism of peripheral deficit is inferred.*
6. Neutropenia leads to impaired innate antibacterial defense, then recurrent bacterial infections, and in the worst cases death in infancy. *Clinical observation.*
7. **Branch on treatment.** rhG-CSF cannot act through a defective receptor and fails even at high dose ("up to 110 μg/kg/day", PMID:34778134). GM-CSF acts through CSF2R, bypassing G-CSFR, and can raise neutrophils ("granulocyte stimulation by GM-CSF and the activation of CSF2R"). *Demonstrated in case reports.*

**Cell types (CL leads).** Granulocyte-monocyte progenitor, myeloid progenitor, neutrophil (CL:0000775), hematopoietic stem cell.
**GO leads.** Granulocyte colony-stimulating factor signaling pathway; neutrophil differentiation / granulocyte differentiation; STAT3/STAT5-mediated signaling; positive regulation of neutrophil apoptotic process (regulation of survival). Protein processing in the ER and glycosylation are relevant for the missense allele.
**Cellular components.** ER (calnexin co-localization), plasma membrane.
**Immune involvement.** Isolated neutrophil-lineage immunodeficiency. Omics, single-cell, and functional-genomics data: none found.

## 7. Anatomical structures affected

- **Primary.** Bone marrow (UBERON:0002371) and blood, through the neutrophil lineage.
- **Secondary (infection sites).** Lungs, middle ear, tonsils, urinary tract.
- **Cells.** Myeloid progenitors and neutrophils.
- **Laterality.** Not applicable.

## 8. Temporal development

- **Onset.** Neonatal to early childhood. In reported cases, from birth to about 2.5 years at diagnosis (PMID:24753537); the Chinese patient had ANC <0.5×10⁹/L from 5 months (PMID:34778134).
- **Course.** Chronic lifelong neutropenia with episodic infections. Severity is variable, with mild neutropenia reported in some homozygous nonsense cases. No spontaneous remission reported.
- **Critical period.** Infancy, when infections can be fatal.
- **Malignant transformation.** Not reported in biallelic SCN7. Risk of secondary leukemia in classical SCN is tied to somatic *CSF3R* truncations under long-term G-CSF exposure (PMID:27270496). Because SCN7 patients do not respond to G-CSF, this has not been assessed here.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007). Parents were unaffected carriers with normal ANCs.
- **Consanguinity.** Family A was consanguineous.
- **Prevalence, incidence, founder effects, carrier frequency and sex ratio.** Not available; only about 13 biallelic cases are reported. Ancestries reported so far: Turkish, Spanish, Chinese.
- Anticipation and germline mosaicism: not applicable or not reported.

## 10. Diagnostics

- **Laboratory.** Repeated CBC with ANC <0.5×10⁹/L. Bone marrow aspirate shows normal granulocyte maturation.
- **Genetic.** *CSF3R* sequencing, gene panel, or exome. Full sequencing is needed because variants are spread across the gene and include splice-site and frameshift changes.
- **Functional.** Optional: receptor glycosylation, surface expression, and STAT3/5 signaling assays.
- **Trial of G-CSF.** Failure to respond is a diagnostic clue.
- **Differential.** *ELANE*-SCN, *HAX1* (Kostmann; the p.W44X variant is the most common cause of congenital neutropenia in Turkey, PMID:31321910), *G6PC3*, *WAS*, cyclic neutropenia, and acquired neutropenias.
- **Screening.** No newborn screening program was identified.

## 11. Outcome and prognosis

- **Survival.** Not quantified. One infant death at 3 months (suspected aspiration pneumonia); others survived with recurrent infections. Survival data are limited to case reports.
- **Complications.** Serious bacterial infections.
- **Prognostic factors.** Genotype (hypomorphic or truncating-late alleles are milder) and responsiveness to GM-CSF or G-CSF.

## 12. Treatment

- **G-CSF (rhG-CSF).** Standard for other SCN forms. Refractory in most SCN7 patients (5–110 µg/kg/d tested). NCIT leads: Pharmacotherapy `NCIT:C15986`; therapeutic agent filgrastim (look up a code).
- **GM-CSF (rhGM-CSF).** Effective in case reports:
  - Low dose 3 µg/kg/d once weekly, no infections over 6 months (PMID:34778134).
  - A 12-year course in one patient without adverse events (as summarized in PMID:34778134).
  - A patient with p.Q204R managed with GM-CSF (PMID:30499904).
  - Off-label. Modality would be `PROTEIN_REPLACEMENT` or `SMALL_MOLECULE`, and the classification needs a curator decision.
- **Supportive care.** Antibiotic treatment of infections; prophylaxis is a clinical practice question, not sourced here. NCIT leads: Supportive Care `NCIT:C15747`.
- **HSCT.** Curative in principle (NCIT:C15431 Hematopoietic cell transplantation). No SCN7-specific outcomes were found.
- **Gene therapy, clinical trials (NCT), and pharmacogenomics.** None found.
- **Adverse events.** No GM-CSF adverse events were reported in the cases above.

## 13. Prevention

- Genetic counseling with recurrence risk of 25% for carrier parents (`NCIT:C15240`).
- Prenatal or preimplantation testing is possible once the familial variants are known.
- Early diagnosis and prompt treatment of infections.
- No vaccine or environmental strategy specific to the disease.

## 14. Other species

Orthologs exist in mouse and other vertebrates (a zebrafish gene page appeared in search results; not verified). No naturally occurring animal disease was found; OMIA was not checked.

## 15. Model organisms

- **Mouse *Csf3r* knockout** (Liu 1996, PMID 8934575, from search snippet). Findings:
  - Decreased circulating neutrophils that are phenotypically normal.
  - Decreased marrow progenitors.
  - Impaired expansion and terminal differentiation of granulocyte progenitors.
  - Increased neutrophil apoptosis.
  - Fidelity is moderate to high for the neutropenia. Limitations: full null versus human hypomorphic or partial alleles, and species differences in neutrophil biology.
- **Cell models.** Heterologous expression of the wild-type and Arg308Cys receptor (PMID:24753537). Patient iPSC/organoid models: none found.
- Suggested `modeled_mechanisms` target: the neutrophil production deficit node, `RECAPITULATES` or `PARTIALLY_RECAPITULATES`.

## Unverified items to check before curation

- The MONDO:0014865 label and ID pairing.
- The HGNC ID for *CSF3R*.
- ClinVar/ClinGen classification.
- The Liu 1996 quote (verify it against the PubMed abstract for PMID 8934575).
- The Orphanet/ICD/MeSH mappings.
- The PMID:30028820 hypomorphic-allele case, which I saw only as a title.
- The 12-year GM-CSF patient details, which come from a secondary review table.
- The quotes marked as coming from PMID:34778134 came from a summarizer of the PMC full text, so re-verify them with `just fetch-reference` and `just count-verified-snippets`.

## Sources

- [Triot et al. 2014, Blood, PMID:24753537](https://pmc.ncbi.nlm.nih.gov/articles/PMC4055927/)
- [Zhou et al. 2021, Front Pediatr, PMID:34778134](https://pmc.ncbi.nlm.nih.gov/articles/PMC8585998/)
- [Yilmaz Karapinar et al. 2020, PMID:30499904](https://pubmed.ncbi.nlm.nih.gov/30499904/)
- [Hypomorphic CSF3R patient responding to G-CSF, PMID:30028820](https://pubmed.ncbi.nlm.nih.gov/30028820/)
- Klimiankou 2016, PMID:27270496; Trottier 2020, PMID:33108454 (PubMed search listing only)
- [LOVD SCN7 disease record](https://databases.lovd.nl/shared/diseases/06009)
- [NORD/MONDO entry](https://rarediseases.org/mondo-disease/autosomal-recessive-severe-congenital-neutropenia-due-to-csf3r-deficiency/)
- [Glycosmos DOID:0112129](https://glycosmos.org/diseases/DOID:0112129)
- [MGI/RIKEN record for PMID 8934575](https://metadb.riken.jp/metadb/db/mgi_rdf/http://rdf.ncbi.nlm.nih.gov/pubmed/8934575)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 10 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:24753537`: "We describe a novel genetic SCN type in 2 unrelated families associated with recessively inherited biallelic CSF3R mutations."
  - closest text in source: "We describe a novel genetic SCN type in 2 unrelated families associated with recessively inherited loss-of-function mutations in CSF3R, encoding the granulocyte colony-stimulating factor (G-CSF) receptor"
- `PMID:34778134`: "from severe neutropenia unresponsive to high-dose rhG-CSF treatment… to mild neutropenia that does not require active treatment"
  - closest text in source: "The phenotype of SCN7 ranged from severe neutropenia unresponsive to high-dose rhG-CSF treatment (c.998-2A>T and p.W547* compound heterozygous) (7) to mild neutropenia that does not require active treatment (p.R440* homozygous) (14)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.