// Injected into the active tab to extract paper / disease metadata.
// Runs in the page's context; the value of the final IIFE is returned to the
// popup via chrome.scripting.executeScript.
(() => {
  const meta = (name) => {
    const el =
      document.querySelector(`meta[name="${name}" i]`) ||
      document.querySelector(`meta[property="${name}" i]`);
    return el ? (el.getAttribute("content") || "").trim() : "";
  };
  const metaAll = (name) =>
    Array.from(
      document.querySelectorAll(
        `meta[name="${name}" i], meta[property="${name}" i]`
      )
    )
      .map((el) => (el.getAttribute("content") || "").trim())
      .filter(Boolean);

  const href = location.href;
  const host = location.hostname.replace(/^www\./, "");
  const path = location.pathname;

  const ids = {};

  // ---- Paper identifiers ---------------------------------------------------
  // PMID
  let pmid = meta("citation_pmid") || meta("ncbi_uid");
  if (!pmid && /(^|\.)pubmed\.ncbi\.nlm\.nih\.gov$/.test(host)) {
    const m = path.match(/\/(\d{4,9})\/?$/);
    if (m) pmid = m[1];
  }
  if (!pmid) {
    const m = href.match(/[?&]list_uids=(\d{4,9})/);
    if (m) pmid = m[1];
  }
  if (pmid) ids.pmid = pmid;

  // PMCID
  let pmcid = meta("citation_pmcid");
  const pmcMatch = href.match(/PMC(\d{4,9})/i);
  if (!pmcid && pmcMatch) pmcid = "PMC" + pmcMatch[1];
  if (pmcid) ids.pmcid = pmcid.toUpperCase().startsWith("PMC")
    ? pmcid.toUpperCase()
    : "PMC" + pmcid;

  // DOI
  let doi =
    meta("citation_doi") ||
    meta("prism.doi") ||
    meta("dc.identifier") ||
    meta("DC.identifier") ||
    meta("bepress_citation_doi");
  const cleanDoi = (s) => {
    if (!s) return "";
    const m = s.match(/10\.\d{4,9}\/[^\s"'<>]+/);
    return m ? m[0].replace(/[.,;)]+$/, "") : "";
  };
  doi = cleanDoi(doi);
  if (!doi && /(^|\.)doi\.org$/.test(host)) doi = cleanDoi(decodeURIComponent(path.slice(1)));
  if (!doi) {
    const canon = document.querySelector('link[rel="canonical"]');
    if (canon) doi = cleanDoi(canon.href);
  }
  if (!doi) doi = cleanDoi(href);
  if (doi) ids.doi = doi;

  // ---- Disease identifiers -------------------------------------------------
  const grab = (re) => {
    const m = decodeURIComponent(href).match(re);
    return m ? m[1] : "";
  };
  const mondo = grab(/MONDO[:_](\d{5,7})/i);
  if (mondo) ids.mondo = "MONDO:" + mondo;

  let omim = "";
  if (/(^|\.)omim\.org$/.test(host)) {
    const m = path.match(/\/entry\/(\d{4,7})/);
    if (m) omim = m[1];
  }
  if (!omim) omim = grab(/OMIM[:_](\d{4,7})/i);
  if (omim) ids.omim = "OMIM:" + omim;

  let orpha = grab(/ORPHA[:_](\d{1,7})/i) || grab(/Orphanet_(\d{1,7})/i);
  if (!orpha && /orpha\.net$/.test(host)) {
    const m = href.match(/[?&]Expert=(\d{1,7})/i);
    if (m) orpha = m[1];
  }
  if (orpha) ids.orpha = "ORPHA:" + orpha;

  const doid = grab(/DOID[:_](\d{1,7})/i);
  if (doid) ids.doid = "DOID:" + doid;

  const mesh = grab(/\/mesh\/(D\d{6})/i);
  if (mesh) ids.mesh = "MESH:" + mesh;

  // ---- Common metadata -----------------------------------------------------
  const title =
    meta("citation_title") ||
    meta("dc.title") ||
    meta("og:title") ||
    (document.querySelector("h1") &&
      document.querySelector("h1").textContent.trim()) ||
    (document.title || "").trim();

  const journal = meta("citation_journal_title") || meta("prism.publicationName");
  const date =
    meta("citation_publication_date") ||
    meta("citation_date") ||
    meta("prism.publicationDate") ||
    meta("dc.date");
  const year = (date.match(/\d{4}/) || [""])[0];
  const authors = metaAll("citation_author").slice(0, 12);

  const selection = (window.getSelection && String(window.getSelection()) || "")
    .trim()
    .slice(0, 1200);

  const hasDisease = !!(ids.mondo || ids.omim || ids.orpha || ids.doid);
  const hasPaper = !!(ids.pmid || ids.doi || ids.pmcid);
  const kind = hasDisease ? "disease" : hasPaper ? "paper" : "unknown";

  return {
    kind,
    ids,
    title: (title || "").replace(/\s+/g, " ").trim(),
    journal,
    year,
    authors,
    selection,
    url: href,
    host,
  };
})();
