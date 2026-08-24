---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T21:00:03.622379'
end_time: '2026-08-01T21:17:54.739135'
duration_seconds: 1071.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 21
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 7
  num_turns: 40
  total_cost_usd: 3.8258884999999996
  session_id: 6120bb25-d6a4-43cd-a033-370268cb0d3f
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 21
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 21** covering all of the
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

# Comprehensive Research Report: Hypertrophic Cardiomyopathy 21 (CMH21)

**MONDO:0013852 · OMIM:614676 · Locus 7p12.1–q21 · Gene: not identified**
Prepared 2026-08-01 for dismech knowledge-base curation.

---

## ⚠️ Epistemic Status — read before curating

**CMH21 is a *linkage locus*, not a gene-defined disease entity.** The entire primary evidence base for this MONDO/OMIM entity is **a single publication describing a single four-generation kindred**: Song L, DePalma SR, Kharlap M, et al. "Novel locus for an inherited cardiomyopathy maps to chromosome 7." *Circulation*. 2006;113(18):2186–92. **PMID:16651466**; DOI:10.1161/CIRCULATIONAHA.106.615658.

Three consequences for curation:

1. **No causal gene, no variant, no protein, no mechanism is known for CMH21.** Any pathophysiology node asserting a molecular mechanism *specific to CMH21* would be fabrication. Mechanistic content must either be (a) explicitly imported from the general HCM/sarcomere-negative-HCM literature and labeled as such, or (b) omitted.
2. **A literature search of all 15 articles citing PMID:16651466 (Europe PMC, retrieved 2026-08-01) shows no follow-up study resolving the locus to a gene.** As of this report the locus remains unsolved — 20 years after mapping. This "unsolved locus" status is itself the single most curation-worthy fact about the entity and is a natural `KNOWLEDGE_GAP` discussion item.
3. **The index family's phenotype is explicitly *atypical* for sarcomeric HCM** — it combined LVH with dilation and end-stage heart failure, and histopathology in two family members **lacked** myocyte disarray and fibrosis. Do not import the canonical "myocyte disarray + interstitial fibrosis" HCM pathology chain into this entry without flagging the contradiction (see §3 and §10).

### Named Entity Confusion (NEC) preflight — PASSED, with one adjacency warning

Per the dismech NEC SOP, the MONDO record was checked against the source:

```
[Term]
id: MONDO:0013852
name: hypertrophic cardiomyopathy 21
def: "A hypertrophic cardiomyopathy associated that has material basis in region
      7p12.1-q21 variation." [DOID:0110311, PMID:16651466]
xref: DOID:0110311 / GARD:0024956 / MEDGEN:766356 / OMIM:614676 / UMLS:C3553442
synonym: "CMH21" EXACT
is_a: MONDO:0024573 ! familial hypertrophic cardiomyopathy
```
*(source: local `sqlite:obo:mondo`, `runoak info MONDO:0013852 -O obo`)*

- **Region check:** MONDO's cited region (7p12.1-q21) matches Song et al. exactly. ✅
- **Reference check:** MONDO's definition cites PMID:16651466 — the same paper. ✅
- **Gene check:** MONDO names **no gene** — consistent with the locus-only status. ✅
- **⚠️ Adjacency warning:** The second reference already cached on this branch, **PMID:21965549** (Theis JL et al., *Circ Cardiovasc Genet* 2011), maps **autosomal-recessive dilated cardiomyopathy (CMD2B, OMIM:614672)** to **7q21** and identifies **GATAD1** (OMIM:614518, 7q21.2). This is a **different disease, different inheritance mode, and — by marker position — most likely a different interval** (see §4). It is *not* the CMH21 gene and must not be curated as such. It is legitimately citable only as a *neighboring-locus / candidate-region context* note.

**High-NEC-risk class:** CMH21 belongs to a numbered series (CMH1–CMH27+) — precisely the class flagged in `research/nec_risk_disease_classes.md`. Deep-research providers routinely return CMH13 (TNNC1), CMH20 (NEXN), or CMH22 (MYPN) content when queried for "hypertrophic cardiomyopathy 21." **If any DR report you are working from names a specific gene for CMH21, discard the report.**

---

## 1. Disease Information

### Overview

Hypertrophic cardiomyopathy 21 designates a locus on chromosome 7 (7p12.1–7q21) linked to autosomal-dominant inherited cardiomyopathy in one large kindred, in which the predominant clinical feature was left ventricular hypertrophy but the phenotype also encompassed cardiac dilation, end-stage heart failure, and sudden death. The family was sarcomere-genotype-negative by direct sequencing of the then-known HCM and DCM sarcomere genes.

From the cached abstract (**PMID:16651466**, verbatim, verified against `references_cache/PMID_16651466.md`):

> "To explore novel genetic causes of inherited cardiomyopathies, genome-wide linkage analysis was used to study one kindred (4 generations, 32 individuals) with predominant clinical features of left ventricular hypertrophy in addition to cardiac dilation, end-stage heart failure, and sudden death."

> "The discovery of a novel genetic locus in this family provides more evidence that molecular pathways leading to inherited cardiac hypertrophy extend beyond the sarcomere. Identification of the causal gene mutation and additional genotype-phenotype correlation studies will provide fundamental insight into mechanisms of cardiac remodeling."

The parent-disease framing (from OMIM 614676 / MedGen 766356, which reuse the shared CMH preamble): HCM is "unexplained cardiac hypertrophy: thickening of the myocardial wall in the absence of any other identifiable cause for left ventricular hypertrophy such as systemic hypertension or valvular heart disease"; myocyte hypertrophy, disarray, and fibrosis are the histopathologic hallmarks; clinical features include arrhythmias, sudden cardiac death, and heart failure.

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| MONDO | **MONDO:0013852** | `hypertrophic cardiomyopathy 21`; `is_a` MONDO:0024573 familial hypertrophic cardiomyopathy |
| OMIM | **614676** | CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 21; CMH21 (phenotype entry, gene unknown) |
| MedGen | **766356** (CUI **C3553442**) | Hypertrophic cardiomyopathy 21 |
| DOID | **DOID:0110311** | |
| GARD | **GARD:0024956** | |
| UMLS | **C3553442** | |
| NCBI Gene | **100909387** ("CMH21") | Gene *type: unknown* — a **phenotype/locus placeholder record**, cytoband 7p12.1-q21, MIM:614676. Do **not** treat as a protein-coding gene or assign an HGNC ID. |
| HGNC | **none** | No HGNC record — there is no gene. |
| Orphanet | **no CMH21-specific code** | Orphanet does not subdivide familial isolated HCM by numbered locus; the applicable parent is ORPHA:155 (familial isolated hypertrophic cardiomyopathy). **Not currently in `references_cache/`** — run `just structured-rebuild-orphanet --id 155` if you want to cite it. |
| ICD-10 | **I42.2** (other hypertrophic cardiomyopathy) / I42.1 (obstructive HCM) | Parent-level only |
| ICD-11 | **BC43.0** Hypertrophic cardiomyopathy | Parent-level only |
| MeSH | **D024741** Cardiomyopathy, Hypertrophic, Familial; D002312 Cardiomyopathy, Hypertrophic | Parent-level only |
| SNOMED CT | 233873004 (Hypertrophic cardiomyopathy) | Parent-level only |
| ClinGen | **no gene-disease validity assertion possible** | ClinGen curates gene–disease pairs; a gene-less locus cannot be curated. No `CGGV:` reference exists for CMH21. |

### Synonyms

`CMH21` (EXACT), `cardiomyopathy, hypertrophic, 21` (EXACT), `hypertrophic cardiomyopathy type 21` (EXACT), `cardiomyopathy, familial hypertrophic, 21` (RELATED), `familial hypertrophic cardiomyopathy 21` (MedGen).

### Data provenance type

**Aggregated disease-level resources built on a single pedigree study** — i.e., OMIM/MONDO/MedGen/DOID all trace to one *Circulation* linkage paper. There is **no** EHR-derived, registry-derived, or cohort-derived data specific to CMH21. No ICEES/COHD comorbidity signal can be attributed to this entity (any such signal would be for HCM generally, MONDO:0005045 / MONDO:0024573).

