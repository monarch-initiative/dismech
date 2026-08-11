---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T23:45:34.643743'
end_time: '2026-07-31T23:50:18.089373'
duration_seconds: 283.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DPM2-congenital disorder of glycosylation
  mondo_id: ''
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 27
  total_cost_usd: 1.9969366000000002
  session_id: b08196c0-a1d7-5849-b9d8-b87c9c272757
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DPM2-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DPM2-congenital disorder of glycosylation** covering all of the
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

I have enough primary-source material now to compile the full report.

## Comprehensive Research Report: DPM2-Congenital Disorder of Glycosylation (DPM2-CDG)

---

### 1. Disease Information

**Overview.** DPM2-CDG (also designated CDG type Iu, CDG1U) is an autosomal recessive congenital disorder of glycosylation caused by biallelic pathogenic variants in *DPM2*, which encodes the regulatory subunit of the heterotrimeric dolichol-phosphate-mannose (Dol-P-Man/DPM) synthase complex. Because Dol-P-Man is the mannose donor for N-linked glycosylation, O-mannosylation of α-dystroglycan, protein C-mannosylation, and GPI-anchor biosynthesis, DPM2 deficiency produces a **combined glycosylation defect** that bridges the classic CDGs with the **secondary dystroglycanopathies** (congenital muscular dystrophies caused by hypoglycosylation of α-dystroglycan). It was the first disorder shown to link CDG-I biochemistry directly to a dystroglycanopathy phenotype, following earlier descriptions of DPM1-CDG and DPM3-CDG (Barone et al., *Ann Neurol* 2012, PMID:23109149).

**Key identifiers:**
- **OMIM (phenotype):** #615042 — Congenital Disorder of Glycosylation, Type Iu (CDG1U)
- **OMIM (gene):** *603564 — DOLICHYL-PHOSPHATE MANNOSYLTRANSFERASE 2, REGULATORY SUBUNIT; DPM2
- **Gene:** DPM2; **HGNC:** HGNC:3006; **Cytogenetic location:** 9q34.11
- **Orphanet:** ORPHA:329178 — "Congenital muscular dystrophy with intellectual disability and severe epilepsy" (the DPM2-CDG Orphanet entry)
- **Inheritance:** Autosomal recessive
- **Suggested MONDO term:** a DPM2-CDG-specific MONDO ID should be confirmed directly via the Monarch/MONDO API before curation (not independently verified in this research pass — flag for OAK lookup, e.g., `uv run runoak -i sqlite:obo:mondo search "DPM2-CDG"`).

**Synonyms/alternative names:** CDG1U; CDG-Iu; DPM2-CDG; Dolichyl-phosphate mannosyltransferase subunit 2 deficiency; Congenital disorder of glycosylation, type Iu; (historically grouped clinically with) muscular dystrophy-dystroglycanopathy.

**Evidence basis.** Essentially all available information derives from **individual published patient case reports/case series** (n≈6–8 patients worldwide across 4 publications spanning 2012–2023) rather than aggregated registries — this is one of the rarest known CDGs, so curation should rely on primary case reports rather than population-level resources.

---

### 2. Etiology

**Disease causal factor:** Biallelic (homozygous or compound heterozygous) loss-of-function/hypomorphic variants in *DPM2* (9q34.11), encoding the 84-amino-acid regulatory/stabilizing subunit of the ER-membrane-embedded DPM synthase complex. This is a purely monogenic, autosomal recessive Mendelian disease — no environmental or infectious causal factors are described.

**Genetic risk factors — reported pathogenic variants:**
| Variant(s) | Zygosity | Family/Patients | Reference |
|---|---|---|---|
| c.68A>G, p.Tyr23Cys (missense, TM domain 1) | Homozygous | 2 unrelated Italian patients (P4, P5) | Barone 2012, PMID:23109149 |
| c.68A>G (p.Tyr23Cys) + c.4-1G>C (splice) | Compound heterozygous | 1 Italian patient (P3) | Barone 2012, PMID:23109149 |
| c.139C>T, p.Arg47Ter (nonsense) + c.173G>A, p.Gly58Asp (missense) | Compound heterozygous | 1 Indian, 23-year-old male | Radenkovic et al. 2021, PMID:33129689 |
| c.197G>A, p.Gly66Glu (missense, TM domain 2) | Homozygous | 2 Chinese siblings | PMID:37152991 (PMC10154465) |

