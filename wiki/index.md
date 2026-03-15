<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

:root {
  --bg-deep: #050508;
  --bg-surface: rgba(255,255,255,0.03);
  --glass: rgba(255,255,255,0.08);
  --glass-border: rgba(255,255,255,0.08);
  --glass-hover: rgba(255,255,255,0.14);
  --text-primary: #f0f0f5;
  --text-secondary: rgba(240,240,245,0.85);
  --text-dim: rgba(240,240,245,0.6);
  --accent-qs: #6366f1;
  --accent-cs: #f59e0b;
  --accent-ps: #10b981;
  --accent-hot: #f43f5e;
  --glow-qs: rgba(99,102,241,0.4);
  --glow-cs: rgba(245,158,11,0.4);
  --glow-ps: rgba(16,185,129,0.4);
}

/* Override MkDocs Material container */
.md-content__inner { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
.md-typeset { font-size: 1rem; }
.md-typeset h1, .md-typeset h2, .md-typeset h3 { font-family: 'Outfit', sans-serif; letter-spacing: -0.02em; }
.md-sidebar { display: none !important; }
.md-content { max-width: 100% !important; }
.print-btn-bar { display: none !important; }


/* ─── LIGHT MODE OVERRIDES ─── */
[data-md-color-scheme="default"] .rtsg-landing {
  --bg-deep: #ffffff;
  --bg-surface: rgba(0,0,0,0.02);
  --glass: rgba(0,0,0,0.04);
  --glass-border: rgba(0,0,0,0.1);
  --glass-hover: rgba(0,0,0,0.07);
  --text-primary: #1a1a2e;
  --text-secondary: rgba(26,26,46,0.75);
  --text-dim: rgba(26,26,46,0.5);
}

[data-md-color-scheme="default"] .rtsg-hero h1 {
  background: linear-gradient(135deg, #1a1a2e 0%, rgba(26,26,46,0.8) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

[data-md-color-scheme="default"] .rtsg-hero-sub {
  color: rgba(26,26,46,0.8) !important;
}

[data-md-color-scheme="default"] .rtsg-hero-sub strong {
  color: #1a1a2e !important;
}

[data-md-color-scheme="default"] .rtsg-hero-badge {
  color: #1a1a2e !important;
  border-color: rgba(0,0,0,0.15) !important;
  background: rgba(0,0,0,0.05) !important;
}

[data-md-color-scheme="default"] .rtsg-space-label .name {
  color: #1a1a2e !important;
}

[data-md-color-scheme="default"] .rtsg-space-label .desc {
  color: rgba(26,26,46,0.65) !important;
}

[data-md-color-scheme="default"] .rtsg-stat-value {
  color: #1a1a2e !important;
}

[data-md-color-scheme="default"] .rtsg-stat-label {
  color: rgba(26,26,46,0.6) !important;
}

[data-md-color-scheme="default"] .rtsg-card {
  background: rgba(0,0,0,0.03) !important;
  border-color: rgba(0,0,0,0.1) !important;
}

[data-md-color-scheme="default"] .rtsg-card:hover {
  background: rgba(0,0,0,0.06) !important;
  box-shadow: 0 16px 48px rgba(0,0,0,0.08) !important;
}

[data-md-color-scheme="default"] .rtsg-card h3 {
  color: #1a1a2e !important;
}

[data-md-color-scheme="default"] .rtsg-card p {
  color: rgba(26,26,46,0.8) !important;
}

[data-md-color-scheme="default"] .rtsg-section-header h2 {
  color: #1a1a2e !important;
}

[data-md-color-scheme="default"] .rtsg-section-header p {
  color: rgba(26,26,46,0.75) !important;
}

[data-md-color-scheme="default"] .rtsg-equation-banner .eq {
  color: rgba(26,26,46,0.85) !important;
}

[data-md-color-scheme="default"] .rtsg-equation-banner .eq strong {
  color: #d97706 !important;
}

[data-md-color-scheme="default"] .rtsg-divider {
  background: linear-gradient(90deg, transparent, rgba(0,0,0,0.1), transparent) !important;
}

[data-md-color-scheme="default"] .rtsg-btn--glass {
  background: rgba(0,0,0,0.05) !important;
  color: #1a1a2e !important;
  border-color: rgba(0,0,0,0.15) !important;
}

[data-md-color-scheme="default"] .rtsg-btn--glass:hover {
  background: rgba(0,0,0,0.08) !important;
}

[data-md-color-scheme="default"] .rtsg-footer {
  color: rgba(26,26,46,0.5) !important;
}

[data-md-color-scheme="default"] .rtsg-footer a {
  color: rgba(26,26,46,0.65) !important;
}

[data-md-color-scheme="default"] .rtsg-card::before {
  background: linear-gradient(90deg, transparent, rgba(0,0,0,0.06), transparent) !important;
}

[data-md-color-scheme="default"] .rtsg-hero canvas {
  opacity: 0.3;
}


.rtsg-landing {
  font-family: 'Outfit', sans-serif;
  color: var(--text-primary);
  overflow-x: hidden;
}

/* ─── HERO ─── */
.rtsg-hero {
  position: relative;
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  overflow: hidden;
}

.rtsg-hero canvas {
  position: absolute !important;
  top: 0; left: 0;
  width: 100% !important;
  height: 100% !important;
  z-index: 0;
}

.rtsg-hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
}

.rtsg-hero-badge {
  display: inline-block;
  padding: 6px 16px;
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #f0f0f5;
  backdrop-filter: blur(20px);
  background: rgba(255,255,255,0.1);
  margin-bottom: 2rem;
  animation: fadeInUp 1s ease 0.2s both;
}

.rtsg-hero h1 {
  font-size: clamp(3.5rem, 10vw, 7rem);
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 0.95;
  margin: 0 0 1.5rem 0;
  animation: fadeInUp 1s ease 0.4s both;
  background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.7) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.rtsg-hero-sub {
  font-size: clamp(1rem, 2.5vw, 1.35rem);
  font-weight: 400;
  color: rgba(240,240,245,0.92);
  line-height: 1.6;
  margin-bottom: 3rem;
  animation: fadeInUp 1s ease 0.6s both;
}

.rtsg-hero-sub strong {
  color: var(--text-primary);
  font-weight: 500;
}

/* ─── SPACE LABELS floating ─── */
.rtsg-space-labels {
  display: flex;
  gap: 3rem;
  justify-content: center;
  margin-bottom: 3rem;
  animation: fadeInUp 1s ease 0.8s both;
}

.rtsg-space-label {
  text-align: center;
}

.rtsg-space-label .orb {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  margin: 0 auto 8px;
  box-shadow: 0 0 20px var(--glow);
}

.rtsg-space-label .orb--qs { background: var(--accent-qs); --glow: var(--glow-qs); }
.rtsg-space-label .orb--cs { background: var(--accent-cs); --glow: var(--glow-cs); }
.rtsg-space-label .orb--ps { background: var(--accent-ps); --glow: var(--glow-ps); }

.rtsg-space-label .name {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #f0f0f5;
}

.rtsg-space-label .desc {
  font-size: 0.7rem;
  color: rgba(240,240,245,0.75);
  font-weight: 400;
}

/* ─── BUTTONS ─── */
.rtsg-hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  animation: fadeInUp 1s ease 1s both;
}

.rtsg-btn {
  padding: 14px 32px;
  border-radius: 12px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
  text-decoration: none !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  border: none;
}

.rtsg-btn--primary {
  background: linear-gradient(135deg, var(--accent-cs), #e88c0a);
  color: #000 !important;
  box-shadow: 0 4px 24px rgba(245,158,11,0.3);
}

.rtsg-btn--primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(245,158,11,0.5);
}

.rtsg-btn--glass {
  background: var(--glass);
  color: var(--text-primary) !important;
  border: 1px solid var(--glass-border);
  backdrop-filter: blur(20px);
}

.rtsg-btn--glass:hover {
  background: var(--glass-hover);
  border-color: rgba(255,255,255,0.15);
  transform: translateY(-2px);
}

/* ─── STATS BAR ─── */
.rtsg-stats {
  display: flex;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
  animation: fadeInUp 1s ease 1.2s both;
}

.rtsg-stat {
  text-align: center;
}

.rtsg-stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #f0f0f5;
}

