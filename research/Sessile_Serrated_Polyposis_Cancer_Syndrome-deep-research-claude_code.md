---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-26T12:39:44.548471'
end_time: '2026-10-26T12:41:08.828932'
duration_seconds: 84.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Sessile Serrated Polyposis Cancer Syndrome
  mondo_id: MONDO:0014919
  category: Mendelian
  causal_genes: RNF43
  omim_id: not recorded
  synonyms: SSPCS; RNF43-associated serrated polyposis; RNF43-related serrated polyposis
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
  - claude-sonnet-5-5
  web_search_requests: 7
  num_turns: 15
  total_cost_usd: 0.9763971999999997
  session_id: ca0a3bf5-8b0d-56f4-9a62-5060b1ec881b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 11
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMID:22575959
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 6
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sessile Serrated Polyposis Cancer Syndrome
- **MONDO ID:** MONDO:0014919 (if available)
- **Causal gene(s):** RNF43
- **OMIM:** not recorded
- **Synonyms:** SSPCS; RNF43-associated serrated polyposis; RNF43-related serrated polyposis
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Sessile Serrated Polyposis Cancer Syndrome** covering all of the
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

I've finished searching and I'm writing the report now. RNF43 is the causal gene. I confirmed the disease identifiers and ClinGen classification from GenCC. For the literature, I read the 2024 Danish paper in full and only search-result abstracts for the rest. Several PMIDs are not confirmed and are marked as such.

---

# Sessile Serrated Polyposis Cancer Syndrome (SSPCS): research report

**Causal gene: RNF43** (HGNC:18505, 17q22; OMIM gene 612482). Disease: MONDO:0014919, OMIM:617108, autosomal dominant. Date: 2026-10-26.

**Source classes.** Primary literature is labelled "primary". Structured databases (ClinGen via GenCC) are labelled "database". Items I recalled from memory without checking are labelled "unverified lead". Where I found nothing, I say so.

## Key points

- ClinGen classifies the RNF43–SSPCS relationship as **Definitive** (autosomal dominant, evaluated 2022-12-30). The 2024 Danish series calls that framing into question.
- The mechanism is heterozygous loss of function. Loss of RNF43 stabilises Frizzled at the cell surface, so cells respond more strongly to Wnt ligand. This is ligand-dependent Wnt activation, not the ligand-independent activation seen with APC or CTNNB1 mutations.
- Penetrance is uncertain and probably lower than the early family reports implied. RNF43 variants occur in people without serrated polyposis. At least one cohort found no germline variants.
- I found no pediatric presentation. Everything I retrieved concerns adults. The only age I have is a healthy 32-year-old carrier in the Danish series.

## 1. Disease information

