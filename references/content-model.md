# Content and evidence model

Use a private `work/profile.json` or equivalent notes. The site can use plain HTML, but its facts should be traceable while drafting.

```json
{
  "identity": {"name": "", "role": "", "location": "", "summary": ""},
  "goal": "job-search | introduction | portfolio | academic",
  "target_role": {
    "title": "",
    "organization": "",
    "verified_priorities": [],
    "evidence_report": "optional private path",
    "unresolved_questions": []
  },
  "public_contact": [{"label": "", "url": "", "approved": false}],
  "experience": [{"organization": "", "role": "", "period": "", "highlights": []}],
  "projects": [{"name": "", "role": "", "problem": "", "actions": [], "results": [], "links": []}],
  "education": [],
  "skills": [],
  "sources": [{"id": "", "file_or_url": "", "note": ""}],
  "open_questions": []
}
```

For any metric or unusually strong claim, keep a source ID in private notes. A source can be the user's own statement; say so. Do not turn a team result into an individual achievement. Do not transfer a number from one project to another. Ask for missing context when it changes the public claim.

When a target role is present, choose homepage proof from verified core requirements first. Transferable evidence may be described as adjacent experience when the connection is explicit. `not_shown`, `missing`, and `unknown` items stay out of public claims until resolved.

Writing order: identify the person and intended reader; select two to four strongest pieces of evidence; write a specific opening; then add chronology and supporting skills. A small site with honest proof is better than a large site full of placeholders.

Before publishing, review every field that might expose private information. A public email address or social link may be used only when the user supplied it for this purpose or approved it. Keep source resumes, extracted text, draft profiles, and private notes out of the public directory and Git staging area.
