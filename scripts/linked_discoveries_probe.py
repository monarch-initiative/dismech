#!/usr/bin/env python3
"""Evaluation probe for NLM's Linked Discoveries pilot (2026-09-26).

Linked Discoveries (https://linkeddiscoveries.ncbi.nlm.nih.gov/) builds a
neighborhood of up to 200 PubMed records around a seed PMID using BiomedBERT
embeddings, and annotates every record with MedGen condition, NCBI Gene and
PubChem tags, review status, NIH funding, publication updates (retraction,
expression of concern, erratum) and the citation edges among the neighbors.

**This script exists to reproduce the measurements in
``docs/reports/linked-discoveries-evaluation-2026-09-26.md``. It is not a
curation dependency, it is not wired into the justfile or CI, and it should
not become one without asking NLM first.** The endpoint it calls is the one
the page's own JavaScript uses (``POST /<pmid>/links/`` with the site's CSRF
cookie). It is undocumented, the site describes itself as an early-stage pilot
"for exploratory and evaluation purposes only", and no programmatic-access
terms are published. The probe paces itself (``--pause``, default 0.5 s) and
identifies itself in the User-Agent.

Usage::

    # the neighborhood around a seed, one row per neighbor
    python scripts/linked_discoveries_probe.py neighborhood 20301443 --neighbors 200
    # ... restricted to neighbors tagged with a MedGen CUI, marking KB citation state
    python scripts/linked_discoveries_probe.py neighborhood 20301443 --neighbors 200 \
        --cui C0031269 --mark-kb
    # the seed's own status (retraction / EoC / erratum / review / tag counts)
    python scripts/linked_discoveries_probe.py seed-status 9500320 40526437

Both subcommands accept ``--format tsv`` (default) or ``--format json``.
"""

from __future__ import annotations

import argparse
import http.cookiejar
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://linkeddiscoveries.ncbi.nlm.nih.gov"
CSRF_COOKIE = "linked-discoveries-csrftoken"
USER_AGENT = (
    "dismech-evaluation-probe/0.1 (+https://github.com/monarch-initiative/dismech)"
)
MAX_NEIGHBORS = 200
KB_DIR = Path(__file__).resolve().parents[1] / "kb"


