"""Tests for the citation-forward scan (papers citing an entry's references)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "citation_scan.py"
SPEC = importlib.util.spec_from_file_location("citation_scan", SCRIPT_PATH)
assert SPEC and SPEC.loader
citation_scan = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = citation_scan
SPEC.loader.exec_module(citation_scan)


def entry(path: str, pmids: set[str], cited: set[str] = frozenset()) -> object:
    refs = {f"PMID:{p}" for p in pmids | set(cited)}
    return citation_scan.Entry(
        path=path, name=Path(path).stem, pmids=set(pmids), references=refs
    )


class StubEuropePMC:
    """Answers the three request shapes run_scan makes."""

    def __init__(
        self,
        citing: dict[str, dict],
        references: dict[str, set[str]],
        cited_by: dict[str, int],
    ):
        self.citing = citing
        self.reference_lists = references
        self.cited_by = cited_by
        self.queries: list[str] = []
        self.requests = 0

    def search(self, query: str, result_type: str = "lite") -> list[dict]:
        self.queries.append(query)
        if "CITES:" in query:
            return [
                record
                for record in self.citing.values()
                if any(
                    f"CITES:{ref}_MED" in query
                    for ref in self.reference_lists[record["pmid"]]
                )
            ]
        pmids = [p for p in self.cited_by if f"EXT_ID:{p}" in query] + [
            p for p in self.citing if f"EXT_ID:{p}" in query
        ]
        return [
            {
                "pmid": p,
                "citedByCount": self.cited_by.get(p, 0),
                "abstractText": f"Abstract {p}",
            }
            for p in pmids
        ]

    def references(self, pmid: str) -> set[str]:
        return self.reference_lists[pmid]


def test_cites_query_filters_on_index_date_not_publication_date() -> None:
    query = citation_scan.build_cites_query(["1", "22"], "2026-10-01", "2026-10-07")

    assert query.startswith("(CITES:1_MED OR CITES:22_MED)")
    assert "FIRST_IDATE:[2026-10-01 TO 2026-10-07]" in query
    assert "FIRST_PDATE" not in query
    assert "SRC:MED" in query


def test_reference_weight_favours_rarely_cited_references() -> None:
    rare = citation_scan.reference_weight(10)
    classic = citation_scan.reference_weight(5000)

    assert citation_scan.reference_weight(0) == 1.0
    assert rare > classic
    # An unknown count must not look rare: a failed lookup cannot inflate a score.
    assert citation_scan.reference_weight(None) < rare


def test_score_counts_overlap_per_entry_and_skips_already_cited() -> None:
    candidates = {
        "900": citation_scan.Candidate(pmid="900", references={"1", "2", "3", "50"}),
        "901": citation_scan.Candidate(pmid="901", references={"1"}),
    }
    entries = [
        entry("kb/disorders/A.yaml", {"1", "2", "3"}),
        entry("kb/disorders/B.yaml", {"1"}, cited={"901"}),
    ]

    rows = citation_scan.score_overlaps(
        candidates, entries, {"1": 5000, "2": 10, "3": 10}
    )
    pairs = {(row["pmid"], row["entry"]): row for row in rows}

    assert pairs[("900", "kb/disorders/A.yaml")]["overlap"] == 3
    assert pairs[("901", "kb/disorders/A.yaml")]["overlap"] == 1
    assert ("901", "kb/disorders/B.yaml") not in pairs  # B already cites 901
    assert rows[0]["pmid"] == "900" and rows[0]["entry"] == "kb/disorders/A.yaml"


def test_ledger_reads_markers_and_legacy_lit_scan_bodies() -> None:
    issues = [
        {
            "number": 10,
            "title": "[citation-scan] A: something",
            "state": "CLOSED",
            "stateReason": "COMPLETED",
            "body": "<!-- citation-scan pmid=900 entry=kb/disorders/A.yaml overlap=2 -->",
        },
        {
            "number": 11,
            "title": "[lit-scan] B: other",
            "state": "closed",
            "state_reason": "completed",  # REST spelling
            "body": "PMID: 901\nLikely file: kb/disorders/B.yaml",
        },
    ]

    decisions = citation_scan.parse_ledger(issues)

    assert (
        citation_scan.LedgerDecision(
            10, "CLOSED", "COMPLETED", "900", "kb/disorders/A.yaml", 2
        )
        in decisions
    )
    assert (
        citation_scan.LedgerDecision(
            11, "CLOSED", "COMPLETED", "901", "kb/disorders/B.yaml", None
        )
        in decisions
    )


def test_ledger_suppresses_decided_pairs_and_resurfaces_on_a_larger_overlap() -> None:
    decisions = [
        citation_scan.LedgerDecision(1, "OPEN", "", "900", "kb/disorders/A.yaml", 1),
        citation_scan.LedgerDecision(
            2, "CLOSED", "COMPLETED", "901", "kb/disorders/A.yaml", 1
        ),
        citation_scan.LedgerDecision(3, "CLOSED", "DUPLICATE", "902", None, None),
    ]

    def verdict(pmid: str, overlap: int, path: str = "kb/disorders/A.yaml") -> str:
        return citation_scan.ledger_verdict(
            {"pmid": pmid, "entry": path, "overlap": overlap}, decisions
        )[0]

    assert verdict("900", 5) == "open_issue"
    assert (
        verdict("901", 2) == "closed_issue"
    )  # one more shared reference is not enough
    assert verdict("901", 3) == "resurfaced"  # recorded 1 + margin 2
    assert (
        verdict("902", 9, "kb/disorders/Z.yaml") == "closed_issue"
    )  # no entry named: applies to all
    assert verdict("903", 1) == "new"


def test_run_scan_end_to_end_with_stub(tmp_path: Path) -> None:
    api = StubEuropePMC(
        citing={
            "900": {"pmid": "900", "title": "New paper", "pubType": "research-article"},
            "901": {"pmid": "901", "title": "Erratum", "pubType": "Published Erratum"},
        },
        references={"900": {"1", "2"}, "901": {"1"}},
        cited_by={"1": 10, "2": 4000},
    )
    entries = [entry("kb/disorders/A.yaml", {"1", "2"})]

    packet = citation_scan.run_scan(
        api,
        entries,
        date_from="2026-10-01",
        date_to="2026-10-07",
        cache_dir=tmp_path,
    )

    assert packet["candidate_count"] == 1  # the erratum is dropped
    [row] = packet["records"]
    assert row["pmid"] == "900" and row["overlap"] == 2
    assert row["abstract"] == "Abstract 900"
    assert (
        row["marker"]
        == "<!-- citation-scan pmid=900 entry=kb/disorders/A.yaml overlap=2 -->"
    )
    # The marker the packet emits is one the ledger parser reads back.
    [decision] = citation_scan.parse_ledger(
        [{"number": 5, "state": "OPEN", "body": row["marker"]}]
    )
    assert (decision.pmid, decision.entry, decision.overlap) == (
        "900",
        "kb/disorders/A.yaml",
        2,
    )
    assert "Citation Scan Packet" in citation_scan.render_markdown(packet)


def test_min_overlap_drops_single_reference_pairs() -> None:
    candidates = {
        "900": citation_scan.Candidate(pmid="900", references={"1", "2"}),
        "901": citation_scan.Candidate(pmid="901", references={"1"}),
    }
    entries = [entry("kb/disorders/A.yaml", {"1", "2"})]

    rows = citation_scan.score_overlaps(candidates, entries, {}, min_overlap=2)

    assert [row["pmid"] for row in rows] == ["900"]


def test_cap_per_entry_keeps_small_entries_in_the_packet() -> None:
    rows = [{"entry": "big", "pmid": str(i)} for i in range(5)] + [
        {"entry": "small", "pmid": "9"}
    ]

    kept = citation_scan.cap_per_entry(rows, 2)

    assert [(row["entry"], row["pmid"]) for row in kept] == [
        ("big", "0"),
        ("big", "1"),
        ("small", "9"),
    ]
    assert citation_scan.cap_per_entry(rows, 0) == rows


def test_bookshelf_chapters_do_not_count_as_rare_references(tmp_path: Path) -> None:
    bookshelf = tmp_path / "bookshelf"
    bookshelf.mkdir()
    (bookshelf / "genereviews.csv").write_text(
        "pmid,nbk,retired,pubdate,title\n2,NBK1454,0,1993,Alkaptonuria.\n"
    )
    api = StubEuropePMC(
        citing={
            "900": {"pmid": "900", "title": "Case report", "pubType": "Case Reports"}
        },
        references={"900": {"1", "2"}},
        cited_by={"1": 10, "2": 1},  # Europe PMC undercounts the chapter
    )

    packet = citation_scan.run_scan(
        api,
        [entry("kb/disorders/A.yaml", {"1", "2"})],
        date_from="2026-10-01",
        date_to="2026-10-07",
        cache_dir=tmp_path,
        bookshelf_dir=bookshelf,
    )

    weights = {ref["pmid"]: ref for ref in packet["records"][0]["overlap_refs"]}
    assert weights["2"]["cited_by"] is None
    assert weights["2"]["weight"] == round(citation_scan.reference_weight(None), 3)


def test_reference_lists_are_reused_not_refetched(tmp_path: Path) -> None:
    api = StubEuropePMC(
        citing={"900": {"pmid": "900", "title": "New paper", "pubType": "Review"}},
        references={"900": {"1", "2"}},
        cited_by={"1": 10, "2": 10},
    )
    api.references = lambda pmid: (_ for _ in ()).throw(AssertionError("refetched"))
    known = {"900": ["1", "2"]}

    packet = citation_scan.run_scan(
        api,
        [entry("kb/disorders/A.yaml", {"1", "2"})],
        date_from="2026-10-01",
        date_to="2026-10-07",
        cache_dir=tmp_path,
        reference_lists=known,
    )

    assert packet["records"][0]["is_review"] is True
