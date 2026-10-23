---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:18.650364'
end_time: '2026-10-14T15:52:21.895610'
duration_seconds: 183.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Fibrosis, Neurodegeneration, and Cerebral Angiomatosis
  mondo_id: MONDO:0032651
  category: Genetic
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
  web_search_requests: 4
  num_turns: 10
  total_cost_usd: 1.9204402000000003
  session_id: 881e5e2b-b935-453f-93a9-c34d574852e4
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 8
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fibrosis, Neurodegeneration, and Cerebral Angiomatosis
- **MONDO ID:** MONDO:0032651 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Fibrosis, Neurodegeneration, and Cerebral Angiomatosis** covering all of the
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

Gathering the last few facts (phagocytosis screen, Orphanet ID), then writing the report.

# Fibrosis, Neurodegeneration, and Cerebral Angiomatosis (FINCA syndrome): research report

**Scope and sources.** This report draws mainly on the 13 PubMed abstracts already cached in `references_cache/` (all quotes below are copied from those cached abstracts), plus a few web searches. The literature is small: about 33 to 35 published patients, one gene, and one compound-heterozygous mouse model. Many template sections have no data, and I say so where that applies rather than filling them in.

**Ontology IDs need checking.** Apart from MONDO:0032651 and the OMIM numbers, the HPO, GO, CL, UBERON and NCIT IDs below came from memory, not from a lookup. Treat them as leads only. Under this repository's rules, run each one through `runoak` or `just validate-terms` before binding it.

**Connectors.** The claude.ai PubMed and OLS connectors were not authorized in this session, so I could not use them. Authorizing them in claude.ai connector settings would make term and PMID checks easier next time.

---

## 1. Disease information

**Overview.** FINCA is an autosomal recessive multisystem disease caused by biallelic variants in *NHLRC2*. It was first described in 2018 in three Finnish children who died in early childhood. Since then the known phenotype has widened: there are now survivors into childhood and adulthood, and some patients have a mainly neurodevelopmental picture.

> "A novel multi-organ disease that is fatal in early childhood was identified in three patients from two non-consanguineous families. These children were born asymptomatic but at the age of 2 months they manifested progressive multi-organ symptoms resembling no previously known disease." — PMID:29423877 (Uusimaa et al., *Acta Neuropathol* 2018)

> "FINCA is the first human disease caused by recessive variants in the highly conserved NHLRC2 gene." — PMID:37179546 (Tallgren et al., *Front Neurosci* 2023)

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0032651 "fibrosis, neurodegeneration, and cerebral angiomatosis" |
| OMIM, disease | #618278 |
| OMIM, gene (*NHLRC2*) | *618277 (PMID:34165204) |
| HGNC | *NHLRC2*; look up the hgnc: number (lowercase `hgnc:` form) before use |
| Orphanet | Not found. No ORPHA record mentioning NHLRC2 is in the local cache, and web search did not return one |
| ICD-10 / ICD-11 / MeSH | No disease-specific codes found |

**Synonyms.** FINCA syndrome; FINCA disease; NHLRC2-related disease (Sczakiel 2023 uses "NHLRC2-related disease").

**Type of evidence.** All of it comes from aggregated case reports and series (individual-patient descriptions). There are no registry or EHR datasets, apart from the chILD-EU register search in Rapp et al. 2021.

## 2. Etiology

- **Cause.** Biallelic (homozygous or compound heterozygous) germline variants in *NHLRC2*. The missense variant p.Asp148Tyr (c.442G>T) recurs, and in the early reports every patient carried it on at least one allele (PMID:37188825).
- **Hypomorphism.** Complete loss of NHLRC2 is presumed lethal. *Nhlrc2*-null mouse embryos stop developing before the morula stage (PMID:29423877) or die during gastrulation (as summarized in PMID:37179546). Patients therefore carry at least one allele that keeps some function.
- **Genetic risk factors.** None known beyond the causal gene. No modifier genes or GWAS loci have been reported.
- **Environmental and gene–environment factors.** Nothing is established. Respiratory disease "was progressive or exacerbated during infections" (PMID:35255187). The FINCA mouse paper suggests environmental triggers as a research question: the model "serves as a tool for investigations on the role of environmental triggers in disease patho[genesis]" (PMID:40510178). This is a hypothesis, not a demonstrated factor.
- **Protective factors.** None known. Higher residual NHLRC2 protein goes with milder disease (see section 4), which works like a protective allele effect.

