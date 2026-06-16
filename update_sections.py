import re

with open('old_index.html', 'r', encoding='utf-8') as f:
    old_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    new_html = f.read()

# 1. Extract Old Hero
old_hero = re.search(r'<!-- ===================== HERO ===================== -->.*?</header>', old_html, re.DOTALL).group(0)

# 2. Extract Old Banner Split (By the Numbers)
old_banner = re.search(r'<!-- ===================== CINEMATIC BANNER ===================== -->.*?</div>\s*</div>', old_html, re.DOTALL).group(0)
# Rename the headline in old banner
old_banner = old_banner.replace('By the Numbers', 'Fun to Know By Numbers')

# Replace Hero and Numbers in new_html
# Find current Hero in new_html
new_html = re.sub(r'<!-- ===================== HERO ===================== -->.*?</header>', old_hero, new_html, flags=re.DOTALL)
# Find current Numbers in new_html
new_html = re.sub(r'<!-- ===================== FUN TO KNOW BY NUMBERS ===================== -->.*?</div>\s*</div>\s*</div>', old_banner, new_html, flags=re.DOTALL)

# 3. Fix Portfolio Donut Section
# Change flex layout to make donut big and centered, and bento grid below it
portfolio_old = r'<div class="section-head reveal" style="text-align:center;">\s*<span class="label">Explore The Branches</span>\s*<h2>My Core <em>Disciplines</em></h2>\s*<p style="color:var\(--stone\); margin-top:20px; max-width:600px; margin-left:auto; margin-right:auto;">\s*Select a portfolio below to dive deep into my specialized experience across different industries.\s*</p>\s*</div>\s*<div style="display:flex; flex-wrap:wrap; align-items:center; gap:60px; justify-content:center;" class="reveal">'

portfolio_new = """<div class="section-head reveal" style="text-align:center;">
      <span class="label" style="display:block; margin-bottom:20px;">Explore The Branches</span>
      <h2>My Core <em>Disciplines</em></h2>
      <p style="color:var(--stone); margin-top:20px; max-width:600px; margin-left:auto; margin-right:auto;">
        Select a portfolio below to dive deep into my specialized experience across different industries.
      </p>
    </div>
    
    <div style="display:flex; flex-direction:column; align-items:center; gap:80px;" class="reveal">"""

new_html = re.sub(portfolio_old, portfolio_new, new_html, flags=re.DOTALL)

# Change bento links layout to a 2 or 3 column grid below the donut
bento_old = r'<div class="bento-links" style="display:flex; flex-direction:column; gap:16px; flex:1; min-width:300px;">'
bento_new = r'<div class="bento-links" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; width:100%;">'
new_html = new_html.replace(bento_old, bento_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# 4. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

# Extract Story and Track Record from old_html
old_story = re.search(r'<!-- ===================== THE PAUSE / STORY ===================== -->.*?</section>', old_html, re.DOTALL).group(0)
old_track_record = re.search(r'<!-- ===================== TRACK RECORD ===================== -->.*?</section>', old_html, re.DOTALL).group(0)

# Replace the "Content coming soon" in about.html with these sections
content_placeholder = r'<!-- PAGE CONTENT -->\n  <div style="padding-top: 140px; text-align: center; min-height: 70vh;">\n    <h1>About Me</h1>\n    <p>Content coming soon...</p>\n  </div>'
new_about_content = f"<!-- PAGE CONTENT -->\n{old_story}\n\n{old_track_record}"
about_html = about_html.replace(content_placeholder, new_about_content)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

print('Updated index.html and about.html')
