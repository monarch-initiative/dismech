---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T00:48:25.997875'
end_time: '2026-08-10T00:54:20.737724'
duration_seconds: 354.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infective Endocarditis
  mondo_id: ''
  category: Infectious
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 24
  num_turns: 29
  total_cost_usd: 2.0937807000000004
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infective Endocarditis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Infective Endocarditis** covering all of the
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

# Infective Endocarditis: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Infective endocarditis (IE) is a life-threatening infection of the endocardial surface of the heart — most commonly the cardiac valves (native or prosthetic), but also the mural endocardium, septal defects, or indwelling intracardiac devices (pacemaker/ICD leads, prosthetic valve sewing rings). It is characterized by microbial colonization of a fibrin-platelet vegetation on damaged or abnormal endothelium, producing local tissue destruction (valve regurgitation/perforation, abscess), immune-mediated phenomena (glomerulonephritis, vasculitic skin/eye lesions), and systemic septic embolization. The StatPearls overview states plainly: "Infective endocarditis is an inflammatory condition of the endocardium, the inner lining of the heart, including the valves" (PMID not separately assigned to StatPearls chapter; NCBI Bookshelf NBK557641). A 2020 review states "Infective endocarditis (IE) is an infection of the endothelium of the heart" with an annual incidence of 3–10/100,000 population and mortality "of up to 30% at 30 days" (PMID:31941729).

**Key identifiers:**
- **MONDO:** MONDO:0000565 (infective endocarditis)
- **OMIM:** No single-gene Mendelian OMIM phenotype entry exists for IE itself (it is not a monogenic disorder); OMIM entries are relevant only for underlying predisposing structural/connective-tissue conditions (e.g., bicuspid aortic valve, Marfan syndrome, hypertrophic cardiomyopathy)
- **Orphanet:** Not a rare/orphan disease per se (common acquired infection); Orphanet indexes it primarily under structural/valvular predisposition syndromes rather than as its own ORPHA entity
- **ICD-10-CM:** I33.0 (Acute and subacute infective endocarditis); I38 (Endocarditis, valve unspecified); I39 (Endocarditis and heart valve disorders in diseases classified elsewhere)
- **ICD-11:** BC63 (Infective endocarditis)
- **MeSH:** D004696 (Endocarditis, Bacterial) / D004697 (Endocarditis, Subacute Bacterial)
- **Synonyms:** Bacterial endocarditis, infectious endocarditis, subacute bacterial endocarditis (SBE), acute bacterial endocarditis (ABE), infective endocarditis (IE), endocarditis lenta (historical)

**Data derivation.** Knowledge about IE derives predominantly from **aggregated disease-level clinical resources**: multicenter prospective cohorts (e.g., the International Collaboration on Endocarditis — ICE-PCS registry), population-level epidemiologic surveillance (Global Burden of Disease, national hospital discharge/administrative databases), and clinical trial/guideline literature (AHA, ESC), rather than from individual case-level curated genetic databases as would apply to a monogenic disease. Some individual EHR-derived cohort statistics are cited below (e.g., Swedish national registry, U.S. NIS/IQVIA claims data).

---

## 2. Etiology

### Disease Causal Factors
IE is fundamentally an **infectious** disease requiring two converging processes: (1) an abnormal/damaged endocardial surface that generates a nidus of sterile platelet-fibrin thrombus (non-bacterial thrombotic endocarditis, NBTE), and (2) transient or sustained bacteremia/fungemia that seeds that nidus. It is not a genetic (Mendelian) disease, but genetic and structural cardiac factors substantially modify individual risk.

**Causative microorganisms and approximate proportions** (PMID:31941729; StatPearls NBK557641; PMC6964163):
- *Staphylococcus aureus* — ~26.6–30% of cases (now the single most common pathogen overall, and dominant in healthcare-associated/IVDU-associated IE); associated with the most aggressive, acute presentation and worst outcomes
- Viridans group streptococci (*S. sanguinis*, *S. mitis*, *S. oralis*, *S. mutans*, etc.) — ~18.7–20%; classic cause of subacute native-valve, community-acquired IE originating from the oral cavity
- Other streptococci (including *Streptococcus gallolyticus* [bovis], associated with colonic neoplasia) — ~17.5%
- Enterococci (*E. faecalis*, *E. faecium*) — ~10.5%, increasing in proportion, linked to rising antimicrobial use and healthcare exposure
- Coagulase-negative staphylococci (*S. epidermidis* and others) — dominant cause of early prosthetic-valve IE
- HACEK organisms (*Haemophilus*, *Aggregatibacter* [formerly *Actinobacillus*], *Cardiobacterium*, *Eikenella*, *Kingella*) — fastidious oral-cavity Gram-negative commensals, a classic cause of culture-negative or slow-growing-culture IE
- Fungi (predominantly *Candida* spp., especially *C. albicans*, also *C. parapsilosis*, *C. tropicalis*, *C. glabrata*) — ~1–3% of all IE but with mortality >70% hospital-mortality rates cited at 33–47%; strongly associated with prosthetic valves, cardiac implantable devices, and injection drug use
- Culture-negative organisms requiring specialized serology/PCR: *Coxiella burnetii* (Q fever — "the most frequent etiological agent of blood culture-negative infective endocarditis worldwide"), *Bartonella* spp. (*B. henselae*, *B. quintana* — biofilm-associated, linked to homelessness/body lice exposure), *Tropheryma whipplei* (Whipple disease), *Brucella* spp., *Legionella*, and non-*Candida* fungi
- "Together [staphylococci, streptococci, and enterococci] account for 80–90% of all cases" (PMID:31941729)

### Risk Factors

**Genetic/host risk factors:**
- Congenital structural cardiac lesions: bicuspid aortic valve (BAV; prevalence 0.5–2.0% of the population, IE incidence 1.8–2% in BAV patients, "the risk of IE can be increased more than 140 times by congenital heart disease"), unrepaired cyanotic congenital heart disease, ventricular septal defect, patent ductus arteriosus
- Connective-tissue/valvulopathy syndromes predisposing via myxomatous degeneration: mitral valve prolapse (MVP), Marfan syndrome (FBN1), Loeys-Dietz syndrome
- Prior rheumatic heart disease (chronic streptococcal valvular scarring)
- Hypertrophic obstructive cardiomyopathy (turbulent flow across LVOT)
- Host innate-immunity gene polymorphisms modifying susceptibility once bacteremic: functional variants in **TLR2** and **TLR5** ("TLR polymorphisms... have been strongly associated with increased susceptibility to IE"), **IL6** (the IL6 c.471+870G>A genotype associated with increased susceptibility), **IL1B**, **IL10**, **IL12B**, **TNF**, **SELE** (E-selectin), and **ICAM1**, implicating dysregulated innate immunity/cytokine signaling and endothelial adhesion pathways (PMID:25360655 [Genetic Variants in Genes of the Inflammatory Response in Association with Infective Endocarditis, PLOS ONE]). A genome-wide association study of *S. aureus* native-valve IE (67 cases vs. 72 *S. aureus*-bacteremic controls without IE) identified four SNPs on chromosome 3 approaching but not reaching genome-wide significance (P<1×10⁻⁵), underscoring that host genetic architecture of susceptibility remains incompletely defined (PMC5893849).

