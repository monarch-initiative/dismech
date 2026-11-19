"""Each edge case in the Complement-ARIE Q&A export has one parser rule, and each rule is pinned here.

``scripts/complement_arie_landscape.py`` parses a Tableau export that is UTF-16,
tab-separated, carries multi-line quoted answers, groups some papers under one
key, has abstracts that do not always line up with their row, and holds UTF-8
text read as Windows-1252, sometimes twice. These tests build a small export
with each of those shapes rather than reading the real 128 MB file, which is
not committed.
"""

import csv
import hashlib
import io
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import complement_arie_landscape as arie


def mojibake(text: str, times: int = 1) -> str:
    # Bytes cp1252 leaves undefined (0x9D in "”") survive as C1 controls, as in the export.
    def byte_to_char(b: int) -> str:
        try:
            return bytes([b]).decode("cp1252")
        except UnicodeDecodeError:
            return chr(b)

    for _ in range(times):
        text = "".join(byte_to_char(b) for b in text.encode("utf-8"))
    return text


def row(key, question, answer, *, title="A title", doi="https://doi.org/10.1/x", abstract="An abstract."):
    return [key, question, "yes", abstract, doi, f"Full wording of {question}?", title, "Yes:", answer]


def write_export(path: Path, rows: list[list[str]]) -> Path:
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    writer.writerow(arie.EXPECTED_COLUMNS)
    writer.writerows(rows)
    path.write_bytes(buffer.getvalue().encode("utf-16"))
    return path


def parse(tmp_path: Path, rows: list[list[str]]):
    export = write_export(tmp_path / "export.csv", rows)
    arie.main(["--input", str(export), "--out-dir", str(tmp_path), "--no-verify"])
    with (tmp_path / "papers.tsv").open(encoding="utf-8") as fh:
        papers = {p["citation_key"]: p for p in csv.DictReader(fh, delimiter="\t")}
    with (tmp_path / "answers.jsonl").open(encoding="utf-8") as fh:
        answers = [json.loads(line) for line in fh]
    return papers, answers


def test_multiline_answers_survive_and_crlf_is_normalised(tmp_path):
    _, answers = parse(tmp_path, [row("Smith et al. 2023 (123)", "Method Details Described", "Line one\r\n- line two")])
    assert answers[0]["answer"] == "Line one\n- line two"


def test_accessions_are_classified_and_pmid_only_set_for_pmids(tmp_path):
    papers, _ = parse(tmp_path, [
        row("Smith et al. 2023 (123)", "Q", "x"),
        row("Lee et al. 2023 (WOS000111)", "Q", "x"),
        row("Kim et al. 2022 (Scopus_42)", "Q", "x"),
        row("Ng et al. 2021 (NA)", "Q", "x", doi="https://doi.org/NA", title="NA"),
    ])
    assert papers["Smith et al. 2023 (123)"]["pmid"] == "123"
    assert papers["Lee et al. 2023 (WOS000111)"]["accession_type"] == "WOS"
    assert papers["Lee et al. 2023 (WOS000111)"]["pmid"] == ""
    assert papers["Kim et al. 2022 (Scopus_42)"]["accession_type"] == "SCOPUS"
    na = papers["Ng et al. 2021 (NA)"]
    assert (na["accession"], na["doi"], na["title"]) == ("", "", "")


def test_merged_keys_are_listed_but_their_answers_dropped(tmp_path):
    papers, answers = parse(tmp_path, [
        row("Wang et al. 2023 (NA)", "Q", "belongs to which paper?", doi="*", abstract="*", title="NA"),
        row("Smith et al. 2023 (123)", "Q", "kept"),
    ])
    assert papers["Wang et al. 2023 (NA)"]["merged_key"] == "1"
    assert [a["citation_key"] for a in answers] == ["Smith et al. 2023 (123)"]


