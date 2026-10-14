---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-13T20:27:38.550709'
end_time: '2026-10-13T20:28:44.520655'
duration_seconds: 65.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: BARD1-related Cancer Predisposition
  mondo_id: MONDO:0700267
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 4
  num_turns: 6
  total_cost_usd: 0.7103430000000001
  session_id: aa4f0803-31cb-5b9b-8409-a0195ed1b485
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 11
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 3
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BARD1-related Cancer Predisposition
- **MONDO ID:** MONDO:0700267 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **BARD1-related Cancer Predisposition** covering all of the
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

# BARD1-related Cancer Predisposition: research report

**Read this first.** I ran four web searches in this session. Anything marked **[searched]** comes from those results. Mostly that is search-result abstracts and snippets, and I did not open the full texts. Anything marked **[memory]** is background recall with no source checked in this run. Treat it as a lead and verify it before it goes into a KB entry. I did not write any PMIDs from memory, because an unchecked PMID is a defect under this repo's rules. Where I have a source, I give the DOI or PMC ID that appeared in the results. The MONDO ID in the template (MONDO:0700267), the OMIM, Orphanet and ClinGen identifiers, and the HP/GO/CL/UBERON/NCIT term suggestions were **not looked up**. Do not bind any of them until they are read from the ontology.

## Scope and lump/split calls

- This entry is the **germline** predisposition syndrome. It should stay separate from the somatic breast, ovarian and neuroblastoma entries it predisposes to (design-decisions §3a).
- **Lump/split call 1.** Adult breast cancer predisposition (moderate-penetrance, heterozygous) and the proposed pediatric neuroblastoma predisposition are different clinical entities with different evidence strength. I would keep one germline entry, with the two as separate phenotype arms. The pediatric arm would be flagged as lower-confidence unless a ClinGen or guideline source supports it. A split into two entries is defensible.
- **Lump/split call 2.** OMIM carries a neuroblastoma susceptibility locus, "Neuroblastoma, Susceptibility To, 5" [searched: findzebra listing only; OMIM number not verified]. Whether this and the breast predisposition belong in one disorder is unresolved.
- The Mendelian lane also needs an explicit decision on **biallelic BARD1**. I found no source on it in this session.

## 1. Disease information

- BARD1 encodes the obligate heterodimer partner of BRCA1. The heterodimer has E3 ubiquitin ligase activity and acts in homologous recombination repair. **[memory]**
- Heterozygous germline loss-of-function variants confer **moderate-penetrance breast cancer risk**, with an apparently stronger association with triple-negative disease. The clinical framing is "BRCA1-like partner, but lower penetrance" **[memory]**.
- Identifiers and synonyms: not retrieved. The MONDO ID given in the template is unverified. HGNC for BARD1 is not looked up. Neuroblastoma susceptibility 5 appears in a findzebra listing [searched], but I did not verify the OMIM number.
- Data source class: aggregated cohort and case-control resources (germline sequencing series, gnomAD-controlled comparisons), not EHR-derived.

## 2. Etiology

- **Causal factor.** Heterozygous germline BARD1 pathogenic variants, mostly truncating **[memory]**.
- **Breast cancer risk estimate [searched].**
  - Source class: primary literature, single cohort. Rofes et al., *Genes* 2021, DOI 10.3390/genes12020150 (PMC7911518), a Spanish hereditary breast and ovarian cancer cohort of 4,015 patients compared with gnomAD controls.
  - Truncating variants overall: OR 3.78 (95% CI 2.10–6.48; p = 1.16 × 10⁻⁵).
  - Hereditary breast cancer group: OR 4.18 (95% CI 2.10–7.70).
  - Triple-negative breast cancer (TNBC) enrichment versus other subtypes: OR 5.40 (95% CI 1.77–18.15; p = 0.001).
  - The authors conclude BARD1 is a moderate-penetrance breast cancer gene with a stronger TNBC association.
  - A payer policy summary states BARD1 variants confer about 2–3× general-population breast cancer risk [searched: payer document, not primary]. This is lower than the single-cohort OR above. The two estimates differ in design and are not directly comparable.
- Large consortium estimates (Dorling and CARRIERS/BCAC-type studies, and the Weber-Lassalle series) were **not retrieved**. My search for them returned nothing relevant. Those are the primary sources the entry should cite for effect sizes.
- **Pediatric arm: neuroblastoma [searched].**
  - Common-variant GWAS: Capasso et al. 2009, *Nat Genet*. Six SNPs at 2q35 in the BARD1 locus associated with high-risk neuroblastoma (397 cases/2,043 controls, replicated in 189 cases/1,178 controls). Source class: primary literature, common-variant association. It does **not** establish a high-penetrance Mendelian effect.
  - Rare-variant enrichment: a cohort of 786 patients reported BARD1 as the most significantly enriched gene for pathogenic or likely pathogenic germline variants (OR 32.30; 95% CI 6.44–310.35), and linked germline P/LP variants to worse overall survival. Source class: primary literature, cohort. I saw only an abstract snippet, and the confidence interval is very wide.
  - A bioRxiv preprint (2023) reports that common and rare neuroblastoma-associated BARD1 variants lower BARD1 mRNA and increase DNA damage, and that BARD1-LoF isogenic cells repair Cas9-induced damage less efficiently. Source class: **preprint**, not peer-reviewed in this retrieval. Check whether a peer-reviewed version exists.
