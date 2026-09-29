"""Fail-closed reconciliation of generated CSV conflicts without losing rows."""

import csv
import importlib.util
import io
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "generated_cache_merge", ROOT / "scripts/generated_cache_merge.py"
)
merge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(merge)

HEADER = b"curie,label,retrieved_at\n"
ENUM_HEADER = b"curie\n"
STAMP = "2026-09-16T12:34:56.123456"
HP = "cache/hp/terms.csv"
ENUM = "cache/enums/phenotypeterm_abc123.csv"


def term(curie, label, stamp=STAMP):
    stream = io.StringIO(newline="")
    csv.writer(stream, lineterminator="\r\n").writerow([curie, label, stamp])
    return stream.getvalue().encode("utf-8")


A = term("HP:0000001", "first")
B = term("HP:0000002", "second")
C = term("HP:0000003", "third")


def read(blob):
    return list(csv.reader(io.StringIO(blob.decode(), newline=""), strict=True))


def test_additions_from_both_sides_preserve_every_field_and_sort():
    base = HEADER + A
    ours = HEADER + C + A
    theirs = HEADER + A + B
    result = merge.merge_cache_csv(HP, base, ours, theirs)
    assert read(result) == read(HEADER + A + B + C)
    assert result == (HEADER + A + B + C).replace(b"\r\n", b"\n")
    assert merge.merge_cache_csv(HP, base, theirs, ours) == result
    assert merge.merge_cache_csv(HP, result, result, result) == result


def test_add_add_conflict_with_no_ancestor():
    assert read(merge.merge_cache_csv(HP, None, HEADER + B, HEADER + A)) == read(
        HEADER + A + B
    )


def test_identical_addition_on_both_sides_is_retained_once():
    assert read(
        merge.merge_cache_csv(HP, HEADER + A, HEADER + A + B, HEADER + A + B)
    ) == read(HEADER + A + B)


def test_empty_but_headered_caches_are_valid():
    assert merge.merge_cache_csv(HP, HEADER, HEADER, HEADER) == HEADER
    assert merge.merge_cache_csv(ENUM, None, ENUM_HEADER, ENUM_HEADER) == ENUM_HEADER


def test_enum_union_keeps_mixed_prefixes_in_codepoint_order():
    base = ENUM_HEADER + b"HP:0000001\n"
    ours = base + b"hgnc:10\n"
    theirs = ENUM_HEADER + b"MONDO:0010001\nHP:0000001\n"
    assert merge.merge_cache_csv(ENUM, base, ours, theirs) == (
        ENUM_HEADER + b"HP:0000001\nMONDO:0010001\nhgnc:10\n"
    )


@pytest.mark.parametrize("ours,theirs", [(HEADER, HEADER + A), (HEADER, HEADER)])
def test_deletion_is_never_resurrected_by_union(ours, theirs):
    with pytest.raises(merge.UnsafeMerge, match="deleted ancestor"):
        merge.merge_cache_csv(HP, HEADER + A, ours, theirs)
    with pytest.raises(merge.UnsafeMerge, match="deleted ancestor"):
        merge.merge_cache_csv(HP, HEADER + A, theirs, ours)


def test_enum_deletion_is_also_refused():
    with pytest.raises(merge.UnsafeMerge, match="deleted ancestor"):
        merge.merge_cache_csv(ENUM, ENUM_HEADER + b"HP:1\n", ENUM_HEADER, ENUM_HEADER)


@pytest.mark.parametrize(
    "changed",
    [
        term("HP:0000001", "corrected label"),
        term("HP:0000001", "first", "2026-09-17T12:34:56.123456"),
        term("hp:0000001", "first"),
    ],
)
def test_existing_edits_are_refused_even_when_both_tips_agree(changed):
    for other in (A, changed):
        with pytest.raises(merge.UnsafeMerge, match="changed ancestor"):
            merge.merge_cache_csv(HP, HEADER + A, HEADER + changed, HEADER + other)


@pytest.mark.parametrize(
    "changed",
    [
        term("HP:0000002", "different label"),
        term("HP:0000002", "second", "2026-09-17T12:34:56.123456"),
        term("hp:0000002", "second"),
    ],
)
def test_competing_additions_never_choose_a_winner(changed):
    with pytest.raises(merge.UnsafeMerge, match="competing rows"):
        merge.merge_cache_csv(HP, HEADER + A, HEADER + A + B, HEADER + A + changed)


def test_enum_case_collision_across_tips_is_refused():
    with pytest.raises(merge.UnsafeMerge, match="competing rows"):
        merge.merge_cache_csv(
            ENUM, ENUM_HEADER, ENUM_HEADER + b"hgnc:10\n", ENUM_HEADER + b"HGNC:10\n"
        )