.rtsg-stat-label {
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: rgba(240,240,245,0.7);
  font-weight: 500;
  margin-top: 4px;
}

/* ─── SECTION ─── */
.rtsg-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
}

.rtsg-section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.rtsg-section-header h2 {
  font-size: 2rem;
  font-weight: 700;
  margin: 0 0 0.75rem 0;
}

.rtsg-section-header p {
  color: rgba(240,240,245,0.85);
  font-weight: 400;
  max-width: 600px;
  margin: 0 auto;
}

/* ─── GLASS CARDS ─── */
.rtsg-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.25rem;
}

.rtsg-card {
  background: var(--glass);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  padding: 2rem;
  backdrop-filter: blur(20px);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none !important;
  display: block;
  position: relative;
  overflow: hidden;
}

.rtsg-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
}

.rtsg-card:hover {
  background: var(--glass-hover);
  border-color: rgba(255,255,255,0.12);
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(0,0,0,0.3);
}

.rtsg-card-icon {
  font-size: 1.75rem;
  margin-bottom: 1rem;
  display: block;
}

.rtsg-card h3 {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 0.5rem 0;
  color: var(--text-primary) !important;
}

.rtsg-card p {
  font-size: 0.85rem;
  color: rgba(240,240,245,0.9);
  line-height: 1.6;
  margin: 0;
  font-weight: 400;
}

