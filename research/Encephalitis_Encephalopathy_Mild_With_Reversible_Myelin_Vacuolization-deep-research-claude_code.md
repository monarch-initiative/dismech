---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:08.535069'
end_time: '2026-10-14T15:52:22.237539'
duration_seconds: 193.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Encephalitis/Encephalopathy, Mild, with Reversible Myelin Vacuolization
  mondo_id: MONDO:0020853
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
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 14
  total_cost_usd: 1.9946298000000002
  session_id: 8e000f55-6d59-40d4-ac72-8ea5a05dc851
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 8
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Encephalitis/Encephalopathy, Mild, with Reversible Myelin Vacuolization
- **MONDO ID:** MONDO:0020853 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Encephalitis/Encephalopathy, Mild, with Reversible Myelin Vacuolization** covering all of the
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

I'm collecting the primary literature: the Kurahashi 2018 discovery paper, the OMIM entry, and the later case reports. The report comes next.

# Encephalitis/Encephalopathy, Mild, with Reversible Myelin Vacuolization (MMERV): Research Report

**MONDO:0020853 · OMIM #618113 · Gene: *MYRF* (OMIM *608329; hgnc:1181)**

*Scope:* Fewer than 20 genotyped patients have been published. The quotes below marked "verified" were read in this session from the repository's local reference cache (`references_cache/`) or from OMIM. I have not checked PMIDs marked "unverified". Run `just fetch-reference` on them before citing. The PubMed and OLS MCP servers need authorization in claude.ai connector settings and were not available, so no new ontology lookups were made. Every CURIE below either already appears in `kb/disorders/Encephalitis_Encephalopathy_Mild_With_Reversible_Myelin_Vacuolization.yaml` or is marked as a suggestion to be looked up.

---

## 1. Disease Information

**Overview.** MMERV is an autosomal dominant disorder. It causes repeated or single episodes of acute, mild encephalopathy, usually triggered by fever or infection, in people whose development is otherwise normal. During an episode, MRI shows extensive symmetric restricted diffusion in the corpus callosum (especially the splenium) and the deep cerebral white matter. The lesions and the symptoms resolve within days to about 2 weeks. The disorder lies on the same clinical spectrum as sporadic MERS (mild encephalitis/encephalopathy with a reversible splenial lesion), but it is familial and the white matter involvement is more extensive.

OMIM summary (verified via OMIM mirror): MMERV is an *"episodic acute reversible encephalopathy that occurs in children and is frequently associated with a trigger, such as a febrile illness."*

**Identifiers**
| System | ID |
|---|---|
| MONDO | MONDO:0020853 |
| OMIM (phenotype) | #618113 |
| OMIM (gene) | *608329 (MYRF); allelic variant .0001 = Q403R |
| MedGen | C4722446 |
| KEGG Disease | H02489 |
| Orphanet / ICD-10 / ICD-11 | No specific code found. ICD-10 G93.4 (other and unspecified encephalopathy) or G93.40 is the nearest generic code. |

**Synonyms:** MMERV; MYRF-related mild encephalopathy with reversible myelin vacuolization (the name proposed by Kurahashi et al. 2018); familial MERS; familial mild encephalopathy with a reversible splenial lesion and extensive white matter involvement.

**Source of the data:** Everything comes from individual pedigree and case reports. No registry or EHR cohort exists.

**Name origin (verified, PMID:29265453):** *"We propose the term 'MYRF-related mild encephalopathy with reversible myelin vacuolization.'"*

---

## 2. Etiology

**Primary cause.** A heterozygous germline missense variant in *MYRF*. The recurrent variant is c.1208A>G, p.Gln403Arg (Q403R), which sits in the conserved Ndt80-like DNA-binding domain.

> "we identified a heterozygous c.1208A>G predicting p.Gln403Arg in the highly conserved DNA-binding domain in the myelin regulatory factor (MYRF) gene." (PMID:29265453, verified)

**Triggers (environmental and infectious).** Febrile infections trigger episodes. Reported triggers include unspecified febrile viral illnesses, SARS-CoV-2 (PMID:35990002), and influenza or COVID-like fever in the Chinese proband (PMID:38155716). One allelic case with a different variant was triggered by influenza A H1N1 (PMID:41190523). OMIM also lists stress as a trigger.