**Environmental/acquired risk factors:**
- Injection drug use (IDU/IVDU): "a 50- to 100-fold higher incidence of IE compared to the general population," via endothelial injury from injected particulate matter, direct inoculation of skin/oral flora (notably *S. aureus*), and vasospasm-induced intimal damage; disproportionately causes right-sided (tricuspid) IE
- Prosthetic heart valves (mechanical or bioprosthetic): incidence 0.3–1.2% per patient-year; highest risk in the first 6–12 months post-implantation (early PVE, dominated by coagulase-negative staphylococci and perioperative contamination) vs. late PVE (organism spectrum resembling native-valve IE)
- Cardiac implantable electronic devices (CIEDs): pacemakers, ICDs — lead-associated infection and device-pocket seeding
- Chronic hemodialysis (repeated vascular-access bacteremia)
- Poor dentition/periodontal disease and invasive dental procedures (viridans streptococcal bacteremia)
- Advanced age (rising incidence in the 55+ population — see Epidemiology)
- Immunocompromised states, including HIV infection, diabetes mellitus (affecting up to one-third of North American IE patients), chronic liver disease, malignancy
- Indwelling central venous catheters, healthcare-associated bacteremia, recent cardiac surgery/transcatheter valve implantation (TAVI)
- Male sex (male:female ratio ~3:2, ranging 3:2 to 9:1 across series)

### Protective Factors
No well-established genetic protective variants have been robustly replicated for IE specifically. General protective factors are indirect: good oral hygiene/regular dental care (reduces bacteremic seeding events), harm-reduction practices in people who inject drugs (sterile injection equipment, supervised consumption sites — reduces endothelial injury and inoculation), prompt treatment of *S. aureus* bacteremia to prevent secondary valve seeding, and (controversially) antibiotic prophylaxis before invasive dental procedures in high-risk cardiac-lesion patients (discussed under Prevention).

### Gene-Environment Interactions
The clearest gene-environment interaction model in IE is a **"two-hit" framework**: an anatomic/structural or genetically-determined endocardial abnormality (bicuspid valve, MVP, prosthetic material) creates the substrate for NBTE formation, while an environmentally-determined bacteremic event (dental procedure, IDU, catheter-associated infection, dialysis access) provides the inoculum. Superimposed on this, polymorphisms in innate-immune genes (TLR2/TLR5, IL6, IL10) appear to modulate whether transient bacteremia in a structurally predisposed host progresses to established valvular infection versus is cleared — i.e., a genetic modifier of the environmentally-triggered infectious event, rather than a primary causal genetic lesion.

---

## 3. Phenotypes

IE phenotypes span constitutional/systemic symptoms, cardiac signs, immune-complex-mediated peripheral stigmata, embolic phenomena, and laboratory abnormalities.

| Phenotype | Type | Frequency | Onset/Course | HPO term (suggested) |
|---|---|---|---|---|
| Fever | Symptom/sign | >95% of cases ("Fever...is present in more than 95% of cases") | Acute (S. aureus) or subacute/low-grade (viridans strep); often the presenting complaint | HP:0001945 (Fever) |
| New or changing heart murmur | Clinical sign | ~48–85% (varies by valve/organism) | Progressive as vegetation/regurgitation worsens | HP:0031264 (Cardiac murmur) |
| Splinter hemorrhages | Physical/dermatologic sign | ~15% (nonspecific) | Subacute; immune-complex or micro-embolic | HP:0100651 (Nail dysplasia) — no exact term; closest is HP:0040242 (splinter hemorrhage not in core HPO; consider free-text) |
| Osler nodes | Physical sign | ~3–15%, more with subacute disease | Tender, painful, immune-complex-mediated | HP:0100547 (Osler node — not standard HPO ID; confirm via OAK lookup) |
| Janeway lesions | Physical sign | ~5–10% | Non-tender, embolic/microabscess-mediated, seen more in acute S. aureus IE | HP:0200042 (Skin ulcer) — nearest generic; verify precise term |
| Roth spots | Ocular sign | ~2–10% | Retinal hemorrhage with pale center, immune-complex-mediated | HP:0025230 (Roth spot) |
| Splenomegaly | Sign | ~20–40% | Subacute/chronic disease | HP:0001744 (Splenomegaly) |
| Petechiae (conjunctival/mucosal/extremity) | Sign | ~20–40% | Variable | HP:0000967 (Petechiae) |
| Glomerulonephritis (immune-complex) | Renal/laboratory | Variable, part of classic triad | Subacute course | HP:0000099 (Glomerulonephritis) |
| Arthralgia/myalgia | Symptom | ~15–30% | Nonspecific systemic | HP:0002829 (Arthralgia) |
| Weight loss/malaise/night sweats | Constitutional symptom | Common in subacute disease | Insidious | HP:0001824 (Weight loss); HP:0001744 |
| Acute/worsening heart failure | Clinical sign/complication | Leading cause of morbidity and the "dominant predictor for 30-day mortality" | Can be abrupt (acute regurgitation, chordal rupture) | HP:0001635 (Congestive heart failure) |
| Embolic stroke/neurological event | Complication | 15–30% (up to 60% with vegetations >30mm) | Can be presenting event | HP:0001297 (Stroke) |
| Anemia (normocytic, of chronic disease) | Laboratory abnormality | Common in subacute IE | Progressive with disease duration | HP:0001903 (Anemia) |
| Elevated inflammatory markers (CRP, ESR) | Laboratory abnormality | Near-universal | — | HP:0011227 (Elevated CRP — verify OAK term); HP:0003565 |
| Positive blood cultures/bacteremia | Laboratory/microbiologic | Major Duke criterion | — | (Not typically HPO-coded; a laboratory/microbiologic finding) |
| Mycotic (infectious) aneurysm | Vascular complication | ~2–10% | Can present late, sometimes after treatment | HP:0004944 (Aneurysm) |

**Quality-of-life impact:** IE carries substantial acute morbidity (prolonged hospitalization, IV antibiotic courses of 4–6+ weeks, frequent cardiac surgery), and survivors — particularly those with embolic stroke, heart failure, or valve replacement — face lasting functional impairment; formal disease-specific QoL instrument data (EQ-5D/SF-36) are sparse in the IE literature relative to chronic diseases, reflecting its status as an acute, often curable infection rather than a chronic condition, though post-stroke and post-cardiac-surgery patients experience durable QoL decrements documented in the broader stroke/cardiac-surgery literature.

---

## 4. Genetic/Molecular Information

IE is **not a monogenic disease** — there are no "causal genes" in the OMIM/ClinVar sense analogous to a Mendelian disorder. Genetic information relevant to IE falls into three categories:

**(a) Host susceptibility loci** (modifier, not causal, and typically common variants of modest effect):
- **TLR2** (HGNC:11848) and **TLR5** (HGNC:11851) polymorphisms — associated with increased IE susceptibility via impaired peptidoglycan/lipoteichoic-acid/flagellin sensing
- **IL6** (HGNC:6018) c.471+870G>A — associated with increased susceptibility
- **IL1B** (HGNC:5992), **IL10** (HGNC:6018... actually HGNC:5962), **IL12B** (HGNC:5970), **TNF** (HGNC:11892), **SELE** (HGNC:10718), **ICAM1** (HGNC:5344) — inflammatory-response gene variants studied for association (PMID:25360655)
- A dedicated GWAS of *S. aureus* native-valve IE (PMC5893849) found suggestive (not genome-wide-significant) chromosome-3 loci, indicating the field lacks a robustly replicated common-variant architecture and larger studies are needed
- Functional consequence framing: these are population susceptibility/modifier alleles, not deterministic pathogenic variants — none currently meet ACMG/AMP pathogenicity criteria because there is no monogenic Mendelian trait to classify against