.rtsg-card .rtsg-tag {
  display: inline-block;
  margin-top: 1rem;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.rtsg-tag--live { background: rgba(16,185,129,0.15); color: var(--accent-ps); }
.rtsg-tag--ready { background: rgba(99,102,241,0.15); color: var(--accent-qs); }
.rtsg-tag--urgent { background: rgba(244,63,94,0.15); color: var(--accent-hot); }
.rtsg-tag--new { background: rgba(245,158,11,0.15); color: var(--accent-cs); }

/* ─── EQUATION BANNER ─── */
.rtsg-equation-banner {
  text-align: center;
  padding: 4rem 2rem;
  position: relative;
}

.rtsg-equation-banner .eq {
  font-family: 'JetBrains Mono', monospace;
  font-size: clamp(1rem, 3vw, 1.5rem);
  font-weight: 400;
  color: rgba(240,240,245,0.9);
  letter-spacing: 0.02em;
}

.rtsg-equation-banner .eq strong {
  color: var(--accent-cs);
  font-weight: 500;
}

/* ─── DIVIDER ─── */
.rtsg-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--glass-border), transparent);
  max-width: 1200px;
  margin: 0 auto;
}

/* ─── FOOTER ─── */
.rtsg-footer {
  text-align: center;
  padding: 3rem 2rem;
  color: rgba(240,240,245,0.65);
  font-size: 0.8rem;
  font-weight: 400;
}

.rtsg-footer a {
  color: var(--text-secondary) !important;
  text-decoration: none;
}

/* ─── ANIMATIONS ─── */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ─── RESPONSIVE ─── */
@media (max-width: 768px) {
  .rtsg-stats { gap: 1.5rem; flex-wrap: wrap; }
  .rtsg-space-labels { gap: 1.5rem; }
  .rtsg-grid { grid-template-columns: 1fr; }
}
</style>

<div class="rtsg-landing" markdown="0">

<div class="rtsg-hero">
  <canvas id="rtsg-three-canvas"></canvas>
  <div class="rtsg-hero-content">
    <div class="rtsg-hero-badge">Relational Three-Space Geometry</div>
    <h1>RTSG</h1>
    <p class="rtsg-hero-sub">
      A unified framework spanning <strong>physics, consciousness, mathematics, and intelligence</strong> — built on three co-primordial spaces, one action principle, and the insight that <strong>you can get smarter and see your walls</strong>.
    </p>
    <div class="rtsg-space-labels">
      <div class="rtsg-space-label">
        <div class="orb orb--qs"></div>
        <div class="name">QS</div>
        <div class="desc">Potentiality</div>
      </div>
      <div class="rtsg-space-label">
        <div class="orb orb--cs"></div>
        <div class="name">CS</div>
        <div class="desc">Instantiation</div>
      </div>
      <div class="rtsg-space-label">
        <div class="orb orb--ps"></div>
        <div class="name">PS</div>
        <div class="desc">Actuality</div>
      </div>
    </div>
    <div class="rtsg-hero-actions">
      <a href="rtsg/definitions/" class="rtsg-btn rtsg-btn--primary">Start Here</a>
      <a href="rtsg/master/" class="rtsg-btn rtsg-btn--glass">Master Reference</a>
      <a href="rtsg/therapeutic/" class="rtsg-btn rtsg-btn--glass">Heal</a>
    </div>
  </div>
