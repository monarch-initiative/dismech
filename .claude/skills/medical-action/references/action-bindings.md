# Action terms, devices, agents, and regimens

### Treatment Terms (NCIT)
Treatments are annotated with NCI Thesaurus (NCIT) clinical-intervention terms, all
reachable from `NCIT:C25218` (Clinical Intervention or Procedure). (The Medical Action
Ontology / MAXO was removed from dismech; every former MAXO treatment/diagnosis term was
remapped to its NCIT equivalent.) Use the most specific and accurate NCIT term for the
treatment; when NCIT has no suitable clinical-action term, omit `term:` and keep a
free-text `preferred_term`.

```yaml
# NCIT treatment example
treatments:
- name: Physical Therapy
  description: Rehabilitation exercises to improve mobility.
  treatment_term:
    preferred_term: physical therapy
    term:
      id: NCIT:C15302
      label: Physical Therapy

# A more specific NCIT procedure term
treatments:
- name: Orthopedic Surgery
  description: Corrective surgery for skeletal deformities.
  treatment_term:
    preferred_term: orthopedic surgical procedure
    term:
      id: NCIT:C16186
      label: Orthopedic Surgical Procedure
```

Common NCIT clinical intervention terms:
- `NCIT:C15986` - Pharmacotherapy (drug treatments)
- `NCIT:C15632` - Chemotherapy
- `NCIT:C49236` - Therapeutic Procedure
- `NCIT:C15329` - Surgical Procedure
- `NCIT:C16186` - Orthopedic Surgical Procedure
- `NCIT:C15302` - Physical Therapy
- `NCIT:C15238` - Gene Therapy
- `NCIT:C15240` - Genetic Counseling
- `NCIT:C15447` - Dietary Intervention
- `NCIT:C15313` - Radiation Therapy
- `NCIT:C15289` - Organ Transplantation
- `NCIT:C15315` - Rehabilitation
- `NCIT:C15747` - Supportive Care

Use OAK to search for terms:
```bash
uv run runoak -i sqlite:obo:ncit info "l^Physical Therap"
```

