"""
1. Add cursor-dot + cursor-ring divs to all project pages
2. Fix Lanka Climate Hub parallax so it doesn't fight the preloader z-index
"""
import re

project_pages = [
    "f:/my-portfolio/eranga-bowatte/eloquent-one.html",
    "f:/my-portfolio/eranga-bowatte/lanka-climate-hub.html",
    "f:/my-portfolio/eranga-bowatte/sentinel-access.html",
    "f:/my-portfolio/eranga-bowatte/boam-real-estates.html",
    "f:/my-portfolio/eranga-bowatte/lyricist-journey.html",
]

CURSOR_HTML = '<div class="cursor-dot" id="cursorDot"></div>\n<div class="cursor-ring" id="cursorRing"></div>\n'

for path in project_pages:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject cursor elements right after <body> (or after parallax-bg if present)
    if 'cursorDot' not in content:
        # Insert after the parallax-bg div if it exists, else after <body>
        if 'id="parallax-bg"' in content:
            content = content.replace(
                '<div id="parallax-bg"></div>\n',
                '<div id="parallax-bg"></div>\n' + CURSOR_HTML
            )
        else:
            content = content.replace('<body>\n', '<body>\n' + CURSOR_HTML)
        print(f"Added cursor to: {path}")
    else:
        print(f"Cursor already present: {path}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ----
# Fix Lanka Climate Hub specifically:
# The parallax-bg is position:fixed at z-index:0 but the preloader from styles.css
# is also position:fixed — we need to make parallax-bg stay BEHIND the preloader.
# The preloader in styles.css has a very high z-index (9999 or similar).
# The issue is the `body > *:not(#parallax-bg) { position:relative; z-index:1 }` rule
# creates a stacking context that traps the preloader at z:1.
# Fix: give preloader explicit z-index:9999 inline and remove the blanket body>* rule.

lch = "f:/my-portfolio/eranga-bowatte/lanka-climate-hub.html"
with open(lch, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the problematic body > *:not rule
content = content.replace(
    "  /* Ensure all direct children of body stack above the parallax bg */\n  body > *:not(#parallax-bg) {\n    position: relative;\n    z-index: 1;\n  }",
    """  /* All content sits above the parallax background */
  nav, header, main, section, footer,
  .preloader, .mobile-menu, #lightbox,
  .cursor-dot, .cursor-ring {
    position: relative;
    z-index: 2;
  }
  /* Preloader gets maximum priority */
  .preloader { z-index: 9999 !important; }"""
)

with open(lch, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed stacking context on Lanka Climate Hub")
