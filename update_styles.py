import re

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the preloader animation
pattern_preloader = r"(\.signature-text\s*\{[^\}]*\})(.+?)(\@keyframes\s+revealSignature)"
# Wait, let's just replace the signature-text animation and add drawUnderline
def replace_signature(match):
    sig = match.group(1)
    # Add ::after
    sig_after = "\n  .signature-text::after {\n    content: '';\n    position: absolute;\n    bottom: -5px;\n    left: 0;\n    width: 100%;\n    height: 3px;\n    background: linear-gradient(90deg, transparent, #FF8C00, transparent);\n    transform: scaleX(0);\n    transform-origin: left;\n    animation: drawUnderline 1.2s cubic-bezier(0.4, 0.0, 0.2, 1) forwards 3.0s;\n  }\n\n  @keyframes drawUnderline {\n    0% { transform: scaleX(0); }\n    100% { transform: scaleX(1); }\n  }\n"
    return sig + sig_after + match.group(2) + match.group(3)

content = re.sub(pattern_preloader, replace_signature, content, flags=re.DOTALL)

# Replace .nav-toggle desktop hiding (first block)
content = content.replace("  .nav-toggle{\n    display:none;", "  .nav-toggle{\n    display:flex;")
content = content.replace("  /* Hamburger button — hidden on desktop */", "  /* Hamburger button */")

# Remove .nav-toggle{ display:flex; } from media queries
content = content.replace("    .nav-toggle{ display:flex; }\n", "")

# We have TWO blocks of .mobile-menu definitions. One around line 476, one around line 2232.
# They are almost identical. We will replace both.
mobile_menu_pattern = re.compile(r'\s*/\*\s*---------- Mobile full-screen menu overlay.*?\@keyframes linkSlideIn\{\s*from\{\s*opacity:0;\s*transform:translateX\(28px\);\s*\}\s*to\s*\{\s*opacity:0\.55;\s*transform:translateX\(0\);\s*\}\s*\}\s*\}', re.DOTALL)

sidebar_css = """
  /* ---------- Contents Box (Sidebar) ---------- */
  .mobile-menu{
    display:flex;
    position:fixed;
    top:0; bottom:0; left:0;
    width: 320px;
    max-width: 100vw;
    z-index:150;
    background: rgba(11, 10, 9, 0.65);
    backdrop-filter: blur(32px);
    -webkit-backdrop-filter: blur(32px);
    flex-direction:column;
    justify-content:center;
    align-items:flex-start;
    gap:28px;
    transform:translateX(-100%);
    transition:transform 0.42s cubic-bezier(0.4,0,0.2,1);
    padding:80px 40px;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
  }

  .mobile-menu.open{
    transform:translateX(0);
  }
  
  .mobile-menu a{
    font-family:'Space Mono',monospace;
    font-size:1.05rem;
    letter-spacing:0.22em;
    text-transform:uppercase;
    text-decoration:none;
    color:var(--paper);
    opacity:0.55;
    position:relative;
    transition:opacity 0.2s ease, color 0.2s ease;
  }
  .mobile-menu a::after{
    content:'';
    position:absolute;
    bottom:-5px; left:0; right:0;
    height:1px;
    background:#FF6A1A;
    transform:scaleX(0);
    transform-origin:left;
    transition:transform 0.3s ease;
  }
  .mobile-menu a:hover,
  .mobile-menu a:focus{
    opacity:1;
    color:#FF6A1A;
  }
  .mobile-menu a:hover::after{
    transform:scaleX(1);
  }
  
  .mobile-menu-close{
    position:absolute;
    top:24px; right:28px;
    background:none;
    border:none;
    cursor:pointer;
    display:flex;
    flex-direction:column;
    gap:0;
    padding:6px;
    opacity:0.6;
    transition:opacity 0.2s;
  }
  .mobile-menu-close:hover{ opacity:1; }
  .mobile-menu-close span{
    display:block;
    width:22px; height:1.5px;
    background:var(--paper);
    border-radius:2px;
  }
  .mobile-menu-close span:nth-child(1){ transform:translateY(0.75px) rotate(45deg); }
  .mobile-menu-close span:nth-child(2){ transform:translateY(-0.75px) rotate(-45deg); }
  
  .mobile-menu.open a{
    animation:linkSlideIn 0.35s ease both;
  }
  .mobile-menu.open a:nth-child(2){ animation-delay:0.05s; }
  .mobile-menu.open a:nth-child(3){ animation-delay:0.10s; }
  .mobile-menu.open a:nth-child(4){ animation-delay:0.15s; }
  .mobile-menu.open a:nth-child(5){ animation-delay:0.20s; }
  .mobile-menu.open a:nth-child(6){ animation-delay:0.25s; }
  .mobile-menu.open a:nth-child(7){ animation-delay:0.30s; }
  .mobile-menu.open a:nth-child(8){ animation-delay:0.35s; }
  .mobile-menu.open a:nth-child(9){ animation-delay:0.40s; }
  
  @keyframes linkSlideIn{
    from{ opacity:0; transform:translateX(-28px); }
    to  { opacity:0.55; transform:translateX(0); }
  }
"""

content = mobile_menu_pattern.sub(sidebar_css, content)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated styles.css")

with open('main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

main_js = main_js.replace("}, 3200);", "}, 4800);")

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)
print("Updated main.js")