## 3. Phenotypes

Frequencies are mostly qualitative. Pooled counts appear in Sczakiel 2023 and Tallgren 2023, but only the abstracts are cached, so exact per-feature percentages should be taken from the full texts.

| Phenotype | Onset and course | Frequency and notes | Candidate HPO (verify) | Key PMID |
|---|---|---|---|---|
| Global developmental delay / intellectual disability | Infancy; becomes the main feature in survivors | Universal in the 15-patient series ("All patients… presented with moderate to severe global developmental delay") | Global developmental delay HP:0001263; Intellectual disability HP:0001249 | 37188825, 34165204 |
| Interstitial lung disease / pulmonary fibrosis | Infancy; progressive in fatal cases, often stabilizes in survivors | Frequent; "pronounced in almost all patients during infancy" in Rapp's 6 patients | Interstitial pulmonary abnormality / Pulmonary fibrosis HP:0002206 | 34165204, 37179546 |
| Respiratory distress / respiratory failure | Infancy | Main cause of early death | Respiratory distress HP:0002098; Respiratory failure HP:0002878 | 29423877, 39328589 |
| Seizures | 9 months to 13 years | "Frequently observed" | Seizure HP:0001250 | 37188825 |
| Truncal hypotonia | Infancy | Frequent | Truncal hypotonia HP:0008936 | 37188825 |
| Movement disorder | Childhood | Frequent; Rett-like features reported | Abnormality of movement HP:0100022 | 37188825, 35255187 |
| Cerebral angiomatosis (leptomeningeal and cortical hypervascularization) | Seen at neuropathology | Autopsy cases | Look up a vascular malformation term | 29423877 |
| White-matter vacuolar degeneration, myelin loss, neuronal degeneration | Progressive | Autopsy cases | Look up leukodystrophy / white-matter abnormality terms | 29423877 |
| Cerebral and cerebellar atrophy | Progressive | Seen on imaging in survivors | Cerebral atrophy HP:0002059; Cerebellar atrophy HP:0001272 | 35255187 |
| Chronic haemolytic or macrocytic anemia | Infancy | A "key feature" in Tallgren's patients | Hemolytic anemia HP:0001878; Macrocytic anemia HP:0001972 | 29423877, 37179546 |
| Recurrent infections | Infancy and childhood | A key feature | Recurrent infections HP:0002719 | 29423877, 37179546 |
| Malabsorption / chronic diarrhea | Infancy | Classic severe cases | Malabsorption HP:0002024 | 29423877, 35255187 |
| Growth failure / failure to thrive | Infancy; progressive | Classic severe cases | Failure to thrive HP:0001508 | 29423877 |
| Hepatomegaly, steatosis, hepatic fibrosis; transient liver dysfunction | Infancy | Autopsy and lab findings | Hepatomegaly HP:0002240; Hepatic steatosis HP:0001397; Hepatic fibrosis HP:0001395 | 29423877 |
| Muscle fibrosis | — | Reported in the earlier cases | Look up | 37188825 |
| Cardiac fibrosis | — | Autopsy | Look up | 37179546 |
| Congenital heart defects (CoA, VSD, ASD, PDA) | Congenital | Single Chinese sibling; may be coincidental | Look up | 39328589 |
| Raised KL-6 (laboratory) | — | Lung injury marker, single case report | — | 39328589 |

Supporting quotes:

