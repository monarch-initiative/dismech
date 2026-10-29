---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-18T23:03:15.402162'
end_time: '2026-10-18T23:07:34.809269'
duration_seconds: 259.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Striatal Degeneration, Autosomal Dominant 2
  mondo_id: MONDO:0014835
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
  - claude-opus-5-5
  web_search_requests: 8
  num_turns: 17
  total_cost_usd: 2.304860495
  session_id: 447377e2-9ffd-4783-a5cd-c156baf050d8
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 5
  relevance_assessed: 14
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0044637
    reported_labels:
    - Recessive PDE10A dyskinesia
    ontology_label: infantile-onset generalized dyskinesia with orofacial involvement
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Striatal Degeneration, Autosomal Dominant 2
- **MONDO ID:** MONDO:0014835 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Striatal Degeneration, Autosomal Dominant 2** covering all of the
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

I've gone through the 12 cached PDE10A abstracts in the worktree and found the landmark Mencacci 2016 paper. Next I'm reading its full text for the clinical and functional details.

# Striatal Degeneration, Autosomal Dominant 2 (ADSD2; PDE10A-related childhood-onset chorea with bilateral striatal lesions): research report

**Scope.** This report covers only the **heterozygous (dominant)** PDE10A disease. Biallelic PDE10A disease is a separate entity: infantile-onset generalized dyskinesia with orofacial involvement (MONDO:0044637, OMIM 616921). It appears here only as a differential diagnosis.

**How it was put together.** The report draws on four sources:
- 12 PubMed abstracts already cached in this worktree (`references_cache/`).
- The open-access full text of Mencacci et al. 2016 (PMC4833291), the founding paper.
- The draft entry `kb/disorders/Striatal_Degeneration_Autosomal_Dominant_2.yaml`.
- Targeted web searches.

**Evidence quality.** Text in quotation marks is copied from a cached abstract or from the Mencacci 2016 full text. Statements I could not check against a primary source are flagged **[unverified]**. The evidence base is very small: about 3 founding patients plus a few families. Most sections therefore record the absence of data rather than findings.

---

## 1. Disease information

**Overview.** ADSD2 is an ultra-rare neurological disorder. Hyperkinetic movements, mainly chorea, begin in the first decade of life. Development and cognition are normal, and the course is only slightly progressive. Brain MRI shows **symmetrical bilateral striatal T2 hyperintensity**, which sets it apart from benign hereditary chorea. It is caused by heterozygous missense variants in the regulatory **GAF-B domain of PDE10A**. PDE10A is a dual cAMP/cGMP phosphodiesterase that is highly and selectively expressed in striatal medium spiny neurons (MSNs).

Founding description (Mencacci et al. 2016, PMID:27058447):
> "Here, we used whole-exome sequencing to unravel the underlying genetic cause in three unrelated individuals with a very similar and unique clinical presentation of childhood-onset chorea and characteristic brain MRI showing symmetrical bilateral striatal lesions."

