# Release check for a resume website

Verify the built site, rather than only checking that files exist.

1. **Facts:** Compare public names, titles, dates, metrics, project roles, and contact links against the source profile. Record unresolved claims privately. No fictional starter facts remain.
2. **Privacy and rights:** Public output contains no raw resume, private working profile, phone number or address without approval, hidden personal data, copied reference media, or unlicensed image/font. Keep credits for used third-party assets.
3. **Interaction:** Every visible link has a real destination or is removed. Keyboard navigation and focus states work. Essential content is visible without JavaScript.
4. **Visual:** Inspect at desktop width and a narrow phone width. Look for overflow, clipping, awkward line breaks, low contrast, and broken imagery. Motion must not obscure content.
5. **Alternatives:** Check `prefers-reduced-motion`, a paused/background tab when relevant, and print preview when PDF export is promised.
6. **Delivery:** Open `index.html` locally. If the user requested deployment, inspect the exact public directory and destination before publishing. Verify the resulting public URL after authorization and deployment.

The checks scale to the site. Use existing project checks if present. Do not add a large test framework merely to verify a static page.
