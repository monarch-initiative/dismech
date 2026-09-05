#!/usr/bin/env python3
"""Guard against `environmental:` exposures with no evidence at all.

An `Environmental` entry is optional to cite (`evidence` is not required by the
schema), so a bare exposure -- just a `name` and usually a one-line `notes` --
passes `just validate`, `validate-terms`, and `count-verified-snippets`
untouched. Every one of those checks is structurally blind to it: an
uncited causation claim like

    environmental:
    - name: Smoking
      notes: Protective (unlike Crohn's)

is indistinguishable, to the whole validation stack, from a fully-evidenced
exposure. See dismech issue #8296.

This is deliberately *not* a curation tool: it only counts and gates, it never
invents a citation. Clearing a finding is real literature work -- find a
citable source, take an exact-quote snippet, `just fetch-reference` +
`count-verified-snippets` -- and manufacturing a citation to silence the gate
is exactly the fabrication risk the evidence SOP warns against elsewhere in
this repo. Where no such source exists, record the failed search as a waiver
rather than inventing one.

Signal
------
An `environmental[]` entry whose `evidence` key is absent, ``None``, or an
empty list -- unless it carries a *waiver* (below).

Waivers
-------
Some exposures cannot be cited, and never will be. A curator searches, finds
no abstract that states the claim, and records that. Before this waiver
existed such an entry was indistinguishable here from one nobody had looked
at, so the backlog could never reach zero and an honest negative result read
as an outstanding task.

An entry is treated as *dispositioned* rather than uncited when its
``review_notes`` begins with::

    Left deliberately uncited.

The sentinel is deliberately narrow. It must be ``review_notes``, not
``notes``: a waiver any prose can trigger is not a waiver, and ``notes`` is
disease content while ``review_notes`` is the curation record. The convention
predates the check -- see the Gout "Dehydration" and Myasthenia_Gravis
"Stress" entries, which already opened their ``review_notes`` with exactly
this sentence.

A waiver is a claim that a search happened, so it is only as good as that
search. One waiver in the first round of dismech#8296's waiver PR asserted
that no quotable source existed for ultraviolet exposure in pemphigus
erythematosus; review found PMID:6531279, a photo-provocation study in that
exact disease with a retrievable abstract, from a one-line PubMed query.
That entry is cited now, not waived. Search properly before reaching for
this.

The sentinel alone does not waive. An entry must also record at least
:data:`MIN_WAIVER_WORDS` words of search after it, and that floor is enforced
*here*, in the check that runs ungated on every PR -- not only in the test
suite, which is path-filtered and would never run on the kb-only curation PRs
that add waivers. A sentinel with nothing behind it stays a finding and is
named as a thin waiver so the message is actionable.

Waived entries stay visible: ``--all`` lists them under their own heading and
``--count`` reports them on their own line. They are dispositioned, not
disappeared.

No baseline
-----------
This check shipped as a ratchet: dismech#8296 found 182 evidence-free
exposures, so a committed baseline plus a live ``origin/main``-derived
grandfather set kept the base branch green while the backlog was worked
down in tranches. The backlog is now zero -- every exposure in ``kb/`` is
either cited or carries a ``review_notes`` waiver -- so the machinery has
nothing left to grandfather and has been removed, matching
``scripts/check_empty_snippets.py``: a straight hard gate, no baseline file,
no ``--against-ref``, no ``ENVIRONMENTAL_EVIDENCE_BASELINE_REF``.

Any finding is now a new finding, and the fix is to cite it or to record a
failed search as a waiver -- not to grandfather it. If a future change
legitimately reintroduces a backlog large enough to need one, the machinery
is recoverable from this file's history (see the dismech#8296 sequence);
re-adding it preemptively for a zero-item backlog would be needless
complexity.

Usage
-----
    python scripts/check_environmental_evidence.py            # gate: fail on any finding
    python scripts/check_environmental_evidence.py --all      # list every finding
    python scripts/check_environmental_evidence.py --count    # summary counts
    python scripts/check_environmental_evidence.py --waivers  # list dispositioned entries
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load

# Scan all of kb/, not just kb/disorders/. `environmental:` only appears under
# kb/disorders/ today, so this is a no-op on current content (verified: 0
# environmental entries anywhere outside kb/disorders/, across all six
# subdirectories -- the finding count is identical either way), but kb/modules/
# and kb/comorbidities/ validate against the same `Disease` class and may carry
# `environmental:` in future -- scoping to disorders/ would make them a silent
# blind spot in a check whose whole point is that the gap is invisible.
# test_scan_covers_kb_beyond_disorders pins this so the scope cannot be
# narrowed back silently.
SCAN_DIR = ROOT / "kb"

# An exposure whose `review_notes` opens with this sentence is a recorded
# failed search, not an unexamined one. See the module docstring: the sentinel
# is matched on `review_notes` only, and only as a prefix, so it cannot be
# triggered by ordinary prose that happens to contain the words.
WAIVER_SENTINEL = "left deliberately uncited."

# A waiver must record the search, not merely claim one. The sentinel alone is
# an assertion that somebody looked; this is the floor on what they wrote down.
# Enforced here rather than only in the test suite: the tests are path-filtered
# and do not run on a kb-only curation PR, which is exactly the shape of PR
# that adds a waiver, so a floor that lived only in pytest would never run on
# the changes it exists to police (dismech#9473 makes the same point).
# The committed waivers run 44-150 words, so this is well clear of all of them
# while still blocking a bare sentinel.
MIN_WAIVER_WORDS = 20


def _has_quoted_evidence(entry: dict) -> bool:
    """True if *entry* carries at least one evidence item with a real snippet.

    An `evidence:` block whose items all have an empty/whitespace-only
    `snippet` is not actually cited -- it is the same "structurally valid,
    substantively empty" shape dismech#8550 describes for evidence items in
    general, reachable here specifically because this check's original
    predicate (`if entry.get("evidence")`) only checked block *presence*, so
    an exposure could be silently "retired" from the #8296 backlog by an
    evidence item that quotes nothing.
    """
    evidence = entry.get("evidence")
    if not isinstance(evidence, list):
        return False
    for item in evidence:
        if not isinstance(item, dict):
            continue
        snippet = item.get("snippet")
        if isinstance(snippet, str) and snippet.strip():
            return True
    return False


def waiver_detail(entry: dict) -> str | None:
    """The text after the waiver sentence, or ``None`` if *entry* has no waiver.

    Matched on ``review_notes`` only, and only as a prefix, so the waiver is a
    deliberate act rather than something ordinary prose can trip. ``notes`` is
    disease content and is not consulted: a claim that merely *mentions* being
    uncited is not the same as a curator recording a failed search.

    Returns ``""`` for a bare sentinel with nothing after it -- distinct from
    ``None``, because "claimed a search and recorded none" and "did not claim
    one" need different messages.
    """
    review_notes = entry.get("review_notes")
    if not isinstance(review_notes, str):
        return None
    stripped = review_notes.strip()
    if not stripped.lower().startswith(WAIVER_SENTINEL):
        return None
    return stripped[len(WAIVER_SENTINEL) :].strip()


def is_waived(entry: dict) -> bool:
    """True if *entry* records a deliberate, searched-for-and-not-found decision.

    Requires both halves: the sentinel *and* at least
    :data:`MIN_WAIVER_WORDS` of recorded search after it. A sentinel with
    nothing behind it does not waive -- see :func:`find_thin_waivers`, which
    reports that case specifically rather than letting it pass as an ordinary
    uncited exposure.
    """
    detail = waiver_detail(entry)
    return detail is not None and len(detail.split()) >= MIN_WAIVER_WORDS


def _iter_environmental(data):
    entries = data.get("environmental") or []
    if not isinstance(entries, list):
        return
    for idx, entry in enumerate(entries):
        if isinstance(entry, dict):
            yield idx, entry


def find_violations(data):
    """Yield ``(location, name)`` for each evidence-free `environmental[]` entry.

    Waived entries are excluded -- they are reported separately by
    :func:`find_waivers` so they stay visible without counting as outstanding.
    """
    for idx, entry in _iter_environmental(data):
        if _has_quoted_evidence(entry) or is_waived(entry):
            continue
        name = entry.get("name") or "<unnamed>"
        yield (f"environmental[{idx}]", name)


def find_thin_waivers(data):
    """Yield ``(location, name, words)`` for waivers that record no search.

    These are *not* waived -- :func:`find_violations` still reports them -- but
    they are worth naming separately, because "you wrote the sentence and
    stopped" needs different advice from "this exposure has no evidence".
    """
    for idx, entry in _iter_environmental(data):
        detail = waiver_detail(entry)
        if detail is None or len(detail.split()) >= MIN_WAIVER_WORDS:
            continue
        name = entry.get("name") or "<unnamed>"
        yield (f"environmental[{idx}]", name, len(detail.split()))


def find_waivers(data):
    """Yield ``(location, name)`` for each waived, still-uncited entry.

    An entry that carries both a waiver and real evidence is not reported: the
    evidence supersedes the waiver, and leaving it here would suggest the claim
    is still unsourced.
    """
    for idx, entry in _iter_environmental(data):
        if _has_quoted_evidence(entry) or not is_waived(entry):
            continue
        name = entry.get("name") or "<unnamed>"
        yield (f"environmental[{idx}]", name)


def scan_repo(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return a sorted list of ``(relpath, location, name)`` findings.

    ``rel_to`` is the base the reported relative paths are computed against.
    It defaults to :data:`ROOT`, so findings read as ``kb/disorders/X.yaml``.
    It is a parameter rather than a constant so a scan can be pointed at a
    tree that is not this repository: ``test_scan_covers_kb_beyond_disorders``
    builds a fixture under ``tmp_path`` and needs the reported paths relative
    to that, not to :data:`ROOT`.
    """
    return _scan((find_violations,), scan_dir, rel_to)[0]


