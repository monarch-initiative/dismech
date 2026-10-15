"""Cross-walk the OLIDA oligogenic-diseases database against kb/disorders.

This resolves the ``digenic_grouping_olida_crosswalk`` proposed experiment on
kb/groupings/Digenic_and_Oligogenic_Disorders.yaml. That grouping's membership
is assembled incidentally - an entry joins because somebody curating an
unrelated disease happened to bind HP:0010984 or HP:0010983 - so it needs an
external frame to say what is missing. OLIDA is that frame: it applies an
explicit curation protocol and scores every combination on the genetic and
functional evidence behind it (Nachtegael et al., PMID:35411390).

The script produces three lists, which is the split the discussion asks for:

1. ALREADY BOUND    - the disease has a dismech entry that binds a
                      digenic/oligogenic inheritance term. Nothing to do.
2. CURATED, UNBOUND - the disease has a dismech entry with no bound term.
                      These are the cheap wins: no new entry is required, only
                      an inheritance block and its evidence.
3. NO ENTRY         - no dismech entry matches. Real curation work, and the
                      list is long, so ``--min-score`` exists to take the
                      confident end of it first.

Matching is deliberately conservative and is a SCREEN, NOT A VERDICT. Disease
names are normalized and matched against entry names, synonyms and subtype
names; OMIM ids are used when both sides carry them. A name match is a lead a
curator must confirm - OLIDA's disease vocabulary is ICD-10-flavoured and does
not align term-for-term with MONDO, so both false pairings and misses are
expected. Nothing here should be curated without reading the OLIDA entry and
its cited literature.

Usage:
    uv run python scripts/olida_crosswalk.py
    uv run python scripts/olida_crosswalk.py --min-score 2
    uv run python scripts/olida_crosswalk.py --markdown > research/olida_crosswalk.md
    uv run python scripts/olida_crosswalk.py --cache tmp/olida.json   # reuse a pull
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dismech.yaml_io import safe_load

ROOT = Path(__file__).resolve().parents[1]
DISORDERS_DIR = ROOT / "kb" / "disorders"
API = "https://olida.ibsquare.be/api"
MULTILOCUS_TERMS = {"HP:0010984", "HP:0010983"}

# OLIDA's final metascore runs 0-3; the paper describes it as the confidence in
# the combination's involvement in the disease given genetic and functional
# evidence. 2+ is the defensible end.
SCORE_KEY = "final_metascore"

_STOP = {"syndrome", "disease", "disorder", "deficiency", "type", "familial", "the",
         "and", "of", "with", "congenital", "hereditary", "idiopathic", "primary"}


def normalize(name: str) -> str:
    """Lowercase, strip punctuation and roman/arabic type numbers, drop stopwords."""
    s = name.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\b(type|typ)\s*[ivx0-9]+\b", " ", s)
    toks = [t for t in s.split() if t and t not in _STOP]
    return " ".join(sorted(set(toks)))


def fetch_json(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.api+json"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        return json.load(fh)


def fetch_olida() -> dict[str, Any]:
    """Pull every disease plus the combinations that point at it."""
    diseases: list[dict] = []
    url = f"{API}/diseases/?page%5Bsize%5D=100"
    while url:
        page = fetch_json(url)
        diseases.extend(page["data"])
        url = (page.get("links") or {}).get("next")

    combos: dict[str, dict] = {}
    url = f"{API}/combinations/?page%5Bsize%5D=100"
    while url:
        page = fetch_json(url)
        for c in page["data"]:
            combos[c["id"]] = c
        url = (page.get("links") or {}).get("next")
    return {"diseases": diseases, "combinations": combos}


def load_dismech() -> tuple[dict[str, str], dict[str, str], set[str]]:
    """Return (normalized-name -> entry name), (OMIM id -> entry name), bound entries."""
    by_name: dict[str, tuple[str, str]] = {}
    by_omim: dict[str, str] = {}
    bound: set[str] = set()
    for fp in sorted(glob.glob(str(DISORDERS_DIR / "*.yaml"))):
        data = safe_load(open(fp))
        if not isinstance(data, dict) or not data.get("name"):
            continue
        entry = data["name"]

        # Kind is tracked because it is how much a match is worth: an entry-name
        # hit is strong, a synonym or subtype hit often means the OLIDA concept
        # is a sibling or a part of the entry rather than the entry itself.
        names = [(entry, "name")]
        names += [(s, "synonym") for s in (data.get("synonyms") or []) if isinstance(s, str)]
        for st in data.get("has_subtypes") or []:
            for key in ("name", "display_name"):
                if isinstance(st.get(key), str):
                    names.append((st[key], "subtype"))
        for n, kind in names:
            key = normalize(n)
            # Never let a weaker alias displace a stronger one already recorded.
            if key not in by_name or (kind == "name" and by_name[key][1] != "name"):
                by_name[key] = (entry, kind)

        text = json.dumps(data.get("mappings") or {}) + json.dumps(
            data.get("disease_term") or {}
        )
        for omim in re.findall(r"OMIM[:_]?(\d{6})", text):
            by_omim.setdefault(omim, entry)

        def scan(blocks: Any, entry: str = entry) -> None:
            for b in blocks or []:
                term = ((b or {}).get("inheritance_term") or {}).get("term") or {}
                if term.get("id") in MULTILOCUS_TERMS:
                    bound.add(entry)

        # Reach every `inheritance` block the criteria reach, matching the walk
        # in `extract_disease_facts` (src/dismech/groupings.py): disease level,
        # has_subtypes, and the per-gene blocks under `genetic`. Missing the
        # gene-level path would report an entry bound only there as an unbound
        # "cheap win" - the opposite of the truth, in a report whose whole job
        # is to say which entries still need binding.
        scan(data.get("inheritance"))
        for st in data.get("has_subtypes") or []:
            scan(st.get("inheritance"))
        for g in data.get("genetic") or []:
            scan((g or {}).get("inheritance"))
    return by_name, by_omim, bound


def build_rows(olida: dict, min_score: int) -> list[dict]:
    combos = olida["combinations"]
    by_name, by_omim, bound = load_dismech()
    rows = []
    for d in olida["diseases"]:
        attrs = d["attributes"]
        label = attrs.get("disease_name") or "(unnamed)"
        ids = [c["id"] for c in
               (((d.get("relationships") or {}).get("combination_set") or {}).get("data") or [])]
        scores = []
        effects = set()
        for cid in ids:
            c = combos.get(cid)
            if not c:
                continue
            scores.append((c["attributes"].get("scores") or {}).get(SCORE_KEY) or 0)
            if c["attributes"].get("oligogenic_effect"):
                effects.add(c["attributes"]["oligogenic_effect"])
        best = max(scores) if scores else 0
        if best < min_score:
            continue

        omims = [re.sub(r"\D", "", o) for o in (attrs.get("omim_ids") or [])]
        entry = next((by_omim[o] for o in omims if o in by_omim), None)
        matched_on = "omim" if entry else ""
        if not entry:
            hit = by_name.get(normalize(label))
            if hit:
                entry, matched_on = hit

        rows.append({
            "disease": label,
            "combinations": len(ids),
            "best_score": best,
            "effects": sorted(effects),
            "entry": entry,
            "matched_on": matched_on,
            "bound": bool(entry and entry in bound),
        })
    rows.sort(key=lambda r: (-r["best_score"], -r["combinations"], r["disease"].lower()))
    return rows


def render(rows: list[dict], min_score: int, markdown: bool) -> str:
    already = [r for r in rows if r["bound"]]
    unbound = [r for r in rows if r["entry"] and not r["bound"]]
    missing = [r for r in rows if not r["entry"]]
    out: list[str] = []
    w = out.append

    if markdown:
        w("# OLIDA cross-walk against kb/disorders\n")
        w("Generated by `scripts/olida_crosswalk.py`. Regenerate rather than hand-editing.\n")
        w("Resolves the `digenic_grouping_olida_crosswalk` proposed experiment on")
        w("`kb/groupings/Digenic_and_Oligogenic_Disorders.yaml`.\n")
        w("**Name matching is a screen, not a verdict.** OLIDA's disease vocabulary is")
        w("ICD-10-flavoured and does not align term-for-term with MONDO, so a match is a")
        w("lead to confirm against the OLIDA entry and its literature, and an absent match")
        w("is not proof that no dismech entry covers the concept.\n")
        w("**A high score is not a membership argument.** The score rates the")
        w("evidence behind the variant COMBINATION, not the claim that the DISEASE")
        w("requires two loci. Cystinuria sits at the maximum score here and is")
        w("correctly a non-member: the International Cystinuria Consortium")
        w("(PMID:15635077) found the digenic type AB genotype in two of 164 families")
        w("and reported it raising aminoaciduria values rather than causing the")
        w("stone-forming disease. Read the primary literature before binding a term;")
        w("the rule is requirement, not severity.\n")
        w(f"Score floor: OLIDA `{SCORE_KEY}` >= {min_score} (0-3; higher is stronger")
        w("genetic plus functional evidence).\n")
        w("`Matched on` is how the pairing was made and how much it is worth:")
        w("`omim` is strongest, `name` is an entry-name hit, and `synonym`/`subtype`")
        w("frequently mean the OLIDA concept is a sibling or a part of that entry")
        w("rather than the entry itself - check those before acting on them.\n")
        w(f"- diseases at or above the floor: **{len(rows)}**")
        w(f"- already bound to HP:0010984 / HP:0010983: **{len(already)}**")
        w(f"- curated in dismech but unbound (cheap wins): **{len(unbound)}**")
        w(f"- no matching dismech entry: **{len(missing)}**\n")
        for title, group, note in (
            ("Already bound", already, "In the grouping already; nothing to do."),
            ("Curated but unbound", unbound,
             ("A dismech entry exists. Needs only an inheritance block plus evidence - "
              "confirm the OLIDA disease really is this entry's concept first.")),
            ("No dismech entry", missing, "New entry required."),
        ):
            w(f"## {title} ({len(group)})\n")
            w(f"{note}\n")
            if not group:
                w("_None._\n")
                continue
            w("| OLIDA disease | Combos | Score | Effect | dismech entry | Matched on |")
            w("|---|---|---|---|---|---|")
            for r in group:
                w(f"| {r['disease']} | {r['combinations']} | {r['best_score']} | "
                  f"{', '.join(r['effects']) or '-'} | {r['entry'] or '-'} | "
                  f"{r['matched_on'] or '-'} |")
            w("")
    else:
        w(f"OLIDA diseases with {SCORE_KEY} >= {min_score}: {len(rows)}")
        w(f"  already bound     : {len(already)}")
        w(f"  curated, unbound  : {len(unbound)}")
        w(f"  no dismech entry  : {len(missing)}")
        w("")
        for r in unbound:
            w(f"  UNBOUND  [{r['best_score']}] {r['disease']}  ->  {r['entry']} ({r['matched_on']})")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--min-score", type=int, default=0,
                    help=f"minimum OLIDA {SCORE_KEY} (0-3, default 0 = all)")
    ap.add_argument("--markdown", action="store_true", help="emit a markdown report")
    ap.add_argument("--cache", help="path to read/write the raw OLIDA pull as JSON")
    args = ap.parse_args(argv)

    cache = Path(args.cache) if args.cache else None
    if cache and cache.exists():
        olida = json.loads(cache.read_text())
    else:
        olida = fetch_olida()
        if cache:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(olida))

    print(render(build_rows(olida, args.min_score), args.min_score, args.markdown))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
