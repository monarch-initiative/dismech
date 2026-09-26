# Jev evidence audit

`just jev-audit` checks the selected snippets against the structured assertions in
all `kb/disorders/*.yaml` files, and produces a queue for recuration. It uses the
same MATCH / MISMATCH / PARTIAL rubric as the evidence-claim-match benchmark.
These are model judgments of snippet support, not curator labels, source-quality
ratings, or judgments of whether a disease assertion is true elsewhere.

## Run locally

Set `TYPESAFE_API_KEY` in your environment for live runs. No key is needed for
inventory or report generation. The default model is `jev-1.13.0`.

```sh
# Discover all assertion/evidence pairs without API calls.
just jev-audit-inventory

# Assess every pair, reusing unchanged successful inputs.
just jev-audit

# A small selection before a larger run (the limit includes missing evidence).
just jev-audit --input kb/disorders/Asthma.yaml --section phenotypes --limit 20

# Regenerate CSVs from saved predictions without inference.
just jev-audit-report

# Inspect all options.
just jev-audit --help
```

`--input` accepts a Disease YAML file or directory and can be repeated. The default
is the entire disorders corpus, including every section and nested evidence-owning
object. This does not load separate module, grouping or comorbidity documents,
whose root objects differ from Disease. `--section` is repeatable; no section
filter is applied by default. `--workers` controls concurrency (default 4).
`--limit 0` means no limit. `--refresh` explicitly buys a new assessment while
preserving the previous response in `reassessments`.

## What gets assessed

Each evidence item is paired with its owning assertion, retaining disease,
ancestor and subtype context. The claim remains a structured object. Each request
asks independent questions about `/` (the whole claim), `/about/disease`, each
inherited context binding, and all present assertion fields. Term ID/label pairs
are assessed together; other nested fields receive their own paths. Scalar lists,
including subtype lists, are assessed as one aspect.

Independent relationship edges (`CausalEdge`, `TreatmentMechanismTarget`, and
`EnvironmentalMechanismTarget`) are excluded from the parent assertion and
assessed through their own evidence. This includes pathophysiology downstream
edges and phenotype sequelae. Other compound fields, such as biochemical readouts,
remain part of the complete parent claim. A missing edge snippet cannot be
rescued by evidence on the parent.

The excerpt is evaluated on its own. No cached reference text or evidence-item
explanation is supplied. The declared SUPPORT / REFUTE / NO_EVIDENCE relationship
and any DIRECT / INDIRECT annotation remain in scope. The prompt allows reasonable
contextual implication and faithful broader abstractions. A proposed mechanism
is not interpreted as a clinical recommendation. Quote fidelity and ontology
validation remain separate deterministic checks.

## Reports

Reports are generated under `reports/jev-audit/` (inventory defaults to
`reports/jev-inventory/`). Rerunning replaces the reports in that directory.

| File | Contents |
| --- | --- |
| `entries.csv` | One row per entry with assertion counts, model outcomes, missing evidence, failures and a recuration rank. |
| `aspects.csv` | One row per assessed aspect and evidence item, including YAML pointers, exact aspect value, excerpt, reference, labels, all three probabilities and confidence. Unassessed inputs have a status and no label. |
| `results.jsonl` | Exact structured claim snapshots, predictions, original assessment timestamps, usage and request fingerprints. |
| `inventory.jsonl` | The selected assertion/evidence pairs before inference (local and individual shard runs). |
| `manifest.json` | Source revision, schema and classifier fingerprints, model, prompt, selection, completion state and totals. Combined CI runs retain each shard's manifest. |
| `summary.md` | Counts and the first 20 entries in the priority queue; also used as the Actions run summary. |

`entries.csv` sorts by the number of **distinct assertions with at least one
MISMATCH**, then maximum mismatch probability, then distinct assertions with
PARTIAL, then missing evidence. More excerpts or more aspects do not multiply the
assertion count. An assertion can have both MISMATCH and PARTIAL aspects and
therefore appear in both counts. This is a snippet-repair queue: a different
snippet supporting the same assertion does not cancel a mismatched snippet.

Root outcomes and individual-aspect counts are separate columns. PARTIAL means
weak, incomplete, mixed or uncertain support; it is not counted as MISMATCH.
Probabilities are retained for sorting and review, not treated as measured accuracy.

Missing evidence, missing snippets and invalid input (for example, an unresolved
subtype) have distinct statuses. Invalid KB input is a reported curation issue;
it does not stop other assessments. API failures and pairs left unassessed after
a time limit cause a nonzero exit **after reports are written**. Authentication
failure stops new requests while retaining cache hits and recording remaining
pairs as unassessed. No KB files are changed.

## Queue reviews for the curation agent

The `Jev Recuration Issues` workflow reads the latest overall queue on
dismech-evals `main` and opens up to five issues each Tuesday. Manual dispatch
can preview or create up to 25 issues. Its schedule follows the repository's
cron profiles, including the `off` switch.

```sh
just plan-eval-issues 5       # Preview; no GitHub writes or model calls
just enqueue-eval-issues 5    # Create the issues
```

Issues carry `curation` and `jev-recuration`, so the existing ai4c-agent
curation scanner can pick them up. Their titles use the disease filename,
for example `Jev evidence review: Asthma.yaml`. A small HTML comment in the
body preserves that identity if the title is edited. Every run lists both
open and closed labelled issues through GitHub's paginated issues API;
previously queued diseases are skipped. Reopen the existing issue when a
second review is wanted. Keep its `jev-recuration` label.

