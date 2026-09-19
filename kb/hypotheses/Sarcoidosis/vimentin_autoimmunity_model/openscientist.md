---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T16:30:47.637634'
end_time: '2026-07-31T16:53:24.856197'
duration_seconds: 1357.22
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Sarcoidosis
  category: Immune
  hypothesis_group_id: vimentin_autoimmunity_model
  hypothesis_label: Vimentin Autoantigen / HLA-DRB1*03 Autoimmunity Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: vimentin_autoimmunity_model\nhypothesis_label:\
    \ Vimentin Autoantigen / HLA-DRB1*03 Autoimmunity Model\nstatus: EMERGING\napplies_to_subtypes:\n\
    - Pulmonary Sarcoidosis\ndescription: 'An alternative to the persistent-microbial-antigen\
    \ premise: in a subset of patients - most\n  clearly the HLA-DRB1*03+ Lofgren\
    \ phenotype - the disease-defining antigen is a self-protein rather than\n  a\
    \ foreign one, with the cytoskeletal protein vimentin as the leading candidate\
    \ autoantigen. HLA-DRB1*03\n  presents vimentin-derived peptides to a strikingly\
    \ restricted CD4+ T-cell receptor repertoire (Valpha2.3/Vbeta22),\n  and linked\
    \ T- and B-cell autoreactivity to vimentin is demonstrable in situ in the sarcoid\
    \ lung. Under\n  this model sarcoidosis (or at least its resolving HLA-restricted\
    \ form) is better understood as an antigen-specific\n  autoimmune disease. It\
    \ is not mutually exclusive with the antigen-persistence model: molecular mimicry\n\
    \  between microbial proteins (e.g. mycobacterial) and vimentin could reconcile\
    \ the two, and it shares\n  the same downstream CD4+ T-cell activation and Th17.1\
    \ effector chain.'\nnotes: 'Held at EMERGING: the vimentin-autoantigen and HLA-DRB1*03/Valpha2.3-Vbeta22\
    \ associations are\n  well documented for pulmonary/Lofgren sarcoidosis, but vimentin\
    \ is not proven to be the (or a) universal\n  disease-initiating antigen, and\
    \ the model is best supported in HLA-DRB1*03+ patients rather than across\n  all\
    \ sarcoidosis.'\nevidence:\n- reference: PMID:30038611\n  reference_title: In\
    \ Situ Humoral Immunity to Vimentin in HLA-DRB1*03(+) Patients With Pulmonary\
    \ Sarcoidosis.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ Vimentin has been implicated in pulmonary sarcoidosis as a T-cell autoantigen\n\
    \  explanation: |\n    Directly establishes vimentin as an implicated T-cell autoantigen\
    \ in pulmonary sarcoidosis in the HLA-DRB1*03 / restricted-TCR / Lofgren context,\
    \ the central premise of this alternative hypothesis.\n- reference: PMID:30038611\n\
    \  reference_title: In Situ Humoral Immunity to Vimentin in HLA-DRB1*03(+) Patients\
    \ With Pulmonary Sarcoidosis.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: linked in situ recognition of vimentin by both T- and B-cells in HLA-DRB1*03+\
    \ sarcoidosis patients\n  explanation: |\n    Demonstrates coordinated T- and\
    \ B-cell autoreactivity to vimentin within the HLA-DRB1*03+ sarcoid lung, supporting\
    \ an antigen-specific autoimmune mechanism rather than a purely foreign-antigen\
    \ response."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Sarcoidosis
- **Category:** Immune

## Target Hypothesis
- **Hypothesis ID:** vimentin_autoimmunity_model
- **Hypothesis Label:** Vimentin Autoantigen / HLA-DRB1*03 Autoimmunity Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: vimentin_autoimmunity_model
hypothesis_label: Vimentin Autoantigen / HLA-DRB1*03 Autoimmunity Model
status: EMERGING
applies_to_subtypes:
- Pulmonary Sarcoidosis
description: 'An alternative to the persistent-microbial-antigen premise: in a subset of patients - most
  clearly the HLA-DRB1*03+ Lofgren phenotype - the disease-defining antigen is a self-protein rather than
  a foreign one, with the cytoskeletal protein vimentin as the leading candidate autoantigen. HLA-DRB1*03
  presents vimentin-derived peptides to a strikingly restricted CD4+ T-cell receptor repertoire (Valpha2.3/Vbeta22),
  and linked T- and B-cell autoreactivity to vimentin is demonstrable in situ in the sarcoid lung. Under
  this model sarcoidosis (or at least its resolving HLA-restricted form) is better understood as an antigen-specific
  autoimmune disease. It is not mutually exclusive with the antigen-persistence model: molecular mimicry
  between microbial proteins (e.g. mycobacterial) and vimentin could reconcile the two, and it shares
  the same downstream CD4+ T-cell activation and Th17.1 effector chain.'
