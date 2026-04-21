---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-16T19:00:00Z'
end_time: '2026-04-16T19:45:00Z'
duration_seconds: 2700.0
citation_count: 7
notes: >
  Manual PubMed- and issue-based review completed to support disease-level
  dismech curation of southern tick-associated rash illness (STARI). Focus was
  kept on exact PMID-backed syndrome framing, microbiologic uncertainty,
  distinction from Lyme disease, and curation-ready phenotype/progression
  evidence.
---

## Question

Provide a disease-level, curation-ready review of Southern Tick-Associated Rash Illness (STARI), including disease framing, microbiologic status, differentiation from Lyme disease, geography, clinical course, and any mechanism-relevant observations that are strong enough to support dismech assertions.

## Output

# Southern Tick-Associated Rash Illness (STARI): Manual Curation Summary

## Disease framing and lumping/splitting

STARI should be curated as its own **lone-star-tick-associated erythema-migrans-like syndrome**, not as a subtype of Lyme disease. The strongest comparative clinical study states that an EM-like illness not caused by *Borrelia burgdorferi* occurs in many southern US states and is known as STARI / Masters disease (PMID:16142659). The 2022 Lyme review likewise treats STARI as one of the principal mimics of early Lyme disease rather than as a geographic Lyme variant (PMID:36116832).

The local MONDO anchor is necessarily imperfect. MONDO issue #9873 requests an exact term for “Southern tick-associated rash illness” with exact synonyms **STARI** and **Masters disease**, under the parent **MONDO:0025294 tick-borne infectious disease**. Until that request is resolved, local curation should use a close match to MONDO:0025294 plus the tracked issue, while NCIT already provides an exact concept (**NCIT:C128427 Southern Tick-Associated Rash Illness**).

## Microbiology and etiology

The core curation point is that **the etiologic agent remains unknown**.

The foundational 2005 Missouri microbiology study found that neither *B. lonestari* nor *B. burgdorferi* was likely to be the cause of the Missouri EM-like lesions; the abstract explicitly concludes that the etiology remains unknown (PMID:15668867). This remains current rather than historical: a 2025 CDC-associated series of 58 STARI patients reported that 16S sequencing detected **no known bacterial pathogen** and again stated that the etiologic agent remains unknown (PMID:40517644).

This means the dismech entry should **not assert an `infectious_agent`** despite the clinical syndrome’s strong tick association and its current placement under a broad MONDO infectious parent.

## Mechanism-relevant observations

There is still no confirmed linear disease mechanism. The strongest curation-ready mechanistic observations are:

1. **Unknown cause despite microbiologic workup**
   Multiple cohorts have failed to identify a causative bacterium (PMID:15668867, PMID:40517644).

2. **A. americanum bites are biologically distinct from Lyme transmission**
   Lone star tick saliva is borreliacidal in vitro, with fewer than 13% of exposed *B. burgdorferi* surviving after 48 hours in one experiment (PMID:15752182). This does not explain STARI, but it strongly supports that A. americanum bites do not simply reproduce classic Lyme transmission biology.

3. **STARI is biochemically distinct from early Lyme disease**
   Human-serum metabolomics differentiated early Lyme disease from STARI with high accuracy and concluded that the two illnesses are metabolically dissimilar (PMID:28814545). This is strong evidence that STARI is a distinct host-response state even though the upstream trigger remains unresolved.

4. **Tick salivary toxins remain a hypothesis, not an established mechanism**
   A 2018 review/case report series proposed that tick salivary toxins may contribute to EM-like rashes and laboratory abnormalities, but this should be captured only as a note-level hypothesis rather than a core pathophysiology claim (PMID:30129909).

## Geography and differential with Lyme disease

The geography follows the range of the lone star tick rather than the classic Lyme vectors. The metabolomics study states that STARI occurs where *Amblyomma americanum* is present, extending from central Texas/Oklahoma through the Midwest and eastward across the southern states and Atlantic coast into Maine, with overlap zones where Lyme disease and STARI are co-prevalent (PMID:28814545).

The 2018 New Jersey review is also useful for curation because it captures the historically reported concentration in southeastern Missouri and several southeastern states while noting east-coast expansion of the vector range (PMID:30129909).

The 2022 review provides the clearest high-level differential diagnosis framing: STARI is a condition causing a similar lesion after a tick bite but of unknown cause (PMID:36116832). This paper is also excellent support for the statement that **no laboratory tool exists to diagnose STARI or differentiate it from Lyme disease**.

## Clinical phenotype and course

The 2005 prospective Missouri versus New York comparison remains the key paper for disease-level phenotype and prognosis claims (PMID:16142659):

- Missouri patients were **less likely to be symptomatic** than New York early Lyme patients.
- Missouri lesions were **smaller**, **more circular**, and **more likely to have central clearing**.
- Missouri patients were **less likely to have multiple lesions**.
- After antibiotic treatment, Missouri patients **recovered more rapidly** than New York patients.

The metabolomics paper complements this by summarizing the usual mild systemic symptoms: fatigue, fever, headache, and muscle/joint pains in addition to the EM-like lesion (PMID:28814545).

These findings justify modeling STARI as a primarily **localized rash-predominant illness with mild constitutional symptoms and a more favorable short-term course than comparator early Lyme disease**, while avoiding strong claims about long-term complications because the available abstract-level evidence is limited.

## Practical curation takeaways

- Use a **close MONDO match** to MONDO:0025294 with tracked issue #9873.
- Add an **exact NCIT mapping** to NCIT:C128427.
- Do **not** assert a specific infectious agent.
- Keep the mechanistic story conservative:
  - unknown etiology
  - non-Lyme biologic context of lone star tick bites
  - metabolically distinct from early Lyme disease
- Use Lyme disease as the primary differential diagnosis.
- Prefer the 2005 Missouri/New York paper and the 2025 CDC-associated outcomes paper for concise disease-level evidence.

## References

- MONDO NTR issue: https://github.com/monarch-initiative/mondo/issues/9873
- PMID:15668867
- PMID:15752182
- PMID:16142659
- PMID:28814545
- PMID:30129909
- PMID:36116832
- PMID:40517644
