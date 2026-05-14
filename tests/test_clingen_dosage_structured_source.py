"""Tests for the ClinGen Dosage Sensitivity structured-database source."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.clingen_dosage import (
    ClinGenDosageSource,
    _ClinGenDosageReportDetails,
    _DosageEvidence,
    _parse_report_details,
)


CSV_TEXT = """"CLINGEN DOSAGE SENSITIVITY CURATIONS","","","","",""
"FILE CREATED: 2026-05-09","","","","",""
"WEBPAGE: https://search.clinicalgenome.org/kb/gene-dosage","","","","",""
"+++++++++++","+++++++","++++++++++++++++++","+++++++++++++++++","+++++++++++++","++++"
"GENE SYMBOL","HGNC ID","HAPLOINSUFFICIENCY","TRIPLOSENSITIVITY","ONLINE REPORT","DATE"
"+++++++++++","+++++++","++++++++++++++++++","+++++++++++++++++","+++++++++++++","++++"
"AAGAB","HGNC:25662","Sufficient Evidence for Haploinsufficiency","No Evidence for Triplosensitivity","https://search.clinicalgenome.org/kb/gene-dosage/HGNC:25662","2013-02-28T20:17:25+00:00"
"PTCH1","HGNC:9585","Sufficient Evidence for Haploinsufficiency","No Evidence for Triplosensitivity","https://search.clinicalgenome.org/kb/gene-dosage/HGNC:9585","2020-07-01T13:25:00+00:00"
"""


TSV_HEADER = [
    "Gene Symbol",
    "Gene ID",
    "cytoBand",
    "Genomic Location",
    "Haploinsufficiency Score",
    "Haploinsufficiency Description",
    "Haploinsufficiency PMID1",
    "Haploinsufficiency PMID2",
    "Haploinsufficiency PMID3",
    "Haploinsufficiency PMID4",
    "Haploinsufficiency PMID5",
    "Haploinsufficiency PMID6",
    "Triplosensitivity Score",
    "Triplosensitivity Description",
    "Triplosensitivity PMID1",
    "Triplosensitivity PMID2",
    "Triplosensitivity PMID3",
    "Triplosensitivity PMID4",
    "Triplosensitivity PMID5",
    "Triplosensitivity PMID6",
    "Date Last Evaluated",
    "Haploinsufficiency Disease ID",
    "Triplosensitivity Disease ID",
]


TSV_ROWS = [
    [
        "AAGAB",
        "79719",
        "15q23",
        "chr15:67200667-67255198",
        "3",
        "Sufficient evidence for dosage pathogenicity",
        "23064416",
        "23000146",
        "",
        "",
        "",
        "",
        "0",
        "No evidence available",
        "",
        "",
        "",
        "",
        "",
        "",
        "2013-02-28",
        "MONDO:0007858",
        "",
    ],
    [
        "PTCH1",
        "5727",
        "9q22.32",
        "chr9:95442980-95516971",
        "3",
        "Sufficient evidence for dosage pathogenicity",
        "30411536",
        "",
        "",
        "",
        "",
        "",
        "0",
        "No evidence available",
        "18830227",
        "",
        "",
        "",
        "",
        "",
        "2020-07-01",
        "MONDO:0007187",
        "",
    ],
]


TSV_TEXT = "\n".join(
    [
        "#ClinGen Gene Curation Results",
        "#08 May,2026",
        "#Genomic Locations are reported on GRCh38 (hg38): GCF_000001405.36",
        "\t".join([f"#{TSV_HEADER[0]}", *TSV_HEADER[1:]]),
        *("\t".join(row) for row in TSV_ROWS),
        "",
    ]
)


AAGAB_ID = "CGDS:HGNC_25662"


@pytest.fixture()
def dosage_source(tmp_path: Path) -> ClinGenDosageSource:
    (tmp_path / "gene_dosage.csv").write_text(CSV_TEXT, encoding="utf-8")
    (tmp_path / "gene_dosage_grch38.tsv").write_text(TSV_TEXT, encoding="utf-8")
    src = ClinGenDosageSource(tmp_path, include_report_text=False)
    src.index()
    return src


def test_index_pairs_csv_hgnc_with_tsv_evidence(dosage_source: ClinGenDosageSource):
    idx = dosage_source.index()
    assert len(idx) == 2
    assert idx[AAGAB_ID].gene_symbol == "AAGAB"
    assert idx[AAGAB_ID].hgnc_id == "HGNC:25662"
    assert idx[AAGAB_ID].entrez_id == "79719"
    assert idx[AAGAB_ID].haplo_disease_id == "MONDO:0007858"
    assert idx[AAGAB_ID].haplo_pmids == ("23064416", "23000146")
    assert dosage_source.snapshot_date == "2026-05-09"


def test_serialize_dosage_record_has_expected_blocks(
    dosage_source: ClinGenDosageSource,
):
    text = dosage_source.serialize(AAGAB_ID).render()
    assert f'reference_id: "{AAGAB_ID}"' in text
    assert 'title: "AAGAB dosage sensitivity"' in text
    assert 'database: "ClinGen"' in text
    assert 'content_type: "structured_record"' in text

    assert f"# {AAGAB_ID}  AAGAB dosage sensitivity" in text
    assert "## Dosage sensitivity summary" in text
    assert "| Gene | HGNC | Entrez | Cytoband | GRCh38 |" in text
    assert (
        "| AAGAB | HGNC:25662 | 79719 | 15q23 | chr15:67200667-67255198 | "
        "3 - Sufficient Evidence for Haploinsufficiency | "
        "0 - No Evidence for Triplosensitivity | 2013-02-28 |"
    ) in text
    assert "- Scored description: Sufficient evidence for dosage pathogenicity" in text
    assert "- Disease ID: MONDO:0007858" in text
    assert "- PMIDs: PMID:23064416, PMID:23000146" in text
    assert (
        "- Report URL: https://search.clinicalgenome.org/kb/gene-dosage/HGNC:25662"
        in text
    )
    assert "ClinGen Dosage Sensitivity gene download and curated gene list" in text


def test_serialize_can_include_dosage_report_text(tmp_path: Path):
    (tmp_path / "gene_dosage.csv").write_text(CSV_TEXT, encoding="utf-8")
    (tmp_path / "gene_dosage_grch38.tsv").write_text(TSV_TEXT, encoding="utf-8")
    src = ClinGenDosageSource(tmp_path)
    src._report_cache[AAGAB_ID] = _ClinGenDosageReportDetails(
        dosage_id="ISCA-16608",
        curation_id="CCID:006592",
        haplo_disease=("palmoplantar keratoderma, punctate type 1A",),
        haplo_evidence=(
            _DosageEvidence(
                pmid="23064416",
                summary="Families with autosomal dominant disease had loss of function mutations.",
            ),
        ),
        haplo_comments=(
            "This disorder is associated with haploinsufficiency of AAGAB.",
        ),
        triplo_comments=(
            "No focal duplications were found at the time of this review.",
        ),
    )

    text = src.serialize(AAGAB_ID).render()
    assert "## Haploinsufficiency report text" in text
    assert (
        "PMID:23064416: Families with autosomal dominant disease had loss of "
        "function mutations."
    ) in text
    assert (
        "Evidence comments: This disorder is associated with haploinsufficiency" in text
    )
    assert "No focal duplications were found at the time of this review." in text
    assert "- Dosage ID: ISCA-16608" in text
    assert "- Curation ID: CCID:006592" in text


def test_parse_report_details_extracts_evidence_comments():
    html = """
    <html><body>
      <div>Dosage ID: ISCA-16608</div>
      <div>ClinGen Curation ID: CCID:006592</div>
      <div id="report_details_haploinsufficiency">
        <div class="row">
          <div>HI Disease:</div>
          <div><ul><li>palmoplantar keratoderma <a>Monarch</a></li></ul></div>
        </div>
        <div class="row">
          <div>HI Evidence:</div>
          <div>
            <ul>
              <li>
                <a>PUBMED: 23064416</a>
                <div class="summariesShow">Loss of function variants segregated.</div>
              </li>
            </ul>
          </div>
        </div>
        <div class="row">
          <div>HI Evidence Comments:</div>
          <div><span class="data_pre">Associated with haploinsufficiency.</span></div>
        </div>
      </div>
      <div id="report_details_triplosensitivity">
        <div class="row">
          <div>TS Evidence Comments:</div>
          <div><span>No focal duplications were found.</span></div>
        </div>
      </div>
    </body></html>
    """
    details = _parse_report_details(html)
    assert details.dosage_id == "ISCA-16608"
    assert details.curation_id == "CCID:006592"
    assert details.haplo_disease == ("palmoplantar keratoderma",)
    assert details.haplo_evidence == (
        _DosageEvidence("23064416", "Loss of function variants segregated."),
    )
    assert details.haplo_comments == ("Associated with haploinsufficiency.",)
    assert details.triplo_comments == ("No focal duplications were found.",)


def test_cache_file_passes_frontmatter_contract(
    dosage_source: ClinGenDosageSource, tmp_path: Path
):
    path = dosage_source.write_cache_file(AAGAB_ID, tmp_path)
    assert check_cache_file(path) is None


@pytest.mark.parametrize(
    "identifier",
    [
        AAGAB_ID,
        "HGNC:25662",
        "HGNC_25662",
        "CLINGEN-DOSAGE:HGNC:25662",
        "https://search.clinicalgenome.org/kb/gene-dosage/HGNC:25662",
    ],
)
def test_serialize_accepts_native_bare_and_url_identifiers(
    dosage_source: ClinGenDosageSource, identifier: str
):
    entry = dosage_source.serialize(identifier)
    assert entry.reference_id == AAGAB_ID
    assert entry.title == "AAGAB dosage sensitivity"
