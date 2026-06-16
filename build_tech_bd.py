import re

# Read the generic scaffold of technology.html to preserve head/nav/footer
with open('technology.html', 'r', encoding='utf-8') as f:
    tech_html = f.read()

top_part_tech = re.search(r'(.*?)<!-- PAGE CONTENT -->', tech_html, re.DOTALL).group(1)
bottom_part_tech = re.search(r'(<footer>.*)', tech_html, re.DOTALL).group(1)

new_tech_content = """
<!-- ===================== HERO ===================== -->
<header class="hero" style="min-height: 60vh;">
  <div class="hero-bg">
    <img src="images/solo-branding-1.jpg" alt="Technology & Engineering">
  </div>
  <div class="container hero-content" style="padding-top: 160px; padding-bottom: 80px;">
    <div class="hero-eyebrow reveal">
      <div class="line"></div>
      <span class="label">Technology & IT Portfolio</span>
    </div>
    <h1 class="headline reveal" style="animation-delay:0.1s">
      Engineering &amp; <em>Architecture</em>
    </h1>
    <p class="hero-sub reveal" style="animation-delay:0.2s">
      Full stack development, data analytics, and building scalable software solutions that bridge the gap between technical execution and user experience.
    </p>
  </div>
</header>

<!-- ===================== TECH BACKGROUND ===================== -->
<section style="padding-top: 100px; padding-bottom: 100px; background: var(--surface);">
  <div class="container">
    <div class="story-grid reveal" style="align-items: center; margin-bottom: 80px;">
      <div class="story-text">
        <span class="label" style="display:block; margin-bottom:15px; color:#FF6A1A;">The Foundation</span>
        <h2 style="font-family:'Poppins',sans-serif; font-size:2.5rem; margin-bottom:20px; line-height:1.2;">Building systems that scale.</h2>
        <p>With over 10+ technology projects delivered, my approach to software engineering is rooted in a deep understanding of business requirements. I don't just write code; I architect solutions that solve real-world problems.</p>
        <p>Currently pursuing my BSc in Information Technology (Hons.) at SLIIT, alongside professional certifications from industry giants like IBM and Google.</p>
      </div>
      
      <!-- Credentials List -->
      <div class="creds-list" style="width: 100%; border-left: 1px solid var(--line); padding-left: 40px;">
        <div class="creds-row" style="padding: 20px 0; border-bottom: 1px solid var(--line);">
          <span class="c-name" style="display:block; font-size: 1.1rem; color: var(--paper); margin-bottom: 5px;">BSc in Information Technology (Hons.)</span>
          <span class="c-org" style="color: var(--stone); font-size: 0.9rem;">SLIIT Malabe (2022–Present)</span>
        </div>
        <div class="creds-row" style="padding: 20px 0; border-bottom: 1px solid var(--line);">
          <span class="c-name" style="display:block; font-size: 1.1rem; color: var(--paper); margin-bottom: 5px;">Full Stack Developer — Software Engineering</span>
          <span class="c-org" style="color: var(--stone); font-size: 0.9rem;">IBM Professional Certificate (In Progress)</span>
        </div>
        <div class="creds-row" style="padding: 20px 0;">
          <span class="c-name" style="display:block; font-size: 1.1rem; color: var(--paper); margin-bottom: 5px;">Data Analytics — Professional Certificate</span>
          <span class="c-org" style="color: var(--stone); font-size: 0.9rem;">Google (In Progress)</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===================== CTA ===================== -->
<section class="cta" id="contact" style="border-top: 1px solid var(--line);">
  <div class="container">
    <span class="label">Let's Connect</span>
    <h2>Need a <span class="accent-word">technical partner?</span></h2>
    <p style="color:var(--stone); margin-top:20px; margin-bottom:40px; max-width:500px; margin-left:auto; margin-right:auto; font-size:1.1rem;">Whether it's full-stack development or data-driven insights, let's build something exceptional.</p>
    <div class="cta-links">
      <a class="cta-link" href="mailto:eranbwt27@gmail.com">EMAIL — eranbwt27@gmail.com</a>
      <a class="cta-link" href="https://www.linkedin.com/in/eranga-bowatte" target="_blank" rel="noopener">LINKEDIN — Eranga Bowatte</a>
    </div>
  </div>
</section>
"""

with open('technology.html', 'w', encoding='utf-8') as f:
    f.write(top_part_tech + new_tech_content + bottom_part_tech)

# Read the generic scaffold of business-development.html
with open('business-development.html', 'r', encoding='utf-8') as f:
    bd_html = f.read()

top_part_bd = re.search(r'(.*?)<!-- PAGE CONTENT -->', bd_html, re.DOTALL).group(1)
bottom_part_bd = re.search(r'(<footer>.*)', bd_html, re.DOTALL).group(1)

