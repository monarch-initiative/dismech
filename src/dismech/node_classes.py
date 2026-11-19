"""Parser for the compact pathograph node-class tree.

``kb/node_classes/pathograph_node_classes.txt`` holds a classification of
pathograph nodes as an indented plain-text tree whose leaves are real
``(node name, disease)`` pairs from ``kb/disorders/``. The format was written
by hand because compactness is the point: the whole classification is readable
in one screen and a category can be added, moved, or argued with in a single
line. This module makes that text machine-readable without giving up the
compactness, so the tree can be checked in CI and converted to YAML/JSON.

The tree is curated content (it lives under ``kb/``). Since its v1.0 its
classes are also the values of ``Pathophysiology.node_class``, through an enum
this module generates (:func:`render_enum_module`, ``just gen-node-class-enum``).

Grammar
-------
Indentation is **exactly two spaces per level**; tabs are rejected. Blank lines
are ignored. Every other line is classified by its **first non-space
character**, so a line's kind never depends on invisible spacing:

``# ...``
    A **comment**, ignored by the parser. The prose notes stay where they are.

``[Disease_Entry] Node name``
    An **example**: a real pathophysiology node cited as a representative of
    the enclosing class. The bracketed slug is the ``kb/`` entry; the rest of
    the line is the node's ``name`` verbatim.

``:key free text value``
    An **attribute** of the nearest enclosing node (class or example).
    Repeats accumulate, so a debundle proposal can carry several ``:split``
    lines.

``= expression``
    The class's **logical definition** -- a sufficient condition over the
    ontology-bound slots a node carries, in the small language documented in
    :mod:`dismech.node_class_definitions`. At most one per class; not allowed
    on an example.

``CLASS NAME -- optional gloss``
    Anything else is a **class**. The gloss follows `` -- `` (space, two
    dashes, space) and is the human-readable definition; a class name may
    therefore contain single spaces but not that separator.

Class names must be unique among siblings, depth may increase by at most one
level per line, and an example may carry attributes but not class children.
"""

from __future__ import annotations

import functools
import json
import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dismech.node_class_definitions import Definition, DefinitionError, parse_definition
from dismech.repo_root import repo_root

INDENT = 2

#: ``[Disease_Entry] Node name`` -- a bracketed slug opens an example line.
EXAMPLE_RE = re.compile(r"^\[(?P<disease>[^\[\]]+)\]\s*(?P<node>.*)$")
#: ``:key value`` -- key is a single bare word.
ATTR_RE = re.compile(r"^:(?P<key>[A-Za-z][\w-]*)\s*(?P<value>.*)$")
#: ``NAME -- gloss`` -- the separator is a spaced double dash.
GLOSS_SEP = " -- "
#: Attribute recording that an example's node was split out of a bundled node
#: the tree used to cite. ``--verify-kb`` checks the old node is really gone.
SPLIT_FROM = "split_from"
#: ``# VERSION 1.0 (2026-11-04)`` -- the one comment line a tool reads.
VERSION_RE = re.compile(r"^# VERSION (?P<version>\d+\.\d+)\b", re.MULTILINE)
#: Top-level classes whose subtrees are not ``node_class`` values. ALSO CLASSES
#: answers a different question than the slot (a compensating node is also a
#: cellular or tissue effect); DEBUNDLE TARGETS and STILL UNPLACED are worklists.
NON_VALUE_ROOTS = frozenset({"ALSO CLASSES", "DEBUNDLE TARGETS", "STILL UNPLACED"})
#: The packaged copy of the generated schema module, which dismech.yaml imports.
#: Read it from here; write and check it through :func:`checkout_enum_schema`.
ENUM_SCHEMA = Path(__file__).parent / "schema" / "pathograph_node_class.yaml"
ENUM_NAME = "PathographNodeClassEnum"
ENUM_HEADER = (
    "# GENERATED from kb/node_classes/pathograph_node_classes.txt by\n"
    "# `just gen-node-class-enum`. Do not edit by hand: edit the tree and\n"
    "# regenerate. tests/test_node_classes.py fails while the two disagree.\n"
)
#: What to do when ``--verify-kb`` finds an example whose node has gone.
STALE_EXAMPLE_HINT = (
    "an example names a node or entry that is gone: re-point a renamed one; if "
    "the node was SPLIT, file each half under its own class with "
    f"':{SPLIT_FROM} <old node name>' instead of deleting the example"
)


