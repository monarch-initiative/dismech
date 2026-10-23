"""Orphanet must say what to run when its bulk data is missing or has drifted.

On a fresh checkout ``data/orphadata/`` holds only ``MANIFEST.yaml``, and
``just fetch-reference ORPHA:<id>`` used to end in a raw ``FileNotFoundError``
from ``ET.parse`` (dismech#13941). Two quieter failures sat behind that one:

- ``refresh`` stopped at the first drifted checksum, so with a stale pin only
  ``en_product1.xml`` reached disk, and the four other loaders skipped their
  missing files without a word. The rebuilt record lost its phenotype, gene,
  prevalence and inheritance sections and the command exited 0.
- The ``## Source`` footer stamped the manifest's ``snapshot_date`` whatever
  file was actually parsed (dismech#10798).

These tests use small inline fixtures, so they run without the bulk download.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest
from typer.testing import CliRunner

from dismech.structured_sources import cli
from dismech.structured_sources.base import BulkFile, MissingBulkDataError
from dismech.structured_sources.orphanet import _PRODUCT_FILES, OrphanetSource

PRODUCT1_XML = """<?xml version="1.0" encoding="UTF-8"?>
<JDBOR date="2026-06-23 07:53:50" version="test">
  <DisorderList count="1">
    <Disorder id="1">
      <OrphaCode>558</OrphaCode>
      <Name lang="en">Marfan syndrome</Name>
      <DisorderType><Name lang="en">Disease</Name></DisorderType>
      <DisorderGroup><Name lang="en">Disorder</Name></DisorderGroup>
    </Disorder>
  </DisorderList>
</JDBOR>
"""
EMPTY_PRODUCT_XML = '<?xml version="1.0" encoding="UTF-8"?>\n<JDBOR/>\n'


def _write_products(data_dir: Path, names=_PRODUCT_FILES) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    for name in names:
        text = PRODUCT1_XML if name == "en_product1.xml" else EMPTY_PRODUCT_XML
        (data_dir / name).write_text(text, encoding="utf-8")


def _pins(data_dir: Path, *, stale: bool) -> tuple[BulkFile, ...]:
    return tuple(
        BulkFile(
            name=name,
            url=f"https://example.invalid/{name}",
            sha256=(
                "0" * 64
                if stale
                else hashlib.sha256((data_dir / name).read_bytes()).hexdigest()
            ),
        )
        for name in _PRODUCT_FILES
    )


def test_product1_alone_is_refused_with_the_remedy(tmp_path: Path):
    """A partial set must not build records with whole sections silently gone."""
    _write_products(tmp_path, names=("en_product1.xml",))

    with pytest.raises(MissingBulkDataError) as excinfo:
        OrphanetSource(tmp_path).index()

    assert excinfo.value.missing == [
        n for n in _PRODUCT_FILES if n != "en_product1.xml"
    ]
    assert "just refresh-orphadata" in str(excinfo.value)


def test_empty_data_dir_names_every_product(tmp_path: Path):
    with pytest.raises(MissingBulkDataError) as excinfo:
        OrphanetSource(tmp_path).index()

    assert excinfo.value.missing == list(_PRODUCT_FILES)
    # Still a FileNotFoundError, so callers that already catch one keep working.
    assert isinstance(excinfo.value, FileNotFoundError)


def test_cli_rebuild_prints_the_remedy_instead_of_a_traceback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setattr(cli, "_data_dir", lambda: tmp_path)

    result = CliRunner().invoke(
        cli.app,
        [
            "rebuild",
            "orphanet",
            "--id",
            "ORPHA:558",
            "--cache-dir",
            str(tmp_path / "out"),
        ],
    )

    assert result.exit_code == 1
    assert "just refresh-orphadata" in result.output
    # A clean exit, not an uncaught FileNotFoundError.
    assert isinstance(result.exception, SystemExit)
    assert not (tmp_path / "out" / "ORPHA_558.md").exists()


def test_snapshot_uses_the_manifest_date_while_files_match_the_pin(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    _write_products(tmp_path)
    monkeypatch.setattr(OrphanetSource, "bulk_files", _pins(tmp_path, stale=False))
    monkeypatch.setattr(
        OrphanetSource, "_manifest_snapshot_date", "2025-12-09", raising=False
    )

    assert OrphanetSource(tmp_path).snapshot_date == "2025-12-09"


def test_snapshot_uses_the_files_own_date_when_the_pin_has_drifted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """Stamping the pin's date on a newer release is a false provenance line."""
    _write_products(tmp_path)
    monkeypatch.setattr(OrphanetSource, "bulk_files", _pins(tmp_path, stale=True))
    monkeypatch.setattr(
        OrphanetSource, "_manifest_snapshot_date", "2025-12-09", raising=False
    )

    src = OrphanetSource(tmp_path)

    assert src.snapshot_date == "2026-06-23"
    assert "**2026-06-23**" in src.serialize("ORPHA:558").body
