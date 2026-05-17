---
name: initiate-new-disorder-creation
description: >
  Skill for initiating new disorder YAML files in the dismech knowledge base.
  Use this skill when the user asks to create a new disorder entry. Also useful
  for enhancing existing entries.
---

# Initiate New Disorder Creation Skill

## Overview

Guide the creation of new disorder YAML files in the dismech knowledge base. This skill
emphasizes a **research-first approach** to ensure scientific accuracy and prevent
AI hallucinations by requiring deep research queries before file creation.

## When to Use

- User asks to create a new disorder/disease entry
- User names a disorder that doesn't exist in `kb/disorders/`

This skill can also be consulted for ongoing curation of existing disorders.

## Workflow

### Step 1: Select Disorder Name and Verify Disorder Doesn't Exist

Choose the clinically preferred name for the disorder, use title case (e.g. `Foo Bar Syndrome`).
For file names, spaces will. be replaced by underscores, and characters such as apostrophes removed.

```bash
ls kb/disorders/*yaml
```
If it exists, edit the existing file instead of creating a new one.

### Step 2a: Setup git worktree

The preferred mode of working is to use git worktrees, unless the user has expressed
a preference not to do this in advance.

### Step 2b: Create initial YAML file

Create an initial yaml file using the underscore form of the disease, e.g.

kb/disorders/Foo_Bar.yaml:
```yaml
name: Foo Bar
creation_date: "2025-06-12T20:16:27Z"
updated_date: "2025-06-12T20:16:27Z"
category: Complex
disease_term:
  term:
    id: MONDO:nnnnnnn
    label: foo bar  ## mondo name will follow OBO case conventions
parents:
  <yaml list of strings>
has_subtypes:
  <optional yaml list of Subtype objects>
pathophysiology:
  <yaml list of Pathophysiology objects>
phenotypes:
  <yaml list of Phenotype objects>
biochemical:
  <optional yaml list of Biochemical objects>
genetic:
  <optional yaml list of Genetic objects>
environmental:
  <optional yaml list of Environmental objects>
treatments:
  <optional yaml list of Treatment objects>
datasets:
```

`creation_date` and `updated_date` must be ISO 8601/RFC 3339 datetime strings.
When editing an existing file, preserve `creation_date` and bump `updated_date`.

The objects must follow the LinkML schema in src/dismech/schema.

It can be validated with `just validate kb/disorders/Foo_Bar.yaml`

This first pass should use textbook knowledge about the disease: you will later refine this.

### Step 3: Perform Deep Research (REQUIRED)

Execute at least one deep research query. Always do this via the `just` command, do
not perform your own deep research.

Depending on user preference, use one or more of the following commands

- `just research-disorder asta DISORDER_NAME`
- `just research-disorder perplexity DISORDER_NAME`
- `just research-disorder falcon DISORDER_NAME`
- `just research-disorder openai DISORDER_NAME`
- `just research-disorder cyberian DISORDER_NAME`
- `just research-disorder openscientist DISORDER_NAME`

Use the filesystem-friendly name here.

`falcon` requires `EDISON_API_KEY` to be exported in the environment.  Edison
(formerly FutureHouse Falcon) is a large-scale literature agent that performs
deep bibliographic research.  `falcon` runs may take 20 minutes or longer.
In addition to the narrative report, Edison runs frequently produce **artifacts**
— structured tables, figures, or supplementary documents — that summarise key
findings in machine-readable form.  When `EDISON_API_KEY` is set, artifact
retrieval happens automatically at the end of `just research-disorder falcon …`.
Artifacts are written to a sub-directory alongside the report:

    research/DISORDER_NAME-deep-research-falcon_artifacts/

The report's YAML frontmatter records the `trajectory_id` used to retrieve them
and lists each artifact under the `artifacts` key.  An `## Artifacts` section
is inserted into the report body for any image artifacts so they render in
Markdown viewers.  If artifact retrieval was skipped (e.g. `EDISON_API_KEY` was
not set at the time), you can run it later with:

    just fetch-research-artifacts <trajectory_id> research/DISORDER_NAME-deep-research-falcon.md

`asta` requires `ASTA_API_KEY` to be exported in the environment. Asta behaves
more like a literature search agent than a full narrative deep-research agent:
its outputs are primarily lists of relevant papers, usually with summaries,
evidence snippets, and relevance scores. The `just research-disorder asta ...`
command automatically uses an Asta-specific template tailored for this output
style.