---

## 2. Etiology

### Disease causal factors

- **Primary cause:** an as-yet-unidentified **germline variant segregating with disease within chromosome 7p12.1–7q21**, transmitted as an autosomal-dominant trait in one kindred. Mode of action (LOF/GOF/dominant-negative), variant class, and the affected gene are all **unknown**.
- **Explicitly excluded causes** (per PMID:16651466, verbatim):
  > "Direct DNA sequencing was performed on sarcomere genes known to cause HCM and dilated cardiomyopathy, and no mutations were identified."

  This is a *negative* mechanistic finding of real curation value: it justifies an evidence item with `supports: SUPPORT` for the claim "CMH21 is not caused by variants in the classical sarcomere genes."
- **Not established:** whether the causal lesion is coding, non-coding/regulatory, a structural variant, or a repeat expansion. Note that 2006-era sequencing would not have detected deep-intronic, regulatory, or copy-number lesions — a live hypothesis for why the locus remains unsolved.

### Risk factors

**Genetic.** The only established genetic risk factor is inheritance of the linked 7p12.1–q21 haplotype in this family (2-point LOD 4.11 — above the 3.0 genome-wide significance threshold, so linkage itself is statistically robust). **No population-level susceptibility variant, modifier gene, or GWAS locus has been assigned to CMH21.**

For general context on non-Mendelian genetic risk in *sarcomere-negative* HCM — the category this family falls into — the relevant landmark data are:
- **PMID:33495597** (Harper AR et al., *Nat Genet* 2021, "Common genetic variants and modifiable risk factors underpin hypertrophic cardiomyopathy susceptibility and expressivity"): GWAS of 2,780 cases / 47,486 controls identified **12 genome-wide-significant HCM susceptibility loci**; SNP heritability showed "a strong polygenic influence, especially for sarcomere-negative HCM (64% of cases; h²g = 0.34 ± 0.02)". A genetic risk score halved HCM odds in the lowest quintile and doubled it in the highest. **None of the 12 loci is reported to lie in 7p12.1–q21** — do not conflate.
- **PMID:33495596** (Tadros R et al., *Nat Genet* 2021): 16 HCM loci, 13 DCM loci, 23 LV-trait loci, with "strong genetic correlations between LV traits and cardiomyopathies, with opposing effects in HCM and DCM"; Mendelian randomization supported "a causal association linking increased LV contractility with HCM risk."

**Environmental.** No environmental risk factor is reported for CMH21. Generic HCM-relevant factors (all *parent-disease* level, not CMH21-specific):
- **Diastolic blood pressure** is the standout modifiable factor for sarcomere-negative HCM specifically — per PMID:33495597, "a one standard deviation increase in DBP increasing the HCM risk fourfold" (Mendelian randomization). Given the index family is sarcomere-negative, this is the most defensible environmental-modifier claim to attach, *with the caveat that it is a population-level finding, not a family-level one.*
- Age, male sex, and hypertension predict *nonfamilial* HCM (PMID:28408708: adjusted ORs — older age 1.04/yr; male sex 1.96; hypertension 2.80) — again parent-level, and this family is explicitly *familial*.
- Intense competitive athletic activity is a trigger for sudden death in HCM generally, not a cause of disease.

**Protective factors.** None known, genetic or environmental, for CMH21. At the parent level, low-DBP genetic background and a low polygenic risk score are associated with reduced HCM odds (PMID:33495597). No protective allele has been described in the 7p12.1–q21 region.

**Gene–environment interactions.** Not studied for CMH21. The general HCM paradigm — that polygenic background plus blood-pressure exposure modulates penetrance and expressivity of a rare Mendelian lesion (PMID:33495597, PMID:33495596) — is a plausible but **untested** framing for this family; curate as hypothesis (`mechanistic_hypotheses`, `status: EMERGING`) rather than as fact if included at all.

---

## 3. Phenotypes

### CMH21-specific phenotype set (from the index kindred, PMID:16651466)

The paper's abstract establishes the following as the family's clinical spectrum, in these words:

> "…one kindred (4 generations, 32 individuals) with predominant clinical features of **left ventricular hypertrophy** in addition to **cardiac dilation**, **end-stage heart failure**, and **sudden death**."

> "Of note, histopathology from 2 family members **did not demonstrate myocyte disarray and fibrosis**, indicating that this phenotype is not typical sarcomere mutation HCM."

### OMIM Clinical Synopsis features (via MedGen 766356)

MedGen renders the OMIM clinical synopsis for CMH21 with these HPO-mapped features:

| Feature | Suggested HP term | Verified label (OAK, `sqlite:obo:hp`) |
|---|---|---|
| Hypertrophic cardiomyopathy | **HP:0001639** | Hypertrophic cardiomyopathy ✅ |
| Left ventricular hypertrophy | **HP:0001712** | Left ventricular hypertrophy ✅ |
| Sudden death / sudden cardiac death | **HP:0001645** | Sudden cardiac death ✅ |
| Atrial fibrillation | **HP:0005110** | Atrial fibrillation ✅ |
| Mitral valve prolapse | **HP:0001634** | Mitral valve prolapse ✅ |
| Myofiber disarray | **HP:0031318** | Myofiber disarray ✅ |

**⚠️ Curation conflict — resolve explicitly.** MedGen/OMIM lists *myofiber disarray* among CMH21 features, but the primary paper states disarray was **absent** in the two family members examined. The most likely explanation is that OMIM's synopsis inherits the generic CMH template rather than the family's actual pathology. **Recommended handling:** either omit HP:0031318, or curate it with `supports: REFUTE` / `WRONG_STATEMENT` against PMID:16651466 with the verbatim "did not demonstrate myocyte disarray and fibrosis" snippet — this is exactly the kind of source-conflict the dismech evidence model is designed to capture.

### Additional phenotype terms defensible from the paper's own wording

| Phenotype | HP term | Verified label |
|---|---|---|
| Dilated cardiomyopathy / cardiac dilation | **HP:0001644** | Dilated cardiomyopathy ✅ |
| End-stage heart failure | **HP:0001635** | Congestive heart failure ✅ (use `severity: SEVERE`, `clinical_course: PROGRESSIVE`) |

### Parent-disease phenotypes (HCM generally — label clearly as inherited context, NOT CMH21-observed)

| Phenotype | HP term | Verified label | Typical HCM frequency |
|---|---|---|---|
| Asymmetric septal hypertrophy | HP:0001670 | Asymmetric septal hypertrophy ✅ | Most common morphology |
| LV outflow tract obstruction | HP:0032092 | Left ventricular outflow tract obstruction ✅ | ~⅓ at rest, ~⅓ provocable (PMID:28912181) |
| LV diastolic dysfunction | HP:0025168 | Left ventricular diastolic dysfunction ✅ | Near-universal |
| Myocardial fibrosis | HP:0001685 | Myocardial fibrosis ✅ | Hallmark in sarcomeric HCM |
| Dyspnea | HP:0002094 | Dyspnea ✅ | Most common symptom |
| Angina pectoris | HP:0001681 | Angina pectoris ✅ | Common |
| Syncope | HP:0001279 | Syncope ✅ | SCD risk marker |
| Palpitations | HP:0001962 | Palpitations ✅ | Common |
| Ventricular tachycardia (NSVT) | HP:0004756 | Ventricular tachycardia ✅ | SCD risk marker |
| Cardiac arrest | HP:0001695 | Cardiac arrest ✅ | |
| Arrhythmia | HP:0011675 | Arrhythmia ✅ | |
| Reduced LVEF ("burnt-out" phase) | HP:0012664 | Reduced left ventricular ejection fraction ✅ | ~2–5% of HCM; **relevant here** given the family's dilation/end-stage HF |
| Abnormal QT interval | HP:0031547 | Abnormal QT interval ✅ | |
| Inheritance | HP:0000006 | Autosomal dominant inheritance ✅ | |
| Onset | HP:0003581 | Adult onset ✅ | Family's onset ages not extractable from abstract |

### Phenotype characteristics

