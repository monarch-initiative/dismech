---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-02T22:40:31.093196'
end_time: '2026-04-02T23:00:18.058977'
duration_seconds: 1186.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spondylodysplastic Ehlers-Danlos Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Spondylodysplastic Ehlers-Danlos Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Spondylodysplastic Ehlers-Danlos Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Spondylodysplastic Ehlers-Danlos Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Spondylodysplastic Ehlers-Danlos Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Comprehensive Research Report: Pathophysiology of Spondylodysplastic Ehlers–Danlos Syndrome (spEDS)

### Executive summary
Spondylodysplastic Ehlers–Danlos syndrome (spEDS) is an autosomal recessive, ultra-rare monogenic EDS subtype defined by a core triad of **short stature**, **muscle hypotonia**, and **skeletal dysplasia-like features**, together with connective-tissue manifestations such as **joint hypermobility** and **skin hyperextensibility**. Contemporary reviews estimate prevalence **<1:1,000,000** and note **>100 reported individuals**. (dijk2024clinicaldiagnosisof pages 4-6, zschocke2024geneticdiagnosisof pages 5-6)

Mechanistically, spEDS comprises at least two convergent molecular “axes”:
1) **Proteoglycan linker-region (GAG) biosynthesis defects (“linkeropathies”)** due to biallelic pathogenic variants in **B4GALT7** or **B3GALT6** (and, in some framings, closely overlapping phenotypes from other linker enzymes such as **B3GAT3**). These disrupt formation of heparan sulfate (HS), chondroitin sulfate (CS), and dermatan sulfate (DS) proteoglycans, altering extracellular matrix (ECM) organization, collagen fibrillogenesis, and tissue biomechanics. (caraffi2019severeperipheraljoint pages 1-3, damme2018biallelicb3galt6mutations pages 1-4, damme2018biallelicb3galt6mutations pages 10-13)
2) **Secretory-pathway metal homeostasis / collagen post-translational modification defects** caused by biallelic pathogenic variants in **SLC39A13 (ZIP13)**. A major 2024 advance is evidence that ZIP13’s primary physiological role is **ER/Golgi iron transport**, needed to supply Fe2+ cofactors to ER-resident lysyl/prolyl hydroxylases for collagen hydroxylation; ZIP13 loss leads to reduced collagen hydroxylation and provides a direct mechanistic bridge from transporter dysfunction to connective-tissue pathology. (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 8-9)

---

