---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-20T14:01:16.919286'
end_time: '2026-07-20T14:05:20.575530'
duration_seconds: 243.66
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: RP2-Related Retinopathy
  mondo_id: MONDO:0100442
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: C:/Users/flaharty/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/bin/claude.exe
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    working_dir: C:/Users/flaharty/AppData/Local/Temp/claude/C--Users-flaharty-Desktop-VSCode/634cea2b-38e9-4ffb-8048-fd46243e54f3/scratchpad
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 24
  total_cost_usd: 1.1167171
  session_id: f624f3e6-57ff-4d58-9120-8897151ce543
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RP2-Related Retinopathy
- **MONDO ID:** MONDO:0100442 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RP2-Related Retinopathy** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I have gathered comprehensive data across all sections. Compiling the full research report now.

# RP2-Related Retinopathy: Comprehensive Disease Characteristics Report

---

## 1. Disease Information

**Overview:** RP2-related retinopathy (also termed RP2-associated X-linked retinitis pigmentosa) is a form of inherited retinal degeneration caused by hemizygous pathogenic variants in the *RP2* gene on the X chromosome. It presents in males as a severe, early-onset, rapidly progressive rod-cone dystrophy, and in female carriers as a highly variable phenotype ranging from asymptomatic to RP-level vision loss due to X-inactivation (Lyonization). RP2 was the second gene identified as a cause of X-linked retinitis pigmentosa (XLRP), historically accounting for roughly **10–20%** of XLRP cases (some sources cite up to 16–20%), with *RPGR* accounting for the majority (~60–75%) (PMC3124502, PMC5353642).

**Key identifiers:**
- **Gene/OMIM disease entry:** RP2, OMIM #312600 (Retinitis Pigmentosa 2); gene locus OMIM *300757 (RP2 Activator of ARL3 GTPase)
- **Related OMIM entries:** #268000 (Retinitis Pigmentosa, general); #300455 (X-linked RP and sinorespiratory infections ± deafness, RPSRDF — contiguous gene deletion syndrome involving RP2)
- **Gene location:** Xp11.3 (5 exons, ~1,050 bp coding sequence, 350 amino acid protein)
- **Orphanet:** ORPHA791 (Retinitis pigmentosa, umbrella term); a gene-specific Orphanet entry also exists for RP2-related XLRP
- **MONDO:** MONDO:0100442 (RP2-related retinopathy, per task); umbrella RP term MONDO:0019200
- **ICD-10:** H35.52 (pigmentary retinal dystrophy), broader H35.5
- **MeSH:** Retinitis Pigmentosa (D012174)
- **Disease Ontology:** DOID:10584

**Data source type:** This report synthesizes aggregated disease-level literature — natural history cohort studies, case series, functional/molecular studies, and model organism data — rather than individual EHR-derived data.

---

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic. Hemizygous (males) or heterozygous (females, with variable expressivity) loss-of-function or dysfunction-causing variants in *RP2* cause disease; no environmental or infectious cause is established.

**Genetic risk factors:**
- Causal variants in *RP2*: nonsense, frameshift, splice-site, and missense variants, plus whole-gene/partial-gene deletions (PMC10190057; PMC9738434 natural history study found 5 nonsense, 6 frameshift, 1 splice-site, 1 missense among 24 variants in one cohort).
- X-linked inheritance means male sex is itself a major risk determinant for full-penetrance disease.
- Family history of X-linked disease — but per PMC11139645 (female carrier study), *"family history of affected females with RP does not exclude X-linked disease,"* since carrier females can be symptomatic.

**Environmental/lifestyle risk factors:** None specifically established for RP2; as with RP broadly, no consistent environmental modifiers are documented in the reviewed literature.

**Protective factors:** No validated genetic or environmental protective factors specific to RP2 were identified in the literature searched. In female carriers, favorable (non-random) X-inactivation skewing toward the mutant allele functions as a protective factor at the individual level (PMC11139645): *"The disease spectrum is likely explained by Lyonization, whereby random X-chromosome inactivation during embryogenesis leads to variable expression of the wild-type phenotype."*

**Gene-environment interactions:** None specifically documented for RP2; vitamin A/E supplementation interactions are described for RP broadly (see Prevention/Treatment) but not RP2-specific.

