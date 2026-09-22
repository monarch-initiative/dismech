# Evidence semantics and provenance

### Evidence Items
Evidence uses supported literature or structured-source references and a
support classification:
```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT  # or REFUTE, NO_EVIDENCE
    directness: DIRECT  # optional: or INDIRECT, UNKNOWN
    evidence_source: HUMAN_CLINICAL  # or MODEL_ORGANISM, IN_VITRO, COMPUTATIONAL
    snippet: "Quoted text from the paper"
    explanation: "Why this evidence supports/refutes the claim"
```

#### `supports` is direction; `directness` is a separate axis

`supports` records **which way** the cited evidence cuts, and nothing else:

- `SUPPORT` — the evidence supports the claim
- `REFUTE` — the evidence contradicts the claim
- `NO_EVIDENCE` — the cited reference does not bear on the claim at all

`directness` (optional) records **how directly** the quoted text bears on the
claim. It is *not* a strength or quality grade — an `INDIRECT` quote may come
from a large controlled trial, and a `DIRECT` one from a single case report:

- `DIRECT` — the quoted text asserts the claim itself
- `INDIRECT` — the quote asserts something from which the claim follows by an
  inference step: a therapeutic response cited as validation of the mechanism it
  targets, or a result from an inverted or non-human model system
- `UNKNOWN` — not yet assessed

**Leave `directness` off unless you have actually assessed it.** Absent means
nobody has judged it, which is the honest state of most of the KB. Do not fill
it in to look complete.

#### `quote_role` is document provenance, and a third separate axis

`reference` says **which paper** a quote came from. `quote_role` (optional) says
**whether that paper produced the finding or was repeating somebody else's**:
where in the cited publication's own argument the quoted sentence sits:

- `PRIMARY_RESULT`: the cited publication produced this observation,
  measurement, analysis, or conclusion
- `BACKGROUND`: it is restating something established elsewhere, such as an
  introduction, a framing sentence, a motivation for the work
- `REVIEW_SYNTHESIS`: it is the publication's synthesis of work it did not
  perform: a review, commentary, editorial, or consensus statement