## Disease identifiers and nosology
- **Disease name:** Spondylodysplastic Ehlers–Danlos syndrome (spEDS)
- **MONDO:** **MONDO_0034021** (Open Targets disease identifier surfaced in this run; used for disease–target associations). (diana2025b3galt6mutationslead pages 1-2)
- **OMIM (examples from spEDS-related subtypes):**
  - **B4GALT7-related spEDS:** EDS, spondylodysplastic type (OMIM **#130070**) (caraffi2019severeperipheraljoint pages 1-3, doolan2023extracutaneousfeaturesand pages 1-2)
  - **B3GALT6-related severe EDS-like disorder:** OMIM **#615349** (caraffi2019severeperipheraljoint pages 1-3, doolan2023extracutaneousfeaturesand pages 1-2)
  - **SLC39A13-related spEDS:** referred to as **EDSSPD3, OMIM 612350** in 2024 mechanistic work. (shoji2024possibleinvolvementof pages 1-2)

### Definition and diagnostic criteria (2017 EDS classification-derived)
A widely used clinical suspicion framework requires two major criteria (short stature; muscle hypotonia) plus characteristic radiographic changes and additional minor criteria, followed by confirmatory molecular testing. (ritelli2017expandingtheclinical pages 1-2)

Two extracted table images from Ritelli et al. (2017) provide a compact representation of these criteria and gene-specific feature sets (Tables 1–2). (ritelli2017expandingtheclinical media 36a1859a, ritelli2017expandingtheclinical media 0d274780)

---

## 1. Core pathophysiology

### 1.1 Linkeropathy axis (B4GALT7, B3GALT6): disrupted GAG–proteoglycan synthesis and ECM biomechanics
Proteoglycans (PGs) carry glycosaminoglycan (GAG) chains attached to core proteins via a **conserved tetrasaccharide linker**. B4GALT7 and B3GALT6 encode two sequential Golgi galactosyltransferases required to build this linker; loss-of-function variants impair HS/CS/DS assembly and lead to a combined connective-tissue + skeletal phenotype (“linkeropathy”). (caraffi2019severeperipheraljoint pages 1-3, damme2018biallelicb3galt6mutations pages 1-4)

Mechanistic consequences documented in patient-derived fibroblasts and model organisms include:
- **Reduced total GAG synthesis** and reduced HS/CS/DS production, including impaired conversion of decorin core protein into mature GAG-bearing proteoglycan. (delbaere2020hypomorphiczebrafishmodels pages 1-5, damme2018biallelicb3galt6mutations pages 10-13)
- **Abnormal collagen fibril architecture** (e.g., altered interfibrillar spacing and fibril variability), consistent with proteoglycan-mediated control of collagen fibrillogenesis and tissue mechanics. (damme2018biallelicb3galt6mutations pages 10-13, damme2018biallelicb3galt6mutations pages 13-15)
- **Impaired cell migration/wound closure** in B3GALT6 patient fibroblasts, linking ECM defects to cellular-level functional phenotypes. (damme2018biallelicb3galt6mutations pages 10-13)

### 1.2 ZIP13 axis (SLC39A13): secretory-pathway iron handling, collagen hydroxylation, and cell fate programs
ZIP13 has historically been described as a zinc transporter, with spEDS linked to altered Zn2+ handling and downstream signaling (e.g., BMP/TGF-β-SMAD perturbation) and collagen modification defects. (malfait2020theehlers–danlossyndromes pages 11-12)

A key 2024 development is direct mechanistic evidence in mammalian systems:
- ZIP13 loss “**led to a decreased iron content in the ER/Golgi, resulting in the loss of iron cofactor for ER-resident lysine and proline hydroxylation enzymes**,” and the “**primary physiological function of ZIP13 is iron instead of zinc**.” (li2024mammalianslc39a13promotes pages 8-9)
- Experimentally, restoring iron to the secretory pathway improved collagen hydroxylation, supporting a causal chain: **ZIP13 loss → ER/Golgi iron deficiency → reduced collagen hydroxylation → connective tissue fragility/dysplasia**. (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 7-8)

In addition, 2024 iPSC/myoblast work provides cellular-mechanistic granularity:
- A pathogenic ZIP13 variant (G64D) undergoes **VCP-linked ubiquitin–proteasome degradation**, producing functional ZIP13 deficiency. (shoji2024possibleinvolvementof pages 1-2)
- ZIP13 is induced during myogenesis; knockdown disrupts myotube formation, and patient iPSC-derived myocytes show incomplete differentiation that is rescued by gene correction—supporting a plausible mechanism for hypotonia and muscle involvement. (shoji2024possibleinvolvementof pages 1-2)

---

## 2. Key molecular players

### 2.1 Genes/Proteins (HGNC symbols)
Core spEDS genes consistently cited in 2017–2024 clinical literature:
- **B4GALT7** (galactosyltransferase I; Golgi) (caraffi2019severeperipheraljoint pages 1-3, dijk2024clinicaldiagnosisof pages 4-6)
- **B3GALT6** (galactosyltransferase II; Golgi) (damme2018biallelicb3galt6mutations pages 1-4, damme2018biallelicb3galt6mutations pages 10-13)
- **SLC39A13 (ZIP13)** (ER/Golgi metal transporter; iron transport strongly supported by 2024 data) (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 8-9)

Closely related “linkeropathy continuum” gene (overlap phenotypes sometimes grouped with spEDS-like presentations):
- **B3GAT3** (glucuronyltransferase; completes linker) (zschocke2024geneticdiagnosisof pages 5-6)

### 2.2 Chemical entities (ChEBI-style)
Evidence-supported relevant chemicals/ions and substrates:
- **Iron (Fe2+)** as ER/Golgi cofactor supply determinant for collagen hydroxylation enzymes (li2024mammalianslc39a13promotes pages 8-9, li2024mammalianslc39a13promotes pages 4-5)
- **Zinc (Zn2+)** historically implicated in ZIP13 biology and collagen processing hypotheses (malfait2020theehlers–danlossyndromes pages 11-12, zschocke2024geneticdiagnosisof pages 5-6)
- **Linker monosaccharides:** xylose, galactose residues, glucuronic acid as part of the GAG linker assembly (damme2018biallelicb3galt6mutations pages 1-4, delbaere2020hypomorphiczebrafishmodels pages 1-5)
- **Experimental xyloside/fluorogenic substrates** used to assay GAG priming (e.g., 4-MUX xyloside; Gal-Xyl(2P)-OMN), useful as mechanistic/assay anchors in research contexts (damme2018biallelicb3galt6mutations pages 10-13, damme2018biallelicb3galt6mutations pages 13-15)

### 2.3 Cell types (CL-style)
- **Fibroblasts**: primary patient cells used for mechanistic evaluation of GAG synthesis and ECM defects (damme2018biallelicb3galt6mutations pages 10-13)
- **Chondrocytes** (and cartilage lineage): implicated by zebrafish phenocopy studies showing loss of chondrocyte organization and cartilage patterning (delbaere2020hypomorphiczebrafishmodels pages 1-5)
- **Myoblasts/myocytes**: ZIP13-dependent myogenic differentiation shown in C2C12 and patient iPSC-derived myocytes (shoji2024possibleinvolvementof pages 1-2)

### 2.4 Anatomical locations (UBERON-style)
Most consistently involved structures:
- **Skin/dermis and extracellular matrix** (hyperextensible/doughy/translucent skin; collagen fibril disorganization) (damme2018biallelicb3galt6mutations pages 10-13, dijk2024clinicaldiagnosisof pages 4-6)
- **Bone and cartilage** (skeletal dysplasia-like features; osteopenia/fractures; cartilage patterning defects in models) (zschocke2024geneticdiagnosisof pages 5-6, delbaere2020hypomorphiczebrafishmodels pages 1-5)
- **Spine/vertebrae** (e.g., platyspondyly; cervical spine instability in some B3GALT6 cases) (agrawal2023acaseof pages 1-2, damme2018biallelicb3galt6mutations pages 1-4)
- **Eye** (bluish sclera, megalocornea/myopia/keratoconus reported in SLC39A13 spEDS) (agrawal2023acaseof pages 1-1, agrawal2023acaseof pages 3-4)
- Additional metal-homeostasis anatomy in Zip13 mouse models: **liver, spleen macrophages, renal tubules** with iron deposition patterns (mechanistic, not necessarily clinical hallmark). (li2024mammalianslc39a13promotes pages 8-9)

---

## 3. Dysregulated pathways and cellular processes

### 3.1 Dysregulated molecular pathways
- **GAG linker assembly / proteoglycan biosynthesis** (Golgi): defective formation of the tetrasaccharide primer disrupts HS/CS/DS proteoglycans. (damme2018biallelicb3galt6mutations pages 1-4, caraffi2019severeperipheraljoint pages 1-3)
- **ECM assembly and collagen fibrillogenesis:** proteoglycan abnormalities (notably decorin glycanation changes) associate with abnormal dermal collagen fibrils and altered biomechanical properties. (damme2018biallelicb3galt6mutations pages 13-15, damme2018biallelicb3galt6mutations pages 10-13)
- **Secretory-pathway iron transport → collagen hydroxylation:** ZIP13-dependent iron supply to ER/Golgi supports iron-dependent lysyl/prolyl hydroxylases; depletion reduces collagen hydroxylation. (li2024mammalianslc39a13promotes pages 8-9, li2024mammalianslc39a13promotes pages 4-5)
- **Proteostasis and protein degradation:** VCP-linked ubiquitin–proteasome degradation of pathogenic ZIP13 (G64D) (shoji2024possibleinvolvementof pages 1-2)
- **Myogenic differentiation programs:** ZIP13 required for myotube differentiation and iPSC-derived myocyte maturation (shoji2024possibleinvolvementof pages 1-2)

### 3.2 Cellular components (GO-CC-style)
- **Golgi apparatus** (linker glycosyltransferases B4GALT7/B3GALT6; GAG assembly) (damme2018biallelicb3galt6mutations pages 1-4, delbaere2020hypomorphiczebrafishmodels pages 1-5)
- **ER/Golgi secretory pathway** (ZIP13 localization and iron transport; collagen hydroxylation enzymes) (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 8-9)
- **Extracellular matrix / collagen fibrils / elastic fibers** (structural output of the dysregulated pathways) (damme2018biallelicb3galt6mutations pages 10-13)
- **Cell surface** (HS distribution changes; cell–matrix signaling platform) (damme2018biallelicb3galt6mutations pages 10-13)
- **Mitochondria/lysosomes** (secondary iron compartment changes after ZIP13 loss) (li2024mammalianslc39a13promotes pages 1-2)

---

## 4. Disease progression model (sequence of events)
A gene-to-phenotype causal chain consistent with available evidence:
1) **Biallelic pathogenic variants** in B4GALT7/B3GALT6 (linker enzymes) or SLC39A13 (ZIP13 transporter). (ritelli2017expandingtheclinical pages 1-2, dijk2024clinicaldiagnosisof pages 4-6)
2) **Early cellular biochemical deficits**:
   - Linkeropathies: impaired linker assembly → reduced/aberrant HS/CS/DS and proteoglycan glycanation → altered ECM assembly and cell migration. (damme2018biallelicb3galt6mutations pages 10-13, delbaere2020hypomorphiczebrafishmodels pages 1-5)
   - ZIP13: reduced ER/Golgi iron → reduced collagen hydroxylation; plus proteasomal degradation of pathogenic ZIP13 variants and myogenic differentiation defects. (li2024mammalianslc39a13promotes pages 8-9, shoji2024possibleinvolvementof pages 1-2)
