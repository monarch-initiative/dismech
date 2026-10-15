"""Phenotype-system spread across the knowledge base.

The browser's "Phenotype Systems" facet tags every disease with each HPO
top-level branch (Nervous System, Musculoskeletal, ...) that any of its
phenotypes falls under. That facet answers "does this disease touch system X?"
but not "how many systems does a disease span, and how strongly?", nor
"which systems tend to occur together?". This module computes both and renders
them as a QC-dashboard page (``dashboard/phenotype_systems.html``) with a
machine-readable twin (``dashboard/phenotype_systems.json``).

Two sources of multiplicity are kept apart:

* a disease has phenotypes in several systems (a genuinely multisystem
  disease), measured per disease by the number of systems present and by the
  *effective* number of systems (:func:`effective_system_count`), which
  discounts systems that hold only a stray finding; and
* a single HP term sits under more than one top-level branch (HP is a DAG), so
  one phenotype can place a disease in two systems. Those phenotypes are
  counted once per system, exactly as the facet does, and reported separately
  as ``multi_system_phenotype_count``.

The HP-term-to-system map is the cache written by the browser export
(``app/hpo_category_cache.json``); this module never queries the ontology.
"""

from __future__ import annotations

import argparse
import html
import json
import math
from collections import Counter
from collections.abc import Iterable, Iterator, Mapping, Sequence
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from itertools import combinations
from pathlib import Path
from typing import Any

from dismech import kb_cache
from dismech.export.browser_export import (
    HPO_CATEGORY_CACHE_PATH,
    HPO_TOP_LEVEL_CATEGORIES,
)
from dismech.export.utils import slugify
from dismech.qc_dashboard import inject_block

SYSTEMS: tuple[str, ...] = tuple(sorted(HPO_TOP_LEVEL_CATEGORIES.values()))
DEFAULT_HPO_CATEGORY_CACHE = HPO_CATEGORY_CACHE_PATH
PHENOTYPE_SYSTEMS_BLOCK_START = "<!-- PHENOTYPE_SYSTEMS_START -->"
PHENOTYPE_SYSTEMS_BLOCK_END = "<!-- PHENOTYPE_SYSTEMS_END -->"
TOP_COMBINATIONS = 30
TOP_PAIRS = 12
MIN_PAIR_COUNT_FOR_LIFT_RANKING = 25


# --------------------------------------------------------------------------- measures


def effective_system_count(system_counts: Mapping[str, int]) -> float:
    """Effective number of systems: ``exp`` of the Shannon entropy of phenotypes per system.

    A disease whose phenotypes all sit in one system scores 1.0; one spread
    evenly over *k* systems scores *k*; one with a dominant system and a few
    stray findings scores a little above 1.

    >>> effective_system_count({"Nervous System": 10})
    1.0
    >>> round(effective_system_count({"Eye": 5, "Ear": 5}), 3)
    2.0
    >>> round(effective_system_count({"Eye": 9, "Ear": 1}), 3)
    1.384
    >>> effective_system_count({})
    0.0
    """
    total = sum(system_counts.values())
    if total == 0:
        return 0.0
    entropy = -sum(
        (count / total) * math.log(count / total)
        for count in system_counts.values()
        if count
    )
    return math.exp(entropy)


@dataclass
class SystemProfile:
    """How one disease's phenotypes distribute over the HPO top-level systems."""

    name: str
    slug: str
    phenotype_count: int
    """Phenotypes carrying an HP term."""
    unbound_count: int
    """Phenotypes with no HP term; they cannot be placed in a system."""
    uncategorized_count: int
    """HP-bound phenotypes whose term maps to no system (missing from the cache, or outside Phenotypic abnormality)."""
    multi_system_phenotype_count: int
    """Phenotypes whose HP term sits under more than one top-level branch."""
    system_counts: dict[str, int]
    """Phenotypes per system, non-zero systems only, in canonical order."""

    @property
    def system_count(self) -> int:
        return len(self.system_counts)

    @property
    def effective_system_count(self) -> float:
        return effective_system_count(self.system_counts)

    @property
    def dominant_system(self) -> str | None:
        if not self.system_counts:
            return None
        return max(self.system_counts, key=lambda s: (self.system_counts[s], -SYSTEMS.index(s)))

    @property
    def dominant_share(self) -> float | None:
        """Fraction of system memberships held by the dominant system."""
        dominant = self.dominant_system
        if dominant is None:
            return None
        return self.system_counts[dominant] / sum(self.system_counts.values())

    def to_record(self) -> dict[str, Any]:
        record = asdict(self)
        record["system_count"] = self.system_count
        record["effective_system_count"] = round(self.effective_system_count, 3)
        record["dominant_system"] = self.dominant_system
        share = self.dominant_share
        record["dominant_share"] = None if share is None else round(share, 3)
        return record


