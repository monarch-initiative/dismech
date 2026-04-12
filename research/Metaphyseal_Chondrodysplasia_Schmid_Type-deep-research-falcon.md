---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-02T15:45:44.851028'
end_time: '2026-04-02T16:15:52.760446'
duration_seconds: 1807.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metaphyseal Chondrodysplasia, Schmid Type
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Metaphyseal Chondrodysplasia, Schmid Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Metaphyseal Chondrodysplasia, Schmid Type**.
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
- **Disease Name:** Metaphyseal Chondrodysplasia, Schmid Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Metaphyseal Chondrodysplasia, Schmid Type**.
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


## Comprehensive Pathophysiology Research Report: Metaphyseal Chondrodysplasia, Schmid Type (MCDS)

### Disease identifiers
- **Disease name:** Metaphyseal chondrodysplasia, Schmid type (MCDS) / Schmid metaphyseal chondrodysplasia (SMCD)
- **Causal gene:** **COL10A1** (type X collagen α1 chain) (ho2007col10a1nonsenseand pages 1-2, richmond2024schmidmetaphysealchondrodysplasia pages 12-15)
- **Inheritance:** Autosomal dominant with variable expressivity; de novo variants are common; rare biallelic cases reported with more severe phenotype (richmond2024schmidmetaphysealchondrodysplasia pages 12-15, richmond2024schmidmetaphysealchondrodysplasia pages 10-12)
- **Epidemiology:** Historical incidence/prevalence estimate **~3–6 per million** (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, meng2026clinicalmolecularcharacteristics pages 1-2)

### Executive summary (current understanding)
MCDS is a growth-plate disorder caused by pathogenic **COL10A1** variants—usually in the **NC1 trimerization domain**—that disrupt collagen X assembly, leading to intracellular retention of mutant collagen X in **hypertrophic chondrocytes** and triggering **endoplasmic reticulum (ER) stress** with activation of the **unfolded protein response (UPR)** and **integrated stress response (ISR)**. These stress programs alter terminal chondrocyte differentiation rather than primarily inducing apoptosis, producing expansion of the hypertrophic zone, impaired **VEGF-mediated vascular invasion**, reduced osteoclast recruitment, and delayed endochondral ossification. A major mechanistic emphasis is PERK→eIF2α→ATF4/CHOP signaling, which can drive aberrant differentiation (including SOX9 dysregulation), while IRE1/XBP1 appears partly redundant for disease severity in at least one mouse genetic context. Recent 2024 work extends the phenotype to include **cell polarity disruption** in chondrocytes/osteoblasts, with rescue by pharmacologic ER-stress reduction in a fish model. (rajpar2009targetedinductionof pages 1-2, cameron2011transcriptionalprofilingof pages 1-2, wang2018inhibitingtheintegrated pages 1-2, cameron2015xbp1independentuprpathways pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa)

---

## 1) Core pathophysiology

### Primary pathogenic mechanism: mutant collagen X proteostasis failure
- **Type X collagen** is expressed specifically in **hypertrophic chondrocytes** of the growth plate. Dominant COL10A1 variants (missense or truncating) often impair collagen X trimerization and/or folding, causing **intracellular retention** within the ER, rather than normal secretion and extracellular matrix (ECM) incorporation (ho2007col10a1nonsenseand pages 1-2, rajpar2009targetedinductionof pages 1-2, forouhan2018carbamazepinereducesdisease pages 4-7).
- Not all truncating variants behave identically: some may undergo **nonsense-mediated decay (NMD)** (haploinsufficiency-like), whereas others produce stable mutant mRNA/protein leading to a “gain-of-function” ER-retention mechanism (ho2007col10a1nonsenseand pages 1-2, forouhan2018carbamazepinereducesdisease pages 1-4).

### ER stress → UPR/ISR activation in hypertrophic chondrocytes
- In a COL10A1 p.N617K knock-in model, mutant collagen X retention in hypertrophic chondrocytes provokes **ER stress** and a robust **UPR**, with activation of canonical sensors **PERK, ATF6, and IRE1** (rajpar2009targetedinductionof pages 1-2).
- Transcriptional profiling of microdissected mutant hypertrophic zones showed upregulation of **chaperones, foldases, and ER-associated degradation (ERAD) machinery**, including regulators such as **Wfs1** and **Syvn1**, and induction of **Fgf21** among other genes (cameron2011transcriptionalprofilingof pages 1-2).

### Differentiation derailment (developmental “arrest”) rather than immediate apoptosis
- In the Cameron et al. transcriptional profiling study, although CHOP/Cebpb pathway induction was observed, **apoptosis was not increased** in mutant hypertrophic zones; instead, ER-stressed hypertrophic chondrocytes displayed disrupted maturation, including persistence of a proliferative-like gene-expression profile (cameron2011transcriptionalprofilingof pages 1-2).
- A distinct mechanistic formulation comes from ISR-focused work: in an MCDS mouse model, the **PERK branch** dominated, with **ATF4-directed transactivation of Sox9** proposed to revert chondrocyte differentiation; CHOP and ATF4 also transactivated **Fgf21** to enable cell-autonomous survival (wang2018inhibitingtheintegrated pages 1-2).

### Tissue-level consequence: impaired vascular invasion and osteoclast recruitment
- Rajpar et al. linked ER-stressed hypertrophic chondrocytes to reduced hypertrophic differentiation and **reduced osteoclast recruitment**, and concluded that the hypertrophic zone expands due to a decreased rate of **VEGF-mediated vascular invasion** at the growth plate (rajpar2009targetedinductionof pages 1-2).

### Recent development (2024): cell polarity as a downstream pathogenic axis
- A 2024 medaka **col10a1** mutant model of MCDS reported early **cell polarity disruption** in chondrocytes and osteoblasts alongside ER stress features, producing abnormal stacking/organization and skeletal deformity; importantly, ER-stress reduction with **carbamazepine** rescued polarity impairment and skeletal defects (tan2024acollagen10a1mutation pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa).

---

## 2) Key molecular players

### Genes/proteins (causal and mechanistic)
- **COL10A1 (type X collagen)**: causal; variants cluster in NC1 domain; misfolding/retention triggers ER stress (ho2007col10a1nonsenseand pages 1-2, richmond2024schmidmetaphysealchondrodysplasia pages 12-15).
- **UPR sensors/branches:**
  - **PERK (EIF2AK3) → eIF2α phosphorylation → ATF4 → CHOP (DDIT3)**: drives ISR, alters differentiation; PERK inhibition improved disease in vivo (wang2018inhibitingtheintegrated pages 1-2).
  - **ATF6**: activated and contributes to chaperone/ERAD responses; ATF6 cleavage observed in some models (forouhan2018carbamazepinereducesdisease pages 4-7, forouhan2018carbamazepinereducesdisease pages 7-9).
  - **IRE1 (ERN1) → XBP1 splicing**: activated (e.g., increased Xbp1s) yet can be redundant for severity in a mouse genetic test (cameron2015xbp1independentuprpathways pages 1-2, forouhan2018carbamazepinereducesdisease pages 4-7).
