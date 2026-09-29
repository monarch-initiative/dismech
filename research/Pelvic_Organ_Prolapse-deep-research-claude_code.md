---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-08-28T05:58:03.292178'
end_time: '2026-08-28T06:02:26.352776'
duration_seconds: 263.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pelvic Organ Prolapse
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
  - claude-opus-4-8[1m]
  web_search_requests: 6
  num_turns: 9
  total_cost_usd: 1.4596905
  session_id: 8ade17f8-9956-4aed-8c1d-13bf72be8725
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 18
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 29
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pelvic Organ Prolapse
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Pelvic Organ Prolapse** covering all of the
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

I'll research Pelvic Organ Prolapse comprehensively. Let me load the search tools and gather current information.

Let me look at the existing file for context and run parallel searches for current data.

Let me gather additional targeted data on identifiers, staging/diagnosis, genetics, and treatment.

I now have sufficient material from both current web sources and the well-cited existing knowledge base entry. Here is the comprehensive research report.

---

# Comprehensive Research Report: Pelvic Organ Prolapse (POP)

**Prepared:** 2026-08-28 · **MONDO ID:** MONDO:0000082 · **Category:** Complex / multifactorial

> **Scope note on evidence quality:** POP is unusual among "diseases" in that it is fundamentally a *mechanical failure of a composite support system*, and one of its defining features is a poor correlation between anatomic findings and symptoms. Several key mechanistic claims (the extracellular-matrix signature in particular) rest on cross-sectional case-control tissue studies that cannot separate cause from consequence. Where this ambiguity exists, it is flagged rather than smoothed over.

---

## 1. Disease Information

**Overview.** Pelvic organ prolapse is the downward descent of one or more pelvic organs — the bladder (cystocele/anterior compartment), uterus or post-hysterectomy vaginal cuff (apical compartment), rectum (rectocele/posterior compartment), or small bowel (enterocele) — producing protrusion of the vaginal walls or uterus toward and beyond the hymen. It is best understood not as a disease of one tissue but as the failure of a *load-sharing* support system: the **levator ani muscle complex** holds the pelvic floor and urogenital hiatus closed, while the **cardinal, uterosacral, and paravaginal connective-tissue attachments** suspend the uterus and vagina from the pelvic sidewall. Failure of either element transfers load to the other (PMID:27517338).

**Key identifiers.**
- **MONDO:** MONDO:0000082 (pelvic organ prolapse)
- **MeSH:** D056887 ("Pelvic Organ Prolapse"); ancestor headings include Prolapse, Female Urogenital Diseases
- **ICD-10-CM:** Category **N81** (Female genital prolapse) — N81.1x cystocele, N81.2 incomplete uterovaginal prolapse, N81.3 complete uterovaginal prolapse, N81.4 uterovaginal prolapse unspecified, N81.5 vaginal enterocele, N81.6 rectocele
- **ICD-11:** **GC40** (Female pelvic organ prolapse) block, with subentities (e.g., GC40.0 cystocele, GC40.3 uterine prolapse)
- **OMIM:** **176780** ("Pelvic Organ Prolapse, POP") — a susceptibility phenotype entry rather than a Mendelian gene entry
- **Orphanet:** POP is *not* an Orphanet rare-disease entry (it is common, not rare); heritable connective-tissue disorders that cause it (e.g., Ehlers-Danlos, ORPHA:98249) are separate entries.

**Synonyms / alternative names:** POP; genital prolapse; urogenital prolapse; vaginal prolapse; pelvic floor dysfunction (broader); by compartment — cystocele, rectocele, enterocele, uterine prolapse, vaginal vault prolapse, procidentia (complete/stage 4).

**Data derivation.** Population estimates derive from aggregated resources (NHANES, claims databases, national registries, Orphanet-style epidemiology tables) and disease-level cohorts; POP-Q staging, mechanistic tissue studies, and imaging findings are individual-patient/EHR-level.

