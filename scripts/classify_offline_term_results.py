#!/usr/bin/env python3
"""Sort an offline term-validation run into real errors and unchecked terms.

`just validate-pre-edit` calls this when the ontology service is down
(dismech#12658). By then the online run has given up on the whole file at the
first uncached lookup, so nothing was checked, cached terms included. The
recipe reruns term validation with ``--offline``, which checks every term the
local cache can answer for, and pipes the output here.

In linkml-term-validator 0.4.5 an offline run also reports two things that are
not errors in the data, only terms it could not check:

* a CURIE with no row in the label cache ("not found in offline cache");
* a CURIE whose dynamic-enum membership is not in the enum cache ("Cannot
  validate ... offline: enum closure not materialized").

Those are listed as not checked. Every other result, such as a label that does
not match its cached label, is a real error and fails the run, so the edit is
still blocked on it.

Usage::

    <validator output> | classify_offline_term_results.py --exit-code N

Exit 0 when nothing blocking was found, 1 when a real error was.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field

# A result header, as printed by `validate-data`: two spaces, an emoji, the
# severity and the message. Detail lines under it are indented further.
RESULT_RE = re.compile(r"^  \S+\s+(ERROR|WARN|WARNING|INFO):\s*(.*)$")
DETAIL_RE = re.compile(r"^\s{4,}(\w+):\s*(.*)$")
CURIE_RE = re.compile(r"'([A-Za-z][\w.-]*:[^'\s]+)'")

# Messages that mean "could not be checked offline", not "is wrong".
# Each maps to the short reason printed for the unchecked term.
UNCHECKED_PATTERNS = (
    (re.compile(r"not found in offline cache"), "not in the local term cache"),
    (
        re.compile(
            r"against dynamic enum '(\w+)' offline: enum closure not materialized"
        ),
        "{0} membership not in the local enum cache",
    ),
)


@dataclass
class Result:
    severity: str
    message: str
    details: dict[str, str] = field(default_factory=dict)

    @property
    def unchecked_reason(self) -> str | None:
        for pattern, reason in UNCHECKED_PATTERNS:
            match = pattern.search(self.message)
            if match:
                return reason.format(*match.groups())
        return None

    @property
    def key(self) -> tuple[str, str]:
        """One entry per term: the enum and the label-cache result for the same
        uncached CURIE describe the same unchecked term."""
        curie = CURIE_RE.search(self.message)
        return (self.details.get("path", ""), curie.group(1) if curie else self.message)

    def describe(self) -> str:
        where = self.details.get("path")
        return f"{self.message} ({where})" if where else self.message


def parse_results(output: str) -> list[Result]:
    results: list[Result] = []
    for line in output.splitlines():
        header = RESULT_RE.match(line)
        if header:
            results.append(Result(header.group(1), header.group(2).strip()))
            continue
        detail = DETAIL_RE.match(line)
        if detail and results:
            results[-1].details.setdefault(detail.group(1), detail.group(2).strip())
    return results


def classify(output: str, exit_code: int) -> tuple[int, list[str]]:
    """Return the exit code for the recipe and the lines to print."""
    if exit_code == 0:
        return 0, ["Offline recheck: every term was in the local cache and passed."]

    results = parse_results(output)
    if not results:
        # Nothing readable came back, so this run checked nothing either.
        # Keep the pre-#12658 behaviour (warn, allow) instead of blocking the
        # edit on output this script does not understand.
        return 0, [
            "not checked: all terms (the offline recheck exited "
            f"{exit_code} without results this script could read)"
        ]

    blocking = [r for r in results if r.unchecked_reason is None]
    if blocking:
        lines = ["❌ Offline recheck found errors in cached terms:"]
        lines += [f"  {r.severity}: {r.describe()}" for r in blocking]
        return 1, lines

    reasons: dict[tuple[str, str], list[str]] = {}
    for r in results:
        reasons.setdefault(r.key, []).append(r.unchecked_reason)
    lines = [
        "Offline recheck: no errors in what the local cache could check. Not checked:"
    ]
    for (path, curie), why in reasons.items():
        where = f" at {path}" if path else ""
        lines.append(f"  not checked: {curie}{where} ({'; '.join(why)})")
    return 0, lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--exit-code",
        type=int,
        required=True,
        help="exit code of the offline validate-data run",
    )
    args = parser.parse_args(argv)
    code, lines = classify(sys.stdin.read(), args.exit_code)
    for line in lines:
        print(line, file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
