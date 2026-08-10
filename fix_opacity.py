js_file = "3d-it-portfolio/assets/index-DDITMpZT.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# Change opacity from .8 to 1 (fully opaque) to maximize visibility
fixes = [
    ("opacity:.8", "opacity:1")
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("Patched: " + old[:30])
    else:
        print("NOT FOUND: " + old[:30])

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
