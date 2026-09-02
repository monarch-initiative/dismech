# Science sandboxes (Rao et al. 2026) — paper map and dismech implications

> Rao AS, Castro RI, Gosai SJ, Hsu KB, Ektefaie Y, Singh S, Bhatia SN, Reilly SK,
> Tewhey R, Lander ES, Sabeti PC. *Science sandboxes measure the scientific
> capability of AI agents.* arXiv:2608.30165 [q-bio.QM], 31 Aug 2026.
> Code: <https://github.com/asr2210/science-sandbox>

Read on 2026-09-02 from the submitted PDF. This page has two halves: a factual
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

*This half is assessment, not the paper's claims.*

### dismech has no oracle, and should say so plainly

The sandbox construct exposes what dismech's validation stack actually is.
Every gate we run — exact-substring `snippet` checking, ontology term and label
validation, dynamic-enum membership, entity-reference foreign keys, causal-target
resolution — verifies **faithfulness to a cited source or to the schema**. None
verifies correspondence to nature. In the paper's vocabulary dismech has assays
and specimens but **no oracle at all**: the literature is a record of other
people's oracles, and a curated claim that faithfully quotes a wrong paper
passes every check we have.

This is not a defect to fix; it is the correct description of a curation
project, and it is worth stating in these terms because it bounds what our green
CI can mean. The paper's own caveat about damp oracles — they inherit the biases
and assumptions of the underlying model — applies with more force to a
literature-derived oracle, which inherits publication bias too.

### The compliance score is dismech's MPRAbox metric

`linkml-data-qc` reduces an entry to a weighted scalar over field population
([Quality Control](../quality-control.md)). Agents curate against it. The paper's
central result is that agents reliably improve such a scalar while their
underlying model of the system stays wrong or absent — and that the score alone
cannot distinguish the two cases.

Applied here: a high-compliance entry is evidence that fields are populated and
snippets verify. It is **not** evidence that the pathophysiology chain is the
right causal account of the disease. We already know this informally; the paper
supplies the reason to keep the two separate in reporting, and an argument
against ever treating compliance as a proxy for mechanistic quality in
prioritization or in a manuscript.

### `REPORTED_ONLY` is already the sealed-oracle instinct

The strongest existing alignment is in hypothesis-report assessment
([Hypothesis Report Assessments](../hypothesis-report-assessments.md)). That
policy refuses to let a provider's *claim* of an analysis count as an executed
analysis: `SUCCEEDED` requires a reproducible artifact-backed run, and
`REPORTED_ONLY` explicitly marks unverified execution. Dataset access is graded
the same way, with `ACCESSED` requiring a committed sanitized artifact and
`CITED_NOT_ACCESSED` naming the gap.

That is structurally the same move as sealing the oracle: separate what the
agent asserts from what independently happened. The paper is a citable
justification for a policy dismech adopted on its own, and an argument against
relaxing it.

### The dry-oracle failure is the `mechanistic_hypotheses` failure

The Fibonacci result is the one to internalize. The agent produced a coherent,
partially predictive, and wrong account of the system — and the score kept
improving. dismech's `mechanistic_hypotheses` blocks, and the provider reports
under `kb/hypotheses/`, are exactly this genre of artifact: a mechanism
narrative that explains observations. The paper demonstrates that fluency and
partial predictive success are compatible with the mechanism being wrong, and
that this is the *expected* failure when the true rule sits outside the model's
priors.

Practical consequence: an `EMERGING` hypothesis whose support is a coherent
narrative plus consistency with the literature is weaker evidence than its
readability suggests. The schema already offers the right instrument — an
`Experiment` with `decision_criterion`, `would_support`, and `would_refute`,
which forces a claim about what would *break* the hypothesis. We should prefer
recording that discriminating experiment over adding another paragraph of
supporting narrative.

### Provider non-convergence is not by itself an error signal

Directly useful for cross-provider reconciliation. The paper reports that agents
given identical prior knowledge **did not converge** on one strategy, and that
four long-horizon runs of the *same* model ended at four different
high-performing designs. Divergence was a property of the task, not evidence
that three of the four were malfunctioning.

