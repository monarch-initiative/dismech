# How much of dismech could Rhea actually reach? (2026-09-06)

**Question.** Issue [#973](https://github.com/monarch-initiative/dismech/issues/973)
asks what the relationship between [Rhea](https://www.rhea-db.org/) and dismech should be,
and proposes adding a `reactions:` slot bound to Rhea reaction CURIEs. The thread's one
substantive objection, from @AO33, is that nobody knows how spotty the coverage would be,
and that evaluation metrics should come first. This run measures the coverage.

**What this run did not do.** It changed no schema file, no `kb/` entry, no cache, and no
`conf/` adapter. It is measurement only. Whether to add the slot remains open.

**Baseline.** dismech contains no Rhea identifiers at all. At the commit measured, the only
occurrences of `RHEA:` anywhere in the repository are two deep-research reports
(`Isolated_Sedoheptulokinase_Deficiency`, `CHILD_Syndrome`), their rendered pages, and
`docs/reports/physiomap-assessment-2026-08-23.md`, which describes an *external* project's
use of Rhea. Nothing in `kb/`, `src/`, or `conf/`.

## Method

Rhea and dismech share no identifier today. The only bridge between them is
[`rhea2go.tsv`](https://ftp.expasy.org/databases/rhea/tsv/rhea2go.tsv), which maps Rhea
reactions to GO terms — and GO terms are what dismech already curates, in the
`molecular_functions` and `biological_processes` descriptor slots. So the measurable
question is: of the GO terms already in `kb/`, how many sit on the far end of that bridge,
and how ambiguous is the crossing?

`coverage.py` (committed one directory up) walks every mapping in every `kb/**/*.yaml`
using dismech's own `yaml_io.safe_load`, collects every `term.id` under those two slots,
and joins against the pinned `rhea2go.tsv` snapshot in this directory. Regenerate with:

```bash
python3 experiments/rhea_reaction_grounding/coverage.py > metrics.txt
```

Full output is in [`metrics.txt`](metrics.txt).

## Results

Measured against `kb/` at commit `d985fb64`, 3,110 KB YAML files.

### The rhea2go bridge itself

| | |
|---|---|
| Distinct GO terms mapped | 4,743 |
| Distinct Rhea reactions | 7,745 |
| Direction values | `UN` 7,738 · `LR` 5 · `RL` 2 |
| Undirected share | **99.9%** |

### Coverage of dismech's GO annotation

| | `molecular_functions` | `biological_processes` |
|---|---|---|
| Distinct terms in `kb/` | 648 | 2,462 |
| …with ≥1 Rhea reaction | **284 (43.8%)** | **0 (0.0%)** |
| Annotation instances | 1,358 | 16,536 |
| …covered | 478 (35.2%) | 0 (0.0%) |
| Files carrying the slot | 953 | 2,832 |
| …with ≥1 mappable term | 374 (39.2%) | 0 (0.0%) |
| Covered terms mapping to >1 reaction | 70 (24.6% of covered) | — |

## Three findings that bear on the design decision

### 1. Rhea reaches the molecular-function layer only, and that layer is small

Zero of 2,462 distinct biological-process terms map to anything in rhea2go — across 16,536
annotation instances. This is not a curation gap that better annotation would close. Rhea
maps reactions to molecular function and to a narrow band of metabolic process terms;
dismech's `biological_processes` annotations sit at pathway and process altitude, well above
individual reactions. The layers do not meet.

So the addressable surface is the `molecular_functions` slot alone: 648 distinct terms
against 2,462 for processes, on 953 files against 2,832. A `reactions:` slot would be
populated on a minority of a minority — roughly 374 of 3,110 KB files could carry even one.

Within that layer the coverage is respectable: **43.8% of distinct MF terms**, 35.2% of
annotation instances. "About half the molecular-function layer" is a fair summary, and it is
a better answer than the thread feared.

### 2. Directionality does not come through this bridge

Issue #973's suggested next steps include: *"Consider directionality: RHEA reactions are
directional — this could enrich dismech causal chain representation (upstream → downstream
edges in pathophysiology)."*

The data does not support that. 99.9% of rhea2go rows (7,738 of 7,745) carry `DIRECTION=UN`
— the mapping runs through *undirected master* reactions. Only 7 rows in the entire file are
directional. A reaction ID obtained this way tells a curator what transforms into what, but
not which way flux runs in vivo.

To be precise about what *is* available: directional variants do exist in Rhea and sit one
hop from the master, reachable through `rhea:hasLeftToRightReaction` /
`rhea:hasRightToLeftReaction` (for `RHEA:23844`, those are `RHEA:23845` and `RHEA:23846`).
So directional identifiers are obtainable — what is not obtainable is *which* of the two is
physiological for a given enzyme, tissue, and disease. Rhea does not encode that, and it is
the only part a causal edge needs.

The physiomap assessment independently documents why that matters. Its IEM enzyme edges are
Rhea-grounded, and its header records that *"Physiological flux direction was curated per
enzyme (can reverse the canonical Rhea equation, e.g. CPT2 vs CPT1A on
plasma_palmitoylcarnitine -> opposite signs)"* — the same Rhea equation yields opposite
causal signs for two enzymes depending on physiological context.

Direction therefore stays curator work under any design. A `reactions:` slot justified on
the grounds that it would enrich causal edges with polarity would be built on a premise this
data contradicts. (Polarity on causal edges is separately tracked in
[#9895](https://github.com/monarch-initiative/dismech/issues/9895); nothing here bears on
that except to say Rhea will not supply it for free.)

### 3. A quarter of reachable terms are ambiguous, and the ambiguity is severe

70 of the 284 covered MF terms (24.6%) map to more than one Rhea reaction. The tail is long:

| GO term | Rhea reactions | KB uses |
|---|---|---|
| `GO:0004022` | 67 | 3 |
| `GO:0015020` | 65 | 4 |
| `GO:0003988` | 47 | 1 |
| `GO:0004046` | 42 | 1 |
| `GO:0019166` | 36 | 1 |

For those terms the GO annotation does not determine the reaction, so the slot cannot be
mechanically backfilled — a curator must pick one reaction from as many as 67. That is a
judgment call with no current guidance, and it is the Named Entity Confusion risk pattern
the `dismech-references` skill warns about, reached through a new door.

The corollary is the more useful framing: for the other 75%, the mapping is 1:1 and the
reaction ID is *derivable* from the GO term. Storing a derivable value in YAML is
denormalization. So the slot earns its place precisely on the 70 ambiguous terms — the hard
cases — and adds little on the easy 214.

## Worked examples: what the slot would look like

The two entries whose deep-research reports already carry Rhea IDs land on opposite sides of
finding 3. These fragments are **illustrative only** — no such slot exists, and neither entry
was modified.

### Clean case — `Isolated_Sedoheptulokinase_Deficiency`

`GO:0050277` maps to exactly one reaction. The reaction adds the substrates and products,
each a ChEBI entity, which the GO term does not carry:

```yaml
molecular_functions:
- preferred_term: sedoheptulokinase activity
  term:
    id: GO:0050277
    label: sedoheptulokinase activity
  modifier: DECREASED
  # illustrative — no such slot exists
  reactions:
  - id: RHEA:23844
    label: sedoheptulose + ATP = D-sedoheptulose 7-phosphate + ADP + H(+)
```

### Ambiguous case — `CHILD_Syndrome`

`GO:0000252` maps to **five** reactions (`RHEA:20673`, `33447`, `34771`, `60088`, `60096`).
A curator must choose, and the entry's own GO term does not decide it.

Worse, the deep-research report for this entry proposes `RHEA:33455` and `RHEA:33447` as the
representative NSDHL reactions — and **`RHEA:33455` is not in rhea2go at all**. It maps to no
GO term, so it is not reachable from the curated annotation by any automated route. A curator
following the report would be adding an identifier the validation bridge cannot corroborate.
This is a concrete instance of the standing rule that a CURIE suggested by a deep-research
report is a lead, not a binding.

### Note on label ergonomics

Rhea's canonical label *is* the equation, charge states included — `sedoheptulose + ATP =
D-sedoheptulose 7-phosphate + ADP + H(+)`. The repository's term contract requires
`term.label` to match the canonical label exactly. A `reactions:` slot would therefore put
full chemical equations into KB YAML and into `cache/rhea/terms.csv` rows: verbose, hard to
eyeball in review, and more liable to churn across releases than an HP or GO label.

## Validation feasibility

`sqlite:obo:rhea` resolves through OAK — `runoak -i sqlite:obo:rhea info RHEA:23844` returns
the equation above. So term validation is technically possible, which was the open risk.

The cost is the direction the repository has been moving away from. OLS4 has no Rhea
(`/api/ontologies/rhea` returns 404), so the `ols:` adapter pattern is unavailable and the
prefix would have to be `sqlite:obo:rhea` — a 163 MB local build. `conf/oak_config.yaml`
deliberately migrated large ontologies *to* `ols:` to avoid exactly that (issue #5160), and
its own note records the precondition for migrating a further prefix. Adding Rhea would
reverse that trend for a new prefix.

## Limits of this measurement

- **It measures one bridge, not the ceiling.** Coverage here is what is *derivable from
  already-curated GO terms* via rhea2go. A curator could assign a Rhea ID by hand from
  UniProt or an EC number without going through GO, and the achievable annotation rate would
  be higher than 43.8%. What this run bounds is automated backfill and mechanical validation,
  not what a determined curator could reach.
- **It says nothing about scientific correctness.** That a GO term maps to a reaction does
  not mean that reaction is the right claim for the pathophysiology node it sits on. Every
  number here is an upper bound on *availability*, never on *appropriateness*.
- **It does not test ergonomics.** Whether curators would populate the slot is not something
  a census can answer; the fragments above are the cheapest available proxy.
- **Snapshot-dependent.** rhea2go is unversioned upstream and pinned here by sha256. Both
  Rhea and GO release independently, so these numbers will drift.
- **`biological_processes` is measured only through rhea2go.** The 0% is a statement about
  this bridge. It is a strong result given 16,536 instances, but a different mapping route
  could in principle do better.

## What this run does and does not settle

It settles that coverage is not the blocker: 43.8% of the molecular-function layer is
reachable, and validation is technically feasible. It also settles that two premises in
#973's next-steps list do not hold — directionality is not inherited through rhea2go, and a
quarter of reachable terms cannot be mechanically resolved.

It does not settle whether the slot is worth building. The case against is now sharper than
coverage: the addressable surface is one slot on a minority of files, three quarters of the
reachable terms would store a derivable value, and the validation path runs against the
repository's adapter-size policy.

A reasonable next step, if the slot is pursued, is to scope it to the ambiguous quarter —
where a curator's choice adds information no automated route can — rather than to the full
molecular-function layer. That is a smaller, more defensible change than #973 as written.

## Provenance

| | |
|---|---|
| `rhea2go.tsv` | https://ftp.expasy.org/databases/rhea/tsv/rhea2go.tsv |
| Retrieved | 2026-09-06 |
| sha256 | `a6695b6938942615d4529dea0125277b03bd025c42e0f314557091a08a489b07` |
| Bytes | 201,401 |
| KB commit | `d985fb64` |
| Rhea license | CC BY 4.0 |
