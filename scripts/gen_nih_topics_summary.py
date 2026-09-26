#!/usr/bin/env python3
"""Generate a self-contained HTML page summarizing NIH-topic tags across dismech.

Scans ``kb/disorders/*.yaml`` (``classifications.nih_research_priority``) and
``projects/*.md`` (``nih_topics`` frontmatter) for the secondary NIH
Highlighted-Topic funding-priority classification, then emits a browsable,
client-side-filterable page grouped by topic.

The page is DERIVED (like all of ``pages/``) — regenerate it, don't hand-edit:

    python scripts/gen_nih_topics_summary.py           # -> pages/nih-topics/index.html
    python scripts/gen_nih_topics_summary.py --check    # fail if stale

It is intentionally not linked from the top-level nav.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

import yaml

from dismech.frontmatter import split_frontmatter
from dismech.yaml_io import safe_load, safe_load_path

ROOT = Path(__file__).resolve().parent.parent
DISORDERS = ROOT / "kb" / "disorders"
PROJECTS = ROOT / "projects"
ENUM_PATH = ROOT / "src" / "dismech" / "schema" / "classifications" / "nih_research_priorities.yaml"
MANIFEST = ROOT / "data" / "nih_highlighted_topics" / "MANIFEST.yaml"
OUT = ROOT / "pages" / "nih-topics" / "index.html"


def _load_topics() -> dict[str, dict]:
    """key -> {number, title, expires, url} from the generated enum descriptions."""
    doc = safe_load_path(ENUM_PATH)
    pvs = doc["enums"]["NIHResearchPriorityEnum"]["permissible_values"]
    topics: dict[str, dict] = {}
    for key, meta in pvs.items():
        desc = (meta or {}).get("description", "")
        title = desc.split(" (NIH Highlighted Topic", 1)[0].strip()
        num = key.split("_")[2]
        exp = re.search(r"expires ([^)]+)\)", desc)
        url = re.search(r"(https?://\S+)", desc)
        topics[key] = {
            "key": key,
            "number": int(num),
            "title": title,
            "expires": exp.group(1) if exp else "",
            "url": url.group(1) if url else "",
        }
    return topics


def _snapshot_date() -> str:
    for line in MANIFEST.read_text().splitlines():
        m = re.match(r'\s*snapshot_date:\s*"?([0-9-]+)"?', line)
        if m:
            return m.group(1)
    return ""


def _split_front_matter(text: str) -> dict:
    # Delimiter-aware (issue #7697): ``---`` inside a value is not a delimiter.
    split = split_frontmatter(text)
    if split is None:
        return {}
    try:
        return safe_load(split.frontmatter) or {}
    except yaml.YAMLError:
        return {}


def _collect() -> dict[str, dict]:
    """topic_key -> {diseases: [...], projects: [...]}."""
    hits: dict[str, dict] = {}

    def bucket(key: str) -> dict:
        return hits.setdefault(key, {"diseases": [], "projects": []})

    # Disorders — grep-prefilter to avoid parsing all ~1.5k files.
    for path in sorted(DISORDERS.glob("*.yaml")):
        text = path.read_text()
        if "nih_research_priority" not in text:
            continue
        data = safe_load(text) or {}
        assignments = (
            (data.get("classifications") or {}).get("nih_research_priority") or []
        )
        for a in assignments:
            if not isinstance(a, dict) or not a.get("classification_value"):
                continue
            bucket(a["classification_value"])["diseases"].append({
                "name": data.get("name") or path.stem,
                "slug": path.stem,
                "notes": a.get("notes", ""),
            })

    # Projects.
    for path in sorted(PROJECTS.glob("*.md")):
        meta = _split_front_matter(path.read_text())
        for key in meta.get("nih_topics") or []:
            bucket(str(key))["projects"].append({
                "title": meta.get("title") or path.stem,
                "slug": path.stem,
                "status": str(meta.get("status") or ""),
            })

    for entry in hits.values():
        entry["diseases"].sort(key=lambda d: d["name"].casefold())
        entry["projects"].sort(key=lambda p: p["title"].casefold())
    return hits


def build() -> str:
    topics = _load_topics()
    hits = _collect()
    snapshot = _snapshot_date()

    cards = []
    for key, topic in sorted(topics.items(), key=lambda kv: kv[1]["number"]):
        h = hits.get(key, {"diseases": [], "projects": []})
        cards.append({
            **topic,
            "diseases": h["diseases"],
            "projects": h["projects"],
            "count": len(h["diseases"]) + len(h["projects"]),
        })

    n_disease_tags = sum(len(c["diseases"]) for c in cards)
    n_project_tags = sum(len(c["projects"]) for c in cards)
    n_topics_used = sum(1 for c in cards if c["count"])
    data_json = json.dumps(cards)

    return _TEMPLATE.format(
        data=data_json,
        snapshot=html.escape(snapshot),
        n_topics=len(cards),
        n_topics_used=n_topics_used,
        n_disease_tags=n_disease_tags,
        n_project_tags=n_project_tags,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="Fail if the page is stale.")
    args = ap.parse_args()

    content = build()
    if args.check:
        current = OUT.read_text() if OUT.exists() else ""
        if current != content:
            print("OUT OF DATE: run python scripts/gen_nih_topics_summary.py", file=sys.stderr)
            return 1
        print("OK: pages/nih-topics/index.html is up to date.")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content)
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NIH Funding-Topic Coverage — dismech</title>
<style>
:root {{
  --bg:#f7f8fa; --card:#fff; --ink:#1a1f2b; --muted:#5b6472; --line:#e4e7ec;
  --accent:#3457b2; --accent-bg:#eef4ff; --accent-line:#c7d7fe; --chip:#f0f2f5;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg:#0f1420; --card:#171d2b; --ink:#e8ecf3; --muted:#9aa4b4; --line:#28304050;
    --accent:#9bb8ff; --accent-bg:#1b2540; --accent-line:#2f4270; --chip:#212938;
  }}
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink);
  font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }}
.wrap {{ max-width:1000px; margin:0 auto; padding:2rem 1.25rem 4rem; }}
h1 {{ font-size:1.6rem; margin:0 0 .3rem; }}
.sub {{ color:var(--muted); margin:0 0 1.25rem; font-size:.9rem; }}
.stats {{ display:flex; flex-wrap:wrap; gap:.6rem; margin:0 0 1.25rem; }}
.stat {{ background:var(--card); border:1px solid var(--line); border-radius:9px;
  padding:.55rem .8rem; min-width:120px; }}
.stat b {{ display:block; font-size:1.35rem; }}
.stat span {{ color:var(--muted); font-size:.78rem; }}
.controls {{ display:flex; flex-wrap:wrap; gap:.75rem; align-items:center; margin:0 0 1.25rem; }}
#q {{ flex:1; min-width:220px; padding:.55rem .75rem; border:1px solid var(--line);
  border-radius:9px; background:var(--card); color:var(--ink); font-size:.95rem; }}
label.tog {{ color:var(--muted); font-size:.85rem; user-select:none; cursor:pointer; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:12px;
  padding:1rem 1.1rem; margin:0 0 .85rem; }}
.card.empty {{ opacity:.55; }}
.card h2 {{ font-size:1.05rem; margin:0 0 .15rem; display:flex; gap:.5rem; align-items:baseline; }}
.card h2 a {{ color:var(--accent); text-decoration:none; }}
.card h2 a:hover {{ text-decoration:underline; }}
.num {{ font-variant-numeric:tabular-nums; color:var(--muted); font-weight:600; font-size:.8rem;
  background:var(--accent-bg); border:1px solid var(--accent-line); border-radius:6px;
  padding:.05rem .4rem; white-space:nowrap; }}
.meta {{ color:var(--muted); font-size:.78rem; margin:.1rem 0 .6rem; }}
.grp {{ margin:.5rem 0 0; }}
.grp h3 {{ font-size:.72rem; text-transform:uppercase; letter-spacing:.05em;
  color:var(--muted); margin:.4rem 0 .35rem; }}
.items {{ display:flex; flex-wrap:wrap; gap:.4rem; }}
.pill {{ display:inline-block; background:var(--chip); border:1px solid var(--line);
  border-radius:999px; padding:.2rem .6rem; font-size:.82rem; color:var(--ink);
  text-decoration:none; }}
.pill:hover {{ border-color:var(--accent-line); }}
.pill.proj {{ background:var(--accent-bg); border-color:var(--accent-line); color:var(--accent); }}
.pill .st {{ color:var(--muted); font-size:.7rem; }}
.none {{ color:var(--muted); font-size:.85rem; font-style:italic; }}
footer {{ color:var(--muted); font-size:.75rem; margin-top:1.5rem; }}
/* Reader-facing AI-curation / not-medical-advice disclaimer. Mirrors
   src/dismech/templates/_disclaimer.html.j2 — keep the wording in step.
   Styled with this page's own tokens so it works in light and dark mode. */
/* Flex rather than an absolutely positioned button: the dismiss control stays
   in flow, so it can never overlap the text however the bar wraps. */
.dismech-disclaimer {{ display:flex; align-items:center; gap:8px; width:100%;
  box-sizing:border-box; margin:0; padding:10px 16px; background:var(--card);
  color:var(--muted); border-bottom:1px solid var(--line); font-size:.85rem;
  line-height:1.5; text-align:center; }}
/* `display:flex` above outranks the UA rule for the `hidden` attribute. */
.dismech-disclaimer[hidden] {{ display:none; }}
.dismech-disclaimer p {{ flex:1 1 auto; min-width:0; max-width:1000px;
  margin:0 auto; }}
.dismech-disclaimer strong {{ color:var(--ink); }}
.dismech-disclaimer a {{ color:var(--accent); text-decoration:underline; }}
/* Hidden until the script confirms it can act on a click, so a reader without
   JavaScript is never shown a dead control. */
.dismech-disclaimer-dismiss {{ display:none; }}
/* margin-right clears the Hypothes.is sidebar toolbar, which covers the
   rightmost ~33px of the pages that embed the annotation client and swallows
   clicks there. Applied everywhere for consistency. */
.dismech-disclaimer.is-dismissible .dismech-disclaimer-dismiss {{
  display:flex; flex:0 0 auto; margin-right:28px;
  align-items:center; justify-content:center;
  width:28px; height:28px; padding:0; border:0; border-radius:4px;
  background:none; color:inherit; font:inherit; font-size:1.15rem;
  line-height:1; cursor:pointer; }}
.dismech-disclaimer-dismiss:hover {{ background:var(--chip); }}
.dismech-disclaimer-dismiss:focus-visible {{ outline:2px solid var(--accent);
  outline-offset:2px; }}
/* The button's footprint sits only on the right, so the centred text lands about
   half that left of true centre. Mirroring it fixes that but costs the same width
   again, so it applies only where there is room to spare. */
@media (min-width: 900px) {{
  .dismech-disclaimer.is-dismissible::before {{ content:""; flex:0 0 auto;
    width:28px; margin-left:28px; }}
}}
</style>
</head>
<body>
<aside class="dismech-disclaimer" aria-label="DisMech disclaimer">
  <p>
    <strong>AI-curated research resource &mdash; not medical advice.</strong>
    DisMech content is generated and maintained by AI curation agents under human
    review, from publicly accessible literature and curated biomedical knowledge
    resources. Nothing here is intended to inform medical diagnosis or treatment.
    <a href="https://dismech.monarchinitiative.org/elements/disclaimer/">Read the full disclaimer</a>.
  </p>
  <button type="button" class="dismech-disclaimer-dismiss"
          aria-label="Dismiss this disclaimer" title="Dismiss this disclaimer">
    <span aria-hidden="true">&times;</span>
  </button>
</aside>
<!-- Runs synchronously, immediately after the bar, so an already-dismissed bar is
     hidden before first paint rather than flashing and disappearing. Dismissal is
     kept for the browsing session in sessionStorage; see design-decisions.md §11. -->
<script>
  (function () {{
    var KEY = 'dismech-disclaimer-dismissed';
    var bar = document.querySelector('.dismech-disclaimer');
    if (!bar) {{ return; }}
    // sessionStorage access itself throws when storage is blocked (Safari
    // private browsing, cookies-disabled), so every use is guarded.
    var store = null;
    try {{ store = window.sessionStorage; }} catch (err) {{ store = null; }}
    try {{
      if (store && store.getItem(KEY) === '1') {{ bar.hidden = true; return; }}
    }} catch (err) {{ /* unreadable storage: show the bar */ }}
    var button = bar.querySelector('.dismech-disclaimer-dismiss');
    if (!button) {{ return; }}
    bar.classList.add('is-dismissible');
    button.addEventListener('click', function () {{
      bar.hidden = true;
      try {{ if (store) {{ store.setItem(KEY, '1'); }} }} catch (err) {{ /* not persisted */ }}
      // Focus would otherwise fall back to <body>, losing a keyboard reader's
      // place. preventScroll keeps the viewport where it was.
      var next = document.querySelector('main, h1');
      if (next) {{
        if (!next.hasAttribute('tabindex')) {{ next.setAttribute('tabindex', '-1'); }}
        try {{ next.focus({{ preventScroll: true }}); }} catch (err) {{ next.focus(); }}
      }}
    }});
  }})();
</script>
<div class="wrap">
  <h1>NIH Funding-Topic Coverage</h1>
  <p class="sub">Secondary <code>nih_research_priority</code> tags across dismech disease
  entries and curation projects. NIH Highlighted-Topics snapshot: {snapshot}. This is a
  soft, grant-strategy classification — not a disease nosology.</p>

  <div class="stats">
    <div class="stat"><b>{n_topics_used}</b><span>topics with tags</span></div>
    <div class="stat"><b>{n_disease_tags}</b><span>disease tags</span></div>
    <div class="stat"><b>{n_project_tags}</b><span>project tags</span></div>
    <div class="stat"><b>{n_topics}</b><span>topics available</span></div>
  </div>

  <div class="controls">
    <input id="q" type="search" placeholder="Filter by topic title, disease, or project…">
    <label class="tog"><input type="checkbox" id="onlyTagged" checked> only tagged topics</label>
  </div>

  <div id="list"></div>
  <footer>Derived page — regenerate with <code>python scripts/gen_nih_topics_summary.py</code>.
  See <code>docs/nih-research-priorities.md</code>.</footer>
</div>

<script>
const DATA = {data};
const list = document.getElementById('list');
const q = document.getElementById('q');
const onlyTagged = document.getElementById('onlyTagged');

function esc(s) {{ const d = document.createElement('div'); d.textContent = s ?? ''; return d.innerHTML; }}

function render() {{
  const term = q.value.trim().toLowerCase();
  const tagged = onlyTagged.checked;
  list.innerHTML = '';
  let shown = 0;
  for (const t of DATA) {{
    if (tagged && t.count === 0) continue;
    const hay = (t.title + ' ' +
      t.diseases.map(d => d.name).join(' ') + ' ' +
      t.projects.map(p => p.title).join(' ')).toLowerCase();
    if (term && !hay.includes(term)) continue;
    shown++;
    const card = document.createElement('div');
    card.className = 'card' + (t.count === 0 ? ' empty' : '');
    let html = '';
    html += '<h2><a href="' + esc(t.url) + '" target="_blank" rel="noopener">#' + t.number +
            ' · ' + esc(t.title) + '</a> <span class="num">' + t.count + '</span></h2>';
    html += '<div class="meta">' + (t.expires ? 'expires ' + esc(t.expires) : '') + '</div>';
    if (t.diseases.length) {{
      html += '<div class="grp"><h3>Diseases (' + t.diseases.length + ')</h3><div class="items">';
      for (const d of t.diseases) {{
        html += '<a class="pill" href="../disorders/' + esc(d.slug) + '.html" title="' +
                esc(d.notes) + '">' + esc(d.name) + '</a>';
      }}
      html += '</div></div>';
    }}
    if (t.projects.length) {{
      html += '<div class="grp"><h3>Projects (' + t.projects.length + ')</h3><div class="items">';
      for (const p of t.projects) {{
        html += '<a class="pill proj" href="../projects/' + esc(p.slug) + '.html">' +
                esc(p.title) + (p.status ? ' <span class="st">' + esc(p.status) + '</span>' : '') +
                '</a>';
      }}
      html += '</div></div>';
    }}
    if (t.count === 0) html += '<div class="none">No entries tagged yet.</div>';
    card.innerHTML = html;
    list.appendChild(card);
  }}
  if (!shown) list.innerHTML = '<p class="none">No topics match.</p>';
}}
q.addEventListener('input', render);
onlyTagged.addEventListener('change', render);
render();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    raise SystemExit(main())
