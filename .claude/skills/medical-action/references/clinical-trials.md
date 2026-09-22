# Clinical trial records

Examples illustrate the record structure. Read the current registry record for
the actual trial's phase, status, and evidence before curating it.

### Clinical Trials

Clinical trials can be added to disease entries with evidence validated against ClinicalTrials.gov:

```yaml
clinical_trials:
- name: NCT05813288
  phase: PHASE_III
  status: COMPLETED
  description: Brief description of the trial's objective and approach
  target_phenotypes:
    - preferred_term: Wheezing
      term:
        id: HP:0030828
        label: Wheezing
    - preferred_term: Breathlessness
      term:
        id: HP:0002094
        label: Dyspnea
  evidence:
    - reference: clinicaltrials:NCT05813288
      supports: SUPPORT
      snippet: "Exact quote from the trial summary"
      explanation: "Why this trial is relevant to the disease"
```

**Fetching trial data:**
```bash
just fetch-reference NCT05813288  # Caches trial data from ClinicalTrials.gov API
```

#### Trials not registered on ClinicalTrials.gov (`ICTRP:`)

A trial registered on ChiCTR, ISRCTN, EUCTR, jRCT/UMIN, CTRI, ANZCTR, IRCT, or
any other WHO primary registry has no NCT identifier. Key it on its **WHO ICTRP**
identifier and cite the ICTRP record — one prefix covers every primary registry,
because ICTRP is the umbrella that normalizes them (24-element WHO Trial
Registration Data Set). Do **not** bury the identifier in `description:`/`notes:`
prose or wedge it into a free-text `name`; nothing validates either form.

```bash
just ictrp-fetch ChiCTR2100045397        # → references_cache/ICTRP_ChiCTR2100045397.md
just fetch-reference ICTRP:ISRCTN67795930  # equivalent
just ictrp-audit                          # registry IDs still stranded in prose
```

```yaml
clinical_trials:
- name: ISRCTN67795930
  phase: PHASE_III
  status: COMPLETED
  evidence:
  - reference: ICTRP:ISRCTN67795930
    supports: SUPPORT
    evidence_source: OTHER          # a registration document, not study evidence
    snippet: "| Register | ISRCTN |"
    explanation: WHO ICTRP registration record establishing the trial's identity.
```

Each `## Registration` table row is a stable quotable substring (pipes optional,
as with ORPHA/ICEES rows). Investigator contact details are deliberately excluded
from the cache. The portal returns its "not found" page with **HTTP 200**, so a
malformed identifier is caught by the fetcher, not by a status code — this is how
a nonexistent `ChiCTR-2100045397` (hyphenated, and mislabeled "Clinicaltrials.gov"
in the publication itself) was found in `Progressive_Supranuclear_Palsy`. Never
"correct" an identifier inside an evidence `snippet:`; that quote belongs to the
cited paper. Worked examples: `Progressive_Supranuclear_Palsy` (ChiCTR),
`Ectopic_Pregnancy` (ISRCTN). See [`docs/ictrp.md`](../../../../docs/ictrp.md).

**Key fields:**
- `name`: NCT identifier (e.g., NCT05813288)
- `phase` (`ClinicalTrialPhaseEnum`): `PHASE_I`, `PHASE_II`, `PHASE_III`, `PHASE_IV`, or
  `NOT_APPLICABLE` (observational or device studies that do not follow the standard FDA
  phase classification)
- `status` (`ClinicalTrialStatusEnum`): `RECRUITING`, `NOT_RECRUITING`,
  `ACTIVE_NOT_RECRUITING`, `COMPLETED`, `ENROLLING_BY_INVITATION`, `SUSPENDED`,
  `TERMINATED`, `WITHDRAWN`, or `UNKNOWN`
- `target_phenotypes`: Phenotypes addressed by the trial (with HP ontology terms)
- `evidence`: Evidence items validated against ClinicalTrials.gov

**These are enum values, not free text.** Write `phase: PHASE_III`, not `Phase III`, and
`status: COMPLETED`, not `Completed` — the schema binds both slots to enums via
`ClinicalTrial` `slot_usage`, so the prose spellings fail `just validate`. Note the enum
*descriptions* in the schema render as "Phase III - Efficacy confirmation…", which is what
makes the free-text form look plausible; the permissible value is the upper-snake-case key.
