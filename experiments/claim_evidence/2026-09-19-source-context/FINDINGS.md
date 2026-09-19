# Does source context help evaluate the selected snippet?

Yes in this small paired test: adding the source corrected one wrong-entity
acceptance, with no other label changes. The task remained judging the selected
snippet, not finding evidence elsewhere in the paper.

## Design

17 cases, two arms, three repetitions each: 102 live TypeSafe requests to
`jev-1.13.0`, with no errors. Both arms used exactly the same prompt and answer
criteria. Their only input difference was the presence of `source_text`.
Order alternated between arms across cases and repetitions.

The simplified task fixes SUPPORT and DIRECT. Input is just `claim`, `snippet`,
and optional `source_text`; no curator explanation, expected label, rationale,
or exemplars is sent to the model. `task.json` preserves the exact prompt.

The key instruction was:

> Support elsewhere in source_text does not rescue an irrelevant or insufficient
> snippet. The selected snippet must carry the evidence for the claim.

`cases.jsonl` freezes inputs, expectations and source provenance. `results.jsonl`
contains every response, repetition, model, probability, usage and request hash.
The request is reconstructed from the selected case's claim/snippet, its source
only in the with-source arm, and `task.json`'s instructions/criteria.

## Results

| Arm | Correct cases in each repetition | Correct assessments across three repetitions |
| --- | --- | --- |
| Claim + snippet | 16/17 | 48/51 |
| Claim + snippet + source | 17/17 | 51/51 |

All eight expected matches were accepted in both arms. Eight of nine expected
mismatches were detected without source; all nine were detected with source.
Labels were stable across all three repetitions, although probabilities varied.
These are 17 selected cases, not 51 independent examples.

### Concrete correction: which patients?

The two `cropped_*` cases use exactly the same selected passage from
PMID:30391351, beginning “Infections reported include” and listing bacterial,
mycobacterial, fungal and viral infections, including pneumocystis pneumonitis.
The snippet omits the preceding sentence identifying **NFKBIA** patients.

| Claim | Expected | Snippet-only P(MATCH), three runs | With-source P(MATCH), three runs |
| --- | --- | --- | --- |
| Pneumocystis pneumonitis was reported in patients with NFKBIA mutations. | MATCH | 0.67, 0.69, 0.69 | 0.93, 0.93, 0.93 |
| Pneumocystis pneumonitis was reported in patients with IKBKB mutations. | MISMATCH | 0.69, 0.68, 0.70 | 0.11, 0.14, 0.11 |

Without context, the model accepted both at similar probabilities. With the
source, it distinguished them. The expected labels are grounded in the source;
the snippet-only input is inherently missing the information needed to identify
the patient group. This is precisely the information the additional input supplies.

The longer comparator snippet, which already names NFKBIA, was correctly
classified in both arms. Adding the source increased its rejection of the wrong
IKBKB attribution (P(MATCH) from 0.10–0.13 to 0.04–0.05).

### Source support did not rescue bad snippets in these examples

- `elsewhere_hsct`: the paper recommends hematopoietic stem cell transplantation
  elsewhere, but the chosen snippet says TREC screening misses IKBKB cases.
  Both arms rejected that snippet as evidence for the treatment claim in all
  repetitions, with P(MATCH) reported as 0.00.
- `dr_laser`: the cached guideline abstract mentions laser treatment elsewhere,
  but the selected generic public health sentence does not establish the
  specific laser cost-effectiveness claim. Both arms rejected this snippet
  in all repetitions. The separate vitrectomy case was also rejected, although
  this cached abstract does not mention vitrectomy at all.
- `scn3b_direct`: a mouse result still failed to directly establish the human
  claim with the paper available. Source increased P(MATCH) somewhat, from
  0.03–0.04 to 0.10–0.13, but did not change the verdict.

Two narrowly worded treatment claims resembling earlier false alarms (PRP as
primary PDR treatment and anti-VEGF as standard DME care) matched in both arms.
This does not demonstrate that the earlier long-parent-description false alarms
are solved: here those claims were explicitly narrowed before evaluation.

## What “source text” means here

We supplied the **entire existing cached body**, with no truncation or selected
context window. This is not uniformly the whole paper:

| Reference | Cached source available | Characters supplied |
| --- | --- | ---: |
| PMID:19796257 | Full text XML | 41,458 |
| PMID:29776671 | Abstract only | 4,106 |
| PMID:30391351 | Full text HTML | 41,148 |
| PMID:33394739 | Full text XML | 20,930 |
| PMID:38995350 | Abstract only | 4,185 |
| PMID:39673354 | Abstract only | 6,228 |

All 17 snippets passed the existing cache-backed quotation check. Cache files
were read, never changed. Source body hashes and cache paths are in each case.
The source arm used 355,962 input tokens versus 25,902 for snippet-only, about
13.7 times as many, across three repetitions.

## Limits and next step

The implementing agent assigned expectations before the run. These are selected,
partly constructed cases reusing six papers, not independently adjudicated or
held-out data. Three repetitions check repeatability, not generalization. The
absence of source-rescue failures here is not proof that they cannot occur.

The result supports providing both snippet and source, with explicit instructions
that source resolves context but does not replace the selected evidence. Keep
this as a report-only classifier and test more real ambiguous excerpts before
choosing an automatic decision threshold.

## Reproduce

```bash
uv run python experiments/claim_evidence/source_context.py summarize \
  experiments/claim_evidence/2026-09-19-source-context
```

To make a new run, create a new directory, copy this run's `cases.jsonl` there,
then run `source_context.py run NEW_DIRECTORY`. It uses the current installed
prompt, records it in `task.json`, and requires `TYPESAFE_API_KEY`. Existing
artifacts are never overwritten. The `build` command reconstructs these cases
from the previous frozen experiment plus the current reference caches; copying
the frozen inputs avoids changes if those caches have since been refreshed.
