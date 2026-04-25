"""Regression test for dismech#40: term cache must be incremental.

When ``linkml-term-validator validate-data`` is run against a disorder file
whose referenced ontology terms are already cached, the cache CSVs must be
left byte-identical. If the validator rewrites timestamps for already-cached
entries, every validation run produces a huge noisy diff in
``cache/<ontology>/terms.csv``, which is exactly the bug reported in
monarch-initiative/dismech#40.

This is fixed upstream in ``linkml-term-validator>=0.3.0rc1`` (timestamp
preservation) and ``>=0.4.0rc1`` (CRLF → LF line endings); this test pins
that contract from dismech's side so a future bump of the dependency cannot
silently reintroduce the cache churn.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
OAK_CONFIG = ROOT_DIR / "conf" / "oak_config.yaml"
DISORDER_FILE = ROOT_DIR / "kb" / "disorders" / "Asthma.yaml"

# Cache files expected to be touched by validating Asthma.yaml. Asthma
# references HP, MONDO, GO, CL, and MAXO terms — the exact set does not
# matter for the test, we just need files that would be rewritten if the
# bug regressed.
CACHE_FILES = [
    ROOT_DIR / "cache" / "hp" / "terms.csv",
    ROOT_DIR / "cache" / "mondo" / "terms.csv",
    ROOT_DIR / "cache" / "go" / "terms.csv",
    ROOT_DIR / "cache" / "cl" / "terms.csv",
    ROOT_DIR / "cache" / "maxo" / "terms.csv",
]


@pytest.mark.skipif(not DISORDER_FILE.exists(), reason="Asthma.yaml fixture is missing")
def test_term_validation_does_not_rewrite_cache(tmp_path: Path) -> None:
    """Running term validation on a fully-cached file must not rewrite caches.

    Regression test for monarch-initiative/dismech#40. If this test fails,
    ``linkml-term-validator`` has regressed on timestamp preservation and
    every PR touching disorder files will show spurious cache diffs. Pin
    the dependency to the last known-good version and open an upstream
    issue before "fixing" this test.
    """
    # Snapshot existing cache contents so we can both assert invariance
    # and restore if the validator misbehaves.
    existing = [p for p in CACHE_FILES if p.exists()]
    assert existing, "Expected at least one term cache file to exist"

    snapshots: dict[Path, bytes] = {}
    for path in existing:
        snapshots[path] = path.read_bytes()
        shutil.copy2(path, tmp_path / path.name)

    try:
        result = subprocess.run(
            [
                "uv",
                "run",
                "linkml-term-validator",
                "validate-data",
                str(DISORDER_FILE),
                "-s",
                str(SCHEMA_PATH),
                "-t",
                "Disease",
                "--labels",
                "--no-dynamic-enums",
                "-c",
                str(OAK_CONFIG),
            ],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, (
            f"linkml-term-validator failed:\nstdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )

        churned: list[str] = []
        for path, before in snapshots.items():
            after = path.read_bytes()
            if before != after:
                churned.append(str(path.relative_to(ROOT_DIR)))

        assert not churned, (
            "Term cache files were rewritten by validation of an already-"
            "cached disorder file, reintroducing dismech#40. Affected: "
            + ", ".join(churned)
        )
    finally:
        # Defensive restore: if the validator did rewrite any cache, put
        # the original bytes back so the test never leaves a dirty tree.
        for path, before in snapshots.items():
            if path.read_bytes() != before:
                path.write_bytes(before)
