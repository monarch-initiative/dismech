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

## Durable assessment history and cost

Successful responses are saved immediately to ordinary, versioned YAML files:

```text
analysis/classification/jev/
  Asthma/evidence_claim_match.yaml
  Cystic_Fibrosis/evidence_claim_match.yaml
```

Each file has an `assessments` mapping keyed by assessment SHA256. The key includes
the model and complete question/state payload: structured assertion, disease and
subtype context, selected snippet, declared support/directness, prompt, and aspect
questions with their slot semantics. No punctuation or whitespace inside strings
is normalized. YAML formatting changes alone do not change the parsed input.
A changed input gets a new record; old records and scores are retained. A return
to an earlier input reuses its saved assessment. Use pinned model versions for
reproducible caching; a moving model alias does not identify a new model release.

| Field | Meaning |
| --- | --- |
| `claim` | Exact extracted claim snapshot, including selected evidence and original YAML pointers. |
| `model_input` | Exact shared state sent to Jev, retained independently of future extraction changes. |
| `input_sha256` | Identity of the model-visible claim/excerpt, independent of model or prompt. Reference metadata and evidence explanations are not model inputs. |
| `configuration_sha256`, `model`, `assessment_source_revision` | Fingerprint of questions/rubric, requested model and assessment source commit when known; the assessment key combines configuration and input. |
| `first_seen_at`, `first_seen_revision` | Earliest retained audit observation of this input, with the source commit when known. **Not the original authoring date.** Imported results without a manifest have a null revision. |
| `assessed_at`, `result` | Original assessment time, per-aspect labels, probabilities/confidence, usage, returned model, and request fingerprint. |
| `active` | Whether this exact model-visible claim/excerpt still occurs in the disease file, as of the recorded inventory. Independent of whether its model/prompt is current. |
| `occurrences` | Most recently observed assertion/evidence pointers and reference IDs; supports repeated identical inputs and reordered lists. |
| `last_seen_at` | Last recorded positive observation; unchanged source files retain their prior observation timestamp. |
| `activity_history` | Observed retirement/reactivation dates and source revisions. A removal is detected at the next inventory, not dated retrospectively. |
| `reassessments` | Subsequent responses from explicit refreshes or independently assessed copies. Cache reads use the latest response; the original remains intact. |

The file's `inventory` records the inspected disease-file hash, extraction-code
and schema fingerprint, source revision, observation time and whether extraction was complete. Unchanged disease snapshots
and cache hits do not churn timestamps. Activity is reconciled against **complete
disease files**, even when inference uses `--section`, `--limit` or a time budget.
Invalid extraction does not retire unseen claims: it records `complete: false`.
The standalone cache command also detects deleted source files. Explicit audit
input selections leave other disease files alone.

Errors are never cached as judgments. Successful cached rows retain their original
assessment date and do not add to new-call token totals. Concurrent identical
requests within one audit share a response. Run only one writer per checkout;
CI shards have separate checkouts. Malformed cache files stop a run instead of
silently spending tokens to recreate their contents. Writes replace one file
atomically; no global cache file is rewritten.

```sh
# Update active flags from current KB files, without inference.
just jev-audit-cache

# Import earlier successful predictions, preserving dates and scores.
just jev-audit-cache --import-results reports/jev-section-smoke/results.jsonl

# Union saved histories from another checkout or downloaded shard.
just jev-audit-cache --merge-cache /path/to/saved/analysis/classification/jev
```

Import verifies assessment hashes against the current questions and extraction;
incompatible results fail rather than being relabeled. YAML history merges retain
older configurations as well as new ones, then reconcile activity with the local
KB. These commands need no API key. An existing SQLite checkpoint is not silently
converted: import its accompanying `results.jsonl` using the command above.

For future derived HTML, look up a score using the **current input and configured
model/prompt hash**, and display its model and `assessed_at`. `active: true` alone
is insufficient: a claim can remain present while the assessment configuration
has changed. `occurrences` provides the current YAML locations, and `result.answers`
provides the aspect paths for display. No HTML rendering is added here.

The first full audit requests each usable assertion/snippet pair once, batching all
its aspect questions. Later runs reuse unchanged results. Inventory the corpus
before a live run; `--max-seconds` bounds scheduling and successful responses survive
partial failures. CSV reports remain disposable; the YAML history is the checkpoint.

## Weekly GitHub Action

[The Jev evidence audit workflow](../.github/workflows/jev-evidence-audit.yaml)
runs every Monday at **09:17 UTC**, using the centrally managed cron profiles.
The `off` profile disables its schedule. Manual dispatch supports an inventory-only
run, a per-shard limit and a model override.

Configure the `TYPESAFE_API_KEY` repository or organization Actions secret before
live runs. Publication uses the existing `AI4C_AGENT_APP_ID` and
`AI4C_AGENT_PRIVATE_KEY` secrets to propose updates to `analysis/classification/jev/`
through an ordinary PR targeting `main`. It never edits KB assertions or benchmark
labels, bypasses review, or enables auto-merge. Only dispatches on `main` publish.

Sixteen stable filename-hash partitions run with at most four jobs in parallel,
each with four API workers. Each job stops scheduling new requests after five
hours so it has time to save its checkpoint and report before the job timeout.
Successful judgments come from the checked-out YAML history and any open assessment
update PR. Reusing that pending PR prevents repeat charges while review is pending.
Only changed per-disease YAML files are uploaded with each shard, including after
partial failure. A separate job unions the checkpoints and reconciles activity
against its checkout of current `main`, then creates or updates the assessment PR.
It writes only the assessment directory and pushes without force. Reports can be
incomplete while successful assessments are still saved for the next run.

The committed history has no Actions-cache expiration. The combined `jev-assessment-history` artifact has 90-day retention; individual
shard artifacts have 14-day retention: if publication fails, recover their `cache/` directories
with `just jev-audit-cache --merge-cache ...` before another paid run. Missing or
unreadable pending history stops inference rather than being treated as an empty
cache. CSV reports and prediction artifacts retain their normal expiration.

Download **`jev-recuration-report`** from the Actions run for combined CSVs, raw
predictions and provenance. Per-shard prediction artifacts are also retained.
Missing shards, failed API requests, or pairs left unassessed after a time limit
produce `complete: false` and an explicitly incomplete combined report
and a failed report job; they are not presented as a full-corpus audit.

To combine downloaded shard artifacts locally:

```sh
just jev-audit-report reports/jev-combined --merge build/jev-shards --expected-shards 16
```

`--merge` expects one subdirectory per artifact, each containing `manifest.json`
and `results.jsonl`. It rejects duplicate partitions or incompatible model,
source, schema, classifier or prompt settings.