- **UPR markers/effectors:** **BiP/GRP78 (HSPA5)**, **CRELD2**, **SYVN1**, **WFS1**, **ARMET**, **Fgf21** (cameron2011transcriptionalprofilingof pages 1-2, forouhan2018carbamazepinereducesdisease pages 7-9).
- **Differentiation regulators:** **SOX9**, **C/EBPβ (CEBPB)**, **RUNX2**, **GADD45β**—implicated in differentiation control and UPR-mediated disruption (cameron2015xbp1independentuprpathways pages 1-2, wang2018inhibitingtheintegrated pages 1-2).
- **Tissue remodeling/invasion axis:** **VEGF-mediated vascular invasion**, osteoclast recruitment (rajpar2009targetedinductionof pages 1-2).

### Chemical entities / candidate therapeutics
- **Carbamazepine (CBZ)**: repurposed ER-stress/proteostasis modulator; reduces ER stress markers and improves growth plate architecture and skeletal measures in mice; also rescues skeletal/cell polarity defects in the 2024 medaka model (forouhan2018carbamazepinereducesdisease pages 7-9, tan2024acollagen10a1mutation media 7b4c3afa).
- **ISRIB** (ISR inhibitor): reported to improve MCDS-related phenotypes in mice by inhibiting ATF4-driven aberrant differentiation, though with practical limitations (e.g., solubility/bioavailability) and incomplete rescue (wang2018inhibitingtheintegrated pages 21-22, wang2018inhibitingtheintegrated pages 19-21).

### Cell types primarily affected
- **Hypertrophic chondrocytes** (primary): site of COL10A1 expression and mutant protein retention/UPR activation (kung2012hypertrophicchondrocyteshave pages 1-2, rajpar2009targetedinductionof pages 1-2).
- **Osteoblasts** (implicated in 2024 medaka model): polarity disruption and ER stress ultrastructure in mutants (tan2024acollagen10a1mutation media 7b4c3afa).

### Anatomical locations
- **Growth plate (epiphyseal plate), hypertrophic zone**, metaphyses of long bones, hip region (coxa vara), proximal tibia/distal femur (richmond2024schmidmetaphysealchondrodysplasia pages 3-6, rajpar2009targetedinductionof pages 1-2).

---

## 3) Dysregulated pathways and processes (GO-oriented)
Key disrupted biological processes supported by the evidence base include:
- **Response to ER stress / unfolded protein response** with induction of chaperones, foldases, and **ERAD** machinery (cameron2011transcriptionalprofilingof pages 1-2, patterson2014mechanismsandmodels pages 3-4).
- **Integrated stress response / PERK-eIF2α signaling** influencing cell fate/differentiation through ATF4/CHOP and downstream effectors including **SOX9** and **FGF21** (wang2018inhibitingtheintegrated pages 1-2).
- **Regulation of chondrocyte differentiation / hypertrophic maturation**, including disruption of C/EBPβ-mediated programs and suppression of RUNX2-associated pathways (cameron2015xbp1independentuprpathways pages 1-2).
- **Angiogenesis/vascular invasion at growth plate** (VEGF-mediated) and **osteoclast recruitment** required for endochondral ossification (rajpar2009targetedinductionof pages 1-2).
- **Establishment/maintenance of cell polarity** (2024 model) as a downstream phenotype potentially linking ER stress to tissue architecture (tan2024acollagen10a1mutation media 7b4c3afa).

---

## 4) Cellular components (where key processes occur)
- **Rough endoplasmic reticulum (RER) and ER lumen:** site of collagen folding; mutant protein retention leads to ER distension and stress responses; TEM evidence in 2024 medaka mutants shows swollen/fragmented RER cisternae (tan2024acollagen10a1mutation media 7b4c3afa).

---

## 5) Disease progression (sequence of events)
1. **COL10A1 variant** (typically NC1 domain missense/truncation) alters collagen X folding/trimerization (ho2007col10a1nonsenseand pages 1-2, richmond2024schmidmetaphysealchondrodysplasia pages 12-15).
2. **Intracellular retention** of mutant collagen X in hypertrophic chondrocyte ER triggers **ER stress** (rajpar2009targetedinductionof pages 1-2, forouhan2018carbamazepinereducesdisease pages 4-7).
3. Activation of **UPR/ISR** (PERK/ATF4/CHOP; ATF6 cleavage; XBP1 splicing), inducing chaperones/ERAD and altering translation/transcription programs (cameron2011transcriptionalprofilingof pages 1-2, forouhan2018carbamazepinereducesdisease pages 7-9).
4. **Hypertrophic differentiation disruption**: developmental arrest/proliferative-like persistence; Sox9 misexpression and C/EBPβ/RUNX2 interference are proposed nodes (cameron2011transcriptionalprofilingof pages 1-2, cameron2015xbp1independentuprpathways pages 1-2, wang2018inhibitingtheintegrated pages 1-2).
5. Reduced hypertrophic-zone output (e.g., **VEGF-mediated vascular invasion**) and reduced osteoclast recruitment slows turnover of hypertrophic cartilage and delays ossification, causing **hypertrophic zone expansion** and impaired long-bone growth (rajpar2009targetedinductionof pages 1-2).
6. Clinical manifestations emerge in early childhood (typically not present at birth) with progressive deformity/gait changes (richmond2024schmidmetaphysealchondrodysplasia pages 3-6).

---

## 6) Phenotypic manifestations (and mechanistic links)
- **Short-limbed short stature, genu varum, waddling gait, lumbar lordosis, coxa vara, metaphyseal flaring/widening** reflect impaired endochondral ossification and altered growth plate architecture (richmond2024schmidmetaphysealchondrodysplasia pages 3-6, richmond2024schmidmetaphysealchondrodysplasia pages 6-8).
- **Quantitative phenotype frequencies (aggregated cohorts/review):** waddling gait >80%/88.5%, genu varum >80%/83.6%, lumbar lordosis ~51–>60%, coxa vara ~50–80% or ~80% depending on dataset (richmond2024schmidmetaphysealchondrodysplasia pages 3-6, meng2026clinicalmolecularcharacteristics pages 8-9).

---

## Recent developments (prioritizing 2023–2024)

### 2024: Novel model-based mechanistic insight—cell polarity
- Tan et al. (iScience, **Apr 2024**, DOI:10.1016/j.isci.2024.109405) report a medaka **col10a1** MCDS model in which ER stress is accompanied by early disruption of chondrocyte/osteoblast polarity, disorganized stacking, and skeletal deformity, with **carbamazepine rescue** (tan2024acollagen10a1mutation pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa).

### 2024: Clinical consolidation of genetics and care pathways
- Richmond & Savarirayan (GeneReviews chapter update displayed as 2024; DOI:10.1007/978-1-60327-161-5_164) summarize that pathogenic variants are mostly missense or truncating, commonly clustered in NC1; penetrance approaches 100% with broad variability; and provide current diagnostic testing and management guidance (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, richmond2024schmidmetaphysealchondrodysplasia pages 1-3).

*Evidence limitation note:* within the retrieved corpus, 2023–2024 mechanistic primary literature specifically on MCDS is limited mainly to the 2024 medaka model plus the 2024 GeneReviews-style synthesis; much of the UPR/ISR mechanistic detail still relies on landmark mouse-model studies (2009–2018). (rajpar2009targetedinductionof pages 1-2, wang2018inhibitingtheintegrated pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa)

---

## Current applications and real-world implementations

