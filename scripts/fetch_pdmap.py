#!/usr/bin/env python3
"""Fetch a MINERVA-hosted disease map's curated reactions as curation leads.

Defaults to the Parkinson's disease map (https://pdmap.uni.lu/minerva, project
``pd_map_spring_24``, CC-BY 4.0). Nothing here is PD-specific: every MINERVA
instance serves the same REST API, so ``--instance``/``--project`` retargets the
script at another disease map.

Outputs, under ``pathways/pdmap/`` by default:

    index.yaml        source provenance plus one row per submap
    <submap>.yaml     referenced reactions and the annotated elements they use
    lead_pmids.tsv    one row per cited PubMed ID, with dismech's own coverage

**These are leads, not evidence.** A map reaction asserts that its cited paper
supports that interaction; a dismech evidence item additionally needs the paper
in ``references_cache/`` (``just fetch-reference PMID:NNNNNNN``) and an exact
quoted sentence. The article titles recorded here come from MINERVA, not from
that cache, so they must never be copied into a ``reference_title:`` slot --
see the reference-title rule in CLAUDE.md.

Reaction and modifier types are the map's own (``State transition``,
``Catalysis``, ``Inhibition``, ...). They are recorded verbatim rather than
translated into a dismech causal predicate: dismech ``downstream`` edges are
unsigned, and choosing which reactions deserve a pathophysiology node at all is
a curation judgement this script does not make.

Usage:
    uv run python scripts/fetch_pdmap.py --list
    uv run python scripts/fetch_pdmap.py
    uv run python scripts/fetch_pdmap.py --submap Autophagy --submap "LRRK2 activity"
    uv run python scripts/fetch_pdmap.py --all-reactions
    uv run python scripts/fetch_pdmap.py --instance https://host/minerva --project ID \
        --out pathways/other-map
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any

import yaml

DEFAULT_INSTANCE = "https://pdmap.uni.lu/minerva"
DEFAULT_PROJECT = "pd_map_spring_24"
DEFAULT_OUT = Path("pathways/pdmap")
KB_DIR = Path("kb")
REFERENCES_CACHE = Path("references_cache")
TIMEOUT = 180

# MINERVA annotation types worth carrying into a lead file, and the CURIE prefix
# each becomes. HGNC is lowercased to match this repository's convention. The
# omitted types (INCHI, INCHIKEY, STITCH, REFSEQ, VMH_METABOLITE, ...) are
# structure/registry identifiers that add bulk without helping a curator.
CURIE_PREFIXES = {
    "HGNC": "hgnc",
    "UNIPROT": "uniprot",
    "ENTREZ": "ncbigene",
    "ENSEMBL": "ensembl",
    "CHEBI": "CHEBI",
    "GO": "GO",
    "REACTOME": "reactome",
    "MESH_2012": "mesh",
    "EC": "eccode",
    "PUBCHEM": "pubchem.compound",
    "KEGG_REACTION": "kegg.reaction",
}

# Element types that carry no biology worth listing as a lead participant.
SKIPPED_ELEMENT_TYPES = {"Compartment"}


def fetch_json(url: str, cache: Path | None, refresh: bool = False) -> Any:
    """GET *url* as JSON, memoized on disk at *cache*."""
    if cache is not None and cache.exists() and not refresh:
        return json.loads(cache.read_text())
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as response:
            payload = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:  # pragma: no cover - network
        raise SystemExit(f"{url}: HTTP {exc.code} {exc.reason}") from exc
    except urllib.error.URLError as exc:  # pragma: no cover - network
        raise SystemExit(f"{url}: {exc.reason}") from exc
    if cache is not None:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(payload)
    return json.loads(payload)


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    return slug or "submap"


def curies(references: list[dict] | None) -> list[str]:
    out = []
    for ref in references or []:
        prefix = CURIE_PREFIXES.get(ref.get("type") or "")
        resource = ref.get("resource")
        if prefix and resource:
            curie = f"{prefix}:{resource}"
            if curie not in out:
                out.append(curie)
    return sorted(out)


def pubmed_ids(references: list[dict] | None) -> list[str]:
    out = {
        ref["resource"]
        for ref in references or []
        if ref.get("type") == "PUBMED" and ref.get("resource")
    }
    return sorted(out, key=int)


def articles(references: list[dict] | None) -> dict[str, dict]:
    """PubMed ID -> the article metadata MINERVA reports for it."""
    out = {}
    for ref in references or []:
        if ref.get("type") != "PUBMED" or not ref.get("resource"):
            continue
        article = ref.get("article") or {}
        out[ref["resource"]] = {
            "title": (article.get("title") or "").strip(),
            "journal": (article.get("journal") or "").strip(),
            "year": article.get("year") or "",
        }
    return out


def element_label(element: dict) -> str:
    return (element.get("name") or element.get("elementId") or "").strip()


def build_submap(
    reactions: list[dict],
    elements: list[dict],
    referenced_only: bool,
) -> tuple[list[dict], list[dict], dict[str, dict]]:
    """Return (reaction records, element records, article metadata)."""
    by_id = {element["id"]: element for element in elements}
    kept, used_ids, article_meta = [], set(), {}

    for reaction in sorted(
        reactions, key=lambda r: str(r.get("reactionId") or r["id"])
    ):
        pmids = pubmed_ids(reaction.get("references"))
        if referenced_only and not pmids:
            continue
        article_meta.update(articles(reaction.get("references")))

        def participants(key: str) -> list[str]:
            names = []
            for part in reaction.get(key) or []:
                element = by_id.get(part.get("aliasId"))
                if element is None:
                    continue
                used_ids.add(element["id"])
                label = element_label(element)
                if label:
                    names.append(label)
            return names

        record: dict[str, Any] = {
            "id": str(reaction.get("reactionId") or reaction["id"]),
            "type": reaction.get("type") or "",
        }
        name = (reaction.get("name") or "").strip()
        if name:
            record["name"] = name
        for key in ("reactants", "products"):
            values = participants(key)
            if values:
                record[key] = values
        modifiers = []
        for modifier in reaction.get("modifiers") or []:
            element = by_id.get(modifier.get("aliasId"))
            if element is None:
                continue
            used_ids.add(element["id"])
            label = element_label(element)
            if label:
                modifiers.append({"type": modifier.get("type") or "", "element": label})
        if modifiers:
            record["modifiers"] = modifiers
        if pmids:
            record["pmids"] = [f"PMID:{pmid}" for pmid in pmids]
        kept.append(record)

    # One species is often drawn several times in a submap, so the same element
    # record arrives once per glyph. Emit each distinct record once.
    element_records: list[dict] = []
    seen: set[tuple] = set()
    for element in sorted(by_id.values(), key=lambda e: (element_label(e), e["id"])):
        if element["id"] not in used_ids:
            continue
        if element.get("type") in SKIPPED_ELEMENT_TYPES:
            continue
        label = element_label(element)
        if not label:
            continue
        record = {"name": label, "type": element.get("type") or ""}
        full_name = (element.get("fullName") or "").strip()
        if full_name and full_name != label:
            record["full_name"] = full_name
        identifiers = curies(element.get("references"))
        if identifiers:
            record["identifiers"] = identifiers
        key = (label, record["type"], record.get("full_name", ""), tuple(identifiers))
        if key in seen:
            continue
        seen.add(key)
        element_records.append(record)

    return kept, element_records, article_meta


def cited_pmids_in_kb() -> set[str]:
    cited: set[str] = set()
    if not KB_DIR.exists():
        return cited
    for path in KB_DIR.rglob("*.yaml"):
        cited |= set(re.findall(r"PMID:(\d+)", path.read_text()))
    return cited


def write_yaml(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        handle.write(
            "# Generated by scripts/fetch_pdmap.py -- do not hand-edit.\n"
            "# Curation LEADS from a MINERVA disease map, not dismech evidence:\n"
            "# fetch each PMID into references_cache/ and quote it exactly before use.\n"
        )
        yaml.safe_dump(payload, handle, sort_keys=False, width=100, allow_unicode=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__ and __doc__.splitlines()[0])
    parser.add_argument("--instance", default=DEFAULT_INSTANCE, help="MINERVA base URL")
    parser.add_argument("--project", default=DEFAULT_PROJECT, help="MINERVA project id")
    parser.add_argument(
        "--out", type=Path, default=DEFAULT_OUT, help="output directory"
    )
    parser.add_argument(
        "--submap",
        action="append",
        default=[],
        metavar="NAME",
        help="restrict to this submap (repeatable; matched case-insensitively)",
    )
    parser.add_argument("--list", action="store_true", help="list submaps and exit")
    parser.add_argument(
        "--all-reactions",
        action="store_true",
        help="also emit reactions carrying no PubMed reference (they are not leads)",
    )
    parser.add_argument(
        "--refresh", action="store_true", help="ignore the local JSON cache"
    )
    args = parser.parse_args()

    api = f"{args.instance.rstrip('/')}/api"
    cache_dir = args.out / ".cache" / args.project
    referenced_only = not args.all_reactions

    projects = fetch_json(f"{api}/projects/", cache_dir / "projects.json", args.refresh)
    project = next((p for p in projects if p.get("projectId") == args.project), None)
    if project is None:
        names = sorted(p["projectId"] for p in projects if p.get("name"))
        raise SystemExit(
            f"project {args.project!r} not found; available: {', '.join(names)}"
        )

    submaps = fetch_json(
        f"{api}/projects/{args.project}/models/",
        cache_dir / "models.json",
        args.refresh,
    )
    if args.list:
        for submap in submaps:
            print(f"{submap['idObject']}\t{submap.get('name') or '(unnamed)'}")
        return 0

    wanted = {name.lower() for name in args.submap}
    if wanted:
        submaps = [s for s in submaps if (s.get("name") or "").lower() in wanted]
        if not submaps:
            raise SystemExit(f"no submap matched {sorted(wanted)}; try --list")

    license_block = project.get("license") or {}
    disease = project.get("disease") or {}
    organism = project.get("organism") or {}
    source = {
        "instance": args.instance.rstrip("/"),
        "project_id": args.project,
        "project_name": project.get("name") or "",
        "project_version": project.get("version") or "",
        "license": license_block.get("name") or project.get("customLicenseName") or "",
        "disease": f"mesh:{disease['resource']}" if disease.get("resource") else "",
        "organism": f"NCBITaxon:{organism['resource']}"
        if organism.get("resource")
        else "",
        "api_base": f"{api}/projects/{args.project}",
        "retrieved": date.today().isoformat(),
        "reaction_filter": "referenced_only" if referenced_only else "all_reactions",
    }

    rows: list[dict] = []
    pmid_reactions: dict[str, int] = {}
    pmid_submaps: dict[str, set[str]] = {}
    pmid_articles: dict[str, dict] = {}

    for submap in submaps:
        model_id = submap["idObject"]
        name = submap.get("name") or f"model_{model_id}"
        base = f"{api}/projects/{args.project}/models/{model_id}/bioEntities"
        reactions = fetch_json(
            f"{base}/reactions/", cache_dir / f"{model_id}.reactions.json", args.refresh
        )
        elements = fetch_json(
            f"{base}/elements/", cache_dir / f"{model_id}.elements.json", args.refresh
        )
        records, element_records, article_meta = build_submap(
            reactions, elements, referenced_only
        )
        pmid_articles.update(article_meta)

        for record in records:
            for pmid in record.get("pmids", []):
                bare = pmid.split(":", 1)[1]
                pmid_reactions[bare] = pmid_reactions.get(bare, 0) + 1
                pmid_submaps.setdefault(bare, set()).add(name)

        slug = slugify(name)
        unique = sorted({p for r in records for p in r.get("pmids", [])})
        write_yaml(
            args.out / f"{slug}.yaml",
            {
                "source": {**source, "submap": name, "submap_id": model_id},
                "counts": {
                    "reactions_in_submap": len(reactions),
                    "reactions_emitted": len(records),
                    "elements_emitted": len(element_records),
                    "unique_pmids": len(unique),
                },
                "elements": element_records,
                "reactions": records,
            },
        )
        rows.append(
            {
                "submap": name,
                "submap_id": model_id,
                "file": f"{slug}.yaml",
                "reactions_in_submap": len(reactions),
                "reactions_emitted": len(records),
                "unique_pmids": len(unique),
            }
        )
        print(
            f"{name}: {len(records)}/{len(reactions)} reactions, "
            f"{len(unique)} PMIDs -> {args.out / f'{slug}.yaml'}"
        )

    cited = cited_pmids_in_kb()
    all_pmids = sorted(pmid_reactions, key=int)
    uncited = [p for p in all_pmids if p not in cited]

    write_yaml(
        args.out / "index.yaml",
        {
            "source": source,
            "totals": {
                "submaps": len(rows),
                "reactions_emitted": sum(r["reactions_emitted"] for r in rows),
                "unique_pmids": len(all_pmids),
                "pmids_already_cited_in_kb": len(all_pmids) - len(uncited),
                "pmids_not_yet_cited_in_kb": len(uncited),
            },
            "submaps": rows,
        },
    )

    leads = args.out / "lead_pmids.tsv"
    with leads.open("w") as handle:
        handle.write(
            "pmid\treactions\tsubmaps\tcited_in_kb\tin_references_cache\tyear\tjournal\ttitle\n"
        )
        for pmid in sorted(all_pmids, key=lambda p: (-pmid_reactions[p], int(p))):
            article = pmid_articles.get(pmid, {})
            handle.write(
                "\t".join(
                    [
                        f"PMID:{pmid}",
                        str(pmid_reactions[pmid]),
                        ";".join(sorted(pmid_submaps.get(pmid, ()))),
                        "yes" if pmid in cited else "no",
                        "yes"
                        if (REFERENCES_CACHE / f"PMID_{pmid}.md").exists()
                        else "no",
                        str(article.get("year") or ""),
                        str(article.get("journal") or "").replace("\t", " "),
                        str(article.get("title") or "").replace("\t", " "),
                    ]
                )
                + "\n"
            )

    print(
        f"\n{len(all_pmids)} unique PMIDs across {len(rows)} submaps; "
        f"{len(uncited)} not yet cited anywhere in kb/ -> {leads}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
