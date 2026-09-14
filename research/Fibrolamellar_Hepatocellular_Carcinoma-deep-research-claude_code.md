---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T00:56:11.998989'
end_time: '2026-09-07T01:00:59.157831'
duration_seconds: 287.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Fibrolamellar Hepatocellular Carcinoma
  mondo_id: MONDO:0006210
  category: ''
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
  - claude-sonnet-5
  web_search_requests: 19
  num_turns: 21
  total_cost_usd: 1.2858143999999998
  session_id: 4bf4a114-75db-54c3-885d-72412fe47716
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fibrolamellar Hepatocellular Carcinoma
- **MONDO ID:** MONDO:0006210 (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Fibrolamellar Hepatocellular Carcinoma** covering all of the
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

I now have comprehensive material to compile the full research report.

I now have enough material across all sections to compile the comprehensive report.

# Fibrolamellar Hepatocellular Carcinoma (FLC/FL-HCC): Comprehensive Research Report

## 1. Disease Information

**Overview.** Fibrolamellar hepatocellular carcinoma (FLC, also FL-HCC or FLHCC) is a rare, histologically and molecularly distinct primary liver malignancy that predominantly arises in adolescents and young adults **without underlying cirrhosis, viral hepatitis, or other chronic liver disease** — a striking contrast to conventional hepatocellular carcinoma (HCC), which is overwhelmingly a cirrhosis-associated cancer of older adults. FLC is defined pathologically by large polygonal eosinophilic tumor cells embedded in parallel lamellae of collagenous stroma, and molecularly by a near-universal somatic **DNAJB1-PRKACA** gene fusion arising from a ~400 kb heterozygous deletion on chromosome 19p13.12 (Medscape; PMC8448801; PMC10787162).

**Key identifiers:**
- **MONDO:** MONDO:0006210
- **Orphanet:** ORPHA:401920 (also cross-referenced under ORPHA:33402, Pediatric hepatocellular carcinoma) ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=401920))
- **ICD-O-3:** 8171/3 (fibrolamellar carcinoma morphology code)
- **ICD-10:** C22.0 (liver cell carcinoma, as a subtype)
- **MeSH:** D049688 (Carcinoma, Hepatocellular is D006528; fibrolamellar variant indexed under related HCC headings)

**Synonyms:** Fibrolamellar carcinoma; fibrolamellar hepatocellular carcinoma; fibrolamellar liver cancer; polygonal cell type hepatocellular carcinoma with fibrous stroma (older WHO terminology).

**Information source.** Most quantitative data below derive from **aggregated disease-level resources** — the SEER registry, the National Cancer Database (NCDB), and pooled case-series/systematic reviews — supplemented by individual case reports for rare presentations (e.g., paraneoplastic syndromes). Because FLC is rare, single-institution and multi-institution retrospective cohorts (rather than prospective trials) are the dominant human evidence base.

---

## 2. Etiology

### Disease Causal Factors
The molecular driver of FLC is a **somatic ~400 kb heterozygous deletion on chromosome 19p13.12** that fuses the first exon of *DNAJB1* (encoding a heat-shock protein 40/Hsp40 co-chaperone) in-frame to exons 2–10 of *PRKACA* (the catalytic alpha subunit of protein kinase A, PKA) (PubMed:29162699; PNAS:1716483114). This fusion is found in **>80–100% of morphologically classic FLC cases** across independent series and is considered the pathognomonic, essentially disease-defining lesion (PMC5758901).

**There is no established environmental, infectious, or lifestyle cause.** Unlike conventional HCC, FLC arises in the absence of viral hepatitis (HBV/HCV), alcohol-related liver disease, metabolic dysfunction-associated steatotic liver disease, hemochromatosis, or cirrhosis of any etiology (NORD; PMC9750232 "Fibrolamellar Hepatocellular Carcinoma in the Absence of Risk Factors").

### Risk Factors

**Genetic risk factors:**
- The defining lesion is **somatic, not germline** — occurring de novo in tumor tissue and not inherited or transmissible to offspring (Fibrolamellar Cancer Foundation).
- Whole-genome sequencing of 10 patient tumor/normal pairs found FLC has a **remarkably low somatic coding-mutation burden**, among the lowest of any solid tumor sequenced, with the DNAJB1-PRKACA fusion as essentially the only recurrent structural event and no consistent "second hit" (PMC4359253/Oncotarget:2712).
- A single case report describes a 14-year-old girl with FLC carrying **both a germline and somatic TP53 mutation**, raising the possibility that FLC could rarely fall within the Li-Fraumeni tumor spectrum, though this is not an established recurrent association (Familial Cancer, 10.1007/s10689-017-9998-5).
- No confirmed susceptibility loci, modifier genes, or GWAS-defined risk alleles have been established for FLC given its rarity.