### Diagnostics (genetic testing)
- Diagnosis can be made by clinical/radiographic features and/or identification of a **heterozygous COL10A1 pathogenic variant** (richmond2024schmidmetaphysealchondrodysplasia pages 1-3).
- Recommended molecular approaches include:
  - **Single-gene COL10A1 sequencing** (detects missense/nonsense/splice-site variants and small indels) (richmond2024schmidmetaphysealchondrodysplasia pages 1-3).
  - **Multigene skeletal dysplasia panels** including COL10A1 (richmond2024schmidmetaphysealchondrodysplasia pages 1-3).
  - **Exome/genome sequencing** when phenotype is atypical or differential is broad (richmond2024schmidmetaphysealchondrodysplasia pages 1-3).
- Deletion/duplication (CNV) testing is expected to be low yield because reported pathogenic variants to date are missense/truncating rather than multi-exon CNVs (richmond2024schmidmetaphysealchondrodysplasia pages 3-6, richmond2024schmidmetaphysealchondrodysplasia pages 1-3).

### Genetic counseling
- Autosomal dominant transmission risk is ~50% when a parent carries the pathogenic variant; mosaicism can complicate parental testing, and sibling recurrence risk in de novo cases is estimated ~1% due to possible germline mosaicism (richmond2024schmidmetaphysealchondrodysplasia pages 12-15, richmond2024schmidmetaphysealchondrodysplasia pages 10-12).
- Reported de novo fraction: ~43–55% simplex/de novo in GeneReviews summary; inherited fraction 45–57% (richmond2024schmidmetaphysealchondrodysplasia pages 10-12).

### Management
- No formal practice guidelines; care is multidisciplinary (orthopedics, PT/OT, pain management), emphasizing joint-friendly exercise, mobility aids as needed, and weight optimization to reduce joint loading (richmond2024schmidmetaphysealchondrodysplasia pages 8-10, richmond2024schmidmetaphysealchondrodysplasia pages 1-3).
- Orthopedic options include guided growth and osteotomies (valgus-producing, derotational, corrective osteotomy) for progressive or symptomatic deformities (richmond2024schmidmetaphysealchondrodysplasia pages 10-12).
- In a pooled 2026 analysis of reported cases, among 24 cases mentioning treatment, **~74.1% underwent osteotomy**; limited efficacy was noted for calcium/vitamin D/GH in general, though one child on long-acting rhGH plus supplements gained 5 cm over 6 months (meng2026clinicalmolecularcharacteristics pages 8-9).

---

## Therapeutic landscape and expert analysis

### Proteostasis modulation (carbamazepine)
- In a Col10a1 p.Y632X mouse model, **CBZ 250 mg/kg/day** improved femur/tibia growth, normalized hip geometry after 2 weeks, reduced hypertrophic-zone width ~50%, reduced intracellular mutant collagen retention, suppressed multiple UPR arms (reduced Bip/Creld2/Chop mRNAs, decreased Atf4 induction and cleaved Atf6α, suppressed Xbp1 splicing), and improved osteoclast recruitment (forouhan2018carbamazepinereducesdisease pages 7-9).
- A 2020 expert review emphasizes ER stress as a druggable target in MCDS and notes CBZ’s preclinical efficacy and translation efforts, referencing an ongoing trial resource (briggs2020newdevelopmentsin pages 3-5).
- The 2024 GeneReviews summary notes CBZ showed benefit in a mouse model and received EMA orphan drug designation in 2016, directing readers to trial registries for study status (richmond2024schmidmetaphysealchondrodysplasia pages 10-12).

### ISR/PERK-targeted approaches
- PERK inhibition and ISRIB-based modulation improved disease phenotypes in mouse models by reducing ATF4/CHOP-driven aberrant differentiation, including SOX9 dysregulation, though rescue may be incomplete and pharmacologic limitations exist (wang2018inhibitingtheintegrated pages 1-2, wang2018inhibitingtheintegrated pages 21-22).

### Authoritative mechanistic viewpoint
- A key expert-level consensus from landmark genetic and animal studies is that **ER stress in hypertrophic chondrocytes is sufficient** to reproduce essential MCDS cartilage pathology, positioning ER proteostasis (UPR/ISR) as a central node rather than purely “defective ECM” outside the cell (rajpar2009targetedinductionof pages 1-2).

---

## Relevant statistics and data (from included sources)
- **Mutation spectrum (114 cases):** 53.5% missense; 44.7% truncating (nonsense 16.7%, frameshift 28.1%); **90.4% NC1 domain**; origin: 82.4% inherited, 17.6% de novo (subset with data); zygosity: 92.3% heterozygous, 7.7% homozygous (meng2026clinicalmolecularcharacteristics pages 8-9).
- **Genotype–phenotype correlations (pooled analysis):** NC1 variants associated with earlier onset (median 12 vs 72 months, P=0.0014); missense variants associated with lower height Z-score at presentation (−3.62±1.95 vs −1.99±1.28, P=0.013) (meng2026clinicalmolecularcharacteristics pages 1-2, meng2026clinicalmolecularcharacteristics pages 8-9).
- **Mouse pathology (Y632X model):** hypertrophic zone expansion 3.5-fold (wt/m) and 5-fold (m/m) at 3 weeks; Xbp1s ~2-fold increased; CBZ reduced hypertrophic-zone width ~50% (forouhan2018carbamazepinereducesdisease pages 4-7, forouhan2018carbamazepinereducesdisease pages 7-9).

---

## Visual evidence (2024 model)
The medaka model provides direct visual support for (i) disorganized chondrocyte stacking and polarity defects, (ii) ER ultrastructural stress changes, and (iii) rescue with carbamazepine treatment. (tan2024acollagen10a1mutation media 7b4c3afa, tan2024acollagen10a1mutation media 2ad256bd, tan2024acollagen10a1mutation media c648ae69)

---

## Knowledge-base style structured content

### Pathophysiology description (narrative)
Schmid metaphyseal chondrodysplasia is driven primarily by COL10A1 variants that impair type X collagen folding/trimerization in hypertrophic chondrocytes, causing intracellular retention in the rough ER and activation of UPR/ISR pathways (PERK/ATF4/CHOP; ATF6 cleavage; IRE1/XBP1 splicing). The stress response rewires hypertrophic differentiation programs—often manifesting as persistence of proliferative-like gene expression and/or SOX9-driven reversion—while not necessarily inducing early apoptosis. Reduced terminal differentiation impairs VEGF-driven vascular invasion and osteoclast recruitment at the chondro-osseous junction, expanding the hypertrophic zone and slowing endochondral ossification, leading to short stature and characteristic metaphyseal deformities. Recent model systems show that polarity defects may be an additional downstream cellular phenotype linking ER stress to disrupted growth plate architecture. (rajpar2009targetedinductionof pages 1-2, cameron2011transcriptionalprofilingof pages 1-2, wang2018inhibitingtheintegrated pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa)

