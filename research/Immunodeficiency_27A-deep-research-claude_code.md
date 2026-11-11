---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-11T11:38:15.408469'
end_time: '2026-11-11T11:40:41.515006'
duration_seconds: 146.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Immunodeficiency 27A
  mondo_id: MONDO:0008856
  category: Mendelian
  causal_genes: IFNGR1
  omim_id: OMIM:209950
  synonyms: immunodeficiency 27A, mycobacteriosis, AR; immunodeficiency type 27A
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 15
  total_cost_usd: 2.1719037
  session_id: 27b47c7c-352a-4c25-9e59-a58e3d8b5112
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 3
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 27A
- **MONDO ID:** MONDO:0008856 (if available)
- **Causal gene(s):** IFNGR1
- **OMIM:** OMIM:209950
- **Synonyms:** immunodeficiency 27A, mycobacteriosis, AR; immunodeficiency type 27A
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 27A** covering all of the
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

Hear ye! Let me check what the kitchen already holds before I go foraging.

Let me read those abstracts directly instead.

Hear ye! The report is below. Every quoted sentence was checked against this repository's `references_cache/` copy of the cited paper. Anything I could not check that way is marked **still in the oven**.

---

# Immunodeficiency 27A (MONDO:0008856): research report

**Causal gene: *IFNGR1*** (hgnc:5439), on chromosome 6q23.3. It encodes the IFN-γ receptor 1 chain, the part of the interferon-gamma receptor that binds IFN-γ. Immunodeficiency 27A (IMD27A, OMIM:209950) is the **autosomal recessive** form of IFN-γR1 deficiency. It should not be confused with **Immunodeficiency 27B** (OMIM:615978, ORPHA:319581), the autosomal dominant, dominant-negative form caused by the same gene, or with **Immunodeficiency 28**, which is IFNGR2 deficiency.

## 1. Disease information

- **Overview.** IMD27A is a form of Mendelian susceptibility to mycobacterial disease (MSMD). People with it are highly susceptible to weakly virulent mycobacteria: BCG vaccine strains and environmental (nontuberculous) mycobacteria. Their routine blood counts and immune tests are otherwise normal. MSMD is defined as "a rare condition characterized by predisposition to clinical disease caused by weakly virulent mycobacteria, such as BCG vaccines and environmental mycobacteria, in otherwise healthy individuals with no overt abnormalities in routine hematological and immunological tests" (Bustamante et al., *Semin Immunol* 2014, **PMID:25453225**). IFNGR1 was the first MSMD gene identified, in 1996 (**PMID:8960473**).
- **Two recessive forms, which differ by how much signalling is left:**
  - *AR complete deficiency*: no response to IFN-γ at all. Usually no receptor reaches the cell surface; in a rarer form the receptor is on the surface but cannot bind IFN-γ (**PMID:10811850**). MONDO:0020530; **ORPHA:99898** (Orphanet code confirmed via MedGen).
  - *AR partial deficiency*: cells still respond to high IFN-γ concentrations. The alleles are the founder variants I87T and V63G and the start-codon variant M1K (**PMID:21266457**, **PMID:19880857**). MONDO:0017901. I did not confirm an Orphanet code for this form (**still in the oven**).
- **Other identifiers.** The Orphanet parent group "AR MSMD due to a complete deficiency" is ORPHA:319535. I did not look up ICD-10/ICD-11 or MeSH codes. MeSH indexes these papers under "Receptors, Interferon/deficiency" and "Mycobacterium Infections, Nontuberculous/genetics".
- **Synonyms.** IMD27A; immunodeficiency type 27A; immunodeficiency 27A, mycobacteriosis, AR; autosomal recessive IFN-γR1 deficiency; familial atypical mycobacteriosis.
- **Where the data come from.** Almost everything comes from case reports and multicentre case series of individual patients, collected by a few international consortia, mainly the Casanova/Bustamante group and the Holland group at NIH. No EHR-based data exist.

## 2. Etiology