- Environmental and protective factors: no BARD1-specific sources found. Do not import BRCA1/2 assumptions. Gene-environment interaction: no data retrieved.

## 3. Phenotypes

Everything below is **[memory]** unless stated. Frequencies and HPO bindings need checking against HPO, Orphanet and the primary literature.

| Phenotype | Notes |
|---|---|
| Breast carcinoma, adult onset | Main phenotype. Triple-negative subtype enriched [searched, Rofes 2021]. |
| Neuroblastoma, childhood | Susceptibility arm; high-risk subset in the GWAS [searched]. |
| Ovarian, pancreatic and other cancers | Weaker, uncertain. I did not retrieve sources. |

- There is no known non-cancer syndromic phenotype. Do not invent a quality-of-life section; I have no data.
- Pediatric framing: onset age and penetrance for the neuroblastoma arm are not established in what I retrieved. Say so in the entry rather than imply a childhood surveillance indication.

## 4. Genetic and molecular information

- Gene: BARD1, chromosome 2q35. 2q35 is [searched] (Capasso GWAS). The HGNC ID (lowercase `hgnc:` form in this repo) must be looked up.
- Variants: mostly truncating or LoF. Missense variants in the RING and BRCT domains are largely VUS **[memory]**. Interpretation of missense variants is a known difficulty. I have no sourced classification data.
- Origin: germline. Mechanism: haploinsufficiency is supported for neuroblastoma-associated variants by the preprint [searched]. For breast cancer, LoF is the working model **[memory]**.
- ClinGen validity: **not found** in my search, so no `gene_disease_validity` assertion can be copied. Check `just genes-clingen-gaps` and the cached CGGV records before writing one. Do not assign a tier.
- Modifier genes, epigenetics, chromosomal abnormalities: nothing retrieved.

## 5. Environmental information

None BARD1-specific retrieved. Leave environmental blocks empty rather than borrowing from BRCA1.

## 6. Mechanism (ordered causal chain)

1. A germline heterozygous LoF variant in BARD1 reduces BARD1 dosage. Haploinsufficiency is **demonstrated in neuroblastoma-variant cell and expression data [searched, preprint]**. It is inferred for breast cancer.
2. Reduced BARD1 destabilises or reduces the BRCA1–BARD1 heterodimer, which is **[memory]**, mechanistically expected but not sourced here.
3. The result is a homologous recombination repair defect and increased DNA damage. The preprint supports reduced repair of Cas9-induced damage in BARD1-LoF cells [searched, in vitro].
4. Unrepaired damage and genomic instability follow. This is supported in mouse by McCarthy et al. 2003 (*Mol Cell Biol*; PMC162231 appeared in results): Bard1-null embryos die at E7.5–E8.5 from impaired proliferation, and mutant cells show increased aneuploidy [searched]. Evidence source: model organism.
5. Loss of the second allele or other cooperating events leads to tumour initiation. The two-hit step in human carriers is **inferred**, not shown in anything I retrieved.
6. The tissue pattern is breast, with a TNBC bias, and neuroblastoma in the pediatric arm. In mouse, mammary-specific conditional Bard1 loss produces basal-like mammary carcinomas with frequency, latency and histology indistinguishable from conditional Brca1 loss [searched; snippet only, the paper identity is "likely Shakya et al. 2008", unconfirmed]. This parallels the human TNBC enrichment. It is a model-organism result and the mouse is a full conditional knockout, not a heterozygous germline model.

Suggested GO/CL terms for this chain would be DNA repair and homologous recombination, ubiquitin ligase activity, and mammary epithelial cell and sympathetic neuroblast lineages. All are **unverified** and need ontology lookup.

## 7. Anatomical structures

Breast (mammary epithelium) and the sympathetic nervous system or adrenal medulla (neuroblastoma). Ovary is uncertain. No lateralisation data retrieved. UBERON/CL bindings: not looked up.

## 8. Temporal development

- Breast: adult onset. Specific age distribution not retrieved.
- Neuroblastoma: infancy to early childhood, as is general for the tumour **[memory]**. The age at diagnosis for BARD1 carriers specifically was not retrieved.

## 9. Inheritance and population

- Autosomal dominant with reduced penetrance **[memory]**.
- Population frequency, founder variants, carrier frequency, sex ratio: not retrieved. gnomAD was used as the control set in the Rofes study [searched].
- Penetrance numbers: only the 2–3× relative-risk statement [searched, payer document] and the OR above. Absolute lifetime risk was not retrieved. The UK genomics hub text mentions a ≥30% estimated lifetime risk as a threshold for considering mastectomy [searched], which is a decision threshold and not a BARD1-specific penetrance figure.

## 10. Diagnostics

