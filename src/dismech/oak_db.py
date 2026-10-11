"""Where OAK keeps its local SQLite ontology builds.

`get_adapter("sqlite:obo:ncit")` does **not** fail when the build is absent.
semsql downloads it — 2.7 GB for NCIT alone — so "did the adapter open?" answers
whether the machine has network access, never whether the build was already
there. Anything that must not trigger a multi-gigabyte download has to ask about
the file first, which is what :func:`local_build_path` is for.

OAK resolves these through pystow, which reads ``PYSTOW_HOME`` and nothing else
— not ``OAK_DB_DIR``. This mirrors the resolution in
``scripts/fetch_ontology_dbs.sh`` so everything looks in the same place.
"""

from __future__ import annotations

import os
from pathlib import Path

__all__ = ["adapter_build_name", "local_build_path", "local_build_present"]


def local_build_path(name: str) -> Path:
    """Path to the ``<name>.db`` SQLite build, whether or not it exists."""
    home = os.environ.get("PYSTOW_HOME")
    base = Path(home) if home else Path.home() / ".data"
    return base / "oaklib" / f"{name}.db"


def adapter_build_name(adapter_spec: str) -> str | None:
    """The build name inside a ``sqlite:obo:<name>`` adapter string.

    Returns None for any other adapter form (``ols:``, a file path, …), which
    have no local build to look for.
    """
    prefix = "sqlite:obo:"
    if not adapter_spec.startswith(prefix):
        return None
    return adapter_spec[len(prefix) :].strip() or None


def local_build_present(adapter_spec: str) -> bool:
    """True when this adapter's build is already on disk.

    False for a non-``sqlite:obo:`` adapter too: the question is "can this be
    served without a download", and only a local build answers yes.
    """
    name = adapter_build_name(adapter_spec)
    return bool(name) and local_build_path(name).is_file()
