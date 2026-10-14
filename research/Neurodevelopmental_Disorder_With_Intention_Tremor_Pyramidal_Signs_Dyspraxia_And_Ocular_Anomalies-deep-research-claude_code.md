---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:18.360513'
end_time: '2026-10-14T15:53:24.483649'
duration_seconds: 246.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder With Intention Tremor, Pyramidal Signs,
    Dyspraxia, And Ocular Anomalies
  mondo_id: MONDO:0859274
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 23
  total_cost_usd: 2.5238506000000003
  session_id: 123f44f8-a04b-4669-9d4f-45a3c852599c
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 4
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Intention Tremor, Pyramidal Signs, Dyspraxia, And Ocular Anomalies
- **MONDO ID:** MONDO:0859274 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Intention Tremor, Pyramidal Signs, Dyspraxia, And Ocular Anomalies** covering all of the
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

I'm pulling the cited abstracts from the local reference cache so the quotes in the report are exact. Then I'll write the report.

Next I'm reading the Finnish discovery paper's cached full text to get allele frequencies and the founder-haplotype details.

I have the main facts I need. I'm pulling a few last details (the Finnish allele frequency, the strabismus surgeries and the gene-enrichment results), then I'll write the report.

# Research report: Neurodevelopmental disorder with intention tremor, pyramidal signs, dyspraxia, and ocular anomalies (NEDITPO; MONDO:0859274)

**Sources and method.** This report draws on the reference abstracts and full texts cached in the dismech repository: PMID:35087184, PMID:38806677, PMID:27018474, PMID:35321723, PMID:31792449 and PMID:33242396. It also uses the existing draft entry `kb/disorders/Neurodevelopmental_Disorder_With_Intention_Tremor_Pyramidal_Signs_Dyspraxia_And_Ocular_Anomalies.yaml` and a web search, which confirmed the OMIM and ClinVar identity.

Quotes are copied from the cached text. HPO, CL, UBERON and GO labels were read from the repository's `cache/*/terms.csv`, not written from memory.

Several services could not be used:
- **PMC:** blocked by a captcha.
- **PubMed, OLS and bgpt MCP servers:** they need authorization in claude.ai connector settings before they can be used.

**Bottom line.** The evidence base is a single human report: 5 Finnish men from 3 families (PMID:35087184, *Eur J Hum Genet* 2022). Mechanistic support comes from a 2024 zebrafish *smg9* null model (PMID:38806677) and from the more severe allelic disorder caused by loss-of-function variants, heart and brain malformation syndrome (HBMS).

---

## 1. Disease information

**Overview.** NEDITPO is an autosomal recessive syndromic neurodevelopmental disorder caused by homozygosity for the Finnish founder missense variant SMG9 c.551T>C p.(Val184Ala). The defining phenotype is quoted directly from the paper: *"Characteristic clinical findings in patients were mild to moderate ID, intention tremor, pyramidal signs, dyspraxia, and ocular manifestations."* (PMID:35087184)

It is the mild, hypomorphic end of the SMG9 allelic spectrum. Biallelic loss-of-function (LoF) SMG9 variants cause HBMS (MONDO:0014833), which is often lethal.

| Identifier | Value |
|---|---|
| MONDO | MONDO:0859274 |
| OMIM (phenotype) | 619995 (NEDITPO). This is the ClinVar-linked phenotype for rs749498958, per web search |
| OMIM (gene) | SMG9 *613176 (cited in PMID:35321723) |
| Gene | SMG9, hgnc:25763, 19q13.31 |
| Variant | NM_019108.4 c.551T>C p.(Val184Ala); GRCh38 g.19:43747479A>G; rs749498958 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code found. It would fall under general intellectual-disability codes |

**Synonyms:** NEDITPO; SMG9 p.(Val184Ala)-related neurodevelopmental disorder; mild SMG9-related syndromic intellectual disability.

**Data type:** individual-patient clinical series (case reports), with whole-blood RNA-seq from patients. No registry or EHR-level data exist.

## 2. Etiology

