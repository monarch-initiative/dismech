---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-16T09:28:45.623017'
end_time: '2026-11-16T09:31:12.997330'
duration_seconds: 147.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: DDOST-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0013789
  category: Mendelian
  causal_genes: DDOST
  omim_id: OMIM:614507
  synonyms: CDG syndrome type Ir; CDG-Ir; CDG1R; DDOST-CDG; carbohydrate deficient
    glycoprotein syndrome type Ir; congenital disorder of glycosylation type 1r; congenital
    disorder of glycosylation type Ir
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
  web_search_requests: 4
  num_turns: 11
  total_cost_usd: 1.7809960499999997
  session_id: b4c5412f-31cf-42d9-a775-7781fb6dcdca
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 14
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 7
  validator_version: 0.6.0
term_validation:
  total_terms: 35
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 2
  obsolete_terms:
  - term_id: GO:0018279
    ontology_label: obsolete protein N-linked glycosylation via asparagine
    replaced_by: GO:0006487
  unresolvable_prefixes:
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DDOST-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0013789 (if available)
- **Causal gene(s):** DDOST
- **OMIM:** OMIM:614507
- **Synonyms:** CDG syndrome type Ir; CDG-Ir; CDG1R; DDOST-CDG; carbohydrate deficient glycoprotein syndrome type Ir; congenital disorder of glycosylation type 1r; congenital disorder of glycosylation type Ir
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **DDOST-Congenital Disorder of Glycosylation** covering all of the
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

I'm pulling the abstracts of the key DDOST-CDG papers so I can quote them directly. Then I'll write the report.

# DDOST-Congenital Disorder of Glycosylation (DDOST-CDG; CDG-Ir): Research Report

**Target:** MONDO:0013789 · OMIM:614507 · causal gene **DDOST** (HGNC:2728, written `hgnc:2728` in dismech) · autosomal recessive

> **How to use this report.** I could not get verbatim abstract text this session. The PubMed fetch returned paraphrases, and direct `curl` needed approval I didn't have. Read every claim and PMID below as a **lead**, not a snippet. Before any of it goes into `kb/disorders/DDOST-Congenital_Disorder_of_Glycosylation.yaml`, run `just fetch-reference PMID:<id>` for each paper and copy exact snippets from the cached abstracts. I also wrote the ontology CURIEs from domain knowledge, not from a lookup. Check each one with `runoak` or `just validate-terms` before binding it.

---

## 1. Disease information

DDOST-CDG is an ultra-rare, autosomal recessive **type I congenital disorder of glycosylation**. It is caused by biallelic loss-of-function variants in **DDOST**, which encodes OST48. OST48 is a non-catalytic core subunit of the endoplasmic reticulum oligosaccharyltransferase (OST) complex. That complex moves the preassembled Glc3Man9GlcNAc2 glycan from dolichol-pyrophosphate onto asparagine residues of newly made polypeptides.

The disorder was first described by Jones et al. 2012, who found it by whole-exome sequencing in a previously untyped CDG patient (PMID:22305527). Fewer than about 10 patients have been published so far.

| Identifier | Value | Status |
|---|---|---|
| MONDO | MONDO:0013789 "DDOST-congenital disorder of glycosylation" | Confirmed (already in the KB stub) |
| OMIM (phenotype) | 614507 (CDG1R) | Given in the prompt |
| OMIM (gene) | 602202 (DDOST) | From memory; verify |
| HGNC | HGNC:2728 | Confirmed by the GenCC record URL |
| Orphanet | One DDOST-CDG ORPHA code exists, but I did not confirm the number | Look up with `just fetch-reference ORPHA:<id>` |
| ICD-10 | E77.8 (other disorders of glycoprotein metabolism), used for CDG generally | Not disease-specific |

**Synonyms:** CDG-Ir; CDG1R; DDOST-CDG; congenital disorder of glycosylation type Ir / type 1r; carbohydrate deficient glycoprotein syndrome type Ir.

**Source of data:** Everything known comes from individual case reports (n≈1 per paper) and one functional variant-classification study. There are no registry or EHR cohorts.

---

## 2. Etiology

