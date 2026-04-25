# Nemaline Myopathy Curation Interaction Summary

**Date:** 2026-02-19
**Branch:** `nemaline_rod_myopathy`
**Deep Research Provider:** Falcon

---

## 1. Primary Request and Intent

The user first asked for a tour of the dismech project (a LinkML-based disease pathophysiology knowledge base). After the walkthrough, the user invoked `/curate nemaline rod myopathy` to create a new disorder entry following the `initiate-new-disorder-creation` skill workflow.

After the initial curation was complete, the user challenged whether 7 specific foundational papers were considered during curation — they were not, as the falcon deep research provider focused on 2023–2024 literature. The user then requested incorporation of those 7 papers into the entry, covering the full historical breadth of NM literature from 1984 to 2024.

## 2. Key Technical Concepts

- **LinkML schema validation**: Disorder YAML files must conform to the `Disease` class in `src/dismech/schema/dismech.yaml`
- **Three-layer validation stack**: schema validation (`just validate`), ontology term validation (`just validate-terms`), and reference/snippet validation (`just validate-references`)
- **Evidence-backed curation**: Every factual claim requires a PMID reference with an exact quoted snippet from the abstract — no paraphrasing allowed
- **Ontology term bindings**: Phenotypes → HPO, Cell types → CL, Biological processes → GO, Treatments → MAXO, Diseases → MONDO
- **OAK (Ontology Access Kit)**: Used for looking up ontology terms via `uv run runoak -i sqlite:obo:<ontology> info`
- **Deep research via falcon**: `just research-disorder falcon Nemaline_Myopathy` runs external deep research and outputs to `research/Nemaline_Myopathy-deep-research-falcon.md`
- **Reference fetching**: `just fetch-reference PMID:nnnnn` or `just fetch-reference DOI:...` caches abstracts to `references_cache/`
- **Pre-write validation hook**: A git hook at `.claude/hooks/validate_disorder_hook.py` blocks writes that would create invalid YAML files
- **Compliance scoring**: `just compliance` reports coverage percentages for evidence, terms, and other recommended fields

## 3. Workflow Steps

### Step 1: Verify Disorder Doesn't Exist
- Checked `kb/disorders/` — no existing Nemaline Myopathy file found
- Looked up MONDO term: `MONDO:0018958` (nemaline myopathy)

### Step 2: Create Initial YAML Scaffold
- Created `kb/disorders/Nemaline_Myopathy.yaml` with textbook knowledge
- Included basic structure: name, category (Mendelian), description, disease_term, parents, subtypes, pathophysiology, phenotypes, genetics, treatments

### Step 3: Deep Research
- Ran `just research-disorder falcon Nemaline_Myopathy`
- Research output written to `research/Nemaline_Myopathy-deep-research-falcon.md`
- Falcon returned 42 citations focused on 2023–2024 literature
- Key limitation: falcon's recency bias missed foundational/classic NM papers

### Step 4: DOI-to-PMID Resolution
- Falcon output provided DOIs rather than PMIDs
- NCBI PMC ID converter API returned 404 errors for all DOIs
- Solved by using Biopython `Entrez.esearch` to search PubMed by title keywords
- Successfully resolved 10 DOIs to correct PMIDs

### Step 5: Evidence Enhancement
- Fetched and read 10 abstracts from falcon research
- Added exact snippet quotes from abstracts to evidence items
- Added ontology terms (HP, CL, GO, MAXO) via OAK lookups

### Step 6: User-Identified Paper Incorporation
- User identified 7 foundational papers not covered by falcon research:
  1. PMID:17272906 — Indian cohort study (2007)
  2. PMID:31228046 — Comprehensive NM review (2019)
  3. PMID:9372751 — Adult-onset NM case report (1998)
  4. PMID:35810298 — Severe ACTA1-NM study (2022)
  5. PMID:6481414 — Early adult NM report with mixed pathology (1984)
  6. PMID:19208402 — NM with isolated respiratory failure (2009)
  7. PMID:39691005 — SLONM case with monoclonal protein (2024)
- All 7 papers were fetched, read, and incorporated with exact snippets across multiple sections

