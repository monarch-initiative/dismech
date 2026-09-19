---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T00:42:25.287068'
end_time: '2026-07-31T00:48:31.319941'
duration_seconds: 366.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 4B
  mondo_id: MONDO:0013931,PEX6-related,OMIM:614863,also-called-SCAR3/cerebellar-ataxia-blindness-deafness,non-classic-Zellweger-spectrum
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 29
  total_cost_usd: 1.8401709999999996
  session_id: d6f6fe29-6d81-5583-8980-e24cd536256a
  stop_reason: end_turn
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 4B
- **MONDO ID:** MONDO:0013931,PEX6-related,OMIM:614863,also-called-SCAR3/cerebellar-ataxia-blindness-deafness,non-classic-Zellweger-spectrum (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 4B** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Research Report: Peroxisome Biogenesis Disorder 4B (PEX6-Related)

## Nomenclature Note (read first)

The identifiers supplied for this target collapse **two nosologic lineages that are now understood to be the same molecular disease** but that were named independently before PEX6 was identified as the causal gene:

1. **Peroxisome biogenesis disorder 4B (PBD4B)**, OMIM **#614863**, MONDO:0013931 — the peroxisomal-biology naming track (PEX6 complementation group 4, "B" = milder allelic series vs. the classic-Zellweger 4A/#614862 track), encompassing **neonatal adrenoleukodystrophy (NALD)** and **infantile Refsum disease (IRD)**, the two milder ends of the **Zellweger spectrum disorder (ZSD)** continuum.
2. **"SCAR3" / autosomal recessive spinocerebellar ataxia‑blindness‑deafness syndrome (SCABD)** — an older clinical/neurogenetics label applied before the causal peroxisomal gene defect was recognized in these families.

Monarch Initiative confirms these are **genuinely co-referent, not a Named-Entity-Confusion collision**: MONDO:0013931's exact-synonym list includes *"Spinocerebellar ataxia, autosomal recessive 3," "SCAR3," "SCABD,"* and *"Autosomal recessive cerebellar ataxia-blindness-deafness syndrome"* alongside *"Peroxisome biogenesis disorder type 4B"* and *"PBD4B,"* all mapped to the single PEX6-caused entity (Monarch Initiative, MONDO:0013931). The MONDO definition itself states: *"This condition involves a PEX6 defect causing early-onset cerebellar ataxia combined with hearing loss and blindness. Patients may experience demyelinating peripheral motor neuropathy, with cerebral MRI showing cerebellar white matter alterations without atrophy."* This SCAR3/SCABD framing describes a **particular non-classic, adult/late-childhood-recognized clinical presentation** of PEX6-ZSD (ataxia + sensorineural hearing loss + retinal/visual impairment, sometimes without the neonatal hypotonia/dysmorphism of classic Zellweger) — it is one point on the same PBD4B allelic-severity continuum, not a separate disease. This report treats PBD4B/OMIM:614863/SCAR3-SCABD/NALD-IRD(PEX6) as one disease entity, the **PEX6-caused, non-classic (milder) end of Zellweger spectrum disorder**, and notes where sub-phenotypes (ataxia-predominant vs. NALD/IRD-classic-milder vs. Heimler-syndrome-mildest) diverge.

---

## 1. Disease Information

**Overview.** Peroxisome biogenesis disorder 4B (PBD4B) is an autosomal recessive **peroxisomal biogenesis disorder** caused by biallelic (or, rarely, a specific monoallelic allelic-expression-imbalance mechanism — see §4) pathogenic variants in **PEX6**. It sits within the **Zellweger spectrum disorder (ZSD)** continuum — a single phenotypic spectrum historically split into three named entities (Zellweger syndrome > neonatal adrenoleukodystrophy [NALD] > infantile Refsum disease [IRD], severe→mild) that are now understood to reflect residual peroxisomal function rather than distinct diseases (GeneReviews, NBK1448). PEX6 defects are the **second most common cause of ZSD after PEX1**, accounting for roughly 10–14.5% of ZSD cases (GeneReviews, NBK1448; Ebberink et al. 2010, PMID:19877282). PEX6-caused ZSD spans an unusually wide severity range — from classic lethal neonatal Zellweger syndrome (PBD4A, OMIM:614862) through NALD/IRD-type PBD4B, to an ataxia–deafness–blindness (SCAR3/SCABD) presentation recognized in later childhood/adulthood, to the mildest end, **Heimler syndrome 2** (hearing loss + amelogenesis imperfecta ± mild/late retinal disease, OMIM:616617).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype, milder/NALD-IRD end) | **#614863** PEROXISOME BIOGENESIS DISORDER 4B; PBD4B |
| OMIM (phenotype, classic Zellweger end, same gene) | #614862 PBD4A |
| OMIM (gene) | *601498 PEX6 |
| OMIM (mildest allelic end) | #616617 Heimler syndrome 2 (HMLR2) |
| MONDO | MONDO:0013931 |
| Orphanet (gene page) | ORPHA PEX6 gene entry; component disorders NALD ORPHA:44, Infantile Refsum disease ORPHA:772, Zellweger syndrome ORPHA:912, umbrella "Peroxisome biogenesis disorder, Zellweger syndrome spectrum" ORPHA:79189 |
| MeSH | Zellweger Syndrome (D015211) |
| ICD-11 | 5C56.0 Zellweger spectrum |
| HGNC | PEX6, HGNC:8858 |

**Synonyms:** PBD4B; NALD (PEX6-caused); IRD/Infantile Refsum disease (PEX6-caused); SCAR3; SCABD; Autosomal recessive spinocerebellar ataxia-blindness-hearing loss syndrome; Autosomal recessive cerebellar ataxia-blindness-deafness syndrome (Monarch Initiative MONDO:0013931).

**Evidence basis of this report:** predominantly **aggregated disease-level resources** (OMIM, GeneReviews consensus chapter, Orphanet, systematic mutation surveys of 75–77 PEX6 patients) supplemented by **individual case reports/small case series** (Mixteco founder cluster n=3; late-onset PEX6 case n=1; French-Canadian founder cohort) rather than large single-cohort EHR data — consistent with an ultra-rare monogenic disease.

---

## 2. Etiology

**Disease causal factor:** Exclusively genetic/mechanistic — biallelic (or the specific monoallelic AEI mechanism, see §4) pathogenic loss-of-function or hypomorphic variants in **PEX6** (6p21.1), encoding an AAA-ATPase peroxin required for peroxisomal matrix-protein import. There is no known environmental, infectious, or acquired cause; PBD4B is a Mendelian disorder in the strict sense.

