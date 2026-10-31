# Mechanism-Based Disease Classes for MONDO, Round 2: Four New Proposals and a Status Update

**Date:** 2026-10-23
**Builds on:** [`mondo-mechanism-classification-proposal-2026-08-01.md`](mondo-mechanism-classification-proposal-2026-08-01.md) (round 1, PR #7800)
**Scope:** proposal only. No MONDO edits and no new-term requests have been filed.

## Summary

Round 1 proposed ten mechanism-based classes for MONDO's
`MONDO:7770011 disease by molecular mechanism` branch, each backed by a dismech
mechanism module and a dismech grouping. None of the ten has been created in MONDO
since, and the evidence behind every one of them has grown: each module now has
more conforming entries than it did in August.

Re-running the round-1 selection over the current module set (198 modules,
against 118 in August) finds four further classes that MONDO does not have:

| Proposal | Proposed label | dismech module | Germline members in dismech | MONDO hits (label / synonym / definition) |
|---|---|---|---|---|
| 11 | membrane contact site disorder | `membrane_contact_site_dysfunction` | 9 | 0 / 0 / 1 |
| 12 | mTORopathy | `mtorc1_hyperactivation` | 8 | 0 / 0 / 1 |
| 13 | Mendelian disorder of the epigenetic machinery | `epigenetic_machinery_neurodevelopmental_dysregulation` | 26 | 0 / 0 / 0 |
| 14 | hereditary desmosomopathy | `desmosomal_adhesion_failure` | 7 | 0 / 0 / 2 |

Numbering continues from round 1 so that "proposal 3" always means the same class.
The definition-text hits are single diseases whose definitions mention the
mechanism; they are listed under each proposal and none is a class.

Each proposal has a backing dismech grouping, so membership can be audited with
`just check-groupings` before anything goes to MONDO:
`Membrane_Contact_Site_Disorders` (proposal 11), `mTORopathies` (12),
`Mendelian_Disorders_of_the_Epigenetic_Machinery` (13) and
`Hereditary_Desmosomopathies` (14).

## 1. Status of the round-1 proposals

Checked against MONDO release 2026-10-06 (see section 5 for the snapshot).

| Proposal | Proposed label | In MONDO? | Conformers, Aug 2026 | Conformers, Oct 2026 |
|---|---|---|---|---|
| 1 | intoxication-type inborn error of metabolism | no | 19 | 24 |
| 2 | cardiac channelopathy | no | 12 | 21 |
| 3 | FGFR-opathy | no | 11 | 15 |
| 4 | synaptic vesicle cycle disorder | no | 9 | 13 |
| 5 | centrosomopathy | no | 8 | 12 |
| 6 | meiotic recombination failure disorder | no | 7 | 14 |
| 7 | Hedgehog pathway activation disease | no | 5 | 6 |
| 8 | polyglutamine expansion disease | no | 4 | 8 |
| 9 | macroautophagy deficiency disorder | no | 5 | 15 |
| 10 | BBSome-opathy | no | 3 | 3 |

Conformers are distinct `kb/disorders/` and `kb/comorbidities/` files declaring
`conforms_to` against the proposal's module, the same metric as round 1. A rise in
conformers is not by itself a rise in germline members; for proposal 9 in
particular, re-check which of the 15 are monogenic macroautophagy disorders before
filing, as round 1's scoping note asked.

**One change on the MONDO side.** The mechanism branch now has six direct
children, not five. The new one is `MONDO:1060233 Mediator complex-related
neurodevelopmental disorder`, a class defined by a shared molecular machine
rather than a phenotype. It is a close precedent for proposals 11 and 13.

| Direct children of `MONDO:7770011` (2026-10-06) |
|---|
| `MONDO:0005308` ciliopathy |
| `MONDO:0005574` tauopathy |
| `MONDO:0019119` muscular channelopathy |
| `MONDO:0021060` RASopathy |
| `MONDO:0021179` proteostasis deficiencies |
| `MONDO:1060233` Mediator complex-related neurodevelopmental disorder |

## 2. How the new candidates were selected

The method is round 1's, section 2, unchanged except for one added step.

1. **Rank modules** by the number of distinct disorder files conforming to them.
2. **Keep mechanism families.** Drop modules that describe a phenotype, a
   physiological response or a drug mechanism (fibrotic response, seizure
   excitation-inhibition imbalance, antibiotic targets) rather than a shared
   molecular lesion.
3. **Exclude on an exact or near-synonym MONDO match** in any of three passes:
   labels, all synonym types, and `IAO:0000115` definitions. Adjacent partial
   matches do not exclude but are disclosed.
4. **New this round: count germline members only.** Some modules mix hereditary
   and acquired conformers; the JAK-STAT module, for example, includes
   myeloproliferative neoplasms and lymphomas. A class under
   `MONDO:7770011` is about inherited molecular lesions, so each candidate's member
   list keeps only germline (Mendelian) conformers, and the rest are listed as
   excluded.

**Excluded because MONDO already has the class:**

| Candidate family | dismech module | MONDO class |
|---|---|---|
| type 1 interferonopathy | `innate_antiviral_interferon_response` | `MONDO:0700264 type 1 interferonopathy` |
| laminopathy | none | `MONDO:0021106 laminopathy` |
| telomere biology disorder | `telomere_attrition` | `MONDO:0800467 dyskeratosis congenita and related telomere biology disorder` |

**Excluded for other reasons:** `nlrp3_inflammasome_activation` (7 conformers,
mostly acquired: stroke, silicosis, multiple sclerosis, envenomation; the
hereditary member, familial cold autoinflammatory syndrome, is already under
MONDO's cryopyrin-associated periodic syndrome).

## 3. The four new proposals

### 3.1 Proposal 11: membrane contact site disorder

- **Proposed label:** membrane contact site disorder
- **Synonyms:** organelle contact site disorder; disorder of organelle tethering
- **Definition:** A hereditary disease caused by loss or mis-regulation of a
  protein that tethers two organelle membranes at a membrane contact site, or that
  transfers lipids or calcium across one, resulting in disturbed lipid supply
  between organelles, calcium transfer into mitochondria, or organelle
  morphology and position.
- **Logical definition:** textual only. Members fail at different steps: the
  tether itself (VAPB, ACBD5), lipid transfer across the contact (VPS13A, XK,
  CERT1) or calcium transfer (WFS1, PDZD8). A single
  `RO:0004021 basis_in_disruption_of_process` axiom on `GO:0120009 intermembrane
  lipid transfer` would exclude the calcium-transfer members, and one on
  `GO:0140056 organelle localization by membrane tethering` would exclude CERT1.
  The cellular component `GO:0044232 organelle membrane contact site` is the
  common factor, so a component-scoped axiom, as for proposal 10, would be the
  route if MONDO wants one.
- **Proposed parent:** `MONDO:7770011 disease by molecular mechanism`
- **Why it is a family:** contact sites are where organelles exchange lipids and
  calcium without vesicle traffic, and every organelle forms them
  (PMID:31732717). The disease genes encode the tethers and transfer proteins
  themselves, and the shared consequence is neural. Field definitions: PMID:30894536.
- **Members (dismech, all germline):**

  | MONDO | Disease | Gene | Organelle pair |
  |---|---|---|---|
  | `MONDO:0100112` | acyl-CoA binding domain containing protein 5 deficiency | ACBD5 | peroxisome-ER |
  | `MONDO:0008453` | adult-onset proximal spinal muscular atrophy, autosomal dominant | VAPB | ER to many partners |
  | `MONDO:0008695` | VPS13A-related neurodegenerative disease (chorea-acanthocytosis) | VPS13A | ER-mitochondria, ER-lipid droplet |
  | `MONDO:0018945` | XK-related neurodegenerative disease (McLeod syndrome) | XK | ER-plasma membrane |
  | `MONDO:0014599` | intellectual disability, autosomal dominant 34 | CERT1 | ER-Golgi |
  | `MONDO:0018105` | Wolfram syndrome | WFS1, CISD2 | ER-mitochondria |
  | `MONDO:0700293` | WFS1-related disorder | WFS1 | ER-mitochondria |
  | `MONDO:0859281` | intellectual developmental disorder with autism and dysmorphic facies | PDZD8 | ER-mitochondria, ER-lysosome |
  | `MONDO:0014601` | autosomal recessive spinocerebellar ataxia 20 | SNX14 | ER-lipid droplet |

  Candidates not yet in dismech or not yet conformed: MFN2-related
  Charcot-Marie-Tooth disease type 2A, SPG87 (TMEM63C), PACS2-related
  developmental and epileptic encephalopathy, Alkuraya-Kucinskas syndrome (BLTP1),
  VPS13B-related Cohen syndrome, VPS13C- and VPS13D-related disease.
- **MONDO gap evidence:** "membrane contact site", "organelle contact" and
  "lipid transfer" return no label or synonym hit. "contact site" appears only in
  the definition of `MONDO:0100112`, one of the members.
- **dismech provenance:** `kb/modules/membrane_contact_site_dysfunction.yaml`
  and `kb/groupings/Membrane_Contact_Site_Disorders.yaml` (9 members, all
  `SATISFIED` under a `NECESSARY` module-conformance criterion).

### 3.2 Proposal 12: mTORopathy

- **Proposed label:** mTORopathy
- **Synonyms:** mTORC1 hyperactivation disorder; GATORopathy (narrower: the
  GATOR1-complex members)
- **Definition:** A hereditary disease caused by a germline or mosaic variant in a
  regulator of the mTORC1 pathway that leaves mTORC1 constitutively active,
  typically producing focal cortical malformation, epilepsy, hamartomas or
  overgrowth.
- **Logical definition:** `RO:0004021 some GO:0038202 TORC1 signaling`. As round 1
  section 1 explains, `RO:0004021` does not encode the direction of the change,
  and the definition text carries "hyperactivation".
- **Proposed parent:** `MONDO:7770011 disease by molecular mechanism`
- **Why it is a family:** "mTORopathy" is established clinical usage for the
  disorders of TSC1/TSC2, PTEN, the GATOR1 complex (DEPDC5, NPRL2, NPRL3) and
  MTOR itself. They share focal cortical dysplasia, epilepsy responsive to mTOR
  inhibition, and somatic second-hit mosaicism.
- **Members (dismech, germline):**

  | MONDO | Disease | Gene |
  |---|---|---|
  | `MONDO:0001734` | tuberous sclerosis | TSC1, TSC2 |
  | `MONDO:0017623` | PTEN hamartoma tumor syndrome | PTEN |
  | `MONDO:0016063` | Cowden disease | PTEN |
  | `MONDO:0007924` | Bannayan-Riley-Ruvalcaba syndrome | PTEN |
  | `MONDO:0020310` | familial focal epilepsy with variable foci | DEPDC5, NPRL2, NPRL3 |
  | `MONDO:0000030` | familial sleep-related hypermotor epilepsy (DEPDC5 form) | DEPDC5 |
  | `MONDO:0014201` | developmental and epileptic encephalopathy, 18 | SZT2 |
  | `MONDO:0957960` | Long-Olsen-Distelmaier syndrome | RRAGC |

  Also in MONDO but not in dismech: `MONDO:0100572 MTOR-related overgrowth
  spectrum` and `MONDO:0976294 ragopathy`. Both are single diseases that would
  become children.

  Excluded from the member list: lymphangioleiomyomatosis and perivascular
  epithelioid cell neoplasm (TSC-associated neoplasms that also occur
  sporadically) and Peutz-Jeghers polyp (a lesion, not a disease).
  `DEPDC5-Related_Epilepsy` is also left out of the table, but only because its
  dismech entry is anchored to the broad `MONDO:0005384 focal epilepsy`,
  following ClinGen's lumping. It is a germline DEPDC5 disorder, so the GATOR1
  arm is better supported than the table alone shows. Boundary case: Peutz-Jeghers syndrome (STK11) acts through AMPK
  on mTORC1, and its defining features are polyposis and cancer risk rather than
  the cortical phenotype, so it is listed as a candidate for review rather than a
  member.
- **MONDO gap evidence:** "mTORopathy" and "GATORopathy" return nothing.
  "mTORC1" appears only in the definition of `MONDO:0976294 ragopathy`, a single
  syndrome under `MONDO:0002254 syndromic disease` with no children.
- **dismech provenance:** `kb/modules/mtorc1_hyperactivation.yaml` (13
  conforming files, 8 germline members) and
  `kb/groupings/mTORopathies.yaml`. The grouping has 9 members: the 8 above plus
  `DEPDC5-Related_Epilepsy`, whose broad MONDO anchor matters for a MONDO member
  list but not for dismech. Sleep-related hypermotor epilepsy is listed as its
  DEPDC5 subtype only.

### 3.3 Proposal 13: Mendelian disorder of the epigenetic machinery

- **Proposed label:** Mendelian disorder of the epigenetic machinery
- **Synonyms:** disorder of the epigenetic machinery; chromatinopathy
- **Definition:** A hereditary disease caused by a germline variant in a gene
  encoding a writer, eraser, reader or remodeler of chromatin marks or DNA
  methylation, typically presenting as intellectual disability with growth
  abnormality and characteristic facial features.
- **Logical definition:** `RO:0004021 some GO:0040029 epigenetic regulation of
  gene expression`
- **Proposed parent:** `MONDO:7770011 disease by molecular mechanism`
- **Why it is a family:** this is the largest new family by membership. The
  disorders share a dosage-sensitive chromatin regulator, overlapping
  neurodevelopmental phenotypes, and disease-specific DNA methylation signatures
  ("episignatures") that are used clinically to classify variants.
- **Members (dismech, all germline, 26).** Names are the common syndrome names;
  several MONDO labels are descriptive (for example `MONDO:0014558` is
  "autosomal dominant intellectual disability-craniofacial anomalies-cardiac
  defects syndrome"):
  `MONDO:0016980` ATR-X-related syndrome (ATRX);
  `MONDO:0014558` KAT6A syndrome;
  `MONDO:0015022` BRPF1 syndrome;
  `MONDO:0014205` ASXL3 deficiency (Bainbridge-Ropers syndrome);
  `MONDO:0032922` Beck-Fahrner syndrome (TET3);
  `MONDO:0010537` Borjeson-Forssman-Lehmann syndrome (PHF6);
  `MONDO:0014150` developmental and epileptic encephalopathy 94 (CHD2);
  `MONDO:0014017` CHD8 disorder;
  `MONDO:0015452` Coffin-Siris syndrome (ARID1B, SMARCA4, SMARCB1);
  `MONDO:0030012` Diets-Jongmans syndrome (KDM3B);
  `MONDO:0970951` El Hayek-Chahrour neurodevelopmental disorder (KDM5A);
  `MONDO:0020850` intellectual disability, autosomal recessive 65 (KDM5B);
  `MONDO:0014751` KDM1A disorder;
  `MONDO:0032790` KDM6B disorder;
  `MONDO:0015004` dystonia 28 (KMT2B);
  `MONDO:0016512` Kabuki syndrome (KMT2D, KDM6A);
  `MONDO:0012455` Kleefstra syndrome (EHMT1);
  `MONDO:0014791` Luscan-Lumish syndrome (SETD2);
  `MONDO:0011053` Nicolaides-Baraitser syndrome (SMARCA2);
  `MONDO:0032793` O'Donnell-Luria-Rodan syndrome (KMT2E);
  `MONDO:0019188` Rubinstein-Taybi syndrome (CREBBP, EP300);
  `MONDO:0014336` SETD5 haploinsufficiency;
  `MONDO:0019349` Sotos syndrome (NSD1);
  `MONDO:0010193` Weaver syndrome (EZH2);
  `MONDO:0011518` Wiedemann-Steiner syndrome (KMT2A);
  `MONDO:0016033` Cornelia de Lange syndrome (NIPBL).
- **Boundary to decide:** Cornelia de Lange syndrome is a cohesin disorder.
  Cohesin shapes chromatin architecture and the syndrome has an episignature, but
  it is also the founding member of the "cohesinopathies", which MONDO does not
  have either. It can stay here or seed a sibling class.
- **Candidates not yet in dismech:** Cohen-Gibson syndrome (`MONDO:0060510`,
  EED), a PRC2 disorder in the same family as Weaver syndrome.
- **MONDO gap evidence:** "epigenetic machinery", "chromatinopathy", "chromatin
  regulator" and "chromatin modifier" return nothing in any pass.
- **dismech provenance:**
  `kb/modules/epigenetic_machinery_neurodevelopmental_dysregulation.yaml`
  (26 conforming files, all germline) and
  `kb/groupings/Mendelian_Disorders_of_the_Epigenetic_Machinery.yaml` (26
  members).

### 3.4 Proposal 14: hereditary desmosomopathy

- **Proposed label:** hereditary desmosomopathy
- **Synonyms:** desmosomal disease; cardiocutaneous desmosomal disorder
  (narrower)
- **Definition:** A hereditary disease caused by a germline variant in a gene
  encoding a desmosomal protein, leading to loss of cell-cell adhesion in tissues
  under mechanical stress: skin, hair, oral mucosa and heart.
- **Logical definition:** `RO:0004021 some GO:0002934 desmosome organization`
- **Proposed parent:** `MONDO:7770011 disease by molecular mechanism`
- **Why it is a family:** desmoplakin, plakoglobin, desmoglein and plakophilin
  variants give an overlapping cardiocutaneous pattern of palmoplantar
  keratoderma, woolly hair and arrhythmogenic cardiomyopathy, and the skin and
  hair signs can flag the cardiac risk.
- **Members (dismech, germline):**

  | MONDO | Disease | Gene |
  |---|---|---|
  | `MONDO:0011017` | Naxos disease | JUP |
  | `MONDO:0011581` | arrhythmogenic cardiomyopathy with wooly hair and keratoderma | DSP |
  | `MONDO:0014355` | dilated cardiomyopathy with wooly hair, keratoderma, and tooth agenesis | DSP |
  | `MONDO:0011882` | skin fragility-woolly hair-palmoplantar keratoderma syndrome | DSP |
  | `MONDO:0013034` | keratosis palmoplantaris striata 2 | DSP |
  | `MONDO:0013030` | dilated cardiomyopathy 1BB | DSG2 |
  | `MONDO:0030986` | blistering, acantholytic, of oral and laryngeal mucosa | DSG3 |

  Excluded: the pemphigus diseases (autoimmune attack on desmogleins, not
  hereditary) and Darier and Hailey-Hailey diseases (ATP2A2 and ATP2C1 calcium
  pumps; desmosome loss is downstream of the calcium defect).
- **Adjacent MONDO classes, disclosed:** MONDO's arrhythmogenic cardiomyopathy
  classes are phenotype-defined and include non-desmosomal genes, so they
  overlap without being equivalent. "desmosom" appears only in the definitions
  of `MONDO:0008017` and `MONDO:0011581`.
- **dismech provenance:** `kb/modules/desmosomal_adhesion_failure.yaml`
  (13 conforming files, 7 germline) and
  `kb/groupings/Hereditary_Desmosomopathies.yaml` (7 members). A second
  `HAS_GENE` criterion over the desmosomal genes keeps the pemphigus and
  calcium-pump conformers out.

### Runner-up: JAK-STAT gain-of-function inborn error of immunity

`jak_stat_pathway_activation` has 12 conformers, but most are neoplasms
(myeloproliferative neoplasms, NK-cell leukemia, cutaneous T-cell lymphoma). The
germline members are STAT6 gain-of-function hyper-IgE syndrome
(`MONDO:0957807`), STAT4 disabling pansclerotic morphea (`MONDO:0957497`), SOCS1
haploinsufficiency (`MONDO:0800130`), autoinflammation with immune dysregulation
and eosinophilia (`MONDO:0033558`), and the STAT1 gain-of-function form of
chronic mucocutaneous candidiasis (`MONDO:0015279`, a broader class). MONDO has
no JAK-STAT class (0 / 0 / 0 for "JAK-STAT" and "STAT gain"), but five members,
one of them a broad class, is too thin to propose yet.

## 4. Next steps

1. **Review and prune** proposals 11 to 14 alongside the round-1 queue. Round 1
   was never filed. A single batch to MONDO covering the strongest of both rounds
   (round-1 proposals 1 to 7 and proposals 11 to 13 here) would let MONDO weigh
   the mechanism axis as a whole rather than one class at a time.
2. **Backing groupings are in place** for proposals 11 to 14, so membership is
   auditable with `just check-groupings`, as it was for round 1.
3. **Settle the boundary cases:** Peutz-Jeghers syndrome in proposal 12, Cornelia
   de Lange syndrome in proposal 13, and MFN2-related Charcot-Marie-Tooth disease
   for proposal 11, which needs a contact-site node in its dismech entry first.
4. **Re-check round-1 proposal 9** against its 15 current conformers before
   filing.

## 5. Reproducing this analysis

The MONDO checks used the OAK SQLite build fetched on 2026-10-23
(`$HOME/.data/oaklib/mondo.db`), fingerprinted as **36,017 labelled `MONDO:`
classes and 3,980 deprecated**. OLS reported release 2026-10-06 on the same
day. Round 1's snapshot had 31,886 labelled classes, so counts from the two
rounds are not directly comparable. Re-run before filing.

The commands are those in round 1, section 6. Round 1's step 3 counts
conformers for one module; this command counts them for all modules at once:

```bash
python3 - <<'EOF'
import glob, re, collections, os
cnt = collections.defaultdict(set)
for f in glob.glob('kb/disorders/*.yaml') + glob.glob('kb/comorbidities/*.yaml'):
    for m in re.findall(r'conforms_to:\s*"?([A-Za-z0-9_\-]+)', open(f).read()):
        cnt[m].add(f)
for p in sorted(glob.glob('kb/modules/*.yaml')):
    m = os.path.basename(p)[:-5]
    print(f"{len(cnt.get(m, ()))}\t{m}")
EOF
```

Germline filtering was done by reading each conforming entry's `category`,
`genetic` block and description; it is a judgement per entry, and the excluded
entries are named under each proposal so the call can be checked.
