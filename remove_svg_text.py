import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove text tags inside SVG
html = re.sub(r'<text [^>]*class="donut-text"[^>]*>.*?</text>\s*', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done')
