"""Tally one evidence-claim adjudication run (README.md, "The seven tables").

Both modes are run by the session that built the frame, never by a judging session: the
first shows one reader's verdicts beside another's, and the second opens the checker's
labels.

* ``--disagreements`` (before the freeze). It refuses until the judge's two sheets, the
  second reader's verdicts (``second_look_verdicts.csv``, a filled-in copy of
  ``second_look_sheet.csv``) and the reviewer's blind sample are complete, use the
  vocabulary below and hold exactly the rows of ``frame_index.json``. It then records the
  sha256 of those four files in ``PREFREEZE.txt``, so that none of them can change once
  one reader's verdicts have been shown beside another's, and lists what the reviewer has
  to rule on. It reads no checker label, and until the sheets are complete it names the
  rows and columns at fault without printing what they hold or which rule they break
  (the rules are in ``rubric.md``, "Filling in the sheets"). The reviewer's blind sample is
  locked once its sheet is complete and passes its own checks: its sha256 is written to
  ``BLIND.txt``, and the sha256 of ``BLIND.txt`` is printed, to be published outside the
  run folder before the list is shown to any reader; the tally requires that hash, so a
  lock taken again after the sheet has changed is refused. Until the lock, a problem on
  another reader's row is held when the row is of a sampled pair, of the same or a nested
  assertion, or of a row shown beside a sampled pair (the rows its claim names: its parent
  rows, a subtype or hypothesis row, an edge's endpoints and scope), or when its key or
  assertion path is not in the frame. A held problem is reported without a row, a column
  or a number, and a held blank row is not counted, since either would hint which way a
  reader leaned on a pair the reviewer has still to judge.
* default (after the freeze). It refuses to run unless:
  - ``--expect-freeze`` gives the sha256 of ``FREEZE.txt`` that was recorded before any
    label was opened, and the file still has it;
  - ``--expect-blind`` gives the sha256 of ``BLIND.txt`` that was published when the
    reviewer's sheet was locked, and the file still has it;
  - ``FREEZE.txt`` lists every verdict file, and every file it lists exists and matches;
  - the four files of ``PREFREEZE.txt`` are frozen unchanged, and ``BLIND.txt`` locked
    the reviewer's sheet in the state ``PREFREEZE.txt`` records;
  - every row of every verdict file carries a verdict or ``not judged: <reason>``;
  - every difference between the judge and the second reader has a ruling or the
    reviewer's own blind verdict, and no ruling is given where none is called for;
  - the sheets hold exactly the frame's pairs, assertions and samples.
  Only then does it open the sealed folder. It first reads the sealed record of the build
  and checks that the run folder, the frame index, ``rubric.md`` and the committed key
  file are the ones the frame was built with. Then, before reading a label, it writes
  there, in ``opened.json``, the freeze under which the labels were first opened; a later
  run under another freeze is refused unless ``--reopened`` gives the reason, which the
  tables then carry. It then reads the labels, checks that they are the ones the frame was
  built with, and writes tables 1 to 5, counts only. From ``fenced_sheet.csv`` it reads
  the verdict columns only.

Tables 6 and 7 of the README (before and after the repairs; what was done) are not
computed here. They need the repair pull requests and a checker run made after them, and
are added to this script with those.

Verdict columns, as ``build_frame.py`` writes them empty:

* ``q1_claim_right`` to ``q4_term_level``: yes, no, unsure or n/a.
* ``defect_class``: a class from the README; "none" (or empty, on a pair) for no defect;
  or ``not judged: <reason>``. A judge's ``not judged: stopped`` on a pair, or on its
  assertion, holds the whole assertion as not judged, and its other rows may stay empty.
* ``severity``: 1, 2 or 3 on a defect, empty otherwise.
* ``clauses_covered`` (assertion sheet): yes, no or partly on a row with quotes, where no
  and partly need a defect class; n/a on a row with no quote, which needs ``no quote at
  all`` (with a severity) or ``none`` as its defect class.

Combinations that contradict themselves stop both modes rather than being read one way: a
question answered no or unsure with no defect class, a defect with no severity, every
clause covered together with a defect class, ``no quote at all`` on a pair or on a row
that has quotes.

Which verdict governs a pair, as the README defines a confirmed defect: a ruling in
``rulings.csv`` (key, defect_class, severity, note); else the reviewer's blind verdict;
else the judge's. The second reader never settles a difference on its own, and a ruling
is accepted only on a pair where the second reader differs from the judge and the
reviewer's own blind verdict does not already govern.

Table 4 ranks the frame's assessed pairs by the checker's whole-claim mismatch
probability. A tie at a cut-off is not broken: the table gives the pairs strictly above
the probability of the pair at the cut-off, the pairs tied with it, and both together.

Usage:

    python experiments/evidence_claim_adjudication/tally.py --run <run folder> --disagreements
    python experiments/evidence_claim_adjudication/tally.py --run <run folder> \\
        --sealed <sealed folder> --expect-freeze <sha256 of FREEZE.txt> [--out tables.md]
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path

csv.field_size_limit(sys.maxsize)

HERE = Path(__file__).resolve().parent
Q_COLUMNS = ["q1_claim_right", "q2_direction_right", "q3_quote_bears", "q4_term_level"]
NO_DEFECT = {"", "none", "no defect", "not a defect"}
# The defect classes of the README's rubric, lower-cased. The last is for an assertion
# with no evidence item, never for a pair.
PAIR_CLASSES = {
    "reaches past its quotes",
    "contradicted by its source",
    "wrong direction",
    "wrong quote",
    "unusable quote",
    "wrong grading",
    "explanation misreads the quote",
    "wrong or misplaced term",
}
NO_QUOTE = "no quote at all"
CLASSES = PAIR_CLASSES | {NO_QUOTE}
SEVERITIES = {"1", "2", "3"}
ANSWERS = {"", "yes", "no", "unsure", "n/a"}
COVERED_NO = {"no", "partly"}
NOT_JUDGED = re.compile(r"^not judged: \S")
STOPPED = "not judged: stopped"
FREEZE_LINE = re.compile(r"^([0-9a-fA-F]{64}) [ *](.+)$")
JUDGE, ASSERTIONS = "judge_sheet.csv", "assertion_sheet.csv"
SECOND, USER, FENCED = (
    "second_look_verdicts.csv",
    "user_sample_sheet.csv",
    "fenced_sheet.csv",
)
RULINGS, INDEX, RUBRIC = "rulings.csv", "frame_index.json", "rubric.md"
BLIND = "BLIND.txt"
PRE_FILES = [JUDGE, ASSERTIONS, SECOND, USER]
VERDICT_FILES = [*PRE_FILES, FENCED]
PAIR_VERDICTS = [*Q_COLUMNS, "defect_class", "severity"]
REQUIRED_COLUMNS = {
    JUDGE: ["key", "assertion_path", *PAIR_VERDICTS],
    ASSERTIONS: [
        "assertion_path",
        "pairs",
        "clauses_covered",
        "defect_class",
        "severity",
    ],
    SECOND: ["key", "assertion_path", *PAIR_VERDICTS],
    USER: ["key", "assertion_path", *PAIR_VERDICTS],
    FENCED: ["key", *PAIR_VERDICTS],
    RULINGS: ["key", "defect_class", "severity"],
}
MISSING_HINT = {
    SECOND: " (the second reader writes its verdicts in a copy of second_look_sheet.csv "
    "under that name)",
    INDEX: " (build_frame.py writes it; a run folder built without it must be rebuilt)",
}
CUTOFFS = (50, 100, 200)
FLAGGED_ROW = (
    "assertions flagged MISMATCH, PARTIAL on any field, over every observed input "
    "(excluded rows included)"
)


def norm(text) -> str:
    return " ".join(str(text or "").split())


def read(path: Path) -> list[dict]:
    """A sheet as rows, with a plain message for a missing file or a missing column."""
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            rows = list(reader)
            columns = reader.fieldnames or []
    except FileNotFoundError:
        sys.exit(
            f"{path.name} is missing from the run folder{MISSING_HINT.get(path.name, '')}"
        )
    missing = [c for c in REQUIRED_COLUMNS.get(path.name, []) if c not in columns]
    if missing:
        sys.exit(f"{path.name} lacks the column(s): {', '.join(missing)}")
    return rows


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def defect_class(row: dict) -> str:
    return norm(row.get("defect_class")).lower()


def section_of(assertion_path: str) -> str:
    return assertion_path.strip("/").split("/")[0]


def has_no_quote(row: dict) -> bool:
    return norm(row.get("pairs")) in ("", "0")


def verdict(row: dict | None) -> str:
    """'defect', 'no_defect', 'not_judged' or 'blank' for one pair row."""
    if not row:
        return "blank"
    cls = defect_class(row)
    if NOT_JUDGED.match(cls):
        return "not_judged"
    if cls in CLASSES:
        return "defect"
    if not cls and not all(norm(row.get(q)) for q in Q_COLUMNS):
        return "blank"
    return "no_defect"


def assertion_verdict(row: dict | None) -> str:
    """The same four states for one assertion row. A row with no quote needs an explicit
    class, so that leaving it empty is never read as "no defect"."""
    if not row:
        return "blank"
    cls = defect_class(row)
    covered = norm(row.get("clauses_covered")).lower()
    if NOT_JUDGED.match(cls):
        return "not_judged"
    if cls in CLASSES or covered in COVERED_NO:
        return "defect"
    if has_no_quote(row):
        return "no_defect" if cls in NO_DEFECT - {""} else "blank"
    return "no_defect" if covered == "yes" else "blank"


def judged(state: str) -> bool:
    return state in ("defect", "no_defect")


def nothing_held(_id) -> bool:
    """The default for the sheets whose problems are always named."""
    return False


def problems_in(
    name: str,
    rows: list[dict],
    id_column: str,
    level: str,
    held=nothing_held,
) -> list[str]:
    """Values outside the vocabulary, and verdicts that contradict themselves. Only the row
    and the column are named. What a reader wrote is never printed, and neither is the rule
    it breaks, whose wording would tell whoever reads the output which way a reader went:
    each rule is written beside its test, and for the readers in rubric.md. Problems on
    rows ``held`` picks out, duplicates included, are reported in one line without a row,
    a column or a number."""
    found, held_back = [], set()

    def report(row, column, _rule):
        if held(row.get(id_column)):
            held_back.add(row.get(id_column))
            return
        line = f"{name} {row.get(id_column, '?')}: {column}"
        if line not in found:
            found.append(line)

    seen = Counter(row.get(id_column, "") for row in rows)
    for key, n in seen.items():
        if n > 1 and held(key):
            held_back.add(key)
        elif n > 1:
            found.append(f"{name}: {key} appears {n} times")
    for row in rows:
        cls = defect_class(row)
        severity = norm(row.get("severity"))
        allowed = PAIR_CLASSES if level == "pair" else CLASSES
        if cls.startswith("not judged") and not NOT_JUDGED.match(cls):
            report(row, "defect_class", "must read 'not judged: <reason>'")
        elif not (cls in NO_DEFECT or cls in allowed or NOT_JUDGED.match(cls)):
            report(row, "defect_class", "is not a class of the rubric at this level")
        if cls in CLASSES and severity not in SEVERITIES:
            report(row, "severity", "must be 1, 2 or 3 on a defect")
        if cls not in CLASSES and severity:
            report(row, "severity", "is given without a defect class")
        if level == "pair":
            if cls and not NOT_JUDGED.match(cls) and all(q in row for q in Q_COLUMNS):
                for q in Q_COLUMNS:
                    if not norm(row.get(q)):
                        report(row, q, "is unanswered on a judged pair")
            answers = [norm(row.get(q)).lower() for q in Q_COLUMNS if q in row]
            for q in Q_COLUMNS:
                if q in row and norm(row.get(q)).lower() not in ANSWERS:
                    report(row, q, "must be yes, no, unsure or n/a")
            if cls in NO_DEFECT and "no" in answers:
                report(row, "defect_class", "is empty though a question is answered no")
            if cls in NO_DEFECT and "unsure" in answers:
                report(
                    row,
                    "defect_class",
                    "is empty though a question is unsure: give a class or "
                    "'not judged: <reason>'",
                )
            continue
        covered = norm(row.get("clauses_covered")).lower()
        if covered not in {"", "yes", "n/a", "unsure"} | COVERED_NO:
            report(row, "clauses_covered", "must be yes, no, partly or n/a")
        if covered in COVERED_NO and cls not in CLASSES:
            report(row, "clauses_covered", "says a clause is uncovered: give a class")
        if covered == "yes" and cls in CLASSES:
            report(
                row,
                "clauses_covered",
                "says every clause is covered, yet a class is given",
            )
        if covered == "unsure" and not NOT_JUDGED.match(cls):
            report(row, "clauses_covered", "is unsure: write 'not judged: <reason>'")
        if covered == "yes" and NOT_JUDGED.match(cls):
            report(row, "clauses_covered", "is yes on a row marked not judged")
        if covered in COVERED_NO and not norm(row.get("uncovered_clauses")):
            report(row, "uncovered_clauses", "must name the clauses no quote covers")
        if has_no_quote(row):
            if covered not in ("", "n/a"):
                report(row, "clauses_covered", "must be n/a on a row with no quote")
            if covered != "n/a" and cls and not NOT_JUDGED.match(cls):
                report(
                    row, "clauses_covered", "must be n/a on a judged row with no quote"
                )
            if cls in PAIR_CLASSES:
                report(
                    row,
                    "defect_class",
                    f"on a row with no quote the only defect class is '{NO_QUOTE}'",
                )
        else:
            if covered == "n/a":
                report(row, "clauses_covered", "is n/a on a row that has quotes")
            if not covered and cls and not NOT_JUDGED.match(cls):
                report(row, "clauses_covered", "is empty on a judged row with quotes")
            if cls == NO_QUOTE:
                report(row, "defect_class", f"is '{NO_QUOTE}' on a row with quotes")
    if held_back:
        found.append(held_line(name))
    return found


def held_line(name: str) -> str:
    return (
        f"{name}: some row(s) on or near the reviewer's blind sample, or not in the frame, "
        f"need attention; they are named once {USER} is complete and locked in {BLIND}"
    )


def blanks(rows: list[dict], level: str, stopped: frozenset = frozenset()) -> int:
    """Rows with no verdict. Rows of an assertion the judge's stop holds may stay empty."""
    state = verdict if level == "pair" else assertion_verdict
    return sum(
        1
        for row in rows
        if state(row) == "blank" and row.get("assertion_path") not in stopped
    )