> "Infectious diseases in children are a major triggering factor for MMERV" (PMID:38155716, verified)

**Gene–environment interaction.** The published working model is that mutant MYRF supports myelin adequately at baseline but becomes insufficient under the metabolic and inflammatory stress of infection. OMIM attributes this hypothesis to Kurahashi et al. It is plausible but has not been tested experimentally.

**Genetic risk and modifiers.** No modifier genes are known. Penetrance is incomplete (Section 9).

**Protective factors.** None are known. The 2023 review suggests reducing infections:

> "Minimizing infections can help reduce disease recurrence." (PMID:38155716, verified) This is an expert suggestion without supporting data.

**Sporadic MERS is genetically different.** Kurahashi et al. sequenced *MYRF* in 33 sporadic MERS cases and found the variant only in the second family. *MYRF* therefore does not account for typical sporadic MERS.

---

## 3. Phenotypes

All phenotypes are episodic, start in childhood (as young as 2–3 years) through young adulthood, are mild, and reverse completely. Frequencies cannot be estimated reliably from roughly 9–15 patients; the qualitative estimates below are my own.

| Phenotype | HPO (from current entry, or suggested) | Frequency / notes |
|---|---|---|
| Acute encephalopathy | HP:0001298 Encephalopathy | Defining (all affected) |
| Impaired consciousness / confusion | HP:0001289 Confusion; suggest looking up "Reduced consciousness/confusion" | Very frequent |
| Delirium / abnormal behavior | HP:0031258 Delirium | Frequent |
| Seizures, often febrile in early childhood, with lip smacking or eye deviation | HP:0001250 Seizure; consider HP:0002373 Febrile seizure (look up) | Frequent; often the first sign |
| Speech disturbance: dysarthria, non-fluency, aphasia-like "impaired verbal communication" | HP:0001260 Dysarthria | Frequent; recurrent episodes of non-fluency in the adult Chinese proband |
| Ataxia | HP:0001251 Ataxia | Occasional |
| Limb numbness / transient motor weakness | Suggest paresthesia or hemiparesis terms (look up) | Occasional (PMID:35990002) |
| Reversible white matter lesions (corpus callosum, centrum semiovale) | HP:0002352 Leukoencephalopathy; suggest a "splenium of corpus callosum" abnormality term; HP:0002181 Brain edema (intramyelinic) | Defining imaging finding |
| Restricted diffusion on DWI (low ADC) | Suggest a "restricted diffusion on MRI" term (look up) | Defining |
| Normal serum sodium | Laboratory finding | Differs from sporadic MERS, where hyponatremia is common (Imamura 2010) |

Key clinical quotes (verified):
- PMID:29265453: *"recurrent encephalopathy with extensive but reversible cerebral myelin vacuolization and neurological symptoms similar to those of MERS spanning 3 generations."*
- PMID:35990002: *"a 14-year-old girl with a heterozygous p. Gln403Arg variant in the MYRF gene, who had five episodes of encephalopathy. She experienced reduced consciousness, numbness in the arm, and impaired verbal communication from day 4 of SARS-CoV-2 infection."*
- PMID:38155716: *"The clinical manifestations of MMERV include seizures, impaired speech (such as lack of fluency, dysarthria, and language difficulties), recurrent episodes of impaired consciousness (confusion or delirium), spontaneous motor difficulties, and limb numbness"*

**Quality of life.** No quality-of-life instrument data exist. Between episodes patients function normally. The burden comes from recurrent acute hospitalizations and the anxiety that goes with them.

---

## 4. Genetic and Molecular Information

