"""Repair duplicate `evidence:` (or `notes:`) keys under a single
`- classification_value:` entry that were introduced by the
migrate_harrisons_chapter.py dedupe step.

Pattern:

    - classification_value: INFECTIOUS_DISEASES
      evidence:
      - reference: A
        ...
      evidence:           # <-- second YAML key, silently overrides the first
      - reference: B
        ...

Fix: delete the duplicate `evidence:`/`notes:` header line so both lists fold
into a single key:

    - classification_value: INFECTIOUS_DISEASES
      evidence:
      - reference: A
        ...
      - reference: B
        ...
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DISORDERS = REPO / "kb" / "disorders"

CLASS_VALUE_RE = re.compile(r"^(\s*)- classification_value:")
KEY_RE = re.compile(r"^(\s*)(\w+):\s*$")


def repair(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    # Per-classification-item bookkeeping: which keys have we already seen
    # at which indent.
    seen_keys: dict[int, set[str]] = {}
    item_indent: int | None = None
    dropped = 0

    for line in lines:
        m = CLASS_VALUE_RE.match(line)
        if m:
            # New classification item starts; reset key tracking for its body.
            item_indent = len(m.group(1))
            # Body keys are nested one indent level deeper.
            seen_keys = {}
            out.append(line)
            continue

        if item_indent is not None:
            stripped = line.lstrip(" ")
            indent = len(line) - len(stripped)
            # Exiting the classification item:
            #   * blank line is fine (stays)
            #   * a line with indent <= item_indent (and not blank) means
            #     a sibling list item or end of list
            if line.strip() and indent <= item_indent:
                item_indent = None
                seen_keys = {}
                out.append(line)
                continue

            km = KEY_RE.match(line)
            if km and km.group(2) in ("evidence", "notes"):
                key_indent = len(km.group(1))
                key = km.group(2)
                bucket = seen_keys.setdefault(key_indent, set())
                if key in bucket:
                    dropped += 1
                    continue  # drop the duplicate header line
                bucket.add(key)

        out.append(line)

    new_text = "\n".join(out)
    if not new_text.endswith("\n"):
        new_text += "\n"
    return new_text, dropped


def main() -> int:
    fixed = 0
    for path in sorted(DISORDERS.glob("*.yaml")):
        text = path.read_text()
        new_text, dropped = repair(text)
        if dropped:
            path.write_text(new_text)
            print(f"Fixed {path.name}: removed {dropped} duplicate header(s)")
            fixed += 1
    print(f"\nFixed {fixed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