</div>

<div class="rtsg-stats">
  <div class="rtsg-stat">
    <div class="rtsg-stat-value">171</div>
    <div class="rtsg-stat-label">Wiki Pages</div>
  </div>
  <div class="rtsg-stat">
    <div class="rtsg-stat-value">12</div>
    <div class="rtsg-stat-label">Disciplines</div>
  </div>
  <div class="rtsg-stat">
    <div class="rtsg-stat-value">17</div>
    <div class="rtsg-stat-label">Open Problems</div>
  </div>
  <div class="rtsg-stat">
    <div class="rtsg-stat-value">4</div>
    <div class="rtsg-stat-label">Operators</div>
  </div>
</div>

<div class="rtsg-divider"></div>

<div class="rtsg-equation-banner">
  <div class="eq"><strong>U = Value / (Energy × Time)</strong> — Niko's Cannon</div>
</div>

<div class="rtsg-divider"></div>

<div class="rtsg-section">
  <div class="rtsg-section-header">
    <h2>Explore the Framework</h2>
    <p>Three spaces. One action principle. Everything connects.</p>
  </div>
  <div class="rtsg-grid">
    <a href="rtsg/definitions/" class="rtsg-card">
      <span class="rtsg-card-icon">★</span>
      <h3>Definitions & Novel Concepts</h3>
      <p>Complete glossary of all RTSG terms, every core equation, and the full inventory of novel contributions. Start here.</p>
      <span class="rtsg-tag rtsg-tag--new">Start Here</span>
    </a>
    <a href="rtsg/therapeutic/" class="rtsg-card">
      <span class="rtsg-card-icon">🌱</span>
      <h3>Therapeutic Framework</h3>
      <p>You are not broken — you are adapted to a broken environment. RTSG as a healing tool for trauma survivors, therapists, and anyone seeking self-understanding.</p>
      <span class="rtsg-tag rtsg-tag--new">New</span>
    </a>
    <a href="rtsg/action_principle/" class="rtsg-card">
      <span class="rtsg-card-icon">💥</span>
      <h3>Niko's Cannon</h3>
      <p>U = V/(E×T) replaces Occam's Razor. The razor cuts away. The cannon blasts through. The master selection principle for all decisions.</p>
      <span class="rtsg-tag rtsg-tag--new">New</span>
    </a>
    <a href="rtsg/master/" class="rtsg-card">
      <span class="rtsg-card-icon">📐</span>
      <h3>RTSG Master Reference</h3>
      <p>The complete theory: three spaces, GL action, BRST cohomology, bisimulation quotienting, Will Field dynamics, intelligence geometry.</p>
    </a>
    <a href="rtsg/graded_brst/" class="rtsg-card">
      <span class="rtsg-card-icon">⚛️</span>
      <h3>Graded BRST Decomposition</h3>
      <p>Dark matter = states that pass the gravitational filter but fail the electromagnetic one. The instantiation cascade formalized.</p>
      <span class="rtsg-tag rtsg-tag--new">New</span>
    </a>
    <a href="rtsg/cs_mechanics/" class="rtsg-card">
      <span class="rtsg-card-icon">∞</span>
      <h3>CS Mechanics</h3>
      <p>The missing third mechanics. PS has Hamilton. QS has Schrödinger. CS has Maurer-Cartan. Three-Space Mechanics unified.</p>
      <span class="rtsg-tag rtsg-tag--new">New</span>
    </a>
    <a href="problems/open/" class="rtsg-card">
      <span class="rtsg-card-icon">🎯</span>
      <h3>Open Problems</h3>
      <p>Riemann Hypothesis, Yang-Mills mass gap, consciousness, dark matter — ranked by Niko's Cannon. Confidence scores. Honest gaps.</p>
    </a>
    <a href="papers/grf/mss_horizon/" class="rtsg-card">
      <span class="rtsg-card-icon">📄</span>
      <h3>GRF 2026 Essay</h3>
      <p>One Rate at the Horizon — submission-ready. Five adversarial rounds across three frontier AI models. $4K prize.</p>
      <span class="rtsg-tag rtsg-tag--urgent">Deadline Mar 31</span>
    </a>
    <a href="qrnsp/" class="rtsg-card">
      <span class="rtsg-card-icon">🛡️</span>
      <h3>QR-NSP</h3>
      <p>Quantum-resistant censorship evasion. 8 modules, 9,593 LOC pure C. For people under authoritarian regimes who need to communicate freely.</p>
      <span class="rtsg-tag rtsg-tag--live">AGPL-3.0</span>
    </a>

  </div>