**(b) Predisposing-condition genes** (genes causal for the *structural substrate*, not for IE itself): e.g., **FBN1** (Marfan syndrome, OMIM:154700), **TGFBR1/TGFBR2** (Loeys-Dietz syndrome), genes underlying bicuspid aortic valve (**NOTCH1**, **GATA5**, **SMAD6**) and hypertrophic cardiomyopathy (**MYH7**, **MYBPC3**) — these create the anatomic nidus but are several causal steps removed from the infection itself.

**(c) Pathogen-side molecular determinants** — the mechanistically central "genetics" of IE lies in the microbial virulence factors, not the human genome:
- **Sortase A (SrtA)** — a *S. aureus* transpeptidase that covalently anchors LPXTG-motif surface proteins (MSCRAMMs) to peptidoglycan; essential for surface display of adhesins
- **MSCRAMMs** (Microbial Surface Components Recognizing Adhesive Matrix Molecules): **ClfA** (clumping factor A, binds fibrinogen), **FnBPA/FnBPB** (fibronectin-binding proteins A/B, bind fibronectin/fibrinogen/elastin and mediate both initial colonization and endothelial-cell invasion), and **Cna** (collagen-binding adhesin). "Experiments employing heterologous expression of the staphylococcal MSCRAMMs clumping factor A (ClfA) and fibronectin binding protein A (FnbA) in *Lactococcus lactis* suggest that these proteins mediate initial colonization and invasiveness, respectively, in staphylococcal IE." Polymorphisms in *fnbA* are associated with cardiovascular-device infection risk (PNAS PMID:21969557, PMC of PMID:21969557).
- **von Willebrand factor-binding protein (vWbp)** and **coagulase** — staphylococcal factors implicated in vegetation formation, though a rat catheter-model study found only a "marginal role" for these specific factors in initiating vegetation (PMC7000203)
- Streptococcal MSCRAMMs/pilus adhesins in *Streptococcus gallolyticus* (S. bovis group) — Acb (collagen-binding adhesin) and related pilus proteins (PMID:19717591, J Bacteriol)
- **Epigenetics:** Limited data exist on valve-tissue epigenetic changes in IE specifically; transcriptomic (not epigenomic) profiling has been the dominant molecular-profiling approach (see below).
- **Chromosomal abnormalities:** Not applicable to IE as an infectious process (no karyotypic/CNV etiology), aside from the CNVs/structural variants underlying some predisposing congenital cardiac lesions.

---

## 5. Environmental Information

- **Environmental/exposure factors:** Contaminated injection drug paraphernalia (bacterial and fungal inoculation); indwelling foreign material (catheters, prosthetic valves, CIEDs) providing a surface for biofilm formation; healthcare exposures (hemodialysis, recent hospitalization, invasive procedures)
- **Lifestyle factors:** Injection drug use is the dominant modifiable lifestyle risk factor, with a shifting demographic — "most opioid use disorder-associated IE hospitalizations [2016–2020] were among females, in stark contrast with IE due to other causes" — reflecting the opioid epidemic's changing face; poor dental hygiene; homelessness and body-lice exposure (risk factor specifically for *Bartonella quintana* IE, "trench fever" organism)
- **Infectious agents (primary etiology, detailed in §2):** Gram-positive cocci (*S. aureus*, viridans/other streptococci, enterococci, coagulase-negative staphylococci) dominate; Gram-negative HACEK organisms and fungi (*Candida* spp.) are less common but clinically important; zoonotic/atypical agents (*Coxiella burnetii*, *Bartonella* spp., *Brucella* spp.) cause a meaningful fraction of culture-negative IE and require specific serologic/molecular diagnostics (indirect immunofluorescence for *Coxiella*, EIA/PCR for *Bartonella*).

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Initial Trigger → Clinical Manifestation)

**Step 1 — Endothelial injury and NBTE formation (initiating, upstream):** Endocardial trauma from turbulent blood flow (across a stenotic/regurgitant/bicuspid valve), mechanical irritation from a catheter or prosthetic material, or immune-complex/vasculitic injury exposes the subendothelial extracellular matrix (collagen, fibronectin, tissue factor). This activates platelets and the coagulation cascade, producing a sterile fibrin-platelet thrombus — **non-bacterial thrombotic endocarditis (NBTE)**. As one review states: "Infective endocarditis is initiated by an endothelial injury that results in exposure of the subendothelial extracellular matrix that activates platelets and causes the formation of a fibrin-platelet clot" (Merck/StatPearls synthesis); "the damaged endocardium then serves as a nidus for platelet aggregation and activation of the coagulation cascade, resulting in sterile, nonbacterial thrombotic vegetations" (NBK557641).

**Step 2 — Transient bacteremia and microbial adherence (trigger event):** A bacteremic or fungemic episode (dental manipulation, IDU injection, catheter contamination, gut/mucosal translocation) delivers circulating organisms that adhere to the NBTE surface via pathogen-encoded MSCRAMMs (ClfA, FnBPA/B binding fibrinogen/fibronectin) — "subsequently, microorganisms in the blood adhere to the fibrin-platelet clot to initiate vegetation formation in infective endocarditis."

**Step 3 — Bacterial proliferation, biofilm formation, and vegetation maturation (CELLULAR/MOLECULAR):** Adherent organisms proliferate within the fibrin matrix, are shielded from host phagocytes and antibiotic penetration by the fibrin/platelet scaffold (biofilm-like protection), and continue to recruit platelets/fibrin, producing a mature, friable **vegetation** composed of fibrin, platelets, inflammatory cells, and dense microbial colonies.

**Step 4 — Host innate immune activation (parallel, CELLULAR):** Pathogen-associated molecular patterns (peptidoglycan, lipoteichoic acid via TLR2; LPS via TLR4) engage pattern-recognition receptors on monocytes/endothelium, triggering MyD88-dependent NF-κB signaling, pro-inflammatory cytokine release (IL-1β, IL-6, TNF-α), and **NLRP3 inflammasome activation** with caspase-1-mediated maturation of IL-1β/IL-18 — driving both local tissue inflammation and the systemic inflammatory/febrile response. Complement activation (membrane attack complex assembly) further amplifies endothelial NLRP3 inflammasome activity in IFN-γ-primed endothelium.

**Step 5 — Local tissue destruction (TISSUE, downstream):** Ongoing infection causes valve leaflet perforation, chordal rupture, and can extend beyond the valve annulus to form paravalvular/myocardial abscesses, pseudoaneurysms, or fistulae — mechanically producing valvular regurgitation/stenosis.

**Step 6 — Systemic embolization and immune-complex deposition (ORGANISM, downstream):** Fragments of the friable vegetation embolize to the brain (stroke, mycotic aneurysm), spleen, kidneys, and extremities (Janeway lesions), while circulating immune complexes deposit in skin (Osler nodes), retina (Roth spots), and glomeruli (immune-complex glomerulonephritis).

**Step 7 — Hemodynamic decompensation and multiorgan complications (ORGANISM, terminal common pathway):** Acute valvular regurgitation and/or myocardial abscess/conduction-system involvement (AV block) precipitate heart failure; sepsis, embolic stroke, and renal failure compound systemic decompensation — "heart failure and compromised hemodynamic status are identified as the dominant predictors for 30-day mortality."