**Genetic risk factors:**
- Biallelic PEX6 pathogenic variants (missense, nonsense, frameshift, splice-site, large deletion) — causal.
- The specific **c.2578C>T (p.Arg860Trp)** variant acting *in the heterozygous state* when in cis with a 3′UTR polyadenylation-site variant (rs144286892, c.*442_445delTAAA) that causes allelic expression imbalance (AEI), effectively producing dominant-like disease from one overexpressed hypomorphic allele (Falkenberg et al. 2017, *AJHG*, PMC/ResearchGate; identified in 7 unrelated ZSD patients + 1 affected half-sibling).
- Population-specific founder alleles increase local risk: a French-Canadian PEX6 founder mutation raising ZSD incidence in the Saguenay–Lac-Saint-Jean region of Quebec toward ~1/12,000 (vs. ~1/50,000 general North American incidence) (PMC3483250); a Mixteco-population founder variant **c.1409G>C (p.Gly470Ala)** identified in 2/3 related neonatal cases from Central California (Slaton et al. 2023, Cureus, PMID:37842507).
- Consanguinity increases risk in any AR disorder; not PEX6-specific but relevant to case ascertainment in the Mixteco and other founder clusters.

**Protective factors:** None specifically documented for PEX6-ZSD; general "protective" modifiers are hypomorphic (residual-function) missense alleles rather than null alleles — i.e., allelic severity itself is the modifying axis (genotype–phenotype correlation, §4), not an independent protective factor.

**Gene–environment interactions:** None established; this is a cell-autonomous biosynthetic/organelle-biogenesis defect not modulated by known exposures. (No CTD or GWAS-catalog environmental signal for PEX6-ZSD was found in this search; the disease is fully explained by the biallelic genetic lesion.)

Suggested terms: **HP:0010984** (Digenic inheritance) is *not* applicable — PEX6-ZSD is monogenic AR, with the AEI mechanism being an unusual *cis*-regulatory dosage effect on a single locus rather than true digenic inheritance.

---

## 3. Phenotypes

Phenotype burden and severity track the ZSD continuum; PBD4B (PEX6, NALD/IRD-range) sits milder than classic Zellweger (PBD4A) but generally more severe than PEX1 p.Gly843Asp-type mild ZSD, though PEX6 alleles span an unusually broad range down to Heimler syndrome.

| Phenotype | Type | Onset/course | Notes / frequency (qualitative, per GeneReviews synthesis) | Suggested HPO |
|---|---|---|---|---|
| Hypotonia | Sign | Neonatal–infantile | Common at the more severe end | HP:0001252 |
| Developmental delay / intellectual disability | Sign | Infantile, progressive or static | Variable; "some have normal intellect" per GeneReviews | HP:0001263 / HP:0001249 |
| Sensorineural hearing loss | Sign, progressive | Childhood onset in milder forms, may be presenting feature (e.g., school hearing-test detection in late-onset case, PMID:25079577) | Frequent across the whole PEX6 spectrum, present in Heimler syndrome even without other ZSD features | HP:0000407 |
| Retinal dystrophy / retinitis-pigmentosa-like changes | Sign, progressive | Variable, sometimes late-onset | Contributes to Usher-syndrome misdiagnosis (PEX6 "Usher mimic," ScienceDirect/PMC) | HP:0000556 (Retinal dystrophy) / HP:0000510 (Rod-cone dystrophy) |
| Cataracts | Sign | Can be congenital in atypical presentations | GeneReviews notes "atypical presentations include congenital cataracts" | HP:0000518 |
| Cerebellar ataxia | Sign, progressive | Early-onset in the SCAR3/SCABD presentation | Defining feature of the MONDO:0013931 "ataxia-blindness-deafness" synonym cluster; cerebellar white-matter changes without atrophy on MRI | HP:0001251 |
| Demyelinating peripheral (motor) neuropathy | Sign | Progressive | Explicit in MONDO definition for this entity | HP:0003431 (or more specific demyelinating-neuropathy term) |
| Leukodystrophy / progressive demyelination | Sign/imaging | Childhood–adolescence in milder ZSD, can mimic X-ALD | Presenting as symmetric leukodystrophy on MRI in a late-onset PEX6 case (PMID:25079577) | HP:0002352 (or leukoencephalopathy term) |
| Hepatic dysfunction / liver disease | Lab/sign | Can be present from infancy, progressive to fibrosis | Basis for cholic-acid trials (§12) | HP:0001392 |
| Adrenal insufficiency | Sign/lab | Variable onset | Managed with replacement therapy (GeneReviews) | HP:0000846 |
| Osteopenia | Sign | Progressive with disease duration | Surveillance target; vitamin D/bisphosphonate management | HP:0000938 |
| Renal oxalate stones | Sign | Later disease course | Surveillance via urine oxalate:creatinine ratio | HP:0000787 |
| Esophageal varices | Complication | Advanced liver disease | Managed with sclerosing therapy | (secondary to portal hypertension; no dedicated HP term beyond varices) |
| Seizures | Sign | Variable | Present in a minority; standard anti-seizure management, "no contraindicated agents" | HP:0001250 |
| Amelogenesis imperfecta / dental enamel/dentin defects | Sign | From tooth eruption | Hallmark of the mildest (Heimler) end of the PEX6 allelic spectrum | HP:0000705 |
| Nail abnormalities | Sign | — | Heimler-syndrome-defining triad member | HP:0001597 (or more specific) |

**Quality-of-life impact:** A dedicated caregiver-report QoL instrument for ZSD exists — *"Proxy-Reported Symptoms and Quality of Life Survey in Zellweger Spectrum Disorders"* (ClinicalTrials.gov NCT03440905) — but disease-specific EQ-5D/SF-36 published results were not surfaced in this search; QoL is dominated by combined sensory (hearing+vision) loss, motor/ataxia disability, and — where present — cognitive impairment and hepatic disease burden.

**Severity/course as a class:** A 2022 scoping review/meta-analysis, *"Characterization of Severity in Zellweger Spectrum Disorder by Clinical Findings"* (MDPI, *Cells*), formally stratifies ZSD severity by clinical-finding clusters and is a good source for quantitative frequency data across the whole ZSD population (PEX-gene-agnostic; PEX6 subgroup extractable).

---

## 4. Genetic/Molecular Information