def profile_disorder(
    disorder: Mapping[str, Any], categories: Mapping[str, list[str]]
) -> SystemProfile:
    """Distribute one disorder's phenotypes over the systems named by ``categories``.

    ``categories`` maps an HP CURIE to the top-level systems it falls under, as
    in ``app/hpo_category_cache.json``. A term under two branches counts once
    in each, matching the browser facet.

    >>> cats = {"HP:1": ["Eye"], "HP:2": ["Eye"], "HP:3": ["Ear", "Eye"], "HP:4": []}
    >>> disorder = {"name": "Demo", "phenotypes": [
    ...     {"phenotype_term": {"term": {"id": "HP:1"}}},
    ...     {"phenotype_term": {"term": {"id": "HP:2"}}},
    ...     {"phenotype_term": {"term": {"id": "HP:3"}}},
    ...     {"phenotype_term": {"term": {"id": "HP:4"}}},
    ...     {"phenotype_term": {"term": {"id": "HP:999"}}},
    ...     {"name": "no term"},
    ... ]}
    >>> p = profile_disorder(disorder, cats)
    >>> p.system_counts
    {'Ear': 1, 'Eye': 3}
    >>> (p.phenotype_count, p.unbound_count, p.uncategorized_count, p.multi_system_phenotype_count)
    (5, 1, 2, 1)
    >>> p.dominant_system, round(p.dominant_share, 2), round(p.effective_system_count, 2)
    ('Eye', 0.75, 1.75)
    """
    counts: Counter[str] = Counter()
    phenotype_count = unbound = uncategorized = multi = 0
    for phenotype in disorder.get("phenotypes") or []:
        term = ((phenotype.get("phenotype_term") or {}).get("term") or {})
        hp_id = term.get("id")
        if not hp_id:
            unbound += 1
            continue
        phenotype_count += 1
        systems = categories.get(hp_id) or []
        if not systems:
            uncategorized += 1
            continue
        if len(systems) > 1:
            multi += 1
        counts.update(systems)
    name = disorder.get("name", "Unknown")
    return SystemProfile(
        name=name,
        slug=slugify(name),
        phenotype_count=phenotype_count,
        unbound_count=unbound,
        uncategorized_count=uncategorized,
        multi_system_phenotype_count=multi,
        system_counts={s: counts[s] for s in SYSTEMS if counts[s]},
    )


# --------------------------------------------------------------------------- corpus


def load_hpo_category_cache(path: Path = DEFAULT_HPO_CATEGORY_CACHE) -> dict[str, list[str]]:
    """Load the HP-term-to-system map written by ``just gen-browser-data``."""
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found; run `just gen-browser-data` first, which writes it."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def _median(values: Sequence[float]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2


def collect_phenotype_systems(
    disorders: Iterable[Mapping[str, Any]],
    categories: Mapping[str, list[str]],
) -> dict[str, Any]:
    """Per-disease profiles plus the corpus-level structure they add up to.

    Returns a JSON-serialisable dict with ``summary``, ``systems`` (membership
    totals), ``distribution`` (systems-per-disease histograms), ``pairs``
    (co-occurrence with lift and Jaccard), ``combinations`` (how shared each
    exact set of systems is) and ``diseases`` (one profile per entry).

    >>> cats = {"HP:1": ["Eye"], "HP:2": ["Ear"], "HP:3": ["Eye", "Ear"]}
    >>> def dz(name, *ids):
    ...     return {"name": name, "phenotypes": [{"phenotype_term": {"term": {"id": i}}} for i in ids]}
    >>> data = collect_phenotype_systems(
    ...     [dz("A", "HP:1"), dz("B", "HP:1", "HP:2"), dz("C", "HP:3"), dz("D", "HP:1")], cats)
    >>> data["summary"]["total_diseases"], data["summary"]["median_system_count"]
    (4, 1.5)
    >>> [(s["system"], s["diseases"]) for s in data["systems"]]
    [('Eye', 4), ('Ear', 2)]
    >>> data["pairs"][0]["count"], data["pairs"][0]["lift"], data["pairs"][0]["jaccard"]
    (2, 1.0, 0.5)
    >>> data["combinations"]["unique_diseases"], data["combinations"]["distinct"]
    (0, 2)
    """
    profiles = [profile_disorder(d, categories) for d in disorders]
    total = len(profiles)

    membership: Counter[str] = Counter()
    combos: Counter[frozenset[str]] = Counter()
    pair_counts: Counter[tuple[str, str]] = Counter()
    for profile in profiles:
        present = tuple(profile.system_counts)
        membership.update(present)
        if present:
            combos[frozenset(present)] += 1
        for a, b in combinations(present, 2):
            pair_counts[(a, b)] += 1

    system_order = sorted(SYSTEMS, key=lambda s: (-membership[s], s))
    systems = [{"system": s, "diseases": membership[s]} for s in system_order if membership[s]]

    pairs: list[dict[str, Any]] = []
    for (a, b), count in pair_counts.items():
        expected = membership[a] * membership[b] / total if total else 0
        union = membership[a] + membership[b] - count
        pairs.append(
            {
                "a": a,
                "b": b,
                "count": count,
                "lift": round(count / expected, 3) if expected else None,
                "jaccard": round(count / union, 3) if union else None,
            }
        )
    pairs.sort(key=lambda p: (-p["count"], p["a"], p["b"]))

    system_count_hist = Counter(p.system_count for p in profiles)
    effective_hist = Counter(int(p.effective_system_count) for p in profiles)
    max_bin = max([*system_count_hist, *effective_hist], default=0)

    sharing = Counter(combos.values())
    def _combo_rank(item: tuple[frozenset[str], int]) -> tuple[int, list[str]]:
        systems, diseases = item
        return (-diseases, sorted(systems))

    top_combinations = [
        {"systems": sorted(c, key=system_order.index), "diseases": n}
        for c, n in sorted(combos.items(), key=_combo_rank)[:TOP_COMBINATIONS]
    ]

    system_counts = [p.system_count for p in profiles]
    effective_counts = [p.effective_system_count for p in profiles]
    median_effective = _median(effective_counts)
    summary = {
        "total_diseases": total,
        "total_systems": len(systems),
        "total_memberships": sum(membership.values()),
        "mean_system_count": round(sum(system_counts) / total, 2) if total else None,
        "median_system_count": _median(system_counts),
        "mean_effective_system_count": round(sum(effective_counts) / total, 2) if total else None,
        "median_effective_system_count": (
            None if median_effective is None else round(median_effective, 2)
        ),
        "distinct_combinations": len(combos),
        "unique_combination_diseases": sharing[1],
        "unique_combination_percent": round(100 * sharing[1] / total, 1) if total else None,
        "total_phenotypes": sum(p.phenotype_count for p in profiles),
        "unbound_phenotypes": sum(p.unbound_count for p in profiles),
        "uncategorized_phenotypes": sum(p.uncategorized_count for p in profiles),
        "multi_system_phenotypes": sum(p.multi_system_phenotype_count for p in profiles),
    }
    return {
        "summary": summary,
        "systems": systems,
        "distribution": {
            "max_bin": max_bin,
            "system_count": {str(k): system_count_hist[k] for k in range(max_bin + 1)},
            "effective_system_count": {str(k): effective_hist[k] for k in range(max_bin + 1)},
        },
        "pairs": pairs,
        "combinations": {
            "distinct": len(combos),
            "unique_diseases": sharing[1],
            "shared_2_to_4_diseases": sum(k * v for k, v in sharing.items() if 2 <= k <= 4),
            "shared_5_plus_diseases": sum(k * v for k, v in sharing.items() if k >= 5),
            "no_system_diseases": total - sum(combos.values()),
            "top": top_combinations,
        },
        "diseases": sorted(
            (p.to_record() for p in profiles),
            key=lambda r: (-r["effective_system_count"], r["name"]),
        ),
    }


