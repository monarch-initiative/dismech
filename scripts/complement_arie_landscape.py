#!/usr/bin/env python3
"""Parse the Complement-ARIE Landscape Analysis Q&A export into tables.

The NIH Common Fund Complement-ARIE Landscape Analysis (29 Feb 2024) put 19
questions to a corpus of ~3,000 papers. Its Tableau dashboard exports the
answers as ``Q&A-Question Details_data.csv``: UTF-16LE, tab-separated, one
row per (paper, question). That file is ~128 MB, over GitHub's per-file limit,
so it is not committed; ``data/complement-arie/MANIFEST.yaml`` pins it by sha256.

This script reads it and writes three derived files beside it:

``papers.tsv``
    One row per citation key: accession, PMID, DOI, title, and flags for the
    edge cases below.
``answers.jsonl``
    One JSON object per (paper, question) with the answer text.
``questions.tsv``
    One row per question: its short name, full wording, and how many papers
    have a content answer or an ``NA`` answer to it.

Edge cases in the export, all handled deterministically:

* **Grouped keys.** A few ``Author et al. YEAR (NA)`` keys group several
  papers into one Tableau mark; their DOI and abstract read ``*``. They are
  kept in ``papers.tsv`` with ``merged_key=1`` and their answers are left out,
  because an answer cannot be traced to one paper.
* **Abstract alignment.** The ``Abstract`` column does not always line up
  with its row; the answers follow the title and PMID. It is not written out.
  ``abstract_shared=1`` marks papers whose abstract text also appears on
  another key, which is the case that can be detected mechanically. Fetch
  abstracts by PMID or DOI instead.
* **Character encoding.** UTF-8 text read as Windows-1252 (``naÃ¯ve``) is
  converted back run by run, so a field mixing both is still converted.
* **First-page text as title.** Some titles hold the text of the PDF's first
  page (journal citation, DOI, "REVIEW ARTICLE", "Check for updates") with
  the title inside it. A title with a line break or one of those markers is
  moved to ``title_page_header``, on one line, and ``title`` is left empty:
  take the title from the PMID or DOI. ``TITLE_PREFIX_CORRECTIONS`` handles
  the few that no general rule can separate.
* **Papers without answers.** Some keys have ``NA`` for every question. They
  are marked ``no_content=1``.
* **NA placeholders.** ``NA`` titles, ``https://doi.org/NA`` and answers that
  begin ``NA`` are emitted as empty / ``answer_is_na``.

Usage:
    python scripts/complement_arie_landscape.py
    python scripts/complement_arie_landscape.py --input PATH --out-dir DIR
"""

from __future__ import annotations

import argparse
import collections
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "complement-arie"
DEFAULT_INPUT = DATA_DIR / "Q&A-Question Details_data.csv"

COL_KEY = "Short Citation (Accession Number)"
COL_QUESTION = "Question Column Name"
COL_QUESTION_FULL = "Question Full"
COL_ABSTRACT = "Abstract"
COL_DOI = "DOI URL"
COL_TITLE = "Title"
COL_ANSWER = "TOOLTIP: Answer Detailed"
EXPECTED_COLUMNS = [
    COL_KEY, COL_QUESTION, "Answer-simple", COL_ABSTRACT, COL_DOI,
    COL_QUESTION_FULL, COL_TITLE, "TOOLTIP-Answer Simple", COL_ANSWER,
]

KEY_RE = re.compile(r"^(?P<authors>.+?) (?P<year>\d{4}[a-z]?) \((?P<accession>[^()]+)\)$")
MERGED = "*"
NA_DOI = "https://doi.org/NA"
NA_ANSWER_RE = re.compile(r"^\W*NA\b")
# Text found on a PDF's first page but never in a title.
PAGE_HEADER_RE = re.compile(
    r"https?://|doi\.org/|Check for updates|CrossMark|Contents lists available"
    r"|\(\d{4}\) \d+:\s?[\de]",  # journal citation, e.g. "(2022) 126:523" or "(2023) 9:e15556"
    re.IGNORECASE,
)
# An article-type banner printed above the title. Case-sensitive, so a title
# that merely begins "Review of ..." is left alone.
BANNER_RE = re.compile(r"^(?:INVITED |MINI[- ]|ORIGINAL |RESEARCH |SHORT |BRIEF )?(?:REVIEW|ARTICLE|PAPER|COMMUNICATION|REPORT)(?: ARTICLE| PAPER)?\b")