**Modifier genes:** No validated modifier genes were reported; the natural history study (PMC9738434) explicitly found *"no evidence of genotype–phenotype correlation"* among variant types, and female carrier phenotype is modified primarily by X-inactivation pattern rather than a second gene.

---

## 3. Phenotypes

### Male (hemizygous) patients — from natural history study of 47 males/33 families (PMC9738434, *Ophthalmology* 2022/2023, PMC10567581):

| Phenotype | Frequency | HPO term (suggested) |
|---|---|---|
| Nyctalopia (night blindness) — first symptom | 69.6% | HP:0000662 |
| Reduced visual acuity as first symptom | 13.0% | HP:0000572 (Visual impairment) |
| Nyctalopia + reduced vision combined onset | 8.7% | — |
| Nystagmus | 4.4% | HP:0000639 |
| Asymptomatic at first exam | 4.4% | — |
| Intraretinal (bone-spicule) pigmentation | 89.2% | HP:0007737 |
| Attenuated retinal vessels | 94.6% | HP:0007843 |
| Macular changes | 58.5% | HP:0001103 (Atypical/macular abnormality) |
| Optic disc waxy pallor | 27.0% | HP:0000543 (Optic disc pallor) |
| Severe loss of fundus autofluorescence | 55.3% | — |
| Hyper-autofluorescent ring | 23.8% | — |

**Age of onset:** Median first symptoms at 7 years (IQR 2.25–12); median baseline exam age 20 years. Onset is **childhood**, distinctly earlier than typical autosomal RP.

**Severity/progression:** Rapid and progressive.
- BCVA: median 0.66 logMAR at baseline → 1.3 logMAR at last visit; progression rate of **46–49% acuity loss per decade**; legal blindness reached by a median age of **27 years**.
- Central retinal thickness declining 12.6–13.9% per decade; photoreceptor+RPE complex declining 27–33.9% per decade.
- Ellipsoid zone intact in only 34.3% at baseline (median age 14.5y) vs. severely disrupted/atrophic in 65.7% (median age 35y); EZ becomes "largely not measurable from 25 years of age."
- Overall course: *"rapid progression to outer retina atrophy and early macular involvement with substantial vision loss by age 30–40."*

**High myopia** is a recognized associated feature, and fundus appearance can mimic choroideremia (per PreventionGenetics/differential diagnosis literature) without choroideremia-gene involvement — an important diagnostic pitfall.

### Female carriers — from cohort of 27 carriers/21 pedigrees (PMC11139645, *AJO* 2023/2024):

- 85% asymptomatic with normal vision; 15% with RP-level complaints
- Fundus: normal (30%), tapetal-like reflex/TLR (37%), scattered peripheral pigment (19%), overt RP changes (15%)
- Visual acuity (WHO criteria): no/mild impairment 89%, moderate 3.7%, blind 7.4%
- Full-field ERG abnormal in 82% (9/11 tested), often asymmetric
- Radial fundus autofluorescence pattern in virtually all TLR carriers
- Slowly progressive atrophic changes documented over 6.7–11.4 years in symptomatic carriers

**Quality of life impact:** No RP2-specific QOL study was found, but the broader XLRP burden literature (EXPLORE XLRP-2 study, PMC11794432, *Eye* 2025) is informative: among 169 XLRP patients (RPGR-predominant cohort), anxiety was reported by 74.2% and depression by 15.8%; severe disease correlated with difficulties in low-luminance function, employment, and mobility; mean diagnostic delay from symptom onset to genetic diagnosis was **16.4 years**. These burden patterns are considered broadly applicable to RP2-XLRP given phenotypic overlap.

**Suggested HPO terms:** HP:0000546 (Retinal degeneration/atrophy), HP:0000662 (Nyctalopia), HP:0000639 (Nystagmus), HP:0007737 (Bone spicule pigmentation), HP:0007843 (Attenuation of retinal blood vessels), HP:0000543 (Optic disc pallor), HP:0000505 (Visual impairment), HP:0000545 (Myopia), HP:0000577 (Exotropia — if applicable), HP:0000512 (Abnormal electroretinogram).

---

## 4. Genetic/Molecular Information

