/**
 * Cloudflare Worker proxy for OpenScientist integration with dismech.
 *
 * Proxies job submission, status polling, report download, and cancellation
 * to the OpenScientist API, keeping the API key server-side.
 */

/**
 * Extracts a .md file from a ZIP archive.
 * Supports STORE (no compression) and DEFLATE methods.
 * Prefers files with "report" in the name, falls back to any .md.
 */
async function extractMarkdownFromZipAsync(data: Uint8Array): Promise<string | null> {
  const view = new DataView(data.buffer, data.byteOffset, data.byteLength);
  const entries: { name: string; offset: number; compSize: number; uncompSize: number; method: number }[] = [];

  for (let i = 0; i < data.length - 30; i++) {
    if (data[i] === 0x50 && data[i + 1] === 0x4b && data[i + 2] === 0x03 && data[i + 3] === 0x04) {
      const method = view.getUint16(i + 8, true);
      const compSize = view.getUint32(i + 18, true);
      const uncompSize = view.getUint32(i + 22, true);
      const nameLen = view.getUint16(i + 26, true);
      const extraLen = view.getUint16(i + 28, true);
      const dataOffset = i + 30 + nameLen + extraLen;

      // Bounds check: skip malformed entries
      if (dataOffset + compSize > data.length) break;

      const name = new TextDecoder().decode(data.subarray(i + 30, i + 30 + nameLen));

      if (name.endsWith(".md")) {
        entries.push({ name, offset: dataOffset, compSize, uncompSize, method });
      }
      i = dataOffset + compSize - 1;
    }
  }

  if (entries.length === 0) return null;

  const target = entries.find(e => e.name.toLowerCase().includes("report")) || entries[0];

  if (target.method === 0) {
    const raw = data.subarray(target.offset, target.offset + target.uncompSize);
    return new TextDecoder("utf-8").decode(raw);
  }

  if (target.method === 8) {
    // DEFLATE — use DecompressionStream
    const compressed = data.subarray(target.offset, target.offset + target.compSize);
    const ds = new DecompressionStream("deflate-raw");
    const writer = ds.writable.getWriter();
    writer.write(compressed);
    writer.close();
    const reader = ds.readable.getReader();
    const chunks: Uint8Array[] = [];
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      chunks.push(value);
    }
    const total = chunks.reduce((s, c) => s + c.length, 0);
    const result = new Uint8Array(total);
    let offset = 0;
    for (const chunk of chunks) {
      result.set(chunk, offset);
      offset += chunk.length;
    }
    return new TextDecoder("utf-8").decode(result);
  }

  return null;
}

export interface Env {
  KV: KVNamespace;
  OPENSCIENTIST_API_KEY: string;
  OPENSCIENTIST_BASE_URL: string;
  GITHUB_RAW_BASE: string;
  GITHUB_RELEASE_KB_ZIP: string;
}

// --- Constants ---

// Default to production; override via OPENSCIENTIST_BASE_URL env var for local dev
const OPENSCIENTIST_BASE_DEFAULT = "https://www.openscientist.io";

function osBase(env: Env): string {
  return (env.OPENSCIENTIST_BASE_URL || OPENSCIENTIST_BASE_DEFAULT).replace(/\/+$/, "");
}

const ALLOWED_ORIGINS = [
  "https://dismech.monarchinitiative.org",
  "http://localhost:8000",
  "http://127.0.0.1:8000",
];

const SLUG_RE = /^[a-zA-Z0-9_-]{1,100}$/;
const MONDO_RE = /^MONDO:\d{7}$/;
const UUID_RE =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

const MAX_QUESTION_LENGTH = 1000;
const RATE_LIMIT_PER_HOUR = 5;
const KV_TTL_SECONDS = 7200; // 2 hours

const TERMINAL_STATUSES = new Set(["completed", "failed", "cancelled"]);

// --- Types ---

interface JobSubmitBody {
  disease_slug: string;
  disease_name: string;
  mondo_id: string;
  question: string;
}

interface KvJobEntry {
  disease_slug: string;
  question: string;
  started_at: string;
  cancel_requested?: boolean;
}

interface KvRunningEntry {
  job_id: string;
  ip: string;
  started_at: string;
}

// --- CORS helpers ---

function getAllowedOrigin(request: Request): string | null {
  const origin = request.headers.get("Origin");
  if (origin && ALLOWED_ORIGINS.includes(origin)) {
    return origin;
  }
  return null;
}