> "The main clinical features included progressive cerebropulmonary symptoms, malabsorption, progressive growth failure, recurrent infections, chronic haemolytic anaemia and transient liver dysfunction." — PMID:29423877

> "Interstitial fibrosis and previously undescribed granuloma-like lesions were observed in the lungs. Hepatomegaly, steatosis and collagen accumulation were detected in the liver." — PMID:29423877

> "Seizures, truncal hypotonia and movement disorders were frequently observed." — PMID:37188825

> "All five patients presented with multiorgan dysfunction with neurodevelopmental delay, recurrent infections and macrocytic anemia as key features. Interstitial lung disease was pronounced in infancy but often stabilized." — PMID:37179546

**Quality of life.** No QoL instrument (EQ-5D, SF-36, PROMIS) has been used. Survivors have severe neurodevelopmental disability and long-term care needs.

## 4. Genetic and molecular information

- **Gene.** *NHLRC2* (NHL repeat-containing protein 2), chromosome 10q25.3, gene OMIM *618277. The protein has three domains:
  - an N-terminal thioredoxin-like (Trx-like) domain;
  - a six-bladed NHL-repeat β-propeller;
  - a non-conserved C-terminal domain.

  > "The structure reveals two domains adjacent to each other that form a cleft containing a conserved CCINC motif." — PMID:30138417

  The Trx-like domain has no measurable thioredoxin activity: "an insulin turbidity assay on human recombinant NHLRC2 showed no thioredoxin activity" (PMID:29423877).

- **Variants reported**

| Variant | Type | Notes | PMID |
|---|---|---|---|
| c.442G>T p.Asp148Tyr | Missense, hypomorphic | Recurrent; destabilizes the protein by 2 °C; Asp148 is not conserved across species | 29423877, 30138417 |
| c.601_602del p.Arg201GlyfsTer6 | Frameshift | Not expressed in patient fibroblasts, so likely null | 29423877 |
| c.428C>A p.His143Pro | Missense in the Trx-like domain | Absent from gnomAD | 32435055 |
| Nine novel variants (missense and truncating) | Mixed | Includes 8 patients without p.Asp148Tyr | 37188825 |
| c.1610dupT p.Leu537PhefsTer17 | Frameshift | Chinese siblings | 39328589 |
| Novel missense (Polish patient) | Missense | Rett-like phenotype | 35255187 |

The c.601_602del coordinate for the frameshift comes from my recollection of the full text and is not in the cached abstract, so confirm it. Brodsky 2020 writes the recurrent variant as "c.442T>G"; this is a notation inconsistency, and c.442G>T is what PMID:37179546 and PMID:33297935 use.

- **Classification.** ClinVar and ClinGen status was not checked in this session. There is no CGGV record in the local cache.
- **Origin.** Germline.
- **Functional effect.** Partial loss of function (hypomorphic), with protein level tracking severity:

  > "we propose a potential genotype-phenotype correlation, with a greater reduction in protein expression being associated with a more severe phenotype." — PMID:37188825

- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

## 5. Environmental information