- Multigene hereditary cancer panel testing. BARD1 is included on common panels **[memory]**.
- No BARD1-specific biomarker, imaging, or histology criteria retrieved, though TNBC histology is a reported association [searched].
- Variant interpretation: no ClinGen VCEP or ACMG-specific BARD1 guidance retrieved.

## 11. Prognosis

Not retrieved for adult breast carcinoma. For neuroblastoma, one cohort linked germline P/LP variants to worse overall survival [searched, abstract snippet].

## 12. Treatment and surveillance

- Surveillance: NCCN recommends annual mammogram and breast MRI from age 40 for carriers of BARD1, RAD51C and RAD51D [searched; quoted in an NSGC news item, secondary source. Verify against the NCCN guideline itself, which I did not open].
- Risk-reducing mastectomy: evidence described as insufficient or uncertain in several secondary sources (UK Genomics Education hub, FORCE, a payer summary) [searched]. The UK hub says it may be considered for higher-risk variants with an estimated lifetime risk of 30% or more.
- PARP inhibitors: BARD1 carriers' response is **not established** in anything I retrieved. I did not search for it, so do not assert either way.
- Candidate NCIT terms for surveillance and counselling procedures: not looked up. Use the repo's term-lookup workflow.
- Clinical trials: none searched.

## 13. Prevention

Enhanced breast screening as above. No evidence found for chemoprevention. Cascade testing and genetic counselling apply generally **[memory]**. For children, I found no surveillance recommendation for neuroblastoma in BARD1 carriers. The entry should record that gap.

## 14–15. Other species and model organisms

- Mouse: constitutive Bard1 knockout is embryonic lethal (E7.5–E8.5), delayed to about E9.5 when p53 is also removed [searched, McCarthy 2003, PMC162231]. Conditional mammary knockout gives basal-like carcinomas [searched, snippet; PMC2365565 appeared among results but I did not confirm it is that paper]. Conditional alleles exist (Columbia listing, MGI alleles MGI:2668394 and MGI:4939693 appeared in results, unverified).
- Fidelity caveat for a `modeled_mechanisms` link: the null and conditional-null models do not reproduce the human heterozygous moderate-penetrance state. They support the BRCA1–BARD1 tumour-suppressor mechanism but only partially recapitulate the human phenotype.
- Natural disease in other species, OMIA, zebrafish, Drosophila and cell lines: not searched.

## Gaps to close before curation

1. Primary consortium effect sizes for breast cancer (BCAC/CARRIERS, Dorling, Weber-Lassalle). Not found in my search.
2. ClinGen gene-disease validity for BARD1 and its cached CGGV record.
3. Primary NCCN text, plus any ESMO/ACMG/ERN guidance.
4. Peer-reviewed status of the neuroblastoma preprint, and the exact citation for the 786-patient cohort.
5. Penetrance, ovarian and pancreatic risk, and tumour-spectrum data.
6. Identifiers: MONDO, OMIM, Orphanet, HGNC, and every HPO/GO/CL/UBERON/NCIT term.

## Sources

- [Rofes et al., *Genes* 2021, BARD1 and TNBC in a Spanish HBOC cohort (PMC7911518)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7911518/)
- [Capasso et al. 2009 GWAS and later neuroblastoma results: bioRxiv preprint on BARD1 haploinsufficiency](https://www.biorxiv.org/content/10.1101/2023.01.31.525066.full.pdf)
- [Capasso 2009 record, Birmingham](https://research.birmingham.ac.uk/en/publications/common-variations-in-bard1-influence-susceptibility-to-high-risk-/)
- [Germline pathogenic variants in neuroblastoma enriched in BARD1 (Mount Sinai record)](https://scholars.mssm.edu/en/publications/germline-pathogenic-variants-in-neuroblastoma-patients-are-enrich/)
- [NSGC news item quoting NCCN screening](https://www.nsgc.org/Newsroom/NSGC-In-the-News/Post/women-with-mutations-in-low-moderate-breast-cancer-genes-may-benefit-from-earlier-breast-cancer-screening)
- [UK NHS Genomics Education, BARD1](https://www.genomicseducation.hee.nhs.uk/genotes/knowledge-hub/bard1/)
- [FORCE, BARD1 risk management](https://facingourrisk.org/info/hereditary-cancer-and-genetic-testing/hereditary-cancer-genes-and-risk/genes-by-name/bard1/risk-management)
- [Payer policy 204126, germline genetic testing](https://www.fepblue.org/-/media/PDFs/Medical-Policies/2024/January/Medical-Policies-Dec-2023/New-Add/204126-Germline-Genetic-Testing-for.pdf)
- [McCarthy et al. 2003, Bard1 knockout (PMC162231)](https://pmc.ncbi.nlm.nih.gov/articles/PMC162231)
- [Conditional Bard1 mammary tumour study (PMC2365565, unconfirmed)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2365565)
- [Columbia conditional Bard1 allele listing](https://inventions.techventures.columbia.edu/technologies/conditional-mouse-model-for--CU23026)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

1 of 3 terms resolved to a current term; the rest could not be looked up either way.