class ParseError(ValueError):
    """A node-class file could not be parsed. Carries the offending line."""

    def __init__(self, source: str, line: int, message: str) -> None:
        super().__init__(f"{source}:{line}: {message}")
        self.source = source
        self.line = line
        self.message = message


def _slug(name: str) -> str:
    """Derive a stable upper-snake identifier from a human class name."""
    return re.sub(r"[^A-Z0-9]+", "_", name.upper()).strip("_")


@dataclass
class Example:
    """A real ``(node, disease)`` pair cited under a class."""

    node: str
    disease: str
    line: int
    attributes: dict[str, list[str]] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"node": self.node, "disease": self.disease}
        if self.attributes:
            out["attributes"] = {k: list(v) for k, v in self.attributes.items()}
        return out


@dataclass
class ClassNode:
    """One class in the tree, with its sub-classes and cited examples."""

    name: str
    line: int
    gloss: str | None = None
    #: the ``= expression`` line, verbatim; parsed on demand
    definition: str | None = None
    children: list[ClassNode] = field(default_factory=list)
    examples: list[Example] = field(default_factory=list)
    attributes: dict[str, list[str]] = field(default_factory=dict)

    @property
    def id(self) -> str:
        """Upper-snake identifier, the candidate enum/class name."""
        return _slug(self.name)

    @property
    def parsed_definition(self) -> Definition | None:
        return parse_definition(self.definition) if self.definition else None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"id": self.id, "name": self.name}
        if self.gloss:
            out["gloss"] = self.gloss
        if self.definition:
            out["definition"] = self.definition
        if self.attributes:
            out["attributes"] = {k: list(v) for k, v in self.attributes.items()}
        if self.examples:
            out["examples"] = [e.to_dict() for e in self.examples]
        if self.children:
            out["children"] = [c.to_dict() for c in self.children]
        return out


def _add_attribute(target: ClassNode | Example, key: str, value: str) -> None:
    target.attributes.setdefault(key, []).append(value)


def _close_deeper(last_at_depth: dict[int, ClassNode | Example], depth: int) -> None:
    """Forget the nodes a new line at ``depth`` has just closed.

    ``last_at_depth`` is what an attribute line consults to find its owner. It
    must shrink with the class stack: without this, a misindented attribute
    resolves to a node in an already-closed subtree and attaches there silently,
    which is the one failure the parser exists to make loud.
    """
    for deeper in [d for d in last_at_depth if d > depth]:
        del last_at_depth[deeper]


