# Rubrics review (DRAFT)

## Changes

Revision 2, 2026-11-16:

- Banned terms are renamed leakage_terms and are never stripped from packets, which are pre-cutoff by construction. Each carries in_packet (yes when its pre-cutoff co-occurrence count with the disease is above 0). Planned audit: a leakage term with in_packet no that appears in a curated entry or an arm's output is a leakage alarm.
- Every case and negative has an arm_display_name: a pre-cutoff disease name with no test, analyte or antibody in it. Subset text never appears in arm prompts.
- T2 rule: an analyte in clinical diagnostic use for the disease at the cutoff reaches T1 only (t1_clinical).
- C022: leukocyte acid alpha-glucosidase moved to T1; T2 is the dried-blood-spot assay only.
- C036, C057: plasma AVP moved to T1; T2 is copeptin.
- C045: pipecolic acid moved to T1; T2 is alpha-AASA or P6C.
- C027: VEGF-C removed from T2.
- C051: cholesterol (CHEBI:16113) removed from T2.
- C001: anti-ADAMTS13 IgG or inhibitor (AUTOANTIBODY, serum or plasma) added to T2.
- C008: 'NAA' dropped from the leakage terms (generic abbreviation).
- Revision 3 (defaults, pending Chris; see DEVIATIONS.md): C036 excluded as NOT_NEW_ANALYTE; C047 phytanic acid moved to T1; C056 re-dated to PMID:15589308 (cutoff 2003-12-31); C022 display name 'adult-onset acid maltase deficiency'; negatives N10, N13, N17 replaced after an accessible-test screen.
- PubMed counts for multi-word leakage terms and display names now use the proximity form [tiab:~0]; a quoted phrase in [tiab] returns 0 for phrases outside PubMed's phrase index, which had set some in_packet values to no wrongly.
- Negatives N12 and N13 replaced by the next seeded draws. Every negative has a cutoff from a seeded draw of test cases (provisional: no matching criterion is defined yet) and a literature check at it; drawn negatives below packet_minimum were redrawn (negatives.tsv, negatives_replaced.tsv, negatives_literature_check.tsv).

## Arm display names

The only disease name an arm sees. `Pre-cutoff hits` is the PubMed count of the check phrases on or before the cutoff (0 means the name may not be pre-cutoff); `collisions` lists leakage terms the name contains.

| Case | Display name | Cutoff | Pre-cutoff hits | Collisions | Subset text |
|---|---|---|---|---|---|
| C001 | acquired thrombotic thrombocytopenic purpura | 1997-12-31 | 1281 | none | no |
| C002 | Alzheimer disease | 2019-12-31 | 128022 | none | no |
| C003 | Alzheimer disease | 1994-12-31 | 9825 | none | no |
| C005 | autoimmune polyendocrinopathy syndrome type 1 | 2005-12-31 | 120 | none | no |
| C006 | pulmonary alveolar proteinosis | 1998-12-31 | 537 | none | no |
| C008 | Canavan disease | 1987-12-31 | 13 | none | no |
| C009 | coeliac disease | 1997-12-31 | 4554 | none | no |
| C010 | childhood absence epilepsy | 2007-12-31 | 194 | none | no |
| C011 | chronic inflammatory demyelinating polyneuropathy | 2011-12-31 | 925 | none | no |
| C012 | chronic inflammatory demyelinating polyneuropathy | 2011-12-31 | 925 | none | no |
| C014 | dermatomyositis | 2004-12-31 | 4311 | none | no |
| C015 | dyskeratosis congenita | 2006-12-31 | 358 | none | no |
| C016 | dyskeratosis congenita | 2006-12-31 | 358 | none | no |
| C017 | membranous glomerulonephritis | 2008-12-31 | 1203 | none | no |
| C018 | heparin-induced thrombocytopenia | 1991-12-31 | 189 | none | no |
| C021 | inherited aplastic anaemia | 2006-12-31 | 32 | none | no |
| C022 | adult-onset acid maltase deficiency | 2000-12-31 | 185 | none | no |
| C023 | limbic encephalitis | 2009-12-31 | 430 | none | no |
| C024 | limbic encephalitis | 2009-12-31 | 430 | none | no |
| C025 | limbic encephalitis | 2008-12-31 | 370 | none | no |
| C026 | limbic encephalitis | 2008-12-31 | 370 | none | no |
| C027 | lymphangioleiomyomatosis | 2005-12-31 | 504 | none | no |
| C028 | acquired demyelinating syndrome in children (ADEM or CIS) | 2008-12-31 | 875 | none | no |
| C029 | idiopathic membranous nephropathy | 2008-12-31 | 312 | none | no |
| C030 | Menkes disease | 1992-12-31 | 140 | none | no |
| C033 | myasthenia gravis | 2000-12-31 | 7722 | none | no |
| C034 | narcolepsy with cataplexy | 1999-12-31 | 1211 | none | no |
| C035 | narcolepsy | 1999-12-31 | 1211 | none | no |
| C037 | neuromyelitis optica | 2003-12-31 | 177 | none | no |
| C038 | late infantile neuronal ceroid lipofuscinosis | 1998-12-31 | 49 | none | no |
| C039 | optic neuritis | 2010-12-31 | 3345 | none | no |
| C040 | optic neuritis | 2003-12-31 | 2399 | none | no |
| C041 | paroxysmal dyskinesia | 2007-12-31 | 91 | none | no |
| C042 | paroxysmal nocturnal haemoglobinuria | 1984-12-31 | 499 | none | no |
| C043 | polycythaemia vera | 2004-12-31 | 3474 | none | no |
| C044 | idiopathic bile acid malabsorption | 1992-12-31 | 145 | none | no |
| C045 | pyridoxine-dependent epilepsy | 2005-12-31 | 72 | none | no |
| C047 | rhizomelic chondrodysplasia punctata | 1990-12-31 | 37 | none | no |
| C050 | severe combined immunodeficiency | 2004-12-31 | 2439 | none | no |
| C051 | Smith-Lemli-Opitz syndrome | 1993-12-31 | 111 | none | no |
| C052 | statin-associated myopathy | 2009-12-31 | 116 | none | no |
| C053 | stiff-man syndrome | 1987-12-31 | 127 | none | no |
| C054 | stiff-man syndrome | 1992-12-31 | 169 | none | no |
| C055 | stiff person syndrome | 2007-12-31 | 160 | none | no |
| C056 | transverse myelitis | 2003-12-31 | 626 | none | no |
| C057 | nephrogenic diabetes insipidus | 2010-12-31 | 1018 | none | no |
| N01 | Ehlers-Danlos syndrome type III (hypermobile) | 1987-12-31 | 753 | none | no |
| N02 | Kawasaki disease | 2000-12-31 | 1717 | none | no |
| N03 | sarcoidosis | 1993-12-31 | 10422 | none | no |
| N04 | Behcet's disease | 1987-12-31 | 966 | none | no |
| N05 | complex regional pain syndrome type 1 | 2007-12-31 | 747 | none | no |
| N06 | Takayasu arteritis | 2004-12-31 | 428 | none | no |
| N07 | juvenile idiopathic arthritis | 2011-12-31 | 2102 | none | no |
| N08 | soil-transmitted helminthiasis | 1984-12-31 | 947 | none | no |
| N09 | congenital merosin-deficient muscular dystrophy | 2019-12-31 | 117 | none | no |
| N10 | autoinflammatory disease of infancy with pustulosis and osteomyelitis | 2010-12-31 | 1353 | none | no |
| N11 | autosomal dominant limb-girdle muscular dystrophy | 2003-12-31 | 526 | none | no |
| N12 | hereditary angioedema | 1991-12-31 | 492 | none | no |
| N13 | lipoprotein glomerulopathy | 2000-12-31 | 35 | none | no |
| N14 | choroid plexus tumour | 2010-12-31 | 644 | none | no |
| N15 | psoriasis | 1997-12-31 | 12278 | none | no |
| N16 | angiomatoid fibrous histiocytoma | 1992-12-31 | 6 | none | no |
| N17 | congenital hydrocephalus | 2005-12-31 | 526 | none | no |
| N18 | peeling skin syndrome | 2008-12-31 | 34 | none | no |

## How to read the case blocks

One block per case. The YAML files in this directory are the rubrics; this page is for reading them. Every rubric is drafted from the case row and its discovery paper only.

- **Order:** cases whose T2 boundary or banned terms needed a judgment come first. Each leads with a one-line reason; further calls on the same case follow it.
- **Leakage terms:** names of the test and analyte. They are never stripped from packets. '[in packet]' marks a term that co-occurs with the disease in PubMed on or before the cutoff (in_packet yes). A term with in_packet no that appears in a curated entry or an arm's output is a leakage alarm (audit not yet built).
- **Negatives:** they come last.