new_bd_content = """
<!-- ===================== HERO ===================== -->
<header class="hero" style="min-height: 60vh;">
  <div class="hero-bg">
    <img src="images/iit-business-1.jpg" alt="Business Development">
  </div>
  <div class="container hero-content" style="padding-top: 160px; padding-bottom: 80px;">
    <div class="hero-eyebrow reveal">
      <div class="line"></div>
      <span class="label">Business Development Portfolio</span>
    </div>
    <h1 class="headline reveal" style="animation-delay:0.1s">
      Growth &amp; <em>Strategy</em>
    </h1>
    <p class="hero-sub reveal" style="animation-delay:0.2s">
      Strategic partnerships, global account delivery, and driving business expansion at an international scale.
    </p>
  </div>
</header>

<!-- ===================== BD EXPERIENCE ===================== -->
<section style="padding-top: 100px; padding-bottom: 140px; background: var(--surface);">
  <div class="container">
    
    <!-- Experience 1: AIESEC International -->
    <div class="story-grid reveal" style="align-items: center; margin-bottom: 120px;">
      <div class="story-text">
        <span class="label" style="display:block; margin-bottom:15px; color:#FF6A1A;">Dec 2025 — Present</span>
        <h2 style="font-family:'Poppins',sans-serif; font-size:2.5rem; margin-bottom:10px; line-height:1.2;">AIESEC International</h2>
        <h3 style="font-weight: 400; color:var(--stone); margin-bottom: 30px; font-size: 1.2rem;">Global Account Delivery Manager</h3>
        <p>Operating within AIESEC's Global Support Team, I manage business development and account delivery across multiple country teams.</p>
        <p>My role involves aligning international delegations, ensuring seamless delivery of global accounts, and driving continuous growth through strategic relationship management.</p>
      </div>
      <div class="banner-img-side" style="border-radius:12px; aspect-ratio:4/5;">
        <img src="images/team.jpg" alt="AIESEC Global Support Team">
      </div>
    </div>

    <!-- Experience 2: AIESEC International Congress -->
    <div class="story-grid reveal" style="align-items: center; direction: rtl; margin-bottom: 80px;">
      <div class="story-text" style="direction: ltr;">
        <span class="label" style="display:block; margin-bottom:15px; color:#FF6A1A;">Oct 2025 — Feb 2026</span>
        <h2 style="font-family:'Poppins',sans-serif; font-size:2.5rem; margin-bottom:10px; line-height:1.2;">AIESEC International Congress (UAE)</h2>
        <h3 style="font-weight: 400; color:var(--stone); margin-bottom: 30px; font-size: 1.2rem;">Head of Business Development</h3>
        <p>Serving as the Core Committee Vice President for Business Development (CCVP BD) for the highly anticipated International Congress 2026 in the UAE.</p>
        <p>Responsible for coordinating delegations across global chapters, securing strategic partnerships, and managing the core BD pipeline for one of the largest youth leadership conferences in the world.</p>
      </div>
      <div class="banner-img-side" style="border-radius:12px; aspect-ratio:4/5; direction: ltr;">
        <img src="images/journey-glimpse.jpg" alt="AIESEC International Congress UAE">
      </div>
    </div>
    
    <!-- Credentials -->
    <div class="reveal" style="border-top: 1px solid var(--line); padding-top: 60px;">
        <div class="creds-row" style="display:flex; justify-content:space-between; padding: 20px 0;">
          <span class="c-name" style="font-size: 1.1rem; color: var(--paper);">Sales Operations Professional — Certificate</span>
          <span class="c-org" style="color: var(--stone); font-size: 0.9rem;">Salesforce (In Progress)</span>
        </div>
        <div class="creds-row" style="display:flex; justify-content:space-between; padding: 20px 0;">
          <span class="c-name" style="font-size: 1.1rem; color: var(--paper);">Brand Identity &amp; Strategy — Professional Certification</span>
          <span class="c-org" style="color: var(--stone); font-size: 0.9rem;">IE Business School</span>
        </div>
    </div>

  </div>
</section>

<!-- ===================== CTA ===================== -->
<section class="cta" id="contact" style="border-top: 1px solid var(--line);">
  <div class="container">
    <span class="label">Let's Connect</span>
    <h2>Ready to drive <span class="accent-word">growth?</span></h2>
    <p style="color:var(--stone); margin-top:20px; margin-bottom:40px; max-width:500px; margin-left:auto; margin-right:auto; font-size:1.1rem;">Reach out to discuss strategic partnerships, sales operations, and global business development.</p>
    <div class="cta-links">
      <a class="cta-link" href="mailto:eranbwt27@gmail.com">EMAIL — eranbwt27@gmail.com</a>
      <a class="cta-link" href="https://www.linkedin.com/in/eranga-bowatte" target="_blank" rel="noopener">LINKEDIN — Eranga Bowatte</a>
    </div>
  </div>
</section>
"""

with open('business-development.html', 'w', encoding='utf-8') as f:
    f.write(top_part_bd + new_bd_content + bottom_part_bd)

print('Updated technology.html and business-development.html')