**Identifiers**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014835, *striatal degeneration, autosomal dominant 2* |
| OMIM (phenotype) | 616922 ([LOVD disease page](https://databases.lovd.nl/shared/diseases/05191)) |
| OMIM (gene) | 610652 (PDE10A) |
| MedGen | C4310791 |
| Gene | PDE10A, HGNC:8772 (`hgnc:8772` in dismech), chromosome 6q27 |
| GenCC | PDE10A–ADSD2 rated **Strong**, autosomal dominant (via MedGen/GenCC aggregation) |
| Orphanet | DisGeNET links the disease name to an Orphanet source, but I could not confirm an ORPHA code **[unverified]** |
| ICD-10/ICD-11 | No specific code. G25.5 ("Other chorea") is the nearest ICD-10-CM bucket **[suggested mapping, not an official one]** |
| MeSH | No specific heading. Use Chorea (D002819) and Phosphoric Diester Hydrolases/genetics |
| GeneReviews | No chapter, per a PubMed `genereviews[book]` search recorded in the draft notes |

**Synonyms:** ADSD2; striatal degeneration, autosomal dominant 2; PDE10A-related (dominant) childhood-onset chorea with bilateral striatal lesions; childhood-onset chorea with bilateral striatal lesions.

**Data provenance:** all knowledge comes from aggregated published case reports and series, plus in vitro and mouse work. There are no EHR-derived or registry data.

**Naming caution:** "ADSD1" is the unrelated **PDE8B**-related adult-onset parkinsonian striatal degeneration (MONDO:0012205). The two share a series name but differ in gene, age of onset and phenotype.

---

## 2. Etiology

- **Cause:** monogenic. Heterozygous germline missense variants in the PDE10A GAF-B (cAMP-binding regulatory) domain.
- **Origin:** mostly **de novo**. The founding paper (PMID:27058447) states: "Notably, the family-based sequencing approach of individuals 1 and 2 directly indicated that both PDE10A mutations had occurred de novo." For individual 3, haplotype analysis only *suggested* a de novo origin, because the parents were deceased.
- **Familial dominant transmission** has also been documented (PMID:29130591): "We report a family with multiple affected individuals with childhood onset chorea, striatal abnormalities, and a novel heterozygous mutation, c.1001T>G(p.F334C) in PDE10A which was identified by exome sequencing." A Japanese family is described as familial in its title (PMID:29165877, *A familial case of PDE10A-associated childhood-onset chorea with bilateral striatal lesions*); that paper has no abstract.
- **Risk factors:** the only one is carrying a GAF-B variant. No susceptibility loci, modifier genes, or environmental, lifestyle or occupational factors have been reported.
- **Protective factors:** none reported.
- **Gene–environment interactions:** none reported. CTD and GWAS Catalog have nothing disease-specific.

---

## 3. Phenotypes

| Phenotype | Suggested HPO | Type | Onset | Course | Frequency | Key evidence |
|---|---|---|---|---|---|---|
| Chorea (generalized; choreoathetosis in one family) | HP:0002072 *Chorea*; HP:0001266 *Choreoathetosis* **[verify]** | Sign | 5–10 years | Scarcely progressive | All reported cases (very frequent) | PMID:27058447; PMID:29130591 |
| Bilateral symmetrical striatal T2 hyperintensity (posterolateral putamen) | HP:0031206 *Striatal T2 hyperintensity* | Imaging | From childhood | Evolves: swelling with restricted diffusion, then atrophy | 3/3 founding cases; reported in the familial cases | PMID:27058447 |
| Putaminal atrophy / striatal degeneration | HP:0040140 *Degeneration of the striatum* | Imaging | Adolescence/adulthood | Late stage | 2/3 founding cases (ages 22 and 53 at scan) | PMID:27058447 |
| Normal development and cognition (a negative feature, important for the differential) | — | — | — | — | 3/3 | PMID:27058447 |
| Adult-onset levodopa-responsive parkinsonism, freezing and falls, abnormal DaT-SPECT | HP:0002548 *Parkinsonism with favorable response to dopaminergic medication* | Sign | Fifth decade | — | 1 individual; possibly coincidental | PMID:27058447 |
| Anxiety | HP:0000739 *Anxiety* **[verify]** | Behavioural | — | — | 1/3 founding cases | Mencacci Table 1 |
| Diurnal fluctuation of chorea | No exact HPO term; consider qualifier `temporality: DIURNAL` | Sign | Childhood | Fluctuating | 1 case report | PMID:28949041 (title only, no abstract) |
| Dystonia (e.g. cervical) | HP:0001332 *Dystonia* **[verify]** | Sign | — | — | Single conference abstract, an adult with subtle putaminal hyperintensity ([MDS abstract](https://www.mdsabstracts.org/abstract/a-rare-case-of-pde10a-associated-dystonia-with-bilateral-striatal-lesions/)) | Not peer-reviewed |

**Supporting quotes from the founding paper (PMID:27058447):**
- "all three individuals presented in childhood (age of onset between 5 and 10 years) with a scarcely progressive movement disorder dominated by chorea. Developmental milestones were normal, and there were no other major neurological features, in particular intellectual disability or cognitive decline."
- "However, within the striatum in all three individuals, brain MRI consistently showed bilateral T2 hyperintensity (Figure 1), which is an atypical finding for BHC."
- "Interestingly, individual 3, who is currently 60 years old, developed levodopa-responsive parkinsonism with freezing and falls in the fifth decade."

**Cohort context.** In a 14-centre cohort of 140 children with complex hyperkinetic disorders (PMID:36054588), "chorea predominated in ADCY5-, ATP1A3-, FOXG1-, NKX2.1-, SLC2A1-, GNAO1-, and PDE10A-related disorders". That cohort pools dominant and recessive PDE10A cases.

**Quality of life.** No EQ-5D, SF-36 or PROMIS data exist. Given the normal cognition and slow course, the main functional burden is presumed to be motor (chorea interfering with fine motor tasks, gait and social participation), plus anxiety in one patient. This is an inference, not measured data.

---

## 4. Genetic and molecular information

**Causal gene:** PDE10A (HGNC:8772; OMIM 610652; 6q27). The founding variants use reference transcript NM_001130690.2.

**Reported pathogenic variants (all heterozygous missense in GAF-B)**

| Variant (NM_001130690.2) | Origin | Patients/families | Population data | Source |
|---|---|---|---|---|
| c.898T>C p.(Phe300Leu) | De novo; recurrent on two different haplotypes | 2 unrelated (British) | Absent from ExAC and in-house databases (~75,000 individuals); CADD 28.7 | PMID:27058447 |
| c.1000T>C p.(Phe334Leu) | De novo | 1 (Dutch) | Absent; CADD 31.0 | PMID:27058447 |
| c.1001T>G p.(Phe334Cys) | Familial, segregating | 1 Indian family, multiple affected | — | PMID:29130591 |
| Variants in PMID:28949041 (de novo, Italian) and PMID:29165877 (Japanese family) | — | — | — | No abstracts; variants not confirmed here **[unverified]** |

**Further details**
- **ClinVar/ACMG:** I did not check ClinVar classifications for these variants. Run a lookup before citing a classification.
- **Constraint:** the founding paper reports a residual variation intolerance score of −0.98 (top 8.8% most intolerant), pLI 1.00 and missense Z = 3.78. Residues Phe300 and Phe334 are "completely conserved down to invertebrate species."
- **Germline vs somatic:** germline (heterozygous). Somatic mosaicism has not been reported.
- **Functional consequence:** loss of **allosteric cAMP stimulation**, with basal catalytic activity preserved (see section 6). Overexpressed mutant protein also misfolds and aggregates. The variants are best described as "GAF-B regulatory loss of function" with a possible dominant-negative component through homodimerization, which has been proposed but not tested.
- **Domain is not destiny.** A **homozygous** GAF-B variant, p.Asp295Asn, causes the *recessive* phenotype with normal MRI (PMID:36805523): "Although these individuals displayed a clinical phenotype attributed to the recessive GAF-A mutations, they revealed a bi-allelic GAF-B mutation (c.883G > A:p. D295 N; p.Asp295Asn) that was segregated with all affected individuals."
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported. No CNV or structural-variant cases are known.

---

## 5. Environmental information

No environmental, lifestyle or infectious factors have been reported. No CTD chemical–disease associations are specific to ADSD2. **Not applicable.**

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Heterozygous GAF-B missense variant** (Phe300Leu, Phe334Leu or Phe334Cys) alters phenylalanines deep in the cAMP-binding pocket. This is supported by modelling, not by direct binding measurements (PMID:27058447, built on the GAF-B crystal structure PMID:18477562). It **leads to** impaired cAMP binding at GAF-B. Impaired binding is *inferred*: binding affinity was not measured.
2. **Branch A: loss of allosteric activation.** Basal PDE activity is unchanged, but cAMP no longer stimulates the catalytic domain. With 1-NO-cAMP, wild-type activity rises about 2.7-fold, an effect "almost completely lost for both mutant PDE10As" (in vitro, COS-7 cells). This **results in** a PDE10A that cannot ramp up cyclic-nucleotide breakdown when cAMP rises.
3. **Branch B: misfolding, aggregation and mislocalization.** Mutant PDE10A leaves the plasma membrane and forms cytoplasmic and perinuclear aggregates in about 75% of transfected cells, with p62 and ubiquitin recruitment and autophagic clearance (PMID:31871190; HEK293 cells and rat striatal neurons, overexpression). This **leads to** loss of correctly compartmentalized PDE10A. A *proposed* dominant-negative effect on wild-type protein, through dimers, is untested.
4. **Reduced effective striatal PDE10A.** PET with a PDE10A ligand ([11C]IMA107) shows reduced PDE10A in the striatum and globus pallidus of carriers (PMID:30345538). That study pooled PDE10A and ADCY5 subjects.
5. **Dysregulated cAMP/PKA signaling in MSNs.** In cells, PKA-substrate phosphorylation after forskolin is dampened by wild-type PDE10A "but not with F300L or F334L forms" (PMID:31871190). The path from this to altered direct/indirect pathway MSN output is *inferred* and not measured in vivo.
6. **Basal ganglia circuit dysfunction leads to chorea.** This step rests on the established model: "Chorea is a hyperkinetic movement disorder resulting from dysfunction of striatal medium spiny neurons" (PMID:27058447, background).
7. **A parallel tissue branch: striatal lesion.** Striatal swelling with restricted diffusion in childhood is followed by putaminal atrophy in adults. Aggregation is *proposed* as the cause, because aggregating GAF-B variants produce lesions while non-aggregating GAF-A variants have normal MRI. This has not been shown in patient tissue. In the F300L knock-in mouse, progressive striatal vacuolation and astrocytosis appear from 1 month of age (MDS 2021 abstract), which supports the link.
8. **Possible late branch: nigrostriatal involvement.** Reduced DaT binding, loss of substantia nigra neuromelanin (PMID:30345538) and one patient with levodopa-responsive parkinsonism suggest it. Whether this is part of the disease or a coincidence is unresolved.

Key quotes:
- "In vitro functional studies showed that neither substitution affects the basal PDE10A activity, but they severely disrupt the stimulatory effect mediated by cAMP binding to the GAF-B domain." (PMID:27058447)
- "In contrast to GAF-A mutants, dominant mutations in the GAF-B domain of PDE10A induce PDE10A misfolding, a common pathological phenotype in many neurodegenerative diseases." (PMID:31871190)
- "Striatal cyclic adenosine monophosphate activity modulates movement and is determined from the balance between its synthesis by adenylate cyclase 5 (ADCY5) and its degradation by phosphodiesterase 10A (PDE10A)." (PMID:30345538)

### Mechanism checklist

- **Pathways:** cAMP/PKA signaling. Also cGMP signaling, which is less studied. Dopamine D1 and adenosine A2A receptor–Gαolf–AC5 signaling in MSNs (KEGG hsa04024 cAMP signaling pathway; Reactome "cAMP degradation by phosphodiesterases").
- **Cellular processes:** protein misfolding and aggregation, aggresome formation, autophagic clearance, loss of membrane localization.
- **Protein dysfunction:** loss of GAF-B allostery, with an intact catalytic domain.
- **Metabolic and immune involvement:** no specific metabolic abnormality reported. Astrocytosis without microgliosis in the mouse; no immune involvement in humans.
- **Tissue damage:** striatal neuron loss and atrophy. Vacuolation is seen in the mouse.
- **Omics, single-cell, spatial, CRISPR screens:** no disease-specific datasets.

### Suggested ontology terms

Labels for terms not in the draft must be checked with `runoak` or the cache before use. CURIEs outside the draft are **[verify]**.

- **GO:** GO:0030552 *cAMP binding* (DECREASED); GO:0004114 *3',5'-cyclic-nucleotide phosphodiesterase activity* (DECREASED, for the stimulated state); GO:0006198 *cAMP catabolic process* (DECREASED); GO:0046069 *cGMP catabolic process* **[verify]**; GO:0016235 *aggresome* **[verify]**; GO:0005886 *plasma membrane* (mislocalization) **[verify]**.
- **CL:** CL:1001474 *medium spiny neuron*. The mouse astrocytosis would map to CL:0000127 *astrocyte* **[verify]**.

---

## 7. Anatomical structures affected

- **Organ and system:** the brain only (nervous system). No systemic involvement has been reported.
- **Sites (UBERON):** UBERON:0002435 *striatum*, chiefly the posterolateral putamen, UBERON:0001874 *putamen* **[verify]**. Also UBERON:0001873 *caudate nucleus* **[verify]**; UBERON:0001875 *globus pallidus* **[verify]**, where PET shows reduced PDE10A; and UBERON:0002038 *substantia nigra* **[verify]**, where neuromelanin is lost.
- **Cells:** striatal MSNs. Expression is "exceptionally high" in the putamen (BRAINEAC data). In mouse, expression is very high and selective in the striatum and olfactory tubercle.
- **Subcellular:** plasma membrane (normal PDE10A localization) is lost. Mutant protein shows up in cytoplasmic and perinuclear aggregates and aggresomes.
- **Laterality:** bilateral and symmetrical.

---

## 8. Temporal development

- **Onset:** childhood, 5–10 years in the founding series. Onset is insidious and follows normal milestones.
- **Course:** chronic, lifelong and "scarcely progressive" clinically. Imaging is read as stage-like: swelling with restricted diffusion (active, age 11), then modest putaminal atrophy with normal diffusion (age 22), then a less marked hyperintensity with atrophy (age 53). These are **cross-sectional observations in different individuals**; no serial MRI has been published.
- **Late events:** possible parkinsonism in the fifth decade (1 case).
- **Remission:** none reported. **Critical periods:** unknown. The mouse lesions begin by 1 month of age, which hints that intervention would need to be early.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). Most cases are de novo, and familial transmission is documented (PMID:29130591).
- **Penetrance and expressivity:** not formally studied. The familial reports are consistent with high penetrance. Variable features include anxiety, dystonia, diurnal fluctuation and possible late parkinsonism.
- **Anticipation:** none; the cause is not a repeat expansion.
- **Germline mosaicism:** not reported, but parental mosaicism should be considered when counselling after a de novo diagnosis.
- **Founder effects:** none. p.Phe300Leu recurred independently on different haplotypes.
- **Epidemiology:** prevalence is unknown; ultra-rare. Kalampokini et al. 2024 (PMID:38442915) reviewed **31 PDE10A patients across 8 studies, dominant and recessive combined**. Only about 10–15 individuals with dominant GAF-B variants appear in the literature **[estimate from the case reports]**. A Prevalence entry would use `measure_type: CASES_IN_LITERATURE`.
- **Populations:** Dutch, British, Italian, Indian and Japanese patients reported. No clear sex bias (founding series: 1 male, 2 female).
- **Carrier frequency:** not applicable; the variants are absent from population databases.

---

## 10. Diagnostics

- **Clinical picture:** childhood-onset chorea with normal cognition **plus** bilateral striatal T2 hyperintensity on MRI should prompt PDE10A testing.
- **Imaging:**
  - Brain MRI (NCIT:C16809 *Magnetic Resonance Imaging*): symmetric posterolateral putaminal T2 hyperintensity, with swelling and restricted diffusion early and atrophy later.
  - DaT-SPECT can be abnormal in adults.
  - [11C]IMA107 PDE10A PET is a research tool only.
- **Laboratory tests and biomarkers:** no specific biochemical test or circulating biomarker exists.
- **Genetic testing:** exome or genome sequencing, or a childhood chorea / hyperkinetic movement disorder gene panel that includes PDE10A (with NKX2-1, ADCY5, GNAO1, ATP1A3, SLC2A1, FOXG1 and others; PMID:36054588). Parental testing confirms de novo status. CMA, karyotype, FISH, mtDNA and repeat-expansion testing are relevant only to exclude differentials (for example, HTT expansion when there is a family history).
- **Differential diagnosis**

| Condition | Distinguishing features |
|---|---|
| Recessive PDE10A dyskinesia (MONDO:0044637) | Biallelic variants (GAF-A, catalytic, or GAF-B p.Asp295Asn); onset in infancy; developmental delay common; **normal MRI** (PMID:27058446, PMID:36805523, PMID:38442915) |
| NKX2-1 benign hereditary chorea (MONDO:0008979) | **Normal MRI**; may include thyroid and lung involvement. Screening of about 60 NKX2-1-negative BHC-like cases with normal MRI found no PDE10A variants (PMID:27058447) |
| ADCY5-related dyskinesia | Same striatal cAMP pathway, but gain of function at the synthesis step; paroxysmal and nocturnal exacerbations; usually normal MRI |
| ADSD1 (PDE8B, MONDO:0012205) | Adult-onset parkinsonism; striatal MRI changes |
| Juvenile Huntington disease, mitochondrial/Leigh-spectrum disease, other striatal necrosis syndromes, GNAO1, ATP1A3, Sydenham chorea | HTT repeat expansion; lactate and metabolic workup; acute or necrotizing course; antistreptococcal serology |

- **Screening:** no newborn or population screening. Cascade testing of relatives is appropriate in familial cases.

---

## 11. Outcome and prognosis

- **Survival:** not reported to be shortened. The oldest reported patient was 60. No mortality data exist.
- **Morbidity:** lifelong chorea with only slow progression; cognition preserved.
- **Complications:** possible late nigrostriatal degeneration with parkinsonism (1 case; the founding authors ask whether this "is coincidental or whether individuals with de novo PDE10A mutations are also at an increased risk of developing degeneration of nigral neurons"). Anxiety in 1 case.
- **Prognostic factors and biomarkers:** none established.
- **Quality-of-life instruments:** none applied.

---

## 12. Treatment

**No disease-specific or evidence-based treatment exists.** Management is symptomatic and extrapolated from other childhood choreas.

| Approach | Notes | Suggested NCIT / CHEBI binding |
|---|---|---|
| Symptomatic anti-chorea pharmacotherapy (VMAT2 inhibitors such as tetrabenazine; benzodiazepines; neuroleptics) | Response data for dominant cases are not available from the abstracts I could access. A 2022 Neuropediatrics letter treated a **recessive** p.Arg218Trp patient with tetrabenazine after a levodopa trial with no clear effect | NCIT:C15986 *Pharmacotherapy* + `therapeutic_agent` tetrabenazine (CHEBI ID **[verify]**) |
| Levodopa | Helped the adult-onset parkinsonism in founding individual 3. The Knopp 2019 "two sisters" report of levodopa response (PMID:30777652; MeSH tags include *Consanguinity*) is probably **biallelic/recessive** and should not be attributed to ADSD2 **[unverified, no abstract]** | NCIT:C15986 + levodopa (CHEBI **[verify]**) |
| Physical and occupational therapy | Supportive | NCIT:C15302; NCIT:C121351 |
| Genetic counselling | 50% recurrence risk for offspring of an affected person; low but non-zero sibling risk after a de novo case because of possible parental mosaicism | NCIT:C15240 |

- **Pharmacogenomics:** none specific. CYP2D6 genotype guides tetrabenazine dosing generally (CPIC/FDA label) but has not been studied in this disease.
- **Experimental and future therapies:**
  - The founding report proposes that "Pharmacological modulation of this pathway could offer promising etiologically targeted treatments for chorea and other hyperkinetic movement disorders."
  - Reviews discuss PDE modulators and cAMP-pathway agents as a direction (PMID:34155691, PMID:38442915). PDE10A inhibitors (such as mardepodect/PF-02545920) were tested in Huntington disease and schizophrenia, not in ADSD2. Their logic (inhibiting an already under-active enzyme) would be questionable here.
  - Gene, ASO, siRNA or allele-specific silencing has no reported preclinical work for ADSD2.
  - **ClinicalTrials.gov:** I found no trial specific to ADSD2.

---

## 13. Prevention

- **Primary prevention:** not applicable; the variants are mostly de novo.
- **Secondary prevention:** early genetic diagnosis avoids an unnecessary diagnostic odyssey, and MRI separates this disorder from benign hereditary chorea.
- **Tertiary prevention:** monitor adults for parkinsonism.
- **Reproductive options:** genetic counselling. Prenatal or preimplantation testing is available for families with a known variant.
- **Immunization, prophylaxis, public-health measures:** not applicable.

---

## 14. Other species and natural disease

- No naturally occurring disease is reported in animals (OMIA has no record found).
- Orthologs: mouse *Pde10a* (MGI) and rat *Pde10a*. PDE10A is highly conserved, and Phe300 and Phe334 are conserved down to invertebrates (PMID:27058447).
- No zoonotic relevance.

---

## 15. Model organisms

| Model | Description | Recapitulation | Limitations | Source |
|---|---|---|---|---|
| **Pde10a F300L knock-in mouse** (CRISPR/Cas9) | Behaviour tested at 3, 6 and 12 months; striatal histology | Progressive reduced spontaneous locomotion and motor learning; reduced striatal PDE10A; PDE10A-positive cytosolic aggregates; "prominent and progressive vacuolar lesions within the striatum beginning at one month of age"; severe astrocytosis without microgliosis; homozygotes more severe than heterozygotes (dosage effect) | Hypokinetic rather than choreiform; **conference abstract only** (Marotta, Mencacci, Krainc et al., MDS Virtual Congress 2021, Abstract 1060; [MDS abstract](https://mdsabstracts.org/abstract/characterization-of-a-mouse-model-of-pde10a-related-autosomal-dominant-movement-disorder)); not peer-reviewed | MODEL_ORGANISM |
| HEK293 / COS-7 overexpression; rat primary striatal neurons | Enzyme kinetics (loss of cAMP stimulation); aggregation and trafficking; PKA-substrate phosphorylation | Molecular and cellular mechanism | Overexpression may itself drive aggregation, and the authors call for patient-derived systems | PMID:27058447; PMID:31871190 (IN_VITRO) |
| Recessive GAF-A Tyr97Cys knock-in mouse | Reduced striatal PDE10A, motor abnormalities | Models the **recessive** disease, not ADSD2 | — | PMID:27058446 |
| Pde10a knockout mice | Reported in the pharmacology literature with altered locomotor and striatal signaling phenotypes | Null alleles do not model the GAF-B mechanism | PMID not verified here **[unverified]** | — |

- **Patient-derived models:** no iPSC-derived MSNs or striatal organoids have been reported. This is the main gap for confirming aggregation in a human system.
- **Model resources:** MGI, IMSR and MMRRC for *Pde10a* alleles.

---

## Knowledge gaps

1. Which branch causes disease, and which causes the striatal lesion: lost cAMP stimulation, aggregation and mislocalization, or a dominant-negative effect? Both mechanisms have been shown only with overexpression.
2. Is late parkinsonism part of the disease or a coincidence? Longitudinal follow-up of adults is needed.
3. There is no natural-history study, no serial MRI and no treatment-response data for dominant cases.
4. The variants in the Esposito 2017 and Miyatake 2018 reports, and the genotype in the Knopp 2019 sisters, could not be confirmed from abstracts.

## Key references

| PMID | Citation | Type |
|---|---|---|
| 27058447 | Mencacci NE et al. *De Novo Mutations in PDE10A Cause Childhood-Onset Chorea with Bilateral Striatal Lesions.* Am J Hum Genet 2016;98:763–771 ([PMC4833291](https://pmc.ncbi.nlm.nih.gov/articles/PMC4833291/)) | Human clinical, in vitro |
| 29130591 | Narayanan DL et al. *Familial choreoathetosis due to novel heterozygous mutation in PDE10A.* Am J Med Genet A 2018 | Human clinical |
| 28949041 | Esposito S et al. *A PDE10A de novo mutation causes childhood-onset chorea with diurnal fluctuations.* Mov Disord 2017 | Human clinical; no abstract |
| 29165877 | Miyatake S et al. *A familial case of PDE10A-associated childhood-onset chorea with bilateral striatal lesions.* Mov Disord 2018 | Human clinical; no abstract |
| 31871190 | Tejeda GS et al. *Chorea-related mutations in PDE10A result in aberrant compartmentalization and functionality of the enzyme.* PNAS 2020 | In vitro |
| 30345538 | Niccolini F et al. *PDE10A and ADCY5 mutations linked to molecular and microstructural basal ganglia pathology.* Mov Disord 2018 | Human imaging |
| 18477562 | Handa N et al. *Crystal structure of the GAF-B domain from human PDE10A complexed with cAMP.* J Biol Chem 2008 | Structural |
| 27058446 | Diggle CP et al. *Biallelic Mutations in PDE10A…* Am J Hum Genet 2016 | Recessive differential |
| 36805523 | Bohlega S et al. *Expanding the genotype-phenotype landscape of PDE10A-associated movement disorders.* Parkinsonism Relat Disord 2023 | Human clinical |
| 38442915 | Kalampokini S et al. *PDE10A Mutation as an Emerging Cause of Childhood-Onset Hyperkinetic Movement Disorders: A Review of All Published Cases.* Neuropediatrics 2024 | Review |
| 34155691 | Erro R, Mencacci NE, Bhatia KP. *The Emerging Role of Phosphodiesterases in Movement Disorders.* Mov Disord 2021 | Review |
| 36054588 | Pérez-Dueñas B et al. *The Genetic Landscape of Complex Childhood-Onset Hyperkinetic Movement Disorders.* Mov Disord 2022 | Human cohort |
| 30777652 | Knopp C et al. *PDE10A mutation in two sisters with a hyperkinetic movement disorder – Response to levodopa.* Parkinsonism Relat Disord 2019 | Likely recessive; no abstract |

**Web sources:**
- [PMC4833291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4833291/)
- [LOVD ADSD2](https://databases.lovd.nl/shared/diseases/05191)
- [MDS 2021 F300L mouse abstract](https://mdsabstracts.org/abstract/characterization-of-a-mouse-model-of-pde10a-related-autosomal-dominant-movement-disorder)
- [MDS PDE10A dystonia abstract](https://www.mdsabstracts.org/abstract/a-rare-case-of-pde10a-associated-dystonia-with-bilateral-striatal-lesions/)
- [Narayanan 2018, PubMed](https://pubmed.ncbi.nlm.nih.gov/29130591/)
- [Kalampokini 2024, Thieme](https://www.thieme-connect.com/products/ejournals/html/10.1055/a-2281-1822)
- [Neuropediatrics 2022 letter](https://www.thieme-connect.com/products/ejournals/html/10.1055/a-1892-1547)
- [DisGeNET ADSD2](https://www.disgenet.org/browser/1/1/1/10846/_a/_b./)
- [UCL news release, 2016](https://www.ucl.ac.uk/ion/articles/news/20160414)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0044637` (2 mentions) - the report calls it "Recessive PDE10A dyskinesia"; MONDO calls it **infantile-onset generalized dyskinesia with orofacial involvement**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0008979` (1 mention) - the report calls it "NKX2-1 benign hereditary chorea"; MONDO calls it **chorea, benign familial**, and lists "benign hereditary chorea" among its other names