- **Age of onset:** Not stated in the abstract for the CMH21 family. The four-generation structure with end-stage HF and sudden death implies adult onset with substantial lifetime morbidity, but **specific ages require the full text** (paywalled at ahajournals.org; both AHA and OMIM return HTTP 403 to automated fetch). *If you need per-individual ages, wall thickness, LV dimensions, or the pedigree table, obtain the PDF through institutional access — UNC has AHA journal access via the HSL.*
- **Severity:** Variable within the kindred, ranging (per the abstract) from LVH to end-stage heart failure and sudden death.
- **Progression:** Progressive, with evolution from hypertrophy to dilation — a "burnt-out"/end-stage trajectory. Use `clinical_course: PROGRESSIVE`.
- **Frequency among affected individuals:** **Not quantified.** Do not assign HPO `FrequencyEnum` bands to any CMH21 phenotype — there is no numerator/denominator anywhere in the source. Per `docs/frequency-evidence-guidelines.md`, omit `frequency:` rather than fabricate.
- **Quality-of-life impact:** No CMH21-specific QoL data. HCM-generic instruments: KCCQ (Kansas City Cardiomyopathy Questionnaire, the primary PRO in EXPLORER-HCM and SEQUOIA-HCM), SF-36, EQ-5D. HCM QoL is dominated by exertional dyspnea, activity restriction, ICD-related anxiety, and sports-participation limitation.

---

## 4. Genetic / Molecular Information

### Causal gene: **UNKNOWN**

There is no causal gene, no OMIM gene entry, no HGNC ID, no protein, no variant nomenclature, and no ClinVar record for CMH21. **The `genetic:` block of a dismech entry for CMH21 should either be empty or contain only a locus-level statement.** No `gene_term` binding is possible.

### The locus

From PMID:16651466 (verbatim):

> "Linkage was then established to a novel locus on chromosome 7 (7p12.1-7q21). A maximum 2-point logarithm of odds score of 4.11 was obtained. Recombination events refine the disease interval between D7S506 and D7S3314, corresponding to a distance of 27.2 megabases."

| Parameter | Value |
|---|---|
| Cytogenetic location | 7p12.1–7q21 (**spans the centromere**) |
| Flanking markers | D7S506 (proximal/p-arm boundary) — D7S3314 (q-arm boundary) |
| Interval size | 27.2 Mb |
| Max 2-point LOD | 4.11 (exceeds the 3.0 significance threshold) |
| Mapping method | Genome-wide microsatellite linkage in one 4-generation, 32-individual pedigree |

**Approximate physical coordinates (my derivation — flag as computational, not from the paper).** D7S3314 is reported at ~79.81 Mb on chr7 (UCSC hg17); D7S506 lies on 7p12 telomeric to *EGFR*, in the vicinity of *GRB10* (the hGrb10 gene has been mapped between D7S506 and D7S499). Subtracting the stated 27.2 Mb from D7S3314 places the proximal boundary near ~52.6 Mb. So the interval is roughly **chr7:~52–80 Mb (hg17/hg38 approximate), i.e. 7p12.1 → 7q11.23/7q21.11**, crossing the pericentromere. This is consistent with OMIM's "7p12.1-q21" cytoband string. **Verify against the paper's Figure/Table before committing coordinates to the KB.**

**Positional candidate genes in the interval** — offered strictly as a *computational/positional* annotation by this report, **not** as candidates named in the literature. Song et al.'s abstract names none. Notable cardiovascularly plausible genes falling in ~52–80 Mb of chr7: *GRB10*, *EGFR*, *CHCHD2*, *GBAS*, *PSPH*, *HIP1*, *AUTS2*, *CALN1*, the **7q11.23 Williams–Beuren region including *ELN* (elastin), *LIMK1*, *GTF2I*, *BAZ1B*, *MLXIPL*, *STX1A***, plus *MDH2*, *HSPB1* (small heat-shock chaperone), *YWHAG* (14-3-3γ), *POR*, and — at/just beyond the distal boundary — *CACNA2D1*. **Do not curate any of these as CMH21 candidates in a `genetic:` block.** At most they belong in a `discussions` KNOWLEDGE_GAP `rationale` describing what a modern re-analysis would target.

### The GATAD1 / 7q21 adjacency (why PMID:21965549 is on this branch)

From the cached abstract of **PMID:21965549** (Theis JL et al., *Circ Cardiovasc Genet* 2011; verbatim from `references_cache/PMID_21965549.md`):

> "Genotyping and linkage analysis mapped an AR DCM locus to chromosome arm 7q21, which was validated and refined by high-density homozygosity mapping."

> "The mutation, absent in HapMap, 1000 Genomes, and 474 ethnically matched controls, altered a conserved residue of GATAD1, encoding GATA zinc finger domain-containing protein 1. Thirteen relatives were heterozygous mutation carriers with no evidence of myocardial disease, even at advanced ages."

> "GATAD1 binds to a histone modification site that regulates gene expression. Consistent with murine DCM caused by genetic disruption of histone deacetylases, the data implicate an inherited basis for epigenetic dysregulation in human heart failure."

Key distinctions to preserve if this is cited at all:

| | CMH21 (PMID:16651466) | GATAD1 / CMD2B (PMID:21965549) |
|---|---|---|
| Phenotype | LVH-predominant, with dilation/end-stage HF | Dilated cardiomyopathy |
| Inheritance | Autosomal **dominant** | Autosomal **recessive** (heterozygotes unaffected even at advanced ages) |
| Locus | 7p12.1–7q21 (~52–80 Mb) | 7q21 (*GATAD1* at ~92.5 Mb, **distal to the CMH21 interval**) |
| Gene | Unknown | *GATAD1* (OMIM:614518), p.Ser102Pro |
| OMIM phenotype | 614676 | 614672 (CMD2B) |

*GATAD1* screening in 273 additional DCM probands found no further mutations, so it is a rare cause even of DCM. **Curating GATAD1 as the CMH21 gene would be a textbook NEC error.** If you cite PMID:21965549, do so only to document that a mechanistically distinct 7q21 cardiomyopathy locus exists nearby and was excluded, and use `evidence_source: HUMAN_CLINICAL`.

### Other genetic dimensions

- **Variant classification / ACMG:** N/A — no variant.
- **Allele frequency (gnomAD etc.):** N/A — no variant.
- **Somatic vs germline:** Germline (inherited through four generations).
- **Functional consequence:** Unknown.
- **Modifier genes:** None described for CMH21. Parent-level: polygenic score modifies expressivity in rare-variant carriers (PMID:33495596, PMID:33495597).
- **Epigenetics:** No CMH21 data. (Note only the *conceptual* adjacency that the neighboring 7q21 DCM gene *GATAD1* is chromatin-associated — this is not evidence about CMH21.)
- **Chromosomal abnormalities:** None reported. No CNV, translocation, or microdeletion has been associated with CMH21. Notably, the interval **contains the 7q11.23 Williams–Beuren critical region**, whose recurrent deletion causes a well-characterized, mechanistically unrelated cardiovascular syndrome (supravalvular aortic stenosis) — a useful negative differential, not an etiologic link.

---

## 5. Environmental Information

- **Environmental factors:** None reported for CMH21. No toxin, radiation, pollutant, or occupational exposure is implicated.
- **Lifestyle factors:** None reported for CMH21. Parent-level HCM: blood pressure (see §2), competitive athletics as an SCD trigger, alcohol/dehydration/vasodilators as provocateurs of outflow obstruction in obstructive HCM.
- **Infectious agents:** Not applicable. CMH21 is a Mendelian, non-infectious condition. Viral myocarditis is a *differential diagnosis* for unexplained cardiomyopathy, not an etiology here.

---

## 6. Mechanism / Pathophysiology

### What is actually known about CMH21 mechanism

**Essentially nothing at the molecular level.** The only mechanistic claims that can be evidenced from PMID:16651466 are:

1. **Negative claim (well-evidenced):** the disease in this family is not caused by classical sarcomere-gene mutation — "Direct DNA sequencing was performed on sarcomere genes known to cause HCM and dilated cardiomyopathy, and no mutations were identified."
2. **Negative claim (well-evidenced):** the tissue-level pathology differs from sarcomeric HCM — "histopathology from 2 family members did not demonstrate myocyte disarray and fibrosis, indicating that this phenotype is not typical sarcomere mutation HCM."
3. **Positive inference (author-stated, appropriately hedged):** "molecular pathways leading to inherited cardiac hypertrophy extend beyond the sarcomere."

