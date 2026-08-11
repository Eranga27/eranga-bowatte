import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Sentinel Access — AI-powered intelligent access control and personnel tracking system.">
<meta property="og:title" content="Sentinel Access — Eranga Bowatte">
<meta property="og:description" content="Identify. Authorize. Protect. An AI-powered intelligent access control and personnel tracking system engineered for high-security naval environments.">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0a0a0a">
<title>Sentinel Access — Eranga Bowatte</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Poppins:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<style>
  :root {
    --sentinel-accent: #ff3333;
    --sentinel-accent-dark: #b30000;
    --glass-bg: rgba(255, 51, 51, 0.03);
    --glass-border: rgba(255, 51, 51, 0.15);
  }

  body {
    background-color: #0a0a0a;
    color: #e0e0e0;
  }

  /* Cinematic parallax background — z-index:-1 keeps it behind ALL content naturally */
  #parallax-bg {
    position: fixed;
    top: -30%;
    left: 0;
    width: 100%;
    height: 160%;
    background-image: url('images/sentinalpage/BGDesign.png');
    background-size: cover;
    background-position: center top;
    will-change: transform;
    z-index: -1;
    pointer-events: none;
  }

  /* Dark overlay for text readability */
  #parallax-bg::after {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(10, 10, 10, 0.85);
  }

  .project-hero {
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 120px 5vw 60px;
    position: relative;
    z-index: 1;
  }

  .project-logo {
    width: 280px;
    margin-bottom: 36px;
    animation: fadeUp 1s ease forwards;
    filter: drop-shadow(0 0 25px rgba(255, 51, 51, 0.5));
  }

  .project-headline {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 24px;
    background: linear-gradient(90deg, #ffffff 30%, var(--sentinel-accent) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeUp 1s ease forwards 0.2s;
    opacity: 0;
  }

  .project-subheadline {
    font-size: clamp(1.05rem, 2vw, 1.25rem);
    max-width: 820px;
    margin: 0 auto 40px;
    color: #a0a0a0;
    line-height: 1.7;
    animation: fadeUp 1s ease forwards 0.4s;
    opacity: 0;
  }

  .launch-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 16px 36px;
    background: var(--sentinel-accent);
    color: #ffffff;
    font-family: 'Space Mono', monospace;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    border-radius: 4px;
    text-decoration: none;
    transition: all 0.3s ease;
    animation: fadeUp 1s ease forwards 0.6s;
    opacity: 0;
  }

  .launch-btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(255, 51, 51, 0.35);
  }

  .section-glass {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 16px;
    padding: 60px;
    margin-bottom: 40px;
  }

  .glass-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }

  .glass-grid-4 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 30px;
  }

  .glass-card {
    background: rgba(15, 15, 15, 0.7);
    border: 1px solid var(--glass-border);
    padding: 36px;
    border-radius: 12px;
    transition: transform 0.3s ease, border-color 0.3s ease;
  }

  .glass-card:hover {
    transform: translateY(-6px);
    border-color: rgba(255, 51, 51, 0.4);
  }

  .glass-card .card-icon {
    font-size: 2rem;
    margin-bottom: 16px;
    display: block;
  }

  .glass-card h3 {
    font-size: 1.3rem;
    color: #fff;
    margin-bottom: 14px;
  }

  .glass-card p {
    color: #a0a0a0;
    line-height: 1.65;
    font-size: 0.97rem;
  }

  .feature-row {
    display: flex;
    align-items: center;
    gap: 60px;
    margin-bottom: 80px;
  }

  .feature-row:nth-child(even) {
    flex-direction: row-reverse;
  }

  .feature-text { flex: 1; }

  .feature-text h3 {
    font-size: 1.9rem;
    color: #fff;
    margin-bottom: 18px;
  }

  .feature-text p {
    color: #a0a0a0;
    line-height: 1.75;
    font-size: 1.05rem;
    margin-bottom: 14px;
  }

  .feature-image {
    flex: 1.2;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--glass-border);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
  }

  .feature-image img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.5s ease;
  }

  .feature-image:hover img { transform: scale(1.03); }

  .section-title {
    font-size: 2.4rem;
    color: #fff;
    margin-bottom: 40px;
    text-align: center;
  }

  .section-subtitle {
    text-align: center;
    color: var(--sentinel-accent);
    font-family: 'Space Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.85rem;
    margin-bottom: 14px;
  }

  .tech-pill {
    display: inline-block;
    padding: 9px 18px;
    background: rgba(255, 51, 51, 0.08);
    color: var(--sentinel-accent);
    border: 1px solid rgba(255, 51, 51, 0.2);
    border-radius: 30px;
    margin: 5px;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
  }
  
  .tech-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    font-size: 0.95rem;
  }
  
  .tech-table th, .tech-table td {
    padding: 12px 15px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    text-align: left;
  }
  
  .tech-table th {
    color: #fff;
    font-weight: 600;
  }
  
  .tech-table td {
    color: #a0a0a0;
  }
  
  .tech-table tr:last-child td {
    border-bottom: none;
  }

  .full-width-screenshot {
    max-width: 100%;
    border-radius: 12px;
    border: 1px solid var(--glass-border);
    box-shadow: 0 24px 50px rgba(0, 0, 0, 0.6);
    cursor: pointer;
    transition: transform 0.3s ease;
  }

  .full-width-screenshot:hover { transform: scale(1.01); }

  @media (max-width: 900px) {
    .glass-grid-2 { grid-template-columns: 1fr; }
    .feature-row, .feature-row:nth-child(even) { flex-direction: column; gap: 30px; }
    .section-glass { padding: 28px; }
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>

<!-- Cinematic parallax background -->
<div id="parallax-bg"></div>

<!-- Custom Cursor -->
<div class="cursor-dot" id="cursorDot"></div>
<div class="cursor-ring" id="cursorRing"></div>

<!-- PRELOADER -->
<div id="preloader" class="preloader">
  <div class="preloader-content">
    <h1 class="signature-text"><span class="flare"></span>Eranga Bowatte</h1>
  </div>
</div>

<!-- NAV -->
<nav style="background: rgba(10,10,10,0.85); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(255,51,51,0.08);">
  <button class="nav-toggle" id="navToggle" aria-label="Open menu">
    <span></span><span></span><span></span>
  </button>
  <div class="nav-links" style="align-items: center;">
    <a href="about.html">About</a>
    <a href="index.html" class="logo" aria-label="Home">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
    </a>
    <a href="technology.html">IT Portfolio</a>
    <a href="index.html#contact">Contact</a>
  </div>
</nav>

<div class="mobile-menu" id="mobileMenu" aria-hidden="true">
  <button class="mobile-menu-close" id="mobileClose" aria-label="Close menu"><span></span><span></span></button>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="technology.html">IT Portfolio</a>
  <a href="index.html#contact">Contact</a>
</div>

<!-- HERO -->
<header class="project-hero">
  <img src="images/sentinalpage/LogoTransparent.png" alt="Sentinel Access Logo" class="project-logo">
  <h1 class="project-headline">Identify. Authorize. Protect.</h1>
  <p class="project-subheadline">
    Sentinel Access is an AI-powered intelligent access control and personnel tracking system engineered for high-security naval environments. By fusing real-time biometric authentication with live IoT telemetry and automated threat intelligence, it delivers a hardened, zero-trust security perimeter from a single, unified command dashboard.
  </p>
  <a href="#" target="_blank" rel="noopener noreferrer" class="launch-btn" style="pointer-events: none; opacity: 0.7;">
    App Offline
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</header>

<main class="container" style="padding-bottom: 100px;">

  <!-- Full-width hero screenshot -->
  <div style="margin-bottom: 80px;">
    <img src="images/sentinalpage/Screenshot 2026-08-10 233023.png" alt="Sentinel Access — Dashboard View" class="full-width-screenshot lightbox-trigger" style="width:100%;">
  </div>

  <!-- Vision & Mission -->
  <section class="section-glass" style="margin-bottom: 80px;">
    <div class="glass-grid-2">
      <div>
        <div class="section-subtitle" style="text-align:left;">The Vision</div>
        <h3 style="font-size:1.9rem; color:#fff; margin-bottom:18px;">Impenetrable Security Perimeter</h3>
        <p style="color:#a0a0a0; line-height:1.75; font-size:1.05rem;">
          To establish the most intelligent and impenetrable digital security perimeter for high-security naval vessels. We envision a future where every compartment access event is authenticated with absolute certainty through AI, every threat is surfaced before it escalates, and every commanding officer has the full operational picture at their fingertips — in real time.
        </p>
      </div>
      <div>
        <div class="section-subtitle" style="text-align:left;">The Mission</div>
        <h3 style="font-size:1.9rem; color:#fff; margin-bottom:18px;">Zero-Trust Architecture</h3>
        <p style="color:#a0a0a0; line-height:1.75; font-size:1.05rem;">
          To eliminate the vulnerabilities of manual, credential-based access control by replacing it with a multi-layered, AI-driven security architecture. Sentinel Access integrates biometric identity, role-based clearance, live IoT sensing, and automated intelligence into a single cohesive platform — making unauthorized access computationally and physically impossible.
        </p>
      </div>
    </div>
  </section>

  <!-- Who is it for -->
  <section style="margin-bottom: 100px;">
    <div class="section-subtitle">Target Audience</div>
    <h2 class="section-title">Who is Sentinel Access for?</h2>
    <p style="text-align:center; color:#a0a0a0; max-width:720px; margin:0 auto 50px; font-size:1.05rem;">
      Built for organizations and operators who require airtight, intelligent security in environments where unauthorized access is not an option.
    </p>
    <div class="glass-grid-4">
      <div class="glass-card">
        <span class="card-icon">⚓</span>
        <h3>Naval & Defence Commands</h3>
        <p>Managing and enforcing clearance-level access across multiple compartments, zones, and access points aboard a vessel, with full real-time situational awareness.</p>
      </div>
      <div class="glass-card">
        <span class="card-icon">🛡️</span>
        <h3>Security Officers</h3>
        <p>Running AI-powered threat detection, monitoring failed authentication attempts, identifying anomalous movement patterns, and generating formal security intelligence reports.</p>
      </div>
      <div class="glass-card">
        <span class="card-icon">🚢</span>
        <h3>Vessel Operations</h3>
        <p>Tracking personnel onboard status, managing department-level access rights, and coordinating time-limited visitor access without manual intervention.</p>
      </div>
      <div class="glass-card">
        <span class="card-icon">💻</span>
        <h3>IT & Systems Admins</h3>
        <p>Overseeing the health of the distributed IoT device network, managing firmware states, monitoring connectivity, and responding to system-level alerts.</p>
      </div>
    </div>
  </section>

  <!-- Core Features -->
  <section style="margin-bottom: 100px;">
    <div class="section-subtitle">How It Works</div>
    <h2 class="section-title">Core Features & Capabilities</h2>

    <div class="feature-row">
      <div class="feature-text">
        <h3>AI Face Recognition Engine</h3>
        <p>Personnel are identified through a real-time face recognition pipeline. Captured frames are processed to extract encrypted facial embeddings, which are compared against enrolled biometric references to determine identity and grant or deny access with a confidence score.</p>
      </div>
      <div class="feature-image">
        <img src="images/sentinalpage/Screenshot 2026-08-10 233044.png" alt="AI Face Recognition Engine" class="lightbox-trigger">
      </div>
    </div>

    <div class="feature-row">
      <div class="feature-text">
        <h3>Real-Time Command Dashboard</h3>
        <p>A live WebSocket-powered command center streams telemetry every 3 seconds, displaying personnel onboard count, active visitor passes, secured vs. open doors, IoT device health, authentication event timelines, and active security alerts — all without a page refresh.</p>
        <p>The security intelligence engine continuously runs detection algorithms across access log data to surface anomalies ranked by severity.</p>
      </div>
      <div class="feature-image">
        <img src="images/sentinalpage/Screenshot 2026-08-10 233110.png" alt="Real-Time Command Dashboard" class="lightbox-trigger">
      </div>
    </div>

    <div class="feature-row">
      <div class="feature-text">
        <h3>Visitor Lifecycle Management</h3>
        <p>Authorised personnel can register and sponsor time-bound visitor passes, assigning compartment-specific access with defined validity windows. The system automatically revokes access upon expiry.</p>
        <p>Every physical access control node (door controller, sensor) is tracked by MAC address, firmware version, and real-time connectivity status.</p>
      </div>
      <div class="feature-image">
        <img src="images/sentinalpage/Screenshot 2026-08-10 233146.png" alt="Visitor Lifecycle Management" class="lightbox-trigger">
      </div>
    </div>

  </section>

  <!-- UX Philosophy & Tech Stack -->
  <div class="glass-grid-2" style="margin-bottom: 60px;">
    <div class="section-glass" style="margin-bottom:0;">
      <h3 style="font-size:1.9rem; color:#fff; margin-bottom:18px;">UX & Design Philosophy</h3>
      <p style="color:#a0a0a0; margin-bottom:16px;">Designed to project authority and clarity, giving operators immediate confidence in the data they see.</p>
      <ul style="color:#a0a0a0; line-height:1.8; padding-left:20px;">
        <li style="margin-bottom:12px;"><strong style="color:#ccc;">Unified Command Dashboard:</strong> The primary interface is a dense, high-information operations dashboard. Key metrics are surfaced as live KPI tiles that update in real time via WebSocket telemetry.</li>
        <li style="margin-bottom:12px;"><strong style="color:#ccc;">Dark, High-Contrast Aesthetic:</strong> The UI employs a dark-mode command interface with high-contrast status indicators and color-coded severity signals (green, amber, red).</li>
        <li><strong style="color:#ccc;">Role-Aware Navigation:</strong> Interface modules are surfaced contextually based on the authenticated user's role and permissions, ensuring operators only interact with data relevant to their clearance.</li>
      </ul>
    </div>

    <div class="section-glass" style="margin-bottom:0;">
      <h3 style="font-size:1.9rem; color:#fff; margin-bottom:18px;">Technical Architecture</h3>
      <p style="color:#a0a0a0; margin-bottom:20px;">Engineered for security, reliability, and real-time performance.</p>
      <table class="tech-table">
        <tbody>
          <tr>
            <th>Frontend Interface</th>
            <td>React 18 + TypeScript + Vite</td>
          </tr>
          <tr>
            <th>Styling</th>
            <td>Tailwind CSS</td>
          </tr>
          <tr>
            <th>Backend API</th>
            <td>FastAPI (Python)</td>
          </tr>
          <tr>
            <th>Database</th>
            <td>PostgreSQL + SQLAlchemy ORM (Alembic)</td>
          </tr>
          <tr>
            <th>AI — Face Recognition</th>
            <td>DeepFace / face_recognition + encrypted embedding storage</td>
          </tr>
          <tr>
            <th>AI — Gesture Detection</th>
            <td>MediaPipe Hands</td>
          </tr>
          <tr>
            <th>Real-Time Telemetry</th>
            <td>WebSockets (FastAPI native)</td>
          </tr>
          <tr>
            <th>Infrastructure</th>
            <td>Docker + Docker Compose</td>
          </tr>
          <tr>
            <th>Authentication</th>
            <td>JWT-based (OAuth2 Password Flow)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</main>

<!-- CTA -->
<section class="cta" id="contact" style="border-top:1px solid rgba(255,51,51,0.12); background:#050505;">
  <div class="container">
    <span class="label" style="color:var(--sentinel-accent);">Let's Connect</span>
    <h2 class="reveal-zoom">Ready to build something <span style="color:var(--sentinel-accent);">exceptional?</span></h2>
    <p style="color:var(--stone); margin-top:20px; margin-bottom:40px; max-width:500px; margin-left:auto; margin-right:auto; font-size:1.1rem;">Whether it's highly secure systems, real-time access control, or AI integration, let's collaborate.</p>
    <div class="cta-links">
      <a class="cta-link" href="mailto:eranbwt27@gmail.com" style="border-color:rgba(255,51,51,0.2);">EMAIL — eranbwt27@gmail.com</a>
      <a class="cta-link" href="https://www.linkedin.com/in/eranga-bowatte" target="_blank" rel="noopener" style="border-color:rgba(255,51,51,0.2);">LINKEDIN — Eranga Bowatte</a>
    </div>
  </div>
</section>

<footer style="background:#000000; border-top:1px solid rgba(255,51,51,0.06);">
  <span style="color:#666;">© 2026 Eranga Bowatte</span>
  <span style="color:#666;">Growth · Impact · Redefine</span>
</footer>

<!-- LIGHTBOX -->
<div id="lightbox" class="lightbox">
  <span class="lightbox-close" id="lightboxClose">&times;</span>
  <img class="lightbox-content" id="lightboxImg">
</div>

<script src="main.js" defer></script>
<script>
  // ── Cinematic parallax background scroll ──
  const parallaxBg = document.getElementById('parallax-bg');
  let ticking = false;
  function updateParallax() {
    const scrollY = window.scrollY;
    // Move background at 0.35x scroll speed for a smooth cinematic feel
    if(parallaxBg) parallaxBg.style.transform = 'translateY(' + (scrollY * 0.35) + 'px)';
    ticking = false;
  }
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(updateParallax);
      ticking = true;
    }
  }, { passive: true });

  // ── Lightbox ──
  document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxClose = document.getElementById('lightboxClose');
    document.querySelectorAll('.lightbox-trigger').forEach(img => {
      img.style.cursor = 'pointer';
      img.addEventListener('click', () => { lightbox.style.display = 'flex'; lightboxImg.src = img.src; });
    });
    if (lightboxClose) lightboxClose.addEventListener('click', () => { lightbox.style.display = 'none'; });
    if (lightbox) lightbox.addEventListener('click', e => { if (e.target === lightbox) lightbox.style.display = 'none'; });
  });
</script>
</body>
</html>
"""

with open("f:/my-portfolio/eranga-bowatte/sentinel-access.html", "w", encoding="utf-8") as f:
    f.write(html_content)
