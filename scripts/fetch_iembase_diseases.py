#!/usr/bin/env python3
"""Pre-fetch raw IEMbase disease JSON.

The current IEMbase frontend enumerates disorders through the ICIMD browse
endpoint, then loads each disease detail record by numeric id. This script
captures those raw JSON responses under ``data/iembase/`` for downstream
analysis without touching ``references_cache/``.

Usage:
    just iembase-prefetch
    just iembase-prefetch --force
    uv run python scripts/fetch_iembase_diseases.py --limit 10
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests


DEFAULT_BASE_URL = "https://www.iembase.com/api/v2"
DEFAULT_DATA_DIR = Path("data/iembase")
USER_AGENT = (
    "dismech-iembase-prefetch/1.0 (https://github.com/monarch-initiative/dismech)"
)


@dataclass(frozen=True)
class FetchConfig:
    base_url: str
    timeout: float
    retries: int
    retry_sleep: float


def fetch_json(
    url: str,
    *,
    params: dict[str, Any] | None = None,
    config: FetchConfig,
) -> Any:
    """Fetch JSON with bounded retries for transient network/server failures."""
    headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    last_exc: Exception | None = None

    for attempt in range(config.retries + 1):
        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=config.timeout,
            )
            if response.status_code in {429, 500, 502, 503, 504}:
                response.raise_for_status()
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, json.JSONDecodeError) as exc:
            last_exc = exc
            if attempt >= config.retries:
                break
            wait = config.retry_sleep * (2**attempt)
            time.sleep(wait)

    raise RuntimeError(f"failed to fetch {url}: {last_exc}") from last_exc


def write_json_atomic(path: Path, data: Any) -> None:
    """Write deterministic JSON through a temporary file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


def fetch_browse_tree(config: FetchConfig) -> Any:
    return fetch_json(
        f"{config.base_url}/disorder/icimd_browse/",
        params={"format": "json"},
        config=config,
    )


