---
name: job-fit-evidence-analyzer
description: Compare a job description with a resume or career history using traceable evidence. Use when the user asks whether to apply, requests job fit or gap analysis, needs hard requirements separated from preferences, or wants an evidence-based brief before tailoring a resume, portfolio, or interview plan. Not for generic resume writing without a target role.
---

# Job Fit Evidence Analyzer

Turn a job description and a candidate's real background into a traceable decision brief. Evaluate the evidence visible in the supplied materials rather than guessing the person's full ability. Keep this skill portable: follow the host's available file, document, browser, and shell tools; no particular product or connector is required.

## Guardrails

- Never invent experience, dates, tools, credentials, scope, metrics, or business results.
- Treat `not_shown` as a documentation gap, not proof that the candidate lacks the ability.
- Keep legal eligibility, required licenses, location, travel, language, clearance, and other hard gates separate from the fit score.
- Phrase risk signals as questions to investigate. Do not infer age, health, family status, ethnicity, gender, religion, disability, or other protected traits.
- Keep resumes and extracted personal data private. Do not publish, upload, or send them without explicit authorization.
- When the job description is incomplete or ambiguous, label the uncertainty instead of silently resolving it.

## Intake

Collect the target job description and the candidate material. Accept text, URLs, PDFs, DOCX files, profile notes, or structured data. If only the job description is available, produce a requirement map and an evidence checklist; do not claim a candidate fit result.

Create stable source IDs while reading:

- `JD-001`, `JD-002`, ... for job-description passages.
- `CV-001`, `CV-002`, ... for resume or career-history passages.
- `USR-001`, `USR-002`, ... for facts stated directly by the user.

Keep short source excerpts in private working notes. The final report can cite IDs and concise paraphrases.

## Workflow

1. **Normalize the sources.** Remove duplicated boilerplate, preserve meaningful wording, and record the source location for every extracted claim.
2. **Extract requirements.** Separate hard gates, core capabilities, supporting preferences, responsibilities, outcomes, domain context, and ambiguous language. Use [references/evidence-model.md](references/evidence-model.md).
3. **Map evidence.** For every requirement, assign exactly one status: `proven`, `transferable`, `not_shown`, `missing`, or `unknown`. Add a confidence value and both source IDs where available.
4. **Check hard gates.** Report confirmed blockers and unresolved gates before any overall fit interpretation. A high capability score cannot override a confirmed hard gate.
5. **Calculate the evidence index.** Use [scripts/score_fit.py](scripts/score_fit.py) for structured inputs or apply the same rules in [references/scoring.md](references/scoring.md). Present the rounded index with its band, coverage, and confidence. Never present it as a probability of hiring.
6. **Decide the next action.** Choose one of: `apply`, `apply_with_focus`, `clarify_first`, or `skip_due_to_confirmed_gate`. Base the choice on evidence, user constraints, and hard gates rather than the index alone.
7. **Build the strategy.** Identify which existing evidence should move higher in the resume or portfolio, what truthful wording can be sharpened, what facts to ask the user for, and what interview examples to prepare.
8. **Run the quality check.** Follow [references/quality-check.md](references/quality-check.md) before delivering the report.

## Output contract

Use the concise structure in [references/report-format.md](references/report-format.md). Every consequential conclusion must point to a requirement ID and candidate evidence ID, or be marked `unverified`. Keep these concepts visibly separate:

- **Ability fit:** evidence for doing the work.
- **Evidence coverage:** how much of the role could be assessed from supplied material.
- **Hard-gate status:** eligibility or mandatory constraints.
- **Application action:** the practical recommendation.

When preparing content for a resume website, pass the verified evidence, target priorities, and unresolved questions to `resume-site-studio` if that skill is available. The downstream site must not turn an unverified or transferable claim into a proven fact.

## Originality and attribution

This implementation uses an independently designed evidence model, scoring method, terminology, and report structure. The broad idea of analyzing job descriptions is common. A prior open-source project reviewed during research is credited in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); its text, examples, and code are not included here.