def blank_rows(
    rows: list[dict], level: str, id_column: str, stopped: frozenset = frozenset()
) -> list[str]:
    """The ids of the rows with no verdict, in sheet order (see ``blanks``)."""
    state = verdict if level == "pair" else assertion_verdict
    return [
        str(row.get(id_column, "?"))
        for row in rows
        if state(row) == "blank" and row.get("assertion_path") not in stopped
    ]


def stopped_assertions(judge: list[dict], assertions: list[dict]) -> frozenset:
    """A judge's stop holds the whole assertion (README, "What is left out")."""
    return frozenset(
        row["assertion_path"]
        for row in [*judge, *assertions]
        if defect_class(row).startswith(STOPPED)
    )


def differs(first: dict, other: dict) -> str | None:
    """How another reader's verdict differs from the judge's, if it does."""
    a, b = verdict(first), verdict(other)
    if not judged(b):
        return None
    if a == "not_judged":
        return "the judge left it not judged"
    if a != b:
        return "defect or not"
    if a == "defect" and defect_class(first) != defect_class(other):
        return "class"
    if a == "defect" and norm(first.get("severity")) != norm(other.get("severity")):
        return "severity"
    return None


def needing_a_ruling(judge: dict, second: dict, user: dict, stopped: frozenset) -> dict:
    """Pairs where the second reader differs from the judge and the reviewer's own blind
    verdict does not already settle it."""
    need = {}
    for key, row in second.items():
        first = judge.get(key)
        if not first or first["assertion_path"] in stopped:
            continue
        how = differs(first, row)
        if how and not judged(verdict(user.get(key))):
            need[key] = how
    return need