# Per-paper title corrections that no general rule can make safely: the
# leading text is a journal logo, but stripping leading capitals in general
# would also strip real acronyms (FDA, BRAF, PDMS). Each entry is checked, so
# one that stops matching the export fails loudly instead of going stale.
TITLE_PREFIX_CORRECTIONS = {
    # European Society of Cardiology logo above the title.
    "Barichello et al. 2018 (29648634)": "ESC ",
}

PAPER_FIELDS = [
    "citation_key", "authors", "year", "accession", "accession_type", "pmid",
    "doi", "title", "title_page_header", "merged_key", "abstract_shared", "no_content",
    "n_answers",
]
QUESTION_FIELDS = ["question", "question_full", "n_answered", "n_na"]


def split_title(raw: str) -> tuple[str, str]:
    """Return (title, page_header); exactly one is non-empty unless both are missing."""
    if raw in ("NA", MERGED, ""):
        return "", ""
    one_line = " ".join(raw.split())
    if "\n" in raw or "\r" in raw or PAGE_HEADER_RE.search(raw) or BANNER_RE.match(one_line):
        return "", one_line
    return one_line, ""

_MOJIBAKE_RUN = re.compile(r"[\u0080-￿]+")
_MAX_REPAIR_PASSES = 4  # some text was mis-decoded two or three times over


def _cp1252_byte(char: str) -> int | None:
    """The byte a character came from if it is cp1252 mojibake, else None."""
    if "\u0080" <= char <= "\u009f":  # the five bytes cp1252 leaves undefined
        return ord(char)
    try:
        encoded = char.encode("cp1252")
    except UnicodeEncodeError:
        return None
    return encoded[0] if encoded[0] >= 0x80 else None


def _utf8_length(lead: int) -> int:
    if 0xC2 <= lead <= 0xDF:
        return 2
    if 0xE0 <= lead <= 0xEF:
        return 3
    if 0xF0 <= lead <= 0xF4:
        return 4
    return 0


def _repair_run(match: re.Match[str]) -> str:
    # Decode each complete UTF-8 sequence on its own, so one genuine
    # character inside a run does not stop the rest being repaired.
    run = match.group(0)
    out, i = [], 0
    while i < len(run):
        lead = _cp1252_byte(run[i])
        n = _utf8_length(lead) if lead is not None else 0
        if n and i + n <= len(run):
            raw = [lead] + [_cp1252_byte(c) for c in run[i + 1 : i + n]]
            if all(b is not None and 0x80 <= b <= 0xBF for b in raw[1:]):
                try:
                    out.append(bytes(raw).decode("utf-8"))
                    i += n
                    continue
                except UnicodeDecodeError:
                    pass
        out.append(run[i])
        i += 1
    return "".join(out)


def repair_mojibake(text: str) -> str:
    """Convert UTF-8 text that was read as cp1252 back, leaving other text unchanged."""
    for _ in range(_MAX_REPAIR_PASSES):
        repaired = _MOJIBAKE_RUN.sub(_repair_run, text)
        if repaired == text:
            break
        text = repaired
    return text


def classify_accession(accession: str) -> str:
    if accession == "NA":
        return "NA"
    if accession.isdigit():
        return "PMID"
    if accession.startswith("WOS"):
        return "WOS"
    if accession.startswith("Scopus_"):
        return "SCOPUS"
    return "OTHER"


def clean_doi(value: str) -> str:
    if value in (MERGED, NA_DOI, "NA", ""):
        return ""
    return value.removeprefix("https://doi.org/")


def read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_bytes().decode("utf-16")
    rows = list(csv.reader(io.StringIO(text, newline=""), delimiter="\t"))
    header, body = rows[0], rows[1:]
    if header != EXPECTED_COLUMNS:
        sys.exit(f"Unexpected header in {path}:\n  {header}\nexpected:\n  {EXPECTED_COLUMNS}")
    bad = [i for i, row in enumerate(body, start=2) if len(row) != len(header)]
    if bad:
        sys.exit(f"{len(bad)} records do not have {len(header)} fields (first at record {bad[0]})")
    return [{k: repair_mojibake(v) for k, v in zip(header, row)} for row in body]