## Judgment calls (29 cases)

### C001 · Acquired Thrombotic Thrombocytopenic Purpura · ADAMTS13 activity (test, cutoff 1997-12-31)

- **Judgment:** T2 also accepts an anti-ADAMTS13 IgG or inhibitor (AUTOANTIBODY, serum or plasma): the discovery paper found an inhibitor in the nonfamilial cases.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): von Willebrand factor-cleaving protease (1), vWF-cleaving protease (2).
- **T1:** ENZYME_DEFICIENCY; metalloendopeptidase activity (GO:0004222)
- **T2:** ENZYME_ACTIVITY in plasma; members ADAMTS13 (hgnc:1366)
- **T2:** AUTOANTIBODY in serum, plasma; members ADAMTS13 (hgnc:1366)
- **T3:** Plasma VWF-cleaving protease activity (diluted plasma, purified normal VWF as substrate, degradation read by SDS-agarose electrophoresis and immunoblot) in 53 patients with TTP or HUS, familial and nonfamilial, with an inhibitor (mixing) study against normal plasma. (PMID:9828245)
- **T4:** ADAMTS13 (von Willebrand factor-cleaving protease) activity in plasma; reachable pre-cutoff: yes (PMID:9129011)
- **Arm display name:** acquired thrombotic thrombocytopenic purpura
- **Leakage terms:** ADAMTS13, ADAMTS-13, von Willebrand factor-cleaving protease [in packet], vWF-cleaving protease [in packet], VWF-CP, VWFCP

### C002 · Alzheimer Disease · plasma p-tau217 (test, cutoff 2019-12-31)

- **Judgment:** IMPROVEMENT case: plasma p-tau181 or total tau meet T2 (same target, blood); CSF tau does not.
- **Note:** Only 217-specific names are leakage terms; tau and p-tau are pre-cutoff vocabulary and would raise false alarms.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): pT217 (2).
- **T1:** PROTEIN_AGGREGATION; neurofibrillary tangle assembly (GO:1902988)
- **T2:** PROTEIN_LEVEL in plasma, serum; members MAPT (hgnc:6893)
- **T3:** Plasma p-tau217 immunoassay in three cohorts (neuropathology-confirmed, clinical BioFINDER-2 including other neurodegenerative diseases, and a PSEN1 E280A kindred); discriminative accuracy for AD vs other diagnoses and association with tau pathology. (PMID:32722745)
- **T4:** tau phosphorylated at threonine 217 (p-tau217) in plasma; reachable pre-cutoff: yes (PMID:21342022)
- **Arm display name:** Alzheimer disease
- **Leakage terms:** p-tau217, pTau217, p-tau 217, phospho-tau217, phosphorylated tau 217, tau phosphorylated at threonine 217, pT217 [in packet]

### C006 · Autoimmune Pulmonary Alveolar Proteinosis · anti-GM-CSF autoantibodies (test, cutoff 1998-12-31)

- **Judgment:** The discovery paper found the antibody first in bronchoalveolar lavage fluid, which is not an accessible specimen; T2 allows only serum and plasma, where it was also found.
- **Note:** GM-CSF itself is not a leakage term: GM-CSF signalling in pulmonary alveolar proteinosis is pre-cutoff literature (the readiness paper).
- **T1:** AUTOIMMUNE_ANTIBODY; granulocyte-macrophage colony-stimulating factor signaling pathway (GO:0038157)
- **T2:** AUTOANTIBODY in serum, plasma; members CSF2 (hgnc:2434)
- **T3:** Search for neutralising IgG against GM-CSF in bronchoalveolar lavage fluid and serum of idiopathic PAP patients versus secondary PAP, other lung disease and normal controls; binding and neutralisation of GM-CSF bioactivity in vitro. (PMID:10499925)
- **T4:** neutralising IgG autoantibody to GM-CSF in serum; reachable pre-cutoff: yes (PMID:8171324)
- **Arm display name:** pulmonary alveolar proteinosis
- **Leakage terms:** anti-GM-CSF, GM-CSF autoantibody, GM-CSF antibody, anti-granulocyte-macrophage colony-stimulating factor

### C008 · Canavan disease · urinary N-acetylaspartic acid (test, cutoff 1987-12-31)

- **Judgment:** 'NAA' is left out of the leakage terms: it is a generic abbreviation and would raise false alarms.
- **Note:** The discovery paper's aspartoacylase assay used cultured fibroblasts, so it is not an accessible-specimen T2 hit.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): N-acetylaspartate (1), N-acetylaspartic aciduria (1), aspartoacylase (1).
- **T1:** ENZYME_DEFICIENCY; aspartoacylase activity (GO:0019807)
- **T2:** METABOLITE in urine, plasma; members N-acetyl-L-aspartic acid (CHEBI:21547)
- **T3:** Urine and plasma N-acetylaspartic acid in three patients from two Canavan families; aspartoacylase assayed in cultured skin fibroblasts. (PMID:3354621)
- **T4:** N-acetylaspartic acid in urine; reachable pre-cutoff: no
- **Arm display name:** Canavan disease
- **Leakage terms:** N-acetylaspartic acid, N-acetylaspartate [in packet], N-acetyl-L-aspartic acid, N-acetylaspartic aciduria [in packet], aspartoacylase [in packet]

### C009 · Celiac Disease · anti-tissue transglutaminase IgA (test, cutoff 1997-12-31)

- **Judgment:** Endomysial antibody (a pre-cutoff test) is excluded from T2 because it names a tissue, not tTG.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): tissue transglutaminase (3), tTG (1).
- **T1:** AUTOIMMUNE_ANTIBODY; peptide cross-linking (GO:0018149)
- **T2:** AUTOANTIBODY in serum, plasma; members TGM2 (hgnc:11778)
- **T3:** Prospective IgA anti-tissue-transglutaminase ELISA in 20 untreated coeliacs and 21 consecutive patients with other small-bowel disease. (PMID:9836104)
- **T4:** IgA antibody to tissue transglutaminase by ELISA; reachable pre-cutoff: yes (PMID:9212111)
- **Arm display name:** coeliac disease
- **Leakage terms:** tissue transglutaminase [in packet], transglutaminase 2, tTG [in packet], TG2, anti-tTG, anti-transglutaminase, tTGA, tTG-IgA

### C010 · Childhood Absence Epilepsy · CSF glucose (hypoglycorrhachia) (test, cutoff 2007-12-31)

- **Judgment:** Every leakage term for this test (CSF glucose, hypoglycorrhachia, GLUT1) is pre-cutoff vocabulary, so most are in the packet and the T4 leakage alarm has little to check.
  - also: The case is the GLUT1-deficiency subset; the subset text is kept out of arm prompts.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): GLUT1 (1), GLUT-1 (1).
- **T1:** TRANSPORTER_DEFECT; D-glucose transmembrane transport (GO:1904659)
- **T2:** METABOLITE in csf; members D-glucose (CHEBI:17634)
- **T3:** Case report: a child with absences and myoclonias first diagnosed with idiopathic generalized epilepsy, later documented to have a mild GLUT1 deficiency syndrome (diagnostic work-up not detailed in the abstract). (PMID:18479384)
- **T4:** low CSF glucose (hypoglycorrhachia), CSF:blood glucose ratio; reachable pre-cutoff: yes (PMID:12752470)
- **Arm display name:** childhood absence epilepsy
- **Leakage terms:** hypoglycorrhachia, CSF glucose, cerebrospinal fluid glucose, CSF/blood glucose ratio, CSF/serum glucose ratio, GLUT1 [in packet], GLUT-1 [in packet], Glut1 deficiency, glucose transporter type 1, glucose transporter 1, SLC2A1, De Vivo disease

### C011 · Chronic Inflammatory Demyelinating Polyneuropathy · anti-neurofascin antibodies (test, cutoff 2011-12-31)

- **Judgment:** T2 is the paranodal complex (neurofascin, contactin-1, CASPR1) rather than neurofascin alone, so the neurofascin and contactin-1 cases share a T2 class.
- **T1:** AUTOIMMUNE_ANTIBODY; paranodal junction assembly (GO:0030913)
- **T2:** AUTOANTIBODY in serum, csf; members NFASC (hgnc:29866), CNTN1 (hgnc:2171), CNTNAP1 (hgnc:8011)
- **T3:** ELISA and cell-based assay for antibodies to human NF155 and NF186 in 434 donors, including GBS variants and CIDP; isotyping, tissue staining, epitope mapping and passive transfer in rats. (PMID:23100406)
- **T4:** IgG (often IgG4) autoantibodies to neurofascin-155; reachable pre-cutoff: yes (PMID:21267074)
- **Arm display name:** chronic inflammatory demyelinating polyneuropathy
- **Leakage terms:** neurofascin, NF155, NF186, NFASC, anti-neurofascin, anti-NF155