def test_an_abstract_attached_to_two_keys_flags_both(tmp_path):
    papers, _ = parse(tmp_path, [
        row("Smith et al. 2023 (123)", "Q", "x", abstract="Same text."),
        row("Lee et al. 2023 (456)", "Q", "x", abstract="Same text."),
        row("Kim et al. 2023 (789)", "Q", "x", abstract="Own text."),
    ])
    assert papers["Smith et al. 2023 (123)"]["abstract_shared"] == "1"
    assert papers["Lee et al. 2023 (456)"]["abstract_shared"] == "1"
    assert papers["Kim et al. 2023 (789)"]["abstract_shared"] == "0"


def test_na_answers_are_marked(tmp_path):
    _, answers = parse(tmp_path, [
        row("Smith et al. 2023 (123)", "Disease(s) Examined", "NA"),
        row("Smith et al. 2023 (123)", "Tissue Types Examined", "Nasal epithelium"),
    ])
    by_question = {a["question"]: a["answer_is_na"] for a in answers}
    assert by_question == {"Disease(s) Examined": True, "Tissue Types Examined": False}


def test_pdf_page_headers_are_moved_out_of_title(tmp_path):
    papers, _ = parse(tmp_path, [
        row("Lv et al. 2023 (1)", "Q", "x",
            title="Inflammation Research (2023) 72:443-462\r\nREVIEW\r\nRole of a-synuclein in microglia"),
        row("Wang et al. 2023 (2)", "Q", "x",
            title="Wang et al. Military Medical Research (2023) 10:38 Spatial transcriptomics"),
        row("Tarum et al. 2023 (3)", "Q", "x", title="Hindawi Volume 2023 https://doi.org/10.1155/2023/9802235"),
        row("Smith et al. 2023 (4)", "Q", "x", title="Organ-on-chip models  of the gut"),
        row("Yan et al. 2023 (5)", "Q", "x", title="REVIEW ARTICLE Regenerative Endodontics by Cell Homing"),
        row("Ng et al. 2023 (6)", "Q", "x", title="Review of liver-on-chip platforms"),
        row("Pham et al. 2023 (7)", "Q", "x", title="PDMS Micropatterns Coated with PDA"),
    ])
    assert papers["Yan et al. 2023 (5)"]["title"] == ""
    assert papers["Ng et al. 2023 (6)"]["title"] == "Review of liver-on-chip platforms"
    assert papers["Pham et al. 2023 (7)"]["title"] == "PDMS Micropatterns Coated with PDA"
    lv = papers["Lv et al. 2023 (1)"]
    assert lv["title"] == ""
    assert lv["title_page_header"] == "Inflammation Research (2023) 72:443-462 REVIEW Role of a-synuclein in microglia"
    assert papers["Wang et al. 2023 (2)"]["title"] == ""
    assert papers["Tarum et al. 2023 (3)"]["title"] == ""
    smith = papers["Smith et al. 2023 (4)"]
    assert (smith["title"], smith["title_page_header"]) == ("Organ-on-chip models of the gut", "")


def test_a_listed_title_prefix_is_removed_for_that_paper_only(tmp_path):
    papers, _ = parse(tmp_path, [
        row("Barichello et al. 2018 (29648634)", "Q", "x", title="ESC Personalizing therapy for atrial fibrillation"),
        row("Other et al. 2018 (1)", "Q", "x", title="ESC Guidelines on heart failure"),
    ])
    assert papers["Barichello et al. 2018 (29648634)"]["title"] == "Personalizing therapy for atrial fibrillation"
    assert papers["Other et al. 2018 (1)"]["title"] == "ESC Guidelines on heart failure"


def test_a_title_correction_that_no_longer_matches_stops_the_run(tmp_path):
    export = write_export(tmp_path / "export.csv", [
        row("Barichello et al. 2018 (29648634)", "Q", "x", title="Personalizing therapy for atrial fibrillation"),
    ])
    with pytest.raises(SystemExit, match="TITLE_PREFIX_CORRECTIONS"):
        arie.main(["--input", str(export), "--out-dir", str(tmp_path), "--no-verify"])


