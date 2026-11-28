---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T00:30:50.761891'
end_time: '2026-11-27T00:34:37.524799'
duration_seconds: 226.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Oral Tuberculosis
  mondo_id: MONDO:0005887
  category: Infectious Disease
  causal_genes: not recorded
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
  web_search_requests: 11
  num_turns: 18
  total_cost_usd: 0.8041985850000001
  session_id: aad14886-fcb0-4d02-8d2f-1207c3d52db0
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 25
  retrieval_calls: 23
  assistant_text_blocks: 4
citation_count: 27
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 6
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:22517424
  quotes_not_checkable: 1
  relevance_assessed: 28
  on_topic: 16
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 4
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  service_unreachable: 4
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oral Tuberculosis
- **MONDO ID:** MONDO:0005887 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Oral Tuberculosis** covering all of the
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

Let me try PubMed E-utilities directly for PMIDs and abstracts.

I've got the core sources and PMIDs. Next I'm pulling short exact quotes from the key abstracts, then I'll write the report.

All quotes below are copied exactly from the abstractText fields I already fetched. Each is under 125 characters, and I shortened several by cutting the end of a longer sentence.

**(a) PMID 35785411** (Oral and maxillofacial tuberculosis: A systematic review)
- Male %, mean age: "Of these patients, 192 (63.7%) were male, with an average age of 39.6 ± 19.8 (15 months to 81 years)."
- Tongue %: "The tongue (n = 80/26.6%) represented the most common affected site, followed by the mandible (n = 43/14.3%)."
- Histology %: "Histopathological analysis showed a granulomatous inflammation in most cases (n = 156/63.1%)."
- Treatment and death: "Antituberculosis therapy was used in 244 cases (100.0%) and 5.2% of patients died."

**(b) PMID 26366156** (Tuberculosis of the oral cavity: an uncommon but still a live issue)
- Prevalence and secondary to pulmonary: the abstract has no prevalence figure. The closest sentence is "Oral TB manifestations are uncommon and usually secondary to pulmonary changes."
- Ulcer presentation: "They predominantly appear as ulcers."
- Systemic therapy: "Anti-tubercular systemic therapy is required in every patient diagnosed with oral TB"

**(c) PMID 33456244** (Primary oral tuberculosis: A case series of a rare disease)
- Misdiagnosis and mimicry: "its clinical features can be nonspecific that mimics other diseases and is usually misdiagnosed"

**(d) PMID 37842328** (Primary Tuberculosis of Buccal and Labial Mucosa)
- Solitary ulcer: "The commonest oral TB lesion is solitary ulceration with undermined edges, usually on the tongue"

**(e) PMID 25453225** (Mendelian susceptibility to mycobacterial disease: genetic, immunological, and clinical features of inborn errors of IFN-γ immunity)
- IFN-γ: "The nine gene products are physiologically related, as all are involved in IFN-γ-dependent immunity."
- Penetrance: "Most of these inborn errors do not show complete clinical penetrance for the case-definition phenotype of MSMD."

**(f) PMID 32181218** (Oral Manifestations in HIV-TB Co-infected Patients)
- 77.5%: "A total of 77.5% patients coinfected with HIV-TB had shown oral manifestations"

**(g) PMID 22517424** (Revisiting the role of the granuloma in tuberculosis)
- Granuloma promoting spread: "that implicate the innate immune mechanisms of the tuberculous granuloma in the expansion and dissemination of infection"

The URLs read are the four listed in my earlier report. For full abstract text, fetch the same API URLs directly.

**Scope and interpretation.** This report covers **oral tuberculosis**, MONDO:0005887: tuberculosis of the mouth, tongue and salivary glands. It is an infection caused by *Mycobacterium tuberculosis* complex. **It has no causal gene.** No OMIM entry or Mendelian gene is recorded for it, and none should be expected. Host genetics only change susceptibility to mycobacteria in general (Section 4).

**Methods and limits.** Sources came from web search and Europe PMC record retrieval. PubMed and PMC full-text pages could not be fetched (cookie and reCAPTCHA blocks). Abstract quotes were therefore taken from Europe PMC abstract records, and each is cut to under 125 characters. Ontology terms are given as labels only, because their IDs were not checked in this session. Statements that rely on general tuberculosis knowledge rather than a source retrieved here are marked **[not retrieved]**.

