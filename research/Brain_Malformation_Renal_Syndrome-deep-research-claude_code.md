---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: true
start_time: '2026-10-28T20:53:17.384036'
end_time: '2026-10-28T20:53:17.389908'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Brain Malformation Renal Syndrome
  mondo_id: MONDO:0975799
  category: Mendelian
  causal_genes: EXOC3L2
  omim_id: not recorded
  synonyms: not recorded
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
  web_search_requests: 9
  num_turns: 40
  total_cost_usd: 3.1416248000000007
  session_id: ba9c45e4-83a0-5de4-8ae1-3ac1f0ec68ec
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 5
citation_count: 16
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 9
  validator_version: 0.4.0
term_validation:
  total_terms: 41
  verified: 38
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.026
  labels_checked: 3
  labels_matching: 2
  labels_variant: 1
  unresolved_terms:
  - RO:0004003
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brain Malformation Renal Syndrome
- **MONDO ID:** MONDO:0975799 (if available)
- **Causal gene(s):** EXOC3L2
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Brain Malformation Renal Syndrome** covering all of the
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

I'm still gathering sources: I've confirmed the founding EXOC3L2 paper (Shalata 2019) and the OMIM number, and I'm now looking for any later case reports and abstract text.

I'm pulling the 2016 ciliopathy cohort paper (Shaheen et al.) for its EXOC3L2 family details.

I'm now reading the 2022 fetal exome series (Smogavec) and the mouse knockout paper (Watanabe) for EXOC3L2 details.

Next I'm checking the MONDO record for MONDO:0975799 in OLS so the identifiers are confirmed.

# Brain Malformation Renal Syndrome (BMRS; EXOC3L2-related): Research Report

**Target:** Brain malformation renal syndrome, MONDO:0975799. The causal gene is **EXOC3L2** (exocyst complex component 3-like 2; HGNC:30162, written `hgnc:30162` in dismech; NCBI Gene 90332; OMIM gene *616927; chromosome 19q13.32; reference transcript NM_138568.3). Every identifier in this report points to the same disease: MONDO:0975799 cross-references OMIM #620943 and the EXOC3L2-based KEGG entry H02833. I found no other gene with a similar disease name.

> **Evidence quality.** BMRS is an **ultra-rare, recently defined** autosomal recessive disorder. All published human data come from about 5–6 affected individuals or fetuses in 4–5 families, reported in four papers (2016–2022). There is no GeneReviews chapter, no ClinGen gene–disease validity curation, no natural-history study, no treatment trial and no prevalence estimate. Many sections below are therefore "not available". Inferences are labelled as inferences.
>
> **Verify all quotes.** The PubMed and NCBI interfaces I used summarise abstracts rather than return verbatim text. Quoted phrases below are fragments returned by those tools. Re-derive every snippet with `just fetch-reference PMID:…` before it goes into KB evidence.

---

## 1. Disease Information

**Overview.** BMRS is a recessive multisystem developmental disorder. Its main features are a **hindbrain malformation** (Dandy-Walker malformation (DWM), cerebellar vermis hypoplasia, sometimes encephalocele) and **renal dysplasia** (enlarged or hyperechogenic dysplastic kidneys). One surviving child also had **bone marrow failure**, plus white matter abnormalities, developmental delay and pituitary hypoplasia (panhypopituitarism). Most reported cases ended in fetal loss, termination or early neonatal death. That prenatal phenotype overlaps Meckel–Gruber syndrome (MKS), so EXOC3L2 is often grouped with ciliopathy genes.

The founding paper (Shalata et al. 2019, *J Med Genet* 56:340–346, **PMID:30327448**, DOI 10.1136/jmedgenet-2018-105421) concluded that biallelic EXOC3L2 mutations cause a "novel syndrome" affecting "hindbrain development, kidney and possibly the bone marrow". The title is "Biallelic mutations in EXOC3L2 cause a novel syndrome that affects the brain, kidney and blood".

**Identifiers**

