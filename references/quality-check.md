# Release check for a resume website

Verify the built site, rather than only checking that files exist.

1. **Facts:** Compare public names, titles, dates, metrics, project roles, and contact links against the source profile. Record unresolved claims privately. No fictional starter facts remain.
2. **Privacy and rights:** Public output contains no raw resume, private working profile, phone number or address without approval, hidden personal data, copied reference media, or unlicensed image/font. Keep credits for used third-party assets.
3. **Interaction:** Every visible link has a real destination or is removed. Keyboard navigation and focus states work. Essential content is visible without JavaScript.
4. **Visual hierarchy:** Inspect the complete first viewport at desktop width. It must show identity, target direction, a concise positioning statement, and two to four verified proof points. Navigation must not dominate. Reject a document-like page made from a colored banner followed by repeated identical white cards.
5. **Composition:** Use at least three visibly different section layouts. Prefer typography, whitespace, rules, and grids over wrapping every section in a rounded card. In the first viewport, allow at most one dominant card surface.
6. **Showcase quality:** A professional brief still needs authored visual identity. Confirm the page has subtle atmosphere, one memorable work-relevant visual device, responsive hover or scroll feedback, and a deliberate mobile composition. If it resembles a styled Word document, redesign it.
7. **Responsive:** Inspect at a narrow phone width. Look for overflow, clipping, awkward line breaks, tiny proof labels, horizontal navigation collisions, and broken imagery. Motion must not obscure content.
8. **Alternatives:** Check `prefers-reduced-motion`, a paused/background tab when relevant, and print preview when PDF export is promised.
9. **Delivery:** Open `index.html` locally. If the user requested deployment, inspect the exact public directory and destination before publishing. Verify the resulting public URL after authorization and deployment.

The checks scale to the site. Use existing project checks if present. Do not add a large test framework merely to verify a static page.