def load_index(run: Path) -> dict:
    path = run / INDEX
    try:
        index = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"{INDEX} is missing from the run folder{MISSING_HINT[INDEX]}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        sys.exit(f"{INDEX} cannot be read")
    if "user_sample_context_paths" not in index:
        sys.exit(
            f"{INDEX} predates this tally.py: rebuild the frame with build_frame.py"
        )
    return index


def load_sheets(run: Path, lock: bool = False):
    """The four blind sheets, the frame index, the assertions a judge's stop holds, and
    everything wrong with the sheets. With ``lock``, the reviewer's sheet is locked in
    BLIND.txt as soon as it is complete and passes its own checks."""
    index = load_index(run)
    sheets = {name: read(run / name) for name in PRE_FILES}
    path_of = {key: path for key, path in index["pairs"]}
    index_paths = frozenset(path for path, _ in index["assertions"])
    sample = frozenset(index.get("user_sample_keys") or [])
    sample_paths = frozenset(path_of[k] for k in sample if k in path_of)
    # Rows the reviewer reads beside a sampled pair: its parent rows, an edge's object row.
    context = frozenset(index["user_sample_context_paths"])

    def near_sample(path) -> bool:
        path = str(path or "")
        return path in context or any(
            path == p or path.startswith(p + "/") for p in sample_paths
        )

    # The reviewer's own sheet: its problems are always named.
    user_found = problems_in(USER, sheets[USER], "key", "pair")
    user_found += path_problems(USER, sheets[USER], path_of)
    user_found += stop_problems(USER, sheets[USER], path_of)
    if {r["key"] for r in sheets[USER]} != set(sample):
        user_found.append(f"{USER} does not hold exactly the reviewer's sample")
    user_blank = blank_rows(sheets[USER], "pair", "key")
    if user_blank:
        user_found.append(blank_line(USER, user_blank))
    # The lock: once the reviewer's sheet is final, its hash goes to BLIND.txt, whose own
    # hash is printed to be published outside the run folder.
    blind, user_sha = run / BLIND, sha256_file(run / USER)
    if not blind.exists() and lock and not user_found:
        blind.write_text(f"{user_sha}  {USER}\n", encoding="utf-8")
        print(
            f"# {USER} is now locked in {BLIND}, whose sha256 is {sha256_file(blind)}. "
            "Publish that hash outside the run folder before this list is shown to any "
            "reader; the tally requires it as --expect-blind.",
            file=sys.stderr,
        )
    locked = False
    if blind.exists():
        recorded, bad = read_hash_lines(blind)
        user_found += bad
        if USER not in recorded:
            user_found.append(f"{BLIND} does not record {USER}")
        elif recorded[USER] != user_sha:
            user_found.append(f"{USER} has changed since it was locked in {BLIND}")
        else:
            locked = not bad

    # Until then, the other readers' rows on or near the sample, and rows the frame does
    # not have, are held: a duplicated or mistyped key would otherwise be named.
    def hold_key(key) -> bool:
        return not locked and (
            key not in path_of or key in sample or near_sample(path_of[key])
        )

    def hold_path(path) -> bool:
        return not locked and (path not in index_paths or near_sample(path))

    found = (
        problems_in(JUDGE, sheets[JUDGE], "key", "pair", hold_key)
        + problems_in(
            ASSERTIONS, sheets[ASSERTIONS], "assertion_path", "assertion", hold_path
        )
        + problems_in(SECOND, sheets[SECOND], "key", "pair", hold_key)
        + path_problems(SECOND, sheets[SECOND], path_of, hold_key)
        + stop_problems(SECOND, sheets[SECOND], path_of, hold_key)
        + user_found
    )
    if {r["key"]: r["assertion_path"] for r in sheets[JUDGE]} != path_of:
        found.append(
            f"{JUDGE} does not hold exactly the frame's pairs, each on its own assertion"
        )
    if {r["assertion_path"]: norm(r.get("pairs")) for r in sheets[ASSERTIONS]} != {
        path: str(n) for path, n in index["assertions"]
    }:
        found.append(
            f"{ASSERTIONS} does not hold exactly the frame's assertions, each with its "
            "number of pairs"
        )
    if {r["key"] for r in sheets[SECOND]} != set(index["second_look_keys"]):
        found.append(f"{SECOND} does not hold exactly the second reader's sample")
    stopped = stopped_assertions(sheets[JUDGE], sheets[ASSERTIONS])
    unfinished = {
        JUDGE: (blank_rows(sheets[JUDGE], "pair", "key", stopped), hold_key),
        ASSERTIONS: (
            blank_rows(sheets[ASSERTIONS], "assertion", "assertion_path", stopped),
            hold_path,
        ),
        SECOND: (blank_rows(sheets[SECOND], "pair", "key"), hold_key),
    }
    for name, (ids, hold) in unfinished.items():
        shown = [i for i in ids if not hold(i)]
        if shown:
            found.append(blank_line(name, shown))
        if len(shown) < len(ids):
            found.append(held_line(name))
    # One held line per sheet, always last and in a fixed order, so that neither its
    # place nor its company says what kind of problem it stands for.
    held = [held_line(n) for n in (JUDGE, ASSERTIONS, SECOND) if held_line(n) in found]
    found = [line for line in dict.fromkeys(found) if line not in held] + held
    return sheets, index, stopped, found


