#!/usr/bin/env bash
# Run a list of independent CI gates a few at a time, and report each one as
# if it had been its own step.
#
# The list comes on stdin, one gate per line:
#
#     Human-readable gate name :: the shell command that runs it
#
# Blank lines and lines starting with `#` are ignored, so a gate's rationale
# can sit directly above it. Every gate runs to completion even when another
# fails; the exit status is 1 if any gate failed, 2 if the list itself is
# malformed, 0 otherwise.
#
# Each gate's output is buffered to a file and printed only when all gates are
# done, in list order, inside a `::group::` block titled PASS/FAIL, the gate
# name and its wall time. So the log reads the same however the gates were
# scheduled, and a failure also gets an `::error` annotation naming the gate.
# A table of results goes to $GITHUB_STEP_SUMMARY when that is set.
#
# One line is printed live as each gate finishes (`finished: NAME ...`). The
# full output waits for the end, so if the step is killed by its timeout,
# those lines are what show which gates never finished.
#
# Why: these gates are whole-repo, offline and independent. One after another
# they took ~10 min of a merge-queue build; four at a time they take less than
# half that (12.2 -> 5.7 min locally, 2026-09-24). Listing the slowest first
# keeps a long gate from starting last and becoming the tail.
#
# Usage:
#     scripts/run_ci_gates.sh [-j JOBS] < gates.txt
#     scripts/run_ci_gates.sh --list < gates.txt    # print name<TAB>command
set -u -o pipefail

jobs=4
list_only=0
while (($#)); do
  case "$1" in
    -j) jobs="$2"; shift 2 ;;
    -j*) jobs="${1#-j}"; shift ;;
    --list) list_only=1; shift ;;
    *) echo "usage: $0 [-j JOBS] [--list] < gates" >&2; exit 2 ;;
  esac
done
if ! [[ "$jobs" =~ ^[1-9][0-9]*$ ]]; then
  echo "error: -j needs a positive integer, got '$jobs'" >&2
  exit 2
fi

names=()
commands=()
declare -A seen=()
lineno=0
while IFS= read -r line || [[ -n "$line" ]]; do
  lineno=$((lineno + 1))
  trimmed="${line#"${line%%[![:space:]]*}"}"
  [[ -z "$trimmed" || "$trimmed" == \#* ]] && continue
  if [[ "$trimmed" != *" :: "* ]]; then
    echo "error: line $lineno is not 'name :: command': $trimmed" >&2
    exit 2
  fi
  name="${trimmed%% :: *}"
  command="${trimmed#* :: }"
  if [[ -z "$name" || -z "$command" ]]; then
    echo "error: line $lineno has an empty name or command: $trimmed" >&2
    exit 2
  fi
  if [[ -n "${seen[$name]:-}" ]]; then
    echo "error: gate name '$name' appears twice" >&2
    exit 2
  fi
  seen[$name]=1
  names+=("$name")
  commands+=("$command")
done

if ((${#names[@]} == 0)); then
  echo "error: no gates given on stdin" >&2
  exit 2
fi

if ((list_only)); then
  for i in "${!names[@]}"; do
    printf '%s\t%s\n' "${names[$i]}" "${commands[$i]}"
  done
  exit 0
fi

workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT

run_one() {
  local i="$1" start end rc
  start=$(date +%s)
  bash -c "${commands[$i]}" >"$workdir/$i.out" 2>&1 </dev/null
  rc=$?
  end=$(date +%s)
  echo "$rc $((end - start))" >"$workdir/$i.status"
  echo "finished: ${names[$i]} (exit $rc, $((end - start))s)"
}

echo "Running ${#names[@]} gates, $jobs at a time. Full output follows when all finish."

running=0
for i in "${!names[@]}"; do
  if ((running >= jobs)); then
    wait -n || true
    running=$((running - 1))
  fi
  run_one "$i" &
  running=$((running + 1))
done
wait

failed=()
summary="| Gate | Result | Seconds |"$'\n'"|---|---|---|"$'\n'
for i in "${!names[@]}"; do
  read -r rc secs <"$workdir/$i.status"
  if [[ "$rc" == 0 ]]; then verdict=PASS; else verdict=FAIL; failed+=("$i"); fi
  echo "::group::$verdict ${names[$i]} (${secs}s)"
  echo "\$ ${commands[$i]}"
  cat "$workdir/$i.out"
  echo "::endgroup::"
  if [[ "$verdict" == FAIL ]]; then
    echo "::error title=${names[$i]}::${names[$i]} failed with exit code $rc; its output is in the group above."
  fi
  summary+="| ${names[$i]} | $verdict | $secs |"$'\n'
done

if [[ -n "${GITHUB_STEP_SUMMARY:-}" ]]; then
  printf '### Whole-repo gates\n\n%s\n' "$summary" >>"$GITHUB_STEP_SUMMARY"
fi

if ((${#failed[@]})); then
  echo
  echo "${#failed[@]} of ${#names[@]} gate(s) failed:"
  for i in "${failed[@]}"; do echo "  - ${names[$i]}"; done
  exit 1
fi
echo "All ${#names[@]} gates passed."
