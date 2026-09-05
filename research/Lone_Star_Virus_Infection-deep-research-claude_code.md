---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-08T14:54:58.888172'
end_time: '2026-08-08T15:04:12.278973'
duration_seconds: 553.39
template_file: /tmp/dismech_lsv_research.Pk40TE/template.md
template_variables:
  disease_name: Lone Star Virus Infection
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 6
  num_turns: 47
  total_cost_usd: 3.50864
  session_id: afedb4c1-8da1-43ba-853a-d913a057e033
  stop_reason: end_turn
citation_count: 25
---

## Question

Perform a non-operational bibliographic and ontological evidence review of
Lone Star Virus Infection. Limit the report to these questions:

1. What exact NCBI Taxonomy and current ICTV identities correspond to the virus
   called "Lone Star virus" in PMID:39983710 and PPR:PPR1272399? Distinguish it
   from similarly named tick-associated viruses.
2. How many peer-reviewed human observations specifically associated with this
   virus have been published, and what syndrome was reported? Do not infer a
   recurring clinical spectrum or frequency from a single observation.
3. What confirmation was discordant, and what do the peer-reviewed authors say
   about etiologic causality? State the uncertainty explicitly.
4. What is the publication status, server, date, and relationship to the human
   report of PPR:PPR1272399 / DOI:10.64898/2026.07.06.736858?

Use primary literature and authoritative NCBI, ICTV, PubMed, Europe PMC, or
publisher records. Clearly distinguish peer-reviewed evidence from preprint
evidence. Provide stable source links and identifiers.

Do not provide or derive laboratory or clinical procedures, assay protocols,
culturing, isolation, reverse-genetics, synthesis, propagation, engineering,
optimization, doses, materials, parameters, troubleshooting, or experimental-
model mechanisms. Do not recommend experiments. Summarize discordant results
only at the high level necessary to assess causality. Do not generalize human
transmission, diagnosis, treatment, phenotype frequency, or pathogenicity from
the single reported observation or from model systems.


## Output

# Bibliographic and Ontological Evidence Review: "Lone Star Virus Infection"

**Prepared:** 2026-08-08 · **Scope:** identity, evidence base, causality language, and preprint status only. No laboratory, clinical, or experimental-model detail is reproduced.

---

## Scope note and method

This review answers four bounded questions using primary and authority records only: NCBI Taxonomy (E-utilities + Taxonomy Browser), NCBI Nucleotide, PubMed, Europe PMC REST, ICTV, the bioRxiv API, and the publisher (CDC *Emerging Infectious Diseases*) record. Peer-reviewed and preprint evidence are labeled separately throughout.

Deliberately excluded, per the requested constraints: assay procedures, isolation/culture/reverse-genetics methodology, animal-model mechanisms, doses/parameters, diagnostic or therapeutic guidance, and any generalization from the single human observation. Where the underlying sources contain such material (notably the 2026 preprint), it is cited by identity only and its substance is not summarized.

---

## 1. Taxonomic and ontological identity

### 1.1 Current identity

The virus called "Lone Star virus" (LSV) in PMID:39983710 and PPR:PPR1272399 resolves to a single, unambiguous taxon:

| Authority | Identifier | Name | Rank |
|---|---|---|---|
| ICTV (species) | — | ***Bandavirus amblyommae*** | species |
| NCBI Taxonomy | **txid3048183** | *Bandavirus amblyommae* | species |
| NCBI Taxonomy | **txid2734426** | Lone Star bandavirus | no rank (child of 3048183) |
| NCBI Taxonomy | **txid1219465** | **Lone Star virus** | no rank (child of 2734426) |

**Full NCBI lineage** (verified by `efetch db=taxonomy`, 2026-08-08):
Viruses → *Riboviria* (realm, 2559587) → *Orthornavirae* (kingdom, 2732396) → *Negarnaviricota* (phylum, 2497569) → *Polyploviricotina* (subphylum, 2497571) → *Bunyaviricetes* (class, 3151693) → *Hareavirales* (order, 3151839) → ***Phenuiviridae*** (family, 1980418) → ***Bandavirus*** (genus, 2733256) → ***Bandavirus amblyommae*** (species, 3048183).

