# From evidence pointers to experiment-grounded evidence — a worked example on Familial Hypercholesterolemia

**Date:** 2026-07-30
**Status:** design exploration / proposal (not yet a schema change)
**Scope:** the dismech `EvidenceItem` model, illustrated on `kb/disorders/Familial_Hypercholesterolemia.yaml`

---

## 1. The question

Is the dismech evidence model *about evidence*, or is it mostly a set of guardrails
against AI hallucination? Today an `EvidenceItem` carries seven fields:

```yaml
evidence:
- reference: PMID:1301956            # a real, resolvable ID
  reference_title: "..."
  supports: SUPPORT                  # polarity: SUPPORT/REFUTE/PARTIAL/NO_EVIDENCE/WRONG_STATEMENT
  evidence_source: HUMAN_CLINICAL    # provenance-of-organism, coarse
  snippet: "..."                     # an EXACT quote, validated as a substring of the cited text
  explanation: "..."                 # curator prose
  images: [...]
```

The load-bearing machinery is `reference` + `snippet` + the `linkml-reference-validator`
pipeline, and its job is to answer **"is this citation real, and does the quoted text
actually exist in it?"** That is *citation integrity*. It is necessary and it is dismech's
primary defense against fabrication — but it is not *evidence appraisal*. Two fields
gesture at evidence semantics and both are thin:

- `supports` encodes **direction, not strength**. A single case report and a human
  natural-knockout study both collapse to `SUPPORT`.
- `evidence_source` encodes **study *type*, not study *design* or *inferential power***.
  Every human observation from an n=1 case report to a 27,000-patient trial is one value.

Nothing records **what experiment was run, what was measured, what resulted, or how the
mechanistic claim was inferred from that result.** That is the gap this document explores,
using FH — arguably the best-evidenced disease mechanism in all of human biology.

---

## 2. Two real anchors already in the FH file

### 2a. The mis-targeting problem (evidence pointer ≠ evidence for *this* edge)

Two monogenic head-nodes — `APOB-LDLR Binding Defect` and `PCSK9 Gain-of-Function` — are
**each supported by the same GeneReviews sentence** (`PMID:24404629`, which appears four
times in the file: node-level and edge-level on both nodes):

> "The molecular diagnosis of FH can be established by identification of heterozygous or
> biallelic pathogenic variants in APOB (variants that impair binding of LDL-C to the LDL
> receptor), LDLR, or PCSK9 (gain of function); or rarely, identification of biallelic
> pathogenic variants in LDLRAP1."

That snippet **validates** every time — it is a real quote. For the **APOB** node it is
arguably on-target: the parenthetical "(variants that impair binding of LDL-C to the LDL
receptor)" states exactly the binding-defect mechanism that node claims. But for the
`PCSK9 Gain-of-Function → PCSK9-mediated LDLR degradation` edge the same sentence is a
*diagnostic-classification* statement — it says PCSK9 gain-of-function is a gene you
sequence to diagnose FH, and says **nothing about degradation**, the actual mechanism on
that edge. That is the mis-targeting: a valid quote standing in for mechanism evidence it
does not contain. (The `LDLRAP1-Related LDL Uptake Defect` node, by contrast, does *not*
use this sentence — it cites LDLRAP1-specific evidence, `DOI:10.3390/ijms24043224`, and is
correctly targeted.) The PCSK9 edge is the clean, unambiguous example, and the one this
document builds on.

### 2b. The experiment is *already in the prose* — just not structured

On the `PCSK9` genetic entry (its `genetic:` block) sits a genuinely mechanistic, already-validated
snippet:

```yaml
- reference: DOI:10.1073/pnas.0409736102
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: "Overexpression of PCSK9 in HepG2 cells caused a decrease in whole-cell and
    cell-surface LDLR levels. PCSK9 overexpression had no effect on LDLR synthesis but
    caused a dramatic increase in the degradation of the mature LDLR"
```

Read what that one string actually contains:

| Experiment dimension | Value carried in the snippet |
|---|---|
| **System** | HepG2 cells (hepatocyte-like) |
| **Perturbation** | PCSK9 overexpression — a *gain-of-function* manipulation |
| **Readout** | whole-cell + cell-surface LDLR level; LDLR synthesis; LDLR degradation |
| **Result** | LDLR ↓; synthesis unchanged; degradation ↑ |
| **Inference** | PCSK9 acts *post-translationally* to increase LDLR degradation → *sufficiency* + localizes the mechanism to degradation, not synthesis |

Every one of those dimensions is present — but the model stores the whole thing as an
opaque `string` with `supports: SUPPORT`. None of it is queryable. You cannot ask the KB
"show me every edge established by a gain-of-function perturbation", or "every claim whose
only evidence is correlative", because that structure lives only inside free text.

---

## 3. What experiment-grounded evidence would encode

The proposal: keep the exact-snippet discipline (it stays the anti-hallucination floor),
but let an evidence item optionally decompose the **micropublication** — the experiment
and the inferential step from result to claim. A sketch (`ExperimentalEvidence`, extending
`EvidenceItem`):