- **Gene:** *MYRF* (myelin regulatory factor; formerly C11orf9). Location 11q12.2. hgnc:1181 (in the local HGNC cache).
- **Variant:** NM_001127392 c.1208A>G, p.Gln403Arg. It is in the N-terminal Ndt80/PhoG-like DNA-binding domain and was found in both Japanese families. OMIM reports that haplotype analysis suggested a **founder effect**. The Chinese family (PMID:38155716) carries a heterozygous *MYRF* variant described as related. Check the exact variant in that paper's full text before recording it.
- **Classification:** OMIM lists it as allelic variant .0001. I did not check its ClinVar classification in this session.
- **Origin:** Germline, segregating with disease.
- **Population frequency:** Not established here. Kurahashi et al. filtered for rare variants. Check gnomAD.
- **Functional effect:** Partial loss of function, a hypomorphic reduction in transactivation:
  > "Luciferase assay revealed that transcriptional activity of the N-terminal region of MYRF was significantly diminished by introducing the c.1208A>G variant." (PMID:29265453, verified)

  Whether Q403R acts dominant-negatively on the MYRF trimer has not been tested. The trimerization requirement (PMID:23966832) makes this a reasonable open question.
- **Allelic MYRF disorders (spectrum context).** These are the reason to keep MMERV as its own entry:
  - **Cardiac-urogenital syndrome:** de novo, mostly loss-of-function variants; congenital heart disease, diaphragmatic hernia, and genital anomalies. Key paper: Pinz et al. 2018 (unverified PMID).
  - **Nanophthalmos / high hyperopia:** Garnai et al. 2019 and others (unverified PMIDs).
  - **Persistent (non-reversible) leukoencephalopathy after H1N1 infection,** caused by the C-terminal variant p.Gly735Asp:
    > "establishes persistent leukoencephalopathy as a novel clinical phenotype within the MYRF disease spectrum." (PMID:41190523, verified)
- **Epigenetic or chromosomal changes:** None reported.

---

## 5. Environmental Information

- **Infectious triggers:** non-specific febrile viral infections; SARS-CoV-2 (NCBITaxon:2697049, look up); influenza A virus (NCBITaxon:11320, look up) in the allelic persistent-leukoencephalopathy case.
- **Lifestyle factors:** none known.
- **Toxins:** none implicated.
- **Suggested exposure term:** an ECTO "exposure to virus" class. Search ECTO before binding one; the repository forbids writing CURIEs from memory.

---

## 6. Mechanism and Pathophysiology

### Causal chain
1. **Heterozygous *MYRF* c.1208A>G (p.Gln403Arg)** changes a conserved residue in the N-terminal DNA-binding domain (PMID:29265453).
2. This **reduces the transcriptional activation activity** of the cleaved N-terminal MYRF fragment. This was shown in luciferase assays (in vitro).
3. MYRF is normally a membrane-anchored ER protein. It trimerizes and cleaves itself through an intramolecular chaperone domain related to bacteriophage tailspike proteins, which releases the N-terminal transcription factor into the nucleus (PMID:23966832, PMID:23966833). The variant therefore **weakens a normally constitutive myelin-gene transcription program** after release; the cleavage step itself is unaffected.
4. **Less direct activation of myelin and oligodendrocyte gene enhancers.** The link to specific genes is inferred. ChIP-seq in the normal state shows that the N-terminal fragment *"directly binds the enhancer regions of oligodendrocyte-specific and myelin genes"* (PMID:23966833, verified). Target genes include MBP, PLP1, MOG, and MAG.
5. **Mature oligodendrocytes have a reduced reserve for maintaining myelin.** This is inferred from mouse models: adult deletion of *Myrf* causes loss of oligodendrocyte identity and myelin integrity (Koenning et al. 2012, J Neurosci, PMID:22956843, unverified).
6. **Febrile or systemic infection** acts as a second hit, through fever, cytokines, and possibly metabolic stress. The mechanism is hypothesized, not demonstrated.
7. **Intramyelinic edema and myelin vacuolization** follow, through splitting of myelin lamellae at the intraperiod line. The authors infer this from imaging; there is no human histopathology.
   - **Branch, imaging:** restricted diffusion (low ADC) and T2/FLAIR hyperintensity in the corpus callosum (splenium first) and the centrum semiovale.
8. **Transiently impaired axonal conduction** in the affected white matter tracts (inferred) causes encephalopathy, confusion or delirium, seizures, dysarthria, and ataxia.
9. **The vacuolization resolves** once the trigger clears, so imaging and symptoms normalize within about 1–2 weeks. Steroids may speed recovery, but there are no controlled data.