An ontological point that matters for curation: **NCBI retains a three-node chain**, not a single node. `txid1219465` ("Lone Star virus") is the virus-name node; `txid2734426` ("Lone Star bandavirus") is the *superseded ICTV species epithet* retained as an intermediate no-rank node; `txid3048183` is the current species. A KB entry that binds to `txid2734426` is binding to a deprecated nomenclatural form, not to a distinct organism. The NCBI Browser species page lists "Lone Star bandavirus", "Lone Star virus", and "Lone Star virus TMA1381" as alternate names under 3048183; note that the corresponding `efetch` XML did not render an `OtherNames` block, so treat the browser synonym list as display-layer metadata rather than a stable API field.

### 1.2 Nomenclatural history (why three names exist)

- **1969** — first described as an unnamed new agent from *Amblyomma americanum*: Kokernot RH, Calisher CH, Stannard LJ, Hayes J. *Am J Trop Med Hyg* 1969;18(5):789–95. **PMID:5810802**. (Isolate collected 1966–67.)
- **2013** — genome sequenced and placed as a highly divergent bunyavirus (then discussed in phlebovirus terms; genus *Bandavirus* did not yet exist): Swei A, Russell BJ, Naccache SN, et al. *PLoS One* 2013;8(4):e62083. **PMID:23637969**, DOI:10.1371/journal.pone.0062083.
- **~2020** — ICTV establishes genus *Bandavirus*; species named *Lone Star bandavirus* (this is the origin of NCBI txid2734426).
- **2023** — ICTV binomial renaming of *Negarnaviricota* species; *Lone Star bandavirus* → ***Bandavirus amblyommae***. Documented in Kuhn JH, Abe J, Adkins S, et al., "Annual (2023) taxonomic update…", *J Gen Virol* 2023;104(8), DOI:10.1099/jgv.0.001864, **PMID:37622664**, PMCID:PMC10721048 (abstract: "Two genera and 538 species were renamed"). A Europe PMC full-text search for the exact string `"Bandavirus amblyommae"` returns 3 records, of which two are this paper and the 2024 annual update (PMID:40512168, DOI:10.1099/jgv.0.002077).
- **Current ICTV release:** **MSL41 (2025)**, per https://ictv.global/msl.

**Verification limitation, stated explicitly:** the ICTV taxon-detail page is JavaScript-rendered and did not return taxon data to a plain fetch, and the ICTV *Bandavirus* report chapter does not enumerate its species inline (it states only that "Nine bandaviruses are assigned to the genus *Bandavirus*"). ICTV species-level assignment is therefore corroborated here **indirectly but consistently** by three independent lines: (a) the ICTV chapter's count of nine, which matches exactly the nine species NCBI places in genus *Bandavirus*; (b) NCBI's ICTV-synchronized species record; and (c) the ICTV annual-update papers above. I did not read the MSL41 spreadsheet row directly.

### 1.3 Reference sequence identifiers

- **RefSeq (reference genome, isolate TMA 1381):** `NC_021242.1` (L, 6,341 bp), `NC_021243.1` (M, 3,313 bp), `NC_021244.1` (S, 1,876 bp).
- **Original GenBank deposits (Swei et al. 2013):** `KC589005.1`, `KC589006.1`, `KC589007.1`.
- **Sequences derived from the human observation (see §2):** `PQ347830.1` (297 bp), `PQ347831.1` (224 bp), `PQ347832.1` (140 bp) — all **partial S segment**, strain **UC1**, `/host="Homo sapiens"`, `/isolation_source="cerebrospinal fluid"`, `/country="USA: Idaho"`, `/collection_date=2023`, submitted 14-SEP-2024 by Chiu CY & Servellita V (UCSF), released 12-OCT-2024.
  **These three records carry the GenBank `UNVERIFIED:` flag in their DEFINITION lines.** That flag is part of the primary record and should be carried into any provenance annotation; it is a documented qualification on the only human-derived sequence evidence that exists for this virus.

