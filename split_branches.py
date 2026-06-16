import os
import re
import shutil

# 1. Create separate leadership and creative files
if os.path.exists('leadership-creative.html'):
    shutil.copy('leadership-creative.html', 'leadership.html')
    shutil.copy('leadership-creative.html', 'creative.html')
    os.remove('leadership-creative.html')

# Fix headers in leadership and creative
with open('leadership.html', 'r', encoding='utf-8') as f:
    l_html = f.read()
l_html = l_html.replace('Leadership & Creative', 'Leadership')
l_html = l_html.replace('Vision &amp; <em>Execution</em>', 'Global <em>Leadership</em>')
with open('leadership.html', 'w', encoding='utf-8') as f:
    f.write(l_html)

with open('creative.html', 'r', encoding='utf-8') as f:
    c_html = f.read()
c_html = c_html.replace('Leadership & Creative Portfolio', 'Creative Designing Portfolio')
c_html = c_html.replace('Vision &amp; <em>Execution</em>', 'Creative <em>Designing</em>')
c_html = c_html.replace('A Track Record of <em>Leadership.</em>', 'Creative <em>Projects.</em>')
with open('creative.html', 'w', encoding='utf-8') as f:
    f.write(c_html)

# 2. Update navigation in all files
new_mobile_menu = """<div class="mobile-menu" id="mobileMenu" aria-hidden="true" role="dialog" aria-label="Navigation">
  <button class="mobile-menu-close" id="mobileClose" aria-label="Close menu">
    <span></span><span></span>
  </button>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="technology.html">Technology</a>
  <a href="business-development.html">Business Dev</a>
  <a href="communication.html">Communication</a>
  <a href="human-resources.html">Human Resources</a>
  <a href="leadership.html">Leadership</a>
  <a href="creative.html">Creative Designing</a>
  <a href="index.html#contact">Contact</a>
</div>"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = re.sub(r'<div class="mobile-menu".*?</div>', new_mobile_menu, content, flags=re.DOTALL)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# 3. Update main.js
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_old = """    const segmentDescriptions = {
      0: 'Communication<br><span style="font-size:0.8rem;opacity:0.7">Public Speaking & Confidence</span>',
      1: 'Leadership<br><span style="font-size:0.8rem;opacity:0.7">Corporate & Team Dynamics</span>',
      2: 'HR Practices<br><span style="font-size:0.8rem;opacity:0.7">Employee Engagement</span>',
      3: 'Creative Arts<br><span style="font-size:0.8rem;opacity:0.7">Content Production</span>',
      4: 'IT Projects<br><span style="font-size:0.8rem;opacity:0.7">Technical & Software</span>'
    };"""
js_new = """    const segmentDescriptions = {
      0: 'Communication<br><span style="font-size:0.8rem;opacity:0.7">Voice & Influence</span>',
      1: 'Leadership<br><span style="font-size:0.8rem;opacity:0.7">AIESEC & Beyond</span>',
      2: 'Creative<br><span style="font-size:0.8rem;opacity:0.7">Creative Designing</span>',
      3: 'HR Practices<br><span style="font-size:0.8rem;opacity:0.7">People & Culture</span>',
      4: 'Business Dev<br><span style="font-size:0.8rem;opacity:0.7">Growth & Strategy</span>',
      5: 'Technology<br><span style="font-size:0.8rem;opacity:0.7">Engineering & Architecture</span>'
    };"""
js = js.replace(js_old, js_new)
with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 4. Update index.html Donut and Bento Links
with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

donut_old = re.search(r'<svg viewBox="0 0 600 600" class="portfolio-donut".*?</svg>', index, re.DOTALL).group(0)

donut_new = """<svg viewBox="0 0 600 600" class="portfolio-donut" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern id="img-0" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/mic1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-1" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/team.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-2" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/solo-branding-1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-3" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/virtusa-training-1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-4" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/iit-business-1.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
            <pattern id="img-5" patternUnits="userSpaceOnUse" width="600" height="600">
              <image href="images/mic4.jpg" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>
            </pattern>
          </defs>
          <g class="donut-segment" data-index="0" onclick="window.location.href='communication.html'" style="--tx: 6.00px; --ty: -10.39px;">
            <path d="M 512.01 167.52 A 250 250 0 0 0 308.72 50.15 L 303.49 200.06 A 100 100 0 0 1 384.80 247.01 Z" class="donut-path" fill="url(#img-0)" />
          </g>
          <g class="donut-segment" data-index="1" onclick="window.location.href='leadership.html'" style="--tx: 12.00px; --ty: 0.00px;">
            <path d="M 520.74 417.37 A 250 250 0 0 0 520.74 182.63 L 388.29 253.05 A 100 100 0 0 1 388.29 346.95 Z" class="donut-path" fill="url(#img-1)" />
          </g>
          <g class="donut-segment" data-index="2" onclick="window.location.href='creative.html'" style="--tx: 6.00px; --ty: 10.39px;">
            <path d="M 308.72 549.85 A 250 250 0 0 0 512.01 432.48 L 384.80 352.99 A 100 100 0 0 1 303.49 399.94 Z" class="donut-path" fill="url(#img-2)" />
          </g>
          <g class="donut-segment" data-index="3" onclick="window.location.href='human-resources.html'" style="--tx: -6.00px; --ty: 10.39px;">
            <path d="M 87.99 432.48 A 250 250 0 0 0 291.28 549.85 L 296.51 399.94 A 100 100 0 0 1 215.20 352.99 Z" class="donut-path" fill="url(#img-3)" />
          </g>
          <g class="donut-segment" data-index="4" onclick="window.location.href='business-development.html'" style="--tx: -12.00px; --ty: 0.00px;">
            <path d="M 79.26 182.63 A 250 250 0 0 0 79.26 417.37 L 211.71 346.95 A 100 100 0 0 1 211.71 253.05 Z" class="donut-path" fill="url(#img-4)" />
          </g>
          <g class="donut-segment" data-index="5" onclick="window.location.href='technology.html'" style="--tx: -6.00px; --ty: -10.39px;">
            <path d="M 291.28 50.15 A 250 250 0 0 0 87.99 167.52 L 215.20 247.01 A 100 100 0 0 1 296.51 200.06 Z" class="donut-path" fill="url(#img-5)" />
          </g>
        </svg>"""

index = index.replace(donut_old, donut_new)

bento_links_old = re.search(r'<div class="bento-links".*?</div>\s*</div>', index, re.DOTALL).group(0)

bento_links_new = """<div class="bento-links" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; width:100%;">
        <a href="technology.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Technology & IT</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Full Stack Development, Data Analytics, Software Engineering.</p>
        </a>
        <a href="business-development.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Business Development</h3>
          <p style="color:var(--stone); font-size:0.9rem;">AIESEC BD, Strategic Partnerships, Growth Initiatives.</p>
        </a>
        <a href="human-resources.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Human Resources</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Employee Engagement, Culture Audit, Virtusa.</p>
        </a>
        <a href="communication.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Communication</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Corporate Training, Public Speaking, Emcee.</p>
        </a>
        <a href="leadership.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Leadership</h3>
          <p style="color:var(--stone); font-size:0.9rem;">AIESEC, Team Leadership, Awards.</p>
        </a>
        <a href="creative.html" class="bento-card" style="padding:24px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-decoration:none; transition:transform 0.3s ease, background 0.3s ease;">
          <h3 style="color:#FF6A1A; margin-bottom:8px; font-family:'Inter', sans-serif;">Creative Designing</h3>
          <p style="color:var(--stone); font-size:0.9rem;">Personal Branding, Dubbing, Visuals.</p>
        </a>
      </div>
    </div>"""

index = index.replace(bento_links_old, bento_links_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)

print("Split Leadership and Creative Designing completely.")