def parse_text(text: str, *, source: str = "<text>") -> list[ClassNode]:
    """Parse node-class text into a forest of :class:`ClassNode` roots.

    Raises :class:`ParseError` with a line number on any grammar violation.
    """
    roots: list[ClassNode] = []
    # stack[d] is the class opened at depth d; examples are tracked separately
    # so an attribute line can attach to whichever was most recently opened.
    stack: list[ClassNode] = []
    last_at_depth: dict[int, ClassNode | Example] = {}

    for lineno, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise ParseError(source, lineno, "tab in indentation; use spaces")

        spaces = len(raw) - len(raw.lstrip(" "))
        if spaces % INDENT:
            raise ParseError(
                source, lineno, f"indent {spaces} is not a multiple of {INDENT}"
            )
        depth = spaces // INDENT
        content = raw.strip()

        attr = ATTR_RE.match(content)
        if attr:
            owner = last_at_depth.get(depth - 1)
            if owner is None:
                raise ParseError(
                    source, lineno, "attribute line has no enclosing node"
                )
            _add_attribute(owner, attr.group("key"), attr.group("value").strip())
            continue

        if content.startswith("="):
            owner = last_at_depth.get(depth - 1)
            if owner is None:
                raise ParseError(
                    source, lineno, "definition line has no enclosing class"
                )
            if isinstance(owner, Example):
                raise ParseError(
                    source, lineno, "a definition belongs to a class, not an example"
                )
            if owner.definition is not None:
                raise ParseError(
                    source, lineno, f"class {owner.name!r} already has a definition"
                )
            expression = content[1:].strip()
            try:
                parse_definition(expression)
            except DefinitionError as exc:
                raise ParseError(source, lineno, f"bad definition: {exc}") from exc
            owner.definition = expression
            continue

        example = EXAMPLE_RE.match(content)
        if example:
            # Guarded before the generic depth check so an example with no open
            # class reports what is actually wrong with it.
            if depth == 0 or depth > len(stack):
                raise ParseError(source, lineno, "example outside any class")
            node_name = example.group("node").strip()
            if not node_name:
                raise ParseError(source, lineno, "example line has no node name")
            parent = stack[depth - 1]
            ex = Example(
                node=node_name,
                disease=example.group("disease").strip(),
                line=lineno,
            )
            parent.examples.append(ex)
            # An example opens no class scope; drop anything deeper.
            del stack[depth:]
            _close_deeper(last_at_depth, depth)
            last_at_depth[depth] = ex
            continue

        if depth > len(stack):
            if not stack:
                raise ParseError(
                    source, lineno, "indented line before any class"
                )
            raise ParseError(
                source,
                lineno,
                f"indent jumps from depth {len(stack) - 1} to {depth}; "
                "increase by one level at a time",
            )

        name, sep, gloss = content.partition(GLOSS_SEP)
        name = name.strip()
        gloss = gloss.strip() if sep else None
        if not name:
            raise ParseError(source, lineno, "class line has an empty name")
        if "[" in name and name.endswith("]"):
            raise ParseError(
                source, lineno, "example lines start with [Disease_Entry]"
            )

        node = ClassNode(name=name, line=lineno, gloss=gloss)
        siblings = roots if depth == 0 else stack[depth - 1].children
        if any(s.name == node.name for s in siblings):
            raise ParseError(
                source, lineno, f"duplicate sibling class name {node.name!r}"
            )
        siblings.append(node)
        del stack[depth:]
        stack.append(node)
        _close_deeper(last_at_depth, depth)
        last_at_depth[depth] = node

    return roots


def parse_file(path: str | Path) -> list[ClassNode]:
    """Parse a node-class file from disk."""
    p = Path(path)
    return parse_text(p.read_text(encoding="utf-8"), source=str(p))


def tree_version(text: str) -> str | None:
    """The ``# VERSION x.y`` the tree declares, or None.

    The parser ignores comments; this is the one comment line a tool reads, so
    the generated ``node_class`` enum can say which version of the tree it was
    generated from.
    """
    match = VERSION_RE.search(text)
    return match.group("version") if match else None


def node_class_values(roots: list[ClassNode]) -> list[tuple[ClassNode, ClassNode | None]]:
    """``(class, parent)`` for every class that is a ``node_class`` value.

    Tree order, so the generated enum reads like the tree. A top-level class
    (a tier) has no parent.
    """
    out: list[tuple[ClassNode, ClassNode | None]] = []

    def walk(node: ClassNode, parent: ClassNode | None) -> None:
        out.append((node, parent))
        for child in node.children:
            walk(child, node)

    for root in roots:
        if root.name not in NON_VALUE_ROOTS:
            walk(root, None)
    return out


