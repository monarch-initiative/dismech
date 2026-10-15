---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T14:03:54.337543'
end_time: '2026-09-04T14:08:43.976791'
duration_seconds: 289.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Nail-patella Syndrome
  mondo_id: ''
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
  - claude-sonnet-5
  web_search_requests: 15
  num_turns: 18
  total_cost_usd: 1.2114224000000002
  session_id: 4583080c-1cc0-583c-84bf-77d0d31559d4
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nail-patella Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nail-patella Syndrome** covering all of the
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

I'll research Nail-patella Syndrome now, using web search to verify identifiers, gather recent literature (2023–2024), and confirm mechanistic and clinical details before writing the full report.

I now have sufficient material to write the comprehensive report. Let me compile the full research report.

# Nail-Patella Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview.** Nail-Patella Syndrome (NPS; also called hereditary osteo-onychodysplasia, HOOD syndrome, or Fong disease) is a rare autosomal dominant, multisystem connective-tissue disorder caused by heterozygous loss-of-function variants in *LMX1B*. It classically presents with a tetrad of nail dysplasia, patellar hypoplasia/absence, elbow dysplasia, and iliac horns, with variable penetrance of renal (focal segmental glomerulosclerosis-type nephropathy) and ocular (open-angle glaucoma) disease, plus an emerging neurological/neuropsychiatric phenotype (reduced pain/temperature sensation, ADHD/depression symptoms, paroxysmal dyskinesia).

**Key identifiers:**
- **OMIM:** #161200 (NAIL-PATELLA SYNDROME; NPS)
- **Gene OMIM:** *LMX1B, 602575
- **Orphanet:** ORPHA:2614
- **MONDO:** MONDO:0008061
- **MedGen:** C0027341
- **HGNC:** LMX1B, HGNC:6683 (gene)
- **ICD-10-CM:** Q87.2 (congenital malformation syndromes predominantly involving limbs) is the closest bucket used clinically; NPS has no dedicated ICD-10 code (commonly cross-coded under Q87.2/Q74.8)
- **MeSH:** D053764 (Nail-Patella Syndrome)

**Synonyms:** Hereditary Osteo-Onychodysplasia (HOOD syndrome); Fong disease; Turner-Kieser syndrome; Onycho-osteodysplasia; Iliac horn syndrome; Osteo-onychodysostosis.

**Evidence base:** Predominantly aggregated disease-level resources (OMIM, Orphanet, GeneReviews) plus case series/cohort studies (largest cohorts ~ tens to 100+ families; e.g., a French series of 55 families, Japanese cohorts, and multiple single-family case reports describing novel *LMX1B* variants). No large national EHR-based cohort exists; most epidemiology is derived from clinic-based case series and rare-disease registries.

---

## 2. Etiology

**Causal factor:** NPS is caused by heterozygous pathogenic variants (missense, nonsense, frameshift, splice-site, partial/whole-gene deletions, and rarely balanced translocations disrupting 9q33.3) in ***LMX1B***, a LIM-homeodomain transcription factor gene. Molecular testing identifies a causal variant in roughly 85% of clinically diagnosed families; conventional sequencing detects ~85% sensitivity, with gene-targeted deletion/duplication analysis adding another ~10% (whole-gene/exonic deletions) (GeneReviews, NCBI Bookshelf NBK1132).

**Genetic risk factors:**
- The predominant mechanism is **haploinsufficiency** rather than dominant-negative effect for most loss-of-function variants — supported directly by whole-gene deletion cases that reproduce the full phenotype (*Eur J Hum Genet*, "Identification of entire LMX1B gene deletions… evidence for haploinsufficiency").
- Missense variants clustering in the LIM-A/LIM-B zinc-binding domains (exons 2–3) or the homeodomain (exons 4–6) account for the majority of pathogenic variants; ~80% of pathogenic variants localize to the LIM domains, and recurrent homeodomain variants account for ~30% of all reported pathogenic variants (GeneReviews NBK1132).
- A dominant-negative mechanism has been demonstrated for at least one mouse homeodomain missense allele (V265D), which causes glaucoma and is semi-lethal via LBD1-mediated dimerization (PMC4014447) — showing that mechanism can vary by variant, not purely haploinsufficiency in all cases.
- Non-coding variants are increasingly recognized: a 2024 report describes 5′UTR variants causing LMX1B haploinsufficiency (*npj Genomic Medicine*, 2024, doi 10.1038/s41525-024-00460-6), and a de novo **enhancer deletion** producing a mild NPS phenotype was reported in *Clinical Genetics* 2024 (Francis et al., doi 10.1111/cge.14447) — both expanding the mutational spectrum beyond the coding sequence.
- ~10–12% of cases are simplex, arising from de novo variants; parental gonadal/somatic mosaicism has been documented and affects recurrence-risk counseling for apparently de novo cases.

**Risk factors — environmental:** None established; NPS is a purely monogenic disorder with no known environmental trigger for disease onset. Pregnancy is a recognized risk-modifying state for renal manifestations (see below), not a cause.

**Protective factors:** None described in the human literature. In the mouse V265D glaucoma model, vitamin B3 (nicotinamide) supplementation protected against IOP elevation by rescuing mitochondrial dysfunction in trabecular meshwork cells (Tolman et al., eLife 2026 / bioRxiv 2024, PMC11741249) — a model-organism finding, not yet validated as a human protective factor.

**Gene-environment interactions:** Not established for baseline disease occurrence. However, **pregnancy** functions as a physiological "second hit" that unmasks or exacerbates renal manifestations: 29% of pregnant women with NPS developed preeclampsia in one series, and de novo nephrotic syndrome during pregnancy has been reported (GeneReviews NBK1132). **NSAID exposure** is a recognized aggravating factor for kidney function in patients with pre-existing nephropathy and should be avoided chronically.

---

## 3. Phenotypes

### Nail abnormalities (Clinical signs) — HP:0001799 (Nail dysplasia) / more specific children terms
- **Frequency:** 96–98% of affected individuals (GeneReviews NBK1132)
- **Onset:** Congenital/present from birth (may be subtle initially)
- **Characteristics:** Absence, hypoplasia, dystrophy, longitudinal/horizontal ridging, pitting, discoloration, longitudinal splitting, thinning. Radial gradient of severity — thumb most severely affected, decreasing severity ulnarward; toenails less affected than fingernails.
- **HPO suggestions:** HP:0008365 (Ridged nail), HP:0001807 (Nail dysplasia — check exact term), HP:0001800 (Absent nail), HP:0100774 (Abnormal nail color), HP:0004230 (Abnormality of the toenails)
- **QoL impact:** Cosmetic/psychosocial burden; occasionally functional impairment of fine grip.

