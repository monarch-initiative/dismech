"""ClinGen validity rows checked against MONDO's own causal gene (#12941).

The worked case is the ClinGen row pairing COQ6 with ``MONDO:0014754``, a class
MONDO defines by COQ7. These tests pin the classification on synthetic rows and
a synthetic MONDO cache; nothing here touches the network.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import list_clingen_mondo_gene_mismatches as audit  # noqa: E402

HEADER = ",".join(f'"{h}"' for h in audit.CSV_HEADERS)
SEPARATOR = ",".join(['"+++"'] * len(audit.CSV_HEADERS))
URL = "https://search.clinicalgenome.org/kb/gene-validity/"


def _row(gene, hgnc, label, mondo, tier, record, moi="AR"):
    cells = [gene, hgnc, label, mondo, moi, "SOP11", tier, URL + record, "2024", "GCEP"]
    return ",".join(f'"{c}"' for c in cells)


def _csv(tmp_path: Path, *rows: str) -> Path:
    path = tmp_path / "gene_validity.csv"
    lines = [
        '"CLINGEN GENE DISEASE VALIDITY CURATIONS"',
        '"FILE CREATED: 2026-01-24"',
        SEPARATOR,
        HEADER,
        SEPARATOR,
        *rows,
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


CACHE = {
    "version": audit.CACHE_VERSION,
    "release": "2026-10-06",
    "terms": {
        "MONDO:0014754": {
            "label": "primary coenzyme Q10 deficiency 8",
            "obsolete": False,
            "genes": ["HGNC:2244"],
            "gene_labels": {"HGNC:2244": "COQ7"},
            "replaced_by": [],
        },
        "MONDO:0013836": {
            "label": "familial steroid-resistant nephrotic syndrome with sensorineural deafness",
            "obsolete": False,
            "genes": ["HGNC:20233"],
            "gene_labels": {"HGNC:20233": "COQ6"},
            "replaced_by": [],
        },
        "MONDO:0009026": {
            "label": "Costello syndrome",
            "obsolete": False,
            "genes": ["HGNC:5173"],
            "gene_labels": {"HGNC:5173": "HRAS"},
            "replaced_by": [],
        },
        "MONDO:0005045": {
            "label": "hypertrophic cardiomyopathy",
            "obsolete": False,
            "genes": [],
            "gene_labels": {},
            "replaced_by": [],
        },
        "MONDO:1040044": {
            "label": "BBS4-related ciliopathy",
            "obsolete": False,
            "genes": ["http://identifiers.org/ncbigene/487634"],
            "gene_labels": {},
            "replaced_by": [],
        },
        "MONDO:0017132": {
            "label": "obsolete hereditary ATTR amyloidosis",
            "obsolete": True,
            "genes": [],
            "gene_labels": {},
            "replaced_by": ["MONDO:0007100"],
        },
        "MONDO:0000001": {"not_found": True},
    },
}


def _classify(tmp_path, *rows):
    parsed, created = audit.read_rows(_csv(tmp_path, *rows))
    assert created == "2026-01-24"
    return [audit.classify(r, CACHE, {}) for r in parsed]


def test_coq6_row_names_another_gene(tmp_path):
    (finding,) = _classify(
        tmp_path,
        _row(
            "COQ6",
            "HGNC:20233",
            "primary coenzyme Q10 deficiency 8",
            "MONDO:0014754",
            "Definitive",
            "CGGV:assertion_x",
        ),
    )
    assert finding.status == audit.NAMES_ANOTHER_GENE
    assert finding.mondo_genes == ("HGNC:2244",)
    assert finding.mondo_gene_labels == ("COQ7",)


def test_matching_row_is_a_match(tmp_path):
    (finding,) = _classify(
        tmp_path,
        _row(
            "COQ6", "HGNC:20233", "x", "MONDO:0013836", "Definitive", "CGGV:assertion_y"
        ),
    )
    assert finding.status == audit.MATCH


def test_disputed_pairing_is_contested_not_a_finding(tmp_path):
    findings = _classify(
        tmp_path,
        _row(
            "KRAS",
            "HGNC:6407",
            "Costello syndrome",
            "MONDO:0009026",
            "Disputed",
            "CGGV:assertion_a",
        ),
        _row(
            "NRAS",
            "HGNC:7989",
            "Costello syndrome",
            "MONDO:0009026",
            "Limited",
            "CGGV:assertion_b",
        ),
    )
    assert [f.status for f in findings] == [
        audit.CONTESTED_PAIRING,
        audit.NAMES_ANOTHER_GENE,
    ]


def test_grouping_class_and_non_human_gene_have_no_causal_gene(tmp_path):
    findings = _classify(
        tmp_path,
        _row(
            "MYH7",
            "HGNC:7577",
            "hypertrophic cardiomyopathy",
            "MONDO:0005045",
            "Definitive",
            "CGGV:assertion_c",
        ),
        _row(
            "BBS4",
            "HGNC:969",
            "BBS4-related ciliopathy",
            "MONDO:1040044",
            "Definitive",
            "CGGV:assertion_d",
        ),
    )
    assert [f.status for f in findings] == [audit.NO_CAUSAL_GENE] * 2


def test_obsolete_not_found_and_uncached(tmp_path):
    findings = _classify(
        tmp_path,
        _row(
            "TTR", "HGNC:12405", "x", "MONDO:0017132", "Definitive", "CGGV:assertion_e"
        ),
        _row("ABC", "HGNC:1", "x", "MONDO:0000001", "Definitive", "CGGV:assertion_f"),
        _row("ABC", "HGNC:1", "x", "MONDO:0999999", "Definitive", "CGGV:assertion_g"),
    )
    assert [f.status for f in findings] == [
        audit.OBSOLETE,
        audit.NOT_FOUND,
        audit.UNCACHED,
    ]
    assert findings[0].replaced_by == ("MONDO:0007100",)


def test_legacy_record_id_is_kept():
    assert (
        audit._assertion_id(URL + "CGGCIEX:assertion_3211") == "CGGCIEX:assertion_3211"
    )
    assert audit._assertion_id(URL + "CGGV:assertion_abc-1") == "CGGV:assertion_abc-1"


def test_failed_lookup_is_never_cached_as_a_fact(monkeypatch):
    def fake_fetch(mondo_id, timeout):
        return mondo_id, {"error": "could not reach OLS"}

    monkeypatch.setattr(audit, "_fetch", fake_fetch)
    monkeypatch.setattr(audit, "fetch_mondo_release", lambda timeout: "")
    cache = {"version": audit.CACHE_VERSION, "release": "", "terms": {}}
    assert (
        audit.resolve({"MONDO:0014754"}, cache, refresh=False, workers=1, timeout=1)
        == 1
    )
    assert cache["terms"] == {}
    row = audit.ValidityRow(
        "COQ6", "HGNC:20233", "x", "MONDO:0014754", "AR", "Definitive", ""
    )
    assert audit.classify(row, cache, {}).status == audit.LOOKUP_FAILED


def test_main_is_report_only_unless_strict(tmp_path, capsys):
    csv_path = _csv(
        tmp_path,
        _row(
            "COQ6",
            "HGNC:20233",
            "primary coenzyme Q10 deficiency 8",
            "MONDO:0014754",
            "Definitive",
            "CGGV:assertion_x",
        ),
    )
    cache_path = tmp_path / "cache.json"
    cache_path.write_text(json.dumps(CACHE), encoding="utf-8")
    args = ["--csv", str(csv_path), "--cache", str(cache_path)]
    assert audit.main(args) == 0
    out = capsys.readouterr().out
    assert "names_another_gene (1;" in out
    assert "COQ7 (HGNC:2244)" in out
    assert audit.main([*args, "--strict"]) == 1
    capsys.readouterr()
    assert audit.main([*args, "--format", "tsv", "--findings-only"]) == 0
    tsv = capsys.readouterr().out.splitlines()
    assert tsv[0].startswith("status\tassertion")
    assert tsv[-1].startswith("names_another_gene\tCGGV:assertion_x\tCOQ6")