3) **Tissue-level ECM consequences**: abnormal collagen fibril organization and connective-tissue biomechanics; impaired skeletal growth plate/cartilage organization in developmental contexts. (damme2018biallelicb3galt6mutations pages 13-15, delbaere2020hypomorphiczebrafishmodels pages 1-5)
4) **Clinical manifestations** become apparent in childhood: short stature and bowed limbs; hypotonia/motor delay; joint hypermobility and skin signs; potential complications (fractures, spine instability, rare vascular events). (dijk2024clinicaldiagnosisof pages 4-6, damme2018biallelicb3galt6mutations pages 1-4)

---

## 5. Phenotypic manifestations and mechanistic links (HPO-oriented)
Common phenotypes highlighted in recent diagnostic reviews:
- **Short stature** and **progressive growth delay** (central diagnostic hallmarks; reflect impaired skeletal development/ECM in growth plate and bone). (zschocke2024geneticdiagnosisof pages 5-6, dijk2024clinicaldiagnosisof pages 4-6)
- **Muscle hypotonia** (supported by ZIP13 myogenic differentiation defects; and general connective-tissue/musculoskeletal involvement). (shoji2024possibleinvolvementof pages 1-2, zschocke2024geneticdiagnosisof pages 5-6)
- **Limb bowing** and skeletal dysplasia-like radiographic features (developmental cartilage/bone ECM defects; model phenocopies in B4galt7 zebrafish). (dijk2024clinicaldiagnosisof pages 4-6, delbaere2020hypomorphiczebrafishmodels pages 1-5)
- **Joint hypermobility** (96% in one systematic review’s spEDS cases: 24/25) (doolan2023extracutaneousfeaturesand pages 1-2)
- **Skin hyperextensibility / doughy thin translucent skin** (connective tissue ECM output of proteoglycan/collagen processing defects). (dijk2024clinicaldiagnosisof pages 4-6, damme2018biallelicb3galt6mutations pages 10-13)

Additional phenotypes reported (variable by gene):
- **Osteopenia / recurrent fractures** and sometimes severe osteoporosis (GAG/ECM defects; reported in spEDS descriptions and B3GALT6 case series). (zschocke2024geneticdiagnosisof pages 5-6, damme2018biallelicb3galt6mutations pages 10-13)
- **Ocular findings** such as bluish sclera, megalocornea, myopia/keratoconus (SLC39A13 subtype). (agrawal2023acaseof pages 1-1, agrawal2023acaseof pages 3-4)
- **Aortic dilation/aneurysm** and other potentially life-threatening complications in some B3GALT6 cohorts (ECM integrity effects). (damme2018biallelicb3galt6mutations pages 1-4, damme2018biallelicb3galt6mutations pages 10-13)

---

## 6. Recent developments (prioritizing 2023–2024)

### 6.1 2024: ZIP13 is an ER/Golgi iron transporter linking metal homeostasis to collagen hydroxylation
A major mechanistic advance is mammalian evidence that ZIP13’s primary physiological function is iron trafficking to the secretory pathway, and that ZIP13 loss reduces ER/Golgi iron and collagen hydroxylation (a direct molecular path to ECM defects). (li2024mammalianslc39a13promotes pages 8-9, li2024mammalianslc39a13promotes pages 4-5)
- Publication: **Nature Communications**, Dec 2024. DOI/URL: https://doi.org/10.1038/s41467-024-55149-2 (li2024mammalianslc39a13promotes pages 4-5)
- Key quoted statements:
  - “the primary physiological function of ZIP13 is iron instead of zinc” (li2024mammalianslc39a13promotes pages 8-9)
  - ZIP13 loss “led to a decreased iron content in the ER/Golgi, resulting in the loss of iron cofactor for ER-resident lysine and proline hydroxylation enzymes.” (li2024mammalianslc39a13promotes pages 8-9)

### 6.2 2024: Patient iPSC-based mechanistic modeling of ZIP13-related spEDS features
- Publication: **Scientific Reports**, Apr 2024. DOI/URL: https://doi.org/10.1038/s41598-024-56912-7 (shoji2024possibleinvolvementof pages 1-2)
- Key advances include iPSC-derived myocyte phenotypes, gene-editing rescue, and the mechanism of pathogenic ZIP13 protein degradation via VCP-linked ubiquitin–proteasome pathways. (shoji2024possibleinvolvementof pages 1-2)

### 6.3 2024: Expert diagnostic syntheses for monogenic EDS
Two 2024 expert reviews provide updated disease framing:
- **Clinical diagnosis of monogenic EDS** (Nov 2024) includes prevalence estimate **<1:1,000,000** and key diagnostic features. DOI/URL: https://doi.org/10.1515/medgen-2024-2060 (dijk2024clinicaldiagnosisof pages 4-6)
- **Genetic diagnosis of EDS** (Nov 2024) describes spEDS features, autosomal recessive inheritance, and notes **>100 individuals reported**, while emphasizing core etiologic mechanisms (GAG linker enzymes and a zinc transporter phenotype). DOI/URL: https://doi.org/10.1515/medgen-2024-2061 (zschocke2024geneticdiagnosisof pages 5-6)

### 6.4 2023: Systematic review evidence on extracutaneous features/complications
A 2023 systematic review (n=839 EDS cases) reported **joint hypermobility prevalence in spEDS of 96.0% (24/25)**. DOI/URL: https://doi.org/10.3389/fmed.2023.1053466 (doolan2023extracutaneousfeaturesand pages 1-2)

---

## 7. Current applications and real-world implementations

### 7.1 Diagnostics
- **Gene panel testing with massively parallel sequencing** is described as the gold standard for confirming monogenic EDS types in contemporary expert reviews. (zschocke2024geneticdiagnosisof pages 5-6)
- For spEDS, clinical suspicion is guided by major/minor criteria and gene-specific features; **molecular confirmation is required** for definitive diagnosis. (ritelli2017expandingtheclinical pages 1-2)
- Case literature explicitly notes diagnosis via **next-generation sequencing** and emphasizes that short stature differentiates spEDS from other EDS types. (agrawal2023acaseof pages 3-4)