Our reconciliation practice should not treat inter-provider disagreement as
prima facie evidence that someone is wrong. The paper also supplies the sharper
question to ask instead — one already in our policy: shared input data, shared
code, or one provider's output feeding another's is not independent replication.
Agreement produced by shared priors is worth less than the count of agreeing
providers suggests, which cuts against reading convergence as confirmation just
as much as it cuts against reading divergence as error.

### Notebook discipline is cheap, and we do not have it

Both sandboxes force an **append-only** notebook, and CodonBox requires a
`rationale` stating what hypothesis each experiment tests *before* the result is
known. This is pre-registration at the round level, and it is what makes
after-the-fact evaluation of reasoning possible at all.

dismech has the append-only idea for outcomes — `history/` records are
append-only and never rewritten — but they record what was curated, not what the
agent expected before it looked. A curation session's reasoning survives only as
prose in the PR body and as `details` in the history record, both written after
the work. There is no cheap way today to ask whether an agent's stated
expectation preceded or followed the evidence. Recording an intended approach
and its expected outcome in the history record's `details` before curating would
close most of that gap without new schema.

---

## What a dismech sandbox would look like, and why it is hard

The tempting construction: hold out a curated entry's causal edges, have an
agent propose edges from the literature, score against the held-out curation.

It is worth being clear about what this would and would not measure. The oracle
is **curator judgement**, not nature, so it is damp at best and scores agreement
with dismech's own conventions — node granularity, naming, where a mechanism is
split — as much as biological correctness. An agent could score well by learning
our house style. The paper's damp-oracle caveat applies exactly.

Two variants look more defensible:

1. **A dry sandbox over invented pathophysiology.** Generate synthetic diseases
   with known hidden causal graphs and a generated literature corpus, then ask
   whether an agent recovers the graph. Ground truth is exact, and CodonBox's
   design lever transfers directly: vary whether mechanisms combine additively or
   interact, and whether some observations are silent. Expensive to build, and it
   tests literature-to-graph inference rather than disease biology.
2. **A temporal holdout.** Use publication date as the seal: give an agent the
   literature up to year *Y* and score its predicted mechanism against what was
   established after. Ground truth is real and no corpus needs inventing; the
   cost is that it is unrepeatable per disease, and pretraining contamination is
   the obvious confound — the agent may already know the answer.

Neither is proposed as work. They are recorded so that a future "let's build a
dismech benchmark" conversation starts from the oracle question rather than the
metric question.

## What does not transfer

- **The evaluated capability is different.** MPRAbox agents design experiments
  against a live oracle. dismech agents synthesize and structure existing
  literature. Failure to infer a hidden rule from feedback does not directly
  predict failure at faithful curation, which is nearer to reading comprehension
  with citation discipline — the thing our snippet gate does check.
- **Model versions move.** The headline numbers are Claude Opus 4.7, GPT-5.5,
  and Gemini 3.5 Flash in their native harnesses as of the paper. Treat the
  ranking as a snapshot; the framework and the failure modes are the durable
  contribution.
- **One run per CodonBox world**, and four long-horizon MPRAbox runs. The
  qualitative failure modes are vivid and consistent, but per-world outcomes rest
  on single runs.
- **No AI judge was run.** Automated notebook scoring is proposed as future
  work; the notebook evaluation here was human inspection.

## Follow-ups worth considering

- Cite this paper in [Automation & Agents](../explanation/automation-and-agents.md)
  where it explains the LLM-reviewer approval loop, as published support for the
  claim that a passing score is not evidence of understanding.
- Consider a decision-register entry stating that compliance score is never a
  proxy for mechanistic correctness, if that is not already implied by §7.
- When adding an `EMERGING` mechanistic hypothesis, prefer recording a
  discriminating `Experiment` with `would_refute` over extending the supporting
  narrative.
- Revisit whether cross-provider reconciliation prose treats divergence as an
  error signal; adjust toward the shared-lineage question instead.