### Ontology-linked annotations
| Entity type | Preferred label | Ontology ID | Role in MCDS | Key supporting evidence (paper + mechanism) | PMID/DOI | URL | Year |
|---|---|---|---|---|---|---|---|
| Gene | COL10A1 | HGNC:2186 | Causal gene; encodes type X collagen misfolded in ER | Ho 2007: Human/mouse mutations exhibit gain-of-function retention (ho2007col10a1nonsenseand pages 1-2) | 10.1093/hmg/ddm067 | https://doi.org/10.1093/hmg/ddm067 | 2007 |
| GO Biological Process | Cellular response to ER stress / UPR | GO:0034976 / GO:0030968 | Core pathogenic response driving cartilage dysplasia | Cameron 2011: Transcriptomics identify adaptive UPR disrupting hypertrophy (cameron2011transcriptionalprofilingof pages 1-2) | 10.1371/journal.pone.0024600 | https://doi.org/10.1371/journal.pone.0024600 | 2011 |
| Gene | EIF2AK3 (PERK) / ATF4 / DDIT3 (CHOP) | HGNC:3255 / 786 / 2726 | Drives aberrant dedifferentiation via ISR | Wang 2018: PERK/ATF4 transactivates SOX9; CHOP suppresses CEBPB (wang2018inhibitingtheintegrated pages 1-2) | 10.7554/eLife.37673 | https://doi.org/10.7554/eLife.37673 | 2018 |
| Gene | ERN1 (IRE1) / XBP1 | HGNC:3449 / 12811 | UPR branch activated but pathologically redundant | Cameron 2015: Cartilage-specific Xbp1 deletion does not alter disease severity (cameron2015xbp1independentuprpathways pages 1-2) | 10.1371/journal.pgen.1005505 | https://doi.org/10.1371/journal.pgen.1005505 | 2015 |
| Gene | ATF6 | HGNC:788 | UPR sensor driving chaperone and ERAD expression | Briggs 2020: Review highlighting ATF6 activation by BiP dissociation (briggs2020newdevelopmentsin pages 3-5) | 10.12688/f1000research.22275.1 | https://doi.org/10.12688/f1000research.22275.1 | 2020 |
| Gene | HSPA5 (BiP), CRELD2, SYVN1, WFS1 | HGNC:5238, 24652, 16790, 12762 | Highly induced chaperones and ERAD regulators | Forouhan 2018: UPR markers significantly upregulated in Y632X mice (forouhan2018carbamazepinereducesdisease pages 7-9, cameron2011transcriptionalprofilingof pages 1-2) | 10.1093/hmg/ddy253 | https://doi.org/10.1093/hmg/ddy253 | 2018 |
| Gene | FGF21 | HGNC:3689 | Paracrine factor promoting cell-autonomous survival | Wang 2018: Transactivated by CHOP/ATF4 allowing stressed cells to survive (wang2018inhibitingtheintegrated pages 1-2) | 10.7554/eLife.37673 | https://doi.org/10.7554/eLife.37673 | 2018 |
| Gene | SOX9, CEBPB, RUNX2 | HGNC:11204, 1834, 10472 | Master differentiation regulators dysregulated by UPR/ISR | Cameron 2015, Wang 2018: CEBPB/RUNX2 suppressed, SOX9 aberrantly induced (cameron2015xbp1independentuprpathways pages 1-2, wang2018inhibitingtheintegrated pages 1-2) | 10.1371/journal.pgen.1005505 | https://doi.org/10.1371/journal.pgen.1005505 | 2015 |
| GO Biological Process | Angiogenesis (VEGFA) / Osteoclast differentiation | GO:0001525 / GO:0030316 | Impaired vascular invasion delays endochondral ossification | Rajpar 2009: Targeted ER stress reduces VEGFA-mediated invasion and osteoclast recruitment (rajpar2009targetedinductionof pages 1-2) | 10.1371/journal.pgen.1000691 | https://doi.org/10.1371/journal.pgen.1000691 | 2009 |
| CL cell type | Hypertrophic chondrocyte | CL:0000138 | Primary affected cell type retaining mutant collagen | Kung 2012: HZ expansion depends on gene dosage and latent ER capacity (kung2012hypertrophicchondrocyteshave pages 1-2) | 10.1369/0022155412458436 | https://doi.org/10.1369/0022155412458436 | 2012 |
| UBERON anatomy | Epiphyseal plate / Metaphysis | UBERON:0001645 / UBERON:0001460 | Anatomical sites of radiographic flaring and dysplasia | Richmond 2024: Clinical features including metaphyseal widening and coxa vara (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, richmond2024schmidmetaphysealchondrodysplasia pages 3-6) | 10.1007/978-1-60327-161-5_164 | https://doi.org/10.1007/978-1-60327-161-5_164 | 2024 |
| GO Cellular Component | Rough endoplasmic reticulum / ER lumen | GO:0005791 / GO:0005788 | Site of mutant COL10A1 aggregation and swelling | Tan 2024: TEM reveals swollen and fragmented RER cisternae in mutants (tan2024acollagen10a1mutation media 7b4c3afa) | 10.1016/j.isci.2024.109405 | https://doi.org/10.1016/j.isci.2024.109405 | 2024 |
| GO Biological Process | ERAD (ER-associated ubiquitin-dependent catabolism) | GO:0030433 | Induced pathway to clear misfolded collagen X | Patterson 2014: UPR branches mediate ERAD induction in chondrodysplasia (patterson2014mechanismsandmodels pages 3-4, cameron2011transcriptionalprofilingof pages 1-2) | 10.1002/dvdy.24131 | https://doi.org/10.1002/dvdy.24131 | 2014 |
| CHEBI chemical | Carbamazepine / ISRIB | CHEBI:3423 / CHEBI:90656 | CBZ reduces ER stress; ISRIB inhibits PERK/ISR | Forouhan 2018, Wang 2018: CBZ enhances proteolysis; ISRIB prevents dedifferentiation (wang2018inhibitingtheintegrated pages 19-21, forouhan2018carbamazepinereducesdisease pages 7-9) | 10.1093/hmg/ddy253 | https://doi.org/10.1093/hmg/ddy253 | 2018 |
| GO Biological Process | Establishment of cell polarity / MTOC | GO:0030010 / GO:0005815 | Disrupted spatial organization of gamma-tubulin in cartilage | Tan 2024: Mutants show disorganized stacking; rescued by CBZ (tan2024acollagen10a1mutation pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa) | 10.1016/j.isci.2024.109405 | https://doi.org/10.1016/j.isci.2024.109405 | 2024 |


*Table: A structured mapping of key molecular, cellular, and anatomical components in Schmid metaphyseal chondrodysplasia to standardized ontology terms, highlighting the central role of ER stress and the unfolded protein response.*