- **Cause:** a single homozygous missense variant in SMG9, a subunit of the SMG1–SMG8–SMG9 (SMG1C) kinase complex used in nonsense-mediated mRNA decay (NMD).
  > *"Here we report five patients from three unrelated families with intellectual disability (ID) and a novel pathogenic SMG9 c.551 T > C p.(Val184Ala) homozygous missense variant, identified using exome sequencing. Sanger sequencing confirmed recessive segregation in each family."* (PMID:35087184)
- **Genetic risk factors:** Finnish ancestry (founder effect, §9) and parental consanguinity or autozygosity. The variant is *"most likely an autozygous variant identical by descent."*
- **Environmental risk factors, protective factors and gene–environment interactions:** none reported. No modifier genes are known.

## 3. Phenotypes

All 5 patients were adult men aged 24–56 years. Frequencies are out of 5 (PMID:35087184).

| Phenotype | Frequency | HPO (label read from the term cache) | Notes / quote |
|---|---|---|---|
| Intellectual disability, mild–moderate | 5/5 | HP:0001249 Intellectual disability | *"All patients were male, aged 24–56 years, and had either mild or moderate ID (N = 5/5, 100%)."* |
| Delayed speech and language | 5/5 | HP:0000750 Delayed speech and language development | First words at 2–3.5 y; intelligible speech by 6–8 y |
| Oral motor dyspraxia | 5/5 | HP:0007301 Oromotor apraxia | Recorded as "Yes" for all 5 in Table 1 |
| Intention tremor | 5/5 | HP:0002080 Intention tremor | *"In addition, they had intention tremor and slow diadochokinesis (N = 5/5, 100%)."* |
| Dysdiadochokinesis | 5/5 | HP:0002075 Dysdiadochokinesis | Same sentence as above |
| Lower-limb hypertonia / spasticity | 5/5 | HP:0002061 Lower limb spasticity | *"All patients had muscular hypertonia and clonic or very brisk reflexes in their lower limbs."* |
| Ankle clonus; brisk patellar reflexes | 5/5 | HP:0011448 Ankle clonus; HP:0001347 Hyperreflexia | Brachioradialis reflex also brisk in 2/5 |
| Frequent falls in childhood | 5/5 | HP:0002359 Frequent falls | — |
| Childhood ataxia | 4/5 | HP:0001251 Ataxia | *"Four patients were described as ataxic when they were children (N = 4/5, 80%)."* |
| Strabismus | 4/5 (vertical 3/5) | HP:0000486 Strabismus; HP:0000577 Exotropia | Exotropia or esotropia with hyper- or hypotropia; 3 patients had surgery |
| Abnormal EEG without epilepsy | 3/5 | HP:0011182 Interictal epileptiform activity | Spike-and-slow-wave complexes; *"none of the patients were diagnosed with epilepsy"* |
| Childhood hypotonia | 2/5 | HP:0001252 Hypotonia | — |
| Pes planovalgus | 3/5 | HP:0001763 Pes planus | — |
| Recurrent otitis media in childhood | 3/5 recurrent (5/5 had at least one episode) | HP:0000403 Recurrent otitis media | — |
| Facial dysmorphism | variable | HP:0005280 Depressed nasal bridge; HP:0009765 Low hanging columella; HP:0000455 Broad nasal tip; HP:0011220 Prominent forehead; HP:0000218 High palate (3/5) | Mild |
| Brachydactyly | 2/5 | HP:0001156 Brachydactyly | — |
| Congenital heart defect | 1/5 | HP:0001669 Transposition of the great arteries; HP:0001629 VSD; HP:0001631 ASD; HP:0001643 PDA | One patient had TGA, VSD, ASD, PDA and a hypoplastic right atrium |
| Brain MRI abnormality | 1/5 (2 normal, 2 not available) | HP:0006956 Lateral ventricle dilatation; HP:0034295 Reduced cerebral white matter volume | *"…mild dilation of lateral ventricles and mild lack of white matter in the trigonum area."* |
| Short stature | 1/5 | HP:0004322 Short stature | Other growth parameters normal |