Not applicable as a cause. Intercurrent respiratory infections make the lung disease worse (PMID:35255187). There is no infectious agent and no toxicant link.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic hypomorphic *NHLRC2* variants** (often p.Asp148Tyr in trans with a null allele) **lead to** reduced, destabilized NHLRC2 protein. This is demonstrated: low NHLRC2 in patient fibroblasts (PMID:29423877), 2 °C destabilization (PMID:30138417), and lower expression in HEK293 assays (PMID:37188825).
2. **Reduced NHLRC2 leads to** abnormal Rho GTPase (RhoA–Rac1) signalling and actin-cytoskeleton dynamics. Proximity-labelling MS in human cells and mESC transcriptomics both point to Rho GTPase signalling (PMID:40510178). A genome-wide CRISPR screen identified NHLRC2 as a regulator of RhoA–Rac1, actin polymerization and filopodia in phagocytosis (Haney et al., *Nat Genet* 2018, PMID:30397336; cited from web search, not cached). This step is demonstrated in cells; its contribution to patient disease is inferred.
3. **The disturbed cytoskeleton and vesicle transport branch into four outcomes:**
   - **3a. Fibroblasts are more likely to become myofibroblasts, which leads to** interstitial fibrosis of the lung, liver, muscle and heart. Shown in patient-derived fibroblasts; the link to organ fibrosis is inferred.
     > "compound heterozygous p.Asp148Tyr and p.Arg201GlyfsTer6 mutations in NHLRC2 lead to severe tissue fibrosis in humans by enhancing the differentiation of fibroblasts to myofibroblasts." — PMID:30239752

     Patient cells also show "multilamellar bodies and distinctly organized vimentin filaments" (PMID:30239752).
   - **3b. Macrophage differentiation and phagocytosis fail, and innate immune responses change, which leads to** recurrent infections. This is also a plausible source of inflammatory lung injury, though that link is inferred.
     > "NHLRC2 mutant macrophages were hyperinflammatory and did not exhibit characteristics typical of macrophages, including atypical morphology and inability to interact and phagocytose bacteria/particles." — PMID:31594818 (THP-1 knockout)

     FINCA mice show "an altered innate immune response, particularly in interferon γ production" (PMID:40510178).
   - **3c. Neuronal development is disturbed: altered vesicular-transport and actin proteins, and accumulation of hnRNP C2, which leads to** neurodevelopmental delay, then progressive neurodegeneration, white-matter vacuolization and myelin loss, seizures and movement disorder. The evidence is from mice; the human link is inferred.
     > "isoform C2 of hnRNP C1/C2 was significantly increased in both developing neurons and the hippocampus of adult female FINCA mice" — PMID:33297935
   - **3d. Cerebral vascular abnormality (angiomatosis-like leptomeningeal and cortical hypervascularization) leads to** congestion. The mechanism is unknown. A loose lead: PDGFB showed up next to NHLRC2 in the Salmonella screen (PMID:31594818), but nothing connects it to the angiomatosis.
4. **Anemia (haemolytic, macrocytic, dyserythropoietic)** has no known mechanism.
5. **Redox and apoptosis (peripheral).** In HCT116 colon cancer cells, ROS trigger caspase-8 cleavage of NHLRC2 at Asp580, and losing NHLRC2 makes the cells more prone to ROS-induced apoptosis (PMID:29242562). This has not been shown in FINCA tissue.
6. **Clinical end-point.** The severity of lung fibrosis decides early mortality, and the neurological course decides long-term outcome.

### Candidate terms (verify each)

- **GO biological processes:** regulation of Rho protein signal transduction; actin cytoskeleton organization; phagocytosis (GO:0006909); myofibroblast differentiation; macrophage differentiation (GO:0030225); vesicle-mediated transport (GO:0016192); extracellular matrix organization; interferon-gamma production (GO:0032609).
- **GO cellular component:** cytosol (GO:0005829). NHLRC2 is described as "an essential cytosolic protein" in PMID:30138417.
- **CL cell types:** fibroblast (CL:0000057); myofibroblast (CL:0000186); macrophage (CL:0000235); neuron (CL:0000540); oligodendrocyte (CL:0000128, for the myelin loss, inferred); erythrocyte (CL:0000232); hepatocyte (CL:0000182); endothelial cell (CL:0000115, for the angiomatosis, inferred).

### Omics data

- Transcriptomics of mESCs carrying the variant or the knockout: changes in genes for metabolism, adhesion, neurodevelopment and immune response (PMID:40510178).
- 2D-DIGE proteomics of E13.5 cortical precursors: 19 altered proteins (PMID:33297935).
- BioID proximity-labelling interactomes (PMID:30239752, 40510178).
- Interaction partners from immunoprecipitation: FRYL, EIF2AK2, KLHL13 (PMID:31594818).
- No single-cell or spatial studies, and no GEO datasets found specific to the disease.

