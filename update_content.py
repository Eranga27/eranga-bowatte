import re
import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hr_section = """
<!-- ===================== HR PORTFOLIO TEASER ===================== -->
<section id="hr-teaser" class="portfolio-teaser-section" style="border-top:1px solid var(--line);">
  <div class="teaser-split">
    
    <!-- Left: Hook Text -->
    <div class="teaser-hook-col" style="order: 1;">
      <span class="label" style="display:block; margin-bottom:20px;">Portfolio 02</span>
      <h2 class="reveal-zoom" style="font-family:'Poppins', sans-serif; font-weight:800; font-size:clamp(2.5rem, 5vw, 4.5rem); line-height:1.05; margin-bottom:28px;">People &amp; <em style="font-style:normal; color:#FF6A1A;">Culture.</em></h2>
      <p style="color:var(--stone); font-size:1.05rem; line-height:1.85; max-width:38ch; margin-bottom:20px;">Bridging the gap between technical execution and human connection through robust HR practices and cultural development.</p>
      <a href="human-resources.html" style="display:inline-flex; align-items:center; gap:12px; padding:16px 32px; background:#FF6A1A; color:#0B0A09; text-decoration:none; font-family:'Space Mono',monospace; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.12em; border-radius:4px; transition:transform 0.2s ease, background 0.2s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.background='#ff8c4a'" onmouseout="this.style.transform='translateY(0)'; this.style.background='#FF6A1A'">
        Explore HR Portfolio
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </div>

    <!-- Right: Flip Cards -->
    <div class="teaser-accordion-col hr-cards-container" style="order: 2; display: flex; gap: 20px; align-items: center; justify-content: center; width: 100%; height: 520px; overflow: hidden; padding: 20px;">
      
      <!-- Card 1 -->
      <div class="flip-card-wrapper">
        <div class="flip-card-inner">
          <div class="flip-card-front">
            <h3 style="font-family:'Space Mono',monospace; font-size:1.5rem; letter-spacing: 2px;">AIESEC</h3>
          </div>
          <div class="flip-card-back" style="background-image:url('images/team.jpg');">
            <div class="acc-content">
              <h3>AIESEC Leadership</h3>
              <a href="human-resources.html" class="visit-btn">VISIT</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="flip-card-wrapper">
        <div class="flip-card-inner">
          <div class="flip-card-front">
            <h3 style="font-family:'Space Mono',monospace; font-size:1.5rem; letter-spacing: 2px;">VIRTUSA</h3>
          </div>
          <div class="flip-card-back" style="background-image:url('images/virtusa-training-1.jpg');">
            <div class="acc-content">
              <h3>Virtusa Training</h3>
              <a href="human-resources.html" class="visit-btn">VISIT</a>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</section>

"""

if "id=\"hr-teaser\"" not in html:
    html = html.replace('<!-- ===================== ABOUT ME TEASER ===================== -->', hr_section + '<!-- ===================== ABOUT ME TEASER ===================== -->')

# Add reveal-zoom class to existing text
html = html.replace('<h2 class="snapshot-heading">', '<h2 class="snapshot-heading reveal-zoom">')
html = html.replace('<div class="disciplines-text">', '<div class="disciplines-text reveal-zoom">')
html = html.replace('<h2 style="font-family:\'Poppins\', sans-serif; font-weight:800; font-size:clamp(2.5rem, 5vw, 4.5rem); line-height:1.05; margin-bottom:28px;">Voice &amp; <em style="font-style:normal; color:#FF6A1A;">Influence.</em></h2>', '<h2 class="reveal-zoom" style="font-family:\'Poppins\', sans-serif; font-weight:800; font-size:clamp(2.5rem, 5vw, 4.5rem); line-height:1.05; margin-bottom:28px;">Voice &amp; <em style="font-style:normal; color:#FF6A1A;">Influence.</em></h2>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if ".reveal-zoom" not in css:
    css_to_add = """
  /* ---------- Reveal Zoom (Enlarge on scroll) ---------- */
  .reveal-zoom {
    opacity: 0;
    transform: scale(0.8);
    transition: opacity 0.85s cubic-bezier(0.4,0,0.2,1), transform 0.85s cubic-bezier(0.4,0,0.2,1);
    transform-origin: left center;
  }
  .reveal-zoom.in {
    opacity: 1;
    transform: scale(1);
  }
  .reveal-zoom.out {
    opacity: 0;
    transform: scale(0.8);
    transition: opacity 0.55s ease, transform 0.55s ease;
  }

  /* ---------- HR Flip Cards ---------- */
  .hr-cards-container {
    perspective: 1000px;
  }
  .flip-card-wrapper {
    width: 240px;
    height: 340px;
    background-color: transparent;
    perspective: 1000px;
    cursor: pointer;
    flex-shrink: 0;
  }
  .flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    transform-style: preserve-3d;
    border-radius: 8px;
  }
  .flip-card-wrapper:hover .flip-card-inner {
    transform: rotateY(180deg);
  }
  .flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--line);
    overflow: hidden;
  }
  .flip-card-front {
    background-color: var(--surface);
    color: var(--paper);
    transition: background-color 0.3s ease;
  }
  .flip-card-wrapper:hover .flip-card-front {
    background-color: var(--ink);
  }
  .flip-card-back {
    background-color: var(--ink);
    color: white;
    transform: rotateY(180deg);
    background-size: cover;
    background-position: center;
    position: relative;
  }
  .flip-card-back::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(0deg, rgba(11,10,9,0.95) 0%, rgba(11,10,9,0.3) 100%);
  }
  .flip-card-back .acc-content {
    position: relative;
    z-index: 2;
    padding: 20px;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
  }
  .flip-card-back .visit-btn {
    margin-top: 15px;
    padding: 10px 24px;
    background: #e62020;
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none;
    border-radius: 4px;
    text-transform: uppercase;
    transition: background 0.3s ease, transform 0.2s ease;
    width: 100%;
    text-align: center;
  }
  .flip-card-back .visit-btn:hover {
    background: #ff3333;
    transform: translateY(-2px);
  }
  .flip-card-back h3 {
    font-family: 'Poppins', sans-serif;
    font-size: 1.2rem;
    margin-bottom: 0;
    text-align: center;
  }
"""
    css = css + "\n" + css_to_add

# Shrink the core disciplines padding
css = css.replace('.portfolio-nav-section {\n    padding: 140px 0;\n    position: relative;\n  }', '.portfolio-nav-section {\n    padding: 60px 0;\n    position: relative;\n  }')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update main.js
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make IntersectionObserver target .reveal and .reveal-zoom
js = js.replace("document.querySelectorAll('.reveal');", "document.querySelectorAll('.reveal, .reveal-zoom');")

# Fix the alignment and font of the centerText inside donut
new_center_css = '''    centerText.style.cssText = `
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: var(--paper);
      opacity: 1;
      transition: opacity 0.3s ease;
      pointer-events: none;
      z-index: 5;
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 1.4rem;
      letter-spacing: 0.05em;
      line-height: 1.3;
      max-width: 220px;
    `;'''

js = re.sub(r"centerText\.style\.cssText\s*=\s*`[^`]+`;", new_center_css, js)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updates completed successfully.")