### 7.2 Management and surveillance (supportive care)
Directly stated management elements from a genetically confirmed SLC39A13 case report include:
- Multidisciplinary follow-up with **regular screening of developmental milestones, vision, and growth**, and “**Regular surveillance of vision and growth is required**,” including ophthalmologic surveillance. (agrawal2023acaseof pages 3-4)
- Vascular fragility is described as not a consistent feature in spEDS relative to other EDS types, but rare severe events have been reported, supporting clinical vigilance. (agrawal2023acaseof pages 3-4)

### 7.3 Ongoing clinical research / trials
A clinicaltrials.gov-style search using spEDS terms and core genes did not identify spEDS-specific interventional trials in this run (no relevant trials returned). (clinical trials search executed; no relevant trials in state)

---

## 8. Evidence-linked ontology annotations (for knowledge base ingestion)

### 8.1 Biological processes (GO-style phrases; mechanistically supported)
- glycosaminoglycan biosynthetic process; proteoglycan metabolic process; heparan sulfate biosynthesis; chondroitin/dermatan sulfate biosynthesis (damme2018biallelicb3galt6mutations pages 1-4, delbaere2020hypomorphiczebrafishmodels pages 1-5)
- extracellular matrix organization; collagen fibril organization/collagen fibrillogenesis (damme2018biallelicb3galt6mutations pages 10-13, damme2018biallelicb3galt6mutations pages 13-15)
- cell migration / wound healing (fibroblast scratch closure deficits) (damme2018biallelicb3galt6mutations pages 10-13)
- intracellular iron ion homeostasis; ER/Golgi iron transport (li2024mammalianslc39a13promotes pages 8-9, li2024mammalianslc39a13promotes pages 1-2)
- collagen hydroxylation / collagen post-translational modification (lysyl/prolyl hydroxylases) (li2024mammalianslc39a13promotes pages 8-9, li2024mammalianslc39a13promotes pages 4-5)
- myogenic differentiation (shoji2024possibleinvolvementof pages 1-2)

### 8.2 Cellular components (GO-CC-style phrases)
- Golgi apparatus (linker glycosyltransferases; GAG synthesis) (damme2018biallelicb3galt6mutations pages 1-4, delbaere2020hypomorphiczebrafishmodels pages 1-5)
- ER/Golgi secretory pathway (ZIP13 localization and iron transport) (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 8-9)
- extracellular matrix; collagen fibril; elastic fiber; cell surface proteoglycans (damme2018biallelicb3galt6mutations pages 10-13)

### 8.3 Cell types (CL-style)
- fibroblast (patient fibroblast biochemical/structural assays) (damme2018biallelicb3galt6mutations pages 10-13)
- chondrocyte lineage (cartilage patterning and organization changes in models) (delbaere2020hypomorphiczebrafishmodels pages 1-5)
- myoblast / skeletal muscle cell (ZIP13-dependent differentiation) (shoji2024possibleinvolvementof pages 1-2)

### 8.4 Anatomical entities (UBERON-style)
- skin/dermis; extracellular matrix (dijk2024clinicaldiagnosisof pages 4-6, damme2018biallelicb3galt6mutations pages 10-13)
- bone; cartilage; vertebral column/cervical spine; long bone metaphyses (damme2018biallelicb3galt6mutations pages 10-13, delbaere2020hypomorphiczebrafishmodels pages 1-5)
- eye (sclera/cornea-related phenotypes) (agrawal2023acaseof pages 1-1, agrawal2023acaseof pages 3-4)
- aorta (thoracic aorta aneurysm/dilation in some B3GALT6 cases) (damme2018biallelicb3galt6mutations pages 10-13)

### 8.5 Chemical entities (ChEBI-style)
- iron(II) / iron (Fe2+); zinc(II) / zinc (Zn2+) (li2024mammalianslc39a13promotes pages 8-9, malfait2020theehlers–danlossyndromes pages 11-12)
- glycosaminoglycans (heparan sulfate; chondroitin sulfate; dermatan sulfate) (damme2018biallelicb3galt6mutations pages 1-4, damme2018biallelicb3galt6mutations pages 10-13)

---

