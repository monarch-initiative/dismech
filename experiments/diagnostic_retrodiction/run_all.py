"""Resumable orchestrator for the diagnostic-retrodiction experiment (DRAFT; nothing run yet).

Stages, each with a done-marker (DONE file) per unit, so a rerun resumes where it stopped:
  packets   PubMed packet per unit, built once into the shared cache and never refetched
  curation  two time-sliced replicates per unit: an isolated git worktree at PINNED_COMMIT with
            excluded files left out by sparse checkout, `claude -p` with the deny rules, then
            check_cutoff.py, `just validate`, audit_transcript.py; one retry on failure
  arms      A1, A2, A3, A4, A5 (3 scramble seeds), A6 (25/50/75/100% ablation), A7; 3 runs per
            replicate, k = 10; plus the knowledge probe (once per display name)
  scoring   match.py, LLM adjudication of what matching cannot settle (prompts/adjudicate.md,
            blind to arm), and a blinded 20% human adjudication sample file
  analysis  analysis.py; every metric PROVISIONAL until human adjudication is complete
  findings  FINDINGS draft from the metrics

Dedupe (efficiency):
  - A unit is (DisMech entry, cutoff_date). Cases sharing both share one packet, one pair of
    curation replicates and one set of unit-level arm outputs (A1, A2, A3, A5), each scored
    against its own rubric. A6 and A7 depend on the case's rubric, so they run per case.
  - A4 is deduplicated by (arm_display_name, cutoff year); the probe by arm_display_name.
  - A1, the A5 scrambles and the A6 ablations are computed once per replicate and reused.
Caches (on disk, never refetched): packets and E-utilities results under tmp/retro_cache/,
the disease-name -> kb file map, and MONDO lookups (already cached in literature_check.tsv).

LLM calls:
  - ANTHROPIC_API_KEY set: the Message Batches API, model from RUN_CONFIG.yaml, with prompt
    caching on the shared system prompt (prompts/arm_system.md) and structured output from
    schemas/candidate.yaml. Claude Opus 5.5 accepts no sampling parameters (temperature returns
    a 400), so temperature 0 cannot be set; that deviation is logged on every run.
  - Otherwise: `claude -p` with --json-schema, run in parallel (--workers, default 4); the same
    temperature deviation is logged.
  - Every output is validated against the schema; only invalid outputs are retried, once.
  - --max-calls: the estimated call count is printed and the run stops if it exceeds the budget.

Held-out guard: --split test runs anything other than --dry-run only with
--confirm-heldout I-HAVE-PREREGISTERED.

Usage:
    python run_all.py --split dev --dry-run
    python run_all.py --split dev --stages packets,curation --workers 4 --max-calls 200
    python run_all.py --split test --confirm-heldout I-HAVE-PREREGISTERED --max-calls 20000
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CACHE = ROOT / "tmp" / "retro_cache"
RUNS = HERE / "runs"
SEED = 20261114
STAGES = ("packets", "curation", "arms", "scoring", "analysis", "findings")
HELDOUT_PHRASE = "I-HAVE-PREREGISTERED"
A5_SEEDS = (1, 2, 3)
A6_LEVELS = (25, 50, 75, 100)

# Planning assumptions for --dry-run estimates (tokens per call; minutes per call). Not measured:
# replace with measured values from the first dev run before estimating the test run.
EST = {
    "curation_input_tokens": 1_500_000, "curation_output_tokens": 60_000, "curation_minutes": 30,
    "system_tokens": 400, "entry_tokens": 12_000, "abstract_tokens": 350, "arm_literature_max": 60,
    "arm_output_tokens": 6_000, "arm_minutes_cli": 1.5,
    "adjudication_input_tokens": 6_000, "adjudication_output_tokens": 2_000,
    "curation_retry_rate": 0.10,
}
PRICE = {"input": 4.00, "output": 20.00, "cache_read": 0.20, "batch_discount": 0.5}  # $/MTok, claude-opus-5-5


# ------------------------------------------------------------------ inputs
def read_tsv(p: Path) -> list[dict]:
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def run_config() -> dict:
    return yaml.safe_load((HERE / "RUN_CONFIG.yaml").read_text())


def kb_file_map(names: set[str]) -> dict[str, str]:
    """Disease entry name -> kb/disorders file at PINNED_COMMIT, cached on disk."""
    path = CACHE / "kb_file_map.json"
    m = json.loads(path.read_text()) if path.exists() else {}
    commit = (HERE / "PINNED_COMMIT").read_text().strip()
    for name in sorted(names - set(m)):
        out = subprocess.run(["git", "-C", str(ROOT), "grep", "-l", "-P", "-e", f"^name: {re.escape(name)}$", commit,
                              "--", "kb/disorders"], capture_output=True, text=True).stdout.split()
        files = sorted({o.split(":", 1)[1] for o in out})
        if len(files) != 1:
            sys.exit(f"{name}: {len(files)} kb files at {commit}; resolve by hand in {path}")
        m[name] = files[0]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(m, indent=1, sort_keys=True))
    return m


@dataclass
class Case:
    cid: str
    disease: str
    kb_file: str
    cutoff: str
    display: str
    split: str
    negative: bool
    rubric: dict
    lit_query: str
    packet_size: int | None

    @property
    def unit(self) -> str:
        return f"{Path(self.kb_file).stem}__{self.cutoff}"


@dataclass
class Plan:
    split: str
    cases: list[Case]
    units: dict[str, list[Case]] = field(default_factory=dict)
    a4_units: dict[tuple, list[Case]] = field(default_factory=dict)
    probe_units: dict[str, list[Case]] = field(default_factory=dict)


def load_plan(split: str) -> Plan:
    ids = set((HERE / f"{split}_set.txt").read_text().split())
    dating = {r["case_id"]: r for r in read_tsv(HERE / "dating.tsv")}
    lit = {r["case_id"]: r for r in read_tsv(HERE / "literature_check.tsv")}
    cases = []
    names = {dating[c]["disease"] for c in ids}
    negs = read_tsv(HERE / "negatives.tsv") if split == "test" else []
    kbmap = kb_file_map(names)
    for cid in sorted(ids):
        r = dating[cid]
        rub = yaml.safe_load((HERE / "rubrics" / f"{cid}.yaml").read_text(encoding="utf-8"))
        cases.append(Case(cid, r["disease"], kbmap[r["disease"]], r["cutoff_date"], rub["arm_display_name"]["name"],
                          split, False, rub, _strip_abstract(lit[cid]["lit_query"]), _int(lit[cid]["lit_count"])))
    neg_lit = {r["slot"]: r for r in read_tsv(HERE / "negatives_literature_check.tsv")} if negs else {}
    for n in negs:  # negatives are run with the test split only (README, Decisions)
        rub = yaml.safe_load((HERE / "rubrics" / f"{n['slot']}.yaml").read_text(encoding="utf-8"))
        cases.append(Case(n["slot"], n["disease"], n["kb_file"], n["cutoff_date"], rub["arm_display_name"]["name"],
                          split, True, rub, _strip_abstract(neg_lit.get(n["slot"], {}).get("lit_query", "")),
                          _int(n["lit_count"])))
    p = Plan(split, cases)
    for c in cases:
        p.units.setdefault(c.unit, []).append(c)
        p.a4_units.setdefault((c.display, c.cutoff[:4]), []).append(c)
        p.probe_units.setdefault(c.display, []).append(c)
    return p


def _strip_abstract(q: str) -> str:
    return re.sub(r"\s+AND hasabstract\s*$", "", q or "")


def _int(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return None


# ------------------------------------------------------------------ call accounting
def count_calls(plan: Plan, dedupe: bool, cfg: dict) -> dict:
    runs = cfg["runs_per_llm_arm"]
    reps = cfg.get("curation_replicates", 2)
    unit_groups = list(plan.units.values()) if dedupe else [[c] for c in plan.cases]
    a4_groups = list(plan.a4_units.values()) if dedupe else [[c] for c in plan.cases]
    probe_groups = list(plan.probe_units.values()) if dedupe else [[c] for c in plan.cases]
    n_units = len(unit_groups)
    per_unit = {"A2": reps * runs, "A3": reps * runs, "A5": len(A5_SEEDS) * reps * runs}
    per_case = {"A6": len(A6_LEVELS) * reps * runs, "A7": reps * runs}
    positives = [c for c in plan.cases if not c.negative]
    calls = {
        "curation_sessions": n_units * reps,
        "curation_sessions_with_all_retries": n_units * reps * 2,
        "A2": n_units * per_unit["A2"], "A3": n_units * per_unit["A3"], "A5": n_units * per_unit["A5"],
        "A6": len(positives) * per_case["A6"], "A7": len(plan.cases) * per_case["A7"],
        "A4": len(a4_groups) * reps * runs, "probe": len(probe_groups),
    }
    outputs_per_positive = (per_unit["A2"] + per_unit["A3"] + per_unit["A5"] + per_case["A6"] + per_case["A7"]
                            + reps * runs + reps)  # + A4 and A1 outputs
    calls["adjudication"] = len(positives) * outputs_per_positive
    calls["llm_calls_excluding_curation"] = sum(v for k, v in calls.items()
                                                if k not in ("curation_sessions", "curation_sessions_with_all_retries"))
    calls["units"] = n_units
    calls["a4_units"] = len(a4_groups)
    calls["probe_units"] = len(probe_groups)
    return calls


def estimate(plan: Plan, calls: dict, api: bool, workers: int) -> dict:
    lit_tokens = EST["arm_literature_max"] * EST["abstract_tokens"]
    arm_in = {"A2": EST["entry_tokens"] + lit_tokens, "A3": lit_tokens, "A4": 200, "A5": EST["entry_tokens"] + lit_tokens,
              "A6": EST["entry_tokens"] + lit_tokens, "A7": EST["entry_tokens"], "probe": 200}
    disc = PRICE["batch_discount"] if api else 1.0
    cost = 0.0
    for arm, tin in arm_in.items():
        n = calls[arm]
        cost += n * disc * ((tin * PRICE["input"] + EST["system_tokens"] * PRICE["cache_read"]
                             + EST["arm_output_tokens"] * PRICE["output"]) / 1e6)
    cost += calls["adjudication"] * disc * (EST["adjudication_input_tokens"] * PRICE["input"]
                                            + EST["adjudication_output_tokens"] * PRICE["output"]) / 1e6
    cur_n = calls["curation_sessions"] * (1 + EST["curation_retry_rate"])
    cur_cost = cur_n * (EST["curation_input_tokens"] * PRICE["input"] + EST["curation_output_tokens"] * PRICE["output"]) / 1e6
    llm_n = calls["llm_calls_excluding_curation"]
    hours_arms = (llm_n * EST["arm_minutes_cli"] / 60 / workers) if not api else None
    return {"arms_scoring_cost_usd": round(cost, 2), "curation_cost_usd_api_equivalent": round(cur_cost, 2),
            "curation_hours_at_workers": round(cur_n * EST["curation_minutes"] / 60 / workers, 1),
            "arms_scoring_hours": round(hours_arms, 1) if hours_arms is not None else "batch: within 24 h (most < 1 h)",
            "assumptions": EST, "pricing_per_mtok": PRICE}


# ------------------------------------------------------------------ markers and logging
def marker(*parts: str) -> Path:
    return RUNS.joinpath(*parts) / "DONE"


def done(*parts: str) -> bool:
    return marker(*parts).exists()


def mark(*parts: str, info: dict | None = None) -> None:
    m = marker(*parts)
    m.parent.mkdir(parents=True, exist_ok=True)
    m.write_text(json.dumps({"utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), **(info or {})}))


def log_deviation(split: str, text: str) -> None:
    p = RUNS / split / "deviations.log"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(f"{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}\t{text}\n")


# ------------------------------------------------------------------ stage: packets
def stage_packets(plan: Plan) -> None:
    for unit, cs in sorted(plan.units.items()):
        out = CACHE / "packets" / unit
        if (out / "DONE").exists():
            continue
        q = cs[0].lit_query
        if not q:
            sys.exit(f"{unit}: no literature query; run the literature check first")
        subprocess.run([sys.executable, str(HERE / "build_packet.py"), "--term", q, "--maxdate",
                        cs[0].cutoff.replace("-", "/"), "--out", str(out)], check=True)
        (out / "DONE").write_text(dt.date.today().isoformat())
        print(f"packet {unit}: {json.loads((out / 'packet_meta.json').read_text())['kept']} records")


def packet_dir(unit: str) -> Path:
    return CACHE / "packets" / unit


# ------------------------------------------------------------------ stage: curation
def leakage_no(cases: list[Case]) -> list[str]:
    terms = set()
    for c in cases:
        terms |= {t["term"] for t in c.rubric.get("leakage_terms", []) if t["in_packet"] == "no"}
    return sorted(terms)


def make_worktree(unit: str, rep: int, attempt: int, cases: list[Case], split: str) -> Path:
    commit = (HERE / "PINNED_COMMIT").read_text().strip()
    wt = RUNS / split / "worktrees" / f"{unit}__r{rep}__a{attempt}"
    if wt.exists():
        subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(wt)], check=False)
    subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "--detach", "--no-checkout", str(wt), commit], check=True)
    excluded = ["/experiments/", "/references_cache/", f"/{cases[0].kb_file}", "/research/", "/pages/", "/history/"]
    for term in leakage_no(cases):  # files outside experiments/ naming an absent leakage term
        out = subprocess.run(["git", "-C", str(ROOT), "grep", "-l", "-i", "-F", "-e", term, commit, "--", ":!experiments"],
                             capture_output=True, text=True).stdout.split()
        excluded += ["/" + o.split(":", 1)[1] for o in out]
    patterns = ["/*"] + [f"!{e}" for e in sorted(set(excluded))]
    subprocess.run(["git", "-C", str(wt), "sparse-checkout", "init", "--no-cone"], check=True)
    (wt / ".git").exists()
    subprocess.run(["git", "-C", str(wt), "sparse-checkout", "set", "--no-cone", "--stdin"], input="\n".join(patterns),
                   text=True, check=True)
    subprocess.run(["git", "-C", str(wt), "checkout"], check=True)
    shutil.copytree(packet_dir(unit), wt / "packet", dirs_exist_ok=True)
    deny = json.loads((ROOT / ".claude" / "curation-deny.json").read_text())
    (wt / ".claude").mkdir(exist_ok=True)
    (wt / ".claude" / "settings.json").write_text(json.dumps(deny, indent=2))
    (wt / "EXCLUDED_PATHS.txt").write_text("\n".join(sorted(set(excluded))))
    return wt


def curate_once(plan: Plan, unit: str, rep: int, attempt: int) -> tuple[bool, Path]:
    cases = plan.units[unit]
    c0 = cases[0]
    wt = make_worktree(unit, rep, attempt, cases, plan.split)
    entry = f"kb/disorders/{Path(c0.kb_file).stem}.yaml"
    prompt = (HERE / "prompts" / "curation.md").read_text().split("-->", 1)[1].format(
        DISPLAY_NAME=c0.display, CUTOFF_DATE=c0.cutoff, CUTOFF_YEAR=c0.cutoff[:4], ENTRY_PATH=entry, PACKET_DIR="packet/")
    out = RUNS / plan.split / "curation" / unit / f"r{rep}" / f"attempt{attempt}"
    out.mkdir(parents=True, exist_ok=True)
    deny = json.loads((ROOT / ".claude" / "curation-deny.json").read_text())["permissions"]["deny"]
    with open(out / "transcript.jsonl", "w", encoding="utf-8") as tf:
        subprocess.run(["claude", "-p", prompt, "--output-format", "stream-json", "--verbose",
                        "--model", run_config()["models"]["primary"], "--settings", str(wt / ".claude" / "settings.json"),
                        "--permission-mode", "acceptEdits", "--no-session-persistence",
                        "--allowedTools", "Read", "Grep", "Glob", "Write", "Edit", "Bash(just validate:*)",
                        "--disallowedTools", *deny], cwd=wt, stdout=tf, stderr=subprocess.STDOUT, check=False)
    ok, checks = True, {}
    banned = out / "leakage_terms_absent_from_packet.txt"
    banned.write_text("\n".join(leakage_no(cases)) + "\n", encoding="utf-8")
    ep = wt / entry
    if not ep.exists():
        return False, out
    checks["check_cutoff"] = subprocess.run([sys.executable, str(HERE / "check_cutoff.py"), str(ep), "--packet",
                                             str(packet_dir(unit) / "packet.tsv"), "--banned", str(banned)],
                                            capture_output=True, text=True).returncode
    checks["validate"] = subprocess.run(["just", "validate", entry], cwd=wt, capture_output=True, text=True).returncode
    excl = (wt / "EXCLUDED_PATHS.txt").read_text().split()
    checks["audit"] = subprocess.run([sys.executable, str(HERE / "audit_transcript.py"), str(out / "transcript.jsonl"),
                                      "--packet", str(packet_dir(unit) / "packet.tsv"),
                                      *sum((["--exclude", e.lstrip("/") + "**"] for e in excl), []),
                                      "--out", str(out / "audit.json")], capture_output=True, text=True).returncode
    for c in cases:  # each case's own absent leakage terms, on the entry itself
        if c.negative:
            continue
        r = subprocess.run([sys.executable, str(HERE / "audit_transcript.py"), str(out / "transcript.jsonl"),
                            "--packet", str(packet_dir(unit) / "packet.tsv"), "--rubric",
                            str(HERE / "rubrics" / f"{c.cid}.yaml"), "--out", str(out / f"audit_{c.cid}.json")],
                           capture_output=True, text=True)
        checks[f"audit_{c.cid}"] = r.returncode
    ok = all(v == 0 for v in checks.values())
    (out / "checks.json").write_text(json.dumps(checks, indent=2))
    if ok:
        shutil.copy(ep, out.parent / "entry.yaml")
    return ok, out


def stage_curation(plan: Plan, workers: int) -> None:
    cfg = run_config()
    jobs = [(u, r) for u in sorted(plan.units) for r in range(1, cfg.get("curation_replicates", 2) + 1)
            if not done(plan.split, "curation", u, f"r{r}")]

    def one(job):
        u, r = job
        for attempt in (1, 2):  # one retry
            ok, out = curate_once(plan, u, r, attempt)
            if ok:
                mark(plan.split, "curation", u, f"r{r}", info={"attempt": attempt})
                return
            log_deviation(plan.split, f"curation {u} r{r} attempt {attempt} failed ({out / 'checks.json'})")
        log_deviation(plan.split, f"curation {u} r{r} failed twice; unit has no replicate {r}")
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(one, jobs))


# ------------------------------------------------------------------ arm inputs
def load_entry(split: str, unit: str, rep: int) -> dict | None:
    p = RUNS / split / "curation" / unit / f"r{rep}" / "entry.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None


def cited_literature(entry: dict, unit: str) -> str:
    """The packet abstracts the curated entry cites (the arm literature packet), oldest first."""
    cited = set(re.findall(r"PMID:\d+", yaml.safe_dump(entry)))
    rows = [json.loads(l) for l in (packet_dir(unit) / "abstracts.jsonl").read_text(encoding="utf-8").splitlines()]
    keep = sorted((r for r in rows if r["pmid"] in cited), key=lambda r: (r["date"], r["pmid"]))
    return "\n\n".join(f"[{r['pmid']}, {r['date'][:4]}] {r['title']}\n{r['abstract']}" for r in keep)


def edges(entry: dict) -> list[tuple[int, int]]:
    nodes = entry.get("pathophysiology") or []
    idx = {n.get("name"): i for i, n in enumerate(nodes)}
    return [(i, idx[d["target"]]) for i, n in enumerate(nodes) for d in (n.get("downstream") or [])
            if d.get("target") in idx]


def scramble(entry: dict, seed: int) -> dict:
    """A5: degree-preserving double-edge swaps of the causal pathophysiology edges, 10 x edge count."""
    e = json.loads(json.dumps(entry))
    nodes = e.get("pathophysiology") or []
    E = edges(e)
    rng = random.Random(seed)
    es = list(E)
    for _ in range(10 * len(es)):
        if len(es) < 2:
            break
        i, j = rng.sample(range(len(es)), 2)
        (a, b), (c, d) = es[i], es[j]
        if len({a, b, c, d}) < 4 or (a, d) in es or (c, b) in es:
            continue
        es[i], es[j] = (a, d), (c, b)
    names = [n.get("name") for n in nodes]
    targets = defaultdict(list)
    for a, b in es:
        targets[a].append(names[b])
    for i, n in enumerate(nodes):
        old = {d["target"]: d for d in (n.get("downstream") or []) if d.get("target") in names}
        others = [d for d in (n.get("downstream") or []) if d.get("target") not in names]
        n["downstream"] = [{**(next(iter(old.values()), {})), "target": t} for t in targets.get(i, [])] + others
    return e


def ablate(entry: dict, target_name: str, pct: int, seed: int) -> dict:
    """A6: remove pct% of the nodes on causal paths from the root(s) to target_name, nearest first."""
    e = json.loads(json.dumps(entry))
    nodes = e.get("pathophysiology") or []
    names = [n.get("name") for n in nodes]
    if target_name not in names:
        return e
    E = edges(e)
    preds = defaultdict(set)
    for a, b in E:
        preds[b].add(a)
    t = names.index(target_name)
    dist, frontier = {t: 0}, [t]
    while frontier:
        nxt = []
        for x in frontier:
            for p in preds[x]:
                if p not in dist:
                    dist[p] = dist[x] + 1
                    nxt.append(p)
        frontier = nxt
    path = sorted((i for i in dist if i != t), key=lambda i: (dist[i], random.Random(seed + i).random()))
    drop = {names[i] for i in path[: round(len(path) * pct / 100)]}
    e["pathophysiology"] = [n for n in nodes if n.get("name") not in drop]
    for n in e["pathophysiology"]:
        n["downstream"] = [d for d in (n.get("downstream") or []) if d.get("target") not in drop]
    return e


def t1_target_node(entry: dict, rubric: dict) -> str | None:
    """The pathophysiology node bound to the rubric's T1 GO term or one of its descendants (go.db)."""
    import sqlite3
    go = Path.home() / ".data" / "oaklib" / "go.db"
    anchor = rubric["T1"]["process"]["id"]
    db = sqlite3.connect(f"file:{go}?mode=ro", uri=True) if go.exists() else None
    for n in entry.get("pathophysiology") or []:
        ids = re.findall(r"GO:\d{7}", yaml.safe_dump(n))
        for i in ids:
            if i == anchor or (db and db.execute("select 1 from entailed_edge where subject=? and predicate='rdfs:subClassOf' "
                                                  "and object=? limit 1", (i, anchor)).fetchone()):
                return n.get("name")
    return None