### Patellar dysplasia/instability (Clinical sign/physical manifestation)
- **Frequency:** Patellar hypoplasia/absence is a core feature; recurrent subluxation/dislocation in 74–90% of patients
- **Onset:** Congenital structural anomaly; instability symptoms often manifest in childhood/adolescence with ambulation
- **HPO:** HP:0003065 (Absent patella), HP:0003045 (Hypoplastic patella — check exact ID; HP:0006471 patellar aplasia), HP:0001954 (Patellar dislocation)
- **Progression:** Structurally stable but functionally progressive (recurrent dislocation, early osteoarthritis)

### Elbow dysplasia
- **Frequency:** Common, often asymmetric; radial head dislocation (usually posterior), cubitus valgus, antecubital pterygia, limited pronation/supination/extension
- **HPO:** HP:0003042 (Elbow dysplasia), HP:0003083 (Radial head dislocation), HP:0002987 (Elbow flexion contracture)

### Iliac horns
- **Frequency:** 70–76% (GeneReviews); considered **pathognomonic** — "rarely, if ever, seen in people without this condition"
- **Nature:** Asymptomatic bilateral bony projections from the posterior ilium, detected radiographically
- **HPO:** HP:0002863 (Iliac horn)

### Renal phenotype (laboratory abnormality → clinical sign)
- **Frequency:** 30–50% develop proteinuria ± hematuria; up to 5–15% (GeneReviews cites up to 15%; StatPearls cites up to 15%) progress to end-stage kidney disease (ESKD)
- **Onset:** Any age from birth onward; often detected in childhood/young adulthood
- **Progression:** Variable — may be intermittent, remit spontaneously, remain asymptomatic, or progress to nephrotic-range proteinuria and ESKD
- **Pathology:** FSGS-like histology; characteristic EM finding of irregular, "moth-eaten"/mottled thickening of the GBM with electron-lucent areas and collagen fibril deposition ("collagenofibrotic" change); myelin/zebra bodies reported as a diagnostic clue in some cases
- **HPO:** HP:0000093 (Proteinuria), HP:0000790 (Hematuria), HP:0000822 (Hypertension), HP:0003774 (Stage 5 chronic kidney disease)

### Ocular phenotype
- **Frequency:** Primary open-angle glaucoma/ocular hypertension at increased frequency (~30–40% cited by some series) and younger age than general population
- **Distinctive sign:** "Lester sign" — clover-leaf/cloverleaf-shaped darker pigmentation zone in the iris (a relatively specific clinical clue)
- **HPO:** HP:0000501 (Glaucoma), HP:0000488 (Chorioretinal abnormality — not applicable; use HP:0007906 Open angle glaucoma if available), HP:0007904 (Increased corneal curvature — not relevant), Lester sign has no dedicated HPO term currently

### Neurological/sensory phenotype
- **Frequency:** ~25% show reduced pain/temperature sensation (glove-and-stocking distribution) attributed to failure of Aδ/C-fiber interneuron connections in the dorsal spinal cord; ~6% epilepsy in one large cohort; paroxysmal (cranial) dyskinesia reported in case reports (Bech et al., *Movement Disorders* 2020)
- **HPO:** HP:0002829 (Arthralgia — not applicable), HP:0007398 (Reduced pain sensation — check ID), HP:0012332 (Decreased sensory nerve conduction velocity — not exact), HP:0001250 (Seizure)

### Neuropsychiatric phenotype
- Increased self-reported ADHD and major depressive disorder symptoms reported in a case-control survey study (Sweeney et al., *Am J Med Genet B* 2011, PMID: 21184584), hypothesized to relate to LMX1B's role in dopaminergic/serotonergic neuron development; this remains an association from a modest survey study, not an established core diagnostic feature.
- HPO: HP:0007018 (Attention deficit hyperactivity disorder), HP:0000716 (Depressivity)

### Other systemic features
- GI: constipation/IBS symptoms in ~30%
- Dental: thin enamel, crumbling teeth
- Musculoskeletal: reduced bone mineral density (8–20% reduction at hip reported), lean body habitus with difficulty gaining muscle mass, scoliosis, pes planus, pectus excavatum, back pain (~50%)
- Vasomotor: Raynaud phenomenon; rare reports of internal carotid artery aplasia, spontaneous coronary artery dissection
- High forehead / frontal hairline pattern resembling male-pattern recession

---

## 4. Genetic/Molecular Information

**Causal gene:** *LMX1B* (LIM homeobox transcription factor 1 beta), chromosome 9q33.3. HGNC:6683; NCBI Gene ID 4010; OMIM *602575.

**Protein domains and variant clustering:**
- N-terminal tandem LIM-A and LIM-B zinc-finger domains (protein-protein interaction, encoded by exons 2–3)
- Central homeodomain (DNA-binding, encoded by exons 4–6)
- C-terminal glutamine-rich domain of unknown function
- >170 distinct pathogenic *LMX1B* variants have been documented (GeneReviews). Missense, nonsense, frameshift, splice-site variants, small indels, and whole/partial gene deletions are all reported; a chromosomal translocation disrupting 9q33.3 has also been described (detected via karyotype when targeted testing is negative).

**Variant classification (ACMG/AMP, ClinVar):** Most reported LMX1B variants relevant to NPS are classified Pathogenic/Likely Pathogenic; population-database presence at appreciable frequency argues against pathogenicity (haploinsufficient gene — LOF variants are rare in gnomAD, consistent with a dosage-sensitive developmental gene). Representative ClinVar entries include NM_001174147.2 variants such as c.793G>C (p.Val265Leu), c.745C>T (p.Arg249Ter), c.691C>T (p.Arg231Ter), c.661C>T (p.Arg221Ter), c.244C>T (p.Gln82Ter), and the splice variant c.741+1G>A.

**Functional consequences:** Predominantly **haploinsufficiency** (loss of one functional allele reduces LMX1B dosage below a developmental threshold in dorsal limb, podocyte, ocular anterior-segment, and monoaminergic-neuron lineages). A subset of homeodomain missense variants (e.g., mouse V265D) act as **dominant-negative** through LBD1-mediated dimerization interference (PMC4014447), producing a more severe eye phenotype experimentally.

**Genotype-phenotype correlation (nephropathy risk):** Pathogenic variants located in the **homeodomain** are associated with significantly more frequent and more severe proteinuria than variants in the **LIM domains** (Dreyer et al., *Eur J Hum Genet* 2005/2004, PMID:15928687; confirmed in a Japanese cohort). No clear genotype-phenotype correlation has been established for extrarenal (nail, skeletal, ocular) manifestations. Genotype alone cannot currently predict progression to ESKD; proteinuria severity itself is the best clinical predictor.