**Recommended dismech pathophysiology graph for CMH21** — a deliberately short, honest chain:

```
[Unidentified 7p12.1–q21 germline variant]  (biological_scale: MOLECULAR)
        ↓  (mechanism unknown — hypothesis group: extra-sarcomeric hypertrophy)
[Non-sarcomeric hypertrophic signaling]      (biological_scale: CELLULAR; speculative)
        ↓
[Left ventricular hypertrophy without myocyte disarray]  (biological_scale: TISSUE)
        ↓
[Ventricular dilation and contractile failure]           (biological_scale: TISSUE)
        ↓
[End-stage heart failure / sudden cardiac death]         (biological_scale: ORGANISM)
```

Only the last three nodes are evidenced. The second node should be marked as belonging to an `EMERGING`/`SPECULATIVE` `mechanistic_hypotheses` group, or dropped.

### Conformance opportunity

The chain "cardiomyocyte insult → remodeling → contractile dysfunction → heart failure" is exactly the existing dismech module **`cardiomyopathy_maladaptive_remodeling`** (key conformance target: `cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling`). Declaring `conforms_to` at the ventricular-remodeling and contractile-dysfunction nodes is defensible and adds value without asserting unknown molecular content. Conformance to `cardiac_ion_channel_repolarization` is **not** warranted (no channelopathy evidence).

### Parent-disease mechanism (import only with explicit labeling)

For general sarcomeric HCM, the canonical chain (PMID:28912181, Marian AJ & Braunwald E, *Circ Res* 2017) is: sarcomere variant → altered actin–myosin cross-bridge kinetics and increased myofilament Ca²⁺ sensitivity → **hypercontractility** with increased energetic cost per unit force → impaired relaxation and diastolic dysfunction → stress-responsive hypertrophic signaling in cardiomyocytes → myocyte hypertrophy, myofibrillar disarray, interstitial fibrosis → dynamic LVOT obstruction (in ~⅓ at rest, ~⅓ provocable), microvascular ischemia, arrhythmogenic substrate → heart failure and sudden death. The paper states "Mutations in over a dozen genes encoding sarcomere-associated proteins cause HCM. MYH7 and MYBPC3 … are the 2 most common genes involved, together accounting for ≈50% of the HCM families" and that ~40% of HCM patients lack identified causal genes. Hypercontractility as the therapeutic target is confirmed by EXPLORER-HCM (PMID:32871100): "Cardiac muscle hypercontractility is a key pathophysiological abnormality in hypertrophic cardiomyopathy, and a major determinant of dynamic left ventricular outflow tract (LVOT) obstruction."

**Critically, this chain is the one the CMH21 family's histopathology contradicts.** Import it only as contrast.

### Sarcomere-negative HCM mechanism — the most relevant parent literature

Because CMH21 is sarcomere-negative, the most apt mechanistic context is the emerging biology of genotype-negative HCM:

- **PMID:38853772** (Nollet EE et al., *Circ Genom Precis Med* 2024, "Integrating Clinical Phenotype With Multiomics Analyses of Human Cardiac Tissue Unveils Divergent Metabolic Remodeling in Genotype-Positive and Genotype-Negative Patients With Hypertrophic Cardiomyopathy"). Reported findings: HCM myectomy samples exhibited "(1) increased glucose and glycogen metabolism, (2) downregulation of fatty acid oxidation, and (3) reduced ceramide formation and lipid storage." Crucially, remodeling in **genotype-negative** patients correlated with *depleted* acylcarnitines, amino acids, nucleotide precursors and redox compounds (a mitochondrial-dysfunction signature), whereas in **genotype-positive** patients the same metabolites were *positively* associated with hypertrophy — "suggesting fundamentally different disease mechanisms between groups." Also reported: upregulated proteasomal proteins and downregulated mitochondrial translation machinery across HCM samples. This is the single best citation for "sarcomere-negative HCM is mechanistically distinct," and is directly on-point for CMH21's category, though **not** about this locus.
- **Polygenic contribution:** sarcomere-negative HCM has substantial common-variant heritability (h²g = 0.34 ± 0.02; PMID:33495597).

### Suggested ontology terms for mechanism nodes (all OAK-verified)

**GO biological processes**

| GO ID | Verified label | Use |
|---|---|---|
| GO:0003300 | cardiac muscle hypertrophy | Core hypertrophy node; `modifier: INCREASED` |
| GO:0055008 | cardiac muscle tissue morphogenesis | Remodeling |
| GO:0060047 | heart contraction | Contractile output |
| GO:0086003 | cardiac muscle cell contraction | Cell-level contraction |
| GO:0002026 | regulation of the force of heart contraction | Hypercontractility (parent-disease) |
| GO:0055117 | regulation of cardiac muscle contraction | |
| GO:0006942 | regulation of striated muscle contraction | |
| GO:0006936 | muscle contraction | |
| GO:0030239 | myofibril assembly | Relevant to disarray (here: *absent*) |
| GO:0010659 | cardiac muscle cell apoptotic process | Late remodeling / dilation |
| GO:0030199 | collagen fibril organization | Fibrosis (here: *absent* in the 2 examined members) |
| GO:0046034 | ATP metabolic process | Energetics |
| GO:0006006 | glucose metabolic process | `modifier: INCREASED` (PMID:38853772) |
| GO:0019395 | fatty acid oxidation | `modifier: DECREASED` (PMID:38853772) |

**CL cell types**

| CL ID | Verified label |
|---|---|
| CL:0000746 | cardiac muscle cell |
| CL:0002131 | regular ventricular cardiac myocyte |
| CL:0002548 | fibroblast of cardiac tissue |
| CL:0000071 | blood vessel endothelial cell |
| CL:0000669 | pericyte |

**Subcellular (GO cellular component, unverified in this session — verify before use):** sarcomere (GO:0030017), myofibril (GO:0030016), mitochondrion (GO:0005739), Z disc (GO:0030018).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: the heart, specifically the left ventricle and interventricular septum. Secondary: left atrium (dilation, AF substrate), mitral valve apparatus (prolapse per the OMIM synopsis; SAM in obstructive HCM generally), pulmonary circulation and systemic organs via heart failure. Body system: cardiovascular. No extracardiac involvement is reported — CMH21 is a **nonsyndromic, cardiac-restricted** entity as described.

**Tissue and cell level.** Myocardium (cardiac muscle tissue); cardiomyocytes are the hypertrophying cell; cardiac fibroblasts and the microvasculature are involved in general HCM but **fibrosis was not observed** in the two CMH21 family members examined.

**Subcellular.** Unknown for CMH21. In sarcomeric HCM: sarcomere/myofibril, Z-disc, mitochondria.

**Localization and laterality.** Left-sided/left-ventricular predominance; asymmetric septal involvement is the usual HCM pattern but the CMH21 family's specific morphology (septal vs concentric vs apical) is not stated in the abstract — **obtain from the full text before curating a morphology claim.**

**UBERON terms (OAK-verified)**

| UBERON ID | Verified label |
|---|---|
| UBERON:0000948 | heart |
| UBERON:0002084 | heart left ventricle |
| UBERON:0002094 | interventricular septum |
| UBERON:0002349 | myocardium |
| UBERON:0002135 | mitral valve |
| UBERON:0002079 | left cardiac atrium |

---

## 8. Temporal Development