def iter_disorders(kb_dir: Path) -> Iterator[dict[str, Any]]:
    """Yield every disorder document under ``kb_dir`` (history files excluded), one at a time.

    Streams rather than materialising the corpus: :func:`collect_phenotype_systems`
    keeps only a small profile per disease, so peak memory is one parsed
    document instead of all of them. Routed through :mod:`dismech.kb_cache`
    (issue #11003) so a process that walks the corpus more than once parses
    each file once; the single-walk CLI turns that cache off in ``main``.
    """
    for _path, document in kb_cache.iter_documents(kb_dir):
        yield document


# --------------------------------------------------------------------------- rendering

_BLUE = "#2a78d6"
_BLUE_LIGHT = "#9ec5f4"
_BLUE_DARK = "#104281"
_RED = "#e34948"
_NEUTRAL = "#f0efec"
_ABSENT = "#e5e5e7"
_INK = "#2c3e50"
_INK_LIGHT = "#6b7280"
_FONT = 'font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"'


def _esc(value: Any) -> str:
    return html.escape(str(value))


def _fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, str):
        return html.escape(value)
    if isinstance(value, float):
        return f"{value:,.1f}" if value != int(value) else f"{int(value):,}"
    return f"{value:,}"


def _hex_to_rgb(color: str) -> tuple[int, int, int]:
    return tuple(int(color[i : i + 2], 16) for i in (1, 3, 5))  # type: ignore[return-value]


def _diverging(t: float) -> str:
    """-1 → blue, 0 → neutral gray, +1 → red."""
    if t < 0:
        start, end, u = _hex_to_rgb(_BLUE), _hex_to_rgb(_NEUTRAL), 1 + t
    else:
        start, end, u = _hex_to_rgb(_NEUTRAL), _hex_to_rgb(_RED), t
    return "#" + "".join(f"{round(start[i] + (end[i] - start[i]) * u):02x}" for i in range(3))


def _svg(width: float, height: float, body: list[str]) -> str:
    return (
        f'<svg width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}" '
        f'{_FONT} role="img">\n' + "\n".join(body) + "\n</svg>"
    )


