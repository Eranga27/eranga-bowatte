import re
import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

creative_section = """
<!-- ===================== CREATIVE PORTFOLIO TEASER ===================== -->
<section id="creative-teaser" class="creative-teaser-section" style="border-top:1px solid var(--line);">
  <div class="creative-split">
    
    <!-- Left: Hook Text -->
    <div class="creative-text-col">
      <span class="label" style="display:block; margin-bottom:20px;">Portfolio 03</span>
      <h2 class="reveal-zoom" style="font-family:'Poppins', sans-serif; font-weight:800; font-size:clamp(2.5rem, 5vw, 4.5rem); line-height:1.05; margin-bottom:28px;">Visual <em style="font-style:normal; color:#FF6A1A;">Storytelling.</em></h2>
      <p style="color:var(--stone); font-size:1.05rem; line-height:1.85; max-width:38ch; margin-bottom:20px;">From striking branding at Strider Seven Group to dynamic YouTube thumbnails and personal passion projects. Where logic meets aesthetic.</p>
      <a href="creative.html" style="display:inline-flex; align-items:center; gap:12px; padding:16px 32px; background:#FF6A1A; color:#0B0A09; text-decoration:none; font-family:'Space Mono',monospace; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.12em; border-radius:4px; transition:transform 0.2s ease, background 0.2s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.background='#ff8c4a'" onmouseout="this.style.transform='translateY(0)'; this.style.background='#FF6A1A'">
        Explore Creative Work
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </div>

    <!-- Right: Three overlapping slanted images -->
    <div class="creative-images-col">
      <a href="creative.html#strider" class="creative-img-wrapper img-1" style="background-image:url('images/solo-branding-1.jpg');" aria-label="Strider Seven Group">
        <div class="creative-img-overlay"><span>Strider Seven</span></div>
      </a>
      
      <a href="creative.html#youtube" class="creative-img-wrapper img-2" style="background-image:url('images/mastering-comm-2.jpg');" aria-label="YouTube">
        <div class="creative-img-overlay"><span>YouTube</span></div>
      </a>
      
      <a href="creative.html#personal" class="creative-img-wrapper img-3" style="background-image:url('images/mic4.jpg');" aria-label="Personal Projects">
        <div class="creative-img-overlay"><span>Personal</span></div>
      </a>
    </div>
    
  </div>
</section>

"""

if "id=\"creative-teaser\"" not in html:
    html = html.replace('<!-- ===================== ABOUT ME TEASER ===================== -->', creative_section + '<!-- ===================== ABOUT ME TEASER ===================== -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if ".creative-teaser-section" not in css:
    css_to_add = """
  /* ---------- Creative Portfolio Teaser ---------- */
  .creative-teaser-section {
    position: relative;
    padding: 120px 40px;
    background: radial-gradient(circle at 80% 50%, rgba(255, 106, 26, 0.04) 0%, var(--ink) 100%);
    overflow: hidden;
  }
  .creative-split {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 40px;
  }
  .creative-text-col {
    flex: 1;
    z-index: 2;
  }
  .creative-images-col {
    flex: 1.2;
    position: relative;
    height: 500px;
  }
  .creative-img-wrapper {
    position: absolute;
    background-size: cover;
    background-position: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.8);
    clip-path: polygon(25% 0%, 100% 0%, 75% 100%, 0% 100%);
    transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.2s ease, filter 0.3s ease;
    overflow: hidden;
    cursor: pointer;
  }
  
  .img-1 {
    width: 320px; height: 260px;
    top: 0; right: 20px;
    z-index: 3;
    filter: brightness(0.85);
  }
  .img-2 {
    width: 380px; height: 300px;
    top: 50%; left: -20px;
    margin-top: -150px;
    z-index: 2;
  }
  .img-3 {
    width: 290px; height: 240px;
    bottom: 20px; right: 60px;
    z-index: 4;
    filter: brightness(0.9);
  }

  /* Out-of-view state */
  .creative-teaser-section:not(.in-view) .img-1 {
    transform: translate(150%, -150%);
    opacity: 0;
  }
  .creative-teaser-section:not(.in-view) .img-2 {
    transform: translate(-150%, 0);
    opacity: 0;
  }
  .creative-teaser-section:not(.in-view) .img-3 {
    transform: translate(100%, 150%);
    opacity: 0;
  }

  /* In-view state */
  .creative-teaser-section.in-view .img-1 {
    transform: translate(0, 0);
    opacity: 1;
  }
  .creative-teaser-section.in-view .img-2 {
    transform: translate(0, 0);
    opacity: 1;
  }
  .creative-teaser-section.in-view .img-3 {
    transform: translate(0, 0);
    opacity: 1;
  }

  /* Hover states */
  .creative-img-wrapper::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(0deg, rgba(255,106,26,0.6) 0%, transparent 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  .creative-img-overlay {
    position: absolute;
    bottom: 30px; left: 80px;
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--paper);
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
    z-index: 5;
    text-shadow: 0 2px 4px rgba(0,0,0,0.8);
  }

  @keyframes creativeWiggle {
    0% { transform: rotate(0deg) scale(1.05); }
    25% { transform: rotate(3deg) scale(1.05); }
    50% { transform: rotate(-3deg) scale(1.05); }
    75% { transform: rotate(2deg) scale(1.05); }
    100% { transform: rotate(0deg) scale(1.05); }
  }

  .creative-teaser-section.in-view .creative-img-wrapper:hover {
    z-index: 10;
    filter: brightness(1.1);
    animation: creativeWiggle 0.4s ease-in-out forwards;
  }
  .creative-img-wrapper:hover::after { opacity: 1; }
  .creative-img-wrapper:hover .creative-img-overlay { opacity: 1; transform: translateY(0); }

  @media (max-width: 900px) {
    .creative-split { flex-direction: column; }
    .creative-images-col { height: 400px; width: 100%; margin-top: 40px; }
    .img-1 { width: 220px; height: 180px; top: 0; right: 0; }
    .img-2 { width: 260px; height: 210px; left: 0; margin-top: -105px; }
    .img-3 { width: 200px; height: 160px; bottom: 0; right: 20px; }
    .creative-img-overlay { left: 40px; font-size: 0.8rem; }
  }
"""
    css = css + "\n" + css_to_add

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update main.js
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

if "creativeTeaser" not in js:
    observer_code = """
  /* ---- Creative Section Slide-In ---- */
  const creativeTeaser = document.getElementById('creative-teaser');
  if (creativeTeaser) {
    const creativeIO = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
        } else {
          entry.target.classList.remove('in-view');
        }
      });
    }, { threshold: 0.2 });
    creativeIO.observe(creativeTeaser);
  }
"""
    # Insert it near the end of the DOMContentLoaded block
    js = js.replace("}); // end load", observer_code + "\n}); // end load")
    with open('main.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Creative section added successfully.")