### Step 7: Validation
- `just validate` — schema validation passed
- `just validate-terms-file` — ontology term validation passed
- `just validate-references` — reference/snippet validation passed
- `just compliance` — 82.4% compliance (82.8% weighted)

## 4. Files Created/Modified

| File | Action | Description |
|------|--------|-------------|
| `kb/disorders/Nemaline_Myopathy.yaml` | Created | Main disorder entry (711 lines) |
| `research/Nemaline_Myopathy-deep-research-falcon.md` | Generated | Falcon deep research output |
| `pages/disorders/Nemaline_Myopathy.html` | Generated | Rendered HTML page |
| `references_cache/PMID_38634969.md` | Fetched | Karimi 2024 — NEB thin filament mechanisms |
| `references_cache/PMID_36703211.md` | Fetched | Nicolau 2023 — Nemaline rod signatures (iNM vs SLONM) |
| `references_cache/PMID_38376469.md` | Fetched | Galli 2024 — Tirasemtiv in NEM3 mouse model |
| `references_cache/PMID_36661122.md` | Fetched | Casey 2023 — NRAP in nebulin-deficient NM |
| `references_cache/PMID_36960434.md` | Fetched | 2023 — Pediatric NM systematic review |
| `references_cache/PMID_36714460.md` | Fetched | Moreno 2023 — NEB-NM cohort (33 patients) |
| `references_cache/PMID_39651462.md` | Fetched | van Kleef 2024 — NEM6/KBTBD13 (24 patients) |
| `references_cache/PMID_37432316.md` | Fetched | Mansur 2023 — KLHL40/UPS mechanism |
| `references_cache/PMID_38500810.md` | Fetched | 2024 — ACTA1 case report |
| `references_cache/PMID_39501809.md` | Fetched | 2024 — Additional NM reference |
| `references_cache/PMID_17272906.md` | Fetched | Jain 2007 — Indian NM cohort |
| `references_cache/PMID_31228046.md` | Fetched | Ravenscroft 2019 — Authoritative NM review |
| `references_cache/PMID_9372751.md` | Fetched | Gyure 1997 — Adult-onset NM with HIV |
| `references_cache/PMID_35810298.md` | Fetched | Néstor-Bergmann 2022 — Severe ACTA1-NM |
| `references_cache/PMID_6481414.md` | Fetched | Engel 1984 — Early adult NM report |
| `references_cache/PMID_19208402.md` | Fetched | Kelly 2009 — NM respiratory failure |
| `references_cache/PMID_39691005.md` | Fetched | Vashisht 2024 — SLONM case |

## 5. Errors and Fixes

### Schema Validation Errors (caught by pre-write hook)

| Error | Root Cause | Fix |
|-------|-----------|-----|
| `description` not allowed in `Genetic` class | Schema uses `notes` for Genetic, not `description` | Changed all `description:` to `notes:` in genetic entries |
| `notes` not allowed in `Inheritance` class | Overcorrection from previous error; schema allows `description` here | Changed back to `description:` in inheritance entries |
| `percentage` and `population` not valid in `EpidemiologyInfo` | Used Prevalence-style fields not in schema | Restructured to `name: Incidence` with `description` and `notes` |
| Snippet validation failure for PMID:39651462 | Brackets `[4.9-8.1]` in snippet may have caused matching issues | Replaced with different snippet from same abstract |

### DOI Resolution Errors

| Error | Root Cause | Fix |
|-------|-----------|-----|
| NCBI PMC ID converter API 404 | API endpoint returned 404 for all DOIs | Used Biopython `Entrez.esearch` with title keywords |
| Guessed PMIDs were wrong | Manual PMID guessing returned unrelated papers (neurofilaments, breast cancer, scorpion venom) | Abandoned guessing; used systematic title-based search |

### Deep Research Limitation

| Issue | Impact | Mitigation |
|-------|--------|-----------|
| Falcon provider focused on 2023–2024 | Missed 7 foundational papers (1984–2022) | User identified gaps; papers manually incorporated |

## 6. Final Entry Statistics

