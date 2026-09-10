#!/usr/bin/env python3
"""Semi-deterministic GeneReviews (and StatPearls) baseline check.

The review skill's item 15 asks, for every new Mendelian entry, whether a
GeneReviews chapter exists for the disease and, if so, whether it is tagged in
the top-level ``references:`` block and mined for evidence. Until now the
"does one exist" half was a ``curl`` to PubMed that the automated reviewer
cannot run -- its sandbox permits ``just`` and ``uv run`` and blocks every
network tool -- so on PR #11592 the reviewer recorded, twice, that it could not
verify the entry's "no GeneReviews chapter exists" note. The curator then had
to prove a negative by hand.

This check answers the question offline, from the committed Bookshelf index
(``cache/bookshelf/``; see ``scripts/build_bookshelf_index.py`` and
:mod:`dismech.bookshelf`), and splits the answer into a deterministic part and
a judgement part:

Deterministic
    * whether each ``PMID``/``NBK`` the entry tags as ``GeneReviews`` or
      ``StatPearls`` really is a chapter of that collection (``MISTAGGED``
      otherwise);
    * whether the entry *cites* a chapter PMID anywhere without tagging it
      (``CITED_UNTAGGED`` -- ``just tag-references`` fixes it);
    * whether a chapter whose title is, after normalisation, **exactly** one
      of the entry's names exists and is not tagged (``UNTAGGED_CHAPTER``).

Judgement
    * partial title matches -- the name inside a longer title, the title
      inside a longer name, or a near-identical string -- are reported as
      ``CANDIDATE_CHAPTER`` with the title and the match kind, for a person
      (or the reviewer) to read. ``Alpha Thalassemia`` inside ``Alpha-
      Thalassemia X-Linked Intellectual Disability Syndrome`` is such a
      candidate, and is not that disease's chapter.

Verdict per collection, strongest first::

    MISTAGGED          a tagged reference is not a chapter of that collection
    CITED_UNTAGGED     a chapter PMID is cited in the file but not tagged
    UNTAGGED_CHAPTER   an exact-title chapter exists and is not tagged
    TAGGED             at least one tagged reference is a verified chapter
    CANDIDATE_CHAPTER  only partial matches, or only a retired chapter
    NO_CHAPTER         nothing in the snapshot names this entry

``GeneReviews`` findings gate under ``--strict`` (``MISTAGGED``,
``CITED_UNTAGGED``, ``UNTAGGED_CHAPTER``); ``StatPearls`` never gates -- it is a
different kind of source (see :mod:`dismech.bookshelf`) and dismech has no
policy that an entry must cite it. Neither ``CANDIDATE_CHAPTER`` nor a
``TAGGED`` entry that also has an untagged candidate is a failure: the check
reports them because those are exactly the rows a reviewer should look at.

The index is a snapshot (``MANIFEST.yaml`` records the date). ``--online`` adds
a live PubMed title search per name so a chapter published since the snapshot
is caught; it needs network and is not used by the reviewer.

Usage::

    just check-genereviews kb/disorders/Dandy-Walker_Syndrome.yaml
    just check-genereviews                       # whole KB, findings only
    just check-genereviews --strict FILE...      # exit 1 on a GeneReviews gap
    uv run python scripts/check_genereviews_baseline.py --format tsv
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from dismech import kb_cache  # noqa: E402
from dismech.bookshelf import (  # noqa: E402
    DEFAULT_INDEX_DIR,
    SOURCE_TAGS,
    BookshelfIndex,
    Chapter,
    Match,
    entry_names,
    source_from_cache_text,
)

DISORDERS_DIR = REPO_ROOT / "kb" / "disorders"
CACHE_DIR = REPO_ROOT / "references_cache"

VERDICTS = (
    "MISTAGGED",
    "CITED_UNTAGGED",
    "UNTAGGED_CHAPTER",
    "TAGGED",
    "CANDIDATE_CHAPTER",
    "NO_CHAPTER",
)
GATING_VERDICTS = {"MISTAGGED", "CITED_UNTAGGED", "UNTAGGED_CHAPTER"}
GATED_SOURCES = {"genereviews"}

_PMID_RE = re.compile(r"PMID:(\d+)")
_NBK_RE = re.compile(r"NBK\d+")
_BOOKSHELF_URL_RE = re.compile(r"ncbi\.nlm\.nih\.gov/books/")


@dataclass
class ChapterRow:
    """One chapter the entry relates to, and how."""

    pmid: str
    nbk: str
    title: str
    retired: bool
    kind: (
        str  #: EXACT / CONTAINS / TITLE_IN_NAME / NEAR / ONLINE, or "" for tagged-only
    )
    name: str  #: entry name that matched ("" when found only by citation)
    tagged: bool
    cited: bool
    cited_as: str = ""  #: "PMID" or "NBK" -- how the file cites it, when it does


@dataclass
class TagProblem:
    reference: str
    problem: str  #: MISTAGGED or TAGGED_UNVERIFIED
    detail: str


@dataclass
class SourceReport:
    source: str
    verdict: str
    chapters: list[ChapterRow] = field(default_factory=list)
    tag_problems: list[TagProblem] = field(default_factory=list)


@dataclass
class EntryReport:
    path: str
    names: list[str]
    sources: dict[str, SourceReport]

    @property
    def gating(self) -> bool:
        return any(
            report.verdict in GATING_VERDICTS
            for source, report in self.sources.items()
            if source in GATED_SOURCES
        )

    @property
    def noteworthy(self) -> bool:
        return any(report.verdict != "NO_CHAPTER" for report in self.sources.values())


# -- entry inspection --------------------------------------------------------


def tagged_references(document: dict) -> dict[str, set[str]]:
    """``{tag: {reference strings}}`` from the top-level ``references:`` block."""
    result: dict[str, set[str]] = {tag: set() for tag in SOURCE_TAGS.values()}
    for entry in document.get("references") or []:
        if not isinstance(entry, dict):
            continue
        reference = str(entry.get("reference") or "")
        for tag in entry.get("tags") or []:
            if str(tag) in result and reference:
                result[str(tag)].add(reference)
    return result


def cited_identifiers(text: str) -> tuple[set[str], set[str]]:
    """Every PMID and NBK accession mentioned anywhere in the file text."""
    return set(_PMID_RE.findall(text)), set(_NBK_RE.findall(text))


def _verify_tag(
    reference: str, source: str, index: BookshelfIndex, cache_dir: Path
) -> tuple[Chapter | None, TagProblem | None]:
    """Resolve a tagged reference to a chapter, or explain why it is not one."""
    chapter = index.source_of(reference)
    if chapter is not None:
        if chapter.source == source:
            return chapter, None
        return None, TagProblem(
            reference,
            "MISTAGGED",
            f"is a {chapter.tag} chapter ({chapter.title!r}), tagged {SOURCE_TAGS[source]}",
        )
    pmid = _PMID_RE.search(reference)
    if pmid:
        cache_file = cache_dir / f"PMID_{pmid.group(1)}.md"
        if cache_file.exists():
            marked = source_from_cache_text(cache_file.read_text(encoding="utf-8"))
            if marked == source:
                # Cached as a Bookshelf citation but absent from the snapshot:
                # a chapter newer than the index, most likely. Accept it.
                return Chapter(
                    source, pmid.group(1), "", "(not in index snapshot)", False
                ), None
            if marked is not None:
                return None, TagProblem(
                    reference,
                    "MISTAGGED",
                    f"cache shows a {SOURCE_TAGS[marked]} citation",
                )
            return None, TagProblem(
                reference,
                "MISTAGGED",
                "not in the Bookshelf index and the cached record is not a Bookshelf citation",
            )
        return None, TagProblem(
            reference, "TAGGED_UNVERIFIED", "not in the Bookshelf index and not cached"
        )
    if _NBK_RE.search(reference):
        return None, TagProblem(
            reference, "TAGGED_UNVERIFIED", "NBK accession not in the Bookshelf index"
        )
    if _BOOKSHELF_URL_RE.search(reference):
        # e.g. url:https://www.ncbi.nlm.nih.gov/books/n/gene/<slug>/ -- a Bookshelf
        # URL keyed on a chapter slug rather than an NBK accession; nothing offline
        # can resolve the slug, so it is unverified rather than wrong.
        return None, TagProblem(
            reference,
            "TAGGED_UNVERIFIED",
            "Bookshelf URL without an NBK accession; cannot be resolved offline",
        )
    return None, TagProblem(reference, "MISTAGGED", "not a PMID or Bookshelf URL")


def assess_source(
    source: str,
    names: list[str],
    tagged: set[str],
    cited_pmids: set[str],
    cited_nbks: set[str],
    index: BookshelfIndex,
    cache_dir: Path,
    online_matches: list[Match] = (),
) -> SourceReport:
    report = SourceReport(source=source, verdict="NO_CHAPTER")
    rows: dict[str, ChapterRow] = {}
    verified_tagged: set[str] = set()

    for reference in sorted(tagged):
        chapter, problem = _verify_tag(reference, source, index, cache_dir)
        if problem is not None:
            report.tag_problems.append(problem)
            continue
        assert chapter is not None
        verified_tagged.add(chapter.pmid)
        rows[chapter.pmid] = ChapterRow(
            chapter.pmid,
            chapter.nbk,
            chapter.title,
            chapter.retired,
            "",
            "",
            True,
            True,
            _cited_as(chapter, cited_pmids, cited_nbks),
        )

    # Chapters cited anywhere in the file (evidence items included), by identity.
    for pmid in sorted(cited_pmids):
        chapter = index.by_pmid.get(pmid)
        if chapter is None or chapter.source != source or pmid in rows:
            continue
        rows[pmid] = ChapterRow(
            chapter.pmid,
            chapter.nbk,
            chapter.title,
            chapter.retired,
            "",
            "",
            False,
            True,
            "PMID",
        )
    for nbk in sorted(cited_nbks):
        chapter = index.by_nbk.get(nbk)
        if chapter is None or chapter.source != source or chapter.pmid in rows:
            continue
        rows[chapter.pmid] = ChapterRow(
            chapter.pmid,
            chapter.nbk,
            chapter.title,
            chapter.retired,
            "",
            "",
            False,
            True,
            "NBK",
        )

    # Chapters whose title names the entry.
    matches: list[Match] = []
    for name in names:
        matches.extend(index.match(name, sources=[source]))
    matches.extend(m for m in online_matches if m.chapter.source == source)
    for match in sorted(matches, key=lambda m: (m.rank, int(m.chapter.pmid))):
        pmid = match.chapter.pmid
        if pmid in rows:
            if not rows[pmid].kind or match.rank < _rank(rows[pmid].kind):
                rows[pmid].kind, rows[pmid].name = match.kind, match.name
            continue
        cited_as = _cited_as(match.chapter, cited_pmids, cited_nbks)
        rows[pmid] = ChapterRow(
            pmid,
            match.chapter.nbk,
            match.chapter.title,
            match.chapter.retired,
            match.kind,
            match.name,
            False,
            bool(cited_as),
            cited_as,
        )

    report.chapters = sorted(
        rows.values(), key=lambda r: (not r.tagged, _rank(r.kind), int(r.pmid))
    )

    if any(p.problem == "MISTAGGED" for p in report.tag_problems):
        report.verdict = "MISTAGGED"
    elif any(r.cited and not r.tagged for r in report.chapters):
        report.verdict = "CITED_UNTAGGED"
    elif any(
        r.kind == "EXACT" and not r.tagged and not r.retired for r in report.chapters
    ):
        report.verdict = "UNTAGGED_CHAPTER"
    elif verified_tagged:
        report.verdict = "TAGGED"
    elif report.chapters:
        report.verdict = "CANDIDATE_CHAPTER"
    return report


def _cited_as(chapter: Chapter, cited_pmids: set[str], cited_nbks: set[str]) -> str:
    if chapter.pmid in cited_pmids:
        return "PMID"
    if chapter.nbk and chapter.nbk in cited_nbks:
        return "NBK"
    return ""


def _rank(kind: str) -> int:
    order = {
        "EXACT": 0,
        "ONLINE": 0,
        "CONTAINS": 1,
        "TITLE_IN_NAME": 2,
        "NEAR": 3,
        "": 9,
    }
    return order.get(kind, 9)


def assess_entry(
    path: Path,
    document: dict,
    text: str,
    index: BookshelfIndex,
    *,
    cache_dir: Path = CACHE_DIR,
    sources: list[str] | None = None,
    online: "OnlineSearch | None" = None,
    rel_to: Path = REPO_ROOT,
) -> EntryReport:
    names = entry_names(document)
    tagged = tagged_references(document)
    cited_pmids, cited_nbks = cited_identifiers(text)
    online_matches = online.search(names) if online is not None else []
    try:
        rel = path.resolve().relative_to(rel_to.resolve()).as_posix()
    except ValueError:
        rel = path.as_posix()
    return EntryReport(
        path=rel,
        names=names,
        sources={
            source: assess_source(
                source,
                names,
                tagged[SOURCE_TAGS[source]],
                cited_pmids,
                cited_nbks,
                index,
                cache_dir,
                online_matches,
            )
            for source in (sources or list(SOURCE_TAGS))
        },
    )


# -- optional live supplement -------------------------------------------------


class OnlineSearch:
    """Live ``<name>[TI] AND <source>[book]`` searches, for chapters newer than the snapshot."""

    def __init__(self, index: BookshelfIndex, sources: list[str]):
        from build_bookshelf_index import (
            NcbiClient,
        )  # scripts/ is sys.path[0] under `python scripts/x.py`

        self.client = NcbiClient(os.environ.get("NCBI_API_KEY"))
        self.index = index
        self.sources = sources

    def search(self, names: list[str]) -> list[Match]:
        found: list[Match] = []
        for source in self.sources:
            for name in names:
                term = f"{name}[TI] AND {source}[book]"
                try:
                    ids = self.client.call("esearch.fcgi", db="pubmed", term=term)[
                        "esearchresult"
                    ].get("idlist", [])
                except Exception as exc:  # network is optional; say so and move on
                    print(
                        f"warning: online search failed for {term!r}: {exc}",
                        file=sys.stderr,
                    )
                    continue
                new = [pmid for pmid in ids if pmid not in self.index.by_pmid]
                if not new:
                    continue
                result = self.client.call(
                    "esummary.fcgi", db="pubmed", id=",".join(new)
                )["result"]
                for pmid in new:
                    record = result.get(pmid, {})
                    nbk = next(
                        (
                            a["value"]
                            for a in record.get("articleids", [])
                            if a.get("idtype") == "bookaccession"
                        ),
                        "",
                    )
                    found.append(
                        Match(
                            Chapter(source, pmid, nbk, record.get("title", ""), False),
                            "ONLINE",
                            name,
                        )
                    )
        return found


# -- output -----------------------------------------------------------------


def format_text(report: EntryReport, *, show_all: bool) -> list[str]:
    lines = [report.path]
    for source, sr in report.sources.items():
        if sr.verdict == "NO_CHAPTER" and not show_all:
            continue
        lines.append(f"  {SOURCE_TAGS[source]:<12} {sr.verdict}")
        for problem in sr.tag_problems:
            lines.append(
                f"      {problem.problem}: {problem.reference} -- {problem.detail}"
            )
        for row in sr.chapters:
            if row.tagged:
                state = "tagged"
            elif row.cited:
                state = f"cited as {row.cited_as}, not tagged"
            else:
                state = "not cited"
            how = f"{row.kind} via {row.name!r}" if row.kind else "by identity"
            retired = " [retired chapter]" if row.retired else ""
            lines.append(
                f"      PMID:{row.pmid} {row.nbk} {row.title!r}{retired} -- {how}; {state}"
            )
    if show_all:
        lines.append("  names searched: " + "; ".join(report.names))
    return lines


def to_dict(report: EntryReport) -> dict:
    return {
        "path": report.path,
        "names": report.names,
        "gating": report.gating,
        "sources": {source: asdict(sr) for source, sr in report.sources.items()},
    }


def format_tsv_rows(report: EntryReport) -> list[str]:
    rows = []
    for source, sr in report.sources.items():
        if not sr.chapters and not sr.tag_problems:
            rows.append(
                "\t".join(
                    [report.path, SOURCE_TAGS[source], sr.verdict, "", "", "", "", ""]
                )
            )
        for row in sr.chapters:
            rows.append(
                "\t".join(
                    [
                        report.path,
                        SOURCE_TAGS[source],
                        sr.verdict,
                        f"PMID:{row.pmid}",
                        row.nbk,
                        row.kind or "identity",
                        "tagged"
                        if row.tagged
                        else ("cited" if row.cited else "uncited"),
                        row.title,
                    ]
                )
            )
        for problem in sr.tag_problems:
            rows.append(
                "\t".join(
                    [
                        report.path,
                        SOURCE_TAGS[source],
                        sr.verdict,
                        problem.reference,
                        "",
                        problem.problem,
                        "",
                        problem.detail,
                    ]
                )
            )
    return rows


# -- driver -------------------------------------------------------------------


def iter_targets(paths: list[Path]) -> list[Path]:
    if not paths:
        return sorted(
            p
            for p in DISORDERS_DIR.glob("*.yaml")
            if not p.name.endswith(".history.yaml")
        )
    out: list[Path] = []
    for path in paths:
        if path.is_dir():
            out.extend(sorted(path.glob("*.yaml")))
        else:
            out.append(path)
    return out


def scan(
    paths: list[Path],
    index: BookshelfIndex,
    *,
    cache_dir: Path = CACHE_DIR,
    sources: list[str] | None = None,
    online: OnlineSearch | None = None,
) -> list[EntryReport]:
    reports = []
    for path in iter_targets(paths):
        document = kb_cache.load_document(path)
        if not isinstance(document, dict):
            print(f"warning: skipping {path}: not a mapping", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        reports.append(
            assess_entry(
                path,
                document,
                text,
                index,
                cache_dir=cache_dir,
                sources=sources,
                online=online,
            )
        )
    return reports


def summarize(
    reports: list[EntryReport], index: BookshelfIndex, sources: list[str]
) -> list[str]:
    lines = [
        f"Bookshelf index snapshot {index.snapshot_date or 'unknown'}: "
        + ", ".join(
            f"{len([r for r in index.rows if r.chapter.source == s])} {SOURCE_TAGS[s]}"
            for s in sources
        )
        + f"; {len(reports)} entr{'y' if len(reports) == 1 else 'ies'} checked"
    ]
    for source in sources:
        counts = {v: 0 for v in VERDICTS}
        for report in reports:
            counts[report.sources[source].verdict] += 1
        parts = [f"{v}={n}" for v, n in counts.items() if n]
        lines.append(f"  {SOURCE_TAGS[source]:<12} " + "  ".join(parts))
    return lines


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="disorder YAML files (default: all of kb/disorders/)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 on a GeneReviews MISTAGGED / CITED_UNTAGGED / UNTAGGED_CHAPTER",
    )
    parser.add_argument(
        "--online",
        action="store_true",
        help="also run live PubMed title searches (network)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="print every entry, including NO_CHAPTER, with the names searched",
    )
    parser.add_argument("--format", choices=["text", "tsv", "json"], default="text")
    parser.add_argument(
        "--source",
        action="append",
        choices=sorted(SOURCE_TAGS),
        help="restrict to one collection (repeatable)",
    )
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    parser.add_argument("--cache-dir", type=Path, default=CACHE_DIR)
    args = parser.parse_args(argv)

    sources = args.source or list(SOURCE_TAGS)
    index = BookshelfIndex.load(args.index_dir, sources=sources)
    if not len(index):
        print(
            f"error: no Bookshelf index under {args.index_dir}; run `just refresh-bookshelf-index`",
            file=sys.stderr,
        )
        return 2
    online = OnlineSearch(index, sources) if args.online else None
    reports = scan(
        args.files, index, cache_dir=args.cache_dir, sources=sources, online=online
    )

    if args.format == "json":
        print(json.dumps([to_dict(r) for r in reports], indent=1))
    elif args.format == "tsv":
        print(
            "\t".join(
                [
                    "path",
                    "collection",
                    "verdict",
                    "reference",
                    "nbk",
                    "match",
                    "state",
                    "title",
                ]
            )
        )
        for report in reports:
            print("\n".join(format_tsv_rows(report)))
    else:
        for report in reports:
            if args.all or report.noteworthy:
                print("\n".join(format_text(report, show_all=args.all)))
        print()
        print("\n".join(summarize(reports, index, sources)))
        if any(r.gating for r in reports):
            print(
                "\nGeneReviews gaps above: tag the chapter in the top-level `references:` block\n"
                "(`just tag-references FILE` does it for a chapter cited by PMID; a chapter cited\n"
                "only by its NBK url is tagged by hand) and mine it for evidence, or record in\n"
                "`notes:` why the matched chapter is not this disease's."
            )

    if args.strict and any(r.gating for r in reports):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