</div>

<div class="rtsg-divider"></div>

<div class="rtsg-section">
  <div class="rtsg-section-header">
    <h2>The Three Co-Primordial Spaces</h2>
    <p>All arise simultaneously. None reduces to any other.</p>
  </div>
  <div class="rtsg-grid" style="grid-template-columns: repeat(3, 1fr);">
    <div class="rtsg-card" style="border-color: rgba(99,102,241,0.2);">
      <h3 style="color: var(--accent-qs) !important;">Quantum Space</h3>
      <p>Pure potentiality. Terminal coalgebra of the powerset functor. Non-well-founded. Pre-geometric. The math: Schrödinger.</p>
    </div>
    <div class="rtsg-card" style="border-color: rgba(245,158,11,0.2);">
      <h3 style="color: var(--accent-cs) !important;">Instantiation Operator</h3>
      <p>BRST cohomological filter. Converts QS → PS. Self-referential. CS is math itself. The math: Maurer-Cartan.</p>
    </div>
    <div class="rtsg-card" style="border-color: rgba(16,185,129,0.2);">
      <h3 style="color: var(--accent-ps) !important;">Physical Space</h3>
      <p>Accumulated actuality. Bisimulation quotient of QS. Metric. Classical. The math: Hamilton.</p>
    </div>
  </div>
</div>

<div class="rtsg-divider"></div>

<div class="rtsg-section">
  <div class="rtsg-section-header">
    <h2>Try It Live</h2>
    <p>RTSG is not just theory. It runs.</p>
  </div>
  <div class="rtsg-grid" style="grid-template-columns: repeat(3, 1fr);">
    <a href="engine/dashboard/" class="rtsg-card">
      <span class="rtsg-card-icon">⚡</span>
      <h3>Intelligence Engine</h3>
      <p>Live dashboard. Play chess against a knowledge graph. Explore 2,400+ concepts and 6,700+ relations. Watch the priority queue think.</p>
      <span class="rtsg-tag rtsg-tag--live">Live</span>
    </a>
    <a href="qrnsp/nike/" class="rtsg-card">
      <span class="rtsg-card-icon">👟</span>
      <h3>Sneakernet</h3>
      <p>Uncensorable messaging hidden inside this wiki. No app. No trace. Post-quantum. Deniable. For people who need to speak freely.</p>
      <span class="rtsg-tag rtsg-tag--live">Live</span>
    </a>
    <a href="meta/visual_guide/" class="rtsg-card">
      <span class="rtsg-card-icon">📖</span>
      <h3>Visual Guide</h3>
      <p>Full-color PDF. Every concept three ways: visual, algebraic, conversational. Free download. Print it. Share it.</p>
      <span class="rtsg-tag rtsg-tag--new">Free PDF</span>
    </a>
  </div>
</div>

<div class="rtsg-divider"></div>

<div class="rtsg-section">
  <div class="rtsg-section-header">
    <h2>For Everyone</h2>
  </div>
  <div class="rtsg-grid" style="grid-template-columns: repeat(2, 1fr);">
    <a href="rtsg/therapeutic/" class="rtsg-card">
      <h3>For Humans</h3>
      <p>You can get smarter. You can see your walls. Your filters were smart — they kept you alive. Now you're somewhere safer. You can update.</p>
    </a>
    <a href="agents/start/" class="rtsg-card">
      <h3>For AI Agents</h3>
      <p>Onboard into the research network. Load the wiki. Join the assembly. {@B_Niko, @D_Claude, @D_Gemini, @D_GPT}.</p>
    </a>
    <a href="papers/companions/psychiatry/" class="rtsg-card">
      <h3>For Clinicians</h3>
      <p>K-matrix spectral analysis. Filter decomposition. 15 testable hypotheses. Integrates with CBT, DBT, EMDR, IFS.</p>
    </a>
    <a href="rtsg/rtsg_index/" class="rtsg-card">
      <h3>For Researchers</h3>
      <p>Cross-reference index. Every concept, equation, theorem, and open problem — linked and searchable.</p>
    </a>
  </div>
</div>

