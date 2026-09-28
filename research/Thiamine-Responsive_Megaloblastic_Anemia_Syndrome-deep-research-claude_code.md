---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T18:52:21.904124'
end_time: '2026-08-27T18:57:04.345884'
duration_seconds: 282.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thiamine-Responsive Megaloblastic Anemia Syndrome
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 19
  total_cost_usd: 1.1706872
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 26
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 7
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC10691017
  relevance_assessed: 12
  on_topic: 10
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thiamine-Responsive Megaloblastic Anemia Syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Thiamine-Responsive Megaloblastic Anemia Syndrome** covering all of the
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

I'll research Thiamine-Responsive Megaloblastic Anemia Syndrome (TRMA/Rogers Syndrome) using web search tools to compile a comprehensive report.

# Thiamine-Responsive Megaloblastic Anemia Syndrome (TRMA / Rogers Syndrome): Comprehensive Research Report

## 1. Disease Information

**Overview.** Thiamine-responsive megaloblastic anemia syndrome (TRMA), also known as Rogers syndrome, is a rare autosomal recessive metabolic disorder caused by biallelic loss-of-function variants in *SLC19A2*, which encodes the high-affinity thiamine (vitamin B1) transporter THTR-1. The disease is defined by a classic clinical triad — megaloblastic anemia, non-type 1 (non-autoimmune) diabetes mellitus, and progressive sensorineural hearing loss — with onset typically between infancy and adolescence. It is distinguished from other congenital anemias by its dramatic, though incomplete, responsiveness to pharmacologic (supraphysiologic) doses of oral thiamine ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Key identifiers:**
- **OMIM:** #249270 (Thiamine-Responsive Megaloblastic Anemia Syndrome; also called Thiamine Metabolism Dysfunction Syndrome 1, THMD1) ([OMIM:249270](https://omim.org/entry/249270))
- **Orphanet:** ORPHA:49827 ([Orphanet](https://www.orpha.net/en/disease/detail/49827))
- **MONDO:** MONDO:0009575
- **ICD-10-CM:** D53.1 (Other megaloblastic anemias, not elsewhere classified) — TRMA has no dedicated ICD-10 code and is billed under this broader category
- **MedGen concept:** C0342287 — "Megaloblastic anemia, thiamine-responsive, with diabetes mellitus and sensorineural deafness" ([NCBI MedGen](https://www.ncbi.nlm.nih.gov/medgen/83338))
- **Gene:** *SLC19A2* (HGNC:11021), chromosome 1q24.2 (also cited as 1q23.3 in older sources)

**Synonyms:** Rogers syndrome; TRMA syndrome; Thiamine-responsive anemia with diabetes mellitus and sensorineural deafness; Roger syndrome.

**Data provenance.** Nearly all published knowledge on TRMA derives from aggregated case reports and small case series (individual-patient/family-level data) rather than large disease-level registries, reflecting the disorder's extreme rarity — GeneReviews estimates "more than 183 individuals from approximately 138 families" reported worldwide ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)), and MedlinePlus similarly cites "approximately 200 cases documented in medical literature" ([MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/thiamine-responsive-megaloblastic-anemia-syndrome/)). A newly reported founder-mutation cluster in the Ingush population (see §9) is the first population/cohort-level epidemiologic dataset for the disease ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)).

---

## 2. Etiology

**Disease causal factor: monogenic, autosomal recessive.** TRMA is caused exclusively by biallelic (homozygous or compound heterozygous) pathogenic variants in *SLC19A2*. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause; dietary thiamine deficiency produces classical beriberi/Wernicke pathology, not TRMA, because TRMA arises from a cellular transport defect rather than systemic vitamin insufficiency.

**Genetic risk factors:**
- Biallelic *SLC19A2* pathogenic variants — the sole causal factor.
- **Consanguinity** is a major risk factor for expression of this rare recessive disease; GeneReviews notes it is "exceedingly rare outside of consanguineous families or isolated populations," with reported kindreds from Israeli Arab, Lebanese, Alaskan Native/Russian, Brazilian, Japanese, Omani, Tunisian, Italian, Iranian, Indian, Pakistani, Kashmiri, Kurdish, northern European, and African American populations ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).
- **Founder effects / isolated populations**: A newly characterized *SLC19A2* c.1223+1G>A canonical splice-site founder variant is endemic in the Ingush population of the North Caucasus, with a heterozygous carrier frequency of 2.7% (≈1/36) in a reference cohort of 328 unrelated adults, sharing a 2.3 Mb ATP1B1–FMO2 founder haplotype on chromosome 1 ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)).
- No modifier genes have been identified; GeneReviews explicitly states no genotype–phenotype correlation exists — clinical severity and which triad features manifest vary unpredictably even within families carrying the same variant ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Environmental/risk-modifying factors:** None established as independent disease-causing factors. However, **dietary thiamine status modulates phenotype severity in model systems** — in *Slc19a2*-null mice, diabetes and cochlear pathology are diet-dependent, emerging specifically on a thiamine-free diet and resolving/normalizing on thiamine repletion or a thiamine-replete diet ([PMID:12393806](https://pubmed.ncbi.nlm.nih.gov/12393806/); [PMID:16642288](https://pubmed.ncbi.nlm.nih.gov/16642288/)), suggesting maternal/dietary thiamine intake could plausibly modulate age of clinical onset in humans, though this is not directly demonstrated in patients.

**Protective factors:** Pharmacologic-dose thiamine supplementation is the only known modifier that ameliorates (though does not cure) the phenotype — it is protective against progression of anemia, thrombocytopenia, and (partially) diabetes onset, but does not prevent or reverse hearing loss (see §12). No protective genetic variants have been described; a residual second thiamine transporter, THTR-2 (encoded by the paralog *SLC19A3*), provides partial intestinal compensation but has minimal expression in the tissues driving TRMA pathology (bone marrow, pancreatic β-cells, cochlea), so it does not meaningfully rescue phenotype ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Gene-environment interaction:** The core gene-environment interaction *is* the treatment mechanism itself: loss of the high-affinity, saturable THTR-1 transport pathway is functionally bypassed by supraphysiologic extracellular thiamine concentrations that drive passive/low-affinity diffusion into cells, restoring intracellular thiamine pyrophosphate (TPP) levels sufficient for thiamine-dependent enzymes ([MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/thiamine-responsive-megaloblastic-anemia-syndrome/)).

---

## 3. Phenotypes

TRMA phenotypes span hematologic, endocrine, otologic, ophthalmologic, cardiovascular, and neurologic domains. Frequencies below are as reported in GeneReviews' pooled case-series data ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

| Phenotype | Category | Frequency | Onset | Course | HPO suggestion |
|---|---|---|---|---|---|
| Megaloblastic anemia | Laboratory/hematologic | 60–70% with full megaloblastic features (nearly universal macrocytic anemia) | Infancy–adolescence | Chronic, thiamine-responsive but recurs on withdrawal | HP:0001889 (Megaloblastic anemia) |
| Macrocytosis (elevated MCV) | Laboratory | Very common | Infancy–adolescence | Often persists despite treatment | HP:0001972 (Macrocytic anemia) |
| Ringed sideroblasts / dysplastic marrow | Laboratory/histopathology | Common | At diagnosis | — | HP:0004828 (Ring sideroblasts) |
| Thrombocytopenia | Laboratory/hematologic | 10–30% | Variable | Thiamine-responsive | HP:0001873 (Thrombocytopenia) |
| Neutropenia | Laboratory/hematologic | Reported, less common | Variable | Thiamine-responsive | HP:0001875 (Neutropenia) |
| Sensorineural hearing loss | Sign, sensory | >90% | Often detected in toddlers; may be congenital/prelingual | Progressive, irreversible; **not** prevented by thiamine | HP:0000407 (Sensorineural hearing impairment) |
| Non-type 1 diabetes mellitus | Sign, endocrine | >90% | Infancy–adolescence | Progressive; often insulin-dependent over time | HP:0000857 (Diabetes mellitus, non-insulin dependent context varies) |
| Diabetic ketoacidosis | Complication | ~15% | — | Episodic | HP:0004904 (Diabetic ketoacidosis) |
| Optic atrophy | Ophthalmologic | Within 20–30% ophthalmologic group | Variable | Progressive | HP:0000648 (Optic atrophy) |
| Retinal dystrophy / cone-rod dystrophy | Ophthalmologic | Within 20–30% ophthalmologic group | Variable | Progressive | HP:0000548 (Cone/cone-rod dystrophy) |
| Congenital heart defects (ASD/VSD) | Cardiovascular | Within 20–30% cardiovascular group | Congenital | Static or complicated | HP:0001631 (ASD), HP:0001629 (VSD) |
| Arrhythmia / atrial standstill | Cardiovascular | Within 20–30% cardiovascular group | Variable | Can be life-threatening | HP:0011675 (Arrhythmia) |
| High-output heart failure | Cardiovascular | Within 20–30% cardiovascular group | Variable | — | HP:0001635 (Congestive heart failure) |
| Sudden death | Cardiovascular | Reported | — | — | — |
| Stroke | Neurologic/vascular | Within 20–40% neurologic group | Variable | — | HP:0001297 (Stroke) |
| Epilepsy/seizures | Neurologic | Within 20–40% neurologic group | Variable | — | HP:0001250 (Seizure) |
| Developmental delay/intellectual disability | Neurologic | Within 20–40% neurologic group | Childhood | — | HP:0001263 (Global developmental delay) |
| Mood disorders/behavioral changes | Neuropsychiatric | Reported | Variable | — | HP:0000708 (Behavioral abnormality) |

**Quality-of-life impact:** No disease-specific EQ-5D/SF-36 data were located. Qualitatively, the irreversible progressive sensorineural hearing loss is the most functionally durable burden (unlike anemia, unresponsive to thiamine), often requiring hearing aids or cochlear implantation for rehabilitation — one case report specifically documents "successful hearing rehabilitation by cochlear implantation" in a TRMA patient ([ScienceDirect case report](https://www.sciencedirect.com/science/article/pii/S1672293024000175)). Insulin-dependent diabetes and its complications, plus the cardiovascular/neurologic complication burden in ~20–40% of patients, are the other major chronic quality-of-life determinants ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Diagnostic mimicry note:** Because bone marrow shows dysplastic hematopoiesis with megaloblasts and ringed sideroblasts, TRMA is noted to be easily mistaken for acquired myelodysplastic syndrome (MDS) — a recent case report is explicitly titled "Thiamine-Responsive Megaloblastic Anemia Syndrome Mimicking Myelodysplastic Neoplasm" ([Karger, Acta Haematologica](https://karger.com/aha/article/148/4/380/915336/Thiamine-Responsive-Megaloblastic-Anemia-Syndrome)), underscoring the importance of distinguishing the two given their divergent prognosis and management.

---

## 4. Genetic/Molecular Information

**Causal gene:** *SLC19A2* (Solute Carrier Family 19 Member 2), HGNC:11021, located on chromosome 1q24.2, spanning 6 exons. It encodes **Thiamine Transporter 1 (THTR-1/ThTr1)**, a 497-amino-acid protein with 12 predicted transmembrane domains, structurally homologous to the reduced folate carrier family ([GeneCards SLC19A2](https://www.genecards.org/card/SLC19A2); [PMID:33649974](https://pubmed.ncbi.nlm.nih.gov/33649974/)). THTR-1 is the *sole* thiamine transporter expressed in bone marrow, cochlear tissue, and pancreatic β-cells, which accounts for the tissue-specificity of the clinical triad — a second, paralogous transporter (THTR-2, encoded by *SLC19A3*) is more broadly/intestinally expressed but does not substitute in these tissues ([PMID:33649974](https://pubmed.ncbi.nlm.nih.gov/33649974/)).

**Discovery:** *SLC19A2* was identified by positional cloning in 1999 as the gene mutated in TRMA-segregating families, initially reported by two independent groups; Labay et al. (Nature Genetics, 1999) reported "Mutations in SLC19A2 cause thiamine-responsive megaloblastic anaemia associated with diabetes mellitus and deafness" ([PMID:10391221](https://pubmed.ncbi.nlm.nih.gov/10391221/); [Nature Genetics ng0799_300](https://www.nature.com/articles/ng0799_300)).

**Pathogenic variant spectrum:** A systematic analysis of reported variants found frameshift variants (31%), nonsense variants (24%), and large deletions (3%) — together accounting for 55% of all reported pathogenic alleles and predicted to cause premature termination and protein truncation. Truncating variants localize predominantly to transmembrane domains (46.3%), cytoplasmic domains (34.1%), and extracellular domains (19.5%); missense variants localize to transmembrane domains (59.3%), extracellular domains (29.6%), and cytoplasmic domains (11.1%) ([PMID:33649974](https://pubmed.ncbi.nlm.nih.gov/33649974/)). Whole-gene deletions/duplications are rare (reported in only 2 families) ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)). A recently reported complex example combines a heterozygous missense variant (c.1001G>A, p.Gly334Asp) with a 3.4 Mb structural inversion of exons 2–6 on the second allele, producing a functionally null allele — illustrating that structural variant analysis may be needed when standard sequencing finds only one pathogenic allele.

**Variant classification/interpretation:** Sequence analysis (Sanger or NGS-based) detects >99% of pathogenic variants (missense, nonsense, splice-site, small indels); gene-targeted deletion/duplication analysis (e.g., MLPA, CMA) is recommended as a reflex test when only one or no variant is found by sequencing ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)). ACMG/AMP-based ClinVar classifications exist for the reported alleles but a curated aggregate summary was not directly retrievable in this search; GeneCards/ClinVar and locus-specific databases should be consulted for the current pathogenic/likely-pathogenic variant list.

**Population/allele frequency:** SLC19A2 pathogenic alleles are rare in gnomAD generally — most pathogenic alleles are absent or present at frequencies below 0.00001 — but show strong founder enrichment in specific populations. The missense variant p.(Gly334Asp) has one of the higher reported gnomAD allele frequencies (~0.00002). The Ingush founder splice variant c.1223+1G>A reaches a striking 2.7% heterozygous carrier frequency (≈1/36) in that population due to a shared 2.3 Mb founder haplotype ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)).

**Zygosity/origin:** All reported pathogenic variants are germline; TRMA has no described somatic form. Both homozygous and compound heterozygous genotypes are reported. A case report specifically documents **maternal uniparental isodisomy** as a mechanism producing homozygosity for a single maternally inherited *SLC19A2* pathogenic variant, despite only one parent being a carrier — an important non-classical mechanism to consider in apparent "homozygosity" without biparental transmission ([PMC8017196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8017196/)).

**Functional consequences:** Loss-of-function is the uniform mechanism — pathogenic missense variants in transmembrane domains cause aberrant protein folding/mislocalization (disrupted trafficking to the plasma membrane) with near-complete loss of transport function, while nonsense/frameshift variants produce truncated, non-functional or absent protein ([PMID:33649974](https://pubmed.ncbi.nlm.nih.gov/33649974/); [GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)). There is no described gain-of-function, dominant-negative, or hypermorphic mechanism.

**Modifier genes:** None established; disease expression is unpredictable across genotypically similar/identical patients (no genotype–phenotype correlation) ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Epigenetic information / chromosomal abnormalities:** No epigenetic mechanism or recurrent chromosomal aneuploidy/translocation has been described for TRMA; disease is driven by point/small-indel/structural loss-of-function variants confined to the *SLC19A2* locus.

---

## 5. Environmental Information

TRMA is a purely monogenic disorder with no established infectious, toxic, or occupational-exposure etiology. The principal "environmental" lever is **dietary/therapeutic thiamine**, which is not a disease cause but the disease's specific pharmacologic countermeasure (see §2, §12). No lifestyle risk factor (smoking, alcohol, exercise) has been linked to TRMA onset or severity in the literature reviewed. No infectious trigger is reported. Consanguinity, discussed above, functions as a population-genetic risk factor rather than a true environmental exposure.

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:** Biallelic *SLC19A2* loss-of-function → absence of the high-affinity, saturable thiamine transport component at the plasma membrane of bone marrow precursors, pancreatic β-cells, and cochlear cells → low intracellular free thiamine and thiamine pyrophosphate (TPP) concentration in these tissues (despite normal serum thiamine) → impaired function of TPP-dependent enzymes, most notably **transketolase** in the non-oxidative branch of the pentose phosphate pathway → defective ribose synthesis for nucleic acid (RNA/DNA) production → impaired DNA synthesis and cell-cycle progression in rapidly dividing hematopoietic precursors, producing megaloblastic dysplastic hematopoiesis; and cellular stress/apoptosis in pancreatic β-cells and cochlear hair cells → clinical triad of megaloblastic anemia, diabetes mellitus, and sensorineural deafness ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/); [Blood, PMID search "Defective RNA ribose synthesis"](https://www.bloodjournal.org/content/102/10/3556)).

**Molecular pathway / biochemical abnormality:** Thiamine pyrophosphate (TPP), the active cofactor form of thiamine, is required by transketolase (pentose phosphate pathway, non-oxidative branch), pyruvate dehydrogenase, and α-ketoglutarate dehydrogenase (TCA cycle). In TRMA fibroblasts, the fractional synthetic rate of ribose is reduced, and the balance of ribose synthesis shifts away from the preferred transketolase/transaldolase-dependent non-oxidative branch toward the oxidative pentose pathway branch, which cannot fully compensate — this reduced nucleic-acid ribose production is proposed as the proximate biochemical lesion driving cell-cycle arrest/apoptosis in bone marrow cells ("Defective RNA ribose synthesis in fibroblasts from patients with thiamine-responsive megaloblastic anemia (TRMA)," *Blood* — [bloodjournal.org](https://www.bloodjournal.org/content/102/10/3556)). An earlier syndrome overlapping TRMA's triad was also linked to deficient α-ketoglutarate dehydrogenase activity, a second TPP-dependent enzyme ([PMID:4045602](https://pubmed.ncbi.nlm.nih.gov/4045602/)), consistent with broad TPP-cofactor insufficiency as the shared downstream lesion.

**Cell type/tissue involvement:**
- **Hematopoietic precursors (bone marrow):** dysplastic megaloblastic erythropoiesis with numerous megaloblasts and iron-laden mitochondria (ringed sideroblasts); thrombocytopenia and neutropenia in a subset, likely reflecting shared TPP-dependence across marrow lineages.
- **Pancreatic β-cells:** THTR-1 is "the only transporter of thiamine into pancreatic β-cells," and its deficiency "leads to cell apoptosis and organ failure" (i.e., β-cell loss driving non-autoimmune, non-type-1 diabetes) — search summary from thiamine/diabetes mechanistic review (PMC8505293, "Thiamine and diabetes: back to the future?").
- **Cochlear hair cells:** In the *Slc19a2*-null mouse model on a low-thiamine diet, histology shows selective **inner hair cell loss** occurring within 1–2 weeks of thiamine restriction, with progressively greater inner-than-outer hair cell loss on longer challenge, producing an auditory neuropathy-like phenotype; auditory brainstem response (ABR) thresholds are markedly elevated on a thiamine-free diet but normal on a thiamine-replete diet ([PMID:16642288](https://pubmed.ncbi.nlm.nih.gov/16642288/)). This maps the human "unclear basis" hearing loss to selective inner hair cell vulnerability.

**Molecular profiling / advanced technologies:** No transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to human TRMA tissue were identified in this search; mechanistic insight instead derives from patient fibroblast biochemistry (ribose synthesis assays) and the *Slc19a2*-knockout mouse model.

**GO/CL term suggestions:**
- Molecular function: GO:0034219 (carbohydrate transmembrane transport) / more specifically thiamine transmembrane transporter activity
- Biological process: GO:0006772 (thiamine metabolic process); pentose-phosphate shunt, non-oxidative branch (GO:0009052)
- Cell types: CL:0000542 (lymphocyte) not relevant; relevant CL terms include CL:0000038 (erythroid progendaughter/erythroid progenitor cell), CL:0000169 (type B pancreatic cell), CL:0000598 (cochlear inner hair cell)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Bone marrow (hematopoietic system), pancreas (endocrine, islets of Langerhans), inner ear/cochlea (auditory system).
- **Secondary:** Eye (optic nerve, retina), heart (conduction system, septa), central and peripheral nervous system, vasculature (stroke risk).
- **Body systems involved:** Hematologic, endocrine, auditory/vestibular, ophthalmologic, cardiovascular, neurologic.

**Tissue and cell level:**
- Bone marrow erythroid, myeloid, and megakaryocytic precursors (dysplastic, megaloblastic change; ringed sideroblasts on iron stain).
- Pancreatic islet β-cells (CL:0000169).
- Cochlear inner hair cells (CL:0000598), with relative sparing of outer hair cells in the mouse model, suggesting a similar pattern may occur in humans ([PMID:16642288](https://pubmed.ncbi.nlm.nih.gov/16642288/)).
- Retina/optic nerve (cone-rod dystrophy, optic atrophy).
- Cardiac conduction tissue and myocardium (atrial standstill, arrhythmia, high-output failure).

**Subcellular level:** Mitochondria are directly implicated — the megaloblastic marrow shows iron-filled mitochondria (ringed sideroblasts), and TPP-dependent mitochondrial enzymes (pyruvate dehydrogenase, α-ketoglutarate dehydrogenase) are plausible downstream targets of thiamine deficiency alongside the cytosolic pentose phosphate pathway enzyme transketolase. GO Cellular Component terms of interest: GO:0005739 (mitochondrion), GO:0005829 (cytosol, site of transketolase activity), GO:0005886 (plasma membrane, site of THTR-1 localization).

**Localization / laterality:** Sensorineural hearing loss and cochlear involvement are typically bilateral; cardiac and ophthalmologic findings are systemic/bilateral in nature rather than lateralized.

**UBERON term suggestions:** UBERON:0002371 (bone marrow), UBERON:0001264 (pancreas), UBERON:0001846 (cochlea), UBERON:0000970 (eye), UBERON:0000948 (heart).

---

## 8. Temporal Development

**Onset:** TRMA onset spans infancy through adolescence, with the earliest anemia findings in the first year of life and latest reported presentations in the teenage years. All three triad features are frequently *not* present simultaneously at initial presentation — patients often present with one or two features first, with the remaining feature(s) emerging over subsequent years ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)). Hearing loss is often detected early, in toddlers, and may be congenital/prelingual in some patients.

**Progression:**
- **Megaloblastic anemia:** corrects with pharmacologic thiamine but red cells remain macrocytic; anemia recurs promptly if thiamine is withdrawn — i.e., a chronic, treatment-dependent (not curative) course.
- **Sensorineural hearing loss:** progressive and irreversible; thiamine treatment does not halt or reverse it, distinguishing its course sharply from the hematologic component.
- **Diabetes mellitus:** progressive; while thiamine may reduce insulin requirement and delay onset in some individuals, most patients eventually require insulin therapy; diabetic ketoacidosis occurs in ~15%.
- **Cardiovascular/neurologic/ophthalmologic complications:** variable, sometimes severe (sudden death, stroke, atrial standstill), and thiamine's efficacy against these is not established.

**Disease course pattern:** Chronic and lifelong; not self-limited. No spontaneous remission is described. The disease requires indefinite pharmacologic thiamine dosing — GeneReviews states anemia recurs "if treatment is withdrawn," underscoring that TRMA is managed, not cured.

**Critical periods:** Early diagnosis and thiamine initiation is repeatedly emphasized as critical — an Italian case series is explicitly titled around "the importance of early diagnosis and treatment" ([PMC10691017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691017/)), consistent with the concept that early thiamine repletion may forestall or blunt onset of diabetes and preserve residual hearing, even though it cannot reverse established sensorineural damage.

---

## 9. Inheritance and Population

**Epidemiology:** TRMA is exceedingly rare, with formal prevalence/incidence statistics unknown; the literature has historically reported "less than 80 cases worldwide" in earlier summaries and up to ~200 cases / 138 families in more recent GeneReviews/MedlinePlus tallies (both figures reflect case-series accumulation rather than population-based ascertainment) ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/); [MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/thiamine-responsive-megaloblastic-anemia-syndrome/)).

**Inheritance pattern:** Autosomal recessive. At conception, each sibling of an affected individual has a 25% chance of being affected, 50% chance of being an asymptomatic carrier, and 25% chance of being unaffected/non-carrier ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)). Heterozygous carriers are clinically asymptomatic.

**Penetrance/expressivity:** Effectively complete penetrance for biallelic pathogenic genotypes (disease manifests), but markedly variable expressivity — which triad components appear, their severity, and age of onset differ unpredictably between and even within families, with **no genotype–phenotype correlation** established ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Genetic anticipation:** Not described; TRMA is not a repeat-expansion disorder.

**Germline mosaicism / uniparental disomy:** A documented mechanism of apparent "homozygosity" without both parents being carriers is maternal uniparental isodisomy of chromosome 1, producing two identical maternal copies of a single pathogenic *SLC19A2* allele ([PMC8017196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8017196/)) — an important consideration for genetic counseling when only one parent tests as a carrier.

**Founder effects / consanguinity:** TRMA is strongly enriched in consanguineous unions and in geographically/ethnically isolated populations. The best-documented founder effect is the Ingush population of the North Caucasus (Russia), where the canonical splice variant *SLC19A2* c.1223+1G>A reaches a heterozygous carrier frequency of 2.7% (≈1/36) in a reference cohort of 328 unrelated adults, tracing to a shared 2.3 Mb ATP1B1–FMO2 founder haplotype; this study newly identifies Ingushetia as a **TRMA-endemic region** and recommends targeted screening and early thiamine therapy for macrocytic anemia/diabetes of unclear origin in that population — notably, all identified patients became transfusion-independent on high-dose thiamine therapy ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)). Other reported founder/cluster populations include Israeli Arab, Lebanese, Alaskan Native/ethnic Russian, Brazilian, Japanese, Omani, Tunisian, Italian, Iranian, Indian, Pakistani, Kashmiri (in Great Britain), and Kurdish kindreds ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Carrier frequency:** Population-wide carrier frequency is presumably very low outside founder populations (consistent with gnomAD data showing most pathogenic *SLC19A2* alleles at allele frequency <0.00001), but reaches 2.7% in the Ingush founder population specifically ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)).

**Sex ratio / geographic distribution:** No sex predilection is reported (consistent with autosomal inheritance). Geographic distribution is scattered/sporadic worldwide, reflecting the disorder's dependence on consanguinity/founder effects rather than a specific endemic geography, with the Ingush cluster as a notable exception.

---

## 10. Diagnostics

**Clinical/biochemical diagnostic criteria:** Per GeneReviews, the diagnosis of TRMA is established in a proband with **megaloblastic anemia with normal vitamin B12/folic acid levels**, with or without diabetes or hearing loss, who shows a **response to oral thiamine** ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)). This clinical/biochemical criterion is typically confirmed molecularly.

**Laboratory tests:**
- CBC with elevated MCV (macrocytosis), low hemoglobin.
- Reticulocyte count (monitored for treatment response).
- Bone marrow aspirate/biopsy: megaloblastic, dysplastic hematopoiesis with ringed sideroblasts (iron stain).
- Normal serum vitamin B12 and folate (key distinguishing feature from nutritional megaloblastic anemias).
- Fasting glucose, oral glucose tolerance test, urinalysis for glucose intolerance/diabetes screening.

**Genetic testing:**
- **First-line:** Sequence analysis of *SLC19A2* (Sanger or targeted NGS), which detects >99% of pathogenic variants including small indels, missense, nonsense, and splice-site variants.
- **Reflex testing:** Gene-targeted deletion/duplication analysis (e.g., MLPA, chromosomal microarray) when only one or no variant is identified by sequencing — relevant given rare reported whole-gene deletions/duplications and structural variants (e.g., the exon 2–6 inversion case).
- **Broader testing:** Multigene panels for congenital sideroblastic/megaloblastic anemia or syndromic deafness-diabetes, or comprehensive genomic testing (exome/genome sequencing), particularly useful when the clinical presentation is atypical or incomplete ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).
- Uniparental disomy testing may be informative in cases of apparent unexplained homozygosity ([PMC8017196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8017196/)).

**Imaging/other:** No disease-specific imaging modality; echocardiography is indicated given the 20–30% cardiovascular involvement rate (structural defects, arrhythmia, atrial standstill); audiometry/ABR for hearing assessment; ophthalmologic exam (fundoscopy, possibly electroretinography) for retinal/optic nerve involvement.

**Differential diagnosis** (from GeneReviews):

| Disorder | Distinguishing feature vs. TRMA |
|---|---|
| Wolfram syndrome (*WFS1*, DIDMOAD) | Lacks megaloblastic anemia and thiamine responsiveness |
| Wolfram syndrome type 2 (*CISD2*) | Lacks megaloblastic anemia; high-frequency-only hearing loss; may feature GI ulcers |
| Primary mitochondrial disorders | Share diabetes + deafness but lack the characteristic thiamine-responsive macrocytic anemia |
| Acquired myelodysplastic syndrome (MDS) | Marrow morphology (megaloblasts, ringed sideroblasts) can closely mimic TRMA; distinguished by young age, family history, biallelic *SLC19A2* variants, and thiamine responsiveness — misdiagnosis as MDS is explicitly documented in the literature ([Karger Acta Haematologica case report](https://karger.com/aha/article/148/4/380/915336/)) |

**Screening:** No population newborn-screening program exists for TRMA given its extreme rarity, though the Ingush founder-population study explicitly recommends **targeted carrier/diagnostic screening** for *SLC19A2* c.1223+1G>A in that specific population given macrocytic anemia or diabetes of unclear origin ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)).

---

## 11. Outcome/Prognosis

**Survival/mortality:** No systematic survival statistics (5-year/10-year survival, life expectancy) were located in the literature searched; sudden cardiac death is reported as a rare but real complication, and the disease's cardiovascular (20–30%) and neurologic (20–40%, including stroke) complication burden implies meaningful excess morbidity/mortality risk relative to the general population, though quantified rates were not found.

**Morbidity/function:** The dominant chronic morbidity driver is **irreversible progressive sensorineural hearing loss**, which persists regardless of thiamine treatment and is managed with hearing aids or cochlear implantation. Insulin-dependent diabetes contributes long-term micro/macrovascular risk typical of any chronic diabetes. The 20–40% rate of neurologic complications (developmental delay, intellectual disability, epilepsy, stroke) and 20–30% rate of cardiovascular complications (arrhythmia, congenital heart defects, high-output failure) represent additional major sources of long-term disability.

**Recovery potential / treatment impact:** With thiamine treatment, hematologic parameters (anemia, thrombocytopenia, neutropenia) reliably improve, and some patients — as in the Ingush cohort — become fully transfusion-independent on high-dose thiamine therapy ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)). Diabetes may be delayed in onset or require reduced insulin dosing with thiamine, but is not reliably reversed. Hearing loss, once established, does not recover with thiamine.

