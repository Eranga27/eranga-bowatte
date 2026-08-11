"""
Strip the Eloquent One logo img tag and the BGDark.png background from stub pages.
Replace with a clean neutral dark background so they're ready for their own branding later.
"""
import re

stubs = [
    "f:/my-portfolio/eranga-bowatte/sentinel-access.html",
    "f:/my-portfolio/eranga-bowatte/boam-real-estates.html",
    "f:/my-portfolio/eranga-bowatte/lyricist-journey.html",
]

for path in stubs:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove BGDark background-image line
    content = content.replace(
        "background-image: url('images/myportfoliopage/BGDark.png');",
        "/* project-specific background will be set per page */"
    )
    # Remove Eloquent One logo img tag
    content = re.sub(
        r'<img src="images/myportfoliopage/LogoTransparent\.png"[^>]+>\n?',
        '',
        content
    )
    # Fix wrong meta description
    content = content.replace(
        "Lanka Climate Hub - AI-powered communication coaching platform.",
        content.split('<title>')[1].split('—')[0].strip() + " — Eranga Bowatte's IT Portfolio"
    )
    # Remove Eloquent One meta og description bleed
    content = content.replace(
        'content="Communicate with Absolute Clarity. An enterprise-grade, AI-powered communication coaching platform."',
        f'content="Eranga Bowatte IT Portfolio Project Page."'
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned: {path}")
