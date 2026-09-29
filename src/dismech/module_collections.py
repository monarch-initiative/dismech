"""Loading and structural checks for curated mechanism-module collections."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path

from .yaml_io import safe_load_path


def load_module_collections(input_dir: Path) -> list[tuple[Path, dict]]:
    """Load collection YAML files in stable filename order."""
    if not input_dir.exists():
        return []
    return [
        (path, safe_load_path(path) or {}) for path in sorted(input_dir.glob("*.yaml"))
    ]


def module_collection_reference_errors(
    collections: Iterable[tuple[Path, dict]], module_stems: set[str]
) -> list[str]:
    """Return duplicate and foreign-key errors for module collections."""
    loaded = list(collections)
    names: dict[str, Path] = {}
    errors: list[str] = []

    for path, collection in loaded:
        name = str(collection.get("name") or "").strip()
        if not name:
            errors.append(f"{path}: missing name")
            continue
        if name in names:
            errors.append(
                f"{path}: duplicate collection name {name!r} (also {names[name]})"
            )
        else:
            names[name] = path

        seen_modules: set[str] = set()
        for index, member in enumerate(collection.get("module_members") or []):
            stem = str((member or {}).get("module") or "").strip()
            location = f"{path}: module_members[{index}].module"
            if not stem:
                errors.append(f"{location}: missing module reference")
                continue
            if "#" in stem:
                errors.append(f"{location}: node anchors are not allowed ({stem!r})")
            if stem not in module_stems:
                errors.append(f"{location}: no kb/modules/{stem}.yaml")
            if stem in seen_modules:
                errors.append(f"{location}: duplicate module {stem!r}")
            seen_modules.add(stem)

    known_names = set(names)
    children_by_name: dict[str, list[str]] = {}
    for path, collection in loaded:
        name = str(collection.get("name") or "").strip()
        children = [
            str(child).strip() for child in collection.get("child_collections") or []
        ]
        children_by_name[name] = children
        for index, child in enumerate(children):
            location = f"{path}: child_collections[{index}]"
            if child not in known_names:
                errors.append(f"{location}: unknown collection {child!r}")
            if child == name:
                errors.append(f"{location}: collection cannot contain itself")

    def visit(name: str, stack: tuple[str, ...]) -> None:
        if name in stack:
            cycle = " -> ".join((*stack[stack.index(name) :], name))
            errors.append(f"module collection cycle: {cycle}")
            return
        for child in children_by_name.get(name, []):
            if child in known_names:
                visit(child, (*stack, name))

    for name in sorted(known_names, key=str.casefold):
        visit(name, ())

    return list(dict.fromkeys(errors))


def build_module_collection_tree(collections: list[dict]) -> dict:
    """Build a display forest from explicit child-collection references."""
    by_name = {str(item.get("name")): item for item in collections if item.get("name")}
    children_by_parent: dict[str, list[str]] = {}
    parents_by_child: dict[str, list[str]] = defaultdict(list)

    for collection in collections:
        parent = str(collection.get("name") or "")
        if not parent:
            continue
        children = [
            child
            for child in collection.get("child_collection_names") or []
            if child in by_name
        ]
        children_by_parent[parent] = sorted(children, key=str.casefold)
        for child in children:
            parents_by_child[child].append(parent)

    names = sorted(by_name, key=str.casefold)
    roots = [name for name in names if not parents_by_child.get(name)]
    if not roots and names:
        roots = names

    def make_node(name: str, stack: tuple[str, ...] = ()) -> dict:
        item = by_name[name]
        cycle = name in stack
        children = [] if cycle else children_by_parent.get(name, [])
        return {
            "name": item.get("name"),
            "display_name": item.get("display_name"),
            "href": item.get("href"),
            "collection_type": item.get("collection_type"),
            "module_count": item.get("module_count", 0),
            "children": [make_node(child, (*stack, name)) for child in children],
            "is_shared": len(parents_by_child.get(name, [])) > 1,
            "cycle": cycle,
        }

    return {
        "roots": [make_node(name) for name in roots],
        "edge_count": sum(len(children) for children in children_by_parent.values()),
        "nested_count": len(parents_by_child),
        "root_count": len(roots),
    }