**Causal gene:** *RP2* (HGNC:10295), OMIM *300757, chromosome Xp11.3, NCBI Gene ID 6102. Encodes a 350-amino-acid, ubiquitously plasma-membrane/ciliary-localized protein.

**Protein domain structure (UniProt O75695 / GeneCards):**
- **N-terminal domain**: homologous to tubulin-specific chaperone cofactor C (a β-helix domain involved in tubulin GTPase activation)
- **C-terminal domain**: homology to nucleoside diphosphate kinases (NDK); *"the physiological function of the NDK domain in RP2 remains to be determined"* though it has also been reported to have 3'→5' exonuclease activity and nuclear translocation after DNA damage (ScienceDirect, S001448270500621X)

**Variant classification/type (ClinVar, PMC9738434, PMC11139645):**
- Nonsense, frameshift, splice-site, missense, and whole/partial gene deletions
- In the 47-male natural history cohort: 24 total variants (13 novel) — 5 nonsense, 6 frameshift, 1 splice-site, 1 missense (proportions approximate; most common: c.352C>T p.(Arg118Cys) and c.358C>T p.(Arg120*))
- In the 21-pedigree carrier cohort: frameshift 28.6%, nonsense 28.6%, missense 23.8%, plus splice-site, whole-gene deletion, and smaller deletions
- ClinVar: "39 ClinVar submitters have submitted clinical-significance assessments... after 2014, and all submitters classified the variants as pathogenic or likely pathogenic" — reflecting high consensus once a variant is curated, per ACMG/AMP framework
- Up to **133 disease-associated variants** have been reported across the literature (PMC3124502)

**Functional consequences:** Frameshift/nonsense variants generally cause complete loss of function via truncation/nonsense-mediated decay; missense variants show **variable pathogenic potential** — some behave as near-null, others as partial hypomorphs (PMC3124502, *"Functional Analysis of RP2 Protein Reveals Variable Pathogenic Potential of Disease-Associated Missense Variants"*). Missense variants clustering in the ARL3-binding/N-terminal domain most consistently impair GAP activity; notably in the female carrier study, "no carriers with [ARL3-binding domain] variants were affected," while variants in the ferredoxin-like/β-helix domains were more often associated with an affected carrier phenotype — suggesting domain-specific severity even though no clear genotype-phenotype correlation was found in the male cohort.

**Protein function/mechanism:** RP2 acts as a **GTPase-activating protein (GAP) for ARL3** (ADP-ribosylation factor-like 3), a small ciliary GTPase (Reactome R-HSA-5638007). RP2 stimulates GTP hydrolysis on ARL3-GTP, triggering release of UNC119(B)-bound lipidated cargo (e.g., transducin, NPHP3) at the ciliary base/membrane — a key step in selective ciliary protein trafficking.

**Modifier genes:** None validated; X-inactivation pattern (not a second gene) is the principal modifier of female carrier phenotype.

**Epigenetic information:** X-chromosome inactivation (Lyonization) is the central "epigenetic" determinant of phenotype expression in female carriers — this is not a disease-specific epigenetic mechanism but the generic mechanism underlying all X-linked carrier variability.

**Chromosomal abnormalities:** Contiguous gene deletions spanning *RP2* and neighboring genes cause a distinct contiguous gene deletion syndrome, OMIM #300455 (X-linked RP with sinorespiratory infections ± deafness), illustrating that large deletions removing RP2 plus adjacent loci produce a syndromic phenotype beyond isolated retinopathy.

**Suggested ontology terms:** GO:0005096 (GTPase activator activity), GO:0060271 (cilium assembly), GO:0035861 (site of double-strand break — n/a), GO:0060170 (ciliary membrane), GO:0032391 (photoreceptor connecting cilium).

---

## 5. Environmental Information

No established environmental toxins, occupational exposures, or lifestyle factors are causally linked to RP2-related retinopathy — it is fully genetically determined. No infectious agents are implicated. (Not applicable beyond the general RP literature on vitamin A/E supplementation discussed under Treatment/Prevention.)

---

## 6. Mechanism / Pathophysiology

