---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-27T00:27:08.363798'
end_time: '2026-11-27T00:34:24.523116'
duration_seconds: 436.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Wound Botulism
  mondo_id: MONDO:0015803
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: cutaneous infectious botulism; cutaneous toxin-mediated botulism; inoculation
    botulism; skin infectious botulism; skin toxin-mediated botulism
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 14
  num_turns: 23
  total_cost_usd: 1.359772885
  session_id: b2a809b2-bc70-4a2e-b2ff-05354f3ca511
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 35
  retrieval_calls: 33
  assistant_text_blocks: 4
citation_count: 15
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 8
  validator_version: 0.8.0
term_validation:
  total_terms: 45
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 42
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 3
  service_unreachable: 42
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Wound Botulism
- **MONDO ID:** MONDO:0015803 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** cutaneous infectious botulism; cutaneous toxin-mediated botulism; inoculation botulism; skin infectious botulism; skin toxin-mediated botulism
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Wound Botulism** covering all of the
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

Let me try PubMed E-utilities directly.

I've gathered the core epidemiology, clinical and guideline sources. Next I'm running a few more searches on mechanism, the antitoxin, diagnostics and identifiers, then I'll write the report.

I have enough sourced material to write the report. Let me compose it now.

# Comprehensive Research Report: Wound Botulism (MONDO:0015803)

