# Science sandboxes (Rao et al. 2026) — paper map and dismech implications

> Rao AS, Castro RI, Gosai SJ, Hsu KB, Ektefaie Y, Singh S, Bhatia SN, Reilly SK,
> Tewhey R, Lander ES, Sabeti PC. *Science sandboxes measure the scientific
> capability of AI agents.* arXiv:2608.30165 [q-bio.QM], 31 Aug 2026.
> Code: <https://github.com/asr2210/science-sandbox>

Read on 2026-09-05 from the submitted PDF. This page has two halves: a factual
map of what the paper does, and an assessment of what it implies for dismech.
The second half is argument, not the authors' claims — it is marked as such
throughout.

dismech is an agent-forward knowledge base whose curation is largely performed
by AI agents and reviewed by another AI agent
([Automation & Agents](../explanation/automation-and-agents.md), design
decision §7). This paper is the most direct published attempt to measure whether
such agents are doing science or optimizing a number, so it bears on how much
weight dismech's own automated signals can carry.

---

## Part 1 — What the paper says

### The construct

A **science sandbox** is a closed-loop testbed with exactly three parts:

| Part | Definition |
|---|---|
| **Specimens** | Any entity that can be submitted for testing — a DNA sequence, protein, chemical, cell, or abstract string. |
| **Assays** | Methods for ascertaining properties of those specimens. |
| **Oracle** | A *sealed* mechanism that applies the assays and returns a report. Its internals are hidden from the agent. |

Each round, the agent proposes specimens, the oracle returns a report, and the
agent records its interpretation and chooses the next experiment. Because the
oracle is sealed, the agent must infer the system's rules from evidence alone.

The load-bearing design choice is that **the object of evaluation is the agent's
reasoning, not its score**. Agents are required to keep an append-only
`notebook.md` recording hypotheses, interpretations, and plans. Humans or
independent AI judges then read the notebook to decide whether the agent
inferred the rules or merely found high-scoring specimens. The paper's framing:
a benchmark rewards any strategy that raises the score, so it cannot tell
epicycles from gravity.

### The oracle spectrum

The framework's most portable idea is a three-way classification of where
feedback comes from, each with a stated cost:

| Oracle | Source of truth | Cost the authors name |
|---|---|---|
| **Wet** | A physical experiment | Expensive, slow, noisy |
| **Damp** | A predictive model trained on empirical data | Inherits the biases and assumptions of its training data |
| **Dry** | An invented rule known only to the designers | Exact ground truth, no real-world complexity |

### MPRAbox

Regulatory genomics. The agent designs a library of N = 50,000 sequences of
200 bp over {A, C, G, T}. The task is deliberately not "find high-scoring
enhancers" but "design the library that best trains a generalizable
sequence-to-activity model" — a harder, more realistic experimental-design
problem.

The damp oracle labels the submitted library with Malinois (a published CNN
trained on 776,474 MPRA measurements in K562, HepG2, SK-N-SH), trains a fresh
model from random initialization on those 50,000 labeled sequences, evaluates it
on 14 hidden test sets drawn from 9 source distributions (5 with experimental
labels, 9 with Malinois labels), and returns **only** the 14 Pearson
correlations and their mean. Set identities, sequences, labels, and
sequence-level predictions are withheld. The agent interacts through a sealed
`prepare.py` it is instructed to treat as a wet-lab collaborator and not to
inspect; the authors report that log analysis confirms the agents complied.

Fourteen human-designed sampling strategies (DHS-based, Sei-based, synthetic
random, prior MPRA sequences, and mixtures), five seeds each, form the reference
panel.

**One-shot results**, three agents in their native harnesses, five replicates
per condition:

| Condition | Claude Opus 4.7 | GPT-5.5 | Gemini 3.5 Flash | Best human strategy |
|---|---|---|---|---|
| No prior knowledge (median r) | 0.774 | 0.655 | 0.680 | 0.763 |
| With prior knowledge (median r) | 0.781 | 0.760 | 0.751 | 0.763 |

Without prior knowledge the agents diverged on strategy, not just on score.
Claude chose genomic regulatory DNA in all five replicates, deliberately
weighting rarer ENCODE cCRE classes for calibration. GPT built fully synthetic
motif-perturbation series in all five, reasoning that controlled perturbations
isolate causal features. Gemini mixed approaches and landed in between. Given
the human panel's results, GPT and Gemini shifted toward genomic sequence and
improved most; Claude, already there, moved least. Notably, **the agents did not
converge on one strategy even when given identical prior information**, and did
not simply copy the best human design.

