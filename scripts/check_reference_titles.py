#!/usr/bin/env python3
"""Guard against fabricated publication titles on evidence/reference items.

``EvidenceItem.reference_title`` (and ``PublicationReference.title``) is checked
by *nothing*. Every gate in the stack looks at a different field::

    evidence:
    - reference: PMID:34081534                     # linkml-validate: a valid PMID
      snippet: "exact quote from the abstract"     # validate-references: verified
      reference_title: "Congenital cranial dysinnervation disorders:
        a concept in evolution."                   # <- checked by nothing

So the failure mode is: **correct PMID, verified snippet, invented title.**
``linkml-validate`` confirms the slot is a string; the reference validator and
``count-verified-snippets`` check the *snippet*; ``validate-terms`` looks at
ontology terms; and ``check_title_snippets`` -- despite the name -- asks whether
a *snippet* quotes the paper's title, which is a different question entirely.

Issue #9138. Caught by a reviewer on PR #9111 (CFEOM), where three of twenty
unique ``(reference, reference_title)`` pairs named papers that do not exist.
Two were written by an agent that had just verified the adjacent snippets as
exact substrings of the cached text and then wrote the titles beside them from
memory rather than reading the cache frontmatter. Being rigorous about the
quote and careless about the citation attached to it is a distinct failure
mode, and these values are not inert: they render on the disorder page and flow
into the cx2 and SEPIO exports.

The correct title is already on disk. Every ``references_cache/*.md`` carries it
in frontmatter, so this check is a pure-offline string comparison over data the
repo already has -- no network, no ontology adapter, no new dependency.

Signal
------
A ``(reference, title)`` pair whose title, normalised, has a similarity ratio
below :data:`MIN_SIMILARITY` against the ``title:`` recorded in that reference's
cache file.

Similarity rather than equality, because clean pairs differ harmlessly and
constantly: a trailing period the emitter kept and the curator dropped, an
en-dash transcribed as a hyphen, smart quotes, ``[corrected]`` markers, and
HTML-ish ``<i>`` runs in the cached value. Measured over the whole KB, 0.85
separates those from real fabrications with room to spare -- the three #9111
titles score 0.44, 0.63 and 0.77.

Exemptions (skips, not failures):

* **Uncached references.** Nothing to compare against; reporting those is
  ``just fetch-reference``'s job, not this check's.
* **Cache files with no ``title:``.** Same reason.
* **Blank titles.** ``scripts/find_missing_reference_titles.py`` is the
  complementary check for *absent* titles; this one is for *wrong* ones.
* **One title contains the other verbatim.** If the cached title appears as a
  contiguous word run inside the curated one, the curator identified the paper
  correctly and appended something -- overwhelmingly the ``X (Orphanet
  structured-database record)`` annotation, which accounts for 4,367 of the
  5,232 raw findings and is a *convention being followed*, not a fabrication.
  The converse (curated inside cached) is a title truncated at its subtitle
  (``... in Guillain-Barre syndrome`` for ``...: a prospective cohort study``):
  abbreviated, but the right paper. Containment is exempted symmetrically for
  that reason -- the signal this guard exists for is a citation naming a
  *different* work, and a string carrying the real title verbatim is not that.
* **``url:``/``http(s):`` references and dataset accessions.** A ``url:`` cache
  file's ``title:`` is a scraped HTML ``<title>`` or the first section heading
  of a full-text XML fetch (``Abstract``, ``Introduction``, the URL itself), not
  an authoritative publication title, so comparing a real paper title against it
  says nothing. Dataset prefixes are exempted for the same reason and sourced
  from the reference validator's own ``skip_prefixes`` (minus ``DOI``, which is
  real literature) via :func:`scripts.check_title_snippets.dataset_prefixes`.

Baseline ratchet
----------------
A pre-existing backlog already lives in ``kb/``. It is grandfathered exactly the
way :mod:`scripts.check_snippet_length` and :mod:`scripts.check_title_snippets`
grandfather theirs, and for the same reason: to gate *new* occurrences without
blocking unrelated PRs on a cleanup.

``--against-ref REF`` (env ``REFERENCE_TITLE_BASELINE_REF``) derives the
baseline live from ``kb/`` at a git ref -- CI passes the base branch, so the
base branch is green by construction and parallel merges have nothing to
clobber. Titles are resolved against the *working tree* cache in both cases:
``references_cache/`` holds tens of thousands of files and archiving it per run
would cost far more than it buys, and a cached title that genuinely changed
under a reference is a regeneration worth surfacing rather than hiding.

``tests/reference_title_baseline.txt`` is the committed fallback for local runs
and shallow checkouts.

Usage
-----
    python scripts/check_reference_titles.py                           # gate
    python scripts/check_reference_titles.py --against-ref origin/main
    python scripts/check_reference_titles.py --all
    python scripts/check_reference_titles.py --count
    python scripts/check_reference_titles.py --update-baseline
"""