**Causal chain:** Pathogenic *RP2* variant → loss/reduction of RP2 GAP activity toward ARL3 → failure of ARL3-GTP hydrolysis → impaired release of UNC119-bound lipidated cargo (transducin, and related proteins) at the photoreceptor connecting cilium → **mistrafficking of phototransduction proteins into/through the outer segment** → progressive photoreceptor dysfunction and death.

**Molecular pathway specifics:**
- RP2-ARL3-UNC119 axis governs trafficking of lipidated proteins (e.g., farnesylated/prenylated cargo) across the connecting cilium (PMC5808637; Reactome R-HSA-5638007).
- RP2/ARL3 also regulate trafficking of the **ciliary tip kinesins KIF7 and KIF17**, needed for intraflagellar transport (IFT)-related delivery to the cilium tip.
- RP2 additionally supports **Golgi cohesion** and general vesicle trafficking/tubulin folding (via its cofactor-C-like domain), important for delivering opsins and other outer-segment cargo from the Golgi to the base of the connecting cilium.

**Cellular processes:** Impaired intracellular/intraciliary protein trafficking → progressive **rod and cone photoreceptor degeneration** via apoptosis; in RP2-knockout mouse and iPSC-organoid models, **cone opsin (M-opsin) and rhodopsin mistrafficking**, and diminished cone-specific GRK1 and PDE6 localization in outer segments, precede overt cell death.

**Protein dysfunction:** Predominantly **loss of function** (nonsense/frameshift/deletions) with some missense alleles causing partial or dominant-negative dysfunction of GAP activity (PMC3124502).

**Tissue damage mechanism:** Chronic photoreceptor-intrinsic ciliary trafficking failure leads to progressive apoptotic photoreceptor loss beginning with rods (nyctalopia) and extending to cones and RPE/outer retina (macular/central involvement), culminating in outer retinal atrophy.

**Molecular profiling (model systems):**
- iPSC-derived retinal organoid transcriptomic/histologic data (Stem Cell Reports 2020, PMC7363745): CRISPR RP2-knockout and R120X patient-derived organoids show peak rod photoreceptor cell death around **day 150** of culture and outer nuclear layer thinning by **day 180**; AAV-mediated RP2 gene augmentation rescued ONL thinning and restored rhodopsin expression.
- Mouse knockout models show early cone dysfunction (mistrafficking of cone opsin, GRK1, PDE6) preceding degeneration, described as *"early-onset cone dysfunction, followed by progressive cone degeneration, mimicking cone vision impairment in XLRP patients,"* though overall murine phenotype is milder than human disease.

**Suggested GO/CL terms:** GO:0007601 (visual perception), GO:0035845 (photoreceptor cell outer segment organization), GO:0006915 (apoptotic process), CL:0000210 (photoreceptor cell), CL:0000573 (retinal cone cell), CL:0000604 (retinal rod cell), CL:0000232 (retinal pigment epithelial cell — via GO:0032391 connecting cilium).

---

## 7. Anatomical Structures Affected

