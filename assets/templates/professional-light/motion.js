document.documentElement.classList.add("motion-ready");

const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const items = document.querySelectorAll(".reveal");
const progress = document.querySelector(".page-progress span");
const proofPanel = document.querySelector(".proof-panel");

const updateProgress = () => {
  const max = document.documentElement.scrollHeight - innerHeight;
  if (progress) progress.style.width = `${max > 0 ? Math.min(100, scrollY / max * 100) : 0}%`;
};
addEventListener("scroll", updateProgress, { passive: true });
updateProgress();

if (!reduced && proofPanel && matchMedia("(pointer: fine)").matches) {
  proofPanel.addEventListener("pointermove", (event) => {
    const box = proofPanel.getBoundingClientRect();
    const x = (event.clientX - box.left) / box.width - .5;
    const y = (event.clientY - box.top) / box.height - .5;
    proofPanel.style.transform = `perspective(1100px) rotateY(${x * 6}deg) rotateX(${y * -5}deg) translateY(-4px)`;
  });
  proofPanel.addEventListener("pointerleave", () => { proofPanel.style.transform = ""; });
}

if (reduced || !("IntersectionObserver" in window)) {
  items.forEach((item) => item.classList.add("is-visible"));
} else {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  items.forEach((item) => observer.observe(item));
}