**Long-horizon**: four 30-round Claude runs (two informed, two blind). All four
beat the strongest human strategy, but the quantitative gain over one-shot was
modest — the point was to watch reasoning change. Two behaviors are worth
recording. First, genuine surprise-driven revision: an agent predicted a random
DNA library would score near zero, saw it score high, and rewrote its theory to
separate "free" composition-driven signal from regulatory grammar. Second, an
agent derived experimental hygiene unprompted, after confounding two variables
in one round: *"Always isolate one variable at a time when the result will be
interpreted as 'X works/doesn't work'."* The four runs ended at four different
high-performing libraries.

### Dry oracles: the pivotal experiment

The same MPRAbox structure, with Malinois replaced by 14 invented scoring rules
(Table 3 of the paper): GC balance, alternating purines, a hidden cipher mapping
nucleotide pairs to English letters, compressibility, prime counts, Fibonacci
positions, Conway's Game of Life, modular arithmetic, Collatz stopping time, and
others. Three framings of the identical rule: told it is MPRA regulatory DNA;
told only that it is a black-box scorer over {A, C, G, T}; and with the alphabet
replaced by {0, 1, 2, 3}.

Framing changed how the agent explored — biological framing triggered
motif hypotheses, symbolic framing triggered simple symbol-frequency
hypotheses — but **framing did not reliably produce rule discovery**. For the
English-word cipher, no framing led the agent to consider that character pairs
might encode letters. For the Fibonacci rule, the agent concluded the model was
"learning dinucleotide composition statistics" — an explanation that captured
enough structure to improve the score while being *not the rule generating the
observations*. Sometimes biological priors handed the agent a proxy that
correlated with the hidden rule, so it improved without understanding why.

### CodonBox

De novo rule discovery in invented genetic worlds. A sequence is parsed into
codons, translated by a hidden world-specific table into a 16-residue
hydrophobic/polar chain, and folded under Dill's 2D HP lattice model; fitness is
the count of favorable non-consecutive H–H contacts in the optimal fold, capped
at 9. The agent is told only the alphabet and the sequence length, submits one
sequence per round for 500 rounds, and receives one number. Eight worlds vary
alphabet size (j = 4, 6, 8), codon length (k = 2, 3, 4), presence of silent
positions, and whether informative positions act additively or interact.

Maximization is trivial and uninformative: a repeated character is read as a
repeated codon, and if it maps to H the chain is all-H and hits the ceiling.
**Agents reached the maximum score within 10 rounds in every run.** The
interesting question is what the remaining 490 rounds bought.

| World | Outcome |
|---|---|
| j=4, k=2 or 3 | Codon length inferred; table filled in by enumeration |
| j=4, k=4 (256 codons) | Codon structure inferred; table not recovered |
| j=8, k=3 (512 codons) | Codon structure inferred; substantial fraction of table mapped |
| j=6, k=3 (216 codons) | **Codon structure never discovered.** Built an elaborate theory of individual nucleotides, runs, and short patterns that genuinely predicted the score |
| j=4, k=3, silent outer positions | Correctly inferred silence by controlled perturbation, then mapped the middle position — the cleanest success |
| j=4, k=3, interacting outer positions | Single-nucleotide theory broken by one contradicting experiment; agent switched to testing combinations and recovered the interaction |
| j=6, k=4, silent + 3-way interaction | Codon length inferred; silent position and general rule never recovered; agent regressed to cataloguing known-good codons |

Two results deserve emphasis. The j=6 failure is **non-monotonic** — a smaller
table defeated the agent where a larger one did not — so difficulty is not
simply search-space size. And the recurring failure mode under pressure is
regression from theory-building to memorizing high-scoring specimens.

### The conclusion the authors draw

Agents optimize well by leaning on pretraining priors, and that competence is
**brittle**: rule inference collapses when the rules require positional,
mathematical, or combinatorial logic outside biological intuition, even while
scores keep improving. Notebooks reveal a recurring strategic weakness —
brute-force search exhausting the budget, where stronger trajectories used broad
exploration followed by targeted tests. The authors propose automating notebook
evaluation with independent AI judges scored against the known ground-truth
rule, and intend to release further sandboxes via BroadBox.

---

## Part 2 — Implications for dismech

*This half is assessment, not the paper's claims. Counts were measured on this
checkout on 2026-09-05 with `grep -rl` / `grep -rh` over `kb/`; they will drift.*

### The measurement that makes the paper's point about dismech

The paper's distinction is between a system that raises a score and one that
records what would prove it wrong. Applying that as a query to `kb/`:

| Slot | Files | Occurrences |
|---|---|---|
| `proposed_experiments:` | 842 | **1,732** |
| `decision_criterion:` | 255 | 732 |
| `would_support:` | 219 | 446 |
| `controls:` | 88 | 168 |
| `would_refute:` | **74** | **124** |