### Cell Types and Biological Processes Involved
- **Platelets** (CL:0000233) — initial NBTE scaffold formation, aggregation
- **Endothelial cells** (CL:0000115) — injury/dysfunction, NLRP3 activation, adhesion molecule (E-selectin/ICAM-1) upregulation
- **Monocytes/macrophages** (CL:0000576/CL:0000235) — pathogen recognition, inflammasome activation, phagocytosis (often evaded within biofilm)
- **Neutrophils** (CL:0000775) — recruited to vegetation, contribute to local tissue damage
- **Fibroblasts/myofibroblasts** — organizing/healing response in chronic vegetations
- Relevant **GO Biological Process terms**: GO:0007596 (blood coagulation), GO:0030193 (regulation of blood coagulation), GO:0002376 (immune system process), GO:0006954 (inflammatory response), GO:0043123 (positive regulation of I-kappaB kinase/NF-kappaB signaling), GO:0043312 (neutrophil degranulation), GO:0002250 (adaptive immune response — for immune-complex phenomena), GO:0007599 (hemostasis)

### Molecular Profiling Data
- **Transcriptomics:** "The Transcriptional Programme of Human Heart Valves Reveals the Natural History of Infective Endocarditis" (PMID:20126625) profiled gene expression in excised human IE valve tissue, characterizing the local transcriptional response and its temporal evolution during disease.
- **Proteomics/metabolomics/lipidomics:** No large-scale disease-specific datasets identified in this search; represents a research gap relative to genomics/transcriptomics.
- **Genomic structural features:** Not applicable at the host level (non-Mendelian); pathogen genomic epidemiology (e.g., *S. aureus* clonal complex typing, agr locus variants) is an active research area for virulence correlation.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart — endocardium, cardiac valves (mitral most common in native-valve left-sided IE overall; aortic valve predominant in bicuspid-valve-associated IE; tricuspid valve predominant in IVDU-associated right-sided IE), chordae tendineae, papillary muscles, interventricular septum (in VSD-associated IE), and prosthetic valve material/annular sewing ring
- **Secondary (embolic/immune complications):** Brain (embolic stroke, mycotic aneurysm, abscess), spleen (infarct, abscess), kidney (infarct, immune-complex glomerulonephritis), lung (septic pulmonary emboli — classic in right-sided/tricuspid IE), skin (Osler nodes, Janeway lesions, petechiae), eye/retina (Roth spots), peripheral/visceral arteries (mycotic aneurysm), musculoskeletal system (septic arthritis, vertebral osteomyelitis/discitis)
- **Body systems involved:** Cardiovascular (primary), nervous (embolic/inflammatory CNS complications), renal, immune, dermatologic, ocular, musculoskeletal

**Tissue and cell level:**
- Valvular endothelium/subendothelial connective tissue — site of NBTE and infection
- Vascular endothelium (systemic) — target of embolic and immune-complex injury
- Renal glomerular basement membrane/mesangium — immune-complex deposition

**Subcellular level:**
- Platelet cytoplasmic granules (release reaction feeding NBTE)
- Endothelial cell plasma membrane (TLR/adhesion molecule expression), cytoplasm (NLRP3 inflammasome assembly), and, in host inflammatory cells, mitochondria (oxidative burst)
- Relevant GO Cellular Component: GO:0005886 (plasma membrane), GO:0032991 (protein-containing complex, for the NLRP3 inflammasome), GO:0070062 (extracellular exosome, relevant to platelet-derived microparticles)

**Localization/UBERON terms (suggested):**
- UBERON:0000948 (heart)
- UBERON:0002332 (mitral valve)
- UBERON:0002137 (aortic valve)
- UBERON:0002136 (tricuspid valve)
- UBERON:0002094 (endocardium)
- UBERON:0000955 (brain) — embolic complications
- UBERON:0002106 (spleen)
- UBERON:0002113 (kidney)
- UBERON:0001981 (blood vessel) — mycotic aneurysm

**Lateralization:** Left-sided IE (mitral/aortic) is more common overall and community-associated; right-sided IE (tricuspid, sometimes pulmonic) is strongly associated with IVDU and CIED lead infection.

---

## 8. Temporal Development

**Onset:**
- Age of onset spans the full adult lifespan, with a marked shift toward older age over recent decades (see Epidemiology); pediatric IE is uncommon (estimated 0.43–0.69 cases per 100,000 children) but occurs mainly in children with congenital heart disease or indwelling catheters/central lines, typically school-age children and adolescents, more often male
- **Onset pattern:** Classically dichotomized into **acute** (rapid, fulminant, typically *S. aureus*, high fever, rapid valve destruction, days to 1–2 weeks to presentation) and **subacute** (indolent, typically viridans streptococci or HACEK organisms, low-grade fever, weeks to months of nonspecific constitutional symptoms — historically termed "subacute bacterial endocarditis")

**Progression:**
- **Disease stages** (informal, not a formal staging system like cancer): early localized valvular infection → local extension (annular abscess, fistula) → systemic embolic/immune-complex phase → multiorgan complications/sepsis
- **Progression rate:** Rapid in acute *S. aureus* IE (valve destruction and hemodynamic collapse can occur within days); slow/insidious in subacute viridans-streptococcal or *Coxiella*/culture-negative disease (weeks to months, occasionally presenting as chronic Q fever endocarditis over years)
- **Disease course pattern:** Typically a single acute/subacute infectious episode treated to cure with antibiotics ± surgery, though relapse (within ~6 months, same organism) and reinfection (new episode, often different organism, especially in IVDU/dialysis/prosthetic-valve populations) are well described; not classically relapsing-remitting in the autoimmune sense
- **Disease duration:** Self-limited with appropriate treatment for most native-valve cases (4 weeks IV antibiotics); prosthetic-valve and complicated cases require 6+ weeks and often surgery; without treatment, IE is essentially uniformly fatal

**Patterns:**
- **Remission:** Treatment-induced (antibiotics ± surgical source control); spontaneous resolution is exceedingly rare and disease is not considered self-remitting
- **Critical periods:** The first 2 weeks of antibiotic therapy carry the highest risk of embolic events and hemodynamic decompensation, making this the critical intervention window for surgical timing decisions in patients with large/mobile vegetations or heart failure; the first 6–12 months post-prosthetic-valve-implantation is the critical period of highest risk for early PVE.

---

## 9. Inheritance and Population

### Epidemiology
- **Global incidence:** 3–10 per 100,000 population per year (PMID:31941729)
- **United States trend:** Age-standardized incidence rate (ASIR) rose from 10.2/100,000 in 1990 to 14.4/100,000 in 2019 — a 41% relative increase; increase greater in men (45.8%) than women (34.1%); driven almost entirely by the 55+ age group (112.7% relative increase in that stratum), while incidence among 5–19 year-olds fell 36.6% over the same 30-year period (American Journal of Cardiology, 2023 analysis of Global Burden of Disease data)
- **Mortality:** 30-day all-cause mortality ~10.4% in some cohorts; in-hospital mortality commonly cited 15–30% (up to ~18% in one large series, approaching 30% in early prosthetic-valve IE); one-year mortality approaching 40% in some series; post-treatment survival ~85–90% at 1 year and 70–80% at 5 years per ESC guideline synthesis

### Genetic Etiology Parameters
Because IE is an acquired infectious disease rather than a Mendelian trait, classic Mendelian-genetics parameters (inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, founder effect, carrier frequency) **do not directly apply**. What is heritable/population-structured is host **susceptibility** (innate-immune gene polymorphisms noted in §4) and the structural cardiac lesions that predispose to it (which do follow AD/AR/multifactorial inheritance in their own right — e.g., bicuspid aortic valve shows a multifactorial/oligogenic pattern with ~9% familial recurrence and identified genes including NOTCH1).

