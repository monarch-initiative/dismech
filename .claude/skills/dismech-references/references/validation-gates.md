# Offline evidence and content gates

CI also runs these offline gates without changed-path filtering. Run them after
a tranche of curation edits; only the duplicate-key and entity-ref checks accept
a file path:

```bash
just check-folded-hyphens
just check-snippet-length
just check-title-snippets
just check-snippet-grading
just check-environmental-evidence
just check-duplicate-keys kb/disorders/MyDisease.yaml
just check-entity-refs kb/disorders/MyDisease.yaml
just check-causal-targets kb/disorders/MyDisease.yaml
just check-qualifier-terms kb/disorders/MyDisease.yaml
just check-source-defect-claims  # report-only
```

They catch folded-scalar word corruption, non-propositional short snippets,
paper titles used as findings, one quoted sentence graded with two different
`evidence_source` values in the same file, environmental claims without
entry-level evidence, duplicate YAML keys, broken `<kind>#<name>` entity
references, broken bare-name pathograph targets, and prose claims about
defective sources that the cache contradicts. `check-snippet-length`,
`check-title-snippets`, `check-snippet-grading` and `check-causal-targets` use
baselines; do not update a baseline to admit a defect introduced by the current
change.

Two of these gates used to have a baseline and no longer do, by the same route:
the backlog was repaired, then the mechanism was removed, so there is now no way
to grandfather a finding. `check-environmental-evidence` got there first (#8296),
and an exposure that genuinely cannot be cited now carries a `review_notes:`
waiver instead of a baseline row (see below). `check-folded-hyphens` followed
once #11760 had repaired its 293-split backlog, which was #4800's stated
endpoint. Where that check flags a line that is genuinely correct, the fix is to
teach the detector the shape and pin it with a test -- as `COORD_RE` does for
suspended hyphens and `is_status_marker` for clinical negativity markers
(`ER+/HER2-`, `T-B-NK-`) -- rather than to record an exception.

**When an exposure genuinely cannot be cited, say so in `review_notes:`.**
`check-environmental-evidence` treats an `environmental[]` entry whose
`review_notes` *begins* with the sentence

```
Left deliberately uncited.
```

as dispositioned rather than uncited, and reports it under `just
list-environmental-evidence-waivers` instead of as an outstanding gap. Say
which searches you ran and why they failed, as the `Gout` → Dehydration and
`Myasthenia_Gravis` → Stress entries do — **the sentence alone does not
waive**. At least 20 words of recorded search must follow it, and that floor
is enforced by `check-environmental-evidence` itself, which is ungated, rather
than only by a test that a `kb/`-only PR would skip. The
sentinel is matched on `review_notes` only, and only as a prefix: `notes:` is
disease content and cannot waive, and prose that merely mentions the phrase
does not trigger it. An entry carrying both a waiver and real evidence is not
reported as waived — the evidence supersedes it. This exists so that "searched,
found nothing quotable" is a recordable answer rather than a permanent backlog
item; it is not a way to skip the search (#8296).

`check-snippet-grading` (#8184) is the one to know about when copying an
evidence item into a second block: `evidence_source` classifies the cited
*publication*, so it cannot change because the quote moved. Re-grading a copied
quote is the defect. Note it is keyed on the **quoted sentence**, not the PMID —
one paper legitimately carries several values across different sentences, which
is what "If a paper mixes sources, split evidence items" above already asks for.
`supports` is deliberately *not* gated: it is claim-relative, so the same
sentence correctly reads `SUPPORT` for one claim and `REFUTE` for another
(`just list-snippet-grading --fields all` shows those as a triage view). Note
this is now a much weaker effect than it used to be — retiring `PARTIAL` cut
`supports` divergences from 8,285 to 353, against 715 for `evidence_source`, so
most of that signal was the value's ambiguity rather than claim-relativity.
Gating `supports` is worth revisiting.

**Why the entity-ref check is a CI step and not just a test.** The same rules
run in `check_entity_ref_foreign_keys`, but CI selects pytest by changed path,
and a curation PR touches only `kb/` — matching neither the `python` nor the
`schema` filter. So the checks written to protect KB content were the ones a
content-only PR skipped, which is how two alias prefixes reached `main`
(#9473). `just check-entity-refs` is ungated and whole-KB for the same reason
`check-duplicate-keys` is. A nightly sweep (`.github/workflows/nightly-kb-sweep.yaml`)
runs both pytest lanes against `main` as a backstop.
