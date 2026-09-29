"""Derive whole structured assertions from DM YAML without rewriting their meaning."""

import re
from copy import deepcopy
from functools import cache, lru_cache
from pathlib import Path
from typing import Any

from linkml_runtime.utils.schemaview import SchemaView

ANNOTATIONS = {"evidence", "references", "review_notes"}


def pointer_tokens(pointer: str) -> list[str]:
    """Parse RFC 6901, rejecting invalid escapes and non-pointer spellings."""
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise ValueError("Expected an RFC 6901 JSON Pointer")
    if re.search(r"~(?![01])", pointer):
        raise ValueError("Invalid JSON Pointer escape")
    return (
        [p.replace("~1", "/").replace("~0", "~") for p in pointer[1:].split("/")]
        if pointer
        else []
    )


def pointer(parts: list[str]) -> str:
    return "".join("/" + p.replace("~", "~0").replace("/", "~1") for p in parts)


def resolve(document: Any, path: str) -> Any:
    value = document
    for part in pointer_tokens(path):
        if isinstance(value, list):
            if not re.fullmatch(r"0|[1-9][0-9]*", part):
                raise ValueError("Array pointer must use a nonnegative canonical index")
            try:
                value = value[int(part)]
            except IndexError as error:
                raise ValueError(f"Pointer does not resolve: {path}") from error
        elif isinstance(value, dict) and part in value:
            value = value[part]
        else:
            raise ValueError(f"Pointer does not resolve: {path}")
    return value


@lru_cache(maxsize=1)
def schema() -> SchemaView:
    return SchemaView(str(Path(__file__).parents[1] / "schema/dismech.yaml"))


@cache
def class_slots(class_name: str) -> dict:
    """Induce slots once per class during corpus walks."""
    return {s.name: s for s in schema().class_induced_slots(class_name)}


def class_at(path: str) -> str:
    """Resolve containment using the main schema; fail instead of guessing union ranges."""
    parts = pointer_tokens(path)
    current = "Disease"
    i = 0
    while i < len(parts):
        slots = class_slots(current)
        slot = slots.get(parts[i])
        if slot is None:
            raise ValueError(f"Unknown {current} slot in {path}: {parts[i]}")
        current = slot.range
        if current not in schema().all_classes() or current == "Any":
            raise ValueError(
                f"Path does not select an unambiguous assertion class: {path}"
            )
        i += 1
        if slot.multivalued:
            if i >= len(parts) or not re.fullmatch(r"0|[1-9][0-9]*", parts[i]):
                raise ValueError(f"Expected assertion list index in {path}")
            i += 1
    return current


def without_annotations(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            k: without_annotations(v) for k, v in value.items() if k not in ANNOTATIONS
        }
    if isinstance(value, list):
        return [without_annotations(v) for v in value]
    return deepcopy(value)


def assertion_content(value: dict, class_name: str) -> dict:
    """Keep the evidence-owning assertion, excluding independently evidenced edges.

    Pathophysiology.downstream contains CausalEdge assertions. They are outside
    node evidence scope even when their own evidence lists are absent or empty.
    Other nested terms and qualifiers remain part of the owning assertion.
    """
    result = without_annotations(value)
    # Relationship edges have their own evidence scope, whether or not that
    # evidence has been populated. Other compound content (e.g. readouts)
    # remains part of the whole assertion.
    edge_classes = {
        "CausalEdge",
        "TreatmentMechanismTarget",
        "EnvironmentalMechanismTarget",
    }
    for slot in class_slots(class_name).values():
        if slot.range in edge_classes:
            result.pop(slot.name, None)
    return result


def local_context(node: dict, class_name: str) -> dict:
    """Keep ancestor qualifiers, not independent child assertions or their evidence."""
    children = set()
    for slot in class_slots(class_name).values():
        ranges = [slot.range] + [r.range for r in slot.any_of or []]
        if any(
            r in schema().all_classes() and "evidence" in class_slots(r) for r in ranges
        ):
            children.add(slot.name)
    return without_annotations({k: v for k, v in node.items() if k not in children})


def extract_claim(
    document: dict, evidence_path: str, *, context_paths=(), include_downstream=False
) -> dict:
    """Preserve the evidence-owning assertion; lift disease and ancestor scope.

    A selected explanation remains stored but is never used to narrow the assertion.
    Subtype foreign keys are resolved exactly; ambiguous or missing names fail closed.
    include_downstream is only for reconstructing legacy snapshots; current node
    evaluation excludes those independent edges, regardless of this option.
    """
    parts = pointer_tokens(evidence_path)
    if len(parts) < 3 or parts[-2] != "evidence":
        raise ValueError("Select an evidence entry below an assertion object")
    if any(p in ANNOTATIONS for p in parts[:-2]):
        raise ValueError("Cannot extract a claim from inside an annotation")
    assertion_path = pointer(parts[:-2])
    original = resolve(document, assertion_path)
    evidence = resolve(document, evidence_path)
    assertion_type = class_at(assertion_path)
    if not isinstance(original, dict) or not isinstance(evidence, dict):
        raise ValueError("Assertion and evidence must be objects")
    if "evidence" not in class_slots(assertion_type):
        raise ValueError("Selected class cannot own evidence")
    if not isinstance(document.get("name"), str) or not document["name"].strip():
        raise ValueError("Disease name is required")
    if evidence.get("supports") not in {"SUPPORT", "REFUTE", "NO_EVIDENCE"}:
        raise ValueError("Evidence direction must be explicit; do not infer SUPPORT")
    if not isinstance(evidence.get("snippet"), str) or not evidence["snippet"].strip():
        raise ValueError("Selected snippet is required")
    identity = {
        k: deepcopy(document[k]) for k in ("name", "disease_term") if k in document
    }
    bindings = []
    scopes = [original]
    for i in range(1, len(parts) - 2):
        path = pointer(parts[:i])
        parent = resolve(document, path)
        if isinstance(parent, dict):
            bindings.append(
                {
                    "path": path,
                    "value": local_context(parent, class_at(path)),
                    "role": "ancestor",
                }
            )
            scopes.append(parent)
    # Include the original subtype definition, not an inferred disease rename.
    for scope in scopes:
        names = ([scope["subtype"]] if scope.get("subtype") else []) + scope.get(
            "subtypes", []
        )
        for name in names:
            matches = [
                (i, s)
                for i, s in enumerate(document.get("has_subtypes", []))
                if s.get("name") == name
            ]
            if len(matches) != 1:
                raise ValueError(f"Subtype must resolve uniquely: {name}")
            i, subtype = matches[0]
            binding = {
                "path": f"/has_subtypes/{i}",
                "value": local_context(subtype, "Subtype"),
                "role": "subtype",
            }
            if binding not in bindings:
                bindings.append(binding)
    for path in context_paths:
        if any(p in ANNOTATIONS for p in pointer_tokens(path)):
            raise ValueError(
                "Evidence and review annotations cannot supply claim context"
            )
        value = resolve(document, path)
        bindings.append(
            {"path": path, "value": without_annotations(value), "role": "explicit"}
        )
    return {
        "about": {"disease": identity, "context": bindings},
        "assertion_type": assertion_type,
        "assertion": (
            without_annotations(original)
            if include_downstream
            else assertion_content(original, assertion_type)
        ),
        "selected_evidence": deepcopy(evidence),
        "origin": {
            "assertion_path": assertion_path,
            "evidence_path": evidence_path,
            "context_paths": ["/" + k for k in identity]
            + [b["path"] for b in bindings],
        },
    }