- **Cause.** Germline biallelic loss-of-function variants in *IFNGR1*. "Most of the autosomal recessive IFNGR1 mutations are homozygous loss-of-function single-nucleotide variants, whereas large genomic deletions and compound heterozygosity have been very rarely reported" (Bossi et al., *J Pediatr Genet* 2020, **PMID:32714620**).
- **Trigger.** Disease needs exposure to mycobacteria: live BCG vaccine or environmental mycobacteria such as *M. avium* complex and rapidly growing species. Less often the trigger is *M. tuberculosis* or non-typhoidal *Salmonella*.
- **Genetic risk factors.** Consanguinity, which explains the usual homozygosity, and founder populations: I87T in Chile, Portugal and Poland, and V63G in the Canary Islands (**PMID:21266457**).
- **Environmental risk factors.** BCG vaccination. In the Dorman series, "all nine BCG-vaccinated patients had BCG disease" (*Lancet* 2004, **PMID:15589309**). Environmental exposure to nontuberculous mycobacteria (NTM) cannot be avoided.
- **Protective factors.** None genetic are known. Not giving BCG to at-risk siblings is the one practical environmental protection (see §13).
- **Gene–environment interaction.** The interaction is the disease itself: the genotype sets susceptibility, and the mycobacterial exposure sets when and where disease appears.

## 3. Phenotypes

| Phenotype | HPO (as bound in the KB entry) | Onset / frequency | Key evidence |
|---|---|---|---|
| Disseminated NTM infection | HP:0032283 Disseminated nontuberculous mycobacterial infection | Complete form: 17/22 (77%); mean first-episode age 3.1 y. Partial form: mean 11.25 ± 9.13 y | **PMID:15589309**, **PMID:21266457** |
| BCG disease (local to disseminated) | HP:5210408 BCG-associated disease | 9/9 BCG-vaccinated complete-deficiency patients | **PMID:15589309** |
| Mycobacterial osteomyelitis | HP:5210276 Unusual mycobacterial osteomyelitis | Mainly the partial form (10 patients). Only 1/8 in the complete form vs 22/28 in the dominant form | **PMID:25453225**, **PMID:15589309**, **PMID:16195661** |
| Rapidly growing mycobacteria | (no specific term chosen) | 7/22 (32%) complete vs 1/38 dominant | **PMID:15589309** |
| Tuberculosis | HP:5210111 Tuberculosis infection | Occasional; 2 complete-form cases, one fatal | **PMID:25453225**, **PMID:9389728** |
| Salmonellosis | HP:5210093 Unusual Salmonella infection | Rare: 3 complete-form and 3 partial-form patients | **PMID:25453225**, **PMID:21266457** |
| Lymphadenopathy, hepatosplenomegaly, intermittent fever | HP:0002716, HP:0001433, HP:0001954 | Usual presentation in early childhood | **PMID:26931784** |
| Elevated plasma IFN-γ (laboratory) | HP:0030356 | Complete form and the M1K partial form | **PMID:25453225**, **PMID:19880857** |
| Lepromatous-like (complete) vs tuberculoid (partial) granulomas (histology) | — | Distinguishes the two forms | **PMID:10811850**, **PMID:9389728** |

**Supporting quotes:**
- "Compared with dominant patients, those with recessive deficiency were younger at onset of first environmental mycobacterial disease (mean 3.1 years [SD 2.5] vs 13.4 years [14.3], p=0.001), had more mycobacterial disease episodes (19 vs 8 per 100 person-years of observation, p=0.0001), had more severe mycobacterial disease (mean number of organs infected by Mycobacterium avium complex 4.1 [SD 0.8] vs 2.0 [1.1], p=0.004)…" (**PMID:15589309**)
- "Most commonly, patients with complete IFN-γR1 deficiency present with lymphadenopathy, hepatosplenomegaly and intermittent fever in early childhood, caused by infection with weakly virulent, mostly environmental mycobacteria" (**PMID:26931784**; this sentence is in the paper's introduction, so it restates earlier findings rather than reporting the authors' own result).

**Other notes:**
- **Severity and course.** The complete form is severe and progressive: disease-free intervals averaged 1.6 years, and it is fatal without transplant. The partial form varies from mild to severe; "Up to 10 patients are currently free of infection with no prophylaxis" (**PMID:21266457**).
- **Rarer infections.** Viral infections (CMV, HHV8, RSV, VZV) and *Listeria* are listed for the complete form in **PMID:25453225**, with no frequencies given.
- **Quality of life.** No EQ-5D, SF-36 or other quality-of-life data exist for this disease. The burden is years of multi-drug antibiotic treatment, hospital stays, and the risks of transplantation.