def build(rows: list[dict[str, str]]) -> tuple[list[dict], list[dict], dict[str, int]]:
    by_key: dict[str, list[dict[str, str]]] = collections.defaultdict(list)
    raw_keys: dict[str, set[str]] = collections.defaultdict(set)
    for row in rows:
        # A few keys carry trailing whitespace; group on the stripped form.
        key = row[COL_KEY].strip()
        raw_keys[key].add(row[COL_KEY])
        by_key[key].append(row)
    clashes = [k for k, raw in raw_keys.items() if len(raw) > 1]
    if clashes:
        sys.exit(f"Keys differing only by whitespace: {clashes[:5]}")

    abstract_keys: dict[str, set[str]] = collections.defaultdict(set)
    for key, group in by_key.items():
        abstract = group[0][COL_ABSTRACT]
        if abstract not in (MERGED, "NA", ""):
            abstract_keys[abstract].add(key)

    papers, answers = [], []
    stats = collections.Counter()
    for key in sorted(by_key):
        group = by_key[key]
        first = group[0]
        for col in (COL_TITLE, COL_DOI, COL_ABSTRACT):
            if len({r[col] for r in group}) != 1:
                sys.exit(f"{key}: {col} differs between its rows")
        match = KEY_RE.match(key)
        if not match:
            sys.exit(f"Citation key does not match 'Author YEAR (ACCESSION)': {key!r}")
        accession = match["accession"]
        merged = first[COL_DOI] == MERGED or first[COL_ABSTRACT] == MERGED
        title, page_header = split_title(first[COL_TITLE])
        stats["title_page_header"] += bool(page_header)
        if key in TITLE_PREFIX_CORRECTIONS:
            prefix = TITLE_PREFIX_CORRECTIONS[key]
            if not title.startswith(prefix):
                sys.exit(f"{key}: title no longer starts with {prefix!r}; update TITLE_PREFIX_CORRECTIONS")
            title = title.removeprefix(prefix)
            stats["title_prefix_corrected"] += 1
        papers.append({
            "citation_key": key,
            "authors": match["authors"],
            "year": match["year"],
            "accession": "" if accession == "NA" else accession,
            "accession_type": classify_accession(accession),
            "pmid": accession if accession.isdigit() else "",
            "doi": clean_doi(first[COL_DOI]),
            "title": title,
            "title_page_header": page_header,
            "merged_key": int(merged),
            "abstract_shared": int(len(abstract_keys.get(first[COL_ABSTRACT], ())) > 1),
            "no_content": 0,
            "n_answers": 0 if merged else len(group),
        })
        if merged:
            stats["merged_keys"] += 1
            stats["answers_dropped_merged"] += len(group)
            continue
        paper_answers = []
        for row in sorted(group, key=lambda r: r[COL_QUESTION]):
            answer = row[COL_ANSWER].replace("\r\n", "\n").strip()
            is_na = bool(NA_ANSWER_RE.match(answer))
            stats["answers_na" if is_na else "answers"] += 1
            paper_answers.append({
                "citation_key": key,
                "question": row[COL_QUESTION],
                "question_full": row[COL_QUESTION_FULL],
                "answer_is_na": is_na,
                "answer": answer,
            })
        # A paper whose every answer is NA was listed but never analysed.
        if all(a["answer_is_na"] for a in paper_answers):
            papers[-1]["no_content"] = 1
            stats["no_content"] += 1
        answers.extend(paper_answers)
    stats["papers"] = len(papers)
    stats["abstract_shared"] = sum(p["abstract_shared"] for p in papers)
    return papers, answers, dict(stats)


def summarise_questions(answers: list[dict]) -> list[dict]:
    """One row per question, most-answered first; counts exclude merged keys."""
    rows: dict[str, dict] = {}
    for answer in answers:
        row = rows.setdefault(answer["question"], {
            "question": answer["question"],
            "question_full": answer["question_full"],
            "n_answered": 0,
            "n_na": 0,
        })
        if row["question_full"] != answer["question_full"]:
            sys.exit(f"{answer['question']}: more than one full wording in the export")
        row["n_na" if answer["answer_is_na"] else "n_answered"] += 1
    return sorted(rows.values(), key=lambda r: (-r["n_answered"], r["question"]))


def write(papers: list[dict], answers: list[dict], out_dir: Path) -> None:
    # papers.tsv is read line by line (grep, editors), so no field may span lines.
    for paper in papers:
        for field, value in paper.items():
            if isinstance(value, str) and re.search(r"[\t\r\n]", value):
                sys.exit(f"{paper['citation_key']}: {field} contains a tab or line break")
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "papers.tsv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, PAPER_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(papers)
    with (out_dir / "answers.jsonl").open("w", encoding="utf-8") as fh:
        for answer in answers:
            fh.write(json.dumps(answer, ensure_ascii=False) + "\n")
    with (out_dir / "questions.tsv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, QUESTION_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(summarise_questions(answers))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out-dir", type=Path, default=DATA_DIR)
    args = parser.parse_args(argv)
    if not args.input.exists():
        sys.exit(f"{args.input} not found; see data/complement-arie/MANIFEST.yaml for its source")
    papers, answers, stats = build(read_rows(args.input))
    write(papers, answers, args.out_dir)
    for name, value in sorted(stats.items()):
        print(f"{name}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
