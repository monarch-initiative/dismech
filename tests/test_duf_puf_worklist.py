from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dismech.dufmech.worklist import (
    FALSE_POSITIVE_TEXT_HIT,
    KNOWN_HISTORICAL_DUF,
    UNKNOWN_CANDIDATE,
    InterProPfamClient,
    collect_worklist,
    load_interpro_fixture,
    render_json,
    render_tsv,
    row_from_interpro_entry,
)
from scripts import duf_puf_worklist


def interpro_result(
    *,
    accession: str = "PF01519",
    short_name: str = "DUF16",
    name: str = "Protein of unknown function DUF16",
    description: str = (
        "<p>The function of this protein is unknown. "
        "It appears to only occur in Mycoplasma pneumoniae.</p>"
    ),
    integrated: str = "IPR002862",
    proteins: int = 26,
) -> dict:
    return {
        "metadata": {
            "accession": accession,
            "name": name,
            "source_database": "pfam",
            "type": "coiled_coil",
            "integrated": integrated,
        },
        "extra_fields": {
            "entry_id": None,
            "short_name": short_name,
            "description": [{"text": description}],
            "counters": {
                "domain_architectures": 2,
                "matches": 28,
                "proteins": proteins,
                "proteomes": 1,
                "structural_models": {"alphafold": 26},
                "structures": 1,
                "taxa": 10,
            },
        },
    }


def test_row_from_interpro_entry_normalizes_duf_metadata() -> None:
    row = row_from_interpro_entry(interpro_result())

    assert row is not None
    assert row.pfam_id == "PF01519"
    assert row.short_name == "DUF16"
    assert row.interpro_id == "IPR002862"
    assert row.proteins == 26
    assert row.matches == 28
    assert row.alphafold_models == 26
    assert row.structures == 1
    assert row.unknown_status == UNKNOWN_CANDIDATE
    assert row.candidate_reasons == (
        "short_name_matches_duf",
        "name_says_unknown_function",
        "description_says_unknown_function",
    )
    assert row.description == (
        "The function of this protein is unknown. "
        "It appears to only occur in Mycoplasma pneumoniae."
    )
    assert row.source_url.endswith("/PF01519")


def test_historical_duf_names_are_kept_but_demoted() -> None:
    row = row_from_interpro_entry(
        interpro_result(
            accession="PF01784",
            short_name="DUF34",
            name="NIF3 family protein",
            description="<p>Members of this family bind metal cofactors.</p>",
        )
    )

    assert row is not None
    assert row.unknown_status == KNOWN_HISTORICAL_DUF
    assert row.candidate_reasons == ("short_name_matches_duf",)


def test_domain_descriptions_can_mark_unknown_function() -> None:
    row = row_from_interpro_entry(
        interpro_result(
            accession="PF01629",
            short_name="DUF22",
            name="Uncharacterized DUF22 family",
            description="<p>The function of the domain is unknown.</p>",
        )
    )

    assert row is not None
    assert row.unknown_status == UNKNOWN_CANDIDATE
    assert "description_says_unknown_function" in row.candidate_reasons


def test_false_positive_text_hits_are_dropped_by_default() -> None:
    false_positive = interpro_result(
        accession="PF99999",
        short_name="Duffy_bind",
        name="Duffy binding domain",
        description="<p>Not a domain of the unknown-function class.</p>",
    )

    assert row_from_interpro_entry(false_positive).unknown_status == (
        FALSE_POSITIVE_TEXT_HIT
    )
    assert collect_worklist([false_positive]) == []
    assert collect_worklist([false_positive], include_false_positives=True)[
        0
    ].unknown_status == FALSE_POSITIVE_TEXT_HIT


def test_interpro_client_follows_pagination() -> None:
    first = {
        "next": "https://www.ebi.ac.uk/interpro/api/entry/pfam/?cursor=next",
        "results": [interpro_result(accession="PF01519")],
    }
    second = {
        "next": None,
        "results": [interpro_result(accession="PF01579", short_name="DUF19")],
    }

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.params.get("cursor") == "next":
            return httpx.Response(200, json=second)
        assert request.url.params["search"] == "DUF"
        assert request.url.params["page_size"] == "200"
        assert "counters" in request.url.params["extra_fields"]
        return httpx.Response(200, json=first)

    client = InterProPfamClient(transport=httpx.MockTransport(handler))

    rows = collect_worklist(client.iter_entries())

    assert [row.pfam_id for row in rows] == ["PF01519", "PF01579"]


def test_render_tsv_and_json_are_stable() -> None:
    rows = collect_worklist(
        [
            interpro_result(accession="PF01579", proteins=5),
            interpro_result(accession="PF01519", proteins=26),
        ]
    )

    tsv = render_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["pfam_id"] for row in parsed] == ["PF01519", "PF01579"]
    assert parsed[0]["candidate_reasons"] == (
        "short_name_matches_duf;"
        "name_says_unknown_function;"
        "description_says_unknown_function"
    )

    payload = json.loads(render_json(rows))
    assert payload[0]["source_url"].endswith("/PF01519")


def test_cli_reads_saved_interpro_page(tmp_path, capsys) -> None:
    page = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [interpro_result(accession="PF01519")],
    }
    path = tmp_path / "interpro.json"
    path.write_text(json.dumps(page), encoding="utf-8")

    assert (
        duf_puf_worklist.main(
            ["--input-json", str(path), "--format", "json", "--limit", "1"]
        )
        == 0
    )

    payload = json.loads(capsys.readouterr().out)
    assert payload[0]["pfam_id"] == "PF01519"


def test_load_interpro_fixture_accepts_page_lists() -> None:
    fixture = [{"results": [interpro_result()]}, {"results": [interpro_result()]}]

    assert len(load_interpro_fixture(fixture)) == 2
