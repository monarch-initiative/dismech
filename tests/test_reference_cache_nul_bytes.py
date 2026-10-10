"""Guard and repair tests for NUL bytes in references_cache/ (#12543).

See scripts/check_reference_cache_nul_bytes.py for why a NUL makes grep drop a
file, and scripts/repair_reference_cache_nuls.py for where the NULs come from.
"""
from collections import Counter

from scripts.check_reference_cache_nul_bytes import CACHE_DIR, nul_counts
from scripts.repair_reference_cache_nuls import REPLACEMENT, repair_text

VOCAB = Counter(
    {
        "inflammation": 5000,
        "infiammation": 3,  # OCR junk is attested too; dominance must still win
        "significant": 8000,
        "efficacy": 900,
        "eficacy": 4,
        "first": 9000,
        "five": 700,
        "with": 50000,
    }
)


def test_no_nul_bytes_in_reference_cache():
    found = nul_counts()
    assert not found, "\n".join(
        f"{path.relative_to(CACHE_DIR.parent)}: {count}" for path, count in found.items()
    )


def test_finds_nul_bytes(tmp_path):
    (tmp_path / "PMID_1.md").write_bytes(b"In\x00ammation")
    (tmp_path / "PMID_2.md").write_bytes(b"clean text")
    assert nul_counts(tmp_path) == {tmp_path / "PMID_1.md": 1}


def test_restores_ligatures_the_corpus_attests():
    text, restored, replaced = repair_text(
        "Institute of In\x00ammation; signi\x00cant e\x00cacy; the \x00rst \x00ve", VOCAB
    )
    assert text == "Institute of Inflammation; significant efficacy; the first five"
    assert (restored, replaced) == (5, 0)


def test_run_together_words_use_the_letters_around_the_nul():
    text, restored, _ = repair_text("known withsigni\x00cant residual", VOCAB)
    assert text == "known withsignificant residual"
    assert restored == 1


def test_unrecoverable_nuls_become_the_replacement_character():
    # A digit in a reference number, a minus sign, and a one-letter fragment
    # ("\0n diameter" lost an "i", not a ligature) are not guessed at.
    text, restored, replaced = repair_text("1\x00. Zaidi; 1 \x00 P; 100 nm \x00n diameter", VOCAB)
    assert text == f"1{REPLACEMENT}. Zaidi; 1 {REPLACEMENT} P; 100 nm {REPLACEMENT}n diameter"
    assert (restored, replaced) == (0, 3)


def test_a_lost_separator_is_not_read_as_a_ligature():
    # "history\0n (%)": the NUL is a column separator; one letter on the right
    # is too little to support a reading.
    text, restored, _ = repair_text("Smoking history\x00n (%)", VOCAB)
    assert text == f"Smoking history{REPLACEMENT}n (%)"
    assert restored == 0