Total NCBI Nucleotide holdings under `txid1219465[Organism:exp]`: **15 records** (3 RefSeq + 3 GenBank originals + 3 human-derived partials + 6 associated protein/duplicate entries).

### 1.4 Distinguishing similarly named tick-associated entities

An exhaustive NCBI Taxonomy name search for `"lone star virus" OR "lone star bandavirus" OR "lone star tick"` returns **exactly three taxa**: 1219465, 2734426, and **6943**. The following are the realistic confusion set:

| Entity | NCBI txid | Species | Family | Relationship to LSV |
|---|---|---|---|---|
| **Lone star tick** (*Amblyomma americanum*) | **6943** | *Amblyomma americanum* | Ixodidae | **Not a virus.** The arthropod whose common name supplies the virus's name. The single most likely ontological mis-binding. |
| **Heartland virus** | 1216928 | *Bandavirus heartlandense* | Phenuiviridae | **Congeneric**, same tick species association, and an established human pathogen with its own literature. Distinct taxon; do not merge or transfer claims. |
| **Bourbon virus** | 1618189 | *Thogotovirus bourbonense* | **Orthomyxoviridae** | Different family, different order, different class. Also *A. americanum*-associated and an established human pathogen. Frequently co-listed with LSV in "lone star tick viruses" reviews. |
| **Bhanja virus** | 1213620 | *Bandavirus bhanjanagarense* | Phenuiviridae | Congeneric. Note the species epithet is `bhanjanagarense`, not `bhanjaense` — a common transcription error. |
| **SFTS virus** | — | *Bandavirus dabieense* | Phenuiviridae | Congeneric; the genus type/most-studied member. |
| **Potosi virus** | 273360 | *Orthobunyavirus potosiense* | **Peribunyaviridae** | **Not a bandavirus and not tick-associated.** Critical for this review: Potosi virus is the *other* virus in the same publication (PMID:39983710) and concerns a **different patient**. Claims about the two must not be pooled. |

The nine NCBI species in genus *Bandavirus* are: *albatrossense* (3051988), ***amblyommae*** (3048183), *bhanjanagarense* (3051989), *dabieense* (2748958), *guertuense* (3051991), *heartlandense* (3051992), *kismaayoense* (3051993), *razdanense* (3051994), *zwieselense* (3059756).

**One further disambiguation trap:** pre-2020 literature (including PMID:23637969) describes LSV as an unclassified/divergent "bunyavirus" or discusses it in phlebovirus terms. That is the **same virus under superseded higher classification**, not a separate entity.

---

## 2. Peer-reviewed human observations

### 2.1 Count: one

**Exactly one peer-reviewed human observation associated with *Bandavirus amblyommae* has been published — a single patient.**

Exhaustive searches performed 2026-08-08:
- **PubMed** `"lone star virus"` (all fields): **5 records total** — PMIDs 42384674, 41636781, 39983710, 23637969, 5810802. Of these, only **39983710** contains a human observation.
- **Europe PMC** `"lone star virus"` (all sources, MED + PPR + PMC): **52 records**. Manual triage of the full result set found no additional human case report, human case series, or LSV-specific human seroprevalence study. The non-LSV-specific hits are reviews, tick-virome and vector surveys, Heartland/Bourbon serosurveys in wildlife, SFTSV-focused work, and ICTV taxonomy updates.
- The two other 2026 LSV-titled peer-reviewed papers are **not** human observations: PMID:41636781 (Eaton CW, et al., *Vector Borne Zoonotic Dis* 2026;26(6):355–64, DOI:10.1177/15303667261420983) concerns viral and host model systems; PMID:42384674 (Li C, et al., *Virulence* 2026;17(1):2696699) is a genus-level *Bandavirus* comparison. Their content is out of the scope constraints of this review and, being non-human, cannot be used to characterize human disease.

### 2.2 The single observation

