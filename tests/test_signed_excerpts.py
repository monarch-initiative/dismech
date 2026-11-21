"""Structural and cryptographic integrity checks for ``signed_excerpts/*.yaml``.

Files in ``signed_excerpts/`` are synced exclusively from the private
``monarch-initiative/claimstore`` repository, where full-text PDFs and extracted
Markdowns are validated with ``linkml-reference-validator`` and
``linkml-term-validator``. Because ``linkml-reference-validator`` treats an
exact match in ``signed_excerpts/`` as verified without requiring the quote to
appear in ``references_cache/``, every committed bundle must carry complete
provenance metadata, SHA-256 digests, and fair-use length bounds.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml
from linkml_reference_validator.matching import split_supporting_text

from dismech.reference_cache_names import cache_stems

ROOT = Path(__file__).resolve().parents[1]
SIGNED_EXCERPTS_DIR = ROOT / "signed_excerpts"
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")

# Fair-use bounds enforced by claimstore/.linkml-reference-validator.yaml
MAX_PART_CHARS = 250
MAX_EXCERPT_CHARS = 450
MAX_TOTAL_CHARS_PER_REF = 1500
MAX_REF_FRACTION = 0.05


def test_signed_excerpts_bundles_have_valid_provenance_and_fair_use_bounds() -> None:
    """Every committed signed_excerpts/*.yaml file must satisfy claimstore provenance invariants."""
    assert SIGNED_EXCERPTS_DIR.is_dir(), "signed_excerpts/ directory is missing"
    files = sorted(SIGNED_EXCERPTS_DIR.glob("*.yaml"))
    assert files, "signed_excerpts/ must contain at least one synced bundle"

    for path in files:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert isinstance(data, dict), f"{path.name}: top-level YAML must be a mapping"

        ref_id = data.get("reference_id")
        assert isinstance(ref_id, str) and ref_id.strip(), (
            f"{path.name}: missing reference_id"
        )
        expected_stems = {stem.casefold() for stem in cache_stems(ref_id)}
        assert path.stem.casefold() in expected_stems, (
            f"{path.name}: stem {path.stem!r} does not match reference_id {ref_id!r}"
        )

        title = data.get("title")
        assert isinstance(title, str) and title.strip(), f"{path.name}: missing title"

        content_type = data.get("source_content_type")
        assert content_type in {"full_text_pdf", "full_text_xml"}, (
            f"{path.name}: unexpected source_content_type {content_type!r}"
        )

        source_chars = data.get("source_char_count")
        assert isinstance(source_chars, int) and source_chars > 0, (
            f"{path.name}: source_char_count must be a positive int, got {source_chars!r}"
        )

        for sha_field in ("source_md_sha256", "source_pdf_sha256"):
            digest = data.get(sha_field)
            assert isinstance(digest, str) and HEX64_RE.match(digest), (
                f"{path.name}: {sha_field} must be a 64-char lowercase hex SHA-256 digest"
            )

        excerpts = data.get("excerpts")
        assert isinstance(excerpts, list) and excerpts, (
            f"{path.name}: excerpts must be a non-empty list"
        )

        total_chars = 0
        for idx, excerpt in enumerate(excerpts):
            loc = f"{path.name}#excerpts[{idx}]"
            assert isinstance(excerpt, dict), f"{loc}: excerpt must be a mapping"

            text = excerpt.get("text")
            assert isinstance(text, str) and text.strip(), f"{loc}: missing text"
            stripped = text.strip()
            assert not stripped[0].islower(), (
                f"{loc}: excerpt must begin on a complete sentence/clause, not lowercase {stripped[:30]!r}"
            )

            parts = split_supporting_text(text)
            assert parts, f"{loc}: excerpt has no quotable parts"

            part_lengths = [len("".join(part.split())) for part in parts]
            for part_idx, part_len in enumerate(part_lengths):
                assert part_len <= MAX_PART_CHARS, (
                    f"{loc} part {part_idx}: {part_len} non-whitespace chars exceeds {MAX_PART_CHARS}"
                )

            computed_chars = sum(part_lengths)
            assert computed_chars <= MAX_EXCERPT_CHARS, (
                f"{loc}: {computed_chars} non-whitespace chars exceeds {MAX_EXCERPT_CHARS}"
            )
            assert excerpt.get("char_count") == computed_chars, (
                f"{loc}: char_count {excerpt.get('char_count')!r} != computed {computed_chars}"
            )

            norm_ws = " ".join(text.split())
            expected_sha = hashlib.sha256(norm_ws.encode("utf-8")).hexdigest()
            assert excerpt.get("sha256") == expected_sha, (
                f"{loc}: sha256 {excerpt.get('sha256')!r} != expected {expected_sha}"
            )

            verified_at = excerpt.get("verified_at")
            assert isinstance(verified_at, str) and verified_at.strip(), (
                f"{loc}: missing verified_at timestamp"
            )

            total_chars += computed_chars

        assert total_chars <= MAX_TOTAL_CHARS_PER_REF, (
            f"{path.name}: total excerpt chars {total_chars} exceeds {MAX_TOTAL_CHARS_PER_REF}"
        )
        assert total_chars / source_chars <= MAX_REF_FRACTION, (
            f"{path.name}: excerpt fraction {total_chars / source_chars:.4f} exceeds {MAX_REF_FRACTION}"
        )