## 4. Genetic and molecular information

- **Gene.** *IFNGR1*, OMIM *107470, hgnc:5439. The receptor is "a tetramer of two IFN-γR1 chains in complex with two IFN-γR2 chains, where IFN-γR1 is the ligand-binding chain" (van de Vosse & van Dissel, *Hum Mutat* 2017, **PMID:28744922**).
- **Allelic spectrum.** "Forty unique IFNGR1 mutations have been reported… Mutations resulting in premature stopcodons represent the majority of IFNGR1 mutations (60%; 24 out of 40), followed by amino acid substitutions (28%, 11 out of 40)." That count covers 135 individuals from 98 kindreds, both inheritance modes combined (**PMID:28744922**). The variants are collected in the LOVD database at www.LOVD.nl/IFNGR1.
  - **Complete, no surface receptor.** Nonsense, frameshift and splice variants that stop the protein before its membrane-anchoring segment. The founding variant: "a point mutation at nucleotide 395 that introduces a stop codon and results in a truncated protein that lacks the transmembrane and cytoplasmic domains" (Newport et al., *NEJM* 1996, **PMID:8960473**).
  - **Complete, receptor on the surface.** Two in-frame deletions and two missense variants in the extracellular ligand-binding domain. These "cause complete IFNgammaR1 deficiency by disrupting the IFN-gamma-binding site without affecting surface expression" (**PMID:10811850**).
  - **Structural variants.** A 119,227-nt homozygous deletion at 6q23.3 removes the whole gene and ends 117 nt upstream of *IL22RA2*, with no effect on that gene (**PMID:26931784**). One patient was compound heterozygous for a subpolymorphic copy-number variant and a splice variant (**PMID:32714620**).
  - **Partial.** I87T and V63G are founder missense variants; their most recent common ancestors lived about 1,600 and about 500 years ago (**PMID:21266457**). M1K (start codon) allows "leaky translation initiation at both non-AUG codons and the third AUG codon at position 19" (Kong et al., *HMG* 2010, **PMID:19880857**).
- **Classification and frequency.** I did not query ClinVar, ACMG classifications or gnomAD frequencies for individual variants (**still in the oven**). Recessive pathogenic alleles are expected to be very rare.
- **Origin.** Germline. No somatic or mosaic cases have been reported.
- **Functional consequence.** Loss of function, complete or hypomorphic. The dominant-negative mechanism belongs to IMD27B, not to this entry.
- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported, apart from the 6q23.3 deletion.
- **ClinGen.** I did not check whether ClinGen has a gene–disease validity classification for this pair.

## 5. Environmental information

- **Infectious agents:** *Mycobacterium bovis* BCG; *M. avium* complex; rapidly growing mycobacteria (*M. chelonae*, *M. fortuitum*, *M. abscessus*); *M. szulgai*; *M. tuberculosis*; non-typhoidal *Salmonella*. Case series report these organisms (**PMID:15589309**, **PMID:25453225**).
- **Toxins and lifestyle factors:** none are relevant.

## 6. Mechanism and pathophysiology

**Causal chain:**

1. **Biallelic germline *IFNGR1* loss-of-function variants** lead to →
2. **Absent receptor, or a receptor that cannot bind IFN-γ**: no surface protein (**PMID:8960473**), or a surface receptor with a disrupted binding site (**PMID:10811850**). In the partial form there is a hyporesponsive receptor or a small amount of normal receptor (**PMID:19880857**). This leads to →
3. **Loss of IFN-γ-induced JAK–STAT1 signalling.** STAT1 is not activated, and IFN-γ-induced genes are not switched on in monocytes, macrophages, B cells and fibroblasts. The block is absolute in the complete form and dose-dependent in the partial form. Patient cells were tested at 10 and 10,000 IU/ml: "cells from a child with complete IFNgammaR1 deficiency did not respond to even high IFN-gamma concentrations (10,000 IU/ml), cells from the two siblings did not respond to low or intermediate concentrations, yet responded to high IFN-gamma concentrations" (**PMID:9389728**). This leads to →
4. **Failed macrophage activation.** TNF-α is not up-regulated, IL-12 is not produced, and macrophages do not become able to kill mycobacteria (**PMID:8960473**). This leads to →
5. **Uncontrolled replication of mycobacteria inside macrophages**, which branches three ways:
   - 5a → **dissemination** to lymph nodes, liver, spleen and bone, producing the clinical picture in §3;
   - 5b → **poorly formed granulomas**: lepromatous-like, with many bacilli and few or no giant cells, in the complete form; tuberculoid in the partial form. This feeds back into dissemination (**PMID:10811850**);
   - 5c → **continued IL-12-driven IFN-γ production by T and NK cells**, which still works, so **high plasma IFN-γ** builds up with nothing to respond to it. This step is **inferred** from the known IL-12 → IFN-γ circuit, not directly demonstrated in these patients (**PMID:25453225**). High IFN-γ is thought to contribute to graft rejection after transplant (**PMID:26173802**).