from __future__ import annotations

import argparse
import difflib
import html
import io
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import unicodedata
from collections import Counter
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))
if str(ROOT) not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT))

from dismech.reference_snippet_audit import (
    DEFAULT_SCHEMA,
    CachedReferenceIndex,
    discover_field_names,
)
from dismech.yaml_io import safe_load

# Single-sourced from the title-snippet guard so the two cannot drift apart on
# how a cached title is read out of frontmatter, or on what "the same string"
# means once case, quotes and punctuation are folded away.
from scripts.check_title_snippets import dataset_prefixes, title_of
from scripts.check_title_snippets import normalize as _fold_case_and_punctuation

SCAN_DIR = ROOT / "kb"
CACHE_DIR = ROOT / "references_cache"
BASELINE_PATH = ROOT / "tests" / "reference_title_baseline.txt"
BASELINE_REF_ENV = "REFERENCE_TITLE_BASELINE_REF"

#: The two slots that carry a human-readable publication title.
#:
#: ``EvidenceItem.reference_title`` and ``PublicationReference.title``. Listed
#: rather than discovered from the schema: ``reference_title`` carries no
#: ``implements:`` annotation to key off, and ``linkml:title`` (which ``title``
#: does carry) is a generic slot URI that would sweep in unrelated titles if the
#: schema ever reused it.
TITLE_FIELDS = ("reference_title", "title")

#: Below this similarity ratio a title is reported as not matching its cache.
#:
#: Chosen against the real corpus (see the module docstring): the clean pairs
#: that differ only in punctuation, dashes and markup all sit far above it, and
#: the three known-fabricated #9111 titles sit at 0.44 / 0.63 / 0.77.
MIN_SIMILARITY = 0.85

#: Inline markup left in a cached ``title:`` by the source's own XML.
#:
#: Crossref titles arrive carrying JATS/HTML runs -- ``<scp>FIGO</scp>``,
#: ``<i>TCF4</i>``, ``<italic>IGF1</italic>``, ``GABA<sub>B</sub>``. The angle
#: brackets are punctuation and fold to spaces, but the *tag names* would
#: survive as words and cost a faithful transcription real similarity, so the
#: tags are removed before folding rather than after.
#:
#: Some sources deliver those same runs HTML-escaped (``&lt;i&gt;TCF4&lt;/i&gt;``),
#: where the tag names would survive :data:`_TAG_RE` entirely. Titles are
#: unescaped first so both spellings fold identically -- one Crossref DOI
#: accounted for 7 findings whose curated titles were perfect transcriptions
#: scoring 0.802, and score 1.000 once unescaped.
_TAG_RE = re.compile(r"<[^<>]{1,40}>")

#: Reference prefixes whose cached ``title:`` is not a publication title.
#:
#: A ``url:`` reference is fetched by scraping, so its frontmatter title is
#: whatever the page or the full-text XML happened to lead with -- ``Abstract``,
#: ``Introduction``, an ``... - NCBI Bookshelf`` branded page title, or the URL.
#: Bare ``http``/``https`` references are the same thing written without the
#: ``url:`` prefix.
_SCRAPED_PREFIXES = frozenset({"url", "http", "https"})


