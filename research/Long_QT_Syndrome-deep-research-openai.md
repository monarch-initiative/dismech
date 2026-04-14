---
provider: openai
model: gpt-5
generated_at: '2026-04-14T05:37:14Z'
disease_name: Long QT Syndrome
mondo_id: MONDO:0002442
scope: inherited/familial long QT syndrome root curation
---

# Deep Research Notes: Long QT Syndrome

## Scope Decision

- Curate the disease root at `MONDO:0002442` (`long QT syndrome`) rather than
  splitting the canonical subtype series into separate disorder files.
- Keep the narrative explicitly inherited/familial so the entry does not absorb
  acquired QT prolongation.
- Exclude already distinct syndromic or gene-specific entities from this root:
  `Jervell and Lange-Nielsen syndrome` and `ANK2 ankyrin-B syndrome`
  (historical `LQT4`).

## Key PMID-Backed Quotes Used for Curation

- `PMID:18606002`
  - "Congenital long QT syndrome (LQTS) is a hereditary cardiac disease characterized by a prolongation of the QT interval at basal ECG and by a high risk of life-threatening arrhythmias."
  - "Disease prevalence is estimated at close to 1 in 2,500 live births."
  - "The two cardinal manifestations of LQTS are syncopal episodes, that may lead to cardiac arrest and sudden cardiac death, and electrocardiographic abnormalities, including prolongation of the QT interval and T wave abnormalities."
  - "Treatment should always begin with beta-blockers, unless there are valid contraindications."
  - "If the patient has one more syncope despite a full dose beta-blockade, left cardiac sympathetic denervation (LCSD) should be performed without hesitation and implantable cardioverter defibrillator (ICD) therapy should be considered"

- `PMID:24093767`
  - "Congenital long QT syndrome (LQTS) is a genetically heterogeneous group of heritable disorders of myocardial repolarization linked by the shared clinical phenotype of QT prolongation on electrocardiogram and an increased risk of potentially life-threatening cardiac arrhythmias."

- `PMID:10348966`
  - "The majority of cases are inherited by autosomal dominant transmission."
  - "The primary electrophysiologic disturbance is delayed recovery of the action potential, because of diverse physiologic perturbations dependent upon the specific ion channel and mutation."
  - "The delayed recovery predisposes individuals to the development of early afterdepolarizations and initiation of torsade de pointes arrhythmias."
  - "The torsade produces the syncope and sudden death."
  - "The principal treatment is beta-blocker therapy."

- `PMID:28670758`
  - "A prolonged QT interval in the surface electrocardiogram is the sine qua non of the LQTS and is a surrogate measure of the ventricular action potential duration (APD)."
  - "This together with the tendency of prolonged APD to be associated with oscillations at the plateau level, termed early afterdepolarizations (EADs), provides the substrate of ventricular tachyarrhythmia associated with LQTS, usually referred to as torsade de pointes (TdP) VT."

- `PMID:11136691`
  - "LQT1 patients experienced the majority of their events (62%) during exercise, and only 3% occurred during rest/sleep. These percentages were almost reversed among LQT2 and LQT3 patients, who were less likely to have events during exercise (13%) and more likely to have events during rest/sleep (29% and 39%)."

- `PMID:10673253`
  - "beta-blockers are associated with a significant reduction in cardiac events in LQTS patients."
  - "However, syncope, aborted cardiac arrest, and LQTS-related death continue to occur while patients are on prescribed beta-blockers"

- `PMID:10377081`
  - "Two-electrode voltage-clamp recordings of a recombinant E1784K mutant channel expressed in Xenopus oocytes revealed a defect in fast inactivation characterized by a small, persistent current during long membrane depolarizations."
  - "The functional defect exhibited by the mutant channel causes delayed myocardial repolarization"

- `PMID:26940925`
  - "Besides shortening QTc interval, mexiletine caused a major reduction of life-threatening arrhythmic events in LQT3 patients, thus representing an efficacious therapeutic strategy."

- `PMID:9272508`
  - "The familial long QT syndrome (LQTS) is now recognized as a genetic channelopathy with a propensity to arrhythmogenic syncope and sudden death."

## Mechanistic Model Selected for YAML

1. Reduced repolarizing potassium current
   - Root node for the common KCNQ1/KCNH2-dominant branches.
   - Ontology terms:
     - `GO:0071805` potassium ion transmembrane transport
     - `GO:0086013` membrane repolarization during cardiac muscle cell action potential
     - `CL:0000746` cardiac muscle cell
     - `UBERON:0000948` heart

2. Persistent late sodium current in LQT3
   - Explicit subtype-aware branch retained because it has a clean precision-therapy
     hook to mexiletine.
   - Ontology terms:
     - `GO:0035725` sodium ion transmembrane transport
     - `GO:0086013` membrane repolarization during cardiac muscle cell action potential

3. Prolonged ventricular repolarization and early afterdepolarizations
   - Common convergent substrate downstream of potassium-current loss or late
     sodium current gain.
   - Ontology terms:
     - `GO:0086001` cardiac muscle cell action potential
     - `GO:0086013` membrane repolarization during cardiac muscle cell action potential

4. Adrenergic trigger susceptibility
   - Retained to justify beta-blockers and LCSD at the disease root while still
     preserving subtype-specific trigger heterogeneity.

5. Torsades de pointes and sudden cardiac death
   - Final mechanistic-output node connecting the repolarization substrate to the
     defining clinical risks.

## Subtype and Lumping Rationale

- Keep `Type 1`, `Type 2`, and `Type 3` as `has_subtypes` because they are the
  canonical clinically meaningful series directly referenced in LQTS practice.
- Do not create separate disorder files here for the subtype series; keep them
  nested under the root because this issue asked for a disease-level inherited
  LQTS entry and the repo’s prioritizer tests explicitly treat `long QT syndrome`
  as a broad parent that should absorb subtype rows.
- Do not pull `Jervell and Lange-Nielsen syndrome` into this root because it is a
  recessive syndromic deafness-associated entity with a distinct MONDO term and
  clinical framing.
- Do not pull `ANK2`/historical `LQT4` into this root because the repo already
  has a curated `ANK2_Ankyrin_B_Syndrome.yaml` entry documenting why it is not
  classic long QT syndrome.

## Treatment Choices Kept in Scope

- `Beta-Blocker Therapy`: first-line disease-root treatment.
- `Left Cardiac Sympathetic Denervation`: escalation for recurrent syncope on
  full-dose beta-blockade.
- `Implantable Cardioverter-Defibrillator Placement`: high-risk rescue/device
  therapy.
- `Mexiletine`: kept as a subtype-targeted treatment because the root entry
  still needs one precision-therapy example tied to the LQT3 mechanism.
