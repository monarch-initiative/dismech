// Self-provide Mermaid so the docs do not depend on Material for MkDocs
// fetching it from unpkg at runtime. Material's bundle only fetches Mermaid
// from unpkg when `window.mermaid` is undefined; by importing it here from a
// reliable CDN and assigning it to `window.mermaid`, Material detects the
// existing instance, skips the unpkg fetch, and drives rendering itself
// (initialize + run, including across `navigation.instant` page loads).
//
// This fixes Mermaid diagrams on the generated schema pages not rendering when
// the unpkg fetch is blocked or flaky.
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

window.mermaid = mermaid;

// Pre-initialize with sensible defaults. Material re-calls initialize when it
// mounts each diagram, but setting it here guarantees a usable config even if
// a diagram is rendered before Material's mount runs.
mermaid.initialize({ startOnLoad: false });
