---
provider: claude
model: claude-sonnet-4-6
cached: false
start_time: '2026-06-14T00:00:00Z'
end_time: '2026-06-14T00:30:00Z'
duration_seconds: 1800
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dyslexia
  mondo_id: MONDO:0005489
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 10
---

## Question

# Disease Pathophysiology Research — Dyslexia (MONDO:0005489)

Focus: content-completeness sweep covering alternative mechanistic hypotheses,
spelling/visual processing phenotypes, diagnostic criteria, and comorbidity
structure — areas flagged as gaps in the current dismech entry.

---

## 1. Alternative Mechanistic Hypotheses

### 1a. Phonological Processing Deficit (dominant account)

Developmental dyslexia's core deficit is widely considered to be a phonological
processing impairment — specifically reduced phonological awareness, impaired
phonological memory, and slow phonological retrieval (naming speed). This
account is supported by converging evidence from cognitive, neuroimaging, and
genetic studies. Left-hemisphere reading-network dysfunction (occipito-temporal /
visual word form area, inferior frontal gyrus, angular gyrus) is the systems-level
correlate (Richlan 2012, PMID:22557962; Paulesu et al. 2014, PMID:25426043).

### 1b. Magnocellular/Dorsal-Stream Hypothesis

Stein and colleagues proposed that dyslexia arises from impaired development of the
magnocellular layers of the lateral geniculate nucleus and the dorsal visual stream,
causing unstable binocular control and impaired temporal visual processing. This
was proposed to underlie difficulties with tracking letters across a page.

Evidence for this account is mixed. Some studies show reduced magnocellular VEP
responses in dyslexic readers; others find the deficits are secondary to phonological
impairment. The magnocellular hypothesis has not achieved consensus acceptance. It
remains a complementary rather than competing hypothesis.

Key reference: Stein J, Walsh V (1997) "To see but not to read; the magnocellular
theory of dyslexia." Trends Neurosci 20(4):147-52. (PMID:9106353 — verify before
curating in YAML evidence)

### 1c. Cerebellar/Automaticity Hypothesis

Nicolson and Fawcett proposed that dyslexia reflects impaired cerebellar function,
leading to deficient automatization of cognitive and motor skills — including
phonological processing. Evidence: dyslexic children show impaired balance, motor
learning, and eye movement control consistent with cerebellar dysfunction.

Neuroimaging studies show reduced cerebellar activation during reading tasks in
dyslexic individuals. However, cerebellar deficits may represent an epiphenomenon
of broader automatization failure rather than a primary cause.

Key reference: Nicolson RI, Fawcett AJ, Dean P (2001) "Developmental dyslexia:
the cerebellar deficit hypothesis." Trends Neurosci 24(9):508-11.
(PMID:11509484 — verify before curating in YAML evidence)

### 1d. Double-Deficit Hypothesis

Wolf and Bowers (1999) proposed that dyslexia reflects deficits in phonological
awareness AND rapid automatized naming (RAN) as independent dimensions, with
double-deficit cases being the most severe. RAN captures a timing/automaticity
dimension not fully captured by phonological awareness alone.

This account is empirically well-supported and clinically useful for subtyping.
It is compatible with both the phonological and cerebellar accounts.

---

## 2. Phenotypes Not Yet Modeled

### 2a. Spelling impairment

Persistent spelling difficulties are universal in dyslexia and often more severe
and enduring than the reading impairment. Spelling impairment (HP:0002167 or
more specific) should be considered for formal curation as a phenotype alongside
reading difficulty.

### 2b. Writing difficulties

Handwriting and written composition difficulties frequently co-occur with dyslexia,
partly via dysgraphia comorbidity and partly due to shared orthographic demands.
These are documented in clinical reviews but under-represented in mechanistic entries.

### 2c. Visual processing / orthographic processing