## 7. Anatomical structures affected

- **Primary organs:** brain, including cerebral cortex, white matter, leptomeninges and cerebellum; lung (interstitium); liver.
- **Secondary organs:** skeletal muscle, heart (fibrosis), gut (malabsorption), bone marrow and erythroid lineage, immune system.
- **Candidate UBERON terms (verify):** brain (UBERON:0000955), lung (UBERON:0002048), liver (UBERON:0002107), leptomeninx (UBERON:0000391), cerebral cortex (UBERON:0000956), cerebellum (UBERON:0002037), white matter.
- **Subcellular:** cytosol, actin cytoskeleton, vimentin intermediate filaments, and multilamellar bodies as an ultrastructural finding.
- **Laterality:** bilateral and diffuse. Chest CT shows bilateral ground-glass opacities (PMID:39328589).

## 8. Temporal development

- **Onset.** Patients are well at birth, with onset around 2 months in the severe form (PMID:29423877). Onset is in infancy to early childhood across the spectrum.
- **Course.** Two broad trajectories:
  1. **Severe:** rapidly progressive cerebropulmonary disease with death before about 3 years.
  2. **Attenuated:** interstitial lung disease stabilizes, and developmental delay becomes the main feature.

  > "Two of these children died before the age of two while four others survived until childhood… Interstitial lung disease was pronounced in almost all patients during infancy and stabilized over the course of the disease with neurodevelopmental delay (NDD) evolving as the key clinical finding." — PMID:34165204

- **Neurological course.** Progressive cerebral and cerebellar atrophy has been documented in survivors.
- **Remission.** No spontaneous remission. One child's lung disease improved on long-term glucocorticoids (PMID:39328589).
- **Critical period.** Infancy, for respiratory survival.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007).
- **Prevalence:** ultra-rare. About 33 published patients by 2025:
  > "Since our initial characterisation, 33 patients from various ethnic backgrounds have been reported" — PMID:40510178

  Later case reports may add a few more. No population prevalence estimate exists, so `prevalence_class` would be about literature case counts (`CASES_IN_LITERATURE`) or unknown, not a numeric band.
- **Populations reported:** Finnish (the first families), Ukrainian, German/European chILD register, Jordanian/Middle Eastern, Iranian, Pakistani, Canadian, US, Polish, Austrian, Chinese.
- **Founder effect:** possible for p.Asp148Tyr in Finland (the first families were non-consanguineous). The allele recurs across ancestries, so it is not purely a founder allele. I have not found a formal haplotype analysis.
- **Consanguinity:** present in some of the later homozygous families, for example the Middle Eastern and Iranian families in PMID:37188825 (from the full text; check before use).
- **Penetrance and expressivity:** penetrance appears complete for biallelic genotypes. Expressivity varies widely and tracks residual protein level.
- **Anticipation and mosaicism:** none reported.
- **Carrier frequency:** not established; gnomAD was not queried.
- **Sex ratio:** no sex bias reported.

## 10. Diagnostics

- **Genetic testing.** Exome sequencing found every reported case, with Sanger confirmation and segregation analysis. No single-gene test is in routine use. *NHLRC2* belongs on childhood interstitial lung disease (chILD) panels and on neurodevelopmental, epilepsy and Rett-like panels:
  > "NHLRC2-related disease should be considered in patients presenting with intellectual disability, movement disor[ders]…" — PMID:37188825

  > "the NHLRC2 gene should be considered in patients with symptoms of atypical Rett syndrome" — PMID:35255187
- **Imaging.**
  - Chest CT: ground-glass opacities and consolidation.
  - Brain MRI: cerebral and cerebellar atrophy, white-matter changes.
- **Pathology.**
  - Lung: interstitial fibrosis with granuloma-like lesions.
  - Liver: steatosis and collagen deposition.
  - Brain: angiomatosis-like vascularization, vacuolar white-matter degeneration.
  - Fibroblast electron microscopy: multilamellar bodies.