def test_a_download_that_differs_from_the_manifest_pin_stops_the_run(tmp_path):
    export = write_export(tmp_path / "export.csv", [row("Smith et al. 2023 (1)", "Q", "x")])
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text("sha256: " + "0" * 64 + "\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="--no-verify"):
        arie.main(["--input", str(export), "--out-dir", str(tmp_path), "--manifest", str(manifest)])
    assert not (tmp_path / "papers.tsv").exists()


def test_a_download_matching_the_manifest_pin_is_parsed(tmp_path):
    export = write_export(tmp_path / "export.csv", [row("Smith et al. 2023 (1)", "Q", "x")])
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(f"sha256: {hashlib.sha256(export.read_bytes()).hexdigest()}\n", encoding="utf-8")
    arie.main(["--input", str(export), "--out-dir", str(tmp_path), "--manifest", str(manifest)])
    assert (tmp_path / "papers.tsv").exists()


def test_the_committed_manifest_carries_a_pin_the_script_can_read():
    text = (Path(__file__).resolve().parents[1] / "data" / "complement-arie" / "MANIFEST.yaml").read_text(encoding="utf-8")
    assert arie.MANIFEST_SHA256_RE.search(text)


def test_papers_tsv_has_one_line_per_paper(tmp_path):
    parse(tmp_path, [row("Lv et al. 2023 (1)", "Q", "x", title="Header\r\nREVIEW\r\nTitle")])
    assert len((tmp_path / "papers.tsv").read_text(encoding="utf-8").splitlines()) == 2


def test_questions_tsv_counts_answered_and_na_per_question(tmp_path):
    parse(tmp_path, [
        row("Smith et al. 2023 (1)", "Disease(s) Examined", "Yes, asthma."),
        row("Lee et al. 2023 (2)", "Disease(s) Examined", "NA"),
        row("Kim et al. 2023 (3)", "Disease(s) Examined", "Yes, gout."),
        row("Smith et al. 2023 (1)", "Tissue Types Examined", "Lung"),
        row("Wang et al. 2023 (NA)", "Tissue Types Examined", "merged", doi="*", abstract="*"),
    ])
    with (tmp_path / "questions.tsv").open(encoding="utf-8") as fh:
        questions = list(csv.DictReader(fh, delimiter="\t"))
    assert [(q["question"], q["n_answered"], q["n_na"]) for q in questions] == [
        ("Disease(s) Examined", "2", "1"),
        ("Tissue Types Examined", "1", "0"),
    ]
    assert questions[0]["question_full"] == "Full wording of Disease(s) Examined?"


def test_a_paper_with_only_na_answers_is_flagged_no_content(tmp_path):
    papers, _ = parse(tmp_path, [
        row("Ng et al. 2023 (NA)", "Disease(s) Examined", "NA"),
        row("Ng et al. 2023 (NA)", "Tissue Types Examined", "NA"),
        row("Smith et al. 2023 (1)", "Disease(s) Examined", "NA"),
        row("Smith et al. 2023 (1)", "Tissue Types Examined", "Lung"),
        row("Wang et al. 2023 (NA)", "Tissue Types Examined", "NA", doi="*", abstract="*"),
    ])
    assert papers["Ng et al. 2023 (NA)"]["no_content"] == "1"
    assert papers["Smith et al. 2023 (1)"]["no_content"] == "0"
    assert papers["Wang et al. 2023 (NA)"]["no_content"] == "0"  # merged: answers dropped, not judged


def test_trailing_whitespace_in_a_key_is_stripped(tmp_path):
    papers, _ = parse(tmp_path, [row("André et al. 2022 (36225354) ", "Q", "x")])
    assert "André et al. 2022 (36225354)" in papers


def test_single_and_double_mojibake_is_repaired():
    assert arie.repair_mojibake(mojibake("naïve CD4+ T cells")) == "naïve CD4+ T cells"
    assert arie.repair_mojibake(mojibake("Müller and Gómez", times=2)) == "Müller and Gómez"
    assert arie.repair_mojibake(mojibake("“quoted”")) == "“quoted”"


def test_clean_text_is_left_alone():
    for text in ("naïve", "37 °C", "TNF-α → NF-κB", "Straße", "®"):
        assert arie.repair_mojibake(text) == text


def test_a_genuine_character_does_not_block_repair_of_its_neighbours():
    damaged = mojibake("é") + "α" + mojibake("ü")
    assert arie.repair_mojibake(damaged) == "éαü"
