# Evidence-claim adjudication: Neuroblastoma

This run judges every claim-and-quote pair of `kb/disorders/Neuroblastoma.yaml`, apart from a
declared set of excluded rows, at a pinned commit, following the protocol and rubric in
[`../README.md`](../README.md). This file so far records only the frame and how the run is kept
blind. The results, and the limits of the measurement, are added after the verdicts are frozen;
until then it deliberately holds no figure taken from a checker file, apart from the one bound
stated under *Pin*.

The protocol and rubric are the ones merged in #18343 (commit `524011b434b`). The README has changed
since, before any judging. Four statements about what exists were brought up to date: its Runs
section, the description of `tally.py` in its Layout section, the sentence saying which of a run's
files exist, and the sentence about the calibration's sampler. One sentence of its introduction lost
the two flag counts that issue #16981 reports for this entry, and a new sentence says why: so that
the file carries no checker count for an entry under adjudication. The opening of *The seven tables*
now says that `tally.py` computes tables 1 to 5 and that tables 6 and 7 come with the repairs. And a
section was added, *Filling in the sheets*, which writes down the values each verdict column takes,
the values `tally.py` checks. It changes none of the rubric's questions, classes or severities.

## Whose count

The README calls a run's result a curator's adjudication, one curating group's count of its own
work, and asks a run to name the pull requests it covers. Up to the pin, 73 commits touched the
entry. 52 of them are the squash commits of pull requests opened by the group that runs this
adjudication, the curators of the Neuroblastoma family entries tracked in
`projects/NEUROBLASTOMA.md`:

#14386, #15061, #15079, #15084, #15096, #15100, #15105, #15118, #15221, #15222, #15228, #15230,
#15232, #15233, #15264, #15273, #15274, #15320, #15332, #15336, #15338, #15356, #15360, #15367,
#15368, #15369, #15468, #15718, #15720, #15721, #15730, #15829, #15831, #15838, #15887, #16608,
#16612, #16616, #16617, #16618, #16623, #16637, #16638, #16914, #16926, #16927, #16933, #16934,
#17053, #17062, #17063, #17064.

The frame is the whole entry at the pin, so it also holds what the other commits wrote; pairs are
not attributed to authors here.

## Pin

| | |
|---|---|
| Entry | `kb/disorders/Neuroblastoma.yaml` |
| Commit | `09ce31cd7a38a03122f5e9a9869792b5b61c1f91` |
| Entry sha256 at that commit | `21de5f5442fd5797fa95538b808878fda3dceb6133ae57b8bf6a4fffa9f27fe4` |
| Checker run | the one observed on 16 November 2026, saved in `monarch-initiative/dismech-evals` as `analysis/classification/jev/Neuroblastoma/evidence_claim_match.yaml` at commit `dcd56ccea747db152c1f971d633fd758106c827c` (file sha256 `f0370d1c6d0574965b207518409acfb7f5a2c29deaf5e896b5b24833acf5bc3e`) |
| Earlier checker run, for recomputing the issue's two counts | 9 November 2026, same path at commit `1635a1c227998c00c7ecfd64c043a5b2e4897d1e` (file sha256 `a6542cdc3871f22ef81d7978f6b2971fa0f0b3d3f4365a3bd345a3250e2d13b0`) |

Checks made when the frame was built, all of which passed:

- The commit is the one the 16 November run records as the revision it read, and the entry's bytes
  at that commit hash to the value that run recorded.
- The commit contains the four pull requests meant to land before the pin: #17053, #17062, #17063
  and #17064.
- At least half of the frame's pairs carry an assessment in the 16 November run's saved file. The
  builder refuses a file in which fewer do; the number itself is in the sealed record.
- The builder's other checks also passed, among them that every input the run observed was placed on
  a pair and that no match was ambiguous. Each is printed only as yes or no.

## Frame