## Consolidated gene–mechanism–phenotype table
| Gene (HGNC symbol) | Protein/function | Inheritance | Key molecular mechanism | Key affected pathways/bioprocesses (GO-style phrases) | Primary affected cell types/tissues | Representative phenotypes (HPO-style phrases) | Key recent evidence (2023-2024) with DOI/URL | Key foundational evidence with DOI/URL | Notes/biomarkers/therapeutic implications |
|---|---|---|---|---|---|---|---|---|---|
| **B4GALT7** | β4GalT7 / galactosyltransferase I; Golgi glycosyltransferase adding the **first galactose** to xylose in the proteoglycan tetrasaccharide linker | Autosomal recessive | Defective linker-region assembly impairs initiation of HS/CS/DS GAG chains; reduced sulfated GAGs and incomplete decorin proteoglycan maturation disrupt ECM organization, cartilage patterning, and musculoskeletal development (delbaere2020hypomorphiczebrafishmodels pages 1-5, caraffi2019severeperipheraljoint pages 1-3) | glycosaminoglycan biosynthetic process; proteoglycan metabolic process; extracellular matrix organization; collagen fibril organization; skeletal system development; cartilage development (delbaere2020hypomorphiczebrafishmodels pages 1-5, caraffi2019severeperipheraljoint pages 1-3) | Fibroblasts/dermis; chondrocytes/cartilage; bone; muscle/connective tissue (delbaere2020hypomorphiczebrafishmodels pages 1-5, caraffi2019severeperipheraljoint pages 1-3, dijk2024clinicaldiagnosisof pages 4-6) | Short stature; muscle hypotonia; bowing of limbs; joint hypermobility; skin hyperextensibility; doughy/thin translucent skin; skeletal dysplasia-like presentation (dijk2024clinicaldiagnosisof pages 4-6, doolan2023extracutaneousfeaturesand pages 1-2) | Dijk et al. 2024, *Clinical diagnosis of the monogenic EDS* DOI: 10.1515/medgen-2024-2060 URL: https://doi.org/10.1515/medgen-2024-2060 (dijk2024clinicaldiagnosisof pages 4-6); Zschocke et al. 2024, *Genetic diagnosis of the EDS* DOI: 10.1515/medgen-2024-2061 URL: https://doi.org/10.1515/medgen-2024-2061 (zschocke2024geneticdiagnosisof pages 5-6) | Delbaere et al. 2020, *Hypomorphic zebrafish models mimic the musculoskeletal phenotype of β4galt7-deficient EDS* DOI: 10.1016/j.matbio.2019.12.002 URL: https://doi.org/10.1016/j.matbio.2019.12.002 (delbaere2020hypomorphiczebrafishmodels pages 1-5); Ritelli et al. 2017 DOI: 10.1186/s13023-017-0704-3 URL: https://doi.org/10.1186/s13023-017-0704-3 (ritelli2017expandingtheclinical pages 1-2) | Diagnostic clue: linkeropathy/spEDS phenotype with major criteria short stature + hypotonia; molecular confirmation by sequencing is required. No disease-specific therapy identified; management is supportive and surveillance-based (ritelli2017expandingtheclinical pages 1-2, dijk2024clinicaldiagnosisof pages 4-6) |
| **B3GALT6** | β3GalT6 / galactosyltransferase II; Golgi glycosyltransferase adding the **second galactose** in the linker region | Autosomal recessive | Loss of galactosyltransferase activity causes strongly reduced GAG priming and ~70–80% lower total GAG production in patient fibroblasts, markedly reduced decorin glycanation, reduced cell-surface HS, delayed wound closure/cell migration, abnormal collagen fibril spacing/diameter, fragmented elastic fibers, and compromised tissue biomechanics; partial compensation can occur via B3GAT3/GlcAT-I forming an alternative trisaccharide linker (damme2018biallelicb3galt6mutations pages 13-15, damme2018biallelicb3galt6mutations pages 10-13, diana2025b3galt6mutationslead pages 1-2, diana2025b3galt6mutationslead pages 12-14) | glycosaminoglycan biosynthetic process; heparan sulfate proteoglycan biosynthetic process; chondroitin sulfate/dermatan sulfate biosynthetic process; collagen fibril organization; extracellular matrix organization; wound healing/cell migration; connective tissue development (damme2018biallelicb3galt6mutations pages 13-15, damme2018biallelicb3galt6mutations pages 10-13, diana2025b3galt6mutationslead pages 1-2, diana2025b3galt6mutationslead pages 12-14) | Dermal fibroblasts; skin ECM; tendon/ligament/connective tissue; bone and cartilage (damme2018biallelicb3galt6mutations pages 13-15, damme2018biallelicb3galt6mutations pages 10-13, dijk2024clinicaldiagnosisof pages 4-6) | Short stature; muscle hypotonia; severe distal/peripheral joint laxity; osteopenia/recurrent fractures; cervical spine instability; respiratory insufficiency; possible aortic dilatation/aneurysm; skin hyperextensibility/doughy skin (damme2018biallelicb3galt6mutations pages 1-4, caraffi2019severeperipheraljoint pages 1-3, dijk2024clinicaldiagnosisof pages 4-6) | Shoji et al. 2024 is gene-specific to SLC39A13, not B3GALT6; for B3GALT6 recent mechanistic context is summarized in 2024 diagnostic reviews: Dijk et al. 2024 DOI: 10.1515/medgen-2024-2060 URL: https://doi.org/10.1515/medgen-2024-2060 (dijk2024clinicaldiagnosisof pages 4-6); Zschocke et al. 2024 DOI: 10.1515/medgen-2024-2061 URL: https://doi.org/10.1515/medgen-2024-2061 (zschocke2024geneticdiagnosisof pages 5-6) | Van Damme et al. 2018, *Biallelic B3GALT6 mutations cause spondylodysplastic EDS* DOI: 10.1093/hmg/ddy234 URL: https://doi.org/10.1093/hmg/ddy234 (damme2018biallelicb3galt6mutations pages 13-15, damme2018biallelicb3galt6mutations pages 1-4, damme2018biallelicb3galt6mutations pages 10-13); Caraffi et al. 2019 DOI: 10.3390/genes10100799 URL: https://doi.org/10.3390/genes10100799 (caraffi2019severeperipheraljoint pages 1-3) | Potential biomarker concepts: abnormal decorin glycanation, reduced HS staining, altered collagen fibril ultrastructure. Therapeutic implication remains supportive; 2025 mechanistic work suggests collagen XII glycosylation/biomechanics as translational readouts, but not yet clinical standard (damme2018biallelicb3galt6mutations pages 10-13, diana2025b3galt6mutationslead pages 1-2, diana2025b3galt6mutationslead pages 12-14) |
| **SLC39A13** | ZIP13 / solute carrier family 39 member 13; ER/Golgi-localized metal transporter historically linked to zinc homeostasis, now strongly supported as a secretory-pathway **iron transporter** | Autosomal recessive | ZIP13 deficiency causes ER/Golgi iron deficiency, depriving lysyl/prolyl hydroxylases of Fe2+ and producing reduced collagen hydroxylation/under-crosslinking; older models also implicated altered Zn2+ homeostasis, ER stress, and BMP/TGF-β-SMAD dysregulation. The recurrent pathogenic p.G64D protein undergoes VCP-linked ubiquitin-proteasome degradation, producing functional ZIP13 deficiency. ZIP13 loss additionally impairs myogenic differentiation in C2C12 and patient-iPSC-derived myocytes, reversible by gene correction (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 3-4, li2024mammalianslc39a13promotes pages 8-9, li2024mammalianslc39a13promotes pages 7-8, malfait2020theehlers–danlossyndromes pages 11-12, shoji2024possibleinvolvementof pages 1-2) | intracellular iron ion homeostasis; ER/Golgi metal ion transport; collagen metabolic process; collagen hydroxylation/cross-linking; extracellular matrix organization; BMP signaling/TGF-β signaling; myoblast differentiation; skeletal muscle regeneration (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 8-9, malfait2020theehlers–danlossyndromes pages 11-12, shoji2024possibleinvolvementof pages 1-2) | Fibroblasts; ER/Golgi secretory pathway; myoblasts/myocytes; skeletal muscle; skin; bone/connective tissue (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 7-8, shoji2024possibleinvolvementof pages 1-2) | Short stature; muscle hypotonia; delayed motor development; hypermobile joints; hyperextensible skin; finely wrinkled palms; protuberant eyes/bluish sclera; platyspondyly and other radiologic changes; occasional white-matter abnormalities reported in case literature (agrawal2023acaseof pages 1-1, agrawal2023acaseof pages 3-4, agrawal2023acaseof pages 1-2, dijk2024clinicaldiagnosisof pages 4-6) | Li et al. 2024, *Mammalian SLC39A13 promotes ER/Golgi iron transport and iron homeostasis in multiple compartments* DOI: 10.1038/s41467-024-55149-2 URL: https://doi.org/10.1038/s41467-024-55149-2 (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 3-4, li2024mammalianslc39a13promotes pages 8-9, li2024mammalianslc39a13promotes pages 7-8); Shoji et al. 2024, *Possible involvement of zinc transporter ZIP13 in myogenic differentiation* DOI: 10.1038/s41598-024-56912-7 URL: https://doi.org/10.1038/s41598-024-56912-7 (shoji2024possibleinvolvementof pages 1-2); Agrawal et al. 2023 DOI: 10.1093/omcr/omac107 URL: https://doi.org/10.1093/omcr/omac107 (agrawal2023acaseof pages 1-1, agrawal2023acaseof pages 3-4) | Foundational mechanism summarized in Malfait et al. 2020, *The Ehlers–Danlos syndromes* DOI: 10.1038/s41572-020-0194-9 URL: https://doi.org/10.1038/s41572-020-0194-9 (malfait2020theehlers–danlossyndromes pages 11-12); original disease association PMIDs cited in Open Targets evidence include 18513683 and 18985159 (diana2025b3galt6mutationslead pages 1-2) | Strongest emerging translational implication in this run: secretory-pathway iron restoration rescued collagen hydroxylation in experimental systems, suggesting metal-compartment homeostasis as a tractable mechanistic axis; no registered interventional trials identified here (li2024mammalianslc39a13promotes pages 4-5, li2024mammalianslc39a13promotes pages 7-8) |
| **B3GAT3** *(related linkeropathy; not classically listed in 2017 spEDS but included in 2024 genetic diagnosis review as causing a highly similar phenotype)* | GlcAT-I / glucuronyltransferase adding glucuronic acid to complete the linker tetrasaccharide | Autosomal recessive | Deficiency disrupts final linker assembly step; clinically overlaps the spEDS/linkeropathy continuum. In B3GALT6-deficient systems, GlcAT-I can partially compensate by generating an alternative trisaccharide linker, highlighting pathway-level convergence (diana2025b3galt6mutationslead pages 12-14, zschocke2024geneticdiagnosisof pages 5-6) | glycosaminoglycan biosynthetic process; proteoglycan metabolic process; extracellular matrix organization; skeletal system development (diana2025b3galt6mutationslead pages 12-14, zschocke2024geneticdiagnosisof pages 5-6) | Fibroblasts/connective tissue; cartilage; bone; cardiovascular tissues in broader linkeropathy literature (zschocke2024geneticdiagnosisof pages 5-6) | Skeletal dysplasia, short stature, joint hypermobility/contractures, variable skin/connective tissue findings; considered part of a linkeropathy continuum bridging EDS and skeletal dysplasias (zschocke2024geneticdiagnosisof pages 5-6) | Zschocke et al. 2024 DOI: 10.1515/medgen-2024-2061 URL: https://doi.org/10.1515/medgen-2024-2061 (zschocke2024geneticdiagnosisof pages 5-6); Dijk et al. 2024 DOI: 10.1515/medgen-2024-2060 URL: https://doi.org/10.1515/medgen-2024-2060 (dijk2024clinicaldiagnosisof pages 4-6) | Ritelli et al. 2019, *Further Defining the Phenotypic Spectrum of B3GAT3 Mutations and Literature Review on Linkeropathy Syndromes* DOI: 10.3390/genes10090631 URL: https://doi.org/10.3390/genes10090631 (paper-search result summarized in run); pathway context in Van Damme et al. 2018 DOI: 10.1093/hmg/ddy234 URL: https://doi.org/10.1093/hmg/ddy234 (diana2025b3galt6mutationslead pages 12-14) | Best represented as a **related linkeropathy / phenotypic continuum** note in a knowledge base, rather than a core 2017 spEDS gene, unless adopting the broader 2024 framing (zschocke2024geneticdiagnosisof pages 5-6) |