And the hypothesis layer those experiments hang off: 413 files carry
`mechanistic_hypotheses:`, with 1,508 `hypothesis_group_id:` occurrences and
status lines splitting 512 `CANONICAL` / **462 `EMERGING`** / 176 `ALTERNATIVE`
/ 23 `DEPRECATED`. The discussion layer is larger still: 1,774 `KNOWLEDGE_GAP`
discussions, 573 `HUMAN_MODEL_MISMATCH`, 178 `CONTROVERSY`.

So dismech proposes an experiment roughly **14 times more often than it records
what would refute the hypothesis** (1,732 vs 124), and carries 462 early-stage
hypotheses against 124 refutation clauses in the entire knowledge base.

The sharpest cut: **207 disorder files contain a `status: EMERGING` hypothesis
and no `would_refute` anywhere in the file.** A sample, all real entries as of
this checkout:

```
3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency
3-Hydroxyisobutyryl-CoA_Hydrolase_Deficiency
3-Phosphoglycerate_Dehydrogenase_Deficiency
ABCC9-Related_Intellectual_Disability_and_Myopathy_Syndrome
ADan_amyloidosis
AGAT_Deficiency
ALDH18A1_Cutis_Laxa
ALDH18A1_De_Barsy_Spectrum
```

The entries that do it properly are the model to copy:
`Alzheimer_Disease.yaml`, `Alcoholic_Liver_Disease.yaml`,
`Arrhythmogenic_Right_Ventricular_Cardiomyopathy.yaml`,
`Alveolar_Rhabdomyosarcoma.yaml`,
`ADGRG1_Bilateral_Frontoparietal_Polymicrogyria.yaml`,
`Alopecia-Intellectual_Disability_Syndrome_1.yaml`.

This is the paper's finding restated in our own data. A `KNOWLEDGE_GAP` with a
`proposed_experiments` block reads like scientific rigor and is cheap to
generate — it costs one plausible paragraph. A `would_refute` is expensive
because it commits to an observation that would kill the hypothesis. We have
built 1,732 of the cheap thing and 124 of the expensive one.

### dismech already ran this experiment, on Wilson disease

The single best illustration is in the repo, not in the paper:
`kb/hypotheses/Wilsons_Disease/cuproptosis_model/`.

OpenScientist reported six differential-expression results supporting a
cuproptosis model. A Codex-audited, byte-replayed Biomni bundle recomputed them
over the full platform. From `reconciliation.md`:

| Contrast | OpenScientist reported | Corrected audit |
|---|---|---|
| Human FDX1 | Down, nominal p=0.032 | log2 −0.6315, Welch p=0.0027, **BH q=0.0569** |
| Human DLAT | Down / trending down | log2 **+0.5144**, q=0.2173 — direction contradicted |
| Human DLD | Up, p=0.017 | log2 −0.0549, q=0.8622 — not reproduced |
| Mouse Dlst | Down, p=0.008 | log2 **+0.5607**, q=0.00601 — direction and interpretation contradicted |
| Mouse Gls | Down, p=0.006 | Welch p=0.3557, q=0.5406 — not reproduced |
| Mouse Fdx1 | Down, p=0.039 | Welch p=0.0426, q=0.1793 — nominal only |

Two of six directions were contradicted, none reached adjusted significance, and
the audit caught that GSE125637 is a GPL1261 Affymetrix microarray, not RNA-seq
— a platform fact the provider report was silent on. OpenScientist's two
calculations are recorded as `REPORTED_ONLY / UNVERIFIABLE`: no committed
inputs, code, environment, probe rule, or replay.

That is the Fibonacci result with a disease attached. A coherent, partially
directionally-correct account survived until someone sealed the oracle and
replayed the computation. It is also evidence the assessment policy works —
this was caught by dismech's own machinery, before the claims reached a disease
entry.

The reconciliation also states the shared-lineage rule in a concrete case: both
reports used the same two public accessions, and it records that this "does not
constitute independent computational convergence, particularly when only one
execution is auditable."

### Compliance is literally a field-population ratio

Not a metaphor. `src/dismech/qc_plugins.py:249-253`:

```python
weighted_populated = sum(s.populated * s.weight for s in scores)
weighted_total = sum(s.total * s.weight for s in scores)
...
return weighted_populated / weighted_total * 100
```

The score counts *whether slots are filled*, weighted by `conf/qc_config.yaml`.
Nothing in that expression can see whether the causal chain is right. An entry
that adds a `KNOWLEDGE_GAP` with a `proposed_experiments` block raises its
compliance exactly as much whether the proposed experiment is decisive or
vacuous — and, per the counts above, the vacuous-cheap version is what the KB
has accumulated. That is the concrete mechanism by which our metric and our
scientific goal come apart, and it is the paper's thesis in ten lines of Python.