def a7_entry(case: Case) -> dict:
    """A7: the entry at PINNED_COMMIT without the test's own rows and without any node or evidence item
    naming one of the case's leakage terms."""
    commit = (HERE / "PINNED_COMMIT").read_text().strip()
    e = yaml.safe_load(subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:{case.kb_file}"],
                                      capture_output=True, text=True, check=True).stdout)
    terms = [t["term"] for t in case.rubric.get("leakage_terms", [])]
    rx = re.compile("|".join(rf"(?<![\w-]){re.escape(t)}(?![\w-])" for t in terms), re.I) if terms else None

    def clean(items):
        out = []
        for it in items or []:
            if rx and rx.search(yaml.safe_dump(it, allow_unicode=True)):
                continue
            out.append(it)
        return out
    for sec in ("diagnosis", "biochemical", "pathophysiology", "phenotypes", "genetic", "treatments"):
        if sec in e:
            e[sec] = clean(e[sec])
    for sec in ("pathophysiology", "phenotypes"):
        for n in e.get(sec) or []:
            n["evidence"] = clean(n.get("evidence"))
    return e


# ------------------------------------------------------------------ LLM calls
def schema(name: str = "candidate") -> dict:
    s = yaml.safe_load((HERE / "schemas" / f"{name}.yaml").read_text())
    s.pop("$schema", None)
    s.pop("title", None)
    return s


