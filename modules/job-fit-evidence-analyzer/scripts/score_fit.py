"""Calculate a transparent job-fit evidence index from structured requirements."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


STATUS_VALUES = {
    "proven": 1.0,
    "transferable": 0.65,
    "not_shown": 0.0,
    "missing": 0.0,
}
VALID_STATUSES = set(STATUS_VALUES) | {"unknown"}
VALID_CATEGORIES = {"hard_gate", "core", "supporting"}
DEFAULT_WEIGHTS = {"hard_gate": 0.0, "core": 2.0, "supporting": 1.0}


def rounded_five(value: float) -> int:
    return int(5 * round(value / 5))


def validate_requirement(item: dict[str, Any], index: int) -> None:
    prefix = f"requirements[{index}]"
    for key in ("id", "category", "status", "confidence"):
        if key not in item:
            raise ValueError(f"{prefix}.{key} is required")
    if item["category"] not in VALID_CATEGORIES:
        raise ValueError(f"{prefix}.category must be one of {sorted(VALID_CATEGORIES)}")
    if item["status"] not in VALID_STATUSES:
        raise ValueError(f"{prefix}.status must be one of {sorted(VALID_STATUSES)}")
    jd_sources = item.get("jd_sources")
    if not isinstance(jd_sources, list) or not jd_sources or not all(
        isinstance(value, str) and value.strip() for value in jd_sources
    ):
        raise ValueError(f"{prefix}.jd_sources must be a non-empty list of source IDs")
    if item["status"] in {"proven", "transferable", "missing"}:
        candidate_sources = item.get("candidate_sources")
        if not isinstance(candidate_sources, list) or not candidate_sources or not all(
            isinstance(value, str) and value.strip() for value in candidate_sources
        ):
            raise ValueError(
                f"{prefix}.candidate_sources must cite evidence for status {item['status']}"
            )
    confidence = item["confidence"]
    if not isinstance(confidence, (int, float)) or isinstance(confidence, bool):
        raise ValueError(f"{prefix}.confidence must be a number from 0 to 1")
    if not 0 <= confidence <= 1:
        raise ValueError(f"{prefix}.confidence must be from 0 to 1")
    weight = item.get("weight", DEFAULT_WEIGHTS[item["category"]])
    if not isinstance(weight, (int, float)) or isinstance(weight, bool) or weight < 0:
        raise ValueError(f"{prefix}.weight must be a non-negative number")
    if item["category"] != "hard_gate" and weight == 0:
        raise ValueError(f"{prefix}.weight must be greater than zero")


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    requirements = payload.get("requirements")
    if not isinstance(requirements, list) or not requirements:
        raise ValueError("requirements must be a non-empty list")

    seen_ids: set[str] = set()
    for index, item in enumerate(requirements):
        if not isinstance(item, dict):
            raise ValueError(f"requirements[{index}] must be an object")
        validate_requirement(item, index)
        item_id = str(item["id"])
        if item_id in seen_ids:
            raise ValueError(f"duplicate requirement id: {item_id}")
        seen_ids.add(item_id)

    hard_gates = [item for item in requirements if item["category"] == "hard_gate"]
    scored = [item for item in requirements if item["category"] != "hard_gate"]
    if not scored:
        raise ValueError("at least one core or supporting requirement is required")

    total_weight = sum(float(item.get("weight", DEFAULT_WEIGHTS[item["category"]])) for item in scored)
    assessable = [item for item in scored if item["status"] != "unknown"]
    assessable_weight = sum(
        float(item.get("weight", DEFAULT_WEIGHTS[item["category"]])) for item in assessable
    )
    earned = sum(
        float(item.get("weight", DEFAULT_WEIGHTS[item["category"]]))
        * STATUS_VALUES[item["status"]]
        for item in assessable
    )
    weighted_confidence = sum(
        float(item.get("weight", DEFAULT_WEIGHTS[item["category"]]))
        * float(item["confidence"])
        for item in assessable
    )

    coverage = assessable_weight / total_weight if total_weight else 0.0
    average_confidence = weighted_confidence / assessable_weight if assessable_weight else 0.0
    confidence = coverage * average_confidence
    evidence_index = rounded_five(100 * earned / assessable_weight) if assessable_weight else None

    blockers = [str(item["id"]) for item in hard_gates if item["status"] == "missing"]
    unresolved_gates = [
        str(item["id"])
        for item in hard_gates
        if item["status"] in {"not_shown", "unknown", "transferable"}
    ]

    if blockers:
        band = "blocked_by_confirmed_hard_gate"
        action = "skip_due_to_confirmed_gate"
    elif unresolved_gates:
        band = "clarify_hard_gate"
        action = "clarify_first"
    elif coverage < 0.55 or evidence_index is None:
        band = "insufficient_evidence"
        action = "clarify_first"
    elif evidence_index >= 80 and coverage >= 0.70:
        band = "strong_evidence"
        action = "apply"
    elif evidence_index >= 60:
        band = "promising_evidence"
        action = "apply_with_focus"
    else:
        band = "weak_evidence"
        action = "apply_with_focus"

    counts = {status: 0 for status in sorted(VALID_STATUSES)}
    for item in requirements:
        counts[item["status"]] += 1

    return {
        "role": payload.get("role", ""),
        "evidence_index": evidence_index,
        "evidence_band": band,
        "evidence_coverage": round(coverage, 2),
        "classification_confidence": round(confidence, 2),
        "recommended_action": action,
        "confirmed_hard_gate_blockers": blockers,
        "unresolved_hard_gates": unresolved_gates,
        "status_counts": counts,
        "disclaimer": "The index measures evidence in the supplied materials; it is not a hiring probability.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON input file; reads stdin when omitted")
    parser.add_argument("--output", type=Path, help="Optional JSON output file")
    args = parser.parse_args()

    try:
        raw = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
        payload = json.loads(raw)
        result = calculate(payload)
        rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2) from error


if __name__ == "__main__":
    main()
