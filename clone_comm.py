import re

with open('experience.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update page titles and Hero text
html = re.sub(r'<title>.*?</title>', '<title>Voice & Influence — Communication Portfolio</title>', html)

hero_h1_old = r'<h1 class="headline">The Work / <em>Experience</em></h1>'
hero_h1_new = r'<h1 class="headline">Voice &amp; <em>Influence</em></h1>'
html = html.replace('<h1 class="headline">The Work / <em>Experience</em></h1>', '<h1 class="headline">Voice &amp; <em>Influence</em></h1>')

hero_sub_old = r'<p class="hero-sub">A deep dive into the corporate trainings, workshops, and speaking engagements that define my journey.</p>'
hero_sub_new = r'<p class="hero-sub">A deep dive into the corporate trainings, public speaking, and stage mastery that define my communication portfolio.</p>'
html = html.replace(hero_sub_old, hero_sub_new)

# Fix the 'Experience' breadcrumb or label if any
html = html.replace('<span class="label">Experience Portfolio</span>', '<span class="label">Communication Portfolio</span>')

with open('communication.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Copied to communication.html')
