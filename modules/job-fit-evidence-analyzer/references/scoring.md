# Scoring and decision rules

The score is an **evidence index** for the supplied materials. It is not a measure of a person's worth, a probability of an interview, or a substitute for judgment.

## Evidence values

| Status | Value | Meaning in the index |
| --- | ---: | --- |
| `proven` | 1.00 | Direct evidence supports the requirement. |
| `transferable` | 0.65 | Adjacent evidence supports a credible bridge. |
| `not_shown` | 0.00 | The supplied material provides no evidence. |
| `missing` | 0.00 | Available evidence confirms a gap. |
| `unknown` | excluded | The requirement cannot yet be evaluated. |

For non-hard requirements:

1. Multiply each status value by its weight.
2. Divide earned weight by the weight of assessable items. Exclude `unknown` from both sides.
3. Round the resulting percentage to the nearest five points to avoid false precision.
4. Calculate coverage as assessable weight divided by total non-hard weight.
5. Calculate confidence as coverage multiplied by the weighted average classification confidence of assessable items.

## Interpretation bands

- `strong_evidence`: index 80–100 with at least 70% coverage and no hard-gate issue.
- `promising_evidence`: index 60–75 with at least 55% coverage and no hard-gate issue.
- `weak_evidence`: index below 60 with sufficient coverage. This can still justify applying when the missing items are teachable or the opportunity has strategic value.
- `insufficient_evidence`: coverage below 55%. Ask focused questions before drawing a strong conclusion.

## Hard-gate precedence

- `missing` hard gate: `blocked_by_confirmed_hard_gate`.
- `not_shown`, `unknown`, or `transferable` hard gate: `clarify_hard_gate`.
- All hard gates `proven`: interpret the evidence band normally.

The practical recommendation is separate from the band:

- `apply`: no confirmed blocker, adequate coverage, and strong relevant evidence.
- `apply_with_focus`: no confirmed blocker and a credible evidence story, with clear gaps to address honestly.
- `clarify_first`: a hard gate or too much of the role remains unresolved.
- `skip_due_to_confirmed_gate`: a hard gate is confirmed missing and cannot be resolved for this application.

Do not recommend skipping solely because the evidence index is low.