### Population Demographics
- **Sex ratio:** Male predominance, ~3:2 in most series (range 3:2–9:1 depending on cohort/organism); notable recent reversal in opioid-associated IE, where most 2016–2020 U.S. hospitalizations were among females
- **Age distribution:** Bimodal historically (rheumatic-heart-disease-associated young adults vs. degenerative-valve-disease-associated elderly), now heavily weighted toward older adults (55+) in high-income countries due to declining rheumatic fever and rising prosthetic valve/device use and healthcare-associated bacteremia; younger, IVDU-associated peak in some U.S. regions during the opioid epidemic
- **Geographic distribution:** Regional disparities documented within the U.S. (Gender, Age, and Regional Disparities study, Am J Cardiol 2023); globally, *Coxiella burnetii* IE shows marked geographic clustering (Mediterranean basin, parts of the Middle East and Asia) reflecting Q fever endemicity; rheumatic-heart-disease-associated IE remains disproportionately common in low- and middle-income countries
- **Affected/at-risk populations:** People who inject drugs, hemodialysis patients, patients with prosthetic valves/CIEDs, older adults with degenerative valve disease, patients with congenital heart disease (particularly bicuspid aortic valve)

---

## 10. Diagnostics

### Clinical Tests
- **Blood cultures:** Cornerstone of diagnosis. "Antimicrobial therapy should generally not be commenced until three sets of blood cultures have been taken; this will detect bacteraemia successfully in up to 98% of cases." LOINC-coded (e.g., LOINC:600-7 for blood culture)
- **Inflammatory/laboratory markers:** CRP, ESR, procalcitonin (PCT — "strictly tied with S. aureus etiology" and "the best predictor of poor clinical outcome"), complete blood count (anemia, leukocytosis), rheumatoid factor (immune-complex marker), complement levels (low in immune-complex glomerulonephritis), urinalysis (hematuria/proteinuria)
- **Cardiac biomarkers (prognostic):** NT-proBNP (independent predictor of in-hospital mortality, OR 14.9 in one study; levels <2926 pg/mL had 96.6% negative predictive value for favorable outcome), cardiac troponin, pro-adrenomedullin and copeptin (associated with worse prognosis)
- **Imaging:**
  - **Transthoracic echocardiography (TTE)** — first-line
  - **Transesophageal echocardiography (TEE)** — higher sensitivity for vegetations/abscess, standard in suspected/complex cases; "both TTE and TEE can provide normal or inconclusive findings in up to 30% of cases, especially in patients with prosthetic devices"
  - **Cardiac CT/CT angiography** — best for assessing perivalvular abscess/pseudoaneurysm
  - **¹⁸F-FDG PET/CT** — recommended especially for possible prosthetic-valve IE, "to both detect valvular lesions and confirm the diagnosis," and best for cardiac device infection and extracardiac septic foci
  - Multimodality comparative performance: "Echocardiography performed best in the assessment of vegetations...MDCTA performed best in the assessment of abscesses, and FDG-PET/CT performed best in the assessment of cardiac device infection, extracardiac infectious foci, and alternative diagnoses"
- **Histopathology (surgical/autopsy specimens):** Vegetation histology showing fibrin, platelets, inflammatory infiltrate, and organisms; valve tissue Gram stain and culture

### Genetic Testing
Not applicable as a diagnostic modality for IE itself (non-Mendelian). Molecular diagnostics are pathogen-directed rather than host-genome-directed:
- **PCR/broad-range 16S rRNA sequencing** and **metagenomic/amplicon sequencing** of excised valve tissue or blood — critical for culture-negative IE (fastidious/intracellular organisms)
- **Serology/EIA** for *Coxiella burnetii* (phase I/II antibody titers — gold standard for Q fever endocarditis) and *Bartonella* spp.
- **In situ hybridization** on valve tissue — newly incorporated in the 2023 Duke-ISCVID criteria

### Clinical Criteria — the Duke/Duke-ISCVID Criteria
- **Modified Duke criteria (2000):** Definite IE requires 2 major, or 1 major + 3 minor, or 5 minor criteria; major criteria = positive blood cultures (typical organism from 2 separate cultures, or persistently positive cultures) + evidence of endocardial involvement (echocardiographic vegetation/abscess/new dehiscence, or new valvular regurgitation); minor criteria include predisposing heart condition or IVDU, fever ≥38°C, vascular phenomena (emboli, mycotic aneurysm, Janeway lesions), immunologic phenomena (glomerulonephritis, Osler nodes, Roth spots, rheumatoid factor), and microbiologic evidence not meeting major criteria. Sensitivity ~80% overall, "significantly lower in cases of prosthetic valve endocarditis."
- **2023 Duke-ISCVID criteria (PMID:37138445, *Clinical Infectious Diseases* 77(4):518–526, lead author Vance G. Fowler):** Major revision adding (1) new microbiologic modalities — *Bartonella* EIA, PCR, amplicon/metagenomic sequencing, in situ hybridization; (2) advanced imaging — ¹⁸F-FDG PET/CT and cardiac CT; (3) **intraoperative inspection as a new Major Clinical Criterion** within a newly created **surgical domain** (added to the pre-existing microbiologic and imaging domains); (4) an expanded "typical organism" list, with certain pathogens counted as typical only in the presence of intracardiac prosthetic material; (5) simplified blood-culture timing requirements (removed the requirement for strict timing and separate venipuncture sites); (6) clarified predisposing conditions to explicitly include transcatheter valve implants and endovascular CIEDs. Reported sensitivity 89.4% vs. 87.9% for the 2015 ESC-modified Duke criteria in a comparative cohort.
- **Differential diagnosis:** Non-bacterial thrombotic (marantic) endocarditis, Libman-Sacks endocarditis (SLE/antiphospholipid syndrome), rheumatic valvulitis, atrial myxoma, degenerative valve calcification with sterile vegetation-mimicking lesions, culture-negative "aseptic" post-infectious endocarditis.

### Screening
No population-based screening program exists for IE (it is an acute infectious event, not amenable to presymptomatic screening); the closest analog is targeted surveillance/echocardiographic monitoring in known high-risk populations (e.g., IVDU with recurrent bacteremia, hemodialysis patients with recurrent access infections) and pre-procedural risk stratification for prophylaxis decisions (see Prevention).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- 30-day mortality: ~10.4% in one large contemporary cohort; up to 30% cited in other series
- In-hospital mortality: ~15–30% overall, "approximately 18%" in one cited series, with early prosthetic-valve endocarditis carrying the highest mortality (~30%)
- One-year mortality: approaching 40% in some cohorts
- Post-treatment survival (ESC guideline synthesis): 85–90% at 1 year, 70–80% at 5 years
- Sex/age trends in mortality are an active research area (JACC: Advances 2025, PMC12271061 — "Impact of Sex and Age on Trends of Mortality From Infective Endocarditis in High-Income Countries")

### Morbidity and Function
- "Up to 50% of patients will require surgery" during the index hospitalization
- Neurologic complications occur in 15–30% of cases, "up to 60% of patients experience neurological complications" when vegetations exceed 30mm
- Acute valvular incompetence develops in approximately one-third of cases; intracardiac abscesses in ~14%; AV block in ~8%
- Survivors of embolic stroke or requiring valve replacement face durable functional impairment (documented in general stroke/cardiac-surgery QoL literature; IE-specific disease-specific QoL instrument data are limited)