| | |
|---|---|
| Extractor | `python -m dismech.classifier.audit --dry-run`, at `main` `cefd0537e88`; sha256 of the classifier code `8cc2a7e6dfacd5bd3951b66ce50e49c0236b4d9e5ea76862834e639158408b59` |
| Rows the extractor finds at the pin | 929: 883 claim-and-quote pairs and 46 assertions with no quote at all |
| Excluded rows, judged by the human reviewer | 8 rows, 70 pairs: two treatment rows (Crizotinib, Lorlatinib), one trial row (NCT03126916) and five genetic rows (Segmental Chromosomal Aberrations, Chromosome 1p36 Deletion, Chromosome 11q Deletion, Chromosome 17q Gain, Chromothripsis) |
| Frame | 813 pairs over 283 assertions; 46 of the assertions are the rows with no quote, judged at the assertion level only |
| Keys | `frame_keys.tsv`: one row per frame pair, keyed by evidence path and the first 12 characters of a sha256 of claim and quote |

A checker input is matched to a pair on assertion path, evidence path and quote text, using the
paths the run recorded when it last saw the input, and only among the inputs the run itself
observed, because the saved file keeps inputs from earlier weekly runs marked active after the row
they came from has changed. Where the checker holds more than one response for an input, the latest
is used. How many inputs were matched, how many frame pairs carry an assessment, and the run's own
completeness flag are kept with the checker's labels, outside the repository. `build_frame.py`
prints no count of them, only whether at least half of the frame's pairs carry an assessment, and
`tally.py` reports them with the tables once the verdicts are frozen.

Judging batches, in the order the judge works through them:

| Batch | Sections | Pairs |
|---|---|---|
| 1 | pathophysiology nodes | 194 |
| 2 | causal edges and other rows nested under a node, mechanistic hypotheses, discussions, models, datasets | 138 |
| 3 | treatments, clinical trials, diagnosis, imaging | 176 |
| 4 | genetics, subtypes, prevalence, stages, epidemiology, inheritance, progression, classifications | 113 |
| 5 | differential diagnoses, phenotypes, histopathology, biochemistry | 192 |

Samples, drawn by `build_frame.py` at random and stratified by section, seed `20261119`: 120 pairs
for the second pass, and 30 of those for the human reviewer. Each sampled pair is shown with the
other quotes on its row and on the rows nested in it, which the rubric needs and which the second
pass, kept away from the judge's sheets, would not otherwise see. The frame has more than 400 pairs,
so table 4 can be computed at all three of its cut-offs.

## What the readers see

The judge and the second reader work from the run folder alone: their sheets and `rubric.md`, which
`build_frame.py` writes there. It is an extract of the README, word for word: the sections *The
unit: two levels*, *Who judges*, *The four questions*, *Defect classes and severities*, *What is not
a defect*, *Worked examples*, *What is left out, and how it is counted* and *Filling in the sheets*.
The readers do not open the README itself, whose introduction and account of the calibration discuss
the checker's output, nor anything else in the repository apart from the cached sources of the
quotes they judge.

Four limits are declared now, before any verdict:

- The rubric's worked examples state the checker's labels on rows of the calibration entry. The
  readers therefore know how the checker labelled those rows of another entry. They see nothing of
  its output on this one.
- The session that built the frame handled the two checker files. It saw counts taken from them
  (inputs, pairs matched and assessed, assertions flagged) and the run's own completeness flag, and
  no label or probability for any single pair. It judges nothing and rules on nothing; it lists the
  disagreements and runs the tally.
- The run folder also holds the two samples and `frame_index.json`, which say which pairs will be
  read again. The judge's instructions name the files it may open, and these are not among them.
- The excluded rows are judged by the human reviewer at the pair level only, and the two samples are
  samples of pairs. The assertion level therefore has one reader, the judge, and table 5 compares
  readers on pairs.