def normalize(text: str) -> str:
    """Fold a title to its comparable form: case, punctuation, and diacritics.

    Case/quote/punctuation folding is single-sourced from the title-snippet
    guard. Source-XML markup runs (see :data:`_TAG_RE`), diacritics and
    ligatures are folded on top of it, because a curator
    transcribing ``Guillain-Barre`` for a cached ``Guillain-Barré`` (or ``ae``
    for a PDF-extracted ``æ``) has not misidentified the paper -- and without
    this the accent alone costs enough similarity to push an otherwise clean
    pair under the threshold. Folding is applied to *both* sides, so it can only
    bring a faithful transcription and its source back into agreement; it can
    never make two genuinely different titles match.
    """
    text = html.unescape(text)
    text = _TAG_RE.sub(" ", text)
    text = CachedReferenceIndex.fold_ligatures(text)
    decomposed = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    return _fold_case_and_punctuation(text)


def contains(outer: str, inner: str) -> bool:
    """True when *inner* is a contiguous word run inside *outer*.

    Both arguments must already be normalised. Compared on word boundaries so a
    short title cannot match mid-word.
    """
    return bool(inner) and f" {inner} " in f" {outer} "


def exempt_prefix_set() -> frozenset[str]:
    """Case-folded reference prefixes whose cached title is not comparable."""
    return _SCRAPED_PREFIXES | dataset_prefixes()


def similarity(left: str, right: str) -> float:
    """Similarity ratio of two already-normalised strings, 0.0-1.0."""
    if not left or not right:
        return 0.0
    if left == right:
        return 1.0
    return difflib.SequenceMatcher(None, left, right).ratio()


def iter_title_pairs(
    data: Any, reference_fields: Iterable[str]
) -> Iterator[tuple[str, str, str, str]]:
    """Yield ``(location, field, reference_id, title)`` for every titled reference.

    A node qualifies when it carries both a reference field (``reference``, per
    the schema's ``linkml:authoritative_reference``) and one of
    :data:`TITLE_FIELDS`. Both ``evidence:`` items and top-level ``references:``
    entries are shaped that way, so one walk covers both.
    """
    references = tuple(sorted(reference_fields))

    def walk(node: Any, location: str) -> Iterator[tuple[str, str, str, str]]:
        if isinstance(node, dict):
            reference_id = next(
                (
                    node[name]
                    for name in references
                    if isinstance(node.get(name), str) and node[name].strip()
                ),
                None,
            )
            if reference_id is not None:
                for name in TITLE_FIELDS:
                    title = node.get(name)
                    if isinstance(title, str) and title.strip():
                        child = f"{location}.{name}" if location else name
                        yield (child, name, reference_id.strip(), title)
            for key, value in node.items():
                child = f"{location}.{key}" if location else str(key)
                yield from walk(value, child)
        elif isinstance(node, list):
            for index, value in enumerate(node):
                yield from walk(value, f"{location}[{index}]")

    yield from walk(data, "")


def find_violations(data, reference_fields, index, exempt_prefixes=None):
    """Yield ``(location, reference_id, title, cached_title, ratio)`` mismatches."""
    if exempt_prefixes is None:
        exempt_prefixes = exempt_prefix_set()
    for location, _field, reference_id, title in iter_title_pairs(
        data, reference_fields
    ):
        prefix, _, _ = reference_id.partition(":")
        if prefix.casefold() in exempt_prefixes:
            continue
        cache_path = index.resolve_cache_path(reference_id)
        if cache_path is None:
            # Uncached: `just fetch-reference` reports those, not this guard.
            continue
        cached_title = title_of(cache_path)
        if cached_title is None:
            continue
        curated, cached = normalize(title), normalize(cached_title)
        if contains(curated, cached) or contains(cached, curated):
            continue
        ratio = similarity(curated, cached)
        if ratio < MIN_SIMILARITY:
            yield (location, reference_id, title, cached_title, ratio)


