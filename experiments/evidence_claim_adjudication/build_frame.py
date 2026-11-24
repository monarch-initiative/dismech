"""Build the frame of one evidence-claim adjudication run (README.md, "The blind procedure").

Takes the entry as it stood at a pinned commit, lists its claim-and-quote pairs with the
checker's own extractor (a dry run: no checker call, nothing written in the checkout),
gives every pair a key, and writes three kinds of output:

* ``--frame-keys`` (committed): one row per pair of the frame, with its key, section,
  assertion path, evidence path, reference and hash. No claim text, no quote text, no
  verdict and no label.
* ``--out`` (the run folder, kept outside the repository): the judge's sheets; the two
  samples (each sampled pair with the other quotes on its row and on the rows nested in
  it, which ``worklist.py`` shows the judge as well); the excluded rows' sheet;
  ``rubric.md``, the README sections a reader needs in order to judge, so that no reader
  has to open the README, whose other sections discuss the checker's output; and
  ``frame_index.json``, the keys, assertion paths and samples of the frame, which
  ``tally.py`` checks the sheets against. Nothing in the folder comes from the checker.
* ``--sealed`` (a separate folder, also outside the repository, which no judging session
  opens): the checker's labels keyed to the frame, and ``frame_meta.json``, which holds
  every count taken from a checker file. The folder is created readable by its owner
  only; make it unreadable (``chmod 000``) once the build is done.

Both folders must lie outside any git checkout, the checker files must sit inside the
sealed folder, the run folder may hold nothing this script and the readers did not write,
and a run must name its excluded rows with ``--exclude`` or say ``--no-exclusions``. A run
folder that already carries a verdict is never rebuilt. The script prints pair counts from
the extractor and a yes or no for each check. It prints no label, no probability, nothing
from the excluded rows and no count taken from a checker file: those go to
``frame_meta.json`` only. Of the checker file's coverage it prints only whether at least
half of the frame's pairs carry an assessment in it, and the build stops if fewer do. If a
check fails it writes nothing, and the sealed record is written before the run folder.

A checker input is matched to a frame pair on assertion path, evidence path and quote text,
never on the claim hash. The paths are the ones the checker run itself recorded when it
last saw the input (its ``occurrences``), not the path where the input was first seen,
which goes stale when rows move. Only inputs the run observed are matched: a saved run
keeps inputs from earlier runs marked active after the row they came from has changed, so
"active" alone over-counts. Where the checker holds more than one response for an input,
the latest by time is used; ``frame_meta.json`` records how many inputs that concerns.

Usage (run from the repository root, with the package importable):

    python experiments/evidence_claim_adjudication/build_frame.py \\
        --entry kb/disorders/Neuroblastoma.yaml --pin <sha> \\
        --checker-file <sealed folder>/<run at the pin> \\
        --old-checker-file <sealed folder>/<earlier run> \\
        --out <run folder> --sealed <sealed folder> --seed <n> \\
        --exclude treatments=<row name> ... --contains <commit> ...
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent

EVIDENCE_COLUMNS = [
    "reference",
    "reference_title",
    "evidence_source",
    "quote_role",
    "directness",
    "supports",
    "explanation",
]
PAIR_VERDICT_COLUMNS = [
    "q1_claim_right",
    "q2_direction_right",
    "q3_quote_bears",
    "q4_term_level",
    "defect_class",
    "severity",
    "proposed_repair",
    "opened_source",
    "note",
]
ASSERTION_VERDICT_COLUMNS = [
    "clauses_covered",
    "uncovered_clauses",
    "defect_class",
    "severity",
    "proposed_repair",
    "note",
]
PAIR_COLUMNS = [
    "key",
    "batch",
    "section",
    "assertion_path",
    "evidence_path",
    "assertion_type",
    "claim",
    "quote",
    *EVIDENCE_COLUMNS,
    *PAIR_VERDICT_COLUMNS,
]
SAMPLE_COLUMNS = [
    *PAIR_COLUMNS[: -len(PAIR_VERDICT_COLUMNS)],
    "other_quotes_on_row",
    *PAIR_VERDICT_COLUMNS,
]
ASSERTION_COLUMNS = [
    "assertion_path",
    "batch",
    "section",
    "assertion_type",
    "pairs",
    "keys",
    "claim",
    *ASSERTION_VERDICT_COLUMNS,
]
SHEET_FILES = [
    "judge_sheet.csv",
    "assertion_sheet.csv",
    "fenced_sheet.csv",
    "second_look_sheet.csv",
    "user_sample_sheet.csv",
]
RUN_FILES = [*SHEET_FILES, "frame_index.json", "rubric.md"]
# Files a run adds to its folder after the build: the second reader's verdicts, the
# reviewer's rulings and the two freeze records.
LATER_FILES = [
    "second_look_verdicts.csv",
    "rulings.csv",
    "BLIND.txt",
    "PREFREEZE.txt",
    "FREEZE.txt",
]
SEALED_FILES = ["checker_labels.json", "frame_meta.json"]
# The README sections a reader needs in order to judge. Its introduction and its account
# of the calibration are left out of the readers' copy: they discuss the checker's output.
RUBRIC_SECTIONS = [
    "The unit: two levels",
    "Who judges",
    "The four questions",
    "Defect classes and severities",
    "What is not a defect",
    "Worked examples",
    "What is left out, and how it is counted",
    "Filling in the sheets",
]

# The five judging batches of the plan, by top-level section. Pathophysiology rows are
# split: the mechanism nodes themselves go first, the edges and anything else nested
# under a node go with the hypotheses and models.
BATCH_OF_SECTION = {
    "mechanistic_hypotheses": 2,
    "discussions": 2,
    "experimental_models": 2,
    "animal_models": 2,
    "computational_models": 2,
    "datasets": 2,
    "treatments": 3,
    "clinical_trials": 3,
    "diagnosis": 3,
    "imaging_findings": 3,
    "genetic": 4,
    "has_subtypes": 4,
    "prevalence": 4,
    "stages": 4,
    "epidemiology": 4,
    "inheritance": 4,
    "progression": 4,
    "classifications": 4,
    "differential_diagnoses": 5,
    "phenotypes": 5,
    "histopathology": 5,
    "biochemical": 5,
}
NAME_KEYS = ("name", "preferred_term", "target", "hypothesis_label", "discussion_id")


def batch_of(assertion_path: str) -> int:
    parts = assertion_path.strip("/").split("/")
    if parts[0] == "pathophysiology":
        return 1 if len(parts) == 2 else 2
    return BATCH_OF_SECTION.get(parts[0], 4)


def norm(text) -> str:
    return " ".join(str(text or "").split())


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, check=True
    ).stdout


def resolve(document, path: str):
    node = document
    for part in path.strip("/").split("/"):
        node = node[int(part)] if isinstance(node, list) else node[part]
    return node


def dump(body) -> str:
    return yaml.safe_dump(body, sort_keys=False, allow_unicode=True, width=100).strip()


def claim_text(claim: dict) -> str:
    body = {}
    context = (claim.get("about") or {}).get("context")
    if context:
        body["context"] = context
    if "assertion" in claim:
        body["row"] = claim["assertion"]
    else:
        body["row"] = {
            k: v for k, v in claim.items() if k not in ("selected_evidence", "about")
        }
    return dump(body)


def without_evidence(node):
    """The row with every evidence block removed, at any depth: nested rows are assertions
    of their own, and their quotes belong on their own pairs."""
    if isinstance(node, dict):
        return {k: without_evidence(v) for k, v in node.items() if k != "evidence"}
    if isinstance(node, list):
        return [without_evidence(v) for v in node]
    return node


def ancestors_of(document, path: str) -> list[str]:
    """Names of the rows a nested row sits in, outermost first, so that a row shown on its
    own can still be read in place."""
    parts = path.strip("/").split("/")
    names, node = [], document
    for depth, part in enumerate(parts[:-1]):
        node = node[int(part)] if isinstance(node, list) else node[part]
        if isinstance(node, dict):
            label = next((str(node[k]) for k in NAME_KEYS if node.get(k)), None)
            if label:
                names.append(f"/{'/'.join(parts[: depth + 1])}: {label}")
    return names


def assertion_text(document, path: str) -> str:
    body = {}
    context = ancestors_of(document, path)
    if context:
        body["context"] = context
    body["row"] = without_evidence(resolve(document, path))
    return dump(body)


def named_paths(node) -> set[str]:
    """Every row path a claim names, at any depth: the extractor puts the rows a claim
    binds (its context, a subtype or hypothesis row, an edge's endpoints and scope) under
    ``path`` or ``document_path`` keys."""
    found = set()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in ("path", "document_path") and isinstance(value, str):
                found.add(value)
            else:
                found |= named_paths(value)
    elif isinstance(node, list):
        for value in node:
            found |= named_paths(value)
    return found


def context_paths(sample: list[dict], assertion_rows: list[dict]) -> list[str]:
    """The rows a reader sees beside each sampled pair in its claim column: the rows it is
    nested in, and the rows its claim names (a subtype or hypothesis row, an edge's
    endpoints and scope). tally.py holds problems on them while the reviewer's sample is
    unlocked."""
    paths = {a["assertion_path"] for a in assertion_rows}
    found = set()
    for p in sample:
        found.update(a for a in paths if p["assertion_path"].startswith(a + "/"))
        found.update(paths & set(p.get("_named", ())))
    return sorted(found)


def load_yaml_quietly(path: Path):
    """Parse a checker file without letting a parser error echo one of its lines."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (yaml.YAMLError, UnicodeDecodeError):
        data = None
    if not isinstance(data, dict):
        sys.exit(
            f"{path.name} could not be read as a checker file; the parser's message is "
            "withheld because it can quote a label"
        )
    return data


def latest_response(record: dict) -> dict:
    """The response the checker itself reports for an assessment record.

    The checker's cache keeps a record's earliest response at its top level and any later
    ones, in time order, under ``reassessments``; its own lookup returns the last of them.
    """
    later = record.get("reassessments") or []
    return later[-1] if later else record


def load_checker(path: Path):
    data = load_yaml_quietly(path)
    # The entry a checker file is about is named at its top level, beside the inventory.
    inventory = {
        **(data.get("inventory") or {}),
        "source_file": data.get("source_file"),
    }
    observed = str(inventory.get("observed_at"))
    latest: dict[str, dict] = {}
    models = Counter()
    records = Counter()
    for record in (data.get("assessments") or {}).values():
        h = record.get("input_sha256")
        response = latest_response(record)
        if h not in latest or str(response.get("assessed_at")) > str(
            latest[h].get("assessed_at")
        ):
            latest[h] = response
        models[str(record.get("model"))] += 1
        records[h] += 1
    active = {h: v for h, v in (data.get("inputs") or {}).items() if v.get("active")}
    # An input first assessed during the run carries a later last_seen_at than the run's
    # observed_at, so the test is "at or after", not equality.
    seen = {h: v for h, v in active.items() if str(v.get("last_seen_at")) >= observed}
    several = sum(1 for h in seen if records[h] > 1)
    return inventory, active, seen, latest, dict(models), several


def input_places(value: dict) -> list[tuple[str, str]]:
    """Where the checker run saw an input: the occurrences it refreshes on every run. The
    first-seen ``origin`` is used only when a file carries no occurrences."""
    places = [
        (o.get("assertion_path", ""), o.get("evidence_path", ""))
        for o in value.get("occurrences") or []
    ]
    if not places:
        origin = value.get("origin") or {}
        places = [(origin.get("assertion_path", ""), origin.get("evidence_path", ""))]
    return places


def input_quote(value: dict) -> str:
    return norm(
        ((value.get("claim") or {}).get("selected_evidence") or {}).get("snippet")
    )


def answers_of(response) -> dict:
    answers = ((response or {}).get("result") or {}).get("answers") or {}
    return {
        path: {
            "label": answer.get("label"),
            "p_mismatch": (answer.get("probabilities") or {}).get("MISMATCH"),
        }
        for path, answer in answers.items()
    }


def flagged_assertions(inputs: dict, latest: dict) -> tuple[int, int]:
    """The issue's rule: MISMATCH (or PARTIAL) on any field, counted per assertion path."""
    mismatch, partial = set(), set()
    for h, value in inputs.items():
        if h not in latest:
            continue
        labels = {a["label"] for a in answers_of(latest[h]).values()}
        for path, _ in input_places(value):
            if "MISMATCH" in labels:
                mismatch.add(path)
            if "PARTIAL" in labels:
                partial.add(path)
    return len(mismatch), len(partial)


def excluded_prefixes(document: dict, specs: list[str]) -> list[str]:
    prefixes, missing = [], []
    for spec in specs:
        section, _, name = spec.partition("=")
        rows = document.get(section) or []
        hits = [
            i
            for i, row in enumerate(rows)
            if isinstance(row, dict) and row.get("name") == name
        ]
        if len(hits) == 1:
            prefixes.append(f"/{section}/{hits[0]}")
        else:
            missing.append(spec)
    if missing:
        sys.exit(f"--exclude matched no single row for: {', '.join(missing)}")
    return prefixes


def is_excluded(path: str, prefixes: list[str]) -> bool:
    return any(path == p or path.startswith(p + "/") for p in prefixes)


def stratified_sample(rng: random.Random, items: list[dict], n: int) -> list[dict]:
    """Proportional allocation by section (largest remainder), random within section."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        groups[item["section"]].append(item)
    n = min(n, len(items))
    quotas = {g: n * len(v) / len(items) for g, v in groups.items()}
    allocation = {g: int(q) for g, q in quotas.items()}
    remainder = n - sum(allocation.values())
    for g in sorted(groups, key=lambda g: (-(quotas[g] - allocation[g]), g))[
        :remainder
    ]:
        allocation[g] += 1
    chosen = []
    for g in sorted(groups):
        pool = sorted(groups[g], key=lambda item: item["key"])
        chosen.extend(rng.sample(pool, allocation[g]))
    return sorted(chosen, key=lambda item: item["order"])


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in columns})


def checkout_holding(path: Path) -> str | None:
    """The git checkout a folder would sit in, if any; a path inside a ``.git`` directory
    counts as inside one."""
    probe = path.resolve()
    if ".git" in probe.parts:
        return str(Path(*probe.parts[: probe.parts.index(".git")]))
    while not probe.exists():
        probe = probe.parent
    result = subprocess.run(
        ["git", "-C", str(probe), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def run_extractor(entry_copy: Path, workdir: Path) -> tuple[list[dict], dict]:
    output = workdir / "out"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "dismech.classifier.audit",
            "--dry-run",
            "--input",
            str(entry_copy),
            "--output",
            str(output),
            "--cache",
            str(workdir / "cache"),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    rows = [
        json.loads(line)
        for line in (output / "inventory.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    return rows, manifest


def yes(value: bool) -> str:
    return "yes" if value else "NO"


def rubric_extract(readme: Path) -> str:
    """The README sections a reader needs in order to judge, word for word. The README's
    introduction and its account of the calibration are left out, because they discuss the
    checker's output."""
    sections: dict[str, list[str]] = {}
    title = None
    for line in readme.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("## "):
            title = line[3:].strip()
            sections[title] = []
        if title:
            sections[title].append(line)
    missing = [name for name in RUBRIC_SECTIONS if name not in sections]
    if missing:
        sys.exit(f"README.md has no section named: {', '.join(missing)}")
    head = (
        "# Rubric for the readers of this run\n\n"
        "An extract of `experiments/evidence_claim_adjudication/README.md`, written by "
        "`build_frame.py`: the sections a reader needs in order to judge, word for word, "
        "and nothing else. Links in it point into the repository and are not for the "
        "readers to follow.\n\n"
    )
    return head + "".join("".join(sections[name]) for name in RUBRIC_SECTIONS)


def filled_verdicts(folder: Path) -> list[str]:
    """Sheets in a run folder that already carry a verdict, and files a run writes later."""
    found = [name for name in LATER_FILES if (folder / name).exists()]
    verdict_columns = set(PAIR_VERDICT_COLUMNS) | set(ASSERTION_VERDICT_COLUMNS)
    for name in SHEET_FILES:
        path = folder / name
        if not path.is_file():
            continue
        with path.open(encoding="utf-8-sig", newline="") as stream:
            for row in csv.DictReader(stream):
                if any(norm(row.get(c)) for c in verdict_columns):
                    found.append(name)
                    break
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--entry", required=True, help="entry path inside the repository"
    )
    parser.add_argument("--pin", required=True, help="commit the frame is built at")
    parser.add_argument(
        "--checker-file",
        required=True,
        type=Path,
        help="checker run at the pin, kept inside the sealed folder",
    )
    parser.add_argument(
        "--old-checker-file",
        type=Path,
        help="an earlier checker run of the same entry, kept inside the sealed folder",
    )
    parser.add_argument(
        "--out", required=True, type=Path, help="run folder outside the repo"
    )
    parser.add_argument(
        "--sealed",
        required=True,
        type=Path,
        help="folder for the checker's labels and counts, apart from the run folder",
    )
    parser.add_argument("--frame-keys", type=Path, help="where to write frame_keys.tsv")
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--second-look", type=int, default=120)
    parser.add_argument("--user-sample", type=int, default=30)
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="SECTION=ROW NAME of an excluded row",
    )
    parser.add_argument(
        "--no-exclusions",
        action="store_true",
        help="build a frame with no excluded rows, deliberately",
    )
    parser.add_argument(
        "--contains", action="append", default=[], help="a commit the pin must contain"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite a run folder that holds no verdict yet",
    )
    args = parser.parse_args()

    repo = Path(git(Path.cwd(), "rev-parse", "--show-toplevel").strip())
    frame_keys = args.frame_keys or HERE / Path(args.entry).stem / "frame_keys.tsv"
    if bool(args.exclude) == args.no_exclusions:
        sys.exit("name the excluded rows with --exclude, or say --no-exclusions")
    out, sealed = args.out.resolve(), args.sealed.resolve()
    for name, folder in (("--out", out), ("--sealed", sealed)):
        top = checkout_holding(folder)
        if top:
            sys.exit(
                f"{name} lies inside the git checkout at {top}; it holds claim and quote "
                "text or labels and must stay outside every checkout"
            )
    if out == sealed or out in sealed.parents or sealed in out.parents:
        sys.exit(
            "--out and --sealed must be separate folders, neither inside the other"
        )
    if sealed.is_dir() and not os.access(sealed, os.R_OK | os.W_OK | os.X_OK):
        sys.exit(
            f"{sealed} cannot be read. It is kept closed (chmod 000) between uses: reopen "
            "it with chmod 700 to rebuild, and close it again afterwards."
        )
    for f in (args.checker_file, args.old_checker_file):
        if f and sealed not in f.resolve().parents:
            sys.exit(
                f"{f.name} is not inside --sealed; a checker file is kept there and "
                "nowhere else"
            )
    if out.exists():
        known = set(RUN_FILES) | set(LATER_FILES)
        strays = sorted(
            p.name
            for p in out.iterdir()
            if p.name not in known or p.is_symlink() or not p.is_file()
        )
        if strays:
            sys.exit(
                f"--out holds {', '.join(strays)}, which this script did not write; a "
                "run folder holds its sheets and nothing else"
            )
        judged_already = filled_verdicts(out)
        if judged_already:
            sys.exit(
                f"refusing to rebuild: {', '.join(judged_already)} already carry "
                "verdicts or were written after judging began; build into a fresh "
                "folder instead"
            )
    existing = [f"{out / n}" for n in RUN_FILES if (out / n).exists()] + [
        f"{sealed / n}" for n in SEALED_FILES if (sealed / n).exists()
    ]
    if existing and not args.force:
        sys.exit(f"refusing to overwrite {', '.join(existing)}")

    pin = git(repo, "rev-parse", "--verify", f"{args.pin}^{{commit}}").strip()
    entry_bytes = subprocess.run(
        ["git", "show", f"{pin}:{args.entry}"],
        cwd=repo,
        capture_output=True,
        check=True,
    ).stdout
    entry_sha = sha256_bytes(entry_bytes)
    document = yaml.safe_load(entry_bytes.decode("utf-8"))
    print(f"pin {pin} | {args.entry} sha256 {entry_sha}")

    checks = {}
    for commit in args.contains:
        inside = (
            subprocess.run(
                ["git", "merge-base", "--is-ancestor", commit, pin],
                cwd=repo,
                check=False,
            ).returncode
            == 0
        )
        checks[f"pin contains {commit}"] = inside

    inventory, active, seen, latest, models, several = load_checker(args.checker_file)
    entry_name = Path(args.entry).name
    checks["checker run is of this entry"] = (
        str(inventory.get("source_file")) == args.entry
    )
    checks["checker run read the pin"] = str(inventory.get("source_revision")) == pin
    checks["entry bytes match the checker run"] = (
        str(inventory.get("source_sha256")) == entry_sha
    )
    checks["checker run observed at least one input"] = bool(seen)

    with tempfile.TemporaryDirectory() as tmp:
        entry_copy = Path(tmp) / entry_name
        entry_copy.write_bytes(entry_bytes)
        rows, manifest = run_extractor(entry_copy, Path(tmp))
    statuses = Counter(r["status"] for r in rows)
    print(
        f"extractor: classifier_sha256 {manifest.get('classifier_sha256', '')[:16]}; "
        f"rows {len(rows)} {dict(statuses)}"
    )

    prefixes = excluded_prefixes(document, args.exclude)
    by_key = defaultdict(set)
    for h, value in seen.items():
        quote = input_quote(value)
        for assertion_path, evidence_path in input_places(value):
            by_key[(assertion_path, evidence_path, quote)].add(h)

    pairs, excluded, no_quote, other = [], [], [], []
    for order, row in enumerate(rows):
        if row["status"] == "no_evidence":
            no_quote.append(dict(row, order=order))
            continue
        if row["status"] != "ready":
            other.append(dict(row, order=order))
            continue
        claim = row["claim"]
        quote = row.get("snippet") or ""
        digest = sha256_bytes(
            json.dumps(
                {"claim": claim, "quote": quote}, sort_keys=True, ensure_ascii=False
            ).encode("utf-8")
        )
        evidence = claim.get("selected_evidence") or {}
        # For relationship edges the extractor keeps only snippet, supports and directness
        # in the claim and moves the rest of the evidence item to evidence_annotations.
        annotations = row.get("evidence_annotations") or {}
        record = {
            "order": order,
            "key": f"{row['evidence_path']}#{digest[:12]}",
            "hash": digest,
            "batch": batch_of(row["assertion_path"]),
            "section": row["section"],
            "assertion_path": row["assertion_path"],
            "evidence_path": row["evidence_path"],
            "assertion_type": row.get("assertion_type", ""),
            "claim": claim_text(claim),
            "quote": quote,
            **{
                c: evidence.get(c) or annotations.get(c) or row.get(c) or ""
                for c in EVIDENCE_COLUMNS
            },
        }
        matches = sorted(
            by_key.get((row["assertion_path"], row["evidence_path"], norm(quote)), ())
        )
        record["_input"] = matches[0] if len(matches) == 1 else None
        record["_ambiguous"] = len(matches) > 1
        # The rows the claim names, which the claim column then shows beside the pair.
        record["_named"] = sorted(named_paths(claim))
        (excluded if is_excluded(row["assertion_path"], prefixes) else pairs).append(
            record
        )

    assessed = sum(1 for p in pairs if p["_input"] and p["_input"] in latest)
    ambiguous = sum(1 for p in pairs + excluded if p["_ambiguous"])
    placed = {p["_input"] for p in pairs + excluded if p["_input"]}
    excluded_no_quote = [
        r for r in no_quote if is_excluded(r["assertion_path"], prefixes)
    ]
    checks[
        "at least half of the frame's pairs carry an assessment in the checker file"
    ] = 2 * assessed >= len(pairs) > 0
    checks["every observed input placed on a pair"] = placed == set(seen)
    checks["no ambiguous match"] = ambiguous == 0
    checks["no row with another extractor status"] = not other
    checks["keys are unique"] = len({p["key"] for p in pairs + excluded}) == len(
        pairs + excluded
    )
    print(
        f"frame: {len(pairs)} pairs; excluded rows: {len(prefixes)} rows, {len(excluded)} "
        f"pairs, {len(excluded_no_quote)} rows with no quote; other rows with no quote: "
        f"{len(no_quote) - len(excluded_no_quote)}; other statuses: {len(other)}"
    )
    batches = Counter(p["batch"] for p in pairs)
    print("batches (pairs):", ", ".join(f"{b}: {batches[b]}" for b in sorted(batches)))

    issue_counts = {}
    if args.old_checker_file:
        old_inventory, old_active, old_seen, old_latest, _, _ = load_checker(
            args.old_checker_file
        )
        checks["older checker run is of this entry"] = (
            str(old_inventory.get("source_file")) == args.entry
        )
        issue_counts = {
            "observed_at": str(old_inventory.get("observed_at")),
            "observed in that run (mismatch, partial)": flagged_assertions(
                old_seen, old_latest
            ),
            "all active inputs (mismatch, partial)": flagged_assertions(
                old_active, old_latest
            ),
        }
    for name, passed in checks.items():
        label = (
            f"pin contains {name[13:24]}" if name.startswith("pin contains") else name
        )
        print(f"check: {label}: {yes(passed)}")
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        print("FAILED: " + "; ".join(failed) + ". Nothing was written.")
        return 1

    rng = random.Random(args.seed)
    second = stratified_sample(rng, pairs, args.second_look)
    user = stratified_sample(rng, second, args.user_sample)

    assertions: dict[str, dict] = {}
    for p in pairs:
        a = assertions.setdefault(
            p["assertion_path"],
            {
                "order": p["order"],
                "assertion_path": p["assertion_path"],
                "batch": p["batch"],
                "section": p["section"],
                "assertion_type": p["assertion_type"],
                "claim": p["claim"],
                "keys": [],
            },
        )
        a["keys"].append(p["key"])
    for row in no_quote:
        if is_excluded(row["assertion_path"], prefixes):
            continue
        assertions.setdefault(
            row["assertion_path"],
            {
                "order": row["order"],
                "assertion_path": row["assertion_path"],
                "batch": batch_of(row["assertion_path"]),
                "section": row["section"],
                "assertion_type": row.get("assertion_type", ""),
                "claim": assertion_text(document, row["assertion_path"]),
                "keys": [],
            },
        )
    assertion_rows = sorted(assertions.values(), key=lambda a: a["order"])
    for a in assertion_rows:
        a["pairs"] = len(a["keys"])
        a["keys"] = " ".join(a["keys"])

    def with_row_context(sample: list[dict]) -> list[dict]:
        """Each sampled pair with the other quotes on its row and those on the rows nested
        in it, which worklist.py shows the judge as well."""
        result = []
        for p in sample:
            row = p["assertion_path"]
            others = [
                o
                for o in pairs
                if o["key"] != p["key"]
                and (
                    o["assertion_path"] == row
                    or o["assertion_path"].startswith(row + "/")
                )
            ]
            result.append(
                dict(
                    p,
                    other_quotes_on_row="\n\n".join(
                        f"{o['evidence_path']} | {o['reference']} | {o['quote']}"
                        for o in others
                    ),
                )
            )
        return result

    # Everything is prepared in memory first, and the sealed record is written before the
    # run folder, so that sheets never exist without the record of how they were made.
    labels = {}
    for p in pairs + excluded:
        h = p["_input"]
        labels[p["key"]] = {
            "assertion_path": p["assertion_path"],
            "evidence_path": p["evidence_path"],
            "excluded": p in excluded,
            "assessed": bool(h and h in latest),
            "input_sha256": h,
            "assessed_at": (latest.get(h) or {}).get("assessed_at") if h else None,
            "answers": answers_of(latest.get(h)) if h else {},
        }
    labels_bytes = (
        json.dumps(labels, indent=1, ensure_ascii=False, default=str) + "\n"
    ).encode("utf-8")
    index = {
        "entry": args.entry,
        "pin": pin,
        "pairs": [[p["key"], p["assertion_path"]] for p in pairs],
        "assertions": [[a["assertion_path"], a["pairs"]] for a in assertion_rows],
        "second_look_keys": [p["key"] for p in second],
        "user_sample_keys": [p["key"] for p in user],
        "user_sample_context_paths": context_paths(user, assertion_rows),
        "excluded_keys": [p["key"] for p in excluded],
    }
    index_bytes = (json.dumps(index, indent=1) + "\n").encode("utf-8")
    keys_text = "".join(
        "\t".join(row) + "\n"
        for row in [
            ["key", "section", "assertion_path", "evidence_path", "reference", "hash"],
            *[
                [
                    p["key"],
                    p["section"],
                    p["assertion_path"],
                    p["evidence_path"],
                    p["reference"],
                    p["hash"],
                ]
                for p in pairs
            ],
        ]
    )
    rubric = rubric_extract(HERE / "README.md")
    meta = {
        "created_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "entry": args.entry,
        "pin": pin,
        "entry_sha256": entry_sha,
        "run_folder": str(out),
        "checker_file": str(args.checker_file),
        "checker_file_sha256": sha256_bytes(args.checker_file.read_bytes()),
        "checker_observed_at": str(inventory.get("observed_at")),
        "checker_complete": inventory.get("complete"),
        "checker_models": models,
        "inputs_with_several_assessment_records": several,
        "old_checker_file": str(args.old_checker_file or ""),
        "old_checker_file_sha256": (
            sha256_bytes(args.old_checker_file.read_bytes())
            if args.old_checker_file
            else ""
        ),
        "extractor_classifier_sha256": manifest.get("classifier_sha256"),
        "extractor_schema_sha256": manifest.get("schema_sha256"),
        "extractor_statuses": dict(statuses),
        "exclusions": args.exclude,
        "frame_pairs": len(pairs),
        "frame_assertions": len(assertion_rows),
        "excluded_rows": len(prefixes),
        "excluded_pairs": len(excluded),
        "excluded_rows_with_no_quote": len(excluded_no_quote),
        "rows_with_no_quote": len(no_quote),
        "frame_pairs_assessed": assessed,
        "active_inputs": len(active),
        "observed_inputs": len(seen),
        "observed_inputs_placed": len(placed),
        "ambiguous_matches": ambiguous,
        "batches": {str(b): batches[b] for b in sorted(batches)},
        "flagged_assertions_at_pin (mismatch, partial)": flagged_assertions(
            seen, latest
        ),
        "older_run_counts": issue_counts,
        "seed": args.seed,
        "checks": checks,
        "frame_keys_sha256": sha256_bytes(keys_text.encode("utf-8")),
        "frame_index_sha256": sha256_bytes(index_bytes),
        "rubric_sha256": sha256_bytes(rubric.encode("utf-8")),
        "readme_sha256": sha256_bytes((HERE / "README.md").read_bytes()),
        "checker_labels_sha256": sha256_bytes(labels_bytes),
        "script_sha256": sha256_bytes(Path(__file__).read_bytes()),
    }

    sealed.mkdir(parents=True, exist_ok=True)
    sealed.chmod(0o700)
    for name, data in (
        ("checker_labels.json", labels_bytes),
        (
            "frame_meta.json",
            (json.dumps(meta, indent=2, default=str) + "\n").encode("utf-8"),
        ),
    ):
        (sealed / name).write_bytes(data)
        (sealed / name).chmod(0o600)

    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "judge_sheet.csv", PAIR_COLUMNS, pairs)
    write_csv(out / "assertion_sheet.csv", ASSERTION_COLUMNS, assertion_rows)
    write_csv(out / "fenced_sheet.csv", PAIR_COLUMNS, excluded)
    write_csv(out / "second_look_sheet.csv", SAMPLE_COLUMNS, with_row_context(second))
    write_csv(out / "user_sample_sheet.csv", SAMPLE_COLUMNS, with_row_context(user))
    (out / "frame_index.json").write_bytes(index_bytes)
    (out / "rubric.md").write_text(rubric, encoding="utf-8")

    frame_keys.parent.mkdir(parents=True, exist_ok=True)
    frame_keys.write_text(keys_text, encoding="utf-8")

    print(f"samples: second look {len(second)}, user {len(user)} (seed {args.seed})")
    print(
        f"wrote {frame_keys}, {len(RUN_FILES)} files in {out} and "
        f"{len(SEALED_FILES)} files in {sealed}"
    )
    print(
        f"now seal the labels: chmod 000 '{sealed}' (reopen it only to rebuild or to tally)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
