#!/usr/bin/env python3
"""Therapy-specific guideline search: find guidelines whose ABSTRACT names drugs.

The project's original ranking (guideline_search_all.jsonl) used a generic
'"Practice Guideline"[pt] AND <disease>' query. That reliably surfaces flagship
umbrella guidelines whose abstracts are scope/structure boilerplate naming no
drug -- unusable for snippet-verified evidence. This variant adds drug-name
terms and scores each hit by how many drug-naming sentences its abstract has.
"""
import json, re, sys, time, urllib.parse, urllib.request

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "tool=dismech&email=jhc@lbl.gov"

def _get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8", "replace")

def esearch(term, retmax=6):
    u = f"{EUTILS}/esearch.fcgi?db=pubmed&term={urllib.parse.quote(term)}&retmax={retmax}&retmode=json&{TOOL}"
    return json.loads(_get(u))["esearchresult"]["idlist"]

def efetch_abstract(pmid):
    u = f"{EUTILS}/efetch.fcgi?db=pubmed&id={pmid}&rettype=abstract&retmode=text&{TOOL}"
    return re.sub(r"\s+", " ", _get(u))

def drug_sentences(text, drugs):
    rx = re.compile("|".join(drugs), re.I)
    return [s.strip() for s in re.split(r"(?<=[.:]) ", text) if rx.search(s)]

def title_of(text):
    m = re.search(r"\d{4}[;:][^.]*\.\s*(.+?\.)\s", text)
    return m.group(1).strip() if m else ""

def run(slug, term, drugs, retmax=6):
    """Return a metadata record for one disease's therapy-specific search."""
    pmids = esearch(term, retmax)
    time.sleep(0.4)
    hits = []
    for p in pmids:
        try:
            txt = efetch_abstract(p)
        except Exception as e:
            hits.append({"pmid": p, "error": str(e)[:60]}); continue
        ds = drug_sentences(txt, drugs)
        hits.append({
            "pmid": p,
            "title": title_of(txt)[:160],
            "abstract_len": len(txt),
            "drug_sentence_count": len(ds),
            "sample_drug_sentence": ds[0][:240] if ds else None,
        })
        time.sleep(0.4)
    hits.sort(key=lambda h: -h.get("drug_sentence_count", 0))
    return {"slug": slug, "query": term, "drug_terms": drugs,
            "n_hits": len(pmids), "hits": hits}

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    out = [run(s["slug"], s["query"], s["drugs"]) for s in spec]
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    for r in out:
        best = r["hits"][0] if r["hits"] else {}
        print(f"{r['slug']}: {r['n_hits']} hits | best PMID:{best.get('pmid')} "
              f"drug-sents={best.get('drug_sentence_count')} | {(best.get('title') or '')[:60]}")