The checker's labels sit in a sealed folder outside the repository, which is kept unreadable (`chmod
000`) between uses and is reopened only to rebuild the frame or to run the tally. That was not so
from the start. On 19 November, while the frame was first being built, the checker files lay in the
run folder from 13:54 UTC, and the labels from 14:13, until 14:41; they then lay in a folder beside
it until 15:24, and in the sealed folder's present place until it was first made unreadable at
15:32. All three folders were readable by the owner's group, as the run folder still is. In this
session's scratch folder, which only its owner can read, a copy of the record of counts was made at
14:14 and a test build wrote the labels at 14:16; both were removed at 15:10. All of this was before
any reader's session existed, and the sheets now in the run folder hold no verdict.

## How the tables will be computed

Fixed here, before any label is joined. `tally.py` at this commit computes tables 1 to 5. Tables 6
and 7 report on the repairs and are added to the script with them.

- The verdict that governs a pair is the reviewer's ruling where there is one; else the reviewer's
  own blind verdict, where the pair is in the reviewer's sample; else the judge's. A ruling is
  accepted only where the second reader differs from the judge.
- Table 4 ranks the frame's assessed pairs by the checker's whole-claim mismatch probability. On the
  calibration entry those probabilities were coarse, so ties at a cut-off are expected here too, and
  they are not broken: for each cut-off the table gives the pairs strictly above the probability of
  the pair at the cut-off, the pairs tied with it, and both together.
- Before the freeze, `tally.py` names the sheet, row and column of each problem it finds, never
  the value or the rule. While a sheet is incomplete, each reader is shown only the lines about
  their own sheet, and `tally.py --disagreements` is run only after the reviewer has said the blind
  sample is finished. The reviewer's blind sample is locked once its sheet is complete and passes
  its checks. The sha256 of `BLIND.txt` is then added to this file, in a pull request opened before
  the list is shown to any reader, and `tally.py` will not run without it, so the sheet cannot
  change after the lock. Until the lock, problems on the other readers' rows of a sampled pair, of
  the same or a nested assertion, or of a row shown beside a sampled pair, and on rows whose key or
  path is not in the frame, are reported without a row, a column or a number and are not counted
  among the blank rows, so that the list cannot hint which way a reader leaned on a pair the
  reviewer has still to judge.
- The sha256 of `FREEZE.txt` is added to this file, in a pull request opened before the sealed
  folder is reopened. `tally.py` will not run without that hash. It first checks that the sealed
  folder was built with this run folder, this frame index and this `rubric.md`; it then records in
  the sealed folder the freeze under which the labels were first opened, so a later tally under
  another freeze has to say why, and only then reads a label.

## How the frame was built

From the repository root. The judge's sheets go to a run folder, and the two saved checker runs, the
labels keyed to the frame and every count taken from a checker file to a separate sealed folder;
both are kept outside the repository, and no judging session opens the sealed one:

```bash
python experiments/evidence_claim_adjudication/build_frame.py \
  --entry kb/disorders/Neuroblastoma.yaml \
  --pin 09ce31cd7a38a03122f5e9a9869792b5b61c1f91 \
  --checker-file <sealed folder>/_checker/evidence_claim_match_2026-11-16.yaml \
  --old-checker-file <sealed folder>/_checker/evidence_claim_match_2026-11-09.yaml \
  --out <run folder> --sealed <sealed folder> --seed 20261119 \
  --exclude treatments=Crizotinib --exclude treatments=Lorlatinib \
  --exclude clinical_trials=NCT03126916 \
  --exclude "genetic=Segmental Chromosomal Aberrations" \
  --exclude "genetic=Chromosome 1p36 Deletion" --exclude "genetic=Chromosome 11q Deletion" \
  --exclude "genetic=Chromosome 17q Gain" --exclude genetic=Chromothripsis \
  --contains 3516830dd8cf7848acf60ccfe9e0fd0a3e458edc \
  --contains 39bf22acdf434f3fd94c43873b8c7f77a645eace \
  --contains 0c70e806ef6a730594a6a542e6fc7f6951db49c3 \
  --contains 0b2d5d371aa0ece322d847600461f967d27daeea
```

The four `--contains` commits are the merge commits of the four pull requests named above. Run again
with the same inputs into fresh folders, the command reproduces `frame_keys.tsv` byte for byte. It
also writes `frame_index.json` to the run folder: the keys, assertion paths and samples of the
frame, the paths of the rows shown beside the reviewer's sampled pairs, and the keys of the excluded
pairs, with no claim text and nothing from the checker, which `tally.py` checks the sheets against.

## Results

Not yet: the verdicts have not been frozen.