### Mechanism/phenotype evidence table
| Mechanistic layer | Key molecules/processes | Evidence (study type/model) | Key quantitative data/statistics if available | PMID/DOI | Publication year | URL |
|---|---|---|---|---|---|---|
| Genetic lesion | Heterozygous pathogenic variants in **COL10A1** encoding type X collagen; variants include missense, nonsense, frameshift, small deletions, with strong enrichment in the **NC1 trimerization domain**; autosomal dominant inheritance with occasional de novo and rare biallelic cases (richmond2024schmidmetaphysealchondrodysplasia pages 12-15, meng2026clinicalmolecularcharacteristics pages 8-9, richmond2024schmidmetaphysealchondrodysplasia pages 3-6) | Clinical review and aggregated case summaries; literature-based genotype spectrum (richmond2024schmidmetaphysealchondrodysplasia pages 12-15, meng2026clinicalmolecularcharacteristics pages 8-9, richmond2024schmidmetaphysealchondrodysplasia pages 3-6) | Estimated prevalence **3–6 per million**; **>150 unrelated individuals** with confirmed COL10A1 variants reported; among 114 genetically characterized cases, **53.5% missense**, **44.7% truncating**, **90.4% NC1-domain**, **17.6% de novo**, **92.3% heterozygous**, **7.7% homozygous** (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, richmond2024schmidmetaphysealchondrodysplasia pages 3-6, meng2026clinicalmolecularcharacteristics pages 8-9) | DOI:10.1007/978-1-60327-161-5_164; DOI:10.1007/s00223-025-01457-8 | 2024; 2026 | https://doi.org/10.1007/978-1-60327-161-5_164 ; https://doi.org/10.1007/s00223-025-01457-8 |
| Protein consequence | Mutant collagen X chains are misfolded, fail to trimerize normally, and are retained intracellularly in hypertrophic chondrocytes; some truncating alleles may act via gain-of-function when mutant mRNA/protein persists rather than being fully removed by NMD (ho2007col10a1nonsenseand pages 1-2, rajpar2009targetedinductionof pages 1-2, forouhan2018carbamazepinereducesdisease pages 4-7) | Human genetic/pathology study and knock-in/transgenic mouse models (FCdel, N617K, Y632X) (ho2007col10a1nonsenseand pages 1-2, rajpar2009targetedinductionof pages 1-2, forouhan2018carbamazepinereducesdisease pages 4-7) | In one human case with a truncating mutation, cartilage contained **64% wild-type and 36% mutant COL10A1 mRNA**; in Y632X knock-in mice, mutant mRNA had stability similar to wild type and produced retained truncated protein (ho2007col10a1nonsenseand pages 1-2, forouhan2018carbamazepinereducesdisease pages 4-7) | DOI:10.1093/hmg/ddm067; DOI:10.1371/journal.pgen.1000691; DOI:10.1093/hmg/ddy253 | 2007; 2009; 2018 | https://doi.org/10.1093/hmg/ddm067 ; https://doi.org/10.1371/journal.pgen.1000691 ; https://doi.org/10.1093/hmg/ddy253 |
| Cellular stress response | Intracellular retention of mutant collagen X triggers **ER stress** and a canonical **UPR/ISR** involving **BiP/GRP78**, **PERK–eIF2α–ATF4–CHOP**, **IRE1–XBP1**, **ATF6**, with induction of chaperones, foldases, and **ERAD** machinery including **CRELD2**, **SYVN1**, **WFS1**, **ARMET**, **Fgf21** (rajpar2009targetedinductionof pages 1-2, cameron2011transcriptionalprofilingof pages 1-2, cameron2015xbp1independentuprpathways pages 1-2, patterson2014mechanismsandmodels pages 3-4) | Knock-in and transgenic mouse growth-plate studies; transcriptomics of microdissected hypertrophic zones (rajpar2009targetedinductionof pages 1-2, cameron2011transcriptionalprofilingof pages 1-2, cameron2015xbp1independentuprpathways pages 1-2) | In Y632X mice, **Xbp1s increased ~2-fold**; **Bip, Creld2, Chop** mRNAs and **Atf4** plus cleaved **Atf6a(N)** proteins increased; in embryonic N617K mice, homozygotes showed UPR at **E14.5**, delayed primary ossification at **E15.5**, and hypertrophic-zone expansion by **E17.5** (forouhan2018carbamazepinereducesdisease pages 4-7, kung2012hypertrophicchondrocyteshave pages 1-2) | DOI:10.1371/journal.pgen.1000691; DOI:10.1371/journal.pone.0024600; DOI:10.1371/journal.pgen.1005505; DOI:10.1002/dvdy.24131; DOI:10.1369/0022155412458436 | 2009; 2011; 2015; 2014; 2012 | https://doi.org/10.1371/journal.pgen.1000691 ; https://doi.org/10.1371/journal.pone.0024600 ; https://doi.org/10.1371/journal.pgen.1005505 ; https://doi.org/10.1002/dvdy.24131 ; https://doi.org/10.1369/0022155412458436 |
| Differentiation defect | ER-stressed hypertrophic chondrocytes survive but undergo impaired maturation: persistence of proliferative-like programs, suppression of hypertrophic differentiation, and dysregulation of **C/EBPβ**, **RUNX2**, **GADD45β**, **SOX9**; pathology is largely **XBP1-independent** and strongly linked to **PERK/ATF4/CHOP** signaling (cameron2011transcriptionalprofilingof pages 1-2, cameron2015xbp1independentuprpathways pages 1-2, wang2018inhibitingtheintegrated pages 1-2) | Transcriptomics and genetic epistasis in MCDS mice; PERK/ISR intervention studies (cameron2011transcriptionalprofilingof pages 1-2, cameron2015xbp1independentuprpathways pages 1-2, wang2018inhibitingtheintegrated pages 1-2) | Transcriptomic analysis identified **886 XBP1-dependent** vs **688 XBP1-independent** probes; genotype-phenotype severity was unchanged by cartilage-specific Xbp1 deletion, supporting redundancy of IRE1/XBP1 in MCDS; PERK inhibition prevented differentiation defects in vivo (cameron2015xbp1independentuprpathways pages 13-15, cameron2015xbp1independentuprpathways pages 1-2, wang2018inhibitingtheintegrated pages 1-2) | DOI:10.1371/journal.pone.0024600; DOI:10.1371/journal.pgen.1005505; DOI:10.7554/eLife.37673 | 2011; 2015; 2018 | https://doi.org/10.1371/journal.pone.0024600 ; https://doi.org/10.1371/journal.pgen.1005505 ; https://doi.org/10.7554/eLife.37673 |
| Tissue-level consequence | Defective hypertrophic maturation reduces **VEGF-mediated vascular invasion** of the growth plate and lowers **osteoclast recruitment** at the vascular invasion front, expanding the hypertrophic zone and delaying endochondral ossification (rajpar2009targetedinductionof pages 1-2, rellmann2018differentformsof pages 6-7) | Knock-in mouse and ER-stress transgenic mouse models; review synthesis of model findings (rajpar2009targetedinductionof pages 1-2, rellmann2018differentformsof pages 6-7) | In Y632X mice at 3 weeks, hypertrophic zone expanded **3.5-fold in wt/m** and **5-fold in m/m** animals; hip angle increased approximately **2-fold** in wt/m mice; CBZ later reduced HZ width by half (forouhan2018carbamazepinereducesdisease pages 4-7, forouhan2018carbamazepinereducesdisease pages 7-9) | DOI:10.1371/journal.pgen.1000691; DOI:10.1155/2018/8421394; DOI:10.1093/hmg/ddy253 | 2009; 2018; 2018 | https://doi.org/10.1371/journal.pgen.1000691 ; https://doi.org/10.1155/2018/8421394 ; https://doi.org/10.1093/hmg/ddy253 |
| Clinical phenotype | Core phenotypes reflect growth-plate dysfunction: short-limbed short stature, waddling gait, genu varum, lumbar lordosis, coxa vara, bowed femora/tibiae, enlarged capital femoral epiphyses, metaphyseal flaring/widening, usually normal intelligence and craniofacial appearance (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, richmond2024schmidmetaphysealchondrodysplasia pages 3-6, meng2026clinicalmolecularcharacteristics pages 8-9) | 2024 clinical review and 2026 literature-plus-cohort genotype-phenotype analysis (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, richmond2024schmidmetaphysealchondrodysplasia pages 3-6, meng2026clinicalmolecularcharacteristics pages 8-9) | Frequencies in aggregated clinical datasets: waddling gait **>80%** or **88.5%**, genu varum **>80%** or **83.6%**, short stature **>60%**, lumbar lordosis **>60%** or **51.6%**, coxa vara **50–80%** or **80.0%**, short femoral neck **81.7%**, bowed femurs/tibiae **81.5%**, enlarged capital femoral epiphysis **77.4%**; median age at first diagnosis **3.5 years** (richmond2024schmidmetaphysealchondrodysplasia pages 3-6, meng2026clinicalmolecularcharacteristics pages 8-9) | DOI:10.1007/978-1-60327-161-5_164; DOI:10.1007/s00223-025-01457-8 | 2024; 2026 | https://doi.org/10.1007/978-1-60327-161-5_164 ; https://doi.org/10.1007/s00223-025-01457-8 |
| Genotype–phenotype signal | Domain and mutation-class effects suggest earlier onset and greater severity for **NC1** and **missense** variants versus non-NC1/truncating variants, though older reviews note that firm genotype-phenotype rules remain incomplete (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, meng2026clinicalmolecularcharacteristics pages 8-9, wu2021characterizationofa pages 1-2) | Literature review and pooled case analysis (richmond2024schmidmetaphysealchondrodysplasia pages 6-8, meng2026clinicalmolecularcharacteristics pages 8-9, wu2021characterizationofa pages 1-2) | NC1 mutations associated with earlier onset: **12 vs 72 months** (**P=0.0014**); missense variants associated with lower height Z-score at presentation: **−3.62 ± 1.95 vs −1.99 ± 1.28** (**P=0.013**); distal radius/ulna metaphyseal irregularities more frequent with missense variants (**P=0.019**); last-evaluation height differed by NC1 status: **−5.58 ± 1.95 vs −2.61 ± 1.46** (**P=0.0001**) (meng2026clinicalmolecularcharacteristics pages 1-2, meng2026clinicalmolecularcharacteristics pages 8-9) | DOI:10.1007/978-1-60327-161-5_164; DOI:10.1007/s00223-025-01457-8; DOI:10.1002/mgg3.1668 | 2024; 2026; 2021 | https://doi.org/10.1007/978-1-60327-161-5_164 ; https://doi.org/10.1007/s00223-025-01457-8 ; https://doi.org/10.1002/mgg3.1668 |
| Recent 2024 development | A **medaka col10a1** model extends the disease mechanism beyond ER stress to include **loss of cell polarity** in chondrocytes and osteoblasts, with disorganized stacking and abnormal matrix secretion; ER stress reduction rescues polarity and skeletal shape (tan2024acollagen10a1mutation pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa) | 2024 animal model (medaka) with imaging, transcriptomics, TEM, and pharmacologic rescue (tan2024acollagen10a1mutation pages 1-2, tan2024acollagen10a1mutation media 7b4c3afa) | Heterozygous fish recapitulated MCDS-like defects; **10 mg/L carbamazepine** rescued ceratobranchial tortuosity and improved polarity-associated abnormalities; TEM showed swollen/fragmented RER in mutant chondrocytes and osteoblasts (tan2024acollagen10a1mutation media 7b4c3afa) | DOI:10.1016/j.isci.2024.109405 | 2024 | https://doi.org/10.1016/j.isci.2024.109405 |
| Therapeutic leverage point | Targeting proteostasis and ISR signaling can ameliorate disease in vivo: **carbamazepine (CBZ)** enhances mutant collagen X degradation and lowers UPR signaling; **ISR/PERK inhibition** lowers ATF4/CHOP-driven dedifferentiation and improves chondrodysplasia (briggs2020newdevelopmentsin pages 3-5, wang2018inhibitingtheintegrated pages 19-21, forouhan2018carbamazepinereducesdisease pages 7-9, wang2018inhibitingtheintegrated pages 1-2) | Mouse preclinical treatment studies; review noting clinical translation efforts (briggs2020newdevelopmentsin pages 3-5, forouhan2018carbamazepinereducesdisease pages 7-9, wang2018inhibitingtheintegrated pages 1-2) | In Y632X mice, oral **CBZ 250 mg/kg/day** increased femur/tibia growth, normalized hip geometry after **2 weeks**, reduced hypertrophic-zone width by **~50%**, lowered **Bip/Creld2/Chop**, suppressed **Xbp1** splicing, and reduced **Atf4** and cleaved **Atf6α**; ISRIB/chemical PERK inhibition improved phenotype in 13del mice, though rescue was incomplete (forouhan2018carbamazepinereducesdisease pages 7-9, wang2018inhibitingtheintegrated pages 21-22, wang2018inhibitingtheintegrated pages 1-2) | DOI:10.1093/hmg/ddy253; DOI:10.7554/eLife.37673; DOI:10.12688/f1000research.22275.1 | 2018; 2018; 2020 | https://doi.org/10.1093/hmg/ddy253 ; https://doi.org/10.7554/eLife.37673 ; https://doi.org/10.12688/f1000research.22275.1 |