function corsHeaders(origin: string | null): Record<string, string> {
  const headers: Record<string, string> = {
    Vary: "Origin",
  };
  if (origin) {
    headers["Access-Control-Allow-Origin"] = origin;
    headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS";
    headers["Access-Control-Allow-Headers"] = "Content-Type";
    headers["Access-Control-Max-Age"] = "86400";
  }
  return headers;
}

function jsonResponse(
  body: unknown,
  status: number,
  origin: string | null,
  extraHeaders?: Record<string, string>,
): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json",
      ...corsHeaders(origin),
      ...extraHeaders,
    },
  });
}

// --- Rate limiting ---

async function checkIpRateLimit(
  kv: KVNamespace,
  ip: string,
): Promise<{ allowed: boolean; retryAfter?: number }> {
  const key = `ratelimit:ip:${ip}`;
  const raw = await kv.get(key);
  const now = Date.now();

  if (!raw) {
    await kv.put(key, JSON.stringify({ count: 1, window_start: now }), {
      expirationTtl: 3600,
    });
    return { allowed: true };
  }

  const data = JSON.parse(raw) as { count: number; window_start: number };
  const elapsed = now - data.window_start;

  if (elapsed > 3600_000) {
    // Window expired, reset
    await kv.put(key, JSON.stringify({ count: 1, window_start: now }), {
      expirationTtl: 3600,
    });
    return { allowed: true };
  }

  if (data.count >= RATE_LIMIT_PER_HOUR) {
    const retryAfter = Math.ceil((3600_000 - elapsed) / 1000);
    return { allowed: false, retryAfter };
  }

  data.count++;
  const remainingTtl = Math.ceil((3600_000 - elapsed) / 1000);
  await kv.put(key, JSON.stringify(data), {
    expirationTtl: remainingTtl > 0 ? remainingTtl : 1,
  });
  return { allowed: true };
}

// --- GitHub fetch helpers ---

async function fetchPrimaryYaml(
  env: Env,
  slug: string,
): Promise<{ ok: true; content: ArrayBuffer; } | { ok: false; status: number }> {
  const url = `${env.GITHUB_RAW_BASE}/${encodeURIComponent(slug)}.yaml`;
  const resp = await fetch(url);
  if (!resp.ok) {
    return { ok: false, status: resp.status };
  }
  return { ok: true, content: await resp.arrayBuffer() };
}

async function fetchKbZip(
  env: Env,
): Promise<ArrayBuffer | null> {
  const resp = await fetch(env.GITHUB_RELEASE_KB_ZIP, { redirect: "follow" });
  if (!resp.ok) {
    return null;
  }
  return resp.arrayBuffer();
}

// --- Route handlers ---

