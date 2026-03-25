#!/usr/bin/env python3
"""Add a COHD association signal directly into a comorbidity YAML file.

Examples:
  uv run python scripts/cohd_add_signal_to_comorbidity.py \
      kb/comorbidities/com_Wilsons_Disease__Osteoporosis.yaml \
      --concept-a 436672 --concept-b 80502

  uv run python scripts/cohd_add_signal_to_comorbidity.py \
      kb/comorbidities/com_Wilsons_Disease__Osteoporosis.yaml \
      --query-a "disorder of copper metabolism" \
      --query-b "osteoporosis" \
      --show-candidates \
      --replace-existing
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml

_HELPER_PATH = Path(__file__).with_name("cohd_pair_to_signal.py")
_SPEC = importlib.util.spec_from_file_location("cohd_pair_to_signal", _HELPER_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError(f"Could not load helper module at {_HELPER_PATH}")
_HELPER = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _HELPER
_SPEC.loader.exec_module(_HELPER)

COHDClient = _HELPER.COHDClient
_dataset_label = _HELPER._dataset_label
build_signal = _HELPER.build_signal
resolve_concept = _HELPER.resolve_concept


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("comorbidity_file", type=Path, help="Path to kb/comorbidities/*.yaml file")
    parser.add_argument("--base-url", default="https://cohd-api.transltr.io", help="COHD API base URL.")
    parser.add_argument("--dataset-id", type=int, default=3, help="COHD dataset_id.")

    group_a = parser.add_mutually_exclusive_group(required=True)
    group_a.add_argument("--concept-a", type=int, help="OMOP concept ID for disorder A.")
    group_a.add_argument("--query-a", help="Concept search query for disorder A.")

    group_b = parser.add_mutually_exclusive_group(required=True)
    group_b.add_argument("--concept-b", type=int, help="OMOP concept ID for disorder B.")
    group_b.add_argument("--query-b", help="Concept search query for disorder B.")

    parser.add_argument("--pick-a", type=int, default=0, help="Candidate index for --query-a.")
    parser.add_argument("--pick-b", type=int, default=0, help="Candidate index for --query-b.")
    parser.add_argument(
        "--show-candidates",
        action="store_true",
        help="Print candidate concepts when query mode is used.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="How many candidate concepts to show when --show-candidates is set.",
    )
    parser.add_argument(
        "--replace-existing",
        action="store_true",
        help="Replace existing COHD signal(s) for the same OMOP pair instead of appending.",
    )
    parser.add_argument(
        "--allow-duplicate",
        action="store_true",
        help="Allow appending duplicate COHD pair signals.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the generated signal and exit without editing the file.",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run `just validate-comorbidity <file>` after writing.",
    )
    return parser.parse_args()


def _load_yaml(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Comorbidity file does not exist: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"Comorbidity file must contain a YAML mapping at top level: {path}")
    return data


def _save_yaml(path: Path, data: dict) -> None:
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
    path.write_text(text, encoding="utf-8")


def _pair_matches(signal: dict, a_id: str, b_id: str) -> bool:
    return (
        signal.get("source") == "COHD"
        and signal.get("signal_disorder_a_id") == a_id
        and signal.get("signal_disorder_b_id") == b_id
    )


def main() -> int:
    args = parse_args()

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

        if args.dry_run:
            print(yaml.safe_dump({"association_signals": [signal]}, sort_keys=False))
            return 0

        data = _load_yaml(args.comorbidity_file)
        signals = data.setdefault("association_signals", [])
        if not isinstance(signals, list):
            raise SystemExit("Expected `association_signals` to be a list.")

        a_id = signal["signal_disorder_a_id"]
        b_id = signal["signal_disorder_b_id"]

        existing_idx = [i for i, s in enumerate(signals) if isinstance(s, dict) and _pair_matches(s, a_id, b_id)]

        if existing_idx and not args.allow_duplicate and not args.replace_existing:
            print(
                f"No changes: found existing COHD signal for pair {a_id} -> {b_id}. "
                "Use --replace-existing or --allow-duplicate.",
            )
            return 0

        if args.replace_existing and existing_idx:
            signals = [s for i, s in enumerate(signals) if i not in set(existing_idx)]
            data["association_signals"] = signals

        data["association_signals"].append(signal)
        _save_yaml(args.comorbidity_file, data)
        print(f"Updated {args.comorbidity_file} with COHD signal {a_id} -> {b_id}.")

        if args.validate:
            subprocess.run(
                ["just", "validate-comorbidity", str(args.comorbidity_file)],
                check=True,
            )

        return 0
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