def extract_disease_index_records(
    browse_tree: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Flatten IEMbase's collection/group/subgroup browse tree to disease rows."""
    rows: list[dict[str, Any]] = []

    for collection in browse_tree:
        collection_code = collection.get("collection_code")
        collection_name = collection.get("name")
        for group in collection.get("disorders_groups", []) or []:
            group_code = group.get("icimd_nosology_group_code")
            group_name = group.get("name")
            for subgroup in group.get("subgroups", []) or []:
                subgroup_code = subgroup.get("icimd_nosology_subgroup_code")
                subgroup_name = subgroup.get("name")
                for disorder in subgroup.get("disorders", []) or []:
                    if "id" not in disorder:
                        continue
                    row = {
                        "id": int(disorder["id"]),
                        "name": disorder.get("name"),
                        "name_alt1": disorder.get("name_alt1"),
                        "name_alt2": disorder.get("name_alt2"),
                        "gene_sym": disorder.get("gene_sym"),
                        "inheritance": disorder.get("inheritance"),
                        "icimd_nosology_disorder_num": disorder.get(
                            "icimd_nosology_disorder_num"
                        ),
                        "collection_code": collection_code,
                        "collection_name": collection_name,
                        "icimd_nosology_group_code": group_code,
                        "group_name": group_name,
                        "icimd_nosology_subgroup_code": subgroup_code,
                        "subgroup_name": subgroup_name,
                        "detail_json": f"diseases/{int(disorder['id'])}.json",
                    }
                    rows.append(row)

    rows.sort(key=lambda row: row["id"])
    seen: set[int] = set()
    duplicates: set[int] = set()
    for row in rows:
        disease_id = row["id"]
        if disease_id in seen:
            duplicates.add(disease_id)
        seen.add(disease_id)
    if duplicates:
        duplicate_text = ", ".join(str(d) for d in sorted(duplicates))
        raise ValueError(
            f"duplicate IEMbase disease ids in browse tree: {duplicate_text}"
        )
    return rows


def fetch_disease_detail(
    disease_id: int,
    *,
    data_dir: Path,
    config: FetchConfig,
    force: bool,
) -> tuple[int, str]:
    """Fetch one disease detail JSON file. Returns (id, status)."""
    target = data_dir / "diseases" / f"{disease_id}.json"
    if target.exists() and not force:
        return disease_id, "cached"

    data = fetch_json(
        f"{config.base_url}/disorder/{disease_id}",
        params={"format": "json"},
        config=config,
    )
    write_json_atomic(target, data)
    return disease_id, "fetched"


def prefetch(args: argparse.Namespace) -> int:
    data_dir = args.data_dir
    data_dir.mkdir(parents=True, exist_ok=True)
    config = FetchConfig(
        base_url=args.base_url.rstrip("/"),
        timeout=args.timeout,
        retries=args.retries,
        retry_sleep=args.retry_sleep,
    )

    print(f"Fetching IEMbase browse tree from {config.base_url} ...", flush=True)
    browse_tree = fetch_browse_tree(config)
    if not isinstance(browse_tree, list):
        raise RuntimeError("IEMbase browse endpoint did not return a list")

    write_json_atomic(data_dir / "browse.json", browse_tree)
    disease_rows = extract_disease_index_records(browse_tree)
    if args.id:
        requested = set(args.id)
        disease_rows = [row for row in disease_rows if row["id"] in requested]
        missing = requested.difference(row["id"] for row in disease_rows)
        if missing:
            raise SystemExit(
                "requested ids not found in IEMbase browse tree: "
                + ", ".join(str(i) for i in sorted(missing))
            )
    if args.limit:
        disease_rows = disease_rows[: args.limit]

    print(f"Fetching {len(disease_rows)} disease detail JSON files ...", flush=True)
    failures: list[tuple[int, str]] = []
    counts = {"cached": 0, "fetched": 0}

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                fetch_disease_detail,
                row["id"],
                data_dir=data_dir,
                config=config,
                force=args.force,
            ): row["id"]
            for row in disease_rows
        }
        for done_count, future in enumerate(as_completed(futures), start=1):
            disease_id = futures[future]
            try:
                _, status = future.result()
                counts[status] = counts.get(status, 0) + 1
            except Exception as exc:  # noqa: BLE001 - report all failed ids together
                failures.append((disease_id, str(exc)))
            if done_count % args.progress_every == 0 or done_count == len(futures):
                print(
                    f"  ... {done_count}/{len(futures)} "
                    f"({counts.get('fetched', 0)} fetched, "
                    f"{counts.get('cached', 0)} cached, {len(failures)} failed)",
                    flush=True,
                )

    fetched_at = datetime.now(UTC).replace(microsecond=0).isoformat()
    index = {
        "source": "IEMbase",
        "base_url": config.base_url,
        "browse_endpoint": f"{config.base_url}/disorder/icimd_browse/?format=json",
        "detail_endpoint_template": f"{config.base_url}/disorder/{{id}}?format=json",
        "fetched_at": fetched_at,
        "disease_count": len(disease_rows),
        "fetched_count": counts.get("fetched", 0),
        "cached_count": counts.get("cached", 0),
        "failed_count": len(failures),
        "failures": [
            {"id": disease_id, "error": error} for disease_id, error in failures
        ],
        "diseases": disease_rows,
    }
    write_json_atomic(data_dir / "disease_index.json", index)

    print(
        f"Wrote {data_dir / 'browse.json'}, "
        f"{data_dir / 'disease_index.json'}, and "
        f"{data_dir / 'diseases'}/*.json",
        flush=True,
    )
    if failures:
        for disease_id, error in failures[:20]:
            print(f"  failed {disease_id}: {error}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  ... {len(failures) - 20} more failures", file=sys.stderr)
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"IEMbase API base URL (default: {DEFAULT_BASE_URL})",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help=f"Output directory (default: {DEFAULT_DATA_DIR})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch disease detail JSON even when a local file already exists.",
    )
    parser.add_argument(
        "--id",
        type=int,
        action="append",
        help="Restrict to one disease id. May be passed more than once.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Fetch only the first N diseases from the sorted browse index.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of concurrent detail fetches (default: 4).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="HTTP timeout in seconds (default: 60).",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Retry count for transient fetch failures (default: 3).",
    )
    parser.add_argument(
        "--retry-sleep",
        type=float,
        default=1.0,
        help="Initial retry sleep in seconds, doubled each retry (default: 1).",
    )
    parser.add_argument(
        "--progress-every",
        type=int,
        default=100,
        help="Print progress every N completed detail fetches (default: 100).",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be at least 1")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    if args.progress_every < 1:
        parser.error("--progress-every must be at least 1")
    raise SystemExit(prefetch(args))


if __name__ == "__main__":
    main()
