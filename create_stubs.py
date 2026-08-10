import os

template_file = "technology.html"

with open(template_file, "r", encoding="utf-8") as f:
    html = f.read()

# We want to replace the hero text and remove the iframe section
# We can just replace the <header> block and everything between <header> and <footer>

projects = [
    {"file": "eloquent-one.html", "title": "Eloquent One"},
    {"file": "smart-agri-suite.html", "title": "Smart-Agri-Suite"},
    {"file": "lanka-climate-hub.html", "title": "Lanka Climate Hub"},
    {"file": "sentinel-access.html", "title": "Sentinel Access"},
    {"file": "boam-real-estates.html", "title": "BOAM Real Estates"},
    {"file": "lyricist-journey.html", "title": "A Lyricist Journey"}
]

for p in projects:
    file_name = p["file"]
    title = p["title"]
    
    # Simple replacement string
    new_html = html.replace("<title>Technology & IT Portfolio — Eranga Bowatte</title>", f"<title>{title} — Eranga Bowatte</title>")
    new_html = new_html.replace("Engineering &amp; <em>Architecture</em>", f"<em>{title}</em>")
    new_html = new_html.replace("Full stack development, data analytics, and building scalable software solutions that bridge the gap between technical execution and user experience.", "Project details coming soon.")
    
    # Remove the iframe section entirely for the stub
    start_str = "<!-- ===================== IT PROJECTS (3D TIMELINE) ===================== -->"
    end_str = "</section>"
    
    if start_str in new_html:
        start_idx = new_html.find(start_str)
        # Find the next </section> after start_idx
        end_idx = new_html.find(end_str, start_idx) + len(end_str)
        new_html = new_html[:start_idx] + new_html[end_idx:]
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Created {file_name}")

