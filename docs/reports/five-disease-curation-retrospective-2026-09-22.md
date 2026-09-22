# Custody of a Claim: A Five-Entry Curation Retrospective

**Date:** 2026-09-22
**Scope:** PRs [#12400](https://github.com/monarch-initiative/dismech/pull/12400),
[#12402](https://github.com/monarch-initiative/dismech/pull/12402),
[#12409](https://github.com/monarch-initiative/dismech/pull/12409),
[#12430](https://github.com/monarch-initiative/dismech/pull/12430),
[#12433](https://github.com/monarch-initiative/dismech/pull/12433) — five agent-curated
disease entries taken from claim to merge in one batch.

Every error made in this batch was caught by something before it reached `main`. Which
*something* — an automated gate, a self-check, or a reviewer — turns out to be the whole
finding, because the three categories catch different kinds of error and one class of
claim falls outside all three.

## What was built

Five ultra-rare Mendelian disorders claimed from the curation queue, each researched,
curated, opened as its own pull request, and driven through review to approval.

| PR | Disease | Gene | Snippets | Phenotypes wired | Review rounds |
|---|---|---|---|---|---|
| [#12402](https://github.com/monarch-initiative/dismech/pull/12402) | Chassaing–Lacombe chondrodysplasia | `HDAC6` | 38 → 43 | 1/9 → 1/9 | 3 |
| [#12400](https://github.com/monarch-initiative/dismech/pull/12400) | Isolated TSH deficiency | `TSHB` | 50 → 66 | 3/7 → 11/11 | 2 |
| [#12409](https://github.com/monarch-initiative/dismech/pull/12409) | EBS7 with nephropathy and deafness | `CD151` | 61 → 76 | 4/13 → 7/13 | 2 |
| [#12430](https://github.com/monarch-initiative/dismech/pull/12430) | Neuromuscular oculoauditory syndrome | `DHX16` | 42 → 46 | 4/11 → 8/11 | 1 |
| [#12433](https://github.com/monarch-initiative/dismech/pull/12433) | Kariminejad neurodevelopmental syndrome | `RBSN` | 19 → 43 | 2/4 → 14/14 | 2 |

Both numeric columns are measured at the PR's first commit and again at the merged entry
on `main`. Every snippet counted is an exact quote verified against a cached reference.
The phenotype column is the fraction of clinical features that a causal edge actually
explains (`just list-disconnected-phenotypes`).

Phenotype connectivity was the single most repeated review finding in the batch, raised as
*blocking* on #12400 and #12409, which is why the last two entries were wired before they
were opened. It was **not** raised on #12402, and that row is the one worth reading: the
`HDAC6` entry went through review at 1/9 and merged at 1/9, because the bridge from the
molecular lesion to the skeletal phenotypes is unevidenced. The reviewer said so
explicitly — *"I am explicitly not asking for that edge"* — and the gap is recorded as a
`KNOWLEDGE_GAP` with two proposed experiments rather than invented. An edge added to clear
a report is worse than no edge, and this is what that looks like when the tooling and the
reviewer both agree to leave a number low.

The review-rounds column carries its own lesson. #12402 took three rounds because the
first review **approved** it and I then pushed two more commits — fixing real defects I
had found myself, but at the cost of dismissing the approval and buying two further
reviews. `main` dismisses stale approvals on every push, so a two-line fix and a rewritten
section cost the same. Everything I intend to change has to go in one push, including the
things I find on my own after the verdict lands.

## The ledger

Thirteen errors reached a draft. None reached `main`. The useful question is not how many
there were but what stopped each one, because the categories do not overlap and one of
them is empty by construction.

| Caught by | Count | What it means |
|---|---|---|
| A gate | 6 | An automated check refused the commit. |
| Self-check | 4 | Caught by re-reading a source or re-running a query. |
| A reviewer | 3 | Reached a PR and was found by review. |
| *Nothing could have* | *5* | Of the above, the number no gate could ever have caught. |

### Caught by a gate

Five ontology identifiers written from memory, plus one fabricated reference title. Each
is well-formed, plausible, and names a different concept from the one intended. None felt
like invention while being written.

| Written as | Actually is |
|---|---|
| `NCIT:C16340` "Blood Group Determination" | *Biomedical Ethics* — replaced with `NCIT:C210738` Blood Typing Test |
| `NCIT:C38086` "Laboratory Procedure" | *Renography* |
| `NCIT:C177209` "Newborn Screening" | *Believe* |
| `NCIT:C18132` "Optical Coherence Tomography" | *Parallel Computing* (its cache row is still in the repository — see [#12472](https://github.com/monarch-initiative/dismech/issues/12472)) |
| `HP:0012103` "Abnormal mitochondrial morphology" | The CURIE is real; the label is *Abnormality of the mitochondrion*. A label copied from memory rather than from the lookup. |

The sixth was a **composed reference title**. "Rabenosyn-5 suppresses non-homologous end
joining…" was written for `PMID:35652444` on four evidence items before the cache was
checked; the real title is about separation-of-function mutations uncoupling endosomal
recycling from lysosomal degradation. `just check-reference-titles` exists for exactly
this, and it caught it.

This is the failure mode CLAUDE.md already documents under *Every CURIE is read from a
source in the same step it is written*. The gate held every time — and that is the least
interesting half of the story, because the errors it cannot see have a different shape.

### Caught by re-reading the source

| Claim as drafted | What the source actually said |
|---|---|
| A quotation attributed to `PMID:38188895` describing "a school urine dipstick screening program" | The paper says the boy's mother tested his urine at home. Caught by checking the quote against the cache before committing. |
| "GO has no alpha-tubulin-specific process term" | `l~tubulin deacetylation` had been run and generalised past. `l~alpha-tubulin` returns `GO:0071929` and `GO:0043014`. |
| "No specific HPO term for mtDNA depletion" | `HP:0009141` *Depletion of mitochondrial DNA in muscle tissue* is an exact match. The coarse binding and its stated justification both went. |
| "`preflight-dr` does not distinguish a phenotype MIM from a gene MIM" | Testing the regex showed it never sees the phenotype MIM at all: the report writes `**OMIM:**` and markdown bold defeats the pattern. The conclusion held; the reason was invented. |

### Caught by a reviewer

**A comparison refuted by its own numbers.** A pooled prevalence range of 3.3–7.7 per
100,000 was said to "sit below" a Dutch figure of 1 in 16,000, with an inference about
ascertainment built on top. 1 in 16,000 is 6.25 per 100,000 — *inside* the range. Both
conversions elsewhere in the same block are correct and show their working; only the
sentence relating them was false.

**A justification falsified by improving the entry.** A phenotype carried
`coarse_binding_basis: SOURCE_UNSPECIFIED`, true when written, because the only source
said "facial dysmorphisms" and stopped. A better source that enumerates eight features was
then added three lines below the declaration, and the basis was never revisited. The fix
split those eight features into their own phenotypes with individually verified HPO terms.

**A search run and then misreported.** A curation note said an ECTO query returned "only
ambient air and water pressure classes". It also returned `ECTO:1000019`, `ECTO:4000025`
and `ECTO:4000026`, none of which is air- or water-specific. The binding decision stands;
the summary of the output did not. The reviewer graded it non-blocking and approved, and
I chose not to spend a round on wording alone — so **the inaccurate sentence is still in
`main`** at `Epidermolysis_Bullosa_Simplex_7_With_Nephropathy_And_Deafness.yaml:131`. It
is recorded here, not repaired.

That last one is a category of its own. The first two negative-existence failures were
searches *generalised past their output*. This was a search whose output was read and then
described inaccurately anyway. Running the query and reporting it faithfully are separate
acts, and only the first one feels like diligence.

## What nothing can catch

Five of the thirteen belong to one class, and this repository's own documentation already
names it: a negative-existence claim is the single assertion in an entry that no gate can
reach.

Writing "no HPO term exists for this", "no module covers this mechanism", or "no transplant
outcome has been reported" asserts something about the state of an ontology or a
literature. Nothing in the validation stack can evaluate it. The only thing standing
between a false negative and the knowledge base is whether somebody re-types the search.

Five were written here. Two were caught by reviewers, two by re-running the query, one by
a reviewer after the query had been run. The most instructive is the fourth, found during
a self-audit on the last day: an entry asserted that no kidney-transplant outcome had ever
been reported for the disease, and **the search had never been run at all** — nine hours
after filing an issue about precisely this failure mode.

> A false justification is worse than no justification. It tells the next reviewer the
> check has been done, so they skip the one action that would catch it.

When the search was finally run the negative held — and it turned up a case report worth
carrying: `PMID:28615054`, a patient with laminin-5 epidermolysis bullosa, bilateral
sensorineural deafness and end-stage renal disease in whom transplantation was pursued.
Laminin is the ligand whose integrin binding CD151 stabilises: the same adhesion axis,
failing from the other side, arriving at the same endpoint. It is cited in the entry now.
Verifying the negative is what found it.

This is the same rule CLAUDE.md states under *Naming the query does not make the note
true; re-running it does*. The batch is four more instances of it.

## Metadata that would help judge evidence

Four gaps where the knowledge base cannot record something a reader needs in order to
weigh a claim. Each was found by hitting it, not by looking for it.

**[#12410](https://github.com/monarch-initiative/dismech/issues/12410) — verification
depth is not recorded.** A snippet verified against a 200-word abstract and one verified
against a results section read identically in the YAML. The reference cache knows which
(`abstract_only` against three full-text forms; 3,703 versus 272 in the 4,000-file sample
behind #12410 — a sample that skews low, since across all 46,104 `PMID_*.md` caches it is
33,478 abstract-only against 12,379 full-text, about 27%)
but the evidence item has no slot for it. This silently shapes what gets curated: the
founding clinical paper for one of these five diseases is abstract-only, which is *why*
eight real phenotypes were dropped from that entry, and nothing distinguishes "not
reported" from "reported, not quotable".

**[#12411](https://github.com/monarch-initiative/dismech/issues/12411) — negative claims
are unverifiable prose.** The remedy is not more discipline; it is making the recorded
search replayable — source adapter, query string, date, result — so a recipe can
re-execute it and fail when a query recorded as empty now returns hits. That converts the
one assertion no gate can reach into an ordinary gate, and it catches ontology releases
that later add the term.

**[#12416](https://github.com/monarch-initiative/dismech/issues/12416) — an evidence item
cannot say how much evidence it is.** 131,641 evidence items are graded `HUMAN_CLINICAL`
(22 September; it was 127,512 the previous day — the figure moves with every curation PR);
a single kindred and a population cohort are indistinguishable. For ultra-rare disease the entire
literature is often one family. The project already accepts the principle in three
separate silos — `cohort_size`, `sample_count`, `CASES_IN_LITERATURE` — but not at the
level where claims are made.

**[#12472](https://github.com/monarch-initiative/dismech/issues/12472) — a wrong lookup is
permanent.** `NCIT:C18132` *Parallel Computing* sits in a committed cache because term
validation fetched the row before the binding was discovered to be wrong. The binding
went; the row stayed. Hand-editing caches is forbidden, no recipe reaps orphans, and the
documented recovery procedure covers rows that are *wrong* — this one is correct data that
nothing references. It is not one row: when measured for that issue on 21 September, 278 of 22,879 committed
term-cache rows were referenced by nothing in the repository, accumulating month over month. Not all 278 are
necessarily error residue — a row may be a binding removed for good reasons, or a lookup
made while deciding — and that is the point. Nothing distinguishes a mistake from a
withdrawal, and there is no supported way to remove either.

### One more, unfiled

**Near-misses leave no trace.** Two fabrications in this batch were caught before commit,
so they appear in no gate's output and no metric. The gates only ever see what is
committed, which means the measured error rate is the rate of errors that survived
attention — not the rate of errors.

## Tooling bugs filed

Three, all found by using the tools rather than auditing them.

**[#12403](https://github.com/monarch-initiative/dismech/issues/12403) — quota exhaustion
reported under three wrong causes.** Filed at 05:28; by 05:31 it was identified as the
*third* independent report of the same defect. The sharper finding came later, from
reading the workflow source in a job log: the file already contains a correct quota branch
with the right diagnosis and remedy. Its match list checks for `"usage limit"`; the
runtime string is `"You've hit your limit"`. The good message has never once printed.

**[#12414](https://github.com/monarch-initiative/dismech/issues/12414) — an identifier
check blind to markdown bold.** A preflight warns that a report's OMIM disagrees with the
ontology, when the report cites the right one three times — always as `**OMIM:**`, which
its pattern cannot cross. Re-measured over the 6,150 `research/*-deep-research-*.md`
files: 538 carry the bold form, and in 151 of those the extractor's regex finds no MIM
anywhere in the file. (#12414 itself quotes 314 and 67. I cannot reproduce those under any
scope I have tried, and the corpus grew by 21 files in the interval, so the difference is
not growth — the issue's figures are wrong and I have said so on it.)

**[#12415](https://github.com/monarch-initiative/dismech/issues/12415) — a check that is
wrong five times out of six.** Research-report term validation pairs each identifier with
the wrong table cell, so it reports the *frequency* column as the term's name —
"Frequent", "Core", "Index kindred". On one report all six findings were artifacts except
one, and that one was a genuinely wrong binding, worded identically to the noise. A second
report gave three out of three spurious. A list that is 83% false teaches you to skip it,
which is where the real finding was hiding.

## Two things worth keeping

### Disagreeing with a review beat complying with it

Three times the response to a review was something other than what it asked for, and in
each case the reviewer preferred the result. A disconnected node was parented on the
molecular lesion rather than the suggested downstream state, because the absent molecule
*is* the analyte a screening test measures — "better than the one I suggested… avoids
inventing an intermediate node." A missing treatment became a *diagnosis* entry, because
the sources support an audiology referral and no report describes a device or an outcome —
"more defensible than my own suggestion, which leaned on a generic standard-of-care line."
And a coarse node offered `PATHOGRAPH_HUB` was refused, because a hub is defined by
convergence and that node is one arm of a fourteen-way fan-out.

### A failed research run is content

Deep research succeeded for four of the five diseases. The fifth failed twice — once to a
concurrency mistake, once to a two-hour provider timeout that produced nothing. Rather
than substitute another provider or let the PR imply a pass, the entry records both
attempts, the job identifier, the timestamps, and the fact that everything in it came from
primary literature instead. The reviewer approved it on the first pass and said so
explicitly: the rule guards against under-consuming an artifact that exists, and there was
none to under-consume.

The run that did land earned its place on something missed rather than on mechanism: it
named the founding clinical description the syndrome is *named after*, published seven
years before the gene was found, which the draft entry did not cite. It supplies the
electrophysiology, the brain imaging, the actual ocular finding behind a one-word
phenotype, and the only enumeration of the facial features anywhere in the literature.

## Caveats on the numbers

Counts in the ledger are of errors that reached a draft, not of errors committed. Every
figure quoted from the knowledge base was measured on 21–22 September 2026 and moves with
the corpus — re-run the recipes rather than trusting the numbers here. The batch is five
entries curated by one agent in one sitting; it is a worked example of where errors get
caught, not a measured error rate for the project.
