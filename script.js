/* ---------- Year ---------- */
document.querySelectorAll('.year').forEach(el => { el.textContent = new Date().getFullYear(); });

/* ---------- Mobile nav ---------- */
const burger = document.getElementById('burger');
const mobileNav = document.getElementById('mobileNav');
if (burger && mobileNav) {
  burger.addEventListener('click', () => {
    mobileNav.classList.toggle('open');
    burger.classList.toggle('active');
  });
  document.querySelectorAll('.mobile-nav a').forEach(a =>
    a.addEventListener('click', () => mobileNav.classList.remove('open'))
  );
}

/* ---------- Particle background ---------- */
const canvas = document.getElementById('particle-canvas');
if (canvas) {
  const ctx = canvas.getContext('2d');
  let particles = [];
  let w, h;

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = document.body.scrollHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  function makeParticles() {
    const count = Math.min(70, Math.floor(w / 22));
    particles = Array.from({ length: count }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 1.6 + 0.4,
      vy: -(Math.random() * 0.25 + 0.05),
      vx: (Math.random() - 0.5) * 0.15,
      hue: Math.random() > 0.5 ? '44,243,240' : '179,85,255',
      alpha: Math.random() * 0.5 + 0.15,
    }));
  }
  makeParticles();
  window.addEventListener('resize', makeParticles);

  function tick() {
    ctx.clearRect(0, 0, w, h);
    particles.forEach(p => {
      p.y += p.vy;
      p.x += p.vx;
      if (p.y < -10) { p.y = h + 10; p.x = Math.random() * w; }
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${p.hue},${p.alpha})`;
      ctx.shadowColor = `rgba(${p.hue},0.8)`;
      ctx.shadowBlur = 6;
      ctx.fill();
    });
    requestAnimationFrame(tick);
  }
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    tick();
  }
}

/* ---------- Click-pulse for member/leader/team cards ---------- */
function attachPulse(card) {
  const pulse = () => {
    card.classList.remove('pulse');
    void card.offsetWidth; // restart animation
    card.classList.add('pulse');
  };
  card.addEventListener('click', pulse);
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pulse(); }
  });
}
document.querySelectorAll('.leader-card, .member-card, .team-card').forEach(attachPulse);