**Onset, severity and course.** Onset is in infancy or early childhood. Severity is mild to moderate. The course is non-progressive and lifelong. All patients walked independently; PMID:35321723 tabulates walking as achieved by ≤20 months.

**Quality of life.** No formal measures (EQ-5D, SF-36) have been reported. The functional burden comes mainly from intellectual disability, speech and dyspraxia, and motor incoordination. Adults are described as being in good general health.

## 4. Genetic and molecular information

- **Causal gene:** SMG9 (hgnc:25763). The variant lies in the central nucleotide-binding G-domain.
- **Variant classification:** likely pathogenic under ACMG/AMP criteria in the original paper (*"classified as likely pathogenic (PS4, PM2, PP1, PP3)"*). The ClinVar/OMIM-linked record lists it as Pathogenic (web search).
- **In silico scores:** CADD 23.8. MutationTaster: disease-causing. SIFT: deleterious. PolyPhen: benign.
- **Population frequency** (gnomAD v2.1.1): overall MAF 0.0001627. *"…the allele frequency is 34 times higher in the Finns (0.001598) than in non-Finnish Europeans (0.00004644), and there are no homozygous individuals in the gnomAD."* The expected number of homozygotes in Finland is about 14.
- **Founder haplotype:** shared ancestral haplotype with median length 1.7 Mb.
- **Origin and functional effect:** germline. Hypomorphic (partial loss of function). RNA-seq showed *"the SMG9 c.551T > C variant did not affect the splicing or expression level of SMG9 gene products."*
- **Allelic spectrum (HBMS, for comparison):**
  - Homozygous LoF variants: c.520_521delCC p.(Pro174Argfs*12); c.701+4A>G; c.1177C>T p.(Gln393*).
  - Missense: c.1508G>C p.(Trp503Ser).
  - Compound heterozygous: c.947A>G p.(His316Arg) + c.1318_1319delAG.

  These are tabulated in PMID:35321723 and PMID:27018474. PMID:35321723 notes that homozygous missense genotypes give milder disease: *"patients with SMG9 homozygous missense variants exhibited a milder phenotype"*.
- **Modifier genes, epigenetic changes, chromosomal abnormalities:** none reported.

## 5. Environmental information

No environmental, lifestyle or infectious factors are reported. This section does not apply.

## 6. Mechanism and pathophysiology

**Causal chain:**

1. **Lesion.** Homozygous SMG9 p.Val184Ala in the G-domain. Expression and splicing are unchanged (shown, human RNA-seq).
2. **The structural defect is predicted to impair SMG1C assembly or regulation** (inferred, from computational modelling): *"In the predicted model of mutated SMG9 p.184Ala structure, the magnesium ion is not conserved and there is a structural defect in the G-domain, which is the ATP binding site. This structural change could affect the binding of UPF1 to SMG1-SMG8-SMG9 protein complex, altering the kinase activity of SMG1."* The SMG1–SMG8–SMG9 architecture is from cryo-EM (PMID:31792449).
3. **Canonical NMD of transcripts with a premature termination codon (PTC) is preserved** (shown, allele-specific expression analysis): *"…indicating a functioning PTC-induced NMD mechanism"*.
4. **Endogenous transcripts are selectively dysregulated** (shown in blood). 112 genes were differentially expressed: *"~ 6.5 times more upregulated (97) than downregulated (15) genes"*. Many of these transcripts carry upstream ORFs (uORFs) or long 3′UTRs, both features of NMD targets.
   - Up: SMOX (logFC 2.1), OSBP2 (2.2), GPX3 (2.4), RAP1GAP (4.0), HEY1 (2.0), MAP1B (2.9).
   - Down: ZNF155 (−2.3), OLFM1, NTSR1, TUBB2A (−2.9).
   - Enriched pathways include hydrogen peroxide metabolism and cellular oxidant detoxification.