**Contrast with sporadic MERS / cytotoxic lesions of the corpus callosum (CLOCCs).** In sporadic MERS, cytokine-mediated cytotoxic edema and hyponatremia have been proposed. MMERV adds a constitutional myelin-maintenance defect, which probably explains why its lesions are more extensive and why episodes recur.

### Annotations (from the current entry unless marked)
- **Molecular function:** GO:0000981, DNA-binding transcription factor activity, RNA polymerase II-specific.
- **Biological processes:** GO:0045944 positive regulation of transcription by RNA polymerase II; GO:0043217 myelin maintenance; GO:0022010 central nervous system myelination; GO:0019227 neuronal action potential propagation. Suggested additions, to look up: protein autoprocessing and protein homotrimerization.
- **Cell types:** CL:0000128 oligodendrocyte; CL:0002453 mature oligodendrocyte.
- **Cellular component, suggested:** endoplasmic reticulum membrane (full-length MYRF) and nucleus (cleaved N-terminal fragment).
- **Biological scale tags:** the variant node is MOLECULAR; oligodendrocyte myelin maintenance is CELLULAR; vacuolization and edema are TISSUE; encephalopathy is ORGANISM.

**Molecular profiling:** No transcriptomic, proteomic, metabolomic, or single-cell data exist for MMERV patients. No GEO datasets were found.

---

## 7. Anatomical Structures Affected

- **Organ and system:** brain, central nervous system (UBERON:0001017). No other organs are involved, unlike the syndromic MYRF disorders.
- **Specific sites:** corpus callosum (UBERON:0002336), splenium of the corpus callosum (UBERON:0013750), cerebral hemisphere white matter (UBERON:0002437; centrum semiovale), white matter (UBERON:0002316).
- **Cells:** oligodendrocytes, mature oligodendrocytes, and the myelin sheath (GO cellular component "myelin sheath"; look up).
- **Lateralization:** bilateral and symmetric.

---

## 8. Temporal Development

- **Onset:** early childhood (seizures from about 32 months in Family A; ages 2–9 in Family B, with the mother affected at age 6). The Chinese proband had adult episodes from age 19, after febrile seizures in childhood.
- **Pattern:** acute, starting within days of a febrile illness (day 4 of SARS-CoV-2 infection in PMID:35990002).
- **Course:** episodic, relapsing and remitting. The disease does not progress between episodes. Up to five episodes have been reported in one patient.
- **Duration of an episode:** a few days to about 1 week clinically. MRI normalized within days to 13 days (PMID:38155716).
- **Critical window:** the febrile phase of infection.
- **Remission:** spontaneous, or after steroid treatment.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006). Three-generation transmission is documented.
- **Penetrance:** incomplete. Verified quote from PMID:38155716: *"His father, aunt, and grandmother all carry the same variant in the MYRF gene, despite having no history of recursive neurological symptoms or cognitive deterioration."* (Note: the cached sentence says "His", although the proband is described elsewhere in the paper as female. Check this against the full text before quoting.)
- **Expressivity:** variable. It ranges from a single childhood febrile seizure, to adult speech dysfluency, to five or more full encephalopathy episodes.
- **Founder effect:** suggested in the two Japanese families (OMIM, from Kurahashi et al.).
- **Epidemiology:** ultra-rare. About 9 individuals in the two Japanese families (4 definite, 5 suspected affected according to OMIM), plus the Saito 2022 patient (one of the original family members followed up) and the Chinese family (2023). There is no prevalence figure.
- **Populations:** Japanese and Chinese so far. This probably reflects ascertainment bias, since MERS is recognized most often in East Asia.
- **Sex ratio:** both sexes affected.
- **Anticipation, consanguinity:** not reported.

---

## 10. Diagnostics