**Prognostic factors:** Early diagnosis and early initiation of thiamine therapy is repeatedly emphasized in the literature as the single most actionable prognostic factor, given its role in mitigating hematologic disease and potentially delaying diabetes onset, even though it cannot rescue hearing ([PMC10691017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691017/)). No molecular biomarker for prognosis (beyond genotype, which does not correlate with severity) has been established.

---

## 12. Treatment

**Primary pharmacotherapy:** Lifelong oral thiamine (vitamin B1) at pharmacologic doses of **50–100 mg/day** (occasionally reported up to 25–100 mg/day in at-risk relatives pending genetic confirmation), regardless of patient age, is the cornerstone of TRMA management. GeneReviews notes no additional clinical benefit is observed above 150 mg/day. Thiamine "invariably improves hematologic findings" but must be continued indefinitely, as anemia recurs upon discontinuation ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).
- NCIT suggestion: NCIT:C15986 (Pharmacotherapy), with `therapeutic_agent` bound to thiamine (CHEBI, if available) — vitamin/nutrient supplementation therapy.

**Manifestation-specific treatment:**

| Manifestation | Treatment | NCIT suggestion |
|---|---|---|
| Megaloblastic anemia | Oral thiamine 50–100 mg/day; red cell transfusion for severe/acute cases | NCIT:C15986 (Pharmacotherapy); NCIT:C15170 (Blood Transfusion) |
| Sensorineural hearing loss | Hearing aids, cochlear implantation, audiologic follow-up (thiamine ineffective) | NCIT:C50399 (Hearing Aid), cochlear implantation procedure term |
| Diabetes mellitus | Standard diabetes care (oral hypoglycemics initially, insulin as needed) plus thiamine | NCIT:C15986 (Pharmacotherapy) |
| Thrombocytopenia | Oral thiamine (responsive) | NCIT:C15986 |
| Cardiac, neurologic, ophthalmologic complications | Standard specialist (cardiology, neurology, ophthalmology) supportive care; thiamine efficacy not established for these domains | Varies by intervention |

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or targeted molecular therapy has been developed or trialed for TRMA specifically — the disease is managed entirely through cofactor-bypass pharmacotherapy (high-dose thiamine) and manifestation-directed supportive/specialist care. No disease-specific registered clinical trials (ClinicalTrials.gov, NCT identifiers) were identified for TRMA in this search, consistent with its ultra-rare status; management guidance derives from case-series experience rather than randomized trials.

