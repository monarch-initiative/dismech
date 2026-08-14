"use strict";

const { DEFAULTS, buildIssue, prefilledUrl, titleOnlyUrl, MAX_PREFILL_URL } =
  globalThis.DismechIssue;
const API_ORIGIN = "https://api.github.com/*";

const $ = (id) => document.getElementById(id);

// Render a status line without innerHTML (extension surface — build DOM nodes).
// `link`, when given, is appended as an {href, text} anchor.
function showStatus(text, cls, link) {
  const s = $("status");
  s.hidden = false;
  s.className = "status" + (cls ? " " + cls : "");
  s.textContent = text;
  if (link) {
    s.append(" ");
    const a = document.createElement("a");
    a.href = link.href;
    a.target = "_blank";
    a.rel = "noopener";
    a.textContent = link.text;
    s.append(a);
  }
}

async function getSettings() {
  const sync = await chrome.storage.sync.get(DEFAULTS);
  const { githubToken } = await chrome.storage.local.get({ githubToken: "" });
  return { ...sync, githubToken };
}

async function getActiveTab() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  return tab;
}

async function extractFromTab(tabId) {
  const results = await chrome.scripting.executeScript({
    target: { tabId },
    files: ["extract.js"],
  });
  return results && results[0] ? results[0].result : null;
}

async function hasApiPermission() {
  return chrome.permissions.contains({ origins: [API_ORIGIN] });
}

async function createViaApi(settings, title, body, labels) {
  // The host permission is granted from the options page (a stable context),
  // not requested here — requesting from the popup tears it down mid-request.
  const res = await fetch(
    `https://api.github.com/repos/${settings.owner}/${settings.repo}/issues`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${settings.githubToken}`,
        Accept: "application/vnd.github+json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        body,
        labels: labels
          ? labels.split(",").map((s) => s.trim()).filter(Boolean)
          : [],
      }),
    }
  );
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`GitHub API ${res.status}: ${txt.slice(0, 200)}`);
  }
  return res.json();
}

// Open the prefilled GitHub form, falling back to clipboard + title-only form
// when the full body would exceed GitHub's URL length limit.
async function openPrefilledForm(settings, title, body, labels) {
  const url = prefilledUrl(settings, title, body, labels);
  if (url.length <= MAX_PREFILL_URL) {
    chrome.tabs.create({ url });
    return;
  }
  try {
    await navigator.clipboard.writeText(body);
  } catch {
    /* clipboard may be unavailable; still open the title-only form */
  }
  chrome.tabs.create({ url: titleOnlyUrl(settings, title, labels) });
}

let SETTINGS = null;
let META = null;

async function init() {
  $("settings-link").addEventListener("click", (e) => {
    e.preventDefault();
    chrome.runtime.openOptionsPage();
  });

  SETTINGS = await getSettings();
  const tab = await getActiveTab();

  if (
    !tab ||
    !tab.id ||
    /^(chrome|edge|about|chrome-extension):/.test(tab.url || "")
  ) {
    showStatus(
      "Open a paper or disease page (PubMed, DOI, Monarch, OMIM, Orphanet…) then click the extension.",
      "error"
    );
    return;
  }

  try {
    META = await extractFromTab(tab.id);
  } catch (err) {
    showStatus(
      "Couldn't read this page. It may be a restricted page. " +
        (err.message || ""),
      "error"
    );
    return;
  }
  if (!META) {
    showStatus("No metadata could be extracted from this page.", "error");
    return;
  }

  const issue = buildIssue(META, SETTINGS);

  $("form").hidden = false;
  const badge = $("kind-badge");
  badge.textContent = META.kind;
  badge.classList.toggle("unknown", META.kind === "unknown");

  const chips = $("id-chips");
  chips.textContent = "";
  for (const v of Object.values(META.ids)) {
    const span = document.createElement("span");
    span.className = "chip";
    span.textContent = v;
    chips.append(span);
  }

  $("title").value = issue.title;
  $("labels").value = issue.labels;
  $("body").value = issue.body;

  const apiReady = SETTINGS.mode === "api" && SETTINGS.githubToken;
  $("mode-note").textContent = apiReady
    ? `One-click mode → creates directly in ${SETTINGS.owner}/${SETTINGS.repo}.`
    : `Opens a pre-filled issue form in ${SETTINGS.owner}/${SETTINGS.repo} — review, then submit.`;

  $("copy").addEventListener("click", async () => {
    await navigator.clipboard.writeText($("body").value);
    $("copy").textContent = "Copied";
    setTimeout(() => ($("copy").textContent = "Copy"), 1200);
  });

  $("create").addEventListener("click", onCreate);
}

async function onCreate() {
  const title = $("title").value.trim();
  const body = $("body").value;
  const labels = $("labels").value.trim();
  const btn = $("create");
  btn.disabled = true;

  try {
    if (SETTINGS.mode === "api" && SETTINGS.githubToken && (await hasApiPermission())) {
      btn.textContent = "Creating…";
      const issue = await createViaApi(SETTINGS, title, body, labels);
      showStatus("Created", "ok", {
        href: issue.html_url,
        text: `#${issue.number}`,
      });
      chrome.tabs.create({ url: issue.html_url });
    } else {
      if (SETTINGS.mode === "api" && SETTINGS.githubToken) {
        // Token mode selected but the api.github.com permission was not granted
        // (grant it from Settings). Fall back to the prefilled form.
        showStatus(
          "Token mode needs api.github.com access — enable it in Settings. Opened the pre-filled form instead.",
          "error"
        );
      }
      await openPrefilledForm(SETTINGS, title, body, labels);
      if (!(SETTINGS.mode === "api" && SETTINGS.githubToken)) window.close();
    }
  } catch (err) {
    showStatus("Failed: " + (err.message || err), "error");
    btn.disabled = false;
    btn.textContent = "Create issue";
  }
}

init();
