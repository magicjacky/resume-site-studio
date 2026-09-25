(() => {
  const root = document.documentElement;
  const button = document.querySelector('.mode-toggle');
  const label = button?.querySelector('.mode-label');

  button?.addEventListener('click', () => {
    const expressive = root.dataset.mode !== 'expressive';
    root.dataset.mode = expressive ? 'expressive' : 'professional';
    button.setAttribute('aria-pressed', String(expressive));
    if (label) label.textContent = expressive ? '动态模式' : '专业模式';
  });

  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const targets = [...document.querySelectorAll('.reveal')];
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    }
  }, { threshold: 0.08, rootMargin: '0px 0px 40px 0px' });
  targets.forEach((target) => observer.observe(target));
  root.classList.add('motion-ready');
})();