notes: 'Held at EMERGING: the vimentin-autoantigen and HLA-DRB1*03/Valpha2.3-Vbeta22 associations are
  well documented for pulmonary/Lofgren sarcoidosis, but vimentin is not proven to be the (or a) universal
  disease-initiating antigen, and the model is best supported in HLA-DRB1*03+ patients rather than across
  all sarcoidosis.'
evidence:
- reference: PMID:30038611
  reference_title: In Situ Humoral Immunity to Vimentin in HLA-DRB1*03(+) Patients With Pulmonary Sarcoidosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Vimentin has been implicated in pulmonary sarcoidosis as a T-cell autoantigen
  explanation: |
    Directly establishes vimentin as an implicated T-cell autoantigen in pulmonary sarcoidosis in the HLA-DRB1*03 / restricted-TCR / Lofgren context, the central premise of this alternative hypothesis.
- reference: PMID:30038611
  reference_title: In Situ Humoral Immunity to Vimentin in HLA-DRB1*03(+) Patients With Pulmonary Sarcoidosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: linked in situ recognition of vimentin by both T- and B-cells in HLA-DRB1*03+ sarcoidosis patients
  explanation: |
    Demonstrates coordinated T- and B-cell autoreactivity to vimentin within the HLA-DRB1*03+ sarcoid lung, supporting an antigen-specific autoimmune mechanism rather than a purely foreign-antigen response.