| Resource | ID | Source / note |
|---|---|---|
| MONDO | MONDO:0975799 "brain malformation renal syndrome" | OLS4. No definition or synonyms yet. Parents: MONDO:0002254 *syndromic disease* and MONDO:0003847 *hereditary disease*. Carries an RO:0004003 germline-mutation relation. |
| OMIM (phenotype) | #620943, BMRS | KEGG H02833; Genomics England PanelApp (phenotype renamed to this on 2 Oct 2024) |
| OMIM (gene) | *616927 EXOC3L2 | PanelApp, NCBI Gene |
| MedGen / UMLS | 1874920 / C5975390 | MONDO xrefs |
| KEGG DISEASE | H02833 | KEGG |
| ICD-11 | LD20.0Y (other specified syndromes with CNS anomalies as a major feature) | KEGG |
| Orphanet, MeSH | None found | — |
| GenCC | PanelApp Australia: **Strong**, AR, for MONDO:0975799 / OMIM:620943 (evaluated 2025-01-17) | thegencc.org |

**Synonyms:** BMRS. Before OMIM named it, PanelApp used the descriptive label "Dandy-Walker malformation; renal dysplasia; bone marrow failure". Some panels call it "EXOC3L2-related ciliopathy" or a "Meckel–Gruber-like phenotype". GeneCards maps some EXOC3L2 variants to "Meckel syndrome, type 1"; that is a misattribution and should not be used as a synonym.

**Data provenance:** individual patient and fetal case reports (clinical exams, prenatal ultrasound and MRI, autopsy, exome sequencing), plus aggregated resources (OMIM, PanelApp, GenCC, KEGG). There are no EHR-derived data.

## 2. Etiology