**LMX1B target genes (mechanistic basis for genotype-phenotype effects):**
- ***COL4A3/COL4A4*** — LMX1B binds an intronic enhancer in *COL4A4* and coordinately regulates *COL4A3*/*COL4A4* transcription in podocytes; loss reduces α3(IV)/α4(IV) collagen deposition in the GBM (Morello et al., *Nat Genet* 2001, PMID:11175791).
- ***NPHS2*** (podocin) and ***CD2AP*** — LMX1B binds regulatory regions and is required for slit-diaphragm gene induction during podocyte differentiation (Rohr et al., *J Clin Invest*, PMID via JCI13954).
- LMX1B is also required for **maintenance** of differentiated podocytes in the adult kidney, not just developmental patterning (PMC3810075) — relevant to adult-onset/progressive nephropathy.

**Isolated LMX1B-associated nephropathy (allelic disorder):** Specific missense variants — most notably recurrent **p.Arg246Gln (R246Q)** and p.Arg246Pro (R246P) in the homeodomain — cause hereditary FSGS/nephropathy **without** the classic nail/skeletal/ocular features ("nail-patella-like renal disease," NPLRD; Boyer et al., *J Am Soc Nephrol* 2013, PMC3736714; multiple confirmatory case series including Japanese and Korean cohorts). This is a clinically important allelic variant to distinguish from typical NPS in the differential of hereditary FSGS.

**Population frequency:** No specific founder allele or ethnic enrichment is established; *LMX1B* loss-of-function variants are constrained (low observed/expected ratio) in gnomAD, consistent with dosage sensitivity, but specific pLI/allele-frequency figures were not independently verified in this pass and should be checked directly against gnomAD before KB citation.

**Epigenetic information:** No disease-specific DNA methylation or histone-modification studies were identified for NPS; this is an unstudied area for this gene/disease.

**Chromosomal abnormalities:** Rare balanced translocations at 9q33.3 disrupting *LMX1B* have been reported as a cause of NPS in families where sequence-level testing is negative (detected by karyotype) — including a "novel cause of Nail-Patella Syndrome" described as an *LMX1B* inversion in a Swedish family (PMC9235307).

---

## 5. Environmental Information

NPS is a purely monogenic disorder; there is no established toxin, occupational, infectious, or lifestyle causal factor. The main "environmental" modulator identified in the literature is:
- **Pregnancy** as a physiological state that increases risk of preeclampsia (29% in one NPS cohort) and can unmask/exacerbate nephrotic syndrome.
- **Chronic NSAID use**, flagged in management guidance as detrimental to kidney function in patients with NPS-associated nephropathy and to be avoided.
- No infectious agent is implicated in etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (organ-specific branches from one shared lesion)

1. A heterozygous loss-of-function (or, less commonly, dominant-negative) variant in *LMX1B* **leads to** reduced or altered LMX1B transcription-factor dosage in every LMX1B-expressing lineage during embryogenesis (haploinsufficiency in most cases; inferred from whole-gene-deletion phenocopies).
2. In the developing limb, reduced LMX1B dosage in the dorsal limb mesenchyme **results in** failure of the normal dorsal-ventral (D-V) patterning gradient (LMX1B is the master dorsalizing signal downstream of Wnt7a in the apical ectodermal ridge/dorsal ectoderm) — **leading to** a partial "double-ventral" limb phenotype: absent/hypoplastic nails, patella, and dorsal-specific structures (this D-V patterning role is directly demonstrated in *Lmx1b*-null mice, which show symmetrical ventral-ventral autopod/zeugopod structure).
3. In the developing kidney, reduced LMX1B dosage in podocyte precursors **impairs** transcriptional induction of slit-diaphragm and GBM genes (*NPHS2*/podocin, *CD2AP*, *COL4A3*, *COL4A4*) **leading to** arrested podocyte differentiation at the cuboidal stage, failure of foot-process/slit-diaphragm elaboration, and defective, split, "moth-eaten" GBM — **resulting in** proteinuria, and in a subset, progressive FSGS-type glomerulosclerosis and ESKD. LMX1B is also required for **maintenance** of the mature podocyte cytoskeleton in adulthood, so ongoing haploinsufficiency **can continue driving** slow nephron loss even after normal development (inferred from conditional-knockout data — this step is more strongly demonstrated in mouse than directly shown in human tissue).
4. Where the pathogenic variant lies in the **homeodomain** rather than the LIM domains, DNA-binding/target-gene transactivation is more severely disrupted, statistically **increasing** the frequency and severity of proteinuria — a genotype-specific branch of step 3 (human genotype-phenotype cohort evidence, not fully mechanistically resolved at the biochemical level).
5. In the anterior segment of the eye, LMX1B is required for normal development and homeostasis of the trabecular meshwork and Schlemm canal; reduced dosage **drives** mitochondrial dysfunction specifically in a trabecular-meshwork cell subtype (TM3), evidenced by swollen mitochondria with reduced cristae area in a mouse homeodomain-variant (V265D) model, **leading to** oxidative stress and outflow-pathway dysfunction, **resulting in** elevated intraocular pressure and early-onset open-angle glaucoma. This chain is demonstrated at the mouse single-cell/mitochondrial level (Tolman et al., eLife 2026/bioRxiv 2024) and inferred, not yet directly shown, in human trabecular meshwork tissue.
6. In the CNS, LMX1B is required for specification/maintenance of midbrain dopaminergic neurons and hindbrain serotonergic neurons, and for migration/connectivity of dorsal spinal cord interneurons that relay nociceptive (Aδ/C-fiber) input; reduced dosage **leads to** disrupted serotonergic axon arborization and dopaminergic circuit development (mouse data) and failure of nociceptive afferents to connect properly in the dorsal horn, **manifesting clinically as** reduced pain/temperature sensation (glove-and-stocking distribution) and, per one survey study, increased ADHD/depressive symptomatology — this branch is the most inferential, resting mainly on mouse neurodevelopmental biology with human correlation from a single case-control symptom-survey study.

### Molecular pathways
LMX1B acts principally as a **direct transcriptional activator** (not classically framed as part of Wnt/MAPK/mTOR/PI3K-AKT signaling per se, though it operates downstream of dorsal-limb Wnt7a/En1 patterning signals in limb development). Its downstream transcriptional targets of curatorial interest: *COL4A3*, *COL4A4*, *NPHS2*, *CD2AP* (kidney); genes governing dorsal limb identity (kidney/limb pathway crosstalk with Wnt7a-En1-Lmx1b axis, established primarily in mouse).

### Cellular processes
- Arrested/incomplete **podocyte differentiation** (failure of foot-process formation, slit-diaphragm assembly)
- **Mitochondrial dysfunction and oxidative stress** in trabecular meshwork cells (glaucoma mechanism)
- Failure of **dorsal-ventral limb mesenchymal patterning**
- Abnormal **neuronal migration/connectivity** in dorsal spinal cord and failure of serotonergic axon arborization