**Devices are not clinical actions, and NCIT has terms for both.** `TreatmentActionTerm` is
rooted at `NCIT:C25218` (Clinical Intervention or Procedure), so a term naming the
*equipment* cannot be the `term:` of a `TreatmentDescriptor`, no matter how exactly it matches
the treatment's name. The worked case is cochlear implantation: `NCIT:C157820` "Cochlear
Implant" is the obvious term, is defined as "a two part electronic device...", and has
**no** `C25218` ancestor. Bind the clinical action instead — `NCIT:C15329` (Surgical
Procedure) for the implantation itself — and carry the specificity in `preferred_term`
(`cochlear device implantation`). This is the case the
[Ontology Term Contract](../../../../CLAUDE.md#ontology-term-contract) covers — `preferred_term` may be more
specific than the best available ontology term — and it generalizes: hearing aids,
pumps, stents, and shunts all have NCIT device terms that cannot sit in that slot.

**Better still, keep the device term queryable.** `preferred_term` is free text, so
binding the action alone throws the device concept away. Attach it as a `qualifiers`
predicate-value pair instead — `NCIT:C16830` (Medical Device) as the predicate,
the device term as the value — which validates today and leaves `NCIT:C157820`
searchable. `qualifiers` is deprecated for the common clinical qualifiers that have
dedicated slots (see [Descriptor Qualifier Slots](../../dismech-terms/references/descriptors.md)), but a
device attached to an action is exactly the predicate-value pattern that section
reserves it for, so this use is the carve-out and not a regression:

```yaml
  treatment_term:
    preferred_term: cochlear device implantation
    term:
      id: NCIT:C15329
      label: Surgical Procedure
    qualifiers:
    - predicate:
        preferred_term: medical device
        term:
          id: NCIT:C16830
          label: Medical Device
      value:
        preferred_term: cochlear implant
        term:
          id: NCIT:C157820
          label: Cochlear Implant
```

Worked examples: `Labyrinthitis`, `Otofacial_Neurodevelopmental_Syndrome`,
`Autosomal_Recessive_Nonsyndromic_Hearing_Loss_104`,
`Jervell_and_Lange-Nielsen_Syndrome_1`.

Two things follow that are easy to get wrong:

- **When the binding is broader than the treatment, `preferred_term` must not echo the
  ontology label.** A treatment named `Cochlear Implantation and Auditory Rehabilitation`
  bound to `NCIT:C15315` whose `preferred_term` is just `Rehabilitation` has thrown away
  every bit of information the binding lost. This is *not* a rule against ever matching
  the label: where the term already says what the treatment is, echoing it is correct
  and is what `dismech-terms` recommends (`preferred_term: Pharmacotherapy` against
  `NCIT:C15986` is right). The test is whether the label is narrower than, or as narrow
  as, the treatment being described.
- **A divergent binding is not automatically drift.** A treatment that bundles
  amplification *or* implantation *with* rehabilitation is genuinely a rehabilitation
  intervention, and one whose disease has no reported surgical case should not assert
  a surgical term. Check what the treatment actually is before normalizing it to the
  majority binding, and record the reason in `notes` when you leave one alone.

#### Therapeutic Agent Pattern (drug + drug class on pharmacotherapy)

Treatment terms describe the **medical action** (e.g., Pharmacotherapy, chemotherapy,
vaccination) but not the specific agent involved. When the action is generic but a
specific drug or drug class is involved, combine the generic treatment term with the
`therapeutic_agent` slot, which is multivalued and bindable to CHEBI (for specific drugs)
or NCIT (for drug classes).

**When to use `therapeutic_agent`:**
- `treatment_term` is a generic action like `NCIT:C15986` (Pharmacotherapy),
  `NCIT:C15632` (chemotherapy), `NCIT:C15346` (vaccination), or `NCIT:C15313` (radiation therapy)
- A specific drug, chemical, or drug class is referenced in the `name` / `description`
- You want the treatment to be machine-queryable by drug identity

**Ontology selection:**
- **CHEBI**: preferred for specific small-molecule drugs (`CHEBI:36796` duloxetine, `CHEBI:46345` 5-fluorouracil)
- **NCIT**: use for drug classes, or for biologics/newer drugs that lack a CHEBI term
  (`NCIT:C20401` Monoclonal Antibody, `NCIT:C2322` Corticosteroid, `NCIT:C65216` Adalimumab)
- Leave `therapeutic_agent` absent when the treatment is non-pharmacological
  (surgery, physical therapy, counseling, dietary intervention — use `dietary_modifications` for the latter)

**Example — single specific drug (CHEBI):**
```yaml
treatments:
- name: Duloxetine
  description: SNRI, FDA-approved for fibromyalgia chronic pain management.
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: duloxetine
      term:
        id: CHEBI:36796
        label: duloxetine
```

**Example — drug class (NCIT) when CHEBI is too specific:**
```yaml
treatments:
- name: Anti-TNF Biologic Therapy
  description: TNF inhibitors such as adalimumab or infliximab.
  treatment_term:
    preferred_term: anti-TNF biologic therapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: monoclonal antibody
      term:
        id: NCIT:C20401
        label: Monoclonal Antibody
```

**Example — combination therapy (multivalued):**
```yaml
treatments:
- name: FOLFIRINOX
  description: Combination chemotherapy regimen for pancreatic adenocarcinoma.
  treatment_term:
    preferred_term: chemotherapy
    term:
      id: NCIT:C15632
      label: Chemotherapy
    therapeutic_agent:
    - preferred_term: fluorouracil
      term:
        id: CHEBI:46345
        label: 5-fluorouracil
    - preferred_term: irinotecan
      term:
        id: CHEBI:80630
        label: irinotecan
    - preferred_term: oxaliplatin
      term:
        id: CHEBI:31941
        label: oxaliplatin
```

**Guidelines:**
- `therapeutic_agent` is optional at the schema level but **recommended whenever `treatment_term` is NCIT:C15986** or another generic action term where a specific drug is involved.
- Use OAK to verify CHEBI terms: `uv run runoak -i sqlite:obo:chebi search "duloxetine"`
- For NCIT drug-class terms, the local `ncit` adapter is configured in `conf/oak_config.yaml`.
- A dedicated `treatment.name` (e.g., "Duloxetine") should still match common clinical usage; `therapeutic_agent` carries the machine-readable identifier.
- Do NOT put the drug name in `preferred_term` on `treatment_term` — `preferred_term` describes the action (Pharmacotherapy), `therapeutic_agent.preferred_term` describes the agent.

#### Named Combination Regimens (`regimen_term`)

`regimen_term` is a **third, distinct** treatment slot — not an alternative spelling of
`treatment_term` or `therapeutic_agent`. Use it only when the treatment follows an
established, **named multi-drug protocol** that itself has an NCIT identity (e.g.
FOLFIRINOX, ABVD, R-CHOP, CHOP). It is bound to the `RegimenTerm` dynamic enum, reachable
only from `NCIT:C15697` (Treatment Regimen) / `NCIT:C62634` (Chemo/immuno/hormone Therapy
Regimen) — generic drug-class terms (e.g. `NCIT:C66930` Angiotensin II Receptor
Antagonist) are **not** reachable from that root and will fail validation if used here;
those belong in `therapeutic_agent` instead.

**How the three slots divide the work:**
- `treatment_term`: the medical action/modality (e.g. `NCIT:C15632` chemotherapy, `NCIT:C15986` Pharmacotherapy)
- `therapeutic_agent`: the individual drug(s) or drug class(es) involved
- `regimen_term`: the named combination protocol itself, when one exists

```yaml
treatments:
- name: ABVD-Based Chemotherapy
  treatment_term:
    preferred_term: chemotherapy
    term:
      id: NCIT:C15632
      label: Chemotherapy
    therapeutic_agent:
    - preferred_term: doxorubicin
      term:
        id: CHEBI:28748
        label: doxorubicin
    - preferred_term: bleomycin
      term:
        id: CHEBI:22907
        label: bleomycin
    - preferred_term: vinblastine
      term:
        id: CHEBI:27375
        label: vincaleukoblastine
    - preferred_term: dacarbazine
      term:
        id: CHEBI:4305
        label: dacarbazine
  regimen_term:
    preferred_term: ABVD regimen
    term:
      id: NCIT:C9509
      label: ABVD Regimen
```

Leave `regimen_term` absent when the treatment is monotherapy or an ad hoc/unnamed drug
combination — do not invent a regimen identity that OAK can't verify. Worked examples:
`Pancreatic_Ductal_Adenocarcinoma` (FOLFIRINOX), `Classic_Hodgkin_Lymphoma` (ABVD),
`Diffuse_Large_B_Cell_Lymphoma` (R-CHOP), `Peripheral_T_Cell_Lymphoma` (CHOP),
`BRAF_V600E_Mutant_Colorectal_Cancer` (FOLFOXIRI, curated against the closest available
NCIT term, `Folfirinox Regimen`, since NCIT does not separately code the FOLFOXIRI name).