6. **Severity follows residual signalling.** "Strikingly, the severity and penetrance of MSMD are inversely correlated with the residual levels of IFN-γ" (Bustamante, *Hum Genet* 2020, **PMID:32025907**). Dorman reports "a strong correlation… between IFNGR1 genotype, cellular responsiveness to interferon gamma, and clinical disease features" (**PMID:15589309**).

**Ontology suggestions** (all already validated in the KB entry):
- GO: GO:0004906 type II interferon receptor activity (decreased); GO:0060333 type II interferon-mediated signaling pathway (decreased); GO:0042116 macrophage activation (decreased); GO:0042742 defense response to bacterium (decreased).
- CL: CL:0000235 macrophage; CL:0000576 monocyte; CL:0000236 B cell; CL:0000057 fibroblast; CL:0000545 T-helper 1 cell; CL:0000623 natural killer cell.
- GO cellular component: plasma membrane (the receptor's location). **Still in the oven**: I have not looked up that CURIE.

**Molecular profiling.** I found no transcriptomic, proteomic, single-cell or CRISPR-screen studies specific to IMD27A.

## 7. Anatomical structures affected

- **Primary:** the immune system (mononuclear phagocytes).
- **Organs infected:** lymph nodes, liver, spleen, bone (more often in the partial form), lungs, skin and soft tissue at the BCG injection site, and rarely the brain (**PMID:16195661**).
- **UBERON suggestions** (**still in the oven**: these are leads I have not looked up): lymph node, liver, spleen, bone tissue, lung.
- **Laterality:** not applicable; the disease is systemic.

## 8. Temporal development

- **Onset.** Complete form: infancy or early childhood. "Infections typically begin in early childhood, before three years of age" (**PMID:25453225**). It often follows BCG given at birth. Partial form: childhood to adulthood. One patient first became ill at 20, after "she was completely healthy up until the present illness" (**PMID:16195661**).
- **Course.** Complete form: relapsing and progressive, with a mean disease-free interval of 1.6 years and lower Kaplan–Meier survival (p<0.0001) (**PMID:15589309**). Partial form: separate episodes that usually respond to treatment.
- **Critical window.** Before BCG vaccination, and before transplant: transplant outcomes are best when infection is controlled and IFN-γ levels have normalised (**PMID:26173802**).

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). "Complete IFN-gamma receptor ligand-binding chain (IFNgammaR1) deficiency is a life-threatening autosomal recessive immune disorder" (**PMID:10811850**).
- **Penetrance.** Complete for the complete form. The complete IFN-γR1 and IFN-γR2 deficiencies are among "the only four genetic etiologies shown to date to be fully penetrant (i.e. Mendelian) in childhood and always lethal before the third decade of life in the absence of hematopoietic stem cell transplantation (HSCT)" (**PMID:32025907**). Expressivity in the partial form varies even with identical genotypes (**PMID:16195661**, **PMID:21266457**).
- **Founder effects:** I87T in Chile, Portugal and Poland; V63G in the Canary Islands (**PMID:21266457**).
- **Consanguinity:** frequent in reported kindreds. No anticipation or germline mosaicism has been reported.
- **Epidemiology.** Ultra-rare.
  - Complete AR form: 31 patients from 26 families by 2014 (**PMID:25453225**); 32 patients by 2015, described as about 8% of MSMD (**PMID:26173802**); 36 cases by 2016 (**PMID:26931784**).
  - Partial AR form: about 15 patients (**PMID:25453225**).
  - MSMD as a whole affects "about 1/50,000 individuals worldwide" (**PMID:32025907**). That figure is an upper bound for the whole group, not a rate for this genotype. No rate specific to IMD27A has been published.
  - No sex bias is reported.

