"""Stale manifest pins must be recoverable in one command.

Most structured-source manifests pin a sha256 against an *unversioned* upstream
URL — ``https://www.orphadata.com/data/xml/en_product1.xml`` is always the
current Orphanet release, not a versioned artifact. So the pin is guaranteed to
stop matching the next time upstream publishes, and `just refresh-orphadata`
hard-fails until somebody re-pins it by hand. That recurred four times in one
week (issues #9687, #9897, #10150 for Orphadata; #10081 for ClinGen).

The fix is not to weaken the check — a source changing under a curator is what
the pin exists to catch — but to make accepting a new release a single explicit
command that leaves a reviewable diff. These tests pin both halves: the default
still refuses, and `--repin` records the new checksum without disturbing the
manifest's comments.
"""

import hashlib

import pytest
from ruamel.yaml import YAML

from dismech.structured_sources.base import (
    BulkFile,
    ChecksumChange,
    ChecksumMismatchError,
    StructuredSource,
    repin_manifest,
)

PAYLOAD = b"a new upstream release\n"
NEW_SHA = hashlib.sha256(PAYLOAD).hexdigest()
STALE_SHA = "0" * 64


class _FakeSource(StructuredSource):
    prefix = "FAKE"
    bulk_files = (
        BulkFile(
            name="data.xml", url="https://example.invalid/data.xml", sha256=STALE_SHA
        ),
    )

    @staticmethod
    def _download(url: str, target) -> None:  # no network
        target.write_bytes(PAYLOAD)

    def build_index(self):
        return {}

    def identifiers(self):
        return []

    def serialize(self, identifier):
        raise NotImplementedError


MANIFEST = f"""# Pinned snapshot of the bulk files.
#
# License: CC-BY 4.0
source: Fake
snapshot_date: "2020-01-01"

bulk_files:
  - name: data.xml
    url: https://example.invalid/data.xml
    sha256: {STALE_SHA}
    size_bytes: 1
    description: The data
"""


def test_stale_pin_fails_by_default_and_names_the_remedy(tmp_path):
    """A drifted checksum must not be accepted silently."""
    source = _FakeSource(tmp_path / "data")

    with pytest.raises(ChecksumMismatchError) as excinfo:
        source.refresh()

    message = str(excinfo.value)
    assert NEW_SHA in message, "the error should show what upstream actually served"
    assert STALE_SHA in message, "and what the manifest pinned"
    assert "--repin" in message, (
        "the error must name the recovery command; leaving a curator to work out "
        "the manual re-pin ritual is what made this recur"
    )


def test_repin_records_the_new_checksum(tmp_path):
    source = _FakeSource(tmp_path / "data")

    changes = source.refresh(repin=True)

    assert [(c.name, c.old_sha256, c.new_sha256) for c in changes] == [
        ("data.xml", STALE_SHA, NEW_SHA)
    ]
    assert changes[0].size_bytes == len(PAYLOAD)


def test_repin_manifest_updates_only_the_drifted_lines(tmp_path):
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(MANIFEST)

    notes = repin_manifest(
        manifest,
        [ChecksumChange("data.xml", STALE_SHA, NEW_SHA, len(PAYLOAD))],
        snapshot_date="2026-01-02",
    )

    text = manifest.read_text()
    assert NEW_SHA in text and STALE_SHA not in text
    assert 'snapshot_date: "2026-01-02"' in text
    assert f"size_bytes: {len(PAYLOAD)}" in text
    # The manifest's prose is the only record of licence and provenance; a
    # round-trip that drops it would trade one maintenance problem for another.
    assert "# License: CC-BY 4.0" in text
    assert "description: The data" in text
    assert "  - name: data.xml" in text, "committed sequence indentation preserved"
    assert notes, "the caller needs something to show the user"

    reloaded = YAML(typ="safe").load(manifest)
    assert reloaded["bulk_files"][0]["sha256"] == NEW_SHA


def test_repin_refuses_a_download_that_lost_most_of_its_content(tmp_path):
    """A truncated transfer and a new release look identical by checksum.

    Size is the one cheap discriminator: these sources grow or shrink by a few
    percent between releases, not by half. Recording a truncated file's checksum
    would pin the corruption as if it were upstream's intent.
    """
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(MANIFEST.replace("size_bytes: 1", "size_bytes: 1000000"))

    with pytest.raises(RuntimeError, match="refusing to repin"):
        repin_manifest(
            manifest,
            [ChecksumChange("data.xml", STALE_SHA, NEW_SHA, 1234)],
        )

    # The manifest must be untouched when the guard fires.
    assert STALE_SHA in manifest.read_text()


def test_repin_accepts_an_ordinary_release_size_change(tmp_path):
    """The guard must not block a normal release, which moves by a few percent."""
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(MANIFEST.replace("size_bytes: 1", "size_bytes: 1000000"))

    notes = repin_manifest(
        manifest,
        [ChecksumChange("data.xml", STALE_SHA, NEW_SHA, 1_050_000)],
    )

    assert notes and NEW_SHA in manifest.read_text()


def test_repin_manifest_is_a_noop_without_changes(tmp_path):
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(MANIFEST)

    assert repin_manifest(manifest, []) == []
    assert manifest.read_text() == MANIFEST