@pytest.mark.parametrize(
    "label", ["a, b", 'a "quoted" label', "β-cell", "a\nb", "a\rb", "a\r\nb"]
)
def test_csv_quoting_and_unicode_preserve_labels_exactly(label):
    unusual = term("HP:0000002", label)
    result = merge.merge_cache_csv(HP, HEADER + A, HEADER + A + unusual, HEADER + A + C)
    assert read(result) == read(HEADER + A + unusual + C)


def test_valid_alternative_quoting_is_semantically_identical():
    quoted = f'"HP:0000001","first","{STAMP}"'.encode()
    result = merge.merge_cache_csv(HP, HEADER + A, HEADER + quoted, HEADER + A)
    assert read(result) == read(HEADER + A)


@pytest.mark.parametrize(
    "bad",
    [
        b"",
        b"curie,label\n" + A,
        b"label,curie,retrieved_at\n" + A,
        b"curie,label,retrieved_at,extra\n" + A,
        b"\xef\xbb\xbf" + HEADER + A,
        HEADER + A + b"\n",
        HEADER + A + A,
        HEADER + A + term("hp:0000001", "first"),
        HEADER + term("GO:1", "wrong prefix"),
        HEADER + term("HP:1:2", "bad CURIE"),
        HEADER + term("HP:1\n", "newline in CURIE"),
        HEADER + term(" HP:1", "space in CURIE"),
        HEADER + term("HP:1", ""),
        HEADER + term("HP:1", " \t "),
        HEADER + term("HP:1", "label", ""),
        HEADER + term("HP:1", "label", "2026-09-16"),
        HEADER + term("HP:1", "label", "2026-99-16T12:34:56"),
        HEADER + b"HP:1,unquoted,comma," + STAMP.encode() + b"\n",
        HEADER + b'HP:1,bare"quote,' + STAMP.encode() + b"\n",
        HEADER + b'HP:1,"unclosed,' + STAMP.encode() + b"\n",
        HEADER + b'HP:1,"closed"junk,' + STAMP.encode() + b"\n",
        HEADER + term("HP:1", "nul\x00byte"),
        HEADER + b"HP:1,\xff," + STAMP.encode() + b"\n",
        HEADER + b"<<<<<<< HEAD\n" + A + b"=======\n" + B + b">>>>>>> main\n",
    ],
)
@pytest.mark.parametrize("side", ["base", "ours", "theirs"])
def test_every_blob_must_be_valid_even_if_unchanged_or_shared(bad, side):
    blobs = {"base": HEADER, "ours": HEADER, "theirs": HEADER}
    blobs[side] = bad
    with pytest.raises(merge.UnsafeMerge):
        merge.merge_cache_csv(HP, **blobs)


@pytest.mark.parametrize(
    "bad",
    [
        b"id\nHP:1\n",
        ENUM_HEADER + b"HP:1,label\n",
        ENUM_HEADER + b"HP:1\nHP:1\n",
        ENUM_HEADER + b"hgnc:10\nHGNC:10\n",
        ENUM_HEADER + b"HP:1:2\n",
        ENUM_HEADER + b'"HP:1\n"\n',
    ],
)
def test_malformed_enum_input_is_refused(bad):
    with pytest.raises(merge.UnsafeMerge):
        merge.merge_cache_csv(ENUM, ENUM_HEADER, bad, ENUM_HEADER)


@pytest.mark.parametrize(
    "path",
    [
        "cache/legacy.json",
        "cache/hp/hierarchy.csv",
        "cache/hp/other.csv",
        "references_cache/PMID_1.md",
        "pages/generated.html",
        "src/dismech/schema/dismech.yaml",
        "/cache/hp/terms.csv",
        "./cache/hp/terms.csv",
        "cache/../terms.csv",
        "cache/hp/../hp/terms.csv",
        "cache//hp/terms.csv",
        "cache/enums/nested/foo.csv",
        "cache/enums/../hp/terms.csv",
        "cache/enums/foo.csv\n",
        "cache/enums/foo.csv\x00",
        "cache\\hp\\terms.csv",
    ],
)
def test_unsupported_paths_are_refused_before_parsing(path):
    assert not merge.is_supported_cache_path(path)
    with pytest.raises(merge.UnsafeMerge, match="unsupported cache path"):
        merge.merge_cache_csv(path, None, b"", b"")


def test_enum_named_terms_is_still_single_column():
    path = "cache/enums/terms.csv"
    assert merge.merge_cache_csv(path, None, ENUM_HEADER, ENUM_HEADER) == ENUM_HEADER
    with pytest.raises(merge.UnsafeMerge):
        merge.merge_cache_csv(path, None, HEADER, HEADER)


@pytest.mark.parametrize(
    "prefix,curie", [("ncbitaxon", "NCBITaxon:9606"), ("hgnc", "hgnc:746")]
)
def test_actual_mixed_case_prefixes_are_supported(prefix, curie):
    row = term(curie, "label")
    result = merge.merge_cache_csv(
        f"cache/{prefix}/terms.csv", None, HEADER + row, HEADER
    )
    assert read(result) == read(HEADER + row)