### Protein dysfunction
Loss-of-function (haploinsufficiency) is the dominant mechanism; a subset of homeodomain missense alleles act via **dominant-negative interference with LBD1-mediated dimerization** (demonstrated in mouse V265D model), altering the biochemistry from simple dosage loss to disrupted protein-protein interaction.

### Tissue damage mechanisms
GBM structural disruption ("moth-eaten"/collagenofibrotic thickening) in kidney; mitochondrial oxidative stress in trabecular meshwork; no classical fibrotic/ischemic/necrotic tissue-damage mechanism has been characterized as primary — the dominant damage mode is a **developmental patterning defect** rather than acquired tissue injury, with the kidney and eye showing secondary progressive structural failure superimposed on a developmentally abnormal substrate.

### Suggested ontology terms
- **GO (biological process):** GO:0009953 (dorsal/ventral pattern formation), GO:0072015 (glomerular visceral epithelial cell development), GO:0072311 (glomerular epithelial cell differentiation), GO:0007586 (digestion — not relevant), GO:0007507 (heart development — not relevant); GO:0021756 (striatum development — not directly relevant), GO:0021542 (dentate gyrus development — not relevant); more precisely: GO:0072015 (podocyte development), GO:0003094 (glomerular filtration), GO:0006916 (anti-apoptosis — not primary)
- **CL (cell types):** CL:0000653 (podocyte), CL:0000091 (Kupffer cell — not relevant), CL:1000452 (trabecular meshwork cell — verify exact CURIE), CL:0000700 (dopaminergic neuron), CL:0000850 (serotonergic neuron — verify exact CURIE, likely CL:0000850 or similar)
- **UBERON:** UBERON:0000074 (renal glomerulus), UBERON:0001707 (trabecular meshwork — verify), UBERON:0002102 (patella), UBERON:0001705 (nail)

*(Note: all suggested ontology CURIEs should be verified against `conf/oak_config.yaml`-configured adapters before binding in a KB entry, per the dismech-terms skill.)*

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Integument (nails), skeletal system (patella, elbow, pelvis/ilium), kidney (glomerulus), eye (anterior segment — trabecular meshwork/Schlemm canal)
- **Secondary/complication-level:** Peripheral/central nervous system (dorsal spinal cord sensory relay, midbrain dopaminergic and hindbrain serotonergic nuclei), GI tract (functional — constipation), dental (enamel), bone (systemic BMD reduction), cardiovascular (rare — coronary artery dissection, carotid aplasia)
- **Body systems:** Musculoskeletal, renal/urinary, ophthalmologic, integumentary, nervous, and to a lesser extent gastrointestinal and cardiovascular systems

**Tissue/cell level:**
- Podocytes (glomerular visceral epithelial cells) — CL:0000653
- Trabecular meshwork cells (specifically a TM3 subpopulation per single-cell mouse data)
- Dorsal limb mesenchyme / connective tissue (nail bed, patellar/periarticular connective tissue)
- Dorsal spinal cord interneurons; midbrain dopaminergic neurons; hindbrain serotonergic neurons

**Subcellular level:**
- **Mitochondria** — swollen, reduced-cristae mitochondria in trabecular meshwork cells (glaucoma mechanism) and in zebrafish *lmx1bb*-mutant kidney tubule cells (GO:0005739 mitochondrion; GO Cellular Component)
- Glomerular basement membrane (extracellular matrix, not strictly subcellular) — irregular thickening with electron-lucent zones
- Nucleus (LMX1B is a nuclear transcription factor; GO:0005634)

**Localization/laterality:** Iliac horns and elbow dysplasia are typically **bilateral but often asymmetric** in severity; nail involvement follows a **radial-to-ulnar severity gradient** (thumb most severe); renal and ocular involvement are typically bilateral (both kidneys, both eyes) though asymmetric glaucoma severity between eyes is reported.

---

## 8. Temporal Development

**Onset:**
- Structural features (nail dysplasia, patellar/elbow dysplasia, iliac horns) are **congenital**, present from birth, though iliac horns are radiographically silent/asymptomatic and often noted only on incidental imaging.
- Renal proteinuria can present at **any age from birth through adulthood**.
- Glaucoma tends to develop at a **younger age than typical primary open-angle glaucoma** in the general population but is not congenital in most cases (congenital glaucoma is reported as a rarer subtype within NPS).
- Neurological/sensory symptoms and neuropsychiatric symptoms are typically recognized in **childhood to adulthood**, without a sharply defined onset window.

**Progression:**
- **Skeletal:** Structurally static developmental anomaly, but functional consequences (patellar instability, early osteoarthritis, back pain, scoliosis) are progressive over the lifespan.
- **Renal:** Highly variable course — can be intermittent, spontaneously remitting, stable low-grade proteinuria, or progressive to nephrotic syndrome and ESKD (5–15% lifetime risk of ESKD). No validated staging system specific to NPS nephropathy exists; standard CKD staging applies once nephropathy is diagnosed.
- **Ocular:** Progressive, as with typical open-angle glaucoma, but earlier onset warrants lifelong surveillance beginning in childhood as soon as the child can cooperate with testing.
- **Disease course pattern:** Chronic, lifelong, non-remitting for the structural (skeletal) and gene-dosage-driven organ phenotypes; the renal component can show a **relapsing-remitting-like pattern** in some individuals.

**Critical periods / windows of vulnerability:**
- Embryonic dorsal-limb and nephrogenic patterning windows are the developmental "point of no return" for structural limb and early podocyte anomalies (cannot be prevented postnatally).
- Pregnancy is a recognized period of heightened renal risk (preeclampsia, new-onset/worsened proteinuria) warranting intensified monitoring.
- Childhood ophthalmologic screening onset (as soon as the child can cooperate with exams) is emphasized as a window for early glaucoma detection before irreversible optic nerve damage.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Estimated at **1 in 50,000 live births**, though regional registries suggest wide variation (e.g., ~22 per million in England vs. ~4.5 per million in the United States per Orphanet-style regional estimates), and true prevalence is likely underestimated due to mild/undiagnosed phenotypes.
- No sex predilection — autosomal dominant, males and females equally affected.

**Inheritance pattern:** Autosomal dominant with **full penetrance** for the gene defect itself, but with **extremely variable expressivity** — severity and organ-system involvement vary widely even within the same family and between the two alleles' carriers.

**Familial vs. de novo:** ~88% of probands have an affected parent; ~10–12% are simplex/de novo cases. Parental **germline/somatic mosaicism** has been documented, which affects recurrence-risk counseling even when parental testing is negative.

