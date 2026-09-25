# Motion design

Use motion selectively. The expressive mode may use a slow layered color field in the hero, a subtle light pass through the name, section entrance transitions, and hover/focus responses. The professional mode should keep only small interaction feedback unless the user asks otherwise.

Rules that preserve usability:

- Keep text on a stable surface. Background color movement belongs behind a dark overlay or otherwise high-contrast text.
- Animate transforms and opacity for ordinary entrances. Avoid continuously animating layout, large shadows, filters, or document height.
- Reveal content progressively only as enhancement: it must remain visible when JavaScript is off or fails.
- Never make a visitor wait through an intro screen to read the resume. Avoid autoplay audio, rapid flashes, and cursor effects that cover controls.
- Respect `prefers-reduced-motion: reduce`; freeze ambient animation and remove entrance travel. Pause or simplify effects on small screens and when the page is hidden.
- Keep keyboard focus visible, including on animated cards and navigation. Hover must not be the only way to discover a link.
- Disable decorative motion and dark backgrounds in print styles.

The [starter](../assets/starter/) shows CSS-only ambient color, a small `IntersectionObserver` reveal, and a scroll progress line. Adapt it to the person's visual identity rather than using its palette automatically. If a Canvas/WebGL effect is genuinely necessary, provide a static fallback and verify performance on a low-power mobile viewport.