### C012 · Chronic Inflammatory Demyelinating Polyneuropathy · anti-contactin-1 antibodies (test, cutoff 2011-12-31)

- **Judgment:** T2 is the paranodal complex (neurofascin, contactin-1, CASPR1), shared with the neurofascin case.
- **T1:** AUTOIMMUNE_ANTIBODY; paranodal junction assembly (GO:0030913)
- **T2:** AUTOANTIBODY in serum, csf; members NFASC (hgnc:29866), CNTN1 (hgnc:2171), CNTNAP1 (hgnc:8011)
- **T3:** Screening CIDP sera on live hippocampal neurons, antigen identification by immunoprecipitation and mass spectrometry, confirmed by cell-based assays, teased-nerve immunohistochemistry and immunoabsorption. (PMID:23280477)
- **T4:** IgG (often IgG4) autoantibodies to contactin-1; reachable pre-cutoff: yes (PMID:21267074)
- **Arm display name:** chronic inflammatory demyelinating polyneuropathy
- **Leakage terms:** contactin-1, contactin 1, CNTN1, anti-contactin, anti-CNTN1, CASPR1, contactin-associated protein 1

### C015 · Dyskeratosis Congenita Autosomal Recessive 2 · leukocyte telomere length by flow-FISH (test, cutoff 2006-12-31)

- **Judgment:** Blood telomere length was measured before the cutoff (by Southern blot); T2 accepts any method, and T4 requires flow-FISH.
  - also: Every leakage term is in the packet, so the leakage alarm cannot fire for this case.
- **Note:** 'telomere length' is in the packet, so only the flow-FISH terms can raise an alarm.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): flow-FISH (2), flow FISH (2), flow fluorescence in situ hybridization (1), very short telomeres (3), telomere length (19).
- **T1:** TELOMERE_MAINTENANCE_DEFECT; telomere maintenance (GO:0000723)
- **T2:** CELLULAR_DNA_MEASURE in leukocytes, lymphocytes, whole_blood; members chromosome, telomeric region (GO:0000781)
- **T3:** Multicolour flow-FISH of median telomere length in blood leukocytes, granulocytes and lymphocyte subsets in DC patients, relatives and other marrow-failure patients against 400 healthy controls; 'very short' defined as below the 1st percentile for age. (PMID:17468339)
- **T4:** very short lymphocyte telomere length (<1st percentile for age) by flow-FISH; reachable pre-cutoff: yes (PMID:16822458)
- **Arm display name:** dyskeratosis congenita
- **Leakage terms:** flow-FISH [in packet], flow FISH [in packet], flow fluorescence in situ hybridization [in packet], very short telomeres [in packet], telomere length [in packet]

### C016 · Dyskeratosis Congenita Autosomal Recessive 6 · leukocyte telomere length by flow-FISH (test, cutoff 2006-12-31)

- **Judgment:** Blood telomere length was measured before the cutoff (by Southern blot); T2 accepts any method, and T4 requires flow-FISH.
  - also: Every leakage term is in the packet, so the leakage alarm cannot fire for this case.
- **Note:** 'telomere length' is in the packet, so only the flow-FISH terms can raise an alarm.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): flow-FISH (2), flow FISH (2), flow fluorescence in situ hybridization (1), very short telomeres (3), telomere length (19).
- **T1:** TELOMERE_MAINTENANCE_DEFECT; telomere maintenance (GO:0000723)
- **T2:** CELLULAR_DNA_MEASURE in leukocytes, lymphocytes, whole_blood; members chromosome, telomeric region (GO:0000781)
- **T3:** Multicolour flow-FISH of median telomere length in blood leukocytes, granulocytes and lymphocyte subsets in DC patients, relatives and other marrow-failure patients against 400 healthy controls; 'very short' defined as below the 1st percentile for age. (PMID:17468339)
- **T4:** very short lymphocyte telomere length (<1st percentile for age) by flow-FISH; reachable pre-cutoff: yes (PMID:16822458)
- **Arm display name:** dyskeratosis congenita
- **Leakage terms:** flow-FISH [in packet], flow FISH [in packet], flow fluorescence in situ hybridization [in packet], very short telomeres [in packet], telomere length [in packet]

### C018 · Heparin-Induced Thrombocytopenia · anti-PF4/heparin IgG immunoassay (test, cutoff 1991-12-31)

- **Judgment:** IMPROVEMENT case: the pre-cutoff functional tests detect the same antibody, but T2 requires PF4 as the target, so they reach T1/T3 only.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): PF4 (2), platelet factor 4 (12).
- **T1:** DRUG_DEPENDENT_ANTIBODY; platelet activation (GO:0030168)
- **T2:** AUTOANTIBODY in serum, plasma; members PF4 (hgnc:8861), heparin (CHEBI:28304)
- **T3:** Letter (no PubMed abstract): identification of PF4 complexed to heparin as the target of HIT antibodies. (PMID:1514184)
- **T4:** IgG antibody to platelet factor 4-heparin complexes (immunoassay); reachable pre-cutoff: yes (PMID:2709525)
- **Arm display name:** heparin-induced thrombocytopenia
- **Leakage terms:** PF4 [in packet], platelet factor 4 [in packet], PF4/heparin, PF4-heparin, anti-PF4, PF4/H, heparin-PF4

### C021 · Inherited Aplastic Anemia · leukocyte telomere length by flow-FISH (test, cutoff 2006-12-31)

- **Judgment:** Blood telomere length was measured before the cutoff (by Southern blot); T2 accepts any method, and T4 requires flow-FISH.
- **Note:** 'telomere length' is in the packet, so only the flow-FISH terms can raise an alarm.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): flow-FISH (1), flow FISH (1), telomere length (7).
- **T1:** TELOMERE_MAINTENANCE_DEFECT; telomere maintenance (GO:0000723)
- **T2:** CELLULAR_DNA_MEASURE in leukocytes, lymphocytes, whole_blood; members chromosome, telomeric region (GO:0000781)
- **T3:** Multicolour flow-FISH of median telomere length in blood leukocytes, granulocytes and lymphocyte subsets in DC patients, relatives and other marrow-failure patients against 400 healthy controls; 'very short' defined as below the 1st percentile for age. (PMID:17468339)
- **T4:** very short lymphocyte telomere length (<1st percentile for age) by flow-FISH; reachable pre-cutoff: yes (PMID:16822458)
- **Arm display name:** inherited aplastic anaemia
- **Leakage terms:** flow-FISH [in packet], flow FISH [in packet], flow fluorescence in situ hybridization, very short telomeres, telomere length [in packet]

### C023 · Limbic Encephalitis · anti-LGI1 antibodies (test, cutoff 2009-12-31)

- **Judgment:** The VGKC-complex antibody was the pre-cutoff test; it is kept out of T2, so T2 is not reachable merely by proposing it.
- **T1:** AUTOIMMUNE_ANTIBODY; regulation of potassium ion transmembrane transport (GO:1901379)
- **T2:** AUTOANTIBODY in serum, csf; members LGI1 (hgnc:6572), ADAM22 (hgnc:201), ADAM23 (hgnc:202)
- **T3:** Sera and CSF of 57 patients with limbic encephalitis attributed to VGKC antibodies and 148 controls; immunohistochemistry, immunoprecipitation and mass spectrometry identified LGI1, tested on HEK293 cells expressing LGI1 with ADAM22/23 and confirmed in Lgi1-null mice. (PMID:20580615)
- **T4:** IgG autoantibodies to LGI1; reachable pre-cutoff: yes (PMID:17395141)
- **Arm display name:** limbic encephalitis
- **Leakage terms:** LGI1, leucine-rich glioma-inactivated 1, leucine-rich, glioma inactivated 1, anti-LGI1, LGI1 antibody, epitempin

### C024 · Limbic Encephalitis · anti-CASPR2 antibodies (test, cutoff 2009-12-31)

- **Judgment:** The VGKC-complex antibody was the pre-cutoff test; it is kept out of T2.
- **T1:** AUTOIMMUNE_ANTIBODY; regulation of potassium ion transmembrane transport (GO:1901379)
- **T2:** AUTOANTIBODY in serum, csf; members CNTNAP2 (hgnc:13830)
- **T3:** 96 VGKC-antibody-positive patients: binding to HEK293 cells expressing potassium-channel subunits and complexed proteins, identifying LGI1, CASPR2 and contactin-2 as the targets. (PMID:20663977)
- **T4:** IgG autoantibodies to contactin-associated protein-2; reachable pre-cutoff: yes (PMID:17395141)
- **Arm display name:** limbic encephalitis
- **Leakage terms:** CASPR2, CNTNAP2, contactin-associated protein-2, contactin-associated protein 2, contactin-associated protein-like 2, anti-CASPR2