class LinkedDiscoveries:
    """Minimal client for the pilot's neighborhood endpoint."""

    def __init__(self, pause: float = 0.5) -> None:
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.jar)
        )
        self.opener.addheaders = [("User-Agent", USER_AGENT)]
        self.pause = pause
        self._token: str | None = None

    def token(self, pmid: str) -> str:
        """The CSRF cookie is set on a seed page, not on the landing page."""
        if self._token is None:
            self.opener.open(f"{BASE}/{pmid}/", timeout=60).read()
            for cookie in self.jar:
                if cookie.name == CSRF_COOKIE:
                    self._token = cookie.value
            if self._token is None:
                raise RuntimeError(
                    f"{CSRF_COOKIE} cookie was not set by {BASE}/{pmid}/"
                )
        return self._token

    def neighborhood(self, pmid: str, neighbors: int = 50) -> dict:
        if not 1 <= neighbors <= MAX_NEIGHBORS:
            raise ValueError(
                f"neighbors must be 1..{MAX_NEIGHBORS} (the endpoint returns 400 otherwise)"
            )
        token = self.token(pmid)
        request = urllib.request.Request(
            f"{BASE}/{pmid}/links/",
            data=urllib.parse.urlencode({"neighbors": neighbors}).encode(),
            headers={
                "X-CSRFToken": token,
                "Referer": f"{BASE}/{pmid}/",
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            method="POST",
        )
        started = time.time()
        with self.opener.open(request, timeout=120) as response:
            payload = json.loads(response.read().decode())
        payload["_seconds"] = round(time.time() - started, 2)
        time.sleep(self.pause)
        return payload


def seed_article(payload: dict) -> dict | None:
    for article in payload.get("articles", []):
        if article.get("isSeed"):
            return article
    return None


def cui_names(payload: dict) -> dict[str, str]:
    return {
        cui: info.get("preferredName", "")
        for cui, info in (payload.get("diseases") or {}).items()
    }


def kb_citations() -> dict[str, set[str]]:
    """PMID -> set of kb/ file stems that cite it as a ``reference:``."""
    cited: dict[str, set[str]] = {}
    for path in KB_DIR.rglob("*.yaml"):
        for pmid in re.findall(r"reference: PMID:(\d+)", path.read_text()):
            cited.setdefault(pmid, set()).add(path.stem)
    return cited


def updates_summary(article: dict) -> str:
    updates = article.get("publicationUpdates") or {}
    parts = [f"{key}={value}" for key, value in updates.items() if value]
    return ";".join(parts)


def cmd_neighborhood(args: argparse.Namespace) -> int:
    client = LinkedDiscoveries(pause=args.pause)
    payload = client.neighborhood(args.pmid, args.neighbors)
    names = cui_names(payload)
    wanted = set(args.cui or [])
    cited = kb_citations() if args.mark_kb else {}
    rows = []
    for article in payload.get("articles", []):
        if article.get("isSeed"):
            continue
        cuis = set(article.get("diseases") or [])
        if wanted and not (cuis & wanted):
            continue
        pmid = article["articleId"]
        row = {
            "pmid": pmid,
            "year": article.get("publicationYear"),
            "score": round(article.get("score") or 0.0, 4),
            "retracted": bool(article.get("isRetracted")),
            "review": bool(article.get("isReview")),
            "nih_funded": bool(article.get("hasNIHFunding")),
            "updates": updates_summary(article),
            "conditions": "|".join(names.get(c, c) for c in sorted(cuis)),
            "genes": "|".join(article.get("genes") or []),
            "title": (article.get("title") or "").replace("\t", " "),
        }
        if args.mark_kb:
            files = cited.get(pmid, set())
            row["kb"] = "in_kb:" + ",".join(sorted(files)) if files else "new"
        rows.append(row)
    seed = seed_article(payload)
    meta = {
        "seed": args.pmid,
        "seed_found": seed is not None,
        "seed_title": (seed or {}).get("title"),
        "requested": args.neighbors,
        "returned": payload.get("realCount"),
        "rows": len(rows),
        "citation_edges": len(payload.get("citationEdges") or []),
        "seconds": payload.get("_seconds"),
    }
    if args.format == "json":
        json.dump({"meta": meta, "rows": rows}, sys.stdout, indent=1)
        print()
    else:
        print("# " + json.dumps(meta), file=sys.stderr)
        if rows:
            print("\t".join(rows[0].keys()))
            for row in rows:
                print("\t".join(str(v) for v in row.values()))
    return 0


def cmd_seed_status(args: argparse.Namespace) -> int:
    client = LinkedDiscoveries(pause=args.pause)
    rows = []
    for pmid in args.pmids:
        payload = client.neighborhood(pmid, 1)
        seed = seed_article(payload) or {}
        rows.append(
            {
                "pmid": pmid,
                "seed_found": bool(seed),
                "neighborhood": payload.get("realCount"),
                "retracted": bool(seed.get("isRetracted")),
                "updates": updates_summary(seed),
                "review": bool(seed.get("isReview")),
                "condition_tags": len(seed.get("diseases") or []),
                "gene_tags": len(seed.get("genes") or []),
                "chemical_tags": len(seed.get("chemicals") or []),
                "publication_types": "|".join(seed.get("publicationTypes") or []),
                "title": (seed.get("title") or "").replace("\t", " "),
            }
        )
    if args.format == "json":
        json.dump(rows, sys.stdout, indent=1)
        print()
    else:
        print("\t".join(rows[0].keys()))
        for row in rows:
            print("\t".join(str(v) for v in row.values()))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--pause",
        type=float,
        default=0.5,
        help="seconds to sleep after each request (default 0.5)",
    )
    parser.add_argument("--format", choices=("tsv", "json"), default="tsv")
    sub = parser.add_subparsers(dest="command", required=True)

    nb = sub.add_parser("neighborhood", help="one row per neighbor of a seed PMID")
    nb.add_argument("pmid")
    nb.add_argument(
        "--neighbors", type=int, default=50, help=f"1..{MAX_NEIGHBORS} (default 50)"
    )
    nb.add_argument(
        "--cui",
        action="append",
        help="keep only neighbors tagged with this MedGen CUI (repeatable)",
    )
    nb.add_argument(
        "--mark-kb",
        action="store_true",
        help="mark each neighbor as new or already cited under kb/",
    )
    nb.set_defaults(func=cmd_neighborhood)

    st = sub.add_parser(
        "seed-status", help="retraction / update / review / tag status of each PMID"
    )
    st.add_argument("pmids", nargs="+")
    st.set_defaults(func=cmd_seed_status)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