def to_linkml_enum(roots: list[ClassNode], version: str) -> dict[str, Any]:
    """The ``node_class`` enum as a LinkML schema module, ready for YAML.

    Each value's ``title`` is the class name, its ``description`` the gloss and
    its ``is_a`` the class it sits under, so the tier of any value can be read
    back from the schema without the tree (see :func:`node_class_tiers`).
    """
    values: dict[str, dict[str, str]] = {}
    for node, parent in node_class_values(roots):
        value: dict[str, str] = {"title": node.name}
        if node.gloss:
            value["description"] = node.gloss
        if parent is not None:
            value["is_a"] = parent.id
        values[node.id] = value
    return {
        "id": "https://w3id.org/monarch-initiative/dismech/pathograph_node_class",
        "name": "dismech-pathograph-node-class",
        "title": "Pathograph Node Classes",
        "version": version,
        "description": (
            "The kinds of causal claim a pathophysiology node can make: the "
            "classes under the nine cascade tiers and DISPOSITION in "
            "kb/node_classes/pathograph_node_classes.txt, whose worked examples "
            "and build notes are the guidance for assigning one. Generated from "
            "that file; design decision 14 records why the vocabulary is curated "
            "content rather than an ontology."
        ),
        "imports": ["linkml:types"],
        "prefixes": {
            "linkml": "https://w3id.org/linkml/",
            "dismech": "https://w3id.org/monarch-initiative/dismech/",
        },
        "default_prefix": "dismech",
        "enums": {
            ENUM_NAME: {
                "description": (
                    "Pathograph node classes, the range of Pathophysiology "
                    "node_class. A value without is_a is a tier; every other "
                    "value names the class it sits under."
                ),
                "permissible_values": values,
            }
        },
    }


def render_enum_module(roots: list[ClassNode], version: str) -> str:
    """The generated schema module's text."""
    import yaml

    body = yaml.safe_dump(
        to_linkml_enum(roots, version), sort_keys=False, width=88, allow_unicode=True
    )
    return ENUM_HEADER + body


def checkout_enum_schema() -> Path:
    """The generated enum module in the checkout the command runs in.

    :data:`ENUM_SCHEMA` names the tree the package was installed from, which
    is right for reading (:func:`node_class_tiers`) but, with one virtualenv
    shared across git worktrees, is the primary checkout: writing there would
    put a worktree's regenerated enum on ``main``, and checking there would
    compare the worktree's tree with ``main``'s enum (#15051). Falls back to
    the packaged copy when the checkout has no ``src/dismech/schema/``, as
    when the package is installed rather than run from source.
    """
    candidate = repo_root() / "src" / "dismech" / "schema" / ENUM_SCHEMA.name
    return candidate if candidate.parent.is_dir() else ENUM_SCHEMA


def stale_enum_problem(
    tree_path: str | Path, enum_path: str | Path | None = None
) -> str | None:
    """Why the committed enum does not match the tree, or None when it does.

    ``enum_path`` defaults to :func:`checkout_enum_schema`, so the tree and
    the enum are read from the same checkout. Parsed YAML is compared, not
    text, so a formatter cannot make it fail.
    """
    import yaml

    if enum_path is None:
        enum_path = checkout_enum_schema()
    text = Path(tree_path).read_text(encoding="utf-8")
    version = tree_version(text)
    if version is None:
        return f"{tree_path} declares no '# VERSION x.y' line"
    expected = to_linkml_enum(parse_text(text, source=str(tree_path)), version)
    try:
        committed = yaml.safe_load(Path(enum_path).read_text(encoding="utf-8"))
    except OSError:
        committed = None
    if committed != expected:
        return (
            f"{enum_path} does not match {tree_path} (tree version {version}): "
            "run `just gen-node-class-enum` and commit both files"
        )
    return None


@functools.lru_cache(maxsize=4)
def node_class_tiers(path: str | Path = ENUM_SCHEMA) -> dict[str, str]:
    """Each ``node_class`` value mapped to the id of the tier it sits under.

    Read from the generated enum rather than the tree, so it needs no checkout
    paths and agrees with what ``linkml-validate`` accepts.
    """
    import yaml

    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    values = data["enums"][ENUM_NAME]["permissible_values"]
    tiers: dict[str, str] = {}
    for value in values:
        top, seen = value, set()
        while (values[top] or {}).get("is_a"):
            if top in seen:
                raise ValueError(f"{path}: is_a cycle at {top}")
            seen.add(top)
            top = values[top]["is_a"]
        tiers[value] = top
    return tiers