### C028 · MOGAD · MOG-IgG cell-based assay (test, cutoff 2008-12-31)

- **Judgment:** Anti-MOG ELISA and Western blot studies, which were nonspecific, predate the cutoff; T2 accepts them and T4 requires the native-MOG cell-based assay.
  - also: MOGAD is named after its test; arm_display_name uses a pre-cutoff name for paediatric demyelination.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): MOG-IgG (5), MOG IgG (6), anti-MOG (62), MOG antibody (22), MOG antibodies (27), myelin oligodendrocyte glycoprotein antibody (3).
- **T1:** AUTOIMMUNE_ANTIBODY; myelination (GO:0042552)
- **T2:** AUTOANTIBODY in serum, csf; members MOG (hgnc:7197)
- **T3:** Cell-based bioassay for antibodies to native MOG in 47 children at a first episode of CNS demyelination (ADEM or CIS) against neurological, healthy-child and adult controls. (PMID:20033986)
- **T4:** IgG to native myelin oligodendrocyte glycoprotein by cell-based assay; reachable pre-cutoff: yes (PMID:16934337)
- **Arm display name:** acquired demyelinating syndrome in children (ADEM or CIS)
- **Leakage terms:** MOG-IgG [in packet], MOG IgG [in packet], anti-MOG [in packet], MOG antibody [in packet], MOG antibodies [in packet], myelin oligodendrocyte glycoprotein antibody [in packet], MOGAD, MOG antibody-associated disease, nMOG

### C030 · Menkes Disease · plasma DOPA:DHPG ratio (test, cutoff 1992-12-31)

- **Judgment:** IMPROVEMENT case: copper and ceruloplasmin are left at T1. DOPA, DOPAC and noradrenaline are too generic to be leakage terms.
- **T1:** ENZYME_DEFICIENCY; norepinephrine biosynthetic process (GO:0042421)
- **T2:** METABOLITE in plasma, csf; members L-dopa (CHEBI:15765), 3,4-dihydroxyphenylethyleneglycol (CHEBI:1387), (3,4-dihydroxyphenyl)acetic acid (CHEBI:41941), dopamine (CHEBI:18243), noradrenaline (CHEBI:33569)
- **T3:** Plasma and CSF catechols in 10 Menkes patients aged 9 days to 27 months; DOPA:DHPG and DOPAC:DHPG ratios compared with controls. (PMID:8434878)
- **T4:** plasma DOPA:DHPG ratio; reachable pre-cutoff: yes (PMID:3233105)
- **Arm display name:** Menkes disease
- **Leakage terms:** DOPA:DHPG, DOPA/DHPG, DOPAC:DHPG, DHPG, dihydroxyphenylglycol, plasma catechols, plasma neurochemical

### C033 · Myasthenia Gravis · anti-MuSK antibodies (test, cutoff 2000-12-31)

- **Judgment:** T2 includes LRP4, whose antibodies were described only years later; this is a deliberate class boundary (postsynaptic non-AChR targets).
- **T1:** AUTOIMMUNE_ANTIBODY; neuromuscular junction development (GO:0007528)
- **T2:** AUTOANTIBODY in serum; members MUSK (hgnc:7525), LRP4 (hgnc:6696)
- **T3:** Sera of AChR-antibody-seronegative and seropositive generalized MG patients tested against the extracellular domains of MuSK expressed in transfected COS7 cells. (PMID:11231638)
- **T4:** IgG autoantibodies to muscle-specific kinase (MuSK); reachable pre-cutoff: yes (PMID:3352902)
- **Arm display name:** myasthenia gravis
- **Leakage terms:** MuSK, muscle-specific kinase, muscle-specific receptor tyrosine kinase, muscle specific kinase, anti-MuSK

### C037 · Neuromyelitis Optica Spectrum Disorder with Anti-AQP4 Antibodies · AQP4-IgG (test, cutoff 2003-12-31)

- **Judgment:** For the 2003 cutoffs (all three cases since C056 was re-dated) the antigen was unknown at discovery (a tissue-staining pattern); T2 accepts an end-foot antigen named descriptively.
  - also: The NMOSD entry is named after its antibody; arm_display_name is 'neuromyelitis optica'.
- **Note:** 'NMO' alone is not a leakage alarm: terms match whole and exact, so only 'NMO-IgG' and the like match.
- **T1:** AUTOIMMUNE_ANTIBODY; water transport (GO:0006833)
- **T2:** AUTOANTIBODY in serum, csf; members AQP4 (hgnc:637)
- **T3:** Indirect immunofluorescence on composite mouse tissue for an NMO-IgG staining pattern; masked sera from 102 North American patients with NMO or high-risk syndromes and 12 Japanese optic-spinal MS patients against MS and other controls; sensitivity and specificity. (PMID:15589308)
- **T4:** NMO-IgG / aquaporin-4 IgG; reachable pre-cutoff: no
- **Arm display name:** neuromyelitis optica
- **Leakage terms:** NMO-IgG, NMO IgG, AQP4-IgG, AQP4 IgG, anti-AQP4, aquaporin-4 antibody, aquaporin-4 antibodies, anti-aquaporin-4, aquaporin-4, aquaporin 4, AQP4, AQP-4, MIWC, mercurial-insensitive water channel

### C038 · Neuronal Ceroid Lipofuscinosis 2 · TPP1 enzyme activity (dev, cutoff 1998-12-31)

- **Judgment:** The discovery paper measured cultured fibroblasts, which are not accessible; T2's specimens come from the case row (blood).
  - also: The gene name CLN2 is also the disease name, so it is not a leakage term.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): tripeptidyl peptidase 1 (1), TPP1 (1), lysosomal pepstatin-insensitive carboxypeptidase (1), LPIC (1).
- **T1:** ENZYME_DEFICIENCY; tripeptidyl-peptidase activity (GO:0008240)
- **T2:** ENZYME_ACTIVITY in leukocytes, dried_blood_spot, whole_blood, plasma; members TPP1 (hgnc:2073)
- **T3:** TPP-I activity in cultured fibroblasts from LINCL patients against controls, with other lysosomal enzymes and peptide degradation, after sequence identity of TPP-I with the CLN2 protease. (PMID:9989590)
- **T4:** tripeptidyl peptidase I activity; reachable pre-cutoff: yes (PMID:9295267)
- **Arm display name:** late infantile neuronal ceroid lipofuscinosis
- **Leakage terms:** tripeptidyl peptidase I, tripeptidyl peptidase 1 [in packet], tripeptidyl-peptidase I, TPP-I, TPP1 [in packet], TPPI, TPP-1, pepstatin-insensitive carboxyl proteinase, pepstatin-insensitive protease, lysosomal pepstatin-insensitive carboxypeptidase [in packet], LPIC [in packet]

### C039 · Optic Neuritis · MOG-IgG (test, cutoff 2010-12-31)

- **Judgment:** Anti-MOG ELISA and Western blot studies, which were nonspecific, predate the cutoff; T2 accepts them and T4 requires the native-MOG cell-based assay.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): anti-MOG (5), MOG antibody (1).
- **T1:** AUTOIMMUNE_ANTIBODY; myelination (GO:0042552)
- **T2:** AUTOANTIBODY in serum, csf; members MOG (hgnc:7197)
- **T3:** Native-MOG cell-based assay for complement-activating MOG antibodies in NMO, high-risk NMO (recurrent optic neuritis or LETM), ADEM, CIS, MS and controls. (PMID:22204662)
- **T4:** IgG to native myelin oligodendrocyte glycoprotein by cell-based assay; reachable pre-cutoff: yes (PMID:11427318)
- **Arm display name:** optic neuritis
- **Leakage terms:** MOG-IgG, MOG IgG, anti-MOG [in packet], MOG antibody [in packet], MOG antibodies, myelin oligodendrocyte glycoprotein antibody, MOGAD, MOG antibody-associated disease, nMOG

### C040 · Optic Neuritis · AQP4-IgG (test, cutoff 2003-12-31)