**Genotype–phenotype correlation:** Variants localizing to the **first transmembrane/domain region** (e.g., p.Tyr23Cys) associate with the **severe, early-lethal** phenotype; variants in the **second domain region** (p.Gly66Glu) or the Arg47Ter/Gly58Asp combination associate with a **milder, longer-surviving** phenotype — "patients with variants within the region encoding the first domain had more severe clinical symptoms than those with variants within the second domain" (PMC10154465).

**Population/allele-frequency risk factors:** No specific ClinVar/gnomAD population enrichment or founder-effect data were identified for DPM2 variants; the G66E and Y23C alleles are absent from gnomAD/1000 Genomes/ClinVar, consistent with extreme rarity rather than population-specific founder alleles. No consanguinity data beyond standard AR expectation were specifically reported in the search results retrieved.

**Protective factors:** None identified — no protective variant or environmental modifier literature exists for this ultra-rare monogenic disorder.

**Gene-environment interactions:** Not applicable/not reported; this is a fully genetically determined enzymatic deficiency with no known environmental modifiers.

---

### 3. Phenotypes

DPM2-CDG spans a **severe, early-lethal end** (Barone et al. 2012) and a **mild, long-survival end** (Radenkovic et al. 2021; the Chinese sibling report) — genuine phenotypic heterogeneity rather than a single stereotyped presentation.

**Severe end-of-spectrum (3 patients, 2 Italian families; onset at birth):**
- Profound/severe developmental delay, absent psychomotor development — HP:0012758 (Motor delay), HP:0001263 (Global developmental delay)
- Intractable/treatment-resistant epilepsy, described as "severe epilepsy" — HP:0001250 (Seizure), HP:0002373 (Febrile/other- consider HP:0011097 for epileptic spasms if applicable)
- Progressive microcephaly — HP:0000252
- Severe hypotonia — HP:0001252
- Elevated blood creatine kinase — HP:0003236 (Elevated CK)
- Mild cerebellar hypoplasia in one patient — HP:0007360
- Early fatal outcome: deaths at 3 years, 16 months, and 7 months of age
- Muscle biopsy: deficient O-mannosylation of α-dystroglycan on immunohistochemistry, consistent with dystroglycanopathy-type congenital muscular dystrophy — HP:0003198 (Myopathy), HP:0009046 (Diffusely decreased α-dystroglycan immunostaining, if precise term available)

**Mild end-of-spectrum (23-year-old Indian male, PMID:33129689):**
- Truncal hypotonia and hypertonicity (mixed tone abnormality) — HP:0001252 / HP:0001276
- Congenital heart defects — HP:0001627
- Intellectual disability (mild-moderate) — HP:0001249
- Generalized muscle wasting — HP:0003202
- Alive at 23 years — markedly better survival than the severe cohort

**Mild end-of-spectrum (2 Chinese sisters, PMID:37152991, ages 11 and 20 years):**
- Motor and language developmental delay (delayed head control to 4 months, walking at 3 years in one) — HP:0001270
- Mild intellectual disability — HP:0001256
- Hypotonia (elder sibling) / hypertonia (younger sibling) — mixed tone findings
- Strabismus — HP:0000486
- Recurrent infections in preschool years — HP:0002719
- Exercise intolerance — HP:0003546
- Markedly elevated CK (2097 and 2022 U/L; reference 20–250) and CK-MB elevation — HP:0003236
- Peripheral nerve involvement: slowed motor nerve conduction velocity, prolonged motor latency — HP:0003431
- Brain MRI: demyelinating lesions in bilateral parietal white matter — HP:0002500 (or HP:0032131)
- EEG: mildly slowed occipital background — HP:0011182
- Orthopedic sequela requiring Achilles tendon lengthening (contracture) — HP:0001371

**Severity/progression:** Bimodal — either a rapidly progressive, fatal infantile neuromuscular/epileptic encephalopathy, or a stable/slowly progressive congenital myopathy-intellectual disability phenotype persisting into adulthood. No formal QOL instrument (EQ-5D/SF-36) data were located for this disorder given its extreme rarity; QOL impact can be inferred as substantial in the severe form (early death, no psychomotor development) and moderate in the mild form (chronic disability, preserved survival to adulthood).

---

### 4. Genetic/Molecular Information

**Causal gene:** *DPM2* (HGNC:3006; OMIM *603564; chr9q34.11). Encodes an 84-amino-acid, two-transmembrane-domain ER integral membrane protein.

**Variant classes reported:** missense (p.Tyr23Cys, p.Gly58Asp, p.Gly66Glu), nonsense (p.Arg47Ter), and a canonical splice-acceptor variant (c.4-1G>C). All are **germline**, biallelic, loss-of-function or hypomorphic — no somatic DPM2 variants are described (not a cancer-associated gene in this context).