async function handleSubmitJob(
  request: Request,
  env: Env,
  origin: string | null,
): Promise<Response> {
  // Parse and validate request body
  let body: JobSubmitBody;
  try {
    body = (await request.json()) as JobSubmitBody;
  } catch {
    return jsonResponse({ error: "Invalid JSON body" }, 400, origin);
  }

  const { disease_slug, disease_name, mondo_id, question } = body;

  if (!disease_slug || typeof disease_slug !== "string") {
    return jsonResponse({ error: "disease_slug is required" }, 400, origin);
  }
  if (!SLUG_RE.test(disease_slug)) {
    return jsonResponse({ error: "Invalid disease_slug format" }, 400, origin);
  }
  if (!disease_name || typeof disease_name !== "string") {
    return jsonResponse({ error: "disease_name is required" }, 400, origin);
  }
  if (disease_name.length > 200 || /[\r\n]/.test(disease_name)) {
    return jsonResponse({ error: "Invalid disease_name" }, 400, origin);
  }
  if (mondo_id && typeof mondo_id === "string" && !MONDO_RE.test(mondo_id)) {
    return jsonResponse({ error: "Invalid mondo_id format (expected MONDO:NNNNNNN)" }, 400, origin);
  }
  if (!question || typeof question !== "string") {
    return jsonResponse({ error: "question is required" }, 400, origin);
  }
  const trimmedQuestion = question.trim();
  if (trimmedQuestion.length === 0) {
    return jsonResponse({ error: "question must not be empty" }, 400, origin);
  }
  if (trimmedQuestion.length > MAX_QUESTION_LENGTH) {
    return jsonResponse(
      { error: `question exceeds ${MAX_QUESTION_LENGTH} characters` },
      400,
      origin,
    );
  }

  // Rate limit: per-IP
  const ip = request.headers.get("CF-Connecting-IP") || "unknown";
  const rateCheck = await checkIpRateLimit(env.KV, ip);
  if (!rateCheck.allowed) {
    return jsonResponse(
      { error: "Rate limit exceeded", retry_after: rateCheck.retryAfter },
      429,
      origin,
      { "Retry-After": String(rateCheck.retryAfter) },
    );
  }

  // Rate limit: per-disease concurrency
  const runningKey = `running:${disease_slug}`;
  const existingRaw = await env.KV.get(runningKey);
  if (existingRaw) {
    const existing = JSON.parse(existingRaw) as KvRunningEntry;
    return jsonResponse(
      {
        error: "A job is already running for this disease",
        existing_job_id: existing.job_id,
      },
      409,
      origin,
    );
  }

  // Fetch primary YAML and KB ZIP in parallel
  const [yamlResult, kbZip] = await Promise.all([
    fetchPrimaryYaml(env, disease_slug),
    fetchKbZip(env),
  ]);

  if (!yamlResult.ok) {
    if (yamlResult.status === 404) {
      return jsonResponse(
        { error: `Disorder "${disease_slug}" not found in knowledge base` },
        404,
        origin,
      );
    }
    return jsonResponse(
      { error: "Failed to fetch disorder YAML from GitHub" },
      502,
      origin,
    );
  }

  // Compose research question
  const researchQuestion = [
    `You are researching the disorder "${disease_name}" (${mondo_id || "unknown MONDO ID"}).`,
    "",
    `User Question: ${trimmedQuestion}`,
    "",
    "Two data files are attached:",
    "",
    `1. ${disease_slug}.yaml — the dismech knowledge base entry for this specific disorder. It`,
    "   contains compiled mechanistic data — pathophysiology, phenotypes, genetic basis,",
    "   treatments — generated through deep research, extensively validated, and harmonized",
    "   with ontology standards. Use it as primary context for your research.",
    "",
    "2. dismech_kb.zip — a ZIP archive containing YAML entries for all 55+ disorders in the",
    "   dismech knowledge base (https://dismech.monarchinitiative.org). Use these for",
    "   cross-disease comparisons, shared mechanisms, or related disorder context if relevant",
    "   to the user's question.",
  ].join("\n");

  // Build title
  const titleQuestion =
    trimmedQuestion.length > 200
      ? trimmedQuestion.slice(0, 197) + "..."
      : trimmedQuestion;
  const title = `${disease_name}: ${titleQuestion}`;

  // Build multipart form
  const formData = new FormData();
  formData.append("title", title.slice(0, 255));
  formData.append("research_question", researchQuestion);
  formData.append("max_iterations", "5");
  formData.append("use_hypotheses", "false");
  formData.append("investigation_mode", "autonomous");

  // Attach primary YAML as data_files
  const yamlBlob = new Blob([yamlResult.content], {
    type: "application/x-yaml",
  });
  formData.append("data_files", yamlBlob, `${disease_slug}.yaml`);

  // Attach KB ZIP if available
  if (kbZip) {
    const zipBlob = new Blob([kbZip], { type: "application/zip" });
    formData.append("data_files", zipBlob, "dismech_kb.zip");
  }

  // Submit to OpenScientist — do NOT set Content-Type manually
  const osResp = await fetch(`${osBase(env)}/api/v1/jobs`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.OPENSCIENTIST_API_KEY}`,
    },
    body: formData,
  });

  if (!osResp.ok) {
    const errText = await osResp.text().catch(() => "Unknown error");
    return jsonResponse(
      { error: "OpenScientist API error", detail: errText.slice(0, 500) },
      osResp.status >= 500 ? 502 : osResp.status,
      origin,
    );
  }

  const osData = (await osResp.json()) as Record<string, unknown>;
  const jobId = (osData.job_id || osData.id) as string;
  if (!jobId) {
    return jsonResponse(
      { error: "No job_id in OpenScientist response" },
      502,
      origin,
    );
  }

  const now = new Date().toISOString();

  // Store KV entries for tracking
  await Promise.all([
    env.KV.put(
      runningKey,
      JSON.stringify({ job_id: jobId, ip, started_at: now } satisfies KvRunningEntry),
      { expirationTtl: KV_TTL_SECONDS },
    ),
    env.KV.put(
      `job:${jobId}`,
      JSON.stringify({
        disease_slug,
        question: trimmedQuestion,
        started_at: now,
      } satisfies KvJobEntry),
      { expirationTtl: KV_TTL_SECONDS },
    ),
  ]);

  return jsonResponse(
    {
      job_id: jobId,
      view_url: `${osBase(env)}/job/${jobId}`,
    },
    201,
    origin,
  );
}

async function handleJobStatus(
  jobId: string,
  env: Env,
  origin: string | null,
): Promise<Response> {
  if (!UUID_RE.test(jobId)) {
    return jsonResponse({ error: "Invalid job_id format" }, 400, origin);
  }

  // Verify job is tracked
  const jobRaw = await env.KV.get(`job:${jobId}`);
  if (!jobRaw) {
    return jsonResponse({ error: "Unknown job_id" }, 404, origin);
  }
  const jobEntry = JSON.parse(jobRaw) as KvJobEntry;

  // Proxy to OpenScientist
  const osResp = await fetch(
    `${osBase(env)}/api/v1/jobs/${jobId}/status`,
    {
      headers: { Authorization: `Bearer ${env.OPENSCIENTIST_API_KEY}` },
    },
  );

  if (!osResp.ok) {
    // If upstream returns 5xx repeatedly, clean up the lock so users aren't stuck
    if (osResp.status >= 500 && jobEntry.cancel_requested) {
      await env.KV.delete(`running:${jobEntry.disease_slug}`);
    }
    return jsonResponse(
      { error: `Status check failed (HTTP ${osResp.status})` },
      502,
      origin,
      { "Cache-Control": "no-store" },
    );
  }

  const data = (await osResp.json()) as Record<string, unknown>;
  const status = data.status as string;

  // Clean up locks on terminal status
  if (TERMINAL_STATUSES.has(status)) {
    await env.KV.delete(`running:${jobEntry.disease_slug}`);

    // If failed, fetch error detail
    if (status === "failed") {
      try {
        const detailResp = await fetch(
          `${osBase(env)}/api/v1/jobs/${jobId}`,
          {
            headers: {
              Authorization: `Bearer ${env.OPENSCIENTIST_API_KEY}`,
            },
          },
        );
        if (detailResp.ok) {
          const detail = (await detailResp.json()) as Record<string, unknown>;
          data.error_message = detail.error_message || "Unknown error";
        }
      } catch {
        // Non-critical — proceed without error detail
      }
    }
  }

  return jsonResponse(
    {
      status: data.status,
      current_iteration: data.current_iteration,
      max_iterations: data.max_iterations,
      error_message: data.error_message || null,
    },
    200,
    origin,
    { "Cache-Control": "no-store" },
  );
}

async function handleJobReport(
  jobId: string,
  env: Env,
  origin: string | null,
): Promise<Response> {
  if (!UUID_RE.test(jobId)) {
    return jsonResponse({ error: "Invalid job_id format" }, 400, origin);
  }

  const jobRaw = await env.KV.get(`job:${jobId}`);
  if (!jobRaw) {
    return jsonResponse({ error: "Unknown job_id" }, 404, origin);
  }

  // Try markdown report first
  const osResp = await fetch(
    `${osBase(env)}/api/v1/jobs/${jobId}/report`,
    {
      headers: {
        Authorization: `Bearer ${env.OPENSCIENTIST_API_KEY}`,
        Accept: "text/markdown",
      },
    },
  );

  if (!osResp.ok) {
    return jsonResponse(
      { error: "Failed to fetch report" },
      502,
      origin,
    );
  }

  const contentType = osResp.headers.get("content-type") || "";

  if (contentType.includes("text/") || contentType.includes("markdown")) {
    const text = await osResp.text();
    return new Response(text, {
      status: 200,
      headers: {
        "Content-Type": "text/markdown; charset=utf-8",
        ...corsHeaders(origin),
      },
    });
  }

  // Report is PDF/binary — fall back to artifacts ZIP and extract markdown
  const artifactsResp = await fetch(
    `${osBase(env)}/api/v1/jobs/${jobId}/artifacts`,
    {
      headers: { Authorization: `Bearer ${env.OPENSCIENTIST_API_KEY}` },
    },
  );

  if (!artifactsResp.ok) {
    return jsonResponse(
      {
        kind: "external",
        message: "Report not available as markdown. View on OpenScientist.",
        view_url: `${osBase(env)}/job/${jobId}`,
      },
      200,
      origin,
    );
  }

  // Extract markdown from ZIP using the Web API (no Node deps needed)
  try {
    const zipBytes = await artifactsResp.arrayBuffer();
    const markdown = await extractMarkdownFromZipAsync(new Uint8Array(zipBytes));
    if (markdown) {
      return new Response(markdown, {
        status: 200,
        headers: {
          "Content-Type": "text/markdown; charset=utf-8",
          ...corsHeaders(origin),
        },
      });
    }
  } catch {
    // ZIP extraction failed — fall through to external link
  }

  return jsonResponse(
    {
      kind: "external",
      message: "Report not available as markdown. View on OpenScientist.",
      view_url: `${osBase(env)}/job/${jobId}`,
    },
    200,
    origin,
  );
}

async function handleJobCancel(
  jobId: string,
  env: Env,
  origin: string | null,
): Promise<Response> {
  if (!UUID_RE.test(jobId)) {
    return jsonResponse({ error: "Invalid job_id format" }, 400, origin);
  }

  const jobRaw = await env.KV.get(`job:${jobId}`);
  if (!jobRaw) {
    return jsonResponse({ error: "Unknown job_id" }, 404, origin);
  }

  // Mark cancel_requested and clean up the running lock so new jobs can be submitted
  const jobEntry = JSON.parse(jobRaw) as KvJobEntry;
  jobEntry.cancel_requested = true;
  await Promise.all([
    env.KV.put(`job:${jobId}`, JSON.stringify(jobEntry), {
      expirationTtl: KV_TTL_SECONDS,
    }),
    env.KV.delete(`running:${jobEntry.disease_slug}`),
  ]);

  // Forward cancel to upstream
  const osResp = await fetch(
    `${osBase(env)}/api/v1/jobs/${jobId}/cancel`,
    {
      method: "POST",
      headers: { Authorization: `Bearer ${env.OPENSCIENTIST_API_KEY}` },
    },
  );

  if (!osResp.ok) {
    // Cancel may fail if job already completed — that's okay
    const status = osResp.status;
    if (status >= 500) {
      return jsonResponse(
        { error: "Failed to send cancel to OpenScientist" },
        502,
        origin,
      );
    }
  }

  return jsonResponse(
    { status: "cancel_requested" },
    200,
    origin,
  );
}

// --- Router ---

function parseRoute(
  url: URL,
  method: string,
): { handler: string; jobId?: string } | null {
  const path = url.pathname;

  if (method === "OPTIONS") {
    return { handler: "preflight" };
  }

  if (method === "POST" && path === "/api/jobs") {
    return { handler: "submit" };
  }

  const jobMatch = path.match(/^\/api\/jobs\/([^/]+)/);
  if (!jobMatch) return null;
  const jobId = jobMatch[1];

  if (method === "GET" && path === `/api/jobs/${jobId}/status`) {
    return { handler: "status", jobId };
  }
  if (method === "GET" && path === `/api/jobs/${jobId}/report`) {
    return { handler: "report", jobId };
  }
  if (method === "POST" && path === `/api/jobs/${jobId}/cancel`) {
    return { handler: "cancel", jobId };
  }

  return null;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const origin = getAllowedOrigin(request);
    const route = parseRoute(url, request.method);

    if (!route) {
      return jsonResponse({ error: "Not found" }, 404, origin);
    }

    if (route.handler === "preflight") {
      return new Response(null, {
        status: 204,
        headers: corsHeaders(origin),
      });
    }

    try {
      switch (route.handler) {
        case "submit":
          return await handleSubmitJob(request, env, origin);
        case "status":
          return await handleJobStatus(route.jobId!, env, origin);
        case "report":
          return await handleJobReport(route.jobId!, env, origin);
        case "cancel":
          return await handleJobCancel(route.jobId!, env, origin);
        default:
          return jsonResponse({ error: "Not found" }, 404, origin);
      }
    } catch (err) {
      const message =
        err instanceof Error ? err.message : "Internal server error";
      return jsonResponse({ error: message }, 500, origin);
    }
  },
};