- **Onset age:** Not specified in the available abstract for CMH21. Four-generation segregation with adult end-stage heart failure and sudden death implies adolescent-to-adult onset. HP:0003581 (Adult onset) is the defensible default, but **flag as inferred**, not sourced.
- **Onset pattern:** Insidious/chronic; disease is typically detected on family screening or after symptom onset. Sudden death may be the sentinel event.
- **Stages:** The family's course maps onto the recognized HCM trajectory: (i) subclinical/gene-positive-phenotype-negative → (ii) hypertrophic phase with preserved EF → (iii) **transition to dilation with declining EF ("burnt-out"/end-stage HCM)** → (iv) advanced heart failure requiring transplant/MCS. The explicit mention of "cardiac dilation, end-stage heart failure" in the abstract makes stage (iii)–(iv) a *documented*, not merely theoretical, feature of this kindred — unusual, since only ~2–5% of unselected HCM reaches this phase.
- **Progression rate:** Variable; not quantified for CMH21.
- **Course pattern:** Chronic and progressive, punctuated by arrhythmic events (AF, sudden death).
- **Duration:** Lifelong.
- **Remission:** None spontaneous. Treatment can relieve symptoms and obstruction but does not reverse the genetic substrate; regression of hypertrophy is not an established outcome.
- **Critical periods:** Adolescence/early adulthood for phenotypic conversion in at-risk relatives (drives serial screening intervals); the window before ventricular dilation is the plausible window for disease-modifying intervention.

---

## 9. Inheritance and Population

### Epidemiology of CMH21 specifically

**Prevalence: unknown; likely ultra-rare or private to one kindred.** One family has ever been reported. Recommended dismech `Prevalence` record:

```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: UNKNOWN
  notes: >-
    Reported in a single 4-generation kindred (32 individuals genotyped);
    no additional families or population estimates published as of 2026-08.
  evidence:
  - reference: PMID:16651466
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "one kindred (4 generations, 32 individuals)"
    explanation: Establishes that CMH21 rests on a single reported family.
```

### Parent-disease epidemiology (HCM), for context only

- **PMID:7641357** (Maron BJ et al., *Circulation* 1995, CARDIA echocardiographic study of 4,111 young adults): "Probable or definite echocardiographic evidence of HCM was present in 7 subjects (0.17%)"; "Prevalence in men and women was 0.26:0.09%; in blacks and whites, 0.24:0.10%"; conclusion: "HCM was present in about 2 of 1000 young adults." → the classic **1 in 500** figure (200 per 100,000).
- **PMID:25814232** (Semsarian C et al., *JACC* 2015): argues HCM "is more common than previously estimated" once gene-positive/phenotype-negative individuals and modern imaging are accounted for — the basis of the widely quoted **1 in 200** genetic prevalence (500 per 100,000).
- **PMID:28408708** (Ingles J et al., *Circ Cardiovasc Genet* 2017): "Approximately 40% of HCM probands have a nonfamilial subtype, with later onset and less severe clinical course."

### Inheritance parameters for CMH21

| Parameter | Value / status |
|---|---|
| Pattern | **Autosomal dominant** (HP:0000006) — four-generation vertical transmission |
| Penetrance | Not quantified; the LOD of 4.11 is consistent with high penetrance under the assumed model, but the paper's penetrance assumption is not in the abstract. **Do not state a penetrance figure.** |
| Expressivity | **Variable** — the same haplotype produced LVH, dilation, end-stage HF, and sudden death within one family |
| Anticipation | Not reported; no repeat-expansion mechanism proposed |
| Germline mosaicism | Not reported |
| Founder effect | Not applicable/not assessed (single family) |
| Consanguinity | Not reported; irrelevant to a dominant model |
| Carrier frequency | Not applicable (dominant; no variant identified) |

### Population demographics

- **Affected populations:** One kindred; ancestry not stated in the abstract. **No** ethnic, geographic, or founder association can be asserted.
- **Geographic distribution:** Study conducted at Harvard Medical School / Brigham (Boston, USA); family origin not specified in the abstract.
- **Sex ratio:** Not reported; autosomal dominant inheritance predicts ~1:1 transmission.
- **Age distribution:** Not reported.

---

## 10. Diagnostics

**There is no CMH21-specific diagnostic test.** No clinical genetic test can diagnose CMH21, because there is no gene to sequence; a linkage-based diagnosis is possible only within the original informative pedigree. Everything below is HCM-generic and should be curated as such.

### Clinical tests

- **Echocardiography** (first-line): maximal LV wall thickness ≥15 mm (or ≥13 mm with family history) unexplained by loading conditions; LV cavity size; LVEF; LVOT gradient at rest and with provocation (Valsalva, exercise); systolic anterior motion of the mitral valve; diastolic indices (E/e′, LA volume index); mitral valve morphology and prolapse.
- **Cardiac magnetic resonance (CMR)**: the reference standard for wall-thickness measurement and apical/anterolateral segments; **late gadolinium enhancement (LGE)** quantifies replacement fibrosis and is both a diagnostic and prognostic marker. In this family CMR would be especially informative given the reported *absence* of fibrosis histologically.
- **ECG** (12-lead): abnormal in most HCM; LVH voltage, repolarization abnormalities, pathologic Q waves, deep T-wave inversion. In CARDIA, "ECGs were abnormal in 5 of the 7 subjects" (PMID:7641357).
- **Ambulatory ECG monitoring** (24–48 h Holter or extended): detects NSVT (an SCD risk factor) and atrial fibrillation — directly relevant given AF is in the CMH21 synopsis.
- **Exercise testing / CPET**: functional capacity, provocable obstruction, blood-pressure response (abnormal BP response is a risk marker).
- **Laboratory / biomarkers:** NT-proBNP and high-sensitivity troponin (prognostic in HCM, not diagnostic). **Phenocopy exclusion labs are essential** and are arguably the highest-yield workup for a sarcomere-negative, disarray-negative family like this one: α-galactosidase A activity and *GLA* genotyping (Fabry), serum/urine immunofixation + free light chains and bone-scintigraphy (cardiac amyloidosis), creatine kinase and *LAMP2*/Danon workup in young males, *PRKAG2* glycogen-storage cardiomyopathy (pre-excitation + conduction disease).
- **Endomyocardial biopsy / explant histopathology:** normally shows myocyte hypertrophy, myofibrillar disarray, and interstitial fibrosis in sarcomeric HCM (HP:0031318, HP:0001685). **In this kindred, two members showed neither disarray nor fibrosis** — a defining negative finding.

### Genetic testing

- **Recommended approach (parent-disease):** an HCM/cardiomyopathy multigene panel covering the eight core sarcomere genes (*MYH7, MYBPC3, TNNT2, TNNI3, TPM1, MYL2, MYL3, ACTC1*) plus phenocopy genes (*GLA, LAMP2, PRKAG2, TTR, PTPN11* and other RASopathy genes, *DES, FHL1*). See GeneReviews **PMID:20301725** ("Nonsyndromic Hypertrophic Cardiomyopathy Overview," updated 2025-03-06) and the 2024 AHA/ACC guideline (**PMID:38718139**).
- **Expected result in CMH21:** negative. The index family was sarcomere-negative by direct sequencing.
- **WES/WGS:** the appropriate modern strategy for this family and for the locus. WGS is specifically indicated because it can detect the lesion classes 2006 Sanger sequencing of coding exons would have missed: deep-intronic/splice-altering, promoter/enhancer, and structural variants. Combining WGS with the existing linkage interval (~27 Mb) would be a high-yield reanalysis — this is the concrete `proposed_experiments` content for the KNOWLEDGE_GAP discussion.
- **CMA / karyotype / FISH:** no indication; no chromosomal abnormality reported. CMA would nonetheless be a reasonable adjunct if a structural variant in the interval is hypothesized.
- **mtDNA / repeat-expansion testing:** not indicated (dominant nuclear transmission, no anticipation).
- **Cascade / linkage-based testing:** within the original pedigree, haplotype segregation at D7S506–D7S3314 could in principle stratify at-risk relatives — but with a 27 Mb interval and no functional variant, this is research-grade, not clinical-grade, and should not be presented as a clinical test.

### Clinical criteria

Diagnosis follows generic HCM criteria (2024 AHA/ACC, PMID:38718139; 2023 ESC cardiomyopathy guidelines, PMID:37622657): unexplained LV wall thickness ≥15 mm in an adult (≥13 mm with a positive family history or positive genotype), in the absence of abnormal loading conditions sufficient to explain it; in children, wall thickness ≥2 SD above the predicted mean (z-score >2).

**Differential diagnosis** (particularly important here, because absent disarray/fibrosis plus dilation should prompt reconsideration of an infiltrative or metabolic cause):