**Functional consequences:**
- Reduced DPM2 protein expression in patient fibroblasts (compound heterozygous R47X/G58D case), with secondary reduction of DPM1 protein — loss-of-function/destabilization of the complex.
- Conversely, the G66E variant, when overexpressed in HCT116 cells, showed **increased** DPM2 mRNA and protein but still produced a functional glycosylation defect (significant decrease in ICAM1, "a universal biomarker for hypoglycosylation in patients with CDG") — indicating the pathogenic mechanism is not simply reduced protein abundance but impaired function/regulatory activity, without altering ER subcellular localization.
- Net biochemical consequence in all cases: reduced Dol-P-Man synthesis → defective N-glycan precursor assembly (CDG type I biochemical pattern), deficient O-mannosylation of α-dystroglycan, and (mechanistically expected, per GPI-pathway biology) defective GPI-anchor mannosylation.

**Allele frequency:** All reported pathogenic DPM2 alleles are absent or near-absent from gnomAD/1000 Genomes/ClinVar population databases, consistent with an ultra-rare AR disease.

**Modifier genes:** None specifically documented; genotype-driven severity (TM domain 1 vs. domain 2 location) functions as the main documented "modifier" of phenotype, as above.

**Chromosomal abnormalities:** None reported; DPM2-CDG is due to sequence-level variants, not structural/copy-number changes.

**Epigenetic information:** No DPM2-CDG-specific methylation/histone data were identified.

**Suggested HGNC/ontology binding for curation:** `hgnc:3006` (lowercase per dismech convention), gene symbol DPM2.

---

### 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors are described for DPM2-CDG — it is a purely monogenic enzymatic-deficiency disorder. (Infections were reported as a *consequence* — "recurrent infections during preschool years" in one sibling case — rather than a cause, plausibly reflecting immune-glycoprotein hypoglycosylation, a recognized theme across CDGs broadly; see immunological-involvement-in-CDG literature, PMC7408855, for the general mechanism, though not DPM2-specific.)

---