### Disease Course / Complications
- **Cardiac:** Acute heart failure/cardiogenic shock (leading mortality predictor), paravalvular abscess, fistula, conduction abnormalities/heart block, pericarditis
- **Neurologic:** Ischemic embolic stroke, intracranial hemorrhage (including from mycotic aneurysm rupture), brain abscess, meningitis
- **Renal:** Immune-complex glomerulonephritis, embolic renal infarction, acute kidney injury (from sepsis, nephrotoxic antibiotics, or hemodynamic compromise)
- **Vascular:** Septic/mycotic aneurysms (any arterial bed), splenic infarct/abscess, septic pulmonary emboli (right-sided IE)
- **Musculoskeletal:** Septic arthritis, vertebral osteomyelitis/discitis

### Prognostic Factors and Biomarkers
- Dominant predictors of mortality: heart failure/hemodynamic compromise, septic shock, uncontrolled local infection/periannular complications, *S. aureus* etiology, negative blood cultures, and failure to undergo indicated surgery
- Prognostic biomarkers: NT-proBNP (OR 14.9 for in-hospital mortality), procalcitonin, CRP (specifically associated with embolic risk), cardiac troponin (s-cTnI showed highest single-marker accuracy for mortality prediction in one multimarker study), IL-6, TNF-α, pro-adrenomedullin, copeptin

---

## 12. Treatment

### Pharmacotherapy
Antibiotic selection is organism- and susceptibility-directed, with prolonged parenteral courses (NCIT:C15986 Pharmacotherapy):
- **Streptococcal native-valve IE (penicillin-susceptible):** Ceftriaxone 2g IV daily × 4 weeks, or ceftriaxone + gentamicin (synergy regimen) × 2 weeks
- **MSSA native-valve IE:** Nafcillin/oxacillin or cefazolin × 6 weeks
- **MRSA native-valve IE:** Vancomycin or daptomycin × 6 weeks
- **Enterococcal IE:** Combination therapy — ampicillin (or penicillin G) plus an aminoglycoside (gentamicin) × 4–6 weeks (increasingly, ampicillin plus ceftriaxone dual beta-lactam regimens to reduce aminoglycoside nephrotoxicity)
- **Prosthetic-valve IE:** Minimum 6 weeks, combination therapy typically including rifampin plus gentamicin (staphylococcal PVE) to address biofilm-associated organisms
- **Fungal (Candida) IE:** Echinocandins (e.g., caspofungin, micafungin) or liposomal amphotericin B ± flucytosine as first-line, with fluconazole step-down; "no difference in either 42-day or 1-year mortality between those receiving an amphotericin B-based regimen vs those receiving an echinocandin-based regimen," and echinocandins are increasingly favored for their renal safety profile
- **Culture-negative/atypical organisms:** Doxycycline ± hydroxychloroquine for chronic *Coxiella burnetii* (Q fever) endocarditis (often prolonged, sometimes lifelong, therapy); doxycycline-based regimens for *Bartonella*

**Pharmacogenomics:** Not a major axis of IE-specific precision therapy at present (unlike oncology); relevant PGx considerations are largely generic antibiotic-safety pharmacogenomics (e.g., vancomycin nephrotoxicity monitoring, aminoglycoside ototoxicity risk) rather than IE-specific gene-drug pairs in CPIC/PharmGKB.

### Surgical and Interventional
- **Standard surgical indications** (NCIT:C15329 Surgical Procedure / NCIT:C16186 Orthopedic-analog cardiac procedure term / more precisely valve-specific procedure terms): severe heart failure from valve dysfunction, uncontrolled infection (periannular abscess, persistent bacteremia despite appropriate antibiotics, fungal/highly resistant organisms), prosthetic-valve infection, invasion beyond the leaflets (abscess/fistula/pseudoaneurysm), recurrent systemic embolization despite antibiotics, and large mobile vegetations (classically >10mm with embolic events)
- Emergency surgery (<24 hours) for cardiogenic shock; urgent surgery (within days) for progressive heart failure or uncontrolled infection
- Valve repair preferred over replacement when feasible, especially mitral/tricuspid; allograft favored for aortic valve in the setting of annular abscess; choice between mechanical and bioprosthetic valve follows standard non-IE-specific criteria (PMID:31832353, AATS 2016 consensus guidelines)

### Supportive and Rehabilitative Care
- Hemodynamic support and management of septic shock/heart failure during acute treatment; anticoagulation management is individualized (embolic risk vs. hemorrhagic transformation risk, particularly in mechanical-valve patients with concurrent stroke)
- Post-surgical cardiac rehabilitation and, where indicated, post-stroke rehabilitation (physical/occupational/speech therapy)

### Experimental / Investigational
- Bacteriophage therapy for refractory/multidrug-resistant staphylococcal or Gram-negative IE (case-report-level evidence, active investigational area)
- Novel anti-biofilm and anti-adhesin (anti-MSCRAMM) therapeutic strategies targeting FnBPA/ClfA remain preclinical
- Search of ClinicalTrials.gov identified ongoing interventional and observational trials (e.g., NCT06403839, evaluating preoperative dental screening to reduce IE risk in surgical valve-replacement patients)

### Treatment Strategy
- Treatment algorithms follow society guidelines (AHA/ACC and, more comprehensively and recently, ESC 2023): empiric broad-spectrum therapy pending cultures → organism-directed narrow-spectrum regimen once identified → reassessment for surgical indications throughout the antibiotic course, ideally via a **multidisciplinary "Endocarditis Team"** (cardiology, cardiac surgery, infectious disease, microbiology, sometimes neurology) — an ESC-endorsed structural recommendation
- Two-phase inpatient/outpatient model: "the first phase of antibiotic treatment consists of 2 weeks of in-hospital parenteral treatment," during which surgery (if indicated) is performed, followed by completion of therapy (sometimes via outpatient parenteral antibiotic therapy, OPAT, for stable patients)

For each treatment class, suggested **NCIT** terms: NCIT:C15986 (Pharmacotherapy), NCIT:C15632 (Chemotherapy — n/a here), NCIT:C15329 (Surgical Procedure), NCIT:C15289 (Organ/valve replacement — Organ Transplantation is the closest existing generic NCIT class for valve replacement framing), NCIT:C15747 (Supportive Care), NCIT:C15315 (Rehabilitation).

---

## 13. Prevention

### Prevention Levels
- **Primary prevention:** Antibiotic prophylaxis before invasive dental procedures in defined high-risk patients (see below); good oral hygiene and routine dental care for all patients with predisposing cardiac lesions; harm-reduction interventions for people who inject drugs (sterile equipment, treatment for substance use disorder) to reduce inoculation events; prompt, adequate treatment of *S. aureus* bacteremia from any source to prevent secondary valve seeding; meticulous aseptic technique for prosthetic valve/CIED implantation and catheter care
- **Secondary prevention:** Early recognition and treatment of bacteremia in high-risk patients; surveillance echocardiography in patients with recurrent bacteremia or known device infection risk
- **Tertiary prevention:** Prompt surgical intervention when indicated to prevent progression to heart failure/embolic catastrophe; long-term follow-up echocardiography after treated IE to detect relapse or valve dysfunction

### Prophylaxis — High-Risk Cardiac Conditions
Per AHA (2007 guideline, reaffirmed with no substantive changes by a 2021 AHA scientific statement) and the more recently strengthened 2023 ESC guidance (elevating dental antibiotic prophylaxis in high-risk patients to a Class I recommendation): prophylaxis is recommended **only** for patients with the **highest-risk underlying cardiac conditions**:
- Prosthetic cardiac valve or prosthetic material used for valve repair
- Previous history of infective endocarditis
- Unrepaired cyanotic congenital heart disease, or repaired congenital heart disease with residual defects at or adjacent to a prosthetic patch/device, or during the first 6 months after complete repair with prosthetic material
- Cardiac transplant recipients who develop valvulopathy
- (Notably, common lesions such as isolated mitral valve prolapse or bicuspid aortic valve **without** other high-risk features are **not** indications for prophylaxis under current AHA guidance, though some literature notes ongoing debate about extending coverage to BAV/MVP patients)