```

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Mechanistic Hypothesis Search — Vimentin Autoantigen / HLA-DRB1*03 Autoimmunity Model in Sarcoidosis

**Disease:** Sarcoidosis (Immune)
**Hypothesis ID:** `vimentin_autoimmunity_model`
**KB Status:** EMERGING
**Report date:** 2026-07-31

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — retain at EMERGING, tightened to the HLA-DRB1*03+ Löfgren (self-resolving pulmonary) subtype.**

The Vimentin Autoantigen / HLA-DRB1\*03 Autoimmunity Model rests on an unusually convergent body of human evidence *within one subtype* of sarcoidosis. In HLA-DRB1\*03+ (DR3+) Löfgren's syndrome patients, the disease is characterized by a clonally restricted CD4+ T-cell expansion using the Vα2.3 (TRAV12-1) / Vβ22 (TRBV2) T-cell receptor; this restricted TCR docks onto an HLA-DRB1\*03-presented vimentin peptide, Vim429-443 (DSLPLVDTHSKRTLL); and the sarcoid lung shows **linked in-situ T- and B-cell autoreactivity** to the vimentin C-terminus. A mouse model in which vimentin immunization plus vimentin-bead challenge reproduces sarcoid-like lung granulomas supplies rare experimental (causal) support. On these grounds, the antigen-specific autoimmune framing of *this subtype* is genuinely well documented.

However, three lines of evidence prevent elevation beyond EMERGING and specifically block the model's claim to be a *universal* or *disease-initiating* mechanism. First, **vimentin is not the unique antigen**: the same DR3/AV2S3+ T cells respond to ATP synthase, lysyl-tRNA synthetase, and — critically — the microbial antigen mycobacterial catalase-peroxidase (mKatG), so a competing foreign-antigen model explains the same restricted TCR population. Second, **anti-vimentin autoreactivity is not sarcoidosis-specific** — the identical in-situ anti-vimentin B-cell phenomenon occurs in lupus nephritis, and anti-mutated-citrullinated-vimentin is an established rheumatoid arthritis marker — so vimentin is a poor "disease-defining" antigen. Third, and most tellingly, the seed hypothesis's proposed **molecular-mimicry bridge** between vimentin and mycobacterial proteins has **no linear-sequence support**: BLOSUM62 sliding-window scans of Vim429-443 against KatG, ESAT-6, and CFP-10 returned only background-level similarity (best 14.7% of self-score vs KatG).

The deepest conceptual caveat is the **resolution paradox**: HLA-DRB1\*03, the very allele that anchors the model, is a dominant *good-prognosis* allele that predicts spontaneous resolution. This is difficult to reconcile with classic chronic autoimmunity and instead suggests the mechanism is *antigen recognition coupled to effective clearance* rather than a self-perpetuating autoimmune attack. Combined with sarcoidosis genetics that extend beyond HLA class II into innate/apoptosis-autophagy genes (BTNL2, ANXA11), and with contradictory B-cell-depletion (rituximab) data, the most parsimonious reading is that the self-versus-foreign dichotomy is probably false, and a **defective-antigen-clearance** frame better accommodates all observations. Vimentin autoimmunity is a real, mechanistically detailed feature of DR3+ Löfgren sarcoidosis — but it is one facet of a shared antigen-presentation program, not the proven root cause of the disease.

---

## Key Findings

### F001 — HLA-DRB1*03 presents a specific vimentin peptide to a clonally restricted Vα2.3/Vβ22 CD4+ T-cell repertoire in Löfgren's sarcoidosis

The core molecular claim of the hypothesis is strongly documented. In bronchoalveolar lavage (BAL) studies of Löfgren's syndrome, **all HLA-DRB1\*03+ patients** showed simultaneous expression of the Vα2.3/Vβ22 TCR, and the accumulated lung T cells were highly clonal, carrying near-identical Vα2.3 sequences — the hallmark of an antigen-driven, oligoclonal response rather than a bystander expansion. Three-dimensional structural modelling demonstrated that the sarcoidosis-associated vimentin peptide **(Vim)429-443 DSLPLVDTHSKRTLL** fits both the HLA-DRB1\*03 peptide-binding cleft and the distinct contact features of this restricted TCR ([PMID: 26585430](https://pubmed.ncbi.nlm.nih.gov/26585430/)). Independent deep-sequencing confirmed the population-level, "public" nature of this repertoire: **TRAV12-1 (AV2S3) and TRBV2 (formerly BV22) were the most expanded V-region gene segments** in DR3+ Löfgren patients relative to controls, with shared public CDR3 motifs ([PMID: 28827283](https://pubmed.ncbi.nlm.nih.gov/28827283/)). Complementing this, elution of self-peptides from BAL HLA-DR molecules recovered vimentin among 78 presented self-peptides ([PMID: 17975675](https://pubmed.ncbi.nlm.nih.gov/17975675/)). This is the strongest direct evidence for the hypothesis — but note the same elution study also recovered **ATP synthase** and other well-known autoantigens, foreshadowing the specificity problem below.

### F002 — Linked in-situ T- and B-cell autoreactivity to the vimentin C-terminus in HLA-DRB1*03+ sarcoid lung

The seed evidence (PMID:30038611) is corroborated in detail. In a cohort of 48 sarcoidosis patients and 15 controls, the sarcoid lung — **especially in HLA-DRB1\*03+ patients** — contained vimentin-rich tertiary lymphoid structures. BAL fluid (BALF) was enriched for IgG and IgA anti-vimentin antibodies (AVAs), and **AVA titers correlated with the percentage of CD4+ T cells expressing the Vα2.3/Vβ22 TCR**, directly linking the humoral and cellular arms. Anti-C-terminal vimentin reactivity was selectively elevated in DRB1\*03+ BALF, and BALF AVA greatly exceeded serum levels, indicating **local (in-situ) antibody production** rather than passive transudation. The abstract states these studies reveal "linked in situ recognition of vimentin by both T- and B-cells in HLA-DRB1\*03+ sarcoidosis patients, associated with a selective humoral immune response to the vimentin C-terminus" ([PMID: 30038611](https://pubmed.ncbi.nlm.nih.gov/30038611/)). This coordinated T-/B-cell recognition of a single self-protein in the target organ is precisely the signature expected of an antigen-specific autoimmune process.

### F003 — Vimentin immunization plus vimentin-bead challenge reproduces sarcoidosis-like lung granulomas in mice (experimental causal support)

The model gains rare *causal* support from a mouse system. Sarcoidosis patients had higher frequency and levels of circulating anti-vimentin IgG than controls. Critically, **mice immunized with recombinant vimentin and then challenged intravenously with vimentin-coated beads developed lung granulomas** exhibiting Langhans and foreign-body giant cells, CD4 T cells, MHC-II+/Arg1+ macrophages, and upregulated *Ifng*, *Il17*, and *Tnfa* — a Th1/Th17 signature matching human sarcoid granulomas. The authors conclude these results "further validate vimentin as an autoantigen in sarcoidosis and provide evidence for an anti-vimentin immune response in disease pathogenesis" ([PMID: 35434591](https://pubmed.ncbi.nlm.nih.gov/35434591/)). This moves vimentin from a *correlate* to a *sufficient trigger* of sarcoid-like pathology in a model organism — the single most important piece of causal support, though a bead-challenge model does not establish that vimentin is the *initiating* antigen in spontaneous human disease.

### F004 — Competing/reconciling evidence: mycobacterial catalase-peroxidase (mKatG) engages the same AV2S3+/Löfgren T cells

A well-developed foreign-antigen model targets the same T-cell population. Mycobacterial catalase-peroxidase (mKatG) was detected in **5/9 sarcoid tissues vs 0/14 controls (p=0.0037)**, and anti-mKatG IgG was present in **12/25 patients vs 0/11 PPD-negative controls (p=0.0059)**; the authors concluded mKatG "is one target of the adaptive immune response driving granulomatous inflammation in sarcoidosis" ([PMID: 15753209](https://pubmed.ncbi.nlm.nih.gov/15753209/)). Crucially, mKatG stimulated higher IFN-γ responses in **AV2S3+** than AV2S3− T cells — i.e., the *same restricted TCR population* central to the vimentin model responds to a microbial antigen — and Löfgren/DR3+ patients showed elevated mKatG-driven IL-17. A parallel study confirmed strong T-cell responses to a vimentin peptide "in 6 out of 11 DRB1\*0301(pos) patients with active disease but not in patients with other HLA types," while the same work also identified ATP synthase and lysyl-tRNA synthetase responses ([PMID: 19786367](https://pubmed.ncbi.nlm.nih.gov/19786367/)). Thus multiple candidate antigens — self and microbial — converge on one DR3-restricted TCR, which is the central challenge to vimentin's claimed uniqueness.

### F005 & F007 — No linear-sequence molecular mimicry between vimentin Vim429-443 and canonical mycobacterial antigens (computational)

The seed hypothesis explicitly invokes molecular mimicry between microbial proteins and vimentin to reconcile the self- and foreign-antigen models. This bridge was tested directly and **failed**. A BLOSUM62 ungapped sliding-window scan of Vim429-443 (DSLPLVDTHSKRTLL; confirmed at vimentin UniProt P08670 residues 429-443) against the full *M. tuberculosis* KatG sequence (P9WIE5, 740 aa) found a best-scoring 15-mer (KatG629-643, GGLRVLGANYKRLPL) reaching only **11 of the epitope self-score of 75 (14.7%)**, with just 4/15 identical residues — background-level similarity (F005). Extending the analysis to ESAT-6 (EsxA, P9WNK7) and CFP-10 (EsxB, P9WNK5), the best windows scored only **7/75 (9.3%)** with ≤3/15 identity — *below* even the KatG best and at background level (F007). At the level of linear amino-acid sequence, there is no evidence for classical mimicry between the sarcoid vimentin epitope and the leading mycobacterial sarcoid antigens. (Caveat: this does not exclude *structural/conformational* mimicry or shared post-translational modification, which linear scans cannot detect.)

### F006 — Anti-vimentin autoreactivity is not sarcoidosis-specific

Vimentin fails a key test for a *disease-defining* antigen: specificity. In lupus, vimentin is "commonly targeted by in situ activated B-cells" in tubulointerstitial inflammation, and high serum IgG anti-vimentin antibodies **predict therapy-resistant lupus nephritis** (Kinloch/Clark 2020, TRIDOM n=99 + LUNAR n=132). Anti-mutated-citrullinated-vimentin (anti-MCV) is an established **rheumatoid arthritis** biomarker. Notably, the identical in-situ AVA phenomenon in sarcoidosis and lupus was reported by the same senior research group, underscoring that the readout is a shared feature of tissue inflammation rather than a sarcoidosis-specific mechanism. This substantially weakens the argument that vimentin is *the* disease-defining self-protein.

### F008 — Sarcoidosis genetic architecture extends beyond HLA class II

A pure antigen-presentation autoimmune framing is qualified by genetics. The **BTNL2** splice-site variant rs2076530 is described as an HLA-independent susceptibility factor (Szyld 2006), and variants in **ANXA11** (annexin A11; apoptosis/autophagy) and **RAB23** associate with sarcoidosis and its ocular subtype (Davoudi 2018: rs1040461/RAB23 and rs61860052/ANXA11, p≈0.01 after correction). While HLA-DRB1 class II remains the dominant susceptibility signal, the involvement of innate-immunity and apoptosis/autophagy genes points to defective clearance and innate dysregulation as parallel contributors — consistent with the defective-clearance reframing.

### F009 — The resolution paradox: HLA-DRB1*03 predicts GOOD prognosis / spontaneous resolution

This is the most conceptually important finding. In a large cohort (n=754: 302 Löfgren, 452 non-Löfgren; 1366 controls), the HLA-DRB1 distribution differed dramatically between Löfgren and non-Löfgren disease (**p=4×10⁻³⁶**). Critically, **DRB1\*01 and DRB1\*03 protected against non-resolving disease**, while DRB1\*07/14/15 associated with it, and "the clinical influence of DRB1\*03 (good prognosis) dominated over that of DRB1\*15 (bad prognosis)" ([PMID: 20187937](https://pubmed.ncbi.nlm.nih.gov/20187937/)). The allele that anchors the vimentin-autoimmunity model therefore marks the *self-resolving* phenotype — a striking mismatch with classic chronic autoimmunity, where autoantigen-driven responses tend to perpetuate disease. This supports reframing the mechanism as **antigen recognition coupled to effective clearance/resolution** rather than a persistent autoimmune attack. It is consistent with reports that Löfgren/DR3+ IL-17 responders recover, and that vimentin-Th17.1 responses feature in acute rather than chronic sarcoidosis.

### F010 — B-cell-depletion evidence is limited and contradictory

If anti-vimentin humoral autoimmunity were causally central, B-cell depletion should help. The evidence is unresolved. Rituximab in refractory pulmonary sarcoidosis has produced only partial/variable responses in small open-label series (e.g., PMIDs 34320381, 26330764). Paradoxically, **rituximab-induced sarcoidosis** has been reported after B-cell depletion for pemphigus vulgaris, which the authors interpret as "further support for an important role of B cells in the pathogenesis of sarcoidosis" ([PMID: 26800651](https://pubmed.ncbi.nlm.nih.gov/26800651/)) — i.e., B-cell depletion can *cause* sarcoid granulomas. The humoral arm's causal role is thus not straightforwardly therapeutic, leaving the direction of causation for anti-vimentin antibodies unresolved.

---

## Mechanistic Model / Interpretation

The hypothesis implies the following causal chain. Below, each link is annotated with the strength of literature support.

```
[Unknown initiating event]
        │  (STRENGTH: weak — trigger unproven; self vs foreign unresolved)
        ▼
