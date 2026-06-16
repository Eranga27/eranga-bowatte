import re

new_nav = """<nav>
  <a href="index.html" class="logo">EB.</a>
  <div class="nav-links">
    <a href="about.html">About</a>
    <a href="index.html#portfolios">Portfolios</a>
    <a href="index.html#contact">Contact</a>
  </div>
  <button class="audio-toggle" id="audioToggle" aria-label="Toggle background music">
    <div class="audio-bars">
      <span></span><span></span><span></span>
    </div>
    <span class="audio-text">Sound</span>
  </button>
  <button class="nav-toggle" id="navToggle" aria-label="Open menu">
    <span></span><span></span><span></span>
  </button>
</nav>"""

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
  <a href="leadership-creative.html">Leadership & Creative</a>
  <a href="index.html#contact">Contact</a>
</div>"""

with open('communication.html', 'r', encoding='utf-8') as file:
    content = file.read()
    
content = re.sub(r'<nav>.*?</nav>', new_nav, content, flags=re.DOTALL)
content = re.sub(r'<div class="mobile-menu".*?</div>', new_mobile_menu, content, flags=re.DOTALL)

with open('communication.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Updated nav in communication.html")
