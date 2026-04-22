"""Second batch: replace remaining MAXO:0000058 entries with specific terms."""
import yaml, re
from pathlib import Path
from datetime import datetime, timezone
from ruamel.yaml import YAML

disorders_dir = Path("kb/disorders")
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# (regex pattern, new_id, canonical_label, preferred_term)
MAPPINGS = [
    # Supplementation / metabolic
    (r'nitrogen scavenger|ammonia scavenger|sodium benzoate|sodium phenylbut|glycerol phenylbut',
     'MAXO:0000106', 'nutritional supplementation', 'nitrogen scavenger therapy'),
    (r'riboflavin|thiamine|coenzyme q|biotin|selenium|folate|betaine|ribitol',
     'MAXO:0000106', 'nutritional supplementation', 'nutritional supplementation'),
    (r'triheptanoin|medium.chain|MCT oil|dietary fat supplement',
     'MAXO:0000106', 'nutritional supplementation', 'nutritional supplementation'),

    # Supportive / symptomatic
    (r'\baspirin\b|acetylsalicylic',
     'MAXO:0000903', 'aspirin therapy', 'aspirin therapy'),
    (r'\bNSAID|cox.2 inhibitor|ibuprofen|naproxen|celecoxib',
     'MAXO:0000221', 'NSAID therapy', 'NSAID therapy'),
    (r'pain management|analgesic|opioid',
     'MAXO:0000457', 'pain management', 'pain management'),
    (r'loperamide|antidiarrheal|anti.diarrheal',
     'MAXO:0000267', 'gastrointestinal agent therapy', 'gastrointestinal agent therapy'),
    (r'G.CSF|granulocyte.colony|filgrastim|pegfilgrastim',
     'NCIT:C15262', 'Immunotherapy', 'hematopoietic growth factor therapy'),

    # Hormone / endocrine
    (r'insulin therap|\binsulin\b',
     'MAXO:0000259', 'insulin treatment', 'insulin therapy'),
    (r'antithyroid|propylthiouracil|methimazole|thyroid medic',
     'MAXO:0000283', 'hormone modifying therapy', 'hormone modifying therapy'),
    (r'progestin|progesterone|estrogen|testosterone|gnrh|lhrh|leuprolide|aromatase',
     'MAXO:0000283', 'hormone modifying therapy', 'hormone modifying therapy'),
    (r'fertility.sparing hormonal|hormone replacement',
     'MAXO:0000283', 'hormone modifying therapy', 'hormone modifying therapy'),

    # Investigational / gene therapy
    (r'gene therap|mrna therap|\baav\b|lentiviral|\bcrispr\b',
     'MAXO:0001001', 'gene therapy', 'gene therapy'),
    (r'antisense oligonucleotide|splice.switching|siRNA',
     'MAXO:0001593', 'antisense oligonucleotide inhibitor therapy', 'antisense oligonucleotide therapy'),
    (r'dornase alfa|pulmozyme',
     'MAXO:0000312', 'respiratory tract agent therapy', 'respiratory tract agent therapy'),

    # Complement inhibitors
    (r'eculizumab|ravulizumab|avacopan|complement inhibit',
     'MAXO:0001483', 'complement 5 inhibitor agent therapy', 'complement inhibitor therapy'),

    # Biologics / mAb -> Immunotherapy
    (r'dupilumab|omalizumab|mepolizumab|benralizumab|tezepelumab|tralokinumab',
     'NCIT:C15262', 'Immunotherapy', 'biologic therapy'),
    (r'secukinumab|ixekizumab|bimekizumab|guselkumab|risankizumab|tildrakizumab',
     'NCIT:C15262', 'Immunotherapy', 'biologic therapy'),
    (r'ustekinumab|vedolizumab|natalizumab|ozanimod|siponimod',
     'NCIT:C15262', 'Immunotherapy', 'biologic therapy'),
    (r'ocrelizumab|ofatumumab|ublituximab|inebilizumab|satralizumab',
     'NCIT:C15262', 'Immunotherapy', 'biologic therapy'),
    (r'daratumumab|elotuzumab|isatuximab|bortezomib|carfilzomib|ixazomib',
     'NCIT:C15262', 'Immunotherapy', 'biologic therapy'),
    (r'infliximab|adalimumab|etanercept|golimumab|certolizumab|TNF inhibit|anti.TNF',
     'NCIT:C15262', 'Immunotherapy', 'biologic therapy'),
    (r'\bbiologic',
     'NCIT:C15262', 'Immunotherapy', 'biologic therapy'),

    # Small molecule targeted
    (r'PARP inhibit|olaparib|rucaparib|niraparib|talazoparib|veliparib',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),
    (r'ruxolitinib|baricitinib|fedratinib|pacritinib|momelotinib',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),
    (r'entrectinib|repotrectinib|larotrectinib|selitrectinib',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),
    (r'abemaciclib|ribociclib|palbociclib|CDK4.6',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),
    (r'vemurafenib|vandetanib|lapatinib|neratinib|tucatinib',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),
    (r'ezetimibe|bempedoic|statin therap|lipid.lower|cholesterol.lower',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),
    (r'sparsentan|atrasentan|endothelin',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),
    (r'eltrombopag|romiplostim|thrombopoietin',
     'NCIT:C93352', 'Targeted Therapy', 'targeted therapy'),

    # Chemotherapy / cytotoxic
    (r'chemoprevention|chemoprevent',
     'MAXO:0000646', 'cancer chemotherapy', 'chemoprevention'),
    (r'hydroxyurea',
     'MAXO:0000646', 'cancer chemotherapy', 'chemotherapy'),
    (r'azathioprine|mycophenolate|cyclophosphamide|\bmethotrexate\b',
     'MAXO:0000646', 'cancer chemotherapy', 'chemotherapy'),

    # Antimicrobial
    (r'nitazoxanide|antiparasitic',
     'MAXO:0001021', 'antimicrobial agent therapy', 'antimicrobial agent therapy'),
]

ryaml = YAML()
ryaml.preserve_quotes = True
ryaml.width = 4096

files_modified = 0
entries_modified = 0
match_counts = {}

for f in sorted(disorders_dir.glob("*.yaml")):
    if ".history." in f.name:
        continue
    try:
        data = ryaml.load(f)
    except:
        continue

    treatments = data.get("treatments") or []
    changed = False

    for t in treatments:
        tt = t.get("treatment_term") or {}
        term = tt.get("term") or {}
        if term.get("id") != "MAXO:0000058":
            continue
        pt = (tt.get("preferred_term") or "").lower()
        if pt != "pharmacotherapy":
            continue
        name = t.get("name", "")
        for pattern, new_id, new_label, new_pt in MAPPINGS:
            if re.search(pattern, name, re.IGNORECASE):
                term["id"] = new_id
                term["label"] = new_label
                tt["preferred_term"] = new_pt
                changed = True
                entries_modified += 1
                key = f"{new_id} | {new_pt}"
                match_counts[key] = match_counts.get(key, 0) + 1
                break

    if changed:
        data["updated_date"] = NOW
        with open(f, "w", encoding="utf-8") as fh:
            ryaml.dump(data, fh)
        files_modified += 1

print(f"Modified {entries_modified} entries across {files_modified} files\n")
for k, v in sorted(match_counts.items(), key=lambda x: -x[1]):
    print(f"  {v:3d}  {k}")