Exposure/processing of vimentin (± citrullination / C-terminal modification)
        │  (MODERATE — vimentin peptides eluted from BAL HLA-DR; F001)
        ▼
HLA-DRB1*03 presents Vim429-443 (DSLPLVDTHSKRTLL)
        │  (STRONG — structural docking + elution; F001)
        ▼
Clonal Vα2.3(TRAV12-1)/Vβ22(TRBV2) CD4+ T-cell expansion in lung
        │  (STRONG — all DR3+ LS patients; deep-sequenced public repertoire; F001)
        ▼
Th1/Th17.1 effector program (IFN-γ, IL-17) + tertiary lymphoid structures
        │  (STRONG in human lung + mouse model; F002/F003)
        ▼
Linked in-situ B-cell help → local anti-vimentin (C-terminal) IgG/IgA
        │  (MODERATE — correlation with TCR+ fraction, local production; F002)
        ▼
Granuloma formation (CD4 T cells, MHC-II+/Arg1+ macrophages, giant cells)
        │  (MODERATE-STRONG — reproduced by vimentin immunization in mice; F003)
        ▼
Pulmonary sarcoidosis — predominantly the RESOLVING Löfgren phenotype
           (PARADOX — DR3 predicts resolution, not chronicity; F009)
```

**Where the literature is strong:** the middle of the chain — HLA-DRB1\*03 presentation of a defined vimentin peptide to a public, clonally restricted TCR, with linked T-/B-cell autoreactivity in the target organ, and mouse-causal reproduction of granulomas.

**Where links are inferred or missing:** (1) the *initiating event* — what first exposes/modifies vimentin, and whether it is self, foreign, or damage-associated — is unknown; (2) the *self-vs-foreign* reconciliation via molecular mimicry is **unsupported at the sequence level** (F005/F007); (3) the *direction of causation* for anti-vimentin antibodies (driver vs biomarker of tissue damage) is unresolved (F010); and (4) the mechanistic link between an autoimmune framing and the *good-prognosis/resolving* clinical outcome (F009) is unexplained by classic autoimmunity.

**Most parsimonious synthesis:** Rather than "self-antigen vimentin *vs* foreign-antigen mKatG," the data fit a **shared antigen-presentation program** in which a DR3-restricted public TCR recognizes *multiple* structurally accommodated peptides (vimentin, ATP synthase, lysyl-tRNA synthetase, mKatG). Vimentin is a genuine and prominent autoantigen in DR3+ Löfgren disease, but likely acts within a **defective-clearance / effective-resolution** framework — the DR3-restricted response mounts a vigorous, self-limiting Th17.1 reaction that clears antigen and resolves. This reconciles the autoimmune molecular detail (F001–F003) with the resolution paradox (F009) and the non-specificity of the antibody (F006) without requiring vimentin to be the unique disease initiator.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [26585430](https://pubmed.ncbi.nlm.nih.gov/26585430/) | Human clinical + computational | **Supports** | DR3 presents Vim429-443 to restricted TCR | Vim429-443 fits DR3 cleft and TCR contacts; all DR3+ patients express Vα2.3/Vβ22 | DR3+ Löfgren, BAL | High for structure; modelling-based docking |
| [28827283](https://pubmed.ncbi.nlm.nih.gov/28827283/) | Human clinical | **Supports** | Public restricted TCR repertoire | TRAV12-1 & TRBV2 most expanded in DR3+ LS; shared CDR3 | DR3+ Löfgren | High; does not prove antigen identity |
| [17975675](https://pubmed.ncbi.nlm.nih.gov/17975675/) | Human clinical | **Qualifies** | Vimentin physically presented on BAL HLA-DR | Vimentin among 78 eluted self-peptides — but so was ATP synthase | DRB1*0301+ | High for presentation; not vimentin-unique |
| [30038611](https://pubmed.ncbi.nlm.nih.gov/30038611/) | Human clinical | **Supports** (seed) | Linked in-situ T-/B-cell anti-vimentin autoreactivity | AVA correlates with Vα2.3/Vβ22 fraction; local C-terminal AVA production | DR3+ pulmonary | High; correlation, not causation |
| [35434591](https://pubmed.ncbi.nlm.nih.gov/35434591/) | Model organism | **Supports** | Anti-vimentin immunity causes granulomas | Vimentin immunization + bead challenge → sarcoid-like lung granulomas, Th1/Th17 | Mouse model | Moderate-high causal; bead model ≠ spontaneous disease |
| [15753209](https://pubmed.ncbi.nlm.nih.gov/15753209/) | Human clinical | **Competing** | mKatG is a sarcoid tissue antigen | mKatG in 5/9 tissues (p=0.0037); anti-mKatG IgG 12/25 (p=0.0059) | Sarcoid tissue | High; foreign-antigen alternative |
| [19786367](https://pubmed.ncbi.nlm.nih.gov/19786367/) | Human clinical | **Qualifies / competing** | HLA-restricted multi-antigen T-cell reactivity | Vimentin response in 6/11 DRB1*0301+; also ATP synthase, lysyl-tRNA synthetase | DR3+ active disease | High; shows multiple antigens |
| F005 (this work) | Computational | **Refutes** (mimicry bridge) | Vim429-443 ↔ KatG linear mimicry | Best window 14.7% of self-score, 4/15 identity | Sequence analysis | High for linear; cannot exclude conformational mimicry |
| F007 (this work) | Computational | **Refutes** (mimicry bridge) | Vim429-443 ↔ ESAT-6/CFP-10 mimicry | Best 9.3%, ≤3/15 identity — background | Sequence analysis | High for linear only |
| Kinloch/Clark 2020 (Lupus; TRIDOM/LUNAR) | Human clinical | **Qualifies** | Anti-vimentin specificity | In-situ AVA & serum AVA also in lupus nephritis; anti-MCV in RA | Lupus/RA | High; undermines disease-specificity |
| Szyld 2006 / Davoudi 2018 | Human clinical (genetics) | **Qualifies** | Genetics beyond HLA class II | BTNL2 (HLA-independent), ANXA11, RAB23 associations | Sarcoidosis / ocular | Moderate; points to innate/clearance genes |
| [20187937](https://pubmed.ncbi.nlm.nih.gov/20187937/) | Human clinical (genetics) | **Qualifies / paradox** | DR3 prognosis | DR3 protects against non-resolving disease; dominates DR15 | LS vs non-LS (n=754) | High; central paradox |
| [26800651](https://pubmed.ncbi.nlm.nih.gov/26800651/) | Human clinical (case) | **Qualifies** | B-cell causal role | Rituximab-induced sarcoidosis after B-cell depletion | Pemphigus→sarcoid | Low-moderate; case-level, paradoxical |

**Narrative.** The **strongest direct support** is a tightly interlocking set of human immunology studies from the Karolinska (Grunewald/Wahlström/Eklund) and Kinloch/Clark programs: structural and repertoire data placing a specific vimentin peptide at the center of a public DR3-restricted TCR response ([26585430](https://pubmed.ncbi.nlm.nih.gov/26585430/), [28827283](https://pubmed.ncbi.nlm.nih.gov/28827283/), [17975675](https://pubmed.ncbi.nlm.nih.gov/17975675/)), plus in-situ demonstration of linked T-/B-cell anti-vimentin autoreactivity in the lung ([30038611](https://pubmed.ncbi.nlm.nih.gov/30038611/)). The unique **causal** contribution is the vimentin-immunization mouse granuloma model ([35434591](https://pubmed.ncbi.nlm.nih.gov/35434591/)). The **strongest challenges** are the mKatG foreign-antigen literature ([15753209](https://pubmed.ncbi.nlm.nih.gov/15753209/), [19786367](https://pubmed.ncbi.nlm.nih.gov/19786367/)), the non-specificity of anti-vimentin autoimmunity across lupus and RA (Kinloch/Clark 2020), the computational refutation of the linear molecular-mimicry bridge (F005/F007), and the DR3 good-prognosis paradox ([20187937](https://pubmed.ncbi.nlm.nih.gov/20187937/)). These do not refute vimentin autoreactivity — they refute its claims to *uniqueness*, *disease-specificity*, and a *chronic-autoimmune* framing, and dissolve the seed's self/foreign reconciliation.

---

## Limitations and Knowledge Gaps

| # | Gap / scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| G1 | **Initiating event unknown** — no proven trigger that first exposes/modifies vimentin | The whole causal chain hangs on an unspecified upstream node | Literature reviewed; no proven initiator | Longitudinal pre-symptomatic cohorts; environmental/microbial exposure mapping at onset |
| G2 | **Molecular-mimicry bridge unsupported (linear)** — self/foreign reconciliation fails at sequence level | Seed hypothesis explicitly relies on mimicry to unify models | BLOSUM62 scans vs KatG, ESAT-6, CFP-10 (F005/F007) | Structural/conformational mimicry assays; TCR cross-reactivity tetramer studies; test citrullinated/PTM epitopes |
| G3 | **Vimentin not proven unique or initiating** — ATP synthase, lysyl-tRNA synthetase, mKatG engage same TCR | Undercuts "disease-defining antigen" claim | Elution & T-cell reactivity studies (F001/F004) | Quantitative antigen-ranking with DR3 tetramers across a large DR3+ cohort |
| G4 | **Antibody direction of causation** — driver vs damage biomarker | Determines whether humoral autoimmunity is mechanistic | Rituximab series + paradoxical case (F010) | Adequately powered RCT of B-cell depletion in DR3+ Löfgren; longitudinal AVA vs disease activity |
| G5 | **Resolution paradox unexplained** — DR3 = good prognosis | Contradicts classic autoimmunity framing | HLA-prognosis cohort (F009) | Mechanistic study linking DR3-restricted response to resolution (Treg induction, antigen-clearance kinetics) |
| G6 | **Specificity absence** — AVA shared with lupus/RA | Weakens biomarker/curation value | Cross-disease literature (F006) | Head-to-head AVA epitope-mapping across sarcoid vs lupus vs RA |
| G7 | **Data/source absences** — no GenCC/ClinGen gene-disease validity for VIM–sarcoidosis; no vimentin-antigen omics/trial dataset located | Curation cannot cite a structured source | Search of KB-relevant sources during iterations | Targeted omics (single-cell BAL TCR+antigen); registered trials stratified by DR3 |

---

## Alternative Models

1. **Persistent-microbial-antigen model (mKatG / mycobacterial)** — *Competing / possibly upstream.* mKatG is present in sarcoid tissue and drives the same AV2S3+ Th1/Th17 response ([15753209](https://pubmed.ncbi.nlm.nih.gov/15753209/)). It is a direct alternative to a self-antigen initiator and could be upstream if microbial antigen deposition seeds the response. The mimicry bridge that would unify it with vimentin is unsupported at sequence level (F005/F007).

2. **Multi-antigen shared-presentation model** — *More parsimonious integration.* The DR3-restricted public TCR accommodates several structurally similar peptides (vimentin, ATP synthase, lysyl-tRNA synthetase, mKatG). Vimentin is one prominent member, not the unique cause. This best explains F001 and F004 together.

3. **Defective-antigen-clearance / effective-resolution model** — *Parallel / reframing.* Supported by BTNL2/ANXA11/RAB23 (autophagy/apoptosis) genetics (F008) and the DR3 good-prognosis paradox (F009). Reframes DR3-restricted responses as vigorous but self-limiting clearance rather than chronic autoimmunity; accommodates the resolving Löfgren phenotype.

4. **Th17.1 effector-convergence model** — *Downstream consequence.* Both self- and foreign-antigen routes converge on IFN-γ/IL-17 Th17.1 granuloma biology; shared by all models and not discriminating on its own.

5. **B-cell/humoral-autoimmunity model** — *Downstream / uncertain-direction.* Linked in-situ AVA (F002) is real, but rituximab data are contradictory (F010), so this arm may be a consequence of, rather than a driver of, granulomatous inflammation.

---

## Discriminating Tests (Proposed Follow-up Experiments)

| Test | Stratification | Sample / system | Perturbation / readout | Expected result if vimentin model true | Discriminates against |
|---|---|---|---|---|---|
| **DR3 tetramer antigen ranking** | DR3+ Löfgren vs DR3+ non-Löfgren vs DR3+ healthy | BAL + blood CD4 T cells | DR3 tetramers loaded with vimentin, ATP synthase, lysyl-tRNA synthetase, mKatG peptides; quantify frequency/avidity | Vimentin-tetramer+ cells dominate and track disease | Multi-antigen / mKatG models (G3) |
| **TCR cross-reactivity assay** | DR3+ public-TCR clones | In vitro (transduced TCRs) | Challenge a single AV2S3/BV22 clone with vimentin vs mKatG peptides | Genuine cross-reactivity would rescue mimicry despite no linear homology | Mimicry bridge (G2) |
| **B-cell depletion RCT** | DR3+ Löfgren, AVA-high | Randomized rituximab vs placebo | AVA titer, TCR+ fraction, resolution rate | AVA reduction accelerates resolution | Antibody-direction gap (G4) |
| **Longitudinal onset cohort** | New-onset, pre-treatment, HLA-typed | Serial BAL/serum | Track antigen reactivity, AVA, clearance kinetics vs outcome | Vimentin response precedes and predicts resolution | Initiating-event & resolution paradox (G1/G5) |
| **Cross-disease epitope mapping** | Sarcoid vs lupus nephritis vs RA | Serum/tissue | Fine-map anti-vimentin epitopes (C-terminal vs citrullinated) | Sarcoid-restricted C-terminal epitope distinct from lupus/RA | Specificity gap (G6) |
| **Conformational/PTM mimicry screen** | — | Structural + MS | Test citrullinated/structural vimentin vs mycobacterial epitopes | Shared conformation/PTM despite no linear homology | Mimicry gap (G2) |

---

## Curation Leads (require curator verification)

**Candidate evidence references + exact snippets to verify against stored abstracts:**
- `PMID:26585430` — "a previously identified, sarcoidosis-associated vimentin peptide, (Vim)429-443 DSLPLVDTHSKRTLL, matching both the HLA peptide-binding cleft and distinct T-cell receptor features" (SUPPORT, HUMAN_CLINICAL).
- `PMID:28827283` — "TRAV12-1 and TRBV2 (formerly BV22) were the most expanded V region gene segments in DR3+ LS patients relative to control subjects" (SUPPORT, HUMAN_CLINICAL).
- `PMID:17975675` — "some of which were well-known autoantigens such as vimentin and ATP synthase" (QUALIFY — vimentin presented but not unique).
- `PMID:35434591` — "Vimentin-immunized mice developed lung granulomas following intravenous challenge with vimentin-coated beads"; "these results further validate vimentin as an autoantigen in sarcoidosis and provide evidence for an anti-vimentin immune response in disease pathogenesis" (SUPPORT, MODEL_ORGANISM).
- `PMID:15753209` — "suggesting that remnant mycobacterial catalase-peroxidase is one target of the adaptive immune response driving granulomatous inflammation in sarcoidosis" (COMPETING, HUMAN_CLINICAL).
- `PMID:19786367` — "strong T cell responses to a peptide derived from the cytoskeletal protein vimentin in 6 out of 11 DRB1\*0301(pos) patients with active disease but not in patients with other HLA types" (QUALIFY/COMPETING).
- `PMID:20187937` — "DRB1\*01 and DRB1\*03 protected against, a non-resolving disease"; "the clinical influence of DRB1\*03 (good prognosis) dominated over that of DRB1\*15 (bad prognosis)" (QUALIFY — resolution paradox).
- `PMID:26800651` — "rituximab-induced sarcoidal granulomas may be a rare adverse effect of treatment with this medication, providing further support for an important role of B cells in the pathogenesis of sarcoidosis" (QUALIFY — B-cell paradox).

**Candidate pathophysiology nodes/edges:**
- Node: `Vimentin (VIM, UniProt P08670)` autoantigen; epitope `Vim429-443 DSLPLVDTHSKRTLL`.
- Edge: `HLA-DRB1*03 —presents→ Vim429-443` (STRONG, DR3+ Löfgren).
- Edge: `Vim429-443 —activates→ Vα2.3(TRAV12-1)/Vβ22(TRBV2) CD4+ T cell` (STRONG).
- Edge: `restricted CD4 T cell —helps→ in-situ anti-vimentin B cell / AVA` (MODERATE).
- Edge: `anti-vimentin immunity —causes→ lung granuloma` (MODEL_ORGANISM only).
- Edge (REFUTED — mark as such): `Vim429-443 ↔ mKatG/ESAT-6/CFP-10 linear mimicry` — no support.
- Competing node/edge: `mKatG —activates→ AV2S3+ CD4 T cell` (COMPETING).

**Candidate ontology terms:** CD4+ T cell (CL:0000624); alveolar macrophage; MHC-II+ Arg1+ macrophage; tertiary lymphoid structure; granuloma; biological processes — antigen processing and presentation of peptide antigen via MHC class II (GO:0019886), T-cell receptor signaling pathway, Th17 cell differentiation (GO:0072539), autophagy (GO:0006914; via ANXA11).

**Candidate subtype restriction / status:** Restrict applicability from "Pulmonary Sarcoidosis" to **"HLA-DRB1\*03+ Löfgren's syndrome (self-resolving pulmonary sarcoidosis)."** Retain **status: EMERGING**. Add note that vimentin is *a* prominent autoantigen, not proven *unique/initiating*.

**Candidate `knowledge_gaps` / discussion prompts:**
- "Molecular-mimicry bridge to mycobacterial antigens is unsupported at linear-sequence level (BLOSUM62 vs KatG/ESAT-6/CFP-10 background); the self-vs-foreign dichotomy may be false."
- "DR3 marks good-prognosis/resolving disease — reconcile autoimmune framing with spontaneous resolution."
- "Anti-vimentin autoreactivity is shared with lupus nephritis and RA; not sarcoidosis-specific."
- "Direction of causation for anti-vimentin antibodies unresolved; rituximab data contradictory (can even induce sarcoidosis)."
- "Source absence: no GenCC/ClinGen VIM–sarcoidosis gene-disease validity entry and no vimentin-antigen omics/trial dataset located as of 2026-07-31."

---

## Conclusion

Vimentin autoimmunity is a genuine, mechanistically detailed phenomenon in **HLA-DRB1\*03+ Löfgren's sarcoidosis**, supported by convergent human immunology and rare mouse-causal evidence. But it is best understood as **one antigen within a shared DR3-restricted antigen-presentation program**, not as the unique or disease-initiating trigger. The seed hypothesis's molecular-mimicry reconciliation with mycobacterial antigens is unsupported at the sequence level, anti-vimentin antibodies are non-specific, and the DR3 good-prognosis paradox favors a **defective-clearance / effective-resolution** reframing. The hypothesis should remain **EMERGING**, with its scope tightened to the DR3+ Löfgren subtype and explicit knowledge gaps flagged for curation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)