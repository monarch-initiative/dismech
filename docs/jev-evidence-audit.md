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
`--limit 0` means no limit. `--refresh` ignores prior successful results.

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

## Checkpoints and cost

Successful responses are persisted immediately in
`build/jev-audit-cache.sqlite`. The cache key includes the model and complete
question/state payload, including prompt and slot semantics. Changed snippets,
assertions, inherited context, questions or models are reassessed. Errors are never
cached as judgments. Cached rows retain their original assessment date and are
marked `cached`; they do not add to the new-call token totals.

The first complete run makes a request per usable assertion/snippet pair, with
all of that pair's aspect questions batched. Later runs reuse unchanged results.
Use the inventory command to count the current corpus before running it live.
A time-limited run (`--max-seconds`) records unfinished pairs and can resume using
the same cache. Keep cache files for the next run; reports alone are not checkpoints.

## Weekly GitHub Action

[The Jev evidence audit workflow](../.github/workflows/jev-evidence-audit.yaml)
runs every Monday at **09:17 UTC**, using the centrally managed cron profiles.
The `off` profile disables its schedule. Manual dispatch supports an inventory-only
run, a per-shard limit and a model override.

Configure the `TYPESAFE_API_KEY` repository or organization Actions secret before
live runs. The workflow has read-only repository permissions and uploads artifacts;
it does not commit edits, create curation issues or change benchmark labels.

Sixteen stable filename-hash partitions run with at most four jobs in parallel,
each with four API workers. Each job stops scheduling new requests after five
hours so it has time to save its checkpoint and report before the job timeout.
Successful judgments are restored/saved through the Actions cache, including after
partial failures. Cache eviction can cause reassessment and additional API usage.

Download **`jev-recuration-report`** from the Actions run for combined CSVs, raw
predictions and provenance. Per-shard prediction artifacts are also retained.
Missing or unfinished shards produce an explicitly incomplete combined report
and a failed report job; they are not presented as a full-corpus audit.

To combine downloaded shard artifacts locally:

```sh
just jev-audit-report reports/jev-combined --merge build/jev-shards --expected-shards 16
```

`--merge` expects one subdirectory per artifact, each containing `manifest.json`
and `results.jsonl`. It rejects duplicate partitions or incompatible model,
source, schema, classifier or prompt settings.