`openscientist` requires `OPENSCIENTIST_API_KEY` to be exported in the
environment. OpenScientist (https://www.openscientist.io) is an autonomous AI
research agent from Berkeley Lab that runs iterative hypothesis-driven research
using PubMed search and code execution. It produces markdown reports with PMID
citations. To set up:

1. Sign up at https://www.openscientist.io
2. Wait for admin approval (required before jobs can run)
3. Generate an API key (shown once in `name:secret` format)
4. `export OPENSCIENTIST_API_KEY="name:secret"`

OpenScientist jobs are asynchronous — the provider submits a job, then polls
until completion. Jobs are queued server-side and processed sequentially, so
wait times depend on queue depth. The API's `/report` endpoint returns PDF;
the provider automatically extracts the markdown `final_report.md` from the
`/artifacts` ZIP. The artifacts ZIP also contains provenance data (iteration
transcripts, generated plots as PNG/JSON) and agent logs.

Timing varies by provider. As a rule of thumb:

- `asta` usually completes in seconds
- `openai` and `perplexity` usually complete within a few minutes
- `falcon` may take 20 minutes or longer
- `cyberian` runtime varies with workflow complexity and can also be long-running
- `openscientist` typically takes 10–30 minutes depending on queue depth and iteration count

On completion, this will create a file here:

`./research/DISORDER_NAME-deep-research-PROVIDER.md`

and a separate citations file here:

`./research/DISORDER_NAME-deep-research-PROVIDER.md.citations.md`

For Edison (falcon) runs, artifacts (figures, structured tables, etc.) are also
saved in:

`./research/DISORDER_NAME-deep-research-falcon_artifacts/`

and referenced in the report's YAML frontmatter under the `artifacts` key.

For example:

- `research/Urticaria-deep-research-openai.md`
- `research/Urticaria-deep-research-openai.md.citations.md`
- `research/Urticaria-deep-research-falcon_artifacts/` *(falcon only)*

You MUST read this before progressing.

### Step 3b: GeneReviews Baseline (REQUIRED when applicable)

GeneReviews (https://www.ncbi.nlm.nih.gov/books/NBK1116/) is the authoritative
expert-curated clinical reference for Mendelian disorders. Before curating
phenotypes, you MUST check whether a GeneReviews article exists for the disease.
If one exists, it is the mandatory phenotype baseline — not just a convenient
source.

#### 1. Search PubMed for a GeneReviews article

```bash
curl -sG "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi" \
  --data-urlencode "db=pubmed" \
  --data-urlencode "retmode=json" \
  --data-urlencode "term=<DISEASE_NAME>[TI] GeneReviews[TI]"
```

If no results, try a broader search: `<DISEASE_NAME> GeneReviews[Book]`

#### 2. If a PMID is found, fetch and cache it

```bash
just fetch-reference PMID:XXXXXXXX
```

#### 3. Tag it in the top-level `references:` block

```yaml
references:
  - reference: PMID:XXXXXXXX
    title: "<GeneReviews article title>"
    tags:
      - GeneReviews
```

You can also run `just tag-references` after adding the PMID to inline
evidence items — the script detects GeneReviews PMIDs from the cached
abstract and writes the top-level tag automatically.

#### 4. Cross-reference Clinical Characteristics against your YAML

- Read the cached abstract at `references_cache/PMID_XXXXXXXX.md`
- Identify every phenotype, anomaly, and comorbidity listed in the
  Clinical Characteristics section of the abstract
- Compare against your YAML `phenotypes:` section
- Any GeneReviews-documented phenotype **absent** from your YAML must
  either be added (with an HPO term and evidence item quoting the
  GeneReviews abstract) or explicitly explained as out of scope

#### 5. Capture drug-safety warnings

GeneReviews often has an *Agents/Circumstances to Avoid* section.
If the abstract mentions any, add a note in the relevant treatment entry's
`description:` and include a GeneReviews evidence item quoting it exactly.

#### 6. Frequency mapping — prose → FrequencyEnum

GeneReviews uses narrative frequency language. Map to the enum as follows:

| GeneReviews phrase | FrequencyEnum | HPO range |
|---|---|---|
| "virtually all", "most individuals", ">80%" | `VERY_FREQUENT` | 80–100% |
| "many", "majority", "common", "~50%–79%", ">30%" | `FREQUENT` | 30–79% |
| "some", "occasional", "uncommon", "~10%–29%" | `OCCASIONAL` | 5–29% |
| "rare", "few", "<5%", "infrequently reported" | `VERY_RARE` | 1–4% |
| "isolated reports", "single case" | (omit frequency) | <1% |

When frequency is ambiguous, **omit `frequency:`** rather than guessing.

#### 7. No GeneReviews article? Document it

If no GeneReviews article exists for the disease, proceed to Step 4
without this baseline. No action needed — the absence itself is not a
problem.

---

### Step 4: Enhance YAML file with evidence for assestions

Use the results of deep research to enhance the yaml file, providing evidence for as many assertions as possible.

Find the pubmed IDs or DOIs for the papers in the deep research and retrieve these:

- `just fetch-reference PMID:nnnnnnn`
- `just fetch-reference DOI:...`

The `just fetch-reference` command can accept multiple identifiers of different types, such as:

- `just fetch-reference PMID:nnnnnnn DOI:nn.nnnn`

You can also find additional references relevant to individual assertions, on top of what is in the deep research.

#### Including Images from Deep Research Artifacts

When an Edison (falcon) run produces artifacts, check whether any images in the
artifact directory directly support a specific evidence claim you are curating.
If so, include the image path in the `images` slot on the evidence item.

**CRITICAL relevance rule:** Only include an image if it **directly illustrates
the specific claim** made in that evidence item.  Do NOT include images for
general background, unrelated figures, or mere "this might be interesting"
reasons.  Every listed image must be clearly connected to the snippet or
explanation it accompanies.

To check available artifacts for a falcon report:
```bash
ls research/DISORDER_NAME-deep-research-falcon_artifacts/
```

The `images` slot is a list of paths **relative to the `research/` directory**:

```yaml
evidence:
  - reference: PMID:35533128
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "Exactly quoted text from the abstract..."
    explanation: "Why this supports the claim."
    images:
      - Dimethylglycine_Dehydrogenase_Deficiency-deep-research-falcon_artifacts/figure-01.png
```

Multiple images per evidence item are allowed when each is distinctly relevant:

```yaml
evidence:
  - reference: PMID:35533128
    supports: SUPPORT
    snippet: "..."
    images:
      - MyDisorder-deep-research-falcon_artifacts/pathway-diagram.png
      - MyDisorder-deep-research-falcon_artifacts/clinical-data-table.png
```

**Do not invent image paths.** Only reference files that actually exist in the
artifact directory and have been committed to the repository.  Non-image
artifacts (e.g., `.md` tables, `.json` data) should generally not be listed
under `images`; they are already linked in the report's `## Artifacts` section.

#### Finding Additional References

Use PubMed first whenever possible. Use Semantic Scholar as a backup discovery
tool if PubMed search is not finding the paper you want.

##### Search the PubMed API

Use the NCBI E-utilities API to search PubMed directly. A typical workflow is:

1. Search for candidate papers with `esearch`
2. Inspect metadata with `esummary`
3. Retrieve the abstract text with `efetch` if needed
3. Cache the paper locally with `just fetch-reference`

Example search:

```bash
curl -sG "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi" \
  --data-urlencode "db=pubmed" \
  --data-urlencode "retmode=json" \
  --data-urlencode "term=<SEARCH_TERMS>"
```

Example summary lookup once you have one or more PMIDs:

```bash
curl -sG "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi" \
  --data-urlencode "db=pubmed" \
  --data-urlencode "retmode=json" \
  --data-urlencode "id=<PMID1>,<PMID2>"
```

Example abstract fetch:

```bash
curl -sG "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi" \
  --data-urlencode "db=pubmed" \
  --data-urlencode "id=<PMID>" \
  --data-urlencode "rettype=abstract" \
  --data-urlencode "retmode=text"
```

Once you identify the paper you want, cache it with:

```bash
just fetch-reference PMID:nnnnnnn
```

##### Search the Semantic Scholar API as a backup

If PubMed search is sparse or the deep research output only gives you a title,
DOI, or Semantic Scholar paper ID, use the Semantic Scholar API to find the
paper and recover identifiers.

Important: the Semantic Scholar search endpoint may return `429 Too
Many Requests` without an API key, even for simple queries. If you have a
Semantic Scholar API key, include it as an `x-api-key` header. If you do not,
use Semantic Scholar as a secondary/manual fallback rather than your primary
search method.

Example paper search (often requires an API key):

```bash
curl -sG "https://api.semanticscholar.org/graph/v1/paper/search" \
  -H "x-api-key: <SEMANTIC_SCHOLAR_API_KEY>" \
  --data-urlencode "query=<SEARCH_TERMS>" \
  --data-urlencode "limit=10" \
  --data-urlencode "fields=title,year,externalIds,url"
```

Example lookup by Semantic Scholar paper ID (this should work without an
API key):

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/<S2_PAPER_ID>?fields=title,year,externalIds,url"
```

Prefer records that expose `externalIds` such as DOI, PubMed, or PMC.

##### Get a PMID and PMCID from a DOI or Semantic Scholar ID

If you have a DOI, use the PMC ID Converter API to recover PubMed/PMC IDs when
available:

```bash
curl -sG "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/" \
  --data-urlencode "ids=<DOI>" \
  --data-urlencode "format=json" \
  --data-urlencode "tool=dismech" \
  --data-urlencode "email=<YOUR_EMAIL>"
```

This can return:

- `pmid`
- `pmcid`
- the normalized `doi`

If you start from a Semantic Scholar paper ID:

1. Query the Semantic Scholar paper endpoint and inspect `externalIds`
2. If `PubMed` is present, use that PMID directly
3. If `PMC` is present, keep the PMCID as supporting metadata
4. If only `DOI` is present, run the DOI through the PMC ID Converter API above

Then cache the article locally with whichever identifier you recovered:

```bash
just fetch-reference PMID:nnnnnnn
just fetch-reference DOI:10.xxxx/xxxxx
```

Use PMID-based references in YAML evidence whenever possible. Keep PMCID as
useful supporting metadata, but Dismech evidence validation is centered on PMID
abstracts.

Then use this to provide snippets/excerpts and explanations for assertions. For example, for a phenotype assertion:

```
phenotypes:
- name: <Phenotype Name>
  description: <Description from research>
  evidence:
  - reference: PMID:XXXXXXXX
    supports: <SUPPORT | REFUTE | PARTIAL>
    evidence_source: <HUMAN_CLINICAL | MODEL_ORGANISM | IN_VITRO | COMPUTATIONAL>
    snippet: "<Exact quote from abstract>"
    explanation: "<Why this supports the phenotype>"
```

**IMPORTANT**: The `evidence_source` field classifies **the type of evidence in the cited publication** (human study, animal model, cell culture, computational simulation), NOT whether the curation was performed by an AI agent. Always classify based on what the paper reports, regardless of who or what is doing the curation.

The same generic `evidence` list schema is used for most types.

### Step 5: Add term objects

Add term objects using ontology term IDs; for example, for a `pathophsyiology` object, it might look like this:

```
pathophysiology:
- name: <Mechanism Name>
  description: >
    <Detailed mechanism description from research>
  cell_types:
  - preferred_term: <Cell Type>
    term:
      id: CL:XXXXXXX
      label: <exact CL label>
  biological_processes:
  - preferred_term: <Process Name>
    term:
      id: GO:XXXXXXX
      label: <exact GO label>
```      

Consult the LinkML schema to see what terms are appropriate for any given object type. These will be validated.

You can use OAK commands to find relevant terms.

General term search (use mondo for diseases)

```bash
uv run runoak -i sqlite:obo:mondo info "l~<disease name>"
```

starts-with queries (use hp for phenotypes)

```bash
uv run runoak -i sqlite:obo:hp info "l^<phenotype>"
```

exact:

```
uv run runoak -i sqlite:obo:cl info CL:nnnnnnn
```

relationships (up and down):

```
uv run runoak -i sqlite:obo:go relationships --direction both GO:nnnnnnn
```


### Step 6: Validation

Strict validation check (adherence to schema, term and reference checks):

```bash
just validate kb/disorders/<Disease_Name>.yaml
```

Compliance report (completeness, term and evidence coverage):

```bash
just compliance kb/disorders/<Disease_Name>.yaml
```

### Step 7: Review

Use the `dismech-pr-review/` to do an initial round of review. Use a subagent for fresh context
(note that we haven't made the PR yet, but we want to do our own "red team" before making the actual PR

### Step 8: Make a PR

IF THE USER asks, then go ahead and make a PR on behalf of the user

### Step 9: Check reviews on the PR

Some time (~5 mins) after making the PR, a review will appear. You should prioritize in order:

1. reviews from a human/curator -- always take precedence
2. reviews from claude -- high quality but sometimes focuses on wrong thing
3. copilot -- useful for targeted line-level edits but in general lower quality

Follow these priorities but use judgment. If something doesn't sit right, ask for clarification on the PR.
Be proactive. If the review says "moderate" go ahead and fix it as you are fixing things anyway.
Ignore things that seem super-minor but if there is no cost in making a fix and you agree, do it.

Once you have made the changes:

1. **Stage ONLY disorder-relevant files** — never use `git add -A` or `git add .`:
   ```bash
   git add kb/disorders/ references_cache/ research/
   ```
   This prevents committing unrelated generated files (HTML, schema docs, cache CSVs) that cause merge conflicts.

2. **Commit and push**:
   ```bash
   git commit --no-verify -m "feat: Add <Disease Name> (<gene>) with deep research and validated evidence"
   git push
   ```

3. **Post a PR comment** summarizing what you did:
   - What was created/changed
   - Key PMIDs used
   - Validation results
   - Any issues you found but intentionally did NOT fix (with reasoning)


## File Naming Convention

Convert the disease name to a file-safe format:
- Replace spaces with underscores
- Remove special characters
- Use title case

Examples:
- "Type 2 Diabetes" → `Type_2_Diabetes.yaml`
- "Alzheimer's Disease" → `Alzheimers_Disease.yaml`
- "COVID-19" → `COVID-19.yaml`

## Minimum Required Fields

A new disorder file MUST include at minimum:

| Field | Source | Notes |
|-------|--------|-------|
| `name` | - | Human-readable disease name |
| `category` | Research | Mendelian, Complex, Infectious, etc. |
| `disease_term` | OAK lookup | MONDO term binding |
| `phenotypes` (1+) | Research | At least one phenotype with HPO term |
| `pathophysiology` (1+) | Research | At least one mechanism |
| `evidence` (1+) | Research | At least one PMID reference |

## Evidence Requirements

All evidence items MUST:
1. Use real PMIDs from the research query results
2. Have snippets that are exact quotes from abstracts
3. Include explanations linking evidence to claims
4. Set `evidence_source` based on the **publication's evidence type** (human clinical, animal model, in vitro, computational), NOT based on whether an AI agent performed the curation

**NEVER fabricate PMIDs or paraphrase snippets.**

**Evidence Source Classification**: When adding `evidence_source`, ask "What kind of study does this paper report?" not "How was this entry curated?" A computational fluid dynamics study gets `COMPUTATIONAL`, a mouse model study gets `MODEL_ORGANISM`, a human clinical trial gets `HUMAN_CLINICAL` - regardless of whether the curation was done by a human or an AI agent.

## Validation Errors and Fixes

### "Term not found in ontology"
- Re-run OAK lookup with fuzzy search: `info "l~<term>"`
- Use the exact label from the ontology

### "Snippet not found in reference"
- The quoted text must be from the PMID's abstract
- Fetch and verify: `just validate-references <file>`
- Use `--fix-threshold 0.80` to auto-repair minor mismatches

### "Required field missing"
- Check the schema for required fields
- Ensure `name`, `category`, and at least one `pathophysiology` entry

## Integration with Other Skills

Use all loaded skills, including:

- Use **dismech-terms** to add additional ontology term bindings
- Use **dismech-references** to validate/repair evidence items
- Use **dismech-compliance** to check completeness and identify gaps

## Responding to PR Review Comments

When asked to address review comments on an existing PR:

1. **Read the full review carefully** — understand each issue before making changes
2. **Address ALL 🔴 CRITICAL and 🟡 IMPORTANT issues** — don't skip any
3. **For issues you disagree with**, don't silently ignore them. Post a PR comment explaining why:
   - e.g. "The reviewer flagged X as a typo, but this matches the canonical MONDO label (verified with OAK). Filed upstream issue."
4. **After pushing fixes, post a PR comment** with a table summarizing:
   - Each reviewer issue and how you addressed it
   - Any issues you intentionally did NOT fix, with reasoning
   - Validation results after fixes
5. **Use `supports: PARTIAL`** when evidence is indirect — don't overstate evidence strength
6. **If evidence doesn't support a claim, find better evidence** rather than arguing about evidence_source classification
7. **Verify ontology terms with OAK** when the reviewer questions them — don't assume

### Git discipline for review fixes

```bash
# ONLY stage disorder-relevant files
git add kb/disorders/ references_cache/ research/

# NEVER do this — picks up generated files from other disorders
# git add -A
# git add .

git commit --no-verify -m "fix: Address PR review comments"
git push
```

## Anti-Hallucination Checklist

Before finalizing a new disorder file, verify:

- [ ] Deep research query was performed (document which tool)
- [ ] GeneReviews article searched for this disease
  - [ ] If found: PMID fetched, cached, and tagged `GeneReviews` in top-level `references:`
  - [ ] If found: all Clinical Characteristics phenotypes either captured in YAML or explicitly noted as out of scope
  - [ ] If found: any drug-safety warnings (Agents to Avoid) reflected in relevant treatment entries
  - [ ] If not found: no action needed
- [ ] All PMIDs exist and are for relevant papers
- [ ] All snippets are exact quotes from abstracts
- [ ] MONDO term exists and label matches exactly
- [ ] HPO terms exist and labels match exactly
- [ ] CL terms exist and labels match exactly
- [ ] GO terms exist and labels match exactly
- [ ] MAXO terms (if used) exist and labels match exactly
- [ ] `just validate` passes
- [ ] `just validate-terms-file` passes
- [ ] `just validate-references` passes