- **Judgment:** For the 2003 cutoffs (all three cases since C056 was re-dated) the antigen was unknown at discovery (a tissue-staining pattern); T2 accepts an end-foot antigen named descriptively.
- **Note:** 'NMO' alone is not a leakage alarm: terms match whole and exact, so only 'NMO-IgG' and the like match.
- **T1:** AUTOIMMUNE_ANTIBODY; water transport (GO:0006833)
- **T2:** AUTOANTIBODY in serum, csf; members AQP4 (hgnc:637)
- **T3:** Indirect immunofluorescence on composite mouse tissue for an NMO-IgG staining pattern; masked sera from 102 North American patients with NMO or high-risk syndromes and 12 Japanese optic-spinal MS patients against MS and other controls; sensitivity and specificity. (PMID:15589308)
- **T4:** NMO-IgG / aquaporin-4 IgG; reachable pre-cutoff: no
- **Arm display name:** optic neuritis
- **Leakage terms:** NMO-IgG, NMO IgG, AQP4-IgG, AQP4 IgG, anti-AQP4, aquaporin-4 antibody, aquaporin-4 antibodies, anti-aquaporin-4, aquaporin-4, aquaporin 4, AQP4, AQP-4, MIWC, mercurial-insensitive water channel

### C041 · Paroxysmal Dyskinesia · CSF glucose (hypoglycorrhachia) (test, cutoff 2007-12-31)

- **Judgment:** Every leakage term for this test (CSF glucose, hypoglycorrhachia, GLUT1) is pre-cutoff vocabulary, so most are in the packet and the T4 leakage alarm has little to check.
  - also: The case is the GLUT1-deficiency subset; the subset text is kept out of arm prompts.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): glucose transporter 1 (1).
- **T1:** TRANSPORTER_DEFECT; D-glucose transmembrane transport (GO:1904659)
- **T2:** METABOLITE in csf; members D-glucose (CHEBI:17634)
- **T3:** Family study of paroxysmal exertion-induced dyskinesia with reduced CSF glucose; candidate-gene sequencing of GLUT1, functional transport studies in oocytes and erythrocytes, and screening of four further families. (PMID:18451999)
- **T4:** low CSF glucose (hypoglycorrhachia), CSF:blood glucose ratio; reachable pre-cutoff: yes (PMID:16149086)
- **Arm display name:** paroxysmal dyskinesia
- **Leakage terms:** hypoglycorrhachia, CSF glucose, cerebrospinal fluid glucose, CSF/blood glucose ratio, CSF/serum glucose ratio, GLUT1, GLUT-1, Glut1 deficiency, glucose transporter type 1, glucose transporter 1 [in packet], SLC2A1, De Vivo disease

### C042 · Paroxysmal Nocturnal Hemoglobinuria · flow cytometry for GPI-anchored proteins (test, cutoff 1984-12-31)

- **Judgment:** IMPROVEMENT case: erythrocyte DAF deficiency was published before the cutoff (the readiness paper) and meets T2, so T2 is reachable from pre-cutoff literature; T4 requires leukocytes or platelets.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): decay-accelerating factor (2), decay accelerating factor (2), DAF (2).
- **T1:** GPI_ANCHOR_DEFICIENCY; GPI anchor biosynthetic process (GO:0006506)
- **T2:** CELL_SURFACE_MARKER in granulocytes, monocytes, erythrocytes, platelets, whole_blood; members CD55 (hgnc:2665), CD59 (hgnc:1689)
- **T3:** Cytofluorographic analysis with anti-DAF antibody of granulocytes, monocytes and platelets from four PNH patients and controls, with surface radiolabelling and immunoprecipitation. (PMID:3845321)
- **T4:** decay-accelerating factor (CD55) deficiency on granulocytes and monocytes by flow cytometry; reachable pre-cutoff: yes (PMID:6576376)
- **Arm display name:** paroxysmal nocturnal haemoglobinuria
- **Leakage terms:** decay-accelerating factor [in packet], decay accelerating factor [in packet], DAF [in packet], CD55, CD59, GPI-anchored, glycosylphosphatidylinositol-anchored, FLAER

### C043 · Polycythemia Vera · JAK2 V617F (test, cutoff 2004-12-31)

- **Judgment:** JAK2 itself is a pre-cutoff term (the readiness paper), so only variant-specific names are leakage terms.
- **T1:** SOMATIC_KINASE_ACTIVATION; cell surface receptor signaling pathway via JAK-STAT (GO:0007259)
- **T2:** SOMATIC_VARIANT in granulocytes, whole_blood; members JAK2 (hgnc:6192)
- **T3:** Bidirectional sequencing of JAK2 coding exons from peripheral-blood granulocytes and T cells of patients with PV, ET and myelofibrosis; allele-specific PCR, cytogenetics, SNP arrays and colony assays. (PMID:15781101)
- **T4:** JAK2 p.Val617Phe (V617F); reachable pre-cutoff: yes (PMID:15102479)
- **Arm display name:** polycythaemia vera
- **Leakage terms:** V617F, Val617Phe, JAK2V617F, JAK2 V617F, JAK2 mutation, 1849G>T, JAK2 617

### C044 · Primary Bile Acid Malabsorption · serum 7-alpha-hydroxy-4-cholesten-3-one (C4) (dev, cutoff 1992-12-31)

- **Judgment:** 'C4' is not a leakage term: it also names complement C4.
- **T1:** BILE_ACID_SYNTHESIS_UPREGULATION; bile acid biosynthetic process (GO:0006699)
- **T2:** METABOLITE in serum, plasma; members 7alpha-hydroxycholest-4-en-3-one (CHEBI:17899)
- **T3:** Fasting serum 7alpha-hydroxy-4-cholesten-3-one in 28 patients with chronic diarrhoea, correlated with SeHCAT retention measured the same day. (PMID:8504974)
- **T4:** serum 7alpha-hydroxy-4-cholesten-3-one (C4); reachable pre-cutoff: yes (PMID:3181435)
- **Arm display name:** idiopathic bile acid malabsorption
- **Leakage terms:** 7 alpha-hydroxy-4-cholesten-3-one, 7alpha-hydroxy-4-cholesten-3-one, 7α-hydroxy-4-cholesten-3-one, 7alpha-hydroxycholest-4-en-3-one, 7-alpha-hydroxy-4-cholesten-3-one, 7-HCO, 7alpha-HCO

### C052 · Statin Toxicity · anti-HMGCR antibodies (test, cutoff 2009-12-31)

- **Judgment:** HMG-CoA reductase is the statin target and appears in nearly every pre-cutoff statin paper, so only antibody phrases are leakage terms.
- **Note:** The discovery paper identified the antigen only by size (200/100 kd); T4 names the later identity.
- **T1:** AUTOIMMUNE_ANTIBODY; cholesterol biosynthetic process (GO:0006695)
- **T2:** AUTOANTIBODY in serum; members HMGCR (hgnc:5006)
- **T3:** Immunoprecipitation from 35S-labelled HeLa lysates of sera from 225 myopathy patients with muscle biopsy, finding a 200/100-kd specificity in necrotizing myopathy; staining for MAC, MHC-I and CD31. (PMID:20496415)
- **T4:** autoantibodies to HMG-CoA reductase (the 200/100-kd antigen); reachable pre-cutoff: yes (PMID:14609738)
- **Arm display name:** statin-associated myopathy
- **Leakage terms:** anti-HMGCR, HMGCR antibody, HMGCR antibodies, anti-200/100, 200-kd and 100-kd, anti-HMG-CoA reductase

### C053 · Stiff Person Syndrome · anti-GAD65 antibodies (test, cutoff 1987-12-31)

- **Judgment:** 'GAD' alone is not a leakage term: it also abbreviates generalized anxiety disorder.
- **Note:** T4 accepts either isoform, because the discovery paper predates the GAD65 identification.
- **T1:** AUTOIMMUNE_ANTIBODY; gamma-aminobutyric acid biosynthetic process (GO:0009449)
- **T2:** AUTOANTIBODY in serum, csf; members GAD2 (hgnc:4093), GAD1 (hgnc:4092)
- **T3:** Serum and CSF of one stiff-man patient with epilepsy and type 1 diabetes: oligoclonal IgG, immunocytochemical staining of brain matching anti-GAD, and SDS-PAGE identifying a band comigrating with GAD. (PMID:3281011)
- **T4:** autoantibodies to glutamic acid decarboxylase; reachable pre-cutoff: yes (PMID:7271246)
- **Arm display name:** stiff-man syndrome
- **Leakage terms:** glutamic acid decarboxylase, glutamate decarboxylase, GAD65, GAD67, anti-GAD, GAD antibodies, GAD autoantibodies

### C055 · Stiff Person Syndrome · anti-glycine receptor antibodies (test, cutoff 2007-12-31)

