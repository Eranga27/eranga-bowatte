import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change video src
html = html.replace('src="images/hero.mp4"', 'src="images/update-hero.mov"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add Section Glows
if "/* ===================== SECTION GLOWS ===================== */" not in css:
    glows = """
  /* ===================== SECTION GLOWS ===================== */
  #stats::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at 20% 50%, rgba(0, 212, 255, 0.12) 0%, transparent 60%);
    pointer-events: none; z-index: 0;
  }
  #portfolios::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at 80% 20%, rgba(255, 106, 26, 0.12) 0%, transparent 60%);
    pointer-events: none; z-index: 0;
  }
  #comm-teaser::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at 50% 80%, rgba(156, 39, 176, 0.12) 0%, transparent 60%);
    pointer-events: none; z-index: 0;
  }
  #hr-teaser::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at 10% 90%, rgba(233, 80, 80, 0.12) 0%, transparent 60%);
    pointer-events: none; z-index: 0;
  }
  #about-teaser::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at 90% 90%, rgba(255, 193, 7, 0.12) 0%, transparent 60%);
    pointer-events: none; z-index: 0;
  }
  #contact::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at 50% 10%, rgba(233, 30, 99, 0.12) 0%, transparent 60%);
    pointer-events: none; z-index: 0;
  }
  #stats, #portfolios, #comm-teaser, #hr-teaser, #about-teaser, #contact {
    position: relative;
    overflow: hidden;
  }
  #stats > *, #portfolios > *, #comm-teaser > *, #hr-teaser > *, #about-teaser > *, #contact > * {
    position: relative;
    z-index: 1;
  }
"""
    css = css + "\n" + glows

# Tighten Donut section
css = css.replace('.portfolio-circle-container {\n    width: 600px;\n    height: 600px;', '.portfolio-circle-container {\n    width: 440px;\n    height: 440px;')
# Also reduce padding further
css = css.replace('.portfolio-nav-section {\n    padding: 60px 0;\n    position: relative;\n  }', '.portfolio-nav-section {\n    padding: 40px 0;\n    position: relative;\n  }')


# Update Creative artwork background and card borders
bg_pattern = r'\.creative-images-col::before\s*\{[^}]+\}'
new_bg = """.creative-images-col::before {
    content: "";
    position: absolute;
    top: 0; left: -10%; right: -10%; bottom: 0;
    background-image: url('images/creative-art.png');
    background-size: cover;
    background-position: center;
    filter: blur(4px) brightness(0.65);
    opacity: 0.9;
    z-index: 1;
    border-radius: 20px;
    mask-image: radial-gradient(circle at center, black 40%, transparent 80%);
    -webkit-mask-image: radial-gradient(circle at center, black 40%, transparent 80%);
  }"""
css = re.sub(bg_pattern, new_bg, css)

wrapper_pattern = r'\.creative-img-wrapper\s*\{[^}]+\}'
new_wrapper = """.creative-img-wrapper {
    position: absolute;
    background-size: cover;
    background-position: center;
    box-shadow: 0 30px 60px rgba(0,0,0,0.8), inset 0 0 0 1px rgba(255,255,255,0.15);
    border-radius: 16px;
    transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.2s ease, filter 0.3s ease;
    overflow: hidden;
    cursor: pointer;
  }"""
css = re.sub(wrapper_pattern, new_wrapper, css)


with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates successful.")