def api_schema(name: str = "candidate") -> dict:
    """The schema with keywords the structured-output endpoint may not enforce removed (checked locally)."""
    s = json.loads(json.dumps(schema(name)))

    def strip(o):
        if isinstance(o, dict):
            for k in ("minimum", "maximum", "minItems", "maxItems", "description"):
                o.pop(k, None)
            for v in o.values():
                strip(v)
        elif isinstance(o, list):
            for v in o:
                strip(v)
    strip(s)
    return s


def valid(obj, name: str = "candidate") -> bool:
    import jsonschema
    try:
        jsonschema.validate(obj, schema(name))
        return True
    except jsonschema.ValidationError:
        return False


def render(arm: str, case: Case, entry_text: str = "", literature: str = "") -> str:
    tmpl = (HERE / "prompts" / f"{'A2' if arm in ('A2', 'A5', 'A6', 'A7') else arm}.md").read_text()
    body = tmpl.split("-->", 1)[1].lstrip("\n")
    return body.format(DISPLAY_NAME=case.display, CUTOFF_YEAR=case.cutoff[:4], ENTRY=entry_text, LITERATURE=literature)


def call_cli(prompt: str, system: str, name: str = "candidate") -> dict | None:
    cfg = run_config()
    r = subprocess.run(["claude", "-p", prompt, "--model", cfg["models"]["primary"], "--system-prompt", system,
                        "--output-format", "json", "--json-schema", json.dumps(schema(name)), "--no-session-persistence",
                        "--disallowedTools", "WebSearch", "WebFetch", "Bash", "Read", "Grep", "Glob", "Write", "Edit"],
                       capture_output=True, text=True)
    try:
        res = json.loads(r.stdout)
        out = res.get("structured_output") or json.loads(res.get("result", ""))
        return out
    except (json.JSONDecodeError, TypeError, AttributeError):
        return None


