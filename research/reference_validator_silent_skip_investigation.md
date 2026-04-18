# Reference Validator Silent Skip Investigation

Date: 2026-04-15
Repo: `monarch-initiative/dismech`
PR investigated: `#1379`

## Executive Summary

The critical claim is **not confirmed**.

A missing `references_cache/PMID_*.md` file does **not** cause `linkml-reference-validator` to silently skip the entire disorder file. In the installed version here, `linkml-reference-validator 0.1.8`, the behavior is:

1. Try in-memory cache.
2. Try disk cache.
3. If the cache file is missing, attempt a live fetch from the reference source.
4. If fetch fails, emit an issue for the specific evidence item(s) that cite that reference.
5. Continue validating the rest of the file.

The misleading part is the CLI summary line:

```text
Validation Summary:
  Total checks: 0
```

In `0.1.8`, `Total checks` is actually the number of **issues emitted**, not the number of snippets validated. A clean validation therefore always prints `Total checks: 0`, even when many snippets were validated successfully.

The real risk is not a silent bypass. The real risk is **non-determinism**: if a curator forgets to commit a cache file, CI may still pass because the validator can fetch the PMID live during the run.

## 1. Installed Validator Version and Source Inspection

The requested command `uv run pip show linkml-reference-validator` did not work in this environment because the ephemeral environment did not have `pip` installed as a module. I confirmed the installed version with Python metadata instead:

```bash
uv run python - <<'PY'
import importlib.metadata as md
print(md.version("linkml-reference-validator"))
print(md.distribution("linkml-reference-validator").locate_file(""))
PY
```

Result:

- Version: `0.1.8`
- Location: `.venv/lib/python3.12/site-packages`

### Relevant code paths

#### Missing cache file does not short-circuit the file

`ReferenceFetcher.fetch()` checks disk cache first, then falls through to a live fetch when the cache file is absent:

- `.venv/lib/python3.12/site-packages/linkml_reference_validator/etl/reference_fetcher.py:61-114`
- `.venv/lib/python3.12/site-packages/linkml_reference_validator/etl/reference_fetcher.py:360-385`

Key behavior:

- `_load_from_disk()` returns `None` if the cache file does not exist.
- `fetch()` then resolves the appropriate source and calls `source.fetch(...)`.
- If live fetch succeeds, it writes the cache back to disk.

#### A failed fetch produces a per-evidence validation failure

`SupportingTextValidator.validate()` calls `self.fetcher.fetch(reference_id)` and, if it gets no reference back, returns an invalid `ValidationResult` with:

```text
Could not fetch reference: PMID:...
```

Source:

- `.venv/lib/python3.12/site-packages/linkml_reference_validator/validation/supporting_text_validator.py:136-185`

This is not a whole-file skip. It is a failure for that specific validation attempt.

#### The plugin keeps traversing the file and only yields failures

`ReferenceValidationPlugin._validate_instance()` recursively walks the object tree and calls `_validate_excerpt()` for each discovered `snippet`/`reference` pair:

- `.venv/lib/python3.12/site-packages/linkml_reference_validator/plugins/reference_validation_plugin.py:180-245`

`_validate_excerpt()` only yields a `LinkMLValidationResult` when the validation failed:

- `.venv/lib/python3.12/site-packages/linkml_reference_validator/plugins/reference_validation_plugin.py:488-521`

That means successful validations are silent. The report only accumulates failures.

#### Why `Total checks: 0` is misleading

The CLI prints:

```python
typer.echo(f"  Total checks: {len(all_results)}")
```

where `all_results` is only the list of emitted validation results, i.e. issues:

- `.venv/lib/python3.12/site-packages/linkml_reference_validator/cli/validate.py:287-320`

So in `0.1.8`:

- `Total checks: 0` means `0 issues`
- It does **not** mean `0 snippets validated`

#### Repo wrapper does not change this control flow

`dismech` runs the validator through `scripts/run_reference_validator.sh`, which imports `dismech.patch_reference_validator` before invoking the upstream CLI:

- `scripts/run_reference_validator.sh`
- `src/dismech/patch_reference_validator.py:27-88`

That patch only adds retry-and-return-`None` behavior around PubMed/PMC network calls. It does not change traversal semantics and does not introduce a file-level skip.

## 2. Local Reproduction

### Control run on a known-good file

I used `kb/disorders/Autoimmune_Encephalitis.yaml`, which cites two cached PMIDs:

- `PMID:31326280`
- `PMID:23290630`

Control run:

```bash
just validate-references kb/disorders/Autoimmune_Encephalitis.yaml
```

Output:

```text
Validating kb/disorders/Autoimmune_Encephalitis.yaml against schema src/dismech/schema/dismech.yaml
Cache directory: references_cache

Validation Summary:
  Total checks: 0
  All validations passed!
```

This already shows that `Total checks: 0` is normal for a passing run.

### Exact requested reproduction: temporarily hide one cache file

I temporarily moved `references_cache/PMID_31326280.md` out of the cache directory, ran:

```bash
just validate-references kb/disorders/Autoimmune_Encephalitis.yaml
```

and then restored the original file.

Output was still:

```text
Validation Summary:
  Total checks: 0
  All validations passed!
```

Interpretation:

- The validator did **not** skip the whole file.
- It fell back to a live fetch for the missing PMID and completed successfully.

### Deterministic forced-failure harness

Because the normal `just` run can refetch live data, I also ran an isolated harness with:

- a temporary cache directory containing only `PMID_23290630.md`
- `PMID_31326280.md` intentionally omitted
- live fetch for `PMID:31326280` monkey-patched to return `None`

