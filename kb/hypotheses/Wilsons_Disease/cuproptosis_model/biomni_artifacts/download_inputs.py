#!/usr/bin/env python3
import os, requests, hashlib, csv, json, datetime

BASE_DIR = r'/Users/cjm/.biomni-lake/runs/wilson-cuproptosis-unseeded-20260829/artifacts'
RAW_DIR = os.path.join(BASE_DIR, 'raw')
os.makedirs(RAW_DIR, exist_ok=True)

INPUTS = [
  {
    "identifier": "GSE197406_series_matrix",
    "url": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE197nnn/GSE197406/matrix/GSE197406_series_matrix.txt.gz",
    "filename": "GSE197406_series_matrix.txt.gz"
  },
  {
    "identifier": "GPL570_annotation",
    "url": "https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPLnnn/GPL570/annot/GPL570.annot.gz",
    "filename": "GPL570.annot.gz"
  },
  {
    "identifier": "GSE125637_series_matrix",
    "url": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE125nnn/GSE125637/matrix/GSE125637_series_matrix.txt.gz",
    "filename": "GSE125637_series_matrix.txt.gz"
  },
  {
    "identifier": "GPL1261_annotation",
    "url": "https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL1nnn/GPL1261/annot/GPL1261.annot.gz",
    "filename": "GPL1261.annot.gz"
  }
]

def sha256_file(path, chunk=1024*1024):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return "sha256:" + h.hexdigest()

def main():
    meta = []
    for item in INPUTS:
        url = item["url"]
        fn = os.path.join(RAW_DIR, item["filename"])
        t0 = datetime.datetime.utcnow().isoformat() + "Z"
        r = requests.get(url, stream=True, timeout=300)
        r.raise_for_status()
        with open(fn, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
        info = {
            "identifier": item["identifier"],
            "canonical_url": url,
            "local_path": os.path.relpath(fn, BASE_DIR),
            "retrieval_time_utc": t0,
            "byte_count": os.path.getsize(fn),
            "sha256": sha256_file(fn),
        }
        print(f"Downloaded {item['identifier']} -> {info['local_path']} ({info['byte_count']} bytes)")
        print(f"Checksum: {info['sha256']} Retrieved: {info['retrieval_time_utc']}")
        meta.append(info)
    preflight = {
        "schema_version": "1.0",
        "utc_generated": datetime.datetime.utcnow().isoformat() + "Z",
        "inputs": meta
    }
    with open(os.path.join(BASE_DIR, "preflight.json"), "w") as f:
        json.dump(preflight, f, indent=2, sort_keys=True)
    with open(os.path.join(BASE_DIR, "input_manifest.tsv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["identifier","canonical_url","local_path","retrieval_time_utc","byte_count","sha256"])
        for m in meta:
            w.writerow([m["identifier"], m["canonical_url"], m["local_path"], m["retrieval_time_utc"], m["byte_count"], m["sha256"]])

if __name__ == "__main__":
    main()
