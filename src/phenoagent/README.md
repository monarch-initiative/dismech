# Phenoagent

Phenotype-matching and explanation-loop tooling for dismech.

Phenoagent compares a **patient case** (a GA4GH phenopacket) against a **single
dismech disease model** and produces a structured `MatchingRun`: a table of rows
that align case phenotypes with the disease's modelled phenotypes, an ontology
relation for each alignment, a reusable set of *explanations* for the rows that
don't match exactly, and a roll-up probability `pr_is_diagnosis`.

The four steps below are a pipeline. Steps 1-3 work on **one case + one disease**
(diagnostic explanation); step 4 is a **batch evaluator** that scores the matcher
over many phenopackets at once.

```
            ┌─ Step 1: deterministic init ──────────────┐
phenopacket │  align case ⇄ model phenotypes,           │   matching.yaml
   +  ──────▶  classify each row (exact/broader/...),    ├──▶ (a MatchingRun)
 disease     │  stub non-exact rows with NO_EXPLANATION  │
            └───────────────────────────────────────────┘
                                │
            ┌─ Step 2: agentic explanation loop ────────┐
            │  cyberian + Claude fill real explanations  │   matching.yaml
            │  for every non-exact row, recompute        ├──▶ (pr_is_diagnosis
            │  pr_is_diagnosis, loop until complete       │     now > 0)
            └────────────────────────────────────────────┘
                                │
            ┌─ Step 3: match-aware causal graph ────────┐
            │  overlay the matching onto the disease's   ├──▶ report.html
            │  causal graph → Mermaid + HTML report      │     (Mermaid)
            └────────────────────────────────────────────┘

Step 4 (batch): many phenopackets ─▶ score each vs its true disease ─▶ report
```

## Concepts

A **`MatchingRun`** (`src/phenoagent/schema/matching.yaml`) has run metadata,
a list of reusable `explanations`, a `pr_is_diagnosis` float, and a list of
`matches` rows. Each **`MatchingRow`** carries up to three pieces:

- **case side** — `case_term_id`, `case_label`, `case_present`
  (`false` for an *excluded*/negated phenotype)
- **model side** — `model_term_id`, `model_label`, `model_frequency`
  (`OBLIGATE` › `VERY_FREQUENT` › `FREQUENT` › `OCCASIONAL` › `VERY_RARE`)
- **relation** — exactly one of `exact`, `case_is_broader`, `case_is_narrower`,
  `case_is_close`, plus a `similarity_percent`

Three kinds of row exist: **matched** (both sides), **case-only** (a case
phenotype the model lacks), and **model-only** (a modelled phenotype the case
lacks). Every row where `exact: false` points to an **explanation** via
`explanation_for_no_match`, and `pr_is_diagnosis` is the product of the unique
referenced explanation probabilities.

Annotated example (`tests/phenoagent/data/valid/MatchingRun-001.yaml`):

```yaml
disease_slug: Hypertrophic_Cardiomyopathy
pr_is_diagnosis: 0.0                       # product of referenced explanation probs
explanations:
  - explanation_id: NO_EXPLANATION         # the default stub, probability 0.0
    estimated_probability: 0.0
    description: No explanation assigned yet for this non-match.
matches:
  - case_term_id: HP:0002094               # matched, exact: case == model
    model_term_id: HP:0002094
    exact: true
    similarity_percent: 100.0
  - case_term_id: HP:0001649               # matched, close: Palpitations ~ Tachycardia
    model_term_id: HP:0001979
    exact: false
    case_is_close: true
    similarity_percent: 62.0
  - case_term_id: HP:0012378               # case-only (case_present: false), needs explanation
    case_present: false
    exact: false
    explanation_for_no_match: NO_EXPLANATION
  - model_term_id: HP:0001635              # model-only: modelled but absent in the case
    model_frequency: VERY_RARE
    exact: false
    explanation_for_no_match: NO_EXPLANATION
```

A **disease reference** (used by steps 1-3) can be a dismech slug
(`Fanconi_Anemia`), a disease ontology id (`MONDO:0019391`), a disease name
(`"Fanconi anemia"`), or a path to a disorder YAML file.

---

## Step 1 — Deterministic Init

**What it does.** Loads the phenopacket, resolves the disease, then for each
case phenotype finds the best-matching model phenotype by strict HPO `is-a`
relation (precedence: exact › narrower/broader, ties broken by model
frequency). Unmatched modelled phenotypes are emitted as model-only rows. Every
non-exact row is stubbed with `explanation_for_no_match: NO_EXPLANATION`, so
`pr_is_diagnosis` starts at `0.0`. This step is fully deterministic — no LLM.

**In / out.** phenopacket JSON + disease reference → a `MatchingRun` YAML,
written to `output/matching/<case>__<slug>.yaml` (override with `--output`).
The output path is printed to stdout.

```bash
# Recipe (uses the bundled Fanconi anemia fixture)
just matching-init tests/phenoagent/data/phenopackets/PMID_35451551_proband.min.json Fanconi_Anemia

# Direct module entrypoint, with an explicit output path
uv run python -m phenoagent.matching_cli \
    tests/phenoagent/data/phenopackets/PMID_35451551_proband.min.json \
    Fanconi_Anemia \
    --output output/matching/fanconi_demo.yaml
# prints: output/matching/fanconi_demo.yaml
```

Resolving by ontology id or name works identically:

```bash
just matching-init <phenopacket.json> MONDO:0019391
just matching-init <phenopacket.json> "Fanconi anemia"
```

---

## Step 2 — Agentic Explanation Loop (cyberian + Claude)

**What it does.** Runs Step 1, then hands the matching file to a cyberian
workflow (`workflows/explain_non_matches.workflow.yaml`) driven by Claude. The
agent assigns a concrete, **reusable** explanation to every `exact: false` row
(an `explanation_id` + `estimated_probability` + `description`, reusing the same
id when one reason covers several rows), recomputes `pr_is_diagnosis`, and the
workflow **loops until** no non-exact row still points at `NO_EXPLANATION`
(status `EXPLANATIONS_COMPLETE`). Deterministic content from Step 1 — ids,
labels, relation flags, `similarity_percent` — must stay unchanged; only the
explanations and `pr_is_diagnosis` are filled in.

**Requirements.** This step calls out to `cyberian` and a running agent server
(default `--host localhost --port 3284`). Use `--dry-run` to print the exact
cyberian command without executing anything.

**In / out.** phenopacket + disease → the same matching file, now with real
explanations and `pr_is_diagnosis > 0`. Agent scratch output lands in a
workdir; when `--workdir` is omitted it defaults to:

```text
./workdirs/matching/<case_id>/<disease_slug>/<shortuuid>/
```

```bash
# Dry run — print the cyberian command and exit (no agent needed)
just matching-agent tests/phenoagent/data/phenopackets/PMID_35451551_proband.min.json \
    Fanconi_Anemia --dry-run --verbosity 0

# Real run (requires cyberian + an agent server)
just matching-agent tests/phenoagent/data/phenopackets/PMID_35451551_proband.min.json \
    Fanconi_Anemia

# Direct module entrypoint
uv run python -m phenoagent.cyberian_wrapper <phenopacket.json> <disease_ref>
```

On completion the wrapper prints the matching-file path, the `workdir=`, and the
final `pr_is_diagnosis=` value.

---

## Step 3 — Match-Aware Causal Graph

**What it does.** Builds the disease's dismech causal graph and overlays the
matching report onto it, producing an embedded Mermaid diagram inside a
standalone HTML report (with run metadata). This makes it easy to see *which
nodes of the disease mechanism the case did and didn't hit*.

**In / out.** disease reference + a matching report YAML (the output of Step 1
or 2) → `output/matching/<report_stem>.mermaid.html` (override with `--output`).

```bash
# Recipe (disease first, then the matching report from step 1/2)
just matching-graph Fanconi_Anemia output/matching/fanconi_demo.yaml

# Direct module entrypoint, explicit output
uv run python -m phenoagent.match_graph \
    Fanconi_Anemia output/matching/fanconi_demo.yaml \
    --output output/matching/fanconi_demo.mermaid.html
# prints the written .html path
```

---

## Step 4 — Phenopacket Match-Quality Eval (batch)

**What it does.** A *deterministic batch evaluator*, separate from the
per-case loop above. For each phenopacket that carries a ground-truth diagnosis
(`interpretations[].diagnosis.disease` or a top-level `diseases[]`), it resolves
that diagnosis to a dismech disorder, runs the Step-1 matcher against *that true
disease only*, and reports phenotype-overlap quality plus KB coverage. It does
**not** rank candidate diseases.

```bash
# Bundled fixtures (default)
just phenopacket-eval

# A phenopacket-store checkout (gene-organized notebooks/<GENE>/phenopackets/*.json)
just phenopacket-eval projects/PHENOPACKETS/files/phenopacket-store

# Direct module entrypoint
uv run python -m phenoagent.eval <phenopacket_or_dir>... [--store-dir DIR] \
    [--kb-dir kb/disorders] [--json out.json] [--markdown out.md]
```

Example summary (bundled fixtures, run against the live KB):

```text
- Phenopackets evaluated: 5  (with ground truth: 3, no ground truth: 2)
- Resolved to a dismech disorder (scored): 2
- Ground-truth disease not in KB (KB miss): 1   -> MONDO:0032739 (Stolerman syndrome)
- KB coverage rate: 66.67%
- Mean exact recall: 66.67% | related recall: 83.33% | model coverage: 26.80%
```

**Metrics** (per scored packet, averaged in the summary):
- `exact_recall` — case terms with an exact model match / case terms
- `related_recall` — exact + broader/narrower matches / case terms
- `model_coverage` / `weighted_model_coverage` — distinct modelled phenotypes hit
  by the case (the weighted form scores by frequency: OBLIGATE > VERY_FREQUENT > …)

**Coverage status.** Each packet is `SCORED`, `KB_MISS` (ground-truth disease
absent from dismech — feeds the KB-coverage rate), or `NO_GROUND_TRUTH`.

> **Why not `pr_is_diagnosis`?** At deterministic init every non-exact /
> model-only row points to `NO_EXPLANATION` (probability 0.0), so the product
> `pr_is_diagnosis` is ~0.0 for every packet — it only becomes meaningful after
> Step 2 assigns real probabilities. The eval therefore grades on the
> match-quality surrogate above and reports `pr_is_diagnosis` alongside purely
> so a zero column is not mistaken for a broken matcher.

This v1 is the minimal *match-quality* scope (each packet scored only against
its true disease). Candidate **ranking** (score every packet against all
disorders, report rank-of-true-diagnosis) and a pinned phenopacket-store
**fetch** recipe are the scoped follow-ups.