def run_batch(requests: list[tuple[str, str]], system: str, split: str, name: str = "candidate") -> dict[str, dict | None]:
    """requests: (custom_id, user prompt). Message Batches API, cached system prompt, structured output."""
    import time

    import anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    cfg = run_config()
    client = anthropic.Anthropic()
    sys_blocks = [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}]
    out: dict[str, dict | None] = {}
    for start in range(0, len(requests), 10_000):
        chunk = requests[start:start + 10_000]
        batch = client.messages.batches.create(requests=[
            Request(custom_id=cid, params=MessageCreateParamsNonStreaming(
                model=cfg["models"]["primary"], max_tokens=16000, system=sys_blocks,
                output_config={"effort": cfg.get("effort", "high"),
                               "format": {"type": "json_schema", "schema": api_schema(name)}},
                messages=[{"role": "user", "content": prompt}])) for cid, prompt in chunk])
        (RUNS / split / "batches.log").parent.mkdir(parents=True, exist_ok=True)
        with open(RUNS / split / "batches.log", "a") as f:
            f.write(f"{batch.id}\t{len(chunk)}\n")
        while client.messages.batches.retrieve(batch.id).processing_status != "ended":
            time.sleep(60)
        for res in client.messages.batches.results(batch.id):
            if res.result.type == "succeeded":
                msg = res.result.message
                if msg.stop_reason == "refusal":
                    out[res.custom_id] = None
                    continue
                text = next((b.text for b in msg.content if b.type == "text"), "")
                try:
                    out[res.custom_id] = json.loads(text)
                except json.JSONDecodeError:
                    out[res.custom_id] = None
            else:
                out[res.custom_id] = None
    return out