- **Neuroimaging (the key test):** brain MRI during an episode shows symmetric diffusion-weighted hyperintensity with low ADC in the corpus callosum and centrum semiovale, and follow-up imaging shows it resolving. Suggested NCIT term: NCIT:C16809 Magnetic Resonance Imaging (already in the entry). Repeat MRI to document reversal is required for the diagnosis.
- **EEG:** may show slowing during an episode (Kurahashi et al. used EEG; the details are in the full text).
- **Laboratory:** cerebrospinal fluid is generally unremarkable. Serum sodium is normal, unlike in many sporadic MERS cases. Infectious workup identifies the trigger. Mitochondrial DNA testing was negative in the Chinese proband.
- **Genetic testing:** exome sequencing found the gene. Targeted *MYRF* sequencing, or a leukoencephalopathy or epilepsy panel that includes *MYRF*, is appropriate for familial or recurrent MERS. Testing of relatives (cascade testing) is reasonable. Suggested NCIT term: NCIT:C15709 Genetic Testing (already in the entry).
  > "The definitive diagnosis of MMERV can be confirmed through genetic analysis." (PMID:38155716, verified)
- **Diagnostic criteria:** none formal. In practice: familial or recurrent MERS-like episodes, plus extensive reversible white matter diffusion restriction, plus a heterozygous *MYRF* variant.
- **Differential diagnosis:**
  - Sporadic MERS / CLOCCs (single episode, mostly splenial lesion, often hyponatremia)
  - X-linked Charcot-Marie-Tooth disease type 1 (CMTX1, *GJB1*), which causes transient stroke-like white matter lesions
  - Acute disseminated encephalomyelitis (ADEM)
  - Acute necrotizing encephalopathy (*RANBP2*)
  - Mitochondrial disease
  - Toxic or metabolic leukoencephalopathy (for example, metronidazole)
  - Persistent MYRF leukoencephalopathy (PMID:41190523)
- **Screening:** none at the population level.

---

## 11. Outcome and Prognosis

- **Mortality:** none reported.
- **Recovery:** complete after each episode. OMIM states there are no permanent neurologic sequelae. The Saito patient recovered *"completely within a week"* (PMID:35990002, verified).
- **Morbidity:** recurrent acute admissions. No cognitive decline was seen in follow-up up to adulthood.
- **Prognostic factors:** unknown. Allelic variants outside the DNA-binding domain (G735D) can leave persistent lesions, which suggests that genotype affects reversibility.

---

## 12. Treatment

No disease-specific therapy exists, and there are no trials.
- **Corticosteroids (empirical):** intravenous methylprednisolone pulse, 1 g/day for 3 days (PMID:35990002), or a methylprednisolone 500 mg taper followed by oral prednisone (PMID:38155716). Suggested annotation: NCIT:C15986 Pharmacotherapy as `treatment_term`, with methylprednisolone (CHEBI term, look up) as `therapeutic_agent` and modality SMALL_MOLECULE. Recovery also happens spontaneously, so the benefit of steroids is unproven.
  > "She was treated with a single course of intravenous methylprednisolone pulse therapy (1 g/day for 3 days), which resulted in an immediate improvement in her symptoms." (PMID:35990002, verified)
- **Supportive care:** antiseizure medication for acute seizures, fever control, and treatment of the infection. Suggested NCIT term: NCIT:C15747 Supportive Care.
- **Gene, cell, or RNA therapies; clinical trials:** none. No NCT or ICTRP records were found.

---

## 13. Prevention

- **Primary prevention:** not applicable beyond genetic counseling. Each child of a carrier has a 50% chance of inheriting the variant, and penetrance is incomplete. Suggested NCIT term: NCIT:C15240 Genetic Counseling.
- **Secondary and tertiary prevention:** avoid infections and keep vaccinations up to date, including influenza and COVID-19 (expert suggestion, PMID:38155716). Prompt MRI and supportive care during febrile illness in known carriers.
- **Prenatal or preimplantation testing:** technically possible once the familial variant is known. Its use for a mild, reversible disorder would need careful counseling.

---

## 14. Other Species and Natural Disease

- No naturally occurring MYRF-related reversible myelin vacuolization has been reported in animals. No OMIA entry was found.
- **Orthologs:** mouse *Myrf* (MGI), zebrafish *myrf*, and *C. elegans* *myrf-1* (which acts in synaptic rewiring). The Ndt80-like DNA-binding domain is conserved down to yeast Ndt80 and *Dictyostelium*.
- **Comparative note:** some veterinary toxic and inherited spongiform leukoencephalopathies show intramyelinic vacuolization, but none has been linked to *MYRF*.

