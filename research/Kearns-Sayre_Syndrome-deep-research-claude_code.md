---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T01:30:13.036611'
end_time: '2026-07-31T01:35:31.039607'
duration_seconds: 318.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kearns-Sayre syndrome
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
  web_search_requests: 15
  num_turns: 25
  total_cost_usd: 1.8735335000000006
  session_id: 88238ee2-0063-556d-b082-f501096afca2
  stop_reason: end_turn
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kearns-Sayre syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kearns-Sayre syndrome** covering all of the
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

# Kearns-Sayre Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview:** Kearns-Sayre syndrome (KSS) is a rare, sporadic, progressive multisystem mitochondrial disease caused by large-scale single deletions (or duplications) of mitochondrial DNA (mtDNA). It is the most severe end of the phenotypic spectrum of the "Single Large-Scale Mitochondrial DNA Deletion Syndromes" (SLSMDS), which also includes isolated chronic progressive external ophthalmoplegia (CPEO) and Pearson marrow-pancreas syndrome (PS) — three clinically distinct but molecularly related and sometimes interconverting presentations of the same underlying mtDNA lesion ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

The disorder was first described in 1958: Kearns TP, Sayre GP. "Retinitis pigmentosa, external ophthalmoplegia, and complete heart block: unusual syndrome with histologic study in one of two cases." *Arch Ophthalmol (Chicago)* 1958;60:280-289 — the original clinical description of the triad that now bears their names ([EyeWiki](https://eyewiki.org/Kearns-Sayre_Ptosis); [Wiley Acta Ophthalmologica commentary](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1755-3768.1975.tb01779.x)).

**Key Identifiers:**
- **OMIM:** #530000 ([omim.org/entry/530000](https://omim.org/entry/530000))
- **Orphanet:** ORPHA:480 ([orpha.net](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=480))
- **ICD-10-CM:** H49.81 (Kearns-Sayre syndrome) ([icd10data.com](https://www.icd10data.com/ICD10CM/Codes/H00-H59/H49-H52/H49-/H49.81))
- **MONDO:** MONDO:0010787
- **Disease Ontology:** DOID:12934
- **MeSH:** Kearns-Sayre Syndrome (D016218, typically indexed under "Ophthalmoplegia, Progressive External")

**Synonyms:** Kearns-Sayre mitochondrial cytopathy; KSS; oculocraniosomatic syndrome; ophthalmoplegia-plus syndrome; chronic progressive external ophthalmoplegia with ragged red fibers (in some older nosologies, though CPEO alone is now distinguished from full KSS) ([MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/kearns-sayre-syndrome/)).

**Data source type:** The evidence base is drawn overwhelmingly from **aggregated disease-level resources** — case reports/series, multi-institutional retrospective cohorts, and the pooled clinical/molecular database underlying GeneReviews and Orphanet — rather than from a single large prospective EHR cohort, reflecting the rarity of the condition. A newer prospective effort is the **Global Registry and Natural History Study for Mitochondrial Disorders (NCT05554835)**, which includes KSS patients ([ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05554835)).

---

## 2. Etiology

**Disease Causal Factors:** KSS is caused by a **single large-scale deletion (or, less commonly, duplication) of mitochondrial DNA**, ranging in size from **1.1 to 10 kb**, occurring as a **de novo somatic/germline mutational event** — not by inheritance of a nuclear gene mutation in the vast majority of cases. Approximately 90% of cases are sporadic ([StatPearls NBK482341](https://www.ncbi.nlm.nih.gov/books/NBK482341/)). The most common single deletion is the "**common deletion**," m.8470_13446del4977 (a 4,977-bp deletion), found in roughly one-third of SLSMDS/KSS patients ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

**Genetic Risk Factors:**
- The deletion itself is the causal genetic lesion — there is no separate "susceptibility locus" model; KSS is essentially monogenic at the mtDNA level, but polygenic/heteroplasmic in effect (variable deletion size, location, and load determine phenotype).
- **Rare nuclear-gene-driven secondary forms** exist: mutations in nuclear genes governing mtDNA replication/maintenance can produce multiple mtDNA deletions or an autosomal-recessive KSS-like phenotype:
  - **RRM2B** (ribonucleotide reductase small subunit 2-like) — the first reported case of autosomal recessive KSS was linked to compound heterozygous RRM2B mutations causing altered mtDNA transcription ([ScienceDirect abstract, G.P.188](https://www.sciencedirect.com/science/article/abs/pii/S0960896614003952); [Thieme abstract](https://www.thieme-connect.com/products/ejournals/abstract/10.1055/s-0033-1337752)).
  - **SSBP1** (mitochondrial single-stranded DNA-binding protein) — a de novo SSBP1 variant has been reported in a child with a single large-scale mtDNA deletion manifesting sequentially as Pearson, Kearns-Sayre, and Leigh syndromes ([PMC6719858](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6719858/)).
  - Other mtDNA-maintenance genes implicated in the broader multi-deletion disease class include **POLG, POLG2, TWNK (Twinkle), RNASEH1, DNA2,** and **MGME1** ([search synthesis](https://www.thieme-connect.com/products/ejournals/abstract/10.1055/s-0033-1337752)).
- **Age/maternal factors**: because the deletion typically arises during oogenesis or very early embryogenesis, maternal germline mosaicism is the presumed origin in the rare familial cases.

**Environmental Risk Factors:** None established. No toxin, infection, or lifestyle exposure has been convincingly linked to sporadic mtDNA deletion formation in KSS; the deletion is considered a stochastic replication/repair error.

**Protective Factors:** No genetic or environmental protective factor has been identified. Lower heteroplasmy load and smaller/less complex-gene-disrupting deletions are associated with milder phenotype (see Genetics section) but are not "protective factors" in the traditional sense — they represent points along a severity continuum rather than modifiable protection.

**Gene-Environment Interactions:** Not applicable in the classical sense; the principal "interaction" is genotype (deletion size/location) × tissue bioenergetic demand × mitotic/segregation dynamics (see Mechanism section), not an environmental exposure interacting with genotype.

---

## 3. Phenotypes

**Diagnostic (obligate) triad** — onset before age 20 years, **progressive external ophthalmoplegia (PEO)**, and **pigmentary retinopathy**, **plus at least one** of: cardiac conduction block, CSF protein >100 mg/dL, or cerebellar ataxia ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/); [PMC9056216](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9056216/)).

| Phenotype | Type | Onset/Course | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Progressive external ophthalmoplegia / ptosis (often asymmetric) | Clinical sign | Childhood–adolescent onset (<20y), progressive | Core/obligate feature | HP:0000602 (Ophthalmoplegia), HP:0000508 (Ptosis) |
| Pigmentary retinopathy ("salt-and-pepper" fundus) | Clinical sign, imaging | Progressive, impairs night vision first | Core/obligate feature | HP:0000580 (Pigmentary retinopathy) |
| Cardiac conduction block (bundle branch block → complete heart block) | Clinical sign | Progressive; complete heart block reported ages 5–13y | Major criterion; heart block causes death in ~20% | HP:0011675 (Arrhythmia), HP:0001677 (Atrioventricular block) |
| Elevated CSF protein (>100 mg/dL) | Laboratory abnormality | Present at diagnosis in many cases | Major criterion | HP:0002922 (Increased CSF protein) |
| Cerebellar ataxia | Clinical sign | Progressive | Major criterion; correlates with hearing loss, retinopathy, poor growth | HP:0001251 (Ataxia) |
| Sensorineural hearing loss | Clinical sign | Progressive | 18–67% across cohorts | HP:0000407 |
| Cognitive decline/dementia/intellectual disability | Behavioral/clinical sign | Progressive | Variable | HP:0002376 (Developmental regression), HP:0001249 |
| Renal tubular/glomerular dysfunction (renal tubular acidosis) | Laboratory/clinical | May be presenting feature | Most frequently affected organ over disease course — **85%** in documented cohorts | HP:0001919 (Renal tubular acidosis) |
| Endocrinopathies (diabetes mellitus, hypoparathyroidism, GH deficiency, adrenal insufficiency, hypogonadism) | Clinical/lab | Variable onset, progressive | 35–67% | HP:0000819 (Diabetes mellitus), HP:0000829 (Hypoparathyroidism), HP:0000824 (Growth hormone deficiency) |
| Cardiomyopathy | Clinical sign | Later feature | ~10% | HP:0001638 |
| Proximal myopathy / exercise intolerance | Clinical sign | Progressive | Common | HP:0003701 (Proximal muscle weakness), HP:0003546 (Exercise intolerance) |
| Oropharyngeal/esophageal dysfunction, cricopharyngeal achalasia, dysphagia | Clinical sign | Progressive | Common | HP:0002015 (Dysphagia) |
| Short stature / poor growth | Physical | Chronic | Common | HP:0004322 |
| Seizures | Clinical sign | Episodic | 6–9% | HP:0001250 |
| White matter abnormalities / basal ganglia (globus pallidus) lesions on MRI | Imaging | Progressive | Common | HP:0002500 (Leukoencephalopathy) |

Age of onset, severity, and progression rate are **directly correlated with deletion size, deletion location (whether MT-CYB and MT-COX genes are included), and heteroplasmy level** — higher heteroplasmy load correlates with earlier onset and greater severity ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)). Prognostic clustering: "those with retinopathy had statistically significant increased incidence of hearing loss, ataxia, and poor growth. Those with ataxia had statistically significant increased incidence of hearing loss, retinopathy, poor growth, cognitive involvement, and tremor" ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

**Quality of life impact:** Chronic progressive multisystem disease produces cumulative disability (vision loss, hearing loss, mobility impairment, cardiac risk). Psychiatric morbidity is common in mitochondrial disease broadly ("70% of mitochondrial disorder patients will have evidence of mental illness at some point in their lives") ([search synthesis](https://www.ovid.com/jnls/neur/fulltext/10.4103/0028-3886.325321~psychiatric-morbidities-in-kearns-sayre-syndrome); [UMDF KSS page](https://umdf.org/kss/)). No KSS-specific validated EQ-5D/SF-36 dataset was identified in this search; QoL literature is largely case-based rather than instrument-validated.

---

## 4. Genetic/Molecular Information

**Causal lesion:** A **single large-scale mtDNA deletion**, 1.1–10 kb, with **more than 150 distinct deletions reported** in KSS/SLSMDS. The most common is **m.8470_13446del4977** ("common deletion," ~4,977 bp), present in roughly one-third of patients ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

**Genes typically removed by the deletion** (varies by breakpoints, but the common deletion spans):
- Complex I subunits: **MT-ND3, MT-ND4, MT-ND4L, MT-ND5**
- Complex IV subunits: **MT-CO1, MT-CO2, MT-CO3** (frequently only partially — the common 4977-bp deletion actually spans MT-ATP8 through MT-ND5, encompassing COX III, ATP6/8, ND3, ND4L, ND4, and several tRNAs)
- Complex V subunits: **MT-ATP6, MT-ATP8**
- Multiple mt-tRNA genes: **tRNA-Gly, tRNA-Arg, tRNA-His, tRNA-Ser, tRNA-Leu**, among others

"Deletions disrupt multiple essential mitochondrial genes involved in oxidative phosphorylation, including several subunits of respiratory chain complexes (e.g., ATP6, COXIII, ND3, ND4L, ND4, and ND5) as well as tRNA genes... thereby impairing mitochondrial protein synthesis and electron transport chain function" ([search synthesis of PMC12169696 and related](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12169696/)). Larger deletions removing more tRNA and structural genes correlate with the more severe KSS phenotype versus isolated CPEO: "Longer deletions and higher number of deleted genes encoding respiratory chain complex subunits and tRNA genes were observed in the Kearns-Sayre syndrome group."

**Variant classification/type:** Structural variant — large genomic deletion (not point mutation). Deletion mechanism classes per GeneReviews:
- **Class I:** flanked by perfect direct repeats, likely arising via homologous recombination or replication slippage ("slipped mispairing").
- **Class II:** not flanked by homologous sequence; mechanism unknown.

**Heteroplasmy and allele "frequency":** KSS deletions are always **heteroplasmic** (coexisting with wild-type mtDNA) — homoplasmic large deletions are not compatible with life. "The size of the mtDNA deletion is uniform in an affected individual," implying clonal expansion from a single mutational event early in oogenesis/embryogenesis ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)). Because these are somatic/de novo events, they are essentially **absent from population databases** like gnomAD (which catalogs germline nuclear variants) — mtDNA deletion burden is not represented there.

**Somatic vs. germline origin:** Predominantly somatic/early-embryonic de novo events. Rare maternal germline transmission occurs (see Inheritance, section 9).

**Functional consequences:** Loss-of-function at the level of mitochondrial protein synthesis and OXPHOS — the deletion removes tRNA genes required for mitochondrial translation and/or structural OXPHOS subunit genes, producing a **combined translational and complex-specific biochemical defect** rather than a single-protein loss/gain-of-function in the classical Mendelian sense.

**Modifier genes:** No consistently validated modifier genes beyond the mtDNA deletion characteristics themselves (size, location, heteroplasmy) and — in rare autosomal recessive KSS-like cases — primary nuclear mtDNA-maintenance genes (RRM2B, SSBP1) acting as the primary rather than modifying cause.

**Epigenetic information:** Not a major axis of KSS pathogenesis in the literature surveyed; disease mechanism is structural/bioenergetic rather than epigenetic-regulatory. No dedicated ENCODE/Roadmap Epigenomics KSS dataset was identified.

**Chromosomal abnormalities:** Not applicable — the causal lesion is confined to the mitochondrial genome, not nuclear chromosomes.

---

## 5. Environmental Information

- **Environmental/toxic factors:** None established as causal. No CTD/TOXNET association was identified linking specific toxins to sporadic mtDNA deletion formation.
- **Lifestyle factors:** Not causal, though disease management includes **avoidance of volatile anesthetics and prolonged propofol infusion (>30–60 minutes)** due to "volatile anesthetic hypersensitivity" in mitochondrial disease patients ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/); [orphananesthesia.eu guideline](https://www.orphananesthesia.eu/rare-diseases/published-guidelines/kearns-sayre-syndrome/281-kearns-sayre-syndrome/file.html)) — this is a management consideration rather than an etiological environmental factor.
- **Infectious agents:** None implicated in KSS causation. (Fatal pneumonia has been reported as a *complication* in advanced KSS, not a cause — [PMC12350349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12350349/).)

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Initial trigger — de novo mtDNA deletion formation:** During mtDNA replication/repair, a large segment (1.1–10 kb) is lost. Class I deletions arise at flanking direct repeats via replication slippage or homologous recombination; Class II deletions have no clear repeat-mediated mechanism ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).
2. **Clonal expansion and heteroplasmy establishment:** The deleted molecule is thought to gain a **replicative advantage** in certain conditions (a shorter genome may replicate faster), leading to clonal expansion during oogenesis/embryogenesis and subsequent mosaic distribution across tissues ([PMC5893934](https://pmc.ncbi.nlm.nih.gov/articles/PMC5893934/)).
3. **Threshold effect:** Biochemical/respiratory-chain deficiency manifests only once the deleted-to-wild-type mtDNA ratio exceeds a tissue- and complex-specific threshold — reported in postmitotic tissue (skeletal muscle) as roughly **50–90%**, with complex-specific nuance: "thresholds for complex I and complex IV deficiency are modulated by the deletion of complex-specific protein-encoding genes" (e.g., ~71–75% for Class I deletions; Complex I ~65% vs. Complex IV ~91% for Class II deletions) ([PMC5893934](https://pmc.ncbi.nlm.nih.gov/articles/PMC5893934/)). Mouse (mito-mice∆) modeling corroborates this: "Kearns-Sayre syndrome-like phenotypes were expressed when the proportion of ∆mtDNA in various tissues reached >70–80%" ([PMC3755915](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755915/)).
4. **Molecular pathway disruption:** Loss of mt-tRNA genes impairs **mitochondrial protein translation broadly**; loss of structural OXPHOS genes (ND3/ND4/ND4L/ND5 for Complex I; COI/COII/COIII for Complex IV; ATP6/ATP8 for Complex V) directly removes subunits of the electron transport chain and ATP synthase. "Transcription and translation of deleted mitochondrial genomes" studies show the deleted genome is transcribed but its translation products are compromised ([PMC1683616](https://ncbi.nlm.nih.gov/pmc/articles/PMC1683616)).
5. **Cellular consequences:** Impaired oxidative phosphorylation → reduced ATP synthesis → energy deficit in high-energy-demand tissues (extraocular muscle, retina, cardiac conduction system, cerebellar/cortical neurons, renal tubular epithelium, skeletal muscle). Secondary cellular stress responses documented include **reactive oxygen species (ROS) overproduction, mitochondrial protein synthesis inhibition, myelin vacuolation/demyelination, dysregulated autophagy, apoptosis, and lipid-raft/oligodendrocyte involvement** in CNS white matter pathology ([Molecular Neurobiology 2024, PMID: 38224444](https://pubmed.ncbi.nlm.nih.gov/38224444/)). Muscle biopsy shows **ragged red fibers** (subsarcolemmal mitochondrial proliferation, seen on modified Gomori trichrome stain) with abnormal succinate dehydrogenase (SDH) staining — a hallmark of compensatory mitochondrial biogenesis in respiratory-deficient fibers, and "respiratory-deficient fibers show increased total mtDNA copy number but decreased wild-type mtDNA," consistent with subunit haploinsufficiency driving the biochemical defect ([PMC5893934](https://pmc.ncbi.nlm.nih.gov/articles/PMC5893934/)).
6. **Tissue-specific clinical manifestation:** Retinal pigment epithelium atrophy with aberrant pigment migration into sensory retina (pigmentary retinopathy); cardiac conducting-system fibrosis/dysfunction (progressive bundle branch block → complete heart block); cerebellar Purkinje/neuronal energy failure (ataxia); basal ganglia (globus pallidus) and white-matter injury (leukoencephalopathy, sometimes linked to **secondary cerebral folate deficiency** responsive to folinic acid); renal proximal tubular dysfunction (Fanconi-like renal tubular acidosis, 85% of documented cases); endocrine gland dysfunction (parathyroid, pancreatic islet, pituitary/GH axis, adrenal, gonadal).

**Protein dysfunction:** Loss-of-function at multiple mtDNA-encoded OXPHOS subunits simultaneously (not a single misfolded protein) plus global impairment of mitochondrial translation from tRNA gene loss — a compound respiratory-chain assembly/function defect.

**Metabolic changes:** Impaired oxidative ATP generation shifts cellular energy metabolism toward compensatory glycolysis where possible; lactic acidosis can occur, though it is a less uniform biochemical marker in KSS than in some other mitochondrial syndromes (e.g., MELAS).

**Immune system involvement:** Not a primary autoimmune/immunodeficiency mechanism; inflammation is a secondary consequence of tissue injury (e.g., in CNS demyelination) rather than a driving immune-mediated process.

**Suggested GO terms:** GO:0006120 (mitochondrial electron transport, NADH to ubiquinone), GO:0006123 (mitochondrial electron transport, cytochrome c to oxygen), GO:0042775 (mitochondrial ATP synthesis coupled electron transport), GO:0032543 (mitochondrial translation), GO:0006119 (oxidative phosphorylation), GO:0006915 (apoptotic process), GO:0006914 (autophagy).

**Suggested CL terms:** CL:0000187 (muscle cell)/skeletal myocyte, CL:0000210 (photoreceptor cell) / retinal pigment epithelial cell, CL:0000097 (cardiac conduction system cell) / Purkinje fiber cell, CL:0000121 (cerebellar Purkinje cell), CL:1001111 (kidney proximal convoluted tubule epithelial cell), CL:0000165 (neuroendocrine cell) for affected endocrine glands.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** eyes (extraocular muscles, retina), heart (conduction system), skeletal muscle, cerebellum/CNS white matter and basal ganglia.
- **Secondary:** kidney (renal tubular acidosis — most frequently affected organ over disease course, 85%), endocrine glands (parathyroid, pancreas, pituitary, adrenal, gonads), inner ear (cochlea), gastrointestinal tract (pharynx/esophagus — cricopharyngeal achalasia).
- **Body systems:** ophthalmologic, cardiovascular, neurologic, endocrine, renal, musculoskeletal, gastrointestinal, auditory.

**Tissue/cell level:**
- Extraocular muscle fibers and levator palpebrae superioris (ptosis, ophthalmoplegia).
- Retinal pigment epithelium and photoreceptor layer (salt-and-pepper retinopathy — postmortem shows RPE atrophy with aberrant pigment migration into sensory retina).
- Cardiac conduction system (SA/AV node, bundle branches).
- Skeletal muscle fibers (ragged red fibers, SDH-abnormal fibers).
- Cerebellar Purkinje cells and cerebral white matter oligodendrocytes/myelin.
- Renal proximal tubular epithelial cells.
- Parathyroid chief cells, pancreatic islet beta cells, pituitary somatotrophs, adrenal cortex, gonadal tissue.

**Subcellular level:** Mitochondria (inner membrane electron transport chain complexes I, III, IV, V; mitochondrial matrix/nucleoid where mtDNA replicates). GO Cellular Component: GO:0005739 (mitochondrion), GO:0005743 (mitochondrial inner membrane), GO:0005759 (mitochondrial matrix), GO:0042645 (mitochondrial nucleoid).

**Localization (UBERON):** UBERON:0000970 (eye) / UBERON:0001782 (extraocular muscle), UBERON:0000966 (retina), UBERON:0000948 (heart) / UBERON:0002348 (cardiac conduction system), UBERON:0001134 (skeletal muscle tissue), UBERON:0002037 (cerebellum), UBERON:0002435 (globus pallidus), UBERON:0002113 (kidney), UBERON:0001132 (parathyroid gland), UBERON:0001264 (pancreas).

**Lateralization:** Ophthalmoplegia and ptosis are typically **bilateral but often asymmetric** in onset — a distinguishing clinical clue versus other CPEO causes, which tend to be more symmetric ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

---

## 8. Temporal Development

- **Onset:** By definition before age 20 years; typically childhood to adolescence. Onset pattern is **insidious and progressive** rather than acute.
- **Progression:** Chronic, relentlessly progressive multisystem decline — new organ involvement accrues over years (e.g., ophthalmoplegia/retinopathy in childhood, cardiac conduction disease emerging in the 5–13 year age range, endocrinopathies and renal/CNS involvement appearing over subsequent years). "May progress to death by young adulthood," though "some patients achieve normal lifespans with appropriate management" (pacemaker placement being the single most life-saving intervention) ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).
- **Disease course pattern:** Progressive and generally non-relapsing/non-remitting, in contrast to some other mitochondrial encephalomyopathies with stroke-like episodic features (e.g., MELAS).
- **Critical transition — Pearson to KSS:** A striking natural-history phenomenon is that infants with **Pearson (marrow-pancreas) syndrome** — bone marrow failure/sideroblastic anemia and exocrine pancreatic insufficiency from the *same* mtDNA deletion — who survive infancy may go on to develop the neurologic/ophthalmologic/cardiac KSS phenotype later in childhood, "due to the gradual decrease in SLSMDs in rapidly dividing blood cells and the gradual increase in SLSMDs in postmitotic tissues." In one Italian cohort, **64% of Pearson syndrome survivors** developed neurologic symptoms and clinical KSS ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)). Mouse modeling reproduces this same tissue-specific heteroplasmy shift over time ([PMC3755915](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755915/)).
- **Remission patterns:** None reported; no spontaneous remission described. Some symptomatic improvement (e.g., transient benefit from CoQ10, or reversal of white-matter abnormalities with folinic acid in cerebral folate deficiency) has been reported but is not disease remission.
- **Critical periods:** Early identification of cardiac conduction disease is the key intervention window — prophylactic pacemaker placement before complete heart block develops is considered life-saving, since heart block causes death in ~20% of untreated patients.

---

## 9. Inheritance and Population

**Epidemiology:**
- Estimated prevalence: **1–3 per 100,000** ([MedlinePlus](https://medlineplus.gov/genetics/condition/kearns-sayre-syndrome/); [StatPearls NBK482341](https://www.ncbi.nlm.nih.gov/books/NBK482341/)).
- Orphanet estimate: ~**1/125,000** ([Orphanet search synthesis](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=480)).
- A Finnish adult-population epidemiological study estimated prevalence of large-scale mtDNA deletions (the class of disorders causing KSS) at **1.6/100,000**.
- Affects males and females in roughly equal numbers.

**Inheritance pattern:** Predominantly **de novo / sporadic**, arising in the maternal germline (oocyte) or very early embryogenesis — not classically "maternally inherited" in the transmission sense since the deletion is not present in the mother's own tissues in most cases. "SLSMDSs are almost never inherited." True **maternal transmission**, when it occurs, follows mitochondrial (cytoplasmic) inheritance rules but is rare: "maternal transmission to more than one child has not been reported to date" ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)). Rare autosomal recessive forms exist via nuclear genes (RRM2B, SSBP1) that secondarily cause mtDNA instability/multiple deletions.

**Penetrance/Expressivity:** Because clinical severity depends continuously on heteroplasmy level, deletion size, and tissue distribution, KSS shows **highly variable expressivity** rather than simple penetrance — this is a hallmark of heteroplasmic mitochondrial disease.

**Genetic anticipation:** Not a feature of KSS (this is a nucleotide-repeat-expansion phenomenon; KSS is a single deletion event, not applicable).

**Germline mosaicism:** Central to disease origin — the deletion is believed to arise in oogenesis or early embryogenesis, producing germline/somatic mosaicism that determines the tissue distribution of mutant mtDNA in the offspring.

**Founder effects:** No population-specific founder mtDNA deletion has been established for KSS (unlike some point-mutation mitochondrial diseases); the common 4977-bp deletion recurs across populations due to a shared local secondary-structure/repeat-mediated deletion "hotspot" rather than a founder haplotype.

**Consanguinity role:** Relevant only to the rare autosomal recessive (RRM2B/SSBP1-driven) secondary forms, not to the typical sporadic mtDNA-deletion KSS.

**Carrier frequency:** Not meaningfully defined for a de novo somatic/germline structural mtDNA event (as opposed to a heritable point mutation with population carrier frequency).

**Recurrence risk (genetic counseling):**
- If the proband is a "simplex case" and the mother is clinically and molecularly unaffected: sibling recurrence risk is **≤1%** (empiric, very low).
- If the mother is affected/carries the deletion: recurrence risk to future offspring is estimated at **~4% (1 in 24 births)** ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

**Population demographics:** No strong ethnic or geographic clustering has been established; case reports span diverse populations (e.g., Colombia, Thailand, Lithuania, Finland) with population-specific deletion variants reported (e.g., a unique 3.5-kb deletion in Thai patients — [PMID 10480366](https://pubmed.ncbi.nlm.nih.gov/10480366/)), consistent with a stochastic mutational mechanism rather than a founder-driven or geographically endemic disease.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Lumbar puncture / CSF protein** (>100 mg/dL is a major diagnostic criterion).
- **CSF 5-methyltetrahydrofolate** — low levels identify secondary cerebral folate deficiency, guiding folinic acid therapy.
- **Serum lactate/pyruvate** (variably elevated; not a defining criterion).
- **Electrolytes** — hypokalemia, hypophosphatemia, hypomagnesemia from renal tubular acidosis.
- **Endocrine panel** — glucose/HbA1c, PTH/calcium, GH axis, cortisol, gonadotropins.

**Biomarkers:** No single validated circulating biomarker exists; heteroplasmy load itself (measured molecularly) functions as the closest quantitative biomarker of severity.

**Imaging:**
- **Brain MRI**: bilateral globus pallidus lesions, white matter abnormalities/leukoencephalopathy.
- **Cardiovascular MRI**: assessment for cardiomyopathy.
- **Echocardiography**: structural/functional cardiac assessment.

**Functional/electrophysiologic tests:**
- **ECG and 24-hour Holter monitoring**: essential for detecting progressive conduction block.
- **Audiometry**: for sensorineural hearing loss.
- **EMG/nerve conduction** as needed to exclude neuromuscular junction or peripheral nerve mimics.

**Biopsy/histopathology:**
- **Skeletal muscle biopsy**: ragged red fibers (modified Gomori trichrome), abnormal succinate dehydrogenase (SDH) staining, cytochrome c oxidase (COX)-deficient fibers.
- **Retinal histopathology** (postmortem): RPE atrophy and outer retinal atrophy with aberrant pigment migration.

**Genetic testing (the definitive diagnostic modality):**
- **Detection rate: 100%** of clinically diagnosed KSS patients demonstrate an identifiable single large-scale mtDNA deletion by appropriate deletion/duplication analysis ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).
- **First-line/gold standard**: Next-generation sequencing (NGS) of the mitochondrial genome from **peripheral blood leukocytes** — SLSMDs are detectable in blood, buccal cells, and urine sediment "in all reported affected children," though in **adults** the deletion may be diluted out of blood over time (mitotic segregation favoring wild-type mtDNA in blood), requiring **skeletal muscle biopsy** for mtDNA analysis ([StatPearls NBK482341](https://www.ncbi.nlm.nih.gov/books/NBK482341/); [GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).
- **Long-range PCR / quantitative PCR**: identifies deletions and maps breakpoints.
- **Droplet digital PCR**: quantifies heteroplasmy load, though it "cannot reliably detect less than 10% heteroplasmy levels."
- **Whole mtDNA sequencing** is generally more informative than targeted single-gene testing, since KSS is a structural (deletion) rather than point-mutation disorder; **whole exome/genome sequencing** is more relevant to excluding the rare nuclear-gene (RRM2B/SSBP1/POLG/TWNK) secondary forms.
- **Chromosomal microarray/karyotype/FISH**: not relevant (nuclear chromosomes are normal in typical KSS).
- **Repeat expansion testing**: not applicable.

**Clinical diagnostic criteria:** The obligate triad (onset <20y + PEO + pigmentary retinopathy) plus ≥1 of (cardiac conduction block, CSF protein >100 mg/dL, cerebellar ataxia), as above.

**Differential diagnosis:**
- Isolated CPEO (no retinopathy/cardiac/CSF findings; often more symmetric ptosis).
- Oculopharyngeal muscular dystrophy.
- Myotonic dystrophy type 1 (myotonia distinguishes it).
- POLG-related PEO (often adult-onset, with mtDNA depletion rather than deletion).
- Myasthenia gravis and congenital myasthenic syndromes (fluctuating weakness, abnormal repetitive nerve stimulation/EMG, antibody-positive in acquired MG).
- Other mitochondrial encephalomyopathies with overlapping features (MELAS, MERRF) — distinguished by point mutations rather than large deletions, and by distinct clinical hallmarks (stroke-like episodes for MELAS, myoclonic epilepsy for MERRF).

**Screening:** No population-based newborn screening exists for KSS (it is a de novo, non-Mendelian somatic event, unsuited to standard carrier/newborn screening paradigms). Prenatal/preimplantation genetic testing is "scientifically possible but technically prohibitive" because current sequencing methods cannot reliably quantify heteroplasmy at the single-cell/embryo level ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

---

## 11. Outcome/Prognosis

- **Mortality/survival**: KSS "may progress to death by young adulthood" in more severe cases; however, "some patients achieve normal lifespans with appropriate management," particularly with proactive cardiac surveillance and pacemaker placement. **Complete heart block causes death in approximately 20% of patients** if unrecognized/untreated ([search synthesis, GeneReviews-derived](https://emedicine.medscape.com/article/950897-overview)).
- **Disease-specific mortality driver**: Sudden cardiac death from complete heart block is the single most important preventable cause of death — this is why KSS is considered an indication for **prophylactic pacemaker implantation** even before symptomatic bradyarrhythmia manifests.
- **Morbidity/functional outcomes**: Progressive visual loss (night blindness progressing toward broader visual field loss), progressive hearing loss, ataxia/gait disturbance, cognitive decline, short stature, and endocrine dysfunction (diabetes, hypoparathyroidism, hypogonadism) accumulate over the disease course, producing cumulative multi-domain disability.
- **Complications**: Aspiration pneumonia (from oropharyngeal/esophageal dysfunction — a reported fatal complication, [PMC12350349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12350349/)), malnutrition/failure to thrive, cardiac arrhythmia/heart failure, seizures, adrenal crisis (from adrenal insufficiency), electrolyte derangement from renal tubular dysfunction.
- **Prognostic factor clustering** (from GeneReviews-cited cohort analysis): presence of retinopathy correlates with higher incidence of hearing loss, ataxia, and poor growth; presence of ataxia correlates with hearing loss, retinopathy, poor growth, cognitive involvement, and tremor — supporting a model where greater overall mtDNA deletion burden/heteroplasmy manifests as clustered multi-organ severity rather than isolated single-organ disease.
- **Prognostic biomarkers**: heteroplasmy level and deletion size/location are the best available quantitative prognostic correlates, though genotype-phenotype correlation "remains controversial, with some cohorts reporting correlations and others finding none" ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)).

---

## 12. Treatment

**No disease-modifying/curative therapy exists.** Management is supportive, multidisciplinary, and surveillance-driven ([GeneReviews NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/); [StatPearls NBK482341](https://www.ncbi.nlm.nih.gov/books/NBK482341/)).

**Pharmacotherapy:**
- **Coenzyme Q10 (ubiquinone)** — mitochondrial cofactor supplementation; "beneficial in individual cases... although effects are transient," and benefit is generally considered "of unproven benefit" at a rigorous evidence level despite widespread use ([PMID 3941783 — original CoQ10 treatment report](https://pubmed.ncbi.nlm.nih.gov/3941783/); MAXO term: MAXO:0000950 supportive care, or a dietary-supplement modality).
- **Folinic acid (folinic acid/leucovorin)** — targeted therapy for patients with documented low CSF 5-methyltetrahydrofolate or MRI white-matter abnormalities, dosed at 1.5–5 mg/kg/day (max 100 mg/day); "reported to improve neurologic symptoms in a few individuals" and can "reverse white matter abnormalities" (MAXO relevant: pharmacotherapy, NCIT:C15986).
- **Antioxidant supplementation** (general mitochondrial cocktail approach).
- **Investigational CoQ10 analog EPI-743** (vatiquinone/alpha-tocotrienol quinone derivative) was studied in KSS — registered trial **NCT01370447** ([ClinicalTrials.gov search synthesis](https://www.ncbi.nlm.nih.gov/books/NBK482341/)).
- **Anti-seizure medications** for the subset with epilepsy.
- **Hormone replacement therapy** for endocrinopathies (insulin for diabetes, calcium/calcitriol for hypoparathyroidism, growth hormone, corticosteroids for adrenal insufficiency, sex hormone replacement for hypogonadism) — under endocrinology guidance.

**Advanced/experimental therapeutics:**
- **Gene therapy / mtDNA-targeting nuclease approaches**: zinc-finger nucleases (mitoZFNs) designed to selectively degrade mutant/deleted mtDNA and shift heteroplasmy toward wild-type have been explored experimentally ([StatPearls NBK482341](https://www.ncbi.nlm.nih.gov/books/NBK482341/)).
- **iPSC-based cell replacement research**: patient-derived induced pluripotent stem cells have been generated and evaluated as a potential source of isogenic cell-replacement therapy for KSS ([PMC7998189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7998189/)).
- **Mitochondrial augmentation therapy (MAT)**: autologous CD34+ hematopoietic stem cells enriched with exogenous healthy mitochondria have been used under compassionate use in at least one juvenile KSS patient with tunnel vision, ptosis, ophthalmoplegia, and retinal atrophy, reportedly improving cellular oxygen consumption/energy production in preclinical/early clinical work ([search synthesis, Nature STTT review 2024](https://www.nature.com/articles/s41392-024-02044-3)).
- A pharmaceutical developer (Precision, per industry search results) reported preclinical work toward an IND submission targeting muscle in 2025, though no approved product exists as of this writing.

**Surgical and interventional:**
- **Prophylactic cardiac pacemaker implantation** for conduction block — considered standard of care given the risk of sudden death from progression to complete heart block; **implantable cardioverter-defibrillator (ICD)** considered in select cases (MAXO: cardiac device implantation; NCIT:C15329 Surgical Procedure category).
- **Strabismus surgery / frontalis sling surgery** for severe ptosis/ophthalmoplegia (MAXO:0000004 surgical procedure).
- **Esophageal sphincter dilation** for cricopharyngeal achalasia.
- **Gastrostomy tube placement** for dysphagia/failure to thrive.
- **Cochlear implantation / hearing aids** for sensorineural hearing loss (MAXO:0009030 hearing aid usage; device-based intervention).

**Supportive/rehabilitative care:**
- Physical and occupational therapy for myopathy/ataxia (MAXO:0000011 physical therapy).
- Nutritional optimization, dietary intervention (MAXO:0000088).
- Genetic counseling (MAXO:0000079).
- Regular multidisciplinary surveillance (below).

**Treatment outcomes/adverse events:** No large randomized controlled trial has established efficacy for CoQ10 or antioxidant "mitochondrial cocktails" — benefit described in the literature is largely anecdotal/case-based. **Volatile anesthetic hypersensitivity** is a documented adverse-response risk requiring anesthesia protocol modification (avoid prolonged propofol) ([orphananesthesia.eu](https://www.orphananesthesia.eu/rare-diseases/published-guidelines/kearns-sayre-syndrome/281-kearns-sayre-syndrome/file.html)).

**Treatment strategy / surveillance algorithm** (from GeneReviews):
- **Annually**: neurology, audiology, developmental/cognitive assessment, ophthalmology, endocrinology, complete blood count.
- **Every 6–12 months**: EKG and echocardiogram.
- **At every visit**: growth parameters, nutritional status, aspiration risk, mobility assessment.

**Personalized medicine approaches:** Given the deletion-driven, heteroplasmy-dependent biology, individualized surveillance intensity is generally scaled to known heteroplasmy burden/deletion characteristics rather than a genotype-directed drug-selection paradigm (unlike, e.g., oncology precision medicine).

---

## 13. Prevention

- **Primary prevention:** None available — the causal mtDNA deletion arises as a stochastic de novo event; there is no known modifiable risk factor to prevent its occurrence.
- **Secondary prevention (early detection):** The most clinically impactful secondary-prevention measure is **proactive cardiac surveillance (regular ECG/Holter monitoring) with prophylactic pacemaker placement before complete heart block develops**, directly reducing sudden cardiac death risk.
- **Tertiary prevention:** The full multidisciplinary surveillance/management program described above (endocrine monitoring and hormone replacement, nutritional support/gastrostomy for aspiration risk, hearing/vision aids, physical therapy) is designed to prevent or mitigate downstream complications of established disease.
- **Immunization:** No KSS-specific vaccine strategy; standard immunization is recommended, with attention to minimizing febrile/catabolic stress that could unmask mitochondrial decompensation (a general mitochondrial-disease management principle rather than a KSS-specific finding in the literature reviewed).
- **Genetic screening/counseling:** Because most cases are de novo, population/carrier screening is not applicable in the way it is for Mendelian recessive disorders. Family counseling should establish maternal mtDNA deletion status to estimate the **~4%** sibling recurrence risk if the mother is a carrier, versus **≤1%** if she is not. Prenatal/preimplantation testing remains technically limited due to heteroplasmy quantification challenges.
- **Public health/environmental interventions:** Not applicable — no environmental exposure has been identified as a modifiable population-level risk factor.
- **Prophylaxis:** The clearest "prophylactic" medical intervention specific to this disease is the **prophylactic pacemaker**, discussed above.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** The engineered/experimental disease models are in **mouse (*Mus musculus*, NCBITaxon:10090)**. No naturally occurring veterinary KSS-equivalent disease was identified in this search (OMIA was not found to list a directly analogous natural condition in companion animals).
- **Breed:** Not applicable — no breed-specific natural disease identified.
- **Orthologous genes:** The mtDNA-encoded genes affected (ND3, ND4, ND4L, ND5, COI–COIII, ATP6/8, mt-tRNAs) are highly conserved across vertebrate species given the near-universal function of the mitochondrial electron transport chain; comparative mtDNA sequences are catalogued via NCBI Gene/GenBank across mammalian species.
- **Natural disease in other species:** Not identified as a spontaneously occurring veterinary disease entity in the sources reviewed; this remains predominantly a modeled (not naturally occurring) disease outside humans.
- **Comparative biology:** The bioenergetic threshold principle (heteroplasmy load driving OXPHOS dysfunction once a critical mutant fraction is exceeded) is evolutionarily conserved and forms the basis for using mouse trans-mitochondrial models to recapitulate the human threshold effect (see below).
- **Transmission:** Not applicable — KSS is not a transmissible/zoonotic disease.

---

## 15. Model Organisms

**Mammalian genetic models:**
- **"Mito-mice∆" (trans-mitochondrial mice)**: heteroplasmic mice engineered to carry a mixture of wild-type mtDNA and a **∆mtDNA (deleted mitochondrial genome)**, generated via cytoplast/cybrid transfer techniques. "The proportion of ∆mtDNA in various tissues of surviving mito-mice∆ increased with time, and Kearns-Sayre syndrome-like phenotypes were expressed when the proportion of ∆mtDNA in various tissues reached >70–80%" ([PMC3755915](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755915/)).
  - **Phenotype recapitulation**: This model reproduces the human **Pearson-to-KSS transition** — "late-stage embryos carrying ≥50% ∆mtDNA showed abnormal hematopoiesis and iron metabolism in livers similar to Pearson syndrome phenotypes, with more than half of the neonates with PS-like phenotypes dying by 1 month after birth," while surviving mice that accumulate higher ∆mtDNA burden in postmitotic tissue over time go on to develop the KSS-like multisystem phenotype — directly mirroring the human natural history where infantile Pearson syndrome survivors later develop KSS.
  - **Applications**: studying the tissue-specific segregation dynamics of deleted vs. wild-type mtDNA over development/aging, and testing the heteroplasmy threshold model quantitatively.
- **PolG "mutator" mouse**: carries a proofreading-deficient mitochondrial DNA polymerase gamma (POLG), causing accelerated accumulation of mtDNA point mutations and (to a lesser extent) deletions with age, used as a broader model of somatic mtDNA mutation accrual and premature aging-like phenotypes; complements the mito-mice∆ model though it models polymerase-driven mutagenesis rather than the single clonal deletion event characteristic of human KSS ([PMC8620558](https://pmc.ncbi.nlm.nih.gov/articles/PMC8620558/)).

**Cellular models:**
- **Patient-derived induced pluripotent stem cells (iPSCs)**: generated from KSS patients and evaluated as an isogenic source for cell-replacement therapeutics and to model tissue-specific heteroplasmy segregation in vitro ([PMC7998189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7998189/)).
- **Cybrid cell lines**: cytoplasmic hybrid cell models (patient mitochondria fused with mtDNA-depleted rho-zero recipient cells) have historically been used to study the biochemical consequences of the specific deletion in isolation from nuclear genetic background — a standard approach in the mitochondrial disease field, though a KSS-specific cybrid paper was not individually retrieved in this search.

**Model limitations:** Mouse trans-mitochondrial models require artificial cytoplast-transfer generation of the ∆mtDNA line (the deletion does not arise spontaneously in mice as it does in human oogenesis), and murine tissue bioenergetic thresholds/lifespan differ from humans, meaning the exact percentage thresholds and tissue-specific timing may not map precisely onto human disease. No model to date fully recapitulates the specific human ophthalmoplegia/pigmentary retinopathy phenotype in as much clinical detail as the systemic/hematologic (Pearson-like) and general multisystem energy-deficiency phenotypes.

**Resources:** Mouse Genome Informatics (MGI) for mito-mice∆ and PolG mutator strain records; broadly, IMSR/EMMA/MMRRC for repository access to relevant mitochondrial-disease mouse strains.

---

## Summary of Key Primary Citations

| Citation | Contribution |
|---|---|
| Kearns TP, Sayre GP. *Arch Ophthalmol* 1958;60:280-289 | Original clinical description of the triad |
| Holt IJ, Harding AE, Morgan-Hughes JA. *Nature* 1988;331:717-719. PMID: [2830540](https://pubmed.ncbi.nlm.nih.gov/2830540/) | First demonstration of mtDNA deletions in mitochondrial myopathy patients |
| GeneReviews — Single Large-Scale Mitochondrial DNA Deletion Syndromes ([NBK1203](https://www.ncbi.nlm.nih.gov/books/NBK1203/)) | Comprehensive clinical/molecular/management reference (primary source for this report) |
| OMIM #530000 ([omim.org/entry/530000](https://omim.org/entry/530000)) | Clinical synopsis and molecular genetics |
| Orphanet ORPHA:480 | Epidemiology and clinical summary |
| StatPearls ([NBK482341](https://www.ncbi.nlm.nih.gov/books/NBK482341/)) | Concise clinical/management overview |
| PMC5893934 | Pathological mechanisms/heteroplasmy threshold data |
| PMC3755915 | Mito-mice∆ mouse model, Pearson-to-KSS transition |
| Molecular Neurobiology 2024, PMID: [38224444](https://pubmed.ncbi.nlm.nih.gov/38224444/) | Cellular/molecular response mechanisms (ROS, autophagy, demyelination) |
| PMC6719858 | SSBP1 nuclear-gene secondary KSS case |
| PMC7998189 | iPSC-based cell-replacement therapy research |
| ClinicalTrials.gov NCT05554835 / NCT01370447 | Natural history registry / EPI-743 trial |

---

**Sources:**
- [Single Large-Scale Mitochondrial DNA Deletion Syndromes - GeneReviews® - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1203/)
- [Entry - #530000 - KEARNS-SAYRE SYNDROME; KSS - OMIM](https://omim.org/entry/530000)
- [Orphanet: Kearns-Sayre syndrome](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=480)
- [Kearns-Sayre Syndrome - StatPearls - NCBI Bookshelf - NIH](https://www.ncbi.nlm.nih.gov/books/NBK482341/)
- [Kearns-Sayre syndrome - MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/kearns-sayre-syndrome/)
- [Kearns-Sayre Syndrome: Practice Essentials, Pathophysiology, Epidemiology - Medscape](https://emedicine.medscape.com/article/950897-overview)
- [Pathological mechanisms underlying single large-scale mitochondrial DNA deletions - PMC5893934](https://pmc.ncbi.nlm.nih.gov/articles/PMC5893934/)
- [Mitochondrial DNA with a Large-Scale Deletion Causes Two Distinct Mitochondrial Disease Phenotypes in Mice - PMC3755915](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755915/)
- [The mtDNA mutation spectrum in the PolG mutator mouse reveals germline and somatic selection - PMC8620558](https://pmc.ncbi.nlm.nih.gov/articles/PMC8620558/)
- [Deletions of muscle mitochondrial DNA in patients with mitochondrial myopathies - PubMed 2830540](https://pubmed.ncbi.nlm.nih.gov/2830540/)
- [Cellular and Molecular Responses to Mitochondrial DNA Deletions in Kearns-Sayre Syndrome - PubMed 38224444](https://pubmed.ncbi.nlm.nih.gov/38224444/)
- [Mitochondrial single-stranded DNA binding protein novel de novo SSBP1 mutation - PMC6719858](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6719858/)
- [Autosomal-recessive Kearns-Sayre syndrome (RRM2B) - Thieme](https://www.thieme-connect.com/products/ejournals/abstract/10.1055/s-0033-1337752)
- [Generation and Evaluation of Isogenic iPSC as a Source of Cell Replacement Therapies in Patients with Kearns Sayre Syndrome - PMC7998189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7998189/)
- [Mitochondrial diseases: from molecular mechanisms to therapeutic advances - Nature STTT](https://www.nature.com/articles/s41392-024-02044-3)
- [Treatment of Kearns-Sayre syndrome with coenzyme Q10 - PubMed 3941783](https://pubmed.ncbi.nlm.nih.gov/3941783/)
- [Global Registry and Natural History Study for Mitochondrial Disorders - NCT05554835](https://clinicaltrials.gov/study/NCT05554835)
- [2024 ICD-10-CM Diagnosis Code H49.81: Kearns-Sayre syndrome](https://www.icd10data.com/ICD10CM/Codes/H00-H59/H49-H52/H49-/H49.81)
- [Kearns–Sayre Syndrome Minus: Two Cases outside the Classical Triad - PMC9056216](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9056216/)
- [Kearns-Sayre Ptosis - EyeWiki](https://eyewiki.org/Kearns-Sayre_Ptosis)
- [orphananesthesia.eu Kearns-Sayre syndrome anesthesia guideline](https://www.orphananesthesia.eu/rare-diseases/published-guidelines/kearns-sayre-syndrome/281-kearns-sayre-syndrome/file.html)
- [A unique 3.5-kb deletion of the mitochondrial genome in Thai patients with Kearns-Sayre syndrome - PubMed 10480366](https://pubmed.ncbi.nlm.nih.gov/10480366/)
- [Fatal pneumonia in a patient with Kearns-Sayre syndrome - PMC12350349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12350349/)