*Table: This table summarizes the gene-specific molecular mechanisms, affected pathways, tissues, phenotypes, and evidence base for spondylodysplastic Ehlers-Danlos syndrome. It is designed for knowledge-base use and highlights both recent 2023–2024 findings and foundational studies.*

---

## Statistics and data points (recent sources)
- Prevalence estimate: **spEDS prevalence <1:1,000,000** (2024 review). (dijk2024clinicaldiagnosisof pages 4-6)
- Reported individuals: **spEDS reported in >100 individuals** (2024 review). (zschocke2024geneticdiagnosisof pages 5-6)
- Joint hypermobility frequency: **96.0% (24/25)** among spEDS cases in a 2023 systematic review. (doolan2023extracutaneousfeaturesand pages 1-2)
- SLC39A13 molecular case count: as of a 2023 case report, **13 individuals** with molecularly diagnosed SLC39A13-related spEDS had been reported prior to that case. (agrawal2023acaseof pages 1-1)

---

## Limitations of this evidence set
- Several mechanistic claims in EDS biology are supported by high-authority reviews but are not accompanied by explicit PMIDs in the retrieved excerpts; where PMIDs were visible in OpenTargets evidence (e.g., 18513683, 18985159 for SLC39A13), full primary texts were not retrieved in this run. (diana2025b3galt6mutationslead pages 1-2)
- The 2023 systematic review contains additional spEDS phenotype frequencies in a table, but the retrieved text segment did not preserve labeled phenotype-to-percentage mapping; only the clearly labeled 24/25 hypermobility statistic could be used confidently. (doolan2023extracutaneousfeaturesand pages 1-2, doolan2023extracutaneousfeaturesand pages 4-4)

---

## Key references (with publication dates and URLs)
- van Dijk FS et al. **Clinical diagnosis of the monogenic Ehlers-Danlos syndromes**. *Medizinische Genetik*. **Nov 2024**. https://doi.org/10.1515/medgen-2024-2060 (dijk2024clinicaldiagnosisof pages 4-6)
- Zschocke J et al. **Genetic diagnosis of the Ehlers-Danlos syndromes**. *Medizinische Genetik*. **Nov 2024**. https://doi.org/10.1515/medgen-2024-2061 (zschocke2024geneticdiagnosisof pages 5-6)
- Li H et al. **Mammalian SLC39A13 promotes ER/Golgi iron transport and iron homeostasis in multiple compartments**. *Nature Communications*. **Dec 2024**. https://doi.org/10.1038/s41467-024-55149-2 (li2024mammalianslc39a13promotes pages 4-5)
- Shoji M et al. **Possible involvement of zinc transporter ZIP13 in myogenic differentiation**. *Scientific Reports*. **Apr 2024**. https://doi.org/10.1038/s41598-024-56912-7 (shoji2024possibleinvolvementof pages 1-2)
- Doolan BJ et al. **Extracutaneous features and complications of the Ehlers-Danlos syndromes: A systematic review**. *Frontiers in Medicine*. **Jan 2023**. https://doi.org/10.3389/fmed.2023.1053466 (doolan2023extracutaneousfeaturesand pages 1-2)
- Agrawal P et al. **A case of Ehlers–Danlos syndrome presenting as short stature: a novel mutation in SLC39A13 causing spEDS**. *Oxford Medical Case Reports*. **Jan 2023**. https://doi.org/10.1093/omcr/omac107 (agrawal2023acaseof pages 1-1)



References

1. (dijk2024clinicaldiagnosisof pages 4-6): Fleur S. van Dijk, Chloe Angwin, Serwet Demirdas, Neeti Ghali, and Johannes Zschocke. Clinical diagnosis of the monogenic ehlers-danlos syndromes. Medizinische Genetik, 36:225-234, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2060, doi:10.1515/medgen-2024-2060. This article has 2 citations.

