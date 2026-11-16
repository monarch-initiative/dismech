"""Write the per-case scoring rubrics (DRAFT, for human review).

One YAML per verified case in dating.tsv (dev and test) and one per negative in
negatives.tsv, under rubrics/, plus rubrics/rubrics_review.md.

Each positive rubric is drafted from the case row (dating.tsv) and the case's
discovery paper only. The tiers follow README.md, *Scoring*:
  T1  mechanism_class (enum below) and a GO process or function; a candidate
      reaches T1 when its mechanism class matches and its GO term is the
      rubric's or a descendant of it.
  T2  analyte_type (enum below) + allowed specimens + target class. The target
      class is an anchor term plus an explicit member list; a candidate's
      target must be one of the members.
  T3  the discovery experiment, as the discovery paper describes it.
  T4  the exact analyte, with reachable_from_pre_cutoff: "yes" with the case's
      mechanistic-readiness PMID, which dating.tsv already checks predates the
      cutoff, or "no".
  leakage_terms names, synonyms and abbreviations of the test and analyte
      (revision 2; formerly banned_terms). They are never stripped from
      packets, which are pre-cutoff by construction.
      The lists are hand-written. HGNC exact synonyms of each T4 gene were
      read from hgnc.db and only the ones naming the analyte were copied in;
      the rest are clone IDs, disease names or common words ("NF", "OX",
      "TTP", "stiff person syndrome"), which would strip unrelated text.
      For each term, pre_cutoff_hits is the PubMed count of the term (title or
      abstract; a multi-word term by the proximity form [tiab:~0], since quoted
      phrases miss PubMed's phrase index) together with the case's
      literature-check query, published on
      or before the cutoff; in_packet is yes when it is above 0. A leakage term
      with in_packet no that appears in a curated entry or an arm's output is a
      leakage alarm (the audit is not built yet).
  arm_display_name  the only disease name an arm sees (DISPLAY, NEG_DISPLAY),
      checked by PubMed count before the cutoff and against the leakage terms.

Every ontology identifier is resolved here by exact label from the local
semsql builds (~/.data/oaklib/{go,chebi,hgnc}.db); the script stops on a label
that does not resolve to exactly one term. Nothing is written from memory.

NCBI_API_KEY is read from the environment, sent only in POST bodies, and never
printed. PubMed counts are cached under tmp/rubric_cache/.

Usage:
    uv run python experiments/diagnostic_retrodiction/build_rubrics.py
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "rubrics"
CACHE = ROOT / "tmp" / "rubric_cache"
OAK = Path.home() / ".data" / "oaklib"

MECHANISM_CLASSES = {
    "AUTOIMMUNE_ANTIBODY": "autoantibody against a self antigen drives or marks the disease",
    "DRUG_DEPENDENT_ANTIBODY": "antibody that forms against a drug-protein complex",
    "ENZYME_DEFICIENCY": "loss or inhibition of an enzyme activity",
    "METABOLIC_PATHWAY_BLOCK": "a blocked pathway step raises or lowers a metabolite",
    "TRANSPORTER_DEFECT": "loss of a solute transporter lowers the solute across a barrier",
    "PROTEIN_AGGREGATION": "pathological processing or aggregation of a protein",
    "NEUROPEPTIDE_DEFICIENCY": "loss of the neurons that make a neuropeptide",
    "HORMONE_SECRETION_OR_ACTION_DEFECT": "deficient hormone secretion or end-organ resistance",
    "GROWTH_FACTOR_EXCESS": "a lesion secretes excess growth factor",
    "TELOMERE_MAINTENANCE_DEFECT": "defective telomere maintenance shortens telomeres",
    "THYMIC_OUTPUT_FAILURE": "absent or reduced production of new T cells",
    "GPI_ANCHOR_DEFICIENCY": "a clone lacks GPI-anchored surface proteins",
    "SOMATIC_KINASE_ACTIVATION": "an acquired activating kinase mutation in a clone",
    "BILE_ACID_SYNTHESIS_UPREGULATION": "loss of feedback raises hepatic bile acid synthesis",
}
ANALYTE_TYPES = {"AUTOANTIBODY", "ENZYME_ACTIVITY", "METABOLITE", "PROTEIN_LEVEL", "CELL_SURFACE_MARKER",
                 "SOMATIC_VARIANT", "CELLULAR_DNA_MEASURE"}
SPECIMENS = {"serum", "plasma", "whole_blood", "dried_blood_spot", "leukocytes", "lymphocytes", "granulocytes",
             "monocytes", "erythrocytes", "platelets", "urine", "csf"}


# ---------------------------------------------------------------- the rubric table
# One entry per test_group (cases sharing a test share the rubric body), keyed by
# test_group as in dating.tsv. Ontology terms are (db, exact label).
#   t1: (mechanism_class, (db, label))
#   t2: analyte_type, specimens, anchor, members, note
#   t3: by discovery PMID (below)
#   t4: label, terms, qualifier
#   banned: hand-written names; HGNC synonyms of t4 genes are added
#   judgment: one-line reasons a T2 boundary or banned term needed a call;
#             "NOTE: " marks information rather than a call, and "ONLY Cxxx: "
#             limits an item to the cases named
G = {
    "ADAMTS13 activity": dict(
        t1=("ENZYME_DEFICIENCY", ("go", "metalloendopeptidase activity")),
        t2=dict(type="ENZYME_ACTIVITY", specimens=["plasma"], anchor=("go", "metalloendopeptidase activity"),
                members=[("hgnc", "ADAMTS13")],
                note="Activity of the von Willebrand factor-cleaving protease. An antibody or inhibitor "
                     "against it is analyte_type AUTOANTIBODY and reaches T1 at most."),
        t4=dict(label="ADAMTS13 (von Willebrand factor-cleaving protease) activity in plasma",
                terms=[("hgnc", "ADAMTS13")], qualifier="severely reduced activity"),
        banned=["ADAMTS13", "ADAMTS-13", "von Willebrand factor-cleaving protease", "vWF-cleaving protease",
                "VWF-cleaving protease", "VWF-CP", "vWF-CP", "VWFCP"],
        judgment=["The discovery paper reports both deficiency and an inhibitor; T2 is fixed to enzyme "
                  "activity, so an inhibitor or anti-ADAMTS13 candidate reaches T1 only."]),
    "plasma p-tau217": dict(
        t1=("PROTEIN_AGGREGATION", ("go", "neurofibrillary tangle assembly")),
        t2=dict(type="PROTEIN_LEVEL", specimens=["plasma", "serum"], anchor=("hgnc", "MAPT"),
                members=[("hgnc", "MAPT")],
                note="Any phosphorylated tau species in blood. CSF tau is outside the specimen set."),
        t4=dict(label="tau phosphorylated at threonine 217 (p-tau217) in plasma", terms=[("hgnc", "MAPT")],
                qualifier="phospho-Thr217 proteoform"),
        banned=["p-tau217", "P-tau217", "pTau217", "p-tau 217", "phospho-tau217", "phosphorylated tau 217",
                "tau phosphorylated at threonine 217", "pT217"],
        judgment=["IMPROVEMENT case: plasma p-tau181 or total tau meet T2 (same target, blood); CSF tau does "
                  "not. Only the 217 site is banned, because tau and p-tau are pre-cutoff terms."]),
    "CSF amyloid-beta 42": dict(
        t1=("PROTEIN_AGGREGATION", ("go", "amyloid-beta formation")),
        t2=dict(type="PROTEIN_LEVEL", specimens=["csf"], anchor=("hgnc", "APP"),
                members=[("hgnc", "APP"), ("chebi", "amyloid-beta polypeptide 42")],
                note="Any amyloid-beta species in CSF."),
        t4=dict(label="amyloid-beta 1-42 in CSF", terms=[("chebi", "amyloid-beta polypeptide 42")],
                qualifier="reduced"),
        banned=["Abeta42", "Abeta 42", "A beta 42", "Aβ42", "Aβ1-42", "amyloid beta 42", "beta-amyloid 42",
                "amyloid-beta 42", "beta-amyloid peptide42", "Abeta1-42"],
        judgment=[]),
    "anti-type I interferon autoantibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "type I interferon-mediated signaling pathway")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "plasma"],
                anchor=("go", "type I interferon-mediated signaling pathway"),
                members=[("hgnc", "IFNW1"), ("hgnc", "IFNA1"), ("hgnc", "IFNA2"), ("hgnc", "IFNB1")],
                note="Neutralising antibodies to any type I interferon."),
        t4=dict(label="neutralising IgG autoantibodies to interferon-omega (and interferon-alpha)",
                terms=[("hgnc", "IFNW1")], qualifier="neutralising IgG"),
        banned=["anti-interferon", "anti-IFN", "anti-interferon-omega", "anti-IFN-omega", "IFN-omega",
                "interferon-omega", "interferon omega", "IFN-ω", "anti-type I interferon"],
        judgment=[]),
    "anti-GM-CSF autoantibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "granulocyte-macrophage colony-stimulating factor signaling pathway")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "plasma"],
                anchor=("go", "granulocyte-macrophage colony-stimulating factor signaling pathway"),
                members=[("hgnc", "CSF2")], note="Antibody to GM-CSF in blood."),
        t4=dict(label="neutralising IgG autoantibody to GM-CSF in serum", terms=[("hgnc", "CSF2")],
                qualifier="neutralising IgG"),
        banned=["anti-GM-CSF", "GM-CSF autoantibody", "GM-CSF antibody", "anti-granulocyte-macrophage colony-stimulating factor"],
        judgment=["The discovery paper found the antibody first in bronchoalveolar lavage fluid, which is "
                  "not an accessible specimen; T2 allows only serum and plasma, where it was also found.",
                  "GM-CSF itself is not banned: GM-CSF signalling in pulmonary alveolar proteinosis is "
                  "pre-cutoff literature (the readiness paper)."]),
    "urinary N-acetylaspartic acid": dict(
        t1=("ENZYME_DEFICIENCY", ("go", "aspartoacylase activity")),
        t2=dict(type="METABOLITE", specimens=["urine", "plasma"], anchor=("chebi", "N-acyl-L-aspartic acid"),
                members=[("chebi", "N-acetyl-L-aspartic acid")], note="N-acetylaspartate in urine or blood."),
        t4=dict(label="N-acetylaspartic acid in urine", terms=[("chebi", "N-acetyl-L-aspartic acid")],
                qualifier="increased"),
        banned=["N-acetylaspartic acid", "N-acetylaspartate", "N-acetyl-L-aspartic acid", "N-acetylaspartic aciduria",
                "aspartoacylase", "NAA"],
        judgment=["'NAA' is a generic abbreviation, and N-acetylaspartate is a well-known pre-cutoff brain "
                  "metabolite; banning it strips unrelated text.",
                  "NOTE: The discovery paper's aspartoacylase assay used cultured fibroblasts, so it is not an "
                  "accessible-specimen T2 hit."]),
    "anti-tissue transglutaminase IgA": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "peptide cross-linking")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "plasma"],
                anchor=("go", "protein-glutamine gamma-glutamyltransferase activity"),
                members=[("hgnc", "TGM2")],
                note="Antibody to tissue transglutaminase, either isotype. Endomysial antibodies name a "
                     "tissue, not a molecule, and reach T1 only."),
        t4=dict(label="IgA antibody to tissue transglutaminase by ELISA", terms=[("hgnc", "TGM2")],
                qualifier="IgA isotype"),
        banned=["tissue transglutaminase", "transglutaminase 2", "tTG", "TG2", "anti-tTG", "anti-transglutaminase",
                "tTGA", "tTG-IgA"],
        judgment=["Endomysial antibody (a pre-cutoff test) is excluded from T2 by naming its tissue, not "
                  "tTG.",
                  "NOTE: 'tissue transglutaminase' is named in the pre-cutoff readiness paper (Dieterich 1997)."]),
    "CSF glucose for GLUT1 deficiency": dict(
        t1=("TRANSPORTER_DEFECT", ("go", "D-glucose transmembrane transport")),
        t2=dict(type="METABOLITE", specimens=["csf"], anchor=("chebi", "D-glucose"),
                members=[("chebi", "D-glucose")],
                note="CSF glucose, or the CSF:blood glucose ratio. The erythrocyte glucose-uptake assay is "
                     "a transport assay, not a metabolite level, and reaches T1 only."),
        t4=dict(label="low CSF glucose (hypoglycorrhachia), CSF:blood glucose ratio", terms=[("chebi", "D-glucose")],
                qualifier="decreased"),
        banned=["hypoglycorrhachia", "CSF glucose", "cerebrospinal fluid glucose", "CSF/blood glucose ratio",
                "CSF/serum glucose ratio", "GLUT1", "GLUT-1", "Glut1 deficiency", "glucose transporter type 1",
                "glucose transporter 1", "SLC2A1", "De Vivo disease"],
        judgment=["CSF glucose is a routine measurement, and GLUT1 deficiency syndrome was named in 1991; "
                  "banning these terms strips pre-cutoff literature, including the readiness paper.",
                  "The case is the GLUT1-deficiency subset, so the subset name is itself banned."]),
    "anti-neurofascin antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "paranodal junction assembly")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "paranodal junction assembly"),
                members=[("hgnc", "NFASC"), ("hgnc", "CNTN1"), ("hgnc", "CNTNAP1")],
                note="Antibody to any protein of the paranodal axoglial complex."),
        t4=dict(label="IgG (often IgG4) autoantibodies to neurofascin-155", terms=[("hgnc", "NFASC")],
                qualifier="NF155 isoform"),
        banned=["neurofascin", "NF155", "NF186", "NFASC", "anti-neurofascin", "anti-NF155"],
        judgment=["T2 is the paranodal complex (neurofascin, contactin-1, CASPR1) rather than neurofascin "
                  "alone, so the neurofascin and contactin-1 cases share a T2 class."]),
    "anti-contactin-1 antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "paranodal junction assembly")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "paranodal junction assembly"),
                members=[("hgnc", "NFASC"), ("hgnc", "CNTN1"), ("hgnc", "CNTNAP1")],
                note="Antibody to any protein of the paranodal axoglial complex."),
        t4=dict(label="IgG (often IgG4) autoantibodies to contactin-1", terms=[("hgnc", "CNTN1")], qualifier=""),
        banned=["contactin-1", "contactin 1", "CNTN1", "anti-contactin", "anti-CNTN1", "CASPR1",
                "contactin-associated protein 1"],
        judgment=["T2 is the paranodal complex (neurofascin, contactin-1, CASPR1), shared with the "
                  "neurofascin case."]),
    "anti-MDA5 antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "cytoplasmic pattern recognition receptor signaling pathway")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum"],
                anchor=("go", "cytoplasmic pattern recognition receptor signaling pathway"),
                members=[("hgnc", "IFIH1")], note="Antibody to MDA5."),
        t4=dict(label="autoantibodies to MDA5 (the 140-kd CADM-140 antigen)", terms=[("hgnc", "IFIH1")], qualifier=""),
        banned=["MDA5", "MDA-5", "IFIH1", "melanoma differentiation-associated gene 5", "CADM-140", "CADM140",
                "anti-MDA5", "Helicard"],
        judgment=["NOTE: The discovery paper identified the antigen only by its size (CADM-140); T4 names the "
                  "later molecular identity, MDA5."]),
    "leukocyte telomere length by flow-FISH": dict(
        t1=("TELOMERE_MAINTENANCE_DEFECT", ("go", "telomere maintenance")),
        t2=dict(type="CELLULAR_DNA_MEASURE", specimens=["leukocytes", "lymphocytes", "whole_blood"],
                anchor=("go", "chromosome, telomeric region"), members=[("go", "chromosome, telomeric region")],
                note="Telomere length in blood cells by any method (TRF Southern blot, qPCR or flow-FISH)."),
        t4=dict(label="very short lymphocyte telomere length (<1st percentile for age) by flow-FISH",
                terms=[("go", "chromosome, telomeric region")], qualifier="flow-FISH in lymphocyte subsets"),
        banned=["flow-FISH", "flow FISH", "flow fluorescence in situ hybridization", "very short telomeres",
                "telomere length"],
        judgment=["Blood telomere length was measured before the cutoff (by Southern blot); T2 accepts any "
                  "method, and T4 requires flow-FISH.",
                  "'telomere length' is banned although it is pre-cutoff literature, including the readiness "
                  "paper."]),
    "anti-PLA2R antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "glomerular filtration")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum"], anchor=("hgnc", "PLA2R1"), members=[("hgnc", "PLA2R1")],
                note="Antibody to a podocyte antigen. A named podocyte antigen other than PLA2R is "
                     "adjudicated, not matched."),
        t4=dict(label="IgG4 autoantibodies to the M-type phospholipase A2 receptor", terms=[("hgnc", "PLA2R1")],
                qualifier="mainly IgG4"),
        banned=["PLA2R", "PLA(2)R", "PLA2R1", "phospholipase A2 receptor", "M-type phospholipase A2 receptor",
                "anti-PLA2R", "PLA2-R", "PLA2G1R", "CLEC13C"],
        judgment=["NOTE: T2 is a single protein, so 'antibody to an unidentified podocyte antigen' has no T2 "
                  "match and goes to adjudication."]),
    "anti-PF4/heparin IgG": dict(
        t1=("DRUG_DEPENDENT_ANTIBODY", ("go", "platelet activation")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "plasma"], anchor=("hgnc", "PF4"),
                members=[("hgnc", "PF4"), ("chebi", "heparin")],
                note="Antibody to PF4, or to a PF4-heparin complex. Functional platelet-activation assays "
                     "(serotonin release, HIPA) name no molecular target and reach T1/T3 only."),
        t4=dict(label="IgG antibody to platelet factor 4-heparin complexes (immunoassay)",
                terms=[("hgnc", "PF4"), ("chebi", "heparin")], qualifier="IgG; PF4 complexed with heparin"),
        banned=["PF4", "platelet factor 4", "PF4/heparin", "PF4-heparin", "anti-PF4", "PF4/H",
                "heparin-PF4"],
        judgment=["IMPROVEMENT case: the pre-cutoff functional tests detect the same antibody, but T2 "
                  "requires PF4 as the target, so they reach T1/T3 only.",
                  "NOTE: PF4 is named in the pre-cutoff readiness paper, so banning it strips that evidence."]),
    "acid alpha-glucosidase activity": dict(
        t1=("ENZYME_DEFICIENCY", ("go", "alpha-1,4-glucosidase activity")),
        t2=dict(type="ENZYME_ACTIVITY", specimens=["dried_blood_spot", "whole_blood", "leukocytes", "lymphocytes"],
                anchor=("go", "alpha-1,4-glucosidase activity"), members=[("hgnc", "GAA")],
                note="Acid alpha-glucosidase activity in any blood-derived specimen."),
        t4=dict(label="acid alpha-glucosidase activity in dried blood spots", terms=[("hgnc", "GAA")],
                qualifier="dried blood spot (immune-capture assay)"),
        banned=["acid alpha-glucosidase activity in dried blood", "blood spot acid alpha-glucosidase",
                "dried blood spot GAA", "DBS GAA"],
        judgment=["The enzyme (acid maltase, GAA) defines Pompe disease long before the cutoff, so only "
                  "test-specific phrases are banned, not the enzyme's names.",
                  "T2 accepts leukocyte GAA, a pre-cutoff assay, so T2 is reachable from pre-cutoff "
                  "literature; T4 needs the dried blood spot."]),
    "anti-LGI1 antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "regulation of potassium ion transmembrane transport")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "voltage-gated potassium channel complex"),
                members=[("hgnc", "LGI1"), ("hgnc", "ADAM22"), ("hgnc", "ADAM23")],
                note="Antibody to LGI1 or its ADAM22/23 receptors. 'VGKC-complex antibody' (radioimmunoassay, "
                     "antigen unspecified) reaches T1 only."),
        t4=dict(label="IgG autoantibodies to LGI1", terms=[("hgnc", "LGI1")], qualifier=""),
        banned=["LGI1", "leucine-rich glioma-inactivated 1", "leucine-rich, glioma inactivated 1", "anti-LGI1",
                "LGI1 antibody", "epitempin"],
        judgment=["The VGKC-complex antibody was the pre-cutoff test; it is kept out of T2, so T2 is not "
                  "reachable merely by proposing it."]),
    "anti-CASPR2 antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "regulation of potassium ion transmembrane transport")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "voltage-gated potassium channel complex"),
                members=[("hgnc", "CNTNAP2")],
                note="Antibody to CASPR2. 'VGKC-complex antibody' reaches T1 only."),
        t4=dict(label="IgG autoantibodies to contactin-associated protein-2", terms=[("hgnc", "CNTNAP2")], qualifier=""),
        banned=["CASPR2", "Caspr2", "CNTNAP2", "contactin-associated protein-2", "contactin-associated protein 2",
                "contactin-associated protein-like 2", "anti-CASPR2"],
        judgment=["The VGKC-complex antibody was the pre-cutoff test; it is kept out of T2."]),
    "anti-GABAB receptor antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "gamma-aminobutyric acid signaling pathway")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "gamma-aminobutyric acid signaling pathway"),
                members=[("hgnc", "GABBR1"), ("hgnc", "GABBR2")], note="Antibody to either GABA(B) subunit."),
        t4=dict(label="IgG autoantibodies to the GABA(B1) receptor subunit", terms=[("hgnc", "GABBR1")], qualifier=""),
        banned=["GABA(B) receptor", "GABAB receptor", "GABA-B receptor", "GABA(B1)", "GABBR1", "GABBR2",
                "anti-GABAB", "GABAB1"],
        judgment=[]),
    "anti-AMPA receptor antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "synaptic transmission, glutamatergic")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "AMPA glutamate receptor complex"),
                members=[("hgnc", "GRIA1"), ("hgnc", "GRIA2"), ("hgnc", "GRIA3"), ("hgnc", "GRIA4")],
                note="Antibody to any AMPA receptor subunit."),
        t4=dict(label="IgG autoantibodies to the GluR1/GluR2 subunits of the AMPA receptor",
                terms=[("hgnc", "GRIA1"), ("hgnc", "GRIA2")], qualifier=""),
        banned=["AMPA receptor", "AMPAR", "GluR1", "GluR2", "GluA1", "GluA2", "GRIA1", "GRIA2",
                "anti-AMPA", "alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid receptor",
                "GLURA", "GLURB"],
        judgment=["NOTE: The AMPA receptor and its subunits are standard pre-cutoff neuroscience terms; banning "
                  "them strips any pre-cutoff link to limbic encephalitis."]),
    "serum VEGF-D": dict(
        t1=("GROWTH_FACTOR_EXCESS", ("go", "lymphangiogenesis")),
        t2=dict(type="PROTEIN_LEVEL", specimens=["serum", "plasma"], anchor=("go", "lymphangiogenesis"),
                members=[("hgnc", "VEGFD"), ("hgnc", "VEGFC")], note="Either lymphangiogenic VEGF in blood."),
        t4=dict(label="VEGF-D in serum", terms=[("hgnc", "VEGFD")], qualifier="increased"),
        banned=["VEGF-D", "VEGFD", "FIGF", "vascular endothelial growth factor D", "vascular endothelial growth factor-D",
                "c-fos-induced growth factor"],
        judgment=["T2 includes VEGF-C, which the discovery paper measured and found not raised; that is "
                  "a deliberate class boundary."]),
    "MOG-IgG": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "myelination")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("hgnc", "MOG"), members=[("hgnc", "MOG")],
                note="Antibody to MOG by any assay. Linear-epitope ELISA or Western blot counts at T2; T4 "
                     "requires native (conformational) MOG."),
        t4=dict(label="IgG to native myelin oligodendrocyte glycoprotein by cell-based assay", terms=[("hgnc", "MOG")],
                qualifier="native MOG, cell-based assay"),
        banned=["MOG-IgG", "MOG IgG", "anti-MOG", "MOG antibody", "MOG antibodies", "myelin oligodendrocyte glycoprotein antibody",
                "MOGAD", "MOG antibody-associated disease", "nMOG"],
        judgment=["Anti-MOG ELISA and Western blot studies, which were nonspecific, predate the cutoff; T2 "
                  "accepts them and T4 requires the native-MOG cell-based assay.",
                  "ONLY C028: MOGAD is named after its test, so the disease name is itself a banned term."]),
    "plasma DOPA:DHPG ratio": dict(
        t1=("ENZYME_DEFICIENCY", ("go", "norepinephrine biosynthetic process")),
        t2=dict(type="METABOLITE", specimens=["plasma", "csf"], anchor=("chebi", "catechol"),
                members=[("chebi", "L-dopa"), ("chebi", "3,4-dihydroxyphenylethyleneglycol"),
                         ("chebi", "(3,4-dihydroxyphenyl)acetic acid"), ("chebi", "dopamine"), ("chebi", "noradrenaline")],
                note="Any catechol level or ratio reflecting dopamine-beta-hydroxylase. Serum copper and "
                     "ceruloplasmin are the pre-existing tests and reach T1 only."),
        t4=dict(label="plasma DOPA:DHPG ratio", terms=[("chebi", "L-dopa"), ("chebi", "3,4-dihydroxyphenylethyleneglycol")],
                qualifier="increased ratio"),
        banned=["DOPA:DHPG", "DOPA/DHPG", "DOPAC:DHPG", "DHPG", "dihydroxyphenylglycol", "plasma catechols",
                "plasma neurochemical"],
        judgment=["IMPROVEMENT case: copper and ceruloplasmin are left at T1. DOPA, DOPAC and "
                  "noradrenaline are too generic to ban alone."]),
    "anti-MuSK antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "neuromuscular junction development")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum"], anchor=("go", "neuromuscular junction development"),
                members=[("hgnc", "MUSK"), ("hgnc", "LRP4")],
                note="Antibody to a postsynaptic neuromuscular-junction protein other than the AChR."),
        t4=dict(label="IgG autoantibodies to muscle-specific kinase (MuSK)", terms=[("hgnc", "MUSK")], qualifier=""),
        banned=["MuSK", "MUSK", "muscle-specific kinase", "muscle-specific receptor tyrosine kinase", "muscle specific kinase",
                "anti-MuSK"],
        judgment=["T2 includes LRP4, whose antibodies were described only years later; this is a "
                  "deliberate class boundary (postsynaptic non-AChR targets)."]),
    "CSF hypocretin-1": dict(
        t1=("NEUROPEPTIDE_DEFICIENCY", ("go", "neuropeptide signaling pathway")),
        t2=dict(type="PROTEIN_LEVEL", specimens=["csf", "plasma"], anchor=("hgnc", "HCRT"), members=[("hgnc", "HCRT")],
                note="Either hypocretin peptide, in CSF or blood."),
        t4=dict(label="hypocretin-1 (orexin-A) in CSF", terms=[("hgnc", "HCRT")], qualifier="undetectable or low"),
        banned=["hypocretin", "hypocretin-1", "hypocretin 1", "orexin", "orexin-A", "orexin A", "HCRT",
                "preprohypocretin", "prepro-orexin"],
        judgment=["NOTE: Hypocretin/orexin was discovered in 1998 and linked to narcolepsy in animals in 1999, "
                  "before the cutoff (the readiness paper); banning it strips that evidence."]),
    "plasma copeptin": dict(
        t1=("HORMONE_SECRETION_OR_ACTION_DEFECT", ("go", "vasopressin secretion")),
        t2=dict(type="PROTEIN_LEVEL", specimens=["plasma", "serum"], anchor=("hgnc", "AVP"), members=[("hgnc", "AVP")],
                note="Any product of the vasopressin precursor (AVP, copeptin, neurophysin II) in blood."),
        t4=dict(label="copeptin (C-terminal pro-vasopressin) in plasma", terms=[("hgnc", "AVP")],
                qualifier="C-terminal glycopeptide of pre-pro-vasopressin"),
        banned=["copeptin", "CT-proAVP", "CTproAVP", "C-terminal pro-vasopressin", "C-terminal provasopressin",
                "C-terminal portion of provasopressin"],
        judgment=["IMPROVEMENT case: plasma AVP, the pre-existing reference test, meets T2 because it is "
                  "the same precursor gene, so T2 is easy to reach; T4 requires copeptin.",
                  "NOTE: Copeptin is named in the pre-cutoff readiness paper."]),
    "AQP4-IgG": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "water transport")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "astrocyte end-foot"),
                members=[("hgnc", "AQP4")],
                note="Antibody to aquaporin-4, or an astrocyte end-foot / blood-brain-barrier antigen "
                     "named as such. Tissue-pattern NMO-IgG counts as AQP4-IgG."),
        t4=dict(label="NMO-IgG / aquaporin-4 IgG", terms=[("hgnc", "AQP4")], qualifier=""),
        banned=["NMO-IgG", "NMO IgG", "AQP4-IgG", "AQP4 IgG", "anti-AQP4", "aquaporin-4 antibody", "aquaporin-4 antibodies",
                "anti-aquaporin-4", "aquaporin-4", "aquaporin 4", "AQP4", "AQP-4", "MIWC",
                "mercurial-insensitive water channel"],
        judgment=["ONLY C037,C040: For the 2003 cutoffs the antigen was unknown at discovery (a tissue-staining pattern); "
                  "T2 accepts an end-foot antigen named descriptively.",
                  "ONLY C056: NOTE: For transverse myelitis (2005 cutoff) aquaporin-4 is named in the pre-cutoff readiness "
                  "paper.",
                  "ONLY C037: The NMOSD entry is named after its antibody, so the disease name is itself banned."]),
    "TPP1 enzyme activity": dict(
        t1=("ENZYME_DEFICIENCY", ("go", "tripeptidyl-peptidase activity")),
        t2=dict(type="ENZYME_ACTIVITY", specimens=["leukocytes", "dried_blood_spot", "whole_blood", "plasma"],
                anchor=("go", "tripeptidyl-peptidase activity"), members=[("hgnc", "TPP1")],
                note="Tripeptidyl peptidase I activity in a blood-derived specimen."),
        t4=dict(label="tripeptidyl peptidase I activity", terms=[("hgnc", "TPP1")], qualifier="deficient"),
        banned=["tripeptidyl peptidase I", "tripeptidyl peptidase 1", "tripeptidyl-peptidase I", "TPP-I", "TPP1",
                "TPPI", "TPP-1", "pepstatin-insensitive carboxyl proteinase", "pepstatin-insensitive protease",
                "lysosomal pepstatin-insensitive carboxypeptidase", "LPIC"],
        judgment=["The discovery paper measured cultured fibroblasts, which are not accessible; T2's "
                  "specimens come from the case row (blood).",
                  "The gene name CLN2 is also the disease name, so it is not banned."]),
    "flow cytometry for GPI-anchored proteins": dict(
        t1=("GPI_ANCHOR_DEFICIENCY", ("go", "GPI anchor biosynthetic process")),
        t2=dict(type="CELL_SURFACE_MARKER", specimens=["granulocytes", "monocytes", "erythrocytes", "platelets", "whole_blood"],
                anchor=("go", "GPI anchor biosynthetic process"), members=[("hgnc", "CD55"), ("hgnc", "CD59")],
                note="Loss of a GPI-anchored protein on blood cells. The Ham and sucrose-lysis tests are the "
                     "pre-existing tests and reach T1 only."),
        t4=dict(label="decay-accelerating factor (CD55) deficiency on granulocytes and monocytes by flow cytometry",
                terms=[("hgnc", "CD55")], qualifier="leukocytes and platelets, flow cytometry"),
        banned=["decay-accelerating factor", "decay accelerating factor", "DAF", "CD55", "CD59",
                "GPI-anchored", "glycosylphosphatidylinositol-anchored", "FLAER"],
        judgment=["IMPROVEMENT case: erythrocyte DAF deficiency was published before the cutoff (the "
                  "readiness paper) and meets T2, so T2 is reachable from pre-cutoff literature; T4 "
                  "requires leukocytes or platelets.",
                  "NOTE: 'DAF' and 'decay-accelerating factor' are pre-cutoff terms."]),
    "JAK2 V617F": dict(
        t1=("SOMATIC_KINASE_ACTIVATION", ("go", "cell surface receptor signaling pathway via JAK-STAT")),
        t2=dict(type="SOMATIC_VARIANT", specimens=["granulocytes", "whole_blood"], anchor=("hgnc", "JAK2"),
                members=[("hgnc", "JAK2")], note="An acquired JAK2 variant in blood cells."),
        t4=dict(label="JAK2 p.Val617Phe (V617F)", terms=[("hgnc", "JAK2")], qualifier="somatic, granulocyte DNA"),
        banned=["V617F", "Val617Phe", "JAK2V617F", "JAK2 V617F", "JAK2 mutation", "1849G>T", "JAK2 617"],
        judgment=["JAK2 itself is a pre-cutoff term (the readiness paper), so only variant-specific terms "
                  "are banned."]),
    "serum 7-alpha-hydroxy-4-cholesten-3-one": dict(
        t1=("BILE_ACID_SYNTHESIS_UPREGULATION", ("go", "bile acid biosynthetic process")),
        t2=dict(type="METABOLITE", specimens=["serum", "plasma"], anchor=("chebi", "bile acid"),
                members=[("chebi", "7alpha-hydroxycholest-4-en-3-one")],
                note="A blood marker of bile acid synthesis rate."),
        t4=dict(label="serum 7alpha-hydroxy-4-cholesten-3-one (C4)", terms=[("chebi", "7alpha-hydroxycholest-4-en-3-one")],
                qualifier="increased"),
        banned=["7 alpha-hydroxy-4-cholesten-3-one", "7alpha-hydroxy-4-cholesten-3-one", "7α-hydroxy-4-cholesten-3-one",
                "7alpha-hydroxycholest-4-en-3-one", "7-alpha-hydroxy-4-cholesten-3-one", "7-HCO", "7alpha-HCO"],
        judgment=["'C4' is deliberately not banned, because it also names complement C4.",
                  "NOTE: C4 as a marker of bile acid synthesis is pre-cutoff (the readiness paper)."]),
    "alpha-aminoadipic semialdehyde": dict(
        t1=("METABOLIC_PATHWAY_BLOCK", ("go", "L-lysine catabolic process")),
        t2=dict(type="METABOLITE", specimens=["urine", "plasma", "csf"], anchor=("go", "L-lysine catabolic process"),
                members=[("chebi", "L-allysine"), ("chebi", "1-piperideine-6-carboxylic acid"), ("chebi", "pipecolic acid")],
                note="A lysine-pathway metabolite upstream of antiquitin."),
        t4=dict(label="urinary alpha-aminoadipic semialdehyde (alpha-AASA)", terms=[("chebi", "L-allysine")],
                qualifier="increased"),
        banned=["alpha-aminoadipic semialdehyde", "α-aminoadipic semialdehyde", "alpha-AASA", "α-AASA", "AASA",
                "piperideine-6-carboxylate", "P6C", "antiquitin", "ALDH7A1"],
        judgment=["T2 includes pipecolic acid, which was raised in pyridoxine-dependent epilepsy before "
                  "the cutoff, so T2 is reachable from pre-cutoff literature; T4 requires alpha-AASA."]),
    "erythrocyte plasmalogens": dict(
        t1=("METABOLIC_PATHWAY_BLOCK", ("go", "ether lipid biosynthetic process")),
        t2=dict(type="METABOLITE", specimens=["erythrocytes", "plasma"], anchor=("chebi", "ether lipid"),
                members=[("chebi", "1-(alk-1-enyl)-2-acyl-sn-glycero-3-phosphoethanolamine"), ("chebi", "phytanic acid")],
                note="A plasmalogen level, or phytanic acid, in blood."),
        t4=dict(label="low erythrocyte plasmalogens",
                terms=[("chebi", "1-(alk-1-enyl)-2-acyl-sn-glycero-3-phosphoethanolamine")], qualifier="decreased"),
        banned=["plasmalogen", "plasmalogens", "erythrocyte plasmalogen", "plasmenylethanolamine", "ether lipid",
                "ether phospholipid"],
        judgment=["T2 includes plasma phytanic acid, which the discovery paper reports alongside "
                  "plasmalogens.",
                  "NOTE: The plasmalogen synthesis defect in RCDP is pre-cutoff (the readiness paper)."]),
    "TREC newborn screening": dict(
        t1=("THYMIC_OUTPUT_FAILURE", ("go", "T cell differentiation in thymus")),
        t2=dict(type="CELLULAR_DNA_MEASURE", specimens=["dried_blood_spot", "whole_blood"],
                anchor=("go", "T cell differentiation in thymus"), members=[("go", "T cell differentiation in thymus")],
                note="A DNA marker of recent thymic output in blood. A lymphocyte count is a cell count, not "
                     "this analyte type, and reaches T1 only."),
        t4=dict(label="T-cell receptor excision circles by real-time PCR in dried blood spots",
                terms=[("go", "T cell differentiation in thymus")], qualifier="qPCR, newborn dried blood spot"),
        banned=["TREC", "TRECs", "T-cell receptor excision circle", "T-cell receptor excision circles",
                "T cell receptor excision circles", "sjTREC", "signal-joint TREC"],
        judgment=["NOTE: TRECs as a marker of thymic output are pre-cutoff (the readiness paper), so banning "
                  "them strips that evidence; the lymphocyte count is kept at T1."]),
    "serum 7-dehydrocholesterol": dict(
        t1=("METABOLIC_PATHWAY_BLOCK", ("go", "cholesterol biosynthetic process")),
        t2=dict(type="METABOLITE", specimens=["serum", "plasma", "erythrocytes"], anchor=("chebi", "sterol"),
                members=[("chebi", "cholesta-5,7-dien-3beta-ol"), ("chebi", "8-Dehydrocholesterol"), ("chebi", "cholesterol")],
                note="A sterol level in blood, including low cholesterol."),
        t4=dict(label="raised 7-dehydrocholesterol in serum or plasma", terms=[("chebi", "cholesta-5,7-dien-3beta-ol")],
                qualifier="increased"),
        banned=["7-dehydrocholesterol", "7-DHC", "7DHC", "cholesta-5,7-dien-3beta-ol", "cholesta-5,7-dien-3 beta-ol",
                "8-dehydrocholesterol", "DHCR7", "7-dehydrocholesterol reductase", "dehydrocholesterol"],
        judgment=["T2 includes low plasma cholesterol, so it is reachable without naming 7-DHC; T4 requires "
                  "7-DHC.",
                  "NOTE: The pre-cutoff readiness letter (Irons 1993) has no abstract, so the co-occurrence "
                  "counts cannot see it."]),
    "anti-HMGCR antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "cholesterol biosynthetic process")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum"], anchor=("hgnc", "HMGCR"), members=[("hgnc", "HMGCR")],
                note="Antibody to HMG-CoA reductase. Creatine kinase reaches T1 at most."),
        t4=dict(label="autoantibodies to HMG-CoA reductase (the 200/100-kd antigen)", terms=[("hgnc", "HMGCR")],
                qualifier=""),
        banned=["anti-HMGCR", "HMGCR antibody", "HMGCR antibodies", "anti-200/100", "200-kd and 100-kd",
                "anti-HMG-CoA reductase"],
        judgment=["HMG-CoA reductase is the statin target and appears in nearly every pre-cutoff statin "
                  "paper, so only antibody phrases are banned, not the enzyme's names.",
                  "NOTE: The discovery paper identified the antigen only by size (200/100 kd); T4 names the later "
                  "identity."]),
    "anti-GAD65 antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "gamma-aminobutyric acid biosynthetic process")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "gamma-aminobutyric acid biosynthetic process"),
                members=[("hgnc", "GAD2"), ("hgnc", "GAD1")], note="Antibody to either GAD isoform."),
        t4=dict(label="autoantibodies to glutamic acid decarboxylase", terms=[("hgnc", "GAD2"), ("hgnc", "GAD1")],
                qualifier="isoform not specified at discovery"),
        banned=["glutamic acid decarboxylase", "glutamate decarboxylase", "GAD65", "GAD67", "anti-GAD",
                "GAD antibodies", "GAD autoantibodies"],
        judgment=["'GAD' alone is not banned: it also abbreviates generalized anxiety disorder.",
                  "NOTE: T4 accepts either isoform, because the discovery paper predates the GAD65 identification."]),
    "anti-amphiphysin antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "synaptic vesicle endocytosis")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "synaptic vesicle endocytosis"),
                members=[("hgnc", "AMPH")], note="Antibody to amphiphysin."),
        t4=dict(label="autoantibodies to amphiphysin (the 128-kd synaptic protein)", terms=[("hgnc", "AMPH")],
                qualifier=""),
        banned=["amphiphysin", "AMPH", "128-kd synaptic protein", "128-kd brain protein", "anti-amphiphysin"],
        judgment=["NOTE: The discovery paper identified the antigen only by size (128 kd); T4 names the identity "
                  "published the same year."]),
    "anti-glycine receptor antibodies": dict(
        t1=("AUTOIMMUNE_ANTIBODY", ("go", "synaptic transmission, glycinergic")),
        t2=dict(type="AUTOANTIBODY", specimens=["serum", "csf"], anchor=("go", "synaptic transmission, glycinergic"),
                members=[("hgnc", "GLRA1"), ("hgnc", "GLRA2"), ("hgnc", "GLRA3"), ("hgnc", "GLRB")],
                note="Antibody to any glycine receptor subunit. Gephyrin is a scaffold, not a receptor "
                     "subunit, and reaches T1 only."),
        t4=dict(label="IgG autoantibodies to the glycine receptor alpha1 subunit", terms=[("hgnc", "GLRA1")], qualifier=""),
        banned=["glycine receptor", "glycine receptors", "GlyR", "GLRA1", "glycine receptor alpha1", "anti-GlyR",
                "GlyRα1"],
        judgment=["Gephyrin antibodies (the pre-cutoff readiness paper) are kept out of T2, so T2 is not "
                  "reachable merely by proposing them."]),
}

# ---------------------------------------------------------------- revision 2 (2026-11-16)
# Applied on top of G. Each entry replaces the named keys of that test group.
# CHANGES lists what changed, for rubrics_review.md.
#   t1_clinical  analytes in clinical diagnostic use for the disease at the cutoff:
#                a candidate naming one reaches T1 only (the T2 rule, README *Scoring*)
#   t2_also      further accepted T2 definitions (analyte_type, specimens, members)
#   a member may be (db, label, form): the gene, with the gene product named in form
REVISION = {
    "ADAMTS13 activity": dict(
        t2_also=[dict(type="AUTOANTIBODY", specimens=["serum", "plasma"], anchor=("hgnc", "ADAMTS13"),
                      members=[("hgnc", "ADAMTS13")],
                      note="IgG autoantibody to, or inhibitor of, ADAMTS13.")],
        judgment=["T2 also accepts an anti-ADAMTS13 IgG or inhibitor (AUTOANTIBODY, serum or plasma): the "
                  "discovery paper found an inhibitor in the nonfamilial cases."]),
    "plasma p-tau217": dict(judgment=[
        "IMPROVEMENT case: plasma p-tau181 or total tau meet T2 (same target, blood); CSF tau does not.",
        "NOTE: Only 217-specific names are leakage terms; tau and p-tau are pre-cutoff vocabulary and would "
        "raise false alarms."]),
    "anti-GM-CSF autoantibodies": dict(judgment=[
        "The discovery paper found the antibody first in bronchoalveolar lavage fluid, which is not an "
        "accessible specimen; T2 allows only serum and plasma, where it was also found.",
        "NOTE: GM-CSF itself is not a leakage term: GM-CSF signalling in pulmonary alveolar proteinosis is "
        "pre-cutoff literature (the readiness paper)."]),
    "urinary N-acetylaspartic acid": dict(
        banned=["N-acetylaspartic acid", "N-acetylaspartate", "N-acetyl-L-aspartic acid", "N-acetylaspartic aciduria",
                "aspartoacylase"],
        judgment=["'NAA' is left out of the leakage terms: it is a generic abbreviation and would raise false "
                  "alarms.",
                  "NOTE: The discovery paper's aspartoacylase assay used cultured fibroblasts, so it is not an "
                  "accessible-specimen T2 hit."]),
    "anti-tissue transglutaminase IgA": dict(judgment=[
        "Endomysial antibody (a pre-cutoff test) is excluded from T2 because it names a tissue, not tTG."]),
    "CSF glucose for GLUT1 deficiency": dict(judgment=[
        "Every leakage term for this test (CSF glucose, hypoglycorrhachia, GLUT1) is pre-cutoff vocabulary, "
        "so most are in the packet and the T4 leakage alarm has little to check.",
        "The case is the GLUT1-deficiency subset; the subset text is kept out of arm prompts."]),
    "leukocyte telomere length by flow-FISH": dict(judgment=[
        "Blood telomere length was measured before the cutoff (by Southern blot); T2 accepts any method, and "
        "T4 requires flow-FISH.",
        "NOTE: 'telomere length' is in the packet, so only the flow-FISH terms can raise an alarm."]),
    "anti-PF4/heparin IgG": dict(judgment=[
        "IMPROVEMENT case: the pre-cutoff functional tests detect the same antibody, but T2 requires PF4 as "
        "the target, so they reach T1/T3 only."]),
    "acid alpha-glucosidase activity": dict(
        t2=dict(type="ENZYME_ACTIVITY", specimens=["dried_blood_spot"],
                anchor=("go", "alpha-1,4-glucosidase activity"), members=[("hgnc", "GAA")],
                note="Acid alpha-glucosidase activity in dried blood spots."),
        t1_clinical=["leukocyte (or lymphocyte) acid alpha-glucosidase activity"],
        judgment=["NOTE: The enzyme's names (acid maltase, GAA) define Pompe disease before the cutoff and are "
                  "not leakage terms."]),
    "anti-AMPA receptor antibodies": dict(judgment=[
        "NOTE: The AMPA receptor and its subunits are standard pre-cutoff neuroscience terms."]),
    "serum VEGF-D": dict(
        t2=dict(type="PROTEIN_LEVEL", specimens=["serum", "plasma"], anchor=("go", "lymphangiogenesis"),
                members=[("hgnc", "VEGFD")], note="VEGF-D in blood."),
        judgment=[]),
    "MOG-IgG": dict(judgment=[
        "Anti-MOG ELISA and Western blot studies, which were nonspecific, predate the cutoff; T2 accepts them "
        "and T4 requires the native-MOG cell-based assay.",
        "ONLY C028: MOGAD is named after its test; arm_display_name uses a pre-cutoff name for paediatric "
        "demyelination."]),
    "plasma DOPA:DHPG ratio": dict(judgment=[
        "IMPROVEMENT case: copper and ceruloplasmin are left at T1. DOPA, DOPAC and noradrenaline are too "
        "generic to be leakage terms."]),
    "CSF hypocretin-1": dict(judgment=[
        "NOTE: Hypocretin/orexin was discovered in 1998 and linked to narcolepsy in animals in 1999, before "
        "the cutoff (the readiness paper), so these terms are in the packet."]),
    "plasma copeptin": dict(
        t2=dict(type="PROTEIN_LEVEL", specimens=["plasma", "serum"], anchor=("hgnc", "AVP"),
                members=[("hgnc", "AVP", "copeptin (C-terminal glycopeptide of pre-pro-vasopressin)")],
                note="Copeptin in blood. Plasma AVP is T1 only."),
        t1_clinical=["plasma arginine vasopressin (AVP), measured in the water deprivation test"],
        judgment=["NOTE: Copeptin is named in the pre-cutoff readiness paper."]),
    "AQP4-IgG": dict(judgment=[
        "For the 2003 cutoffs (all three cases since C056 was re-dated) the antigen was unknown at "
        "discovery (a tissue-staining pattern); T2 accepts an end-foot antigen named descriptively.",
        "ONLY C037: The NMOSD entry is named after its antibody; arm_display_name is 'neuromyelitis optica'.",
        "NOTE: 'NMO' alone is not a leakage alarm: terms match whole and exact, so only 'NMO-IgG' and the "
        "like match."]),
    "TPP1 enzyme activity": dict(judgment=[
        "The discovery paper measured cultured fibroblasts, which are not accessible; T2's specimens come from "
        "the case row (blood).",
        "The gene name CLN2 is also the disease name, so it is not a leakage term."]),
    "flow cytometry for GPI-anchored proteins": dict(judgment=[
        "IMPROVEMENT case: erythrocyte DAF deficiency was published before the cutoff (the readiness paper) "
        "and meets T2, so T2 is reachable from pre-cutoff literature; T4 requires leukocytes or platelets."]),
    "JAK2 V617F": dict(judgment=[
        "JAK2 itself is a pre-cutoff term (the readiness paper), so only variant-specific names are leakage "
        "terms."]),
    "serum 7-alpha-hydroxy-4-cholesten-3-one": dict(judgment=[
        "'C4' is not a leakage term: it also names complement C4."]),
    "alpha-aminoadipic semialdehyde": dict(
        t2=dict(type="METABOLITE", specimens=["urine", "plasma", "csf"], anchor=("go", "L-lysine catabolic process"),
                members=[("chebi", "L-allysine"), ("chebi", "1-piperideine-6-carboxylic acid")],
                note="Alpha-AASA or P6C. Pipecolic acid is T1 only."),
        t1_clinical=["plasma or CSF pipecolic acid"],
        judgment=[]),
    "TREC newborn screening": dict(judgment=[
        "NOTE: TRECs as a marker of thymic output are pre-cutoff (the readiness paper), so these terms are in "
        "the packet."]),
    "erythrocyte plasmalogens": dict(  # revision 3 (default, pending Chris)
        t2=dict(type="METABOLITE", specimens=["erythrocytes", "plasma"], anchor=("chebi", "ether lipid"),
                members=[("chebi", "1-(alk-1-enyl)-2-acyl-sn-glycero-3-phosphoethanolamine")],
                note="A plasmalogen level in blood. Phytanic acid is T1 only."),
        t1_clinical=["plasma phytanic acid (a peroxisomal-disorder test in use before the cutoff)"],
        judgment=["NOTE: The plasmalogen synthesis defect in RCDP is pre-cutoff (the readiness paper)."]),
    "serum 7-dehydrocholesterol": dict(
        t2=dict(type="METABOLITE", specimens=["serum", "plasma", "erythrocytes"], anchor=("chebi", "sterol"),
                members=[("chebi", "cholesta-5,7-dien-3beta-ol"), ("chebi", "8-Dehydrocholesterol")],
                note="7-DHC or 8-DHC in blood."),
        judgment=["NOTE: The pre-cutoff readiness letter (Irons 1993) has no abstract, so the co-occurrence "
                  "counts cannot see it."]),
    "anti-HMGCR antibodies": dict(judgment=[
        "HMG-CoA reductase is the statin target and appears in nearly every pre-cutoff statin paper, so only "
        "antibody phrases are leakage terms.",
        "NOTE: The discovery paper identified the antigen only by size (200/100 kd); T4 names the later "
        "identity."]),
    "anti-GAD65 antibodies": dict(judgment=[
        "'GAD' alone is not a leakage term: it also abbreviates generalized anxiety disorder.",
        "NOTE: T4 accepts either isoform, because the discovery paper predates the GAD65 identification."]),
}
for _grp, _upd in REVISION.items():
    G[_grp].update(_upd)

CHANGES = [
    "Banned terms are renamed leakage_terms and are never stripped from packets, which are pre-cutoff by "
    "construction. Each carries in_packet (yes when its pre-cutoff co-occurrence count with the disease is "
    "above 0). Planned audit: a leakage term with in_packet no that appears in a curated entry or an arm's "
    "output is a leakage alarm.",
    "Every case and negative has an arm_display_name: a pre-cutoff disease name with no test, analyte or "
    "antibody in it. Subset text never appears in arm prompts.",
    "T2 rule: an analyte in clinical diagnostic use for the disease at the cutoff reaches T1 only "
    "(t1_clinical).",
    "C022: leukocyte acid alpha-glucosidase moved to T1; T2 is the dried-blood-spot assay only.",
    "C036, C057: plasma AVP moved to T1; T2 is copeptin.",
    "C045: pipecolic acid moved to T1; T2 is alpha-AASA or P6C.",
    "C027: VEGF-C removed from T2.",
    "C051: cholesterol (CHEBI:16113) removed from T2.",
    "C001: anti-ADAMTS13 IgG or inhibitor (AUTOANTIBODY, serum or plasma) added to T2.",
    "C008: 'NAA' dropped from the leakage terms (generic abbreviation).",
    "Revision 3 (defaults, pending Chris; see DEVIATIONS.md): C036 excluded as NOT_NEW_ANALYTE; C047 "
    "phytanic acid moved to T1; C056 re-dated to PMID:15589308 (cutoff 2003-12-31); C022 display name "
    "'adult-onset acid maltase deficiency'; negatives N10, N13, N17 replaced after an accessible-test screen.",
    "PubMed counts for multi-word leakage terms and display names now use the proximity form [tiab:~0]; a "
    "quoted phrase in [tiab] returns 0 for phrases outside PubMed's phrase index, which had set some "
    "in_packet values to no wrongly.",
    "Negatives N12 and N13 replaced by the next seeded draws. Every negative has a cutoff from a seeded "
    "draw of test cases (provisional: no matching criterion is defined yet) and a literature check at it; "
    "drawn negatives below packet_minimum were redrawn (negatives.tsv, negatives_replaced.tsv, "
    "negatives_literature_check.tsv).",
]

# arm_display_name: the only disease name an arm sees. A pre-cutoff name with no test, analyte or
# antibody in it, and never the subset text. Each is checked by PubMed count (any listed phrase in
# title/abstract on or before the cutoff) and against the case's leakage terms.
DISPLAY = {
    "C001": ("acquired thrombotic thrombocytopenic purpura", ["thrombotic thrombocytopenic purpura"]),
    "C002": ("Alzheimer disease", ["Alzheimer disease", "Alzheimer's disease"]),
    "C003": ("Alzheimer disease", ["Alzheimer disease", "Alzheimer's disease"]),
    "C005": ("autoimmune polyendocrinopathy syndrome type 1", ["autoimmune polyendocrinopathy syndrome type 1",
                                                                 "APECED"]),
    # "idiopathic PAP" has no PubMed hit before the 1998 cutoff (it spreads from the 1999 discovery paper)
    "C006": ("pulmonary alveolar proteinosis", ["pulmonary alveolar proteinosis"]),
    "C008": ("Canavan disease", ["Canavan disease", "Canavan's disease"]),
    "C009": ("coeliac disease", ["coeliac disease", "celiac disease"]),
    "C010": ("childhood absence epilepsy", ["childhood absence epilepsy"]),
    "C011": ("chronic inflammatory demyelinating polyneuropathy", ["chronic inflammatory demyelinating polyneuropathy"]),
    "C012": ("chronic inflammatory demyelinating polyneuropathy", ["chronic inflammatory demyelinating polyneuropathy"]),
    "C014": ("dermatomyositis", ["dermatomyositis"]),
    "C015": ("dyskeratosis congenita", ["dyskeratosis congenita"]),
    "C016": ("dyskeratosis congenita", ["dyskeratosis congenita"]),
    "C017": ("membranous glomerulonephritis", ["membranous glomerulonephritis"]),
    "C018": ("heparin-induced thrombocytopenia", ["heparin-induced thrombocytopenia"]),
    "C021": ("inherited aplastic anaemia", ["inherited aplastic anemia", "inherited aplastic anaemia",
                                             "constitutional aplastic anemia"]),
    # revision 3 (default, pending Chris): the pre-cutoff name; "late-onset Pompe disease" had 1 hit
    "C022": ("adult-onset acid maltase deficiency", ["adult-onset acid maltase deficiency",
                                                     "adult acid maltase deficiency", "acid maltase deficiency"]),
    "C023": ("limbic encephalitis", ["limbic encephalitis"]),
    "C024": ("limbic encephalitis", ["limbic encephalitis"]),
    "C025": ("limbic encephalitis", ["limbic encephalitis"]),
    "C026": ("limbic encephalitis", ["limbic encephalitis"]),
    "C027": ("lymphangioleiomyomatosis", ["lymphangioleiomyomatosis"]),
    "C028": ("acquired demyelinating syndrome in children (ADEM or CIS)",
             ["acute disseminated encephalomyelitis", "clinically isolated syndrome"]),
    "C029": ("idiopathic membranous nephropathy", ["idiopathic membranous nephropathy"]),
    "C030": ("Menkes disease", ["Menkes disease", "Menkes' disease"]),
    "C033": ("myasthenia gravis", ["myasthenia gravis"]),
    "C034": ("narcolepsy with cataplexy", ["narcolepsy"]),
    "C035": ("narcolepsy", ["narcolepsy"]),
    "C036": ("central diabetes insipidus", ["central diabetes insipidus"]),
    "C037": ("neuromyelitis optica", ["neuromyelitis optica"]),
    "C038": ("late infantile neuronal ceroid lipofuscinosis", ["late infantile neuronal ceroid lipofuscinosis"]),
    "C039": ("optic neuritis", ["optic neuritis"]),
    "C040": ("optic neuritis", ["optic neuritis"]),
    "C041": ("paroxysmal dyskinesia", ["paroxysmal dyskinesia"]),
    "C042": ("paroxysmal nocturnal haemoglobinuria", ["paroxysmal nocturnal hemoglobinuria"]),
    "C043": ("polycythaemia vera", ["polycythemia vera", "polycythaemia vera"]),
    "C044": ("idiopathic bile acid malabsorption", ["bile acid malabsorption"]),
    "C045": ("pyridoxine-dependent epilepsy", ["pyridoxine-dependent epilepsy", "pyridoxine-dependent seizures"]),
    "C047": ("rhizomelic chondrodysplasia punctata", ["rhizomelic chondrodysplasia punctata"]),
    "C050": ("severe combined immunodeficiency", ["severe combined immunodeficiency"]),
    "C051": ("Smith-Lemli-Opitz syndrome", ["Smith-Lemli-Opitz syndrome"]),
    "C052": ("statin-associated myopathy", ["statin myopathy", "statin-associated myopathy",
                                             "statin-induced myopathy"]),
    "C053": ("stiff-man syndrome", ["stiff-man syndrome"]),
    "C054": ("stiff-man syndrome", ["stiff-man syndrome"]),
    "C055": ("stiff person syndrome", ["stiff person syndrome", "stiff-person syndrome"]),
    "C056": ("transverse myelitis", ["transverse myelitis"]),
    "C057": ("nephrogenic diabetes insipidus", ["nephrogenic diabetes insipidus"]),
}

NEG_DISPLAY = {  # kb_file -> (arm_display_name, check phrases), as DISPLAY
    "kb/disorders/Hypermobile_Ehlers-Danlos_Syndrome.yaml": (
        "Ehlers-Danlos syndrome type III (hypermobile)", ["Ehlers-Danlos syndrome type III", "Ehlers-Danlos syndrome"]),
    "kb/disorders/Kawasaki_Disease.yaml": ("Kawasaki disease", ["Kawasaki disease"]),
    "kb/disorders/Sarcoidosis.yaml": ("sarcoidosis", ["sarcoidosis"]),
    "kb/disorders/Behcets_Disease.yaml": ("Behcet's disease", ["Behcet's disease", "Behcet disease"]),
    "kb/disorders/Complex_Regional_Pain_Syndrome_Type_1.yaml": (
        "complex regional pain syndrome type 1", ["complex regional pain syndrome"]),
    "kb/disorders/Takayasu_Arteritis.yaml": ("Takayasu arteritis", ["Takayasu arteritis"]),
    "kb/disorders/Juvenile_Idiopathic_Arthritis.yaml": ("juvenile idiopathic arthritis", ["juvenile idiopathic arthritis"]),
    "kb/disorders/Soil_Transmitted_Helminthiases.yaml": (
        "soil-transmitted helminthiasis", ["soil-transmitted helminth", "hookworm infection"]),
    "kb/disorders/Congenital_Merosin-deficient_Muscular_Dystrophy_1A.yaml": (
        "congenital merosin-deficient muscular dystrophy", ["merosin-deficient congenital muscular dystrophy",
                                                            "merosin-deficient muscular dystrophy"]),
    "kb/disorders/Aortitis.yaml": ("aortitis", ["aortitis"]),
    "kb/disorders/Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant.yaml": (
        "autosomal dominant limb-girdle muscular dystrophy", ["limb-girdle muscular dystrophy"]),
    "kb/disorders/Hereditary_Angioedema.yaml": ("hereditary angioedema", ["hereditary angioedema",
                                                                          "hereditary angioneurotic edema"]),
    "kb/disorders/Kearns-Sayre_Syndrome.yaml": ("Kearns-Sayre syndrome", ["Kearns-Sayre syndrome"]),
    "kb/disorders/Choroid_Plexus_Neoplasm.yaml": (
        "choroid plexus tumour", ["choroid plexus papilloma", "choroid plexus carcinoma", "choroid plexus tumor"]),
    "kb/disorders/Psoriasis.yaml": ("psoriasis", ["psoriasis"]),
    "kb/disorders/Angiomatoid_Fibrous_Histiocytoma.yaml": (
        "angiomatoid fibrous histiocytoma", ["angiomatoid fibrous histiocytoma"]),
    "kb/disorders/Melanotic_Neuroectodermal_Tumor_of_Infancy.yaml": (
        "melanotic neuroectodermal tumour of infancy", ["melanotic neuroectodermal tumor of infancy"]),
    "kb/disorders/Peeling_Skin_Syndrome.yaml": ("peeling skin syndrome", ["peeling skin syndrome"]),
    # revision 3 replacements for N10, N13, N17
    "kb/disorders/Deficiency_of_the_Interleukin-1_Receptor_Antagonist.yaml": (
        "autoinflammatory disease of infancy with pustulosis and osteomyelitis",
        ["pustulosis", "neonatal-onset autoinflammatory", "sterile multifocal osteomyelitis"]),
    "kb/disorders/Lipoprotein_Glomerulopathy.yaml": ("lipoprotein glomerulopathy", ["lipoprotein glomerulopathy"]),
    "kb/disorders/Congenital_Hydrocephalus.yaml": ("congenital hydrocephalus", ["congenital hydrocephalus"]),
}

# T3 from each discovery paper (title and abstract), keyed by PMID.
T3 = {
    "9828245": "Plasma VWF-cleaving protease activity (diluted plasma, purified normal VWF as substrate, degradation "
               "read by SDS-agarose electrophoresis and immunoblot) in 53 patients with TTP or HUS, familial and "
               "nonfamilial, with an inhibitor (mixing) study against normal plasma.",
    "32722745": "Plasma p-tau217 immunoassay in three cohorts (neuropathology-confirmed, clinical BioFINDER-2 including "
                "other neurodegenerative diseases, and a PSEN1 E280A kindred); discriminative accuracy for AD vs "
                "other diagnoses and association with tau pathology.",
    "7574461": "CSF amyloid-beta 42 measured in AD patients and controls, alongside total amyloid-beta, tau and APOE "
               "genotype; Abeta42 was lower in AD while total Abeta was not.",
    "16784312": "Serum binding and neutralisation assays for autoantibodies to type I interferons and other cytokines "
                "in Finnish and Norwegian APS1 patients with biallelic AIRE mutations, against controls.",
    "10499925": "Search for neutralising IgG against GM-CSF in bronchoalveolar lavage fluid and serum of idiopathic "
                "PAP patients versus secondary PAP, other lung disease and normal controls; binding and "
                "neutralisation of GM-CSF bioactivity in vitro.",
    "3354621": "Urine and plasma N-acetylaspartic acid in three patients from two Canavan families; aspartoacylase "
               "assayed in cultured skin fibroblasts.",
    "9836104": "Prospective IgA anti-tissue-transglutaminase ELISA in 20 untreated coeliacs and 21 consecutive "
               "patients with other small-bowel disease.",
    "18479384": "Case report: a child with absences and myoclonias first diagnosed with idiopathic generalized "
                "epilepsy, later documented to have a mild GLUT1 deficiency syndrome (diagnostic work-up not "
                "detailed in the abstract).",
    "18451999": "Family study of paroxysmal exertion-induced dyskinesia with reduced CSF glucose; candidate-gene "
                "sequencing of GLUT1, functional transport studies in oocytes and erythrocytes, and screening of "
                "four further families.",
    "23100406": "ELISA and cell-based assay for antibodies to human NF155 and NF186 in 434 donors, including GBS "
                "variants and CIDP; isotyping, tissue staining, epitope mapping and passive transfer in rats.",
    "23280477": "Screening CIDP sera on live hippocampal neurons, antigen identification by immunoprecipitation and "
                "mass spectrometry, confirmed by cell-based assays, teased-nerve immunohistochemistry and "
                "immunoabsorption.",
    "15880816": "Immunoprecipitation of 298 sera from connective tissue disease and IPF patients, finding a 140-kd "
                "antigen (CADM-140); immunoblot, immunofluorescence and clinical association with amyopathic DM "
                "and rapidly progressive ILD.",
    "17468339": "Multicolour flow-FISH of median telomere length in blood leukocytes, granulocytes and lymphocyte "
                "subsets in DC patients, relatives and other marrow-failure patients against 400 healthy controls; "
                "'very short' defined as below the 1st percentile for age.",
    "19571279": "Western blot of normal human glomerular extract with sera from idiopathic and secondary MN, other "
                "renal and autoimmune diseases and controls; mass spectrometry identified PLA2R, confirmed with "
                "recombinant protein and a monospecific antibody.",
    "1514184": "Letter (no PubMed abstract): identification of PF4 complexed to heparin as the target of HIT "
               "antibodies.",
    "11468225": "Immune-capture acid alpha-glucosidase activity assay in dried blood spots from newborn and adult "
                "controls and Pompe-affected individuals.",
    "20580615": "Sera and CSF of 57 patients with limbic encephalitis attributed to VGKC antibodies and 148 controls; "
                "immunohistochemistry, immunoprecipitation and mass spectrometry identified LGI1, tested on HEK293 "
                "cells expressing LGI1 with ADAM22/23 and confirmed in Lgi1-null mice.",
    "20663977": "96 VGKC-antibody-positive patients: binding to HEK293 cells expressing potassium-channel subunits and "
                "complexed proteins, identifying LGI1, CASPR2 and contactin-2 as the targets.",
    "19962348": "15 patients with suspected immune-mediated limbic encephalitis; confocal microscopy, "
                "immunoprecipitation and mass spectrometry identified GABA(B1)/(B2); HEK293 cell-based assay against "
                "91 encephalitis controls and 13 anti-GAD65 controls.",
    "19338055": "10 limbic encephalitis patients; immunoprecipitation and mass spectrometry identified GluR1/GluR2; "
                "HEK293 cell-based assay and ELISA; effect of patient antibodies on live hippocampal neurons.",
    "17034294": "ELISA of serum VEGF-A, VEGF-C and VEGF-D in 44 LAM patients and 24 matched healthy volunteers; only "
                "VEGF-D was raised.",
    "20033986": "Cell-based bioassay for antibodies to native MOG in 47 children at a first episode of CNS "
                "demyelination (ADEM or CIS) against neurological, healthy-child and adult controls.",
    "8434878": "Plasma and CSF catechols in 10 Menkes patients aged 9 days to 27 months; DOPA:DHPG and DOPAC:DHPG "
               "ratios compared with controls.",
    "11231638": "Sera of AChR-antibody-seronegative and seropositive generalized MG patients tested against the "
                "extracellular domains of MuSK expressed in transfected COS7 cells.",
    "10615891": "CSF hypocretin-1 measured in nine people with narcolepsy and controls; undetectable in seven of nine.",
    "25768671": "Prospective multicentre study of adults with polyuria-polydipsia undergoing a combined water "
                "deprivation / 3% saline infusion test, with copeptin and AVP measured throughout against the "
                "final diagnosis.",
    "15589308": "Indirect immunofluorescence on composite mouse tissue for an NMO-IgG staining pattern; masked sera "
                "from 102 North American patients with NMO or high-risk syndromes and 12 Japanese optic-spinal MS "
                "patients against MS and other controls; sensitivity and specificity.",
    "9989590": "TPP-I activity in cultured fibroblasts from LINCL patients against controls, with other lysosomal "
               "enzymes and peptide degradation, after sequence identity of TPP-I with the CLN2 protease.",
    "22204662": "Native-MOG cell-based assay for complement-activating MOG antibodies in NMO, high-risk NMO "
                "(recurrent optic neuritis or LETM), ADEM, CIS, MS and controls.",
    "3845321": "Cytofluorographic analysis with anti-DAF antibody of granulocytes, monocytes and platelets from four "
               "PNH patients and controls, with surface radiolabelling and immunoprecipitation.",
    "15781101": "Bidirectional sequencing of JAK2 coding exons from peripheral-blood granulocytes and T cells of "
                "patients with PV, ET and myelofibrosis; allele-specific PCR, cytogenetics, SNP arrays and colony "
                "assays.",
    "8504974": "Fasting serum 7alpha-hydroxy-4-cholesten-3-one in 28 patients with chronic diarrhoea, correlated "
               "with SeHCAT retention measured the same day.",
    "16491085": "ALDH7A1 sequencing in children with pyridoxine-dependent seizures, showing loss of P6C/alpha-AASA "
                "dehydrogenase activity; urinary alpha-AASA proposed to confirm the diagnosis.",
    "1955304": "Case report: a boy diagnosed with RCDP from high plasma phytanic acid and low erythrocyte "
               "plasmalogens, followed for 16 years.",
    "15696101": "Real-time PCR for TRECs in DNA from dried blood spots (beta-actin control) in adult and cord-blood "
                "controls, spotted SCID patient blood, routine Maryland newborn screening spots and archived spots "
                "of two infants later diagnosed with SCID.",
    "8259166": "Capillary-column GC-MS of sterols in plasma, erythrocytes, lens, cultured fibroblasts and faeces of "
               "five children with SLOS against controls.",
    "20496415": "Immunoprecipitation from 35S-labelled HeLa lysates of sera from 225 myopathy patients with muscle "
                "biopsy, finding a 200/100-kd specificity in necrotizing myopathy; staining for MAC, MHC-I and CD31.",
    "3281011": "Serum and CSF of one stiff-man patient with epilepsy and type 1 diabetes: oligoclonal IgG, "
               "immunocytochemical staining of brain matching anti-GAD, and SDS-PAGE identifying a band comigrating "
               "with GAD.",
    "8381208": "Serum and CSF of three women with stiff-man syndrome and breast cancer screened by "
               "immunocytochemistry, Western blot and immunoprecipitation, finding antibodies to a 128-kd synaptic "
               "protein; GAD antibodies were negative.",
    "18852446": "Clinical note (no PubMed abstract): a patient with severe PERM and a novel anti-glycine receptor "
                "antibody, judged from the source's opening text supplied by the reviewer.",
    "16453327": "Prospective study of NMO-IgG serostatus at a first attack of longitudinally extensive transverse "
                "myelitis (29 patients) and relapse or optic neuritis over one year of follow-up.",
    "21367924": "Water deprivation test with plasma AVP and copeptin in 20 healthy subjects and 50 patients with "
                "polydipsia-polyuria, against a reference diagnosis from clinical information and treatment response.",
}

NEG_FALSE_POSITIVE = (
    "Any candidate proposed as a confirmatory accessible-specimen test for this disease (blood, serum, plasma, "
    "dried blood spot, urine or CSF; germline sequencing excluded) is a false positive, at whatever tier it would "
    "otherwise reach. The measurable nodes listed are what an arm is most likely to propose; each is nonspecific.")


# ---------------------------------------------------------------- lookups
class Onto:
    def __init__(self) -> None:
        self.db = {n: sqlite3.connect(f"file:{OAK / (n + '.db')}?mode=ro", uri=True) for n in ("go", "chebi", "hgnc")}

    def member(self, m: tuple) -> dict:
        r = self.resolve(m[0], m[1])
        return {**r, "form": m[2]} if len(m) > 2 else r

    def resolve(self, db: str, label: str) -> dict:
        rows = self.db[db].execute("select subject from statements where predicate='rdfs:label' and value=?",
                                   (label,)).fetchall()
        ids = sorted({r[0] for r in rows if not r[0].startswith("_:")})
        if len(ids) != 1:
            sys.exit(f"{db}: label {label!r} resolves to {ids}")
        return {"id": ids[0], "label": label}

    def gene_names(self, curie: str) -> list[str]:
        out = []
        for pred in ("IAO:0000115", "oio:hasExactSynonym"):
            out += [r[0] for r in self.db["hgnc"].execute(
                "select value from statements where subject=? and predicate=?", (curie, pred))]
        return out


def pubmed_count(term: str, maxdate: str) -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(f"{term}|{maxdate}".encode()).hexdigest()
    path = CACHE / f"{key}.json"
    if path.exists():
        return json.loads(path.read_text())["count"]
    api = os.environ.get("NCBI_API_KEY", "").strip()
    if not api:
        sys.exit("NCBI_API_KEY is not set")
    body = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": 0, "retmode": "json", "datetype": "pdat",
                                   "mindate": "1800", "maxdate": maxdate, "api_key": api,
                                   "tool": "dismech-retrodiction"}).encode()
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(
                    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", data=body), timeout=60) as r:
                n = int(json.load(r)["esearchresult"]["count"])
            break
        except Exception as e:  # type only: the request body carries the key
            if attempt == 3:
                sys.exit(f"esearch failed ({type(e).__name__})")
            time.sleep(2 ** attempt)
    time.sleep(0.12)
    path.write_text(json.dumps({"count": n}))
    return n


def read_tsv(name: str) -> list[dict]:
    with open(HERE / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def quote(term: str) -> str:
    return term.replace('"', "")


def tiab(term: str) -> str:
    """A title/abstract clause. A quoted multi-word phrase in [tiab] matches only phrases in PubMed's
    phrase index, and E-utilities returns 0 for the rest, so multi-word terms use the proximity form
    [tiab:~0] (words adjacent, in order), as find_decoys.py does."""
    t = quote(term)
    return f'"{t}"[tiab:~0]' if " " in t.strip() else f'"{t}"[tiab]'



# ---------------------------------------------------------------- build
def main() -> None:
    onto = Onto()
    rows = read_tsv("dating.tsv")
    lit = {r["case_id"]: r for r in read_tsv("literature_check.tsv")}
    dev = set((HERE / "dev_set.txt").read_text().split())
    test = set((HERE / "test_set.txt").read_text().split())
    verified = [r for r in rows if lit[r["case_id"]]["lit_ruling"] == "PASS"]
    if {r["case_id"] for r in verified} != dev | test:
        sys.exit("verified cases differ from dev_set.txt + test_set.txt")
    missing = sorted({r["test_group"] for r in verified} - set(G))
    if missing:
        sys.exit(f"no rubric for test groups: {missing}")
    OUT.mkdir(exist_ok=True)

    review = []
    for r in sorted(verified, key=lambda r: r["case_id"]):
        g = G[r["test_group"]]
        cid, pmid = r["case_id"], r["discovery_pmid"].replace("PMID:", "")
        mc, proc = g["t1"]
        if mc not in MECHANISM_CLASSES:
            sys.exit(f"{cid}: unknown mechanism class {mc}")
        t2 = g["t2"]
        for t in [t2] + g.get("t2_also", []):
            if t["type"] not in ANALYTE_TYPES or not set(t["specimens"]) <= SPECIMENS:
                sys.exit(f"{cid}: bad analyte_type or specimen")
        t4_terms = [onto.resolve(*t) for t in g["t4"]["terms"]]
        names = list(g["banned"])
        seen, leakage = set(), []
        lq = lit[cid]["lit_query"]
        maxdate = r["cutoff_date"].replace("-", "/")
        for term in names:
            if term.casefold() in seen or len(term) < 3:
                continue
            seen.add(term.casefold())
            n = pubmed_count(f"{tiab(term)} AND {lq}", maxdate)
            leakage.append({"term": term, "pre_cutoff_hits_with_disease": n, "in_packet": "yes" if n else "no"})
        pre_hits = [b for b in leakage if b["in_packet"] == "yes"]
        ready = r["mechanistic_readiness"]
        items = []
        for j in g["judgment"]:  # "ONLY C001,C002: ..." restricts an item to those cases
            if j.startswith("ONLY "):
                ids, j = j[len("ONLY "):].split(": ", 1)
                if cid not in ids.split(","):
                    continue
            items.append(j)
        judgment = [j for j in items if not j.startswith("NOTE: ")]
        notes = [j[len("NOTE: "):] for j in items if j.startswith("NOTE: ")]
        if pre_hits:
            notes.append("Leakage terms in the packet (in_packet yes; they cannot raise an alarm): "
                         + ", ".join(f"{b['term']} ({b['pre_cutoff_hits_with_disease']})" for b in pre_hits) + ".")
        if leakage and not any(b["in_packet"] == "no" for b in leakage):
            judgment.append("Every leakage term is in the packet, so the leakage alarm cannot fire for this case.")
        dname, dphr = DISPLAY[cid]
        dhits = pubmed_count("(" + " OR ".join(tiab(t) for t in dphr) + ")", maxdate)
        collide = [b["term"] for b in leakage if b["term"].casefold() in dname.casefold()
                   or dname.casefold() in b["term"].casefold()]
        sub = r["subset"]
        subset_clash = sub != "ALL" and (sub.casefold() in dname.casefold() or dname.casefold() == sub.casefold())
        display = {"name": dname, "check_phrases": dphr, "pre_cutoff_hits": dhits,
                   "leakage_term_collisions": collide, "contains_subset_text": subset_clash}
        rubric = {
            "case_id": cid, "status": "DRAFT", "split": "dev" if cid in dev else "test",
            "disease": r["disease"], "mondo_id": r["mondo_id"], "subset": r["subset"], "test": r["test"],
            "test_class": r["test_class"], "test_group": r["test_group"],
            "first_or_improvement": r["first_or_improvement"], "cutoff_date": r["cutoff_date"],
            "discovery_pmid": r["discovery_pmid"], "dating_status": r["dating_status"],
            "arm_display_name": display,
            "T1": {"mechanism_class": mc, "mechanism_class_definition": MECHANISM_CLASSES[mc],
                   "process": onto.resolve(*proc),
                   "t1_only_in_clinical_use": g.get("t1_clinical", [])},
            "T2": [{"analyte_type": t["type"], "allowed_specimens": t["specimens"],
                    "target_class": {"anchor": onto.resolve(*t["anchor"]),
                                     "members": [onto.member(m) for m in t["members"]]},
                    "note": t["note"]} for t in [t2] + g.get("t2_also", [])],
            "T3": {"discovery_experiment": T3[pmid], "source": r["discovery_pmid"]},
            "T4": {"exact_analyte": g["t4"]["label"], "terms": t4_terms, "qualifier": g["t4"]["qualifier"],
                   "reachable_from_pre_cutoff": "no" if ready == "no" else "yes",
                   "reachable_pmid": None if ready == "no" else ready.split()[1]},
            "leakage_terms": leakage,
            "judgment_calls": judgment,
            "notes": notes,
        }
        (OUT / f"{cid}.yaml").write_text(yaml.safe_dump(rubric, sort_keys=False, allow_unicode=True, width=100),
                                         encoding="utf-8")
        review.append(rubric)

    negs = []
    for i, n in enumerate(read_tsv("negatives.tsv"), 1):
        nid = n["slot"]
        if n["kb_file"] not in NEG_DISPLAY:
            sys.exit(f"{nid} {n['kb_file']}: no arm_display_name in NEG_DISPLAY")
        dname, dphr = NEG_DISPLAY[n["kb_file"]]
        dhits = pubmed_count("(" + " OR ".join(tiab(t) for t in dphr) + ")",
                             n["cutoff_date"].replace("-", "/"))
        rubric = {
            "negative_id": nid, "status": "DRAFT", "disease": n["disease"], "kb_file": n["kb_file"],
            "mondo_id": n["mondo_id"], "origin": n["origin"], "h3_usable": n["h3_usable"],
            "monogenic_germline": n["monogenic_germline"],
            "arm_display_name": {"name": dname, "check_phrases": dphr, "pre_cutoff_hits": dhits,
                                 "leakage_term_collisions": [], "contains_subset_text": False},
            "accessible_test": "none: no accessible-specimen confirmatory test",
            "cutoff_date": n["cutoff_date"],
            "cutoff_source": f"matched test case {n['matched_case']} (provisional unmatched seeded draw; "
                             "README, Decisions)",
            "literature_check": {"lit_count": n["lit_count"], "lit_ruling": n["lit_ruling"]},
            "false_positive": NEG_FALSE_POSITIVE,
            "likely_false_positive_candidates": [x.strip() for x in n["measurable_nodes"].split(";")
                                                 if x.strip() and x.strip() != "NA"],
            "leakage_terms": [],
        }
        (OUT / f"{nid}.yaml").write_text(yaml.safe_dump(rubric, sort_keys=False, allow_unicode=True, width=100),
                                         encoding="utf-8")
        negs.append(rubric)

    write_review(review, negs)
    flagged = [r for r in review if r["judgment_calls"]]
    print(f"{len(review)} case rubrics, {len(negs)} negative rubrics; {len(flagged)} cases with judgment calls")


def write_review(cases: list[dict], negs: list[dict]) -> None:
    def block(r: dict) -> list[str]:
        lines = [f"### {r['case_id']} · {r['disease']} · {r['test']} ({r['split']}, cutoff {r['cutoff_date']})", ""]
        if r["judgment_calls"]:
            lines.append(f"- **Judgment:** {r['judgment_calls'][0]}")
            for j in r["judgment_calls"][1:]:
                lines.append(f"  - also: {j}")
        for j in r["notes"]:
            lines.append(f"- **Note:** {j}")
        lines += [
            f"- **T1:** {r['T1']['mechanism_class']}; {r['T1']['process']['label']} ({r['T1']['process']['id']})",
            *[f"- **T2:** {t2['analyte_type']} in {', '.join(t2['allowed_specimens'])}; members "
              + ", ".join(f"{m.get('form') or m['label']} ({m['id']})" for m in t2["target_class"]["members"])
              for t2 in r["T2"]],
            *([f"- **T1 only (in clinical use at cutoff):** {'; '.join(r['T1']['t1_only_in_clinical_use'])}"]
              if r["T1"]["t1_only_in_clinical_use"] else []),
            f"- **T3:** {r['T3']['discovery_experiment']} ({r['T3']['source']})",
            f"- **T4:** {r['T4']['exact_analyte']}; reachable pre-cutoff: {r['T4']['reachable_from_pre_cutoff']}"
            + (f" ({r['T4']['reachable_pmid']})" if r["T4"]["reachable_pmid"] else ""),
            f"- **Arm display name:** {r['arm_display_name']['name']}",
            "- **Leakage terms:** " + ", ".join(b["term"] + (" [in packet]" if b["in_packet"] == "yes" else "")
                                                for b in r["leakage_terms"]),
            ""]
        return lines

    md = ["# Rubrics review (DRAFT)", "", "## Changes", "",
          "Revision 2, 2026-11-16:", ""] + [f"- {c}" for c in CHANGES] + ["",
          "## Arm display names", "",
          "The only disease name an arm sees. `Pre-cutoff hits` is the PubMed count of the check phrases "
          "on or before the cutoff (0 means the name may not be pre-cutoff); `collisions` lists leakage "
          "terms the name contains.", "",
          "| Case | Display name | Cutoff | Pre-cutoff hits | Collisions | Subset text |",
          "|---|---|---|---|---|---|"]
    for r in cases + negs:
        d = r["arm_display_name"]
        md.append(f"| {r.get('case_id') or r.get('negative_id')} | {d['name']} | {r['cutoff_date']} | "
                  f"{d['pre_cutoff_hits']} | {', '.join(d['leakage_term_collisions']) or 'none'} | "
                  f"{'YES' if d['contains_subset_text'] else 'no'} |")
    md += ["", "## How to read the case blocks", "",
          "One block per case. The YAML files in this directory are the rubrics; this page is for reading "
          "them. Every rubric is drafted from the case row and its discovery paper only.", "",
          "- **Order:** cases whose T2 boundary or banned terms needed a judgment come first. Each "
          "leads with a one-line reason; further calls on the same case follow it.",
          "- **Leakage terms:** names of the test and analyte. They are never stripped from packets. "
          "'[in packet]' marks a term that co-occurs with the disease in PubMed on or before the cutoff "
          "(in_packet yes). A term with in_packet no that appears in a curated entry or an arm's output "
          "is a leakage alarm (audit not yet built).",
          "- **Negatives:** they come last.", ""]
    flagged = [r for r in cases if r["judgment_calls"]]
    plain = [r for r in cases if not r["judgment_calls"]]
    md += [f"## Judgment calls ({len(flagged)} cases)", ""]
    for r in flagged:
        md += block(r)
    md += [f"## No judgment needed ({len(plain)} cases)", ""]
    for r in plain:
        md += block(r)
    md += [f"## Negatives ({len(negs)})", "", NEG_FALSE_POSITIVE, ""]
    for n in negs:
        cands = "; ".join(n["likely_false_positive_candidates"]) or "none (no measurable node)"
        lc = n["literature_check"]
        md.append(f"- **{n['negative_id']} {n['disease']}** ({n['origin']}; H3 usable {n['h3_usable']}; "
                  f"cutoff {n['cutoff_date']}, literature {lc['lit_ruling']} {lc['lit_count']}; monogenic "
                  f"germline {n['monogenic_germline']}): likely false positives: {cands}.")
    md.append("")
    (OUT / "rubrics_review.md").write_text("\n".join(md), encoding="utf-8")


if __name__ == "__main__":
    main()
