# Inter-annotator consistency studies

How much of a dismech entry is determined by the evidence, and how much by the
curator? Each study here curates one disease twice, independently, and measures
where the two versions agree.

## Comparisons

| Study | Disease | Curators | Phenotype agreement (strict / subsumption-aware) | Band agreement |
|---|---|---|---|---|
| [`FG_Syndrome_1/`](FG_Syndrome_1/) | FG syndrome 1 (`MONDO:0010590`) | A: merged [#7254](https://github.com/monarch-initiative/dismech/pull/7254) · B: independent | 0.484 / 0.766–0.812 | 25/31 = 0.806 |

## Layout

`compare.py` is shared tooling and lives at this level. Everything else is
per-comparison and lives in a subdirectory named for the disease slug (matching
its `kb/disorders/` stem):

```
interannotator/
├── README.md                     this index
├── compare.py                    shared metric script
└── <Disease_Slug>/
    ├── PREREGISTRATION.md        written and committed BEFORE curation starts
    ├── FINDINGS.md               the report
    ├── metrics.txt               compare.py output, as run
    ├── <Disease_Slug>.curator-A.<provenance>.yaml
    └── <Disease_Slug>.curator-B.<provenance>.yaml
```

Snapshots keep the disease in the filename even though the folder repeats it, so
a YAML that gets downloaded or attached somewhere still identifies itself. The
`<provenance>` suffix records where the version came from (`merged-pr7254`,
`independent`, …). If the same disease is studied more than once, suffix the
folder rather than overwriting: `<Disease_Slug>-run2/`.

## Running a comparison

```bash
uv run python experiments/interannotator/compare.py \
  experiments/interannotator/<Disease_Slug>/<...>.curator-A.<...>.yaml \
  experiments/interannotator/<Disease_Slug>/<...>.curator-B.<...>.yaml \
  | tee experiments/interannotator/<Disease_Slug>/metrics.txt
```

Subsumption-aware phenotype matching shells out to OAK per term and takes a
couple of minutes; `--no-ontology` skips it and reports strict term identity only.

## Independence: what actually leaks

The FG syndrome 1 run satisfied the letter of its own rule — curator B never opened
A's YAML — and was contaminated anyway, because B's operator had read **PR #7254's
description** before starting. That description named the three mechanistic arms and
roughly ten PMIDs, which is most of what an independent curator is supposed to
rediscover. The two dimensions the study most wanted to measure (mechanism graph,
reference set) were the two it lost.

The lesson is that *reading the entry* is only one of several channels, and not the
likeliest one. Treat these as the blocklist:

| Channel | How it leaked / could leak | Control |
|---|---|---|
| **Prior conversation context** | The agent that reviewed or fixed A goes on to curate B | B runs in a **fresh session** that has never discussed the disease. Not a rule B follows — a session B starts in. |
| **The PR** — description, diff, review threads, commits | The actual FG leak | On the blocklist explicitly. A PR description is a *summary of A's conclusions*; it leaks more per word than the entry does. |
| **The dispatch prompt** | Whoever briefs B paraphrases A ("check the GLI3 arm") | Fixed template, committed verbatim in `PREREGISTRATION.md`. Disease name + MONDO id + "curate per `/curate`" and nothing else. |
| **Git history** | `git log -p -- kb/disorders/<Slug>.yaml` reconstructs A even if the file is gone | Shallow clone (below) |
| **The entry, its history record, its rendered page** | Direct read, or an incidental `grep`/`Glob` hit | Scrub from B's workspace |
| **`research/<Slug>-*`** | A's deep-research report and citation sidecars | Scrub |
| **`references_cache/`** | The mere *presence* of `PMID_23091001.md` points at a citation | Remove cache files cited only by A; B re-fetches what it finds |
| **The curation issue, `docs/curation-notes/`, project files** | Named phenotypes or genes | Blocklist |

**Be honest about the limit:** scrubbing is a guard against accident, not a sandbox
against a determined agent. The load-bearing controls are the fresh session and the
fixed prompt; the scrub mainly stops B from tripping over A while grepping.

## Preferred design: prospective, not retrospective

Comparing against an already-merged entry is inherently leak-prone — the artifacts
exist, the PR is indexed, and the operator has usually read it. **Prefer a
prospective run:** pick the disease, freeze one base commit, and dispatch both
curators in parallel from it, neither aware the other exists. Nothing needs
scrubbing because nothing has been written yet, and both dimensions the FG run lost
are recoverable.

Retrospective runs against a merged entry are still worth doing — the FG run's
uncontaminated dimensions carried real findings — but declare the design in
`PREREGISTRATION.md` and expect to mark the mechanism graph and reference set as
untrusted from the outset.

## Adding a new study

1. **Pick the disease without reading it.** Select by a rule that doesn't require
   opening the entry — priority dashboard rank, a random draw from entries meeting a
   criterion. Whoever selects should not be whoever curates as B.

2. **Pre-register.** Write and commit `PREREGISTRATION.md` *before* any curation:
   base commit; design (prospective / retrospective); the dispatch prompt verbatim;
   which blinding measures were actually applied; and — filled in **a priori** — the
   per-dimension contamination table and which dimensions are primary. `FINDINGS.md`
   may later *downgrade* a dimension's trust; it may never upgrade one. This is the
   change that stops the trust table from being written to fit the results.

3. **Blind the workspace** (retrospective runs only). A shallow clone drops the git
   history along with the files, which a `git worktree` does not:

   ```bash
   git clone --no-local --depth 1 file://$PWD /tmp/blind-workspace
   cd /tmp/blind-workspace
   rm -f  kb/disorders/<Slug>.yaml pages/disorders/<Slug>.html
   rm -rf history/disorders/<Slug>/ research/<Slug>-*
   # plus every references_cache/ file cited ONLY by that entry
   ```

   Then confirm the blind before dispatching: `grep -ril "<disease name>" kb/ history/
   research/ docs/` should return nothing disease-specific.

   Verified: `--depth 1` leaves exactly one commit, so `git log -- <the entry>` returns
   that commit and nothing else. Budget the disk — the working tree is several GB and
   `references_cache/` has to come along for `validate-references` to run. If that cost
   is prohibitive, a scrubbed `git worktree` is the fallback, but it leaves the git
   history readable and the blind is correspondingly weaker; say so in
   `PREREGISTRATION.md` rather than implying a clean blind.

4. **Dispatch B into a fresh session** with the pre-registered prompt. Do not answer
   mid-run questions about what A did.

5. **Curate to validation.** B finishes when its own version passes schema, term, and
   reference validation — that is the unblinding point, not before.

6. **Take B's attestation.** Before unblinding, B states in its own words what it
   consulted, since B knows this better than the dispatcher does. Paste it into
   `FINDINGS.md` verbatim. The FG contamination was caught this way and would not have
   been caught by inspecting B's output.

7. **Snapshot both versions verbatim**, and record the commit each came from.
   Verify the KB-derived snapshot is byte-identical to its source (`diff -q`).

8. **Run `compare.py`**, saving output to `metrics.txt`. Quote its numbers in the
   report rather than recomputing them by hand. Record the metrics before writing any
   interpretation of them.

9. **Write `FINDINGS.md`.** Restate the pre-registered contamination limits before the
   results, not after. Separate *defects* (violations of the project's own evidence
   rules) from *differences* (defensible curator choices) — the two warrant different
   follow-up.

10. **Update the table above.**

## Notes carried across studies

Findings that generalise beyond a single disease. Add to this as studies accumulate.

- **Strict term-identity Jaccard understates agreement on this KB** and should not
  be reported alone. In the FG syndrome 1 study it scored 0.484 where
  subsumption-aware agreement was 0.766–0.812; the gap is entirely
  parent/child pairs (`Hypotonia`↔`Neonatal hypotonia`) and roll-up-vs-split
  choices (`Abnormality of the eye` ↔ four specific ocular terms).
- **Agreement tracks the source, not the curator.** Divergence concentrates where
  the literature says "were frequent" without a count, and collapses wherever a
  denominator is stated.
- **A coarse action vocabulary hides disagreement.** Agreement measured at the
  ontology-term level can overstate agreement about the underlying content, because
  two curators can bind the same catch-all term to different things. In the FG
  syndrome 1 study, 7 shared NCIT treatment ids reduced to 4 genuine agreements once
  the names behind them were read: `NCIT:C15747` Supportive Care absorbed both bowel
  management and audiology surveillance, and `NCIT:C15302` Physical Therapy was a
  pure collision. Report id-level and content-level agreement separately; the former
  alone is not a measure of curator agreement.
- **Independent re-curation and code review catch different things.** Review
  checks whether a snippet supports its claim; it is far less likely to notice
  that a better, more specific source exists and was not cited. That class of
  defect survived three review rounds and an approval in the FG syndrome 1 study.
- **Contamination arrives through the PR, not the entry.** A curator who is
  scrupulous about not opening the first version will still have read its PR
  description — which is a distilled summary of exactly the conclusions the study
  is trying to measure independent rediscovery of. Blind the PR first, the file
  second.