2. (zschocke2024geneticdiagnosisof pages 5-6): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 4 citations.

3. (caraffi2019severeperipheraljoint pages 1-3): Stefano Giuseppe Caraffi, Ilenia Maini, Ivan Ivanovski, Marzia Pollazzon, Sara Giangiobbe, Maurizia Valli, Antonio Rossi, Silvia Sassi, Silvia Faccioli, Maja Di Rocco, Cinzia Magnani, Belinda Campos-Xavier, Sheila Unger, Andrea Superti-Furga, and Livia Garavelli. Severe peripheral joint laxity is a distinctive clinical feature of spondylodysplastic-ehlers-danlos syndrome (eds)-b4galt7 and spondylodysplastic-eds-b3galt6. Genes, 10:799, Oct 2019. URL: https://doi.org/10.3390/genes10100799, doi:10.3390/genes10100799. This article has 31 citations.

4. (damme2018biallelicb3galt6mutations pages 1-4): Tim Van Damme, Xiaomeng Pang, Brecht Guillemyn, Sandrine Gulberti, Delfien Syx, Riet De Rycke, Olivier Kaye, Christine E M de Die-Smulders, Rolph Pfundt, Ariana Kariminejad, Sheela Nampoothiri, Geneviève Pierquin, Saskia Bulk, Austin A Larson, Kathryn C Chatfield, Marleen Simon, Anne Legrand, Marion Gerard, Sofie Symoens, Sylvie Fournel-Gigleux, and Fransiska Malfait. Biallelic b3galt6 mutations cause spondylodysplastic ehlers‐danlos syndrome. Human Molecular Genetics, 27:3475–3487, Jun 2018. URL: https://doi.org/10.1093/hmg/ddy234, doi:10.1093/hmg/ddy234. This article has 54 citations and is from a domain leading peer-reviewed journal.

5. (damme2018biallelicb3galt6mutations pages 10-13): Tim Van Damme, Xiaomeng Pang, Brecht Guillemyn, Sandrine Gulberti, Delfien Syx, Riet De Rycke, Olivier Kaye, Christine E M de Die-Smulders, Rolph Pfundt, Ariana Kariminejad, Sheela Nampoothiri, Geneviève Pierquin, Saskia Bulk, Austin A Larson, Kathryn C Chatfield, Marleen Simon, Anne Legrand, Marion Gerard, Sofie Symoens, Sylvie Fournel-Gigleux, and Fransiska Malfait. Biallelic b3galt6 mutations cause spondylodysplastic ehlers‐danlos syndrome. Human Molecular Genetics, 27:3475–3487, Jun 2018. URL: https://doi.org/10.1093/hmg/ddy234, doi:10.1093/hmg/ddy234. This article has 54 citations and is from a domain leading peer-reviewed journal.

6. (li2024mammalianslc39a13promotes pages 4-5): Huihui Li, Yanmei Cui, Yule Hu, Mengran Zhao, Kuanyu Li, Xiaoyun Pang, Fei Sun, and Bing Zhou. Mammalian slc39a13 promotes er/golgi iron transport and iron homeostasis in multiple compartments. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55149-2, doi:10.1038/s41467-024-55149-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

7. (li2024mammalianslc39a13promotes pages 8-9): Huihui Li, Yanmei Cui, Yule Hu, Mengran Zhao, Kuanyu Li, Xiaoyun Pang, Fei Sun, and Bing Zhou. Mammalian slc39a13 promotes er/golgi iron transport and iron homeostasis in multiple compartments. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55149-2, doi:10.1038/s41467-024-55149-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (diana2025b3galt6mutationslead pages 1-2): Roméo Milan Diana, Benjamin Jolivet, Jean-Baptiste Vincourt, Sébastien Hergalant, Grégory Francius, Yasaman Karami, Hamed Khakzad, Rebekka Wild, Marie Bourgeais, Anne Robert, Alison Wurtz, Guillermo Barreto, Nick Ramalanjaona, Déborah Helle, Rachel Onifarasoaniaina, Sophie Front, Chrystel Lopin-Bon, Delfien Syx, Fransiska Malfait, Sylvie Fournel-Gigleux, Sandrine Gulberti, and Catherine Bui. B3galt6 mutations lead to compromised connective tissue biomechanics in ehlers-danlos syndrome. JCI Insight, Aug 2025. URL: https://doi.org/10.1172/jci.insight.179474, doi:10.1172/jci.insight.179474. This article has 1 citations and is from a domain leading peer-reviewed journal.

9. (doolan2023extracutaneousfeaturesand pages 1-2): Brent J. Doolan, Mark E. Lavallee, Ingrid Hausser, Jane R. Schubart, F. Michael Pope, Suranjith L. Seneviratne, Ingrid M. Winship, and Nigel P. Burrows. Extracutaneous features and complications of the ehlers-danlos syndromes: a systematic review. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2023.1053466, doi:10.3389/fmed.2023.1053466. This article has 27 citations.

10. (shoji2024possibleinvolvementof pages 1-2): Masaki Shoji, Takuto Ohashi, Saki Nagase, Haato Yuri, Kenta Ichihashi, Teruhisa Takagishi, Yuji Nagata, Yuki Nomura, Ayako Fukunaka, Sae Kenjou, Hatsuna Miyake, Takafumi Hara, Emi Yoshigai, Yoshio Fujitani, Hidetoshi Sakurai, Heloísa G. dos Santos, Toshiyuki Fukada, and Takashi Kuzuhara. Possible involvement of zinc transporter zip13 in myogenic differentiation. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-56912-7, doi:10.1038/s41598-024-56912-7. This article has 4 citations and is from a peer-reviewed journal.

11. (ritelli2017expandingtheclinical pages 1-2): Marco Ritelli, Chiara Dordoni, Valeria Cinquina, Marina Venturini, Piergiacomo Calzavara-Pinton, and Marina Colombi. Expanding the clinical and mutational spectrum of b4galt7-spondylodysplastic ehlers-danlos syndrome. Orphanet Journal of Rare Diseases, Sep 2017. URL: https://doi.org/10.1186/s13023-017-0704-3, doi:10.1186/s13023-017-0704-3. This article has 50 citations and is from a peer-reviewed journal.

12. (ritelli2017expandingtheclinical media 36a1859a): Marco Ritelli, Chiara Dordoni, Valeria Cinquina, Marina Venturini, Piergiacomo Calzavara-Pinton, and Marina Colombi. Expanding the clinical and mutational spectrum of b4galt7-spondylodysplastic ehlers-danlos syndrome. Orphanet Journal of Rare Diseases, Sep 2017. URL: https://doi.org/10.1186/s13023-017-0704-3, doi:10.1186/s13023-017-0704-3. This article has 50 citations and is from a peer-reviewed journal.