def llm(requests: list[tuple[str, str]], split: str, workers: int, name: str = "candidate",
        system: str | None = None) -> dict[str, dict | None]:
    """Run requests, validate each output, retry only the invalid ones once."""
    if system is None:
        system = (HERE / "prompts" / "arm_system.md").read_text().split("-->", 1)[1].strip()
    api = bool(os.environ.get("ANTHROPIC_API_KEY"))
    log_deviation(split, "temperature 0 not set: claude-opus-5-5 accepts no sampling parameters "
                         f"({'Message Batches API' if api else 'claude -p'})")

    def go(reqs):
        if api:
            return run_batch(reqs, system, split, name)
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            return dict(zip([c for c, _ in reqs], ex.map(lambda r: call_cli(r[1], system, name), reqs)))
    res = go(requests)
    bad = [(c, p) for c, p in requests if not (res.get(c) is not None and valid(res[c], name))]
    if bad:
        res.update(go(bad))
        for c, _ in bad:
            if not (res.get(c) is not None and valid(res[c], name)):
                log_deviation(split, f"invalid output after one retry: {c}")
                res[c] = None
    return res


# ------------------------------------------------------------------ stage: arms
def a1_candidates(entry: dict, case: Case) -> dict:
    """A1 (graph only, no LLM): placeholder ranking until the A1 implementation is frozen with a1_config.yaml.
    Candidates are the entry's measurable nodes, scored per a1_config.yaml."""
    sys.path.insert(0, str(HERE / "coverage_audit"))
    import audit as cov  # noqa: E402
    cfg = yaml.safe_load((HERE / "a1_config.yaml").read_text())
    nodes = cov.measurable_nodes(entry) if hasattr(cov, "measurable_nodes") else []
    cands = []
    for rank, n in enumerate(nodes[: cfg["weights"]["k"]], 1):
        cands.append({"analyte": n, "analyte_type": "OTHER", "specimen": "other", "target": n, "mechanism": "",
                      "rationale": "A1 graph score", "confidence": 0.0, "rank": rank})
    return {"candidates": cands}