- **Cause:** germline biallelic (homozygous in every reported case) loss-of-function or hypomorphic variants in EXOC3L2.
- **Genetic risk factors:** parental consanguinity in every reported family. Family 1 in Shalata et al. was described as consanguineous Arab-Israeli (from the OMIM *616927 summary, seen only as a search snippet). The Smogavec et al. 2022 family was consanguineous. There is no known founder allele, modifier gene or GWAS signal for this phenotype.
  - Common EXOC3L2-locus SNPs such as rs597668 have been studied for late-onset Alzheimer disease (e.g., PMID:20460622, 23663385). That signal sits in the 19q13 *APOE*/*BLOC1S3* region and is **unrelated to BMRS**. Do not curate it as a risk factor.
- **Environmental risk factors:** none known (not applicable).
- **Protective factors:** none known.
- **Gene–environment interactions:** none known.

## 3. Phenotypes

The case series is very small, so frequencies below are counts of reported individuals, not percentages.

**Reported individuals**

| ID | Source | Genotype (homozygous) | Outcome |
|---|---|---|---|
| A | Shaheen et al. 2016, *Genome Biol* 17:242, **PMID:27894351** | c.398dupC, p.Leu134Thrfs\*25 (frameshift) | MKS-like: occipital encephalocele, early postnatal death. No polydactyly or cystic kidneys, per the Halim 2023 review (PMID:37085629). PanelApp's summary of the same family says "severe posterior fossa malformation with kidney enlargement". |
| B | Shamseldin et al. 2018, *Genet Med* 20:420–427, **PMID:28749478** (molecular autopsy, 44 families) | Biallelic EXOC3L2 variant; details not retrieved | Fetus with MKS-like phenotype. EXOC3L2 proposed as a candidate gene. |
| C1–C3 | Shalata et al. 2019, Family 1 | c.122T>A, p.Leu41Gln (missense at a highly conserved residue) | Three fetuses with severe DWM, seen on prenatal ultrasound and confirmed at autopsy |
| D | Shalata et al. 2019, Family 2 | p.Arg72\* (nonsense; no detectable protein, reduced EXOC3L2 in fibroblasts) | Liveborn child: white matter abnormalities, developmental delay, pituitary hypoplasia, severe renal dysplasia, bone marrow failure |
| E | Smogavec et al. 2022, *Eur J Hum Genet* 30:428–438, **PMID:34974531** (case 22) | c.(90+1_91-1)_(404+1_405-1)del, exons 3–5 deleted (ACMG class 5, PVS1; ClinVar SCV001519072) | Prenatal scan: cerebellar vermis hypoplasia, enlarged hyperechogenic kidneys, lung hypoplasia, oligohydramnios. Two affected siblings by history: one terminated at 22 weeks for renal dysgenesis; one born at 25 weeks with DWM and encephalocele after anhydramnios, who died shortly after birth. |

**Phenotypes with suggested HPO terms.** All CURIEs below are **unverified leads**. Confirm each with `runoak` or `cache/hp/terms.csv` before binding.

| Phenotype | Type | Onset | Reported in | Suggested HPO (verify) |
|---|---|---|---|---|
| Dandy-Walker malformation | Structural sign | Prenatal | C1–C3; E sibling | HP:0001305 Dandy-Walker malformation |
| Cerebellar vermis hypoplasia / posterior fossa malformation | Sign | Prenatal | A, E | HP:0001320 Cerebellar vermis hypoplasia |
| Occipital encephalocele | Sign | Prenatal | A; E sibling | HP:0002085 Occipital encephalocele |
| Hydrocephalus | Sign | Prenatal/neonatal | OMIM synopsis (per MalaCards) | HP:0000238 Hydrocephalus |
| Cerebral white matter abnormality | Imaging | Infancy | D | HP:0002500 Abnormality of the cerebral white matter |
| Developmental delay | Neurodevelopmental | Infancy | D | HP:0001263 Global developmental delay |
| Pituitary hypoplasia / panhypopituitarism | Endocrine | Infancy | D | HP:0010626 Anterior pituitary hypoplasia; HP:0000871 Panhypopituitarism |
| Renal dysplasia / dysgenesis | Structural | Prenatal | D; E and sibling; possibly A | HP:0000110 Renal dysplasia |
| Enlarged, hyperechogenic kidneys | Prenatal imaging | Prenatal | E; OMIM synopsis | HP:0004719 Hyperechogenic kidneys; HP:0000105 Enlarged kidney |
| Oligohydramnios / anhydramnios | Pregnancy finding (likely from fetal renal failure) | Prenatal | E and sibling | HP:0001562 Oligohydramnios |
| Pulmonary hypoplasia | Sign (likely downstream of oligohydramnios) | Prenatal | E | HP:0002089 Pulmonary hypoplasia |
| Bone marrow failure | Laboratory/hematologic | Childhood | D only; the authors hedge it as "possibly" | HP:0005528 Bone marrow hypocellularity, or a pancytopenia term (choose after reading the full text) |
| Fetal or neonatal lethality | Outcome | Prenatal/neonatal | A, B, C1–C3, E siblings | Stillbirth / neonatal death terms (verify) |

- **Severity and progression:** severe and congenital in all cases. Progression cannot be assessed: there is one survivor, with limited follow-up.
- **Quality of life:** no data. The surviving child's renal dysplasia, marrow failure and hypopituitarism imply heavy morbidity (inferred).

## 4. Genetic / Molecular Information

**Gene.** EXOC3L2 is an exocyst-like paralog of EXOC3 (SEC6), alongside EXOC3L1, EXOC3L3 (M-Sec) and EXOC3L4.
- Tagged EXOC3L2 **co-precipitates with EXOC4 (SEC8)** and partly colocalises with EXOC4 and EXOC7 (Barkefors et al. 2011, *J Biol Chem* 286:24189, **PMID:21566143**; tool-extracted phrase: "Myc-tagged EXOC3L2 co-precipitates with the exocyst protein EXOC4").
- KEGG and Shalata et al. describe it as a component of the exocyst complex involved in tethering and trafficking post-Golgi vesicles to the plasma membrane.
- A murine splice isoform lacking a domain, Exoc3l2a, has been described (O'Callaghan et al. 2018, *PLoS One*, **PMID:30086153**).

**Pathogenic variants (all homozygous, all germline)**

| Variant | Type | Family | Classification |
|---|---|---|---|
| c.398dupC, p.Leu134Thrfs\*25 | Frameshift, predicted LoF | Shaheen 2016 | Candidate; LoF |
| c.122T>A, p.Leu41Gln | Missense, conserved residue | Shalata 2019, Family 1 | Likely pathogenic, based on segregation in 3 fetuses |
| p.Arg72\* | Nonsense; protein absent or markedly reduced in fibroblasts | Shalata 2019, Family 2 | Pathogenic (LoF) |
| Exons 3–5 deletion | Intragenic CNV (frameshift) | Smogavec 2022 | ACMG class 5 (PVS1) |
| Unspecified biallelic variant | — | Shamseldin 2018 | Candidate |

- **Functional consequence:** loss of function (amorphic or hypomorphic). No gain-of-function or dominant-negative mechanism has been proposed.
- **Allele frequencies:** not retrieved for these alleles. Check gnomAD; private variants in consanguineous families are expected.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported.
- **Evidence grading:**
  - PanelApp Australia (ciliopathies, CAKUT): Green; submitted to GenCC as **Strong**.
  - Genomics England: Amber on CAKUT, tagged "watchlist" awaiting more cases; Green on the Fetal anomalies panel after three unrelated fetal cases (PMIDs 27894351, 28749478, 30327448).
  - **ClinGen: no curation found.** A `gene_disease_validity` entry may copy the GenCC/PanelApp Australia "Strong" tier with `classified_by` the matching source value. Do not assign a tier independently.

## 5. Environmental Information

Not applicable. No environmental, lifestyle or infectious factors are known.

## 6. Mechanism / Pathophysiology

**Ordered causal chain.** Steps 4–6 are largely **inferred**. No patient-tissue cilia study or human-cell trafficking study of these variants has been published.

1. Biallelic EXOC3L2 LoF variants (frameshift, nonsense, exon deletion; missense p.Leu41Gln assumed hypomorphic) **lead to** absent or markedly reduced EXOC3L2 protein. This is *demonstrated* for p.Arg72\* in patient fibroblasts (Shalata 2019).
2. Loss of EXOC3L2 **results in** impaired exocyst-dependent vesicle tethering and delivery to the plasma membrane. This is *inferred*: binding to EXOC4 and colocalisation with EXOC7 were shown in endothelial cells (PMID:21566143), but trafficking was not measured in patient cells.
3. **Branch A, vascular/endothelial (demonstrated in vitro and in mice):**
   - EXOC3L2 silencing **reduces VEGFR2 (KDR) phosphorylation and VEGFA-directed endothelial migration** (PMID:21566143; tool-extracted phrase: "exoc3l2 silencing inhibits VEGF receptor 2 phosphorylation and VEGFA-directed migration").
   - Exoc3l2 knockout mice **die in utero** with extensive hemorrhage. Knockout via Tie2-Cre (hematopoietic plus endothelial lineages) reproduces the hemorrhage, ventricular septal defects, myocardial hypoplasia, and telencephalic and cerebellar anomalies (Watanabe et al. 2022, *Life* 12:1730, **PMID:36362885**).
   - This suggests embryonic vascular insufficiency may contribute to the hindbrain malformation (*hypothesis*).
4. **Branch B, primary cilia (inferred, by analogy with other exocyst genes):**
   - Exocyst subunits deliver ciliary membrane cargo. Patient cells with EXOC2 variants mislocalise Arl13b, and patient cells with EXOC6B variants have short cilia (reviewed in Halim et al. 2023, *Hum Genet* 142:1263, **PMID:37085629**).
   - Defective ciliogenesis in cerebellar progenitors and renal tubular epithelium would **lead to** a ciliopathy-like phenotype (MKS-like). Shaheen et al. classed EXOC3L2 as a "novel candidate ciliopathy gene", but **no EXOC3L2 cilia assay exists**.
5. In the developing hindbrain, defective trafficking and/or vascular support **results in** cerebellar vermis hypoplasia, a cystic fourth ventricle (DWM) and, in some cases, encephalocele.
6. In the developing kidney, defective epithelial morphogenesis (possibly via cilia) **results in** renal dysplasia with enlarged hyperechogenic kidneys. This **leads to** fetal anuria, then oligohydramnios, then pulmonary hypoplasia (the Potter sequence), then perinatal death.
7. **Branch C, hematopoietic (one patient, mechanism unknown):** loss of EXOC3L2 in hematopoietic or niche cells may **lead to** bone marrow failure. This is consistent with the mouse Tie2-Cre (hemato-endothelial) data, but unproven. Halim et al. state that the marrow failure mechanism needs further study.
8. **Pituitary hypoplasia and white matter disease** (one patient): mechanism unknown, consistent with a broad midline/CNS developmental defect.

**Suggested GO terms (verify):**
- GO:0000145 exocyst (cellular component)
- GO:0006887 exocytosis
- GO:0006893 Golgi to plasma membrane transport
- GO:0060271 cilium assembly (inferred only)
- GO:0048010 vascular endothelial growth factor receptor signaling pathway
- GO:0043542 endothelial cell migration
- GO:0021549 cerebellum development
- GO:0001822 kidney development
- GO:0030097 hemopoiesis

**Suggested CL terms (verify):**
- CL:0000115 endothelial cell
- CL:0000037 hematopoietic stem cell
- A renal epithelial cell term
- A cerebellar granule-cell precursor term, if supported

**Molecular profiling, single-cell, omics and CRISPR screens:** none published for this disease.

## 7. Anatomical Structures Affected

- **Primary:** cerebellum and vermis, fourth ventricle and posterior fossa (UBERON:0002037 cerebellum); kidney (UBERON:0002113).
- **Secondary:** lung (hypoplasia secondary to oligohydramnios); bone marrow (UBERON:0002371); pituitary gland (UBERON:0000007); cerebral white matter.
- **Systems:** nervous, urinary, hematopoietic, endocrine. In mice also cardiovascular; no human cardiac finding has been reported.
- **Subcellular:** exocyst / post-Golgi vesicles and plasma membrane; the primary cilium is hypothesised.
- **Laterality:** renal involvement bilateral (enlarged kidneys); brain findings midline.

UBERON IDs above should also be verified before binding.

## 8. Temporal Development

- **Onset:** congenital and prenatal. Detectable on second-trimester ultrasound (about 22–24 weeks or later; Smogavec reports both 24 weeks and 30+5 weeks for the same case).
- **Course:** usually lethal in the fetal or neonatal period. One liveborn child survived to clinical work-up in childhood. Staging and progression rates are not defined.
- **Critical period:** embryonic hindbrain and nephron development. In mice, Exoc3l2 is expressed in endothelium at E8.5, and knockouts die by about E15.5–E17.5.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007; PanelApp: "BIALLELIC, autosomal or pseudoautosomal"). Heterozygous parents were unaffected.
- **Penetrance and expressivity:** complete within families as far as reported. Expressivity varies between families (DWM-only fetuses versus a renal-plus-marrow phenotype in a survivor). Whether that variation tracks allele severity is unknown.
- **Consanguinity:** present in all families with known pedigrees.
- **Populations:** Arab-Israeli (Shalata Family 1; secondary source); Saudi cohorts (Shaheen, Shamseldin); a consanguineous family in a German fetal cohort (Smogavec).
- **Founder effect, carrier frequency, sex ratio, prevalence and incidence:** unknown. Fewer than 10 cases have been published (CASES_IN_LITERATURE; prevalence class ULTRA_RARE or NOT_YET_DOCUMENTED).
- **Anticipation and germline mosaicism:** not reported.

## 10. Diagnostics

- **Prenatal imaging:** fetal ultrasound and MRI showing DWM or vermis hypoplasia (e.g., brainstem–vermis angle 38.2° in Smogavec case 22), encephalocele, enlarged hyperechogenic kidneys and oligohydramnios.
- **Postnatal:**
  - Brain MRI for white matter and posterior fossa.
  - Renal ultrasound and renal function.
  - Complete blood count and bone marrow examination for marrow failure.
  - Pituitary hormone testing.
- **Autopsy:** confirmed DWM in Shalata Family 1.
- **Genetic testing:**
  - Trio exome or genome sequencing is the effective approach.
  - **CNV calling from exome data is essential.** The exons 3–5 deletion was found only by CNV analysis and confirmed by qPCR (Smogavec).
  - Smogavec et al. note that gene-panel or OMIM-filtered pipelines would have missed this case, because EXOC3L2 had no OMIM disease at the time.
  - EXOC3L2 is on PanelApp ciliopathy, CAKUT, fetal anomalies and neurological ciliopathy panels.
  - Chromosomal microarray was used in Shalata et al., mainly to exclude other causes.
- **Clinical criteria:** none established.
- **Differential diagnosis:**
  - Meckel–Gruber syndrome (MKS1, TMEM67, CC2D2A and others; usually with polydactyly and cystic kidneys)
  - Joubert syndrome (molar tooth sign)
  - Other DWM syndromes (e.g., FOXC1, ZIC1/ZIC4)
  - Renal-hepatic-pancreatic dysplasia (NPHP3, NEK8)
  - Other exocyst disorders (EXOC2, EXOC7, EXOC8, EXOC6B)
  - Inherited bone marrow failure syndromes (for the survivor phenotype)
- **Screening:** no newborn or population screening. Carrier and prenatal testing are possible once familial variants are known.

## 11. Outcome / Prognosis

- Most reported pregnancies ended in termination, intrauterine death or neonatal death (Shaheen; Shamseldin; Shalata Family 1; Smogavec siblings).
- The one survivor (Shalata Family 2) had severe multisystem morbidity: renal dysplasia, bone marrow failure, hypopituitarism and developmental delay.
- Survival statistics, life expectancy, quality-of-life measures and prognostic biomarkers: **not available**.

## 12. Treatment

There is no disease-specific therapy and no clinical trial. Management is supportive and organ-directed, by analogy with renal dysplasia and marrow failure in general; these are not specific recommendations from the literature. NCIT terms below are taken from the dismech CLAUDE.md list and should still be checked against the enum.

| Intervention | NCIT (verify) | Notes |
|---|---|---|
| Supportive care | NCIT:C15747 | Multidisciplinary |
| Kidney replacement (dialysis or transplant) | NCIT:C15289 Organ Transplantation (for transplant) | No published report in BMRS |
| Hematopoietic cell transplantation for marrow failure | NCIT:C15431 | Theoretical; not reported |
| Hormone replacement for hypopituitarism | NCIT:C15986 Pharmacotherapy + agent | Inferred |
| Genetic counseling | NCIT:C15240 | Recurrence risk 25% |

- **Pharmacogenomics, gene therapy and RNA therapy:** none.
- **Clinical trials:** none registered (checked indirectly through literature searches; no NCT number found).

## 13. Prevention

- **Primary prevention:** genetic counseling of consanguineous couples; carrier testing of relatives once familial variants are known.
- **Secondary prevention:** prenatal diagnosis (chorionic villus sampling or amniocentesis) and preimplantation genetic testing for known familial variants; targeted fetal ultrasound in later pregnancies.
- **Tertiary prevention:** monitoring of renal, hematologic and endocrine function in survivors.
- **Vaccines, prophylaxis and public-health measures:** not applicable.

## 14. Other Species / Natural Disease

No naturally occurring disease has been found (no OMIA record). Orthologs exist in vertebrates, including mouse *Exoc3l2* (MGI). The exocyst complex itself is conserved from yeast onward (Halim 2023). Not zoonotic.

## 15. Model Organisms

**Mouse (Watanabe et al. 2022, PMID:36362885)**

| Allele | Phenotype | Fidelity to human BMRS |
|---|---|---|
| Global knockout (most coding exons deleted) | Embryonic lethal. No knockout pups born. 9/17 knockout embryos dead or hemorrhagic at E15.5. | Partial. Reproduces lethality; brain malformation is only partly modelled. Kidney **not examined**. Human cases show no hemorrhage or cardiac phenotype. |
| Tie2-Cre conditional (exon 3 floxed; Exoc3l2^ΔHEC^) | Lethal around E17.5. Hemorrhage, VSD (2/3), myocardial hypoplasia (2/3), telencephalic and cerebellar anomalies. Neocortical progenitor numbers normal. | Suggests a hemato-endothelial cause for hemorrhage and possibly marrow involvement; this is unresolved. |
| Inducible endothelial deletion (postnatal) | Retinal angiogenesis normal ("dispensable for postnatal angiogenesis in retina") | Not a disease model. |
| GFP knock-in reporter | Expression in about 15% of Pecam1+ endothelial cells at E8.5, plus putative cranial neural crest | Expression mapping only. |

The authors conclude, in a tool-extracted phrase: "Exoc3l2 is essential for cardiovascular and brain development in mice."

**Cellular models:**
- HUVEC and other endothelial cells with EXOC3L2 knockdown: reduced VEGFR2 phosphorylation and VEGFA-directed migration (PMID:21566143).
- Patient fibroblasts with p.Arg72\*: reduced protein (Shalata 2019).

**Gaps:** no zebrafish or *Xenopus* model, no kidney or cilia phenotyping in any model, and no iPSC or organoid model.

**Suggested dismech framing:**
- Mouse knockout: `animal_models` with `PARTIALLY_RECAPITULATES` against the hindbrain malformation node and `fidelity: LOW`.
- `HUMAN_MODEL_MISMATCH` discussion: the mouse vascular/cardiac phenotype is absent in humans, and the renal phenotype is untested in mice.
- `KNOWLEDGE_GAP` discussion: whether EXOC3L2 is required for ciliogenesis.

---

## Curation Notes for the dismech Entry

- **Entry type:** DISEASE. It has its own MONDO and OMIM IDs and a defined gene. The evidence base is thin, and that should be stated plainly.
- **Keep findings separate.** Renal dysplasia, bone marrow failure and pituitary findings rest on 1–2 probands, so each should be its own phenotype row with its own evidence. Do not inflate bone marrow failure into a core feature; the founding authors say "possibly".
- **Read the full text before quoting.** Retrieve the full text of PMID:30327448 (paywalled; not retrieved here) to confirm:
  - the p.Arg72\* cDNA notation;
  - ancestry;
  - details of the marrow and pituitary phenotype;
  - any treatment the survivor received.
- **Cilia link is a hypothesis.** It comes from analogy with other exocyst genes and the MKS-like phenotype. Encode it as an `EMERGING` mechanistic hypothesis, not as an established node.

## Sources

- Shalata A, Lauhasurayotin S, et al. *J Med Genet* 2019;56(5):340–346. PMID:30327448. https://pubmed.ncbi.nlm.nih.gov/30327448/ ; https://cris.biu.ac.il/en/publications/biallelic-mutations-in-exoc3l2-cause-a-novel-syndrome-that-affect/
- Shaheen R, et al. Characterizing the morbid genome of ciliopathies. *Genome Biol* 2016;17:242. PMID:27894351. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5126998/
- Shamseldin HE, et al. Molecular autopsy in maternal–fetal medicine. *Genet Med* 2018;20(4):420–427. PMID:28749478.
- Smogavec M, et al. Singleton exome sequencing of 90 fetuses with ultrasound anomalies. *Eur J Hum Genet* 2022;30:428–438. PMID:34974531. https://www.nature.com/articles/s41431-021-01012-7
- Watanabe C, et al. Exoc3l2 and cardiovascular development in mice. *Life (Basel)* 2022;12:1730. PMID:36362885 (PMC9694714).
- Barkefors I, et al. EXOC3L2 associates with the exocyst and mediates endothelial migration. *J Biol Chem* 2011;286:24189–99. PMID:21566143.
- O'Callaghan P, et al. Exoc3l2a splice variant. *PLoS One* 2018;13:e0201557. PMID:30086153.
- Halim DO, Munson M, Gao FB. The exocyst complex in neurological disorders. *Hum Genet* 2023;142:1263–1270. PMID:37085629. https://pmc.ncbi.nlm.nih.gov/articles/PMC10449956/
- KEGG DISEASE H02833: https://www.kegg.jp/entry/H02833
- OMIM #620943: https://omim.org/entry/620943 ; OMIM *616927: https://www.omim.org/entry/616927 (both seen only through secondary sources; access was blocked)
- Genomics England PanelApp, EXOC3L2: https://panelapp.genomicsengland.co.uk/panels/234/gene/EXOC3L2 ; https://panelapp.genomicsengland.co.uk/panels/478/gene/EXOC3L2/
- PanelApp Australia: https://panelapp-aus.org/panels/84/gene/EXOC3L2/ ; GenCC: https://thegencc.org/genes/HGNC:30162/disease
- MONDO:0975799 via EBI OLS4: https://www.ebi.ac.uk/ols4/
- NCBI Gene 90332: https://www.ncbi.nlm.nih.gov/gene/90332
- MalaCards BMRS: https://www.malacards.org/card/brain_malformation_renal_syndrome
- dismech claim issue #14027: https://github.com/monarch-initiative/dismech/issues/14027

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `RO:0004003` (1 mention) - RO does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15431` (1 mention) - the report calls it "Hematopoietic cell transplantation for marrow failure"; NCIT calls it **Hematopoietic Cell Transplantation**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.