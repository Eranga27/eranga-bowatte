import os, glob, re

new_nav_html = """<nav>
  <button class="nav-toggle" id="navToggle" aria-label="Open menu">
    <span></span><span></span><span></span>
  </button>
  <div class="nav-links" style="align-items: center;">
    <a href="about.html">About</a>
    <a href="index.html" class="logo" aria-label="Home">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
    </a>
    <a href="index.html#portfolios">Portfolios</a>
    <a href="index.html#contact">Contact</a>
  </div>
  <button class="audio-toggle" id="audioToggle" aria-label="Toggle background music">
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-music"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
    <div class="audio-bars">
      <span></span><span></span><span></span>
    </div>
  </button>
</nav>"""

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = re.compile(r'<nav>.*?</nav>', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(new_nav_html, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
