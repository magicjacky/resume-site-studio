# Evidence model

Create one record per distinct requirement. Split sentences when they contain requirements that could receive different evidence statuses.

```json
{
  "role": "Example role",
  "requirements": [
    {
      "id": "REQ-001",
      "category": "hard_gate | core | supporting",
      "requirement": "What the role requires",
      "jd_sources": ["JD-003"],
      "status": "proven | transferable | not_shown | missing | unknown",
      "candidate_sources": ["CV-007"],
      "confidence": 0.85,
      "weight": 2,
      "reason": "Concise evidence-based explanation",
      "question": "Optional question that could resolve uncertainty"
    }
  ]
}
```

## Categories

- `hard_gate`: a mandatory condition that can independently block the application, such as work authorization, a legally required license, a stated location constraint, or a required language level. Do not classify ordinary skills as hard gates merely because the posting says “must.”
- `core`: a capability central to the actual work or repeated responsibilities.
- `supporting`: a useful preference, secondary tool, domain familiarity, or differentiator.

Default weights are `2` for core and `1` for supporting. Hard gates are evaluated separately and use no score weight. Change a weight only when the job description clearly gives the requirement unusual importance, and record why.

## Evidence statuses

- `proven`: direct, relevant evidence demonstrates the requirement. Cite the candidate source.
- `transferable`: adjacent evidence makes the capability plausible, but the context, scale, tool, or domain differs. State the bridge that still needs validation.
- `not_shown`: the supplied candidate materials contain no evidence either way. Ask for evidence; do not describe this as a skill deficit.
- `missing`: reliable candidate information confirms the requirement is not met. This is stronger than silence and needs a candidate source or explicit user statement.
- `unknown`: the job requirement itself is unclear, contradictory, or cannot yet be evaluated.

## Confidence

Use a value from `0` to `1` to express the reliability of the classification, not the candidate's skill level.

- `0.90–1.00`: explicit evidence and close context match.
- `0.70–0.89`: clear evidence with a limited inference.
- `0.50–0.69`: partial evidence or meaningful ambiguity.
- Below `0.50`: keep the item visible as uncertain and ask a question.

Do not use keyword presence by itself as proof. Prefer demonstrated actions, artifacts, scope, outcomes, repeated responsibility, or direct user confirmation.