**Treatment response/outcomes:** Response to thiamine is the diagnostic hallmark itself (see §10) — reticulocytosis and hemoglobin normalization are expected within weeks of thiamine initiation. Diabetes response is more variable: thiamine "may reduce insulin requirement and delay onset of diabetes in some individuals" but is not curative. No systematic adverse-event data for high-dose thiamine in TRMA were found; oral thiamine is generally very well tolerated even at pharmacologic doses.

**Pregnancy management:** GeneReviews specifically recommends good diabetic control prior to and during pregnancy in affected women.

**Genetic counseling / at-risk relative management:** GeneReviews recommends **empiric thiamine supplementation** (25–100 mg/day, compared with the US RDA of ~1.5 mg/day) for at-risk siblings as early as possible, pending determination of their genetic/carrier status, given the low harm profile of thiamine and the benefit of early treatment if affected ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

---

## 13. Prevention

**Primary prevention:** Because TRMA is a fully penetrant monogenic recessive disorder, primary prevention is achieved through **genetic counseling and carrier screening** in at-risk families/populations (particularly consanguineous families and founder populations such as the Ingush cluster), plus **prenatal and preimplantation genetic testing** once the family's pathogenic variant(s) are identified ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/); [PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)). There is no vaccine or environmental-exposure-avoidance strategy relevant to this genetic disease.