def scan_thin_waivers(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return ``(relpath, location, name, words)`` for substance-less waivers."""
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        rel = path.relative_to(rel_to).as_posix()
        for location, name, words in find_thin_waivers(data):
            findings.append((rel, location, name, words))
    return findings


def scan_waivers(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return a sorted list of ``(relpath, location, name)`` waived entries."""
    return _scan((find_waivers,), scan_dir, rel_to)[0]


def scan_all(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return ``(findings, waivers)`` from a single walk of *scan_dir*.

    Both lists come from the same ``environmental[]`` entries, differing only
    in which side of :func:`is_waived` they keep, so calling
    :func:`scan_repo` and :func:`scan_waivers` separately parses all of
    ``kb/`` twice -- about 11 seconds each on the current tree, on the ungated
    CI step and in every ``just qc``.
    """
    return tuple(_scan((find_violations, find_waivers), scan_dir, rel_to))


def _scan(finders, scan_dir: Path, rel_to: Path):
    buckets = [[] for _ in finders]
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception as exc:
            # Not this check's job to gate on malformed YAML (`validate-all`
            # does that), but skipping silently would make the file invisible
            # here rather than merely unchecked.
            print(
                f"warning: skipping unparseable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        if not isinstance(data, dict):
            continue
        rel = path.relative_to(rel_to).as_posix()
        for bucket, finder in zip(buckets, finders):
            for location, name in finder(data):
                bucket.append((rel, location, name))
    return buckets


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--check", action="store_true", help="(default) fail on any finding"
    )
    group.add_argument("--all", action="store_true", help="list every finding")
    group.add_argument("--count", action="store_true", help="print summary counts")
    group.add_argument(
        "--waivers",
        action="store_true",
        help="list entries dispositioned by a review_notes waiver",
    )
    args = parser.parse_args(argv)

    # One walk, both lists: the success message reports the waiver count, so
    # every path needs both, and scanning kb/ twice to get them is ~11s wasted
    # on the ungated CI step and in every `just qc`.
    findings, waivers = scan_all()

    if args.waivers:
        for rel, location, name in waivers:
            print(f"{rel}:{location}: {name!r}")
        files = {rel for rel, _, _ in waivers}
        print(
            f"\n{len(waivers)} exposure(s) dispositioned by a "
            f"'{WAIVER_SENTINEL.capitalize()}' review_notes waiver "
            f"across {len(files)} file(s)."
        )
        return 0

    if args.all:
        for rel, location, name in findings:
            print(f"{rel}:{location}: {name!r}")
        files = {rel for rel, _, _ in findings}
        print(f"\n{len(findings)} evidence-free exposure(s) across {len(files)} file(s).")
        if waivers:
            print(
                f"({len(waivers)} further exposure(s) carry a review_notes waiver "
                "recording a failed search; see --waivers.)"
            )
        return 0

    if args.count:
        files = {rel for rel, _, _ in findings}
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(f"dispositioned (review_notes waiver): {len(waivers)}")
        return 0

    if findings:
        print("Evidence-free `environmental:` exposure(s) detected.")
        print("Every environmental entry is an uncited causation claim until it")
        print("carries an `evidence:` block -- a citable PMID/DOI with a verified")
        print("snippet. See the evidence SOP in CLAUDE.md before adding one.\n")
        for rel, location, name in findings:
            print(f"{rel}:{location}: {name!r}")
        print(f"\n{len(findings)} finding(s).")
        thin = scan_thin_waivers()
        if thin:
            print()
            print("Some of these carry a waiver sentence with nothing behind it.")
            print(f"A waiver must record the search -- at least {MIN_WAIVER_WORDS}")
            print("words saying which searches were run and why they failed:")
            for rel, location, name, words in thin:
                print(f"  {rel}:{location}: {name!r} ({words} word(s) after the sentinel)")
        print()
        print("There is no baseline to grandfather these into: the dismech#8296")
        print("backlog was worked to zero and the ratchet was removed. Either")
        print("cite the exposure, or -- if you searched and found no abstract that")
        print("states the claim -- record that in `review_notes:` beginning with")
        print(f"'{WAIVER_SENTINEL.capitalize()}', saying which searches you ran.")
        print("A waiver is a recorded negative result, not a way to skip the search.")
        return 1

    print(
        f"OK: no evidence-free `environmental:` exposures "
        f"({len(waivers)} dispositioned by a review_notes waiver)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
