---
name: resume-site-studio
description: 分析目标职位与真实职业证据，把简历、履历或职业资料制作成可编辑的个人网站或作品集，并可加入适度动态效果。适用于职位匹配、简历与岗位差距分析、简历网站、职业主页、学术主页和作品集；不用于只编辑 DOCX 或 PDF 简历。Analyze job fit against real career evidence and build an editable resume website or portfolio when users request these tasks.
---

# 简历网站工坊 · Resume Site Studio

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

- Before coding, write one private design-read sentence covering the page type, audience, visual language, and intended density. For a recruiter-facing resume site, optimize the first 20 seconds of scanning: identity, target direction, strongest evidence, then detail.
- Create a real homepage: a precise identity statement, one clear action when a real destination exists, selected proof, and a path to deeper work. Organize by relevance to the site's goal rather than copying resume section order.
- Treat "clean" and "professional" as a premium professional direction, not a bare document page. For a light, concise, or professional request, start from [assets/templates/professional-light](assets/templates/professional-light/) and replace every fictional fact. Preserve its immersive hero, layered light, evidence panel, varied section rhythm, restrained motion, type scale, and responsive behavior unless the brief calls for a materially different direction. Never copy its demo facts into a real site.
- Use [assets/starter](assets/starter/) for expressive or dark directions. Its fictional content is a demo, not user content.
- Offer two presentation modes when the user has no visual preference: **professional** (quiet, content-first) and **expressive** (dark cinematic hero with restrained motion). A supplied reference takes priority. Capture its visual principles without copying proprietary source, logos, media, or distinctive assets.
- Avoid the common document-like output: a full-width colored banner followed by identical rounded white cards, oversized paragraphs, and repeated bullet lists. Use no more than one dominant card surface in the first viewport. Build hierarchy through typography, whitespace, rules, asymmetric grids, and evidence-led numbers.
- The first viewport must show the person's name or identity, target direction, a short positioning statement, and two to four verified proof points. Do not make navigation the main visual feature. Do not add a button without a real anchor or approved destination.
- Use at least three distinct section compositions across the page, such as a split hero, evidence strip, timeline, editorial list, capability grid, or education band. Repeated cards do not count as distinct compositions.
- Match the production ambition of the bundled showcase: subtle background atmosphere, one memorable visual device tied to the person's work, responsive hover or scroll feedback, and a composed mobile version. Decorative effects must remain secondary to verified evidence.
- Keep the profile readable with JavaScript disabled. Use semantic HTML and meaningful link labels. Make all important content and actions keyboard accessible.
- Read [references/motion.md](references/motion.md) when using animation. Motion should help the visitor understand hierarchy or interaction. Do not apply every available effect by default.
- Treat mobile, reduced-motion, and print as first-class outputs. Motion and background effects must never obscure the name, positioning, projects, or contact action.

## Build and verify

1. Produce a static site whose public root contains `index.html`, CSS, optional small JavaScript, and licensed assets. Keep editable content in an obvious file or a clearly documented section of HTML. Avoid dependencies unless the requested interaction needs them.
2. Use project cards to show the person's role, the problem, what they did, and an evidenced result or artifact. If a claim lacks proof, omit or soften it and record the gap in the private notes.
3. Run [references/quality-check.md](references/quality-check.md). When a browser is available, capture the full first viewport at desktop and phone widths, compare it with the chosen bundled template, and fix weak hierarchy, excess card framing, overflow, broken links, motion problems, and unreadable contrast. If browser control is unavailable, run static checks and explicitly report visual checks as unverified. Check that print/PDF output is usable if offered.
4. Give the user a local preview path and a brief account of content decisions, unresolved facts, and asset credits. A request to create the site does not by itself authorize pushing a repository or making personal information public. Prepare a reviewable public directory before asking for publication approval.

## Reference origin

This skill adapts ideas from [personal-site-builder](https://github.com/SpaceZephyr/personal-site-builder) and [Resume2Site-Skill](https://github.com/Bearcoder6/Resume2Site-Skill), both MIT licensed. The starter code here is newly written. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) when publishing this skill or incorporating source from those projects.