def stage_arms(plan: Plan, workers: int, arms: set[str]) -> None:
    cfg = run_config()
    reps, runs = range(1, cfg.get("curation_replicates", 2) + 1), range(1, cfg["runs_per_llm_arm"] + 1)
    reqs, dest = [], {}

    def want(path: Path, cid: str, prompt: str):
        if not path.exists():
            reqs.append((cid, prompt))
            dest[cid] = path

    base = RUNS / plan.split / "arms"
    for unit, cs in sorted(plan.units.items()):
        for rep in reps:
            entry = load_entry(plan.split, unit, rep)
            if entry is None:
                continue
            lit = cited_literature(entry, unit)
            etext = yaml.safe_dump(entry, sort_keys=False, allow_unicode=True)
            c0 = cs[0]
            if "A1" in arms:
                p = base / unit / f"r{rep}" / "A1.json"
                if not p.exists():
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(json.dumps(a1_candidates(entry, c0)))
            for run in runs:
                if "A2" in arms:
                    want(base / unit / f"r{rep}" / f"A2_run{run}.json", f"{unit}|r{rep}|A2|{run}", render("A2", c0, etext, lit))
                if "A3" in arms:
                    want(base / unit / f"r{rep}" / f"A3_run{run}.json", f"{unit}|r{rep}|A3|{run}", render("A3", c0, "", lit))
                if "A5" in arms:
                    for s in A5_SEEDS:
                        sp = base / unit / f"r{rep}" / f"A5_seed{s}_entry.yaml"
                        if not sp.exists():
                            sp.parent.mkdir(parents=True, exist_ok=True)
                            sp.write_text(yaml.safe_dump(scramble(entry, SEED + s), sort_keys=False, allow_unicode=True))
                        want(base / unit / f"r{rep}" / f"A5_seed{s}_run{run}.json", f"{unit}|r{rep}|A5s{s}|{run}",
                             render("A5", c0, sp.read_text(), lit))
            for c in cs:
                if c.negative:
                    continue
                if "A6" in arms:
                    tgt = t1_target_node(entry, c.rubric)
                    for lvl in A6_LEVELS:
                        ap = base / unit / f"r{rep}" / c.cid / f"A6_{lvl}_entry.yaml"
                        if tgt is None:
                            continue  # A6 is NA for this case and replicate
                        if not ap.exists():
                            ap.parent.mkdir(parents=True, exist_ok=True)
                            ap.write_text(yaml.safe_dump(ablate(entry, tgt, lvl, SEED), sort_keys=False, allow_unicode=True))
                        for run in runs:
                            want(base / unit / f"r{rep}" / c.cid / f"A6_{lvl}_run{run}.json",
                                 f"{unit}|r{rep}|{c.cid}|A6_{lvl}|{run}", render("A6", c, ap.read_text(), lit))
    for c in plan.cases:
        if "A7" in arms:
            ap = base / "A7" / c.cid / "entry.yaml"
            if not ap.exists():
                ap.parent.mkdir(parents=True, exist_ok=True)
                ap.write_text(yaml.safe_dump(a7_entry(c), sort_keys=False, allow_unicode=True))
            for rep in reps:
                for run in runs:
                    want(base / "A7" / c.cid / f"r{rep}_run{run}.json", f"A7|{c.cid}|r{rep}|{run}",
                         render("A7", c, ap.read_text(), ""))
    for (disp, year), cs in sorted(plan.a4_units.items()):
        key = hashlib.sha1(f"{disp}|{year}".encode()).hexdigest()[:10]
        if "A4" in arms:
            for rep in reps:
                for run in runs:
                    want(base / "A4" / key / f"r{rep}_run{run}.json", f"A4|{key}|r{rep}|{run}", render("A4", cs[0]))
    for disp, cs in sorted(plan.probe_units.items()):
        if "probe" in arms:
            key = hashlib.sha1(disp.encode()).hexdigest()[:10]
            body = (HERE / "prompts" / "probe.md").read_text().split("-->", 1)[1].lstrip("\n")
            want(base / "probe" / key / "run1.json", f"probe|{key}", body.format(DISPLAY_NAME=disp))
    if not reqs:
        return
    res = llm(reqs, plan.split, workers)
    for cid, path in dest.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(res.get(cid) if res.get(cid) is not None else {"candidates": [], "invalid": True}))