def blank_line(name: str, ids: list[str]) -> str:
    """How many rows carry no verdict, with a few of them named. While the reviewer's sheet
    is unlocked, held rows are left out of both (``load_sheets``)."""
    line = f"{name}: {len(ids)} row(s) carry no verdict and no 'not judged: <reason>'"
    return line + f" (among them: {', '.join(ids[:5])})"


def path_problems(
    name: str, rows: list[dict], path_of: dict, held=nothing_held
) -> list[str]:
    """Rows of a sample sheet whose assertion path is not the one the frame gives."""
    bad = [
        r.get("key")
        for r in rows
        if r.get("assertion_path") != path_of.get(r.get("key"))
    ]
    found = [f"{name} {k}: assertion_path" for k in bad if not held(k)]
    if len(found) < len(bad):
        found.append(held_line(name))
    return found


def stop_problems(
    name: str, rows: list[dict], path_of: dict, held=nothing_held
) -> list[str]:
    """Another reader's stop covers each of its rows of that assertion, the assertion
    being the one the frame gives for the pair."""
    rows_of = defaultdict(list)
    for row in rows:
        rows_of[path_of.get(row.get("key"), row.get("assertion_path"))].append(row)
    partial = [
        row.get("key")
        for group in rows_of.values()
        if any(defect_class(r).startswith(STOPPED) for r in group)
        for row in group
        if not defect_class(row).startswith(STOPPED)
    ]
    found = [f"{name} {k}: defect_class" for k in partial if not held(k)]
    if len(found) < len(partial):
        found.append(held_line(name))
    return found


