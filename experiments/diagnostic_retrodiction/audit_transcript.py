"""Audit a curation session transcript for the events that disqualify a replicate.

Reads a JSONL transcript (Claude Code session JSONL, or `claude -p --output-format
stream-json` output: one JSON object per line, assistant and user messages carrying
content blocks). Records an event for each of:

  WEB_TOOL            a call to a web tool (WebSearch, WebFetch, any tool whose name
                      contains "web"), or to a denied MCP tool (mcp__codex__*)
  NETWORK_COMMAND     a Bash command containing http://, https://, curl, wget, urllib,
                      requests, eutils, or an inline interpreter (python -c, python3 -c,
                      node -e), which can sidestep the prefix deny rules
  EXCLUDED_PATH       a tool call whose path argument, or a Bash command, names a path
                      matching one of the --exclude glob patterns
  OUT_OF_PACKET_PMID  a PMID, in any tool input or in the assistant's text, that is not
                      in the case's packet
  LEAKAGE_TERM        a leakage term with in_packet "no" (from the case rubric) in the
                      assistant's text or in any tool input. Terms match as whole words,
                      case-insensitively, on the exact term: "NMO-IgG" matches, "NMO"
                      alone does not

A replicate passes only with zero events (README, *Curation protocol*). Tool results
(what the tools returned) are not scanned for PMIDs or leakage terms, because a packet
file legitimately contains its own PMIDs; what the agent writes or asks for is.

Usage:
    python audit_transcript.py TRANSCRIPT.jsonl --packet packet.tsv --rubric rubrics/C017.yaml \
        [--exclude 'references_cache/**' ...] [--out report.json]
Exit code 0 = no events, 1 = events, 2 = unreadable input.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

WEB_TOOL_RE = re.compile(r"web|^mcp__codex__", re.I)
NETWORK_RE = re.compile(r"https?://|\bcurl\b|\bwget\b|\burllib\b|\brequests\b|\beutils\b|"
                        r"\bpython3?\s+-c\b|\bnode\s+-e\b", re.I)
PMID_RE = re.compile(r"PMID[:\s]*(\d{5,9})", re.I)
PATH_KEYS = ("file_path", "path", "notebook_path", "pattern")


@dataclass
class Event:
    kind: str
    line: int
    detail: str


def blocks(obj: dict):
    """Yield (role, block) for every content block in one transcript line."""
    msg = obj.get("message") if isinstance(obj.get("message"), dict) else None
    role = obj.get("type") or (msg or {}).get("role")
    content = (msg or {}).get("content") if msg else obj.get("content")
    if isinstance(content, str):
        yield role, {"type": "text", "text": content}
    elif isinstance(content, list):
        for b in content:
            if isinstance(b, dict):
                yield role, b


def term_regex(term: str) -> re.Pattern:
    return re.compile(rf"(?<![\w-]){re.escape(term)}(?![\w-])", re.I)


def audit(lines: list[str], packet_pmids: set[str], leakage: list[str], exclude: list[str]) -> list[Event]:
    events: list[Event] = []
    leak_res = [(t, term_regex(t)) for t in leakage]

    def scan_text(text: str, n: int, where: str) -> None:
        for m in PMID_RE.finditer(text):
            if m.group(1) not in packet_pmids:
                events.append(Event("OUT_OF_PACKET_PMID", n, f"PMID:{m.group(1)} in {where}"))
        for t, rx in leak_res:
            if rx.search(text):
                events.append(Event("LEAKAGE_TERM", n, f"'{t}' in {where}"))

    for n, raw in enumerate(lines, 1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            events.append(Event("UNPARSEABLE_LINE", n, raw[:80]))
            continue
        for role, b in blocks(obj):
            if b.get("type") == "tool_use":
                name, inp = str(b.get("name", "")), b.get("input") or {}
                flat = json.dumps(inp, ensure_ascii=False)
                if WEB_TOOL_RE.search(name):
                    events.append(Event("WEB_TOOL", n, name))
                if name == "Bash":
                    cmd = str(inp.get("command", ""))
                    if NETWORK_RE.search(cmd):
                        events.append(Event("NETWORK_COMMAND", n, cmd[:200]))
                    for pat in exclude:
                        stem = pat.rstrip("*").rstrip("/")
                        if stem and stem in cmd:
                            events.append(Event("EXCLUDED_PATH", n, f"Bash names {stem}"))
                for k in PATH_KEYS:
                    v = inp.get(k)
                    if isinstance(v, str) and any(fnmatch.fnmatch(v.lstrip("./"), p) for p in exclude):
                        events.append(Event("EXCLUDED_PATH", n, f"{name} {k}={v}"))
                scan_text(flat, n, f"{name} input")
            elif b.get("type") == "text" and role == "assistant":
                scan_text(str(b.get("text", "")), n, "assistant text")
    return events


def leakage_terms(rubric: Path) -> list[str]:
    r = yaml.safe_load(rubric.read_text(encoding="utf-8")) or {}
    return [t["term"] for t in r.get("leakage_terms", []) if t.get("in_packet") == "no"]


def packet_pmids(packet: Path) -> set[str]:
    out = set()
    for line in packet.read_text(encoding="utf-8").splitlines()[1:]:
        m = PMID_RE.search(line.split("\t")[0]) if line.strip() else None
        if m:
            out.add(m.group(1))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("transcript", type=Path)
    ap.add_argument("--packet", required=True, type=Path, help="packet.tsv (first column PMID:N)")
    ap.add_argument("--rubric", type=Path, help="case rubric; its in_packet=no leakage terms are checked")
    ap.add_argument("--exclude", action="append", default=[], help="glob of an excluded path (repeatable)")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    try:
        lines = a.transcript.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as e:
        print(f"cannot read transcript ({type(e).__name__})", file=sys.stderr)
        sys.exit(2)
    ev = audit(lines, packet_pmids(a.packet), leakage_terms(a.rubric) if a.rubric else [], a.exclude)
    report = {"transcript": str(a.transcript), "events": [asdict(e) for e in ev], "passed": not ev}
    text = json.dumps(report, indent=2, ensure_ascii=False)
    if a.out:
        a.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    sys.exit(0 if not ev else 1)


if __name__ == "__main__":
    main()