- **Judgment:** Gephyrin antibodies (the pre-cutoff readiness paper) are kept out of T2, so T2 is not reachable merely by proposing them.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): glycine receptor (6), glycine receptors (3), GlyR (4), GLRA1 (7), glycine receptor alpha1 (1).
- **T1:** AUTOIMMUNE_ANTIBODY; synaptic transmission, glycinergic (GO:0060012)
- **T2:** AUTOANTIBODY in serum, csf; members GLRA1 (hgnc:4326), GLRA2 (hgnc:4327), GLRA3 (hgnc:4328), GLRB (hgnc:4329)
- **T3:** Clinical note (no PubMed abstract): a patient with severe PERM and a novel anti-glycine receptor antibody, judged from the source's opening text supplied by the reviewer. (PMID:18852446)
- **T4:** IgG autoantibodies to the glycine receptor alpha1 subunit; reachable pre-cutoff: yes (PMID:10839351)
- **Arm display name:** stiff person syndrome
- **Leakage terms:** glycine receptor [in packet], glycine receptors [in packet], GlyR [in packet], GLRA1 [in packet], glycine receptor alpha1 [in packet], anti-GlyR, GlyRα1

### C056 · Transverse Myelitis · AQP4-IgG (test, cutoff 2003-12-31)

- **Judgment:** For the 2003 cutoffs (all three cases since C056 was re-dated) the antigen was unknown at discovery (a tissue-staining pattern); T2 accepts an end-foot antigen named descriptively.
- **Note:** 'NMO' alone is not a leakage alarm: terms match whole and exact, so only 'NMO-IgG' and the like match.
- **T1:** AUTOIMMUNE_ANTIBODY; water transport (GO:0006833)
- **T2:** AUTOANTIBODY in serum, csf; members AQP4 (hgnc:637)
- **T3:** Indirect immunofluorescence on composite mouse tissue for an NMO-IgG staining pattern; masked sera from 102 North American patients with NMO or high-risk syndromes and 12 Japanese optic-spinal MS patients against MS and other controls; sensitivity and specificity. (PMID:15589308)
- **T4:** NMO-IgG / aquaporin-4 IgG; reachable pre-cutoff: no
- **Arm display name:** transverse myelitis
- **Leakage terms:** NMO-IgG, NMO IgG, AQP4-IgG, AQP4 IgG, anti-AQP4, aquaporin-4 antibody, aquaporin-4 antibodies, anti-aquaporin-4, aquaporin-4, aquaporin 4, AQP4, AQP-4, MIWC, mercurial-insensitive water channel

## No judgment needed (17 cases)

### C003 · Alzheimer Disease · CSF amyloid-beta 42 (dev, cutoff 1994-12-31)

- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): Abeta42 (1), A beta 42 (4), Aβ42 (1).
- **T1:** PROTEIN_AGGREGATION; amyloid-beta formation (GO:0034205)
- **T2:** PROTEIN_LEVEL in csf; members APP (hgnc:620), amyloid-beta polypeptide 42 (CHEBI:64647)
- **T3:** CSF amyloid-beta 42 measured in AD patients and controls, alongside total amyloid-beta, tau and APOE genotype; Abeta42 was lower in AD while total Abeta was not. (PMID:7574461)
- **T4:** amyloid-beta 1-42 in CSF; reachable pre-cutoff: yes (PMID:7699397)
- **Arm display name:** Alzheimer disease
- **Leakage terms:** Abeta42 [in packet], Abeta 42, A beta 42 [in packet], Aβ42 [in packet], Aβ1-42, amyloid beta 42, beta-amyloid 42, amyloid-beta 42, beta-amyloid peptide42, Abeta1-42

### C005 · Autoimmune Polyendocrine Syndrome Type 1 · anti-interferon-omega autoantibodies (test, cutoff 2005-12-31)

- **T1:** AUTOIMMUNE_ANTIBODY; type I interferon-mediated signaling pathway (GO:0060337)
- **T2:** AUTOANTIBODY in serum, plasma; members IFNW1 (hgnc:5448), IFNA1 (hgnc:5417), IFNA2 (hgnc:5423), IFNB1 (hgnc:5434)
- **T3:** Serum binding and neutralisation assays for autoantibodies to type I interferons and other cytokines in Finnish and Norwegian APS1 patients with biallelic AIRE mutations, against controls. (PMID:16784312)
- **T4:** neutralising IgG autoantibodies to interferon-omega (and interferon-alpha); reachable pre-cutoff: no
- **Arm display name:** autoimmune polyendocrinopathy syndrome type 1
- **Leakage terms:** anti-interferon, anti-IFN, anti-interferon-omega, anti-IFN-omega, IFN-omega, interferon-omega, interferon omega, IFN-ω, anti-type I interferon

### C014 · Dermatomyositis · anti-MDA5 antibodies (test, cutoff 2004-12-31)

- **Note:** The discovery paper identified the antigen only by its size (CADM-140); T4 names the later molecular identity, MDA5.
- **T1:** AUTOIMMUNE_ANTIBODY; cytoplasmic pattern recognition receptor signaling pathway (GO:0002753)
- **T2:** AUTOANTIBODY in serum; members IFIH1 (hgnc:18873)
- **T3:** Immunoprecipitation of 298 sera from connective tissue disease and IPF patients, finding a 140-kd antigen (CADM-140); immunoblot, immunofluorescence and clinical association with amyopathic DM and rapidly progressive ILD. (PMID:15880816)
- **T4:** autoantibodies to MDA5 (the 140-kd CADM-140 antigen); reachable pre-cutoff: no
- **Arm display name:** dermatomyositis
- **Leakage terms:** MDA5, MDA-5, IFIH1, melanoma differentiation-associated gene 5, CADM-140, CADM140, anti-MDA5, Helicard

### C017 · Glomerulonephritis · anti-PLA2R antibodies (test, cutoff 2008-12-31)

- **Note:** T2 is a single protein, so 'antibody to an unidentified podocyte antigen' has no T2 match and goes to adjudication.
- **T1:** AUTOIMMUNE_ANTIBODY; glomerular filtration (GO:0003094)
- **T2:** AUTOANTIBODY in serum; members PLA2R1 (hgnc:9042)
- **T3:** Western blot of normal human glomerular extract with sera from idiopathic and secondary MN, other renal and autoimmune diseases and controls; mass spectrometry identified PLA2R, confirmed with recombinant protein and a monospecific antibody. (PMID:19571279)
- **T4:** IgG4 autoantibodies to the M-type phospholipase A2 receptor; reachable pre-cutoff: yes (PMID:16159900)
- **Arm display name:** membranous glomerulonephritis
- **Leakage terms:** PLA2R, PLA(2)R, PLA2R1, phospholipase A2 receptor, M-type phospholipase A2 receptor, anti-PLA2R, PLA2-R, PLA2G1R, CLEC13C

### C022 · Late-Onset Pompe Disease · dried-blood-spot acid alpha-glucosidase activity (test, cutoff 2000-12-31)

- **Note:** The enzyme's names (acid maltase, GAA) define Pompe disease before the cutoff and are not leakage terms.
- **T1:** ENZYME_DEFICIENCY; alpha-1,4-glucosidase activity (GO:0004558)
- **T2:** ENZYME_ACTIVITY in dried_blood_spot; members GAA (hgnc:4065)
- **T1 only (in clinical use at cutoff):** leukocyte (or lymphocyte) acid alpha-glucosidase activity
- **T3:** Immune-capture acid alpha-glucosidase activity assay in dried blood spots from newborn and adult controls and Pompe-affected individuals. (PMID:11468225)
- **T4:** acid alpha-glucosidase activity in dried blood spots; reachable pre-cutoff: yes (PMID:7603530)
- **Arm display name:** adult-onset acid maltase deficiency
- **Leakage terms:** acid alpha-glucosidase activity in dried blood, blood spot acid alpha-glucosidase, dried blood spot GAA, DBS GAA

### C025 · Limbic Encephalitis · anti-GABAB receptor antibodies (dev, cutoff 2008-12-31)

- **T1:** AUTOIMMUNE_ANTIBODY; gamma-aminobutyric acid signaling pathway (GO:0007214)
- **T2:** AUTOANTIBODY in serum, csf; members GABBR1 (hgnc:4070), GABBR2 (hgnc:4507)
- **T3:** 15 patients with suspected immune-mediated limbic encephalitis; confocal microscopy, immunoprecipitation and mass spectrometry identified GABA(B1)/(B2); HEK293 cell-based assay against 91 encephalitis controls and 13 anti-GAD65 controls. (PMID:19962348)
- **T4:** IgG autoantibodies to the GABA(B1) receptor subunit; reachable pre-cutoff: no
- **Arm display name:** limbic encephalitis
- **Leakage terms:** GABA(B) receptor, GABAB receptor, GABA-B receptor, GABA(B1), GABBR1, GABBR2, anti-GABAB, GABAB1

### C026 · Limbic Encephalitis · anti-AMPA receptor antibodies (test, cutoff 2008-12-31)