def _histogram_svg(hist: Mapping[str, int], max_bin: int, title: str, marker: float | None, marker_label: str) -> str:
    left, colw, barh, top = 30, 24, 110, 26
    width = left + colw * (max_bin + 1) + 10
    height = top + barh + 44  # axis labels, then the median pointer, then the caption
    max_value = max(hist.values(), default=1) or 1
    marker_text = (
        f' <tspan font-weight="400" fill="{_RED}">· {_esc(marker_label)}</tspan>' if marker is not None else ""
    )
    body = [f'<text x="0" y="12" font-size="12" font-weight="600" fill="{_INK}">{_esc(title)}{marker_text}</text>']
    for k in range(max_bin + 1):
        value = hist.get(str(k), 0)
        x = left + k * colw + 3
        h = value / max_value * barh
        y = top + barh - h
        body.append(
            f'<rect x="{x}" y="{y:.1f}" width="{colw - 6}" height="{h:.1f}" rx="2" fill="{_BLUE}">'
            f"<title>{k}: {_fmt(value)} diseases</title></rect>"
        )
        if value:
            body.append(f'<text x="{x + (colw - 6) / 2}" y="{y - 3:.1f}" font-size="8" text-anchor="middle" fill="{_INK_LIGHT}">{value}</text>')
        body.append(f'<text x="{x + (colw - 6) / 2}" y="{top + barh + 12}" font-size="9" text-anchor="middle" fill="{_INK}">{k}</text>')
    if marker is not None:
        # a small pointer under the axis label of the bin the marker falls in;
        # a full-height line would run through the value labels above the bars
        mx = left + marker * colw + colw / 2
        ty = top + barh + 16
        body.append(f'<polygon points="{mx - 4:.1f},{ty + 6} {mx + 4:.1f},{ty + 6} {mx:.1f},{ty}" fill="{_RED}"><title>{_esc(marker_label)}</title></polygon>')
    body.append(f'<text x="{left}" y="{height - 6}" font-size="9" fill="{_INK_LIGHT}">systems per disease (bin = whole number, effective count floored)</text>')
    return _svg(width, height, body)


def _matrix_svg(system_order: list[str], pairs: list[dict[str, Any]]) -> str:
    n = len(system_order)
    cell, left, top = 20, 110, 104
    width = left + cell * n + 80  # room for the last rotated column label
    height = top + cell * n + 40
    lookup = {(p["a"], p["b"]): p for p in pairs}
    lookup.update({(p["b"], p["a"]): p for p in pairs})
    lifts = [p["lift"] for p in pairs if p["lift"]]
    clamp = min(1.5, max((abs(math.log2(v)) for v in lifts), default=1.0)) or 1.0
    body = []
    for i, s in enumerate(system_order):
        x = left + i * cell + cell / 2
        body.append(f'<text transform="translate({x + 3},{top - 6}) rotate(-60)" font-size="8.5" fill="{_INK}">{_esc(s)}</text>')
        body.append(f'<text x="{left - 6}" y="{top + i * cell + cell / 2 + 3}" font-size="8.5" text-anchor="end" fill="{_INK}">{_esc(s)}</text>')
    for i, a in enumerate(system_order):
        for j, b in enumerate(system_order):
            x, y = left + j * cell, top + i * cell
            if a == b:
                body.append(f'<rect x="{x + 1}" y="{y + 1}" width="{cell - 2}" height="{cell - 2}" rx="2" fill="{_ABSENT}"/>')
                continue
            pair = lookup.get((a, b))
            if pair is None or not pair["lift"]:
                body.append(f'<rect x="{x + 1}" y="{y + 1}" width="{cell - 2}" height="{cell - 2}" rx="2" fill="none" stroke="{_ABSENT}"><title>{_esc(a)} + {_esc(b)}: never co-occur</title></rect>')
                continue
            t = max(-1.0, min(1.0, math.log2(pair["lift"]) / clamp))
            body.append(
                f'<rect x="{x + 1}" y="{y + 1}" width="{cell - 2}" height="{cell - 2}" rx="2" fill="{_diverging(t)}">'
                f'<title>{_esc(a)} + {_esc(b)}: {_fmt(pair["count"])} diseases, lift {pair["lift"]:.2f}, Jaccard {pair["jaccard"]:.2f}</title></rect>'
            )
    # legend: gradient bar
    lx, ly, lw = left, top + cell * n + 12, 300
    steps = 30
    for k in range(steps):
        t = -1 + 2 * k / (steps - 1)
        body.append(f'<rect x="{lx + k * lw / steps:.1f}" y="{ly}" width="{lw / steps + 0.5:.1f}" height="10" fill="{_diverging(t)}"/>')
    body.append(f'<text x="{lx}" y="{ly + 22}" font-size="9" fill="{_INK_LIGHT}">lift ≤ {2 ** -clamp:.2f}</text>')
    body.append(f'<text x="{lx + lw / 2}" y="{ly + 22}" font-size="9" text-anchor="middle" fill="{_INK_LIGHT}">1</text>')
    body.append(f'<text x="{lx + lw}" y="{ly + 22}" font-size="9" text-anchor="end" fill="{_INK_LIGHT}">≥ {2 ** clamp:.2f}</text>')
    body.append(f'<rect x="{lx + lw + 24}" y="{ly}" width="10" height="10" rx="2" fill="none" stroke="{_ABSENT}"/>')
    body.append(f'<text x="{lx + lw + 38}" y="{ly + 9}" font-size="9" fill="{_INK_LIGHT}">never co-occur</text>')
    body.append(f'<text x="{lx + lw + 24}" y="{ly + 22}" font-size="9" fill="{_INK_LIGHT}">blue: less than chance · red: more</text>')
    return _svg(width, height, body)