### 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular lesion:** Biallelic *DPM2* variants (missense/nonsense/splice) → loss or dysfunction of the DPM2 regulatory subunit.
2. **Complex destabilization:** DPM synthase is a heterotrimer — DPM1 (catalytic, cytoplasmic-facing), DPM2 (ER membrane, stabilizes DPM1's correct ER localization and enhances dolichol-phosphate binding to DPM1), and DPM3 (tethers/stabilizes DPM1 at the ER membrane). Loss of DPM2 function destabilizes DPM1 localization/expression and impairs dolichol-phosphate binding.
3. **Enzymatic consequence:** Reduced synthesis of dolichol-phosphate-mannose (Dol-P-Man) from GDP-mannose + dolichol-phosphate in the ER membrane (GO:0004582, dolichyl-phosphate beta-D-mannosyltransferase activity; the complex itself localizes to GO:0005789, endoplasmic reticulum membrane).
4. **Multi-pathway mannose-donor deficiency** (Dol-P-Man is required by four distinct downstream pathways):
   - **N-linked glycosylation:** impaired mannosylation of the dolichol-linked oligosaccharide (LLO) precursor in the ER lumen → truncated/hypoglycosylated LLO → hypoglycosylated glycoproteins (CDG type I biochemical signature). Lipid-linked oligosaccharide analysis in patient fibroblasts showed accumulation of the truncated intermediate **Dol-PP-GlcNAc₂Man₅** (Barone et al. 2012), diagnostic of a defect at/after the Dol-P-Man-dependent mannosylation steps of LLO assembly.
   - **O-mannosylation of α-dystroglycan:** loss of Dol-P-Man-dependent O-mannosyl transfer onto α-dystroglycan (POMT1/POMT2-catalyzed step) → hypoglycosylated α-dystroglycan → loss of its laminin-binding function in the extracellular matrix → **secondary dystroglycanopathy** with muscular dystrophy features (confirmed by reduced α-dystroglycan immunostaining on muscle biopsy in the Barone cohort).
   - **Protein C-mannosylation** (e.g., of thrombospondin repeats) — also Dol-P-Man-dependent, mechanistically implicated though not specifically assayed in these patients.
   - **GPI-anchor biosynthesis:** Dol-P-Man is required for mannosylation steps of the GPI-anchor precursor in the ER; DPM2-deficient cells accumulate GPI intermediates lacking mannose, and GPI-anchored proteins such as alkaline phosphatase are degraded/mis-processed rather than properly surface-expressed — mechanistically linking DPM2-CDG to the broader **GPI-anchor-deficiency (CDG type II/IV)** disease class.
5. **Cellular/tissue consequence:** Combined N-glycan and O-mannosylation/GPI defects → skeletal muscle membrane fragility and impaired laminin-dystroglycan-ECM linkage (myopathy/elevated CK), CNS glycoprotein/glycolipid dysfunction (developmental delay, seizures, white-matter/demyelinating change, cerebellar hypoplasia), and generalized hypoglycosylation of serum glycoproteins (abnormal transferrin isoelectric focusing pattern, CDG type I).
6. **Downstream systemic consequence:** In the Radenkovic et al. (2021) glycomics/lipidomics study, secondary alterations in phospholipid and sphingolipid metabolism were identified, suggesting broader downstream metabolic perturbation beyond glycoprotein synthesis alone.

**Suggested ontology terms for pathophysiology nodes:**
- **GO (molecular function):** GO:0004582 (dolichyl-phosphate beta-D-mannosyltransferase activity)
- **GO (biological process):** GO:0006486 (protein glycosylation), GO:0035269 (protein O-linked mannosylation), GO:0006506 (GPI anchor biosynthetic process), GO:0009101 (glycoprotein biosynthetic process)
- **GO (cellular component):** GO:0005789 (endoplasmic reticulum membrane), GO:0033185 (dolichol-phosphate-mannose synthase complex, if present in current GO)
- **CL (cell types):** CL:0000188 (skeletal muscle cell/myocyte), CL:0000540 (neuron) — reflecting the two principal affected tissues
- **UBERON:** UBERON:0001134 (skeletal muscle tissue), UBERON:0000955 (brain)

**Molecular/omics profiling available:** Lipid-linked oligosaccharide (LLO) profiling (Barone 2012); glycomics + lipidomics (phospholipid/sphingolipid) profiling (Radenkovic 2021); targeted transcript/protein overexpression functional assay with ICAM1 as a glycosylation reporter (PMC10154465). No published single-cell, spatial transcriptomic, or CRISPR functional-genomics screen specific to DPM2-CDG was identified.

---

### 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skeletal muscle (dystroglycanopathy-type myopathy), central nervous system (developmental delay, epilepsy, structural brain abnormality)
- **Secondary/variable:** Cardiovascular system (congenital heart defects in the mild-phenotype adult patient), peripheral nervous system (demyelinating peripheral neuropathy in the Chinese sibling case), craniofacial (dysmorphic features, micrognathia, malocclusion in the severe Barone cohort), musculoskeletal (congenital joint contractures, scoliosis, strabismus/ocular findings)
- **Body systems involved:** musculoskeletal, nervous (central and peripheral), cardiovascular, ophthalmologic

**Tissue/cell level:**
- Skeletal myofibers (CL:0000188/CL:0000737) — dystrophic changes, hypoglycosylated α-dystroglycan on the sarcolemma
- Neurons and white-matter oligodendrocyte-myelin unit (demyelinating lesions reported) — CL:0000128 (oligodendrocyte)
- Cerebellar tissue (hypoplasia in one Italian patient)

**Subcellular level:**
- Endoplasmic reticulum (site of DPM synthase complex and Dol-P-Man synthesis) — GO:0005789
- ER lumen (site of LLO assembly and N-glycan precursor mannosylation)
- Plasma membrane (site of hypoglycosylated α-dystroglycan and deficient GPI-anchored protein display)

**Localization/laterality:** Bilateral/symmetric involvement is described (e.g., bilateral parietal white-matter demyelination); no lateralized/asymmetric pattern reported.

---

### 8. Temporal Development

**Onset:** Congenital in essentially all reported cases — severe cases present **at birth** (hypotonia, dysmorphism, joint contractures); milder cases present in **early childhood** with developmental/motor/language delay (walking delayed to 3 years in one sibling), later diagnosed retrospectively in adulthood.

**Onset pattern:** Insidious/chronic developmental presentation in the mild phenotype; acute/severe neonatal presentation with rapid multisystem involvement in the severe phenotype.

**Progression:**
- **Severe phenotype:** Rapidly progressive, fatal — deaths at 7 months, 16 months, and 3 years of age; intractable epilepsy and progressive microcephaly documented.
- **Mild phenotype:** Stable-to-slowly progressive chronic course; patients survive into the third decade of life (23-year-old male; 20-year-old sibling) with persistent but non-fatal disability (intellectual disability, myopathy, exercise intolerance).

**Disease duration:** Lifelong/chronic in survivors; the disease is not self-limited.

**Patterns:** No remission pattern is described (this is a structural enzymatic deficiency, not an episodic/relapsing-remitting disease). No specific "critical period" intervention window has been established given the absence of disease-modifying therapy.

---

### 9. Inheritance and Population

**Epidemiology:** DPM2-CDG is **ultra-rare** — only approximately **6–8 patients** have been reported in the peer-reviewed literature worldwide as of the most recent identified report (2023): 3 from 2 Italian families (Barone 2012), 1 Indian adult male (Radenkovic 2021), and 2 Chinese sisters (2023). No formal prevalence/incidence rate (cases per 100,000) has been established or published; combined N-linked CDG prevalence across ~27 disorders has been estimated around 1 in 22,000 in European populations, but DPM2-CDG specifically is far rarer than the more common subtypes (e.g., PMM2-CDG).

**Inheritance pattern:** Autosomal recessive (biallelic variants required in all reported cases — either homozygous or compound heterozygous).

**Penetrance:** Full penetrance is implied by all reported biallelic carriers being clinically affected (no unaffected biallelic carriers reported), though the sample size is too small for formal penetrance estimation.

**Expressivity:** Markedly **variable expressivity** — this is the disease's most notable population-genetics feature, spanning neonatal-lethal to adult-viable mild phenotypes, correlating with variant location (TM domain 1 vs domain 2/other).

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder).