<div class="rtsg-footer">
  <p>© 2026 <strong>Jean-Paul Niko</strong> — All rights reserved</p>
  <p style="margin-top: 0.5rem;">Sole author of RTSG. Built with {@B_Niko, @D_Claude, @D_Gemini, @D_GPT}.</p>
</div>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function() {
  const canvas = document.getElementById('rtsg-three-canvas');
  if (!canvas) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Three orbs: QS (indigo), CS (amber), PS (emerald)
  const colors = [0x6366f1, 0xf59e0b, 0x10b981];
  const positions = [[-3, 0, 0], [0, 0, 0], [3, 0, 0]];
  const orbs = [];

  colors.forEach((color, i) => {
    const geo = new THREE.SphereGeometry(0.6, 64, 64);
    const mat = new THREE.MeshPhysicalMaterial({
      color: color,
      transparent: true,
      opacity: 0.25,
      roughness: 0.1,
      metalness: 0.3,
      clearcoat: 1.0,
      clearcoatRoughness: 0.1,
      emissive: color,
      emissiveIntensity: 0.15
    });
    const mesh = new THREE.Mesh(geo, mat);
    mesh.position.set(...positions[i]);
    scene.add(mesh);
    orbs.push(mesh);

    // Wireframe shell
    const wireGeo = new THREE.SphereGeometry(0.75, 24, 24);
    const wireMat = new THREE.MeshBasicMaterial({ color: color, wireframe: true, transparent: true, opacity: 0.08 });
    const wire = new THREE.Mesh(wireGeo, wireMat);
    wire.position.set(...positions[i]);
    scene.add(wire);
    orbs.push(wire);
  });

  // Connection lines between orbs
  const lineMat = new THREE.LineBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.06 });
  for (let i = 0; i < 3; i++) {
    for (let j = i+1; j < 3; j++) {
      const geo = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(...positions[i]),
        new THREE.Vector3(...positions[j])
      ]);
      scene.add(new THREE.Line(geo, lineMat));
    }
  }

  // Particles
  const particleCount = 600;
  const particleGeo = new THREE.BufferGeometry();
  const particlePositions = new Float32Array(particleCount * 3);
  const particleColors = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount; i++) {
    particlePositions[i*3] = (Math.random() - 0.5) * 20;
    particlePositions[i*3+1] = (Math.random() - 0.5) * 20;
    particlePositions[i*3+2] = (Math.random() - 0.5) * 20;

    const c = new THREE.Color(colors[Math.floor(Math.random() * 3)]);
    particleColors[i*3] = c.r;
    particleColors[i*3+1] = c.g;
    particleColors[i*3+2] = c.b;
  }

  particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
  particleGeo.setAttribute('color', new THREE.BufferAttribute(particleColors, 3));
  const particleMat = new THREE.PointsMaterial({ size: 0.03, vertexColors: true, transparent: true, opacity: 0.5 });
  scene.add(new THREE.Points(particleGeo, particleMat));

  // Lighting
  scene.add(new THREE.AmbientLight(0xffffff, 0.3));
  const pointLight = new THREE.PointLight(0xf59e0b, 1, 20);
  pointLight.position.set(0, 3, 5);
  scene.add(pointLight);

  camera.position.z = 7;
  camera.position.y = 1;

  let t = 0;
  function animate() {
    requestAnimationFrame(animate);
    t += 0.005;

    // Gentle rotation
    orbs.forEach((orb, i) => {
      orb.rotation.y = t * (0.3 + i * 0.1);
      orb.rotation.x = Math.sin(t + i) * 0.1;
    });

    // Breathe the orbs
    for (let i = 0; i < 3; i++) {
      const s = 1 + Math.sin(t * 2 + i * 2.1) * 0.05;
      orbs[i*2].scale.set(s, s, s);
    }

    // Slow camera orbit
    camera.position.x = Math.sin(t * 0.3) * 1.5;
    camera.position.y = 0.5 + Math.sin(t * 0.2) * 0.5;
    camera.lookAt(0, 0, 0);

    // Rotate particles
    const pts = scene.children.find(c => c instanceof THREE.Points);
    if (pts) pts.rotation.y = t * 0.05;

    renderer.render(scene, camera);
  }

  animate();

  window.addEventListener('resize', () => {
    camera.aspect = canvas.clientWidth / canvas.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  });
})();
</script>