| Metric | Value |
|--------|-------|
| Subtypes | 5 (Severe Congenital, Typical Congenital, Childhood-Onset, Adult-Onset, NEM6) |
| Pathophysiology mechanisms | 6 (Thin Filament Dysfunction, Nemaline Rod Formation, Thin Filament Length Dysregulation, UPS/KLHL40, Nuclear Envelope Disruption, NRAP-Mediated Sarcomere Disorganization) |
| Phenotypes | 9 |
| Genetic entries | 10 (NEB, ACTA1, KBTBD13, KLHL40, TPM3, TPM2, TNNT1, CFL2, LMOD3, KLHL41) |
| Treatments | 7 (including 2 investigational) |
| Epidemiology entries | 1 |
| Unique PMIDs | 17 (spanning 1984–2024) |
| Compliance | 82.4% (82.8% weighted) |
| Validation | All 3 layers pass (schema, terms, references) |

## 7. PMIDs Used

| PMID | First Author | Year | Key Contribution |
|------|-------------|------|-----------------|
| 38634969 | Karimi | 2024 | NEB thin filament length mechanisms, omecamtiv mecarbil |
| 36703211 | Nicolau | 2023 | Rod signatures: iNM vs SLONM |
| 38376469 | Galli | 2024 | Tirasemtiv in NEM3 mouse model |
| 36661122 | Casey | 2023 | NRAP as disease modifier in NEB-NM |
| 36960434 | — | 2023 | Pediatric NM systematic review |
| 36714460 | Moreno | 2023 | NEB-NM cohort (33 patients) |
| 39651462 | van Kleef | 2024 | NEM6/KBTBD13 cross-sectional study (24 patients) |
| 37432316 | Mansur | 2023 | KLHL40/UPS/ER-Golgi trafficking mechanism |
| 38500810 | — | 2024 | Novel ACTA1 variant case report |
| 39501809 | — | 2024 | Additional NM reference |
| 17272906 | Jain | 2007 | Indian NM cohort, epidemiology (0.53% of muscle diseases) |
| 31228046 | Ravenscroft | 2019 | Comprehensive NM review (authoritative) |
| 9372751 | Gyure | 1997 | Adult-onset NM with HIV, rod morphology description |
| 35810298 | Néstor-Bergmann | 2022 | Severe ACTA1-NM, nuclear envelope disruption |
| 6481414 | Engel | 1984 | Early adult NM case, mixed pathology |
| 19208402 | Kelly | 2009 | NM with isolated respiratory failure |
| 39691005 | Vashisht | 2024 | SLONM case with monoclonal protein |

## 8. Lessons Learned

1. **Deep research providers have recency bias**: Falcon focused on 2023–2024 papers, missing foundational literature. Supplementary manual reference searching is needed, especially for well-established diseases with decades of published literature.

2. **Schema field constraints vary by class**: Different LinkML classes (`Genetic`, `Inheritance`, `EpidemiologyInfo`) have different allowed slots. Always check the schema before writing YAML.

3. **DOI-to-PMID resolution is fragile**: The NCBI PMC ID converter API can fail. Title-based PubMed search via Biopython `Entrez.esearch` is a reliable fallback.

4. **Never guess PMIDs**: Attempting to guess PMIDs based on author/year produces completely unrelated papers. Always use systematic search.

5. **Pre-write validation hooks catch errors early**: The `.claude/hooks/validate_disorder_hook.py` hook prevented multiple schema-invalid writes from being saved, forcing immediate correction.

6. **Snippet bracket characters can cause validation issues**: Brackets in quoted snippets (e.g., `[4.9-8.1]`) may not survive the reference validation pipeline. Use alternative snippets when possible.

## 9. User Messages (Chronological)

1. "Give me a tour of the dismech project"
2. `/curate nemaline rod myopathy`
3. "is there evidence in the output, that you considered and read these papers: https://pubmed.ncbi.nlm.nih.gov/17272906/ https://pubmed.ncbi.nlm.nih.gov/31228046/ https://pubmed.ncbi.nlm.nih.gov/9372751/ https://pubmed.ncbi.nlm.nih.gov/35810298/ https://pubmed.ncbi.nlm.nih.gov/6481414/ https://pubmed.ncbi.nlm.nih.gov/19208402/ https://pubmed.ncbi.nlm.nih.gov/39691005/"
4. "yes" (confirming to incorporate the 7 papers)
5. "write out this interaction to a md file"