def read_hash_lines(path: Path) -> tuple[dict[str, str], list[str]]:
    listed, found = {}, []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return {}, [f"{path.name} cannot be read as text"]
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        match = FREEZE_LINE.match(line.rstrip())
        name = Path(match.group(2).strip()).name if match else ""
        if not name:
            found.append(f"{path.name} line {n} is not a sha256sum line")
            continue
        digest = match.group(1).lower()
        if listed.get(name, digest) != digest:
            found.append(f"{path.name}: {name} is listed twice, with different hashes")
        listed[name] = digest
    return listed, found


def disagreements(run: Path) -> int:
    sheets, _, stopped, found = load_sheets(run, lock=True)
    if found:
        sys.exit(
            "not yet: the four sheets must be complete and within the rubric's vocabulary "
            "before one reader's verdicts are shown beside another's. Each line names a "
            "sheet, and a row and a column where one is at fault; the rules are in "
            f"{RUBRIC}, 'Filling in the sheets':\n  " + "\n  ".join(found)
        )
    now = {name: sha256_file(run / name) for name in PRE_FILES}
    record = run / "PREFREEZE.txt"
    if record.exists():
        before, bad = read_hash_lines(record)
        if bad or before != now:
            sys.exit(
                "refusing: a sheet has changed since the disagreements were first listed "
                "(PREFREEZE.txt records the four sheets as they were then)"
            )
    else:
        record.write_text(
            "".join(f"{digest}  {name}\n" for name, digest in now.items()),
            encoding="utf-8",
        )
    judge = {r["key"]: r for r in sheets[JUDGE]}
    second = {r["key"]: r for r in sheets[SECOND]}
    user = {r["key"]: r for r in sheets[USER]}
    need = needing_a_ruling(judge, second, user, stopped)
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(
        [
            "key",
            "assertion_path",
            "differs_on",
            "judge",
            "judge_class",
            "judge_severity",
            "other_reader",
            "other",
            "other_class",
            "other_severity",
            "to_do",
        ]
    )

    def line(key, how, reader, other, to_do):
        first = judge[key]
        out.writerow(
            [
                key,
                first["assertion_path"],
                how,
                verdict(first),
                first.get("defect_class", ""),
                first.get("severity", ""),
                reader,
                verdict(other),
                other.get("defect_class", ""),
                other.get("severity", ""),
                to_do,
            ]
        )

    for key, how in need.items():
        line(key, how, "second reader", second[key], f"rule on it in {RULINGS}")
    settled = 0
    for key, row in user.items():
        first = judge.get(key)
        if not first or first["assertion_path"] in stopped:
            continue
        how = differs(first, row)
        if how:
            settled += 1
            line(key, how, "reviewer", row, "none: the reviewer's verdict governs")
    print(
        f"# {len(need)} pair(s) need a ruling; on {settled} more the reviewer's own blind "
        f"verdict differs from the judge's and governs; {len(stopped)} assertion(s) are "
        f"held by a stop. PREFREEZE.txt records the four sheets; {BLIND} has sha256 "
        f"{sha256_file(run / BLIND)}.",
        file=sys.stderr,
    )
    return 0


def check_freeze(run: Path) -> dict[str, str]:
    freeze = run / "FREEZE.txt"
    if not freeze.is_file():
        sys.exit(
            "FREEZE.txt is missing: the verdicts are not frozen, so no label may be joined"
        )
    listed, found = read_hash_lines(freeze)
    required = set(VERDICT_FILES)
    if (run / RULINGS).exists():
        required.add(RULINGS)
    found += [
        f"{name} is not listed in FREEZE.txt" for name in sorted(required - set(listed))
    ]
    # Every listed file is checked, not only the expected ones: a frozen file deleted or
    # renamed after the freeze would otherwise drop out of the tally unnoticed.
    for name, digest in sorted(listed.items()):
        path = run / name
        if not path.is_file():
            found.append(f"{name} is listed but missing")
        elif sha256_file(path) != digest:
            found.append(f"{name} does not match its hash in FREEZE.txt")
    record = run / "PREFREEZE.txt"
    if not (run / BLIND).is_file():
        found.append(f"{BLIND} is missing: the reviewer's sheet was never locked")
    if not record.is_file():
        found.append("PREFREEZE.txt is missing: run --disagreements before the freeze")
    else:
        before, bad = read_hash_lines(record)
        found += bad
        if (run / BLIND).is_file():
            locked, bad_lock = read_hash_lines(run / BLIND)
            found += bad_lock
            if locked.get(USER) != before.get(USER):
                found.append(f"PREFREEZE.txt and {BLIND} disagree on {USER}")
        found += [
            f"{name} changed after the disagreements were listed"
            for name in PRE_FILES
            if before.get(name) != listed.get(name)
        ]
    if found:
        sys.exit("refusing to tally:\n  " + "\n  ".join(found))
    return listed


def sealed_bytes(path: Path) -> bytes:
    """A file of the sealed folder, with a plain message when the folder is closed."""
    if not path.parent.exists():
        sys.exit(
            f"{path.parent} does not exist: give the sealed folder the frame was built with"
        )
    if not os.access(path.parent, os.R_OK | os.X_OK):
        sys.exit(
            f"{path.parent} cannot be read. It is kept closed (chmod 000) between uses: "
            "reopen it with chmod 700 for the tally, once the sha256 of FREEZE.txt is "
            "public, and close it again afterwards."
        )
    try:
        return path.read_bytes()
    except FileNotFoundError:
        sys.exit(f"{path.name} is missing from the sealed folder {path.parent}")