**Identifiers** (database; GenCC submission by ClinGen, [thegencc.org](https://thegencc.org/submissions/GENCC_000102-HGNC_18505-MONDO_0014919-HP_0000006-GENCC_100001)):
- Disease title: "Sessile serrated polyposis cancer syndrome (OMIM:617108)"
- MONDO:0014919
- MOI: autosomal dominant (HP:0000006)
- Classification: Definitive, evaluated 12/30/2022

KEGG H02795 and MedGen C4310714 also index the disease (search results only, not opened). I did not check Orphanet, ICD-10/11 or MeSH, and I did not read OMIM or MONDO directly.

**ClinGen notes, as returned by GenCC:**
- The gene was first linked to the syndrome in 2014 (Gala et al., PMID 24512911).
- Seven variants (missense, nonsense, frameshift, splice site) in nine probands across seven publications were scored.
- The proposed mechanism is heterozygous loss of function.
- Experimental evidence from animal models, expression studies and in vitro assays supports the association.

**Lump/split.** SSPCS is the RNF43-defined subset of serrated polyposis syndrome (SPS). SPS is a clinical diagnosis by WHO criteria, and most SPS has no identified germline cause. I would keep SSPCS as a germline entry separate from the somatic serrated-pathway tumours. The source for this boundary is design-decisions §3a as cited in your instructions, not something I verified in this session.

**Synonyms.** The template lists SSPCS and RNF43-associated serrated polyposis. The OMIM wording appears in a LOVD record as "cancer, polyposis, sessile serrated syndrome (SSPCS)" (search result).

## 2. Etiology

- **Cause.** Heterozygous germline loss-of-function variants in RNF43. In the lesions examined, a somatic second hit inactivates the other allele. Yan et al. (Gut 2017;66:1645, DOI 10.1136/gutjnl-2016-311849; PMID not confirmed) found second-hit inactivation in "every serrated polyp, adenoma, and cancer examined" in one germline family (abstract via search summary).
- **Genetic risk factors.** I found no confirmed modifier genes. Gala et al. also reported senescence-pathway gene mutations (ATM, PIF1, TELO2, XAF1, RBL1) in 5 of 20 people with multiple sessile serrated adenomas (OR 3.0, 95% CI 0.9–8.9, P=.04). That is a separate, weak signal from a small cohort (primary, abstract only).
- **Environmental risk factors for SPS in general.** I did not search this. For this syndrome specifically I have no evidence, so I do not assert any.
- **Protective factors and gene–environment interaction.** Nothing found.

## 3. Phenotypes

Phenotype data come from a few small series, so frequencies are unavailable. The HPO terms below are suggestions I did not look up. Verify each CURIE with a lookup before binding.

| Phenotype | Evidence | Suggested HPO term (unverified) |
|---|---|---|
| Multiple sessile serrated polyps | Danish family I: proband had about 42 sessile serrated polyps and 6 tubular adenomas removed (primary, PMID 39546056) | colonic polyposis / serrated polyposis (term to be looked up) |
| Colorectal cancer | Mother, aunt and maternal cousin of the family I proband had CRC (primary, PMID 39546056) | HP:0003003 Colon cancer (from memory) |
| Gastric cancer | One carrier, age 61, with one tubular adenoma (same paper) | HP:0012126 Stomach cancer (from memory) |

- **Onset and progression.** I have no onset data beyond the single 32-year-old carrier. I found no quality-of-life data.
- **Penetrance.** The Danish paper states that "only three out of eight carriers (all relatives) had either serrated polyps or CRC." Only two members of one family met WHO SPS criteria. The authors conclude penetrance "is much lower than previously thought" (primary, PMID 39546056).
- **Pediatric framing.** Not established in what I retrieved. Before treating any minimum surveillance age as supported, check guidelines (ESGE, USMSTF, ACG), which I did not search.

## 4. Genetic and molecular information

- **Variant spectrum.**
  - The Danish series (likely pathogenic under ACMG):
    - Exon 4–9 deletion, (c.375+1_376-1)_(2308+1_2309-1)del.
    - p.(Arg650Ter), c.1948C>T, in two families.
    - p.(Arg337Ter), c.1009C>T, in one family.
  - Taupin et al. 2015: a nonsense variant in the extracellular domain in a severely affected kindred (Hum Genome Var 2:15013; the PMID 27081527 came from a search summary and is a lead).
  - Gala et al. 2014: two probands with nonsense variants. The reported OR of 460 (95% CI 23.1–16384) has a very wide interval, so read it as a weak association.
- **Conflicting cohorts.**
  - Buchanan et al., Gut 2017, a large multinational study, reported no evidence for germline RNF43 variants in SPS (title and finding from a search summary only; PMID unverified).
  - A UK dataset study found RNF43 germline variants in CRC and polyp cases and also in controls, often without multiple polyps or notable family history (search result from the Oxford UK Biobank publication page, not read).
  - Brinch et al. 2024 question whether RNF43 belongs on broad cancer panels, and call it speculative whether variants should instead be treated as "a contributing polygenetic risk factor" (primary).
- **Somatic.** RNF43 mutations were found in 34% of sporadic sessile and traditional serrated adenomas and 0% of hyperplastic polyps (Yan 2017, abstract). In MSI colorectal cancers, mutations were more frequent in the MLH1-methylated group (85%) than the unmethylated group (33.3%).
- **Epigenetic.** I did not research this. The MLH1 methylation association above comes from the somatic data only.

## 6. Mechanism (ordered chain)

1. A germline loss-of-function variant in RNF43 is inherited heterozygous. Truncating variants should trigger nonsense-mediated decay (predicted for Taupin's nonsense variant, per search summary).
2. In an intestinal epithelial cell, the second RNF43 allele is lost somatically. This is shown in a tumour-series from one family (Yan 2017), and I did not read ClinGen's wording on it.
3. RNF43 is a transmembrane E3 ubiquitin ligase. It normally ubiquitinates Frizzled and targets the receptor for degradation. Koo et al., Nature 2012 (DOI 10.1038/nature11308; PMID not confirmed) state: "RNF43 and ZNRF3 reduce Wnt signals by selectively ubiquitinating frizzled receptors, thereby targeting these Wnt receptors for degradation."
4. Without RNF43, Frizzled accumulates and the cell responds to Wnt ligand more strongly. Whether this is sufficient to start a serrated lesion is inferred, not demonstrated for SSPCS.
5. This leads to a sessile serrated lesion. The link between Wnt sensitisation and the serrated morphology is inferred from the somatic data, where RNF43 mutations are enriched in serrated lesions and absent from hyperplastic polyps.
6. Some lesions progress to MSI-high colorectal cancer. The MLH1-methylation association is correlative.

**Branch.** Gala et al. also proposed a role for RNF43 in the ATM–ATR DNA damage response, from knockdown in pancreatic duct cells (abstract only). I treat that as a second, less supported mechanism.

**Mouse and cell models.**
- Koo 2012: simultaneous deletion of Rnf43 and Znrf3 in mouse intestinal epithelium induces "rapidly growing adenomas." This is a double knockout, so it does not model the human single-gene syndrome. The paper reports adenomas, not serrated lesions, so the model captures the Wnt mechanism but not the serrated phenotype.
- R-spondin binds ZNRF3 and recruits LGR4, which clears ZNRF3 from the membrane (PMID 22575959, from a search URL, abstract not read). RSPO fusions and RNF43 loss therefore have a similar effect.
- Jiang et al., PNAS 2013 (PMID unverified): in 39 pancreatic cancer lines, all LGK974-sensitive lines carried inactivating RNF43 mutations. A review notes the RNF43 R519X variant remained unaffected by PORCN inhibitors.

**Suggested ontology terms** (from memory, not looked up): GO "negative regulation of Wnt signaling pathway"; GO protein ubiquitination; CL intestinal crypt stem cell of colon (find the exact CURIE); UBERON colon, with emphasis on the proximal colon.

## 7. Anatomical structures

The colon is the primary organ, and the proximal colon is where WHO criteria place the lesions ("proximal to the sigmoid colon," per the search summary). Stomach involvement was seen in one carrier (gastric cancer at 61). Rectal and extracolonic involvement are not characterised.

## 8–9. Temporal development, inheritance, population

- **Inheritance.** Autosomal dominant, per ClinGen. Penetrance is low and variable, per the Danish series.
- **Founder effects.** I found none, though p.(Arg650Ter) in two Danish families may be worth checking against gnomAD (not done).
- **Prevalence.** Not found. Sex ratio, geography and anticipation are not found.

## 10–13. Diagnostics, outcome, treatment, prevention

- **Diagnosis.** SPS is diagnosed clinically by WHO criteria; the search summary quotes at least 5 sessile serrated polyps proximal to the sigmoid colon, 2 or more larger than 10 mm. Genetic testing uses multigene panels, and the Danish authors say existing guidelines differ on whether to include RNF43. Brinch 2024 recommends basing surveillance "on patient phenotype and clinical SPS criteria rather than genetic results alone."
- **Prognosis.** I found no survival or CRC risk estimates for RNF43 carriers. I did not search outcome data.
- **Treatment.** I did not search guidelines. Standard SPS management is colonoscopic polypectomy with surveillance and surgery in selected cases, but I did not verify that here. No RNF43-directed therapy is established for this syndrome. PORCN inhibitors are preclinical or trial-stage for RNF43-mutant tumours (review summary, not read). I found no NCT identifiers.
- **Prevention.** Cascade testing and colonoscopy surveillance are plausible, but the supporting guidance was not retrieved. The Danish authors' point that a variant alone does not establish high risk bears directly on counselling.

## 14–15. Other species and models

I did not search OMIA, MGI or ZFIN. The Rnf43/Znrf3 double knockout above is the only model I found. For single Rnf43 knockouts, the zebrafish record in the search results (ZFIN ZDB-PUB-120727-41) was not read.

## Gaps and checks before curation

1. **Unverified PMIDs.** Koo 2012, Yan 2017, Buchanan 2017 and Jiang 2013 were not confirmed. Taupin 2015 came from a search summary. Only PMIDs 24512911 and 39546056 were confirmed by a retrieved source, and PMID 22575959 appears only in a search URL.
2. **Unread papers.** I could not open the PMC page for PMC8048817 (a reCAPTCHA page was returned). The Springer, UK Biobank and Buchanan items are abstract-level only, so I have no exact quotes from them.
3. **Not searched.** Orphanet, ClinVar, gnomAD, guidelines, HPO term lookup, GO/CL lookup, MGI/OMIA, and ClinicalTrials.gov.
4. **ClinGen caveat.** Definitive is a copied tier. The Danish 2024 paper postdates the 2022 evaluation, so a re-evaluation is plausible. I found no indication that ClinGen has changed the tier.

## Sources

- [GenCC/ClinGen submission](https://thegencc.org/submissions/GENCC_000102-HGNC_18505-MONDO_0014919-HP_0000006-GENCC_100001)
- [Brinch et al. 2024, Familial Cancer](https://pmc.ncbi.nlm.nih.gov/articles/PMC11568000/)
- [Gala et al. 2014, PMC3978775](https://pmc.ncbi.nlm.nih.gov/articles/PMC3978775)
- [Taupin et al. 2015, PMC4785559](https://pmc.ncbi.nlm.nih.gov/articles/PMC4785559)
- [Yan et al. 2017, Gut](https://gut.bmj.com/content/66/9/1645)
- [Koo et al. 2012, Nature](https://www.nature.com/articles/nature11308)
- [ZNRF3 R-spondin, PMID 22575959](https://pubmed.ncbi.nlm.nih.gov/22575959/)
- [Jiang et al. 2013, PMC3732970](https://pmc.ncbi.nlm.nih.gov/articles/PMC3732970)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:22575959` (5 mentions) - ZNRF3 promotes Wnt receptor turnover in an R-spondin-sensitive manner.
  - shared terms: rnf43

Weighed against this report's own most characteristic terms: `found`, `rnf43`, `serrated`, `cancer`, `clingen`, `danish`, `sessile`, `variant`, `read`, `polyp`, `sps`, `family`, `germline`, `primary`, `syndrome`, `gala`, `unverified`, `yan`, `colon`, `polyposis`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000006` (1 mention) - the report calls it "MOI: autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

4 of 6 terms resolved to a current term; the rest could not be looked up either way.