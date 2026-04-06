# Plan: DisMech as Validation Resource for Causal Gene-to-Trait Analyses

## The Idea

Given outputs from causal modeling pipelines (GWAS + Perturb-seq → gene programs → traits), can dismech's curated pathophysiology knowledge **explain, validate, or contextualize** the discovered relationships?

This positions dismech as a **benchmark/interpretation layer** rather than a data store.

## Background: The Ota et al. Methodology

The paper ["Causal modelling of gene effects from regulators to programs to traits"](https://www.nature.com/articles/s41586-025-09866-3) (Ota et al., Nature 2025) builds causal graphs:

```
Gene (regulator) --[β]--> Program --[effect]--> Trait/Phenotype
                          ↑
Gene (member) ----[γ]----/
```

**Key data types:**
- **γ (gamma)**: Gene effect on trait from LoF burden tests (UK Biobank, 454K participants)
- **β (beta)**: Regulatory effect from Perturb-seq knockdowns (K562 cells, 9,498 genes)
- **Programs**: Co-expressed gene modules (60 identified via consensus NMF)

**Key outputs:**
- Program-trait effect sizes with directions
- Gene-program regulatory relationships
- Causal chains explaining how genes affect traits via biological programs
- 73% accuracy in predicting effect directions for top GWAS hits

## Use Cases for DisMech

### 1. Validate Discovered Gene-Program-Trait Relationships

**Question**: Does a computationally discovered pathway match curated knowledge?

| Pipeline Output | DisMech Query |
|-----------------|---------------|
| GATA1 → erythroid program → MCH | Do blood disorders document GATA1 affecting hemoglobin via erythropoiesis? |
| BCL2 → apoptosis program → lymphocyte count | Do immune disorders link BCL2 to apoptosis affecting lymphocytes? |

**Validation levels:**
- CONFIRMED: Gene, process, and phenotype all documented with evidence
- PARTIAL: Some elements present but incomplete chain
- NOVEL: Not in dismech (curation candidate)
- CONTRADICTED: Dismech documents opposite effect

### 2. Explain Programs via Pathophysiology

**Question**: What does "Program 17" actually mean in disease context?

Pipeline outputs are anonymous gene modules (Program 1, Program 2, ...). DisMech can provide clinical/mechanistic context:

| Program GO Annotation | DisMech Diseases | Clinical Context |
|-----------------------|------------------|------------------|
| GO:0007049 (cell cycle) | CML, Retinoblastoma | "Uncontrolled proliferation drives tumor growth" |
| GO:0006915 (apoptosis) | SLE, Autoimmune diseases | "Defective clearance of apoptotic cells triggers autoimmunity" |
| GO:0030218 (erythrocyte differentiation) | Sickle Cell, Thalassemia | "Ineffective erythropoiesis causes anemia" |

### 3. Prioritize Novel Findings

**Question**: Which discovered relationships are genuinely novel vs. already known?

Given 500 gene-trait associations from a pipeline, dismech can partition into:
- **Known**: Already documented (low priority for follow-up)
- **Novel**: Not in literature (high priority for experimental validation)
- **Contradicted**: Conflicts with literature (needs investigation)

### 4. Identify Mechanistic Gaps in DisMech

**Question**: Where does computational analysis find things missing from curated knowledge?

If pipeline discovers "Gene X → autophagy → Trait Y" but dismech's Disease Y entry lacks autophagy in pathophysiology, this flags a curation gap.

**Feedback loop**: Pipeline discoveries improve dismech coverage.

### 5. Cross-Disease Program Analysis

**Question**: Do different diseases share causal programs?

| Shared Program | Diseases | Implication |
|----------------|----------|-------------|
| Inflammation (GO:0006954) | RA, Crohn's, Psoriasis | Common therapeutic targets |
| Fibrosis (GO:0030198) | IPF, Liver Cirrhosis, Systemic Sclerosis | Shared mechanism despite different organs |

## Data Requirements

### From Ota et al. Pipeline

1. **Program definitions**: Gene lists per program + GO annotations
2. **Program-trait effects**: Effect sizes and directions for each program-trait pair
3. **Gene-program relationships**: Which genes regulate which programs (β values)
4. **Gene-trait effects**: Direct LoF burden test results (γ values)

*Note: Check if supplementary tables from paper are publicly available.*

### From DisMech

1. **Gene mentions**: Genes in `genetic` and `pathophysiology.genes` sections
2. **Process annotations**: GO terms in `pathophysiology.biological_processes`
3. **Phenotype annotations**: HP terms in `phenotypes`
4. **Cell type context**: CL terms in `pathophysiology.cell_types`
5. **Evidence**: PMIDs supporting each relationship

### Mapping Requirements

| Pipeline Entity | DisMech Entity | Mapping Strategy |
|-----------------|----------------|------------------|
| Gene symbol | GeneDescriptor | Direct match or HGNC lookup |
| Program GO term | BiologicalProcessTerm | Exact or ancestor match via GO hierarchy |
| Trait | Phenotype HP term | Manual curation of trait-to-HPO mappings |
| Cell type | CellTypeTerm | Match K562 → CL:0000255 (erythroid) |

## Evaluation Criteria

### Quantitative Metrics

1. **Coverage**: % of pipeline gene-trait pairs that dismech can evaluate
2. **Confirmation rate**: % of top pipeline hits confirmed by dismech
3. **Novelty rate**: % of pipeline discoveries not in dismech
4. **Contradiction rate**: % of pipeline results conflicting with dismech

### Qualitative Assessment

1. Do confirmed findings have strong evidence (experimental PMIDs)?
2. Are novel findings biologically plausible given dismech context?
3. Can contradictions be resolved by examining evidence quality?

## DisMech Gaps to Address

### Current Strengths
- 55+ disorders with curated pathophysiology
- GO/HP/CL term bindings enabling semantic matching
- Evidence with PMIDs for traceability
- Structured pathophysiology with biological processes and cell types

### Gaps

| Gap | Impact | Remediation |
|-----|--------|-------------|
| Inconsistent `modifier` usage | Cannot validate effect directions | Curation pass to add INCREASED/DECREASED |
| Genes often missing from pathophysiology | Low gene coverage | Add genes to pathophysiology entries |
| No explicit gene→process links | Cannot trace causal chains | Add `gene` slot to BiologicalProcessDescriptor |
| Blood disorders underrepresented | Poor coverage for Ota et al. test case | Prioritize Thalassemia, Polycythemia, etc. |

## Pilot: Blood Traits

The Ota et al. paper focuses on three blood traits:
- MCH (mean corpuscular hemoglobin)
- RDW (red cell distribution width)
- IRF (immature reticulocyte fraction)

### Relevant DisMech Disorders

| Disorder | Relevance | Current Coverage |
|----------|-----------|------------------|
| Sickle Cell Disease | Hemoglobin, erythrocytes | Good - has GO terms, cell types, evidence |
| Autoimmune Hemolytic Anemia | Hemolysis, RBC destruction | Moderate |
| Fanconi Anemia | Bone marrow failure | Moderate |
| G6PD Deficiency | RBC fragility | Check coverage |
| Hemochromatosis | Iron metabolism | Check coverage |

### Missing Disorders to Add

- Thalassemia (alpha and beta)
- Polycythemia vera
- Iron deficiency anemia
- Aplastic anemia
- Myelodysplastic syndromes

## Output Formats

### 1. Validation Report (per gene-program-trait)

```yaml
gene: GATA1
program: erythroid_differentiation
program_go: GO:0030218
trait: mean_corpuscular_hemoglobin
effect_direction: positive

validation:
  status: CONFIRMED
  matching_disorders:
    - disease: Sickle Cell Disease
      pathophysiology_entry: "Red Blood Cell Sickling"
      process_match: GO:0030218 (erythrocyte differentiation)
      gene_mentioned: false  # gap identified
      evidence: PMID:24277079
  confidence: MEDIUM
  notes: "Process confirmed, gene not explicitly mentioned"
  curation_action: "Add GATA1 to SCD pathophysiology"
```

### 2. Summary Statistics

```
Total pipeline relationships evaluated: 180
  - CONFIRMED: 73 (41%)
  - PARTIAL: 45 (25%)
  - NOVEL: 52 (29%)
  - CONTRADICTED: 10 (6%)

Coverage by program type:
  - Cell cycle programs: 85% evaluable
  - Erythroid programs: 92% evaluable
  - Autophagy programs: 34% evaluable (gap)
```

### 3. Curation Candidates

Ranked list of novel findings with high effect sizes that warrant adding to dismech.

### 4. Gap Report

Which GO terms from programs lack dismech coverage, prioritized by frequency in pipeline results.

## Implementation Phases

### Phase 1: Data Assembly
- Obtain Ota et al. supplementary data
- Export dismech blood disorders to queryable format
- Create trait-to-HPO mapping for MCH, RDW, IRF

### Phase 2: Proof of Concept
- Manual validation of 20 top gene-program-trait relationships
- Document matching logic and edge cases
- Assess dismech coverage and gaps

### Phase 3: Systematic Evaluation
- Automate matching across all pipeline outputs
- Generate validation report
- Quantify confirmation/novelty/contradiction rates

### Phase 4: Bidirectional Improvement
- Use novel findings to improve dismech coverage
- Re-run validation to measure improvement
- Publish methodology and results

## Open Questions

1. **Trait mapping**: How to map blood lab values (MCH) to HPO terms? Direct terms exist (HP:0025066 "Decreased mean corpuscular hemoglobin") but may need expert review.

2. **Cell type specificity**: Ota et al. used K562 (erythroleukemia line). How generalizable are programs to other cell types in dismech pathophysiology?

3. **Effect direction validation**: DisMech has `modifier` but it's underused. How much curation effort to systematically add directions?

4. **Semantic matching depth**: Should GO term matching use exact match, or traverse hierarchy (e.g., "erythrocyte differentiation" matches "hematopoiesis")?

5. **Evidence quality weighting**: Should we weight dismech evidence by experimental type (IDA > TAS > NAS)?

## References

- [Ota et al. Nature 2025](https://www.nature.com/articles/s41586-025-09866-3) - Main methodology
- [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2025.01.22.634424v1) - Open access version
- [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11785173/) - Full text with supplements

## Assets

- Paper PDF: `docs/assets/Causal modelling of gene effects from regulators to programs to traits.pdf`
- **Table S1**: `docs/assets/Ota_2025_TableS1.xlsx` - Program annotations (60 programs)
  - Curated annotations (e.g., "Hemoglobin synthesis", "Cell cycle (S phase)", "Autophagosome")
  - Representative GO terms
  - Top 10 genes per program
  - Representative transcription factors
- **Table S2**: `docs/assets/Ota_2025_TableS2.xlsx` - Trait definitions (54 traits)
  - RBC traits: MCH, MCV, RDW, reticulocyte count, hemoglobin, etc.
  - Other blood traits: platelet count, WBC, lymphocyte count, etc.
  - Serum biomarkers: albumin, cholesterol, glucose, bilirubin, etc.
  - Anthropometric: BMI, height, bone mineral density

### Key Programs for Blood Trait Validation

| Program | Annotation | GO Term | Relevance to DisMech |
|---------|------------|---------|----------------------|
| P4 | Cell cycle (S phase, DNA replication) | DNA replication | CML, Retinoblastoma |
| P6 | Cell cycle (G2M checkpoint) | G2M checkpoint | Cancers |
| P16 | Autophagosome | autophagosome | Neurodegeneration, inflammation |
| P27 | Platelet activation (Mega, IKZF1) | platelet activation | Immune thrombocytopenia |
| P28 | RBC (glycoproteins) | HEME_METABOLISM | Sickle Cell, Thalassemia |
| P35 | TNF signaling (stress response) | TNFA_SIGNALING_VIA_NFKB | Autoimmune diseases |
| P40 | Hemoglobin synthesis | HEME_METABOLISM | Sickle Cell, Thalassemia, Anemia |
| P45 | TNF signaling (apoptosis) | TNFA_SIGNALING_VIA_NFKB | SLE, RA |

### Data Not Yet Available

The bioRxiv preprint only includes Tables S1 and S2. Additional data mentioned in the paper:
- Table S3: Program-trait effect sizes (needed for quantitative validation)
- Gene-level burden test results (γ values)
- GitHub repository with analysis code (not yet public)

These may become available with the Nature publication or upon request to authors.