### What we have no instrument for at all

Every dismech gate verifies faithfulness to a source or to the schema: snippet
exact-substring matching, CURIE and label validation, dynamic-enum membership,
entity-reference foreign keys, causal-target resolution. A claim that faithfully
quotes a wrong paper passes all of them. In the paper's vocabulary, dismech has
specimens and assays but no oracle — the literature is a record of *other
people's* oracles.

The one place we approximate one is the hypothesis-assessment tree: 291 provider
reports under `kb/hypotheses/` against 81 YAML sidecars
(assessments, reconciliations, manifests). Roughly **one in four provider
reports has been audited.** The other three in four are unexamined narrative of
exactly the genre the Wilson case shows can be directionally wrong.

### Provider disagreement is not an error signal

Concretely: the paper's agents received identical prior knowledge and still did
not converge on a strategy, and four long-horizon runs of the same model ended
at four different high-performing libraries. Divergence was a property of the
task.

For our reconciliation practice, the count of agreeing providers is the wrong
statistic in both directions — and the Wilson reconciliation already writes the
right one down: shared accessions, shared code, or one provider's output feeding
another's is not independent replication. Two providers agreeing off one GEO
series is one observation, not two.

### The notebook half we do not have

Both sandboxes force an append-only notebook, and CodonBox requires a
`rationale` naming the hypothesis *before* the result is known — round-level
pre-registration, which is what makes after-the-fact evaluation of reasoning
possible.

`history/` records are append-only, but they are written after curation and
record what was done, not what was expected. Nothing distinguishes an agent that
predicted a finding from one that rationalized it afterward. Writing the
intended approach and expected outcome into a history record's `details` before
curating would close most of that gap with no schema change.

---

## What a dismech sandbox would look like, and why it is hard

The tempting construction: hold out a curated entry's causal edges, have an
agent propose edges from the literature, score against the held-out curation.

The oracle there is **curator judgement**, not nature, so it is damp at best and
scores agreement with our house conventions — node granularity, naming, where a
mechanism is split — as much as biological correctness. An agent could score
well by learning dismech's style. The paper's damp-oracle caveat applies exactly.

Two variants look more defensible:

1. **A dry sandbox over invented pathophysiology.** Generate synthetic diseases
   with known hidden causal graphs plus a generated literature corpus, and ask
   whether an agent recovers the graph. CodonBox's design lever transfers
   directly: vary whether mechanisms combine additively or interact, and whether
   some observations are silent. Recall that the interacting-position world was
   solved only when the agent switched to testing combinations, and that the
   silent-position world was the cleanest success — both are ordinary situations
   in disease mechanism.
2. **A temporal holdout.** Use publication date as the seal: give an agent the
   literature to year *Y*, score its predicted mechanism against what was
   established after. Ground truth is real; the cost is that it is unrepeatable
   per disease and pretraining contamination is the obvious confound.

Neither is proposed as work. They are recorded so a future "let's build a
dismech benchmark" conversation starts from the oracle question, not the metric.

## What does not transfer

- **Different capability.** MPRAbox agents design experiments against a live
  oracle; dismech agents synthesize existing literature. Failing to infer a
  hidden rule from feedback does not directly predict failing at faithful
  curation, which is nearer to reading comprehension with citation discipline —
  the thing our snippet gate does check, and checks well.
- **Model versions move.** Claude Opus 4.7, GPT-5.5, Gemini 3.5 Flash in their
  native harnesses. Treat the ranking as a snapshot; the framework and failure
  modes are the durable contribution.
- **Small n.** One run per CodonBox world, four long-horizon MPRAbox runs. The
  failure modes are consistent and vivid, but per-world outcomes are single runs.
- **No AI judge was run.** Automated notebook scoring is proposed future work;
  evaluation here was human inspection.

## Follow-ups worth considering

1. **Close the 207.** Disorder files with an `EMERGING` hypothesis and no
   `would_refute` are a concrete, enumerable worklist, and the six named entries
   above are the pattern to copy. This is the highest-value item here.
2. **Audit more of the 291.** One in four provider reports has an assessment
   sidecar. The Wilson case shows what the unaudited three in four can contain.
3. **Cite this paper in [Automation & Agents](../explanation/automation-and-agents.md)**
   where it explains the LLM-reviewer approval loop, as published support for
   "a passing score is not evidence of understanding."
4. **Consider a decision-register line** stating compliance is never a proxy for
   mechanistic correctness, given `_weighted_compliance` is a population ratio.
5. **Pre-register in `history/`**: record intended approach and expected outcome
   in `details` before curating, not after.