- **Laboratory.** Full blood count (macrocytic or haemolytic anemia), liver function tests, KL-6 (PMID:39328589). There is no disease-specific biomarker. Western blot of NHLRC2 in fibroblasts is a research test.
- **Differential diagnosis.**
  - Surfactant dysfunction disorders (*SFTPB*, *SFTPC*, *ABCA3*, *NKX2-1*). NKX2-1 is the brain–lung–thyroid syndrome and also combines a CNS and a lung picture.
  - *MARS1*-related pulmonary alveolar proteinosis.
  - *COPA* syndrome.
  - STING-associated vasculopathy (SAVI).
  - Rett and atypical Rett syndromes.
  - Mitochondrial disease.
- **Screening.** No newborn screening. Cascade carrier testing and prenatal or preimplantation testing are possible once the familial variants are known.

## 11. Outcome and prognosis

- **Mortality.** The existing KB entry gives 25.8% overall mortality across 31 patients, and 77.8% among the 9 patients with interstitial lung disease. Those figures need a source quote from the full text: they do not appear in the cached abstracts.
- **Timing of deaths.** Most deaths happen before 3 years, from respiratory failure:
  > "Patients described by the Finnish and Ukrainian group, and two patients described by Rapp et al. (2021) died before reaching the age of 3" — PMID:35255187
- **Survivors.** Reported survivors have reached late childhood and adulthood (KB entry: 4 to 61 years; check against the full text). They live with moderate to severe intellectual disability, epilepsy and movement disorder.
- **Prognostic factors.** Early interstitial lung disease predicts a poor outcome. Lower residual NHLRC2 expression goes with greater severity (PMID:37188825).

## 12. Treatment

There is no disease-modifying therapy. Management is supportive.

| Intervention | Evidence | Candidate NCIT (verify) |
|---|---|---|
| Systemic glucocorticoids for ILD | One case report: respiratory symptoms, CT and KL-6 improved in the younger sibling (PMID:39328589) | Pharmacotherapy NCIT:C15986, plus a therapeutic_agent glucocorticoid such as CHEBI:24261 (verify) |
| Respiratory support (oxygen, ventilation) | Standard care | Supportive Care NCIT:C15747 |
| Antiseizure medication | Standard care | Pharmacotherapy NCIT:C15986 |
| Nutritional support for malabsorption and growth failure | Standard care | Nutritional Support NCIT:C15433. Per CLAUDE.md, do not tag this BEHAVIORAL without reading the treatment |
| Physical, occupational and speech therapy | Standard care | NCIT:C15302 / C121351 / C159273 |
| Genetic counseling | Standard care | NCIT:C15240 |

> "the younger brother showed improvement in respiratory symptoms, chest CT, and Krebs von den Lungen-6 levels after long-term systemic glucocorticoid therapy, indicating that anti-inflammatory treatment may be beneficial in the treatment of ILD caused by FINCA syndrome." — PMID:39328589

- **Clinical trials.** None found. No gene therapy, ASO or other targeted approach has been reported.
- **Pharmacogenomics.** None.

## 13. Prevention

- **Primary prevention:** genetic counseling, with carrier, prenatal or preimplantation testing in families with known variants.
- **Secondary prevention:** early exome sequencing in infants who have chILD together with neurological signs.
- **Tertiary prevention:** prevent and treat infections early, given the infection-related worsening of lung disease. Vaccination is reasonable but has not been studied for this disease. Monitor anemia, liver and nutrition.
- **Public health and environmental measures:** not applicable.

## 14. Other species and natural disease

- No naturally occurring animal disease is known; no OMIA entry was found.
- Orthologs: mouse *Nhlrc2* and zebrafish *nhlrc2*. NHLRC2 homologs are "across a range of eukaryotic and prokaryotic species", and the conserved residues sit in the cleft between the Trx-like and β-propeller domains (PMID:30138417).
- No zoonotic relevance.

## 15. Model organisms