*Sources:* [MONDO](https://monarchinitiative.org/MONDO:0000082), [ICD-10 N81 (AAPC)](https://www.aapc.com/codes/icd-10-codes/N81), [StatPearls POP (NBK563229)](https://www.ncbi.nlm.nih.gov/books/NBK563229/); PMID:27517338, PMID:31851453.

---

## 2. Etiology

POP is **multifactorial**. The most consistent risk factors across the literature are **vaginal childbirth, advancing age, and rising body-mass index** (PMID:17382829): *"Prolapse development is multifactorial, with vaginal child birth, advancing age, and increasing body-mass index as the most consistent risk factors."*

### Disease Causal Factors
- **Mechanical / obstetric (primary trigger).** Vaginal delivery imposes overstretch on the levator ani and birth canal to >3× resting length, producing levator injury/avulsion (PMID:38168908). This is the single largest *modifiable* driver.
- **Genetic / constitutional (susceptibility).** Inherited variation in connective-tissue composition and turnover sets the load tolerance of the support system (GWAS + monogenic connective-tissue disorders; see §4, §9).
- **Degenerative / hormonal.** Ageing and menopausal estrogen withdrawal (§6).
- **Not infectious.** POP has no infectious etiology.

### Risk Factors
**Environmental / demographic:**
- **Vaginal childbirth & parity** — risk rises with 1, 2, and ≥3 vaginal deliveries vs nulliparity; **instrumental (forceps) delivery, occiput-posterior birth, prolonged second stage, macrosomia (>4000 g), older maternal age** increase levator-injury risk (PMID:38168908).
- **Age** — POP prevalence on exam rises from ~26.5% (age 40–59) to 36.8% (60–79) to 49.7% (≥80); incidence in menopausal women rises ~40% per decade (PMID:31851453; Current Opinion in Urology, PMID:23619578).
- **Obesity / high BMI** — overweight and obese women more likely to report ≥1 pelvic-floor disorder (PMID:18799443).
- **Chronic straining** — constipation, IBS, chronic cough, heavy lifting.
- **Prior hysterectomy** (esp. for prolapse) predisposes to later vault prolapse (PMID:31851453).
- **Family history / ethnicity** — Hispanic and White women report higher rates than Black/Asian women in several US cohorts.

**Genetic risk factors:** susceptibility loci near **WNT4, EFEMP1, WT1, FGFR2, FAT4, IMPDH1, TBX5, SALL1, GDF7, LOXL1** (see §4). Monogenic: Ehlers-Danlos and joint-hypermobility syndromes carry POP prevalence of **29–75%** (PMID:39033997).

### Protective Factors
- **Cesarean delivery** (avoids levator overstretch) and **nulliparity** are strongly protective.
- **Weight management** plausibly protective (inference from BMI gradient).
- **Genetic protective alleles:** the reciprocal (support-favoring) alleles at GWAS loci; no single validated protective variant is established.
- **Notable negative results:** lifetime physical activity does **not** increase POP odds in community cohorts (PMID:26348380), so avoidance of exercise is *not* protective; and hormone therapy does **not** improve pelvic support (PMID:28538602) — so estrogen is not a validated protective intervention.

### Gene-Environment Interaction
The central G×E model: **childbirth (environment) acts as the load that unmasks a constitutional connective-tissue susceptibility (genetics).** Recovery of pelvic support after delivery requires a postpartum burst of elastic-fiber assembly; animals genetically unable to make it (Loxl1-null, Fbln5-null) prolapse specifically after parturition (PMID:14745449; PMID:17255326) — a direct demonstration that a genetic defect and the obstetric load combine to produce disease.

*Sources:* PMID:17382829, PMID:38168908, PMID:31851453, PMID:18799443, PMID:26348380, PMID:28538602, PMID:39033997; [IUGA epidemiology consultation](https://link.springer.com/article/10.1007/s00192-021-05018-z).

---

## 3. Phenotypes

POP is characterized by anatomic descent (sign) that correlates poorly with symptoms — **only vaginal bulging is specific to prolapse** (PMID:17382829, PMID:31851453).

| Phenotype | Type | Suggested HPO | Frequency / notes |
|---|---|---|---|
| **Vaginal bulge / "something coming down"** | Symptom (specific) | HP:0000005-adjacent; use *Pelvic organ prolapse* **HP:0100615** | The only symptom specific to POP; sensitivity of the symptom is limited |
| **Pelvic organ prolapse (anatomic)** | Clinical sign | **HP:0100615** (Pelvic organ prolapse) | Root phenotype |
| **Cystocele (anterior)** | Sign | **HP:0009611** (Cystocele) | Most common compartment (~68.6%) |
| **Rectocele (posterior)** | Sign | HP:0100823 (Rectocele) | ~16% |
| **Uterine/apical prolapse** | Sign | HP:0000139 (Uterine prolapse) | ~38.6% apical |
| **Pelvic pressure / heaviness** | Symptom | HP:0030496-adjacent (pelvic pain HP:0012648) | Common, non-specific |
| **Stress urinary incontinence** | Symptom | **HP:0000020** (Urinary incontinence) / stress-specific | Frequent co-occurring pelvic-floor disorder |
| **Voiding dysfunction / incomplete emptying** | Symptom | HP:0000012 (Urinary bladder dysfunction) | Advanced anterior/apical POP; may require splinting |
| **Obstructed defecation / splinting** | Symptom | HP:0002015 (dysphagia-adjacent → use HP:0002019 Constipation) | Posterior compartment |
| **Dyspareunia / sexual dysfunction** | Symptom | HP:0030016 (Dyspareunia) | QoL impact |
| **Vaginal mucosal erosion/ulceration** | Sign | HP:0100699 (Vaginal neoplasm-adjacent; use erosion) | Advanced procidentia |

**Onset / severity / progression:** adult-onset, typically peri-/postmenopausal; severity graded by POP-Q stage 0–4 (§10); course is **chronic and generally slowly progressive**, though anatomic descent can fluctuate and mild descent may regress. Symptom threshold is classically when the leading edge reaches or passes the hymen.

**Frequency among affected:** anterior > apical > posterior compartment involvement; multi-compartment disease common in advanced/high-avulsion cases (PMID:36343586).

**Quality-of-life impact:** measured with condition-specific instruments — **PFDI-20 / PFIQ-7, P-QoL, PISQ-12** (sexual function). Bulge symptoms, voiding/defecatory dysfunction, and dyspareunia drive impairment; generic tools (SF-36, EQ-5D) also used.

*Sources:* PMID:17382829, PMID:31851453, PMID:36343586; [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK563229/), [Merck Manual](https://www.merckmanuals.com/professional/gynecology-and-obstetrics/pelvic-organ-prolapse-pop/overview-of-pelvic-organ-prolapse-pop).

---

## 4. Genetic / Molecular Information

POP is a **complex/polygenic** trait, not Mendelian, but with clear connective-tissue genetic architecture.

### GWAS susceptibility loci
- **Iceland + UK Biobank (2020):** 8 variants at **7 loci** in 15,010 cases; implicated genes **WNT4** (estrogen-pathway/urogenital development) and **EFEMP1/fibulin-3** (connective-tissue homeostasis). *"Our results highlight the role of connective tissue metabolism and estrogen exposure in the etiology of POP"* and rs3791675 at EFEMP1 also associates with hernias and carpal tunnel syndrome (PMID:32184442).
- **European meta-analysis (2022, Nat Commun):** 28,086 cases / 546,291 controls → **19 novel loci**, implicating connective-tissue, urogenital, and cardiometabolic systems; replicated WNT4, EFEMP1, FAT4, IMPDH1, TBX5, SALL1 ([Nat Commun 2022](https://www.nature.com/articles/s41467-022-31188-5)).
- **Japanese GWAS + cross-ancestry (2024, Commun Biol):** identified **WT1** (rs10742277, OR 1.48, P=6.7×10⁻⁹) and, cross-ancestry, **FGFR2** (rs7072877, OR 1.06, P=4.1×10⁻⁸); **21 of 24** European loci showed directionally consistent effects — evidence for a **shared cross-ancestry genetic architecture** (PMID:39349682).

**HGNC / gene annotations (suggested, lowercase hgnc):** WNT4 (hgnc:12782), EFEMP1 (hgnc:3218), WT1 (hgnc:12796), FGFR2 (hgnc:3689), LOXL1 (hgnc:6664), FBLN5 (hgnc:3602), COL1A1 (hgnc:2197), COL3A1 (hgnc:2201), MMP2 (hgnc:7166), MMP9 (hgnc:7176), TIMP1 (hgnc:11820).

### Variant classification / type
GWAS signals are **common non-coding regulatory variants** (SNPs) of small effect (OR ~1.05–1.5), not coding pathogenic variants. No ACMG "pathogenic" single-gene classification applies to idiopathic POP. In the monogenic connective-tissue disorders that cause secondary POP (COL5A1/COL5A2 in classical EDS; FBN1 in Marfan), variants are pathogenic missense/null per ClinVar.

**Somatic vs germline:** entirely **germline** susceptibility; POP is a degenerative/mechanical condition, not neoplastic — no somatic driver landscape.

**Functional consequences:** the implicated genes converge on **extracellular-matrix organization and elastogenesis** (EFEMP1/fibulin-3, LOXL1, FBLN5) and **urogenital development / estrogen signaling** (WNT4, WT1, FGFR2). Mechanistic causality at these human loci is not yet demonstrated at the protein level.

### Modifier genes
Estrogen-receptor ratio (ESR1/ESR2 balance) is proposed as a modifier of connective-tissue remodeling (PMID:31851453).

### Epigenetic information
Under-studied for POP; candidate work reports altered methylation/microRNA regulation of collagen and MMP genes in prolapsed tissue, but no ENCODE/Roadmap-level consensus dataset exists. This is a genuine gap.

### Chromosomal abnormalities
None specific to idiopathic POP.

*Sources:* PMID:32184442, PMID:39349682, [Nat Commun 2022 (PMC9226158)](https://ncbi.nlm.nih.gov/pmc/articles/PMC9226158); PMID:31851453.

---

## 5. Environmental Information

- **Environmental / occupational:** heavy manual labor and repetitive heavy lifting appear as risk factors in **surgical series** but **not** in community-recruited cohorts — a discordance suggesting ascertainment bias rather than a true dose-response (PMID:26348380): *"women recruited from the community with pelvic organ prolapse on examination report similar lifetime levels of strenuous activity as women without this examination finding."* No chemical toxicant (CTD-type) etiology.
- **Lifestyle:** obesity/high BMI (robust, PMID:18799443); chronic constipation and chronic cough (chronic straining); smoking (via chronic cough — modest/indirect). Physical activity per se does **not** increase POP risk (PMID:26348380).
- **Infectious agents:** none. POP has no microbial etiology (not applicable).

*Sources:* PMID:18799443, PMID:26348380, PMID:17382829.

---

## 6. Mechanism / Pathophysiology

The contemporary model, built on imaging of *living* women, places the **primary lesion in the levator ani muscle**, with connective-tissue failure largely **downstream** — though an older "constitutional matrix defect" model remains live. The KB entry curates both explicitly as competing hypotheses.

### Causal chain (canonical hypothesis — levator-primary)

1. **Vaginal childbirth mechanical overload** (TISSUE; GO:0009612 response to mechanical stimulus). Levator ani + birth-canal tissues stretch to **>3× resting length**; damage is by **overstretch**, not compression ischemia or neuropathy (PMID:38168908).
2. → **Levator ani muscle injury / avulsion** (TISSUE; UBERON:0001326 levator ani, UBERON:0011528 pubococcygeus; CL skeletal muscle fiber). Birth-induced pubococcygeal injury is present in **55% of women with prolapse vs 16% with normal support** (PMID:27517338), OR **7.3** (PMID:38168908); occurs in up to **19% of primiparas**; **does not heal** (permanent mechanical change). Complete/bilateral avulsion → more advanced stage, more compartments (PMID:36343586).
3. → **Urogenital hiatus enlargement / loss of levator closure** (the mechanical hinge). With the hiatus closed, pressures above/below the vaginal wall cancel; once open, exposed vaginal wall lies between abdominal and atmospheric pressure → net downward force. Enlarged hiatus "antedates prolapse" and predicts surgical failure (PMID:38168908).
4a. → **Descent of pelvic organs beyond the hymen** (direct mechanical effect).
4b. → **Failure of apical/lateral connective-tissue attachments** (cardinal/uterosacral/paravaginal): the pressure differential *"produces abnormal tension on the attachments of the pelvic organs to the pelvic sidewall"* (PMID:27517338). Notably, the measurable ligament difference is in **length, not stiffness** (PMID:27517338), constraining pure matrix-composition explanations.
5. → **Recurrence after reconstructive surgery**: standard apical suspension does not reattach the levator, so a wide hiatus persists and predicts anatomic recurrence (PMID:34270804).

### Parallel / upstream molecular arms (susceptibility)

- **Constitutional connective-tissue susceptibility** (MOLECULAR; GO:0030198 ECM organization). GWAS connective-tissue/estrogen loci + heritable connective-tissue disorders (PMID:32184442, PMID:39349682, PMID:39033997, PMID:23240798).
- **Impaired elastic-fiber assembly / postpartum elastogenesis** (MOLECULAR; GO:0004720 protein-lysine 6-oxidase activity ↓, GO:0048251 elastic fiber assembly ↓; UBERON:0000996 vagina). LOXL1–fibulin-5 program deposits new elastic fibers after delivery; deletion of either gene causes prolapse in mice (PMID:14745449, PMID:17255326).
- **Collagen / MMP-TIMP remodeling imbalance** (MOLECULAR; GO:0030574 collagen catabolic process ↑, GO:0022617 ECM disassembly ↑). Meta-analysis of 30 studies (840 cases/755 controls): **↓ type I collagen, ↓ TIMP-1; ↑ type III collagen, ↑ MMP-1/-2/-9** (PMID:38291948) — but site-dependent, with the anterior vaginal wall showing *no* difference in COL-I and MMP-1, and uterosacral-ligament findings controversial or non-significant (PMID:38291948, PMID:16398770). **Causal direction unsettled** (open knowledge gap).
- **Oxidative stress in pelvic connective tissue** (CELLULAR; GO:0006979 response to oxidative stress ↑; CL:0000057 fibroblast). ↑ 8-OHdG in prolapsed uterosacral ligament; H₂O₂ shifts uterosacral-ligament fibroblasts toward collagen catabolism in a **concentration-dependent (non-monotonic)** way — low OS stimulates synthesis, high OS flips to catabolism (PMID:26936098).
- **Vaginal-wall smooth-muscle depletion** (CELLULAR; CL:0000192 smooth muscle cell; UBERON:0000996 vagina). Reduced fractional area of nonvascular smooth muscle in anterior vaginal wall muscularis, **independent of age/stage**, present premenopausally, most marked in postmenopausal women off estrogen (PMID:12114889).
- **Estrogen withdrawal / ageing** (ORGANISM; GO:0030198 ↓). Strong epidemiologic risk factor, BUT the therapeutic corollary is refuted: past HT, HT duration, and current vaginal estrogen are **not** associated with pelvic support (PMID:28538602).
- **Chronically increased intra-abdominal load** (ORGANISM; GO:0009612 ↑). Obesity, straining, cough, lifting — best-supported is the BMI gradient (PMID:18799443); occupational/exercise causal edge is weak/inconsistent (PMID:26348380).

### Molecular pathways / processes
Wnt signaling (WNT4), FGF signaling (FGFR2), estrogen-receptor signaling, TGF-β1 (modulated by oxidative stress in fibroblasts, PMID:26936098), MMP/TIMP proteolytic balance, elastic-fiber assembly (fibulin-5/LOXL1/tropoelastin), collagen fibrillogenesis.

### Molecular profiling
- **Transcriptomics/proteomics:** vaginal fibroblasts from POP produce stiffer, higher-collagen matrices in some studies (Nature Sci Rep) — an apparent contradiction with the "weaker matrix" narrative, reinforcing site/context dependence.
- **Metabolomics/lipidomics/single-cell/spatial:** largely absent for POP — a genuine data gap.

*Sources:* PMID:27517338, PMID:38168908, PMID:36343586, PMID:34270804, PMID:38291948, PMID:16398770, PMID:26936098, PMID:12114889, PMID:14745449, PMID:17255326, PMID:28538602, PMID:18799443, PMID:26348380, PMID:32184442, PMID:39349682.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** vagina (UBERON:0000996), uterus (UBERON:0000995), urinary bladder (UBERON:0001255 → cystocele), rectum (UBERON:0001052 → rectocele), small intestine (enterocele). **Secondary:** urethra (voiding dysfunction), ureters (hydronephrosis in procidentia). **Body systems:** female reproductive + lower urinary tract + lower GI (pelvic floor).

**Support-structure level:** levator ani muscle (UBERON:0001326), pubococcygeus (UBERON:0011528), pubovisceralis/puborectalis; cardinal ligament, uterosacral ligament (UBERON:0012332), paravaginal/pubocervical fascia, perineal body, urogenital hiatus.

**Tissue level:** skeletal muscle (levator), dense connective tissue/ligament, vaginal wall muscularis (smooth muscle), fibroelastic ECM.

**Cell level:** levator skeletal muscle fibers (CL:0008002), fibroblasts (CL:0000057, uterosacral-ligament and pelvic connective-tissue fibroblasts), vaginal smooth-muscle cells (CL:0000192).

**Subcellular / GO cellular component:** extracellular matrix (GO:0031012), collagen-containing ECM (GO:0062023), elastic fiber (GO:0071953), fibroblast cytoplasm/mitochondria (oxidative stress).

**Localization / lateralization:** compartmentalized — **anterior** (cystocele, most common ~69%), **apical** (uterine/vault, ~39%), **posterior** (rectocele, ~16%); levator avulsion may be unilateral or bilateral (bilateral → worse).

*Sources:* PMID:27517338, PMID:36343586, [POP-Q compartment review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10682140/).

---

## 8. Temporal Development

- **Onset:** adult, typically **peri- to post-menopausal**; anatomic descent may begin in reproductive years post-delivery ("antedate" hiatal enlargement precedes overt prolapse; PMID:38168908). Onset is **chronic/insidious**, punctuated by the acute levator injury event at delivery.
- **Progression / staging:** POP-Q stages 0–4 (§10); course is generally **slowly progressive** with ageing/estrogen loss, but individual anatomic points can fluctuate and mild prolapse can regress. Symptom onset classically at leading edge ≈ hymen.
- **Duration:** chronic, lifelong tendency; the levator lesion is permanent and untreated by current surgery.
- **Remission:** spontaneous regression of *mild* descent occurs; symptomatic relief via pessary or surgery is treatment-induced, not cure of the underlying muscular lesion.
- **Critical periods / windows of intervention:** the peripartum window (birth injury prevention; postpartum elastogenesis) is the key modifiable window; menopause is a secondary inflection.

*Sources:* PMID:38168908, PMID:31851453; [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK563229/).

---

## 9. Inheritance and Population

### Epidemiology
- **Symptomatic point prevalence (US, NHANES 2005-06, women ≥20):** **2.9% (95% CI 2.1–3.7%)** report seeing/feeling a vaginal bulge (PMID:18799443). *"2.9% of women (95% CI, 2.1%-3.7%) experiencing pelvic organ prolapse."* (≈2,900 / 100,000)
- **Anatomic prevalence on exam is far higher:** 26.5% (40–59 y), 36.8% (60–79 y), 49.7% (≥80 y) (PMID:31851453). Reported prevalence ranges 1–65% depending on ascertainment (symptom 1–31%; exam 10–50%; both 20–65%).
- **Lifetime prevalence (high-income):** **~40%** of women will experience prolapse in their lifetime (PMID:33207004): *"About 40% of women will experience prolapse in their lifetime, with the proportion expected to rise in line with an ageing population."*
- **Lifetime risk of prolapse surgery (US, to age 80):** **12.6%** (PMID:24807341), from a claims database of 10.2M women — a lower bound sensitive to access/practice patterns.
- **Trend:** burden rising with population ageing (elderly population expected to double by ~2030).

### Genetic epidemiology
- **Inheritance pattern:** **multifactorial / polygenic** (complex trait); familial clustering and twin studies support heritability; **not** simple Mendelian for idiopathic POP.
- **Penetrance/expressivity:** not applicable in Mendelian terms; polygenic risk with variable expressivity modulated by parity, BMI, age.
- **Carrier frequency / founder effects:** GWAS risk alleles are common across populations; **cross-ancestry directional consistency (21/24 European loci)** in Japanese data argues shared architecture rather than population-specific founder effects (PMID:39349682).
- **Monogenic contribution:** heritable connective-tissue disorders (EDS, Marfan, joint hypermobility) show markedly elevated POP burden — **POP prevalence 29–75% in EDS**, urinary incontinence 50–60% (PMID:39033997); POP is objectively more severe by POP-Q in benign joint hypermobility syndrome (PMID:23240798).

### Population demographics
- **Sex:** essentially **female-specific** (analogous male pelvic-floor descent is rare/distinct).
- **Age distribution:** strongly skewed to older/postmenopausal women.
- **Ethnicity/geography:** higher reported rates in Hispanic and White women; lower in Black and Asian women in several US cohorts — partly true biology, partly ascertainment.

*Sources:* PMID:18799443, PMID:33207004, PMID:24807341, PMID:31851453, PMID:39349682, PMID:39033997, PMID:23240798; [IUGA epidemiology consultation](https://link.springer.com/article/10.1007/s00192-021-05018-z), [Current Opinion in Urology (PMID:23619578)](https://pubmed.ncbi.nlm.nih.gov/23619578/).

---

## 10. Diagnostics

**Primary diagnosis is clinical**, by history (specific symptom = vaginal bulge) plus physical examination.

### Clinical examination & staging — POP-Q (gold standard)
- **POP-Q (Pelvic Organ Prolapse Quantification, 1996/ICS)** measures 9 points relative to the hymen: anterior **Aa, Ba**; apical **C, D**; posterior **Ap, Bp**; plus genital hiatus (gh), perineal body (pb), total vaginal length (tvl).
- **Stages:** **0** = no prolapse; **I** = leading edge >1 cm above hymen; **II** = −1 to +1 cm (at hymen); **III** = >+1 cm but < (tvl−2); **IV** = complete eversion/procidentia.
- Examination during **Valsalva/cough**, split-speculum/Sims technique, evaluating all 3 compartments.
- Historic Baden-Walker halfway system still used clinically.

### Imaging & functional tests
- **Translabial/transperineal ultrasound** — quantifies levator avulsion and hiatal area; correlates with POP-Q (PMID:36343586).
- **Dynamic (defecography) MRI** — evaluates multi-compartment and posterior/enterocele.
- **Urodynamics** — when concurrent urinary symptoms/occult stress incontinence (reduce prolapse to unmask).
- **Post-void residual, uroflow** — voiding dysfunction assessment.

### Laboratory / biomarkers
- **No validated diagnostic blood/urine biomarker.** Urinalysis to exclude infection; renal function/renal ultrasound in procidentia (obstructive uropathy).
- Research biomarkers (tissue collagen I/III ratio, MMP/TIMP, elastin) are **not** clinically deployed.

### Genetic / omics testing
- Not indicated for idiopathic POP. Consider connective-tissue-disorder work-up (clinical criteria ± gene panel: COL5A1/COL5A2, FBN1, etc.) when EDS/Marfan/hypermobility features present.

### Clinical criteria & differential diagnosis
- Society guidance: ACOG/AUGS, ICS/IUGA, NICE.
- **Differential:** vaginal/cervical cysts or masses, urethral diverticulum, Gartner duct cyst, vaginal/cervical malignancy, large introital condyloma, prolapsed uterine fibroid — distinguished by exam ± imaging.

### Screening
- **No population screening** for asymptomatic POP is recommended (anatomy-symptom discordance; treatment is symptom-driven).

*Sources:* [POP-Q staging (PMID:21505577)](https://pubmed.ncbi.nlm.nih.gov/21505577/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK563229/), [IUGA clinical evaluation (PMC10682140)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10682140/), PMID:36343586.

---

## 11. Outcome / Prognosis

- **Mortality:** POP is **not directly life-threatening**; disease-specific mortality is negligible except rare complications (obstructive uropathy → renal failure, or ulcerated procidentia). No 5-/10-year survival framework applies.
- **Morbidity / function:** substantial QoL and functional impairment — voiding/defecatory dysfunction, sexual dysfunction, physical/social limitation. Measured by PFDI-20, PFIQ-7, PISQ-12, P-QoL.
- **Complications:** vaginal erosion/ulceration and bleeding (advanced), urinary retention/recurrent UTI, hydronephrosis (procidentia), obstructed defecation; **mesh-related** complications after surgery (erosion/exposure, pain).
- **Recovery / recurrence:** conservative therapy manages symptoms without anatomic cure. Surgery is effective but **recurrence is common**; **enlarged genital hiatus predicts recurrence** after apical suspension (PMID:34270804). Sacrocolpopexy is anatomically superior to vaginal apical procedures (PMID:23633316).
- **Prognostic factors:** POP-Q stage, levator avulsion (esp. bilateral/complete — worse; PMID:36343586), genital hiatus width, BMI, connective-tissue disorder, prior failed repair. No validated molecular prognostic biomarker.

*Sources:* PMID:34270804, PMID:23633316, PMID:36343586; [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK563229/).

---

## 12. Treatment

Management is **graded and symptom-driven**; none of the current options repairs the underlying levator injury.

### Conservative / first-line
- **Observation/expectant management** — for asymptomatic or mildly symptomatic (NCIT:C64263 Watchful Waiting / NCIT:C15747 Supportive Care).
- **Pelvic floor muscle training (PFMT)** — NCIT:C15302 (Physical Therapy). The POPPY multicentre RCT showed **symptom-score improvement** with one-to-one PFMT in stage I–III POP; anatomy was not the endpoint (PMID:24290404).
- **Vaginal pessary** (mechanical device) — NCIT:C50077-type device. Cochrane: pessary added to PFMT **probably improves symptoms and prolapse-specific QoL**; pessary vs no treatment/vs PFMT alone remains uncertain (PMID:33207004).
- **Lifestyle:** weight loss, constipation treatment, reduction of heavy lifting (modifiable-load components; note no prevention strategy is proven effective — PMID:17382829).

### Pharmacotherapy
- **Vaginal estrogen** — commonly used adjunct, especially with atrophy/pessary use; **but does not improve pelvic support** in a 1443-woman study (PMID:28538602). NCIT:C15986 Pharmacotherapy + therapeutic_agent estradiol (CHEBI:23965). Evidence for POP outcomes is weak.
- No disease-modifying drug exists.

### Surgical / interventional
- **Apical suspension is the cornerstone.** **Sacrocolpopexy** (abdominal/laparoscopic/robotic, Y-shaped polypropylene mesh to sacral promontory) — anatomically superior "gold standard" for apical/vault prolapse (PMID:23633316) — NCIT:C15329 Surgical Procedure.
- **Native-tissue vaginal repairs:** sacrospinous ligament fixation, uterosacral ligament suspension, anterior/posterior colporrhaphy.
- **Obliterative:** colpocleisis (for frail patients not desiring vaginal function).
- **Hysterectomy** ± apical suspension for uterine prolapse; uterine-preserving hysteropexy as alternative.
- **Transvaginal synthetic mesh:** durable anatomically **but** FDA reclassified to Class III (2016) and withdrew from US market (2019) over erosion/pain; restricted internationally to complex recurrent cases in specialist centers (PMID:23633316; [synthetic mesh review](https://www.mdpi.com/2563-6499/6/1/2)).
- **Recurrence** after sacrocolpopexy remains a surgical challenge; hiatus width predicts failure (PMID:34270804).

### Treatment outcomes / adverse events
- Sacrocolpopexy: high anatomic success; risks include mesh exposure, bowel injury, sacral bleeding. Transvaginal mesh: mesh erosion/exposure, dyspareunia, chronic pelvic pain. Native-tissue repair: higher recurrence but no mesh risk.

### Experimental / regenerative
- Regenerative approaches (ECM hydrogels for birth-injured pelvic muscle in animal models; stem-cell/tissue-engineering scaffolds) are **preclinical/early-phase** ([bioRxiv ECM hydrogel](https://www.biorxiv.org/content/10.1101/2021.05.28.446170.full.pdf)); ongoing trials on ClinicalTrials.gov (e.g., laser therapy NCT05000957 — investigational, evidence limited).

**Suggested NCIT terms:** C15302 (Physical Therapy), C15747 (Supportive Care), C15329 (Surgical Procedure), C15986 (Pharmacotherapy), C64263 (Watchful Waiting).

*Sources:* PMID:24290404, PMID:33207004, PMID:23633316, PMID:34270804, PMID:28538602, PMID:17382829; [surgical guideline review (IJGO 2024)](https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/ijgo.15614).

---

## 13. Prevention

- **Primary prevention:** the key lever is **reducing obstetric levator injury** — the birth-injury literature frames it as *"life-altering and preventable"* (PMID:38168908) via management of forceps use, prolonged second stage, macrosomia; cesarean avoids levator overstretch but is not recommended solely for POP prevention. Weight management, constipation treatment. **Caveat:** no prevention strategy has been definitively proven effective (PMID:17382829), and restricting physical activity is not warranted (PMID:26348380).
- **Secondary prevention (early detection):** no population screening; opportunistic identification of at-risk women (post-instrumental delivery, connective-tissue disorders); postpartum PFMT.
- **Tertiary prevention:** PFMT and pessary to slow progression/manage symptoms; optimizing genital-hiatus management at surgery to reduce recurrence (PMID:34270804).
- **Behavioral:** postpartum and ongoing pelvic-floor exercise; weight/constipation management.
- **Counseling:** genetic/family counseling relevant only in heritable connective-tissue disorders.
- **Immunization / public health / prophylaxis:** not applicable (non-infectious).

*Sources:* PMID:38168908, PMID:17382829, PMID:26348380, PMID:34270804.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** naturally occurring pelvic organ/vaginal/uterine prolapse is documented in several mammals — **cattle (*Bos taurus*, NCBITaxon:9913)** and **sheep (*Ovis aries*, NCBITaxon:9940)** show peri-/postpartum vaginal and uterine prolapse of major veterinary importance; also swine, dogs (NCBITaxon:9615), and non-human primates.
- **Comparative biology:** **Fbln5-null mouse prolapse is "remarkably similar to that in primates"** (PMID:17255326), supporting cross-species conservation of the elastic-fiber-dependent support mechanism. Non-human primates develop spontaneous POP and are used as a translational model.
- **Veterinary relevance:** bovine/ovine vaginal-uterine prolapse is a recognized peripartum emergency (genetic predisposition, hypocalcemia, high intra-abdominal pressure) — an economically important condition managed surgically/with retention devices.
- **Transmission / zoonosis:** not applicable (non-communicable).

*Sources:* PMID:17255326; OMIA (veterinary), general veterinary obstetrics literature.

---

## 15. Model Organisms

**Mouse knockouts are the workhorse** (systematic review of 5 models, PMID:35088092): *"Loxl1 and Fbln5 give the most reliable phenotype, and they fail by different routes (failure to heal after birth versus prolapse with ageing)."*

| Model | Type | Gene | Phenotype recapitulation | Fidelity / limitation |
|---|---|---|---|---|
| **Loxl1−/− mouse** | Knockout | LOXL1 | Fails to deposit normal elastic fibers in uterine tract **post partum**; develops POP + lax skin, emphysema, vascular abnormality (PMID:14745449) | Systemic elastinopathy, not pelvis-restricted; failure-to-heal-after-birth route |
| **Fbln5−/− mouse** | Knockout | FBLN5/fibulin-5 | POP developing **with age**; postpartum elastic-fiber assembly is what normal recovery depends on; *"remarkably similar to primates"* (PMID:17255326) | Age-driven; humanization/translational validity is an open question |
| Other KO models | Various | e.g., elastin/matrix genes | Less reliable phenotypes | Reviewed PMID:35088092 |
| **Non-human primate** | Natural/spontaneous | — | Spontaneous POP; closest anatomic homology | Cost, availability |
| **iPSC / vaginal-fibroblast cultures** | In vitro | — | Model ECM production; POP fibroblasts alter matrix stiffness/collagen (Sci Rep) | Loss of 3D mechanical context |
| **Simulated/induced (ovariectomy, mechanical/birth-injury rodent)** | Induced | — | Model hormonal and birth-injury contributions; ECM hydrogel rescue tested (bioRxiv) | Rodent hiatal anatomy differs from human |

**Model characteristics.** Strength: KO models demonstrate that an **elastogenesis defect alone is sufficient** to cause POP without obstetric trauma — the key support for the "constitutional matrix defect" hypothesis that cross-sectional human data cannot supply (PMID:35088092). **Limitations:** mice are quadrupedal with different pelvic-floor loading; systemic elastinopathies (Loxl1) affect multiple organs; the human primary lesion (levator avulsion) is **not** captured by these matrix-gene KOs — a genuine **human-model mismatch** flagged in the KB entry.

**Resources:** MGI, IMPC/KOMP (Loxl1, Fbln5 alleles), Alliance of Genome Resources.

*Sources:* PMID:35088092, PMID:14745449, PMID:17255326; [ECM hydrogel birth-injury model (bioRxiv)](https://www.biorxiv.org/content/10.1101/2021.05.28.446170.full.pdf).

---

## Summary of Key Ontology Term Suggestions

- **Disease:** MONDO:0000082
- **Phenotypes (HP):** HP:0100615 (POP), HP:0009611 (Cystocele), HP:0100823 (Rectocele), HP:0000139 (Uterine prolapse), HP:0000020 (Urinary incontinence), HP:0030016 (Dyspareunia), HP:0002019 (Constipation)
- **Biological processes (GO):** GO:0030198 (ECM organization), GO:0048251 (elastic fiber assembly), GO:0030574 (collagen catabolic process), GO:0022617 (ECM disassembly), GO:0006979 (response to oxidative stress), GO:0009612 (response to mechanical stimulus)
- **Molecular function (GO):** GO:0004720 (protein-lysine 6-oxidase activity)
- **Cell types (CL):** CL:0008002 (skeletal muscle fiber), CL:0000057 (fibroblast), CL:0000192 (smooth muscle cell)
- **Anatomy (UBERON):** UBERON:0001326 (levator ani), UBERON:0011528 (pubococcygeus), UBERON:0000996 (vagina), UBERON:0000995 (uterus), UBERON:0012332 (uterosacral ligament)
- **Genes (hgnc):** WNT4, EFEMP1, WT1, FGFR2, LOXL1, FBLN5, COL1A1, COL3A1, MMP2, MMP9, TIMP1
- **Treatments (NCIT):** C15302, C15747, C15329, C15986, C64263
- **Species (NCBITaxon):** 9606 (human), 10090 (mouse), 9913 (cattle), 9940 (sheep)

---

## Consolidated Source List

**Primary literature (PMIDs):** 17382829, 27517338, 38168908, 36343586, 32184442, 39349682, 14745449, 17255326, 35088092, 38291948, 26936098, 16398770, 12114889, 18799443, 24807341, 24290404, 33207004, 23633316, 28538602, 26348380, 23240798, 39033997, 34270804, 31851453, 23619578, 21505577.

**Web sources:**
- [MONDO:0000082 (Monarch)](https://monarchinitiative.org/MONDO:0000082)
- [StatPearls — Pelvic Organ Prolapse (NBK563229)](https://www.ncbi.nlm.nih.gov/books/NBK563229/)
- [Narrative review of POP epidemiology/pathophysiology (PMC6968909)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6968909/)
- [IUGA consultation — epidemiology (Int Urogynecol J)](https://link.springer.com/article/10.1007/s00192-021-05018-z)
- [IUGA consultation — clinical evaluation (PMC10682140)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10682140/)
- [GWAS meta-analysis, 19 novel loci (Nat Commun 2022, PMC9226158)](https://ncbi.nlm.nih.gov/pmc/articles/PMC9226158)
- [Japanese/cross-ancestry GWAS (Commun Biol 2024, PMC11443051)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443051/)
- [Iceland+UKB GWAS (Commun Biol 2020)](https://www.nature.com/articles/s42003-020-0857-9)
- [ECM meta-analysis (BJOG 2024)](https://obgyn.onlinelibrary.wiley.com/doi/10.1111/1471-0528.17768)
- [Molecular mechanism of ECM disorder in POP (PMC7716395)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7716395/)
- [POP-Q staging (PMID:21505577)](https://pubmed.ncbi.nlm.nih.gov/21505577/)
- [ICD-10 N81 (AAPC)](https://www.aapc.com/codes/icd-10-codes/N81)
- [Surgical guideline review (IJGO 2024)](https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/ijgo.15614)
- [Synthetic meshes in POP — narrative review (MDPI 2024)](https://www.mdpi.com/2563-6499/6/1/2)
- [Merck Manual — Overview of POP](https://www.merckmanuals.com/professional/gynecology-and-obstetrics/pelvic-organ-prolapse-pop/overview-of-pelvic-organ-prolapse-pop)
- [ECM hydrogel birth-injury model (bioRxiv)](https://www.biorxiv.org/content/10.1101/2021.05.28.446170.full.pdf)

---

**Overall assessment / curation note.** POP is a paradigm "complex" entry: its strongest, largest-effect mechanistic claim (birth-induced levator avulsion, OR 7.3) rests on human imaging, while its molecular story (collagen/MMP/elastin imbalance) rests on cross-sectional tissue studies whose causal direction is genuinely unsettled — best curated as **competing hypotheses** (levator-primary vs constitutional-matrix-primary) rather than a single linear pathway. The animal (Loxl1/Fbln5) evidence uniquely establishes *sufficiency* of a matrix defect but does not capture the human primary lesion. The therapeutic corollary of the estrogen/ageing risk factor is **refuted** (hormone therapy does not restore support), a nuance worth preserving. The existing `kb/disorders/Pelvic_Organ_Prolapse.yaml` entry already models this structure faithfully with verified snippets; this report corroborates it and adds current identifier, staging (POP-Q), GWAS (19-loci meta-analysis; FGFR2/WT1 cross-ancestry), and surgical-guideline detail.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 34 |
| On topic | 29 |
| Off topic | 0 |

All extracted references resolved successfully.