Observed result:

```text
issue_count 8
issues_by_reference Counter({'PMID:31326280': 8})
validate_calls_by_reference Counter({'PMID:31326280': 8, 'PMID:23290630': 2})
network_calls Counter({'PMID:31326280': 8})
```

And the emitted failures were all specific to `PMID:31326280`, e.g.:

```text
INVALID PMID:31326280 phenotypes[0].evidence[0].snippet Could not fetch reference: PMID:31326280
```

This is the decisive reproduction:

- the missing PMID caused failures only for evidence items that cite that PMID
- evidence items citing the other PMID were still validated
- the file was **not** silently skipped

## 3. CI Evidence for PR #1379

### Current PR head

Current PR head:

- SHA: `bc506e7f669c7bd7fa4a47d8359600d141675a5a`
- Checked via `gh pr checks 1379`

Current checks are green:

- `test (3.13)` passed
- `claude-review` passed

Current PR file list includes:

- `references_cache/PMID_32477874.md`
- `references_cache/PMID_37476587.md`
- `references_cache/PMID_38923610.md`

So the current PR head already contains the previously alleged missing cache file.

### Intermediate commit where the review comment was made

The relevant review comment was posted on `2026-04-16T01:12:08Z` against commit:

- `361351604a9324bded5e73997357225a5bde6096`

That commit modified only:

- `kb/disorders/Glycogen_Storage_Disease_XV.yaml`

and did **not** add `references_cache/PMID_37476587.md`.

Associated CI run:

- Build and test: `24486472624`
- Job: `71562434704`

From the job log:

- Changed-file loop included:
  - `kb/disorders/Glycogen_Storage_Disease_XV.yaml`
  - `references_cache/PMID_32477874.md`
  - `references_cache/PMID_38923610.md`
- It did **not** include `references_cache/PMID_37476587.md`

The same job then ran reference validation on the disorder file and printed:

```text
Validating kb/disorders/Glycogen_Storage_Disease_XV.yaml against schema src/dismech/schema/dismech.yaml
Cache directory: references_cache

Validation Summary:
  Total checks: 0
  All validations passed!
```

This is exactly the run that appears to have triggered the mistaken review conclusion.

### What the CI log actually proves

The CI log proves only this:

- the cache file was absent from the committed diff at that commit
- the validator exited successfully
- the CLI reported `Total checks: 0`, which in `0.1.8` means `0 issues`

The CI log does **not** prove:

- that the file was skipped
- that zero snippets were validated
- that missing cache disables the whole file

Given the source code and local reproductions, the most likely explanation is:

1. `PMID_37476587.md` was missing from the repo at that commit.
2. The validator fetched `PMID:37476587` live during CI.
3. All snippet validations passed.
4. The CLI summary was misread because `Total checks` is badly named.

## 4. Severity Assessment

The claimed architecture-breaking bug is **not present**.

### Not supported by evidence

I found no evidence that:

- one missing cache file silently disables all reference validation for a disorder file
- fabricated snippets in other evidence items can pass because one unrelated PMID cache is missing

### Real remaining concern

There is still a meaningful reliability issue:

- reference validation is **not deterministic** if cache completeness is not enforced
- CI can pass when a cache file is missing, because the validator may fetch the reference live
- reviewers can be misled by the `Total checks: 0` wording

So the risk is:

- **not** silent anti-hallucination bypass
- **yes** to network-dependent validation and confusing reporting

Severity assessment:

- Silent whole-file bypass: **not confirmed**
- Deterministic CI gap / review confusion: **real and worth fixing**

## 5. Recommendation

### Upstream validator behavior

For a generic validator library, the best default is still:

- **(a) validate what it can and skip/fail only the specific missing reference**

That is already the effective behavior, except that a missing reference currently becomes an emitted issue only if live fetch fails.

I do **not** recommend `(c) WARN loudly but continue` as the only behavior for a missing cache in `dismech`, because a warning-only policy keeps CI nondeterministic and easy to ignore.

### Dismech CI/repo policy

For `dismech`, the better operational policy is:

- **(b) fail when a cited PMID cache file is missing**

But I recommend implementing that as a **repo-level precheck**, not by changing the upstream validator’s default behavior for all users.

Reason:

- `linkml-reference-validator` is a general-purpose tool; live-fetch-on-miss is reasonable there
- `dismech` wants deterministic anti-hallucination enforcement in CI
- a repo-side precheck is fast, explicit, and easy to understand

### Concrete fix

Add a CI/pre-validation guard that:

1. Scans the target YAML file(s) for cited references.
2. Ignores prefixes explicitly listed in `skip_prefixes`.
3. Verifies that each cited `PMID:` has a corresponding `references_cache/PMID_*.md`.
4. Fails with a message that prints the exact `just fetch-reference ...` commands needed.

This would convert:

- a confusing network-dependent pass

into:

- a deterministic and actionable failure

### Nice-to-have upstream improvement

Even though I do **not** think there is an upstream silent-skip bug, the CLI summary should be improved. At minimum:

- rename `Total checks` to `Total issues`
- add a separate success counter such as `Validated excerpts: N`

That change would have prevented this investigation entirely.

## 6. Disposition

- Upstream `linkml/linkml-reference-validator` bug issue: **not filed**
  - Reason: the claimed bug was not reproduced or supported by source review.
- `dismech` repo issue for cache completeness guard: **filed**
  - Issue: `monarch-initiative/dismech#1396`
  - Title: `Add CI precheck for missing cited reference cache files`