def first_opening(
    sealed: Path, freeze_sha: str, prefreeze_sha: str, reason: str | None
):
    """Record, before any label is read, the freeze under which the labels are opened. A
    later run under another freeze is refused unless a reason is given."""
    record = sealed / "opened.json"
    now = {"freeze_sha256": freeze_sha, "prefreeze_sha256": prefreeze_sha}
    if not record.exists():
        first = {**now, "opened_at": datetime.now(UTC).isoformat(timespec="seconds")}
        try:
            record.write_text(json.dumps(first, indent=2) + "\n", encoding="utf-8")
        except PermissionError:
            sys.exit(
                f"{sealed} cannot be written, so the opening cannot be recorded and no label "
                "is read: reopen it with chmod 700"
            )
        return first, None
    first = json.loads(record.read_text(encoding="utf-8"))
    if {k: first.get(k) for k in now} == now:
        return first, None
    if not reason or not str(reason).strip():
        sys.exit(
            "refusing to tally: the labels were first opened on "
            f"{first.get('opened_at')} under another freeze "
            f"({str(first.get('freeze_sha256'))[:12]}). Verdicts frozen after the labels "
            "were seen are not blind. To tally them all the same, give the reason with "
            "--reopened; the tables will carry it."
        )
    return first, reason


def reason_text(reason) -> str:
    text = " ".join(str(reason).split())
    return text if text[-1:] in ".?!" else text + "."


def table(title: str, header: list[str], rows: list[list]) -> str:
    lines = [
        f"### {title}",
        "",
        "| " + " | ".join(header) + " |",
        "|" + "---|" * len(header),
    ]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines) + "\n"


