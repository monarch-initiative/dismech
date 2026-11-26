---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T20:05:01.565864'
end_time: '2026-11-25T20:08:50.814962'
duration_seconds: 229.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Infectious Mononucleosis
  mondo_id: MONDO:0005810
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Gammaherpesviral mononucleosis; Mono; glandular fever
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
  web_search_requests: 29
  num_turns: 39
  total_cost_usd: 1.6921036
  session_id: 236e9cc7-4496-49e1-b458-8c2dfd1b32b6
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  tool_calls: 37
  retrieval_calls: 30
  assistant_text_blocks: 4
citation_count: 29
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 2
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:26424648
  - PMC:PMC4670567
  - PMC:PMC8721657
  - PMC:PMC2708605
  relevance_assessed: 22
  on_topic: 12
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infectious Mononucleosis
- **MONDO ID:** MONDO:0005810 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Gammaherpesviral mononucleosis; Mono; glandular fever
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Infectious Mononucleosis** covering all of the
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

Bash can't reach the web here, so I'm switching to web search to gather sources.

I have most of the core sources. Running one last batch of searches on complications, identifiers, and inborn errors of immunity, then I'll write the report.

# Infectious mononucleosis (MONDO:0005810): research report for a disease knowledge base entry

**How I read the request:** this is an infectious disease, so **it has no causal human gene.** The cause is primary infection with Epstein–Barr virus (EBV, human gammaherpesvirus 4). Host genes only change risk and severity. These include HLA class I polymorphisms, and rare inborn errors of immunity such as *SH2D1A* that cause fulminant disease. The genetics fields in the template that assume a Mendelian disease are marked "not applicable".

**Limits of what I could check:** I had no access to PubMed or the ontology APIs in this run. All sources were found through web search. PMIDs are given only where a PubMed or QxMD record was returned; otherwise I give the PMC ID or DOI that was returned. Under the instruction not to state unretrieved identifiers, **ontology terms (HPO, GO, CL, UBERON, NCIT, CHEBI) are given as labels only, without IDs.** The MONDO ID comes from the request. Of the other identifiers, I checked only ICD-10 B27.0.

---

## 1. Disease Information