# ------------------------------------------------------------------ stage: scoring, analysis, findings
def stage_scoring(plan: Plan) -> None:
    """Match every arm output against every case that uses it; write scored.jsonl, the adjudication
    queue and the blinded human sample (20%, or all if fewer than 50, seed SEED)."""
    sys.path.insert(0, str(HERE))
    import match
    base, rows = RUNS / plan.split / "arms", []
    for unit, cs in plan.units.items():
        for f in sorted((base / unit).rglob("*.json")):
            parts = f.relative_to(base / unit).parts
            rep = int(parts[0][1:])
            arm = parts[-1].split("_")[0].split(".")[0]
            run = int(re.search(r"run(\d+)", parts[-1]).group(1)) if "run" in parts[-1] else 1
            cands = json.loads(f.read_text()).get("candidates", [])
            for c in cs:
                if len(parts) == 3 and parts[1] != c.cid:
                    continue  # a per-case output (A6) belongs to its own case only
                for s in match.score(c.rubric, cands):
                    rows.append({"case_id" if not c.negative else "negative_id": c.cid, "arm": arm, "replicate": rep,
                                 "run": run, **s, "source": str(f.relative_to(RUNS))})
    out = RUNS / plan.split / "scoring"
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "scored_auto.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    pool = [i for i, r in enumerate(rows) if r.get("case_id")]
    rng = random.Random(SEED)
    sample = sorted(pool if len(pool) < 50 else rng.sample(pool, round(0.2 * len(pool))))
    blind = {i: hashlib.sha1(f"{SEED}|{i}".encode()).hexdigest()[:12] for i in sample}
    with open(out / "human_sample_blinded.tsv", "w") as f:
        f.write("item\tcase_id\tanalyte\tanalyte_type\tspecimen\ttarget\tT1\tT2\tT3\tT4\tadjudicator\tnotes\n")
        for i in sample:
            r = rows[i]
            f.write(f"{blind[i]}\t{r['case_id']}\t{r['analyte']}\t{r['analyte_type']}\t{r['specimen']}\t{r['target']}"
                    "\t\t\t\t\t\t\n")
    (out / "human_sample_key.json").write_text(json.dumps({blind[i]: rows[i]["source"] for i in sample}))
    print(f"scored {len(rows)} candidates; human sample {len(sample)}")