**Penetrance:** Full penetrance is generally described for the overall syndrome (i.e., virtually all mutation carriers show at least the nail/patellar phenotype), but individual organ-system manifestations (renal, ocular, neurological) show incomplete, variable penetrance.

**Expressivity:** Highly variable — well documented within single families (some relatives have only mild nail changes; others develop ESKD or glaucoma).

**Genetic anticipation:** Not a recognized feature of NPS (not a repeat-expansion disorder).

**Germline mosaicism:** Documented in multiple case reports of "de novo" probands with subsequently affected siblings, informing genetic counseling (empiric recurrence risk for sibs of a de novo case exceeds general population risk even with negative parental testing).

**Founder effects:** No major population-specific founder allele has been robustly established in the literature reviewed; variants are largely private/family-specific (>170 distinct pathogenic variants reported, consistent with high allelic heterogeneity rather than founder mutations).

**Consanguinity:** Not a relevant risk factor, given autosomal dominant inheritance (a single copy is sufficient).

**Carrier frequency:** Not applicable in the traditional AR sense; gnomAD-based population frequency of LMX1B loss-of-function alleles should be checked directly (not independently verified in this pass) but is expected to be very low given the gene's mutational constraint and dominant dosage sensitivity.

**Population demographics:** No specific ethnic/geographic enrichment reported; cases described across European, East Asian (Japanese, Chinese, Korean), and other populations without documented differential prevalence attributable to ancestry.

---

## 10. Diagnostics

**Clinical diagnosis:** Suspected based on the classic tetrad plus compatible family history; **iliac horns are considered pathognomonic** when present.

**Molecular confirmation (tiered testing approach per GeneReviews):**
1. **Single-gene sequencing of LMX1B** (first-line) — detects missense/nonsense/splice variants and small indels; ~85% diagnostic sensitivity for suggestive presentations.
2. **Gene-targeted deletion/duplication analysis** — detects exon-level and whole-gene deletions/duplications; adds ~10% additional diagnostic yield.
3. **Multigene renal or glaucoma panels** — useful when kidney disease or glaucoma is the presenting/predominant feature without a clear skeletal phenotype (important for capturing the "nail-patella-like renal disease" allelic phenotype).
4. **Exome/genome sequencing** — for atypical presentations not initially suspected to be NPS.
5. **Karyotype** — reserved for cases with strong clinical/radiographic suspicion and dominant inheritance pattern but negative gene-targeted testing, to detect rare balanced translocations disrupting 9q33.3.

Variants of uncertain significance (VUS) neither establish nor exclude the diagnosis.

**Laboratory tests:** Urinalysis, first-morning urine albumin-to-creatinine ratio (preferred for sensitivity), serum creatinine/eGFR for renal surveillance.

**Imaging:**
- Plain radiographs of pelvis (iliac horns), knees (patellar hypoplasia), elbows (radial head dislocation, dysplasia)
- MRI recommended prior to any orthopedic surgical intervention to characterize anatomic abnormalities
- Renal ultrasound as clinically indicated

**Biopsy/histopathology:** Renal biopsy shows FSGS-pattern light microscopy with the pathognomonic EM finding of irregular "moth-eaten"/mottled GBM thickening with electron-lucent zones and interstitial collagen fibrils (collagenofibrotic change); myelin/zebra bodies reported in some cases as an additional diagnostic clue that can cause misdiagnosis if not recognized as NPS-associated.

**Ophthalmologic testing:** Intraocular pressure measurement, gonioscopy, optic nerve/visual field assessment for glaucoma screening — recommended to begin as early as the child can cooperate.

**Differential diagnosis** (from GeneReviews):
- **Coffin-Siris syndrome** — 5th-finger nail hypoplasia, patellar/elbow dislocation, but with dysmorphic facies, developmental delay
- **Meier-Gorlin syndrome** — absent patellae, radial head dislocation, but with microtia, severe short stature
- **Genitopatellar syndrome (*KAT6B*)** — absent/hypoplastic patellae, kidney anomalies, but with genital anomalies, microcephaly
- **RAPADILINO syndrome (*RECQL4*)** — absent patellae, radial defects, but with cleft palate, short stature
- **DOORS syndrome (*TBC1D24*)** — absent/poorly formed nails, but with hearing loss, developmental delay, optic atrophy
- ***TBX4*-related ischiopatellar dysplasia** — small/absent patellae and pelvic anomalies but without nail/elbow changes or kidney involvement; associated instead with pulmonary arterial hypertension

**Screening:** No population newborn-screening program exists (not detectable by biochemical newborn screening panels); at-risk relative evaluation uses targeted molecular testing when the familial variant is known, or clinical/renal/ophthalmologic surveillance when it is not.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No significant reduction in overall life expectancy is described for NPS as a whole; mortality risk is essentially confined to the minority who progress to **ESKD** (managed with dialysis/transplantation, generally with favorable transplant outcomes since NPS-associated nephropathy does not recur in the transplanted kidney, as it is a developmental/genetic podocyte disorder rather than a circulating factor-mediated disease — this is implied by general FSGS-genetics literature though not independently confirmed with an NPS-specific PMID in this pass and should be verified before citing).

**Morbidity:**
- **Renal:** 5–15% lifetime ESKD risk; the dominant driver of serious morbidity/mortality risk in NPS.
- **Ocular:** Risk of irreversible vision loss from undetected/undertreated early-onset glaucoma if surveillance is not maintained.
- **Musculoskeletal:** Chronic pain, recurrent patellar dislocation, early osteoarthritis, reduced bone mineral density with associated fracture risk, functional limitation from elbow contractures.
- **Neurological:** Risk of thermal/mechanical injury due to reduced pain/temperature sensation (burns, unrecognized trauma) — an important patient-education point.

**Complications:** Preeclampsia in pregnancy (29% in one cohort); nephrotic syndrome; ESKD; glaucoma-related vision loss; dental complications from thin enamel; rare vascular anomalies.

**Prognostic factors:** Presence and severity of proteinuria is the best available clinical predictor of renal progression; mutation location (homeodomain vs. LIM domain) correlates with proteinuria risk/severity but cannot yet be used to individually predict ESKD trajectory.

**Recovery potential:** With ACE-inhibitor therapy for proteinuria/hypertension and standard glaucoma management, morbidity from the two most serious organ-system complications (renal, ocular) can be substantially mitigated; skeletal manifestations are managed symptomatically/surgically rather than "recovered from," as they are structural.

---

## 12. Treatment

Management is **multidisciplinary and predominantly supportive/symptomatic** — there is no disease-modifying or gene-targeted therapy for NPS at present.