**Overview.** Infectious mononucleosis (IM) is the clinical illness that sometimes follows primary EBV infection. A review by Dunmire, Hogquist and Balfour describes it as typically "sore throat, cervical lymph node enlargement, fatigue and fever, most often in adolescents and young adults, lasting several weeks" ([PMC4670567](https://pmc.ncbi.nlm.nih.gov/articles/PMC4670567), PMID 26424648). Balfour et al. (Clin Transl Immunol 2015, PMID [25774295](https://pubmed.ncbi.nlm.nih.gov/25774295/)) add two points:
- A typical picture with a positive heterophile test is usually enough to diagnose IM, although heterophile antibodies are not specific.
- IM is linked to long-term consequences, especially Hodgkin lymphoma and multiple sclerosis.

According to the CDC, EBV is the most common cause of IM, but other viruses can cause it too ([CDC](https://www.cdc.gov/epstein-barr/about/mononucleosis.html)).

**Identifiers**

| System | Identifier | Status |
|---|---|---|
| MONDO | MONDO:0005810 | From the request |
| ICD-10-CM | **B27.0** Gammaherpesviral mononucleosis. Subcodes: B27.00 without complication; B27.01 with polyneuropathy; B27.02 with meningitis; B27.09 with other complications. Related codes: B27.1 cytomegaloviral, B27.8 other, B27.9 unspecified. | Verified ([AAPC](https://www.aapc.com/codes/icd-10-codes/B27.0); [health.mil case definition](https://health.mil/Reference-Center/Publications/2019/08/01/Mononucleosis)) |
| PheWAS phecode | 079.2 "Infectious mononucleosis" | Verified ([UMich](https://csg.sph.umich.edu/larsf/exprsweb/phecodes/079.2)) |
| OMIM | None for IM itself. Related host disorders exist: XLP1 is caused by *SH2D1A*, OMIM gene entry *300490 ([OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/300490)). | — |
| MeSH, ICD-11, Orphanet | Not checked in this session; look up before use | — |

**Synonyms:** glandular fever, mono, gammaherpesviral mononucleosis, EBV mononucleosis, Pfeiffer's disease, monocytic angina. The last two are ICD-10 inclusion terms ([AAPC](https://www.aapc.com/codes/icd-10-codes/B27.0)).

**Evidence base:** almost all of it comes from aggregated cohorts and registries, for example Danish and Swedish registries, US NHANES, and prospective student cohorts. None of it comes from individual EHR case records.

---

## 2. Etiology

**Cause.** Primary infection with EBV, a gammaherpesvirus spread through saliva ([CDC](https://www.cdc.gov/epstein-barr/about/mononucleosis.html)). Whether primary infection causes IM, rather than no symptoms, depends strongly on age. In a prospective cohort of Minnesota students who started out antibody-negative, 66 of 143 became infected over a median of 3 years. Of those 66, 77% developed IM, 12% had atypical symptoms and 11% had no symptoms (Balfour et al., J Infect Dis 2013, PMID [23100562](https://pubmed.ncbi.nlm.nih.gov/23100562/)).

**Environmental and behavioural risk factors**
- **Deep kissing:** students who reported deep kissing, with or without intercourse, had a higher risk of infection than those who reported no kissing (PMID 23100562).
- **Age at first infection:** infection in adolescence or early adulthood carries the highest risk. Peak incidence is at ages 15–24 ([AAFP review via PMC6822211](https://pmc.ncbi.nlm.nih.gov/articles/PMC6822211)).
- **Socioeconomic status and race/ethnicity:** in NHANES, EBV seroprevalence differed widely by race/ethnicity and income (Dowd et al., PLoS ONE 2013, [PMC3661547](https://pmc.ncbi.nlm.nih.gov/articles/PMC3661547)). Better-off groups tend to acquire EBV later, which raises their risk of IM.

**Genetic risk factors (host susceptibility)**

*HLA class I.* McAulay et al. studied markers near the HLA class I region (J Clin Invest 2007;117:3042, [PMC1994627](https://pmc.ncbi.nlm.nih.gov/articles/PMC1994627)).
- Alleles of the microsatellites D6S510 and D6S265 were "significantly associated with development of IM".
- Alleles of the SNPs rs2530388 and rs6457110 were more frequent in IM than in EBV-seronegative controls. For rs6457110, the T allele was found in 70% of IM patients versus 57% of controls (P = 0.038).
- Patients carrying the associated allele "displayed higher EBV titers and milder IM symptoms".

*Twin evidence.* In the California Twin Program, pairwise concordance for IM was 12.1% in identical (monozygotic) pairs versus 6.1% in non-identical (dizygotic) pairs. The hazard ratio for the unaffected co-twin was 1.9 (95% CI 1.1–3.4). The authors call this "compatible with a heritable contribution" (Hwang et al., Epidemiol Infect 2012, [PMC3845900](https://pmc.ncbi.nlm.nih.gov/articles/PMC3845900)).

*Genome-wide association study (GWAS).* Tian et al. (Nat Commun 2017, PMID [28928442](https://pubmed.ncbi.nlm.nih.gov/28928442/)) fine-mapped the HLA region across 23 infections, including mononucleosis. They report that virus-induced infections are "mainly associated with class I molecules". I did not find a GWAS specific to IM published in 2023–2024.

*Inborn errors of immunity (rare).* These cause severe, fulminant or fatal IM:
- *SH2D1A*, which encodes SAP and causes XLP1 (Coffey et al., Nat Genet 1998, PMID [9771704](https://pubmed.ncbi.nlm.nih.gov/9771704/)).
- *XIAP*, which causes XLP2.
- *ITK*, *MAGT1*, *CTPS1*, *CD27*, *CD70*, *CORO1A* and *RASGRP1* (Latour & Winter, Front Immunol 2018, [PMC6004768](https://pmc.ncbi.nlm.nih.gov/articles/PMC6004768)).

**Protective factors**
- *HLA-A\*02* is associated with lower risk of EBV-positive Hodgkin lymphoma (OR 0.70 per allele). The added Hodgkin risk after IM disappeared in people carrying HLA-A\*02 (Hjalgrim et al., PNAS 2010, [PMC2851961](https://pmc.ncbi.nlm.nih.gov/articles/PMC2851961)). Whether HLA-A\*02 protects against IM itself was not shown directly here.
- *Early childhood infection:* acquiring EBV in childhood, which is usually symptom-free, effectively protects against IM. This is inferred from the age dependence above.

**Gene–environment interaction**
- *Sequence of events toward Hodgkin lymphoma:* host HLA-A type, then IM, then EBV-positive Hodgkin lymphoma. The authors conclude that "HLA class I-restricted EBV-specific cytotoxic T-cell responses and events in the early immune response to EBV infection in IM play critical roles" (PMC2851961).
- *Multiple sclerosis:* IM is also a risk factor for MS (see §11).
- *Databases:* CTD and other GxE databases were not queried.

---

## 3. Phenotypes

**Case definition used in research:** at least 2 of sore throat, cervical lymphadenopathy, fever and fatigue (PMID 23100562).

| Phenotype | Type | Suggested HPO label | Frequency / characteristics | Source |
|---|---|---|---|---|
| Pharyngitis / sore throat | Symptom | Pharyngitis | Sensitivity 0.81–0.83, but not specific | Ebell, JAMA 2016, PMID [27115266](https://read.qxmd.com/read/27115266/) |
| Fatigue | Symptom | Fatigue | Sensitive but not specific; can last weeks to months | PMID 27115266; [CDC](https://www.cdc.gov/epstein-barr/about/mononucleosis.html) |
| Fever | Sign | Fever | Common | CDC |
| Cervical lymphadenopathy, especially posterior cervical | Sign | Cervical lymphadenopathy | Posterior nodes make IM more likely; absent nodes make it less likely | PMID 27115266 |
| Splenomegaly | Sign | Splenomegaly | Common | CDC |
| Hepatomegaly | Sign | Hepatomegaly | Less common | CDC |
| Rash, and rash after aminopenicillins | Sign | Maculopapular exanthema | 29.5% with amoxicillin (95% CI 18.5–42.6) vs about 90% historically with ampicillin | Chovel-Sella, Pediatrics 2013 ([Healio](https://www.healio.com/news/pediatrics/20130501/idc0413chovelsella_10_3928_1081_597x_20130401_04_1132857)) |
| Lymphocytosis with atypical lymphocytes | Lab | Lymphocytosis; Atypical lymphocytes | ≥10% atypical lymphocytes gives a likelihood ratio of 11.4. >50% lymphocytes plus >10% atypical gives specificity 0.99 | PMID 27115266 |
| Elevated liver enzymes | Lab | Elevated hepatic transaminase | 58–100% of outpatients | AAFP 2023, PMID [36689975](https://pubmed.ncbi.nlm.nih.gov/36689975/) |
| Inverted CD8:CD4 ratio | Lab | Decreased CD4:CD8 ratio | A hallmark of IM | [PMC6542544](https://pmc.ncbi.nlm.nih.gov/articles/PMC6542544) |

**Onset:** adolescents and young adults, with symptoms appearing about 4–6 weeks after infection (CDC). **Severity:** usually mild to moderate and self-limited. **Course:** acute, lasting several weeks.

**Quality of life:** prolonged fatigue is the main burden. In adolescents, 13%, 7% and 4% met chronic fatigue syndrome criteria at 6, 12 and 24 months after IM. Female sex and more severe fatigue predicted this outcome (Katz et al., Pediatrics 2009, PMID [19564299](https://pubmed.ncbi.nlm.nih.gov/19564299/)). No studies using EQ-5D or SF-36 in IM were retrieved.

---

## 4. Genetic/Molecular Information

**Causal genes:** none in the host, because IM is infectious. The causal agent is the EBV genome. The relevant viral entry proteins are gp350, gp42, gH/gL and gB (§6).

**Pathogenic variants and ACMG classification:** not applicable to IM as a whole. ClinVar and gnomAD apply only to the inborn-error genes.
- *SH2D1A* lies on Xq25, has 4 exons and encodes a 128-amino-acid protein (SAP).
- XLP mutations make SAP lose function: "SAP cDNAs isolated from … patients with X-linked lymphoproliferative syndrome did not bind SLAM" (search summary of Sayos et al.).
- For *ITK*, *MAGT1*, *CTPS1* and *RASGRP1*, "LOF mutations … impair T-cell activation and proliferation after TCR triggering" (Béziat & Jouanguy 2021, via [PMC8721657](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721657)).
- These variants are germline: X-linked for *SH2D1A* and *XIAP*, autosomal recessive for most of the others.

**Modifier loci:** the HLA class I region (rs6457110, rs2530388, D6S510, D6S265) and HLA-A\*01 / A\*02 (§2). A linkage and association study found that at least 2 HLA loci affect anti-EBNA-1 antibody levels ([PMC4099326](https://pmc.ncbi.nlm.nih.gov/articles/PMC4099326)).

**Epigenetics and chromosomal abnormalities:** I retrieved no IM-specific human data. (EBV latency programs are controlled epigenetically, but that literature was not retrieved here.)

---

## 5. Environmental Information

- **Infectious agent:** Epstein–Barr virus, a lymphocryptovirus (gammaherpesvirus). The NCBI Taxon ID was not retrieved; look it up as "Human gammaherpesvirus 4".
- **Other agents that can cause a mononucleosis-like illness:** cytomegalovirus (ICD B27.1) and acute HIV. People with HIV risk factors should be tested for HIV ([MSD Manual](https://www.msdmanuals.com/professional/infectious-diseases/herpesviruses/infectious-mononucleosis?ruleredirectid=743)).
- **Lifestyle:** kissing and sexual behaviour drive transmission (PMID 23100562).
- **Toxins and occupation:** no data retrieved.
- **Drug interaction:** aminopenicillins can trigger rash (§3).

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. **Oral exposure to EBV in saliva.** Transmission happens through saliva ([CDC](https://www.cdc.gov/epstein-barr/about/mononucleosis.html)). This **leads to** infection of tonsillar B cells and epithelium.
2. **Entry into cells.** Two branches:
   - **B cells:** viral gp350 binds CD21 (CR2), gp42 binds HLA class II, and this triggers fusion by gH/gL and gB ([PMC9529843](https://pmc.ncbi.nlm.nih.gov/articles/PMC9529843)).
   - **Epithelial cells:** these lack CD21 and HLA class II, so gH/gL binding to αv integrins acts as the trigger instead ([PMC7317989](https://pmc.ncbi.nlm.nih.gov/articles/PMC7317989)).

   **Results in** latent infection that transforms and expands B cells, plus lytic replication.
3. **Epithelium amplifies the virus.** Shedding dynamics "strongly implicate the epithelium as a site where virus is amplified prior to shedding" (Hadinoto et al., PLoS Pathog 2009, [PMC2708605](https://pmc.ncbi.nlm.nih.gov/articles/PMC2708605)). This **leads to** high viral load in saliva and blood. The incubation period is about 4–6 weeks (CDC).
4. **Innate control first.** NK cells provide initial control, and human NK cells limit CD8+ T-cell expansion. This was shown in humanized mice ([PMC6542544](https://pmc.ncbi.nlm.nih.gov/articles/PMC6542544)), so in humans it is inferred.
5. **Massive expansion of CD8+ T cells.** "Selective and massive expansion of a few dominant clones of CD8+ T cells is an important feature of the primary response" (Callan et al., Nat Med 1996;2:906, [Nature](https://www.nature.com/articles/nm0896-906)). The expansions are limited to CD8 cells, and some clones persist about a year (PMID [11067931](https://pubmed.ncbi.nlm.nih.gov/11067931)). This **results in** the atypical lymphocytosis and inverted CD8:CD4 ratio.
6. **Symptoms come from the immune response.** The lymphocytosis infiltrates lymphoid organs, causing lymphadenopathy, tonsillar swelling and splenomegaly, and is accompanied by fever and fatigue. The idea that the immune response causes the symptoms is supported by HLA findings: patients with the risk allele had *higher* viral titres but *milder* symptoms and fewer lymphocytes (PMC1994627). This step is therefore inferred from correlation.
   - **Branch, splenic infiltration:** leads to splenomegaly and, rarely, rupture.
   - **Branch, liver:** leads to transaminitis.
   - **Branch, tonsillar swelling:** leads to airway obstruction.
   - **Branch, failure of cytotoxic killing (for example SAP/SLAM or MAGT1/NKG2D defects):** leads to uncontrolled B-cell proliferation, hemophagocytic lymphohistiocytosis (HLH) or fatal IM (PMC6004768).
7. **Resolution.** Clinical recovery follows, with lifelong latency in memory B cells. A history of IM is linked to later EBV-positive Hodgkin lymphoma and multiple sclerosis (§11).

### Mechanism checklist
- **Pathways:** SLAM–SAP signalling; NKG2D (MAGT1-dependent); CD27–CD70 co-stimulation of EBV-specific T cells (PMC6004768).
- **Suggested GO labels:** viral entry into host cell; T cell proliferation; natural killer cell mediated cytotoxicity; antigen processing and presentation via MHC class I.
- **Suggested CL labels:** B cell; memory B cell; CD8-positive, alpha-beta cytotoxic T cell; natural killer cell; epithelial cell of tonsil.
- **Single-cell and other omics:** not retrieved in this session.

---

## 7. Anatomical Structures Affected

Suggested UBERON labels: palatine tonsil, pharynx, cervical lymph node, spleen, liver, peripheral blood.
- **Primary sites:** oropharynx, tonsils, cervical lymph nodes and spleen.
- **Secondary sites:** liver; nervous system (ICD subcodes exist for polyneuropathy and meningitis).
- **Body systems:** lymphatic/immune, hepatic, upper respiratory.
- **Cell level:** see the CL labels in §6.
- **Subcellular, GO cellular component labels:** plasma membrane (entry via receptors) and nucleus (episome during latency).
- **Lymphadenopathy:** typically bilateral, cervical, often posterior (PMID 27115266).

---

## 8. Temporal Development

- **Onset:** acute, after about 4–6 weeks of incubation. Peak ages are 15–24 years.
- **Course:** self-limited, lasting several weeks. Fatigue can persist for months.
- **Remission:** spontaneous.
- **Critical periods:**
  - Most splenic ruptures happen in the first 3 weeks (Bartlett et al., Injury 2016, 85 cases).
  - Military data suggest the risk lasts longer, and support delaying return to contact sport until about 31 days after symptom onset (Sylvester et al.; summarized in [PMC6822211](https://pmc.ncbi.nlm.nih.gov/articles/PMC6822211)).
  - Return-to-play decisions should be individualized.

---

## 9. Inheritance and Population

**Incidence:** about 500 per 100,000 persons per year, highest at ages 15–24 (PMC6822211).

**Seroprevalence in the US (NHANES, n = 9,338), Balfour et al., J Infect Dis 2013, PMID [23868878

A safety check stopped my report on infectious mononucleosis (EBV) partway through section 9, so it is incomplete. I'm not going to rewrite or resume it.

Before it stopped, I had gathered sources for sections 1–8 and found these with PubMed IDs (PMIDs):
- **Reviews:** 25774295, 26424648
- **Minnesota student cohort:** 23100562
- **Teen chronic fatigue after mono:** 19564299
- **Diagnostic accuracy review (JAMA):** 27115266
- **US childhood seroprevalence:** 23868878
- **Multiple sclerosis risk after EBV infection (Science 2022):** 35025605
- **gp350 vaccine trial:** 18190254
- **X-linked lymphoproliferative disease gene (SH2D1A):** 9771704
- **Rhesus monkey model:** 9197263

Other sources had only a PMC number or DOI: the HLA class I study, the twin study, the HLA-A and Hodgkin lymphoma study, and the meta-analysis of multiple sclerosis after mono.

- **Not covered:** sections 9–15 (population, diagnostics, prognosis, treatment, prevention, other species, model organisms). The search results above were not written up for these.
- **No causal human gene:** this is an infectious disease caused by EBV. Host genes only change risk or severity.
- **Ontology terms are labels only:** I couldn't look up the HPO, GO, CL, UBERON and NCIT IDs in this run. Look them up before entering them.
- **Identifiers checked:** only ICD-10 B27.0. MeSH, ICD-11 and Orphanet are unchecked.

To get the rest, run a new request for sections 9–15 on their own.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 22 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26424648` *(abstract only)*: "sore throat, cervical lymph node enlargement, fatigue and fever, most often in adolescents and young adults, lasting several weeks"
  - closest text in source: "Infectious mononucleosis is a clinical entity characterized by sore throat, cervical lymph node enlargement, fatigue, and fever most often seen in adolescents and young adults and lasting several weeks"
- `PMC:PMC4670567` *(abstract only)*: "sore throat, cervical lymph node enlargement, fatigue and fever, most often in adolescents and young adults, lasting several weeks"
  - closest text in source: "Infectious mononucleosis is a clinical entity characterized by sore throat, cervical lymph node enlargement, fatigue, and fever most often seen in adolescents and young adults and lasting several weeks"
- `PMC:PMC8721657` *(abstract only)*: "LOF mutations … impair T-cell activation and proliferation after TCR triggering"
  - closest text in source: "Seven viruses are currently recognized as oncogenic in humans: Epstein Barr virus (EBV), Kaposi sarcoma-associated herpesvirus (KSHV, also known as HHV8), human papillomaviruses (HPVs), hepatitis B virus (HBV), hepatitis C virus (HCV), human T-lymphotropic virus-1 (HTLV-1), and Merkel cell polyomavirus (MCPyV)"
- `PMC:PMC2708605` *(abstract only)*: "strongly implicate the epithelium as a site where virus is amplified prior to shedding"
  - closest text in source: "In contrast to B cells, where amplification of the EBV episome occurred even with a replication-defective BZLF1-knockout virus, amplification in AGS cells was dependent upon early lytic cycle gene expression"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0005810` (2 mentions) - the report calls it "MONDO"; MONDO calls it **infectious mononucleosis**, and lists "Mono" among its other names

Every term resolved, and every label the report gave matched.