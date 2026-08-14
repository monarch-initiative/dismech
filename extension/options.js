"use strict";

const { DEFAULTS } = globalThis.DismechIssue;
const API_ORIGIN = "https://api.github.com/*";

const $ = (id) => document.getElementById(id);
const SYNC_KEYS = ["owner", "repo", "trackerIssue", "diseaseLabels", "paperLabels", "mode"];

async function load() {
  const sync = await chrome.storage.sync.get(DEFAULTS);
  const { githubToken } = await chrome.storage.local.get({ githubToken: "" });
  for (const k of SYNC_KEYS) {
    if (k === "mode") continue;
    $(k).value = sync[k];
  }
  // Guard against a stale/corrupt sync store with an unexpected mode value.
  const modeInput =
    document.querySelector(`input[name="mode"][value="${sync.mode}"]`) ||
    $("mode-url");
  modeInput.checked = true;
  $("githubToken").value = githubToken;
  await refreshPermNote();
}

// Request the optional api.github.com host permission from the options page —
// the page persists across Chrome's permission prompt, whereas requesting from
// the popup tears the popup down mid-request (see popup.js).
//
// Call request() as the first statement inside the user-gesture handler: the
// gesture token does not reliably survive an awaited chrome.* call, so a
// contains() pre-check would risk "must be called during a user gesture".
// request() resolves true without prompting when already granted.
async function ensureApiPermission() {
  return chrome.permissions.request({ origins: [API_ORIGIN] });
}

async function refreshPermNote() {
  const note = $("perm-note");
  if (!note) return;
  const mode = document.querySelector('input[name="mode"]:checked')?.value;
  if (mode !== "api") {
    note.textContent = "";
    return;
  }
  const has = await chrome.permissions.contains({ origins: [API_ORIGIN] });
  note.textContent = has
    ? "api.github.com access granted."
    : "Token mode needs permission to reach api.github.com — granted when you save.";
}

async function onModeChange() {
  const mode = document.querySelector('input[name="mode"]:checked')?.value;
  if (mode === "api") await ensureApiPermission();
  await refreshPermNote();
}

async function save() {
  const sync = {};
  for (const k of SYNC_KEYS) {
    if (k === "mode") continue;
    sync[k] = $(k).value.trim();
  }
  const mode = document.querySelector('input[name="mode"]:checked')?.value || "url";
  sync.mode = mode;

  // If saving in token mode, secure the host permission now (options page is a
  // stable context for the prompt). If the user declines, fall back to url mode.
  if (mode === "api") {
    const granted = await ensureApiPermission();
    if (!granted) {
      sync.mode = "url";
      $("mode-url").checked = true;
    }
  }

  await chrome.storage.sync.set(sync);
  await chrome.storage.local.set({ githubToken: $("githubToken").value.trim() });
  await refreshPermNote();

  const saved = $("saved");
  saved.hidden = false;
  setTimeout(() => (saved.hidden = true), 1500);
}

$("save").addEventListener("click", save);
for (const r of document.querySelectorAll('input[name="mode"]')) {
  r.addEventListener("change", onModeChange);
}
load();