**Pharmacotherapy:**
- **ACE inhibitors** (and/or angiotensin receptor blockers) for proteinuria and/or hypertension — first-line renoprotective therapy (NCIT:C15986 Pharmacotherapy; specific agent class would map to an ACE-inhibitor/ARB CHEBI or NCIT drug-class term). Combination RAAS blockade has been reported in refractory pediatric/severe proteinuria cases but requires nephrology supervision due to hyperkalemia risk.
- Steroid therapy is generally reported as **ineffective** for NPS-associated nephropathy (distinguishing it from immune-mediated glomerular disease).
- **Agents to avoid:** Chronic NSAID use, due to detrimental effects on kidney function.
- Standard **glaucoma pharmacotherapy** (topical IOP-lowering agents) per ophthalmology, with **laser or surgical intervention** as needed for refractory IOP elevation.
- **Anti-seizure medications** for the subset with epilepsy.

**Surgical/interventional:**
- Orthopedic surgery for patellar instability, elbow contracture, or scoliosis, guided by pre-operative MRI to characterize anatomy (NCIT:C15329 Surgical Procedure; NCIT:C16186 Orthopedic Surgical Procedure)
- Glaucoma surgery/laser trabeculoplasty for refractory cases (NCIT:C15313-adjacent procedural codes as appropriate)
- **Kidney transplantation** for ESKD, generally with favorable outcomes (NCIT:C15289 Organ Transplantation)

**Supportive/rehabilitative:**
- Physical therapy, bracing/splinting for joint instability (NCIT:C15302 Physical Therapy)
- Patient education regarding reduced pain/temperature sensation to prevent inadvertent burns/injury
- Dental surveillance and care (every 6 months) given enamel fragility
- Bone-health management (standard osteoporosis/low-BMD treatment as indicated) with DEXA monitoring

**Experimental:** No NPS-specific gene therapy, RNA-based therapy, or targeted molecular therapy is in clinical development as of current literature. The mouse-model finding that **vitamin B3 (nicotinamide)** protects against glaucoma-associated mitochondrial dysfunction and IOP elevation (Tolman et al., eLife 2026/bioRxiv 2024) is a preclinical lead of translational interest but has not been tested in NPS patients.

**Pregnancy-specific management:** Frequent urinalysis and blood pressure monitoring; ACE inhibitors/ARBs should be discontinued and switched to pregnancy-safe alternatives prior to or immediately upon recognition of pregnancy, given teratogenicity.

**Surveillance schedule (at least annually per GeneReviews):**
- Orthopedic mobility/gait assessment, scoliosis screening
- Blood pressure, urinalysis, first-morning urine albumin-to-creatinine ratio
- GI and neurologic assessment
- Glaucoma screening starting as soon as the child can cooperate
- Dental exam every 6 months
- DEXA as clinically indicated

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (monogenic dominant disorder); the only "primary prevention" avenue is reproductive — genetic counseling, carrier/at-risk relative testing, and reproductive options (prenatal diagnosis, preimplantation genetic testing) for families with a known pathogenic variant.

**Secondary prevention:** Early ophthalmologic screening for glaucoma (to catch elevated IOP before irreversible optic nerve damage) and renal surveillance (urinalysis/ACR) to catch proteinuria early enough for ACE-inhibitor initiation, which may slow progression to ESKD.

**Tertiary prevention:** ACE inhibitor/ARB therapy to limit progression once proteinuria is established; avoidance of nephrotoxic agents (chronic NSAIDs); prompt transition of antihypertensive regimen around pregnancy to avoid ACE-inhibitor fetotoxicity while still managing preeclampsia risk; patient education on sensory deficits to prevent burns/injuries; DEXA-guided bone-health management to reduce fracture risk.

**Genetic counseling:** Central to prevention/family planning — 50% recurrence risk for offspring of an affected parent; empiric residual risk for sibs of an apparently de novo proband due to possible parental gonadal mosaicism; at-risk relative testing recommended even when the parent appears unaffected, given variable expressivity (an apparently "unaffected" relative could still be a mutation carrier with minimal manifestations).

**Screening programs:** No population-level newborn screening exists; screening is targeted (cascade testing in known families) rather than population-based.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No well-documented naturally occurring NPS-equivalent disease has been established in companion animals or wildlife in the literature surveyed here. Searches for a canine or other veterinary natural counterpart (e.g., via OMIA) did not return a confirmed naturally occurring *LMX1B*-associated syndrome in dogs or other domestic species in this research pass — this should be treated as an open gap rather than a confirmed absence, and a direct OMIA query would be needed before asserting "no natural disease exists in other species."