def scan_repo(
    scan_dir: Path = SCAN_DIR,
    schema_path: Path | None = None,
    rel_to: Path = ROOT,
    cache_dir: Path | None = None,
):
    """Return sorted ``(relpath, location, reference, title, cached, ratio)``.

    ``cache_dir`` defaults to :data:`CACHE_DIR` but is resolved at call time,
    not bound as a default: :func:`baseline_from_ref` reaches this through two
    frames, so a default evaluated at import would make the cache location
    unoverridable from there.
    """
    _excerpt_fields, reference_fields = discover_field_names(
        schema_path if schema_path is not None else ROOT / DEFAULT_SCHEMA
    )
    index = CachedReferenceIndex(CACHE_DIR if cache_dir is None else cache_dir)
    exempt = exempt_prefix_set()
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception as exc:
            # Gating on malformed YAML is `validate-all`'s job; skipping silently
            # would make the file invisible here rather than merely unchecked.
            print(
                f"warning: skipping unparseable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        rel = path.relative_to(rel_to).as_posix()
        for location, reference_id, title, cached, ratio in find_violations(
            data, reference_fields, index, exempt
        ):
            findings.append((rel, location, reference_id, title, cached, ratio))
    return findings


def _baseline_key(rel: str, reference_id: str, title: str) -> str:
    # Keyed on (file, reference, title text) rather than the YAML location,
    # which shifts whenever a list above it grows. Whitespace is collapsed
    # because the baseline file is line-oriented and titles wrap freely in YAML.
    return f"{rel}\t{reference_id}\t{' '.join(title.split())}"


def count_by_key(findings) -> Counter:
    """How many times each ``(file, reference, title)`` appears in *findings*."""
    return Counter(
        _baseline_key(rel, reference_id, title)
        for rel, _, reference_id, title, _, _ in findings
    )


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    """Read the baseline as ``{key: grandfathered occurrence count}``.

    The count matters for the same reason it does in the sibling guards: one
    wrong title pasted across several evidence items is worse than one, and a
    plain set of keys would let the extra copies through silently.
    """
    counts: Counter = Counter()
    if not path.exists():
        return counts
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        count, tab, key = line.partition("\t")
        if tab and count.isdigit():
            counts[key] = int(count)
        else:  # tolerate a pre-count baseline
            counts[line] = counts.get(line, 0) + 1
    return counts


def write_baseline(findings, path: Path = BASELINE_PATH) -> None:
    counts = count_by_key(findings)
    header = (
        "# Grandfathered reference titles that do not match their cached\n"
        "# `title:` (see scripts/check_reference_titles.py and issue #9138).\n"
        "# Each line is `count<TAB>path<TAB>reference<TAB>title`, where count is\n"
        "# how many times that title is written against that reference in that\n"
        "# file. A mismatching title fails the guard if it is absent here OR\n"
        "# appears MORE often than the count recorded. Remove entries as the\n"
        "# backlog is fixed; do not add new ones -- the correct title is in the\n"
        "# reference's cache frontmatter, so a fix is a copy-paste.\n"
        "# Regenerate with:\n"
        "#   just update-reference-title-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def baseline_from_ref(ref: str, root: Path = ROOT) -> Counter | None:
    """Baseline derived live from ``kb/`` at a git *ref*.

    Titles are resolved against the working-tree cache -- see the module
    docstring for why the cache is not archived alongside. Returns ``None`` if
    *ref* cannot be read (no git, ref absent in a shallow checkout, ...), so the
    caller can fall back to the committed baseline. On failure git's own stderr
    is surfaced, so a CI misconfiguration is diagnosable rather than a silent
    capability downgrade.
    """
    # Relative to the real ROOT (always ``kb``), not *root*: tests pass a
    # throwaway repo as *root* while the layout under it is still ``kb/``.
    scan_rel = SCAN_DIR.relative_to(ROOT).as_posix()
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "archive", "--format=tar", ref, "--", scan_rel],
            capture_output=True,
            check=False,  # returncode handled explicitly below (PLW1510)
        )
    except (FileNotFoundError, OSError) as exc:
        print(
            f"reference-title baseline: git archive for {ref!r} could not run: {exc}",
            file=sys.stderr,
        )
        return None
    if proc.returncode != 0:
        detail = (
            proc.stderr.decode("utf-8", "replace").strip() or f"exit {proc.returncode}"
        )
        print(
            f"reference-title baseline: git archive {ref!r} failed: {detail}",
            file=sys.stderr,
        )
        return None
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        try:
            with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tar:
                # filter="data" is the safe extraction policy that becomes the
                # default in 3.14; set explicitly to pin behavior. The archive is
                # git-authored (kb/ only), so it never rejects a real member.
                tar.extractall(tmp_path, filter="data")
        except tarfile.TarError as exc:
            print(
                f"reference-title baseline: unreadable archive for {ref!r}: {exc}",
                file=sys.stderr,
            )
            return None
        findings = scan_repo(scan_dir=tmp_path / scan_rel, rel_to=tmp_path)
    return count_by_key(findings)