def share(part: int, whole: int) -> str:
    return f"{100 * part / whole:.0f}%" if whole else "-"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument(
        "--sealed", type=Path, help="the folder holding the checker's labels and counts"
    )
    parser.add_argument("--disagreements", action="store_true")
    parser.add_argument(
        "--expect-freeze",
        help="the sha256 of FREEZE.txt, as recorded before any label was opened",
    )
    parser.add_argument(
        "--expect-blind",
        help="the sha256 of BLIND.txt, as published when the reviewer's sheet was locked",
    )
    parser.add_argument(
        "--reopened",
        help="why a tally is run under a freeze other than the one the labels were first "
        "opened under",
    )
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    run = args.run
    if args.disagreements:
        return disagreements(run)
    if not args.sealed:
        sys.exit("--sealed is required: it is where the checker's labels are kept")
    if not args.expect_freeze:
        sys.exit(
            "--expect-freeze is required: give the sha256 of FREEZE.txt that was recorded "
            "before any label was opened"
        )
    if not args.expect_blind:
        sys.exit(
            "--expect-blind is required: give the sha256 of BLIND.txt that was published "
            "when the reviewer's sheet was locked"
        )

    frozen = check_freeze(run)
    freeze_sha = sha256_file(run / "FREEZE.txt")
    if args.expect_freeze.lower() != freeze_sha:
        sys.exit("refusing to tally: FREEZE.txt is not the one whose hash was recorded")
    if args.expect_blind.lower() != sha256_file(run / BLIND):
        sys.exit("refusing to tally: BLIND.txt is not the one whose hash was published")
    sheets, index, stopped, found = load_sheets(run)
    fenced = [
        {c: r.get(c, "") for c in ["key", *PAIR_VERDICTS]} for r in read(run / FENCED)
    ]
    found += problems_in(FENCED, fenced, "key", "pair")
    if blanks(fenced, "pair"):
        found.append(
            f"{FENCED}: {blanks(fenced, 'pair')} row(s) carry no verdict and no "
            "'not judged: <reason>'"
        )
    if {r["key"] for r in fenced} != set(index["excluded_keys"]):
        found.append(f"{FENCED} does not hold exactly the excluded pairs")
    judge = {r["key"]: r for r in sheets[JUDGE]}
    assertion_rows = {r["assertion_path"]: r for r in sheets[ASSERTIONS]}
    second = {r["key"]: r for r in sheets[SECOND]}
    user = {r["key"]: r for r in sheets[USER]}
    need = needing_a_ruling(judge, second, user, stopped)
    ruling_rows = read(run / RULINGS) if (run / RULINGS).exists() else []
    found += problems_in(RULINGS, ruling_rows, "key", "pair")
    found += [
        f"{RULINGS} {r.get('key')}: a ruling needs a defect class or 'none'"
        for r in ruling_rows
        if not defect_class(r) or NOT_JUDGED.match(defect_class(r))
    ]
    found += [
        f"{RULINGS} {r.get('key')}: no ruling is called for on this pair"
        for r in ruling_rows
        if r.get("key") not in need
    ]
    rulings = {r["key"]: r for r in ruling_rows}
    found += [
        f"{key}: the second reader differs from the judge ({how}) and there is no ruling"
        for key, how in need.items()
        if key not in rulings
    ]
    if found:
        sys.exit("refusing to tally:\n  " + "\n  ".join(found))

    # The sealed folder is opened only now, after the freeze and every check above. Its
    # record of the build is read first, to make sure the folder belongs to this run; only
    # then is the opening recorded, and only after that is a label read.
    meta = json.loads(sealed_bytes(args.sealed / "frame_meta.json").decode("utf-8"))
    mismatches = []
    if Path(str(meta.get("run_folder"))).resolve() != run.resolve():
        mismatches.append("the sealed folder was built with another run folder")
    if sha256_file(run / INDEX) != meta.get("frame_index_sha256"):
        mismatches.append(f"{INDEX} is not the one this frame was built with")
    if not (run / RUBRIC).is_file() or sha256_file(run / RUBRIC) != meta.get(
        "rubric_sha256"
    ):
        mismatches.append(f"{RUBRIC} is not the one this frame was built with")
    keys_file = HERE / Path(str(meta.get("entry"))).stem / "frame_keys.tsv"
    keys_note = ""
    if not keys_file.is_file():
        keys_note = (
            f" The committed key file ({keys_file.parent.name}/{keys_file.name}) is not in "
            "this checkout, so it was not compared with the frame."
        )
    elif sha256_file(keys_file) != meta.get("frame_keys_sha256"):
        mismatches.append(
            "the committed frame_keys.tsv is not the one this frame wrote"
        )
    if mismatches:
        sys.exit(
            "refusing to tally, before any label was read:\n  "
            + "\n  ".join(mismatches)
        )
    first, reopened = first_opening(
        args.sealed, freeze_sha, sha256_file(run / "PREFREEZE.txt"), args.reopened
    )
    labels_bytes = sealed_bytes(args.sealed / "checker_labels.json")
    labels = json.loads(labels_bytes.decode("utf-8"))
    frame = {k: v["assertion_path"] for k, v in labels.items() if not v.get("excluded")}
    mismatches = []
    if hashlib.sha256(labels_bytes).hexdigest() != meta.get("checker_labels_sha256"):
        mismatches.append(
            "checker_labels.json is not the file this frame was built with"
        )
    if frame != {key: path for key, path in index["pairs"]}:
        mismatches.append(f"{INDEX} and the labels do not hold the same frame")
    if mismatches:
        sys.exit("refusing to tally:\n  " + "\n  ".join(mismatches))

    pairs_of = defaultdict(list)
    for key, row in judge.items():
        pairs_of[row["assertion_path"]].append(key)

    final, settled_by = {}, Counter()
    for key, row in judge.items():
        if row["assertion_path"] in stopped:
            source = "held by a stop"
        elif key in rulings:
            source = "ruling"
            row = {**row, **{k: v for k, v in rulings[key].items() if k != "key"}}
        elif judged(verdict(user.get(key))):
            source, row = "reviewer", user[key]
        else:
            source = "judge"
        final[key] = row
        settled_by[source] += 1
    pair_verdict = {
        key: "not_judged"
        if judge[key]["assertion_path"] in stopped or not judged(verdict(row))
        else verdict(row)
        for key, row in final.items()
    }
    free = [k for k in judge if judge[k]["assertion_path"] not in stopped]
    readers = Counter(
        1 + judged(verdict(second.get(key))) + judged(verdict(user.get(key)))
        for key in free
        if judged(verdict(judge[key]))
    )
    defects = [(k, final[k]) for k in judge if pair_verdict[k] == "defect"]
    upheld = sum(1 for k, _ in defects if verdict(judge[k]) == "defect")

    status_of = {}
    for path, arow in assertion_rows.items():
        levels = [pair_verdict[k] for k in pairs_of.get(path, [])]
        levels.append(assertion_verdict(arow))
        if path in stopped:
            status_of[path] = "not_judged"
        elif "defect" in levels:
            status_of[path] = "defect"
        elif "not_judged" in levels:
            status_of[path] = "not_judged"
        else:
            status_of[path] = "no_defect"
    level_rows = [
        (p, r)
        for p, r in assertion_rows.items()
        if p not in stopped and assertion_verdict(r) == "defect"
    ]

    opening = f"The labels were first opened on {first.get('opened_at')} under "
    opening += (
        "this freeze."
        if not reopened
        else f"another freeze (`{first.get('freeze_sha256')}`); this tally was run again "
        f"under a later one, for this stated reason: {reason_text(reopened)}"
    )
    older = meta.get("older_run_counts") or {}
    out = [
        f"# Tally: {meta.get('entry')} at {str(meta.get('pin', ''))[:11]}",
        "",
        f"FREEZE.txt sha256 `{freeze_sha}`. {opening}{keys_note} Frozen files:",
        "",
        *[f"- `{name}` `{digest}`" for name, digest in sorted(frozen.items())],
        "",
        (
            f"Frame: {len(judge)} pairs over {len(assertion_rows)} assertions; excluded "
            f"rows, judged by the human reviewer: {len(fenced)} pairs."
        ),
        "",
        (
            "Verdicts governing the frame's pairs: "
            + ", ".join(f"{name} {n}" for name, n in sorted(settled_by.items()))
            + f". Pairs the judge judged that one reader saw: {readers[1]}; two: "
            f"{readers[2]}; three: {readers[3]}. Of {len(defects)} pair defects, {upheld} "
            f"were recorded by the judge and {len(defects) - upheld} only by another reader."
        ),
        "",
        table(
            "The checker run the labels come from",
            ["measure", "value"],
            [
                ["run observed at", meta.get("checker_observed_at")],
                ["run marked complete", meta.get("checker_complete")],
                ["inputs the run observed", meta.get("observed_inputs")],
                [
                    "of those, placed on a pair at the pin",
                    meta.get("observed_inputs_placed"),
                ],
                [
                    "frame pairs the run assessed",
                    f"{meta.get('frame_pairs_assessed')} of {meta.get('frame_pairs')}",
                ],
                [
                    "inputs with more than one assessment record (latest used)",
                    meta.get("inputs_with_several_assessment_records"),
                ],
                [
                    "assessment records by model",
                    "; ".join(
                        f"{m} {n}"
                        for m, n in sorted((meta.get("checker_models") or {}).items())
                    ),
                ],
                [
                    FLAGGED_ROW,
                    meta.get("flagged_assertions_at_pin (mismatch, partial)"),
                ],
                *[[f"older run: {name}", value] for name, value in older.items()],
            ],
        ),
    ]

    answers_by_assertion = defaultdict(list)
    for key in judge:
        lab = labels[key]
        if lab.get("assessed"):
            answers_by_assertion[judge[key]["assertion_path"]].append(
                {a.get("label") for a in (lab.get("answers") or {}).values()}
            )
    assessed = set(answers_by_assertion)
    mismatch = {
        p
        for p, sets in answers_by_assertion.items()
        if "MISMATCH" in set().union(*sets)
    }
    partial = {
        p for p, sets in answers_by_assertion.items() if "PARTIAL" in set().union(*sets)
    }
    with_pairs = {path for path in assertion_rows if pairs_of.get(path)}
    groups = [
        ("flagged MISMATCH on any field", mismatch),
        ("flagged PARTIAL on any field", partial),
        ("not flagged", assessed - mismatch - partial),
        ("with pairs, none assessed by the checker", with_pairs - assessed),
        ("with no quote, so no pair for the checker", set(assertion_rows) - with_pairs),
    ]
    rows = []
    for name, paths in groups:
        c = Counter(status_of[p] for p in paths)
        rows.append([name, len(paths), c["defect"], c["no_defect"], c["not_judged"]])
    out.append(
        table(
            "1. Per assertion, in the issue's unit (the frame only; the first two rows overlap)",
            ["assertions", "n", "confirmed defect", "no defect", "not judged"],
            rows,
        )
    )

    by_label = defaultdict(Counter)
    for key in judge:
        lab = labels[key]
        whole = (lab.get("answers") or {}).get("/", {}).get("label")
        name = whole if lab.get("assessed") and whole else None
        by_label[
            name
            or ("not assessed" if not lab.get("assessed") else "no whole-claim answer")
        ][pair_verdict[key]] += 1
    rows = [
        [
            name,
            sum(c.values()),
            c["defect"],
            c["no_defect"],
            c["not_judged"],
            share(c["defect"], c["defect"] + c["no_defect"]),
        ]
        for name, c in sorted(by_label.items())
    ]
    out.append(
        table(
            "2. Per pair, by the checker's whole-claim verdict",
            [
                "whole-claim verdict",
                "pairs",
                "defect",
                "no defect",
                "not judged",
                "defect share of judged",
            ],
            rows,
        )
    )

    rows = [
        ["pair", "class", cls, n]
        for cls, n in sorted(Counter(defect_class(r) for _, r in defects).items())
    ]
    rows += [
        ["pair", "severity", s or "-", n]
        for s, n in sorted(Counter(norm(r.get("severity")) for _, r in defects).items())
    ]
    rows += [
        ["pair", "section", s, n]
        for s, n in sorted(
            Counter(section_of(judge[k]["assertion_path"]) for k, _ in defects).items()
        )
    ]
    rows += [
        ["assertion", "class", cls, n]
        for cls, n in sorted(Counter(defect_class(r) for _, r in level_rows).items())
    ]
    rows += [
        ["assertion", "severity", s or "-", n]
        for s, n in sorted(
            Counter(norm(r.get("severity")) for _, r in level_rows).items()
        )
    ]
    rows += [
        ["assertion", "section", s, n]
        for s, n in sorted(Counter(section_of(p) for p, _ in level_rows).items())
    ]
    out.append(
        table(
            "3. Defects by class, severity and section",
            ["level", "by", "value", "n"],
            rows,
        )
    )

    ranked = sorted(
        (
            (labels[k]["answers"]["/"].get("p_mismatch") or 0.0, k)
            for k in judge
            if labels[k].get("assessed") and "/" in (labels[k].get("answers") or {})
        ),
        key=lambda item: (-item[0], item[1]),
    )
    ranked_judged = [k for _, k in ranked if pair_verdict[k] != "not_judged"]
    base = sum(1 for k in ranked_judged if pair_verdict[k] == "defect")

    def group(keys: list[str]) -> list:
        hits = sum(1 for k in keys if pair_verdict[k] == "defect")
        seen = sum(1 for k in keys if pair_verdict[k] != "not_judged")
        return [len(keys), hits, share(hits, seen)]

    rows = []
    for cut in CUTOFFS:
        if len(judge) < 2 * cut:
            why = "not computed: the frame is smaller than twice the cut-off"
            rows.append([cut, why, *[""] * 10])
            continue
        if len(ranked) < cut:
            rows.append(
                [cut, "not computed: fewer ranked pairs than the cut-off", *[""] * 10]
            )
            continue
        threshold = ranked[cut - 1][0]
        above = [k for p, k in ranked if p > threshold]
        tied = [k for p, k in ranked if p == threshold]
        rows.append(
            [
                cut,
                threshold,
                *group(above),
                *group(tied),
                *group(above + tied),
                share(base, len(ranked_judged)),
            ]
        )
    out.append(
        table(
            "4. Confirmed defects among the checker's top pairs by whole-claim mismatch "
            "probability (ties at a cut-off are not broken)",
            [
                "cut-off",
                "probability at the cut-off",
                "pairs above it",
                "defects",
                "share of judged",
                "pairs tied at it",
                "defects",
                "share of judged",
                "above and tied",
                "defects",
                "share of judged",
                "base rate among ranked pairs",
            ],
            rows,
        )
    )

    rows = []
    for name, other in (("second reader", second), ("human reviewer", user)):
        both = [
            k
            for k in other
            if k in judge
            and judge[k]["assertion_path"] not in stopped
            and judged(verdict(judge[k]))
            and judged(verdict(other[k]))
        ]
        binary = sum(1 for k in both if verdict(judge[k]) == verdict(other[k]))
        plain = sum(
            1
            for k in both
            if verdict(judge[k]) == verdict(other[k])
            and (
                verdict(judge[k]) != "defect"
                or defect_class(judge[k]) == defect_class(other[k])
            )
        )
        rows.append(
            [
                name,
                len(other),
                len(both),
                plain,
                share(plain, len(both)),
                binary,
                share(binary, len(both)),
            ]
        )
    out.append(
        table(
            "5. Agreement with the first verdicts (pairs; the assertion level has one reader)",
            [
                "against",
                "sample",
                "both judged",
                "same verdict and class",
                "share",
                "same defect-or-not",
                "share",
            ],
            rows,
        )
    )

    c = Counter(verdict(r) for r in fenced)
    out.append(
        table(
            "Excluded rows, from the human reviewer's sheet (pairs only)",
            ["pairs", "defect", "no defect", "not judged"],
            [[len(fenced), c["defect"], c["no_defect"], c["not_judged"]]],
        )
    )
    out.append(
        "Tables 6 and 7 of the README (before and after the repairs; what was done) are "
        "not computed by this version of the script: they need the repair pull requests "
        "and a checker run made after them.\n"
    )

    text = "\n".join(out)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
