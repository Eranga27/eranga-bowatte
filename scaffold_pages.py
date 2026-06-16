import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the head, nav, and footer to use as a template
head = re.search(r'<!DOCTYPE html>.*?<body>', html, re.DOTALL).group(0)
nav = re.search(r'<nav>.*?</nav>', html, re.DOTALL).group(0)
mobile_menu = re.search(r'<div class="mobile-menu".*?</div>', html, re.DOTALL).group(0)
footer = re.search(r'<footer>.*?</footer>', html, re.DOTALL).group(0)
scripts = re.search(r'<!-- ===================== LIGHTBOX ===================== -->.*</html>', html, re.DOTALL).group(0)

template = head + '\n' + nav + '\n' + mobile_menu + '\n\n  <!-- PAGE CONTENT -->\n  <div style="padding-top: 140px; text-align: center; min-height: 70vh;">\n    <h1>{TITLE}</h1>\n    <p>Content coming soon...</p>\n  </div>\n\n' + footer + '\n' + scripts

pages = {
    'about.html': 'About Me',
    'technology.html': 'Technology & IT Portfolio',
    'communication.html': 'Communication Portfolio',
    'human-resources.html': 'Human Resources Portfolio',
    'business-development.html': 'Business Development Portfolio',
    'leadership-creative.html': 'Leadership & Creative Portfolio'
}

for filename, title in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template.replace('{TITLE}', title))
print('Scaffolded 6 new branch pages.')