5. **Branch A: oxidative stress** (shown in zebrafish; inferred in humans). Raised SMOX leads to excess polyamine catabolism, which produces H₂O₂ (reactive oxygen species, ROS) and acrolein. These cause mitochondrial swelling and vacuolization in the brain. *"Spermidine oxidase (Smox) is increased in smg9oi7/oi7 zebrafish, resulting in the accumulation of byproducts, reactive oxygen species, and acrolein."* (PMID:38806677)
6. **Branch B: neurodevelopmental genes** (inferred). Dysregulation of HEY1 (Notch signalling, gliogenesis), RAP1GAP (neuronal differentiation), and the microtubule genes MAP1B and TUBB2A plausibly disturbs neural progenitor and circuit development.
7. **Cellular outcome** (shown in zebrafish). Fewer proliferating radial glial progenitors and a smaller telencephalon. Both were partly rescued by the SMOX inhibitor MDL72527 and by N-acetylcysteine.
8. **Clinical outcome** (inferred). Abnormal maturation of cerebellar and corticospinal circuits leads to intention tremor, dysdiadochokinesis and ataxia (cerebellar signs) and to spasticity and clonus (pyramidal signs). Cortical involvement leads to intellectual disability and dyspraxia. Heart defects have low penetrance (1/5), reflecting SMG9's role in heart development, which HBMS shows fully.

**Upstream versus downstream:** the SMG9/SMG1C defect is upstream. The transcriptome change is the intermediate step. Oxidative stress and progenitor defects are downstream. All human molecular data come from whole blood; there are no data from patient brain tissue.

**Suggested ontology terms:**
- **GO:** GO:0000184 nuclear-transcribed mRNA catabolic process, nonsense-mediated decay; GO:0006598 polyamine catabolic process; GO:0072593 reactive oxygen species metabolic process; GO:0098869 cellular oxidant detoxification; GO:0007005 mitochondrion organization; GO:0022008 neurogenesis; GO:0007420 brain development; GO:0007507 heart development.
- **CL:** CL:0000681 radial glial cell; CL:2000029 central nervous system neuron.

**Not available:** proteomics, metabolomics, single-cell, spatial or epigenetic data.

## 7. Anatomical structures affected

- **Primary:** brain, UBERON:0000955. The signs point to cerebellum (UBERON:0002037) and corticospinal tract involvement.
- **Secondary:** extraocular muscle control (strabismus), heart (UBERON:0000948; 1/5), middle ear (otitis), feet and hands.
- **Subcellular:** cytoplasm (the NMD and SMG1C machinery), and mitochondria in the model.
- **Laterality:** neurological signs are bilateral. Strabismus is variable; right-sided exotropia or hypertropia is common.

## 8. Temporal development

- **Onset:** infancy to early childhood, insidious. Speech delay is the most prominent early sign.
- **Course:** static and lifelong, with childhood ataxia and falls. Five adults evaluated at 24–56 years had persistent tremor and pyramidal signs.
- **Stages and remission:** none described.
- **Critical period:** early neurodevelopment, when speech and motor therapy may matter most (inferred).

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). Penetrance is apparently complete for the neurological core. Expressivity varies for heart defects, MRI findings and growth.
- **Founder effect:** Finnish (see §4). No homozygotes are listed in gnomAD.
- **Prevalence:** 5 reported cases (ultra-rare). About 14 homozygotes are predicted in Finland.
- **Sex:** all 5 reported patients are male, which is probably chance given recessive inheritance.
- **Not reported:** anticipation and germline mosaicism.
- **Carrier frequency:** about 1 in 313 Finns (2 × 0.0016), derived arithmetically from the gnomAD frequency.

## 10. Diagnostics