The intake accepts delayed or incomplete evaluation results. It skips files
that are no longer in the current KB and asks the agent to compare the saved
findings with current content before editing. It does not require matching
revisions. Issues link to the current YAML, dashboard and full assessment
history, with a few example findings. Jev's flags request review; they do not
instruct the agent to make a change where the content is already correct.

Only the latest published overall top-25 queue is considered. If fewer than
N entries remain after duplicate and missing-file checks, fewer issues are
created. An empty queue creates none; a failed download or GitHub read fails
the job before any issues are created. Reruns after a partial publication
skip issues already created. No separate claim-disease workflow or local
curation-state files are used.

## Assessment history lives in dismech-evals

The public [dismech-evals repository](https://github.com/monarch-initiative/dismech-evals)
owns corpus assessment history and the weekly workflow. Dismech owns extraction,
the classifier and these CLI commands. The private dismech-bench repository remains
focused on curated benchmark cases, reviews and benchmark results.

A local audit defaults to the ignored `build/jev-assessments/` directory. To use a
sibling evaluation checkout, run from the **dismech source checkout**:

```sh
just jev-audit --cache ../dismech-evals/analysis/classification/jev
just jev-audit-cache --cache ../dismech-evals/analysis/classification/jev
```

Do not commit corpus assessment YAML to dismech. In dismech-evals the layout is:

```text
analysis/classification/jev/
  Asthma/evidence_claim_match.yaml
  Cystic_Fibrosis/evidence_claim_match.yaml
```

Version 2 stores each input once, shared across model and prompt configurations:

| Mapping | Contents |
| --- | --- |
| `inputs[INPUT_SHA256]` | One canonical `claim` snapshot: the exact shared state sent to Jev. Separate `origin` and `evidence_metadata` preserve source pointers and excluded citation metadata. |
| `assessments[ASSESSMENT_SHA256]` | An `input_sha256` reference, configuration fingerprint, requested model, source revision, original assessment timestamp, per-aspect results and any reassessments. No repeated claim snapshot. |

The input record owns `first_seen_at`, `first_seen_revision`, `last_seen_at`,
`active`, `active_as_of`, `occurrences` and observed `activity_history`.
First seen means the earliest retained audit observation, **not the original
writing date**. Unknown source revisions remain null. Activity means the exact
model-visible claim/excerpt still occurs in the source file at the recorded
observation; it is independent of model or prompt currency.

The assessment hash covers the model, exact input, prompt and aspect questions
including slot semantics. Punctuation changes inside strings produce a new input;
YAML formatting alone does not. Historical inputs and scores remain, and restoring
old wording reuses its saved response. An explicit `--refresh` retains previous
responses. Use pinned model versions, since a moving alias does not identify a
new release. API failures are not cached as judgments.

Each file's `inventory` records source and extraction fingerprints, source revision,
observation time and completeness. Activity uses complete disease files even when
inference is limited by section, pair count or elapsed time. Invalid extraction
does not retire unseen claims. Unchanged inventories do not churn timestamps.
The standalone cache command also detects deleted source files.

```sh
# Import successful predictions without inference; original dates/scores survive.
just jev-audit-cache --cache ../dismech-evals/analysis/classification/jev \
  --import-results reports/jev-audit/results.jsonl

# Merge saved checkpoints and reconcile activity against this source checkout.
just jev-audit-cache --cache ../dismech-evals/analysis/classification/jev \
  --merge-cache /path/to/downloaded/cache
```

Import verifies assessment hashes against the current inference configuration.
History merges retain older configurations too. Version 1 YAML is upgraded without
inference; the duplicate claim/model-input copies become one shared snapshot.
Malformed caches fail rather than silently buying their contents again. Writes
replace one file atomically. Use one writer per checkout; workflow shards each
have their own checkout. A time-limited audit retains successful responses and
marks unfinished work in its reports.

For future HTML, a build can consume an evaluation export pinned to a dismech-evals
revision. Match the current input **and** configured assessment hash before showing
a score, and display the model and assessment date. `active: true` alone is not a
freshness check. No history download or evaluation dependency is added to ordinary
dismech builds, and HTML integration is deferred.

## Weekly workflow and reports

The [weekly workflow in dismech-evals](https://github.com/monarch-initiative/dismech-evals/blob/main/.github/workflows/weekly.yaml)
runs Monday at 09:17 UTC. It records the exact source commit and uses a separately
pinned classifier commit, so data can advance while the evaluation method remains
stable. All shards in a run use the same revisions and model. The dismech cron
profiles do not control this external workflow.

The evaluation repository's `TYPESAFE_API_KEY` secret supplies inference credentials.
Only its publication job receives `contents: write`, using its own `GITHUB_TOKEN`
to commit generated assessment data and run summaries directly to **dismech-evals**.
These data updates are automatic; there is no human approval or PR merge stage.
It has no write credentials for dismech or dismech-bench and never changes curated
assertions or benchmark labels. Code/configuration changes remain ordinary GitHub
changes, separate from generated data publication.

Sixteen filename partitions run with up to four jobs in parallel and four workers
per job. Successful assessments are reused from the checked-out evaluation history.
The publication job unions completed checkpoints even when some inference jobs
fail. It pushes without force; unpublished checkpoints remain downloadable if
publication fails. Recover them before a new paid run to avoid repeat charges.

CSV reports, complete prediction streams and provenance are workflow artifacts;
small recuration summaries are also published in dismech-evals. Missing shards,
API failures and time-limited runs remain explicitly incomplete.

To combine downloaded shard artifacts locally:

```sh
just jev-audit-report reports/jev-combined --merge build/jev-shards --expected-shards 16
```

`--merge` expects one subdirectory per shard, containing `manifest.json` and
`results.jsonl`. It rejects duplicate partitions or incompatible configurations.
