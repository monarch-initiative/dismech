#!/usr/bin/env python3
"""Generate a dismech COHD association_signal block for a concept pair.

Examples:
  uv run python scripts/cohd_pair_to_signal.py \
      --concept-a 436672 --concept-b 80502

  uv run python scripts/cohd_pair_to_signal.py \
      --query-a "disorder of copper metabolism" \
      --query-b "osteoporosis" \
      --show-candidates
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

import httpx
import yaml


DEFAULT_BASE_URL = "https://cohd-api.transltr.io"
DEFAULT_DATASET_ID = 3
DEFAULT_PRECISION_COUNT_THRESHOLD = 10


@dataclass
class ResolvedConcept:
    concept_id: int
    concept_name: str
    vocabulary_id: str
    concept_code: str
    domain_id: str
    resolution_note: str


class COHDClient:
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(timeout=timeout, follow_redirects=True)

    def close(self) -> None:
        self.client.close()

    def _get(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.base_url}/api/{path.lstrip('/')}"
        response = self.client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def datasets(self) -> list[dict[str, Any]]:
        return self._get("metadata/datasets", params={}).get("results", [])

    def find_concepts(self, query: str, dataset_id: int, min_count: int = 1) -> list[dict[str, Any]]:
        data = self._get(
            "omop/findConceptIDs",
            params={"q": query, "dataset_id": dataset_id, "min_count": min_count},
        )
        return data.get("results", [])

    def concept(self, concept_id: int, dataset_id: int) -> dict[str, Any] | None:
        data = self._get("omop/concepts", params={"q": concept_id, "dataset_id": dataset_id})
        results = data.get("results", [])
        if not results:
            return None
        # Prefer exact ID if multiple returned.
        for row in results:
            if int(row.get("concept_id", -1)) == int(concept_id):
                return row
        return results[0]

    def single_concept_freq(self, concept_id: int, dataset_id: int) -> dict[str, Any] | None:
        data = self._get(
            "frequencies/singleConceptFreq",
            params={"dataset_id": dataset_id, "q": concept_id},
        )
        results = data.get("results", [])
        return results[0] if results else None

    def paired_concept_freq(self, concept_id_1: int, concept_id_2: int, dataset_id: int) -> dict[str, Any] | None:
        data = self._get(
            "frequencies/pairedConceptFreq",
            params={"dataset_id": dataset_id, "q": f"{concept_id_1},{concept_id_2}"},
        )
        results = data.get("results", [])
        return results[0] if results else None

    def relative_frequency(self, concept_id_1: int, concept_id_2: int, dataset_id: int) -> dict[str, Any] | None:
        data = self._get(
            "association/relativeFrequency",
            params={
                "dataset_id": dataset_id,
                "concept_id_1": concept_id_1,
                "concept_id_2": concept_id_2,
            },
        )
        results = data.get("results", [])
        return results[0] if results else None

    def obs_exp_ratio(self, concept_id_1: int, concept_id_2: int, dataset_id: int) -> dict[str, Any] | None:
        data = self._get(
            "association/obsExpRatio",
            params={
                "dataset_id": dataset_id,
                "concept_id_1": concept_id_1,
                "concept_id_2": concept_id_2,
            },
        )
        results = data.get("results", [])
        return results[0] if results else None

    def chi_square(self, concept_id_1: int, concept_id_2: int, dataset_id: int) -> dict[str, Any] | None:
        data = self._get(
            "association/chiSquare",
            params={
                "dataset_id": dataset_id,
                "concept_id_1": concept_id_1,
                "concept_id_2": concept_id_2,
            },
        )
        results = data.get("results", [])
        return results[0] if results else None


def _require_one(value: str | None, concept_id: int | None, label: str) -> None:
    if value is None and concept_id is None:
        raise SystemExit(f"Provide one of --concept-{label} or --query-{label}.")


def _print_candidates(label: str, query: str, rows: list[dict[str, Any]], top_k: int) -> None:
    print(f"{label} candidates for query '{query}':", file=sys.stderr)
    if not rows:
        print("  (none)", file=sys.stderr)
        return
    for idx, row in enumerate(rows[:top_k]):
        print(
            f"  [{idx}] {row.get('concept_id')} | {row.get('concept_name')} "
            f"(count={row.get('concept_count')}, {row.get('vocabulary_id')}:{row.get('concept_code')})",
            file=sys.stderr,
        )


def resolve_concept(
    client: COHDClient,
    *,
    concept_id: int | None,
    query: str | None,
    dataset_id: int,
    pick_index: int,
    show_candidates: bool,
    top_k: int,
    label: str,
) -> ResolvedConcept:
    if concept_id is not None:
        concept_row = client.concept(concept_id, dataset_id)
        if concept_row is None:
            raise SystemExit(f"Could not resolve concept metadata for ID {concept_id}.")
        return ResolvedConcept(
            concept_id=int(concept_row["concept_id"]),
            concept_name=concept_row.get("concept_name", ""),
            vocabulary_id=concept_row.get("vocabulary_id", ""),
            concept_code=concept_row.get("concept_code", ""),
            domain_id=concept_row.get("domain_id", ""),
            resolution_note=f"Resolved from explicit OMOP concept ID {concept_id}.",
        )

    assert query is not None  # guarded by argument validation
    rows = client.find_concepts(query, dataset_id)
    if show_candidates:
        _print_candidates(label, query, rows, top_k)
    if not rows:
        raise SystemExit(f"No COHD concepts found for query '{query}'.")
    if pick_index < 0 or pick_index >= len(rows):
        raise SystemExit(
            f"--pick-{label} index {pick_index} out of range for query '{query}' ({len(rows)} candidates)."
        )
    chosen = rows[pick_index]
    return ResolvedConcept(
        concept_id=int(chosen["concept_id"]),
        concept_name=chosen.get("concept_name", ""),
        vocabulary_id=chosen.get("vocabulary_id", ""),
        concept_code=chosen.get("concept_code", ""),
        domain_id=chosen.get("domain_id", ""),
        resolution_note=(
            f"Resolved from query '{query}' using candidate index {pick_index} "
            f"(concept_count={chosen.get('concept_count')})."
        ),
    )


def _dataset_label(client: COHDClient, dataset_id: int) -> str:
    for row in client.datasets():
        if int(row.get("dataset_id", -1)) == dataset_id:
            return row.get("dataset_name", f"dataset_id={dataset_id}")
    return f"dataset_id={dataset_id}"


def _safe_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def build_signal(
    *,
    concept_a: ResolvedConcept,
    concept_b: ResolvedConcept,
    dataset_id: int,
    dataset_name: str,
    single_a: dict[str, Any] | None,
    single_b: dict[str, Any] | None,
    pair_freq: dict[str, Any] | None,
    rel_freq: dict[str, Any] | None,
    obs_exp: dict[str, Any] | None,
    chi_square: dict[str, Any] | None,
) -> dict[str, Any]:
    metrics: list[dict[str, Any]] = []

    if rel_freq is not None:
        rf_metric: dict[str, Any] = {
            "metric_type": "PREVALENCE",
            "metric_value": _safe_float(rel_freq.get("relative_frequency")),
            "notes": "COHD relative frequency for concept pair.",
        }
        ci = rel_freq.get("confidence_interval")
        if isinstance(ci, list) and len(ci) == 2:
            rf_metric["metric_ci_lower"] = _safe_float(ci[0])
            rf_metric["metric_ci_upper"] = _safe_float(ci[1])
        metrics.append(rf_metric)

    if obs_exp is not None:
        oe_metric: dict[str, Any] = {
            "metric_type": "LOG_OBS_EXP_RATIO",
            "metric_value": _safe_float(obs_exp.get("ln_ratio")),
            "notes": "Natural-log observed/expected co-occurrence ratio from COHD.",
        }
        ci = obs_exp.get("confidence_interval")
        if isinstance(ci, list) and len(ci) == 2:
            oe_metric["metric_ci_lower"] = _safe_float(ci[0])
            oe_metric["metric_ci_upper"] = _safe_float(ci[1])
        metrics.append(oe_metric)

    if chi_square is not None:
        metrics.append(
            {
                "metric_type": "CHI_SQUARE",
                "metric_value": _safe_float(chi_square.get("chi_square")),
                "p_value": _safe_float(chi_square.get("p-value")),
                "fdr": _safe_float(chi_square.get("adj_p-value")),
                "notes": "Chi-square association statistic from COHD.",
            }
        )

    n_pair = None
    if pair_freq is not None:
        n_pair = pair_freq.get("concept_count")
    elif rel_freq is not None:
        n_pair = rel_freq.get("concept_pair_count")
    elif chi_square is not None:
        n_pair = chi_square.get("n_c1_c2")

    n_a = single_a.get("concept_count") if single_a is not None else None
    n_b = single_b.get("concept_count") if single_b is not None else None
    precision_threshold = DEFAULT_PRECISION_COUNT_THRESHOLD
    limited_precision = bool(n_pair is not None and n_pair < precision_threshold)

    notes_parts = [
        f"Generated from COHD on {datetime.now(timezone.utc).isoformat()}",
        f"dataset_id={dataset_id} ({dataset_name})",
    ]
    if n_a is not None:
        notes_parts.append(f"n_a={n_a}")
    if n_b is not None:
        notes_parts.append(f"n_b={n_b}")
    if n_pair is not None:
        notes_parts.append(f"n_pair={n_pair}")

    mapping_notes = (
        f"Concept A OMOP:{concept_a.concept_id} "
        f"({concept_a.concept_name}; {concept_a.vocabulary_id}:{concept_a.concept_code}, "
        f"domain={concept_a.domain_id}). "
        f"Concept B OMOP:{concept_b.concept_id} "
        f"({concept_b.concept_name}; {concept_b.vocabulary_id}:{concept_b.concept_code}, "
        f"domain={concept_b.domain_id}). "
        f"{concept_a.resolution_note} {concept_b.resolution_note}"
    )

    signal: dict[str, Any] = {
        "source": "COHD",
        "method": "EHR_COHORT_ASSOCIATION",
        "signal_disorder_a_id": f"OMOP:{concept_a.concept_id}",
        "signal_disorder_b_id": f"OMOP:{concept_b.concept_id}",
        "population": (
            f"COHD dataset_id={dataset_id} ({dataset_name}), patient-level co-occurrence in "
            "Columbia University Irving Medical Center OMOP data."
        ),
        "mapping_notes": mapping_notes,
        "disorder_a_count": n_a,
        "disorder_b_count": n_b,
        "pair_count": n_pair,
        "limited_precision": limited_precision,
        "precision_count_threshold": precision_threshold,
        "directionality": "UNKNOWN",
        "notes": "; ".join(notes_parts),
    }

    # Keep payload compact by omitting unknown count fields.
    for key in ("disorder_a_count", "disorder_b_count", "pair_count"):
        if signal.get(key) is None:
            signal.pop(key, None)

    if metrics:
        signal["statistics"] = {"metrics": metrics}

    return signal


def _write_output(payload: Any, output: str | None, fmt: str) -> None:
    if fmt == "json":
        rendered = json.dumps(payload, indent=2)
    else:
        rendered = yaml.safe_dump(payload, sort_keys=False)

    if output:
        with open(output, "w", encoding="utf-8") as handle:
            handle.write(rendered)
    else:
        sys.stdout.write(rendered)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="COHD API base URL.")
    parser.add_argument("--dataset-id", type=int, default=DEFAULT_DATASET_ID, help="COHD dataset_id.")

    group_a = parser.add_mutually_exclusive_group(required=True)
    group_a.add_argument("--concept-a", type=int, help="OMOP concept ID for disorder A.")
    group_a.add_argument("--query-a", help="Concept search query for disorder A.")

    group_b = parser.add_mutually_exclusive_group(required=True)
    group_b.add_argument("--concept-b", type=int, help="OMOP concept ID for disorder B.")
    group_b.add_argument("--query-b", help="Concept search query for disorder B.")

    parser.add_argument("--pick-a", type=int, default=0, help="Candidate index to choose for query A.")
    parser.add_argument("--pick-b", type=int, default=0, help="Candidate index to choose for query B.")
    parser.add_argument(
        "--show-candidates",
        action="store_true",
        help="Print query candidates to stderr before selecting.",
    )
    parser.add_argument("--top-k", type=int, default=5, help="How many candidates to print when using --show-candidates.")
    parser.add_argument(
        "--wrap-association-signals",
        action="store_true",
        help="Wrap output as {association_signals: [...]} instead of a list item.",
    )
    parser.add_argument("--format", choices=("yaml", "json"), default="yaml", help="Output format.")
    parser.add_argument("--output", help="Write output to file instead of stdout.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    _require_one(args.query_a, args.concept_a, "a")
    _require_one(args.query_b, args.concept_b, "b")

    client = COHDClient(args.base_url)
    try:
        concept_a = resolve_concept(
            client,
            concept_id=args.concept_a,
            query=args.query_a,
            dataset_id=args.dataset_id,
            pick_index=args.pick_a,
            show_candidates=args.show_candidates,
            top_k=args.top_k,
            label="a",
        )
        concept_b = resolve_concept(
            client,
            concept_id=args.concept_b,
            query=args.query_b,
            dataset_id=args.dataset_id,
            pick_index=args.pick_b,
            show_candidates=args.show_candidates,
            top_k=args.top_k,
            label="b",
        )

        dataset_name = _dataset_label(client, args.dataset_id)

        single_a = client.single_concept_freq(concept_a.concept_id, args.dataset_id)
        single_b = client.single_concept_freq(concept_b.concept_id, args.dataset_id)
        pair_freq = client.paired_concept_freq(concept_a.concept_id, concept_b.concept_id, args.dataset_id)
        rel_freq = client.relative_frequency(concept_a.concept_id, concept_b.concept_id, args.dataset_id)
        obs_exp = client.obs_exp_ratio(concept_a.concept_id, concept_b.concept_id, args.dataset_id)
        chi_square = client.chi_square(concept_a.concept_id, concept_b.concept_id, args.dataset_id)

        signal = build_signal(
            concept_a=concept_a,
            concept_b=concept_b,
            dataset_id=args.dataset_id,
            dataset_name=dataset_name,
            single_a=single_a,
            single_b=single_b,
            pair_freq=pair_freq,
            rel_freq=rel_freq,
            obs_exp=obs_exp,
            chi_square=chi_square,
        )

        payload: Any
        if args.wrap_association_signals:
            payload = {"association_signals": [signal]}
        else:
            payload = [signal]

        _write_output(payload, args.output, args.format)
        return 0
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