def iter_classes(
    roots: list[ClassNode], _trail: tuple[str, ...] = ()
) -> Iterator[tuple[tuple[str, ...], ClassNode]]:
    """Yield ``(path, node)`` for every class, depth-first."""
    for node in roots:
        trail = _trail + (node.name,)
        yield trail, node
        yield from iter_classes(node.children, trail)


def iter_examples(roots: list[ClassNode]) -> Iterator[tuple[tuple[str, ...], Example]]:
    """Yield ``(class path, example)`` for every cited example."""
    for trail, node in iter_classes(roots):
        for ex in node.examples:
            yield trail, ex


def to_dict(roots: list[ClassNode]) -> dict[str, Any]:
    """Serialize the forest to a plain dict, ready for YAML or JSON."""
    return {"classes": [r.to_dict() for r in roots]}


def render_text(roots: list[ClassNode]) -> str:
    """Render the forest back to the compact text form (round-trips)."""
    lines: list[str] = []

    def emit_attrs(owner: ClassNode | Example, depth: int) -> None:
        pad = " " * (INDENT * depth)
        for key, values in owner.attributes.items():
            for value in values:
                lines.append(f"{pad}:{key} {value}".rstrip())

    def walk(node: ClassNode, depth: int) -> None:
        pad = " " * (INDENT * depth)
        lines.append(f"{pad}{node.name}{GLOSS_SEP}{node.gloss}" if node.gloss else f"{pad}{node.name}")
        if node.definition:
            lines.append(f"{pad}{' ' * INDENT}= {node.definition}")
        emit_attrs(node, depth + 1)
        for ex in node.examples:
            lines.append(f"{pad}{' ' * INDENT}[{ex.disease}] {ex.node}")
            emit_attrs(ex, depth + 2)
        for child in node.children:
            walk(child, depth + 1)

    for root in roots:
        walk(root, 0)
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def verify_examples(
    roots: list[ClassNode], kb_dirs: list[Path]
) -> list[str]:
    """Check every example resolves to a real pathophysiology node in ``kb/``.

    This is the check that was being run by hand while the tree was drafted: a
    class tree whose leaves have drifted from the knowledge base is worse than
    no tree, because it looks grounded. Returns a list of human-readable
    problems; empty means every example resolved.
    """
    from dismech.yaml_io import safe_load

    known: set[tuple[str, str]] = set()
    diseases: set[str] = set()
    for kb_dir in kb_dirs:
        for path in sorted(kb_dir.glob("*.yaml")):
            diseases.add(path.stem)
            try:
                data = safe_load(path.read_text(encoding="utf-8"))
            except Exception:  # a malformed KB file is not this check's business
                continue
            for node in (data or {}).get("pathophysiology") or []:
                name = node.get("name")
                if name:
                    known.add((str(name), path.stem))

    problems: list[str] = []
    for trail, ex in iter_examples(roots):
        where = " > ".join(trail)
        for old in ex.attributes.get(SPLIT_FROM, []):
            if (old, ex.disease) in known:
                problems.append(
                    f"line {ex.line}: :{SPLIT_FROM} names {old!r}, but "
                    f"{ex.disease} still has a node of that name ({where})"
                )
        if (ex.node, ex.disease) in known:
            continue
        if ex.disease not in diseases:
            problems.append(
                f"line {ex.line}: no such entry {ex.disease!r} ({where})"
            )
        else:
            problems.append(
                f"line {ex.line}: {ex.disease} has no pathophysiology node "
                f"named {ex.node!r} ({where})"
            )
    return problems


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m dismech.node_classes",
        description="Parse and check the compact pathograph node-class tree.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="kb/node_classes/pathograph_node_classes.txt",
        help="node-class text file (default: %(default)s)",
    )
    parser.add_argument(
        "--format",
        choices=("check", "yaml", "json", "text", "summary", "linkml-enum"),
        default="check",
        help="output format; 'check' parses and reports nothing on success; "
        "'linkml-enum' prints the generated node_class enum module",
    )
    parser.add_argument(
        "--write-enum",
        action="store_true",
        help="write the generated node_class enum module to "
        f"src/dismech/schema/{ENUM_SCHEMA.name} in the checkout the command runs in",
    )
    parser.add_argument(
        "--check-enum",
        action="store_true",
        help=f"fail if the checkout's committed {ENUM_SCHEMA.name} does not match the tree",
    )
    parser.add_argument(
        "--verify-kb",
        action="store_true",
        help="also check every example resolves in kb/ (slow: parses the KB)",
    )
    parser.add_argument(
        "--kb-dir",
        action="append",
        default=None,
        help="KB directory to verify against (repeatable; "
        "default: kb/disorders and kb/modules)",
    )
    parser.add_argument(
        "--check-definitions",
        action="store_true",
        help="check every `=` line's CURIE labels against cache/<prefix>/terms.csv "
        "(offline; a term absent from the cache is reported but not failed)",
    )
    parser.add_argument(
        "--online",
        action="store_true",
        help="with --check-definitions: resolve labels from the ontology (OLS) "
        "instead of the local caches; there an unresolved CURIE is a failure",
    )
    parser.add_argument(
        "--evaluate",
        action="store_true",
        help="evaluate every definition against its examples and the whole KB "
        "(slow; the GO is_a closure comes from --go-obo or the local OAK GO "
        "sqlite build, which is never downloaded implicitly)",
    )
    parser.add_argument(
        "--go-obo",
        metavar="PATH",
        help="with --evaluate: read the GO is_a closure from this OBO file "
        "(e.g. go-basic.obo) instead of the local sqlite:obo:go build",
    )
    args = parser.parse_args(argv)

    try:
        roots = parse_file(args.path)
    except ParseError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    problems: list[str] = []
    if args.check_definitions:
        from dismech.node_class_definitions import (
            cache_label_lookup,
            check_labels,
            curie_labels,
            ontology_label_lookup,
            triage_label_problems,
        )

        defined = [n.parsed_definition for _, n in iter_classes(roots) if n.definition]
        lookup = ontology_label_lookup() if args.online else cache_label_lookup()
        source = "the ontology" if args.online else "the term cache"
        found = check_labels(curie_labels(d for d in defined if d), lookup)
        # Offline, an unresolved CURIE is merely unchecked and is reported
        # without failing. Online the ontology is authoritative, so a CURIE it
        # does not know is a fabricated term and fails the run.
        failures, unchecked = triage_label_problems(found, authoritative=args.online)
        for problem in unchecked:
            print(f"{args.path}: definition term {problem.render(source)} -- not checked", file=sys.stderr)
        problems.extend(f"definition term {p.render(source)}" for p in failures)
        print(f"checked {len(defined)} definitions", file=sys.stderr)

    if args.evaluate:
        from dismech.node_class_definitions import (
            evaluate_tree,
            go_ancestors,
            obo_ancestors,
        )
        from dismech.oak_db import local_build_present

        if args.go_obo:
            ancestors = obo_ancestors(args.go_obo)
        elif local_build_present("sqlite:obo:go"):
            ancestors = go_ancestors()
        else:
            # Opening the adapter would download the build silently (CLAUDE.md,
            # "An oak_db test needs two guards"), so ask instead.
            print(
                "error: --evaluate needs the GO is_a closure: pass --go-obo "
                "go-basic.obo, or fetch the build with `just fetch-ontology-dbs go`",
                file=sys.stderr,
            )
            return 2
        kb_dirs = [Path(d) for d in (args.kb_dir or ["kb/disorders", "kb/modules"])]
        reports = evaluate_tree(roots, kb_dirs, ancestors)
        print(f"{'class':58s} {'ex':>4s} {'hit':>4s} {'recall':>7s} {'kb':>6s}  cross-hits")
        for r in reports:
            cross = ", ".join(
                f"{' > '.join(k[-1:])}={v}" for k, v in sorted(r.cross_hits.items(), key=lambda kv: -kv[1])[:4]
            )
            # A tier's examples sit on its leaves; score it over all of them.
            tier = r.subtree_examples > r.examples
            ex, hit = (r.subtree_examples, r.subtree_matched) if tier else (r.examples, r.examples_matched)
            recall = r.subtree_recall if tier else r.recall
            print(
                f"{' > '.join(r.path)[:58]:58s} {ex:4d} {hit:4d} "
                f"{100 * recall:6.0f}%{'*' if tier else ' '}{r.kb_matched:6d}  {cross}"
            )
        total_ex = sum(r.examples for r in reports)
        total_hit = sum(r.examples_matched for r in reports)
        print(
            f"\n{len(reports)} definitions; {total_hit}/{total_ex} of their own examples "
            f"satisfied ({100 * total_hit / total_ex if total_ex else 0:.0f}%); "
            "* = scored over every example beneath the class",
            file=sys.stderr,
        )

    if args.verify_kb:
        kb_dirs = [Path(d) for d in (args.kb_dir or ["kb/disorders", "kb/modules"])]
        missing = [d for d in kb_dirs if not d.is_dir()]
        if missing:
            print(
                "error: not a directory: " + ", ".join(str(d) for d in missing),
                file=sys.stderr,
            )
            return 2
        problems.extend(verify_examples(roots, kb_dirs))

    if args.check_enum:
        stale = stale_enum_problem(args.path)
        if stale:
            problems.append(stale)

    if args.format == "linkml-enum" or args.write_enum:
        version = tree_version(Path(args.path).read_text(encoding="utf-8"))
        if version is None:
            print(f"error: {args.path} declares no '# VERSION x.y' line", file=sys.stderr)
            return 1
        module = render_enum_module(roots, version)
        if args.write_enum:
            target = checkout_enum_schema()
            target.write_text(module, encoding="utf-8")
            print(f"wrote {target} (tree version {version})", file=sys.stderr)
        if args.format == "linkml-enum":
            print(module, end="")

    if args.format == "json":
        print(json.dumps(to_dict(roots), indent=2))
    elif args.format == "yaml":
        import yaml

        print(yaml.safe_dump(to_dict(roots), sort_keys=False, width=100), end="")
    elif args.format == "text":
        print(render_text(roots), end="")
    elif args.format == "summary":
        classes = list(iter_classes(roots))
        examples = list(iter_examples(roots))
        version = tree_version(Path(args.path).read_text(encoding="utf-8"))
        print(f"tree version {version or 'undeclared'}")
        print(f"{len(roots)} top-level classes, {len(classes)} classes total")
        print(f"{len(examples)} examples across {len({e.disease for _, e in examples})} entries")
        leaves = [n for _, n in classes if not n.children]
        defined = [n for _, n in classes if n.definition]
        print(
            f"{len(defined)} classes carry a logical definition "
            f"({sum(1 for n in leaves if n.definition)} of {len(leaves)} leaves)"
        )
        splits = {
            (ex.disease, old)
            for _, ex in examples
            for old in ex.attributes.get(SPLIT_FROM, [])
        }
        print(f"{len(splits)} cited nodes recorded as since split by curators (:{SPLIT_FROM})")
        for trail, node in classes:
            if len(trail) == 1:
                n = sum(1 for t, _ in examples if t[0] == node.name)
                print(f"  {node.id:30s} {n:4d} examples")

    for problem in problems:
        print(f"{args.path}: {problem}", file=sys.stderr)
    if problems:
        if args.verify_kb:
            print(f"hint: {STALE_EXAMPLE_HINT}", file=sys.stderr)
        print(f"error: {len(problems)} problems", file=sys.stderr)
        return 1
    if args.format == "check":
        classes = sum(1 for _ in iter_classes(roots))
        examples = sum(1 for _ in iter_examples(roots))
        suffix = ", all examples resolved in kb/" if args.verify_kb else ""
        print(f"ok: {classes} classes, {examples} examples{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