**Orthologous gene:** *Lmx1b* is highly conserved; mouse *Lmx1b* (NCBI Gene, MGI) and zebrafish paralogues *lmx1ba*/*lmx1bb* (from a genome duplication event) are the principal orthologs used experimentally (NCBITaxon:10090 Mus musculus; NCBITaxon:7955 Danio rerio).

**Comparative biology:** The mouse and zebrafish orthologs recapitulate distinct sub-phenotypes of the human disease (see Model Organisms below), supporting deep evolutionary conservation of LMX1B's roles in dorsal limb/fin patterning, podocyte/nephron development, and monoaminergic neuron specification — though zebrafish gene duplication has led to **subfunctionalization** between the two paralogues (lmx1ba → skeletal/neuronal; lmx1bb → renal), a divergence not present in mammals where a single *LMX1B* gene serves all these roles.

**Transmission:** Not applicable — NPS is not an infectious or zoonotic condition.

---

## 15. Model Organisms

**Mouse (*Mus musculus*):**
- ***Lmx1b*-null mice** (conventional knockout): Recapitulate the core limb phenotype (symmetrical ventral-ventral autopod/zeugopod pattern, absence of nails and patellae, loss of dorsal hair follicles) and the core renal phenotype (podocyte arrest at cuboidal stage, absent slit diaphragms, split/thickened GBM, reduced/absent COL4A3/COL4A4 and podocin expression) (Chen et al., *Nat Genet* 1998, PMID:9590288; Miner et al., *J Clin Invest* PMID via JCI13954; Morello et al., *Nat Genet* 2001, PMID:11175791). Perinatal lethality is attributed to combined eye, cerebellar, and kidney developmental failure — a **model limitation**, since human NPS is compatible with normal lifespan, so the null mouse models embryonic patterning roles more faithfully than adult disease progression.
- **Conditional *Lmx1b* knockout** (podocyte-specific, inducible in adult mice): Demonstrates a **maintenance** role for LMX1B in differentiated adult podocytes, not just developmental specification (PMC3810075) — directly relevant to modeling adult-onset/progressive human nephropathy, a feature the conventional null cannot capture due to perinatal lethality.
- ***Lmx1b* V265D dominant-negative homeodomain-variant mice**: Model a specific human-relevant missense mechanism; cause glaucoma via LBD1-mediated dimerization interference and are semi-lethal (PMC4014447). The same allele was used in the 2024–2026 single-cell trabecular meshwork study demonstrating TM3-subtype mitochondrial dysfunction as the proximate glaucoma mechanism, with vitamin B3 (nicotinamide) rescue (Tolman et al., eLife 2026/bioRxiv 2024, PMC11741249).
- **Serotonergic-neuron *Lmx1b* variant model:** A human NPS-causing *LMX1B* variant introduced into mice disrupts serotonin neuron development (Case Western Reserve Cleveland Brain Health Initiative 2019 abstract) — supports the mechanistic link to the human neuropsychiatric/sensory phenotype, though this remains a conference-abstract-level source that should be corroborated with a peer-reviewed publication before being cited as strong evidence.
- **Limb-specific *Lmx1b* auto-regulatory module mice:** Identify *cis*-regulatory (enhancer) elements whose disruption alone reproduces NPS-relevant limb pathogenicity, directly modeling the human 2024 enhancer-deletion case report (Reinhardt et al./co-authors, *Nat Commun* 2021, PMC8452625) — mechanistic support for non-coding pathogenic variants.

**Zebrafish (*Danio rerio*):**
- ***lmx1ba* and *lmx1bb* single and double knockout lines** (Moss, Neal, Kague, Lane, Hammond; *Biology Open* 2025, PMC12403520): due to teleost genome duplication, the two paralogues have **subfunctionalized** — *lmx1ba*−/− shows reduced chondrocyte proliferation/maturation (jaw/skeletal growth defects) and neuronal phenotypes, while *lmx1bb*−/− shows renal pathology with swollen/round mitochondria (kidney dysfunction, water-regulation failure) recapitulating the mitochondrial-dysfunction theme seen in the mouse glaucoma model. The double knockout adds trunk-muscle patterning defects and inflation failure. This establishes zebrafish as a genetically tractable, rapidly-scored platform for dissecting organ-specific LMX1B pathobiology, complementary to mouse.

**Applications:** Mouse models are best suited for studying developmental limb/kidney patterning mechanisms, adult podocyte maintenance, and glaucoma-relevant trabecular meshwork mitochondrial biology (including candidate therapeutic testing, e.g., vitamin B3). Zebrafish models offer high-throughput genetic/pharmacological screening for kidney and skeletal phenotypes and support dissecting paralogue-specific (i.e., domain-specific) gene function.

**Model limitations:** Conventional mouse *Lmx1b* nulls are perinatal lethal and thus cannot model the adult, chronic, slowly progressive human disease course without conditional/inducible approaches; zebrafish paralogue subfunctionalization means no single zebrafish mutant fully phenocopies the multi-system human disorder, requiring double mutants (which add non-human-relevant muscle/inflation phenotypes) to approach full pathway coverage.

**Resources:** MGI (Mouse Genome Informatics) for *Lmx1b* allele catalog; ZFIN for zebrafish *lmx1ba*/*lmx1bb* lines; IMPC/KOMP for additional conditional allele resources (not independently confirmed for LMX1B-specific IMPC coverage in this pass).

---

