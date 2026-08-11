import os
import re

source_file = "f:/my-portfolio/eranga-bowatte/eloquent-one.html"
with open(source_file, "r", encoding="utf-8") as f:
    template = f.read()

projects = [
    {
        "file": "f:/my-portfolio/eranga-bowatte/lanka-climate-hub.html",
        "title": "Lanka Climate Hub",
        "sub": "Climate Intelligence Platform",
        "link": "#",
        "logo": "images/myportfoliopage/LogoTransparent.png",
        "bg": "images/myportfoliopage/BGDark.png"
    },
    {
        "file": "f:/my-portfolio/eranga-bowatte/sentinel-access.html",
        "title": "Sentinel Access",
        "sub": "Intelligent Access Control System",
        "link": "#",
        "logo": "images/myportfoliopage/LogoTransparent.png",
        "bg": "images/myportfoliopage/BGDark.png"
    },
    {
        "file": "f:/my-portfolio/eranga-bowatte/boam-real-estates.html",
        "title": "BOAM Real Estates",
        "sub": "Real Estates Platform",
        "link": "#",
        "logo": "images/myportfoliopage/LogoTransparent.png",
        "bg": "images/myportfoliopage/BGDark.png"
    },
    {
        "file": "f:/my-portfolio/eranga-bowatte/lyricist-journey.html",
        "title": "A Lyricist Journey",
        "sub": "Kamila Ratnayake's Lyricist Portfolio",
        "link": "#",
        "logo": "images/myportfoliopage/LogoTransparent.png",
        "bg": "images/myportfoliopage/BGDark.png"
    }
]

for p in projects:
    content = template
    # Replace Titles
    content = content.replace("Eloquent One", p["title"])
    content = content.replace("Communicate with<br>Absolute Clarity.", p["title"])
    
    # Replace Subtitle (the long paragraph)
    sub_pattern = r'<p class="project-subheadline">.*?</p>'
    content = re.sub(sub_pattern, f'<p class="project-subheadline">{p["sub"]}</p>', content, flags=re.DOTALL)
    
    # Replace Link
    link_pattern = r'href="https://comms-app-lq2e.vercel.app/"'
    content = re.sub(link_pattern, f'href="{p["link"]}"', content)
    
    # Replace specific features text with generic placeholders
    content = re.sub(r'<h3>Live Telemetry Engine</h3>.*?</div>', f'<h3>Feature One</h3>\n        <p><strong>Detail:</strong> Add your project specific feature description here.</p>\n      </div>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>NLP Coaching Engine</h3>.*?</div>', f'<h3>Feature Two</h3>\n        <p><strong>Detail:</strong> Add your project specific feature description here.</p>\n      </div>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>Dashboard Intelligence</h3>.*?</div>', f'<h3>Feature Three</h3>\n        <p><strong>Detail:</strong> Add your project specific feature description here.</p>\n      </div>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>Goal-Oriented Practice</h3>.*?</div>', f'<h3>Feature Four</h3>\n        <p><strong>Detail:</strong> Add your project specific feature description here.</p>\n      </div>', content, flags=re.DOTALL)
    
    # Replace Who is it for text
    content = re.sub(r'<h3>Executives & Founders</h3>.*?</div>', f'<h3>Target Group 1</h3>\n        <p>Add description.</p>\n      </div>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>Sales Professionals</h3>.*?</div>', f'<h3>Target Group 2</h3>\n        <p>Add description.</p>\n      </div>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>Job Seekers</h3>.*?</div>', f'<h3>Target Group 3</h3>\n        <p>Add description.</p>\n      </div>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>Public Speakers</h3>.*?</div>', f'<h3>Target Group 4</h3>\n        <p>Add description.</p>\n      </div>', content, flags=re.DOTALL)

    # Save
    with open(p["file"], "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Generated {p['title']}")