13. (ritelli2017expandingtheclinical media 0d274780): Marco Ritelli, Chiara Dordoni, Valeria Cinquina, Marina Venturini, Piergiacomo Calzavara-Pinton, and Marina Colombi. Expanding the clinical and mutational spectrum of b4galt7-spondylodysplastic ehlers-danlos syndrome. Orphanet Journal of Rare Diseases, Sep 2017. URL: https://doi.org/10.1186/s13023-017-0704-3, doi:10.1186/s13023-017-0704-3. This article has 50 citations and is from a peer-reviewed journal.

14. (delbaere2020hypomorphiczebrafishmodels pages 1-5): Sarah Delbaere, Tim Van Damme, Delfien Syx, Sofie Symoens, Paul Coucke, Andy Willaert, and Fransiska Malfait. Hypomorphic zebrafish models mimic the musculoskeletal phenotype of β4galt7-deficient ehlers-danlos syndrome. Matrix Biology, 89:59-75, Jul 2020. URL: https://doi.org/10.1016/j.matbio.2019.12.002, doi:10.1016/j.matbio.2019.12.002. This article has 32 citations and is from a domain leading peer-reviewed journal.

15. (damme2018biallelicb3galt6mutations pages 13-15): Tim Van Damme, Xiaomeng Pang, Brecht Guillemyn, Sandrine Gulberti, Delfien Syx, Riet De Rycke, Olivier Kaye, Christine E M de Die-Smulders, Rolph Pfundt, Ariana Kariminejad, Sheela Nampoothiri, Geneviève Pierquin, Saskia Bulk, Austin A Larson, Kathryn C Chatfield, Marleen Simon, Anne Legrand, Marion Gerard, Sofie Symoens, Sylvie Fournel-Gigleux, and Fransiska Malfait. Biallelic b3galt6 mutations cause spondylodysplastic ehlers‐danlos syndrome. Human Molecular Genetics, 27:3475–3487, Jun 2018. URL: https://doi.org/10.1093/hmg/ddy234, doi:10.1093/hmg/ddy234. This article has 54 citations and is from a domain leading peer-reviewed journal.

16. (malfait2020theehlers–danlossyndromes pages 11-12): Fransiska Malfait, Marco Castori, Clair A. Francomano, Cecilia Giunta, Tomoki Kosho, and Peter H. Byers. The ehlers–danlos syndromes. Nature Reviews Disease Primers, 6:1-25, Jul 2020. URL: https://doi.org/10.1038/s41572-020-0194-9, doi:10.1038/s41572-020-0194-9. This article has 372 citations.

17. (li2024mammalianslc39a13promotes pages 7-8): Huihui Li, Yanmei Cui, Yule Hu, Mengran Zhao, Kuanyu Li, Xiaoyun Pang, Fei Sun, and Bing Zhou. Mammalian slc39a13 promotes er/golgi iron transport and iron homeostasis in multiple compartments. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55149-2, doi:10.1038/s41467-024-55149-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

18. (agrawal2023acaseof pages 1-2): Poorvi Agrawal, Harpreet Kaur, Alpana Kondekar, and Surbhi Rathi. A case of ehlers–danlos syndrome presenting as short stature: a novel mutation in slc39a13 causing spondylodysplastic ehlers–danlos syndrome. Oxford Medical Case Reports, Jan 2023. URL: https://doi.org/10.1093/omcr/omac107, doi:10.1093/omcr/omac107. This article has 7 citations and is from a peer-reviewed journal.

19. (agrawal2023acaseof pages 1-1): Poorvi Agrawal, Harpreet Kaur, Alpana Kondekar, and Surbhi Rathi. A case of ehlers–danlos syndrome presenting as short stature: a novel mutation in slc39a13 causing spondylodysplastic ehlers–danlos syndrome. Oxford Medical Case Reports, Jan 2023. URL: https://doi.org/10.1093/omcr/omac107, doi:10.1093/omcr/omac107. This article has 7 citations and is from a peer-reviewed journal.

20. (agrawal2023acaseof pages 3-4): Poorvi Agrawal, Harpreet Kaur, Alpana Kondekar, and Surbhi Rathi. A case of ehlers–danlos syndrome presenting as short stature: a novel mutation in slc39a13 causing spondylodysplastic ehlers–danlos syndrome. Oxford Medical Case Reports, Jan 2023. URL: https://doi.org/10.1093/omcr/omac107, doi:10.1093/omcr/omac107. This article has 7 citations and is from a peer-reviewed journal.

21. (li2024mammalianslc39a13promotes pages 1-2): Huihui Li, Yanmei Cui, Yule Hu, Mengran Zhao, Kuanyu Li, Xiaoyun Pang, Fei Sun, and Bing Zhou. Mammalian slc39a13 promotes er/golgi iron transport and iron homeostasis in multiple compartments. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55149-2, doi:10.1038/s41467-024-55149-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

22. (diana2025b3galt6mutationslead pages 12-14): Roméo Milan Diana, Benjamin Jolivet, Jean-Baptiste Vincourt, Sébastien Hergalant, Grégory Francius, Yasaman Karami, Hamed Khakzad, Rebekka Wild, Marie Bourgeais, Anne Robert, Alison Wurtz, Guillermo Barreto, Nick Ramalanjaona, Déborah Helle, Rachel Onifarasoaniaina, Sophie Front, Chrystel Lopin-Bon, Delfien Syx, Fransiska Malfait, Sylvie Fournel-Gigleux, Sandrine Gulberti, and Catherine Bui. B3galt6 mutations lead to compromised connective tissue biomechanics in ehlers-danlos syndrome. JCI Insight, Aug 2025. URL: https://doi.org/10.1172/jci.insight.179474, doi:10.1172/jci.insight.179474. This article has 1 citations and is from a domain leading peer-reviewed journal.

23. (li2024mammalianslc39a13promotes pages 3-4): Huihui Li, Yanmei Cui, Yule Hu, Mengran Zhao, Kuanyu Li, Xiaoyun Pang, Fei Sun, and Bing Zhou. Mammalian slc39a13 promotes er/golgi iron transport and iron homeostasis in multiple compartments. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55149-2, doi:10.1038/s41467-024-55149-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

24. (doolan2023extracutaneousfeaturesand pages 4-4): Brent J. Doolan, Mark E. Lavallee, Ingrid Hausser, Jane R. Schubart, F. Michael Pope, Suranjith L. Seneviratne, Ingrid M. Winship, and Nigel P. Burrows. Extracutaneous features and complications of the ehlers-danlos syndromes: a systematic review. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2023.1053466, doi:10.3389/fmed.2023.1053466. This article has 27 citations.