**Founder effects/consanguinity:** Not explicitly documented in the retrieved literature; the 2 Italian families with the same p.Tyr23Cys variant (one homozygous in 2 patients) could suggest a possible regional founder allele, but this has not been formally established.

**Carrier frequency:** Not established; consistent with allele absence from gnomAD.

**Population demographics:** Cases reported from Italy, India, and China — no evidence of a specific ethnic/geographic predisposition; likely reflects ascertainment/publication bias rather than a true geographic pattern for an ultra-rare AR disease.

**Sex ratio:** Reported cases include both sexes — 2 males + 1 female of unspecified sex noted in the severe Italian cohort description ("affected boys" is mentioned for 2 of the 3 severe patients), 1 male (Indian adult), 2 females (Chinese siblings) — no clear sex bias is apparent, consistent with autosomal inheritance.

**Age distribution:** Bimodal — infantile deaths (7–36 months) in the severe subgroup vs. surviving pediatric/adult patients (11, 20, 23 years) in the mild subgroup.

---

### 10. Diagnostics

**Laboratory tests:**
- **Serum creatine kinase (CK):** Markedly elevated in all reported patients (up to ~2000 U/L; reference range 20–250 U/L) — reflects the myopathic/dystroglycanopathy component.
- **Transferrin isoelectric focusing (IEF):** Shows a **CDG type I pattern** (cathodic shift due to under-sialylated, hypoglycosylated N-glycans from incomplete LLO assembly) — the classic first-line CDG screening test (gold standard per general CDG diagnostic literature).
- **Lipid-linked oligosaccharide (LLO) analysis in cultured fibroblasts:** Diagnostic biochemical signature — accumulation of the truncated intermediate Dol-PP-GlcNAc₂Man₅, localizing the biosynthetic block to the Dol-P-Man-dependent mannosylation steps.
- **ICAM1 expression assay:** Used as a functional glycosylation biomarker in one functional-variant study (decreased with pathogenic DPM2 variant expression).

**Biomarkers:** Elevated CK (muscle-specific); abnormal transferrin glycoform pattern (glycosylation-specific); reduced ICAM1 as an experimental hypoglycosylation reporter.

**Imaging:** Brain MRI — cerebellar hypoplasia (severe cases); demyelinating white-matter lesions, bilateral parietal distribution (mild case).

**Electrophysiology:** EEG — epileptiform/slowed background activity; nerve conduction studies — slowed motor conduction velocity and prolonged motor latency (peripheral neuropathy component in at least one mild-phenotype patient).

**Biopsy/histopathology findings:** Skeletal muscle biopsy immunohistochemistry demonstrating **deficient O-mannosylation of α-dystroglycan** — the confirmatory tissue-level test linking the biochemical CDG-I finding to the dystroglycanopathy phenotype.

