---
name: claim-disease
description: Use when claiming the next high-priority uncurated disease from the dismech priority dashboard. Picks the top-ranked disease in dashboard/priority.json that is not already covered in kb/disorders/, opens a GitHub curation issue, and assigns it to the current GitHub user. Accepts an optional integer 1–8 to claim N diseases at once.
---

# claim-disease

Claim the next high-priority uncurated disease(s) from the dismech priority dashboard. Opens GitHub issues and assigns them to whoever is running the skill.

## When to use

- "What should I curate next?"
- "Claim the next disease"
- "Pick me the next 3 priority diseases and open issues"

Skip when:
- The user names a specific disease — just open that issue directly, no priority lookup needed.
- `dashboard/priority.json` is missing or stale — regenerate it first with `just gen-dashboard`.

## Inputs

- Optional positional argument **N**: number of diseases to claim. Defaults to **1**, maximum **8**.
- Invoked as `/claim-disease` (claims 1) or `/claim-disease 3` (claims 3). The number, if present, is the only argument and must be a positive integer between 1 and 8 inclusive. The cap exists because filing many issues at once swamps the curation queue and generates more cleanup than throughput.

## Workflow

1. **Read N from the user's argument.** If the user passed an integer, use it. If no argument, default to 1. `N` is the target number of issues to file and is used in steps 4 and 6. If the argument is non-integer, `<= 0`, or `> 8`, stop and ask the user to clarify rather than guess. Never silently cap a request for `N > 8` to 8 — the user may be picking diseases for batch handoff and needs to know the limit was hit.
2. **Verify priority data is fresh.** If `dashboard/priority.json` is older than 30 days or missing, ask the user whether to regenerate (`just gen-dashboard`) before continuing. Do not silently use stale data.
3. **Resolve the current GitHub user**: `gh api user -q .login`. Use that as the issue assignee.
4. **Run the candidate finder** (Python snippet below) with `LIMIT = N + 50` so there is headroom for candidates that get skipped. The finder reads `dashboard/priority.json`, builds the set of already-covered MONDO IDs from every YAML in `kb/disorders/`, and prints the top `LIMIT` uncovered candidates that have an actionable recommendation (`CURATE_ROOT` or `CURATE_ROOT_WITH_SUBTYPES`). Skips `LUMP_INTO_PARENT`, `REVIEW_AGAINST_PARENT`, `DROP_GROUPING_TERM`. Treat the output as an ordered **candidate pool**.
5. **Run duplicate preflight for the candidate pool.** The
   candidate finder covers the local knowledgebase, but each candidate must also
   be checked against the most recent upstream knowledgebase plus all PRs and
   issues before filing a new issue.
   ```bash
   git fetch origin main

   # Confirm the candidate is still absent from the latest upstream KB.
   git grep -n -i -e "<MONDO_ID>" -e "<label>" origin/main -- kb/disorders || true

   # Check PRs and issues across all states; repeat for important synonyms.
   gh pr list --repo monarch-initiative/dismech --state all \
     --search "\"<MONDO_ID>\" OR \"<label>\"" \
     --json number,title,state,url,headRefName --limit 100
   gh issue list --repo monarch-initiative/dismech --state all \
     --search "\"<MONDO_ID>\" OR \"<label>\"" \
     --json number,title,state,url,labels --limit 100
   ```
   Discard any candidate whose MONDO ID, label, or important synonym appears in
   the latest KB, an existing PR, or an existing issue unless the user confirms
   it is genuinely distinct.
6. **Iterate the pool top-down and claim until you have N successful claims** (or the pool is exhausted):
   - Skip any candidate flagged `possibly_covered_by` unless the user has already confirmed it is genuinely uncurated.
   - For each remaining candidate, open one issue with the template below. Labels: `curation,enhancement`. Assignee: the GitHub user from step 3.
   - Stop as soon as you have filed N issues. If the pool runs out before you reach N, report the shortfall and offer to re-run the finder with a larger `LIMIT`.
7. **Report** the URLs of every issue filed, plus a short list of candidates that were skipped and why (already in KB / already has PR or issue / `possibly_covered_by` / not actionable).

## Candidate finder

Run this from the repo root. Pass `LIMIT` as the first argument — this is **not** the number of issues to file, it is the size of the candidate pool to draw from. Use `LIMIT = N + 50` so there is headroom for candidates that get skipped (already-claimed, `possibly_covered_by`). The finder filters by MONDO ID, by canonical label, and by synonym list — and additionally surfaces any candidates whose label appears as a substring in an existing entry's label/synonyms (these are flagged as `possibly_covered` and should be reviewed by hand, not auto-claimed).