Some individuals with dyslexia have difficulty with the rapid visual recognition of
printed word forms (orthographic processing deficit) independently of phonological
impairment. This supports a role for the visual word form area (VWFA, left
fusiform/occipito-temporal sulcus) in dyslexia. Paulesu et al. (PMID:25426043)
document this dimension via neuroimaging meta-analysis.

---

## 3. Diagnostic Criteria

DSM-5 (APA 2013) requires:
- Persistent difficulties reading for ≥6 months despite intervention
- Performance below age expectations in reading accuracy, fluency, or comprehension
- Onset in school-age
- Not better explained by intellectual disability, vision/hearing problems,
  inadequate instruction, or psychosocial adversity

ICD-11 F81.0 (specific reading disorder) uses similar criteria. Formal diagnostic
evaluation typically includes standardized reading assessments, IQ testing, and
exclusion criteria.

---

## 4. Comorbidity Structure

Dyslexia co-occurs frequently with:

### 4a. ADHD (~30-40% comorbidity)

Shared polygenic genetic architecture (some GWAS loci overlap). ADHD and dyslexia
interact to worsen educational outcomes, but can be dissociated cognitively.
Dyslexia is primarily a phonological/reading disorder; ADHD is primarily an
executive/attention disorder.

### 4b. Developmental Language Disorder (DLD)

Snowling et al. (PMID:31631348) followed children with dyslexia, DLD, and comorbid
dyslexia+DLD. The comorbid group had the most severe reading comprehension deficits.
Dyslexia-only was associated with decoding failures; DLD-only with oral language
comprehension failures. The comorbid group required different forms of intervention
than either condition alone. DLD co-occurs in approximately one-third of dyslexia cases.

Bishop (PMID:30458538) reviews the relationship between DLD and dyslexia:
both involve language-processing difficulties, but with different profiles at
the core.

### 4c. Dyscalculia

Mathematical learning difficulties co-occur in approximately 40% of dyslexia cases,
though the relationship is domain-general (working memory / attention) rather
than phonological.

---

## 5. Evidence Gaps and Curation Recommendations

1. **Magnocellular and cerebellar nodes**: Not yet formally curated as pathophysiology
   nodes with evidence. Both hypotheses have peer-reviewed support but remain
   secondary to the phonological account. Candidate for separate pathophysiology
   nodes with explicit `mechanistic_hypotheses` alternative groups.

2. **Spelling/writing phenotypes**: Could be added with HP:0002167 (Agraphia) or
   more specific HP terms.

3. **ADHD comorbidity section**: Currently noted in phenotypes as a comorbidity
   but not structured in a `comorbidities:` block.

4. **Diagnostic criteria section**: Not yet in the entry. Could be added under a
   `diagnosis:` block following schema conventions.

5. **Speech-language therapy**: Evidence for this as a standalone dyslexia
   intervention is primarily indirect (via DLD literature). Snowling et al.
   (PMID:31631348) note that comorbid dyslexia+DLD requires different intervention
   than dyslexia alone. Not yet curated as a formal treatment entry.

---

## Key PMIDs for Curator Verification

| PMID | Title | Relevance |
|------|-------|-----------|
| PMID:22557962 | Richlan 2012 — Left hemisphere reading network | Already in entry |
| PMID:25426043 | Paulesu 2014 — Neuroimaging meta-analysis | Already in entry |
| PMID:31631348 | Snowling 2020 — Dyslexia and DLD comorbidity | Comorbidity section |
| PMID:30458538 | Bishop 2020 — DLD and dyslexia | Comorbidity section |
| PMID:9106353 | Stein & Walsh 1997 — Magnocellular theory | Verify before YAML use |
| PMID:11509484 | Nicolson et al. 2001 — Cerebellar hypothesis | Verify before YAML use |

**NOTE**: PMIDs marked "verify before YAML use" were identified from literature
background knowledge; curators must run `just fetch-reference PMID:XXXXXXXX`
and verify snippet availability before citing in YAML evidence blocks.