**Genetic testing:** Confirmatory diagnosis requires *DPM2* sequencing (single-gene test, CDG gene panel, or exome/genome sequencing given the extreme rarity and phenotypic overlap with other CDG-I subtypes and dystroglycanopathies). Given the phenotypic and biochemical overlap with DPM1-CDG and DPM3-CDG, a **CDG/dystroglycanopathy gene panel** approach (covering *DPM1*, *DPM2*, *DPM3*, *POMT1/2*, *POMGNT1/2*, *FKTN*, *FKRP*, *LARGE1*, *B3GALNT2*, etc.) is the pragmatic first-tier test; single-gene *DPM2* testing is appropriate when biochemical/biopsy findings (combined CDG-I pattern + dystroglycan hypoglycosylation) point specifically to the DPM synthase complex.

**Differential diagnosis:** Other DPM-synthase-complex CDGs (DPM1-CDG, DPM3-CDG — allelic-complex disorders with overlapping combined CDG-I/dystroglycanopathy biochemistry); other secondary dystroglycanopathies (POMT1/2-, POMGNT1/2-, FKTN-, FKRP-, LARGE1-, B3GALNT2-related congenital muscular dystrophies, e.g., Walker-Warburg syndrome/muscle-eye-brain disease spectrum); other CDG type I disorders (PMM2-CDG, ALG-family CDGs) presenting with elevated CK and developmental delay; GPI-anchor-deficiency disorders (PIGA, PIGV, PIGO, etc.) given the shared GPI-mannosylation defect.

**Screening:** No population/newborn screening program exists for this ultra-rare disorder; diagnosis is case-by-case, typically prompted by a combination of unexplained developmental delay/epilepsy/hypotonia with elevated CK, triggering CDG biochemical screening (transferrin IEF) followed by molecular confirmation.

---

### 11. Outcome/Prognosis

**Survival/mortality:** Bimodal, variant-dependent:
- **Severe phenotype (TM-domain-1 variants, e.g., p.Tyr23Cys):** Uniformly fatal in infancy/early childhood — reported deaths at 7 months, 16 months, and 3 years.
- **Mild phenotype (other variants):** Survival into adulthood documented (23-year-old male alive at report; siblings aged 11 and 20 alive at report) — no mortality reported in this subgroup.

No formal actuarial life-expectancy or population-level mortality-rate data exist given the rarity of the disease.

**Morbidity/function:** In survivors — chronic intellectual disability (mild-moderate), myopathy/generalized muscle wasting, exercise intolerance, orthopedic complications (contractures requiring surgical correction), and in one case peripheral neuropathy. No standardized QOL instrument data identified.

**Complications:** Intractable epilepsy (severe form); congenital heart defects (mild-form adult patient); recurrent infections (childhood, mild-form siblings) — plausibly reflecting broader hypoglycosylation of immune glycoproteins, consistent with general CDG immunological literature, though not specifically studied in DPM2-CDG.

**Prognostic factors:** The single most important documented prognostic factor is **variant location within the DPM2 protein** — first transmembrane-domain variants (p.Tyr23Cys) predict a severe/lethal course, while variants outside this region (p.Gly66Glu; p.Arg47Ter/p.Gly58Asp) predict a milder, longer-surviving course. No molecular biomarker (beyond genotype) has been validated as prognostic.

**Recovery potential:** None — this is a fixed enzymatic/structural deficiency with a progressive-to-stable neuromuscular course; there is no disease-modifying treatment altering the underlying trajectory.

---

### 12. Treatment

**Pharmacotherapy:** No DPM2-CDG-specific or DPM-synthase-complex-targeted pharmacological therapy exists. Unlike **PMM2-CDG** (where oral D-mannose and D-galactose supplementation have shown biochemical/clinical benefit in some patients — Ligezka et al., PMC8359111; PMC7510076) or **MPI-CDG** (mannose-responsive) and **SLC35C1-CDG/PIGM-CDG/PGM1-CDG** (which have specific targeted therapies per the general CDG treatment literature), **DPM2-CDG has no established substrate-supplementation or targeted therapy** — the defect is upstream at the level of Dol-P-Man *synthesis* itself (regulatory subunit dysfunction), not substrate availability, so simple mannose supplementation would not be expected to bypass the enzymatic block. This is an important curation distinction from PMM2-CDG.
- **NCIT suggestion for generic management:** NCIT:C15747 (Supportive Care)