## Summary of Notable 2023–2024/2025 Developments
1. **Mitochondrial dysfunction as the proximate glaucoma mechanism** — single-cell/single-nucleus profiling in a mouse homeodomain-variant model identified TM3 trabecular-meshwork mitochondrial swelling/oxidative stress as the driver of elevated IOP, with vitamin B3 (nicotinamide) as a protective intervention (bioRxiv 2024 → eLife 2026, PMC11741249).
2. **Expansion of the non-coding mutational spectrum** — a 2024 report of pathogenic *LMX1B* 5′UTR variants (*npj Genomic Medicine* 2024) and a de novo limb-specific enhancer deletion producing a mild phenotype (*Clinical Genetics* 2024, doi 10.1111/cge.14447), both extending the diagnostic net beyond exonic sequencing.
3. **Zebrafish paralogue model (2025)** establishing subfunctionalized *lmx1ba*/*lmx1bb* zebrafish lines as a new, faster model system for dissecting skeletal-versus-renal-versus-neuronal LMX1B biology (PMC12403520).
4. Continued case-report-level expansion of the allelic **"isolated LMX1B-associated nephropathy"** spectrum (recurrent R246Q/R246P and other homeodomain variants) in FSGS cohorts without extrarenal disease, reinforcing that renal genetic panels should include *LMX1B* even absent classic NPS skeletal findings.

---

## Notes on Evidence Gaps and Confidence
- Most **quantitative frequencies** (e.g., 30–50% renal involvement, 5–15% ESKD, 25% reduced pain sensation, ~30–40% glaucoma) trace to GeneReviews/StatPearls aggregation of the underlying case-series literature rather than to a single large prospective cohort; treat these as best-available aggregate estimates, not precise incidence rates from a defined population.
- The **neuropsychiatric (ADHD/depression) association** rests on a single case-control symptom-survey study (PMID:21184584) and should be flagged as preliminary/exploratory rather than an established diagnostic feature.
- The **serotonergic-neuron mouse model** finding was identified via a conference abstract (Case Western/Cleveland Brain Health Initiative 2019); a peer-reviewed primary publication should be located before use as a citable KB evidence item.
- **Natural disease in other species** (veterinary/OMIA) was not confirmed in this search pass; this is a gap to close (an OMIA-specific query) rather than a confirmed negative.
- Exact **HPO CURIEs** for several suggested terms (e.g., specific nail-dysplasia child terms, reduced pain sensation, open-angle glaucoma vs. general glaucoma) and **CL/GO/UBERON CURIEs** for trabecular meshwork cell, glomerular podocyte processes, and serotonergic neuron should be verified against the live ontology (OAK/OLS) before binding, per repository convention — several here are flagged "verify exact CURIE" rather than asserted as confirmed.
- **gnomAD-specific allele frequency and pLI/LOEUF values for LMX1B** were not independently pulled in this pass and should be queried directly from gnomAD before citing a specific numeric constraint metric.

### Sources
- [OMIM #161200 — Nail-Patella Syndrome](https://omim.org/entry/161200)
- [GeneReviews — Nail-Patella Syndrome (NBK1132)](https://www.ncbi.nlm.nih.gov/books/NBK1132/)
- [StatPearls — Nail-Patella Syndrome (NBK559190)](https://www.ncbi.nlm.nih.gov/books/NBK559190/)
- [Francis et al. 2024, Clinical Genetics — De novo enhancer deletion of LMX1B produces a mild nail-patella clinical phenotype](https://onlinelibrary.wiley.com/doi/10.1111/cge.14447)
- [LMX1B haploinsufficiency due to 5'UTR variants — npj Genomic Medicine 2024](https://www.nature.com/articles/s41525-024-00460-6)
- [A deletion variant in LMX1B causing NPS in Japanese twins — PMC10904864](https://pmc.ncbi.nlm.nih.gov/articles/PMC10904864/)
- [Case report: Inversion of LMX1B — Swedish family — PMC9235307](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9235307/)
- [Regulation of GBM collagen expression by LMX1B — Nature Genetics 2001](https://www.nature.com/articles/ng0201_205)
- [LMX1B essential for maintenance of differentiated podocytes in adult kidneys — PMC3810075](https://pmc.ncbi.nlm.nih.gov/articles/PMC3810075/)
- [Transcriptional induction of slit diaphragm genes by Lmx1b — JCI](https://www.jci.org/articles/view/13954)
- [Limb and kidney defects in Lmx1b mutant mice — Nature Genetics 1998](https://www.nature.com/articles/ng0598-51)
- [Identification of limb-specific Lmx1b auto-regulatory modules — Nature Communications 2021](https://www.nature.com/articles/s41467-021-25844-5)
- [Identification of entire LMX1B gene deletions — haploinsufficiency evidence — EJHG](https://www.nature.com/articles/ejhg200883)
- [A Dominant-Negative Mutation of Mouse Lmx1b Causes Glaucoma — PMC4014447](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4014447/)
- [Single-cell profiling of trabecular meshwork identifies mitochondrial dysfunction — PMC11741249](https://pmc.ncbi.nlm.nih.gov/articles/PMC11741249/)
- [Characterisation of lmx1b paralogues in zebrafish — Biology Open 2025 — PMC12403520](https://pmc.ncbi.nlm.nih.gov/articles/PMC12403520/)
- [Genotype-phenotype: LMX1B mutation location and nephropathy risk — EJHG](https://www.nature.com/articles/5201446)
- [LMX1B Mutations Cause Hereditary FSGS without Extrarenal Involvement — PMC3736714](https://pmc.ncbi.nlm.nih.gov/articles/PMC3736714/)
- [LMX1B-associated nephropathy showing myelin figures — PMC8494852](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494852/)
- [Increased ADHD/MDD symptoms in NPS — potential LMX1B loss-of-function association — PubMed 21184584](https://pubmed.ncbi.nlm.nih.gov/21184584/)
- [Paroxysmal Cranial Dyskinesia and NPS — novel LMX1B variant — Movement Disorders 2020](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.28244)
- [A neurological phenotype in NPS illuminated by murine Lmx1b expression — EJHG](https://www.nature.com/articles/5201332)
- [Novel LMX1B mutation with variable expression of open angle glaucoma — PMC2669506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2669506/)
- [Orthopedic manifestations and management of NPS — narrative review — PMC12913535](https://pmc.ncbi.nlm.nih.gov/articles/PMC12913535/)
- [Nail-Patella Syndrome: Treatment & Management — Medscape](https://emedicine.medscape.com/article/947391-treatment)
- [Kidney disease in nail-patella syndrome — PMC2770138](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2770138/)
- [Clinical and genetic characterization of nephropathy in NPS — PubMed 32457516](https://pubmed.ncbi.nlm.nih.gov/32457516/)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 40 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001799` (1 mention) - the report calls it "Nail dysplasia"; HP calls it **Short nail**
- `HP:0008365` (1 mention) - the report calls it "Ridged nail"; HP calls it **Abnormal talus morphology**
- `HP:0001807` (1 mention) - the report calls it "Nail dysplasia — check exact term"; HP calls it **Ridged nail**
- `HP:0001800` (1 mention) - the report calls it "Absent nail"; HP calls it **Hypoplastic toenails**
- `HP:0100774` (1 mention) - the report calls it "Abnormal nail color"; HP calls it **Hyperostosis**
- `HP:0004230` (1 mention) - the report calls it "Abnormality of the toenails"; HP calls it **Subluxation of the proximal interphalangeal joint of the little finger**
- `HP:0001954` (1 mention) - the report calls it "Patellar dislocation"; HP calls it **Recurrent fever**
- `HP:0002863` (1 mention) - the report calls it "Iliac horn"; HP calls it **Myelodysplasia**
- `HP:0007398` (1 mention) - the report calls it "Reduced pain sensation — check ID"; HP calls it **Asymmetric, linear skin defects**
- `HP:0012332` (1 mention) - the report calls it "Decreased sensory nerve conduction velocity — not exact"; HP calls it **Abnormal autonomic nervous system physiology**
- `GO:0006916` (1 mention) - the report calls it "anti-apoptosis — not primary"; GO calls it **GO_0006916**
- `CL:1000452` (1 mention) - the report calls it "trabecular meshwork cell — verify exact CURIE"; CL calls it **parietal epithelial cell**
- `UBERON:0001707` (1 mention) - the report calls it "trabecular meshwork — verify"; UBERON calls it **nasal cavity**
- `UBERON:0002102` (1 mention) - the report calls it "patella"; UBERON calls it **forelimb**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0007904` (1 mention), reported as "Increased corneal curvature — not relevant" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006916` (GO_0006916) (1 mention) - replaced by `GO:0043066`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003065` (1 mention) - the report calls it "Absent patella"; HP calls it **Patellar hypoplasia**, and lists "Small patella" among its other names
- `HP:0003042` (1 mention) - the report calls it "Elbow dysplasia"; HP calls it **Elbow dislocation**
- `HP:0003083` (1 mention) - the report calls it "Radial head dislocation"; HP calls it **Dislocated radial head**, and lists "Radial head dislocation" among its other names
- `HP:0002829` (1 mention) - the report calls it "Arthralgia — not applicable"; HP calls it **Arthralgia**
- `HP:0000716` (1 mention) - the report calls it "Depressivity"; HP calls it **Depression**, and lists "Depressivity" among its other names
- `GO:0072015` (2 mentions) - the report calls it "glomerular visceral epithelial cell development", "podocyte development"; GO calls it **podocyte development**, and lists "glomerular visceral epithelial cell development" among its other names
- `GO:0007586` (1 mention) - the report calls it "digestion — not relevant"; GO calls it **digestion**
- `GO:0007507` (1 mention) - the report calls it "heart development — not relevant"; GO calls it **heart development**
- `GO:0021756` (1 mention) - the report calls it "striatum development — not directly relevant"; GO calls it **striatum development**
- `GO:0021542` (1 mention) - the report calls it "dentate gyrus development — not relevant"; GO calls it **dentate gyrus development**
- `CL:0000091` (1 mention) - the report calls it "Kupffer cell — not relevant"; CL calls it **Kupffer cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0072015` - called "glomerular visceral epithelial cell development", "podocyte development"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