**Citation (peer-reviewed):** Chiu CY, Godasi RR, Hughes HR, Servellita V, Foresythe K, Tubati A, Zorn K, Sidhu S, Wilson MR, Bethina SV, Abenroth D, Cheng Y, Grams R, Reese C, Isada C, Thottempudi N. "Two Human Cases of Fatal Meningoencephalitis Associated with Potosi and Lone Star Virus Infections, United States, 2020–2023." *Emerging Infectious Diseases* 2025;**31**(2):215–221. DOI:10.3201/eid3102.240831. **PMID:39983710**. PMCID:PMC11845157. Publication type: **Case Reports; Journal Article**.

**What was reported for the LSV patient (Case 2 of 2):** a 60-year-old man from Idaho, USA, with a history of common variable immunodeficiency, presenting with "a 1-week history of headache and myalgias" and mental-status changes, in whom cerebrospinal fluid metagenomic next-generation sequencing was "positive for Lone star virus (LSV)". The reported syndrome is **fatal meningoencephalitis**; the patient "died 26 days after admission."

**Constraints on how this may be represented:**
- **n = 1.** This is one patient. No frequency, penetrance, incidence, case-fatality rate, or recurring clinical spectrum can be derived from it, and none is asserted here.
- **Case 1 of the same paper is a different virus** (Potosi virus, *Orthobunyavirus potosiense*, Peribunyaviridae). The paper's title and abstract cover both; only Case 2 pertains to LSV.
- **The paper does not claim priority.** It does not state that this is the first human detection of LSV, and no such claim should be attributed to it. What can be said, as a negative bibliographic finding: no earlier peer-reviewed human observation for this virus was found in PubMed or Europe PMC.
- **The paper's own framing is associative, not causal** — "Associated with" in the title, and "associated with fatal cases of meningoencephalitis in immunocompromised patients" in the Discussion.

---

## 3. Discordant confirmation and the authors' causality language

### 3.1 The discordance (stated at the minimum level needed to assess causality)

Detection and confirmation **did not agree between laboratories**. Reported verbatim by the authors:

> "Additional testing of residual CSF by CDC did not detect reads from LSV on mNGS, and confirmatory testing with viral isolation and plaque reduction neutralization testing was negative."

At the originating laboratory, detection was internally reproducible across sequencing runs (initially 50 of 14,386,666 reads aligning to the LSV genome at 84%–95% identity; a subsequent higher-depth run yielded 2,460 reads mapping to all three genome segments, covering 1,601 bp (13.6%) of the 11,730-bp trisegmented genome, with 183 SNPs and pairwise identity of 88.6%).

The authors attribute the inter-laboratory discordance to "potential sample degradation caused by multiple freeze–thaw cycles and longer storage times" and to "differences in sample preparation methods." That is their stated explanation; it is an attribution, not an independent resolution of the discordance.

**Net position:** the detection was **sequence-based only**, reproduced within one laboratory, and **not independently confirmed** — a second, independent laboratory failed to redetect it and returned negative results on two orthogonal confirmatory approaches. The corresponding sequence deposits are additionally flagged `UNVERIFIED:` by GenBank (§1.3). No supporting serologic confirmation is reported; the authors separately note that serologic testing "is problematic for highly immunocompromised patients, for whom results can be false-negative."

### 3.2 What the peer-reviewed authors say about causality

The authors explicitly decline a causal claim:

> "Because mNGS is a molecular detection technique and positive testing alone is insufficient to fulfill Koch's postulates, caution is warranted with clinical interpretation of mNGS results, especially with detection of a novel agent of unclear pathogenicity in highly susceptible immunocompromised hosts."

and:

> "Further clinical and epidemiologic studies are needed to characterize the spectrum of clinical disease and pathogenicity associated with POTV and LSV infections in humans."

**Explicit statement of uncertainty.** Etiologic causality is **not established**. The published evidence supports a claim of the form *"viral RNA was detected in the CSF of one immunocompromised patient with fatal meningoencephalitis, without independent confirmation"* — an **association reported in a single patient**. It does **not** support "*Bandavirus amblyommae* causes meningoencephalitis," "LSV is a human pathogen," or any statement about human transmission, diagnosis, treatment, phenotype frequency, or pathogenicity. The authors themselves characterize LSV as "a novel agent of **unclear pathogenicity**."