**Use it when `evidence_source` alone would say something false.** The case it
exists for (#10262) is a quote taken from an animal study's *introduction*, where
that introduction states the human clinical picture:

```yaml
- reference: PMID:42162447          # a mouse base-editing study
  supports: SUPPORT
  quote_role: BACKGROUND
  evidence_source: HUMAN_CLINICAL
  snippet: "Pathogenic variants in KCNQ4 account for ~9.5% of autosomal dominant nonsyndromic cases."
```

`MODEL_ORGANISM` there would assert that a mouse measured human allele frequency.
`HUMAN_CLINICAL` alone would assert the publication is a human clinical study.
`OTHER`, where review pressure used to push these, says nothing at all, and
files the case next to the unrelated "quoted from a review" one.
`HUMAN_CLINICAL` + `BACKGROUND` is exactly true and exactly queryable.

**Leave it off unless you have assessed it**, as with `directness`. There is no
`UNKNOWN` value: absent already means nobody has judged it.

**It does not change what `evidence_source` means.** `evidence_source` still
grades the evidence the quoted text describes; `quote_role` records that the
citing paper is not where it came from. The two are orthogonal, and so are
`supports` (direction) and `directness` (inferential distance). A `BACKGROUND`
quote can be `DIRECT`, `SUPPORT` and `HUMAN_CLINICAL` all at once.

**Finding candidates:**

```bash
just list-background-citations                 # worklist, three tiers, report-only
just list-background-citations --format tsv    # one row per candidate
just list-background-citations --tier A        # the deterministic tier alone
just list-background-citations kb/disorders/MyDisease.yaml
```

Tier A is deterministic: NLM structured-abstract section labels in the cached
reference body, located by string containment. Tier B is the MeSH
animal-without-`Humans` heuristic, which covers only items graded
`HUMAN_CLINICAL` or `OTHER` citing animal-only papers, so **its count is a lower
bound on a narrow slice and not a measure of the problem**. Tier C reports a
recorded `quote_role` that contradicts Tier A.

**Report-only, never an autofill.** A structured `BACKGROUND:` paragraph
routinely closes with the authors' own framing of what they did, so a flagged
snippet can be correctly `PRIMARY_RESULT`; and a quote taken from a full text has
no NLM labels to sit between, so Tier A declines to classify it rather than
guessing. Read the sentence. This is the same line `dismech-terms` draws for
ontology-term suggestions.

Worked examples: `Cerebrocostomandibular_Syndrome` (one chick-embryo paper cited
both ways, `BACKGROUND` for the human clinical picture in its introduction and
`PRIMARY_RESULT` for its own rib-gap experiments),
`Autosomal_Dominant_Nonsyndromic_Hearing_Loss_2A` (two mouse papers' background
epidemiology, beside the human family series that is the `PRIMARY_RESULT` behind
it), `Immunodeficiency_98_With_Autoinflammation` (the two unrelated reasons an
item lands on `OTHER`, now distinguished as `BACKGROUND` and
`REVIEW_SYNTHESIS`).

A quoted **aim** statement ("the aim of the present study was to…") has no value
in this enum; it is neither the paper's finding nor somebody else's fact. Leave
`quote_role` off; `just list-background-citations` reports those separately.

**`PARTIAL` and `WRONG_STATEMENT` were removed** (issue #7439). If you are
tempted to reach for the old `PARTIAL`, one of these is what you mean:

| You want to say | Use |
|---|---|
| supports the claim, but through an inference step | `SUPPORT` + `directness: INDIRECT` |
| right mechanism, inverted or non-human model system | `SUPPORT` + `directness: INDIRECT` |
| supports one part of the claim, contradicts another | **two items** — a `SUPPORT` and a `REFUTE`, each quoting the sentence that carries it |
| true and worth citing, but not about this claim | `NO_EVIDENCE` |
| an earlier version of this entry's text was wrong | fix the text; record the correction in a `history/` record |

The third row is the one to watch. A single evidence item making two opposite
claims is the same defect as one item mixing two `evidence_source` values, and
has the same remedy: split it.

**IMPORTANT**: The `evidence_source` field classifies **the type of evidence presented in the cited publication**, NOT how the curation was performed. Even if an AI agent is curating the entry, `evidence_source` describes what kind of study the paper reports (human clinical trial, animal model, cell culture, computational simulation, etc.).

That rule is about *how the curation was done*, and it is unchanged. It does not
decide the case where the quoted sentence describes one kind of evidence and the
citing paper ran another: for that, grade `evidence_source` from the quoted text
and record the mismatch in `quote_role` (see
[`quote_role` is document provenance](#quote_role-is-document-provenance-and-a-third-separate-axis)
above). Pushing such an item to `OTHER` on the strength of this paragraph alone
throws away both facts, which is the defect #10262 was filed about.

Set `evidence_source` to clarify the publication's evidence type:
- HUMAN_CLINICAL for direct human observations (default when not specified)
- MODEL_ORGANISM when citing animal model recapitulation
- IN_VITRO for cell-based experiments
- COMPUTATIONAL for in silico predictions/simulations reported in the paper
- OTHER for evidence types that do not fit the above categories
Model organism evidence should not be the only support for human phenotypes; keep it distinct via `evidence_source`.

Quick classification rules (use these before tagging):
- HUMAN_CLINICAL: human patients, cohorts, case reports, clinical trials (NCT), epidemiology.
- MODEL_ORGANISM: any in vivo animal data (mouse, zebrafish, dog/cat/horse veterinary case series, primate, or other non-human animals), even if observational and not interventional.
- IN_VITRO: cultured cells or tissue explants (human or animal), organoids, ex vivo slices, biochemical assays outside an organism.
- COMPUTATIONAL: in silico modeling, docking, simulations, ML predictions, network/pathway inference without wet-lab confirmation.
- OTHER: anything that does not cleanly fit above (e.g., expert consensus without data, pathology image atlases without linked cohort context).

Edge cases:
- Veterinary observations are MODEL_ORGANISM (non-human mammals are still animal models for this purpose).
- In silico “modeling studies” belong to COMPUTATIONAL, even if they use clinical datasets as input.
- If a paper mixes sources, split evidence items so each item gets a single `evidence_source`.