```bash
LIMIT=${1:-51} python3 - <<'PY'
import json, os, glob, yaml, re

n = int(os.environ.get("LIMIT", "51"))

def norm(s):
    return re.sub(r"\s+", " ", s.lower().strip()) if s else ""

covered_ids = set()
covered_labels = set()        # exact normalized labels + synonyms
covered_label_corpus = []     # for substring fallback (list of (norm_label, kb_file))

for path in glob.glob("kb/disorders/*.yaml"):
    try:
        with open(path) as fh:
            d = yaml.safe_load(fh)
    except Exception:
        continue
    if not isinstance(d, dict):
        continue
    dt = (d.get("disease_term") or {}).get("term") or {}
    if dt.get("id"):
        covered_ids.add(dt["id"])
    for m in (d.get("mappings") or {}).get("mondo_mappings") or []:
        tid = ((m or {}).get("term") or {}).get("id")
        if tid:
            covered_ids.add(tid)
    for sub in d.get("has_subtypes") or []:
        st = ((sub or {}).get("disease_term") or {}).get("term") or {}
        if st.get("id"):
            covered_ids.add(st["id"])
    # labels & synonyms for fuzzy matching
    for s in filter(None, [d.get("name"), dt.get("label"), (d.get("disease_term") or {}).get("preferred_term")]):
        covered_labels.add(norm(s))
        covered_label_corpus.append((norm(s), path))
    for syn in d.get("synonyms") or []:
        if isinstance(syn, str):
            covered_labels.add(norm(syn))
            covered_label_corpus.append((norm(syn), path))
        elif isinstance(syn, dict) and syn.get("name"):
            covered_labels.add(norm(syn["name"]))
            covered_label_corpus.append((norm(syn["name"]), path))

try:
    with open("dashboard/priority.json") as fh:
        priority = json.load(fh)
except FileNotFoundError:
    raise SystemExit(
        "dashboard/priority.json not found — run `just gen-dashboard` first"
    )
actionable = {"CURATE_ROOT", "CURATE_ROOT_WITH_SUBTYPES"}
picks = []
for row in priority["rows"]:
    if row.get("recommended_action") not in actionable:
        continue
    if row["mondo_id"] in covered_ids:
        continue
    label_n = norm(row["label"])
    if label_n in covered_labels:
        continue
    # substring fallback: both labels must be multi-word and >=8 chars to avoid noise
    possibly = []
    if len(label_n.split()) >= 2 and len(label_n) >= 8:
        for cn, src in covered_label_corpus:
            if len(cn.split()) < 2 or len(cn) < 8:
                continue
            if label_n in cn or cn in label_n:
                possibly.append(src)
    pick = {
        "mondo_id": row["mondo_id"],
        "label": row["label"],
        "score": row["score"],
        "recommended_action": row["recommended_action"],
    }
    if possibly:
        pick["possibly_covered_by"] = sorted(set(possibly))[:3]
    picks.append(pick)
    if len(picks) >= n:
        break

print(json.dumps(picks, indent=2))
PY
```

If a candidate has `possibly_covered_by`, **do not auto-claim it** — show the user, confirm whether the existing entry already covers it, and skip if so. Only claim candidates with no `possibly_covered_by` flag without confirmation.

## Issue template

Title:

```
Curate <label> (<MONDO_ID>)
```

Body:

```markdown
Curate a dismech entry for **<label>** ([<MONDO_ID>](https://monarchinitiative.org/<MONDO_ID>)) — <one-sentence biomedical context>.

<If recommended_action is CURATE_ROOT_WITH_SUBTYPES, add a paragraph noting that subtypes should be modelled with `has_subtypes`. Mention any obvious subtypes you know of, or note that they should be identified during curation.>

Source: top of [priority dashboard](https://dismech.monarchinitiative.org/dashboard/priority.html) (`<recommended_action>`, score <score>).

Tracker: part of #1079.
```

Create with:

```bash
gh issue create \
  --title "Curate <label> (<MONDO_ID>)" \
  --assignee "$(gh api user -q .login)" \
  --label curation,enhancement \
  --body "$(cat <<'EOF'
...body...
EOF
)"
```

## Common mistakes

- **Hardcoding a username.** Always resolve via `gh api user -q .login` so the skill works for any contributor.
- **Fetching priority.html from the deployed site.** Use the local `dashboard/priority.json` — it's authoritative and structured.
- **Claiming a disease that already has a KB entry, PR, or issue.** Always run
  the duplicate preflight against `origin/main`, all PRs, and all issues before
  posting. Open and closed GitHub records both matter because a closed PR may
  already be merged into a newer main, and a closed issue may explain why a
  superficially similar target should not be curated separately.
- **Including non-actionable rows.** `LUMP_INTO_PARENT` and `DROP_GROUPING_TERM` should not become curation issues; the candidate finder above already filters them.
- **Stale dashboard.** If `dashboard/priority.json` is more than ~30 days old, the ranking may not reflect recent kb additions. Offer to regenerate before claiming.
- **Trusting the finder blindly.** Coverage detection is lexical (MONDO ID, label, synonym, substring). Diseases covered conceptually under a different parent term will pass through (e.g. "Zellweger spectrum disorders" → covered by `Peroxisome_Biogenesis_Disorder.yaml` but no shared MONDO ID or substring). When the candidate label ends in "syndrome", "disorder", "spectrum", "disease" or is a well-known synonym, search the kb manually before posting:
   ```bash
   grep -rli "zellweger" kb/disorders/
   ```
- **Filing fewer issues than requested without saying so.** The candidate pool is `LIMIT = N + 50`, but on a busy day even that can be exhausted by already-filed issues. If you finish step 6 with fewer than N claims, say so explicitly in the report and offer to re-run the finder with a larger `LIMIT`. Don't pad the count with `possibly_covered_by` candidates the user hasn't confirmed.
- **Confusing `LIMIT` with `N`.** `LIMIT` is the candidate-pool size passed to the finder. `N` is how many issues to actually file. They are not the same number; never pass `N` directly as the finder's argument.

## Tracker

The umbrella issue for priority curation is **#1079**. Always link new curation issues back to it.