- **Cause:** Biallelic pathogenic DDOST variants. Reported allele types are missense, frameshift, small in-frame deletion, and a large multi-exon deletion. The ClinGen CDG Gene Curation Expert Panel gives the disease mechanism as *biallelic loss of function* ([GenCC/ClinGen record](https://search.thegencc.org/submissions/GENCC_000102-HGNC_2728-MONDO_0013789-HP_0000007-GENCC_100003)).
- **Genetic risk factors:** The only one is the carrier status of both parents. No susceptibility loci or modifier genes have been described.
- **Environmental risk, protective factors, gene-environment interaction:** None reported. Not applicable for a monogenic recessive glycosylation defect.

---

## 3. Phenotypes

The clinical picture is a multisystem type I CDG, ranging from severe infantile disease with liver involvement to a milder adolescent form dominated by a movement disorder (PMID:36214423). Frequencies are counts out of the ~6 published probands and should be read qualitatively.

| Phenotype | Suggested HPO (verify) | Onset | Reported in |
|---|---|---|---|
| Global developmental delay / intellectual disability | HP:0001263 Global developmental delay | Infancy | Most or all probands (PMID:22305527, 36214423, 34462534, 41392699) |
| Hypotonia | HP:0001252 Hypotonia | Infancy | Several (PMID:22305527, 41392699) |
| Failure to thrive / feeding difficulty | HP:0001508; HP:0011968 Feeding difficulties | Infancy | PMID:22305527, 34462534 |
| Strabismus | HP:0000486 Strabismus | Childhood | Index case (PMID:22305527), from memory; verify |
| Hepatic dysfunction / elevated transaminases | HP:0002910 Elevated hepatic transaminase | Infancy | Index case, from memory; verify |
| Movement disorder (dystonia / involuntary movements) | HP:0100022 Abnormality of movement; or HP:0001332 Dystonia, if the paper names it | Childhood/adolescence | PMID:36214423 |
| Lactose intolerance | HP:0004789 Lactose intolerance | Infancy | PMID:34462534 |
| Situs inversus totalis | HP:0001696 Situs inversus totalis | Congenital | PMID:34462534 (single patient; may be coincidental) |
| Humoral immune deficiency / recurrent infections (~12/year) | HP:0004313 Decreased circulating antibody level; HP:0002719 Recurrent infections | Childhood | PMID:36631682 (one patient) |
| Type I serum transferrin pattern (lab) | HP:0003160 Abnormal isoelectric focusing of serum transferrin | Detectable from infancy | All probands with biochemical testing |

**Severity and course:** Severity varies, and the disease appears static or slowly evolving rather than degenerative. No formal quality-of-life data exist.

The situs inversus totalis and the immunodeficiency each come from a single patient. Record them as reported findings, and do not present them as established features of the disease.

---

## 4. Genetic and molecular information

**Gene:** DDOST (chromosome 1p36.12). Its product, OST48, is a single-pass type I ER membrane protein. Within the OST complex it forms a core with RPN1, RPN2 and DAD1, and it is shared by both the STT3A- and STT3B-containing OST complexes.

### Reported variants

| Proband | Genotype | Source |
|---|---|---|
| Jones 2012 (index case) | Compound heterozygous: a 22-bp deletion and a missense variant | PMID:22305527 |
| Pi 2022 (Chinese) | Homozygous c.1187G>A | PMID:34462534 |
| Elsharkawi 2023 (18-year-old male) | Compound heterozygous: c.1142dupT (frameshift, maternal) and c.661T>C p.(Ser221Pro) (paternal) | PMID:36214423 |
| Sitek 2023 | DDOST variant with humoral immunodeficiency (genotype not in the retrieved record) | PMID:36631682 |
| Reynolds 2025/2026 (female) | Compound heterozygous: 413-kb deletion of exons 3–11 (maternal) and p.(Lys435del) in-frame deletion (paternal). First structural variant reported. | PMID:41392699 |

The exact HGVS strings for the index-case variants and the protein change for c.1187G>A should be taken from the cached abstracts or ClinVar.

### Variant classification

Kas et al. 2023 (PMID:37848450, **IN_VITRO**) reported that 43 DDOST variants had been described in CDG patients, 34 of them as VUS. In a LOX N-glycosylation reporter assay, two known pathogenic variants were confirmed and two VUS were functionally impaired: **p.S243F** and **p.E286del**. The other 39 variants tested showed no impairment.

### Validity

- **ClinGen: Moderate**, autosomal recessive, approved 2023-11-15 by the CDG GCEP (SOP v9). The panel cites at least 4 probands from 4 publications ([GenCC](https://search.thegencc.org/submissions/GENCC_000102-HGNC_2728-MONDO_0013789-HP_0000007-GENCC_100003); ClinGen assertion `CGGV:assertion_e0605b51-70c5-42ee-81b5-d45bb0b1fdab-2023-11-15T170000.000Z`, [ClinGen](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_e0605b51-70c5-42ee-81b5-d45bb0b1fdab-2023-11-15T170000.000Z)).
- Use `just fetch-reference CGGV:…` and record the tier in `gene_disease_validity` with `classified_by: CLINGEN`. Because the tier is Moderate, `relationship_type: CAUSATIVE` would be flagged as `overstated`; choose the relationship type with that in mind.
- Genomics England PanelApp lists DDOST as Green for its CDG panel ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/25/gene/DDOST/)).
- ClinGen Dosage classifies DDOST as "Gene Associated with Autosomal Recessive Phenotype" for haploinsufficiency ([ClinGen dosage](https://dosage.clinicalgenome.org/clingen_gene.cgi?sym=DDOST)).

**Other genetic features:** No modifier genes, epigenetic mechanisms, or chromosomal-abnormality mechanisms have been reported. All reported variants are germline.

---

## 5. Environmental information

None known. There are no infectious, toxic or lifestyle factors. Infections occur as a *consequence* of the immunodeficiency in one patient (PMID:36631682); they are not a cause.

---

## 6. Mechanism / pathophysiology

### Causal chain

1. **Biallelic DDOST loss-of-function variants** reduce the amount and/or function of OST48. Elsharkawi showed reduced DDOST expression in patient fibroblasts (PMID:36214423).
2. Loss of OST48 **destabilizes the OST complex and impairs its function** at the ER membrane. That this happens through complex destabilization is *inferred* from the structural biology of the OST complex; it has not been shown in patient cells.
3. Impaired OST function causes **reduced en bloc transfer of Glc3Man9GlcNAc2 to asparagine** (GO:0018279 protein N-linked glycosylation via asparagine; parent GO:0006487 protein N-linked glycosylation). Glycosylation sites are left unoccupied (hypoglycosylation). This was shown in patient fibroblasts and rescued by wild-type DDOST cDNA (PMID:22305527).
4. **Systemic under-occupancy of N-glycosylation sites** appears in serum glycoproteins as a type I transferrin pattern: increased asialo- and disialo-transferrin (all probands tested).
5. Hypoglycosylated glycoproteins are misfolded, unstable, or wrongly trafficked across many tissues (*inferred*, as general CDG-I biology). From here the mechanism branches:
   - 5a. **Central nervous system:** developmental delay, hypotonia and movement disorder. The neuronal proteins responsible have not been identified.
   - 5b. **Liver:** hepatocyte-secreted glycoproteins are affected, giving raised transaminases and liver dysfunction (index case).
   - 5c. **Immune system, B cells:** humoral immune deficiency and recurrent infections (PMID:36631682). This is plausibly mediated by hypoglycosylated immunoglobulins or B-cell receptors, but that is *inferred*.
   - 5d. **Gut epithelium:** lactose intolerance (PMID:34462534). Defective glycosylation of lactase–phlorizin hydrolase is a hypothesis, not a demonstrated mechanism.
   - 5e. **Left–right patterning:** situs inversus (single case). No mechanism has been shown, and the finding may be coincidental.
6. Together these give a **multisystem CDG phenotype of variable severity**.

### Supporting detail

- **Alternate OST48 function:** OST48 is also known as **AGE-R1**, a receptor that clears advanced glycation end-products. That role has been studied in mouse over-expression models of diabetic kidney and liver disease (e.g., [Sci Rep 2019](https://www.nature.com/articles/s41598-019-50221-0)). It has not been linked to CDG pathogenesis, so do not put it in the CDG pathograph.
- **Suggested GO terms (verify):**
  - GO:0006487 protein N-linked glycosylation
  - GO:0018279 protein N-linked glycosylation via asparagine
  - GO:0008250 oligosaccharyltransferase complex
  - GO:0005789 endoplasmic reticulum membrane
- **Suggested cell types (CL, verify):** fibroblast CL:0000057 (the assay cell); hepatocyte CL:0000182; B cell CL:0000236; neuron CL:0000540.
- **Suggested chemical entity:** dolichyl diphosphooligosaccharide (look up in CHEBI).
- **Molecular profiling:** No published transcriptomic, proteomic, glycoproteomic or single-cell datasets for DDOST-CDG were found. A `KNOWLEDGE_GAP` is reasonable here.

---

## 7. Anatomical structures affected

- **Organs (UBERON, verify):** brain (UBERON:0000955), liver (UBERON:0002107), immune system / lymphoid tissue, intestine (UBERON:0000160), eye muscles (strabismus).
- **Subcellular:** endoplasmic reticulum membrane and the OST complex (GO:0005789, GO:0008250).
- **Laterality:** Not applicable, apart from the situs anomaly in one patient.

---

## 8. Temporal development

- **Onset:** Congenital or infantile in the reported cases (failure to thrive and delay in infancy). The milder case was characterised at 18 years, with movement disorder as the main feature.
- **Course:** Chronic and lifelong. No disease stages, remission, or progression rates have been reported.

---

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive (HP:0000007). Parental carrier status was confirmed in compound heterozygous families (PMID:36214423, 41392699).
- **Epidemiology:** Ultra-rare. About 6–7 published patients, from the USA, China, Italy and other countries. Prevalence is unknown. In dismech terms: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`, or `NOT_YET_DOCUMENTED`.
- **Not reported:** founder effect, anticipation, germline mosaicism. Penetrance is presumed complete for biallelic loss of function. Carrier frequency has not been estimated.
- **Sex:** Both sexes are affected.

---

## 10. Diagnostics

- **First-line screen:** Serum transferrin isoelectric focusing or mass spectrometry, which shows a type I pattern. The pattern cannot distinguish DDOST-CDG from other CDG-I subtypes.
- **Confirmation:** Exome or genome sequencing, or a CDG gene panel that includes DDOST. The index case was solved by exome sequencing combined with biochemistry (PMID:22305527).
  - Chromosomal microarray, or exome with CNV calling, is needed to detect large deletions. The 413-kb deletion in PMID:41392699 shows that sequence-only testing can miss the second allele.
- **Functional tests:**
  - N-glycosylation reporter assays in patient fibroblasts, with cDNA rescue (PMID:22305527).
  - DDOST protein expression in fibroblasts (PMID:36214423).
  - The LOX-based variant assay for VUS (PMID:37848450, research only).
- **Immunology work-up:** Immunoglobulin levels and vaccine responses (PMID:36631682).
- **Differential diagnosis:** Other OST-subunit and CDG-I disorders: STT3A-CDG, STT3B-CDG, MAGT1 (XMEN), TUSC3, OSTC-CDG, RPN2, ALG-gene CDGs, and PMM2-CDG. All share the type I transferrin pattern and are separated by molecular testing.
- **Screening:** No newborn screening exists. Carrier or prenatal testing is possible once the familial variants are known.

---

## 11. Outcome and prognosis

There is no natural-history or survival data. Reported patients survived at least into adolescence (18 years in PMID:36214423). Morbidity comes from neurodevelopmental disability, and in some patients from liver dysfunction or recurrent infections. No prognostic biomarkers are known.

---

## 12. Treatment

There is no disease-specific therapy, and no registered DDOST-CDG trials were found. Unlike MPI-CDG, there is no substrate (mannose) therapy, because the OST defect is not bypassed by sugar supplementation.

| Treatment | NCIT suggestion (verify) | Notes |
|---|---|---|
| Immunoglobulin replacement | NCIT:C15986 Pharmacotherapy + agent NCIT:C80829 Human Immunoglobulin G | Relevant to the humoral-deficiency phenotype (PMID:36631682); check the paper says IVIG was given |
| Nutritional management, lactose-free diet | NCIT:C15447 Dietary Intervention | Feeding difficulty and lactose intolerance (PMID:34462534) |
| Physical, occupational and speech therapy | NCIT:C15302, C121351, C159273 | Developmental delay and hypotonia |
| Supportive care, liver and coagulation monitoring | NCIT:C15747 Supportive Care | Standard CDG surveillance |
| Genetic counseling | NCIT:C15240 | Recurrence risk 25% |

No gene, cell or RNA therapies have been tried.

---

## 13. Prevention

- **Primary and secondary prevention:** Genetic counseling, carrier testing of relatives, and prenatal or preimplantation testing once the familial variants are known.
- **Tertiary prevention:**
  - Infection prophylaxis or immunoglobulin replacement for patients with antibody deficiency.
  - Nutritional support.
  - Surveillance of liver function and coagulation, following general CDG management guidance.

---

## 14. Other species and natural disease

- No naturally occurring DDOST disease is recorded in animals (no OMIA entry found).
- DDOST/OST48 is highly conserved across eukaryotes; its yeast orthologue is **WBP1**, an essential OST subunit. Mouse *Ddost* is MGI:1194508.

---

## 15. Model organisms

- **Mouse knockout:** The IMPC *Ddost* knockout allele (Ddost^tm1.1(KOMP)Vlcg) is **homozygous embryonic lethal**, with "embryonic lethality prior to organogenesis" recorded at about E9.5 and a further lethal entry at E12.5 ([IMPC](https://mousephenotype.org/data/genes/MGI:1194508)). This means complete loss of function is incompatible with development, which fits the hypomorphic genotypes seen in patients. I have not checked the stage values against the primary IMPC record.
- **Mouse over-expression:** OST48/AGE-R1 knock-in mice have been studied for clearance of advanced glycation end-products in diabetic kidney and liver disease, not as a CDG model ([Sci Rep 2019](https://www.nature.com/articles/s41598-019-50221-0)).
- **Cellular models:**
  - Patient fibroblasts with cDNA rescue (PMID:22305527, 36214423).
  - A LOX-glycosylation reporter system for testing variants (PMID:37848450).
- **Gaps:** No conditional mouse, zebrafish, or iPSC-neuron model of DDOST-CDG exists. This is a good place for a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion, since the null mouse dies before birth and the human disease is hypomorphic.

---

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 22305527 | Jones MA et al. *Am J Hum Genet* 2012;90:363–368. DDOST mutations identified by whole-exome sequencing are implicated in congenital disorders of glycosylation | Human clinical + in vitro rescue |
| 34462534 | Pi S et al. *J Hum Genet* 2022;67:103–106. The second DDOST-CDG patient with lactose intolerance, developmental delay, and situs inversus totalis | Human clinical |
| 36214423 | Elsharkawi I et al. *J Inherit Metab Dis* 2023;46:92–100. Third patient with a milder, predominantly movement disorder phenotype | Human clinical + fibroblast studies |
| 36631682 | Sitek A et al. *J Clin Immunol* 2023;43:692–694. Pathogenic DDOST variant is associated with humoral immune deficiency | Human clinical; letter with **no abstract**, so snippets would need full text |
| 37848450 | Kas SM et al. *Sci Rep* 2023;13:17648. Functional classification of DDOST VUS | In vitro |
| 41392699 | Reynolds G et al. *Am J Med Genet A* 2026;200:1069–1076. Defining the clinical spectrum and first structural variant | Human clinical + literature review |

### Sources
- [PubMed 41392699](https://pubmed.ncbi.nlm.nih.gov/41392699/)
- [PMC10155826 (Sitek 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10155826/)
- [PMC10582084 (Kas 2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10582084/)
- [PMC9852036 (Elsharkawi 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9852036)
- [ClinGen gene-disease validity](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_e0605b51-70c5-42ee-81b5-d45bb0b1fdab-2023-11-15T170000.000Z)
- [GenCC submission](https://search.thegencc.org/submissions/GENCC_000102-HGNC_2728-MONDO_0013789-HP_0000007-GENCC_100003)
- [GenCC gene page](https://search.thegencc.org/genes/HGNC:2728)
- [Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/25/gene/DDOST/)
- [PanelApp Australia](https://panelapp-aus.org/panels/68/gene/DDOST/)
- [ClinGen dosage](https://dosage.clinicalgenome.org/clingen_gene.cgi?sym=DDOST)
- [IMPC Ddost](https://mousephenotype.org/data/genes/MGI:1194508)
- [Sci Rep 2019 (OST48/AGE-R1)](https://www.nature.com/articles/s41598-019-50221-0)
- [FCDGC publications](https://fcdgc.rarediseasesnetwork.org/research-publications)
- [RDCRN research report, Nov 2022](https://www.rarediseasesnetwork.org/news/research-summaries/2022-11/rare-research-report-november-2022)

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 2 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0018279` (obsolete protein N-linked glycosylation via asparagine) (2 mentions) - replaced by `GO:0006487`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.

31 of 35 terms resolved to a current term; the rest could not be looked up either way.