def _sharing_bar_svg(combos: Mapping[str, Any], total: int) -> str:
    width, barh = 720, 20
    segments = [
        ("combination unique to one disease", combos["unique_diseases"], _BLUE_DARK, "#ffffff"),
        ("shared by 2–4 diseases", combos["shared_2_to_4_diseases"], _BLUE, "#ffffff"),
        ("shared by 5+ diseases (the part an UpSet plot can show)", combos["shared_5_plus_diseases"], _BLUE_LIGHT, "#0b0b0b"),
    ]
    body = []
    x = 0.0
    for label, n, fill, ink in segments:
        w = n / total * (width - 4) if total else 0
        body.append(f'<rect x="{x:.1f}" y="2" width="{w:.1f}" height="{barh}" rx="3" fill="{fill}"><title>{_esc(label)}: {_fmt(n)}</title></rect>')
        if w > 40:
            body.append(f'<text x="{x + w / 2:.1f}" y="{2 + barh / 2 + 3}" font-size="9" text-anchor="middle" fill="{ink}">{_fmt(n)} ({100 * n / total:.0f}%)</text>')
        x += w + 2
    x = 0.0
    for label, _n, fill, _ink in segments:
        body.append(f'<rect x="{x:.1f}" y="32" width="10" height="10" rx="2" fill="{fill}"/>')
        body.append(f'<text x="{x + 14:.1f}" y="41" font-size="9" fill="{_INK}">{_esc(label)}</text>')
        x += 14 + len(label) * 5.1 + 18
    return _svg(width, 48, body)


def _upset_svg(system_order: list[str], membership: Mapping[str, int], top: list[dict[str, Any]]) -> str:
    k = len(top)
    left, colw, rowh, barh, pad = 128, 20, 15, 80, 10
    width = left + colw * k + 10
    height = pad + barh + 22 + rowh * len(system_order) + 6
    max_n = max((c["diseases"] for c in top), default=1)
    body = []
    for c, combo in enumerate(top):
        x = left + c * colw + 3
        h = combo["diseases"] / max_n * barh
        y = pad + barh - h
        body.append(
            f'<rect x="{x}" y="{y:.1f}" width="{colw - 6}" height="{h:.1f}" rx="2" fill="{_BLUE}">'
            f'<title>{_esc(", ".join(combo["systems"]))}: {_fmt(combo["diseases"])} diseases</title></rect>'
        )
        body.append(f'<text x="{x + (colw - 6) / 2}" y="{y - 3:.1f}" font-size="8" text-anchor="middle" fill="{_INK}">{combo["diseases"]}</text>')
    y0 = pad + barh + 22
    for r, s in enumerate(system_order):
        cy = y0 + r * rowh + rowh / 2
        if r % 2 == 0:
            body.append(f'<rect x="{left}" y="{cy - rowh / 2}" width="{colw * k}" height="{rowh}" fill="{_INK}" opacity="0.04"/>')
        body.append(f'<text x="{left - 8}" y="{cy + 3}" font-size="9" text-anchor="end" fill="{_INK}">{_esc(s)}</text>')
        body.append(f'<text x="4" y="{cy + 3}" font-size="8" fill="{_INK_LIGHT}">{_fmt(membership.get(s, 0))}</text>')
    for c, combo in enumerate(top):
        cx = left + c * colw + colw / 2
        members = [r for r, s in enumerate(system_order) if s in combo["systems"]]
        if len(members) > 1:
            y1 = y0 + members[0] * rowh + rowh / 2
            y2 = y0 + members[-1] * rowh + rowh / 2
            body.append(f'<line x1="{cx}" y1="{y1}" x2="{cx}" y2="{y2}" stroke="{_BLUE}" stroke-width="1.5"/>')
        for r in range(len(system_order)):
            cy = y0 + r * rowh + rowh / 2
            fill = _BLUE if r in members else _ABSENT
            body.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{fill}"/>')
    return _svg(width, height, body)


def _pair_rows(pairs: list[dict[str, Any]]) -> str:
    return "\n".join(
        f"<tr><td>{_esc(p['a'])}</td><td>{_esc(p['b'])}</td><td>{_fmt(p['count'])}</td>"
        f"<td>{p['lift']:.2f}</td><td>{p['jaccard']:.2f}</td></tr>"
        for p in pairs
    )


def _disease_rows(diseases: list[dict[str, Any]]) -> str:
    rows = []
    for d in diseases:
        share = d["dominant_share"]
        dominant = (
            f"{_esc(d['dominant_system'])} ({100 * share:.0f}%)" if d["dominant_system"] else "—"
        )
        rows.append(
            f'<tr><td><a href="../pages/disorders/{_esc(d["slug"])}.html">{_esc(d["name"])}</a></td>'
            f'<td data-value="{d["phenotype_count"]}">{_fmt(d["phenotype_count"])}</td>'
            f'<td data-value="{d["system_count"]}">{_fmt(d["system_count"])}</td>'
            f'<td data-value="{d["effective_system_count"]}">{d["effective_system_count"]:.1f}</td>'
            f'<td data-value="{share if share is not None else -1}">{dominant}</td>'
            f'<td data-value="{d["multi_system_phenotype_count"]}">{_fmt(d["multi_system_phenotype_count"])}</td></tr>'
        )
    return "\n".join(rows)


