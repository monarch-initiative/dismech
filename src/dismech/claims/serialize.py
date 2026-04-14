"""Serialization helpers for claim extraction outputs."""

from __future__ import annotations

import csv
from dataclasses import asdict
from typing import TextIO

from dismech.claims.models import ClaimRow


def write_claim_rows(rows: list[ClaimRow], stream: TextIO) -> None:
    """Write claim rows as CSV."""
    fieldnames = list(ClaimRow.__dataclass_fields__.keys())
    writer = csv.DictWriter(stream, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(asdict(row))