**Regimen:** Prophylaxis is reasonable for dental procedures involving manipulation of gingival tissue, the periapical region of teeth, or perforation of the oral mucosa; amoxicillin is first-line (single oral dose ~30–60 minutes before the procedure), with clindamycin, azithromycin, or cephalosporins as penicillin-allergic alternatives.

### Screening/Genetic Counseling
Not applicable in the Mendelian sense; the closest analog is structural-cardiac-lesion screening (echocardiographic identification of bicuspid aortic valve, MVP) which informs prophylaxis eligibility and long-term surveillance rather than reproductive genetic counseling.

### Public Health / Immunization
No licensed vaccine exists against the principal IE pathogens (*S. aureus* vaccine candidates have repeatedly failed in clinical trials); broader public-health measures include rheumatic-fever prevention programs (penicillin prophylaxis for rheumatic heart disease, reducing a major historical predisposing lesion in low/middle-income countries), harm-reduction services for injection drug use, and infection-control programs targeting healthcare-associated bacteremia (central-line-associated bloodstream infection [CLABSI] prevention bundles, dialysis-access care protocols).

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected species:** Domestic dogs (*Canis lupus familiaris*, NCBITaxon:9615) and cats (*Felis catus*, NCBITaxon:9685) both develop naturally occurring infective endocarditis, though it is uncommon; also described in horses and other domestic/companion animals.
- **Natural disease in companion animals:** In dogs, "endocarditis infrequently occurs in small animals and is most often caused by bacterial infections," predominantly affecting the aortic and mitral valves. A UK retrospective series of 77 canine cases (2009–2019, PMC10099803/PMC10099803, *J Small Anim Pract*) and a separate 71-patient retrospective cohort documented a canine mortality rate of ~56%, with only about half of affected dogs surviving beyond two weeks. Common canine pathogens include *Staphylococcus* spp. (~27.5%, the most common isolate in one series), *Streptococcus* spp., *Escherichia coli*, and *Bartonella* spp. Complications mirror the human disease: left-sided congestive heart failure, arrhythmias, thromboembolic disease, immune-complex glomerulonephritis, and polyarthritis. Case reports also document unusual canine pathogens including *Erysipelothrix rhusiopathiae* and *Bacillus amyloliquefaciens*.
- **Veterinary relevance:** IE is recognized as an important, high-mortality cardiac disease in veterinary internal medicine, generally underdiagnosed antemortem due to nonspecific presentation (fever, lethargy, lameness from immune-complex arthritis) preceding overt cardiac signs.
- **Comparative pathology:** The fundamental NBTE-then-bacterial-seeding pathogenic sequence appears conserved across mammals, supporting the validity of large-animal (rabbit) and rodent (rat) models for translational study (see §15).
- **Zoonotic potential:** Indirect — *Bartonella henselae* (cat-scratch disease agent) can cause IE in humans following exposure to cats, and *Coxiella burnetii* (Q fever), whose reservoir is livestock (sheep, goats, cattle) and their birth products, is a major zoonotic cause of human culture-negative IE; there is no evidence of direct dog-to-human or human-to-animal IE transmission — the shared risk is a common bacterial reservoir/exposure route rather than cross-species transmission of the disease itself.

---

## 15. Model Organisms

### Model Types and Systems
The dominant experimental models of IE are **surgically induced, catheter-based vegetation models** in mammals, not spontaneous genetic models, because IE is fundamentally an infectious rather than a genetic disease:

- **Rabbit model:** The classical and most widely used large-animal model. A polyethylene catheter is introduced (via carotid artery, into the left ventricle across the aortic valve for left-sided disease, or via jugular vein for right-sided disease) to mechanically damage the valve and induce sterile fibrin-platelet vegetations (mimicking NBTE), after which the animal is challenged intravenously with the test organism (classically *S. aureus*, viridans streptococci, or enterococci) to establish infective vegetations. A refined echocardiography-guided technique for creating right-sided *S. aureus* IE in rabbits without open surgery has been described (PMC3598207), improving reproducibility and reducing procedural morbidity. "The models described herein closely reproduced the pathogenesis and pathophysiology of right heart catheter-induced endocarditis in humans."
- **Rat model:** Damage to the aortic valve and sterile vegetation formation is accomplished by insertion of a polyethylene catheter through the carotid artery into the left ventricle; "the rat model of endocarditis is a well-established experimental protocol which closely approximates human native-valve endocarditis," and has been used to dissect specific virulence-factor contributions (e.g., the marginal role of von Willebrand factor-binding protein and coagulase in vegetation initiation, PMC7000203).
- **Mouse model:** A more recently developed induced *S. aureus* IE model exists, enabling use of the extensive mouse genetic/immunologic toolkit; MRI has been used to visualize *S. aureus*-induced vegetations non-invasively in mice (PMC4167704), and a dedicated induced-mouse-IE model paper describes its development and characterization (PMID referenced via ResearchGate summary of "Development of a mouse model of induced Staphylococcus aureus infective endocarditis").
- **In vitro/ex vivo systems:** Heterologous expression systems (e.g., *Lactococcus lactis* expressing individual staphylococcal MSCRAMMs such as ClfA or FnbA) are used to isolate the contribution of single adhesins to colonization/invasiveness without the confounding of the full *S. aureus* virulence repertoire — an important reductionist in vitro/cellular model complementing the whole-animal catheter models.

### Genetic Models
Because IE pathogenesis depends jointly on host vascular anatomy/hemodynamics and pathogen virulence factors, genetic manipulation is applied predominantly to the **pathogen** side (isogenic *S. aureus* mutants lacking specific MSCRAMMs — ClfA, FnBPA/B, sortase A — to test necessity/sufficiency for vegetation colonization) rather than to host germline engineering; host-side genetic models (e.g., TLR2-knockout mice) have been used in related cardiovascular-infection/sepsis contexts and are a logical extension for testing the innate-immune susceptibility genes identified in human association studies (§4), though a comprehensive host-genetic (knockout/transgenic) IE model survey was not surfaced in this search and represents a plausible research gap or an area needing more targeted follow-up querying of MGI/IMPC resources.

### Model Characteristics
- **Phenotype recapitulation:** Catheter-induced rabbit and rat models faithfully reproduce the two-step NBTE-then-bacterial-seeding pathogenesis, valve destruction, and (in some variants) systemic embolic phenomena seen in human disease, making them the field standard for testing novel antimicrobials, anti-adhesin therapeutics, and vaccine candidates.
- **Model limitations:** These models require mechanical/surgical induction of the initiating endothelial injury rather than arising from spontaneous structural valve disease (e.g., naturally aging bicuspid valve degeneration), so they may not fully capture the chronic, degenerative-valve-driven pathogenesis increasingly dominant in elderly human IE; they also typically model a single high-inoculum bacteremic challenge rather than the repeated, lower-grade bacteremic exposures (e.g., from dental brushing) thought to seed some human cases.