```yaml
evidence:
- reference: DOI:10.1073/pnas.0409736102
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: "Overexpression of PCSK9 in HepG2 cells caused a decrease in whole-cell and
    cell-surface LDLR levels. PCSK9 overexpression had no effect on LDLR synthesis but
    caused a dramatic increase in the degradation of the mature LDLR"
  experiment:
    design: OVEREXPRESSION                     # closed enum (see §5)
    system:
      organism:  {id: NCBITaxon:9606, label: Homo sapiens}
      cell_type: {id: CL:0000182, label: hepatocyte}   # HepG2, hepatocyte-like
      background: HepG2 cell line
    perturbation:
      role: GAIN_OF_FUNCTION
      target_gene: {id: hgnc:20001, label: PCSK9}
      method: transient overexpression
    readout:
      measured: cell-surface and whole-cell LDLR protein; LDLR synthesis; LDLR degradation
      method: immunoblot / surface labeling
    result:
      direction: DECREASED                     # of LDLR
      qualifier: synthesis unchanged; degradation increased
      snippet: "no effect on LDLR synthesis but caused a dramatic increase in the
        degradation of the mature LDLR"        # exact-quote grounds the RESULT specifically
    inference:
      role: SUFFICIENCY_GOF                     # what the result licenses about the edge
      supports_edge: "PCSK9 Gain-of-Function#PCSK9-Mediated LDLR Degradation"
      claim: PCSK9 is sufficient to drive post-translational LDLR degradation
      caveats: hepatocyte-like line, not primary human hepatocytes; overexpression is
        non-physiologic in level
```

The key move: **the exact snippet now grounds a specific `result`**, and a separate,
typed `inference` records *how the mechanistic edge is drawn from that result*. Strength is
no longer a subjective grade a curator invents (which would reopen the fabrication hole) —
it is *read off the experiment's design and the inference role*, both of which are
snippet-anchored.

---

## 4. Worked example — the PCSK9 → LDLR sub-graph, four experiments, one edge

FH is the gold standard *because necessity, sufficiency, direct mechanism, and therapeutic
rescue all converge on the same arrows.* Here is that convergence made explicit on the
`PCSK9 → LDLR degradation → reduced LDL clearance` sub-chain. (PMIDs marked ⚠ are
canonical papers that must be fetched with `just fetch-reference` and snippet-validated
before any commit; snippet text below is **illustrative placeholder**, not a validated
quote.)

**A. Sufficiency + direct mechanism — cell overexpression** (real, already in repo)
`DOI:10.1073/pnas.0409736102` — HepG2 PCSK9 overexpression → LDLR degraded, synthesis
unchanged. `design: OVEREXPRESSION`, `inference.role: SUFFICIENCY_GOF`.

**B. Necessity — model-organism loss of function** ⚠
*Pcsk9* knockout mouse → increased hepatic LDLR, lower plasma LDL.
`design: KNOCKOUT`, `evidence_source: MODEL_ORGANISM`, `inference.role: NECESSITY_LOF`.
(Remove PCSK9, the effect on LDLR reverses — the necessity counterpart to A.)

**C. Human natural knockout — the single most important missing citation** ⚠
Cohen, Hobbs et al. (NEJM 2006): PCSK9 nonsense variants → ~28% lower LDL and ~88%
reduction in coronary heart disease over 15-year follow-up (ARIC cohort).
`design: HUMAN_GENETIC_LOF`, `evidence_source: HUMAN_CLINICAL`,
`inference.role: NECESSITY_LOF`. A natural human loss-of-function experiment confirming
both the edge direction *and* its disease relevance — currently absent from the entry.
Its reciprocal, Abifadel et al. (Nat Genet 2003) ⚠, identified the gain-of-function
variants that *cause* FH — the human sufficiency arm.

**D. Therapeutic rescue — pharmacological perturbation in humans** ⚠
FOURIER (Sabatine et al., NEJM 2017): anti-PCSK9 monoclonal antibody (evolocumab) →
~59% LDL reduction and fewer cardiovascular events in ~27,500 patients. Inhibiting PCSK9
raises LDLR and lowers LDL — a pharmacological confirmation of the entire
`PCSK9 → LDLR → LDL → ASCVD` chain. dismech already has `target_mechanisms`
(`TreatmentMechanismTarget`) linking the drug to the node; that link *is* confirmatory
edge evidence and should be citable as such.

### The convergence view for a single edge

| Experiment | Design | Source | Perturbation | Inference role |
|---|---|---|---|---|
| A. HepG2 overexpression | OVEREXPRESSION | IN_VITRO | GoF | SUFFICIENCY_GOF |
| B. *Pcsk9*-null mouse | KNOCKOUT | MODEL_ORGANISM | LoF | NECESSITY_LOF |
| C. Human nonsense carriers | HUMAN_GENETIC_LOF | HUMAN_CLINICAL | natural LoF | NECESSITY_LOF |
| D. Evolocumab (FOURIER) | RANDOMIZED_TRIAL | HUMAN_CLINICAL | pharmacologic LoF | THERAPEUTIC_RESCUE |