*Table: This table summarizes the main mechanistic layers of Metaphyseal Chondrodysplasia, Schmid type, linking COL10A1 mutations to ER stress, disrupted hypertrophic differentiation, growth-plate pathology, clinical manifestations, and therapeutic intervention points. It integrates landmark mechanistic studies with recent clinical and 2024 animal-model updates.*

---

## Evidence items (PMID-preferred; otherwise DOI)
*Note: In the retrieved full texts above, PMIDs were not included in the tool outputs; therefore DOI-based identifiers are provided for unambiguous traceability.*
- Rajpar et al., PLoS Genetics, Oct 2009, DOI:10.1371/journal.pgen.1000691 (rajpar2009targetedinductionof pages 1-2)
- Cameron et al., PLoS ONE, Sep 2011, DOI:10.1371/journal.pone.0024600 (cameron2011transcriptionalprofilingof pages 1-2)
- Kung et al., J Histochem Cytochem, Oct 2012, DOI:10.1369/0022155412458436 (kung2012hypertrophicchondrocyteshave pages 1-2)
- Cameron et al., PLOS Genetics, Sep 2015, DOI:10.1371/journal.pgen.1005505 (cameron2015xbp1independentuprpathways pages 1-2)
- Wang et al., eLife, Jul 2018, DOI:10.7554/eLife.37673 (wang2018inhibitingtheintegrated pages 1-2)
- Forouhan et al., Hum Mol Genet, Jul 2018, DOI:10.1093/hmg/ddy253 (forouhan2018carbamazepinereducesdisease pages 7-9)
- Tan et al., iScience, Apr 2024, DOI:10.1016/j.isci.2024.109405 (tan2024acollagen10a1mutation media 7b4c3afa)
- Richmond & Savarirayan, (GeneReviews chapter as represented), 2024 update, DOI:10.1007/978-1-60327-161-5_164 (richmond2024schmidmetaphysealchondrodysplasia pages 10-12)



References

1. (ho2007col10a1nonsenseand pages 1-2): Matthew S.P. Ho, Kwok Yeung Tsang, Rebecca L.K. Lo, Miki Susic, Outi Mäkitie, Tori W.Y. Chan, Vivian C.W. Ng, David O. Sillence, Raymond P. Boot-Handford, Gary Gibson, Kenneth M.C. Cheung, William G. Cole, Kathryn S.E. Cheah, and Danny Chan. Col10a1 nonsense and frame-shift mutations have a gain-of-function effect on the growth plate in human and mouse metaphyseal chondrodysplasia type schmid. Human molecular genetics, 16 10:1201-15, May 2007. URL: https://doi.org/10.1093/hmg/ddm067, doi:10.1093/hmg/ddm067. This article has 77 citations and is from a domain leading peer-reviewed journal.

