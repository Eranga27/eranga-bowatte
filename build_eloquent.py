import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Eloquent One - AI-powered communication coaching platform.">
<meta property="og:title" content="Eloquent One — Eranga Bowatte">
<meta property="og:description" content="Communicate with Absolute Clarity. An enterprise-grade, AI-powered communication coaching platform.">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0B0A09">
<title>Eloquent One — Eranga Bowatte</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Poppins:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<style>
  :root {
    --eloquent-accent: #00d2ff;
    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-border: rgba(255, 255, 255, 0.08);
  }
  
  body {
    background-color: #050505;
    background-image: url('images/myportfoliopage/BGDark.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #e0e0e0;
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
    width: 200px;
    margin-bottom: 30px;
    animation: fadeUp 1s ease forwards;
  }

  .project-headline {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 24px;
    background: linear-gradient(90deg, #ffffff 30%, var(--eloquent-accent) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeUp 1s ease forwards 0.2s;
    opacity: 0;
  }

  .project-subheadline {
    font-size: clamp(1.1rem, 2vw, 1.3rem);
    max-width: 800px;
    margin: 0 auto 40px;
    color: #a0a0a0;
    line-height: 1.6;
    animation: fadeUp 1s ease forwards 0.4s;
    opacity: 0;
  }

  .launch-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 16px 36px;
    background: var(--eloquent-accent);
    color: #000;
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
    box-shadow: 0 10px 20px rgba(0, 210, 255, 0.3);
  }

  .section-glass {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
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
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
  }

  .glass-card {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid var(--glass-border);
    padding: 40px;
    border-radius: 12px;
    transition: transform 0.3s ease;
  }
  
  .glass-card:hover {
    transform: translateY(-5px);
    border-color: rgba(0, 210, 255, 0.3);
  }

  .glass-card h3 {
    font-size: 1.4rem;
    color: #fff;
    margin-bottom: 16px;
  }

  .glass-card p {
    color: #a0a0a0;
    line-height: 1.6;
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

  .feature-text {
    flex: 1;
  }

  .feature-text h3 {
    font-size: 2rem;
    color: #fff;
    margin-bottom: 20px;
  }

  .feature-text p {
    color: #a0a0a0;
    line-height: 1.7;
    font-size: 1.1rem;
    margin-bottom: 15px;
  }

  .feature-image {
    flex: 1.2;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--glass-border);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  }
  
  .feature-image img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.5s ease;
  }

  .feature-image:hover img {
    transform: scale(1.03);
  }

  .section-title {
    font-size: 2.5rem;
    color: #fff;
    margin-bottom: 40px;
    text-align: center;
  }
  
  .section-subtitle {
    text-align: center;
    color: var(--eloquent-accent);
    font-family: 'Space Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.9rem;
    margin-bottom: 16px;
  }

  .tech-pill {
    display: inline-block;
    padding: 10px 20px;
    background: rgba(0, 210, 255, 0.1);
    color: var(--eloquent-accent);
    border: 1px solid rgba(0, 210, 255, 0.2);
    border-radius: 30px;
    margin: 5px;
    font-family: 'Space Mono', monospace;
    font-size: 0.9rem;
  }

  @media (max-width: 900px) {
    .glass-grid-2 { grid-template-columns: 1fr; }
    .feature-row, .feature-row:nth-child(even) { flex-direction: column; gap: 30px; }
    .section-glass { padding: 30px; }
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>

<!-- ===================== PRELOADER ===================== -->
<div id="preloader" class="preloader">
  <div class="preloader-content">
    <h1 class="signature-text">
      <span class="flare"></span>
      Eranga Bowatte
    </h1>
  </div>
</div>

<nav style="background: rgba(5,5,5,0.8); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.05);">
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
  <button class="mobile-menu-close" id="mobileClose" aria-label="Close menu">
    <span></span><span></span>
  </button>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="technology.html">Technology</a>
  <a href="index.html#contact">Contact</a>
</div>

<!-- ===================== HERO ===================== -->
<header class="project-hero">
  <img src="images/myportfoliopage/LogoTransparent.png" alt="Eloquent One Logo" class="project-logo">
  <h1 class="project-headline">Communicate with<br>Absolute Clarity.</h1>
  <p class="project-subheadline">
    Eloquent One is an enterprise-grade, AI-powered communication coaching platform designed to elevate professional speaking skills. Using real-time telemetry and advanced NLP, it provides instant, executive-level feedback on your delivery, presence, and confidence.
  </p>
  <a href="https://comms-app-lq2e.vercel.app/" target="_blank" rel="noopener noreferrer" class="launch-btn">
    Launch Platform
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</header>

<main class="container" style="padding-bottom: 100px;">
  
  <!-- Vision & Mission -->
  <section class="section-glass">
    <div class="glass-grid-2">
      <div>
        <div class="section-subtitle" style="text-align: left;">The Vision</div>
        <h3 style="font-size: 2rem; color: #fff; margin-bottom: 20px;">Command Any Room</h3>
        <p style="color: #a0a0a0; line-height: 1.7; font-size: 1.1rem;">
          To empower professionals globally with the absolute confidence and clarity to deliver high-impact communication in any environment. We envision a world where anyone can walk into a room—physical or virtual—and command it.
        </p>
      </div>
      <div>
        <div class="section-subtitle" style="text-align: left;">The Mission</div>
        <h3 style="font-size: 2rem; color: #fff; margin-bottom: 20px;">Democratize Coaching</h3>
        <p style="color: #a0a0a0; line-height: 1.7; font-size: 1.1rem;">
          To democratize executive-level communication coaching. We are removing the barrier of expensive, inaccessible private coaches by leveraging advanced AI to provide instant, personalized, and highly actionable feedback on your speech, facial expressions, and body language.
        </p>
      </div>
    </div>
  </section>

  <!-- Who is it for? -->
  <section style="margin-bottom: 100px; margin-top: 100px;">
    <div class="section-subtitle">Target Audience</div>
    <h2 class="section-title">Who is Eloquent One for?</h2>
    <p style="text-align: center; color: #a0a0a0; max-width: 700px; margin: 0 auto 50px; font-size: 1.1rem;">Built for ambitious individuals who understand that how you speak is just as important as what you say.</p>
    
    <div class="glass-grid-4">
      <div class="glass-card">
        <h3>Executives & Founders</h3>
        <p>Preparing for high-stakes board meetings, investor pitches, and company-wide addresses.</p>
      </div>
      <div class="glass-card">
        <h3>Sales Professionals</h3>
        <p>Refining their pitch delivery to build trust, maintain strong eye contact, and close deals.</p>
      </div>
      <div class="glass-card">
        <h3>Job Seekers</h3>
        <p>Practicing interview scenarios to eliminate filler words, control speaking pace, and project confidence.</p>
      </div>
      <div class="glass-card">
        <h3>Public Speakers</h3>
        <p>Honing their stage presence and pacing to keep large audiences engaged and captivated.</p>
      </div>
    </div>
  </section>

  <!-- Core Features -->
  <section style="margin-bottom: 100px;">
    <div class="section-subtitle">How It Works</div>
    <h2 class="section-title">Core Features & Capabilities</h2>
    
    <div class="feature-row">
      <div class="feature-text">
        <h3>Live Telemetry Engine</h3>
        <p><strong>The Eyes:</strong> Utilizing advanced computer vision (MediaPipe), the platform tracks physical presence in real-time. It monitors eye contact consistency, posture alignment, and the frequency of hand gestures without ever storing user video data.</p>
      </div>
      <div class="feature-image">
        <img src="images/myportfoliopage/Screenshot 2026-08-11 121200.png" alt="Live Telemetry Engine" class="lightbox-trigger">
      </div>
    </div>

    <div class="feature-row">
      <div class="feature-text">
        <h3>NLP Coaching Engine</h3>
        <p><strong>The Ears:</strong> Processes live audio transcriptions instantly to calculate speaking pace (Words Per Minute), detect and highlight filler words (um, ah, like), and evaluate narrative structure.</p>
        <p><strong>Context-Aware Assessment:</strong> Users select their environment (Sales Pitch, Job Interview, Casual Presentation) and the AI adjusts its scoring matrix, tracking "Power Words" relevant to that specific context.</p>
      </div>
      <div class="feature-image">
        <img src="images/myportfoliopage/Screenshot 2026-08-11 121632.png" alt="NLP Coaching Engine" class="lightbox-trigger">
      </div>
    </div>

    <div class="feature-row">
      <div class="feature-text">
        <h3>Dashboard Intelligence</h3>
        <p>A dynamic, premium user dashboard that aggregates historical session data to compute rolling averages. It generates personalized insights (e.g., identifying a user's "Most Improved Skill") and prescribes targeted practice drills based on their weakest metrics.</p>
      </div>
      <div class="feature-image">
        <img src="images/myportfoliopage/Screenshot 2026-08-11 121732.png" alt="Dashboard Intelligence" class="lightbox-trigger">
      </div>
    </div>

    <div class="feature-row">
      <div class="feature-text">
        <h3>Goal-Oriented Practice</h3>
        <p>Users can lock in "Active Goals" (e.g., "Reduce Fillers" or "Slow Down Pace"). The coaching engine will focus heavily on these metrics, providing specific nudges and tailored post-session grades.</p>
      </div>
      <div class="feature-image">
        <img src="images/myportfoliopage/Screenshot 2026-08-11 121827.png" alt="Goal-Oriented Practice" class="lightbox-trigger">
      </div>
    </div>
  </section>

  <!-- UX & Design / Tech Stack -->
  <div class="glass-grid-2" style="margin-bottom: 60px;">
    <div class="section-glass" style="margin-bottom: 0;">
      <h3 style="font-size: 2rem; color: #fff; margin-bottom: 20px;">UX & Design Philosophy</h3>
      <p style="color: #a0a0a0; margin-bottom: 15px;">Designed to feel like a premium, enterprise-grade tool.</p>
      <ul style="color: #a0a0a0; line-height: 1.7; padding-left: 20px;">
        <li style="margin-bottom: 10px;"><strong>Distraction-Free Practice:</strong> The recording interface strips away UI clutter, offering "Focus Modes" (blurred background, teleprompter view) to keep the speaker in the zone.</li>
        <li><strong>Glassmorphic Dark Mode:</strong> The entire application uses a modern, dark-mode-first aesthetic with deep slate tones, vibrant ambient glows, and smooth micro-animations to build immediate trust.</li>
      </ul>
    </div>
    
    <div class="section-glass" style="margin-bottom: 0;">
      <h3 style="font-size: 2rem; color: #fff; margin-bottom: 20px;">Technical Architecture</h3>
      <p style="color: #a0a0a0; margin-bottom: 25px;">Built on a highly performant, microservice-inspired architecture.</p>
      <div style="display: flex; flex-wrap: wrap; gap: 10px;">
        <span class="tech-pill">React (TypeScript)</span>
        <span class="tech-pill">Vite</span>
        <span class="tech-pill">Tailwind CSS</span>
        <span class="tech-pill">Framer Motion</span>
        <span class="tech-pill">Google MediaPipe</span>
        <span class="tech-pill">Python NLP</span>
      </div>
    </div>
  </div>
  
  <div style="text-align: center; margin-bottom: 80px;">
    <img src="images/myportfoliopage/Screenshot 2026-08-11 121905.png" alt="Eloquent One UI Overview" class="lightbox-trigger" style="max-width: 100%; border-radius: 12px; border: 1px solid var(--glass-border); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
  </div>

</main>

<!-- ===================== CTA ===================== -->
<section class="cta" id="contact" style="border-top: 1px solid rgba(255,255,255,0.1); background: #050505;">
  <div class="container">
    <span class="label" style="color: var(--eloquent-accent);">Let's Connect</span>
    <h2 class="reveal-zoom">Ready to build something <span style="color: var(--eloquent-accent);">exceptional?</span></h2>
    <p style="color:var(--stone); margin-top:20px; margin-bottom:40px; max-width:500px; margin-left:auto; margin-right:auto; font-size:1.1rem;">Whether it's full-stack development, AI integration, or data-driven insights, let's collaborate.</p>
    <div class="cta-links">
      <a class="cta-link" href="mailto:eranbwt27@gmail.com" style="border-color: rgba(255,255,255,0.2);">EMAIL — eranbwt27@gmail.com</a>
      <a class="cta-link" href="https://www.linkedin.com/in/eranga-bowatte" target="_blank" rel="noopener" style="border-color: rgba(255,255,255,0.2);">LINKEDIN — Eranga Bowatte</a>
    </div>
  </div>
</section>

<footer style="background: #000; border-top: 1px solid rgba(255,255,255,0.05);">
  <span style="color: #666;">© 2026 Eranga Bowatte</span>
  <span style="color: #666;">Growth · Impact · Redefine</span>
</footer>

<!-- ===================== LIGHTBOX ===================== -->
<div id="lightbox" class="lightbox">
  <span class="lightbox-close" id="lightboxClose">&times;</span>
  <img class="lightbox-content" id="lightboxImg">
</div>

<script src="main.js" defer></script>
<!-- Make images click to open in Lightbox -->
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxClose = document.getElementById('lightboxClose');
    
    document.querySelectorAll('.lightbox-trigger').forEach(img => {
      img.style.cursor = 'pointer';
      img.addEventListener('click', () => {
        lightbox.style.display = 'flex';
        lightboxImg.src = img.src;
      });
    });
    
    if(lightboxClose) {
      lightboxClose.addEventListener('click', () => {
        lightbox.style.display = 'none';
      });
    }
    
    if(lightbox) {
      lightbox.addEventListener('click', (e) => {
        if(e.target === lightbox) lightbox.style.display = 'none';
      });
    }
  });
</script>
</body>
</html>"""

with open("f:/my-portfolio/eranga-bowatte/eloquent-one.html", "w", encoding="utf-8") as f:
    f.write(html_content)