**Secondary prevention (early detection):** Because thiamine treatment cannot reverse established hearing loss but can prevent/attenuate anemia and delay diabetes, **early diagnosis via clinical suspicion (megaloblastic anemia with normal B12/folate, especially with diabetes or deafness) followed by prompt genetic confirmation and thiamine initiation** functions as the operative secondary-prevention strategy — repeatedly emphasized across case reports as the modifiable determinant of outcome ([PMC10691017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691017/); [PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)). Empiric thiamine supplementation of at-risk siblings pending genetic testing is a specific, actionable secondary-prevention measure per GeneReviews.

**Tertiary prevention:** Lifelong surveillance (see below) and manifestation-specific specialist management (audiology, endocrinology, cardiology, ophthalmology, neurology) aim to detect and manage complications before they become severe.

**Surveillance schedule (GeneReviews):** At least annual evaluation is recommended, including:
- Hematologic tests (CBC, reticulocyte count) to monitor thiamine treatment efficacy.
- Glucose intolerance assessment (fasting glucose, OGTT, urinalysis).
- Hearing, ophthalmologic, cardiac, and neurologic evaluations.
- Assessment for manifestations of poor glycemic control ([GeneReviews, NBK1282](https://www.ncbi.nlm.nih.gov/books/NBK1282/)).

**Genetic counseling:** Standard autosomal recessive counseling applies (25% recurrence risk per pregnancy for carrier parents); population-specific counseling and targeted variant screening is now specifically recommended for the Ingush population given the newly characterized founder mutation ([PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)).

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease analogous to TRMA (i.e., spontaneous *SLC19A2*-deficiency disease in companion animals or livestock) was identified in this search — this appears to be an area with no OMIA (Online Mendelian Inheritance in Animals) entry located, and no veterinary case series were found. The disease as studied in other species is confined to engineered/induced laboratory models (§15) rather than naturally occurring animal disease.

**Orthology:** *SLC19A2* shows conserved orthology across human, mouse, rat, and zebrafish, indicating cross-species conservation of thiamine transporter biology, though this has not translated into documented spontaneous natural disease reports in non-human species in the literature surveyed.

---

## 15. Model Organisms

**Mouse (*Mus musculus*) — the principal TRMA model:**
- **Model:** *Slc19a2*-null (targeted knockout) mouse, generated via homologous recombination/gene-trap disruption in embryonic stem cells (MGI:1928761) ([PMID:12393806](https://pubmed.ncbi.nlm.nih.gov/12393806/); [MGI Slc19a2](https://www.informatics.jax.org/marker/MGI:1928761)).
- **Phenotype recapitulation:**
  - Erythrocytes from *Slc19a2*⁻/⁻ mice lack the high-affinity component of thiamine transport, mirroring the human cellular defect.
  - On a **thiamin-free diet**, *Slc19a2*⁻/⁻ mice develop diabetes mellitus with reduced insulin secretion and enhanced peripheral insulin sensitivity; this diabetes **resolves after ~6 weeks of thiamin repletion**, directly modeling the human treatment-responsiveness ([PMID:12393806](https://pubmed.ncbi.nlm.nih.gov/12393806/)).
  - Auditory brainstem response (ABR) thresholds are markedly elevated in *Slc19a2*⁻/⁻ mice on a thiamin-free diet but remain normal in wild-type mice on the same diet and in thiamin-fed knockouts — demonstrating diet-dependence of the hearing phenotype.
  - Cochlear histology reveals **selective inner hair cell loss** after 1–2 weeks of low-thiamine challenge, with progressively greater inner-versus-outer hair cell loss over longer challenge periods, producing an auditory neuropathy phenotype; cochlear function is normal in mutants maintained on a high-thiamine diet ([PMID:16642288](https://pubmed.ncbi.nlm.nih.gov/16642288/)).
  - Bone marrow analysis in this model shows evidence for defective deoxyribose and heme synthesis, mechanistically linking the transporter defect to impaired hematopoiesis ([ASH Blood abstract, "Role of Defective High-Affinity Thiamine Transporter slc19a2 in Marrow..."](https://ashpublications.org/blood/article/106/11/516/117230/)).
- **Model limitations:** The mouse phenotype is strongly **diet-dependent** (requiring a thiamin-free diet to unmask diabetes/deafness), whereas human patients develop disease despite normal dietary thiamine intake — reflecting a difference in baseline thiamine reserve/requirement or transporter redundancy between species that should be considered when extrapolating findings. This is a case where the model requires an added environmental manipulation (dietary thiamine restriction) to recapitulate a phenotype that arises spontaneously from genotype alone in humans — i.e., a `PARTIALLY_RECAPITULATES` relationship, gated by diet, rather than full spontaneous recapitulation.
- **Research applications:** This model has been the primary tool for establishing the diet-thiamine-dependence of the diabetes and cochlear phenotypes and for identifying selective inner hair cell vulnerability as the auditory pathology substrate.

**Human patient-derived cellular models:**
- Patient dermal **fibroblasts and erythrocytes** have been used directly (not as engineered lines) to demonstrate loss of high-affinity thiamine uptake and to quantify defective RNA ribose synthesis via the transketolase-dependent non-oxidative pentose phosphate pathway branch, providing the primary human cellular mechanistic evidence base ([Blood, "Defective RNA ribose synthesis in fibroblasts from patients with TRMA"](https://www.bloodjournal.org/content/102/10/3556); [JCI PDF, "Defective high-affinity thiamine transporter leads to cell..."](http://content-assets.jci.org/manuscripts/3000/3895/JCI9903895.pdf)).

**iPSC / zebrafish / Drosophila models:** No TRMA-specific induced pluripotent stem cell line, zebrafish model, or Drosophila model was identified in this search, despite conserved *SLC19A2* orthology in zebrafish making such a model theoretically feasible. (For comparison/contrast, iPSC models exist for the related paralog disease, *SLC19A3*-associated Biotin-Thiamine-Responsive Basal Ganglia Disease — e.g., KAIMRCi004-A/B lines — but these model a genetically and phenotypically distinct disorder, not TRMA itself.) This represents an apparent gap in available model-system resources for TRMA specifically.

**Resources:** MGI:1928761 (mouse *Slc19a2* gene page, with knockout allele information) is the primary curated animal-model database entry identified ([MGI](https://www.informatics.jax.org/marker/MGI:1928761)).

---

## Summary Table of Key Ontology Term Suggestions

| Domain | Suggested term |
|---|---|
| Disease (MONDO) | MONDO:0009575 |
| Disease (OMIM) | 249270 |
| Disease (Orphanet) | ORPHA:49827 |
| Causal gene (HGNC) | hgnc:11021 (SLC19A2) |
| Megaloblastic anemia (HP) | HP:0001889 |
| Sensorineural hearing loss (HP) | HP:0000407 |
| Diabetes mellitus (HP) | HP:0000819 / HP:0000857 |
| Ring sideroblasts (HP) | HP:0004828 |
| Thrombocytopenia (HP) | HP:0001873 |
| Optic atrophy (HP) | HP:0000648 |
| Atrial septal defect (HP) | HP:0001631 |
| Thiamine metabolic process (GO) | GO:0006772 |
| Pentose-phosphate shunt, non-oxidative branch (GO) | GO:0009052 |
| Pancreatic β-cell (CL) | CL:0000169 |
| Cochlear inner hair cell (CL) | CL:0000598 |
| Bone marrow (UBERON) | UBERON:0002371 |
| Cochlea (UBERON) | UBERON:0001846 |
| Pancreas (UBERON) | UBERON:0001264 |
| Thiamine (CHEBI) | CHEBI:18385 (thiamine(1+)) / thiamine |
| Treatment: Pharmacotherapy (NCIT) | NCIT:C15986 |

---

## Sources

- [Thiamine-Responsive Megaloblastic Anemia Syndrome — GeneReviews®, NCBI Bookshelf (NBK1282)](https://www.ncbi.nlm.nih.gov/books/NBK1282/)
- [OMIM #249270 — Thiamine-Responsive Megaloblastic Anemia Syndrome](https://omim.org/entry/249270)
- [Orphanet: Thiamine-responsive megaloblastic anemia syndrome (ORPHA:49827)](https://www.orpha.net/en/disease/detail/49827)
- [MedlinePlus Genetics: Thiamine-responsive megaloblastic anemia syndrome](https://medlineplus.gov/genetics/condition/thiamine-responsive-megaloblastic-anemia-syndrome/)
- [NCBI MedGen C0342287](https://www.ncbi.nlm.nih.gov/medgen/83338)
- [GARD (NIH) — Megaloblastic anemia, thiamine-responsive, with diabetes mellitus and sensorineural deafness](https://rarediseases.info.nih.gov/diseases/9210/megaloblastic-anemia-thiamine-responsive-with-diabetes-mellitus-and-sensorineural-deafness)
- Labay V, et al. "Mutations in SLC19A2 cause thiamine-responsive megaloblastic anaemia associated with diabetes mellitus and deafness." *Nat Genet.* 1999. [PMID:10391221](https://pubmed.ncbi.nlm.nih.gov/10391221/) / [Nature Genetics ng0799_300](https://www.nature.com/articles/ng0799_300)
- Oishi K, et al. "Targeted disruption of Slc19a2, the gene encoding the high-affinity thiamin transporter Thtr-1, causes diabetes mellitus, sensorineural deafness and megaloblastosis in mice." *Hum Mol Genet.* 2002. [PMID:12393806](https://pubmed.ncbi.nlm.nih.gov/12393806/)
- "Deletion of SLC19A2, the High Affinity Thiamine Transporter, Causes Selective Inner Hair Cell Loss and an Auditory Neuropathy Phenotype." *JARO.* [PMID:16642288](https://pubmed.ncbi.nlm.nih.gov/16642288/)
- "The Effects of Genetic Mutations and Drugs on the Activity of the Thiamine Transporter, SLC19A2." [PMID:33649974](https://pubmed.ncbi.nlm.nih.gov/33649974/)
- "An Endemic Region of Thiamine-Responsive Megaloblastic Anemia Caused by an SLC19A2 c.1223+1G>A Founder Mutation" (Ingush population). [PMID:42511616](https://pubmed.ncbi.nlm.nih.gov/42511616/)
- "Defective RNA ribose synthesis in fibroblasts from patients with thiamine-responsive megaloblastic anemia (TRMA)." *Blood.* [bloodjournal.org](https://www.bloodjournal.org/content/102/10/3556)
- "Diabetes mellitus, thiamine-dependent megaloblastic anemia, and sensorineural deafness associated with deficient alpha-ketoglutarate dehydrogenase activity." [PMID:4045602](https://pubmed.ncbi.nlm.nih.gov/4045602/)
- "Case Report: Genetic and Clinical Features of Maternal Uniparental Isodisomy-Induced Thiamine-Responsive Megaloblastic Anemia Syndrome." [PMC8017196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8017196/)
- "An Italian case series' description of thiamine responsive megaloblastic anemia syndrome: importance of early diagnosis and treatment." [PMC10691017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691017/)
- "Thiamine-Responsive Megaloblastic Anemia Syndrome Mimicking Myelodysplastic Neoplasm." *Acta Haematologica.* [Karger](https://karger.com/aha/article/148/4/380/915336/)
- "Cardiac Manifestations in Thiamine-Responsive Megaloblastic Anemia Syndrome." *Pediatric Cardiology.* [SpringerLink](https://link.springer.com/article/10.1007/s00246-002-0215-3)
- "Thiamine-responsive megaloblastic anemia syndrome with atrial standstill: a case report." [PMID:21285901](https://pubmed.ncbi.nlm.nih.gov/21285901/)
- "Thiamine responsive megaloblastic Anemia and deafness: A rare case of Roger's syndrome with successful hearing rehabilitation by cochlear implantation." [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1672293024000175)
- SLC19A2 gene — GeneCards (SLC19A2 protein structure). [GeneCards](https://www.genecards.org/card/SLC19A2)
- MGI:1928761 — Slc19a2 Mouse Gene Detail. [Jackson Laboratory MGI](https://www.informatics.jax.org/marker/MGI:1928761)
- "[Thiamine-responsive megaloblastic anemia or Rogers syndrome: A literature review]." [PMID:30031565](https://pubmed.ncbi.nlm.nih.gov/30031565/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC10691017` *(abstract only)*: "the importance of early diagnosis and treatment"
  - closest text in source: "In Cases 2 and 3, follow-up showed no blindness, unlike Case 4, in which treatment was started for megaloblastic anemia at age 7 but was increased to high doses only at age 25, when the genetic diagnosis of TRMA was performed"