**Symptomatic/supportive management (documented in case reports):**
- Anti-seizure medication for intractable epilepsy in the severe phenotype (specific agents not detailed in retrieved abstracts) — NCIT:C15986 (Pharmacotherapy)
- Orthopedic surgical correction — Achilles tendon lengthening for contracture in one sibling — NCIT:C15329 (Surgical Procedure) / NCIT:C16186 (Orthopedic Surgical Procedure)
- Physical therapy / rehabilitative management for hypotonia/motor delay — NCIT:C15302 (Physical Therapy)
- Nutritional/growth support (implied for failure to thrive in severe neonatal presentations) — NCIT:C15447 (Dietary Intervention)
- Cardiac management for congenital heart defects in the mild adult phenotype — cardiology follow-up/surgical repair as indicated

**Advanced/experimental therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or clinical trial specific to DPM2-CDG was identified (no ClinicalTrials.gov entries located in this search). Given the extreme rarity (<10 published patients), a dedicated interventional trial is unlikely to exist.

**Genetic counseling:** Recommended given autosomal recessive inheritance and 25% recurrence risk per pregnancy for carrier parents — NCIT:C15240 (Genetic Counseling).

**Treatment strategy:** Management is multidisciplinary and purely supportive/symptom-directed (neurology for seizures, orthopedics for contractures/scoliosis, cardiology as needed, physical/occupational therapy, nutritional support) — no disease-modifying or curative approach currently exists.

---

### 13. Prevention

**Primary prevention:** None available (no environmental risk factor to modify; a purely genetic AR disease).

**Secondary prevention/screening:** No population or newborn screening program exists. In families with a known proband, **carrier testing and prenatal/preimplantation genetic diagnosis** are the applicable prevention strategies once the familial *DPM2* variants are identified — standard for any AR Mendelian disorder with 25% recurrence risk.

**Genetic counseling:** Central preventive/family-planning tool — informing carrier parents of recurrence risk and reproductive options (prenatal diagnosis, PGD/IVF) — NCIT:C15240.

**Tertiary prevention:** Anticipatory multidisciplinary surveillance (seizure monitoring/management, orthopedic monitoring for contractures/scoliosis, cardiac surveillance, developmental/rehabilitative support) to reduce complications in affected individuals, particularly in the milder, longer-surviving phenotype.

**Immunization/public health/prophylaxis:** No disease-specific vaccination, public-health, or prophylactic-medication strategy is described.

---

### 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring DPM2-deficient disease has been reported in non-human species (companion animals, wildlife) — this appears to be a human-only reported clinical entity; no OMIA (Online Mendelian Inheritance in Animals) entry was identified in this search.

**Orthologous gene:** Mouse *Dpm2* (MGI:1330238) is the confirmed ortholog; used exclusively for laboratory knockout modeling (see Model Organisms below), not for natural/spontaneous veterinary disease.

**Comparative biology:** The DPM synthase complex (DPM1/DPM2/DPM3) is evolutionarily conserved from yeast to humans — a functional DPM2 homolog exists in *Saccharomyces cerevisiae* (Yil102c-A, PMC7728079), underscoring deep conservation of Dol-P-Man biosynthesis machinery across eukaryotes and validating yeast as a tool for functional variant characterization (as used for the related PMM2-CDG disorder, though not yet specifically published for DPM2 variants in the retrieved literature).

**Zoonotic potential/transmission:** Not applicable — this is a non-infectious, purely genetic disorder.

---

### 15. Model Organisms

**Mouse:**
- Constitutive *Dpm2* knockout is **homozygous embryonic/perinatal lethal** — "Knockout of the mouse homolog of human DPM2 is homozygous-lethal (defined as absence of homozygous mice after screening of at least 28 pups before weaning)" (per IMPC/MGI data referenced in search results, MGI:1330238). This parallels the embryonic lethality seen in other dystroglycanopathy-pathway mouse knockouts (e.g., *Pomt1*, due to the essential placental role of dystroglycan in rodents), and implies that **conditional/tissue-specific knockout strategies** would be required to model postnatal DPM2-CDG phenotypes in mice — no such conditional model was identified in the retrieved literature specifically for *Dpm2*.

**Zebrafish:**
- No DPM2-specific zebrafish model was identified in this search. However, zebrafish are an actively used and validated platform for the broader dystroglycanopathy gene class (e.g., *pomt1* loss-of-function zebrafish recapitulate α-dystroglycan hypoglycosylation and dystroglycanopathy phenotypes, PMID:38272461/PMC11000664; *fkrp*-deficient zebrafish, PMID:18477595) — representing a **model-system gap** worth flagging for a `HUMAN_MODEL_MISMATCH`-type discussion if curated in dismech, since DPM2 itself lacks a published zebrafish disease model despite the pathway being well-modeled in zebrafish for sibling genes.

