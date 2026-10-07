/*
 * Browser port of models/neuronal_migration_abm/run.py.
 *
 * Same rules, same draws, same readouts: a run here with the same parameters
 * and run name reproduces run.py's numbers exactly, which
 * tests/test_neuronal_migration_abm_js.py checks against the committed
 * results.json. That exactness is what lets the model page (pages/models/
 * neuronal_migration_abm.html) replay a scenario agent by agent and claim the
 * replay is the committed run rather than a lookalike.
 *
 * Exactness needs three pieces of CPython reproduced here, and nothing else:
 *   - random.Random seeded with a str: the seed integer is the UTF-8 bytes
 *     followed by their SHA-512 digest, read big-endian, fed to MT19937's
 *     init_by_array as little-endian 32-bit words;
 *   - random.random(): MT19937 genrand_res53;
 *   - round(x, n): round-half-even on the exact binary value of x.
 *
 * run.py is the reference implementation. A change to a rule goes there first,
 * then here, and the parity test fails until both agree.
 *
 * No dependencies. Loads as a CommonJS module under node (the parity test)
 * and as a global `NeuronalMigrationABM` in a browser.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  } else {
    root.NeuronalMigrationABM = api;
  }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  // ---------------------------------------------------------------- SHA-512
  const K512 = [
    "428a2f98d728ae22", "7137449123ef65cd", "b5c0fbcfec4d3b2f", "e9b5dba58189dbbc",
    "3956c25bf348b538", "59f111f1b605d019", "923f82a4af194f9b", "ab1c5ed5da6d8118",
    "d807aa98a3030242", "12835b0145706fbe", "243185be4ee4b28c", "550c7dc3d5ffb4e2",
    "72be5d74f27b896f", "80deb1fe3b1696b1", "9bdc06a725c71235", "c19bf174cf692694",
    "e49b69c19ef14ad2", "efbe4786384f25e3", "0fc19dc68b8cd5b5", "240ca1cc77ac9c65",
    "2de92c6f592b0275", "4a7484aa6ea6e483", "5cb0a9dcbd41fbd4", "76f988da831153b5",
    "983e5152ee66dfab", "a831c66d2db43210", "b00327c898fb213f", "bf597fc7beef0ee4",
    "c6e00bf33da88fc2", "d5a79147930aa725", "06ca6351e003826f", "142929670a0e6e70",
    "27b70a8546d22ffc", "2e1b21385c26c926", "4d2c6dfc5ac42aed", "53380d139d95b3df",
    "650a73548baf63de", "766a0abb3c77b2a8", "81c2c92e47edaee6", "92722c851482353b",
    "a2bfe8a14cf10364", "a81a664bbc423001", "c24b8b70d0f89791", "c76c51a30654be30",
    "d192e819d6ef5218", "d69906245565a910", "f40e35855771202a", "106aa07032bbd1b8",
    "19a4c116b8d2d0c8", "1e376c085141ab53", "2748774cdf8eeb99", "34b0bcb5e19b48a8",
    "391c0cb3c5c95a63", "4ed8aa4ae3418acb", "5b9cca4f7763e373", "682e6ff3d6b2b8a3",
    "748f82ee5defb2fc", "78a5636f43172f60", "84c87814a1f0ab72", "8cc702081a6439ec",
    "90befffa23631e28", "a4506cebde82bde9", "bef9a3f7b2c67915", "c67178f2e372532b",
    "ca273eceea26619c", "d186b8c721c0c207", "eada7dd6cde0eb1e", "f57d4f7fee6ed178",
    "06f067aa72176fba", "0a637dc5a2c898a6", "113f9804bef90dae", "1b710b35131c471b",
    "28db77f523047d84", "32caab7b40c72493", "3c9ebe0a15c9bebc", "431d67c49c100d4c",
    "4cc5d4becb3e42b6", "597f299cfc657e2a", "5fcb6fab3ad6faec", "6c44198c4a475817",
  ].map((h) => BigInt("0x" + h));
  const H512 = [
    "6a09e667f3bcc908", "bb67ae8584caa73b", "3c6ef372fe94f82b", "a54ff53a5f1d36f1",
    "510e527fade682d1", "9b05688c2b3e6c1f", "1f83d9abfb41bd6b", "5be0cd19137e2179",
  ].map((h) => BigInt("0x" + h));
  const MASK64 = (1n << 64n) - 1n;
  const rotr = (x, n) => ((x >> n) | (x << (64n - n))) & MASK64;

  function sha512(bytes) {
    const len = bytes.length;
    const padLen = ((len + 17 + 127) >> 7) << 7;
    const msg = new Uint8Array(padLen);
    msg.set(bytes);
    msg[len] = 0x80;
    const bitLen = BigInt(len) * 8n;
    for (let i = 0; i < 16; i++) {
      msg[padLen - 1 - i] = Number((bitLen >> BigInt(8 * i)) & 0xffn);
    }
    const h = H512.slice();
    const w = new Array(80);
    for (let off = 0; off < padLen; off += 128) {
      for (let t = 0; t < 16; t++) {
        let v = 0n;
        for (let b = 0; b < 8; b++) v = (v << 8n) | BigInt(msg[off + t * 8 + b]);
        w[t] = v;
      }
      for (let t = 16; t < 80; t++) {
        const s0 = rotr(w[t - 15], 1n) ^ rotr(w[t - 15], 8n) ^ (w[t - 15] >> 7n);
        const s1 = rotr(w[t - 2], 19n) ^ rotr(w[t - 2], 61n) ^ (w[t - 2] >> 6n);
        w[t] = (w[t - 16] + s0 + w[t - 7] + s1) & MASK64;
      }
      let [a, b, c, d, e, f, g, hh] = h;
      for (let t = 0; t < 80; t++) {
        const S1 = rotr(e, 14n) ^ rotr(e, 18n) ^ rotr(e, 41n);
        const ch = (e & f) ^ (~e & MASK64 & g);
        const t1 = (hh + S1 + ch + K512[t] + w[t]) & MASK64;
        const S0 = rotr(a, 28n) ^ rotr(a, 34n) ^ rotr(a, 39n);
        const maj = (a & b) ^ (a & c) ^ (b & c);
        const t2 = (S0 + maj) & MASK64;
        hh = g; g = f; f = e; e = (d + t1) & MASK64;
        d = c; c = b; b = a; a = (t1 + t2) & MASK64;
      }
      const upd = [a, b, c, d, e, f, g, hh];
      for (let i = 0; i < 8; i++) h[i] = (h[i] + upd[i]) & MASK64;
    }
    const out = new Uint8Array(64);
    for (let i = 0; i < 8; i++) {
      for (let b = 0; b < 8; b++) {
        out[i * 8 + b] = Number((h[i] >> BigInt(56 - 8 * b)) & 0xffn);
      }
    }
    return out;
  }

  // ------------------------------------------------- CPython random.Random
  class PyRandom {
    /** Equivalent to CPython's random.Random(seedString). */
    constructor(seed) {
      const enc = new TextEncoder().encode(String(seed));
      const bytes = new Uint8Array(enc.length + 64);
      bytes.set(enc);
      bytes.set(sha512(enc), enc.length);
      // int.from_bytes(bytes, "big") as little-endian 32-bit words, with the
      // zero high words CPython drops removed.
      const key = [];
      for (let end = bytes.length; end > 0; end -= 4) {
        let word = 0;
        for (let i = Math.max(0, end - 4); i < end; i++) {
          word = ((word << 8) | bytes[i]) >>> 0;
        }
        key.push(word);
      }
      while (key.length > 1 && key[key.length - 1] === 0) key.pop();
      this.mt = new Uint32Array(624);
      this.index = 625;
      this.initByArray(key);
    }

    initGenrand(s) {
      const mt = this.mt;
      mt[0] = s >>> 0;
      for (let i = 1; i < 624; i++) {
        const prev = mt[i - 1] ^ (mt[i - 1] >>> 30);
        mt[i] = (Math.imul(1812433253, prev) + i) >>> 0;
      }
      this.index = 624;
    }

    initByArray(key) {
      const mt = this.mt;
      this.initGenrand(19650218);
      let i = 1;
      let j = 0;
      for (let k = Math.max(624, key.length); k > 0; k--) {
        const prev = mt[i - 1] ^ (mt[i - 1] >>> 30);
        mt[i] = ((mt[i] ^ Math.imul(prev, 1664525)) + key[j] + j) >>> 0;
        i++;
        j++;
        if (i >= 624) { mt[0] = mt[623]; i = 1; }
        if (j >= key.length) j = 0;
      }
      for (let k = 623; k > 0; k--) {
        const prev = mt[i - 1] ^ (mt[i - 1] >>> 30);
        mt[i] = ((mt[i] ^ Math.imul(prev, 1566083941)) - i) >>> 0;
        i++;
        if (i >= 624) { mt[0] = mt[623]; i = 1; }
      }
      mt[0] = 0x80000000;
    }

    genrandInt32() {
      const mt = this.mt;
      if (this.index >= 624) {
        for (let kk = 0; kk < 624; kk++) {
          const y = (mt[kk] & 0x80000000) | (mt[(kk + 1) % 624] & 0x7fffffff);
          mt[kk] = mt[(kk + 397) % 624] ^ (y >>> 1) ^ (y & 1 ? 0x9908b0df : 0);
        }
        this.index = 0;
      }
      let y = mt[this.index++];
      y ^= y >>> 11;
      y ^= (y << 7) & 0x9d2c5680;
      y ^= (y << 15) & 0xefc60000;
      y ^= y >>> 18;
      return y >>> 0;
    }

    /** random.random(): 53-bit float in [0, 1). */
    random() {
      const a = this.genrandInt32() >>> 5;
      const b = this.genrandInt32() >>> 6;
      return (a * 67108864 + b) / 9007199254740992;
    }
  }

  // ------------------------------------------------------ CPython round(x, n)
  const F64 = new Float64Array(1);
  const U32 = new Uint32Array(F64.buffer);
  const LITTLE = new Uint8Array(new Uint16Array([1]).buffer)[0] === 1;

  /** round(x, n) with CPython's semantics: half-even on the exact double. */
  function pyRound(x, n) {
    if (x === null || x === undefined) return x;
    if (!isFinite(x) || x === 0) return x;
    F64[0] = Math.abs(x);
    const hi = U32[LITTLE ? 1 : 0];
    const lo = U32[LITTLE ? 0 : 1];
    const expBits = (hi >>> 20) & 0x7ff;
    let mant = (BigInt(hi & 0xfffff) << 32n) | BigInt(lo);
    let exp;
    if (expBits === 0) {
      exp = -1074;
    } else {
      mant |= 1n << 52n;
      exp = expBits - 1075;
    }
    // |x| = mant * 2^exp; compute q = round_half_even(|x| * 10^n)
    let num = mant * 10n ** BigInt(n);
    let q;
    if (exp >= 0) {
      q = num << BigInt(exp);
    } else {
      const den = 1n << BigInt(-exp);
      q = num / den;
      const r2 = (num % den) * 2n;
      if (r2 > den || (r2 === den && q % 2n === 1n)) q += 1n;
    }
    const value = Number(`${q}e-${n}`);
    return x < 0 ? -value : value;
  }

  /** str() of a Python float, as run.py interpolates sweep values into seeds. */
  function pyFloatStr(v) {
    return Number.isInteger(v) ? `${v}.0` : String(v);
  }

  // ------------------------------------------------------------------ model
  const PATTERN_THRESHOLDS = {
    normal_min_plate_fraction: 0.95,
    normal_min_lamination_fidelity: 0.95,
    band_min_affected_arrested_fraction: 0.5,
    band_min_unaffected_plate_fraction: 0.9,
    band_min_band_score: 0.6,
    failure_max_plate_fraction: 0.5,
    band_half_width: 5.0,
  };

  const INPUT_DEFAULTS = {
    perturbation: 0.0,
    affected_fraction: 0.0,
    base_motility: 0.8,
    arrest_rate: 0.0,
    rescue: 0.0,
  };

  function inputDefaults(spec) {
    const defaults = Object.assign({}, INPUT_DEFAULTS);
    for (const [name, body] of Object.entries(spec.inputs || {})) {
      if (body && typeof body === "object" && "default" in body) {
        defaults[name] = body.default;
      }
    }
    return defaults;
  }

  function paramsFrom(mapping, defaults) {
    const params = Object.assign({}, defaults);
    for (const [k, v] of Object.entries(mapping || {})) {
      if (k in params) params[k] = v;
    }
    return params;
  }

  function zone(column, position) {
    if (position < column.vz_top) return "ventricular_zone";
    if (position < column.plate_floor) return "intermediate_zone";
    return "cortical_plate";
  }

  const STATE_CODE = { migrating: 0, arrested: 1, settled: 2 };

  /**
   * Simulate one parameter set. Mirrors run.simulate, including the optional
   * trace of agent positions every `traceEvery` steps.
   */
  function simulate(spec, params, runName, trace, traceEvery) {
    traceEvery = traceEvery || 4;
    const dom = spec.domain;
    const cohorts = spec.cohorts;
    const column = {
      vz_top: Number(dom.ventricular_zone_top),
      plate_floor: Number(dom.cortical_plate_floor),
      pia: Number(dom.pia),
      step_length: Number(dom.step_length),
      settled_cell_thickness: Number(dom.settled_cell_thickness),
      birth_position: Number(dom.birth_position),
      n_settled: 0,
    };
    column.plate_top = column.plate_floor;
    const rng = new PyRandom(`${spec.seed}:${runName}`);

    const nCohorts = Math.trunc(cohorts.count);
    const cohortSize = Math.trunc(cohorts.size);
    const interval = Math.trunc(cohorts.birth_interval);
    const lastBirth = (nCohorts - 1) * interval;
    const tEnd = lastBirth + Math.trunc(cohorts.migration_window);

    const neurons = [];
    for (let cohort = 0; cohort < nCohorts; cohort++) {
      for (let k = 0; k < cohortSize; k++) {
        const affected = rng.random() < params.affected_fraction;
        neurons.push({
          cohort,
          affected,
          birth_time: cohort * interval,
          position: column.birth_position,
          state: "migrating",
          settle_rank: -1,
          arrival_time: -1,
        });
      }
    }

    if (trace) {
      trace.cohort = neurons.map((n) => n.cohort);
      trace.affected = neurons.map((n) => (n.affected ? 1 : 0));
      trace.domain = {
        vz_top: column.vz_top,
        plate_floor: column.plate_floor,
        pia: column.pia,
      };
      trace.frames = [];
    }

    for (let t = 0; t <= tEnd; t++) {
      if (trace && t % traceEvery === 0) {
        trace.frames.push({
          t,
          pos: neurons.map((n) => (n.birth_time <= t ? pyRound(n.position, 1) : null)),
          state: neurons.map((n) => STATE_CODE[n.state]),
          plate_top: pyRound(column.plate_top, 2),
        });
      }
      for (const n of neurons) {
        if (n.state !== "migrating" || n.birth_time > t) continue;
        // effective_perturbation
        const e = n.affected ? params.perturbation * (1.0 - params.rescue) : 0.0;
        // arrest: confined to the intermediate zone
        if (
          params.arrest_rate > 0 &&
          e > 0 &&
          zone(column, n.position) === "intermediate_zone" &&
          rng.random() < params.arrest_rate * e
        ) {
          n.state = "arrested";
          continue;
        }
        // slowed_nucleokinesis
        if (rng.random() < params.base_motility * (1.0 - e)) {
          n.position = Math.min(n.position + column.step_length, column.pia);
        }
        // inside_out_settling
        if (n.position >= column.plate_top) {
          n.state = "settled";
          n.settle_rank = column.n_settled;
          n.arrival_time = t;
          column.n_settled += 1;
          column.plate_top =
            column.plate_floor + column.settled_cell_thickness * column.n_settled;
        }
      }
    }
    return score(neurons, column, nCohorts, tEnd);
  }

  function bisectLeft(sorted, x) {
    let lo = 0;
    let hi = sorted.length;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (sorted[mid] < x) lo = mid + 1;
      else hi = mid;
    }
    return lo;
  }

  function laminationFidelity(settled, nCohorts) {
    const ranks = Array.from({ length: nCohorts }, () => []);
    for (const n of settled) ranks[n.cohort].push(n.settle_rank);
    for (const r of ranks) r.sort((a, b) => a - b);
    let concordant = 0;
    let total = 0;
    for (let a = 0; a < nCohorts; a++) {
      for (let b = a + 1; b < nCohorts; b++) {
        const earlier = ranks[a];
        const later = ranks[b];
        if (!earlier.length || !later.length) continue;
        for (const r of later) concordant += bisectLeft(earlier, r);
        total += earlier.length * later.length;
      }
    }
    return total === 0 ? null : concordant / total;
  }

  function median(sorted) {
    const n = sorted.length;
    const i = n >> 1;
    return n % 2 === 1 ? sorted[i] : (sorted[i - 1] + sorted[i]) / 2;
  }

  function score(neurons, column, nCohorts, tEnd) {
    const total = neurons.length;
    const settled = neurons.filter((n) => n.state === "settled");
    const arrested = neurons.filter((n) => n.state === "arrested");
    const inTransit = neurons.filter((n) => n.state === "migrating");
    const ectopic = arrested.concat(inTransit);

    const zoneCounts = { ventricular_zone: 0, intermediate_zone: 0, cortical_plate: 0 };
    for (const n of ectopic) zoneCounts[zone(column, n.position)] += 1;

    const affected = neurons.filter((n) => n.affected);
    const unaffected = neurons.filter((n) => !n.affected);
    const plateFraction = (group) =>
      group.length ? group.filter((n) => n.state === "settled").length / group.length : null;

    const affectedEctopic = affected.filter((n) => n.state !== "settled");
    const affectedArrested = affected.filter((n) => n.state === "arrested");
    let bandScore = null;
    let bandMedianDepth = null;
    if (affectedArrested.length) {
      const depths = affectedArrested.map((n) => n.position).sort((a, b) => a - b);
      bandMedianDepth = median(depths);
      const half = PATTERN_THRESHOLDS.band_half_width;
      bandScore =
        depths.filter((d) => Math.abs(d - bandMedianDepth) <= half).length / depths.length;
    }

    const fidelity = laminationFidelity(settled, nCohorts);
    const delays = settled.map((n) => n.arrival_time - n.birth_time);
    const perCohort = [];
    for (let c = 0; c < nCohorts; c++) {
      perCohort.push(pyRound(plateFraction(neurons.filter((n) => n.cohort === c)) || 0.0, 4));
    }

    const r = {
      cortical_plate_fraction: pyRound(settled.length / total, 4),
      ectopic_fraction: pyRound(ectopic.length / total, 4),
      arrested_fraction: pyRound(arrested.length / total, 4),
      in_transit_fraction: pyRound(inTransit.length / total, 4),
      ectopic_by_zone: Object.fromEntries(
        Object.entries(zoneCounts).map(([k, v]) => [k, pyRound(v / total, 4)])
      ),
      lamination_fidelity: fidelity === null ? null : pyRound(fidelity, 4),
      mean_arrival_delay: delays.length
        ? pyRound(delays.reduce((s, d) => s + d, 0) / delays.length, 2)
        : null,
      cortical_plate_thickness: pyRound(column.settled_cell_thickness * settled.length, 2),
      per_cohort_plate_fraction: perCohort,
      affected_plate_fraction: affected.length ? pyRound(plateFraction(affected), 4) : null,
      unaffected_plate_fraction: unaffected.length ? pyRound(plateFraction(unaffected), 4) : null,
      affected_ectopic_fraction: affected.length
        ? pyRound(affectedEctopic.length / affected.length, 4)
        : null,
      affected_arrested_fraction: affected.length
        ? pyRound(affectedArrested.length / affected.length, 4)
        : null,
      band_score: bandScore === null ? null : pyRound(bandScore, 4),
      band_median_depth: bandMedianDepth === null ? null : pyRound(bandMedianDepth, 2),
      window_end: tEnd,
    };
    r.pattern = classify(r);
    return r;
  }

  function classify(r) {
    const th = PATTERN_THRESHOLDS;
    const plate = r.cortical_plate_fraction;
    const fidelity = r.lamination_fidelity !== null ? r.lamination_fidelity : 0.0;
    if (plate >= th.normal_min_plate_fraction && fidelity >= th.normal_min_lamination_fidelity) {
      return "normal";
    }
    if (
      r.affected_arrested_fraction !== null &&
      r.unaffected_plate_fraction !== null &&
      r.band_score !== null &&
      r.affected_arrested_fraction >= th.band_min_affected_arrested_fraction &&
      r.unaffected_plate_fraction >= th.band_min_unaffected_plate_fraction &&
      r.band_score >= th.band_min_band_score
    ) {
      return "band_heterotopia";
    }
    if (plate < th.failure_max_plate_fraction) return "migration_failure";
    if (plate >= th.normal_min_plate_fraction) return "delayed_lamination";
    return "diffuse_ectopia";
  }

  function activatedPhenotypes(spec, readouts) {
    const active = [];
    for (const mapping of spec.phenotype_mappings || []) {
      let holds = true;
      for (const cond of mapping.conditions) {
        const value = readouts[cond.variable];
        if (value === null || value === undefined) { holds = false; break; }
        if (cond.direction === "above") holds = value >= cond.threshold;
        else if (cond.direction === "below") holds = value < cond.threshold;
        else throw new Error(`unknown direction ${cond.direction}`);
        if (!holds) break;
      }
      if (holds) active.push(Object.assign({}, mapping.phenotype));
    }
    return active;
  }

  /** Mirror of run.build_results: every scenario and sweep in the spec. */
  function buildResults(spec) {
    const defaults = inputDefaults(spec);
    const scenarios = {};
    for (const [name, body] of Object.entries(spec.scenarios)) {
      const params = paramsFrom(body, defaults);
      const readouts = simulate(spec, params, `scenario:${name}`);
      scenarios[name] = {
        description: body.description || "",
        params,
        readouts,
        activated_phenotypes: activatedPhenotypes(spec, readouts),
      };
    }
    const sweeps = {};
    for (const [name, body] of Object.entries(spec.sweeps)) {
      const rows = [];
      for (const value of body.values) {
        const mapping = Object.assign({}, body.fixed || {});
        mapping[body.vary] = value;
        const params = paramsFrom(mapping, defaults);
        const readouts = simulate(spec, params, `sweep:${name}:${pyFloatStr(value)}`);
        rows.push({
          [body.vary]: value,
          cortical_plate_fraction: readouts.cortical_plate_fraction,
          arrested_fraction: readouts.arrested_fraction,
          in_transit_fraction: readouts.in_transit_fraction,
          lamination_fidelity: readouts.lamination_fidelity,
          mean_arrival_delay: readouts.mean_arrival_delay,
          band_score: readouts.band_score,
          affected_arrested_fraction: readouts.affected_arrested_fraction,
          unaffected_plate_fraction: readouts.unaffected_plate_fraction,
          pattern: readouts.pattern,
          activated_phenotypes: activatedPhenotypes(spec, readouts).map((p) => p.id),
        });
      }
      sweeps[name] = { vary: body.vary, fixed: body.fixed || {}, rows };
    }
    return {
      model_id: spec.model_id,
      source_entry: spec.source_entry,
      seed: spec.seed,
      pattern_thresholds: PATTERN_THRESHOLDS,
      scenarios,
      sweeps,
    };
  }

  return {
    PATTERN_THRESHOLDS,
    PyRandom,
    activatedPhenotypes,
    buildResults,
    classify,
    inputDefaults,
    paramsFrom,
    pyRound,
    sha512,
    simulate,
  };
});
