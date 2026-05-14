---
name: claim-disease
description: Use when claiming the next high-priority uncurated disease from the dismech priority dashboard. Picks the top-ranked disease in dashboard/priority.json that is not already covered in kb/disorders/, opens a GitHub curation issue, and assigns it to the current GitHub user. Accepts an optional integer to claim N diseases at once.
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

- Optional positional argument: number of diseases to claim. Defaults to **1**.

## Workflow

1. **Verify priority data is fresh.** If `dashboard/priority.json` is older than 30 days or missing, ask the user whether to regenerate (`just gen-dashboard`) before continuing. Do not silently use stale data.
2. **Resolve the current GitHub user**: `gh api user -q .login`. Use that as the issue assignee.
3. **Run the candidate finder** (Python snippet below). It reads `dashboard/priority.json`, builds the set of already-covered MONDO IDs from every YAML in `kb/disorders/`, and prints the top N uncovered candidates that have an actionable recommendation (`CURATE_ROOT` or `CURATE_ROOT_WITH_SUBTYPES`). Skips `LUMP_INTO_PARENT`, `REVIEW_AGAINST_PARENT`, `DROP_GROUPING_TERM`.
4. **Check for existing open issues** for each candidate before posting — search by MONDO ID:
   ```bash
   gh issue list --state open --search "MONDO:0100249 in:title,body" --json number,title
   ```
   If a match exists, skip that candidate, log it, and pick the next one from the finder output.
5. **Open one issue per candidate** with the template below. Labels: `curation,enhancement`. Assignee: the GitHub user from step 2.
6. **Report** issue URLs to the user, plus any candidates that were skipped (already covered, already has an open issue).

## Candidate finder

Run this from the repo root. Pass N as the first argument. The finder filters by MONDO ID, by canonical label, and by synonym list — and additionally surfaces any candidates whose label appears as a substring in an existing entry's label/synonyms (these are flagged as `possibly_covered` and should be reviewed by hand, not auto-claimed).

```bash
N=${1:-1} python3 - <<'PY'
import json, os, glob, yaml, re

n = int(os.environ.get("N", "1"))

def norm(s):
    return re.sub(r"\s+", " ", s.lower().strip()) if s else ""

covered_ids = set()
covered_labels = set()        # exact normalized labels + synonyms
covered_label_corpus = []     # for substring fallback (list of (norm_label, kb_file))

for path in glob.glob("kb/disorders/*.yaml"):
    try:
        d = yaml.safe_load(open(path))
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

priority = json.load(open("dashboard/priority.json"))
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
- **Claiming a disease that already has an open issue.** Always run the `gh issue list --search "MONDO:..."` check before posting.
- **Including non-actionable rows.** `LUMP_INTO_PARENT` and `DROP_GROUPING_TERM` should not become curation issues; the candidate finder above already filters them.
- **Stale dashboard.** If `dashboard/priority.json` is more than ~30 days old, the ranking may not reflect recent kb additions. Offer to regenerate before claiming.
- **Trusting the finder blindly.** Coverage detection is lexical (MONDO ID, label, synonym, substring). Diseases covered conceptually under a different parent term will pass through (e.g. "Zellweger spectrum disorders" → covered by `Peroxisome_Biogenesis_Disorder.yaml` but no shared MONDO ID or substring). When the candidate label ends in "syndrome", "disorder", "spectrum", "disease" or is a well-known synonym, search the kb manually before posting:
   ```bash
   grep -rli "zellweger" kb/disorders/
   ```

## Tracker

The umbrella issue for priority curation is **#1079**. Always link new curation issues back to it.
