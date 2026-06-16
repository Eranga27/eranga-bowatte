import re

# Read the generic scaffold of human-resources.html to preserve head/nav/footer
with open('human-resources.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract top and bottom parts
top_part = re.search(r'(.*?)<!-- PAGE CONTENT -->', html, re.DOTALL).group(1)
bottom_part = re.search(r'(<footer>.*)', html, re.DOTALL).group(1)

new_content = """
<!-- ===================== HERO ===================== -->
<header class="hero" style="min-height: 60vh;">
  <div class="hero-bg">
    <img src="images/team.jpg" alt="Human Resources & People Culture">
  </div>
  <div class="container hero-content" style="padding-top: 160px; padding-bottom: 80px;">
    <div class="hero-eyebrow reveal">
      <div class="line"></div>
      <span class="label">Human Resources Portfolio</span>
    </div>
    <h1 class="headline reveal" style="animation-delay:0.1s">
      People &amp; <em>Culture</em>
    </h1>
    <p class="hero-sub reveal" style="animation-delay:0.2s">
      A deep dive into employee engagement, strategic HR operations, and building high-performance workplace cultures that put people first.
    </p>
  </div>
</header>

<!-- ===================== HR EXPERIENCE ===================== -->
<section style="padding-top: 100px; padding-bottom: 140px; background: var(--surface);">
  <div class="container">
    
    <!-- Experience 1: Virtusa -->
    <div class="story-grid reveal" style="align-items: center; margin-bottom: 120px;">
      <div class="story-text">
        <span class="label" style="display:block; margin-bottom:15px; color:#FF6A1A;">Jul 2025 — Apr 2026</span>
        <h2 style="font-family:'Poppins',sans-serif; font-size:2.5rem; margin-bottom:10px; line-height:1.2;">Virtusa Corporation</h2>
        <h3 style="font-weight: 400; color:var(--stone); margin-bottom: 30px; font-size: 1.2rem;">Business Partner Executive, HR</h3>
        <p>Managed end-to-end HR operations and employee engagement initiatives for a massive workforce of over <strong>350 employees</strong>.</p>
        <p>I played a pivotal role in driving organizational culture by spearheading Sri Lanka's <em>Great Place to Work (GPTW)</em> survey and leading comprehensive Culture Audits to ensure alignment with global standards.</p>
        
        <ul style="margin-top: 20px; color: var(--stone); list-style-type: square; padding-left: 20px; line-height: 1.8;">
          <li>End-to-End HR Operations</li>
          <li>Employee Engagement & Retention</li>
          <li>Great Place To Work (GPTW) Survey Leadership</li>
          <li>Culture Audit Execution</li>
        </ul>
      </div>
      <div class="banner-img-side" style="border-radius:12px; aspect-ratio:4/5;">
        <img src="images/virtusa-training-1.jpg" alt="HR Operations at Virtusa">
      </div>
    </div>

    <!-- Experience 2: MAS Holdings -->
    <div class="story-grid reveal" style="align-items: center; direction: rtl;">
      <div class="story-text" style="direction: ltr;">
        <span class="label" style="display:block; margin-bottom:15px; color:#FF6A1A;">Oct 2024 — Apr 2025</span>
        <h2 style="font-family:'Poppins',sans-serif; font-size:2.5rem; margin-bottom:10px; line-height:1.2;">MAS Holdings</h2>
        <h3 style="font-weight: 400; color:var(--stone); margin-bottom: 30px; font-size: 1.2rem;">Executive, Group Human Resources</h3>
        <p>Led strategic university engagement and employer branding initiatives, ensuring MAS Holdings remained the top destination for emerging talent.</p>
        <p>Bridging my technical skills with HR, I also built a brand-new <strong>Career Fair productivity dashboard</strong> from scratch, streamlining the recruitment tracking process and significantly increasing data visibility for the HR team.</p>
        
        <ul style="margin-top: 20px; color: var(--stone); list-style-type: square; padding-left: 20px; line-height: 1.8;">
          <li>Employer Branding & University Engagement</li>
          <li>Talent Acquisition Pipeline Management</li>
          <li>HR Tech: Developed Career Fair Productivity Dashboard</li>
        </ul>
      </div>
      <div class="banner-img-side" style="border-radius:12px; aspect-ratio:4/5; direction: ltr;">
        <img src="images/iit-business-1.jpg" alt="University Engagement and Branding">
      </div>
    </div>

  </div>
</section>

<!-- ===================== CTA ===================== -->
<section class="cta" id="contact" style="border-top: 1px solid var(--line);">
  <div class="container">
    <span class="label">Let's Connect</span>
    <h2>Ready to transform your <span class="accent-word">workplace?</span></h2>
    <p style="color:var(--stone); margin-top:20px; margin-bottom:40px; max-width:500px; margin-left:auto; margin-right:auto; font-size:1.1rem;">Reach out to discuss HR strategy, employee engagement, or culture building.</p>
    <div class="cta-links">
      <a class="cta-link" href="mailto:eranbwt27@gmail.com">EMAIL — eranbwt27@gmail.com</a>
      <a class="cta-link" href="https://www.linkedin.com/in/eranga-bowatte" target="_blank" rel="noopener">LINKEDIN — Eranga Bowatte</a>
    </div>
  </div>
</section>
"""

with open('human-resources.html', 'w', encoding='utf-8') as f:
    f.write(top_part + new_content + bottom_part)
print('Updated human-resources.html')