## 10. Diagnostics

1. **Flow cytometry for IFN-γR1 (CD119) on monocytes or granulocytes.** Absent receptor supports the complete form: "There was no expression of the IFN-γR1 on the monocytes" (**PMID:26931784**). A normal result does **not** rule out deficiency: "The detection of surface IFNgammaR1 molecules by specific antibodies, including blocking antibodies, does not exclude a diagnosis of complete IFNgammaR1 deficiency" (**PMID:10811850**).
2. **Functional assays with graded IFN-γ doses.** Readouts include STAT1 phosphorylation or nuclear translocation, HLA class II induction in fibroblasts, CD64 induction and TNF-α/IL-12p40 production in monocytes, and whole-blood tests with LPS plus IFN-γ (**PMID:9389728**, **PMID:26931784**).
3. **Plasma IFN-γ.** High levels point to a receptor defect: "Plasma IFN-γ concentration was very high (370 ng/ml, undetectable in controls…)" (**PMID:19880857**).
4. **Genetic testing.** *IFNGR1* sequencing within an MSMD or inborn-errors-of-immunity panel, or exome/genome sequencing. **Copy-number analysis is essential**, because whole-gene deletions and CNVs are missed by sequencing alone (**PMID:26931784**, **PMID:32714620**).
5. **Histopathology.** Lepromatous-like granulomas with many bacilli in the complete form; tuberculoid granulomas in the partial form.
6. **Differential diagnosis:**
   - IFNGR2 deficiency (Immunodeficiency 28): same clinical picture; told apart by sequencing.
   - IL-12Rβ1 or IL-12p40 deficiency: a defect in making IFN-γ, not responding to it. Cells respond to IFN-γ, plasma IFN-γ is not raised, and recombinant IFN-γ works.
   - STAT1 deficiency.
   - Dominant IFNGR1 deficiency (IMD27B): later onset, bone-predominant disease.
   - Chronic granulomatous disease: ruled out with the dihydrorhodamine (DHR) test.
   - Anti-IFN-γ autoantibodies in adults with late-onset disease (**still in the oven**: not from cached sources).
   - SCID.
7. **Screening.** No newborn screening exists. Carrier and cascade testing and prenatal diagnosis are possible once the family's variants are known.
8. **Guidelines.** GeneReviews has no chapter for this disease; the repository's Bookshelf index confirms the absence.

## 11. Outcome and prognosis

- **Complete form:** "The overall prognosis is poor, with 17 deaths reported for the 31 known patients (58%) patients, including four deaths after HSCT" (**PMID:25453225**). "Affected children invariably die of mycobacterial infection, unless bone marrow transplantation is undertaken" (**PMID:10811850**).
- **Partial form:** "Only one of the 15 patients reported to date died (6.6%)" (**PMID:25453225**). In the Sologuren series, 13 of 14 were alive at a mean age of 14.8 years (**PMID:21266457**).
- **Prognostic factors:** how much IFN-γ signalling remains (the most important factor); lepromatous-like granulomas; organ dissemination; high plasma IFN-γ before transplant.
- **Complications:** organ dissemination, antibiotic toxicity, graft rejection and graft-versus-host disease after HSCT.

## 12. Treatment

| Treatment | NCIT suggestion | Applies to | Evidence |
|---|---|---|---|
| Haematopoietic stem cell transplantation (HSCT) | NCIT:C15431 Hematopoietic Cell Transplantation | Complete form; the only cure | "Although hematopoietic stem cell transplantation (HSCT) remains the only curative treatment, outcomes are heterogeneous; delayed engraftment and/or graft rejection being commonly observed" (**PMID:26173802**). "Ideal transplant conditions include control of mycobacterial infection, normalized IFN-γ levels, myeloablative conditioning and a non-T-cell-depleted graft…" (**PMID:26173802**) |
| Long-term multi-drug antimycobacterial therapy | NCIT:C15620 Antibiotic Therapy | Both forms | Complete form: "Antibiotic treatment should not be stopped." Partial form: "Prophylactic antibiotics are not required" (**PMID:25453225**) |
| Recombinant IFN-γ (subcutaneous) | NCIT:C15986 Pharmacotherapy + agent NCIT:C583 Recombinant Interferon Gamma | **Partial form only** | "Mycobacteriosis progressed in spite of treatment with antituberculous drugs and was controlled only after addition of interferon-gamma subcutaneously" (**PMID:16195661**). Complete form: "Treatment with IFN-γ is not indicated, owing to the lack of specific receptors" (**PMID:25453225**) |
| IFN-α | NCIT:C225 Recombinant Interferon Alfa | Tried in the complete form; not established | "variable clinical responses"; "exogenous IFN-α treatment may aggravate mycobacterial disease" (**PMID:25453225**) |