- **Note:** The AMPA receptor and its subunits are standard pre-cutoff neuroscience terms.
- **T1:** AUTOIMMUNE_ANTIBODY; synaptic transmission, glutamatergic (GO:0035249)
- **T2:** AUTOANTIBODY in serum, csf; members GRIA1 (hgnc:4571), GRIA2 (hgnc:4572), GRIA3 (hgnc:4573), GRIA4 (hgnc:4574)
- **T3:** 10 limbic encephalitis patients; immunoprecipitation and mass spectrometry identified GluR1/GluR2; HEK293 cell-based assay and ELISA; effect of patient antibodies on live hippocampal neurons. (PMID:19338055)
- **T4:** IgG autoantibodies to the GluR1/GluR2 subunits of the AMPA receptor; reachable pre-cutoff: yes (PMID:17262855)
- **Arm display name:** limbic encephalitis
- **Leakage terms:** AMPA receptor, AMPAR, GluR1, GluR2, GluA1, GluA2, GRIA1, GRIA2, anti-AMPA, alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid receptor, GLURA, GLURB

### C027 · Lymphangioleiomyomatosis · serum VEGF-D (test, cutoff 2005-12-31)

- **T1:** GROWTH_FACTOR_EXCESS; lymphangiogenesis (GO:0001946)
- **T2:** PROTEIN_LEVEL in serum, plasma; members VEGFD (hgnc:3708)
- **T3:** ELISA of serum VEGF-A, VEGF-C and VEGF-D in 44 LAM patients and 24 matched healthy volunteers; only VEGF-D was raised. (PMID:17034294)
- **T4:** VEGF-D in serum; reachable pre-cutoff: yes (PMID:15252306)
- **Arm display name:** lymphangioleiomyomatosis
- **Leakage terms:** VEGF-D, VEGFD, FIGF, vascular endothelial growth factor D, vascular endothelial growth factor-D, c-fos-induced growth factor

### C029 · Membranous nephropathy · anti-PLA2R antibodies (test, cutoff 2008-12-31)

- **Note:** T2 is a single protein, so 'antibody to an unidentified podocyte antigen' has no T2 match and goes to adjudication.
- **T1:** AUTOIMMUNE_ANTIBODY; glomerular filtration (GO:0003094)
- **T2:** AUTOANTIBODY in serum; members PLA2R1 (hgnc:9042)
- **T3:** Western blot of normal human glomerular extract with sera from idiopathic and secondary MN, other renal and autoimmune diseases and controls; mass spectrometry identified PLA2R, confirmed with recombinant protein and a monospecific antibody. (PMID:19571279)
- **T4:** IgG4 autoantibodies to the M-type phospholipase A2 receptor; reachable pre-cutoff: yes (PMID:16159900)
- **Arm display name:** idiopathic membranous nephropathy
- **Leakage terms:** PLA2R, PLA(2)R, PLA2R1, phospholipase A2 receptor, M-type phospholipase A2 receptor, anti-PLA2R, PLA2-R, PLA2G1R, CLEC13C

### C034 · Narcolepsy-Cataplexy Syndrome · CSF hypocretin-1 (test, cutoff 1999-12-31)

- **Note:** Hypocretin/orexin was discovered in 1998 and linked to narcolepsy in animals in 1999, before the cutoff (the readiness paper), so these terms are in the packet.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): hypocretin (3), orexin (3).
- **T1:** NEUROPEPTIDE_DEFICIENCY; neuropeptide signaling pathway (GO:0007218)
- **T2:** PROTEIN_LEVEL in csf, plasma; members HCRT (hgnc:4847)
- **T3:** CSF hypocretin-1 measured in nine people with narcolepsy and controls; undetectable in seven of nine. (PMID:10615891)
- **T4:** hypocretin-1 (orexin-A) in CSF; reachable pre-cutoff: yes (PMID:10481909)
- **Arm display name:** narcolepsy with cataplexy
- **Leakage terms:** hypocretin [in packet], hypocretin-1, hypocretin 1, orexin [in packet], orexin-A, orexin A, HCRT, preprohypocretin, prepro-orexin

### C035 · Narcolepsy · CSF hypocretin-1 (test, cutoff 1999-12-31)

- **Note:** Hypocretin/orexin was discovered in 1998 and linked to narcolepsy in animals in 1999, before the cutoff (the readiness paper), so these terms are in the packet.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): hypocretin (3), orexin (3).
- **T1:** NEUROPEPTIDE_DEFICIENCY; neuropeptide signaling pathway (GO:0007218)
- **T2:** PROTEIN_LEVEL in csf, plasma; members HCRT (hgnc:4847)
- **T3:** CSF hypocretin-1 measured in nine people with narcolepsy and controls; undetectable in seven of nine. (PMID:10615891)
- **T4:** hypocretin-1 (orexin-A) in CSF; reachable pre-cutoff: yes (PMID:10481909)
- **Arm display name:** narcolepsy
- **Leakage terms:** hypocretin [in packet], hypocretin-1, hypocretin 1, orexin [in packet], orexin-A, orexin A, HCRT, preprohypocretin, prepro-orexin

### C045 · Pyridoxine-Dependent Epilepsy · alpha-aminoadipic semialdehyde (test, cutoff 2005-12-31)

- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): alpha-aminoadipic semialdehyde (1), α-aminoadipic semialdehyde (1), alpha-AASA (1), α-AASA (1), AASA (1), antiquitin (1), ALDH7A1 (1).
- **T1:** METABOLIC_PATHWAY_BLOCK; L-lysine catabolic process (GO:0019477)
- **T2:** METABOLITE in urine, plasma, csf; members L-allysine (CHEBI:17917), 1-piperideine-6-carboxylic acid (CHEBI:49015)
- **T1 only (in clinical use at cutoff):** plasma or CSF pipecolic acid
- **T3:** ALDH7A1 sequencing in children with pyridoxine-dependent seizures, showing loss of P6C/alpha-AASA dehydrogenase activity; urinary alpha-AASA proposed to confirm the diagnosis. (PMID:16491085)
- **T4:** urinary alpha-aminoadipic semialdehyde (alpha-AASA); reachable pre-cutoff: yes (PMID:15944906)
- **Arm display name:** pyridoxine-dependent epilepsy
- **Leakage terms:** alpha-aminoadipic semialdehyde [in packet], α-aminoadipic semialdehyde [in packet], alpha-AASA [in packet], α-AASA [in packet], AASA [in packet], piperideine-6-carboxylate, P6C, antiquitin [in packet], ALDH7A1 [in packet]

### C047 · Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect · erythrocyte plasmalogens (test, cutoff 1990-12-31)

- **Note:** The plasmalogen synthesis defect in RCDP is pre-cutoff (the readiness paper).
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): plasmalogen (8), plasmalogens (6), ether lipid (4).
- **T1:** METABOLIC_PATHWAY_BLOCK; ether lipid biosynthetic process (GO:0008611)
- **T2:** METABOLITE in erythrocytes, plasma; members 1-(alk-1-enyl)-2-acyl-sn-glycero-3-phosphoethanolamine (CHEBI:17476)
- **T1 only (in clinical use at cutoff):** plasma phytanic acid (a peroxisomal-disorder test in use before the cutoff)
- **T3:** Case report: a boy diagnosed with RCDP from high plasma phytanic acid and low erythrocyte plasmalogens, followed for 16 years. (PMID:1955304)
- **T4:** low erythrocyte plasmalogens; reachable pre-cutoff: yes (PMID:2452243)
- **Arm display name:** rhizomelic chondrodysplasia punctata
- **Leakage terms:** plasmalogen [in packet], plasmalogens [in packet], erythrocyte plasmalogen, plasmenylethanolamine, ether lipid [in packet], ether phospholipid

### C050 · Severe Combined Immunodeficiency · TREC newborn screening (dev, cutoff 2004-12-31)

- **Note:** TRECs as a marker of thymic output are pre-cutoff (the readiness paper), so these terms are in the packet.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): TREC (8), TRECs (2), T-cell receptor excision circle (3), T-cell receptor excision circles (2), T cell receptor excision circles (2).
- **T1:** THYMIC_OUTPUT_FAILURE; T cell differentiation in thymus (GO:0033077)
- **T2:** CELLULAR_DNA_MEASURE in dried_blood_spot, whole_blood; members T cell differentiation in thymus (GO:0033077)
- **T3:** Real-time PCR for TRECs in DNA from dried blood spots (beta-actin control) in adult and cord-blood controls, spotted SCID patient blood, routine Maryland newborn screening spots and archived spots of two infants later diagnosed with SCID. (PMID:15696101)
- **T4:** T-cell receptor excision circles by real-time PCR in dried blood spots; reachable pre-cutoff: yes (PMID:11715066)
- **Arm display name:** severe combined immunodeficiency
- **Leakage terms:** TREC [in packet], TRECs [in packet], T-cell receptor excision circle [in packet], T-cell receptor excision circles [in packet], T cell receptor excision circles [in packet], sjTREC, signal-joint TREC