| Condition | Distinguishing features |
|---|---|
| Hypertensive heart disease | Concentric, history of hypertension, regresses with BP control |
| Athlete's heart | ≤15 mm, LV cavity enlarged, regresses with detraining |
| Fabry disease (*GLA*, X-linked) | Low native T1 on CMR, α-Gal A deficiency, extracardiac features |
| Cardiac amyloidosis (ATTR/AL) | Elevated native T1/ECV, diffuse LGE, positive PYP scan or monoclonal protein |
| Danon disease (*LAMP2*) | Young males, extreme LVH, pre-excitation, myopathy, intellectual disability |
| PRKAG2 glycogen storage cardiomyopathy | Pre-excitation, progressive conduction disease |
| Noonan/RASopathies | Dysmorphism, pulmonary valve stenosis, short stature |
| Mitochondrial cardiomyopathy | Maternal inheritance, multisystem involvement, lactate |
| Other numbered CMH loci (CMH1–CMH27) | Gene-defined; **CMH21 is the diagnosis of exclusion here only within the mapped family** |

### Screening

For families with unexplained inherited cardiomyopathy and no identified variant — exactly this situation — guidelines recommend **serial clinical screening of first-degree relatives** (ECG + echocardiography), typically every 1–2 years in adolescence and every 3–5 years in adulthood, continuing indefinitely because genetic testing cannot discharge relatives from surveillance. There is no newborn screening or population carrier screening for HCM.

---

## 11. Outcome / Prognosis

### CMH21-specific

No survival data, no cohort, no natural-history study. What the primary source establishes qualitatively: the family's phenotype included **end-stage heart failure and sudden death** — i.e., a severe, fully-penetrant-appearing, malignant course in at least some members. That is the extent of defensible prognostic content.

### Parent-disease prognosis (label as HCM-general)