**Environmental/demographic risk factors:**
- **Age:** Bimodal incidence peaks at 15–19 years and 70–74 years, but the disease is classically associated with adolescents and young adults (typical reported range 14–33 years), with rare cases from age 2 to 74 (npj Precision Oncology, 10.1038/s41698-023-00371-2).
- **Race/ethnicity:** In the U.S., >85% of patients are non-Hispanic white, with smaller proportions among Chinese Americans (~6%), Black patients (~4%), and white Hispanic patients (~4%) — a markedly different demographic distribution than conventional HCC (PubMed:32052215).
- **Sex:** No strong sex predominance is consistently reported across series (unlike conventional HCC's male predominance), though some cohorts report a slight male-favoring trend as a prognostic (not necessarily risk) factor.
- **No family history association** has been established (sporadic disease).

### Protective Factors
No genetic or environmental protective factors have been identified in the literature; this reflects both disease rarity and lack of dedicated case-control epidemiological studies.

### Gene-Environment Interactions
None established. Given the essentially monogenic somatic driver (DNAJB1-PRKACA) and absence of implicated environmental exposures, there is no described gene-environment interaction model for FLC, unlike conventional HCC (where HBV/HCV × alcohol × metabolic risk interactions are well characterized).

---

## 3. Phenotypes

FLC's clinical phenotype is notable for **vague, insidious presentation** and, critically, **absence of the stigmata of chronic liver disease** seen in conventional HCC.

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Abdominal pain | ~72% (most common symptom) | HP:0002027 (Abdominal pain) |
| Abdominal distension/fullness | ~44% | HP:0003270 (Abdominal distention) |
| Anorexia/weight loss | ~32% | HP:0002039 (Anorexia); HP:0001824 (Weight loss) |
| Hepatomegaly / palpable abdominal mass | Common physical finding | HP:0002240 (Hepatomegaly) |
| Malaise/constitutional symptoms | Frequent | HP:0033834 (Fatigue-related) |
| Fever | Reported | HP:0001945 (Fever) |
| Jaundice | ~20% | HP:0000952 (Jaundice) |
| Gynecomastia (males) | Rare, due to tumor aromatase activity converting androgens to estrogens | HP:0000771 (Gynecomastia) |
| Hyperammonemic encephalopathy (paraneoplastic) | Rare but life-threatening complication | HP:0001982 (Hyperammonemia); HP:0002480 (Encephalopathy) |
| Absence of portal hypertension/cirrhosis stigmata | Characteristic negative finding | — |
| Metastatic sites: lymph nodes, lung, peritoneum, bone, pancreas, ovary | Variable, at diagnosis or recurrence | — |
| Rare paraneoplastic: cold agglutinin disease, Budd-Chiari syndrome, recurrent DVT/PE, cardiac spread with IVC obstruction, hyperthyroidism | Case-report level | — |

(Source: Chinese Clinical Oncology review, cco.amegroups.org/article/view/21275; PMC12576631; PMC6304646; PMC11002470)

**Phenotype characteristics:**
- **Onset:** Typically adolescent/young adult onset, though the true age range spans 2–74 years with a secondary elderly peak in registry data.
- **Progression:** Often insidious for months before diagnosis due to nonspecific symptoms; disease is frequently locally advanced or has nodal/metastatic spread at presentation because of this diagnostic delay.
- **Severity/frequency:** Symptom severity is variable; a subset of patients are diagnosed incidentally.
- **Quality of life impact:** Not systematically measured with validated instruments (EQ-5D/SF-36) in FLC-specific studies; QoL burden is inferred from the aggressive natural history, high recurrence rate, and the young age of patients (loss of years of life, fertility/oncofertility concerns, and psychosocial burden of a rare cancer diagnosis in adolescence).

### Hyperammonemic Encephalopathy — Mechanistic Detail
This is a distinctive, often under-recognized FLC paraneoplastic phenotype: tumor cells show **upregulation of glutaminase (GLS)**, which generates ammonia from glutamine, coupled with **downregulation of ornithine transcarbamylase and glutamine synthetase (GS)** — the ammonia-detoxifying enzymes. Net tumor ammoniagenesis overwhelms the (non-cirrhotic) residual liver's clearance capacity, producing severe hyperammonemic encephalopathy disproportionate to tumor burden or synthetic liver failure (PMC9922532; PMC4828114). Immunohistochemistry shows weak/diffuse GS expression in tumor cells.

---

## 4. Genetic/Molecular Information

### Causal Gene Fusion
**DNAJB1-PRKACA** is the signature and essentially universal driver:
- **DNAJB1** (HGNC:14887; DnaJ heat shock protein family member B1) exon 1 fused in-frame to
- **PRKACA** (HGNC:9380; protein kinase cAMP-activated catalytic subunit alpha) exons 2–10
- Resulting from a **~400 kb heterozygous deletion on chromosome 19p13.12** (PubMed:29162699).
- The fusion transcript is expressed at ~10-fold higher levels than wild-type *PRKACA*, and confers elevated cAMP-stimulated PKA catalytic activity relative to normal liver (ScienceDirect:S2772572322001911).
- Detected in **99–102/103 (99%)** of morphologically classic FLC cases in the largest multicenter FISH validation series (PubMed:35777788), and by RT-PCR in 92% (24/26) of tested cases, with the fusion transcript essentially specific to FLC among primary liver tumors tested (though see the diagnostic caveat below) (PMC5758901).

### Variant Classification and Functional Consequence
- **Somatic**, not germline (essentially always) — arises in the tumor only.
- **Functional impact:** Gain-of-function/neomorphic — the fusion is not merely PRKACA overexpression; ectopic overexpression of wild-type PRKACA alone fails to recapitulate FLC's oncogenic phenotype, indicating the DNAJB1 moiety confers a qualitatively distinct, "acquired scaffolding function" (PMC6533061) that (a) recruits Hsp70 into an altered PKA holoenzyme complex, and (b) via the upregulated scaffold protein AKAP-Lbc, clusters DNAJ-PKAc/Hsp70 with a RAF-MEK-ERK signaling module.
- Structural biology studies of the PKA RIIβ holoenzyme containing the DNAJB1-PKAc fusion reveal **protomer asymmetry and fusion-induced allosteric perturbations** relative to wild-type PKA holoenzyme (PMC7793292).

### Modifier/Cooperating Pathways
- **Wnt/β-catenin (CTNNB1) pathway:** DNAJB1-PRKACA interacts with β-catenin, and tumorigenesis is significantly enhanced by concurrent β-catenin activation in mouse models; this is consistent with recurrent Wnt-pathway mutations observed in human FLC series (PubMed:29162699; PNAS:1716483114). (Note: dedicated large-cohort CTNNB1 mutation-frequency data were not retrievable in this search pass and should be verified against primary genomic-landscape papers before citing a specific percentage.)
- **SIK/CRTC2/p300 axis (2024 mechanistic advance):** A 2024 *Cancer Discovery* study (10.1158/2159-8290.CD-24-0634) showed DNAJB1-PRKACA phosphorylates and **inactivates salt-inducible kinases (SIKs)**, deregulating the **CRTC2** transcriptional coactivator and **p300** acetyltransferase, producing global histone hyperacetylation and transcriptional reprogramming that drives malignant growth — nominating **CRTC2/p300 as a therapeutic target**.
- **RAS/MAPK and AURKA/GSK3-MYC networks:** Two downstream signaling branches have been mapped: (1) RAS/MAPK pathway components, and (2) an Aurora Kinase A (AURKA)/GSK3 sub-network with activity toward MYC — oncogenic PKA signaling increases c-MYC protein expression through multiple targetable mechanisms (PMC9925115).
- **Oncogenic addiction:** FLC tumor cells show dependency ("oncogenic addiction") specifically on the fusion kinase, supporting the fusion as the primary therapeutic vulnerability (PubMed:36302174).

### Mutational Burden
Whole-genome sequencing of paired tumor/normal samples from 10 patients found **relatively few coding somatic mutations** — among the lowest mutation burdens described for any sequenced solid tumor — with **no consistent recurrent "second-hit" mutation** beyond the founding fusion event (PMC4359253).

### Epigenetic Information
- Single-nucleus multi-omic profiling (snATAC-seq + snRNA-seq, 2024–2025) has revealed **cell-type-specific chromatin accessibility, transcription factor networks (notably CREB3L1), microRNA regulatory elements, and super-enhancers**, including super-enhancers near FLC-enriched genes such as **CDH11** and **SLC16A14** (Nature Scientific Reports 10.1038/s41598-026-44899-2; bioRxiv 10.1101/2024.12.11.627911).
- Global **histone hyperacetylation** downstream of CRTC2/p300 deregulation is a key epigenetic consequence of the fusion kinase (Cancer Discovery 2024).

### Chromosomal Abnormalities
The defining lesion is itself the **~400 kb interstitial deletion at 19p13.12** producing the DNAJB1-PRKACA fusion; beyond this, FLC genomes are notably stable/quiet, without the widespread aneuploidy or chromothripsis seen in many other cancers (PMC4359253).

### Diagnostic Caveat on Fusion Specificity
Although historically considered pathognomonic, DNAJB1-PRKACA fusions have also been reported in **oncocytic pancreatic and biliary neoplasms**, meaning the fusion is **not absolutely exclusive** to FLC and must be interpreted alongside morphology and clinical context (Modern Pathology 10.1038/s41379-019-0398-2).

**Suggested ontology bindings:** HGNC:9380 (PRKACA), HGNC:14887 (DNAJB1), HGNC:11986 (TP53, for the rare germline-mutation case), GO:0004691 (cAMP-dependent protein kinase activity), GO:0007190 (activation of adenylate cyclase activity), GO:0016575 (histone deacetylation, inverse direction relevant), NCIT for fusion gene concept.

---

## 5. Environmental Information

- **Environmental factors:** None established. FLC is not associated with aflatoxin exposure, industrial toxins, or occupational carcinogens the way conventional HCC or angiosarcoma can be.
- **Lifestyle factors:** No association with alcohol use, smoking, obesity/metabolic syndrome, or diet has been demonstrated; this is a key point of contrast with conventional HCC risk-factor profiles.
- **Infectious agents:** No association with HBV, HCV, or other hepatotropic pathogens. This absence is itself diagnostically informative — FLC is essentially defined in part by exclusion of viral/infectious hepatocarcinogenesis (NORD; Liver Foundation Australia).

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain (Proposed Sequence)

1. A **somatic ~400 kb heterozygous deletion at chromosome 19p13.12** occurs in a hepatocyte (or hepatic progenitor/biliary-hepatocyte intermediate cell), fusing *DNAJB1* exon 1 in-frame to *PRKACA* exons 2–10 — **leads to** formation of the chimeric DNAJB1-PRKACA transcript and protein (demonstrated; PubMed:29162699).
2. The fusion transcript is overexpressed (~10-fold over wild-type PRKACA) — **results in** markedly elevated, and qualitatively altered, cAMP-stimulated PKA catalytic activity, because the DNAJB1 moiety confers Hsp70-recruiting scaffold properties absent from wild-type PKA (demonstrated in vitro/structural studies; PMC6533061, PMC7793292).
3. The altered PKA holoenzyme, via **upregulated AKAP-Lbc**, clusters DNAJ-PKAc/Hsp70 subcomplexes with a **RAF-MEK-ERK kinase module** — **leads to** aberrant, spatially organized MAPK pathway activation (demonstrated; PMC6533061).
4. In parallel, DNAJB1-PRKACA phosphorylates and inactivates **salt-inducible kinases (SIKs)** — **results in** deregulation of the **CRTC2** coactivator and **p300** acetyltransferase, driving global histone hyperacetylation and a pro-tumorigenic transcriptional program (demonstrated 2024; Cancer Discovery 10.1158/2159-8290.CD-24-0634).
5. Downstream, an **AURKA/GSK3 sub-network** stabilizes **MYC** oncoprotein — **leads to** enhanced proliferative and cell-cycle-driving transcriptional output (demonstrated; PMC9925115).
6. The fusion kinase also **interacts directly with β-catenin**, and concurrent Wnt/β-catenin pathway activation **significantly enhances** tumorigenesis in mouse models, consistent with recurrent Wnt pathway alterations noted in human tumors — **leads to** cooperative oncogenic transformation of hepatocytes (demonstrated in mouse models; inferred as cooperating rather than sole driver in humans; PNAS:1716483114).
7. Neoplastic hepatocytes proliferate as large, eosinophilic, mitochondria-rich polygonal cells; concurrently, tumor cells (via TGF-β overexpression) **induce** stromal fibroblasts/myofibroblasts to deposit **parallel lamellar collagen bands** around cell nests — **results in** the pathognomonic fibrolamellar histologic architecture (mechanistically inferred from TGF-β overexpression data; direct causal proof in humans is largely histological/correlative).
8. Metabolically, tumor cells **upregulate glutaminase (GLS)** and **downregulate ornithine transcarbamylase and glutamine synthetase (GS)** — **leads to** a net ammoniagenic phenotype that, in a subset of patients (often with high tumor burden), **overwhelms** residual (non-cirrhotic) hepatic ammonia clearance — **resulting in** the paraneoplastic hyperammonemic encephalopathy phenotype (demonstrated mechanistically at the tumor tissue level; PMC9922532).
9. Neuroendocrine-gene overexpression, including **neurotensin**, provides an additional autocrine/paracrine source of cAMP and co-mitogenic signaling that may **reinforce** the PKA-driven proliferative loop (demonstrated in vitro; PMC6707953) — though neurotensin has not proven sufficiently sensitive/specific as a stand-alone clinical biomarker.
10. Clinically, unchecked local growth **leads to** a large, well-circumscribed hepatic mass (often 5–20 cm) with a central fibrous scar, and given the typically late, nonspecific symptom presentation, a substantial fraction of patients **progress to** regional lymph-node and distant (lung, peritoneal, osseous) metastatic spread by diagnosis or shortly after resection (documented in surgical/SEER series; e-jlc.org, cco.amegroups.org).

### Molecular Pathways
- **cAMP-PKA signaling** (central driver pathway; KEGG hsa04024)
- **RAS/MAPK (RAF-MEK-ERK)** cascade, aberrantly scaffolded by AKAP-Lbc
- **SIK-CRTC2-CREB/p300** transcriptional coactivation axis
- **Wnt/β-catenin** signaling (cooperating pathway)
- **AURKA-GSK3-MYC** proliferative axis

Suggested GO terms: GO:0007188 (adenylate-cyclase-activating G protein-coupled receptor signaling pathway), GO:0004691 (cAMP-dependent protein kinase activity), GO:0060070 (canonical Wnt signaling pathway), GO:0000165 (MAPK cascade), GO:0016575 (histone deacetylation — inverse relevant to acetylation increase), GO:0006541 (glutamine metabolic process, for the hyperammonemia axis).

### Cellular Processes
- Sustained hepatocyte proliferation and impaired terminal differentiation
- TGF-β–driven activation of hepatic stellate cells/portal fibroblasts producing the lamellar fibrotic stroma
- Altered mitochondrial biogenesis (tumor cells are notably mitochondria-rich, contributing to the granular eosinophilic cytoplasm seen histologically)
- Neuroendocrine transdifferentiation/gene expression program (neurotensin and related genes)

### Protein Dysfunction
The DNAJB1-PRKACA fusion protein represents a **gain-of-function, neomorphic chimeric kinase** — not simple PKA overactivity but a structurally altered holoenzyme with novel scaffolding and allosteric properties (PMC7793292). This is best captured in dismech schema terms as `functional_impact_category: NEOMORPHIC` on the fusion's `genetic_context`.

### Metabolic Changes
Dysregulated nitrogen/ammonia handling (GLS↑, OTC↓, GS↓) as detailed above; broader metabolomic characterization (lipidomic, amino-acid flux) is less well established in the literature retrieved here.

### Immune System Involvement
FLC tumors and their microenvironment have been targeted by immunotherapy approaches (see Treatment), and rewired cell-to-cell communication signaling — including **SPP1-CD44, MIF-ACKR3, GDF15-TGFBR2, and FGF7-FGFR** axes — has been identified via single-cell multi-omic analysis, implicating altered tumor-immune and tumor-stromal crosstalk (bioRxiv 2024.12.11.627911).

### Tissue Damage / Structural Formation Mechanisms
TGF-β overexpression is implicated in driving the characteristic **lamellar fibrosis** — parallel bands of collagen encircling tumor cell nests — a pattern distinct from cirrhotic fibrosis and specific to this tumor's stroma-tumor interaction (ScienceDirect S0740257016301162).

### Molecular Profiling Summary
- **Transcriptomics:** Neuroendocrine gene overexpression (including neurotensin) among the most significantly overexpressed genes; single-nucleus RNA-seq has mapped cell-type-specific expression programs (2024–2025 studies).
- **Epigenomics:** snATAC-seq has resolved FLC-specific chromatin accessibility and super-enhancer landscapes (CDH11, SLC16A14 loci).
- **Genomics:** Low overall mutation burden; the founding 19p13.12 deletion/fusion is essentially the sole recurrent structural event (PMC4359253).
- **Single-cell/spatial:** 2024 multi-omic single-nucleus study is the most advanced published dataset, revealing rewired intercellular signaling (SPP1-CD44, MIF-ACKR3, GDF15-TGFBR2, FGF7-FGFR).
- **Functional genomics:** In vitro drug screens have nominated HDAC inhibitors, topoisomerase I inhibitors, and the STAT3 inhibitor napabucasin as active compounds, with synergy reported when combined with Bcl-xL inhibition (Molecular Therapy, cell.com S1525-0016(23)00664-0).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Liver (hepatic parenchyma), typically arising as a solitary large mass, often in the left lobe in a substantial proportion of cases (per multiple imaging series).
- **Secondary/metastatic involvement:** Regional (hilar, celiac, mediastinal) and distant lymph nodes; lungs; peritoneum; bone; less commonly pancreas, ovary, and — rarely — cardiac/right atrial extension via IVC.
- **Body systems:** Primarily hepatobiliary/digestive system; secondary lymphatic and, in metastatic disease, respiratory and skeletal systems.

Suggested UBERON terms: UBERON:0002107 (liver), UBERON:0002370 (thymus – n/a), UBERON:0000029 (lymph node), UBERON:0002048 (lung), UBERON:0001474 (bone element), UBERON:0000992 (ovary).

**Tissue and cell level:**
- Tumor cells are large, polygonal, hepatocyte-derived (or hepatic-progenitor-derived) neoplastic epithelial cells (CL:0000182 hepatocyte, or a progenitor-like cell type given ongoing debate about cell-of-origin).
- Stromal compartment: activated portal/stellate fibroblasts producing lamellar collagen (CL:0000057 fibroblast; CL:0000632 hepatic stellate cell as a candidate contributor).
- CD68+ macrophage-lineage co-expression pattern is diagnostically notable in tumor cells themselves (aberrant marker expression rather than true macrophage infiltration is one interpretation; CL:0000235 macrophage marker used diagnostically).

**Subcellular level:**
- Tumor cells are characteristically **mitochondria-rich** (GO:0005739 mitochondrion), contributing to granular eosinophilic cytoplasm.
- Intracytoplasmic "pale bodies" (amphophilic, fibrinogen-containing inclusions) and "hyaline bodies" (smaller, intensely eosinophilic) are seen in roughly half of cases (AASLD Pathology Pearls; ScienceDirect S0740257016301162).

**Localization:** Typically a single large hepatic mass (5–20 cm); bilobar or multifocal presentation is less common. No established lateralization pattern beyond frequent left-lobe predominance noted in some imaging series.

---

## 8. Temporal Development

- **Onset:** Adolescent/young-adult onset is classic (peak ~15–19 years in registry data), with a smaller elderly-onset peak (~70–74 years); reported age range 2–74 years (npj Precision Oncology 2023).
- **Onset pattern:** Insidious — symptoms (abdominal pain, distension, malaise) typically develop gradually over weeks to months before diagnosis, contributing to advanced stage at presentation.
- **Disease stages:** No FLC-specific staging system exists; conventional HCC/AJCC liver staging or the Milan-type resectability framework is generally applied, alongside surgical categorization into resectable vs. unresectable/advanced disease.
- **Progression rate:** Variable but often aggressive once metastatic; **recurrence after resection is common — reported in up to 86% of patients** in some surgical series (Yamashita et al., cited in cco.amegroups.org review).
- **Disease course pattern:** Typically progressive with a high rate of locoregional and distant recurrence; not classically relapsing-remitting.
- **Remission patterns:** Surgical resection (with negative margins) offers the only realistic chance of durable remission; spontaneous remission is not described. Recurrence, when resectable again, can still yield meaningful survival benefit (median OS 122 months with repeat resection of recurrence vs. 37 months without, per the Yamashita series).
- **Critical periods:** Early surgical intervention while disease remains resectable is the single most important modifiable window; delayed diagnosis due to nonspecific symptoms is a major driver of poor outcomes.

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence:** Age-adjusted U.S. incidence is approximately **0.02 per 100,000 person-years**, roughly **100-fold lower** than the ~1.99 per 100,000 annual incidence of conventional HCC (npj Precision Oncology 2023).
- FLC represents **~1–2% of all hepatocellular carcinoma cases** in the U.S. (PubMed:32052215; Fibrofoundation).
- A 2023 computational/tiered clinical-data analysis suggests **true incidence may be 5- to 8-fold higher** than prior registry-based estimates, implying substantial historical under-ascertainment (PMC10034241/npj Precision Oncology 2023).
- Bimodal age distribution: incidence peaks at ages 15–19 and 70–74.

### Inheritance Pattern
FLC is essentially **sporadic**, driven by a **somatic** (non-inherited) DNAJB1-PRKACA fusion. No Mendelian inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, founder-effect, or carrier-frequency data apply in the conventional sense, since the causal lesion is not transmitted through the germline. A single case report of concurrent germline + somatic TP53 mutation raises a hypothesis-generating (not established) link to Li-Fraumeni-spectrum tumors in rare instances (Familial Cancer 2017), but this is not a recognized recurrent inheritance mechanism for FLC as a class.

### Population Demographics
- **Race/ethnicity:** >85% non-Hispanic white in U.S. cohorts; ~6% Chinese American, ~4% Black, ~4% white Hispanic (PubMed:32052215).
- **Geographic distribution:** No clearly defined endemic regions; most epidemiological data derive from U.S. (SEER, NCDB) cohorts, with case series also reported from Europe and Asia, though comparative incidence data outside the U.S. are sparse.
- **Sex ratio:** No strong sex predominance is consistently reported in the largest series (contrasts with conventional HCC's male predominance), though some surgical-outcome cohorts note male sex as a favorable prognostic factor.
- **Age distribution:** Predominantly adolescents/young adults, with a smaller elderly subgroup.

---

## 10. Diagnostics

### Laboratory Tests
- **Alpha-fetoprotein (AFP):** Characteristically **normal** — an important distinguishing feature from conventional HCC, where AFP is often elevated (emedicine.medscape.com/278354-workup).
- **Vitamin B12-binding globulin (transcobalamin):** Elevated in some series (classic but not universally sensitive/specific marker).
- **Neurotensin:** Elevated in a subset of patients but **not sufficiently sensitive or specific** for stand-alone diagnostic use (PMC search results synthesis).
- **Procalcitonin:** A newly proposed (2025) candidate tumor biomarker for diagnosis and follow-up, based on case reports and a literature review (medRxiv 2025.11.18.25340286; PMC12907347) — still investigational.
- **Serum ammonia:** Elevated in the rare hyperammonemic encephalopathy presentation.

### Imaging Studies
- **CT:** Large (7–20 cm), heterogeneous, hypervascular, well-defined lobulated mass; **central non-enhancing stellate scar** in >80% of tumors at diagnosis; calcifications in **33–68%** of cases, usually within the central scar (AJR 10.2214/AJR.13.11117; PMC4112400).
- **MRI:** Near-isointense to liver on T1, hyperintense on T2; central scar is hypointense on both T1 and T2 (a helpful distinguishing feature from focal nodular hyperplasia, whose central scar is typically T2-hyperintense and lacks calcification).
- **Distinguishing FNH vs. FLC:** Low T2 signal intensity and presence of calcification in the central scar favor FLC over FNH.

### Biopsy/Pathology
- **Histopathology:** Large polygonal/spindled cells with abundant granular eosinophilic cytoplasm, vesicular nuclei, prominent macronucleoli; paucicellular fibrous stroma in parallel lamellae; pale bodies/hyaline bodies in ~50% of cases.
- **Immunohistochemistry:** **CK7 and CD68 co-expression** — when combined with compatible morphology, this combination is considered diagnostic of FLC (PMC search synthesis).

### Molecular/Genetic Testing
- **Break-apart FISH for PRKACA rearrangement:** Positive in 99% (102/103) of classic FLC cases in the largest multicenter validation study; a clinically validated, high-sensitivity/specificity assay (PubMed:35777788).
- **RT-PCR for DNAJB1-PRKACA fusion transcript:** Successful detection in 92% (24/26) of tested cases; fusion transcript essentially specific to FLC among primary liver tumors tested, though shared with rare oncocytic pancreatobiliary neoplasms (PMC5758901; Modern Pathology 2019).
- **Targeted NGS fusion panels** (e.g., MSK-IMPACT/MSK-Fusion hybridization-capture assays) are used clinically to detect the fusion (search synthesis).
- Commercial clinical assay example: Mayo Clinic Laboratories' PRKAF test (FISH for PRKACA rearrangement, tissue-based).

### Clinical Criteria / Differential Diagnosis
No DSM/ICD-based diagnostic criteria apply (this is a solid-organ malignancy); diagnosis rests on the combination of clinical context (young patient, no cirrhosis, normal AFP), imaging (central scar with calcification), histology, and CK7/CD68 IHC, confirmed by DNAJB1-PRKACA fusion testing (FISH, RT-PCR, or NGS). Key differentials: focal nodular hyperplasia (shares central scar but lacks fusion/calcification pattern), conventional HCC, hepatocellular adenoma, and other oncocytic hepatobiliary/pancreatic tumors that can rarely share the fusion.

### Screening
No population or genetic screening program exists for FLC, consistent with its sporadic, non-heritable molecular basis and rarity.

---

## 11. Outcome/Prognosis

### Survival Statistics (SEER/NCDB-based)
- **Overall median survival:** ~24.5 months in a recent SEER cohort analysis (JCO 2024.42.16_suppl.e16213); considerably better in surgically managed patients (**median survival ~75 months**) (Dove Medical Press IJGM).
- **Age-stratified survival (SEER, n=225):** Median survival 85 months for patients ≤19 years; 29 months for ages 20–59; 12 months for ages ≥60 — indicating **younger age is strongly favorably prognostic** (search synthesis of SEER analyses).
- **Stage-dependent survival:** 1-year OS 67–100%; 5-year OS 28–65% across series; **5-year OS ~80% for resectable disease vs. ~10% for advanced/unresectable disease** (systematic review/meta-analysis, PMC10073062).
- **Surgical outcome comparison:** 3-year survival ~100% after liver resection vs. ~76% after liver transplantation in one comparative series (search synthesis).

### Prognostic Factors
- **Favorable:** Male sex, younger age, white race, surgical resectability, combined liver + lymph node resection (vs. liver resection alone).
- **Unfavorable:** Vascular invasion, lymph node metastasis, advanced/unresectable disease at diagnosis, older age at diagnosis.

### Recurrence
Recurrence after resection is common — reported in **86% of patients** in one series (Yamashita et al.) — most frequently to intra-abdominal/intrathoracic lymph nodes, liver, lungs, and peritoneum. Notably, **surgical resection of recurrent disease** is associated with substantially improved median OS (122 months) compared to non-surgical management of recurrence (37 months), underscoring an aggressive surgical approach even at relapse.

### Morbidity
Beyond mortality, morbidity includes recurrent surgical burden, paraneoplastic hyperammonemic encephalopathy (potentially severe/refractory), and — rarely — thromboembolic and cardiac complications from tumor extension. Systematic QoL outcome data (EQ-5D/PROMIS) specific to FLC were not identified in this search.

---

## 12. Treatment

### Surgical/Interventional (Mainstay)
- **Surgical resection** remains the **only potentially curative modality** and the single most important determinant of outcome, with 5-year OS of 50–76% in resected cohorts (cco.amegroups.org). NCIT: `NCIT:C15329` (Surgical Procedure); more specific `NCIT:C158**` hepatectomy-type terms as applicable.
- **Orthotopic liver transplantation (OLT):** Reserved for selected unresectable cases; outcomes are generally inferior to resection (3-year survival ~76% vs. ~100% for resection in comparative data), but transplantation (including living-donor transplant) has been reported even in cases with hilar lymph node metastasis (PubMed:29633928).
- **Lymphadenectomy:** Combined liver resection + lymph node dissection is associated with better survival than liver resection alone, reflecting the disease's propensity for nodal spread.
- **Re-resection of recurrence:** Associated with markedly improved survival versus non-operative management of relapse (see Outcome section).

### Pharmacotherapy — No Established Standard of Care
There is **no FDA-approved systemic therapy specific to FLC**; conventional HCC systemic regimens (sorafenib, lenvatinib, other multikinase inhibitors) have shown limited/inconsistent efficacy, reflecting FLC's distinct molecular biology.

### Immunotherapy
- **Checkpoint inhibitor combinations:** Case reports describe tumor control with **atezolizumab + bevacizumab** re-administration (PMC11659117).
- **Nivolumab + fluorouracil + interferon alfa-2b:** Active phase I/II trial at MD Anderson (**NCT04380545**) for unresectable FLC, estimated primary completion 2028 (`NCIT:C2963` for immune checkpoint inhibitor class; therapeutic_agent CHEBI/NCIT terms for nivolumab, 5-FU, interferon alfa-2b).
- **Therapeutic peptide vaccine (2025 landmark trial):** A **phase 1 trial of a DNAJB1-PRKACA fusion-neoantigen peptide vaccine**, combined with **nivolumab + ipilimumab**, was reported safe with encouraging early efficacy — **disease control rate 75% (9/12)** in patients completing the priming phase, including **3 partial responses (25%)** (*Nature Medicine* 2025, 10.1038/s41591-025-03995-y). This is the first therapy directly targeting the fusion neoantigen immunologically and represents the most significant recent (2025) treatment advance.

### Targeted/Experimental Therapies
- **ENMD-2076** (oral Aurora A kinase/VEGFR/FLT3/FGFR3 inhibitor): Phase 2 multicenter trial (**NCT02234986**) met its Stage 1 non-futility endpoint and advanced to Stage 2, but **final results were modest — only 1/N (3%) partial response, 57% stable disease** — insufficient to support further single-agent development (PubMed:32154962; CASI Pharmaceuticals press releases). Rationale was AURKA overexpression downstream of the fusion.
- **DT2216** (Bcl-xL-targeting PROTAC/degrader) **+ irinotecan:** Phase I/II trial (**NCT06620302**) for relapsed/refractory pediatric, adolescent, and young-adult solid tumors including FLC, building on preclinical synergy between Bcl-xL inhibition and HDAC/topoisomerase I inhibitors/napabucasin (Fibrofoundation; Molecular Therapy 2023).
- **Napabucasin** (STAT3/cancer-stemness inhibitor), **HDAC inhibitors**, and **topoisomerase I inhibitors** showed the most potent activity in a preclinical drug screen ("preclinical magic bullet" study), with synergy when combined with Bcl-xL inhibition — supporting the DT2216 combination trial rationale (Molecular Therapy 2023, S1525-0016(23)00664-0).
- **CRTC2/p300 targeting:** Nominated as a therapeutic strategy following the 2024 mechanistic discovery of SIK inactivation/CRTC2-p300 deregulation by the fusion kinase (Cancer Discovery 2024) — not yet in clinical testing per available search results.

### Supportive Care
Management of paraneoplastic hyperammonemic encephalopathy (a proposed treatment algorithm exists in the literature — PMC4828114) typically involves ammonia-lowering strategies (e.g., lactulose, rifaximin, sometimes dialysis/CRRT) alongside tumor-directed therapy, since standard cirrhosis-based hyperammonemia treatments may be less effective given the tumor-intrinsic ammoniagenic mechanism.

### Treatment Algorithm Summary
1. Assess resectability at diagnosis (imaging + multidisciplinary review).
2. If resectable: hepatic resection + regional lymphadenectomy — curative-intent, best survival outcomes.
3. If borderline/unresectable: consider liver transplantation in selected cases; consider clinical trial enrollment (peptide vaccine + checkpoint inhibitors, nivolumab-based regimens, DT2216 combinations).
4. At recurrence: re-resection where feasible, given demonstrated survival benefit; otherwise systemic/experimental therapy.
5. Manage paraneoplastic complications (notably hyperammonemic encephalopathy) proactively.

Suggested NCIT terms: `NCIT:C15329` (Surgical Procedure), `NCIT:C15289` (Organ Transplantation), `NCIT:C1647` (Nivolumab), `NCIT:C2039` (Ipilimumab — verify code), `NCIT:C328` (Interferon alfa-2b — verify code), `NCIT:C561` (Fluorouracil), `NCIT:C15346` (Vaccination, for the peptide vaccine), `NCIT:C15632` (Chemotherapy).

---

## 13. Prevention

- **Primary prevention:** None established, since there are no modifiable environmental/lifestyle risk factors and the driver mutation is a sporadic somatic event.
- **Secondary prevention/screening:** No population or genetic screening program exists; early recognition depends on clinical suspicion in young patients presenting with an incidental hepatic mass, especially with the CT/MRI central-scar-with-calcification pattern and normal AFP.
- **Tertiary prevention:** Post-resection surveillance imaging is standard practice to detect recurrence early, given the high (up to 86%) recurrence rate and the demonstrated survival benefit of re-resection.
- **Genetic counseling:** Not routinely indicated given the sporadic, somatic nature of the disease; would only be considered in the rare context of a suspected co-occurring germline cancer-predisposition syndrome (e.g., the isolated TP53/Li-Fraumeni-spectrum case report).
- **Public health/environmental interventions:** Not applicable, as no environmental driver has been identified.

---

## 14. Other Species / Natural Disease

The literature retrieved in this search did not identify well-characterized **naturally occurring** FLC in companion animals or wildlife (unlike some other cancers with recognized veterinary correlates via OMIA). FLC-like disease in other species has not been prominently reported in the sources found. Genetically engineered animal models (see below) are the primary cross-species research tool, rather than natural veterinary disease. (This is a gap that would benefit from a dedicated OMIA/veterinary-literature search if higher confidence is needed.)

---

## 15. Model Organisms

### Genetically Engineered Mouse Models
- **Transgenic/genetically engineered mouse models** expressing DNAJB1-PKA(c) in the liver have been developed; initial adult-liver expression models produced FLC-resembling tumors but at **low penetrance** (bioRxiv 2023.12.06.569624; PMC11582006).
- Mouse models combining **DNAJB1-PRKACA expression with β-catenin activation** show significantly enhanced tumorigenesis, supporting a two-hit cooperative model relevant to human Wnt-pathway alterations (PNAS:1716483114; PubMed:29162699).

### Zebrafish Models
A **zebrafish model** expressing the DNAJB1-PRKACA fusion has been used to study fusion-induced **liver inflammation** as an early step in FLC pathogenesis (bioRxiv 781583).

### Patient-Derived Models
- **Patient-derived xenografts (PDX)** established from patient tumor tissue or ascites in immunocompromised mice, and **PDX-derived organoids** composed of FLC epithelial cells, endothelial progenitor cells, and stellate cells, have been developed by several research groups (PMC11582006).
- **CRISPR/Cas9-engineered ex vivo hepatocyte models:** Mature hepatocytes edited to express the fusion gene (and, in some models, additional FLC-associated mutations) to generate FLC-like cells for mechanistic and drug-screening studies.
- A commercial PDX model (Crown Bio's LI5132) is available for liver cancer/FLC-relevant preclinical drug testing.

### Model Limitations
Current models — particularly the low-penetrance transgenic mouse — do not fully recapitulate the human disease's histology (lamellar fibrosis), long latency, and metastatic behavior; PDX/organoid models better preserve tumor-stroma heterogeneity but are lower-throughput and harder to scale for large drug screens. The Aurora kinase inhibitor ENMD-2076, effective in some preclinical models, translated to only modest clinical activity, illustrating a translational fidelity gap.

### Research Applications
These models collectively support: (1) validation of the DNAJB1-PRKACA fusion as a necessary/sufficient driver, (2) testing of cooperating mutations (β-catenin), (3) mechanistic dissection of the SIK-CRTC2-p300 axis and AURKA/MYC network, and (4) preclinical drug screening (napabucasin, HDAC inhibitors, topoisomerase I inhibitors, Bcl-xL degraders such as DT2216).

---

## Summary of Key Ontology Term Suggestions

| Category | Term |
|---|---|
| MONDO | MONDO:0006210 (Fibrolamellar hepatocellular carcinoma) |
| Orphanet | ORPHA:401920 |
| Gene | HGNC:9380 (PRKACA), HGNC:14887 (DNAJB1), HGNC:11998 (TP53) |
| GO (molecular function) | GO:0004691 (cAMP-dependent protein kinase activity) |
| GO (biological process) | GO:0060070 (canonical Wnt signaling), GO:0000165 (MAPK cascade), GO:0006541 (glutamine metabolic process) |
| GO (cellular component) | GO:0005739 (mitochondrion) |
| CL | CL:0000182 (hepatocyte), CL:0000057 (fibroblast) |
| UBERON | UBERON:0002107 (liver), UBERON:0000029 (lymph node), UBERON:0002048 (lung) |
| HP | HP:0002240 (Hepatomegaly), HP:0002027 (Abdominal pain), HP:0000771 (Gynecomastia), HP:0001982 (Hyperammonemia), HP:0000952 (Jaundice) |
| NCIT (treatment) | NCIT:C15329 (Surgical Procedure), NCIT:C15289 (Organ Transplantation), NCIT:C15632 (Chemotherapy), NCIT:C15346 (Vaccination) |
| CHEBI | (fluorouracil, therapeutic agents — verify specific CHEBI IDs before curation) |

---

## Notable Evidence Gaps / Curation Cautions

1. **CTNNB1 mutation frequency in human FLC** — the mouse-model cooperation with β-catenin is well documented, but a precise human-cohort mutation frequency was not retrievable in this pass and should be verified against the primary genomic-landscape papers (Oncotarget 2015; subsequent cohort studies) before citing a specific percentage.
2. **DNAJB1-PRKACA specificity** — not absolutely exclusive to FLC (also found in oncocytic pancreatobiliary neoplasms); curation should qualify "pathognomonic" claims accordingly.
3. **Natural veterinary disease** — no strong evidence of naturally occurring FLC in other species was found; this section should be flagged as a gap rather than asserted as "none exists" without a dedicated OMIA search.
4. Quantitative QoL data (EQ-5D/SF-36/PROMIS) specific to FLC patients were not identified and likely do not exist in validated form.

## Sources

- [DNAJB1-PRKACA fusion peptide immunotherapy (Nat Commun 2022)](https://www.nature.com/articles/s41467-022-33746-3)
- [DNAJB1-PRKACA interacts with β-catenin (PubMed 29162699)](https://pubmed.ncbi.nlm.nih.gov/29162699/)
- [SIK/CRTC2/p300 mechanism (Cancer Discovery 2024)](https://doi.org/10.1158/2159-8290.cd-24-0634)
- [DNAJB1–PRKACA and β-catenin (PNAS)](https://www.pnas.org/doi/10.1073/pnas.1716483114)
- [Zebrafish model liver inflammation](https://www.biorxiv.org/content/10.1101/781583.full.pdf)
- [Oncogenic addiction to DNAJB1-PRKACA (PubMed 36302174)](https://pubmed.ncbi.nlm.nih.gov/36302174/)
- [Orphanet: Fibrolamellar hepatocellular carcinoma](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=401920)
- [Population-based observational study (PubMed 32052215)](https://pubmed.ncbi.nlm.nih.gov/32052215/)
- [Defining incidence via tiered computational analysis (npj Precision Oncology 2023)](https://www.nature.com/articles/s41698-023-00371-2)
- [Fibrolamellar Cancer Foundation: What is Fibrolamellar?](https://fibrofoundation.org/about-fibro/what-is-fibrolamellar-carcinoma/)
- [Peptide vaccine phase 1 trial (Nature Medicine 2025)](https://www.nature.com/articles/s41591-025-03995-y)
- [NCT04380545 — Nivolumab/5-FU/IFN-α2b](https://clinicaltrials.gov/study/NCT04380545)
- [NCT02234986 — ENMD-2076 phase 2](https://clinicaltrials.gov/study/NCT02234986)
- [ENMD-2076 phase 2 results (PubMed 32154962)](https://pubmed.ncbi.nlm.nih.gov/32154962/)
- [CASI Pharmaceuticals ENMD-2076 update](https://www.prnewswire.com/news-releases/casi-pharmaceuticals-provides-update-on-phase-2-trial-of-enmd-2076-in-fibrolamellar-carcinoma-300313638.html)
- [DT2216 clinical trial (Fibrofoundation)](https://fibrofoundation.org/dt2216-clinical-trial-now-open/)
- [Framework for FLC research and clinical trials (Nat Rev Gastro Hepatol)](https://www.nature.com/articles/s41575-022-00580-3)
- [Molecular testing for clinical diagnosis (PMC5758901)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5758901/)
- [Procalcitonin as tumor marker (PMC12907347)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12907347/)
- [Treatment and prognosis national perspective (PMC4596238)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4596238/)
- [SEER epidemiology and survival (JCO 2024)](https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.e16213)
- [5-year cancer survival SEER (PubMed 37307948)](https://pubmed.ncbi.nlm.nih.gov/37307948/)
- [Survival factors (Dove Press IJGM)](https://www.dovepress.com/factors-influencing-overall-survival-for-patients-with-fibrolamellar-h-peer-reviewed-fulltext-article-IJGM)
- [Treatment/prognosis systematic review meta-analysis (PMC10073062)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10073062/)
- [PKA scaffolding function (PMC6533061)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6533061/)
- [Road map for fibrolamellar carcinoma (Dove Press JHC)](https://www.dovepress.com/road-map-for-fibrolamellar-carcinoma-progress-and-goals-of-a-diversifi-peer-reviewed-fulltext-article-JHC)
- [Oncogenic PKA increases MYC (PMC9925115)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9925115/)
- [PRKACA as therapeutic target (ScienceDirect S2772572322001911)](https://www.sciencedirect.com/science/article/pii/S2772572322001911)
- [Neurotensin as cAMP/co-mitogen source (PMC6707953)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6707953/)
- [PKA holoenzyme structure (PMC7793292)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7793292/)
- [AASLD Pathology Pearls: FLC](https://www.aasld.org/liver-fellow-network/core-series/pathology-pearls/fibrolamellar-hepatocellular-carcinoma)
- [Imaging features (AJR)](https://ajronline.org/doi/10.2214/AJR.13.11117)
- [FLC histologically unique tumor (ScienceDirect S0740257016301162)](https://www.sciencedirect.com/science/article/abs/pii/S0740257016301162)
- [Murine models development (bioRxiv 2023.12.06.569624)](https://www.biorxiv.org/content/10.1101/2023.12.06.569624v2.full)
- [Models of FLC review (PMC11582006)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11582006/)
- [Management of FLC (Chinese Clinical Oncology)](https://cco.amegroups.org/article/view/21275/html)
- [Surgical outcomes single-center (World J Surg Oncol)](https://link.springer.com/article/10.1186/s12957-020-01855-2)
- [Resection vs transplantation outcomes (PubMed 11112043)](https://pubmed.ncbi.nlm.nih.gov/11112043/)
- [Living-donor transplant with nodal metastasis (PubMed 29633928)](https://pubmed.ncbi.nlm.nih.gov/29633928/)
- [FLC absence of risk factors case report (PMC9750232)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9750232/)
- [FLC advances/challenges/opportunities review (PMC12576631)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12576631/)
- [Hyperammonemic encephalopathy (PMC6304646)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6304646/)
- [Molecular basis of hyperammonemic encephalopathy (PMC9922532)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9922532/)
- [Hyperammonemic encephalopathy treatment algorithm (PMC4828114)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4828114/)
- [Single-cell multi-omic analysis (bioRxiv 2024.12.11.627911)](https://www.biorxiv.org/content/10.1101/2024.12.11.627911v1)
- [snATAC-seq analysis (Nature Scientific Reports)](https://www.nature.com/articles/s41598-026-44899-2)
- [Genomic landscape whole genome sequencing (PMC4359253)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4359253/)
- [Preclinical magic bullet HDAC/napabucasin (Molecular Therapy)](https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(23)00664-0)
- [DNAJB1-PRKACA FISH specificity (ScienceDirect S089339522201417X)](https://www.sciencedirect.com/science/article/pii/S089339522201417X)
- [FISH validation study (PubMed 35777788)](https://pubmed.ncbi.nlm.nih.gov/35777788/)
- [Fusion not fully specific — oncocytic neoplasms (Modern Pathology)](https://www.nature.com/articles/s41379-019-0398-2)
- [TP53 germline/somatic case report (Familial Cancer)](https://link.springer.com/article/10.1007/s10689-017-9998-5)
- [CT/MRI case series (PMC4112400)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4112400/)
- [Medscape: FLC Practice Essentials](https://emedicine.medscape.com/article/278354-overview)
- [NORD: Fibrolamellar Carcinoma](https://rarediseases.org/rare-diseases/fibrolamellar-carcinoma/)
- [Liver Foundation Australia: FLC](https://liver.org.au/your-liver/liver-cancer/fibrolamellar-carcinoma-flc/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 35 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 14 |
| Terms whose name was checked | 22 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0006210` (3 mentions) - the report calls it "if available", "Fibrolamellar hepatocellular carcinoma"; MONDO calls it **fibrolamellar hepatocellular carcinoma**
- `HP:0033834` (1 mention) - the report calls it "Fatigue-related"; HP calls it **Malaise**
- `GO:0016575` (2 mentions) - the report calls it "histone deacetylation, inverse direction relevant", "histone deacetylation — inverse relevant to acetylation increase"; GO calls it **obsolete histone deacetylation**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C158` (1 mention) - NCIT does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016575` (obsolete histone deacetylation) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007188` (1 mention) - the report calls it "adenylate-cyclase-activating G protein-coupled receptor signaling pathway"; GO calls it **adenylate cyclase-modulating G protein-coupled receptor signaling pathway**
- `GO:0006541` (2 mentions) - the report calls it "glutamine metabolic process, for the hyperammonemia axis"; GO calls it **L-glutamine metabolic process**
- `UBERON:0002370` (1 mention) - the report calls it "thymus – n/a"; UBERON calls it **thymus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0006210` - called "if available", "Fibrolamellar hepatocellular carcinoma"
- `GO:0016575` - called "histone deacetylation, inverse direction relevant", "histone deacetylation — inverse relevant to acetylation increase"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `PubMed`, `PNAS`, `Oncotarget`.