---

## 15. Model Organisms

| Model | Phenotype | Relevance and limits |
|---|---|---|
| *Myrf* oligodendrocyte-specific conditional knockout, developmental (Emery et al. 2009, Cell; PMID:19596243, unverified) | Severe CNS hypomyelination; oligodendrocytes fail to mature | Shows MYRF is needed for myelination. It is a null allele, not a hypomorph, and does not model episodic disease. |
| Inducible adult *Myrf* deletion in mature oligodendrocytes (Koenning et al. 2012, J Neurosci; PMID:22956843, unverified) | Progressive demyelination; loss of myelin gene expression | Shows MYRF is needed to *maintain* myelin. This is the closest mechanistic support for the model above, but it is progressive and irreversible, not episodic. |
| Cell lines / HEK293 luciferase assays (PMID:29265453) | Reduced transactivation by Q403R | The only functional test of the variant itself (in vitro). |
| Heterologous reconstitution in *E. coli* and yeast (PMID:23966832) | Constitutive trimerization-dependent self-cleavage | Mechanism of MYRF activation. |
| **Gap** | No Q403R knock-in mouse; no fever or infection challenge model; no patient iPSC-derived oligodendrocytes | Whether infection causes reversible vacuolization in a hypomorphic *Myrf* background has not been tested. In the repository's scheme this is a `KNOWLEDGE_GAP` (evidence absent), not a `HUMAN_MODEL_MISMATCH`. |

---

## Key References

| PMID | Citation | Use | Status |
|---|---|---|---|
| 29265453 | Kurahashi H et al. *MYRF is associated with encephalopathy with reversible myelin vacuolization.* Ann Neurol 2018;83:98–106 | Gene discovery, phenotype, functional assay | Cached, verified |
| 35990002 | Saito M et al. *Mild encephalitis with a reversible splenial lesion associated with SARS-CoV-2 infection in a patient with MYRF variant.* Front Pediatr 2022 | Trigger, recurrence, steroids | Cached, verified |
| 38155716 | Yao S et al. *MYRF-related MMERV: a case report and literature review.* Front Genet 2023 | Chinese family, penetrance, review | Cached, verified |
| 41190523 | Hu J et al. *Persistent leukoencephalopathy following H1N1 infection associated with a novel MYRF variant (p.Gly735Asp).* Ann Clin Transl Neurol 2026 | Allelic, non-reversible phenotype | Cached, verified |
| 23966833 | Bujalka H et al. *MYRF is a membrane-associated transcription factor that autoproteolytically cleaves…* PLoS Biol 2013 | Mechanism, ChIP-seq | Cached, verified |
| 23966832 | Li Z et al. *A bacteriophage tailspike domain promotes self-cleavage of… MYRF.* PLoS Biol 2013 | Trimerization and self-cleavage | Cached, verified |
| 20042198 | Imamura T et al. *Sisters with clinically mild encephalopathy with a reversible splenial lesion (MERS)-like features; familial MERS?* J Neurol Sci 2010;290:153–156 | First clinical description of Family B | PMID taken from OMIM; not cached |
| 22956843 | Koenning M et al. J Neurosci 2012 (adult *Myrf* deletion) | Model organism | Unverified |
| 19596243 | Emery B et al. Cell 2009 (*Myrf* discovery) | Model organism | Unverified |

**Web sources consulted:**
- [OMIM #618113 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/omim/618113)
- [OMIM *608329 MYRF (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/omim/608329)
- [MedGen C4722446](https://ncbi.nlm.nih.gov/medgen/C4722446)
- [KEGG H02489](https://www.kegg.jp/entry/H02489)
- [Frontiers in Genetics 2023 (PMID:38155716)](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2023.1284060/pdf)
- [Saito et al. 2022, PMC9386134](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9386134/)
- [Imamura et al. 2010 bibliographic record](https://wicri-demo.istex.fr/Wicri/Sante/explor/MersV1/Site/fr/Ncbi/Merge/bibRecord.php?hk=000728)
- [Recurrent MERS case series, PMC8722321](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8722321/)
