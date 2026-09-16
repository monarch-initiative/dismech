#!/usr/bin/env python3
"""Extract every hgnc-bound gene symbol per dismech entry into a TSV
(symbol, kind, entry name, path) for BPM overlap annotation.

Run from the repository root with the repo environment:
    uv run python experiments/human_gi_bpm/extract_dismech_genes.py > genes.tsv
"""
import glob

from dismech.yaml_io import safe_load


def walk(o, fn):
    if isinstance(o, dict):
        fn(o)
        for v in o.values():
            walk(v, fn)
    elif isinstance(o, list):
        for v in o:
            walk(v, fn)


def main():
    for path in sorted(glob.glob("kb/disorders/*.yaml") + glob.glob("kb/modules/*.yaml")):
        d = safe_load(open(path))
        name = d.get("name", path)
        syms = set()

        def collect(o):
            t = o.get("term")
            if isinstance(t, dict) and str(t.get("id", "")).lower().startswith("hgnc:"):
                if t.get("label"):
                    syms.add(t["label"])

        walk(d, collect)
        kind = "module" if "/modules/" in path else "disorder"
        for s in sorted(syms):
            print(f"{s}\t{kind}\t{name}\t{path}")


if __name__ == "__main__":
    main()