2. (richmond2024schmidmetaphysealchondrodysplasia pages 12-15): C. Richmond and R. Savarirayan. Schmid metaphyseal chondrodysplasia. ArXiv, pages 870-873, Oct 2024. URL: https://doi.org/10.1007/978-1-60327-161-5\_164, doi:10.1007/978-1-60327-161-5\_164. This article has 12 citations.

3. (richmond2024schmidmetaphysealchondrodysplasia pages 10-12): C. Richmond and R. Savarirayan. Schmid metaphyseal chondrodysplasia. ArXiv, pages 870-873, Oct 2024. URL: https://doi.org/10.1007/978-1-60327-161-5\_164, doi:10.1007/978-1-60327-161-5\_164. This article has 12 citations.

4. (richmond2024schmidmetaphysealchondrodysplasia pages 6-8): C. Richmond and R. Savarirayan. Schmid metaphyseal chondrodysplasia. ArXiv, pages 870-873, Oct 2024. URL: https://doi.org/10.1007/978-1-60327-161-5\_164, doi:10.1007/978-1-60327-161-5\_164. This article has 12 citations.

5. (meng2026clinicalmolecularcharacteristics pages 1-2): Lingyang Meng, Jing Hu, Lei Sun, Qian Zhang, Ou Wang, Yan Jiang, Xiaoping Xing, Weibo Xia, and Mei Li. Clinical, molecular characteristics, and genotype–phenotype relationships of metaphyseal chondrodysplasia type schmid. Calcified Tissue International, Dec 2026. URL: https://doi.org/10.1007/s00223-025-01457-8, doi:10.1007/s00223-025-01457-8. This article has 0 citations and is from a peer-reviewed journal.

6. (rajpar2009targetedinductionof pages 1-2): M. Helen Rajpar, Ben McDermott, Louise Kung, Rachel Eardley, Lynette Knowles, Mel Heeran, David J. Thornton, Richard Wilson, John F. Bateman, Richard Poulsom, Peter Arvan, Karl E. Kadler, Michael D. Briggs, and Raymond P. Boot-Handford. Targeted induction of endoplasmic reticulum stress induces cartilage pathology. PLoS Genetics, 5:e1000691, Oct 2009. URL: https://doi.org/10.1371/journal.pgen.1000691, doi:10.1371/journal.pgen.1000691. This article has 159 citations and is from a domain leading peer-reviewed journal.

7. (cameron2011transcriptionalprofilingof pages 1-2): Trevor L. Cameron, Katrina M. Bell, Liliana Tatarczuch, Eleanor J. Mackie, M. Helen Rajpar, Ben T. McDermott, Raymond P. Boot-Handford, and John F. Bateman. Transcriptional profiling of chondrodysplasia growth plate cartilage reveals adaptive er-stress networks that allow survival but disrupt hypertrophy. PLoS ONE, 6:e24600, Sep 2011. URL: https://doi.org/10.1371/journal.pone.0024600, doi:10.1371/journal.pone.0024600. This article has 77 citations and is from a peer-reviewed journal.

8. (wang2018inhibitingtheintegrated pages 1-2): Cheng Wang, Zhijia Tan, Ben Niu, Kwok Yeung Tsang, Andrew Tai, Wilson C W Chan, Rebecca L K Lo, Keith K H Leung, Nelson W F Dung, Nobuyuki Itoh, Michael Q Zhang, Danny Chan, and Kathryn Song Eng Cheah. Inhibiting the integrated stress response pathway prevents aberrant chondrocyte differentiation thereby alleviating chondrodysplasia. eLife, Jul 2018. URL: https://doi.org/10.7554/elife.37673, doi:10.7554/elife.37673. This article has 93 citations and is from a domain leading peer-reviewed journal.

9. (cameron2015xbp1independentuprpathways pages 1-2): Trevor L. Cameron, Katrina M. Bell, Irma L. Gresshoff, Lisa Sampurno, Lorna Mullan, Joerg Ermann, Laurie H. Glimcher, Raymond P. Boot-Handford, and John F. Bateman. Xbp1-independent upr pathways suppress c/ebp-β mediated chondrocyte differentiation in er-stress related skeletal disease. PLOS Genetics, 11:e1005505, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005505, doi:10.1371/journal.pgen.1005505. This article has 44 citations and is from a domain leading peer-reviewed journal.

10. (tan2024acollagen10a1mutation media 7b4c3afa): Wen Hui Tan, Martin Rücklin, Daria Larionova, Tran Bich Ngoc, Bertie Joan van Heuven, Federica Marone, Paul Matsudaira, and Christoph Winkler. A collagen10a1 mutation disrupts cell polarity in a medaka model for metaphyseal chondrodysplasia type schmid. iScience, 27:109405, Apr 2024. URL: https://doi.org/10.1016/j.isci.2024.109405, doi:10.1016/j.isci.2024.109405. This article has 2 citations and is from a peer-reviewed journal.

11. (forouhan2018carbamazepinereducesdisease pages 4-7): Mitra Forouhan, Stephan Sonntag, and Raymond P Boot-Handford. Carbamazepine reduces disease severity in a mouse model of metaphyseal chondrodysplasia type schmid caused by a premature stop codon (y632x) in the <i>col10a1</i> gene. Human Molecular Genetics, 27:3840-3853, Jul 2018. URL: https://doi.org/10.1093/hmg/ddy253, doi:10.1093/hmg/ddy253. This article has 28 citations and is from a domain leading peer-reviewed journal.

12. (forouhan2018carbamazepinereducesdisease pages 1-4): Mitra Forouhan, Stephan Sonntag, and Raymond P Boot-Handford. Carbamazepine reduces disease severity in a mouse model of metaphyseal chondrodysplasia type schmid caused by a premature stop codon (y632x) in the <i>col10a1</i> gene. Human Molecular Genetics, 27:3840-3853, Jul 2018. URL: https://doi.org/10.1093/hmg/ddy253, doi:10.1093/hmg/ddy253. This article has 28 citations and is from a domain leading peer-reviewed journal.

13. (tan2024acollagen10a1mutation pages 1-2): Wen Hui Tan, Martin Rücklin, Daria Larionova, Tran Bich Ngoc, Bertie Joan van Heuven, Federica Marone, Paul Matsudaira, and Christoph Winkler. A collagen10a1 mutation disrupts cell polarity in a medaka model for metaphyseal chondrodysplasia type schmid. iScience, 27:109405, Apr 2024. URL: https://doi.org/10.1016/j.isci.2024.109405, doi:10.1016/j.isci.2024.109405. This article has 2 citations and is from a peer-reviewed journal.

14. (forouhan2018carbamazepinereducesdisease pages 7-9): Mitra Forouhan, Stephan Sonntag, and Raymond P Boot-Handford. Carbamazepine reduces disease severity in a mouse model of metaphyseal chondrodysplasia type schmid caused by a premature stop codon (y632x) in the <i>col10a1</i> gene. Human Molecular Genetics, 27:3840-3853, Jul 2018. URL: https://doi.org/10.1093/hmg/ddy253, doi:10.1093/hmg/ddy253. This article has 28 citations and is from a domain leading peer-reviewed journal.