def resolve_baseline(ref: str | None = None) -> Counter:
    """The grandfather baseline: live from *ref* when given, else the committed file."""
    if ref is None:
        ref = os.environ.get(BASELINE_REF_ENV) or None
    if ref:
        from_ref = baseline_from_ref(ref)
        if from_ref is not None:
            # State which baseline engaged: the gate behaves differently
            # depending on whether the ref was reachable, so make that legible
            # in CI logs instead of leaving it to be inferred.
            print(
                f"reference-title baseline: grandfathered against ref {ref!r} "
                f"({len(from_ref)} distinct title(s))",
                file=sys.stderr,
            )
            return from_ref
        print(
            f"reference-title baseline: could not read ref {ref!r}; "
            "falling back to the committed baseline",
            file=sys.stderr,
        )
    return load_baseline()


def new_findings(findings, baseline: Counter):
    """Findings not covered by *baseline*, including extra reuses of a known one."""
    seen: Counter = Counter()
    new = []
    for finding in findings:
        key = _baseline_key(finding[0], finding[2], finding[3])
        seen[key] += 1
        if seen[key] > baseline.get(key, 0):
            new.append(finding)
    return new


def _format(finding) -> str:
    rel, location, reference_id, title, cached, ratio = finding
    flat = " ".join(title.split())
    return (
        f"{rel}:{location}: {reference_id} (similarity {ratio:.2f})\n"
        f"    curated: {flat}\n"
        f"     cached: {cached}"
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--check", action="store_true", help="(default) fail on non-baselined findings"
    )
    group.add_argument("--all", action="store_true", help="list every finding")
    group.add_argument("--count", action="store_true", help="print summary counts")
    group.add_argument(
        "--update-baseline",
        action="store_true",
        help="rewrite the baseline from current findings",
    )
    parser.add_argument(
        "--against-ref",
        metavar="REF",
        default=None,
        help=(
            "grandfather against the mismatching titles present in kb/ at this "
            f"git ref instead of the committed baseline (env: {BASELINE_REF_ENV}). "
            "CI uses the base branch so it is green by construction."
        ),
    )
    args = parser.parse_args(argv)

    findings = scan_repo()

    if args.update_baseline:
        write_baseline(findings)
        print(
            f"Wrote baseline with {len(findings)} finding(s) to "
            f"{BASELINE_PATH.relative_to(ROOT)}"
        )
        return 0

    if args.all:
        for finding in findings:
            print(_format(finding))
        print(
            f"\n{len(findings)} reference title(s) below similarity "
            f"{MIN_SIMILARITY} against their cached title."
        )
        return 0

    if args.count:
        baseline = resolve_baseline(args.against_ref)
        files = {rel for rel, *_ in findings}
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(
            f"baseline: {len(baseline)} distinct title(s), "
            f"{sum(baseline.values())} grandfathered occurrence(s)"
        )
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        return 0

    baseline = resolve_baseline(args.against_ref)
    new = new_findings(findings, baseline)
    if new:
        print("Reference title(s) that do not match the cited reference detected.")
        print("`reference_title` / `title` is the title of the paper you cited, and")
        print("the correct value is already on disk in that reference's cache")
        print("frontmatter -- copy it from the `cached:` line below. A verified")
        print("snippet does not vouch for the citation written beside it.\n")
        for finding in new:
            print(_format(finding))
        print(f"\n{len(new)} new finding(s).")
        if args.against_ref or os.environ.get(BASELINE_REF_ENV):
            # A ref baseline (CI) never reads tests/reference_title_baseline.txt,
            # so --update-baseline would pass locally and still fail CI.
            print("Grandfathering is unavailable when checking against a ref: use")
            print("the cached title, or drop the field if you cannot source one.")
        else:
            print("If a finding is genuinely unavoidable, run --update-baseline")
            print("to grandfather it.")
        return 1
    print(
        f"OK: no new reference titles below similarity {MIN_SIMILARITY} "
        f"({sum(baseline.values())} occurrence(s) of {len(baseline)} distinct "
        "title(s) grandfathered in baseline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
