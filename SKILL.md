---
name: resume-site-studio
description: Analyze a target job against real career evidence and turn a resume, CV, or career history into an editable personal website or portfolio with optional motion. Use for job-fit analysis, resume-to-job gap analysis, resume websites, career homepages, academic profiles, or portfolios. Not for DOCX/PDF-only resume editing.
---

# Resume Site Studio

Analyze target roles when requested, then build a personal website that explains who the person is, what they have done, and how to contact them. Treat the resume as evidence, not as a page layout to copy. Deliver an editable, responsive static site that works locally before offering publication. This skill uses the portable `SKILL.md` format. Follow the host's available file, document, browser, and shell tools; no specific product or connector is required.

## Route the request

- For job-fit, job-description, hard-gate, or resume-gap analysis, read and follow [modules/job-fit-evidence-analyzer/SKILL.md](modules/job-fit-evidence-analyzer/SKILL.md). Deliver its evidence report even when no website is requested.
- For a targeted resume website, run the bundled analyzer first, then use only its verified evidence and priorities in the site.
- For a general resume website without a target role, continue directly with the intake and site workflow below.
- When the user asks for both analysis and a website, keep the private evidence report outside the public site directory.

## Intake and evidence

1. Read the provided DOCX, PDF, Markdown, text, links, images, and target role. Use available document or PDF tools when needed. Do not require the user to reorganize files.
2. Extract a private working profile before writing page copy. Use [references/content-model.md](references/content-model.md) for the fields and evidence rules. Distinguish source facts, reasonable summaries, and unanswered questions. Never invent dates, employers, credentials, testimonials, project results, or metrics.
3. When a target job description is supplied, follow the bundled `job-fit-evidence-analyzer` module before selecting site content. Use its verified evidence, priorities, hard-gate findings, and unresolved questions. Never promote an unverified or transferable claim into a proven fact.
4. Decide the site's primary goal from the material: job search, professional introduction, portfolio, or academic profile. Ask one focused question only when the goal or public contact details cannot be inferred. Make an initial draft with clearly marked omissions when information is incomplete.
5. Keep the source resume and the private working profile outside the public output directory. Phone numbers, private addresses, personal IDs, internal documents, and customer data are excluded unless the user explicitly requests their publication.

## Site design

- Create a real homepage: a precise identity statement, one clear action, selected proof, and a path to deeper work. Organize by relevance to the site's goal rather than copying resume section order.
- Use the starter in [assets/starter](assets/starter/) as optional editable reference code. Its fictional content is a demo, not user content. Do not copy sample facts into a real site.
- Offer two presentation modes when the user has no visual preference: **professional** (quiet, content-first) and **expressive** (dark cinematic hero with restrained motion). A supplied reference takes priority. Capture its visual principles without copying proprietary source, logos, media, or distinctive assets.
- Keep the profile readable with JavaScript disabled. Use semantic HTML and meaningful link labels. Make all important content and actions keyboard accessible.
- Read [references/motion.md](references/motion.md) when using animation. Motion should help the visitor understand hierarchy or interaction. Do not apply every available effect by default.
- Treat mobile, reduced-motion, and print as first-class outputs. Motion and background effects must never obscure the name, positioning, projects, or contact action.

## Build and verify

1. Produce a static site whose public root contains `index.html`, CSS, optional small JavaScript, and licensed assets. Keep editable content in an obvious file or a clearly documented section of HTML. Avoid dependencies unless the requested interaction needs them.
2. Use project cards to show the person's role, the problem, what they did, and an evidenced result or artifact. If a claim lacks proof, omit or soften it and record the gap in the private notes.
3. Run [references/quality-check.md](references/quality-check.md). When a browser is available, open the result at desktop and mobile widths; fix overflow, broken links, motion problems, and unreadable contrast. If browser control is unavailable, run static checks and explicitly report visual checks as unverified. Check that print/PDF output is usable if offered.
4. Give the user a local preview path and a brief account of content decisions, unresolved facts, and asset credits. A request to create the site does not by itself authorize pushing a repository or making personal information public. Prepare a reviewable public directory before asking for publication approval.

## Reference origin

This skill adapts ideas from [personal-site-builder](https://github.com/SpaceZephyr/personal-site-builder) and [Resume2Site-Skill](https://github.com/Bearcoder6/Resume2Site-Skill), both MIT licensed. The starter code here is newly written. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) when publishing this skill or incorporating source from those projects.