**Yeast:**
- *Saccharomyces cerevisiae* Yil102c-A functions as a DPM2 homolog and has been used to functionally characterize the yeast DPM synthase regulatory subunit (PMC7728079) — a potential future functional-variant-testing platform analogous to the yeast complementation assays already published for PMM2-CDG variant classification (bioRxiv 414862).

**Cell-based/in vitro models:**
- **Patient-derived dermal fibroblasts** — used for LLO profiling (Barone 2012) and glycomics/lipidomics (Radenkovic 2021); these directly recapitulate the biochemical CDG-I defect and reduced DPM1/DPM2 protein expression.
- **HCT116 cell line transfection/overexpression assays** — used to functionally characterize the p.Gly66Glu variant's effect on DPM2 mRNA/protein expression and on the ICAM1 hypoglycosylation reporter (PMC10154465) — this is the most direct functional-genomics tool currently published for DPM2 variant interpretation.

**Model limitations:** No model currently recapitulates the full clinical spectrum (severe neonatal-lethal epileptic-myopathic phenotype vs. mild adult-viable phenotype) in vivo; the mouse constitutive-knockout lethality precludes whole-animal phenotypic study without a conditional allele, and no such conditional/hypomorphic mouse model was identified in this search.

---

## Summary for Knowledge-Base Curation

DPM2-CDG is an ultra-rare (≤10 published patients), autosomal recessive, allelic-series disorder (alongside DPM1-CDG and DPM3-CDG) of the dolichol-phosphate-mannose synthase complex, causally unifying **CDG type I** (N-glycosylation/LLO defect) and **secondary dystroglycanopathy** (α-dystroglycan O-mannosylation defect) mechanisms with a probable but unconfirmed **GPI-anchor biosynthesis** contribution. The clearest curatable causal chain is: *DPM2* biallelic variant → DPM synthase complex destabilization → Dol-P-Man deficiency → parallel failure of (a) N-glycan LLO assembly, (b) α-dystroglycan O-mannosylation, and (c) GPI-anchor mannosylation → combined CDG-I biochemistry + dystroglycanopathy-type myopathy + neurodevelopmental phenotype, with **variant location within DPM2 (TM domain 1 vs. domain 2)** as the key documented genotype-severity modifier distinguishing the fatal-infantile from mild-adult-viable ends of the phenotypic spectrum. Treatment is entirely supportive; no targeted or disease-modifying therapy (including simple mannose supplementation, unlike PMM2-CDG) has been established. This entry is a strong candidate for `conforms_to` linkage to the `lysosomal_substrate_accumulation`-adjacent glycosylation-defect pattern conceptually, and more directly overlaps mechanistically with any future dismech module capturing the shared DPM1/DPM2/DPM3 "dolichol-phosphate-mannose synthesis disorder" pattern (cf. PMID:30931530, "Toward understanding tissue-specific symptoms in dolichol-phosphate-mannose synthesis disorders; insight from DPM3-CDG") — worth checking whether such a module already exists or should be proposed given the shared trigger→consequence chain across all three DPM subunit deficiencies.

**Primary literature cited (PMIDs):** 23109149 (Barone et al. 2012, *Ann Neurol* — first DPM2-CDG description, 3 patients); 33129689 (Radenkovic et al. 2021, *Mol Genet Metab* — 23-year-old mild phenotype, glycomics/lipidomics); 37152991 (2023 — Chinese siblings, novel p.Gly66Glu variant, ICAM1 functional assay); 16280320 and related DPM1/DPM3 stabilization mechanism papers; 30931530 (DPM3-CDG tissue-specificity review, mechanistically relevant); 38272461/PMID for zebrafish *pomt1* dystroglycanopathy model (pathway-analogous, not DPM2-specific).

**Notable evidence gaps requiring `KNOWLEDGE_GAP`/`HUMAN_MODEL_MISMATCH` flags if curated:** (1) no confirmed MONDO ID verified in this pass — requires OAK lookup before entry creation; (2) no DPM2-specific animal model recapitulating the human phenotype exists (mouse knockout is embryonic lethal; no zebrafish model published), a clear `HUMAN_MODEL_MISMATCH` candidate; (3) GPI-anchor pathway involvement is mechanistically inferred from DPM-synthase biochemistry but not directly demonstrated with patient GPI-anchored-protein/ALP data in the DPM2-CDG case reports themselves (unlike PMM2-CDG, where this has been directly studied per PMC4016514) — treat as an extrapolated/inferred edge rather than direct human evidence.