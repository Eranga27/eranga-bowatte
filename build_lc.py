import re

with open('leadership-creative.html', 'r', encoding='utf-8') as f:
    lc_html = f.read()

top_part_lc = re.search(r'(.*?)<!-- PAGE CONTENT -->', lc_html, re.DOTALL).group(1)
bottom_part_lc = re.search(r'(<footer>.*)', lc_html, re.DOTALL).group(1)

new_lc_content = """
<!-- ===================== HERO ===================== -->
<header class="hero" style="min-height: 60vh;">
  <div class="hero-bg">
    <img src="images/mic1.jpg" alt="Leadership & Creative">
  </div>
  <div class="container hero-content" style="padding-top: 160px; padding-bottom: 80px;">
    <div class="hero-eyebrow reveal">
      <div class="line"></div>
      <span class="label">Leadership & Creative Portfolio</span>
    </div>
    <h1 class="headline reveal" style="animation-delay:0.1s">
      Vision &amp; <em>Execution</em>
    </h1>
    <p class="hero-sub reveal" style="animation-delay:0.2s">
      From winning national colours in scouting to leading global youth initiatives, intertwined with a passion for creative arts and personal branding.
    </p>
  </div>
</header>

<!-- ===================== LEADERSHIP & RECOGNITION ===================== -->
<section style="padding-top: 100px; padding-bottom: 140px; background: var(--surface);">
  <div class="container">
    
    <div class="section-head reveal" style="margin-bottom: 80px;">
      <span class="label">Awards & Honours</span>
      <h2>A Track Record of <em>Leadership.</em></h2>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px;" class="reveal">
      
      <!-- Recognition 1 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 40px; border-radius: 12px;">
        <span style="color:#FF6A1A; font-family:'Space Mono', monospace; font-size:0.9rem; margin-bottom: 10px; display:block;">2023 — AIESEC in SLIIT</span>
        <h3 style="font-family:'Poppins', sans-serif; font-size:1.5rem; margin-bottom: 15px;">Legacy Awards Night</h3>
        <p style="color:var(--stone);">Won Best Emerging Incoming Global Volunteer (CXP, B2B) and was nominated for Best Emerging Young Leader.</p>
      </div>

      <!-- Recognition 2 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 40px; border-radius: 12px;">
        <span style="color:#FF6A1A; font-family:'Space Mono', monospace; font-size:0.9rem; margin-bottom: 10px; display:block;">2013 to 2019 — Scouting</span>
        <h3 style="font-family:'Poppins', sans-serif; font-size:1.5rem; margin-bottom: 15px;">President Sea Scout Award</h3>
        <p style="color:var(--stone);">Achieved National Colours at Lyceum International School, culminating years of dedicated scouting leadership.</p>
      </div>

      <!-- Recognition 3 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 40px; border-radius: 12px;">
        <span style="color:#FF6A1A; font-family:'Space Mono', monospace; font-size:0.9rem; margin-bottom: 10px; display:block;">Public Speaking Excellence</span>
        <h3 style="font-family:'Poppins', sans-serif; font-size:1.5rem; margin-bottom: 15px;">Inter-University Debate</h3>
        <p style="color:var(--stone);">Runners-Up at the SLIIT IEEE Debate and a Finalist at the University of Kelaniya All-Island Best Speakers contest.</p>
      </div>

    </div>

  </div>
</section>

<!-- ===================== CTA ===================== -->
<section class="cta" id="contact" style="border-top: 1px solid var(--line);">
  <div class="container">
    <span class="label">Let's Connect</span>
    <h2>Ready to build <span class="accent-word">something great?</span></h2>
    <p style="color:var(--stone); margin-top:20px; margin-bottom:40px; max-width:500px; margin-left:auto; margin-right:auto; font-size:1.1rem;">Whether you need a visionary leader or a creative spark, let's talk.</p>
    <div class="cta-links">
      <a class="cta-link" href="mailto:eranbwt27@gmail.com">EMAIL — eranbwt27@gmail.com</a>
      <a class="cta-link" href="https://www.linkedin.com/in/eranga-bowatte" target="_blank" rel="noopener">LINKEDIN — Eranga Bowatte</a>
    </div>
  </div>
</section>
"""

with open('leadership-creative.html', 'w', encoding='utf-8') as f:
    f.write(top_part_lc + new_lc_content + bottom_part_lc)

print('Updated leadership-creative.html')
