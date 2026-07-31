#!/usr/bin/env python3
"""
Convert an OHDSI/ATLAS cohort definition JSON into a dismech definitions YAML fragment.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import httpx
import yaml


def _first_value(data: dict, keys: tuple[str, ...]) -> Any:
    for key in keys:
        if key in data:
            return data[key]
    return None


def _find_container(data: dict, keys: tuple[str, ...]) -> dict:
    for container in (data, data.get("expression", {}), data.get("Expression", {})):
        if isinstance(container, dict) and any(k in container for k in keys):
            return container
    return {}


def _get_concept_sets(data: dict) -> list[dict]:
    container = _find_container(data, ("conceptSets", "ConceptSets", "concept_sets"))
    for key in ("conceptSets", "ConceptSets", "concept_sets"):
        value = container.get(key)
        if isinstance(value, list):
            return value
    return []


def _get_inclusion_rules(data: dict) -> list[dict]:
    container = _find_container(data, ("inclusionRules", "InclusionRules"))
    for key in ("inclusionRules", "InclusionRules"):
        value = container.get(key)
        if isinstance(value, list):
            return value
    return []


def _count_concepts(concept_set: dict) -> int | None:
    expression = concept_set.get("expression")
    if not isinstance(expression, dict):
        return None
    items = expression.get("items")
    if isinstance(items, list):
        return len(items)
    return None


def _prune(value: Any) -> Any:
    if isinstance(value, dict):
        pruned = {k: _prune(v) for k, v in value.items()}
        return {k: v for k, v in pruned.items() if v not in (None, [], {})}
    if isinstance(value, list):
        pruned_list = [_prune(v) for v in value]
        return [v for v in pruned_list if v not in (None, [], {})]
    return value


def fetch_cohort_from_webapi(base_url: str, cohort_id: int, timeout: float = 30.0) -> dict:
    """Fetch a cohort definition live from an OHDSI WebAPI endpoint.

    Calls ``GET {base_url}/cohortdefinition/{cohort_id}``. The WebAPI response is
    an envelope carrying ``name`` / ``description`` plus an ``expression`` field
    that is itself a JSON-encoded *string*. This normalizes ``expression`` into a
    nested dict so the downstream parser sees the same shape as a hand-exported
    ATLAS JSON file. The public ATLAS demo lives at
    ``https://atlas-demo.ohdsi.org/WebAPI``.
    """
    url = f"{base_url.rstrip('/')}/cohortdefinition/{cohort_id}"
    with httpx.Client(timeout=timeout, follow_redirects=True) as client:
        response = client.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
        envelope = response.json()

    expression = envelope.get("expression")
    if isinstance(expression, str):
        try:
            envelope["expression"] = json.loads(expression)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"WebAPI cohort {cohort_id} returned an 'expression' string "
                "that is not valid JSON"
            ) from exc
    return envelope


def build_definition(data: dict, args: argparse.Namespace) -> dict:
    name = args.name or _first_value(data, ("name", "Name")) or "OHDSI cohort definition"
    description = args.description or _first_value(data, ("description", "Description"))
    scope = args.scope or "OMOP CDM (OHDSI)"

    concept_sets = _get_concept_sets(data)
    inclusion_rules = _get_inclusion_rules(data)

    concept_items = []
    for concept_set in concept_sets:
        cs_name = concept_set.get("name") or concept_set.get("Name") or "Concept set"
        cs_id = concept_set.get("id") or concept_set.get("Id")
        count = _count_concepts(concept_set)
        details = []
        if cs_id is not None:
            details.append(f"id {cs_id}")
        if count is not None:
            details.append(f"{count} concept(s)")
        description_bits = ", ".join(details) if details else None
        concept_items.append({
            "preferred_term": f"Concept set: {cs_name}",
            "description": description_bits,
        })

    criteria_sets = []
    if concept_items:
        criteria_sets.append({
            "name": "Primary criteria",
            "description": "Concept sets used to define the cohort entry event.",
            "inclusion_criteria": concept_items,
        })

    for rule in inclusion_rules:
        rule_name = rule.get("name") or rule.get("Name") or "Inclusion rule"
        criteria_sets.append({
            "name": rule_name,
            "description": "Inclusion rule from the cohort definition.",
        })

    definition = {
        "name": name,
        "definition_type": "PHENOTYPE_ALGORITHM",
        "description": description,
        "scope": scope,
        "criteria_sets": criteria_sets,
    }

    return _prune(definition)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert an OHDSI/ATLAS cohort JSON to a dismech definition fragment."
    )
    parser.add_argument(
        "json_path",
        nargs="?",
        type=Path,
        help="Path to cohort JSON exported from ATLAS/WebAPI (omit when using --webapi-url)",
    )
    parser.add_argument(
        "--webapi-url",
        help=(
            "Base URL of an OHDSI WebAPI (e.g. https://atlas-demo.ohdsi.org/WebAPI) "
            "to fetch the cohort definition live instead of reading a local file"
        ),
    )
    parser.add_argument(
        "--cohort-id",
        type=int,
        help="Cohort definition id to fetch from --webapi-url",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout in seconds for the --webapi-url fetch (default: 30)",
    )
    parser.add_argument("--name", help="Override definition name")
    parser.add_argument("--description", help="Override definition description")
    parser.add_argument("--scope", help="Override scope (default: OMOP CDM (OHDSI))")
    parser.add_argument(
        "--wrap",
        action="store_true",
        help="Wrap output in a top-level 'definitions' key",
    )

    args = parser.parse_args()

    if args.webapi_url or args.cohort_id is not None:
        if not (args.webapi_url and args.cohort_id is not None):
            parser.error("--webapi-url and --cohort-id must be given together")
        if args.json_path is not None:
            parser.error("provide either a cohort json_path or --webapi-url/--cohort-id, not both")
        data = fetch_cohort_from_webapi(args.webapi_url, args.cohort_id, timeout=args.timeout)
    elif args.json_path is not None:
        data = json.loads(args.json_path.read_text())
    else:
        parser.error("provide a cohort json_path, or --webapi-url with --cohort-id")

    definition = build_definition(data, args)

    if args.wrap:
        payload = {"definitions": [definition]}
    else:
        payload = [definition]

    yaml.safe_dump(payload, sys.stdout, sort_keys=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