def render_phenotype_systems_page(data: Mapping[str, Any], generated_at: str) -> str:
    """Render the dashboard page from :func:`collect_phenotype_systems` output."""
    summary = data["summary"]
    dist = data["distribution"]
    combos = data["combinations"]
    system_order = [s["system"] for s in data["systems"]]
    membership = {s["system"]: s["diseases"] for s in data["systems"]}
    total = summary["total_diseases"]

    cards = [
        ("Diseases", summary["total_diseases"], "Disorder entries analysed"),
        ("Systems", summary["total_systems"], "HPO top-level branches with at least one disease"),
        ("Median systems per disease", summary["median_system_count"], "Presence count, as the browser facet sees it"),
        ("Median effective systems", summary["median_effective_system_count"], "Weighted by phenotypes per system"),
        ("Unique combinations", f"{_fmt(summary['unique_combination_percent'])}%", "Diseases whose exact set of systems no other disease shares"),
        ("Multi-system phenotypes", summary["multi_system_phenotypes"], "Phenotypes whose HP term sits under two or more branches"),
    ]
    cards_html = "\n".join(
        f'<div class="card"><h3>{_esc(title)}</h3><div class="value">{_fmt(value)}</div><p>{_esc(detail)}</p></div>'
        for title, value, detail in cards
    )
    by_lift = sorted(
        (p for p in data["pairs"] if p["count"] >= MIN_PAIR_COUNT_FOR_LIFT_RANKING and p["lift"]),
        key=lambda p: -p["lift"],
    )[:TOP_PAIRS]
    by_count = data["pairs"][:TOP_PAIRS]
    system_rows = "\n".join(
        f"<tr><td>{_esc(s['system'])}</td><td>{_fmt(s['diseases'])}</td><td>{100 * s['diseases'] / total:.0f}%</td></tr>"
        for s in data["systems"]
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QC Dashboard - Phenotype Systems</title>
    <style>
        :root {{
            --bg: #f5f6fa;
            --card-bg: #ffffff;
            --text: {_INK};
            --text-light: {_INK_LIGHT};
            --border: #dcdde1;
            --accent: #2980b9;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 2rem;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        header {{ margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 2px solid var(--border); }}
        h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
        h2 {{ font-size: 1.2rem; margin-bottom: 0.8rem; }}
        h3 {{ font-size: 1rem; margin: 1rem 0 0.6rem; }}
        .subtitle, .meta, .card p, .note {{ color: var(--text-light); }}
        .meta {{ margin-top: 0.4rem; font-size: 0.9rem; }}
        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}
        .card, .panel {{
            background: var(--card-bg);
            border-radius: 8px;
            padding: 1.2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .card h3 {{ font-size: 0.82rem; color: var(--text-light); text-transform: uppercase; margin: 0 0 0.4rem; }}
        .card .value {{ font-size: 1.8rem; font-weight: 700; color: var(--accent); }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1rem; }}
        .wide {{ grid-column: 1 / -1; }}
        .note {{ margin-bottom: 1rem; }}
        .scroll {{ overflow-x: auto; }}
        .side-by-side {{ display: flex; flex-wrap: wrap; gap: 2rem; align-items: flex-start; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; }}
        th, td {{ padding: 0.5rem 0.65rem; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }}
        th {{ background: var(--bg); font-weight: 600; }}
        th.sortable {{ cursor: pointer; user-select: none; }}
        th.sortable::after {{ content: " ↕"; color: var(--text-light); font-size: 0.8em; }}
        th.sorted-desc::after {{ content: " ↓"; }}
        th.sorted-asc::after {{ content: " ↑"; }}
        a {{ color: var(--accent); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .breadcrumb {{ margin-bottom: 1rem; font-size: 0.92rem; }}
        .filter {{ margin-bottom: 0.8rem; padding: 0.45rem 0.6rem; border: 1px solid var(--border); border-radius: 6px; width: min(100%, 360px); font-size: 0.92rem; }}
        dl.method {{ display: grid; grid-template-columns: max-content 1fr; gap: 0.3rem 1rem; }}
        dl.method dt {{ font-weight: 600; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="breadcrumb"><a href="index.html">Back to QC Dashboard</a></div>
        <header>
            <h1>Phenotype Systems</h1>
            <p class="subtitle">
                How many HPO top-level systems each disease spans, how strongly, and which systems occur together.
                The browser's "Phenotype Systems" facet records presence only; this page adds the weight behind it.
            </p>
            <p class="meta">Generated: {_esc(generated_at)}</p>
        </header>

        <section class="summary-cards">
            {cards_html}
        </section>

        <section class="grid">
            <div class="panel wide">
                <h2>Systems per disease</h2>
                <p class="note">
                    Left: the number of systems a disease appears in, counting a system as present if any phenotype falls under it (the facet's view).
                    Right: the effective number of systems, exp of the Shannon entropy of phenotypes per system, which discounts a system that holds one stray finding.
                    The gap between the two is how much the presence count overstates spread.
                </p>
                <div class="side-by-side scroll">
                    {_histogram_svg(dist["system_count"], dist["max_bin"], "Systems present", summary["median_system_count"], f"median {_fmt(summary['median_system_count'])}")}
                    {_histogram_svg(dist["effective_system_count"], dist["max_bin"], "Effective systems", summary["median_effective_system_count"], f"median {_fmt(summary['median_effective_system_count'])}")}
                </div>
            </div>

            <div class="panel wide">
                <h2>Which systems travel together</h2>
                <p class="note">
                    Every pair of systems, coloured by lift: the number of diseases in both, divided by the number expected if the two were independent.
                    Red pairs co-occur more than chance, blue less; hover a cell for the count, lift and Jaccard index. Rows and columns are ordered by how many diseases each system has.
                </p>
                <div class="side-by-side">
                    <div class="scroll">{_matrix_svg(system_order, data["pairs"])}</div>
                    <div>
                        <h3>Strongest co-occurrence (lift, pairs with ≥ {MIN_PAIR_COUNT_FOR_LIFT_RANKING} diseases)</h3>
                        <table>
                            <thead><tr><th>System</th><th>System</th><th>Diseases</th><th>Lift</th><th>Jaccard</th></tr></thead>
                            <tbody>{_pair_rows(by_lift)}</tbody>
                        </table>
                        <h3>Most frequent pairs</h3>
                        <table>
                            <thead><tr><th>System</th><th>System</th><th>Diseases</th><th>Lift</th><th>Jaccard</th></tr></thead>
                            <tbody>{_pair_rows(by_count)}</tbody>
                        </table>
                    </div>
                </div>
            </div>

            <div class="panel wide">
                <h2>Exact combinations of systems</h2>
                <p class="note">
                    An UpSet plot shows how often each exact set of systems recurs. Here {_fmt(combos["distinct"])} distinct combinations occur across {_fmt(total)} diseases,
                    and {_fmt(combos["unique_diseases"])} diseases ({_fmt(summary["unique_combination_percent"])}%) have a combination shared by no other disease,
                    so the plot below covers only the {TOP_COMBINATIONS} most frequent combinations. The bar shows where the rest sit.
                </p>
                <div class="scroll">{_sharing_bar_svg(combos, total)}</div>
                <div class="scroll">{_upset_svg(system_order, membership, combos["top"])}</div>
            </div>

            <div class="panel">
                <h2>Diseases per system</h2>
                <table>
                    <thead><tr><th>System</th><th>Diseases</th><th>Share</th></tr></thead>
                    <tbody>{system_rows}</tbody>
                </table>
            </div>

            <div class="panel">
                <h2>Method</h2>
                <dl class="method">
                    <dt>System</dt><dd>One of the {len(SYSTEMS)} direct children of HP:0000118 (Phenotypic abnormality). A phenotype belongs to every system its HP term descends from, so an HP term under two branches counts once in each, exactly as the browser facet does.</dd>
                    <dt>Systems present</dt><dd>Number of systems with at least one phenotype.</dd>
                    <dt>Effective systems</dt><dd>exp(−Σ pᵢ ln pᵢ), where pᵢ is the share of the disease's system memberships held by system i. Equals the presence count when phenotypes are spread evenly, and approaches 1 when one system dominates.</dd>
                    <dt>Lift</dt><dd>Diseases in both systems ÷ (diseases in A × diseases in B ÷ all diseases).</dd>
                    <dt>Not counted</dt><dd>{_fmt(summary["unbound_phenotypes"])} phenotypes without an HP term and {_fmt(summary["uncategorized_phenotypes"])} whose term maps to no system (outside Phenotypic abnormality, or missing from the browser's category cache).</dd>
                </dl>
            </div>

            <div class="panel wide">
                <h2>All diseases</h2>
                <p class="note">Click a column header to sort. Dominant system shows the share of the disease's system memberships it holds.</p>
                <input class="filter" id="diseaseFilter" type="search" placeholder="Filter by disease name…" aria-label="Filter diseases">
                <div class="scroll">
                <table id="diseaseTable">
                    <thead><tr>
                        <th class="sortable" data-type="text">Disease</th>
                        <th class="sortable" data-type="number">Phenotypes</th>
                        <th class="sortable" data-type="number">Systems present</th>
                        <th class="sortable sorted-desc" data-type="number">Effective systems</th>
                        <th class="sortable" data-type="number">Dominant system</th>
                        <th class="sortable" data-type="number">Multi-system phenotypes</th>
                    </tr></thead>
                    <tbody>{_disease_rows(data["diseases"])}</tbody>
                </table>
                </div>
            </div>
        </section>
    </div>
    <script>
    (function () {{
        const table = document.getElementById('diseaseTable');
        const tbody = table.querySelector('tbody');
        const headers = Array.from(table.querySelectorAll('th.sortable'));
        headers.forEach((th, index) => th.addEventListener('click', () => {{
            const desc = !th.classList.contains('sorted-desc');
            headers.forEach(h => h.classList.remove('sorted-asc', 'sorted-desc'));
            th.classList.add(desc ? 'sorted-desc' : 'sorted-asc');
            const numeric = th.dataset.type === 'number';
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const key = row => {{
                const cell = row.children[index];
                return numeric ? parseFloat(cell.dataset.value ?? cell.textContent) : cell.textContent.trim().toLowerCase();
            }};
            rows.sort((a, b) => {{
                const ka = key(a), kb = key(b);
                const cmp = numeric ? ka - kb : ka.localeCompare(kb);
                return desc ? -cmp : cmp;
            }});
            rows.forEach(row => tbody.appendChild(row));
        }}));
        document.getElementById('diseaseFilter').addEventListener('input', event => {{
            const needle = event.target.value.trim().toLowerCase();
            tbody.querySelectorAll('tr').forEach(row => {{
                row.hidden = needle !== '' && !row.children[0].textContent.toLowerCase().includes(needle);
            }});
        }});
    }})();
    </script>
</body>
</html>
"""


# --------------------------------------------------------------------------- report


def _build_index_block(summary: Mapping[str, Any]) -> str:
    return f"""
        {PHENOTYPE_SYSTEMS_BLOCK_START}
        <section class="chart-card">
            <h2>Phenotype Systems</h2>
            <p class="priority-note">
                The median disease appears in <strong>{_fmt(summary["median_system_count"])}</strong> HPO top-level systems
                but spans <strong>{_fmt(summary["median_effective_system_count"])}</strong> effectively;
                <strong>{_fmt(summary["unique_combination_percent"])}%</strong> of diseases have a combination of systems no other disease shares.
            </p>
            <p><a href="phenotype_systems.html">View the phenotype systems report</a></p>
        </section>
        {PHENOTYPE_SYSTEMS_BLOCK_END}
"""


def inject_phenotype_systems_link(dashboard_index_path: Path, summary: Mapping[str, Any]) -> bool:
    """Insert or update the phenotype-systems section in the dashboard index page."""
    return inject_block(
        dashboard_index_path,
        start_sentinel=PHENOTYPE_SYSTEMS_BLOCK_START,
        end_sentinel=PHENOTYPE_SYSTEMS_BLOCK_END,
        block=_build_index_block(summary),
    )


def generate_phenotype_systems_report(
    kb_dir: Path,
    dashboard_dir: Path,
    dashboard_index_path: Path | None = None,
    hpo_category_cache_path: Path = DEFAULT_HPO_CATEGORY_CACHE,
) -> dict[str, Any]:
    """Write ``phenotype_systems.html`` and ``.json`` under ``dashboard_dir``."""
    categories = load_hpo_category_cache(hpo_category_cache_path)
    data = collect_phenotype_systems(iter_disorders(kb_dir), categories)
    generated_at = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    dashboard_dir.mkdir(parents=True, exist_ok=True)
    json_path = dashboard_dir / "phenotype_systems.json"
    html_path = dashboard_dir / "phenotype_systems.html"
    json_path.write_text(json.dumps({"generated_at": generated_at, **data}, indent=2), encoding="utf-8")
    html_path.write_text(render_phenotype_systems_page(data, generated_at), encoding="utf-8")

    index_updated = False
    if dashboard_index_path is not None:
        index_updated = inject_phenotype_systems_link(dashboard_index_path, data["summary"])
    return {
        "json_path": json_path,
        "html_path": html_path,
        "summary": data["summary"],
        "index_updated": index_updated,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate the phenotype-systems page of the QC dashboard."
    )
    parser.add_argument("--kb-dir", default="kb/disorders", type=Path)
    parser.add_argument("--dashboard-dir", default="dashboard", type=Path)
    parser.add_argument(
        "--dashboard-index",
        default="dashboard/index.html",
        type=Path,
        help="Dashboard index file to patch with a link to the report.",
    )
    parser.add_argument(
        "--hpo-category-cache",
        default=DEFAULT_HPO_CATEGORY_CACHE,
        type=Path,
        help="HP-term-to-system map written by `just gen-browser-data`.",
    )
    args = parser.parse_args(argv)
    kb_cache.default_off()  # one walk of the corpus: a parse cache would only cost memory
    result = generate_phenotype_systems_report(
        kb_dir=args.kb_dir,
        dashboard_dir=args.dashboard_dir,
        dashboard_index_path=args.dashboard_index,
        hpo_category_cache_path=args.hpo_category_cache,
    )
    summary = result["summary"]
    print(
        "Generated phenotype systems report:"
        f" {summary['total_diseases']} diseases,"
        f" median {summary['median_system_count']} systems present,"
        f" median {summary['median_effective_system_count']} effective,"
        f" {summary['unique_combination_percent']}% unique combinations"
    )
    print(f"- HTML: {result['html_path']}")
    print(f"- JSON: {result['json_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