### Applications
These models are used to: (1) define the molecular determinants of bacterial adherence and vegetation colonization (MSCRAMM/sortase A studies); (2) evaluate novel and combination antimicrobial regimens for efficacy in sterilizing vegetations (a setting where poor antibiotic penetration into biofilm-protected vegetations is a central pharmacologic challenge); (3) test candidate anti-virulence or vaccine strategies; and (4) develop and validate non-invasive imaging approaches (e.g., MRI vegetation visualization) for translational diagnostic research.

### Resources
Model-organism databases relevant to follow-up investigation: MGI (Mouse Genome Informatics) for any TLR2/TLR5/IL6 knockout strains relevant to host-susceptibility follow-up studies; standard rabbit/rat experimental-endocarditis protocols are documented in specialized infectious-disease methods literature (e.g., the *Infection and Immunity*/*Antimicrobial Agents and Chemotherapy* experimental-endocarditis model literature) rather than a centralized model-organism repository, reflecting the surgically-induced (not strain-distributed) nature of these models.

---

## Summary of Suggested Ontology Term Bindings for Curation

| Category | Term |
|---|---|
| Disease | MONDO:0000565 (infective endocarditis) |
| Causal organism example | NCBITaxon:1280 (*Staphylococcus aureus*); NCBITaxon:1301 (*Streptococcus sanguinis*, representative viridans strep); NCBITaxon:1351 (*Enterococcus faecalis*); NCBITaxon:777 (*Coxiella burnetii*); NCBITaxon:773 (*Bartonella henselae*) |
| Gene (host susceptibility) | hgnc:11848 (TLR2); hgnc:11851 (TLR5); hgnc:6018 (IL6) |
| Gene (predisposing structural) | hgnc:3603 (FBN1) |
| Cell types | CL:0000233 (platelet); CL:0000115 (endothelial cell); CL:0000235 (macrophage); CL:0000775 (neutrophil) |
| Biological processes | GO:0007596 (blood coagulation); GO:0006954 (inflammatory response); GO:0002250 (adaptive immune response) |
| Anatomical sites | UBERON:0002332 (mitral valve); UBERON:0002137 (aortic valve); UBERON:0002094 (endocardium) |
| Key phenotypes | HP:0001945 (fever); HP:0031264 (cardiac murmur); HP:0025230 (Roth spot); HP:0001744 (splenomegaly); HP:0000099 (glomerulonephritis); HP:0001635 (congestive heart failure); HP:0001297 (stroke) |
| Treatment | NCIT:C15986 (Pharmacotherapy); NCIT:C15329 (Surgical Procedure) |

**Note on evidence gaps:** Genome-wide host-susceptibility data remain underpowered (largest reported GWAS: 67 cases/72 controls, no genome-wide-significant hits); IE-specific proteomic/metabolomic/lipidomic datasets and host-genetic (knockout) animal models were not identified in this search and should be treated as unconfirmed/absent rather than assumed present.

---

### Sources

- [Infective Endocarditis: Background, Pathophysiology, Etiology (Medscape)](https://emedicine.medscape.com/article/216650-overview)
- [Infective Endocarditis - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK557641/)
- [Infective endocarditis: A contemporary update - PMC (PMID:31941729)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6964163/)
- [Infective Endocarditis - GARD/NIH](https://rarediseases.info.nih.gov/diseases/6337/infective-endocarditis)
- [2023 Duke-ISCVID Criteria for Infective Endocarditis - PubMed (PMID:37138445)](https://pubmed.ncbi.nlm.nih.gov/37138445/)
- [Evaluation of the 2023 Duke-ISCVID Criteria - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11006096/)
- [Non-bacterial thrombotic endocarditis: a clinical and pathophysiological reappraisal - Eur Heart J](https://academic.oup.com/eurheartj/article/46/3/236/7905393)
- [Infective endocarditis complicated by embolic events: Pathogenesis and predictors - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7943911/)
- [Native valve, prosthetic valve, and cardiac device-related infective endocarditis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9574252/)
- [Infective Endocarditis in Special Populations - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12554326/)
- [Fibronectin-binding proteins A and B (FnBPA and FnBPB) of Staphylococcus aureus - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7480013/)
- [Polymorphisms in fibronectin binding protein A associated with cardiovascular device infection - PNAS](https://www.pnas.org/doi/10.1073/pnas.1109071108)
- [A rabbit model of right-sided Staphylococcus aureus endocarditis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3598207/)
- [MRI Visualization of Staphylococcus aureus-Induced Infective Endocarditis in Mice - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4167704/)
- [Marginal role of von Willebrand factor-binding protein and coagulase in rat catheter-induced endocarditis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7000203/)
- [What are the main predictors of in-hospital mortality in infective endocarditis - PubMed](https://pubmed.ncbi.nlm.nih.gov/29382232/)
- [A Nationwide Cohort Study of Mortality Risk and Long-Term Prognosis in IE in Sweden - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3704638/)
- [Current AATS guidelines on surgical treatment of infective endocarditis - PubMed (PMID:31832353)](https://pubmed.ncbi.nlm.nih.gov/31832353/)
- [Infective endocarditis due to Erysipelothrix rhusiopathiae in a dog - BMC Vet Res](https://link.springer.com/article/10.1186/s12917-020-02546-6)
- [Infective endocarditis in dogs in the UK: 77 cases (2009-2019) - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10099803/)
- [Genetic Variants in Genes of the Inflammatory Response in Association with Infective Endocarditis - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0110151)
- [Human Genetic Susceptibility to Native Valve S. aureus Endocarditis: GWAS - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5893849/)
- [Fungal Endocarditis: Pathophysiology, Epidemiology, Clinical Presentation, Diagnosis, and Management - Clin Microbiol Rev](https://journals.asm.org/doi/10.1128/cmr.00019-23)
- [Fungal Endocarditis - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK532987/)
- [Inflammatory parameters and prediction of prognosis in infective endocarditis - BMC Infect Dis](https://bmcinfectdis.biomedcentral.com/articles/10.1186/1471-2334-13-272)
- [Procalcitonin and C-reactive protein in infective endocarditis - PubMed (PMID:12714816)](https://www.ncbi.nlm.nih.gov/pubmed/12714816)
- [Dissecting the correlates of NT-proBNP in acute infective endocarditis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9705495/)
- [Prognostic value of pro-adrenomedullin and copeptin in acute infective endocarditis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7791699/)
- [The transcriptional programme of human heart valves reveals the natural history of infective endocarditis - PubMed (PMID:20126625)](https://pubmed.ncbi.nlm.nih.gov/20126625/)
- [Gender, Age, and Regional Disparities in the Incidence and Mortality Trends of IE in the US 1990-2019 - Am J Cardiol](https://www.ajconline.org/article/S0002-9149(23)00546-5/fulltext)
- [Impact of Sex and Age on Trends of Mortality From Infective Endocarditis in High-Income Countries - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12271061/)
- [Infective Endocarditis in Patients With Bicuspid Aortic Valve or Mitral Valve Prolapse - JACC](https://www.jacc.org/doi/10.1016/j.jacc.2018.03.534)
- [Pediatric Infective Endocarditis: A Literature Review - PubMed](https://pubmed.ncbi.nlm.nih.gov/35683606/)
- [2023 ESC Guidelines for Management of Endocarditis: Key Points - ACC](https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2023/08/29/20/49/2023-esc-guidelines-for-endocarditis-esc-2023)
- [Prevention of Infective Endocarditis - Circulation/AHA](https://www.ahajournals.org/doi/pdf/10.1161/circulationaha.106.183095)
- [P-931: Sex-Specific Trends in Opioid Use Disorder-Associated Infective Endocarditis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11778978/)