---

## 1. Disease Information

**Overview.** Oral tuberculosis is a rare form of extrapulmonary TB affecting the oral soft tissues, the jaws and the salivary glands.
- It is usually **secondary** to pulmonary TB. "Oral TB manifestations are uncommon and usually secondary to pulmonary changes" (Krawiecka & Szponar 2015, **PMID 26366156**).
- It most often appears as a chronic, painful ulcer that does not heal.
- **Primary** oral TB, with no other focus of disease, is rarer still (PMID 33456244; PMID 34932768).

**Identifiers** (from the MONDO record mirrored by the [HDR UK Phenotype Library](https://phenotypes.healthdatagateway.org/api/v1/ontology/node/MONDO:0005887/) and from [MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D014393)):

| Resource | ID |
|---|---|
| MONDO | MONDO:0005887 (parent categories: "digestive system disorder" MONDO:0004335; "mouth disorder" MONDO:0006858) |
| MeSH | D014393, "Tuberculosis, Oral": "Tuberculosis of the mouth, tongue, and salivary glands." |
| DOID | DOID:402 |
| UMLS | C0041323 |
| MedGen | 52888 |
| GARD | 0024251 |
| SNOMED CT | 235067001 |
| ICD-9 | 017.90; 528.9 |
| OMIM / Orphanet / ICD-10 / ICD-11 | Not retrieved in this session. No OMIM entry is expected for an infectious disease. |

**Synonyms:** tuberculosis of the mouth; oral TB; tuberculosis of the oral cavity (MeSH entry term "Tuberculosis, Oral"). Related subtypes in the clinical literature include lingual (tongue) TB, gingival TB and tuberculous sialadenitis (PMID 34932768; PMID 37842328).

**Source of the data.** Everything here is aggregated disease-level literature. Most of it comes from case reports and case series, pooled in one systematic review of 301 cases (PMID 35785411). No EHR-derived cohorts were found.

## 2. Etiology

**Cause.** Infection of the oral tissues with *M. tuberculosis* complex. There are two routes:
- **Secondary oral TB:** bacilli in infected sputum reach mucosa that is already broken, or the disease spreads through the blood. A 2025 South African HIV case series (University of Pretoria [repository](https://repository.up.ac.za/server/api/core/bitstreams/be0f157e-1508-458a-94cb-c6df66ed97b9/content)) states that oral TB "usually results from secondary bacterial inoculation of oral mucosa breached by any ulceration or minor masticatory trauma."
- **Primary oral TB:** direct inoculation in a person with no other TB focus (PMID 33456244).

**Risk factors**
- **Active pulmonary TB.** In a four-case series, every secondary case had "cavitary lesions in lungs and were sputum positive for acid fast bacilli" (Dogra et al., [Indian J Otolaryngol](https://link.springer.com/doi/10.1007/s12070-012-0489-6)).
- **Immunosuppression and HIV.** In 200 people with HIV–TB coinfection, "A total of 77.5% patients coinfected with HIV-TB had shown oral manifestations" (**PMID 32181218**). That figure covers all oral lesions, not oral TB specifically. The authors relate oral lesions to CD4 count.
- **Diabetes mellitus.** It was the most common comorbidity (12 of 78 patients) in an Indian cross-sectional TB cohort that included one case of primary oral TB ([JIAOMR 2011](https://doaj.org/article/e28263056db849ff97632194a890ec10)).
- **Local factors:**
  - mucosal trauma, poor oral hygiene, extraction sockets and leukoplakia ([UP repository](https://repository.up.ac.za/server/api/core/bitstreams/be0f157e-1508-458a-94cb-c6df66ed97b9/content); PMID 26366156). The full text supporting this list was not verified.
  - multidrug-resistant strains, which Krawiecka & Szponar suggest may increase oral TB ([PMC4565830](https://pmc.ncbi.nlm.nih.gov/articles/PMC4565830)).
- **Sex and age.** In the systematic review, 63.7% of patients were male and the mean age was 39.6 years (PMID 35785411).
- **Genetic risk.** Inborn errors of IFN-γ immunity (Mendelian susceptibility to mycobacterial disease, MSMD) predispose to mycobacterial disease. Some MSMD patients develop disease from *M. tuberculosis* itself (PMID 25453225; PMID 30264912). No genetic risk factor specific to oral TB has been reported.

**Protective factors**
- Treating pulmonary TB promptly removes the source of infected sputum.
- An intact oral epithelium, saliva and the oral flora are commonly described as making the mouth resistant to infection. This rests on a review-level statement whose full text was not verified (PMC4565830).
- BCG vaccination and other primary prevention: see Section 13 **[not retrieved]**.

**Gene–environment interaction.** Not documented for oral TB. In MSMD, defects in IFN-γ-dependent immunity combine with exposure to mycobacteria to cause disease, with incomplete penetrance (PMID 25453225).

## 3. Phenotypes

| Phenotype (suggested HPO label) | Type | Frequency / notes | Source |
|---|---|---|---|
| Oral ulcer, typically solitary, painful and non-healing with undermined edges | Sign | Most common presentation. "The commonest oral TB lesion is solitary ulceration with undermined edges, usually on the tongue" | PMID 37842328; PMID 26366156 ("They predominantly appear as ulcers.") |
| Tongue lesion (glossal ulcer or nodule) | Sign | The most common site: "The tongue (n = 80/26.6%) represented the most common affected site" | PMID 35785411 |
| Jaw bone involvement (osteomyelitis) | Sign | Mandible in 14.3% | PMID 35785411 |
| Gingival lesion, enlargement or granular appearance | Sign | Typical in primary oral TB in children and young adults | PMID 33456244; [PMC10569891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569891/) |
| Palatal, buccal or labial mucosal ulcer or swelling | Sign | Reported | PMID 33456244; PMID 37842328 |
| Cervical lymphadenopathy | Sign | Accompanies primary lesions | [PMC10569891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569891/) |
| Oral pain, odynophagia, dysphagia | Symptom | Common with ulcers. Not quantified. | PMID 35785411 (abstract: "painful ulcerated lesion"; quote not obtained verbatim) |
| Constitutional symptoms (fever, weight loss, night sweats, cough) | Symptom | Mainly in secondary cases with pulmonary disease **[not quantified]** | Dogra et al. |
| Granulomatous inflammation on biopsy | Lab / pathology | 63.1% of cases | PMID 35785411 |
| Lesion that clinically resembles squamous cell carcinoma | Sign | A frequent source of misdiagnosis | PMID 33456244 |

**Characteristics**
- **Onset:** adult (mean age 39.6 years; range 15 months to 81 years). Primary lesions are more common in the young and secondary lesions in middle-aged and older people ([PMC10569891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569891/)).
- **Course:** chronic and slowly progressive without treatment.
- **Severity:** variable.
- **Quality of life:** pain, difficulty eating and speaking, and weight loss. No EQ-5D or SF-36 data specific to oral TB were found.

## 4. Genetic / Molecular Information

- **Causal genes:** none. This is not a Mendelian disease, so pathogenic variants, allele frequencies, somatic versus germline origin, chromosomal abnormalities and epigenetic data specific to oral TB are **not applicable or not available**.
- **Host susceptibility genes, applicable to mycobacterial disease generally:**
  - **MSMD genes** in the IL-12/IL-23–IFN-γ axis, including **IL12RB1** (MIM 601604). IL-12Rβ1 deficiency is the most common MSMD form (PMID 23864330).
  - Bustamante et al. state that "The nine gene products are physiologically related, as all are involved in IFN-γ-dependent immunity" and "Most of these inborn errors do not show complete clinical penetrance" (**PMID 25453225**).
  - The 2014–2018 update reports disease-causing mutations "in 11 genes" underlying "21 different genetic disorders", and adds SPPL2A, RORC and JAK1 (**PMID 30264912**; PMID 32025907).
  - These are mainly autosomal recessive loss-of-function or autosomal dominant dominant-negative variants **[mode details not retrieved here]**.
- **Pathogen genetics:** resistance mutations bear on treatment. The *rpoB* rifampicin-resistance region is detected by Xpert MTB/RIF (Section 10).

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* (and the wider complex, including *M. bovis*, by inference). NCBI Taxonomy IDs were not retrieved here.
- **Exposures:** close contact with infectious pulmonary TB; settings with high TB burden.
  - The 2025 WHO report lists 16% of notified TB as extrapulmonary ([WHO GTB 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-diagnosis-and-treatment/2-1-case-notifications)).
- **Lifestyle:** smoking and tobacco chewing, alcohol, malnutrition and poor oral hygiene are cited in the case literature as local predisposing factors **[not verified in full text]**.

## 6. Mechanism / Pathophysiology

**Causal chain**
1. Viable *M. tuberculosis* reaches the oral mucosa, by one of two routes:
   - **Branch A (secondary):** infected sputum from pulmonary TB, or spread through blood or lymph.
   - **Branch B (primary):** direct exogenous inoculation.
2. Breaks in the epithelium (trauma, extraction, inflammation) **lead to** bacilli entering the submucosa. An intact epithelium is thought to resist infection; this step is inferred from the case literature ([UP repository](https://repository.up.ac.za/server/api/core/bitstreams/be0f157e-1508-458a-94cb-c6df66ed97b9/content)).
3. Tissue macrophages take up the bacilli, which **results in** intracellular bacterial persistence and recruitment of more macrophages. This is shown in the zebrafish model (PMID 24973748) and extrapolated to the oral site.
4. Macrophages aggregate and change into epithelioid cells and multinucleated Langhans giant cells, which **leads to** granuloma formation. "The granuloma… is the hallmark structure of tuberculosis" (PMID 22517424, paraphrased).
5. Antigen-specific T cells produce IFN-γ under IL-12 control, and TNF maintains the granuloma. Together these **lead to** macrophage activation and partial containment ([PMC4561401](https://pmc.ncbi.nlm.nih.gov/articles/PMC4561401) and other reviews; human genetic evidence in PMID 25453225).
   - **Branch:** when IFN-γ immunity is deficient (MSMD, HIV with CD4 depletion), containment fails and the disease is more extensive.
6. Excess TNF or strong T-cell immunity **leads to** macrophage necrosis, which then **results in** caseous necrosis and extracellular bacterial growth. "Macrophage necrosis promotes more bacterial growth than macrophage apoptosis" (PMID 22517424, figure caption). The granuloma may itself drive "the expansion and dissemination of infection" (**PMID 22517424**).
7. Necrosis breaking through the surface mucosa **results in** a chronic ulcer with undermined edges. In bone it **results in** tuberculous osteomyelitis of the mandible or maxilla. This step is inferred from clinical and pathological correlation (PMID 35785411).
8. Spread along lymphatics **leads to** cervical lymphadenitis. Clinically, the result is pain, dysphagia and a non-healing ulcer.

**Mechanism checklist**
- **Pathways:** IL-12/IL-23–IFN-γ signalling; TNF signalling.
- **Suggested GO terms:**
  - granuloma formation
  - macrophage activation
  - interferon-gamma-mediated signaling pathway
  - tumor necrosis factor-mediated signaling pathway
  - phagocytosis
  - necrotic cell death
- **Suggested CL terms:** macrophage; epithelioid cell; multinucleated giant cell (Langhans); CD4-positive alpha-beta T cell; neutrophil.
- **Omics, single-cell and CRISPR data specific to oral TB:** none found.

## 7. Anatomical Structures Affected

- **Primary sites, with suggested UBERON labels and frequencies from PMID 35785411:**
  - tongue (26.6%)
  - mandible (14.3%)
  - gingiva
  - palate
  - buccal mucosa
  - lip
  - also reported: maxilla, salivary glands (parotid, submandibular), tonsil (PMC12910516)
- **Secondary or associated involvement:**
  - lung (the source in secondary disease)
  - cervical lymph nodes
- **Body systems:** digestive (oral cavity), respiratory, lymphatic, musculoskeletal (jaw bone).
- **Tissues:** stratified squamous mucosa, lamina propria and submucosa, skeletal muscle (tongue), bone.
- **Suggested GO cellular component terms:** phagosome; phagolysosome.
- **Laterality:** usually a single, solitary lesion; not lateralized.

## 8. Temporal Development

- **Onset:** insidious and chronic. Lesions are typically present for weeks to months before diagnosis, and they fail to heal with conservative treatment (PMID 37842328).
- **Age:** mostly adults; primary oral TB occurs in children and young adults ([PMC10569891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569891/)).
- **Course:** progressive without treatment. Remission is treatment-induced, and all four primary cases in one series resolved on antituberculous therapy (PMID 33456244).
- **Critical window:** early biopsy of any non-healing ulcer avoids delayed diagnosis, which matters most where carcinoma is suspected.

## 9. Inheritance and Population

- **Inheritance:** not applicable; this is an acquired infection. Penetrance, anticipation, founder effects and carrier frequency are **not applicable**.
- **Frequency:**
  - Oral lesions occur in about **0.5–1.5% of TB patients** ([PMC4565830](https://pmc.ncbi.nlm.nih.gov/articles/PMC4565830)). Other sources give a range of 0.05–5%.
  - Primary oral TB is reported as under 1% of extrapulmonary cases ([PMC8687499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8687499/)).
  - In a Brazilian TB cohort of 121 patients, 1 (0.8%) had oral ulceration ([search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC3914305/)).
- **Incidence per 100,000:** not available for oral TB specifically.
- **Geography:** mirrors the overall TB burden. Most published cases come from South Asia, Latin America and sub-Saharan Africa.
- **Sex ratio:** male-predominant, 63.7% male, about 1.8:1 (PMID 35785411).
- **Age:** mean 39.6 ± 19.8 years (PMID 35785411).

## 10. Diagnostics

**Biopsy and histopathology** are the cornerstone of diagnosis.
- Typical findings are epithelioid granulomas with Langhans giant cells, with or without caseous necrosis.
- Granulomatous inflammation was seen in 63.1% of cases (PMID 35785411).

**Microbiology on tissue**
- **Ziehl–Neelsen (acid-fast) stain:** low sensitivity. It was positive in 31.25% (5/16) of an orofacial series ([IJPM 2021](https://doaj.org/article/020b694dc26a42d3aaa412749c1aefdc)).
- **Culture:** slow, and often not reported in the case literature **[not retrieved]**.

**Molecular tests**
- Nested PCR and Xpert MTB/RIF on oral biopsies were positive in 2 and 3 caseating-granuloma samples respectively; the authors call them useful auxiliary methods ([JORDI](https://jordi.emnuvens.com.br/revista/article/view/257)).
- PCR was used in primary oral TB cases (PMID 33456244).

**Immunological tests**
- Tuberculin skin test (Mantoux) was used in PMID 33456244.
- Interferon-γ release assays (IGRA) **[not retrieved]**.

**Work-up for a primary focus**
- Chest radiograph or CT.
- Sputum AFB smear or Xpert testing (Dogra et al.).

**Differential diagnosis**
- squamous cell carcinoma (the most important mimic; PMID 33456244)
- traumatic ulcer
- aphthous ulcer
- deep fungal infections such as histoplasmosis
- syphilis
- Crohn disease and orofacial granulomatosis
- sarcoidosis
- lymphoma
- granulomatosis with polyangiitis
- PMID 26366156 recommends that TB be considered for atypical or non-healing ulcers.

**Genetic testing**
- Not used to diagnose oral TB.
- Worth considering only for MSMD work-up in severe, recurrent or disseminated mycobacterial disease, using a gene panel or exome for IL12RB1, IFNGR1/2, STAT1 and others (PMID 38535546).

**Screening:** no programme exists for oral TB. Oral lesions have been proposed as a screening signal in HIV–TB coinfection (PMID 32181218).

## 11. Outcome / Prognosis

- **Mortality:** "Antituberculosis therapy was used in 244 cases (100.0%) and 5.2% of patients died" (**PMID 35785411**). Deaths probably reflect disseminated or HIV-associated disease (inferred).
- **Recovery:** oral lesions usually heal fully on standard therapy (PMID 33456244).
- **Complications:**
  - jaw osteomyelitis and pathological changes in bone (PMID 35785411)
  - scarring, tissue loss and lymphadenitis
  - transmission, when the disease is secondary to pulmonary TB
- **Prognostic factors:** HIV with a low CD4 count (PMID 32181218), drug resistance and delay in diagnosis. Formal prognostic biomarkers have not been described.

## 12. Treatment

**Systemic antituberculous therapy is mandatory.** "Anti-tubercular systemic therapy is required in every patient diagnosed with oral TB" (**PMID 26366156**). Topical treatment is adjuvant only.

**Drug-susceptible TB**
- **Standard regimen:** 2 months of isoniazid + rifampicin + pyrazinamide + ethambutol, then 4 months of isoniazid + rifampicin (2HRZE/4HR). This is the standard regimen in WHO Module 4 ([WHO 2022](https://www.who.int/publications/i/item/9789240048126)).
- **4-month alternative (2HPMZ/2HPM):** isoniazid + rifapentine + moxifloxacin + pyrazinamide for people aged 12 or older. WHO restricts it to **pulmonary** DS-TB, so its use in extrapulmonary oral TB is outside the guideline (inferred).
  - In Study 31/ACTG A5349 it was non-inferior, with cure in 84.5% versus 85.4% and grade ≥3 adverse events in 18.8% versus 19.3% ([tbksp.who.int](https://tbksp.who.int/en/node/1926)).

**Drug-resistant TB:** MDR/RR-TB regimens under WHO Module 4 **[details not retrieved]**.

**Pharmacogenomics:** NAT2 acetylator status affects isoniazid toxicity **[not retrieved in this session]**.

**Supportive care**
- analgesia
- topical anaesthetic or antiseptic rinses
- nutritional support
- treatment of HIV with antiretroviral therapy (ART)
- surgery is limited to biopsy and debridement of necrotic bone

**Adverse events:** hepatotoxicity (H, R, Z); peripheral neuropathy (H); optic neuritis (E); rifampicin drug eruptions. Rifampicin eruptions on the lips were seen in an Indian cohort ([JIAOMR](https://doaj.org/article/e28263056db849ff97632194a890ec10)).

**Not applicable:** gene, cell and RNA therapies, targeted therapy and immunotherapy. No oral-TB-specific trials were found.

**Suggested NCIT intervention labels:** Isoniazid; Rifampin; Pyrazinamide; Ethambutol; Rifapentine; Moxifloxacin; Biopsy; Antiretroviral therapy.

## 13. Prevention

- **Primary prevention:**
  - TB infection control
  - treatment of contacts and TB preventive therapy
  - BCG vaccination, which mainly protects children against severe forms **[not retrieved]**
  - oral hygiene and avoiding mucosal trauma in people with TB (inferred)
- **Secondary prevention:**
  - biopsy of non-healing oral ulcers
  - chest imaging when oral TB is found
  - attention to oral lesions in people with HIV (PMID 32181218)
- **Tertiary prevention:**
  - completing the full course with adherence support
  - drug susceptibility testing
  - HIV care
- **Genetic counselling:** relevant only to MSMD families.

## 14. Other Species / Natural Disease

- No oral-TB-specific veterinary literature was retrieved.
- *M. bovis* causes TB in cattle and is zoonotic, for example through unpasteurized milk **[not retrieved; general knowledge]**.
- *M. marinum* naturally infects fish and forms granulomas like those of human TB (PMID 24973748).
- There is no OMIA entry; the disease is not Mendelian.

## 15. Model Organisms

**There is no model of oral TB specifically.** General TB models:

| Model | Recapitulation | Limitations | Source |
|---|---|---|---|
| Zebrafish larvae and adults infected with *M. marinum* | Macrophage aggregates and granulomas. Transparent larvae allow live imaging, and macrophages alone are enough to start granulomas. Used for drug and host-directed screening. | Not easily inbred; granulomas do not calcify | PMID 24973748; [PMC4871865](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4871865/) |
| Mouse (C57BL/6, BALB/c) infected with *M. tuberculosis* | Extensive genetic tools, including knockouts (e.g., *Ifng*, *Tnf*, *Il12b*) | Granulomas "comparatively diffuse and fail to caseate" | PMID 24973748 |
| C3HeB/FeJ mouse | Necrotic, caseating lesions | Limited genetic tools | PMID 24973748 |

Other models are **not retrieved** here: guinea pig, rabbit, non-human primate, and in vitro macrophage or organoid models. No oral-inoculation model was found.

---

### Key evidence items

| PMID | Type | Quote |
|---|---|---|
| 35785411 | Human, systematic review (301 cases) | "192 (63.7%) were male, with an average age of 39.6 ± 19.8"; "The tongue (n = 80/26.6%)…"; "granulomatous inflammation in most cases (n = 156/63.1%)"; "5.2% of patients died" |
| 26366156 | Human, review | "usually secondary to pulmonary changes"; "They predominantly appear as ulcers." |
| 37842328 | Human, case report and review | "solitary ulceration with undermined edges, usually on the tongue" |
| 33456244 | Human, case series | "nonspecific that mimics other diseases and is usually misdiagnosed" |
| 32181218 | Human, cross-sectional (n=200) | "77.5% patients coinfected with HIV-TB had shown oral manifestations" |
| 25453225 | Human genetics, review | "all are involved in IFN-γ-dependent immunity" |
| 22517424 | Model and human, review | "the expansion and dissemination of infection" |
| 24973748 | Model organism, review | Zebrafish–*M. marinum* granuloma model |

### Sources
- [PubMed 35785411](https://www.pubmed.gov/35785411/)
- [PMC4565830](https://pmc.ncbi.nlm.nih.gov/articles/PMC4565830)
- [PMC7802837](https://pmc.ncbi.nlm.nih.gov/articles/PMC7802837)
- [PMC10569891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569891/)
- [PMC8687499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8687499/)
- [PMC12910516](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12910516/)
- [Dogra et al.](https://link.springer.com/doi/10.1007/s12070-012-0489-6)
- [UP repository case series](https://repository.up.ac.za/server/api/core/bitstreams/be0f157e-1508-458a-94cb-c6df66ed97b9/content)
- [MONDO via HDR UK](https://phenotypes.healthdatagateway.org/api/v1/ontology/node/MONDO:0005887/)
- [MeSH D014393](https://meshb.nlm.nih.gov/record/ui?ui=D014393)
- [WHO GTB 2025 notifications](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-diagnosis-and-treatment/2-1-case-notifications)
- [WHO Module 4](https://www.who.int/publications/i/item/9789240048126)
- [tbksp 4-month regimen](https://tbksp.who.int/en/node/1926)
- [PMC7055335](https://pmc.ncbi.nlm.nih.gov/articles/PMC7055335)
- [JIAOMR 2011](https://doaj.org/article/e28263056db849ff97632194a890ec10)
- [PMC3914305](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3914305/)
- [IJPM 2021](https://doaj.org/article/020b694dc26a42d3aaa412749c1aefdc)
- [JORDI](https://jordi.emnuvens.com.br/revista/article/view/257)
- [PMC4357480](https://pmc.ncbi.nlm.nih.gov/articles/PMC4357480)
- [PMC6438774](https://pmc.ncbi.nlm.nih.gov/articles/PMC6438774)
- [PMC4104692](https://pmc.ncbi.nlm.nih.gov/articles/PMC4104692)
- [PMC10975294](https://pmc.ncbi.nlm.nih.gov/articles/PMC10975294)
- [Nature Rev Immunol 2012](https://www.nature.com/articles/nri3211.pdf)
- [PMC4561401](https://pmc.ncbi.nlm.nih.gov/articles/PMC4561401)
- [PMC4073268](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4073268/)
- [PMC4871865](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4871865/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 2 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 28 |
| On topic | 16 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:22517424` *(abstract only)*: "The granuloma… is the hallmark structure of tuberculosis"
  - closest text in source: "The granuloma, which is a compact aggregate of immune cells, is the hallmark structure of tuberculosis"
- `PMID:22517424` *(abstract only)*: "Macrophage necrosis promotes more bacterial growth than macrophage apoptosis"
  - Text part not found as substring: 'Macrophage necrosis promotes more bacterial growth than macrophage apoptosis' (note: only abstract available for PMID:22517424, full text may contain this excerpt)

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1007/s12070-012-0489-6`: "cavitary lesions in lungs and were sputum positive for acid fast bacilli"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |

### Terms the ontology service could not be reached for

4 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0005887` (5 mentions)
- `MONDO:0004335` (1 mention)
- `MONDO:0006858` (1 mention)
- `DOID:402` (1 mention)

No term could be looked up either way, so nothing here was confirmed or contradicted.