15. (wang2018inhibitingtheintegrated pages 21-22): Cheng Wang, Zhijia Tan, Ben Niu, Kwok Yeung Tsang, Andrew Tai, Wilson C W Chan, Rebecca L K Lo, Keith K H Leung, Nelson W F Dung, Nobuyuki Itoh, Michael Q Zhang, Danny Chan, and Kathryn Song Eng Cheah. Inhibiting the integrated stress response pathway prevents aberrant chondrocyte differentiation thereby alleviating chondrodysplasia. eLife, Jul 2018. URL: https://doi.org/10.7554/elife.37673, doi:10.7554/elife.37673. This article has 93 citations and is from a domain leading peer-reviewed journal.

16. (wang2018inhibitingtheintegrated pages 19-21): Cheng Wang, Zhijia Tan, Ben Niu, Kwok Yeung Tsang, Andrew Tai, Wilson C W Chan, Rebecca L K Lo, Keith K H Leung, Nelson W F Dung, Nobuyuki Itoh, Michael Q Zhang, Danny Chan, and Kathryn Song Eng Cheah. Inhibiting the integrated stress response pathway prevents aberrant chondrocyte differentiation thereby alleviating chondrodysplasia. eLife, Jul 2018. URL: https://doi.org/10.7554/elife.37673, doi:10.7554/elife.37673. This article has 93 citations and is from a domain leading peer-reviewed journal.

17. (kung2012hypertrophicchondrocyteshave pages 1-2): Louise H. W. Kung, M. Helen Rajpar, Michael D. Briggs, and Raymond P. Boot-Handford. Hypertrophic chondrocytes have a limited capacity to cope with increases in endoplasmic reticulum stress without triggering the unfolded protein response. Journal of Histochemistry and Cytochemistry, 60:734-748, Oct 2012. URL: https://doi.org/10.1369/0022155412458436, doi:10.1369/0022155412458436. This article has 18 citations and is from a peer-reviewed journal.

18. (richmond2024schmidmetaphysealchondrodysplasia pages 3-6): C. Richmond and R. Savarirayan. Schmid metaphyseal chondrodysplasia. ArXiv, pages 870-873, Oct 2024. URL: https://doi.org/10.1007/978-1-60327-161-5\_164, doi:10.1007/978-1-60327-161-5\_164. This article has 12 citations.

19. (patterson2014mechanismsandmodels pages 3-4): Sara E. Patterson and Caroline N. Dealy. Mechanisms and models of endoplasmic reticulum stress in chondrodysplasia. Developmental Dynamics, 243:875-893, Jul 2014. URL: https://doi.org/10.1002/dvdy.24131, doi:10.1002/dvdy.24131. This article has 41 citations and is from a peer-reviewed journal.

20. (meng2026clinicalmolecularcharacteristics pages 8-9): Lingyang Meng, Jing Hu, Lei Sun, Qian Zhang, Ou Wang, Yan Jiang, Xiaoping Xing, Weibo Xia, and Mei Li. Clinical, molecular characteristics, and genotype–phenotype relationships of metaphyseal chondrodysplasia type schmid. Calcified Tissue International, Dec 2026. URL: https://doi.org/10.1007/s00223-025-01457-8, doi:10.1007/s00223-025-01457-8. This article has 0 citations and is from a peer-reviewed journal.

21. (richmond2024schmidmetaphysealchondrodysplasia pages 1-3): C. Richmond and R. Savarirayan. Schmid metaphyseal chondrodysplasia. ArXiv, pages 870-873, Oct 2024. URL: https://doi.org/10.1007/978-1-60327-161-5\_164, doi:10.1007/978-1-60327-161-5\_164. This article has 12 citations.

22. (richmond2024schmidmetaphysealchondrodysplasia pages 8-10): C. Richmond and R. Savarirayan. Schmid metaphyseal chondrodysplasia. ArXiv, pages 870-873, Oct 2024. URL: https://doi.org/10.1007/978-1-60327-161-5\_164, doi:10.1007/978-1-60327-161-5\_164. This article has 12 citations.

23. (briggs2020newdevelopmentsin pages 3-5): Michael D. Briggs, Ella P. Dennis, Helen F. Dietmar, and Katarzyna A. Pirog. New developments in chondrocyte er stress and related diseases. F1000Research, 9:290, Apr 2020. URL: https://doi.org/10.12688/f1000research.22275.1, doi:10.12688/f1000research.22275.1. This article has 36 citations and is from a peer-reviewed journal.

24. (tan2024acollagen10a1mutation media 2ad256bd): Wen Hui Tan, Martin Rücklin, Daria Larionova, Tran Bich Ngoc, Bertie Joan van Heuven, Federica Marone, Paul Matsudaira, and Christoph Winkler. A collagen10a1 mutation disrupts cell polarity in a medaka model for metaphyseal chondrodysplasia type schmid. iScience, 27:109405, Apr 2024. URL: https://doi.org/10.1016/j.isci.2024.109405, doi:10.1016/j.isci.2024.109405. This article has 2 citations and is from a peer-reviewed journal.

25. (tan2024acollagen10a1mutation media c648ae69): Wen Hui Tan, Martin Rücklin, Daria Larionova, Tran Bich Ngoc, Bertie Joan van Heuven, Federica Marone, Paul Matsudaira, and Christoph Winkler. A collagen10a1 mutation disrupts cell polarity in a medaka model for metaphyseal chondrodysplasia type schmid. iScience, 27:109405, Apr 2024. URL: https://doi.org/10.1016/j.isci.2024.109405, doi:10.1016/j.isci.2024.109405. This article has 2 citations and is from a peer-reviewed journal.

26. (cameron2015xbp1independentuprpathways pages 13-15): Trevor L. Cameron, Katrina M. Bell, Irma L. Gresshoff, Lisa Sampurno, Lorna Mullan, Joerg Ermann, Laurie H. Glimcher, Raymond P. Boot-Handford, and John F. Bateman. Xbp1-independent upr pathways suppress c/ebp-β mediated chondrocyte differentiation in er-stress related skeletal disease. PLOS Genetics, 11:e1005505, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005505, doi:10.1371/journal.pgen.1005505. This article has 44 citations and is from a domain leading peer-reviewed journal.

27. (rellmann2018differentformsof pages 6-7): Yvonne Rellmann and Rita Dreier. Different forms of er stress in chondrocytes result in short stature disorders and degenerative cartilage diseases: new insights by cartilage-specific erp57 knockout mice. Oxidative Medicine and Cellular Longevity, Dec 2018. URL: https://doi.org/10.1155/2018/8421394, doi:10.1155/2018/8421394. This article has 27 citations.

28. (wu2021characterizationofa pages 1-2): Huixiao Wu, Shuping Wang, Guimei Li, Yangyang Yao, Ninguan Wang, Xiaoqing Sun, L. Fang, Xiu-yun Jiang, Jiajun Zhao, Yanzhou Wang, and Chao Xu. Characterization of a novel col10a1 variant associated with schmid‐type metaphyseal chondrodysplasia and a literature review. Molecular Genetics & Genomic Medicine, Mar 2021. URL: https://doi.org/10.1002/mgg3.1668, doi:10.1002/mgg3.1668. This article has 18 citations and is from a peer-reviewed journal.