| Model | Genotype | What it reproduces | Limitations | PMID |
|---|---|---|---|---|
| Mouse, null | *Nhlrc2*−/− | Shows the gene is essential: development stops before the morula stage or during gastrulation | Cannot model the postnatal disease | 29423877 |
| Mouse, "FINCA mouse" | Knock-in p.Asp148Tyr over a knockout allele (compound heterozygous) | Neurodevelopmental and behavioural changes (adolescent hyperactivity, less exploration of a new object), altered IFN-γ and innate immunity, raised hippocampal hnRNP C2 | **No severe early multiorgan disease and no fibrosis**: "Despite the significant decrease in NHLRC2, the mice did not develop severe early onset multiorgan disease in either sex" (PMID:33297935) | 33297935, 40510178 |
| Zebrafish | *nhlrc2*−/− | Early larval lethality; injected *nhlrc2* mRNA delays onset and reduces severity | Not yet peer-reviewed (Oulu thesis / conference abstract) | web: Oulu thesis |
| Patient-derived immortalized skin fibroblasts | Compound heterozygous | Myofibroblast features, multilamellar bodies, vimentin reorganization | Cell culture only; no organ context | 30239752 |
| THP-1 macrophages | CRISPR knockout | Failed differentiation, loss of phagocytosis, hyperinflammation | Complete knockout, not hypomorphic; cancer cell line | 31594818 |
| HEK293 expression | Variant constructs | Protein-level assay behind the genotype–phenotype correlation | Overexpression system | 37188825 |
| mESCs | Homozygous p.Asp148Tyr or knockout | Transcriptomic changes | Embryonic stem-cell context | 40510178 |

For KB curation, the FINCA mouse fits `animal_models:` with `PARTIALLY_RECAPITULATES` against the neurodevelopmental and immune nodes and `FAILS_TO_RECAPITULATE` against the fibrosis node. The abstract quote above can serve as the required evidence for that negative link. This is also a natural `HUMAN_MODEL_MISMATCH` discussion: the mouse has reduced protein and no fibrosis, while patients have severe fibrosis.

---

## Notes for curation against the existing entry

- An untracked entry `kb/disorders/Fibrosis_Neurodegeneration_And_Cerebral_Angiomatosis.yaml` already exists in this worktree. It cites most of the PMIDs above and has two problems under current rules:
  - It carries `updated_date`, which is deprecated.
  - It uses the deprecated `percentage` field in `prevalence`. That should become `measure_type: CASES_IN_LITERATURE` with structured slots.
- Haney et al. 2018 (PMID:30397336) is the main evidence for the RhoA–Rac1 node and is not in `references_cache/`. Fetch it with `just fetch-reference PMID:30397336` before citing it.
- Three numbers in the existing entry are not in any cached abstract: the mortality figures (25.8% / 77.8%), the survivor age range (4 to 61 years) and the seizure-onset range. Each needs a full-text source.

## Sources

- Cached abstracts: PMID:29423877, 30138417, 30239752, 31594818, 32435055, 33297935, 34165204, 35255187, 37179546, 37188825, 39328589, 40510178, 29242562.
- [Haney et al. 2018, *Nat Genet*, doi:10.1038/s41588-018-0254-1](https://www.doi.org/10.1038/S41588-018-0254-1) and [BioGRID ORCS dataset](https://orcs.thebiogrid.org/Dataset/246)
- [Hiltunen et al. 2025, PMC12159220](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12159220/); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2024.06.14.599017.full.pdf)
- [Oulu thesis: NHLRC2 in embryonic development and FINCA modelling (zebrafish)](https://oulu.fi/en/theses/nhlrc2-embryonic-development-neurodevelopment-and-neurodegeneration-modelling-novel-finca-disease)
- [Tallgren et al. 2023, PMC10173879](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10173879/); [Sczakiel et al. 2023, PMC10400545](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400545/); [Biterova et al. 2018, PMC6107167](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6107167/)