- **PMID:30297972** (Ho CY et al., *Circulation* 2018, SHaRe registry; 4,591 patients, 2,763 genotyped, mean follow-up 5.4 ± 6.9 years): "Patients <40 years old at diagnosis had a 77% [95% confidence interval: 72%, 80%] cumulative incidence of the overall composite outcome by age 60"; young HCM patients had "4-fold higher mortality than the general United States population"; "Heart failure and atrial fibrillation were the most prevalent adverse events," with younger age at diagnosis and **sarcomere mutations predicting worse outcomes**. *Note the direction: sarcomere-positive status is the adverse marker — the CMH21 family is sarcomere-negative yet clinically severe, so SHaRe's genotype stratification does not transfer.*
- **PMID:28408708:** nonfamilial (sarcomere-negative, no family history) HCM "had a less severe clinical course with greater event-free survival from major cardiac events (P=0.04) compared with sarcomere-positive HCM probands." Again, **the CMH21 family is familial**, so this favorable stratum does not apply.
- **PMID:28912181:** "In the majority of patients, HCM has a relatively benign course. However, HCM is also an important cause of sudden cardiac death, particularly in adolescents and young adults." Major SCD risk factors: nonsustained VT, syncope, family history of SCD, severe hypertrophy.
- **SCD risk prediction:** HCM Risk-SCD (O'Mahony C et al., *Eur Heart J* 2014, **PMID:24126876**) — a validated individualized 5-year SCD risk model developed in 3,675 patients over 24,313 patient-years, incorporating seven predictors (age, maximal wall thickness, left atrial diameter, LVOT gradient, family history of SCD, NSVT, unexplained syncope). The ESC guideline uses this; the AHA/ACC guideline uses a risk-marker approach that additionally weighs LGE extent, apical aneurysm, and LVEF <50%.

### Morbidity, complications, function

Progressive exertional dyspnea and reduced exercise capacity; atrial fibrillation with thromboembolic stroke risk (AF in HCM warrants anticoagulation largely irrespective of CHA₂DS₂-VASc); ventricular arrhythmias and SCD; progression to end-stage HF requiring transplantation; infective endocarditis (rare, obstructive HCM); ICD-related complications (inappropriate shocks, lead failure, psychological burden). Quality of life is measured with KCCQ, SF-36, EQ-5D; HCMSQ (HCM Symptom Questionnaire) is used in myosin-inhibitor trials.

### Prognostic factors and biomarkers

Age at diagnosis, maximal wall thickness, LVOT gradient, LA size, NSVT, unexplained syncope, family history of SCD, LVEF <50%, apical aneurysm, extensive LGE on CMR, elevated NT-proBNP and hs-troponin. Sarcomere-variant status is prognostic in the parent disease but **uninformative for CMH21**.

---

## 12. Treatment

**No CMH21-specific, genotype-directed, or locus-directed therapy exists or is in development.** Management follows general HCM guidelines — 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR (**PMID:38718139**) and 2023 ESC (**PMID:37622657**). Given this family's LVH-with-dilation/end-stage-HF phenotype, **advanced heart-failure management and transplant evaluation are as relevant as classic HCM obstruction therapy** — an important nuance if you curate treatments for this entry.

### Pharmacotherapy

| Treatment | NCIT `treatment_term` | `therapeutic_agent` | `therapeutic_modality` | Notes |
|---|---|---|---|---|
| Beta-blockade (first-line, symptomatic) | NCIT:C15986 Pharmacotherapy ✅ | NCIT:C29576 **Beta-Adrenergic Antagonist** ✅ ; CHEBI:6904 **metoprolol** ✅ | SMALL_MOLECULE | Reduces gradient, improves diastolic filling |
| Non-dihydropyridine calcium channel blockade | NCIT:C15986 ✅ | NCIT:C333 **Calcium Channel Blocker** ✅ ; CHEBI:9948 **verapamil** ✅ | SMALL_MOLECULE | Alternative when beta-blockers not tolerated; caution in severe obstruction/hypotension |
| Disopyramide (add-on for obstruction) | NCIT:C15986 ✅ | CHEBI:4657 **disopyramide** ✅ | SMALL_MOLECULE | Negative inotrope; anticholinergic effects; QT monitoring |
| Cardiac myosin inhibitor — mavacamten | NCIT:C15986 ✅ | **NCIT:C174901 Mavacamten** ✅ | SMALL_MOLECULE | **Obstructive HCM only.** EXPLORER-HCM (PMID:32871100): 251 patients, 30 weeks; 37% vs 17% met the composite primary endpoint (p=0.0005); greater reduction in post-exercise LVOT gradient. REMS/echo monitoring for systolic dysfunction. |
| Cardiac myosin inhibitor — aficamten | NCIT:C15986 ✅ | **NCIT:C179072 Aficamten** ✅ | SMALL_MOLECULE | SEQUOIA-HCM (PMID:38739079): 282 patients, 24 weeks; peak VO₂ +1.8 vs 0.0 mL/kg/min (difference 1.7, p<0.001); "The results for all 10 secondary end points were significantly improved with aficamten as compared with placebo." |
| Antiarrhythmic for AF | NCIT:C15986 ✅ | CHEBI:2663 **amiodarone** ✅ | SMALL_MOLECULE | Rhythm control; sotalol/dofetilide alternatives |
| Anticoagulation for AF | NCIT:C15986 ✅ | DOAC or warfarin (verify CHEBI ids before use) | SMALL_MOLECULE | HCM + AF → anticoagulate largely irrespective of CHA₂DS₂-VASc |
| Guideline-directed HF therapy once EF falls | NCIT:C15986 ✅ | ACEi/ARB/ARNI, beta-blocker, MRA, SGLT2i (verify ids) | SMALL_MOLECULE | **Applies specifically to the end-stage/dilated phase seen in this kindred**; vasodilators are contraindicated while obstruction persists |

**⚠️ Important caveat for this entry:** cardiac myosin inhibitors are approved and studied only for **obstructive** HCM with preserved EF; they are contraindicated/inappropriate in the dilated, low-EF phase. Since the CMH21 family's described phenotype includes dilation and end-stage HF, curating mavacamten/aficamten under this entry requires an explicit scope note.

**Pharmacogenomics:** No HCM- or CMH21-specific PGx. Generic relevance only: *CYP2D6* metabolizer status for metoprolol; *CYP2C9*/*VKORC1* for warfarin (CPIC guidelines). Of incidental note, the *CYP3A* cluster lies on 7q22.1 just distal to the linkage interval — coincidental, not mechanistic.

### Advanced therapeutics

- **Gene therapy / gene editing:** none for CMH21 (no target). At the parent level, *MYBPC3* gene-replacement (e.g. TN-201) and base-editing approaches for *MYH7* are in early clinical/preclinical development — **not applicable** to a gene-less locus.
- **RNA-based therapies, cell therapy, immunotherapy, targeted therapy:** none applicable.

### Surgical and interventional

| Intervention | NCIT term (OAK-verified) | Notes |
|---|---|---|
| Septal myectomy (Morrow procedure) | **NCIT:C51591 Myectomy** ✅ (or NCIT:C15329 Surgical Procedure ✅) | Gold standard for drug-refractory obstruction at experienced centers; `therapeutic_modality: SURGERY` |
| Alcohol septal ablation | **NCIT:C80439 Septal Ablation** ✅ | Catheter-based alternative for suitable anatomy; `therapeutic_modality: SURGERY` (procedure bucket) |
| ICD implantation (primary/secondary SCD prevention) | **NCIT:C80435 Implantable Cardioverter-Defibrillator Placement** ✅ ; device **NCIT:C93238 Implantable Cardioverter-Defibrillator** ✅ | Driven by HCM Risk-SCD / AHA-ACC risk markers; **highly relevant to this kindred given documented sudden death** |
| Heart transplantation | **NCIT:C15246 Heart Transplantation** ✅ (parent NCIT:C15289 Organ Transplantation ✅) | For end-stage disease — **explicitly relevant given "end-stage heart failure" in the family** |
| Mechanical circulatory support (LVAD) | NCIT:C49236 Therapeutic Procedure ✅ | Technically challenging in small, hypertrophied cavities; more feasible once dilated |
| AF catheter ablation | NCIT:C49236 ✅ | Symptomatic AF |

### Supportive, rehabilitative, experimental

- Supportive care (NCIT:C15747 ✅): symptom management, volume/BP optimization, avoidance of dehydration and vasodilators in obstructive physiology.
- **Genetic counseling (NCIT:C15240 ✅)** — arguably the highest-value "treatment" for this entry: counseling must explain that a negative gene panel does **not** exclude disease in relatives, that surveillance is clinical and lifelong, and that research WGS re-analysis may be offered.
- Exercise counseling: 2024 guideline liberalized recommendations; mild-to-moderate recreational exercise is encouraged, with shared decision-making for higher intensity/competitive sport.
- Experimental: HCM trials of myosin inhibitors, ninerafaxstat (cardiac mitotrope), and gene therapies are all enrolling by *phenotype* (obstructive/nonobstructive HCM) or by *specific genotype* — a CMH21 patient could be eligible on phenotype only. **No trial targets this locus.** Search ClinicalTrials.gov by "hypertrophic cardiomyopathy," not by CMH21; there are no CMH21 NCT records.

### Treatment strategy

Algorithm: (1) confirm HCM and exclude phenocopies; (2) stratify SCD risk → ICD decision; (3) if obstructive and symptomatic → beta-blocker → verapamil → add disopyramide or a myosin inhibitor → septal reduction therapy; (4) if nonobstructive and symptomatic → symptom-directed therapy, evaluate for microvascular ischemia/diastolic HF; (5) **if EF falls / cavity dilates → switch to guideline-directed HF therapy, stop negative inotropes and myosin inhibitors, evaluate for transplant**; (6) manage AF aggressively with anticoagulation; (7) screen and counsel the family. Step (5) is the pathway this kindred actually traversed.

---

## 13. Prevention

- **Primary prevention (of the disease itself):** not possible — CMH21 is a germline Mendelian condition. Reproductive options for known carriers within an informative family are the only true primary prevention: genetic counseling, prenatal diagnosis, and preimplantation genetic testing (PGT-M) — **but all require a known variant, which CMH21 lacks.** This is a concrete, patient-facing harm of the unsolved locus and belongs in the entry's knowledge-gap rationale.
- **Secondary prevention (early detection):** cascade **clinical** screening (ECG + echocardiography ± CMR) of first-degree relatives, at the intervals in §10. Because no variant exists, no relative can be released from surveillance — the family carries the full lifetime screening burden.
- **Tertiary prevention (complication avoidance):** ICD for SCD prevention in high-risk individuals; anticoagulation for AF-related stroke prevention; blood-pressure control (biologically motivated by the DBP–sarcomere-negative-HCM Mendelian randomization result, PMID:33495597); avoidance of dehydration and vasodilators in obstructive physiology; individualized exercise prescription; heart-failure prevention through GDMT once systolic function declines.
- **Immunization:** not applicable to etiology; routine influenza/COVID-19/pneumococcal vaccination is standard supportive care in heart failure.
- **Genetic screening programs:** no newborn or population screening exists for HCM. Pre-participation athletic screening (ECG-inclusive in Italy and per some societies) detects HCM generally, not CMH21.
- **Public health / environmental interventions:** not applicable.
- **Prophylaxis:** no pharmacologic prophylaxis prevents phenotype development in at-risk relatives. (Trials of pre-clinical intervention — e.g. VANISH with valsartan in sarcomere-variant carriers — were conducted in *genotyped* cohorts and cannot enroll CMH21 relatives.)

---

## 14. Other Species / Natural Disease

**No CMH21 ortholog can exist** — the locus has no gene, so there is no ortholog to identify and no comparative-genomics analysis to perform. The 7p12.1–q21 human region is broadly syntenic with portions of mouse chromosomes 5, 6, and 11, but stating anything more specific would be speculation.

Naturally occurring HCM in other species (**parent-disease context only**):

| Species | NCBI Taxon | Findings |
|---|---|---|
| Domestic cat (*Felis catus*) | NCBITaxon:9685 | **The premier spontaneous animal model of HCM.** Maine Coon: *MYBPC3* p.A31P — "The discovery represents the first documented spontaneous mutation causing HCM in a non-human species" (Meurs KM et al., *Hum Mol Genet* 2005, **PMID:16236761**). Ragdoll: a separate *MYBPC3* mutation converting a conserved arginine to tryptophan, in a different protein domain, arising independently (Meurs KM et al., *Genomics* 2007, **PMID:17521870**). Feline HCM is the most common feline heart disease and causes congestive heart failure, aortic thromboembolism, and sudden death. VBO breed terms exist for Maine Coon and Ragdoll (verify VBO IDs with OAK before curating). |
| Dog (*Canis lupus familiaris*) | NCBITaxon:9615 | HCM is rare in dogs; DCM predominates |
| Pig, rhesus macaque | — | Engineered/experimental HCM models only |

**OMIA** records exist for feline HCM (Maine Coon and Ragdoll *MYBPC3*). **Zoonotic potential / cross-species transmission:** not applicable — this is a genetic, non-transmissible disease.

---

## 15. Model Organisms

**There is no CMH21 model of any kind** — no mouse, zebrafish, fly, iPSC line, or organoid — because there is no gene to knock out, knock in, or edit. Any DR-report claim of a "CMH21 mouse model" is fabricated; treat as an automatic discard signal.

Models of the **parent disease** (import only with explicit `evidence_source: MODEL_ORGANISM` and a scope note):

- **αMHC⁴⁰³/⁺ mouse** (Geisterfer-Lowrance AA et al., *Science* 1996, **PMID:8614836**): the founding HCM mouse, made by introducing the "Arg 403 --> Gln mutation into the alpha cardiac myosin heavy chain (MHC) gene." Homozygotes died at ~7 days; heterozygotes survived ~1 year with "cardiac histopathology and dysfunction" resembling human disease, and importantly "Cardiac dysfunction preceded histopathologic changes, and myocyte disarray, hypertrophy, and fibrosis increased with age," with more severe disease in young males than females. *Directly illustrates the disarray-and-fibrosis pathology the CMH21 family lacked.*
- ***Mybpc3*-targeted mice** (knockout and knock-in): model haploinsufficiency/truncation biology; the platform for *MYBPC3* gene-therapy proof-of-concept.
- **Patient-derived hiPSC-cardiomyocytes and engineered heart tissue**: the leading in-vitro system for sarcomeric HCM hypercontractility, Ca²⁺ handling, and energetics; **could in principle be derived from CMH21 family members** and is a sensible `proposed_experiments` item alongside WGS reanalysis.
- **Zebrafish and *Drosophila*** cardiac models: used for candidate-gene functional triage — the natural downstream assay if a candidate emerges from the 7p12.1–q21 interval.

**Model limitations relevant here:** every existing HCM model is sarcomere-driven and reproduces the disarray/fibrosis phenotype that the CMH21 kindred conspicuously lacked. None models a sarcomere-negative, disarray-negative hypertrophy-to-dilation trajectory. Per dismech convention, if you curate model-organism content on this entry, pair it with a `discussions` entry of `kind: HUMAN_MODEL_MISMATCH` rather than plain `KNOWLEDGE_GAP` — evidence exists in models, but its fidelity to *this* disease is precisely the open question.

---

## Curation Recommendations for the dismech Entry

1. **Frame the entry honestly as a mapped-but-unsolved locus.** The `description` should lead with "linkage locus, causal gene unidentified," not with generic HCM prose.
2. **Do not populate `genetic:` with any gene.** No `gene_term`, no HGNC ID. Put the locus in the description and, if desired, a locus-level `Inheritance` block bound to HP:0000006.
3. **Curate the two negative findings as first-class evidence** — sarcomere-gene-negative, and disarray/fibrosis-negative. Both have clean verbatim snippets in `references_cache/PMID_16651466.md`.
4. **Handle the HP:0031318 (Myofiber disarray) conflict explicitly** (§3) — this is a genuine OMIM-vs-primary-source discrepancy and a good demonstration of the `supports: REFUTE` machinery.
5. **Add a `discussions` entry, `kind: KNOWLEDGE_GAP`, `attaches_to` the locus node**, with `proposed_experiments`: (a) WGS of surviving affected/unaffected family members restricted to the 27 Mb linkage interval, prioritizing non-coding and structural variation invisible to 2006 Sanger sequencing; (b) RNA-seq / long-read sequencing of available myocardium or hiPSC-CMs to catch splice-altering and regulatory lesions; (c) re-contact and re-phenotyping of the kindred with CMR/LGE.
6. **Consider `conforms_to: cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling`** — defensible, adds structure, asserts nothing unknown.
7. **`prevalence`:** use `measure_type: CASES_IN_LITERATURE`, `prevalence_class: UNKNOWN` (§9). Do not import HCM's 1-in-500 figure as CMH21's prevalence.
8. **Reference hygiene:** only PMID:16651466 and PMID:21965549 are currently in `references_cache/` on this branch and have been read verbatim by me. **Every other PMID in this report was retrieved through a summarizing web fetch and its snippets must be re-verified** — run `just fetch-reference PMID:<id>` and then `just validate-references kb/disorders/Hypertrophic_Cardiomyopathy_21.yaml` before committing any quote. Candidate references to fetch: 7641357, 25814232, 28408708, 28912181, 30297972, 33495596, 33495597, 38718139, 37622657, 32871100, 38739079, 38853772, 24126876, 20301725, 8614836, 16236761, 17521870.
9. **Full-text gap:** the *Circulation* full text (per-individual ages, wall thicknesses, LV dimensions, pedigree figure, marker map, LOD table) is behind HTTP 403 for automated access. If you need pedigree-level detail — particularly the age-of-onset data that would let you justify HP:0003581 with evidence rather than inference — retrieve the PDF via UNC institutional access.

---

## Sources

- [Novel locus for an inherited cardiomyopathy maps to chromosome 7 — PubMed (PMID:16651466)](https://pubmed.ncbi.nlm.nih.gov/16651466/) · [Circulation full text](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.106.615658)
- [OMIM Entry #614676 — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 21; CMH21](https://omim.org/entry/614676)
- [MedGen: Hypertrophic cardiomyopathy 21 (C3553442, UID 766356)](https://www.ncbi.nlm.nih.gov/medgen/766356)
- [NCBI Gene: CMH21 (Gene ID 100909387)](https://www.ncbi.nlm.nih.gov/gene/100909387)
- [MalaCards: Cardiomyopathy, Familial Hypertrophic, 21](https://www.malacards.org/card/cardiomyopathy_familial_hypertrophic_21)
- Local `sqlite:obo:mondo`, `:hp`, `:go`, `:cl`, `:uberon`, `:ncit`, `:chebi` via OAK (all ontology IDs/labels in this report verified 2026-08-01)
- [Homozygosity mapping and exome sequencing reveal GATAD1 mutation in autosomal recessive dilated cardiomyopathy (PMID:21965549)](https://pubmed.ncbi.nlm.nih.gov/21965549/) · [OMIM *614518 GATAD1](https://omim.org/entry/614518)
- [Europe PMC citation list for PMID:16651466](https://www.ebi.ac.uk/europepmc/webservices/rest/MED/16651466/citations?format=json)
- [Prevalence of hypertrophic cardiomyopathy in a general population of young adults — CARDIA (PMID:7641357)](https://pubmed.ncbi.nlm.nih.gov/7641357/)
- [New perspectives on the prevalence of hypertrophic cardiomyopathy (PMID:25814232)](https://pubmed.ncbi.nlm.nih.gov/25814232/)
- [Nonfamilial Hypertrophic Cardiomyopathy: Prevalence, Natural History, and Clinical Implications (PMID:28408708)](https://pubmed.ncbi.nlm.nih.gov/28408708/)
- [Hypertrophic Cardiomyopathy: Genetics, Pathogenesis, Clinical Manifestations, Diagnosis, and Therapy (PMID:28912181)](https://pubmed.ncbi.nlm.nih.gov/28912181/)
- [Genotype and Lifetime Burden of Disease in HCM — SHaRe registry (PMID:30297972)](https://pubmed.ncbi.nlm.nih.gov/30297972/)
- [Common genetic variants and modifiable risk factors underpin HCM susceptibility and expressivity (PMID:33495597)](https://pubmed.ncbi.nlm.nih.gov/33495597/)
- [Shared genetic pathways contribute to risk of hypertrophic and dilated cardiomyopathies (PMID:33495596)](https://pubmed.ncbi.nlm.nih.gov/33495596/)
- [2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of HCM (PMID:38718139)](https://pubmed.ncbi.nlm.nih.gov/38718139/)
- [2023 ESC Guidelines for the management of cardiomyopathies (PMID:37622657)](https://pubmed.ncbi.nlm.nih.gov/37622657/)
- [EXPLORER-HCM: Mavacamten for symptomatic obstructive HCM (PMID:32871100)](https://pubmed.ncbi.nlm.nih.gov/32871100/)
- [SEQUOIA-HCM: Aficamten for Symptomatic Obstructive HCM (PMID:38739079)](https://pubmed.ncbi.nlm.nih.gov/38739079/)
- [HCM Risk-SCD prediction model (PMID:24126876)](https://pubmed.ncbi.nlm.nih.gov/24126876/)
- [Nonsyndromic Hypertrophic Cardiomyopathy Overview — GeneReviews (PMID:20301725)](https://pubmed.ncbi.nlm.nih.gov/20301725/)
- [Divergent Metabolic Remodeling in Genotype-Positive and Genotype-Negative HCM (PMID:38853772)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11188634/)
- [A mouse model of familial hypertrophic cardiomyopathy (PMID:8614836)](https://pubmed.ncbi.nlm.nih.gov/8614836/)
- [A cardiac myosin binding protein C mutation in the Maine Coon cat (PMID:16236761)](https://pubmed.ncbi.nlm.nih.gov/16236761/) · [Ragdoll MYBPC3 mutation (PMID:17521870)](https://pubmed.ncbi.nlm.nih.gov/17521870/)
- [Genotype-Negative Patients With Familial HCM: Traveling to the "Middle Earth" — JACC: Advances 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12103094/)
- [Familial hypertrophic cardiomyopathy — MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/familial-hypertrophic-cardiomyopathy/)