Four orthogonal method classes agreeing on one arrow. **That agreement is the evidence** —
and today the model records none of it, only `causal_link_type: DIRECT` (topology) and
`supports: SUPPORT` (polarity) four times over. With the structure above, the KB can
compute "this edge is supported by convergent necessity + sufficiency + human-genetic +
therapeutic evidence" — the actual reason a biologist believes it.

---

## 5. Proposed vocabularies (small, closed, dismech house-style)

Two enums do most of the work. Both are ~6–10 values, matching the register of existing
enums like `biological_scale` (4) and `evidence_source` (5).

**`experiment.design`** — *how it was shown* (the observable protocol):
`CORRELATIVE_OBSERVATION`, `OVEREXPRESSION`, `KNOCKDOWN`, `KNOCKOUT`,
`HUMAN_GENETIC_LOF`, `HUMAN_GENETIC_GOF`, `RESCUE_COMPLEMENTATION`, `EPISTASIS`,
`DIRECT_BIOCHEMICAL` (binding/structure/reconstitution), `RANDOMIZED_TRIAL`,
`PHARMACOLOGIC_PERTURBATION`.

**`inference.role`** — *what the result licenses about the causal edge* (the reasoning):
`CORRELATIVE`, `NECESSITY_LOF`, `SUFFICIENCY_GOF`, `RESCUE`, `EPISTASIS_ORDERING`,
`DIRECT_PHYSICAL`, `THERAPEUTIC_RESCUE`.

`design` is largely extractable from the reference metadata / snippet; `inference.role` is
the appraisal axis — but it is *constrained* by design (an overexpression cannot establish
necessity), so the pair is mutually checkable rather than freely asserted.

---

## 6. How this composes with what already exists

- **`causal_link_type`** (`DIRECT` / `INDIRECT_KNOWN_INTERMEDIATES` /
  `INDIRECT_UNKNOWN_INTERMEDIATES` / `UNKNOWN`) stays — it is
  *topology* (how many steps). `inference.role` is *epistemics* (how well established).
  Orthogonal, complementary.
- **`target_mechanisms` (`TreatmentMechanismTarget`)** already links treatment → node.
  Allowing that link to surface as confirmatory edge evidence turns experiment **D** into
  first-class support without new plumbing.
- **`association_signals.statistics`** is the existing structured-effect model for
  comorbidity pairs. The `experiment.result` block generalizes the same idea
  (direction/magnitude, snippet-grounded) to any evidence item.
- **`HUMAN_MODEL_MISMATCH`** discussions already flag model-to-human translation gaps;
  `experiment.system` + `inference.caveats` make the species/system distance structured
  rather than a prose note.
- **Not ECO.** ECO types the assay behind an *annotation of an entity to a term* (its GO
  heritage); dismech's unit is a *supported assertion in a causal graph*, and the axis it
  needs is the inferential role of the experiment for that edge — which ECO does not model.
  A bespoke closed enum fits both the modeling target and the house style.
- **SEPIO** is the correct ontology-backed *shape* for assertion ↔ evidence-line ↔
  evidence-item ↔ provenance, and is Monarch-lineage — but it is heavy for a curation
  surface. Treat it as an **export-layer target** (as BioLink already is), not the thing
  curators hand-edit.

---

## 7. Guardrails preserved

1. **Exact snippets stay mandatory** — `experiment.result.snippet` is still validated as a
   substring, so the granular claim is grounded, not narrated.
2. **Strength is derived, not authored** — from `design` + `inference.role`, both
   constrained and snippet-anchored, so the appraisal layer does not become a new
   fabrication surface (the reason a curator-typed `certainty: HIGH` was rejected).
3. **Claim-type-local** — the causal-inference vocabulary applies to *pathophysiology
   edges* (the mechanistic backbone). Comorbidity, prevalence, and treatment-efficacy
   claims keep their own strength models rather than being forced through one column.

---

## 8. Next steps

1. Float `experiment.design` + `inference.role` on the design register (issue) before any
   schema change.
2. Prototype the block on the FH PCSK9 sub-graph only, fetching and validating the
   experiment B–D references first — the *Pcsk9*-null mouse (Rashid et al.), Abifadel,
   Cohen-Hobbs, and FOURIER (experiment A, the HepG2 overexpression, is already in the
   repo). Brown & Goldstein anchors the separate `LDLR Functional Defect` edge and would
   come in when the prototype extends beyond the PCSK9 sub-graph.
3. Re-point the mis-targeted PCSK9 GeneReviews snippet (§2a) to a real degradation-mechanism
   paper as a *current-schema* fix, independent of the extension.

*Companion slide deck:
[`From evidence pointers to experiment-grounded evidence`](../slides/evidence-model-experiment-grounded.html).
Conceptual overview: [The Evidence Model](../explanation/evidence-model.md).*