### C051 · Smith-Lemli-Opitz syndrome · serum 7-dehydrocholesterol (test, cutoff 1993-12-31)

- **Note:** The pre-cutoff readiness letter (Irons 1993) has no abstract, so the co-occurrence counts cannot see it.
- **Note:** Leakage terms in the packet (in_packet yes; they cannot raise an alarm): 7-dehydrocholesterol (1), 7-DHC (1), 7DHC (1), DHCR7 (1), 7-dehydrocholesterol reductase (1), dehydrocholesterol (1).
- **T1:** METABOLIC_PATHWAY_BLOCK; cholesterol biosynthetic process (GO:0006695)
- **T2:** METABOLITE in serum, plasma, erythrocytes; members cholesta-5,7-dien-3beta-ol (CHEBI:17759), 8-Dehydrocholesterol (CHEBI:89982)
- **T3:** Capillary-column GC-MS of sterols in plasma, erythrocytes, lens, cultured fibroblasts and faeces of five children with SLOS against controls. (PMID:8259166)
- **T4:** raised 7-dehydrocholesterol in serum or plasma; reachable pre-cutoff: yes (PMID:7684480)
- **Arm display name:** Smith-Lemli-Opitz syndrome
- **Leakage terms:** 7-dehydrocholesterol [in packet], 7-DHC [in packet], 7DHC [in packet], cholesta-5,7-dien-3beta-ol, cholesta-5,7-dien-3 beta-ol, 8-dehydrocholesterol, DHCR7 [in packet], 7-dehydrocholesterol reductase [in packet], dehydrocholesterol [in packet]

### C054 · Stiff Person Syndrome · anti-amphiphysin antibodies (test, cutoff 1992-12-31)

- **Note:** The discovery paper identified the antigen only by size (128 kd); T4 names the identity published the same year.
- **T1:** AUTOIMMUNE_ANTIBODY; synaptic vesicle endocytosis (GO:0048488)
- **T2:** AUTOANTIBODY in serum, csf; members AMPH (hgnc:471)
- **T3:** Serum and CSF of three women with stiff-man syndrome and breast cancer screened by immunocytochemistry, Western blot and immunoprecipitation, finding antibodies to a 128-kd synaptic protein; GAD antibodies were negative. (PMID:8381208)
- **T4:** autoantibodies to amphiphysin (the 128-kd synaptic protein); reachable pre-cutoff: no
- **Arm display name:** stiff-man syndrome
- **Leakage terms:** amphiphysin, AMPH, 128-kd synaptic protein, 128-kd brain protein, anti-amphiphysin

### C057 · X-Linked Nephrogenic Diabetes Insipidus · basal plasma copeptin (test, cutoff 2010-12-31)

- **Note:** Copeptin is named in the pre-cutoff readiness paper.
- **T1:** HORMONE_SECRETION_OR_ACTION_DEFECT; vasopressin secretion (GO:0030103)
- **T2:** PROTEIN_LEVEL in plasma, serum; members copeptin (C-terminal glycopeptide of pre-pro-vasopressin) (hgnc:894)
- **T1 only (in clinical use at cutoff):** plasma arginine vasopressin (AVP), measured in the water deprivation test
- **T3:** Water deprivation test with plasma AVP and copeptin in 20 healthy subjects and 50 patients with polydipsia-polyuria, against a reference diagnosis from clinical information and treatment response. (PMID:21367924)
- **T4:** copeptin (C-terminal pro-vasopressin) in plasma; reachable pre-cutoff: yes (PMID:11091117)
- **Arm display name:** nephrogenic diabetes insipidus
- **Leakage terms:** copeptin, CT-proAVP, CTproAVP, C-terminal pro-vasopressin, C-terminal provasopressin, C-terminal portion of provasopressin

## Negatives (18)

Any candidate proposed as a confirmatory accessible-specimen test for this disease (blood, serum, plasma, dried blood spot, urine or CSF; germline sequencing excluded) is a false positive, at whatever tier it would otherwise reach. The measurable nodes listed are what an arm is most likely to propose; each is nonspecific.

- **N01 Hypermobile Ehlers-Danlos Syndrome** (ORIGINAL; H3 usable no; cutoff 1987-12-31, literature INSUFFICIENT_PRE_CUTOFF_LITERATURE 2; monogenic germline no): likely false positives: none (no measurable node).
- **N02 Kawasaki Disease** (ORIGINAL; H3 usable yes; cutoff 2000-12-31, literature PASS 1550; monogenic germline no): likely false positives: Leukocytosis; Erythrocyte Sedimentation Rate (ESR); Platelet Count.
- **N03 Sarcoidosis** (ORIGINAL; H3 usable yes; cutoff 1993-12-31, literature PASS 4680; monogenic germline no): likely false positives: Leukopenia.
- **N04 Behcet's Disease** (ORIGINAL; H3 usable no; cutoff 1987-12-31, literature PASS 638; monogenic germline no): likely false positives: none (no measurable node).
- **N05 Complex Regional Pain Syndrome Type 1** (ORIGINAL; H3 usable no; cutoff 2007-12-31, literature PASS 2888; monogenic germline no): likely false positives: none (no measurable node).
- **N06 Takayasu Arteritis** (ORIGINAL; H3 usable yes; cutoff 2004-12-31, literature PASS 1454; monogenic germline no): likely false positives: Erythrocyte Sedimentation Rate (ESR).
- **N07 Juvenile Idiopathic Arthritis** (DRAW_SEED_20261114_NEXT; H3 usable yes; cutoff 2011-12-31, literature PASS 5812; monogenic germline no): likely false positives: Elevated erythrocyte sedimentation rate; Antinuclear antibody positivity; Increased serum interferon-gamma level.
- **N08 Soil-transmitted helminthiases** (DRAW_SEED_20261114_NEXT; H3 usable no; cutoff 1984-12-31, literature PASS 8327; monogenic germline no): likely false positives: Blood-feeding hookworms cause iron deficiency anemia.
- **N09 Congenital Merosin-deficient Muscular Dystrophy 1A** (DRAW_SEED_20261114_NEXT; H3 usable yes; cutoff 2019-12-31, literature PASS 145; monogenic germline yes): likely false positives: Elevated serum creatine kinase.
- **N10 Deficiency of the Interleukin-1 Receptor Antagonist** (DRAW_SEED_20261114_SCREENED; H3 usable yes; cutoff 2010-12-31, literature PASS 33; monogenic germline yes): likely false positives: Leukocytosis.
- **N11 Limb-Girdle Muscular Dystrophy, Autosomal Dominant** (DRAW_SEED_20261114; H3 usable yes; cutoff 2003-12-31, literature PASS 31; monogenic germline yes): likely false positives: Elevated Serum Creatine Kinase.
- **N12 Hereditary Angioedema** (DRAW_SEED_20261114_NEXT; H3 usable no; cutoff 1991-12-31, literature PASS 586; monogenic germline yes): likely false positives: Plasma kallikrein activation.
- **N13 Lipoprotein Glomerulopathy** (DRAW_SEED_20261114_SCREENED; H3 usable yes; cutoff 2000-12-31, literature PASS 325; monogenic germline yes): likely false positives: Elevated serum apolipoprotein E.
- **N14 Choroid Plexus Neoplasm** (DRAW_SEED_20261114; H3 usable no; cutoff 2010-12-31, literature PASS 43; monogenic germline no): likely false positives: Cerebrospinal Fluid Overproduction by Secretory Tumour Epithelium.
- **N15 Psoriasis** (DRAW_SEED_20261114_NEXT; H3 usable yes; cutoff 1997-12-31, literature PASS 7576; monogenic germline no): likely false positives: Leukocytosis.
- **N16 Angiomatoid Fibrous Histiocytoma** (DRAW_SEED_20261114; H3 usable yes; cutoff 1992-12-31, literature PASS 36; monogenic germline no): likely false positives: Elevated inflammatory markers.
- **N17 Congenital Hydrocephalus** (DRAW_SEED_20261114_SCREENED; H3 usable no; cutoff 2005-12-31, literature PASS 397; monogenic germline no): likely false positives: Choroid Plexus CSF Hypersecretion; Impaired CSF Absorption and Perivascular Clearance.
- **N18 Peeling Skin Syndrome** (DRAW_SEED_20261114_NEXT; H3 usable yes; cutoff 2008-12-31, literature PASS 3335; monogenic germline yes): likely false positives: Elevated circulating IgE.