---

## 4. Status of PPR:PPR1272399 / DOI:10.64898/2026.07.06.736858

| Field | Value | Source |
|---|---|---|
| **Title** | "Reverse genetics and comparative pathogenesis of Lone star virus" | bioRxiv API; Europe PMC |
| **Europe PMC ID** | PPR1272399 (source `PPR`) | Europe PMC REST |
| **DOI** | 10.64898/2026.07.06.736858 | bioRxiv API |
| **Server** | **bioRxiv** (`"server": "bioRxiv"`) | bioRxiv API |
| **Posted** | **2026-07-07** (`date`); Europe PMC `firstPublicationDate` 2026-07-07 | bioRxiv API; Europe PMC |
| **Version** | **1** | bioRxiv API |
| **Type / category** | "new results" / microbiology | bioRxiv API |
| **License** | CC BY-NC-ND | bioRxiv API |
| **Corresponding author** | Natasha Louise Tilston-Lunel | bioRxiv API |
| **Authors** | Omoga DCA; Witt C; Giesel H; Bowen JM; Gunter K; Pozuelos S; Relich R; Brennan B; Tilston-Lunel NL | bioRxiv API |
| **Peer-review status** | **Preprint. Not peer reviewed.** | — |
| **Published journal version** | **None.** bioRxiv API `"published": "NA"`; Europe PMC returns no `commentCorrectionList` / linked published version | bioRxiv API; Europe PMC |

**Metadata note for curation:** Europe PMC renders the last author as **"Tilston NL"**, while bioRxiv gives **"Tilston-Lunel, N. L."** — an indexing truncation of a hyphenated surname, not two different people. Also note the unusual DOI prefix **10.64898** (not the legacy `10.1101` bioRxiv prefix); the bioRxiv API nonetheless returns `server: bioRxiv` for this DOI, confirming the server assignment. Where the DOI stem encodes 2026.07.06 and the posting date is 2026-07-07, cite **2026-07-07** as the posting date.

**Relationship to the human report.** The preprint **cites the peer-reviewed human observation as its motivation**. Its abstract states that LSV "remains poorly studied, and its pathogenic potential is not well defined," and that "Recent detection of LSV RNA in cerebrospinal fluid from an immunocompromised patient in Idaho, U.S., with fatal meningoencephalitis further highlights the need" for further study. The Idaho patient is Case 2 of PMID:39983710 (§2.2) — so the two documents are linked by **the preprint referencing the case report as background**, not by any shared patient data, and not by any confirmation of the human finding.

The preprint is a laboratory virology study. Its experimental content — model systems, reverse-genetics work, comparative outcomes, and cross-protection findings — is **outside the scope of this review by the stated constraints and is not summarized here**. Two points bear on evidence weight only:

1. It is **preprint evidence**, uncertified by peer review, version 1, with no journal version as of 2026-08-08.
2. It contains **no human observation** and therefore cannot corroborate the Idaho detection, cannot resolve the inter-laboratory discordance in §3.1, and cannot be used to infer human pathogenicity, transmission, or clinical phenotype.

---

## Summary of evidence tiers

| Claim | Strongest available support | Tier |
|---|---|---|
| Identity = *Bandavirus amblyommae*, genus *Bandavirus*, family *Phenuiviridae* | NCBI txid3048183; ICTV MSL41; Kuhn et al. 2023 (PMID:37622664) | Authority record |
| Virus originally isolated from *Amblyomma americanum* (1969) | PMID:5810802 | Peer-reviewed |
| Reference genome (isolate TMA 1381) | NC_021242–NC_021244; PMID:23637969 | Authority record + peer-reviewed |
| One patient with fatal meningoencephalitis and CSF detection of LSV RNA | PMID:39983710 (Case 2) | **Peer-reviewed, n=1, case report** |
| Independent confirmation of that detection | **Absent — discordant**; CDC mNGS, isolation, and PRNT negative | Peer-reviewed negative result |
| Etiologic causality in that patient | **Not established**; authors invoke Koch's postulates as unfulfilled | Explicitly unresolved |
| LSV as a human pathogen generally | **No supporting evidence found**; authors describe "unclear pathogenicity" | Unsupported |
| Laboratory characterization of LSV pathogenesis | PPR:PPR1272399 (bioRxiv, 2026-07-07, v1) | **Preprint, non-human, not peer reviewed** |

