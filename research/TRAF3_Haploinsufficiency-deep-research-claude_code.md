---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-26T12:59:49.016733'
end_time: '2026-08-26T13:04:04.593728'
duration_seconds: 255.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TRAF3 Haploinsufficiency
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 27
  total_cost_usd: 1.2799766
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TRAF3 Haploinsufficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TRAF3 Haploinsufficiency** covering all of the
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

Now let me fetch the full-text PMC pages for the key primary papers.

I now have sufficient depth across all major domains. Let me compile the comprehensive research report.

# TRAF3 Haploinsufficiency: Comprehensive Disease Research Report

## 1. Disease Information

**Overview.** TRAF3 haploinsufficiency (TRAF3-HI, also cataloged as Immunodeficiency-132B / IMD132B) is a recently delineated (2022–2024) autosomal dominant monogenic immune dysregulation syndrome caused by heterozygous loss-of-function variants in *TRAF3* (TNF Receptor-Associated Factor 3, chromosome 14q32.32). It is distinct from — but mechanistically related to — an earlier-described entity, **Immunodeficiency-132A (IMD132A)**, caused by a *dominant-negative* (rather than simple loss-of-function/haploinsufficient) *TRAF3* variant and first linked to susceptibility to herpes simplex encephalitis (HSE) ([Pérez de Diego et al., 2010, PMID 20832341](https://pubmed.ncbi.nlm.nih.gov/20832341/); [OMIM #614849](https://www.omim.org/entry/614849)).

TRAF3-HI/IMD132B was formally characterized in a 2022 *Science Immunology* study of 9 individuals from 5 unrelated families ([Wan/Uzel et al., PMID unlisted directly but DOI 10.1126/sciimmunol.abn3800](https://www.science.org/doi/10.1126/sciimmunol.abn3800); [OMIM #621096](https://omim.org/entry/621096)), and expanded in a 2024 *Journal of Clinical Immunology* cohort study (Urban et al., PMID 39579173) that used a TRAF3-targeted reanalysis of next-generation sequencing data from 800 inborn-errors-of-immunity (IEI) patients, identifying 3 additional patients in 2 families who had previously carried a diagnosis of common variable immunodeficiency (CVID).

**Key identifiers:**
- **OMIM (phenotype):** #621096 (IMD132B, TRAF3-HI; loss-of-function) and #614849 (IMD132A; dominant-negative)
- **OMIM (gene):** *601896 — TNF Receptor-Associated Factor 3; TRAF3
- **Gene location:** 14q32.32
- **MalaCards:** "Immunodeficiency 132B"
- **MONDO:** No stable, indexed MONDO term was retrievable via search at the time of this report (the entity is very recently described; Mondo/Monarch integration may lag behind the 2022–2024 primary literature — this should be verified directly against a current Mondo release before curation, as no confirmed MONDO CURIE could be established from available sources)
- **HGNC:** TRAF3 (gene ID for the causal gene)

**Synonyms:** TRAF3 deficiency; TRAF3 haploinsufficiency syndrome (TRAF3-HI); Immunodeficiency 132B (IMD132B); CD40-associated protein 1 / CAP-1 (historical alternate gene name); LAP1 (historical alternate gene name).

**Data derivation:** Almost all clinical characterization comes from **aggregated case series** (9 patients/5 families in the founding paper; 3 more patients/2 families in the follow-up cohort study derived from an 800-patient IEI sequencing registry) rather than large-scale EHR/population data, consistent with an ultra-rare, newly described monogenic disorder.

---

## 2. Etiology

### Disease Causal Factors
TRAF3-HI is caused by **heterozygous loss-of-function (LOF) variants in TRAF3** (premature stop-codon/nonsense, frameshift) that reduce TRAF3 mRNA and protein to roughly half of normal levels in patient PBMCs — true haploinsufficiency, as opposed to the dominant-negative missense mechanism of IMD132A. Reported LOF variants include stop-gain mutations **p.Arg163\*** and **p.Gln407\*** (Urban et al., 2024, PMID 39579173).

By contrast, IMD132A is caused by a **de novo dominant-negative missense variant**, **c.352C>T (p.Arg118Trp, R118W)**, in the first of TRAF3's five zinc-finger domains; Western blot in the index patient showed TRAF3 protein reduced to ~17.5% of control levels — far below the ~50% expected from simple haploinsufficiency — indicating the mutant protein actively destabilizes wild-type TRAF3 (dominant-negative interference) (PMID 20832341; [OMIM #614849](https://www.omim.org/entry/614849)). A second dominant-negative variant, **R338W**, has been reported in a patient with chronic pulmonary *Mycobacterium abscessus* infection ([Open Forum Infect Dis, PMID 36004314](https://academic.oup.com/ofid/article/9/8/ofac379/6654828)).

### Risk Factors
- **Genetic:** Inheritance of a heterozygous LOF or dominant-negative *TRAF3* allele is both necessary and sufficient risk. No modifier genes are yet established, though variable expressivity within families (see Inheritance section) implies unidentified genetic or environmental modifiers.
- **Age:** A 2025 PNAS study (Hornick et al., PMID 40773231) found that **TRAF3 protein (but not mRNA) declines with normal aging** in human B cells — comparing donors over 65 vs. under 32 years — via proteasome-mediated (bortezomib-reversible) degradation rather than transcriptional loss. This suggests age itself is a "second hit" that phenocopies genetic haploinsufficiency, plausibly explaining age-related increases in B-cell hyperactivity and B-cell malignancy risk in the general population, and predicting that TRAF3-HI patients' phenotypes may worsen with age.
- **Chronic receptor engagement:** Sustained **CD40 ligand (CD40L) signaling** — as occurs in lupus and Sjögren's disease — drives ongoing TRAF3 degradation and could compound genetic deficiency.

### Protective Factors
No specific genetic or environmental protective factors have been identified in the literature to date.

### Gene-Environment Interactions
The clearest documented interaction is the convergence of **chronic B-cell-receptor pathway signaling (CD40, BAFF-R/TNFRSF13C)** with reduced TRAF3 dosage: BAFF-receptor stimulation causes *sustained* TRAF3 reduction (>72 hours) while CD40 stimulation causes *transient* reduction (recovery by 24h), but both converge on NF-κB2 (non-canonical) activation — meaning inflammatory/infectious triggers that engage these receptors chronically could exacerbate B-cell dysregulation in genetically haploinsufficient individuals (PMID 40773231).

---

## 3. Phenotypes

TRAF3-HI presents as a **complex, variably expressive immune dysregulation syndrome** combining immunodeficiency, autoimmunity, and lymphoproliferation — a triad increasingly recognized across NF-κB pathway primary immunodeficiencies.

**Core/consistent features (IMD132B):**
- **Recurrent upper and lower respiratory tract infections** with diverse pathogens, onset in childhood — HPO: Recurrent respiratory infections (**HP:0002205**)
- **Bronchiectasis** — HPO: Bronchiectasis (**HP:0002110**) (documented in a 36-year-old male index patient with lifelong sinopulmonary infections)
- **B-cell lymphoid hyperplasia / lymphoproliferation** — HPO: Lymphoproliferative disorder-adjacent terms; Lymphadenopathy (**HP:0002716**)
- **T-cell subset dysregulation** — low/mildly reduced CD4+ T-cell counts, decreased naive T cells, increased CD4+ memory T cells, variably increased regulatory T cells (Tregs), increased circulating T follicular helper (Tfh) cells, and impaired T-cell proliferative responses

**Variable features:**
- **Autoimmune disease with autoantibodies** (e.g., autoimmune hepatitis-type presentations, cytopenias reported across the NF-κB-PID literature) — HPO: Autoimmunity (**HP:0002960**)
- **Systemic autoinflammation**
- **Gastrointestinal inflammation** — one index patient had ileitis and chronic active pancolitis — HPO: Inflammation of the large intestine (**HP:0002037**)/Ileitis
- **Hepatosplenomegaly** — HPO: Hepatosplenomegaly (**HP:0001433**); the index 36-year-old also had **nodular lymphoid hyperplasia**
- **B-cell maturation defects**: reduced class-switched memory B cells, increased naive B cells
- **Dysgammaglobulinemia**: hyper- *or* hypogammaglobulinemia (both directions reported) — HPO: Hypergammaglobulinemia (**HP:0010702**) / Hypogammaglobulinemia (**HP:0004313**)
- **Increased risk of B-cell malignancy** (see Prognosis section)

**IMD132A-specific phenotype (dominant-negative form):**
- **Herpes simplex encephalitis (HSE)** in childhood — HPO: Encephalitis (**HP:0002383**); impaired TLR3-dependent interferon-β and IL-6 production upon poly(I:C) stimulation
- **Chronic pulmonary *Mycobacterium abscessus* infection**, treatment-resistant, reported in an adult patient — HPO: Recurrent bronchitis/Nontuberculous mycobacterial infection

**Age of onset:** Predominantly childhood for the core immunodeficiency/lymphoproliferative phenotype; some manifestations (e.g., chronic *M. abscessus* infection) present in adulthood.

**Severity/progression:** Variable and progressive in at least some patients (bronchiectasis implies cumulative structural lung damage from recurrent infection); course is chronic/lifelong.

**Quality of life impact:** Not formally quantified in the literature (no EQ-5D/SF-36 data identified); qualitatively, the combination of recurrent infection, chronic GI inflammation, and immunoglobulin-replacement dependence implies substantial burden, consistent with other CVID-spectrum disorders.

---

## 4. Genetic/Molecular Information

**Causal gene:** TRAF3 (HGNC symbol TRAF3; historically CAP1, LAP1), 14q32.32, OMIM *601896.

**Variant classes reported:**

| Variant | Type | Effect | Associated phenotype | Source |
|---|---|---|---|---|
| c.352C>T (p.Arg118Trp) | Missense, zinc-finger domain 1 | Dominant-negative; protein reduced to ~17.5% of control | IMD132A — HSE | PMID 20832341 |
| p.Arg338Trp (R338W) | Missense | Dominant-negative | IMD132A — *M. abscessus* infection, bronchiectasis | PMID 36004314 |
| p.Arg163\* | Nonsense (stop-gain) | Loss-of-function (haploinsufficiency) | IMD132B — CVID-like | PMID 39579173 |
| p.Gln407\* | Nonsense (stop-gain) | Loss-of-function (haploinsufficiency) | IMD132B — CVID-like | PMID 39579173 |
| Multiple additional LOF variants (5 families) | Various premature-stop/frameshift | Haploinsufficiency (~50% reduced protein/mRNA) | IMD132B founding cohort | Science Immunology, abn3800 |

**Protein domain architecture:** TRAF3 has an N-terminal **RING-type zinc-finger domain** (required for TRAF3's role in downregulating NF-κB2/p100 processing) and additional zinc fingers, followed by a C-terminal **MATH/TRAF domain**, which mediates receptor binding — the crystal structure of the CD40 cytoplasmic tail bound to the TRAF3 MATH domain shows the CD40 peptide binding as a hairpin loop across the domain surface.

**Functional consequence:** `functional_impact_category`-relevant — LOF variants → **LOSS_OF_FUNCTION** (haploinsufficiency, ~50% protein/mRNA reduction); R118W and R338W → **DOMINANT_NEGATIVE** (disproportionate reduction of total TRAF3 below the 50% haploinsufficiency threshold via interference with wild-type protein).

**Population frequency / ClinVar:** ClinVar records specific TRAF3 variants under "Herpes simplex encephalitis, susceptibility to, 3" (e.g., NM_145725.3:c.810C>T and c.651+13G>C). No large-scale gnomAD constraint or general-population carrier-frequency statistic specific to disease-causing LOF alleles was retrieved; TRAF3 is broadly conserved and intolerant of loss-of-function based on its essential immune-regulatory role (inferred from mouse knockout lethality, below).

**Somatic vs. germline distinction:** Germline heterozygous LOF/dominant-negative variants cause the Mendelian immunodeficiency syndrome. Separately, **somatic** homozygous deletions and inactivating mutations of TRAF3 are well documented as recurrent, non-germline drivers in **multiple myeloma** and **B-cell non-Hodgkin lymphoma**, where TRAF3 behaves as a bona fide tumor suppressor via constitutive non-canonical NF-κB activation. This is mechanistically related but etiologically distinct from the germline haploinsufficiency syndrome.

**Epigenetics:** No disease-specific DNA methylation/histone data were identified; however, the 2025 PNAS aging study shows TRAF3 protein (not mRNA) declines with age via **proteasomal degradation**, a post-translational rather than epigenetic mechanism.

**Chromosomal abnormalities:** No recurrent aneuploidy/translocation involving 14q32.32 is described for the germline syndrome (distinct from the well-known 14q32 IGH translocations in B-cell malignancy, which is a different genomic phenomenon).

---

## 5. Environmental Information

- **Infectious triggers:** Herpes simplex virus-1 is the specific documented trigger for encephalitis in IMD132A; *Mycobacterium abscessus* is documented as a chronic pulmonary pathogen in TRAF3-deficient patients. Diverse unspecified bacterial/viral pathogens drive the recurrent sinopulmonary infections seen in IMD132B.
- **Lifestyle/toxin factors:** None specifically implicated in the literature reviewed.
- No infectious *cause* of the underlying disease itself is implicated (this is a monogenic immunodeficiency, not an infection-triggered disease); rather, infection is a downstream *phenotypic consequence* of the impaired antiviral/antibacterial immune signaling.

---

## 6. Mechanism / Pathophysiology

### Molecular pathway
TRAF3 is a cytoplasmic adaptor that functions **downstream of CD40, BAFF-receptor (BAFF-R/TNFRSF13C), other TNFR-superfamily members, TLR3/TRIF, and RIG-I-like receptors**. Its central, disease-relevant role is as a **negative regulator of the non-canonical (alternative) NF-κB2 pathway**: together with TRAF2 and cIAP1/2, TRAF3 constitutively targets **NIK (NF-κB-inducing kinase)** for K48-linked polyubiquitination and proteasomal degradation, keeping NF-κB2/p100→p52 processing suppressed at baseline. Receptor engagement (CD40L, BAFF) triggers TRAF3's own K48-ubiquitination and degradation, releasing NIK, and permitting NF-κB2 (p52) activation and downstream B-cell survival/differentiation signaling. TRAF3 also participates in **TLR3-TRIF-dependent type I interferon induction** (IFN-β) relevant to antiviral defense (PMID 20832341) and in canonical NF-κB/MAPK regulation more broadly.

### Causal chain (haploinsufficiency form, IMD132B)
1. **Trigger:** Heterozygous LOF *TRAF3* variant → ~50% reduction in TRAF3 protein/mRNA in B cells and PBMCs.
2. **Molecular consequence:** Insufficient TRAF3-TRAF2-cIAP degradation of NIK → **increased basal and receptor-stimulated non-canonical NF-κB2 (p52) activation** — shown to be "significantly more abundant" in heterozygous mouse B cells vs. wild-type, at levels intermediate between wild-type and complete knockout.
3. **Downstream transcriptional/metabolic effects:** Dose-dependent elevation of pro-survival proteins **Mcl1, Pim2, c-Myc**, and the glycolytic enzyme **Hxk2**; increased **mitochondrial respiration**; heightened **phospho-STAT3 (Y705)** signaling downstream of IL-6 receptor engagement.
4. **Cellular consequence:** Prolonged B-cell survival in vitro (heterozygous B cells outlive wild-type through day 3 of culture before dying by day 5), increased splenic B-cell numbers and plasma cells (splenic but not bone-marrow), and altered B-cell maturation (reduced class-switched memory B cells, increased naive B cells) in humans.
5. **Tissue/organism consequence:** B-cell hyperactivity → **hypergammaglobulinemia and autoimmunity** (autoantibody production, lymphoid hyperplasia, GI inflammation, hepatosplenomegaly) coexisting paradoxically with **impaired pathogen clearance** (recurrent respiratory infection) — attributable to concurrent T-cell dysregulation (reduced naive T cells, impaired T-cell proliferation) and disrupted humoral maturation despite B-cell numeric expansion.
6. **Malignancy risk:** Chronic non-canonical NF-κB2 hyperactivation and elevated pro-survival/proliferative signaling (Mcl1, c-Myc, Pim2) create a cell-intrinsic substrate for **B-cell malignant transformation**, mirroring the well-established role of complete/biallelic somatic TRAF3 loss as an oncogenic driver in multiple myeloma and B-cell lymphoma.

### Dominant-negative form (IMD132A)
Rather than simple dosage reduction, mutant TRAF3 protein (e.g., R118W) destabilizes the wild-type protein produced from the normal allele, driving TRAF3 levels far below the 50% haploinsufficiency threshold. This severely impairs **TLR3/TRIF-dependent IFN-β and IL-6 production**, compromising CNS antiviral defense against HSV-1 and predisposing to **herpes simplex encephalitis**; a distinct manifestation involves impaired antimycobacterial TNF-α-dependent responses, predisposing to chronic *M. abscessus* pulmonary infection.

### Cell types and biological processes involved
- **Cell types (CL terms):** B lymphocyte (CL:0000236), plasma cell (CL:0000786), naive B cell (CL:0000788), memory B cell (CL:0000787), CD4+ T cell (CL:0000624), regulatory T cell (CL:0000815), T follicular helper cell (CL:0002038)
- **Biological processes (GO terms):** non-canonical NF-kappaB signal transduction (GO:0038061 / related to GO:0043123 positive regulation of NF-kB), protein K48-linked ubiquitination (GO:0070936), toll-like receptor 3 signaling pathway (GO:0034138), type I interferon production, B cell proliferation (GO:0042100), B cell differentiation, mitochondrial respiration/oxidative phosphorylation

### Molecular profiling
No published transcriptomic (GEO), proteomic, or single-cell datasets specific to human TRAF3-HI patients were identified in this search; the mechanistic dataset is largely built from **B-cell-conditional Traf3 knockout/heterozygous mouse models** (B-Traf3+/−) combined with patient PBMC/B-cell immunophenotyping (flow cytometry, Western blot) rather than omics-scale profiling.

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary — respiratory tract (recurrent infection, bronchiectasis), lymphoid organs (spleen, lymph nodes — lymphadenopathy, splenomegaly), liver (hepatomegaly, possible autoimmune hepatitis-type involvement), gastrointestinal tract (ileitis, pancolitis). CNS involvement (encephalitis) specific to the IMD132A/HSE phenotype.
- **Body systems:** Immune system (primary), respiratory system, hepatobiliary system, gastrointestinal system, and secondarily the central nervous system in the dominant-negative HSE-associated form.
- **Tissue/cell level:** Lymphoid tissue (nodular lymphoid hyperplasia), B-lymphocyte and T-lymphocyte compartments specifically.
- **Subcellular:** Cytoplasmic signalosome complexes (TRAF3-TRAF2-cIAP1/2-NIK) at the plasma membrane/receptor complex; proteasome-mediated degradation machinery.
- **UBERON-relevant sites:** spleen (UBERON:0002106), lymph node (UBERON:0000029), lung (UBERON:0002048), liver (UBERON:0002107), large intestine (UBERON:0000059), ileum (UBERON:0002116).

---

## 8. Temporal Development

- **Onset:** Predominantly childhood for the core immunodeficiency phenotype (recurrent respiratory infections, bronchiectasis by adulthood implies childhood onset); HSE onset also in childhood (IMD132A); *M. abscessus* pulmonary infection described in an adult (51-year-old woman).
- **Progression:** Chronic, apparently progressive in respiratory (structural bronchiectasis) and possibly hepatic/GI domains; not described as episodic overall, though autoimmune flares may be episodic in nature (consistent with other autoimmune-lymphoproliferative PIDs).
- **Course:** Lifelong/chronic — no spontaneous remission described. The 2025 aging data suggest phenotype severity could plausibly worsen with advancing age due to superimposed age-related TRAF3 protein decline, though this has not been formally studied longitudinally in patients.

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; only ~12 patients (9 in the founding cohort + 3 in the follow-up CVID-reanalysis cohort) are documented in the literature reviewed for the haploinsufficiency (IMD132B) form as of this report, plus a small number of additional IMD132A (dominant-negative) cases (HSE and *M. abscessus* presentations). No formal prevalence/incidence estimate exists.
- **Inheritance pattern:** Autosomal dominant for both IMD132A and IMD132B.
- **Penetrance/expressivity:** Variable expressivity is evident — patients within and across families present with differing combinations of infection, autoimmunity, and lymphoproliferation; some previously carried alternate diagnoses (e.g., CVID) before TRAF3 variants were identified via targeted reanalysis, suggesting either incomplete ascertainment of the syndrome's distinctive features or genuinely variable presentation.
- **De novo occurrence:** The prototypic IMD132A R118W variant arose **de novo**.
- **Founder effects/consanguinity/carrier frequency:** Not reported; not applicable given autosomal dominant, non-recessive inheritance.
- **Sex ratio:** Not explicitly reported as skewed in available sources (index patients described include both male and female).

---

## 10. Diagnostics

- **Genetic testing:** Diagnosis is established via **NGS-based inborn-errors-of-immunity gene panels or exome/genome sequencing** with TRAF3-targeted variant calling/reanalysis — explicitly how the 2024 cohort was ascertained (reanalysis of 800 existing IEI sequencing datasets). Given the gene's association with CVID-like presentations, **TRAF3 should be considered in any CVID/hypogammaglobulinemia gene panel**, and clinicians are encouraged to revisit "CVID of unknown cause" cohorts for TRAF3 variants.
- **Immunophenotyping (flow cytometry):** CD4+ T-cell count and naive/memory subsets, Treg and Tfh proportions, B-cell maturation subsets (naive vs. class-switched memory), immunoglobulin levels (IgG/IgA/IgM), autoantibody panels.
- **Functional assays:** TRAF3 protein quantification (Western blot) in PBMCs/B cells to confirm haploinsufficient (~50%) vs. dominant-negative (<50%, e.g. ~17.5%) reduction; TLR3-stimulated IFN-β/IL-6 production assays (fibroblast-based, as used in the original HSE study) for suspected IMD132A.
- **Imaging:** Chest CT for bronchiectasis assessment; abdominal imaging for hepatosplenomegaly/lymphadenopathy.
- **Endoscopy/biopsy:** For GI inflammation (ileitis, pancolitis) as seen in the index patient.
- **Differential diagnosis:** Other NF-κB-pathway primary immunodeficiencies — NFKB1 haploinsufficiency (CVID-like), NFKB2 deficiency, CTLA4 haploinsufficiency, TNFAIP3/A20 haploinsufficiency (HA20), LRBA deficiency — all share overlapping combined immunodeficiency-with-autoimmunity phenotypes and should be distinguished by targeted gene panel/exome sequencing. Also distinguish idiopathic CVID (no identified monogenic cause) from monogenic TRAF3-HI, since a subset of "CVID" patients are now understood to actually have TRAF3-HI.
- **Screening:** No population/newborn screening applicable given rarity; cascade testing of relatives is appropriate given autosomal dominant inheritance and variable expressivity.

---

## 11. Outcome/Prognosis

- **Malignancy risk:** The founding *Science Immunology* study explicitly reports an **increased risk of B-cell malignancy** among TRAF3-HI patients, mechanistically consistent with TRAF3's established tumor-suppressor role — chronic non-canonical NF-κB2/pro-survival protein (Mcl1, Pim2, c-Myc) hyperactivation in the heterozygous state provides a plausible intermediate step toward the complete/biallelic TRAF3 loss recurrently observed as a somatic driver in multiple myeloma and B-cell lymphoma. Comparative oncology data reinforce this: germline TRAF3 mutations were found in **17.5% (11/63)** of canine B-cell lymphoma cases, with 14.2% lacking any additional somatic TRAF3 mutation, suggesting inherited TRAF3 variants alone can predispose to lymphoma (PMID 25468570).
- **Structural/functional sequelae:** Bronchiectasis represents a documented, presumably irreversible structural complication of recurrent respiratory infection.
- **Mortality/survival:** No formal survival statistics are available given the small, recently described cohort; the historical HSE-associated case responded to antiviral treatment, while the *M. abscessus*-associated case was treatment-resistant, illustrating variable infection-related morbidity.
- **Complications:** Chronic GI inflammation (ileitis, pancolitis), hepatosplenomegaly, autoimmune manifestations, and immunoglobulin abnormalities requiring ongoing management.
- **Prognostic factors:** No validated biomarkers for stratifying disease severity/malignancy risk are yet established; age-related TRAF3 decline (independent of the germline variant) is a biologically plausible but clinically unvalidated risk-modifying factor.

---

## 12. Treatment

No disease-specific, TRAF3-HI-tailored treatment guideline yet exists (reflecting its very recent characterization); management is inferred to follow the general combined-immunodeficiency-with-autoimmunity paradigm used for related NF-κB-pathway PIDs (e.g., CVID, NFKB1-HI, CTLA4-HI):

- **Immunoglobulin replacement therapy (IVIG/SCIG):** Documented directly — the 2024 cohort's 3 patients, having previously been diagnosed with CVID, were receiving immunoglobulin replacement therapy for hypogammaglobulinemia and recurrent infections (NCIT:C15986 Pharmacotherapy category; specific product NCIT terms would apply to the IVIG/SCIG agent used).
- **Antibiotic prophylaxis/treatment:** Implied standard-of-care for recurrent bacterial sinopulmonary infection and bronchiectasis management, and specifically required (with resistance noted) for the *M. abscessus* pulmonary infection case.
- **Antiviral therapy:** Standard HSV antiviral treatment (e.g., acyclovir) for herpes simplex encephalitis in the IMD132A phenotype; the reported HSE case "responded to treatment."
- **Immunomodulation for autoimmune manifestations:** Not explicitly reported for TRAF3-HI patients in the sources retrieved, but by analogy to closely related NF-κB-pathway PIDs (e.g., CTLA4 haploinsufficiency, ALPS), agents such as **sirolimus** (mTOR inhibitor, effective for refractory autoimmune cytopenias/lymphoproliferation in related PIDs) and **rituximab** (anti-CD20, B-cell depletion) represent plausible off-label options for autoimmune cytopenia/lymphoproliferation, though no TRAF3-HI-specific outcome data were found.
- **Targeted/experimental therapeutics:** Given TRAF3's role upstream of NF-κB2/NIK, **NIK inhibitors** or other non-canonical NF-κB pathway modulators represent a mechanistically rational but currently unvalidated therapeutic avenue; a related mouse study found **Syk inhibition** limited autoimmunity and abnormal B-cell phenotype/function in B-cell-specific TRAF3-deficient mice (J Immunol, academic.oup.com/jimmunol article), suggesting Syk-pathway targeting as another candidate strategy warranting translational investigation.
- **Malignancy surveillance:** Given the demonstrated B-cell malignancy risk, ongoing hematologic/oncologic surveillance is a reasonable clinical inference, though no formal surveillance protocol has been published.
- **No gene therapy, cell therapy, or disease-specific clinical trials** (ClinicalTrials.gov) were identified for TRAF3-HI specifically.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (germline monogenic disease); **genetic counseling** for affected families is appropriate given autosomal dominant inheritance and variable expressivity, including consideration of cascade testing in relatives and reproductive counseling.
- **Secondary prevention:** Early genetic diagnosis (via IEI panel/exome reanalysis) allows earlier initiation of immunoglobulin replacement and infection-prevention measures, potentially forestalling bronchiectasis and other structural sequelae; routine vaccination status optimization (noting that live vaccines may be contraindicated depending on the degree of immunodeficiency, as in other combined immunodeficiencies) is a standard PID consideration though not TRAF3-HI-specific in the literature reviewed.
- **Tertiary prevention:** Malignancy surveillance (as above) to enable early detection of B-cell lymphoproliferative transformation.
- No vaccine, chemoprophylactic, or public-health-level prevention strategy specific to TRAF3-HI exists, consistent with its status as an ultra-rare monogenic disorder rather than an infectious or environmentally-driven condition.

---

## 14. Other Species / Natural Disease

- **Dog (*Canis lupus familiaris*):** The most clinically relevant comparative model — **germline and somatic TRAF3 inactivation is a recurrent, naturally occurring feature of canine B-cell lymphoma (cBCL)**. Somatic TRAF3 mutations (frameshift + truncating SNVs) were found in ~30.2% of a cBCL cohort, and **germline TRAF3 mutations in 17.5% (11/63)** of cases, with 14.2% of cases carrying only a germline (no somatic) TRAF3 mutation — directly supporting the concept that a single inherited TRAF3 LOF allele predisposes to B-cell malignancy, paralleling concerns for human TRAF3-HI patients (PMID 25468570, Blood). This makes naturally occurring canine BCL a valuable **spontaneous large-animal comparative model** for the human malignancy-risk arm of TRAF3-HI.
- **Taxonomy:** *Canis lupus familiaris* (NCBITaxon:9615).
- **Orthology:** TRAF3 is highly conserved across mammals; canine TRAF3 shares the same NF-κB-regulatory function as human TRAF3.
- **Zoonotic potential:** Not applicable — this is a non-communicable, germline genetic condition, not a transmissible disease.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*), full-body *Traf3* knockout:** Per MGI (marker MGI:108041), **homozygous Traf3-null mice show progressive runting, hypoglycemia, and depletion of peripheral white blood cells, dying by ~10 days of age**; lethally irradiated mice reconstituted with mutant hematopoietic cells show impaired T-dependent antibody responses — establishing TRAF3 as essential for immune and metabolic homeostasis, and explaining why disease-causing human variants are invariably heterozygous (complete biallelic loss is likely embryonically/perinatally incompatible with survival, analogous to the mouse).
- **Mouse, B-cell-conditional heterozygous knockout (B-Traf3+/−):** The key genetic model directly modeling human haploinsufficiency (Hornick et al., 2025, PNAS). Findings: 40–50% reduction of TRAF3 protein/mRNA in splenic B cells; dose-intermediate increases in spleen weight, splenic B-cell number, NF-κB2 (p52) activation, plasma-cell numbers (splenic, not marrow), and pro-survival protein expression (Mcl1, Pim2, c-Myc, Hxk2) relative to wild-type and full knockout; **prolonged in vitro B-cell survival** through day 3 (dying by day 5); **elevated phospho-STAT3(Y705)** after IL-6 stimulation.
- **Mouse, B-cell-specific complete Traf3 knockout:** Used in earlier mechanistic work (e.g., leu2011309, Leukemia journal) showing that complete B-lineage Traf3 deletion drives spontaneous B-lymphoma development in mice — modeling the malignancy end of the phenotypic spectrum; Syk inhibition was shown to limit the resulting autoimmunity and abnormal B-cell phenotype in this model.
- **Aged wild-type mice:** Used as a model of physiological TRAF3 decline — aged (≥16 months) vs. young (≤3 months) mouse B cells show reduced TRAF3 protein (mirroring the human aging data), reversible acutely by proteasome inhibition (bortezomib), directly linking normal aging biology to the same pathway disrupted genetically in TRAF3-HI.
- **Model limitations:** Full knockout mice die neonatally and cannot model the chronic, decades-long human disease course; heterozygous B-cell-conditional mice best model the dosage-sensitive human phenotype but do not capture T-cell dysregulation, GI inflammation, or CNS (HSE-susceptibility) aspects of the human syndrome, which currently lack dedicated animal models. No zebrafish, *Drosophila*, *C. elegans*, iPSC, or organoid TRAF3-HI-specific disease models were identified in this search.
- **Resources:** MGI (Traf3 marker MGI:108041; targeted alleles e.g. MGI:3722126 [tm1Bshp], MGI:2135257 [tm1Bal], MGI:3777325 [tm1.1Rbr]); Cyagen commercial Traf3-KO mouse model.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| Causal gene | HGNC:TRAF3 (hgnc: TRAF3), Chromosome 14q32.32 |
| GO Biological Process | non-canonical NF-kB signal transduction, protein K48-linked ubiquitination (GO:0070936), toll-like receptor 3 signaling pathway (GO:0034138), B cell proliferation (GO:0042100) |
| GO Molecular Function | ubiquitin-protein transferase adaptor activity |
| Cell types (CL) | B lymphocyte (CL:0000236), plasma cell (CL:0000786), naive/memory B cell, CD4+ T cell (CL:0000624), regulatory T cell (CL:0000815), Tfh cell (CL:0002038) |
| Phenotypes (HP) | Recurrent respiratory infections (HP:0002205), Bronchiectasis (HP:0002110), Lymphadenopathy (HP:0002716), Hepatosplenomegaly (HP:0001433), Hypergammaglobulinemia (HP:0010702), Hypogammaglobulinemia (HP:0004313), Encephalitis (HP:0002383), Autoimmunity (HP:0002960) |
| Anatomy (UBERON) | Spleen, Lymph node, Lung, Liver, Ileum, Large intestine |
| Treatment (NCIT) | Pharmacotherapy (NCIT:C15986) with therapeutic_agent immunoglobulin; Chemotherapy/anti-infective for M. abscessus/HSV |

---

## Notes on Evidentiary Gaps

- No confirmed **MONDO ID** was identified for this specific entity via search; this should be independently verified in the current Mondo release before curation.
- **Direct primary-source full text** for the founding *Science Immunology* paper (abn3800) and the *Journal of Clinical Immunology* CVID cohort paper (10.1007/s10875-024-01833-3) could not be fetched directly (paywalled/403); the information above for these two papers is drawn from search-result summaries and secondary citations rather than verified direct quotes from the primary text. **Exact-quote snippets for dismech evidence items should be re-verified against the primary PMID/DOI sources (or PMC full text if available) before being entered into evidence blocks**, per the project's evidence-integrity requirements.
- Quantitative epidemiological data (prevalence/incidence), formal quality-of-life measures, and a validated diagnostic/treatment algorithm are not yet available in the literature, consistent with this being a very recently characterized (2022–2024), ultra-rare monogenic disorder.

---

**Sources:**
- [Human TRAF3 Adaptor Molecule Deficiency Leads to Impaired Toll-like Receptor 3 Response and Susceptibility to Herpes Simplex Encephalitis (PubMed, PMID 20832341)](https://pubmed.ncbi.nlm.nih.gov/20832341/)
- [Human TRAF3 Adaptor Molecule Deficiency... (Immunity/Cell.com full text)](https://www.cell.com/immunity/fulltext/S1074-7613(10)00319-5)
- [Immunodeficiency, autoimmunity, and increased risk of B cell malignancy in humans with TRAF3 mutations (Science Immunology, abn3800)](https://www.science.org/doi/10.1126/sciimmunol.abn3800)
- [Heterozygous Predicted Loss-of-function Variants of TRAF3 in Patients with Common Variable Immunodeficiency (J Clin Immunol, PMID 39579173)](https://link.springer.com/article/10.1007/s10875-024-01833-3)
- [Reduction of TRAF3 by heterozygosity or aging impacts B cell function (PNAS, PMID 40773231)](https://www.pnas.org/doi/10.1073/pnas.2507217122)
- [Reduction of TRAF3 by heterozygosity or aging impacts B cell function (PMC free full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12358898/)
- [OMIM #621096 — IMMUNODEFICIENCY 132B; IMD132B](https://omim.org/entry/621096)
- [OMIM #614849 — IMMUNODEFICIENCY 132A; IMD132A](https://www.omim.org/entry/614849)
- [OMIM *601896 — TNF RECEPTOR-ASSOCIATED FACTOR 3; TRAF3](https://www.omim.org/entry/601896)
- [Dominant Negative TRAF3 Variant With Recurrent Mycobacterium abscessus Infection and Bronchiectasis (Open Forum Infectious Diseases, PMID 36004314)](https://academic.oup.com/ofid/article/9/8/ofac379/6654828)
- [Genetic inactivation of TRAF3 in canine and human B-cell lymphoma (Blood, PMID 25468570)](https://ashpublications.org/blood/article/125/6/999/34100/Genetic-inactivation-of-TRAF3-in-canine-and-human)
- [Specific deletion of TRAF3 in B lymphocytes leads to B-lymphoma development in mice (Leukemia)](https://www.nature.com/articles/leu2011309)
- [TRAF3: A novel regulator of mitochondrial physiology and metabolic pathways in B lymphocytes (Frontiers in Oncology, PMC9911533)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9911533/)
- [Syk inhibition limits autoimmunity and abnormal B cell phenotype and function in mice with B cell-specific TRAF3 deficiency (Journal of Immunology)](https://academic.oup.com/jimmunol/article/215/4/vkag049/8661558?searchresult=1)
- [Traf3 MGI Mouse Gene Detail — MGI:108041](https://www.informatics.jax.org/marker/MGI:108041)
- [TRAF3 Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=TRAF3)
- [TNF receptor (TNFR)-associated factor (TRAF) 3 serves as an inhibitor of TRAF2/5-mediated activation of the noncanonical NF-κB pathway (PNAS)](https://www.pnas.org/doi/10.1073/pnas.0500187102)
- [Molecular basis for CD40 signaling mediated by TRAF3 (PNAS)](https://www.pnas.org/content/97/19/10395.long)
- [Immunodeficiency 132b — MalaCards](https://www.malacards.org/card/immunodeficiency_132b)