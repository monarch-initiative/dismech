"""Batch-add therapeutic_agent to treatments missing it, using confirmed KB IDs."""
import re
from pathlib import Path
from datetime import datetime, timezone
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq, CommentedMap

disorders_dir = Path("kb/disorders")
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Mapping: (regex on treatment name) -> list of (preferred_term, id, label)
# All IDs verified from existing KB therapeutic_agent entries
AGENT_MAPPINGS = [
    # Checkpoint inhibitors
    (r'\bpembrolizumab\b',
     [("pembrolizumab", "NCIT:C106432", "Pembrolizumab")]),
    (r'\bmogamulizumab\b',
     [("mogamulizumab", "NCIT:C62510", "Mogamulizumab")]),
    (r'\bdostarlimab\b',
     [("dostarlimab", "NCIT:C126799", "Dostarlimab")]),
    (r'\batezolizumab\b',
     [("atezolizumab", "NCIT:C106250", "Atezolizumab")]),
    (r'\bnivolumab\b',
     [("nivolumab", "NCIT:C68814", "Nivolumab")]),

    # Anti-CD20 / mAbs
    (r'\brituximab\b',
     [("rituximab", "CHEBI:64357", "rituximab")]),
    (r'\bbrentuximab vedotin\b',
     [("brentuximab vedotin", "NCIT:C66944", "Brentuximab Vedotin")]),
    (r'\btrastuzumab deruxtecan|T-DXd\b',
     [("trastuzumab deruxtecan", "NCIT:C128799", "Trastuzumab Deruxtecan")]),
    (r'\btrastuzumab\b',
     [("trastuzumab", "CHEBI:231601", "trastuzumab")]),
    (r'\beculizumab\b',
     [("eculizumab", "NCIT:C48386", "Eculizumab")]),
    (r'\bdupilumab\b',
     [("dupilumab", "NCIT:C162455", "Dupilumab")]),

    # TKIs - ALK/ROS1/RET
    (r'\bcrizotinib\b',
     [("crizotinib", "CHEBI:64310", "crizotinib")]),
    (r'\blorlatinib\b',
     [("lorlatinib", "CHEBI:143117", "lorlatinib")]),
    (r'\balectinib\b',
     [("alectinib", "CHEBI:90936", "alectinib")]),
    (r'\bbrigatinib\b',
     [("brigatinib", "CHEBI:232810", "brigatinib")]),
    (r'\bselpercatinib\b',
     [("selpercatinib", "NCIT:C134987", "Selpercatinib")]),
    (r'\bpralsetinib\b',
     [("pralsetinib", "NCIT:C132295", "Pralsetinib")]),

    # TKIs - BCR-ABL
    (r'\bimatinib\b',
     [("imatinib", "CHEBI:45783", "imatinib")]),
    (r'\bdasatinib\b',
     [("dasatinib", "CHEBI:49375", "dasatinib (anhydrous)")]),
    (r'\bnilotinib\b',
     [("nilotinib", "CHEBI:52172", "nilotinib")]),
    (r'\bponatinib\b',
     [("ponatinib", "CHEBI:78543", "ponatinib")]),

    # BTK inhibitors
    (r'\bibrutinib\b',
     [("ibrutinib", "CHEBI:76612", "ibrutinib")]),
    (r'\bacalabrutinib\b',
     [("acalabrutinib", "CHEBI:167707", "acalabrutinib")]),

    # BRAF/MEK
    (r'\bdabrafenib\b.*\btrametinib\b|\btrametinib\b.*\bdabrafenib\b',
     [("dabrafenib", "CHEBI:75045", "dabrafenib"),
      ("trametinib", "CHEBI:75998", "trametinib")]),
    (r'\bdabrafenib\b',
     [("dabrafenib", "CHEBI:75045", "dabrafenib")]),
    (r'\btrametinib\b',
     [("trametinib", "CHEBI:75998", "trametinib")]),
    (r'\bencorafenib\b.*\bbinimetinib\b|\bbinimetinib\b.*\bencorafenib\b',
     [("encorafenib", "CHEBI:175851", "encorafenib"),
      ("binimetinib", "CHEBI:133021", "binimetinib")]),

    # Hedgehog inhibitors
    (r'\bvismodegib\b',
     [("vismodegib", "CHEBI:66903", "vismodegib")]),
    (r'\bsonidegib\b',
     [("sonidegib", "CHEBI:90863", "sonidegib")]),

    # HIF inhibitor
    (r'\bbelzutifan\b',
     [("belzutifan", "NCIT:C135627", "Belzutifan")]),

    # IDH inhibitors
    (r'\bivosidenib\b',
     [("ivosidenib", "CHEBI:145430", "ivosidenib")]),

    # JAK inhibitors
    (r'\bruxolitinib\b',
     [("ruxolitinib", "CHEBI:66919", "ruxolitinib")]),
    (r'\bbaricitinib\b',
     [("baricitinib", "CHEBI:95341", "baricitinib")]),

    # VEGFR/multikinase
    (r'\blenvatinib\b.*\bsorafenib\b|\bsorafenib\b.*\blenvatinib\b',
     [("lenvatinib", "CHEBI:85994", "lenvatinib"),
      ("sorafenib", "CHEBI:50924", "sorafenib")]),
    (r'\blenvatinib\b',
     [("lenvatinib", "CHEBI:85994", "lenvatinib")]),
    (r'\bsorafenib\b',
     [("sorafenib", "CHEBI:50924", "sorafenib")]),

    # Hydroxyurea
    (r'\bhydroxyurea\b',
     [("hydroxyurea", "CHEBI:44423", "hydroxyurea")]),

    # Antidiabetic
    (r'\bmetformin\b',
     [("metformin", "CHEBI:6801", "metformin")]),
    (r'\bliraglutide\b',
     [("liraglutide", "CHEBI:167574", "liraglutide")]),
    (r'\bsemaglutide\b',
     [("semaglutide", "CHEBI:71193", "semaglutide")]),
    (r'\bGLP.1 receptor agonist',
     [("liraglutide", "CHEBI:167574", "liraglutide")]),

    # MC4R pathway
    (r'\bsetmelanotide\b',
     [("setmelanotide", "NCIT:C152349", "Setmelanotide")]),

    # Myeloproliferative
    (r'\banagrelide\b',
     [("anagrelide", "CHEBI:142290", "anagrelide")]),
]

def make_agent(preferred_term, tid, label):
    """Build a ruamel CommentedMap for a therapeutic_agent entry."""
    m = CommentedMap()
    m["preferred_term"] = preferred_term
    term = CommentedMap()
    term["id"] = tid
    term["label"] = label
    m["term"] = term
    return m

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
        if tt.get("therapeutic_agent"):
            continue  # already has agents
        name = t.get("name", "")
        for pattern, agents in AGENT_MAPPINGS:
            if re.search(pattern, name, re.IGNORECASE):
                agent_list = CommentedSeq()
                for pt, tid, label in agents:
                    agent_list.append(make_agent(pt, tid, label))
                tt["therapeutic_agent"] = agent_list
                changed = True
                entries_modified += 1
                key = " + ".join(a[0] for a in agents)
                match_counts[key] = match_counts.get(key, 0) + 1
                break

    if changed:
        data["updated_date"] = NOW
        with open(f, "w", encoding="utf-8") as fh:
            ryaml.dump(data, fh)
        files_modified += 1

print(f"Modified {entries_modified} treatment entries across {files_modified} files\n")
for k, v in sorted(match_counts.items(), key=lambda x: -x[1]):
    print(f"  {v:3d}  {k}")
