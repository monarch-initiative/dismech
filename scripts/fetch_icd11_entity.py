#!/usr/bin/env python3
"""Download and parse an ICD-11 entity from the WHO ICD browser or API.

The WHO ICD-11 browser (e.g. ``https://icd.who.int/browse/2026-01/mms/en#314107400``)
is a single-page app: fetching the URL returns only the shell, and the entity
itself is loaded by the embedded coding tool from the ICD API at
``https://id.who.int/icd/release/11/<release>/<linearization>/<entity_id>``.

That API needs a bearer token. Rather than requiring an ICD API account, this
script reuses the same public guest token the browser itself uses: the browser
fetches ``https://icd.who.int/browse/gt`` and de-obfuscates the response with a
character-shift keyed on the 14th character (see ``/browse/js/browser.js``).
Pass ``--token`` to use your own OAuth token instead.

Examples::

    # Parse the entity behind a browser URL
    uv run python scripts/fetch_icd11_entity.py \\
        'https://icd.who.int/browse/2026-01/mms/en#314107400'

    # Raw API JSON, with ancestors and one level of children
    uv run python scripts/fetch_icd11_entity.py 314107400 \\
        --ancestors --children --format json -o LA05.4.json

    # Walk a whole subtree
    uv run python scripts/fetch_icd11_entity.py LA05 --depth 2
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from typing import Any, Iterable
from urllib.parse import urlparse

import httpx

BROWSER_HOST = "https://icd.who.int"
GUEST_TOKEN_URL = f"{BROWSER_HOST}/browse/gt"
API_ROOT = "https://id.who.int/icd/release/11"

DEFAULT_RELEASE = "2026-01"
DEFAULT_LINEARIZATION = "mms"
DEFAULT_LANGUAGE = "en"

USER_AGENT = "dismech-icd11-fetch/1.0 (+https://github.com/monarch-initiative/dismech)"
TIMEOUT = httpx.Timeout(60.0)

# Language-tagged value fields worth surfacing as plain strings.
_TEXT_FIELDS = (
    "title",
    "definition",
    "longDefinition",
    "fullySpecifiedName",
    "codingNote",
    "inclusion",
    "exclusion",
    "note",
)


class IcdError(RuntimeError):
    """Raised when the ICD browser/API cannot be reached or parsed."""


@dataclass
class EntityRef:
    """A resolved pointer to one entity in one linearization release."""

    entity_id: str
    release: str = DEFAULT_RELEASE
    linearization: str = DEFAULT_LINEARIZATION
    language: str = DEFAULT_LANGUAGE

    @property
    def api_url(self) -> str:
        return f"{API_ROOT}/{self.release}/{self.linearization}/{self.entity_id}"

    @property
    def browser_url(self) -> str:
        return (
            f"{BROWSER_HOST}/browse/{self.release}/"
            f"{self.linearization}/{self.language}#{self.entity_id}"
        )

    def sibling(self, entity_id: str) -> "EntityRef":
        """Another entity in the same release/linearization/language."""
        return EntityRef(entity_id, self.release, self.linearization, self.language)


@dataclass
class Entity:
    """The parsed, flattened form of one ICD-11 linearization entity."""

    entity_id: str
    code: str | None = None
    title: str | None = None
    class_kind: str | None = None
    definition: str | None = None
    long_definition: str | None = None
    fully_specified_name: str | None = None
    browser_url: str | None = None
    foundation_uri: str | None = None
    parent_ids: list[str] = field(default_factory=list)
    child_ids: list[str] = field(default_factory=list)
    index_terms: list[str] = field(default_factory=list)
    inclusions: list[str] = field(default_factory=list)
    exclusions: list[str] = field(default_factory=list)
    coding_note: str | None = None
    block_id: str | None = None
    code_range: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    @property
    def curie(self) -> str | None:
        return f"ICD11:{self.code}" if self.code else None

    def to_dict(self, *, include_raw: bool = False) -> dict[str, Any]:
        out: dict[str, Any] = {
            "entity_id": self.entity_id,
            "code": self.code,
            "curie": self.curie,
            "title": self.title,
            "class_kind": self.class_kind,
            "definition": self.definition,
            "long_definition": self.long_definition,
            "fully_specified_name": self.fully_specified_name,
            "block_id": self.block_id,
            "code_range": self.code_range,
            "browser_url": self.browser_url,
            "foundation_uri": self.foundation_uri,
            "parent_ids": self.parent_ids,
            "child_ids": self.child_ids,
            "index_terms": self.index_terms,
            "inclusions": self.inclusions,
            "exclusions": self.exclusions,
            "coding_note": self.coding_note,
        }
        out = {k: v for k, v in out.items() if v not in (None, [], "")}
        if include_raw:
            out["raw"] = self.raw
        return out


# --------------------------------------------------------------------------
# Reference parsing
# --------------------------------------------------------------------------

_ENTITY_ID_RE = re.compile(r"^\d+(?:/(?:other|unspecified))?$")
_CODE_RE = re.compile(r"^[0-9A-Z]{2}[0-9A-Z]{1,2}(?:\.[0-9A-Z]+)*$")


def parse_reference(
    ref: str,
    *,
    release: str | None = None,
    linearization: str | None = None,
    language: str | None = None,
) -> EntityRef | str:
    """Resolve a user-supplied reference.

    Accepts a browser URL, an ``id.who.int`` API/foundation URI, a bare numeric
    entity id, or an ICD-11 code. Returns an :class:`EntityRef`, or the code as
    a plain string when the reference is a code that must be looked up first.
    """
    ref = ref.strip()
    defaults = {
        "release": release or DEFAULT_RELEASE,
        "linearization": linearization or DEFAULT_LINEARIZATION,
        "language": language or DEFAULT_LANGUAGE,
    }

    if ref.startswith(("http://", "https://")):
        url = urlparse(ref)
        parts = [p for p in url.path.split("/") if p]
        found: dict[str, str] = {}
        # Browser: /browse/<release>/<linearization>/<lang>#<entity_id>
        if parts and parts[0] == "browse" and len(parts) >= 4:
            found = {
                "release": parts[1],
                "linearization": parts[2],
                "language": parts[3],
            }
        # API: /icd/release/11/<release>/<linearization>/<entity_id>
        elif "release" in parts:
            idx = parts.index("release")
            tail = parts[idx + 1 :]
            if len(tail) >= 3:
                found = {"release": tail[1], "linearization": tail[2]}
        # Explicit CLI options still win over anything parsed from the URL.
        explicit = {
            "release": release,
            "linearization": linearization,
            "language": language,
        }
        for key, value in found.items():
            defaults[key] = explicit[key] or value

        entity_id = url.fragment.strip() or (parts[-1] if parts else "")
        entity_id = entity_id.split("#")[0]
        if not _ENTITY_ID_RE.match(entity_id):
            raise IcdError(f"Could not find an entity id in URL: {ref}")
        return EntityRef(entity_id, **defaults)

    ref = ref.removeprefix("ICD11:").removeprefix("icd11:")
    if _ENTITY_ID_RE.match(ref):
        return EntityRef(ref, **defaults)
    if _CODE_RE.match(ref):
        return ref  # needs a code lookup
    raise IcdError(f"Unrecognized ICD-11 reference: {ref!r}")


# --------------------------------------------------------------------------
# API client
# --------------------------------------------------------------------------


def fetch_guest_token(client: httpx.Client) -> str:
    """Fetch and de-obfuscate the ICD browser's public guest token.

    Mirrors ``getNewTokenFunction`` in ``https://icd.who.int/browse/js/browser.js``:
    the response character at index 13 keys a shift applied to every other
    character, and index 13 itself is dropped.
    """
    response = client.get(
        GUEST_TOKEN_URL,
        headers={"Referer": f"{BROWSER_HOST}/browse/{DEFAULT_RELEASE}/mms/en"},
    )
    response.raise_for_status()
    try:
        obfuscated = response.json()["res"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise IcdError(f"Unexpected guest-token response from {GUEST_TOKEN_URL}") from exc
    if len(obfuscated) < 14:
        raise IcdError("Guest token too short to de-obfuscate")
    offset = (ord(obfuscated[13]) - 48) % 70 % 14
    return "".join(
        chr(ord(char) - offset) for index, char in enumerate(obfuscated) if index != 13
    )


class IcdClient:
    """Minimal client for the ICD-11 linearization API."""

    def __init__(self, token: str | None = None, language: str = DEFAULT_LANGUAGE):
        self._client = httpx.Client(
            timeout=TIMEOUT,
            follow_redirects=True,
            headers={"User-Agent": USER_AGENT},
        )
        self.language = language
        self.token = token or fetch_guest_token(self._client)

    def __enter__(self) -> "IcdClient":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "API-Version": "v2",
            "Accept-Language": self.language,
        }

    def get_json(self, url: str, params: dict[str, str] | None = None) -> dict[str, Any]:
        response = self._client.get(url, headers=self._headers(), params=params)
        if response.status_code == 401:
            raise IcdError(
                "ICD API rejected the bearer token (401). The guest token may have "
                "expired — rerun, or pass your own token with --token."
            )
        if response.status_code == 404:
            raise IcdError(f"ICD API has no entity at {url} (404)")
        response.raise_for_status()
        return response.json()

    def get_entity(self, ref: EntityRef) -> Entity:
        return parse_entity(self.get_json(ref.api_url))

    def lookup_code(self, code: str, ref: EntityRef) -> EntityRef:
        """Resolve an ICD-11 code (e.g. ``LA05.4``) to an entity reference."""
        data = self.get_json(
            f"{API_ROOT}/{ref.release}/{ref.linearization}/codeinfo/{code}"
        )
        target = data.get("stemId") or data.get("@id") or ""
        entity_id = target.rstrip("/").split("/")[-1]
        if not _ENTITY_ID_RE.match(entity_id):
            raise IcdError(f"Could not resolve code {code!r} to an entity id")
        return ref.sibling(entity_id)


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------


def _text(value: Any) -> str | None:
    """Flatten a language-tagged ICD value to plain text."""
    if value is None:
        return None
    if isinstance(value, str):
        return _strip_markup(value)
    if isinstance(value, dict):
        for key in ("@value", "value", "label"):
            if key in value:
                return _text(value[key])
    return None


def _texts(value: Any) -> list[str]:
    if not value:
        return []
    items = value if isinstance(value, list) else [value]
    out: list[str] = []
    for item in items:
        text = _text(item.get("label") if isinstance(item, dict) else item)
        if text:
            out.append(text)
    return out


def _strip_markup(text: str) -> str:
    """ICD titles embed ``<em class='found'>`` highlight spans; drop them."""
    return re.sub(r"<[^>]+>", "", text).strip()


def _ids(value: Any) -> list[str]:
    """Reduce entity URIs to ids, keeping ``/other`` and ``/unspecified`` residuals."""
    if not value:
        return []
    items = value if isinstance(value, list) else [value]
    out: list[str] = []
    for item in items:
        segments = str(item).rstrip("/").split("/")
        if len(segments) > 1 and segments[-1] in ("other", "unspecified"):
            out.append("/".join(segments[-2:]))
        else:
            out.append(segments[-1])
    return out


def parse_entity(data: dict[str, Any]) -> Entity:
    """Flatten one linearization-entity JSON document."""
    entity_id = str(data.get("@id", "")).rstrip("/").split("/")[-1]
    return Entity(
        entity_id=entity_id,
        code=data.get("code"),
        title=_text(data.get("title")),
        class_kind=data.get("classKind"),
        definition=_text(data.get("definition")),
        long_definition=_text(data.get("longDefinition")),
        fully_specified_name=_text(data.get("fullySpecifiedName")),
        browser_url=data.get("browserUrl"),
        foundation_uri=data.get("source"),
        parent_ids=_ids(data.get("parent")),
        child_ids=_ids(data.get("child")),
        index_terms=_texts(data.get("indexTerm")),
        inclusions=_texts(data.get("inclusion")),
        exclusions=_texts(data.get("exclusion")),
        coding_note=_text(data.get("codingNote")),
        block_id=data.get("blockId"),
        code_range=data.get("codeRange"),
        raw=data,
    )


def collect_ancestors(client: IcdClient, ref: EntityRef, entity: Entity) -> list[Entity]:
    """Walk parent links to the linearization root (root first)."""
    chain: list[Entity] = []
    seen = {entity.entity_id}
    current = entity
    while current.parent_ids:
        parent_id = current.parent_ids[0]
        # A chapter's parent is the linearization root itself (".../mms"),
        # which is where the climb stops.
        if not _ENTITY_ID_RE.match(parent_id) or parent_id in seen:
            break
        seen.add(parent_id)
        current = client.get_entity(ref.sibling(parent_id))
        chain.append(current)
    return list(reversed(chain))


def collect_descendants(
    client: IcdClient, ref: EntityRef, entity: Entity, depth: int
) -> list[tuple[int, Entity]]:
    """Depth-first walk of children, ``depth`` levels deep (document order)."""
    out: list[tuple[int, Entity]] = []
    stack = [(1, child_id) for child_id in reversed(entity.child_ids)]
    while stack:
        level, entity_id = stack.pop()
        if level > depth:
            continue
        child = client.get_entity(ref.sibling(entity_id))
        out.append((level, child))
        if level < depth:
            stack.extend((level + 1, gid) for gid in reversed(child.child_ids))
    return out


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def _label(entity: Entity) -> str:
    return " ".join(part for part in (entity.code or entity.block_id, entity.title) if part)


def render_text(
    entity: Entity,
    ref: EntityRef,
    ancestors: Iterable[Entity] = (),
    descendants: Iterable[tuple[int, Entity]] = (),
) -> str:
    lines = [_label(entity), "=" * len(_label(entity)), ""]
    lines.append(f"entity id     : {entity.entity_id}")
    if entity.class_kind:
        lines.append(f"class kind    : {entity.class_kind}")
    if entity.code:
        lines.append(f"code          : {entity.code}")
    if entity.code_range:
        lines.append(f"code range    : {entity.code_range}")
    lines.append(f"release       : {ref.release} / {ref.linearization} / {ref.language}")
    lines.append(f"browser       : {entity.browser_url or ref.browser_url}")
    if entity.foundation_uri:
        lines.append(f"foundation    : {entity.foundation_uri}")
    lines.append(f"api           : {ref.api_url}")

    if entity.definition:
        lines += ["", "Definition", "----------", entity.definition]
    if entity.long_definition:
        lines += ["", "Long definition", "---------------", entity.long_definition]
    for heading, values in (
        ("Index terms", entity.index_terms),
        ("Inclusions", entity.inclusions),
        ("Exclusions", entity.exclusions),
    ):
        if values:
            lines += ["", heading, "-" * len(heading)]
            lines += [f"- {value}" for value in values]
    if entity.coding_note:
        lines += ["", "Coding note", "-----------", entity.coding_note]

    ancestors = list(ancestors)
    if ancestors:
        lines += ["", "Ancestors", "---------"]
        for level, ancestor in enumerate(ancestors):
            lines.append(f"{'  ' * level}{_label(ancestor)}")
        lines.append(f"{'  ' * len(ancestors)}{_label(entity)}  <-- this entity")

    descendants = list(descendants)
    if descendants:
        lines += ["", "Descendants", "-----------"]
        for level, child in descendants:
            lines.append(f"{'  ' * (level - 1)}- {_label(child)}")

    return "\n".join(lines) + "\n"


def render_markdown(
    entity: Entity,
    ref: EntityRef,
    ancestors: Iterable[Entity] = (),
    descendants: Iterable[tuple[int, Entity]] = (),
) -> str:
    lines = [f"# {_label(entity)}", ""]
    lines += [
        "| Field | Value |",
        "| --- | --- |",
        f"| Entity id | `{entity.entity_id}` |",
        f"| Code | `{entity.code or '-'}` |",
        f"| Class kind | {entity.class_kind or '-'} |",
        f"| Release | {ref.release} / {ref.linearization} / {ref.language} |",
        f"| Browser | {entity.browser_url or ref.browser_url} |",
        f"| Foundation URI | {entity.foundation_uri or '-'} |",
        "",
    ]
    if entity.definition:
        lines += ["## Definition", "", entity.definition, ""]
    if entity.long_definition:
        lines += ["## Long definition", "", entity.long_definition, ""]
    for heading, values in (
        ("Index terms", entity.index_terms),
        ("Inclusions", entity.inclusions),
        ("Exclusions", entity.exclusions),
    ):
        if values:
            lines += [f"## {heading}", ""]
            lines += [f"- {value}" for value in values]
            lines.append("")
    if entity.coding_note:
        lines += ["## Coding note", "", entity.coding_note, ""]

    ancestors = list(ancestors)
    if ancestors:
        lines += ["## Ancestors", ""]
        for level, ancestor in enumerate(ancestors):
            lines.append(f"{'  ' * level}- {_label(ancestor)}")
        lines.append(f"{'  ' * len(ancestors)}- **{_label(entity)}**")
        lines.append("")

    descendants = list(descendants)
    if descendants:
        lines += ["## Descendants", ""]
        for level, child in descendants:
            lines.append(f"{'  ' * (level - 1)}- {_label(child)}")
        lines.append("")

    return "\n".join(lines)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "reference",
        help="Browser URL, id.who.int URI, numeric entity id, or ICD-11 code",
    )
    parser.add_argument("--release", help=f"Release (default: {DEFAULT_RELEASE})")
    parser.add_argument(
        "--linearization", help=f"Linearization (default: {DEFAULT_LINEARIZATION})"
    )
    parser.add_argument("--language", help=f"Language (default: {DEFAULT_LANGUAGE})")
    parser.add_argument(
        "--token",
        help="Bearer token for the ICD API (default: the browser's public guest token)",
    )
    parser.add_argument(
        "--ancestors", action="store_true", help="Also fetch the parent chain"
    )
    parser.add_argument(
        "--children", action="store_true", help="Also fetch direct children (depth 1)"
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=0,
        help="Fetch descendants this many levels deep (implies --children)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "markdown", "json", "raw"),
        default="text",
        help="Output format; 'raw' is the unmodified API JSON",
    )
    parser.add_argument("-o", "--output", help="Write to this file instead of stdout")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    depth = max(args.depth, 1 if args.children else 0)

    try:
        parsed = parse_reference(
            args.reference,
            release=args.release,
            linearization=args.linearization,
            language=args.language,
        )
        with IcdClient(token=args.token, language=args.language or DEFAULT_LANGUAGE) as client:
            if isinstance(parsed, str):  # an ICD-11 code needing lookup
                ref = client.lookup_code(
                    parsed,
                    EntityRef(
                        "0",
                        args.release or DEFAULT_RELEASE,
                        args.linearization or DEFAULT_LINEARIZATION,
                        args.language or DEFAULT_LANGUAGE,
                    ),
                )
            else:
                ref = parsed
            entity = client.get_entity(ref)
            ancestors = collect_ancestors(client, ref, entity) if args.ancestors else []
            descendants = (
                collect_descendants(client, ref, entity, depth) if depth else []
            )
    except (IcdError, httpx.HTTPError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.format == "raw":
        payload: Any = entity.raw
        if ancestors or descendants:
            payload = {
                "entity": entity.raw,
                "ancestors": [item.raw for item in ancestors],
                "descendants": [item.raw for _, item in descendants],
            }
        rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    elif args.format == "json":
        rendered = json.dumps(
            {
                "reference": {
                    "release": ref.release,
                    "linearization": ref.linearization,
                    "language": ref.language,
                    "api_url": ref.api_url,
                    "browser_url": ref.browser_url,
                },
                "entity": entity.to_dict(),
                "ancestors": [item.to_dict() for item in ancestors],
                "descendants": [
                    {"depth": level, **item.to_dict()} for level, item in descendants
                ],
            },
            indent=2,
            ensure_ascii=False,
        )
    elif args.format == "markdown":
        rendered = render_markdown(entity, ref, ancestors, descendants)
    else:
        rendered = render_text(entity, ref, ancestors, descendants)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered if rendered.endswith("\n") else rendered + "\n")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