**Causal gene:** **PEX6** (HGNC:8858; NCBI Gene 5190; OMIM *601498), chromosome 6p21.1, 17 exons, encoding a **AAA-ATPase family peroxin** with two tandem AAA-ATPase cassettes (Ebberink et al. 2010, PMID:19877282).

**Variant landscape.** A systematic screen of 75 PEX6-complementation-group patients identified **77 distinct mutations, 47 of them novel at the time**, spanning missense, nonsense, frameshift, and splice-site classes (Ebberink et al. 2010, PMID:19877282: *"Analysis of 75 patients assigned to the PEX6 complementation group revealed a total of 77 distinct mutations, with 47 being previously unreported and 14 representing polymorphic variants."*). Loss-of-function alleles (nonsense/frameshift/large deletion) generally cluster with the severe (classic Zellweger, PBD4A) end; missense/hypomorphic alleles retaining partial function produce the PBD4B/NALD-IRD, SCAR3/SCABD, or Heimler-syndrome milder phenotypes (genotype–phenotype principle summarized in GeneReviews, NBK1448).

**Notable specific variants:**
- **c.2578C>T (p.Arg860Trp)** — the unique **monoallelic-sufficient** PEX6 variant, pathogenic only when in *cis* with the 3′UTR AEI-driving variant rs144286892 (Falkenberg et al. 2017, *Am J Hum Genet*). This is a rare, mechanistically distinct example of dosage-driven "dominant" disease at a canonically AR peroxin locus.
- **c.1409G>C (p.Gly470Ala)** — founder allele in the Mixteco population of Central California/Oaxaca-origin families, identified in 2 of 3 related neonatal PBD cases with severe (classic-range) presentation (Slaton et al. 2023, PMID:37842507).
- A distinct **French-Canadian founder PEX6 mutation** elevates regional incidence in the Saguenay–Lac-Saint-Jean population of Quebec (PMC3483250).

**Classification (ACMG/ClinVar):** Multiple PEX6 variants are curated in ClinVar with pathogenic/likely-pathogenic classifications across "multiple conditions" (ZSD spectrum + Heimler syndrome), e.g., NM_000287.4(PEX6):c.2626C>T (p.Arg876Trp) reported for multiple conditions in ClinVar.

**Population/allele frequency:** Formal gnomAD-based carrier-frequency figures specific to PEX6 were not retrievable via this search pass (recommend a direct gnomAD v4 query for the curation step); one older ExAC data point noted a PEX6 c.1082G>A allele at ~0.41% in the European population (context/source secondary — verify directly before citing).

**Somatic vs. germline:** Germline only; PEX6-ZSD is not associated with somatic mosaicism reports in this search, though germline mosaicism cannot be excluded generically for an AR condition (no PEX6-specific report surfaced).

**Functional consequence:** Loss- or reduced-function of the PEX1/PEX6 AAA-ATPase heterohexameric motor (see Mechanism, §6) — impaired peroxisomal matrix-protein import, not a gain-of-function or dominant-negative mechanism in the classical biallelic-null cases; the AEI allele is a **dosage/expression-level**, not structural gain-of-function, mechanism.

**Modifier genes:** None specifically documented for PEX6 beyond the *cis*-acting 3′UTR AEI variant itself, which functions as its own allele-specific modifier.

**Epigenetic/chromosomal information:** No PEX6-specific DNA-methylation or chromosomal-rearrangement etiology was identified in this search; disease arises from coding/splice/UTR-regulatory sequence variants, not large chromosomal abnormalities.

Suggested gene/molecular terms: **hgnc:8858** (PEX6); GO Molecular Function **GO:0016887** (ATP hydrolysis activity) and **GO:0043495** (protein-membrane adaptor activity, for the PEX1-PEX6-PEX26 anchoring complex) — verify exact GO ID via OAK before curation use.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors are described for PEX6-related PBD4B in the literature surveyed — it is a fully genetically determined organelle-biogenesis disorder. This section is **not applicable** beyond the population-genetic "environment" of founder effects in isolated/consanguineous communities (Mixteco, French-Canadian Saguenay–Lac-Saint-Jean) documented above, which are demographic/genetic rather than exposure-based risk factors.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular lesion:** Biallelic PEX6 pathogenic variants (or the monoallelic AEI mechanism) reduce/abolish functional PEX6 protein.
2. **Complex disruption:** PEX6 normally heterohexamerizes with **PEX1** to form the peroxisomal **receptor export module (REM)**, anchored to the peroxisomal membrane via **PEX26** (mammalian ortholog of yeast Pex15/plant APEM9) (Nature Communications 2023, s41467-023-41640-9; PMC5762779; PMC9265785 review "Insights into the Structure and Function of the Pex1/Pex6 AAA-ATPase in Peroxisome Homeostasis"). *"Pex1 and Pex6 form a heterohexameric motor essential for peroxisome biogenesis and function, and mutations in these AAA-ATPases cause most peroxisome-biogenesis disorders in humans."*
3. **Failure of PEX5 receptor recycling:** The PTS1-import receptor **PEX5**, after delivering matrix (PTS1-tagged) enzymes into the peroxisomal lumen, is mono-ubiquitinated at a conserved cysteine and must be extracted back to the cytosol by the PEX1/PEX6 AAA-ATPase, which **processively threads and unfolds** ubiquitinated PEX5 through its central pore in an ATP-hydrolysis-dependent manner (PMC5762779, "The peroxisomal AAA-ATPase Pex1/Pex6 unfolds substrates by processive threading"). Loss of PEX6 function stalls this receptor-recycling/export step.
4. **Peroxisomal matrix protein import failure:** With PEX5 recycling blocked, both **PTS1- and PTS2-mediated matrix protein import** are impaired — demonstrated directly in PEX6-knockout cells by immunofluorescence, alongside a **reduction in peroxisome number**; overexpression of wild-type PEX6 restored import, confirming causality and highlighting a genetic-therapy rationale (search synthesis of PEX6 knockout/complementation studies).
5. **Metabolic consequences (biochemical abnormalities):** Failure to import peroxisomal beta-oxidation and ether-lipid-synthesis enzymes produces the ZSD biochemical signature: **elevated very-long-chain fatty acids (VLCFA, C26:0/C26:1)**, **decreased plasmalogens** (C16/C18 erythrocyte membrane), **elevated pipecolic acid**, **elevated C27 bile-acid intermediates (THCA/DHCA)**, and elevated **C26:0-lysophosphatidylcholine (C26:0-LPC)** on dried blood spot (GeneReviews NBK1448; JIMD 2017, PMID:28677031, sensitivity 89.2% for C26:0-LPC).
6. **Downstream tissue injury:**
   - **Hepatotoxicity** from accumulated C27 bile-acid intermediates (THCA/DHCA) — rationale for cholic-acid replacement therapy (§12).
   - **Neural/white-matter injury** from VLCFA/plasmalogen deficiency contributing to demyelination (leukodystrophy) and, in the SCAR3/SCABD presentation, **cerebellar white-matter changes without atrophy** plus **demyelinating peripheral motor neuropathy** (MONDO:0013931 definition).
   - **Sensorineural hearing loss and retinal dystrophy**, thought to reflect the combined effect of impaired ether-phospholipid (plasmalogen) content — essential in myelin and photoreceptor/cochlear membranes — and VLCFA accumulation.
   - **Renal, skeletal (osteopenia), adrenal, and dental (amelogenesis imperfecta)** involvement at the milder end of the spectrum.