**Interpretation note (stated up front, per instructions):** Wound botulism is an **infectious, toxin-mediated disease**, not a Mendelian genetic disorder. The template field "Causal gene(s)" is marked "not recorded," which is correct: there is no human causal gene. The relevant "gene" is bacterial — the botulinum neurotoxin gene (*bont*, historically *botA–botG*) carried by *Clostridium botulinum* (and rarely *C. baratii*/*C. butyricum*). The disease is caused by *in vivo* wound infection with toxigenic *Clostridium* and local production of botulinum neurotoxin (BoNT). Throughout, I flag where a cited figure is drawn from all-botulism data rather than wound-specific data, since much published symptom/outcome data pools forms.

**A note on source retrieval:** Several PubMed/PMC article pages returned bot-walls/CAPTCHAs during this session, so for a few primary papers I could retrieve only the bibliographic citation and abstract fragments mirrored in secondary indices or reference lists (flagged inline). CDC MMWR pages, the 2021 CDC clinical guidelines, and ECDC documents were retrieved directly. Where I could not verify a verbatim abstract, I say so rather than fabricate a quote.

---

## 1. Disease Information

**Overview.** Wound botulism is a form of botulism in which *Clostridium botulinum* spores germinate and multiply within an anaerobic wound, producing botulinum neurotoxin (BoNT) locally; the toxin is absorbed systemically and produces a characteristic **acute, afebrile, symmetric, descending flaccid paralysis** with prominent cranial-nerve (bulbar) involvement and clear sensorium. Unlike foodborne botulism, prominent gastrointestinal prodrome is usually absent. In the modern era it is overwhelmingly a disease of **people who inject drugs (PWID)**, especially **subcutaneous/intramuscular injection ("skin popping"/"muscle popping") of black tar heroin** ([CDC, Injection Drug Use and Wound Botulism](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)).

**Key identifiers.**
- **MONDO:** MONDO:0015803 (wound botulism), as given.
- **ICD-10-CM:** **A48.52** "Wound botulism," a billable code under parent A48.5 ("Other specified botulism"); inclusion term "Non-foodborne botulism NOS," with a "use additional code for associated wound" note ([ICD-10-CM A48.52, icdlist](https://icdlist.com/icd-10/A4852); [unboundmedicine A48.52](https://www.unboundmedicine.com/icd/view/ICD-10-CM/921618/all/A48_52___Wound_botulism)).
- **ICD-11:** I could not verify a wound-specific ICD-11 stem code from retrieved sources. Botulism maps generally to **1A11** ("Botulism"); the "unspecified" variant seen in crosswalks is 1A11.Z. *Treat as not verified for the wound subtype* — the WHO ICD-11 browser (icd.who.int) should be checked before populating.
- **MeSH:** "Botulism" (D001906); there is no separate MeSH heading for wound botulism — it is indexed as a subset of Botulism.
- **OMIM / Orphanet:** Not applicable as a genetic disease; no OMIM entry. (Botulism is not an Orphanet rare-disease entry in the usual genetic sense; it is a notifiable infectious disease.)
- **SNOMED CT:** Wound botulism is represented (concept "Wound botulism"); exact SCTID not retrieved this session.

**Synonyms (as supplied, all valid):** cutaneous infectious botulism; cutaneous toxin-mediated botulism; inoculation botulism; skin infectious botulism; skin toxin-mediated botulism. Common clinical usage: "wound botulism," "injection(-related) botulism."

**Data source type.** The knowledge base entry should be tagged as derived from **aggregated disease-level resources** — public-health surveillance (CDC National Botulism Surveillance, CDPH), outbreak investigations (MMWR), case series, and clinical guidelines — supplemented by **individual-patient case reports**. There is no genomic/EHR-cohort basis as there would be for a Mendelian disease.

---

## 2. Etiology

**Primary cause (infectious + toxin-mediated).** The disease results from **wound contamination with *Clostridium botulinum* spores → germination in the anaerobic wound microenvironment → local elaboration of botulinum neurotoxin → systemic absorption**. The causal agent is almost always *C. botulinum* **Group I (proteolytic)**, producing **toxin type A or type B** (the two serotypes that dominate human wound botulism in the US). The toxin — not the organism's dissemination — produces disease. Heating/"cooking" the drug does **not** inactivate heat-resistant spores: *"Heating ('cooking') heroin will not kill the bacteria"* ([CDC risk-factors page](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)).

**Risk factors (environmental/behavioral — these dominate):**
- **Injection drug use, specifically subcutaneous/intramuscular "skin popping" of black tar heroin.** The landmark case-control study (Passaro et al., *JAMA* 1998;279(11):859–863, **PMID 9516001**) found subcutaneous/intramuscular black-tar-heroin injection was *"the only behavior associated with WB among IDUs,"* with an **odds ratio of 13.7 (95% CI 3.0–63.0)** ([JAMA fulltext](https://jamanetwork.com/journals/jama/fullarticle/187346); abstract mirrored via search). Skin/muscle popping creates localized anaerobic, devitalized tissue (foreign particulate, contaminants) ideal for spore germination.
- **Black tar heroin** specifically — likely contaminated with *C. botulinum* spores (e.g., from soil/adulterants during informal production and transport); CDC: *"Most get it from skin popping or muscle popping black tar heroin"* ([CDC](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)).
- **Traumatic/contaminated wounds** (historically): crush injuries, open fractures, puncture wounds contaminated with soil — the predominant mechanism before the IDU epidemic (Werner et al., *Clin Infect Dis* 2000;31:1018–24, **PMID 11049786**: *"Whereas early cases of WB occurred after gross trauma, all but one of the last 102 cases occurred in drug users"*).
- **Demographic skew:** cases occur *"disproportionately in Hispanics and women"* in the California epidemic (Werner et al. 2000, PMID 11049786).
- **Non-protective "hygiene" behaviors:** Notably, risk was *"not affected by cleaning the skin, cleaning injection paraphernalia, or sharing needles"* (Passaro 1998, PMID 9516001) — distinguishing it from bloodborne-virus risk.
- Rarer reported routes: sinusitis in intranasal cocaine users; post-surgical/post-traumatic wounds; cesarean section.

**Genetic risk / protective factors (human):** None established. There are no human susceptibility loci, modifier genes, or protective alleles identified for wound botulism. (gnomAD/GWAS not applicable.)

**Protective factors (environmental):** Avoidance of skin/muscle popping (injecting intravenously rather than subcutaneously carries lower risk per the case-control data), harm-reduction/supervised-injection and drug-supply interventions, and cessation of injection drug use. No dietary/nutritional protective factor applies.

**Gene–environment interactions:** Not applicable in the human-genetics sense. The operative "gene–environment" axis is **bacterial toxin gene × anaerobic wound microenvironment**: the *bont* gene is only pathogenic when the host provides a low-redox, devitalized niche permitting germination and toxin synthesis.

---

## 3. Phenotypes

Botulinum toxin produces a **symmetric, descending flaccid paralysis** beginning in bulbar musculature (cranial nerves) and progressing caudally, **without fever, without sensory loss, and with preserved mentation**. Pupillary and autonomic (cholinergic) features may occur. In wound botulism specifically, the GI prodrome typical of foodborne disease is characteristically **absent/rare**: in the 2021 CDC guidelines, *"vomiting was reported by 172 (50%) patients with foodborne botulism compared with three (5%) with wound botulism"* ([CDC MMWR RR 2021;70(2)](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)). Wound botulism may also show **fever and leukocytosis** attributable to the wound infection itself (unlike other forms).

**Symptom frequencies** (Table 3 of the 2021 CDC guidelines, pooled across confirmed botulism, N=332 — *not* wound-specific, so interpret as botulism-wide): descending paralysis 93%, dysphagia 85%, weakness/fatigue 85%, ptosis 81%, blurred vision 80%, difficulty speaking 78%, diplopia 75%, shortness of breath 65%, nausea 43%, vomiting 33% ([CDC MMWR RR 2021](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)). Also: *"169 (42%) patients had respiratory compromise when admitted"* and *"126 (34%) patients had one or two cranial nerve palsies."*

| Phenotype | Type | HPO suggestion | Characteristics / notes |
|---|---|---|---|
| Ptosis (drooping eyelids) | Clinical sign | **HP:0000508** Ptosis | Early bulbar sign; very common |
| Diplopia / blurred vision | Symptom | **HP:0000651** Diplopia; **HP:0000622** Blurred vision | Early; ophthalmoplegia |
| Ophthalmoplegia | Clinical sign | **HP:0000602** Ophthalmoplegia | External eye muscle weakness |
| Dysphagia | Symptom/sign | **HP:0002015** Dysphagia | Bulbar; aspiration risk |
| Dysarthria / difficulty speaking | Symptom/sign | **HP:0001260** Dysarthria | Bulbar |
| Dry mouth | Symptom | **HP:0000217** Xerostomia | Cholinergic autonomic blockade |
| Facial weakness | Clinical sign | **HP:0010628** Facial palsy | Predictor of ventilation (see §11) |
| Descending symmetric flaccid paralysis / muscle weakness | Clinical sign | **HP:0003484** Upper limb muscle weakness; **HP:0001324** Muscle weakness; **HP:0001252** Hypotonia | Hallmark; symmetric, descending |
| Respiratory insufficiency / failure | Clinical sign | **HP:0002093** Respiratory insufficiency; **HP:0002878** Respiratory failure | Life-threatening; drives ICU need |
| Dilated/poorly reactive pupils | Clinical sign | **HP:0000545** (mydriasis-related) / **HP:0007686** Abnormal pupillary function | Autonomic; variable |
| Constipation / ileus | Symptom | **HP:0002019** Constipation | Autonomic |
| Urinary retention | Symptom/sign | **HP:0000016** Urinary retention | Autonomic |
| Fever (from wound) | Clinical sign | **HP:0001945** Fever | Wound-botulism–specific vs other forms |
| Preserved consciousness | (negative finding) | — | Toxin does not cross BBB; mentation clear |
| Localized wound abscess/cellulitis | Physical manifestation | **HP:0025615** Abscess (approx.) | At injection/trauma site |

**Onset / severity / progression.** Onset is **acute to subacute**, over hours to days once toxin is absorbed. Severity ranges **mild → severe**, with the feared endpoint being **neuromuscular respiratory failure**. The natural course is **monophasic**: progression (worsening) over days, a plateau, then **slow recovery over weeks to months** as motor nerve terminals regenerate; it is **not** relapsing-remitting or episodic. Untreated progression can reach complete flaccid quadriplegia with ventilator dependence.

**Quality-of-life impact.** During the acute illness, QoL impact is profound — prolonged ICU stay, mechanical ventilation (often weeks), tracheostomy, inability to speak/swallow/move, with "locked-in"–like experience despite intact cognition. Recovery of residual fatigue and weakness can take many months. Formal EQ-5D/SF-36 data specific to wound botulism were **not identified** in retrieved sources; this should be marked "data not available."

---

## 4. Genetic/Molecular Information

**Not a human genetic disease** — no human causal genes, pathogenic variants, modifier genes, allele frequencies, chromosomal abnormalities, or human epigenetic changes apply. All molecular etiology is **bacterial**.

**Bacterial "causal gene":**
- **Botulinum neurotoxin gene** — generically ***bont*** (serotype-specific alleles historically *botA, botB, … botG*; now *bont/A*, *bont/B*, etc.). Encodes a ~150 kDa single-chain protoxin.
- **Organism:** *Clostridium botulinum* (Group I, proteolytic, predominant in US wound cases), rarely *C. baratii* (type F) or *C. butyricum* (type E).
- **Toxin serotypes causing human wound botulism:** predominantly **type A and type B**. In the Dallas 2020 outbreak the two laboratory-confirmed cases were **BoNT types A and B** ([MMWR 2022;71(15):556–557](https://www.cdc.gov/mmwr/volumes/71/wr/mm7115a3.htm)); the New Mexico 2016 cluster was **type A** (*"detection of botulinum toxin type A in a wound culture sample"*; [Front Public Health 2021;9:744179, PMID 34976915](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8716579/)).
- **Genetic organization/mobility:** *bont* genes reside in neurotoxin gene clusters that may be chromosomal, plasmid-borne, or phage-associated — explaining horizontal spread of toxigenicity (general clostridial biology; see Rossetto/Pirazzini/Montecucco reviews, below).
- **Functional consequence of the toxin:** a **gain-of-(toxic)-function zinc metalloprotease**; its catalytic light chain is a Zn²⁺-dependent endopeptidase.

**Chemical entity suggestions (CHEBI):** botulinum toxin (CHEBI concept for "botulinum toxin"); Zn²⁺ (CHEBI:29105) as the catalytic cofactor. (Exact CHEBI IDs should be verified in the ontology.)

---

## 5. Environmental Information

- **Environmental factors:** Soil/dust-borne *C. botulinum* spores are the environmental reservoir; spores contaminate wounds directly (traumatic) or via contaminated black tar heroin (likely soil/adulterant contamination during production/transport). *"Heating ('cooking') heroin will not kill the bacteria"* ([CDC](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)).
- **Lifestyle factors:** Injection drug use is the dominant behavioral driver; **subcutaneous/intramuscular injection ("skin/muscle popping")** of **black tar heroin** is the specific high-risk behavior (OR 13.7; Passaro 1998, PMID 9516001). Skin cleaning, paraphernalia cleaning, and needle-sharing did **not** modify risk (Passaro 1998).
- **Infectious agents (NCBI Taxonomy):**
  - ***Clostridium botulinum*** — NCBI:txid1491 (primary agent).
  - ***Clostridium baratii*** — NCBI:txid1561 (rare, type F).
  - ***Clostridium butyricum*** — NCBI:txid1492 (rare, type E).
  - The pathogenic principle is the secreted BoNT; the organism remains localized to the wound and is **not transmitted person-to-person** ([ECDC/EMCDDA Rapid Risk Assessment 2015](https://www.ecdc.europa.eu/sites/default/files/media/en/publications/Publications/RRA-Botulism-Norway-UK.pdf): *"Clostridium botulinum is not transmitted from person to person, the risk to the general population … is negligible"*).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Wound contamination:** *C. botulinum* spores are introduced into a wound (traumatic soil contamination, or subcutaneous/intramuscular injection of spore-contaminated black tar heroin) — **leads to** spores lodging in devitalized tissue.
2. **Anaerobic germination:** The low-oxygen/low-redox, devitalized injection site or abscess **results in** spore germination and vegetative outgrowth of *C. botulinum* (inferred to require the anaerobic, necrotic microenvironment that skin-popping creates — mechanistically consistent with the OR 13.7 for SC/IM injection, Passaro 1998, PMID 9516001).
3. **Local toxin synthesis:** Vegetative bacteria **produce and secrete** BoNT (type A or B) as a ~150 kDa single-chain protoxin, proteolytically **activated (nicked)** into a di-chain of ~100 kDa heavy chain (HC) + ~50 kDa light chain (LC) joined by a disulfide bond.
4. **Systemic absorption:** Toxin **is absorbed** from the wound into the circulation and **distributes to** peripheral cholinergic nerve terminals (it does **not** cross the blood–brain barrier → sensorium preserved).
5. **Dual-receptor binding at the presynaptic terminal:** The HC **binds** a polysialoganglioside *and* a protein receptor on the presynaptic membrane of motor neurons at the neuromuscular junction — **SV2** for type A, **synaptotagmin I/II** for type B (Rossetto/Montecucco literature; search-retrieved review content, PMID 10865130 *"BoNTs bind to a polysialoganglioside and to a protein receptor (SV2 or synaptotagmin)"*).
6. **Internalization:** Receptor binding **triggers** receptor-mediated endocytosis into the nerve terminal; vesicle acidification **drives** translocation of the LC across the endosomal membrane into the cytosol.
7. **SNARE proteolysis (catalytic step):** The LC Zn²⁺-metalloprotease **cleaves** SNARE proteins — **BoNT/A cleaves SNAP-25; BoNT/B cleaves VAMP/synaptobrevin** (serotype-specific: *"a Zn²⁺-dependent endopeptidase specific for one or more of the three SNARE proteins (VAMP, SNAP-25, syntaxin)"*; Schiavo/Montecucco work, e.g., *Nature* 1992 synaptobrevin cleavage by TeNT/BoNT-B).
8. **Block of neuroexocytosis:** SNARE cleavage **prevents** assembly of the fusogenic SNARE complex → **blocks** Ca²⁺-triggered fusion of acetylcholine-containing synaptic vesicles → **abolishes** acetylcholine release into the synaptic cleft.
9. **Presynaptic cholinergic denervation:** Failure of ACh release **causes** functional denervation at **somatic NMJs** (→ flaccid paralysis) and at **autonomic cholinergic synapses** (→ dry mouth, mydriasis, ileus, urinary retention).
10. **Clinical manifestation:** Descending symmetric flaccid paralysis beginning bulbar (cranial nerves) → limbs → **diaphragm/respiratory muscles**, culminating (if untreated) in **neuromuscular respiratory failure**. **Branch:** local wound infection independently **produces** fever, leukocytosis, abscess/cellulitis — the feature distinguishing wound from foodborne botulism.
11. **Recovery (downstream, slow):** Over weeks–months, **sprouting of new nerve terminals and SNARE protein turnover** restores functional transmission. Antitoxin only neutralizes **circulating, not yet internalized** toxin — hence it *"arrest[s] … progression"* but does *"not reverse paralysis"* ([CDC MMWR RR 2021](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)).

### Checklist detail
- **Molecular pathways:** SNARE-mediated synaptic vesicle exocytosis (Reactome "Neurotransmitter release cycle"; KEGG "SNARE interactions in vesicular transport," map04130). Core targets: **SNAP-25, VAMP/synaptobrevin, syntaxin-1**.
- **Cellular processes:** Blockade of regulated exocytosis / neurotransmitter release; no apoptosis or inflammation at the neuron (toxin effect is enzymatic/functional). Local wound: acute pyogenic inflammation.
- **Protein dysfunction:** Proteolytic **destruction** of SNARE substrates (loss of function of the fusion machinery) by a toxin **gain-of-function** protease (UniProt: BoNT/A **P0DPI1**; BoNT/B **P10844** — IDs to verify; target SNAP-25 **P60880**, VAMP2 **P63027**, syntaxin-1A **Q16623**).
- **Metabolic/biochemical:** Zn²⁺-dependent endopeptidase catalysis (CHEBI:29105 Zn²⁺); no host enzyme deficiency. The defect is **ion-channel/receptor-independent** but functionally presynaptic.
- **Immune involvement:** Local innate inflammatory response to wound infection; the toxin itself is poorly immunogenic at disease doses (patients can be re-infected; no durable protective immunity).
- **Tissue damage mechanism:** Functional denervation (reversible) rather than structural neuronal necrosis; wound tissue shows infectious necrosis.

**Suggested GO / CL terms:**
- GO biological process: **GO:0007269** neurotransmitter secretion; **GO:0017158** regulation of calcium ion-dependent exocytosis; **GO:0006887** exocytosis; **GO:0035493** SNARE complex assembly.
- GO cellular component: **GO:0031201** SNARE complex; **GO:0008021** synaptic vesicle; **GO:0042734** presynaptic membrane.
- GO molecular function: **GO:0004222** metalloendopeptidase activity.
- Cell type (CL): **CL:0000100** motor neuron; **CL:0011001** spinal cord motor neuron; **CL:0000211** electrically active cell (cholinergic neuron); target effector **CL:0000187** muscle cell.

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Primary target: peripheral nervous system / neuromuscular junction** (somatic + autonomic cholinergic). UBERON: **UBERON:0001016** nervous system; **UBERON:0001134** skeletal muscle tissue; structure "neuromuscular junction" (GO:0031594 as a synapse; UBERON "neuromuscular junction" if needed).
- **Secondary / complication organs:** **Respiratory system** (diaphragm failure → ventilatory failure; UBERON:0001004 respiratory system; UBERON:0001103 diaphragm); **eye/extraocular muscles** (UBERON:0000970 eye); **GI tract** (ileus; UBERON:0001555 digestive tract); **urinary bladder** (retention; UBERON:0001255).
- **Site of infection (local):** skin/subcutaneous tissue and soft tissue at the injection/trauma site (UBERON:0002097 skin of body; UBERON:0002384 connective tissue) — abscess/cellulitis.

**Tissue/cell level:** Motor neurons and their **presynaptic cholinergic nerve terminals** at NMJs; autonomic cholinergic terminals. Cell Ontology: **CL:0000100** motor neuron. Muscle fibers themselves are structurally normal but functionally denervated.

**Subcellular level (GO cellular component):** **synaptic vesicle (GO:0008021)**; **presynaptic membrane (GO:0042734)**; **SNARE complex (GO:0031201)**; cytosol (site of LC protease action, GO:0005829); endosome (translocation, GO:0005768).

**Localization / lateralization:** Neuromuscular effects are **bilateral and symmetric** (hallmark); the **wound/abscess is focal/localized** (often unilateral extremity or injection site). HPO descriptor for symmetry is intrinsic to the "symmetric descending paralysis" phenotype.

---

## 8. Temporal Development

- **Onset / incubation:** For wound botulism, neurologic symptoms *"usually appear within a few days to two weeks"* after the exposure/injection ([CDC risk-factors page](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)) — longer and more variable than foodborne (which is typically 12–72 h) because toxin must first be produced in situ. Documented toxin detection as late as **43 days** post-exposure in a wound culture (New Mexico 2016; PMID 34976915). **Onset pattern:** acute/subacute.
- **Progression / stages:** Prodrome/local wound symptoms → cranial nerve (bulbar) onset → descending limb weakness → respiratory compromise (potential failure). Course is **monophasic progressive then plateau**, not relapsing.
- **Rate:** Variable (hours–days); earlier/larger toxin burden → faster, more severe.
- **Duration:** **Self-limited in the sense of monophasic**, but recovery is **prolonged (weeks to months)**; ventilator dependence of weeks is common (New Mexico: *"Patient 3 required mechanical ventilation for 110 days"*; Germany case: mechanical ventilation for **11 weeks** per [EID 2007 letter, PMC2792833](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2792833/)).
- **Remission:** Spontaneous functional recovery via nerve-terminal sprouting; treatment (antitoxin) halts progression but does not accelerate reversal of established paralysis.
- **Critical period for intervention:** Antitoxin is effective only against **circulating toxin before neuronal internalization**, so the therapeutic window is **early** — hence the guideline emphasis on treating on clinical suspicion without awaiting labs. In San Diego, *"Median interval from symptom onset to BAT administration was 6.5 days (range 2.7–10.5)"* ([MMWR San Diego 2017–2018](https://www.cdc.gov/mmwr/volumes/67/wr/mm675152a3.htm)).

---

## 9. Inheritance and Population

**Inheritance:** Not applicable — infectious/toxin-mediated, **no heritability, no inheritance pattern, no penetrance/expressivity/anticipation/mosaicism/founder/consanguinity/carrier concepts** apply.

**Epidemiology:**
- **US incidence:** *"Every year in the United States, about 20 people are diagnosed with wound botulism"* ([CDC](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)). Over 2010–2019, *"a total of 206 laboratory-confirmed cases of wound botulism were reported in the United States, including 160 (78%) in California and eight (4%) in Texas"* ([MMWR Dallas 2022;71(15)](https://www.cdc.gov/mmwr/volumes/71/wr/mm7115a3.htm)).
- **California dominance:** California has reported the majority of US (and historically world) wound botulism; Werner et al. 2000 (PMID 11049786): California *"has reported … nearly three-fourths of the cases reported in the United States."* CDPH reported **184 cases in 2013–2019 (~26/year)**, rate <1/100,000 ([CDPH Wound Botulism Epi Summary 2013–2019](https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/WoundBotulismEpiSummary2013-2019.pdf)); and ~50 cases in 2009–2012 (~0.03/100,000) ([CDPH 2009–2012 summary](https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/WoundBotulismEpiSummary09-12.pdf)).
- **Prevalence:** As an acute, non-chronic condition, point-prevalence is not a standard metric; incidence (~20/year US) is the operative figure. Rate <<1/100,000.
- **Historical trajectory:** Pre-1990 California cases were trauma-associated; an **IDU-driven epidemic** began in the early 1990s (annual California counts rising 1→11 over 1990–1994 per MMWR). Werner 2000: California reported **127 cases 1951–1998**, with the last 102 nearly all in drug users.

**Demographics / geographic distribution:**
- **Geography:** Clustered where **black tar heroin** circulates — the **western US (esp. California)**; emerging foci (New Mexico 2016, San Diego 2017–18, Texas/Dallas 2020). In Europe, episodic outbreaks among PWID (UK/Scotland, Norway, Germany, Ireland).
- **Sex/ethnicity:** California epidemic skewed toward **Hispanic patients and women** (Werner 2000, PMID 11049786), though other outbreaks (e.g., San Diego) were male-predominant (8/9 men; median age 40, range 25–67; [MMWR San Diego](https://www.cdc.gov/mmwr/volumes/67/wr/mm675152a3.htm)). Sex ratio therefore varies by outbreak and is **not fixed**.
- **Age:** Working-age adults (PWID), typically ~25–60; not a pediatric/geriatric disease (contrast infant botulism).

**International outbreaks (PWID):**
- **Scotland 2015:** largest European PWID wound-botulism outbreak — **40 cases** across six Scottish regions (Dec 2014–May/June 2015), plus **8 in Norway**; **4 deaths (botulism contributory in 2)**; likely contaminated heroin/cutting-agent batch; all treated with antitoxin, ~50% debrided, all received antibiotics ([Harm Reduction Journal 2018, PMC6042261](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6042261/); [ECDC/EMCDDA RRA 2015](https://www.ecdc.europa.eu/sites/default/files/media/en/publications/Publications/RRA-Botulism-Norway-UK.pdf)).
- **Germany:** first molecularly-confirmed IDU wound-botulism outbreak; index 31-yo woman with leg abscesses, ventilated 11 weeks ([EID 2007 letter, PMC2792833](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2792833/)).

---

## 10. Diagnostics

**Diagnosis is primarily clinical** — the 2021 CDC guidelines stress diagnosis rests on clinical suspicion and neurologic exam, and that *treatment should begin before laboratory confirmation* ([CDC MMWR RR 2021;70(2), PMID 33956777](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)).

**Laboratory / confirmatory tests:**
- **Serum toxin assay:** detection of BoNT in serum (historically **mouse bioassay**, the reference standard; increasingly mass-spectrometry/Endopep-MS). Collect **5–15 mL serum (children 4 mL)**, tested for toxin, *"Collect before antitoxin treatment"* (Table 5, [CDC MMWR RR 2021](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)). **Do not freeze serum.**
- **Wound specimens:** debrided tissue, wound swab, or **anaerobic wound culture** tested **for *Clostridium*** (organism isolation + toxin production). Caveat (guidelines): *"In patients with wound botulism, botulinum neurotoxin–producing species of Clostridium are not always detected in wound specimens, especially after administration of antibiotics."*
- **Stool/gastric** testing is more relevant to foodborne but may be done to exclude intestinal source.
- Serum toxin and wound culture are **complementary**; negative labs do **not** exclude the diagnosis.
- **LOINC:** "Clostridium botulinum toxin" and "Clostridium botulinum culture" panels exist (specific LOINC codes to be verified in LOINC).

**Supporting / rule-out studies:**
- **Electrodiagnostics (EMG/nerve conduction/repetitive nerve stimulation):** presynaptic neuromuscular transmission defect — **low CMAP amplitude** with **facilitation (incremental response) on high-frequency (rapid) repetitive stimulation**; helps distinguish from Guillain-Barré and myasthenia gravis.
- **CSF:** typically normal (distinguishes from GBS, where protein is elevated).
- **Imaging (brain MRI/CT):** normal — used to exclude stroke/brainstem lesions.
- **Edrophonium (Tensilon) / AChR antibodies:** to exclude myasthenia gravis.

**Differential diagnosis:** Guillain-Barré syndrome (esp. Miller-Fisher variant), myasthenia gravis, Lambert-Eaton myasthenic syndrome, stroke/brainstem CVA, tick paralysis, heavy-metal/organophosphate poisoning, and — critically in PWID — **opioid intoxication/overdose** (symptoms *"can resemble an opioid overdose"*; naloxone *"will not reverse symptoms of botulism"* — [CDC](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)). Diagnostic delay from mistaking it for intoxication was repeatedly documented (New Mexico: *"Wound botulism was not considered during patient 1 and patient 3's initial emergency department evaluations"*, PMID 34976915).

**Genetic testing / omics diagnostics:** Not applicable (no human genetics). Microbial typing (PFGE, WGS of *C. botulinum*, toxin-gene PCR, Endopep-MS) is used for **outbreak epidemiology/serotyping**, not patient genetic diagnosis — Germany outbreak was *"the first outbreak … confirmed by molecular epidemiologic typing"* ([EID 2007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2792833/)).

**Clinical criteria / screening:** Case definitions follow CDC/CSTE notifiable-disease criteria (clinically compatible illness + laboratory confirmation OR epidemiologic link). No population screening exists; there is no newborn/carrier screening (not genetic).

---

## 11. Outcome / Prognosis

- **Mortality:** Botulism case-fatality has fallen from *"approached 70% in the first half of the twentieth century"* to *"<5%"* with modern critical care and antitoxin ([CDC MMWR RR 2021](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)). Wound-botulism outbreak fatalities: **1 of 9 died** in San Diego 2017–18 ([MMWR](https://www.cdc.gov/mmwr/volumes/67/wr/mm675152a3.htm)); **4 deaths** (botulism contributory in 2) in Scotland/Norway 2015 ([Harm Reduction J 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6042261/)). A discrete wound-specific case-fatality rate was not isolated in retrieved guideline text — report as roughly single-digit percent.
- **Morbidity / ICU burden:** High. Respiratory failure requiring **mechanical ventilation and prolonged ICU care** is the principal morbidity — *"Four (57%) patients required mechanical ventilation and prolonged intensive care"* (Dallas; [MMWR 2022](https://www.cdc.gov/mmwr/volumes/71/wr/mm7115a3.htm)); **six of nine** intubated in San Diego; ventilation of **30 and 110 days** in New Mexico (PMID 34976915). Median hospital stay 15 days and estimated direct hospital costs **$2.3 million** for the San Diego cluster.
- **Recovery potential:** Generally **good functional recovery** with supportive care, though prolonged; residual fatigue/weakness can persist months. Recovery depends on nerve-terminal regeneration.
- **Prognostic factors:** **Early antitoxin** administration improves outcome — Sandrock & Murin (*Chest* 2001;120(2):562–566) concluded *early antitoxin may decrease the need for and duration of mechanical ventilation, and early tracheostomy may be beneficial* (citation and conclusions retrieved via index; full abstract not directly accessible this session — flag as secondary). Surveillance analysis found **facial paralysis and shortness of breath** predicted need for mechanical ventilation (Emory thesis analysis of 1999–2014 CDC data — secondary source). Delay to diagnosis/treatment worsens outcome.
- **Quality-of-life measures:** No validated disease-specific QoL instrument identified; mark "not available."

---

## 12. Treatment

**(a) Antitoxin — the only specific therapy.**
- **Botulism Antitoxin Heptavalent (BAT)** — equine-derived, **despeciated F(ab')₂/Fab fragments against serotypes A–G** ([CDC MMWR RR 2021](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm); Table 6 lists IU/vial: A 4,500; B 3,300; C 3,000; D 600; E 5,100; F 3,000; G footnoted/not internationally recognized). **Standard adult dose = one vial.** In the US it is supplied free by the federal government (via state/local health departments and CDC) for suspected non-infant cases.
- **Mechanism/limitation:** neutralizes **circulating (not yet internalized) toxin**; *"Botulism Antitoxin Heptavalent and BabyBIG do not reverse paralysis but arrest its progression by neutralizing toxin circulating in the blood"* — so **administer early, on clinical suspicion, without awaiting labs**.
- **Administration/safety:** infusion begun slowly (per guideline-adjacent sources, ~0.5 mL/min, up-titrated); **routine skin testing is not recommended**; anaphylaxis rate **<2%**, other (typically rash) allergic reactions in **6/249** recipients; serum sickness reported, frequency not well established. In New Mexico, *"Among 249 patients treated with BAT, the most frequently reported adverse events included fever (4%), rash (2%)"* (PMID 34976915). **NCIT:** "Botulinum Antitoxin."

**(b) Wound source control (wound-botulism–specific).**
- **Surgical debridement** of the infected wound/abscess — guidelines: wound botulism treatment is *"generally centered on debridement."* In Scotland, ~50% of cases underwent debridement ([Harm Reduction J 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6042261/)). **NCIT:** "Debridement."
- **Antibiotics:** given to treat the wound infection (and commonly as adjunct in wound botulism — all Scotland cases received antibiotics), **but** the guidelines caution *"Antimicrobials do not provide any benefit in treatment of botulism"* per se (they treat the infection, not the toxin).
  - **Agents to AVOID / use with caution:** **aminoglycosides** (*"Aminoglycosides act in vitro as neuromuscular blocking agents"*) and **clindamycin** (*"Concerns exist about the ability of clindamycin to block acetylcholine release"*). Guideline recommendation: *"Aminoglycosides, magnesium, clindamycin, tetracycline, or calcium should only be administered to patients with botulism after careful consideration and with appropriate monitoring"* — because they can **potentiate neuromuscular blockade** ([CDC MMWR RR 2021](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)). **Penicillin/metronidazole** are the conventionally preferred agents for the clostridial wound (standard clinical practice).

**(c) Supportive / critical care — the backbone of survival.**
- **Airway protection, intubation, mechanical ventilation**, often prolonged; tracheostomy for extended ventilation; ICU monitoring of respiratory function (vital capacity/NIF); nutrition, DVT/pressure-ulcer prophylaxis, bowel/bladder management. *"Evidence does not indicate benefit from any treatment modalities other than antitoxin, although data are limited."* **NCIT:** "Mechanical Ventilation," "Supportive Care."

**(d) Advanced/experimental:** No approved gene, cell, RNA, targeted, or immunotherapy. No pharmacogenomics applies. Experimental small-molecule/oligonucleotide BoNT-LC protease inhibitors and monoclonal antibody antitoxins are in research but not standard of care (no specific NCT verified this session).

**(e) Personalized/combination approach:** Management is **not** genotype-guided; it is a standardized combination: **early BAT + wound debridement + appropriate antibiotics (avoiding neuromuscular-blocking agents) + intensive supportive care** ([CDC MMWR RR 2021](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)).

---

## 13. Prevention

- **Primary prevention:**
  - **Harm reduction for PWID** — avoiding **skin/muscle popping**, not using black tar heroin, needle/drug-supply interventions; abstinence/cessation of injection drug use. The Scotland 2015 response used a *"pragmatic harm reduction approach … focused on reducing the risk of infection for those who continued to inject and limited consequences for those who got infected"* ([Harm Reduction J 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6042261/)).
  - **Proper wound care** for traumatic/contaminated wounds (cleaning, debridement of devitalized tissue removes the anaerobic niche).
  - No routinely used human vaccine — a **pentavalent (A–E) botulinum toxoid** was historically available only as an investigational agent for occupational/laboratory exposure and is **not** used in the general population or routinely for PWID.
- **Secondary prevention / early detection:** Clinician and public-health **awareness and rapid recognition** in PWID presenting with cranial-nerve signs; prompt reporting to health departments; outbreak surveillance. New Mexico authors: *"clinicians and health departments should maintain suspicion"* (PMID 34976915).
- **Tertiary prevention:** Early antitoxin + ICU care to prevent respiratory failure and death; aggressive debridement to prevent ongoing toxin production.
- **Public health:** Botulism is a **nationally notifiable disease**; suspected cases trigger emergency health-department consultation and antitoxin release. Drug-supply monitoring and alerts to PWID networks during outbreaks.
- **Genetic counseling / carrier/prenatal screening:** **Not applicable** (non-genetic).

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected hosts:** Naturally occurring botulism (including wound botulism) affects multiple vertebrates. Humans — *Homo sapiens* (NCBI:txid9606). Notable animal hosts: **horse** *Equus caballus* (NCBI:txid9796), **cattle** *Bos taurus* (NCBI:txid9913), **dog** *Canis lupus familiaris* (NCBI:txid9615), **donkey** *Equus asinus*, birds (waterfowl, "limberneck").
- **Natural disease in animals (wound-specific):** Wound botulism is a recognized clinical form in **horses** — veterinary references describe three equine forms: **forage poisoning, toxicoinfectious (shaker foal), and wound botulism**, the last from *C. botulinum* infecting anaerobic wounds such as **puncture wounds, castration sites, injection-site abscesses, and umbilical/urachal abscesses in foals** ([Merck/MSD Veterinary Manual, Botulism in Animals](https://www.msdvetmanual.com/veterinary/generalized-conditions/clostridial-diseases/botulism-in-animals)). Forage poisoning is the most common equine form, so wound cases are comparatively uncommon.
- **Dogs:** susceptible but *"very few reports"*; no well-documented canine wound-botulism case identified in retrieved sources ([MSD Vet Manual](https://www.msdvetmanual.com/veterinary/generalized-conditions/clostridial-diseases/botulism-in-animals)).
- **Orthologous genes:** Not applicable in the usual sense — the disease is driven by the **bacterial** *bont* gene, not a host ortholog; the neuromuscular targets (SNAP-25, VAMP2, syntaxin) are highly conserved across mammals, explaining broad cross-species susceptibility.
- **Comparative biology / conservation:** The BoNT mechanism (SNARE cleavage → cholinergic blockade) is conserved across all susceptible species; serotype susceptibility varies (e.g., animals commonly affected by types C/D; humans by A/B/E/F). **Zoonotic transmission:** not person-to-person or animal-to-person via contagion; shared risk is environmental spore exposure. **Veterinary/VBO breed-specific** predisposition: none established (exposure-driven, not breed-driven).

---

## 15. Model Organisms

- **In vivo potency/neutralization assay (reference standard):** the **mouse lethality (mouse bioassay)** — the historical gold standard for detecting/quantifying BoNT and for testing antitoxin neutralization. Mouse (*Mus musculus*, NCBI:txid10090) is the principal whole-animal model.
- **There is no genetic mouse "model of wound botulism"** in the knockout/transgenic sense — because the disease is a **toxin exposure/infection**, models are **induced** (toxin challenge or bacterial wound inoculation), not germline-engineered. Knockout mice of SNARE genes (e.g., *Snap25*, *Vamp2*) are used mechanistically to study the exocytosis machinery the toxin targets, not as disease recapitulations.
- **Ex vivo / in vitro systems:** mouse **phrenic nerve–hemidiaphragm preparation** (classic assay of neuromuscular transmission block); primary neuron cultures and **iPSC-derived motor neurons**; cell-based translocation/cleavage assays (e.g., Endopep-MS using recombinant SNARE substrates). These are used to study receptor binding (SV2, synaptotagmin), LC protease activity, and antitoxin/inhibitor efficacy.
- **Large-animal/natural models:** horses and cattle experience natural toxicoinfectious/wound botulism and inform veterinary pathology, but are not standard laboratory disease models.
- **Phenotype recapitulation:** Toxin-challenge rodent models **faithfully reproduce the peripheral flaccid paralysis and respiratory failure** (the lethal endpoint) and the SNARE-cleavage biochemistry, making them highly predictive for therapeutics targeting circulating toxin. **Limitation:** they do not capture the **human behavioral/wound-ecology context** (skin-popping, abscess microenvironment, chronic injection) that defines real-world wound botulism, nor the prolonged human rehabilitation course.
- **Resources:** MGI (mouse SNARE gene alleles), standard toxin/antitoxin assay protocols in the CDC/select-agent framework.

---

## Summary of ontology term suggestions (for KB population)

- **MONDO:** MONDO:0015803 (wound botulism).
- **HPO (phenotypes):** HP:0000508 (ptosis), HP:0000602 (ophthalmoplegia), HP:0000651 (diplopia), HP:0002015 (dysphagia), HP:0001260 (dysarthria), HP:0010628 (facial palsy), HP:0001324 (muscle weakness), HP:0002093 (respiratory insufficiency), HP:0002878 (respiratory failure), HP:0000217 (xerostomia), HP:0002019 (constipation), HP:0000016 (urinary retention), HP:0001945 (fever).
- **GO:** GO:0007269, GO:0017158, GO:0006887, GO:0031201, GO:0008021, GO:0042734, GO:0004222.
- **CL:** CL:0000100 (motor neuron).
- **UBERON:** UBERON:0001016 (nervous system), UBERON:0001134 (skeletal muscle tissue), UBERON:0001103 (diaphragm), UBERON:0002097 (skin), UBERON:0000970 (eye).
- **CHEBI:** Zn²⁺ (CHEBI:29105); botulinum toxin (verify CHEBI ID).
- **NCIT (treatments):** Botulinum Antitoxin; Debridement; Mechanical Ventilation; Supportive Care; Antibiotic Therapy.
- **NCBI Taxonomy:** *C. botulinum* txid1491; *C. baratii* txid1561; *C. butyricum* txid1492.

## Key references (PMID/identifiers verified this session where shown)

1. Rao AK, Sobel J, Chatham-Stephens K, Luquez C. **Clinical Guidelines for Diagnosis and Treatment of Botulism, 2021.** MMWR Recomm Rep 2021;70(2):1–30. **PMID 33956777**; PMCID PMC8112830; DOI 10.15585/mmwr.rr7002a1. [link](https://www.cdc.gov/mmwr/volumes/70/rr/rr7002a1.htm)
2. Passaro DJ, Werner SB, McGee J, Mac Kenzie WR, Vugia DJ. **Wound botulism associated with black tar heroin among injecting drug users.** JAMA 1998;279(11):859–863. **PMID 9516001**. [link](https://jamanetwork.com/journals/jama/fullarticle/187346)
3. Werner SB, Passaro D, McGee J, Schechter R, Vugia DJ. **Wound botulism in California, 1951–1998: recent epidemic in heroin injectors.** Clin Infect Dis 2000;31(4):1018–1024. **PMID 11049786**.
4. Sandrock CE, Murin S. **Clinical predictors of respiratory failure and long-term outcome in black tar heroin-associated wound botulism.** Chest 2001;120(2):562–566. (abstract via index; verify PMID — listed secondarily as 11502659).
5. Middaugh N, Edwards L, Chatham-Stephens K, Arguello DF. **Wound Botulism Among Persons Who Inject Black Tar Heroin in New Mexico, 2016.** Front Public Health 2021;9:744179. **PMID 34976915**; PMCID PMC8716579. [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8716579/)
6. Peak CM, et al. **Wound Botulism Outbreak Among Persons Who Use Black Tar Heroin — San Diego County, California, 2017–2018.** MMWR 2019;67(5152):1415–1418. [link](https://www.cdc.gov/mmwr/volumes/67/wr/mm675152a3.htm)
7. Edwards LD, et al. **Notes from the Field: Wound Botulism Outbreak … Dallas, Texas, 2020.** MMWR 2022;71(15):556–557. [link](https://www.cdc.gov/mmwr/volumes/71/wr/mm7115a3.htm)
8. Trayner KMA, et al. **A pragmatic harm reduction approach to manage a large outbreak of wound botulism in people who inject drugs, Scotland 2015.** Harm Reduct J 2018. PMCID PMC6042261. [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6042261/)
9. Kalka-Moll WM, et al. **Wound Botulism in Injection Drug Users.** Emerg Infect Dis 2007;13(6). PMCID PMC2792833; DOI 10.3201/eid1306.061336. [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2792833/)
10. ECDC/EMCDDA. **Rapid Risk Assessment: Wound botulism in people who inject heroin: Norway and the United Kingdom, 16 Feb 2015.** [link](https://www.ecdc.europa.eu/sites/default/files/media/en/publications/Publications/RRA-Botulism-Norway-UK.pdf)
11. (Mechanism) Review on how BoNTs/TeNT block neurotransmitter release via SNARE cleavage — **PMID 10865130** (Schiavo/Montecucco lineage); Schiavo et al., *Nature* 1992 (synaptobrevin cleavage, BoNT/B & TeNT). [link](https://pubmed.ncbi.nlm.nih.gov/10865130/)
12. CDC. **Injection Drug Use and Wound Botulism** (clinical/risk-factor page). [link](https://www.cdc.gov/botulism/risk-factors/wound-botulism.html)
13. CDPH. Wound Botulism Epidemiology Summaries [2009–2012](https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/WoundBotulismEpiSummary09-12.pdf) and [2013–2019](https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/WoundBotulismEpiSummary2013-2019.pdf).
14. Merck/MSD Veterinary Manual. **Botulism in Animals.** [link](https://www.msdvetmanual.com/veterinary/generalized-conditions/clostridial-diseases/botulism-in-animals)

---

**Caveats on evidence quality:** Symptom-frequency percentages (Table 3) and some mortality/safety figures from the 2021 CDC guidelines are **pooled across all botulism forms**, not wound-specific, and are flagged as such above. A few primary-article abstracts (PMID 9516001, 11049786, 11502659) could not be opened directly this session due to publisher/PubMed access walls; their citations and key findings are drawn from CDC/MMWR reference lists and bibliographic indices and are labeled accordingly. The ICD-11 wound-subtype code and exact SNOMED CT/CHEBI/LOINC identifiers should be verified in the respective ontology browsers before final KB entry.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 42 |
| Terms whose name was checked | 3 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |

### Terms the ontology service could not be reached for

42 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0015803` (3 mentions)
- `HP:0000622` (1 mention)
- `HP:0002015` (2 mentions)
- `HP:0001260` (2 mentions)
- `HP:0000217` (2 mentions)
- `HP:0010628` (2 mentions)
- `HP:0003484` (1 mention)
- `HP:0001324` (2 mentions)
- `HP:0001252` (1 mention)
- `HP:0002093` (2 mentions)
- `HP:0002878` (2 mentions)
- `HP:0000545` (1 mention)
- `HP:0007686` (1 mention)
- `HP:0002019` (2 mentions)
- `HP:0000016` (2 mentions)
- `HP:0001945` (2 mentions)
- `HP:0025615` (1 mention)
- `CHEBI:29105` (3 mentions)
- `GO:0007269` (2 mentions)
- `GO:0017158` (2 mentions)
- `GO:0006887` (2 mentions)
- `GO:0035493` (1 mention)
- `GO:0031201` (3 mentions)
- `GO:0008021` (3 mentions)
- `GO:0042734` (3 mentions)
- `GO:0004222` (2 mentions)
- `CL:0000100` (3 mentions)
- `CL:0011001` (1 mention)
- `CL:0000211` (1 mention)
- `CL:0000187` (1 mention)
- `UBERON:0001016` (2 mentions)
- `UBERON:0001134` (2 mentions)
- `GO:0031594` (1 mention)
- `UBERON:0001004` (1 mention)
- `UBERON:0001103` (2 mentions)
- `UBERON:0000970` (2 mentions)
- `UBERON:0001555` (1 mention)
- `UBERON:0001255` (1 mention)
- `UBERON:0002097` (2 mentions)
- `UBERON:0002384` (1 mention)
- `GO:0005829` (1 mention)
- `GO:0005768` (1 mention)

3 of 45 terms resolved to a current term; the rest could not be looked up either way.