"""Behavior checks for the evidence scoring rules."""

from pathlib import Path
import importlib.util
import unittest


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "modules"
    / "job-fit-evidence-analyzer"
    / "scripts"
    / "score_fit.py"
)
SPEC = importlib.util.spec_from_file_location("score_fit", SCRIPT)
assert SPEC and SPEC.loader
score_fit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(score_fit)


def requirement(item_id: str, category: str, status: str, confidence: float = 1.0) -> dict:
    item = {
        "id": item_id,
        "category": category,
        "status": status,
        "confidence": confidence,
        "jd_sources": [f"JD-{item_id}"],
    }
    if status in {"proven", "transferable", "missing"}:
        item["candidate_sources"] = [f"CV-{item_id}"]
    return item


class ScoreFitTests(unittest.TestCase):
    def test_missing_hard_gate_overrides_strong_capability_evidence(self) -> None:
        result = score_fit.calculate(
            {
                "requirements": [
                    requirement("GATE-1", "hard_gate", "missing"),
                    requirement("CORE-1", "core", "proven"),
                ]
            }
        )
        self.assertEqual(result["evidence_index"], 100)
        self.assertEqual(result["evidence_band"], "blocked_by_confirmed_hard_gate")
        self.assertEqual(result["recommended_action"], "skip_due_to_confirmed_gate")

    def test_unresolved_hard_gate_requires_clarification(self) -> None:
        result = score_fit.calculate(
            {
                "requirements": [
                    requirement("GATE-1", "hard_gate", "not_shown"),
                    requirement("CORE-1", "core", "proven"),
                ]
            }
        )
        self.assertEqual(result["evidence_band"], "clarify_hard_gate")
        self.assertEqual(result["recommended_action"], "clarify_first")

    def test_low_coverage_prevents_strong_conclusion(self) -> None:
        result = score_fit.calculate(
            {
                "requirements": [
                    requirement("CORE-1", "core", "proven"),
                    requirement("CORE-2", "core", "unknown"),
                    requirement("CORE-3", "core", "unknown"),
                ]
            }
        )
        self.assertEqual(result["evidence_index"], 100)
        self.assertEqual(result["evidence_band"], "insufficient_evidence")
        self.assertEqual(result["evidence_coverage"], 0.33)

    def test_not_shown_is_scored_as_absent_evidence(self) -> None:
        result = score_fit.calculate(
            {
                "requirements": [
                    requirement("CORE-1", "core", "proven"),
                    requirement("CORE-2", "core", "not_shown"),
                ]
            }
        )
        self.assertEqual(result["evidence_index"], 50)
        self.assertEqual(result["status_counts"]["not_shown"], 1)

    def test_supported_status_requires_candidate_source(self) -> None:
        item = requirement("CORE-1", "core", "proven")
        del item["candidate_sources"]
        with self.assertRaisesRegex(ValueError, "candidate_sources"):
            score_fit.calculate({"requirements": [item]})


if __name__ == "__main__":
    unittest.main()