- **Genetic testing:** exome sequencing was how the diagnosis was made. Targeted testing for c.551T>C is reasonable in Finnish patients with ID plus intention tremor. SMG9 appears on intellectual-disability gene panels (PanelApp Australia).
- **Supporting tests:** EEG (interictal discharges), brain MRI (usually normal or mild changes), echocardiography, ophthalmology.
- **Biomarkers:** none validated. Upregulation of SMOX and GPX3 in blood is a research signal only.
- **Differential diagnosis:**
  - HBMS (biallelic SMG9 LoF: severe, with microcephaly and heart and brain malformations).
  - SMG8-related NDD (PMID:33242396).
  - Other NMD-factor disorders (UPF3B, UPF2).
  - Hereditary spastic paraplegias with ID.
  - Autosomal recessive cerebellar ataxias with ID.
- **Screening:** no newborn screening. Carrier screening could be considered in Finland.

## 11. Outcome and prognosis

Life expectancy appears normal: *"All the patients were adults with good general health, providing evidence that the homozygous SMG9 c.551T > C variant was not significantly associated with reduced life expectancy."*

Disability comes from intellectual disability and motor and speech impairment. Adult comorbidities were noted in some patients (hypertension, hypercholesterolemia, type 2 diabetes), but their relationship to the disorder is unknown. No prognostic markers exist.

## 12. Treatment

There is no disease-specific therapy. Management is supportive. NCIT terms are suggested from the dismech CLAUDE.md list:
- speech-language therapy (NCIT:C159273)
- physical therapy (NCIT:C15302)
- occupational therapy (NCIT:C121351)
- strabismus surgery (NCIT:C15329, Surgical Procedure); 3 of 5 patients had surgery
- cardiac surgical repair where a heart defect is present (NCIT:C15329)
- special education, supportive care (NCIT:C15747) and genetic counseling (NCIT:C15240)

**Experimental only.** SMOX inhibition (MDL72527) and antioxidant N-acetylcysteine rescued brain size in *smg9* null zebrafish (PMID:38806677). There is no human data and no clinical trials are listed.

## 13. Prevention

The only prevention options are genetic counseling (25% recurrence risk for carrier couples), cascade carrier testing in families, and prenatal or preimplantation testing.

## 14. Other species

No naturally occurring disease in other species has been identified (no OMIA entry found). SMG9 is conserved across vertebrates.

## 15. Model organisms

| Model | Phenotype | Fidelity to NEDITPO |
|---|---|---|
| **Smg9 knockout mouse** (CRISPR/Cas9; PMID:27018474) | *"…we were able to recapitulate the major features of the SMG9-related multiple congenital anomaly syndrome"*. Brain, heart and eye defects; early embryonic lethality | Models HBMS (null allele), not the hypomorphic Val184Ala |
| **smg9 oi7/oi7 null zebrafish** (PMID:38806677) | Small telencephalon, fewer radial glia, reduced cardiac contraction, premature aging. Smox/gpx3 upregulation matches the patient transcriptome; MDL72527/NAC rescue | Partial. A null allele, but it reproduces the human SMOX/GPX3 signature |
| **Patient cells** (whole blood RNA-seq; PMID:35087184) | Transcriptome dysregulation | Only the peripheral tissue was examined |

No Val184Ala knock-in model exists. That is the main gap in the mechanistic evidence.

---

### Evidence gaps
- Only one human cohort exists, and every patient is Finnish.
- The structural effect of Val184Ala comes only from modelling; it has not been tested biochemically.
- There are no brain-relevant cell data from patients (iPSC-derived neurons).
- The SMOX and oxidative-stress mechanism is shown only in null zebrafish.

### Sources
- [Rahikkala et al. 2022, PMC9090808 (PMID:35087184)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9090808/)
- [ClinVar RCV002274864](https://https.ncbi.nlm.nih.gov/clinvar/RCV002274864.1)
- [Yang et al. 2022, compound heterozygous SMG9 HBMS (PMID:35321723)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8943999/)
- [PanelApp Australia, SMG9](https://panelapp-aus.org/panels/76/gene/SMG9/)
- Shaheen et al. 2016, *Am J Hum Genet* (PMID:27018474)
- Lai et al. 2024, *Commun Biol* (PMID:38806677)
- SMG1–SMG8–SMG9 cryo-EM structure (PMID:31792449)
- SMG8 developmental disorder (PMID:33242396)