**Cell types/tissues implicated:** hepatocytes, cochlear hair cells/spiral ganglion, retinal photoreceptors/RPE, cerebellar Purkinje neurons and oligodendrocytes (white matter), peripheral Schwann cells (demyelinating neuropathy), adrenal cortex, renal tubular epithelium, ameloblasts (dental enamel).

**Zebrafish/mouse mechanistic model data (§15) reinforce this chain:** zebrafish *pex1*/*pex2* loss-of-function recapitulates "increased tissue levels of VLCFA and branched chain fatty acids as well as a reduction in ether phospholipids," with gene-expression changes in "crystallin (lens), troponin, parvalbumin (muscle contraction), and fatty acid metabolic genes," directly linking the biochemical lesion to the cataract/lens and myopathic phenotypic themes seen clinically.

Suggested GO Biological Process terms (verify via OAK before use): **GO:0016558** (protein import into peroxisome matrix), **GO:0007031** (peroxisome organization), **GO:0006635** (fatty acid beta-oxidation), **GO:0008611** (ether lipid biosynthetic process / plasmalogen synthesis). Suggested CL terms: **CL:0000182** (hepatocyte), **CL:0000540** (neuron; refine to Purkinje cell / photoreceptor / cochlear hair cell as appropriate), **CL:0002573** (Schwann cell), **CL:0000064** (ciliated columnar cell — not applicable, remove) — refine per node.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** liver, central nervous system (cerebrum white matter, cerebellum), peripheral nervous system, inner ear (cochlea), eye (retina, lens), adrenal gland, kidney, skeleton, teeth.
**Body systems:** hepatobiliary, nervous (central and peripheral), special sensory (audiovestibular, visual), endocrine (adrenal), renal, skeletal, dental/craniofacial.
**Tissue/cell level:** hepatocytes and biliary epithelium; cerebellar cortex (Purkinje cells) and cerebral/cerebellar white matter (oligodendrocytes/myelin); peripheral motor nerve myelin (Schwann cells); cochlear hair cells and spiral ganglion neurons; retinal photoreceptors and RPE; lens epithelium (cataract); adrenal cortical cells; renal tubular epithelium; ameloblasts/odontoblasts (enamel/dentin).
**Subcellular level:** the **peroxisome** itself (matrix and membrane), with GO Cellular Component anchors **GO:0005777** (peroxisome), **GO:0005778** (peroxisomal membrane); secondary organelle stress in mitochondria (shared fission machinery/metabolic crosstalk) is plausible but not directly documented in this search.
**Localization/laterality:** bilateral/symmetric in essentially all reported manifestations (symmetric leukodystrophy on MRI per PMID:25079577; bilateral sensorineural hearing loss; bilateral retinal dystrophy) — consistent with a systemic, non-lateralized metabolic mechanism.

Suggested UBERON terms (verify before use): **UBERON:0002107** (liver), **UBERON:0002037** (cerebellum), **UBERON:0001851** (cortex), **UBERON:0001846** (cochlea... verify exact ID), **UBERON:0000970** (eye), **UBERON:0000029** (lymph node — not relevant, omit), **UBERON:0002369** (adrenal gland), **UBERON:0002113** (kidney).

---

## 8. Temporal Development

**Onset:** Ranges continuously across the PEX6 allelic series:
- **Neonatal** (severe/classic end, PBD4A): hypotonia, dysmorphism, seizures at birth.
- **Infantile** (NALD/IRD-type, PBD4B core): developmental delay, hepatic and sensory (hearing/vision) involvement emerging in infancy–early childhood.
- **Later childhood/school-age** (SCAR3/SCABD presentation): can present first as an isolated finding on a **school hearing screen** at age 6.5–7 years, with ataxia and leukodystrophy following (PMID:25079577).
- **Very mild/Heimler end:** hearing loss + dental enamel defects recognized in childhood, sometimes with only late or subtle retinal findings.

**Onset pattern:** insidious/progressive in the milder forms; acute-appearing decompensation (diplopia, coordination loss, cognitive decline) can punctuate an otherwise stable course, as in the PMID:25079577 case ("acute-onset diplopia, coordination difficulties, and cognitive decline at age 7" after years of normal development).

**Progression / disease course pattern:** predominantly **progressive** (leukodystrophy, sensorineural loss, hepatic fibrosis, osteopenia) but with a subgroup showing a **non-progressive, stable course** after an initial insult — GeneReviews notes *"children who survive the first year and who have a non-progressive course have a 77% probability of reaching school age."* Course is therefore bimodal: progressive-demyelinating (worse prognosis) vs. stable/non-progressive (better prognosis).

**Duration:** classic/severe end is typically fatal in infancy ("usually die during the first year of life"); milder NALD/IRD/SCAR3/Heimler-range disease is **chronic and lifelong**, with IRD-range patients reported reaching adulthood.

**Remission:** Not applicable — this is a fixed genetic enzymatic/organelle defect without spontaneous remission; "remission" concepts apply only to individual complications (e.g., seizure control) via symptomatic treatment.

**Critical periods:** Neonatal/early-infantile window is critical for diagnosis (newborn-screening C26:0-LPC assays) and initiation of nutritional/hepatic supportive care before irreversible white-matter or hepatic injury accrues; there is no known disease-modifying intervention that alters the peroxisomal defect itself once diagnosed (§12).

---

## 9. Inheritance and Population

**Inheritance pattern:** Autosomal recessive (biallelic PEX6 pathogenic variants), with the well-documented exception of the **p.Arg860Trp allelic-expression-imbalance mechanism**, which produces disease from a single (over-expressed) mutant allele in *cis* with a specific 3′UTR variant (Falkenberg et al. 2017) — described by GeneReviews as *"One PEX6 variant, p.Arg860Trp, has been associated with ZSD in the heterozygous state due to allelic expression imbalance dependent on allelic background."* Asymptomatic parents heterozygous for the same coding variant but lacking the 3′UTR AEI variant do not manifest disease, confirming the *cis*-regulatory (not simple dominant) mechanism.

**Penetrance:** Effectively complete for biallelic null/severe genotypes; variable expressivity governs the resulting phenotype (severe vs. milder ZSD vs. Heimler) rather than penetrance per se.

**Expressivity:** Markedly **variable**, correlating with residual peroxisomal-import function — this is the central genotype–phenotype axis for PEX6, spanning classic Zellweger through NALD/IRD, SCAR3/SCABD, and Heimler syndrome from different combinations of PEX6 alleles.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for PEX6 in this search.

**Founder effects:**
- **French-Canadian (Saguenay–Lac-Saint-Jean, Quebec)** founder PEX6 mutation, associated with regional ZSD incidence approaching **~1/12,000** vs. ~1/50,000 North American baseline (PMC3483250).
- **Mixteco population** (Central California, Oaxaca-origin) founder variant **c.1409G>C (p.Gly470Ala)**, identified in a 2023 cluster of 3 related neonatal cases (Slaton et al., PMID:37842507), with authors recommending targeted community screening/awareness.

**Consanguinity:** Relevant risk-amplifier in founder/isolated populations (implied in both founder reports) though not separately quantified in this search.

**Carrier frequency:** Formal PEX6-specific gnomAD carrier-frequency figures were not directly retrieved in this pass (recommend direct gnomAD v4 lookup for curation); general ZSD (all-PEX-gene) carrier frequency is consistent with the ~1/50,000–1/100,000 birth-incidence estimates below.

**Epidemiology (birth prevalence/incidence, whole-ZSD, PEX-gene-agnostic since PEX6-specific figures are not separately tabulated):**
- **North America/US:** ~1/50,000 births (classic estimate); newborn-screening-based C26:0-LPC data from New York gave **1:133,000** births (GeneReviews) — the discrepancy is attributed to biochemical assays underestimating mild/atypical ZSD.
- **Quebec (Saguenay–Lac-Saint-Jean), Canada:** highest reported regional incidence, ~**1/12,000**, driven by the PEX6 founder allele.
- **Japan:** ~**1/500,000**, reflecting absence of the common European PEX1 founder alleles (p.Ile700Tyrfs*42, p.Gly843Asp); PEX6 relative contribution in Japan not separately reported here.
- Within ZSD, PEX6 accounts for **~10–14.5%** of genetically solved cases (second only to PEX1's ~60%) (GeneReviews NBK1448; Ebberink et al. 2010).

**Sex ratio:** No sex bias reported (autosomal recessive; consistent with equal male:female representation in described cohorts, e.g., the Mixteco case series and the late-onset PEX6 case being male — anecdotal, not indicative of a true sex bias).

**Geographic/ethnic distribution:** Elevated in French-Canadian (Saguenay–Lac-Saint-Jean) and Mixteco (Central California/Oaxaca) founder populations specifically for PEX6; broader ZSD (all genes) shows the North-America-vs.-Japan contrast above driven mainly by PEX1 founder-allele presence/absence.

---

## 10. Diagnostics

**Biochemical screening (first-line):**
- Plasma **VLCFA** (C26:0, C26:1; ratios) — elevated; caution re: false positives in non-fasting samples.
- Erythrocyte membrane **plasmalogens** (C16, C18) — decreased; may be normal in mild disease.
- Plasma/urine **pipecolic acid** — elevated (urine more sensitive in neonates, plasma in older children).
- Plasma/urine **C27 bile-acid intermediates (THCA, DHCA)** — elevated.
- **C26:0-lysophosphatidylcholine (C26:0-LPC)** on dried blood spot — newborn-screening-compatible marker; sensitivity 89.2% (86/91 DBS samples, 33/37 patients) in a dedicated evaluation study (JIMD 2017, PMID:28677031). GeneReviews explicitly cautions: *"Some individuals with ZSD do not have abnormalities of these screening assays,"* mandating molecular confirmation for atypical/mild cases.

**Genetic testing (confirmatory, required for diagnosis per GeneReviews):**
- **Multigene PEX panel** (13 known PEX genes) is the preferred first-tier molecular test for a suggestive phenotype.
- **Exome/genome sequencing** for atypical presentations (e.g., isolated hearing loss/ataxia without classic biochemical signature, as in the Usher-mimic and late-onset leukodystrophy cases).
- **Single-gene PEX6 testing** is *not* generally recommended as a first step (panel/exome preferred), per GeneReviews sequence-detection-rate table (PEX6 ~100% detection rate, 77/77 alleles, once the complementation group is known).

**Other modalities:**
- **Brain MRI:** symmetric leukodystrophy (white-matter change, non-enhancing) in the milder/late-onset presentations; cerebellar white-matter change **without atrophy** in the SCAR3/SCABD presentation.
- **Audiology:** baseline and annual sensorineural hearing loss assessment.
- **Ophthalmology:** annual assessment for retinal dystrophy/pigmentary retinopathy and cataract.
- **Liver panel / imaging:** LFTs, coagulation factors, hepatic ultrasound/fibroscan for fibrosis surveillance.
- **Fibroblast complementation/functional studies:** historically used to assign PEX6 complementation group and confirm impaired PTS1/PTS2 import (as in the original PEX6-defective family report, PMID:11873320).
- **Dental exam:** enamel/dentin abnormality assessment, especially relevant at the Heimler end.

**Differential diagnosis:**
- Other PEX-gene ZSD (PEX1 especially — clinically indistinguishable without molecular testing).
- **X-linked adrenoleukodystrophy (X-ALD, ABCD1)** — elevated VLCFA but normal other peroxisomal markers; explicitly the key differential in the late-onset PEX6 case (PMID:25079577), where ABCD1 sequencing/dosage was normal, prompting the correct PEX6 diagnosis.
- **D-bifunctional protein deficiency, acyl-CoA oxidase deficiency** (single peroxisomal enzyme defects mimicking ZSD biochemically) — GeneReviews notes ~15% of ZSD-like/VLCFA-elevated cases are actually single-enzyme defects.
- **Usher syndrome** — the PEX6 "Usher-syndrome mimic" phenomenon (deafness + retinitis pigmentosa) led to a negative Usher panel before compound-heterozygous PEX6 variants were found in a 12-year-old boy (ScienceDirect/PMC PEX6-Usher-mimic report).
- Other syndromic hearing-loss/retinal-dystrophy conditions; other leukodystrophies and hypotonia syndromes (myotonic dystrophy, SMA, Prader-Willi) at the neonatal-severe end.

**Screening:** Newborn screening for ZSD via C26:0-LPC on dried blood spot is implemented in some US states/programs (e.g., 9 California NBS-positive infants 2016–2022, 7 confirmed ZSD by biallelic PEX-gene variants); carrier/targeted screening is recommended in the Mixteco founder population per Slaton et al. 2023.

Suggested LOINC/marker anchors for curation: VLCFA panel, plasmalogen assay, pipecolic acid, THCA/DHCA, C26:0-LPC — verify specific LOINC codes at curation time.

---

## 11. Outcome/Prognosis

**Severe end (classic Zellweger, PBD4A-range PEX6 genotypes):** poor prognosis; **"usually die during the first year of life, usually having made no developmental progress,"** typically from progressive apnea or respiratory infection (GeneReviews NBK1448).

**Milder end (PBD4B/NALD-IRD, SCAR3/SCABD, Heimler):**
- Survivors past year one with a **non-progressive course** have a **77% probability of reaching school age** (GeneReviews).
- A subset develops **progressive demyelinating leukodystrophy**, causing skill loss and eventually death — the key prognostic bifurcation within the milder group.
- Progressive **sensory deficits** (hearing, vision) are common even in stable/non-progressive courses.
- Some individuals retain **normal intellectual function**.
- **Adults** are rarely diagnosed (historically under-recognized) and typically present with predominantly sensory (hearing/vision) deficits and otherwise normal neurologic development — consistent with the IRD/SCAR3-type adult survivors.

**Complications driving morbidity:** hepatic fibrosis/failure and esophageal varices, adrenal insufficiency, osteopenia/fracture risk, renal oxalate stones, combined sensory (dual hearing-vision) impairment, seizures.

**Prognostic factors:** genotype (null/severe vs. hypomorphic/missense allele combination — the dominant driver, §4/§9), progressive vs. non-progressive leukoencephalopathy course, age at diagnosis/intervention, degree of residual peroxisomal import function.

**Formal severity-stratification resource:** the 2022 MDPI *Cells* scoping review/meta-analysis/chart review on "Characterization of Severity in Zellweger Spectrum Disorder by Clinical Findings" is a good source for quantitative clinical-finding-based severity/prognostic staging across ZSD (verify PMID/exact figures directly for curation-grade quotes).

---

## 12. Treatment

There is **no disease-modifying/curative therapy** for the underlying peroxisomal defect; management is symptomatic/supportive, organized around annual multisystem surveillance (GeneReviews NBK1448):

| Manifestation | Intervention | Suggested MAXO/other term |
|---|---|---|
| Feeding/nutrition | Gastrostomy tube (persistent feeding difficulty); elemental formula for malabsorption | MAXO:0000088 (dietary intervention) |
| Hearing loss | Hearing aids; audiologic follow-up | MAXO:0009030 (hearing aid usage) |
| Vision impairment | Cataract extraction; refractive correction | MAXO:0000004 (surgical procedure, cataract-specific) |
| Liver dysfunction | Vitamin K + fat-soluble vitamin (A/D/E/K) supplementation; **cholic acid therapy** | MAXO:0000088 / pharmacotherapy (NCIT:C15986) + therapeutic_agent CHEBI (cholic acid) |
| Seizures | Standard anti-seizure medications (no PEX6-specific contraindications) | Pharmacotherapy (NCIT:C15986) |
| Adrenal insufficiency | Corticosteroid/glucocorticoid replacement | Pharmacotherapy (NCIT:C15986); therapeutic_agent NCIT:C2322 (Corticosteroid) |
| Osteopenia | Vitamin D supplementation; consider bisphosphonates | Pharmacotherapy (NCIT:C15986) |
| Amelogenesis imperfecta | Dental management (restorative/protective) | Dental-procedure-specific NCIT/MAXO term |
| Renal oxalate stones | Hydration, lithotripsy, surgery as needed | MAXO:0000004 (surgical procedure) |
| Esophageal varices | Endoscopic sclerosing therapy | Endoscopic-procedure NCIT term |
| Respiratory infection prevention | Annual influenza and RSV vaccination | MAXO:0001017 (vaccination) |

**Cholic-acid pharmacotherapy detail:** rationale is suppression of hepatotoxic C27 bile-acid intermediate (THCA/DHCA) synthesis via restored feedback inhibition. A 19-patient open-label pretest–posttest trial (9 months) found cholic acid **"can suppress bile acid synthesis in ZSD patients and, thereby, decrease plasma levels of toxic C27-bile acid intermediates. However, no effect on clinically relevant outcome measures could be observed after 9 months of CA treatment"** (Cholic acid therapy in ZSD, PMC5065608 / PMID:27469511), with an important safety caveat that **cholic acid can worsen liver disease in individuals with pre-existing fibrosis/advanced liver disease** — necessitating careful patient selection. Long-term case reports (Karger *Case Reports in Gastroenterology*, PMC6062720) describe extended cholic-acid treatment courses.

**Experimental/investigational:** No PEX6-specific gene therapy, ASO, or targeted molecular therapy in active late-stage development was identified in this search; a US patent ("Compositions and methods for the treatment of Zellweger spectrum disorder," USPTO 11065247) indicates active IP/early-stage interest but no confirmed clinical-trial-stage disease-modifying agent. The **PEX6-overexpression rescue of matrix-protein import in PEX6-knockout cells** (fibroblast complementation data, §6) provides *in vitro* proof-of-concept for a gene-supplementation therapeutic strategy, but this remains preclinical.

**Ongoing trials:** NCT03440905 (Proxy-Reported Symptoms and Quality of Life Survey in ZSD) is a natural-history/outcomes-measure study rather than an interventional trial — useful for future trial-readiness and outcome-measure development, not itself a treatment.

**Treatment strategy:** Management follows an **annual/biannual multidisciplinary surveillance algorithm** (audiology, ophthalmology, hepatology labs+imaging, adrenal function, urine oxalate, dental exam every 6 months post-secondary-dentition eruption, head MRI as needed for new neurologic decline, growth/nutrition and developmental monitoring at every visit) rather than a linear treatment algorithm, since no curative option exists (GeneReviews NBK1448).

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (monogenic disorder, no modifiable environmental cause); the closest analog is **carrier screening and genetic counseling** in at-risk/founder populations.

**Secondary prevention (early detection):**
- **Newborn screening** via C26:0-LPC dried-blood-spot assay is implemented in some jurisdictions and enables presymptomatic identification and earlier supportive-care initiation.
- **Targeted community screening** recommended for the Mixteco population given the identified c.1409G>C founder allele (Slaton et al. 2023).

**Genetic counseling / reproductive options:**
- Standard AR recurrence-risk counseling: 25% recurrence risk per pregnancy for carrier couples.
- **Carrier screening, preimplantation genetic diagnosis, and prenatal testing** are appropriate once a familial PEX6 genotype is known — standard GTR/ACMG-consistent recommendations for a well-characterized AR gene; no PEX6-specific prenatal-screening program beyond general peroxisomal-disorder prenatal biochemical/molecular testing was identified in this search.
- In founder populations (French-Canadian Saguenay–Lac-Saint-Jean, Mixteco), **population-targeted carrier screening** is the most actionable, evidence-supported prevention lever documented.

**Tertiary prevention:** the entire supportive-care/surveillance regimen in §12 functions as tertiary prevention (preventing/mitigating complications — hepatic decompensation, fracture, renal stone complications, missed sensory-loss-related developmental impact) in individuals already diagnosed.

**Immunization:** Annual influenza and RSV vaccination per standard pediatric schedules is explicitly recommended as part of ZSD management (GeneReviews) to reduce respiratory-infection mortality risk, particularly relevant given respiratory infection is a leading proximate cause of death in severe ZSD.

---

## 14. Other Species / Natural Disease

No naturally occurring PEX6-associated disease in companion animals or wildlife (OMIA-type veterinary entity) was identified in this search — peroxisome biogenesis disorders are not documented as a recognized spontaneous veterinary disease class for PEX6 specifically. PEX6 is broadly conserved across vertebrates (ortholog present in mouse, zebrafish — see §15) and lower eukaryotes (yeast Pex6p performs the analogous AAA-ATPase/Pex15p-anchored receptor-export function, underscoring deep evolutionary conservation of the PEX1/PEX6/PEX26(Pex15) module described in §6). No zoonotic or transmission relevance — this is a non-infectious inherited metabolic/organelle-biogenesis disorder.

---

## 15. Model Organisms

**Mouse:**
- Murine *Pex6* (MGI:2385054) knockout/complementation studies show, consistent with human pathophysiology: fewer peroxisomes, impaired PTS1/PTS2-mediated matrix protein import (immunofluorescence-confirmed), and **rescue of import upon PEX6 overexpression** — supporting a gene-supplementation therapeutic rationale (search-synthesized from PEX6-knockout literature; IMPC/MGI hold the formal allele/phenotype records).
- Related PEX1 mouse models (e.g., the PEX1-p.Gly844Asp knock-in) have been used to study **RPE structural/lipid changes** relevant to the retinal phenotype in milder ZSD (bioRxiv 2024.09.05.611330) — directly informative for the PEX6-associated retinal dystrophy phenotype by extension of the shared PEX1/PEX6 complex biology.
- Classic *Pex1*-null and other *Pex*-null mice are frequently **early embryonic/perinatal lethal**, limiting study of postnatal disease progression — a key model **limitation** relative to human milder ZSD.

**Zebrafish** (increasingly favored for peroxisomal-disorder modeling because postnatal lethality is circumvented):
- ***pex2*** zebrafish mutants: locomotive defects, feeding disability, liver abnormalities, early death — recapitulating classic-ZSD-like severity (Takashima et al. 2021, cited in "Modelling Peroxisomal Disorders in Zebrafish," PMC11764017/MDPI 2073-4409/14/2/147).
- ***pex1*** loss-of-function zebrafish: **viable** (unlike mouse), enabling study of ZSD pathophysiology beyond early development; recapitulates hallmark biochemical features — increased VLCFA and branched-chain fatty acids, reduced ether phospholipids (plasmalogens) — plus organ-specific fatty-acid-species accumulation and broad transcriptomic changes including **reduced crystallin (lens), troponin, and parvalbumin (muscle) gene expression** (bioRxiv 2021.01.03.425169; Frontiers in Molecular Neuroscience 2025, "Pex1 loss-of-function in zebrafish is viable and recapitulates hallmarks of Zellweger spectrum disorders").
- No PEX6-specific zebrafish line was identified by name in this search, but given the shared PEX1/PEX6 heterohexameric complex mechanism, the *pex1* zebrafish model is considered broadly informative for PEX6-mediated disease and is the most translationally active current small-vertebrate ZSD model.

**Cellular models:** Patient-derived **fibroblasts** are the primary human cellular model, used historically to assign PEX6 complementation-group status and to demonstrate the PEX6-overexpression rescue of peroxisomal import described above — directly bridging molecular mechanism (§6) to therapeutic hypothesis-generation.

**Model limitations (general, applicable to PEX6-ZSD):** mouse null models are often too severe/lethal to model the milder NALD/IRD/SCAR3/Heimler end of the human PEX6 allelic spectrum; zebrafish, while viable and biochemically faithful, differ from humans in CNS complexity (limiting direct modeling of the cerebellar ataxia/leukodystrophy phenotype) and audiovestibular/retinal anatomy (limiting precise recapitulation of the sensorineural-hearing-loss and retinal-dystrophy phenotypes that dominate the milder PEX6 clinical picture) — a **human-model-mismatch** consideration worth flagging explicitly if this is curated into a dismech `HUMAN_MODEL_MISMATCH` discussion node, particularly for the SCAR3/SCABD ataxia-deafness-blindness presentation, which has not yet been shown to be faithfully reproduced in any existing PEX6 animal model in the literature surveyed.

---

## Key PMIDs / Citations Compiled

| Citation | Topic |
|---|---|
| PMID:19877282 (Ebberink et al., *Hum Mutat* 2010) | Spectrum of 77 PEX6 mutations in 75 ZSS patients |
| PMID:25079577 (Tran et al., *Pediatr Neurol* 2014) | Late-onset PEX6 ZSD mimicking X-ALD |
| PMID:37842507 (Slaton et al., *Cureus* 2023) | Mixteco founder PEX6 c.1409G>C (p.Gly470Ala) neonatal cluster |
| PMID:26750748 (Braverman et al., *Mol Genet Metab* 2016) | ZSD diagnosis/management guideline overview |
| PMID:27469511 (Klouwer/Berendse et al.) | Cholic acid therapy in ZSD |
| PMID:11873320 | PEX6-defective PBD: severe infant vs. mild Usher-like parents |
| PMID:28677031 | C26:0-LPC/C26:0-carnitine diagnostic markers for ZSD |
| Falkenberg et al. 2017, *AJHG* | PEX6 allelic-expression-imbalance (p.Arg860Trp) mechanism |
| GeneReviews NBK1448 (Steinberg et al., updated) | Comprehensive ZSD clinical/genetic/management reference |
| PMC3483250 | French-Canadian PEX6 founder mutation, Saguenay–Lac-Saint-Jean |
| ScienceDirect S2666-9145(21)00026-9 | PEX6 as an Usher-syndrome clinical mimic |

**Data gaps flagged for curation:** (1) precise gnomAD v4 PEX6 carrier-frequency figures — needs direct database query; (2) quantitative phenotype-frequency percentages specific to the PEX6 subgroup (vs. all-ZSD) — the 2022 *Cells* severity-characterization meta-analysis is the best lead; (3) confirmation of whether any PEX6-specific (as opposed to pan-PEX1/pan-ZSD) animal model exists in current MGI/ZFIN records; (4) exact current OMIM clinical-synopsis field values for #614863 (OMIM.org blocked direct fetch in this session — recommend direct OMIM API/manual lookup before finalizing a KB entry).

Sources:
- [Entry - #614863 - PEROXISOME BIOGENESIS DISORDER 4B; PBD4B - OMIM](https://omim.org/entry/614863?search=PEX1&highlight=pex1)
- [Entry - #614862 - PEROXISOME BIOGENESIS DISORDER 4A (ZELLWEGER); PBD4A - OMIM](https://www.omim.org/entry/614862)
- [Entry - *601498 - PEROXISOME BIOGENESIS FACTOR 6; PEX6 - OMIM](https://omim.org/entry/601498)
- [Zellweger Spectrum Disorder - GeneReviews - NCBI Bookshelf (NBK1448)](https://www.ncbi.nlm.nih.gov/books/NBK1448/)
- [Spectrum of PEX6 mutations in Zellweger syndrome spectrum patients - PubMed (PMID:19877282)](https://pubmed.ncbi.nlm.nih.gov/19877282/)
- [Late-onset Zellweger spectrum disorder caused by PEX6 mutations mimicking X-linked adrenoleukodystrophy - PubMed (PMID:25079577)](https://pubmed.ncbi.nlm.nih.gov/25079577/)
- [Zellweger's Syndrome With PEX6 Gene Mutation in Mixteco Neonates Due to Possible Founder Effect - PMC (PMID:37842507)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10573658/)
- [A founder mutation in the PEX6 gene is responsible for increased incidence of Zellweger syndrome in a French Canadian population - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483250/)
- [Allelic Expression Imbalance Promoting a Mutant PEX6 Allele Causes Zellweger Spectrum Disorder - Cell.com AJHG](https://www.cell.com/ajhg/pdf/S0002-9297(17)30460-3.pdf)
- [PEX6 Mutations in Peroxisomal Biogenesis Disorders: An Usher Syndrome Mimic - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666914521000269)
- [Heimler Syndrome Is Caused by Hypomorphic Mutations in the Peroxisome-Biogenesis Genes PEX1 and PEX6 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4596894/)
- [Spectrum of PEX1 and PEX6 variants in Heimler syndrome - EJHG](https://www.nature.com/articles/ejhg201662)
- [Structure of the peroxisomal Pex1/Pex6 ATPase complex bound to a substrate - Nature Communications](https://www.nature.com/articles/s41467-023-41640-9)
- [The peroxisomal AAA-ATPase Pex1/Pex6 unfolds substrates by processive threading - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762779/)
- [Insights into the Structure and Function of the Pex1/Pex6 AAA-ATPase in Peroxisome Homeostasis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9265785/)
- [Peroxisomal monoubiquitinated PEX5 interacts with the AAA ATPases PEX1 and PEX6 - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0021925820315763)
- [Evaluation of C26:0-lysophosphatidylcholine and C26:0-carnitine as diagnostic markers for Zellweger spectrum disorders - PubMed](https://pubmed.ncbi.nlm.nih.gov/28677031/)
- [Cholic acid therapy in Zellweger spectrum disorders - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5065608/)
- [Long-Term Cholic Acid Therapy in Zellweger Spectrum Disorders - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6062720/)
- [Braverman et al., Peroxisome biogenesis disorders in the Zellweger spectrum overview - Mol Genet Metab (PMID:26750748)](https://pure.psu.edu/en/publications/peroxisome-biogenesis-disorders-in-the-zellweger-spectrum-an-over/)
- [Zellweger spectrum disorders: clinical overview and management approach - PubMed/Orphanet J Rare Dis](https://pubmed.ncbi.nlm.nih.gov/26627182/)
- [Characterization of Severity in Zellweger Spectrum Disorder by Clinical Findings - MDPI Cells](https://www.mdpi.com/2073-4409/11/12/1891)
- [Modelling Peroxisomal Disorders in Zebrafish - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11764017/)
- [Pex1 loss-of-function in zebrafish is viable and recapitulates hallmarks of Zellweger spectrum disorders - Frontiers](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2025.1634536/full)
- [Zebrafish model of human Zellweger syndrome reveals organ specific accumulation of distinct fatty acid species - bioRxiv](https://www.biorxiv.org/content/10.1101/2021.01.03.425169v1.full)
- [Pex6 MGI Mouse Gene Detail - MGI:2385054](https://www.informatics.jax.org/marker/MGI:2385054)
- [peroxisome biogenesis disorder 4B MONDO:0013931 - Monarch Initiative](https://monarchinitiative.org/MONDO:0013931)
- [Peroxisome biogenesis disorder 4B - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3553937/)
- [Orphanet: PEX6-peroxisomal biogenesis factor 6](https://www.orpha.net/en/disease/gene/PEX6)
- [Orphanet: Infantile Refsum disease](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=772&lng=EN)
- [Orphanet: Neonatal adrenoleukodystrophy](https://www.orpha.net/en/disease/detail/44)
- [Proxy-Reported Symptoms and Quality of Life Survey in Zellweger Spectrum Disorders - ClinicalTrials.gov NCT03440905](https://clinicaltrials.gov/study/NCT03440905)