## Verification limitations

Three things I could not verify directly and am not asserting as verified: (a) the ICTV MSL41 spreadsheet row for *Bandavirus amblyommae* was not read — ICTV species assignment is corroborated indirectly as described in §1.2; (b) the ICTV taxon-detail page did not render to a plain fetch, so no ICTV `taxnode_id` is reported; (c) full texts of PMID:41636781 and PMID:42384674 were screened by title/abstract-level metadata rather than read in full, though both are non-human by title and neither returned as a human-observation record in the Europe PMC sweep.

---

## Sources

- [PubMed 39983710 — Chiu CY, et al. *Emerg Infect Dis* 2025;31(2):215–221](https://pubmed.ncbi.nlm.nih.gov/39983710/) · [PMC11845157](https://pmc.ncbi.nlm.nih.gov/articles/PMC11845157/) · [CDC EID publisher record, DOI:10.3201/eid3102.240831](https://wwwnc.cdc.gov/eid/article/31/2/24-0831_article)
- [PubMed 23637969 — Swei A, et al. *PLoS One* 2013;8(4):e62083](https://pubmed.ncbi.nlm.nih.gov/23637969/)
- [PubMed 5810802 — Kokernot RH, et al. *Am J Trop Med Hyg* 1969;18(5):789–95](https://pubmed.ncbi.nlm.nih.gov/5810802/)
- [PubMed 37622664 — Kuhn JH, et al. Annual (2023) taxonomic update, *J Gen Virol*](https://pubmed.ncbi.nlm.nih.gov/37622664/) · [PubMed 40512168 — Annual (2024) update](https://pubmed.ncbi.nlm.nih.gov/40512168/)
- [NCBI Taxonomy — *Bandavirus amblyommae* (txid3048183)](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3048183) · [Lone Star virus (txid1219465)](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1219465) · [genus *Bandavirus* (txid2733256)](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2733256) · [*Amblyomma americanum* (txid6943)](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=6943)
- [NCBI Nucleotide NC_021242.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_021242.1) · [NC_021243.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_021243.1) · [NC_021244.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_021244.1) · [PQ347830.1](https://www.ncbi.nlm.nih.gov/nuccore/PQ347830.1) · [PQ347831.1](https://www.ncbi.nlm.nih.gov/nuccore/PQ347831.1) · [PQ347832.1](https://www.ncbi.nlm.nih.gov/nuccore/PQ347832.1)
- [ICTV Master Species List index (MSL41, 2025)](https://ictv.global/msl) · [ICTV Report — Genus: *Bandavirus*](https://ictv.global/report/chapter/phenuiviridae/phenuiviridae/bandavirus) · [ICTV Report — Family: *Phenuiviridae*](https://ictv.global/report/chapter/phenuiviridae/phenuiviridae) · [ICTV current taxonomy release](https://ictv.global/taxonomy)
- [Europe PMC preprint PPR1272399](https://europepmc.org/article/PPR/PPR1272399) · [bioRxiv API record, DOI:10.64898/2026.07.06.736858](https://api.biorxiv.org/details/biorxiv/10.64898/2026.07.06.736858)
- [PubMed 41636781 — Eaton CW, et al. *Vector Borne Zoonotic Dis* 2026](https://pubmed.ncbi.nlm.nih.gov/41636781/) · [PubMed 42384674 — Li C, et al. *Virulence* 2026](https://pubmed.ncbi.nlm.nih.gov/42384674/)

*One operational note unrelated to the report's content: several claude.ai MCP connectors in this session (PubMed, OLS, and others) are unauthenticated and could not be used here, so all queries went through public REST/E-utilities endpoints instead. Authorizing those connectors in an interactive session would let a future run query PubMed and OLS directly.*