- **HSCT is not indicated for the partial form:** "HSCT is not indicated, given the relatively mild infectious phenotype" (**PMID:25453225**). The exception is the severe M1K patient, who was transplanted.
- **Gene therapy.** A lentiviral *IFNGR1* gene therapy has been explored in preclinical work, including a mouse model of pulmonary macrophage transplantation (Hetzel et al., *Nat Commun* 2018). **Still in the oven**: I did not verify the PMID, and I know of no registered NCT trial.
- **Pharmacogenomics:** not applicable.

## 13. Prevention

- **Primary:** genetic counselling, carrier testing in families, prenatal or preimplantation diagnosis.
- **Secondary:** avoid BCG vaccination in siblings and newborns of affected families until IFNGR1 status is known (**inferred** from the 9/9 BCG-disease rate, **PMID:15589309**). Diagnose early in any child with BCG disease or disseminated NTM infection.
- **Tertiary:** keep antimycobacterial treatment going; transplant early in the complete form, once infection is under control.
- **Vaccines:** live BCG is contraindicated.

## 14. Other species and natural disease

- **Naturally occurring animal disease:** I found no IFNGR1 deficiency in OMIA. **Still in the oven**: I did not query OMIA directly.
- **Orthologues:** mouse *Ifngr1* (MGI) and others. I did not look up NCBI Gene IDs.
- **Zoonotic potential:** none for the genetic defect. The pathogens are environmental or come from the vaccine.

## 15. Model organisms

- ***Ifngr1*-knockout mouse.** Huang et al., "Immune Response in Mice That Lack the Interferon-γ Receptor," *Science* 1993;259:1742–1745, DOI 10.1126/science.8456301 ([record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_75642227)). **Still in the oven**: I did not confirm the PMID, so look it up before citing.
  - What it shows: the mice develop normally, but resistance to intracellular pathogens such as *Listeria* and BCG is impaired, which models the human susceptibility.
  - Limitations: inbred laboratory mice do not reproduce the human pattern of disseminated environmental mycobacteria and BCG-osis, and their granulomas differ from human ones.
- **Cellular models.** Patient EBV-B cell lines and primary fibroblasts are used to grade IFN-γ responsiveness (**PMID:9389728**, **PMID:19880857**). Patient iPSC-derived macrophages have been used in IFNGR gene-therapy research; I did not verify the specific citations.
- **Resources:** MGI, IMSR, JAX (B6.129S7-*Ifngr1*^tm1Agt^ is commonly used; **still in the oven**).

---

## What I checked and what I didn't

- **Checked:** every quote marked with a PMID was compared against the 13 cached abstracts and full texts in this worktree. The HPO, GO, CL and NCIT terms in the tables come from the existing `kb/disorders/Immunodeficiency_27A.yaml`.
- **Not checked:**
  - the PMID of the 1993 mouse knockout paper;
  - ClinVar, gnomAD and ClinGen data;
  - the UBERON suggestions;
  - an Orphanet code for the partial recessive form;
  - the gene-therapy citations.

Taste-tested where it counts; leads only where I said so.

> *Oh, the receptor's gone from the table, and the gravy finds no plate,*
> *so we read it in the plasma, where the IFN piles high and late!*

**Sources (web lookups):**
- [MedGen – complete IFNγR1 deficiency (ORPHA:99898)](https://ncbi.nlm.nih.gov/medgen/1789166)
- [NORD/MONDO page – MSMD due to complete IFNγR1 deficiency](https://rarediseases.org/mondo-disease/mendelian-susceptibility-to-mycobacterial-diseases-due-to-complete-ifngammar1-deficiency/)
- [Huang et al. 1993 bibliographic record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_75642227)