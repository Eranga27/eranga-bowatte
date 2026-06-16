import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract top and bottom parts
top_part = re.search(r'(.*?<!-- ===================== HERO ===================== -->)', html, re.DOTALL).group(1)
bottom_part = re.search(r'(<footer>.*)', html, re.DOTALL).group(1)

new_body = """
<!-- ===================== HERO ===================== -->
<header class="hero" id="top">
  <div class="hero-bg">
    <img src="images/solo-branding-1.jpg" alt="Eranga Bowatte - Multi-Disciplinary Professional">
  </div>
  <div class="container hero-content">
    <div class="hero-eyebrow reveal">
      <div class="line"></div>
      <span class="label">Eranga Bowatte</span>
    </div>
    <h1 class="headline reveal" style="animation-delay:0.1s">
      I build systems, <br>
      shape cultures, <span class="accent-word">and drive growth.</span>
    </h1>
    <p class="hero-sub reveal" style="animation-delay:0.2s">
      Bridging the gap between technology, human resources, business development, and high-impact communication. A multi-disciplinary professional turning complexity into clarity.
    </p>
    <div class="hero-meta reveal" style="animation-delay:0.3s">
      <span class="frame-label">Scroll to explore</span>
      <div class="waveform">
        <div class="bar" style="animation-delay: 0.0s"></div>
        <div class="bar" style="animation-delay: 0.2s"></div>
        <div class="bar" style="animation-delay: 0.4s"></div>
        <div class="bar" style="animation-delay: 0.1s"></div>
        <div class="bar" style="animation-delay: 0.3s"></div>
      </div>
    </div>
  </div>
</header>

<!-- ===================== FUN TO KNOW BY NUMBERS ===================== -->
<div class="banner-split reveal" id="numbers" style="grid-template-columns: 1fr;">
  <div class="banner-stats-side" style="border-left:none; align-items:center; text-align:center;">
    <h3 class="stats-headline" style="color:var(--paper); font-size:1.5rem; letter-spacing:0.1em; margin-bottom:40px;">Fun to Know By Numbers</h3>
    <div style="display:flex; flex-wrap:wrap; gap:60px; justify-content:center;">
      <div class="stat-row">
        <span class="stat-number"><span class="counter" data-target="75">0</span>+</span>
        <span class="stat-label">Training Sessions<br>Conducted</span>
      </div>
      <div class="stat-row">
        <span class="stat-number"><span class="counter" data-target="1500">0</span>+</span>
        <span class="stat-label">Attendees<br>Reached</span>
      </div>
      <div class="stat-row">
        <span class="stat-number"><span class="counter" data-target="10">0</span>+</span>
        <span class="stat-label">Tech Projects<br>Delivered</span>
      </div>
      <div class="stat-row">
        <span class="stat-number"><span class="counter" data-target="350">0</span>+</span>
        <span class="stat-label">Employees<br>Managed (HR)</span>
      </div>
    </div>
  </div>
</div>

<!-- ===================== PORTFOLIOS (THE GATEWAY) ===================== -->
<section id="portfolios" class="portfolio-nav-section" style="padding-top:140px; padding-bottom:140px;">
  <div class="container">
    <div class="section-head reveal" style="text-align:center;">
      <span class="label">Explore The Branches</span>
      <h2>My Core <em>Disciplines</em></h2>
      <p style="color:var(--stone); margin-top:20px; max-width:600px; margin-left:auto; margin-right:auto;">
        Select a portfolio below to dive deep into my specialized experience across different industries.
      </p>
    </div>
    
    <div style="display:flex; flex-wrap:wrap; align-items:center; gap:60px; justify-content:center;" class="reveal">
      
      <!-- The Interactive Donut -->
      <div class="portfolio-circle-container" style="flex-shrink:0;">
        <svg viewBox="0 0 600 600" class="portfolio-donut" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern id="img-0" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/mic1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-1" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/team.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-2" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/virtusa-training-1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-3" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/solo-branding-1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-4" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/iit-business-1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
          </defs>
          <g class="donut-segment" data-index="0" onclick="window.location.href='communication.html'" style="--tx: 7.05px; --ty: -9.71px;">
            <path d="M 304.36 50.04 A 250 250 0 0 1 536.38 218.61 L 394.55 267.44 A 100 100 0 0 0 301.75 200.02 Z" class="donut-path" fill="url(#img-0)" />
          </g>
          <g class="donut-segment" data-index="1" onclick="window.location.href='leadership-creative.html'" style="--tx: 11.41px; --ty: 3.71px;">
            <path d="M 539.08 226.91 A 250 250 0 0 1 450.45 499.66 L 360.18 379.86 A 100 100 0 0 0 395.63 270.76 Z" class="donut-path" fill="url(#img-1)" />
          </g>
          <g class="donut-segment" data-index="2" onclick="window.location.href='human-resources.html'" style="--tx: 0.00px; --ty: 12.00px;">
            <path d="M 443.39 504.79 A 250 250 0 0 1 156.61 504.79 L 242.64 381.92 A 100 100 0 0 0 357.36 381.92 Z" class="donut-path" fill="url(#img-2)" />
          </g>
          <g class="donut-segment" data-index="3" onclick="window.location.href='business-development.html'" style="--tx: -11.41px; --ty: 3.71px;">
            <path d="M 149.55 499.66 A 250 250 0 0 1 60.92 226.91 L 204.37 270.76 A 100 100 0 0 0 239.82 379.86 Z" class="donut-path" fill="url(#img-3)" />
          </g>
          <g class="donut-segment" data-index="4" onclick="window.location.href='technology.html'" style="--tx: -7.05px; --ty: -9.71px;">
            <path d="M 63.62 218.61 A 250 250 0 0 1 295.64 50.04 L 298.25 200.02 A 100 100 0 0 0 205.45 267.44 Z" class="donut-path" fill="url(#img-4)" />
          </g>
        </svg>
      </div>

      <!-- Bento Grid Navigation Links -->
      <div class="bento-links" style="display:flex; flex-direction:column; gap:16px; flex:1; min-width:300px;">
        <a href="technology.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Technology & IT</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Full Stack Development, Data Analytics, Software Engineering.</p>
        </a>
        <a href="business-development.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Business Development</h3>
          <p style="color:var(--stone); font-size:0.9rem;">AIESEC BD, Strategic Partnerships, Growth Initiatives.</p>
        </a>
        <a href="communication.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Communication</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Corporate Training, Public Speaking, Emcee.</p>
        </a>
        <a href="human-resources.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Human Resources</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Employee Engagement, Culture Audit, Virtusa.</p>
        </a>
        <a href="leadership-creative.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Leadership & Creative</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Personal Branding, Team Leadership, Dubbing.</p>
        </a>
      </div>

    </div>
  </div>
</section>

<!-- ===================== ABOUT ME TEASER ===================== -->
<section id="about-teaser" style="background:var(--surface); border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="container">
    <div class="story-grid reveal" style="align-items:center;">
      <div class="story-text">
        <span class="label" style="display:block; margin-bottom:20px;">The Person Behind The Work</span>
        <h2 style="font-family:'Poppins',sans-serif; font-weight:500; font-size:clamp(2rem, 4vw, 3rem); line-height:1.15; margin-bottom:30px;">
          From the back row to <br><em>the global stage.</em>
        </h2>
        <p>Before the words came, there was silence. I spent my early years paralyzed by the thought of public speaking. Today, I don't just speak—I train others to find their voice, I build technology systems that scale, and I lead high-impact teams across the globe.</p>
        <p>My journey is built on small, deliberate repetitions and an obsession with bridging the gap between human connection and technical execution.</p>
        <a href="about.html" style="display:inline-block; margin-top:30px; padding:16px 32px; background:#FF6A1A; color:var(--ink); text-decoration:none; font-family:'Space Mono',monospace; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; border-radius:4px; transition:transform 0.2s ease, background 0.2s ease;">Read Full Story</a>
      </div>
      <div class="banner-img-side" style="border-radius:12px; aspect-ratio:4/5;">
        <img src="images/journey-glimpse.jpg" alt="Eranga Bowatte on stage">
      </div>
    </div>
  </div>
</section>

<!-- ===================== CTA ===================== -->
<section class="cta" id="contact">
  <div class="container">
    <span class="label">Let's Connect</span>
    <h2>Ready to <span class="accent-word">collaborate?</span></h2>
    <p style="color:var(--stone); margin-top:20px; margin-bottom:40px; max-width:500px; margin-left:auto; margin-right:auto; font-size:1.1rem;">Whether you need a tech wizard, an HR strategist, a corporate trainer, or a business development lead, I'm ready to bring value to your team.</p>
    <div class="cta-links">
      <a class="cta-link" href="mailto:eranbwt27@gmail.com">EMAIL — eranbwt27@gmail.com</a>
      <a class="cta-link" href="tel:+94765900817">CALL — +94 76 590 0817</a>
      <a class="cta-link" href="https://www.linkedin.com/in/eranga-bowatte" target="_blank" rel="noopener">LINKEDIN — Eranga Bowatte</a>
    </div>
  </div>
</section>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(top_part + new_body + bottom_part)
print("Updated index.html")
