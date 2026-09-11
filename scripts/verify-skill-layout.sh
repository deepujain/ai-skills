#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
errors=0

while IFS= read -r skill; do
  if ! rg -q '^# ' "$skill"; then
    echo "missing title: ${skill#$root/}" >&2
    errors=1
  fi
done < <(find "$root/projects" "$root/skippy" -name SKILL.md -type f | sort)

for reference in contribution-quality.md continuous-learning.md contribution-queues.md execution-contracts.md verification-receipts.md engineering-principles.md engineering-foundations.md graph-engineering.md project-bootstrap.md delegation.md oss-contribution-system.md sweep-output-contract.md; do
  if [[ ! -f "$root/references/$reference" ]]; then
    echo "missing shared reference: $reference" >&2
    errors=1
  fi
done

for file in playbooks/index.md playbooks/bootstrap-project.md playbooks/continuous-learning.md playbooks/contribution-queue.md skippy/agents/investigator.md skippy/agents/verifier.md scripts/bootstrap-project.sh scripts/configure-project-queue.sh scripts/record-project-learning.sh scripts/skippy-graph.py scripts/verify_sweep_output.py workflows/skippy-delivery.json automations/continuation/sweep-and-replenish-prompt.md; do
  if [[ ! -f "$root/$file" ]]; then
    echo "missing orchestration artifact: $file" >&2
    errors=1
  fi
done

while IFS= read -r skill; do
  if rg -qi 'sweep|replenish' "$skill" && ! rg -Fq 'sweep-output-contract.md' "$skill"; then
    echo "missing canonical sweep output contract: ${skill#$root/}" >&2
    errors=1
  fi
done < <(find "$root/projects" -name SKILL.md -type f | sort)

if rg -l 'Use this table format for .*sweep' "$root/projects" -g SKILL.md >/dev/null; then
  echo "project skill redefines the canonical sweep table" >&2
  errors=1
fi

sweep_prompt="$("$root/scripts/sweep-tick-prompt.sh" superset verification)"
if ! rg -Fq 'verify_sweep_output.py' <<<"$sweep_prompt"; then
  echo "generated sweep prompt omits final-output validation" >&2
  errors=1
fi
if ! rg -Fq 'Maintain → Learn → Replenish' <<<"$sweep_prompt"; then
  echo "generated sweep prompt does not make replenishment default" >&2
  errors=1
fi

if ! python3 -B "$root/scripts/skippy-graph.py" validate \
  "$root/workflows/skippy-delivery.json" >/dev/null; then
  echo "invalid canonical Skippy workflow" >&2
  errors=1
fi

if ! python3 -B -m unittest discover -s "$root/tests" >/dev/null 2>&1; then
  echo "Skippy graph runtime tests failed" >&2
  errors=1
fi

for heading in '## Frame the problem' '## Design the right change' '## Build for operation' '## Verify and learn' '## Collaborate without losing ownership'; do
  if ! rg -Fqx "$heading" "$root/references/engineering-principles.md"; then
    echo "missing engineering decision area: $heading" >&2
    errors=1
  fi
done

for heading in '## Understand before changing' '## Change the product safely' '## Assure and deliver' '## Sustain autonomous and parallel work' '## Selection rules'; do
  if ! rg -Fqx "$heading" "$root/playbooks/index.md"; then
    echo "missing playbook section: $heading" >&2
    errors=1
  fi
done

for file in skippy/SKILL.md playbooks/contribution-queue.md references/contribution-quality.md references/contribution-queues.md automations/continuation/sweep-and-replenish-prompt.md projects/leaflet/SKILL.md; do
  if ! rg -Fq 'rolling 24-hour window' "$root/$file"; then
    echo "missing rolling publication cadence: $file" >&2
    errors=1
  fi
done

if ! rg -Fq 'Cosmetic synonyms, reordered sentences, or arbitrary paragraph-count' "$root/references/contribution-quality.md"; then
  echo "missing repeated-description quality gate" >&2
  errors=1
fi

pacing_prompt="$("$root/scripts/sweep-tick-prompt.sh" superset verification)"
if ! rg -Fq 'tick does not reset the window' <<<"$pacing_prompt"; then
  echo "generated sweep prompt resets publication cadence" >&2
  errors=1
fi
if ! rg -Fq 'open, merged, and closed states' <<<"$pacing_prompt"; then
  echo "generated sweep prompt omits live publication timestamp check" >&2
  errors=1
fi

if ((errors)); then
  exit 1
fi

echo "Skippy skill layout verified."