**Organ level:** Primary organ — the **eye/retina** (neurosensory retina, primarily photoreceptor layer; RPE secondarily). No consistent extra-ocular organ involvement in isolated RP2 disease, though contiguous-gene deletion cases (OMIM #300455) add sinorespiratory and hearing involvement (UBERON:0000949 endocrine — n/a; UBERON:0001004 respiratory system; UBERON:0001846 - middle ear structures for deafness).

**Tissue/cell level:** Rod photoreceptors (affected earliest — nyctalopia), cone photoreceptors (progressive involvement, central/macular vision loss), retinal pigment epithelium (atrophy with disease progression). Cell Ontology: CL:0000604 (rod), CL:0000573 (cone), CL:0002586 (retinal pigment epithelial cell).

**Subcellular level:** **Connecting cilium / ciliary transition zone** of photoreceptors (GO:0032391); Golgi apparatus (vesicle sorting, GO:0005794); outer segment membrane disc trafficking machinery.

**Localization:** Bilateral, generally symmetric in males; **asymmetric/unilateral presentations reported in female carriers** and rare male case reports (PMC10190057 — "asymmetric presentation with a novel RP2 gene mutation"). UBERON:0000966 (retina), UBERON:0001782 (macula lutea, for macular involvement).

---

## 8. Temporal Development

**Onset:** Pediatric/childhood — median age at first symptom 7 years in males; insidious onset of nyctalopia, sometimes with early nystagmus in infancy signaling more severe congenital-onset disease.

**Progression:** Rapid and relentlessly progressive (not episodic or relapsing-remitting).
- Early stage (childhood–adolescence): nyctalopia, peripheral field constriction, intact ellipsoid zone in a minority
- Intermediate stage (teens–20s): progressive EZ disruption, vessel attenuation, bone-spicule pigment
- Advanced stage (30s–40s): outer retinal atrophy, macular involvement, legal blindness by median age 27
- Disease course pattern: chronic, lifelong, progressive (not self-limited); "46–49% BCVA loss per decade" quantifies the rate.

**Patterns:** No spontaneous remission described. In female carriers, disease can remain **stable and mild for decades** if X-inactivation favors the wild-type allele, or progress "slowly" (documented over 6.7–11.4 year follow-up) if unfavorably skewed. No defined "critical window" for intervention is established in the human literature, though preclinical gene-therapy rescue data (mouse, organoid) suggest earlier intervention (before extensive photoreceptor loss) yields better structural/functional rescue.

---

## 9. Inheritance and Population

**Epidemiology:** RP overall affects ~1/3,000–5,000; XLRP accounts for **5–15%** of all RP and has a worldwide prevalence of roughly **1:30,000–1:40,000**. Within XLRP, *RPGR* accounts for ~60–75% of cases and **RP2 accounts for approximately 10–20%** (estimates range 5–20% depending on cohort; PMC3124502, PMC5353642). No RP2-specific population prevalence figure was identified in the literature searched.

**Inheritance pattern:** **X-linked** — historically described as X-linked recessive, though the existence of a substantial fraction of symptomatic female carriers (documented above) means the disease is now often characterized as showing **quasi-dominant or intermediate/semi-dominant inheritance** with sex-limited penetrance modulated by X-inactivation, rather than "true" recessive inheritance.

**Penetrance:** Complete in hemizygous males; **incomplete and variable in heterozygous females** (only 15% symptomatic in the reviewed cohort), governed by random X-inactivation skewing.

**Expressivity:** Highly variable, especially in females (ranging from normal fundus to full RP); in males, expressivity is more uniform/severe, though the natural history study found no genotype-phenotype correlation across variant types.

**Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically quantified in the reviewed literature for RP2, though it is a general consideration in X-linked disorder genetic counseling.

**Founder effects/geographic distribution:** No major founder mutations for RP2 were identified in the searched literature (contrast with RPGR ORF15 mutational hotspot, which accounts for ~2/3 of RPGR disease alleles). RP2 variants are described as diverse and largely private/family-specific across cohorts (Chinese, European/US cohorts referenced).

**Consanguinity role:** Not a significant factor given X-linked (not autosomal recessive) inheritance.

**Carrier frequency:** Not specifically reported; inferred to be very low given rarity of RP2 pathogenic alleles (private variants predominating over founder alleles).

**Sex ratio:** Disease manifests fully in males; females are carriers with variable, generally milder or absent phenotype — consistent with the essentially exclusive-male full phenotype pattern of X-linked RP.

**Age distribution:** Concentrated diagnosis in childhood-to-young-adult males (median baseline age in cohort 20 years); carrier females identified across a broad age range (16–76 years in the reviewed cohort) since many are ascertained through family cascade testing rather than symptoms.

---

## 10. Diagnostics

**Clinical tests:**
- **Fundus examination/fundus photography**: bone-spicule pigmentation, vessel attenuation, waxy disc pallor
- **Fundus autofluorescence (FAF)**: hyperautofluorescent ring (parafoveal), radial pattern in carriers, progressive loss of AF signal
- **Optical coherence tomography (OCT/SD-OCT)**: ellipsoid zone (EZ) width/loss, central retinal thickness, photoreceptor+RPE complex thickness — all quantified with defined decline rates in the natural history study
- **Full-field electroretinography (ff-ERG)**: rod-cone dysfunction pattern, often severely reduced/non-recordable in advanced male disease; abnormal in 82% of tested carriers
- **Pattern ERG (PERG)**: used to detect macular dysfunction in carriers
- **Visual field testing**: documents peripheral constriction
- **Visual acuity (BCVA, logMAR)**: primary functional endpoint tracked longitudinally

**Genetic testing:**
- **Single-gene *RP2* sequencing** or **targeted XLRP gene panels** (RP2 + RPGR ORF15 + OFD1, ± broader IRD panels) are the standard approach given clinical overlap
- **Whole exome/genome sequencing** used when panel testing is non-diagnostic or phenotype is atypical
- **Chromosomal microarray**: relevant when contiguous gene deletion (OMIM #300455) is suspected (e.g., syndromic features — deafness, recurrent sinorespiratory infection)
- Sanger confirmation and segregation analysis in relatives remains standard for variant classification
- No mitochondrial, repeat-expansion, or karyotype-specific testing is routinely indicated for isolated RP2 disease

**Clinical criteria/differential diagnosis:** Diagnosis relies on typical RP fundus/ERG findings plus X-linked pedigree pattern and confirmed hemizygous *RP2* variant. Key differentials: **RPGR-associated XLRP** (most common XLRP gene; ORF15 mutational hotspot), **choroideremia** (RP2 disease can closely mimic choroideremia fundus appearance without *CHM* involvement — an important diagnostic pitfall noted in PreventionGenetics literature), autosomal RP forms, and other syndromic ciliopathies given RP2's ciliary function.

**Screening:** No population newborn screening; family cascade genetic testing/counseling is the main "screening" modality for at-risk relatives (particularly potential female carriers, given the significant proportion who are symptomatic).

---

## 11. Outcome/Prognosis

**Visual prognosis (not life-threatening — an isolated ocular disease):**
- Legal blindness reached at a **median age of 27 years** in the male cohort
- BCVA loss of ~46–49% per decade; substantial vision loss by age 30–40
- Structural retinal decline (EZ, CRT, PR+RPE thickness) parallels functional loss, with EZ becoming unmeasurable from age 25 onward in many patients — indicating this as a useful structural endpoint for future trials
- Carrier females: prognosis is bimodal — majority retain good vision lifelong; a minority (~15% symptomatic, up to 7.4% legally blind in the reviewed cohort) progress to significant visual impairment

**Morbidity/QOL:** Drawing on the broader XLRP burden literature (EXPLORE XLRP-2), patients with severe disease show substantially higher rates of anxiety (74.2%), depression (15.8%), and impaired mobility/employment/daily functioning; **diagnostic delay averages 16.4 years** from symptom onset, a modifiable systemic factor affecting timely counseling and trial eligibility.

**Complications:** Cystoid macular edema and cataract can complicate advanced RP generally (not RP2-specific data identified); high myopia is a recognized associated ocular feature.

**Prognostic factors:** Earlier nystagmus at presentation may signal more severe/congenital-onset disease; no genotype-phenotype correlation has been established for variant type/location predicting severity in males. In females, X-inactivation skewing is the dominant prognostic determinant.

---

## 12. Treatment

**Pharmacotherapy:** No approved disease-modifying drug specific to RP2. General RP literature suggests **vitamin A palmitate** supplementation may modestly slow progression in some RP forms (evidence is weak/"insubstantial"), while **high-dose vitamin E should be avoided** (documented adverse effect on RP progression in the DHOM/Berson-type trials). No RP2-specific pharmacogenomic data exists.

**Gene therapy (most promising avenue, preclinical/early translational stage):**
- **AAV8/AAV9-mediated RP2 gene augmentation** (full-length human RP2 coding sequence) has shown efficacy in **RP2-knockout mouse models**, achieving *"long-term rescue of cone photoreceptor degeneration"* (PMC4626763) and in **iPSC-derived retinal organoids** (isogenic RP2-knockout and R120X patient-derived), where AAV-RP2 *"rescued the degeneration phenotype... preventing outer nuclear layer thinning and restoring rhodopsin expression"* (Stem Cell Reports 2020, PMC7363745).
- As of the literature reviewed, **no RP2-specific gene therapy has yet reached registered human clinical trials** (unlike RPGR, for which AGTC-501/laruparetigene zosaparvovec and 4D-125 are in Phase 1/2/3 trials, NCT04850118 and NCT04517149). RP2 vectors have been described as advancing toward clinical stage (NIH Tech Transfer listing) but a registered NCT trial specific to RP2 was not identified in this search.

**Surgical/interventional:** **Argus II retinal prosthesis** (FDA-approved for severe-to-profound RP of any genetic cause, age >25) is applicable to end-stage RP2 disease as a vision-restoration option, delivering electrical stimulation to surviving retinal cells via an epiretinal electrode array.

**Supportive/rehabilitative:** Low-vision aids, portable/adaptive lighting, orientation and mobility training, and genetic counseling are mainstays of current management.

**Experimental:** Retinal organoid and AAV vector platforms remain the primary experimental therapeutic pipeline; no RNA-based (ASO/siRNA) or small-molecule targeted therapy for RP2 was identified.

**Suggested MAXO terms:** MAXO term for "gene replacement therapy" (AAV-mediated gene augmentation), "retinal prosthesis implantation" (Argus II), "low vision rehabilitation," "genetic counseling," "dietary supplementation" (vitamin A).

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (monogenic disease); **genetic counseling and carrier testing** for at-risk female relatives is the principal preventive strategy, given that carrier detection informs reproductive decision-making.

**Secondary prevention/screening:** Cascade genetic testing in families with a known *RP2* variant; given that ~15% of female carriers are symptomatic, comprehensive ophthalmologic and genetic evaluation of at-risk females (not just male relatives) is recommended.

**Reproductive options:** Prenatal testing and preimplantation genetic diagnosis (PGD) are available options for known carrier families, following standard X-linked disorder genetic counseling frameworks (ACMG/NSGC), though no RP2-specific PGD outcome data was identified.

**Tertiary prevention:** Regular monitoring (OCT, FAF, ERG) to time low-vision intervention and clinical trial eligibility; avoidance of vitamin E supplementation; UV/blue-light protection is commonly recommended in general RP care (photoreceptor stress reduction), though direct RP2 evidence is lacking.

---

## 14. Other Species / Natural Disease

**Taxonomy:** *Mus musculus* (NCBI Taxon 10090) — Rp2-knockout mouse models exist; *Danio rerio* (NCBI Taxon 7955) — TALEN-generated rp2 knockout zebrafish. 

**Canine models — clarification:** Initial search results returned OMIA:001518-9615 ("X-linked progressive retinal atrophy, type 2," XLPRA2) which is actually caused by ***RPGR*** ORF15 mutations, not *RP2* — this is an important distinction to avoid conflating the two XLRP genes. No well-characterized naturally-occurring canine ortholog model specific to *RP2* was identified in this search; canine XLPRA1/XLPRA2 remain the standard dog models for XLRP generally (via RPGR) and are useful comparators given similarities in ciliary photoreceptor biology.

**Gene orthologs:** Mouse *Rp2* (MGI ortholog of human RP2), zebrafish *rp2*.

**Comparative biology:** Rp2-knockout mice show a **milder phenotype than human disease** — early cone-specific opsin/GRK1/PDE6 mistrafficking (as early as 2 months in one model, with ONL thinning by 5 months; another model showed abnormalities only by 14 months) followed by slow degeneration, useful for mechanistic study and therapy testing but not fully recapitulating the rapid, severe human course. Zebrafish rp2 knockouts show mild visual impairment (30% reduction in scotopic ERG b-wave) at 7 days post-fertilization. iPSC-derived retinal organoids (human, isogenic knockout and patient-derived) more directly recapitulate rod-predominant degeneration with defined kinetics (peak cell death ~day 150, ONL thinning by day 180) and have been used successfully for AAV rescue proof-of-concept.

**Transmission/zoonotic potential:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms Summary

| Model | Type | Key findings | Limitation |
|---|---|---|---|
| Rp2-knockout mouse | Genetic KO, mammalian | Early cone opsin/GRK1/PDE6 mistrafficking → progressive cone degeneration; used for successful AAV-RP2 gene therapy rescue (PMC4626763) | Milder/slower phenotype than human disease |
| rp2-knockout zebrafish (TALEN) | Genetic KO, non-mammalian | Mild visual impairment, ~30% reduced scotopic ERG b-wave at 7dpf | Limited characterization to date; less translatable to cone-rich human macula |
| Isogenic CRISPR RP2-KO and R120X patient iPSC-retinal organoids | In vitro, human cellular | Peak rod death ~day 150, ONL thinning by day 180; AAV-RP2 rescues ONL thinning and restores rhodopsin expression (PMC7363745) | 3D organoid model lacks vasculature/immune context, finite culture duration |

---

## Summary of Key Data Gaps
- No RP2-specific prevalence/incidence figures (only pooled XLRP figures) were located.
- No RP2-specific registered human gene therapy trial (NCT number) was found — this differentiates RP2 from RPGR, where multiple trials are active/completed.
- No validated modifier genes or founder variants specific to RP2 were identified.
- No RP2-specific naturally-occurring large-animal (canine) model was identified — existing canine XLPRA models are RPGR-linked, not RP2-linked.

---

### Sources
- [Functional Analysis of RP2 Protein Reveals Variable Pathogenic Potential of Disease-Associated Missense Variants (PMC3124502)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3124502/)
- [Asymmetric presentation with a novel RP2 gene mutation (PMC10190057)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10190057/)
- [A Natural History Study of RP2-Related Retinopathy (PMC9738434)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9738434/)
- [OMIM #268000 Retinitis Pigmentosa](https://omim.org/entry/268000)
- [Analysis of RP2 and RPGR Mutations in Five X-Linked Chinese Families (PMC5353642)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5353642/)
- [A Clinical Trial of Retinal Gene Therapy Using BIIB112 (NCT03116113 protocol)](https://cdn.clinicaltrials.gov/large-docs/13/NCT03116113/Prot_000.pdf)
- [OMIM #300455 RPSRDF](https://omim.org/entry/300455)
- [OMIM #312600 Retinitis Pigmentosa 2](https://www.omim.org/entry/312600)
- [MalaCards Retinitis Pigmentosa](https://www.malacards.org/card/retinitis_pigmentosa)
- [ICD-10 H35.52 Pigmentary retinal dystrophy](https://icdlist.com/icd-10/H35.52)
- [GeneCards RP2](https://www.genecards.org/card/RP2)
- [OMIM *300757 RP2 Activator of ARL3 GTPase](https://omim.org/entry/300757)
- [Arl3 and RP2 regulate trafficking of ciliary tip kinesins (PMC5808637)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5808637/)
- [Reactome: RP2 activates GTPase activity of ARL3](https://reactome.org/content/detail/R-HSA-5638007)
- [RP2-Associated X-linked Retinopathy: Natural History in Female Carriers (PMC11139645)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11139645/)
- [RP2 X-linked RP carrier state with vascular leakage (PMC10448798)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10448798/)
- [RP2-Associated X-linked Retinopathy (PMC10567581)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10567581/)
- [Moran CORE: RP2-Associated Retinitis Pigmentosa](https://morancore.utah.edu/section-12-retina-and-vitreous/rp2-associated-retinitis-pigmentosa/)
- [Long-term rescue of cone photoreceptor degeneration in RP2-KO mice (PMC4626763)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4626763/)
- [Modeling and Rescue of RP2 RP Using iPSC-Derived Retinal Organoids (PMC7363745)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7363745/)
- [RP2 Gene Analysis in X-Linked RP (GeneDx)](https://providers2.genedx.com/Resources/TIS-Files/TIS-TA72.pdf)
- [The burden of XLRP on patient experience (EXPLORE XLRP-2, PMC11794432)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11794432/)
- [OMIA:001518-9615 XLPRA2 (RPGR, not RP2 — noted correction)](https://omia.org/OMIA001518/9615/)
- [A putative silencer variant in a spontaneous canine model of RP (PLOS Genetics)](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1008659)
- [Solution Structure of N-Terminal Domain of Tubulin Binding Cofactor C (PMC3196536)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3196536/)
- [The RP2 protein exhibits exonuclease activity (ScienceDirect)](https://sciencedirect.com/science/article/abs/pii/S001448270500621X)
- [AGTC-501 HORIZON Phase 1/2 24-month results (AJO)](https://www.ajo.com/article/S0002-9394(24)00552-X/fulltext)
- [4D-125 in Patients With XLRP (NCT04517149)](https://clinicaltrials.gov/study/NCT04517149)