def stage_adjudication(plan: Plan, workers: int) -> None:
    """LLM adjudication of T1, T3 and CLINICAL_T1_ONLY: one fresh call per (case, arm output), blind to the
    arm; merged with the automatic tiers into scored_final.jsonl."""
    sys.path.insert(0, str(HERE))
    import match
    out = RUNS / plan.split / "scoring"
    rows = [json.loads(l) for l in (out / "scored_auto.jsonl").read_text().splitlines() if l.strip()]
    rubrics = {c.cid: c.rubric for c in plan.cases}
    groups = defaultdict(list)
    for i, r in enumerate(rows):
        if r.get("case_id") and r["needs_adjudication"]:
            groups[(r["case_id"], r["source"])].append(i)
    tmpl = (HERE / "prompts" / "adjudicate.md").read_text().split("-->", 1)[1].lstrip("\n")
    store = out / "adjudication.json"
    have = json.loads(store.read_text()) if store.exists() else {}
    reqs = []
    for (cid, src), idx in sorted(groups.items()):
        key = hashlib.sha1(f"{cid}|{src}".encode()).hexdigest()[:16]
        if key in have:
            continue
        rb = rubrics[cid]
        cands = "\n".join(f"{n}: {rows[i]['analyte']} | {rows[i]['analyte_type']} | {rows[i]['specimen']} | "
                          f"{rows[i]['target']}" for n, i in enumerate(idx))
        reqs.append((key, tmpl.format(
            RUBRIC_T1=f"{rb['T1']['mechanism_class']} ({rb['T1']['mechanism_class_definition']}); "
                      f"{rb['T1']['process']['label']} ({rb['T1']['process']['id']})",
            RUBRIC_T3=rb["T3"]["discovery_experiment"],
            CLINICAL_T1_ONLY="; ".join(rb["T1"].get("t1_only_in_clinical_use") or []) or "none",
            CANDIDATES=cands)))
        have.setdefault("_index", {})[key] = idx
    if reqs:
        res = llm(reqs, plan.split, workers, name="adjudication",
                  system="You adjudicate candidate diagnostic tests against a rubric. Return only the JSON the schema asks for.")
        for k, v in res.items():
            have[k] = v
        store.write_text(json.dumps(have))
    for key, idx in have.get("_index", {}).items():
        verdicts = {v["index"]: v for v in ((have.get(key) or {}).get("verdicts") or [])}
        for n, i in enumerate(idx):
            v = verdicts.get(n)
            rows[i]["adjudicated"] = v is not None
            rows[i]["tier"] = match.final_tier(rows[i], v)
    for r in rows:
        if not r.get("needs_adjudication"):
            r["adjudicated"] = True
            r["tier"] = r.get("tier_auto", "none")
    with open(out / "scored_final.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def stage_analysis(plan: Plan) -> None:
    out = RUNS / plan.split / "analysis"
    out.mkdir(parents=True, exist_ok=True)
    cases = {c.cid: {"test_group": c.rubric.get("test_group", c.cid), "cutoff_date": c.cutoff, "negative": c.negative,
                     "packet_size": c.packet_size, "h3_usable": c.rubric.get("h3_usable")} for c in plan.cases}
    cases["_human_sample_complete"] = False
    (out / "cases.json").write_text(json.dumps(cases, indent=1))
    scored = RUNS / plan.split / "scoring" / "scored_final.jsonl"
    if not scored.exists():
        print("analysis: no scored_final.jsonl yet (adjudication not merged); nothing computed")
        return
    subprocess.run([sys.executable, str(HERE / "analysis.py"), str(scored), str(out / "cases.json"), "--out",
                    str(out / "metrics.json")], check=True)


def stage_findings(plan: Plan) -> None:
    m = RUNS / plan.split / "analysis" / "metrics.json"
    if not m.exists():
        return
    d = json.loads(m.read_text())
    lines = [f"# Findings draft ({plan.split}, {d['status']})", "",
             "Every number below is PROVISIONAL until human adjudication is complete." if d["status"] != "FINAL" else "", ""]
    for name, c in d.get("comparisons", {}).items():
        lines.append(f"- **{name}:** {c['rate_a']} vs {c['rate_b']} (n={c['n_cases']}); discordant {c['discordant_b']}:"
                     f"{c['discordant_c']}; exact McNemar p={c['mcnemar_p']:.3g}; paired difference "
                     f"{c['paired_difference']:.3f}, 95% CI {c['paired_difference_ci95']}")
    (RUNS / plan.split / "FINDINGS_draft.md").write_text("\n".join(lines) + "\n")


# ------------------------------------------------------------------ main
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--split", choices=("dev", "test"), required=True)
    ap.add_argument("--stages", default=",".join(STAGES))
    ap.add_argument("--arms", default="A1,A2,A3,A4,A5,A6,A7,probe")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--max-calls", type=int, default=0, help="stop if the estimated LLM call count exceeds this")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--confirm-heldout", default="")
    a = ap.parse_args()
    plan = load_plan(a.split)
    cfg = run_config()
    api = bool(os.environ.get("ANTHROPIC_API_KEY"))
    after, before = count_calls(plan, True, cfg), count_calls(plan, False, cfg)
    if a.dry_run:
        report = {"split": a.split, "cases": sum(not c.negative for c in plan.cases),
                  "negatives": sum(c.negative for c in plan.cases),
                  "shared_units": {u: [c.cid for c in cs] for u, cs in plan.units.items() if len(cs) > 1},
                  "before_dedupe": before, "after_dedupe": after,
                  "estimate_after_dedupe": estimate(plan, after, api, a.workers),
                  "estimate_before_dedupe": estimate(plan, before, api, a.workers),
                  "llm_path": "Message Batches API" if api else f"claude -p, {a.workers} workers"}
        print(json.dumps(report, indent=2))
        return
    if a.split == "test" and a.confirm_heldout != HELDOUT_PHRASE:
        sys.exit(f"held-out split: pass --confirm-heldout {HELDOUT_PHRASE} (only after preregistration)")
    stages = [s for s in a.stages.split(",") if s]
    planned = after["llm_calls_excluding_curation"] if "arms" in stages else 0
    planned += after["curation_sessions_with_all_retries"] if "curation" in stages else 0
    if a.max_calls and planned > a.max_calls:
        sys.exit(f"estimated {planned} LLM calls exceed --max-calls {a.max_calls}; stopping")
    print(f"estimated LLM calls for stages {stages}: {planned}")
    if not api:
        log_deviation(a.split, "no ANTHROPIC_API_KEY: arms run through claude -p (no batch discount, no explicit "
                               "prompt caching; temperature not settable)")
    for s in stages:
        if s == "packets":
            stage_packets(plan)
        elif s == "curation":
            stage_curation(plan, a.workers)
        elif s == "arms":
            stage_arms(plan, a.workers, set(a.arms.split(",")))
        elif s == "scoring":
            stage_scoring(plan)
            stage_adjudication(plan, a.workers)
        elif s == "analysis":
            stage_analysis(plan)
        elif s == "findings":
            stage_findings(plan)


if __name__ == "__main__":
    main()
